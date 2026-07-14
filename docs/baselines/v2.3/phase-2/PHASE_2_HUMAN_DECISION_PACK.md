---
schema_version: "1.0"
document_code: V23-PHASE-2-HUMAN-DECISION-PACK
title: Phase 2 BRD/UXF Human Decision Pack
product_baseline: "2.3"
document_revision: "0.1"
lifecycle_status: PENDING_APPROVAL
language: en
authority: HUMAN_DECISION_PACK
supersedes: null
requirement_block_schema: null
---

# Phase 2 BRD/UXF Human Decision Pack

## 1. Status and binding

- candidate_id: `V23-P2A-DECISION-PACK-C1`
- status: `CANDIDATE`
- approval_status: `PENDING_MARKDOWN_APPROVAL`
- decision_count: `10`
- open_decision_count: `0`
- decided_pending_pack_approval_count: `10`
- next_gate: `HUMAN_DECISION_PACK_APPROVAL`
- source_registry_candidate_id: `V23-REQ-REGISTRY-FC2`
- source_git_commit: `8c2e41f89443048a5b8568b308c32129634d7241`
- hash_basis: `GIT_INDEX_BLOB_CONTENT`
- line_endings: `GIT_CANONICAL_TEXT`
- Decision selection status: `DECIDED_PENDING_PACK_APPROVAL`.
- Selected option for every decision: `1`.
- Open semantic decisions: `0`.
- Effective approval: `PENDING`.
- Accepted registry commit: `8c2e41f89443048a5b8568b308c32129634d7241`.
- Accepted registry tag: `baseline/v2.3/requirements-registry/fc2-accepted`.
- Source document commit: `7f16d4c4b8ab514bd45de184f65ace221b03f4db`.
- Source aggregate: `34685bed33422505763d31ef8f86837a1139fd5aaf2946a9adcbfa9dd1cd9a35`.
- Registry aggregate: `832cc96192c72b89472964e030893ac4c01bcc0d20eb21f7e935b7a7c6288658`.

The decisions below are fully selected but are not approved or frozen until
the Human Approval block is signed directly. No decision is applied to
BRD/UXF source in Phase 2A.

## P2-DEC-001 — Inbound workforce federation

- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

### Approved scope

- Protocols are OIDC Authorization Code with PKCE and SAML 2.0 Web Browser SSO.
- YSim acts as relying party/service provider.
- Federation applies to Organization, Agency, and limited Partner workforce portals.
- Platform Admin federation uses a separate YSim-operator trust.
- Customer Portal and Storefront authentication are outside enterprise federation.

### Identity and claims

- The immutable federation identity key is Organization + Issuer + Subject.
- Email is not an immutable identity key and may be consumed only when verified.
- Claims use an allowlist.
- JIT provisioning follows Organization policy and defaults to least privilege.
- JIT provisioning must not assign privileged roles.

### Assurance and policy

- Privileged roles must still meet MFA assurance; YSim performs step-up when IdP assurance is insufficient.
- Organization policy is LOCAL_ALLOWED, FEDERATION_OPTIONAL, or FEDERATION_REQUIRED.
- FEDERATION_REQUIRED retains a controlled, audited break-glass recovery account.

### Linking, validation, lifecycle, and audit

- Account linking requires an authenticated existing session or admin approval.
- A privileged account must never be auto-linked by email.
- Signature, issuer, audience, time, nonce/replay, and tenant binding are validated fail-closed.
- Disabling a trust or User blocks new login and revokes sessions according to policy.
- Audit covers login, failure, JIT, link/unlink, conflict, and trust changes.

### Out of v2.3

- Outbound IdP.
- SCIM.
- Cross-Organization federation linking.
- Automatic privileged-role assignment.

## P2-DEC-002 — Mandatory Security Platform events

- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

### Mandatory event types

- security.authentication.succeeded
- security.authentication.failed
- security.mfa.challenge.succeeded
- security.mfa.challenge.failed
- security.account.locked
- security.account.unlocked
- security.session.revoked
- security.identity.linked
- security.identity.unlinked
- security.access.denied
- security.privilege.changed
- security.policy.changed
- security.credential.lifecycle.changed
- security.federation.trust.changed
- security.risk.decision.made
- security.suspicious_activity.detected
- security.break_glass.started
- security.break_glass.ended

### Shared envelope

- event_id
- event_type
- event_version
- occurred_at
- producer
- organization_id/platform_scope
- actor
- subject
- correlation_id
- causation_id
- classification
- outcome
- reason_code
- typed payload

### Contract

- Event Registry owns canonical schema and producer declarations.
- No password, OTP, token, private key, raw assertion, or secret is allowed.
- PII is minimized and stable references are preferred.
- Delivery is at least once; consumers deduplicate by event_id.
- There is no global ordering; explicit per-subject ordering is used only where declared.
- Replay preserves original event identity and adds replay metadata.
- Schema changes within a major version are backward-compatible.
- Consumer authorization is constrained by Organization, event type, and classification.
- Retry, DLQ, alerting, retention, and publish observability are mandatory.
- A durable audit/event record exists before a security state-changing operation completes.
- Transport topology remains architecture-owned.

## P2-DEC-003 — Two-layer shared-budget retry ownership

- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

### Ownership and budget

- Connector Retry handles transient transport/provider failure inside one operation attempt.
- Operation Retry owns persisted business state, total SLA, fallback, compensation, and manual resolution.
- Each operation has one absolute deadline and one retry budget.
- The Connector receives only the remaining sub-budget.
- operation_attempt and connector_attempt counters are separate and share one correlation context.
- Provider SDK retries are disabled or counted in the shared budget.
- Side effects use a stable operation idempotency key.

### Error classes

- TRANSIENT
- RATE_LIMITED
- TERMINAL
- AMBIGUOUS_OUTCOME
- POLICY_BLOCKED
- CANCELLED/DEADLINE_EXCEEDED

### Failure behavior

- Ambiguous payment, procurement, allocation, or fulfillment outcomes are queried/reconciled before side effects are repeated.
- Blind retry is prohibited and no exactly-once claim is made.
- On exhaustion, control returns to Operation; policy then selects fallback, compensation, DLQ, or manual resolution.
- Partial fulfillment continues to manual resolution and does not trigger automatic refund.
- Numeric budgets reference P2-DEC-010.

## P2-DEC-004 — Mandatory Operations Platform events

- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

### Mandatory event types

- operations.operation.started
- operations.operation.completed
- operations.operation.failed
- operations.operation.cancelled
- operations.retry.scheduled
- operations.retry.exhausted
- operations.manual_resolution.required
- operations.manual_resolution.resolved
- operations.maintenance.scheduled
- operations.maintenance.started
- operations.maintenance.completed
- operations.maintenance.cancelled
- operations.runbook.started
- operations.runbook.completed
- operations.runbook.failed
- operations.recovery.started
- operations.recovery.completed
- operations.recovery.failed

### Ownership and payload

- The owning capability publishes operation lifecycle events.
- Operations Platform publishes retry/exhaustion, maintenance, runbook, and recovery events when it owns the transition.
- Attempt telemetry remains metric/trace unless an attempt is materially scheduled or exhausted.
- The shared envelope is defined by P2-DEC-002.
- Additional fields are operation_id/type, state_before/after, attempt counters, deadline, outcome, reason_code, and runbook/recovery/maintenance references.

### Transition contract

- The state transition is durable before publication.
- Delivery is at least once and consumers deduplicate by event_id.
- Sequence is monotonic per operation; there is no global ordering.
- A terminal state must not silently return to a non-terminal state.
- Manual resolution requires owner, reason, SLA reference, and audit.
- Transport topology remains architecture-owned.

## P2-DEC-005 — Capability event role and metadata split

- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

### Existing principle

- Reclassify CAP-P07 as DESIGN_PRINCIPLE.
- CAP-EP-006 remains an alias.
- A Capability may be PUBLISHER, SUBSCRIBER, BOTH, or NONE; not every Capability must be event-driven.

### New requirement allocation

- Add one V2.3_ACTIVE DATA_REQUIREMENT with reserved stable ID BRD-CAP-INDEX-R029.
- Required fields are event_role, published_event_ids, and subscribed_event_ids.
- NONE requires both lists to be empty.
- PUBLISHER, SUBSCRIBER, and BOTH require the corresponding lists to be non-empty.
- Event references resolve to canonical active/approved Event Registry IDs.
- Alias, retired, tombstone, and dangling references are prohibited.
- Event ownership and schema version remain authoritative in Event Registry.
- The new requirement has HIGH verification criticality.

## P2-DEC-006 — External integration applicability matrix

- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

### Normative matrix

- External client to YSim API: Gateway required; Connector normally not required; Adapter required when contracts differ.
- Provider to YSim webhook: Gateway and Connector required; Adapter required when mapping is required.
- YSim to provider API: Connector and Adapter required; API Gateway not required.
- YSim to partner/customer webhook: delivery Connector and Adapter required; API Gateway not required.
- External asynchronous event/message: bridge/Connector and Adapter required; API Gateway not required.
- Batch/SFTP/file: Connector and Adapter required.
- Portal/Storefront/Web SDK to public YSim API: Gateway required; Connector/Adapter not required when the API is canonical.
- Internal domain API/event is not governed by the external Connector/Adapter matrix.

### Additional invariants

- A Business Domain never connects directly to an external system.
- Gateway owns ingress policy, routing, limits, and observability and contains no business logic.
- Connector owns connectivity, authentication, protocol, retry, and provider health and contains no domain decisions.
- Adapter owns schema/semantic translation and contains no business logic.
- Provider-specific models must not leak into Business Domains.
- Direct browser/mobile-to-provider interaction is allowed only through an approved short-lived scoped token/session pattern; backend webhook/status remains authoritative.
- Production bypass is prohibited.
- An exception requires architecture/security review, expiry, and audit.

## P2-DEC-007 — Storefront supplier decoupling and disclosure split

- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

### Existing principle

- Reclassify UXF-505 as DESIGN_PRINCIPLE and preserve its stable ID.
- Storefront does not select, route, or directly integrate Supplier; Allocation alone owns supplier selection.

### New disclosure requirement

- Add one V2.3_ACTIVE UX_REQUIREMENT with reserved stable ID UXF-05-R054.
- Customer-facing provider/network/brand may be shown when required by Catalog, legal, or product definition, as read-only disclosure.
- Internal Supplier ID, procurement source, cost/margin, routing priority, supplier health, connector identity, and allocation details must never be exposed.
- Storefront API payloads must not contain those internal fields.
- Disclosure must not influence allocation.
- Missing mandatory disclosure data uses fail-closed business behavior.
- The new requirement has HIGH verification criticality.

## P2-DEC-008 — Identity, User, and Customer cardinality and lifecycle

- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

### Cardinality

- Identity is a global authentication principal with multiple verified methods.
- User is a workforce membership in exactly one Organization.
- Each User has exactly one Identity.
- There is at most one active User per Identity + Organization.
- Multiple roles belong to one User.
- Customer is a commercial relationship in exactly one selling Organization.
- Customer may temporarily exist without Identity.
- Customer links to at most one Identity.
- There is at most one active Customer per Identity + Organization.
- There is no YSim-wide Customer Portal aggregation.

### Lifecycle and access

- User and Customer lifecycles are independent.
- A User role does not grant Customer access and Customer status does not grant workforce access.
- Disabling/deleting one relationship does not delete the others.
- Federation JIT creates User only.
- Guest checkout always has email.
- Payment-success account provisioning is idempotent.
- An existing verified Identity is reused; otherwise a pending-verification Identity is created and a magic link/OTP is sent.
- Portal access begins only after identifier control is proven.
- Email text matching is not ownership proof.
- Linking requires verified control or an audited case-scoped admin action.
- A conflict blocks automatic linking and goes to manual resolution.
- Destructive Customer merge is outside v2.3.
- Manual resolution may select a canonical relationship and correct links but must not silently re-parent financial/order history.
- Portal session is bound to Organization/Customer context and fails closed.

## P2-DEC-009 — Authoritative UX performance budgets

- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

### Authority and percentile

- The shared authoritative matrix belongs in UXF-00.
- Field/RUM thresholds use p75.

### Channel budgets

- Storefront: LCP 2.5s, INP 200ms, CLS 0.10, initial JavaScript 200 KiB, initial route 800 KiB.
- Customer Portal: LCP 2.5s, INP 200ms, CLS 0.10, initial JavaScript 250 KiB, initial route 900 KiB.
- Platform Admin, Organization, and Agency Portal: LCP 2.5s, INP 200ms, CLS 0.10, initial JavaScript 300 KiB, initial route 1000 KiB.
- Builder: shell LCP 2.5s, ready-state INP 200ms, CLS 0.10, initial JavaScript 300 KiB with lazy editor modules, initial route 1000 KiB.
- Embedded SDK: host LCP regression 100ms, host INP regression 50ms, CLS contribution 0.05, SDK 75 KiB, widget 150 KiB, route transfer 300 KiB.
- Embedded WebView: LCP 2.5s, INP 200ms, CLS 0.10, initial JavaScript 200 KiB, initial route 800 KiB.
- Partner Portal is NOT_APPLICABLE_FOR_V2.3.

### Measurement and governance

- Transfer budgets are compressed production transfer.
- Initial route includes HTML, CSS, JavaScript, font, and critical media.
- Default LCP asset maximum is 250 KiB.
- Default critical-route third-party maximum is 100 KiB unless approved.
- Dynamic composition cannot bypass the budget.
- Missing measurement is failure.
- RUM uses rolling 28-day p75 segmented by channel, route, mobile, desktop, and WebView.
- Lab uses production build, cold cache, representative data, mobile 150ms latency, 1.6Mbps down, 750Kbps up, and calibrated mid-tier CPU.
- At least five lab runs are required and raw evidence is stored.
- Critical journeys are listed per channel.
- An exception records metric, current/requested value, reason, expiry, owner, and approval.
- API latency references P2-DEC-010.

### References

- https://web.dev/articles/vitals
- https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md

## P2-DEC-010 — Reliability, timeout, and freshness matrices

- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

### Service tiers

- T0_INTEGRITY_CRITICAL: availability 99.95%, RTO 15m, RPO 0 committed business records.
- T1_CUSTOMER_CRITICAL: availability 99.90%, RTO 1h, RPO 5m.
- T2_OPERATIONAL: availability 99.50%, RTO 4h, RPO 1h.
- T3_ANALYTICAL_BATCH: availability 99.00%, RTO 24h, RPO 24h.

### Latency p95/p99

- Interactive read: 500ms / 1.5s.
- Local transactional command: 750ms / 2s.
- Async command acceptance: 1s / 3s.
- Operational search/table: 2s / 5s.
- Large report/export submission: 1s / 3s.

### Timeout defaults

- Internal interactive hop: 2s.
- Public interactive request: 10s.
- External connect: 3s.
- External response: 15s, with synchronous hard cap 30s.
- Async acknowledgement: 1s p95.
- Inquiry/reconciliation: 15s.

### Reservation

- Online default is 15m.
- Payment policy is configurable from 5m to 30m.
- Total with extension is at most 30m unless an approved method policy says otherwise.
- Extension is allowed only while provider state is PENDING.
- Inventory and promotion reservations share the payment-attempt lifecycle.
- Offline confirmation after expiry requires price, promotion, inventory, procurement, and fulfillment revalidation.
- Previously approved retry, refund, and manual-resolution rules remain effective.

### Connector health

- Evaluation uses a rolling 5m window with a traffic floor of 20 attempts.
- DEGRADED: error at least 5%, p95 above SLO, or rate-limit at least 10%.
- UNHEALTHY: error at least 20%, three failed probes, circuit open, or credential/trust failure.
- RECOVERING: five successful probes and error below 5%, maintained for 10m.
- Business rejection is not connector technical failure.
- Routing does not select an UNHEALTHY connector.

### Freshness

- F0_LIVE: p95 at most 60s, hard stale 5m.
- F1_NEAR_REAL_TIME: p95 at most 5m, hard stale 15m.
- F2_HOURLY: at most 60m.
- F3_DAILY: at most 24h and before 06:00 local business time.
- Every report/export includes data_as_of, generated_at, timezone, freshness tier, completeness/provisional state, filters, and snapshot identity.

### Governance

- SLO uses a rolling 30-day window with burn-rate monitoring.
- Correctness/integrity is not an availability error-budget allowance.
- User-impacting planned maintenance counts unless explicitly contracted.
- Missing telemetry is failure.
- A configuration override requires owner, reason, expiry, approval, and audit.
- RTO/RPO is tested through drills.
- SLA is used only when contractual consequences exist.

### References

- https://sre.google/sre-book/service-level-objectives/
- https://sre.google/workbook/implementing-slos/

## Projected requirement splits and ID reservations

The two selected split decisions add two active canonical atomic units only
after pack approval. They are reservations, not temporary-key mappings and
not active source Requirement Blocks in this phase.

- `P2-DEC-005`: reserve `BRD-CAP-INDEX-R029` as a `V2.3_ACTIVE`
  `DATA_REQUIREMENT` with proposed `HIGH` criticality.
- `P2-DEC-007`: reserve `UXF-05-R054` as a `V2.3_ACTIVE`
  `UX_REQUIREMENT` with proposed `HIGH` criticality.
- Projected registry entries: `1185 → 1187`.
- Projected canonical atomic units: `1174 → 1176`.
- Projected active acceptance denominator: `1068 → 1070`.
- Inactive `NOT_APPLICABLE_FOR_V2.3` denominator: `106`.
- Projected IDs after mapping/allocation: `576 + 609 + 2 = 1187`.
- Projected active registry entries without ID: `0`.
- Proposed criticality: `CRITICAL 313`, `HIGH 409`, `NORMAL 348`.
- Criticality exceptions remain `46 OPEN`; review has not started.

## Human Approval

- Status: PENDING
- Authorized Approver: PENDING
- Decision: PENDING
- Date: PENDING
- Signature: PENDING
