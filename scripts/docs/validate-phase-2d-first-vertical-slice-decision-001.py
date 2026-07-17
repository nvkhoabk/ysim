#!/usr/bin/env python3
"""Validate the immutable first vertical-slice selection candidate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2d"
PAYLOAD = BASE / "first-vertical-slice-decision-001.json"
DOCUMENT = BASE / "FIRST_VERTICAL_SLICE_DECISION_001.md"
MANIFEST = BASE / "first-vertical-slice-decision-001-manifest.json"
DECISION_ID = "V23-P2D-FIRST-SLICE-DECISION-001"
SLICE_ID = "V23-P2D-VS001-PUBLIC_PRODUCT_CATALOG_BROWSE_DETAIL"
SCOPE = "FIRST_VERTICAL_SLICE_SELECTION_AND_PRODUCT_IMPLEMENTATION_COMMISSIONING_BOUNDARY"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"INVALID_PHASE_2D_FIRST_VERTICAL_SLICE_DECISION_001: {message}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    payload = json.loads(PAYLOAD.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    document = DOCUMENT.read_text(encoding="utf-8")
    require(payload["decision_id"] == DECISION_ID, "decision ID")
    require(payload["selected_slice"] == SLICE_ID, "selected slice")
    require(payload["status"] == "CANDIDATE", "candidate status")
    require(payload["approval_status"] == "PENDING_HUMAN_APPROVAL", "embedded approval")
    require(payload["approval_scope"] == SCOPE, "approval scope")
    require(payload["approval_basis"] == "EXACT_HUMAN_AUTHORIZATION_TEXT_AND_SCOPE", "approval basis")
    require(payload["authorized_approver"] == "Khoa, Nguyen", "approver")
    boundary = payload["requirement_boundary"]
    require(len(boundary["acceptance_ready"]) == 9, "ready population")
    require(len(boundary["pending_vertical_slice_acceptance_elaboration"]) == 16, "pending population")
    require(len(set(boundary["acceptance_ready"] + boundary["pending_vertical_slice_acceptance_elaboration"])) == 25, "unique boundary")
    require(boundary["readiness_counts"] == {"acceptance_ready": 9, "pending_elaboration": 16, "total": 25}, "counts")
    require(len(payload["commissioning_boundary"]["allowed"]) == 13, "commissioning allowlist")
    require(len(payload["commissioning_boundary"]["forbidden"]) == 13, "commissioning denylist")
    require(payload["commissioning_boundary"]["separate_gate_required"] is True, "separate gate")
    for value in (DECISION_ID, SLICE_ID, SCOPE, "Khoa, Nguyen"):
        require(value in document, f"markdown mirror {value}")

    inventory = sorted(manifest["candidate_inventory"])
    expected = sorted([
        "docs/baselines/v2.3/phase-2d/FIRST_VERTICAL_SLICE_DECISION_001.md",
        "docs/baselines/v2.3/phase-2d/first-vertical-slice-decision-001-manifest.json",
        "docs/baselines/v2.3/phase-2d/first-vertical-slice-decision-001.json",
        "scripts/docs/validate-phase-2d-first-vertical-slice-decision-001.py",
    ])
    require(inventory == expected, "candidate inventory")
    for relative, expected_hash in manifest["signed_file_sha256"].items():
        require(not relative.endswith("manifest.json"), "self-referential hash")
        require(sha256(ROOT / relative) == expected_hash, f"signed hash {relative}")
    require(manifest["decision_id"] == DECISION_ID, "manifest decision")
    require(manifest["status"] == "CANDIDATE", "manifest status")
    require(manifest["approval_status"] == "PENDING_HUMAN_APPROVAL", "manifest approval")
    print("VALID_PHASE_2D_FIRST_VERTICAL_SLICE_DECISION_001_CANDIDATE")


if __name__ == "__main__":
    main()
