#!/usr/bin/env python3
"""False-pass regressions for C4 generic contracts and C1 metadata kills."""

from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"
C4_REF = "refs/ysim-backups/v2.3/phase-2c-document-baseline-c4-blocked"


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    assert spec.loader
    spec.loader.exec_module(value)
    return value


RENDERER = module("semantic_oracle_renderer_regression", ROOT / "scripts/docs/render-semantic-oracle-contract.py")


def main() -> int:
    registry = json.loads(subprocess.check_output(["git", "show", f"{C4_REF}^2:docs/baselines/v2.3/phase-2/phase-2c-final-registry.json"], cwd=ROOT))
    active = [item for item in registry["requirements"] if item["record_kind"] == "CANONICAL_ATOMIC" and item["scope_status"] == "V2.3_ACTIVE"]
    contracts = [case for item in active for case in item["acceptance_contract"]]
    positive_templates: Counter[str] = Counter()
    for item in active:
        positive = next(case for case in item["acceptance_contract"] if case["case"] == "POSITIVE")
        normalized = re.sub(r"'[^']*'", "'<BINDING>'", positive["then"])
        normalized = re.sub(r"\b[A-Z]{2,}(?:-[A-Z0-9]+)+\b", "<ID>", normalized)
        positive_templates[normalized] += 1
    counts = {
        "generic_negative": sum("the contradictory outcome is rejected, denied, blocked, challenged" in case["then"].casefold() for case in contracts if case["case"] == "NEGATIVE_FAIL_CLOSED"),
        "generic_boundary": sum("the system distinguishes the permitted boundary outcome" in case["then"].casefold() for case in contracts if case["case"] == "BOUNDARY_OR_FAILURE"),
        "generic_positive": positive_templates["the bound policy or conformance evaluation for '<BINDING>' records the exact decision, resulting business state, qualifier, reason, and observable outcome"],
        "generic_evidence": sum(next(case for case in item["acceptance_contract"] if case["case"] == "POSITIVE")["observable_evidence"] == "policy or conformance decision, before/after business state, exact result, reason, and customer/operator-visible evidence" for item in active),
    }
    if counts != {"generic_negative":1146,"generic_boundary":1146,"generic_positive":373,"generic_evidence":422}:
        raise AssertionError(f"preserved C4 regression population changed: {counts}")

    paraphrases = [
        "The operation produces the intended result.",
        "Invalid input is dealt with in a suitable manner.",
        "Evidence demonstrates that behavior remains acceptable.",
    ]
    for text in paraphrases:
        contract = {"operator_id":"CAPABILITY_AVAILABLE","bindings":{},"positive":text,"negative":text + " Negative.","boundary":text + " Boundary.","evidence_fields":[]}
        try:
            RENDERER.validate_rendered_contract(contract)
        except RENDERER.RenderError:
            continue
        raise AssertionError(f"generic paraphrase accepted: {text}")

    references = json.loads((P2 / "semantic-oracle-reference-contracts.json").read_text())
    forbidden = re.compile(r"SOURCE_GROUNDED_|BOUND_|works as expected|handled correctly|appropriate error|derive later|intended result|suitable manner|remains acceptable", re.I)
    if forbidden.search(json.dumps([item["rendered_oracles"] for item in references["contracts"]], ensure_ascii=False)):
        raise AssertionError("C2 retained references contain placeholder/generic prose")
    execution = json.loads((P2 / "semantic-oracle-execution-results.json").read_text())
    if execution["result_source"] != "EXECUTION_DERIVED_ONLY" or execution["runtime_mutation_score"] is not None:
        raise AssertionError("metadata-derived or runtime false-pass regression")
    print("PASS — VALID_PHASE_2C_SEMANTIC_ORACLE_FALSE_PASS_REGRESSIONS_C2")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL — {exc}")
        raise SystemExit(1)
