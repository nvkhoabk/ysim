# VS-R1-008 — Payment Intent Core and Test Provider

## Outcome

A protected B2C Sales Order creates a normalized Payment Intent whose amount and currency are copied from the Order snapshot. A deterministic TEST provider drives controlled events through an idempotent provider-event inbox.

## Documents

1. [Slice specification](./SLICE_SPEC.md)
2. [Acceptance checklist](./ACCEPTANCE_CHECKLIST.md)

## Explicit exclusions

- No GPay, OnePay or uMoney network call.
- No provider webhook signature contract.
- No refund, chargeback or reconciliation scheduler.
- No procurement or fulfillment trigger.
