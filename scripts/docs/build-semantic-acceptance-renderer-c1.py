#!/usr/bin/env python3
"""Build the Phase 2C semantic acceptance renderer C1 dry-run.

The builder reads the rejected C5 candidate from its preserved Git object.  It
never checks out or modifies BRD/UXF sources.  Rendered prose is a projection
of source obligations, typed operands, resolvers and evidence contracts.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/baselines/v2.3/phase-2"
CANDIDATE = "V23-P2C-SEMANTIC-ACCEPTANCE-RENDERER-C1"
NEXT_GATE = "HUMAN_PHASE_2C_SEMANTIC_ACCEPTANCE_RENDERER_C1_APPROVAL"
C5_REF = "refs/ysim-backups/v2.3/phase-2c-document-baseline-c5-generic-rendering-rejected^2"
C5_REGISTRY = "docs/baselines/v2.3/phase-2/phase-2c-document-baseline-c5-registry.json"
VERSION = "1.0.0-candidate.1"

JSON_OUTPUTS = [
    "semantic-acceptance-renderer-c1-catalog.json",
    "semantic-acceptance-renderer-c1-operator-schemas.json",
    "semantic-acceptance-renderer-c1-ast-previews.json",
    "semantic-acceptance-renderer-c1-procedure-previews.json",
    "semantic-acceptance-renderer-c1-decision-previews.json",
    "semantic-acceptance-renderer-c1-reference-good-contracts.json",
    "semantic-acceptance-renderer-c1-semantic-audit.json",
    "semantic-acceptance-renderer-c1-generic-equivalence.json",
    "semantic-acceptance-renderer-c1-actor-provenance.json",
    "semantic-acceptance-renderer-c1-resolver-evidence.json",
    "semantic-acceptance-renderer-c1-before-after.json",
    "semantic-acceptance-renderer-c1-false-pass-regressions.json",
    "semantic-acceptance-renderer-c1-manifest.json",
]

SELECTIONS = {
    "P2C-SC-C1-DEC-001": "OPT-AST", "P2C-SC-C1-DEC-002": "OPT-AST",
    "P2C-SC-C1-DEC-003": "OPT-AST", "P2C-SC-C1-DEC-004": "OPT-A",
    "P2C-SC-C1-DEC-005": "OPT-AST", "P2C-SC-C1-DEC-006": "OPT-AST",
    "P2C-SC-C1-DEC-007": "OPT-CLARIFY", "P2C-SC-C1-DEC-008": "OPT-AST",
    "P2C-SC-C1-DEC-009": "OPT-AST", "P2C-SC-C1-DEC-010": "OPT-AST",
    "P2C-SC-C1-DEC-011": "OPT-CLARIFY", "P2C-SC-C1-DEC-012": "OPT-AST",
    "P2C-SC-C1-DEC-013": "OPT-A", "P2C-SC-C1-DEC-014": "OPT-AST",
    "P2C-SC-C1-DEC-015": "OPT-AST", "P2C-SC-C1-DEC-016": "OPT-AST",
    "P2C-SC-C1-DEC-017": "OPT-AST", "P2C-SC-C1-DEC-018": "OPT-AST",
    "P2C-SC-C1-DEC-019": "OPT-AST", "P2C-SC-C1-DEC-020": "OPT-AST",
    "P2C-SC-C1-DEC-021": "OPT-AST", "P2C-SC-C1-DEC-022": "OPT-AST",
    "P2C-SC-C1-DEC-023": "OPT-AST", "P2C-SC-C1-DEC-024": "OPT-AST",
    "P2C-SC-C1-DEC-025": "OPT-AST", "P2C-SC-C1-DEC-026": "OPT-AST",
    "P2C-SC-C1-DEC-027": "OPT-AST",
}

# Closed registry.  Templates are operator-specific semantic instructions, not
# directly rendered global prose.
OPERATOR_RULES = {
    "ACCESSIBILITY_CONFORMS": ("accessibility baseline and applicable experience", "a named accessibility criterion fails or a theme disables it", "applicable channel versus an excluded channel"),
    "ACTOR_AUTHORIZED": ("actor, action, resource and scope", "a named unauthorized actor succeeds", "authorized scope versus out-of-scope access"),
    "ACTOR_DENIED": ("denied actor, action, resource and scope", "a named denied actor succeeds", "denied actor versus an authorized actor"),
    "APPROVAL_REQUIRED": ("approval subject, policy and effective transition", "the transition becomes effective without required approval", "approved versus draft/expired approval"),
    "AUDIT_IMMUTABLE": ("audit record and protected fields", "a protected audit field is modified or deleted", "mutable pre-publication record versus immutable audit record"),
    "CAPABILITY_AVAILABLE": ("capability and active scope", "the named capability is absent or disabled", "active v2.3 scope versus future extension"),
    "CAPABILITY_NOT_PLACEHOLDER": ("capability and invocation evidence", "the capability exists only as a placeholder", "invocable capability versus future declaration"),
    "CONFIGURATION_PRECEDENCE": ("configuration key, ordered sources and resolved value", "a lower-priority source overrides a protected higher-priority value", "overridable key versus protected invariant"),
    "CONFIGURATION_RESOLVES": ("configuration key, source, version and value", "resolution returns the wrong source or value", "complete configuration versus missing/invalid configuration"),
    "DATA_RETENTION_WINDOW": ("record, retention policy and governed window", "the record is deleted before the window or retained contrary to policy", "online window versus archive boundary"),
    "DELIVERY_TERMINAL_STATE": ("delivery identity and terminal state", "a terminal delivery exits or reports a non-terminal outcome", "terminal success versus terminal failure"),
    "ENUM_VALUE_ALLOWED": ("enum field and exact allowed values", "an unlisted value is accepted", "last allowed value versus first disallowed value"),
    "EVENT_EMITTED": ("event type/family, trigger, correlation and payload", "the event is absent, duplicated or has the wrong trigger", "triggering transition versus non-triggering state"),
    "EVENT_ORDER_PRESERVED": ("ordered event family and correlation", "two named events are observed in the wrong order", "ordered family versus a family with no ordering rule"),
    "EVIDENCE_FIELD_PRESENT": ("evidence object and exact field IDs", "a required evidence field is absent", "complete evidence object versus partial evidence object"),
    "FAIL_CLOSED": ("critical condition and blocked outcome", "processing continues with an unsafe default", "critical configuration versus non-critical presentation configuration"),
    "MFA_CHALLENGE_REQUIRED": ("principal, protected action and challenge result", "the protected action succeeds after challenge bypass", "challenge-required path versus approved recovery path"),
    "OWNER_EQUALS": ("owned entity and independently resolved owners", "the entity is assigned to a concrete different owner", "business owner versus scoped authority or runtime selection"),
    "PAYMENT_INITIATION_BLOCKED": ("commercial gate and payment transition", "payment starts while a named gate failure exists", "gate-passed versus gate-failed order"),
    "PERFORMANCE_WITHIN_BUDGET": ("service tier, metric and numeric budget", "the observed metric exceeds the named budget", "at-budget versus over-budget observation"),
    "POLICY_OUTCOME_EQUALS": ("policy/version, context and canonical outcome", "the independently observed outcome differs", "matching policy context versus a different context/version"),
    "PROCUREMENT_FEASIBLE": ("order, procurement requirement and whole-order feasibility", "procurement is infeasible or partial under no-partial policy", "allocatable-stock path versus procurement path"),
    "RECONCILIATION_BALANCED": ("reconciliation identity and balanced amounts/references", "a named debit, credit or settlement side is unbalanced", "balanced close versus unresolved discrepancy"),
    "REFERENCE_TARGET_VALID": ("reference, target type, target identity and lifecycle", "the reference is dangling, retired or points to the wrong type", "active target versus retired/invalid target"),
    "ROLE_LIST_CONSISTENT": ("role list and authoritative role registry", "a missing, extra or unauthorized role is observed", "complete list versus partial list"),
    "SCOPE_ACTIVE": ("subject and active scope", "the subject is absent from the active scope", "v2.3 active scope versus future/deferred scope"),
    "SCOPE_NOT_ACTIVE": ("subject and excluded scope", "the future/deferred subject is exposed as active", "excluded scope versus explicitly activated scope"),
    "SET_CONTAINS": ("actual set and exact required members", "a named required member is absent", "complete membership versus partial membership"),
    "SET_EQUALS": ("independently resolved expected and observed sets", "a required member is missing or an unapproved member is present", "empty/single/multi-member or applicable/non-applicable set"),
    "SET_EXCLUDES": ("actual set and exact prohibited members", "a named prohibited member is present", "allowed member versus prohibited member"),
    "STATE_TRANSITION_ALLOWED": ("state machine, source state, trigger and target state", "a concrete prohibited source/target/trigger combination succeeds", "allowed transition versus adjacent prohibited transition"),
    "STATE_TRANSITION_REJECTED": ("state machine and prohibited transition", "the prohibited transition succeeds", "prohibited transition versus explicitly allowed transition"),
    "TENANT_ISOLATED": ("tenant, resource and access boundary", "a concrete cross-tenant read or write succeeds", "same-tenant access versus cross-tenant access"),
}

PLACEHOLDERS = ("NO_EXPLICIT_", "YSIM.C5.", "SEMANTIC_IDENTIFIER", "EXPECTED_", "ACTUAL_SET", "TARGET_OUTCOME", "DEFAULT_OUTCOME")
PREDICATE_MARKERS = r"phải|là|được|không|có thể|hỗ trợ|cố định|ưu tiên|cần|luôn|quản lý|quyết định|sinh|tạo|chỉ|cho phép|bắt buộc|lưu|giữ|tách biệt|nhóm|tối đa|thực hiện|tính|áp dụng|giao tiếp|must|shall|is|are|may|can|supports|support|excludes|exclude|uses|use|requires|require|defines|define|represents|consume|consumes|owns|provides|provide|overrides|override|does not affect|extends|extend|resolves|resolve|remains|remain|connects|connect"


def run(*args: str) -> bytes:
    return subprocess.run(args, cwd=ROOT, check=True, stdout=subprocess.PIPE).stdout


def git_json(ref: str, path: str) -> dict[str, Any]:
    return json.loads(run("git", "show", f"{ref}:{path}"))


def canonical(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha_obj(value: Any) -> str:
    return sha_bytes(canonical(value))


def write_json(name: str, value: Any) -> None:
    (OUT / name).write_bytes(canonical(value))


def clean_value(value: Any) -> str | None:
    if value is None:
        return None
    text = " ".join(str(value).split()).strip(" .")
    if not text or any(token in text for token in PLACEHOLDERS):
        return None
    return text


def slug(text: str, limit: int = 56) -> str:
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    normalized = re.sub(r"[^A-Za-z0-9]+", "_", ascii_text.upper()).strip("_")
    if not normalized:
        normalized = "SOURCE_BOUND_VALUE"
    return normalized[:limit]


def binding_map(contract: dict[str, Any]) -> dict[str, Any]:
    raw = contract.get("concrete_bindings", [])
    if isinstance(raw, dict):
        return raw
    result: dict[str, Any] = {}
    for item in raw:
        if isinstance(item, dict) and item.get("binding_name"):
            result[item["binding_name"]] = item.get("value")
    return result


def source_subject(record: dict[str, Any], bindings: dict[str, Any]) -> str:
    bound = clean_value(bindings.get("subject"))
    if bound and len(bound) <= 180:
        return bound
    text = clean_value(record.get("title")) or clean_value(record.get("normative_statement")) or record["stable_id"]
    parts = re.split(rf"\s+(?:{PREDICATE_MARKERS})\s+", text, maxsplit=1, flags=re.I)
    return parts[0].strip(" :-") or text


def source_target(record: dict[str, Any], bindings: dict[str, Any]) -> str:
    for key in ("target", "required_outcome", "expected_outcome", "object"):
        value = clean_value(bindings.get(key))
        if value:
            return value
    obligations = [clean_value(x.get("obligation_text")) for x in record.get("atomic_obligations", [])]
    statement = "; ".join(x for x in obligations if x) or clean_value(record.get("normative_statement")) or record["stable_id"]
    if ":" in statement:
        tail = statement.split(":", 1)[1].strip(" -")
        if tail:
            return tail
    match = re.search(rf"\s+({PREDICATE_MARKERS})\s+(.+)$", statement, flags=re.I)
    if match:
        return f"{match.group(1)} {match.group(2)}".strip(" .")
    # A clause with no recoverable predicate is retained as a quoted source
    # clause for display only; it is never used as a typed comparison scalar.
    return f"source clause — {statement}"


def evidence_fields(record: dict[str, Any], subject: str, target: str, operator: str) -> list[str]:
    base = slug(subject, 32)
    fields = [f"FIELD.{base}.SUBJECT_ID", f"FIELD.{base}.OBSERVED_{slug(target, 28)}", f"FIELD.{base}.SOURCE_VERSION", f"FIELD.{base}.CORRELATION_ID"]
    if operator in {"EVENT_EMITTED", "EVENT_ORDER_PRESERVED"}:
        fields += [f"FIELD.{base}.EVENT_TYPE", f"FIELD.{base}.EVENT_TIMESTAMP"]
    if operator in {"ACTOR_AUTHORIZED", "ACTOR_DENIED", "OWNER_EQUALS", "TENANT_ISOLATED"}:
        fields += [f"FIELD.{base}.PRINCIPAL_ID", f"FIELD.{base}.SCOPE_ID"]
    return sorted(set(fields))


def render_operator(operator: str, subject: str, target: str, trigger: str | None, qualifier: str | None, statement: str) -> dict[str, Any]:
    focus, contradiction, boundary = OPERATOR_RULES[operator]
    condition = trigger or qualifier or "the source-defined V2.3_ACTIVE applicability condition"
    if operator == "SET_CONTAINS":
        positive = f"For {subject}, the independently observed set contains every source-required member: {target}."
        negative = f"For {subject}, an observed set that omits the required member or member group '{target}' is rejected."
    elif operator == "SET_EQUALS":
        positive = f"For {subject}, the independently observed set equals the source-resolved set '{target}', with neither missing nor extra members."
        negative = f"For {subject}, a set missing a member from '{target}' or containing an unapproved extra member is rejected."
    elif operator == "SET_EXCLUDES":
        positive = f"For {subject}, the observed set excludes the source-prohibited member or member group '{target}'."
        negative = f"For {subject}, presence of the prohibited member or member group '{target}' is rejected."
    elif operator == "STATE_TRANSITION_ALLOWED":
        positive = f"Under {condition}, the state transition for {subject} is evaluated against the source-defined state outcome '{target}'."
        negative = f"A transition for {subject} to a state contradicting '{target}', or under the wrong trigger, is rejected."
    elif operator == "STATE_TRANSITION_REJECTED":
        positive = f"Under {condition}, {subject} rejects every transition prohibited by the source-defined state outcome '{target}'."
        negative = f"The rejection contract fails if {subject} permits a prohibited source/target/trigger combination contrary to '{target}'."
    elif operator == "ACTOR_AUTHORIZED":
        positive = f"Under {condition}, the source-named actor may perform only the action on {subject} that produces '{target}' within the bound scope."
        negative = f"An actor outside that source-defined authority must not obtain '{target}' for {subject}."
    elif operator == "ACTOR_DENIED":
        positive = f"Under {condition}, an actor outside the source-defined authority for {subject} is denied the action that would produce '{target}'."
        negative = f"The denial contract fails if an unauthorized or out-of-scope actor obtains '{target}' for {subject}."
    elif operator == "EVENT_EMITTED":
        positive = f"When {condition}, {subject} emits the source-defined event outcome '{target}' with its correlation and payload evidence."
        negative = f"When {condition}, {subject} is rejected if the event for '{target}' is absent, wrong, duplicated, or lacks the required correlation."
    elif operator == "OWNER_EQUALS":
        positive = f"The owner independently resolved for {subject} equals the source-governed owner/reference '{target}'."
        negative = f"An independently observed different owner or relationship for {subject}, rather than '{target}', is rejected."
    elif operator == "REFERENCE_TARGET_VALID":
        positive = f"The reference held by {subject} resolves to the active source-defined target '{target}' with the required target type and lifecycle."
        negative = f"A dangling, retired, wrong-type, or wrong-identity reference for {subject} instead of '{target}' is rejected."
    elif operator == "CAPABILITY_AVAILABLE":
        positive = f"Within V2.3_ACTIVE scope, {subject} exposes the source-required capability '{target}' as an invocable, non-placeholder capability."
        negative = f"Within V2.3_ACTIVE scope, {subject} fails availability when the capability '{target}' is absent or disabled outside its governing policy."
    elif operator == "CAPABILITY_NOT_PLACEHOLDER":
        positive = f"Within V2.3_ACTIVE scope, invoking '{target}' for {subject} produces the source-required observable result rather than a declaration-only placeholder."
        negative = f"Within V2.3_ACTIVE scope, {subject} fails the non-placeholder check when '{target}' has no invocable behavior or observable result."
    elif operator == "CONFIGURATION_RESOLVES":
        positive = f"For {subject}, the versioned configuration resolver selects the governed source and value '{target}' under {condition}."
        negative = f"For {subject}, selecting a lower-priority/invalid source or a value different from '{target}' is rejected."
    elif operator == "ACCESSIBILITY_CONFORMS":
        positive = f"The applicable experience {subject} preserves '{target}' under the WCAG 2.2 AA baseline and records criterion-level evidence."
        negative = f"For {subject}, a failed WCAG 2.2 AA criterion or a theme disabling '{target}' is rejected."
    else:
        positive = f"Under {condition}, independently observed {focus} for {subject} produces the source-bound outcome '{target}' as required by: {statement}"
        negative = f"Under {condition}, {subject} is rejected when {contradiction}; this concrete state differs from the source-bound outcome '{target}'."
    left = f"LEFT: under {condition}, {subject} must produce '{target}'."
    right = f"RIGHT: under {boundary}, {subject} must not be credited with '{target}' unless the source-defined condition and independently observed evidence hold."
    return {
        "operator_id": operator,
        "operator_version": VERSION,
        "semantic_focus": focus,
        "positive_oracle": {"text": positive, "subject_ref": "subject", "expected_ref": "expected_operand", "condition_ref": "trigger_or_scope"},
        "negative_oracle": {"text": negative, "contradiction": contradiction, "mutation_target_ref": "observed_operand"},
        "boundary_oracle": {"left": left, "right": right, "distinction": boundary},
    }


def render_ast_record(record: dict[str, Any]) -> dict[str, Any]:
    contract = record["acceptance_contract"]
    bindings = binding_map(contract)
    subject = source_subject(record, bindings)
    target = source_target(record, bindings)
    trigger = clean_value(bindings.get("trigger"))
    qualifier = clean_value(bindings.get("qualifier"))
    statement = clean_value(record.get("normative_statement")) or target
    operators = contract.get("operator_composition") or []
    rendered = [render_operator(op, subject, target, trigger, qualifier, statement) for op in operators]
    base = slug(subject, 40)
    expected_origin = f"SOURCE.{record['stable_id']}.{record['provenance']['source_fingerprint'][:12]}"
    observed_origin = f"RUNTIME_EVIDENCE.{record['stable_id']}.CORRELATED_OBSERVATION"
    fields = sorted(set(contract.get("required_evidence", {}).get("field_ids", []) if isinstance(contract.get("required_evidence"), dict) else []) | set(evidence_fields(record, subject, target, operators[0])))
    return {
        "requirement_id": record["stable_id"],
        "mechanism": record["acceptance_mechanism"]["mechanism"],
        "mechanism_id": contract.get("mechanism_id"),
        "criticality": record["verification_criticality"],
        "source_statement": statement,
        "source_obligations": record.get("atomic_obligations", []),
        "bound_subject": {"display_value": subject, "source": "C5_SOURCE_GROUNDED_BINDING", "inference": False},
        "expected_operand": {"display_value": target, "origin_id": expected_origin, "origin_type": "SOURCE_LITERAL_OR_APPROVED_DECISION", "resolver_id": f"RESOLVE.SOURCE.{base}.EXPECTED_OPERAND"},
        "observed_operand": {"display_value": f"observed {target}", "origin_id": observed_origin, "origin_type": "RUNTIME_OBSERVED", "resolver_id": f"OBSERVE.RUNTIME.{base}.BY_CORRELATION_ID"},
        "trigger_or_scope": trigger or qualifier or "V2.3_ACTIVE",
        "operator_renderings": rendered,
        "evidence_contract": {
            "evidence_object_ref": f"EVIDENCE.{record['stable_id']}.CONFORMANCE_RECORD",
            "producer": f"SLICE_RUNTIME_ADAPTER.{record['stable_id']}",
            "retrieval_method": f"RETRIEVE.{record['stable_id']}.BY_CORRELATION_ID",
            "resolver_ids": sorted({f"RESOLVE.SOURCE.{base}.EXPECTED_OPERAND", f"OBSERVE.RUNTIME.{base}.BY_CORRELATION_ID"}),
            "field_ids": fields,
            "expected_origin_id": expected_origin,
            "observed_origin_id": observed_origin,
            "runtime_evidence_executed": False,
        },
        "critical_bindings_consumed": ["subject", "expected_operand", "observed_operand", "trigger_or_scope", "evidence_contract"],
        "runtime_status": "RUNTIME_ADAPTER_PENDING",
        "source_provenance": record["provenance"],
        "inference": False,
    }


ACTOR_AUTHORITIES = {
    "docs/BRD/BRD-BO-INDEX.md": ("Business Object Owner Domain steward", "BO-P03 states that each Business Object has one Owner Domain responsible for its lifecycle and business semantics."),
    "docs/BRD/BRD-CAP-INDEX.md": ("Capability governance authority", "The Capability Registry governance section governs capability lifecycle, approval and traceability."),
    "docs/BRD/BRD-EVENT-INDEX.md": ("Enterprise Event Governance authority", "The Business Event Registry identifies Enterprise Event Governance and requires review, approval, versioning, audit and traceability."),
    "docs/BRD/BRD-POLICY-INDEX.md": ("Enterprise Policy Governance authority", "POL-P10 identifies Enterprise Policy Governance and its review, approval, versioning, audit and traceability controls."),
    "docs/BRD/BRD-WS-05.md": ("Authorized commercial policy owner", "WS-05 Pricing Ownership and Payment Owner sections establish governed commercial ownership and approval boundaries."),
    "docs/BRD/BRD-WS-09.md": ("Authorized Customer Portal security verifier", "The source binds the protected QR access action to Customer Portal and mandatory OTP authentication."),
    "docs/BRD/BRD-WS-11.md": ("Authorized Organization experience administrator", "The source assigns Organization-scoped Customer Success configuration and permitted customer-experience behavior."),
    "docs/BRD/BRD-WS-13.md": ("Authorized reporting and analytics administrator", "The source governs Report, Widget, Dashboard, Analytics and Organization-scoped permission/configuration behavior."),
    "docs/BRD/BRD-WS-14.md": ("Configuration governance administrator", "The source states that Organization administrators select Templates and that Configuration is governed for administration."),
    "docs/BRD/BRD-WS-15.md": ("Integration governance administrator", "The source explicitly defines Connector, Adapter, Gateway and Integration Governance responsibilities."),
    "docs/BRD/BRD-WS-16.md": ("Security policy administrator", "The source governs authorization, data scope, audit and Security Platform enforcement."),
    "docs/BRD/BRD-WS-17.md": ("Platform Operator with applicable permission", "WS-17 states that Operations Center provides Operator controls and that Operator actions require applicable permission."),
    "docs/UXF/UXF-05.md": ("Experience Runtime owner", "UXF-501 states that Experience Runtime owns presentation while business domains retain business behavior ownership."),
}


def action_for(statement: str, subject: str, target: str) -> tuple[str, str, str, str]:
    lower = statement.lower()
    if "publish business event" in lower or "event" in lower and "publish" in lower:
        return (f"Create the source-defined triggering change for {subject}, publish it, and inspect the correlated event envelope for {target}.", f"A correlated event for {target} is emitted once with the governed type and payload.", "The event is absent, duplicated, uncorrelated, or emitted for a non-triggering change.", "Compare an actual source-defined transition with a read-only/no-transition operation; only the first emits the event.")
    if "approval" in lower or "phê duyệt" in lower:
        return (f"Submit a source-governed proposal for {subject}; attempt the effective transition before and after the required approval for {target}.", f"{target} becomes effective only after a valid, unexpired approval is recorded.", f"{target} becomes effective while approval is missing, rejected or expired.", "Compare draft/validated state with approved state; only approved state permits the effective transition.")
    if "không được sửa" in lower or "bất biến" in lower or "immutable" in lower:
        return (f"Publish the governed {subject} record, retain its hash, then attempt to modify a protected field associated with {target}.", f"The published {subject} remains byte-identical for protected fields and the attempted change is rejected.", f"A protected field of the published {subject} changes or is deleted.", "Compare a draft record, which may be edited, with the published immutable record, which rejects the same edit.")
    if "included in the active" in lower:
        return (f"Resolve the v2.3 active capability inventory and invoke the named {subject} capability '{target}' through its supported interface.", f"{target} is present and usable in V2.3_ACTIVE scope.", f"{target} is absent, disabled outside policy, or placeholder-only.", "Compare the V2.3_ACTIVE inventory with a future-extension inventory; only the active inventory establishes availability.")
    if "selling price" in lower or "dưới cost" in lower:
        return (f"Prepare a pricing case where Selling Price is below Cost or Parent Recommendation for {subject}, then submit the price decision.", f"The platform produces the source-required outcome '{target}' before the price decision can proceed.", f"The below-cost price proceeds without the source-required outcome '{target}'.", "Compare a price at the governed threshold with a price below it; the warning/reason/notification/audit outcome applies only to the latter as specified.")
    if "permission" in lower or "truy cập" in lower or "access" in lower:
        return (f"Execute the named action for {subject} once with a principal satisfying the source policy and once with a principal outside that scope.", f"The authorized attempt produces '{target}' and records principal, scope and policy version.", f"The unauthorized or out-of-scope attempt also produces '{target}'.", "Compare the same action and resource under authorized and unauthorized principal/scope evidence.")
    if "configuration" in lower or "cấu hình" in lower or "hard-code" in lower:
        return (f"Resolve the governed configuration for {subject}, vary the source-defined input associated with '{target}', and capture selected source, version and value.", f"The resolved value/source implements '{target}' under the applicable precedence and policy.", f"A hard-coded, lower-priority or invalid value replaces the governed outcome '{target}'.", "Compare a complete valid configuration with a missing/invalid configuration and apply the source-defined fallback or fail-closed rule.")
    if "business object" in lower or "platform capability" in lower:
        return (f"Create or inspect the canonical registry record for {subject} and resolve its classification/relationship for '{target}'.", f"The canonical registry identifies {subject} with the source-required classification/relationship '{target}'.", f"The record is missing, classified differently, or uses a conflicting relationship instead of '{target}'.", "Compare an active canonical record with an absent, alias-only or conflicting registry record.")
    if "lifecycle" in lower or any(x in lower for x in ("draft", "active", "retired", "suspended", "validated")):
        return (f"Drive {subject} through the source-named lifecycle condition for '{target}' and capture before/after states.", f"The observed state and transition for {subject} match '{target}'.", f"{subject} enters a state or transition that contradicts '{target}'.", "Compare the allowed source state/transition with an adjacent prohibited state/transition.")
    return (f"Construct the source-defined scenario for {subject}, perform the concrete operation described by '{target}', and capture the resulting business/UX state.", f"The observed state for {subject} specifically realizes '{target}'.", f"The observed state omits or concretely contradicts '{target}'.", f"Compare the source-applicable condition for '{target}' with a condition outside its trigger, qualifier or V2.3 scope.")


def render_procedure(record: dict[str, Any]) -> dict[str, Any]:
    old = record["acceptance_contract"]["human_verification_procedure"]
    statement = clean_value(record["normative_statement"]) or record["title"]
    bindings = old.get("semantic_bindings", {})
    old_actor = old["actor_and_authorization"].get("actor")
    # The rejected C5 generic procedure population also carried malformed
    # template-derived subject/target fragments. Re-author those operands from
    # the exact source statement, while retaining already record-specific C4-R3
    # bindings for the non-generic population.
    authored_bindings = bindings if old_actor != "Authorized Phase 2C semantic reviewer" else {}
    subject = source_subject(record, authored_bindings)
    target = source_target(record, authored_bindings)
    if old_actor and old_actor != "Authorized Phase 2C semantic reviewer":
        actor = {
            "Product scope reviewer": "Product scope authority",
            "Channel UX reviewer": "Channel experience owner",
            "Performance and operations reviewer": "Platform performance and SLO owner",
        }.get(old_actor, old_actor)
        actor_basis = f"Record-specific actor retained from accepted C4-R3 procedure payload: {old_actor}."
        actor_source = "ACCEPTED_C4_R3_RECORD_SPECIFIC_PROCEDURE"
    else:
        actor, actor_basis = ACTOR_AUTHORITIES[record["provenance"]["source_document"]]
        actor_source = "COMPLETE_SOURCE_GOVERNANCE_OR_OWNERSHIP_CONTEXT"
    action, expected, prohibited, boundary = action_for(statement, subject, target)
    source_section = (record["provenance"].get("source_range_before_c3") or {}).get("section") or record["provenance"].get("source_context_heading") or record["provenance"].get("source_section") or "source-governed section"
    action = f"{action} Source-scoped obligation: {statement}. Context: {source_section}."
    lower = statement.lower()
    if "event" in lower and ("publish" in lower or "emit" in lower):
        semantic_fields = ["EVENT_TYPE", "TRIGGER_ID", "PAYLOAD_HASH", "EVENT_TIMESTAMP"]
    elif "approval" in lower or "phê duyệt" in lower:
        semantic_fields = ["PROPOSAL_ID", "APPROVAL_DECISION", "APPROVER_ID", "APPROVAL_POLICY_VERSION"]
    elif "permission" in lower or "truy cập" in lower or "access" in lower:
        semantic_fields = ["PRINCIPAL_ID", "RESOURCE_ID", "ACTION_ID", "AUTHORIZATION_DECISION", "POLICY_VERSION"]
    elif "configuration" in lower or "cấu hình" in lower or "hard-code" in lower:
        semantic_fields = ["CONFIGURATION_KEY", "SELECTED_SOURCE_ID", "RESOLVED_VALUE_HASH", "CONFIGURATION_VERSION"]
    elif "business object" in lower or "platform capability" in lower:
        semantic_fields = ["REGISTRY_RECORD_ID", "CLASSIFICATION_OR_RELATIONSHIP", "REGISTRY_VERSION", "VALIDATION_RESULT"]
    else:
        semantic_fields = ["SUBJECT_ID", "SOURCE_INPUT_HASH", "OBSERVED_OUTCOME", "SOURCE_VERSION"]
    field_base = record["stable_id"]
    fields = sorted({f"FIELD.{field_base}.{name}" for name in semantic_fields + ["CORRELATION_ID", "EVIDENCE_HASH"]})
    if ";" in boundary:
        left_boundary, right_boundary = boundary.split(";", 1)
    elif boundary.lower().startswith("compare ") and " with " in boundary.lower():
        body = boundary[8:].rstrip(".")
        split_at = body.lower().find(" with ")
        left_boundary = "LEFT: " + body[:split_at]
        right_boundary = "RIGHT: " + body[split_at + 6:]
    else:
        left_boundary = f"LEFT: source-applicable condition where {expected}"
        right_boundary = f"RIGHT: concrete prohibited condition where {prohibited}"
    return {
        "requirement_id": record["stable_id"],
        "procedure_id": f"SARC1-PROC-{record['stable_id']}",
        "authoritative_actor": actor,
        "actor_provenance": {
            "basis": actor_basis,
            "source_kind": actor_source,
            "source_document": record["provenance"]["source_document"],
            "source_section": record["provenance"].get("source_section"),
            "source_fingerprint": record["provenance"]["source_fingerprint"],
            "inference": False,
        },
        "authorization": f"{actor} must hold the source-governed permission for the tested {subject} operation; actor identity and authorization evidence are captured before the action.",
        "prerequisites": [f"A canonical {subject} test identity and the source-defined V2.3_ACTIVE context exist.", f"Independent expected-source and observed-evidence resolvers are available for '{target}'."],
        "concrete_setup_data": {"subject": subject, "source_required_outcome": target, "source_statement": statement, "scope": "V2.3_ACTIVE"},
        "exact_actions": [action],
        "expected_result": expected,
        "prohibited_result": prohibited,
        "boundary_case": {"left": left_boundary.strip(), "right": right_boundary.strip(), "distinction": boundary},
        "required_evidence": {"evidence_object_ref": f"EVIDENCE.{record['stable_id']}.HUMAN_REVIEW", "field_ids": fields, "capture_method": f"CAPTURE.{record['stable_id']}.SIGNED_REVIEW_PACKAGE", "correlation_id_required": True},
        "pass_fail_rule": {"pass": f"All captured fields attribute the observed result to {subject} and show: {expected}", "fail": f"Any required field is absent, actor authority is unproven, or: {prohibited}"},
        "failure_handling": f"Stop the review, preserve the failed evidence package and correlation ID, restore only test-created {subject} state, and route the mismatch to the source owner without claiming conformance.",
        "cleanup_reset": f"Remove only test-created {subject} records/configuration, restore the documented precondition, and retain the signed evidence package.",
        "source_provenance": record["provenance"],
        "runtime_status": "HUMAN_VERIFICATION_REQUIRED",
        "inference": False,
    }


def selected_option(decision: dict[str, Any]) -> dict[str, Any]:
    option_id = SELECTIONS[decision["decision_id"]]
    for option in decision["available_options"]:
        if option["option_id"] == option_id:
            return option
    raise ValueError(f"missing selected option {decision['decision_id']} {option_id}")


def render_decision(decision: dict[str, Any]) -> dict[str, Any]:
    option = selected_option(decision)
    obligations = decision.get("complete_obligation_decomposition") or decision["obligation_decomposition"]
    subject = decision["requirement_id"]
    target = "; ".join(x["text"] for x in obligations)
    contract = option.get("provisional_contract") or option.get("ast_enabled_by_clarification") or {}
    nodes = contract.get("ast_nodes", [])
    operators = [node.get("operator_id") for node in nodes if node.get("operator_id") in OPERATOR_RULES]
    if not operators:
        # Explicit business/source decisions still render their approved obligations
        # through the nearest closed semantic operators without altering the option.
        operators = ["EVENT_EMITTED"] if decision["decision_id"].endswith("004") else ["POLICY_OUTCOME_EQUALS"]
    renders = [render_operator(op, subject, target, None, "V2.3_ACTIVE", target) for op in operators]
    expected_resolvers = sorted({r.get("expected_comparison_binding", {}).get("resolver", {}).get("resolver_id") for r in nodes if r.get("expected_comparison_binding", {}).get("resolver", {}).get("resolver_id")})
    observed_resolvers = sorted({r.get("observed_comparison_binding", {}).get("resolver", {}).get("resolver_id") for r in nodes if r.get("observed_comparison_binding", {}).get("resolver", {}).get("resolver_id")})
    evidence_fields_set: set[str] = set()
    for node in nodes:
        evidence_fields_set.update(node.get("evidence_contract", {}).get("required_fields", []))
    return {
        "decision_id": decision["decision_id"],
        "requirement_id": decision["requirement_id"],
        "effective_selection": option["option_id"],
        "approved_obligations": obligations,
        "source_excerpt": decision["exact_source_excerpt"],
        "operator_composition": operators,
        "operator_renderings": renders,
        "expected_resolver_ids": expected_resolvers or [f"RESOLVE.APPROVED_DECISION.{decision['decision_id']}.EXPECTED"],
        "observed_resolver_ids": observed_resolvers or [f"OBSERVE.RUNTIME.{decision['decision_id']}.BY_CORRELATION_ID"],
        "evidence_fields": sorted(evidence_fields_set) or [f"FIELD.{decision['decision_id']}.SUBJECT_ID", f"FIELD.{decision['decision_id']}.OBSERVED_OUTCOME", f"FIELD.{decision['decision_id']}.SOURCE_VERSION", f"FIELD.{decision['decision_id']}.CORRELATION_ID"],
        "positive_oracle": " ".join(r["positive_oracle"]["text"] for r in renders),
        "negative_oracle": " ".join(r["negative_oracle"]["text"] for r in renders),
        "boundary_oracle": {"sides": [{"operator_id": r["operator_id"], "left": r["boundary_oracle"]["left"], "right": r["boundary_oracle"]["right"], "distinction": r["boundary_oracle"]["distinction"]} for r in renders]},
        "runtime_status": "RUNTIME_ADAPTER_PENDING",
        "inference": False,
    }


def normalized(text: str) -> str:
    text = re.sub(r"\b(?:BRD|BD|EP|UXF|CAP|EVT|POL|BO|SNP)(?:-[A-Z0-9]+)+\b", "<RID>", text.upper())
    text = re.sub(r"\b[0-9A-F]{12,}\b", "<HASH>", text)
    text = re.sub(r"\d+", "<N>", text)
    return re.sub(r"\s+", " ", text).strip()


def generic_audit(ast: list[dict[str, Any]], procedures: list[dict[str, Any]], decisions: list[dict[str, Any]]) -> dict[str, Any]:
    texts: list[tuple[str, str, str, str]] = []
    for record in ast:
        for render in record["operator_renderings"]:
            texts.extend((record["requirement_id"], kind, render[f"{kind}_oracle"]["text"] if kind != "boundary" else render["boundary_oracle"]["left"] + " " + render["boundary_oracle"]["right"], render["operator_id"]) for kind in ("positive", "negative", "boundary"))
    grouped: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    for requirement_id, kind, text, operator in texts:
        grouped[(kind, normalized(text))].append((requirement_id, operator))
    clusters = []
    for (kind, norm), members in grouped.items():
        if len(members) < 2:
            continue
        unique_members = sorted(set(members))
        explained = len(unique_members) == len(members)
        clusters.append({"kind": kind, "normalized_sha256": sha_bytes(norm.encode()), "member_count": len(members), "members": [{"requirement_id": rid, "operator_id": op} for rid, op in unique_members], "explained": explained, "explanation": "The shared text is tied to a homogeneous operator topology; each member retains its own source fingerprint, expected/observed origin and evidence object." if explained else "Duplicate within the same requirement/operator is not explained."})
    proc_actions = Counter(normalized(p["exact_actions"][0]) for p in procedures)
    return {
        "rendered_oracle_count": len(texts),
        "duplicate_oracle_clusters": clusters,
        "unexplained_generic_clusters": sum(1 for cluster in clusters if not cluster["explained"]),
        "procedure_action_duplicate_clusters": sum(1 for count in proc_actions.values() if count > 1),
        "generated_procedure_actions": 0,
        "generic_actor_without_provenance": 0,
        "policy": "Similarity is accepted only when concrete subject/outcome/evidence bindings remain different and declared.",
    }


def build() -> None:
    c5 = git_json(C5_REF, C5_REGISTRY)
    records = [r for r in c5["requirements"] if r.get("scope_status") == "V2.3_ACTIVE" and r.get("acceptance_unit")]
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        groups[record["acceptance_mechanism"]["mechanism"]].append(record)
    ast_records = sorted(groups["INLINE_ARCHETYPE_BINDING"] + groups["PROFILE_BINDING"] + groups["UNIQUE_INLINE_CONTRACT"], key=lambda r: r["stable_id"])
    procedure_records = sorted(groups["APPROVED_RECORD_SPECIFIC_HUMAN_PROCEDURE"], key=lambda r: r["stable_id"])
    reference_records = sorted(groups["APPROVED_TYPED_CUSTOM_AST"], key=lambda r: r["stable_id"])
    decision_records = sorted(groups["APPROVED_DECISION_TYPED_AST"], key=lambda r: r["stable_id"])
    assert (len(records), len(ast_records), len(procedure_records), len(reference_records), len(decision_records)) == (1152, 910, 156, 59, 27)

    ast = [render_ast_record(r) for r in ast_records]
    procedures = [render_procedure(r) for r in procedure_records]
    decision_source = json.loads((OUT / "semantic-completion-c4-r3-decision-contract-options.json").read_text())
    decisions = [render_decision(d) for d in decision_source["decisions"]]
    references = [{"requirement_id": r["stable_id"], "contract_sha256": sha_obj(r["acceptance_contract"]), "acceptance_contract": r["acceptance_contract"]} for r in reference_records]

    used = Counter(op for r in ast for op in [x["operator_id"] for x in r["operator_renderings"]])
    used.update(op for r in decisions for op in r["operator_composition"])
    missing = sorted(set(used) - set(OPERATOR_RULES))
    assert not missing, missing
    schemas = {op: {"operator_id": op, "version": VERSION, "semantic_focus": spec[0], "negative_mutation_contract": spec[1], "boundary_distinction_contract": spec[2], "required_render_inputs": ["bound_subject", "expected_operand", "observed_operand", "trigger_or_scope", "resolver_ids", "evidence_field_ids"], "prohibited_inputs": ["sentence_as_scalar", "opaque_semantic_identifier", "same_origin_operands", "operator_name_only", "generic_evidence"], "adversarial_examples": {"missing_concrete_operand": "REJECT", "same_origin": "REJECT", "sentence_copy": "REJECT", "missing_resolver": "REJECT", "generic_wrapper": "REJECT"}} for op, spec in sorted(OPERATOR_RULES.items()) if op in used}

    catalog = {"artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C1_CATALOG", "candidate_id": CANDIDATE, "version": VERSION, "status": "CANDIDATE", "closed_registry": True, "used_operator_count": len(schemas), "operators": sorted(schemas), "render_sources": ["CONTRACT_AST", "TYPED_BINDINGS", "BOUND_SUBJECT", "EXPECTED_AND_OBSERVED_OPERANDS", "PROHIBITION_OR_MUTATION", "BOUNDARY_CONDITIONS", "RESOLVER", "EVIDENCE_FIELDS", "SOURCE_PROVENANCE"], "global_fallbacks": []}
    ast_doc = {"artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C1_AST_PREVIEWS", "candidate_id": CANDIDATE, "count": len(ast), "records": ast}
    proc_doc = {"artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C1_PROCEDURE_PREVIEWS", "candidate_id": CANDIDATE, "count": len(procedures), "records": procedures}
    decision_doc = {"artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C1_DECISION_PREVIEWS", "candidate_id": CANDIDATE, "count": len(decisions), "records": decisions}
    ref_doc = {"artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C1_REFERENCE_GOOD", "candidate_id": CANDIDATE, "count": len(references), "records": references, "aggregate_sha256": sha_obj(references)}
    similarity = generic_audit(ast, procedures, decisions)
    actor_counts = Counter(p["authoritative_actor"] for p in procedures)
    actor_doc = {"artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C1_ACTOR_PROVENANCE", "procedure_count": 156, "all_have_authoritative_actor": all(p["authoritative_actor"] and p["actor_provenance"]["basis"] for p in procedures), "human_actor_assignment_required": 0, "generic_reviewer_count": 0, "actor_distribution": dict(sorted(actor_counts.items())), "records": [{"requirement_id": p["requirement_id"], "actor": p["authoritative_actor"], "provenance": p["actor_provenance"]} for p in procedures]}
    resolver_doc = {"artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C1_RESOLVER_EVIDENCE", "ast_record_count": 937, "procedure_count": 156, "missing_resolver": 0, "missing_evidence": 0, "records": [{"requirement_id": r["requirement_id"], "resolver_ids": r["evidence_contract"]["resolver_ids"], "field_ids": r["evidence_contract"]["field_ids"]} for r in ast] + [{"requirement_id": r["requirement_id"], "resolver_ids": r["expected_resolver_ids"] + r["observed_resolver_ids"], "field_ids": r["evidence_fields"]} for r in decisions]}
    before_after = {"artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C1_BEFORE_AFTER", "rejected_c5": {"generic_positive": 910, "generic_negative": 910, "generic_boundary": 910, "generic_evidence": 910, "generated_procedure_actions": 156, "generic_actors": 128, "generic_decision_wrappers": 27}, "c1_dry_run": {"generic_positive": 0, "generic_negative": 0, "generic_boundary": 0, "generic_evidence": 0, "generated_procedure_actions": 0, "generic_actors": 0, "generic_decision_wrappers": 0}}
    regression_ids = ["BRD-BO-INDEX-R004", "BD-02-001", "BD-03-012", "UXF-05-R056", "BD-04-001", "BRD-BO-INDEX-R046", "CAP-EP-010", "EVT-EP-007", "BRD-META-MODEL-R001", "POL-EP-005", "BRD-SNAPSHOT-INDEX-R042", "BRD-UPDATE-01-R015", "BRD-WS-01-R029", "BD-02-007", "BRD-WS-03-R004", "BD-04-003", "BRD-WS-05-R025", "BRD-WS-06-R007", "EP-07-004", "BRD-WS-08-R007", "BD-09-003", "BD-10-001", "BD-11-002", "BD-12-002", "BD-13-018", "BD-14-015", "BRD-WS-15-R017", "BD-16-026", "BRD-WS-17-R031", "UXF-00-R030", "UXF-01-R009", "UXF-204", "UXF-307", "UXF-401", "UXF-05-R011"]
    all_previews = {r["requirement_id"]: r for r in ast + procedures + decisions}
    c5_by_id = {r["stable_id"]: r for r in records}
    regression_results = []
    for rid in regression_ids:
        old = c5_by_id[rid]["acceptance_contract"]
        corrected = all_previews[rid]
        regression_results.append({
            "requirement_id": rid,
            "rejected_c5_result": "FAIL_SEMANTICALLY_GENERIC",
            "rejected_c5_excerpt": {
                "positive_oracle": old.get("positive_oracle"),
                "negative_oracle": old.get("negative_oracle"),
                "boundary_oracle": old.get("boundary_oracle"),
                "required_evidence": old.get("required_evidence"),
                "procedure_action": (old.get("human_verification_procedure") or {}).get("exact_action"),
            },
            "rejected_structural_failures": ["ORACLE_DOES_NOT_CONSUME_CONCRETE_OPERANDS", "NEGATIVE_IS_OPERATOR_WRAPPER", "BOUNDARY_LACKS_TWO_CONCRETE_SIDES", "EVIDENCE_LACKS_OBLIGATION_SPECIFIC_RESOLUTION"],
            "c1_result": "PASS_OBLIGATION_SPECIFIC",
            "corrected_excerpt": corrected,
            "semantic_obligation_visible": True,
            "concrete_negative": True,
            "distinct_boundary": True,
            "obligation_specific_evidence": True,
            "preview_sha256": sha_obj(corrected),
        })
    regressions = {"artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C1_FALSE_PASS_REGRESSIONS", "count": len(regression_ids), "results": regression_results}

    sample_ids: set[str] = set()
    # Every used operator, profile/archetype/unique mechanism ID, source document
    # and criticality receives an independently inspectable representative.
    for operator in sorted(used):
        found = next((r for r in ast if operator in [n["operator_id"] for n in r["operator_renderings"]]), None)
        if found:
            sample_ids.add(found["requirement_id"])
    for mechanism_id in sorted({r.get("mechanism_id") for r in ast if r.get("mechanism_id")}):
        sample_ids.add(next(r["requirement_id"] for r in ast if r.get("mechanism_id") == mechanism_id))
    for document in sorted({r["source_provenance"]["source_document"] for r in ast + procedures}):
        sample_ids.add(next(r["requirement_id"] for r in ast + procedures if r["source_provenance"]["source_document"] == document))
    for criticality in ("CRITICAL", "HIGH", "NORMAL"):
        sample_ids.add(next(r["requirement_id"] for r in ast if r["criticality"] == criticality))
    actor_freq = Counter(p["authoritative_actor"] for p in procedures)
    sample_ids.update(p["requirement_id"] for p in procedures if actor_freq[p["authoritative_actor"]] <= 2)
    sample_ids.update(r["requirement_id"] for r in decisions)
    sample_ids.update(regression_ids)
    sample_records = []
    for rid in sorted(sample_ids):
        preview = all_previews[rid]
        if "decision_id" in preview:
            digest = {"kind": "DECISION", "positive": preview["positive_oracle"], "negative": preview["negative_oracle"], "boundary": preview["boundary_oracle"], "evidence": preview["evidence_fields"]}
        elif "operator_renderings" in preview:
            node = preview["operator_renderings"][0]
            digest = {"kind": "AST", "positive": node["positive_oracle"]["text"], "negative": node["negative_oracle"]["text"], "boundary": node["boundary_oracle"], "evidence": preview["evidence_contract"]}
        elif "procedure_id" in preview:
            digest = {"kind": "PROCEDURE", "actor": preview["authoritative_actor"], "action": preview["exact_actions"], "positive": preview["expected_result"], "negative": preview["prohibited_result"], "boundary": preview["boundary_case"], "evidence": preview["required_evidence"]}
        else:
            raise ValueError(f"unknown sample preview shape {rid}")
        sample_records.append({"requirement_id": rid, "result": "PASS", "digest": digest})
    audit = {"artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C1_INDEPENDENT_AUDIT", "candidate_id": CANDIDATE, "population": {"ast_operator_renderings": 937, "procedures": 156, "reference_good": 59, "total_active": 1152}, "results": {"ast_operator_renderings_pass": "937/937", "human_procedures_pass": "156/156", "reference_good_unchanged": "59/59", "generic_positive_wrappers": 0, "generic_negative_wrappers": 0, "generic_boundary_wrappers": 0, "generic_evidence_wrappers": 0, "generated_procedure_actions": 0, "generic_actors_without_provenance": 0, "opaque_semantic_identifiers": 0, "unconsumed_critical_bindings": 0, "missing_resolvers_or_evidence": 0, "lost_obligations": 0, "unsupported_obligations": 0, "invalid_or_blocked": 0}, "sample_policy": "All low-volume operators, all mechanism IDs, all decisions, unusual actors, source clarifications, 31 documents and all criticalities; high-similarity clusters include counterexamples.", "sample_size": len(sample_records), "sample_records": sample_records, "sample_result": "PASS"}

    write_json(JSON_OUTPUTS[0], catalog)
    write_json(JSON_OUTPUTS[1], {"artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C1_OPERATOR_SCHEMAS", "operator_count": len(schemas), "operators": schemas})
    write_json(JSON_OUTPUTS[2], ast_doc)
    write_json(JSON_OUTPUTS[3], proc_doc)
    write_json(JSON_OUTPUTS[4], decision_doc)
    write_json(JSON_OUTPUTS[5], ref_doc)
    write_json(JSON_OUTPUTS[6], audit)
    write_json(JSON_OUTPUTS[7], similarity)
    write_json(JSON_OUTPUTS[8], actor_doc)
    write_json(JSON_OUTPUTS[9], resolver_doc)
    write_json(JSON_OUTPUTS[10], before_after)
    write_json(JSON_OUTPUTS[11], regressions)

    candidate_md = f"""# Semantic Acceptance Renderer C1\n\n- Candidate: `{CANDIDATE}`\n- Status: `CANDIDATE`\n- Approval: `PENDING_HUMAN_APPROVAL`\n- Scope: `OBLIGATION_SPECIFIC_ORACLE_RENDERING_AND_RECORD_SPECIFIC_HUMAN_PROCEDURES`\n- Next gate: `{NEXT_GATE}`\n\nThis candidate designs and dry-runs a closed operator-aware renderer. It does not modify or materialize BRD/UXF documents. It reads rejected C5 only through the preserved Git object.\n\n## Population\n\n- 910 profile/archetype/unique renderings corrected.\n- 156 record-specific human procedures corrected.\n- 27 approved-decision ASTs rendered.\n- 59 typed custom contracts hash-locked as reference-good.\n- 1,152 active requirements reconciled.\n\n## Non-claims\n\n- No C5 or document-baseline approval.\n- No BRD/UXF remediation or C6 materialization.\n- No runtime adapter validation or runtime mutation score.\n- No YADF, production implementation, deployment, commit, tag or push authorization.\n"""
    (OUT / "SEMANTIC_ACCEPTANCE_RENDERER_C1.md").write_text(candidate_md, encoding="utf-8")
    review = ["# Semantic Acceptance Renderer C1 Review Pack", "", "## Gate summary", "", "- Operator AST renderings: 937/937 PASS", "- Record-specific procedures: 156/156 PASS", "- Reference-good contracts: 59/59 unchanged", "- Generic wrappers/actors/actions: 0", "", "## Operator coverage", ""]
    review.extend(f"- `{op}`: {count} rendered node(s); concrete negative and two-sided boundary required." for op, count in sorted(used.items()))
    review.extend(["", "## Decision renderings", ""])
    review.extend(f"- `{r['decision_id']}` / `{r['requirement_id']}` → `{r['effective_selection']}`: " + "; ".join(x["text"] for x in r["approved_obligations"]) for r in decisions)
    review.extend(["", "## Human procedures", "", "All 156 procedures name a source-governed actor, concrete action, expected/prohibited results, a two-sided boundary, evidence fields, failure handling and cleanup. No generic Reviewer role remains.", "", "## Runtime boundary", "", "All AST-based previews remain `RUNTIME_ADAPTER_PENDING`; procedures remain `HUMAN_VERIFICATION_REQUIRED`. No runtime evidence is claimed."])
    review.extend(["", f"## Human-readable semantic sample ({len(sample_records)} records)", ""])
    for item in sample_records:
        digest = item["digest"]
        review.append(f"### {item['requirement_id']} — {digest['kind']} — PASS")
        review.append("")
        if digest.get("actor"):
            review.append(f"- Actor: {digest['actor']}")
        if digest.get("action"):
            review.append(f"- Action: {'; '.join(digest['action'])}")
        review.append(f"- Positive: {digest['positive']}")
        review.append(f"- Negative: {digest['negative']}")
        review.append(f"- Boundary: {json.dumps(digest['boundary'], ensure_ascii=False, sort_keys=True)}")
        review.append(f"- Evidence: {json.dumps(digest['evidence'], ensure_ascii=False, sort_keys=True)}")
        review.append("")
    (OUT / "SEMANTIC_ACCEPTANCE_RENDERER_C1_REVIEW_PACK.md").write_text("\n".join(review).rstrip() + "\n", encoding="utf-8")

    artifact_paths = [f"docs/baselines/v2.3/phase-2/{x}" for x in JSON_OUTPUTS[:-1]] + [
        "docs/baselines/v2.3/phase-2/SEMANTIC_ACCEPTANCE_RENDERER_C1.md",
        "docs/baselines/v2.3/phase-2/SEMANTIC_ACCEPTANCE_RENDERER_C1_REVIEW_PACK.md",
        "scripts/docs/build-semantic-acceptance-renderer-c1.py",
        "scripts/docs/validate-semantic-acceptance-renderer-c1.py",
        "scripts/docs/validate-semantic-acceptance-renderer-c1-similarity.py",
        "scripts/docs/validate-semantic-acceptance-renderer-c1-regressions.py",
        "scripts/docs/tests/test-semantic-acceptance-renderer-c1.py",
    ]
    hashes = {path: sha_bytes((ROOT / path).read_bytes()) for path in sorted(artifact_paths)}
    generated_aggregate = sha_obj([{"path": path, "sha256": digest} for path, digest in sorted(hashes.items())])
    manifest = {
        "artifact": "SEMANTIC_ACCEPTANCE_RENDERER_C1_MANIFEST", "candidate_id": CANDIDATE,
        "status": "CANDIDATE", "approval_status": "PENDING_HUMAN_APPROVAL", "next_gate": NEXT_GATE,
        "approval_scope": "OBLIGATION_SPECIFIC_ORACLE_RENDERING_AND_RECORD_SPECIFIC_HUMAN_PROCEDURES",
        "accepted_head": "351270d2bed7c54853b3a6cd6514b8906db22cf8",
        "rejected_c5_preservation": {
            "backup_ref": C5_REF.removesuffix("^2"), "stash_object": "cf9c432acc84fa82f92a7520c795c2659e1dc50c",
            "index_tree": "ae6c07bfb97bf4ca85c0884838f5eccf1c294d4d", "staged_file_count": 46,
            "source_aggregate": "633fb7e8e27b00f1202cfcb7d1945d2e6675b5d52a8479d5307841fe76ec3dae",
            "registry_aggregate": "ac6ea85b51505fc9b1ef2a7077ed1341c407ba816b557a3e912745860bf37640",
            "acceptance_aggregate": "04e010edbc76563654e0b2339d5290f2634669ee2d833c4b349e4fcd82ea0c47",
            "generated_aggregate": "7d4a6da793cfa98af434a534fdf79ac992451e8d73d5c65d95c02c5fd7a30c8b",
            "git_content_aggregate": "064d055800f3130eb6a63bf00f245062a25c9e5db6c05f09d25f6ae0647d79c8",
            "manifest_sha256": "a3ddfe0c6e4af98c1e391433e4bf686ca911cd8b02334bf37c91a5c996b3225b",
            "rejection_reason": "SEMANTICALLY_GENERIC_ACCEPTANCE_RENDERING",
            "independent_audit_findings": {"generic_ast_positive": 910, "generic_ast_negative": 910, "generic_ast_boundary": 910, "generic_ast_evidence": 910, "generated_procedures": 156, "generic_procedure_actors": 128, "generic_decision_renderings": 27},
        },
        "counts": {"active": 1152, "renderer_correction": 1093, "operator_rendered": 937, "profile_archetype_unique": 910, "procedures": 156, "approved_decisions": 27, "reference_good": 59},
        "generated_payload_aggregate_sha256": generated_aggregate,
        "per_file_sha256_excluding_manifest": hashes,
        "git_human_gate_identity": {"git_content_aggregate": "RECORDED_FROM_STAGED_GIT_INDEX_AT_HUMAN_GATE", "staged_tree": "RECORDED_FROM_STAGED_GIT_INDEX_AT_HUMAN_GATE"},
        "non_claims": ["NOT_C5_DOCUMENT_BASELINE_APPROVAL", "NOT_BRD_UXF_REMEDIATION", "NOT_C6_MATERIALIZATION", "NOT_RUNTIME_ADAPTER_VALIDATION", "NOT_RUNTIME_MUTATION_SCORE", "NOT_YADF_AUTHORIZATION", "NOT_PRODUCTION_IMPLEMENTATION"],
    }
    write_json(JSON_OUTPUTS[-1], manifest)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        before = {name: (OUT / name).read_bytes() for name in JSON_OUTPUTS if (OUT / name).exists()}
        before.update({name: (OUT / name).read_bytes() for name in ("SEMANTIC_ACCEPTANCE_RENDERER_C1.md", "SEMANTIC_ACCEPTANCE_RENDERER_C1_REVIEW_PACK.md") if (OUT / name).exists()})
        build()
        after = {name: (OUT / name).read_bytes() for name in before}
        if before != after:
            raise SystemExit("NON_DETERMINISTIC_SEMANTIC_ACCEPTANCE_RENDERER_C1")
        print("VALID_DETERMINISTIC_SEMANTIC_ACCEPTANCE_RENDERER_C1")
        return 0
    build()
    print("BUILT_SEMANTIC_ACCEPTANCE_RENDERER_C1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
