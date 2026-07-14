#!/usr/bin/env python3
"""Validate the detached approval state for V23-REQ-REGISTRY-FC2."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "docs/baselines/v2.3/requirements/registry-freeze-manifest.json"
CANDIDATE_PATH = ROOT / "docs/baselines/v2.3/REQUIREMENT_REGISTRY_FREEZE_CANDIDATE.md"
APPROVAL_PATH = ROOT / "docs/baselines/v2.3/REQUIREMENT_REGISTRY_FREEZE_APPROVAL.md"
REGISTRY_VALIDATOR_PATH = ROOT / "scripts/docs/validate-requirement-registry.py"

EXPECTED_MANIFEST = {
    "schema_version": "1.1",
    "candidate_id": "V23-REQ-REGISTRY-FC2",
    "supersedes_candidate_id": "V23-REQ-REGISTRY-FC1",
    "baseline_kind": "RECONCILED_REQUIREMENT_REGISTRY",
    "status": "CANDIDATE",
    "approval_status": "PENDING_HUMAN_APPROVAL",
    "source_git_commit": "7f16d4c4b8ab514bd45de184f65ace221b03f4db",
    "source_hash_basis": "GIT_BLOB_CONTENT_AT_SOURCE_COMMIT",
    "line_ending_semantics": "GIT_CANONICAL_TEXT",
    "source_aggregate_hash": "34685bed33422505763d31ef8f86837a1139fd5aaf2946a9adcbfa9dd1cd9a35",
    "registry_aggregate_hash": "832cc96192c72b89472964e030893ac4c01bcc0d20eb21f7e935b7a7c6288658",
    "ready_to_freeze": True,
}
EXPECTED_CORRECTION = {
    "category": "SOURCE_HASH_BASIS_REPAIR",
    "fc1_failure": "CLEAN_CHECKOUT_SOURCE_HASH_MISMATCH",
    "root_cause": "RAW_WORKING_TREE_CRLF_VS_CANONICAL_GIT_BLOB_LF",
    "affected_source_document_count": 28,
    "semantic_payload_changed": False,
}
EXPECTED_PENDING_APPROVAL = {
    "status": "PENDING",
    "authorized_approver": "PENDING",
    "decision": "PENDING",
    "date": "PENDING",
    "signature": "PENDING",
}
EXPECTED_SIGNED_FILE_HASHES = {
    "docs/baselines/v2.3/requirements/registry-freeze-manifest.json": "ec9c6afc86a45e1465e674b7e1278113b296470ef82d2c36f5c0fb9b54cbba78",
    "docs/baselines/v2.3/REQUIREMENT_REGISTRY_FREEZE_CANDIDATE.md": "eb0a08e070564a64a4cecfd9679c1ce2feca6ba72d206b06cba1a73d9bfd0244",
    "scripts/docs/validate-requirement-registry.py": "68a2c020cd413893c3459001069d2c54d31ee28c05cd9f91cca550ba702d9eaa",
}
EXPECTED_APPROVAL_ENVELOPE_SHA256 = "37eaf01f88b5fe2b86a2606b232d3e6a35593430404af427cab88006d32e9fc9"
EXPECTED_HISTORY_LINES = [
    "- Candidate ID: `V23-REQ-REGISTRY-FC1`",
    "- Approval revision: `1`",
    "- Approval revision: `2`",
    "- Revision status: `SUPERSEDED`",
    "- Superseded by: `V23-REQ-REGISTRY-FC1 revision 2`",
    "- Superseded by: `V23-REQ-REGISTRY-FC2`",
    "- Supersession reason: staged `git diff --check` detected one extra blank line at EOF.",
    "- Supersession reason: FC1 failed required clean-checkout source-hash verification.",
    "- Root cause: raw CRLF working-tree source hashes were not reproducible from canonical LF Git blobs for 28 of 31 source documents.",
    "- Previous manifest SHA-256: `d596e556125af8e8a8fc3e089489d0e6773e505ec39a36ffc22d0ee302057017`",
    "- Corrected FC1 manifest SHA-256: `225b7e36096cff05576e140c17340e434789f34a7d22b0aaf657ceaf5344f6ea`",
    "FC1 approval does not transfer automatically to FC2.",
]
EXPECTED_FC2_APPROVAL_LINES = [
    "## V23-REQ-REGISTRY-FC2 — Effective Detached Approval",
    "- Candidate ID: `V23-REQ-REGISTRY-FC2`",
    "- Baseline kind: `RECONCILED_REQUIREMENT_REGISTRY`",
    "- Approval model: `DETACHED_MARKDOWN_APPROVAL`",
    "- Effective approval status: `APPROVED`",
    "- Decision: `APPROVED`",
    "- Approval date: `2026-07-14`",
    "- Timezone: `Asia/Ho_Chi_Minh`",
    "- Authorized Approver: `Khoa, Nguyen`",
    "- Signature: `Khoa, Nguyen`",
    "- Source Git commit: `7f16d4c4b8ab514bd45de184f65ace221b03f4db`",
    "- Hash basis: `GIT_BLOB_CONTENT_AT_SOURCE_COMMIT`",
    "- Line-ending semantics: `GIT_CANONICAL_TEXT`",
    "- Manifest SHA-256: `ec9c6afc86a45e1465e674b7e1278113b296470ef82d2c36f5c0fb9b54cbba78`",
    "- Source aggregate: `34685bed33422505763d31ef8f86837a1139fd5aaf2946a9adcbfa9dd1cd9a35`",
    "- Registry aggregate: `832cc96192c72b89472964e030893ac4c01bcc0d20eb21f7e935b7a7c6288658`",
    "The manifest and candidate remain `CANDIDATE` / `PENDING_HUMAN_APPROVAL` as the immutable review payload. Effective approval is represented by this detached Markdown envelope. FC2 supersedes FC1.",
]
EXPECTED_APPROVAL_SCOPE_LINES = [
    "## FC2 Approval Scope",
    "- Approve the Phase 1C reconciled requirement registry baseline.",
    "- Approve source inventory, extraction/reconciliation result, identity mappings, aliases, composites, retired keys, scope classifications and traceability.",
    "- Permit this baseline to be committed and used as controlled input for BRD/UXF correction.",
]
EXPECTED_NON_CLAIM_LINES = [
    "- Not final BRD/UXF v2.3 approval.",
    "- Not final acceptance baseline.",
    "- Not architecture approval.",
    "- Not implementation authorization.",
    "- Temporary keys are not final canonical IDs.",
]
EXPECTED_GAP_LINES = [
    "- 609 active temporary keys.",
    "- 1174 acceptance units remain `INFERRED_ONLY`.",
    "- 15 documentation findings remain open for source correction.",
    "- BRD/UXF v2.2 source content still requires correction and approval for v2.3.",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_approved_envelope() -> list[str]:
    errors: list[str] = []
    existing = subprocess.run(
        [sys.executable, str(REGISTRY_VALIDATOR_PATH)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if existing.returncode != 0 or "Requirement registry validation VALID_READY_TO_FREEZE" not in existing.stdout.splitlines():
        errors.append("existing registry validator did not return VALID_READY_TO_FREEZE")

    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        manifest = {}
        errors.append(f"cannot read FC2 manifest: {exc}")
    if {field: manifest.get(field) for field in EXPECTED_MANIFEST} != EXPECTED_MANIFEST:
        errors.append("FC2 manifest identity, pending status, source contract, aggregate hash, or readiness differs")
    if manifest.get("correction") != EXPECTED_CORRECTION:
        errors.append("FC2 correction provenance is missing or altered")
    if manifest.get("approval") != EXPECTED_PENDING_APPROVAL:
        errors.append("FC2 manifest approval block must remain entirely pending")
    if manifest.get("unresolved_count") != 0:
        errors.append("FC2 manifest contains unresolved records")

    for relative_path, expected_hash in EXPECTED_SIGNED_FILE_HASHES.items():
        path = ROOT / relative_path
        if not path.is_file() or sha256(path) != expected_hash:
            errors.append(f"FC2 signed file raw SHA-256 differs: {relative_path}")

    if not APPROVAL_PATH.is_file() or sha256(APPROVAL_PATH) != EXPECTED_APPROVAL_ENVELOPE_SHA256:
        errors.append("FC1 approval history or FC2 approved detached envelope bytes differ")
        approval_lines: list[str] = []
    else:
        approval_lines = APPROVAL_PATH.read_text(encoding="utf-8").splitlines()
    for expected_line in (
        EXPECTED_HISTORY_LINES
        + EXPECTED_FC2_APPROVAL_LINES
        + EXPECTED_APPROVAL_SCOPE_LINES
        + EXPECTED_NON_CLAIM_LINES
        + EXPECTED_GAP_LINES
    ):
        expected_count = {
            "- Candidate ID: `V23-REQ-REGISTRY-FC1`": 2,
            "- Revision status: `SUPERSEDED`": 2,
            "- Approval date: `2026-07-14`": 3,
            "- Timezone: `Asia/Ho_Chi_Minh`": 3,
        }.get(expected_line, 1)
        if approval_lines.count(expected_line) != expected_count:
            errors.append(f"missing, duplicated, or inexact approval-history line: {expected_line}")

    detached_paths = {
        "docs/baselines/v2.3/requirements/registry-freeze-manifest.json",
        "docs/baselines/v2.3/REQUIREMENT_REGISTRY_FREEZE_CANDIDATE.md",
        "docs/baselines/v2.3/REQUIREMENT_REGISTRY_FREEZE_APPROVAL.md",
        "scripts/docs/validate-requirement-registry-approval.py",
    }
    aggregate_paths = {
        entry.get("path")
        for field in ("registry_artifacts", "validator_artifacts")
        for entry in manifest.get(field, [])
        if isinstance(entry, dict)
    }
    if detached_paths & aggregate_paths:
        errors.append("manifest/candidate/approval artifacts must remain outside the signed registry aggregate")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", action="store_true", help="validate the immutable FC2 candidate payload")
    args = parser.parse_args()
    errors = validate_approved_envelope()
    if errors:
        print("FAIL — INVALID_RECONCILED_REGISTRY_FREEZE_CANDIDATE", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    if args.candidate:
        print("PASS — VALID_RECONCILED_REGISTRY_FREEZE_CANDIDATE_PENDING_APPROVAL")
        return 0
    print("PASS — VALID_APPROVED_RECONCILED_REGISTRY_BASELINE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
