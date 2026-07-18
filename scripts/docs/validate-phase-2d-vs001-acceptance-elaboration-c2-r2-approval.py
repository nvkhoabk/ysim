#!/usr/bin/env python3
"""Independently validate detached approval of VS001 Acceptance Elaboration C2-R2."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = "5780bf5e89c66103980fd4cda7c2b294fdc23f20"
GOVERNING = "c818d734049fbf8997a5dce4e1e66e65d6a92f59"
DECISION_CANDIDATE = "f003eca82512887a616c4ee83ed4ab8da4432b8a"
DECISION_BASE = "f7f2aeca3c1643996f77dec1b0b5caae22363ddc"
CANDIDATE_TREE = "aa8c81032777c30e0c30e4c1b9ceadcfca610591"
EXPECTED_GIT_AGGREGATE = "382d7de9d17ed61800132fc2fea6533ed5650b483b73d894133f0e64358de499"
EXPECTED_GENERATED_AGGREGATE = "b57b530fc984266674856bfa003a2fcbc322296781846830c43ea175922dc8fa"

CANDIDATE_FILES = [
    "docs/baselines/v2.3/phase-2d/VS001_ACCEPTANCE_ELABORATION_C2_R2_CANDIDATE.md",
    "docs/baselines/v2.3/phase-2d/vs001-acceptance-elaboration-c2-r2.json",
    "docs/baselines/v2.3/phase-2d/vs001-acceptance-elaboration-c2-r2-manifest.json",
    "scripts/docs/build-phase-2d-vs001-acceptance-elaboration-c2-r2.py",
    "scripts/docs/validate-phase-2d-vs001-acceptance-elaboration-c2-r2.py",
    "scripts/docs/tests/test-phase-2d-vs001-acceptance-elaboration-c2-r2.py",
]
APPROVAL_FILES = [
    "docs/baselines/v2.3/phase-2d/VS001_ACCEPTANCE_ELABORATION_C2_R2_APPROVAL.md",
    "scripts/docs/validate-phase-2d-vs001-acceptance-elaboration-c2-r2-approval.py",
]
EXPECTED_HASHES = {
    CANDIDATE_FILES[0]: "b64e094af418a6a4910e8c81b550f26371f31d022ffe191144dbddb646a06abd",
    CANDIDATE_FILES[1]: "d80d6c5b00660eb9dc5a8d3835f9dd6baecca93e732def903f568b675af71ac7",
    CANDIDATE_FILES[2]: "7285c30e18afcfe324dbe8e12e2e0c310de20f24e0ed6197057771c20dbba874",
    CANDIDATE_FILES[3]: "cbae11ac761dd5fd94b1d894e011ad35bd074113dc20e821496a7e3e3f435d6c",
    CANDIDATE_FILES[4]: "bb3c1edf79ab19fda196c8738eed500695c141411124efb386aa9eaedf40fa3f",
    CANDIDATE_FILES[5]: "12b7e7541baba51c5cadb08bf3baeb008cbdd181489f64a103fc9ed79e74d8e1",
}
SELECTIONS = {
    "V23-P2D-VS001-ACCEPTANCE-DEC-001": "OPT-PUBLISHED-STOREFRONT-ELIGIBLE",
    "V23-P2D-VS001-ACCEPTANCE-DEC-002": "OPT-MINIMUM-COMMERCIAL-DISPLAY-WITH-PRICE",
    "V23-P2D-VS001-ACCEPTANCE-DEC-003": "OPT-STABLE-SLUG-UNIFORM-NOT-FOUND",
}


class ApprovalFailure(RuntimeError):
    pass


def fail(code: str, detail: str) -> None:
    raise ApprovalFailure(f"{code}: {detail}")


def git(*args: str, text: bool = True) -> str | bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=text).strip()


def git_bytes(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_sha(value: object) -> str:
    encoded = (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    return sha(encoded)


def aggregate(files: dict[str, bytes], paths: list[str]) -> str:
    records = [{"path": path, "sha256": sha(files[path])} for path in sorted(paths)]
    return canonical_sha(records)


def approval_lifecycle() -> tuple[str, str, dict[str, bytes]]:
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
    if str(git("rev-parse", "HEAD^")) == CANDIDATE:
        if status:
            fail("ACCEPTED_APPROVAL_DIRTY_STATE", repr(status))
        delta = set(str(git("diff", "--name-only", CANDIDATE, "HEAD")).splitlines())
        if delta != expected:
            fail("CANDIDATE_ACCEPTED_DIFF_MISMATCH", repr(delta))
        return "COMMITTED_ACCEPTED", head, {path: git_bytes(head, path) for path in APPROVAL_FILES}
    fail("APPROVAL_LIFECYCLE_INVALID", head)


def validate_candidate() -> dict:
    if str(git("rev-parse", f"{CANDIDATE}^")) != GOVERNING:
        fail("CANDIDATE_DIRECT_PARENT_MISMATCH", CANDIDATE)
    if str(git("rev-parse", f"{CANDIDATE}^{{tree}}")) != CANDIDATE_TREE:
        fail("CANDIDATE_TREE_MISMATCH", CANDIDATE)
    delta = set(str(git("diff", "--name-only", GOVERNING, CANDIDATE)).splitlines())
    if delta != set(CANDIDATE_FILES):
        fail("CANDIDATE_INVENTORY_MISMATCH", repr(delta))
    files = {path: git_bytes(CANDIDATE, path) for path in CANDIDATE_FILES}
    for path, expected in EXPECTED_HASHES.items():
        observed = sha(files[path])
        if observed != expected:
            fail("SIGNED_CANDIDATE_HASH_MISMATCH", f"{path}: {observed}")
    if aggregate(files, CANDIDATE_FILES) != EXPECTED_GIT_AGGREGATE:
        fail("SIGNED_GIT_AGGREGATE_MISMATCH", CANDIDATE)
    if aggregate(files, [CANDIDATE_FILES[1], CANDIDATE_FILES[0]]) != EXPECTED_GENERATED_AGGREGATE:
        fail("SIGNED_GENERATED_AGGREGATE_MISMATCH", CANDIDATE)

    payload = json.loads(files[CANDIDATE_FILES[1]])
    expected_metadata = {
        "candidate_id": "V23-P2D-VS001-ACCEPTANCE-ELABORATION-C2-R2",
        "status": "CANDIDATE",
        "approval": "PENDING_HUMAN_APPROVAL",
        "approval_ready": True,
        "runtime_evidence_status": "NOT_EXECUTED",
        "implementation_authorized": False,
        "governing_commit": GOVERNING,
    }
    for key, expected in expected_metadata.items():
        if payload.get(key) != expected:
            fail("CANDIDATE_LIFECYCLE_PAYLOAD_MISMATCH", key)
    population = payload.get("population", {})
    expected_population = {
        "total": 25,
        "retained": 9,
        "elaborated": 16,
        "governing_decisions": 3,
        "acceptance_coverage": 25,
        "source_verification": 25,
        "runtime_evidence_executed": 0,
        "unresolved_contracts": 0,
        "invalid_or_blocked_contracts": 0,
    }
    for key, expected in expected_population.items():
        if population.get(key) != expected:
            fail("CANDIDATE_ACCOUNTING_MISMATCH", key)
    contracts = sum((payload[name] for name in ("batch_1_contracts", "batch_2_contracts", "batch_3_contracts")), [])
    obligations = sum(len(contract["obligation_mapping"]) for contract in contracts)
    criteria = sum(len(contract["positive_outcomes"]) for contract in contracts)
    if len(payload["retained_contracts"]) != 9 or len(contracts) != 16 or obligations != 21 or criteria != 32:
        fail("CANDIDATE_CONTRACT_ACCOUNTING_MISMATCH", f"9/{len(contracts)}/{obligations}/{criteria}")
    clauses = payload.get("decision_derived_acceptance_clauses", [])
    counts = {
        decision: sum(clause.get("decision_id") == decision for clause in clauses) for decision in SELECTIONS
    }
    if len(clauses) != 124 or list(counts.values()) != [27, 54, 43]:
        fail("CANDIDATE_DECISION_CLAUSE_ACCOUNTING_MISMATCH", repr(counts))
    observed_selections = {item["decision_id"]: item["selected_option"] for item in payload["governing_decisions"]}
    if observed_selections != SELECTIONS:
        fail("CANDIDATE_GOVERNING_SELECTION_MISMATCH", repr(observed_selections))
    return payload


def validate_governing_decision() -> None:
    if str(git("rev-parse", f"{GOVERNING}^")) != DECISION_CANDIDATE:
        fail("DECISION_ACCEPTED_PARENT_MISMATCH", GOVERNING)
    if str(git("rev-parse", f"{DECISION_CANDIDATE}^")) != DECISION_BASE:
        fail("DECISION_CANDIDATE_PARENT_MISMATCH", DECISION_CANDIDATE)
    decision_path = "docs/baselines/v2.3/phase-2d/vs001-acceptance-decision-c1.json"
    approval_path = "docs/baselines/v2.3/phase-2d/VS001_ACCEPTANCE_DECISION_C1_APPROVAL.md"
    decision = json.loads(git_bytes(DECISION_CANDIDATE, decision_path))
    if any(item.get("selected_option") is not None for item in decision["decisions"]):
        fail("DECISION_CANDIDATE_SELECTION_NOT_NULL", DECISION_CANDIDATE)
    option_sets = {item["decision_id"]: {option["option_id"] for option in item["options"]} for item in decision["decisions"]}
    for decision_id, option_id in SELECTIONS.items():
        if option_id not in option_sets.get(decision_id, set()):
            fail("GOVERNING_OPTION_MISSING", f"{decision_id}:{option_id}")
    approval = git_bytes(GOVERNING, approval_path).decode()
    for token in ["Khoa, Nguyen", *SELECTIONS.values()]:
        if token not in approval:
            fail("GOVERNING_APPROVAL_CONTENT_MISMATCH", token)


def validate_approval(files: dict[str, bytes]) -> None:
    approval = files[APPROVAL_FILES[0]].decode()
    required = [
        "Decision: `APPROVED`",
        "V23-P2D-VS001-ACCEPTANCE-ELABORATION-C2-R2",
        CANDIDATE,
        GOVERNING,
        CANDIDATE_TREE,
        EXPECTED_GIT_AGGREGATE,
        EXPECTED_GENERATED_AGGREGATE,
        "Khoa, Nguyen",
        "2026-07-18",
        "PHASE_2D_VS001_ACCEPTANCE_ELABORATION_CONTRACTS_ONLY",
        "25-requirement VS001 acceptance boundary",
        "nine retained signed Renderer C2 contracts",
        "sixteen elaborated source-derived contracts",
        "124 concrete Decision C1-derived acceptance clauses",
        "Effective human approval exists only in this detached approval layer",
        "NOT_VS001_IMPLEMENTATION_AUTHORIZATION",
    ]
    required.extend(EXPECTED_HASHES.values())
    required.extend(SELECTIONS.values())
    for token in required:
        if token not in approval:
            fail("APPROVAL_CONTENT_MISSING", token)
    prohibited = ["implementation_authorized=true", "runtime_evidence_status=PASS", "APPROVED_IMPLEMENTATION"]
    for token in prohibited:
        if token in approval:
            fail("APPROVAL_SCOPE_OVERREACH", token)


def main() -> None:
    try:
        mode, accepted, approval_files = approval_lifecycle()
        validate_candidate()
        validate_governing_decision()
        validate_approval(approval_files)
        result = {
            "result": "VALID_APPROVED_PHASE_2D_VS001_ACCEPTANCE_ELABORATION_C2_R2",
            "lifecycle_mode": mode,
            "candidate_commit": CANDIDATE,
            "accepted_commit": accepted if mode == "COMMITTED_ACCEPTED" else None,
            "candidate_tree": CANDIDATE_TREE,
            "candidate_files": 6,
            "approval_files": 2,
            "requirements": 25,
            "retained": 9,
            "elaborated": 16,
            "source_obligations": 21,
            "criteria": 32,
            "decision_clauses": 124,
            "runtime_evidence_executed": 0,
            "implementation_authorized": False,
        }
        print(json.dumps(result, sort_keys=True))
        print("VALID_APPROVED_PHASE_2D_VS001_ACCEPTANCE_ELABORATION_C2_R2")
    except (ApprovalFailure, AssertionError, KeyError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"INVALID_PHASE_2D_VS001_ACCEPTANCE_ELABORATION_C2_R2_APPROVAL: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
