# VS-R1-008 — Payment Intent Core and Test Provider

## Purpose

Establish the provider-neutral PAY bounded context after accepted Sales Order creation. The slice proves payment initiation, provider-event normalization, duplicate suppression and one order-payment business effect without relying on an external gateway.

## Business rules

1. A Payment Intent is created only for an accessible `PENDING_PAYMENT` Sales Order.
2. Browser input never supplies amount or currency; PAY copies both from the immutable Order snapshot.
3. Public creation requires `Idempotency-Key` and `x-ysim-order-access-token`.
4. Raw access tokens and idempotency keys are never stored.
5. One Order has at most one active intent in `CREATED` or `PENDING`.
6. A terminal failed or expired intent may be followed by a new attempt.
7. Provider events are unique by provider and provider-event identifier.
8. An exact duplicate event returns the existing effect; conflicting reuse is rejected.
9. `SUCCEEDED` confirms the Order and marks it `PAID` exactly once.
10. Terminal Payment Intent states are immutable.

## Public API

- `POST /api/r1/payments/intents`
- `GET /api/r1/payments/intents/:intentId`

Both responses are `private, no-store` and require the guest Order access token. Creation also requires an idempotency key.

## Internal executable provider

- `POST /internal/r1/payments/test-provider/intents/:intentId/events`

The route requires `YSIM_PAYMENT_TEST_PROVIDER_ENABLED=true`, the bootstrap token and actor identity. The TEST provider is disabled by default and must not be enabled in production. It accepts only normalized TEST events: `PENDING`, `SUCCEEDED`, `FAILED`, `EXPIRED`.

## Data ownership

PAY owns:

- Payment Intent.
- Provider-event inbox.
- PAY activity.

ORD remains owner of Sales Order. PAY updates only the accepted payment projection fields and appends an Order activity when payment succeeds.

## Security

- Public intent lookup is protected by the Order access-token hash.
- Public contracts exclude supplier cost, access-token hash, idempotency hash, request fingerprint and provider event payload.
- The TEST provider is deterministic and makes no external network request.

## Out of scope

- GPay, OnePay and uMoney adapters.
- Real provider callbacks and signature verification.
- Refunds, disputes and chargebacks.
- Reconciliation scheduler.
- Procurement and fulfillment.
