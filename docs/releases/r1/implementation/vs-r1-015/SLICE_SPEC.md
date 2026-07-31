# VS-R1-015 Slice Specification

## Included
- PROC-owned `procurement.requests` table without cross-context foreign keys.
- Read-only resolution of a confirmed paid unfulfilled Sales Order.
- Active sandbox Gigago plan mapping with PROBED contract and PUT create method.
- Exact payment amount, currency, order and mapping validation.
- Idempotent replay by source event, payment intent and order.
- Payment Success sink and one-item outbox consumer service.
- PostgreSQL proof from signed payment success to Procurement Request.

## Excluded
- No Gigago API call.
- No supplier order submission.
- No eSIM asset, QR or delivery email.
- No polling daemon or production activation.
