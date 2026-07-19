#!/usr/bin/env python3
"""Validate detached approval of the VS001 execution-boundary amendment A2."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GOVERNING = "77c25755ece698088820447f92b094594e9e21c4"
CANDIDATE = "4fd47a8ca75f6eded632de16201d186d3756f9f8"
CANDIDATE_TREE = "e4b5e82df51c171c24028c4cbe02c82d3da56ddb"
GIT_AGGREGATE = "87cb960deeb3b72f49a37535023a4459dec80de7971eedbb2bd88531dea3b01e"
GENERATED_AGGREGATE = "a0dd30c855263bde2f273999275644fa6b849630184bc478f07ff9ce5a9dab6b"

CANDIDATE_FILES = [
    "docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2_CANDIDATE.md",
    "docs/baselines/v2.3/phase-2d/vs001-implementation-contract-execution-boundary-amendment-a2.json",
    "docs/baselines/v2.3/phase-2d/vs001-implementation-contract-execution-boundary-amendment-a2-manifest.json",
    "scripts/docs/build-phase-2d-vs001-implementation-contract-execution-boundary-amendment-a2.py",
    "scripts/docs/validate-phase-2d-vs001-implementation-contract-execution-boundary-amendment-a2.py",
    "scripts/docs/tests/test-phase-2d-vs001-implementation-contract-execution-boundary-amendment-a2.py",
]
APPROVAL_FILES = [
    "docs/baselines/v2.3/phase-2d/VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2_APPROVAL.md",
    "scripts/docs/validate-phase-2d-vs001-implementation-contract-execution-boundary-amendment-a2-approval.py",
]
HASHES = {
    CANDIDATE_FILES[0]: "fe5299a97d92a943c651122922512d036452a5feaa140f2209cf337a2def221f",
    CANDIDATE_FILES[1]: "a27d45016a76223f57c704d462f7b0e24dd88d6c01a8db14d1b74d0453a45b8e",
    CANDIDATE_FILES[2]: "bc719acac485e22d3c0c8f9ee400d7e25c249b55552a693f06ce52081f4ed3f3",
    CANDIDATE_FILES[3]: "0f08cfbb58388c7f1503959e1365acdcf5ab95af7bc51e22382a4c666fc45a04",
    CANDIDATE_FILES[4]: "a152becb0acb492bf89e7c53121bda57729ea48daa13d3dac189bb3ca04ac519",
    CANDIDATE_FILES[5]: "a6cc4b0ca0590025e9021268a813b6fbd931e12e2cf29c3c0aff6b5dd3ff15cb",
}


class ApprovalError(RuntimeError):
    pass


def fail(code: str, detail: str = "") -> None:
    raise ApprovalError(code + (": " + detail if detail else ""))


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def git_bytes(ref: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def aggregate(files: dict[str, bytes], paths: list[str]) -> str:
    return sha(canonical([{"path": path, "sha256": sha(files[path])} for path in sorted(paths)]))


def lifecycle() -> tuple[str, str, dict[str, bytes]]:
    head = git("rev-parse", "HEAD")
    staged = set(git("diff", "--cached", "--name-only").splitlines())
    status = set(git("status", "--porcelain=v1", "--untracked-files=all").splitlines())
    expected = set(APPROVAL_FILES)
    if head == CANDIDATE and staged == expected:
        if status != {f"A  {path}" for path in expected}:
            fail("A2_APPROVAL_STAGED_DIRTY_STATE", repr(status))
        return "STAGED_APPROVAL_OVER_CANDIDATE", head, {
            path: subprocess.check_output(["git", "show", f":{path}"], cwd=ROOT)
            for path in APPROVAL_FILES
        }
    try:
        parent = git("rev-parse", "HEAD^")
    except subprocess.CalledProcessError:
        parent = ""
    if parent == CANDIDATE:
        if status:
            fail("A2_APPROVAL_ACCEPTED_DIRTY_STATE", repr(status))
        delta = set(git("diff", "--name-only", CANDIDATE, "HEAD").splitlines())
        if delta != expected:
            fail("A2_CANDIDATE_ACCEPTED_DIFF_MISMATCH", repr(delta))
        return "COMMITTED_ACCEPTED", head, {path: git_bytes(head, path) for path in APPROVAL_FILES}
    fail("A2_APPROVAL_LIFECYCLE_INVALID", head)


def validate_candidate() -> dict[str, int]:
    if git("rev-parse", f"{CANDIDATE}^") != GOVERNING:
        fail("A2_CANDIDATE_DIRECT_PARENT_MISMATCH")
    if git("rev-parse", f"{CANDIDATE}^{{tree}}") != CANDIDATE_TREE:
        fail("A2_CANDIDATE_TREE_MISMATCH")
    delta = set(git("diff", "--name-only", GOVERNING, CANDIDATE).splitlines())
    if delta != set(CANDIDATE_FILES):
        fail("A2_CANDIDATE_INVENTORY_MISMATCH", repr(delta))
    files = {path: git_bytes(CANDIDATE, path) for path in CANDIDATE_FILES}
    for path, expected in HASHES.items():
        if sha(files[path]) != expected:
            fail("A2_SIGNED_CANDIDATE_BLOB_MISMATCH", path)
    if aggregate(files, CANDIDATE_FILES) != GIT_AGGREGATE:
        fail("A2_CANDIDATE_GIT_AGGREGATE_MISMATCH")
    if aggregate(files, CANDIDATE_FILES[:2]) != GENERATED_AGGREGATE:
        fail("A2_CANDIDATE_GENERATED_AGGREGATE_MISMATCH")

    payload = json.loads(files[CANDIDATE_FILES[1]])
    if (
        payload.get("candidate_id") != "V23-P2D-VS001-IMPLEMENTATION-CONTRACT-EXECUTION-BOUNDARY-AMENDMENT-A2"
        or payload.get("status") != "CANDIDATE"
        or payload.get("approval") != "PENDING_HUMAN_APPROVAL"
    ):
        fail("A2_SIGNED_CANDIDATE_LIFECYCLE_MISMATCH")
    if payload.get("runtime_evidence_status") != "NOT_EXECUTED":
        fail("A2_FALSE_RUNTIME_EVIDENCE_CLAIM")
    if payload.get("implementation_authorized") is not False:
        fail("A2_PREMATURE_IMPLEMENTATION_AUTHORIZATION")

    artifacts = payload.get("evidence_file_catalog", [])
    categories: dict[str, int] = {}
    for row in artifacts:
        category = row.get("artifact_category")
        categories[category] = categories.get(category, 0) + 1
        if not any(
            row.get(key)
            for key in (
                "contained_mapping_lineage_record_ids",
                "contained_support_record_ids",
                "contained_support_revalidation_record_ids",
            )
        ):
            fail("A2_APPROVED_ARTIFACT_EMPTY_CONTAINMENT", row.get("path", ""))
    if len(artifacts) != 57 or categories != {
        "MAPPING_EVIDENCE_ARTIFACT": 13,
        "EXECUTION_SUPPORT_ARTIFACT": 44,
    }:
        fail("A2_APPROVED_ARTIFACT_ACCOUNTING_MISMATCH")

    mappings = payload.get("mapping_closure_catalog", [])
    lineage = payload.get("evidence_lineage_requirements", [])
    support = payload.get("support_record_catalog", [])
    support_revalidation = payload.get("support_revalidation_catalog", [])
    relations = payload.get("command_path_record_closure", [])
    if len(mappings) != 211 or len({row.get("mapping_id") for row in mappings}) != 211:
        fail("A2_APPROVED_MAPPING_CLOSURE_MISMATCH")
    provisional = [row for row in lineage if row.get("record_kind") == "PROVISIONAL_OBSERVATION"]
    final = [row for row in lineage if row.get("record_kind") == "FINAL_REVALIDATION"]
    if len(lineage) != 767 or len(provisional) != 556 or len(final) != 211:
        fail("A2_APPROVED_MAPPING_LINEAGE_MISMATCH")
    support_ids = {row.get("support_record_id") for row in support}
    revalidation_ids = {row.get("support_revalidation_record_id") for row in support_revalidation}
    if len(support) != len(support_ids) or len(support) != 163:
        fail("A2_APPROVED_SUPPORT_POPULATION_MISMATCH")
    if len(support_revalidation) != len(revalidation_ids) or len(support_revalidation) != 163:
        fail("A2_APPROVED_SUPPORT_REVALIDATION_POPULATION_MISMATCH")
    if support_ids & revalidation_ids:
        fail("A2_APPROVED_SUPPORT_IDENTITY_CONFLATION")
    for row in support:
        if row.get("direct_acceptance_evidence") is not False:
            fail("A2_APPROVED_SUPPORT_FALSE_ACCEPTANCE")
        if row.get("runtime_status") != "NOT_EXECUTED":
            fail("A2_APPROVED_SUPPORT_STORED_PASS")
        if row.get("b7_support_revalidation_record_id") not in revalidation_ids:
            fail("A2_APPROVED_SUPPORT_B7_ROUTE_MISSING")
    if len(relations) != 14 or any(row.get("executable_record_count", 0) <= 0 for row in relations):
        fail("A2_APPROVED_COMMAND_RECORD_CLOSURE_MISMATCH")
    if len(payload.get("package_script_bindings", [])) != 7 or len(payload.get("seven_batch_matrix", [])) != 7:
        fail("A2_APPROVED_PACKAGE_OR_BATCH_ACCOUNTING_MISMATCH")
    b7 = payload.get("b7_dual_revalidation_contract", {})
    if (
        b7.get("final_evidence_path") != "artifacts/vs001/b7/final-evidence.json"
        or b7.get("producer_command_id") != "vs001:evidence:validate"
        or b7.get("bootstrap_consumer_orchestrator_command_id") != "vs001:bootstrap:clean-checkout"
        or b7.get("final_mapping_closure_requires_complete_support_union") is not True
    ):
        fail("A2_APPROVED_B7_DUAL_UNION_MISMATCH")
    if "CMDREC-" in json.dumps(payload, sort_keys=True):
        fail("A2_APPROVED_UNFROZEN_SUPPORT_IDENTITY")
    return {
        "artifact_files": 57,
        "mapping_records": 767,
        "support_records": 163,
        "support_revalidations": 163,
        "relations": 14,
    }


def validate_approval(blobs: dict[str, bytes]) -> None:
    text = blobs[APPROVAL_FILES[0]].decode()
    required = [
        "Authorized approver: `Khoa, Nguyen`",
        "Approval date: `2026-07-19`",
        "Approval scope: `PHASE_2D_VS001_EXECUTION_BOUNDARY_AND_DUAL_LINEAGE_GOVERNANCE`",
        f"Candidate commit: `{CANDIDATE}`",
        f"Candidate direct parent: `{GOVERNING}`",
        f"Candidate tree: `{CANDIDATE_TREE}`",
        f"Git-content aggregate: `{GIT_AGGREGATE}`",
        f"Generated payload aggregate: `{GENERATED_AGGREGATE}`",
        "Total mapping-lineage records: `767/767`",
        "Total support-lineage records: `326`",
        "NOT_B1_IMPLEMENTATION_IN_APPROVAL_PERSISTENCE",
        "NOT_RUNTIME_EVIDENCE_EXECUTION_IN_APPROVAL_PERSISTENCE",
        "NOT_FINAL_VS001_ACCEPTANCE_BEFORE_B7_RUNTIME_REVALIDATION_AND_HUMAN_APPROVAL",
        "HUMAN_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2_APPROVAL",
    ]
    if not all(item in text for item in required):
        fail("A2_APPROVAL_IDENTITY_SCOPE_OR_NONCLAIM_MISMATCH")
    if "separate implementation turn may begin B1" not in text:
        fail("A2_B1_ENTRY_NOT_DETACHED")


def validate_boundaries(mode: str, accepted: str) -> None:
    if mode == "COMMITTED_ACCEPTED":
        delta = set(git("diff", "--name-only", CANDIDATE, accepted).splitlines())
        if delta != set(APPROVAL_FILES):
            fail("A2_APPROVAL_DIFF_NOT_EXACT_TWO_FILES", repr(delta))
        total = set(git("diff", "--name-only", GOVERNING, accepted).splitlines())
    else:
        total = set(git("diff", "--name-only", GOVERNING, CANDIDATE).splitlines())
        total |= set(git("diff", "--cached", "--name-only").splitlines())
    if total != set(CANDIDATE_FILES) | set(APPROVAL_FILES):
        fail("A2_ACCEPTED_TOTAL_INVENTORY_MISMATCH", repr(total))
    protected = (
        "apps/", "packages/", "database/", "configs/", "docs/BRD/", "docs/UXF/",
        "scripts/commissioning/", "runtime/", "infrastructure/", "factory/", "knowledge/",
        "tools/ysf/", "integrations/", "YADF/", "deployment/", "pnpm-lock.yaml", "package.json",
    )
    if any(path == prefix or path.startswith(prefix) for path in total for prefix in protected):
        fail("A2_IMPLEMENTATION_OR_PROTECTED_PATH_CHANGE")


def main() -> int:
    try:
        mode, accepted, blobs = lifecycle()
        counts = validate_candidate()
        validate_approval(blobs)
        validate_boundaries(mode, accepted)
        result = {
            "result": "VALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2",
            "lifecycle_mode": mode,
            "candidate_commit": CANDIDATE,
            "accepted_commit": accepted if mode == "COMMITTED_ACCEPTED" else None,
            "candidate_tree": CANDIDATE_TREE,
            "approval_files": 2,
            "implementation_in_persistence": 0,
            "runtime_evidence_executed": 0,
            **counts,
        }
        print(json.dumps(result, sort_keys=True))
        print("VALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2")
        return 0
    except (ApprovalError, KeyError, TypeError, ValueError, UnicodeDecodeError, subprocess.CalledProcessError) as error:
        print(
            "INVALID_APPROVED_PHASE_2D_VS001_IMPLEMENTATION_CONTRACT_EXECUTION_BOUNDARY_AMENDMENT_A2",
            error,
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
