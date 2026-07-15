#!/usr/bin/env python3
"""Validate detached approval for V23-P2B-CRITICALITY-DECISION-C1."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PHASE2 = ROOT / "docs/baselines/v2.3/phase-2"
PACK_PATH = PHASE2 / "PHASE_2_CRITICALITY_EXCEPTION_REVIEW_PACK.md"
DATA_PATH = PHASE2 / "phase-2-criticality-exception-review.json"
CANDIDATE_VALIDATOR = ROOT / "scripts/docs/validate-phase-2-criticality-review.py"
APPROVAL_PATH = PHASE2 / "PHASE_2_CRITICALITY_DECISION_APPROVAL.md"
APPROVAL_VALIDATOR = ROOT / "scripts/docs/validate-phase-2-criticality-decision-approval.py"
EXCEPTION_REGISTER = PHASE2 / "PHASE_2_CRITICALITY_EXCEPTION_REGISTER.md"

REGISTRY_VALIDATOR = ROOT / "scripts/docs/validate-requirement-registry.py"
REGISTRY_APPROVAL_VALIDATOR = ROOT / "scripts/docs/validate-requirement-registry-approval.py"
PREFLIGHT_VALIDATOR = ROOT / "scripts/docs/validate-phase-2-preflight.py"
DECISION_PACK_APPROVAL_VALIDATOR = ROOT / "scripts/docs/validate-phase-2-decision-pack-approval.py"

CANDIDATE_ID = "V23-P2B-CRITICALITY-DECISION-C1"
CANDIDATE_COMMIT = "05250440b6f40bfbf2426a6b6fc9a69bd489ca82"
SOURCE_REVIEW = "V23-P2B-CRITICALITY-REVIEW-R2"
SOURCE_DECISION_PACK = "V23-P2A-DECISION-PACK-C1"
SOURCE_COMMIT = "1a74dd7486945d3820e1d7c735f3b37cd9e418a7"
PACK_SHA256 = "734bc57679ce5f535a88b38130c76ec6370d103a37a89346d90e112c270e307b"
DATA_SHA256 = "c9e8128f76a51620db4381be8c3c9887f4bff28c97d97ea68b30c76af776393c"
VALIDATOR_SHA256 = "bf0de65fe921033a4e04afb7f314ef8e2e44334a4cba6297c1bdeaad527a179e"
PROJECTION_QUALIFIER = "PROVISIONAL_EXCLUDES_PENDING_SOURCE_REMEDIATION_AND_CHILD_RECONCILIATION"

APPROVAL_PATHS = {
    "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_DECISION_APPROVAL.md",
    "scripts/docs/validate-phase-2-criticality-decision-approval.py",
}
ALLOWED_PHASE_2B_PATHS = APPROVAL_PATHS | {
    "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_EXCEPTION_REVIEW_PACK.md",
    "docs/baselines/v2.3/phase-2/phase-2-criticality-exception-review.json",
    "scripts/docs/validate-phase-2-criticality-review.py",
}


def run(command: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


def relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def command_text(command: list[str]) -> str:
    result = run(command)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace"))
    return result.stdout.decode("utf-8")


def index_blob(path: Path) -> bytes:
    result = run(["git", "show", ":" + relative(path)])
    if result.returncode != 0:
        raise RuntimeError("missing Git-index blob: " + relative(path))
    return result.stdout


def commit_blob(commit: str, path: Path) -> bytes:
    result = run(["git", "show", commit + ":" + relative(path)])
    if result.returncode != 0:
        raise RuntimeError("missing committed blob: " + commit + ":" + relative(path))
    return result.stdout


def validate_required_validator(path: Path, marker: bytes, errors: list[str]) -> None:
    result = run([sys.executable, "-B", str(path)])
    if result.returncode != 0 or marker not in result.stdout.splitlines():
        errors.append(path.name + " did not return required success")


def main() -> int:
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    try:
        blobs = {
            "pack": index_blob(PACK_PATH),
            "data": index_blob(DATA_PATH),
            "validator": index_blob(CANDIDATE_VALIDATOR),
            "approval": index_blob(APPROVAL_PATH),
            "approval_validator": index_blob(APPROVAL_VALIDATOR),
            "exceptions": index_blob(EXCEPTION_REGISTER),
        }
        committed_payloads = {
            "pack": commit_blob(CANDIDATE_COMMIT, PACK_PATH),
            "data": commit_blob(CANDIDATE_COMMIT, DATA_PATH),
            "validator": commit_blob(CANDIDATE_COMMIT, CANDIDATE_VALIDATOR),
        }
    except RuntimeError as exc:
        errors.append(str(exc))
        blobs = {}
        committed_payloads = {}

    expected_hashes = {
        "pack": PACK_SHA256,
        "data": DATA_SHA256,
        "validator": VALIDATOR_SHA256,
    }
    for name, expected_hash in expected_hashes.items():
        if name in blobs:
            check(hashlib.sha256(blobs[name]).hexdigest() == expected_hash, name + " Git-index SHA-256 differs")
        if name in committed_payloads:
            check(hashlib.sha256(committed_payloads[name]).hexdigest() == expected_hash, name + " candidate-commit SHA-256 differs")
            check(blobs.get(name) == committed_payloads[name], name + " Git-index content differs from candidate commit")

    data: dict = {}
    if "data" in blobs:
        try:
            data = json.loads(blobs["data"].decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append("Decision Data is not valid UTF-8 JSON: " + str(exc))
    expected_identity = {
        "candidate_id": CANDIDATE_ID,
        "status": "CANDIDATE",
        "approval_status": "PENDING_MARKDOWN_APPROVAL",
        "source_review": SOURCE_REVIEW,
        "source_decision_pack": SOURCE_DECISION_PACK,
        "source_commit": SOURCE_COMMIT,
        "dispositioned_exception_count": 46,
        "undispositioned_exception_count": 0,
    }
    check({key: data.get(key) for key in expected_identity} == expected_identity, "embedded candidate identity/state differs")
    check(data.get("decision_accounting", {}).get("dispositioned_exceptions") == 46, "embedded disposition count differs")
    check(data.get("decision_accounting", {}).get("undispositioned_exceptions") == 0, "embedded undispositioned count differs")
    check(data.get("projection_qualifier") == PROJECTION_QUALIFIER, "embedded projection limitation differs")
    check(data.get("provisional_decision_adjusted_projection", {}).get("final_atomic_denominator") is None, "embedded candidate claims a final atomic denominator")
    check(data.get("provisional_decision_adjusted_projection", {}).get("final_tier_distribution_claimed") is False, "embedded candidate claims a final tier distribution")
    check(all(value == "PENDING" for value in data.get("candidate_approval_block", {}).values()), "embedded candidate approval block is not entirely pending")

    approval_text = blobs.get("approval", b"").decode("utf-8", errors="replace")
    approval_lines = approval_text.splitlines()
    exact_lines = [
        "- Candidate ID: `V23-P2B-CRITICALITY-DECISION-C1`",
        "- Candidate commit: `05250440b6f40bfbf2426a6b6fc9a69bd489ca82`",
        "- Approval model: `DETACHED_MARKDOWN_APPROVAL`",
        "- Decision: `APPROVED`",
        "- Approval status: `APPROVED`",
        "- Authorized Approver: `Khoa, Nguyen`",
        "- Signature: `Khoa, Nguyen`",
        "- Date: `2026-07-15`",
        "- Timezone: `Asia/Ho_Chi_Minh`",
        "- Approval revision: `2`",
        "- Approval scope: `CRITICALITY_DISPOSITIONS_AND_REMEDIATION_CONTRACTS`",
        "- Projection status: `PROVISIONAL_EXCLUDES_PENDING_SOURCE_REMEDIATION_AND_CHILD_RECONCILIATION`",
        "- Source review: `V23-P2B-CRITICALITY-REVIEW-R2`",
        "- Source decision pack: `V23-P2A-DECISION-PACK-C1`",
        "- Source commit: `1a74dd7486945d3820e1d7c735f3b37cd9e418a7`",
        "- Hash basis: `GIT_INDEX_BLOB_CONTENT`",
        "- Line endings: `GIT_CANONICAL_TEXT`",
        "- Decision Pack SHA-256: `734bc57679ce5f535a88b38130c76ec6370d103a37a89346d90e112c270e307b`",
        "- Decision Data SHA-256: `c9e8128f76a51620db4381be8c3c9887f4bff28c97d97ea68b30c76af776393c`",
        "- Corrected Validator SHA-256: `bf0de65fe921033a4e04afb7f314ef8e2e44334a4cba6297c1bdeaad527a179e`",
        "- Effective result: `APPROVED_PHASE_2_CRITICALITY_DECISION_PACK`",
    ]
    for line in exact_lines:
        check(approval_lines.count(line) == 1, "detached approval line missing, duplicated, or altered: " + line)
    for non_claim in (
        "NOT_SOURCE_REMEDIATION",
        "NOT_FINAL_ATOMIC_COUNT_APPROVAL",
        "NOT_FINAL_TIER_DISTRIBUTION_APPROVAL",
        "NOT_BRD_UXF_FREEZE",
        "NOT_IMPLEMENTATION_AUTHORIZATION",
    ):
        check(approval_lines.count("- `" + non_claim + "`") == 1, "detached approval non-claim missing or duplicated: " + non_claim)

    exception_text = blobs.get("exceptions", b"").decode("utf-8", errors="replace")
    exception_rows = [line for line in exception_text.splitlines() if line.startswith("| P2-CRIT-EXC-")]
    check(len(exception_rows) == 46, "source exception row count differs")
    check(all(line.endswith("| `OPEN` |") for line in exception_rows), "one or more source exceptions are no longer OPEN")

    check(run(["git", "cat-file", "-e", SOURCE_COMMIT + "^{commit}"]).returncode == 0, "source commit does not exist")
    check(run(["git", "cat-file", "-e", CANDIDATE_COMMIT + "^{commit}"]).returncode == 0, "candidate commit does not exist")
    check(command_text(["git", "rev-parse", CANDIDATE_COMMIT + "^"]).strip() == SOURCE_COMMIT, "candidate parent differs from source commit")
    check(run(["git", "merge-base", "--is-ancestor", CANDIDATE_COMMIT, "HEAD"]).returncode == 0, "candidate commit is not an ancestor of current HEAD")
    check(run(["git", "cat-file", "-e", CANDIDATE_COMMIT + ":" + relative(APPROVAL_PATH)]).returncode != 0, "approval Markdown exists in candidate commit")
    check(run(["git", "cat-file", "-e", CANDIDATE_COMMIT + ":" + relative(APPROVAL_VALIDATOR)]).returncode != 0, "approval validator exists in candidate commit")

    committed_since_candidate = set(filter(None, command_text([
        "git", "diff", "--name-only", CANDIDATE_COMMIT + "..HEAD",
    ]).splitlines()))
    staged_paths = set(filter(None, command_text(["git", "diff", "--cached", "--name-only"]).splitlines()))
    check(committed_since_candidate | staged_paths == APPROVAL_PATHS, "candidate-to-target approval-layer paths differ")
    committed_since_source = set(filter(None, command_text([
        "git", "diff", "--name-only", SOURCE_COMMIT + "..HEAD",
    ]).splitlines()))
    check(committed_since_source | staged_paths == ALLOWED_PHASE_2B_PATHS, "unauthorized or missing path since source commit")
    check(run(["git", "diff", "--quiet"]).returncode == 0, "tracked working tree differs from Git index")

    prior_validators = [
        (REGISTRY_VALIDATOR, b"Requirement registry validation VALID_READY_TO_FREEZE"),
        (REGISTRY_APPROVAL_VALIDATOR, b"PASS \xe2\x80\x94 VALID_APPROVED_RECONCILED_REGISTRY_BASELINE"),
        (PREFLIGHT_VALIDATOR, b"PASS \xe2\x80\x94 PHASE_2_DECISION_PACK_READY_FOR_HUMAN_APPROVAL"),
        (DECISION_PACK_APPROVAL_VALIDATOR, b"PASS \xe2\x80\x94 VALID_APPROVED_PHASE_2_HUMAN_DECISION_PACK"),
        (CANDIDATE_VALIDATOR, b"PASS \xe2\x80\x94 PHASE_2_CRITICALITY_REVIEW_READY"),
    ]
    for validator, marker in prior_validators:
        validate_required_validator(validator, marker, errors)

    if errors:
        print("FAIL — INVALID_PHASE_2_CRITICALITY_DECISION_PACK_APPROVAL", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        return 1
    print("PASS — VALID_APPROVED_PHASE_2_CRITICALITY_DECISION_PACK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
