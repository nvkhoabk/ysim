#!/usr/bin/env python3
"""Validate C2 opaque-identifier false-pass regressions."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2"
PATTERN = re.compile(r"(?:^|\.)C\d+(?:\.|$).*(?:SEMANTIC_IDENTIFIER)|SEMANTIC_IDENTIFIER", re.I)


def main() -> int:
    reg = json.loads((BASE / "semantic-acceptance-renderer-c2-false-pass-regressions.json").read_text())
    if reg["old_renderer_c1_contracts_rejected"] != "11/11":
        raise SystemExit("old contracts not rejected")
    for row in reg["old_contract_results"]:
        if not row["opaque_paths"] or not all(PATTERN.search(x["value"]) for x in row["opaque_paths"]):
            raise SystemExit(f"bad old regression {row['requirement_id']}")
    for prefix in ("C5", "C6", "C99"):
        if not PATTERN.search(f"YSIM.{prefix}.RID.SEMANTIC_IDENTIFIER.DEADBEEF"):
            raise SystemExit(f"prefix bypass {prefix}")
    print("VALID_SEMANTIC_ACCEPTANCE_RENDERER_C2_FALSE_PASS_REGRESSIONS 11/11")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
