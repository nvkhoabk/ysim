# VS-R1-008 Acceptance Checklist

## Identity and boundaries

- [ ] Base is `baseline/r1/vs-r1-007/accepted-v1` at `1458c5f021ad7e75dec60a9641e8186668dc01f5`.
- [ ] Candidate contains exactly 22 approved paths.
- [ ] `pnpm-lock.yaml` is unchanged.
- [ ] Root tests import only root-declared dependencies.
- [ ] Script lint enforces `no-undef`.

## Payment Intent

- [ ] Amount and currency come from the Sales Order snapshot.
- [ ] Public creation requires idempotency and Order access-token headers.
- [ ] Exact replay returns the same Payment Intent before and after Order payment.
- [ ] Changed idempotent data is rejected.
- [ ] A second active intent is rejected.
- [ ] Raw tokens and idempotency keys are not stored.
- [ ] Public response exposes no internal hashes.

## Provider events

- [ ] TEST provider performs no external call.
- [ ] TEST provider and event route are disabled unless explicitly enabled.
- [ ] `CREATED → PENDING → FAILED` is accepted for the first attempt.
- [ ] A failed attempt permits a second Payment Intent with `attemptNumber = 2`.
- [ ] The retry can transition to `SUCCEEDED` and confirm the Order.
- [ ] Failed and expired terminal states are supported.
- [ ] Terminal states reject later transitions.
- [ ] Exact duplicate provider event creates no second business effect.
- [ ] Conflicting event-ID reuse is rejected.
- [ ] Success confirms the Order and marks it `PAID` once.
- [ ] Payment success activity records the internal actor identity.

## Verification

- [ ] Frozen install passes.
- [ ] Boundary audit, script syntax and lint pass.
- [ ] Full typecheck and build pass.
- [ ] Both VS-R1-008 test files and all 28 assertions pass.
- [ ] All 11 test files and all 99 assertions pass.
- [ ] PostgreSQL/API runtime proof passes twice.
- [ ] Candidate validator passes.
- [ ] Working tree remains clean after committed validation.

## Exclusions

- [ ] No live GPay, OnePay or uMoney request is claimed.
- [ ] No refund, reconciliation, procurement or fulfillment is claimed.
