---
document_code: V3-R1-G00-S04-README
document_name: Integration Boundary and Operator Visibility Source Baseline
project: YSim v3
document_set: V3-R1-G00-S04
version: 0.1.0
status: DRAFT
language: en
---
# V3-R1 G00 S04 — Integration Boundary and Operator Visibility Source Baseline

This checkpoint is a source-only reference for `V3-R1-INT-001`,
`V3-R1-INT-002`, `V3-R1-INT-003`, and `V3-R1-REL-009`. It establishes an
owned boundary, versioned canonical request/result records, explicit adapter
and interaction-mode policies, and a read-only redacted view of synthetic
failures.

The package is `PLANNED` and `SOURCE_VALIDATED_NON_OPERATIONAL` with
`CANDIDATE_MODEL=NONE`. It does not claim that a provider, transport,
production adapter, operations center, monitoring plane, payment,
fulfillment, notification, customer action, or deployed runtime exists.

## Controlled package

- `integration-boundary-operator-visibility-baseline.yaml` binds the four
  exact SOURCE_APPROVED requirements and the bounded behavior adopted for S04.
- `scope-decisions.yaml` records the authorized dispositions for REL-001,
  REL-003, REL-004, REL-005, and REL-006 without rewriting accepted S01 history.
- `source-provenance.yaml` binds the accepted S03 predecessor, the S03 Human
  Decision, immutable traceability/source inputs, and requirement digests.
- `package-spec.yaml` defines the exact 14-path recovery scope, external snapshot
  contract, validation gates, and non-operational boundary.
- `MANIFEST.sha256` checksums every non-self path in the frozen allowlist.

## Source behavior

Every request binds a canonical contract version, capability and scenario,
idempotency key, correlation identifier, interaction mode, adapter identity,
owner, timeout/retry policy references, and bounded redacted diagnostics.
Adapter identifiers must be allowlisted. Adapters are disabled unless an
explicit profile enables an exact scenario/mode/version/owner/policy binding.
Absent, disabled, unallowlisted, or mismatched policy returns a deterministic
failure before any adapter or network invocation.

The package implements no provider-specific client and exposes no callable
transport. Even the allow path returns `ACCEPTED_SYNTHETIC_NO_EFFECT` with
adapter and network call counts fixed at zero. Static dependency validation
rejects business, presentation, or UI imports of direct provider/transport
modules.

The operator projection accepts synthetic failure results only. It returns the
correlation, current synthetic state, adapter/capability identity, redacted
classification, reconciliation and alert eligibility, and a safe manual-action
classification. The frozen projection cannot execute or modify anything.

## Public validation

The public API is
`validate_integration_boundary(repository_root, snapshot_contract)`. The
standalone CLI requires both `--repository-root` and `--snapshot-contract`.
Both paths share the same deterministic output boundary and require an
external schema-v2 contract.

Validation requires an absolute normalized symlink-free Linux repository root,
the exact origin/repository/branch identity, the accepted S03 parent, one S04
commit, exact changed paths and `100644` modes, a clean worktree/index, exact
artifact digests, the four-requirement set, five scope dispositions, fresh
knowledge counts, and branch coverage for `ysf.integration_boundary` at or
above 90.0 percent.

Trusted package files are captured through descriptor-relative no-follow
reads. File and parent identities are checked before/after capture, worktree
bytes must equal the exact HEAD blob, and captured bytes are reused for YAML,
manifest, digest, document, and sensitive-data validation. Empty/dot aliases,
traversal, symlinks, replacement races, and descriptor leaks fail closed.

## Explicit boundary

Providers are `OFF`, email is `NON_RELAYING`, and external effects are
`DENY_ALL`. Enterprise event registry, universal integration platform, legacy
protocol blanket support, enterprise operations center, production control
plane, real provider actions, merge, release, deployment, and operational
maturity are outside S04. A fresh independent advisory review is mandatory
before any later Human Decision.

Fresh final discovery observes 125 Markdown documents and 123 governed
document codes with zero duplicates. The fresh index and knowledge build bind
the same 125 documents, 14 retained knowledge records, 8 capabilities, 0
integrations, and 48 relationships. These counts are derived from current
source and bound into the external snapshot; no stale tracked document index is
accepted as input.
