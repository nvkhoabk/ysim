# VS-R1-013 Slice Specification

## Goal

Persist a durable, idempotent Payment Success integration event when a Payment
Intent reaches `SUCCEEDED`.

## Included

- `payment.integration_outbox` owned by Payment.
- Versioned `payment.succeeded.v1` contract.
- Deterministic SHA-256 deduplication by Payment Intent.
- Transactional insertion with Payment Intent and Sales Order state changes.
- Duplicate provider webhook suppression.
- Safe payload containing commercial identifiers only.
- PostgreSQL runtime proof for success, duplicate replay and one business effect.

## Excluded

- No outbox publisher worker.
- No supplier API call.
- No Procurement Request yet.
- No fulfillment or eSIM asset creation.
- No customer email.
- No production provider request.
