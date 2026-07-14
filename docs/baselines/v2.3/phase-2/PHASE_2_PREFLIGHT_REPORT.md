---
schema_version: "1.0"
document_code: V23-PHASE-2-PREFLIGHT-REPORT
title: Phase 2 BRD/UXF Big-Bang Remediation Preflight Report
product_baseline: "2.3"
document_revision: "0.1"
lifecycle_status: PREFLIGHT
language: en
authority: PHASE_2_PREFLIGHT
supersedes: null
requirement_block_schema: null
---

# Phase 2 BRD/UXF Big-Bang Remediation Preflight Report

## 1. Status

- Artifact status: `PREFLIGHT`.
- Human approval status: `PENDING`.
- Source documents modified in Phase 2A: `0`.
- Real source acceptance criteria created in Phase 2A: `0`.
- Human Decision Pack status: `PENDING_MARKDOWN_APPROVAL`.
- Final candidate status: `BLOCKED_BY_PENDING_DECISION_PACK_AND_OPEN_CRITICALITY_EXCEPTIONS`.

This report is an audit and projection. It is not a remediated BRD/UXF
baseline, a document freeze, architecture approval, implementation
authorization, or acceptance baseline.

## 2. Immutable baseline binding

- Accepted registry commit:
  `8c2e41f89443048a5b8568b308c32129634d7241`.
- Accepted registry tag:
  `baseline/v2.3/requirements-registry/fc2-accepted`.
- Source document commit:
  `7f16d4c4b8ab514bd45de184f65ace221b03f4db`.
- Candidate: `V23-REQ-REGISTRY-FC2`.
- Source hash basis: `GIT_BLOB_CONTENT_AT_SOURCE_COMMIT`.
- Line-ending semantics: `GIT_CANONICAL_TEXT`.
- Source aggregate:
  `34685bed33422505763d31ef8f86837a1139fd5aaf2946a9adcbfa9dd1cd9a35`.
- Registry aggregate:
  `832cc96192c72b89472964e030893ac4c01bcc0d20eb21f7e935b7a7c6288658`.

## 3. Authoritative-input audit

The preflight loaded and parsed the complete canonical Git blob for all 31
source documents, rather than a summary or working-tree byte representation.
It also loaded the full framework decisions, document baseline, review
register, FC2 manifest, approval envelope, Markdown reports, QA,
reconciliation, all JSON registries, and both validators.

Source scan coverage:

| Measure | Result |
|---|---:|
| BRD documents | 24 |
| UXF documents | 7 |
| Canonical source blobs read | 31/31 |
| Canonical source SHA-256 matches | 31/31 |
| Canonical source bytes read | 453,359 |
| Canonical source lines scanned | 25,690 |
| Placeholder hits (`TBD`, `TODO`, undefined markers) | 0 |
| Numeric/service-budget term lines | 136 |
| Future/version-scope term lines | 111 |
| Identity/authentication term lines | 244 |
| Solution-design term lines | 295 |
| Documented-acceptance term lines | 0 |

Term counts are review signals, not requirements or blocker counts. Exact
per-document counts and hashes are recorded in
`phase-2-preflight-summary.json`.

## 4. Accepted counts and stable-ID projection

| Measure | Accepted FC2 | Projected after ID application |
|---|---:|---:|
| Active registry entries | 1,185 | 1,187 |
| Canonical atomic units | 1,174 | 1,176 |
| Registry entries with current IDs | 576 | 1,187 |
| Existing-ID canonical atomic units | 565 | 565 |
| Active temporary keys | 609 | 0 |
| Stable IDs mapped from temporary keys | 0 | 609 |
| Newly allocated stable IDs | 0 | 2 |
| Alias records | 9 | 9 |
| Composite parents | 2 | 2 |
| Retired temporary-key tombstones | 157 | 157 |
| Unresolved reconciliation records | 0 | 0 |
| Active registry entries without ID | 609 | 0 |

The 609 mapping records remain sorted by temporary key, preserve their numeric
suffixes, and have no collision with existing IDs, aliases, composite parents,
retired-key reservations, or other planned IDs. The selected P2-DEC-005 and
P2-DEC-007 splits reserve `BRD-CAP-INDEX-R029` and `UXF-05-R054` in a separate
allocation ledger. No retired key receives a mapping; the two allocations are
not fake temporary mappings. Two independent generator runs produced
byte-identical JSON.

## 5. Scope and acceptance projection

Canonical atomic scope distribution:

| Scope | Count | Phase 2 acceptance applicability |
|---|---:|---|
| `V2.3_ACTIVE` | 1,070 | `REQUIRED_FOR_V2.3` |
| `FUTURE` | 74 | `NOT_APPLICABLE_FOR_V2.3` |
| `DEFERRED` | 15 | `NOT_APPLICABLE_FOR_V2.3` |
| `OUT_OF_SCOPE` | 17 | `NOT_APPLICABLE_FOR_V2.3` |
| Total | 1,176 | — |

- Active acceptance denominator: `1,070`.
- Inactive `NOT_APPLICABLE_FOR_V2.3` denominator: `106`.
- Phase 1C `INFERRED_ONLY` acceptance units: `1,174`.
- Projected active acceptance gap before remediation: `1,070`.
- Projected active acceptance gap after complete remediation: `0`.
- Inactive units excluded from the active acceptance gap: `106`.

The after-remediation value is a target projection, not a claim that any real
acceptance criterion exists today.

## 6. Lifecycle distribution

| Lifecycle | Canonical atomic | All registry entries |
|---|---:|---:|
| `DRAFT` | 165 | 165 |
| `FROZEN` | 1,009 | 1,020 |

The historical source lifecycle does not authorize partial freezing. P2D-10
requires all 31 documents to transition together through the v2.3 lifecycle.

## 7. Requirement-type distribution

| Requirement type | Canonical atomic | All registry entries |
|---|---:|---:|
| `ACCESSIBILITY_REQUIREMENT` | 8 | 8 |
| `BUSINESS_DECISION` | 177 | 177 |
| `BUSINESS_REQUIREMENT` | 363 | 367 |
| `BUSINESS_RULE` | 14 | 14 |
| `DATA_REQUIREMENT` | 147 | 149 |
| `DESIGN_PRINCIPLE` | 18 | 18 |
| `INTEGRATION_REQUIREMENT` | 53 | 54 |
| `OPERATIONAL_REQUIREMENT` | 75 | 77 |
| `PERFORMANCE_REQUIREMENT` | 4 | 4 |
| `PRIVACY_REQUIREMENT` | 9 | 9 |
| `SCOPE_CONSTRAINT` | 116 | 116 |
| `SECURITY_REQUIREMENT` | 58 | 60 |
| `UX_REQUIREMENT` | 132 | 132 |

## 8. Proposed criticality preflight

P2D-05 rules were applied to the projected 1,070 active canonical atomic units:

| Proposed tier | Count |
|---|---:|
| `CRITICAL` | 313 |
| `HIGH` | 409 |
| `NORMAL` | 348 |
| Total | 1,070 |

There are 46 borderline/cross-tier assignments. Every one is listed as `OPEN`
in `PHASE_2_CRITICALITY_EXCEPTION_REGISTER.md`; none is automatically resolved.
The complete per-requirement proposed tier, matched rule, rationale, expected
verification mode, and evidence dimensions are in the machine-readable
preflight summary.

## 9. Documentation finding dispositions

All 15 FC2 documentation findings are carried forward. Seven have deterministic
corrections grounded in approved decisions or Phase 1C semantic clarification.
Eight are covered by selected option 1 decisions in the pending Human Decision
Pack. Those selections are not approved until the Markdown pack is signed.

### DOC-OVL-EXACT-004 — Partial Payment version wording

- Source/requirement: `docs/BRD/BRD-WS-08.md:L600-L603`, `BD-08-012`.
- Finding: source says “Version 2.0”; Partial Payment and Partial Refund are
  distinct, and supporting Partial Refund does not activate Partial Payment.
- Provenance: OVL-EXACT-004 reconciliation; SD-02; `BD-08-012` remains
  `OUT_OF_SCOPE`.
- Planned disposition: deterministic `CLARIFICATION` to v2.3 baseline wording,
  preserving the capability distinction and inactive scope rationale.

### DOC-OVL-EXACT-006 — Auto Payout version wording

- Source/requirement: `docs/BRD/BRD-WS-10.md:L735-L738`, `BD-10-016`.
- Finding: source says “Version 2.0”.
- Provenance: OVL-EXACT-006 reconciliation and SD-02.
- Planned disposition: deterministic `CLARIFICATION` to v2.3 wording while Auto
  Payout remains `OUT_OF_SCOPE`.

### DOC-OVL-EXACT-008 — Personal Inbox fallback semantics

- Source/requirement: `docs/BRD/BRD-WS-12.md:L660-L663`, `BD-12-005`.
- Finding: “cuối cùng” does not distinguish external delivery, durable inbox
  persistence, read state, retry, or recovery/DLQ.
- Provenance: approved OVL-EXACT-008 semantic clarification and acceptance
  intent.
- Planned disposition: deterministic `CLARIFICATION`; preserve
  `INFERRED_ONLY` until real source acceptance is written during remediation.

### DOC-OVL-EXACT-009 — Federation definition

- Source/requirement: `docs/BRD/BRD-WS-16.md:L1025-L1028`, `BD-16-026`.
- Finding: missing actors/use cases, trust/tenant boundaries, protocol/profile,
  claim mapping, linking conflicts, lifecycle, assurance/MFA/risk, audit,
  revocation, failure, and acceptance contract.
- Disposition: P2-DEC-001 option 1 selected in the pending pack; no source
  change occurs before pack approval.

### DOC-OVL-EXACT-010 — Security Platform events

- Source/requirement: `docs/BRD/BRD-WS-16.md:L1031-L1034`, `BD-16-027`.
- Finding: missing taxonomy, triggers/ownership, schema/version/classification,
  tenant context, sensitive-data rules, guarantees, retry/DLQ, ordering,
  deduplication/idempotency, authorization, audit, retention, observability,
  and acceptance.
- Disposition: P2-DEC-002 option 1 selected in the pending pack; transport
  architecture remains outside this decision.

### DOC-OVL-EXACT-011 — Independent retry layers

- Source/requirement: `docs/BRD/BRD-WS-17.md:L1079-L1082`, `BD-17-011`.
- Finding: missing ownership/scope, independent counters/state,
  timeout/backoff/jitter/budget, idempotency, escalation, amplification control,
  exhaustion/DLQ/manual recovery, correlation, audit, observability, and
  acceptance.
- Disposition: P2-DEC-003 option 1 selected in the pending pack; numeric budgets
  are governed by selected P2-DEC-010.

### DOC-OVL-EXACT-012 — Operations Platform events

- Source/requirement: `docs/BRD/BRD-WS-17.md:L1189-L1192`, `BD-17-026`.
- Finding: missing lifecycle/retry/maintenance/runbook/recovery taxonomy,
  triggers/ownership, operation/correlation/causation IDs, Organization/actor
  context, schema/classification, delivery/ordering/idempotency, retry/DLQ/
  replay, authorization, audit, retention, observability, and acceptance.
- Disposition: P2-DEC-004 option 1 selected in the pending pack; transport
  architecture remains architecture-owned.

### DOC-OVL-EXACT-013 — Capability event-role principle

- Source/requirement: `docs/BRD/BRD-CAP-INDEX.md:L325-L328`, `CAP-P07`.
- Finding: classification and event-role metadata/reference/ownership/versioning
  contract remain undecided; dangling references need validation.
- Provenance: OVL-EXACT-013 semantic clarification defines optional roles
  `PUBLISHER`, `SUBSCRIBER`, `BOTH`, and `NONE`.
- Disposition: P2-DEC-005 option 1 selects reclassification plus one split;
  `BRD-CAP-INDEX-R029` is reserved pending pack approval.

### DOC-OVL-EXACT-015 — Integration layer applicability

- Source/requirement: `docs/BRD/BRD-WS-15.md:L1198-L1201`, `EP-15-002`.
- Finding: inbound/outbound, sync/async, batch/event, internal communication,
  mandatory-layer combinations, exception/bypass, enforcement, observability,
  and acceptance are unclear.
- Disposition: P2-DEC-006 option 1 selects the explicit external-integration
  matrix; it remains pending pack approval.

### DOC-OVL-EXACT-029 — Storefront supplier decoupling

- Source/requirement: `docs/UXF/UXF-05.md:L667-L670`, `UXF-505`.
- Finding: source slogan must become approved technical-decoupling semantics;
  classification as UX requirement versus design principle is undecided.
- Provenance: approved OVL-EXACT-029 semantic clarification preserves read-only
  provider/brand disclosure while prohibiting routing control and internal
  supplier metadata exposure.
- Disposition: P2-DEC-007 option 1 selects reclassification plus one disclosure
  split; `UXF-05-R054` is reserved pending pack approval.

### DOC-OVL-PROB-001 — Identity–User–Customer relationship

- Source/requirement: `docs/BRD/BRD-WS-03.md:L551-L554`, `BD-03-006`.
- Finding: cardinality, Organization ownership, link/unlink lifecycle,
  provisioning, merge/conflict, authorization, isolation, and acceptance need
  specification.
- Provenance: OVL-PROB-001 clarification, UXD-17, UXD-19.
- Disposition: approved distinctions remain deterministic; P2-DEC-008 option 1
  selects the complete cardinality/lifecycle contract pending pack approval.

### DOC-OVL-PROB-002 — Promotion Funding Owner

- Source/requirement: `docs/BRD/BRD-WS-06.md:L532-L535`, `BD-06-011`.
- Finding: connect Promotion, Funding Owner, Organization ownership, budget
  reserve/consume/release, financial attribution, and acceptance.
- Provenance: OVL-PROB-002 semantic clarification, BDD-11, BDD-14.
- Planned disposition: deterministic `CLARIFICATION` at business/financial
  contract boundary; do not design a financial storage model.

### DOC-OVL-PROB-003 — Promotion Snapshot lifecycle

- Source/requirement: `docs/BRD/BRD-WS-06.md:L552-L555`, `BD-06-014`.
- Finding: source must say Final Promotion Snapshot and specify Evaluation,
  Reservation, and Final lifecycle with budget transitions, immutability,
  version, input, funding, currency, timestamp, and acceptance.
- Provenance: OVL-PROB-003 effective statement, BDD-11, BDD-12.
- Planned disposition: deterministic `CLARIFICATION`; do not reintroduce the
  false interpretation that pre-payment Evaluation/Reservation snapshots are
  prohibited.

### DOC-OVL-PROB-004 — Snapshot Security and Retention policies

- Source/requirement: `docs/BRD/BRD-SNAPSHOT-INDEX.md:L359-L362`, `SNP-P07`.
- Finding: joint policy resolution needs jurisdiction/data-class mapping,
  conflict behavior, legal hold, deletion/anonymization with immutability,
  audit evidence, and acceptance.
- Provenance: OVL-PROB-004 semantic clarification and BDD-18.
- Planned disposition: deterministic `CLARIFICATION` at policy outcome
  boundary; do not design a policy engine or storage mechanism.

### DOC-OVL-PROB-006 — Attachment scope and version labels

- Source/requirements:
  `docs/BRD/BRD-WS-11.md:L541-L550`, `TMP-BRD-WS-11-010`; and
  `docs/BRD/BRD-WS-12.md:L481-L490`, `TMP-BRD-WS-12-013`.
- Finding: normalize “Version 2.0” and “Version 2” to v2.3; Video exclusion is
  limited to Customer Support Ticket Attachment and Notification Attachment.
- Provenance: OVL-PROB-006 `DISTINCT_BY_APPLICABILITY`.
- Planned disposition: deterministic `CLARIFICATION`; do not generalize to a
  platform-wide Attachment policy or design a shared capability.

## 10. Additional full-source semantic-blocker scan

The complete 31-document scan applied the requested review families:

- Approved-decision conflicts: known v2.2 version/scope wording is handled by
  deterministic corrections where authority is explicit; no conflict is
  silently resolved.
- Acceptance that would add meaning: all eight finding-derived decisions have
  selected option 1, but source authoring waits for pack approval.
- Actor/owner/scope/state ambiguity: selected options now define Federation,
  event ownership, retry layers, integration applicability, and
  Identity–User–Customer lifecycle, pending pack approval.
- Undefined numeric thresholds and performance budgets: `P2-DEC-009` and
  `P2-DEC-010` were added from the full-source scan and now have selected
  quantitative matrices pending pack approval.
- Authentication/identity behavior: UXD-03, UXD-04, UXD-17, UXD-19, and BDD-17
  remain authoritative; selected P2-DEC-001 and P2-DEC-008 add the pending
  Federation and relationship contracts.
- Cross-document terminology: Final Promotion Snapshot, Personal Inbox delivery
  state, Funding Owner, and attachment scope have approved correction
  provenance; CAP-P07 and UXF-505 classification/splits are selected pending
  pack approval.
- Future/deferred wording: P2D-03 and FC2 scope classifications control; no
  inactive record is included in the active acceptance denominator.
- Solution design presented as business meaning: CAP-P07, EP-15-002, event
  publication, and retry wording now have selected business/contract
  boundaries, while transport topology remains architecture-owned.

Decision Register result: `0 OPEN`; all 10 items are
`DECIDED_PENDING_PACK_APPROVAL` with selected option 1. The next gate is
`HUMAN_DECISION_PACK_APPROVAL`.

## 11. Determinism and provenance

- JSON contains relative POSIX paths only.
- No runtime timestamp, absolute path, checkout line ending, host name, or
  machine-specific data participates in deterministic output.
- Source evidence is read from Git objects at the declared source commit.
- Mapping output is sorted by `temporary_key`.
- Two generator runs produced byte-identical decision pack, decision JSON,
  mapping, and summary outputs.
- Proposed source IDs preserve the original numeric suffix and document origin.
- Two next-never-used allocations are recorded separately from the 609 mappings.

## 12. Phase 2A stop condition

Stop for direct Markdown approval after staging this report, the contract, the
pending Human Decision Pack, the decided register, the still-open criticality
exception register, the validator, and deterministic JSON artifacts. Do not
edit BRD/UXF, author real source acceptance, approve exceptions, create a Phase
2 candidate, commit, push, or tag.
