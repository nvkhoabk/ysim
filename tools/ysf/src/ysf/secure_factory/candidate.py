"""Build-once candidate creation and non-rebuilding verification."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

from ysf.secure_factory.environment import require_output_outside_checkout
from ysf.secure_factory.evidence import (
    build_manifest,
    sha256_file,
    verify_manifest,
    write_exclusive,
)
from ysf.secure_factory.models import FactoryFailure, FileDigest, GateResult
from ysf.secure_factory.policy import validate_relative_path
from ysf.secure_factory.sensitive import require_no_sensitive_values

REQUIRED_CANDIDATE_FILES: frozenset[str] = frozenset(
    {
        "artifact-manifest.json",
        "SHA256SUMS",
        "sbom.cdx.json",
        "provenance.json",
        "reports/gates.json",
        "reports/test-and-coverage.json",
        "reports/lint-type-sast-dependency.json",
        "reports/leak-scan.json",
        "environment-identity.json",
        "execution-ledger.jsonl",
    }
)
REQUIRED_REPORT_INPUTS: tuple[str, ...] = (
    "test-and-coverage.json",
    "lint-type-sast-dependency.json",
    "leak-scan.json",
    "environment-identity.json",
    "execution-ledger.jsonl",
)
_LOCK_LINE = re.compile(r"^([A-Za-z0-9_.-]+)==([^\s;\\]+)")


def _json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")


def _parse_lock_components(lock_paths: Iterable[Path]) -> list[dict[str, str]]:
    components: dict[str, str] = {}
    for path in lock_paths:
        for line in path.read_text(encoding="utf-8").splitlines():
            match = _LOCK_LINE.match(line.strip())
            if match:
                name = match.group(1).lower().replace("_", "-")
                version = match.group(2)
                existing = components.get(name)
                if existing is not None and existing != version:
                    raise FactoryFailure(
                        "FAIL_LOCK_CONFLICT",
                        "Dependency lock contains conflicting package versions.",
                    )
                components[name] = version
    if not components:
        raise FactoryFailure("FAIL_LOCK_EMPTY", "Dependency lock contains no packages.")
    return [
        {
            "type": "library",
            "name": name,
            "version": version,
            "purl": f"pkg:pypi/{name}@{version}",
        }
        for name, version in sorted(components.items())
    ]


def write_reproducible_zip(
    output_path: Path,
    files: Mapping[str, bytes],
    *,
    source_date_epoch: int,
) -> None:
    """Write deterministic ZIP bytes for synthetic verification fixtures."""

    source_date_epoch = max(source_date_epoch, 315532800)
    import time

    timestamp = time.gmtime(source_date_epoch)[:6]
    if output_path.exists():
        raise FactoryFailure("FAIL_SECOND_BUILD", "Candidate output already exists.")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        output_path, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name in sorted(files):
            normalized = validate_relative_path(name)
            info = zipfile.ZipInfo(normalized, timestamp)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, files[name])


def _write_candidate_metadata(
    candidate_dir: Path,
    *,
    repository: str,
    commit: str,
    tree: str,
    contract_sha256: str,
    source_date_epoch: int,
    lock_paths: Iterable[Path],
    gate_report: Mapping[str, Any],
    report_root: Path,
) -> None:
    reports = candidate_dir / "reports"
    reports.mkdir(mode=0o750)
    write_exclusive(reports / "gates.json", _json_bytes(gate_report))
    for name in REQUIRED_REPORT_INPUTS:
        source = report_root / name
        if source.is_symlink() or not source.is_file() or source.stat().st_nlink != 1:
            raise FactoryFailure(
                "FAIL_CANDIDATE_REPORT_BUNDLE",
                "Candidate quality report bundle is incomplete or unsafe.",
                details={"report": name},
            )
        destination = (
            candidate_dir / name
            if name in {"environment-identity.json", "execution-ledger.jsonl"}
            else reports / name
        )
        write_exclusive(destination, source.read_bytes())
    sbom = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "version": 1,
        "metadata": {"component": {"type": "application", "name": "ysf", "version": "0.1.0"}},
        "components": _parse_lock_components(lock_paths),
    }
    write_exclusive(candidate_dir / "sbom.cdx.json", _json_bytes(sbom))
    wheels = sorted((candidate_dir / "artifacts").glob("*.whl"))
    if len(wheels) != 1:
        raise FactoryFailure("FAIL_WHEEL_COUNT", "Candidate must contain exactly one wheel.")
    provenance = {
        "_type": "https://in-toto.io/Statement/v1",
        "subject": [
            {
                "name": f"artifacts/{wheels[0].name}",
                "digest": {"sha256": sha256_file(wheels[0])},
            }
        ],
        "predicateType": "https://slsa.dev/provenance/v1",
        "predicate": {
            "buildDefinition": {
                "buildType": "https://ysim.vn/build-types/v3-r1-s00/ysf-wheel/v1",
                "externalParameters": {"contract_sha256": contract_sha256},
                "resolvedDependencies": [
                    {
                        "uri": f"git+https://github.com/{repository}@{commit}",
                        "digest": {"gitTree": tree},
                    }
                ],
            },
            "runDetails": {
                "builder": {"id": "https://github.com/actions/runner"},
                "metadata": {
                    "invocationId": f"{commit}:{tree}",
                    "startedOnEpoch": source_date_epoch,
                    "finishedOnEpoch": source_date_epoch,
                },
            },
        },
    }
    write_exclusive(candidate_dir / "provenance.json", _json_bytes(provenance))
    manifest_paths = [
        str(path.relative_to(candidate_dir).as_posix())
        for path in candidate_dir.rglob("*")
        if path.is_file()
    ]
    manifest = [record.to_dict() for record in build_manifest(candidate_dir, manifest_paths)]
    write_exclusive(candidate_dir / "artifact-manifest.json", _json_bytes(manifest))
    checksum_paths = sorted(manifest_paths + ["artifact-manifest.json"])
    checksum_text = "".join(
        f"{sha256_file(candidate_dir / path)}  {path}\n" for path in checksum_paths
    )
    write_exclusive(candidate_dir / "SHA256SUMS", checksum_text.encode("ascii"))


def build_candidate(
    repository_root: Path,
    candidate_dir: Path,
    *,
    repository: str,
    commit: str,
    tree: str,
    contract_sha256: str,
    source_date_epoch: int,
    gate_report: Mapping[str, Any],
    report_root: Path,
) -> GateResult:
    """Build exactly one wheel and bind all generated evidence to it."""

    try:
        report_root = require_output_outside_checkout(repository_root, report_root).resolve(
            strict=True
        )
    except OSError as exc:
        raise FactoryFailure(
            "FAIL_CANDIDATE_REPORT_BUNDLE",
            "Candidate quality report root is unavailable.",
        ) from exc
    try:
        candidate_dir.mkdir(parents=True, mode=0o750)
    except FileExistsError as exc:
        raise FactoryFailure("FAIL_SECOND_BUILD", "Candidate directory already exists.") from exc
    artifacts = candidate_dir / "artifacts"
    artifacts.mkdir(mode=0o750)
    environment = dict(os.environ)
    environment.update(
        {
            "PYTHONHASHSEED": "0",
            "SOURCE_DATE_EPOCH": str(source_date_epoch),
        }
    )
    try:
        with tempfile.TemporaryDirectory(
            prefix="ysim-v3-r1-s00-build-source."
        ) as temporary_directory:
            temporary_root = require_output_outside_checkout(
                repository_root, Path(temporary_directory)
            )
            build_source = temporary_root / "ysf"
            shutil.copytree(
                repository_root / "tools/ysf",
                build_source,
                symlinks=True,
            )
            if any(path.is_symlink() for path in build_source.rglob("*")):
                raise FactoryFailure(
                    "FAIL_CANDIDATE_SOURCE_SYMLINK",
                    "Candidate build source contains a symbolic link.",
                )
            process = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "build",
                    "--wheel",
                    "--no-isolation",
                    "--outdir",
                    str(artifacts),
                    str(build_source),
                ],
                cwd=temporary_root,
                env=environment,
                check=False,
                capture_output=True,
                text=True,
            )
    except OSError as exc:
        raise FactoryFailure(
            "FAIL_CANDIDATE_SOURCE_COPY",
            "Candidate build source could not be copied to disposable storage.",
        ) from exc
    if process.returncode != 0:
        raise FactoryFailure(
            "FAIL_CANDIDATE_BUILD",
            "Build-once wheel command failed.",
            details={"exit_code": process.returncode},
        )
    _write_candidate_metadata(
        candidate_dir,
        repository=repository,
        commit=commit,
        tree=tree,
        contract_sha256=contract_sha256,
        source_date_epoch=source_date_epoch,
        lock_paths=(
            repository_root / "tools/ysf/requirements-s00-build.lock",
            repository_root / "tools/ysf/requirements-s00-dev.lock",
        ),
        gate_report=gate_report,
        report_root=report_root,
    )
    require_no_sensitive_values(path for path in candidate_dir.rglob("*") if path.is_file())
    verify_candidate(candidate_dir)
    return GateResult(
        gate="build_candidate",
        result="PASS",
        message="One checksummed provenance-bound ysf wheel was built.",
        details={"candidate_path": str(candidate_dir)},
    )


def _load_manifest(path: Path) -> list[FileDigest]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(raw, list):
            raise TypeError
        return [
            FileDigest(
                relative_path=str(item["relative_path"]),
                byte_size=int(item["byte_size"]),
                sha256=str(item["sha256"]),
            )
            for item in raw
        ]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise FactoryFailure("FAIL_MANIFEST_FORMAT", "Artifact manifest is invalid.") from exc


def _verify_checksums(candidate_dir: Path) -> set[str]:
    try:
        lines = (candidate_dir / "SHA256SUMS").read_text(encoding="ascii").splitlines()
    except OSError as exc:
        raise FactoryFailure(
            "FAIL_CHECKSUMS_MISSING", "Candidate checksums are unavailable."
        ) from exc
    seen: set[str] = set()
    for line in lines:
        if len(line) < 67 or line[64:66] != "  ":
            raise FactoryFailure("FAIL_CHECKSUM_FORMAT", "Candidate checksum record is invalid.")
        digest, relative = line[:64], validate_relative_path(line[66:])
        if not re.fullmatch(r"[0-9a-f]{64}", digest) or relative in seen:
            raise FactoryFailure("FAIL_CHECKSUM_FORMAT", "Candidate checksum record is invalid.")
        seen.add(relative)
        if sha256_file(candidate_dir / relative) != digest:
            raise FactoryFailure(
                "FAIL_CANDIDATE_TAMPER",
                "Candidate checksum mismatch detected.",
                details={"path": relative},
            )
    return seen


def verify_candidate(candidate_dir: Path) -> GateResult:
    """Verify exact candidate bytes without rebuilding or installing them."""

    try:
        candidate_is_symlink = candidate_dir.is_symlink()
        root = candidate_dir.resolve(strict=True)
    except OSError as exc:
        raise FactoryFailure(
            "FAIL_CANDIDATE_PATH", "Candidate path is not a regular directory."
        ) from exc
    if candidate_is_symlink or not root.is_dir():
        raise FactoryFailure("FAIL_CANDIDATE_PATH", "Candidate path is not a regular directory.")
    files = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and not path.is_symlink()
    }
    if not REQUIRED_CANDIDATE_FILES.issubset(files):
        raise FactoryFailure("FAIL_CANDIDATE_INCOMPLETE", "Candidate required records are missing.")
    wheels = [path for path in files if path.startswith("artifacts/") and path.endswith(".whl")]
    if len(wheels) != 1:
        raise FactoryFailure("FAIL_WHEEL_COUNT", "Candidate must contain exactly one wheel.")
    if any(path.is_symlink() for path in root.rglob("*")):
        raise FactoryFailure("FAIL_CANDIDATE_SYMLINK", "Candidate contains a symbolic link.")
    manifest = _load_manifest(root / "artifact-manifest.json")
    manifest_paths = {record.relative_path for record in manifest}
    expected_manifest_paths = files.difference({"artifact-manifest.json", "SHA256SUMS"})
    if manifest_paths != expected_manifest_paths:
        raise FactoryFailure(
            "FAIL_MANIFEST_FILE_SET",
            "Artifact manifest does not cover the exact candidate file set.",
            details={
                "missing": sorted(expected_manifest_paths - manifest_paths),
                "extra": sorted(manifest_paths - expected_manifest_paths),
            },
        )
    verify_manifest(root, manifest)
    checksum_paths = _verify_checksums(root)
    expected_checksum_paths = manifest_paths.union({"artifact-manifest.json"})
    if checksum_paths != expected_checksum_paths:
        raise FactoryFailure(
            "FAIL_CHECKSUM_FILE_SET",
            "SHA256SUMS does not cover the exact checksummed candidate file set.",
            details={
                "missing": sorted(expected_checksum_paths - checksum_paths),
                "extra": sorted(checksum_paths - expected_checksum_paths),
            },
        )
    require_no_sensitive_values(path for path in root.rglob("*") if path.is_file())
    return GateResult(
        gate="verify_candidate",
        result="PASS",
        message="Exact candidate bytes verified without rebuild or installation.",
        details={"wheel": wheels[0], "file_count": len(files)},
    )
