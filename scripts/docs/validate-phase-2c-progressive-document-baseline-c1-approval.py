#!/usr/bin/env python3
"""Validate detached approval for progressive document baseline C1."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2"
CANDIDATE_ID = "V23-P2C-PROGRESSIVE-DOCUMENT-BASELINE-C1"
CANDIDATE = "dd59cb4b2b011aced670f2a319ebb2447caa732d"
PARENT = "662eeac15d8ac336c80a495ba2a1dcb4712b7fb0"
CANDIDATE_TREE = "02014f423cda7753b89508f24a7511682b9e3f2c"
SCOPE = "PROGRESSIVE_DOCUMENT_BASELINE_SOURCE_ID_SCOPE_CRITICALITY_DECISIONS_AND_ACCEPTANCE_READINESS_STATES"
SOURCE_AGGREGATE = "25da523063c6d3ab609ba98113bd8095eb853b10f0591570ccb150d8f6b58002"
REGISTRY_AGGREGATE = "34e5a3d0d0b0b81451abbf0589b9b88ad5300c1f6602d8d94e401b863c161392"
ACCEPTANCE_AGGREGATE = "6b70e4622884e5564e2ecccc6b7514a7fcbf289f99800ebff3a6eac342f3e9bc"
GENERATED_AGGREGATE = "0b7345bca6116989a387d3976cd7895967a5f82ccaf1ed82d771ec8a762ca4bf"
GIT_CONTENT_AGGREGATE = "3495a1764568618f6bc17cb70449d5f1df12de6f7627286c7c9994a02d8a1c4f"
MANIFEST_SHA256 = "1b46112c9b5dda31e7b288e572f91e2595d218ad6f3927bc1cf9c977655716a4"
MANIFEST = "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-manifest.json"
REGISTRY = "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-registry.json"
APPROVAL_MD = "docs/baselines/v2.3/phase-2/PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1_APPROVAL.md"
APPROVAL_VALIDATOR = "scripts/docs/validate-phase-2c-progressive-document-baseline-c1-approval.py"
APPROVAL_FILES = sorted([APPROVAL_MD, APPROVAL_VALIDATOR])
READY = "ACCEPTANCE_READY"
PENDING = "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
NA = "NOT_APPLICABLE_FOR_V2.3"


def git(*args: str, binary: bool = False) -> str | bytes:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, text=not binary
    ).strip() if not binary else subprocess.check_output(["git", *args], cwd=ROOT)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(
            "INVALID_APPROVED_PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1: "
            + message
        )


def object_bytes(commit: str, path: str) -> bytes:
    return git("show", f"{commit}:{path}", binary=True)  # type: ignore[return-value]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact(value: Any) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def file_aggregate(commit: str, paths: list[str]) -> str:
    body = "".join(
        f"{sha256(object_bytes(commit, path))}  {path}\n"
        for path in sorted(paths)
    ).encode("utf-8")
    return sha256(body)


def approval_bytes(mode: str) -> bytes:
    if mode == "STAGED":
        return git("show", f":{APPROVAL_MD}", binary=True)  # type: ignore[return-value]
    return object_bytes("HEAD", APPROVAL_MD)


def main() -> None:
    head = git("rev-parse", "HEAD")
    require(isinstance(head, str), "HEAD")
    mode = "STAGED" if head == CANDIDATE else "ACCEPTED"

    require(git("cat-file", "-t", CANDIDATE) == "commit", "candidate commit")
    require(git("rev-parse", f"{CANDIDATE}^") == PARENT, "candidate parent")
    require(git("rev-parse", f"{CANDIDATE}^{{tree}}") == CANDIDATE_TREE, "candidate tree")

    manifest_bytes = object_bytes(CANDIDATE, MANIFEST)
    require(sha256(manifest_bytes) == MANIFEST_SHA256, "manifest SHA-256")
    manifest = json.loads(manifest_bytes)
    candidate_paths = sorted(manifest["exact_staged_inventory"])
    require(len(candidate_paths) == 45, "candidate inventory count")
    require(
        sorted(str(git("diff", "--name-only", f"{PARENT}..{CANDIDATE}")).splitlines())
        == candidate_paths,
        "candidate inventory",
    )
    require(
        (manifest["candidate_id"], manifest["status"], manifest["approval_status"])
        == (CANDIDATE_ID, "CANDIDATE", "PENDING_HUMAN_ACCEPTANCE"),
        "immutable candidate lifecycle",
    )
    require(
        manifest["readiness"] == {READY: 59, PENDING: 1093, NA: 111},
        "readiness",
    )

    for path, expected in manifest["signed_file_sha256"].items():
        require(
            sha256(object_bytes(CANDIDATE, path)) == expected,
            f"signed candidate blob {path}",
        )

    source_paths = [
        path for path in candidate_paths
        if path.startswith(("docs/BRD/", "docs/UXF/"))
    ]
    require(len(source_paths) == 31, "source inventory")
    require(file_aggregate(CANDIDATE, source_paths) == SOURCE_AGGREGATE, "source aggregate")
    registry_bytes = object_bytes(CANDIDATE, REGISTRY)
    require(sha256(registry_bytes) == REGISTRY_AGGREGATE, "registry aggregate")
    registry = json.loads(registry_bytes)

    acceptance_rows = []
    for record in registry["requirements"]:
        if record["record_kind"] == "CANONICAL_ATOMIC":
            acceptance_rows.append(
                f"{record['stable_id']}:{sha256(compact(record['acceptance_contract']))}\n"
            )
    require(
        sha256("".join(sorted(acceptance_rows)).encode("utf-8"))
        == ACCEPTANCE_AGGREGATE,
        "acceptance aggregate",
    )
    non_manifest = [path for path in candidate_paths if path != MANIFEST]
    require(
        file_aggregate(CANDIDATE, non_manifest) == GENERATED_AGGREGATE,
        "generated aggregate",
    )
    require(
        file_aggregate(CANDIDATE, candidate_paths) == GIT_CONTENT_AGGREGATE,
        "Git-content aggregate",
    )
    for field, expected in (
        ("source_aggregate_sha256", SOURCE_AGGREGATE),
        ("registry_aggregate_sha256", REGISTRY_AGGREGATE),
        ("acceptance_aggregate_sha256", ACCEPTANCE_AGGREGATE),
        ("generated_payload_aggregate_sha256", GENERATED_AGGREGATE),
    ):
        require(manifest[field] == expected, f"manifest {field}")

    if mode == "STAGED":
        require(
            sorted(str(git("diff", "--cached", "--name-only")).splitlines())
            == APPROVAL_FILES,
            "staged approval inventory",
        )
    else:
        require(git("rev-parse", "HEAD^") == CANDIDATE, "accepted direct parent")
        require(
            sorted(str(git("diff", "--name-only", f"{CANDIDATE}..HEAD")).splitlines())
            == APPROVAL_FILES,
            "candidate to accepted diff",
        )
        for path in candidate_paths:
            require(
                object_bytes(CANDIDATE, path) == object_bytes("HEAD", path),
                f"candidate blob changed {path}",
            )

    approval = approval_bytes(mode).decode("utf-8")
    required_values = (
        CANDIDATE_ID,
        CANDIDATE,
        PARENT,
        CANDIDATE_TREE,
        SCOPE,
        SOURCE_AGGREGATE,
        REGISTRY_AGGREGATE,
        ACCEPTANCE_AGGREGATE,
        GENERATED_AGGREGATE,
        GIT_CONTENT_AGGREGATE,
        MANIFEST_SHA256,
        "Decision: `APPROVED`",
        "Authorized Approver: `Khoa, Nguyen`",
        "Signature: `Khoa, Nguyen`",
        "Date: `2026-07-17`",
        "Timezone: `Asia/Ho_Chi_Minh`",
        "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
        "Honest active acceptance gap: 1,093",
    )
    for value in required_values:
        require(value in approval, f"approval field {value}")
    for non_claim in (
        "1,093 pending acceptance contracts",
        "any vertical slice",
        "source-code implementation",
        "runtime adapter",
        "YADF production work",
        "deployment",
    ):
        require(non_claim in approval, f"non-claim {non_claim}")

    print("VALID_APPROVED_PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1")


if __name__ == "__main__":
    main()
