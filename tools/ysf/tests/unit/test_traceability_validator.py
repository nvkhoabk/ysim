from __future__ import annotations

import copy
import hashlib
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
    assert summary["source_decision"] == "PENDING_HUMAN_REVIEW"
    assert summary["corpus_file_count"] == 31
    assert summary["brd_file_count"] == 24
    assert summary["uxf_file_count"] == 7
    assert summary["requirement_count"] == 86
    assert summary["exact_anchor_count"] == 94
    assert summary["human_review_requirement_count"] == 36
    assert summary["source_group_human_decision_count"] == 11
    assert summary["facet_counts"] == {
        "CONFLICT": 6,
        "DECISION_DEPENDENT": 5,
        "EXCLUSION": 5,
        "MULTI_SOURCE": 8,
        "REFINEMENT": 20,
    }
    conflict = validate_traceability_baseline(root, facet="CONFLICT")
    assert len(conflict["query_requirement_ids"]) == 6


def test_requirement_traces_do_not_claim_future_execution() -> None:
    value = _baseline()
    assert {item["state"] for item in value["requirements"]} == {"PROPOSED"}
    assert {item["traceability_maturity"] for item in value["requirements"]} == {
        "PLANNED"
    }
    assert {item["test"]["status"] for item in value["traces"]} == {"PLANNED"}
    assert {item["evidence"]["status"] for item in value["traces"]} == {"PLANNED"}
    assert value["s01_slice_acceptance"]["direct_requirement_count"] == 0
    assert value["s01_slice_acceptance"]["direct_requirement_ids"] == []


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


def _approval_missing(value: dict[str, Any], _: Path) -> None:
    value["human_review"]["selection"][0]["status"] = "RESOLVED"


def _approval_stale(value: dict[str, Any], _: Path) -> None:
    item = value["human_review"]["selection"][0]
    item["status"] = "RESOLVED"
    value["human_review"]["approvals"].append(
        {
            "review_id": item["id"],
            "requirement_id": item["requirement_id"],
            "requirement_sha256": hashlib.sha256(b"stale").hexdigest(),
            "decision": "ACCEPT",
        }
    )


def _requirement_state(value: dict[str, Any], _: Path) -> None:
    value["requirements"][0]["state"] = "ACCEPTED"


def _forbidden_source_decision(value: dict[str, Any], _: Path) -> None:
    value["authority"]["source_decision"] = "SOURCE_APPROVED"


def _stale_seed_commit(value: dict[str, Any], _: Path) -> None:
    value["authority"]["seed_commit"] = "0" * 40


def _stale_seed_tree(value: dict[str, Any], _: Path) -> None:
    value["authority"]["seed_tree"] = "0" * 40


def _legacy_maturity_transfer(value: dict[str, Any], _: Path) -> None:
    value["authority"]["legacy_maturity_transfer"] = "ALLOWED"


def _source_group(value: dict[str, Any], _: Path) -> None:
    value["corpus"]["files"][0]["source_group_status"] = "UNASSIGNED"


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
        ("FAIL_REGISTRY_FORMAT", ("schema_version",), 2),
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
        ("FAIL_SOURCE_ANCHOR_MISSING", ("exact_anchor_count",), 0),
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
        ("FAIL_SOURCE_ANCHOR_MISSING", _missing_anchor),
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
        ("FAIL_HUMAN_APPROVAL_MISSING", _approval_missing),
        ("FAIL_HUMAN_APPROVAL_STALE", _approval_stale),
        ("FAIL_REQUIREMENT_STATE", _requirement_state),
        ("FAIL_SOURCE_APPROVED_FORBIDDEN", _forbidden_source_decision),
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
