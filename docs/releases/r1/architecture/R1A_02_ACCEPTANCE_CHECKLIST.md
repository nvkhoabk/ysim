# R1A-02 Acceptance Checklist

## A. Baseline

- [ ] Branch was created from `baseline/r1/r1a-01/accepted-v1`.
- [ ] Branch name is `release/r1a-02-domain-context`.
- [ ] R1A-01 accepted baseline remains unchanged.
- [ ] VS001 recovery worktree remains unchanged.
- [ ] No runtime files are modified.
- [ ] No database files are modified.
- [ ] No package manifest is modified.
- [ ] No secret or credential is included.

## B. Domain Context Map

- [ ] IAM context is defined.
- [ ] Organization and Agency context is defined.
- [ ] Catalog context is defined.
- [ ] Supplier Management context is defined.
- [ ] Pricing context is defined.
- [ ] Agency Commerce context is defined.
- [ ] Checkout context is defined.
- [ ] Order context is defined.
- [ ] Payment context is defined.
- [ ] Procurement context is defined.
- [ ] Fulfillment context is defined.
- [ ] Delivery context is defined.
- [ ] Commission context is defined.
- [ ] Customer Experience context is defined.
- [ ] Operations context is defined.
- [ ] Audit context is defined.
- [ ] Process managers are defined.
- [ ] Dependency direction is explicit.
- [ ] Cross-context invariants are explicit.

## C. Ownership Matrix

- [ ] Every business object has one canonical owner.
- [ ] Snapshot ownership is defined.
- [ ] Organization scope is defined.
- [ ] Sensitive-data ownership is defined.
- [ ] Read access rules are defined.
- [ ] Write access rules are defined.
- [ ] State ownership is defined.
- [ ] Ownership-change policy is defined.

## D. Inter-context contracts

- [ ] Synchronous queries are defined.
- [ ] Synchronous commands are defined.
- [ ] Domain events are defined.
- [ ] Integration events are defined.
- [ ] Event envelope is defined.
- [ ] Core event contracts are listed.
- [ ] Core command contracts are listed.
- [ ] Process-manager ownership is defined.
- [ ] Idempotency scopes are defined.
- [ ] Provider inbox is defined.
- [ ] Transactional outbox is defined.
- [ ] Failure contracts are defined.
- [ ] Forbidden interactions are defined.
- [ ] Read-model projections are defined.
- [ ] Contract versioning is defined.

## E. Scope integrity

- [ ] Payment and Procurement remain separate.
- [ ] Procurement and Fulfillment remain separate.
- [ ] Fulfillment and Delivery remain separate.
- [ ] Agency Offer and Commission remain separate.
- [ ] Customer Portal does not own canonical Order data.
- [ ] Operations cannot bypass owning contexts.
- [ ] Provider adapters cannot write business tables directly.
- [ ] Storefront cannot provide trusted price or commission values.
- [ ] Overall Order status remains derived.
- [ ] Audit Event remains append-only.

## F. Candidate inventory

The candidate must contain exactly:

```text
docs/releases/r1/architecture/INDEX.md
docs/releases/r1/architecture/DOMAIN_CONTEXT_MAP.md
docs/releases/r1/architecture/DOMAIN_OWNERSHIP_MATRIX.md
docs/releases/r1/architecture/INTER_CONTEXT_CONTRACTS.md
docs/releases/r1/architecture/R1A_02_ACCEPTANCE_CHECKLIST.md
```

Validation:

- [ ] Candidate contains exactly five files cumulatively from the R1A-01 baseline.
- [ ] `git diff --check` succeeds.
- [ ] All files exist and are non-empty.
- [ ] Architecture Index links all R1A-02 documents.
- [ ] Markdown headings and checklist syntax are present.
- [ ] No runtime, database, package or artifact path is changed.
- [ ] Working tree is clean after commit.
- [ ] Candidate tag is created.

## Acceptance result

```text
R1A-02_RESULT=PENDING
```

After approval:

```text
R1A-02_RESULT=PASS
```
