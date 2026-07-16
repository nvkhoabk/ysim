#!/usr/bin/env python3
"""Validate the detached human approval for Semantic Completion C4-R3.

The signed candidate is always read from committed Git objects. The validator
supports either the two-file staged approval state on the candidate commit or
a clean accepted commit whose direct parent is the candidate.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE_ID = "V23-P2C-SEMANTIC-COMPLETION-C4-R3"
CANDIDATE = "c9100b0a3e5f78c8c61cec46ac14528373a0aff2"
PARENT = "522442635eb0df24dd5de0d42dad84656a5920e0"
TREE = "717ffc49fdb0825bfcd57001e5bd2310ed69336c"
GIT_CONTENT_AGGREGATE = "c2bf15e033a48d8c43f1695fbd28211f809bd204f6db15502fd0eb67e1efc624"
GENERATED_AGGREGATE = "93b673e5ebb318d401361e6b5f12b294932278aeb6805cb4b0e1ad2be55fcabb"
MANIFEST_SHA256 = "2b4be49f5064abb292aa3e793c6f44bdb3e75e881b11e57b05cfdeb663735762"
SCOPE = "SEMANTIC_COMPLETION_DECISION_CONTRACTS_SOURCE_CLARIFICATIONS_AND_EXPLICIT_BUSINESS_DECISIONS"

P2 = "docs/baselines/v2.3/phase-2"
MANIFEST = f"{P2}/semantic-completion-c4-r3-manifest.json"
DECISIONS = f"{P2}/semantic-completion-c4-r3-decision-contract-options.json"
APPROVAL_MD = f"{P2}/PHASE_2C_SEMANTIC_COMPLETION_C4_R3_APPROVAL.md"
APPROVAL_VALIDATOR = "scripts/docs/validate-phase-2c-semantic-completion-c4-r3-approval.py"
APPROVAL_PATHS = [APPROVAL_MD, APPROVAL_VALIDATOR]

GENERATED_PATHS = [
    f"{P2}/SEMANTIC_COMPLETION_C4_R3_CANDIDATE.md",
    f"{P2}/SEMANTIC_COMPLETION_C4_R3_DECISION_REVIEW_PACK.md",
    f"{P2}/semantic-completion-c4-r3-decision-contract-options.json",
    f"{P2}/semantic-completion-c4-r3-decision-audit.json",
    f"{P2}/semantic-completion-c4-r3-dependency-overlap-register.json",
    f"{P2}/semantic-completion-c4-r3-source-provenance-register.json",
    f"{P2}/semantic-completion-c4-r2-custom-contracts.json",
    f"{P2}/semantic-completion-c4-r2-fixtures.json",
    f"{P2}/semantic-completion-c4-r2-execution-results.json",
    f"{P2}/semantic-completion-c4-r2-procedures.json",
    f"{P2}/semantic-completion-c4-r2-accounting.json",
    f"{P2}/semantic-completion-c4-r2-audit.json",
    f"{P2}/semantic-completion-c4-r2-mutation-delta.json",
    f"{P2}/semantic-completion-c4-r2-normalization-register.json",
    "scripts/docs/validate-phase-2c-semantic-completion-c4-r2-reproduction.py",
]

SELECTIONS = {
    **{f"P2C-SC-C1-DEC-{i:03d}": "OPT-AST" for i in range(1, 28)},
    "P2C-SC-C1-DEC-004": "OPT-A",
    "P2C-SC-C1-DEC-007": "OPT-CLARIFY",
    "P2C-SC-C1-DEC-011": "OPT-CLARIFY",
    "P2C-SC-C1-DEC-013": "OPT-A",
}

REQUIREMENTS = {
    "P2C-SC-C1-DEC-001": "BD-04-001",
    "P2C-SC-C1-DEC-002": "BD-07-014",
    "P2C-SC-C1-DEC-003": "BD-09-014",
    "P2C-SC-C1-DEC-004": "BD-16-027",
    "P2C-SC-C1-DEC-005": "BD-17-016",
    "P2C-SC-C1-DEC-006": "BRD-UPDATE-01-R028",
    "P2C-SC-C1-DEC-007": "BRD-WS-02-R004",
    "P2C-SC-C1-DEC-008": "BRD-WS-04-R011",
    "P2C-SC-C1-DEC-009": "BRD-WS-07-R001",
    "P2C-SC-C1-DEC-010": "BRD-WS-11-R009",
    "P2C-SC-C1-DEC-011": "BRD-WS-13-R003",
    "P2C-SC-C1-DEC-012": "BRD-WS-13-R021",
    "P2C-SC-C1-DEC-013": "BRD-WS-14-R013",
    "P2C-SC-C1-DEC-014": "BRD-WS-14-R025",
    "P2C-SC-C1-DEC-015": "BRD-WS-17-R018",
    "P2C-SC-C1-DEC-016": "BRD-WS-17-R029",
    "P2C-SC-C1-DEC-017": "EP-12-003",
    "P2C-SC-C1-DEC-018": "EP-13-001",
    "P2C-SC-C1-DEC-019": "EP-14-010",
    "P2C-SC-C1-DEC-020": "EP-17-001",
    "P2C-SC-C1-DEC-021": "UXF-002",
    "P2C-SC-C1-DEC-022": "UXF-003",
    "P2C-SC-C1-DEC-023": "UXF-008",
    "P2C-SC-C1-DEC-024": "UXF-02-R009",
    "P2C-SC-C1-DEC-025": "UXF-209",
    "P2C-SC-C1-DEC-026": "UXF-301",
    "P2C-SC-C1-DEC-027": "UXF-302",
}

BACKUP_OBJECTS = {
    "refs/ysim-backups/v2.3/phase-2c-document-baseline-c4-blocked": "90bc3cac386163430d78bf7c6a346e189cd55459",
    "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c1-blocked": "82818182b014e09bdbae4a83e16f7f8870f3c737",
    "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c2-blocked": "e635c3ea1ee9acfe1ecbce74d2e7b8e5e1a064e2",
    "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c3-blocked": "891cfe16ad877edf905896ff769a7a24d6c0dadd",
    "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c3-r1-rejected": "ee44c27aa92fc9f39408d86642ad09ca2e0fcecc",
    "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c4-blocked": "24037270c435a80210ab00f1b20f2a38c92ea36f",
    "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c4-r1-blocked": "a6a1075f4134689f1f5e60185bfd1986d846eb04",
    "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c4-r2-decision-incomplete": "24d72df1e1eba625b89983e80b6fad32a973bbb5",
    "refs/ysim-backups/v2.3/phase-2c-semantic-oracle-model-c1-rejected": "e7fe153e8402ca9d7a3ec7832a9d1df9f438a3bf",
}

NON_CLAIMS = [
    "NOT_FINAL_BRD_UXF_BASELINE_APPROVAL",
    "NOT_IMMEDIATE_BRD_UXF_REMEDIATION",
    "NOT_RUNTIME_ADAPTER_COMPLETION",
    "NOT_RUNTIME_MUTATION_SCORE",
    "NOT_YADF_AUTHORIZATION",
    "NOT_PRODUCTION_IMPLEMENTATION",
    "NOT_AUTOMATIC_SOURCE_COMMIT_TAG_OR_PUSH",
    "NOT_SEMANTIC_INFERENCE_BEYOND_SELECTED_OPTIONS",
]


def git(*args: str, binary: bool = False) -> str | bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=not binary).strip() if not binary else subprocess.check_output(["git", *args], cwd=ROOT)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def object_bytes(commit: str, path: str) -> bytes:
    return git("show", f"{commit}:{path}", binary=True)  # type: ignore[return-value]


def aggregate(paths: list[str]) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths):
        digest.update(path.encode("utf-8") + b"\0" + object_bytes(CANDIDATE, path) + b"\0")
    return digest.hexdigest()


def selected_option(decision: dict[str, Any], option_id: str) -> dict[str, Any]:
    return next(option for option in decision["available_options"] if option["option_id"] == option_id)


def approval_bytes(mode: str) -> bytes:
    return git("show", f":{APPROVAL_MD}", binary=True) if mode == "STAGED" else object_bytes("HEAD", APPROVAL_MD)  # type: ignore[return-value]


def main() -> int:
    head = git("rev-parse", "HEAD")
    require(git("cat-file", "-t", CANDIDATE) == "commit", "candidate commit is absent")
    require(git("rev-parse", f"{CANDIDATE}^") == PARENT, "candidate direct parent mismatch")
    require(git("rev-parse", f"{CANDIDATE}^{{tree}}") == TREE, "candidate tree mismatch")

    candidate_paths = str(git("diff", "--name-only", f"{PARENT}..{CANDIDATE}")).splitlines()
    require(len(candidate_paths) == 20, "candidate inventory is not exactly 20 files")
    require(aggregate(candidate_paths) == GIT_CONTENT_AGGREGATE, "Git-content aggregate mismatch")
    require(aggregate(GENERATED_PATHS) == GENERATED_AGGREGATE, "generated aggregate mismatch")
    require(hashlib.sha256(object_bytes(CANDIDATE, MANIFEST)).hexdigest() == MANIFEST_SHA256, "manifest SHA-256 mismatch")

    manifest = json.loads(object_bytes(CANDIDATE, MANIFEST))
    require(
        (manifest["candidate_id"], manifest["status"], manifest["approval_status"])
        == (CANDIDATE_ID, "CANDIDATE", "PENDING_HUMAN_APPROVAL"),
        "embedded candidate state changed",
    )
    require(manifest["approval_block"] == {"decision": "PENDING", "approver": None, "signature": None}, "embedded approval block changed")
    require(manifest["selected_options"] == 0, "embedded selection count changed")
    require(manifest["exact_inventory"] == candidate_paths, "manifest inventory mismatch")
    require(manifest["generated_payload_aggregate_sha256"] == GENERATED_AGGREGATE, "manifest generated aggregate mismatch")
    for path, expected in manifest["per_file_sha256_excluding_manifest"].items():
        require(hashlib.sha256(object_bytes(CANDIDATE, path)).hexdigest() == expected, f"signed blob changed: {path}")

    payload = json.loads(object_bytes(CANDIDATE, DECISIONS))
    require(payload["decision_count"] == 27 and payload["selected_count"] == 0, "candidate decision accounting changed")
    decisions = {row["decision_id"]: row for row in payload["decisions"]}
    require(set(decisions) == set(SELECTIONS) == set(REQUIREMENTS), "decision inventory mismatch")
    for decision_id, option_id in SELECTIONS.items():
        row = decisions[decision_id]
        require(row["requirement_id"] == REQUIREMENTS[decision_id], f"requirement mismatch: {decision_id}")
        require(row["selected_option"] is None and row["status"] == row["approval_status"] == "PENDING_HUMAN_APPROVAL", f"candidate decision mutated: {decision_id}")
        require(option_id in {option["option_id"] for option in row["available_options"]}, f"selected option absent: {decision_id}")

    if head == CANDIDATE:
        mode = "STAGED"
        require(str(git("diff", "--cached", "--name-only")).splitlines() == APPROVAL_PATHS, "staged approval inventory mismatch")
        require(not git("diff", "--name-only"), "tracked unstaged changes exist")
        require(not git("ls-files", "--others", "--exclude-standard"), "untracked files exist")
    else:
        mode = "COMMITTED"
        require(git("rev-parse", "HEAD^") == CANDIDATE, "accepted commit direct parent mismatch")
        require(str(git("diff", "--name-only", f"{CANDIDATE}..HEAD")).splitlines() == APPROVAL_PATHS, "candidate-to-accepted diff is not exactly two files")
        require(not git("status", "--porcelain"), "accepted checkout is not clean")

    approval = approval_bytes(mode).decode("utf-8")
    required_tokens = [
        CANDIDATE_ID, CANDIDATE, PARENT, TREE, GIT_CONTENT_AGGREGATE,
        GENERATED_AGGREGATE, MANIFEST_SHA256, f"Approval Scope: `{SCOPE}`",
        "Decision: `APPROVED`", "Authorized Approver: `Khoa, Nguyen`",
        "Signature: `Khoa, Nguyen`", "Date: `2026-07-17`",
        "Timezone: `Asia/Ho_Chi_Minh`", *NON_CLAIMS,
    ]
    for token in required_tokens:
        require(token in approval, f"approval record missing token: {token}")

    mapping_pattern = re.compile(r"^\| `(P2C-SC-C1-DEC-\d{3})` \| `([^`]+)` \| `([^`]+)` \|$", re.MULTILINE)
    mappings = mapping_pattern.findall(approval)
    require(len(mappings) == 27, "approval does not contain exactly 27 mapping rows")
    require(len({decision_id for decision_id, _, _ in mappings}) == 27, "duplicate decision mapping")
    require({decision_id: option_id for decision_id, _, option_id in mappings} == SELECTIONS, "approval selections differ from authorization")
    require({decision_id: requirement_id for decision_id, requirement_id, _ in mappings} == REQUIREMENTS, "approval requirement mappings differ")

    option_004 = json.dumps(selected_option(decisions["P2C-SC-C1-DEC-004"], "OPT-A"), ensure_ascii=False)
    for token in ("versioned Security Event Catalog", "event type", "trigger", "correlation", "payload"):
        require(token.lower() in option_004.lower(), f"DEC-004 candidate effect missing: {token}")
        require(token.lower() in approval.lower(), f"DEC-004 approval effect missing: {token}")
    require("No fixed universal event list is inferred." in approval and "Runtime implementation is not claimed." in approval, "DEC-004 non-inferences missing")

    option_013 = json.dumps(selected_option(decisions["P2C-SC-C1-DEC-013"], "OPT-A"), ensure_ascii=False)
    for token in ("addressable", "overwrite"):
        require(token.lower() in option_013.lower(), f"DEC-013 candidate effect missing: {token}")
        require(token.lower() in approval.lower(), f"DEC-013 approval effect missing: {token}")
    require("no finite duration" in option_013.lower(), "DEC-013 candidate duration non-inference missing")
    require("No finite retention duration is inferred" in approval, "DEC-013 approval duration non-inference missing")
    require("Configuration Version history is append-only." in approval, "DEC-013 append-only effect missing")

    for decision_id, tokens in {
        "P2C-SC-C1-DEC-007": ("Inventory Status", "Lifecycle", "QR Code", "ICCID", "Activation Code", "Supplier Reference", "Purchase Cost", "Current Owner"),
        "P2C-SC-C1-DEC-011": ("Dashboard", "Workspace", "Admin Portal", "Organization Portal", "Customer Portal"),
    }.items():
        option = json.dumps(selected_option(decisions[decision_id], "OPT-CLARIFY"), ensure_ascii=False)
        for token in tokens:
            require(token in option, f"candidate clarification missing {token}: {decision_id}")
            require(token in approval, f"approval clarification missing {token}: {decision_id}")

    require(not git("diff", "--name-only", f"{PARENT}..{CANDIDATE}", "--", "docs/BRD", "docs/UXF"), "candidate changed BRD/UXF")
    if mode == "COMMITTED":
        require(not git("diff", "--name-only", f"{CANDIDATE}..HEAD", "--", "docs/BRD", "docs/UXF"), "approval changed BRD/UXF")
    for ref, expected in BACKUP_OBJECTS.items():
        require(git("rev-parse", ref) == expected, f"backup ref changed: {ref}")

    print("VALID_APPROVED_PHASE_2C_SEMANTIC_COMPLETION_C4_R3")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, StopIteration, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(f"FAIL — {exc}")
        raise SystemExit(1)
