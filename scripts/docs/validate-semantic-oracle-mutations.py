#!/usr/bin/env python3
"""Recompute C2 mutation results through evaluator execution."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    assert spec.loader
    spec.loader.exec_module(value)
    return value


ENGINE = module("semantic_oracle_engine_mutations", ROOT / "scripts/docs/semantic-oracle-engine.py")


def main() -> int:
    catalog = json.loads((P2 / "oracle-operator-catalog.json").read_text())
    stored = json.loads((P2 / "semantic-oracle-execution-results.json").read_text())
    conformance = ENGINE.run_operator_conformance(catalog)
    adversarial = ENGINE.run_adversarial(catalog)
    challenges = ENGINE.run_independent_challenges(catalog)
    if conformance != stored["model_conformance"] or adversarial != stored["adversarial"] or challenges != stored["independent_challenges"]:
        raise AssertionError("stored execution result differs from evaluator recomputation")
    for key in ("custom_and_high_risk_operator_model_probes", "criticality_stratified_operator_model_probes"):
        sample = [{field: row[field] for field in ("requirement_id", "criticality", "coverage_disposition", "operator_id")} for row in stored[key]["rows"]]
        if ENGINE.run_mapping_model_probes(catalog, sample) != stored[key]:
            raise AssertionError(f"stored {key} differs from evaluator recomputation")
    if conformance["operator_count"] != 40 or conformance["passed"] != 40:
        raise AssertionError("40/40 operator conformance not passed")
    if adversarial["total"] != 10 or adversarial["passed"] != 10:
        raise AssertionError("10/10 adversarial fail-closed gate not passed")
    if challenges["generated"] != 42 or challenges["killed"] != 42 or challenges["survived"] != 0 or len({item["operator_id"] for item in challenges["rows"]}) != 40:
        raise AssertionError("independent model challenge survivors")
    for row in conformance["rows"]:
        if any(item["original_sha256"] == item["mutant_sha256"] for item in row["execution_records"]):
            raise AssertionError(f"no-op hash accepted: {row['operator_id']}")
        if any(item["actual_detection"] != "KILLED" or not item["baseline"]["passed"] or item["mutant"]["passed"] for item in row["execution_records"]):
            raise AssertionError(f"false killed: {row['operator_id']}")
    refs = json.loads((P2 / "semantic-oracle-reference-contracts.json").read_text())
    operators = {item["operator_id"]: item for item in catalog["operators"]}
    for ref in refs["contracts"]:
        if ref["semantic_status"] != "RETAINED_EXECUTABLE":
            continue
        expected = []
        for fixture in ref["fixtures"]:
            definitions = ENGINE.conformance_mutations(fixture)
            if ref["reference_id"] == "retry-limit" and fixture["operator_id"] == "RETRY_LIMIT_NOT_EXCEEDED":
                definitions[0]["mutated_value"] = 4
            expected.extend(ENGINE.execute_mutation(fixture, mutation, operators) for mutation in definitions)
        if expected != ref["execution_records"]:
            raise AssertionError(f"reference execution not reproducible: {ref['reference_id']}")
    if stored["runtime_adapter_execution"] != "NOT_EXECUTED" or stored["runtime_mutation_score"] is not None or stored["false_killed"] != 0:
        raise AssertionError("runtime/non-execution accounting is dishonest")
    if stored["custom_and_high_risk_operator_model_probes"]["sample_size"] != 59 or stored["criticality_stratified_operator_model_probes"]["sample_size"] != 60:
        raise AssertionError("custom/high-risk or stratified model-probe population mismatch")
    print("PASS — VALID_EXECUTED_PHASE_2C_SEMANTIC_ORACLE_MUTATIONS_C2")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL — {exc}")
        raise SystemExit(1)
