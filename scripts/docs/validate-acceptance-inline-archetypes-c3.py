#!/usr/bin/env python3
"""Validate the C3 inline-archetype catalog against its mapped population."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


P2 = Path(__file__).resolve().parents[2] / "docs/baselines/v2.3/phase-2"
REQUIRED = {"archetype_id", "version", "mapping_count", "semantic_intent", "required_bindings", "prohibited_uses", "positive_case_structure", "negative_case_structure", "boundary_failure_case_structure", "evidence_structure", "anti_generic_rule", "counterexample_rule"}


def main() -> int:
    mapping = json.loads((P2 / "acceptance-mapping-c3.json").read_text())
    catalog = json.loads((P2 / "acceptance-inline-archetype-catalog.json").read_text())
    counts = Counter(row.get("inline_archetype_id") for row in mapping["mappings"] if row.get("inline_archetype_id"))
    declared = {item["archetype_id"]: item for item in catalog["archetypes"]}
    if catalog["version"] != "1.1.0-candidate.3" or set(counts) != set(declared):
        print("FAIL — inline-archetype catalog/mapping mismatch", file=sys.stderr)
        return 1
    for archetype_id, item in declared.items():
        if not REQUIRED <= set(item) or item["mapping_count"] != counts[archetype_id]:
            print(f"FAIL — incomplete archetype: {archetype_id}", file=sys.stderr)
            return 1
        if len(item["required_bindings"]) < 6 or not item["prohibited_uses"] or not item["counterexample_rule"]:
            print(f"FAIL — weak archetype contract: {archetype_id}", file=sys.stderr)
            return 1
    print("PASS — VALID_ACCEPTANCE_INLINE_ARCHETYPES_C3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
