#!/usr/bin/env python3
"""Audit C3 rendered positive, negative, boundary and evidence previews."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


P2 = Path(__file__).resolve().parents[2] / "docs/baselines/v2.3/phase-2"
ROUTES = {"EXISTING_PROFILE_BINDING_HIGH_CONFIDENCE", "NEW_PROFILE_BINDING_HIGH_CONFIDENCE", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE", "UNIQUE_INLINE_CONTRACT_REQUIRED"}
FIELDS = ("positive_oracle", "negative_oracle", "boundary_failure_oracle", "expected_evidence", "requirement_specific_bindings")
FORBIDDEN = re.compile(r"works as expected|handled correctly|appropriate error|requirement is satisfied|verify the business rule|derive negative later|derive later|SOURCE_BOUND_ACTION", re.I)


def check_preview(label: str, preview: dict) -> str | None:
    if not preview or any(not preview.get(field) for field in FIELDS):
        return f"missing rendered oracle/evidence: {label}"
    text = " ".join(str(preview[field]) for field in FIELDS[:-1])
    if FORBIDDEN.search(text):
        return f"generic/default marker in rendered preview: {label}"
    bindings = preview["requirement_specific_bindings"]
    if not isinstance(bindings, dict) or not bindings:
        return f"requirement-specific bindings missing: {label}"
    return None


def main() -> int:
    mapping = json.loads((P2 / "acceptance-mapping-c3.json").read_text())
    decisions = json.loads((P2 / "acceptance-mapping-archetype-decisions.json").read_text())
    source = json.loads((P2 / "acceptance-source-normalization-plan.json").read_text())
    structural = json.loads((P2 / "acceptance-structural-reconciliation-plan.json").read_text())
    for row in mapping["mappings"]:
        graph_text = " ".join((str(row["obligation_graph"].get("failure_mode", "")), " ".join(row["obligation_graph"].get("action_or_capability", []))))
        if FORBIDDEN.search(graph_text):
            print(f"FAIL — default or unclassified graph marker: {row['requirement_id']}", file=sys.stderr)
            return 1
        if row["disposition"] in ROUTES:
            error = check_preview(row["requirement_id"], row.get("rendered_contract_preview"))
            if error:
                print(f"FAIL — {error}", file=sys.stderr)
                return 1
        if row["disposition"] == "UNIQUE_INLINE_CONTRACT_REQUIRED":
            if not row.get("unique_reason") or not row.get("unique_reason_detail") or row["obligation_graph"]["prohibited_outcome"] == "NOT_EXPLICIT_IN_SOURCE":
                print(f"FAIL — incomplete unique-inline semantics: {row['requirement_id']}", file=sys.stderr)
                return 1
            if "nearest" not in row["unique_reason_detail"].casefold():
                print(f"FAIL — nearest reusable structure exclusion missing: {row['requirement_id']}", file=sys.stderr)
                return 1
    for decision in decisions["decisions"]:
        for option in decision["options"]:
            error = check_preview(option["option_id"], option.get("contract_preview"))
            if error:
                print(f"FAIL — {error}", file=sys.stderr)
                return 1
    for item in source["plans"]:
        error = check_preview(item["requirement_id"], item.get("contract_preview"))
        if error:
            print(f"FAIL — {error}", file=sys.stderr)
            return 1
    for item in structural["plans"]:
        preview = item.get("contract_preview") or {}
        if any(not preview.get(field) for field in ("positive_oracle", "negative_oracle", "boundary_failure_oracle", "expected_evidence")):
            print(f"FAIL — structural preview incomplete: {item['composite_parent_id']}", file=sys.stderr)
            return 1
    print("PASS — VALID_ACCEPTANCE_RENDERED_CONTRACTS_C3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
