#!/usr/bin/env python3
"""Reject C5/C6/C6-R1 false acceptance and accept explicit progressive state."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any, Iterator


ROOT = Path(__file__).resolve().parents[2]
CURRENT = ROOT / "docs/baselines/v2.3/phase-2/phase-2c-progressive-document-baseline-c1-registry.json"
CASES = {
    "C5": ("refs/ysim-backups/v2.3/phase-2c-document-baseline-c5-generic-rendering-rejected", "docs/baselines/v2.3/phase-2/phase-2c-document-baseline-c5-registry.json"),
    "C6": ("refs/ysim-backups/v2.3/phase-2c-document-baseline-c6-opaque-origin-blocked", "docs/baselines/v2.3/phase-2/phase-2c-document-baseline-c6-registry.json"),
    "C6_R1": ("refs/ysim-backups/v2.3/phase-2c-document-baseline-c6-r1-rejected", "docs/baselines/v2.3/phase-2/phase-2c-document-baseline-c6-r1-registry.json"),
}


def strings(value: Any) -> Iterator[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from strings(child)


def load_ref(ref: str, path: str) -> dict[str, Any]:
    tree = subprocess.check_output(["git", "rev-parse", f"{ref}^{{tree}}"], cwd=ROOT, text=True).strip()
    return json.loads(subprocess.check_output(["git", "show", f"{tree}:{path}"], cwd=ROOT))


def defects(registry: dict[str, Any]) -> dict[str, int]:
    active = [r for r in registry["requirements"] if r["record_kind"] == "CANONICAL_ATOMIC" and r["scope_status"] == "V2.3_ACTIVE"]
    opaque = expected_derived = generic_boundary = generic_procedure = 0
    for record in active:
        contract = record.get("acceptance_contract") or {}
        values = "\n".join(strings(contract))
        opaque += bool(re.search(r"YSIM\.(?:C5|C6|C99)\..*SEMANTIC_IDENTIFIER", values))
        bindings = contract.get("concrete_bindings")
        if isinstance(bindings, dict):
            expected = bindings.get("expected_operand")
            observed = bindings.get("observed_operand")
            if isinstance(expected, dict) and isinstance(observed, dict):
                expected_derived += observed.get("display_value") == "observed " + str(expected.get("display_value"))
        generic_boundary += "must not be credited with" in values
        procedure = contract.get("human_verification_procedure")
        if isinstance(procedure, dict):
            action = " ".join(procedure.get("exact_actions", [])) + str(procedure.get("exact_action", ""))
            generic_procedure += any(term in action for term in ("Construct the source-defined scenario", "evaluate ", "through operator REQUIRE"))
    return {"opaque": opaque, "expected_derived": expected_derived, "generic_boundary": generic_boundary, "generic_procedure": generic_procedure}


def main() -> None:
    results = {name: defects(load_ref(ref, path)) for name, (ref, path) in CASES.items()}
    if not sum(results["C5"].values()):
        raise SystemExit("C5 false-pass regression did not reject")
    if results["C6"]["opaque"] < 11:
        raise SystemExit("C6 opaque-origin regression did not reject all eleven")
    if results["C6_R1"]["expected_derived"] != 910 or results["C6_R1"]["opaque"] < 27:
        raise SystemExit("C6-R1 systemic regression did not reject")
    current = json.loads(CURRENT.read_text(encoding="utf-8"))
    active = [r for r in current["requirements"] if r["record_kind"] == "CANONICAL_ATOMIC" and r["scope_status"] == "V2.3_ACTIVE"]
    pending = [r for r in active if r["acceptance_status"] == "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"]
    if len(pending) != 1093 or any(r["acceptance_contract"]["acceptance_content"] is not None for r in pending):
        raise SystemExit("progressive pending state invalid")
    if defects(current) != {"opaque": 0, "expected_derived": 0, "generic_boundary": 0, "generic_procedure": 0}:
        raise SystemExit("progressive state retains rejected acceptance")
    print("VALID_PHASE_2C_PROGRESSIVE_REGRESSIONS_C5_C6_C6_R1_REJECTED")


if __name__ == "__main__":
    main()
