# VS-R1-011 Slice Specification

## Objective

Expose `POST /api/r1/payments/gpay/webhook` and apply only verified GPay
events to the matching `GPAY` Payment Intent.

## Rules

- Provider reference resolves only a GPAY intent.
- Amount and currency match the immutable intent snapshot.
- Exact duplicate provider events are idempotent.
- Conflicting event identifiers and illegal transitions are rejected.
- Successful payment confirms the Order exactly once.
- Raw signature, certificate and payload are never returned.

## Exclusions

- No outbound GPay commercial request.
- No production activation.
- No refund or reconciliation.
- No procurement or fulfillment execution.
