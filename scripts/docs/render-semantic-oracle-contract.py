#!/usr/bin/env python3
"""Catalog-aware renderer for Semantic Oracle Model C2.

Rendering is allowed only from a catalog operator and a schema-valid concrete
fixture.  There is deliberately no requirement-type or category fallback.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "docs/baselines/v2.3/phase-2/oracle-operator-catalog.json"

GENERIC = re.compile(
    r"works?\s+as\s+expected|handled\s+correctly|appropriate\s+error|"
    r"requirement\s+(?:is|was)\s+satisfied|verify\s+the\s+business\s+rule|"
    r"derive\s+later|remains?\s+consistent|intended\s+result|suitable\s+manner|"
    r"remains?\s+acceptable|contradictory\s+outcome|permitted\s+boundary\s+outcome",
    re.I,
)


class RenderError(ValueError):
    pass


def catalog_index(catalog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["operator_id"]: item for item in catalog["operators"]}


def _concrete_values(bindings: dict[str, Any]) -> list[str]:
    values: list[str] = []
    for value in bindings.values():
        if isinstance(value, list):
            values.extend(str(item) for item in value)
        elif isinstance(value, (str, int, float)) and not isinstance(value, bool):
            values.append(str(value))
    return [value for value in values if value]


def validate_rendered_contract(contract: dict[str, Any]) -> None:
    required = {"operator_id", "bindings", "positive", "negative", "boundary", "evidence_fields"}
    if set(contract) != required:
        raise RenderError(f"RENDERED_CONTRACT_SCHEMA_MISMATCH:{sorted(required-set(contract))}")
    texts = [contract["positive"], contract["negative"], contract["boundary"]]
    if len(set(texts)) != 3:
        raise RenderError("ORACLE_PURPOSES_NOT_DISTINCT")
    if any(GENERIC.search(text) for text in texts):
        raise RenderError("GENERIC_ORACLE_REJECTED")
    values = _concrete_values(contract["bindings"])
    if any(not any(value in text for value in values) for text in texts):
        raise RenderError("ORACLE_DOES_NOT_REFERENCE_CONCRETE_BINDING")
    if not contract["evidence_fields"] or any(not str(item).strip() for item in contract["evidence_fields"]):
        raise RenderError("CONCRETE_EVIDENCE_REQUIRED")


def render(operator_id: str, bindings: dict[str, Any], evidence_fields: list[str], catalog: dict[str, Any]) -> dict[str, Any]:
    operators = catalog_index(catalog)
    if operator_id not in operators:
        raise RenderError(f"HUMAN_OPERATOR_MAPPING_REVIEW:{operator_id}")
    operator = operators[operator_id]
    required = set(operator["required_bindings"])
    if set(bindings) != required:
        raise RenderError(f"BINDING_SCHEMA_MISMATCH:{operator_id}:{sorted(required-set(bindings))}")
    try:
        rendered = {
            "operator_id": operator_id,
            "bindings": bindings,
            "positive": operator["rendering_templates"]["positive"].format(**bindings),
            "negative": operator["rendering_templates"]["negative"].format(**bindings),
            "boundary": operator["rendering_templates"]["boundary"].format(**bindings),
            "evidence_fields": evidence_fields,
        }
    except KeyError as exc:
        raise RenderError(f"BINDING_SCHEMA_MISMATCH:{operator_id}:{exc}") from exc
    validate_rendered_contract(rendered)
    return rendered


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("operator_id")
    parser.add_argument("bindings_json")
    parser.add_argument("evidence_json")
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text())
    print(json.dumps(render(args.operator_id, json.loads(args.bindings_json), json.loads(args.evidence_json), catalog), ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
