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
- [Manifest](MANIFEST.sha256) checksums all sixteen non-self paths in the
  seventeen-path authorization, including the unchanged secure-factory
  integration test, the fresh knowledge builder/test bindings, and the two
  descendant-only S02 compatibility paths. It also binds the repository
  coverage configuration and exact runtime-state ignore rules.

Configuration records bind tenant/partition identity into immutable record and
effective-resolution digests. `GLOBAL` records are tenant-neutral; every other
supported scope requires exactly one tenant, and cross-tenant inheritance is
rejected. Authentication policy rules bind actor class, role, exact method,
assurance requirement, session rule, and deterministic failure behavior.
Pre-execution validation accepts only policy, request, grants, and synthetic
verification inputs and recomputes authentication and authorization internally;
caller-created decision objects are never authority.

Knowledge generation builds its document index in memory from the current
`docs/**/*.md` bytes during every invocation. It never reads or falls back to
the tracked `factory/index/documents.json`. On this snapshot, index and
knowledge generation bind the same 124 documents; knowledge derives 8
capabilities and 48 relationships. The coverage gate uses covered branches
divided by valid branches and requires at least 90.00%; line or aggregate
coverage is not substituted for that metric.

## Validation

The public API is
`validate_configuration_access_control(repository_root, snapshot_contract)`.
The standalone CLI requires both `--repository-root` and
`--snapshot-contract`; neither observed Git evidence nor the contract has a
permissive default. An exact repository may be validated at a safe disposable
absolute path when its observed origin, branch, topology, changed paths, modes,
content, and sensitive-data gates match the external contract.

Trusted validation content is captured once through a Linux descriptor-based
boundary. Directory traversal uses descriptor-relative `O_DIRECTORY`,
`O_NOFOLLOW`, and `O_CLOEXEC`; final regular files are read through the opened
descriptor and checked with `fstat` before and after the read. Captured
worktree bytes must equal their exact `HEAD` blobs. YAML parsing, manifests,
artifact digests, README checks, and sensitive-data scanning reuse those
immutable captured bytes and do not reopen trusted pathnames.

The mandatory external contract uses schema version 2. It binds the exact
sorted sixteen-path base-to-head delta, all seventeen authorized paths and their
`100644` Git modes (including the unchanged secure-factory integration test),
and independently supplied SHA-256 values for the package specification,
manifest, and source provenance. It also binds the fresh in-memory knowledge
builder/count boundary and the covered-branches-divided-by-valid-branches
coverage metric with its exact 90.0% threshold. Schema version 1 and every
missing, extra, reordered, malformed, or mismatched binding fail closed.

The standard unified coverage invocation is
`pytest --cov=ysf.configuration_access_control --cov-branch`; it runs the
entire collected suite and needs no `COVERAGE_FILE`
environment override. Coverage state is written to
`tools/ysf/.coverage.runtime` by `tools/ysf/pyproject.toml`; that exact runtime
file and its suffix variants are ignored. The historical tracked
`tools/ysf/.coverage` bytes are never mutated by the standard run. Branch
instrumentation, the exact source package, and the 90.0% branch threshold
remain mandatory.

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
