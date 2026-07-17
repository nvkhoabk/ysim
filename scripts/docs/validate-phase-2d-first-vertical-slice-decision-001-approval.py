#!/usr/bin/env python3
"""Validate detached approval for Phase 2D first-slice decision 001."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2d"
CANDIDATE = "625dc7a2164de9f6dd179677ebdf98c85c9e4b31"
PARENT = "9a4e163734f57d0be871f4cd9392a2ad21e3055e"
CANDIDATE_TREE = "9994c05f051d5be6afb67a665cb3a02e454b2669"
DECISION_ID = "V23-P2D-FIRST-SLICE-DECISION-001"
SLICE_ID = "V23-P2D-VS001-PUBLIC_PRODUCT_CATALOG_BROWSE_DETAIL"
SCOPE = "FIRST_VERTICAL_SLICE_SELECTION_AND_PRODUCT_IMPLEMENTATION_COMMISSIONING_BOUNDARY"
APPROVAL_FILES = sorted([
    "docs/baselines/v2.3/phase-2d/PHASE_2D_FIRST_VERTICAL_SLICE_DECISION_001_APPROVAL.md",
    "scripts/docs/validate-phase-2d-first-vertical-slice-decision-001-approval.py",
])
CANDIDATE_FILES = sorted([
    "docs/baselines/v2.3/phase-2d/FIRST_VERTICAL_SLICE_DECISION_001.md",
    "docs/baselines/v2.3/phase-2d/first-vertical-slice-decision-001-manifest.json",
    "docs/baselines/v2.3/phase-2d/first-vertical-slice-decision-001.json",
    "scripts/docs/validate-phase-2d-first-vertical-slice-decision-001.py",
])


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"INVALID_APPROVED_PHASE_2D_FIRST_VERTICAL_SLICE_DECISION_001: {message}")


def main() -> None:
    head = git("rev-parse", "HEAD")
    require(git("rev-parse", f"{CANDIDATE}^") == PARENT, "candidate parent")
    require(git("rev-parse", f"{CANDIDATE}^{{tree}}") == CANDIDATE_TREE, "candidate tree")
    require(git("rev-parse", "HEAD^") == CANDIDATE, "accepted direct parent")
    require(sorted(git("diff", "--name-only", f"{CANDIDATE}..{head}").splitlines()) == APPROVAL_FILES, "approval diff")
    require(sorted(git("diff", "--name-only", f"{PARENT}..{CANDIDATE}").splitlines()) == CANDIDATE_FILES, "candidate inventory")

    manifest = json.loads(blob(CANDIDATE, "docs/baselines/v2.3/phase-2d/first-vertical-slice-decision-001-manifest.json"))
    payload = json.loads(blob(CANDIDATE, "docs/baselines/v2.3/phase-2d/first-vertical-slice-decision-001.json"))
    require(payload["status"] == "CANDIDATE" and payload["approval_status"] == "PENDING_HUMAN_APPROVAL", "immutable candidate")
    require(payload["decision_id"] == DECISION_ID, "decision ID")
    require(payload["selected_slice"] == SLICE_ID, "selected slice")
    require(payload["approval_scope"] == SCOPE, "scope")
    require(payload["requirement_boundary"]["readiness_counts"] == {"acceptance_ready": 9, "pending_elaboration": 16, "total": 25}, "boundary counts")
    for path, expected_hash in manifest["signed_file_sha256"].items():
        require(hashlib.sha256(blob(CANDIDATE, path)).hexdigest() == expected_hash, f"candidate hash {path}")
        require(blob(CANDIDATE, path) == blob(head, path), f"candidate changed {path}")

    approval = (BASE / "PHASE_2D_FIRST_VERTICAL_SLICE_DECISION_001_APPROVAL.md").read_text(encoding="utf-8")
    for value in ("APPROVED", DECISION_ID, SLICE_ID, SCOPE, "Khoa, Nguyen", CANDIDATE, PARENT, CANDIDATE_TREE):
        require(value in approval, f"approval field {value}")
    for requirement_id in payload["requirement_boundary"]["acceptance_ready"] + payload["requirement_boundary"]["pending_vertical_slice_acceptance_elaboration"]:
        require(approval.count(f"`{requirement_id}`") == 1, f"approval requirement {requirement_id}")
    require("Slice-specific acceptance elaboration is not approved." in approval, "acceptance non-claim")
    require("Commissioning implementation and VS001 implementation are not approved." in approval, "implementation non-claim")
    print("VALID_APPROVED_PHASE_2D_FIRST_VERTICAL_SLICE_DECISION_001")


if __name__ == "__main__":
    main()
