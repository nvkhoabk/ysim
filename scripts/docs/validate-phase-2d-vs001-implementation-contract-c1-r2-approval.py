#!/usr/bin/env python3
"""Independently validate detached approval of VS001 implementation contract C1-R2."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GOVERNING = "f67422a19fb91a03f3e7c8336268724262c696e7"
CANDIDATE = "e29f2835947987ebb864062427d371f2eaa21074"
CANDIDATE_TREE = "0e3ff28fdcee64c12c323d6e9f3312836932b582"
GIT_AGGREGATE = "b35841b8f0baf3d17926e3a94b1a6dc4488e127129ea2a0adf6fe27bd753f1ee"
GENERATED_AGGREGATE = "50a82628a5e9bd9bf497a9c4dede06eab38c0a466e42b573fc4f62cc50a28859"

CANDIDATE_FILES = [
    "docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_CONTRACT_C1_R2_CANDIDATE.md",
    "docs/baselines/v2.3/phase-2d/vs001-implementation-contract-c1-r2.json",
    "docs/baselines/v2.3/phase-2d/vs001-implementation-contract-c1-r2-manifest.json",
    "scripts/docs/build-phase-2d-vs001-implementation-contract-c1-r2.py",
    "scripts/docs/validate-phase-2d-vs001-implementation-contract-c1-r2.py",
    "scripts/docs/tests/test-phase-2d-vs001-implementation-contract-c1-r2.py",
]
APPROVAL_FILES = [
    "docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_CONTRACT_C1_R2_APPROVAL.md",
    "scripts/docs/validate-phase-2d-vs001-implementation-contract-c1-r2-approval.py",
]
HASHES = {
    CANDIDATE_FILES[0]: "b9aefb7e388df5c6a8ee400bc11987d55c09e6673a4744edfd8a4fb5d938d30f",
    CANDIDATE_FILES[1]: "8d7ef0dbb4d4621ef0385d5b23669836b8fffdc50df7528432c6f6fd6882f539",
    CANDIDATE_FILES[2]: "cee66b2c329f840b2cd71680458160f9d6d6d0c3fb2ad9a38b8e703f5b385e23",
    CANDIDATE_FILES[3]: "25eebbea9b56cab546ac220a1ab28b693ec4f94290576651eff691ca05c4cfac",
    CANDIDATE_FILES[4]: "23aacf8f7c916f3f9d9373b0f42446c3c300d4fab0f570eb76a1a95b4f27822b",
    CANDIDATE_FILES[5]: "1207d2d260f0378560e5e1fe10b52f8fad3abbb063de78ebfc78b28cb90e957a",
}
EXPECTED_ACCOUNTING = {
    "requirements": 25,
    "retained": 9,
    "elaborated": 16,
    "source_obligations": 21,
    "source_criteria": 32,
    "acceptance_clauses": 124,
    "implementation_decisions": 9,
    "continuity_decisions": 2,
    "traceability_mappings": 211,
    "decision_bindings": 11,
    "inherited_commands": 10,
    "focused_commands": 12,
    "batches": 7,
}


class ApprovalError(RuntimeError):
    pass


def fail(code: str, detail: str = "") -> None:
    raise ApprovalError(code + (": " + detail if detail else ""))


def git(*args: str, text: bool = True) -> str | bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=text).strip()


def git_bytes(ref: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_sha(value: object) -> str:
    body = (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    return sha(body)


def aggregate(files: dict[str, bytes], paths: list[str]) -> str:
    return canonical_sha([{"path": path, "sha256": sha(files[path])} for path in sorted(paths)])


def lifecycle() -> tuple[str, str, dict[str, bytes]]:
    head = str(git("rev-parse", "HEAD"))
    staged = set(str(git("diff", "--cached", "--name-only")).splitlines())
    status = set(str(git("status", "--porcelain=v1", "--untracked-files=all")).splitlines())
    expected = set(APPROVAL_FILES)
    if head == CANDIDATE and staged == expected:
        if status != {f"A  {path}" for path in expected}:
            fail("STAGED_APPROVAL_DIRTY_STATE", repr(status))
        return "STAGED_APPROVAL_OVER_CANDIDATE", head, {
            path: subprocess.check_output(["git", "show", f":{path}"], cwd=ROOT) for path in APPROVAL_FILES
        }
    try:
        parent = str(git("rev-parse", "HEAD^"))
    except subprocess.CalledProcessError:
        parent = ""
    if parent == CANDIDATE:
        if status:
            fail("ACCEPTED_APPROVAL_DIRTY_STATE", repr(status))
        delta = set(str(git("diff", "--name-only", CANDIDATE, "HEAD")).splitlines())
        if delta != expected:
            fail("CANDIDATE_ACCEPTED_DIFF_MISMATCH", repr(delta))
        return "COMMITTED_ACCEPTED", head, {path: git_bytes(head, path) for path in APPROVAL_FILES}
    fail("APPROVAL_LIFECYCLE_INVALID", head)


def validate_candidate() -> dict[str, object]:
    if str(git("rev-parse", f"{CANDIDATE}^")) != GOVERNING:
        fail("CANDIDATE_DIRECT_PARENT_MISMATCH")
    if str(git("rev-parse", f"{CANDIDATE}^{{tree}}")) != CANDIDATE_TREE:
        fail("CANDIDATE_TREE_MISMATCH")
    delta = set(str(git("diff", "--name-only", GOVERNING, CANDIDATE)).splitlines())
    if delta != set(CANDIDATE_FILES):
        fail("CANDIDATE_INVENTORY_MISMATCH", repr(delta))
    files = {path: git_bytes(CANDIDATE, path) for path in CANDIDATE_FILES}
    for path, expected in HASHES.items():
        if sha(files[path]) != expected:
            fail("SIGNED_CANDIDATE_BLOB_MISMATCH", path)
    if aggregate(files, CANDIDATE_FILES) != GIT_AGGREGATE:
        fail("CANDIDATE_GIT_AGGREGATE_MISMATCH")
    if aggregate(files, [CANDIDATE_FILES[0], CANDIDATE_FILES[1]]) != GENERATED_AGGREGATE:
        fail("CANDIDATE_GENERATED_AGGREGATE_MISMATCH")

    payload = json.loads(files[CANDIDATE_FILES[1]])
    if (
        payload.get("candidate_id") != "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-C1-R2"
        or payload.get("status") != "CANDIDATE"
        or payload.get("approval") != "PENDING_HUMAN_APPROVAL"
    ):
        fail("SIGNED_CANDIDATE_LIFECYCLE_MISMATCH")
    if payload.get("runtime_evidence_status") != "NOT_EXECUTED":
        fail("FALSE_RUNTIME_EVIDENCE_CLAIM")
    if payload.get("implementation_authorized") is not False:
        fail("CANDIDATE_PREMATURE_IMPLEMENTATION_AUTHORIZATION")
    accounting = payload.get("accounting", {})
    for key, expected in EXPECTED_ACCOUNTING.items():
        if accounting.get(key) != expected:
            fail("CANDIDATE_ACCOUNTING_MISMATCH", key)
    if len(payload.get("traceability_mappings", [])) != 211 or len(payload.get("decision_bindings", [])) != 11:
        fail("CANDIDATE_CONTRACT_POPULATION_MISMATCH")
    return {"candidate_files": 6, "mappings": 211, "bindings": 11, "commands": 22, "batches": 7}


def validate_approval(blobs: dict[str, bytes]) -> None:
    text = blobs[APPROVAL_FILES[0]].decode()
    required = [
        "Authorized approver: `Khoa, Nguyen`",
        "Approval date: `2026-07-19`",
        "Approval scope: `PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_AND_CONTROLLED_IMPLEMENTATION_ENTRY`",
        f"Candidate commit: `{CANDIDATE}`",
        f"Candidate direct parent: `{GOVERNING}`",
        f"Candidate tree: `{CANDIDATE_TREE}`",
        f"Git-content aggregate: `{GIT_AGGREGATE}`",
        f"Generated aggregate: `{GENERATED_AGGREGATE}`",
        "NOT_RUNTIME_EVIDENCE_EXECUTION_IN_APPROVAL_PERSISTENCE",
        "NOT_VS001_IMPLEMENTATION_IN_APPROVAL_PERSISTENCE",
        "NOT_FINAL_RUNTIME_ACCEPTANCE_BEFORE_REAL_EVIDENCE_AUDIT_AND_HUMAN_APPROVAL",
    ]
    if not all(item in text for item in required):
        fail("APPROVAL_IDENTITY_SCOPE_OR_NONCLAIM_MISMATCH")
    if "separate VS001 implementation\nturn" not in text:
        fail("CONTROLLED_IMPLEMENTATION_ENTRY_NOT_DETACHED")


def validate_boundaries(mode: str, accepted: str) -> None:
    if mode == "COMMITTED_ACCEPTED":
        delta = set(str(git("diff", "--name-only", CANDIDATE, accepted)).splitlines())
        if delta != set(APPROVAL_FILES):
            fail("APPROVAL_DIFF_NOT_EXACT_TWO_FILES")
        total = set(str(git("diff", "--name-only", GOVERNING, accepted)).splitlines())
    else:
        total = set(str(git("diff", "--name-only", GOVERNING, CANDIDATE)).splitlines())
        total |= set(str(git("diff", "--cached", "--name-only")).splitlines())
    if total != set(CANDIDATE_FILES) | set(APPROVAL_FILES):
        fail("ACCEPTED_TOTAL_INVENTORY_MISMATCH", repr(total))
    protected = ("apps/", "packages/", "database/", "configs/", "docs/BRD/", "docs/UXF/", "scripts/commissioning/", "runtime/", "infrastructure/", "YADF/", "deployment/")
    if any(path.startswith(protected) for path in total):
        fail("IMPLEMENTATION_OR_PROTECTED_PATH_CHANGE")


def main() -> int:
    try:
        mode, accepted, approval_blobs = lifecycle()
        candidate = validate_candidate()
        validate_approval(approval_blobs)
        validate_boundaries(mode, accepted)
        result = {
            "result": "VALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_C1_R2",
            "lifecycle_mode": mode,
            "candidate_commit": CANDIDATE,
            "accepted_commit": accepted if mode == "COMMITTED_ACCEPTED" else None,
            "candidate_tree": CANDIDATE_TREE,
            "approval_files": 2,
            "implementation_in_persistence": 0,
            "runtime_evidence_executed": 0,
            **candidate,
        }
        print(json.dumps(result, sort_keys=True))
        print("VALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_C1_R2")
        return 0
    except (ApprovalError, KeyError, TypeError, ValueError, UnicodeDecodeError, subprocess.CalledProcessError) as error:
        print("INVALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_C1_R2", error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
