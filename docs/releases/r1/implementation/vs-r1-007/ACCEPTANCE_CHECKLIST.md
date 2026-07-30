# VS-R1-007 Acceptance Checklist

## Candidate identity

- [ ] Base tag is `baseline/r1/vs-r1-006/accepted-v2`.
- [ ] Candidate contains exactly 20 approved paths.
- [ ] `pnpm-lock.yaml` is unchanged.
- [ ] No generated or Windows metadata path is committed.

## Contracts and module

- [ ] Sales Order public contracts are exported.
- [ ] Sales Order module is registered in `AppModule`.
- [ ] Public POST and token-protected GET routes are present.
- [ ] Public routes use `Cache-Control: private, no-store`.
- [ ] Public routes do not require a bootstrap token.

## Database

- [ ] Sales Order migration is present.
- [ ] Pricing Quote foreign key is restrictive.
- [ ] Pricing Quote conversion is unique.
- [ ] Order number and access-token hash are unique.
- [ ] Monetary snapshot constraints use integer minor units.
- [ ] Initial order/payment/fulfillment state is constrained.
- [ ] Idempotency, fingerprint and token hashes are constrained.
- [ ] Order activity is append-only.

## Policy and security

- [ ] Idempotency key normalization is tested.
- [ ] Email and locale normalization are tested.
- [ ] B2C-only public conversion is tested.
- [ ] Request fingerprint behavior is tested.
- [ ] Access token HMAC derivation and verification are tested.
- [ ] Raw access token is not stored.
- [ ] Public order contract contains no internal hashes or supplier data.

## Runtime

- [ ] Frozen-lockfile installation passes.
- [ ] Boundary audit and lint pass.
- [ ] Full typecheck and build pass.
- [ ] All 71 cumulative tests pass.
- [ ] All 20 VS-R1-007 tests pass.
- [ ] PostgreSQL/API runtime proof passes twice.
- [ ] Runtime fixture uses the declared Supplier Plan Mapping identifier.
- [ ] Script lint enforces `no-undef`.
- [ ] Missing idempotency key is rejected.
- [ ] Active B2C quote converts exactly.
- [ ] Token-protected read succeeds and invalid token is hidden as `404`.
- [ ] Exact replay returns the same order and token.
- [ ] Changed replay and second key are rejected.
- [ ] Expired quote is rejected.
- [ ] AGENCY quote is rejected on the public route.
- [ ] Exactly one order and one activity remain after replay attempts.
- [ ] Candidate validator passes.
- [ ] Working tree remains clean after committed validation.
