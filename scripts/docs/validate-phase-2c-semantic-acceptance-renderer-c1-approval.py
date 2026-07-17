#!/usr/bin/env python3
"""Validate detached approval of Semantic Acceptance Renderer C1.

All signed candidate content is read from committed Git objects. The validator
supports the exact two-file staged approval state on the candidate commit and a
clean accepted commit whose direct parent is the candidate.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE_ID = "V23-P2C-SEMANTIC-ACCEPTANCE-RENDERER-C1"
CANDIDATE = "128bd588a7a5411ce21f466da8cd1ff0c722b75c"
PARENT = "351270d2bed7c54853b3a6cd6514b8906db22cf8"
TREE = "4222dad205ef02f3c989d4a6a80c00775317ed0f"
GIT_CONTENT_AGGREGATE = "f8c3469c7462a38b6ea6290e8ac524591d11daf59ea76386e724c834f9ee31b9"
GENERATED_AGGREGATE = "22daa4048b6577f37cb6fdda978f3b258165a96921e5e2c1a2e421b587ba140b"
MANIFEST_SHA256 = "5332d8fd15523b9bc6bb40c4cf0987d54e3565c6653e6632971905b3283e98c9"
SCOPE = "OBLIGATION_SPECIFIC_ORACLE_RENDERING_AND_RECORD_SPECIFIC_HUMAN_PROCEDURES"

P2 = "docs/baselines/v2.3/phase-2"
MANIFEST = f"{P2}/semantic-acceptance-renderer-c1-manifest.json"
APPROVAL_MD = f"{P2}/PHASE_2C_SEMANTIC_ACCEPTANCE_RENDERER_C1_APPROVAL.md"
APPROVAL_VALIDATOR = "scripts/docs/validate-phase-2c-semantic-acceptance-renderer-c1-approval.py"
APPROVAL_PATHS = [APPROVAL_MD, APPROVAL_VALIDATOR]
BACKUP_REF = "refs/ysim-backups/v2.3/phase-2c-document-baseline-c5-generic-rendering-rejected"
BACKUP_OBJECT = "cf9c432acc84fa82f92a7520c795c2659e1dc50c"

CANDIDATE_PATHS = [
    f"{P2}/SEMANTIC_ACCEPTANCE_RENDERER_C1.md",
    f"{P2}/SEMANTIC_ACCEPTANCE_RENDERER_C1_REVIEW_PACK.md",
    f"{P2}/semantic-acceptance-renderer-c1-actor-provenance.json",
    f"{P2}/semantic-acceptance-renderer-c1-ast-previews.json",
    f"{P2}/semantic-acceptance-renderer-c1-before-after.json",
    f"{P2}/semantic-acceptance-renderer-c1-catalog.json",
    f"{P2}/semantic-acceptance-renderer-c1-decision-previews.json",
    f"{P2}/semantic-acceptance-renderer-c1-false-pass-regressions.json",
    f"{P2}/semantic-acceptance-renderer-c1-generic-equivalence.json",
    f"{P2}/semantic-acceptance-renderer-c1-manifest.json",
    f"{P2}/semantic-acceptance-renderer-c1-operator-schemas.json",
    f"{P2}/semantic-acceptance-renderer-c1-procedure-previews.json",
    f"{P2}/semantic-acceptance-renderer-c1-reference-good-contracts.json",
    f"{P2}/semantic-acceptance-renderer-c1-resolver-evidence.json",
    f"{P2}/semantic-acceptance-renderer-c1-semantic-audit.json",
    "scripts/docs/build-semantic-acceptance-renderer-c1.py",
    "scripts/docs/tests/test-semantic-acceptance-renderer-c1.py",
    "scripts/docs/validate-semantic-acceptance-renderer-c1-regressions.py",
    "scripts/docs/validate-semantic-acceptance-renderer-c1-similarity.py",
    "scripts/docs/validate-semantic-acceptance-renderer-c1.py",
]

NON_CLAIMS = [
    "NOT_REJECTED_DOCUMENT_BASELINE_C5_APPROVAL",
    "NOT_DOCUMENT_BASELINE_C6_MATERIALIZATION_OR_ACCEPTANCE",
    "NOT_BRD_UXF_REMEDIATION",
    "NOT_RUNTIME_ADAPTER_VALIDATION",
    "NOT_RUNTIME_MUTATION_SCORE",
    "NOT_YADF_AUTHORIZATION",
    "NOT_PRODUCTION_IMPLEMENTATION",
]


def git(*args: str, binary: bool = False) -> str | bytes:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, text=not binary
    ).strip() if not binary else subprocess.check_output(["git", *args], cwd=ROOT)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def object_bytes(commit: str, path: str) -> bytes:
    return git("show", f"{commit}:{path}", binary=True)  # type: ignore[return-value]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_content_aggregate(paths: list[str]) -> str:
    entries = [
        {"path": path, "sha256": sha256(object_bytes(CANDIDATE, path))}
        for path in sorted(paths)
    ]
    body = (json.dumps(entries, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()
    return sha256(body)


def generated_aggregate(manifest: dict[str, object]) -> str:
    hashes = manifest["per_file_sha256_excluding_manifest"]
    require(isinstance(hashes, dict), "manifest per-file hashes are malformed")
    entries = [{"path": path, "sha256": digest} for path, digest in sorted(hashes.items())]
    body = (json.dumps(entries, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()
    return sha256(body)


def approval_bytes(mode: str) -> bytes:
    if mode == "STAGED":
        return git("show", f":{APPROVAL_MD}", binary=True)  # type: ignore[return-value]
    return object_bytes("HEAD", APPROVAL_MD)


def main() -> int:
    head = str(git("rev-parse", "HEAD"))
    require(git("cat-file", "-t", CANDIDATE) == "commit", "candidate commit is absent")
    require(git("rev-parse", f"{CANDIDATE}^") == PARENT, "candidate direct parent mismatch")
    require(git("rev-parse", f"{CANDIDATE}^{{tree}}") == TREE, "candidate tree mismatch")

    paths = str(git("diff", "--name-only", f"{PARENT}..{CANDIDATE}")).splitlines()
    require(paths == CANDIDATE_PATHS, "candidate inventory is not the exact signed 20-file set")
    require(git_content_aggregate(paths) == GIT_CONTENT_AGGREGATE, "Git-content aggregate mismatch")
    manifest_bytes = object_bytes(CANDIDATE, MANIFEST)
    require(sha256(manifest_bytes) == MANIFEST_SHA256, "manifest SHA-256 mismatch")
    manifest = json.loads(manifest_bytes)
    require(generated_aggregate(manifest) == GENERATED_AGGREGATE, "generated aggregate mismatch")
    require(manifest["generated_payload_aggregate_sha256"] == GENERATED_AGGREGATE, "manifest aggregate mismatch")
    require(
        (manifest["candidate_id"], manifest["status"], manifest["approval_status"])
        == (CANDIDATE_ID, "CANDIDATE", "PENDING_HUMAN_APPROVAL"),
        "embedded candidate approval state changed",
    )
    require(manifest["approval_scope"] == SCOPE, "embedded approval scope mismatch")
    require(manifest["counts"]["operator_rendered"] == 937, "operator-rendered count mismatch")
    require(manifest["counts"]["procedures"] == 156, "procedure count mismatch")
    require(manifest["counts"]["reference_good"] == 59, "reference-good count mismatch")
    for path, digest in manifest["per_file_sha256_excluding_manifest"].items():
        require(sha256(object_bytes(CANDIDATE, path)) == digest, f"signed blob changed: {path}")

    if head == CANDIDATE:
        mode = "STAGED"
        staged = str(git("diff", "--cached", "--name-only")).splitlines()
        require(staged == APPROVAL_PATHS, "staged approval inventory is not exactly two files")
        require(not git("diff", "--name-only"), "tracked unstaged changes exist")
        require(not git("ls-files", "--others", "--exclude-standard"), "untracked files exist")
    else:
        mode = "COMMITTED"
        require(git("rev-parse", "HEAD^") == CANDIDATE, "accepted direct parent mismatch")
        accepted_paths = str(git("diff", "--name-only", f"{CANDIDATE}..HEAD")).splitlines()
        require(accepted_paths == APPROVAL_PATHS, "candidate-to-accepted diff is not exactly two files")
        require(not git("status", "--porcelain"), "accepted checkout is not clean")

    approval = approval_bytes(mode).decode("utf-8")
    required_tokens = [
        CANDIDATE_ID, CANDIDATE, PARENT, TREE, GIT_CONTENT_AGGREGATE,
        GENERATED_AGGREGATE, MANIFEST_SHA256, f"Approval Scope: `{SCOPE}`",
        "Decision: `APPROVED`", "Authorized Approver: `Khoa, Nguyen`",
        "Signature: `Khoa, Nguyen`", "Date: `2026-07-17`",
        "Timezone: `Asia/Ho_Chi_Minh`", "937 AST-based records",
        "156 records", "59 hash-locked typed custom contracts", *NON_CLAIMS,
    ]
    for token in required_tokens:
        require(token in approval, f"approval record missing token: {token}")

    require(not git("diff", "--name-only", f"{PARENT}..{CANDIDATE}", "--", "docs/BRD", "docs/UXF"), "candidate changed BRD/UXF")
    if mode == "COMMITTED":
        require(not git("diff", "--name-only", f"{CANDIDATE}..HEAD", "--", "docs/BRD", "docs/UXF"), "approval changed BRD/UXF")
    try:
        local_backup = git("rev-parse", BACKUP_REF)
    except subprocess.CalledProcessError:
        local_backup = ""
    require(not local_backup or local_backup == BACKUP_OBJECT, "rejected C5 backup ref changed")

    print("VALID_APPROVED_PHASE_2C_SEMANTIC_ACCEPTANCE_RENDERER_C1")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, TypeError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(f"FAIL — {exc}")
        raise SystemExit(1)
