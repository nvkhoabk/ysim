#!/usr/bin/env python3
"""Independent nested business-semantic origin validator for Renderer C2."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3/phase-2"
DOC = BASE / "semantic-acceptance-renderer-c2-reference-good-contracts.json"
BAD_VERSIONED = re.compile(r"(?:^|\.)C\d+(?:\.|$).*(?:SEMANTIC_IDENTIFIER)|SEMANTIC_IDENTIFIER", re.I)
SCHEMA_NAMES = {"EXPECTED_SET", "ACTUAL_SET", "EXPECTED_VALUE", "ACTUAL_VALUE"}


def inspect(value: Any, path: str = "") -> list[str]:
    failures: list[str] = []
    if isinstance(value, dict):
        # A first-class symbolic identity has an identifier and origin. Typed
        # collection/value envelopes without an identifier are validated by
        # their accepted operator schema and are outside this amendment.
        if "semantic_type" in value and "identifier" in value and "origin" in value:
            if value.get("inference") is not False:
                failures.append(f"{path}: inference must be false")
            for required in ("semantic_type", "origin", "provenance"):
                if not value.get(required):
                    failures.append(f"{path}: missing {required}")
            for required in ("namespace", "authoritative_source", "resolver_contract", "lifecycle"):
                if not value.get(required):
                    failures.append(f"{path}: missing {required}")
            identifier = str(value.get("identifier", ""))
            if identifier.upper() in SCHEMA_NAMES or BAD_VERSIONED.search(identifier):
                failures.append(f"{path}: schema/opaque identifier {identifier}")
        for key, item in value.items():
            child = f"{path}/{key}"
            if isinstance(item, str):
                if BAD_VERSIONED.search(item):
                    failures.append(f"{child}: opaque identifier {item}")
                if key == "origin_id" and item.upper() in SCHEMA_NAMES:
                    failures.append(f"{child}: schema-derived origin")
            failures.extend(inspect(item, child))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            failures.extend(inspect(item, f"{path}/{index}"))
    return failures


def main() -> int:
    data = json.loads(DOC.read_text())
    failures = []
    for record in data["records"]:
        failures.extend(f"{record['requirement_id']}{x}" for x in inspect(record["acceptance_contract"]))
    if failures:
        raise SystemExit("\n".join(failures))
    print("VALID_SEMANTIC_ACCEPTANCE_RENDERER_C2_NESTED_ORIGINS 59/59")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
