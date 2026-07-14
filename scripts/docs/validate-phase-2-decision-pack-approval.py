#!/usr/bin/env python3
"""Validate the detached approval for V23-P2A-DECISION-PACK-C1."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACK_PATH = ROOT / "docs/baselines/v2.3/phase-2/PHASE_2_HUMAN_DECISION_PACK.md"
DATA_PATH = ROOT / "docs/baselines/v2.3/phase-2/phase-2-human-decisions.json"
APPROVAL_PATH = ROOT / "docs/baselines/v2.3/phase-2/PHASE_2_HUMAN_DECISION_PACK_APPROVAL.md"
EXCEPTION_PATH = ROOT / "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_EXCEPTION_REGISTER.md"
REGISTRY_VALIDATOR = ROOT / "scripts/docs/validate-requirement-registry.py"
REGISTRY_APPROVAL_VALIDATOR = ROOT / "scripts/docs/validate-requirement-registry-approval.py"
PHASE2_PREFLIGHT_VALIDATOR = ROOT / "scripts/docs/validate-phase-2-preflight.py"

CANDIDATE_ID = "V23-P2A-DECISION-PACK-C1"
SOURCE_REGISTRY_CANDIDATE_ID = "V23-REQ-REGISTRY-FC2"
SOURCE_COMMIT = "8c2e41f89443048a5b8568b308c32129634d7241"
SOURCE_DOCUMENT_COMMIT = "7f16d4c4b8ab514bd45de184f65ace221b03f4db"
PACK_SHA256 = "76be9ff85f50e60d9f466763a73b939a5482c914dd7f42b5b261c27b691453fb"
DATA_SHA256 = "0240802b4cdd1bdc483d5f73c6a8187b8ac037395bba1cf094fa0f98359d7671"
EXPECTED_DECISION_IDS = ["P2-DEC-{:03d}".format(index) for index in range(1, 11)]
EXPECTED_PENDING_APPROVAL = {
    "status": "PENDING",
    "authorized_approver": "PENDING",
    "decision": "PENDING",
    "date": "PENDING",
    "signature": "PENDING",
}


def run(command: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


def relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def index_blob(path: Path) -> bytes:
    result = run(["git", "show", ":" + relative(path)])
    if result.returncode != 0:
        raise RuntimeError("missing staged Git blob: " + relative(path))
    return result.stdout


def validate_required_validator(path: Path, success_marker: bytes, errors: list[str]) -> None:
    result = run([sys.executable, str(path)])
    if result.returncode != 0 or success_marker not in result.stdout.splitlines():
        errors.append(path.name + " did not return required success")


def main() -> int:
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    blobs: dict[str, bytes] = {}
    for name, path in (
        ("pack", PACK_PATH),
        ("data", DATA_PATH),
        ("approval", APPROVAL_PATH),
        ("exceptions", EXCEPTION_PATH),
    ):
        if not path.is_file():
            errors.append("missing required file: " + relative(path))
            continue
        try:
            blobs[name] = index_blob(path)
        except RuntimeError as exc:
            errors.append(str(exc))

    if "pack" in blobs:
        check(hashlib.sha256(blobs["pack"]).hexdigest() == PACK_SHA256, "Decision Pack staged SHA-256 differs")
    if "data" in blobs:
        check(hashlib.sha256(blobs["data"]).hexdigest() == DATA_SHA256, "Decision Data staged SHA-256 differs")

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
        "decision_count": 10,
        "open_decision_count": 0,
        "decided_pending_pack_approval_count": 10,
        "next_gate": "HUMAN_DECISION_PACK_APPROVAL",
        "source_registry_candidate_id": SOURCE_REGISTRY_CANDIDATE_ID,
        "source_git_commit": SOURCE_COMMIT,
        "hash_basis": "GIT_INDEX_BLOB_CONTENT",
        "line_endings": "GIT_CANONICAL_TEXT",
    }
    check({key: data.get(key) for key in expected_identity} == expected_identity, "signed Decision Data candidate identity/state differs")
    check(data.get("approval") == EXPECTED_PENDING_APPROVAL, "signed Decision Data approval block is not entirely pending")
    binding = data.get("baseline_binding", {})
    check(binding.get("source_registry_candidate_id") == SOURCE_REGISTRY_CANDIDATE_ID, "signed Decision Data FC2 identity differs")
    check(binding.get("accepted_registry_commit") == SOURCE_COMMIT, "signed Decision Data source commit differs")
    check(binding.get("source_document_commit") == SOURCE_DOCUMENT_COMMIT, "signed Decision Data source-document commit differs")
    check(binding.get("source_hash_basis") == "GIT_BLOB_CONTENT_AT_SOURCE_COMMIT", "signed Decision Data FC2 source hash basis differs")

    decisions = data.get("decisions", [])
    decision_ids = [item.get("decision_id") for item in decisions if isinstance(item, dict)]
    check(decision_ids == EXPECTED_DECISION_IDS, "signed decisions are missing, duplicated, aliased, or out of order")
    check(len(set(decision_ids)) == 10, "signed decision IDs are duplicated")
    check(len(decisions) == data.get("decision_count") == 10, "signed top-level decision_count differs")
    check(sum(item.get("status") == "OPEN" for item in decisions) == data.get("open_decision_count") == 0, "a signed decision remains OPEN or open count differs")
    check(sum(item.get("status") == "DECIDED_PENDING_PACK_APPROVAL" for item in decisions) == data.get("decided_pending_pack_approval_count") == 10, "signed decided-pending count differs")
    for item in decisions:
        if not isinstance(item, dict):
            errors.append("signed decision record is not an object")
            continue
        check(item.get("selected_option") == 1, str(item.get("decision_id")) + " selected option differs")
        check(item.get("status") == "DECIDED_PENDING_PACK_APPROVAL", str(item.get("decision_id")) + " immutable status differs")

    pack_text = blobs.get("pack", b"").decode("utf-8", errors="replace")
    pack_lines = pack_text.splitlines()
    markdown_identity = {
        "candidate_id": CANDIDATE_ID,
        "status": "CANDIDATE",
        "approval_status": "PENDING_MARKDOWN_APPROVAL",
        "decision_count": 10,
        "open_decision_count": 0,
        "decided_pending_pack_approval_count": 10,
        "next_gate": "HUMAN_DECISION_PACK_APPROVAL",
        "source_registry_candidate_id": SOURCE_REGISTRY_CANDIDATE_ID,
        "source_git_commit": SOURCE_COMMIT,
        "hash_basis": "GIT_INDEX_BLOB_CONTENT",
        "line_endings": "GIT_CANONICAL_TEXT",
    }
    for key, value in markdown_identity.items():
        line = "- {}: `{}`".format(key, value)
        check(pack_lines.count(line) == 1, "signed Decision Pack identity line missing or duplicated: " + line)
    check(pack_lines.count("- Selected option: `1`.") == 10, "signed Decision Pack option-1 count differs")
    check(pack_lines.count("- Status: `DECIDED_PENDING_PACK_APPROVAL`.") == 10, "signed Decision Pack immutable decision status count differs")
    check(pack_text.count("## P2-DEC-") == 10, "signed Decision Pack decision-heading count differs")
    pack_candidate_tokens = set(re.findall(r"V23-P2A-DECISION-PACK-C[0-9]+", pack_text))
    check(pack_candidate_tokens == {CANDIDATE_ID}, "signed Decision Pack contains an alias candidate identity")
    check(not any(key in data for key in ("candidate_alias", "candidate_aliases", "alias_candidate_id", "alias_of_candidate")), "signed Decision Data contains an alias candidate identity")
    expected_pack_tail = """## Human Approval

- Status: PENDING
- Authorized Approver: PENDING
- Decision: PENDING
- Date: PENDING
- Signature: PENDING"""
    check(pack_text.rstrip().endswith(expected_pack_tail), "signed Decision Pack embedded approval is not entirely pending")

    approval_text = blobs.get("approval", b"").decode("utf-8", errors="replace")
    approval_lines = approval_text.splitlines()
    exact_approval_lines = [
        "- Candidate ID: `V23-P2A-DECISION-PACK-C1`",
        "- Approval model: `DETACHED_MARKDOWN_APPROVAL`",
        "- Decision: `APPROVED`",
        "- Approval status: `APPROVED`",
        "- Authorized Approver: `Khoa, Nguyen`",
        "- Signature: `Khoa, Nguyen`",
        "- Date: `2026-07-14`",
        "- Timezone: `Asia/Ho_Chi_Minh`",
        "- Approval revision: `1`",
        "- Source registry candidate: `V23-REQ-REGISTRY-FC2`",
        "- Source commit: `8c2e41f89443048a5b8568b308c32129634d7241`",
        "- Hash basis: `GIT_INDEX_BLOB_CONTENT`",
        "- Line endings: `GIT_CANONICAL_TEXT`",
        "- Decision Pack SHA-256: `76be9ff85f50e60d9f466763a73b939a5482c914dd7f42b5b261c27b691453fb`",
        "- Decision Data SHA-256: `0240802b4cdd1bdc483d5f73c6a8187b8ac037395bba1cf094fa0f98359d7671`",
        "- Effective result: `APPROVED_PHASE_2_HUMAN_DECISION_PACK`",
    ]
    for line in exact_approval_lines:
        check(approval_lines.count(line) == 1, "detached approval line missing, duplicated, or altered: " + line)
    for non_claim in (
        "NOT_CRITICALITY_EXCEPTION_APPROVAL",
        "NOT_BRD_UXF_REMEDIATION_APPROVAL",
        "NOT_FINAL_DOCUMENT_BASELINE_APPROVAL",
        "NOT_ARCHITECTURE_OR_IMPLEMENTATION_APPROVAL",
    ):
        check(approval_lines.count("- `" + non_claim + "`") == 1, "detached approval non-claim missing or duplicated: " + non_claim)
    check("approves all ten decisions `P2-DEC-001` through" in approval_text, "detached approval scope start is missing")
    check("`P2-DEC-010` exactly as contained in the two signed payloads" in approval_text, "detached approval scope end is missing")
    approval_candidate_tokens = set(re.findall(r"V23-P2A-DECISION-PACK-C[0-9]+", approval_text))
    check(approval_candidate_tokens == {CANDIDATE_ID}, "detached approval contains an alias candidate identity")

    exception_text = blobs.get("exceptions", b"").decode("utf-8", errors="replace")
    exception_rows = [line for line in exception_text.splitlines() if line.startswith("| P2-CRIT-EXC-")]
    check(len(exception_rows) == 46, "criticality exception row count differs")
    check(all(line.endswith("| `OPEN` |") for line in exception_rows), "one or more criticality exceptions are no longer OPEN")

    validate_required_validator(REGISTRY_VALIDATOR, b"Requirement registry validation VALID_READY_TO_FREEZE", errors)
    validate_required_validator(REGISTRY_APPROVAL_VALIDATOR, b"PASS \xe2\x80\x94 VALID_APPROVED_RECONCILED_REGISTRY_BASELINE", errors)
    validate_required_validator(PHASE2_PREFLIGHT_VALIDATOR, b"PASS \xe2\x80\x94 PHASE_2_DECISION_PACK_READY_FOR_HUMAN_APPROVAL", errors)

    check(run(["git", "diff", "--quiet", "HEAD", "--", "docs/BRD", "docs/UXF"]).returncode == 0, "BRD/UXF differ from HEAD")
    check(run(["git", "diff", "--quiet", SOURCE_DOCUMENT_COMMIT, "HEAD", "--", "docs/BRD", "docs/UXF"]).returncode == 0, "HEAD BRD/UXF differ from source baseline")
    check(run(["git", "diff", "--quiet", "--", relative(PACK_PATH), relative(DATA_PATH), relative(APPROVAL_PATH), relative(Path(__file__))]).returncode == 0, "approval-layer working files differ from staged Git content")

    if errors:
        print("FAIL \u2014 INVALID_PHASE_2_HUMAN_DECISION_PACK_APPROVAL", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        return 1

    print("PASS \u2014 VALID_APPROVED_PHASE_2_HUMAN_DECISION_PACK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
