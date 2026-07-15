#!/usr/bin/env python3
"""Validate accepted 1.0 profiles and the unapproved 1.1 C3 extension boundary."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


P2 = Path(__file__).resolve().parents[2] / "docs/baselines/v2.3/phase-2"
ADDITIONS = {"ACP-ATOMIC_CAPABILITY_AVAILABILITY", "ACP-BUSINESS_CLASSIFICATION", "ACP-DATA_VALUE_CONSTRAINT"}


def main() -> int:
    accepted = json.loads((P2 / "acceptance-profile-catalog.json").read_text())
    candidate = json.loads((P2 / "acceptance-profile-catalog-v1.1-candidate.json").read_text())
    mapping = json.loads((P2 / "acceptance-mapping-c3.json").read_text())
    accepted_ids = {item["profile_id"] for item in accepted["profiles"]}
    candidate_by_id = {item["profile_id"]: item for item in candidate["profiles"]}
    candidate_ids = set(candidate_by_id)
    if accepted["catalog_version"] != "1.0.0-candidate.1" or candidate["catalog_version"] != "1.1.0":
        print("FAIL — profile catalog version boundary mismatch", file=sys.stderr)
        return 1
    if candidate["status"] != "CANDIDATE" or candidate["supersedes_if_approved"] != "1.0.0" or candidate_ids - accepted_ids != ADDITIONS:
        print("FAIL — profile catalog candidate additions mismatch", file=sys.stderr)
        return 1
    counts = Counter(row.get("profile_id") for row in mapping["mappings"] if row.get("profile_id"))
    if not set(counts) <= candidate_ids:
        print("FAIL — mapping references an undeclared profile", file=sys.stderr)
        return 1
    for row in mapping["mappings"]:
        profile_id = row.get("profile_id")
        if not profile_id:
            continue
        if row["disposition"] == "NEW_PROFILE_BINDING_HIGH_CONFIDENCE" and profile_id not in ADDITIONS:
            print(f"FAIL — NEW profile route is not a 1.1 addition: {row['requirement_id']}", file=sys.stderr)
            return 1
        if row["disposition"] == "EXISTING_PROFILE_BINDING_HIGH_CONFIDENCE" and profile_id not in accepted_ids:
            print(f"FAIL — EXISTING profile route is not accepted in 1.0: {row['requirement_id']}", file=sys.stderr)
            return 1
        required = {item["name"] for item in candidate_by_id[profile_id]["required_bindings"]}
        if not required <= set(row.get("bindings", {})):
            print(f"FAIL — required profile binding missing: {row['requirement_id']}", file=sys.stderr)
            return 1
    print("PASS — VALID_ACCEPTANCE_PROFILE_CATALOG_C3_BOUNDARY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
