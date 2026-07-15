#!/usr/bin/env python3
"""Validate the detached approval for the Phase 2C acceptance model."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = "0df2d424e00f9cd27b8dcb6645eef827ce97b60e"
CANDIDATE = "e63213f932528452801f4f776e40b4c5dfc0c2fa"
CANDIDATE_ID = "V23-P2C-ACCEPTANCE-MODEL-C1"
APPROVAL_MD = "docs/baselines/v2.3/phase-2/PHASE_2_ACCEPTANCE_MODEL_APPROVAL.md"
APPROVAL_VALIDATOR = "scripts/docs/validate-phase-2-acceptance-model-approval.py"
APPROVAL_PATHS = {APPROVAL_MD, APPROVAL_VALIDATOR}
SIGNED = {
    "docs/baselines/v2.3/phase-2/acceptance-profile-catalog.json": "0ffc968ea54d40293dc4d7e8fa07b0dcd4e6f37893471c2091b89fd422c6ce0c",
    "docs/baselines/v2.3/phase-2/acceptance-mapping-dry-run.json": "70286130036369db925433d723e43e819a0eaf6bac0e3723cb288080dce2b882",
    "docs/baselines/v2.3/phase-2/ACCEPTANCE_MAPPING_REVIEW_PACK.md": "ca81d7a0dd8a085141f7cc7657ab0a64ad73fc34607ad267bd061142ecaf96c2",
    "docs/baselines/v2.3/phase-2/acceptance-model-candidate-manifest.json": "001cee4e3ddefd440efc4d8f027c59744c0139f45a4f1f6d9976c6c8a283116e",
}
GENERATED_AGGREGATE = "6ff7a50dbfa376f65e820e6844360519dd678c030d56d94df12209f486d423d9"
MODEL_AGGREGATE = "de1a878da589d78c9d857c2f4d62e81b5f4624aaf02eca9233c61c1e3da244fc"
PROTECTED_PATHS = (
    "docs/baselines/v2.3/requirements",
    "docs/baselines/v2.3/phase-2/stable-id-mapping-candidate.json",
    "docs/baselines/v2.3/REQUIREMENT_REGISTRY_FREEZE_APPROVAL.md",
    "docs/baselines/v2.3/REQUIREMENT_REGISTRY_FREEZE_CANDIDATE.md",
    "docs/baselines/v2.3/phase-2/PHASE_2_DECISION_REGISTER.md",
    "docs/baselines/v2.3/phase-2/PHASE_2_HUMAN_DECISION_PACK.md",
    "docs/baselines/v2.3/phase-2/PHASE_2_HUMAN_DECISION_PACK_APPROVAL.md",
    "docs/baselines/v2.3/phase-2/phase-2-human-decisions.json",
    "docs/baselines/v2.3/phase-2/PHASE_2_PREFLIGHT_REPORT.md",
    "docs/baselines/v2.3/phase-2/phase-2-preflight-summary.json",
    "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_EXCEPTION_REGISTER.md",
    "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_EXCEPTION_REVIEW_PACK.md",
    "docs/baselines/v2.3/phase-2/phase-2-criticality-exception-review.json",
    "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_DECISION_APPROVAL.md",
    "scripts/docs/validate-phase-2-criticality-review.py",
    "scripts/docs/validate-phase-2-criticality-decision-approval.py",
)
NON_CLAIMS = (
    "NOT_APPROVAL_OF_871_HUMAN_MAPPING_REVIEW_RECORDS",
    "NOT_ACCEPTANCE_OF_C1_C2_GENERATED_ACCEPTANCE_CONTRACTS",
    "NOT_FINAL_BRD_UXF_DOCUMENT_BASELINE_APPROVAL",
    "NOT_FINAL_ACCEPTANCE_MAPPING_APPROVAL",
    "NOT_YADF_IMPLEMENTATION_AUTHORIZATION",
)


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def git(*args: str, binary: bool = False) -> bytes | str:
    result = subprocess.run(["git", *args], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    require(result.returncode == 0, f"git {' '.join(args)} failed: {result.stderr.decode(errors='replace')}")
    return result.stdout if binary else result.stdout.decode().strip()


def commit_blob(commit: str, path: str) -> bytes:
    return git("show", f"{commit}:{path}", binary=True)  # type: ignore[return-value]


def approval_blob(head: str) -> bytes:
    if head == CANDIDATE:
        return git("show", f":{APPROVAL_MD}", binary=True)  # type: ignore[return-value]
    return commit_blob(head, APPROVAL_MD)


def aggregate(paths: list[str], commit: str) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths):
        digest.update(path.encode())
        digest.update(b"\0")
        digest.update(commit_blob(commit, path))
        digest.update(b"\0")
    return digest.hexdigest()


def validate_history(head: str) -> None:
    git("cat-file", "-e", f"{BASE}^{{commit}}")
    git("cat-file", "-e", f"{CANDIDATE}^{{commit}}")
    require(subprocess.run(["git", "merge-base", "--is-ancestor", BASE, CANDIDATE], cwd=ROOT).returncode == 0, "historical accepted commit is not candidate ancestor")
    require(git("rev-parse", f"{CANDIDATE}^") == BASE, "candidate parent mismatch")
    changed = git("diff", "--name-only", BASE, CANDIDATE, "--", *PROTECTED_PATHS)
    require(changed == "", f"protected governance artifacts changed: {changed}")
    if head != CANDIDATE:
        require(git("rev-parse", f"{head}^") == CANDIDATE, "accepted commit parent is not candidate")
        diff = set(filter(None, git("diff", "--name-only", CANDIDATE, head).splitlines()))
        require(diff == APPROVAL_PATHS, f"candidate..accepted diff is not exactly approval layer: {sorted(diff)}")
    else:
        staged = set(filter(None, git("diff", "--cached", "--name-only").splitlines()))
        require(staged == APPROVAL_PATHS, f"staged approval layer mismatch: {sorted(staged)}")


def validate_signed_candidate() -> None:
    for path, expected in SIGNED.items():
        require(hashlib.sha256(commit_blob(CANDIDATE, path)).hexdigest() == expected, f"signed hash mismatch: {path}")
    manifest = json.loads(commit_blob(CANDIDATE, "docs/baselines/v2.3/phase-2/acceptance-model-candidate-manifest.json"))
    require(manifest["candidate_id"] == CANDIDATE_ID, "candidate identity mismatch")
    require(manifest["status"] == "CANDIDATE" and manifest["approval_status"] == "PENDING_HUMAN_APPROVAL", "embedded candidate must remain pending")
    generated_paths = sorted(manifest["generated_file_sha256"])
    require(aggregate(generated_paths, CANDIDATE) == GENERATED_AGGREGATE, "generated payload aggregate mismatch")
    model_paths = sorted(set(manifest["generated_file_sha256"]) | set(manifest["tool_sha256"]) | {"docs/baselines/v2.3/phase-2/acceptance-model-candidate-manifest.json"})
    require(aggregate(model_paths, CANDIDATE) == MODEL_AGGREGATE, "staged model aggregate mismatch")
    mapping = json.loads(commit_blob(CANDIDATE, "docs/baselines/v2.3/phase-2/acceptance-mapping-dry-run.json"))
    require(mapping["summary"]["disposition_counts"]["HUMAN_MAPPING_REVIEW"] == 871, "unapproved mapping count mismatch")
    require(mapping["summary"]["disposition_counts"]["INVALID_OR_BLOCKED"] == 0, "candidate contains invalid/blocked mappings")


def validate_approval(text: str) -> None:
    required = (
        CANDIDATE_ID, CANDIDATE, "APPROVED", "Khoa, Nguyen", "2026-07-15", "Asia/Ho_Chi_Minh",
        "ACCEPTANCE_CONTRACT_MODEL_PROFILE_CATALOG_AND_MAPPING_CLASSIFICATION_ONLY",
        "HYBRID_ACCEPTANCE_PROFILES_AND_INLINE_CONTRACTS", "1.0.0", BASE,
        "HISTORICAL_ACCEPTED_BASELINE_VALIDATION", "VALID_PHASE_2C_BASELINE_TRANSITION",
        "BATCH_SEMANTIC_RECONCILIATION_OF_HUMAN_MAPPING_REVIEW",
        GENERATED_AGGREGATE, MODEL_AGGREGATE, *SIGNED.values(), *NON_CLAIMS,
    )
    for value in required:
        require(value in text, f"approval field/non-claim missing: {value}")
    require(text.count("Authorized Approver: `Khoa, Nguyen`") == 1, "authorized approver mismatch")
    require(text.count("Signature: `Khoa, Nguyen`") == 1, "signature mismatch")
    require("does not mark the Phase 2C document baseline accepted" in text, "final document-baseline non-claim missing")


def run_current_validators() -> None:
    for script, expected in (
        ("scripts/docs/validate-acceptance-profile-catalog.py", "PASS — VALID_ACCEPTANCE_PROFILE_CATALOG_CANDIDATE"),
        ("scripts/docs/validate-acceptance-mapping-dry-run.py", "PASS — VALID_ACCEPTANCE_MAPPING_DRY_RUN_CANDIDATE"),
    ):
        result = subprocess.run([sys.executable, script], cwd=ROOT, text=True, capture_output=True, check=False)
        require(result.returncode == 0 and result.stdout.strip() == expected, f"current validator failed: {script}: {result.stdout}{result.stderr}")


def main() -> int:
    try:
        head = git("rev-parse", "HEAD")
        validate_history(head)
        validate_signed_candidate()
        validate_approval(approval_blob(head).decode())
        run_current_validators()
    except (ValidationError, KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL — {error}", file=sys.stderr)
        return 1
    print("VALID_APPROVED_PHASE_2C_ACCEPTANCE_MODEL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
