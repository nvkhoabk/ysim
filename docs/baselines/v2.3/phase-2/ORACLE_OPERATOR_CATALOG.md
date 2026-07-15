# Oracle Operator Catalog C2

- Candidate: `V23-P2C-SEMANTIC-ORACLE-MODEL-C2`
- Version: `1.0.0-candidate.2`
- Operators: `40`
- Mutation result source: `EXECUTION_DERIVED_ONLY`
- Runtime claim: `SLICE_RUNTIME_ADAPTER_REQUIRED`

## ACCESSIBILITY_CONFORMS

- Mode: `HYBRID`
- Required bindings: `experience, accessibility_standard, required_outcomes`
- Evidence: `experience, accessibility_results, assistive_technology, violations`
- Intent: A rendered interaction satisfies named accessibility criteria.

## ACTOR_AUTHORIZED

- Mode: `EXECUTABLE`
- Required bindings: `actor, action, resource, effective_policy`
- Evidence: `policy_input, policy_outcome, policy_version, audit_record`
- Intent: An actor is explicitly authorized for an action and resource scope.

## ACTOR_DENIED

- Mode: `EXECUTABLE`
- Required bindings: `actor, action, resource, effective_policy`
- Evidence: `policy_input, policy_outcome, reason, audit_record`
- Intent: A prohibited actor/action/resource combination is denied.

## APPROVAL_REQUIRED

- Mode: `EXECUTABLE`
- Required bindings: `action, approval_policy, approval_reference`
- Evidence: `approval_id, approval_status, approver, approved_at, action_at`
- Intent: A governed action proceeds only with a valid required approval.

## AUDIT_IMMUTABLE

- Mode: `HYBRID`
- Required bindings: `audit_record, required_fields, immutability_boundary`
- Evidence: `audit_record, required_fields, integrity_proof, change_attempt`
- Intent: An audit record contains required fields and cannot be altered after creation.

## CAPABILITY_AVAILABLE

- Mode: `HYBRID`
- Required bindings: `subject, capability, scope`
- Evidence: `capability_inventory, invocation_or_conformance_result`
- Intent: A named capability is independently usable in an applicable scope.

## CAPABILITY_NOT_PLACEHOLDER

- Mode: `HYBRID`
- Required bindings: `subject, capability, scope`
- Evidence: `capability_status, observable_use_result`
- Intent: A required capability is more than a label or extension placeholder.

## COMPOSITE_COVERED_BY_CHILDREN

- Mode: `STATIC`
- Required bindings: `parent_id, child_ids, coverage_mode`
- Evidence: `parent_id, child_ids, coverage_mode, unit_flags`
- Intent: A composite parent is covered by all atomic children and is not a direct unit.

## CONFIGURATION_PRECEDENCE

- Mode: `EXECUTABLE`
- Required bindings: `configuration_key, source_values, precedence_order`
- Evidence: `source_values, precedence_order, selected_source, effective_value`
- Intent: Configuration sources resolve according to an explicit precedence order.

## CONFIGURATION_RESOLVES

- Mode: `EXECUTABLE`
- Required bindings: `configuration_key, configuration_sources, expected_value`
- Evidence: `source_values, selected_source, effective_value, configuration_version`
- Intent: Configuration resolves deterministically from governed sources.

## DATA_RETENTION_WINDOW

- Mode: `HYBRID`
- Required bindings: `data_class, retention_window, terminal_action`
- Evidence: `data_class, created_at, retention_deadline, terminal_action_result`
- Intent: Data remains available for its retention window and follows its terminal retention action.

## DELIVERY_TERMINAL_STATE

- Mode: `EXECUTABLE`
- Required bindings: `delivery_id, allowed_terminal_states, observed_state`
- Evidence: `delivery_id, observed_state, outcome, failure_reason`
- Intent: A delivery/operation reaches an allowed terminal state with evidence.

## ENUM_VALUE_ALLOWED

- Mode: `EXECUTABLE`
- Required bindings: `field, actual_value, allowed_values`
- Evidence: `field, actual_value, allowed_values, validation_result`
- Intent: A field value belongs to an explicitly allowed enumeration.

## EVENT_EMITTED

- Mode: `EXECUTABLE`
- Required bindings: `event_id, trigger, correlation_id`
- Evidence: `event_id, emitted_at, correlation_id, event_metadata`
- Intent: A required event is emitted with identity and correlation evidence.

## EVENT_NOT_EMITTED

- Mode: `EXECUTABLE`
- Required bindings: `event_id, condition, observation_window`
- Evidence: `event_query, observation_window, matching_events`
- Intent: An event is absent when emission is prohibited.

## EVENT_ORDER_NOT_REQUIRED

- Mode: `STATIC`
- Required bindings: `event_family, scope, ordering_policy`
- Evidence: `event_family, scope, ordering_policy, classification_result`
- Intent: A named event family is explicitly outside the processing-order obligation.

## EVENT_ORDER_PRESERVED

- Mode: `EXECUTABLE`
- Required bindings: `event_family, correlation_id, expected_sequence`
- Evidence: `observed_sequence, expected_sequence, correlation_id`
- Intent: Events in an ordered family preserve processing sequence.

## EVIDENCE_FIELD_PRESENT

- Mode: `STATIC`
- Required bindings: `evidence_object, required_fields`
- Evidence: `evidence_object, field_presence, missing_fields`
- Intent: Named evidence fields are present and non-empty where required.

## FAIL_CLOSED

- Mode: `EXECUTABLE`
- Required bindings: `failure_condition, protected_action, denied_state`
- Evidence: `failure, action_result, resulting_state, reason`
- Intent: A protected operation is blocked when required evidence/configuration is invalid.

## MFA_CHALLENGE_REQUIRED

- Mode: `EXECUTABLE`
- Required bindings: `principal, policy_scope, effective_policy, challenge_result`
- Evidence: `principal, policy_scope, policy_version, challenge_result, audit_record`
- Intent: Effective MFA policy requires and records a challenge for a bound principal and scope.

## OWNER_EQUALS

- Mode: `EXECUTABLE`
- Required bindings: `entity, actual_owner, expected_owner`
- Evidence: `entity_id, actual_owner, expected_owner`
- Intent: The observed owner/reference owner equals the required owner.

## PAYMENT_INITIATION_ALLOWED

- Mode: `EXECUTABLE`
- Required bindings: `order_id, commercial_gate_result, payment_state`
- Evidence: `order_id, gate_result, gate_at, payment_state, payment_at`
- Intent: Payment initiation is allowed only after its commercial gate passes.

## PAYMENT_INITIATION_BLOCKED

- Mode: `EXECUTABLE`
- Required bindings: `order_id, failed_checks, blocked_states`
- Evidence: `order_id, failed_checks, payment_state, payment_decision`
- Intent: Payment initiation and authorization remain blocked when a named gate check fails.

## PERFORMANCE_WITHIN_BUDGET

- Mode: `EXECUTABLE`
- Required bindings: `service, metric, observed_value, budget`
- Evidence: `service, metric, observed_value, budget, measurement_window`
- Intent: Observed performance remains within a named service-tier budget.

## POLICY_OUTCOME_EQUALS

- Mode: `EXECUTABLE`
- Required bindings: `policy, policy_inputs, expected_outcome`
- Evidence: `policy_inputs, policy_outcome, reason, policy_version`
- Intent: A versioned policy returns an exact bound outcome for bound inputs.

## PROCUREMENT_FEASIBLE

- Mode: `EXECUTABLE`
- Required bindings: `order_id, supplier_terms, capacity, coverage_policy`
- Evidence: `order_id, supplier_terms_result, capacity_result, coverage_result`
- Intent: Procurement can cover the entire required order under bound terms and policy.

## PROCUREMENT_NOT_FEASIBLE

- Mode: `EXECUTABLE`
- Required bindings: `order_id, failure_reason, dependent_action`
- Evidence: `order_id, failure_reason, procurement_result, dependent_action_result`
- Intent: A procurement failure is explicitly represented and blocks dependent actions.

## RECONCILIATION_BALANCED

- Mode: `EXECUTABLE`
- Required bindings: `correlation_id, debits, credits, currency`
- Evidence: `correlation_id, debits, credits, difference, currency`
- Intent: Financial/reconciliation components balance under one correlation and currency context.

## REFERENCE_TARGET_VALID

- Mode: `EXECUTABLE`
- Required bindings: `reference, registry, allowed_states`
- Evidence: `reference_value, resolved_target, target_state`
- Intent: A reference resolves to a canonical allowed target.

## RETRY_LIMIT_NOT_EXCEEDED

- Mode: `EXECUTABLE`
- Required bindings: `operation, retry_count, retry_limit`
- Evidence: `operation, attempts, terminal_state, failure_reason`
- Intent: Retry attempts never exceed a bound maximum before terminal failure.

## ROLE_LIST_CONSISTENT

- Mode: `EXECUTABLE`
- Required bindings: `role, role_rules, dependent_lists`
- Evidence: `role, dependent_lists, consistency_result`
- Intent: A role/enum selection is consistent with its dependent lists.

## SAFE_FALLBACK_USED

- Mode: `EXECUTABLE`
- Required bindings: `failure_condition, fallback, affected_experience`
- Evidence: `failure, selected_fallback, render_outcome, recovery_information`
- Intent: A non-critical presentation failure selects an approved safe fallback.

## SCOPE_ACTIVE

- Mode: `STATIC`
- Required bindings: `subject, baseline, scope`
- Evidence: `subject, baseline, scope_record`
- Intent: A requirement/capability is active in a named baseline and applicability scope.

## SCOPE_NOT_ACTIVE

- Mode: `STATIC`
- Required bindings: `subject, baseline, inactive_scope`
- Evidence: `scope_record, implementation_inventory`
- Intent: A future/deferred/out-of-scope item is not exposed as active implementation.

## SET_CONTAINS

- Mode: `EXECUTABLE`
- Required bindings: `actual_set, required_members`
- Evidence: `actual_members, missing_members`
- Intent: A set contains every named required member.

## SET_EQUALS

- Mode: `EXECUTABLE`
- Required bindings: `actual_set, expected_set`
- Evidence: `actual_members, expected_members, set_difference`
- Intent: Two bound sets contain exactly the same members.

## SET_EXCLUDES

- Mode: `EXECUTABLE`
- Required bindings: `actual_set, prohibited_members`
- Evidence: `actual_members, prohibited_matches`
- Intent: A set contains none of the prohibited members.

## STATE_TRANSITION_ALLOWED

- Mode: `EXECUTABLE`
- Required bindings: `state_machine, from_state, trigger, to_state`
- Evidence: `before_state, trigger, after_state, transition_result`
- Intent: A state machine permits a named transition and reaches the expected state.

## STATE_TRANSITION_REJECTED

- Mode: `EXECUTABLE`
- Required bindings: `state_machine, from_state, trigger, prohibited_state`
- Evidence: `before_state, trigger, after_state, rejection_reason`
- Intent: A state machine rejects a forbidden transition.

## TENANT_ISOLATED

- Mode: `EXECUTABLE`
- Required bindings: `actor_tenant, resource_tenant, permission_context`
- Evidence: `access_decision, actor_tenant, resource_tenant, audit_record`
- Intent: Tenant-scoped data and actions remain inside the permitted tenant boundary.
