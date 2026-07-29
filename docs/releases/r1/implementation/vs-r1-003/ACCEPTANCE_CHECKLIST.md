# VS-R1-003 Acceptance Checklist

## A. Baseline

- [ ] Branch was created from `baseline/r1/vs-r1-002/accepted-v1`.
- [ ] Branch name is `release/vs-r1-003-canonical-catalog`.
- [ ] VS-R1-002 accepted baseline remains unchanged.
- [ ] Runtime versions match the accepted baseline.
- [ ] No secret or real credential is included.

## B. Contracts

- [ ] Catalog locales are defined.
- [ ] Region contracts are defined.
- [ ] Destination contracts are defined.
- [ ] Product contracts are defined.
- [ ] Product Offer contracts are defined.
- [ ] Data policies are defined.
- [ ] Activation policies are defined.
- [ ] Localized read contracts expose fallback source locale.
- [ ] Contract package builds successfully.

## C. Database

- [ ] Migration creates the `catalog` schema.
- [ ] Region and localization tables are CAT-owned.
- [ ] Destination and localization tables are CAT-owned.
- [ ] Product table is CAT-owned.
- [ ] Product Offer tables are CAT-owned.
- [ ] Product Offer coverage is modeled explicitly.
- [ ] Catalog activity is append-only by application contract.
- [ ] Catalog codes are unique.
- [ ] Data-policy shape is enforced by database constraints.
- [ ] Publication timestamp invariant is enforced.
- [ ] Migration runs against real PostgreSQL.
- [ ] Runtime database resources are cleaned.

## D. Domain behavior

- [ ] Codes are normalized and validated.
- [ ] English and Vietnamese localizations are mandatory.
- [ ] Duplicate locales are rejected.
- [ ] Destination IDs are unique.
- [ ] Fixed data requires `dataAmountMb`.
- [ ] Daily data requires `dailyDataAmountMb`.
- [ ] Unlimited data allows optional fair-use allowance.
- [ ] Draft offer is not returned by published filtering.
- [ ] Offer can transition from draft to published.
- [ ] Offer can transition from published to suspended.
- [ ] Unsupported transitions are rejected.
- [ ] Missing requested locale falls back to English.

## E. API and authorization

- [ ] Catalog administration routes require bootstrap authorization.
- [ ] Actor identity is required for commands.
- [ ] Region creation is supported.
- [ ] Destination creation is supported.
- [ ] Product creation is supported.
- [ ] Product Offer creation is supported.
- [ ] Product Offer publish is supported.
- [ ] Product Offer suspension is supported.
- [ ] Localized offer query is supported.
- [ ] Status-filtered offer list is supported.
- [ ] SQL uses parameterized queries.

## F. Scope integrity

- [ ] No supplier adapter is introduced.
- [ ] No Gigago mapping is introduced.
- [ ] No price or currency is stored in Catalog.
- [ ] No Agency Offer is introduced.
- [ ] No Storefront public API is claimed.
- [ ] No WooCommerce canonical ownership is introduced.
- [ ] No unrelated portal UI is introduced.

## G. Automated evidence

- [ ] Boundary audit passes.
- [ ] Lint passes.
- [ ] Contracts and API typecheck pass.
- [ ] Build passes.
- [ ] All VS-R1-001 through VS-R1-003 tests pass.
- [ ] PostgreSQL/API runtime proof passes.
- [ ] Duplicate code behavior is proven.
- [ ] Invalid data-policy behavior is proven.
- [ ] Localization fallback is proven.
- [ ] Process and Docker cleanup are verified.

## H. Candidate inventory

- [ ] Candidate contains exactly 19 approved VS-R1-003 paths.
- [ ] `pnpm-lock.yaml` remains unchanged.
- [ ] No `Zone.Identifier` file exists.
- [ ] No generated `node_modules`, `dist`, `.next`, coverage or test-report path is staged.
- [ ] `git diff --check` succeeds.
- [ ] Candidate tag is created.
- [ ] Clean-checkout evidence is produced.

## Acceptance result

```text
VS-R1-003_RESULT=PENDING
```

After human approval:

```text
VS-R1-003_RESULT=PASS
```
