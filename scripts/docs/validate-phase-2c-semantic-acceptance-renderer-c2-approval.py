#!/usr/bin/env python3
"""Validate detached approval of Semantic Acceptance Renderer C2."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P2 = "docs/baselines/v2.3/phase-2"
CANDIDATE = "120184748c70543b86220fb4f3f3089e99d175dc"
PARENT = "9a49377d9fcd3d25e922b80cc6af3a4474ec0975"
TREE = "364bb5e4c327e1c49af07fb50eed548e89a49cda"
GIT_AGGREGATE = "914b562cda91176a72220115d91658d1e879339c93934c84afff8879b282049c"
GENERATED_AGGREGATE = "76597f70c34d0e4721b5a59e93823803a9b6f308434e8f807b4d2c97d1955f57"
MANIFEST_SHA256 = "95564cb152d894fdb2e5daf4f89f3f5535187a86c3aa7e0370c0c83f7aedb692"
APPROVAL_MD = f"{P2}/PHASE_2C_SEMANTIC_ACCEPTANCE_RENDERER_C2_APPROVAL.md"
APPROVAL_VALIDATOR = "scripts/docs/validate-phase-2c-semantic-acceptance-renderer-c2-approval.py"
APPROVAL_PATHS = sorted([APPROVAL_MD, APPROVAL_VALIDATOR])
MANIFEST = f"{P2}/semantic-acceptance-renderer-c2-manifest.json"


def git(*args: str, binary: bool = False):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=not binary)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def object_bytes(commit: str, path: str) -> bytes:
    return git("show", f"{commit}:{path}", binary=True)


def candidate_paths() -> list[str]:
    manifest = json.loads(object_bytes(CANDIDATE, MANIFEST))
    return manifest["exact_inventory"]


def aggregate(paths: list[str]) -> str:
    entries = [{"path": p, "sha256": sha(object_bytes(CANDIDATE, p))} for p in sorted(paths)]
    body = (json.dumps(entries, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    return sha(body)


def approval_bytes(mode: str) -> bytes:
    return git("show", f":{APPROVAL_MD}", binary=True) if mode == "STAGED" else object_bytes("HEAD", APPROVAL_MD)


def main() -> int:
    head = git("rev-parse", "HEAD").strip()
    mode = "STAGED" if head == CANDIDATE else "ACCEPTED"
    if git("rev-parse", f"{CANDIDATE}^").strip() != PARENT:
        raise SystemExit("candidate parent mismatch")
    if git("rev-parse", f"{CANDIDATE}^{{tree}}").strip() != TREE:
        raise SystemExit("candidate tree mismatch")
    paths = candidate_paths()
    if len(paths) != 12 or aggregate(paths) != GIT_AGGREGATE:
        raise SystemExit("candidate inventory or Git-content aggregate mismatch")
    manifest_bytes = object_bytes(CANDIDATE, MANIFEST)
    manifest = json.loads(manifest_bytes)
    if sha(manifest_bytes) != MANIFEST_SHA256 or manifest["generated_payload_aggregate_sha256"] != GENERATED_AGGREGATE:
        raise SystemExit("manifest identity mismatch")
    if manifest["status"] != "CANDIDATE" or manifest["approval_status"] != "PENDING_HUMAN_APPROVAL":
        raise SystemExit("candidate lifecycle was mutated")
    if manifest["approval_scope"] != "ELEVEN_TYPED_CUSTOM_CONTRACT_ORIGIN_NORMALIZATIONS_ONLY":
        raise SystemExit("candidate approval scope mismatch")

    if mode == "STAGED":
        staged = sorted(git("diff", "--cached", "--name-only").splitlines())
        if staged != APPROVAL_PATHS:
            raise SystemExit("staged approval inventory mismatch")
    else:
        if git("rev-parse", "HEAD^").strip() != CANDIDATE:
            raise SystemExit("accepted commit does not directly descend from candidate")
        diff = sorted(git("diff", "--name-only", CANDIDATE, "HEAD").splitlines())
        if diff != APPROVAL_PATHS:
            raise SystemExit("candidate-to-accepted diff is not exactly two approval files")
        for path in paths:
            if object_bytes(CANDIDATE, path) != object_bytes("HEAD", path):
                raise SystemExit(f"signed candidate payload changed: {path}")

    approval = approval_bytes(mode).decode("utf-8")
    required = [
        "V23-P2C-SEMANTIC-ACCEPTANCE-RENDERER-C2", CANDIDATE, PARENT, "Decision: `APPROVED`",
        "ELEVEN_TYPED_CUSTOM_CONTRACT_ORIGIN_NORMALIZATIONS_ONLY", "Authorized Approver: `Khoa, Nguyen`",
        "Signature: `Khoa, Nguyen`", "Date: `2026-07-17`", "Timezone: `Asia/Ho_Chi_Minh`",
        TREE, GIT_AGGREGATE, GENERATED_AGGREGATE, MANIFEST_SHA256,
    ]
    if any(item not in approval for item in required):
        raise SystemExit("detached approval content mismatch")
    changed_sources = git("diff", "--name-only", PARENT, "HEAD", "--", "docs/BRD", "docs/UXF").strip()
    if changed_sources:
        raise SystemExit("BRD/UXF changed in renderer lifecycle")
    try:
        backup = git("rev-parse", "refs/ysim-backups/v2.3/phase-2c-document-baseline-c6-opaque-origin-blocked").strip()
        if backup != "c8222c506d784c278d6c7bff4c27572bcf39c7e3":
            raise SystemExit("blocked C6 preservation changed")
    except subprocess.CalledProcessError:
        pass
    print("VALID_APPROVED_PHASE_2C_SEMANTIC_ACCEPTANCE_RENDERER_C2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
