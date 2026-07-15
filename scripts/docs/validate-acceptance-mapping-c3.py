#!/usr/bin/env python3
"""Validate the focused Phase 2C acceptance-mapping C3 candidate."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"
HEAD = "a989367a6f69f1a03a8269562ce43bda3968b71a"
CANDIDATE = "V23-P2C-ACCEPTANCE-MAPPING-C3"
ALLOWED = {
    "EXISTING_PROFILE_BINDING_HIGH_CONFIDENCE",
    "NEW_PROFILE_BINDING_HIGH_CONFIDENCE",
    "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE",
    "UNIQUE_INLINE_CONTRACT_REQUIRED",
    "DETERMINISTIC_SOURCE_NORMALIZATION_REQUIRED",
    "STRUCTURAL_RECONCILIATION_REQUIRED",
    "BUSINESS_SEMANTIC_DECISION_REQUIRED",
    "INVALID_OR_BLOCKED",
}
C2_HASHES = {
    "generated_payload_aggregate_sha256": "b0e3239d96a47f08b7a43b872ea2d8154e8923c5e05844b94a47580c920386b3",
    "staged_git_content_aggregate_sha256": "51f6ea2ab2bb98581d1388618c661e8b2ae91e6f3930680b5e7620716c59596e",
    "mapping_sha256": "b4110c2ac1bf7c2b1279c0fd2e047c06ea135c818a6ada58ed20165edffa9440",
    "cluster_data_sha256": "fcbf3f688bf0be7f4473b0ac3252ee50f914726154c6f3ec4dfd115bbf5d8a51",
    "decision_data_sha256": "621d7a37789d01dabf05f3fd3703138b7b8f6659af5b91486d1bbae1762a52bc",
    "inline_archetype_catalog_sha256": "60d1afe30889c171f4c8bb5101ad7c31b1f95bc782cd9ef2e52c9524dde1a989",
    "manifest_sha256": "ea73447f96862ade1aca5acf86813673b668224b38757e2f03a572f4e05711a1",
}


class Failure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Failure(message)


def load(name: str) -> dict:
    return json.loads((P2 / name).read_text())


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True)
    require(result.returncode == 0, f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def main() -> int:
    try:
        require(git("rev-parse", "HEAD") == HEAD, "HEAD is not the accepted Acceptance Model commit")
        mapping = load("acceptance-mapping-c3.json")
        manifest = load("acceptance-mapping-c3-manifest.json")
        decisions = load("acceptance-mapping-archetype-decisions.json")
        audit = load("acceptance-mapping-c2-approval-audit.json")

        require(mapping["candidate_id"] == CANDIDATE, "candidate identity mismatch")
        require(mapping["status"] == "CANDIDATE" and mapping["approval_status"] == "PENDING_HUMAN_APPROVAL", "candidate is not pending")
        require(mapping["supersedes"] == "V23-P2C-ACCEPTANCE-MAPPING-C2", "C2 supersession missing")
        require(mapping["supersession_reason"] == "UNSUPPORTED_UNIQUE_REASON_NON_DISPOSITIONING_DECISIONS_AND_HIDDEN_SOURCE_DEFECTS", "supersession reason mismatch")
        require(mapping["blocker"] == "ACCEPTANCE_MAPPING_DECISIONS_NOT_APPROVED", "blocker mismatch")
        require(mapping["next_gate"] == "HUMAN_ACCEPTANCE_MAPPING_DECISION_APPROVAL", "next gate mismatch")
        require(mapping["final_document_baseline"] == "NOT_APPROVED" and mapping["yadf_implementation"] == "NOT_AUTHORIZED", "non-claims missing")

        rows = mapping["mappings"]
        ids = [row["requirement_id"] for row in rows]
        require(len(rows) == len(set(ids)) == 1076, "mapping accounting is not exactly 1,076 unique records")
        require(all(row["disposition"] in ALLOWED for row in rows), "unknown disposition")
        require(all(row.get("unique_reason") != "OTHER_WITH_EXPLICIT_JUSTIFICATION" for row in rows), "unsupported OTHER remains")
        counts = Counter(row["disposition"] for row in rows)
        require(counts["INVALID_OR_BLOCKED"] == 0, "INVALID_OR_BLOCKED must be zero")
        require(mapping["summary"]["disposition_counts"] == {name: counts[name] for name in sorted(ALLOWED)}, "summary disposition accounting mismatch")
        require(mapping["summary"]["unsupported_other_count"] == 0, "unsupported OTHER summary mismatch")

        require(decisions["candidate_id"] == CANDIDATE, "decision candidate mismatch")
        require(decisions["decision_count"] == len(decisions["decisions"]), "decision count mismatch")
        decision_members = []
        for decision in decisions["decisions"]:
            require(decision["status"] == "PENDING_HUMAN_APPROVAL" and decision["selected_option"] is None, f"decision is not pending: {decision['decision_id']}")
            require(2 <= len(decision["options"]) <= 3, f"decision must have 2-3 options: {decision['decision_id']}")
            require(sum(bool(option["recommended"]) for option in decision["options"]) == 1, f"decision must have one recommendation: {decision['decision_id']}")
            for option in decision["options"]:
                require(option["terminal_disposition"] in ALLOWED, f"non-terminal option: {option['option_id']}")
                require(option["terminal_disposition"] != "BUSINESS_SEMANTIC_DECISION_REQUIRED", f"option loops to human review: {option['option_id']}")
                require(option.get("contract_preview"), f"option preview missing: {option['option_id']}")
            decision_members.extend(decision["affected_requirements"])
        expected_members = sorted(row["requirement_id"] for row in rows if row["disposition"] == "BUSINESS_SEMANTIC_DECISION_REQUIRED")
        require(sorted(decision_members) == expected_members, "decision coverage mismatch")

        require(audit["approval_blocker_count"] == len(audit["approval_blockers"]) == 12, "C2 audit must preserve 12 blockers")
        require(audit["hashes"] == C2_HASHES, "C2 audit hashes mismatch")
        require(manifest["candidate_id"] == CANDIDATE and manifest["status"] == "CANDIDATE", "manifest identity mismatch")
        require(manifest["supersedes"]["candidate_id"] == "V23-P2C-ACCEPTANCE-MAPPING-C2", "manifest supersession missing")
        require(manifest["supersedes"]["hashes"] == C2_HASHES, "manifest C2 hashes mismatch")
        require(len(manifest["audit_blocker_resolution"]) == 12, "manifest blocker resolutions missing")
        require(all(item["resolution_status"] == "RESOLVED_IN_C3_CANDIDATE" and item.get("resolution_evidence") for item in manifest["audit_blocker_resolution"]), "unresolved or unevidenced audit blocker")
        require(manifest["approval_block"]["decision"] == "PENDING", "approval block must remain pending")

        require(hashlib.sha256((P2 / "acceptance-mapping-c2.json").read_bytes()).hexdigest() == C2_HASHES["mapping_sha256"], "preserved C2 mapping hash mismatch")
        require(hashlib.sha256((P2 / "acceptance-mapping-c2-manifest.json").read_bytes()).hexdigest() == C2_HASHES["manifest_sha256"], "preserved C2 manifest hash mismatch")
        require(git("diff", "--name-only", HEAD, "--", "docs/BRD", "docs/UXF") == "", "BRD/UXF changed during Phase B")

        check = subprocess.run([sys.executable, "scripts/docs/generate-acceptance-mapping-c3.py", "--check"], cwd=ROOT, text=True, capture_output=True)
        require(check.returncode == 0, f"deterministic generation failed: {check.stdout}{check.stderr}")
    except (Failure, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL — {error}", file=sys.stderr)
        return 1
    print("PASS — VALID_ACCEPTANCE_MAPPING_C3_CANDIDATE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
