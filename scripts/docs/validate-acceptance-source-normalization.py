#!/usr/bin/env python3
"""Validate deterministic source-normalization and the true semantic gap."""

from __future__ import annotations

import json
import sys
from pathlib import Path


P2 = Path(__file__).resolve().parents[2] / "docs/baselines/v2.3/phase-2"


def main() -> int:
    mapping = json.loads((P2 / "acceptance-mapping-c3.json").read_text())
    plans = json.loads((P2 / "acceptance-source-normalization-plan.json").read_text())
    decisions = json.loads((P2 / "acceptance-mapping-archetype-decisions.json").read_text())
    normalization_ids = {row["requirement_id"] for row in mapping["mappings"] if row["disposition"] == "DETERMINISTIC_SOURCE_NORMALIZATION_REQUIRED"}
    plan_ids = {row["requirement_id"] for row in plans["plans"]}
    if plans["plan_count"] != 41 or plan_ids != normalization_ids:
        print(f"FAIL — expected 41 deterministic normalization records, got {plans['plan_count']}", file=sys.stderr)
        return 1
    for item in plans["plans"]:
        required = ("current_source_range", "corrected_source_range", "corrected_effective_statement", "source_fingerprint", "deterministic_transformation", "expected_mapping_after_normalization", "contract_preview")
        if any(not item.get(key) for key in required) or item["source_application_status"] != "NOT_YET_APPLIED":
            print(f"FAIL — incomplete source normalization: {item['requirement_id']}", file=sys.stderr)
            return 1
    ws04 = next((item for item in plans["plans"] if item["requirement_id"] == "BRD-WS-04-R012"), None)
    if not ws04 or ws04["deterministic_transformation"] != "EXPAND_RANGE_AND_RETIRE_EXAMPLE_EXTRACTION":
        print("FAIL — BRD-WS-04-R012 is not treated as an extraction/example defect", file=sys.stderr)
        return 1
    pre = next((item for item in decisions["decisions"] if item["decision_id"] == "P2C-AC-C3-DEC-PREFULFILLMENT"), None)
    if not pre or set(pre["affected_requirements"]) != {"BD-05-016", "BRD-WS-05-R021"} or len(pre["options"]) != 3:
        print("FAIL — Pre-Fulfillment business semantic decision is incomplete", file=sys.stderr)
        return 1
    labels = {option["label"] for option in pre["options"]}
    if labels != {"FULL_COMMERCIAL_ELIGIBILITY", "PRICING_MARGIN_APPROVAL_ONLY", "BLOCK_UNDEFINED_BUSINESS_TERM"}:
        print("FAIL — Pre-Fulfillment options mismatch", file=sys.stderr)
        return 1
    print("PASS — VALID_ACCEPTANCE_SOURCE_NORMALIZATION_C3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
