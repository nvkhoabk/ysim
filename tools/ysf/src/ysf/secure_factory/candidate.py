"""Build-once candidate creation and non-rebuilding verification."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import zipfile
from collections.abc import Iterable, Mapping
from datetime import datetime
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
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_TIMESTAMP_UTC = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
_CONTRACT_SHA256 = "337519fcf7d08104ba0e53cbf33dcc4b4a75ec32aac18601cb097c778aa0ae35"
_BUILDER_ID = "https://github.com/actions/runner"
_BUILD_TYPE = "https://ysim.vn/build-types/v3-r1-s00/ysf-wheel/v1"
_REQUIRED_PREFLIGHT_GATES = frozenset(
    {
        "candidate_build_environment",
        "policy_self_protection",
        "source_allowlist",
        "immutable_corpus",
        "sensitive_data",
    }
)
_QUALITY_REPORT_GATES: dict[str, frozenset[str]] = {
    "test-and-coverage.json": frozenset({"pytest"}),
    "lint-type-sast-dependency.json": frozenset({"ruff", "mypy", "bandit", "pip-audit"}),
    "leak-scan.json": frozenset({"leak-scan"}),
    "environment-identity.json": frozenset({"environment-identity"}),
}
_EVIDENCE_REQUIRED_FIELDS = frozenset(
    {
        "execution_id",
        "timestamp_utc",
        "mutation_class",
        "repository",
        "branch",
        "head_commit",
        "head_tree",
        "contract_sha256",
        "environment_identity",
        "changed_paths",
        "input_digests",
        "command_or_gate",
        "exit_code",
        "result",
        "next_allowed_action",
    }
)


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


def _lock_digest_map(lock_paths: Iterable[Path]) -> dict[str, str]:
    paths = tuple(lock_paths)
    if {path.name for path in paths} != {
        "requirements-s00-build.lock",
        "requirements-s00-dev.lock",
    }:
        raise FactoryFailure("FAIL_LOCK_SET", "Candidate dependency lock set is not exact.")
    return {path.name: sha256_file(path) for path in sorted(paths, key=lambda item: item.name)}


def verify_declared_dependency_closure(
    pyproject_path: Path, lock_paths: Iterable[Path]
) -> GateResult:
    """Require every direct runtime, build and development dependency in the locks."""

    try:
        project = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))
        declared = [
            *project["build-system"]["requires"],
            *project["project"]["dependencies"],
            *project["project"]["optional-dependencies"]["dev"],
        ]
    except (OSError, KeyError, TypeError, tomllib.TOMLDecodeError) as exc:
        raise FactoryFailure(
            "FAIL_DEPENDENCY_DECLARATION", "Dependency declaration is invalid."
        ) from exc
    locked = {item["name"]: item["version"] for item in _parse_lock_components(lock_paths)}
    missing: list[str] = []
    mismatched: list[str] = []
    for requirement in declared:
        match = _LOCK_LINE.match(str(requirement))
        if not match:
            raise FactoryFailure(
                "FAIL_DEPENDENCY_DECLARATION", "Direct dependency is not exactly pinned."
            )
        name = match.group(1).lower().replace("_", "-")
        version = match.group(2)
        if name not in locked:
            missing.append(name)
        elif locked[name] != version:
            mismatched.append(name)
    if missing or mismatched:
        raise FactoryFailure(
            "FAIL_DEPENDENCY_CLOSURE",
            "Declared dependency closure does not match the hash-locked inputs.",
            details={"missing": sorted(missing), "mismatched": sorted(mismatched)},
        )
    return GateResult(
        gate="dependency_closure",
        result="PASS",
        message="All direct dependencies are exactly pinned in approved locks.",
    )


def _expected_input_digests(
    *, tree: str, contract_sha256: str, lock_paths: Iterable[Path]
) -> dict[str, str]:
    return {
        "contract_sha256": contract_sha256,
        "head_tree": tree,
        **_lock_digest_map(lock_paths),
    }


def _load_json_object(path: Path, failure_code: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise FactoryFailure(failure_code, "Candidate JSON record is invalid.") from exc
    if not isinstance(value, dict):
        raise FactoryFailure(failure_code, "Candidate JSON record is invalid.")
    return value


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
    branch: str,
    commit: str,
    tree: str,
    contract_sha256: str,
    source_date_epoch: int,
    lock_paths: Iterable[Path],
    reproducible_wheel_sha256: str,
    gate_report: Mapping[str, Any],
    report_root: Path,
) -> None:
    locks = tuple(lock_paths)
    lock_digests = _lock_digest_map(locks)
    reports = candidate_dir / "reports"
    reports.mkdir(mode=0o750)
    bound_gate_report = {
        "schema_version": 1,
        "repository": repository,
        "branch": branch,
        "head_commit": commit,
        "head_tree": tree,
        "contract_sha256": contract_sha256,
        **gate_report,
    }
    write_exclusive(reports / "gates.json", _json_bytes(bound_gate_report))
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
        "metadata": {
            "component": {"type": "application", "name": "ysf", "version": "0.1.0"},
            "properties": [
                {"name": "ysim:contract:sha256", "value": contract_sha256},
                {"name": "ysim:source:branch", "value": branch},
                {"name": "ysim:source:commit", "value": commit},
                {"name": "ysim:source:tree", "value": tree},
                *[
                    {"name": f"ysim:lock:{name}:sha256", "value": digest}
                    for name, digest in sorted(lock_digests.items())
                ],
            ],
        },
        "components": _parse_lock_components(locks),
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
                "buildType": _BUILD_TYPE,
                "externalParameters": {
                    "branch": branch,
                    "contract_sha256": contract_sha256,
                    "lock_digests": lock_digests,
                },
                "resolvedDependencies": [
                    {
                        "uri": f"git+https://github.com/{repository}@{commit}",
                        "digest": {"gitTree": tree},
                    }
                ],
            },
            "runDetails": {
                "builder": {"id": _BUILDER_ID},
                "metadata": {
                    "invocationId": f"{commit}:{tree}",
                    "startedOnEpoch": source_date_epoch,
                    "finishedOnEpoch": source_date_epoch,
                    "reproducibility": {
                        "independentBuildCount": 2,
                        "wheelSha256": reproducible_wheel_sha256,
                    },
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


def _build_wheel_once(
    repository_root: Path,
    output_directory: Path,
    *,
    environment: Mapping[str, str],
) -> Path:
    try:
        with tempfile.TemporaryDirectory(
            prefix="ysim-v3-r1-s00-build-source."
        ) as temporary_directory:
            temporary_root = require_output_outside_checkout(
                repository_root, Path(temporary_directory)
            )
            build_source = temporary_root / "ysf"
            shutil.copytree(repository_root / "tools/ysf", build_source, symlinks=True)
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
                    str(output_directory),
                    str(build_source),
                ],
                cwd=temporary_root,
                env=dict(environment),
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
            "Candidate wheel command failed.",
            details={"exit_code": process.returncode},
        )
    wheels = sorted(output_directory.glob("*.whl"))
    if len(wheels) != 1:
        raise FactoryFailure("FAIL_WHEEL_COUNT", "Candidate build must produce one wheel.")
    return wheels[0]


def build_candidate(
    repository_root: Path,
    candidate_dir: Path,
    *,
    repository: str,
    branch: str,
    commit: str,
    tree: str,
    contract_sha256: str,
    source_date_epoch: int,
    gate_report: Mapping[str, Any],
    report_root: Path,
) -> GateResult:
    """Retain one wheel after two independent byte-for-byte reproducibility builds."""

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
    lock_paths = (
        repository_root / "tools/ysf/requirements-s00-build.lock",
        repository_root / "tools/ysf/requirements-s00-dev.lock",
    )
    verify_declared_dependency_closure(repository_root / "tools/ysf/pyproject.toml", lock_paths)
    artifacts = candidate_dir / "artifacts"
    artifacts.mkdir(mode=0o750)
    environment = dict(os.environ)
    environment.update(
        {
            "PYTHONHASHSEED": "0",
            "SOURCE_DATE_EPOCH": str(source_date_epoch),
        }
    )
    retained_wheel = _build_wheel_once(repository_root, artifacts, environment=environment)
    with tempfile.TemporaryDirectory(prefix="ysim-v3-r1-s00-reproducibility.") as proof_directory:
        proof_root = require_output_outside_checkout(repository_root, Path(proof_directory))
        proof_output = proof_root / "wheel"
        proof_output.mkdir(mode=0o750)
        proof_wheel = _build_wheel_once(repository_root, proof_output, environment=environment)
        if proof_wheel.name != retained_wheel.name or sha256_file(proof_wheel) != sha256_file(
            retained_wheel
        ):
            raise FactoryFailure(
                "FAIL_WHEEL_REPRODUCIBILITY",
                "Independent wheel builds are not byte-for-byte reproducible.",
            )
    _write_candidate_metadata(
        candidate_dir,
        repository=repository,
        branch=branch,
        commit=commit,
        tree=tree,
        contract_sha256=contract_sha256,
        source_date_epoch=source_date_epoch,
        lock_paths=lock_paths,
        reproducible_wheel_sha256=sha256_file(retained_wheel),
        gate_report=gate_report,
        report_root=report_root,
    )
    require_no_sensitive_values(path for path in candidate_dir.rglob("*") if path.is_file())
    verify_candidate(
        candidate_dir,
        expected_repository=repository,
        expected_branch=branch,
        expected_commit=commit,
        expected_tree=tree,
        expected_contract_sha256=contract_sha256,
        expected_lock_paths=lock_paths,
        expected_changed_paths=gate_report.get("changed_paths", []),
    )
    return GateResult(
        gate="build_candidate",
        result="PASS",
        message="One retained wheel matched an independent reproducibility build.",
        details={
            "candidate_path": str(candidate_dir),
            "independent_build_count": 2,
            "wheel_sha256": sha256_file(retained_wheel),
        },
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


def _verify_gate_report(
    root: Path,
    *,
    repository: str,
    branch: str,
    commit: str,
    tree: str,
    contract_sha256: str,
) -> None:
    report = _load_json_object(root / "reports/gates.json", "FAIL_GATE_REPORT_FORMAT")
    identity = {
        "repository": repository,
        "branch": branch,
        "head_commit": commit,
        "head_tree": tree,
        "contract_sha256": contract_sha256,
    }
    if any(report.get(name) != value for name, value in identity.items()):
        raise FactoryFailure(
            "FAIL_GATE_REPORT_IDENTITY", "Candidate preflight report identity is invalid."
        )
    gates = report.get("gates")
    if not isinstance(gates, list):
        raise FactoryFailure("FAIL_GATE_REPORT_FORMAT", "Candidate preflight gates are invalid.")
    names: list[str] = []
    for gate in gates:
        if not isinstance(gate, dict) or gate.get("result") != "PASS":
            raise FactoryFailure(
                "FAIL_GATE_REPORT_RESULT", "Candidate preflight gate did not pass."
            )
        name = gate.get("gate")
        if not isinstance(name, str):
            raise FactoryFailure("FAIL_GATE_REPORT_FORMAT", "Candidate preflight gate is invalid.")
        names.append(name)
    if set(names) != _REQUIRED_PREFLIGHT_GATES or len(names) != len(set(names)):
        raise FactoryFailure(
            "FAIL_GATE_REPORT_SET", "Candidate preflight gate set is incomplete or duplicated."
        )


def _verify_quality_record(
    record: dict[str, Any],
    *,
    gate: str,
    repository: str,
    branch: str,
    commit: str,
    tree: str,
    contract_sha256: str,
    changed_paths: list[str],
    input_digests: dict[str, str],
) -> None:
    if not _EVIDENCE_REQUIRED_FIELDS.issubset(record):
        raise FactoryFailure(
            "FAIL_EVIDENCE_SCHEMA", "Candidate evidence record omits required fields."
        )
    identity = {
        "repository": repository,
        "branch": branch,
        "head_commit": commit,
        "head_tree": tree,
        "contract_sha256": contract_sha256,
        "changed_paths": changed_paths,
        "input_digests": input_digests,
        "command_or_gate": gate,
        "exit_code": 0,
        "result": "PASS",
        "mutation_class": "READ_ONLY_QUALITY_GATE",
        "next_allowed_action": "BUILD_ONCE_CANDIDATE",
    }
    if any(record.get(name) != value for name, value in identity.items()):
        raise FactoryFailure(
            "FAIL_EVIDENCE_IDENTITY", "Candidate evidence is not bound to exact source inputs."
        )
    execution_id = record.get("execution_id")
    timestamp = record.get("timestamp_utc")
    environment = record.get("environment_identity")
    output_sha256 = record.get("output_sha256")
    if (
        not isinstance(execution_id, str)
        or not re.fullmatch(r"[A-Z0-9][A-Z0-9._-]{7,127}", execution_id)
        or not isinstance(timestamp, str)
        or not _TIMESTAMP_UTC.fullmatch(timestamp)
        or not isinstance(environment, dict)
        or environment.get("external_effect_budget") != "DENY_ALL"
        or environment.get("providers") != "OFF"
        or environment.get("email_mode") != "NON_RELAYING"
        or not isinstance(output_sha256, str)
        or not _SHA256.fullmatch(output_sha256)
    ):
        raise FactoryFailure("FAIL_EVIDENCE_SCHEMA", "Candidate evidence field is invalid.")
    try:
        datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as exc:
        raise FactoryFailure("FAIL_EVIDENCE_SCHEMA", "Candidate timestamp is invalid.") from exc
    if gate == "pytest" and record.get("branch_coverage_threshold_percent") != 90:
        raise FactoryFailure(
            "FAIL_EVIDENCE_QUALITY", "Candidate coverage threshold evidence is invalid."
        )


def _verify_quality_evidence(
    root: Path,
    *,
    repository: str,
    branch: str,
    commit: str,
    tree: str,
    contract_sha256: str,
    lock_paths: Iterable[Path],
    changed_paths: Iterable[str],
) -> None:
    expected_paths = sorted({validate_relative_path(path) for path in changed_paths})
    expected_inputs = _expected_input_digests(
        tree=tree, contract_sha256=contract_sha256, lock_paths=lock_paths
    )
    records: dict[str, dict[str, Any]] = {}
    execution_ids: set[str] = set()
    for filename, required_gates in _QUALITY_REPORT_GATES.items():
        location = (
            root / filename
            if filename == "environment-identity.json"
            else root / "reports" / filename
        )
        report = _load_json_object(location, "FAIL_EVIDENCE_REPORT_FORMAT")
        raw_records = report.get("records")
        if (
            report.get("schema_version") != 1
            or report.get("result") != "PASS"
            or not isinstance(raw_records, list)
        ):
            raise FactoryFailure(
                "FAIL_EVIDENCE_REPORT_FORMAT", "Candidate quality report is invalid."
            )
        observed_gates: set[str] = set()
        for record in raw_records:
            if not isinstance(record, dict) or not isinstance(record.get("command_or_gate"), str):
                raise FactoryFailure(
                    "FAIL_EVIDENCE_REPORT_FORMAT", "Candidate quality record is invalid."
                )
            gate = record["command_or_gate"]
            _verify_quality_record(
                record,
                gate=gate,
                repository=repository,
                branch=branch,
                commit=commit,
                tree=tree,
                contract_sha256=contract_sha256,
                changed_paths=expected_paths,
                input_digests=expected_inputs,
            )
            execution_id = str(record["execution_id"])
            if gate in records or execution_id in execution_ids:
                raise FactoryFailure(
                    "FAIL_EVIDENCE_DUPLICATE",
                    "Candidate quality gate or execution ID is duplicated.",
                )
            records[gate] = record
            execution_ids.add(execution_id)
            observed_gates.add(gate)
        if observed_gates != required_gates:
            raise FactoryFailure(
                "FAIL_EVIDENCE_GATE_SET", "Candidate report gate set is incomplete."
            )
    try:
        ledger_records = [
            json.loads(line)
            for line in (root / "execution-ledger.jsonl").read_text(encoding="utf-8").splitlines()
            if line
        ]
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise FactoryFailure(
            "FAIL_EVIDENCE_LEDGER", "Candidate evidence ledger is invalid."
        ) from exc
    if (
        len(ledger_records) != len(records)
        or any(not isinstance(item, dict) for item in ledger_records)
        or {str(item.get("command_or_gate")): item for item in ledger_records} != records
    ):
        raise FactoryFailure(
            "FAIL_EVIDENCE_LEDGER", "Candidate ledger does not match executed quality gates."
        )


def _verify_sbom(
    root: Path,
    *,
    repository: str,
    branch: str,
    commit: str,
    tree: str,
    contract_sha256: str,
    lock_paths: Iterable[Path],
) -> None:
    del repository
    locks = tuple(lock_paths)
    lock_digests = _lock_digest_map(locks)
    expected = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "version": 1,
        "metadata": {
            "component": {"type": "application", "name": "ysf", "version": "0.1.0"},
            "properties": [
                {"name": "ysim:contract:sha256", "value": contract_sha256},
                {"name": "ysim:source:branch", "value": branch},
                {"name": "ysim:source:commit", "value": commit},
                {"name": "ysim:source:tree", "value": tree},
                *[
                    {"name": f"ysim:lock:{name}:sha256", "value": digest}
                    for name, digest in sorted(lock_digests.items())
                ],
            ],
        },
        "components": _parse_lock_components(locks),
    }
    if _load_json_object(root / "sbom.cdx.json", "FAIL_SBOM_FORMAT") != expected:
        raise FactoryFailure("FAIL_SBOM_SEMANTICS", "Candidate SBOM semantics are invalid.")


def _verify_provenance(
    root: Path,
    *,
    wheel: str,
    repository: str,
    branch: str,
    commit: str,
    tree: str,
    contract_sha256: str,
    lock_paths: Iterable[Path],
) -> None:
    provenance = _load_json_object(root / "provenance.json", "FAIL_PROVENANCE_FORMAT")
    expected_subject = [{"name": wheel, "digest": {"sha256": sha256_file(root / wheel)}}]
    try:
        build_definition = provenance["predicate"]["buildDefinition"]
        run_details = provenance["predicate"]["runDetails"]
        metadata = run_details["metadata"]
    except (KeyError, TypeError) as exc:
        raise FactoryFailure(
            "FAIL_PROVENANCE_SEMANTICS", "Candidate provenance semantics are invalid."
        ) from exc
    wanted_parameters = {
        "branch": branch,
        "contract_sha256": contract_sha256,
        "lock_digests": _lock_digest_map(lock_paths),
    }
    checks = (
        provenance.get("_type") == "https://in-toto.io/Statement/v1",
        provenance.get("subject") == expected_subject,
        provenance.get("predicateType") == "https://slsa.dev/provenance/v1",
        build_definition.get("buildType") == _BUILD_TYPE,
        build_definition.get("externalParameters") == wanted_parameters,
        build_definition.get("resolvedDependencies")
        == [
            {
                "uri": f"git+https://github.com/{repository}@{commit}",
                "digest": {"gitTree": tree},
            }
        ],
        run_details.get("builder") == {"id": _BUILDER_ID},
        metadata.get("invocationId") == f"{commit}:{tree}",
        isinstance(metadata.get("startedOnEpoch"), int),
        metadata.get("startedOnEpoch") == metadata.get("finishedOnEpoch"),
        metadata.get("reproducibility")
        == {
            "independentBuildCount": 2,
            "wheelSha256": sha256_file(root / wheel),
        },
    )
    if not all(checks):
        raise FactoryFailure(
            "FAIL_PROVENANCE_SEMANTICS", "Candidate provenance semantics are invalid."
        )


def verify_candidate(
    candidate_dir: Path,
    *,
    expected_repository: str,
    expected_branch: str,
    expected_commit: str,
    expected_tree: str,
    expected_contract_sha256: str,
    expected_lock_paths: Iterable[Path],
    expected_changed_paths: Iterable[str],
) -> GateResult:
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
    if (
        expected_contract_sha256 != _CONTRACT_SHA256
        or not re.fullmatch(r"[0-9a-f]{40}", expected_commit)
        or not re.fullmatch(r"[0-9a-f]{40}", expected_tree)
    ):
        raise FactoryFailure(
            "FAIL_CANDIDATE_EXPECTATION", "Candidate verification expectation is invalid."
        )
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
    lock_paths = tuple(expected_lock_paths)
    _verify_gate_report(
        root,
        repository=expected_repository,
        branch=expected_branch,
        commit=expected_commit,
        tree=expected_tree,
        contract_sha256=expected_contract_sha256,
    )
    _verify_quality_evidence(
        root,
        repository=expected_repository,
        branch=expected_branch,
        commit=expected_commit,
        tree=expected_tree,
        contract_sha256=expected_contract_sha256,
        lock_paths=lock_paths,
        changed_paths=expected_changed_paths,
    )
    _verify_sbom(
        root,
        repository=expected_repository,
        branch=expected_branch,
        commit=expected_commit,
        tree=expected_tree,
        contract_sha256=expected_contract_sha256,
        lock_paths=lock_paths,
    )
    _verify_provenance(
        root,
        wheel=wheels[0],
        repository=expected_repository,
        branch=expected_branch,
        commit=expected_commit,
        tree=expected_tree,
        contract_sha256=expected_contract_sha256,
        lock_paths=lock_paths,
    )
    require_no_sensitive_values(path for path in root.rglob("*") if path.is_file())
    return GateResult(
        gate="verify_candidate",
        result="PASS",
        message="Exact candidate bytes, source binding, SBOM, provenance and evidence verified.",
        details={
            "wheel": wheels[0],
            "file_count": len(files),
            "semantic_verification": "PASS",
        },
    )
