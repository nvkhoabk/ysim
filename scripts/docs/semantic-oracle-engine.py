#!/usr/bin/env python3
"""Executable model-conformance engine for Phase 2C Semantic Oracle Model C2."""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from typing import Any, Callable, Mapping


class EngineError(ValueError):
    def __init__(self, code: str, detail: str) -> None:
        super().__init__(f"{code}: {detail}")
        self.code = code


def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


class TrackedBindings(Mapping[str, Any]):
    def __init__(self, values: dict[str, Any]) -> None:
        self.values = values
        self.read: set[str] = set()

    def __getitem__(self, key: str) -> Any:
        self.read.add(key)
        return self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __len__(self) -> int:
        return len(self.values)


@dataclass(frozen=True)
class Evaluation:
    passed: bool
    code: str
    detail: str
    bindings_read: tuple[str, ...]


Evaluator = Callable[[TrackedBindings, dict[str, Any]], bool]
EVALUATORS: dict[str, Evaluator] = {}


def evaluator(operator_id: str):
    def decorate(fn: Evaluator) -> Evaluator:
        if operator_id in EVALUATORS:
            raise RuntimeError(f"duplicate evaluator {operator_id}")
        EVALUATORS[operator_id] = fn
        return fn
    return decorate


@evaluator("CAPABILITY_AVAILABLE")
def eval_capability_available(b, s):
    return bool(b["subject"] and b["capability"] and b["scope"] and s["available"] and s["usable"] and not s["prohibited"])


@evaluator("CAPABILITY_NOT_PLACEHOLDER")
def eval_capability_not_placeholder(b, s):
    return bool(b["subject"] and b["capability"] and b["scope"] and s["usable"] and not s["placeholder"] and not s["prohibited"])


@evaluator("SET_EQUALS")
def eval_set_equals(b, s):
    return set(s["actual_set"]) == set(b["expected_set"]) == set(b["actual_set"]) and not s["prohibited"]


@evaluator("SET_CONTAINS")
def eval_set_contains(b, s):
    return set(b["required_members"]) <= set(s["actual_set"]) and bool(b["actual_set"]) and not s["prohibited"]


@evaluator("SET_EXCLUDES")
def eval_set_excludes(b, s):
    return not (set(b["prohibited_members"]) & set(s["actual_set"])) and bool(b["actual_set"]) and not s["prohibited"]


@evaluator("REFERENCE_TARGET_VALID")
def eval_reference_target_valid(b, s):
    return bool(b["reference"] and b["registry"] and s["resolved"] and s["target_state"] in b["allowed_states"] and not s["prohibited"])


@evaluator("OWNER_EQUALS")
def eval_owner_equals(b, s):
    return bool(b["entity"] and b["actual_owner"] == b["expected_owner"] == s["observed_owner"] and not s["prohibited"])


@evaluator("TENANT_ISOLATED")
def eval_tenant_isolated(b, s):
    permitted = b["actor_tenant"] == b["resource_tenant"] or s["relationship_authorized"]
    return bool(b["permission_context"] and s["access_allowed"] == permitted and not s["cross_tenant_disclosure"])


@evaluator("ACTOR_AUTHORIZED")
def eval_actor_authorized(b, s):
    return bool(b["actor"] and b["action"] and b["resource"] and b["effective_policy"] and s["entitled"] and s["decision"] == "ALLOW")


@evaluator("ACTOR_DENIED")
def eval_actor_denied(b, s):
    return bool(b["actor"] and b["action"] and b["resource"] and b["effective_policy"] and not s["entitled"] and s["decision"] == "DENY")


@evaluator("STATE_TRANSITION_ALLOWED")
def eval_state_transition_allowed(b, s):
    return bool(b["state_machine"] and s["before"] == b["from_state"] and s["trigger"] == b["trigger"] and s["after"] == b["to_state"] and s["accepted"])


@evaluator("STATE_TRANSITION_REJECTED")
def eval_state_transition_rejected(b, s):
    return bool(b["state_machine"] and s["before"] == b["from_state"] and s["trigger"] == b["trigger"] and s["after"] != b["prohibited_state"] and not s["accepted"])


@evaluator("EVENT_EMITTED")
def eval_event_emitted(b, s):
    return bool(b["event_id"] and b["trigger"] and s["count"] == 1 and s["correlation_id"] == b["correlation_id"] and not s["suppressed"])


@evaluator("EVENT_NOT_EMITTED")
def eval_event_not_emitted(b, s):
    return bool(b["event_id"] and b["condition"] and b["observation_window"] and s["count"] == 0 and not s["prohibited"])


@evaluator("EVENT_ORDER_PRESERVED")
def eval_event_order_preserved(b, s):
    return bool(b["event_family"] and b["correlation_id"] and s["observed_sequence"] == b["expected_sequence"] and not s["order_violation"])


@evaluator("EVENT_ORDER_NOT_REQUIRED")
def eval_event_order_not_required(b, s):
    return bool(b["event_family"] and b["scope"] and b["ordering_policy"] and s["classification"] == "UNORDERED" and not s["forced_ordering"])


@evaluator("POLICY_OUTCOME_EQUALS")
def eval_policy_outcome_equals(b, s):
    return bool(b["policy"] and b["policy_inputs"] and s["observed_outcome"] == b["expected_outcome"] and not s["prohibited"])


@evaluator("APPROVAL_REQUIRED")
def eval_approval_required(b, s):
    return bool(b["action"] and b["approval_policy"] and b["approval_reference"] and s["approval_valid"] and s["approval_at"] < s["action_at"] and not s["bypassed"])


@evaluator("CONFIGURATION_RESOLVES")
def eval_configuration_resolves(b, s):
    return bool(b["configuration_key"] and b["configuration_sources"] and s["valid"] and s["effective_value"] == b["expected_value"] and not s["conflict"])


@evaluator("SAFE_FALLBACK_USED")
def eval_safe_fallback_used(b, s):
    return bool(b["failure_condition"] and b["affected_experience"] and s["selected_fallback"] == b["fallback"] and s["continued"] and not s["unsafe_default"])


@evaluator("FAIL_CLOSED")
def eval_fail_closed(b, s):
    return bool(b["failure_condition"] and b["protected_action"] and s["resulting_state"] == b["denied_state"] and not s["action_allowed"] and not s["unsafe_default"])


@evaluator("PAYMENT_INITIATION_ALLOWED")
def eval_payment_initiation_allowed(b, s):
    return bool(b["order_id"] and s["gate_result"] == b["commercial_gate_result"] == "PASS" and s["payment_state"] == b["payment_state"] and s["gate_at"] < s["payment_at"])


@evaluator("PAYMENT_INITIATION_BLOCKED")
def eval_payment_initiation_blocked(b, s):
    return bool(b["order_id"] and b["failed_checks"] and set(b["blocked_states"]).isdisjoint({s["payment_state"]}) and not s["authorization_started"])


@evaluator("PROCUREMENT_FEASIBLE")
def eval_procurement_feasible(b, s):
    return bool(b["order_id"] and b["supplier_terms"] and b["capacity"] and b["coverage_policy"] and s["terms_valid"] and s["whole_order_capacity"] and not s["partial"])


@evaluator("PROCUREMENT_NOT_FEASIBLE")
def eval_procurement_not_feasible(b, s):
    return bool(b["order_id"] and b["failure_reason"] and b["dependent_action"] and not s["feasible"] and not s["dependent_action_allowed"])


@evaluator("EVIDENCE_FIELD_PRESENT")
def eval_evidence_field_present(b, s):
    return bool(b["evidence_object"] and set(b["required_fields"]) <= set(s["present_fields"]) and not s["invalid_field"])


@evaluator("SCOPE_ACTIVE")
def eval_scope_active(b, s):
    return bool(b["subject"] and b["baseline"] and b["scope"] and s["active"] and not s["future_only"])


@evaluator("SCOPE_NOT_ACTIVE")
def eval_scope_not_active(b, s):
    return bool(b["subject"] and b["baseline"] and b["inactive_scope"] and not s["active"] and s["extension_only"])


@evaluator("COMPOSITE_COVERED_BY_CHILDREN")
def eval_composite_covered_by_children(b, s):
    return bool(b["parent_id"] and b["child_ids"] and b["coverage_mode"] == "ALL_CHILDREN" and s["covered_children"] == b["child_ids"] and not any(s["unit_flags"].values()))


@evaluator("ENUM_VALUE_ALLOWED")
def eval_enum_value_allowed(b, s):
    return bool(b["field"] and b["allowed_values"] and s["actual_value"] == b["actual_value"] and s["actual_value"] in b["allowed_values"])


@evaluator("ROLE_LIST_CONSISTENT")
def eval_role_list_consistent(b, s):
    return bool(b["role"] and b["role_rules"] and b["dependent_lists"] and s["required_lists_present"] and not s["prohibited_lists_present"])


@evaluator("AUDIT_IMMUTABLE")
def eval_audit_immutable(b, s):
    return bool(b["audit_record"] and b["immutability_boundary"] and set(b["required_fields"]) <= set(s["present_fields"]) and not s["modified"] and not s["deleted"])


@evaluator("RETRY_LIMIT_NOT_EXCEEDED")
def eval_retry_limit_not_exceeded(b, s):
    return bool(b["operation"] and b["retry_count"] <= b["retry_limit"] and s["attempts"] <= b["retry_limit"] and not s["attempt_after_terminal"])


@evaluator("CONFIGURATION_PRECEDENCE")
def eval_configuration_precedence(b, s):
    order = b["precedence_order"] if isinstance(b["precedence_order"],list) else [b["precedence_order"]]
    available = [name for name in order if name in b["source_values"]]
    return bool(b["configuration_key"] and available and s["selected_source"] == available[0] and not s["reversed"])


@evaluator("RECONCILIATION_BALANCED")
def eval_reconciliation_balanced(b, s):
    return bool(b["correlation_id"] and b["currency"] and b["debits"] == b["credits"] and s["difference"] == 0 and s["currency"] == b["currency"])


@evaluator("DELIVERY_TERMINAL_STATE")
def eval_delivery_terminal_state(b, s):
    return bool(b["delivery_id"] and b["allowed_terminal_states"] and s["observed_state"] == b["observed_state"] and s["observed_state"] in b["allowed_terminal_states"] and not s["exited_terminal"])


@evaluator("DATA_RETENTION_WINDOW")
def eval_data_retention_window(b, s):
    return bool(b["data_class"] and b["retention_window"] > 0 and b["terminal_action"] and s["age"] <= b["retention_window"] and not s["removed_early"])


@evaluator("ACCESSIBILITY_CONFORMS")
def eval_accessibility_conforms(b, s):
    return bool(b["experience"] and b["accessibility_standard"] and b["required_outcomes"] and set(b["required_outcomes"]) <= set(s["passed_outcomes"]) and not s["disabled"])


@evaluator("PERFORMANCE_WITHIN_BUDGET")
def eval_performance_within_budget(b, s):
    return bool(b["service"] and b["metric"] and s["observed_value"] == b["observed_value"] and b["observed_value"] <= b["budget"] and not s["unobservable"])


@evaluator("MFA_CHALLENGE_REQUIRED")
def eval_mfa_challenge_required(b, s):
    return bool(b["principal"] and b["policy_scope"] and b["effective_policy"] and s["challenge_result"] == b["challenge_result"] and not s["bypassed"] and s["audit_present"])


def _bindings(operator: dict[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(operator["valid_examples"][0]["bindings"])


def _specs() -> dict[str, dict[str, Any]]:
    """Operator-specific baseline state and independent conformance mutations."""
    return {
        "CAPABILITY_AVAILABLE": {"s":{"available":True,"usable":True,"prohibited":False},"p":["available",False],"n":["prohibited",True]},
        "CAPABILITY_NOT_PLACEHOLDER":{"s":{"usable":True,"placeholder":False,"prohibited":False},"p":["usable",False],"n":["placeholder",True]},
        "SET_EQUALS":{"s":{"actual_set":None,"prohibited":False},"p":["actual_set",[]],"n":["prohibited",True]},
        "SET_CONTAINS":{"s":{"actual_set":None,"prohibited":False},"p":["actual_set",[]],"n":["prohibited",True]},
        "SET_EXCLUDES":{"s":{"actual_set":None,"prohibited":False},"p":["actual_set",None],"n":["prohibited",True]},
        "REFERENCE_TARGET_VALID":{"s":{"resolved":True,"target_state":None,"prohibited":False},"p":["resolved",False],"n":["prohibited",True]},
        "OWNER_EQUALS":{"s":{"observed_owner":None,"prohibited":False},"p":["observed_owner","WRONG_OWNER"],"n":["prohibited",True]},
        "TENANT_ISOLATED":{"s":{"relationship_authorized":False,"access_allowed":True,"cross_tenant_disclosure":False},"p":["access_allowed",False],"n":["cross_tenant_disclosure",True]},
        "ACTOR_AUTHORIZED":{"s":{"entitled":True,"decision":"ALLOW"},"p":["decision","DENY"],"n":["entitled",False]},
        "ACTOR_DENIED":{"s":{"entitled":False,"decision":"DENY"},"p":["decision","ALLOW"],"n":["entitled",True]},
        "STATE_TRANSITION_ALLOWED":{"s":{"before":None,"trigger":None,"after":None,"accepted":True},"p":["after","WRONG_STATE"],"n":["accepted",False]},
        "STATE_TRANSITION_REJECTED":{"s":{"before":None,"trigger":None,"after":"UNCHANGED","accepted":False},"p":["after",None],"n":["accepted",True]},
        "EVENT_EMITTED":{"s":{"count":1,"correlation_id":None,"suppressed":False},"p":["count",0],"n":["suppressed",True]},
        "EVENT_NOT_EMITTED":{"s":{"count":0,"prohibited":False},"p":["count",1],"n":["prohibited",True]},
        "EVENT_ORDER_PRESERVED":{"s":{"observed_sequence":None,"order_violation":False},"p":["observed_sequence",[]],"n":["order_violation",True]},
        "EVENT_ORDER_NOT_REQUIRED":{"s":{"classification":"UNORDERED","forced_ordering":False},"p":["classification","ORDERED"],"n":["forced_ordering",True]},
        "POLICY_OUTCOME_EQUALS":{"s":{"observed_outcome":None,"prohibited":False},"p":["observed_outcome","WRONG_OUTCOME"],"n":["prohibited",True]},
        "APPROVAL_REQUIRED":{"s":{"approval_valid":True,"approval_at":1,"action_at":2,"bypassed":False},"p":["approval_valid",False],"n":["bypassed",True]},
        "CONFIGURATION_RESOLVES":{"s":{"valid":True,"effective_value":None,"conflict":False},"p":["valid",False],"n":["conflict",True]},
        "SAFE_FALLBACK_USED":{"s":{"selected_fallback":None,"continued":True,"unsafe_default":False},"p":["continued",False],"n":["unsafe_default",True]},
        "FAIL_CLOSED":{"s":{"resulting_state":None,"action_allowed":False,"unsafe_default":False},"p":["action_allowed",True],"n":["unsafe_default",True]},
        "PAYMENT_INITIATION_ALLOWED":{"s":{"gate_result":"PASS","payment_state":None,"gate_at":1,"payment_at":2},"p":["gate_result","FAIL"],"n":["payment_at",0]},
        "PAYMENT_INITIATION_BLOCKED":{"s":{"payment_state":"BLOCKED","authorization_started":False},"p":["authorization_started",True],"n":["payment_state",None]},
        "PROCUREMENT_FEASIBLE":{"s":{"terms_valid":True,"whole_order_capacity":True,"partial":False},"p":["whole_order_capacity",False],"n":["partial",True]},
        "PROCUREMENT_NOT_FEASIBLE":{"s":{"feasible":False,"dependent_action_allowed":False},"p":["feasible",True],"n":["dependent_action_allowed",True]},
        "EVIDENCE_FIELD_PRESENT":{"s":{"present_fields":None,"invalid_field":False},"p":["present_fields",[]],"n":["invalid_field",True]},
        "SCOPE_ACTIVE":{"s":{"active":True,"future_only":False},"p":["active",False],"n":["future_only",True]},
        "SCOPE_NOT_ACTIVE":{"s":{"active":False,"extension_only":True},"p":["active",True],"n":["extension_only",False]},
        "COMPOSITE_COVERED_BY_CHILDREN":{"s":{"covered_children":None,"unit_flags":{"implementation":False,"acceptance":False,"scope":False,"criticality":False}},"p":["covered_children",[]],"n":["unit_flags",{"implementation":True,"acceptance":False,"scope":False,"criticality":False}]},
        "ENUM_VALUE_ALLOWED":{"s":{"actual_value":None},"p":["actual_value","UNKNOWN"],"n":["actual_value","PROHIBITED"]},
        "ROLE_LIST_CONSISTENT":{"s":{"required_lists_present":True,"prohibited_lists_present":False},"p":["required_lists_present",False],"n":["prohibited_lists_present",True]},
        "AUDIT_IMMUTABLE":{"s":{"present_fields":None,"modified":False,"deleted":False},"p":["present_fields",[]],"n":["modified",True]},
        "RETRY_LIMIT_NOT_EXCEEDED":{"s":{"attempts":None,"attempt_after_terminal":False},"p":["attempts",999],"n":["attempt_after_terminal",True]},
        "CONFIGURATION_PRECEDENCE":{"s":{"selected_source":None,"reversed":False},"p":["selected_source","WRONG_SOURCE"],"n":["reversed",True]},
        "RECONCILIATION_BALANCED":{"s":{"difference":0,"currency":None},"p":["difference",1],"n":["currency","WRONG_CURRENCY"]},
        "DELIVERY_TERMINAL_STATE":{"s":{"observed_state":None,"exited_terminal":False},"p":["observed_state","UNKNOWN"],"n":["exited_terminal",True]},
        "DATA_RETENTION_WINDOW":{"s":{"age":0,"removed_early":False},"p":["age",999],"n":["removed_early",True]},
        "ACCESSIBILITY_CONFORMS":{"s":{"passed_outcomes":None,"disabled":False},"p":["passed_outcomes",[]],"n":["disabled",True]},
        "PERFORMANCE_WITHIN_BUDGET":{"s":{"observed_value":None,"unobservable":False},"p":["observed_value",999999],"n":["unobservable",True]},
        "MFA_CHALLENGE_REQUIRED":{"s":{"challenge_result":None,"bypassed":False,"audit_present":True},"p":["challenge_result","NOT_COMPLETED"],"n":["bypassed",True]},
    }


CASE_SPECS = _specs()


def build_fixture(operator: dict[str, Any]) -> dict[str, Any]:
    op = operator["operator_id"]
    if op not in CASE_SPECS:
        raise EngineError("MISSING_EVALUATOR_FIXTURE", op)
    b = _bindings(operator)
    s = copy.deepcopy(CASE_SPECS[op]["s"])
    if op == "SET_EQUALS": s["actual_set"] = copy.deepcopy(b["expected_set"]); b["actual_set"] = copy.deepcopy(b["expected_set"])
    elif op == "SET_CONTAINS": s["actual_set"] = copy.deepcopy(b["required_members"]); b["actual_set"] = copy.deepcopy(b["required_members"])
    elif op == "SET_EXCLUDES": s["actual_set"] = ["ALLOWED_MEMBER"]; b["actual_set"] = ["ALLOWED_MEMBER"]
    elif op == "REFERENCE_TARGET_VALID": s["target_state"] = b["allowed_states"][0]
    elif op == "OWNER_EQUALS": b["actual_owner"] = b["expected_owner"]; s["observed_owner"] = b["expected_owner"]
    elif op == "TENANT_ISOLATED": b["resource_tenant"] = b["actor_tenant"]
    elif op == "STATE_TRANSITION_ALLOWED": s.update(before=b["from_state"],trigger=b["trigger"],after=b["to_state"])
    elif op == "STATE_TRANSITION_REJECTED": s.update(before=b["from_state"],trigger=b["trigger"]); s["after"] = "UNCHANGED" if b["prohibited_state"] != "UNCHANGED" else "OTHER"
    elif op == "EVENT_EMITTED": s["correlation_id"] = b["correlation_id"]
    elif op == "EVENT_ORDER_PRESERVED": s["observed_sequence"] = copy.deepcopy(b["expected_sequence"])
    elif op == "POLICY_OUTCOME_EQUALS": s["observed_outcome"] = copy.deepcopy(b["expected_outcome"])
    elif op == "CONFIGURATION_RESOLVES": s["effective_value"] = copy.deepcopy(b["expected_value"])
    elif op == "SAFE_FALLBACK_USED": s["selected_fallback"] = b["fallback"]
    elif op == "FAIL_CLOSED": s["resulting_state"] = b["denied_state"]
    elif op == "PAYMENT_INITIATION_ALLOWED": b["commercial_gate_result"]="PASS"; s["payment_state"] = b["payment_state"]
    elif op == "PAYMENT_INITIATION_BLOCKED": s["payment_state"] = "BLOCKED" if "BLOCKED" not in b["blocked_states"] else "NOT_STARTED"
    elif op == "EVIDENCE_FIELD_PRESENT": s["present_fields"] = copy.deepcopy(b["required_fields"])
    elif op == "COMPOSITE_COVERED_BY_CHILDREN": b["coverage_mode"]="ALL_CHILDREN"; s["covered_children"] = copy.deepcopy(b["child_ids"])
    elif op == "ENUM_VALUE_ALLOWED": b["actual_value"] = b["allowed_values"][0]; s["actual_value"] = b["actual_value"]
    elif op == "AUDIT_IMMUTABLE": s["present_fields"] = copy.deepcopy(b["required_fields"])
    elif op == "RETRY_LIMIT_NOT_EXCEEDED": s["attempts"] = b["retry_count"]
    elif op == "CONFIGURATION_PRECEDENCE": b["source_values"] = [b["precedence_order"]]; s["selected_source"] = b["precedence_order"]
    elif op == "RECONCILIATION_BALANCED": b["credits"] = b["debits"]; s["currency"] = b["currency"]
    elif op == "DELIVERY_TERMINAL_STATE": b["observed_state"] = b["allowed_terminal_states"][0]; s["observed_state"] = b["observed_state"]
    elif op == "ACCESSIBILITY_CONFORMS": s["passed_outcomes"] = copy.deepcopy(b["required_outcomes"])
    elif op == "PERFORMANCE_WITHIN_BUDGET": b["observed_value"] = min(b["observed_value"],b["budget"]); s["observed_value"] = b["observed_value"]
    elif op == "MFA_CHALLENGE_REQUIRED": s["challenge_result"] = b["challenge_result"]
    s["boundary_valid"] = True
    evidence={name:f"observed:{op}:{name}" for name in operator["required_evidence_schema"]["required"]}
    return {"fixture_id":f"FIX-{op}","operator_id":op,"operator_version":operator["version"],"verification_mode":operator["verification_mode"],"execution_layer":"MODEL_CONFORMANCE_EXECUTED","bindings":b,"observed":s,"evidence":evidence,"boundary":{"left":{"case":"APPLICABLE"},"right":{"case":"NON_APPLICABLE"}},"provenance":{"source":"OPERATOR_CATALOG_CONFORMANCE_FIXTURE","inference":False}}


def _type_ok(value: Any, expected: str) -> bool:
    return {"string":isinstance(value,str) and bool(value),"array":isinstance(value,list) and bool(value),"number":isinstance(value,(int,float)) and not isinstance(value,bool),"boolean":isinstance(value,bool),"object":isinstance(value,dict)}.get(expected,False)


def evaluate_fixture(fixture: dict[str, Any], catalog: dict[str, dict[str, Any]], registry: dict[str, Evaluator] | None=None, *, require_all_bindings: bool=True) -> Evaluation:
    registry=registry or EVALUATORS; op_id=fixture.get("operator_id")
    if op_id not in catalog or op_id not in registry: raise EngineError("MISSING_OR_UNKNOWN_EVALUATOR",str(op_id))
    op=catalog[op_id]
    if fixture.get("verification_mode")=="MANUAL" and fixture.get("execution_layer")!="HUMAN_VERIFICATION_REQUIRED": raise EngineError("MANUAL_ORACLE_MARKED_EXECUTABLE",op_id)
    if fixture.get("operator_version")!=op["version"]: raise EngineError("OPERATOR_VERSION_MISMATCH",op_id)
    b=fixture.get("bindings",{}); required=set(op["required_bindings"])
    if set(b)!=required: raise EngineError("BINDING_SCHEMA_MISMATCH",f"{op_id}:{sorted(required-set(b))}")
    for name,value in b.items():
        if not _type_ok(value,op["input_json_schema"]["properties"][name]["type"]):raise EngineError("BINDING_SCHEMA_MISMATCH",f"{op_id}.{name}")
    evidence=fixture.get("evidence",{}); missing=set(op["required_evidence_schema"]["required"])-set(evidence)
    if missing: raise EngineError("MISSING_EVIDENCE",f"{op_id}:{sorted(missing)}")
    boundary=fixture.get("boundary",{})
    if boundary.get("left")==boundary.get("right"): raise EngineError("BOUNDARY_NOT_DISTINCT",op_id)
    tracked=TrackedBindings(b)
    try: passed=bool(registry[op_id](tracked,fixture["observed"]))
    except EngineError: raise
    except Exception as exc: raise EngineError("EVALUATOR_EXCEPTION",f"{op_id}:{type(exc).__name__}:{exc}") from exc
    passed = passed and fixture["observed"].get("boundary_valid", True) is True
    unused=required-tracked.read
    if require_all_bindings and unused: raise EngineError("UNUSED_REQUIRED_BINDING",f"{op_id}:{sorted(unused)}")
    return Evaluation(passed,"PASS" if passed else "ASSERTION_VIOLATED",op["assertion_semantics"] if passed else op["violation_semantics"],tuple(sorted(tracked.read)))


def _resolve(container: dict[str, Any], path: str) -> tuple[Any,str,Any]:
    if not path.startswith("/"): raise EngineError("INVALID_MUTATION_TARGET",path)
    parts=[p for p in path.split("/") if p]; current:Any=container
    for part in parts[:-1]:
        if not isinstance(current,dict) or part not in current: raise EngineError("MISSING_MUTATION_TARGET",path)
        current=current[part]
    key=parts[-1]
    if not isinstance(current,dict) or key not in current: raise EngineError("MISSING_MUTATION_TARGET",path)
    return current,key,current[key]


def apply_mutation(fixture: dict[str, Any], mutation: dict[str, Any]) -> tuple[dict[str, Any],dict[str, str]]:
    if "actual_detection" in mutation or "execution_result" in mutation: raise EngineError("PREMARKED_RESULT_FORBIDDEN",mutation.get("mutation_id","unknown"))
    operation=mutation.get("operation")
    if operation not in {"SET_VALUE","REMOVE_FIELD"}: raise EngineError("UNKNOWN_MUTATION_OPERATOR",str(operation))
    mutant=copy.deepcopy(fixture); parent,key,original=_resolve(mutant,mutation.get("target_path",""))
    if operation=="SET_VALUE":
        value=copy.deepcopy(mutation.get("mutated_value"))
        if value==original: raise EngineError("NO_OP_MUTATION",mutation.get("mutation_id","unknown"))
        parent[key]=value
    else:
        del parent[key]
    original_hash=digest(fixture); mutant_hash=digest(mutant)
    if original_hash==mutant_hash: raise EngineError("NO_OP_MUTATION",mutation.get("mutation_id","unknown"))
    return mutant,{"original_sha256":original_hash,"mutant_sha256":mutant_hash}


def execute_mutation(fixture: dict[str, Any], mutation: dict[str, Any], catalog: dict[str, dict[str, Any]], registry: dict[str, Evaluator] | None=None) -> dict[str, Any]:
    baseline=evaluate_fixture(fixture,catalog,registry)
    mutant,hashes=apply_mutation(fixture,mutation)
    try:
        changed=evaluate_fixture(mutant,catalog,registry,require_all_bindings=False)
        detection="KILLED" if baseline.passed and not changed.passed else "SURVIVED"
        mutant_result={"status":changed.code,"passed":changed.passed,"detail":changed.detail}
    except EngineError as exc:
        detection="ERROR_NOT_KILLED";mutant_result={"status":exc.code,"passed":False,"detail":str(exc)}
    return {"mutation_id":mutation["mutation_id"],"operator_id":fixture["operator_id"],"mutation_class":mutation["mutation_class"],"target_path":mutation["target_path"],"original_value":mutation.get("original_value"),"mutated_value":mutation.get("mutated_value"),**hashes,"baseline":{"status":baseline.code,"passed":baseline.passed},"mutant":mutant_result,"actual_detection":detection,"execution_layer":"MODEL_CONFORMANCE_EXECUTED"}


def conformance_mutations(fixture: dict[str, Any]) -> list[dict[str, Any]]:
    spec=CASE_SPECS[fixture["operator_id"]]
    positive_value=spec["p"][1];negative_value=spec["n"][1]
    if fixture["operator_id"]=="PAYMENT_INITIATION_BLOCKED": negative_value=fixture["bindings"]["blocked_states"][0]
    if fixture["operator_id"]=="STATE_TRANSITION_REJECTED": positive_value=fixture["bindings"]["prohibited_state"]
    if fixture["operator_id"]=="SET_EXCLUDES": positive_value=list(fixture["bindings"]["prohibited_members"])
    return [
        {"mutation_id":f"{fixture['operator_id']}-POS","mutation_class":"POSITIVE_MUTATION","operation":"SET_VALUE","target_path":f"/observed/{spec['p'][0]}","original_value":fixture["observed"][spec["p"][0]],"mutated_value":positive_value},
        {"mutation_id":f"{fixture['operator_id']}-NEG","mutation_class":"NEGATIVE_MUTATION","operation":"SET_VALUE","target_path":f"/observed/{spec['n'][0]}","original_value":fixture["observed"][spec["n"][0]],"mutated_value":negative_value},
        {"mutation_id":f"{fixture['operator_id']}-BOUND","mutation_class":"BOUNDARY_MUTATION","operation":"SET_VALUE","target_path":"/observed/boundary_valid","original_value":True,"mutated_value":False},
    ]


def run_operator_conformance(catalog_data: dict[str, Any]) -> dict[str, Any]:
    catalog={op["operator_id"]:op for op in catalog_data["operators"]};rows=[]
    for op_id in sorted(catalog):
        op=catalog[op_id];fixture=build_fixture(op);baseline=evaluate_fixture(fixture,catalog)
        invalid=copy.deepcopy(fixture);invalid["bindings"].pop(op["required_bindings"][0])
        try:evaluate_fixture(invalid,catalog);invalid_rejected=False
        except EngineError as exc:invalid_rejected=exc.code=="BINDING_SCHEMA_MISMATCH"
        missing=copy.deepcopy(fixture);missing["evidence"].pop(op["required_evidence_schema"]["required"][0])
        try:evaluate_fixture(missing,catalog);evidence_rejected=False
        except EngineError as exc:evidence_rejected=exc.code=="MISSING_EVIDENCE"
        counter=copy.deepcopy(fixture);spec=CASE_SPECS[op_id];counter["observed"][spec["n"][0]]=copy.deepcopy(conformance_mutations(fixture)[1]["mutated_value"]);counter_eval=evaluate_fixture(counter,catalog,require_all_bindings=False)
        executions=[execute_mutation(fixture,m,catalog) for m in conformance_mutations(fixture)]
        noop=conformance_mutations(fixture)[0];noop["mutated_value"]=noop["original_value"]
        try:apply_mutation(fixture,noop);noop_rejected=False
        except EngineError as exc:noop_rejected=exc.code=="NO_OP_MUTATION"
        rows.append({"operator_id":op_id,"verification_mode":op["verification_mode"],"schema_validation":"PASS","valid_baseline_evaluation":"PASS" if baseline.passed else "FAIL","invalid_binding_rejection":"PASS" if invalid_rejected else "FAIL","positive_mutation":"PASS" if executions[0]["actual_detection"]=="KILLED" else "FAIL","negative_mutation":"PASS" if executions[1]["actual_detection"]=="KILLED" else "FAIL","boundary_mutation":"PASS" if executions[2]["actual_detection"]=="KILLED" else "FAIL","missing_evidence_rejection":"PASS" if evidence_rejected else "FAIL","no_op_rejection":"PASS" if noop_rejected else "FAIL","counterexample_rejection":"PASS" if not counter_eval.passed else "FAIL","required_binding_usage":"PASS" if set(baseline.bindings_read)==set(op["required_bindings"]) else "FAIL","execution_records":executions})
    return {"operator_count":len(rows),"passed":sum(all(row[k]=="PASS" for k in ["schema_validation","valid_baseline_evaluation","invalid_binding_rejection","positive_mutation","negative_mutation","boundary_mutation","missing_evidence_rejection","no_op_rejection","counterexample_rejection","required_binding_usage"]) for row in rows),"rows":rows}


def run_adversarial(catalog_data: dict[str, Any]) -> dict[str, Any]:
    from collections import OrderedDict
    catalog={op["operator_id"]:op for op in catalog_data["operators"]};op=catalog["CAPABILITY_AVAILABLE"];base=build_fixture(op);good=conformance_mutations(base)[0]
    tests=OrderedDict()
    tests["NO_OP_MUTATION"]=(lambda:apply_mutation(base,{**good,"mutated_value":good["original_value"]}),"NO_OP_MUTATION")
    tests["UNKNOWN_MUTATION_OPERATOR"]=(lambda:apply_mutation(base,{**good,"operation":"UNKNOWN"}),"UNKNOWN_MUTATION_OPERATOR")
    tests["MISSING_MUTATION_TARGET"]=(lambda:apply_mutation(base,{**good,"target_path":"/observed/missing"}),"MISSING_MUTATION_TARGET")
    tests["MUTATED_VALUE_EQUALS_ORIGINAL"]=(lambda:apply_mutation(base,{**good,"mutated_value":good["original_value"]}),"NO_OP_MUTATION")
    def always_true(b,s):return True
    tests["EVALUATOR_ALWAYS_TRUE"]=(lambda:evaluate_fixture(copy.deepcopy({**base,"observed":{**base["observed"],"prohibited":True}}),catalog,{**EVALUATORS,"CAPABILITY_AVAILABLE":always_true}),"UNUSED_REQUIRED_BINDING")
    def ignores_capability(b,s):return bool(b["subject"] and s["available"])
    tests["EVALUATOR_IGNORES_MUTATED_BINDING"]=(lambda:evaluate_fixture(base,catalog,{**EVALUATORS,"CAPABILITY_AVAILABLE":ignores_capability}),"UNUSED_REQUIRED_BINDING")
    no_evidence=copy.deepcopy(base);no_evidence["evidence"]={}
    tests["MISSING_EVIDENCE"]=(lambda:evaluate_fixture(no_evidence,catalog),"MISSING_EVIDENCE")
    tests["PREMARKED_KILLED"]=(lambda:apply_mutation(base,{**good,"actual_detection":"KILLED"}),"PREMARKED_RESULT_FORBIDDEN")
    same_boundary=copy.deepcopy(base);same_boundary["boundary"]["right"]=copy.deepcopy(same_boundary["boundary"]["left"])
    tests["BOUNDARY_LEFT_EQUALS_RIGHT"]=(lambda:evaluate_fixture(same_boundary,catalog),"BOUNDARY_NOT_DISTINCT")
    manual=copy.deepcopy(base);manual["verification_mode"]="MANUAL"
    tests["MANUAL_MARKED_EXECUTABLE"]=(lambda:evaluate_fixture(manual,catalog),"MANUAL_ORACLE_MARKED_EXECUTABLE")
    rows=[]
    for name,(call,expected) in tests.items():
        try:call();actual="UNSAFE_PASS";passed=False
        except EngineError as exc:actual=exc.code;passed=exc.code==expected
        rows.append({"case":name,"expected_rejection":expected,"actual":actual,"result":"PASS" if passed else "FAIL"})
    return {"total":len(rows),"passed":sum(r["result"]=="PASS" for r in rows),"rows":rows}


INDEPENDENT_CHALLENGES = [
    ("CAPABILITY_ABSENT","CAPABILITY_AVAILABLE","/observed/available",False),("PLACEHOLDER_CAPABILITY","CAPABILITY_NOT_PLACEHOLDER","/observed/placeholder",True),("REQUIRED_ENUM_MEMBER_MISSING","SET_CONTAINS","/observed/actual_set",[]),("PROHIBITED_ENUM_MEMBER_ADDED","SET_EXCLUDES","/observed/prohibited",True),("DANGLING_REFERENCE","REFERENCE_TARGET_VALID","/observed/resolved",False),("RETIRED_ALIAS_USED","REFERENCE_TARGET_VALID","/observed/target_state","RETIRED"),("WRONG_OWNER","OWNER_EQUALS","/observed/observed_owner","OTHER_OWNER"),("CROSS_TENANT_DISCLOSURE","TENANT_ISOLATED","/observed/cross_tenant_disclosure",True),("UNAUTHORIZED_ACTOR_ALLOWED","ACTOR_DENIED","/observed/decision","ALLOW"),("MFA_BYPASS","MFA_CHALLENGE_REQUIRED","/observed/bypassed",True),("APPROVAL_MISSING","APPROVAL_REQUIRED","/observed/approval_valid",False),("INVALID_STATE_TRANSITION","STATE_TRANSITION_ALLOWED","/observed/after","WRONG"),("TERMINAL_STATE_EXITED","DELIVERY_TERMINAL_STATE","/observed/exited_terminal",True),("REQUIRED_EVENT_SUPPRESSED","EVENT_EMITTED","/observed/suppressed",True),("DUPLICATE_EVENT","EVENT_EMITTED","/observed/count",2),("FINANCIAL_EVENT_ORDER_INVERTED","EVENT_ORDER_PRESERVED","/observed/order_violation",True),("RETRY_LIMIT_EXCEEDED","RETRY_LIMIT_NOT_EXCEEDED","/observed/attempts",999),("AUDIT_RECORD_MODIFIED","AUDIT_IMMUTABLE","/observed/modified",True),("RETENTION_WINDOW_VIOLATED","DATA_RETENTION_WINDOW","/observed/age",999),("CONFIGURATION_PRECEDENCE_REVERSED","CONFIGURATION_PRECEDENCE","/observed/reversed",True),("CRITICAL_CONFIG_USES_FALLBACK","FAIL_CLOSED","/observed/action_allowed",True),("NON_CRITICAL_PRESENTATION_FAILS_CLOSED","SAFE_FALLBACK_USED","/observed/continued",False),("PAYMENT_BEFORE_GATE","PAYMENT_INITIATION_ALLOWED","/observed/gate_result","FAIL"),("PROCUREMENT_INFEASIBLE_PAYMENT_ALLOWED","PAYMENT_INITIATION_BLOCKED","/observed/authorization_started",True),("PARTIAL_PROCUREMENT","PROCUREMENT_FEASIBLE","/observed/partial",True),("SETTLEMENT_IMBALANCE","RECONCILIATION_BALANCED","/observed/difference",1),("PERFORMANCE_BUDGET_EXCEEDED","PERFORMANCE_WITHIN_BUDGET","/observed/observed_value",999999),("ACCESSIBILITY_VIOLATED","ACCESSIBILITY_CONFORMS","/observed/disabled",True),("FUTURE_FEATURE_EXPOSED_ACTIVE","SCOPE_NOT_ACTIVE","/observed/active",True),("COMPOSITE_PARENT_IMPLEMENTATION_UNIT","COMPOSITE_COVERED_BY_CHILDREN","/observed/unit_flags",{"implementation":True,"acceptance":False,"scope":False,"criticality":False}),
    ("AUTHORIZED_ACTOR_DENIED","ACTOR_AUTHORIZED","/observed/decision","DENY"),
    ("CONFIGURATION_INVALID","CONFIGURATION_RESOLVES","/observed/valid",False),
    ("ENUM_UNKNOWN_VALUE","ENUM_VALUE_ALLOWED","/observed/actual_value","UNKNOWN"),
    ("PROHIBITED_EVENT_EMITTED","EVENT_NOT_EMITTED","/observed/count",1),
    ("UNORDERED_FAMILY_FORCED_ORDER","EVENT_ORDER_NOT_REQUIRED","/observed/forced_ordering",True),
    ("REQUIRED_EVIDENCE_FIELD_REMOVED","EVIDENCE_FIELD_PRESENT","/observed/present_fields",[]),
    ("POLICY_WRONG_OUTCOME","POLICY_OUTCOME_EQUALS","/observed/observed_outcome","WRONG_OUTCOME"),
    ("INFEASIBLE_DEPENDENT_ACTION_ALLOWED","PROCUREMENT_NOT_FEASIBLE","/observed/dependent_action_allowed",True),
    ("ROLE_REQUIRED_LIST_MISSING","ROLE_LIST_CONSISTENT","/observed/required_lists_present",False),
    ("ACTIVE_SCOPE_MARKED_FUTURE","SCOPE_ACTIVE","/observed/future_only",True),
    ("SET_MEMBER_ADDED","SET_EQUALS","/observed/prohibited",True),
    ("PROHIBITED_STATE_ENTERED","STATE_TRANSITION_REJECTED","/observed/after","PROHIBITED_STATE"),
]


def run_independent_challenges(catalog_data: dict[str, Any]) -> dict[str, Any]:
    catalog={op["operator_id"]:op for op in catalog_data["operators"]};rows=[]
    for name,op_id,path,value in INDEPENDENT_CHALLENGES:
        fixture=build_fixture(catalog[op_id]);parent,key,original=_resolve(fixture,path)
        if name=="PROHIBITED_STATE_ENTERED": value=fixture["bindings"]["prohibited_state"]
        result=execute_mutation(fixture,{"mutation_id":f"CHALLENGE-{name}","mutation_class":"INDEPENDENT_CHALLENGE","operation":"SET_VALUE","target_path":path,"original_value":original,"mutated_value":value},catalog)
        rows.append({"challenge":name,**result})
    return {"generated":len(rows),"killed":sum(r["actual_detection"]=="KILLED" for r in rows),"survived":sum(r["actual_detection"]!="KILLED" for r in rows),"rows":rows}


def run_mapping_model_probes(catalog_data: dict[str, Any], sample: list[dict[str, Any]]) -> dict[str, Any]:
    """Execute operator-model probes without claiming requirement/runtime coverage."""
    catalog={op["operator_id"]:op for op in catalog_data["operators"]}
    by_operator={}
    for challenge in INDEPENDENT_CHALLENGES:
        by_operator.setdefault(challenge[1],challenge)
    rows=[]
    for item in sample:
        op_id=item["operator_id"]
        if op_id not in by_operator: raise EngineError("MISSING_INDEPENDENT_CHALLENGE",op_id)
        name,_,path,value=by_operator[op_id]
        fixture=build_fixture(catalog[op_id]);_,_,original=_resolve(fixture,path)
        if name=="PROHIBITED_STATE_ENTERED": value=fixture["bindings"]["prohibited_state"]
        result=execute_mutation(fixture,{"mutation_id":f"SAMPLE-{item['requirement_id']}-{name}","mutation_class":"INDEPENDENT_MODEL_PROBE","operation":"SET_VALUE","target_path":path,"original_value":original,"mutated_value":value},catalog)
        rows.append({**item,"requirement_semantics_evaluated":False,"runtime_adapter_evaluated":False,"model_operator_result":result})
    return {"sample_size":len(rows),"model_probes_killed":sum(row["model_operator_result"]["actual_detection"]=="KILLED" for row in rows),"requirement_runtime_score":None,"rows":rows}
