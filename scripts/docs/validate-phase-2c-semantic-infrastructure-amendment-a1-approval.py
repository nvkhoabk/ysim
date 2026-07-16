#!/usr/bin/env python3
"""Validate detached approval for semantic infrastructure amendment A1."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE_ID = "V23-P2C-SEMANTIC-INFRASTRUCTURE-AMENDMENT-A1"
CANDIDATE = "50044d2200c6dcc6e27f7ba44623bb8ca8c4dee0"
PARENT = "c11d95116154ff8919c04b49b0a502cf66b3907d"
TREE = "ad1a98eece479370d6b7c9bab828e2e26a0b6cbb"
GIT_CONTENT_AGGREGATE = "ac025b45895f3a895796c58af1e37bc999cba19c1af0feddab741cfa4764a700"
GENERATED_AGGREGATE = "9beda29ad8fe380b9931f128a9747a7a00b042b333259111dc5e1fd8e011926d"
MANIFEST_SHA256 = "1fe5f48b3305ada86ebcce94e31407b06888419ac2c2731822ac39f8fb2e2b2e"
C4_REF = "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c4-blocked"
C4_OBJECT = "24037270c435a80210ab00f1b20f2a38c92ea36f"
C4_TREE = "897079721b3e8a808f363480d554e88dc9f8f284"
C4_GENERATED_AGGREGATE = "f2c57653024f28f47f80bbaf2da3110bf3d80417a606382613d431db802ededc"
MANIFEST = "docs/baselines/v2.3/phase-2/semantic-infrastructure-amendment-a1-manifest.json"
C4_MANIFEST = "docs/baselines/v2.3/phase-2/semantic-completion-c4-manifest.json"
APPROVAL_MD = "docs/baselines/v2.3/phase-2/PHASE_2C_SEMANTIC_INFRASTRUCTURE_AMENDMENT_A1_APPROVAL.md"
APPROVAL_VALIDATOR = "scripts/docs/validate-phase-2c-semantic-infrastructure-amendment-a1-approval.py"
APPROVAL_PATHS = [APPROVAL_MD, APPROVAL_VALIDATOR]
GENERATED_PATHS = [
    "docs/baselines/v2.3/phase-2/PHASE_2C_SEMANTIC_INFRASTRUCTURE_AMENDMENT_A1.md",
    "docs/baselines/v2.3/phase-2/semantic-infrastructure-amendment-a1-regressions.json",
    "docs/baselines/v2.3/phase-2/semantic-infrastructure-brd-ws-14-r031-example-a1.json",
    "docs/baselines/v2.3/phase-2/semantic-infrastructure-c4-impact-register-a1.json",
    "docs/baselines/v2.3/phase-2/semantic-infrastructure-generic-set-types-a1.json",
    "docs/baselines/v2.3/phase-2/semantic-infrastructure-mutation-isolation-a1.json",
]
NON_CLAIMS = [
    "NOT_C4_DOCUMENT_BASELINE_APPROVAL",
    "NOT_BRD_UXF_REMEDIATION",
    "NOT_RUNTIME_ADAPTER_VALIDATION",
    "NOT_RUNTIME_MUTATION_SCORE",
    "NOT_YADF_AUTHORIZATION",
    "NOT_PRODUCTION_IMPLEMENTATION",
    "NOT_APPROVAL_OF_27_PENDING_DECISIONS",
]


def git(*args: str, binary: bool = False):
    result = subprocess.check_output(["git", *args], cwd=ROOT, text=not binary)
    return result if binary else result.strip()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def object_bytes(commit: str, path: str) -> bytes:
    return git("show", f"{commit}:{path}", binary=True)


def candidate_paths() -> list[str]:
    return git("diff", "--name-only", f"{PARENT}..{CANDIDATE}").splitlines()


def path_aggregate(paths: list[str]) -> str:
    digest = hashlib.sha256()
    for path in sorted(paths):
        digest.update(path.encode("utf-8") + b"\0" + object_bytes(CANDIDATE, path) + b"\0")
    return digest.hexdigest()


def approval_text(mode: str) -> str:
    payload = git("show", f":{APPROVAL_MD}", binary=True) if mode == "STAGED" else object_bytes("HEAD", APPROVAL_MD)
    return payload.decode("utf-8")


def main() -> int:
    head = git("rev-parse", "HEAD")
    require(git("cat-file", "-t", CANDIDATE) == "commit", "candidate commit is absent")
    require(git("rev-parse", f"{CANDIDATE}^") == PARENT, "candidate direct parent mismatch")
    require(git("rev-parse", f"{CANDIDATE}^{{tree}}") == TREE, "candidate tree mismatch")

    paths = candidate_paths()
    require(len(paths) == 11, "candidate path count differs from 11")
    require(path_aggregate(paths) == GIT_CONTENT_AGGREGATE, "signed Git-content aggregate mismatch")
    require(hashlib.sha256(object_bytes(CANDIDATE, MANIFEST)).hexdigest() == MANIFEST_SHA256, "manifest hash mismatch")
    require(path_aggregate(GENERATED_PATHS) == GENERATED_AGGREGATE, "generated payload aggregate mismatch")

    manifest = json.loads(object_bytes(CANDIDATE, MANIFEST))
    require(
        (manifest["candidate_id"], manifest["status"], manifest["approval_status"])
        == (CANDIDATE_ID, "CANDIDATE", "PENDING_HUMAN_APPROVAL"),
        "embedded candidate state changed",
    )
    require(manifest["exact_file_inventory"] == paths, "candidate inventory differs from manifest")
    require(manifest["generated_payload_aggregate_sha256"] == GENERATED_AGGREGATE, "manifest generated aggregate mismatch")
    for path, expected in manifest["signed_file_hashes_excluding_self_referential_manifest"].items():
        require(hashlib.sha256(object_bytes(CANDIDATE, path)).hexdigest() == expected, f"signed candidate file changed: {path}")

    if head == CANDIDATE:
        mode = "STAGED"
        require(git("diff", "--cached", "--name-only").splitlines() == APPROVAL_PATHS, "staged approval inventory mismatch")
        require(not git("diff", "--name-only"), "tracked unstaged changes exist")
        require(not git("ls-files", "--others", "--exclude-standard"), "untracked files exist")
    else:
        mode = "COMMITTED"
        require(git("rev-parse", "HEAD^") == CANDIDATE, "accepted commit direct parent mismatch")
        require(git("diff", "--name-only", f"{CANDIDATE}..HEAD").splitlines() == APPROVAL_PATHS, "accepted diff is not exactly two approval files")
        require(not git("status", "--porcelain"), "accepted checkout is not clean")

    approval = approval_text(mode)
    required_tokens = [
        CANDIDATE_ID, CANDIDATE, PARENT, TREE, GIT_CONTENT_AGGREGATE,
        GENERATED_AGGREGATE, MANIFEST_SHA256,
        "Decision: `APPROVED`",
        "Reapproval reason: `CORRECTED_MANIFEST_SHA_256`",
        "Approval Scope: `OPERATOR_GENERIC_SET_TYPING_AND_CANONICAL_MUTATION_ISOLATION`",
        "Authorized Approver: `Khoa, Nguyen`", "Signature: `Khoa, Nguyen`",
        "Date: `2026-07-16`", "Timezone: `Asia/Ho_Chi_Minh`",
        "Generic `SET_EQUALS<T>`, `SET_CONTAINS<T>`, and `SET_EXCLUDES<T>` typing.",
        "The `BRD-WS-14-R031` typed `REFERENCE_ID` set model.",
        "Independent future regeneration of the 354 affected C4 mutation hashes.",
        C4_REF, C4_OBJECT, C4_TREE, C4_GENERATED_AGGREGATE, *NON_CLAIMS,
    ]
    for token in required_tokens:
        require(token in approval, f"approval record missing: {token}")

    require(git("rev-parse", C4_REF) == C4_OBJECT, "C4 backup object changed")
    require(git("rev-parse", f"{C4_REF}^3^{{tree}}") == C4_TREE, "C4 backup tree changed")
    c4_manifest = json.loads(git("show", f"{C4_REF}^3:{C4_MANIFEST}", binary=True))
    require(c4_manifest["generated_payload_aggregate_sha256"] == C4_GENERATED_AGGREGATE, "C4 generated aggregate changed")

    require(not git("diff", "--name-only", f"{PARENT}..{CANDIDATE}", "--", "docs/BRD", "docs/UXF"), "candidate changed BRD/UXF")
    if mode == "COMMITTED":
        require(not git("diff", "--name-only", f"{CANDIDATE}..HEAD", "--", "docs/BRD", "docs/UXF"), "approval changed BRD/UXF")

    print("VALID_APPROVED_PHASE_2C_SEMANTIC_INFRASTRUCTURE_AMENDMENT_A1")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, subprocess.CalledProcessError, KeyError, json.JSONDecodeError) as exc:
        print(f"FAIL — {exc}")
        raise SystemExit(1)
