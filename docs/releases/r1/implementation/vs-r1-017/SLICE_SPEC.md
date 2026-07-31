# VS-R1-017 Slice Specification

## Included

- `procurement.supplier_submissions` persistence.
- One submission identity per Procurement Request.
- Deterministic Gigago `request_id`.
- Payload fingerprint conflict detection.
- Claim lease and active-claim suppression.
- Attempt-count fencing for completion and failure.
- Sanitized failure evidence and bounded exponential retry.
- Provider order ID, code, status and order-status persistence.
- Atomic Procurement Request transition to `SUBMITTED`.
- Idempotent replay without another Gigago call.
- Lazy Gigago configuration loading so API startup needs no credential.
- Explicit Nest registration of the safe, dormant submission service.
- Human Review Manifest for business review during acceptance.

## Excluded

- No automatic worker or scheduler.
- No live Gigago request in runtime proof.
- No supplier-order polling.
- No eSIM Asset.
- No QR/LPA retrieval.
- No customer delivery.
- No production activation.

## Business decision

A failed attempt leaves the Procurement Request in `PENDING_SUPPLIER`.
The submission row records `FAILED`, retry time and sanitized evidence.
A later manual or scheduled invocation may safely retry using the same
deterministic provider request ID.
