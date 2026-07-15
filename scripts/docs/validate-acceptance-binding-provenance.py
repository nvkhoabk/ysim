#!/usr/bin/env python3
"""Validate binding-level provenance for all materialized C3 mappings."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"
BINDING_ROUTES = {
    "EXISTING_PROFILE_BINDING_HIGH_CONFIDENCE",
    "NEW_PROFILE_BINDING_HIGH_CONFIDENCE",
    "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE",
    "UNIQUE_INLINE_CONTRACT_REQUIRED",
}
REQUIRED = {"binding_name", "bound_value", "provenance_type", "source_document", "source_section", "source_lines", "approved_decision_ids", "source_fingerprint", "derivation_rule", "inference"}


def main() -> int:
    data = json.loads((P2 / "acceptance-mapping-c3.json").read_text())
    for row in data["mappings"]:
        if row["disposition"] not in BINDING_ROUTES:
            continue
        bindings = row.get("bindings") or {}
        provenance = row.get("binding_provenance") or []
        by_name = {item.get("binding_name"): item for item in provenance}
        if not bindings or set(by_name) != set(bindings):
            print(f"FAIL — binding provenance coverage mismatch: {row['requirement_id']}", file=sys.stderr)
            return 1
        for name, value in bindings.items():
            item = by_name[name]
            if not REQUIRED <= set(item) or item["bound_value"] != value or item["inference"] is not False:
                print(f"FAIL — invalid binding provenance: {row['requirement_id']}:{name}", file=sys.stderr)
                return 1
            if not item["source_document"] or not item["source_fingerprint"] or not item["derivation_rule"]:
                print(f"FAIL — ungrounded binding provenance: {row['requirement_id']}:{name}", file=sys.stderr)
                return 1
    print("PASS — VALID_ACCEPTANCE_BINDING_PROVENANCE_C3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
