from __future__ import annotations

import copy
import shutil
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest
import yaml

from ysf.secure_factory.models import FactoryFailure
from ysf.traceability.service import run_traceability_validation
from ysf.traceability.validator import (
    DEFAULT_REGISTRY_PATH,
    validate_traceability_baseline,
)

Mutation = Callable[[dict[str, Any], Path], None]


def _repository_root() -> Path:
    return Path(__file__).resolve().parents[4]


def _baseline() -> dict[str, Any]:
    value = yaml.safe_load((_repository_root() / DEFAULT_REGISTRY_PATH).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _workspace(tmp_path: Path, value: dict[str, Any]) -> tuple[Path, Path]:
    root = tmp_path / "repository"
    shutil.copytree(_repository_root() / "docs/BRD", root / "docs/BRD")
    shutil.copytree(_repository_root() / "docs/UXF", root / "docs/UXF")
    registry = root / DEFAULT_REGISTRY_PATH
    registry.parent.mkdir(parents=True)
    registry.write_text(
        yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8",
    )
    return root, registry


def _assert_failure(tmp_path: Path, code: str, mutation: Mutation) -> None:
    value = copy.deepcopy(_baseline())
    root, registry = _workspace(tmp_path, value)
    mutation(value, root)
    registry.write_text(
        yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8",
    )
    with pytest.raises(FactoryFailure) as captured:
        validate_traceability_baseline(root, registry)
    assert captured.value.code == code


def test_repository_baseline_passes_and_is_queryable() -> None:
    root = _repository_root()
    summary = validate_traceability_baseline(root)
    assert summary["repository"] == "nvkhoabk/ysim"
    assert summary["stacked_base_branch"] == "feature/v3-r1-g00-s00-secure-factory"
    assert summary["seed_commit"] == "a8cfc5d93c8176fc3a727257be609f3af82f38de"
    assert summary["seed_tree"] == "1953815ee35edc5f6fc487784e4f2bac9191ec1f"
    assert summary["source_decision"] == "SOURCE_INPUT_DECISIONS_RESOLVED"
    assert summary["corpus_file_count"] == 31
    assert summary["brd_file_count"] == 24
    assert summary["uxf_file_count"] == 7
    assert summary["requirement_count"] == 86
    assert summary["exact_anchor_count"] == 86
    assert summary["human_review_requirement_count"] == 36
    assert summary["human_review_resolved_count"] == 36
    assert summary["human_review_pending_count"] == 0
    assert summary["human_review_decision_counts"] == {
        "REFINE": 25,
        "EXCLUDE": 9,
        "DEFER": 2,
    }
    assert summary["source_group_decision_count"] == 11
    assert summary["source_group_pending_count"] == 0
    assert summary["requirement_state_counts"] == {
        "DEFERRED": 2,
        "EXCLUDED": 9,
        "PROPOSED": 50,
        "SOURCE_APPROVED": 25,
    }
    assert summary["final_human_acceptance"] == "PENDING"
    assert summary["facet_counts"] == {
        "CONFLICT": 6,
        "DECISION_DEPENDENT": 5,
        "EXCLUSION": 5,
        "MULTI_SOURCE": 0,
        "REFINEMENT": 20,
    }
    conflict = validate_traceability_baseline(root, facet="CONFLICT")
    assert len(conflict["query_requirement_ids"]) == 6


def test_requirement_traces_do_not_claim_future_execution() -> None:
    value = _baseline()
    assert {item["state"] for item in value["requirements"]} == {
        "SOURCE_APPROVED",
        "PROPOSED",
        "EXCLUDED",
        "DEFERRED",
    }
    assert {item["traceability_maturity"] for item in value["requirements"]} == {
        "PLANNED"
    }
    states = {item["id"]: item["state"] for item in value["requirements"]}
    normative = [
        item
        for item in value["traces"]
        if states[item["requirement_id"]] in {"SOURCE_APPROVED", "PROPOSED"}
    ]
    references = [
        item
        for item in value["traces"]
        if states[item["requirement_id"]] in {"EXCLUDED", "DEFERRED"}
    ]
    assert {item["test"]["status"] for item in normative} == {"PLANNED"}
    assert {item["evidence"]["status"] for item in normative} == {"PLANNED"}
    assert {item["trace_status"] for item in references} == {"SOURCE_REFERENCE_ONLY"}
    assert {item["test"]["status"] for item in references} == {"NOT_APPLICABLE"}
    assert {item["evidence"]["status"] for item in references} == {"NOT_APPLICABLE"}
    assert value["s01_slice_acceptance"]["direct_requirement_count"] == 0
    assert value["s01_slice_acceptance"]["direct_requirement_ids"] == []


def test_all_source_decisions_and_review_selections_are_resolved_without_overclaim() -> None:
    value = _baseline()
    assert len(value["source_decisions"]) == 11
    assert {item["decision"] for item in value["source_decisions"]} == {
        "ACCEPT_AS_SOURCE_INPUT"
    }
    assert {item["normative_requirement_authority"] for item in value["source_decisions"]} == {
        "NONE"
    }
    assert len(value["source_decision_matrix_sha256"]) == 64
    review = value["human_review"]
    assert review["selection_count"] == 36
    assert review["unresolved_selection_count"] == 0
    assert review["final_human_acceptance"] == "PENDING"
    assert review["approvals"] == []
    assert len(review["decision_matrix_sha256"]) == 64
    assert {item["status"] for item in review["selection"]} == {
        "RESOLVED_PENDING_FINAL_ACCEPTANCE"
    }


def _corpus_count(_: dict[str, Any], root: Path) -> None:
    (root / "docs/UXF/INDEX.md").unlink()


def _extra_corpus_file(_: dict[str, Any], root: Path) -> None:
    (root / "docs/UXF/synthetic-extra.md").write_text(
        "Synthetic extra corpus file.\n", encoding="utf-8"
    )


def _requirement_count(value: dict[str, Any], _: Path) -> None:
    value["requirements"].pop()


def _corpus_blob(_: dict[str, Any], root: Path) -> None:
    path = root / "docs/BRD/BRD-WS-01.md"
    path.write_text(path.read_text(encoding="utf-8") + "\nSynthetic mutation.\n", encoding="utf-8")


def _missing_anchor(value: dict[str, Any], _: Path) -> None:
    removed = value["source_anchors"].pop()
    value["exact_anchor_count"] -= 1
    requirement = next(
        item for item in value["requirements"] if item["id"] == removed["requirement_id"]
    )
    requirement["source_anchor_ids"].remove(removed["id"])


def _stale_anchor(value: dict[str, Any], _: Path) -> None:
    value["source_anchors"][0]["locator"]["start_line"] += 1
    value["source_anchors"][0]["locator"]["end_line"] += 1


def _statement_digest(value: dict[str, Any], _: Path) -> None:
    value["source_anchors"][0]["statement_sha256"] = "0" * 64


def _stale_heading(value: dict[str, Any], _: Path) -> None:
    value["source_anchors"][0]["heading"] = "Stale synthetic heading"


def _orphan_requirement(value: dict[str, Any], _: Path) -> None:
    value["source_anchors"][0]["requirement_id"] = "V3-R1-UNKNOWN-001"


def _orphan_acceptance(value: dict[str, Any], _: Path) -> None:
    value["traces"][0]["acceptance_case"]["requirement_id"] = "V3-R1-UNKNOWN-001"


def _orphan_test(value: dict[str, Any], _: Path) -> None:
    value["traces"][0]["test"]["acceptance_case_id"] = "V3-R1-AC-UNKNOWN"


def _orphan_evidence(value: dict[str, Any], _: Path) -> None:
    value["traces"][0]["evidence"]["test_id"] = "V3-R1-TEST-UNKNOWN"


def _gate_slice(value: dict[str, Any], _: Path) -> None:
    value["requirements"][0]["gate_slice"] = "V3-R1-G99-S99"


def _maturity(value: dict[str, Any], _: Path) -> None:
    requirement = value["requirements"][0]
    requirement["traceability_maturity"] = "EXECUTED"
    for anchor in value["source_anchors"]:
        if anchor["requirement_id"] == requirement["id"]:
            anchor["traceability_maturity"] = "EXECUTED"


def _future_test_overclaim(value: dict[str, Any], _: Path) -> None:
    value["traces"][0]["test"]["status"] = "EXECUTED"


def _selection_resolution_missing(value: dict[str, Any], _: Path) -> None:
    value["human_review"]["selection"][0]["status"] = "PENDING"


def _selection_digest_stale(value: dict[str, Any], _: Path) -> None:
    value["human_review"]["selection"][0]["requirement_sha256"] = "0" * 64


def _requirement_state(value: dict[str, Any], _: Path) -> None:
    value["requirements"][0]["state"] = "ACCEPTED"


def _forbidden_source_decision(value: dict[str, Any], _: Path) -> None:
    value["authority"]["source_decision"] = "PENDING_HUMAN_REVIEW"


def _stale_seed_commit(value: dict[str, Any], _: Path) -> None:
    value["authority"]["seed_commit"] = "0" * 40


def _stale_seed_tree(value: dict[str, Any], _: Path) -> None:
    value["authority"]["seed_tree"] = "0" * 40


def _legacy_maturity_transfer(value: dict[str, Any], _: Path) -> None:
    value["authority"]["legacy_maturity_transfer"] = "ALLOWED"


def _source_group(value: dict[str, Any], _: Path) -> None:
    value["corpus"]["files"][0]["source_group_status"] = "UNASSIGNED"


def _duplicate_anchor(value: dict[str, Any], _: Path) -> None:
    duplicate = copy.deepcopy(value["source_anchors"][0])
    duplicate["id"] = "V3-R1-SA-087"
    value["source_anchors"].append(duplicate)
    value["exact_anchor_count"] = 87
    value["requirements"][0]["source_anchor_ids"].append(duplicate["id"])


def _misbound_anchor(value: dict[str, Any], _: Path) -> None:
    duplicate = copy.deepcopy(value["source_anchors"][0])
    duplicate["id"] = "V3-R1-SA-087"
    requirement = value["requirements"][1]
    duplicate["requirement_id"] = requirement["id"]
    for field in ("gate_slice", "disposition", "traceability_maturity"):
        duplicate[field] = requirement[field]
    value["source_anchors"].append(duplicate)
    value["exact_anchor_count"] = 87
    requirement["source_anchor_ids"].append(duplicate["id"])


def _fake_multi_source(value: dict[str, Any], _: Path) -> None:
    item = value["human_review"]["selection"][0]
    requirement = next(
        entry for entry in value["requirements"] if entry["id"] == item["requirement_id"]
    )
    requirement["review_facets"].append("MULTI_SOURCE")
    item["facets"].append("MULTI_SOURCE")


def _source_decision_missing(value: dict[str, Any], _: Path) -> None:
    value["source_decisions"].pop()


def _source_decision_digest(value: dict[str, Any], _: Path) -> None:
    value["source_decision_matrix_sha256"] = "0" * 64


def _declared_anchor_count(value: dict[str, Any], _: Path) -> None:
    value["exact_anchor_count"] = 94


def _requirement_semantics(value: dict[str, Any], _: Path) -> None:
    requirement = next(
        entry for entry in value["requirements"] if entry["state"] == "SOURCE_APPROVED"
    )
    requirement["release_requirement"]["statement"] = "TBD"


def _approved_requirement(value: dict[str, Any]) -> dict[str, Any]:
    return next(
        entry for entry in value["requirements"] if entry["state"] == "SOURCE_APPROVED"
    )


def _release_missing_field(value: dict[str, Any], _: Path) -> None:
    _approved_requirement(value)["release_requirement"].pop("out_of_scope")


def _release_short_owner(value: dict[str, Any], _: Path) -> None:
    _approved_requirement(value)["release_requirement"]["owner"] = "Ops"


def _release_empty_boundary(value: dict[str, Any], _: Path) -> None:
    _approved_requirement(value)["release_requirement"]["out_of_scope"] = []


def _release_one_criterion(value: dict[str, Any], _: Path) -> None:
    requirement = _approved_requirement(value)["release_requirement"]
    requirement["acceptance_criteria"] = requirement["acceptance_criteria"][:1]


def _release_criterion_missing_field(value: dict[str, Any], _: Path) -> None:
    criterion = _approved_requirement(value)["release_requirement"]["acceptance_criteria"][0]
    criterion.pop("verification")


def _release_short_condition(value: dict[str, Any], _: Path) -> None:
    criterion = _approved_requirement(value)["release_requirement"]["acceptance_criteria"][0]
    criterion["condition"] = "Too short"


def _source_approved_binding_invalid(value: dict[str, Any], _: Path) -> None:
    _approved_requirement(value)["resolution_decision"] = "EXCLUDE"


def _proposed_blocker_short(value: dict[str, Any], _: Path) -> None:
    requirement = next(
        entry for entry in value["requirements"] if entry["state"] == "PROPOSED"
    )
    requirement["promotion_blocker"] = "Too short"


def _excluded_binding_invalid(value: dict[str, Any], _: Path) -> None:
    requirement = next(
        entry for entry in value["requirements"] if entry["state"] == "EXCLUDED"
    )
    requirement["source_provenance_retained"] = False


def _anchor_count_type_invalid(value: dict[str, Any], _: Path) -> None:
    value["exact_anchor_count"] = "86"


def _anchor_id_stale(value: dict[str, Any], _: Path) -> None:
    value["source_anchors"][0]["id"] = "V3-R1-SA-999"


def _final_acceptance_overclaim(value: dict[str, Any], _: Path) -> None:
    value["human_review"]["final_human_acceptance"] = "ACCEPT"


def _s01_reallocation(value: dict[str, Any], _: Path) -> None:
    value["s01_slice_acceptance"]["direct_requirement_count"] = 1
    value["s01_slice_acceptance"]["direct_requirement_ids"] = ["V3-R1-GOV-001"]


def _set_path(value: dict[str, Any], path: tuple[str | int, ...], replacement: Any) -> None:
    target: Any = value
    for part in path[:-1]:
        target = target[part]
    target[path[-1]] = replacement


@pytest.mark.parametrize(
    ("code", "path", "replacement"),
    [
        ("FAIL_REGISTRY_FORMAT", ("schema_version",), 1),
        ("FAIL_SOURCE_IDENTITY", ("authority",), []),
        ("FAIL_CORPUS_COUNT", ("corpus", "files"), "invalid"),
        ("FAIL_CORPUS_COUNT", ("corpus", "expected_brd_count"), 23),
        ("FAIL_CORPUS_FORMAT", ("corpus", "files", 0, "source_set"), "OTHER"),
        (
            "FAIL_CORPUS_FORMAT",
            ("corpus", "files", 0, "path"),
            "docs/BRD/../BRD-BO-INDEX.md",
        ),
        ("FAIL_CORPUS_BLOB", ("corpus", "files", 0, "git_blob_sha"), "invalid"),
        ("FAIL_GATE_SLICE_ID", ("roadmap", "valid_gate_slices"), ["invalid"]),
        ("FAIL_DISPOSITION", ("requirements", 0, "disposition"), "INVALID"),
        (
            "FAIL_TRACEABILITY_MATURITY",
            ("requirements", 0, "traceability_maturity"),
            "INVALID",
        ),
        ("FAIL_REVIEW_SELECTION", ("requirements", 0, "review_facets"), ["INVALID"]),
        ("FAIL_SOURCE_ANCHOR_COUNT", ("exact_anchor_count",), 0),
        (
            "FAIL_SOURCE_ANCHOR_STALE",
            ("source_anchors", 0, "source_path"),
            "docs/BRD/unknown.md",
        ),
        ("FAIL_SOURCE_ANCHOR_STALE", ("source_anchors", 0, "source_set"), "UXF"),
        ("FAIL_SOURCE_ANCHOR_STALE", ("source_anchors", 0, "git_blob_sha"), "0" * 40),
        ("FAIL_SOURCE_ANCHOR_STALE", ("source_anchors", 0, "locator", "start_line"), 0),
        ("FAIL_SOURCE_ANCHOR_STALE", ("source_anchors", 0, "locator", "end_line"), 999999),
        ("FAIL_STATEMENT_DIGEST", ("source_anchors", 0, "statement_sha256"), "invalid"),
        (
            "FAIL_SOURCE_ANCHOR_STALE",
            ("source_anchors", 0, "traceability_maturity"),
            "IMPLEMENTED",
        ),
        ("FAIL_SOURCE_ANCHOR_MISSING", ("requirements", 0, "source_anchor_ids"), []),
        (
            "FAIL_ORPHAN_TEST",
            ("traces", 0, "acceptance_case", "test_id"),
            "V3-R1-TEST-UNKNOWN",
        ),
        (
            "FAIL_ORPHAN_ACCEPTANCE_CASE",
            ("requirements", 0, "acceptance_case_id"),
            "V3-R1-AC-UNKNOWN",
        ),
        (
            "FAIL_TRACEABILITY_MATURITY",
            ("traces", 0, "acceptance_case", "traceability_maturity"),
            "INVALID",
        ),
        ("FAIL_TRACEABILITY_MATURITY", ("traces", 0, "test", "status"), "INVALID"),
        ("FAIL_REVIEW_SELECTION", ("human_review", "selection", 0, "facets"), []),
        ("FAIL_REVIEW_SELECTION", ("human_review", "selection", 0, "status"), "INVALID"),
        (
            "FAIL_SOURCE_DECISION",
            ("source_decisions", 0, "normative_requirement_authority"),
            "ALL_CONTENT_APPROVED",
        ),
        ("FAIL_S01_ACCEPTANCE", ("s01_slice_acceptance", "acceptance_cases"), []),
        (
            "FAIL_S01_ACCEPTANCE",
            ("s01_slice_acceptance", "acceptance_cases", 0, "status"),
            "INVALID",
        ),
        (
            "FAIL_S01_ACCEPTANCE",
            ("s01_slice_acceptance", "acceptance_cases", 0, "evidence_status"),
            "INVALID",
        ),
    ],
)
def test_additional_fail_closed_schema_matrix(
    tmp_path: Path,
    code: str,
    path: tuple[str | int, ...],
    replacement: Any,
) -> None:
    _assert_failure(tmp_path, code, lambda value, _: _set_path(value, path, replacement))


@pytest.mark.parametrize(
    ("code", "mutation"),
    [
        ("FAIL_SOURCE_ANCHOR_DUPLICATE", _duplicate_anchor),
        ("FAIL_SOURCE_ANCHOR_SEMANTIC_BINDING", _misbound_anchor),
        ("FAIL_SOURCE_ANCHOR_COUNT", _declared_anchor_count),
        ("FAIL_FAKE_MULTI_SOURCE", _fake_multi_source),
    ],
)
def test_canonical_anchor_integrity_fails_closed(
    tmp_path: Path, code: str, mutation: Mutation
) -> None:
    _assert_failure(tmp_path, code, mutation)


@pytest.mark.parametrize(
    ("code", "mutation"),
    [
        ("FAIL_REQUIREMENT_SEMANTICS", _release_missing_field),
        ("FAIL_REQUIREMENT_SEMANTICS", _release_short_owner),
        ("FAIL_REQUIREMENT_SEMANTICS", _release_empty_boundary),
        ("FAIL_REQUIREMENT_SEMANTICS", _release_one_criterion),
        ("FAIL_REQUIREMENT_SEMANTICS", _release_criterion_missing_field),
        ("FAIL_REQUIREMENT_SEMANTICS", _release_short_condition),
        ("FAIL_REQUIREMENT_STATE", _source_approved_binding_invalid),
        ("FAIL_REQUIREMENT_STATE", _proposed_blocker_short),
        ("FAIL_REQUIREMENT_STATE", _excluded_binding_invalid),
        ("FAIL_SOURCE_ANCHOR_COUNT", _anchor_count_type_invalid),
        ("FAIL_SOURCE_ANCHOR_STALE", _anchor_id_stale),
    ],
)
def test_resolved_semantics_fail_closed(
    tmp_path: Path, code: str, mutation: Mutation
) -> None:
    _assert_failure(tmp_path, code, mutation)


def test_registry_io_query_and_service_paths(tmp_path: Path) -> None:
    with pytest.raises(FactoryFailure) as captured:
        validate_traceability_baseline(tmp_path, tmp_path / "missing.yaml")
    assert captured.value.code == "FAIL_REGISTRY_READ"

    invalid = tmp_path / "invalid.yaml"
    invalid.write_text("[invalid", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        validate_traceability_baseline(tmp_path, invalid)
    assert captured.value.code == "FAIL_REGISTRY_FORMAT"

    with pytest.raises(FactoryFailure) as captured:
        validate_traceability_baseline(_repository_root(), facet="INVALID")
    assert captured.value.code == "FAIL_QUERY_FACET"

    result = run_traceability_validation(_repository_root(), facet="CONFLICT")
    assert result.status == "PASS"
    assert result.data["query_facet"] == "CONFLICT"


@pytest.mark.parametrize(
    ("code", "mutation"),
    [
        ("FAIL_CORPUS_COUNT", _corpus_count),
        ("FAIL_CORPUS_COUNT", _extra_corpus_file),
        ("FAIL_REQUIREMENT_COUNT", _requirement_count),
        ("FAIL_CORPUS_BLOB", _corpus_blob),
        ("FAIL_SOURCE_ANCHOR_COUNT", _missing_anchor),
        ("FAIL_SOURCE_ANCHOR_DUPLICATE", _duplicate_anchor),
        ("FAIL_SOURCE_ANCHOR_SEMANTIC_BINDING", _misbound_anchor),
        ("FAIL_FAKE_MULTI_SOURCE", _fake_multi_source),
        ("FAIL_SOURCE_ANCHOR_STALE", _stale_anchor),
        ("FAIL_STATEMENT_DIGEST", _statement_digest),
        ("FAIL_SOURCE_ANCHOR_STALE", _stale_heading),
        ("FAIL_ORPHAN_REQUIREMENT", _orphan_requirement),
        ("FAIL_ORPHAN_ACCEPTANCE_CASE", _orphan_acceptance),
        ("FAIL_ORPHAN_TEST", _orphan_test),
        ("FAIL_ORPHAN_EVIDENCE", _orphan_evidence),
        ("FAIL_GATE_SLICE_ID", _gate_slice),
        ("FAIL_TRACEABILITY_MATURITY", _maturity),
        ("FAIL_TRACEABILITY_MATURITY", _future_test_overclaim),
        ("FAIL_REVIEW_SELECTION", _selection_resolution_missing),
        ("FAIL_REVIEW_SELECTION", _selection_digest_stale),
        ("FAIL_REQUIREMENT_STATE", _requirement_state),
        ("FAIL_REQUIREMENT_SEMANTICS", _requirement_semantics),
        ("FAIL_REVIEW_SELECTION", _final_acceptance_overclaim),
        ("FAIL_SOURCE_DECISION", _source_decision_missing),
        ("FAIL_SOURCE_DECISION_DIGEST", _source_decision_digest),
        ("FAIL_SOURCE_IDENTITY", _forbidden_source_decision),
        ("FAIL_SOURCE_IDENTITY", _stale_seed_commit),
        ("FAIL_SOURCE_IDENTITY", _stale_seed_tree),
        ("FAIL_SOURCE_IDENTITY", _legacy_maturity_transfer),
        ("FAIL_SOURCE_GROUP", _source_group),
        ("FAIL_S01_ACCEPTANCE", _s01_reallocation),
    ],
)
def test_fail_closed_matrix(
    tmp_path: Path,
    code: str,
    mutation: Mutation,
) -> None:
    _assert_failure(tmp_path, code, mutation)
