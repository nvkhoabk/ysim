# VS-R1-006 Acceptance Checklist

## Candidate identity

- [ ] Branch is `release/vs-r1-006-price-book-pricing-quote`.
- [ ] Base is `baseline/r1/vs-r1-005/accepted-v1`.
- [ ] Candidate contains exactly 20 approved paths.
- [ ] `pnpm-lock.yaml` is unchanged.
- [ ] No generated or Windows metadata path is present.

## Domain and persistence

- [ ] Pricing migration creates all five PRI-owned tables.
- [ ] Market/currency combinations are constrained.
- [ ] Money is stored as exact integer minor units.
- [ ] Supplier Cost Snapshot verifies the active Supplier Plan hash.
- [ ] Price Book entries require a published Product Offer and matching cost snapshot.
- [ ] Price Book lifecycle is `DRAFT -> ACTIVE -> SUSPENDED`.
- [ ] Empty Price Book activation is rejected.
- [ ] Overlapping active Price Books are rejected.
- [ ] Pricing activity is append-only.

## Public quote contract

- [ ] Public quote creation requires no bootstrap token.
- [ ] VND, LAK and USD exponents are correct.
- [ ] Quote quantity is limited to 1–20.
- [ ] Quote TTL is limited to 1–900 seconds.
- [ ] Quote expiry cannot exceed the Price Book valid-to timestamp.
- [ ] Quote totals use exact integer arithmetic.
- [ ] Quote persistence explicitly casts every PostgreSQL parameter.
- [ ] Supplier cost and supplier identifiers are absent from public responses.
- [ ] Public quote responses use `Cache-Control: private, no-store`.
- [ ] Existing quote snapshot survives Price Book suspension.
- [ ] New quote is unavailable after Price Book suspension.
- [ ] Expired quote returns `EXPIRED`.

## Verification

- [ ] Frozen-lockfile install passes.
- [ ] Boundary audit passes.
- [ ] Lint passes.
- [ ] Full typecheck passes.
- [ ] Full build passes.
- [ ] All 51 tests pass.
- [ ] PostgreSQL/API runtime proof passes and preserves API process diagnostics on failure.
- [ ] Candidate validator passes.
- [ ] Working tree remains clean after committed-candidate validation.

## Exclusions confirmed

- [ ] No FX conversion is implemented.
- [ ] No discount, tax or promotion engine is implemented.
- [ ] No Checkout, Order or Payment is implemented.
- [ ] No live Gigago call or plaintext credential is used.
- [ ] No file in the separate `ysim-storefront` repository is changed.
