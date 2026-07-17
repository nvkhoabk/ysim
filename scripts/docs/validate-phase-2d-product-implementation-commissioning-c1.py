#!/usr/bin/env python3
"""Validate the Phase 2D product implementation commissioning contract."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2d"
CANDIDATE = "V23-P2D-PRODUCT-IMPLEMENTATION-COMMISSIONING-C1"
GOVERNING_DECISION = "V23-P2D-FIRST-SLICE-DECISION-001"


def load(name: str) -> dict:
    return json.loads((BASE / name).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"INVALID_PHASE_2D_PRODUCT_IMPLEMENTATION_COMMISSIONING_C1: {message}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    contract = load("product-implementation-commissioning-c1-execution-contract.json")
    policy = load("product-implementation-commissioning-c1-path-policy.json")
    matrix = load("product-implementation-commissioning-c1-validation-matrix.json")
    evidence = load("product-implementation-commissioning-c1-evidence-plan.json")
    technology = load("product-implementation-commissioning-c1-technology-decisions.json")
    manifest = load("product-implementation-commissioning-c1-manifest.json")

    for payload in (contract, policy, matrix, evidence, technology):
        require(payload["candidate_id"] == CANDIDATE, "candidate identity")
        require(payload["status"] == "CANDIDATE", "candidate state")
    require(contract["approval_status"] == "PENDING_HUMAN_APPROVAL", "embedded approval")
    require(contract["governing_decision"] == GOVERNING_DECISION, "governing decision")
    require(contract["implementation_authorized"] is False, "implementation flag")
    require(contract["correction_pass_limit_after_approval"] == 2, "correction limit")
    require(len(contract["validation_commands"]) == 9, "validation commands")
    require(len(contract["acceptance_criteria"]) == 15, "acceptance criteria")
    require(len(contract["proposed_directory_tree"]) == 16, "proposed tree")
    require(matrix["required_gate_count"] == 9 and len(matrix["gates"]) == 9, "validation matrix")
    require(matrix["implementation_executed"] is False, "matrix execution claim")
    require(evidence["required_evidence_count"] == 9 and len(evidence["evidence_requirements"]) == 9, "evidence plan")
    require(evidence["implementation_evidence_present"] is False, "evidence claim")

    decisions = technology["decisions"]
    require(len(decisions) == 7 and technology["unresolved_decision_count"] == 7, "technology decisions")
    require([item["decision_id"] for item in decisions] == [f"TECH-COM-{number:03d}" for number in range(1, 8)], "technology decision IDs")
    require(all(item["selected_option"] is None and item["status"] == "PENDING_HUMAN_APPROVAL" for item in decisions), "technology decisions must remain pending")
    require(technology["fixed_stack"]["runtime_category"] == "NODE_EXACT_VERSION_PENDING", "Node authority boundary")
    require(technology["fixed_stack"]["package_manager"] == "PNPM_EXACT_VERSION_PENDING", "pnpm authority boundary")

    allowed = policy["allowed_future_implementation_paths"]
    protected = policy["protected_paths"]
    forbidden = policy["forbidden_content_classes"]
    require(len(allowed) == len(set(allowed)) == 16, "allowed paths")
    require(len(protected) == len(set(protected)) == 12, "protected paths")
    require(len(forbidden) == len(set(forbidden)) == 13, "forbidden content")
    require("docs/BRD/**" in protected and "docs/UXF/**" in protected, "source protection")
    require("PRODUCT_LIST_OR_PRODUCT_DETAIL_API" in forbidden, "business API prohibition")
    require("PRODUCT_OR_CATALOG_UI" in forbidden, "business UI prohibition")

    expected_inventory = sorted([
        "docs/baselines/v2.3/phase-2d/PRODUCT_IMPLEMENTATION_COMMISSIONING_C1.md",
        "docs/baselines/v2.3/phase-2d/PRODUCT_IMPLEMENTATION_COMMISSIONING_C1_HUMAN_APPROVAL_PACK.md",
        "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-evidence-plan.json",
        "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-execution-contract.json",
        "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-manifest.json",
        "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-path-policy.json",
        "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-technology-decisions.json",
        "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-validation-matrix.json",
        "scripts/docs/build-phase-2d-product-implementation-commissioning-c1.py",
        "scripts/docs/tests/test-phase-2d-product-implementation-commissioning-c1.py",
        "scripts/docs/validate-phase-2d-product-implementation-commissioning-c1.py",
    ])
    require(sorted(manifest["candidate_inventory"]) == expected_inventory, "manifest inventory")
    require(manifest["candidate_id"] == CANDIDATE, "manifest identity")
    require(manifest["status"] == "CANDIDATE" and manifest["approval_status"] == "PENDING_HUMAN_APPROVAL", "manifest state")
    require(manifest["governing_decision"] == GOVERNING_DECISION, "manifest governing decision")
    for relative, expected in manifest["signed_file_sha256"].items():
        require(not relative.endswith("manifest.json"), "self-reference")
        require(sha256(ROOT / relative) == expected, f"signed hash {relative}")

    existing_forbidden_roots = [name for name in ("apps", "packages", "database", "infrastructure") if (ROOT / name).exists()]
    require(existing_forbidden_roots == [], f"implementation roots unexpectedly materialized: {existing_forbidden_roots}")
    print("VALID_PHASE_2D_PRODUCT_IMPLEMENTATION_COMMISSIONING_C1_CANDIDATE")


if __name__ == "__main__":
    main()
