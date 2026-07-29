# ADR-R1-004 — Idempotency Strategy

## Status

PROPOSED

## Context

The platform receives repeated actions from:

- Storefront retries.
- Browser redirects.
- Payment webhooks.
- Supplier webhooks.
- Polling jobs.
- Delivery retries.
- Operations commands.

Repeated processing could create duplicate orders, payments, supplier purchases, eSIM assignments or commissions.

## Decision

Every externally repeatable business command must have an explicit idempotency scope.

The platform stores idempotency records and also enforces domain-level uniqueness and transition guards.

## Required scopes

| Operation | Scope |
|---|---|
| Create Sales Order | Checkout Session |
| Start Payment | Sales Order plus provider |
| Provider webhook | Provider plus external event ID or payload fingerprint |
| Confirm payment | Payment Intent plus provider transaction |
| Request procurement | Order Item plus fulfillment requirement |
| Create supplier order | Procurement Request |
| Assign eSIM Asset | Fulfillment plus supplier result |
| Request delivery | Fulfillment plus channel |
| Resend delivery | Delivery Request plus resend request |
| Create commission transition | Order plus transition |
| Refund | Payment Intent plus refund request |

## Idempotency record

Each record contains:

- Idempotency key.
- Operation name.
- Organization or tenant scope where applicable.
- Request hash.
- Processing status.
- Result reference.
- Response metadata where safe.
- Created timestamp.
- Completion timestamp.
- Retention or expiry.
- Correlation ID.

## Request-hash rule

The same idempotency key with an equivalent request returns the stored result.

The same key with a different request hash is rejected as an idempotency conflict.

## In-progress rule

Concurrent calls using the same key must not execute the business effect twice.

The second call either:

- Returns an in-progress response.
- Waits for the first result within a defined timeout.
- Reads the completed stored result.

## Domain safeguards

Idempotency records do not replace domain invariants.

Required domain constraints include:

- One active payment initiation per permitted scope.
- One supplier purchase per procurement request.
- One active eSIM assignment per fulfillment requirement.
- One commission transition per order and transition type.
- One provider inbox record per external event identity.

## Provider events without event IDs

When a provider does not supply a stable event ID, the adapter derives a fingerprint from normalized immutable fields and payload hash.

The derivation must be provider-specific and versioned.

## Retention

Idempotency evidence for commercial operations is retained for at least the operational retention period of six months, unless a longer payment or regulatory requirement applies.

## Consequences

### Positive

- Prevents duplicate commercial effects.
- Supports safe retries.
- Simplifies recovery and reconciliation.

### Negative

- Requires storage and cleanup policy.
- Poor key design can block legitimate operations.
- Provider-specific event identity must be understood.

## Required tests

- Duplicate checkout confirmation creates one order.
- Duplicate payment webhook creates one success transition.
- Repeated procurement creates one supplier order.
- Repeated fulfillment result assigns one eSIM.
- Same key with changed amount is rejected.
- Concurrent duplicate requests produce one effect.
