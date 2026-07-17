#!/usr/bin/env python3
"""Validate the immutable progressive-acceptance decision candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2"
DECISION_PATH = BASE / "progressive-acceptance-decision-001.json"
DOC_PATH = BASE / "PROGRESSIVE_ACCEPTANCE_DECISION_001.md"
MANIFEST_PATH = BASE / "progressive-acceptance-decision-001-manifest.json"

DECISION_ID = "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001"
SCOPE = "PROGRESSIVE_ACCEPTANCE_ELABORATION_AND_VERTICAL_SLICE_ENTRY_POLICY"
OPTION = "PROGRESSIVE_VERTICAL_SLICE_ACCEPTANCE"
REASON = "SYSTEMIC_GENERIC_ACCEPTANCE_AND_EXPECTED_DERIVED_OBSERVATION"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"INVALID_PROGRESSIVE_ACCEPTANCE_DECISION_001: {message}")


def main() -> None:
    decision = json.loads(DECISION_PATH.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    doc = DOC_PATH.read_text(encoding="utf-8")

    require(decision["decision_id"] == DECISION_ID, "decision_id")
    require(decision["candidate_id"] == DECISION_ID, "candidate_id")
    require(decision["status"] == "CANDIDATE", "candidate status")
    require(decision["approval_status"] == "PENDING_HUMAN_APPROVAL", "embedded approval")
    require(decision["authorized_approver"] == "Khoa, Nguyen", "approver")
    require(decision["approval_scope"] == SCOPE, "scope")
    require(decision["approval_basis"] == "EXACT_HUMAN_AUTHORIZATION_TEXT_AND_SCOPE", "basis")
    require(decision["decision"]["selected_option"] == OPTION, "selected option")
    populations = decision["decision"]["acceptance_populations"]
    require(populations == {
        "acceptance_ready": 59,
        "active_total": 1152,
        "pending_vertical_slice_acceptance_elaboration": 1093,
    }, "population")
    require(sum((populations["acceptance_ready"], populations["pending_vertical_slice_acceptance_elaboration"])) == 1152, "population sum")
    require(decision["decision"]["rejected_candidate"] == {
        "candidate_id": "V23-P2C-DOCUMENT-BASELINE-C6-R1",
        "reason": REASON,
    }, "rejected candidate")
    require(len(decision["decision"]["canonical_terms"]) == 10, "canonical term count")
    require("options" not in decision and "exceptions" not in decision, "unauthorized alternatives")
    require(len(decision["non_claims"]) == 7, "non-claims")
    for value in (DECISION_ID, OPTION, SCOPE, REASON, "Khoa, Nguyen"):
        require(value in doc, f"markdown mirror missing {value}")

    inventory = manifest["candidate_inventory"]
    expected_inventory = sorted([
        "docs/baselines/v2.3/phase-2/PROGRESSIVE_ACCEPTANCE_DECISION_001.md",
        "docs/baselines/v2.3/phase-2/progressive-acceptance-decision-001-manifest.json",
        "docs/baselines/v2.3/phase-2/progressive-acceptance-decision-001.json",
        "scripts/docs/validate-progressive-acceptance-decision-001.py",
    ])
    require(inventory == expected_inventory, "candidate inventory")
    for relative_path, expected_hash in manifest["signed_file_sha256"].items():
        require(relative_path != "docs/baselines/v2.3/phase-2/progressive-acceptance-decision-001-manifest.json", "self-referential hash")
        require(sha256(ROOT / relative_path) == expected_hash, f"hash {relative_path}")
    require(manifest["decision_id"] == DECISION_ID, "manifest decision")
    require(manifest["status"] == "CANDIDATE", "manifest status")
    require(manifest["approval_status"] == "PENDING_HUMAN_APPROVAL", "manifest approval")
    require(manifest["approval_scope"] == SCOPE, "manifest scope")
    print("VALID_PHASE_2C_PROGRESSIVE_ACCEPTANCE_DECISION_001_CANDIDATE")


if __name__ == "__main__":
    main()
