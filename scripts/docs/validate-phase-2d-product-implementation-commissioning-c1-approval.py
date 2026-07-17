#!/usr/bin/env python3
"""Validate detached approval for commissioning C1 using committed Git objects."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2d"
CANDIDATE = "0d55ce58dbef66cc0f9d02db765d0ba52fd4ee59"
PARENT = "487e806f03899ebc7571d47e72055ea28236efb4"
TREE = "6faed0e044d176070d2625166b029cfca13f33bd"
CANDIDATE_ID = "V23-P2D-PRODUCT-IMPLEMENTATION-COMMISSIONING-C1"
SCOPE = "PRODUCT_IMPLEMENTATION_COMMISSIONING_CONTRACT_AND_COMMISSIONING_IMPLEMENTATION"
GENERATED = "550f9c5a3759003ed08ae285ee89ce1d503e69302c51193fb2320c9e5fae15cf"
GIT_CONTENT = "dfbde225b3d3d325e48a2afb828cc1ea13d2d0b151c9d3a000171b605e9ce497"
MANIFEST_SHA = "c5e411f004f32c2e19d18a75cc2d2005a18f49739bfe6a3b3ab8ddd02bf1caf3"
APPROVAL_FILES = sorted([
    "docs/baselines/v2.3/phase-2d/PRODUCT_IMPLEMENTATION_COMMISSIONING_C1_APPROVAL.md",
    "scripts/docs/validate-phase-2d-product-implementation-commissioning-c1-approval.py",
])


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"INVALID_APPROVED_PHASE_2D_PRODUCT_IMPLEMENTATION_COMMISSIONING_C1: {message}")


def aggregate(paths: list[str]) -> str:
    entries = [{"path": path, "sha256": hashlib.sha256(blob(CANDIDATE, path)).hexdigest()} for path in sorted(paths)]
    body = (json.dumps(entries, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()
    return hashlib.sha256(body).hexdigest()


def main() -> None:
    head = git("rev-parse", "HEAD")
    require(git("rev-parse", f"{CANDIDATE}^") == PARENT, "candidate parent")
    require(git("rev-parse", f"{CANDIDATE}^{{tree}}") == TREE, "candidate tree")
    require(git("rev-parse", "HEAD^") == CANDIDATE, "accepted direct parent")
    require(sorted(git("diff", "--name-only", f"{CANDIDATE}..{head}").splitlines()) == APPROVAL_FILES, "approval diff")
    candidate_paths = git("diff", "--name-only", f"{PARENT}..{CANDIDATE}").splitlines()
    require(len(candidate_paths) == 11, "candidate inventory")
    require(aggregate(candidate_paths) == GIT_CONTENT, "Git-content aggregate")

    manifest_path = "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-manifest.json"
    manifest_bytes = blob(CANDIDATE, manifest_path)
    manifest = json.loads(manifest_bytes)
    require(hashlib.sha256(manifest_bytes).hexdigest() == MANIFEST_SHA, "manifest hash")
    require(manifest["generated_payload_aggregate_sha256"] == GENERATED, "generated aggregate")
    require(manifest["candidate_id"] == CANDIDATE_ID, "candidate ID")
    require(manifest["status"] == "CANDIDATE" and manifest["approval_status"] == "PENDING_HUMAN_APPROVAL", "immutable candidate state")
    for path, expected in manifest["signed_file_sha256"].items():
        require(hashlib.sha256(blob(CANDIDATE, path)).hexdigest() == expected, f"candidate hash {path}")
        require(blob(CANDIDATE, path) == blob(head, path), f"candidate changed {path}")
    technology = json.loads(blob(CANDIDATE, "docs/baselines/v2.3/phase-2d/product-implementation-commissioning-c1-technology-decisions.json"))
    require(all(item["selected_option"] is None for item in technology["decisions"]), "candidate selection mutated")

    approval = (BASE / "PRODUCT_IMPLEMENTATION_COMMISSIONING_C1_APPROVAL.md").read_text(encoding="utf-8")
    required_values = [
        "APPROVED", CANDIDATE_ID, CANDIDATE, PARENT, TREE, SCOPE, "Khoa, Nguyen", GENERATED,
        GIT_CONTENT, MANIFEST_SHA, "24.18.0", "pnpm@11.13.1", "11.1.28", "5.10.0",
        "16.2.10", "19.2.7", "18.4", "postgres:18.4-bookworm", "7.8.0", "8.22.0",
        "4.1.10", "1.61.1", "5.9.3", "9.39.5", "pg_isready", "Docker Compose v2",
    ]
    for value in required_values:
        require(value in approval, f"approval value {value}")
    for decision_id in [f"TECH-COM-{number:03d}" for number in range(1, 8)]:
        require(approval.count(decision_id) == 1, f"selection {decision_id}")
    require("VS001 business acceptance is not approved." in approval, "VS001 non-claim")
    require("business seed data are not approved" in approval, "business seed non-claim")
    print("VALID_APPROVED_PHASE_2D_PRODUCT_IMPLEMENTATION_COMMISSIONING_C1")


if __name__ == "__main__":
    main()
