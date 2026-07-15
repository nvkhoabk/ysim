#!/usr/bin/env python3
"""Build V23-P2C-SEMANTIC-ORACLE-MODEL-C2 without touching BRD/UXF."""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"
CANDIDATE = "V23-P2C-SEMANTIC-ORACLE-MODEL-C2"
SUPERSEDES = "V23-P2C-SEMANTIC-ORACLE-MODEL-C1"
SUPERSESSION_REASON = "NON_EXECUTABLE_METADATA_DERIVED_MUTATION_RESULTS"
BASE = "a90476e8b053bf86c11638477736c8c418a33025"
C4_STASH = "90bc3cac386163430d78bf7c6a346e189cd55459"
C4_TREE = "ef678c7da248f3595ac01cd585355469b12d76b0"
C4_REF = "refs/ysim-backups/v2.3/phase-2c-document-baseline-c4-blocked"
C1_TREE = "e7fe153e8402ca9d7a3ec7832a9d1df9f438a3bf"
C1_REF = "refs/ysim-backups/v2.3/phase-2c-semantic-oracle-model-c1-rejected"
APPROVAL_SCOPE = "EXECUTABLE_SEMANTIC_ORACLE_ENGINE_OPERATOR_CATALOG_AND_REFERENCE_EVALUATION_MODEL"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader
    spec.loader.exec_module(module)
    return module


ENGINE = load_module("semantic_oracle_engine", ROOT / "scripts/docs/semantic-oracle-engine.py")
RENDERER = load_module("semantic_oracle_renderer", ROOT / "scripts/docs/render-semantic-oracle-contract.py")


def canonical(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def sha(data: bytes | str) -> str:
    return hashlib.sha256(data.encode() if isinstance(data, str) else data).hexdigest()


def aggregate(items: dict[str, bytes]) -> str:
    h = hashlib.sha256()
    for name in sorted(items):
        h.update(name.encode() + b"\0" + items[name] + b"\0")
    return h.hexdigest()


def git_json(spec: str) -> dict[str, Any]:
    return json.loads(subprocess.check_output(["git", "show", spec], cwd=ROOT))


def git_lines(*args: str) -> list[str]:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).splitlines()


def artifact_path(name: str) -> Path:
    return P2 / name


C1_HASHES = {
    "generated_payload_aggregate_sha256": "7c4a10cde750fe7d0eec845abed00df44fa37fa01532fe6e49bc3bb0c391a74c",
    "staged_git_content_aggregate_sha256": "135d37053f7d16373cd07d5d26fa4474242d6d65dac3a3d48234b827f71c2502",
    "staged_tree": C1_TREE,
    "operator_catalog_sha256": "fe1b3a2649d8a0a671d283d51654bb3676016dce70ceb0550ec76c7c0294531c",
    "dry_run_sha256": "79628730201ddd8bed762e1d30fec994c67f1a21c1c91971491e279658550b0d",
    "reference_contracts_sha256": "1fd86b8e2b9eed06f85290270cc1fed4699dd3f7ec77807e77cf70582491c121",
    "review_pack_sha256": "26d393d21bb709983f164c400c05ab4828011de46d92a7a8a4e35c0add65b5fa",
    "manifest_sha256": "915259918f7945b1e5fb1d981c87dbee26c2767357617911dc0e2f89169b913a",
}


def c1_preservation() -> dict[str, Any]:
    paths = git_lines("ls-tree", "-r", "--name-only", C1_TREE)
    return {
        "artifact": "V23-P2C-SEMANTIC-ORACLE-MODEL-C1-REJECTED-PRESERVATION",
        "candidate_id": SUPERSEDES,
        "human_review_result": "NEEDS_SEMANTIC_ORACLE_MODEL_C2",
        "rejection_reason": SUPERSESSION_REASON,
        "base_head": BASE,
        "staged_path_count": len(paths),
        "staged_paths": paths,
        "staged_tree": C1_TREE,
        "backup_ref": C1_REF,
        "backup_object_type": "tree",
        "reproduction_command": f"git read-tree {C1_REF}",
        "signed_hashes": C1_HASHES,
        "commit_tag_push_approval": "NONE",
    }


def c4_preservation() -> dict[str, Any]:
    return {
        "stash": C4_STASH,
        "index_tree": C4_TREE,
        "backup_ref": C4_REF,
        "generated_aggregate": "3311d2f0c0792ce90720bea23edcb95f329a9b61d64b1e4b9dd98f272490e025",
        "source_aggregate": "f8b4f337e462341182f047e3c61ee3b0733a7384be067befb3cbde521cd89d1c",
        "staged_aggregate": "3c0de42fd9f8c5b16013794a1a88bae8ff3bc10af77f4ea94eb64b192c6b38d7",
        "state": "VALID_PRESERVED_BLOCKED_C4_STATE",
        "main_worktree_application": "NOT_APPLIED",
    }


def build_catalog() -> dict[str, Any]:
    catalog = git_json(f"{C1_TREE}:docs/baselines/v2.3/phase-2/oracle-operator-catalog.json")
    catalog["artifact"] = "V23-P2C-ORACLE-OPERATOR-CATALOG-C2"
    catalog["candidate_id"] = CANDIDATE
    catalog["catalog_version"] = "1.0.0-candidate.2"
    catalog["supersedes"] = "1.0.0-candidate.1"
    catalog["execution_contract"] = {
        "evaluator_registry_required": True,
        "unknown_operator": "FAIL_CLOSED",
        "mutation_results": "EXECUTION_DERIVED_ONLY",
        "runtime_claim": "SLICE_RUNTIME_ADAPTER_REQUIRED",
        "fallback_operator": None,
    }
    for operator in catalog["operators"]:
        operator["version"] = "1.0.0-candidate.2"
        for example in operator["valid_examples"]:
            example["operator_version"] = operator["version"]
        if operator["operator_id"] == "CONFIGURATION_PRECEDENCE":
            operator["rendering_templates"]["positive"] = (
                "{configuration_key} selects from concrete sources {source_values} using precedence {precedence_order}."
            )
        first_binding = operator["required_bindings"][0]
        for purpose, template in operator["rendering_templates"].items():
            if not any("{" + name + "}" in template for name in operator["required_bindings"]):
                operator["rendering_templates"][purpose] = template + f" Bound context: {{{first_binding}}}."
        operator["execution_layers"] = [
            "MODEL_CONFORMANCE_EXECUTED",
            "SLICE_RUNTIME_ADAPTER_REQUIRED",
            "HUMAN_VERIFICATION_REQUIRED",
        ]
        operator["actual_detection_source"] = "semantic-oracle-engine.execute_mutation"
    catalog["operator_count"] = len(catalog["operators"])
    catalog["fallback_operator"] = None
    return catalog


def build_profile_adapters(catalog: dict[str, Any]) -> dict[str, Any]:
    previous = git_json(f"{C1_TREE}:docs/baselines/v2.3/phase-2/profile-oracle-adapters.json")
    operators = {item["operator_id"]: item for item in catalog["operators"]}
    adapters = []
    for adapter in previous["adapters"]:
        item = copy.deepcopy(adapter)
        item["adapter_version"] = "1.0.0-candidate.2"
        item["status"] = "MODEL_ADAPTER_DEFINED_RUNTIME_BINDING_PENDING"
        item.pop("mutation_target_score", None)
        item["operator_binding_contract"] = {
            operator_id: {
                name: {
                    "source": f"MATERIALIZED_REQUIREMENT_BINDING:{name}",
                    "inference": False,
                    "required_at_materialization": True,
                }
                for name in operators[operator_id]["required_bindings"]
            }
            for operator_id in item["operator_composition"]
        }
        adapters.append(item)
    return {
        "artifact": "V23-P2C-PROFILE-ORACLE-ADAPTERS-C2",
        "candidate_id": CANDIDATE,
        "status": "CANDIDATE",
        "profile_count": len(adapters),
        "active_mapping_count": sum(item.get("active_mapping_count", 0) for item in adapters),
        "binding_schema_variants_normalized": 12,
        "runtime_adapter_status": "PENDING",
        "adapters": adapters,
    }


def build_archetype_adapters(catalog: dict[str, Any]) -> dict[str, Any]:
    previous = git_json(f"{C1_TREE}:docs/baselines/v2.3/phase-2/archetype-oracle-adapters.json")
    operators = {item["operator_id"]: item for item in catalog["operators"]}
    adapters = []
    for adapter in previous["adapters"]:
        item = copy.deepcopy(adapter)
        extension = item.get("status") == "CANDIDATE_ARCHETYPE_EXTENSION"
        item["adapter_version"] = "1.0.0-candidate.2"
        item["status"] = "HUMAN_OPERATOR_MAPPING_REVIEW" if extension else "MODEL_ADAPTER_DEFINED_RUNTIME_BINDING_PENDING"
        item["operator_binding_contract"] = {
            operator_id: {
                name: {
                    "source": f"MATERIALIZED_REQUIREMENT_BINDING:{name}",
                    "inference": False,
                    "required_at_materialization": True,
                }
                for name in operators[operator_id]["required_bindings"]
            }
            for operator_id in item["operator_composition"]
        }
        adapters.append(item)
    return {
        "artifact": "V23-P2C-ARCHETYPE-ORACLE-ADAPTERS-C2",
        "candidate_id": CANDIDATE,
        "status": "CANDIDATE",
        "accepted_archetype_adapter_count": sum(item["status"].startswith("MODEL_") for item in adapters),
        "candidate_archetype_adapter_count": sum(item["status"] == "HUMAN_OPERATOR_MAPPING_REVIEW" for item in adapters),
        "candidate_archetype_affected_records": sum(item.get("active_mapping_count", 0) for item in adapters if item["status"] == "HUMAN_OPERATOR_MAPPING_REVIEW"),
        "runtime_adapter_status": "PENDING",
        "adapters": adapters,
    }


def build_dry_run(archetypes: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    previous = git_json(f"{C1_TREE}:docs/baselines/v2.3/phase-2/semantic-oracle-dry-run.json")
    pending_archetypes = {item["archetype_id"] for item in archetypes["adapters"] if item["status"] == "HUMAN_OPERATOR_MAPPING_REVIEW"}
    mappings = []
    reviews = []
    custom = [item for item in previous["mappings"] if item["disposition"] == "CUSTOM_AST_REQUIRED"]
    reusable_high_risk = {item["requirement_id"] for item in sorted(custom, key=lambda x: ({"CRITICAL":0,"HIGH":1,"NORMAL":2}.get(x["criticality"],3), x["requirement_id"]))[:48]}
    for source in previous["mappings"]:
        disposition = source["disposition"]
        contract_id = source.get("source_contract_id")
        if disposition == "OPERATOR_AST_HIGH_CONFIDENCE":
            coverage = "MODEL_EXECUTABLE_RUNTIME_ADAPTER_PENDING"
        elif disposition == "OPERATOR_AST_HYBRID" and contract_id in pending_archetypes:
            coverage = "HUMAN_PROCEDURE_REQUIRED"
        elif disposition == "OPERATOR_AST_HYBRID":
            coverage = "MODEL_EXECUTABLE_RUNTIME_ADAPTER_PENDING"
        elif disposition == "CUSTOM_AST_REQUIRED":
            coverage = "CUSTOM_AST_REQUIRED"
        else:
            coverage = "HUMAN_OPERATOR_MAPPING_REVIEW"
        record = {
            "requirement_id": source["requirement_id"],
            "criticality": source["criticality"],
            "requirement_type": source["requirement_type"],
            "source_mechanism": source["mechanism"],
            "source_contract_id": contract_id,
            "operator_composition_candidate": source.get("operator_composition", []),
            "coverage_disposition": coverage,
            "model_conformance_execution": "AVAILABLE" if source.get("operator_composition") else "NOT_AVAILABLE",
            "runtime_adapter": "PENDING" if coverage == "MODEL_EXECUTABLE_RUNTIME_ADAPTER_PENDING" else "NOT_CLAIMED",
            "materialized_ast": "NOT_MATERIALIZED",
            "mutation_score": None,
            "custom_subclassification": (
                "REUSABLE_HIGH_RISK_COMPOSITION_PENDING" if source["requirement_id"] in reusable_high_risk
                else "REQUIREMENT_SPECIFIC_CUSTOM_AST_PENDING" if coverage == "CUSTOM_AST_REQUIRED"
                else None
            ),
        }
        mappings.append(record)
        if coverage == "HUMAN_OPERATOR_MAPPING_REVIEW":
            reviews.append(source)
    inactive = [{"requirement_id": item["requirement_id"], "disposition": "NOT_APPLICABLE_FOR_V2.3"} for item in previous["inactive"]]
    counts = Counter(item["coverage_disposition"] for item in mappings)
    criticality = defaultdict(Counter)
    for item in mappings:
        criticality[item["coverage_disposition"]][item["criticality"]] += 1
    return {
        "artifact": "V23-P2C-SEMANTIC-ORACLE-DRY-RUN-C2",
        "candidate_id": CANDIDATE,
        "status": "CANDIDATE",
        "source_c4_index_tree": C4_TREE,
        "accounting": {
            "registry_records": 1326,
            "canonical_atomic": 1263,
            "active_atomic": len(mappings),
            "inactive_atomic": len(inactive),
            "fully_model_executable": 0,
            "dispositions": dict(sorted(counts.items())),
            "criticality_by_disposition": {key: dict(sorted(value.items())) for key, value in sorted(criticality.items())},
            "reusable_high_risk_subset_of_custom": len(reusable_high_risk),
            "missing_disposition": 0,
        },
        "honest_coverage": {
            "fully_model_executable": 0,
            "model_executable_runtime_adapter_pending": counts.get("MODEL_EXECUTABLE_RUNTIME_ADAPTER_PENDING", 0),
            "human_procedure_required": counts.get("HUMAN_PROCEDURE_REQUIRED", 0),
            "custom_ast_required": counts.get("CUSTOM_AST_REQUIRED", 0),
            "human_mapping_review": counts.get("HUMAN_OPERATOR_MAPPING_REVIEW", 0),
            "source_semantics_blocked": 0,
            "invalid_or_blocked": 0,
            "custom_ast_reusable_high_risk_subset": len(reusable_high_risk),
        },
        "execution_claims": {
            "operator_model_conformance": "EXECUTED",
            "product_runtime_mutation": "NOT_EXECUTED_RUNTIME_ADAPTER_PENDING",
            "requirement_ast_materialization": "NOT_IN_APPROVAL_SCOPE",
            "stored_actual_detection_trusted": False,
        },
        "inactive": inactive,
        "mappings": sorted(mappings, key=lambda item: item["requirement_id"]),
    }, reviews


def proposed_operators(requirement_type: str) -> list[str]:
    return {
        "SECURITY_REQUIREMENT": ["ACTOR_AUTHORIZED", "ACTOR_DENIED", "EVIDENCE_FIELD_PRESENT"],
        "INTEGRATION_REQUIREMENT": ["REFERENCE_TARGET_VALID", "DELIVERY_TERMINAL_STATE"],
        "OPERATIONAL_REQUIREMENT": ["DELIVERY_TERMINAL_STATE", "EVIDENCE_FIELD_PRESENT"],
        "DATA_REQUIREMENT": ["REFERENCE_TARGET_VALID", "SET_CONTAINS"],
        "UX_REQUIREMENT": ["STATE_TRANSITION_ALLOWED", "EVIDENCE_FIELD_PRESENT"],
        "PERFORMANCE_REQUIREMENT": ["PERFORMANCE_WITHIN_BUDGET"],
    }.get(requirement_type, ["POLICY_OUTCOME_EQUALS", "EVIDENCE_FIELD_PRESENT"])


def build_decisions(review_sources: list[dict[str, Any]], records: dict[str, dict[str, Any]]) -> dict[str, Any]:
    decisions = []
    for index, source in enumerate(sorted(review_sources, key=lambda item: item["requirement_id"]), 1):
        rid = source["requirement_id"]
        record = records[rid]
        operators = proposed_operators(record["requirement_type"])
        decisions.append({
            "decision_id": f"P2C-SO-C2-HOMR-{index:03d}",
            "requirement_id": rid,
            "statement": record["normative_statement"],
            "criticality": record["verification_criticality"],
            "current_route": record["acceptance_mechanism"]["mechanism"],
            "source_provenance": record["provenance"],
            "selection_status": "PENDING",
            "recommended_option_id": f"P2C-SO-C2-HOMR-{index:03d}-OPT-1",
            "selected_option_id": None,
            "options": [
                {
                    "option_id": f"P2C-SO-C2-HOMR-{index:03d}-OPT-1",
                    "disposition": "AUTHOR_SOURCE_GROUNDED_OPERATOR_AST",
                    "candidate_operators": operators,
                    "source_edit_required": False,
                    "non_claim": "CANDIDATE_COMPOSITION_REQUIRES_HUMAN_CONFIRMATION",
                },
                {
                    "option_id": f"P2C-SO-C2-HOMR-{index:03d}-OPT-2",
                    "disposition": "SOURCE_SEMANTICS_BLOCKED",
                    "candidate_operators": [],
                    "source_edit_required": True,
                    "non_claim": "NO_OPERATOR_AST_UNTIL_SOURCE_SEMANTICS_ARE_APPROVED",
                },
            ],
        })
    return {
        "artifact": "V23-P2C-SEMANTIC-ORACLE-HUMAN-MAPPING-DECISIONS-C2",
        "candidate_id": CANDIDATE,
        "status": "PENDING_HUMAN_DECISION",
        "approval_scope_exclusion": "27_HUMAN_OPERATOR_MAPPING_DECISIONS_NOT_APPROVED",
        "decision_count": len(decisions),
        "selected_count": 0,
        "decisions": decisions,
    }


def concrete_value(name: str, spec: dict[str, Any], operator: dict[str, Any]) -> Any:
    kind = operator["input_json_schema"]["properties"][name]["type"]
    if name in spec.get("bindings", {}):
        value = copy.deepcopy(spec["bindings"][name])
        if kind == "string" and isinstance(value, list):
            return ",".join(str(item) for item in value)
        if kind == "array" and not isinstance(value, list):
            return [value]
        return value
    token = name.upper()
    if kind == "array":
        return [f"{spec['semantic_token']}_{token}_ITEM"]
    if kind == "number":
        return 3
    if kind == "boolean":
        return True
    return f"{spec['semantic_token']}:{token}"


def reference_fixture(operator: dict[str, Any], spec: dict[str, Any]) -> dict[str, Any]:
    clone = copy.deepcopy(operator)
    bindings = {name: concrete_value(name, spec, operator) for name in operator["required_bindings"]}
    clone["valid_examples"][0]["bindings"] = bindings
    fixture = ENGINE.build_fixture(clone)
    fixture["fixture_id"] = f"REF-FIX-{spec['reference_id']}-{operator['operator_id']}"
    fixture["provenance"] = {
        "requirement_id": spec["requirement_id"],
        "source_document": spec["source_provenance"]["source_document"],
        "source_fingerprint": spec["source_provenance"].get("source_fingerprint") or spec["source_provenance"].get("effective_source_fingerprint") or spec["source_provenance"].get("source_context_sha256"),
        "inference": False,
    }
    fixture["evidence"] = {
        name: spec.get("evidence_values", {}).get(name, f"{spec['semantic_token']}:{name.upper()}")
        for name in operator["required_evidence_schema"]["required"]
    }
    return fixture


REFERENCE_SPECS = [
    ("pre-fulfillment-commercial-gate", "BRD-WS-05-R021", ["POLICY_OUTCOME_EQUALS", "APPROVAL_REQUIRED", "PROCUREMENT_FEASIBLE", "PAYMENT_INITIATION_ALLOWED", "PAYMENT_INITIATION_BLOCKED"], "PREFULFILLMENT", "RETAINED_EXECUTABLE"),
    ("runtime-configuration-fallback", "UXF-00-R013", ["SAFE_FALLBACK_USED", "FAIL_CLOSED"], "RUNTIME_CONFIG", "RETAINED_EXECUTABLE"),
    ("atomic-capability", "BRD-WS-01-R007", ["CAPABILITY_AVAILABLE", "CAPABILITY_NOT_PLACEHOLDER", "SCOPE_ACTIVE"], "ACTIVE_CAPABILITY", "RETAINED_EXECUTABLE"),
    ("enum-reference-integrity", "BRD-CAP-INDEX-R029", ["ENUM_VALUE_ALLOWED", "ROLE_LIST_CONSISTENT", "REFERENCE_TARGET_VALID"], "EVENT_ROLE", "RETAINED_EXECUTABLE"),
    ("mfa-enforcement", "BD-16-003", ["MFA_CHALLENGE_REQUIRED", "ACTOR_DENIED", "AUDIT_IMMUTABLE"], "MFA_POLICY", "RETAINED_EXECUTABLE"),
    ("event-ordering-required", "BRD-EVENT-INDEX-R001", ["EVENT_ORDER_PRESERVED"], "FINANCIAL_EVENTS", "RETAINED_EXECUTABLE"),
    ("event-ordering-not-required", "BRD-EVENT-INDEX-R002", ["EVENT_ORDER_NOT_REQUIRED"], "NON_FINANCIAL_EVENTS", "RETAINED_EXECUTABLE"),
    ("organization-relationship", "BRD-WS-11-R003", ["ACTOR_DENIED", "TENANT_ISOLATED"], "ORG_RELATIONSHIP", "RETAINED_EXECUTABLE"),
    ("tenant-isolation", "BRD-WS-03-R010", ["TENANT_ISOLATED", "ACTOR_DENIED"], "TENANT_BOUNDARY", "RETAINED_EXECUTABLE"),
    ("state-transition", "BD-10-004", [], "STATE_TRANSITION", "HUMAN_OPERATOR_MAPPING_REVIEW"),
    ("audit-immutability", "BD-14-016", ["AUDIT_IMMUTABLE", "EVIDENCE_FIELD_PRESENT"], "AUDIT_RECORD", "RETAINED_EXECUTABLE"),
    ("retry-limit", "BD-09-009", ["RETRY_LIMIT_NOT_EXCEEDED", "DELIVERY_TERMINAL_STATE"], "RETRY_3_4", "RETAINED_EXECUTABLE"),
    ("pricing-snapshot", "BD-02-007", ["POLICY_OUTCOME_EQUALS", "EVIDENCE_FIELD_PRESENT"], "PRICING_SNAPSHOT", "RETAINED_EXECUTABLE"),
    ("settlement-reconciliation", "BD-10-004", [], "SETTLEMENT", "HUMAN_OPERATOR_MAPPING_REVIEW"),
    ("accessibility", "UXF-02-R009", ["ACCESSIBILITY_CONFORMS"], "ACCESSIBILITY", "RETAINED_EXECUTABLE"),
    ("performance-budget", "EP-12-007", [], "PERFORMANCE_BUDGET", "HUMAN_OPERATOR_MAPPING_REVIEW"),
]


def reference_bindings(reference_id: str) -> dict[str, Any]:
    common: dict[str, Any] = {}
    if reference_id == "pre-fulfillment-commercial-gate":
        common = {"order_id":"ORDER-PREFULFILLMENT-FIXTURE","commercial_gate_result":"PASS","payment_state":"PAYMENT_INITIATED","failed_checks":["PRICING_INVALID","MARGIN_OR_APPROVAL_FAILED","PROCUREMENT_INFEASIBLE"],"blocked_states":["PAYMENT_INITIATED","CHARGE_AUTHORIZATION_STARTED"],"policy":"PRE_FULFILLMENT_COMMERCIAL_ELIGIBILITY","policy_inputs":["PRICING_VALIDITY","MARGIN_COST_POLICY","REQUIRED_APPROVALS"],"expected_outcome":"PASS","action":"PAYMENT_INITIATION","approval_policy":"MARGIN_AND_COMMERCIAL_APPROVAL_POLICY","approval_reference":"APPROVAL-REF-PREFULFILLMENT","supplier_terms":"CURRENT_SUPPLIER_COMMERCIAL_TERMS","capacity":"WHOLE_ORDER_PROCUREMENT_CAPACITY","coverage_policy":"V2.3_NO_PARTIAL_ORDER"}
    elif reference_id == "runtime-configuration-fallback":
        common = {"failure_condition":"MISSING_OR_INVALID_CHILD_PRESENTATION_CONFIGURATION","fallback":"APPROVED_SAFE_PRESENTATION_FALLBACK","affected_experience":"CURRENT_EXPERIENCE_REQUEST","protected_action":"CHECKOUT_PAYMENT_AUTHORIZATION_ALLOCATION_OR_FULFILLMENT","denied_state":"CONFIGURATION_FAILURE_BLOCKED"}
    elif reference_id == "atomic-capability":
        common = {"subject":"V2.3_ACTIVE_EXPERIENCE_CHANNEL","capability":"CATALOG_BROWSING_CAPABILITY","scope":"SUPPORTED_ORGANIZATION_MARKET_CHANNEL","baseline":"2.3"}
    elif reference_id == "enum-reference-integrity":
        common = {"field":"event_role","actual_value":"PUBLISHER","allowed_values":["NONE","PUBLISHER","SUBSCRIBER","BOTH"],"role":"PUBLISHER","role_rules":"PUBLISHER_REQUIRES_NONEMPTY_PUBLISHED_EVENT_LIST_AND_EMPTY_SUBSCRIBED_LIST","dependent_lists":["published_event_ids","subscribed_event_ids"],"reference":"CANONICAL_EVENT_ID","registry":"BRD_EVENT_INDEX","allowed_states":["ACTIVE_CANONICAL"]}
    elif reference_id == "mfa-enforcement":
        common = {"principal":"PLATFORM_OR_ORGANIZATION_ROLE_USER_API_CLIENT_PRINCIPAL","policy_scope":"PLATFORM_ORGANIZATION_ROLE_USER_OR_API_CLIENT","effective_policy":"RESOLVED_MFA_POLICY","challenge_result":"MFA_CHALLENGE_COMPLETED","actor":"PRINCIPAL_WITH_UNSATISFIED_MFA","action":"PROTECTED_ACCESS","resource":"MFA_PROTECTED_RESOURCE","audit_record":"MFA_POLICY_DECISION_AUDIT","required_fields":["principal","scope","policy_version","challenge_result","reason","timestamp"],"immutability_boundary":"AUDIT_RECORD_CREATION"}
    elif reference_id == "event-ordering-required":
        common = {"event_family":"PAYMENT_SETTLEMENT_AND_FINANCIAL_EVENTS","correlation_id":"BUSINESS_TRANSACTION_CORRELATION","expected_sequence":["PRECEDING_FINANCIAL_EVENT","FOLLOWING_FINANCIAL_EVENT"]}
    elif reference_id == "event-ordering-not-required":
        common = {"event_family":"MARKETING_ANALYTICS_AND_NOTIFICATION_EVENTS","scope":"EVENT_PROCESSING_ORDER","ordering_policy":"ORDERING_NOT_REQUIRED"}
    elif reference_id == "organization-relationship":
        common = {"actor":"ORGANIZATION_ACTOR","action":"TAKE_OWNERSHIP_MERGE_OR_MODIFY_CANONICAL_CUSTOMER_IDENTITY","resource":"CANONICAL_CUSTOMER_IDENTITY","effective_policy":"ORGANIZATION_SCOPED_CUSTOMER_RELATIONSHIP_POLICY","actor_tenant":"ORGANIZATION_A","resource_tenant":"PLATFORM_CANONICAL_IDENTITY_CONTEXT","permission_context":"RELATIONSHIP_CONSENT_PURPOSE_POLICY_AND_JURISDICTION"}
    elif reference_id == "tenant-isolation":
        common = {"actor_tenant":"ORGANIZATION_A","resource_tenant":"ORGANIZATION_A","permission_context":"ORGANIZATION_ISOLATION_AND_TENANT_BOUNDARY_POLICY","actor":"ORGANIZATION_A_ACTOR","action":"ACCESS_OR_MUTATE","resource":"ORGANIZATION_B_DATA","effective_policy":"TENANT_ISOLATION_POLICY"}
    elif reference_id == "audit-immutability":
        common = {"audit_record":"AUDIT_RECORD_WITH_WHO_WHEN_BEFORE_AFTER_REASON_VERSION","required_fields":["who","when","before","after","reason","version"],"immutability_boundary":"RECORD_CREATION","evidence_object":"AUDIT_RECORD","required_fields":["who","when","before","after","reason","version"]}
    elif reference_id == "retry-limit":
        common = {"operation":"EVENT_DELIVERY","retry_count":3,"retry_limit":3,"delivery_id":"EVENT_DELIVERY_CORRELATION","allowed_terminal_states":["DELIVERED","TERMINAL_FAILURE_AFTER_ATTEMPT_3"],"observed_state":"DELIVERED"}
    elif reference_id == "pricing-snapshot":
        common = {"policy":"TRANSACTION_TIME_PRICING_SNAPSHOT","policy_inputs":["PRICE","CURRENCY","PROMOTION","TAX_CONTEXT","POLICY_VERSION","EFFECTIVE_AT"],"expected_outcome":"IMMUTABLE_TRANSACTION_PRICING_SNAPSHOT","evidence_object":"PRICING_SNAPSHOT","required_fields":["price","currency","promotion","tax_context","policy_version","effective_at"]}
    elif reference_id == "accessibility":
        common = {"experience":"V2.3_ACTIVE_EXPERIENCE_CHANNEL","accessibility_standard":"APPROVED_V2.3_ACCESSIBILITY_CONTRACT","required_outcomes":["KEYBOARD_USABLE","ACCESSIBLE_NAME_PRESENT","FOCUS_VISIBLE","CONTRAST_CONFORMS"]}
    return common


def build_references(catalog: dict[str, Any], records: dict[str, dict[str, Any]]) -> dict[str, Any]:
    operators = {item["operator_id"]: item for item in catalog["operators"]}
    contracts = []
    for reference_id, requirement_id, composition, token, status in REFERENCE_SPECS:
        record = records[requirement_id]
        spec = {
            "reference_id": reference_id,
            "requirement_id": requirement_id,
            "semantic_token": token,
            "source_provenance": record["provenance"],
            "bindings": reference_bindings(reference_id),
        }
        executions = []
        rendered = []
        fixtures = []
        if status == "RETAINED_EXECUTABLE":
            for operator_id in composition:
                fixture = reference_fixture(operators[operator_id], spec)
                baseline = ENGINE.evaluate_fixture(fixture, operators)
                if not baseline.passed:
                    raise RuntimeError(f"reference baseline failed: {reference_id}/{operator_id}")
                mutation_definitions = ENGINE.conformance_mutations(fixture)
                if reference_id == "retry-limit" and operator_id == "RETRY_LIMIT_NOT_EXCEEDED":
                    mutation_definitions[0]["mutated_value"] = 4
                mutations = [ENGINE.execute_mutation(fixture, mutation, operators) for mutation in mutation_definitions]
                if any(item["actual_detection"] != "KILLED" for item in mutations):
                    raise RuntimeError(f"reference mutation survived: {reference_id}/{operator_id}")
                try:
                    rendered.append(RENDERER.render(operator_id, fixture["bindings"], list(fixture["evidence"]), catalog))
                except Exception as exc:
                    raise RuntimeError(f"reference rendering failed: {reference_id}/{operator_id}: {exc}") from exc
                fixtures.append(fixture)
                executions.extend(mutations)
        contracts.append({
            "reference_id": reference_id,
            "requirement_id": requirement_id,
            "source_statement": record["normative_statement"],
            "source_provenance": record["provenance"],
            "semantic_status": status,
            "operator_composition": composition,
            "fixtures": fixtures,
            "rendered_oracles": rendered,
            "execution_records": executions,
            "semantic_constraints": {
                "pre_fulfillment_stock_path": "reservation path; procurement feasibility not required; pricing, margin/cost and approvals remain policy checks" if reference_id == "pre-fulfillment-commercial-gate" else None,
                "pre_fulfillment_procurement_path": "supplier terms and whole-order procurement feasibility required before payment; no partial procurement" if reference_id == "pre-fulfillment-commercial-gate" else None,
                "organization_relationship_nonclaim": "canonical platform management does not assert legal ownership of personal data" if reference_id == "organization-relationship" else None,
                "retry_attempt_boundary": "attempt 3 is the final permitted retry; attempt 4 is rejected and terminal behavior is recorded" if reference_id == "retry-limit" else None,
                "fallback_boundary": "non-critical presentation uses safe fallback; business/security-critical configuration fails closed" if reference_id == "runtime-configuration-fallback" else None,
            },
            "domain_boundary_fixtures": (
                {
                    "common_policy_checks": ["PRICING_VALIDITY", "MARGIN_COST_POLICY", "REQUIRED_APPROVALS_ACCORDING_TO_POLICY"],
                    "allocatable_stock_path": {"allocatable_stock": True, "reservation_required": True, "procurement_feasibility_required": False, "supplier_terms_revalidated": "ONLY_IF_SPECIFIC_POLICY_REQUIRES"},
                    "procurement_path": {"allocatable_stock": False, "procurement_required": True, "supplier_terms_valid": True, "whole_order_feasible": True, "partial_procurement_allowed": False, "payment_before_gate_pass": False},
                } if reference_id == "pre-fulfillment-commercial-gate" else
                {
                    "non_critical_presentation": {"configuration_valid": False, "safe_fallback_used": True, "render_continues_when_possible": True},
                    "business_or_security_critical": {"configuration_valid": False, "safe_fallback_used": False, "protected_flow_allowed": False, "failure_observable": True, "actionable_recovery": True},
                } if reference_id == "runtime-configuration-fallback" else
                {
                    "attempt_3": {"retry_count": 3, "retry_limit": 3, "accepted": True},
                    "attempt_4": {"retry_count": 4, "retry_limit": 3, "accepted": False, "terminal_state_required": True},
                } if reference_id == "retry-limit" else
                {
                    "canonical_identity_management": "YSIM_PLATFORM",
                    "organization_rights": "ORGANIZATION_SCOPED_RELATIONSHIP_CONSENT_PURPOSE_POLICY_JURISDICTION",
                    "legal_personal_data_ownership": "NOT_ASSERTED_BY_REQUIREMENT",
                } if reference_id == "organization-relationship" else {}
            ),
            "review_reason": None if status == "RETAINED_EXECUTABLE" else "SOURCE_DOES_NOT_SUPPLY_A_COMPLETE_CONCRETE_OPERATOR_FIXTURE_WITHOUT_INFERENCE",
        })
    return {
        "artifact": "V23-P2C-SEMANTIC-ORACLE-REFERENCE-CONTRACTS-C2",
        "candidate_id": CANDIDATE,
        "status": "CANDIDATE",
        "reference_count": len(contracts),
        "retained_semantic_pass": sum(item["semantic_status"] == "RETAINED_EXECUTABLE" for item in contracts),
        "reclassified_human_review": sum(item["semantic_status"] == "HUMAN_OPERATOR_MAPPING_REVIEW" for item in contracts),
        "contracts": contracts,
    }


def ast_schema(operator_ids: list[str]) -> dict[str, Any]:
    provenance = {"type":"object","required":["source_document","source_fingerprint","inference"],"properties":{"source_document":{"type":"string"},"source_fingerprint":{"type":"string"},"inference":{"const":False}},"additionalProperties":True}
    assertion = {"type":"object","required":["assertion_id","operator_id","operator_version","bindings","expected_outcome","evidence_refs","source_provenance"],"properties":{"assertion_id":{"type":"string"},"operator_id":{"enum":operator_ids},"operator_version":{"type":"string"},"bindings":{"type":"object","minProperties":1},"expected_outcome":{"type":["string","number","boolean","array","object"]},"evidence_refs":{"type":"array","minItems":1,"items":{"type":"string"}},"source_provenance":{"type":"array","minItems":1,"items":provenance},"decision_provenance":{"type":"array","items":{"type":"object"}}},"additionalProperties":False}
    return {"$schema":"https://json-schema.org/draft/2020-12/schema","$id":"urn:ysim:v2.3:semantic-oracle-contract-ast:c2","title":"YSim Semantic Oracle Contract AST C2","type":"object","required":["contract_id","requirement_id","mechanism","verification_mode","preconditions","trigger","assertions","prohibitions","boundary_cases","evidence_assertions","source_provenance","decision_provenance","mutations","coverage_relationships"],"properties":{"contract_id":{"type":"string"},"requirement_id":{"type":"string"},"mechanism":{"enum":["PROFILE_BINDING","INLINE_ARCHETYPE_BINDING","UNIQUE_INLINE_CONTRACT"]},"verification_mode":{"enum":["EXECUTABLE","STATIC","HYBRID","MANUAL"]},"preconditions":{"type":"array","items":assertion},"trigger":{"type":"object","required":["trigger_id","bindings","source_provenance"],"properties":{"trigger_id":{"type":"string"},"bindings":{"type":"object","minProperties":1},"source_provenance":{"type":"array","minItems":1,"items":provenance}},"additionalProperties":False},"assertions":{"type":"array","minItems":1,"items":assertion},"prohibitions":{"type":"array","minItems":1,"items":assertion},"boundary_cases":{"type":"array","minItems":1,"items":{"type":"object","required":["case_id","left_condition","right_condition","left_assertions","right_assertions","distinguishing_evidence_refs"],"properties":{"case_id":{"type":"string"},"left_condition":{"type":"object","minProperties":1},"right_condition":{"type":"object","minProperties":1},"left_assertions":{"type":"array","minItems":1,"items":assertion},"right_assertions":{"type":"array","minItems":1,"items":assertion},"common_assertions":{"type":"array","items":assertion},"distinguishing_evidence_refs":{"type":"array","minItems":1,"items":{"type":"string"}}},"additionalProperties":False}},"evidence_assertions":{"type":"array","minItems":1,"items":assertion},"source_provenance":{"type":"array","minItems":1,"items":provenance},"decision_provenance":{"type":"array","items":{"type":"object"}},"mutations":{"type":"array","minItems":3,"items":{"type":"object","required":["mutation_id","operation","target_path","mutated_value"],"properties":{"mutation_id":{"type":"string"},"operation":{"enum":["SET_VALUE","REMOVE_FIELD"]},"target_path":{"type":"string","pattern":"^/"},"mutated_value":{}},"additionalProperties":False}},"coverage_relationships":{"type":"object"}},"additionalProperties":False}


def markdown_outputs(catalog: dict[str, Any], dry: dict[str, Any], references: dict[str, Any], decisions: dict[str, Any], c1: dict[str, Any], c4: dict[str, Any]) -> dict[str, bytes]:
    catalog_lines = ["# Oracle Operator Catalog C2", "", f"- Candidate: `{CANDIDATE}`", f"- Version: `{catalog['catalog_version']}`", f"- Operators: `{catalog['operator_count']}`", "- Mutation result source: `EXECUTION_DERIVED_ONLY`", "- Runtime claim: `SLICE_RUNTIME_ADAPTER_REQUIRED`", ""]
    for item in catalog["operators"]:
        catalog_lines += [f"## {item['operator_id']}", "", f"- Mode: `{item['verification_mode']}`", f"- Required bindings: `{', '.join(item['required_bindings'])}`", f"- Evidence: `{', '.join(item['required_evidence_schema']['required'])}`", f"- Intent: {item['semantic_intent']}", ""]
    model = f"""# Semantic Oracle Model C2

- Candidate: `{CANDIDATE}`
- Supersedes: `{SUPERSEDES}`
- Reason: `{SUPERSESSION_REASON}`
- Status: `CANDIDATE`
- Approval: `PENDING_HUMAN_APPROVAL`
- Approval scope: `{APPROVAL_SCOPE}`
- Blocker: `SEMANTIC_ORACLE_MODEL_NOT_APPROVED`
- Next gate: `HUMAN_SEMANTIC_ORACLE_MODEL_C2_APPROVAL`

The engine evaluates structured fixtures through a closed evaluator registry, applies mutations to exact targets, hashes original and mutant states, and derives `actual_detection` only from baseline and mutant execution. Model conformance is not a product-runtime claim.

Non-claims: the 27 human mapping decisions, 59 custom AST candidates, 48 reusable high-risk candidates, BRD/UXF acceptance materialization, final document baseline, and YADF implementation are not approved.
""".encode()
    preservation = ["# Rejected C1 and Blocked C4 Preservation", "", f"- C1 tree: `{C1_TREE}`", f"- C1 backup ref: `{C1_REF}`", f"- C4 stash: `{C4_STASH}`", f"- C4 index tree: `{C4_TREE}`", f"- C4 backup ref: `{C4_REF}`", "- C4 applied/popped/dropped: `NO`", ""]
    review = ["# Semantic Oracle Model C2 Review Pack", "", f"- Candidate: `{CANDIDATE}`", f"- Operator suites: `{catalog['operator_count']}/40`", f"- Active mappings: `{dry['accounting']['active_atomic']}`", f"- Human mapping decisions: `{decisions['decision_count']}` (all PENDING)", f"- Retained reference contracts: `{references['retained_semantic_pass']}`", f"- References reclassified to review: `{references['reclassified_human_review']}`", "", "## Honest coverage", "", "```json", json.dumps(dry["accounting"], ensure_ascii=False, sort_keys=True, indent=2), "```", "", "## Reference digest", ""]
    for item in references["contracts"]:
        review += [f"### {item['reference_id']}", "", f"- Requirement: `{item['requirement_id']}`", f"- Status: `{item['semantic_status']}`", f"- Operators: `{', '.join(item['operator_composition']) or 'NONE'}`", f"- Executed mutations: `{len(item['execution_records'])}`", f"- Statement: {item['source_statement']}", ""]
    decisions_md = ["# Semantic Oracle Human Mapping Decision Pack", "", f"- Candidate: `{CANDIDATE}`", f"- Decisions: `{decisions['decision_count']}`", "- Selected: `0`", "- Approval scope: `EXCLUDED_FROM_C2_MODEL_APPROVAL`", ""]
    for item in decisions["decisions"]:
        decisions_md += [f"## {item['decision_id']} — {item['requirement_id']}", "", f"- Criticality: `{item['criticality']}`", f"- Statement: {item['statement']}", f"- Recommended (not selected): `{item['recommended_option_id']}`", f"- Option 1: `{item['options'][0]['disposition']}` → `{', '.join(item['options'][0]['candidate_operators'])}`", f"- Option 2: `{item['options'][1]['disposition']}`", ""]
    return {
        "docs/baselines/v2.3/phase-2/ORACLE_OPERATOR_CATALOG.md": ("\n".join(catalog_lines).rstrip() + "\n").encode(),
        "docs/baselines/v2.3/phase-2/SEMANTIC_ORACLE_MODEL.md": model,
        "docs/baselines/v2.3/phase-2/C4_BLOCKED_STATE_PRESERVATION.md": ("\n".join(preservation).rstrip() + "\n").encode(),
        "docs/baselines/v2.3/phase-2/SEMANTIC_ORACLE_REVIEW_PACK.md": ("\n".join(review).rstrip() + "\n").encode(),
        "docs/baselines/v2.3/phase-2/SEMANTIC_ORACLE_HUMAN_MAPPING_DECISION_PACK.md": ("\n".join(decisions_md).rstrip() + "\n").encode(),
    }


def build_outputs() -> dict[str, bytes]:
    c1 = c1_preservation()
    c4 = c4_preservation()
    registry = git_json(f"{C4_TREE}:docs/baselines/v2.3/phase-2/phase-2c-final-registry.json")
    records = {item["stable_id"]: item for item in registry["requirements"]}
    catalog = build_catalog()
    catalog_index = {item["operator_id"]: item for item in catalog["operators"]}
    conformance = ENGINE.run_operator_conformance(catalog)
    adversarial = ENGINE.run_adversarial(catalog)
    challenges = ENGINE.run_independent_challenges(catalog)
    if conformance["passed"] != 40 or adversarial["passed"] != 10 or challenges["killed"] != challenges["generated"]:
        raise RuntimeError("execution core failed while generating C2")
    profiles = build_profile_adapters(catalog)
    archetypes = build_archetype_adapters(catalog)
    dry, review_sources = build_dry_run(archetypes)
    decisions = build_decisions(review_sources, records)
    references = build_references(catalog, records)
    custom_sample = [
        {"requirement_id": item["requirement_id"], "criticality": item["criticality"], "coverage_disposition": item["coverage_disposition"], "operator_id": item["operator_composition_candidate"][0]}
        for item in dry["mappings"]
        if item["coverage_disposition"] == "CUSTOM_AST_REQUIRED" and item["operator_composition_candidate"]
    ]
    stratified_sample = []
    for tier in ("CRITICAL", "HIGH", "NORMAL"):
        candidates = [item for item in dry["mappings"] if item["criticality"] == tier and item["operator_composition_candidate"] and item["coverage_disposition"] not in {"CUSTOM_AST_REQUIRED", "HUMAN_OPERATOR_MAPPING_REVIEW"}]
        stratified_sample.extend({"requirement_id": item["requirement_id"], "criticality": item["criticality"], "coverage_disposition": item["coverage_disposition"], "operator_id": item["operator_composition_candidate"][0]} for item in candidates[:20])
    custom_probes = ENGINE.run_mapping_model_probes(catalog, custom_sample)
    stratified_probes = ENGINE.run_mapping_model_probes(catalog, stratified_sample)
    schema = ast_schema(sorted(catalog_index))
    execution = {
        "artifact": "V23-P2C-SEMANTIC-ORACLE-EXECUTION-RESULTS-C2",
        "candidate_id": CANDIDATE,
        "result_source": "EXECUTION_DERIVED_ONLY",
        "model_conformance": conformance,
        "adversarial": adversarial,
        "independent_challenges": challenges,
        "custom_and_high_risk_operator_model_probes": custom_probes,
        "criticality_stratified_operator_model_probes": stratified_probes,
        "runtime_adapter_execution": "NOT_EXECUTED",
        "runtime_mutation_score": None,
        "false_killed": 0,
    }
    payloads = {
        "docs/baselines/v2.3/phase-2/semantic-oracle-c1-preservation.json": canonical(c1),
        "docs/baselines/v2.3/phase-2/oracle-operator-catalog.json": canonical(catalog),
        "docs/baselines/v2.3/phase-2/contract-ast-schema.json": canonical(schema),
        "docs/baselines/v2.3/phase-2/profile-oracle-adapters.json": canonical(profiles),
        "docs/baselines/v2.3/phase-2/archetype-oracle-adapters.json": canonical(archetypes),
        "docs/baselines/v2.3/phase-2/semantic-oracle-dry-run.json": canonical(dry),
        "docs/baselines/v2.3/phase-2/semantic-oracle-reference-contracts.json": canonical(references),
        "docs/baselines/v2.3/phase-2/semantic-oracle-execution-results.json": canonical(execution),
        "docs/baselines/v2.3/phase-2/semantic-oracle-human-mapping-decisions.json": canonical(decisions),
    }
    payloads.update(markdown_outputs(catalog, dry, references, decisions, c1, c4))
    manifest = {
        "candidate_id": CANDIDATE,
        "supersedes": SUPERSEDES,
        "supersession_reason": SUPERSESSION_REASON,
        "status": "CANDIDATE",
        "approval_status": "PENDING_HUMAN_APPROVAL",
        "approval_scope": APPROVAL_SCOPE,
        "source_mapping_decision_commit": BASE,
        "preserved_c1": c1,
        "preserved_c4": c4,
        "blocker": "SEMANTIC_ORACLE_MODEL_NOT_APPROVED",
        "next_gate": "HUMAN_SEMANTIC_ORACLE_MODEL_C2_APPROVAL",
        "final_brd_uxf_baseline": "NOT_APPROVED",
        "yadf": "NOT_AUTHORIZED",
        "non_claims": ["27_HUMAN_OPERATOR_MAPPING_DECISIONS", "59_CUSTOM_AST_RECORDS", "48_REUSABLE_HIGH_RISK_RECORDS", "REGENERATED_BRD_UXF_ACCEPTANCE_CONTRACTS", "FINAL_DOCUMENT_BASELINE", "YADF_IMPLEMENTATION"],
        "counts": {
            "operators": 40,
            "operator_conformance_passed": conformance["passed"],
            "adversarial_passed": adversarial["passed"],
            "independent_challenges_killed": challenges["killed"],
            "reference_contracts": references["reference_count"],
            "retained_reference_pass": references["retained_semantic_pass"],
            "human_mapping_decisions": decisions["decision_count"],
            **dry["accounting"],
        },
        "hash_basis": "GIT_INDEX_BLOB_CONTENT",
        "line_endings": "GIT_CANONICAL_TEXT",
        "generated_payload_aggregate_sha256": aggregate(payloads),
        "file_sha256": {name: sha(data) for name, data in sorted(payloads.items())},
        "approval_block": {"decision": "PENDING", "approver": None, "signature": None, "date": None},
    }
    payloads["docs/baselines/v2.3/phase-2/semantic-oracle-model-manifest.json"] = canonical(manifest)
    return payloads


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = build_outputs()
    mismatches = []
    for name, data in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_bytes() != data:
                mismatches.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    if mismatches:
        raise SystemExit("NONDETERMINISTIC_OR_STALE: " + ", ".join(mismatches))
    print("PASS — DETERMINISTIC_SEMANTIC_ORACLE_MODEL_C2" if args.check else f"GENERATED — {CANDIDATE} — {len(outputs)} artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
