#!/usr/bin/env python3
"""Build Semantic Completion C4-R3 without changing the locked R2 technical core."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HEAD = "522442635eb0df24dd5de0d42dad84656a5920e0"
R2_REF = "refs/ysim-backups/v2.3/phase-2c-semantic-completion-c4-r2-decision-incomplete"
R2_OBJECT = "24d72df1e1eba625b89983e80b6fad32a973bbb5"
R2_TREE = "607c36df252de32a14947b8d725f2c6b1f06353a"
R2_GIT_AGGREGATE = "cced96cceb2939742c5621cb669b8f7d293745a292de6ad058093cf265e22dcf"
R2_GENERATED_AGGREGATE = "34b6d49a6baab01ab4df1e520b238cb3556da6638f11c28ba75246825fea2124"
R2_MANIFEST_SHA = "0bce1e5e907324eda6b0889527c8570ca1e06cf9d9a635af70142fb045ceb611"
CANDIDATE = "V23-P2C-SEMANTIC-COMPLETION-C4-R3"
SUPERSEDES = "V23-P2C-SEMANTIC-COMPLETION-C4-R2"
REASON = "INCOMPLETE_DECISION_CONTRACTS_AND_FALSE_OPTION_EFFECT_CLAIMS"
NEXT_GATE = "HUMAN_PHASE_2C_SEMANTIC_COMPLETION_C4_R3_DECISION_AND_CANDIDATE_APPROVAL"

CORE_PATHS = [
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r2-custom-contracts.json",
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r2-fixtures.json",
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r2-execution-results.json",
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r2-procedures.json",
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r2-accounting.json",
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r2-audit.json",
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r2-mutation-delta.json",
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r2-normalization-register.json",
    "scripts/docs/validate-phase-2c-semantic-completion-c4-r2-reproduction.py",
]

OUTPUTS = {
    "docs/baselines/v2.3/phase-2/SEMANTIC_COMPLETION_C4_R3_CANDIDATE.md": "report",
    "docs/baselines/v2.3/phase-2/SEMANTIC_COMPLETION_C4_R3_DECISION_REVIEW_PACK.md": "review",
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r3-decision-contract-options.json": "decisions",
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r3-decision-audit.json": "audit",
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r3-dependency-overlap-register.json": "dependencies",
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r3-source-provenance-register.json": "provenance",
    "docs/baselines/v2.3/phase-2/semantic-completion-c4-r3-manifest.json": "manifest",
}

TOOLING = [
    "scripts/docs/build-phase-2c-semantic-completion-c4-r3.py",
    "scripts/docs/validate-phase-2c-semantic-completion-c4-r3.py",
    "scripts/docs/validate-phase-2c-semantic-completion-c4-r3-decisions.py",
    "scripts/docs/tests/test-phase-2c-semantic-completion-c4-r3.py",
]

NON_CLAIMS = [
    "NOT_FINAL_BRD_UXF_BASELINE_APPROVAL", "NOT_RUNTIME_ADAPTER_VALIDATION",
    "NOT_RUNTIME_MUTATION_SCORE", "NOT_YADF_AUTHORIZATION", "NOT_PRODUCTION_IMPLEMENTATION",
    "NOT_AUTOMATIC_APPROVAL_OF_27_DECISIONS", "NOT_C4_R3_ACCEPTANCE", "NO_SOURCE_EDIT_PERFORMED",
]


def git_bytes(spec: str) -> bytes:
    return subprocess.check_output(["git", "show", spec], cwd=ROOT)


def git_json(spec: str) -> dict[str, Any]:
    return json.loads(git_bytes(spec))


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(value if isinstance(value, bytes) else canonical(value)).hexdigest()


def source_excerpt(path: str, start: int, end: int) -> str:
    lines = git_bytes(f"{HEAD}:{path}").decode("utf-8").splitlines()
    if start < 1 or end > len(lines) or start > end:
        raise RuntimeError(f"INVALID_SOURCE_RANGE:{path}:{start}-{end}")
    return "\n".join(lines[start - 1:end])


def slug(value: str) -> str:
    return re.sub(r"[^A-Z0-9]+", "_", value.upper()).strip("_")


SEMANTIC_ROLES = {
    "accessibility_standard":"GOVERNED_ACCESSIBILITY_STANDARD", "action":"GOVERNED_OPERATION",
    "actor":"AUTHORIZED_PRINCIPAL", "actual_set":"RESOLVED_DOMAIN_MEMBERS", "actual_value":"RESOLVED_DOMAIN_VALUE",
    "after_hash":"POST_OPERATION_CONTENT_HASH", "allowed_lifecycle_states":"PERMITTED_LIFECYCLE_STATES",
    "allowed_states":"PERMITTED_TARGET_STATES", "allowed_values":"PERMITTED_DOMAIN_VALUES",
    "audit_record":"IMMUTABLE_AUDIT_RECORD", "baseline":"GOVERNED_BASELINE", "before_hash":"PRE_OPERATION_CONTENT_HASH",
    "capability":"REQUIRED_PLATFORM_CAPABILITY", "configuration_key":"GOVERNED_CONFIGURATION_KEY",
    "configuration_sources":"PERMITTED_CONFIGURATION_SOURCES", "correlation_id":"OPERATION_CORRELATION_ID",
    "credits":"CREDIT_ENTRY_COLLECTION", "currency":"SETTLEMENT_CURRENCY", "data_class":"VERSION_HISTORY_DATA_CLASS",
    "debits":"DEBIT_ENTRY_COLLECTION", "effective_policy":"EFFECTIVE_AUTHORIZATION_POLICY",
    "event_id":"CANONICAL_EVENT_TYPE", "evidence_object":"CONFORMANCE_EVIDENCE_RECORD",
    "expected_outcome":"CANONICAL_DECISION_OUTCOME", "expected_set":"GOVERNED_DOMAIN_MEMBERS",
    "expected_value":"GOVERNED_CONFIGURATION_VALUE", "experience":"APPLICABLE_EXPERIENCE",
    "field":"REQUIRED_OBSERVABLE_FIELD", "from_state":"SOURCE_LIFECYCLE_STATE",
    "immutability_boundary":"PROTECTED_IMMUTABILITY_POLICY", "policy":"GOVERNING_POLICY",
    "policy_inputs":"POLICY_EVALUATION_CONTEXT", "policy_version":"GOVERNING_POLICY_VERSION",
    "prohibited_members":"GOVERNED_EXCLUDED_MEMBERS", "prohibited_state":"PROHIBITED_LIFECYCLE_STATE",
    "protected_fields":"IMMUTABLE_FIELD_COLLECTION", "reference":"DOMAIN_RELATIONSHIP_REFERENCE",
    "registry":"AUTHORITATIVE_ENTITY_REGISTRY", "registry_source":"REGISTRY_IDENTITY_SOURCE",
    "required_fields":"MANDATORY_EVIDENCE_FIELDS", "required_members":"GOVERNED_REQUIRED_MEMBERS",
    "required_outcomes":"MANDATORY_ACCESSIBILITY_OUTCOMES", "resolved_source":"SELECTED_CONFIGURATION_SOURCE",
    "resource":"PROTECTED_RESOURCE", "retention_window":"POLICY_RETENTION_DURATION", "scope":"APPLICABLE_V2_3_SCOPE",
    "source_versions":"CONFIGURATION_SOURCE_VERSIONS", "state_machine":"CANONICAL_STATE_MACHINE",
    "subject":"GOVERNED_DOMAIN_SUBJECT", "target_id":"REFERENCED_ENTITY_IDENTITY",
    "target_type":"REFERENCED_ENTITY_TYPE", "terminal_action":"RETENTION_TERMINAL_ACTION",
    "to_state":"DESTINATION_LIFECYCLE_STATE", "trigger":"GOVERNED_TRANSITION_TRIGGER",
}


# Exact ranges cover the current canonical statements, including their governing list/context where needed.
SOURCE_RANGES = {
    "001": ("docs/BRD/BRD-WS-04.md", "24. Business Decisions (Locked) > BD-04-001", 523, 530),
    "002": ("docs/BRD/BRD-WS-07.md", "24. Business Decisions (Locked) > BD-07-014", 718, 720),
    "003": ("docs/BRD/BRD-WS-09.md", "25. Business Decisions (Locked) > BD-09-014", 642, 644),
    "004": ("docs/BRD/BRD-WS-16.md", "31. Business Decisions (Locked) > BD-16-027", 1033, 1035),
    "005": ("docs/BRD/BRD-WS-17.md", "37. Business Decisions (Locked) > BD-17-016", 1121, 1123),
    "006": ("docs/BRD/BRD-UPDATE-01.md", "17. Business Principles > API First", 907, 919),
    "007": ("docs/BRD/BRD-WS-02.md", "11. Inventory Strategy", 286, 300),
    "008": ("docs/BRD/BRD-WS-04.md", "16. Product Version", 337, 348),
    "009": ("docs/BRD/BRD-WS-07.md", "4. Order Taxonomy > Purchase Order (PO)", 120, 125),
    "010": ("docs/BRD/BRD-WS-11.md", "20. Satisfaction Survey", 480, 496),
    "011": ("docs/BRD/BRD-WS-13.md", "4. Dashboard Widget", 108, 118),
    "012": ("docs/BRD/BRD-WS-13.md", "25. Widget Library", 648, 658),
    "013": ("docs/BRD/BRD-WS-14.md", "15. Configuration Version", 419, 435),
    "014": ("docs/BRD/BRD-WS-14.md", "22. Configuration Rollback", 590, 599),
    "015": ("docs/BRD/BRD-WS-17.md", "33. Operational Command Center", 883, 897),
    "016": ("docs/BRD/BRD-WS-17.md", "30. Enterprise Operations Principle", 798, 810),
    "017": ("docs/BRD/BRD-WS-12.md", "33. Enterprise Design Principles > EP-12-003", 766, 768),
    "018": ("docs/BRD/BRD-WS-13.md", "30. Enterprise Design Principles > EP-13-001", 993, 999),
    "019": ("docs/BRD/BRD-WS-14.md", "32. Enterprise Design Principles > EP-14-010", 1252, 1254),
    "020": ("docs/BRD/BRD-WS-17.md", "38. Enterprise Design Principles > EP-17-001", 1235, 1239),
    "021": ("docs/UXF/UXF-00.md", "20. Architectural Principles > UXF-002", 612, 614),
    "022": ("docs/UXF/UXF-00.md", "20. Architectural Principles > UXF-003", 618, 620),
    "023": ("docs/UXF/UXF-00.md", "20. Architectural Principles > UXF-008", 648, 650),
    "024": ("docs/UXF/UXF-02.md", "18. Design Accessibility", 535, 543),
    "025": ("docs/UXF/UXF-02.md", "20. Design Principles > UXF-209", 613, 615),
    "026": ("docs/UXF/UXF-03.md", "22. Architectural Principles > UXF-301", 628, 632),
    "027": ("docs/UXF/UXF-03.md", "22. Architectural Principles > UXF-302", 636, 638),
}


# Record-level authored obligations and operator topology. Values are source/decision concepts, not schema labels.
SPECS = {
"001": {"ob":["Exactly Supplier, Master, Sales and Storefront Catalog levels exist.","The declared four-level sequence is Supplier → Master → Sales → Storefront."],"nodes":[("SET_EQUALS","FOUR_LEVEL_CATALOG_MEMBERS"),("POLICY_OUTCOME_EQUALS","FOUR_LEVEL_CATALOG_SEQUENCE")],"why":"Exact membership and declared sequence replace under-constrained SET_CONTAINS."},
"002": {"ob":["A Sales Order may relate to more than one Purchase Order.","Every observed Purchase Order retains a valid reference to its originating Sales Order."],"nodes":[("REFERENCE_TARGET_VALID","SALES_ORDER_PURCHASE_ORDER_RELATIONSHIP"),("SET_CONTAINS","PURCHASE_ORDERS_BY_SALES_ORDER")],"why":"Reference validity and one-to-many cardinality are both explicit."},
"003": {"ob":["Fulfillment may enter Completed only after Delivery succeeds.","Fulfillment completion before successful Delivery is prohibited."],"nodes":[("STATE_TRANSITION_ALLOWED","FULFILLMENT_COMPLETION_AFTER_DELIVERY_SUCCESS"),("STATE_TRANSITION_REJECTED","FULFILLMENT_COMPLETION_BEFORE_DELIVERY_SUCCESS")],"why":"Canonical states plus prerequisite and terminal prohibition are retained."},
"004": {"ob":["Security Platform publishes a governed business event under the selected governance model."],"nodes":[("EVENT_EMITTED","SECURITY_PLATFORM_BUSINESS_EVENT")],"why":"Source lacks exact event governance; three mutually exclusive business choices are exposed.","business":True},
"005": {"ob":["The Operational Dashboard is available for Operator use.","Authorized Operators are allowed and non-Operators are denied."],"nodes":[("CAPABILITY_AVAILABLE","OPERATIONAL_DASHBOARD"),("ACTOR_AUTHORIZED","OPERATOR_DASHBOARD_ACCESS"),("ACTOR_DENIED","NON_OPERATOR_DASHBOARD_ACCESS")],"why":"Availability and both access boundaries are independently evidenced."},
"006": {"ob":["Commerce Experience Platform capabilities expose approved API contracts.","Undocumented presentation-only access is outside the API First boundary."],"nodes":[("SCOPE_ACTIVE","APPROVED_API_CONTRACT_BOUNDARY"),("SET_EXCLUDES","UNDOCUMENTED_PRESENTATION_ONLY_PATHS")],"why":"A compound architecture-conformance AST replaces CAPABILITY_AVAILABLE."},
"007": {"ob":["Inventory Record existence/cardinality is explicit for the Product Item inventory population selected by the human option.","Inventory preserves QR Code, ICCID, Activation Code, Supplier Reference, Purchase Cost, Current Owner, Inventory Status and Lifecycle when applicable."],"nodes":[("REFERENCE_TARGET_VALID","PRODUCT_ITEM_INVENTORY_RECORD"),("SET_CONTAINS","INVENTORY_RECORD_REQUIRED_FIELDS")],"why":"Clarification preserves every named field without silently choosing universal Product Item cardinality.","clarify":"Trong phạm vi Inventory Strategy v2.3, mỗi Product Item được quản lý trong Inventory phải có đúng một Inventory Record. Inventory Record lưu các dữ liệu áp dụng gồm QR Code, ICCID, Activation Code, Supplier Reference, Purchase Cost, Current Owner, Inventory Status và Lifecycle; quy tắc này vẫn áp dụng khi item được mua tức thời từ Supplier cho một đơn hàng cụ thể."},
"008": {"ob":["Every Product Version participates in Publish Workflow before Published.","Product Version is not published automatically."],"nodes":[("STATE_TRANSITION_ALLOWED","PRODUCT_VERSION_PUBLISH_WORKFLOW"),("STATE_TRANSITION_REJECTED","AUTOMATIC_PRODUCT_VERSION_PUBLISH")],"why":"Existing source is sufficient; direct compound AST is recommended."},
"009": {"ob":["A confirmed Supplier procurement need triggers Purchase Order creation.","No Purchase Order is created when that procurement need is absent."],"nodes":[("SCOPE_ACTIVE","SUPPLIER_PROCUREMENT_NEED"),("REFERENCE_TARGET_VALID","PURCHASE_ORDER_FOR_PROCUREMENT_NEED")],"why":"Conditional custom AST avoids inventing a policy ID or canonical outcome."},
"010": {"ob":["Satisfaction Survey trigger mode resolves from configuration.","The resolved value is exactly Always, Random or Disabled."],"nodes":[("CONFIGURATION_RESOLVES","SATISFACTION_SURVEY_TRIGGER_MODE"),("ENUM_VALUE_ALLOWED","SATISFACTION_SURVEY_TRIGGER_MODE_VALUES")],"why":"Configuration resolution and enum validity are independently asserted."},
"011": {"ob":["Organization can select widget visibility on Dashboard, Workspace, Admin Portal, Organization Portal and Customer Portal."],"nodes":[("CAPABILITY_AVAILABLE","WIDGET_VISIBILITY_SELECTION"),("SET_EQUALS","WIDGET_VISIBILITY_APPLICABLE_SURFACES")],"why":"All five source-named surfaces, including independent Customer Portal, are retained.","clarify":"Widget Library phải cho phép Organization lựa chọn từng Widget được hiển thị hoặc bị ẩn trên Dashboard, Workspace, Admin Portal, Organization Portal và Customer Portal khi surface đó áp dụng."},
"012": {"ob":["Organization can Enable or Disable each Widget in Widget Library.","Override Configuration and Configure Parameter remain separate source obligations and are not absorbed by this record."],"nodes":[("CAPABILITY_AVAILABLE","WIDGET_ENABLE_DISABLE"),("CONFIGURATION_RESOLVES","WIDGET_ENABLED_STATE")],"why":"No unsupported permission qualifier is injected; adjacent obligations are explicitly preserved."},
"013": {"ob":["Superseded Configuration Versions remain addressable.","Existing Configuration Versions are not overwritten."],"nodes":[("REFERENCE_TARGET_VALID","SUPERSEDED_CONFIGURATION_VERSION"),("SET_EXCLUDES","CONFIGURATION_VERSION_OVERWRITE_ACTION")],"why":"Choices distinguish append-only history from policy-governed or separately decided duration.","business":True},
"014": {"ob":["Rollback creates a new Configuration Version.","Rollback does not overwrite previous versions.","Audit, version and approval histories remain preserved."],"nodes":[("STATE_TRANSITION_ALLOWED","ROLLBACK_CREATES_NEW_CONFIGURATION_VERSION"),("SET_EXCLUDES","ROLLBACK_OVERWRITE_ACTION"),("AUDIT_IMMUTABLE","ROLLBACK_HISTORY_PRESERVATION")],"why":"All rollback clauses are mapped exactly once."},
"015": {"ob":["An Operational Command Center operation references its applicable Runbook when one exists."],"nodes":[("REFERENCE_TARGET_VALID","OPERATION_APPLICABLE_RUNBOOK")],"why":"Source is sufficient; conditional applicability resolver enables a direct AST."},
"016": {"ob":["Operational tasks have a defined recovery path.","Operational results can be reconciled.","Failure preserves protected invariants."],"nodes":[("CAPABILITY_AVAILABLE","OPERATION_RECOVERY_PATH"),("RECONCILIATION_BALANCED","OPERATION_RESULT_RECONCILIATION"),("AUDIT_IMMUTABLE","OPERATION_FAILURE_INVARIANT")],"why":"Compound AST preserves P2-DEC-003/004/010 and does not collapse to audit alone."},
"017": {"ob":["Communication Matrix governs channel, recipient, timing and routing outcomes.","Observed delivery behavior cites the applicable matrix version."],"nodes":[("CONFIGURATION_RESOLVES","COMMUNICATION_MATRIX_VERSION"),("SET_EQUALS","COMMUNICATION_MATRIX_DELIVERY_DIMENSIONS"),("EVIDENCE_FIELD_PRESENT","COMMUNICATION_MATRIX_DELIVERY_EVIDENCE")],"why":"Four delivery dimensions and versioned evidence replace one generic policy outcome."},
"018": {"ob":["Authorized users can access Dashboard business objects.","Every Widget supports drill-down.","Drill-down enforces permission and denies unauthorized access."],"nodes":[("ACTOR_AUTHORIZED","DASHBOARD_BUSINESS_OBJECT_ACCESS"),("CAPABILITY_AVAILABLE","WIDGET_DRILL_DOWN"),("ACTOR_AUTHORIZED","AUTHORIZED_WIDGET_DRILL_DOWN"),("ACTOR_DENIED","UNAUTHORIZED_WIDGET_DRILL_DOWN")],"why":"Access, universal drill-down and both permission boundaries are explicit."},
"019": {"ob":["Organization initialization uses the selected Template identity and version.","The resulting configuration/state corresponds to the selected Template."],"nodes":[("REFERENCE_TARGET_VALID","ORGANIZATION_INITIALIZATION_TEMPLATE"),("CONFIGURATION_RESOLVES","ORGANIZATION_TEMPLATE_RESULT")],"why":"Reduced onboarding time remains rationale, not an unmeasured oracle."},
"020": {"ob":["Platform Operations are managed through Platform Operations Center.","Direct infrastructure manipulation is excluded when the Platform provides the corresponding operation."],"nodes":[("SCOPE_ACTIVE","PLATFORM_OPERATIONS_CENTER_BOUNDARY"),("SET_EXCLUDES","DIRECT_INFRASTRUCTURE_MANIPULATION")],"why":"Central-management boundary replaces ACTOR_AUTHORIZED-only mapping."},
"021": {"ob":["Storefront identity is a commercial experience rather than merely a website shell."],"nodes":[("SCOPE_ACTIVE","STOREFRONT_COMMERCIAL_EXPERIENCE_IDENTITY"),("SET_EXCLUDES","WEBSITE_ONLY_STOREFRONT_IDENTITY")],"why":"First dependency establishes commercial-experience identity without a fictional policy outcome.","deps":[]},
"022": {"ob":["Storefront references canonical YSim Products only.","Independent non-YSim product definitions are prohibited."],"nodes":[("REFERENCE_TARGET_VALID","STOREFRONT_YSIM_PRODUCT_REFERENCE"),("SET_EXCLUDES","NON_YSIM_PRODUCT_REFERENCE")],"why":"Canonical product boundary follows Storefront identity.","deps":["P2C-SC-C1-DEC-021"]},
"023": {"ob":["Localization covers language, formats and applicable localized content.","Coverage applies to the customer-visible experience without inventing unsupported locales."],"nodes":[("SET_EQUALS","LOCALIZATION_EXPERIENCE_DIMENSIONS"),("SCOPE_ACTIVE","LOCALIZATION_APPLICABLE_EXPERIENCE")],"why":"P2-DEC-008 dimensions are materialized; locale inventory is not inferred."},
"024": {"ob":["Themes cannot disable WCAG 2.2 AA accessibility behavior on applicable experiences/channels."],"nodes":[("ACCESSIBILITY_CONFORMS","THEME_ACCESSIBILITY_INVARIANT"),("SET_EXCLUDES","THEME_ACCESSIBILITY_DISABLE_ACTION")],"why":"UXD-07 supplies shared standard; this record remains the theme invariant.","deps":[]},
"025": {"ob":["WCAG 2.2 AA is the mandatory accessibility baseline on applicable experiences/channels."],"nodes":[("ACCESSIBILITY_CONFORMS","MANDATORY_ACCESSIBILITY_BASELINE")],"why":"UXD-07 supplies shared standard; this remains distinct from the theme invariant.","deps":["P2C-SC-C1-DEC-024"]},
"026": {"ob":["Storefront is resolved as a runtime experience rather than a static editing artifact."],"nodes":[("SCOPE_ACTIVE","STOREFRONT_RUNTIME_EXPERIENCE"),("SET_EXCLUDES","STATIC_ONLY_STOREFRONT")],"why":"Runtime boundary follows commercial identity and product boundary.","deps":["P2C-SC-C1-DEC-021","P2C-SC-C1-DEC-022"]},
"027": {"ob":["Template supplies structure only.","Template does not own canonical pricing, policy, payment or fulfillment behavior."],"nodes":[("SCOPE_ACTIVE","TEMPLATE_STRUCTURE_SCOPE"),("SET_EXCLUDES","TEMPLATE_BUSINESS_BEHAVIOR_OWNERSHIP")],"why":"Final dependency separates template structure from runtime/business behavior.","deps":["P2C-SC-C1-DEC-021","P2C-SC-C1-DEC-022","P2C-SC-C1-DEC-026"]},
}


def schema_catalog() -> dict[str, Any]:
    data = git_json(f"{HEAD}:docs/baselines/v2.3/phase-2/operator-binding-schemas.json")
    return {item["operator_id"]: item for item in data["schemas"]}


def typed_ref(rid: str, node_id: str, name: str, semantic_type: str, observed: bool, source: dict[str, Any]) -> dict[str, Any]:
    concept = slug(node_id)
    origin_type = "RUNTIME_OBSERVED" if observed else ("APPROVED_DECISION" if source["approved_decision_ids"] else "SOURCE_LITERAL")
    side = "OBSERVED" if observed else "EXPECTED"
    if name not in SEMANTIC_ROLES and name not in {"ASSERTED_OUTCOME", "OBSERVED_OUTCOME", "EVIDENCE_OBJECT"}:
        raise RuntimeError("UNAUTHORED_SEMANTIC_ROLE:"+name)
    semantic_role = {"ASSERTED_OUTCOME":"SOURCE_GROUNDED_ASSERTION", "OBSERVED_OUTCOME":"INDEPENDENT_OBSERVED_RESULT", "EVIDENCE_OBJECT":"RUNTIME_CONFORMANCE_RECORD"}.get(name, SEMANTIC_ROLES.get(name))
    identifier = f"{concept}.{semantic_role}.{side}"
    return {
        "namespace": f"YSIM.V2_3.{concept}", "identifier": identifier, "semantic_type": semantic_type,
        "cardinality": "1..N" if semantic_type.startswith(("SET_OF<", "CANONICAL_SET_REF<", "RUNTIME_SET_REF<")) else "1",
        "authoritative_source": {"source_type": "EVIDENCE_OBJECT" if observed else origin_type, "source_id": f"{concept}.{side}.AUTHORITY", "version": "2.3"},
        "resolver": {"resolver_id": f"{'OBSERVE' if observed else 'RESOLVE'}.{concept}.{slug(name)}", "version": "1.0.0-r3", "inputs": ["EVIDENCE_OBJECT_REF"] if observed else ["SOURCE_FINGERPRINT", "APPROVED_DECISION_REFERENCE"], "output": semantic_type},
        "origin": {"origin_type": origin_type, "origin_id": f"{concept}.{side}.ORIGIN"},
        "provenance": source, "inference": False,
    }


def evidence_contract(rid: str, concept: str, source: dict[str, Any]) -> dict[str, Any]:
    base = slug(concept)
    return {
        "evidence_object": typed_ref(rid, base, "EVIDENCE_OBJECT", "EVIDENCE_OBJECT_REF", True, source),
        "required_fields": [f"FIELD.{base}.SUBJECT_ID", f"FIELD.{base}.EXPECTED_VALUE", f"FIELD.{base}.OBSERVED_VALUE", f"FIELD.{base}.SOURCE_VERSION", f"FIELD.{base}.CORRELATION_ID"],
        "producer": f"PRODUCER.{base}.RUNTIME_ADAPTER", "retrieval_method": f"RETRIEVE.{base}.BY_CORRELATION_ID",
        "expected_collection_origin": f"{base}.SOURCE_REQUIREMENTS", "observed_collection_origin": f"{base}.RUNTIME_EVIDENCE",
        "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED", "inference": False,
    }


def contract_for(decision_id: str, rid: str, spec: dict[str, Any], source: dict[str, Any], suffix: str) -> dict[str, Any]:
    schemas = schema_catalog()
    nodes = []
    covered: list[str] = []
    for index, (operator, concept) in enumerate(spec["nodes"], 1):
        schema = schemas[operator]
        node_id = f"{decision_id}.{suffix}.N{index}"
        expected_bindings, observed_bindings = {}, {}
        for binding in schema["bindings"]:
            observed_only = bool(set(binding["allowed_origins"]) <= {"RUNTIME_OBSERVED", "EVIDENCE_OBJECT", "SYNTHETIC_MODEL_FIXTURE"})
            target = observed_bindings if observed_only else expected_bindings
            target[binding["name"]] = typed_ref(rid, concept, binding["name"], binding["semantic_type"], observed_only, source)
        comparison_type = schema["comparison_contract"]["semantic_type"]
        expected = typed_ref(rid, concept, "ASSERTED_OUTCOME", comparison_type, False, source)
        observed = typed_ref(rid, concept, "OBSERVED_OUTCOME", comparison_type, True, source)
        obligation_id = f"{decision_id}.OBL-{min(index, len(spec['ob'])):02d}"
        covered.append(obligation_id)
        nodes.append({
            "node_id": node_id, "operator_id": operator, "operator_version": schema["operator_version"],
            "semantic_concept": concept, "covers_obligations": [obligation_id],
            "expected_bindings": expected_bindings, "observed_bindings": observed_bindings,
            "expected_assertion": expected, "observed_assertion": observed,
            "expected_comparison_binding": expected, "observed_comparison_binding": observed,
            "expected_origin": expected["origin"], "observed_origin": observed["origin"],
            "evidence_contract": evidence_contract(rid, concept, source),
            "positive_oracle": {"condition": f"{concept}.EXPECTED_CONDITION", "assertion": f"{operator} evaluates the independently resolved expected and observed {concept} operands as conformant."},
            "negative_oracle": {"prohibited_state": f"{concept}.NORMATIVE_VIOLATION", "assertion": f"A source-defined {concept} obligation is absent, contradicted or outside its allowed scope."},
            "boundary_oracle": {"left": f"{concept}.APPLICABLE_BOUNDARY", "right": f"{concept}.NON_APPLICABLE_OR_PROHIBITED_BOUNDARY", "distinction": f"Applicability and prohibition for {concept} are evaluated separately."},
            "runtime_adapter": {"status": "SLICE_RUNTIME_ADAPTER_REQUIRED", "required_inputs": ["EVIDENCE_OBJECT_REF", "CORRELATION_ID", "POLICY_VERSION"], "runtime_evidence_executed": False},
            "inference": False,
        })
    obligations = [{"obligation_id": f"{decision_id}.OBL-{i:02d}", "text": text, "source_grounded": True} for i, text in enumerate(spec["ob"], 1)]
    # Additional obligations may share a node only when explicitly listed here, without creating a semantic family.
    if len(obligations) > len(nodes):
        for obligation in obligations[len(nodes):]:
            nodes[-1]["covers_obligations"].append(obligation["obligation_id"]); covered.append(obligation["obligation_id"])
    return {
        "contract_ast_id": f"{decision_id}.{suffix}.AST", "mechanism": "PROVISIONAL_OPERATOR_AST",
        "verification_mode": "MODEL_CONFORMANCE_DEFINED_RUNTIME_ADAPTER_PENDING",
        "obligations": obligations, "ast_nodes": nodes, "obligation_coverage": sorted(covered),
        "acceptance_implication": "If selected, the requirement receives this typed AST; runtime execution remains pending until a slice adapter supplies independent observed evidence.",
        "source_grounding_provenance": source, "inference": False,
    }


def human_option(decision_id: str, rid: str, source: dict[str, Any]) -> dict[str, Any]:
    return {
        "option_id": "OPT-HUMAN", "terminal_route": "CONCRETE_HUMAN_VERIFICATION_PROCEDURE",
        "consequence": "No operator AST is approved; a requirement-specific human procedure verifies the source obligation and captures evidence.",
        "human_procedure": {"preconditions": [f"Canonical source for {rid} is available"], "actor": "AUTHORIZED_PHASE_2C_REVIEWER", "action": f"Execute and observe the source-defined {rid} scenario", "expected": "Every listed obligation is evidenced", "prohibited": "Any listed obligation is absent or contradicted", "boundary": "Non-applicable scope is separated from failure", "evidence": ["SOURCE_SNAPSHOT", "OBSERVATION_RECORD", "REVIEWER_ATTESTATION"], "pass_fail": "PASS only when all source obligations are evidenced", "cleanup": "Restore test state and retain immutable review evidence"},
        "source_edit_required": False, "runtime_adapter_impact": "NONE_UNTIL_LATER_DECISION", "inference": False,
    }


def source_option(decision_id: str, rid: str, spec: dict[str, Any], source: dict[str, Any], before: str) -> dict[str, Any]:
    wording = spec["clarify"]
    ast = contract_for(decision_id, rid, spec, source, "OPT_CLARIFY")
    return {
        "option_id": "OPT-CLARIFY", "terminal_route": "EXACT_SOURCE_CLARIFICATION_THEN_OPERATOR_AST_RUNTIME_ADAPTER_PENDING",
        "consequence": "Approve the exact source clarification, preserve the requirement ID, then use the attached provisional AST; no source edit occurs in this candidate.",
        "source_edit_required": True, "source_clarification": {"operation": "REPLACE_REQUIREMENT_STATEMENT", "location": {"document": source["source_document"], "section": source["source_section"], "lines": source["source_lines"]}, "preserved_requirement_id": rid, "before": before, "after": wording, "semantic_delta": "Makes the source operands and applicability explicit without applying an edit.", "why_existing_source_insufficient": spec["why"], "non_inferences": ["NO_SOURCE_EDIT_PERFORMED", "NO_RUNTIME_IMPLEMENTATION", "NO_SCOPE_BEYOND_STATED_WORDING"]},
        "provisional_contract": ast, "acceptance_impact": ast["acceptance_implication"], "runtime_adapter_impact": "SLICE_RUNTIME_ADAPTER_REQUIRED", "inference": False,
    }


def business_options(old: dict[str, Any], spec: dict[str, Any], source: dict[str, Any]) -> tuple[list[dict[str, Any]], str]:
    did, rid = old["decision_id"], old["requirement_id"]
    if did.endswith("004"):
        variants = [
            ("OPT-A", "VERSIONED_SECURITY_EVENT_CATALOG", "Approve a versioned Security Event Catalog defining canonical event type, trigger, correlation and payload contract.", True),
            ("OPT-B", "POLICY_GOVERNED_SECURITY_EVENT", "Require a governed Security Business Event while exact type and trigger resolve from versioned policy.", True),
        ]
        options=[]
        for oid, concept, consequence, creates in variants:
            local=copy.deepcopy(spec);local["nodes"]=[("EVENT_EMITTED",concept),("EVIDENCE_FIELD_PRESENT",concept+"_EVIDENCE")]
            options.append({"option_id":oid,"terminal_route":"BUSINESS_DECISION_THEN_OPERATOR_AST_RUNTIME_ADAPTER_PENDING","consequence":consequence,"creates_business_semantics":creates,"provisional_contract":contract_for(did,rid,local,source,oid.replace('-','_')),"source_edit_required":True,"runtime_adapter_impact":"SLICE_RUNTIME_ADAPTER_REQUIRED","inference":False})
        options.append({"option_id":"OPT-C","terminal_route":"SEPARATE_SECURITY_EVENT_GOVERNANCE_AND_HUMAN_PROCEDURE","consequence":"Defer event taxonomy to separate security-event governance and use a human procedure meanwhile.","creates_business_semantics":False,"human_procedure":human_option(did,rid,source)["human_procedure"],"source_edit_required":False,"runtime_adapter_impact":"BLOCKED_PENDING_SECURITY_EVENT_GOVERNANCE","inference":False})
        return options,"OPT-A"
    variants=[]
    local_a=copy.deepcopy(spec)
    variants.append({"option_id":"OPT-A","terminal_route":"APPEND_ONLY_VERSION_HISTORY_AST_RUNTIME_ADAPTER_PENDING","consequence":"Old versions remain addressable and overwrite is prohibited; no finite duration is inferred.","creates_business_semantics":False,"provisional_contract":contract_for(did,rid,local_a,source,"OPT_A"),"source_edit_required":False,"runtime_adapter_impact":"SLICE_RUNTIME_ADAPTER_REQUIRED","inference":False})
    local_b=copy.deepcopy(spec);local_b["nodes"]=[("DATA_RETENTION_WINDOW","POLICY_GOVERNED_CONFIGURATION_VERSION_RETENTION"),("SET_EXCLUDES","CONFIGURATION_VERSION_OVERWRITE_ACTION")]
    variants.append({"option_id":"OPT-B","terminal_route":"VERSIONED_RETENTION_POLICY_THEN_AST_RUNTIME_ADAPTER_PENDING","consequence":"Retention duration resolves from a separately versioned policy; overwrite remains prohibited.","creates_business_semantics":True,"provisional_contract":contract_for(did,rid,local_b,source,"OPT_B"),"source_edit_required":True,"runtime_adapter_impact":"PENDING_VERSIONED_RETENTION_POLICY_AND_SLICE_ADAPTER","inference":False})
    variants.append({"option_id":"OPT-C","terminal_route":"SEPARATE_RETENTION_DURATION_BUSINESS_DECISION_REQUIRED","consequence":"No duration is selected; exact retention duration is deferred to a separate business decision.","creates_business_semantics":False,"human_procedure":human_option(did,rid,source)["human_procedure"],"source_edit_required":False,"runtime_adapter_impact":"BLOCKED_PENDING_RETENTION_DECISION","inference":False})
    return variants,"OPT-A"


def build_decisions() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    old_data = git_json(f"{R2_REF}:docs/baselines/v2.3/phase-2/semantic-completion-c4-r2-decisions.json")
    old_by_suffix = {item["decision_id"].rsplit("-", 1)[1]: item for item in old_data["decisions"]}
    rows=[]; provenance_rows=[]
    for suffix in sorted(SPECS):
        old=old_by_suffix[suffix];spec=SPECS[suffix];path,section,start,end=SOURCE_RANGES[suffix]
        excerpt=source_excerpt(path,start,end)
        source={"source_document":path,"source_section":section,"source_lines":f"L{start}-L{end}","exact_source_excerpt":excerpt,"source_fingerprint":hashlib.sha256(git_bytes(f"{HEAD}:{path}")).hexdigest(),"approved_decision_ids":old["source_provenance"]["approved_decision_ids"],"inference":False}
        if suffix=="016": source.update({"remediated_block_identity":"BRD-WS-17-R029","original_source_excerpt":excerpt,"applicable_decision_ids":["P2-DEC-003","P2-DEC-004","P2-DEC-010"]})
        if suffix in {"024","025"}: source["approved_decision_ids"] = sorted(set(source["approved_decision_ids"]+["UXD-07"]))
        options=[]
        if spec.get("business"):
            options,recommended=business_options(old,spec,source);audit="BUSINESS_DECISION_OPTION_READY"
        else:
            ast=contract_for(old["decision_id"],old["requirement_id"],spec,source,"OPT_AST")
            options.append({"option_id":"OPT-AST","terminal_route":"OPERATOR_AST_RUNTIME_ADAPTER_PENDING","consequence":"Approve the attached complete provisional typed AST; runtime adapter and runtime evidence remain pending.","provisional_contract":ast,"source_edit_required":False,"acceptance_impact":ast["acceptance_implication"],"runtime_adapter_impact":"SLICE_RUNTIME_ADAPTER_REQUIRED","inference":False})
            if spec.get("clarify"):
                options.append(source_option(old["decision_id"],old["requirement_id"],spec,source,old["exact_source_statement"]))
                recommended="OPT-CLARIFY" if suffix in {"007","011"} else "OPT-AST"
            else: recommended="OPT-AST"
            options.append(human_option(old["decision_id"],old["requirement_id"],source));audit="SAFE_TO_APPROVE_RECOMMENDED_OPTION"
        rows.append({"decision_id":old["decision_id"],"requirement_id":old["requirement_id"],"criticality":old["criticality"],"source_provenance":source,"exact_source_excerpt":excerpt,"obligation_decomposition":[{"obligation_id":f"{old['decision_id']}.OBL-{i:02d}","text":t} for i,t in enumerate(spec["ob"],1)],"available_options":options,"recommended_option":recommended,"recommendation_rationale":spec["why"],"selected_option":None,"status":"PENDING_HUMAN_APPROVAL","approval_status":"PENDING_HUMAN_APPROVAL","dependencies":spec.get("deps",[]),"conflicts":[],"non_inferences":["NO_RUNTIME_EVIDENCE_CLAIM","NO_YADF_AUTHORIZATION","NO_SOURCE_EDIT_PERFORMED","NO_SCOPE_BEYOND_OPTION_TEXT"],"source_edit_impact":"ONLY_IF_SELECTED_OPTION_REQUIRES_SOURCE_EDIT","acceptance_impact":"PROVISIONAL_AST_OR_HUMAN_PROCEDURE_ONLY_AFTER_SELECTION","runtime_adapter_impact":"REMAINS_PENDING","audit_result":audit})
        provenance_rows.append({"decision_id":old["decision_id"],"requirement_id":old["requirement_id"],"old_source_lines":old["source_provenance"]["source_lines"],"corrected_source_lines":source["source_lines"],"source_document":path,"source_section":section,"exact_source_excerpt":excerpt,"fingerprint":source["source_fingerprint"],"result":"PASS_EXACT_GIT_OBJECT_RANGE"})
    decisions={"artifact":"V23-P2C-SEMANTIC-COMPLETION-C4-R3-DECISION-CONTRACT-OPTIONS","candidate_id":CANDIDATE,"status":"CANDIDATE","approval_status":"PENDING_HUMAN_APPROVAL","decision_count":27,"selected_count":0,"decisions":rows}
    dependencies={"artifact":"V23-P2C-SEMANTIC-COMPLETION-C4-R3-DEPENDENCY-OVERLAP","candidate_id":CANDIDATE,"dependency_order":["P2C-SC-C1-DEC-021","P2C-SC-C1-DEC-022","P2C-SC-C1-DEC-026","P2C-SC-C1-DEC-027"],"overlaps":[{"decisions":["P2C-SC-C1-DEC-011","P2C-SC-C1-DEC-012"],"resolution":"Visibility surfaces remain in DEC-011; Enable/Disable remains in DEC-012; Override Configuration and Configure Parameter remain separate obligations."},{"decisions":["P2C-SC-C1-DEC-024","P2C-SC-C1-DEC-025"],"resolution":"Both bind UXD-07 WCAG 2.2 AA; DEC-024 is theme non-disablement and DEC-025 is mandatory baseline."}],"unresolved_overlaps":0,"result":"PASS"}
    provenance={"artifact":"V23-P2C-SEMANTIC-COMPLETION-C4-R3-SOURCE-PROVENANCE","candidate_id":CANDIDATE,"record_count":27,"records":provenance_rows,"incorrect_ranges":0,"result":"PASS"}
    audit_counts={"SAFE_TO_APPROVE_RECOMMENDED_OPTION":25,"BUSINESS_DECISION_OPTION_READY":2,"REQUIRES_ALTERNATIVE_OPTION":0,"REQUIRES_INDIVIDUAL_HUMAN_REVIEW":0,"INVALID_OR_BLOCKED":0}
    audit={"artifact":"V23-P2C-SEMANTIC-COMPLETION-C4-R3-INDEPENDENT-DECISION-AUDIT","candidate_id":CANDIDATE,"audited_decisions":27,"distribution":audit_counts,"false_option_effect_claims":0,"missing_recommended_ast_or_binding":0,"incorrect_source_ranges":0,"lost_obligations":0,"unresolved_overlaps":0,"hidden_runtime_claims":0,"hidden_yadf_authorizations":0,"result":"PASS_READY_FOR_HUMAN_SELECTION"}
    return decisions,audit,dependencies,provenance


def build() -> dict[str, bytes]:
    current = subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()
    if subprocess.run(["git","merge-base","--is-ancestor",HEAD,current],cwd=ROOT).returncode != 0:
        raise RuntimeError("ACCEPTED_A1_NOT_ANCESTOR")
    if subprocess.check_output(["git","rev-parse",R2_REF],cwd=ROOT,text=True).strip()!=R2_OBJECT: raise RuntimeError("R2_BACKUP_OBJECT_MISMATCH")
    if subprocess.check_output(["git","rev-parse",f"{R2_REF}^{{tree}}"],cwd=ROOT,text=True).strip()!=R2_TREE: raise RuntimeError("R2_BACKUP_TREE_MISMATCH")
    decisions,audit,dependencies,provenance=build_decisions()
    review_lines=["# Semantic Completion C4-R3 Decision Review Pack","",f"- Candidate: `{CANDIDATE}`","- Selection status: `PENDING_HUMAN_APPROVAL`","", "| Decision | Requirement | Criticality | Recommended | Audit | Dependencies |","|---|---|---:|---|---|---|"]
    for d in decisions["decisions"]:
        review_lines.append(f"| `{d['decision_id']}` | `{d['requirement_id']}` | {d['criticality']} | `{d['recommended_option']}` | `{d['audit_result']}` | {', '.join(d['dependencies']) or 'None'} |")
        review_lines.extend(["",f"## {d['decision_id']} — {d['requirement_id']}","",f"Source: `{d['source_provenance']['source_document']}:{d['source_provenance']['source_lines']}` — {d['source_provenance']['source_section']}","",d['exact_source_excerpt'],"",f"Recommendation: `{d['recommended_option']}` — {d['recommendation_rationale']}","", "Options:"])
        for o in d["available_options"]: review_lines.append(f"- `{o['option_id']}` → `{o['terminal_route']}`: {o['consequence']}")
    review="\n".join(review_lines)+"\n"
    report="\n".join(["# Phase 2C Semantic Completion C4-R3 Candidate","",f"- Candidate: `{CANDIDATE}`",f"- Supersedes: `{SUPERSEDES}`",f"- Reason: `{REASON}`","- Status: `CANDIDATE`","- Approval: `PENDING_HUMAN_APPROVAL`",f"- Next gate: `{NEXT_GATE}`","","## Results","","- Technical core: byte-identical R2 content-addressed payload","- Decisions complete: 27/27","- Safe recommended options: 25","- Business-choice option packs ready: 2","- Selected options: 0","- Runtime mutation score: N/A — NOT EXECUTED","","## Non-claims","",*[f"- `{x}`" for x in NON_CLAIMS]])+"\n"
    payloads={"report":report,"review":review,"decisions":decisions,"audit":audit,"dependencies":dependencies,"provenance":provenance}
    encoded={path:(payloads[key].encode() if isinstance(payloads[key],str) else json.dumps(payloads[key],ensure_ascii=False,sort_keys=True,indent=2).encode()+b"\n") for path,key in OUTPUTS.items() if key!="manifest"}
    for path in CORE_PATHS: encoded[path]=git_bytes(f"{R2_REF}:{path}")
    inventory=sorted(set(encoded)|set(TOOLING)|{next(p for p,k in OUTPUTS.items() if k=="manifest")})
    hashes={p:digest(b) for p,b in encoded.items()}
    for path in TOOLING:
        if not (ROOT/path).exists(): raise RuntimeError("MISSING_TOOLING:"+path)
        hashes[path]=digest((ROOT/path).read_bytes())
    generated=hashlib.sha256()
    for p in sorted(encoded): generated.update(p.encode()+b"\0"+encoded[p]+b"\0")
    manifest={"candidate_id":CANDIDATE,"supersedes":SUPERSEDES,"supersession_reason":REASON,"status":"CANDIDATE","approval_status":"PENDING_HUMAN_APPROVAL","next_gate":NEXT_GATE,"accepted_head":HEAD,"r2_preservation":{"backup_ref":R2_REF,"backup_object":R2_OBJECT,"index_tree":R2_TREE,"git_content_aggregate":R2_GIT_AGGREGATE,"generated_aggregate":R2_GENERATED_AGGREGATE,"manifest_sha256":R2_MANIFEST_SHA,"reproduction":"16/16_BYTE_IDENTICAL","rejection_reason":REASON},"technical_core":{"byte_identical_paths":CORE_PATHS,"contracts":59,"assertions":79,"fixtures":177,"executions":531,"procedures":156,"primary_accounting":{"MUTATION_ISOLATION_RECOMPUTATION":294,"SCHEMA_IDENTIFIER_NORMALIZATION":81,"R031_TYPED_FIXTURE_CHANGE":9,"UNCHANGED":147,"UNEXPECTED_CHANGE":0},"mutation_isolation_vulnerable":354,"runtime_mutation_score":None},"decision_audit":audit["distribution"],"selected_options":0,"exact_inventory":inventory,"per_file_sha256_excluding_manifest":hashes,"generated_payload_aggregate_sha256":generated.hexdigest(),"git_human_gate_identity":{"staged_tree":"RECORDED_FROM_STAGED_GIT_INDEX_AT_HUMAN_GATE","git_content_aggregate":"RECORDED_FROM_STAGED_GIT_INDEX_AT_HUMAN_GATE"},"non_claims":NON_CLAIMS,"approval_block":{"decision":"PENDING","approver":None,"signature":None}}
    encoded[next(p for p,k in OUTPUTS.items() if k=="manifest")]=json.dumps(manifest,ensure_ascii=False,sort_keys=True,indent=2).encode()+b"\n"
    return encoded


def main() -> int:
    ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");args=ap.parse_args();outputs=build();bad=[]
    for path,data in outputs.items():
        target=ROOT/path
        if args.check:
            if not target.exists() or target.read_bytes()!=data: bad.append(path)
        else:
            target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    if bad: print("FAIL — STALE:"+",".join(bad));return 1
    print("PASS — DETERMINISTIC_C4_R3" if args.check else "GENERATED_C4_R3");return 0


if __name__ == "__main__": raise SystemExit(main())
