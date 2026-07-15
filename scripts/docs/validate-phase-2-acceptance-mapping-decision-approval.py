#!/usr/bin/env python3
"""Validate detached approval of the Phase 2C C3 mapping decisions."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
P2 = "docs/baselines/v2.3/phase-2/"
HISTORICAL = "0df2d424e00f9cd27b8dcb6645eef827ce97b60e"
MODEL = "a989367a6f69f1a03a8269562ce43bda3968b71a"
CANDIDATE = "f4f4a5e8a3dba1fb1cadc3e3daa3881dbbc6ba39"
CANDIDATE_ID = "V23-P2C-ACCEPTANCE-MAPPING-C3"
APPROVAL_MD = P2 + "PHASE_2_ACCEPTANCE_MAPPING_DECISION_APPROVAL.md"
APPROVAL_VALIDATOR = "scripts/docs/validate-phase-2-acceptance-mapping-decision-approval.py"
APPROVAL_PATHS = {APPROVAL_MD, APPROVAL_VALIDATOR}

SIGNED = {
    P2 + "acceptance-mapping-c3.json": "9f1e1a62ff16149b7c1af849590db07d7cb87847f523a5c5b4d2bf06d6a145a8",
    P2 + "acceptance-mapping-c3-manifest.json": "7f00d4171abe59039e6099c16d311e8953de92b7b091389dd8a4e5450b5e83f6",
    P2 + "acceptance-verification-shapes.json": "080cbd2f9f2e744ec88beef5a08a1f6cea107fcb5519436911c04acf2bfdcd61",
    P2 + "acceptance-semantic-clusters.json": "c0d16237bbc102549ea19fd17ade90885209b86e306cc1797d32698f2a7ad8d5",
    P2 + "acceptance-mapping-archetype-decisions.json": "d9bd1c409e91fe222c042ecc829b127812876b60e3267e93182f4e65d9843fcd",
    P2 + "acceptance-inline-archetype-catalog.json": "e5d729d4966d60e4fd25c622e30ba10d8371cdd02d9a9ce4ad4528c7ca2d61c0",
    P2 + "acceptance-source-normalization-plan.json": "4520b87782b7c259692871608903d78b261a7fd76eaf1ef32927f0b451dfd85a",
    P2 + "acceptance-structural-reconciliation-plan.json": "4c7960738e2c6754f21280d767da435e1bc166ef3c065a08787eb0cef5e48c3c",
}
GENERATED_AGGREGATE = "09127e4ead4ab143953d47004d71dc85027e3976c5921f22899037f92aab6df9"
STAGED_AGGREGATE = "626a53c67b83cd34310d53b0c3f75747ad000b9a5184f70f6d3e16af359798c3"

SELECTED = {
    "P2C-AC-C3-DEC-005-OPT-1", "P2C-AC-C3-DEC-023-OPT-1",
    "P2C-AC-C3-DEC-027-OPT-1", "P2C-AC-C3-DEC-030-OPT-1",
    "P2C-AC-C3-DEC-PREFULFILLMENT-OPT-1", "P2C-AC-C3-DEC-001-OPT-3",
    "P2C-AC-C3-DEC-002-OPT-3", "P2C-AC-C3-DEC-003-OPT-3",
    "P2C-AC-C3-DEC-009-OPT-3", "P2C-AC-C3-DEC-010-OPT-3",
    "P2C-AC-C3-DEC-011-OPT-3", "P2C-AC-C3-DEC-018-OPT-3",
    "P2C-AC-C3-DEC-019-OPT-3", "P2C-AC-C3-DEC-029-OPT-3",
    "P2C-AC-C3-DEC-031-OPT-3", "P2C-AC-C3-DEC-032-OPT-3",
    "P2C-AC-C3-DEC-034-OPT-3", "P2C-AC-C3-DEC-035-OPT-3",
    "P2C-AC-C3-DEC-036-OPT-3",
}

DIRECTIVE_ANCHORS = (
    "Touch and responsive experience", "KPI Definition", "Identity Providers",
    "Commerce First", "Authorization future extensibility",
    "Communication channel extensibility", "Communication performance",
    "Customer Portal", "Multi-tenant", "Experience First",
    "Customer Identity ownership", "Organization Relationship rights",
    "Gateway extensibility", "Configuration over hard-code",
    "Runtime rendering fallback", "Pre-Fulfillment Commercial Validation",
)


class Failure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Failure(message)


def git(*args: str, binary: bool = False) -> bytes | str:
    result = subprocess.run(["git", *args], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    require(result.returncode == 0, f"git {' '.join(args)} failed: {result.stderr.decode(errors='replace')}")
    return result.stdout if binary else result.stdout.decode().strip()


def commit_blob(commit: str, path: str) -> bytes:
    return git("show", f"{commit}:{path}", binary=True)  # type: ignore[return-value]


def candidate_paths() -> list[str]:
    return sorted(filter(None, str(git("diff", "--name-only", MODEL, CANDIDATE)).splitlines()))


def aggregate_candidate() -> str:
    value = hashlib.sha256()
    for path in candidate_paths():
        blob = commit_blob(CANDIDATE, path)
        value.update(path.encode())
        value.update(b"\0")
        value.update(blob)
        value.update(b"\0")
    return value.hexdigest()


def approval_text(head: str) -> str:
    if head == CANDIDATE:
        return git("show", f":{APPROVAL_MD}", binary=True).decode()  # type: ignore[union-attr]
    return commit_blob(head, APPROVAL_MD).decode()


def main() -> int:
    try:
        head = str(git("rev-parse", "HEAD"))
        for commit in (HISTORICAL, MODEL, CANDIDATE):
            git("cat-file", "-e", f"{commit}^{{commit}}")
        require(git("rev-parse", f"{CANDIDATE}^") == MODEL, "candidate parent mismatch")
        require(subprocess.run(["git", "merge-base", "--is-ancestor", HISTORICAL, MODEL], cwd=ROOT).returncode == 0, "historical baseline ancestry mismatch")
        require(subprocess.run(["git", "merge-base", "--is-ancestor", MODEL, CANDIDATE], cwd=ROOT).returncode == 0, "candidate ancestry mismatch")
        tag_target = git("rev-parse", "baseline/v2.3/phase-2/acceptance-model/c1-accepted^{}")
        require(tag_target == MODEL, "accepted Acceptance Model tag target mismatch")

        paths = candidate_paths()
        require(len(paths) == 32, "candidate inventory is not exactly 32 files")
        require(APPROVAL_MD not in paths and APPROVAL_VALIDATOR not in paths, "approval layer exists in candidate")
        require(git("diff", "--name-only", MODEL, CANDIDATE, "--", "docs/BRD", "docs/UXF") == "", "BRD/UXF changed in candidate")
        for path, expected in SIGNED.items():
            require(hashlib.sha256(commit_blob(CANDIDATE, path)).hexdigest() == expected, f"signed blob mismatch: {path}")
        require(aggregate_candidate() == STAGED_AGGREGATE, "signed candidate aggregate mismatch")

        manifest = json.loads(commit_blob(CANDIDATE, P2 + "acceptance-mapping-c3-manifest.json"))
        mapping = json.loads(commit_blob(CANDIDATE, P2 + "acceptance-mapping-c3.json"))
        decisions = json.loads(commit_blob(CANDIDATE, P2 + "acceptance-mapping-archetype-decisions.json"))
        require(manifest["generated_payload_aggregate_sha256"] == GENERATED_AGGREGATE, "generated aggregate mismatch")
        require(mapping["candidate_id"] == CANDIDATE_ID and mapping["status"] == "CANDIDATE" and mapping["approval_status"] == "PENDING_HUMAN_APPROVAL", "embedded candidate state mismatch")
        available = {option["option_id"] for decision in decisions["decisions"] for option in decision["options"]}
        require(len(SELECTED) == 19 and SELECTED <= available, "selected options are incomplete or invalid")

        if head == CANDIDATE:
            staged = set(filter(None, str(git("diff", "--cached", "--name-only")).splitlines()))
            require(staged == APPROVAL_PATHS, "pre-commit approval index must contain exactly two files")
        else:
            require(git("rev-parse", f"{head}^") == CANDIDATE, "accepted commit direct parent mismatch")
            changed = set(filter(None, str(git("diff", "--name-only", CANDIDATE, head)).splitlines()))
            require(changed == APPROVAL_PATHS, "candidate..accepted diff must contain exactly two approval files")

        text = approval_text(head)
        required = (
            CANDIDATE_ID, CANDIDATE, MODEL, "APPROVED",
            "ACCEPTANCE_MAPPING_DECISIONS_AND_REMEDIATION_ROUTES_ONLY",
            "Authorized Approver: `Khoa, Nguyen`", "Signature: `Khoa, Nguyen`",
            "2026-07-15", "Asia/Ho_Chi_Minh", GENERATED_AGGREGATE,
            STAGED_AGGREGATE, *SIGNED.values(), *SELECTED, *DIRECTIVE_ANCHORS,
            "NOT_APPROVAL_OF_C1_C2_ACCEPTANCE_CONTRACTS",
            "NOT_APPROVAL_OF_MATERIALIZED_SOURCE_ACCEPTANCE_CONTRACTS",
            "NOT_FINAL_BRD_UXF_DOCUMENT_BASELINE_APPROVAL",
            "NOT_YADF_IMPLEMENTATION_AUTHORIZATION",
            "NOT_AUTHORIZATION_TO_SKIP_CLEAN_CHECKOUT_OR_HUMAN_SEMANTIC_SAMPLING",
            "HISTORICAL_REGISTRY_AND_PHASE_2_VALIDATORS",
            "ACCEPTED_ACCEPTANCE_MODEL_VALIDATORS", "C3 PRE-COMMIT/INDEX VALIDATORS",
            "C3 COMMITTED CANDIDATE VERIFICATION", "C3 ACCEPTED DECISION VERIFICATION",
        )
        for value in required:
            require(value in text, f"approval value missing: {value}")
        for option_id in SELECTED:
            require(text.count(f"`{option_id}`") == 1, f"selected option must appear once: {option_id}")
        require(text.count("### ") >= 21, "applicability matrix or semantic directives incomplete")
    except (Failure, KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"FAIL — {error}", file=sys.stderr)
        return 1
    print("VALID_APPROVED_PHASE_2C_ACCEPTANCE_MAPPING_DECISIONS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
