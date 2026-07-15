#!/usr/bin/env python3
"""Validate the accepted-model to Phase 2C mapping-candidate transition."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ACCEPTED_MODEL = "a989367a6f69f1a03a8269562ce43bda3968b71a"
HISTORICAL_BASE = "0df2d424e00f9cd27b8dcb6645eef827ce97b60e"
SIGNED_MODEL_PATHS = (
    "docs/baselines/v2.3/phase-2/ACCEPTANCE_CONTRACT_MODEL.md",
    "docs/baselines/v2.3/phase-2/ACCEPTANCE_MAPPING_REVIEW_PACK.md",
    "docs/baselines/v2.3/phase-2/ACCEPTANCE_PROFILE_CATALOG.md",
    "docs/baselines/v2.3/phase-2/acceptance-mapping-dry-run.json",
    "docs/baselines/v2.3/phase-2/acceptance-profile-catalog.json",
    "docs/baselines/v2.3/phase-2/acceptance-model-candidate-manifest.json",
    "docs/baselines/v2.3/phase-2/schemas/acceptance-mapping-dry-run.schema.json",
    "docs/baselines/v2.3/phase-2/schemas/acceptance-profile-catalog.schema.json",
    "scripts/docs/generate-acceptance-model-candidate.py",
    "scripts/docs/validate-acceptance-profile-catalog.py",
    "scripts/docs/validate-acceptance-mapping-dry-run.py",
    "docs/baselines/v2.3/phase-2/PHASE_2_ACCEPTANCE_MODEL_APPROVAL.md",
    "scripts/docs/validate-phase-2-acceptance-model-approval.py",
)
PROTECTED = (
    "docs/baselines/v2.3/requirements",
    "docs/baselines/v2.3/phase-2/stable-id-mapping-candidate.json",
    "docs/baselines/v2.3/phase-2/PHASE_2_DECISION_REGISTER.md",
    "docs/baselines/v2.3/phase-2/PHASE_2_HUMAN_DECISION_PACK.md",
    "docs/baselines/v2.3/phase-2/PHASE_2_HUMAN_DECISION_PACK_APPROVAL.md",
    "docs/baselines/v2.3/phase-2/phase-2-human-decisions.json",
    "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_EXCEPTION_REGISTER.md",
    "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_EXCEPTION_REVIEW_PACK.md",
    "docs/baselines/v2.3/phase-2/phase-2-criticality-exception-review.json",
    "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_DECISION_APPROVAL.md",
)


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)


def main() -> int:
    head = run("git", "rev-parse", "HEAD")
    if head.returncode or head.stdout.strip() != ACCEPTED_MODEL:
        print("FAIL — current HEAD is not the accepted Acceptance Model commit", file=sys.stderr)
        return 1
    if run("git", "merge-base", "--is-ancestor", HISTORICAL_BASE, ACCEPTED_MODEL).returncode:
        print("FAIL — historical baseline is not an ancestor", file=sys.stderr)
        return 1
    changed = run("git", "diff", "--name-only", ACCEPTED_MODEL, "--", "docs/BRD", "docs/UXF", *SIGNED_MODEL_PATHS, *PROTECTED)
    if changed.returncode or changed.stdout.strip():
        print(f"FAIL — protected transition path changed: {changed.stdout.strip()}", file=sys.stderr)
        return 1
    approval = run(sys.executable, "scripts/docs/validate-phase-2-acceptance-model-approval.py")
    if approval.returncode or approval.stdout.strip() != "VALID_APPROVED_PHASE_2C_ACCEPTANCE_MODEL":
        print(f"FAIL — accepted Acceptance Model approval failed: {approval.stdout}{approval.stderr}", file=sys.stderr)
        return 1
    for script, expected in (
        ("scripts/docs/validate-acceptance-profile-catalog.py", "PASS — VALID_ACCEPTANCE_PROFILE_CATALOG_CANDIDATE"),
        ("scripts/docs/validate-acceptance-mapping-dry-run.py", "PASS — VALID_ACCEPTANCE_MAPPING_DRY_RUN_CANDIDATE"),
    ):
        result = run(sys.executable, script)
        if result.returncode or result.stdout.strip() != expected:
            print(f"FAIL — signed model validator failed: {script}: {result.stdout}{result.stderr}", file=sys.stderr)
            return 1
    print("PASS — VALID_PHASE_2C_ACCEPTANCE_MAPPING_TRANSITION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
