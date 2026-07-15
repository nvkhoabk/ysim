#!/usr/bin/env python3
"""Validate Semantic Oracle Model C2 identity, catalog, adapters and accounting."""

from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"
BASE = "a90476e8b053bf86c11638477736c8c418a33025"
CANDIDATE = "V23-P2C-SEMANTIC-ORACLE-MODEL-C2"
C1_TREE = "e7fe153e8402ca9d7a3ec7832a9d1df9f438a3bf"
C1_REF = "refs/ysim-backups/v2.3/phase-2c-semantic-oracle-model-c1-rejected"
C4_TREE = "ef678c7da248f3595ac01cd585355469b12d76b0"
C4_REF = "refs/ysim-backups/v2.3/phase-2c-document-baseline-c4-blocked"
C4_STASH = "90bc3cac386163430d78bf7c6a346e189cd55459"


def module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    assert spec.loader
    spec.loader.exec_module(value)
    return value


ENGINE = module("semantic_oracle_engine_validate", ROOT / "scripts/docs/semantic-oracle-engine.py")


def load(name: str) -> Any:
    return json.loads((P2 / name).read_text())


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    if git("rev-parse", "HEAD") != BASE:
        fail("candidate must be validated on accepted mapping-decision HEAD")
    if git("rev-parse", f"{C1_REF}^{{tree}}") != C1_TREE:
        fail("rejected C1 index backup changed")
    if git("rev-parse", C4_REF) != C4_STASH or git("rev-parse", f"{C4_REF}^2^{{tree}}") != C4_TREE:
        fail("blocked C4 preservation changed")
    subprocess.run([sys.executable, "scripts/docs/build-semantic-oracle-model.py", "--check"], cwd=ROOT, check=True)

    catalog = load("oracle-operator-catalog.json")
    schema = load("contract-ast-schema.json")
    profiles = load("profile-oracle-adapters.json")
    archetypes = load("archetype-oracle-adapters.json")
    dry = load("semantic-oracle-dry-run.json")
    refs = load("semantic-oracle-reference-contracts.json")
    decisions = load("semantic-oracle-human-mapping-decisions.json")
    manifest = load("semantic-oracle-model-manifest.json")

    if (manifest["candidate_id"], manifest["status"], manifest["approval_status"]) != (CANDIDATE, "CANDIDATE", "PENDING_HUMAN_APPROVAL"):
        fail("candidate identity/state mismatch")
    if manifest["supersession_reason"] != "NON_EXECUTABLE_METADATA_DERIVED_MUTATION_RESULTS":
        fail("supersession reason mismatch")
    if manifest["approval_scope"] != "EXECUTABLE_SEMANTIC_ORACLE_ENGINE_OPERATOR_CATALOG_AND_REFERENCE_EVALUATION_MODEL":
        fail("approval scope mismatch")
    if manifest["next_gate"] != "HUMAN_SEMANTIC_ORACLE_MODEL_C2_APPROVAL" or manifest["blocker"] != "SEMANTIC_ORACLE_MODEL_NOT_APPROVED":
        fail("gate/blocker mismatch")
    if manifest["final_brd_uxf_baseline"] != "NOT_APPROVED" or manifest["yadf"] != "NOT_AUTHORIZED":
        fail("non-claims missing")

    operators = {item["operator_id"]: item for item in catalog["operators"]}
    if len(operators) != catalog["operator_count"] or set(operators) != set(ENGINE.EVALUATORS) or len(operators) != 40:
        fail("40-operator/evaluator registry mismatch")
    if catalog["fallback_operator"] is not None or catalog["execution_contract"]["mutation_results"] != "EXECUTION_DERIVED_ONLY":
        fail("catalog fallback or result-source contract invalid")
    for operator_id, operator in operators.items():
        if len(operator["valid_examples"]) < 2 or not operator["invalid_counterexamples"]:
            fail(f"operator examples incomplete: {operator_id}")
        if not operator["required_bindings"] or not operator["required_evidence_schema"]["required"]:
            fail(f"operator binding/evidence contract incomplete: {operator_id}")
        templates = operator["rendering_templates"]
        if len(set(templates.values())) != 3:
            fail(f"operator oracle purposes not distinct: {operator_id}")
        tokens = set(re.findall(r"\{([A-Za-z0-9_]+)\}", json.dumps(templates)))
        if not tokens <= set(operator["required_bindings"] + operator["optional_bindings"]):
            fail(f"undeclared rendering binding: {operator_id}")
        if any(not any("{" + name + "}" in text for name in operator["required_bindings"]) for text in templates.values()):
            fail(f"rendering does not materialize a required binding: {operator_id}")

    if schema["additionalProperties"] is not False:
        fail("AST schema not strict")
    if set(schema["properties"]["assertions"]["items"]["properties"]["operator_id"]["enum"]) != set(operators):
        fail("AST schema operator enum mismatch")
    mutation_properties = schema["properties"]["mutations"]["items"]["properties"]
    if "actual_detection" in mutation_properties or "expected_detection" in mutation_properties:
        fail("AST mutation definitions may not pre-mark detection")

    if profiles["profile_count"] != 31 or profiles["binding_schema_variants_normalized"] != 12:
        fail("profile adapter accounting mismatch")
    if archetypes["accepted_archetype_adapter_count"] != 57 or archetypes["candidate_archetype_adapter_count"] != 9 or archetypes["candidate_archetype_affected_records"] != 156:
        fail("archetype adapter accounting mismatch")
    for adapter in profiles["adapters"] + archetypes["adapters"]:
        if not adapter["operator_composition"] or not set(adapter["operator_composition"]) <= set(operators):
            fail("adapter operator composition invalid")
        for operator_id in adapter["operator_composition"]:
            if set(adapter["operator_binding_contract"][operator_id]) != set(operators[operator_id]["required_bindings"]):
                fail(f"adapter binding schema incomplete: {adapter.get('profile_id') or adapter.get('archetype_id')}:{operator_id}")

    account = dry["accounting"]
    if (account["registry_records"], account["canonical_atomic"], account["active_atomic"], account["inactive_atomic"]) != (1326, 1263, 1152, 111):
        fail("dry-run population mismatch")
    expected = {"CUSTOM_AST_REQUIRED": 59, "HUMAN_OPERATOR_MAPPING_REVIEW": 27, "HUMAN_PROCEDURE_REQUIRED": 156, "MODEL_EXECUTABLE_RUNTIME_ADAPTER_PENDING": 910}
    if account["dispositions"] != expected or account["fully_model_executable"] != 0 or account["reusable_high_risk_subset_of_custom"] != 48:
        fail(f"honest coverage accounting mismatch: {account['dispositions']}")
    if dry["honest_coverage"] != {"fully_model_executable":0,"model_executable_runtime_adapter_pending":910,"human_procedure_required":156,"custom_ast_required":59,"human_mapping_review":27,"source_semantics_blocked":0,"invalid_or_blocked":0,"custom_ast_reusable_high_risk_subset":48}:
        fail("explicit honest execution/runtime/human coverage mismatch")
    if len(dry["mappings"]) != 1152 or len({item["requirement_id"] for item in dry["mappings"]}) != 1152 or len(dry["inactive"]) != 111:
        fail("dry-run identities not exhaustive/disjoint")
    if any(item["mutation_score"] is not None or item["materialized_ast"] != "NOT_MATERIALIZED" for item in dry["mappings"]):
        fail("dry-run falsely claims requirement mutation/materialization")
    if dry["execution_claims"]["product_runtime_mutation"] != "NOT_EXECUTED_RUNTIME_ADAPTER_PENDING":
        fail("runtime execution non-claim missing")

    if decisions["decision_count"] != 27 or decisions["selected_count"] != 0 or len(decisions["decisions"]) != 27:
        fail("27 pending human decisions mismatch")
    if any(item["selection_status"] != "PENDING" or item["selected_option_id"] is not None for item in decisions["decisions"]):
        fail("human decision was selected")
    if refs["reference_count"] != 16 or refs["retained_semantic_pass"] != 13 or refs["reclassified_human_review"] != 3:
        fail("reference accounting mismatch")
    forbidden = re.compile(r"SOURCE_GROUNDED_|BOUND_|works as expected|handled correctly|appropriate error|derive later", re.I)
    for ref in refs["contracts"]:
        if ref["semantic_status"] == "RETAINED_EXECUTABLE":
            if not ref["operator_composition"] or not ref["execution_records"]:
                fail(f"retained reference incomplete: {ref['reference_id']}")
            if any(item["actual_detection"] != "KILLED" for item in ref["execution_records"]):
                fail(f"retained reference survivor: {ref['reference_id']}")
            if forbidden.search(json.dumps(ref["rendered_oracles"], ensure_ascii=False)):
                fail(f"reference placeholder/generic rendering: {ref['reference_id']}")
        elif ref["semantic_status"] != "HUMAN_OPERATOR_MAPPING_REVIEW" or ref["execution_records"]:
            fail(f"invalid unresolved reference state: {ref['reference_id']}")
    by_reference = {item["reference_id"]: item for item in refs["contracts"]}
    pre_boundary = by_reference["pre-fulfillment-commercial-gate"]["domain_boundary_fixtures"]
    if pre_boundary["allocatable_stock_path"]["procurement_feasibility_required"] is not False or pre_boundary["procurement_path"]["payment_before_gate_pass"] is not False or pre_boundary["procurement_path"]["partial_procurement_allowed"] is not False:
        fail("pre-fulfillment stock/procurement boundary invalid")
    fallback = by_reference["runtime-configuration-fallback"]["domain_boundary_fixtures"]
    if fallback["non_critical_presentation"]["safe_fallback_used"] is not True or fallback["business_or_security_critical"]["protected_flow_allowed"] is not False:
        fail("runtime fallback criticality boundary invalid")
    retry = by_reference["retry-limit"]["domain_boundary_fixtures"]
    if retry["attempt_3"]["accepted"] is not True or retry["attempt_4"]["accepted"] is not False:
        fail("retry attempt 3/4 boundary invalid")
    relationship = by_reference["organization-relationship"]["domain_boundary_fixtures"]
    if relationship["legal_personal_data_ownership"] != "NOT_ASSERTED_BY_REQUIREMENT":
        fail("organization relationship implies legal ownership")

    if git("diff", "--name-only", "HEAD", "--", "docs/BRD", "docs/UXF"):
        fail("BRD/UXF changed")
    print("PASS — VALID_PHASE_2C_SEMANTIC_ORACLE_MODEL_C2")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, subprocess.CalledProcessError) as exc:
        print(f"FAIL — {exc}")
        raise SystemExit(1)
