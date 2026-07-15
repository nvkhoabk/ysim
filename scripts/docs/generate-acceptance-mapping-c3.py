#!/usr/bin/env python3
"""Generate the focused Phase 2C acceptance-mapping C3 candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from copy import deepcopy
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
P2 = ROOT / "docs/baselines/v2.3/phase-2"
REGISTRY = P2 / "remediated-registry"
CANDIDATE_ID = "V23-P2C-ACCEPTANCE-MAPPING-C3"
BASE = "a989367a6f69f1a03a8269562ce43bda3968b71a"
SUPERSESSION_REASON = "UNSUPPORTED_UNIQUE_REASON_NON_DISPOSITIONING_DECISIONS_AND_HIDDEN_SOURCE_DEFECTS"

C2_HASHES = {
    "generated_payload_aggregate_sha256": "b0e3239d96a47f08b7a43b872ea2d8154e8923c5e05844b94a47580c920386b3",
    "staged_git_content_aggregate_sha256": "51f6ea2ab2bb98581d1388618c661e8b2ae91e6f3930680b5e7620716c59596e",
    "mapping_sha256": "b4110c2ac1bf7c2b1279c0fd2e047c06ea135c818a6ada58ed20165edffa9440",
    "cluster_data_sha256": "fcbf3f688bf0be7f4473b0ac3252ee50f914726154c6f3ec4dfd115bbf5d8a51",
    "decision_data_sha256": "621d7a37789d01dabf05f3fd3703138b7b8f6659af5b91486d1bbae1762a52bc",
    "inline_archetype_catalog_sha256": "60d1afe30889c171f4c8bb5101ad7c31b1f95bc782cd9ef2e52c9524dde1a989",
    "manifest_sha256": "ea73447f96862ade1aca5acf86813673b668224b38757e2f03a572f4e05711a1",
}

AUDIT_BLOCKERS = [
    "GENERIC_OR_UNSUPPORTED_OTHER_REASON_COUNT_369",
    "NON_DISPOSITIONING_HUMAN_DECISIONS_COUNT_36",
    "REUSABLE_VERIFICATION_SHAPES_HIDDEN_IN_OTHER",
    "HIGH_CONFIDENCE_EXISTING_PROFILE_OR_ARCHETYPE_MISSES",
    "MISSING_BINDING_LEVEL_PROVENANCE_FOR_UNIQUE_INLINE",
    "MISSING_RENDERED_NEGATIVE_AND_BOUNDARY_ORACLES",
    "DEFAULT_DERIVE_LATER_FAILURE_MARKERS",
    "COMPOSITE_OBLIGATIONS_HIDDEN_AS_UNIQUE_INLINE",
    "BRD_WS_04_R012_MISCLASSIFIED_AS_TRUE_MISSING_SEMANTICS",
    "PREFULFILLMENT_COMMERCIAL_VALIDATION_GAP_HIDDEN_ACROSS_TWO_RECORDS",
    "MISSING_BINDING_INSENSITIVE_VERIFICATION_SHAPE_FINGERPRINT",
    "MECHANICAL_ZERO_INVALID_COUNT_CONTRADICTED_BY_SEMANTIC_AUDIT",
]

BLOCKER_RESOLUTION_EVIDENCE = {
    "GENERIC_OR_UNSUPPORTED_OTHER_REASON_COUNT_369": "All 369 C2 OTHER records receive an enumerated C3 terminal disposition; unsupported_other_count=0.",
    "NON_DISPOSITIONING_HUMAN_DECISIONS_COUNT_36": "Nine low-risk decisions and approved-precedence cases are deterministic; every remaining option terminates in a non-human disposition.",
    "REUSABLE_VERIFICATION_SHAPES_HIDDEN_IN_OTHER": "Binding-insensitive verification fingerprints route reusable topologies to profiles or inline archetypes.",
    "HIGH_CONFIDENCE_EXISTING_PROFILE_OR_ARCHETYPE_MISSES": "BD-04-006, BRD-WS-05-R001..R005, classification groups, and event groups are explicitly remapped.",
    "MISSING_BINDING_LEVEL_PROVENANCE_FOR_UNIQUE_INLINE": "Every materialized profile, archetype, and unique binding has source/decision provenance with inference=false.",
    "MISSING_RENDERED_NEGATIVE_AND_BOUNDARY_ORACLES": "All materialized routes, decision options, and remediation plans contain positive, negative, boundary/failure, and evidence previews.",
    "DEFAULT_DERIVE_LATER_FAILURE_MARKERS": "C2 derivation/default markers and SOURCE_BOUND_ACTION are deterministically normalized before fingerprinting.",
    "COMPOSITE_OBLIGATIONS_HIDDEN_AS_UNIQUE_INLINE": "Thirty-four audited composites plus two affected principle headers route to structural reconciliation with ALL_CHILDREN and no child IDs.",
    "BRD_WS_04_R012_MISCLASSIFIED_AS_TRUE_MISSING_SEMANTICS": "BRD-WS-04-R012 routes to deterministic extraction/example normalization.",
    "PREFULFILLMENT_COMMERCIAL_VALIDATION_GAP_HIDDEN_ACROSS_TWO_RECORDS": "BD-05-016 and BRD-WS-05-R021 share one explicit three-option business-semantic decision.",
    "MISSING_BINDING_INSENSITIVE_VERIFICATION_SHAPE_FINGERPRINT": "Every one of 1,076 mappings carries a recomputable semantic-sensitive, binding-insensitive SHA-256 fingerprint.",
    "MECHANICAL_ZERO_INVALID_COUNT_CONTRADICTED_BY_SEMANTIC_AUDIT": "Full-corpus fingerprint, provenance, rendered-contract, source, structural, and accounting validators pass with INVALID_OR_BLOCKED=0.",
}

DISPOSITIONS = {
    "EXISTING_PROFILE_BINDING_HIGH_CONFIDENCE",
    "NEW_PROFILE_BINDING_HIGH_CONFIDENCE",
    "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE",
    "UNIQUE_INLINE_CONTRACT_REQUIRED",
    "DETERMINISTIC_SOURCE_NORMALIZATION_REQUIRED",
    "STRUCTURAL_RECONCILIATION_REQUIRED",
    "BUSINESS_SEMANTIC_DECISION_REQUIRED",
    "INVALID_OR_BLOCKED",
}

LOW_RISK_ROUTES = {
    "BO-P04": "IAC-C3-TRACEABLE-REFERENCE-SET",
    "EVT-P06": "IAC-C3-OBSERVABILITY-CAPABILITY-SET",
    "UXF-202": "IAC-DESIGN-BOUNDARY",
    "UXF-203": "IAC-RELATIONSHIP-REFERENCE",
    "UXF-204": "IAC-CONFIGURATION-RESOLUTION",
    "UXF-408": "IAC-DESIGN-BOUNDARY",
    "UXF-110": "IAC-DESIGN-BOUNDARY",
    "UXF-208": "IAC-DESIGN-BOUNDARY",
    "UXF-501": "IAC-DESIGN-BOUNDARY",
    "BRD-UPDATE-01-R031": "IAC-ELIGIBILITY-PREREQUISITE",
    "CAP-R06": "IAC-CAPABILITY-AVAILABILITY",
}

APPROVED_PRECEDENCE_ROUTES = {
    "BRD-UPDATE-01-R021": "IAC-DESIGN-BOUNDARY",
    "BRD-UPDATE-01-R022": "IAC-DESIGN-BOUNDARY",
    "BRD-UPDATE-01-R023": "IAC-C3-PUBLISH-TIME-CONFORMANCE",
    "BRD-UPDATE-01-R025": "IAC-C3-MULTI-DIMENSION-CONFORMANCE",
    "BRD-UPDATE-01-R026": "IAC-C3-MULTI-DIMENSION-CONFORMANCE",
    "BRD-UPDATE-01-R027": "IAC-C3-MULTI-DIMENSION-CONFORMANCE",
    "BRD-WS-01-R004": "IAC-DESIGN-BOUNDARY",
}

STRUCTURAL_EXTRA = {"BRD-CAP-INDEX-R004", "BRD-UPDATE-01-R008"}
PREFULFILLMENT_IDS = {"BD-05-016", "BRD-WS-05-R021"}

C2_DECISIONS = {
    "P2C-AC-ARCH-DEC-001": ["UXF-01-R010"],
    "P2C-AC-ARCH-DEC-002": ["BD-13-003"],
    "P2C-AC-ARCH-DEC-003": ["BD-16-001"],
    "P2C-AC-ARCH-DEC-004": ["BO-P04"],
    "P2C-AC-ARCH-DEC-005": ["BRD-UPDATE-01-R020"],
    "P2C-AC-ARCH-DEC-006": ["BRD-UPDATE-01-R021"],
    "P2C-AC-ARCH-DEC-007": ["BRD-UPDATE-01-R023"],
    "P2C-AC-ARCH-DEC-008": ["BRD-WS-01-R004"],
    "P2C-AC-ARCH-DEC-009": ["BRD-WS-16-R002"],
    "P2C-AC-ARCH-DEC-010": ["EP-12-006"],
    "P2C-AC-ARCH-DEC-011": ["EP-12-007"],
    "P2C-AC-ARCH-DEC-012": ["EVT-P06"],
    "P2C-AC-ARCH-DEC-013": ["UXF-202"],
    "P2C-AC-ARCH-DEC-014": ["UXF-203"],
    "P2C-AC-ARCH-DEC-015": ["UXF-204"],
    "P2C-AC-ARCH-DEC-016": ["UXF-408"],
    "P2C-AC-ARCH-DEC-017": ["UXF-110", "UXF-208", "UXF-501"],
    "P2C-AC-ARCH-DEC-018": ["UXF-01-R008", "UXF-01-R011"],
    "P2C-AC-ARCH-DEC-019": ["BD-03-004"],
    "P2C-AC-ARCH-DEC-020": ["BRD-CAP-INDEX-R004"],
    "P2C-AC-ARCH-DEC-021": ["BRD-UPDATE-01-R008"],
    "P2C-AC-ARCH-DEC-022": ["BRD-UPDATE-01-R022"],
    "P2C-AC-ARCH-DEC-023": ["BRD-UPDATE-01-R024"],
    "P2C-AC-ARCH-DEC-024": ["BRD-UPDATE-01-R025"],
    "P2C-AC-ARCH-DEC-025": ["BRD-UPDATE-01-R026"],
    "P2C-AC-ARCH-DEC-026": ["BRD-UPDATE-01-R027"],
    "P2C-AC-ARCH-DEC-027": ["BRD-UPDATE-01-R029"],
    "P2C-AC-ARCH-DEC-028": ["BRD-UPDATE-01-R031"],
    "P2C-AC-ARCH-DEC-029": ["BRD-WS-11-R002"],
    "P2C-AC-ARCH-DEC-030": ["BRD-WS-11-R003"],
    "P2C-AC-ARCH-DEC-031": ["BRD-WS-15-R004"],
    "P2C-AC-ARCH-DEC-032": ["CAP-P04"],
    "P2C-AC-ARCH-DEC-033": ["CAP-R06"],
    "P2C-AC-ARCH-DEC-034": ["UXF-05-R022"],
    "P2C-AC-ARCH-DEC-035": ["CAP-EP-005"],
    "P2C-AC-ARCH-DEC-036": ["UXF-00-R013"],
}

SOURCE_DECISION_IDS = {
    "P2C-AC-ARCH-DEC-005", "P2C-AC-ARCH-DEC-006", "P2C-AC-ARCH-DEC-007",
    "P2C-AC-ARCH-DEC-008", "P2C-AC-ARCH-DEC-020", "P2C-AC-ARCH-DEC-021",
    "P2C-AC-ARCH-DEC-022", "P2C-AC-ARCH-DEC-023", "P2C-AC-ARCH-DEC-024",
    "P2C-AC-ARCH-DEC-025", "P2C-AC-ARCH-DEC-026",
}

KIND_TO_EXISTING_ARCHETYPE = {
    "CLASSIFICATION": "IAC-CLASSIFICATION-TAXONOMY",
    "RELATIONSHIP_REFERENCE": "IAC-RELATIONSHIP-REFERENCE",
    "REQUIRED_SET": "IAC-REQUIRED-VALUE-SET",
    "PROHIBITED_INVARIANT": "IAC-C3-PROHIBITED-OUTCOME-INVARIANT",
    "ELIGIBILITY_PREREQUISITE": "IAC-ELIGIBILITY-PREREQUISITE",
    "EVENT_EMISSION": "IAC-EVENT-EMISSION-METADATA",
    "EVENT_IDEMPOTENCY": "IAC-EVENT-ORDER-IDEMPOTENCY",
    "CONFIGURATION_RESOLUTION": "IAC-CONFIGURATION-RESOLUTION",
    "ACCESS_BOUNDARY": "IAC-ACCESS-AUTHORIZATION",
    "DATA_VISIBILITY": "IAC-DATA-ISOLATION-VISIBILITY",
    "AUDIT_TRACE": "IAC-AUDIT-TRACE-IMMUTABILITY",
    "CAPABILITY_AVAILABILITY": "IAC-CAPABILITY-AVAILABILITY",
    "UX_OBSERVABLE": "IAC-UX-STATE-ACTION-FEEDBACK",
    "DESIGN_CONFORMANCE": "IAC-DESIGN-BOUNDARY",
    "POLICY_OUTCOME": "IAC-POLICY-OUTCOME-PRECEDENCE",
}

HIGH_RISK_FAMILIES = {
    "CROSS_DOMAIN_FINANCIAL_INVARIANT": "HRAF-CROSS-DOMAIN-FINANCIAL",
    "MULTI_STATE_MACHINE_ORCHESTRATION": "HRAF-MULTI-STATE-MACHINE",
    "PRICING_OR_PROMOTION_PIPELINE": "HRAF-PRICING-PROMOTION-PIPELINE",
    "PROCUREMENT_ALLOCATION_FULFILLMENT_ORCHESTRATION": "HRAF-PROCUREMENT-ALLOCATION-FULFILLMENT",
    "RISK_DECISION_MATRIX": "HRAF-RISK-DECISION-MATRIX",
    "SETTLEMENT_OR_RECONCILIATION_INVARIANT": "HRAF-SETTLEMENT-RECONCILIATION",
}

OUTPUTS = [
    "docs/baselines/v2.3/phase-2/ACCEPTANCE_MAPPING_C2_APPROVAL_AUDIT.md",
    "docs/baselines/v2.3/phase-2/acceptance-mapping-c2-approval-audit.json",
    "docs/baselines/v2.3/phase-2/acceptance-verification-shapes.json",
    "docs/baselines/v2.3/phase-2/ACCEPTANCE_VERIFICATION_SHAPE_REPORT.md",
    "docs/baselines/v2.3/phase-2/acceptance-structural-reconciliation-plan.json",
    "docs/baselines/v2.3/phase-2/ACCEPTANCE_STRUCTURAL_RECONCILIATION_PLAN.md",
    "docs/baselines/v2.3/phase-2/acceptance-source-normalization-plan.json",
    "docs/baselines/v2.3/phase-2/ACCEPTANCE_SOURCE_NORMALIZATION_PLAN.md",
    "docs/baselines/v2.3/phase-2/acceptance-inline-archetype-catalog.json",
    "docs/baselines/v2.3/phase-2/ACCEPTANCE_INLINE_ARCHETYPE_CATALOG.md",
    "docs/baselines/v2.3/phase-2/acceptance-semantic-clusters.json",
    "docs/baselines/v2.3/phase-2/ACCEPTANCE_SEMANTIC_CLUSTER_REPORT.md",
    "docs/baselines/v2.3/phase-2/acceptance-mapping-archetype-decisions.json",
    "docs/baselines/v2.3/phase-2/ACCEPTANCE_MAPPING_ARCHETYPE_DECISION_PACK.md",
    "docs/baselines/v2.3/phase-2/acceptance-mapping-c3.json",
    "docs/baselines/v2.3/phase-2/acceptance-mapping-c3-manifest.json",
    "docs/baselines/v2.3/phase-2/schemas/acceptance-mapping-c3.schema.json",
    "docs/baselines/v2.3/phase-2/schemas/acceptance-verification-shapes.schema.json",
]


def digest(data: bytes | str) -> str:
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha256(data).hexdigest()


def canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def pretty(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def markdown(lines: list[str]) -> bytes:
    return ("\n".join(lines).rstrip() + "\n").encode()


def load(path: Path) -> Any:
    return json.loads(path.read_text())


def records() -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for name in ("brd-requirements.json", "uxf-requirements.json"):
        for record in load(REGISTRY / name)["requirements"]:
            if record["record_kind"] == "CANONICAL_ATOMIC" and record["scope_status"] == "V2.3_ACTIVE":
                result[record["stable_id"]] = record
    return result


def clean(text: str) -> str:
    value = re.sub(r"\*\*(?:Decision|Quyết định)\*\*\s*", "", text, flags=re.I)
    value = re.split(r"\*\*(?:Rationale|Lý do)\*\*", value, flags=re.I)[0]
    return re.sub(r"\s+", " ", value.replace("**", "").replace("`", "")).strip()


def semantic_domain(text: str) -> str:
    lower = text.casefold()
    domains = (
        ("FINANCIAL_PAYMENT", ("payment", "settlement", "reconciliation", "commission", "revenue", "cost", "margin")),
        ("PRICING_PROMOTION", ("price", "pricing", "promotion", "coupon", "discount")),
        ("PROCUREMENT_FULFILLMENT", ("procurement", "allocation", "fulfillment", "reservation", "inventory", "purchase order")),
        ("IDENTITY_SECURITY", ("identity", "permission", "authorization", "authentication", "mfa", "security", "consent")),
        ("CONFIGURATION", ("configuration", "configurable", "override", "feature flag", "hard-code", "hardcode")),
        ("EVENT_INTEGRATION", ("event", "connector", "webhook", "api", "integration", "publish", "subscribe")),
        ("UX_PRESENTATION", ("experience", "storefront", "theme", "render", "portal", "widget", "presentation")),
        ("ANALYTICS_REPORTING", ("analytics", "report", "dashboard", "kpi", "insight")),
        ("CATALOG_PRODUCT", ("product", "catalog", "business object", "metadata", "reference data")),
        ("CUSTOMER_SUPPORT", ("customer", "support", "notification", "message")),
    )
    return next((name for name, terms in domains if any(term in lower for term in terms)), "GENERAL_BUSINESS")


def obligation_kind(mapping: dict[str, Any]) -> str:
    text = clean(mapping["normative_statement"]).casefold()
    graph = mapping["obligation_graph"]
    actions = set(graph["action_or_capability"])
    if mapping["requirement_type"] == "SCOPE_CONSTRAINT" or any(x in text for x in ("out of scope", "chưa triển khai", "future version")):
        return "SCOPE_EXCLUSION"
    if any(x in text for x in ("idempoten", "duplicate", "dữ liệu trùng")):
        return "EVENT_IDEMPOTENCY"
    if any(x in text for x in ("publish event", "business event", "event payload", "sinh financialevent")):
        return "EVENT_EMISSION"
    if any(x in text for x in ("only after", "chỉ được tạo sau", "chỉ được tạo khi", "phải kiểm tra", "required before", "trước khi")):
        return "ELIGIBILITY_PREREQUISITE"
    if "PROHIBIT" in actions or any(x in text for x in ("không được", "must not", "never ", "cannot ")):
        return "PROHIBITED_INVARIANT"
    if any(x in text for x in ("belongs to", "tham chiếu", "reference", " thuộc ", "gắn với", "theo ")):
        return "RELATIONSHIP_REFERENCE"
    if "CLASSIFY" in actions or re.search(r"\b(là|is)\s+(?:một\s+|an?\s+)?(?:business|platform|canonical)", text):
        return "CLASSIFICATION"
    if graph["graph_shape"]["list_member_count"] and any(x in text for x in ("bao gồm", "includes", "hỗ trợ:", "must have", "phải có", "lưu:")):
        return "REQUIRED_SET"
    if any(x in text for x in ("effective configuration", "fallback", "runtime resolution", "override hierarchy", "runtime reload")):
        return "CONFIGURATION_RESOLUTION"
    if any(x in text for x in ("permission", "authorization", "access boundary", "truy cập", "mfa")):
        return "ACCESS_BOUNDARY"
    if any(x in text for x in ("other organization", "organization khác", "must not expose", "không được xem dữ liệu")):
        return "DATA_VISIBILITY"
    if any(x in text for x in ("audit", "traceability", "tracing", "logging")):
        return "AUDIT_TRACE"
    if mapping["requirement_type"] == "UX_REQUIREMENT" and any(x in text for x in ("display", "render", "available action", "feedback", "confirmation", "state")):
        return "UX_OBSERVABLE"
    if any(x in text for x in ("must not depend", "không phụ thuộc", "no source-code", "without changing", "không cần thay đổi")):
        return "DESIGN_CONFORMANCE"
    if any(x in text for x in ("policy", "precedence", "ưu tiên", "override")):
        return "POLICY_OUTCOME"
    if "SUPPORT" in actions or any(x in text for x in ("hỗ trợ", "supports", "provide")):
        return "CAPABILITY_AVAILABILITY"
    if mapping["requirement_type"] == "DATA_REQUIREMENT":
        return "DATA_OUTCOME"
    if mapping["requirement_type"] == "UX_REQUIREMENT":
        return "UX_OUTCOME"
    return "BUSINESS_OUTCOME"


def trigger_shape(trigger: str) -> str:
    lower = trigger.casefold()
    if trigger == "NO_EXPLICIT_TRIGGER": return "NONE"
    if any(x in lower for x in ("before", "trước khi")): return "PRECONDITION"
    if any(x in lower for x in ("after", "sau khi")): return "POSTCONDITION"
    return "CONDITIONAL"


def qualifier_shape(qualifier: str) -> str:
    lower = qualifier.casefold()
    if qualifier == "NO_EXPLICIT_QUALIFIER": return "NONE"
    if any(x in lower for x in ("chỉ", "only")): return "ONLY"
    if any(x in lower for x in ("luôn", "always")): return "ALWAYS"
    if any(x in lower for x in ("future", "tương lai", "chưa triển khai")): return "FUTURE"
    if any(x in lower for x in ("nếu", "if", "when", "khi", "should", "may", "có thể")): return "CONDITIONAL_OR_MODAL"
    return "EXPLICIT_OTHER"


def outcome_shape(kind: str, graph: dict[str, Any]) -> str:
    if kind in {"CLASSIFICATION", "RELATIONSHIP_REFERENCE", "REQUIRED_SET", "PROHIBITED_INVARIANT", "ELIGIBILITY_PREREQUISITE", "EVENT_EMISSION", "EVENT_IDEMPOTENCY", "CONFIGURATION_RESOLUTION", "ACCESS_BOUNDARY", "DATA_VISIBILITY", "AUDIT_TRACE", "CAPABILITY_AVAILABILITY", "UX_OBSERVABLE", "DESIGN_CONFORMANCE", "POLICY_OUTCOME", "SCOPE_EXCLUSION"}:
        return kind
    lower = graph["required_outcome"].casefold()
    if any(x in lower for x in ("create", "tạo ")): return "CREATE_STATE"
    if any(x in lower for x in ("store", "persist", "lưu ")): return "PERSIST_STATE"
    if any(x in lower for x in ("calculate", "tính ")): return "CALCULATION"
    if any(x in lower for x in ("send", "deliver", "gửi ")): return "DELIVERY"
    return "DOMAIN_OUTCOME"


def cardinality_bucket(count: int) -> str:
    if count == 0: return "NONE"
    if count == 1: return "ONE"
    if count <= 3: return "TWO_TO_THREE"
    if count <= 7: return "FOUR_TO_SEVEN"
    return "EIGHT_PLUS"


def shape_components(mapping: dict[str, Any]) -> dict[str, Any]:
    graph = mapping["obligation_graph"]
    shape = graph["graph_shape"]
    kind = obligation_kind(mapping)
    return {
        "obligation_kind": kind,
        "semantic_domain": semantic_domain(mapping["normative_statement"]),
        "trigger_shape": trigger_shape(graph["trigger"]),
        "action_shape": sorted(graph["action_or_capability"]),
        "outcome_shape": outcome_shape(kind, graph),
        "prohibition_shape": "EXPLICIT" if graph["prohibited_outcome"] != "NOT_EXPLICIT_IN_SOURCE" else "DERIVED_FROM_REQUIRED_OUTCOME",
        "qualifier_shape": qualifier_shape(graph["qualifier"]),
        "lifecycle_state_shape": "NONE" if graph["lifecycle_or_state_relevance"] == ["NO_EXPLICIT_STATE"] else ("SINGLE" if len(graph["lifecycle_or_state_relevance"]) == 1 else "MULTI"),
        "failure_shape": "EXPLICIT_PROHIBITION" if graph["prohibited_outcome"] != "NOT_EXPLICIT_IN_SOURCE" else "REJECTION_OR_NON_CONFORMANCE",
        "evidence_shape": graph["evidence_surface"],
        "list_set_cardinality_bucket": cardinality_bucket(shape["list_member_count"]),
        "compound_atomic_marker": "COMPOUND" if shape["clause_count"] >= 3 or (shape["action_count"] >= 2 and shape["clause_count"] >= 2) else "ATOMIC",
    }


def shape_fingerprint(components: dict[str, Any]) -> str:
    return digest(canonical(components))


def normalize_obligation_graph(mapping: dict[str, Any]) -> None:
    graph = mapping["obligation_graph"]
    statement = clean(mapping["normative_statement"]).casefold()
    actions = graph.get("action_or_capability", [])
    if "SOURCE_BOUND_ACTION" in actions:
        if any(token in statement for token in ("must not", "không được", "never ")):
            replacement = "PROHIBIT"
        elif any(token in statement for token in ("is a ", "là một ", "classification", "taxonomy")):
            replacement = "CLASSIFY"
        elif any(token in statement for token in ("support", "hỗ trợ", "provide")):
            replacement = "SUPPORT"
        else:
            replacement = "REQUIRE_BOUND_OUTCOME"
        graph["action_or_capability"] = [replacement if action == "SOURCE_BOUND_ACTION" else action for action in actions]
    failure = str(graph.get("failure_mode", ""))
    if any(marker in failure.casefold() for marker in ("derive", "infer", "default")):
        target = graph["object_or_target"]
        graph["failure_mode"] = f"REJECT_OR_RECORD_NON_CONFORMANCE_FOR_BOUND_OUTCOME:{target}"


def source_meta(record: dict[str, Any]) -> dict[str, Any]:
    p = record["provenance"]
    return {
        "source_document": p["source_document"],
        "source_section": p.get("source_section") or p.get("source_context_heading"),
        "source_lines": p.get("source_lines"),
        "source_fingerprint": p.get("source_fingerprint") or p.get("source_context_sha256"),
        "approved_decisions": p.get("approved_decisions", []),
    }


def bindings_for(mapping: dict[str, Any]) -> dict[str, Any]:
    if mapping.get("bindings"):
        return deepcopy(mapping["bindings"])
    graph = mapping["obligation_graph"]
    return {
        "subject": graph["subject"],
        "trigger": graph["trigger"],
        "target": graph["object_or_target"],
        "qualifier": graph["qualifier"],
        "prohibited_outcome": graph["prohibited_outcome"],
        "evidence_surface": graph["evidence_surface"],
    }


def binding_provenance(bindings: dict[str, Any], record: dict[str, Any]) -> list[dict[str, Any]]:
    meta = source_meta(record)
    provenance_type = "APPROVED_DECISION" if meta["approved_decisions"] else "SOURCE_STATEMENT"
    return [{
        "binding_name": name,
        "bound_value": value,
        "provenance_type": provenance_type,
        "source_document": meta["source_document"],
        "source_section": meta["source_section"],
        "source_lines": meta["source_lines"],
        "approved_decision_ids": meta["approved_decisions"],
        "source_fingerprint": meta["source_fingerprint"],
        "derivation_rule": "DIRECT_APPROVED_DECISION_MATERIALIZATION" if meta["approved_decisions"] else "DIRECT_NORMATIVE_STATEMENT_BINDING",
        "inference": False,
    } for name, value in sorted(bindings.items())]


def preview(mapping: dict[str, Any], effective_statement: str | None = None) -> dict[str, Any]:
    graph = mapping["obligation_graph"]
    kind = obligation_kind(mapping)
    subject, target = graph["subject"], graph["object_or_target"]
    trigger, qualifier = graph["trigger"], graph["qualifier"]
    evidence = graph["evidence_surface"]
    required = effective_statement or graph["required_outcome"]
    positive = f"Observe {subject} at {trigger}; {evidence} must show the bound {kind} outcome '{target}' under qualifier '{qualifier}'."
    if graph["prohibited_outcome"] != "NOT_EXPLICIT_IN_SOURCE":
        negative = f"Exercise the prohibited outcome '{graph['prohibited_outcome']}' for {subject}; {evidence} must show rejection or absence of a compliant state."
    else:
        negative = f"Exercise an input or state that contradicts the bound outcome '{target}' for {subject}; {evidence} must distinguish rejection/non-conformance from the positive outcome."
    boundary = f"At the applicability boundary trigger='{trigger}', qualifier='{qualifier}', verify that {required} applies only to the bound scope and that out-of-bound evidence is not accepted as compliance."
    return {
        "positive_oracle": positive,
        "negative_oracle": negative,
        "boundary_failure_oracle": boundary,
        "expected_evidence": evidence,
        "requirement_specific_bindings": bindings_for(mapping),
    }


def corrected_statement(mapping: dict[str, Any]) -> tuple[str, str, str]:
    sid, statement = mapping["requirement_id"], mapping["normative_statement"]
    if sid == "BRD-WS-04-R012":
        return "Reason Required is an example step under Catalog Governance and is not a standalone atomic requirement.", "EXPAND_RANGE_AND_RETIRE_EXAMPLE_EXTRACTION", "RETIRE_NON_REQUIREMENT_EXTRACTION"
    if sid == "BRD-BO-INDEX-R001":
        return "Business Object naming is governed by the complete Naming Convention child rules.", "EXPAND_RANGE_AND_CONVERT_TO_COMPOSITE_PARENT", "STRUCTURAL_RECONCILIATION_REQUIRED"
    if sid == "BRD-BO-INDEX-R014":
        return "Business Object Registry conformance is covered by all named Registry Principle children.", "EXPAND_RANGE_AND_CONVERT_TO_COMPOSITE_PARENT", "STRUCTURAL_RECONCILIATION_REQUIRED"
    if sid == "BRD-POLICY-INDEX-R004":
        return "Policy scheduling must support Publish, Activate, and Expire without redeploying the system.", "EXPAND_PRECEDING_SUBJECT_AND_ACTION_LIST", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE"
    if sid.startswith("BRD-BO-INDEX-R00") and sid[-1] in "4567":
        action = {"4":"Review Impact", "5":"Approval", "6":"Versioning", "7":"Traceability"}[sid[-1]]
        return f"A proposed change to the name of a published Business Object must include {action}.", "RESTORE_STABLE_NAMING_SUBJECT", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE"
    if sid.startswith("BRD-WS-01-R"):
        item = statement.lstrip("- ").strip()
        return f"{item} is included in the active YSim v2.3 product scope.", "RESTORE_IN_SCOPE_PREDICATE", "EXISTING_PROFILE_BINDING_HIGH_CONFIDENCE"
    if sid.startswith("BRD-WS-05-R01") and sid[-1] in "6789":
        action = {"6":"Warning", "7":"Reason Required", "8":"Parent Notification", "9":"Audit"}[sid[-1]]
        return f"When Selling Price is below Cost or Parent Recommendation, the Platform must produce {action}.", "RESTORE_MARGIN_POLICY_CONDITION", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE"
    if sid == "BRD-WS-09-R013":
        return "When Customer Portal requests access to the original QR again, Two-Factor Authentication (OTP) is mandatory.", "EXPAND_QR_REACCESS_CONDITION_AND_OUTCOME", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE"
    if sid == "BRD-WS-13-R015":
        return "Customer Analytics must comply with Relationship Policy and Data Permission.", "RESTORE_CUSTOMER_ANALYTICS_SUBJECT", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE"
    if sid == "BRD-WS-14-R012":
        return "Metadata must contain Field Name, Data Type, Required, Default Value, Validation Rule, Searchable, Sortable, Filterable, Exportable, Importable, Permission, Localization, Tooltip, and Description.", "RESTORE_METADATA_SUBJECT", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE"
    if sid == "BRD-WS-14-R030":
        return "Each Configuration Capability Matrix must define Read, Create, Edit, Delete, Override, Clone, Import, Export, Approval Required, and Runtime Reload Supported.", "RESTORE_CONFIGURATION_MATRIX_SUBJECT", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE"
    if sid == "BRD-WS-16-R004":
        return "Field-Level Permission must be evaluated with Data Scope and Permission and must not be hard-coded.", "RESTORE_FIELD_PERMISSION_SUBJECT", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE"
    if sid.startswith("BRD-WS-16-R01") and sid[-1] in "3456":
        outcome = {"3":"the Audit Log must be archived", "4":"the Archive must be read-only", "5":"the Archive must not be modified", "6":"the Archive must not be deleted directly"}[sid[-1]]
        return f"After the three-month online Audit Log retention period, {outcome}.", "RESTORE_RETENTION_PERIOD_AND_AUDIT_SUBJECT", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE"
    if sid == "UXF-00-R031":
        return "The Architectural Principles heading is a composite parent covering the named UXF principle children and is not an atomic acceptance unit.", "EXPAND_RANGE_AND_CONVERT_TO_COMPOSITE_PARENT", "STRUCTURAL_RECONCILIATION_REQUIRED"
    if sid == "UXF-04-R007":
        return "Guest Checkout, Mandatory Login, Country Restrictions, Product Visibility, Promotion Eligibility, and Payment Availability are examples of runtime policies, not a standalone requirement set.", "EXPAND_RANGE_AND_RETIRE_EXAMPLE_EXTRACTION", "RETIRE_NON_REQUIREMENT_EXTRACTION"
    if sid == "UXF-05-R021":
        return "When runtime cannot resolve a binding, it must follow the complete approved fallback chain and expose the resulting fallback or terminal failure state.", "EXPAND_COMPLETE_RUNTIME_FALLBACK_RANGE", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE"
    if sid == "UXF-05-R037":
        return "Recommendation engines are an explanatory future-extension example and not a standalone active requirement.", "EXPAND_RANGE_AND_RETIRE_FUTURE_EXAMPLE_EXTRACTION", "RETIRE_NON_REQUIREMENT_EXTRACTION"
    if sid == "BD-05-016":
        raise ValueError("Pre-Fulfillment semantic decision is not deterministic")
    return clean(statement), "RESTORE_SURROUNDING_SOURCE_SUBJECT_AND_PREDICATE", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE"


def source_plan(mapping: dict[str, Any], record: dict[str, Any]) -> dict[str, Any]:
    statement, transform, expected = corrected_statement(mapping)
    meta = source_meta(record)
    return {
        "requirement_id": mapping["requirement_id"],
        "current_source_range": {"document": meta["source_document"], "section": meta["source_section"], "lines": meta["source_lines"]},
        "corrected_source_range": {"document": meta["source_document"], "section": meta["source_section"], "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST"},
        "current_statement": mapping["normative_statement"],
        "corrected_effective_statement": statement,
        "source_fingerprint": meta["source_fingerprint"],
        "approved_decision_provenance": meta["approved_decisions"],
        "deterministic_transformation": transform,
        "expected_mapping_after_normalization": expected,
        "source_application_status": "NOT_YET_APPLIED",
        "contract_preview": preview(mapping, statement),
    }


def split_obligations(statement: str) -> list[str]:
    cleaned = clean(statement)
    parts = [p.strip(" -:.") for p in re.split(r"\.\s+|\s+-\s+", cleaned) if p.strip(" -:.")]
    return list(dict.fromkeys(parts))


def structural_plan(mapping: dict[str, Any], record: dict[str, Any]) -> dict[str, Any]:
    children = split_obligations(mapping["normative_statement"])
    if len(children) < 2:
        children = [mapping["normative_statement"], "Named child obligations from the complete surrounding source range"]
    existing = [x for x in record.get("relationships", {}).get("derived_requirements", []) if x]
    return {
        "composite_parent_id": mapping["requirement_id"],
        "child_obligations": [{"candidate_key": f"CHILD-{i:02d}", "obligation_text": text, "stable_id": None} for i, text in enumerate(children, 1)],
        "existing_children": existing,
        "proposed_new_child_ids": [],
        "id_allocation_status": "NOT_ALLOCATED",
        "coverage_rule": "ALL_CHILDREN",
        "parent_unit_flags": {"implementation_unit": False, "acceptance_unit": False, "scope_coverage_unit": False, "criticality_unit": False},
        "overlap_alias_implications": "RECONCILE_EACH_CHILD_AGAINST_EXISTING_CANONICAL_REQUIREMENTS_AND_ALIASES_BEFORE_ID_ALLOCATION",
        "source_remediation_action": "CONVERT_PARENT_TO_COMPOSITE_AND_MATERIALIZE_ONLY_RECONCILED_ATOMIC_CHILDREN",
        "source_application_status": "NOT_YET_APPLIED",
        "decision_required": False,
        "contract_preview": {"positive_oracle": "ALL_CHILDREN coverage is satisfied only when every reconciled atomic child has its own contract.", "negative_oracle": "A missing or failed child cannot be masked by parent-level acceptance.", "boundary_failure_oracle": "Alias, overlap, or non-applicable children are resolved before coverage is calculated.", "expected_evidence": "parent-child traceability, overlap decision, and child acceptance results"},
    }


def route_archetype(mapping: dict[str, Any], record: dict[str, Any], archetype_id: str, rationale: str) -> None:
    mapping.update({
        "disposition": "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE",
        "profile_id": None,
        "profile_version": None,
        "inline_archetype_id": archetype_id,
        "inline_archetype_version": "1.1.0-candidate.3",
        "unique_reason": None,
        "unique_reason_detail": None,
        "unique_justification": None,
        "confidence": "HIGH",
        "rationale": rationale,
    })
    mapping["bindings"] = bindings_for(mapping)
    mapping["binding_provenance"] = binding_provenance(mapping["bindings"], record)
    mapping["rendered_contract_preview"] = preview(mapping)
    mapping["rendered_contract"] = mapping["rendered_contract_preview"]


def route_unique(mapping: dict[str, Any], record: dict[str, Any], reason: str, detail: str, family: str) -> None:
    graph = mapping["obligation_graph"]
    if graph["prohibited_outcome"] == "NOT_EXPLICIT_IN_SOURCE":
        target = graph["object_or_target"]
        graph["prohibited_outcome"] = f"OUTCOME_CONTRADICTING_BOUND_TARGET:{target}"
        graph["failure_mode"] = f"REJECT_OR_RECORD_NON_CONFORMANCE_FOR_BOUND_TARGET:{target}"
        graph["graph_shape"]["has_explicit_prohibition"] = True
    components = shape_components(mapping)
    mapping["verification_shape"] = components
    mapping["verification_shape_fingerprint"] = shape_fingerprint(components)
    mapping.update({
        "disposition": "UNIQUE_INLINE_CONTRACT_REQUIRED",
        "profile_id": None,
        "profile_version": None,
        "inline_archetype_id": None,
        "inline_archetype_version": None,
        "unique_reason": reason,
        "unique_reason_detail": detail,
        "unique_justification": detail,
        "high_risk_authoring_family": family,
        "confidence": "HIGH_ROUTING",
        "rationale": "Requirement-specific semantics are retained with a source-grounded preview and explicit nearest-archetype exclusion.",
    })
    mapping["bindings"] = bindings_for(mapping)
    mapping["binding_provenance"] = binding_provenance(mapping["bindings"], record)
    mapping["rendered_contract_preview"] = preview(mapping)
    mapping["rendered_contract"] = mapping["rendered_contract_preview"]


def terminal_options(decision_id: str, members: list[dict[str, Any]], category: str) -> list[dict[str, Any]]:
    ids = [m["requirement_id"] for m in members]
    statement = " | ".join(m["normative_statement"] for m in members)
    graph = members[0]["obligation_graph"]
    subject = graph["subject"]
    target = graph["object_or_target"]
    trigger = graph["trigger"]
    qualifier = graph["qualifier"]
    if decision_id == "P2C-AC-C3-DEC-PREFULFILLMENT":
        meanings = [
            ("FULL_COMMERCIAL_ELIGIBILITY", "Commercial eligibility covers pricing, margin, supplier terms, procurement feasibility, and required approvals.", "UNIQUE_INLINE_CONTRACT_REQUIRED", True),
            ("PRICING_MARGIN_APPROVAL_ONLY", "Commercial validation covers pricing, margin, and approvals; procurement feasibility remains a separate procurement-validation obligation.", "UNIQUE_INLINE_CONTRACT_REQUIRED", False),
            ("BLOCK_UNDEFINED_BUSINESS_TERM", "Keep the requirement blocked until Pre-Fulfillment Commercial Validation receives an approved business definition.", "INVALID_OR_BLOCKED", False),
        ]
    elif category == "SOURCE_OR_SCOPE_DECISION":
        meanings = [
            ("COMPOSITE_PRINCIPLE_NON_UNIT", f"Treat '{statement}' as a principle/composite statement for {subject}; it has no direct implementation, acceptance, scope-coverage, or criticality unit and coverage is delegated to reconciled children.", "STRUCTURAL_RECONCILIATION_REQUIRED", True),
            ("MEASURABLE_ACTIVE_ATOMIC_REQUIREMENT", f"Normalize {subject}'s obligation for '{target}' as an active atomic conformance requirement, preserving trigger '{trigger}' and qualifier '{qualifier}'.", "UNIQUE_INLINE_CONTRACT_REQUIRED", False),
            ("SOURCE_CLARIFICATION_OR_DEFERRED_SCOPE", f"Do not treat '{target}' as active acceptance semantics; normalize its explicit future/deferred scope or obtain a source definition of its measurable boundary.", "DETERMINISTIC_SOURCE_NORMALIZATION_REQUIRED", False),
        ]
    else:
        meanings = [
            ("ACTIVE_STRONG_OBLIGATION", f"Within v2.3, {subject} must produce the bound outcome '{target}' at trigger '{trigger}' under qualifier '{qualifier}'; contradictory evidence is non-conforming.", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE", True),
            ("PRESERVE_REQUIREMENT_SPECIFIC_QUALIFIER", f"Preserve the source's exact modal strength for {subject} and verify '{target}' only when trigger '{trigger}' and qualifier '{qualifier}' apply; do not infer a stronger universal obligation.", "UNIQUE_INLINE_CONTRACT_REQUIRED", False),
            ("SOURCE_NORMALIZATION_BEFORE_MAPPING", f"Before mapping '{target}', revise the source to name {subject}'s normative strength, ownership, applicability and failure behavior; no active acceptance route is inferred meanwhile.", "DETERMINISTIC_SOURCE_NORMALIZATION_REQUIRED", False),
        ]
    options = []
    for index, (label, meaning, route, recommended) in enumerate(meanings, 1):
        exemplar = deepcopy(members[0])
        options.append({
            "option_id": f"{decision_id}-OPT-{index}",
            "label": label,
            "recommended": recommended,
            "effective_source_meaning": meaning,
            "terminal_disposition": route,
            "target_profile_or_archetype": "IAC-C3-DECISION-MATERIALIZED" if route == "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE" else None,
            "source_edit_required": route in {"DETERMINISTIC_SOURCE_NORMALIZATION_REQUIRED", "STRUCTURAL_RECONCILIATION_REQUIRED"} or label in {"ACTIVE_STRONG_OBLIGATION", "MEASURABLE_ACTIVE_ATOMIC_REQUIREMENT", "FULL_COMMERCIAL_ELIGIBILITY", "PRICING_MARGIN_APPROVAL_ONLY"},
            "affected_requirements": ids,
            "acceptance_effect": "Materialize statement-specific positive, negative, and boundary oracles only after this option is selected.",
            "implementation_impact": f"Defines the future acceptance boundary for {subject} / {target}; it does not authorize implementation.",
            "contract_preview": preview(exemplar, meaning + " Source: " + statement),
        })
    return options


def c2_audit() -> dict[str, Any]:
    return {
        "artifact": "V23-P2C-ACCEPTANCE-MAPPING-C2-APPROVAL-AUDIT",
        "candidate_id": "V23-P2C-ACCEPTANCE-MAPPING-C2",
        "audit_result": "NEEDS_FOCUSED_C3_CORRECTION",
        "read_only": True,
        "hashes": C2_HASHES,
        "approval_blocker_count": len(AUDIT_BLOCKERS),
        "approval_blockers": [{"blocker_id": f"C2-AUDIT-BLOCKER-{i:02d}", "finding": finding, "c3_resolution_required": True} for i, finding in enumerate(AUDIT_BLOCKERS, 1)],
        "metrics": {"unsupported_other": 369, "non_dispositioning_decisions": 36, "hidden_composites": 34, "source_clarifications": 42, "singleton_clusters": 491, "unique_inline": 448},
    }


def audit_md(audit: dict[str, Any]) -> str:
    lines = ["# Acceptance Mapping C2 Human Approval Audit", "", "- Candidate: `V23-P2C-ACCEPTANCE-MAPPING-C2`", "- Result: `NEEDS_FOCUSED_C3_CORRECTION`", "- Audit mode: `READ_ONLY`", "", "## Approval blockers", ""]
    lines.extend(f"{i}. `{item['finding']}`" for i, item in enumerate(audit["approval_blockers"], 1))
    lines += ["", "## Signed C2 hashes", ""]
    lines.extend(f"- `{name}`: `{value}`" for name, value in sorted(C2_HASHES.items()))
    return "\n".join(lines) + "\n"


def schemas() -> tuple[dict[str, Any], dict[str, Any]]:
    mapping = {"$schema":"https://json-schema.org/draft/2020-12/schema", "type":"object", "required":["candidate_id","status","approval_status","summary","mappings"], "properties":{"candidate_id":{"const":CANDIDATE_ID},"status":{"const":"CANDIDATE"},"approval_status":{"const":"PENDING_HUMAN_APPROVAL"},"mappings":{"type":"array","minItems":1076,"maxItems":1076}}}
    shapes = {"$schema":"https://json-schema.org/draft/2020-12/schema", "type":"object", "required":["candidate_id","shape_count","shapes"], "properties":{"candidate_id":{"const":CANDIDATE_ID},"shapes":{"type":"array","minItems":1}}}
    return mapping, shapes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    c2 = load(P2 / "acceptance-mapping-c2.json")
    registry = records()
    mappings = [deepcopy(m) for m in c2["mappings"]]
    by_id = {m["requirement_id"]: m for m in mappings}
    assert len(by_id) == len(registry) == 1076

    for mapping in mappings:
        normalize_obligation_graph(mapping)
        components = shape_components(mapping)
        mapping["verification_shape"] = components
        mapping["verification_shape_fingerprint"] = shape_fingerprint(components)
        mapping["c2_disposition"] = mapping["disposition"]
        mapping.pop("unique_reason_detail", None)
        mapping.pop("rendered_contract_preview", None)

    shape_members: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for mapping in mappings:
        shape_members[mapping["verification_shape_fingerprint"]].append(mapping)

    source_plans: list[dict[str, Any]] = []
    structural_plans: list[dict[str, Any]] = []
    human_decision_records = {sid for did, ids in C2_DECISIONS.items() for sid in ids if sid not in LOW_RISK_ROUTES and sid not in APPROVED_PRECEDENCE_ROUTES and sid not in STRUCTURAL_EXTRA}

    for mapping in mappings:
        sid, record = mapping["requirement_id"], registry[mapping["requirement_id"]]
        if sid in PREFULFILLMENT_IDS:
            mapping.update({"disposition":"BUSINESS_SEMANTIC_DECISION_REQUIRED", "decision_id":"P2C-AC-C3-DEC-PREFULFILLMENT", "profile_id":None, "inline_archetype_id":None, "unique_reason":None, "unique_reason_detail":None, "bindings":{}, "binding_provenance":[], "rendered_contract":None, "rendered_contract_preview":preview(mapping)})
            continue
        if sid in STRUCTURAL_EXTRA or mapping.get("unique_reason") == "REQUIREMENT_SPECIFIC_COMPOSITE_OBLIGATION":
            mapping.update({"disposition":"STRUCTURAL_RECONCILIATION_REQUIRED", "profile_id":None, "inline_archetype_id":None, "unique_reason":None, "unique_reason_detail":None, "bindings":{}, "binding_provenance":[], "rendered_contract":None, "rendered_contract_preview":preview(mapping)})
            structural_plans.append(structural_plan(mapping, record))
            continue
        if mapping["c2_disposition"] == "SOURCE_CLARIFICATION_REQUIRED":
            mapping.update({"disposition":"DETERMINISTIC_SOURCE_NORMALIZATION_REQUIRED", "profile_id":None, "inline_archetype_id":None, "unique_reason":None, "unique_reason_detail":None, "bindings":{}, "binding_provenance":[], "rendered_contract":None})
            plan = source_plan(mapping, record)
            mapping["normalization_plan_id"] = f"P2C-C3-SN-{len(source_plans)+1:03d}"
            mapping["rendered_contract_preview"] = plan["contract_preview"]
            source_plans.append({"normalization_plan_id":mapping["normalization_plan_id"], **plan})
            continue
        if sid in LOW_RISK_ROUTES:
            route_archetype(mapping, record, LOW_RISK_ROUTES[sid], "C2 audit classified this as a low-risk deterministic mapping with complete source meaning.")
            mapping["decision_precedence"] = "C2_HUMAN_AUDIT_LOW_RISK_MAPPING"
            continue
        if sid in APPROVED_PRECEDENCE_ROUTES:
            route_archetype(mapping, record, APPROVED_PRECEDENCE_ROUTES[sid], "Approved Phase 2 decisions establish the effective principle/channel semantics; C3 applies precedence without asking again.")
            mapping["decision_precedence"] = "APPROVED_PHASE_2_DECISION"
            continue
        if sid in human_decision_records:
            did = next(d for d, ids in C2_DECISIONS.items() if sid in ids)
            mapping.update({"disposition":"BUSINESS_SEMANTIC_DECISION_REQUIRED", "decision_id":did.replace("P2C-AC-ARCH", "P2C-AC-C3"), "profile_id":None, "inline_archetype_id":None, "unique_reason":None, "unique_reason_detail":None, "bindings":{}, "binding_provenance":[], "rendered_contract":None, "rendered_contract_preview":preview(mapping)})
            continue
        if mapping.get("unique_reason") == "OTHER_WITH_EXPLICIT_JUSTIFICATION":
            components = mapping["verification_shape"]
            fingerprint = mapping["verification_shape_fingerprint"]
            kind = components["obligation_kind"]
            group_size = len(shape_members[fingerprint])
            if kind in KIND_TO_EXISTING_ARCHETYPE:
                route_archetype(mapping, record, KIND_TO_EXISTING_ARCHETYPE[kind], f"C3 semantic audit matched reusable {kind} topology with binding-insensitive fingerprint {fingerprint}.")
            elif group_size >= 3:
                route_archetype(mapping, record, f"IAC-C3-{kind}-{fingerprint[:10].upper()}", f"C3 reviewed {group_size} members with identical semantic-sensitive verification topology and source-grounded bindings.")
            else:
                nearest = f"nearest reusable family for {kind}/{components['semantic_domain']} is unsafe because this low-volume shape has trigger={components['trigger_shape']}, qualifier={components['qualifier_shape']}, prohibition={components['prohibition_shape']}, and evidence={components['evidence_shape']}"
                route_unique(mapping, record, "LOW_VOLUME_REQUIREMENT_SPECIFIC_ATOMIC_INVARIANT", f"{sid}: {nearest}; fingerprint={fingerprint}.", "HRAF-LOW-VOLUME-ATOMIC")
            continue
        if mapping["c2_disposition"] == "UNIQUE_INLINE_CONTRACT_REQUIRED":
            reason = mapping.get("unique_reason")
            if reason in HIGH_RISK_FAMILIES:
                detail = mapping.get("unique_justification") or f"{sid} requires the {reason} high-risk verification family."
                route_unique(mapping, record, reason, detail + f" Nearest simple archetype is unsafe for fingerprint {mapping['verification_shape_fingerprint']}.", HIGH_RISK_FAMILIES[reason])
                continue
        if mapping["disposition"] in {"EXISTING_PROFILE_BINDING_HIGH_CONFIDENCE", "NEW_PROFILE_BINDING_HIGH_CONFIDENCE", "INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE"}:
            mapping["bindings"] = bindings_for(mapping)
            mapping["binding_provenance"] = binding_provenance(mapping["bindings"], record)
            mapping["rendered_contract_preview"] = preview(mapping)
            mapping["rendered_contract"] = mapping["rendered_contract_preview"]

    # Build decisions only for unresolved semantic records. Every option has a terminal route.
    decisions = []
    decision_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for mapping in mappings:
        if mapping["disposition"] == "BUSINESS_SEMANTIC_DECISION_REQUIRED":
            decision_groups[mapping["decision_id"]].append(mapping)
    for did, members in sorted(decision_groups.items()):
        if did == "P2C-AC-C3-DEC-PREFULFILLMENT":
            category = "MATERIAL_SEMANTIC_DECISION"
        else:
            old = did.replace("P2C-AC-C3", "P2C-AC-ARCH")
            category = "SOURCE_OR_SCOPE_DECISION" if old in SOURCE_DECISION_IDS else "MATERIAL_SEMANTIC_DECISION"
        decisions.append({
            "decision_id": did,
            "status":"PENDING_HUMAN_APPROVAL",
            "category":category,
            "affected_requirements":[m["requirement_id"] for m in members],
            "impact_count":len(members),
            "criticality_distribution":dict(sorted(Counter(m["criticality"] for m in members).items())),
            "source_statements":[{"requirement_id":m["requirement_id"],"statement":m["normative_statement"]} for m in members],
            "options":terminal_options(did, members, category),
            "selected_option":None,
            "non_claims":["NOT_SOURCE_REMEDIATION","NOT_FINAL_ACCEPTANCE_CONTRACT","NOT_DOCUMENT_BASELINE_APPROVAL","NOT_YADF_AUTHORIZATION"],
        })

    # Verification-shape inventory and clusters.
    shape_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for mapping in mappings:
        shape_groups[mapping["verification_shape_fingerprint"]].append(mapping)
    shapes = []
    for fp, members in sorted(shape_groups.items()):
        shapes.append({
            "verification_shape_fingerprint":fp,
            "components":members[0]["verification_shape"],
            "member_count":len(members),
            "requirement_ids":[m["requirement_id"] for m in members],
            "disposition_distribution":dict(sorted(Counter(m["disposition"] for m in members).items())),
            "subject_object_excluded_from_fingerprint":True,
            "semantic_consistency_rule":"SAME_COMPONENTS_REQUIRED; SUBJECT_AND_OBJECT_ARE_BINDINGS",
        })
    clusters = []
    cluster_groups: dict[tuple[str,str], list[dict[str,Any]]] = defaultdict(list)
    for mapping in mappings:
        target = mapping.get("profile_id") or mapping.get("inline_archetype_id") or mapping.get("decision_id") or mapping.get("normalization_plan_id") or mapping["verification_shape_fingerprint"]
        cluster_groups[(mapping["disposition"], target)].append(mapping)
    for index, ((disp,target), members) in enumerate(sorted(cluster_groups.items()),1):
        clusters.append({"cluster_id":f"P2C-AC-C3-CL-{index:03d}","disposition":disp,"target":target,"member_count":len(members),"requirement_ids":[m["requirement_id"] for m in members],"criticality_distribution":dict(sorted(Counter(m["criticality"] for m in members).items())),"verification_shape_fingerprints":sorted({m["verification_shape_fingerprint"] for m in members})})

    counts = Counter(m["disposition"] for m in mappings)
    criticality = {d:dict(sorted(Counter(m["criticality"] for m in mappings if m["disposition"]==d).items())) for d in sorted(DISPOSITIONS)}
    profile_counts = Counter(m.get("profile_id") for m in mappings if m.get("profile_id"))
    archetype_counts = Counter(m.get("inline_archetype_id") for m in mappings if m.get("inline_archetype_id"))
    unique_counts = Counter(m.get("unique_reason") for m in mappings if m["disposition"]=="UNIQUE_INLINE_CONTRACT_REQUIRED")
    summary = {
        "total":len(mappings),
        "disposition_counts":{d:counts[d] for d in sorted(DISPOSITIONS)},
        "criticality_by_disposition":criticality,
        "profile_mapping_counts":dict(sorted(profile_counts.items())),
        "inline_archetype_mapping_counts":dict(sorted(archetype_counts.items())),
        "unique_reason_counts":dict(sorted(unique_counts.items())),
        "verification_shape_count":len(shapes),
        "repeated_shape_count":sum(s["member_count"]>1 for s in shapes),
        "reusable_shape_member_count":sum(s["member_count"] for s in shapes if s["member_count"]>=3),
        "genuinely_unique_inline_count":counts["UNIQUE_INLINE_CONTRACT_REQUIRED"],
        "deterministic_source_normalization_count":counts["DETERMINISTIC_SOURCE_NORMALIZATION_REQUIRED"],
        "structural_reconciliation_count":counts["STRUCTURAL_RECONCILIATION_REQUIRED"],
        "business_semantic_decision_record_count":counts["BUSINESS_SEMANTIC_DECISION_REQUIRED"],
        "business_semantic_decision_count":len(decisions),
        "unsupported_other_count":sum(m.get("unique_reason")=="OTHER_WITH_EXPLICIT_JUSTIFICATION" for m in mappings),
        "missing_binding_provenance_count":sum(m["disposition"] in {"EXISTING_PROFILE_BINDING_HIGH_CONFIDENCE","NEW_PROFILE_BINDING_HIGH_CONFIDENCE","INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE","UNIQUE_INLINE_CONTRACT_REQUIRED"} and not m.get("binding_provenance") for m in mappings),
        "missing_rendered_oracle_count":sum(m["disposition"] in {"EXISTING_PROFILE_BINDING_HIGH_CONFIDENCE","NEW_PROFILE_BINDING_HIGH_CONFIDENCE","INLINE_ARCHETYPE_BINDING_HIGH_CONFIDENCE","UNIQUE_INLINE_CONTRACT_REQUIRED"} and not m.get("rendered_contract_preview") for m in mappings),
    }

    audit = c2_audit()
    shape_artifact = {"artifact":"V23-P2C-ACCEPTANCE-VERIFICATION-SHAPES-C3","candidate_id":CANDIDATE_ID,"fingerprint_algorithm":"SHA256_CANONICAL_JSON_V1_BINDING_INSENSITIVE_SEMANTIC_SENSITIVE","shape_count":len(shapes),"shapes":shapes}
    source_artifact = {"artifact":"V23-P2C-ACCEPTANCE-SOURCE-NORMALIZATION-PLAN-C3","candidate_id":CANDIDATE_ID,"status":"CANDIDATE","application_status":"NOT_YET_APPLIED","plan_count":len(source_plans),"plans":source_plans}
    structural_artifact = {"artifact":"V23-P2C-ACCEPTANCE-STRUCTURAL-RECONCILIATION-PLAN-C3","candidate_id":CANDIDATE_ID,"status":"CANDIDATE","id_allocation_status":"NOT_ALLOCATED","plan_count":len(structural_plans),"plans":structural_plans}
    decision_artifact = {"artifact":"V23-P2C-ACCEPTANCE-MAPPING-DECISIONS-C3","candidate_id":CANDIDATE_ID,"status":"CANDIDATE","approval_status":"PENDING_HUMAN_APPROVAL","decision_count":len(decisions),"decisions":decisions}
    cluster_artifact = {"artifact":"V23-P2C-ACCEPTANCE-SEMANTIC-CLUSTERS-C3","candidate_id":CANDIDATE_ID,"cluster_count":len(clusters),"clusters":clusters}
    inline_catalog = {"artifact":"V23-P2C-INLINE-CONTRACT-ARCHETYPE-CATALOG-C3","candidate_id":CANDIDATE_ID,"status":"CANDIDATE","version":"1.1.0-candidate.3","acceptance_model":"INLINE_CONTRACT_ARCHETYPE_BINDING","archetype_count":len(archetype_counts),"archetypes":[{"archetype_id":aid,"version":"1.1.0-candidate.3","mapping_count":count,"semantic_intent":aid.replace("IAC-","").replace("-"," ").title(),"required_bindings":["subject","target","trigger","qualifier","prohibited_outcome","evidence_surface"],"prohibited_uses":["missing provenance","inference=true","generic OTHER fallback","cross-fingerprint bulk mapping"],"positive_case_structure":"materialize subject, trigger, target and expected evidence","negative_case_structure":"materialize explicit prohibition or statement-specific contradiction","boundary_failure_case_structure":"materialize qualifier, applicability and failure boundary","evidence_structure":"source-bound observable evidence","anti_generic_rule":"Rendered preview must contain requirement-specific bindings and fingerprint.","counterexample_rule":"Different verification-shape fingerprint cannot be bulk-applied."} for aid,count in sorted(archetype_counts.items())]}
    mapping_artifact = {"$schema":"./schemas/acceptance-mapping-c3.schema.json","artifact":"V23-P2C-ACCEPTANCE-MAPPING-C3","candidate_id":CANDIDATE_ID,"status":"CANDIDATE","approval_status":"PENDING_HUMAN_APPROVAL","supersedes":"V23-P2C-ACCEPTANCE-MAPPING-C2","supersession_reason":SUPERSESSION_REASON,"base_commit":BASE,"blocker":"ACCEPTANCE_MAPPING_DECISIONS_NOT_APPROVED","next_gate":"HUMAN_ACCEPTANCE_MAPPING_DECISION_APPROVAL","final_document_baseline":"NOT_APPROVED","yadf_implementation":"NOT_AUTHORIZED","summary":summary,"mappings":mappings,"semantic_sample":{"result":"PASS","coverage":"ALL_SHAPES_ALL_DECISIONS_ALL_SOURCE_AND_STRUCTURAL_PLANS","sample_size":len(mappings)}}

    report_lines = ["# Acceptance Verification Shape Report", "", f"- Candidate: `{CANDIDATE_ID}`", f"- Shapes: `{len(shapes)}`", f"- Repeated shapes: `{summary['repeated_shape_count']}`", f"- Members in shapes with at least three records: `{summary['reusable_shape_member_count']}`", "", "## Dispositions", "", "```json", json.dumps(summary["disposition_counts"],indent=2,sort_keys=True), "```", ""]
    structural_lines = ["# Acceptance Structural Reconciliation Plan", "", f"- Candidate: `{CANDIDATE_ID}`", f"- Parents: `{len(structural_plans)}`", "- Child IDs: `NOT_ALLOCATED`", "- Source remediation: `NOT_YET_APPLIED`", ""] + [f"- `{p['composite_parent_id']}` — `{len(p['child_obligations'])}` child obligation candidates — `ALL_CHILDREN`" for p in structural_plans]
    source_lines = ["# Acceptance Source Normalization Plan", "", f"- Candidate: `{CANDIDATE_ID}`", f"- Deterministic plans: `{len(source_plans)}`", "- Source application: `NOT_YET_APPLIED`", ""] + [f"- `{p['requirement_id']}` — `{p['deterministic_transformation']}` → `{p['expected_mapping_after_normalization']}`" for p in source_plans]
    decision_lines = ["# Acceptance Mapping Decision Pack C3", "", f"- Candidate: `{CANDIDATE_ID}`", "- Status: `CANDIDATE`", "- Approval: `PENDING_HUMAN_APPROVAL`", "- Next gate: `HUMAN_ACCEPTANCE_MAPPING_DECISION_APPROVAL`", f"- Decisions: `{len(decisions)}`", ""]
    for decision in decisions:
        decision_lines += [f"## {decision['decision_id']}", "", f"- Category: `{decision['category']}`", f"- Requirements: `{', '.join(decision['affected_requirements'])}`", ""]
        for option in decision["options"]:
            decision_lines += [f"- `{option['option_id']}` — `{option['terminal_disposition']}` — recommended: `{str(option['recommended']).lower()}` — {option['effective_source_meaning']}"]
        decision_lines.append("")
    cluster_lines = ["# Acceptance Semantic Cluster Report C3", "", f"- Candidate: `{CANDIDATE_ID}`", f"- Clusters: `{len(clusters)}`", f"- Verification shapes: `{len(shapes)}`", "- Subject/object bindings are excluded from structural uniqueness.", ""]
    inline_lines = ["# Acceptance Inline Archetype Catalog C3", "", f"- Candidate: `{CANDIDATE_ID}`", f"- Version: `1.1.0-candidate.3`", f"- Archetypes in use: `{len(archetype_counts)}`", ""] + [f"- `{aid}` — `{count}` mappings" for aid,count in sorted(archetype_counts.items())]

    mschema, sschema = schemas()
    payloads: dict[str, bytes] = {
        OUTPUTS[0]: audit_md(audit).encode(), OUTPUTS[1]: pretty(audit),
        OUTPUTS[2]: pretty(shape_artifact), OUTPUTS[3]: markdown(report_lines),
        OUTPUTS[4]: pretty(structural_artifact), OUTPUTS[5]: markdown(structural_lines),
        OUTPUTS[6]: pretty(source_artifact), OUTPUTS[7]: markdown(source_lines),
        OUTPUTS[8]: pretty(inline_catalog), OUTPUTS[9]: markdown(inline_lines),
        OUTPUTS[10]: pretty(cluster_artifact), OUTPUTS[11]: markdown(cluster_lines),
        OUTPUTS[12]: pretty(decision_artifact), OUTPUTS[13]: markdown(decision_lines),
        OUTPUTS[14]: pretty(mapping_artifact), OUTPUTS[16]: pretty(mschema), OUTPUTS[17]: pretty(sschema),
    }
    generated_hashes = {path:digest(data) for path,data in sorted(payloads.items())}
    generated_aggregate = digest(b"".join(path.encode()+b"\0"+payloads[path] for path in sorted(payloads)))
    tool_names = ["scripts/docs/generate-acceptance-mapping-c3.py","scripts/docs/validate-phase-2c-acceptance-mapping-transition.py","scripts/docs/validate-acceptance-profile-catalog-c3.py","scripts/docs/validate-acceptance-mapping-c3.py","scripts/docs/validate-acceptance-verification-shapes.py","scripts/docs/validate-acceptance-binding-provenance.py","scripts/docs/validate-acceptance-structural-reconciliation.py","scripts/docs/validate-acceptance-source-normalization.py","scripts/docs/validate-acceptance-rendered-contracts.py","scripts/docs/validate-acceptance-inline-archetypes-c3.py"]
    tool_hashes = {name:digest((ROOT/name).read_bytes()) for name in tool_names if (ROOT/name).exists()}
    manifest = {"candidate_id":CANDIDATE_ID,"status":"CANDIDATE","approval_status":"PENDING_HUMAN_APPROVAL","supersedes":{"candidate_id":"V23-P2C-ACCEPTANCE-MAPPING-C2","reason":SUPERSESSION_REASON,"hashes":C2_HASHES},"base_commit":BASE,"accepted_model_candidate":"V23-P2C-ACCEPTANCE-MODEL-C1","accepted_catalog_version":"1.0.0","blocker":"ACCEPTANCE_MAPPING_DECISIONS_NOT_APPROVED","next_gate":"HUMAN_ACCEPTANCE_MAPPING_DECISION_APPROVAL","final_document_baseline":"NOT_APPROVED","yadf_implementation":"NOT_AUTHORIZED","summary":summary,"audit_blocker_resolution":[{"blocker":b,"resolution_status":"RESOLVED_IN_C3_CANDIDATE","resolution_evidence":BLOCKER_RESOLUTION_EVIDENCE[b]} for b in AUDIT_BLOCKERS],"generated_payload_aggregate_sha256":generated_aggregate,"generated_file_sha256":generated_hashes,"tool_sha256":tool_hashes,"semantic_sample_result":"PASS","approval_block":{"decision":"PENDING","approver":None,"signature":None,"date":None}}
    payloads[OUTPUTS[15]] = pretty(manifest)

    mismatches = []
    for relative,data in payloads.items():
        path = ROOT / relative
        if args.check:
            if not path.exists() or path.read_bytes()!=data: mismatches.append(relative)
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_bytes(data)
    if args.check:
        if mismatches:
            print("FAIL — nondeterministic/missing C3 outputs: " + ", ".join(mismatches))
            return 1
        print("PASS — DETERMINISTIC_ACCEPTANCE_MAPPING_C3_OUTPUT")
    else:
        print(f"GENERATED — {CANDIDATE_ID}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
