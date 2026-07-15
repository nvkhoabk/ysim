---
schema_version: "1.0"
document_code: V23-PHASE-2-CRITICALITY-DECISION-CANDIDATE
title: Phase 2 Criticality Decision Candidate
product_baseline: "2.3"
document_revision: "0.4"
lifecycle_status: CANDIDATE
language: en
authority: PHASE_2B_CONTROLLED_FAST_TRACK_CANDIDATE
supersedes: V23-P2B-CRITICALITY-REVIEW-R2
requirement_block_schema: null
---

# Phase 2 Criticality Decision Candidate

## 1. Candidate identity and source

- Candidate ID: `V23-P2B-CRITICALITY-DECISION-C1`.
- Status: `CANDIDATE`.
- Approval status: `PENDING_MARKDOWN_APPROVAL`.
- Source review: `V23-P2B-CRITICALITY-REVIEW-R2`.
- Source Decision Pack: `V23-P2A-DECISION-PACK-C1`.
- Source commit: `1a74dd7486945d3820e1d7c735f3b37cd9e418a7`.
- Accepted tag: `baseline/v2.3/phase-2/decision-pack/c1-accepted`.
- Hash basis: `GIT_INDEX_BLOB_CONTENT`.
- Line endings: `GIT_CANONICAL_TEXT`.
- Next gate: `HUMAN_CRITICALITY_DECISION_PACK_APPROVAL`.

The 2026-07-15 CONTROLLED FAST-TRACK authorization selects every existing recommended option for the 40 previously remaining exceptions. It does not authorize new interpretations, source edits, source resolution, stable-ID allocation, approval, commit, push, or tag.

## 2. Current and provisional projections

| Projection | CRITICAL | HIGH | NORMAL | Denominator | Inactive N/A |
|---|---:|---:|---:|---:|---:|
| Current source | 313 | 409 | 348 | 1070 | 106 |
| Provisional known-tier subset | 312 | 389 | 351 | 1052 | 107 |

Projection qualifier: `PROVISIONAL_EXCLUDES_PENDING_SOURCE_REMEDIATION_AND_CHILD_RECONCILIATION`.
Excluded pending source-remediation active units: `17`. Final atomic denominator: `UNKNOWN`; final tier distribution claimed: `NO`.

## 3. Decision accounting

- Source exceptions: `46`; OPEN: `46`; resolved: `0`.
- Dispositioned: `46`; undispositioned: `0`.
- Earlier explicit human decisions: `2`.
- Bulk-authorized human-risk decisions: `11`.
- Deterministic/policy remediation dispositions: `16`.
- Criticality-rule dispositions: `17`.
- Total: `46`.

### Selected effective outcomes

- `CRITICAL`: `13`.
- `HIGH`: `12`.
- `NORMAL`: `3`.
- `REMEDIATION_REQUIRED`: `18`.

### Related non-exception extraction defect

- Requirement: `BRD-EVENT-INDEX-R001` (not a source criticality exception; source exception count remains 46).
- Existing truncated statement: “phải đảm bảo thứ tự xử lý.”
- Effective statement candidate: “Payment, Settlement, and Financial events must preserve processing order.”
- Remediation: `EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT` with corrected source coverage `L193-L197`.
- Carry forward: later source remediation and validation; no source change is applied by this pack.

## 4. Structural reconciliation-impact register

| Source identity | Exception | Impact | Candidate children | Canonical result | IDs allocated | In projection | Blocker |
|---|---|---|---:|---|---|---|---|
| `BRD-UPDATE-01-R010` | `P2-CRIT-EXC-005` | `COMPOSITE_PARENT_CHILD_RECONCILIATION` | 12 | `UNKNOWN` | `NO` | `NO` | `SEMANTIC_NORMALIZATION_OVERLAP_ALIAS_SCOPE_AND_ATOMICITY_RECONCILIATION` |
| `BRD-WS-17-R013` | `P2-CRIT-EXC-023` | `COMPOSITE_PARENT_CHILD_RECONCILIATION` | 6 | `UNKNOWN` | `NO` | `NO` | `OVERLAP_RECONCILIATION_AND_PER_CHILD_TYPE_CRITICALITY_ACCEPTANCE_CONTRACTS` |
| `BRD-WS-08-R012` | `P2-CRIT-EXC-020` | `ACTIVE_DEFERRED_SCOPE_SPLIT` | UNKNOWN | `UNKNOWN` | `NO` | `NO` | `SPLIT_ACTIVE_RULE_BASED_BEHAVIOR_FROM_DEFERRED_ML_AND_RECONCILE_IDENTITIES` |

## 5. Candidate approval block

- Candidate Approval: `PENDING`.
- Markdown Approval: `PENDING`.
- Approver: `PENDING`.
- Approval Date: `PENDING`.
- Source Application: `PENDING`.

## 6. Classification summary

| Finding classification | Count |
|---|---:|
| `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 18 |
| `HUMAN_RISK_DECISION` | 11 |
| `RULE_APPLICATION` | 17 |

## 7. Cluster summary

| Cluster | Classification | Members | Review status | Recommended option | Selected option | Uniform safe |
|---|---|---:|---|---|---|---|
| `P2-CRIT-CL-033` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `ROUTE_TO_SCOPE_REMEDIATION` | `ROUTE_TO_SCOPE_REMEDIATION` | `YES` |
| `P2-CRIT-CL-034` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `APPROVED_SCOPE_PROMOTION_REMEDIATION` | `APPROVED_SCOPE_PROMOTION_REMEDIATION` | `YES` |
| `P2-CRIT-CL-035` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `APPROVED_SCOPE_PROMOTION_REMEDIATION` | `APPROVED_SCOPE_PROMOTION_REMEDIATION` | `YES` |
| `P2-CRIT-CL-002` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT` | `EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT` | `YES` |
| `P2-CRIT-CL-003` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION` | `COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION` | `YES` |
| `P2-CRIT-CL-004` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN` | `COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN` | `YES` |
| `P2-CRIT-CL-005` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `ROUTE_TO_REMEDIATION` | `ROUTE_TO_REMEDIATION` | `YES` |
| `P2-CRIT-CL-006` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `ROUTE_TO_REMEDIATION` | `ROUTE_TO_REMEDIATION` | `YES` |
| `P2-CRIT-CL-007` | `HUMAN_RISK_DECISION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_CRITICAL` | `CONFIRM_CRITICAL` | `YES` |
| `P2-CRIT-CL-008` | `HUMAN_RISK_DECISION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_HIGH` | `CONFIRM_HIGH` | `YES` |
| `P2-CRIT-CL-009` | `RULE_APPLICATION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_HIGH` | `CONFIRM_HIGH` | `YES` |
| `P2-CRIT-CL-010` | `HUMAN_RISK_DECISION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_NORMAL` | `CONFIRM_NORMAL` | `YES` |
| `P2-CRIT-CL-011` | `HUMAN_RISK_DECISION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_HIGH` | `CONFIRM_HIGH` | `YES` |
| `P2-CRIT-CL-012` | `HUMAN_RISK_DECISION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_HIGH` | `CONFIRM_HIGH` | `YES` |
| `P2-CRIT-CL-013` | `HUMAN_RISK_DECISION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_CRITICAL` | `CONFIRM_CRITICAL` | `YES` |
| `P2-CRIT-CL-014` | `HUMAN_RISK_DECISION` | 2 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_HIGH` | `CONFIRM_HIGH` | `YES` |
| `P2-CRIT-CL-015` | `HUMAN_RISK_DECISION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_HIGH` | `CONFIRM_HIGH` | `YES` |
| `P2-CRIT-CL-016` | `HUMAN_RISK_DECISION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_NORMAL` | `CONFIRM_NORMAL` | `YES` |
| `P2-CRIT-CL-017` | `RULE_APPLICATION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_HIGH` | `CONFIRM_HIGH` | `YES` |
| `P2-CRIT-CL-018` | `RULE_APPLICATION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_CRITICAL` | `CONFIRM_CRITICAL` | `YES` |
| `P2-CRIT-CL-019` | `RULE_APPLICATION` | 4 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_CRITICAL` | `CONFIRM_CRITICAL` | `YES` |
| `P2-CRIT-CL-020` | `RULE_APPLICATION` | 2 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_HIGH` | `CONFIRM_HIGH` | `YES` |
| `P2-CRIT-CL-021` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 3 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `ROUTE_TO_REMEDIATION` | `ROUTE_TO_REMEDIATION` | `YES` |
| `P2-CRIT-CL-022` | `RULE_APPLICATION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_CRITICAL` | `CONFIRM_CRITICAL` | `YES` |
| `P2-CRIT-CL-023` | `RULE_APPLICATION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_HIGH` | `CONFIRM_HIGH` | `YES` |
| `P2-CRIT-CL-024` | `RULE_APPLICATION` | 2 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_CRITICAL` | `CONFIRM_CRITICAL` | `YES` |
| `P2-CRIT-CL-025` | `RULE_APPLICATION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_NORMAL` | `CONFIRM_NORMAL` | `YES` |
| `P2-CRIT-CL-026` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 3 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `ROUTE_TO_REMEDIATION` | `ROUTE_TO_REMEDIATION` | `YES` |
| `P2-CRIT-CL-027` | `RULE_APPLICATION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_CRITICAL` | `CONFIRM_CRITICAL` | `YES` |
| `P2-CRIT-CL-028` | `RULE_APPLICATION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_CRITICAL` | `CONFIRM_CRITICAL` | `YES` |
| `P2-CRIT-CL-029` | `RULE_APPLICATION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_CRITICAL` | `CONFIRM_CRITICAL` | `YES` |
| `P2-CRIT-CL-030` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `ROUTE_TO_REMEDIATION` | `ROUTE_TO_REMEDIATION` | `YES` |
| `P2-CRIT-CL-031` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | 3 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `ROUTE_TO_REMEDIATION` | `ROUTE_TO_REMEDIATION` | `YES` |
| `P2-CRIT-CL-032` | `HUMAN_RISK_DECISION` | 1 | `DISPOSITIONED_PENDING_PACK_APPROVAL` | `CONFIRM_HIGH` | `CONFIRM_HIGH` | `YES` |

## 8. Disposition clusters

### P2-CRIT-CL-033 — Product Variant inactive-scope human decision

- Classification: `CLASSIFICATION_OR_EXTRACTION_DEFECT`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-001`.
- Common decision question: Should Product Variant remain outside v2.3 and be routed to inactive-scope remediation?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `SD-02`, `HUMAN_DECISION_2026-07-14`.
- Recommended option: `ROUTE_TO_SCOPE_REMEDIATION`.
- Recommendation rationale: Product Variant has no approved scope promotion; the human selected option 1 to retain it outside v2.3.
- Under-classification consequence: Keeping Product Variant active would contradict the selected scope decision and create an implementation-acceptance obligation for an excluded capability.
- Acceptance-depth impact: Use NOT_APPLICABLE_FOR_V2.3 and assign no verification criticality while inactive.
- Confidence: `HIGH`.
- Selected option: `ROUTE_TO_SCOPE_REMEDIATION`.
- Remediation contract: `{"acceptance_applicability": "NOT_APPLICABLE_FOR_V2.3", "decision_provenance": "Human selected option 1 on 2026-07-14; unpromoted legacy future capabilities remain outside v2.3.", "decision_status": "DECIDED_PENDING_REVIEW_PACK_APPROVAL", "target_scope": "FUTURE_OR_EQUIVALENT_INACTIVE_V2_3", "verification_criticality": null}`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `ROUTE_TO_SCOPE_REMEDIATION` | `REMEDIATE_AS_INACTIVE` | `INACTIVE` | `YES` | `YES` |
| `KEEP_ACTIVE_WITH_NEW_SCOPE_PROMOTION` | `KEEP_ACTIVE` | `KEEP_CURRENT` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-001 — BD-04-007

- Source: `docs/BRD/BRD-WS-04.md`, `24. Business Decisions (Locked) > BD-04-007`, `L571-L574`.
- Type/scope: `SCOPE_CONSTRAINT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `ROUTE_TO_SCOPE_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Product Variant has no approved scope promotion; the human selected option 1 to retain it outside v2.3.
- Consequence of under-classification: Keeping Product Variant active would contradict the selected scope decision and create an implementation-acceptance obligation for an excluded capability.
- Acceptance-depth impact: Use NOT_APPLICABLE_FOR_V2.3 and assign no verification criticality while inactive.
- Human options: `ROUTE_TO_SCOPE_REMEDIATION`, `KEEP_ACTIVE_WITH_NEW_SCOPE_PROMOTION`.
- Selected disposition: `ROUTE_TO_SCOPE_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `EARLIER_EXPLICIT_HUMAN_DECISION`.
- Provenance: `{"authority": "EXPLICIT_HUMAN_SELECTION", "decision_date": "2026-07-14", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Product Variant chưa triển khai trong phiên bản 2.0.
```

Canonical source context:

```text
## BD-04-007

Product Variant chưa triển khai trong phiên bản 2.0.

```

### P2-CRIT-CL-034 — Shared Approval Engine approved scope promotion

- Classification: `CLASSIFICATION_OR_EXTRACTION_DEFECT`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-003`.
- Common decision question: How must the legacy CAP-9003 Future row be remediated to reflect the approved v2.3 Shared Approval Engine?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `SD-03`, `BDD-27`.
- Recommended option: `APPROVED_SCOPE_PROMOTION_REMEDIATION`.
- Recommendation rationale: SD-03 and BDD-27 override the legacy Future label and require an active Shared Approval Engine distinct from general-purpose BPM workflow.
- Under-classification consequence: Routing the capability inactive would violate approved scope and omit separation-of-duties, expiry, escalation, evidence, and immutable-audit obligations.
- Acceptance-depth impact: Keep HIGH only as provisional; rewrite the active contract and re-evaluate type and criticality before acceptance depth is finalized.
- Confidence: `HIGH`.
- Selected option: `APPROVED_SCOPE_PROMOTION_REMEDIATION`.
- Remediation contract: `{"criticality_finalized": false, "excluded_inference": "GENERAL_PURPOSE_BPM_WORKFLOW_ENGINE", "provisional_criticality": "HIGH", "required_source_remediation": "Rewrite the legacy row into the active Shared Approval Engine contract with SD-03 and BDD-27 provenance.", "route": "APPROVED_SCOPE_PROMOTION_REMEDIATION", "target_scope": "V2.3_ACTIVE"}`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `APPROVED_SCOPE_PROMOTION_REMEDIATION` | `REWRITE_AS_ACTIVE_SHARED_APPROVAL_ENGINE` | `KEEP_CURRENT` | `YES` | `YES` |
| `ESCALATE_APPROVED_PRECEDENCE_CONFLICT` | `ESCALATE_PRECEDENCE_CONFLICT` | `KEEP_CURRENT` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-003 — BRD-CAP-INDEX-R007

- Source: `docs/BRD/BRD-CAP-INDEX.md`, `13.17 Cross Platform Capabilities`, `L626`.
- Type/scope: `SCOPE_CONSTRAINT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_PORTAL_STOREFRONT_ACCESSIBILITY`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `APPROVED_SCOPE_PROMOTION_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: SD-03 and BDD-27 override the legacy Future label and require an active Shared Approval Engine distinct from general-purpose BPM workflow.
- Consequence of under-classification: Routing the capability inactive would violate approved scope and omit separation-of-duties, expiry, escalation, evidence, and immutable-audit obligations.
- Acceptance-depth impact: Keep HIGH only as provisional; rewrite the active contract and re-evaluate type and criticality before acceptance depth is finalized.
- Human options: `APPROVED_SCOPE_PROMOTION_REMEDIATION`, `ESCALATE_APPROVED_PRECEDENCE_CONFLICT`.
- Selected disposition: `APPROVED_SCOPE_PROMOTION_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
| CAP ID | Capability | Level | Main Business Object | Availability | Workshop |
| CAP-9003 | Approval Engine | Platform | Approval Workflow | Platform | Future |
```

Canonical source context:

```text
| CAP-9003 | Approval Engine | Platform | Approval Workflow | Platform | Future |
```

### P2-CRIT-CL-035 — Rule-based Fraud/Risk Engine approved scope promotion

- Classification: `CLASSIFICATION_OR_EXTRACTION_DEFECT`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-020`.
- Common decision question: How must the legacy Anti Fraud Engine future statement be remediated to separate active rule-based risk from deferred ML?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `SD-03`, `BDD-26`.
- Recommended option: `APPROVED_SCOPE_PROMOTION_REMEDIATION`.
- Recommendation rationale: SD-03 requires rule-based Fraud/Risk for authentication, checkout, and payment while advanced/ML scoring remains post-v2.3.
- Under-classification consequence: Routing the whole capability inactive would remove approved authentication, checkout, and payment risk controls.
- Acceptance-depth impact: Keep CRITICAL only as provisional; split/rewrite the statement and re-evaluate type and criticality before acceptance depth is finalized.
- Confidence: `HIGH`.
- Selected option: `APPROVED_SCOPE_PROMOTION_REMEDIATION`.
- Remediation contract: `{"active_surfaces": ["LOGIN_AUTHENTICATION", "CHECKOUT", "PAYMENT"], "criticality_finalized": false, "deferred_scope": "ML_AND_ADVANCED_SCORING_POST_V2.3", "provisional_criticality": "CRITICAL", "required_source_remediation": "Rewrite or split the legacy statement into active rule-based behavior and explicitly deferred ML.", "route": "APPROVED_SCOPE_PROMOTION_REMEDIATION", "target_scope": "V2.3_ACTIVE_RULE_BASED"}`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `APPROVED_SCOPE_PROMOTION_REMEDIATION` | `SPLIT_ACTIVE_RULE_BASED_AND_DEFERRED_ML` | `KEEP_CURRENT` | `YES` | `YES` |
| `ESCALATE_APPROVED_PRECEDENCE_CONFLICT` | `ESCALATE_PRECEDENCE_CONFLICT` | `KEEP_CURRENT` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-020 — BRD-WS-08-R012

- Source: `docs/BRD/BRD-WS-08.md`, `21. Payment Security`, `L474`.
- Type/scope: `SCOPE_CONSTRAINT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_FINANCIAL_PRICING_INTEGRITY`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `APPROVED_SCOPE_PROMOTION_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: SD-03 requires rule-based Fraud/Risk for authentication, checkout, and payment while advanced/ML scoring remains post-v2.3.
- Consequence of under-classification: Routing the whole capability inactive would remove approved authentication, checkout, and payment risk controls.
- Acceptance-depth impact: Keep CRITICAL only as provisional; split/rewrite the statement and re-evaluate type and criticality before acceptance depth is finalized.
- Human options: `APPROVED_SCOPE_PROMOTION_REMEDIATION`, `ESCALATE_APPROVED_PRECEDENCE_CONFLICT`.
- Selected disposition: `APPROVED_SCOPE_PROMOTION_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Anti Fraud Engine sẽ triển khai ở phiên bản sau.
```

Canonical source context:

```text
Anti Fraud Engine sẽ triển khai ở phiên bản sau.
```

### P2-CRIT-CL-002 — Event Ordering R002 deterministic extraction remediation

- Classification: `CLASSIFICATION_OR_EXTRACTION_DEFECT`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-004`.
- Common decision question: Must the Marketing, Analytics, and Notification subject list be restored before criticality is re-evaluated?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-002`, `P2-DEC-004`.
- Recommended option: `EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT`.
- Recommendation rationale: The extracted statement contains only the trailing predicate; source context distinguishes ordered financial events from unordered marketing, analytics, and notification events.
- Under-classification consequence: A fragment-level tier can attach ordering evidence to the wrong event families and hide data-integrity or delivery risks.
- Acceptance-depth impact: Acceptance and criticality remain unfinalized until the corrected effective statement is re-evaluated.
- Confidence: `HIGH`.
- Selected option: `EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT`.
- Remediation contract: `{"corrected_source_coverage_candidate": "L201-L205", "criticality_finalized": false, "criticality_re_evaluation_required": true, "effective_statement_candidate": "Marketing, Analytics, and Notification events are not required to preserve processing order.", "existing_truncated_statement": "không bắt buộc Ordering.", "preserve_stable_id": "BRD-EVENT-INDEX-R002", "remediation": "EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT", "requirement_type": "DESIGN_PRINCIPLE", "scope_status": "V2.3_ACTIVE", "source_coverage_includes_event_family_subjects_and_predicate": true}`.

- Effective statement candidate: “Marketing, Analytics, and Notification events are not required to preserve processing order.”
- Corrected source coverage candidate: `L201-L205` (event-family subjects plus predicate).
- Criticality finalized: `NO`; re-evaluation is required after source remediation.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT` | `REMEDIATE_RULE_INPUT_BEFORE_CRITICALITY` | `KEEP_CURRENT` | `YES` | `YES` |
| `REJECT_DEFECT_AND_KEEP_PROVISIONAL` | `REJECT_DEFECT_FINDING` | `KEEP_CURRENT` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-004 — BRD-EVENT-INDEX-R002

- Source: `docs/BRD/BRD-EVENT-INDEX.md`, `7. Event Delivery Principles`, `L205`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The extracted statement contains only the trailing predicate; source context distinguishes ordered financial events from unordered marketing, analytics, and notification events.
- Consequence of under-classification: A fragment-level tier can attach ordering evidence to the wrong event families and hide data-integrity or delivery risks.
- Acceptance-depth impact: Acceptance and criticality remain unfinalized until the corrected effective statement is re-evaluated.
- Human options: `EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
không bắt buộc Ordering.
```

Canonical source context:

```text
không bắt buộc Ordering.
```

### P2-CRIT-CL-003 — Business Principles composite-parent human decision

- Classification: `CLASSIFICATION_OR_EXTRACTION_DEFECT`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-005`.
- Common decision question: Should BRD-UPDATE-01-R010 become a composite parent pending atomic child reconciliation?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-005`, `HUMAN_DECISION_2026-07-14`.
- Recommended option: `COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION`.
- Recommendation rationale: The statement merely introduces a list and contains no independently verifiable principle.
- Under-classification consequence: Treating a preamble as an atomic HIGH unit inflates coverage while providing no observable obligation.
- Acceptance-depth impact: Only resulting canonical atomic children receive criticality and acceptance contracts.
- Confidence: `HIGH`.
- Selected option: `COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION`.
- Remediation contract: `{"acceptance_unit": false, "child_candidates": [{"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Business Model First", "explanatory_source_sentence": "Business Model là điểm khởi đầu của mọi Commerce Experience trên nền tảng YSim.", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Template Driven", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Configuration over Customization", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "White-label by Default", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Publish in Minutes", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Experience First", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Multi-brand", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Multi-language", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Multi-country", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "API First", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Headless Ready", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "AI Ready", "non_inference_guard": "MUST_NOT_BE_INTERPRETED_AS_AN_ACTIVE_AI_PRODUCT_FEATURE_WITHOUT_AN_APPROVED_REQUIREMENT", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}], "child_id_allocation": "DEFERRED_PENDING_OVERLAP_RECONCILIATION", "composite_parent_candidate": true, "criticality_assignment_target": "RESULTING_CANONICAL_ATOMIC_CHILDREN_ONLY", "criticality_unit": false, "decision": "COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION", "decision_provenance": "Human selected option 1 on 2026-07-14.", "do_not_blindly_create_twelve_requirements": true, "implementation_unit": false, "preserve_parent_stable_id": "BRD-UPDATE-01-R010", "projected_count_changes_applied": false, "scope_coverage_unit": false, "source_coverage_candidate": "L629-L644", "structural_count_impact": "PENDING_CHILD_RECONCILIATION"}`.

#### Pending child reconciliation contract

- Composite parent candidate: `YES`; parent stable ID: `BRD-UPDATE-01-R010`.
- Parent units: implementation `NO`; acceptance `NO`; scope coverage `NO`; criticality `NO`.
- Structural count impact: `PENDING_CHILD_RECONCILIATION`; child ID allocation: `DEFERRED_PENDING_OVERLAP_RECONCILIATION`.

Atomic child candidates:

1. Business Model First
   - Explanatory source sentence: “Business Model là điểm khởi đầu của mọi Commerce Experience trên nền tảng YSim.”
2. Template Driven
3. Configuration over Customization
4. White-label by Default
5. Publish in Minutes
6. Experience First
7. Multi-brand
8. Multi-language
9. Multi-country
10. API First
11. Headless Ready
12. AI Ready
   - Non-inference guard: `MUST_NOT_BE_INTERPRETED_AS_AN_ACTIVE_AI_PRODUCT_FEATURE_WITHOUT_AN_APPROVED_REQUIREMENT`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION` | `MODEL_COMPOSITE_PARENT_AND_RECONCILE_ATOMIC_CHILDREN` | `KEEP_CURRENT` | `YES` | `YES` |
| `REJECT_COMPOSITE_MODEL_AND_KEEP_PROVISIONAL` | `REJECT_COMPOSITE_MODEL` | `KEEP_CURRENT` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-005 — BRD-UPDATE-01-R010

- Source: `docs/BRD/BRD-UPDATE-01.md`, `6I. Business Principles`, `L629`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The statement merely introduces a list and contains no independently verifiable principle.
- Consequence of under-classification: Treating a preamble as an atomic HIGH unit inflates coverage while providing no observable obligation.
- Acceptance-depth impact: Only resulting canonical atomic children receive criticality and acceptance contracts.
- Human options: `COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION`, `REJECT_COMPOSITE_MODEL_AND_KEEP_PROVISIONAL`.
- Selected disposition: `COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION` (matches recommendation: `YES`).
- Decision basis: `EARLIER_EXPLICIT_HUMAN_DECISION`.
- Provenance: `{"authority": "EXPLICIT_HUMAN_SELECTION", "decision_date": "2026-07-14", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Commerce Experience Platform tuân thủ các nguyên tắc sau.
```

Canonical source context:

```text
Commerce Experience Platform tuân thủ các nguyên tắc sau.
```

### P2-CRIT-CL-004 — Enterprise Operations composite-parent deterministic remediation

- Classification: `CLASSIFICATION_OR_EXTRACTION_DEFECT`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-023`.
- Common decision question: Should BRD-WS-17-R013 become a composite parent with six atomic child candidates?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-003`, `P2-DEC-004`, `P2-DEC-010`.
- Recommended option: `COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN`.
- Recommendation rationale: The extraction ends at a colon and omits every capability that gives the principle meaning.
- Under-classification consequence: A generic HIGH label can mask CRITICAL audit/recovery obligations and under-specify operational failure evidence.
- Acceptance-depth impact: Each resulting canonical atomic child receives its own type, criticality, and acceptance contract.
- Confidence: `HIGH`.
- Selected option: `COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN`.
- Remediation contract: `{"acceptance_unit": false, "child_candidates": [{"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Every operational task must be observable.", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Every operational task must be auditable.", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Every operational task must be configurable.", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Every operational task must be recoverable.", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "Every operational task must be automatable.", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}, {"atomicity_review_required": true, "candidate_id": null, "candidate_name": "An operator must not directly manipulate infrastructure when the Platform provides the corresponding operation.", "overlap_alias_check_required": true, "scope_confirmation_required": true, "semantic_normalization_required": true}], "child_contract_assignment": "EACH_CHILD_RECEIVES_OWN_TYPE_CRITICALITY_AND_ACCEPTANCE_CONTRACT", "child_id_allocation": "DEFERRED_PENDING_OVERLAP_RECONCILIATION", "composite_parent_candidate": true, "criticality_unit": false, "decision": "COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN", "explanatory_non_requirement_sentence": "Đây là nguyên lý cốt lõi của Enterprise Operations Foundation.", "explanatory_sentence_becomes_requirement": false, "implementation_unit": false, "parent_to_child_coverage_semantics": "ALL_CHILDREN", "preserve_parent_stable_id": "BRD-WS-17-R013", "projected_count_changes_applied": false, "scope_coverage_unit": false, "source_coverage_candidate": "L798-L810", "structural_count_impact": "PENDING_CHILD_RECONCILIATION"}`.

#### Pending child reconciliation contract

- Composite parent candidate: `YES`; parent stable ID: `BRD-WS-17-R013`.
- Parent units: implementation `NO`; acceptance `NO`; scope coverage `NO`; criticality `NO`.
- Structural count impact: `PENDING_CHILD_RECONCILIATION`; child ID allocation: `DEFERRED_PENDING_OVERLAP_RECONCILIATION`.
- Parent-to-child coverage semantics: `ALL_CHILDREN`.
- Explanatory only, not another requirement: “Đây là nguyên lý cốt lõi của Enterprise Operations Foundation.”

Atomic child candidates:

1. Every operational task must be observable.
2. Every operational task must be auditable.
3. Every operational task must be configurable.
4. Every operational task must be recoverable.
5. Every operational task must be automatable.
6. An operator must not directly manipulate infrastructure when the Platform provides the corresponding operation.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN` | `MODEL_COMPOSITE_PARENT_AND_RECONCILE_ATOMIC_CHILDREN` | `KEEP_CURRENT` | `YES` | `YES` |
| `REJECT_COMPOSITE_MODEL_AND_KEEP_PROVISIONAL` | `REJECT_COMPOSITE_MODEL` | `KEEP_CURRENT` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-023 — BRD-WS-17-R013

- Source: `docs/BRD/BRD-WS-17.md`, `30. Enterprise Operations Principle`, `L798-L800`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_NOTIFICATION_REPORTING_OPERATIONS`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The extraction ends at a colon and omits every capability that gives the principle meaning.
- Consequence of under-classification: A generic HIGH label can mask CRITICAL audit/recovery obligations and under-specify operational failure evidence.
- Acceptance-depth impact: Each resulting canonical atomic child receives its own type, criticality, and acceptance contract.
- Human options: `COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN`, `REJECT_COMPOSITE_MODEL_AND_KEEP_PROVISIONAL`.
- Selected disposition: `COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Platform áp dụng nguyên lý:

**Mọi tác vụ vận hành phải có khả năng:**
```

Canonical source context:

```text
Platform áp dụng nguyên lý:

**Mọi tác vụ vận hành phải có khả năng:**
```

### P2-CRIT-CL-005 — Product vision used as an atomic implementation unit

- Classification: `CLASSIFICATION_OR_EXTRACTION_DEFECT`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-016`.
- Common decision question: Is the positioning statement an atomic implementation requirement or non-normative product vision?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `ROUTE_TO_REMEDIATION`.
- Recommendation rationale: The source describes market positioning rather than an observable system behavior.
- Under-classification consequence: Forcing implementation acceptance onto vision wording invites arbitrary criteria and false traceability.
- Acceptance-depth impact: Classification/identity must be corrected or a concrete derived requirement approved before acceptance depth is assigned.
- Confidence: `HIGH`.
- Selected option: `ROUTE_TO_REMEDIATION`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `ROUTE_TO_REMEDIATION` | `REMEDIATE_RULE_INPUT_BEFORE_CRITICALITY` | `KEEP_CURRENT` | `YES` | `YES` |
| `REJECT_DEFECT_AND_KEEP_PROVISIONAL` | `REJECT_DEFECT_FINDING` | `KEEP_CURRENT` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-016 — BRD-WS-01-R001

- Source: `docs/BRD/BRD-WS-01.md`, `2. Product Vision`, `L30`.
- Type/scope: `BUSINESS_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `ROUTE_TO_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The source describes market positioning rather than an observable system behavior.
- Consequence of under-classification: Forcing implementation acceptance onto vision wording invites arbitrary criteria and false traceability.
- Acceptance-depth impact: Classification/identity must be corrected or a concrete derived requirement approved before acceptance depth is assigned.
- Human options: `ROUTE_TO_REMEDIATION`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `ROUTE_TO_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
YSim không được định vị là một website bán eSIM đơn lẻ mà là một White-label Commerce Platform dành riêng cho ngành eSIM.
```

Canonical source context:

```text
YSim không được định vị là một website bán eSIM đơn lẻ mà là một White-label Commerce Platform dành riêng cho ngành eSIM.
```

### P2-CRIT-CL-006 — Context-free product-scope fragment

- Classification: `CLASSIFICATION_OR_EXTRACTION_DEFECT`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-017`.
- Common decision question: Must the subject and normative scope contract for the White-label Commerce fragment be restored before tiering?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `ROUTE_TO_REMEDIATION`.
- Recommendation rationale: The statement is a list fragment without actor, obligation, or acceptance surface.
- Under-classification consequence: A tier on the fragment does not establish what must be delivered and can duplicate more concrete storefront requirements.
- Acceptance-depth impact: Acceptance is blocked until a complete normative statement and relationship to concrete requirements are established.
- Confidence: `HIGH`.
- Selected option: `ROUTE_TO_REMEDIATION`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `ROUTE_TO_REMEDIATION` | `REMEDIATE_RULE_INPUT_BEFORE_CRITICALITY` | `KEEP_CURRENT` | `YES` | `YES` |
| `REJECT_DEFECT_AND_KEEP_PROVISIONAL` | `REJECT_DEFECT_FINDING` | `KEEP_CURRENT` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-017 — BRD-WS-01-R004

- Source: `docs/BRD/BRD-WS-01.md`, `4. Product Scope > In Scope`, `L62`.
- Type/scope: `BUSINESS_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `ROUTE_TO_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The statement is a list fragment without actor, obligation, or acceptance surface.
- Consequence of under-classification: A tier on the fragment does not establish what must be delivered and can duplicate more concrete storefront requirements.
- Acceptance-depth impact: Acceptance is blocked until a complete normative statement and relationship to concrete requirements are established.
- Human options: `ROUTE_TO_REMEDIATION`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `ROUTE_TO_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
- White-label Commerce
```

Canonical source context:

```text
- White-label Commerce
```

### P2-CRIT-CL-007 — Organization bootstrap security boundary

- Classification: `HUMAN_RISK_DECISION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-002`.
- Common decision question: Does Organization Template bootstrap require CRITICAL verification because it creates roles and production configuration, or HIGH as a core administrative workflow?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-001`, `P2-DEC-008`, `P2-DEC-010`.
- Recommended option: `CONFIRM_CRITICAL`.
- Recommendation rationale: Bootstrap creates authorization and runtime configuration together; an unsafe default can grant access or misconfigure an entire tenant.
- Under-classification consequence: Under-classification may omit fail-closed, least-privilege, rollback, audit, and partial-bootstrap recovery evidence.
- Acceptance-depth impact: CRITICAL adds negative/fail-closed and recovery/authorization-boundary evidence; HIGH covers the primary failure path only.
- Confidence: `MEDIUM`.
- Selected option: `CONFIRM_CRITICAL`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_CRITICAL` | `CLASSIFY_AS_CRITICAL` | `CRITICAL` | `YES` | `YES` |
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-002 — BD-14-022

- Source: `docs/BRD/BRD-WS-14.md`, `31. Business Decisions (Locked) > BD-14-022`, `L1109-L1126`.
- Type/scope: `BUSINESS_DECISION` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_NOTIFICATION_REPORTING_OPERATIONS`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `MEDIUM`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Bootstrap creates authorization and runtime configuration together; an unsafe default can grant access or misconfigure an entire tenant.
- Consequence of under-classification: Under-classification may omit fail-closed, least-privilege, rollback, audit, and partial-bootstrap recovery evidence.
- Acceptance-depth impact: CRITICAL adds negative/fail-closed and recovery/authorization-boundary evidence; HIGH covers the primary failure path only.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION`.
- Provenance: `{"authority": "CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "authorization_scope": "ACCEPT_EXISTING_RECOMMENDED_OPTIONS_FOR_REMAINING_EXCEPTIONS", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Organization Template hỗ trợ Bootstrap toàn bộ Organization.

Template tự động tạo:

- Role
- Dashboard
- Storefront
- Theme
- Report
- Notification
- KB
- FAQ
- Survey
- Support Policy
- Configuration
```

Canonical source context:

```text
## BD-14-022

Organization Template hỗ trợ Bootstrap toàn bộ Organization.

Template tự động tạo:

- Role
- Dashboard
- Storefront
- Theme
- Report
- Notification
- KB
- FAQ
- Survey
- Support Policy
- Configuration

```

### P2-CRIT-CL-008 — Store currency capability

- Classification: `HUMAN_RISK_DECISION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-006`.
- Common decision question: Is Currency a financial-integrity boundary requiring CRITICAL, or a white-label store capability adequately covered as HIGH?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-010`.
- Recommended option: `CONFIRM_HIGH`.
- Recommendation rationale: The source places Currency beside branding and localization but does not state settlement, conversion, or ledger semantics.
- Under-classification consequence: If transactional currency is intended, HIGH could omit fail-closed evidence for amount/currency mismatch; if only presentation is intended, CRITICAL overstates the contract.
- Acceptance-depth impact: CRITICAL requires negative financial-integrity evidence; HIGH requires expected behavior plus the principal currency edge case.
- Confidence: `MEDIUM`.
- Selected option: `CONFIRM_HIGH`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_CRITICAL` | `CLASSIFY_AS_CRITICAL` | `CRITICAL` | `NO` | `NO` |
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `YES` | `YES` |

#### Member records

##### P2-CRIT-EXC-006 — BRD-UPDATE-01-R018

- Source: `docs/BRD/BRD-UPDATE-01.md`, `12. White-label Capability`, `L824-L831`.
- Type/scope: `BUSINESS_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_FINANCIAL_PRICING_INTEGRITY`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `CONFIRM_HIGH`; confidence `MEDIUM`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The source places Currency beside branding and localization but does not state settlement, conversion, or ledger semantics.
- Consequence of under-classification: If transactional currency is intended, HIGH could omit fail-closed evidence for amount/currency mismatch; if only presentation is intended, CRITICAL overstates the contract.
- Acceptance-depth impact: CRITICAL requires negative financial-integrity evidence; HIGH requires expected behavior plus the principal currency edge case.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_HIGH` (matches recommendation: `YES`).
- Decision basis: `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION`.
- Provenance: `{"authority": "CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "authorization_scope": "ACCEPT_EXISTING_RECOMMENDED_OPTIONS_FOR_REMAINING_EXCEPTIONS", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `HIGH`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Store phải hỗ trợ:

- Currency
```

Canonical source context:

```text
Store phải hỗ trợ:

- Brand Name
- Logo
- Domain
- Theme
- Language
- Currency
```

### P2-CRIT-CL-009 — Commerce First principle

- Classification: `RULE_APPLICATION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-007`.
- Common decision question: Should the Commerce First design principle remain HIGH rather than be treated as non-runtime descriptive governance?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `CONFIRM_HIGH`.
- Recommendation rationale: The principle governs the product's core commerce behavior rather than presentation convenience.
- Under-classification consequence: NORMAL could permit shallow evidence that fails to demonstrate the principle at the business-contract boundary.
- Acceptance-depth impact: HIGH requires an expected commerce path and primary failure/edge path; NORMAL would require only one observable criterion.
- Confidence: `MEDIUM`.
- Selected option: `CONFIRM_HIGH`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `YES` | `YES` |
| `CONFIRM_NORMAL` | `CLASSIFY_AS_NORMAL` | `NORMAL` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-007 — BRD-UPDATE-01-R020

- Source: `docs/BRD/BRD-UPDATE-01.md`, `17. Business Principles`, `L904-L906`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `CONFIRM_HIGH`; confidence `MEDIUM`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The principle governs the product's core commerce behavior rather than presentation convenience.
- Consequence of under-classification: NORMAL could permit shallow evidence that fails to demonstrate the principle at the business-contract boundary.
- Acceptance-depth impact: HIGH requires an expected commerce path and primary failure/edge path; NORMAL would require only one observable criterion.
- Human options: `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_HIGH` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `HIGH`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Commerce Experience Platform tuân thủ:

- Commerce First
```

Canonical source context:

```text
Commerce Experience Platform tuân thủ:

- Commerce First
```

### P2-CRIT-CL-010 — Configuration over Customization principle

- Classification: `HUMAN_RISK_DECISION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-008`.
- Common decision question: Is this an enforceable runtime/configuration boundary at HIGH, or non-runtime governance at NORMAL?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-010`.
- Recommended option: `CONFIRM_NORMAL`.
- Recommendation rationale: The isolated principle does not specify production configuration integrity or a runtime acceptance surface.
- Under-classification consequence: If it actually constrains runtime customization, NORMAL may miss unsafe bypass and unsupported customization paths.
- Acceptance-depth impact: NORMAL uses one observable governance criterion; HIGH adds the primary unsupported-customization failure path.
- Confidence: `MEDIUM`.
- Selected option: `CONFIRM_NORMAL`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `NO` | `NO` |
| `CONFIRM_NORMAL` | `CLASSIFY_AS_NORMAL` | `NORMAL` | `YES` | `YES` |

#### Member records

##### P2-CRIT-EXC-008 — BRD-UPDATE-01-R021

- Source: `docs/BRD/BRD-UPDATE-01.md`, `17. Business Principles`, `L904-L907`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `CONFIRM_NORMAL`; confidence `MEDIUM`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The isolated principle does not specify production configuration integrity or a runtime acceptance surface.
- Consequence of under-classification: If it actually constrains runtime customization, NORMAL may miss unsafe bypass and unsupported customization paths.
- Acceptance-depth impact: NORMAL uses one observable governance criterion; HIGH adds the primary unsupported-customization failure path.
- Human options: `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_NORMAL` (matches recommendation: `YES`).
- Decision basis: `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION`.
- Provenance: `{"authority": "CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "authorization_scope": "ACCEPT_EXISTING_RECOMMENDED_OPTIONS_FOR_REMAINING_EXCEPTIONS", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `NORMAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Commerce Experience Platform tuân thủ:

- Configuration over Customization
```

Canonical source context:

```text
Commerce Experience Platform tuân thủ:

- Commerce First
- Configuration over Customization
```

### P2-CRIT-CL-011 — White-label by Default principle

- Classification: `HUMAN_RISK_DECISION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-009`.
- Common decision question: Is White-label by Default a core product delivery obligation at HIGH or a descriptive design principle at NORMAL?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `CONFIRM_HIGH`.
- Recommendation rationale: White-label behavior is central to the approved platform proposition, but the principle alone lacks a concrete runtime surface.
- Under-classification consequence: NORMAL may under-test tenant branding defaults and fallback; HIGH may over-interpret a broad principle without derived requirements.
- Acceptance-depth impact: HIGH adds a primary fallback/edge path; NORMAL retains a single observable conformance criterion.
- Confidence: `MEDIUM`.
- Selected option: `CONFIRM_HIGH`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `YES` | `YES` |
| `CONFIRM_NORMAL` | `CLASSIFY_AS_NORMAL` | `NORMAL` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-009 — BRD-UPDATE-01-R022

- Source: `docs/BRD/BRD-UPDATE-01.md`, `17. Business Principles`, `L904-L908`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `CONFIRM_HIGH`; confidence `MEDIUM`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: White-label behavior is central to the approved platform proposition, but the principle alone lacks a concrete runtime surface.
- Consequence of under-classification: NORMAL may under-test tenant branding defaults and fallback; HIGH may over-interpret a broad principle without derived requirements.
- Acceptance-depth impact: HIGH adds a primary fallback/edge path; NORMAL retains a single observable conformance criterion.
- Human options: `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_HIGH` (matches recommendation: `YES`).
- Decision basis: `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION`.
- Provenance: `{"authority": "CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "authorization_scope": "ACCEPT_EXISTING_RECOMMENDED_OPTIONS_FOR_REMAINING_EXCEPTIONS", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `HIGH`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Commerce Experience Platform tuân thủ:

- White-label by Default
```

Canonical source context:

```text
Commerce Experience Platform tuân thủ:

- Commerce First
- Configuration over Customization
- White-label by Default
```

### P2-CRIT-CL-012 — Publish in Minutes principle

- Classification: `HUMAN_RISK_DECISION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-010`.
- Common decision question: Is Publish in Minutes a HIGH core publishing workflow obligation or NORMAL product-positioning metadata?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-009`, `P2-DEC-010`.
- Recommended option: `CONFIRM_HIGH`.
- Recommendation rationale: Publishing speed affects a core storefront workflow, although the source provides no numeric threshold.
- Under-classification consequence: NORMAL could omit failed-publish and rollback evidence; HIGH without a clarified threshold could still create unverifiable acceptance.
- Acceptance-depth impact: HIGH requires expected publish plus primary failure/edge evidence; the later document correction must supply an observable budget.
- Confidence: `MEDIUM`.
- Selected option: `CONFIRM_HIGH`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `YES` | `YES` |
| `CONFIRM_NORMAL` | `CLASSIFY_AS_NORMAL` | `NORMAL` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-010 — BRD-UPDATE-01-R023

- Source: `docs/BRD/BRD-UPDATE-01.md`, `17. Business Principles`, `L904-L909`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `CONFIRM_HIGH`; confidence `MEDIUM`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Publishing speed affects a core storefront workflow, although the source provides no numeric threshold.
- Consequence of under-classification: NORMAL could omit failed-publish and rollback evidence; HIGH without a clarified threshold could still create unverifiable acceptance.
- Acceptance-depth impact: HIGH requires expected publish plus primary failure/edge evidence; the later document correction must supply an observable budget.
- Human options: `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_HIGH` (matches recommendation: `YES`).
- Decision basis: `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION`.
- Provenance: `{"authority": "CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "authorization_scope": "ACCEPT_EXISTING_RECOMMENDED_OPTIONS_FOR_REMAINING_EXCEPTIONS", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `HIGH`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Commerce Experience Platform tuân thủ:

- Publish in Minutes
```

Canonical source context:

```text
Commerce Experience Platform tuân thủ:

- Commerce First
- Configuration over Customization
- White-label by Default
- Publish in Minutes
```

### P2-CRIT-CL-013 — Multi-tenant principle

- Classification: `HUMAN_RISK_DECISION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-011`.
- Common decision question: Does Multi-tenant denote a CRITICAL tenant-isolation boundary or only a HIGH platform capability?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-001`, `P2-DEC-008`.
- Recommended option: `CONFIRM_CRITICAL`.
- Recommendation rationale: Tenant isolation is a security and data-integrity boundary, but the source statement names only the capability.
- Under-classification consequence: HIGH may omit cross-tenant negative and authorization evidence; CRITICAL may add meaning if isolation is not the intended contract.
- Acceptance-depth impact: CRITICAL requires fail-closed and authorization-boundary evidence; HIGH covers the principal tenant edge path.
- Confidence: `MEDIUM`.
- Selected option: `CONFIRM_CRITICAL`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_CRITICAL` | `CLASSIFY_AS_CRITICAL` | `CRITICAL` | `YES` | `YES` |
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-011 — BRD-UPDATE-01-R024

- Source: `docs/BRD/BRD-UPDATE-01.md`, `17. Business Principles`, `L904-L910`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `MEDIUM`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Tenant isolation is a security and data-integrity boundary, but the source statement names only the capability.
- Consequence of under-classification: HIGH may omit cross-tenant negative and authorization evidence; CRITICAL may add meaning if isolation is not the intended contract.
- Acceptance-depth impact: CRITICAL requires fail-closed and authorization-boundary evidence; HIGH covers the principal tenant edge path.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION`.
- Provenance: `{"authority": "CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "authorization_scope": "ACCEPT_EXISTING_RECOMMENDED_OPTIONS_FOR_REMAINING_EXCEPTIONS", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Commerce Experience Platform tuân thủ:

- Multi-tenant
```

Canonical source context:

```text
Commerce Experience Platform tuân thủ:

- Commerce First
- Configuration over Customization
- White-label by Default
- Publish in Minutes
- Multi-tenant
```

### P2-CRIT-CL-014 — Multi-brand and multi-language platform capabilities

- Classification: `HUMAN_RISK_DECISION`.
- Member count: `2`.
- Members: `P2-CRIT-EXC-012`, `P2-CRIT-EXC-013`.
- Common decision question: Are these core white-label delivery capabilities uniformly HIGH, or descriptive/presentation capabilities at NORMAL?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `CONFIRM_HIGH`.
- Recommendation rationale: Both capabilities materially shape storefront delivery across tenants while remaining outside direct financial or security boundaries.
- Under-classification consequence: NORMAL could omit inheritance, fallback, and cross-brand/language edge evidence.
- Acceptance-depth impact: HIGH requires expected resolution and the primary inheritance/fallback edge; NORMAL requires one observable criterion.
- Confidence: `MEDIUM`.
- Selected option: `CONFIRM_HIGH`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `YES` | `YES` |
| `CONFIRM_NORMAL` | `CLASSIFY_AS_NORMAL` | `NORMAL` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-012 — BRD-UPDATE-01-R025

- Source: `docs/BRD/BRD-UPDATE-01.md`, `17. Business Principles`, `L904-L911`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `CONFIRM_HIGH`; confidence `MEDIUM`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Both capabilities materially shape storefront delivery across tenants while remaining outside direct financial or security boundaries.
- Consequence of under-classification: NORMAL could omit inheritance, fallback, and cross-brand/language edge evidence.
- Acceptance-depth impact: HIGH requires expected resolution and the primary inheritance/fallback edge; NORMAL requires one observable criterion.
- Human options: `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_HIGH` (matches recommendation: `YES`).
- Decision basis: `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION`.
- Provenance: `{"authority": "CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "authorization_scope": "ACCEPT_EXISTING_RECOMMENDED_OPTIONS_FOR_REMAINING_EXCEPTIONS", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `HIGH`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Commerce Experience Platform tuân thủ:

- Multi-brand
```

Canonical source context:

```text
Commerce Experience Platform tuân thủ:

- Commerce First
- Configuration over Customization
- White-label by Default
- Publish in Minutes
- Multi-tenant
- Multi-brand
```

##### P2-CRIT-EXC-013 — BRD-UPDATE-01-R026

- Source: `docs/BRD/BRD-UPDATE-01.md`, `17. Business Principles`, `L904-L912`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `CONFIRM_HIGH`; confidence `MEDIUM`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Both capabilities materially shape storefront delivery across tenants while remaining outside direct financial or security boundaries.
- Consequence of under-classification: NORMAL could omit inheritance, fallback, and cross-brand/language edge evidence.
- Acceptance-depth impact: HIGH requires expected resolution and the primary inheritance/fallback edge; NORMAL requires one observable criterion.
- Human options: `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_HIGH` (matches recommendation: `YES`).
- Decision basis: `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION`.
- Provenance: `{"authority": "CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "authorization_scope": "ACCEPT_EXISTING_RECOMMENDED_OPTIONS_FOR_REMAINING_EXCEPTIONS", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `HIGH`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Commerce Experience Platform tuân thủ:

- Multi-language
```

Canonical source context:

```text
Commerce Experience Platform tuân thủ:

- Commerce First
- Configuration over Customization
- White-label by Default
- Publish in Minutes
- Multi-tenant
- Multi-brand
- Multi-language
```

### P2-CRIT-CL-015 — Multi-country principle

- Classification: `HUMAN_RISK_DECISION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-014`.
- Common decision question: Is Multi-country HIGH as a core platform capability, CRITICAL because it governs jurisdictional boundaries, or NORMAL as descriptive scope?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-010`.
- Recommended option: `CONFIRM_HIGH`.
- Recommendation rationale: The statement implies international delivery but does not itself define jurisdiction, privacy, currency, or compliance behavior.
- Under-classification consequence: A lower tier may miss country-specific failure paths; a CRITICAL tier may infer regulatory semantics not present in the source.
- Acceptance-depth impact: HIGH adds the primary country-resolution edge; CRITICAL additionally requires applicable fail-closed boundary evidence.
- Confidence: `LOW`.
- Selected option: `CONFIRM_HIGH`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_CRITICAL` | `CLASSIFY_AS_CRITICAL` | `CRITICAL` | `NO` | `NO` |
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `YES` | `YES` |
| `CONFIRM_NORMAL` | `CLASSIFY_AS_NORMAL` | `NORMAL` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-014 — BRD-UPDATE-01-R027

- Source: `docs/BRD/BRD-UPDATE-01.md`, `17. Business Principles`, `L904-L913`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `CONFIRM_HIGH`; confidence `LOW`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The statement implies international delivery but does not itself define jurisdiction, privacy, currency, or compliance behavior.
- Consequence of under-classification: A lower tier may miss country-specific failure paths; a CRITICAL tier may infer regulatory semantics not present in the source.
- Acceptance-depth impact: HIGH adds the primary country-resolution edge; CRITICAL additionally requires applicable fail-closed boundary evidence.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_HIGH` (matches recommendation: `YES`).
- Decision basis: `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION`.
- Provenance: `{"authority": "CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "authorization_scope": "ACCEPT_EXISTING_RECOMMENDED_OPTIONS_FOR_REMAINING_EXCEPTIONS", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `HIGH`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Commerce Experience Platform tuân thủ:

- Multi-country
```

Canonical source context:

```text
Commerce Experience Platform tuân thủ:

- Commerce First
- Configuration over Customization
- White-label by Default
- Publish in Minutes
- Multi-tenant
- Multi-brand
- Multi-language
- Multi-country
```

### P2-CRIT-CL-016 — Experience Driven principle

- Classification: `HUMAN_RISK_DECISION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-015`.
- Common decision question: Is Experience Driven an enforceable HIGH runtime/UX obligation or NORMAL descriptive governance?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `CONFIRM_NORMAL`.
- Recommendation rationale: The phrase is broad and does not identify a journey, state, or contract boundary.
- Under-classification consequence: If treated too lightly, concrete experience obligations may be missed; if treated as HIGH, acceptance must invent the missing meaning.
- Acceptance-depth impact: NORMAL permits one explicit conformance criterion; HIGH requires a journey failure path that the source does not currently name.
- Confidence: `LOW`.
- Selected option: `CONFIRM_NORMAL`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `NO` | `NO` |
| `CONFIRM_NORMAL` | `CLASSIFY_AS_NORMAL` | `NORMAL` | `YES` | `YES` |

#### Member records

##### P2-CRIT-EXC-015 — BRD-UPDATE-01-R029

- Source: `docs/BRD/BRD-UPDATE-01.md`, `17. Business Principles`, `L904-L915`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `CONFIRM_NORMAL`; confidence `LOW`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The phrase is broad and does not identify a journey, state, or contract boundary.
- Consequence of under-classification: If treated too lightly, concrete experience obligations may be missed; if treated as HIGH, acceptance must invent the missing meaning.
- Acceptance-depth impact: NORMAL permits one explicit conformance criterion; HIGH requires a journey failure path that the source does not currently name.
- Human options: `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_NORMAL` (matches recommendation: `YES`).
- Decision basis: `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION`.
- Provenance: `{"authority": "CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "authorization_scope": "ACCEPT_EXISTING_RECOMMENDED_OPTIONS_FOR_REMAINING_EXCEPTIONS", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `NORMAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Commerce Experience Platform tuân thủ:

- Experience Driven
```

Canonical source context:

```text
Commerce Experience Platform tuân thủ:

- Commerce First
- Configuration over Customization
- White-label by Default
- Publish in Minutes
- Multi-tenant
- Multi-brand
- Multi-language
- Multi-country
- API First
- Experience Driven
```

### P2-CRIT-CL-017 — White-label Website sales channel

- Classification: `RULE_APPLICATION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-018`.
- Common decision question: Should the concrete White-label Website sales-channel requirement remain HIGH?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `CONFIRM_HIGH`.
- Recommendation rationale: It is an explicit storefront/channel delivery surface covered by the HIGH portal/storefront rule.
- Under-classification consequence: NORMAL would under-test the primary channel workflow and its failure path.
- Acceptance-depth impact: HIGH requires the expected storefront path and the principal channel failure/edge path.
- Confidence: `HIGH`.
- Selected option: `CONFIRM_HIGH`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `YES` | `YES` |
| `CONFIRM_NORMAL` | `CLASSIFY_AS_NORMAL` | `NORMAL` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-018 — BRD-WS-01-R029

- Source: `docs/BRD/BRD-WS-01.md`, `9. Sales Channels`, `L164-L167`.
- Type/scope: `BUSINESS_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `CONFIRM_HIGH`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: It is an explicit storefront/channel delivery surface covered by the HIGH portal/storefront rule.
- Consequence of under-classification: NORMAL would under-test the primary channel workflow and its failure path.
- Acceptance-depth impact: HIGH requires the expected storefront path and the principal channel failure/edge path.
- Human options: `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_HIGH` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `HIGH`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Hệ thống phải hỗ trợ:

- White-label Website
```

Canonical source context:

```text
Hệ thống phải hỗ trợ:

- Direct Website
- White-label Website
```

### P2-CRIT-CL-018 — Pre-fulfillment commercial validation

- Classification: `RULE_APPLICATION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-019`.
- Common decision question: Should pre-fulfillment commercial validation remain CRITICAL?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-003`, `P2-DEC-010`.
- Recommended option: `CONFIRM_CRITICAL`.
- Recommendation rationale: The validation gates fulfillment against commercial state and protects pricing, allocation, and fulfillment integrity.
- Under-classification consequence: Under-classification could allow fulfillment after stale or inconsistent commercial state without fail-closed/recovery evidence.
- Acceptance-depth impact: CRITICAL requires positive, negative fail-closed, and applicable retry/concurrency/reconciliation evidence.
- Confidence: `HIGH`.
- Selected option: `CONFIRM_CRITICAL`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_CRITICAL` | `CLASSIFY_AS_CRITICAL` | `CRITICAL` | `YES` | `YES` |
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-019 — BRD-WS-05-R021

- Source: `docs/BRD/BRD-WS-05.md`, `20. Commercial Consistency Principle`, `L492-L494`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_RESERVATION_ALLOCATION_FULFILLMENT`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The validation gates fulfillment against commercial state and protects pricing, allocation, and fulfillment integrity.
- Consequence of under-classification: Under-classification could allow fulfillment after stale or inconsistent commercial state without fail-closed/recovery evidence.
- Acceptance-depth impact: CRITICAL requires positive, negative fail-closed, and applicable retry/concurrency/reconciliation evidence.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Trước khi Fulfillment, hệ thống bắt buộc thực hiện:

Pre-Fulfillment Commercial Validation.
```

Canonical source context:

```text
Trước khi Fulfillment, hệ thống bắt buộc thực hiện:

Pre-Fulfillment Commercial Validation.
```

### P2-CRIT-CL-019 — Identity, relationship, tenant, and published-rule boundaries

- Classification: `RULE_APPLICATION`.
- Member count: `4`.
- Members: `P2-CRIT-EXC-021`, `P2-CRIT-EXC-022`, `P2-CRIT-EXC-027`, `P2-CRIT-EXC-032`.
- Common decision question: Should all four explicit identity/authorization/isolation boundaries be CRITICAL?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-001`, `P2-DEC-008`.
- Recommended option: `CONFIRM_CRITICAL`.
- Recommendation rationale: Each member constrains identity ownership, relationship authority, tenant isolation, or the effect of identity on published business rules.
- Under-classification consequence: Under-classification can omit cross-tenant, unauthorized relationship, or identity-induced rule-change negative evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and authorization-boundary evidence wherever applicable.
- Confidence: `HIGH`.
- Selected option: `CONFIRM_CRITICAL`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_CRITICAL` | `CLASSIFY_AS_CRITICAL` | `CRITICAL` | `YES` | `YES` |
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-021 — BRD-WS-11-R002

- Source: `docs/BRD/BRD-WS-11.md`, `4. Enterprise Customer Principle`, `L108`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_IDENTITY_AUTH_PRIVILEGED_ACCESS`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Each member constrains identity ownership, relationship authority, tenant isolation, or the effect of identity on published business rules.
- Consequence of under-classification: Under-classification can omit cross-tenant, unauthorized relationship, or identity-induced rule-change negative evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and authorization-boundary evidence wherever applicable.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Customer Identity luôn thuộc YSim.
```

Canonical source context:

```text
Customer Identity luôn thuộc YSim.
```

##### P2-CRIT-EXC-022 — BRD-WS-11-R003

- Source: `docs/BRD/BRD-WS-11.md`, `4. Enterprise Customer Principle`, `L110`.
- Type/scope: `DESIGN_PRINCIPLE` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_CORE_COMMERCE_CUSTOMER_ORDER`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`, `NON_RUNTIME_CLASSIFICATION_WITH_RUNTIME_IMPACT`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Each member constrains identity ownership, relationship authority, tenant isolation, or the effect of identity on published business rules.
- Consequence of under-classification: Under-classification can omit cross-tenant, unauthorized relationship, or identity-induced rule-change negative evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and authorization-boundary evidence wherever applicable.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Organization chỉ được cấp quyền quản lý Relationship.
```

Canonical source context:

```text
Organization chỉ được cấp quyền quản lý Relationship.
```

##### P2-CRIT-EXC-027 — UXF-00-R021

- Source: `docs/UXF/UXF-00.md`, `19. Experience Runtime Goals`, `L582-L586`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_IDENTITY_AUTH_PRIVILEGED_ACCESS`.
- Exception trigger: `UX_CRITICAL_BOUNDARY_REQUIRES_JOURNEY_REVIEW`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Each member constrains identity ownership, relationship authority, tenant isolation, or the effect of identity on published business rules.
- Consequence of under-classification: Under-classification can omit cross-tenant, unauthorized relationship, or identity-induced rule-change negative evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and authorization-boundary evidence wherever applicable.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
The Experience Runtime must provide:

- Multi-tenant Isolation
```

Canonical source context:

```text
The Experience Runtime must provide:

- Dynamic Rendering
- White-label Support
- Multi-tenant Isolation
```

##### P2-CRIT-EXC-032 — UXF-04-R004

- Source: `docs/UXF/UXF-04.md`, `11. Identity Resolution`, `L331`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_IDENTITY_AUTH_PRIVILEGED_ACCESS`.
- Exception trigger: `UX_CRITICAL_BOUNDARY_REQUIRES_JOURNEY_REVIEW`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Each member constrains identity ownership, relationship authority, tenant isolation, or the effect of identity on published business rules.
- Consequence of under-classification: Under-classification can omit cross-tenant, unauthorized relationship, or identity-induced rule-change negative evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and authorization-boundary evidence wherever applicable.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Identity never changes published business rules.
```

Canonical source context:

```text
Identity never changes published business rules.
```

### P2-CRIT-CL-020 — Accessibility safeguards

- Classification: `RULE_APPLICATION`.
- Member count: `2`.
- Members: `P2-CRIT-EXC-029`, `P2-CRIT-EXC-031`.
- Common decision question: Should high-contrast support and the prohibition on disabling accessibility remain HIGH?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-009`.
- Recommended option: `CONFIRM_HIGH`.
- Recommendation rationale: Both are enforceable accessibility safeguards across experience surfaces and critical journeys.
- Under-classification consequence: NORMAL could reduce coverage to a superficial positive check and omit theme-based regression/failure evidence.
- Acceptance-depth impact: HIGH requires expected accessibility behavior and the primary theme/contrast failure path.
- Confidence: `HIGH`.
- Selected option: `CONFIRM_HIGH`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `YES` | `YES` |
| `CONFIRM_NORMAL` | `CLASSIFY_AS_NORMAL` | `NORMAL` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-029 — UXF-01-R009

- Source: `docs/UXF/UXF-01.md`, `12. Accessibility`, `L624-L629`.
- Type/scope: `ACCESSIBILITY_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_RUNTIME_CONTRACT_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `CONFIRM_HIGH`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Both are enforceable accessibility safeguards across experience surfaces and critical journeys.
- Consequence of under-classification: NORMAL could reduce coverage to a superficial positive check and omit theme-based regression/failure evidence.
- Acceptance-depth impact: HIGH requires expected accessibility behavior and the primary theme/contrast failure path.
- Human options: `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_HIGH` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `HIGH`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Every experience should support:

- High contrast themes
```

Canonical source context:

```text
Every experience should support:

- Keyboard navigation
- Screen readers
- Responsive layouts
- High contrast themes
```

##### P2-CRIT-EXC-031 — UXF-02-R009

- Source: `docs/UXF/UXF-02.md`, `18. Design Accessibility`, `L540`.
- Type/scope: `ACCESSIBILITY_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_RUNTIME_CONTRACT_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `CONFIRM_HIGH`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Both are enforceable accessibility safeguards across experience surfaces and critical journeys.
- Consequence of under-classification: NORMAL could reduce coverage to a superficial positive check and omit theme-based regression/failure evidence.
- Acceptance-depth impact: HIGH requires expected accessibility behavior and the primary theme/contrast failure path.
- Human options: `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_HIGH` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `HIGH`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Accessibility cannot be disabled by Themes.
```

Canonical source context:

```text
Accessibility cannot be disabled by Themes.
```

### P2-CRIT-CL-021 — White-label no-source-code statements typed as UX requirements

- Classification: `CLASSIFICATION_OR_EXTRACTION_DEFECT`.
- Member count: `3`.
- Members: `P2-CRIT-EXC-024`, `P2-CRIT-EXC-033`, `P2-CRIT-EXC-044`.
- Common decision question: Should these repeated architecture/principle statements be reclassified before criticality is decided?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `ROUTE_TO_REMEDIATION`.
- Recommendation rationale: The records state an architecture/design principle and occur in principle/architecture sections, but are typed as UX_REQUIREMENT.
- Under-classification consequence: An ordinary HIGH/NORMAL override would preserve a suspect rule input and could duplicate one semantic obligation three times.
- Acceptance-depth impact: Reclassify/reconcile identity first, then derive acceptance depth from the surviving canonical obligation.
- Confidence: `HIGH`.
- Selected option: `ROUTE_TO_REMEDIATION`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `ROUTE_TO_REMEDIATION` | `REMEDIATE_RULE_INPUT_BEFORE_CRITICALITY` | `KEEP_CURRENT` | `YES` | `YES` |
| `REJECT_DEFECT_AND_KEEP_PROVISIONAL` | `REJECT_DEFECT_FINDING` | `KEEP_CURRENT` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-024 — UXF-00-R016

- Source: `docs/UXF/UXF-00.md`, `17. White-label Principle`, `L542`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_UX_JOURNEY_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `ROUTE_TO_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The records state an architecture/design principle and occur in principle/architecture sections, but are typed as UX_REQUIREMENT.
- Consequence of under-classification: An ordinary HIGH/NORMAL override would preserve a suspect rule input and could duplicate one semantic obligation three times.
- Acceptance-depth impact: Reclassify/reconcile identity first, then derive acceptance depth from the surviving canonical obligation.
- Human options: `ROUTE_TO_REMEDIATION`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `ROUTE_TO_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
White-label customization must never require source code modification.
```

Canonical source context:

```text
White-label customization must never require source code modification.
```

##### P2-CRIT-EXC-033 — UXF-04-R006

- Source: `docs/UXF/UXF-04.md`, `17. White-label Architecture`, `L512`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_UX_JOURNEY_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `ROUTE_TO_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The records state an architecture/design principle and occur in principle/architecture sections, but are typed as UX_REQUIREMENT.
- Consequence of under-classification: An ordinary HIGH/NORMAL override would preserve a suspect rule input and could duplicate one semantic obligation three times.
- Acceptance-depth impact: Reclassify/reconcile identity first, then derive acceptance depth from the surviving canonical obligation.
- Human options: `ROUTE_TO_REMEDIATION`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `ROUTE_TO_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
White-label customization never requires code modification.
```

Canonical source context:

```text
White-label customization never requires code modification.
```

##### P2-CRIT-EXC-044 — UXF-408

- Source: `docs/UXF/UXF-04.md`, `24. Architectural Principles > UXF-408`, `L660-L663`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_UX_JOURNEY_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `ROUTE_TO_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The records state an architecture/design principle and occur in principle/architecture sections, but are typed as UX_REQUIREMENT.
- Consequence of under-classification: An ordinary HIGH/NORMAL override would preserve a suspect rule input and could duplicate one semantic obligation three times.
- Acceptance-depth impact: Reclassify/reconcile identity first, then derive acceptance depth from the surviving canonical obligation.
- Human options: `ROUTE_TO_REMEDIATION`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `ROUTE_TO_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
White-label customization requires no source code changes.
```

Canonical source context:

```text
### UXF-408

White-label customization requires no source code changes.

```

### P2-CRIT-CL-022 — Immutable published runtime configuration

- Classification: `RULE_APPLICATION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-025`.
- Common decision question: Should immutable published runtime configuration remain CRITICAL?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-010`.
- Recommended option: `CONFIRM_CRITICAL`.
- Recommendation rationale: The requirement protects production configuration and runtime data integrity.
- Under-classification consequence: Under-classification could omit mutable-draft rejection, rollback, concurrency, and recovery evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and applicable recovery/concurrency evidence in addition to the positive path.
- Confidence: `HIGH`.
- Selected option: `CONFIRM_CRITICAL`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_CRITICAL` | `CLASSIFY_AS_CRITICAL` | `CRITICAL` | `YES` | `YES` |
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-025 — UXF-00-R017

- Source: `docs/UXF/UXF-00.md`, `18. Published Experience Snapshot`, `L548`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_AUDIT_RECOVERY_DATA_INTEGRITY`.
- Exception trigger: `UX_CRITICAL_BOUNDARY_REQUIRES_JOURNEY_REVIEW`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The requirement protects production configuration and runtime data integrity.
- Consequence of under-classification: Under-classification could omit mutable-draft rejection, rollback, concurrency, and recovery evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and applicable recovery/concurrency evidence in addition to the positive path.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Runtime rendering must use immutable published configurations.
```

Canonical source context:

```text
Runtime rendering must use immutable published configurations.
```

### P2-CRIT-CL-023 — Runtime white-label support

- Classification: `RULE_APPLICATION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-026`.
- Common decision question: Should explicit Experience Runtime white-label support remain HIGH?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `CONFIRM_HIGH`.
- Recommendation rationale: This is a runtime delivery capability on the storefront/experience surface, not only descriptive governance.
- Under-classification consequence: NORMAL could omit tenant-resolution and fallback failure evidence.
- Acceptance-depth impact: HIGH requires the expected runtime path and the principal tenant/fallback edge path.
- Confidence: `HIGH`.
- Selected option: `CONFIRM_HIGH`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `YES` | `YES` |
| `CONFIRM_NORMAL` | `CLASSIFY_AS_NORMAL` | `NORMAL` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-026 — UXF-00-R020

- Source: `docs/UXF/UXF-00.md`, `19. Experience Runtime Goals`, `L582-L585`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_UX_JOURNEY_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `CONFIRM_HIGH`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: This is a runtime delivery capability on the storefront/experience surface, not only descriptive governance.
- Consequence of under-classification: NORMAL could omit tenant-resolution and fallback failure evidence.
- Acceptance-depth impact: HIGH requires the expected runtime path and the principal tenant/fallback edge path.
- Human options: `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_HIGH` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `HIGH`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
The Experience Runtime must provide:

- White-label Support
```

Canonical source context:

```text
The Experience Runtime must provide:

- Dynamic Rendering
- White-label Support
```

### P2-CRIT-CL-024 — Exclusive Allocation supplier selection

- Classification: `RULE_APPLICATION`.
- Member count: `2`.
- Members: `P2-CRIT-EXC-028`, `P2-CRIT-EXC-046`.
- Common decision question: Should both equivalent Allocation ownership statements remain CRITICAL pending later identity reconciliation?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-007`.
- Recommended option: `CONFIRM_CRITICAL`.
- Recommendation rationale: P2-DEC-007 explicitly assigns supplier selection exclusively to Allocation; violating the boundary affects procurement and fulfillment integrity.
- Under-classification consequence: Under-classification could omit direct-supplier bypass, unauthorized routing, and allocation recovery evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and applicable recovery/idempotency evidence at the allocation boundary.
- Confidence: `HIGH`.
- Selected option: `CONFIRM_CRITICAL`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_CRITICAL` | `CLASSIFY_AS_CRITICAL` | `CRITICAL` | `YES` | `YES` |
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-028 — UXF-005

- Source: `docs/UXF/UXF-00.md`, `20. Architectural Principles > UXF-005`, `L627-L630`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_RESERVATION_ALLOCATION_FULFILLMENT`.
- Exception trigger: `UX_CRITICAL_BOUNDARY_REQUIRES_JOURNEY_REVIEW`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: P2-DEC-007 explicitly assigns supplier selection exclusively to Allocation; violating the boundary affects procurement and fulfillment integrity.
- Consequence of under-classification: Under-classification could omit direct-supplier bypass, unauthorized routing, and allocation recovery evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and applicable recovery/idempotency evidence at the allocation boundary.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Allocation is the only capability allowed to select suppliers.
```

Canonical source context:

```text
### UXF-005

Allocation is the only capability allowed to select suppliers.

```

##### P2-CRIT-EXC-046 — UXF-506

- Source: `docs/UXF/UXF-05.md`, `24. Architectural Principles > UXF-506`, `L673-L676`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_RESERVATION_ALLOCATION_FULFILLMENT`.
- Exception trigger: `UX_CRITICAL_BOUNDARY_REQUIRES_JOURNEY_REVIEW`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: P2-DEC-007 explicitly assigns supplier selection exclusively to Allocation; violating the boundary affects procurement and fulfillment integrity.
- Consequence of under-classification: Under-classification could omit direct-supplier bypass, unauthorized routing, and allocation recovery evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and applicable recovery/idempotency evidence at the allocation boundary.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Allocation is the only capability allowed to select suppliers.
```

Canonical source context:

```text
### UXF-506

Allocation is the only capability allowed to select suppliers.

```

### P2-CRIT-CL-025 — Theme override granularity

- Classification: `RULE_APPLICATION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-030`.
- Common decision question: Is overriding only required theme properties a NORMAL presentation/configuration rule or a HIGH runtime contract?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `CONFIRM_NORMAL`.
- Recommendation rationale: The statement controls non-critical theme inheritance and does not itself govern accessibility or production integrity.
- Under-classification consequence: If hidden runtime integrity semantics exist, NORMAL may miss fallback/regression evidence; none are explicit here.
- Acceptance-depth impact: NORMAL requires one observable inheritance criterion; HIGH would add a primary override/fallback failure path.
- Confidence: `MEDIUM`.
- Selected option: `CONFIRM_NORMAL`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `NO` | `NO` |
| `CONFIRM_NORMAL` | `CLASSIFY_AS_NORMAL` | `NORMAL` | `YES` | `YES` |

#### Member records

##### P2-CRIT-EXC-030 — UXF-02-R001

- Source: `docs/UXF/UXF-02.md`, `9. Theme Inheritance`, `L302`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_UX_JOURNEY_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `CONFIRM_NORMAL`; confidence `MEDIUM`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The statement controls non-critical theme inheritance and does not itself govern accessibility or production integrity.
- Consequence of under-classification: If hidden runtime integrity semantics exist, NORMAL may miss fallback/regression evidence; none are explicit here.
- Acceptance-depth impact: NORMAL requires one observable inheritance criterion; HIGH would add a primary override/fallback failure path.
- Human options: `CONFIRM_HIGH`, `CONFIRM_NORMAL`.
- Selected disposition: `CONFIRM_NORMAL` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `NORMAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Each level overrides only required properties.
```

Canonical source context:

```text
Each level overrides only required properties.
```

### P2-CRIT-CL-026 — Theme model principles typed as UX requirements

- Classification: `CLASSIFICATION_OR_EXTRACTION_DEFECT`.
- Member count: `3`.
- Members: `P2-CRIT-EXC-039`, `P2-CRIT-EXC-040`, `P2-CRIT-EXC-041`.
- Common decision question: Should the Theme/Experience Profile model statements be reclassified as DESIGN_PRINCIPLE before tiering?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `ROUTE_TO_REMEDIATION`.
- Recommendation rationale: All three records are in a Design Principles section and describe the configuration model rather than a user outcome.
- Under-classification consequence: An ordinary tier override can conceal a type mismatch and lead to duplicated or implementation-shaped UX acceptance.
- Acceptance-depth impact: Correct the classification, then decide whether the resulting design-principle evidence is NORMAL or linked to a stronger runtime requirement.
- Confidence: `HIGH`.
- Selected option: `ROUTE_TO_REMEDIATION`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `ROUTE_TO_REMEDIATION` | `REMEDIATE_RULE_INPUT_BEFORE_CRITICALITY` | `KEEP_CURRENT` | `YES` | `YES` |
| `REJECT_DEFECT_AND_KEEP_PROVISIONAL` | `REJECT_DEFECT_FINDING` | `KEEP_CURRENT` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-039 — UXF-202

- Source: `docs/UXF/UXF-02.md`, `20. Design Principles > UXF-202`, `L568-L571`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_UX_JOURNEY_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `ROUTE_TO_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: All three records are in a Design Principles section and describe the configuration model rather than a user outcome.
- Consequence of under-classification: An ordinary tier override can conceal a type mismatch and lead to duplicated or implementation-shaped UX acceptance.
- Acceptance-depth impact: Correct the classification, then decide whether the resulting design-principle evidence is NORMAL or linked to a stronger runtime requirement.
- Human options: `ROUTE_TO_REMEDIATION`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `ROUTE_TO_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Themes are configuration objects.
```

Canonical source context:

```text
### UXF-202

Themes are configuration objects.

```

##### P2-CRIT-EXC-040 — UXF-203

- Source: `docs/UXF/UXF-02.md`, `20. Design Principles > UXF-203`, `L574-L577`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_UX_JOURNEY_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `ROUTE_TO_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: All three records are in a Design Principles section and describe the configuration model rather than a user outcome.
- Consequence of under-classification: An ordinary tier override can conceal a type mismatch and lead to duplicated or implementation-shaped UX acceptance.
- Acceptance-depth impact: Correct the classification, then decide whether the resulting design-principle evidence is NORMAL or linked to a stronger runtime requirement.
- Human options: `ROUTE_TO_REMEDIATION`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `ROUTE_TO_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Experience Profiles extend Themes.
```

Canonical source context:

```text
### UXF-203

Experience Profiles extend Themes.

```

##### P2-CRIT-EXC-041 — UXF-204

- Source: `docs/UXF/UXF-02.md`, `20. Design Principles > UXF-204`, `L580-L583`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_UX_JOURNEY_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `ROUTE_TO_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: All three records are in a Design Principles section and describe the configuration model rather than a user outcome.
- Consequence of under-classification: An ordinary tier override can conceal a type mismatch and lead to duplicated or implementation-shaped UX acceptance.
- Acceptance-depth impact: Correct the classification, then decide whether the resulting design-principle evidence is NORMAL or linked to a stronger runtime requirement.
- Human options: `ROUTE_TO_REMEDIATION`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `ROUTE_TO_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Themes support inheritance.
```

Canonical source context:

```text
### UXF-204

Themes support inheritance.

```

### P2-CRIT-CL-027 — Storefront pricing ownership boundary

- Classification: `RULE_APPLICATION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-034`.
- Common decision question: Should the prohibition on Storefront owning Pricing remain CRITICAL?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `CONFIRM_CRITICAL`.
- Recommendation rationale: The boundary prevents presentation code from controlling pricing integrity.
- Under-classification consequence: Under-classification could omit tampered-price rejection and fail-closed evidence.
- Acceptance-depth impact: CRITICAL requires negative pricing-integrity evidence in addition to the expected path.
- Confidence: `HIGH`.
- Selected option: `CONFIRM_CRITICAL`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_CRITICAL` | `CLASSIFY_AS_CRITICAL` | `CRITICAL` | `YES` | `YES` |
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-034 — UXF-05-R005

- Source: `docs/UXF/UXF-05.md`, `7. Storefront Responsibilities`, `L158-L161`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_FINANCIAL_PRICING_INTEGRITY`.
- Exception trigger: `UX_CRITICAL_BOUNDARY_REQUIRES_JOURNEY_REVIEW`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The boundary prevents presentation code from controlling pricing integrity.
- Consequence of under-classification: Under-classification could omit tampered-price rejection and fail-closed evidence.
- Acceptance-depth impact: CRITICAL requires negative pricing-integrity evidence in addition to the expected path.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Storefronts never own:

- Pricing
```

Canonical source context:

```text
Storefronts never own:

- Products
- Pricing
```

### P2-CRIT-CL-028 — Storefront allocation ownership boundary

- Classification: `RULE_APPLICATION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-035`.
- Common decision question: Should the prohibition on Storefront owning Allocation remain CRITICAL?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-007`.
- Recommended option: `CONFIRM_CRITICAL`.
- Recommendation rationale: The boundary preserves canonical allocation ownership and prevents client-side supplier routing.
- Under-classification consequence: Under-classification could omit routing bypass, duplicate allocation, and recovery evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and applicable recovery/idempotency evidence.
- Confidence: `HIGH`.
- Selected option: `CONFIRM_CRITICAL`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_CRITICAL` | `CLASSIFY_AS_CRITICAL` | `CRITICAL` | `YES` | `YES` |
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-035 — UXF-05-R008

- Source: `docs/UXF/UXF-05.md`, `7. Storefront Responsibilities`, `L158-L164`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_RESERVATION_ALLOCATION_FULFILLMENT`.
- Exception trigger: `UX_CRITICAL_BOUNDARY_REQUIRES_JOURNEY_REVIEW`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The boundary preserves canonical allocation ownership and prevents client-side supplier routing.
- Consequence of under-classification: Under-classification could omit routing bypass, duplicate allocation, and recovery evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and applicable recovery/idempotency evidence.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Storefronts never own:

- Allocation
```

Canonical source context:

```text
Storefronts never own:

- Products
- Pricing
- Supplier
- Inventory
- Allocation
```

### P2-CRIT-CL-029 — Storefront fulfillment ownership boundary

- Classification: `RULE_APPLICATION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-036`.
- Common decision question: Should the prohibition on Storefront owning Fulfillment remain CRITICAL?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-003`, `P2-DEC-010`.
- Recommended option: `CONFIRM_CRITICAL`.
- Recommendation rationale: The boundary prevents the experience layer from initiating or controlling fulfillment state.
- Under-classification consequence: Under-classification could omit duplicate fulfillment, ambiguous outcome, and manual-recovery evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and applicable recovery/idempotency/concurrency evidence.
- Confidence: `HIGH`.
- Selected option: `CONFIRM_CRITICAL`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_CRITICAL` | `CLASSIFY_AS_CRITICAL` | `CRITICAL` | `YES` | `YES` |
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-036 — UXF-05-R009

- Source: `docs/UXF/UXF-05.md`, `7. Storefront Responsibilities`, `L158-L165`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_RESERVATION_ALLOCATION_FULFILLMENT`.
- Exception trigger: `UX_CRITICAL_BOUNDARY_REQUIRES_JOURNEY_REVIEW`.
- Preliminary recommendation: `CONFIRM_CRITICAL`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The boundary prevents the experience layer from initiating or controlling fulfillment state.
- Consequence of under-classification: Under-classification could omit duplicate fulfillment, ambiguous outcome, and manual-recovery evidence.
- Acceptance-depth impact: CRITICAL requires fail-closed and applicable recovery/idempotency/concurrency evidence.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_CRITICAL` (matches recommendation: `YES`).
- Decision basis: `CRITICALITY_RULE_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `CRITICAL`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Storefronts never own:

- Fulfillment
```

Canonical source context:

```text
Storefronts never own:

- Products
- Pricing
- Supplier
- Inventory
- Allocation
- Fulfillment
```

### P2-CRIT-CL-030 — Allocation invisibility wording and UX classification

- Classification: `CLASSIFICATION_OR_EXTRACTION_DEFECT`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-037`.
- Common decision question: Must the statement be clarified and reclassified before deciding whether its tier is CRITICAL or HIGH?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-007`.
- Recommended option: `ROUTE_TO_REMEDIATION`.
- Recommendation rationale: The wording can mean hiding internal allocation mechanics, but P2-DEC-007 permits controlled read-only provider/brand disclosure; the UX_REQUIREMENT type is also suspect for an architecture boundary.
- Under-classification consequence: Tiering the ambiguous word 'invisible' can either suppress required disclosure or weaken allocation-decoupling evidence.
- Acceptance-depth impact: Clarify technical invisibility versus disclosure, then link acceptance to the correct architecture and journey surfaces.
- Confidence: `HIGH`.
- Selected option: `ROUTE_TO_REMEDIATION`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `ROUTE_TO_REMEDIATION` | `REMEDIATE_RULE_INPUT_BEFORE_CRITICALITY` | `KEEP_CURRENT` | `YES` | `YES` |
| `REJECT_DEFECT_AND_KEEP_PROVISIONAL` | `REJECT_DEFECT_FINDING` | `KEEP_CURRENT` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-037 — UXF-106

- Source: `docs/UXF/UXF-01.md`, `15. Experience Principles > UXF-106`, `L709-L712`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_RESERVATION_ALLOCATION_FULFILLMENT`.
- Exception trigger: `UX_CRITICAL_BOUNDARY_REQUIRES_JOURNEY_REVIEW`.
- Preliminary recommendation: `ROUTE_TO_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The wording can mean hiding internal allocation mechanics, but P2-DEC-007 permits controlled read-only provider/brand disclosure; the UX_REQUIREMENT type is also suspect for an architecture boundary.
- Consequence of under-classification: Tiering the ambiguous word 'invisible' can either suppress required disclosure or weaken allocation-decoupling evidence.
- Acceptance-depth impact: Clarify technical invisibility versus disclosure, then link acceptance to the correct architecture and journey surfaces.
- Human options: `ROUTE_TO_REMEDIATION`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `ROUTE_TO_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Allocation remains invisible within customer journeys.
```

Canonical source context:

```text
### UXF-106

Allocation remains invisible within customer journeys.

```

### P2-CRIT-CL-031 — Presentation/business separation statements typed as UX requirements

- Classification: `CLASSIFICATION_OR_EXTRACTION_DEFECT`.
- Member count: `3`.
- Members: `P2-CRIT-EXC-038`, `P2-CRIT-EXC-042`, `P2-CRIT-EXC-045`.
- Common decision question: Should these ownership/separation statements be reclassified as DESIGN_PRINCIPLE before tiering?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `NONE_SPECIFIC`.
- Recommended option: `ROUTE_TO_REMEDIATION`.
- Recommendation rationale: The statements define architecture ownership and presentation separation rather than direct journey outcomes.
- Under-classification consequence: An ordinary override may preserve wrong acceptance abstraction and duplicate the same separation contract.
- Acceptance-depth impact: Reclassify/reconcile first; then attach observable UX acceptance only through impacted journeys or runtime contracts.
- Confidence: `HIGH`.
- Selected option: `ROUTE_TO_REMEDIATION`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `ROUTE_TO_REMEDIATION` | `REMEDIATE_RULE_INPUT_BEFORE_CRITICALITY` | `KEEP_CURRENT` | `YES` | `YES` |
| `REJECT_DEFECT_AND_KEEP_PROVISIONAL` | `REJECT_DEFECT_FINDING` | `KEEP_CURRENT` | `NO` | `NO` |

#### Member records

##### P2-CRIT-EXC-038 — UXF-110

- Source: `docs/UXF/UXF-01.md`, `15. Experience Principles > UXF-110`, `L733-L736`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_UX_JOURNEY_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `ROUTE_TO_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The statements define architecture ownership and presentation separation rather than direct journey outcomes.
- Consequence of under-classification: An ordinary override may preserve wrong acceptance abstraction and duplicate the same separation contract.
- Acceptance-depth impact: Reclassify/reconcile first; then attach observable UX acceptance only through impacted journeys or runtime contracts.
- Human options: `ROUTE_TO_REMEDIATION`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `ROUTE_TO_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Business capabilities are independent from presentation.
```

Canonical source context:

```text
### UXF-110

Business capabilities are independent from presentation.

```

##### P2-CRIT-EXC-042 — UXF-208

- Source: `docs/UXF/UXF-02.md`, `20. Design Principles > UXF-208`, `L604-L607`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_UX_JOURNEY_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `ROUTE_TO_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The statements define architecture ownership and presentation separation rather than direct journey outcomes.
- Consequence of under-classification: An ordinary override may preserve wrong acceptance abstraction and duplicate the same separation contract.
- Acceptance-depth impact: Reclassify/reconcile first; then attach observable UX acceptance only through impacted journeys or runtime contracts.
- Human options: `ROUTE_TO_REMEDIATION`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `ROUTE_TO_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Business behavior is independent from presentation.
```

Canonical source context:

```text
### UXF-208

Business behavior is independent from presentation.

```

##### P2-CRIT-EXC-045 — UXF-501

- Source: `docs/UXF/UXF-05.md`, `24. Architectural Principles > UXF-501`, `L643-L646`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `HIGH` via `HIGH_UX_JOURNEY_TYPE`.
- Exception trigger: `CROSS_TIER_RULE_MATCH`.
- Preliminary recommendation: `ROUTE_TO_REMEDIATION`; confidence `HIGH`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: The statements define architecture ownership and presentation separation rather than direct journey outcomes.
- Consequence of under-classification: An ordinary override may preserve wrong acceptance abstraction and duplicate the same separation contract.
- Acceptance-depth impact: Reclassify/reconcile first; then attach observable UX acceptance only through impacted journeys or runtime contracts.
- Human options: `ROUTE_TO_REMEDIATION`, `REJECT_DEFECT_AND_KEEP_PROVISIONAL`.
- Selected disposition: `ROUTE_TO_REMEDIATION` (matches recommendation: `YES`).
- Decision basis: `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION`.
- Provenance: `{"authority": "RECORDED_RECOMMENDATION_APPLIED_UNDER_CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `REMEDIATION_REQUIRED`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Experience Runtime owns presentation.
```

Canonical source context:

```text
### UXF-501

Experience Runtime owns presentation.

```

### P2-CRIT-CL-032 — Storefront identity versus authentication identity

- Classification: `HUMAN_RISK_DECISION`.
- Member count: `1`.
- Members: `P2-CRIT-EXC-043`.
- Common decision question: Does domain-to-storefront identity resolution require CRITICAL tenant-isolation evidence, or HIGH storefront-routing evidence?
- Uniform resolution safe: `YES`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Approved decision provenance: `P2-DEC-001`, `P2-DEC-008`.
- Recommended option: `CONFIRM_HIGH`.
- Recommendation rationale: Here 'identity' denotes storefront selection, not an authentication principal; however an incorrect domain binding could cross tenant boundaries.
- Under-classification consequence: HIGH may omit cross-tenant fail-closed checks if domain binding is security-enforcing; CRITICAL may conflate brand routing with authentication identity.
- Acceptance-depth impact: HIGH covers expected routing and the primary invalid-domain edge; CRITICAL adds explicit tenant/authorization boundary evidence.
- Confidence: `MEDIUM`.
- Selected option: `CONFIRM_HIGH`.
- Remediation contract: `NONE`.

| Option | Decision | Target | Recommended | Selected |
|---|---|---|---|---|
| `CONFIRM_CRITICAL` | `CLASSIFY_AS_CRITICAL` | `CRITICAL` | `NO` | `NO` |
| `CONFIRM_HIGH` | `CLASSIFY_AS_HIGH` | `HIGH` | `YES` | `YES` |

#### Member records

##### P2-CRIT-EXC-043 — UXF-402

- Source: `docs/UXF/UXF-04.md`, `24. Architectural Principles > UXF-402`, `L624-L627`.
- Type/scope: `UX_REQUIREMENT` / `V2.3_ACTIVE`.
- Rule-derived criticality: `CRITICAL` via `CRITICAL_IDENTITY_AUTH_PRIVILEGED_ACCESS`.
- Exception trigger: `UX_CRITICAL_BOUNDARY_REQUIRES_JOURNEY_REVIEW`.
- Preliminary recommendation: `CONFIRM_HIGH`; confidence `MEDIUM`.
- Review status: `DISPOSITIONED_PENDING_PACK_APPROVAL`.
- Risk rationale: Here 'identity' denotes storefront selection, not an authentication principal; however an incorrect domain binding could cross tenant boundaries.
- Consequence of under-classification: HIGH may omit cross-tenant fail-closed checks if domain binding is security-enforcing; CRITICAL may conflate brand routing with authentication identity.
- Acceptance-depth impact: HIGH covers expected routing and the primary invalid-domain edge; CRITICAL adds explicit tenant/authorization boundary evidence.
- Human options: `CONFIRM_CRITICAL`, `CONFIRM_HIGH`.
- Selected disposition: `CONFIRM_HIGH` (matches recommendation: `YES`).
- Decision basis: `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION`.
- Provenance: `{"authority": "CONTROLLED_FAST_TRACK", "authorization_date": "2026-07-15", "authorization_scope": "ACCEPT_EXISTING_RECOMMENDED_OPTIONS_FOR_REMAINING_EXCEPTIONS", "source_review": "V23-P2B-CRITICALITY-REVIEW-R2"}`.
- Effective tier/remediation: `HIGH`.
- Source application: `NOT_YET_APPLIED`; pack approval: `PENDING`.
- Source-exception status: `OPEN`; source-resolution claim: `NO`.

Exact source statement:

```text
Domains determine storefront identity.
```

Canonical source context:

```text
### UXF-402

Domains determine storefront identity.

```

## 9. Complete disposition index

| Exception | Requirement | Classification | Current | Selected disposition | Effective outcome | Basis | Source application | Source status |
|---|---|---|---|---|---|---|---|---|
| `P2-CRIT-EXC-001` | `BD-04-007` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `ROUTE_TO_SCOPE_REMEDIATION` | `REMEDIATION_REQUIRED` | `EARLIER_EXPLICIT_HUMAN_DECISION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-002` | `BD-14-022` | `HUMAN_RISK_DECISION` | `HIGH` | `CONFIRM_CRITICAL` | `CRITICAL` | `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-003` | `BRD-CAP-INDEX-R007` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `APPROVED_SCOPE_PROMOTION_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-004` | `BRD-EVENT-INDEX-R002` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-005` | `BRD-UPDATE-01-R010` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `COMPOSITE_PARENT_WITH_ATOMIC_CHILD_RECONCILIATION` | `REMEDIATION_REQUIRED` | `EARLIER_EXPLICIT_HUMAN_DECISION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-006` | `BRD-UPDATE-01-R018` | `HUMAN_RISK_DECISION` | `CRITICAL` | `CONFIRM_HIGH` | `HIGH` | `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-007` | `BRD-UPDATE-01-R020` | `RULE_APPLICATION` | `HIGH` | `CONFIRM_HIGH` | `HIGH` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-008` | `BRD-UPDATE-01-R021` | `HUMAN_RISK_DECISION` | `HIGH` | `CONFIRM_NORMAL` | `NORMAL` | `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-009` | `BRD-UPDATE-01-R022` | `HUMAN_RISK_DECISION` | `HIGH` | `CONFIRM_HIGH` | `HIGH` | `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-010` | `BRD-UPDATE-01-R023` | `HUMAN_RISK_DECISION` | `HIGH` | `CONFIRM_HIGH` | `HIGH` | `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-011` | `BRD-UPDATE-01-R024` | `HUMAN_RISK_DECISION` | `HIGH` | `CONFIRM_CRITICAL` | `CRITICAL` | `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-012` | `BRD-UPDATE-01-R025` | `HUMAN_RISK_DECISION` | `HIGH` | `CONFIRM_HIGH` | `HIGH` | `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-013` | `BRD-UPDATE-01-R026` | `HUMAN_RISK_DECISION` | `HIGH` | `CONFIRM_HIGH` | `HIGH` | `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-014` | `BRD-UPDATE-01-R027` | `HUMAN_RISK_DECISION` | `HIGH` | `CONFIRM_HIGH` | `HIGH` | `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-015` | `BRD-UPDATE-01-R029` | `HUMAN_RISK_DECISION` | `HIGH` | `CONFIRM_NORMAL` | `NORMAL` | `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-016` | `BRD-WS-01-R001` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `ROUTE_TO_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-017` | `BRD-WS-01-R004` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `ROUTE_TO_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-018` | `BRD-WS-01-R029` | `RULE_APPLICATION` | `HIGH` | `CONFIRM_HIGH` | `HIGH` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-019` | `BRD-WS-05-R021` | `RULE_APPLICATION` | `CRITICAL` | `CONFIRM_CRITICAL` | `CRITICAL` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-020` | `BRD-WS-08-R012` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `CRITICAL` | `APPROVED_SCOPE_PROMOTION_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-021` | `BRD-WS-11-R002` | `RULE_APPLICATION` | `CRITICAL` | `CONFIRM_CRITICAL` | `CRITICAL` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-022` | `BRD-WS-11-R003` | `RULE_APPLICATION` | `HIGH` | `CONFIRM_CRITICAL` | `CRITICAL` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-023` | `BRD-WS-17-R013` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `COMPOSITE_PARENT_WITH_ATOMIC_CHILDREN` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-024` | `UXF-00-R016` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `ROUTE_TO_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-025` | `UXF-00-R017` | `RULE_APPLICATION` | `CRITICAL` | `CONFIRM_CRITICAL` | `CRITICAL` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-026` | `UXF-00-R020` | `RULE_APPLICATION` | `HIGH` | `CONFIRM_HIGH` | `HIGH` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-027` | `UXF-00-R021` | `RULE_APPLICATION` | `CRITICAL` | `CONFIRM_CRITICAL` | `CRITICAL` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-028` | `UXF-005` | `RULE_APPLICATION` | `CRITICAL` | `CONFIRM_CRITICAL` | `CRITICAL` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-029` | `UXF-01-R009` | `RULE_APPLICATION` | `HIGH` | `CONFIRM_HIGH` | `HIGH` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-030` | `UXF-02-R001` | `RULE_APPLICATION` | `HIGH` | `CONFIRM_NORMAL` | `NORMAL` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-031` | `UXF-02-R009` | `RULE_APPLICATION` | `HIGH` | `CONFIRM_HIGH` | `HIGH` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-032` | `UXF-04-R004` | `RULE_APPLICATION` | `CRITICAL` | `CONFIRM_CRITICAL` | `CRITICAL` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-033` | `UXF-04-R006` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `ROUTE_TO_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-034` | `UXF-05-R005` | `RULE_APPLICATION` | `CRITICAL` | `CONFIRM_CRITICAL` | `CRITICAL` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-035` | `UXF-05-R008` | `RULE_APPLICATION` | `CRITICAL` | `CONFIRM_CRITICAL` | `CRITICAL` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-036` | `UXF-05-R009` | `RULE_APPLICATION` | `CRITICAL` | `CONFIRM_CRITICAL` | `CRITICAL` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-037` | `UXF-106` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `CRITICAL` | `ROUTE_TO_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-038` | `UXF-110` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `ROUTE_TO_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-039` | `UXF-202` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `ROUTE_TO_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-040` | `UXF-203` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `ROUTE_TO_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-041` | `UXF-204` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `ROUTE_TO_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-042` | `UXF-208` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `ROUTE_TO_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-043` | `UXF-402` | `HUMAN_RISK_DECISION` | `CRITICAL` | `CONFIRM_HIGH` | `HIGH` | `CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-044` | `UXF-408` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `ROUTE_TO_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-045` | `UXF-501` | `CLASSIFICATION_OR_EXTRACTION_DEFECT` | `HIGH` | `ROUTE_TO_REMEDIATION` | `REMEDIATION_REQUIRED` | `DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |
| `P2-CRIT-EXC-046` | `UXF-506` | `RULE_APPLICATION` | `CRITICAL` | `CONFIRM_CRITICAL` | `CRITICAL` | `CRITICALITY_RULE_RECOMMENDATION` | `NOT_YET_APPLIED` | `OPEN` |

## 10. Candidate state

- All 46 exceptions remain `OPEN`.
- Resolved exceptions: `0`.
- Dispositioned exceptions: `46`; undispositioned exceptions: `0`.
- Every selected disposition exactly matches its recorded recommendation.
- Source application status for every exception: `NOT_YET_APPLIED`.
- Projection qualifier: `PROVISIONAL_EXCLUDES_PENDING_SOURCE_REMEDIATION_AND_CHILD_RECONCILIATION`.
- Candidate approval block: entirely `PENDING`.
- No source criticality, scope, statement, stable ID, or resolution status has been modified.
- Next gate: `HUMAN_CRITICALITY_DECISION_PACK_APPROVAL`.
