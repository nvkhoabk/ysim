#!/usr/bin/env python3
"""Validate detached approval for V23-P2C-SEMANTIC-ORACLE-MODEL-C2.

The validator supports both the two-file staged approval state on the candidate
commit and a clean accepted commit whose direct parent is the candidate. Signed
candidate payload identity is always read from committed Git objects.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = "4e39433306c463ecef803182f87b19518f926772"
BASE = "a90476e8b053bf86c11638477736c8c418a33025"
TREE = "79bcb74b56e1bc8c7054d412c77c1b36eb26401a"
C1_TREE = "e7fe153e8402ca9d7a3ec7832a9d1df9f438a3bf"
C1_REF = "refs/ysim-backups/v2.3/phase-2c-semantic-oracle-model-c1-rejected"
C4_STASH = "90bc3cac386163430d78bf7c6a346e189cd55459"
C4_TREE = "ef678c7da248f3595ac01cd585355469b12d76b0"
C4_REF = "refs/ysim-backups/v2.3/phase-2c-document-baseline-c4-blocked"
APPROVAL_MD = "docs/baselines/v2.3/phase-2/PHASE_2_SEMANTIC_ORACLE_MODEL_C2_APPROVAL.md"
APPROVAL_VALIDATOR = "scripts/docs/validate-semantic-oracle-model-c2-approval.py"
APPROVAL_PATHS = [APPROVAL_MD, APPROVAL_VALIDATOR]
EXPECTED = {
    "generated": "29f70c58884e5dd10b11f2f3da8798b007fcccff07891bacb1454149058af711",
    "staged": "2ff424ea8bb42baeb2a5c4a2eecf6580bfe68a901ca8b87e23fab400bcf53c86",
    "manifest": "a4669729b5784937c42f7a575b87cd1f2344d01505d805b4841bfbc75943583d",
    "engine": "4b6c023ba661f5e1cbaa351a9aee54e19ebc71d5a5863c1b4e5d1f57545e97a2",
    "execution": "66b66ecc5161f8de829d061a5f9d1214cfa56b511eca2e26894268b158b75f69",
    "decisions": "e03a18451342a15bf808751fcca999d7f628d5459c24e4cd597c46413162f600",
}
SIGNED_FILES = {
    "manifest": "docs/baselines/v2.3/phase-2/semantic-oracle-model-manifest.json",
    "engine": "scripts/docs/semantic-oracle-engine.py",
    "execution": "docs/baselines/v2.3/phase-2/semantic-oracle-execution-results.json",
    "decisions": "docs/baselines/v2.3/phase-2/semantic-oracle-human-mapping-decisions.json",
}


def git(*args: str, binary: bool = False):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=not binary).strip() if not binary else subprocess.check_output(["git", *args], cwd=ROOT)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def object_bytes(commit: str, path: str) -> bytes:
    return git("show", f"{commit}:{path}", binary=True)


def aggregate_candidate() -> str:
    paths = git("diff-tree", "--no-commit-id", "--name-only", "-r", CANDIDATE).splitlines()
    require(len(paths) == 23, "candidate path count differs from 23")
    digest = hashlib.sha256()
    for path in sorted(paths):
        payload = object_bytes(CANDIDATE, path)
        digest.update(path.encode() + b"\0" + payload + b"\0")
    return digest.hexdigest()


def approval_bytes(mode: str) -> bytes:
    return git("show", f":{APPROVAL_MD}", binary=True) if mode == "STAGED" else object_bytes("HEAD", APPROVAL_MD)


def main() -> int:
    head = git("rev-parse", "HEAD")
    require(git("cat-file", "-t", CANDIDATE) == "commit", "candidate commit does not exist")
    require(git("rev-parse", f"{CANDIDATE}^") == BASE, "candidate parent mismatch")
    require(git("rev-parse", f"{CANDIDATE}^{{tree}}") == TREE, "candidate tree mismatch")
    for ancestor in ("0df2d424e00f9cd27b8dcb6645eef827ce97b60e", "a989367a6f69f1a03a8269562ce43bda3968b71a", BASE):
        subprocess.run(["git", "merge-base", "--is-ancestor", ancestor, CANDIDATE], cwd=ROOT, check=True)

    if head == CANDIDATE:
        mode = "STAGED"
        require(git("diff", "--cached", "--name-only").splitlines() == APPROVAL_PATHS, "staged approval inventory mismatch")
        require(not git("diff", "--name-only"), "tracked unstaged changes exist")
        require(not git("ls-files", "--others", "--exclude-standard"), "untracked files exist")
    else:
        mode = "COMMITTED"
        require(git("rev-parse", "HEAD^") == CANDIDATE, "accepted commit direct parent is not candidate")
        require(git("diff", "--name-only", f"{CANDIDATE}..HEAD").splitlines() == APPROVAL_PATHS, "candidate-to-accepted diff is not exactly approval layer")
        require(not git("status", "--porcelain"), "accepted checkout is not clean")

    require(aggregate_candidate() == EXPECTED["staged"], "signed candidate aggregate mismatch")
    for label, path in SIGNED_FILES.items():
        require(hashlib.sha256(object_bytes(CANDIDATE, path)).hexdigest() == EXPECTED[label], f"signed {label} hash mismatch")
    manifest = json.loads(object_bytes(CANDIDATE, SIGNED_FILES["manifest"]))
    require(manifest["generated_payload_aggregate_sha256"] == EXPECTED["generated"], "generated aggregate mismatch")
    require((manifest["candidate_id"], manifest["status"], manifest["approval_status"]) == ("V23-P2C-SEMANTIC-ORACLE-MODEL-C2", "CANDIDATE", "PENDING_HUMAN_APPROVAL"), "embedded candidate identity/state changed")
    require(manifest["counts"]["operator_conformance_passed"] == 40 and manifest["counts"]["adversarial_passed"] == 10, "approved model evidence counts changed")
    require(manifest["counts"]["human_mapping_decisions"] == 27 and manifest["counts"]["dispositions"]["CUSTOM_AST_REQUIRED"] == 59 and manifest["counts"]["reusable_high_risk_subset_of_custom"] == 48, "pending populations changed")

    approval = approval_bytes(mode).decode()
    required_text = [
        "V23-P2C-SEMANTIC-ORACLE-MODEL-C2", CANDIDATE, BASE, TREE, "Decision: `APPROVED`",
        "EXECUTABLE_SEMANTIC_ORACLE_ENGINE_OPERATOR_CATALOG_AND_REFERENCE_EVALUATION_MODEL",
        "Authorized Approver: `Khoa, Nguyen`", "Signature: `Khoa, Nguyen`",
        "Approval date: `2026-07-15`", "Timezone: `Asia/Ho_Chi_Minh`", "Runtime mutation score: `N/A`",
        *EXPECTED.values(),
        "NOT_APPROVAL_OF_27_PENDING_HUMAN_OPERATOR_MAPPING_DECISIONS",
        "NOT_APPROVAL_OF_59_CUSTOM_AST_CONTRACTS",
        "NOT_APPROVAL_OF_48_REUSABLE_HIGH_RISK_COMPOSITIONS",
        "NOT_REGENERATED_BRD_UXF_ACCEPTANCE_BLOCK_APPROVAL",
        "NOT_FINAL_V2_3_DOCUMENT_BASELINE_APPROVAL",
        "NOT_RUNTIME_MUTATION_OR_RUNTIME_ACCEPTANCE_EVIDENCE",
        "NOT_YADF_IMPLEMENTATION_AUTHORIZATION",
        "NOT_PRODUCTION_IMPLEMENTATION_AUTHORIZATION",
    ]
    for token in required_text:
        require(token in approval, f"approval record missing token: {token}")

    require(not git("diff", "--name-only", f"{BASE}..{CANDIDATE}", "--", "docs/BRD", "docs/UXF"), "candidate changed BRD/UXF")
    if mode == "COMMITTED":
        require(not git("diff", "--name-only", f"{CANDIDATE}..HEAD", "--", "docs/BRD", "docs/UXF"), "approval changed BRD/UXF")
    require(git("rev-parse", f"{C1_REF}^{{tree}}") == C1_TREE, "C1 preservation changed")
    require(git("rev-parse", C4_REF) == C4_STASH, "C4 backup ref changed")
    require(git("rev-parse", f"{C4_REF}^2^{{tree}}") == C4_TREE, "C4 index tree changed")
    print("VALID_APPROVED_PHASE_2C_SEMANTIC_ORACLE_MODEL_C2")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, subprocess.CalledProcessError) as exc:
        print(f"FAIL — {exc}")
        raise SystemExit(1)
