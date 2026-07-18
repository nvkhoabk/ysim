#!/usr/bin/env python3
"""Validate detached approval for VS001 implementation decision C1."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = "51857c222509b058067589d8d2dab42cd0593dff"
GOVERNING = "4a0ff5700554023b30d9a6dba01d80d1dbc78867"
CANDIDATE_TREE = "bd6d4c556235754c3e91768980d802b6084cbc78"
GIT_AGGREGATE = "0fe206520b3282fe1e1d6dd2a9c70b913c66d5bc94d641081f2395b338559c58"
GENERATED_AGGREGATE = "d9dbe169c00945194acb7bcd23e70d604accfaf5fbb343b5e523f2effcc86e5b"
CANDIDATE_FILES = [
    "docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_DECISION_C1_CANDIDATE.md",
    "docs/baselines/v2.3/phase-2d/vs001-implementation-decision-c1.json",
    "docs/baselines/v2.3/phase-2d/vs001-implementation-decision-c1-manifest.json",
    "scripts/docs/build-phase-2d-vs001-implementation-decision-c1.py",
    "scripts/docs/validate-phase-2d-vs001-implementation-decision-c1.py",
    "scripts/docs/tests/test-phase-2d-vs001-implementation-decision-c1.py",
]
APPROVAL_FILES = [
    "docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_DECISION_C1_APPROVAL.md",
    "scripts/docs/validate-phase-2d-vs001-implementation-decision-c1-approval.py",
]
HASHES = {
    CANDIDATE_FILES[0]: "24121c7a1e680954993b3b099884546ba7b30cd3d05fcda59668a57006f1b8d6",
    CANDIDATE_FILES[1]: "08c22be8b5ff29e0d8b8dbd3aa3ddeeed74533fe866848d5ad051f832d7df705",
    CANDIDATE_FILES[2]: "cf2ed65e0bcf318a3f02730c7f14dad98e20c5e5fb0250c433c4d00de8af742b",
    CANDIDATE_FILES[3]: "7412030cd9d110246b5f43afa18e8d96f81862bc847cff6365dd1526a74b1d02",
    CANDIDATE_FILES[4]: "a9f58fdd339b3a7ab4db57ea7f5e5206c62e1d0fcbdb6f2cf67affa42a4bee5b",
    CANDIDATE_FILES[5]: "a8bced8c4739538c2cd744306f2f3d8cb18245f0e086a60daa4d3e032727e5b2",
}
SELECTIONS = {
    "V23-P2D-VS001-IMPLEMENTATION-DEC-001": "OPT-V1-STOREFRONT-RESOURCE-HIERARCHY",
    "V23-P2D-VS001-IMPLEMENTATION-DEC-002": "OPT-BCP47-REQUEST-THEN-STOREFRONT-DEFAULT",
    "V23-P2D-VS001-IMPLEMENTATION-DEC-003": "OPT-OPAQUE-CURSOR-SLUG-IDENTITY-ORDER",
    "V23-P2D-VS001-IMPLEMENTATION-DEC-004": "OPT-EXPLICIT-DATA-META-DTO",
    "V23-P2D-VS001-IMPLEMENTATION-DEC-005": "OPT-STOREFRONT-ENTRY-SLUG-UUIDV7-PUBLIC-ID",
    "V23-P2D-VS001-IMPLEMENTATION-DEC-006": "OPT-HYBRID-RELATIONAL-CORE-JSONB-SPECIFICATION",
    "V23-P2D-VS001-IMPLEMENTATION-DEC-007": "OPT-FORWARD-MIGRATION-SEPARATE-FIXTURE-LOADER",
    "V23-P2D-VS001-IMPLEMENTATION-DEC-008": "OPT-REQUEST-TIMESTAMP-REPEATABLE-READ-SNAPSHOT",
    "V23-P2D-VS001-IMPLEMENTATION-DEC-009": "OPT-SERVER-CORRELATION-ID-ALLOWLISTED-AUDIT",
}


class ApprovalFailure(RuntimeError):
    pass


def fail(code: str, detail: str) -> None:
    raise ApprovalFailure(f"{code}: {detail}")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def git_bytes(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_sha(value: object) -> str:
    return sha((json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode())


def aggregate(files: dict[str, bytes], paths: list[str]) -> str:
    return canonical_sha([{"path": path, "sha256": sha(files[path])} for path in sorted(paths)])


def lifecycle() -> tuple[str, str, dict[str, bytes]]:
    head = git("rev-parse", "HEAD")
    staged = set(git("diff", "--cached", "--name-only").splitlines())
    status = set(git("status", "--porcelain=v1", "--untracked-files=all").splitlines())
    expected = set(APPROVAL_FILES)
    if head == CANDIDATE and staged == expected:
        if status != {f"A  {path}" for path in expected}:
            fail("STAGED_APPROVAL_DIRTY", repr(status))
        return "STAGED_APPROVAL_OVER_CANDIDATE", head, {
            path: subprocess.check_output(["git", "show", f":{path}"], cwd=ROOT) for path in APPROVAL_FILES
        }
    if git("rev-parse", "HEAD^") == CANDIDATE:
        if status:
            fail("ACCEPTED_APPROVAL_DIRTY", repr(status))
        delta = set(git("diff", "--name-only", CANDIDATE, "HEAD").splitlines())
        if delta != expected:
            fail("CANDIDATE_ACCEPTED_DIFF_MISMATCH", repr(delta))
        return "COMMITTED_ACCEPTED", head, {path: git_bytes(head, path) for path in APPROVAL_FILES}
    fail("APPROVAL_LIFECYCLE_INVALID", head)


def validate_candidate() -> dict:
    if git("rev-parse", f"{CANDIDATE}^") != GOVERNING:
        fail("CANDIDATE_PARENT_MISMATCH", CANDIDATE)
    if git("rev-parse", f"{CANDIDATE}^{{tree}}") != CANDIDATE_TREE:
        fail("CANDIDATE_TREE_MISMATCH", CANDIDATE)
    if set(git("diff", "--name-only", GOVERNING, CANDIDATE).splitlines()) != set(CANDIDATE_FILES):
        fail("CANDIDATE_INVENTORY_MISMATCH", CANDIDATE)
    files = {path: git_bytes(CANDIDATE, path) for path in CANDIDATE_FILES}
    for path, expected in HASHES.items():
        if sha(files[path]) != expected:
            fail("CANDIDATE_HASH_MISMATCH", path)
    if aggregate(files, CANDIDATE_FILES) != GIT_AGGREGATE:
        fail("CANDIDATE_GIT_AGGREGATE_MISMATCH", CANDIDATE)
    if aggregate(files, [CANDIDATE_FILES[1], CANDIDATE_FILES[0]]) != GENERATED_AGGREGATE:
        fail("CANDIDATE_GENERATED_AGGREGATE_MISMATCH", CANDIDATE)
    payload = json.loads(files[CANDIDATE_FILES[1]])
    if payload.get("candidate_id") != "V23-P2D-VS001-IMPLEMENTATION-DECISION-C1" or payload.get("status") != "CANDIDATE" or payload.get("approval") != "PENDING_HUMAN_APPROVAL":
        fail("CANDIDATE_STATE_MISMATCH", "metadata")
    if payload.get("implementation_authorized") is not False or payload.get("runtime_evidence_status") != "NOT_EXECUTED" or payload.get("implementation_contract_created") is not False:
        fail("CANDIDATE_NON_AUTHORIZATION_MISMATCH", "implementation/runtime")
    decisions = payload.get("decisions", [])
    if len(decisions) != 9 or any(item.get("selected_option") is not None for item in decisions):
        fail("CANDIDATE_SELECTION_STATE_MISMATCH", str(len(decisions)))
    options = {item["decision_id"]: {option["option_id"] for option in item["options"]} for item in decisions}
    for decision_id, option_id in SELECTIONS.items():
        if option_id not in options.get(decision_id, set()):
            fail("APPROVED_OPTION_NOT_IN_CANDIDATE", f"{decision_id}:{option_id}")
    return payload


def validate_approval(files: dict[str, bytes]) -> None:
    text = files[APPROVAL_FILES[0]].decode()
    required = [
        "Decision: `APPROVED`", "Khoa, Nguyen", "2026-07-19",
        "PHASE_2D_VS001_IMPLEMENTATION_TECHNICAL_DECISIONS_ONLY",
        CANDIDATE, GOVERNING, CANDIDATE_TREE, GIT_AGGREGATE, GENERATED_AGGREGATE,
        "all nine `selected_option` fields null", "effective selections exist only in this detached approval layer",
        "NOT_VS001_IMPLEMENTATION_AUTHORIZATION", "NOT_DATABASE_SCHEMA_OR_MIGRATION", "NOT_RUNTIME_EVIDENCE",
    ]
    required.extend(HASHES.values())
    required.extend(SELECTIONS.values())
    for token in required:
        if token not in text:
            fail("APPROVAL_CONTENT_MISSING", token)
    prohibited = ["implementation_authorized=true", "runtime_evidence_status=PASS", "IMPLEMENTATION_CONTRACT_APPROVED"]
    for token in prohibited:
        if token in text:
            fail("APPROVAL_SCOPE_OVERREACH", token)


def main() -> None:
    try:
        mode, accepted, files = lifecycle()
        validate_candidate()
        validate_approval(files)
        result = {
            "result": "VALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_DECISION_C1",
            "lifecycle_mode": mode,
            "candidate_commit": CANDIDATE,
            "accepted_commit": accepted if mode == "COMMITTED_ACCEPTED" else None,
            "candidate_tree": CANDIDATE_TREE,
            "candidate_files": 6,
            "approval_files": 2,
            "decisions": 9,
            "effective_selections": 9,
            "candidate_selected_options": 0,
            "implementation_contract_created": False,
            "implementation_authorized": False,
            "runtime_evidence_status": "NOT_EXECUTED",
        }
        print(json.dumps(result, sort_keys=True))
        print("VALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_DECISION_C1")
    except (ApprovalFailure, KeyError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"INVALID_PHASE_2D_VS001_IMPLEMENTATION_DECISION_C1_APPROVAL: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
