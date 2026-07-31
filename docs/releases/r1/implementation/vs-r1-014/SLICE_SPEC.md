# VS-R1-014 Slice Specification

## Goal

Publish `payment.succeeded.v1` outbox events through an application sink
port without duplicate dispatch or unbounded inline background work.

## Included

- `FOR UPDATE SKIP LOCKED` claim ordering.
- Bounded claim lease using `available_at`.
- Attempt-number fencing for success and failure completion.
- Exponential retry from five seconds, capped at fifteen minutes.
- Sanitized `last_error` without stack traces or secrets.
- Strict Payment Success envelope and payload validation.
- A sink port for the future Procurement consumer.
- PostgreSQL runtime proof for success, idle, failure and retry.
- No automatic scheduler and no external request.

## Excluded

- No Procurement Request creation.
- No Gigago API call.
- No outbox polling daemon.
- No distributed queue.
- No production activation.

## Next boundary

A later slice may implement a Procurement sink consuming the normalized
Payment Success event. The publisher in this slice remains transport- and
supplier-neutral.
