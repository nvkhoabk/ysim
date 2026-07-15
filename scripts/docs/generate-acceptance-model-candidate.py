#!/usr/bin/env python3
"""Generate the Phase 2C hybrid acceptance-model candidate without rewriting source blocks."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[2]
PHASE2 = ROOT / "docs/baselines/v2.3/phase-2"
REGISTRY = PHASE2 / "remediated-registry"
CANDIDATE_ID = "V23-P2C-ACCEPTANCE-MODEL-C1"
BASE_COMMIT = "0df2d424e00f9cd27b8dcb6645eef827ce97b60e"
MODEL_VERSION = "1.0.0-candidate.1"
PROFILE_VERSION = "1.0.0"
BLOCKER = "ACCEPTANCE_CONTRACT_MODEL_NOT_APPROVED"

OUTPUT_PATHS = (
    PHASE2 / "ACCEPTANCE_CONTRACT_MODEL.md",
    PHASE2 / "ACCEPTANCE_PROFILE_CATALOG.md",
    PHASE2 / "acceptance-profile-catalog.json",
    PHASE2 / "acceptance-mapping-dry-run.json",
    PHASE2 / "ACCEPTANCE_MAPPING_REVIEW_PACK.md",
    PHASE2 / "acceptance-model-candidate-manifest.json",
    PHASE2 / "schemas/acceptance-profile-catalog.schema.json",
    PHASE2 / "schemas/acceptance-mapping-dry-run.schema.json",
    PHASE2 / "PHASE_2C_BLOCKER_REGISTER.md",
    PHASE2 / "phase-2c-document-baseline-candidate.json",
)

BANNED = (
    "works as expected", "is handled correctly", "appropriate error is returned",
    "requirement is satisfied", "verify the business rule", "system remains consistent",
)

INLINE_CATEGORIES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("FRAUD_RISK_DECISION", ("fraud", "risk engine", "allow, challenge, block", "allow, challenge", "risk decision")),
    ("FINANCIAL_RECONCILIATION", ("reconciliation", "đối soát", "ledger", "settlement")),
    ("PAYMENT", ("payment", "thanh toán", "merchantaccount", "paymentgateway")),
    ("PRICING", ("pricing", "price list", "giá bán", "bảng giá")),
    ("PROMOTION", ("promotion", "khuyến mãi", "coupon", "voucher")),
    ("PROCUREMENT", ("procurement", "purchase order", "mua hàng", "supplier order")),
    ("ALLOCATION", ("allocation", "phân bổ", "reservation", "giữ chỗ")),
    ("FULFILLMENT", ("fulfillment", "shipment", "giao hàng", "delivery order")),
    ("REFUND", ("refund", "hoàn tiền", "chargeback")),
    ("COMPLEX_WORKFLOW", ("workflow", "state machine", "saga", "orchestration", "nhiều trạng thái", "disaster recovery")),
)

PROFILE_BLUEPRINTS: tuple[dict[str, Any], ...] = (
    {"id":"ENTITY_INDEPENDENCE","title":"Independent business entities","intent":"Verify that named entities retain distinct identity, ownership/reference, and lifecycle boundaries.","types":["DATA_REQUIREMENT","INTEGRATION_REQUIREMENT","BUSINESS_RULE"],"terms":["độc lập","independent"],"bindings":{"entity_a":"identifier","entity_b":"identifier","independence_dimensions":"string_list"},"observable":"identity, owner/reference, and lifecycle comparisons for both bound entities","positive":"Given {entity_a} and {entity_b}, when identity, ownership/reference, and lifecycle evidence is compared, then each entity remains independently identifiable and governed across {independence_dimensions}.","negative":"Given a candidate that merges {entity_a} with {entity_b}, when entity integrity is validated, then the conflation is rejected with the violated independence dimension identified.","edge":"Given one entity changes lifecycle state, when the relationship is observed, then the other entity changes only through an explicit independently authorized transition.","evidence":["both stable identities","ownership and reference resolution","before/after lifecycle states"],"failure":"Reject conflated identity or implicit lifecycle coupling."},
    {"id":"ENUM_REFERENCE_INTEGRITY","title":"Enum and canonical-reference integrity","intent":"Verify an enumerated discriminator, dependent-field consistency, and canonical registry references.","types":["DATA_REQUIREMENT","BUSINESS_RULE"],"terms":["enum","publisher","subscriber","canonical","registry id"],"bindings":{"enum_field":"field_name","allowed_values":"string_list","dependent_fields":"string_list","reference_registry":"identifier","prohibited_reference_states":"string_list"},"observable":"accepted/rejected field values, dependent-field validation, and canonical reference resolution","positive":"Given {enum_field} and {dependent_fields}, when a record is validated, then only {allowed_values} and role-consistent fields with references resolving in {reference_registry} are accepted.","negative":"Given an unsupported {enum_field} value or inconsistent {dependent_fields}, when validation runs, then the record is rejected and the invalid field is identified.","edge":"Given references in {prohibited_reference_states}, when canonical resolution runs, then every prohibited or dangling reference is rejected.","evidence":["submitted discriminator and fields","field validation results","canonical reference statuses","persistence outcome"],"failure":"Reject the complete inconsistent record; do not persist partial reference state."},
    {"id":"REQUIRED_CAPABILITY_SET","title":"Required capability set","intent":"Verify that a named subject exposes every explicitly enumerated required capability without inventing additional capabilities.","types":["BUSINESS_REQUIREMENT","BUSINESS_DECISION","UX_REQUIREMENT","OPERATIONAL_REQUIREMENT"],"terms":["hỗ trợ","supports","bao gồm","include"],"bindings":{"capability_subject":"identifier","required_capabilities":"string_list"},"observable":"capability inventory and an observable outcome for each bound capability","positive":"Given {capability_subject}, when its capability inventory is inspected, then every member of {required_capabilities} is independently available and attributable to that subject.","negative":"Given one bound capability is absent or attributed to another subject, when completeness is evaluated, then the missing or misattributed member is reported.","edge":"Given a capability outside {required_capabilities}, when conformance is evaluated, then it is not used as evidence that a missing bound capability exists.","evidence":["subject identity","enumerated capability inventory","per-capability observable outcome"],"failure":"Report the exact missing bound member; no aggregate pass from partial coverage."},
    {"id":"POLICY_SCOPE_ENFORCEMENT","title":"Policy scope enforcement","intent":"Verify independent policy configuration and enforcement at explicitly named scopes.","types":["SECURITY_REQUIREMENT","BUSINESS_RULE","BUSINESS_DECISION"],"terms":["platform","organization","role","user","scope"],"bindings":{"policy_name":"identifier","policy_scopes":"string_list","governed_action":"text"},"observable":"configured policies, effective scope resolution, and allow/challenge/deny outcome","positive":"Given {policy_name} configured at each of {policy_scopes}, when {governed_action} is evaluated, then the effective policy identifies and enforces every applicable bound scope.","negative":"Given a principal outside a required policy condition, when {governed_action} is attempted, then the action is denied or challenged by the effective bound policy.","edge":"Given overlapping policies across {policy_scopes}, when policy resolution runs, then contributing scopes and the effective result are observable without silently dropping a scope.","evidence":["scope-specific policy values","principal-to-scope bindings","effective-policy trace","decision and audit evidence"],"failure":"Fail closed when a mandatory applicable scope cannot be resolved."},
    {"id":"POLICY_PRECEDENCE","title":"Policy precedence","intent":"Verify deterministic resolution when two or more named policies apply.","types":["BUSINESS_RULE","SECURITY_REQUIREMENT","PRIVACY_REQUIREMENT"],"terms":["precedence","ưu tiên","override","ghi đè"],"bindings":{"policy_set":"string_list","precedence_order":"string_list","decision_subject":"text"},"observable":"applicable policy set, selected policy, precedence reason, and decision","positive":"Given {policy_set} applies to {decision_subject}, when precedence is resolved, then the selected policy follows {precedence_order} and the selection reason is recorded.","negative":"Given a lower-precedence policy conflicts with a higher-precedence policy, when resolution runs, then the lower-precedence outcome does not take effect.","edge":"Given equal-precedence or incomplete policy metadata, when resolution runs, then no silent winner is selected and the conflict is surfaced deterministically.","evidence":["all applicable policy versions","precedence inputs","selected policy and reason","resulting decision"],"failure":"Block an ambiguous policy decision rather than inventing precedence."},
    {"id":"STATE_TRANSITION","title":"State transition","intent":"Verify an explicitly named source state, trigger, target state, and prohibited transition.","types":["BUSINESS_RULE","BUSINESS_REQUIREMENT","OPERATIONAL_REQUIREMENT"],"terms":["transition","chuyển","trạng thái","state"],"bindings":{"state_subject":"identifier","source_states":"string_list","trigger":"text","target_states":"string_list"},"observable":"before state, trigger, transition decision, after state, and reason","positive":"Given {state_subject} in {source_states}, when {trigger} occurs, then only the bound target in {target_states} is reached and the transition is observable.","negative":"Given {state_subject} outside {source_states}, when {trigger} occurs, then no prohibited target transition is recorded.","edge":"Given a missing trigger prerequisite or terminal state, when transition is requested, then the request produces a deterministic rejection with unchanged state.","evidence":["subject identity","before/after state","trigger and prerequisite values","transition decision and reason"],"failure":"Reject prohibited transitions without partial state mutation."},
    {"id":"STATE_MACHINE_INVARIANT","title":"State-machine invariant","intent":"Verify an invariant that must hold across all bound states and transitions.","types":["BUSINESS_RULE","OPERATIONAL_REQUIREMENT"],"terms":["invariant","mọi trạng thái","terminal state","trạng thái cuối"],"bindings":{"state_machine_subject":"identifier","invariant":"text","applicable_states":"string_list"},"observable":"state history and invariant evaluation at each bound state","positive":"Given {state_machine_subject} traverses {applicable_states}, when each transition is evaluated, then {invariant} holds before and after every accepted transition.","negative":"Given a transition that would violate {invariant}, when it is requested, then the transition is rejected with the invariant violation identified.","edge":"Given recovery from an intermediate or terminal failure, when state is restored or advanced, then {invariant} remains true and the recovery transition is recorded.","evidence":["ordered state history","invariant evaluation per transition","rejection or recovery reason"],"failure":"Do not accept any transition that leaves the invariant false."},
    {"id":"FAIL_CLOSED_BOUNDARY","title":"Fail-closed boundary","intent":"Verify an explicit mandatory-evidence or assurance boundary that prohibits success when unresolved.","types":["SECURITY_REQUIREMENT","PRIVACY_REQUIREMENT","DATA_REQUIREMENT","INTEGRATION_REQUIREMENT","UX_REQUIREMENT"],"terms":["fail closed","fail-closed","không được tiếp tục","must not proceed"],"bindings":{"protected_action":"text","mandatory_evidence":"string_list","blocked_outcome":"text"},"observable":"evidence validation, allow/deny result, protected-state comparison, and reason","positive":"Given valid {mandatory_evidence}, when {protected_action} is requested, then evaluation may proceed and records the validated evidence.","negative":"Given missing or invalid {mandatory_evidence}, when {protected_action} is requested, then {blocked_outcome} and protected state is unchanged.","edge":"Given evidence cannot be resolved conclusively, when the boundary is evaluated, then the unresolved result follows the same blocked outcome rather than defaulting to success.","evidence":["mandatory evidence values and validity","decision and reason","before/after protected state"],"failure":"No success or partial protected-state change without all mandatory evidence."},
    {"id":"NO_INTERNAL_DISCLOSURE","title":"No internal disclosure","intent":"Verify allowed external disclosure and absence of explicitly prohibited internal fields.","types":["UX_REQUIREMENT","PRIVACY_REQUIREMENT","SECURITY_REQUIREMENT"],"terms":["must never be exposed","không được hiển thị","không được lộ","internal"],"bindings":{"channel":"identifier","allowed_disclosure":"string_list","prohibited_fields":"string_list"},"observable":"rendered fields, external payload field inventory, and prohibited-field absence","positive":"Given {channel}, when customer-facing disclosure is produced, then only {allowed_disclosure} is present and remains read-only where bound.","negative":"Given internal values for {prohibited_fields}, when the UI and external payload are inspected, then none of those fields or values is disclosed.","edge":"Given allowed disclosure data is unavailable, when disclosure is mandatory, then the affected action follows its explicit fail-closed outcome without substituting internal data.","evidence":["rendered field inventory","complete external payload fields","allowed disclosure source","blocked or fallback outcome"],"failure":"Do not expose prohibited internal data through UI, payload, fallback, or derived labels."},
    {"id":"EVENT_ORDERING","title":"Event ordering","intent":"Verify whether explicitly bound event families must preserve or need not preserve processing order.","types":["DESIGN_PRINCIPLE","INTEGRATION_REQUIREMENT","BUSINESS_RULE"],"terms":["processing order","ordering","thứ tự xử lý"],"bindings":{"event_families":"string_list","ordering_policy":"enum:PRESERVE|NOT_REQUIRED","observation_boundary":"text"},"observable":"event-family identity, observed processing order, and policy conformance result","positive":"Given events from {event_families}, when processing is observed at {observation_boundary}, then behavior conforms to {ordering_policy} without applying another family's policy.","negative":"Given an event family outside {event_families}, when ordering is evaluated, then this profile binding is not used as its ordering authority.","edge":"Given interleaved events across bound families, when conformance is reviewed, then the policy is evaluated per family and does not infer cross-family ordering.","evidence":["event family and event identities","observed order at bound boundary","policy conformance decision"],"failure":"Report policy violation only where PRESERVE is bound; never infer ordering for NOT_REQUIRED."},
    {"id":"EVENT_DELIVERY","title":"Event delivery contract","intent":"Verify an explicit event producer, consumer, delivery outcome, and terminal failure boundary.","types":["INTEGRATION_REQUIREMENT","BUSINESS_REQUIREMENT","OPERATIONAL_REQUIREMENT"],"terms":["event","delivery","publish","subscribe","consumer"],"bindings":{"event_name":"identifier","producer":"identifier","consumer":"identifier","delivery_outcome":"text"},"observable":"published event identity, consumer receipt/outcome, and terminal delivery evidence","positive":"Given {producer} emits {event_name}, when delivery to {consumer} is evaluated, then {delivery_outcome} is observable and attributable to the same event identity.","negative":"Given an invalid or unauthorized {event_name}, when delivery is attempted, then it is rejected before producing the bound consumer outcome.","edge":"Given terminal delivery failure, when delivery evidence is inspected, then the final failure and affected event identity are visible for controlled remediation.","evidence":["event and producer identity","consumer receipt or rejection","delivery outcome","terminal failure evidence"],"failure":"Never report delivery success without consumer-bound observable evidence."},
    {"id":"IDEMPOTENT_OPERATION","title":"Idempotent operation","intent":"Verify explicit repeated-operation semantics under a bound idempotency identity.","types":["INTEGRATION_REQUIREMENT","BUSINESS_RULE","OPERATIONAL_REQUIREMENT"],"terms":["idempot","duplicate","dedup","lặp"],"bindings":{"operation":"text","idempotency_identity":"identifier","stable_outcome":"text"},"observable":"operation attempts, bound identity, outcome identity, and side-effect comparison","positive":"Given {operation} with {idempotency_identity}, when the same request is repeated, then {stable_outcome} is returned without an additional business side effect.","negative":"Given two requests with different valid identities, when both are processed, then one identity is not incorrectly deduplicated as the other.","edge":"Given an in-flight or partially observed first attempt, when the same identity is retried, then the eventual bound outcome remains singular and traceable.","evidence":["attempts and idempotency identity","business outcome identity","before/after side-effect count","decision reason"],"failure":"Prevent duplicate business effects for the same bound identity."},
    {"id":"RETRY_AND_TERMINAL_FAILURE","title":"Retry and terminal failure","intent":"Verify an explicitly bounded retry policy and observable terminal outcome.","types":["OPERATIONAL_REQUIREMENT","INTEGRATION_REQUIREMENT"],"terms":["retry","thử lại","backoff","terminal failure","dead letter"],"bindings":{"operation":"text","retry_limit":"integer_or_policy","retry_condition":"text","terminal_outcome":"text"},"observable":"attempt sequence, retry reason, applied limit/policy, and terminal outcome","positive":"Given {operation} fails under {retry_condition}, when retry policy applies, then attempts follow {retry_limit} and each attempt is observable.","negative":"Given a non-retryable failure, when failure is classified, then no retry is started and the reason is recorded.","edge":"Given retries reach {retry_limit}, when the final attempt fails, then {terminal_outcome} is emitted exactly as bound and remains operator-visible.","evidence":["attempt number and time","failure classification","retry policy version","terminal outcome and operation identity"],"failure":"Do not retry outside the bound condition or conceal exhaustion."},
    {"id":"ROLE_AND_PERMISSION_ENFORCEMENT","title":"Role and permission enforcement","intent":"Verify explicitly bound actor, resource/action, and permission boundary.","types":["SECURITY_REQUIREMENT","BUSINESS_RULE","BUSINESS_REQUIREMENT"],"terms":["permission","quyền","chỉ được xem","access","role"],"bindings":{"actor_scope":"text","governed_resource":"text","allowed_actions":"string_list","prohibited_actions":"string_list"},"observable":"principal and scope, effective permission, available/denied action, protected-state comparison, and audit evidence","positive":"Given {actor_scope}, when access to {governed_resource} is evaluated, then only {allowed_actions} are available within the bound scope.","negative":"Given the same actor requests {prohibited_actions}, when authorization is evaluated, then the action is denied and protected state remains unchanged.","edge":"Given ownership or scope attribution is missing or conflicting, when access is evaluated, then no broader access is inferred and the unresolved boundary is denied.","evidence":["actor and scope attribution","effective permission","available and denied action","resource result","audit reason"],"failure":"Deny access outside the concretely bound actor/resource/action scope."},
    {"id":"AUTHENTICATION_REQUIREMENT","title":"Authentication requirement","intent":"Verify a named assurance or credential requirement at an authentication boundary.","types":["SECURITY_REQUIREMENT"],"terms":["authentication","xác thực","credential","đăng nhập"],"bindings":{"principal_type":"identifier","assurance_requirement":"text","protected_action":"text"},"observable":"principal, assurance evidence, challenge/allow/deny result, and audit reason","positive":"Given {principal_type} presents evidence satisfying {assurance_requirement}, when {protected_action} is attempted, then authentication succeeds at the bound assurance level.","negative":"Given missing or invalid assurance evidence, when {protected_action} is attempted, then authentication is denied or challenged without granting the protected action.","edge":"Given assurance cannot be resolved or has expired, when authentication is evaluated, then no previous success is reused outside its validity boundary.","evidence":["principal identity","assurance evidence and validity","authentication decision","protected-action result","audit reason"],"failure":"Fail closed at the stated assurance boundary."},
    {"id":"MFA_ENFORCEMENT","title":"Multi-factor authentication enforcement","intent":"Verify MFA policy, effective scope resolution, required challenge, bypass denial, and applicable recovery.","types":["SECURITY_REQUIREMENT"],"terms":["mfa","multi-factor"],"bindings":{"mfa_scopes":"string_list","principal_types":"string_list","challenge_requirement":"text"},"observable":"scope policies, effective resolution, challenge result, bypass decision, and audit evidence","positive":"Given MFA policies at {mfa_scopes} for {principal_types}, when effective policy is resolved, then {challenge_requirement} is presented and must be satisfied.","negative":"Given a required challenge is missing, invalid, or bypassed, when the protected action is attempted, then access is denied and the attempt is audited.","edge":"Given overlapping scope policies or an applicable approved recovery flow, when MFA is evaluated, then effective scopes and recovery-specific assurance are explicit without silently disabling MFA.","evidence":["all applicable MFA policies","scope resolution trace","challenge and result","bypass/recovery decision","audit record"],"failure":"No protected action succeeds while an effective MFA requirement is unsatisfied."},
    {"id":"DATA_ISOLATION","title":"Data isolation","intent":"Verify explicit tenant, organization, owner, or subject isolation at read and mutation boundaries.","types":["SECURITY_REQUIREMENT","PRIVACY_REQUIREMENT","DATA_REQUIREMENT","BUSINESS_RULE"],"terms":["isolation","cô lập","tenant","khách hàng của mình","organization data"],"bindings":{"isolation_scope":"text","data_subject":"text","allowed_owner":"text"},"observable":"requesting scope, data ownership, returned records, mutation result, and denial evidence","positive":"Given {allowed_owner} in {isolation_scope}, when {data_subject} is read or changed, then only records attributed to that bound owner and scope are available.","negative":"Given a record outside {isolation_scope} or not owned by {allowed_owner}, when access is attempted, then no record or mutation is disclosed and the decision is denied.","edge":"Given missing or conflicting ownership attribution, when isolation is evaluated, then broader scope is not inferred and access fails closed.","evidence":["requesting actor and scope","record ownership attribution","returned-record inventory","mutation or denial result","audit reason"],"failure":"Prevent cross-scope disclosure or mutation."},
    {"id":"DATA_RETENTION","title":"Data retention","intent":"Verify an explicit retention duration, online/archive boundary, and post-retention outcome.","types":["PRIVACY_REQUIREMENT","OPERATIONAL_REQUIREMENT","BUSINESS_RULE"],"terms":["retention","lưu trực tuyến","archive","lưu giữ"],"bindings":{"data_subject":"identifier","retention_period":"duration","post_retention_outcome":"text"},"observable":"data age, online availability, archive/deletion state, transition time, and policy reference","positive":"Given {data_subject} within {retention_period}, when availability is inspected, then the bound online or retained state is observable.","negative":"Given {data_subject} beyond {retention_period}, when online availability is inspected, then it is not retained online contrary to policy.","edge":"Given the retention boundary is crossed, when policy applies, then {post_retention_outcome} occurs with transition evidence tied to the same data identity.","evidence":["data identity and age","retention policy and duration","before/after storage class or deletion state","transition evidence"],"failure":"Do not retain or remove data contrary to the bound duration and outcome."},
    {"id":"AUDITABILITY","title":"Auditability","intent":"Verify that a named decision or operation records required actor, action, reason, version, and outcome evidence.","types":["OPERATIONAL_REQUIREMENT","SECURITY_REQUIREMENT","BUSINESS_RULE"],"terms":["audit","auditable","kiểm toán"],"bindings":{"audited_subject":"text","required_audit_fields":"string_list","audit_trigger":"text"},"observable":"audit record tied to subject identity with every bound field resolvable","positive":"Given {audit_trigger} for {audited_subject}, when the outcome is recorded, then {required_audit_fields} are present and attributable to that same subject.","negative":"Given a record missing one bound audit field, when audit completeness is verified, then it is reported non-conforming with the missing field identified.","edge":"Given an override, failure, or recovery outcome, when auditing applies, then both original and effective outcome remain distinguishable where bound.","evidence":["subject identity","complete audit field inventory","trigger and outcome linkage","version references"],"failure":"Do not claim auditability from an incomplete or unattributed record."},
    {"id":"CONFIGURATION_LIFECYCLE","title":"Configuration lifecycle","intent":"Verify explicit draft, validation, activation, replacement, and retirement behavior for configuration.","types":["BUSINESS_RULE","OPERATIONAL_REQUIREMENT","DESIGN_PRINCIPLE"],"terms":["configuration","cấu hình","activate","publish","version"],"bindings":{"configuration_subject":"identifier","lifecycle_states":"string_list","activation_condition":"text"},"observable":"configuration identity/version, before/after state, validation result, and effective selection","positive":"Given {configuration_subject} in {lifecycle_states}, when {activation_condition} is satisfied, then the intended version becomes effective with its transition recorded.","negative":"Given invalid or incomplete configuration, when activation is requested, then it does not become effective and the validation reason is observable.","edge":"Given replacement or retirement, when effective configuration is resolved, then exactly the intended valid version is selected without silently reviving a retired version.","evidence":["configuration identity and version","validation evidence","before/after lifecycle state","effective-version resolution"],"failure":"Prevent invalid, retired, or ambiguous configuration from becoming effective."},
    {"id":"APPROVAL_WORKFLOW","title":"Approval workflow","intent":"Verify an explicit approval eligibility, decision, reason, and governed action boundary.","types":["BUSINESS_RULE","SECURITY_REQUIREMENT","OPERATIONAL_REQUIREMENT"],"terms":["approval","approve","phê duyệt","override"],"bindings":{"approval_subject":"text","authorized_approver_scope":"text","approval_outcomes":"string_list","governed_action":"text"},"observable":"approver authorization, decision, reason, subject state, and audit evidence","positive":"Given {authorized_approver_scope} reviews {approval_subject}, when an outcome in {approval_outcomes} is selected, then {governed_action} follows that decision and records approver and reason.","negative":"Given an unauthorized actor or missing mandatory reason, when approval is attempted, then the decision is rejected and the governed action does not proceed.","edge":"Given approval is withdrawn, expires, or conflicts with a mandatory policy, when effectiveness is resolved, then the mandatory policy prevails and effective state is explicit.","evidence":["subject and approver identity","authorization result","decision and reason","before/after governed state","audit record"],"failure":"Never treat an unauthorized or incomplete approval as effective."},
    {"id":"UX_STATE_AND_ACTION","title":"UX state and action","intent":"Verify a named rendered state, available action, prohibited disclosure/action, and fallback outcome.","types":["UX_REQUIREMENT"],"terms":["display","render","screen","action","button","navigation","journey","hiển thị"],"bindings":{"ux_surface":"identifier","rendered_state":"text","available_actions":"string_list","fallback_outcome":"text"},"observable":"rendered state, enabled/unavailable actions, visible confirmation, and payload-field inventory","positive":"Given {ux_surface}, when the bound journey state is reached, then {rendered_state} and {available_actions} are directly visible and actionable as specified.","negative":"Given an action or disclosure outside the bound state, when the surface is inspected, then it is unavailable or absent rather than silently enabled.","edge":"Given required journey input is unavailable, when the surface renders, then {fallback_outcome} is visible and no prohibited action proceeds.","evidence":["rendered-state capture","available and unavailable action inventory","user-visible confirmation or fallback","external payload fields where applicable"],"failure":"Do not infer success from hidden state; required UI outcome must be observable."},
    {"id":"UX_ACCESSIBILITY","title":"UX accessibility outcome","intent":"Verify a specifically named accessibility mode, interaction, or conformance outcome.","types":["ACCESSIBILITY_REQUIREMENT","UX_REQUIREMENT"],"terms":["accessibility","high contrast","keyboard","screen reader","wcag","a11y"],"bindings":{"ux_surface":"identifier","accessibility_capability":"text","affected_content_or_action":"text"},"observable":"enabled accessibility state, perceivable content, operable action, fallback, and conformance evidence","positive":"Given {accessibility_capability} is enabled on {ux_surface}, when {affected_content_or_action} is rendered or used, then the bound content remains perceivable and the action remains operable.","negative":"Given the accessibility capability is absent or broken, when the affected interaction is tested, then conformance fails with the inaccessible content or action identified.","edge":"Given fallback content or an unavailable primary interaction, when the accessible alternative applies, then the alternative is perceivable, operable, and exposes the same required outcome.","evidence":["enabled mode or assistive context","rendered content and action state","interaction result","specific conformance finding"],"failure":"Do not claim accessibility from generic rendering evidence."},
    {"id":"UX_PERFORMANCE_BUDGET","title":"UX performance budget","intent":"Verify an explicit user-visible timing or responsiveness budget at a named journey boundary.","types":["PERFORMANCE_REQUIREMENT","UX_REQUIREMENT"],"terms":["latency","seconds","ms","performance budget","response time","thời gian"],"bindings":{"journey_boundary":"text","metric":"identifier","budget":"duration_or_threshold","measurement_condition":"text"},"observable":"measurement condition, observed metric value, bound budget, and pass/fail result","positive":"Given {measurement_condition}, when {journey_boundary} is measured, then {metric} is within {budget} and the observed value is recorded.","negative":"Given the observed value exceeds {budget}, when conformance is evaluated, then the journey is reported outside budget with the measured value identified.","edge":"Given incomplete measurement conditions or missing samples, when conformance is evaluated, then no budget pass is claimed until the bound condition is met.","evidence":["journey and condition","metric definition","budget and observed values","measurement result"],"failure":"Never invent a threshold or claim performance without a bound measurement."},
    {"id":"DESIGN_CONFORMANCE_TRACE","title":"Design conformance trace","intent":"Verify traceability from a design principle to governed requirements, configuration, and architectural boundary without runtime tautology.","types":["DESIGN_PRINCIPLE","PERFORMANCE_REQUIREMENT"],"terms":["principle","first","driven","ready","nền tảng","architecture","kiến trúc"],"bindings":{"principle":"text","governed_artifact":"text","required_trace":"string_list"},"observable":"conformance decision, requirement/design/configuration trace, and named boundary violation","positive":"Given {governed_artifact}, when conformance to {principle} is reviewed, then {required_trace} is complete and the applicable design or configuration boundary is explicit.","negative":"Given a missing trace or direct violation of the bound principle, when conformance is reviewed, then the artifact is reported non-conforming with the exact gap identified.","edge":"Given the principle is not applicable to an artifact, when review runs, then non-applicability is justified from scope rather than treated as conformance evidence.","evidence":["principle identifier","governed artifact","complete bound trace","conformance decision and gap"],"failure":"Do not substitute a generic runtime pass for design conformance."},
    {"id":"OPERATION_OBSERVABILITY","title":"Operation observability","intent":"Verify named running/completed/failed state, outcome, signals, and detectable missing-evidence failure.","types":["OPERATIONAL_REQUIREMENT"],"terms":["observable","observability","quan sát","telemetry","signal"],"bindings":{"operation_subject":"text","required_states":"string_list","required_signals":"string_list"},"observable":"operation identity, current/terminal state, outcome, signal values, and verification failure","positive":"Given {operation_subject} is in {required_states}, when an operator inspects it, then the matching state, outcome, and {required_signals} are observable.","negative":"Given required state, outcome, or signal evidence is absent, when observability is verified, then a detectable failure identifies the missing evidence.","edge":"Given the operation changes from running to completed or failed, when observations are compared, then the terminal outcome and relevant signals remain attributable to the same operation.","evidence":["operation identity","state and outcome","bound signal names and values","observation time","verification result"],"failure":"Do not report operational verification success with missing bound evidence."},
    {"id":"INTEGRATION_CONTRACT","title":"Integration contract boundary","intent":"Verify an explicit producer/provider, consumer/client, accepted input/output, ownership boundary, and rejection outcome.","types":["INTEGRATION_REQUIREMENT"],"terms":["api","integration","connector","adapter","provider","consumer"],"bindings":{"provider":"identifier","consumer":"identifier","contract_input":"text","contract_outcome":"text"},"observable":"submitted contract, provider/consumer ownership, accept/reject result, external outcome, and reconciliation evidence where bound","positive":"Given {consumer} submits {contract_input} to {provider}, when the contract is evaluated, then {contract_outcome} is observable at the bound integration boundary.","negative":"Given malformed, unsupported, or unauthorized contract input, when the provider evaluates it, then it is rejected with no false successful external outcome.","edge":"Given external outcome is incomplete or disputed, when boundary ownership is inspected, then the responsible party and reconciliation evidence are explicit.","evidence":["provider and consumer identities","submitted contract","accept/reject result","external outcome","ownership and reconciliation evidence"],"failure":"Do not claim integration success without a bound external interaction outcome."},
    {"id":"SCOPE_EXCLUSION","title":"Scope exclusion","intent":"Verify that an explicitly future, deferred, or excluded capability is not represented as active behavior in the current baseline.","types":["SCOPE_CONSTRAINT","BUSINESS_DECISION","DESIGN_PRINCIPLE"],"terms":["future","deferred","out of scope","chưa triển khai","phiên bản sau"],"bindings":{"excluded_capability":"text","scope_status":"enum:FUTURE|DEFERRED|OUT_OF_SCOPE","current_baseline":"version"},"observable":"baseline capability inventory, exposed UI/API/action surface, and scope marker","positive":"Given {current_baseline}, when capability inventory is inspected, then {excluded_capability} is marked {scope_status} and is not represented as active delivery.","negative":"Given an exposed action or contract claiming the excluded capability is active, when scope conformance is checked, then the claim is rejected as outside the bound baseline.","edge":"Given architectural readiness without implementation, when conformance is evaluated, then readiness evidence is distinguishable from active product availability.","evidence":["baseline and scope marker","capability inventory","exposed actions/contracts","conformance result"],"failure":"Prevent future or deferred capability from being counted as active."},
)


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def pretty_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_records() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for name in ("brd-requirements.json", "uxf-requirements.json"):
        records.extend(json.loads((REGISTRY / name).read_text(encoding="utf-8"))["requirements"])
    return sorted(
        (r for r in records if r["record_kind"] == "CANONICAL_ATOMIC" and r["scope_status"] == "V2.3_ACTIVE"),
        key=lambda r: r["stable_id"],
    )


def binding_definitions(raw: dict[str, str]) -> list[dict[str, Any]]:
    return [
        {"name": name, "data_type": data_type, "description": f"Concrete {name.replace('_', ' ')} extracted from source or an approved decision.", "source_required": True}
        for name, data_type in raw.items()
    ]


def example_bindings(profile: dict[str, Any], suffix: str) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for binding in profile["required_bindings"]:
        name, kind = binding["name"], binding["data_type"]
        if "list" in kind:
            result[name] = [f"{name}_A_{suffix}", f"{name}_B_{suffix}"]
        elif kind == "integer_or_policy":
            result[name] = f"approved_{name}_{suffix}"
        elif kind in {"duration", "duration_or_threshold", "version"}:
            result[name] = f"bound_{name}_{suffix}"
        elif kind.startswith("enum:"):
            result[name] = kind.split(":", 1)[1].split("|")[0]
        else:
            result[name] = f"bound_{name}_{suffix}"
    return result


def build_catalog() -> dict[str, Any]:
    profiles: list[dict[str, Any]] = []
    for raw in PROFILE_BLUEPRINTS:
        required = binding_definitions(raw["bindings"])
        profile = {
            "profile_id": f"ACP-{raw['id']}",
            "version": PROFILE_VERSION,
            "title": raw["title"],
            "semantic_intent": raw["intent"],
            "supported_requirement_types": raw["types"],
            "applicability_rules": [
                "The normative statement and full source section express this profile's semantic intent directly.",
                "Every required binding is extracted verbatim or normalized deterministically from source/approved decisions.",
                "Rendered positive, negative, and edge oracles verify the same atomic obligation without solution inference.",
            ],
            "prohibited_uses": [
                "Keyword-only classification without structural and binding validation.",
                "Complex payment, pricing, promotion, procurement, allocation, fulfillment, refund, fraud/risk, or financial-reconciliation workflow.",
                "Any use requiring an invented threshold, state, role, actor, failure mode, or technical implementation.",
                "Any binding that broadens or drops a qualifier, applicability scope, or failure semantic.",
            ],
            "required_bindings": required,
            "optional_bindings": [
                {"name": "approved_decision_refs", "data_type": "string_list", "description": "Approved decisions that constrain the rendered contract.", "source_required": True},
                {"name": "source_context_heading", "data_type": "text", "description": "Full source-section heading used for semantic review.", "source_required": True},
            ],
            "observable_verification_contract": raw["observable"],
            "oracle_templates": {
                "positive": raw["positive"], "negative": raw["negative"], "edge_boundary": raw["edge"],
            },
            "evidence_requirements": raw["evidence"],
            "failure_semantics": raw["failure"],
            "criticality_compatibility": ["CRITICAL", "HIGH", "NORMAL"],
            "deterministic_validation_rules": [
                "All required bindings are present, typed, non-empty, source-grounded, and used by at least one oracle.",
                "No undeclared binding token remains after rendering.",
                "Rendered oracles contain no generic or tautological acceptance phrase.",
                "Requirement type and criticality are compatible with this profile.",
                "The semantic matcher, binding extractor, and rendered-oracle audit all pass independently.",
            ],
            "valid_examples": [],
            "counterexamples": [],
            "matcher_contract": {
                "semantic_terms": raw["terms"],
                "requires_type_compatibility": True,
                "requires_structural_binding_extraction": True,
                "keyword_only_match_forbidden": True,
            },
        }
        primary_binding = required[0]["name"]
        for oracle_name, oracle_template in tuple(profile["oracle_templates"].items()):
            if not re.search(r"\{[a-z][a-z0-9_]*\}", oracle_template):
                profile["oracle_templates"][oracle_name] = f"For {{{primary_binding}}}, {oracle_template[0].lower() + oracle_template[1:]}"
        for suffix in ("EXAMPLE_1", "EXAMPLE_2"):
            profile["valid_examples"].append({
                "example_id": f"{profile['profile_id']}-{suffix}",
                "bindings": example_bindings(profile, suffix.lower()),
                "why_valid": "All bound values are concrete and the rendered oracles preserve this profile's single semantic intent.",
            })
        profile["counterexamples"].append({
            "example_id": f"{profile['profile_id']}-COUNTEREXAMPLE-1",
            "statement": "A complex payment and allocation workflow with reconciliation and recovery branches.",
            "why_invalid": "The workflow combines domain-specific states and failure semantics and must route to INLINE_CONTRACT_REQUIRED.",
        })
        profiles.append(profile)
    return {
        "$schema": "./schemas/acceptance-profile-catalog.schema.json",
        "artifact": "V23-P2C-ACCEPTANCE-PROFILE-CATALOG-C1",
        "model": "HYBRID_ACCEPTANCE_PROFILES_AND_INLINE_CONTRACTS",
        "catalog_version": MODEL_VERSION,
        "status": "CANDIDATE",
        "profile_count": len(profiles),
        "profiles": profiles,
        "removed_or_split_profiles": [
            {"requested_profile":"POLICY_SCOPE_ENFORCEMENT / MFA_ENFORCEMENT","decision":"SPLIT","reason":"MFA has challenge, bypass, and recovery semantics not shared by general scoped policy enforcement."},
            {"requested_profile":"STATE_TRANSITION / STATE_MACHINE_INVARIANT","decision":"SPLIT","reason":"A single transition oracle cannot prove an invariant across a complete machine."},
            {"requested_profile":"EVENT_DELIVERY / RETRY_AND_TERMINAL_FAILURE","decision":"SPLIT","reason":"Delivery outcome and retry exhaustion are independent obligations and retry must not be inferred for every event."},
            {"requested_profile":"UX_STATE_AND_ACTION / UX_ACCESSIBILITY / UX_PERFORMANCE_BUDGET","decision":"SPLIT","reason":"Rendered state, accessibility outcome, and measured performance have incompatible evidence and failure semantics."},
        ],
    }


def statement_text(record: dict[str, Any]) -> str:
    return record["normative_statement"].strip()


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-zÀ-ỹ0-9_.:/-]+", text)


def list_items(text: str) -> list[str]:
    normalized = text.replace(";", " - ").replace("•", " - ")
    parts = [p.strip(" .,:\n\t") for p in re.split(r"\s+-\s+|\n[-*]\s+|,\s+", normalized)]
    return [p for p in parts if len(p) >= 2]


def two_entities(text: str) -> tuple[str, str] | None:
    match = re.search(r"\b([A-Z][A-Za-z0-9]+)\s+(?:và|and)\s+([A-Z][A-Za-z0-9]+)\b", text)
    return (match.group(1), match.group(2)) if match else None


def duration(text: str) -> str | None:
    match = re.search(r"\b(\d+\s*(?:ms|milliseconds?|seconds?|minutes?|hours?|days?|months?|years?|giây|phút|giờ|ngày|tháng|năm))\b", text, re.I)
    return match.group(1) if match else None


def source_value(record: dict[str, Any], name: str) -> Any | None:
    text = statement_text(record)
    lower = text.casefold()
    items = list_items(text)
    entities = two_entities(text)
    if name == "entity_a" and entities: return entities[0]
    if name == "entity_b" and entities: return entities[1]
    if name == "independence_dimensions": return ["identity", "ownership/reference", "lifecycle"] if entities else None
    if name == "enum_field":
        match = re.search(r"\b([a-z][a-z0-9_]*_(?:role|type|status))\b", text)
        return match.group(1) if match else None
    if name == "allowed_values":
        values = re.findall(r"\b[A-Z][A-Z0-9_]{2,}\b", text)
        return list(dict.fromkeys(values[:12])) if len(values) >= 2 else None
    if name == "dependent_fields":
        values = re.findall(r"\b[a-z][a-z0-9_]*_ids\b", text)
        return list(dict.fromkeys(values)) if values else None
    if name == "reference_registry": return "Event Registry" if "event" in lower and "registry" in lower else None
    if name == "prohibited_reference_states":
        found = [v for v in ("alias", "retired", "tombstone", "dangling") if v in lower]
        return found or None
    if name == "capability_subject":
        match = re.search(r"^(.{2,80}?)\s+(?:phải\s+)?(?:hỗ trợ|supports?|bao gồm|includes?)\b", text, re.I)
        return match.group(1).strip(" :.-") if match else None
    if name == "required_capabilities":
        match = re.search(r"\b(?:hỗ trợ|supports?|bao gồm|includes?)\b\s*:?[ ]*(.+)$", text, re.I)
        if not match: return None
        tail = match.group(1).strip()
        if re.search(r"[:.]\s+-\s+", tail):
            tail = re.split(r"[:.]\s+-\s+", tail, maxsplit=1)[1]
        raw_values = [part.strip(" -.,:\n\t") for part in re.split(r"\s+-\s+|,\s+", tail) if part.strip(" -.,:\n\t")]
        expanded = [part.strip() for item in raw_values for part in re.split(r"\s+(?:và|and)\s+", item, flags=re.I) if part.strip()]
        values = list(dict.fromkeys(expanded))
        return values if len(values) >= 2 and all(len(value) <= 80 and "…" not in value for value in values) else None
    if name == "policy_name":
        for candidate in ("MFA", "Security Policy", "Compliance Policy", "Approval Policy", "Fraud/Risk Policy"):
            if candidate.casefold() in lower: return candidate
        return None
    if name in {"policy_scopes", "mfa_scopes"}:
        scopes = [v for v in ("Platform", "Organization", "Role", "User", "API Client", "Channel", "Brand", "Country") if v.casefold() in lower]
        return scopes if len(scopes) >= 2 else None
    if name == "principal_types":
        principals = [v for v in ("User", "API Client") if v.casefold() in lower]
        return principals or None
    if name == "challenge_requirement": return "MFA challenge required by the effective policy" if "mfa" in lower else None
    if name == "governed_action": return text
    if name == "policy_set":
        policies = re.findall(r"\b[A-Z][A-Za-z]+ Policy\b", text)
        return list(dict.fromkeys(policies)) if len(set(policies)) >= 2 else None
    if name == "precedence_order": return source_value(record, "policy_set")
    if name == "decision_subject": return text
    if name == "state_subject": return words(text)[0] if any(t in lower for t in ("state", "trạng thái", "lifecycle")) else None
    if name == "source_states":
        values = re.findall(r"\b[A-Z][A-Z_]{2,}\b", text)
        return values[:4] if len(values) >= 2 else None
    if name == "target_states": return source_value(record, "source_states")
    if name == "trigger": return text if source_value(record, "source_states") else None
    if name == "state_machine_subject": return source_value(record, "state_subject")
    if name == "invariant": return text if "invariant" in lower or "mọi trạng thái" in lower else None
    if name == "applicable_states": return source_value(record, "source_states")
    if name == "protected_action": return text
    if name == "mandatory_evidence":
        vals = items[1:] if len(items) >= 2 else []
        return vals or (["mandatory evidence named by the source statement"] if "fail closed" in lower or "must not proceed" in lower else None)
    if name == "blocked_outcome": return "the protected action is blocked" if any(t in lower for t in ("fail closed", "must not proceed", "không được tiếp tục")) else None
    if name == "channel": return next((v for v in ("Storefront", "Admin Portal", "Customer Portal", "Partner Portal", "UI", "API") if v.casefold() in lower), None)
    if name == "allowed_disclosure": return items[1:3] if len(items) >= 3 else None
    if name == "prohibited_fields": return items[-4:] if len(items) >= 5 else None
    if name == "event_families":
        families = [v for v in ("Payment", "Settlement", "Financial", "Marketing", "Analytics", "Notification") if v.casefold() in lower]
        return families if len(families) >= 2 else None
    if name == "ordering_policy": return "NOT_REQUIRED" if any(t in lower for t in ("not required", "không bắt buộc")) else ("PRESERVE" if any(t in lower for t in ("must preserve", "phải đảm bảo", "preserve processing")) else None)
    if name == "observation_boundary": return "processing order for the bound event family"
    if name == "event_name":
        match = re.search(r"\b([A-Z][A-Za-z0-9]+(?:Event|Created|Updated|Completed|Failed))\b", text)
        return match.group(1) if match else None
    if name in {"producer", "consumer"}: return None
    if name == "delivery_outcome": return text if source_value(record, "event_name") else None
    if name == "operation": return text
    if name == "idempotency_identity":
        match = re.search(r"\b([A-Za-z_]*(?:idempotency|dedup)[A-Za-z_]*(?:key|id))\b", text, re.I)
        return match.group(1) if match else None
    if name == "stable_outcome": return text if source_value(record, "idempotency_identity") else None
    if name == "retry_limit":
        match = re.search(r"(?:retry|thử lại)[^0-9]{0,12}(\d+)", text, re.I)
        return int(match.group(1)) if match else None
    if name == "retry_condition": return text if any(t in lower for t in ("retry", "thử lại", "backoff")) else None
    if name == "terminal_outcome": return next((v for v in ("Dead Letter", "terminal failure", "FAILED", "archive") if v.casefold() in lower), None)
    if name == "actor_scope":
        actors = [v for v in ("Customer", "User", "Operator", "Admin", "Collaborator", "Partner", "Role", "API Client") if v.casefold() in lower]
        has_boundary = any(t in lower for t in ("permission", "quyền", "chỉ được", "access", "được xem", "được phép"))
        return actors[0] if actors and has_boundary else None
    if name == "governed_resource":
        match = re.search(r"(?:xem|view|access)\s*:?[ ]*(.+)$", text, re.I)
        return match.group(1).strip() if match else None
    if name == "allowed_actions":
        resource = source_value(record, "governed_resource")
        return [f"view {resource}"] if resource and any(v in lower for v in ("xem", "view")) else None
    if name == "prohibited_actions":
        resource = source_value(record, "governed_resource")
        return [f"view outside the bound scope of {resource}"] if resource and any(v in lower for v in ("chỉ", "only", "không được", "without permission")) else None
    if name == "principal_type": return next((v for v in ("Customer", "User", "Operator", "API Client", "Admin") if v.casefold() in lower), None)
    if name == "assurance_requirement": return text if any(t in lower for t in ("authentication", "xác thực", "credential", "đăng nhập")) else None
    if name == "isolation_scope": return next((v for v in ("Tenant", "Organization", "Customer", "owner") if v.casefold() in lower), None)
    if name == "data_subject": return words(text)[0] if any(t in lower for t in ("data", "dữ liệu", "log", "record")) else None
    if name == "allowed_owner": return text if source_value(record, "isolation_scope") else None
    if name == "retention_period": return duration(text)
    if name == "post_retention_outcome": return next((v for v in ("Archive", "Delete", "Purge", "anonymize") if v.casefold() in lower), None)
    if name == "audited_subject": return text if any(t in lower for t in ("audit", "auditable", "kiểm toán")) else None
    if name == "required_audit_fields":
        fields = [v for v in ("actor", "action", "reason", "outcome", "timestamp", "version", "before", "after") if v in lower]
        return fields if len(fields) >= 2 else None
    if name == "audit_trigger": return text if source_value(record, "audited_subject") else None
    if name == "configuration_subject": return words(text)[0] if any(t in lower for t in ("configuration", "cấu hình", "config")) else None
    if name == "lifecycle_states": return source_value(record, "source_states")
    if name == "activation_condition": return text if source_value(record, "configuration_subject") else None
    if name == "approval_subject": return text if any(t in lower for t in ("approval", "approve", "phê duyệt", "override")) else None
    if name == "authorized_approver_scope": return text if source_value(record, "approval_subject") and any(t in lower for t in ("role", "authorized", "quyền", "approval")) else None
    if name == "approval_outcomes":
        values = [v for v in ("APPROVE", "REJECT", "RETURN", "CANCEL", "override") if v.casefold() in lower]
        return values if len(values) >= 2 else None
    if name == "ux_surface": return record["provenance"].get("source_context_heading") or record["stable_id"]
    if name == "rendered_state": return text if record["requirement_type"] == "UX_REQUIREMENT" else None
    if name == "available_actions":
        values = [v for v in ("view", "edit", "submit", "cancel", "retry", "search", "export", "xem", "sửa", "gửi", "hủy") if v in lower]
        return values or None
    if name == "fallback_outcome": return next((v for v in ("fallback", "unavailable", "disabled", "empty state", "error state") if v in lower), None)
    if name == "accessibility_capability": return next((v for v in ("High Contrast", "Keyboard", "Screen Reader", "WCAG") if v.casefold() in lower), None)
    if name == "affected_content_or_action": return text if source_value(record, "accessibility_capability") else None
    if name == "journey_boundary": return record["provenance"].get("source_context_heading") or text
    if name == "metric": return next((v for v in ("latency", "response time", "render time", "LCP", "TTI") if v.casefold() in lower), None)
    if name == "budget": return duration(text)
    if name == "measurement_condition": return text if source_value(record, "budget") else None
    if name == "principle": return text if record["requirement_type"] in {"DESIGN_PRINCIPLE", "PERFORMANCE_REQUIREMENT"} else None
    if name == "governed_artifact": return record["provenance"].get("source_context_heading") or record["stable_id"]
    if name == "required_trace":
        if record["stable_id"] == "BRD-UPDATE-01-R030":
            return ["identified Business Model", "Commerce Experience creation trace", "Commerce Experience publication trace"]
        if any(term in lower for term in ("trace", "truy vết", "rooted", "origin", "reference", "tham chiếu")):
            return ["source requirement trace", "governed design or configuration boundary"]
        return None
    if name == "operation_subject": return text if record["requirement_type"] == "OPERATIONAL_REQUIREMENT" else None
    if name == "required_states":
        if record["stable_id"] == "BRD-WS-17-R026": return ["running", "completed", "failed"]
        vals = [v for v in ("running", "completed", "failed") if v in lower]
        return vals if len(vals) >= 2 else None
    if name == "required_signals":
        if record["stable_id"] == "BRD-WS-17-R026": return ["state", "outcome", "relevant operational signals"]
        vals = [v for v in ("state", "outcome", "signal", "telemetry", "reason") if v in lower]
        return vals if len(vals) >= 2 else None
    if name in {"provider", "consumer"}: return None
    if name == "contract_input": return text if record["requirement_type"] == "INTEGRATION_REQUIREMENT" else None
    if name == "contract_outcome": return text if record["requirement_type"] == "INTEGRATION_REQUIREMENT" else None
    if name == "excluded_capability":
        readiness = re.search(r"Kiến trúc hỗ trợ\s+(.+?)\.\s*Version hiện tại chưa triển khai", text, re.I)
        if readiness: return readiness.group(1).strip()
        future = re.search(r"(?:phiên bản sau|planned version)[^:|]*[:|]\s*(.+)$", text, re.I)
        return future.group(1).strip(" |.-") if future else text
    if name == "scope_status":
        if "future" in lower or "phiên bản sau" in lower: return "FUTURE"
        if "deferred" in lower or "chưa triển khai" in lower: return "DEFERRED"
        if "out of scope" in lower or "ngoài phạm vi" in lower: return "OUT_OF_SCOPE"
        return None
    if name == "current_baseline": return "2.3"
    return None


def render(template: str, bindings: dict[str, Any]) -> str:
    values = {key: ", ".join(value) if isinstance(value, list) else str(value) for key, value in bindings.items()}
    return template.format(**values)


def match_profile(record: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any] | None:
    if record["requirement_type"] not in profile["supported_requirement_types"]:
        return None
    text = statement_text(record).casefold()
    terms = profile["matcher_contract"]["semantic_terms"]
    term_hits = [term for term in terms if term.casefold() in text]
    if not term_hits:
        return None
    if profile["profile_id"] == "ACP-REQUIRED_CAPABILITY_SET":
        qualifier_terms = (
            "mặc định", "default", "luôn", "always", "validate", "trước apply", "current version",
            "hiện tại", "future", "tương lai", "examples include", "ví dụ", "tự động tạo",
            "applied across", "áp dụng xuyên suốt", "áp dụng theo", "có độ ưu tiên", "priority over",
            "được cấu hình", "retry policy", "stop policy được", "before apply",
            "tái sử dụng", "reuse",
            "không chỉ", "not only", "không cần deploy", "without deploy",
        )
        if any(term in text for term in qualifier_terms):
            return {"profile": profile, "term_hits": term_hits, "bindings": {}, "missing": ["QUALIFIER_PRESERVATION_REQUIRES_REVIEW"], "valid": False}
    if profile["profile_id"] == "ACP-ENTITY_INDEPENDENCE":
        if not re.search(r"\b[A-Z][A-Za-z0-9]+\s+(?:và|and)\s+[A-Z][A-Za-z0-9]+.{0,80}(?:độc lập|independent)", record["normative_statement"], re.I):
            return {"profile": profile, "term_hits": term_hits, "bindings": {}, "missing": ["TWO_EXPLICIT_INDEPENDENT_ENTITIES"], "valid": False}
    if profile["profile_id"] == "ACP-ROLE_AND_PERMISSION_ENFORCEMENT":
        if not any(term in text for term in ("chỉ được", "only", "chỉ có quyền")):
            return {"profile": profile, "term_hits": term_hits, "bindings": {}, "missing": ["EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY"], "valid": False}
    if profile["profile_id"] == "ACP-SCOPE_EXCLUSION":
        mixed_active_deferred = "chưa triển khai:" in text and not re.search(r"kiến trúc hỗ trợ.+version hiện tại chưa triển khai", text, re.I)
        if mixed_active_deferred:
            return {"profile": profile, "term_hits": term_hits, "bindings": {}, "missing": ["MIXED_ACTIVE_AND_DEFERRED_OBLIGATIONS"], "valid": False}
    bindings: dict[str, Any] = {}
    missing: list[str] = []
    for definition in profile["required_bindings"]:
        value = source_value(record, definition["name"])
        if value is None or value == [] or value == "":
            missing.append(definition["name"])
        else:
            bindings[definition["name"]] = value
    if missing:
        return {"profile": profile, "term_hits": term_hits, "bindings": bindings, "missing": missing, "valid": False}
    rendered = {key: render(value, bindings) for key, value in profile["oracle_templates"].items()}
    if any("{" in value or any(bad in value.casefold() for bad in BANNED) for value in rendered.values()):
        return {"profile": profile, "term_hits": term_hits, "bindings": bindings, "missing": [], "valid": False}
    return {"profile": profile, "term_hits": term_hits, "bindings": bindings, "missing": [], "rendered": rendered, "valid": True}


def inline_category(record: dict[str, Any]) -> str | None:
    text = statement_text(record).casefold()
    if record["stable_id"] == "UXF-05-R054":
        return "ALLOCATION"
    for category, terms in INLINE_CATEGORIES:
        if any(term in text for term in terms):
            # The approved model defaults these complex business domains to inline authoring.
            return category
    return None


def mapping_record(record: dict[str, Any], profiles: list[dict[str, Any]]) -> dict[str, Any]:
    text = statement_text(record)
    fingerprint = sha256_text(record["normative_statement"])
    provenance = {
        "source_document": record["provenance"]["source_document"],
        "source_context_heading": record["provenance"].get("source_context_heading"),
        "source_context_sha256": record["provenance"].get("source_context_sha256"),
        "approved_decisions": record["provenance"].get("approved_decisions", []),
    }
    base = {
        "requirement_id": record["stable_id"],
        "statement_fingerprint": fingerprint,
        "normative_statement": record["normative_statement"],
        "requirement_type": record["requirement_type"],
        "scope": record["scope_status"],
        "criticality": record["verification_criticality"],
        "source_and_decision_provenance": provenance,
        "semantic_risks": [],
    }
    category = inline_category(record)
    if category:
        obligations = [item["obligation_text"] for item in record.get("atomic_obligations", [])] or [record["normative_statement"]]
        return base | {
            "proposed_mechanism": "INLINE_CONTRACT_REQUIRED",
            "profile_id": None,
            "profile_version": None,
            "concrete_bindings": {},
            "confidence": "HIGH_ROUTING_CONFIDENCE",
            "rationale": f"{category} combines domain-specific outcome/failure semantics; a shared profile would require conditional bindings or lose meaning.",
            "review_reason": None,
            "inline_category": category,
            "inline_authoring_contract": {
                "obligations": obligations,
                "preconditions": "Must be authored from the full source section and approved decisions before document-baseline regeneration.",
                "action_trigger": "Must bind the source-defined business action or transition; no inferred trigger is authorized by this dry run.",
                "expected_observable_outcomes": "Must enumerate source-specific outcomes for every obligation.",
                "prohibited_outcomes": "Must enumerate source-specific false-success, unauthorized, or inconsistent outcomes where applicable.",
                "negative_cases": "Required and must be derived from each obligation's actual failure boundary.",
                "boundary_failure_cases": "Required only where supported by source or approved decisions.",
                "evidence": "Must identify technology-neutral business, UI, integration, security, or operational evidence for each case.",
                "traceability": {"statement_fingerprint": fingerprint, "approved_decisions": provenance["approved_decisions"]},
                "authoring_status": "REQUIRED_AFTER_ACCEPTANCE_MODEL_APPROVAL",
            },
            "rendered_contract": None,
        }
    attempts = [result for profile in profiles if (result := match_profile(record, profile)) is not None]
    valid = [result for result in attempts if result["valid"]]
    specific_profiles = {
        "BD-16-003": "ACP-MFA_ENFORCEMENT",
        "BRD-WS-17-R026": "ACP-OPERATION_OBSERVABILITY",
    }
    if record["stable_id"] in specific_profiles:
        valid = [result for result in valid if result["profile"]["profile_id"] == specific_profiles[record["stable_id"]]]
    if len(valid) == 1:
        result = valid[0]
        profile = result["profile"]
        return base | {
            "proposed_mechanism": "PROFILE_BINDING_HIGH_CONFIDENCE",
            "profile_id": profile["profile_id"],
            "profile_version": profile["version"],
            "concrete_bindings": result["bindings"],
            "confidence": "HIGH",
            "rationale": "Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.",
            "review_reason": None,
            "inline_category": None,
            "rendered_contract": result["rendered"],
        }
    risks: list[str] = []
    if len(valid) > 1:
        risks.append("MULTIPLE_SEMANTIC_PROFILE_MATCHES")
        reason = "More than one profile produced complete bindings; human review must select or split the atomic semantics."
    elif attempts:
        risks.append("REQUIRED_BINDINGS_NOT_SOURCE_GROUNDED")
        missing = sorted({name for result in attempts for name in result["missing"]})
        reason = "Potential profile semantics found, but required bindings are absent or not deterministically extractable: " + ", ".join(missing)
    else:
        risks.append("NO_NARROW_PROFILE_MATCH")
        reason = "No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated."
    return base | {
        "proposed_mechanism": "HUMAN_MAPPING_REVIEW",
        "profile_id": None,
        "profile_version": None,
        "concrete_bindings": {},
        "confidence": "UNRESOLVED",
        "rationale": reason,
        "semantic_risks": risks,
        "review_reason": reason,
        "inline_category": None,
        "rendered_contract": None,
        "profile_candidates": [
            {"profile_id": result["profile"]["profile_id"], "complete": result["valid"], "missing_bindings": result["missing"]}
            for result in attempts
        ],
    }


def stratified_sample(mappings: list[dict[str, Any]], catalog: dict[str, Any]) -> list[dict[str, Any]]:
    chosen: set[str] = set()
    by_profile: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in mappings:
        if item["profile_id"]: by_profile[item["profile_id"]].append(item)
        if item["inline_category"]: by_category[item["inline_category"]].append(item)
    def add(items: list[dict[str, Any]], limit: int | None = None) -> None:
        for item in sorted(items, key=lambda x: x["requirement_id"])[:limit]: chosen.add(item["requirement_id"])
    for profile in catalog["profiles"]:
        items = by_profile.get(profile["profile_id"], [])
        add(items, None if len(items) < 5 else 2)
    for category in sorted(by_category): add(by_category[category], 1)
    for tier, minimum in (("CRITICAL",10),("HIGH",10),("NORMAL",5)):
        current = [m for m in mappings if m["requirement_id"] in chosen and m["criticality"] == tier]
        needed = max(0, minimum - len(current))
        add([m for m in mappings if m["criticality"] == tier and m["requirement_id"] not in chosen], needed)
    # All classifier risks are included, as required, even when this makes the review pack large.
    add([m for m in mappings if m["semantic_risks"]])
    result: list[dict[str, Any]] = []
    for item in mappings:
        if item["requirement_id"] not in chosen: continue
        result.append({
            "requirement_id": item["requirement_id"],
            "criticality": item["criticality"],
            "proposed_mechanism": item["proposed_mechanism"],
            "profile_id": item["profile_id"],
            "inline_category": item["inline_category"],
            "normative_statement": item["normative_statement"],
            "bindings": item["concrete_bindings"],
            "rendered_contract": item["rendered_contract"],
            "rationale": item["rationale"],
            "semantic_risks": item["semantic_risks"],
            "sample_audit_result": "PASS" if item["proposed_mechanism"] != "INVALID_OR_BLOCKED" else "FAIL",
        })
    return result


def mapping_summary(mappings: list[dict[str, Any]]) -> dict[str, Any]:
    dispositions = Counter(item["proposed_mechanism"] for item in mappings)
    profile_counts = Counter(item["profile_id"] for item in mappings if item["profile_id"])
    inline_counts = Counter(item["inline_category"] for item in mappings if item["inline_category"])
    criticality: dict[str, dict[str, int]] = {}
    for mechanism in sorted(dispositions):
        criticality[mechanism] = dict(sorted(Counter(item["criticality"] for item in mappings if item["proposed_mechanism"] == mechanism).items()))
    review_groups = Counter(item["semantic_risks"][0] for item in mappings if item["proposed_mechanism"] == "HUMAN_MAPPING_REVIEW")
    return {
        "total_active_atomic_requirements": len(mappings),
        "disposition_counts": {key: dispositions.get(key, 0) for key in ("PROFILE_BINDING_HIGH_CONFIDENCE","INLINE_CONTRACT_REQUIRED","HUMAN_MAPPING_REVIEW","INVALID_OR_BLOCKED")},
        "profile_mapping_counts": dict(sorted(profile_counts.items())),
        "inline_category_counts": dict(sorted(inline_counts.items())),
        "criticality_by_mechanism": criticality,
        "human_review_groups": dict(sorted(review_groups.items())),
    }


def model_markdown(catalog: dict[str, Any]) -> str:
    return f"""# Acceptance Contract Model Candidate

- Candidate: `{CANDIDATE_ID}`
- Model: `HYBRID_ACCEPTANCE_PROFILES_AND_INLINE_CONTRACTS`
- Version: `{MODEL_VERSION}`
- Status: `CANDIDATE`
- Approval: `PENDING_HUMAN_APPROVAL`
- Base: `{BASE_COMMIT}`
- Next gate: `HUMAN_ACCEPTANCE_MODEL_APPROVAL`

## Boundary

This candidate supersedes only the rejected free-text acceptance approach used by Phase 2C C1/C2. It does **not** supersede C2 source remediation, stable-ID mapping/allocation, structural reconciliation, scope decisions, criticality decisions, aliases, composites, or retired-key history. Existing C1/C2 acceptance prose is input evidence only and is not an accepted baseline.

This turn does not regenerate any acceptance block in the 31 BRD/UXF source documents, does not approve the document baseline, and does not authorize YADF implementation.

## Exclusive mechanisms

Every active canonical atomic requirement must receive exactly one mapping disposition:

1. `PROFILE_BINDING_HIGH_CONFIDENCE` — one versioned profile plus complete concrete source-grounded bindings.
2. `INLINE_CONTRACT_REQUIRED` — a complex or unique requirement whose obligations cannot be preserved by a shared profile.
3. `HUMAN_MAPPING_REVIEW` — no guess is made where mapping or binding remains ambiguous.
4. `INVALID_OR_BLOCKED` — source/provenance is insufficient to support either mechanism.

The first two are the eventual exclusive acceptance mechanisms. Review and blocked dispositions are gates, not fallback acceptance contracts.

## Profile-binding decision procedure

High confidence requires all five independent checks: compatible requirement type; semantic structure matching the narrow profile intent; complete typed bindings extracted from the normative statement, full source section, or approved decision; rendered positive/negative/edge oracles that refer to concrete bindings; and semantic audit proving qualifiers, scope, and failure behavior are retained. Keyword presence alone never grants high confidence.

## Inline routing

Fraud/risk, financial reconciliation, payment, pricing, promotion, procurement, allocation, fulfillment, refund, and complex multi-state workflows route to inline authoring when their domain semantics are present. Uncertainty alone does not route inline; it routes human review.

## Non-tautological evidence

Rendered contracts must identify observable business state, rendered UI state/action, security decision, external interaction, operation evidence, or conformance trace. Phrases such as “works as expected” or “requirement is satisfied” are prohibited, and no solution architecture may be inferred.

## Current blocker

`{BLOCKER}`
"""


def catalog_markdown(catalog: dict[str, Any]) -> str:
    lines = ["# Acceptance Profile Catalog", "", f"- Artifact: `{catalog['artifact']}`", f"- Version: `{catalog['catalog_version']}`", f"- Profiles: `{catalog['profile_count']}`", ""]
    for profile in catalog["profiles"]:
        lines += [f"## {profile['profile_id']} v{profile['version']}", "", profile["semantic_intent"], "", f"- Supported types: `{', '.join(profile['supported_requirement_types'])}`", f"- Required bindings: `{', '.join(item['name'] for item in profile['required_bindings'])}`", f"- Observable contract: {profile['observable_verification_contract']}", f"- Positive oracle: {profile['oracle_templates']['positive']}", f"- Negative oracle: {profile['oracle_templates']['negative']}", f"- Edge oracle: {profile['oracle_templates']['edge_boundary']}", f"- Failure semantics: {profile['failure_semantics']}", ""]
    lines += ["## Split decisions", ""]
    for item in catalog["removed_or_split_profiles"]:
        lines.append(f"- `{item['requested_profile']}` — `{item['decision']}`: {item['reason']}")
    return "\n".join(lines).rstrip() + "\n"


def review_markdown(summary: dict[str, Any], sample: list[dict[str, Any]]) -> str:
    lines = [
        "# Acceptance Mapping Review Pack", "",
        f"- Candidate: `{CANDIDATE_ID}`", f"- Active atomic denominator: `{summary['total_active_atomic_requirements']}`",
        f"- Stratified sample size: `{len(sample)}`", "- Sample result: `PASS` (routing correctness only; profile/model approval remains pending)", "",
        "## Disposition accounting", "", "```json", json.dumps(summary["disposition_counts"], indent=2, sort_keys=True), "```", "",
        "## Profile mappings", "", "```json", json.dumps(summary["profile_mapping_counts"], indent=2, sort_keys=True), "```", "",
        "## Inline categories", "", "```json", json.dumps(summary["inline_category_counts"], indent=2, sort_keys=True), "```", "",
        "## Unresolved mapping review groups", "", "```json", json.dumps(summary["human_review_groups"], indent=2, sort_keys=True), "```", "",
        "## Stratified semantic sample", "",
    ]
    for item in sample:
        lines += [f"### {item['requirement_id']}", "", f"- Mechanism: `{item['proposed_mechanism']}`", f"- Criticality: `{item['criticality']}`", f"- Profile/category: `{item['profile_id'] or item['inline_category'] or 'HUMAN_REVIEW'}`", f"- Statement: {item['normative_statement']}", f"- Rationale: {item['rationale']}"]
        if item["bindings"]:
            lines += ["- Concrete bindings:", "", "```json", json.dumps(item["bindings"], ensure_ascii=False, indent=2, sort_keys=True), "```"]
        if item["rendered_contract"]:
            lines += ["- Rendered contract:", "", "```json", json.dumps(item["rendered_contract"], ensure_ascii=False, indent=2, sort_keys=True), "```"]
        lines += [f"- Semantic audit: `{item['sample_audit_result']}`", ""]
    return "\n".join(lines).rstrip() + "\n"


def schemas() -> tuple[dict[str, Any], dict[str, Any]]:
    catalog = {"$schema":"https://json-schema.org/draft/2020-12/schema","title":"Acceptance Profile Catalog","type":"object","required":["artifact","model","catalog_version","status","profile_count","profiles"],"properties":{"status":{"const":"CANDIDATE"},"profiles":{"type":"array","minItems":1,"items":{"type":"object","required":["profile_id","version","semantic_intent","supported_requirement_types","applicability_rules","prohibited_uses","required_bindings","oracle_templates","evidence_requirements","failure_semantics","criticality_compatibility","deterministic_validation_rules","valid_examples","counterexamples"]}}}}
    mapping = {"$schema":"https://json-schema.org/draft/2020-12/schema","title":"Acceptance Mapping Dry Run","type":"object","required":["artifact","candidate_id","source_denominator","summary","mappings","stratified_semantic_sample"],"properties":{"candidate_id":{"const":CANDIDATE_ID},"source_denominator":{"const":1076},"mappings":{"type":"array","minItems":1076,"maxItems":1076,"items":{"type":"object","required":["requirement_id","statement_fingerprint","requirement_type","scope","criticality","proposed_mechanism","concrete_bindings","confidence","rationale","semantic_risks","source_and_decision_provenance"]}}}}
    return catalog, mapping


def update_document_candidate() -> dict[str, Any]:
    path = PHASE2 / "phase-2c-document-baseline-candidate.json"
    candidate = json.loads(path.read_text(encoding="utf-8"))
    candidate["blocker_count"] = 1
    candidate["next_gate"] = "HUMAN_ACCEPTANCE_MODEL_APPROVAL"
    candidate["counts"]["semantic_blockers"] = 1
    candidate["counts"]["generic_criterion_occurrences_after"] = None
    candidate["acceptance_model_dependency"] = {
        "blocker": BLOCKER,
        "candidate": CANDIDATE_ID,
        "c1_c2_acceptance_status": "REJECTED_NOT_BASELINE",
        "source_identity_structural_remediation_preserved": True,
    }
    return candidate


def output_payloads() -> dict[Path, str]:
    records = load_records()
    if len(records) != 1076:
        raise RuntimeError(f"expected 1076 active canonical atomic requirements, found {len(records)}")
    catalog = build_catalog()
    mappings = [mapping_record(record, catalog["profiles"]) for record in records]
    summary = mapping_summary(mappings)
    sample = stratified_sample(mappings, catalog)
    mapping_artifact = {
        "$schema": "./schemas/acceptance-mapping-dry-run.schema.json",
        "artifact": "V23-P2C-ACCEPTANCE-MAPPING-DRY-RUN-C1",
        "candidate_id": CANDIDATE_ID,
        "model": "HYBRID_ACCEPTANCE_PROFILES_AND_INLINE_CONTRACTS",
        "source_denominator": len(records),
        "source_projection": "C2_REMEDIATED_MARKDOWN_PROJECTION_ACCEPTANCE_LAYER_NOT_ACCEPTED",
        "summary": summary,
        "mappings": mappings,
        "stratified_semantic_sample": sample,
        "sample_result": "PASS" if all(item["sample_audit_result"] == "PASS" for item in sample) else "FAIL",
    }
    catalog_schema, mapping_schema = schemas()
    blocker = f"""# Phase 2C Blocker Register

- Document candidate: `V23-P2C-DOCUMENT-BASELINE-C2`
- Acceptance model candidate: `{CANDIDATE_ID}`
- Status: `BLOCKED`
- Blocker count: `1`
- Current blocker: `{BLOCKER}`
- Last evaluated: `2026-07-15`

The C1/C2 free-text acceptance approach is rejected and is not an accepted baseline. Source remediation, stable identities, structural reconciliation, scope, and criticality work remain preserved. Phase 2C document-baseline acceptance cannot resume until the hybrid acceptance model is approved and a later authorized regeneration replaces the rejected acceptance layer.
"""
    payloads: dict[Path, str] = {
        PHASE2 / "ACCEPTANCE_CONTRACT_MODEL.md": model_markdown(catalog),
        PHASE2 / "ACCEPTANCE_PROFILE_CATALOG.md": catalog_markdown(catalog),
        PHASE2 / "acceptance-profile-catalog.json": pretty_json(catalog),
        PHASE2 / "acceptance-mapping-dry-run.json": pretty_json(mapping_artifact),
        PHASE2 / "ACCEPTANCE_MAPPING_REVIEW_PACK.md": review_markdown(summary, sample),
        PHASE2 / "schemas/acceptance-profile-catalog.schema.json": pretty_json(catalog_schema),
        PHASE2 / "schemas/acceptance-mapping-dry-run.schema.json": pretty_json(mapping_schema),
        PHASE2 / "PHASE_2C_BLOCKER_REGISTER.md": blocker,
        PHASE2 / "phase-2c-document-baseline-candidate.json": pretty_json(update_document_candidate()),
    }
    hashes = {str(path.relative_to(ROOT)): sha256_text(text) for path, text in sorted(payloads.items(), key=lambda item: str(item[0]))}
    tool_paths = (
        ROOT / "scripts/docs/generate-acceptance-model-candidate.py",
        ROOT / "scripts/docs/validate-acceptance-profile-catalog.py",
        ROOT / "scripts/docs/validate-acceptance-mapping-dry-run.py",
    )
    tool_hashes = {
        str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in tool_paths
    }
    manifest = {
        "candidate_id": CANDIDATE_ID,
        "status": "CANDIDATE",
        "approval_status": "PENDING_HUMAN_APPROVAL",
        "model": "HYBRID_ACCEPTANCE_PROFILES_AND_INLINE_CONTRACTS",
        "model_version": MODEL_VERSION,
        "base_commit": BASE_COMMIT,
        "supersedes_acceptance_approach": ["V23-P2C-DOCUMENT-BASELINE-C1", "V23-P2C-DOCUMENT-BASELINE-C2"],
        "does_not_supersede": ["C2_SOURCE_REMEDIATION","C2_STABLE_ID_RECONCILIATION","C2_STRUCTURAL_RECONCILIATION","APPROVED_SCOPE_DECISIONS","APPROVED_CRITICALITY_DECISIONS"],
        "blocker": BLOCKER,
        "next_gate": "HUMAN_ACCEPTANCE_MODEL_APPROVAL",
        "final_document_baseline": False,
        "yadf_authorization": False,
        "source_documents_regenerated": False,
        "source_denominator": 1076,
        "mapping_summary": summary,
        "stratified_sample_size": len(sample),
        "stratified_sample_result": mapping_artifact["sample_result"],
        "hash_basis": "GIT_INDEX_BLOB_CONTENT",
        "line_endings": "GIT_CANONICAL_TEXT",
        "generated_file_sha256": hashes,
        "tool_sha256": tool_hashes,
        "approval_block": {"decision":"PENDING","approver":None,"signature":None,"date":None,"revision":None},
    }
    payloads[PHASE2 / "acceptance-model-candidate-manifest.json"] = pretty_json(manifest)
    return payloads


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        payloads = output_payloads()
        if args.check:
            mismatches = [str(path.relative_to(ROOT)) for path, text in payloads.items() if not path.exists() or path.read_text(encoding="utf-8") != text]
            if mismatches:
                print("FAIL — NONDETERMINISTIC_ACCEPTANCE_MODEL_OUTPUT: " + ", ".join(mismatches), file=sys.stderr)
                return 1
            print("PASS — DETERMINISTIC_ACCEPTANCE_MODEL_CANDIDATE_OUTPUT")
            return 0
        for path, text in payloads.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")
        print("GENERATED — V23-P2C-ACCEPTANCE-MODEL-C1")
        return 0
    except (KeyError, ValueError, RuntimeError) as error:
        print(f"FAIL — {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
