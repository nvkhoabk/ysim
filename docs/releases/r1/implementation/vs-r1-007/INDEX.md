# VS-R1-007 — Sales Order and Quote Conversion

## Objective

Create the canonical Sales Order boundary by converting one active B2C
Pricing Quote into one immutable initial Sales Order.

## Deliverables

1. `ORD — Sales Order` NestJS module.
2. PostgreSQL migration for orders and append-only order activity.
3. Public idempotent quote-to-order conversion API.
4. Token-protected public order read API.
5. Public contracts for Storefront integration.
6. Policy, service and PostgreSQL/API runtime proofs.
7. Exact candidate and clean-checkout validation tooling.

## Public routes

```text
POST /api/r1/orders
GET  /api/r1/orders/:orderId
```

The POST route requires an `Idempotency-Key` header. The GET route requires
an `x-ysim-order-access-token` header.

## Out of scope

Payment transitions, fulfillment, supplier procurement, eSIM assets,
agency order authorization, cancellation, Customer Portal authentication,
tax, discounts and promotion.
