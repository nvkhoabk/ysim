#!/usr/bin/env python3
"""Validate detached approval for progressive acceptance decision 001."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2"
CANDIDATE = "50d1b0e6761abc5cdd8108b9bba1c696608e8408"
PARENT = "374a808d3749dfda97a9d9534e4d798cbd6ae05a"
CANDIDATE_TREE = "3f1b41a99ba58d1e97437fe8d46f069d352bde3d"
DECISION_ID = "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001"
SCOPE = "PROGRESSIVE_ACCEPTANCE_ELABORATION_AND_VERTICAL_SLICE_ENTRY_POLICY"
OPTION = "PROGRESSIVE_VERTICAL_SLICE_ACCEPTANCE"
APPROVAL_FILES = sorted([
    "docs/baselines/v2.3/phase-2/PHASE_2C_PROGRESSIVE_ACCEPTANCE_DECISION_001_APPROVAL.md",
    "scripts/docs/validate-phase-2c-progressive-acceptance-decision-001-approval.py",
])
CANDIDATE_FILES = sorted([
    "docs/baselines/v2.3/phase-2/PROGRESSIVE_ACCEPTANCE_DECISION_001.md",
    "docs/baselines/v2.3/phase-2/progressive-acceptance-decision-001-manifest.json",
    "docs/baselines/v2.3/phase-2/progressive-acceptance-decision-001.json",
    "scripts/docs/validate-progressive-acceptance-decision-001.py",
])


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"INVALID_APPROVED_PHASE_2C_PROGRESSIVE_ACCEPTANCE_DECISION_001: {message}")


def blob(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def main() -> None:
    head = git("rev-parse", "HEAD")
    require(git("rev-parse", f"{CANDIDATE}^") == PARENT, "candidate parent")
    require(git("rev-parse", f"{CANDIDATE}^{{tree}}") == CANDIDATE_TREE, "candidate tree")
    require(git("rev-parse", "HEAD^") == CANDIDATE, "accepted direct parent")
    require(sorted(git("diff", "--name-only", f"{CANDIDATE}..{head}").splitlines()) == APPROVAL_FILES, "approval diff")
    require(sorted(git("diff", "--name-only", f"{PARENT}..{CANDIDATE}").splitlines()) == CANDIDATE_FILES, "candidate inventory")

    manifest = json.loads(blob(CANDIDATE, "docs/baselines/v2.3/phase-2/progressive-acceptance-decision-001-manifest.json"))
    decision = json.loads(blob(CANDIDATE, "docs/baselines/v2.3/phase-2/progressive-acceptance-decision-001.json"))
    require(decision["status"] == "CANDIDATE" and decision["approval_status"] == "PENDING_HUMAN_APPROVAL", "immutable candidate state")
    require(decision["decision_id"] == DECISION_ID, "decision ID")
    require(decision["decision"]["selected_option"] == OPTION, "selected option")
    require(decision["approval_scope"] == SCOPE, "candidate scope")
    for path, expected in manifest["signed_file_sha256"].items():
        require(hashlib.sha256(blob(CANDIDATE, path)).hexdigest() == expected, f"candidate blob {path}")
        require(blob(CANDIDATE, path) == blob(head, path), f"candidate changed {path}")

    approval = (BASE / "PHASE_2C_PROGRESSIVE_ACCEPTANCE_DECISION_001_APPROVAL.md").read_text(encoding="utf-8")
    for value in (DECISION_ID, OPTION, SCOPE, "Khoa, Nguyen", CANDIDATE, PARENT, CANDIDATE_TREE,
                  "SYSTEMIC_GENERIC_ACCEPTANCE_AND_EXPECTED_DERIVED_OBSERVATION"):
        require(value in approval, f"approval field {value}")
    require(approval.count("Authorized approver: Khoa, Nguyen") == 1, "approver")
    require(approval.count("Signature: Khoa, Nguyen") == 1, "signature")
    require("1,093" in approval and "59" in approval, "populations")

    backup_ref = "refs/ysim-backups/v2.3/phase-2c-document-baseline-c6-r1-rejected"
    try:
        require(git("rev-parse", backup_ref) == "8ec2a5381054fc6dddad2e1c2ad15bd4e53a0a28", "backup ref")
        require(git("rev-parse", f"{backup_ref}^{{tree}}") == "699a7de703fc1c0009cca0d851c67766a1d7d333", "backup tree")
    except subprocess.CalledProcessError:
        pass
    print("VALID_APPROVED_PHASE_2C_PROGRESSIVE_ACCEPTANCE_DECISION_001")


if __name__ == "__main__":
    main()
