#!/usr/bin/env python3
"""Validate C3 composite-parent structural reconciliation plans."""

from __future__ import annotations

import json
import sys
from pathlib import Path


P2 = Path(__file__).resolve().parents[2] / "docs/baselines/v2.3/phase-2"


def main() -> int:
    mapping = json.loads((P2 / "acceptance-mapping-c3.json").read_text())
    plan = json.loads((P2 / "acceptance-structural-reconciliation-plan.json").read_text())
    rows = {row["requirement_id"]: row for row in mapping["mappings"] if row["disposition"] == "STRUCTURAL_RECONCILIATION_REQUIRED"}
    plans = {row["composite_parent_id"]: row for row in plan["plans"]}
    if set(rows) != set(plans) or plan["plan_count"] != len(plans):
        print("FAIL — structural plan coverage mismatch", file=sys.stderr)
        return 1
    for requirement_id, item in plans.items():
        flags = item["parent_unit_flags"]
        if any(flags.values()) or item["coverage_rule"] != "ALL_CHILDREN" or item["id_allocation_status"] != "NOT_ALLOCATED":
            print(f"FAIL — invalid composite-parent semantics: {requirement_id}", file=sys.stderr)
            return 1
        if item["proposed_new_child_ids"] or any(child["stable_id"] is not None for child in item["child_obligations"]):
            print(f"FAIL — child ID allocated prematurely: {requirement_id}", file=sys.stderr)
            return 1
        if len(item["child_obligations"]) < 2 or item["source_application_status"] != "NOT_YET_APPLIED":
            print(f"FAIL — incomplete structural plan: {requirement_id}", file=sys.stderr)
            return 1
    print("PASS — VALID_ACCEPTANCE_STRUCTURAL_RECONCILIATION_C3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
