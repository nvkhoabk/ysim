#!/usr/bin/env python3
"""Generate the Phase 2C operator-binding semantic type model candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"
BASE = "77d10a8c3ccb2e7795724fd1c82cdbea36c54e2e"
REJECTED_REF = "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c3-r1-rejected^2"
CANDIDATE = "V23-P2C-OPERATOR-BINDING-TYPE-MODEL-C1"


def canonical(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def aggregate(items: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for path in sorted(items):
        digest.update(path.encode() + b"\0" + items[path] + b"\0")
    return digest.hexdigest()


def git_json(spec: str) -> dict[str, Any]:
    return json.loads(subprocess.check_output(["git", "show", spec], cwd=ROOT))


BASE_TYPES = [
    "ENTITY_ID", "ENTITY_TYPE", "REFERENCE_ID", "PRINCIPAL_ID", "TENANT_ID", "RESOURCE_ID",
    "CAPABILITY_ID", "CONFIGURATION_KEY", "FIELD_ID", "EVENT_TYPE_ID", "POLICY_ID", "POLICY_VERSION",
    "CANONICAL_OUTCOME", "STATE_MACHINE_ID", "STATE_ID", "CANONICAL_ENUM_VALUE", "BOOLEAN", "INTEGER",
    "DECIMAL", "TIMESTAMP", "DURATION", "CORRELATION_ID", "HASH", "EVIDENCE_OBJECT_REF",
    "ACTION_ID", "APPROVAL_ID", "SERVICE_ID", "METRIC_ID", "DATA_CLASS_ID", "CURRENCY_CODE",
    "ORDER_ID", "DELIVERY_ID", "ROLE_ID", "OPERATION_ID", "FAILURE_REASON_ID", "CONFIGURATION_SOURCE_ID",
    "EVENT_FAMILY_ID", "EXPERIENCE_ID", "STANDARD_ID",
]


FIELD_TYPES: dict[str, dict[str, str]] = {
    "ACCESSIBILITY_CONFORMS":{"experience":"EXPERIENCE_ID","accessibility_standard":"STANDARD_ID","required_outcomes":"SET_OF<CANONICAL_OUTCOME>"},
    "ACTOR_AUTHORIZED":{"actor":"PRINCIPAL_ID","action":"ACTION_ID","resource":"RESOURCE_ID","effective_policy":"POLICY_ID"},
    "ACTOR_DENIED":{"actor":"PRINCIPAL_ID","action":"ACTION_ID","resource":"RESOURCE_ID","effective_policy":"POLICY_ID"},
    "APPROVAL_REQUIRED":{"action":"ACTION_ID","approval_policy":"POLICY_ID","approval_reference":"APPROVAL_ID"},
    "AUDIT_IMMUTABLE":{"audit_record":"EVIDENCE_OBJECT_REF","required_fields":"SET_OF<FIELD_ID>","protected_fields":"SET_OF<FIELD_ID>","before_hash":"HASH","after_hash":"HASH","immutability_boundary":"POLICY_ID"},
    "CAPABILITY_AVAILABLE":{"subject":"ENTITY_ID","capability":"CAPABILITY_ID","scope":"CANONICAL_ENUM_VALUE"},
    "CAPABILITY_NOT_PLACEHOLDER":{"subject":"ENTITY_ID","capability":"CAPABILITY_ID","scope":"CANONICAL_ENUM_VALUE"},
    "COMPOSITE_COVERED_BY_CHILDREN":{"parent_id":"ENTITY_ID","child_ids":"SET_OF<ENTITY_ID>","coverage_mode":"CANONICAL_ENUM_VALUE"},
    "CONFIGURATION_PRECEDENCE":{"configuration_key":"CONFIGURATION_KEY","source_values":"SET_OF<CONFIGURATION_SOURCE_ID>","source_versions":"SET_OF<POLICY_VERSION>","precedence_order":"CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>","resolved_source":"CONFIGURATION_SOURCE_ID","resolved_value":"CANONICAL_ENUM_VALUE"},
    "CONFIGURATION_RESOLVES":{"configuration_key":"CONFIGURATION_KEY","configuration_sources":"CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>","source_versions":"SET_OF<POLICY_VERSION>","resolved_source":"CONFIGURATION_SOURCE_ID","expected_value":"CANONICAL_ENUM_VALUE"},
    "DATA_RETENTION_WINDOW":{"data_class":"DATA_CLASS_ID","retention_window":"DURATION","terminal_action":"ACTION_ID"},
    "DELIVERY_TERMINAL_STATE":{"delivery_id":"DELIVERY_ID","allowed_terminal_states":"SET_OF<STATE_ID>","observed_state":"STATE_ID"},
    "ENUM_VALUE_ALLOWED":{"field":"FIELD_ID","actual_value":"CANONICAL_ENUM_VALUE","allowed_values":"SET_OF<CANONICAL_ENUM_VALUE>"},
    "EVENT_EMITTED":{"event_id":"EVENT_TYPE_ID","trigger":"ACTION_ID","correlation_id":"CORRELATION_ID"},
    "EVENT_NOT_EMITTED":{"event_id":"EVENT_TYPE_ID","condition":"POLICY_ID","observation_window":"DURATION"},
    "EVENT_ORDER_NOT_REQUIRED":{"event_family":"EVENT_FAMILY_ID","scope":"CANONICAL_ENUM_VALUE","ordering_policy":"POLICY_ID"},
    "EVENT_ORDER_PRESERVED":{"event_family":"EVENT_FAMILY_ID","correlation_id":"CORRELATION_ID","expected_sequence":"CANONICAL_SET_REF<EVENT_TYPE_ID>"},
    "EVIDENCE_FIELD_PRESENT":{"evidence_object":"EVIDENCE_OBJECT_REF","required_fields":"SET_OF<FIELD_ID>"},
    "FAIL_CLOSED":{"failure_condition":"CANONICAL_OUTCOME","protected_action":"ACTION_ID","denied_state":"STATE_ID"},
    "MFA_CHALLENGE_REQUIRED":{"principal":"PRINCIPAL_ID","policy_scope":"RESOURCE_ID","effective_policy":"POLICY_ID","challenge_result":"CANONICAL_OUTCOME"},
    "OWNER_EQUALS":{"entity":"ENTITY_ID","actual_owner":"REFERENCE_ID","expected_owner":"REFERENCE_ID","ownership_semantics":"CANONICAL_ENUM_VALUE"},
    "PAYMENT_INITIATION_ALLOWED":{"order_id":"ORDER_ID","commercial_gate_result":"CANONICAL_OUTCOME","payment_state":"STATE_ID"},
    "PAYMENT_INITIATION_BLOCKED":{"order_id":"ORDER_ID","failed_checks":"SET_OF<CANONICAL_OUTCOME>","blocked_states":"SET_OF<STATE_ID>"},
    "PERFORMANCE_WITHIN_BUDGET":{"service":"SERVICE_ID","metric":"METRIC_ID","observed_value":"DECIMAL","budget":"DECIMAL"},
    "POLICY_OUTCOME_EQUALS":{"policy":"POLICY_ID","policy_version":"POLICY_VERSION","policy_inputs":"EVIDENCE_OBJECT_REF","expected_outcome":"CANONICAL_OUTCOME"},
    "PROCUREMENT_FEASIBLE":{"order_id":"ORDER_ID","supplier_terms":"POLICY_ID","capacity":"DECIMAL","coverage_policy":"POLICY_ID"},
    "PROCUREMENT_NOT_FEASIBLE":{"order_id":"ORDER_ID","failure_reason":"FAILURE_REASON_ID","dependent_action":"ACTION_ID"},
    "RECONCILIATION_BALANCED":{"correlation_id":"CORRELATION_ID","debits":"DECIMAL","credits":"DECIMAL","currency":"CURRENCY_CODE"},
    "REFERENCE_TARGET_VALID":{"reference":"REFERENCE_ID","target_id":"ENTITY_ID","target_type":"ENTITY_TYPE","registry":"ENTITY_ID","registry_source":"REFERENCE_ID","allowed_states":"SET_OF<STATE_ID>","allowed_lifecycle_states":"SET_OF<STATE_ID>"},
    "RETRY_LIMIT_NOT_EXCEEDED":{"operation":"OPERATION_ID","retry_count":"INTEGER","retry_limit":"INTEGER"},
    "ROLE_LIST_CONSISTENT":{"role":"ROLE_ID","role_rules":"POLICY_ID","dependent_lists":"SET_OF<REFERENCE_ID>"},
    "SAFE_FALLBACK_USED":{"failure_condition":"CANONICAL_OUTCOME","fallback":"CONFIGURATION_KEY","affected_experience":"EXPERIENCE_ID"},
    "SCOPE_ACTIVE":{"subject":"ENTITY_ID","baseline":"CANONICAL_ENUM_VALUE","scope":"CANONICAL_ENUM_VALUE"},
    "SCOPE_NOT_ACTIVE":{"subject":"ENTITY_ID","baseline":"CANONICAL_ENUM_VALUE","inactive_scope":"CANONICAL_ENUM_VALUE"},
    "SET_CONTAINS":{"actual_set":"RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>","required_members":"CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"},
    "SET_EQUALS":{"actual_set":"RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>","expected_set":"CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"},
    "SET_EXCLUDES":{"actual_set":"RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>","prohibited_members":"CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"},
    "STATE_TRANSITION_ALLOWED":{"state_machine":"STATE_MACHINE_ID","from_state":"STATE_ID","trigger":"ACTION_ID","to_state":"STATE_ID"},
    "STATE_TRANSITION_REJECTED":{"state_machine":"STATE_MACHINE_ID","from_state":"STATE_ID","trigger":"ACTION_ID","prohibited_state":"STATE_ID"},
    "TENANT_ISOLATED":{"actor_tenant":"TENANT_ID","resource_tenant":"TENANT_ID","permission_context":"POLICY_ID"},
}


COMPARISON_TYPES = {
    "SET_EQUALS":"SET_OF<CANONICAL_ENUM_VALUE>", "SET_CONTAINS":"SET_OF<CANONICAL_ENUM_VALUE>", "SET_EXCLUDES":"SET_OF<CANONICAL_ENUM_VALUE>",
    "OWNER_EQUALS":"REFERENCE_ID", "STATE_TRANSITION_ALLOWED":"STATE_ID", "STATE_TRANSITION_REJECTED":"STATE_ID",
    "POLICY_OUTCOME_EQUALS":"CANONICAL_OUTCOME", "CONFIGURATION_RESOLVES":"CANONICAL_ENUM_VALUE",
    "CONFIGURATION_PRECEDENCE":"CONFIGURATION_SOURCE_ID", "PAYMENT_INITIATION_ALLOWED":"STATE_ID",
    "DELIVERY_TERMINAL_STATE":"STATE_ID", "ENUM_VALUE_ALLOWED":"CANONICAL_ENUM_VALUE",
    "PERFORMANCE_WITHIN_BUDGET":"DECIMAL", "RECONCILIATION_BALANCED":"DECIMAL",
}


EXPECTED_ORIGINS = ["APPROVED_DECISION","CANONICAL_REGISTRY","VERSIONED_POLICY","VERSIONED_CONFIGURATION","SOURCE_LITERAL","SYNTHETIC_MODEL_FIXTURE"]
OBSERVED_ORIGINS = ["RUNTIME_OBSERVED","EVIDENCE_OBJECT","SYNTHETIC_MODEL_FIXTURE"]
CONTEXT_ORIGINS = ["SOURCE_LITERAL","APPROVED_DECISION","CANONICAL_REGISTRY","VERSIONED_POLICY","VERSIONED_CONFIGURATION","SYNTHETIC_MODEL_FIXTURE"]


def type_catalog() -> dict[str, Any]:
    return {
        "catalog_id":"V23-P2C-BUSINESS-SEMANTIC-TYPE-CATALOG-C1", "version":"1.0.0-candidate.1",
        "candidate_id":CANDIDATE, "natural_language_is_typed_value":False,
        "origins":["SOURCE_LITERAL","APPROVED_DECISION","CANONICAL_REGISTRY","VERSIONED_POLICY","VERSIONED_CONFIGURATION","RUNTIME_OBSERVED","EVIDENCE_OBJECT","SYNTHETIC_MODEL_FIXTURE"],
        "types":{name:{"type_id":name,"kind":"PRIMITIVE" if name in {"BOOLEAN","INTEGER","DECIMAL","TIMESTAMP","DURATION"} else "SYMBOLIC_REFERENCE","prose_allowed":False,"requires_origin":True,"requires_provenance":True,"requires_resolver":name not in {"BOOLEAN","INTEGER","DECIMAL","TIMESTAMP","DURATION"}} for name in BASE_TYPES},
        "generic_types":{
            "SET_OF<T>":{"member_type":"T","members_must_be_typed":True,"sentence_members_forbidden":True},
            "CANONICAL_SET_REF<T>":{"resolver_required":True,"allowed_origins":["CANONICAL_REGISTRY","VERSIONED_POLICY","VERSIONED_CONFIGURATION","APPROVED_DECISION","SYNTHETIC_MODEL_FIXTURE"]},
            "RUNTIME_SET_REF<T>":{"resolver_required":True,"allowed_origins":["RUNTIME_OBSERVED","EVIDENCE_OBJECT","SYNTHETIC_MODEL_FIXTURE"]},
        },
        "symbolic_reference_required_fields":["namespace","identifier","semantic_type","authoritative_source","resolver_contract","lifecycle","origin","provenance","inference"],
        "source_clarification_rule":"MISSING_AUTHORITATIVE_SOURCE_OR_RESOLVER",
    }


def origin_for(name: str, semantic_type: str) -> list[str]:
    if name.startswith("actual_") or name in {"observed_state","observed_value","retry_count","debits","credits"} or semantic_type.startswith("RUNTIME_SET_REF"):
        return OBSERVED_ORIGINS
    if name.startswith(("expected_","required_","prohibited_","allowed_")) or semantic_type.startswith("CANONICAL_SET_REF") or semantic_type in {"POLICY_ID","POLICY_VERSION","CANONICAL_OUTCOME","STATE_ID","CANONICAL_ENUM_VALUE"}:
        return EXPECTED_ORIGINS
    return CONTEXT_ORIGINS


def operator_schemas(catalog: dict[str, Any]) -> dict[str, Any]:
    rows=[]
    for operator in catalog["operators"]:
        op=operator["operator_id"]
        if op not in FIELD_TYPES or not set(operator["required_bindings"]) <= set(FIELD_TYPES[op]):
            raise RuntimeError(f"INCOMPLETE_OPERATOR_TYPE_SCHEMA:{op}")
        bindings=[]
        binding_names=list(operator["required_bindings"])+sorted(set(FIELD_TYPES[op])-set(operator["required_bindings"]))
        for name in binding_names:
            semantic_type=FIELD_TYPES[op][name]
            bindings.append({
                "name":name,"semantic_type":semantic_type,"cardinality":"1..N" if "SET" in semantic_type else "1",
                "allowed_origins":origin_for(name,semantic_type),"resolver_required":semantic_type not in {"BOOLEAN","INTEGER","DECIMAL","TIMESTAMP","DURATION"},
                "prohibited_value_shapes":["NATURAL_LANGUAGE_SENTENCE","PREDICATE_CLAUSE","FULL_REQUIREMENT_TEXT","UNRESOLVED_LABEL","PLACEHOLDER_DEFAULT"],
            })
        comparison_type=COMPARISON_TYPES.get(op, next(iter(FIELD_TYPES[op].values())))
        rows.append({
            "operator_id":op,"operator_version":operator["version"],"binding_schema_version":"1.0.0-candidate.1",
            "bindings":bindings,
            "comparison_contract":{"semantic_type":comparison_type,"relation":"SEMANTIC_EQUALITY","mutated_difference_must_fail":True},
            "origin_constraints":{"expected_allowed":EXPECTED_ORIGINS,"observed_allowed":OBSERVED_ORIGINS,"expected_observed_origin_ids_must_differ":True,"expected_observed_resolvers_must_differ":True},
            "resolver_requirements":{"authoritative_source_required":True,"deterministic_resolver_required":True,"output_type_must_match":True,"missing_resolver_disposition":"SOURCE_CLARIFICATION_REQUIRED"},
            "evidence_requirements":{"evidence_object_type":"EVIDENCE_OBJECT_REF","field_identifier_type":"FIELD_ID","labels_are_values":False,"runtime_evidence_pending":True},
            "cross_field_invariants":["ALL_BINDINGS_CONSUMED","EXPECTED_AND_OBSERVED_INDEPENDENT","RESOLVER_OUTPUT_MATCHES_SEMANTIC_TYPE","NO_PROSE_TYPED_VALUES"],
            "evaluator_consumes_all_bindings":True,
            "adversarial_tests_required":10,
        })
    return {"artifact":"V23-P2C-OPERATOR-BINDING-SCHEMAS-C1","candidate_id":CANDIDATE,"schema_count":len(rows),"schemas":rows}


SOURCE_CLARIFICATIONS={"BD-05-009","BRD-WS-02-R003","BRD-WS-07-R005","EP-08-006","EP-17-002","UXF-405"}
COMPOUND={"BD-02-005","BD-04-005","BD-13-015","BD-13-016","BRD-WS-07-R010","EP-16-005"}
UNSUPPORTED={"BD-02-005","BD-05-009","BD-13-015","BD-13-016","BRD-META-MODEL-R005","BRD-SNAPSHOT-INDEX-R010","BRD-WS-02-R002","BRD-WS-06-R003","BRD-WS-07-R005","BRD-WS-07-R009","BRD-WS-07-R010","BRD-WS-08-R004","BRD-WS-13-R013","BRD-WS-14-R029","EP-08-006","EP-11-002","EP-16-005","UXF-010","UXF-011","UXF-402","UXF-405"}


SPECIAL_RECOMMENDATIONS={
    "BRD-WS-02-R003":"SET_EQUALS over CANONICAL_SET_REF<CANONICAL_ENUM_VALUE> eSIM capability registry and independently resolved RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>",
    "BRD-WS-07-R014":"OWNER_EQUALS with Order ID, runtime order.owner_id and independently resolved order.payment_owner_id",
    "BRD-WS-08-R004":"REFERENCE_TARGET_VALID plus owner-to-MerchantAccount selection invariant; OWNER_EQUALS is prohibited",
    "BRD-WS-14-R031":"SET_EQUALS over dependency-graph resolved expected Configuration/Capability IDs and independently reported impact IDs",
    "EP-17-002":"SET_EQUALS over canonical Platform Component Inventory and independently observed monitored component IDs",
    "EP-08-006":"Replace RETRY_LIMIT_NOT_EXCEEDED with new-PaymentAttempt identity assertion unless a retry policy is approved",
    "UXF-405":"CONFIGURATION_PRECEDENCE only after a governed ordered source registry is approved",
}


def dispositions(schemas: dict[str, Any]) -> dict[str, Any]:
    custom=git_json(f"{REJECTED_REF}:docs/baselines/v2.3/phase-2/semantic-completion-custom-asts.json")["contracts"]
    fixtures=git_json(f"{REJECTED_REF}:docs/baselines/v2.3/phase-2/semantic-completion-canonical-fixtures.json")["fixtures"]
    by={(item["requirement_id"],item["evaluator_id"]):item for item in fixtures}
    schema_by={item["operator_id"]:item for item in schemas["schemas"]}
    rows=[]
    for contract in sorted(custom,key=lambda item:item["requirement_id"]):
        rid=contract["requirement_id"]
        primary=next(op for op in contract["operator_composition"] if op not in {"EVIDENCE_FIELD_PRESENT","SCOPE_ACTIVE"})
        if rid in SOURCE_CLARIFICATIONS: disposition="SOURCE_CLARIFICATION_REQUIRED"
        elif rid in COMPOUND: disposition="COMPOUND_AST_REQUIRED"
        elif rid in UNSUPPORTED: disposition="OPERATOR_REMAP_REQUIRED"
        else: disposition="CORRECTABLE_WITH_APPROVED_TYPE_MODEL"
        schema=schema_by[primary]
        rows.append({
            "requirement_id":rid,"criticality":contract["criticality"],"current_operator":primary,
            "current_invalid_bindings":by[(rid,primary)]["bindings"],
            "correct_semantic_types":{item["name"]:item["semantic_type"] for item in schema["bindings"]},
            "expected_origins":schema["origin_constraints"]["expected_allowed"],"observed_origins":schema["origin_constraints"]["observed_allowed"],
            "resolver_and_evidence_requirement":"Independent authoritative resolver for expected operands; runtime/evidence resolver for observed operands; EVIDENCE_OBJECT_REF with FIELD_ID values",
            "recommended_operator_composition":SPECIAL_RECOMMENDATIONS.get(rid,f"Retain {primary} only with typed bindings, independent origins, EVIDENCE_FIELD_PRESENT and SCOPE_ACTIVE"),
            "disposition":disposition,"source_clarification_required":rid in SOURCE_CLARIFICATIONS,
            "mandatory_audit_record":rid in {"BRD-WS-02-R003","BRD-WS-07-R014","BRD-WS-08-R004","BRD-WS-14-R031","EP-17-002"},
            "regeneration_applied":False,
        })
    counts=Counter(item["disposition"] for item in rows)
    return {"artifact":"V23-P2C-OPERATOR-BINDING-TYPE-DISPOSITIONS-C1","candidate_id":CANDIDATE,"record_count":len(rows),"counts":dict(sorted(counts.items())),"records":rows}


DECISION_DATA={
"BD-05-009":{
 "question":"What approval and lifecycle govern a Price Change Set?","recommended":"OPT-1",
 "options":[
  {"option_id":"P2C-OBT-C1-BD-05-009-OPT-1","meaning":"A Price Change Set follows DRAFT, SUBMITTED, APPROVED, REJECTED and EFFECTIVE states; only a valid APPROVED set may change a Price Book.","source_wording":"Price Book chỉ được thay đổi bởi Price Change Set có trạng thái APPROVED còn hiệu lực. Price Change Set phải đi qua DRAFT, SUBMITTED, APPROVED hoặc REJECTED; approver, quyết định, thời điểm và policy version phải được ghi nhận.","consequence":"Requires versioned approval policy and approval evidence before effectiveness."},
  {"option_id":"P2C-OBT-C1-BD-05-009-OPT-2","meaning":"Price Change Set requires deterministic validation and publication but no human approval.","source_wording":"Price Book chỉ được thay đổi bởi Price Change Set đã vượt qua validation và được publish; v2.3 không yêu cầu human approval trừ khi policy riêng quy định.","consequence":"Removes universal approval; policy-specific approval remains possible."}],
 "operators":["APPROVAL_REQUIRED","STATE_TRANSITION_ALLOWED","EVIDENCE_FIELD_PRESENT"],"non_inferences":["No approver role is inferred.","No SLA is inferred."],"runtime_impact":"Price lifecycle, approval service and effective-state gate.","criticality":"CRITICAL"},
"BRD-WS-02-R003":{
 "question":"What is the authoritative eSIM capability set and resolution rule?","recommended":"OPT-1",
 "options":[
  {"option_id":"P2C-OBT-C1-BRD-WS-02-R003-OPT-1","meaning":"A versioned eSIM Capability Registry is canonical; Product Specification declarations equal independently resolved operational capabilities.","source_wording":"Product Specification phải khai báo các eSIM Capability bằng ID trong eSIM Capability Registry có version. Tập capability khai báo phải khớp tập capability được resolver xác định độc lập từ profile/provider và policy đang hiệu lực.","consequence":"Creates canonical registry and two independent resolvers."},
  {"option_id":"P2C-OBT-C1-BRD-WS-02-R003-OPT-2","meaning":"Each provider owns a versioned capability schema mapped to a common YSim capability taxonomy.","source_wording":"Khả năng eSIM thực tế được xác định theo provider capability schema có version và được map sang YSim capability taxonomy trước khi đối chiếu Product Specification.","consequence":"Adds provider mapping and reconciliation complexity."}],
 "operators":["SET_EQUALS","REFERENCE_TARGET_VALID","EVIDENCE_FIELD_PRESENT"],"non_inferences":["No capability members are invented.","No provider schema is assumed."],"runtime_impact":"Capability registry, provider resolver and validation evidence.","criticality":"HIGH"},
"BRD-WS-07-R005":{
 "question":"What approval and lifecycle govern Identity merge?","recommended":"OPT-1",
 "options":[
  {"option_id":"P2C-OBT-C1-BRD-WS-07-R005-OPT-1","meaning":"Merge is a governed proposal requiring approval; no automatic merge.","source_wording":"Identity Merge phải được tạo dưới dạng Merge Proposal, được authorized reviewer APPROVE hoặc REJECT, và chỉ proposal APPROVED mới được áp dụng. Source identities, canonical target, reason, decision và audit evidence phải được giữ lại.","consequence":"Requires merge proposal, authorization and audit lifecycle."},
  {"option_id":"P2C-OBT-C1-BRD-WS-07-R005-OPT-2","meaning":"Identity merge is deferred; v2.3 only records possible links.","source_wording":"V2.3 không thực hiện Identity Merge; Platform chỉ ghi nhận possible-duplicate linkage để review trong baseline tương lai.","consequence":"No active merge workflow; duplicate resolution remains deferred."}],
 "operators":["APPROVAL_REQUIRED","STATE_TRANSITION_ALLOWED","AUDIT_IMMUTABLE"],"non_inferences":["No automatic matching threshold is inferred.","No legal identity consolidation is inferred."],"runtime_impact":"Identity merge workflow or deferred-link store.","criticality":"CRITICAL"},
"EP-08-006":{
 "question":"Does v2.3 define a universal payment retry limit?","recommended":"OPT-1",
 "options":[
  {"option_id":"P2C-OBT-C1-EP-08-006-OPT-1","meaning":"No universal numeric limit is asserted here; every retry creates a new PaymentAttempt and any limit comes from versioned payment policy.","source_wording":"Mỗi lần retry phải tạo PaymentAttempt mới. Retry limit, nếu áp dụng, phải được lấy từ Payment Retry Policy có version; requirement này không quy định một limit cố định.","consequence":"Removes unsupported value 3 and requires policy-driven limits."},
  {"option_id":"P2C-OBT-C1-EP-08-006-OPT-2","meaning":"A universal maximum of three attempts is normative.","source_wording":"Mỗi lần retry phải tạo PaymentAttempt mới và tổng số PaymentAttempt cho một PaymentSession không được vượt quá 3 trước terminal failure.","consequence":"Introduces an explicit global limit of three."}],
 "operators":["REFERENCE_TARGET_VALID","RETRY_LIMIT_NOT_EXCEEDED"],"non_inferences":["The value 3 is not retained unless OPT-2 is selected.","No gateway retry topology is inferred."],"runtime_impact":"PaymentAttempt identity and policy-based or fixed retry enforcement.","criticality":"CRITICAL"},
"EP-17-002":{
 "question":"What inventory and signals define Platform monitoring coverage?","recommended":"OPT-1",
 "options":[
  {"option_id":"P2C-OBT-C1-EP-17-002-OPT-1","meaning":"A versioned Platform Component Inventory and component-class signal profile are authoritative.","source_wording":"Monitoring coverage phải được đối chiếu với Platform Component Inventory có version. Mỗi active component phải có các mandatory signals theo component-class Monitoring Profile; inventory IDs và observed signal evidence phải được resolve độc lập.","consequence":"Defines canonical inventory and mandatory signal profiles."},
  {"option_id":"P2C-OBT-C1-EP-17-002-OPT-2","meaning":"Only critical Platform components require mandatory signal coverage in v2.3.","source_wording":"V2.3 bắt buộc monitoring signal coverage cho các Platform component được phân loại CRITICAL; coverage cho component khác theo approved monitoring policy.","consequence":"Narrows the original whole-Platform obligation."}],
 "operators":["SET_EQUALS","EVIDENCE_FIELD_PRESENT"],"non_inferences":["No component or signal list is invented.","External dependencies are not automatically Platform components."],"runtime_impact":"Component inventory, signal profiles and coverage reconciliation.","criticality":"HIGH"},
"UXF-405":{
 "question":"What governed precedence resolves inherited Organization and Storefront configuration?","recommended":"OPT-1",
 "options":[
  {"option_id":"P2C-OBT-C1-UXF-405-OPT-1","meaning":"Platform/security invariants override jurisdiction/market, then Organization, then Storefront configuration.","source_wording":"Storefront kế thừa Organization configuration. Effective configuration được resolve theo thứ tự: Platform và Security Invariants; Jurisdiction/Market policy; Organization; Storefront. Override chỉ hợp lệ tại layer được policy cho phép và phải versioned, observable, auditable.","consequence":"Defines a fixed governed precedence and override boundary."},
  {"option_id":"P2C-OBT-C1-UXF-405-OPT-2","meaning":"Organization supplies defaults and Storefront overrides them except immutable platform/security invariants.","source_wording":"Storefront kế thừa Organization defaults và có thể override các key được phép; Platform/Security invariants không thể bị override. Effective source và version phải observable và auditable.","consequence":"Leaves jurisdiction/market precedence to separate policy."}],
 "operators":["CONFIGURATION_PRECEDENCE","CONFIGURATION_RESOLVES","EVIDENCE_FIELD_PRESENT"],"non_inferences":["No configuration keys are invented.","No override is allowed unless its layer policy permits it."],"runtime_impact":"Versioned configuration layers, resolver and effective-source evidence.","criticality":"HIGH"}}


def decisions() -> dict[str, Any]:
    rows=[]
    for rid,data in sorted(DECISION_DATA.items()):
        rows.append({"decision_id":f"P2C-OBT-C1-DEC-{rid}","requirement_id":rid,"approval_status":"PENDING_HUMAN_APPROVAL",**data,"selected_option":None})
    return {"artifact":"V23-P2C-OPERATOR-BINDING-SOURCE-CLARIFICATIONS-C1","candidate_id":CANDIDATE,"decision_count":len(rows),"selected_count":0,"decisions":rows}


def markdown_model(types: dict[str, Any], schemas: dict[str, Any], dispositions_data: dict[str, Any]) -> bytes:
    lines=["# Phase 2C Operator Binding Business-Semantic Type Model C1","",f"- Candidate: `{CANDIDATE}`","- Status: `CANDIDATE`","- Approval: `PENDING_HUMAN_APPROVAL`","- Next gate: `HUMAN_OPERATOR_BINDING_TYPE_MODEL_AND_SOURCE_CLARIFICATION_APPROVAL`","","Natural-language predicates, labels and complete requirement statements are not typed values.","","## Type catalog","",f"- Named semantic types: {len(types['types'])}","- Generic types: `SET_OF<T>`, `CANONICAL_SET_REF<T>`, `RUNTIME_SET_REF<T>`","- Expected and observed origin IDs and resolvers must be independent.","","## Operator schemas","",f"- Complete schemas: {schemas['schema_count']}/40","- Each schema declares semantic types, cardinality, origins, resolvers, evidence, invariants and evaluator consumption.","","## Read-only C3-R1 reassessment","",f"- Records: {dispositions_data['record_count']}"]
    for key,value in dispositions_data["counts"].items(): lines.append(f"- {key}: {value}")
    lines += ["","## Non-claims","","- Does not regenerate custom ASTs or fixtures.","- Does not modify BRD/UXF.","- Does not claim runtime evidence or runtime mutation coverage.","- Does not approve the final document baseline, runtime adapters or YADF implementation.",""]
    return "\n".join(lines).encode()


def markdown_decisions(payload: dict[str, Any]) -> bytes:
    lines=["# Operator Binding Source Clarification Decision Pack","",f"- Candidate: `{CANDIDATE}`","- All decisions: `PENDING_HUMAN_APPROVAL`",""]
    for item in payload["decisions"]:
        lines += [f"## {item['decision_id']} — {item['requirement_id']}","",item["question"],"",f"Recommended: `{item['recommended']}`",""]
        for option in item["options"]:
            lines += [f"### {option['option_id']}","",f"- Meaning: {option['meaning']}",f"- Exact proposed wording: {option['source_wording']}",f"- Consequence: {option['consequence']}",""]
        lines += [f"- Resulting operators: {', '.join(item['operators'])}",f"- Criticality: {item['criticality']}",f"- Runtime impact: {item['runtime_impact']}","- Non-inferences: "+"; ".join(item["non_inferences"]),""]
    return "\n".join(lines).encode()


def adversarial_matrix(schemas: dict[str, Any]) -> dict[str, Any]:
    tests=[("VALID_INDEPENDENTLY_SOURCED_FIXTURE","PASS"),("SENTENCE_COPY_EXPECTED_OBSERVED","FAIL"),("WHOLE_REQUIREMENT_AS_SCALAR","FAIL"),("SENTENCE_AS_SET_MEMBER","FAIL"),("UNKNOWN_ENUM_OR_STATE","FAIL"),("MISSING_AUTHORITATIVE_RESOLVER","FAIL"),("SAME_EXPECTED_OBSERVED_ORIGIN","FAIL"),("EVIDENCE_LABEL_AS_OBJECT","FAIL"),("WRONG_TYPED_IDENTIFIER","FAIL"),("REAL_MUTATED_DIFFERENCE","DETECTED")]
    rows=[{"operator_id":schema["operator_id"],"tests":[{"test_id":test,"expected":expected} for test,expected in tests]} for schema in schemas["schemas"]]
    return {"artifact":"V23-P2C-OPERATOR-BINDING-ADVERSARIAL-MATRIX-C1","candidate_id":CANDIDATE,"operator_count":len(rows),"tests_per_operator":10,"total_tests":len(rows)*10,"sentence_copy_required":len(rows),"rows":rows}


def build_outputs() -> dict[str, bytes]:
    accepted=git_json(f"{BASE}:docs/baselines/v2.3/phase-2/oracle-operator-catalog.json")
    types=type_catalog();schemas=operator_schemas(accepted);disp=dispositions(schemas);decs=decisions();matrix=adversarial_matrix(schemas)
    outputs={
        "docs/baselines/v2.3/phase-2/OPERATOR_BINDING_TYPE_MODEL.md":markdown_model(types,schemas,disp),
        "docs/baselines/v2.3/phase-2/operator-binding-semantic-types.json":canonical(types),
        "docs/baselines/v2.3/phase-2/operator-binding-schemas.json":canonical(schemas),
        "docs/baselines/v2.3/phase-2/operator-binding-type-dispositions.json":canonical(disp),
        "docs/baselines/v2.3/phase-2/OPERATOR_BINDING_SOURCE_CLARIFICATION_DECISION_PACK.md":markdown_decisions(decs),
        "docs/baselines/v2.3/phase-2/operator-binding-source-clarification-decisions.json":canonical(decs),
        "docs/baselines/v2.3/phase-2/operator-binding-type-adversarial-matrix.json":canonical(matrix),
    }
    manifest={
        "candidate_id":CANDIDATE,"status":"CANDIDATE","approval_status":"PENDING_HUMAN_APPROVAL",
        "purpose":"DEFINE_OPERATOR_SPECIFIC_BUSINESS_SEMANTIC_BINDING_TYPES_ORIGIN_INDEPENDENCE_AND_RESOLVER_CONTRACTS",
        "next_gate":"HUMAN_OPERATOR_BINDING_TYPE_MODEL_AND_SOURCE_CLARIFICATION_APPROVAL","base_commit":BASE,
        "rejected_c3_r1_ref":"refs/ysim-backups/v2.3/phase-2c-semantic-completion-c3-r1-rejected","rejected_c3_r1_tree":"92fb9de65f2fd6b5be888a271ab4ab245798eb9d","rejected_c3_r1_git_content_aggregate":"29c13a89ff0116c00117bbed0472d115ffc6afb1f21924fcb3c2af23f0d07c4f",
        "audit_input":{"failed_custom_asts":59,"evidence_labels":550,"sentence_copy_vulnerable_shapes":20,"represented_shapes":21,"semantic_type_mismatches":57,"unsupported_mappings":21,"source_clarifications":6},
        "counts":{"semantic_types":len(types["types"]),"generic_types":len(types["generic_types"]),"operator_schemas":schemas["schema_count"],"dispositions":disp["record_count"],"source_clarification_decisions":decs["decision_count"],"adversarial_tests":matrix["total_tests"]},
        "scope":"SEMANTIC_TYPE_CATALOG_OPERATOR_BINDING_SCHEMAS_ORIGIN_MODEL_RESOLVER_MODEL_TYPE_CHECKER_AND_SIX_PROPOSED_CLARIFICATIONS_ONLY",
        "non_claims":["NOT_REGENERATED_CUSTOM_ASTS","NOT_REGENERATED_FIXTURES","NOT_RUNTIME_EVIDENCE","NOT_BRD_UXF_EDIT","NOT_FINAL_PHASE_2C_BASELINE","NOT_RUNTIME_ADAPTER_IMPLEMENTATION","NOT_YADF_IMPLEMENTATION"],
        "brd_uxf":"UNCHANGED","approval_block":{"decision":"PENDING","approver":None,"signature":None,"date":None},
        "generated_payload_aggregate_sha256":aggregate(outputs),"file_sha256":{path:sha(data) for path,data in sorted(outputs.items())},
    }
    outputs["docs/baselines/v2.3/phase-2/operator-binding-type-model-manifest.json"]=canonical(manifest)
    return outputs


def main() -> int:
    parser=argparse.ArgumentParser();parser.add_argument("--check",action="store_true");args=parser.parse_args();outputs=build_outputs();bad=[]
    for name,data in outputs.items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_bytes()!=data:bad.append(name)
        else:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
    if bad:raise SystemExit("NONDETERMINISTIC_OR_STALE:"+",".join(bad))
    print("PASS — DETERMINISTIC_OPERATOR_BINDING_TYPE_MODEL_C1" if args.check else f"GENERATED — {CANDIDATE} — {len(outputs)} artifacts")
    return 0


if __name__=="__main__":raise SystemExit(main())
