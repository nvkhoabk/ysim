"""Fail-closed validation for the V3-R1 G00-S02 governance baseline."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import subprocess
from collections import Counter
from collections.abc import Mapping, Sequence
from pathlib import Path, PurePosixPath
from typing import Any, NoReturn

import yaml

from ysf.index.documents import build_document_index
from ysf.index.metadata import parse_frontmatter
from ysf.secure_factory.models import FactoryFailure
from ysf.secure_factory.sensitive import require_no_sensitive_values

EXPECTED_REPOSITORY = "nvkhoabk/ysim"
EXPECTED_BRANCH = "feature/v3-r1-g00-s02-governance-requirements-baseline"
EXPECTED_BASE_BRANCH = "feature/v3-r1-g00-s01-traceability-fast-track"
EXPECTED_BASE_COMMIT = "3afc37eb366769603f7a898c53432c444f50726a"
EXPECTED_BASE_TREE = "217db32ea46636a40bc0aa611c653836e461b6de"
EXPECTED_CANONICAL_ROOT = Path("/root/projects/ysim-v2.1/ysim")
EXPECTED_CANDIDATE_PATH = Path(
    "factory/releases/v3-r1-g00-s02-governance-requirements-baseline/"
    "YSim_V3_R1_G00_S02_Governance_Requirements_Baseline_"
    "v0.1.0-candidate.1.md"
)
EXPECTED_WRAPPER_PATH = Path(
    "docs/v3/r1/g00/s02/governance-requirements-baseline.md"
)
EXPECTED_README_PATH = Path("docs/v3/r1/g00/s02/README.md")
EXPECTED_DOCUMENT_CODES = {
    EXPECTED_README_PATH.as_posix(): "V3-R1-G00-S02-README",
    EXPECTED_WRAPPER_PATH.as_posix(): (
        "V3-R1-G00-S02-GOVERNANCE-BASELINE-WRAPPER"
    ),
}
EXPECTED_CANDIDATE_SHA256 = (
    "f3aa80a23a1ab95ab9914263d8c79bf11fc466579f162c79d0302cbfa77c9a77"
)
EXPECTED_CANDIDATE_SIZE = 28555
EXPECTED_ACCEPTANCE_STATEMENT = (
    "ACCEPT V3-R1-G00-S02 version 0.1.0-candidate.1 SHA-256 "
    + EXPECTED_CANDIDATE_SHA256
)
EXPECTED_REQUIREMENTS = tuple(f"V3-R1-GOV-{index:03d}" for index in range(1, 13))
EXPECTED_DECISIONS = {
    requirement_id: "REFINE" if index <= 10 else "DEFER"
    for index, requirement_id in enumerate(EXPECTED_REQUIREMENTS, start=1)
}
EXPECTED_ALLOWLIST = frozenset(
    {
        EXPECTED_README_PATH.as_posix(),
        EXPECTED_WRAPPER_PATH.as_posix(),
        EXPECTED_CANDIDATE_PATH.as_posix(),
        "docs/v3/r1/g00/s02/acceptance-receipt.yaml",
        "docs/v3/r1/g00/s02/package-spec.yaml",
        "docs/v3/r1/g00/s02/MANIFEST.sha256",
        "tools/ysf/src/ysf/governance_baseline/__init__.py",
        "tools/ysf/src/ysf/governance_baseline/validator.py",
        "tools/ysf/tests/unit/test_governance_baseline_validator.py",
    }
)
MANIFEST_PATH = "docs/v3/r1/g00/s02/MANIFEST.sha256"
MANIFEST_COVERAGE = EXPECTED_ALLOWLIST - {MANIFEST_PATH}
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_UTC_TIMESTAMP = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
_PLACEHOLDER = re.compile(
    r"(?i)(?:\bTODO\b|\bTBD\b|\bFIXME\b|CHANGE_ME|REPLACE_ME|\{\{[^}]+\}\})"
)
_FORBIDDEN_STATUS_CLAIM = re.compile(
    r"(?i)\b(?:Business Factory|AI Store Generator)\s+"
    r"(?:is\s+|status\s*[:=]\s*)(?:IMPLEMENTED|OPERATIONAL)\b"
)
_ACCEPTANCE_OVERCLAIM = re.compile(
    r"(?i)(?:\bwrapper\s+(?:is|was)\s+Human-Accepted\b|"
    r"\bHuman Acceptance applies to (?:this|the) wrapper\b)"
)
_REQUIREMENT_HEADING = re.compile(
    r"(?m)^### (V3-R1-GOV-\d{3})\s+—[^\n]*$"
)
_MARKDOWN_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")


def _fail(code: str, message: str, **details: Any) -> NoReturn:
    raise FactoryFailure(code, message, details=details)


def _mapping(value: Any, code: str, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        _fail(code, f"{label} must be a mapping.")
    return value


def _sequence(value: Any, code: str, label: str) -> Sequence[Any]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        _fail(code, f"{label} must be a sequence.")
    return value


def _load_yaml(path: Path, code: str) -> Mapping[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError):
        _fail(code, "Required YAML cannot be read exactly.", path=str(path))
    return _mapping(value, code, path.name)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_candidate_semantics(text: str) -> dict[str, str]:
    """Validate the immutable candidate's exact requirement decision semantics."""

    matches = list(_REQUIREMENT_HEADING.finditer(text))
    ids = [match.group(1) for match in matches]
    if len(ids) != 12 or len(set(ids)) != 12 or set(ids) != set(EXPECTED_REQUIREMENTS):
        _fail(
            "FAIL_GOVERNANCE_REQUIREMENT_IDS",
            "Candidate must contain exactly one section for every GOV-001 through GOV-012.",
            observed=ids,
        )
    decisions: dict[str, str] = {}
    for index, match in enumerate(matches):
        requirement_id = match.group(1)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[match.end() : end]
        decision_matches = re.findall(r"(?m)^\*\*Decision:\*\* `(REFINE|DEFER)`$", section)
        if decision_matches != [EXPECTED_DECISIONS[requirement_id]]:
            _fail(
                "FAIL_GOVERNANCE_DECISION",
                "Requirement decision is missing, duplicated, or incorrect.",
                requirement_id=requirement_id,
            )
        if requirement_id in {"V3-R1-GOV-011", "V3-R1-GOV-012"}:
            if "REFERENCE_ONLY/FUTURE" not in section:
                _fail(
                    "FAIL_DEFERRED_BOUNDARY",
                    "Deferred governance requirement lacks REFERENCE_ONLY/FUTURE binding.",
                    requirement_id=requirement_id,
                )
        decisions[requirement_id] = decision_matches[0]
    if _FORBIDDEN_STATUS_CLAIM.search(text):
        _fail(
            "FAIL_FORBIDDEN_STATUS_CLAIM",
            "Business Factory or AI Store Generator is falsely claimed as implemented.",
        )
    required_structure = (
        "# YSim V3 Release 1 — Governance Requirements Baseline",
        "## 4. Decision Matrix",
        "## 5. Normative requirements",
        "## 6. Cross-requirement validation gates",
        "## 7. Traceability to historical source inputs",
        "## 9. Human Acceptance decision protocol",
        "## 10. Candidate state",
    )
    if any(value not in text for value in required_structure):
        _fail("FAIL_MARKDOWN_STRUCTURE", "Candidate Markdown structure is incomplete.")
    return decisions


def _validate_candidate(repository_root: Path) -> tuple[str, dict[str, str]]:
    candidate = repository_root / EXPECTED_CANDIDATE_PATH
    if not candidate.is_file() or candidate.is_symlink():
        _fail("FAIL_CANDIDATE_DIGEST", "Candidate is missing or not a regular file.")
    data = candidate.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if len(data) != EXPECTED_CANDIDATE_SIZE or digest != EXPECTED_CANDIDATE_SHA256:
        _fail(
            "FAIL_CANDIDATE_DIGEST",
            "Candidate bytes differ from the exact Human-Accepted artifact.",
            size=len(data),
            sha256=digest,
        )
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        _fail("FAIL_CANDIDATE_DIGEST", "Candidate is not valid UTF-8.")
    if (
        "| Status | `CANDIDATE_FOR_HUMAN_ACCEPTANCE` |" not in text
        or "| Human Acceptance | `NOT_RECORDED` |" not in text
    ):
        _fail(
            "FAIL_CANDIDATE_IMMUTABILITY",
            "Candidate's historical pre-acceptance fields were changed in place.",
        )
    return digest, validate_candidate_semantics(text)


def _validate_receipt(repository_root: Path, decisions: Mapping[str, str]) -> str:
    path = repository_root / "docs/v3/r1/g00/s02/acceptance-receipt.yaml"
    receipt = _load_yaml(path, "FAIL_ACCEPTANCE_RECEIPT")
    document = _mapping(receipt.get("document"), "FAIL_ACCEPTANCE_RECEIPT", "document")
    acceptance = _mapping(
        receipt.get("human_acceptance"), "FAIL_ACCEPTANCE_RECEIPT", "human acceptance"
    )
    recorded_decisions = _mapping(
        receipt.get("governance_decisions"),
        "FAIL_ACCEPTANCE_RECEIPT",
        "governance decisions",
    )
    deferred = _mapping(
        receipt.get("deferred_boundary"), "FAIL_ACCEPTANCE_RECEIPT", "deferred boundary"
    )
    boundaries = _mapping(
        receipt.get("authorization_boundaries"),
        "FAIL_ACCEPTANCE_RECEIPT",
        "authorization boundaries",
    )
    scope = _mapping(receipt.get("scope"), "FAIL_ACCEPTANCE_RECEIPT", "scope")
    if (
        receipt.get("schema_version") != 1
        or receipt.get("checkpoint") != "V3-R1-G00-S02"
        or document.get("id") != "V3-R1-G00-S02-GOVERNANCE-REQUIREMENTS-BASELINE"
        or document.get("version") != "0.1.0-candidate.1"
        or document.get("path") != EXPECTED_CANDIDATE_PATH.as_posix()
        or document.get("size_bytes") != EXPECTED_CANDIDATE_SIZE
        or document.get("sha256") != EXPECTED_CANDIDATE_SHA256
        or document.get("candidate_bytes_immutable") is not True
        or document.get("candidate_status_preserved") != "CANDIDATE_FOR_HUMAN_ACCEPTANCE"
        or document.get("candidate_human_acceptance_field_preserved") != "NOT_RECORDED"
        or document.get("governed_wrapper_path")
        != EXPECTED_WRAPPER_PATH.as_posix()
        or document.get("governed_wrapper_human_accepted") is not False
        or acceptance.get("decision") != "ACCEPT"
        or acceptance.get("statement") != EXPECTED_ACCEPTANCE_STATEMENT
        or acceptance.get("source") != "RECORDED_OUT_OF_BAND"
        or acceptance.get("acceptance_timestamp_utc") != "NOT_PROVIDED"
        or not isinstance(acceptance.get("receipt_created_at_utc"), str)
        or not _UTC_TIMESTAMP.fullmatch(str(acceptance.get("receipt_created_at_utc")))
        or dict(recorded_decisions) != dict(decisions)
        or deferred
        != {
            "V3-R1-GOV-011": "REFERENCE_ONLY/FUTURE",
            "V3-R1-GOV-012": "REFERENCE_ONLY/FUTURE",
        }
        or not boundaries
        or any(value is not False for value in boundaries.values())
        or scope.get("accepted_content") != "Governance Requirements Baseline only"
        or scope.get("accepted_bytes") != "RAW_CANDIDATE_ONLY"
        or scope.get("governed_wrapper_human_accepted") is not False
    ):
        _fail(
            "FAIL_ACCEPTANCE_RECEIPT",
            "Acceptance receipt does not bind the exact accepted candidate and boundaries.",
        )
    return _sha256(path)


def _validate_spec(repository_root: Path, decisions: Mapping[str, str]) -> Mapping[str, Any]:
    path = repository_root / "docs/v3/r1/g00/s02/package-spec.yaml"
    spec = _load_yaml(path, "FAIL_PACKAGE_SPEC")
    baseline = _mapping(spec.get("required_baseline"), "FAIL_PACKAGE_SPEC", "baseline")
    environment = {
        "environment_scope": "WSL:YSim-Debian12:DOCUMENTATION_SOURCE_ONLY",
        "execution_os": "Linux",
        "development_shell": "bash",
        "canonical_repo_root": EXPECTED_CANONICAL_ROOT.as_posix(),
    }
    candidate = _mapping(spec.get("candidate"), "FAIL_PACKAGE_SPEC", "candidate")
    wrapper = _mapping(
        spec.get("governed_wrapper"), "FAIL_PACKAGE_SPEC", "governed wrapper"
    )
    mutations = _mapping(spec.get("mutations"), "FAIL_PACKAGE_SPEC", "mutations")
    requirement_ids = _sequence(
        spec.get("requirement_ids"), "FAIL_PACKAGE_SPEC", "requirement IDs"
    )
    allowed_paths = _sequence(
        spec.get("allowed_paths"), "FAIL_PACKAGE_SPEC", "allowed paths"
    )
    if (
        spec.get("schema_version") != 1
        or spec.get("package_id") != "V3-R1-G00-S02-GOVERNANCE-REQUIREMENTS-BASELINE-R1"
        or spec.get("package_version") != "0.1.0-candidate.1"
        or spec.get("checkpoint") != "V3-R1-G00-S02"
        or spec.get("repository") != EXPECTED_REPOSITORY
        or baseline
        != {
            "branch": EXPECTED_BASE_BRANCH,
            "commit": EXPECTED_BASE_COMMIT,
            "tree": EXPECTED_BASE_TREE,
        }
        or any(spec.get(key) != value for key, value in environment.items())
        or tuple(requirement_ids) != EXPECTED_REQUIREMENTS
        or set(str(item) for item in allowed_paths) != EXPECTED_ALLOWLIST
        or candidate
        != {
            "path": EXPECTED_CANDIDATE_PATH.as_posix(),
            "size_bytes": EXPECTED_CANDIDATE_SIZE,
            "sha256": EXPECTED_CANDIDATE_SHA256,
        }
        or wrapper
        != {
            "path": EXPECTED_WRAPPER_PATH.as_posix(),
            "document_code": EXPECTED_DOCUMENT_CODES[
                EXPECTED_WRAPPER_PATH.as_posix()
            ],
            "human_accepted": False,
        }
        or mutations
        != {
            "source": True,
            "runtime": False,
            "external_provider": False,
            "customer_communication": False,
            "scheduler": False,
        }
        or spec.get("approval_mode") != "HUMAN_ACCEPTANCE_RECORDED_OUT_OF_BAND"
        or spec.get("payment_owner_mode") != "NOT_APPLICABLE"
        or spec.get("money_ledger_impact") != "NONE"
        or spec.get("manifest") != MANIFEST_PATH
        or set(decisions) != set(requirement_ids)
    ):
        _fail("FAIL_PACKAGE_SPEC", "Package specification identity or scope is incorrect.")
    return spec


def _validate_s01_traceability(repository_root: Path) -> None:
    path = repository_root / "docs/v3/r1/g00/s01/traceability-baseline.yaml"
    baseline = _load_yaml(path, "FAIL_TRACEABILITY_BINDING")
    requirements = _sequence(
        baseline.get("requirements"), "FAIL_TRACEABILITY_BINDING", "S01 requirements"
    )
    observed: dict[str, tuple[Any, Any]] = {}
    for raw in requirements:
        requirement = _mapping(raw, "FAIL_TRACEABILITY_BINDING", "S01 requirement")
        requirement_id = requirement.get("id")
        if requirement_id in EXPECTED_REQUIREMENTS:
            observed[str(requirement_id)] = (
                requirement.get("state"),
                requirement.get("disposition"),
            )
    if observed != {key: ("PROPOSED", "REUSE") for key in EXPECTED_REQUIREMENTS}:
        _fail(
            "FAIL_TRACEABILITY_BINDING",
            "S01 governance source states differ from the accepted S02 starting boundary.",
        )


def _validate_document_metadata(repository_root: Path) -> None:
    expected_fields = {
        EXPECTED_README_PATH.as_posix(): {
            "document_code": EXPECTED_DOCUMENT_CODES[
                EXPECTED_README_PATH.as_posix()
            ],
            "document_set": "V3-R1-G00-S02",
            "version": "0.1.0-candidate.1",
            "status": "FROZEN",
            "language": "en",
        },
        EXPECTED_WRAPPER_PATH.as_posix(): {
            "document_code": EXPECTED_DOCUMENT_CODES[
                EXPECTED_WRAPPER_PATH.as_posix()
            ],
            "document_set": "V3-R1-G00-S02",
            "version": "0.1.0-candidate.1",
            "status": "FROZEN",
            "language": "en",
        },
    }
    for relative, expected in expected_fields.items():
        path = repository_root / relative
        metadata = parse_frontmatter(path)
        if any(metadata.get(key) != value for key, value in expected.items()):
            _fail(
                "FAIL_DOCUMENT_METADATA",
                "Governed S02 Markdown metadata is missing or incorrect.",
                path=relative,
            )

    document_index = build_document_index(repository_root)
    records = _sequence(
        document_index.get("documents"), "FAIL_DOCUMENT_METADATA", "documents"
    )
    codes = [
        str(record.get("documentCode"))
        for record in records
        if isinstance(record, Mapping) and record.get("documentCode")
    ]
    duplicates = sorted(code for code, count in Counter(codes).items() if count > 1)
    if duplicates or any(codes.count(code) != 1 for code in EXPECTED_DOCUMENT_CODES.values()):
        _fail(
            "FAIL_DOCUMENT_METADATA",
            "Governed documentCode values must be present and globally unique.",
            duplicates=duplicates,
        )


def _validate_wrapper(repository_root: Path) -> None:
    wrapper = (repository_root / EXPECTED_WRAPPER_PATH).read_text(encoding="utf-8")
    required = (
        "checkpoint `V3-R1-G00-S02`",
        "`0.1.0-candidate.1`",
        EXPECTED_CANDIDATE_PATH.as_posix(),
        "`28555` bytes",
        EXPECTED_CANDIDATE_SHA256,
        "`RECORDED_OUT_OF_BAND`",
        "this wrapper was not Human-Accepted",
        "`V3-R1-GOV-001` through `V3-R1-GOV-010`: `REFINE`",
        "`V3-R1-GOV-011` and `V3-R1-GOV-012`: `DEFER`",
        "`REFERENCE_ONLY/FUTURE`",
        "[Acceptance Receipt](acceptance-receipt.yaml)",
        "Neither the raw candidate acceptance nor this wrapper authorizes merge, tag,\n"
        "release, deployment, production activation",
        "business external effect",
    )
    if any(value not in wrapper for value in required):
        _fail(
            "FAIL_WRAPPER_BINDING",
            "Governed wrapper does not bind the exact accepted raw artifact and boundary.",
        )
    if _ACCEPTANCE_OVERCLAIM.search(wrapper):
        _fail(
            "FAIL_ACCEPTANCE_OVERCLAIM",
            "Governed wrapper falsely claims Human Acceptance.",
        )


def _validate_text_surfaces(repository_root: Path) -> None:
    text_paths = [
        path
        for path in EXPECTED_ALLOWLIST
        if Path(path).suffix in {".md", ".yaml"} and path != MANIFEST_PATH
    ]
    for relative in text_paths:
        text = (repository_root / relative).read_text(encoding="utf-8")
        if _PLACEHOLDER.search(text):
            _fail("FAIL_UNRESOLVED_PLACEHOLDER", "Unresolved template text is present.")
        if _FORBIDDEN_STATUS_CLAIM.search(text):
            _fail(
                "FAIL_FORBIDDEN_STATUS_CLAIM",
                "A document falsely claims deferred capability maturity.",
                path=relative,
            )
    for markdown_path in (EXPECTED_README_PATH, EXPECTED_WRAPPER_PATH):
        document = repository_root / markdown_path
        for target in _MARKDOWN_LINK.findall(document.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (document.parent / target).resolve()
            try:
                relative = resolved.relative_to(repository_root.resolve()).as_posix()
            except ValueError:
                _fail("FAIL_MARKDOWN_LINK", "Markdown link escapes the repository.")
            if relative not in EXPECTED_ALLOWLIST or not resolved.is_file():
                _fail(
                    "FAIL_MARKDOWN_LINK",
                    "Markdown link is missing or outside the allowlist.",
                )

    overclaim_paths = (
        EXPECTED_README_PATH,
        EXPECTED_WRAPPER_PATH,
        Path("docs/v3/r1/g00/s02/acceptance-receipt.yaml"),
    )
    if any(
        _ACCEPTANCE_OVERCLAIM.search(
            (repository_root / path).read_text(encoding="utf-8")
        )
        for path in overclaim_paths
    ):
        _fail(
            "FAIL_ACCEPTANCE_OVERCLAIM",
            "A repository integration surface overclaims Human Acceptance.",
        )


def _validate_manifest(repository_root: Path) -> str:
    path = repository_root / MANIFEST_PATH
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError):
        _fail("FAIL_PACKAGE_MANIFEST", "S02 manifest is unreadable.")
    observed: dict[str, str] = {}
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if match is None:
            _fail("FAIL_PACKAGE_MANIFEST", "S02 manifest line is malformed.")
        digest, relative = match.groups()
        pure = PurePosixPath(relative)
        if pure.is_absolute() or ".." in pure.parts or relative in observed:
            _fail("FAIL_PACKAGE_MANIFEST", "S02 manifest path is unsafe or duplicated.")
        observed[relative] = digest
    if set(observed) != MANIFEST_COVERAGE:
        _fail(
            "FAIL_PACKAGE_MANIFEST",
            "S02 manifest coverage differs from the closed allowlist.",
            missing=sorted(MANIFEST_COVERAGE - set(observed)),
            extra=sorted(set(observed) - MANIFEST_COVERAGE),
        )
    for relative, digest in observed.items():
        target = repository_root / relative
        if not target.is_file() or target.is_symlink() or _sha256(target) != digest:
            _fail(
                "FAIL_PACKAGE_MANIFEST",
                "S02 manifest digest does not match a regular file.",
                path=relative,
            )
    return _sha256(path)


def validate_governance_baseline(
    repository_root: Path,
    *,
    current_base_sha: str = EXPECTED_BASE_COMMIT,
    changed_paths: set[str] | frozenset[str] = EXPECTED_ALLOWLIST,
) -> dict[str, Any]:
    """Validate exact S02 bytes, acceptance, traceability, scope and manifest."""

    root = repository_root.resolve()
    if current_base_sha != EXPECTED_BASE_COMMIT:
        _fail(
            "FAIL_BASE_IDENTITY",
            "S02 package is not based on the exact accepted S01 head.",
            observed=current_base_sha,
        )
    if set(changed_paths) != EXPECTED_ALLOWLIST:
        _fail(
            "FAIL_FILE_ALLOWLIST",
            "Observed S02 changed paths differ from the closed allowlist.",
            missing=sorted(EXPECTED_ALLOWLIST - set(changed_paths)),
            extra=sorted(set(changed_paths) - EXPECTED_ALLOWLIST),
        )
    candidate_digest, decisions = _validate_candidate(root)
    receipt_digest = _validate_receipt(root, decisions)
    _validate_spec(root, decisions)
    _validate_s01_traceability(root)
    _validate_document_metadata(root)
    _validate_wrapper(root)
    _validate_text_surfaces(root)
    manifest_digest = _validate_manifest(root)
    return {
        "checkpoint": "V3-R1-G00-S02",
        "base_commit": EXPECTED_BASE_COMMIT,
        "base_tree": EXPECTED_BASE_TREE,
        "changed_paths": sorted(changed_paths),
        "candidate_path": EXPECTED_CANDIDATE_PATH.as_posix(),
        "candidate_size": EXPECTED_CANDIDATE_SIZE,
        "candidate_sha256": candidate_digest,
        "receipt_sha256": receipt_digest,
        "manifest_sha256": manifest_digest,
        "requirements_total": len(decisions),
        "refine_total": sum(value == "REFINE" for value in decisions.values()),
        "defer_total": sum(value == "DEFER" for value in decisions.values()),
        "human_acceptance": "RECORDED_OUT_OF_BAND",
        "providers": "OFF",
        "external_effect_budget": "DENY_ALL",
        "result": "PASS",
    }


def _run_git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def _git_changed_paths(root: Path) -> set[str]:
    committed = set(
        _run_git(root, "diff", "--name-only", f"{EXPECTED_BASE_COMMIT}...HEAD").splitlines()
    )
    status = subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
            "-z",
        ],
        check=True,
        capture_output=True,
    ).stdout.decode("utf-8").split("\0")
    uncommitted = {entry[3:] for entry in status if entry}
    return committed | uncommitted


def _validate_execution_environment(root: Path) -> tuple[str, set[str]]:
    if (
        platform.system() != "Linux"
        or os.environ.get("WSL_DISTRO_NAME") != "YSim-Debian12"
        or root.resolve() != EXPECTED_CANONICAL_ROOT
    ):
        _fail("FAIL_ENVIRONMENT_IDENTITY", "Execution environment is not canonical WSL.")
    repository = _run_git(root, "rev-parse", "--show-toplevel")
    branch = _run_git(root, "branch", "--show-current")
    origin = _run_git(root, "remote", "get-url", "origin")
    ssh_user = "git"
    accepted_origins = {
        f"{ssh_user}@github-ysim:nvkhoabk/ysim.git",
        f"{ssh_user}@github.com:nvkhoabk/ysim.git",
        "https://github.com/nvkhoabk/ysim.git",
    }
    if (
        Path(repository).resolve() != EXPECTED_CANONICAL_ROOT
        or branch != EXPECTED_BRANCH
        or origin not in accepted_origins
    ):
        _fail("FAIL_ENVIRONMENT_IDENTITY", "Git repository identity is incorrect.")
    head = _run_git(root, "rev-parse", "HEAD")
    if head == EXPECTED_BASE_COMMIT:
        base = head
    else:
        base = _run_git(root, "rev-parse", "HEAD^")
        ancestor = subprocess.run(
            ["git", "-C", str(root), "merge-base", "--is-ancestor", EXPECTED_BASE_COMMIT, "HEAD"]
        ).returncode
        if ancestor != 0:
            _fail("FAIL_BASE_IDENTITY", "Expected S01 head is not an ancestor of S02.")
    changed_paths = _git_changed_paths(root)
    return base, changed_paths


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        root = args.repository_root.resolve()
        base, changed_paths = _validate_execution_environment(root)
        summary = validate_governance_baseline(
            root, current_base_sha=base, changed_paths=changed_paths
        )
        sensitive = require_no_sensitive_values(root / path for path in sorted(changed_paths))
        summary["sensitive_data"] = sensitive.result
        if args.json:
            print(json.dumps(summary, sort_keys=True))
        else:
            print("V3-R1-G00-S02 validation PASS")
        return 0
    except FactoryFailure as failure:
        result = {
            "code": failure.code,
            "details": failure.details,
            "message": str(failure),
            "result": "FAIL",
        }
        print(json.dumps(result, sort_keys=True))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
