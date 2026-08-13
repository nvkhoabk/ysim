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
from collections.abc import Mapping, Sequence
from pathlib import Path, PurePosixPath
from typing import Any, NoReturn, cast

import yaml

from ysf.index.documents import build_document_index
from ysf.secure_factory.models import FactoryFailure
from ysf.secure_factory.sensitive import require_no_sensitive_values

EXPECTED_REPOSITORY = "nvkhoabk/ysim"
EXPECTED_BRANCH = "feature/v3-r1-g00-s03-configuration-access-control-source-baseline"
EXPECTED_BASE_BRANCH = "feature/v3-r1-g00-s02-governance-requirements-baseline"
EXPECTED_BASE_SHA = "6e71bdd58df2c5baddb36783abbc513867656df0"
EXPECTED_BASE_TREE = "b40ef828825e36641695adb23faedf7346102630"
EXPECTED_REQUIREMENTS = (
    "V3-R1-OPS-001",
    "V3-R1-OPS-002",
    "V3-R1-OPS-003",
    "V3-R1-SEC-001",
    "V3-R1-SEC-003",
)
EXPECTED_ALLOWLIST_ORDER = (
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
    "tools/ysf/tests/integration/test_secure_factory_pipeline.py",
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


def _load_yaml(path: Path, code: str) -> Mapping[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError):
        _fail(code, "Required YAML cannot be read exactly.")
    return _mapping(value, code, path.name)


def _sha256(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        _fail("FAIL_REQUIRED_FILE", "Required file cannot be read.")


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
            "binding": "MANDATORY_EXTERNAL_SNAPSHOT_CONTRACT",
            "base_to_head_commit_count": 1,
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


def _validate_package(root: Path) -> dict[str, Any]:
    observed = _load_yaml(root / SPEC_PATH, "FAIL_PACKAGE_SPEC")
    if dict(observed) != _expected_spec():
        _fail("FAIL_PACKAGE_SPEC", "Package specification differs from exact contract.")
    return {"result": "PASS", "sha256": _sha256(root / SPEC_PATH)}


def _validate_provenance(root: Path) -> dict[str, Any]:
    observed = _load_yaml(root / PROVENANCE_PATH, "FAIL_SOURCE_PROVENANCE")
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
            or _sha256(root / path) != binding["sha256"]
        ):
            _fail("FAIL_SOURCE_PROVENANCE", "A source blob binding is incorrect.", path=path)
    return {"result": "PASS", "sha256": _sha256(root / PROVENANCE_PATH)}


def _validate_baseline(root: Path) -> dict[str, Any]:
    baseline = _load_yaml(root / BASELINE_PATH, "FAIL_S03_BASELINE")
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
            "canonical_serialization": "RFC8259_SORTED_KEYS_COMPACT_UTF8",
            "digest": "SHA-256",
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
            "decisions": ["ALLOW", "DENY"],
            "audit": "DETERMINISTIC_REDACTED",
            "provider_delivery_precondition": "AUTHENTICATION_AND_AUTHORIZATION_PASS",
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
    traceability = _load_yaml(root / TRACEABILITY_PATH, "FAIL_S01_BINDING")
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
        "sha256": _sha256(root / BASELINE_PATH),
    }


def _validate_manifest(root: Path) -> dict[str, Any]:
    path = root / MANIFEST_PATH
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError):
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
        target = root / relative
        if target.is_symlink() or not target.is_file() or _sha256(target) != digest:
            _fail("FAIL_PACKAGE_MANIFEST", "Manifest digest binding failed.", path=relative)
    return {"result": "PASS", "sha256": _sha256(path)}


def _validate_documents(root: Path) -> None:
    readme = root / README_PATH
    text = readme.read_text(encoding="utf-8")
    if _PLACEHOLDER.search(text) or _OVERCLAIM.search(text):
        _fail("FAIL_DOCUMENT_CLAIM", "S03 document contains placeholder or overclaim.")
    index = build_document_index(root)
    entries = cast(Sequence[Mapping[str, Any]], index["documents"])
    matches = [item for item in entries if item.get("path") == README_PATH]
    if len(matches) != 1 or matches[0].get("documentCode") != "V3-R1-G00-S03-README":
        _fail("FAIL_DOCUMENT_METADATA", "S03 README metadata is missing or duplicated.")


def _validated_repository_root(repository_root: Path) -> Path:
    if not isinstance(repository_root, Path) or not repository_root.is_absolute():
        _fail("FAIL_REPOSITORY_ROOT", "Repository root must be an absolute path.")
    normalized = Path(os.path.normpath(os.fspath(repository_root)))
    if normalized != repository_root or ".." in repository_root.parts:
        _fail("FAIL_REPOSITORY_ROOT", "Repository root path is not normalized.")
    current = Path(repository_root.anchor)
    try:
        for component in repository_root.parts[1:]:
            current /= component
            observed = os.lstat(current)
            if stat.S_ISLNK(observed.st_mode) or not stat.S_ISDIR(observed.st_mode):
                _fail("FAIL_REPOSITORY_ROOT", "Repository root component is unsafe.")
    except OSError:
        _fail("FAIL_REPOSITORY_ROOT", "Repository root is missing or unsafe.")
    if repository_root.resolve(strict=True) != repository_root:
        _fail("FAIL_REPOSITORY_ROOT", "Repository root is an alias.")
    return repository_root


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


def _validate_snapshot_contract(contract: Mapping[str, Any]) -> None:
    code = "FAIL_SNAPSHOT_CONTRACT"
    _exact_keys(
        contract,
        {"schema_version", "repository", "topology", "changed_paths", "file_modes"},
        code,
        "snapshot contract",
    )
    if type(contract.get("schema_version")) is not int or contract["schema_version"] != 1:
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
    if (
        topology.get("base_sha") != EXPECTED_BASE_SHA
        or topology.get("base_tree") != EXPECTED_BASE_TREE
        or topology.get("base_to_head_commit_count") != 1
        or topology.get("parent_to_head_commit_count") != 1
    ):
        _fail(code, "Snapshot topology differs from the exact one-commit stack.")
    changed = _sequence(contract.get("changed_paths"), code, "changed_paths")
    if list(changed) != sorted(EXPECTED_CHANGED_PATHS):
        _fail(code, "Snapshot changed paths differ from exact observed S03 delta.")
    modes = _mapping(contract.get("file_modes"), code, "file_modes")
    if set(modes) != EXPECTED_CHANGED_PATHS or any(value != "100644" for value in modes.values()):
        _fail(code, "Snapshot modes differ from exact 100644 boundary.")


def load_snapshot_contract(path: Path) -> Mapping[str, Any]:
    if not path.is_absolute() or path.is_symlink() or not path.is_file():
        _fail("FAIL_SNAPSHOT_CONTRACT", "Snapshot contract path is unsafe.")
    return _load_yaml(path, "FAIL_SNAPSHOT_CONTRACT")


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


def _observe_repository(root: Path, contract: Mapping[str, Any]) -> set[str]:
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
    if _run_git(root, "rev-parse", "HEAD^") != EXPECTED_BASE_SHA:
        _fail("FAIL_BASE_IDENTITY", "Observed corrective parent is incorrect.")
    if int(_run_git(root, "rev-list", "--count", f"{EXPECTED_BASE_SHA}..HEAD")) != 1:
        _fail("FAIL_COMMIT_TOPOLOGY", "Observed base-to-head count is incorrect.")
    changed = _changed_paths(root)
    if changed != set(cast(Sequence[str], contract["changed_paths"])):
        _fail("FAIL_FILE_ALLOWLIST", "Observed paths differ from snapshot.")
    modes: dict[str, str] = {}
    for relative in sorted(changed):
        current = root
        for part in PurePosixPath(relative).parts:
            current /= part
            if current.is_symlink():
                _fail("FAIL_PATH_SAFETY", "Changed path contains a symlink.")
        if not current.is_file():
            _fail("FAIL_PATH_SAFETY", "Changed path is not a regular file.")
        record = _run_git(root, "ls-tree", "HEAD", "--", relative)
        match = re.fullmatch(r"(\d{6}) blob [0-9a-f]{40}\t.+", record)
        if match is None:
            _fail("FAIL_FILE_MODE", "Changed path mode cannot be observed.")
        modes[relative] = match.group(1)
    if modes != dict(cast(Mapping[str, str], contract["file_modes"])):
        _fail("FAIL_FILE_MODE", "Observed modes differ from snapshot.")
    return changed


def validate_configuration_access_control(
    repository_root: Path, snapshot_contract: Mapping[str, Any]
) -> dict[str, Any]:
    """Validate exact repository evidence through one shared API/CLI boundary."""

    root = _validated_repository_root(repository_root)
    _validate_snapshot_contract(snapshot_contract)
    changed = _observe_repository(root, snapshot_contract)
    sensitive = require_no_sensitive_values(root / path for path in sorted(changed))
    package = _validate_package(root)
    provenance = _validate_provenance(root)
    baseline = _validate_baseline(root)
    manifest = _validate_manifest(root)
    _validate_documents(root)
    return {
        "result": "PASS",
        "checkpoint": "V3-R1-G00-S03",
        "title": "Configuration and Access Control Source Baseline",
        "repository_head": _run_git(root, "rev-parse", "HEAD"),
        "repository_tree": _run_git(root, "rev-parse", "HEAD^{tree}"),
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
        "sensitive_data": sensitive.result,
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
