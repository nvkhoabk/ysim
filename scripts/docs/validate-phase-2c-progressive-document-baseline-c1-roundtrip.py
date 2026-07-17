#!/usr/bin/env python3
"""Independently validate source/registry round-trip and fingerprints."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-registry.json"
BEGIN = "<!-- YSIM:REQUIREMENT BEGIN -->"
END = "<!-- YSIM:REQUIREMENT END -->"
OUTER = re.compile(r"<!-- YSIM:REQUIREMENT BEGIN -->\n(.*?)<!-- YSIM:REQUIREMENT END -->", re.S)
INNER = re.compile(r"```json\n(.*?)\n```", re.S)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"INVALID_PHASE_2C_PROGRESSIVE_ROUNDTRIP: {message}")


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    expected = {record["stable_id"]: record for record in registry["requirements"]}
    found = {}
    source_paths = sorted((ROOT / "docs/BRD").glob("*.md")) + sorted((ROOT / "docs/UXF").glob("*.md"))
    require(len(source_paths) == 31, "source document count")
    range_count = fingerprint_count = 0
    for path in source_paths:
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        for block in OUTER.findall(text):
            match = INNER.search(block)
            require(match is not None, f"JSON block {path}")
            record = json.loads(match.group(1))
            rid = record["stable_id"]
            require(rid not in found, f"duplicate {rid}")
            found[rid] = record
            line_match = re.fullmatch(r"L(\d+)-L(\d+)", record["provenance"]["source_lines"])
            require(line_match is not None, f"line syntax {rid}")
            start, end = map(int, line_match.groups())
            segment = "\n".join(lines[start - 1 : end])
            require(rid in segment and record["normative_statement"] in segment, f"line range {rid}")
            range_count += 1
            require(hashlib.sha256(record["normative_statement"].encode()).hexdigest() == record["provenance"]["source_fingerprint"], f"fingerprint {rid}")
            fingerprint_count += 1
    require(found == expected, "registry/source object mismatch")
    require(range_count == 1326 and fingerprint_count == 1326, "round-trip counts")
    print("VALID_PHASE_2C_PROGRESSIVE_DOCUMENT_BASELINE_C1_ROUNDTRIP_1326")


if __name__ == "__main__":
    main()
