#!/usr/bin/env python3
"""Validate detached approval for Operator Binding Type Model C1.

Signed candidate identity is always read from committed Git objects. The
validator supports the two-file staged approval state on the candidate commit
and a clean accepted commit whose direct parent is the candidate.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE_ID = "V23-P2C-OPERATOR-BINDING-TYPE-MODEL-C1"
CANDIDATE = "214bc3798a8ea586cec76a2584eb0eb11a2c5cf6"
PARENT = "77d10a8c3ccb2e7795724fd1c82cdbea36c54e2e"
TREE = "277821e564a0862e6512bc40eb5b9e9395d2fe55"
STAGED_AGGREGATE = "ddd98927167aa5b5443e2ded2d6fd6c1947e397caa1862b8a844d2a375c84809"
GENERATED_AGGREGATE = "bf63a716f99899f16403a52b9331ec2b0bcc4ba2ae8075e3da9c87caf3dafedf"
APPROVAL_MD = "docs/baselines/v2.3/phase-2/OPERATOR_BINDING_TYPE_MODEL_C1_APPROVAL.md"
APPROVAL_VALIDATOR = "scripts/docs/validate-operator-binding-type-model-c1-approval.py"
APPROVAL_PATHS = [APPROVAL_MD, APPROVAL_VALIDATOR]
MANIFEST = "docs/baselines/v2.3/phase-2/operator-binding-type-model-manifest.json"
DECISIONS = "docs/baselines/v2.3/phase-2/operator-binding-source-clarification-decisions.json"
DISPOSITIONS = "docs/baselines/v2.3/phase-2/operator-binding-type-dispositions.json"
SELECTIONS = {
    "BD-05-009": "P2C-OBT-C1-BD-05-009-OPT-1",
    "BRD-WS-02-R003": "P2C-OBT-C1-BRD-WS-02-R003-OPT-1",
    "BRD-WS-07-R005": "P2C-OBT-C1-BRD-WS-07-R005-OPT-1",
    "EP-08-006": "P2C-OBT-C1-EP-08-006-OPT-1",
    "EP-17-002": "P2C-OBT-C1-EP-17-002-OPT-1",
    "UXF-405": "P2C-OBT-C1-UXF-405-OPT-1",
}
BACKUP_TREES = {
    "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c3-r1-rejected^2^{tree}": "92fb9de65f2fd6b5be888a271ab4ab245798eb9d",
    "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c3-blocked^{tree}": "19bf019617e5f6672a45b85247bdea9d9103b73f",
    "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c2-blocked^{tree}": "6973e1f4b09b59198d3eb2103dbc9e381125a480",
    "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c1-blocked^{tree}": "3241762b05565c813a590df4032c2587d9c14f3e",
    "refs/ysim-backups/v2.3/phase-2c-document-baseline-c4-blocked^2^{tree}": "ef678c7da248f3595ac01cd585355469b12d76b0",
    "refs/ysim-backups/v2.3/phase-2c-semantic-oracle-model-c1-rejected^{tree}": "e7fe153e8402ca9d7a3ec7832a9d1df9f438a3bf",
}


def git(*args: str, binary: bool = False):
    result = subprocess.check_output(["git", *args], cwd=ROOT, text=not binary)
    return result if binary else result.strip()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def object_bytes(commit: str, path: str) -> bytes:
    return git("show", f"{commit}:{path}", binary=True)


def candidate_paths() -> list[str]:
    return git("diff", "--name-only", f"{PARENT}..{CANDIDATE}").splitlines()


def candidate_aggregate() -> str:
    digest = hashlib.sha256()
    paths = candidate_paths()
    require(len(paths) == 12, "candidate path count differs from 12")
    for path in sorted(paths):
        digest.update(path.encode() + b"\0" + object_bytes(CANDIDATE, path) + b"\0")
    return digest.hexdigest()


def approval_text(mode: str) -> str:
    payload = git("show", f":{APPROVAL_MD}", binary=True) if mode == "STAGED" else object_bytes("HEAD", APPROVAL_MD)
    return payload.decode("utf-8")


def main() -> int:
    head = git("rev-parse", "HEAD")
    require(git("cat-file", "-t", CANDIDATE) == "commit", "candidate commit is absent")
    require(git("rev-parse", f"{CANDIDATE}^") == PARENT, "candidate parent mismatch")
    require(git("rev-parse", f"{CANDIDATE}^{{tree}}") == TREE, "candidate tree mismatch")
    require(candidate_aggregate() == STAGED_AGGREGATE, "signed candidate aggregate mismatch")

    if head == CANDIDATE:
        mode = "STAGED"
        require(git("diff", "--cached", "--name-only").splitlines() == APPROVAL_PATHS, "staged approval inventory mismatch")
        require(not git("diff", "--name-only"), "tracked unstaged changes exist")
        require(not git("ls-files", "--others", "--exclude-standard"), "untracked files exist")
    else:
        mode = "COMMITTED"
        require(git("rev-parse", "HEAD^") == CANDIDATE, "accepted commit direct parent mismatch")
        require(git("diff", "--name-only", f"{CANDIDATE}..HEAD").splitlines() == APPROVAL_PATHS, "accepted diff is not exactly the approval layer")
        require(not git("status", "--porcelain"), "accepted checkout is not clean")

    manifest = json.loads(object_bytes(CANDIDATE, MANIFEST))
    require((manifest["candidate_id"], manifest["status"], manifest["approval_status"]) == (CANDIDATE_ID, "CANDIDATE", "PENDING_HUMAN_APPROVAL"), "embedded candidate state changed")
    require(manifest["generated_payload_aggregate_sha256"] == GENERATED_AGGREGATE, "generated payload aggregate mismatch")
    for path, expected in manifest["file_sha256"].items():
        require(hashlib.sha256(object_bytes(CANDIDATE, path)).hexdigest() == expected, f"immutable payload hash mismatch: {path}")

    decisions = json.loads(object_bytes(CANDIDATE, DECISIONS))
    require(decisions["decision_count"] == 6 and decisions["selected_count"] == 0, "candidate decision accounting changed")
    decision_by_id = {item["requirement_id"]: item for item in decisions["decisions"]}
    require(set(decision_by_id) == set(SELECTIONS), "candidate decision inventory changed")
    for requirement_id, option_id in SELECTIONS.items():
        decision = decision_by_id[requirement_id]
        require(decision["selected_option"] is None and decision["approval_status"] == "PENDING_HUMAN_APPROVAL", f"candidate selection mutated: {requirement_id}")
        require(option_id in {item["option_id"] for item in decision["options"]}, f"approved option absent: {requirement_id}")

    dispositions = json.loads(object_bytes(CANDIDATE, DISPOSITIONS))
    require(dispositions["record_count"] == 59, "disposition count changed")
    require(dispositions["counts"] == {"COMPOUND_AST_REQUIRED": 6, "CORRECTABLE_WITH_APPROVED_TYPE_MODEL": 35, "OPERATOR_REMAP_REQUIRED": 12, "SOURCE_CLARIFICATION_REQUIRED": 6}, "disposition totals changed")

    approval = approval_text(mode)
    required_tokens = [
        CANDIDATE_ID, CANDIDATE, PARENT, TREE, STAGED_AGGREGATE, GENERATED_AGGREGATE,
        "Decision: `APPROVED`", "Authorized Approver: `Khoa, Nguyen`", "Signature: `Khoa, Nguyen`",
        "Approval date: `2026-07-16`", "Timezone: `Asia/Ho_Chi_Minh`",
        "Runtime mutation and runtime acceptance: `N/A`", *SELECTIONS.values(),
        "Approval is handled by the Shared Approval Engine.",
        "Provider-specific schemas must be mapped into the canonical YSim capability taxonomy.",
        "Duplicate detection does not automatically merge identities.",
        "Absence of a universal limit does not mean unlimited retries.",
        "Every active Platform component must belong to the authoritative inventory.",
        "Platform/Security → Jurisdiction/Market → Organization → Storefront",
        "NOT_APPROVAL_OF_REJECTED_C3_R1_ASTS_OR_FIXTURES",
        "NOT_REGENERATED_CUSTOM_AST_APPROVAL", "NOT_REGENERATED_SEMANTIC_FIXTURE_APPROVAL",
        "NOT_RUNTIME_ADAPTER_OR_RUNTIME_EVIDENCE_APPROVAL", "NOT_BRD_UXF_EDIT_APPROVAL",
        "NOT_FINAL_PHASE_2C_DOCUMENT_BASELINE_APPROVAL", "NOT_FINAL_V2_3_BRD_UXF_FREEZE",
        "NOT_YADF_IMPLEMENTATION_AUTHORIZATION", "NOT_PRODUCTION_IMPLEMENTATION_AUTHORIZATION",
    ]
    for token in required_tokens:
        require(token in approval, f"approval record missing: {token}")

    require(not git("diff", "--name-only", f"{PARENT}..{CANDIDATE}", "--", "docs/BRD", "docs/UXF"), "candidate changed BRD/UXF")
    if mode == "COMMITTED":
        require(not git("diff", "--name-only", f"{CANDIDATE}..HEAD", "--", "docs/BRD", "docs/UXF"), "approval changed BRD/UXF")
    for spec, expected in BACKUP_TREES.items():
        require(git("rev-parse", spec) == expected, f"backup preservation changed: {spec}")

    print("VALID_APPROVED_PHASE_2C_OPERATOR_BINDING_TYPE_MODEL_C1")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, subprocess.CalledProcessError, KeyError, json.JSONDecodeError) as exc:
        print(f"FAIL — {exc}")
        raise SystemExit(1)
