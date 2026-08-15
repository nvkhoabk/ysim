"""Fail-closed public validator for V3-R1 G00-S04."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import stat
import subprocess
from collections import Counter
from collections.abc import Mapping, Sequence
from pathlib import Path, PurePosixPath
from types import MappingProxyType
from typing import Any, NoReturn, cast

import yaml

from ysf.index.documents import build_document_index
from ysf.index.knowledge import build_knowledge_index
from ysf.knowledge.catalog import build_named_catalog
from ysf.knowledge.models import KnowledgeDocument
from ysf.knowledge.normalizer import normalize_document
from ysf.knowledge.patterns import CAPABILITY_PATTERNS, INTEGRATION_PATTERNS
from ysf.knowledge.validator import validate_documents, validate_unique_ids
from ysf.secure_factory.models import FactoryFailure
from ysf.secure_factory.sensitive import scan_bytes

EXPECTED_REPOSITORY = "nvkhoabk/ysim"
EXPECTED_ORIGIN_SHA256 = "b9ce8b55768f59f974ebdb2d0268204d1fb7c2b3147ba4545859fa64aa268c07"
EXPECTED_BRANCH = (
    "feature/v3-r1-g00-s04-integration-boundary-operator-visibility-source-baseline"
)
EXPECTED_BASE_BRANCH = "feature/v3-r1-g00-s03-configuration-access-control-source-baseline"
EXPECTED_BASE_SHA = "168efc707cde042ef0459a2bd92f177617c4a25b"
EXPECTED_BASE_TREE = "6126508cf1fdae163dbf9ccc43684a567fa6c7e1"
EXPECTED_REQUIREMENTS = (
    "V3-R1-INT-001",
    "V3-R1-INT-002",
    "V3-R1-INT-003",
    "V3-R1-REL-009",
)
EXPECTED_SCOPE_DECISIONS = {
    "V3-R1-REL-001": "DEFER",
    "V3-R1-REL-003": "DEFER",
    "V3-R1-REL-004": "EXCLUDE_FROM_S04_NORMATIVE_SCOPE",
    "V3-R1-REL-005": "EXCLUDE_FROM_S04_NORMATIVE_SCOPE",
    "V3-R1-REL-006": "EXCLUDE_FROM_S04_NORMATIVE_SCOPE",
}
EXPECTED_ALLOWLIST_ORDER = (
    "docs/v3/r1/g00/s04/MANIFEST.sha256",
    "docs/v3/r1/g00/s04/README.md",
    "docs/v3/r1/g00/s04/integration-boundary-operator-visibility-baseline.yaml",
    "docs/v3/r1/g00/s04/package-spec.yaml",
    "docs/v3/r1/g00/s04/scope-decisions.yaml",
    "docs/v3/r1/g00/s04/source-provenance.yaml",
    "tools/ysf/src/ysf/integration_boundary/__init__.py",
    "tools/ysf/src/ysf/integration_boundary/models.py",
    "tools/ysf/src/ysf/integration_boundary/service.py",
    "tools/ysf/src/ysf/integration_boundary/validator.py",
    "tools/ysf/tests/unit/test_integration_boundary.py",
    "tools/ysf/tests/unit/test_integration_boundary_validator.py",
    "tools/ysf/tests/integration/test_integration_boundary_pipeline.py",
)
EXPECTED_ALLOWLIST = frozenset(EXPECTED_ALLOWLIST_ORDER)
EXPECTED_CHANGED_PATHS = EXPECTED_ALLOWLIST
MANIFEST_PATH = "docs/v3/r1/g00/s04/MANIFEST.sha256"
README_PATH = "docs/v3/r1/g00/s04/README.md"
BASELINE_PATH = (
    "docs/v3/r1/g00/s04/integration-boundary-operator-visibility-baseline.yaml"
)
SPEC_PATH = "docs/v3/r1/g00/s04/package-spec.yaml"
SCOPE_PATH = "docs/v3/r1/g00/s04/scope-decisions.yaml"
PROVENANCE_PATH = "docs/v3/r1/g00/s04/source-provenance.yaml"
EXPECTED_ARTIFACT_PATHS = (BASELINE_PATH, SPEC_PATH, MANIFEST_PATH, SCOPE_PATH, PROVENANCE_PATH)
EXPECTED_STABLE_READ = {
    "platform": "Linux",
    "component_traversal": "DESCRIPTOR_RELATIVE",
    "empty_parts_rejected": True,
    "normalization_aliases_rejected": True,
    "controlled_failure": "FactoryFailure",
    "failure_code_passthrough": True,
    "raw_exception_escape_allowed": False,
    "descriptor_closure_required": True,
    "minimum_descriptor_cycles": 500,
    "nofollow": True,
    "descriptor_fstat_before_after": True,
    "worktree_bytes_equal_head_blob": True,
    "trusted_path_reopen_allowed": False,
    "sensitive_scan_source": "CAPTURED_BYTES",
}
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_GIT_SHA = re.compile(r"^[0-9a-f]{40}$")
_PLACEHOLDER = re.compile(
    r"(?i)(?:\bTODO\b|\bTBD\b|\bFIXME\b|CHANGE_ME|REPLACE_ME|\{\{[^}]+\}\})"
)
_OVERCLAIM = re.compile(
    r"(?i)\b(?:checkpoint|requirement|integration runtime)\s+"
    r"(?:is|status\s*[:=])\s*(?:IMPLEMENTED|OPERATIONAL|DEPLOYED)\b"
)


def _fail(code: str, message: str, **details: object) -> NoReturn:
    raise FactoryFailure(code, message, details=dict(details))


def _mapping(value: Any, code: str, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        _fail(code, f"{label} must be a mapping.")
    return value


def _sequence(value: Any, code: str, label: str) -> Sequence[Any]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        _fail(code, f"{label} must be a sequence.")
    return value


def _exact_keys(value: Mapping[str, Any], expected: set[str], code: str, label: str) -> None:
    if set(value) != expected:
        _fail(
            code,
            f"{label} keys differ from the exact schema.",
            missing=sorted(expected - set(value)),
            extra=sorted(set(value) - expected),
        )


def _metadata(identity: os.stat_result) -> tuple[int, int, int, int, int, int, int]:
    return (
        identity.st_dev,
        identity.st_ino,
        stat.S_IFMT(identity.st_mode),
        identity.st_size,
        identity.st_mtime_ns,
        identity.st_ctime_ns,
        identity.st_nlink,
    )


def _safe_relative_parts(relative: str, code: str) -> tuple[str, ...]:
    if not isinstance(relative, str) or "\x00" in relative:
        _fail(code, "Required path is unsafe.")
    pure = PurePosixPath(relative)
    if (
        not relative
        or not pure.parts
        or pure.is_absolute()
        or pure.as_posix() != relative
        or any(part in {"", ".", ".."} for part in pure.parts)
    ):
        _fail(code, "Required path is unsafe.")
    return pure.parts


def _directory_flags() -> int:
    return os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC


def _file_flags() -> int:
    return os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC


def _open_absolute_directory(path: Path, code: str) -> int:
    if platform.system() != "Linux":
        _fail("FAIL_ENVIRONMENT_IDENTITY", "Stable descriptor validation requires Linux.")
    if not path.is_absolute() or Path(os.path.normpath(os.fspath(path))) != path:
        _fail(code, "Absolute directory path is unsafe.")
    descriptors: list[int] = []
    try:
        current = os.open(path.anchor, _directory_flags())
        descriptors.append(current)
        for component in path.parts[1:]:
            current = os.open(component, _directory_flags(), dir_fd=current)
            descriptors.append(current)
        result = os.dup(descriptors[-1])
        os.set_inheritable(result, False)
        return result
    except (OSError, ValueError):
        _fail(code, "Absolute directory path is missing or unsafe.")
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def _read_descriptor_bytes(descriptor: int) -> bytes:
    chunks: list[bytes] = []
    while True:
        chunk = os.read(descriptor, 1024 * 1024)
        if not chunk:
            return b"".join(chunks)
        chunks.append(chunk)


def _verify_relative_identity(
    root_descriptor: int,
    parts: tuple[str, ...],
    directories: Sequence[tuple[int, int, int, int, int, int, int]],
    expected_file: tuple[int, int, int, int, int, int, int],
    code: str,
) -> None:
    descriptors: list[int] = []
    try:
        current = os.dup(root_descriptor)
        os.set_inheritable(current, False)
        descriptors.append(current)
        if _metadata(os.fstat(current)) != directories[0]:
            _fail(code, "Required root identity changed during stable read.")
        for index, component in enumerate(parts[:-1], start=1):
            current = os.open(component, _directory_flags(), dir_fd=current)
            descriptors.append(current)
            if _metadata(os.fstat(current)) != directories[index]:
                _fail(code, "Required parent identity changed during stable read.")
        final_descriptor = os.open(parts[-1], _file_flags(), dir_fd=current)
        descriptors.append(final_descriptor)
        if _metadata(os.fstat(final_descriptor)) != expected_file:
            _fail(code, "Required file identity changed during stable read.")
    except (OSError, ValueError):
        _fail(code, "Required path identity cannot be reverified.")
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def _stable_read_relative(root_descriptor: int, relative: str, code: str) -> bytes:
    parts = _safe_relative_parts(relative, code)
    descriptors: list[int] = []
    directory_metadata: list[tuple[int, int, int, int, int, int, int]] = []
    try:
        current = os.dup(root_descriptor)
        os.set_inheritable(current, False)
        descriptors.append(current)
        directory_metadata.append(_metadata(os.fstat(current)))
        for component in parts[:-1]:
            current = os.open(component, _directory_flags(), dir_fd=current)
            descriptors.append(current)
            observed = os.fstat(current)
            if not stat.S_ISDIR(observed.st_mode):
                _fail(code, "Required parent is not a directory.")
            directory_metadata.append(_metadata(observed))
        file_descriptor = os.open(parts[-1], _file_flags(), dir_fd=current)
        descriptors.append(file_descriptor)
        before = os.fstat(file_descriptor)
        if not stat.S_ISREG(before.st_mode):
            _fail(code, "Required path is not a regular file.")
        before_metadata = _metadata(before)
        data = _read_descriptor_bytes(file_descriptor)
        if _metadata(os.fstat(file_descriptor)) != before_metadata or len(data) != before.st_size:
            _fail(code, "Required file changed during stable read.")
        for descriptor, expected in zip(descriptors[:-1], directory_metadata, strict=True):
            if _metadata(os.fstat(descriptor)) != expected:
                _fail(code, "Required parent changed during stable read.")
        _verify_relative_identity(
            root_descriptor, parts, directory_metadata, before_metadata, code
        )
        return data
    except (OSError, ValueError):
        _fail(code, "Required path cannot be opened through the stable boundary.")
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def _stable_read_absolute(path: Path, code: str) -> bytes:
    if not path.is_absolute() or Path(os.path.normpath(os.fspath(path))) != path:
        _fail(code, "Required absolute file path is unsafe.")
    root_descriptor = _open_absolute_directory(Path(path.anchor), code)
    try:
        relative = PurePosixPath(*path.parts[1:]).as_posix()
        return _stable_read_relative(root_descriptor, relative, code)
    finally:
        os.close(root_descriptor)


def _git_file_bytes(root: Path, revision: str, relative: str, code: str) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(root), "show", f"{revision}:{relative}"],
        check=False,
        capture_output=True,
    )
    if completed.returncode != 0:
        _fail(code, "Git blob bytes cannot be read.", path=relative)
    return completed.stdout


class _ValidationSnapshot:
    def __init__(self, root: Path) -> None:
        self.root = root
        self._root_descriptor = _open_absolute_directory(root, "FAIL_REPOSITORY_ROOT")
        self._root_metadata = _metadata(os.fstat(self._root_descriptor))
        self._cache: dict[str, bytes] = {}

    def __enter__(self) -> _ValidationSnapshot:
        return self

    def __exit__(self, *_args: object) -> None:
        os.close(self._root_descriptor)

    def read(self, relative: str) -> bytes:
        cached = self._cache.get(relative)
        if cached is not None:
            return cached
        captured = _stable_read_relative(self._root_descriptor, relative, "FAIL_PATH_SAFETY")
        expected = _git_file_bytes(self.root, "HEAD", relative, "FAIL_PATH_SAFETY")
        if captured != expected:
            _fail(
                "FAIL_WORKTREE_BLOB",
                "Captured worktree bytes differ from the exact HEAD blob.",
                path=relative,
            )
        self._cache[relative] = captured
        return captured

    def capture_all(self, paths: Sequence[str]) -> None:
        for relative in paths:
            self.read(relative)

    def verify_root_stable(self) -> None:
        if _metadata(os.fstat(self._root_descriptor)) != self._root_metadata:
            _fail("FAIL_REPOSITORY_ROOT", "Repository root changed during validation.")
        observed = _open_absolute_directory(self.root, "FAIL_REPOSITORY_ROOT")
        try:
            if _metadata(os.fstat(observed)) != self._root_metadata:
                _fail("FAIL_REPOSITORY_ROOT", "Repository root path changed during validation.")
        finally:
            os.close(observed)


def _load_yaml_bytes(data: bytes, code: str, label: str) -> Mapping[str, Any]:
    try:
        value = yaml.safe_load(data.decode("utf-8"))
    except (UnicodeError, yaml.YAMLError):
        _fail(code, "Required YAML cannot be parsed from captured bytes.", artifact=label)
    return _mapping(value, code, label)


def _run_git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        _fail("FAIL_REPOSITORY_IDENTITY", "Required Git observation failed.")
    return completed.stdout.strip()


def _freeze_value(value: Any) -> Any:
    try:
        if isinstance(value, Mapping):
            return MappingProxyType(
                {key: _freeze_value(item) for key, item in tuple(value.items())}
            )
        if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
            return tuple(_freeze_value(item) for item in tuple(value))
    except (RuntimeError, TypeError, ValueError):
        _fail("FAIL_SNAPSHOT_CONTRACT", "Snapshot contract changed while being frozen.")
    return value


def _contract_paths(value: Any, label: str) -> list[str]:
    observed = list(_sequence(value, "FAIL_SNAPSHOT_CONTRACT", label))
    for relative in observed:
        if not isinstance(relative, str):
            _fail("FAIL_SNAPSHOT_CONTRACT", f"{label} contains a non-string path.")
        _safe_relative_parts(relative, "FAIL_SNAPSHOT_CONTRACT")
    if observed != sorted(EXPECTED_ALLOWLIST):
        _fail("FAIL_SNAPSHOT_CONTRACT", f"{label} differs from the exact sorted boundary.")
    return observed


def _exact_scalar_mapping(
    observed: Mapping[str, Any], expected: Mapping[str, Any], label: str
) -> None:
    _exact_keys(observed, set(expected), "FAIL_SNAPSHOT_CONTRACT", label)
    for key, expected_value in expected.items():
        value = observed[key]
        if type(value) is not type(expected_value) or value != expected_value:
            _fail("FAIL_SNAPSHOT_CONTRACT", f"{label} differs from the exact boundary.")


def _validate_contract(contract: Mapping[str, Any]) -> None:
    code = "FAIL_SNAPSHOT_CONTRACT"
    _exact_keys(
        contract,
        {
            "schema_version",
            "repository",
            "topology",
            "changed_paths",
            "authorized_paths",
            "file_modes",
            "artifact_digests",
            "requirements",
            "scope_decisions",
            "safety",
            "knowledge",
            "branch_coverage",
            "stable_read",
        },
        code,
        "snapshot contract",
    )
    if type(contract["schema_version"]) is not int or contract["schema_version"] != 2:
        _fail(code, "Snapshot schema version is incorrect.")
    repository = _mapping(contract["repository"], code, "repository")
    _exact_scalar_mapping(
        repository,
        {
            "identity": EXPECTED_REPOSITORY,
            "origin_sha256": EXPECTED_ORIGIN_SHA256,
            "branch": EXPECTED_BRANCH,
        },
        "repository",
    )
    topology = _mapping(contract["topology"], code, "topology")
    _exact_keys(
        topology,
        {
            "base_sha",
            "base_tree",
            "parent_sha",
            "expected_head_sha",
            "expected_head_tree",
            "base_to_head_commit_count",
            "parent_to_head_commit_count",
        },
        code,
        "topology",
    )
    for key in {"base_sha", "base_tree", "parent_sha", "expected_head_sha", "expected_head_tree"}:
        if not isinstance(topology[key], str) or _GIT_SHA.fullmatch(topology[key]) is None:
            _fail(code, "Snapshot contains malformed Git identity.")
    if (
        topology["base_sha"] != EXPECTED_BASE_SHA
        or topology["base_tree"] != EXPECTED_BASE_TREE
        or topology["parent_sha"] != EXPECTED_BASE_SHA
        or topology["base_to_head_commit_count"] != 1
        or topology["parent_to_head_commit_count"] != 1
    ):
        _fail(code, "Snapshot topology differs from the exact S04 stack.")
    _contract_paths(contract["changed_paths"], "changed_paths")
    _contract_paths(contract["authorized_paths"], "authorized_paths")
    modes = _mapping(contract["file_modes"], code, "file_modes")
    if set(modes) != EXPECTED_ALLOWLIST or any(value != "100644" for value in modes.values()):
        _fail(code, "Snapshot modes differ from the exact 100644 boundary.")
    artifacts = _mapping(contract["artifact_digests"], code, "artifact_digests")
    if set(artifacts) != set(EXPECTED_ARTIFACT_PATHS) or any(
        not isinstance(value, str) or _SHA256.fullmatch(value) is None
        for value in artifacts.values()
    ):
        _fail(code, "Snapshot artifact digests are malformed or incomplete.")
    if list(_sequence(contract["requirements"], code, "requirements")) != list(
        EXPECTED_REQUIREMENTS
    ):
        _fail(code, "Snapshot requirements differ from the exact authority.")
    decisions = _mapping(contract["scope_decisions"], code, "scope_decisions")
    if dict(decisions) != EXPECTED_SCOPE_DECISIONS:
        _fail(code, "Snapshot scope decisions differ from explicit authority.")
    _exact_scalar_mapping(
        _mapping(contract["safety"], code, "safety"),
        {"providers": "OFF", "email_mode": "NON_RELAYING", "external_effect_budget": "DENY_ALL"},
        "safety",
    )
    knowledge = _mapping(contract["knowledge"], code, "knowledge")
    _exact_keys(
        knowledge,
        {
            "source",
            "tracked_factory_index_allowed",
            "index_documents",
            "knowledge_records",
            "knowledge_documents",
            "capabilities",
            "integrations",
            "relationships",
            "document_codes",
            "duplicate_document_codes",
        },
        code,
        "knowledge",
    )
    if knowledge["source"] != "CURRENT_DOCS_IN_MEMORY" or knowledge[
        "tracked_factory_index_allowed"
    ] is not False:
        _fail(code, "Snapshot knowledge source is weakened.")
    for key in set(knowledge) - {"source", "tracked_factory_index_allowed"}:
        if type(knowledge[key]) is not int or knowledge[key] < 0:
            _fail(code, "Snapshot knowledge count is malformed.")
    if knowledge["index_documents"] != knowledge["knowledge_documents"]:
        _fail(code, "Snapshot index and knowledge document counts differ.")
    if knowledge["duplicate_document_codes"] != 0:
        _fail(code, "Snapshot contains duplicate document codes.")
    coverage = _mapping(contract["branch_coverage"], code, "branch_coverage")
    _exact_keys(
        coverage,
        {
            "source_package",
            "metric",
            "minimum_percent",
            "branches_covered",
            "branches_valid",
            "branch_rate",
            "percent",
        },
        code,
        "branch_coverage",
    )
    if (
        coverage["source_package"] != "ysf.integration_boundary"
        or coverage["metric"] != "COVERED_BRANCHES_DIVIDED_BY_VALID_BRANCHES"
        or coverage["minimum_percent"] != 90.0
        or type(coverage["branches_covered"]) is not int
        or type(coverage["branches_valid"]) is not int
        or type(coverage["branch_rate"]) is not float
        or type(coverage["percent"]) is not float
        or coverage["branches_valid"] <= 0
    ):
        _fail(code, "Snapshot branch coverage boundary is malformed.")
    exact_percent = coverage["branches_covered"] / coverage["branches_valid"] * 100
    if (
        coverage["branches_covered"] > coverage["branches_valid"]
        or abs(coverage["percent"] - exact_percent) > 1e-12
        or abs(coverage["branch_rate"] - round(exact_percent / 100, 4)) > 1e-12
        or exact_percent < 90.0
    ):
        _fail(code, "Snapshot branch coverage is below or inconsistent with the gate.")
    _exact_scalar_mapping(
        _mapping(contract["stable_read"], code, "stable_read"),
        EXPECTED_STABLE_READ,
        "stable_read",
    )


def load_snapshot_contract(path: Path) -> Mapping[str, Any]:
    return _load_yaml_bytes(
        _stable_read_absolute(path, "FAIL_SNAPSHOT_CONTRACT"),
        "FAIL_SNAPSHOT_CONTRACT",
        path.name,
    )


def _validated_root(root: Path) -> Path:
    if not isinstance(root, Path) or not root.is_absolute():
        _fail("FAIL_REPOSITORY_ROOT", "Repository root must be an absolute path.")
    if Path(os.path.normpath(os.fspath(root))) != root or ".." in root.parts:
        _fail("FAIL_REPOSITORY_ROOT", "Repository root path is not normalized.")
    descriptor = _open_absolute_directory(root, "FAIL_REPOSITORY_ROOT")
    os.close(descriptor)
    return root


def _changed_paths(root: Path) -> set[str]:
    completed = subprocess.run(
        ["git", "-C", str(root), "diff", "--name-only", "-z", f"{EXPECTED_BASE_SHA}...HEAD"],
        check=False,
        capture_output=True,
    )
    if completed.returncode != 0:
        _fail("FAIL_REPOSITORY_IDENTITY", "Changed paths cannot be observed.")
    paths: set[str] = set()
    for raw in completed.stdout.split(b"\0"):
        if not raw:
            continue
        try:
            relative = raw.decode("utf-8")
        except UnicodeError:
            _fail("FAIL_PATH_SAFETY", "Changed path is not UTF-8.")
        _safe_relative_parts(relative, "FAIL_PATH_SAFETY")
        paths.add(relative)
    return paths


def _mode(root: Path, relative: str, snapshot: _ValidationSnapshot) -> str:
    snapshot.read(relative)
    record = _run_git(root, "ls-tree", "HEAD", "--", relative)
    match = re.fullmatch(r"(\d{6}) blob [0-9a-f]{40}\t.+", record)
    if match is None:
        _fail("FAIL_FILE_MODE", "Authorized path is not a regular Git blob.", path=relative)
    return match.group(1)


def _observe_repository(
    root: Path, contract: Mapping[str, Any], snapshot: _ValidationSnapshot
) -> tuple[str, str, set[str]]:
    if platform.system() != "Linux":
        _fail("FAIL_ENVIRONMENT_IDENTITY", "S04 validation requires Linux.")
    repository = cast(Mapping[str, Any], contract["repository"])
    topology = cast(Mapping[str, Any], contract["topology"])
    origin = _run_git(root, "remote", "get-url", "origin")
    if any(character in origin for character in ("\r", "\n", "\x00")):
        _fail("FAIL_REPOSITORY_IDENTITY", "Repository origin contains unsafe bytes.")
    origin_digest = hashlib.sha256(origin.encode("utf-8")).hexdigest()
    top = Path(_run_git(root, "rev-parse", "--show-toplevel"))
    branch = _run_git(root, "branch", "--show-current")
    if (
        top != root
        or repository["identity"] != EXPECTED_REPOSITORY
        or origin_digest != repository["origin_sha256"]
        or branch != EXPECTED_BRANCH
    ):
        _fail("FAIL_REPOSITORY_IDENTITY", "Observed repository identity is incorrect.")
    status = subprocess.run(
        ["git", "-C", str(root), "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        check=False,
        capture_output=True,
    )
    if status.returncode != 0:
        _fail("FAIL_REPOSITORY_IDENTITY", "Repository status cannot be observed.")
    if status.stdout:
        _fail("FAIL_DIRTY_WORKTREE", "Public S04 validation requires a clean checkout.")
    head = _run_git(root, "rev-parse", "HEAD")
    tree = _run_git(root, "rev-parse", "HEAD^{tree}")
    if (
        _run_git(root, "rev-parse", f"{EXPECTED_BASE_SHA}^{{tree}}") != EXPECTED_BASE_TREE
        or _run_git(root, "rev-parse", "HEAD^") != EXPECTED_BASE_SHA
        or int(_run_git(root, "rev-list", "--count", f"{EXPECTED_BASE_SHA}..HEAD")) != 1
        or head != topology["expected_head_sha"]
        or tree != topology["expected_head_tree"]
    ):
        _fail("FAIL_HEAD_IDENTITY", "Observed head/tree/topology differs from snapshot.")
    modes = {relative: _mode(root, relative, snapshot) for relative in sorted(EXPECTED_ALLOWLIST)}
    if modes != dict(cast(Mapping[str, str], contract["file_modes"])):
        _fail("FAIL_FILE_MODE", "Observed file modes differ from snapshot.")
    changed = _changed_paths(root)
    if changed != EXPECTED_CHANGED_PATHS:
        _fail("FAIL_FILE_ALLOWLIST", "Observed changed paths differ from S04 authority.")
    return head, tree, changed


def _yaml(snapshot: _ValidationSnapshot, relative: str, code: str) -> Mapping[str, Any]:
    return _load_yaml_bytes(snapshot.read(relative), code, relative)


def _validate_artifacts(
    snapshot: _ValidationSnapshot, contract: Mapping[str, Any]
) -> dict[str, str]:
    baseline = _yaml(snapshot, BASELINE_PATH, "FAIL_PACKAGE_BASELINE")
    if (
        baseline.get("checkpoint") != "V3-R1-G00-S04"
        or baseline.get("title") != "Integration Boundary and Operator Visibility Source Baseline"
        or baseline.get("checkpoint_type") != "SOURCE_IMPLEMENTATION"
        or baseline.get("maturity_target") != "PLANNED"
        or baseline.get("package_evidence_level") != "SOURCE_VALIDATED_NON_OPERATIONAL"
        or baseline.get("candidate_model") != "NONE"
    ):
        _fail("FAIL_PACKAGE_BASELINE", "Baseline identity or maturity boundary differs.")
    requirement_records = list(
        _sequence(baseline.get("normative_requirements"), "FAIL_PACKAGE_BASELINE", "requirements")
    )
    if [item.get("id") for item in requirement_records if isinstance(item, Mapping)] != list(
        EXPECTED_REQUIREMENTS
    ) or any(item.get("state") != "SOURCE_APPROVED" for item in requirement_records):
        _fail("FAIL_PACKAGE_BASELINE", "Baseline requirement authority differs.")
    safety = _mapping(baseline.get("safety"), "FAIL_PACKAGE_BASELINE", "safety")
    if safety != {
        "synthetic_data_only": True,
        "providers": "OFF",
        "email_mode": "NON_RELAYING",
        "external_effect_budget": "DENY_ALL",
    }:
        _fail("FAIL_PACKAGE_BASELINE", "Baseline safety boundary differs.")

    scope = _yaml(snapshot, SCOPE_PATH, "FAIL_SCOPE_DECISIONS")
    if (
        scope.get("checkpoint") != "V3-R1-G00-S04"
        or scope.get("authority") != "EXPLICIT_SCOPED_ADOPTION_DECISION"
        or scope.get("unresolved_human_decisions") != 0
    ):
        _fail("FAIL_SCOPE_DECISIONS", "Scope decisions remain unresolved.")
    decision_items = list(_sequence(scope.get("decisions"), "FAIL_SCOPE_DECISIONS", "decisions"))
    observed_decisions = {
        str(item.get("requirement_id")): item.get("decision")
        for item in decision_items
        if isinstance(item, Mapping)
    }
    if observed_decisions != EXPECTED_SCOPE_DECISIONS or any(
        item.get("normative_in_s04") is not False or item.get("retained_state") != "PROPOSED"
        for item in decision_items
        if isinstance(item, Mapping)
    ):
        _fail("FAIL_SCOPE_DECISIONS", "Scope dispositions differ from explicit authority.")

    package = _yaml(snapshot, SPEC_PATH, "FAIL_PACKAGE_SPEC")
    if (
        package.get("checkpoint") != "V3-R1-G00-S04"
        or package.get("requirements") != list(EXPECTED_REQUIREMENTS)
        or package.get("allowed_paths") != list(EXPECTED_ALLOWLIST_ORDER)
        or package.get("file_mode") != "100644"
        or package.get("branch") != EXPECTED_BRANCH
        or package.get("checkpoint_type") != "SOURCE_IMPLEMENTATION"
        or package.get("maturity_target") != "PLANNED"
        or package.get("package_evidence_level") != "SOURCE_VALIDATED_NON_OPERATIONAL"
        or package.get("candidate_model") != "NONE"
    ):
        _fail("FAIL_PACKAGE_SPEC", "Package identity, scope, or maturity differs.")
    package_safety = _mapping(package.get("safety"), "FAIL_PACKAGE_SPEC", "safety")
    if package_safety != safety:
        _fail("FAIL_PACKAGE_SPEC", "Package safety boundary differs from baseline.")
    validation_gates = _mapping(
        package.get("validation_gates"), "FAIL_PACKAGE_SPEC", "validation_gates"
    )
    branch_gate = _mapping(
        validation_gates.get("branch_coverage"), "FAIL_PACKAGE_SPEC", "branch_coverage"
    )
    if branch_gate != {
        "source_package": "ysf.integration_boundary",
        "metric": "COVERED_BRANCHES_DIVIDED_BY_VALID_BRANCHES",
        "minimum_percent": 90.0,
    }:
        _fail("FAIL_PACKAGE_SPEC", "Package branch coverage gate differs.")
    observed_stable_read = _mapping(
        validation_gates.get("stable_descriptor_read"),
        "FAIL_PACKAGE_SPEC",
        "stable_read",
    )
    if dict(observed_stable_read) != EXPECTED_STABLE_READ:
        _fail("FAIL_PACKAGE_SPEC", "Package stable-read boundary differs.")

    provenance = _yaml(snapshot, PROVENANCE_PATH, "FAIL_SOURCE_PROVENANCE")
    if (
        provenance.get("checkpoint") != "V3-R1-G00-S04"
        or provenance.get("authority") != "EXPLICIT_SCOPED_ADOPTION_DECISION"
    ):
        _fail("FAIL_SOURCE_PROVENANCE", "Source provenance identity differs.")
    predecessor = _mapping(
        provenance.get("predecessor"), "FAIL_SOURCE_PROVENANCE", "predecessor"
    )
    if (
        predecessor.get("commit") != EXPECTED_BASE_SHA
        or predecessor.get("tree") != EXPECTED_BASE_TREE
        or predecessor.get("branch") != EXPECTED_BASE_BRANCH
    ):
        _fail("FAIL_SOURCE_PROVENANCE", "Predecessor provenance differs.")
    provenance_requirements = list(
        _sequence(
            provenance.get("normative_requirements"),
            "FAIL_SOURCE_PROVENANCE",
            "normative_requirements",
        )
    )
    expected_hashes = {
        "V3-R1-INT-001": "16c5210e4073ce54d0fb8c93ae5674fb5a8df3e45490571dce7408d2004ad01a",
        "V3-R1-INT-002": "eaebb90c097141b74c54075f2a53d37a458c5a3230ff7d7067dec1a653cc0d01",
        "V3-R1-INT-003": "93b8726606055c5fa29261f4a6a62553f09bb6dbb7e18638ca10aaee2c5a3912",
        "V3-R1-REL-009": "5c4e5038db3715ac18064c2c0c0f85028e2ce856fb81d6b462da786325b31fe3",
    }
    if {
        str(item.get("id")): item.get("requirement_sha256")
        for item in provenance_requirements
        if isinstance(item, Mapping)
    } != expected_hashes:
        _fail("FAIL_SOURCE_PROVENANCE", "Requirement provenance differs.")
    provenance_decisions = _mapping(
        provenance.get("scope_decision_binding"),
        "FAIL_SOURCE_PROVENANCE",
        "scope_decision_binding",
    )
    if provenance_decisions.get("decisions") != EXPECTED_SCOPE_DECISIONS:
        _fail("FAIL_SOURCE_PROVENANCE", "Scope-decision provenance differs.")

    try:
        readme = snapshot.read(README_PATH).decode("utf-8")
    except UnicodeError:
        _fail("FAIL_DOCUMENT_METADATA", "S04 README is not valid UTF-8.")
    if _PLACEHOLDER.search(readme) or _OVERCLAIM.search(readme):
        _fail("FAIL_DOCUMENT_CLAIM", "S04 README contains placeholder or overclaim.")
    if not readme.startswith("---\n") or "\n---\n" not in readme[4:]:
        _fail("FAIL_DOCUMENT_METADATA", "S04 README metadata is missing.")
    metadata = _load_yaml_bytes(
        readme[4:].split("\n---\n", 1)[0].encode("utf-8"),
        "FAIL_DOCUMENT_METADATA",
        README_PATH,
    )
    if metadata.get("document_code") != "V3-R1-G00-S04-README":
        _fail("FAIL_DOCUMENT_METADATA", "S04 README document code differs.")

    try:
        lines = snapshot.read(MANIFEST_PATH).decode("utf-8").splitlines()
    except UnicodeError:
        _fail("FAIL_PACKAGE_MANIFEST", "Manifest is not UTF-8.")
    records: dict[str, str] = {}
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\r\n]+)", line)
        if match is None:
            _fail("FAIL_PACKAGE_MANIFEST", "Manifest record is malformed.")
        relative = match.group(2)
        _safe_relative_parts(relative, "FAIL_PACKAGE_MANIFEST")
        if relative in records:
            _fail("FAIL_PACKAGE_MANIFEST", "Manifest path is duplicated.")
        records[relative] = match.group(1)
    if list(records) != sorted(EXPECTED_ALLOWLIST - {MANIFEST_PATH}):
        _fail("FAIL_PACKAGE_MANIFEST", "Manifest path coverage differs.")
    for relative, digest in records.items():
        if hashlib.sha256(snapshot.read(relative)).hexdigest() != digest:
            _fail("FAIL_PACKAGE_MANIFEST", "Manifest digest differs.", path=relative)

    actual = {
        relative: hashlib.sha256(snapshot.read(relative)).hexdigest()
        for relative in EXPECTED_ARTIFACT_PATHS
    }
    if actual != dict(cast(Mapping[str, str], contract["artifact_digests"])):
        _fail("FAIL_SNAPSHOT_ARTIFACT", "External artifact digest binding differs.")
    return actual


def _fresh_knowledge(root: Path) -> dict[str, int]:
    source = build_document_index(root)
    raw_documents = source.get("documents")
    if not isinstance(raw_documents, list):
        _fail("FAIL_KNOWLEDGE", "Fresh document input is malformed.")
    documents: list[KnowledgeDocument] = [
        normalize_document(item) for item in raw_documents if isinstance(item, dict)
    ]
    try:
        validate_documents(documents)
        validate_unique_ids(documents)
    except Exception:
        _fail("FAIL_KNOWLEDGE", "Fresh knowledge documents are invalid.")
    capabilities, capability_relationships = build_named_catalog(
        documents=documents,
        patterns=CAPABILITY_PATTERNS,
        relationship_type=("references-capability"),
    )
    integrations, integration_relationships = build_named_catalog(
        documents=documents,
        patterns=INTEGRATION_PATTERNS,
        relationship_type=("references-integration"),
    )
    codes = [document.document_code for document in documents if document.document_code]
    duplicates = sum(count - 1 for count in Counter(codes).values() if count > 1)
    return {
        "index_documents": int(source["documentCount"]),
        "knowledge_records": int(build_knowledge_index(root)["knowledgeCount"]),
        "knowledge_documents": len(documents),
        "capabilities": len(capabilities),
        "integrations": len(integrations),
        "relationships": len(capability_relationships) + len(integration_relationships),
        "document_codes": len(codes),
        "duplicate_document_codes": duplicates,
    }


def _scan(snapshot: _ValidationSnapshot, changed: set[str]) -> str:
    findings = []
    for relative in sorted(changed):
        findings.extend(scan_bytes(snapshot.read(relative), location=relative))
    if findings:
        raise FactoryFailure(
            "FAIL_SENSITIVE_VALUE",
            "Sensitive value detected; raw value suppressed.",
            details={"findings": [finding.safe_dict() for finding in findings]},
        )
    return "PASS"


def _final_readback(
    root: Path, contract: Mapping[str, Any], snapshot: _ValidationSnapshot
) -> None:
    topology = cast(Mapping[str, Any], contract["topology"])
    status = subprocess.run(
        ["git", "-C", str(root), "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        check=False,
        capture_output=True,
    )
    origin = _run_git(root, "remote", "get-url", "origin")
    if (
        status.returncode != 0
        or status.stdout
        or _run_git(root, "rev-parse", "HEAD") != topology["expected_head_sha"]
        or _run_git(root, "rev-parse", "HEAD^{tree}") != topology["expected_head_tree"]
        or _run_git(root, "branch", "--show-current") != EXPECTED_BRANCH
        or hashlib.sha256(origin.encode("utf-8")).hexdigest() != EXPECTED_ORIGIN_SHA256
    ):
        _fail("FAIL_REPOSITORY_IDENTITY", "Repository changed during validation.")
    snapshot.verify_root_stable()


def validate_integration_boundary(
    repository_root: Path, snapshot_contract: Mapping[str, Any]
) -> dict[str, Any]:
    """Validate exact S04 repository evidence through one API/CLI boundary."""

    root = _validated_root(repository_root)
    contract = _mapping(_freeze_value(snapshot_contract), "FAIL_SNAPSHOT_CONTRACT", "contract")
    _validate_contract(contract)
    with _ValidationSnapshot(root) as snapshot:
        head, tree, changed = _observe_repository(root, contract, snapshot)
        artifacts = _validate_artifacts(snapshot, contract)
        sensitive = _scan(snapshot, changed)
        knowledge = _fresh_knowledge(root)
        expected_knowledge: dict[str, Any] = {
            "source": "CURRENT_DOCS_IN_MEMORY",
            "tracked_factory_index_allowed": False,
            **knowledge,
        }
        if dict(cast(Mapping[str, Any], contract["knowledge"])) != expected_knowledge:
            _fail("FAIL_KNOWLEDGE", "Fresh knowledge counts differ from snapshot.")
        _final_readback(root, contract, snapshot)
    coverage = cast(Mapping[str, Any], contract["branch_coverage"])
    return {
        "result": "PASS",
        "checkpoint": "V3-R1-G00-S04",
        "title": "Integration Boundary and Operator Visibility Source Baseline",
        "repository_head": head,
        "repository_tree": tree,
        "changed_paths": sorted(changed),
        "requirements": list(EXPECTED_REQUIREMENTS),
        "scope_decisions": dict(EXPECTED_SCOPE_DECISIONS),
        "checkpoint_type": "SOURCE_IMPLEMENTATION",
        "maturity_target": "PLANNED",
        "package_evidence_level": "SOURCE_VALIDATED_NON_OPERATIONAL",
        "candidate_model": "NONE",
        "artifact_digests": artifacts,
        "knowledge": knowledge,
        "branch_coverage": dict(coverage),
        "stable_read": dict(EXPECTED_STABLE_READ),
        "sensitive_data": sensitive,
        "providers": "OFF",
        "email_mode": "NON_RELAYING",
        "external_effect_budget": "DENY_ALL",
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, required=True)
    parser.add_argument("--snapshot-contract", type=Path, required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        result = validate_integration_boundary(
            args.repository_root, load_snapshot_contract(args.snapshot_contract)
        )
        if args.json:
            print(json.dumps(result, sort_keys=True))
        else:
            print("V3-R1-G00-S04 validation PASS")
        return 0
    except FactoryFailure as failure:
        print(
            json.dumps(
                {
                    "result": "FAIL",
                    "code": failure.code,
                    "message": failure.safe_message,
                    "details": failure.details,
                },
                sort_keys=True,
            )
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
