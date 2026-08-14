"""Fail-closed package validator for V3-R1 G00-S03."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import stat
import subprocess
import tomllib
from collections.abc import Mapping, Sequence
from pathlib import Path, PurePosixPath
from types import MappingProxyType
from typing import Any, NoReturn, cast

import yaml

from ysf.secure_factory.models import FactoryFailure
from ysf.secure_factory.sensitive import scan_bytes

EXPECTED_REPOSITORY = "nvkhoabk/ysim"
EXPECTED_BRANCH = "feature/v3-r1-g00-s03-configuration-access-control-source-baseline"
EXPECTED_BASE_BRANCH = "feature/v3-r1-g00-s02-governance-requirements-baseline"
EXPECTED_BASE_SHA = "6e71bdd58df2c5baddb36783abbc513867656df0"
EXPECTED_BASE_TREE = "b40ef828825e36641695adb23faedf7346102630"
EXPECTED_CORRECTIVE_PARENT_SHA = "82e7adb52940b2a1214f0b97e85156f3758124a6"
EXPECTED_CORRECTIVE_PARENT_TREE = "efcf63461d63e0260de2fb01945d860badca5d97"
R3_CORRECTIVE_PARENT_SHA = "62f73324f00fda213cba52cb7c50686c6a0f5e6a"
R3_CORRECTIVE_PARENT_TREE = "ce1005025986e39dabd5b675aaa8f8956cd754a7"
R2_CORRECTIVE_PARENT_SHA = "bc7893f5efa2c3b40da52396b9e946187c6a2044"
R2_CORRECTIVE_PARENT_TREE = "ff9be9172780065e46dac4a336a9cf38b52af8f2"
EXPECTED_REQUIREMENTS = (
    "V3-R1-OPS-001",
    "V3-R1-OPS-002",
    "V3-R1-OPS-003",
    "V3-R1-SEC-001",
    "V3-R1-SEC-003",
)
EXPECTED_ALLOWLIST_ORDER = (
    ".gitignore",
    "docs/v3/r1/g00/s02/MANIFEST.sha256",
    "tools/ysf/tests/unit/test_governance_baseline_validator.py",
    "docs/v3/r1/g00/s03/MANIFEST.sha256",
    "docs/v3/r1/g00/s03/README.md",
    "docs/v3/r1/g00/s03/configuration-access-control-baseline.yaml",
    "docs/v3/r1/g00/s03/package-spec.yaml",
    "docs/v3/r1/g00/s03/source-provenance.yaml",
    "tools/ysf/src/ysf/configuration_access_control/__init__.py",
    "tools/ysf/src/ysf/configuration_access_control/controls.py",
    "tools/ysf/src/ysf/configuration_access_control/validator.py",
    "tools/ysf/tests/unit/test_configuration_access_control.py",
    "tools/ysf/tests/unit/test_configuration_access_control_validator.py",
    "tools/ysf/src/ysf/knowledge/service.py",
    "tools/ysf/tests/integration/test_build_knowledge.py",
    "tools/ysf/tests/integration/test_secure_factory_pipeline.py",
    "tools/ysf/pyproject.toml",
)
EXPECTED_ALLOWLIST = frozenset(EXPECTED_ALLOWLIST_ORDER)
EXPECTED_CHANGED_PATHS_ORDER = tuple(
    path
    for path in EXPECTED_ALLOWLIST_ORDER
    if path != "tools/ysf/tests/integration/test_secure_factory_pipeline.py"
)
EXPECTED_CHANGED_PATHS = frozenset(EXPECTED_CHANGED_PATHS_ORDER)
MANIFEST_PATH = "docs/v3/r1/g00/s03/MANIFEST.sha256"
README_PATH = "docs/v3/r1/g00/s03/README.md"
BASELINE_PATH = "docs/v3/r1/g00/s03/configuration-access-control-baseline.yaml"
SPEC_PATH = "docs/v3/r1/g00/s03/package-spec.yaml"
PROVENANCE_PATH = "docs/v3/r1/g00/s03/source-provenance.yaml"
TRACEABILITY_PATH = "docs/v3/r1/g00/s01/traceability-baseline.yaml"
EXPECTED_ARTIFACT_PATHS = (
    SPEC_PATH,
    MANIFEST_PATH,
    PROVENANCE_PATH,
)
EXPECTED_KNOWLEDGE_BOUNDARY: dict[str, Any] = {
    "builder": "ysf.index.documents.build_document_index",
    "source": "CURRENT_DOCS_IN_MEMORY",
    "source_glob": "docs/**/*.md",
    "tracked_factory_index_allowed": False,
    "expected_document_count": 124,
    "expected_capability_count": 8,
    "expected_integration_count": 0,
    "expected_relationship_count": 48,
}
EXPECTED_BRANCH_COVERAGE_BOUNDARY: dict[str, Any] = {
    "source_package": "ysf.configuration_access_control",
    "metric": "COVERED_BRANCHES_DIVIDED_BY_VALID_BRANCHES",
    "minimum_percent": 90.0,
}
EXPECTED_COVERAGE_ISOLATION: dict[str, Any] = {
    "configuration_path": "tools/ysf/pyproject.toml",
    "runtime_data_file": ".coverage.runtime",
    "runtime_data_pattern": "tools/ysf/.coverage.runtime*",
    "gitignore_rules": [
        "/tools/ysf/.coverage.runtime",
        "/tools/ysf/.coverage.runtime.*",
    ],
    "tracked_coverage_file": "tools/ysf/.coverage",
    "tracked_coverage_mutation_allowed": False,
    "coverage_file_environment_override_required": False,
    "standard_invocation_clean_required": True,
    "branch_instrumentation": True,
}
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_GIT_SHA = re.compile(r"^[0-9a-f]{40}$")
_PLACEHOLDER = re.compile(r"(?i)(?:\bTODO\b|\bTBD\b|\bFIXME\b|CHANGE_ME|REPLACE_ME|\{\{[^}]+\}\})")
_OVERCLAIM = re.compile(
    r"(?i)\b(?:checkpoint|requirement|identity platform|configuration service)\s+"
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
    pure = PurePosixPath(relative)
    if (
        not relative
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
    except OSError:
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
    expected_directories: Sequence[tuple[int, int, int, int, int, int, int]],
    expected_file: tuple[int, int, int, int, int, int, int],
    code: str,
) -> None:
    descriptors: list[int] = []
    try:
        current = os.dup(root_descriptor)
        os.set_inheritable(current, False)
        descriptors.append(current)
        if _metadata(os.fstat(current)) != expected_directories[0]:
            _fail(code, "Required path root identity changed during stable read.")
        for index, component in enumerate(parts[:-1], start=1):
            current = os.open(component, _directory_flags(), dir_fd=current)
            descriptors.append(current)
            if _metadata(os.fstat(current)) != expected_directories[index]:
                _fail(code, "Required path parent identity changed during stable read.")
        final_descriptor = os.open(parts[-1], _file_flags(), dir_fd=current)
        descriptors.append(final_descriptor)
        if _metadata(os.fstat(final_descriptor)) != expected_file:
            _fail(code, "Required file pathname identity changed during stable read.")
    except OSError:
        _fail(code, "Required path identity cannot be reverified after stable read.")
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def _stable_read_relative(root_descriptor: int, relative: str, code: str) -> bytes:
    parts = _safe_relative_parts(relative, code)
    descriptors: list[int] = []
    directory_metadata: list[tuple[int, tuple[int, int, int, int, int, int, int]]] = []
    try:
        current = os.dup(root_descriptor)
        os.set_inheritable(current, False)
        descriptors.append(current)
        directory_metadata.append((current, _metadata(os.fstat(current))))
        for component in parts[:-1]:
            current = os.open(component, _directory_flags(), dir_fd=current)
            descriptors.append(current)
            observed = os.fstat(current)
            if not stat.S_ISDIR(observed.st_mode):
                _fail(code, "Required path parent is not a directory.")
            directory_metadata.append((current, _metadata(observed)))
        file_descriptor = os.open(parts[-1], _file_flags(), dir_fd=current)
        descriptors.append(file_descriptor)
        before = os.fstat(file_descriptor)
        if not stat.S_ISREG(before.st_mode):
            _fail(code, "Required path is not a regular file.")
        before_metadata = _metadata(before)
        data = _read_descriptor_bytes(file_descriptor)
        after_metadata = _metadata(os.fstat(file_descriptor))
        if before_metadata != after_metadata or len(data) != before.st_size:
            _fail(code, "Required file changed while its stable descriptor was read.")
        for descriptor, expected in directory_metadata:
            if _metadata(os.fstat(descriptor)) != expected:
                _fail(code, "Required path parent changed during stable read.")
        _verify_relative_identity(
            root_descriptor,
            parts,
            [expected for _, expected in directory_metadata],
            before_metadata,
            code,
        )
        return data
    except OSError:
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


def _git_file_bytes(root: Path, revision: str, path: str, code: str) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(root), "show", f"{revision}:{path}"],
        check=False,
        capture_output=True,
    )
    if completed.returncode != 0:
        _fail(code, "Git blob bytes cannot be read.", path=path)
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
            _fail("FAIL_REPOSITORY_ROOT", "Repository root descriptor changed during validation.")
        observed_descriptor = _open_absolute_directory(self.root, "FAIL_REPOSITORY_ROOT")
        try:
            if _metadata(os.fstat(observed_descriptor)) != self._root_metadata:
                _fail("FAIL_REPOSITORY_ROOT", "Repository root path changed during validation.")
        finally:
            os.close(observed_descriptor)


def _load_yaml_bytes(data: bytes, code: str, label: str) -> Mapping[str, Any]:
    try:
        value = yaml.safe_load(data.decode("utf-8"))
    except (UnicodeError, yaml.YAMLError):
        _fail(code, "Required YAML cannot be parsed from captured bytes.")
    return _mapping(value, code, label)


def _load_yaml(path: Path, code: str) -> Mapping[str, Any]:
    return _load_yaml_bytes(_stable_read_absolute(path, code), code, path.name)


def _sha256(path: Path) -> str:
    return hashlib.sha256(_stable_read_absolute(path, "FAIL_REQUIRED_FILE")).hexdigest()


def _content_bytes(root: Path, relative: str, snapshot: _ValidationSnapshot | None) -> bytes:
    if snapshot is not None:
        return snapshot.read(relative)
    return _stable_read_absolute(root / relative, "FAIL_REQUIRED_FILE")


def _content_yaml(
    root: Path, relative: str, code: str, snapshot: _ValidationSnapshot | None
) -> Mapping[str, Any]:
    return _load_yaml_bytes(_content_bytes(root, relative, snapshot), code, relative)


def _content_sha256(root: Path, relative: str, snapshot: _ValidationSnapshot | None) -> str:
    return hashlib.sha256(_content_bytes(root, relative, snapshot)).hexdigest()


def _run_git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        _fail(
            "FAIL_REPOSITORY_IDENTITY",
            "Required Git observation failed.",
            command=list(args),
            exit_code=completed.returncode,
        )
    return completed.stdout.strip()


def _git_file_sha256(root: Path, revision: str, path: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(root), "show", f"{revision}:{path}"],
        check=False,
        capture_output=True,
    )
    if completed.returncode != 0:
        _fail("FAIL_SOURCE_PROVENANCE", "Historical source bytes cannot be read.")
    return hashlib.sha256(completed.stdout).hexdigest()


def _expected_spec() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "package_id": "V3-R1-G00-S03-CONFIGURATION-ACCESS-CONTROL-SOURCE-BASELINE",
        "package_version": "0.1.0",
        "checkpoint": "V3-R1-G00-S03",
        "title": "Configuration and Access Control Source Baseline",
        "repository": EXPECTED_REPOSITORY,
        "origin_policy": "NORMALIZED_GITHUB_REPOSITORY_IDENTITY",
        "branch": EXPECTED_BRANCH,
        "stacked_base": {
            "branch": EXPECTED_BASE_BRANCH,
            "commit": EXPECTED_BASE_SHA,
            "tree": EXPECTED_BASE_TREE,
        },
        "head_topology": {
            "binding": "MANDATORY_EXTERNAL_SNAPSHOT_CONTRACT_V2",
            "corrective_parent_commit": EXPECTED_CORRECTIVE_PARENT_SHA,
            "corrective_parent_tree": EXPECTED_CORRECTIVE_PARENT_TREE,
            "base_to_head_commit_count": 5,
            "parent_to_head_commit_count": 1,
        },
        "repository_root_contract": {
            "absolute_path_required": True,
            "symlink_components_allowed": False,
            "git_top_level_must_equal_repository_root": True,
            "identity_boundary": "OBSERVED_ORIGIN_BRANCH_AND_EXTERNAL_SNAPSHOT_TOPOLOGY",
        },
        "checkpoint_type": "SOURCE_IMPLEMENTATION",
        "maturity_target": "PLANNED",
        "package_evidence_level": "SOURCE_VALIDATED_NON_OPERATIONAL",
        "candidate_model": "NONE",
        "requirements": list(EXPECTED_REQUIREMENTS),
        "allowed_paths": list(EXPECTED_ALLOWLIST_ORDER),
        "file_mode": "100644",
        "external_snapshot_contract": {
            "schema_version": 2,
            "changed_path_binding": "EXACT_SORTED_BASE_TO_HEAD_16_PATHS",
            "authorized_path_binding": "EXACT_SORTED_17_PATHS",
            "authorized_mode_binding": "EXACT_17_PATHS_100644",
            "artifact_digest_paths": list(EXPECTED_ARTIFACT_PATHS),
            "validation_boundaries": ["knowledge_input", "branch_coverage"],
        },
        "validation_gates": {
            "branch_coverage": EXPECTED_BRANCH_COVERAGE_BOUNDARY,
            "knowledge_input": EXPECTED_KNOWLEDGE_BOUNDARY,
            "stable_descriptor_read": {
                "platform": "Linux",
                "component_traversal": "DESCRIPTOR_RELATIVE",
                "nofollow": True,
                "descriptor_fstat_before_after": True,
                "worktree_bytes_equal_head_blob": True,
                "trusted_path_reopen_allowed": False,
                "sensitive_scan_source": "CAPTURED_BYTES",
            },
            "coverage_state_isolation": EXPECTED_COVERAGE_ISOLATION,
        },
        "s02_compatibility_exception": {
            "scope": "DESCENDANT_S03_TEST_FIXTURE_ONLY",
            "accepted_s02_branch_mutated": False,
            "accepted_s02_decision_reinterpreted": False,
            "runtime_or_governance_validator_changed": False,
            "integration_path_changed": False,
        },
        "safety": {
            "synthetic_data_only": True,
            "providers": "OFF",
            "email_mode": "NON_RELAYING",
            "external_effect_budget": "DENY_ALL",
        },
        "forbidden_scope": [
            "IDENTITY_PLATFORM",
            "UNIVERSAL_MFA",
            "FEDERATION",
            "PRODUCTION_SESSIONS",
            "CREDENTIAL_ISSUANCE",
            "KEY_CUSTODY",
            "COMPLIANCE_CERTIFICATION",
        ],
        "final_human_decision": {
            "actor": "nvkhoabk",
            "prerequisite": "FRESH_INDEPENDENT_ADVISORY_REVIEW_PASS",
            "record_type": "TOP_LEVEL_ISSUE_COMMENT",
            "github_approval_review": False,
            "implementation_codex_may_record": False,
            "status_before_decision": "DRAFT",
        },
        "next_allowed_action": "FRESH_INDEPENDENT_ADVISORY_REVIEW_S03",
    }


def _expected_provenance() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "provenance_id": "V3-R1-G00-S03-SOURCE-PROVENANCE-001",
        "checkpoint": "V3-R1-G00-S03",
        "corrective_r2": {
            "parent_commit": R2_CORRECTIVE_PARENT_SHA,
            "parent_tree": R2_CORRECTIVE_PARENT_TREE,
            "knowledge_input": {
                "builder": "ysf.index.documents.build_document_index",
                "source": "CURRENT_DOCS_IN_MEMORY",
                "source_glob": "docs/**/*.md",
                "tracked_factory_index_allowed": False,
                "expected_document_count": 124,
                "expected_capability_count": 8,
                "expected_integration_count": 0,
                "expected_relationship_count": 48,
                "service": {
                    "path": "tools/ysf/src/ysf/knowledge/service.py",
                    "sha256": ("82a03c2dc9a7862b1cb5c79b01f0c6b3ef5feb107c5b5b20e12f34d36f7f334d"),
                },
                "regression_test": {
                    "path": "tools/ysf/tests/integration/test_build_knowledge.py",
                    "sha256": ("c5a9dc34e71b90e7b5a8fe5075626cf039fff37517d2e111b824cab285908905"),
                },
            },
            "branch_coverage_gate": {
                "source_package": "ysf.configuration_access_control",
                "metric": "COVERED_BRANCHES_DIVIDED_BY_VALID_BRANCHES",
                "minimum_percent": 90.0,
            },
        },
        "corrective_r3": {
            "parent_commit": R3_CORRECTIVE_PARENT_SHA,
            "parent_tree": R3_CORRECTIVE_PARENT_TREE,
            "external_snapshot_contract": {
                "schema_version": 2,
                "changed_path_count": 14,
                "authorized_path_count": 15,
                "authorized_file_mode": "100644",
                "artifact_digest_paths": list(EXPECTED_ARTIFACT_PATHS),
                "knowledge_input": EXPECTED_KNOWLEDGE_BOUNDARY,
                "branch_coverage": EXPECTED_BRANCH_COVERAGE_BOUNDARY,
            },
        },
        "corrective_r4": {
            "parent_commit": EXPECTED_CORRECTIVE_PARENT_SHA,
            "parent_tree": EXPECTED_CORRECTIVE_PARENT_TREE,
            "stable_read_boundary": {
                "platform": "Linux",
                "component_traversal": "DESCRIPTOR_RELATIVE",
                "directory_flags": ["O_DIRECTORY", "O_NOFOLLOW", "O_CLOEXEC"],
                "file_flags": ["O_NOFOLLOW", "O_CLOEXEC"],
                "descriptor_fstat_before_after": True,
                "worktree_bytes_equal_head_blob": True,
                "trusted_path_reopen_allowed": False,
                "sensitive_scan_source": "CAPTURED_BYTES",
            },
            "coverage_state_isolation": EXPECTED_COVERAGE_ISOLATION,
            "external_snapshot_contract": {
                "schema_version": 2,
                "changed_path_count": 16,
                "authorized_path_count": 17,
                "authorized_file_mode": "100644",
                "artifact_digest_paths": list(EXPECTED_ARTIFACT_PATHS),
                "knowledge_input": EXPECTED_KNOWLEDGE_BOUNDARY,
                "branch_coverage": EXPECTED_BRANCH_COVERAGE_BOUNDARY,
            },
        },
        "predecessor": {
            "branch": EXPECTED_BASE_BRANCH,
            "commit": EXPECTED_BASE_SHA,
            "tree": EXPECTED_BASE_TREE,
        },
        "s01_traceability": {
            "path": TRACEABILITY_PATH,
            "git_blob_sha": "09f6bb315349666194eb4961776b0e007334973c",
            "sha256": "bd5cd5dc65a9481ca0355a7eb1383632bbcd69a6da64681031c4755554d82a19",
        },
        "brd_sources": [
            {
                "path": "docs/BRD/BRD-WS-14.md",
                "git_blob_sha": "f4efcf874b778d4bada8860a8b5e58804653fa63",
                "sha256": "fe1b5aa63cfede9d949cb678a60bf1eb5e250b131049cda9f5b4dfef437a2ef2",
                "anchor_ids": ["V3-R1-SA-061", "V3-R1-SA-062", "V3-R1-SA-063"],
            },
            {
                "path": "docs/BRD/BRD-WS-16.md",
                "git_blob_sha": "3a99857a3ae62198b0d720e61635f75257df3b0b",
                "sha256": "027fac669b060e1ec9dc66020e10b8d86dfb1b1bd6ec0725f066064e5ff93903",
                "anchor_ids": ["V3-R1-SA-067", "V3-R1-SA-069"],
            },
        ],
        "s02_governance": {
            "human_decision": {
                "comment_id": 5278693551,
                "marker": "YSIM_V3_R1_G00_S02_HUMAN_DECISION_V1",
                "actor": "nvkhoabk",
                "body_sha256": "bd9e1ed4dc05952ad08b81c78173ae9ce3eeb7ab0cfaeaad3b0df61ed513e25d",
            },
            "candidate": {
                "path": (
                    "factory/releases/v3-r1-g00-s02-governance-requirements-"
                    "baseline/YSim_V3_R1_G00_S02_Governance_Requirements_"
                    "Baseline_v0.1.0-candidate.1.md"
                ),
                "git_blob_sha": "6f979e29178fb6f35812ee0815d683a1566f4065",
                "sha256": "f3aa80a23a1ab95ab9914263d8c79bf11fc466579f162c79d0302cbfa77c9a77",
            },
            "acceptance_receipt": {
                "path": "docs/v3/r1/g00/s02/acceptance-receipt.yaml",
                "git_blob_sha": "a3fd4d246b986a06b83ca57fe9809b00e62fe306",
                "sha256": "0a776b91daaef1b6fad67eb6b2d94bd0b6f99e522d089845dfc02ccc62410c23",
            },
            "package_spec": {
                "path": "docs/v3/r1/g00/s02/package-spec.yaml",
                "git_blob_sha": "b6176340a541ff859ceb0be54aa403145143db60",
                "sha256": "8ef86e32ca2313ca80a60a74af4b88b67cad59c6644f3b9525e0f028dff16fd9",
            },
            "standards_provenance": {
                "path": "docs/v3/r1/g00/s02/standards/standards-provenance.yaml",
                "git_blob_sha": "f0fd92bd5d858c42d104b5f07fe4f0c268cdabd8",
                "sha256": "2cb417883bd2a5e9a1a10a95b5669777736979a7a91c62a988c3e0a8e59d45df",
            },
            "authoritative_docx_sha256": (
                "47da5d9dc46bb0e136936f865007d988fe537e3a0413676d8d00fe89496fba48"
            ),
        },
        "s02_descendant_compatibility": {
            "scope": "DESCENDANT_S03_TEST_FIXTURE_ONLY",
            "historical_predecessor": {
                "commit": EXPECTED_BASE_SHA,
                "tree": EXPECTED_BASE_TREE,
                "manifest": {
                    "path": "docs/v3/r1/g00/s02/MANIFEST.sha256",
                    "git_blob_sha": "b937e52ad8f23db2913968b0297cf0640306862b",
                    "sha256": ("1107e55b8aef11722b202ab42c0fdff2b4c3a8cc0f8d720485b7c7f9856a2ae6"),
                },
                "test_helper": {
                    "path": "tools/ysf/tests/unit/test_governance_baseline_validator.py",
                    "git_blob_sha": "43fc00598ff02ef083b4ef90142a2d085b91565f",
                    "sha256": ("e85bb9e42e6dd0ac8901d06d5e930ead7a72acb0aa29b93824df560f2c745bf7"),
                },
            },
            "descendant_bytes": {
                "manifest": {
                    "path": "docs/v3/r1/g00/s02/MANIFEST.sha256",
                    "sha256": ("3a6973d33e592cac9485632b946128ca64292760204070a5415865597c7b7265"),
                },
                "test_helper": {
                    "path": "tools/ysf/tests/unit/test_governance_baseline_validator.py",
                    "sha256": ("06eded35479d05548e0090cd64e12d3ddf2300ea6c612eb91fdad09518738365"),
                },
            },
            "accepted_s02_branch_mutated": False,
            "s02_human_decision_reinterpreted": False,
            "runtime_or_governance_validator_changed": False,
        },
        "normative_requirements": [
            {
                "id": "V3-R1-OPS-001",
                "source_anchor_id": "V3-R1-SA-061",
                "acceptance_case_id": "V3-R1-AC-061",
                "requirement_sha256": (
                    "00ab0c750536bb89f3c0b3602216a539daaaa5ea3219cf7908a12bfde29dca39"
                ),
            },
            {
                "id": "V3-R1-OPS-002",
                "source_anchor_id": "V3-R1-SA-062",
                "acceptance_case_id": "V3-R1-AC-062",
                "requirement_sha256": (
                    "6b944525092a264b893e429be888e620d1fe691faaaf8731fd8d9a380abdcfd5"
                ),
            },
            {
                "id": "V3-R1-OPS-003",
                "source_anchor_id": "V3-R1-SA-063",
                "acceptance_case_id": "V3-R1-AC-063",
                "requirement_sha256": (
                    "8458b0140a58fc6eca555a4f57a26021afab70d021c54755714c5cbb19e4edfe"
                ),
            },
            {
                "id": "V3-R1-SEC-001",
                "source_anchor_id": "V3-R1-SA-067",
                "acceptance_case_id": "V3-R1-AC-067",
                "requirement_sha256": (
                    "97a68795d4d6d6bc91963b1a2c9a6bc6d1907abb47b7d36f4efb6a8dc44b2233"
                ),
            },
            {
                "id": "V3-R1-SEC-003",
                "source_anchor_id": "V3-R1-SA-069",
                "acceptance_case_id": "V3-R1-AC-069",
                "requirement_sha256": (
                    "9a6fdc24be211952b86d90b1dbc69a9209d2186a1db472329ea4ddfa81fa207d"
                ),
            },
        ],
        "legacy_boundary": {
            "path_glob": "docs/DIP/**",
            "role": "HISTORICAL_PROVENANCE_ONLY",
            "v3_normative_authority": False,
            "v3_maturity_authority": False,
            "scope_expansion_authorized": False,
        },
    }


def _validate_package(root: Path, snapshot: _ValidationSnapshot | None = None) -> dict[str, Any]:
    observed = _content_yaml(root, SPEC_PATH, "FAIL_PACKAGE_SPEC", snapshot)
    if dict(observed) != _expected_spec():
        _fail("FAIL_PACKAGE_SPEC", "Package specification differs from exact contract.")
    return {"result": "PASS", "sha256": _content_sha256(root, SPEC_PATH, snapshot)}


def _validate_provenance(root: Path, snapshot: _ValidationSnapshot | None = None) -> dict[str, Any]:
    observed = _content_yaml(root, PROVENANCE_PATH, "FAIL_SOURCE_PROVENANCE", snapshot)
    expected = _expected_provenance()
    if dict(observed) != expected:
        _fail("FAIL_SOURCE_PROVENANCE", "Source provenance differs from exact binding.")
    file_bindings = [expected["s01_traceability"], *expected["brd_sources"]]
    governance = cast(Mapping[str, Any], expected["s02_governance"])
    file_bindings.extend(
        cast(Mapping[str, Any], governance[key])
        for key in ("candidate", "acceptance_receipt", "package_spec", "standards_provenance")
    )
    for raw_binding in file_bindings:
        binding = cast(Mapping[str, Any], raw_binding)
        path = str(binding["path"])
        if (
            _run_git(root, "rev-parse", f"HEAD:{path}") != binding["git_blob_sha"]
            or _content_sha256(root, path, snapshot) != binding["sha256"]
        ):
            _fail("FAIL_SOURCE_PROVENANCE", "A source blob binding is incorrect.", path=path)
    compatibility = cast(Mapping[str, Any], expected["s02_descendant_compatibility"])
    historical = cast(Mapping[str, Any], compatibility["historical_predecessor"])
    for key in ("manifest", "test_helper"):
        binding = cast(Mapping[str, Any], historical[key])
        path = str(binding["path"])
        if (
            _run_git(root, "rev-parse", f"{EXPECTED_BASE_SHA}:{path}") != binding["git_blob_sha"]
            or _git_file_sha256(root, EXPECTED_BASE_SHA, path) != binding["sha256"]
        ):
            _fail(
                "FAIL_SOURCE_PROVENANCE",
                "Historical S02 compatibility binding is incorrect.",
                path=path,
            )
    descendant = cast(Mapping[str, Any], compatibility["descendant_bytes"])
    for key in ("manifest", "test_helper"):
        binding = cast(Mapping[str, Any], descendant[key])
        path = str(binding["path"])
        if _content_sha256(root, path, snapshot) != binding["sha256"]:
            _fail(
                "FAIL_SOURCE_PROVENANCE",
                "Descendant-only S02 compatibility binding is incorrect.",
                path=path,
            )
    corrective = cast(Mapping[str, Any], expected["corrective_r2"])
    knowledge_input = cast(Mapping[str, Any], corrective["knowledge_input"])
    for key in ("service", "regression_test"):
        binding = cast(Mapping[str, Any], knowledge_input[key])
        path = str(binding["path"])
        if _content_sha256(root, path, snapshot) != binding["sha256"]:
            _fail(
                "FAIL_SOURCE_PROVENANCE",
                "Corrective R2 knowledge binding is incorrect.",
                path=path,
            )
    return {
        "result": "PASS",
        "sha256": _content_sha256(root, PROVENANCE_PATH, snapshot),
    }


def _validate_baseline(root: Path, snapshot: _ValidationSnapshot | None = None) -> dict[str, Any]:
    baseline = _content_yaml(root, BASELINE_PATH, "FAIL_S03_BASELINE", snapshot)
    _exact_keys(
        baseline,
        {
            "schema_version",
            "baseline_id",
            "title",
            "document_set",
            "version",
            "status",
            "checkpoint_type",
            "maturity_target",
            "package_evidence_level",
            "candidate_model",
            "requirements",
            "configuration_contract",
            "access_contract",
            "safety",
        },
        "FAIL_S03_BASELINE",
        "baseline",
    )
    fixed = {
        "schema_version": 1,
        "baseline_id": "V3-R1-G00-S03-CONFIGURATION-ACCESS-CONTROL-BASELINE",
        "title": "Configuration and Access Control Source Baseline",
        "document_set": "V3-R1-G00-S03",
        "version": "0.1.0",
        "status": "DRAFT",
        "checkpoint_type": "SOURCE_IMPLEMENTATION",
        "maturity_target": "PLANNED",
        "package_evidence_level": "SOURCE_VALIDATED_NON_OPERATIONAL",
        "candidate_model": "NONE",
        "configuration_contract": {
            "scopes": ["GLOBAL", "ORGANIZATION", "DEPARTMENT", "STOREFRONT", "USER"],
            "tenant_identity": "EXPLICIT_FOR_NON_GLOBAL",
            "global_tenant_binding": "TENANT_NEUTRAL",
            "cross_tenant_inheritance": "FORBIDDEN",
            "canonical_serialization": "RFC8259_SORTED_KEYS_COMPACT_UTF8",
            "value_digest": "SHA-256",
            "record_and_resolution_digest": "SHA-256_WITH_TENANT_BINDING",
            "immutable_identity_version": True,
            "sensitive_values_allowed": False,
            "inheritance": "EXPLICIT_PARENT_DETERMINISTIC",
            "invalid_resolution": "FAIL_CLOSED",
        },
        "access_contract": {
            "authentication_methods": [
                "SERVICE_ASSERTION",
                "SYNTHETIC_OTP",
                "SYNTHETIC_PASSWORD",
            ],
            "policy_rule_fields": [
                "actor_class",
                "role",
                "method",
                "assurance_requirement",
                "session_rule",
                "failure_behavior",
            ],
            "decisions": ["ALLOW", "DENY"],
            "audit_fields": [
                "actor_class",
                "role",
                "subject_digest",
                "action",
                "resource",
                "data_scope",
                "correlation_digest",
                "authentication_method",
                "assurance_result",
                "session_rule_result",
                "authorization_result",
            ],
            "audit": "DETERMINISTIC_REDACTED_NO_RAW_SUBJECT_OR_CORRELATION",
            "provider_delivery_precondition": (
                "RECOMPUTE_AUTHENTICATION_AND_AUTHORIZATION_FROM_IMMUTABLE_INPUTS"
            ),
            "caller_supplied_decision_authority": "FORBIDDEN",
            "provider_execution": "DISABLED",
        },
        "safety": {
            "synthetic_data_only": True,
            "providers": "OFF",
            "email_mode": "NON_RELAYING",
            "external_effect_budget": "DENY_ALL",
            "maturity_overclaim_forbidden": True,
        },
    }
    for key, expected in fixed.items():
        if baseline.get(key) != expected:
            _fail("FAIL_S03_BASELINE", "Baseline fixed field is incorrect.", field=key)
    traceability = _content_yaml(root, TRACEABILITY_PATH, "FAIL_S01_BINDING", snapshot)
    source_requirements = {
        item["id"]: item["release_requirement"]
        for item in _sequence(traceability.get("requirements"), "FAIL_S01_BINDING", "requirements")
        if isinstance(item, Mapping) and item.get("id") in EXPECTED_REQUIREMENTS
    }
    observed_requirements = _sequence(
        baseline.get("requirements"), "FAIL_S03_BASELINE", "requirements"
    )
    if [item.get("id") for item in observed_requirements if isinstance(item, Mapping)] != list(
        EXPECTED_REQUIREMENTS
    ):
        _fail("FAIL_S03_REQUIREMENTS", "Normative requirement IDs/order are incorrect.")
    for item in observed_requirements:
        requirement = _mapping(item, "FAIL_S03_REQUIREMENTS", "requirement")
        requirement_id = str(requirement["id"])
        expected = {
            "id": requirement_id,
            **cast(dict[str, Any], source_requirements[requirement_id]),
        }
        if dict(requirement) != expected:
            _fail(
                "FAIL_S03_REQUIREMENTS",
                "Requirement bytes differ from the S01 normative mapping.",
                requirement_id=requirement_id,
            )
    return {
        "result": "PASS",
        "requirement_count": len(observed_requirements),
        "sha256": _content_sha256(root, BASELINE_PATH, snapshot),
    }


def _validate_manifest(root: Path, snapshot: _ValidationSnapshot | None = None) -> dict[str, Any]:
    try:
        lines = _content_bytes(root, MANIFEST_PATH, snapshot).decode("utf-8").splitlines()
    except UnicodeError:
        _fail("FAIL_PACKAGE_MANIFEST", "Manifest cannot be read.")
    records: dict[str, str] = {}
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\r\n]+)", line)
        if match is None:
            _fail("FAIL_PACKAGE_MANIFEST", "Manifest record is malformed.")
        relative = match.group(2)
        pure = PurePosixPath(relative)
        if (
            pure.is_absolute()
            or pure.as_posix() != relative
            or any(part in {"", ".", ".."} for part in pure.parts)
            or relative in records
        ):
            _fail("FAIL_PACKAGE_MANIFEST", "Manifest path is unsafe or duplicated.")
        records[relative] = match.group(1)
    expected_paths = EXPECTED_ALLOWLIST - {MANIFEST_PATH}
    if set(records) != expected_paths:
        _fail("FAIL_PACKAGE_MANIFEST", "Manifest coverage differs from exact S03 scope.")
    for relative, digest in records.items():
        if _content_sha256(root, relative, snapshot) != digest:
            _fail("FAIL_PACKAGE_MANIFEST", "Manifest digest binding failed.", path=relative)
    return {"result": "PASS", "sha256": _content_sha256(root, MANIFEST_PATH, snapshot)}


def _validate_documents(root: Path, snapshot: _ValidationSnapshot | None = None) -> None:
    try:
        text = _content_bytes(root, README_PATH, snapshot).decode("utf-8")
    except UnicodeError:
        _fail("FAIL_DOCUMENT_METADATA", "S03 README is not valid UTF-8.")
    if _PLACEHOLDER.search(text) or _OVERCLAIM.search(text):
        _fail("FAIL_DOCUMENT_CLAIM", "S03 document contains placeholder or overclaim.")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        _fail("FAIL_DOCUMENT_METADATA", "S03 README metadata is missing or malformed.")
    frontmatter_text = text[4:].split("\n---\n", 1)[0]
    metadata = _load_yaml_bytes(
        frontmatter_text.encode("utf-8"), "FAIL_DOCUMENT_METADATA", README_PATH
    )
    if metadata.get("document_code") != "V3-R1-G00-S03-README":
        _fail("FAIL_DOCUMENT_METADATA", "S03 README metadata is missing or duplicated.")


def _validate_coverage_isolation(
    root: Path, snapshot: _ValidationSnapshot | None = None
) -> dict[str, Any]:
    try:
        configuration = tomllib.loads(
            _content_bytes(root, "tools/ysf/pyproject.toml", snapshot).decode("utf-8")
        )
        ignore_lines = _content_bytes(root, ".gitignore", snapshot).decode("utf-8").splitlines()
    except (UnicodeError, tomllib.TOMLDecodeError):
        _fail("FAIL_COVERAGE_ISOLATION", "Coverage isolation configuration is malformed.")
    coverage = _mapping(
        configuration.get("tool", {}).get("coverage"), "FAIL_COVERAGE_ISOLATION", "coverage"
    )
    run = _mapping(coverage.get("run"), "FAIL_COVERAGE_ISOLATION", "coverage.run")
    report = _mapping(coverage.get("report"), "FAIL_COVERAGE_ISOLATION", "coverage.report")
    if dict(run) != {"branch": True, "source": ["ysf"], "data_file": ".coverage.runtime"}:
        _fail("FAIL_COVERAGE_ISOLATION", "Coverage runtime boundary is not exact.")
    if report.get("fail_under") != 90:
        _fail("FAIL_COVERAGE_ISOLATION", "Coverage threshold is below the exact boundary.")
    coverage_rules = [
        line for line in ignore_lines if ".coverage" in line and not line.startswith("#")
    ]
    if coverage_rules != list(EXPECTED_COVERAGE_ISOLATION["gitignore_rules"]):
        _fail("FAIL_COVERAGE_ISOLATION", "Coverage ignore rules differ from the exact boundary.")
    return {
        "result": "PASS",
        "data_file": ".coverage.runtime",
        "environment_override_required": False,
        "tracked_coverage_mutation_allowed": False,
    }


def _validated_repository_root(repository_root: Path) -> Path:
    if not isinstance(repository_root, Path) or not repository_root.is_absolute():
        _fail("FAIL_REPOSITORY_ROOT", "Repository root must be an absolute path.")
    normalized = Path(os.path.normpath(os.fspath(repository_root)))
    if normalized != repository_root or ".." in repository_root.parts:
        _fail("FAIL_REPOSITORY_ROOT", "Repository root path is not normalized.")
    descriptor = _open_absolute_directory(repository_root, "FAIL_REPOSITORY_ROOT")
    os.close(descriptor)
    return repository_root


def _freeze_contract_value(value: Any) -> Any:
    try:
        if isinstance(value, Mapping):
            copied = {key: _freeze_contract_value(item) for key, item in tuple(value.items())}
            return MappingProxyType(copied)
        if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
            return tuple(_freeze_contract_value(item) for item in tuple(value))
    except (RuntimeError, TypeError, ValueError):
        _fail("FAIL_SNAPSHOT_CONTRACT", "Snapshot contract changed while being frozen.")
    return value


def _freeze_snapshot_contract(contract: Mapping[str, Any]) -> Mapping[str, Any]:
    frozen = _freeze_contract_value(contract)
    return _mapping(frozen, "FAIL_SNAPSHOT_CONTRACT", "snapshot contract")


def _accepted_origin(origin: str) -> str:
    ssh_user = "git"
    accepted = {
        f"{ssh_user}@github-ysim:nvkhoabk/ysim.git",
        f"{ssh_user}@github.com:nvkhoabk/ysim.git",
        "https://github.com/nvkhoabk/ysim.git",
    }
    if origin not in accepted:
        _fail("FAIL_REPOSITORY_IDENTITY", "Repository origin is unauthorized.")
    return EXPECTED_REPOSITORY


def _validate_exact_scalar_mapping(
    observed: Mapping[str, Any], expected: Mapping[str, Any], code: str, label: str
) -> None:
    _exact_keys(observed, set(expected), code, label)
    for key, expected_value in expected.items():
        observed_value = observed[key]
        if type(observed_value) is not type(expected_value) or observed_value != expected_value:
            _fail(code, f"{label} differs from the exact boundary.", field=key)


def _validate_contract_paths(value: Any, expected: frozenset[str], label: str) -> list[str]:
    code = "FAIL_SNAPSHOT_CONTRACT"
    observed = list(_sequence(value, code, label))
    for relative in observed:
        if not isinstance(relative, str):
            _fail(code, f"{label} contains a non-string path.")
        pure = PurePosixPath(relative)
        if (
            pure.is_absolute()
            or pure.as_posix() != relative
            or any(part in {"", ".", ".."} for part in pure.parts)
        ):
            _fail(code, f"{label} contains an unsafe path.")
    if observed != sorted(expected):
        _fail(code, f"{label} differs from the exact sorted boundary.")
    return observed


def _validate_snapshot_contract(contract: Mapping[str, Any]) -> None:
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
            "validation_boundaries",
        },
        code,
        "snapshot contract",
    )
    if type(contract.get("schema_version")) is not int or contract["schema_version"] != 2:
        _fail(code, "Snapshot schema version is incorrect.")
    repository = _mapping(contract.get("repository"), code, "repository")
    _exact_keys(repository, {"identity", "origin", "branch"}, code, "repository")
    if (
        repository.get("identity") != EXPECTED_REPOSITORY
        or repository.get("branch") != EXPECTED_BRANCH
        or _accepted_origin(str(repository.get("origin"))) != EXPECTED_REPOSITORY
    ):
        _fail(code, "Snapshot repository binding is incorrect.")
    topology = _mapping(contract.get("topology"), code, "topology")
    topology_keys = {
        "base_sha",
        "base_tree",
        "corrective_parent_sha",
        "corrective_parent_tree",
        "expected_head_sha",
        "expected_head_tree",
        "base_to_head_commit_count",
        "parent_to_head_commit_count",
    }
    _exact_keys(topology, topology_keys, code, "topology")
    for key in topology_keys - {"base_to_head_commit_count", "parent_to_head_commit_count"}:
        pattern = _GIT_SHA
        if not isinstance(topology.get(key), str) or pattern.fullmatch(str(topology[key])) is None:
            _fail(code, "Snapshot contains malformed Git identity.")
    for key in ("base_to_head_commit_count", "parent_to_head_commit_count"):
        if type(topology.get(key)) is not int:
            _fail(code, "Snapshot contains malformed commit count.")
    if (
        topology.get("base_sha") != EXPECTED_BASE_SHA
        or topology.get("base_tree") != EXPECTED_BASE_TREE
        or topology.get("corrective_parent_sha") != EXPECTED_CORRECTIVE_PARENT_SHA
        or topology.get("corrective_parent_tree") != EXPECTED_CORRECTIVE_PARENT_TREE
        or topology.get("base_to_head_commit_count") != 5
        or topology.get("parent_to_head_commit_count") != 1
    ):
        _fail(code, "Snapshot topology differs from the exact corrective stack.")
    _validate_contract_paths(contract.get("changed_paths"), EXPECTED_CHANGED_PATHS, "changed_paths")
    _validate_contract_paths(
        contract.get("authorized_paths"), EXPECTED_ALLOWLIST, "authorized_paths"
    )
    modes = _mapping(contract.get("file_modes"), code, "file_modes")
    if set(modes) != EXPECTED_ALLOWLIST or any(
        not isinstance(value, str) or value != "100644" for value in modes.values()
    ):
        _fail(code, "Snapshot modes differ from exact 100644 boundary.")
    artifacts = _mapping(contract.get("artifact_digests"), code, "artifact_digests")
    _exact_keys(artifacts, set(EXPECTED_ARTIFACT_PATHS), code, "artifact_digests")
    if any(
        not isinstance(value, str) or _SHA256.fullmatch(value) is None
        for value in artifacts.values()
    ):
        _fail(code, "Snapshot artifact digest is malformed.")
    boundaries = _mapping(contract.get("validation_boundaries"), code, "validation_boundaries")
    _exact_keys(boundaries, {"knowledge_input", "branch_coverage"}, code, "validation_boundaries")
    knowledge = _mapping(boundaries.get("knowledge_input"), code, "knowledge_input")
    coverage = _mapping(boundaries.get("branch_coverage"), code, "branch_coverage")
    _validate_exact_scalar_mapping(knowledge, EXPECTED_KNOWLEDGE_BOUNDARY, code, "knowledge_input")
    _validate_exact_scalar_mapping(
        coverage, EXPECTED_BRANCH_COVERAGE_BOUNDARY, code, "branch_coverage"
    )


def load_snapshot_contract(path: Path) -> Mapping[str, Any]:
    captured = _stable_read_absolute(path, "FAIL_SNAPSHOT_CONTRACT")
    return _load_yaml_bytes(captured, "FAIL_SNAPSHOT_CONTRACT", path.name)


def _changed_paths(root: Path) -> set[str]:
    raw = _run_git(root, "diff", "--name-only", "-z", f"{EXPECTED_BASE_SHA}...HEAD")
    paths: set[str] = set()
    for relative in raw.split("\0"):
        if not relative:
            continue
        pure = PurePosixPath(relative)
        if pure.is_absolute() or pure.as_posix() != relative or ".." in pure.parts:
            _fail("FAIL_PATH_SAFETY", "Observed changed path is unsafe.")
        paths.add(relative)
    return paths


def _observe_bound_file(root: Path, relative: str, snapshot: _ValidationSnapshot) -> str:
    snapshot.read(relative)
    record = _run_git(root, "ls-tree", "HEAD", "--", relative)
    match = re.fullmatch(r"(\d{6}) blob [0-9a-f]{40}\t.+", record)
    if match is None:
        _fail("FAIL_FILE_MODE", "Authorized path is not a regular Git blob.", path=relative)
    return match.group(1)


def _observe_repository(
    root: Path, contract: Mapping[str, Any], snapshot: _ValidationSnapshot
) -> set[str]:
    if platform.system() != "Linux":
        _fail("FAIL_ENVIRONMENT_IDENTITY", "S03 source validation requires Linux.")
    repository_contract = cast(Mapping[str, Any], contract["repository"])
    topology = cast(Mapping[str, Any], contract["topology"])
    top = Path(_run_git(root, "rev-parse", "--show-toplevel"))
    origin = _run_git(root, "remote", "get-url", "origin")
    branch = _run_git(root, "branch", "--show-current")
    if (
        top != root
        or _accepted_origin(origin) != repository_contract["identity"]
        or origin != repository_contract["origin"]
        or branch != repository_contract["branch"]
    ):
        _fail("FAIL_REPOSITORY_IDENTITY", "Observed repository identity is incorrect.")
    status = subprocess.run(
        ["git", "-C", str(root), "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        check=False,
        capture_output=True,
    )
    if status.returncode != 0:
        _fail("FAIL_REPOSITORY_IDENTITY", "Unable to observe repository status.")
    if status.stdout:
        _fail("FAIL_DIRTY_WORKTREE", "Public S03 validation requires a clean checkout.")
    if _run_git(root, "rev-parse", f"{EXPECTED_BASE_SHA}^{{tree}}") != EXPECTED_BASE_TREE:
        _fail("FAIL_BASE_IDENTITY", "Observed stacked base is incorrect.")
    head = _run_git(root, "rev-parse", "HEAD")
    tree = _run_git(root, "rev-parse", "HEAD^{tree}")
    if head != topology["expected_head_sha"]:
        _fail("FAIL_HEAD_IDENTITY", "Observed head differs from snapshot.")
    if tree != topology["expected_head_tree"]:
        _fail("FAIL_HEAD_TREE", "Observed tree differs from snapshot.")
    if (
        _run_git(root, "rev-parse", "HEAD^") != EXPECTED_CORRECTIVE_PARENT_SHA
        or _run_git(root, "rev-parse", "HEAD^^{tree}") != EXPECTED_CORRECTIVE_PARENT_TREE
    ):
        _fail("FAIL_BASE_IDENTITY", "Observed corrective parent is incorrect.")
    if int(_run_git(root, "rev-list", "--count", f"{EXPECTED_BASE_SHA}..HEAD")) != 5:
        _fail("FAIL_COMMIT_TOPOLOGY", "Observed base-to-head count is incorrect.")
    if int(_run_git(root, "rev-list", "--count", f"{EXPECTED_CORRECTIVE_PARENT_SHA}..HEAD")) != 1:
        _fail("FAIL_COMMIT_TOPOLOGY", "Observed parent-to-head count is incorrect.")
    modes = {
        relative: _observe_bound_file(root, relative, snapshot)
        for relative in sorted(EXPECTED_ALLOWLIST)
    }
    if modes != dict(cast(Mapping[str, str], contract["file_modes"])):
        _fail("FAIL_FILE_MODE", "Observed modes differ from snapshot.")
    changed = _changed_paths(root)
    if changed != set(cast(Sequence[str], contract["changed_paths"])):
        _fail("FAIL_FILE_ALLOWLIST", "Observed paths differ from snapshot.")
    return changed


def _validate_snapshot_artifact_digests(
    root: Path, contract: Mapping[str, Any], snapshot: _ValidationSnapshot
) -> dict[str, str]:
    artifacts = cast(Mapping[str, str], contract["artifact_digests"])
    actual = {
        relative: _content_sha256(root, relative, snapshot) for relative in EXPECTED_ARTIFACT_PATHS
    }
    if actual != dict(artifacts):
        _fail("FAIL_SNAPSHOT_ARTIFACT", "External artifact digest binding failed.")
    return actual


def _validate_external_snapshot_bindings(
    root: Path,
    contract: Mapping[str, Any],
    actual_artifacts: Mapping[str, str],
    package: Mapping[str, Any],
    provenance: Mapping[str, Any],
    manifest: Mapping[str, Any],
    snapshot: _ValidationSnapshot,
) -> dict[str, Any]:
    validated = {
        SPEC_PATH: package["sha256"],
        MANIFEST_PATH: manifest["sha256"],
        PROVENANCE_PATH: provenance["sha256"],
    }
    if dict(actual_artifacts) != validated:
        _fail("FAIL_SNAPSHOT_ARTIFACT", "Validated artifact digests differ from the snapshot.")
    package_document = _content_yaml(root, SPEC_PATH, "FAIL_PACKAGE_SPEC", snapshot)
    provenance_document = _content_yaml(root, PROVENANCE_PATH, "FAIL_SOURCE_PROVENANCE", snapshot)
    package_boundaries = cast(Mapping[str, Any], package_document["validation_gates"])
    corrective_r4 = cast(Mapping[str, Any], provenance_document["corrective_r4"])
    provenance_contract = cast(Mapping[str, Any], corrective_r4["external_snapshot_contract"])
    boundaries = cast(Mapping[str, Any], contract["validation_boundaries"])
    if (
        dict(cast(Mapping[str, Any], boundaries["knowledge_input"]))
        != dict(cast(Mapping[str, Any], package_boundaries["knowledge_input"]))
        or dict(cast(Mapping[str, Any], boundaries["branch_coverage"]))
        != dict(cast(Mapping[str, Any], package_boundaries["branch_coverage"]))
        or dict(cast(Mapping[str, Any], boundaries["knowledge_input"]))
        != dict(cast(Mapping[str, Any], provenance_contract["knowledge_input"]))
        or dict(cast(Mapping[str, Any], boundaries["branch_coverage"]))
        != dict(cast(Mapping[str, Any], provenance_contract["branch_coverage"]))
    ):
        _fail("FAIL_SNAPSHOT_BOUNDARY", "External validation boundaries are not cross-bound.")
    return {
        "result": "PASS",
        "schema_version": 2,
        "authorized_paths": sorted(EXPECTED_ALLOWLIST),
        "artifact_digests": dict(actual_artifacts),
        "knowledge_input": dict(EXPECTED_KNOWLEDGE_BOUNDARY),
        "branch_coverage": dict(EXPECTED_BRANCH_COVERAGE_BOUNDARY),
    }


def _scan_snapshot(snapshot: _ValidationSnapshot, changed: set[str]) -> str:
    findings = []
    for relative in sorted(changed):
        findings.extend(scan_bytes(snapshot.read(relative), location=relative))
    if findings:
        raise FactoryFailure(
            "FAIL_SENSITIVE_VALUE",
            "Sensitive or prohibited value detected; raw value suppressed.",
            details={"findings": [item.safe_dict() for item in findings]},
        )
    return "PASS"


def _final_repository_readback(
    root: Path, contract: Mapping[str, Any], snapshot: _ValidationSnapshot
) -> tuple[str, str]:
    topology = cast(Mapping[str, Any], contract["topology"])
    status = subprocess.run(
        ["git", "-C", str(root), "status", "--porcelain=v1", "-z", "--untracked-files=all"],
        check=False,
        capture_output=True,
    )
    if status.returncode != 0 or status.stdout:
        _fail("FAIL_DIRTY_WORKTREE", "Repository changed during validation.")
    head = _run_git(root, "rev-parse", "HEAD")
    tree = _run_git(root, "rev-parse", "HEAD^{tree}")
    branch = _run_git(root, "branch", "--show-current")
    origin = _run_git(root, "remote", "get-url", "origin")
    if (
        head != topology["expected_head_sha"]
        or tree != topology["expected_head_tree"]
        or branch != EXPECTED_BRANCH
        or _accepted_origin(origin) != EXPECTED_REPOSITORY
    ):
        _fail("FAIL_REPOSITORY_IDENTITY", "Repository identity changed during validation.")
    snapshot.verify_root_stable()
    return head, tree


def validate_configuration_access_control(
    repository_root: Path, snapshot_contract: Mapping[str, Any]
) -> dict[str, Any]:
    """Validate exact repository evidence through one shared API/CLI boundary."""

    root = _validated_repository_root(repository_root)
    contract = _freeze_snapshot_contract(snapshot_contract)
    _validate_snapshot_contract(contract)
    with _ValidationSnapshot(root) as captured:
        changed = _observe_repository(root, contract, captured)
        artifact_digests = _validate_snapshot_artifact_digests(root, contract, captured)
        sensitive = _scan_snapshot(captured, changed)
        package = _validate_package(root, captured)
        provenance = _validate_provenance(root, captured)
        baseline = _validate_baseline(root, captured)
        manifest = _validate_manifest(root, captured)
        snapshot = _validate_external_snapshot_bindings(
            root,
            contract,
            artifact_digests,
            package,
            provenance,
            manifest,
            captured,
        )
        _validate_documents(root, captured)
        coverage_isolation = _validate_coverage_isolation(root, captured)
        repository_head, repository_tree = _final_repository_readback(root, contract, captured)
    return {
        "result": "PASS",
        "checkpoint": "V3-R1-G00-S03",
        "title": "Configuration and Access Control Source Baseline",
        "repository_head": repository_head,
        "repository_tree": repository_tree,
        "changed_paths": sorted(changed),
        "requirements": list(EXPECTED_REQUIREMENTS),
        "checkpoint_type": "SOURCE_IMPLEMENTATION",
        "maturity_target": "PLANNED",
        "package_evidence_level": "SOURCE_VALIDATED_NON_OPERATIONAL",
        "candidate_model": "NONE",
        "package": package,
        "provenance": provenance,
        "baseline": baseline,
        "manifest": manifest,
        "snapshot_contract": snapshot,
        "coverage_state_isolation": coverage_isolation,
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
        summary = validate_configuration_access_control(
            args.repository_root, load_snapshot_contract(args.snapshot_contract)
        )
        if args.json:
            print(json.dumps(summary, sort_keys=True))
        else:
            print("V3-R1-G00-S03 validation PASS")
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
