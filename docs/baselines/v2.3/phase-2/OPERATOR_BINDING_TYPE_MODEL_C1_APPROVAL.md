# Phase 2C Operator Binding Type Model C1 Approval

- Candidate ID: `V23-P2C-OPERATOR-BINDING-TYPE-MODEL-C1`
- Candidate commit: `214bc3798a8ea586cec76a2584eb0eb11a2c5cf6`
- Candidate parent: `77d10a8c3ccb2e7795724fd1c82cdbea36c54e2e`
- Candidate tree: `277821e564a0862e6512bc40eb5b9e9395d2fe55`
- Decision: `APPROVED`
- Approval scope: `SEMANTIC_TYPE_CATALOG_40_OPERATOR_BINDING_SCHEMAS_ORIGIN_INDEPENDENCE_RESOLVER_CONTRACTS_TYPE_CHECKER_59_REMEDIATION_DISPOSITIONS_AND_SIX_SELECTED_SOURCE_CLARIFICATIONS`
- Authorized Approver: `Khoa, Nguyen`
- Signature: `Khoa, Nguyen`
- Approval date: `2026-07-16`
- Timezone: `Asia/Ho_Chi_Minh`
- Runtime mutation and runtime acceptance: `N/A`

## Signed candidate identity

- Staged Git Tree: `277821e564a0862e6512bc40eb5b9e9395d2fe55`
- Staged Git-content Aggregate: `ddd98927167aa5b5443e2ded2d6fd6c1947e397caa1862b8a844d2a375c84809`
- Generated Payload Aggregate: `bf63a716f99899f16403a52b9331ec2b0bcc4ba2ae8075e3da9c87caf3dafedf`

The immutable candidate remains `CANDIDATE` / `PENDING_HUMAN_APPROVAL`; its six `selected_option` values remain `null`. This detached approval is the sole effective selection layer.

## Approved model and remediation scope

- Semantic type catalog: 39 named types and three generic set/reference types.
- Operator-specific binding schemas: `40/40`.
- Binding-origin independence and resolver-contract requirements.
- Independent semantic type checker.
- Adversarial type tests: `400/400 PASS`; sentence-copy rejection: `40/40`.
- Remediation dispositions: `35 CORRECTABLE_WITH_APPROVED_TYPE_MODEL`, `12 OPERATOR_REMAP_REQUIRED`, `6 COMPOUND_AST_REQUIRED`, `6 SOURCE_CLARIFICATION_REQUIRED`; total `59`.

## Effective human selections

### BD-05-009 — `P2C-OBT-C1-BD-05-009-OPT-1`

A Price Change Set uses a governed lifecycle and requires approval before becoming effective.

- Approval is handled by the Shared Approval Engine.
- Draft and validation alone do not make a price change effective.
- The approval policy, approver resolution and effective time must be versioned.
- Emergency override, if permitted, requires explicit authorization and immutable audit evidence.
- Non-inferences: no fixed approver role or approval SLA is inferred by this decision.

### BRD-WS-02-R003 — `P2C-OBT-C1-BRD-WS-02-R003-OPT-1`

Use a versioned canonical eSIM Capability Registry with an independent operational capability resolver.

- Provider-specific schemas must be mapped into the canonical YSim capability taxonomy.
- Product Specification declares capabilities using canonical capability IDs.
- Operational capability is resolved independently from provider, inventory and runtime evidence.
- Acceptance compares the declared canonical set against the independently resolved set.
- Non-inferences: providers need not expose identical native schemas; no capability member or provider schema is invented.

### BRD-WS-07-R005 — `P2C-OBT-C1-BRD-WS-07-R005-OPT-1`

Use an authorized Identity Merge Proposal lifecycle with retained lineage and immutable audit evidence.

- Duplicate detection does not automatically merge identities.
- Merge requires authorization under a versioned policy.
- Original identity references, decision evidence and merge lineage must remain traceable.
- Merge must not silently transfer legal ownership, tenant scope or permissions.
- Reversal or correction behavior must be governed explicitly.
- Non-inferences: no automatic matching threshold or legal identity consolidation is inferred.

### EP-08-006 — `P2C-OBT-C1-EP-08-006-OPT-1`

Do not establish an invented universal retry limit. Retry limits come from versioned policy.

- A retry always creates a new PaymentAttempt identity.
- Retry policy may vary by provider, failure class, payment method and risk context.
- Absence of a universal limit does not mean unlimited retries.
- Terminal states and non-retryable failure reasons must fail closed.
- The value three is not canonical unless explicitly defined by an applicable policy.
- Non-inferences: no gateway retry topology is inferred.

### EP-17-002 — `P2C-OBT-C1-EP-17-002-OPT-1`

Use a versioned Platform Component Inventory together with component-class monitoring profiles.

- Every active Platform component must belong to the authoritative inventory.
- Every inventoried component must resolve to an applicable monitoring profile.
- Required signals, SLOs, alerting and evidence may vary by component class and criticality.
- CRITICAL components receive stricter profiles, but non-critical components are not excluded from monitoring.
- Coverage compares the canonical inventory against independently observed monitoring registration and signals.
- Non-inferences: no component or signal list is invented; external dependencies are not automatically Platform components.

### UXF-405 — `P2C-OBT-C1-UXF-405-OPT-1`

Configuration precedence is `Platform/Security → Jurisdiction/Market → Organization → Storefront`.

- Higher-level security, regulatory and platform invariants cannot be overridden by lower levels.
- Organization and Storefront may override only keys explicitly marked overridable.
- More-specific scope wins only within the permitted override contract.
- Every resolution exposes the selected source, source version and effective value.
- Storefront configuration cannot change business, security or regulatory invariants.
- Non-inferences: no configuration key or ungoverned override is invented.

## Explicit non-claims

This approval does not approve or authorize:

- `NOT_APPROVAL_OF_REJECTED_C3_R1_ASTS_OR_FIXTURES`
- `NOT_REGENERATED_CUSTOM_AST_APPROVAL`
- `NOT_REGENERATED_SEMANTIC_FIXTURE_APPROVAL`
- `NOT_RUNTIME_ADAPTER_OR_RUNTIME_EVIDENCE_APPROVAL`
- `NOT_BRD_UXF_EDIT_APPROVAL`
- `NOT_FINAL_PHASE_2C_DOCUMENT_BASELINE_APPROVAL`
- `NOT_FINAL_V2_3_BRD_UXF_FREEZE`
- `NOT_YADF_IMPLEMENTATION_AUTHORIZATION`
- `NOT_PRODUCTION_IMPLEMENTATION_AUTHORIZATION`
