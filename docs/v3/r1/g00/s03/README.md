---
document_code: V3-R1-G00-S03-README
document_name: Configuration and Access Control Source Baseline
project: YSim v3
document_set: V3-R1-G00-S03
version: 0.1.0
status: DRAFT
language: en
---
# V3-R1 G00 S03 — Configuration and Access Control Source Baseline

This source-only checkpoint implements deterministic reference controls for
five exact Release 1 requirements: `V3-R1-OPS-001`, `V3-R1-OPS-002`,
`V3-R1-OPS-003`, `V3-R1-SEC-001`, and `V3-R1-SEC-003`.

The implementation is `PLANNED` and
`SOURCE_VALIDATED_NON_OPERATIONAL`. It does not claim that a production
configuration, identity, authentication, authorization, delivery, or provider
system exists.

## Controlled package

- [Baseline](configuration-access-control-baseline.yaml) binds the exact
  requirement statements, Release 1 scopes, acceptance criteria, and
  out-of-scope boundaries from the immutable S01 traceability baseline.
- [Source provenance](source-provenance.yaml) binds the historical predecessor,
  exact Git blobs, source SHA-256 values, S02 governance decision, and the
  descendant-only S02 test-fixture compatibility bytes. The compatibility
  exception does not alter the accepted S02 branch or decision.
- [Package specification](package-spec.yaml) defines the exact source-only
  scope, effects boundary, and final Human Decision boundary.
- [Manifest](MANIFEST.sha256) checksums all twelve non-self paths in the
  thirteen-path corrective authorization, including the unchanged integration
  test and the two descendant-only S02 compatibility paths.

Configuration records bind tenant/partition identity into immutable record and
effective-resolution digests. `GLOBAL` records are tenant-neutral; every other
supported scope requires exactly one tenant, and cross-tenant inheritance is
rejected. Authentication policy rules bind actor class, role, exact method,
assurance requirement, session rule, and deterministic failure behavior.
Pre-execution validation accepts only policy, request, grants, and synthetic
verification inputs and recomputes authentication and authorization internally;
caller-created decision objects are never authority.

## Validation

The public API is
`validate_configuration_access_control(repository_root, snapshot_contract)`.
The standalone CLI requires both `--repository-root` and
`--snapshot-contract`; neither observed Git evidence nor the contract has a
permissive default. An exact repository may be validated at a safe disposable
absolute path when its observed origin, branch, topology, changed paths, modes,
content, and sensitive-data gates match the external contract.

## Safety boundary

Only synthetic source validation is permitted. Providers are `OFF`, email is
`NON_RELAYING`, and the external-effect budget is `DENY_ALL`. Access decisions
must pass before any delivery/provider boundary, but this package contains no
provider invocation. Legacy `docs/DIP/**` material is historical provenance
only and has no V3 maturity authority.

No merge, mark-ready action, GitHub approval review, tag, release, deployment,
production activation, payment, fulfillment, email, scheduler action, or
business external effect is authorized. A fresh independent advisory review
must PASS before the separately authorized actor may record one final Human
Decision comment.
