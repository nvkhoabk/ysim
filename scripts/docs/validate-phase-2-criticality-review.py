#!/usr/bin/env python3
"""Build and validate the deterministic Phase 2B criticality review payload."""

from __future__ import annotations

import argparse
import collections
import copy
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PHASE2 = ROOT / "docs/baselines/v2.3/phase-2"
REQUIREMENTS = ROOT / "docs/baselines/v2.3/requirements"
REVIEW_MD = PHASE2 / "PHASE_2_CRITICALITY_EXCEPTION_REVIEW_PACK.md"
REVIEW_JSON = PHASE2 / "phase-2-criticality-exception-review.json"
EXCEPTION_REGISTER = PHASE2 / "PHASE_2_CRITICALITY_EXCEPTION_REGISTER.md"
SUMMARY = PHASE2 / "phase-2-preflight-summary.json"
MAPPING = PHASE2 / "stable-id-mapping-candidate.json"
DECISIONS = PHASE2 / "phase-2-human-decisions.json"
FRAMEWORK = ROOT / "docs/baselines/v2.3/FRAMEWORK_DECISIONS.md"

SOURCE_COMMIT = "1a74dd7486945d3820e1d7c735f3b37cd9e418a7"
ACCEPTED_TAG = "baseline/v2.3/phase-2/decision-pack/c1-accepted"
SOURCE_DOCUMENT_COMMIT = "7f16d4c4b8ab514bd45de184f65ace221b03f4db"
REVIEW_ID = "V23-P2B-CRITICALITY-REVIEW-R2"
SUPERSEDED_REVIEW_ID = "V23-P2B-CRITICALITY-REVIEW-R1"
CURRENT = {"CRITICAL": 313, "HIGH": 409, "NORMAL": 348, "active_denominator": 1070}
CURRENT_SOURCE_PROJECTION = {
    **CURRENT,
    "inactive_not_applicable_for_v2_3": 106,
}
CLASSIFICATIONS = {
    "RULE_APPLICATION",
    "HUMAN_RISK_DECISION",
    "CLASSIFICATION_OR_EXTRACTION_DEFECT",
}
EXPECTED_DECISIONS = [f"P2-DEC-{number:03d}" for number in range(1, 11)]
CANDIDATE_ID = "V23-P2B-CRITICALITY-DECISION-C1"
SOURCE_REVIEW_ID = "V23-P2B-CRITICALITY-REVIEW-R2"
FAST_TRACK_AUTHORIZATION_DATE = "2026-07-15"
PROJECTION_QUALIFIER = "PROVISIONAL_EXCLUDES_PENDING_SOURCE_REMEDIATION_AND_CHILD_RECONCILIATION"
EARLIER_EXPLICIT_DECISION_IDS = {"P2-CRIT-EXC-001", "P2-CRIT-EXC-005"}
BUSINESS_MODEL_EXPLANATION = "Business Model là điểm khởi đầu của mọi Commerce Experience trên nền tảng YSim."
BUSINESS_PRINCIPLE_NAMES = [
    "Business Model First",
    "Template Driven",
    "Configuration over Customization",
    "White-label by Default",
    "Publish in Minutes",
    "Experience First",
    "Multi-brand",
    "Multi-language",
    "Multi-country",
    "API First",
    "Headless Ready",
    "AI Ready",
]
OPERATIONS_CHILD_STATEMENTS = [
    "Every operational task must be observable.",
    "Every operational task must be auditable.",
    "Every operational task must be configurable.",
    "Every operational task must be recoverable.",
    "Every operational task must be automatable.",
    "An operator must not directly manipulate infrastructure when the Platform provides the corresponding operation.",
]


def child_candidate(name: str, **extra: object) -> dict:
    return {
        "candidate_name": name,
        "candidate_id": None,
        "semantic_normalization_required": True,
        "overlap_alias_check_required": True,
        "scope_confirmation_required": True,
        "atomicity_review_required": True,
        **extra,
    }


BUSINESS_PRINCIPLE_CHILD_CANDIDATES = [
    child_candidate(
        name,
        **({"explanatory_source_sentence": BUSINESS_MODEL_EXPLANATION} if name == "Business Model First" else {}),
        **({
            "non_inference_guard":
                "MUST_NOT_BE_INTERPRETED_AS_AN_ACTIVE_AI_PRODUCT_FEATURE_WITHOUT_AN_APPROVED_REQUIREMENT"
        } if name == "AI Ready" else {}),
    )
    for name in BUSINESS_PRINCIPLE_NAMES
]
OPERATIONS_CHILD_CANDIDATES = [
    child_candidate(statement)
    for statement in OPERATIONS_CHILD_STATEMENTS
]

RELATED_NON_EXCEPTION_EXTRACTION_DEFECTS = [
    {
        "requirement_id": "BRD-EVENT-INDEX-R001",
        "preserve_stable_id": "BRD-EVENT-INDEX-R001",
        "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
        "existing_truncated_statement": "phải đảm bảo thứ tự xử lý.",
        "effective_statement_candidate":
            "Payment, Settlement, and Financial events must preserve processing order.",
        "remediation": "EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT",
        "corrected_source_coverage_candidate": "L193-L197",
        "source_exception": False,
        "increases_source_exception_count": False,
        "carry_into_later_source_remediation_and_validation": True,
    }
]

REGISTRY_VALIDATOR = ROOT / "scripts/docs/validate-requirement-registry.py"
REGISTRY_APPROVAL_VALIDATOR = ROOT / "scripts/docs/validate-requirement-registry-approval.py"
PREFLIGHT_VALIDATOR = ROOT / "scripts/docs/validate-phase-2-preflight.py"
PACK_APPROVAL_VALIDATOR = ROOT / "scripts/docs/validate-phase-2-decision-pack-approval.py"

PROTECTED_PATHS = [
    "docs/BRD",
    "docs/UXF",
    "docs/baselines/v2.3/FRAMEWORK_DECISIONS.md",
    "docs/baselines/v2.3/REQUIREMENT_REGISTRY_FREEZE_APPROVAL.md",
    "docs/baselines/v2.3/REQUIREMENT_REGISTRY_FREEZE_CANDIDATE.md",
    "docs/baselines/v2.3/requirements",
    "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_EXCEPTION_REGISTER.md",
    "docs/baselines/v2.3/phase-2/PHASE_2_DECISION_REGISTER.md",
    "docs/baselines/v2.3/phase-2/PHASE_2_DOCUMENT_REMEDIATION_CONTRACT.md",
    "docs/baselines/v2.3/phase-2/PHASE_2_HUMAN_DECISION_PACK.md",
    "docs/baselines/v2.3/phase-2/PHASE_2_HUMAN_DECISION_PACK_APPROVAL.md",
    "docs/baselines/v2.3/phase-2/PHASE_2_PREFLIGHT_REPORT.md",
    "docs/baselines/v2.3/phase-2/phase-2-human-decisions.json",
    "docs/baselines/v2.3/phase-2/phase-2-preflight-summary.json",
    "docs/baselines/v2.3/phase-2/stable-id-mapping-candidate.json",
    "scripts/docs/validate-requirement-registry.py",
    "scripts/docs/validate-requirement-registry-approval.py",
    "scripts/docs/validate-phase-2-preflight.py",
    "scripts/docs/validate-phase-2-decision-pack-approval.py",
]

ALLOWED_PHASE_2B_PATHS = {
    "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_EXCEPTION_REVIEW_PACK.md",
    "docs/baselines/v2.3/phase-2/phase-2-criticality-exception-review.json",
    "scripts/docs/validate-phase-2-criticality-review.py",
    "docs/baselines/v2.3/phase-2/PHASE_2_CRITICALITY_DECISION_APPROVAL.md",
    "scripts/docs/validate-phase-2-criticality-decision-approval.py",
}


def option(option_id: str, decision: str, target: str, description: str) -> dict:
    return {
        "option_id": option_id,
        "decision": decision,
        "target": target,
        "description": description,
    }


def tier_options(recommended: str, *tiers: str) -> list[dict]:
    descriptions = {
        "CRITICAL": "Apply the CRITICAL verification contract, including applicable fail-closed and boundary evidence.",
        "HIGH": "Apply the HIGH verification contract with expected-path and primary failure/edge evidence.",
        "NORMAL": "Apply the NORMAL verification contract with at least one observable pass/fail criterion.",
    }
    return [option("CONFIRM_" + tier, "CLASSIFY_AS_" + tier, tier, descriptions[tier]) for tier in tiers]


def defect_options() -> list[dict]:
    return [
        option(
            "ROUTE_TO_REMEDIATION",
            "REMEDIATE_RULE_INPUT_BEFORE_CRITICALITY",
            "KEEP_CURRENT",
            "Do not make an ordinary tier override; correct the identified scope, extraction, or classification input and rerun the rules.",
        ),
        option(
            "REJECT_DEFECT_AND_KEEP_PROVISIONAL",
            "REJECT_DEFECT_FINDING",
            "KEEP_CURRENT",
            "Reject the defect finding with explicit human rationale and retain the current provisional tier.",
        ),
    ]


def cluster(
    number: int,
    title: str,
    members: list[int],
    classification: str,
    question: str,
    recommended: str,
    rationale: str,
    under: str,
    acceptance: str,
    confidence: str,
    options: list[dict],
    decisions: list[str] | None = None,
    selected_option: str | None = None,
    review_status: str = "OPEN",
    remediation_contract: dict | None = None,
) -> dict:
    return {
        "cluster_id": f"P2-CRIT-CL-{number:03d}",
        "title": title,
        "member_exception_ids": [f"P2-CRIT-EXC-{member:03d}" for member in members],
        "finding_classification": classification,
        "common_decision_question": question,
        "recommended_option": recommended,
        "recommendation_rationale": rationale,
        "business_technical_risk_rationale": rationale,
        "consequences_of_under_classification": under,
        "acceptance_depth_impact": acceptance,
        "confidence": confidence,
        "applicable_approved_decisions": decisions or [],
        "uniform_resolution_safe": True,
        "selected_option": selected_option,
        "review_status": review_status,
        "remediation_contract": remediation_contract,
        "options": options,
    }


CLUSTER_SPECS = [
    cluster(33, "Product Variant inactive-scope human decision", [1], "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "Should Product Variant remain outside v2.3 and be routed to inactive-scope remediation?",
            "ROUTE_TO_SCOPE_REMEDIATION",
            "Product Variant has no approved scope promotion; the human selected option 1 to retain it outside v2.3.",
            "Keeping Product Variant active would contradict the selected scope decision and create an implementation-acceptance obligation for an excluded capability.",
            "Use NOT_APPLICABLE_FOR_V2.3 and assign no verification criticality while inactive.", "HIGH",
            [option("ROUTE_TO_SCOPE_REMEDIATION", "REMEDIATE_AS_INACTIVE", "INACTIVE", "Set FUTURE or equivalent inactive v2.3 scope and NOT_APPLICABLE_FOR_V2.3 acceptance applicability."),
             option("KEEP_ACTIVE_WITH_NEW_SCOPE_PROMOTION", "KEEP_ACTIVE", "KEEP_CURRENT", "Require a new approved scope-promotion decision; none exists in the current authority set.")],
            decisions=["SD-02", "HUMAN_DECISION_2026-07-14"],
            selected_option="ROUTE_TO_SCOPE_REMEDIATION",
            review_status="DECIDED_PENDING_REVIEW_PACK_APPROVAL",
            remediation_contract={
                "target_scope": "FUTURE_OR_EQUIVALENT_INACTIVE_V2_3",
                "acceptance_applicability": "NOT_APPLICABLE_FOR_V2.3",
                "verification_criticality": None,
                "decision_status": "DECIDED_PENDING_REVIEW_PACK_APPROVAL",
                "decision_provenance": "Human selected option 1 on 2026-07-14; unpromoted legacy future capabilities remain outside v2.3.",
            }),
    cluster(34, "Shared Approval Engine approved scope promotion", [3], "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "How must the legacy CAP-9003 Future row be remediated to reflect the approved v2.3 Shared Approval Engine?",
            "APPROVED_SCOPE_PROMOTION_REMEDIATION",
            "SD-03 and BDD-27 override the legacy Future label and require an active Shared Approval Engine distinct from general-purpose BPM workflow.",
            "Routing the capability inactive would violate approved scope and omit separation-of-duties, expiry, escalation, evidence, and immutable-audit obligations.",
            "Keep HIGH only as provisional; rewrite the active contract and re-evaluate type and criticality before acceptance depth is finalized.", "HIGH",
            [option("APPROVED_SCOPE_PROMOTION_REMEDIATION", "REWRITE_AS_ACTIVE_SHARED_APPROVAL_ENGINE", "KEEP_CURRENT", "Rewrite the legacy row as the active Shared Approval Engine with SD-03/BDD-27 provenance."),
             option("ESCALATE_APPROVED_PRECEDENCE_CONFLICT", "ESCALATE_PRECEDENCE_CONFLICT", "KEEP_CURRENT", "Escalate only if an approved authority is believed to supersede SD-03/BDD-27; do not route inactive.")],
            decisions=["SD-03", "BDD-27"],
            review_status="DETERMINISTIC_REMEDIATION_IDENTIFIED",
            remediation_contract={
                "target_scope": "V2.3_ACTIVE",
                "route": "APPROVED_SCOPE_PROMOTION_REMEDIATION",
                "provisional_criticality": "HIGH",
                "criticality_finalized": False,
                "required_source_remediation": "Rewrite the legacy row into the active Shared Approval Engine contract with SD-03 and BDD-27 provenance.",
                "excluded_inference": "GENERAL_PURPOSE_BPM_WORKFLOW_ENGINE",
            }),
    cluster(35, "Rule-based Fraud/Risk Engine approved scope promotion", [20], "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "How must the legacy Anti Fraud Engine future statement be remediated to separate active rule-based risk from deferred ML?",
            "APPROVED_SCOPE_PROMOTION_REMEDIATION",
            "SD-03 requires rule-based Fraud/Risk for authentication, checkout, and payment while advanced/ML scoring remains post-v2.3.",
            "Routing the whole capability inactive would remove approved authentication, checkout, and payment risk controls.",
            "Keep CRITICAL only as provisional; split/rewrite the statement and re-evaluate type and criticality before acceptance depth is finalized.", "HIGH",
            [option("APPROVED_SCOPE_PROMOTION_REMEDIATION", "SPLIT_ACTIVE_RULE_BASED_AND_DEFERRED_ML", "KEEP_CURRENT", "Rewrite/split the legacy statement so rule-based behavior is active and ML/advanced scoring is deferred."),
             option("ESCALATE_APPROVED_PRECEDENCE_CONFLICT", "ESCALATE_PRECEDENCE_CONFLICT", "KEEP_CURRENT", "Escalate only if an approved authority is believed to supersede SD-03; do not route the whole capability inactive.")],
            decisions=["SD-03", "BDD-26"],
            review_status="DETERMINISTIC_REMEDIATION_IDENTIFIED",
            remediation_contract={
                "target_scope": "V2.3_ACTIVE_RULE_BASED",
                "deferred_scope": "ML_AND_ADVANCED_SCORING_POST_V2.3",
                "active_surfaces": ["LOGIN_AUTHENTICATION", "CHECKOUT", "PAYMENT"],
                "route": "APPROVED_SCOPE_PROMOTION_REMEDIATION",
                "provisional_criticality": "CRITICAL",
                "criticality_finalized": False,
                "required_source_remediation": "Rewrite or split the legacy statement into active rule-based behavior and explicitly deferred ML.",
            }),
    cluster(2, "Event Ordering R002 deterministic extraction remediation", [4], "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "Must the Marketing, Analytics, and Notification subject list be restored before criticality is re-evaluated?", "EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT",
            "The extracted statement contains only the trailing predicate; source context distinguishes ordered financial events from unordered marketing, analytics, and notification events.",
            "A fragment-level tier can attach ordering evidence to the wrong event families and hide data-integrity or delivery risks.",
            "Acceptance and criticality remain unfinalized until the corrected effective statement is re-evaluated.", "HIGH",
            [option("EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT", "REMEDIATE_RULE_INPUT_BEFORE_CRITICALITY", "KEEP_CURRENT", "Expand coverage to the subject list and predicate, rewrite the effective statement, and then re-evaluate criticality."),
             option("REJECT_DEFECT_AND_KEEP_PROVISIONAL", "REJECT_DEFECT_FINDING", "KEEP_CURRENT", "Reject the extraction defect with explicit human rationale and retain the current provisional tier.")],
            ["P2-DEC-002", "P2-DEC-004"],
            review_status="DETERMINISTIC_REMEDIATION_IDENTIFIED",
            remediation_contract={
                "remediation": "EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT",
                "preserve_stable_id": "BRD-EVENT-INDEX-R002",
                "existing_truncated_statement": "không bắt buộc Ordering.",
                "effective_statement_candidate": "Marketing, Analytics, and Notification events are not required to preserve processing order.",
                "corrected_source_coverage_candidate": "L201-L205",
                "source_coverage_includes_event_family_subjects_and_predicate": True,
                "requirement_type": "DESIGN_PRINCIPLE",
                "scope_status": "V2.3_ACTIVE",
                "criticality_finalized": False,
                "criticality_re_evaluation_required": True,
            }),
    cluster(3, "Business Principles composite-parent human decision", [5], "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "Should BRD-UPDATE-01-R010 become a composite parent pending atomic child reconciliation?", "COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION",
            "The statement merely introduces a list and contains no independently verifiable principle.",
            "Treating a preamble as an atomic HIGH unit inflates coverage while providing no observable obligation.",
            "Only resulting canonical atomic children receive criticality and acceptance contracts.", "HIGH",
            [option("COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION", "MODEL_COMPOSITE_PARENT_AND_RECONCILE_ATOMIC_CHILDREN", "KEEP_CURRENT", "Retain the stable parent as a non-unit composite and reconcile the twelve named candidates before allocating child IDs or changing counts."),
             option("REJECT_COMPOSITE_MODEL_AND_KEEP_PROVISIONAL", "REJECT_COMPOSITE_MODEL", "KEEP_CURRENT", "Reject the composite model with explicit human rationale and retain the provisional source representation.")],
            ["P2-DEC-005", "HUMAN_DECISION_2026-07-14"],
            selected_option="COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION",
            review_status="DECIDED_PENDING_REVIEW_PACK_APPROVAL",
            remediation_contract={
                "decision": "COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION",
                "decision_provenance": "Human selected option 1 on 2026-07-14.",
                "preserve_parent_stable_id": "BRD-UPDATE-01-R010",
                "source_coverage_candidate": "L629-L644",
                "composite_parent_candidate": True,
                "implementation_unit": False,
                "acceptance_unit": False,
                "scope_coverage_unit": False,
                "criticality_unit": False,
                "do_not_blindly_create_twelve_requirements": True,
                "structural_count_impact": "PENDING_CHILD_RECONCILIATION",
                "projected_count_changes_applied": False,
                "child_id_allocation": "DEFERRED_PENDING_OVERLAP_RECONCILIATION",
                "criticality_assignment_target": "RESULTING_CANONICAL_ATOMIC_CHILDREN_ONLY",
                "child_candidates": BUSINESS_PRINCIPLE_CHILD_CANDIDATES,
            }),
    cluster(4, "Enterprise Operations composite-parent deterministic remediation", [23], "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "Should BRD-WS-17-R013 become a composite parent with six atomic child candidates?", "COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN",
            "The extraction ends at a colon and omits every capability that gives the principle meaning.",
            "A generic HIGH label can mask CRITICAL audit/recovery obligations and under-specify operational failure evidence.",
            "Each resulting canonical atomic child receives its own type, criticality, and acceptance contract.", "HIGH",
            [option("COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN", "MODEL_COMPOSITE_PARENT_AND_RECONCILE_ATOMIC_CHILDREN", "KEEP_CURRENT", "Retain the stable parent as a non-unit composite and reconcile the six atomic candidates before allocating child IDs or changing counts."),
             option("REJECT_COMPOSITE_MODEL_AND_KEEP_PROVISIONAL", "REJECT_COMPOSITE_MODEL", "KEEP_CURRENT", "Reject the deterministic composite model with explicit rationale and retain the provisional source representation.")],
            ["P2-DEC-003", "P2-DEC-004", "P2-DEC-010"],
            review_status="DETERMINISTIC_REMEDIATION_IDENTIFIED",
            remediation_contract={
                "decision": "COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN",
                "preserve_parent_stable_id": "BRD-WS-17-R013",
                "source_coverage_candidate": "L798-L810",
                "composite_parent_candidate": True,
                "implementation_unit": False,
                "acceptance_unit": False,
                "scope_coverage_unit": False,
                "criticality_unit": False,
                "structural_count_impact": "PENDING_CHILD_RECONCILIATION",
                "projected_count_changes_applied": False,
                "child_id_allocation": "DEFERRED_PENDING_OVERLAP_RECONCILIATION",
                "child_contract_assignment": "EACH_CHILD_RECEIVES_OWN_TYPE_CRITICALITY_AND_ACCEPTANCE_CONTRACT",
                "parent_to_child_coverage_semantics": "ALL_CHILDREN",
                "explanatory_non_requirement_sentence": "Đây là nguyên lý cốt lõi của Enterprise Operations Foundation.",
                "explanatory_sentence_becomes_requirement": False,
                "child_candidates": OPERATIONS_CHILD_CANDIDATES,
            }),
    cluster(5, "Product vision used as an atomic implementation unit", [16], "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "Is the positioning statement an atomic implementation requirement or non-normative product vision?", "ROUTE_TO_REMEDIATION",
            "The source describes market positioning rather than an observable system behavior.",
            "Forcing implementation acceptance onto vision wording invites arbitrary criteria and false traceability.",
            "Classification/identity must be corrected or a concrete derived requirement approved before acceptance depth is assigned.", "HIGH", defect_options()),
    cluster(6, "Context-free product-scope fragment", [17], "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "Must the subject and normative scope contract for the White-label Commerce fragment be restored before tiering?", "ROUTE_TO_REMEDIATION",
            "The statement is a list fragment without actor, obligation, or acceptance surface.",
            "A tier on the fragment does not establish what must be delivered and can duplicate more concrete storefront requirements.",
            "Acceptance is blocked until a complete normative statement and relationship to concrete requirements are established.", "HIGH", defect_options()),
    cluster(7, "Organization bootstrap security boundary", [2], "HUMAN_RISK_DECISION",
            "Does Organization Template bootstrap require CRITICAL verification because it creates roles and production configuration, or HIGH as a core administrative workflow?",
            "CONFIRM_CRITICAL",
            "Bootstrap creates authorization and runtime configuration together; an unsafe default can grant access or misconfigure an entire tenant.",
            "Under-classification may omit fail-closed, least-privilege, rollback, audit, and partial-bootstrap recovery evidence.",
            "CRITICAL adds negative/fail-closed and recovery/authorization-boundary evidence; HIGH covers the primary failure path only.", "MEDIUM",
            tier_options("CRITICAL", "CRITICAL", "HIGH"), ["P2-DEC-001", "P2-DEC-008", "P2-DEC-010"]),
    cluster(8, "Store currency capability", [6], "HUMAN_RISK_DECISION",
            "Is Currency a financial-integrity boundary requiring CRITICAL, or a white-label store capability adequately covered as HIGH?",
            "CONFIRM_HIGH",
            "The source places Currency beside branding and localization but does not state settlement, conversion, or ledger semantics.",
            "If transactional currency is intended, HIGH could omit fail-closed evidence for amount/currency mismatch; if only presentation is intended, CRITICAL overstates the contract.",
            "CRITICAL requires negative financial-integrity evidence; HIGH requires expected behavior plus the principal currency edge case.", "MEDIUM",
            tier_options("HIGH", "CRITICAL", "HIGH"), ["P2-DEC-010"]),
    cluster(9, "Commerce First principle", [7], "RULE_APPLICATION",
            "Should the Commerce First design principle remain HIGH rather than be treated as non-runtime descriptive governance?", "CONFIRM_HIGH",
            "The principle governs the product's core commerce behavior rather than presentation convenience.",
            "NORMAL could permit shallow evidence that fails to demonstrate the principle at the business-contract boundary.",
            "HIGH requires an expected commerce path and primary failure/edge path; NORMAL would require only one observable criterion.", "MEDIUM",
            tier_options("HIGH", "HIGH", "NORMAL")),
    cluster(10, "Configuration over Customization principle", [8], "HUMAN_RISK_DECISION",
            "Is this an enforceable runtime/configuration boundary at HIGH, or non-runtime governance at NORMAL?", "CONFIRM_NORMAL",
            "The isolated principle does not specify production configuration integrity or a runtime acceptance surface.",
            "If it actually constrains runtime customization, NORMAL may miss unsafe bypass and unsupported customization paths.",
            "NORMAL uses one observable governance criterion; HIGH adds the primary unsupported-customization failure path.", "MEDIUM",
            tier_options("NORMAL", "HIGH", "NORMAL"), ["P2-DEC-010"]),
    cluster(11, "White-label by Default principle", [9], "HUMAN_RISK_DECISION",
            "Is White-label by Default a core product delivery obligation at HIGH or a descriptive design principle at NORMAL?", "CONFIRM_HIGH",
            "White-label behavior is central to the approved platform proposition, but the principle alone lacks a concrete runtime surface.",
            "NORMAL may under-test tenant branding defaults and fallback; HIGH may over-interpret a broad principle without derived requirements.",
            "HIGH adds a primary fallback/edge path; NORMAL retains a single observable conformance criterion.", "MEDIUM",
            tier_options("HIGH", "HIGH", "NORMAL")),
    cluster(12, "Publish in Minutes principle", [10], "HUMAN_RISK_DECISION",
            "Is Publish in Minutes a HIGH core publishing workflow obligation or NORMAL product-positioning metadata?", "CONFIRM_HIGH",
            "Publishing speed affects a core storefront workflow, although the source provides no numeric threshold.",
            "NORMAL could omit failed-publish and rollback evidence; HIGH without a clarified threshold could still create unverifiable acceptance.",
            "HIGH requires expected publish plus primary failure/edge evidence; the later document correction must supply an observable budget.", "MEDIUM",
            tier_options("HIGH", "HIGH", "NORMAL"), ["P2-DEC-009", "P2-DEC-010"]),
    cluster(13, "Multi-tenant principle", [11], "HUMAN_RISK_DECISION",
            "Does Multi-tenant denote a CRITICAL tenant-isolation boundary or only a HIGH platform capability?", "CONFIRM_CRITICAL",
            "Tenant isolation is a security and data-integrity boundary, but the source statement names only the capability.",
            "HIGH may omit cross-tenant negative and authorization evidence; CRITICAL may add meaning if isolation is not the intended contract.",
            "CRITICAL requires fail-closed and authorization-boundary evidence; HIGH covers the principal tenant edge path.", "MEDIUM",
            tier_options("CRITICAL", "CRITICAL", "HIGH"), ["P2-DEC-001", "P2-DEC-008"]),
    cluster(14, "Multi-brand and multi-language platform capabilities", [12, 13], "HUMAN_RISK_DECISION",
            "Are these core white-label delivery capabilities uniformly HIGH, or descriptive/presentation capabilities at NORMAL?", "CONFIRM_HIGH",
            "Both capabilities materially shape storefront delivery across tenants while remaining outside direct financial or security boundaries.",
            "NORMAL could omit inheritance, fallback, and cross-brand/language edge evidence.",
            "HIGH requires expected resolution and the primary inheritance/fallback edge; NORMAL requires one observable criterion.", "MEDIUM",
            tier_options("HIGH", "HIGH", "NORMAL")),
    cluster(15, "Multi-country principle", [14], "HUMAN_RISK_DECISION",
            "Is Multi-country HIGH as a core platform capability, CRITICAL because it governs jurisdictional boundaries, or NORMAL as descriptive scope?", "CONFIRM_HIGH",
            "The statement implies international delivery but does not itself define jurisdiction, privacy, currency, or compliance behavior.",
            "A lower tier may miss country-specific failure paths; a CRITICAL tier may infer regulatory semantics not present in the source.",
            "HIGH adds the primary country-resolution edge; CRITICAL additionally requires applicable fail-closed boundary evidence.", "LOW",
            tier_options("HIGH", "CRITICAL", "HIGH", "NORMAL"), ["P2-DEC-010"]),
    cluster(16, "Experience Driven principle", [15], "HUMAN_RISK_DECISION",
            "Is Experience Driven an enforceable HIGH runtime/UX obligation or NORMAL descriptive governance?", "CONFIRM_NORMAL",
            "The phrase is broad and does not identify a journey, state, or contract boundary.",
            "If treated too lightly, concrete experience obligations may be missed; if treated as HIGH, acceptance must invent the missing meaning.",
            "NORMAL permits one explicit conformance criterion; HIGH requires a journey failure path that the source does not currently name.", "LOW",
            tier_options("NORMAL", "HIGH", "NORMAL")),
    cluster(17, "White-label Website sales channel", [18], "RULE_APPLICATION",
            "Should the concrete White-label Website sales-channel requirement remain HIGH?", "CONFIRM_HIGH",
            "It is an explicit storefront/channel delivery surface covered by the HIGH portal/storefront rule.",
            "NORMAL would under-test the primary channel workflow and its failure path.",
            "HIGH requires the expected storefront path and the principal channel failure/edge path.", "HIGH",
            tier_options("HIGH", "HIGH", "NORMAL")),
    cluster(18, "Pre-fulfillment commercial validation", [19], "RULE_APPLICATION",
            "Should pre-fulfillment commercial validation remain CRITICAL?", "CONFIRM_CRITICAL",
            "The validation gates fulfillment against commercial state and protects pricing, allocation, and fulfillment integrity.",
            "Under-classification could allow fulfillment after stale or inconsistent commercial state without fail-closed/recovery evidence.",
            "CRITICAL requires positive, negative fail-closed, and applicable retry/concurrency/reconciliation evidence.", "HIGH",
            tier_options("CRITICAL", "CRITICAL", "HIGH"), ["P2-DEC-003", "P2-DEC-010"]),
    cluster(19, "Identity, relationship, tenant, and published-rule boundaries", [21, 22, 27, 32], "RULE_APPLICATION",
            "Should all four explicit identity/authorization/isolation boundaries be CRITICAL?", "CONFIRM_CRITICAL",
            "Each member constrains identity ownership, relationship authority, tenant isolation, or the effect of identity on published business rules.",
            "Under-classification can omit cross-tenant, unauthorized relationship, or identity-induced rule-change negative evidence.",
            "CRITICAL requires fail-closed and authorization-boundary evidence wherever applicable.", "HIGH",
            tier_options("CRITICAL", "CRITICAL", "HIGH"), ["P2-DEC-001", "P2-DEC-008"]),
    cluster(20, "Accessibility safeguards", [29, 31], "RULE_APPLICATION",
            "Should high-contrast support and the prohibition on disabling accessibility remain HIGH?", "CONFIRM_HIGH",
            "Both are enforceable accessibility safeguards across experience surfaces and critical journeys.",
            "NORMAL could reduce coverage to a superficial positive check and omit theme-based regression/failure evidence.",
            "HIGH requires expected accessibility behavior and the primary theme/contrast failure path.", "HIGH",
            tier_options("HIGH", "HIGH", "NORMAL"), ["P2-DEC-009"]),
    cluster(21, "White-label no-source-code statements typed as UX requirements", [24, 33, 44], "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "Should these repeated architecture/principle statements be reclassified before criticality is decided?", "ROUTE_TO_REMEDIATION",
            "The records state an architecture/design principle and occur in principle/architecture sections, but are typed as UX_REQUIREMENT.",
            "An ordinary HIGH/NORMAL override would preserve a suspect rule input and could duplicate one semantic obligation three times.",
            "Reclassify/reconcile identity first, then derive acceptance depth from the surviving canonical obligation.", "HIGH", defect_options()),
    cluster(22, "Immutable published runtime configuration", [25], "RULE_APPLICATION",
            "Should immutable published runtime configuration remain CRITICAL?", "CONFIRM_CRITICAL",
            "The requirement protects production configuration and runtime data integrity.",
            "Under-classification could omit mutable-draft rejection, rollback, concurrency, and recovery evidence.",
            "CRITICAL requires fail-closed and applicable recovery/concurrency evidence in addition to the positive path.", "HIGH",
            tier_options("CRITICAL", "CRITICAL", "HIGH"), ["P2-DEC-010"]),
    cluster(23, "Runtime white-label support", [26], "RULE_APPLICATION",
            "Should explicit Experience Runtime white-label support remain HIGH?", "CONFIRM_HIGH",
            "This is a runtime delivery capability on the storefront/experience surface, not only descriptive governance.",
            "NORMAL could omit tenant-resolution and fallback failure evidence.",
            "HIGH requires the expected runtime path and the principal tenant/fallback edge path.", "HIGH",
            tier_options("HIGH", "HIGH", "NORMAL")),
    cluster(24, "Exclusive Allocation supplier selection", [28, 46], "RULE_APPLICATION",
            "Should both equivalent Allocation ownership statements remain CRITICAL pending later identity reconciliation?", "CONFIRM_CRITICAL",
            "P2-DEC-007 explicitly assigns supplier selection exclusively to Allocation; violating the boundary affects procurement and fulfillment integrity.",
            "Under-classification could omit direct-supplier bypass, unauthorized routing, and allocation recovery evidence.",
            "CRITICAL requires fail-closed and applicable recovery/idempotency evidence at the allocation boundary.", "HIGH",
            tier_options("CRITICAL", "CRITICAL", "HIGH"), ["P2-DEC-007"]),
    cluster(25, "Theme override granularity", [30], "RULE_APPLICATION",
            "Is overriding only required theme properties a NORMAL presentation/configuration rule or a HIGH runtime contract?", "CONFIRM_NORMAL",
            "The statement controls non-critical theme inheritance and does not itself govern accessibility or production integrity.",
            "If hidden runtime integrity semantics exist, NORMAL may miss fallback/regression evidence; none are explicit here.",
            "NORMAL requires one observable inheritance criterion; HIGH would add a primary override/fallback failure path.", "MEDIUM",
            tier_options("NORMAL", "HIGH", "NORMAL")),
    cluster(26, "Theme model principles typed as UX requirements", [39, 40, 41], "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "Should the Theme/Experience Profile model statements be reclassified as DESIGN_PRINCIPLE before tiering?", "ROUTE_TO_REMEDIATION",
            "All three records are in a Design Principles section and describe the configuration model rather than a user outcome.",
            "An ordinary tier override can conceal a type mismatch and lead to duplicated or implementation-shaped UX acceptance.",
            "Correct the classification, then decide whether the resulting design-principle evidence is NORMAL or linked to a stronger runtime requirement.", "HIGH", defect_options()),
    cluster(27, "Storefront pricing ownership boundary", [34], "RULE_APPLICATION",
            "Should the prohibition on Storefront owning Pricing remain CRITICAL?", "CONFIRM_CRITICAL",
            "The boundary prevents presentation code from controlling pricing integrity.",
            "Under-classification could omit tampered-price rejection and fail-closed evidence.",
            "CRITICAL requires negative pricing-integrity evidence in addition to the expected path.", "HIGH",
            tier_options("CRITICAL", "CRITICAL", "HIGH")),
    cluster(28, "Storefront allocation ownership boundary", [35], "RULE_APPLICATION",
            "Should the prohibition on Storefront owning Allocation remain CRITICAL?", "CONFIRM_CRITICAL",
            "The boundary preserves canonical allocation ownership and prevents client-side supplier routing.",
            "Under-classification could omit routing bypass, duplicate allocation, and recovery evidence.",
            "CRITICAL requires fail-closed and applicable recovery/idempotency evidence.", "HIGH",
            tier_options("CRITICAL", "CRITICAL", "HIGH"), ["P2-DEC-007"]),
    cluster(29, "Storefront fulfillment ownership boundary", [36], "RULE_APPLICATION",
            "Should the prohibition on Storefront owning Fulfillment remain CRITICAL?", "CONFIRM_CRITICAL",
            "The boundary prevents the experience layer from initiating or controlling fulfillment state.",
            "Under-classification could omit duplicate fulfillment, ambiguous outcome, and manual-recovery evidence.",
            "CRITICAL requires fail-closed and applicable recovery/idempotency/concurrency evidence.", "HIGH",
            tier_options("CRITICAL", "CRITICAL", "HIGH"), ["P2-DEC-003", "P2-DEC-010"]),
    cluster(30, "Allocation invisibility wording and UX classification", [37], "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "Must the statement be clarified and reclassified before deciding whether its tier is CRITICAL or HIGH?", "ROUTE_TO_REMEDIATION",
            "The wording can mean hiding internal allocation mechanics, but P2-DEC-007 permits controlled read-only provider/brand disclosure; the UX_REQUIREMENT type is also suspect for an architecture boundary.",
            "Tiering the ambiguous word 'invisible' can either suppress required disclosure or weaken allocation-decoupling evidence.",
            "Clarify technical invisibility versus disclosure, then link acceptance to the correct architecture and journey surfaces.", "HIGH", defect_options(), ["P2-DEC-007"]),
    cluster(31, "Presentation/business separation statements typed as UX requirements", [38, 42, 45], "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "Should these ownership/separation statements be reclassified as DESIGN_PRINCIPLE before tiering?", "ROUTE_TO_REMEDIATION",
            "The statements define architecture ownership and presentation separation rather than direct journey outcomes.",
            "An ordinary override may preserve wrong acceptance abstraction and duplicate the same separation contract.",
            "Reclassify/reconcile first; then attach observable UX acceptance only through impacted journeys or runtime contracts.", "HIGH", defect_options()),
    cluster(32, "Storefront identity versus authentication identity", [43], "HUMAN_RISK_DECISION",
            "Does domain-to-storefront identity resolution require CRITICAL tenant-isolation evidence, or HIGH storefront-routing evidence?", "CONFIRM_HIGH",
            "Here 'identity' denotes storefront selection, not an authentication principal; however an incorrect domain binding could cross tenant boundaries.",
            "HIGH may omit cross-tenant fail-closed checks if domain binding is security-enforcing; CRITICAL may conflate brand routing with authentication identity.",
            "HIGH covers expected routing and the primary invalid-domain edge; CRITICAL adds explicit tenant/authorization boundary evidence.", "MEDIUM",
            tier_options("HIGH", "CRITICAL", "HIGH"), ["P2-DEC-001", "P2-DEC-008"]),
]


def run(command: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)


def command_text(command: list[str]) -> str:
    result = run(command)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace"))
    return result.stdout.decode("utf-8")


def validate_source_lineage_and_paths(review: dict) -> list[str]:
    errors = []
    if review.get("source_commit") != SOURCE_COMMIT:
        errors.append("recorded source_commit differs from approved Phase 2A provenance")
    if run(["git", "cat-file", "-e", SOURCE_COMMIT + "^{commit}"]).returncode != 0:
        errors.append("approved Phase 2A source_commit does not exist")
        return errors
    if run(["git", "merge-base", "--is-ancestor", SOURCE_COMMIT, "HEAD"]).returncode != 0:
        errors.append("approved Phase 2A source_commit is not an ancestor of current HEAD")

    committed_paths = set(filter(None, command_text([
        "git", "diff", "--name-only", SOURCE_COMMIT + "..HEAD",
    ]).splitlines()))
    staged_paths = set(filter(None, command_text([
        "git", "diff", "--cached", "--name-only",
    ]).splitlines()))
    unauthorized_paths = sorted((committed_paths | staged_paths) - ALLOWED_PHASE_2B_PATHS)
    if unauthorized_paths:
        errors.append("unauthorized path changed since source_commit: " + ", ".join(unauthorized_paths))
    return errors


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def index_blob(path: Path) -> bytes:
    relative = path.resolve().relative_to(ROOT).as_posix()
    result = run(["git", "show", ":" + relative])
    if result.returncode != 0:
        raise RuntimeError("missing staged Git blob: " + relative)
    return result.stdout


def parse_exception_rows(text: str) -> list[dict]:
    pattern = re.compile(
        r"^\| (P2-CRIT-EXC-[0-9]{3}) \| `([^`]+)` \| `([^`]+)` \| `([^`]+)` \| `([^`]+)` \| (.*?) \| `([^`]+)` \| `([^`]+)` \|$",
        re.MULTILINE,
    )
    rows = []
    for match in pattern.finditer(text):
        rows.append({
            "exception_id": match.group(1),
            "stable_requirement_id": match.group(2),
            "proposed_criticality": match.group(3),
            "requirement_type": match.group(4),
            "matched_rule": match.group(5),
            "exception_triggers": re.findall(r"`([^`]+)`", match.group(6)),
            "source_document": match.group(7),
            "status": match.group(8),
        })
    return rows


def registry_records() -> list[dict]:
    records = []
    for name in ("brd-requirements.json", "uxf-requirements.json"):
        records.extend(load_json(REQUIREMENTS / name)["requirements"])
    return records


def source_context(record: dict) -> str:
    source_lines = record["source_lines"]
    match = re.fullmatch(r"L([0-9]+)(?:-L([0-9]+))?", source_lines)
    if not match:
        raise ValueError("invalid source line range: " + source_lines)
    start = int(match.group(1))
    end = int(match.group(2) or match.group(1))
    blob = command_text(["git", "cat-file", "blob", SOURCE_DOCUMENT_COMMIT + ":" + record["source_document"]])
    return "\n".join(blob.splitlines()[start - 1:end])


def projected_totals(member_tiers: list[str], target: str) -> dict:
    result = dict(CURRENT)
    if target in {"CRITICAL", "HIGH", "NORMAL", "INACTIVE"}:
        for tier in member_tiers:
            result[tier] -= 1
            result["active_denominator"] -= 1
        if target != "INACTIVE":
            result[target] += len(member_tiers)
            result["active_denominator"] += len(member_tiers)
    result["delta"] = {key: result[key] - CURRENT[key] for key in CURRENT}
    return result


def decision_basis(exception_id: str, classification: str) -> str:
    if exception_id in EARLIER_EXPLICIT_DECISION_IDS:
        return "EARLIER_EXPLICIT_HUMAN_DECISION"
    if classification == "HUMAN_RISK_DECISION":
        return "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION"
    if classification == "RULE_APPLICATION":
        return "CRITICALITY_RULE_RECOMMENDATION"
    return "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION"


def decision_provenance(exception_id: str, classification: str) -> dict:
    basis = decision_basis(exception_id, classification)
    if basis == "EARLIER_EXPLICIT_HUMAN_DECISION":
        return {
            "authority": "EXPLICIT_HUMAN_SELECTION",
            "decision_date": "2026-07-14",
            "source_review": SOURCE_REVIEW_ID,
        }
    if basis == "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION":
        return {
            "authority": "CONTROLLED_FAST_TRACK",
            "authorization_date": FAST_TRACK_AUTHORIZATION_DATE,
            "authorization_scope": "ACCEPT_EXISTING_RECOMMENDED_OPTIONS_FOR_REMAINING_EXCEPTIONS",
            "source_review": SOURCE_REVIEW_ID,
        }
    return {
        "authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK",
        "authorization_date": FAST_TRACK_AUTHORIZATION_DATE,
        "source_review": SOURCE_REVIEW_ID,
    }


def provisional_projection(exceptions: list[dict]) -> dict:
    result = {
        "CRITICAL": CURRENT_SOURCE_PROJECTION["CRITICAL"],
        "HIGH": CURRENT_SOURCE_PROJECTION["HIGH"],
        "NORMAL": CURRENT_SOURCE_PROJECTION["NORMAL"],
        "known_tier_denominator": CURRENT_SOURCE_PROJECTION["active_denominator"],
        "provisional_inactive_not_applicable_for_v2_3": CURRENT_SOURCE_PROJECTION["inactive_not_applicable_for_v2_3"],
        "excluded_pending_source_remediation_active_units": 0,
        "final_atomic_denominator": None,
        "final_tier_distribution_claimed": False,
    }
    for record in exceptions:
        current_tier = record["rule_derived_criticality"]
        effective = record["effective_tier_or_remediation_required"]
        if effective == "REMEDIATION_REQUIRED":
            result[current_tier] -= 1
            result["known_tier_denominator"] -= 1
            if record["exception_id"] == "P2-CRIT-EXC-001":
                result["provisional_inactive_not_applicable_for_v2_3"] += 1
            else:
                result["excluded_pending_source_remediation_active_units"] += 1
            continue
        if effective != current_tier:
            result[current_tier] -= 1
            result[effective] += 1
    return result


def reconciliation_impact_register() -> list[dict]:
    return [
        {
            "source_identity": "BRD-UPDATE-01-R010",
            "source_exception_id": "P2-CRIT-EXC-005",
            "impact_kind": "COMPOSITE_PARENT_CHILD_RECONCILIATION",
            "candidate_child_count": 12,
            "canonical_result_count": None,
            "new_stable_ids_allocated": False,
            "numeric_projection_included": False,
            "blocker": "SEMANTIC_NORMALIZATION_OVERLAP_ALIAS_SCOPE_AND_ATOMICITY_RECONCILIATION",
        },
        {
            "source_identity": "BRD-WS-17-R013",
            "source_exception_id": "P2-CRIT-EXC-023",
            "impact_kind": "COMPOSITE_PARENT_CHILD_RECONCILIATION",
            "candidate_child_count": 6,
            "canonical_result_count": None,
            "new_stable_ids_allocated": False,
            "numeric_projection_included": False,
            "blocker": "OVERLAP_RECONCILIATION_AND_PER_CHILD_TYPE_CRITICALITY_ACCEPTANCE_CONTRACTS",
        },
        {
            "source_identity": "BRD-WS-08-R012",
            "source_exception_id": "P2-CRIT-EXC-020",
            "impact_kind": "ACTIVE_DEFERRED_SCOPE_SPLIT",
            "candidate_child_count": None,
            "canonical_result_count": None,
            "new_stable_ids_allocated": False,
            "numeric_projection_included": False,
            "blocker": "SPLIT_ACTIVE_RULE_BASED_BEHAVIOR_FROM_DEFERRED_ML_AND_RECONCILE_IDENTITIES",
        },
    ]


def build_review() -> dict:
    exception_rows = parse_exception_rows(EXCEPTION_REGISTER.read_text(encoding="utf-8"))
    if len(exception_rows) != 46 or any(row["status"] != "OPEN" for row in exception_rows):
        raise ValueError("source exception register is not exactly 46 OPEN records")

    decision_payload = load_json(DECISIONS)
    decision_ids = [item.get("decision_id") for item in decision_payload.get("decisions", [])]
    if decision_ids != EXPECTED_DECISIONS:
        raise ValueError("approved decision payload does not contain P2-DEC-001 through P2-DEC-010")
    if any(item.get("selected_option") != 1 for item in decision_payload["decisions"]):
        raise ValueError("approved decision payload option differs")

    summary = load_json(SUMMARY)
    assignments = [item for item in summary["criticality_preflight"]["assignments"] if item["exception_review_required"]]
    assignment_by_id = {item["stable_requirement_id"]: item for item in assignments}
    records = registry_records()
    record_by_identity = {}
    for record in records:
        if record.get("current_id"):
            record_by_identity[record["current_id"]] = record
        if record.get("temporary_key"):
            record_by_identity[record["temporary_key"]] = record

    cluster_by_exception = {}
    for spec in CLUSTER_SPECS:
        for exception_id in spec["member_exception_ids"]:
            if exception_id in cluster_by_exception:
                raise ValueError("duplicate cluster membership: " + exception_id)
            cluster_by_exception[exception_id] = spec
    expected_ids = {row["exception_id"] for row in exception_rows}
    if set(cluster_by_exception) != expected_ids:
        raise ValueError("cluster membership is not exhaustive")

    row_by_id = {row["exception_id"]: row for row in exception_rows}
    rendered_clusters = []
    for raw_spec in CLUSTER_SPECS:
        spec = copy.deepcopy(raw_spec)
        spec["selected_option"] = spec["recommended_option"]
        spec["review_status"] = "DISPOSITIONED_PENDING_PACK_APPROVAL"
        member_tiers = [row_by_id[exception_id]["proposed_criticality"] for exception_id in spec["member_exception_ids"]]
        for item in spec["options"]:
            item["recommended"] = item["option_id"] == spec["recommended_option"]
            item["selected"] = item["option_id"] == spec["selected_option"]
        if sum(item["recommended"] for item in spec["options"]) != 1:
            raise ValueError("cluster must have exactly one recommendation: " + spec["cluster_id"])
        if sum(item["selected"] for item in spec["options"]) != (1 if spec["selected_option"] else 0):
            raise ValueError("cluster selected option differs: " + spec["cluster_id"])
        spec["member_count"] = len(spec["member_exception_ids"])
        rendered_clusters.append(spec)

    exceptions = []
    for row in exception_rows:
        assignment = assignment_by_id.get(row["stable_requirement_id"])
        if assignment is None:
            raise ValueError("missing criticality assignment: " + row["stable_requirement_id"])
        if assignment["verification_criticality"] != row["proposed_criticality"]:
            raise ValueError("assignment tier differs: " + row["exception_id"])
        record = record_by_identity.get(assignment["registry_identity"])
        if record is None:
            raise ValueError("missing registry identity: " + assignment["registry_identity"])
        spec = cluster_by_exception[row["exception_id"]]
        competing = sorted({item["target"] for item in spec["options"] if item["target"] not in {"KEEP_CURRENT", row["proposed_criticality"]}})
        if spec["finding_classification"] == "CLASSIFICATION_OR_EXTRACTION_DEFECT":
            competing.append("REMEDIATION_REQUIRED")
        option_refs = []
        rendered_spec = next(item for item in rendered_clusters if item["cluster_id"] == spec["cluster_id"])
        selected_choice = next((item for item in rendered_spec["options"] if item["selected"]), None)
        if selected_choice is None or selected_choice["option_id"] != rendered_spec["recommended_option"]:
            raise ValueError("selected disposition does not match recommendation: " + row["exception_id"])
        effective_outcome = (
            "REMEDIATION_REQUIRED"
            if spec["finding_classification"] == "CLASSIFICATION_OR_EXTRACTION_DEFECT"
            else selected_choice["target"]
        )
        if effective_outcome not in {"CRITICAL", "HIGH", "NORMAL", "REMEDIATION_REQUIRED"}:
            raise ValueError("invalid effective outcome: " + row["exception_id"])
        for item in rendered_spec["options"]:
            option_refs.append({
                "option_id": item["option_id"],
                "decision": item["decision"],
                "target": item["target"],
                "recommended": item["recommended"],
                "selected": item["selected"],
            })
        exceptions.append({
            "exception_id": row["exception_id"],
            "requirement_id_or_key": row["stable_requirement_id"],
            "registry_identity": assignment["registry_identity"],
            "source_document": record["source_document"],
            "source_section": record["source_section"],
            "source_lines": record["source_lines"],
            "exact_source_statement": record["statement"],
            "source_excerpt": record["source_excerpt"],
            "canonical_source_context": source_context(record),
            "source_fingerprint": record["source_fingerprint"],
            "requirement_type": record["requirement_type"],
            "scope_status": record["scope_status"],
            "lifecycle_status": record["lifecycle_status"],
            "rule_derived_criticality": assignment["verification_criticality"],
            "competing_or_proposed_criticality": competing,
            "matched_rule": assignment["matched_rule"],
            "all_rule_matches": assignment["all_rule_matches"],
            "exception_trigger": assignment["exception_reasons"],
            "finding_classification": spec["finding_classification"],
            "business_technical_risk_rationale": spec["business_technical_risk_rationale"],
            "consequences_of_under_classification": spec["consequences_of_under_classification"],
            "acceptance_depth_impact": spec["acceptance_depth_impact"],
            "preliminary_recommendation": spec["recommended_option"],
            "confidence": spec["confidence"],
            "review_cluster": spec["cluster_id"],
            "review_status": rendered_spec["review_status"],
            "remediation_contract": spec["remediation_contract"],
            "applicable_approved_decisions": spec["applicable_approved_decisions"],
            "human_decision_options": option_refs,
            "selected_option": rendered_spec["selected_option"],
            "selected_disposition": spec["recommended_option"],
            "decision_basis": decision_basis(row["exception_id"], spec["finding_classification"]),
            "decision_provenance": decision_provenance(row["exception_id"], spec["finding_classification"]),
            "effective_tier_or_remediation_required": effective_outcome,
            "selected_target": selected_choice["target"],
            "source_application_status": "NOT_YET_APPLIED",
            "pack_approval_status": "PENDING",
            "source_resolution_claim": False,
            "status": "OPEN",
        })

    classification_totals = dict(sorted(collections.Counter(item["finding_classification"] for item in exceptions).items()))
    decision_accounting = {
        "source_exception_count": 46,
        "source_open_exception_count": 46,
        "source_resolved_count": 0,
        "dispositioned_exceptions": len(exceptions),
        "undispositioned_exceptions": sum(item["selected_disposition"] is None for item in exceptions),
        "earlier_explicit_human_decisions": sum(item["decision_basis"] == "EARLIER_EXPLICIT_HUMAN_DECISION" for item in exceptions),
        "bulk_authorized_human_risk_decisions": sum(item["decision_basis"] == "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION" for item in exceptions),
        "deterministic_policy_remediation_dispositions": sum(item["decision_basis"] == "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION" for item in exceptions),
        "criticality_rule_dispositions": sum(item["decision_basis"] == "CRITICALITY_RULE_RECOMMENDATION" for item in exceptions),
        "total": len(exceptions),
    }
    selected_outcome_totals = dict(sorted(collections.Counter(
        item["effective_tier_or_remediation_required"] for item in exceptions
    ).items()))
    selected_disposition_totals = dict(sorted(collections.Counter(
        item["selected_disposition"] for item in exceptions
    ).items()))
    provisional = provisional_projection(exceptions)
    reconciliation_impacts = reconciliation_impact_register()
    return {
        "schema_version": "1.0",
        "artifact": "PHASE_2_CRITICALITY_DECISION_CANDIDATE",
        "candidate_id": CANDIDATE_ID,
        "status": "CANDIDATE",
        "approval_status": "PENDING_MARKDOWN_APPROVAL",
        "source_review": SOURCE_REVIEW_ID,
        "source_decision_pack": "V23-P2A-DECISION-PACK-C1",
        "source_commit": SOURCE_COMMIT,
        "accepted_tag": ACCEPTED_TAG,
        "source_registry_candidate": "V23-REQ-REGISTRY-FC2",
        "source_document_commit": SOURCE_DOCUMENT_COMMIT,
        "hash_basis": "GIT_INDEX_BLOB_CONTENT",
        "line_endings": "GIT_CANONICAL_TEXT",
        "exception_count": 46,
        "resolved_count": 0,
        "source_exception_count": 46,
        "source_resolved_count": 0,
        "dispositioned_exception_count": 46,
        "undispositioned_exception_count": 0,
        "next_gate": "HUMAN_CRITICALITY_DECISION_PACK_APPROVAL",
        "fast_track_authorization": {
            "decision": "ACCEPT_EVERY_EXISTING_RECOMMENDED_OPTION_FOR_ALL_40_REMAINING_EXCEPTIONS",
            "authorization_date": FAST_TRACK_AUTHORIZATION_DATE,
            "interpretation_authorized": False,
            "source_edits_authorized": False,
        },
        "candidate_approval_block": {
            "candidate_approval": "PENDING",
            "markdown_approval": "PENDING",
            "approver": "PENDING",
            "approval_date": "PENDING",
            "source_application": "PENDING",
        },
        "decision_accounting": decision_accounting,
        "selected_effective_outcome_totals": selected_outcome_totals,
        "selected_disposition_totals": selected_disposition_totals,
        "current_source_projection": dict(CURRENT_SOURCE_PROJECTION),
        "provisional_decision_adjusted_projection": provisional,
        "projection_qualifier": PROJECTION_QUALIFIER,
        "reconciliation_impact_register": reconciliation_impacts,
        "classification_totals": classification_totals,
        "cluster_count": len(rendered_clusters),
        "correction_record": {
            "superseded_review": SUPERSEDED_REVIEW_ID,
            "reason": "APPROVED_DECISION_PRECEDENCE_OMITTED",
            "affected_exceptions": ["P2-CRIT-EXC-001", "P2-CRIT-EXC-003", "P2-CRIT-EXC-020"],
            "no_source_changes_applied": True,
            "no_exceptions_resolved": True,
        },
        "review_basis": {
            "framework_decisions": ["P2D-05", "P2D-06"],
            "approved_phase_2_decisions": EXPECTED_DECISIONS,
            "scope_decisions": ["SD-02", "SD-03", "BDD-26", "BDD-27"],
            "authority_precedence": [
                "APPROVED_V2.3_HUMAN_AND_FRAMEWORK_DECISIONS",
                "CORRECTED_BRD",
                "ALIGNED_UXF",
                "GENERATED_REGISTRY_AND_REVIEW_PROJECTIONS",
                "LEGACY_SOURCE_LABELS",
            ],
            "legacy_future_labels_cannot_override_approved_scope_promotion": True,
            "risk_semantics_reviewed": [
                "FAIL_CLOSED", "FINANCIAL", "SECURITY", "IDENTITY", "FULFILLMENT",
                "ALLOCATION", "PAYMENT", "PRIVACY", "OPERATIONAL_RECOVERY", "DATA_INTEGRITY",
            ],
        },
        "recommended_review_order": [
            "CLASSIFICATION_OR_EXTRACTION_DEFECT",
            "HUMAN_RISK_DECISION",
            "RULE_APPLICATION",
        ],
        "clusters": rendered_clusters,
        "exceptions": exceptions,
        "related_non_exception_extraction_defects": copy.deepcopy(RELATED_NON_EXCEPTION_EXTRACTION_DEFECTS),
        "invariants": {
            "every_source_exception_open": all(item["status"] == "OPEN" for item in exceptions),
            "exception_ids_unique": len({item["exception_id"] for item in exceptions}) == 46,
            "cluster_membership_exhaustive_and_disjoint": len(cluster_by_exception) == 46,
            "all_46_dispositions_selected": all(item["selected_disposition"] is not None for item in exceptions),
            "every_selection_matches_recommendation": all(item["selected_disposition"] == item["preliminary_recommendation"] for item in exceptions),
            "no_unresolved_review_decisions": all(item["review_status"] == "DISPOSITIONED_PENDING_PACK_APPROVAL" for item in exceptions),
            "no_source_application_claimed": all(item["source_application_status"] == "NOT_YET_APPLIED" and not item["source_resolution_claim"] for item in exceptions),
            "pack_approval_entirely_pending": True,
            "source_projection_unchanged": True,
            "source_and_provisional_projections_separate": CURRENT_SOURCE_PROJECTION != provisional,
            "structural_count_uncertainty_explicit": provisional["final_atomic_denominator"] is None and not provisional["final_tier_distribution_claimed"] and all(not item["numeric_projection_included"] for item in reconciliation_impacts),
            "no_new_stable_ids_allocated": all(not item["new_stable_ids_allocated"] for item in reconciliation_impacts),
            "related_non_exception_defects_do_not_increase_source_exception_count": all(
                not item["source_exception"] and not item["increases_source_exception_count"]
                for item in RELATED_NON_EXCEPTION_EXTRACTION_DEFECTS
            ),
            "approved_scope_promotions_not_routed_inactive": all(
                item["selected_option"] == item["recommended_option"] and all(option_item["target"] != "INACTIVE" for option_item in item["options"])
                for item in rendered_clusters if item["cluster_id"] in {"P2-CRIT-CL-034", "P2-CRIT-CL-035"}
            ),
            "source_exception_register_sha256": hashlib.sha256(EXCEPTION_REGISTER.read_bytes()).hexdigest(),
        },
    }


def render_json(review: dict) -> bytes:
    return (json.dumps(review, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def inline(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_markdown(review: dict) -> bytes:
    lines = [
        "---",
        'schema_version: "1.0"',
        "document_code: V23-PHASE-2-CRITICALITY-DECISION-CANDIDATE",
        "title: Phase 2 Criticality Decision Candidate",
        'product_baseline: "2.3"',
        'document_revision: "0.4"',
        "lifecycle_status: CANDIDATE",
        "language: en",
        "authority: PHASE_2B_CONTROLLED_FAST_TRACK_CANDIDATE",
        f"supersedes: {SOURCE_REVIEW_ID}",
        "requirement_block_schema: null",
        "---",
        "",
        "# Phase 2 Criticality Decision Candidate",
        "",
        "## 1. Candidate identity and source",
        "",
        f"- Candidate ID: `{review['candidate_id']}`.",
        f"- Status: `{review['status']}`.",
        f"- Approval status: `{review['approval_status']}`.",
        f"- Source review: `{review['source_review']}`.",
        f"- Source Decision Pack: `{review['source_decision_pack']}`.",
        f"- Source commit: `{review['source_commit']}`.",
        f"- Accepted tag: `{review['accepted_tag']}`.",
        f"- Hash basis: `{review['hash_basis']}`.",
        f"- Line endings: `{review['line_endings']}`.",
        f"- Next gate: `{review['next_gate']}`.",
        "",
        "The 2026-07-15 CONTROLLED FAST-TRACK authorization selects every existing recommended option for the 40 previously remaining exceptions. It does not authorize new interpretations, source edits, source resolution, stable-ID allocation, approval, commit, push, or tag.",
        "",
        "## 2. Current and provisional projections",
        "",
        "| Projection | CRITICAL | HIGH | NORMAL | Denominator | Inactive N/A |",
        "|---|---:|---:|---:|---:|---:|",
        f"| Current source | {review['current_source_projection']['CRITICAL']} | {review['current_source_projection']['HIGH']} | {review['current_source_projection']['NORMAL']} | {review['current_source_projection']['active_denominator']} | {review['current_source_projection']['inactive_not_applicable_for_v2_3']} |",
        f"| Provisional known-tier subset | {review['provisional_decision_adjusted_projection']['CRITICAL']} | {review['provisional_decision_adjusted_projection']['HIGH']} | {review['provisional_decision_adjusted_projection']['NORMAL']} | {review['provisional_decision_adjusted_projection']['known_tier_denominator']} | {review['provisional_decision_adjusted_projection']['provisional_inactive_not_applicable_for_v2_3']} |",
        "",
        f"Projection qualifier: `{review['projection_qualifier']}`.",
        f"Excluded pending source-remediation active units: `{review['provisional_decision_adjusted_projection']['excluded_pending_source_remediation_active_units']}`. Final atomic denominator: `UNKNOWN`; final tier distribution claimed: `NO`.",
        "",
        "## 3. Decision accounting",
        "",
        f"- Source exceptions: `{review['decision_accounting']['source_exception_count']}`; OPEN: `{review['decision_accounting']['source_open_exception_count']}`; resolved: `{review['decision_accounting']['source_resolved_count']}`.",
        f"- Dispositioned: `{review['decision_accounting']['dispositioned_exceptions']}`; undispositioned: `{review['decision_accounting']['undispositioned_exceptions']}`.",
        f"- Earlier explicit human decisions: `{review['decision_accounting']['earlier_explicit_human_decisions']}`.",
        f"- Bulk-authorized human-risk decisions: `{review['decision_accounting']['bulk_authorized_human_risk_decisions']}`.",
        f"- Deterministic/policy remediation dispositions: `{review['decision_accounting']['deterministic_policy_remediation_dispositions']}`.",
        f"- Criticality-rule dispositions: `{review['decision_accounting']['criticality_rule_dispositions']}`.",
        f"- Total: `{review['decision_accounting']['total']}`.",
        "",
        "### Selected effective outcomes",
        "",
        f"- `CRITICAL`: `{review['selected_effective_outcome_totals']['CRITICAL']}`.",
        f"- `HIGH`: `{review['selected_effective_outcome_totals']['HIGH']}`.",
        f"- `NORMAL`: `{review['selected_effective_outcome_totals']['NORMAL']}`.",
        f"- `REMEDIATION_REQUIRED`: `{review['selected_effective_outcome_totals']['REMEDIATION_REQUIRED']}`.",
        "",
        "### Related non-exception extraction defect",
        "",
    ]
    for defect in review["related_non_exception_extraction_defects"]:
        lines.extend([
            f"- Requirement: `{defect['requirement_id']}` (not a source criticality exception; source exception count remains 46).",
            f"- Existing truncated statement: “{defect['existing_truncated_statement']}”",
            f"- Effective statement candidate: “{defect['effective_statement_candidate']}”",
            f"- Remediation: `{defect['remediation']}` with corrected source coverage `{defect['corrected_source_coverage_candidate']}`.",
            "- Carry forward: later source remediation and validation; no source change is applied by this pack.",
            "",
        ])
    lines.extend([
        "## 4. Structural reconciliation-impact register",
        "",
        "| Source identity | Exception | Impact | Candidate children | Canonical result | IDs allocated | In projection | Blocker |",
        "|---|---|---|---:|---|---|---|---|",
    ])
    for impact in review["reconciliation_impact_register"]:
        lines.append(
            f"| `{impact['source_identity']}` | `{impact['source_exception_id']}` | `{impact['impact_kind']}` | "
            f"{impact['candidate_child_count'] if impact['candidate_child_count'] is not None else 'UNKNOWN'} | "
            f"`{'UNKNOWN' if impact['canonical_result_count'] is None else impact['canonical_result_count']}` | "
            f"`{'YES' if impact['new_stable_ids_allocated'] else 'NO'}` | "
            f"`{'YES' if impact['numeric_projection_included'] else 'NO'}` | `{impact['blocker']}` |"
        )
    lines.extend([
        "",
        "## 5. Candidate approval block",
        "",
    ])
    for key, value in review["candidate_approval_block"].items():
        lines.append(f"- {key.replace('_', ' ').title()}: `{value}`.")
    lines.extend([
        "",
        "## 6. Classification summary",
        "",
        "| Finding classification | Count |",
        "|---|---:|",
    ])
    for classification in sorted(CLASSIFICATIONS):
        lines.append(f"| `{classification}` | {review['classification_totals'][classification]} |")
    lines.extend(["", "## 7. Cluster summary", "", "| Cluster | Classification | Members | Review status | Recommended option | Selected option | Uniform safe |", "|---|---|---:|---|---|---|---|"])
    for item in review["clusters"]:
        selected = item["selected_option"] or "NONE"
        lines.append(f"| `{item['cluster_id']}` | `{item['finding_classification']}` | {item['member_count']} | `{item['review_status']}` | `{item['recommended_option']}` | `{selected}` | `{'YES' if item['uniform_resolution_safe'] else 'NO'}` |")
    lines.extend([
        "",
        "## 8. Disposition clusters",
        "",
    ])
    exception_by_id = {item["exception_id"]: item for item in review["exceptions"]}
    for item in review["clusters"]:
        lines.extend([
            f"### {item['cluster_id']} — {item['title']}",
            "",
            f"- Classification: `{item['finding_classification']}`.",
            f"- Member count: `{item['member_count']}`.",
            "- Members: " + ", ".join(f"`{member}`" for member in item["member_exception_ids"]) + ".",
            f"- Common decision question: {item['common_decision_question']}",
            f"- Uniform resolution safe: `{'YES' if item['uniform_resolution_safe'] else 'NO'}`.",
            f"- Review status: `{item['review_status']}`.",
            "- Approved decision provenance: " + (", ".join(f"`{value}`" for value in item["applicable_approved_decisions"]) if item["applicable_approved_decisions"] else "`NONE_SPECIFIC`") + ".",
            f"- Recommended option: `{item['recommended_option']}`.",
            f"- Recommendation rationale: {item['recommendation_rationale']}",
            f"- Under-classification consequence: {item['consequences_of_under_classification']}",
            f"- Acceptance-depth impact: {item['acceptance_depth_impact']}",
            f"- Confidence: `{item['confidence']}`.",
            f"- Selected option: `{item['selected_option'] or 'NONE'}`.",
            "- Remediation contract: " + ("`" + json.dumps(item["remediation_contract"], ensure_ascii=False, sort_keys=True) + "`" if item["remediation_contract"] is not None else "`NONE`") + ".",
            "",
        ])
        contract = item["remediation_contract"] or {}
        if contract.get("effective_statement_candidate"):
            lines.extend([
                f"- Effective statement candidate: “{contract['effective_statement_candidate']}”",
                f"- Corrected source coverage candidate: `{contract['corrected_source_coverage_candidate']}` (event-family subjects plus predicate).",
                "- Criticality finalized: `NO`; re-evaluation is required after source remediation.",
                "",
            ])
        if contract.get("child_candidates"):
            lines.extend([
                "#### Pending child reconciliation contract",
                "",
                f"- Composite parent candidate: `YES`; parent stable ID: `{contract['preserve_parent_stable_id']}`.",
                "- Parent units: implementation `NO`; acceptance `NO`; scope coverage `NO`; criticality `NO`.",
                f"- Structural count impact: `{contract['structural_count_impact']}`; child ID allocation: `{contract['child_id_allocation']}`.",
            ])
            if contract.get("parent_to_child_coverage_semantics"):
                lines.append(f"- Parent-to-child coverage semantics: `{contract['parent_to_child_coverage_semantics']}`.")
            if contract.get("explanatory_non_requirement_sentence"):
                lines.append(f"- Explanatory only, not another requirement: “{contract['explanatory_non_requirement_sentence']}”")
            lines.extend(["", "Atomic child candidates:", ""])
            for number, child in enumerate(contract["child_candidates"], start=1):
                lines.append(f"{number}. {child['candidate_name']}")
                if child.get("explanatory_source_sentence"):
                    lines.append(f"   - Explanatory source sentence: “{child['explanatory_source_sentence']}”")
                if child.get("non_inference_guard"):
                    lines.append(f"   - Non-inference guard: `{child['non_inference_guard']}`.")
            lines.append("")
        lines.extend([
            "| Option | Decision | Target | Recommended | Selected |",
            "|---|---|---|---|---|",
        ])
        for choice in item["options"]:
            lines.append(
                f"| `{choice['option_id']}` | `{choice['decision']}` | `{choice['target']}` | `{'YES' if choice['recommended'] else 'NO'}` | `{'YES' if choice['selected'] else 'NO'}` |"
            )
        lines.extend(["", "#### Member records", ""])
        for exception_id in item["member_exception_ids"]:
            record = exception_by_id[exception_id]
            lines.extend([
                f"##### {record['exception_id']} — {record['requirement_id_or_key']}",
                "",
                f"- Source: `{record['source_document']}`, `{record['source_section']}`, `{record['source_lines']}`.",
                f"- Type/scope: `{record['requirement_type']}` / `{record['scope_status']}`.",
                f"- Rule-derived criticality: `{record['rule_derived_criticality']}` via `{record['matched_rule']}`.",
                "- Exception trigger: " + ", ".join(f"`{value}`" for value in record["exception_trigger"]) + ".",
                f"- Preliminary recommendation: `{record['preliminary_recommendation']}`; confidence `{record['confidence']}`.",
                f"- Review status: `{record['review_status']}`.",
                f"- Risk rationale: {record['business_technical_risk_rationale']}",
                f"- Consequence of under-classification: {record['consequences_of_under_classification']}",
                f"- Acceptance-depth impact: {record['acceptance_depth_impact']}",
                "- Human options: " + ", ".join(f"`{value['option_id']}`" for value in record["human_decision_options"]) + ".",
                f"- Selected disposition: `{record['selected_disposition']}` (matches recommendation: `YES`).",
                f"- Decision basis: `{record['decision_basis']}`.",
                f"- Provenance: `{json.dumps(record['decision_provenance'], ensure_ascii=False, sort_keys=True)}`.",
                f"- Effective tier/remediation: `{record['effective_tier_or_remediation_required']}`.",
                f"- Source application: `{record['source_application_status']}`; pack approval: `{record['pack_approval_status']}`.",
                f"- Source-exception status: `OPEN`; source-resolution claim: `NO`.",
                "",
                "Exact source statement:",
                "",
                "```text",
                record["exact_source_statement"],
                "```",
                "",
                "Canonical source context:",
                "",
                "```text",
                record["canonical_source_context"],
                "```",
                "",
            ])
    lines.extend([
        "## 9. Complete disposition index",
        "",
        "| Exception | Requirement | Classification | Current | Selected disposition | Effective outcome | Basis | Source application | Source status |",
        "|---|---|---|---|---|---|---|---|---|",
    ])
    for record in review["exceptions"]:
        competing = ", ".join(record["competing_or_proposed_criticality"]) or "NONE"
        lines.append(
            f"| `{record['exception_id']}` | `{record['requirement_id_or_key']}` | `{record['finding_classification']}` | "
            f"`{record['rule_derived_criticality']}` | `{record['selected_disposition']}` | `{record['effective_tier_or_remediation_required']}` | "
            f"`{record['decision_basis']}` | `{record['source_application_status']}` | `OPEN` |"
        )
    lines.extend([
        "",
        "## 10. Candidate state",
        "",
        "- All 46 exceptions remain `OPEN`.",
        "- Resolved exceptions: `0`.",
        "- Dispositioned exceptions: `46`; undispositioned exceptions: `0`.",
        "- Every selected disposition exactly matches its recorded recommendation.",
        "- Source application status for every exception: `NOT_YET_APPLIED`.",
        f"- Projection qualifier: `{review['projection_qualifier']}`.",
        "- Candidate approval block: entirely `PENDING`.",
        "- No source criticality, scope, statement, stable ID, or resolution status has been modified.",
        f"- Next gate: `{review['next_gate']}`.",
        "",
    ])
    return "\n".join(lines).encode("utf-8")


def _validate_r2_review_legacy(review: dict) -> list[str]:
    errors = []
    expected_identity = {
        "review_id": REVIEW_ID,
        "status": "HUMAN_REVIEW_REQUIRED",
        "approval_status": "NOT_APPLICABLE_REVIEW_ONLY",
        "source_decision_pack": "V23-P2A-DECISION-PACK-C1",
        "source_commit": SOURCE_COMMIT,
        "exception_count": 46,
        "resolved_count": 0,
        "source_exception_count": 46,
        "source_resolved_count": 0,
        "reviewed_exception_count": 6,
        "human_decisions_selected": 2,
        "deterministic_remediation_findings_accepted": 4,
        "exceptions_still_requiring_review": 40,
        "selected_options_among_remaining_unreviewed": 0,
        "final_pack_approval": "PENDING",
        "selected_decision_count": 2,
        "next_gate": "HUMAN_CRITICALITY_EXCEPTION_REVIEW",
    }
    for key, value in expected_identity.items():
        if review.get(key) != value:
            errors.append("review identity/state differs: " + key)
    if "current_projection" in review:
        errors.append("legacy conflated current_projection field is prohibited")
    if review.get("current_source_projection") != CURRENT_SOURCE_PROJECTION:
        errors.append("current source projection differs")
    if review.get("decision_adjusted_candidate_projection") != DECISION_ADJUSTED_CANDIDATE_PROJECTION:
        errors.append("decision-adjusted candidate projection differs")
    if review.get("projection_qualifier") != PROJECTION_QUALIFIER:
        errors.append("numeric projection qualifier differs")
    if review.get("cluster_count") != 34:
        errors.append("corrected cluster count is not 34")
    if review.get("classification_totals") != {
        "CLASSIFICATION_OR_EXTRACTION_DEFECT": 18,
        "HUMAN_RISK_DECISION": 11,
        "RULE_APPLICATION": 17,
    }:
        errors.append("classification totals differ")
    if review.get("correction_record") != {
        "superseded_review": SUPERSEDED_REVIEW_ID,
        "reason": "APPROVED_DECISION_PRECEDENCE_OMITTED",
        "affected_exceptions": ["P2-CRIT-EXC-001", "P2-CRIT-EXC-003", "P2-CRIT-EXC-020"],
        "no_source_changes_applied": True,
        "no_exceptions_resolved": True,
    }:
        errors.append("R2 correction record differs")
    exceptions = review.get("exceptions", [])
    clusters = review.get("clusters", [])
    if len(exceptions) != 46 or len({item.get("exception_id") for item in exceptions}) != 46:
        errors.append("review exception IDs are not exactly 46 unique values")
    if any(item.get("status") != "OPEN" for item in exceptions):
        errors.append("an exception is not OPEN")
    selected_exceptions = [item for item in exceptions if item.get("selected_option") is not None]
    selected_clusters = [item for item in clusters if item.get("selected_option") is not None]
    if [(item.get("exception_id"), item.get("selected_option")) for item in selected_exceptions] != [
        ("P2-CRIT-EXC-001", "ROUTE_TO_SCOPE_REMEDIATION"),
        ("P2-CRIT-EXC-005", "COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION"),
    ]:
        errors.append("exactly the Product Variant and Business Principles human options must be selected")
    if [(item.get("cluster_id"), item.get("selected_option")) for item in selected_clusters] != [
        ("P2-CRIT-CL-033", "ROUTE_TO_SCOPE_REMEDIATION"),
        ("P2-CRIT-CL-003", "COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION"),
    ]:
        errors.append("exactly the Product Variant and Business Principles cluster options must be selected")
    memberships = [member for item in clusters for member in item.get("member_exception_ids", [])]
    if collections.Counter(memberships) != collections.Counter(item.get("exception_id") for item in exceptions):
        errors.append("cluster membership is not exhaustive and disjoint")
    if any(item.get("finding_classification") not in CLASSIFICATIONS for item in exceptions + clusters):
        errors.append("invalid finding classification")
    if sum(review.get("classification_totals", {}).values()) != 46:
        errors.append("classification totals do not sum to 46")
    exception_by_id = {item.get("exception_id"): item for item in exceptions}
    cluster_by_id = {item.get("cluster_id"): item for item in clusters}
    expected_corrected_membership = {
        "P2-CRIT-CL-033": ["P2-CRIT-EXC-001"],
        "P2-CRIT-CL-034": ["P2-CRIT-EXC-003"],
        "P2-CRIT-CL-035": ["P2-CRIT-EXC-020"],
        "P2-CRIT-CL-002": ["P2-CRIT-EXC-004"],
        "P2-CRIT-CL-003": ["P2-CRIT-EXC-005"],
        "P2-CRIT-CL-004": ["P2-CRIT-EXC-023"],
    }
    for cluster_id, members in expected_corrected_membership.items():
        if cluster_by_id.get(cluster_id, {}).get("member_exception_ids") != members:
            errors.append("corrected cluster membership differs: " + cluster_id)
    product_variant = exception_by_id.get("P2-CRIT-EXC-001", {})
    if product_variant.get("review_status") != "DECIDED_PENDING_REVIEW_PACK_APPROVAL":
        errors.append("Product Variant decision status differs")
    product_contract = product_variant.get("remediation_contract") or {}
    if product_contract.get("target_scope") != "FUTURE_OR_EQUIVALENT_INACTIVE_V2_3" or product_contract.get("acceptance_applicability") != "NOT_APPLICABLE_FOR_V2.3" or product_contract.get("verification_criticality") is not None:
        errors.append("Product Variant inactive remediation contract differs")
    approval_engine = exception_by_id.get("P2-CRIT-EXC-003", {})
    approval_cluster = cluster_by_id.get("P2-CRIT-CL-034", {})
    if approval_engine.get("review_status") != "DETERMINISTIC_REMEDIATION_IDENTIFIED" or approval_engine.get("remediation_contract", {}).get("target_scope") != "V2.3_ACTIVE":
        errors.append("Shared Approval Engine deterministic remediation differs")
    if approval_cluster.get("recommended_option") != "APPROVED_SCOPE_PROMOTION_REMEDIATION" or any(item.get("target") == "INACTIVE" for item in approval_cluster.get("options", [])):
        errors.append("Shared Approval Engine was recommended inactive despite SD-03/BDD-27")
    fraud_engine = exception_by_id.get("P2-CRIT-EXC-020", {})
    fraud_cluster = cluster_by_id.get("P2-CRIT-CL-035", {})
    fraud_contract = fraud_engine.get("remediation_contract") or {}
    if fraud_engine.get("review_status") != "DETERMINISTIC_REMEDIATION_IDENTIFIED" or fraud_contract.get("target_scope") != "V2.3_ACTIVE_RULE_BASED" or fraud_contract.get("deferred_scope") != "ML_AND_ADVANCED_SCORING_POST_V2.3":
        errors.append("Fraud/Risk active-rule/deferred-ML remediation differs")
    if fraud_cluster.get("recommended_option") != "APPROVED_SCOPE_PROMOTION_REMEDIATION" or any(item.get("target") == "INACTIVE" for item in fraud_cluster.get("options", [])):
        errors.append("Fraud/Risk Engine was wholly recommended inactive despite SD-03")

    event_r002 = exception_by_id.get("P2-CRIT-EXC-004", {})
    event_r002_contract = event_r002.get("remediation_contract") or {}
    event_r002_statement = event_r002_contract.get("effective_statement_candidate", "")
    if event_r002.get("review_status") != "DETERMINISTIC_REMEDIATION_IDENTIFIED":
        errors.append("Event Ordering R002 deterministic remediation status differs")
    if event_r002.get("requirement_type") != "DESIGN_PRINCIPLE" or event_r002.get("scope_status") != "V2.3_ACTIVE":
        errors.append("Event Ordering R002 type or scope differs")
    if event_r002_contract.get("remediation") != "EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT" or event_r002_contract.get("preserve_stable_id") != "BRD-EVENT-INDEX-R002":
        errors.append("Event Ordering R002 remediation route or stable ID differs")
    if event_r002_contract.get("corrected_source_coverage_candidate") != "L201-L205" or not event_r002_contract.get("source_coverage_includes_event_family_subjects_and_predicate"):
        errors.append("Event Ordering R002 corrected source coverage differs")
    if event_r002_contract.get("criticality_finalized") is not False or not event_r002_contract.get("criticality_re_evaluation_required"):
        errors.append("Event Ordering R002 criticality was finalized prematurely")
    if not all(subject in event_r002_statement for subject in ("Marketing", "Analytics", "Notification")):
        errors.append("Event Ordering R002 effective statement lacks event-family subjects")

    related_defects = review.get("related_non_exception_extraction_defects", [])
    if len(related_defects) != 1 or related_defects[0].get("requirement_id") != "BRD-EVENT-INDEX-R001":
        errors.append("related R001 extraction defect record differs")
    else:
        event_r001 = related_defects[0]
        event_r001_statement = event_r001.get("effective_statement_candidate", "")
        if not all(subject in event_r001_statement for subject in ("Payment", "Settlement", "Financial")):
            errors.append("Event Ordering R001 effective statement lacks event-family subjects")
        if event_r001.get("preserve_stable_id") != "BRD-EVENT-INDEX-R001" or event_r001.get("existing_truncated_statement") != "phải đảm bảo thứ tự xử lý." or event_r001.get("remediation") != "EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT" or event_r001.get("corrected_source_coverage_candidate") != "L193-L197":
            errors.append("related R001 extraction remediation contract differs")
        if event_r001.get("source_exception") is not False or event_r001.get("increases_source_exception_count") is not False or not event_r001.get("carry_into_later_source_remediation_and_validation"):
            errors.append("related R001 defect was counted as a source exception or not carried forward")

    composite_unit_flags = ("implementation_unit", "acceptance_unit", "scope_coverage_unit", "criticality_unit")
    business_principles = exception_by_id.get("P2-CRIT-EXC-005", {})
    business_contract = business_principles.get("remediation_contract") or {}
    business_children = business_contract.get("child_candidates", [])
    if business_principles.get("review_status") != "DECIDED_PENDING_REVIEW_PACK_APPROVAL" or business_contract.get("decision") != "COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION":
        errors.append("Business Principles modeling decision differs")
    if not business_contract.get("composite_parent_candidate") or business_contract.get("preserve_parent_stable_id") != "BRD-UPDATE-01-R010":
        errors.append("Business Principles parent identity/model differs")
    if any(business_contract.get(flag) is not False for flag in composite_unit_flags):
        errors.append("Business Principles composite parent carries a prohibited unit flag")
    if [item.get("candidate_name") for item in business_children] != BUSINESS_PRINCIPLE_NAMES:
        errors.append("Business Principles must have exactly twelve named child candidates")
    business_model_child = next((item for item in business_children if item.get("candidate_name") == "Business Model First"), {})
    if business_model_child.get("explanatory_source_sentence") != BUSINESS_MODEL_EXPLANATION:
        errors.append("Business Model First explanatory source sentence differs")
    ai_ready_child = next((item for item in business_children if item.get("candidate_name") == "AI Ready"), {})
    if ai_ready_child.get("non_inference_guard") != "MUST_NOT_BE_INTERPRETED_AS_AN_ACTIVE_AI_PRODUCT_FEATURE_WITHOUT_AN_APPROVED_REQUIREMENT":
        errors.append("AI Ready non-inference guard differs")
    if business_contract.get("structural_count_impact") != "PENDING_CHILD_RECONCILIATION" or business_contract.get("projected_count_changes_applied") is not False or not business_contract.get("do_not_blindly_create_twelve_requirements"):
        errors.append("Business Principles structural count/reconciliation rule differs")
    if business_contract.get("source_coverage_candidate") != "L629-L644" or business_contract.get("criticality_assignment_target") != "RESULTING_CANONICAL_ATOMIC_CHILDREN_ONLY":
        errors.append("Business Principles source coverage or child criticality target differs")

    operations = exception_by_id.get("P2-CRIT-EXC-023", {})
    operations_contract = operations.get("remediation_contract") or {}
    operations_children = operations_contract.get("child_candidates", [])
    if operations.get("review_status") != "DETERMINISTIC_REMEDIATION_IDENTIFIED" or operations_contract.get("decision") != "COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN":
        errors.append("Enterprise Operations deterministic remediation differs")
    if not operations_contract.get("composite_parent_candidate") or operations_contract.get("preserve_parent_stable_id") != "BRD-WS-17-R013":
        errors.append("Enterprise Operations parent identity/model differs")
    if any(operations_contract.get(flag) is not False for flag in composite_unit_flags):
        errors.append("Enterprise Operations composite parent carries a prohibited unit flag")
    if [item.get("candidate_name") for item in operations_children] != OPERATIONS_CHILD_STATEMENTS:
        errors.append("Enterprise Operations must have exactly six atomic child candidates")
    if operations_contract.get("structural_count_impact") != "PENDING_CHILD_RECONCILIATION" or operations_contract.get("projected_count_changes_applied") is not False or operations_contract.get("parent_to_child_coverage_semantics") != "ALL_CHILDREN":
        errors.append("Enterprise Operations structural count or ALL_CHILDREN semantics differs")
    if operations_contract.get("source_coverage_candidate") != "L798-L810" or operations_contract.get("child_contract_assignment") != "EACH_CHILD_RECEIVES_OWN_TYPE_CRITICALITY_AND_ACCEPTANCE_CONTRACT":
        errors.append("Enterprise Operations source coverage or child contract assignment differs")
    if operations_contract.get("explanatory_sentence_becomes_requirement") is not False or operations_contract.get("explanatory_non_requirement_sentence") != "Đây là nguyên lý cốt lõi của Enterprise Operations Foundation.":
        errors.append("Enterprise Operations explanatory sentence became a requirement")

    all_children = business_children + operations_children
    if any(item.get("candidate_id") is not None for item in all_children):
        errors.append("a child ID was allocated before reconciliation")
    if any(not all(item.get(flag) is True for flag in (
        "semantic_normalization_required", "overlap_alias_check_required",
        "scope_confirmation_required", "atomicity_review_required",
    )) for item in all_children):
        errors.append("a child candidate lacks a required reconciliation gate")
    for cluster_id in ("P2-CRIT-CL-003", "P2-CRIT-CL-004"):
        for projected_option in cluster_by_id.get(cluster_id, {}).get("options", []):
            projected = projected_option.get("projected_totals", {})
            if any(projected.get(key) != value for key, value in CURRENT.items()) or any(projected.get("delta", {}).get(key) != 0 for key in CURRENT):
                errors.append("pending child reconciliation changed a numeric projection: " + cluster_id)

    reviewed_ids = {"P2-CRIT-EXC-001", "P2-CRIT-EXC-003", "P2-CRIT-EXC-004", "P2-CRIT-EXC-005", "P2-CRIT-EXC-020", "P2-CRIT-EXC-023"}
    reviewed = [item for item in exceptions if item.get("review_status") != "OPEN"]
    if len(reviewed) != 6 or {item.get("exception_id") for item in reviewed} != reviewed_ids:
        errors.append("reviewed exception set is not exactly the approved six")
    remaining = [item for item in exceptions if item.get("exception_id") not in reviewed_ids]
    if len(remaining) != 40 or any(item.get("review_status") != "OPEN" or item.get("selected_option") is not None for item in remaining):
        errors.append("one of the remaining 40 exceptions is reviewed or has a selected option")
    if not all(review.get("invariants", {}).get(key) for key in (
        "every_source_exception_open", "exception_ids_unique",
        "cluster_membership_exhaustive_and_disjoint", "exactly_two_human_options_selected",
        "remaining_40_exceptions_have_no_selected_option", "source_projection_unchanged",
        "source_and_decision_adjusted_projections_separate",
        "numeric_projections_exclude_pending_child_reconciliation",
        "related_non_exception_defects_do_not_increase_source_exception_count",
        "approved_scope_promotions_not_routed_inactive",
    )):
        errors.append("review invariant differs")
    framework_text = FRAMEWORK.read_text(encoding="utf-8")
    for required_framework_text in (
        "### SD-03 — Các ngoại lệ được đưa vào v2.3",
        "Rule-based Fraud/Risk Engine cho login, checkout và payment; ML để sau.",
        "Shared Approval Engine dùng chung cho các nghiệp vụ cần phê duyệt.",
        "### BDD-26 — Fraud/Risk Engine",
        "ML scoring là `POST_V2.3`.",
        "### BDD-27 — Shared Approval Engine",
        "Đây không phải general-purpose BPM",
    ):
        if required_framework_text not in framework_text:
            errors.append("approved scope-decision anchor missing: " + required_framework_text)
    return errors


def validate_review(review: dict) -> list[str]:
    errors = []
    expected_identity = {
        "candidate_id": CANDIDATE_ID,
        "status": "CANDIDATE",
        "approval_status": "PENDING_MARKDOWN_APPROVAL",
        "source_review": SOURCE_REVIEW_ID,
        "source_decision_pack": "V23-P2A-DECISION-PACK-C1",
        "source_commit": SOURCE_COMMIT,
        "hash_basis": "GIT_INDEX_BLOB_CONTENT",
        "line_endings": "GIT_CANONICAL_TEXT",
        "source_exception_count": 46,
        "source_resolved_count": 0,
        "dispositioned_exception_count": 46,
        "undispositioned_exception_count": 0,
        "next_gate": "HUMAN_CRITICALITY_DECISION_PACK_APPROVAL",
    }
    for key, value in expected_identity.items():
        if review.get(key) != value:
            errors.append("candidate identity/state differs: " + key)
    if any(key in review for key in ("current_projection", "decision_adjusted_candidate_projection")):
        errors.append("legacy or conflated projection field is prohibited")
    if review.get("current_source_projection") != CURRENT_SOURCE_PROJECTION:
        errors.append("current source projection differs")
    expected_provisional = {
        "CRITICAL": 312,
        "HIGH": 389,
        "NORMAL": 351,
        "known_tier_denominator": 1052,
        "provisional_inactive_not_applicable_for_v2_3": 107,
        "excluded_pending_source_remediation_active_units": 17,
        "final_atomic_denominator": None,
        "final_tier_distribution_claimed": False,
    }
    if review.get("provisional_decision_adjusted_projection") != expected_provisional:
        errors.append("provisional decision-adjusted projection differs")
    if review.get("projection_qualifier") != PROJECTION_QUALIFIER:
        errors.append("provisional projection qualifier differs")
    expected_accounting = {
        "source_exception_count": 46,
        "source_open_exception_count": 46,
        "source_resolved_count": 0,
        "dispositioned_exceptions": 46,
        "undispositioned_exceptions": 0,
        "earlier_explicit_human_decisions": 2,
        "bulk_authorized_human_risk_decisions": 11,
        "deterministic_policy_remediation_dispositions": 16,
        "criticality_rule_dispositions": 17,
        "total": 46,
    }
    if review.get("decision_accounting") != expected_accounting:
        errors.append("decision accounting differs")
    if review.get("selected_effective_outcome_totals") != {
        "CRITICAL": 13, "HIGH": 12, "NORMAL": 3, "REMEDIATION_REQUIRED": 18,
    }:
        errors.append("selected effective outcome totals differ")
    if review.get("selected_disposition_totals") != {
        "APPROVED_SCOPE_PROMOTION_REMEDIATION": 2,
        "COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN": 1,
        "COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION": 1,
        "CONFIRM_CRITICAL": 13,
        "CONFIRM_HIGH": 12,
        "CONFIRM_NORMAL": 3,
        "EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT": 1,
        "ROUTE_TO_REMEDIATION": 12,
        "ROUTE_TO_SCOPE_REMEDIATION": 1,
    }:
        errors.append("selected disposition totals by recommendation differ")

    exceptions = review.get("exceptions", [])
    clusters = review.get("clusters", [])
    if len(exceptions) != 46 or len({item.get("exception_id") for item in exceptions}) != 46:
        errors.append("candidate does not contain exactly 46 unique exceptions")
    if len(clusters) != 34 or len({item.get("cluster_id") for item in clusters}) != 34:
        errors.append("candidate does not contain exactly 34 unique clusters")
    memberships = [member for item in clusters for member in item.get("member_exception_ids", [])]
    if collections.Counter(memberships) != collections.Counter(item.get("exception_id") for item in exceptions):
        errors.append("cluster membership is not exhaustive and disjoint")
    if any(item.get("status") != "OPEN" for item in exceptions):
        errors.append("a source exception is not OPEN")
    if any(item.get("selected_disposition") is None or item.get("selected_option") is None for item in exceptions):
        errors.append("an exception lacks a selected disposition")
    if any(item.get("selected_disposition") != item.get("preliminary_recommendation") or item.get("selected_option") != item.get("preliminary_recommendation") for item in exceptions):
        errors.append("a selection differs from its recorded recommendation")
    if any(item.get("review_status") != "DISPOSITIONED_PENDING_PACK_APPROVAL" for item in exceptions):
        errors.append("an exception review decision remains unresolved")
    if any(item.get("source_application_status") != "NOT_YET_APPLIED" or item.get("pack_approval_status") != "PENDING" or item.get("source_resolution_claim") is not False for item in exceptions):
        errors.append("source application, pack approval, or source-resolution state differs")
    if any(item.get("selected_option") != item.get("recommended_option") or item.get("review_status") != "DISPOSITIONED_PENDING_PACK_APPROVAL" for item in clusters):
        errors.append("a cluster selection differs from its recommendation or remains unresolved")

    exception_by_id = {item.get("exception_id"): item for item in exceptions}
    for item in exceptions:
        classification = item.get("finding_classification")
        effective = item.get("effective_tier_or_remediation_required")
        if classification == "CLASSIFICATION_OR_EXTRACTION_DEFECT":
            if effective != "REMEDIATION_REQUIRED":
                errors.append("a remediation finding carries a false final-tier claim: " + str(item.get("exception_id")))
        elif effective != item.get("selected_target") or effective not in {"CRITICAL", "HIGH", "NORMAL"}:
            errors.append("a tier disposition has an invalid effective tier: " + str(item.get("exception_id")))
    product_variant = exception_by_id.get("P2-CRIT-EXC-001", {})
    business_principles = exception_by_id.get("P2-CRIT-EXC-005", {})
    if product_variant.get("selected_disposition") != "ROUTE_TO_SCOPE_REMEDIATION" or product_variant.get("selected_target") != "INACTIVE":
        errors.append("Product Variant explicit decision differs")
    if business_principles.get("selected_disposition") != "COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION":
        errors.append("Business Principles explicit decision differs")
    explicit_ids = {item.get("exception_id") for item in exceptions if item.get("decision_basis") == "EARLIER_EXPLICIT_HUMAN_DECISION"}
    if explicit_ids != EARLIER_EXPLICIT_DECISION_IDS:
        errors.append("earlier explicit human decision set differs")
    bulk_human = [item for item in exceptions if item.get("decision_basis") == "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION"]
    if len(bulk_human) != 11 or any(item.get("finding_classification") != "HUMAN_RISK_DECISION" or item.get("decision_provenance", {}).get("authorization_date") != FAST_TRACK_AUTHORIZATION_DATE for item in bulk_human):
        errors.append("bulk-authorized human-risk decision set or provenance differs")

    business_contract = business_principles.get("remediation_contract") or {}
    operations_contract = (exception_by_id.get("P2-CRIT-EXC-023", {}).get("remediation_contract") or {})
    business_children = business_contract.get("child_candidates", [])
    operations_children = operations_contract.get("child_candidates", [])
    if [item.get("candidate_name") for item in business_children] != BUSINESS_PRINCIPLE_NAMES:
        errors.append("Business Principles child candidates differ")
    if [item.get("candidate_name") for item in operations_children] != OPERATIONS_CHILD_STATEMENTS:
        errors.append("Enterprise Operations child candidates differ")
    if next((item for item in business_children if item.get("candidate_name") == "Business Model First"), {}).get("explanatory_source_sentence") != BUSINESS_MODEL_EXPLANATION:
        errors.append("Business Model First explanatory sentence differs")
    if "WITHOUT_AN_APPROVED_REQUIREMENT" not in next((item for item in business_children if item.get("candidate_name") == "AI Ready"), {}).get("non_inference_guard", ""):
        errors.append("AI Ready non-inference guard differs")
    if operations_contract.get("parent_to_child_coverage_semantics") != "ALL_CHILDREN":
        errors.append("Enterprise Operations ALL_CHILDREN semantics differs")
    all_child_candidates = business_children + operations_children
    if any(item.get("candidate_id") is not None for item in all_child_candidates):
        errors.append("a new child stable ID was allocated")

    impacts = review.get("reconciliation_impact_register", [])
    if [(item.get("source_identity"), item.get("impact_kind")) for item in impacts] != [
        ("BRD-UPDATE-01-R010", "COMPOSITE_PARENT_CHILD_RECONCILIATION"),
        ("BRD-WS-17-R013", "COMPOSITE_PARENT_CHILD_RECONCILIATION"),
        ("BRD-WS-08-R012", "ACTIVE_DEFERRED_SCOPE_SPLIT"),
    ]:
        errors.append("structural reconciliation-impact register differs")
    if any(item.get("canonical_result_count") is not None or item.get("new_stable_ids_allocated") is not False or item.get("numeric_projection_included") is not False or not item.get("blocker") for item in impacts):
        errors.append("structural count uncertainty or ID/projection exclusion differs")

    approval_block = review.get("candidate_approval_block", {})
    if set(approval_block) != {"candidate_approval", "markdown_approval", "approver", "approval_date", "source_application"} or any(value != "PENDING" for value in approval_block.values()):
        errors.append("candidate approval block is incomplete or not entirely PENDING")
    authorization = review.get("fast_track_authorization", {})
    if authorization.get("authorization_date") != FAST_TRACK_AUTHORIZATION_DATE or authorization.get("interpretation_authorized") is not False or authorization.get("source_edits_authorized") is not False:
        errors.append("CONTROLLED FAST-TRACK authorization boundary differs")

    cluster_by_id = {item.get("cluster_id"): item for item in clusters}
    for cluster_id in ("P2-CRIT-CL-034", "P2-CRIT-CL-035"):
        cluster_item = cluster_by_id.get(cluster_id, {})
        if cluster_item.get("selected_option") != "APPROVED_SCOPE_PROMOTION_REMEDIATION" or any(option_item.get("target") == "INACTIVE" for option_item in cluster_item.get("options", [])):
            errors.append("approved scope-promotion precedence differs: " + cluster_id)
    framework_text = FRAMEWORK.read_text(encoding="utf-8")
    for required_framework_text in (
        "### SD-03 — Các ngoại lệ được đưa vào v2.3",
        "Rule-based Fraud/Risk Engine cho login, checkout và payment; ML để sau.",
        "Shared Approval Engine dùng chung cho các nghiệp vụ cần phê duyệt.",
        "### BDD-26 — Fraud/Risk Engine",
        "ML scoring là `POST_V2.3`.",
        "### BDD-27 — Shared Approval Engine",
        "Đây không phải general-purpose BPM",
    ):
        if required_framework_text not in framework_text:
            errors.append("approved decision precedence anchor missing: " + required_framework_text)

    source_rows = parse_exception_rows(EXCEPTION_REGISTER.read_text(encoding="utf-8"))
    if len(source_rows) != 46 or any(item.get("status") != "OPEN" for item in source_rows):
        errors.append("source exception register is not exactly 46 OPEN entries")
    related = review.get("related_non_exception_extraction_defects", [])
    if len(related) != 1 or related[0].get("requirement_id") != "BRD-EVENT-INDEX-R001" or related[0].get("source_exception") is not False:
        errors.append("related R001 non-exception extraction defect differs")
    required_invariants = (
        "every_source_exception_open", "exception_ids_unique", "cluster_membership_exhaustive_and_disjoint",
        "all_46_dispositions_selected", "every_selection_matches_recommendation", "no_unresolved_review_decisions",
        "no_source_application_claimed", "pack_approval_entirely_pending", "source_projection_unchanged",
        "source_and_provisional_projections_separate", "structural_count_uncertainty_explicit",
        "no_new_stable_ids_allocated", "related_non_exception_defects_do_not_increase_source_exception_count",
        "approved_scope_promotions_not_routed_inactive",
    )
    if not all(review.get("invariants", {}).get(key) is True for key in required_invariants):
        errors.append("a required candidate invariant differs")
    return errors


def emit(directory: Path) -> int:
    review_a = build_review()
    review_b = build_review()
    errors = validate_review(review_a)
    if errors:
        raise RuntimeError("; ".join(errors))
    json_a, json_b = render_json(review_a), render_json(review_b)
    markdown_a, markdown_b = render_markdown(review_a), render_markdown(review_b)
    if json_a != json_b or markdown_a != markdown_b:
        raise RuntimeError("non-deterministic review rendering")
    directory.mkdir(parents=True, exist_ok=True)
    (directory / REVIEW_JSON.name).write_bytes(json_a)
    (directory / REVIEW_MD.name).write_bytes(markdown_a)
    print(hashlib.sha256(markdown_a).hexdigest() + "  " + REVIEW_MD.name)
    print(hashlib.sha256(json_a).hexdigest() + "  " + REVIEW_JSON.name)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit-dir", type=Path)
    args = parser.parse_args()
    if args.emit_dir is not None:
        return emit(args.emit_dir)

    errors = []
    validators = [
        (REGISTRY_VALIDATOR, b"VALID_READY_TO_FREEZE"),
        (REGISTRY_APPROVAL_VALIDATOR, b"VALID_APPROVED_RECONCILED_REGISTRY_BASELINE"),
        (PREFLIGHT_VALIDATOR, b"PHASE_2_DECISION_PACK_READY_FOR_HUMAN_APPROVAL"),
        (PACK_APPROVAL_VALIDATOR, b"VALID_APPROVED_PHASE_2_HUMAN_DECISION_PACK"),
    ]
    for path, marker in validators:
        result = run([sys.executable, str(path)])
        if result.returncode != 0 or marker not in result.stdout:
            errors.append("required validator failed: " + path.name)

    try:
        if command_text(["git", "rev-parse", ACCEPTED_TAG + "^{commit}"]).strip() != SOURCE_COMMIT:
            errors.append("accepted Decision Pack tag target differs")
        review = build_review()
        errors.extend(validate_source_lineage_and_paths(review))
        errors.extend(validate_review(review))
        expected_json = render_json(review)
        expected_markdown = render_markdown(review)
        if render_json(build_review()) != expected_json or render_markdown(build_review()) != expected_markdown:
            errors.append("review generation is not byte-deterministic")
        if index_blob(REVIEW_JSON) != expected_json:
            errors.append("staged review JSON differs from deterministic projection")
        if index_blob(REVIEW_MD) != expected_markdown:
            errors.append("staged review Markdown differs from deterministic projection")
    except (KeyError, OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        errors.append(str(exc))

    if run(["git", "diff", "--quiet", "HEAD", "--", *PROTECTED_PATHS]).returncode != 0:
        errors.append("a protected source/baseline artifact differs from HEAD")
    if run(["git", "diff", "--quiet"]).returncode != 0:
        errors.append("tracked working-tree content differs from the Git index")
    if run(["git", "diff", "--quiet", "--", str(REVIEW_MD.relative_to(ROOT)), str(REVIEW_JSON.relative_to(ROOT)), str(Path(__file__).resolve().relative_to(ROOT))]).returncode != 0:
        errors.append("Phase 2B working-tree content differs from the Git index")

    if errors:
        print("FAIL — PHASE_2_CRITICALITY_REVIEW_INVALID", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        return 1
    print("PASS — PHASE_2_CRITICALITY_REVIEW_READY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
