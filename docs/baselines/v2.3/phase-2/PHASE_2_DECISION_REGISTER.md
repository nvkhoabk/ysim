---
schema_version: "1.0"
document_code: V23-PHASE-2-DECISION-REGISTER
title: Phase 2 BRD/UXF Remediation Decision Register
product_baseline: "2.3"
document_revision: "0.1"
lifecycle_status: PREFLIGHT
language: en
authority: PHASE_2_PREFLIGHT
supersedes: null
requirement_block_schema: null
---

# Phase 2 BRD/UXF Remediation Decision Register

## 1. Status and gate

- Artifact status: `PREFLIGHT`.
- Open semantic decisions: `0`.
- Decisions selected pending pack approval: `10`.
- Selected option for every decision: `1`.
- Pack approval: `PENDING`.
- Next preflight gate: `HUMAN_DECISION_PACK_APPROVAL`.
- Accepted registry commit:
  `8c2e41f89443048a5b8568b308c32129634d7241`.
- Source document commit:
  `7f16d4c4b8ab514bd45de184f65ace221b03f4db`.
- Decision authority: human approval is required.

All ten selections are recorded in full in the Human Decision Pack. They are
not `APPROVED` or `FROZEN` until that Markdown pack is signed directly. A Phase
2 final candidate remains prohibited while pack approval is pending.

## P2-DEC-001 — Federation contract boundary

- Source: `docs/BRD/BRD-WS-16.md:L1025-L1028`.
- Affected Requirement IDs/keys: `BD-16-026`.
- Exact ambiguity: “Identity Platform hỗ trợ Federation” does not define the
  actors/use cases, trust and tenant boundaries, supported protocol/profile,
  claims, linking conflicts, lifecycle, assurance, revocation, failure, or
  acceptance boundary.
- Available options:
  1. Approve a minimum v2.3 federation profile and its observable contract.
  2. Narrow the requirement to an explicitly approved protocol-neutral
     capability boundary and defer concrete profiles with a scope decision.
  3. Move Federation out of v2.3 through an approved scope change.
- Recommended option: human owners define and approve the minimum v2.3 actor,
  trust, protocol/profile, mapping, lifecycle, security, and failure contract;
  this preflight does not select it.
- Downstream impact: BRD statement, security acceptance, identity architecture,
  UX authentication journeys, integration tests, and release scope.
- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

## P2-DEC-002 — Mandatory Security Platform event contract

- Source: `docs/BRD/BRD-WS-16.md:L1031-L1034`.
- Affected Requirement IDs/keys: `BD-16-027`.
- Exact ambiguity: “Security Platform Publish Business Event” lacks mandatory
  taxonomy, triggers, producer ownership, schema/version/classification,
  Organization context, sensitive-data rules, delivery/retry/DLQ behavior,
  ordering/idempotency, consumer authorization, retention, and observability.
- Available options:
  1. Approve the minimum mandatory v2.3 security-event catalog and contract.
  2. Approve a narrower event-publication boundary with an authoritative
     referenced catalog.
  3. Approve a scope change for event families not required in v2.3.
- Recommended option: approve an authoritative minimum event catalog and
  observable contract before acceptance is authored; do not design transport
  topology in the BRD.
- Downstream impact: Security BRD, Event Registry, privacy classification,
  integration architecture, audit evidence, retry/replay, and acceptance.
- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

## P2-DEC-003 — Operation Retry versus Connector Retry

- Source: `docs/BRD/BRD-WS-17.md:L1079-L1082`.
- Affected Requirement IDs/keys: `BD-17-011`.
- Exact ambiguity: “independent” does not define layer ownership, counters and
  state, timeout/backoff/jitter/budget, idempotency, escalation, nested retry
  amplification, exhaustion, DLQ/manual recovery, correlation, or audit.
- Available options:
  1. Approve a two-layer retry responsibility and escalation contract.
  2. Assign retry ownership to one layer and prohibit nested retries except
     named cases.
  3. Approve interaction-specific ownership in a referenced policy matrix.
- Recommended option: human owners approve responsibility, escalation, budget,
  and exhaustion invariants; implementation algorithms remain outside BRD.
- Downstream impact: Operations BRD, connector contracts, failure semantics,
  idempotency, observability, recovery evidence, and acceptance.
- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

## P2-DEC-004 — Operations Platform event contract

- Source: `docs/BRD/BRD-WS-17.md:L1189-L1192`.
- Affected Requirement IDs/keys: `BD-17-026`.
- Exact ambiguity: the required operation lifecycle/retry/maintenance/runbook/
  recovery event taxonomy, triggers, identifiers, Organization and actor
  context, payload classification, guarantees, replay, authorization,
  retention, and observability are unspecified.
- Available options:
  1. Approve a mandatory v2.3 Operations event catalog and contract.
  2. Approve a minimal lifecycle event set with a referenced extensible catalog.
  3. Approve a scope change for non-mandatory event families.
- Recommended option: approve the minimum lifecycle event set and observable
  publication contract without selecting event architecture in this phase.
- Downstream impact: Operations BRD, Event Registry, runbooks, monitoring,
  consumers, replay/recovery, and acceptance.
- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

## P2-DEC-005 — Capability event-role classification and metadata

- Source: `docs/BRD/BRD-CAP-INDEX.md:L325-L328`.
- Affected Requirement IDs/keys: `CAP-P07`.
- Exact ambiguity: the approved semantic clarification permits `PUBLISHER`,
  `SUBSCRIBER`, `BOTH`, or `NONE`, but the source classification and mandatory
  role/reference/ownership/version metadata remain undecided.
- Available options:
  1. Keep `BUSINESS_REQUIREMENT` and define the metadata contract.
  2. Reclassify as `DESIGN_PRINCIPLE` with approved provenance and define the
     same validation contract.
  3. Split the principle from separately identified metadata constraints.
- Recommended option: approve classification and atomicity first, then add
  canonical event references and dangling-reference validation.
- Downstream impact: Capability Registry, Event Registry, requirement type
  totals, block structure, acceptance ownership, and projection validation.
- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

## P2-DEC-006 — Gateway, Connector, and Adapter applicability

- Source: `docs/BRD/BRD-WS-15.md:L1198-L1201`.
- Affected Requirement IDs/keys: `EP-15-002`.
- Exact ambiguity: “all Integration” does not state whether inbound, outbound,
  synchronous, asynchronous, batch, event, and internal domain interactions
  require all three layers or an interaction-specific subset, nor the approved
  exception/bypass boundary.
- Available options:
  1. Require all three layers for every named interaction type.
  2. Approve a matrix mapping interaction types to mandatory layers.
  3. Define the requirement as an external-integration constraint and govern
     internal communication separately.
- Recommended option: human owners approve an applicability and exception
  matrix; Phase 2 must not infer topology from the current slogan.
- Downstream impact: Integration BRD, architecture, enforcement, observability,
  internal communication, and acceptance.
- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

## P2-DEC-007 — UXF-505 classification after semantic clarification

- Source: `docs/UXF/UXF-05.md:L667-L670`.
- Affected Requirement IDs/keys: `UXF-505`.
- Exact ambiguity: technical decoupling semantics are approved, but whether
  the record remains `UX_REQUIREMENT` or becomes `DESIGN_PRINCIPLE` has not
  been approved.
- Available options:
  1. Keep `UX_REQUIREMENT` and express acceptance only at the storefront
     request/disclosure boundary.
  2. Reclassify as `DESIGN_PRINCIPLE` while retaining the stable ID and approved
     semantics.
  3. Split presentation disclosure from architectural decoupling if human
     review determines they are distinct atomic requirements.
- Recommended option: approve classification/atomicity while preserving the
  existing ID and the Phase 1C semantic clarification.
- Downstream impact: UXF block classification, acceptance abstraction,
  allocation architecture traceability, and criticality review.
- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

## P2-DEC-008 — Identity–User–Customer cardinality and lifecycle

- Source: `docs/BRD/BRD-WS-03.md:L551-L554`.
- Affected Requirement IDs/keys: `BD-03-006`.
- Exact ambiguity: approved decisions distinguish Identity, Organization User,
  and Customer relationship, but complete cardinality, link/unlink lifecycle,
  provisioning, merge/conflict rules, and authorization/data-isolation effects
  are not fully specified.
- Available options:
  1. Approve explicit cardinality and lifecycle invariants in BRD/domain terms.
  2. Approve minimal business invariants in BRD and bind detailed lifecycle to
     an authoritative domain specification.
  3. Defer unsupported link/merge operations through explicit scope constraints.
- Recommended option: approve minimum business cardinality, ownership, and
  lifecycle invariants, referencing a later domain model without inventing it
  in acceptance.
- Downstream impact: Identity and Customer BRDs, portal provisioning, tenant
  isolation, authorization, data migration, and acceptance.
- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

## P2-DEC-009 — Quantitative UX performance budgets

- Source: `docs/UXF/UXF-00.md`, `UXF-01.md`, `UXF-02.md`, `UXF-03.md`,
  `UXF-04.md`, and `UXF-05.md`; full-source scan found no documented acceptance
  or channel budgets for LCP, INP, CLS, JavaScript, route payload, API latency,
  device/network profile, environment, or percentile.
- Affected Requirement IDs/keys: `TMP-UXF-01-008`, `TMP-UXF-02-005`, `UXF-210`,
  plus each active critical journey that P2D-06 requires to carry applicable
  performance evidence.
- Exact ambiguity: UXD-12 requires quantitative channel budgets, but the
  numbers and measurement profiles are not approved in current sources.
- Available options:
  1. Approve a channel-specific budget matrix directly in UXF.
  2. Approve a normative performance specification and reference it from each
     impacted UXF block.
  3. Approve documented channel exceptions with rationale where a dimension
     does not apply.
- Recommended option: approve one authoritative quantitative matrix with
  channel/profile/percentile/release-gate bindings; do not invent numbers in
  Phase 2 remediation.
- Downstream impact: UXF acceptance, release gates, browser/device matrix,
  evidence capture, monitoring, and candidate readiness.
- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.

## P2-DEC-010 — Quantitative service-level, timeout, and freshness budgets

- Source: `docs/BRD/BRD-WS-08.md:L564-L567`,
  `docs/BRD/BRD-WS-13.md:L380`, `L886-L894`,
  `docs/BRD/BRD-WS-15.md:L1129-L1142`, and
  `docs/BRD/BRD-WS-17.md:L1003-L1014,L1227-L1230`.
- Affected Requirement IDs/keys: `BD-08-006`, `TMP-BRD-WS-13-006`,
  `BD-13-011`, `BD-15-026`, `BD-17-004`, `BD-17-032`.
- Exact ambiguity: current wording names timeout, real-time/near-real-time,
  health threshold, SLO, and SLA concepts without approved quantitative values,
  service tiers, percentiles, measurement windows, or authoritative policy
  references needed for observable acceptance.
- Available options:
  1. Approve quantitative values in the owning BRDs.
  2. Approve normative policy/reliability/reporting matrices and reference them
     from the owning Requirement Blocks.
  3. Approve explicit deferred scope for service tiers not required in v2.3.
- Recommended option: approve authoritative tiered matrices consistent with
  BDD-19 and BDD-22; do not manufacture numeric thresholds in remediation.
- Downstream impact: BRD acceptance, payment reservation behavior, reporting
  freshness, connector policy, operations monitoring, alerting, and release
  evidence.
- Selected option: `1`.
- Status: `DECIDED_PENDING_PACK_APPROVAL`.
