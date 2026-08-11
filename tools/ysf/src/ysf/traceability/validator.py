"""Fail-closed validation for the V3-R1 G00-S01 traceability baseline."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from collections.abc import Mapping, Sequence
from pathlib import Path, PurePosixPath
from typing import Any, NoReturn

import yaml

from ysf.secure_factory.models import FactoryFailure

DEFAULT_REGISTRY_PATH = Path("docs/v3/r1/g00/s01/traceability-baseline.yaml")
EXPECTED_BRD_COUNT = 24
EXPECTED_UXF_COUNT = 7
EXPECTED_CORPUS_COUNT = EXPECTED_BRD_COUNT + EXPECTED_UXF_COUNT
EXPECTED_REQUIREMENT_COUNT = 86
EXPECTED_REPOSITORY = "nvkhoabk/ysim"
EXPECTED_STACKED_BASE_BRANCH = "feature/v3-r1-g00-s00-secure-factory"
EXPECTED_SEED_COMMIT = "a8cfc5d93c8176fc3a727257be609f3af82f38de"
EXPECTED_SEED_TREE = "1953815ee35edc5f6fc487784e4f2bac9191ec1f"
EXPECTED_CANONICAL_ANCHOR_COUNT = 86
EXPECTED_SOURCE_DECISION_PATHS = {
    "docs/BRD/BRD-BO-INDEX.md",
    "docs/BRD/BRD-CAP-INDEX.md",
    "docs/BRD/BRD-EVENT-INDEX.md",
    "docs/BRD/BRD-META-MODEL.md",
    "docs/BRD/BRD-POLICY-INDEX.md",
    "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "docs/UXF/INDEX.md",
    "docs/UXF/UXF-00.md",
    "docs/UXF/UXF-01.md",
    "docs/UXF/UXF-02.md",
    "docs/UXF/UXF-03.md",
}
REQUIREMENT_STATES = {"PROPOSED", "SOURCE_APPROVED", "EXCLUDED", "DEFERRED"}
EXPECTED_REQUIREMENT_STATE_COUNTS = {
    "PROPOSED": 50,
    "SOURCE_APPROVED": 25,
    "EXCLUDED": 9,
    "DEFERRED": 2,
}
MATURITY_LEVELS = {"PLANNED": 0, "IMPLEMENTED": 1, "EXECUTED": 2}
TEST_LEVELS = {"PLANNED": 0, "IMPLEMENTED": 1, "EXECUTED": 2}
EVIDENCE_LEVELS = {"PLANNED": 0, "PRODUCIBLE": 1, "CAPTURED": 2}
DISPOSITIONS = {"REUSE", "REFINE", "EXCLUDE", "DEFER"}
REVIEW_FACETS = {
    "CONFLICT",
    "EXCLUSION",
    "MULTI_SOURCE",
    "DECISION_DEPENDENT",
    "REFINEMENT",
}
_SLICE_PATTERN = re.compile(r"^V3-R1-G\d{2}-S\d{2}$")
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
_GIT_BLOB_PATTERN = re.compile(r"^[0-9a-f]{40}$")
_PLACEHOLDER_PATTERN = re.compile(
    r"(?i)(?:\bTODO\b|\bTBD\b|\bplaceholder\b|unresolved|pending semantic)"
)


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


def _text(value: Any, code: str, label: str) -> str:
    if not isinstance(value, str) or not value:
        _fail(code, f"{label} must be non-empty text.")
    return value


def normalize_statement(value: str) -> str:
    """Return the baseline's stable Unicode and whitespace normalization."""

    return " ".join(unicodedata.normalize("NFC", value).split())


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data, usedforsecurity=False).hexdigest()


def _load_registry(path: Path) -> Mapping[str, Any]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError:
        _fail("FAIL_REGISTRY_READ", "Traceability registry is unavailable.", path=str(path))
    try:
        value = yaml.safe_load(raw)
    except yaml.YAMLError:
        _fail("FAIL_REGISTRY_FORMAT", "Traceability registry is not valid YAML.")
    return _mapping(value, "FAIL_REGISTRY_FORMAT", "registry")


def _canonical_requirement_digest(requirement: Mapping[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(requirement, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
            "utf-8"
        )
    ).hexdigest()


def _canonical_digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
            "utf-8"
        )
    ).hexdigest()


def _validate_authority(registry: Mapping[str, Any]) -> Mapping[str, Any]:
    authority = _mapping(registry.get("authority"), "FAIL_SOURCE_IDENTITY", "authority")
    expected = {
        "repository": EXPECTED_REPOSITORY,
        "stacked_base_branch": EXPECTED_STACKED_BASE_BRANCH,
        "seed_commit": EXPECTED_SEED_COMMIT,
        "seed_tree": EXPECTED_SEED_TREE,
        "source_decision": "SOURCE_INPUT_DECISIONS_RESOLVED",
        "normative_precedence": "V3_R1_BASELINE_AND_EXPLICIT_DECISIONS",
        "final_human_acceptance": "REQUIRED_BEFORE_GOVERNANCE_RECORD",
        "legacy_maturity_transfer": "FORBIDDEN",
    }
    if set(authority) != set(expected) or any(
        authority.get(key) != value for key, value in expected.items()
    ):
        _fail(
            "FAIL_SOURCE_IDENTITY",
            "Traceability authority does not bind the exact corrected S00 source.",
        )
    return authority


def _validate_corpus(
    repository_root: Path, registry: Mapping[str, Any]
) -> tuple[dict[str, Mapping[str, Any]], dict[str, list[str]]]:
    corpus = _mapping(registry.get("corpus"), "FAIL_CORPUS_COUNT", "corpus")
    records = _sequence(corpus.get("files"), "FAIL_CORPUS_COUNT", "corpus.files")
    if (
        corpus.get("expected_brd_count") != EXPECTED_BRD_COUNT
        or corpus.get("expected_uxf_count") != EXPECTED_UXF_COUNT
    ):
        _fail("FAIL_CORPUS_COUNT", "Registry corpus count declaration is stale.")
    actual_by_set = {
        source_set: sorted(
            path
            for path in (repository_root / f"docs/{source_set}").rglob("*")
            if path.is_file() or path.is_symlink()
        )
        for source_set in ("BRD", "UXF")
    }
    expected_counts = {"BRD": EXPECTED_BRD_COUNT, "UXF": EXPECTED_UXF_COUNT}
    if any(len(actual_by_set[key]) != count for key, count in expected_counts.items()):
        _fail(
            "FAIL_CORPUS_COUNT",
            "Repository corpus does not contain exactly 24 BRD and seven UXF files.",
            observed={key: len(paths) for key, paths in actual_by_set.items()},
        )
    if len(records) != EXPECTED_CORPUS_COUNT:
        _fail(
            "FAIL_CORPUS_COUNT",
            "Registry corpus does not contain exactly 31 files.",
            observed_count=len(records),
        )

    by_path: dict[str, Mapping[str, Any]] = {}
    groups: dict[str, list[str]] = {}
    for raw_record in records:
        record = _mapping(raw_record, "FAIL_CORPUS_FORMAT", "corpus file")
        path_text = _text(record.get("path"), "FAIL_CORPUS_FORMAT", "corpus path")
        path = PurePosixPath(path_text)
        source_set = _text(record.get("source_set"), "FAIL_CORPUS_FORMAT", "source_set")
        expected_prefix = f"docs/{source_set}/"
        if source_set not in expected_counts or not path_text.startswith(expected_prefix):
            _fail("FAIL_CORPUS_FORMAT", "Corpus source set and path disagree.", path=path_text)
        if path.is_absolute() or ".." in path.parts or path_text in by_path:
            _fail("FAIL_CORPUS_FORMAT", "Corpus path is unsafe or duplicated.", path=path_text)
        _text(record.get("source_group"), "FAIL_SOURCE_GROUP", "source_group")
        group_status = _text(
            record.get("source_group_status"),
            "FAIL_SOURCE_GROUP",
            "source_group_status",
        )
        if group_status not in {"ASSIGNED", "RESOLVED"}:
            _fail("FAIL_SOURCE_GROUP", "Corpus source group status is invalid.", path=path_text)
        if group_status == "RESOLVED":
            if (
                record.get("source_role") != "SOURCE_INPUT"
                or record.get("normative_requirement_authority") != "NONE"
                or not isinstance(record.get("source_decision_id"), str)
            ):
                _fail(
                    "FAIL_SOURCE_GROUP",
                    "Resolved corpus source lacks an exact non-normative SOURCE_INPUT decision.",
                    path=path_text,
                )
        groups.setdefault(group_status, []).append(path_text)
        file_path = repository_root / path_text
        if not file_path.is_file() or file_path.is_symlink():
            _fail("FAIL_CORPUS_BLOB", "Corpus file is missing or unsafe.", path=path_text)
        expected_blob = _text(record.get("git_blob_sha"), "FAIL_CORPUS_BLOB", "git blob")
        actual_blob = _git_blob_sha(file_path.read_bytes())
        if not _GIT_BLOB_PATTERN.fullmatch(expected_blob) or actual_blob != expected_blob:
            _fail(
                "FAIL_CORPUS_BLOB",
                "Corpus file bytes differ from the exact recorded Git blob.",
                path=path_text,
                expected=expected_blob,
                observed=actual_blob,
            )
        by_path[path_text] = record

    actual_paths = {
        path.relative_to(repository_root).as_posix()
        for paths in actual_by_set.values()
        for path in paths
    }
    if set(by_path) != actual_paths:
        _fail(
            "FAIL_CORPUS_COUNT",
            "Registry and repository corpus inventories differ.",
            missing=sorted(actual_paths - set(by_path)),
            extra=sorted(set(by_path) - actual_paths),
        )
    return by_path, groups


def _validate_source_decisions(
    registry: Mapping[str, Any], corpus: Mapping[str, Mapping[str, Any]]
) -> list[Mapping[str, Any]]:
    raw_decisions = _sequence(
        registry.get("source_decisions"), "FAIL_SOURCE_DECISION", "source decisions"
    )
    if len(raw_decisions) != len(EXPECTED_SOURCE_DECISION_PATHS):
        _fail(
            "FAIL_SOURCE_DECISION",
            "Exactly 11 source corpus decisions are required.",
            observed_count=len(raw_decisions),
        )
    decisions: list[Mapping[str, Any]] = []
    paths: set[str] = set()
    ids: set[str] = set()
    for index, raw_decision in enumerate(raw_decisions, start=1):
        decision = _mapping(raw_decision, "FAIL_SOURCE_DECISION", "source decision")
        expected_id = f"V3-R1-SD-{index:03d}"
        decision_id = _text(
            decision.get("id"), "FAIL_SOURCE_DECISION", "source decision ID"
        )
        path = _text(
            decision.get("source_path"), "FAIL_SOURCE_DECISION", "source decision path"
        )
        if decision_id != expected_id or decision_id in ids or path in paths:
            _fail("FAIL_SOURCE_DECISION", "Source decision identity is stale or duplicated.")
        record = corpus.get(path)
        expected = {
            "id": expected_id,
            "source_path": path,
            "decision": "ACCEPT_AS_SOURCE_INPUT",
            "status": "RESOLVED",
            "source_role": "SOURCE_INPUT",
            "normative_requirement_authority": "NONE",
            "precedence": "V3_R1_BASELINE_AND_EXPLICIT_DECISIONS",
            "draft_adoption": "REQUIRES_EXPLICIT_ADOPTION_OR_REFINEMENT",
            "legacy_maturity_transfer": "FORBIDDEN",
        }
        if (
            record is None
            or record.get("source_group_status") != "RESOLVED"
            or record.get("source_decision_id") != decision_id
            or any(decision.get(key) != value for key, value in expected.items())
            or set(decision) != set(expected) | {"rationale"}
        ):
            _fail(
                "FAIL_SOURCE_DECISION",
                "Source decision does not preserve the exact non-normative input policy.",
                path=path,
            )
        _text(decision.get("rationale"), "FAIL_SOURCE_DECISION", "source rationale")
        ids.add(decision_id)
        paths.add(path)
        decisions.append(decision)
    if paths != EXPECTED_SOURCE_DECISION_PATHS:
        _fail(
            "FAIL_SOURCE_DECISION",
            "Source decision path set differs from the exact 11-document review set.",
            missing=sorted(EXPECTED_SOURCE_DECISION_PATHS - paths),
            extra=sorted(paths - EXPECTED_SOURCE_DECISION_PATHS),
        )
    digest = registry.get("source_decision_matrix_sha256")
    if not isinstance(digest, str) or digest != _canonical_digest(decisions):
        _fail(
            "FAIL_SOURCE_DECISION_DIGEST",
            "Source decision matrix digest is missing or stale.",
        )
    return decisions


def _validate_slices(registry: Mapping[str, Any]) -> set[str]:
    roadmap = _mapping(registry.get("roadmap"), "FAIL_GATE_SLICE_ID", "roadmap")
    raw_slices = _sequence(
        roadmap.get("valid_gate_slices"), "FAIL_GATE_SLICE_ID", "valid_gate_slices"
    )
    slices = {_text(value, "FAIL_GATE_SLICE_ID", "gate/slice ID") for value in raw_slices}
    invalid_slice = any(not _SLICE_PATTERN.fullmatch(value) for value in slices)
    if len(slices) != len(raw_slices) or invalid_slice:
        _fail("FAIL_GATE_SLICE_ID", "Roadmap contains an invalid or duplicate Gate/Slice ID.")
    if "V3-R1-G00-S01" not in slices:
        _fail("FAIL_GATE_SLICE_ID", "Roadmap does not contain the S01 baseline slice.")
    return slices


def _validate_release_requirement(
    requirement_id: str, value: Any
) -> Mapping[str, Any]:
    release_requirement = _mapping(
        value, "FAIL_REQUIREMENT_SEMANTICS", "release requirement"
    )
    if set(release_requirement) != {
        "statement",
        "release_scope",
        "owner",
        "acceptance_criteria",
        "out_of_scope",
    }:
        _fail(
            "FAIL_REQUIREMENT_SEMANTICS",
            "Source-approved requirement semantic fields are incomplete.",
            id=requirement_id,
        )
    for field in ("statement", "release_scope", "owner"):
        text = _text(
            release_requirement.get(field),
            "FAIL_REQUIREMENT_SEMANTICS",
            f"release requirement {field}",
        )
        if len(text) < 12 or _PLACEHOLDER_PATTERN.search(text):
            _fail(
                "FAIL_REQUIREMENT_SEMANTICS",
                "Source-approved requirement contains ambiguous or placeholder semantics.",
                id=requirement_id,
                field=field,
            )
    out_of_scope = _sequence(
        release_requirement.get("out_of_scope"),
        "FAIL_REQUIREMENT_SEMANTICS",
        "release requirement out-of-scope list",
    )
    if not out_of_scope or any(
        len(_text(item, "FAIL_REQUIREMENT_SEMANTICS", "out-of-scope item")) < 8
        or _PLACEHOLDER_PATTERN.search(str(item))
        for item in out_of_scope
    ):
        _fail(
            "FAIL_REQUIREMENT_SEMANTICS",
            "Source-approved requirement lacks an explicit Release 1 boundary.",
            id=requirement_id,
        )
    criteria = _sequence(
        release_requirement.get("acceptance_criteria"),
        "FAIL_REQUIREMENT_SEMANTICS",
        "acceptance criteria",
    )
    if len(criteria) < 2:
        _fail(
            "FAIL_REQUIREMENT_SEMANTICS",
            "Source-approved requirement needs at least two verifiable acceptance criteria.",
            id=requirement_id,
        )
    criterion_ids: set[str] = set()
    for index, raw_criterion in enumerate(criteria, start=1):
        criterion = _mapping(
            raw_criterion, "FAIL_REQUIREMENT_SEMANTICS", "acceptance criterion"
        )
        expected_id = f"{requirement_id}-AC-{index:02d}"
        if set(criterion) != {"id", "condition", "verification"}:
            _fail(
                "FAIL_REQUIREMENT_SEMANTICS",
                "Acceptance criterion fields are incomplete.",
                id=requirement_id,
            )
        criterion_id = criterion.get("id")
        condition = _text(
            criterion.get("condition"),
            "FAIL_REQUIREMENT_SEMANTICS",
            "acceptance condition",
        )
        verification = _text(
            criterion.get("verification"),
            "FAIL_REQUIREMENT_SEMANTICS",
            "acceptance verification",
        )
        if (
            criterion_id != expected_id
            or criterion_id in criterion_ids
            or len(condition) < 16
            or len(verification) < 12
            or _PLACEHOLDER_PATTERN.search(condition)
            or _PLACEHOLDER_PATTERN.search(verification)
        ):
            _fail(
                "FAIL_REQUIREMENT_SEMANTICS",
                "Acceptance criterion is not exact and verifiable.",
                id=requirement_id,
            )
        criterion_ids.add(str(criterion_id))
    return release_requirement


def _validate_requirements(
    registry: Mapping[str, Any], valid_slices: set[str]
) -> dict[str, Mapping[str, Any]]:
    raw_requirements = _sequence(
        registry.get("requirements"), "FAIL_REQUIREMENT_COUNT", "requirements"
    )
    if len(raw_requirements) != EXPECTED_REQUIREMENT_COUNT:
        _fail(
            "FAIL_REQUIREMENT_COUNT",
            "Registry must contain exactly 86 requirements.",
            observed_count=len(raw_requirements),
        )
    requirements: dict[str, Mapping[str, Any]] = {}
    state_counts = {state: 0 for state in REQUIREMENT_STATES}
    for raw_requirement in raw_requirements:
        requirement = _mapping(
            raw_requirement, "FAIL_REQUIREMENT_FORMAT", "requirement"
        )
        requirement_id = _text(
            requirement.get("id"), "FAIL_REQUIREMENT_FORMAT", "requirement ID"
        )
        if requirement_id in requirements:
            _fail("FAIL_REQUIREMENT_COUNT", "Requirement ID is duplicated.", id=requirement_id)
        state = requirement.get("state")
        if state not in REQUIREMENT_STATES:
            _fail(
                "FAIL_REQUIREMENT_STATE",
                "Requirement state is outside the resolved S01 state model.",
                id=requirement_id,
            )
        state_counts[str(state)] += 1
        gate_slice = _text(
            requirement.get("gate_slice"), "FAIL_GATE_SLICE_ID", "requirement gate/slice"
        )
        if gate_slice not in valid_slices or gate_slice == "V3-R1-G00-S01":
            _fail(
                "FAIL_GATE_SLICE_ID",
                "Requirement has an invalid Gate/Slice assignment.",
                id=requirement_id,
                gate_slice=gate_slice,
            )
        disposition = _text(
            requirement.get("disposition"), "FAIL_DISPOSITION", "disposition"
        )
        if disposition not in DISPOSITIONS:
            _fail("FAIL_DISPOSITION", "Requirement disposition is invalid.", id=requirement_id)
        maturity = _text(
            requirement.get("traceability_maturity"),
            "FAIL_TRACEABILITY_MATURITY",
            "traceability maturity",
        )
        if maturity not in MATURITY_LEVELS:
            _fail(
                "FAIL_TRACEABILITY_MATURITY",
                "Requirement traceability maturity is invalid.",
                id=requirement_id,
            )
        facets = _sequence(
            requirement.get("review_facets", []), "FAIL_REVIEW_SELECTION", "review facets"
        )
        if any(value not in REVIEW_FACETS for value in facets) or len(set(facets)) != len(facets):
            _fail("FAIL_REVIEW_SELECTION", "Requirement review facets are invalid.")
        serialized = json.dumps(requirement, ensure_ascii=False)
        if _PLACEHOLDER_PATTERN.search(serialized):
            _fail(
                "FAIL_REQUIREMENT_SEMANTICS",
                "Requirement contains unresolved semantic placeholder text.",
                id=requirement_id,
            )
        if state == "SOURCE_APPROVED":
            if (
                disposition != "REFINE"
                or requirement.get("resolution_decision") != "REFINE"
                or not isinstance(requirement.get("selection_id"), str)
            ):
                _fail(
                    "FAIL_REQUIREMENT_STATE",
                    "SOURCE_APPROVED is permitted only for an exact refined selection.",
                    id=requirement_id,
                )
            _validate_release_requirement(
                requirement_id, requirement.get("release_requirement")
            )
        elif state == "PROPOSED":
            blocker = _text(
                requirement.get("promotion_blocker"),
                "FAIL_REQUIREMENT_SEMANTICS",
                "promotion blocker",
            )
            if (
                disposition != "REUSE"
                or len(blocker) < 16
                or "release_requirement" in requirement
                or "selection_id" in requirement
            ):
                _fail(
                    "FAIL_REQUIREMENT_STATE",
                    (
                        "PROPOSED requirement lacks an exact promotion blocker "
                        "or exceeds its decision scope."
                    ),
                    id=requirement_id,
                )
        else:
            expected_disposition = "EXCLUDE" if state == "EXCLUDED" else "DEFER"
            expected_decision = "EXCLUDE" if state == "EXCLUDED" else "DEFER"
            reason = _text(
                requirement.get("baseline_exclusion_reason"),
                "FAIL_REQUIREMENT_SEMANTICS",
                "baseline exclusion reason",
            )
            if (
                disposition != expected_disposition
                or requirement.get("resolution_decision") != expected_decision
                or requirement.get("source_provenance_retained") is not True
                or not isinstance(requirement.get("selection_id"), str)
                or len(reason) < 16
                or "release_requirement" in requirement
            ):
                _fail(
                    "FAIL_REQUIREMENT_STATE",
                    (
                        "Excluded or deferred item is not bound to its exact "
                        "source-preserving decision."
                    ),
                    id=requirement_id,
                )
        requirements[requirement_id] = requirement
    if state_counts != EXPECTED_REQUIREMENT_STATE_COUNTS:
        _fail(
            "FAIL_REQUIREMENT_STATE",
            "Requirement state counts differ from the resolved 36-item decision matrix.",
            observed=state_counts,
        )
    return requirements


def _validate_anchors(
    repository_root: Path,
    registry: Mapping[str, Any],
    corpus: Mapping[str, Mapping[str, Any]],
    requirements: Mapping[str, Mapping[str, Any]],
) -> dict[str, Mapping[str, Any]]:
    raw_anchors = _sequence(
        registry.get("source_anchors"), "FAIL_SOURCE_ANCHOR_MISSING", "source anchors"
    )
    expected_count = registry.get("exact_anchor_count")
    if not isinstance(expected_count, int):
        _fail("FAIL_SOURCE_ANCHOR_COUNT", "Exact anchor count is missing or invalid.")
    anchors: dict[str, Mapping[str, Any]] = {}
    anchors_by_requirement: dict[str, list[str]] = {key: [] for key in requirements}
    anchored_paths: set[str] = set()
    canonical_owners: dict[tuple[Any, ...], tuple[str, str]] = {}
    for index, raw_anchor in enumerate(raw_anchors, start=1):
        anchor = _mapping(raw_anchor, "FAIL_SOURCE_ANCHOR_STALE", "source anchor")
        anchor_id = _text(anchor.get("id"), "FAIL_SOURCE_ANCHOR_STALE", "anchor ID")
        if anchor_id != f"V3-R1-SA-{index:03d}" or anchor_id in anchors:
            _fail("FAIL_SOURCE_ANCHOR_STALE", "Source anchor ID is duplicated.")
        path = _text(anchor.get("source_path"), "FAIL_SOURCE_ANCHOR_STALE", "source path")
        corpus_record = corpus.get(path)
        if corpus_record is None:
            _fail("FAIL_SOURCE_ANCHOR_STALE", "Source anchor points outside the corpus.")
        if anchor.get("source_set") != corpus_record.get("source_set"):
            _fail("FAIL_SOURCE_ANCHOR_STALE", "Source anchor set does not match its file.")
        blob = anchor.get("git_blob_sha")
        if blob != corpus_record.get("git_blob_sha"):
            _fail("FAIL_SOURCE_ANCHOR_STALE", "Source anchor Git blob is stale.", id=anchor_id)
        heading = _text(anchor.get("heading"), "FAIL_SOURCE_ANCHOR_STALE", "anchor heading")
        locator = _mapping(
            anchor.get("locator"), "FAIL_SOURCE_ANCHOR_STALE", "anchor locator"
        )
        start = locator.get("start_line")
        end = locator.get("end_line")
        if not isinstance(start, int) or not isinstance(end, int) or start < 1 or end < start:
            _fail("FAIL_SOURCE_ANCHOR_STALE", "Source anchor locator is invalid.")
        lines = (repository_root / path).read_text(encoding="utf-8").splitlines()
        if end > len(lines):
            _fail("FAIL_SOURCE_ANCHOR_STALE", "Source anchor locator exceeds its file.")
        preceding_headings = [
            line.lstrip("#").strip() for line in lines[: start - 1] if line.startswith("#")
        ]
        if not preceding_headings or normalize_statement(preceding_headings[-1]) != heading:
            _fail(
                "FAIL_SOURCE_ANCHOR_STALE",
                "Source anchor heading is missing or stale.",
                id=anchor_id,
            )
        actual_statement = normalize_statement("\n".join(lines[start - 1 : end]))
        statement = _text(
            anchor.get("normalized_statement"),
            "FAIL_SOURCE_ANCHOR_STALE",
            "normalized statement",
        )
        if statement != normalize_statement(statement) or statement != actual_statement:
            _fail(
                "FAIL_SOURCE_ANCHOR_STALE",
                "Source anchor statement is missing or stale.",
                id=anchor_id,
            )
        digest = anchor.get("statement_sha256")
        if not isinstance(digest, str) or not _SHA256_PATTERN.fullmatch(digest):
            _fail("FAIL_STATEMENT_DIGEST", "Statement digest format is invalid.")
        if digest != _sha256_text(statement):
            _fail("FAIL_STATEMENT_DIGEST", "Statement digest does not match its anchor.")
        requirement_id = _text(
            anchor.get("requirement_id"), "FAIL_ORPHAN_REQUIREMENT", "anchor requirement"
        )
        canonical_identity = (
            path,
            blob,
            heading,
            start,
            end,
            statement,
            digest,
        )
        existing = canonical_owners.get(canonical_identity)
        if existing is not None:
            existing_id, existing_requirement = existing
            if existing_requirement != requirement_id:
                _fail(
                    "FAIL_SOURCE_ANCHOR_SEMANTIC_BINDING",
                    (
                        "One canonical source identity is bound to requirements "
                        "with different meaning."
                    ),
                    first_anchor=existing_id,
                    duplicate_anchor=anchor_id,
                )
            _fail(
                "FAIL_SOURCE_ANCHOR_DUPLICATE",
                "Canonical source anchor appears more than once.",
                first_anchor=existing_id,
                duplicate_anchor=anchor_id,
            )
        canonical_owners[canonical_identity] = (anchor_id, requirement_id)
        requirement = requirements.get(requirement_id)
        if requirement is None:
            _fail("FAIL_ORPHAN_REQUIREMENT", "Source anchor references an unknown requirement.")
        for field in ("gate_slice", "disposition", "traceability_maturity"):
            if anchor.get(field) != requirement.get(field):
                _fail(
                    "FAIL_SOURCE_ANCHOR_STALE",
                    f"Source anchor {field} does not match its requirement.",
                    id=anchor_id,
                )
        anchors_by_requirement[requirement_id].append(anchor_id)
        anchored_paths.add(path)
        anchors[anchor_id] = anchor

    if (
        expected_count != EXPECTED_CANONICAL_ANCHOR_COUNT
        or expected_count != len(raw_anchors)
        or expected_count != len(canonical_owners)
    ):
        _fail(
            "FAIL_SOURCE_ANCHOR_COUNT",
            "Declared anchor count differs from the exact canonical unique count.",
            declared=expected_count,
            raw=len(raw_anchors),
            unique=len(canonical_owners),
        )

    if anchored_paths != set(corpus):
        _fail(
            "FAIL_SOURCE_ANCHOR_MISSING",
            "Every corpus file must have at least one exact source anchor.",
            paths=sorted(set(corpus) - anchored_paths),
        )
    for requirement_id, requirement in requirements.items():
        declared = _sequence(
            requirement.get("source_anchor_ids"),
            "FAIL_SOURCE_ANCHOR_MISSING",
            "requirement source anchors",
        )
        if not declared or set(declared) != set(anchors_by_requirement[requirement_id]):
            _fail(
                "FAIL_SOURCE_ANCHOR_MISSING",
                "Requirement source-anchor mapping is incomplete or stale.",
                id=requirement_id,
            )
        if "MULTI_SOURCE" in requirement.get("review_facets", []):
            distinct_paths = {str(anchors[str(anchor_id)]["source_path"]) for anchor_id in declared}
            if len(declared) < 2 or len(distinct_paths) < 2:
                _fail(
                    "FAIL_FAKE_MULTI_SOURCE",
                    "Multi-source facet requires multiple distinct canonical source documents.",
                    id=requirement_id,
                )
    return anchors


def _validate_traces(
    registry: Mapping[str, Any], requirements: Mapping[str, Mapping[str, Any]]
) -> None:
    raw_traces = _sequence(registry.get("traces"), "FAIL_ORPHAN_REQUIREMENT", "traces")
    by_requirement: dict[str, Mapping[str, Any]] = {}
    acceptance_ids: set[str] = set()
    test_ids: set[str] = set()
    evidence_ids: set[str] = set()
    for raw_trace in raw_traces:
        trace = _mapping(raw_trace, "FAIL_ORPHAN_REQUIREMENT", "trace")
        requirement_id = _text(
            trace.get("requirement_id"), "FAIL_ORPHAN_REQUIREMENT", "trace requirement"
        )
        if requirement_id not in requirements or requirement_id in by_requirement:
            _fail(
                "FAIL_ORPHAN_REQUIREMENT",
                "Trace references an unknown or duplicate requirement.",
            )
        acceptance = _mapping(
            trace.get("acceptance_case"), "FAIL_ORPHAN_ACCEPTANCE_CASE", "acceptance case"
        )
        acceptance_id = _text(
            acceptance.get("id"), "FAIL_ORPHAN_ACCEPTANCE_CASE", "acceptance case ID"
        )
        if acceptance_id in acceptance_ids or acceptance.get("requirement_id") != requirement_id:
            _fail(
                "FAIL_ORPHAN_ACCEPTANCE_CASE",
                "Acceptance case is duplicated or orphaned from its requirement.",
            )
        test = _mapping(trace.get("test"), "FAIL_ORPHAN_TEST", "test")
        test_id = _text(test.get("id"), "FAIL_ORPHAN_TEST", "test ID")
        if test_id in test_ids or test.get("acceptance_case_id") != acceptance_id:
            _fail("FAIL_ORPHAN_TEST", "Test is duplicated or orphaned from its acceptance case.")
        evidence = _mapping(trace.get("evidence"), "FAIL_ORPHAN_EVIDENCE", "evidence")
        evidence_id = _text(evidence.get("id"), "FAIL_ORPHAN_EVIDENCE", "evidence ID")
        if evidence_id in evidence_ids or evidence.get("test_id") != test_id:
            _fail("FAIL_ORPHAN_EVIDENCE", "Evidence is duplicated or orphaned from its test.")
        if acceptance.get("test_id") != test_id or test.get("evidence_id") != evidence_id:
            _fail("FAIL_ORPHAN_TEST", "Forward trace links are incomplete.")
        requirement = requirements[requirement_id]
        if requirement.get("acceptance_case_id") != acceptance_id:
            _fail("FAIL_ORPHAN_ACCEPTANCE_CASE", "Requirement acceptance link is stale.")

        if requirement.get("state") in {"EXCLUDED", "DEFERRED"}:
            if (
                trace.get("trace_status") != "SOURCE_REFERENCE_ONLY"
                or acceptance.get("traceability_maturity") != "NOT_APPLICABLE"
                or test.get("status") != "NOT_APPLICABLE"
                or evidence.get("status") != "NOT_APPLICABLE"
            ):
                _fail(
                    "FAIL_TRACEABILITY_MATURITY",
                    (
                        "Excluded or deferred source reference must not claim a "
                        "planned execution chain."
                    ),
                    id=requirement_id,
                )
            acceptance_ids.add(acceptance_id)
            test_ids.add(test_id)
            evidence_ids.add(evidence_id)
            by_requirement[requirement_id] = trace
            continue
        if "trace_status" in trace:
            _fail(
                "FAIL_TRACEABILITY_MATURITY",
                "Normative or proposed requirement cannot use a source-reference-only trace.",
                id=requirement_id,
            )

        maturity = _text(
            requirement.get("traceability_maturity"),
            "FAIL_TRACEABILITY_MATURITY",
            "requirement maturity",
        )
        acceptance_maturity = acceptance.get("traceability_maturity")
        test_status = test.get("status")
        evidence_status = evidence.get("status")
        if acceptance_maturity not in MATURITY_LEVELS:
            _fail("FAIL_TRACEABILITY_MATURITY", "Acceptance maturity is invalid.")
        if test_status not in TEST_LEVELS or evidence_status not in EVIDENCE_LEVELS:
            _fail("FAIL_TRACEABILITY_MATURITY", "Test or evidence status is invalid.")
        claim = MATURITY_LEVELS[maturity]
        actual = min(
            MATURITY_LEVELS[str(acceptance_maturity)],
            TEST_LEVELS[str(test_status)],
            EVIDENCE_LEVELS[str(evidence_status)],
        )
        acceptance_level = MATURITY_LEVELS[str(acceptance_maturity)]
        test_level = TEST_LEVELS[str(test_status)]
        evidence_level = EVIDENCE_LEVELS[str(evidence_status)]
        chain_overclaims = acceptance_level > test_level or test_level > evidence_level
        if claim > actual or chain_overclaims:
            _fail(
                "FAIL_TRACEABILITY_MATURITY",
                "Traceability maturity is higher than the actual test/evidence chain.",
                id=requirement_id,
            )
        if evidence_status == "CAPTURED":
            digest = evidence.get("sha256")
            execution_id = evidence.get("execution_id")
            if not isinstance(digest, str) or not _SHA256_PATTERN.fullmatch(digest):
                _fail("FAIL_TRACEABILITY_MATURITY", "Captured evidence lacks an exact digest.")
            _text(execution_id, "FAIL_TRACEABILITY_MATURITY", "evidence execution ID")
        acceptance_ids.add(acceptance_id)
        test_ids.add(test_id)
        evidence_ids.add(evidence_id)
        by_requirement[requirement_id] = trace
    if set(by_requirement) != set(requirements):
        _fail(
            "FAIL_ORPHAN_REQUIREMENT",
            "Every requirement must have one complete trace chain.",
            missing=sorted(set(requirements) - set(by_requirement)),
        )


def _validate_human_review(
    registry: Mapping[str, Any], requirements: Mapping[str, Mapping[str, Any]]
) -> tuple[list[str], dict[str, int], dict[str, int]]:
    review = _mapping(registry.get("human_review"), "FAIL_REVIEW_SELECTION", "human review")
    selection = _sequence(
        review.get("selection"), "FAIL_REVIEW_SELECTION", "human review selection"
    )
    approvals_raw = _sequence(
        review.get("approvals", []), "FAIL_HUMAN_APPROVAL_STALE", "approvals"
    )
    if approvals_raw:
        _fail(
            "FAIL_HUMAN_APPROVAL_STALE",
            (
                "Final Human Acceptance must be recorded out-of-band after "
                "exact-head CI, not manufactured in source."
            ),
        )
    if (
        review.get("selection_count") != 36
        or review.get("unresolved_selection_count") != 0
        or review.get("final_human_acceptance") != "PENDING"
    ):
        _fail(
            "FAIL_REVIEW_SELECTION",
            "Human-review aggregate state is stale or overclaims final acceptance.",
        )

    expected = {
        requirement_id
        for requirement_id, requirement in requirements.items()
        if requirement.get("disposition") != "REUSE"
    }
    selected: set[str] = set()
    facet_counts = {facet: 0 for facet in sorted(REVIEW_FACETS)}
    decision_counts = {"REFINE": 0, "EXCLUDE": 0, "DEFER": 0}
    policy_groups = {
        range(1, 9): "HR001_008_DEDUP_REFINE",
        range(9, 21): "HR009_020_SCOPED_REFINE",
        range(21, 23): "HR021_022_OPERATIONS_REFINE",
        range(23, 32): "HR023_031_REFERENCE_EXCLUDE",
        range(32, 33): "HR032_STOREFRONT_INVARIANT_REFINE",
        range(33, 35): "HR033_034_FUTURE_ARCHITECTURE_DEFER",
        range(35, 37): "HR035_036_LOGICAL_OWNERSHIP_REFINE",
    }
    for index, raw_item in enumerate(selection, start=1):
        item = _mapping(raw_item, "FAIL_REVIEW_SELECTION", "human review item")
        review_id = _text(item.get("id"), "FAIL_REVIEW_SELECTION", "review ID")
        if review_id != f"V3-R1-HR-{index:03d}":
            _fail("FAIL_REVIEW_SELECTION", "Human-review selection identity is stale.")
        requirement_id = _text(
            item.get("requirement_id"), "FAIL_REVIEW_SELECTION", "review requirement"
        )
        if requirement_id not in expected or requirement_id in selected:
            _fail("FAIL_REVIEW_SELECTION", "Human-review selection is stale or duplicated.")
        reasons = _sequence(item.get("facets"), "FAIL_REVIEW_SELECTION", "review facets")
        requirement_facets = requirements[requirement_id].get("review_facets", [])
        if set(reasons) != set(requirement_facets):
            _fail("FAIL_REVIEW_SELECTION", "Human-review facets do not match requirement data.")
        for facet in reasons:
            if facet in facet_counts:
                facet_counts[str(facet)] += 1
        requirement = requirements[requirement_id]
        decision = item.get("decision")
        expected_state = {
            "REFINE": "SOURCE_APPROVED",
            "EXCLUDE": "EXCLUDED",
            "DEFER": "DEFERRED",
        }.get(str(decision))
        expected_group = next(
            name for indexes, name in policy_groups.items() if index in indexes
        )
        resolution_summary = _text(
            item.get("resolution_summary"),
            "FAIL_REVIEW_SELECTION",
            "resolution summary",
        )
        if (
            item.get("status") != "RESOLVED_PENDING_FINAL_ACCEPTANCE"
            or expected_state is None
            or requirement.get("state") != expected_state
            or requirement.get("resolution_decision") != decision
            or requirement.get("selection_id") != review_id
            or item.get("policy_group") != expected_group
            or item.get("requirement_sha256")
            != _canonical_requirement_digest(requirement)
            or len(resolution_summary) < 16
            or _PLACEHOLDER_PATTERN.search(resolution_summary)
        ):
            _fail(
                "FAIL_REVIEW_SELECTION",
                "Human-review resolution does not bind the exact requirement and policy group.",
                review_id=review_id,
            )
        decision_counts[str(decision)] += 1
        selected.add(requirement_id)
    if selected != expected or len(selected) != 36:
        _fail(
            "FAIL_REVIEW_SELECTION",
            "All and only the 36 non-REUSE requirements require Human review.",
            missing=sorted(expected - selected),
            extra=sorted(selected - expected),
        )
    if decision_counts != {"REFINE": 25, "EXCLUDE": 9, "DEFER": 2}:
        _fail(
            "FAIL_REVIEW_SELECTION",
            "Human-review decision counts differ from the authorized resolution policy.",
            observed=decision_counts,
        )
    matrix_digest = review.get("decision_matrix_sha256")
    if not isinstance(matrix_digest, str) or matrix_digest != _canonical_digest(selection):
        _fail(
            "FAIL_REVIEW_DECISION_DIGEST",
            "Human-review decision matrix digest is missing or stale.",
        )
    return sorted(selected), facet_counts, decision_counts


def _validate_s01_acceptance(registry: Mapping[str, Any]) -> None:
    value = _mapping(
        registry.get("s01_slice_acceptance"),
        "FAIL_S01_ACCEPTANCE",
        "S01 slice acceptance",
    )
    requirement_ids = _sequence(
        value.get("direct_requirement_ids"),
        "FAIL_S01_ACCEPTANCE",
        "S01 direct requirements",
    )
    cases = _sequence(
        value.get("acceptance_cases"), "FAIL_S01_ACCEPTANCE", "S01 acceptance cases"
    )
    if value.get("direct_requirement_count") != 0 or requirement_ids:
        _fail(
            "FAIL_S01_ACCEPTANCE",
            "S01 must transparently retain zero directly allocated requirements.",
        )
    if not cases:
        _fail("FAIL_S01_ACCEPTANCE", "S01 requires executable slice-level acceptance metadata.")
    for raw_case in cases:
        case = _mapping(raw_case, "FAIL_S01_ACCEPTANCE", "S01 acceptance case")
        _text(case.get("id"), "FAIL_S01_ACCEPTANCE", "S01 acceptance case ID")
        _text(case.get("test"), "FAIL_S01_ACCEPTANCE", "S01 acceptance test")
        if case.get("status") not in {"IMPLEMENTED", "PLANNED"}:
            _fail("FAIL_S01_ACCEPTANCE", "S01 acceptance status is invalid.")
        if case.get("evidence_status") not in {"NOT_CAPTURED", "CAPTURED"}:
            _fail("FAIL_S01_ACCEPTANCE", "S01 evidence status is invalid.")


def validate_traceability_baseline(
    repository_root: Path,
    registry_path: Path | None = None,
    *,
    facet: str | None = None,
) -> dict[str, Any]:
    """Validate the complete S01 baseline and return a queryable summary."""

    path = registry_path or repository_root / DEFAULT_REGISTRY_PATH
    if not path.is_absolute():
        path = repository_root / path
    registry = _load_registry(path)
    if registry.get("schema_version") != 2:
        _fail("FAIL_REGISTRY_FORMAT", "Unsupported traceability registry schema.")
    authority = _validate_authority(registry)
    corpus, source_group_statuses = _validate_corpus(repository_root, registry)
    source_decisions = _validate_source_decisions(registry, corpus)
    valid_slices = _validate_slices(registry)
    requirements = _validate_requirements(registry, valid_slices)
    anchors = _validate_anchors(repository_root, registry, corpus, requirements)
    _validate_traces(registry, requirements)
    review_ids, facet_counts, decision_counts = _validate_human_review(
        registry, requirements
    )
    _validate_s01_acceptance(registry)
    if facet is not None and facet not in REVIEW_FACETS:
        _fail("FAIL_QUERY_FACET", "Requested traceability facet is invalid.", facet=facet)
    query_ids = (
        sorted(
            requirement_id
            for requirement_id, requirement in requirements.items()
            if facet in requirement.get("review_facets", [])
        )
        if facet is not None
        else []
    )
    return {
        "baseline_id": registry.get("baseline_id"),
        "repository": authority["repository"],
        "stacked_base_branch": authority["stacked_base_branch"],
        "seed_commit": authority["seed_commit"],
        "seed_tree": authority["seed_tree"],
        "source_decision": authority["source_decision"],
        "corpus_file_count": len(corpus),
        "brd_file_count": sum(path.startswith("docs/BRD/") for path in corpus),
        "uxf_file_count": sum(path.startswith("docs/UXF/") for path in corpus),
        "requirement_count": len(requirements),
        "requirement_state_counts": {
            state: sum(
                requirement.get("state") == state for requirement in requirements.values()
            )
            for state in sorted(REQUIREMENT_STATES)
        },
        "exact_anchor_count": len(anchors),
        "human_review_requirement_count": len(review_ids),
        "human_review_resolved_count": len(review_ids),
        "human_review_pending_count": 0,
        "human_review_decision_counts": decision_counts,
        "human_review_decision_matrix_sha256": registry.get("human_review", {}).get(
            "decision_matrix_sha256"
        ),
        "source_group_decision_count": len(source_decisions),
        "source_group_pending_count": len(
            source_group_statuses.get("HUMAN_DECISION_REQUIRED", [])
        ),
        "source_decision_matrix_sha256": registry.get(
            "source_decision_matrix_sha256"
        ),
        "final_human_acceptance": registry.get("human_review", {}).get(
            "final_human_acceptance"
        ),
        "facet_counts": facet_counts,
        "query_facet": facet,
        "query_requirement_ids": query_ids,
    }
