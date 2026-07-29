# R1A-03 Acceptance Checklist

## A. Baseline

- [ ] Branch was created from `baseline/r1/r1a-02/accepted-v1`.
- [ ] Branch name is `release/r1a-03-architecture-decisions`.
- [ ] R1A-02 accepted baseline remains unchanged.
- [ ] VS001 recovery worktree remains unchanged.
- [ ] No runtime files are modified.
- [ ] No database files are modified.
- [ ] No package manifest is modified.
- [ ] No secret or credential is included.

## B. ADR structure

- [ ] ADR Index is present.
- [ ] Every ADR has a status.
- [ ] Every ADR has context.
- [ ] Every ADR has a decision.
- [ ] Every ADR describes consequences.
- [ ] Rejected alternatives are documented where relevant.
- [ ] Architecture Index links the ADR package.

## C. Decisions

- [ ] ADR-R1-001 selects a modular monolith.
- [ ] ADR-R1-002 defines multi-organization tenancy.
- [ ] ADR-R1-003 defines transactional outbox and provider inbox.
- [ ] ADR-R1-004 defines idempotency scopes and conflict behavior.
- [ ] ADR-R1-005 defines eSIM encryption and audited access.
- [ ] ADR-R1-006 defines payment and supplier adapters.
- [ ] ADR-R1-007 keeps Storefront in a separate repository.
- [ ] ADR-R1-008 defines database ownership and foreign-key policy.

## D. Scope integrity

- [ ] No ADR introduces microservices as a Release 1 requirement.
- [ ] No ADR makes WooCommerce canonical for Order, Payment or Fulfillment.
- [ ] No ADR trusts client-provided price or commission.
- [ ] No ADR permits provider adapters to mutate arbitrary domain tables.
- [ ] No ADR stores eSIM QR data in public storage.
- [ ] No ADR permits cross-agency access.
- [ ] Sandbox and production remain isolated.
- [ ] Production provider contracts require confirmation.

## E. Candidate inventory

The candidate must contain exactly:

```text
docs/releases/r1/architecture/INDEX.md
docs/releases/r1/architecture/adr/INDEX.md
docs/releases/r1/architecture/adr/ADR_R1_001_MODULAR_MONOLITH.md
docs/releases/r1/architecture/adr/ADR_R1_002_MULTI_ORGANIZATION.md
docs/releases/r1/architecture/adr/ADR_R1_003_OUTBOX_INBOX.md
docs/releases/r1/architecture/adr/ADR_R1_004_IDEMPOTENCY.md
docs/releases/r1/architecture/adr/ADR_R1_005_ESIM_SECURITY.md
docs/releases/r1/architecture/adr/ADR_R1_006_PROVIDER_ADAPTERS.md
docs/releases/r1/architecture/adr/ADR_R1_007_STOREFRONT_BOUNDARY.md
docs/releases/r1/architecture/adr/ADR_R1_008_DATABASE_BOUNDARIES.md
docs/releases/r1/architecture/adr/R1A_03_ACCEPTANCE_CHECKLIST.md
```

Validation:

- [ ] Candidate contains exactly eleven files from the R1A-02 baseline.
- [ ] `git diff --check` succeeds.
- [ ] All required files exist and are non-empty.
- [ ] All files use LF line endings.
- [ ] ADR Index links all eight ADRs.
- [ ] No `Zone.Identifier` file exists.
- [ ] No runtime, database, package or artifact path is changed.
- [ ] Working tree is clean after commit.
- [ ] Candidate tag is created.

## Acceptance result

```text
R1A-03_RESULT=PENDING
```

After approval:

```text
R1A-03_RESULT=PASS
```
