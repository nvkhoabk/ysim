#!/usr/bin/env python3
"""Recompute and validate binding-insensitive C3 verification fingerprints."""

from __future__ import annotations

import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"


def fail(message: str) -> int:
    print(f"FAIL — {message}", file=sys.stderr)
    return 1


def main() -> int:
    spec = importlib.util.spec_from_file_location("c3gen", ROOT / "scripts/docs/generate-acceptance-mapping-c3.py")
    if spec is None or spec.loader is None:
        return fail("cannot load fingerprint implementation")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    mapping = json.loads((P2 / "acceptance-mapping-c3.json").read_text())
    shapes = json.loads((P2 / "acceptance-verification-shapes.json").read_text())
    grouped: dict[str, list[str]] = defaultdict(list)
    for row in mapping["mappings"]:
        components = module.shape_components(row)
        fingerprint = module.shape_fingerprint(components)
        if components != row["verification_shape"] or fingerprint != row["verification_shape_fingerprint"]:
            return fail(f"fingerprint recomputation mismatch: {row['requirement_id']}")
        grouped[fingerprint].append(row["requirement_id"])
        if row["disposition"] == "UNIQUE_INLINE_CONTRACT_REQUIRED" and len(grouped[fingerprint]) >= 3 and "nearest" not in row.get("unique_reason_detail", "").casefold():
            return fail(f"repeated unique shape lacks nearest-archetype safety explanation: {row['requirement_id']}")
    declared = {item["verification_shape_fingerprint"]: sorted(item["requirement_ids"]) for item in shapes["shapes"]}
    if declared != {key: sorted(value) for key, value in grouped.items()}:
        return fail("shape inventory does not match mapping")
    if shapes["shape_count"] != len(grouped):
        return fail("shape count mismatch")
    print("PASS — VALID_ACCEPTANCE_VERIFICATION_SHAPES_C3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
