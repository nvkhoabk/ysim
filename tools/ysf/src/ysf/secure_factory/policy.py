"""Exact-allowlist, immutable-corpus, and path-safety policy."""

from __future__ import annotations

import subprocess
from collections.abc import Iterable
from pathlib import Path, PurePosixPath

from ysf.secure_factory.models import FactoryFailure, GateResult

EXACT_ALLOWLIST: tuple[str, ...] = (
    "AGENTS.md",
    ".github/CODEOWNERS",
    ".github/workflows/v3-r1-s00-secure-factory.yml",
    "docs/v3/r1/g00/s00/README.md",
    "docs/v3/r1/g00/s00/context-receipt.yaml",
    "docs/v3/r1/g00/s00/clarification-register.yaml",
    "docs/v3/r1/g00/s00/slice-contract.yaml",
    "docs/v3/r1/g00/s00/ExecPlan.md",
    "docs/v3/r1/g00/s00/source-and-delivery-policy.md",
    "docs/v3/r1/g00/s00/environment-identity.yaml",
    "docs/v3/r1/g00/s00/test-matrix.yaml",
    "docs/v3/r1/g00/s00/evidence-schema.yaml",
    "tools/ysf/pyproject.toml",
    "tools/ysf/requirements-s00-build.lock",
    "tools/ysf/requirements-s00-dev.lock",
    "tools/ysf/src/ysf/cli.py",
    "tools/ysf/src/ysf/secure_factory/__init__.py",
    "tools/ysf/src/ysf/secure_factory/models.py",
    "tools/ysf/src/ysf/secure_factory/cli.py",
    "tools/ysf/src/ysf/secure_factory/environment.py",
    "tools/ysf/src/ysf/secure_factory/policy.py",
    "tools/ysf/src/ysf/secure_factory/sensitive.py",
    "tools/ysf/src/ysf/secure_factory/evidence.py",
    "tools/ysf/src/ysf/secure_factory/candidate.py",
    "tools/ysf/tests/unit/test_secure_factory_environment.py",
    "tools/ysf/tests/unit/test_secure_factory_policy.py",
    "tools/ysf/tests/unit/test_secure_factory_sensitive.py",
    "tools/ysf/tests/unit/test_secure_factory_evidence.py",
    "tools/ysf/tests/unit/test_secure_factory_candidate.py",
    "tools/ysf/tests/integration/test_secure_factory_pipeline.py",
    "tools/ysf/tests/fixtures/secure_factory/compliant/README.txt",
    "tools/ysf/tests/fixtures/secure_factory/noncompliant/path-escape.json",
    "tools/ysf/tests/fixtures/secure_factory/noncompliant/synthetic-secret.txt",
    "tools/ysf/tests/fixtures/secure_factory/noncompliant/synthetic-esim-payload.txt",
    "tools/ysf/tests/fixtures/secure_factory/noncompliant/tampered-manifest.json",
    "scripts/v3-r1-s00.sh",
)

QUARANTINED_FIXTURES: frozenset[str] = frozenset(
    path for path in EXACT_ALLOWLIST if "/noncompliant/" in path
)


def validate_relative_path(value: str) -> str:
    """Return a normalized repository path or fail closed."""

    if not value or "\x00" in value or "\\" in value:
        raise FactoryFailure("FAIL_PATH_FORMAT", "Repository path is not canonical.")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise FactoryFailure("FAIL_PATH_ESCAPE", "Repository path escapes its root.")
    normalized = path.as_posix()
    if normalized != value:
        raise FactoryFailure("FAIL_PATH_FORMAT", "Repository path is not canonical.")
    return normalized


def parse_porcelain_z(data: bytes) -> set[str]:
    """Parse Git porcelain v1 -z, retaining both sides of rename records."""

    records = data.split(b"\x00")
    paths: set[str] = set()
    index = 0
    while index < len(records):
        record = records[index]
        index += 1
        if not record:
            continue
        if len(record) < 4 or record[2:3] != b" ":
            raise FactoryFailure("FAIL_GIT_STATUS_FORMAT", "Git status record is invalid.")
        status = record[:2].decode("ascii", errors="strict")
        path = record[3:].decode("utf-8", errors="strict")
        paths.add(validate_relative_path(path))
        if "R" in status or "C" in status:
            if index >= len(records) or not records[index]:
                raise FactoryFailure("FAIL_GIT_STATUS_FORMAT", "Rename status is incomplete.")
            other = records[index].decode("utf-8", errors="strict")
            index += 1
            paths.add(validate_relative_path(other))
    return paths


def changed_paths(repository_root: Path) -> set[str]:
    process = subprocess.run(
        ["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        cwd=repository_root,
        check=False,
        capture_output=True,
    )
    if process.returncode != 0:
        raise FactoryFailure(
            "FAIL_GIT_STATUS",
            "Unable to determine the repository mutation set.",
            details={"exit_code": process.returncode},
        )
    return parse_porcelain_z(process.stdout)


def mutation_paths(repository_root: Path, *, base_ref: str = "v3/main") -> set[str]:
    """Return committed branch diff plus unstaged/staged/untracked mutations."""

    process = subprocess.run(
        ["git", "diff", "--name-only", "-z", f"{base_ref}...HEAD"],
        cwd=repository_root,
        check=False,
        capture_output=True,
    )
    if process.returncode != 0:
        raise FactoryFailure("FAIL_GIT_DIFF", "Unable to determine branch mutation set.")
    committed = {
        validate_relative_path(item.decode("utf-8", errors="strict"))
        for item in process.stdout.split(b"\x00")
        if item
    }
    return committed.union(changed_paths(repository_root))


def _assert_no_symlink(repository_root: Path, relative_path: str) -> None:
    current = repository_root
    for part in PurePosixPath(relative_path).parts:
        current = current / part
        if current.is_symlink():
            raise FactoryFailure(
                "FAIL_SYMLINK_PATH",
                "Changed repository path contains a symbolic link.",
                details={"path": relative_path},
            )
        if not current.exists():
            break


def validate_changed_paths(
    repository_root: Path,
    paths: Iterable[str],
    *,
    expected: Iterable[str] | None = None,
) -> GateResult:
    """Apply exact allowlist/default-deny and optional exact-stage scope."""

    normalized = {validate_relative_path(path) for path in paths}
    unexpected = sorted(normalized.difference(EXACT_ALLOWLIST))
    if unexpected:
        raise FactoryFailure(
            "FAIL_UNAPPROVED_PATH",
            "Repository contains a changed path outside the exact S00 allowlist.",
            details={"paths": unexpected},
        )
    for path in sorted(normalized):
        _assert_no_symlink(repository_root, path)
    if expected is not None:
        expected_set = {validate_relative_path(path) for path in expected}
        if normalized != expected_set:
            raise FactoryFailure(
                "FAIL_STAGE_MUTATION_SET",
                "Repository mutation set does not match the authorized stage.",
                details={
                    "missing": sorted(expected_set - normalized),
                    "extra": sorted(normalized - expected_set),
                },
            )
    return GateResult(
        gate="source_allowlist",
        result="PASS",
        message="Exact changed-path policy verified.",
        details={"changed_path_count": len(normalized)},
    )


def verify_immutable_corpus(repository_root: Path) -> GateResult:
    """Verify BRD/UXF bytes against HEAD and reject untracked corpus files."""

    process = subprocess.run(
        [
            "git",
            "status",
            "--porcelain=v1",
            "-z",
            "--untracked-files=all",
            "--",
            "docs/BRD",
            "docs/UXF",
        ],
        cwd=repository_root,
        check=False,
        capture_output=True,
    )
    if process.returncode != 0:
        raise FactoryFailure("FAIL_CORPUS_CHECK", "Immutable corpus check failed.")
    mutations = parse_porcelain_z(process.stdout)
    if mutations:
        raise FactoryFailure(
            "FAIL_IMMUTABLE_CORPUS",
            "BRD or UXF corpus bytes differ from the approved seed tree.",
            details={"paths": sorted(mutations)},
        )
    files = subprocess.run(
        ["git", "ls-files", "-z", "--", "docs/BRD", "docs/UXF"],
        cwd=repository_root,
        check=False,
        capture_output=True,
    )
    if files.returncode != 0:
        raise FactoryFailure("FAIL_CORPUS_CHECK", "Immutable corpus inventory failed.")
    count = len([item for item in files.stdout.split(b"\x00") if item])
    if count != 31:
        raise FactoryFailure(
            "FAIL_IMMUTABLE_CORPUS_COUNT",
            "Immutable corpus file count does not match the approved inventory.",
            details={"observed_count": count},
        )
    return GateResult(
        gate="immutable_corpus",
        result="PASS",
        message="All 24 BRD and seven UXF files remain immutable.",
        details={"file_count": count},
    )


def read_policy_allowlist(policy_path: Path) -> tuple[str, ...]:
    """Read the only text block following the Exact allowlist heading."""

    lines = policy_path.read_text(encoding="utf-8").splitlines()
    try:
        heading = lines.index("## Exact allowlist")
        start = lines.index("```text", heading) + 1
        end = lines.index("```", start)
    except ValueError as exc:
        raise FactoryFailure(
            "FAIL_POLICY_SELF_CHECK",
            "Source policy does not contain one readable exact allowlist.",
        ) from exc
    return tuple(line for line in lines[start:end] if line)


def verify_policy_self_protection(policy_path: Path) -> GateResult:
    recorded = read_policy_allowlist(policy_path)
    if recorded != EXACT_ALLOWLIST or len(set(recorded)) != len(recorded):
        raise FactoryFailure(
            "FAIL_POLICY_SELF_CHECK",
            "Executable allowlist differs from the frozen source policy.",
        )
    return GateResult(
        gate="policy_self_protection",
        result="PASS",
        message="Executable and frozen allowlists match exactly.",
        details={"allowlist_path_count": len(recorded)},
    )


def require_regular_files(repository_root: Path, paths: Iterable[str]) -> None:
    """Reject missing, non-regular, or multiply linked source inputs."""

    for relative_path in paths:
        normalized = validate_relative_path(relative_path)
        path = repository_root / normalized
        try:
            stat = path.lstat()
        except OSError as exc:
            raise FactoryFailure(
                "FAIL_SOURCE_FILE",
                "Required source input is missing.",
                details={"path": normalized},
            ) from exc
        if not path.is_file() or path.is_symlink() or stat.st_nlink != 1:
            raise FactoryFailure(
                "FAIL_SOURCE_FILE",
                "Required source input is not a single regular file.",
                details={"path": normalized},
            )
