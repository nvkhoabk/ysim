"""Fail-closed validation for the V3-R1 G00-S02 governance baseline."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import platform
import re
import stat
import subprocess
from collections import Counter
from collections.abc import Mapping, Sequence
from pathlib import Path, PurePosixPath
from typing import Any, NoReturn, TypedDict, cast
from xml.etree import ElementTree
from zipfile import BadZipFile, ZipFile

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
EXPECTED_PACKAGE_CANONICAL_ROOT = Path("/root/projects/ysim-v2.1/ysim")
EXPECTED_CANONICAL_ROOT = EXPECTED_PACKAGE_CANONICAL_ROOT
EXPECTED_CANDIDATE_PATH = Path(
    "factory/releases/v3-r1-g00-s02-governance-requirements-baseline/"
    "YSim_V3_R1_G00_S02_Governance_Requirements_Baseline_"
    "v0.1.0-candidate.1.md"
)
EXPECTED_WRAPPER_PATH = Path(
    "docs/v3/r1/g00/s02/governance-requirements-baseline.md"
)
EXPECTED_README_PATH = Path("docs/v3/r1/g00/s02/README.md")
EXPECTED_RECEIPT_PATH = Path("docs/v3/r1/g00/s02/acceptance-receipt.yaml")
EXPECTED_SPEC_PATH = Path("docs/v3/r1/g00/s02/package-spec.yaml")
EXPECTED_PROVENANCE_PATH = Path(
    "docs/v3/r1/g00/s02/standards/standards-provenance.yaml"
)
EXPECTED_SOURCE_DOCX_SHA256 = (
    "47da5d9dc46bb0e136936f865007d988fe537e3a0413676d8d00fe89496fba48"
)
EXPECTED_SOURCE_DOCX_SIZE = 101886
EXPECTED_SOURCE_DOCX_PATH = Path(
    "/root/projects/ysim-v3-r1/evidence/"
    "V3-R1-G00-S02-READONLY-PREFLIGHT-20260811T100321Z/"
    "V3-R1-G00-S02-CORRECTIVE-INPUTS-R1/"
    "YSim_R1_Documentation_Baseline_2026-08-02_v1.2.1.docx"
)
EXPECTED_INPUT_MANIFEST_PATH = EXPECTED_SOURCE_DOCX_PATH.parent / "MANIFEST.sha256"
EXPECTED_INPUT_MANIFEST_SHA256 = (
    "4e55ba9a4dbeb9329d52aa91161a7f0f1f7e73fcc4b31b17896c376a32539249"
)
EXPECTED_INPUT_MANIFEST_SIZE = 417


class StandardBinding(TypedDict):
    code: str
    version: str
    extract_path: str
    extract_sha256: str


EXPECTED_STANDARD_BINDINGS: tuple[StandardBinding, ...] = (
    {
        "code": "YSIM-PCS-001",
        "version": "1.27.1",
        "extract_path": (
            "docs/v3/r1/g00/s02/standards/04_RELEASE_STANDARD_1.27.1.txt"
        ),
        "extract_sha256": (
            "92823bbef5560bf1a958285555814aa3e2afe20e191ddd3e82b6d85c0a940a0b"
        ),
    },
    {
        "code": "YSIM-ENG-001",
        "version": "1.0.1",
        "extract_path": (
            "docs/v3/r1/g00/s02/standards/"
            "05_ENGINEERING_AND_CODE_GENERATION_STANDARD_1.0.1.txt"
        ),
        "extract_sha256": (
            "a8f475a5c7b3ec72770c92dafd36b079f196e697602d4db300b5a1813da0181d"
        ),
    },
    {
        "code": "YSIM-ENV-001",
        "version": "3.2.1",
        "extract_path": (
            "docs/v3/r1/g00/s02/standards/06_ENVIRONMENT_STANDARD_3.2.1.txt"
        ),
        "extract_sha256": (
            "5512f6ae88772d303f9d478d3f9ea961d7fb17fcc047faaf20b13c974ae58893"
        ),
    },
)
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
        EXPECTED_PROVENANCE_PATH.as_posix(),
        *(binding["extract_path"] for binding in EXPECTED_STANDARD_BINDINGS),
        "tools/ysf/src/ysf/governance_baseline/__init__.py",
        "tools/ysf/src/ysf/governance_baseline/validator.py",
        "tools/ysf/tests/integration/conftest.py",
        "tools/ysf/tests/integration/test_secure_factory_pipeline.py",
        "tools/ysf/tests/unit/test_governance_baseline_validator.py",
    }
)
MANIFEST_PATH = "docs/v3/r1/g00/s02/MANIFEST.sha256"
MANIFEST_COVERAGE = EXPECTED_ALLOWLIST - {MANIFEST_PATH}
EXPECTED_EMAIL_MODE = "NON_RELAYING"
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


def _require_exact_keys(
    value: Mapping[str, Any], expected: set[str], code: str, label: str
) -> None:
    observed = set(value)
    if observed != expected:
        _fail(
            code,
            f"{label} keys differ from the exact schema.",
            missing=sorted(expected - observed),
            extra=sorted(observed - expected),
        )


def _expected_receipt() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "receipt_id": "V3-R1-G00-S02-ACCEPTANCE-RECEIPT-001",
        "checkpoint": "V3-R1-G00-S02",
        "document": {
            "id": "V3-R1-G00-S02-GOVERNANCE-REQUIREMENTS-BASELINE",
            "version": "0.1.0-candidate.1",
            "path": EXPECTED_CANDIDATE_PATH.as_posix(),
            "size_bytes": EXPECTED_CANDIDATE_SIZE,
            "sha256": EXPECTED_CANDIDATE_SHA256,
            "candidate_bytes_immutable": True,
            "candidate_status_preserved": "CANDIDATE_FOR_HUMAN_ACCEPTANCE",
            "candidate_human_acceptance_field_preserved": "NOT_RECORDED",
            "governed_wrapper_path": EXPECTED_WRAPPER_PATH.as_posix(),
            "governed_wrapper_human_accepted": False,
        },
        "human_acceptance": {
            "decision": "ACCEPT",
            "statement": EXPECTED_ACCEPTANCE_STATEMENT,
            "source": "RECORDED_OUT_OF_BAND",
            "acceptance_timestamp_utc": "NOT_PROVIDED",
            "receipt_created_at_utc": "2026-08-11T11:11:08Z",
        },
        "governance_decisions": dict(EXPECTED_DECISIONS),
        "deferred_boundary": {
            "V3-R1-GOV-011": "REFERENCE_ONLY/FUTURE",
            "V3-R1-GOV-012": "REFERENCE_ONLY/FUTURE",
        },
        "scope": {
            "accepted_content": "Governance Requirements Baseline only",
            "accepted_bytes": "RAW_CANDIDATE_ONLY",
            "governed_wrapper_human_accepted": False,
            "implementation_claimed": False,
            "operational_claimed": False,
        },
        "authorization_boundaries": {
            "merge": False,
            "tag": False,
            "release": False,
            "deployment": False,
            "production_activation": False,
            "provider_action": False,
            "payment": False,
            "fulfillment": False,
            "customer_communication": False,
            "scheduler": False,
            "business_external_effects": False,
        },
    }


def _expected_spec() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "package_id": "V3-R1-G00-S02-GOVERNANCE-REQUIREMENTS-BASELINE-R1",
        "package_version": "0.1.0-candidate.1",
        "checkpoint": "V3-R1-G00-S02",
        "repository": EXPECTED_REPOSITORY,
        "required_baseline": {
            "branch": EXPECTED_BASE_BRANCH,
            "commit": EXPECTED_BASE_COMMIT,
            "tree": EXPECTED_BASE_TREE,
        },
        "worktree_entry_mode": "EXPECTED_BASELINE",
        "requirement_ids": list(EXPECTED_REQUIREMENTS),
        "maturity_transition": {
            "from": "PROPOSED",
            "refined_requirements_to": "ACCEPTED_REQUIREMENTS_BASELINE",
            "deferred_requirements_to": "REFERENCE_ONLY/FUTURE",
        },
        "environment_scope": "WSL:YSim-Debian12:DOCUMENTATION_SOURCE_ONLY",
        "execution_os": "Linux",
        "development_shell": "bash",
        "canonical_repo_root": EXPECTED_PACKAGE_CANONICAL_ROOT.as_posix(),
        "governing_standards": {
            "provenance_path": EXPECTED_PROVENANCE_PATH.as_posix(),
            "authoritative_source_sha256": EXPECTED_SOURCE_DOCX_SHA256,
            "bindings": [dict(binding) for binding in EXPECTED_STANDARD_BINDINGS],
        },
        "mutations": {
            "source": True,
            "runtime": False,
            "external_provider": False,
            "customer_communication": False,
            "scheduler": False,
        },
        "approval_mode": "HUMAN_ACCEPTANCE_RECORDED_OUT_OF_BAND",
        "payment_owner_mode": "NOT_APPLICABLE",
        "money_ledger_impact": "NONE",
        "safety": {
            "providers": "OFF",
            "external_effect_budget": "DENY_ALL",
            "email_mode": EXPECTED_EMAIL_MODE,
        },
        "candidate": {
            "path": EXPECTED_CANDIDATE_PATH.as_posix(),
            "size_bytes": EXPECTED_CANDIDATE_SIZE,
            "sha256": EXPECTED_CANDIDATE_SHA256,
        },
        "governed_wrapper": {
            "path": EXPECTED_WRAPPER_PATH.as_posix(),
            "document_code": EXPECTED_DOCUMENT_CODES[
                EXPECTED_WRAPPER_PATH.as_posix()
            ],
            "human_accepted": False,
        },
        "manifest": MANIFEST_PATH,
        "allowed_paths": sorted(EXPECTED_ALLOWLIST),
        "exit_criteria": {
            "validation": "PASS",
            "next_action": "INDEPENDENT_ADVISORY_REREVIEW",
        },
        "safe_stop": (
            "Preserve candidate bytes and the open Draft PR; perform no merge, "
            "release, deployment, runtime action, or business external effect."
        ),
    }


def _expected_provenance() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "binding_id": "V3-R1-G00-S02-GOVERNING-STANDARDS-001",
        "checkpoint": "V3-R1-G00-S02",
        "source": {
            "identity": "YSim_R1_Documentation_Baseline_2026-08-02_v1.2.1",
            "title": "YSim Release 1 — Documentation Baseline v1.2.1",
            "version": "1.2.1",
            "format": "DOCX",
            "filename": "YSim_R1_Documentation_Baseline_2026-08-02_v1.2.1.docx",
            "physical_input_path": EXPECTED_SOURCE_DOCX_PATH.as_posix(),
            "sha256": EXPECTED_SOURCE_DOCX_SHA256,
            "package_manifest_path": (
                EXPECTED_INPUT_MANIFEST_PATH.as_posix()
            ),
            "package_manifest_sha256": EXPECTED_INPUT_MANIFEST_SHA256,
            "authority": "AUTHORITATIVE_DOCUMENTATION_BASELINE",
        },
        "extraction": {
            "method_id": "DOCX_WORDPROCESSINGML_HEADING1_MARKDOWN_REDACTED_V2",
            "source_part": "word/document.xml",
            "boundary_rule": (
                "Exact listed inclusive source body blocks in source order; PCS and ENG "
                "span their complete Heading1 sections, while ENV includes blocks 582 "
                "through 760 and applies the declared deterministic redaction only to "
                "three personal-mailbox values in block 700."
            ),
            "paragraph_rendering": {
                "Heading1": "# ",
                "Heading2": "## ",
                "Heading3": "### ",
                "ListBullet": "- ",
                "ListNumber": "1. ",
                "default": "",
            },
            "table_rendering": (
                "GitHub Markdown table with source row order and pipe escaping."
            ),
            "block_separator": "TWO_LF",
            "final_terminator": "ONE_LF",
            "encoding": "UTF-8",
            "redaction": {
                "source_body_block": 700,
                "match_rule": "RFC_STYLE_EMAIL_ADDRESS_IN_SOURCE_ORDER",
                "exact_match_count": 3,
                "replacement_template": (
                    "<REDACTED:PERSONAL_MAILBOX:{ordinal_2_digit}>"
                ),
                "raw_rendered_block_sha256": (
                    "de819600ca71da5f694f64f6f179ed8f363fb68af231a4e960c9862e2321768a"
                ),
                "redacted_rendered_block_sha256": (
                    "09ba3cc99f13221dab7ed157be5114720f1d93a82b21412b4c5c4ca267ececcf"
                ),
                "preserved_normative_rule": (
                    "Sandbox recipients are limited to the three redacted personal "
                    "mailboxes, or an approved sink that cannot relay externally."
                ),
                "raw_values_retained": False,
            },
        },
        "standards": [
            {
                **EXPECTED_STANDARD_BINDINGS[0],
                "status": "APPROVED FOR RELEASE 1",
                "embedded_document": "04_RELEASE_STANDARD_1.27.1.md",
                "heading": "YSim Package and Release Standard",
                "source_body_blocks_inclusive": [352, 521],
                "extract_size_bytes": 13428,
            },
            {
                **EXPECTED_STANDARD_BINDINGS[1],
                "status": "APPROVED FOR RELEASE 1 PLATFORM WORK",
                "embedded_document": (
                    "05_ENGINEERING_AND_CODE_GENERATION_STANDARD_1.0.1.md"
                ),
                "heading": (
                    "YSim Release 1 — Engineering and Code Generation Standard"
                ),
                "source_body_blocks_inclusive": [522, 581],
                "extract_size_bytes": 6326,
            },
            {
                **EXPECTED_STANDARD_BINDINGS[2],
                "status": "APPROVED CONTRACT; ACTUAL VALUES REQUIRE ENV EVIDENCE",
                "embedded_document": "06_ENVIRONMENT_STANDARD_3.2.1.md",
                "heading": "YSim Release 1 — Environment Standard",
                "source_body_blocks_inclusive": [582, 760],
                "redacted_source_body_blocks": [700],
                "redaction_profile": "PERSONAL_MAILBOX_SOURCE_ORDER_V1",
                "extract_size_bytes": 17183,
            },
        ],
        "scope": {
            "binds_package_spec": EXPECTED_SPEC_PATH.as_posix(),
            "binds_candidate": EXPECTED_CANDIDATE_PATH.as_posix(),
            "extract_human_accepted": False,
            "wrapper_human_accepted": False,
            "candidate_bytes_modified": False,
        },
    }


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
    path = repository_root / EXPECTED_RECEIPT_PATH
    receipt = _load_yaml(path, "FAIL_ACCEPTANCE_RECEIPT")
    expected = _expected_receipt()
    _require_exact_keys(
        receipt, set(expected), "FAIL_ACCEPTANCE_RECEIPT", "acceptance receipt"
    )
    for key in (
        "document",
        "human_acceptance",
        "governance_decisions",
        "deferred_boundary",
        "scope",
        "authorization_boundaries",
    ):
        observed_mapping = _mapping(
            receipt.get(key), "FAIL_ACCEPTANCE_RECEIPT", key
        )
        expected_mapping = _mapping(
            expected[key], "FAIL_ACCEPTANCE_RECEIPT", f"expected {key}"
        )
        _require_exact_keys(
            observed_mapping,
            set(expected_mapping),
            "FAIL_ACCEPTANCE_RECEIPT",
            key,
        )
    if dict(receipt) != expected or dict(receipt["governance_decisions"]) != dict(
        decisions
    ):
        _fail(
            "FAIL_ACCEPTANCE_RECEIPT",
            "Acceptance receipt differs from the complete exact accepted mapping.",
        )
    return _sha256(path)


def _validate_spec(repository_root: Path, decisions: Mapping[str, str]) -> Mapping[str, Any]:
    path = repository_root / EXPECTED_SPEC_PATH
    spec = _load_yaml(path, "FAIL_PACKAGE_SPEC")
    expected = _expected_spec()
    _require_exact_keys(spec, set(expected), "FAIL_PACKAGE_SPEC", "package spec")
    for key in (
        "required_baseline",
        "maturity_transition",
        "governing_standards",
        "mutations",
        "safety",
        "candidate",
        "governed_wrapper",
        "exit_criteria",
    ):
        observed_mapping = _mapping(spec.get(key), "FAIL_PACKAGE_SPEC", key)
        expected_mapping = _mapping(
            expected[key], "FAIL_PACKAGE_SPEC", f"expected {key}"
        )
        _require_exact_keys(
            observed_mapping, set(expected_mapping), "FAIL_PACKAGE_SPEC", key
        )
    if dict(spec) != expected or set(decisions) != set(EXPECTED_REQUIREMENTS):
        _fail(
            "FAIL_PACKAGE_SPEC",
            "Package specification differs from the complete exact governed mapping.",
        )
    return spec


def _validate_standards_provenance(repository_root: Path) -> dict[str, Any]:
    path = repository_root / EXPECTED_PROVENANCE_PATH
    provenance = _load_yaml(path, "FAIL_GOVERNING_STANDARDS")
    expected = _expected_provenance()
    _require_exact_keys(
        provenance,
        set(expected),
        "FAIL_GOVERNING_STANDARDS",
        "standards provenance",
    )
    for key in ("source", "extraction", "scope"):
        observed = _mapping(
            provenance.get(key), "FAIL_GOVERNING_STANDARDS", key
        )
        expected_mapping = _mapping(
            expected[key], "FAIL_GOVERNING_STANDARDS", f"expected {key}"
        )
        _require_exact_keys(
            observed,
            set(expected_mapping),
            "FAIL_GOVERNING_STANDARDS",
            key,
        )
    standards = _sequence(
        provenance.get("standards"),
        "FAIL_GOVERNING_STANDARDS",
        "standards",
    )
    if dict(provenance) != expected or len(standards) != 3:
        _fail(
            "FAIL_GOVERNING_STANDARDS",
            "Governing standards provenance differs from the exact binding.",
        )
    for standard in standards:
        binding = _mapping(
            standard, "FAIL_GOVERNING_STANDARDS", "standard binding"
        )
        extract_path = binding.get("extract_path")
        digest = binding.get("extract_sha256")
        size = binding.get("extract_size_bytes")
        if not isinstance(extract_path, str) or not isinstance(digest, str):
            _fail(
                "FAIL_GOVERNING_STANDARDS",
                "Standard extract identity is malformed.",
            )
        extract = repository_root / extract_path
        if (
            extract.is_symlink()
            or not extract.is_file()
            or extract.stat().st_size != size
            or _sha256(extract) != digest
        ):
            _fail(
                "FAIL_GOVERNING_STANDARDS",
                "A governing standard extract differs from its exact binding.",
                path=extract_path,
            )
        text = extract.read_text(encoding="utf-8")
        if (
            f"Standard ID: {binding.get('code')}" not in text
            or f"Version: {binding.get('version')}" not in text
        ):
            _fail(
                "FAIL_GOVERNING_STANDARDS",
                "A governing standard extract lacks its exact code or version.",
                path=extract_path,
            )
    return {
        "source_sha256": EXPECTED_SOURCE_DOCX_SHA256,
        "provenance_sha256": _sha256(path),
        "extract_sha256": [binding["extract_sha256"] for binding in standards],
    }


def _docx_block_text(block: ElementTree.Element, namespace: dict[str, str]) -> str:
    return "".join(
        item.text or "" for item in block.findall(".//w:t", namespace)
    ).strip()


def _docx_paragraph_style(
    block: ElementTree.Element, namespace: dict[str, str]
) -> str:
    style = block.find("./w:pPr/w:pStyle", namespace)
    if style is None:
        return ""
    word_namespace = namespace["w"]
    return str(style.get(f"{{{word_namespace}}}val") or "")


def _render_docx_block(
    block: ElementTree.Element, namespace: dict[str, str]
) -> list[str]:
    tag = block.tag.rsplit("}", 1)[-1]
    if tag == "p":
        value = _docx_block_text(block, namespace)
        if not value:
            return []
        prefix = {
            "Heading1": "# ",
            "Heading2": "## ",
            "Heading3": "### ",
            "ListBullet": "- ",
            "ListNumber": "1. ",
        }.get(_docx_paragraph_style(block, namespace), "")
        return [prefix + value]
    if tag != "tbl":
        return []
    rows = [
        [
            _docx_block_text(cell, namespace).replace("|", r"\|")
            for cell in row.findall("./w:tc", namespace)
        ]
        for row in block.findall("./w:tr", namespace)
    ]
    if not rows:
        return []
    width = max(len(row) for row in rows)
    padded = [row + [""] * (width - len(row)) for row in rows]
    result = [
        "| " + " | ".join(padded[0]) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    result.extend("| " + " | ".join(row) + " |" for row in padded[1:])
    return result


def _parse_verified_xml(data: bytes) -> ElementTree.Element:
    """Parse XML only after its containing DOCX passed the exact digest gate."""

    parser = ElementTree.XMLPullParser(events=("start", "end"))
    for offset in range(0, len(data), 65536):
        parser.feed(data[offset : offset + 65536])
    parser.close()
    root: ElementTree.Element | None = None
    for raw_event in parser.read_events():
        event, element = cast(tuple[str, ElementTree.Element], raw_event)
        if event == "start" and root is None:
            root = element
    if root is None:
        raise ElementTree.ParseError("verified XML has no root element")
    return root


def _read_external_regular_file(
    path: Path,
    *,
    code: str,
    expected_size: int | None = None,
    expected_sha256: str | None = None,
) -> bytes:
    """Read an absolute path through no-follow descriptors and stable fstat identity."""

    if platform.system() != "Linux" or not path.is_absolute() or not path.parts[1:]:
        _fail(code, "External evidence path is not an absolute Linux file path.")
    directory_fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY | os.O_CLOEXEC)
    file_fd: int | None = None
    try:
        for component in path.parts[1:-1]:
            try:
                observed = os.stat(component, dir_fd=directory_fd, follow_symlinks=False)
                if stat.S_ISLNK(observed.st_mode) or not stat.S_ISDIR(observed.st_mode):
                    _fail(code, "External evidence parent is unsafe.")
                next_fd = os.open(
                    component,
                    os.O_RDONLY | os.O_DIRECTORY | os.O_CLOEXEC | os.O_NOFOLLOW,
                    dir_fd=directory_fd,
                )
            except OSError:
                _fail(code, "External evidence parent is missing or unsafe.")
            os.close(directory_fd)
            directory_fd = next_fd
        filename = path.parts[-1]
        try:
            observed = os.stat(filename, dir_fd=directory_fd, follow_symlinks=False)
            if stat.S_ISLNK(observed.st_mode):
                _fail(code, "External evidence file is a symbolic link.")
            file_fd = os.open(
                filename,
                os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW,
                dir_fd=directory_fd,
            )
        except OSError:
            _fail(code, "External evidence file is missing or unsafe.")
        before = os.fstat(file_fd)
        if not stat.S_ISREG(before.st_mode):
            _fail(code, "External evidence is not a regular file.")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(file_fd, 65536)
            if not chunk:
                break
            chunks.append(chunk)
        after = os.fstat(file_fd)
        stable_identity = (
            before.st_dev,
            before.st_ino,
            before.st_mode,
            before.st_size,
            before.st_mtime_ns,
        )
        if stable_identity != (
            after.st_dev,
            after.st_ino,
            after.st_mode,
            after.st_size,
            after.st_mtime_ns,
        ):
            _fail(code, "External evidence changed while it was being read.")
        data = b"".join(chunks)
        if expected_size is not None and len(data) != expected_size:
            _fail(code, "External evidence size differs from the snapshot contract.")
        digest = hashlib.sha256(data).hexdigest()
        if expected_sha256 is not None and digest != expected_sha256:
            _fail(code, "External evidence digest differs from the snapshot contract.")
        return data
    finally:
        if file_fd is not None:
            os.close(file_fd)
        os.close(directory_fd)


def load_snapshot_contract(path: Path) -> Mapping[str, Any]:
    """Load a mandatory external snapshot contract through the no-follow boundary."""

    data = _read_external_regular_file(path, code="FAIL_SNAPSHOT_CONTRACT")
    try:
        value = yaml.safe_load(data.decode("utf-8"))
    except (UnicodeError, yaml.YAMLError):
        _fail("FAIL_SNAPSHOT_CONTRACT", "Snapshot contract is not exact UTF-8 YAML.")
    return _mapping(value, "FAIL_SNAPSHOT_CONTRACT", "snapshot contract")


def _redact_env_block(lines: list[str]) -> list[str]:
    raw = "\n".join(lines)
    if hashlib.sha256(raw.encode("utf-8")).hexdigest() != (
        "de819600ca71da5f694f64f6f179ed8f363fb68af231a4e960c9862e2321768a"
    ):
        _fail(
            "FAIL_AUTHORITATIVE_STANDARDS_SOURCE",
            "ENV source block 700 differs before redaction.",
        )
    email = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
    ordinal = 0

    def replace(_: re.Match[str]) -> str:
        nonlocal ordinal
        ordinal += 1
        return f"<REDACTED:PERSONAL_MAILBOX:{ordinal:02d}>"

    redacted = email.sub(replace, raw)
    if ordinal != 3 or hashlib.sha256(redacted.encode("utf-8")).hexdigest() != (
        "09ba3cc99f13221dab7ed157be5114720f1d93a82b21412b4c5c4ca267ececcf"
    ):
        _fail(
            "FAIL_AUTHORITATIVE_STANDARDS_SOURCE",
            "ENV block 700 redaction is not the exact deterministic transformation.",
        )
    if "or an approved sink that cannot relay externally." not in redacted:
        _fail(
            "FAIL_AUTHORITATIVE_STANDARDS_SOURCE",
            "ENV block 700 normative sandbox-recipient rule is missing.",
        )
    return redacted.split("\n")


def verify_authoritative_standards_source(
    repository_root: Path, snapshot_contract: Mapping[str, Any]
) -> dict[str, Any]:
    """Verify both authoritative inputs and reproduce all checked-in extracts."""

    inputs = _mapping(
        snapshot_contract.get("authoritative_inputs"),
        "FAIL_SNAPSHOT_CONTRACT",
        "authoritative_inputs",
    )
    docx = _mapping(inputs.get("docx"), "FAIL_SNAPSHOT_CONTRACT", "docx")
    manifest = _mapping(
        inputs.get("manifest"), "FAIL_SNAPSHOT_CONTRACT", "manifest"
    )
    docx_path = Path(str(docx["path"]))
    manifest_path = Path(str(manifest["path"]))
    source_data = _read_external_regular_file(
        docx_path,
        code="FAIL_AUTHORITATIVE_STANDARDS_SOURCE",
        expected_size=int(docx["size_bytes"]),
        expected_sha256=str(docx["sha256"]),
    )
    manifest_data = _read_external_regular_file(
        manifest_path,
        code="FAIL_AUTHORITATIVE_INPUT_MANIFEST",
        expected_size=int(manifest["size_bytes"]),
        expected_sha256=str(manifest["sha256"]),
    )
    membership = re.findall(
        rb"(?m)^([0-9a-f]{64})  ([^\r\n]+)$", manifest_data
    )
    expected_member = docx_path.name.encode("utf-8")
    matches = [digest for digest, name in membership if name == expected_member]
    if matches != [str(docx["sha256"]).encode("ascii")]:
        _fail(
            "FAIL_AUTHORITATIVE_INPUT_MANIFEST",
            "Input manifest does not bind the authoritative DOCX exactly once.",
        )
    try:
        with ZipFile(io.BytesIO(source_data)) as archive:
            document_xml = archive.read("word/document.xml")
            core_xml = archive.read("docProps/core.xml")
    except (BadZipFile, KeyError, OSError):
        _fail(
            "FAIL_AUTHORITATIVE_STANDARDS_SOURCE",
            "Authoritative standards DOCX cannot be read deterministically.",
        )
    namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    try:
        document = _parse_verified_xml(document_xml)
        core = _parse_verified_xml(core_xml)
    except ElementTree.ParseError:
        _fail(
            "FAIL_AUTHORITATIVE_STANDARDS_SOURCE",
            "Authoritative standards DOCX XML is malformed.",
        )
    title = core.find("{http://purl.org/dc/elements/1.1/}title")
    if title is None or title.text != "YSim Release 1 — Documentation Baseline v1.2.1":
        _fail(
            "FAIL_AUTHORITATIVE_STANDARDS_SOURCE",
            "Authoritative standards DOCX title is incorrect.",
        )
    body = document.find(".//w:body", namespace)
    if body is None:
        _fail(
            "FAIL_AUTHORITATIVE_STANDARDS_SOURCE",
            "Authoritative standards DOCX has no document body.",
        )
    blocks = list(body)
    ranges = (
        (EXPECTED_STANDARD_BINDINGS[0], ((352, 521),)),
        (EXPECTED_STANDARD_BINDINGS[1], ((522, 581),)),
        (EXPECTED_STANDARD_BINDINGS[2], ((582, 760),)),
    )
    for binding, selected_ranges in ranges:
        lines: list[str] = []
        for first, last in selected_ranges:
            if first < 1 or last > len(blocks) or first > last:
                _fail(
                    "FAIL_AUTHORITATIVE_STANDARDS_SOURCE",
                    "Authoritative standards block range is unavailable.",
                )
            for block_number in range(first, last + 1):
                rendered_block = _render_docx_block(
                    blocks[block_number - 1], namespace
                )
                if binding["code"] == "YSIM-ENV-001" and block_number == 700:
                    rendered_block = _redact_env_block(rendered_block)
                lines.extend(rendered_block)
        rendered = ("\n\n".join(lines) + "\n").encode("utf-8")
        extract = repository_root / str(binding["extract_path"])
        if rendered != extract.read_bytes() or hashlib.sha256(rendered).hexdigest() != str(
            binding["extract_sha256"]
        ):
            _fail(
                "FAIL_AUTHORITATIVE_STANDARDS_SOURCE",
                "A checked-in standard extract is not derived from the authoritative DOCX.",
                path=str(binding["extract_path"]),
            )
    return {
        "source_path": docx_path.as_posix(),
        "source_sha256": str(docx["sha256"]),
        "input_manifest_path": manifest_path.as_posix(),
        "input_manifest_sha256": str(manifest["sha256"]),
        "standard_count": 3,
        "env_block_700_rule_preserved": True,
        "personal_mailbox_values_redacted": True,
        "result": "PASS",
    }


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


def _validate_content(
    repository_root: Path, changed_paths: set[str] | frozenset[str]
) -> dict[str, Any]:
    """Validate S02 content after trusted repository observations pass."""

    root = repository_root.resolve()
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
    standards = _validate_standards_provenance(root)
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
        "standards": standards,
        "requirements_total": len(decisions),
        "refine_total": sum(value == "REFINE" for value in decisions.values()),
        "defer_total": sum(value == "DEFER" for value in decisions.values()),
        "human_acceptance": "RECORDED_OUT_OF_BAND",
        "providers": "OFF",
        "external_effect_budget": "DENY_ALL",
        "email_mode": EXPECTED_EMAIL_MODE,
        "result": "PASS",
    }


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


def _git_changed_paths(root: Path) -> set[str]:
    output = subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "diff",
            "--name-only",
            "-z",
            f"{EXPECTED_BASE_COMMIT}...HEAD",
        ],
        check=False,
        capture_output=True,
    )
    if output.returncode != 0:
        _fail("FAIL_BASE_IDENTITY", "Unable to derive the S02 branch diff.")
    paths: set[str] = set()
    for item in output.stdout.split(b"\0"):
        if not item:
            continue
        try:
            relative = item.decode("utf-8")
        except UnicodeDecodeError:
            _fail("FAIL_PATH_SAFETY", "Changed path is not valid UTF-8.")
        pure = PurePosixPath(relative)
        if (
            not relative
            or pure.is_absolute()
            or ".." in pure.parts
            or pure.as_posix() != relative
        ):
            _fail("FAIL_PATH_SAFETY", "Changed path is not canonical or safe.")
        paths.add(relative)
    return paths


def _validate_path_safety(root: Path, changed_paths: set[str]) -> None:
    for relative in changed_paths:
        current = root
        for part in PurePosixPath(relative).parts:
            current = current / part
            if current.is_symlink():
                _fail(
                    "FAIL_PATH_SAFETY",
                    "A changed path or parent is a symbolic link.",
                    path=relative,
                )
        if not current.is_file():
            _fail(
                "FAIL_PATH_SAFETY",
                "Every changed path must resolve to a regular file.",
                path=relative,
            )


def _validate_snapshot_contract(contract: Mapping[str, Any]) -> None:
    code = "FAIL_SNAPSHOT_CONTRACT"
    _require_exact_keys(
        contract,
        {
            "schema_version",
            "repository",
            "topology",
            "changed_paths",
            "file_modes",
            "authoritative_inputs",
            "standards",
        },
        code,
        "snapshot contract",
    )
    if type(contract.get("schema_version")) is not int or contract["schema_version"] != 1:
        _fail(code, "Snapshot contract schema version is incorrect.")
    repository = _mapping(contract.get("repository"), code, "repository")
    _require_exact_keys(
        repository, {"identity", "origin", "branch"}, code, "repository"
    )
    ssh_user = "git"
    accepted_origins = {
        f"{ssh_user}@github-ysim:nvkhoabk/ysim.git",
        f"{ssh_user}@github.com:nvkhoabk/ysim.git",
        "https://github.com/nvkhoabk/ysim.git",
    }
    if (
        repository.get("identity") != EXPECTED_REPOSITORY
        or repository.get("branch") != EXPECTED_BRANCH
        or repository.get("origin") not in accepted_origins
    ):
        _fail(code, "Snapshot contract repository identity is unauthorized.")
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
    _require_exact_keys(topology, topology_keys, code, "topology")
    for key in topology_keys - {
        "base_to_head_commit_count",
        "parent_to_head_commit_count",
    }:
        value = topology.get(key)
        if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{40}", value) is None:
            _fail(code, "Snapshot contract contains a malformed Git identity.")
    if (
        topology.get("base_sha") != EXPECTED_BASE_COMMIT
        or topology.get("base_tree") != EXPECTED_BASE_TREE
        or topology.get("base_to_head_commit_count") != 3
        or topology.get("parent_to_head_commit_count") != 1
    ):
        _fail(code, "Snapshot contract topology is not the exact three-commit stack.")
    changed_paths = _sequence(contract.get("changed_paths"), code, "changed_paths")
    if (
        any(not isinstance(path, str) for path in changed_paths)
        or list(changed_paths) != sorted(EXPECTED_ALLOWLIST)
    ):
        _fail(code, "Snapshot contract changed paths differ from the exact allowlist.")
    modes = _mapping(contract.get("file_modes"), code, "file_modes")
    if set(modes) != EXPECTED_ALLOWLIST or any(value != "100644" for value in modes.values()):
        _fail(code, "Snapshot contract requires exact 100644 modes for all S02 paths.")
    inputs = _mapping(
        contract.get("authoritative_inputs"), code, "authoritative_inputs"
    )
    _require_exact_keys(inputs, {"docx", "manifest"}, code, "authoritative_inputs")
    expected_inputs = {
        "docx": {
            "path": EXPECTED_SOURCE_DOCX_PATH.as_posix(),
            "size_bytes": EXPECTED_SOURCE_DOCX_SIZE,
            "sha256": EXPECTED_SOURCE_DOCX_SHA256,
        },
        "manifest": {
            "path": EXPECTED_INPUT_MANIFEST_PATH.as_posix(),
            "size_bytes": EXPECTED_INPUT_MANIFEST_SIZE,
            "sha256": EXPECTED_INPUT_MANIFEST_SHA256,
        },
    }
    for label, expected in expected_inputs.items():
        observed = _mapping(inputs.get(label), code, label)
        _require_exact_keys(observed, set(expected), code, label)
        if dict(observed) != expected:
            _fail(code, "Snapshot contract authoritative input binding is incorrect.")
    expected_standards = [
        {
            **dict(EXPECTED_STANDARD_BINDINGS[0]),
            "source_body_ranges": [[352, 521]],
            "redacted_source_blocks": [],
        },
        {
            **dict(EXPECTED_STANDARD_BINDINGS[1]),
            "source_body_ranges": [[522, 581]],
            "redacted_source_blocks": [],
        },
        {
            **dict(EXPECTED_STANDARD_BINDINGS[2]),
            "source_body_ranges": [[582, 760]],
            "redacted_source_blocks": [700],
        },
    ]
    standards = _mapping(contract.get("standards"), code, "standards")
    _require_exact_keys(
        standards,
        {"provenance_path", "provenance_sha256", "bindings"},
        code,
        "standards",
    )
    provenance_digest = standards.get("provenance_sha256")
    if (
        standards.get("provenance_path") != EXPECTED_PROVENANCE_PATH.as_posix()
        or not isinstance(provenance_digest, str)
        or _SHA256.fullmatch(provenance_digest) is None
    ):
        _fail(code, "Snapshot contract standards provenance binding is malformed.")
    bindings = _sequence(standards.get("bindings"), code, "standards bindings")
    if list(bindings) != expected_standards:
        _fail(code, "Snapshot contract standards extraction binding is incorrect.")


def _observed_modes(root: Path, changed_paths: set[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for relative in sorted(changed_paths):
        record = _run_git(root, "ls-tree", "HEAD", "--", relative)
        match = re.fullmatch(r"(\d{6}) blob [0-9a-f]{40}\t.+", record)
        if match is None:
            _fail("FAIL_FILE_MODE", "Unable to derive an exact Git blob mode.")
        result[relative] = match.group(1)
    return result


def _observe_repository(root: Path, contract: Mapping[str, Any]) -> set[str]:
    repository_contract = _mapping(
        contract.get("repository"), "FAIL_SNAPSHOT_CONTRACT", "repository"
    )
    topology = _mapping(
        contract.get("topology"), "FAIL_SNAPSHOT_CONTRACT", "topology"
    )
    if (
        platform.system() != "Linux"
        or os.environ.get("WSL_DISTRO_NAME") != "YSim-Debian12"
        or root.resolve() != EXPECTED_CANONICAL_ROOT
    ):
        _fail("FAIL_ENVIRONMENT_IDENTITY", "Execution environment is not canonical WSL.")
    repository = _run_git(root, "rev-parse", "--show-toplevel")
    branch = _run_git(root, "branch", "--show-current")
    origin = _run_git(root, "remote", "get-url", "origin")
    if (
        Path(repository).resolve() != EXPECTED_CANONICAL_ROOT
        or branch != repository_contract["branch"]
        or origin != repository_contract["origin"]
    ):
        _fail("FAIL_ENVIRONMENT_IDENTITY", "Git repository identity is incorrect.")
    status = subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "status",
            "--porcelain=v1",
            "-z",
            "--untracked-files=all",
        ],
        check=False,
        capture_output=True,
    )
    if status.returncode != 0:
        _fail("FAIL_REPOSITORY_IDENTITY", "Unable to observe Git worktree state.")
    if status.stdout:
        _fail(
            "FAIL_DIRTY_WORKTREE",
            "Public S02 validation requires a clean worktree.",
        )
    base_sha = str(topology["base_sha"])
    base_tree = _run_git(root, "rev-parse", f"{base_sha}^{{tree}}")
    if base_tree != topology["base_tree"]:
        _fail(
            "FAIL_BASE_TREE",
            "Observed S01 base tree differs from the exact stacked base tree.",
            observed=base_tree,
        )
    ancestor = subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "merge-base",
            "--is-ancestor",
            base_sha,
            "HEAD",
        ],
        check=False,
        capture_output=True,
    )
    if ancestor.returncode != 0:
        _fail("FAIL_BASE_IDENTITY", "Expected S01 head is not an ancestor of S02.")
    head = _run_git(root, "rev-parse", "HEAD")
    head_tree = _run_git(root, "rev-parse", "HEAD^{tree}")
    parent = _run_git(root, "rev-parse", "HEAD^")
    parent_tree = _run_git(root, "rev-parse", "HEAD^^{tree}")
    if head != topology["expected_head_sha"]:
        _fail("FAIL_HEAD_IDENTITY", "Observed head differs from the snapshot contract.")
    if head_tree != topology["expected_head_tree"]:
        _fail("FAIL_HEAD_TREE", "Observed head tree differs from the snapshot contract.")
    if parent != topology["corrective_parent_sha"]:
        _fail("FAIL_CORRECTIVE_PARENT", "Observed parent differs from the snapshot contract.")
    if parent_tree != topology["corrective_parent_tree"]:
        _fail("FAIL_CORRECTIVE_PARENT", "Observed parent tree differs from the snapshot contract.")
    base_count = int(_run_git(root, "rev-list", "--count", f"{base_sha}..HEAD"))
    parent_count = int(_run_git(root, "rev-list", "--count", f"{parent}..HEAD"))
    if base_count != topology["base_to_head_commit_count"]:
        _fail("FAIL_COMMIT_TOPOLOGY", "Base-to-head commit count is incorrect.")
    if parent_count != topology["parent_to_head_commit_count"]:
        _fail("FAIL_COMMIT_TOPOLOGY", "Parent-to-head commit count is incorrect.")
    changed_paths = _git_changed_paths(root)
    contract_paths = set(cast(Sequence[str], contract["changed_paths"]))
    if changed_paths != contract_paths:
        _fail(
            "FAIL_FILE_ALLOWLIST",
            "Actual committed S02 paths differ from the revised closed allowlist.",
            missing=sorted(EXPECTED_ALLOWLIST - changed_paths),
            extra=sorted(changed_paths - EXPECTED_ALLOWLIST),
        )
    _validate_path_safety(root, changed_paths)
    modes = _observed_modes(root, changed_paths)
    if modes != dict(cast(Mapping[str, str], contract["file_modes"])):
        _fail("FAIL_FILE_MODE", "Observed Git modes differ from the snapshot contract.")
    return changed_paths


def validate_governance_baseline(
    repository_root: Path, snapshot_contract: Mapping[str, Any]
) -> dict[str, Any]:
    """Validate the repository against a mandatory exact external snapshot contract."""

    root = repository_root.resolve()
    _validate_snapshot_contract(snapshot_contract)
    changed_paths = _observe_repository(root, snapshot_contract)
    sensitive = require_no_sensitive_values(
        root / path for path in sorted(changed_paths)
    )
    summary = _validate_content(root, changed_paths)
    contract_standards = cast(Mapping[str, Any], snapshot_contract["standards"])
    if summary["standards"]["provenance_sha256"] != contract_standards[
        "provenance_sha256"
    ]:
        _fail(
            "FAIL_GOVERNING_STANDARDS",
            "Observed standards provenance digest differs from the snapshot contract.",
        )
    summary["authoritative_standards_source"] = verify_authoritative_standards_source(
        root, snapshot_contract
    )
    summary["sensitive_data"] = sensitive.result
    summary["repository_head"] = _run_git(root, "rev-parse", "HEAD")
    summary["repository_tree"] = _run_git(root, "rev-parse", "HEAD^{tree}")
    return summary


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=Path.cwd())
    parser.add_argument("--snapshot-contract", type=Path, required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        root = args.repository_root.resolve()
        snapshot_contract = load_snapshot_contract(args.snapshot_contract)
        summary = validate_governance_baseline(root, snapshot_contract)
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
