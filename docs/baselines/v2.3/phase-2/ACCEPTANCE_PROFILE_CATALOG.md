# Acceptance Profile Catalog

- Artifact: `V23-P2C-ACCEPTANCE-PROFILE-CATALOG-C1`
- Version: `1.0.0-candidate.1`
- Profiles: `28`

## ACP-ENTITY_INDEPENDENCE v1.0.0

Verify that named entities retain distinct identity, ownership/reference, and lifecycle boundaries.

- Supported types: `DATA_REQUIREMENT, INTEGRATION_REQUIREMENT, BUSINESS_RULE`
- Required bindings: `entity_a, entity_b, independence_dimensions`
- Observable contract: identity, owner/reference, and lifecycle comparisons for both bound entities
- Positive oracle: Given {entity_a} and {entity_b}, when identity, ownership/reference, and lifecycle evidence is compared, then each entity remains independently identifiable and governed across {independence_dimensions}.
- Negative oracle: Given a candidate that merges {entity_a} with {entity_b}, when entity integrity is validated, then the conflation is rejected with the violated independence dimension identified.
- Edge oracle: For {entity_a}, given one entity changes lifecycle state, when the relationship is observed, then the other entity changes only through an explicit independently authorized transition.
- Failure semantics: Reject conflated identity or implicit lifecycle coupling.

## ACP-ENUM_REFERENCE_INTEGRITY v1.0.0

Verify an enumerated discriminator, dependent-field consistency, and canonical registry references.

- Supported types: `DATA_REQUIREMENT, BUSINESS_RULE`
- Required bindings: `enum_field, allowed_values, dependent_fields, reference_registry, prohibited_reference_states`
- Observable contract: accepted/rejected field values, dependent-field validation, and canonical reference resolution
- Positive oracle: Given {enum_field} and {dependent_fields}, when a record is validated, then only {allowed_values} and role-consistent fields with references resolving in {reference_registry} are accepted.
- Negative oracle: Given an unsupported {enum_field} value or inconsistent {dependent_fields}, when validation runs, then the record is rejected and the invalid field is identified.
- Edge oracle: Given references in {prohibited_reference_states}, when canonical resolution runs, then every prohibited or dangling reference is rejected.
- Failure semantics: Reject the complete inconsistent record; do not persist partial reference state.

## ACP-REQUIRED_CAPABILITY_SET v1.0.0

Verify that a named subject exposes every explicitly enumerated required capability without inventing additional capabilities.

- Supported types: `BUSINESS_REQUIREMENT, BUSINESS_DECISION, UX_REQUIREMENT, OPERATIONAL_REQUIREMENT`
- Required bindings: `capability_subject, required_capabilities`
- Observable contract: capability inventory and an observable outcome for each bound capability
- Positive oracle: Given {capability_subject}, when its capability inventory is inspected, then every member of {required_capabilities} is independently available and attributable to that subject.
- Negative oracle: For {capability_subject}, given one bound capability is absent or attributed to another subject, when completeness is evaluated, then the missing or misattributed member is reported.
- Edge oracle: Given a capability outside {required_capabilities}, when conformance is evaluated, then it is not used as evidence that a missing bound capability exists.
- Failure semantics: Report the exact missing bound member; no aggregate pass from partial coverage.

## ACP-POLICY_SCOPE_ENFORCEMENT v1.0.0

Verify independent policy configuration and enforcement at explicitly named scopes.

- Supported types: `SECURITY_REQUIREMENT, BUSINESS_RULE, BUSINESS_DECISION`
- Required bindings: `policy_name, policy_scopes, governed_action`
- Observable contract: configured policies, effective scope resolution, and allow/challenge/deny outcome
- Positive oracle: Given {policy_name} configured at each of {policy_scopes}, when {governed_action} is evaluated, then the effective policy identifies and enforces every applicable bound scope.
- Negative oracle: Given a principal outside a required policy condition, when {governed_action} is attempted, then the action is denied or challenged by the effective bound policy.
- Edge oracle: Given overlapping policies across {policy_scopes}, when policy resolution runs, then contributing scopes and the effective result are observable without silently dropping a scope.
- Failure semantics: Fail closed when a mandatory applicable scope cannot be resolved.

## ACP-POLICY_PRECEDENCE v1.0.0

Verify deterministic resolution when two or more named policies apply.

- Supported types: `BUSINESS_RULE, SECURITY_REQUIREMENT, PRIVACY_REQUIREMENT`
- Required bindings: `policy_set, precedence_order, decision_subject`
- Observable contract: applicable policy set, selected policy, precedence reason, and decision
- Positive oracle: Given {policy_set} applies to {decision_subject}, when precedence is resolved, then the selected policy follows {precedence_order} and the selection reason is recorded.
- Negative oracle: For {policy_set}, given a lower-precedence policy conflicts with a higher-precedence policy, when resolution runs, then the lower-precedence outcome does not take effect.
- Edge oracle: For {policy_set}, given equal-precedence or incomplete policy metadata, when resolution runs, then no silent winner is selected and the conflict is surfaced deterministically.
- Failure semantics: Block an ambiguous policy decision rather than inventing precedence.

## ACP-STATE_TRANSITION v1.0.0

Verify an explicitly named source state, trigger, target state, and prohibited transition.

- Supported types: `BUSINESS_RULE, BUSINESS_REQUIREMENT, OPERATIONAL_REQUIREMENT`
- Required bindings: `state_subject, source_states, trigger, target_states`
- Observable contract: before state, trigger, transition decision, after state, and reason
- Positive oracle: Given {state_subject} in {source_states}, when {trigger} occurs, then only the bound target in {target_states} is reached and the transition is observable.
- Negative oracle: Given {state_subject} outside {source_states}, when {trigger} occurs, then no prohibited target transition is recorded.
- Edge oracle: For {state_subject}, given a missing trigger prerequisite or terminal state, when transition is requested, then the request produces a deterministic rejection with unchanged state.
- Failure semantics: Reject prohibited transitions without partial state mutation.

## ACP-STATE_MACHINE_INVARIANT v1.0.0

Verify an invariant that must hold across all bound states and transitions.

- Supported types: `BUSINESS_RULE, OPERATIONAL_REQUIREMENT`
- Required bindings: `state_machine_subject, invariant, applicable_states`
- Observable contract: state history and invariant evaluation at each bound state
- Positive oracle: Given {state_machine_subject} traverses {applicable_states}, when each transition is evaluated, then {invariant} holds before and after every accepted transition.
- Negative oracle: Given a transition that would violate {invariant}, when it is requested, then the transition is rejected with the invariant violation identified.
- Edge oracle: Given recovery from an intermediate or terminal failure, when state is restored or advanced, then {invariant} remains true and the recovery transition is recorded.
- Failure semantics: Do not accept any transition that leaves the invariant false.

## ACP-FAIL_CLOSED_BOUNDARY v1.0.0

Verify an explicit mandatory-evidence or assurance boundary that prohibits success when unresolved.

- Supported types: `SECURITY_REQUIREMENT, PRIVACY_REQUIREMENT, DATA_REQUIREMENT, INTEGRATION_REQUIREMENT, UX_REQUIREMENT`
- Required bindings: `protected_action, mandatory_evidence, blocked_outcome`
- Observable contract: evidence validation, allow/deny result, protected-state comparison, and reason
- Positive oracle: Given valid {mandatory_evidence}, when {protected_action} is requested, then evaluation may proceed and records the validated evidence.
- Negative oracle: Given missing or invalid {mandatory_evidence}, when {protected_action} is requested, then {blocked_outcome} and protected state is unchanged.
- Edge oracle: For {protected_action}, given evidence cannot be resolved conclusively, when the boundary is evaluated, then the unresolved result follows the same blocked outcome rather than defaulting to success.
- Failure semantics: No success or partial protected-state change without all mandatory evidence.

## ACP-NO_INTERNAL_DISCLOSURE v1.0.0

Verify allowed external disclosure and absence of explicitly prohibited internal fields.

- Supported types: `UX_REQUIREMENT, PRIVACY_REQUIREMENT, SECURITY_REQUIREMENT`
- Required bindings: `channel, allowed_disclosure, prohibited_fields`
- Observable contract: rendered fields, external payload field inventory, and prohibited-field absence
- Positive oracle: Given {channel}, when customer-facing disclosure is produced, then only {allowed_disclosure} is present and remains read-only where bound.
- Negative oracle: Given internal values for {prohibited_fields}, when the UI and external payload are inspected, then none of those fields or values is disclosed.
- Edge oracle: For {channel}, given allowed disclosure data is unavailable, when disclosure is mandatory, then the affected action follows its explicit fail-closed outcome without substituting internal data.
- Failure semantics: Do not expose prohibited internal data through UI, payload, fallback, or derived labels.

## ACP-EVENT_ORDERING v1.0.0

Verify whether explicitly bound event families must preserve or need not preserve processing order.

- Supported types: `DESIGN_PRINCIPLE, INTEGRATION_REQUIREMENT, BUSINESS_RULE`
- Required bindings: `event_families, ordering_policy, observation_boundary`
- Observable contract: event-family identity, observed processing order, and policy conformance result
- Positive oracle: Given events from {event_families}, when processing is observed at {observation_boundary}, then behavior conforms to {ordering_policy} without applying another family's policy.
- Negative oracle: Given an event family outside {event_families}, when ordering is evaluated, then this profile binding is not used as its ordering authority.
- Edge oracle: For {event_families}, given interleaved events across bound families, when conformance is reviewed, then the policy is evaluated per family and does not infer cross-family ordering.
- Failure semantics: Report policy violation only where PRESERVE is bound; never infer ordering for NOT_REQUIRED.

## ACP-EVENT_DELIVERY v1.0.0

Verify an explicit event producer, consumer, delivery outcome, and terminal failure boundary.

- Supported types: `INTEGRATION_REQUIREMENT, BUSINESS_REQUIREMENT, OPERATIONAL_REQUIREMENT`
- Required bindings: `event_name, producer, consumer, delivery_outcome`
- Observable contract: published event identity, consumer receipt/outcome, and terminal delivery evidence
- Positive oracle: Given {producer} emits {event_name}, when delivery to {consumer} is evaluated, then {delivery_outcome} is observable and attributable to the same event identity.
- Negative oracle: Given an invalid or unauthorized {event_name}, when delivery is attempted, then it is rejected before producing the bound consumer outcome.
- Edge oracle: For {event_name}, given terminal delivery failure, when delivery evidence is inspected, then the final failure and affected event identity are visible for controlled remediation.
- Failure semantics: Never report delivery success without consumer-bound observable evidence.

## ACP-IDEMPOTENT_OPERATION v1.0.0

Verify explicit repeated-operation semantics under a bound idempotency identity.

- Supported types: `INTEGRATION_REQUIREMENT, BUSINESS_RULE, OPERATIONAL_REQUIREMENT`
- Required bindings: `operation, idempotency_identity, stable_outcome`
- Observable contract: operation attempts, bound identity, outcome identity, and side-effect comparison
- Positive oracle: Given {operation} with {idempotency_identity}, when the same request is repeated, then {stable_outcome} is returned without an additional business side effect.
- Negative oracle: For {operation}, given two requests with different valid identities, when both are processed, then one identity is not incorrectly deduplicated as the other.
- Edge oracle: For {operation}, given an in-flight or partially observed first attempt, when the same identity is retried, then the eventual bound outcome remains singular and traceable.
- Failure semantics: Prevent duplicate business effects for the same bound identity.

## ACP-RETRY_AND_TERMINAL_FAILURE v1.0.0

Verify an explicitly bounded retry policy and observable terminal outcome.

- Supported types: `OPERATIONAL_REQUIREMENT, INTEGRATION_REQUIREMENT`
- Required bindings: `operation, retry_limit, retry_condition, terminal_outcome`
- Observable contract: attempt sequence, retry reason, applied limit/policy, and terminal outcome
- Positive oracle: Given {operation} fails under {retry_condition}, when retry policy applies, then attempts follow {retry_limit} and each attempt is observable.
- Negative oracle: For {operation}, given a non-retryable failure, when failure is classified, then no retry is started and the reason is recorded.
- Edge oracle: Given retries reach {retry_limit}, when the final attempt fails, then {terminal_outcome} is emitted exactly as bound and remains operator-visible.
- Failure semantics: Do not retry outside the bound condition or conceal exhaustion.

## ACP-ROLE_AND_PERMISSION_ENFORCEMENT v1.0.0

Verify explicitly bound actor, resource/action, and permission boundary.

- Supported types: `SECURITY_REQUIREMENT, BUSINESS_RULE, BUSINESS_REQUIREMENT`
- Required bindings: `actor_scope, governed_resource, allowed_actions, prohibited_actions`
- Observable contract: principal and scope, effective permission, available/denied action, protected-state comparison, and audit evidence
- Positive oracle: Given {actor_scope}, when access to {governed_resource} is evaluated, then only {allowed_actions} are available within the bound scope.
- Negative oracle: Given the same actor requests {prohibited_actions}, when authorization is evaluated, then the action is denied and protected state remains unchanged.
- Edge oracle: For {actor_scope}, given ownership or scope attribution is missing or conflicting, when access is evaluated, then no broader access is inferred and the unresolved boundary is denied.
- Failure semantics: Deny access outside the concretely bound actor/resource/action scope.

## ACP-AUTHENTICATION_REQUIREMENT v1.0.0

Verify a named assurance or credential requirement at an authentication boundary.

- Supported types: `SECURITY_REQUIREMENT`
- Required bindings: `principal_type, assurance_requirement, protected_action`
- Observable contract: principal, assurance evidence, challenge/allow/deny result, and audit reason
- Positive oracle: Given {principal_type} presents evidence satisfying {assurance_requirement}, when {protected_action} is attempted, then authentication succeeds at the bound assurance level.
- Negative oracle: Given missing or invalid assurance evidence, when {protected_action} is attempted, then authentication is denied or challenged without granting the protected action.
- Edge oracle: For {principal_type}, given assurance cannot be resolved or has expired, when authentication is evaluated, then no previous success is reused outside its validity boundary.
- Failure semantics: Fail closed at the stated assurance boundary.

## ACP-MFA_ENFORCEMENT v1.0.0

Verify MFA policy, effective scope resolution, required challenge, bypass denial, and applicable recovery.

- Supported types: `SECURITY_REQUIREMENT`
- Required bindings: `mfa_scopes, principal_types, challenge_requirement`
- Observable contract: scope policies, effective resolution, challenge result, bypass decision, and audit evidence
- Positive oracle: Given MFA policies at {mfa_scopes} for {principal_types}, when effective policy is resolved, then {challenge_requirement} is presented and must be satisfied.
- Negative oracle: For {mfa_scopes}, given a required challenge is missing, invalid, or bypassed, when the protected action is attempted, then access is denied and the attempt is audited.
- Edge oracle: For {mfa_scopes}, given overlapping scope policies or an applicable approved recovery flow, when MFA is evaluated, then effective scopes and recovery-specific assurance are explicit without silently disabling MFA.
- Failure semantics: No protected action succeeds while an effective MFA requirement is unsatisfied.

## ACP-DATA_ISOLATION v1.0.0

Verify explicit tenant, organization, owner, or subject isolation at read and mutation boundaries.

- Supported types: `SECURITY_REQUIREMENT, PRIVACY_REQUIREMENT, DATA_REQUIREMENT, BUSINESS_RULE`
- Required bindings: `isolation_scope, data_subject, allowed_owner`
- Observable contract: requesting scope, data ownership, returned records, mutation result, and denial evidence
- Positive oracle: Given {allowed_owner} in {isolation_scope}, when {data_subject} is read or changed, then only records attributed to that bound owner and scope are available.
- Negative oracle: Given a record outside {isolation_scope} or not owned by {allowed_owner}, when access is attempted, then no record or mutation is disclosed and the decision is denied.
- Edge oracle: For {isolation_scope}, given missing or conflicting ownership attribution, when isolation is evaluated, then broader scope is not inferred and access fails closed.
- Failure semantics: Prevent cross-scope disclosure or mutation.

## ACP-DATA_RETENTION v1.0.0

Verify an explicit retention duration, online/archive boundary, and post-retention outcome.

- Supported types: `PRIVACY_REQUIREMENT, OPERATIONAL_REQUIREMENT, BUSINESS_RULE`
- Required bindings: `data_subject, retention_period, post_retention_outcome`
- Observable contract: data age, online availability, archive/deletion state, transition time, and policy reference
- Positive oracle: Given {data_subject} within {retention_period}, when availability is inspected, then the bound online or retained state is observable.
- Negative oracle: Given {data_subject} beyond {retention_period}, when online availability is inspected, then it is not retained online contrary to policy.
- Edge oracle: Given the retention boundary is crossed, when policy applies, then {post_retention_outcome} occurs with transition evidence tied to the same data identity.
- Failure semantics: Do not retain or remove data contrary to the bound duration and outcome.

## ACP-AUDITABILITY v1.0.0

Verify that a named decision or operation records required actor, action, reason, version, and outcome evidence.

- Supported types: `OPERATIONAL_REQUIREMENT, SECURITY_REQUIREMENT, BUSINESS_RULE`
- Required bindings: `audited_subject, required_audit_fields, audit_trigger`
- Observable contract: audit record tied to subject identity with every bound field resolvable
- Positive oracle: Given {audit_trigger} for {audited_subject}, when the outcome is recorded, then {required_audit_fields} are present and attributable to that same subject.
- Negative oracle: For {audited_subject}, given a record missing one bound audit field, when audit completeness is verified, then it is reported non-conforming with the missing field identified.
- Edge oracle: For {audited_subject}, given an override, failure, or recovery outcome, when auditing applies, then both original and effective outcome remain distinguishable where bound.
- Failure semantics: Do not claim auditability from an incomplete or unattributed record.

## ACP-CONFIGURATION_LIFECYCLE v1.0.0

Verify explicit draft, validation, activation, replacement, and retirement behavior for configuration.

- Supported types: `BUSINESS_RULE, OPERATIONAL_REQUIREMENT, DESIGN_PRINCIPLE`
- Required bindings: `configuration_subject, lifecycle_states, activation_condition`
- Observable contract: configuration identity/version, before/after state, validation result, and effective selection
- Positive oracle: Given {configuration_subject} in {lifecycle_states}, when {activation_condition} is satisfied, then the intended version becomes effective with its transition recorded.
- Negative oracle: For {configuration_subject}, given invalid or incomplete configuration, when activation is requested, then it does not become effective and the validation reason is observable.
- Edge oracle: For {configuration_subject}, given replacement or retirement, when effective configuration is resolved, then exactly the intended valid version is selected without silently reviving a retired version.
- Failure semantics: Prevent invalid, retired, or ambiguous configuration from becoming effective.

## ACP-APPROVAL_WORKFLOW v1.0.0

Verify an explicit approval eligibility, decision, reason, and governed action boundary.

- Supported types: `BUSINESS_RULE, SECURITY_REQUIREMENT, OPERATIONAL_REQUIREMENT`
- Required bindings: `approval_subject, authorized_approver_scope, approval_outcomes, governed_action`
- Observable contract: approver authorization, decision, reason, subject state, and audit evidence
- Positive oracle: Given {authorized_approver_scope} reviews {approval_subject}, when an outcome in {approval_outcomes} is selected, then {governed_action} follows that decision and records approver and reason.
- Negative oracle: For {approval_subject}, given an unauthorized actor or missing mandatory reason, when approval is attempted, then the decision is rejected and the governed action does not proceed.
- Edge oracle: For {approval_subject}, given approval is withdrawn, expires, or conflicts with a mandatory policy, when effectiveness is resolved, then the mandatory policy prevails and effective state is explicit.
- Failure semantics: Never treat an unauthorized or incomplete approval as effective.

## ACP-UX_STATE_AND_ACTION v1.0.0

Verify a named rendered state, available action, prohibited disclosure/action, and fallback outcome.

- Supported types: `UX_REQUIREMENT`
- Required bindings: `ux_surface, rendered_state, available_actions, fallback_outcome`
- Observable contract: rendered state, enabled/unavailable actions, visible confirmation, and payload-field inventory
- Positive oracle: Given {ux_surface}, when the bound journey state is reached, then {rendered_state} and {available_actions} are directly visible and actionable as specified.
- Negative oracle: For {ux_surface}, given an action or disclosure outside the bound state, when the surface is inspected, then it is unavailable or absent rather than silently enabled.
- Edge oracle: Given required journey input is unavailable, when the surface renders, then {fallback_outcome} is visible and no prohibited action proceeds.
- Failure semantics: Do not infer success from hidden state; required UI outcome must be observable.

## ACP-UX_ACCESSIBILITY v1.0.0

Verify a specifically named accessibility mode, interaction, or conformance outcome.

- Supported types: `ACCESSIBILITY_REQUIREMENT, UX_REQUIREMENT`
- Required bindings: `ux_surface, accessibility_capability, affected_content_or_action`
- Observable contract: enabled accessibility state, perceivable content, operable action, fallback, and conformance evidence
- Positive oracle: Given {accessibility_capability} is enabled on {ux_surface}, when {affected_content_or_action} is rendered or used, then the bound content remains perceivable and the action remains operable.
- Negative oracle: For {ux_surface}, given the accessibility capability is absent or broken, when the affected interaction is tested, then conformance fails with the inaccessible content or action identified.
- Edge oracle: For {ux_surface}, given fallback content or an unavailable primary interaction, when the accessible alternative applies, then the alternative is perceivable, operable, and exposes the same required outcome.
- Failure semantics: Do not claim accessibility from generic rendering evidence.

## ACP-UX_PERFORMANCE_BUDGET v1.0.0

Verify an explicit user-visible timing or responsiveness budget at a named journey boundary.

- Supported types: `PERFORMANCE_REQUIREMENT, UX_REQUIREMENT`
- Required bindings: `journey_boundary, metric, budget, measurement_condition`
- Observable contract: measurement condition, observed metric value, bound budget, and pass/fail result
- Positive oracle: Given {measurement_condition}, when {journey_boundary} is measured, then {metric} is within {budget} and the observed value is recorded.
- Negative oracle: Given the observed value exceeds {budget}, when conformance is evaluated, then the journey is reported outside budget with the measured value identified.
- Edge oracle: For {journey_boundary}, given incomplete measurement conditions or missing samples, when conformance is evaluated, then no budget pass is claimed until the bound condition is met.
- Failure semantics: Never invent a threshold or claim performance without a bound measurement.

## ACP-DESIGN_CONFORMANCE_TRACE v1.0.0

Verify traceability from a design principle to governed requirements, configuration, and architectural boundary without runtime tautology.

- Supported types: `DESIGN_PRINCIPLE, PERFORMANCE_REQUIREMENT`
- Required bindings: `principle, governed_artifact, required_trace`
- Observable contract: conformance decision, requirement/design/configuration trace, and named boundary violation
- Positive oracle: Given {governed_artifact}, when conformance to {principle} is reviewed, then {required_trace} is complete and the applicable design or configuration boundary is explicit.
- Negative oracle: For {principle}, given a missing trace or direct violation of the bound principle, when conformance is reviewed, then the artifact is reported non-conforming with the exact gap identified.
- Edge oracle: For {principle}, given the principle is not applicable to an artifact, when review runs, then non-applicability is justified from scope rather than treated as conformance evidence.
- Failure semantics: Do not substitute a generic runtime pass for design conformance.

## ACP-OPERATION_OBSERVABILITY v1.0.0

Verify named running/completed/failed state, outcome, signals, and detectable missing-evidence failure.

- Supported types: `OPERATIONAL_REQUIREMENT`
- Required bindings: `operation_subject, required_states, required_signals`
- Observable contract: operation identity, current/terminal state, outcome, signal values, and verification failure
- Positive oracle: Given {operation_subject} is in {required_states}, when an operator inspects it, then the matching state, outcome, and {required_signals} are observable.
- Negative oracle: For {operation_subject}, given required state, outcome, or signal evidence is absent, when observability is verified, then a detectable failure identifies the missing evidence.
- Edge oracle: For {operation_subject}, given the operation changes from running to completed or failed, when observations are compared, then the terminal outcome and relevant signals remain attributable to the same operation.
- Failure semantics: Do not report operational verification success with missing bound evidence.

## ACP-INTEGRATION_CONTRACT v1.0.0

Verify an explicit producer/provider, consumer/client, accepted input/output, ownership boundary, and rejection outcome.

- Supported types: `INTEGRATION_REQUIREMENT`
- Required bindings: `provider, consumer, contract_input, contract_outcome`
- Observable contract: submitted contract, provider/consumer ownership, accept/reject result, external outcome, and reconciliation evidence where bound
- Positive oracle: Given {consumer} submits {contract_input} to {provider}, when the contract is evaluated, then {contract_outcome} is observable at the bound integration boundary.
- Negative oracle: For {provider}, given malformed, unsupported, or unauthorized contract input, when the provider evaluates it, then it is rejected with no false successful external outcome.
- Edge oracle: For {provider}, given external outcome is incomplete or disputed, when boundary ownership is inspected, then the responsible party and reconciliation evidence are explicit.
- Failure semantics: Do not claim integration success without a bound external interaction outcome.

## ACP-SCOPE_EXCLUSION v1.0.0

Verify that an explicitly future, deferred, or excluded capability is not represented as active behavior in the current baseline.

- Supported types: `SCOPE_CONSTRAINT, BUSINESS_DECISION, DESIGN_PRINCIPLE`
- Required bindings: `excluded_capability, scope_status, current_baseline`
- Observable contract: baseline capability inventory, exposed UI/API/action surface, and scope marker
- Positive oracle: Given {current_baseline}, when capability inventory is inspected, then {excluded_capability} is marked {scope_status} and is not represented as active delivery.
- Negative oracle: For {excluded_capability}, given an exposed action or contract claiming the excluded capability is active, when scope conformance is checked, then the claim is rejected as outside the bound baseline.
- Edge oracle: For {excluded_capability}, given architectural readiness without implementation, when conformance is evaluated, then readiness evidence is distinguishable from active product availability.
- Failure semantics: Prevent future or deferred capability from being counted as active.

## Split decisions

- `POLICY_SCOPE_ENFORCEMENT / MFA_ENFORCEMENT` — `SPLIT`: MFA has challenge, bypass, and recovery semantics not shared by general scoped policy enforcement.
- `STATE_TRANSITION / STATE_MACHINE_INVARIANT` — `SPLIT`: A single transition oracle cannot prove an invariant across a complete machine.
- `EVENT_DELIVERY / RETRY_AND_TERMINAL_FAILURE` — `SPLIT`: Delivery outcome and retry exhaustion are independent obligations and retry must not be inferred for every event.
- `UX_STATE_AND_ACTION / UX_ACCESSIBILITY / UX_PERFORMANCE_BUDGET` — `SPLIT`: Rendered state, accessibility outcome, and measured performance have incompatible evidence and failure semantics.
