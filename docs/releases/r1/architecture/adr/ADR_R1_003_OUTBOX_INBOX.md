# ADR-R1-003 — Transactional Outbox and Provider Inbox

## Status

PROPOSED

## Context

Release 1 depends on asynchronous and external events:

- Payment callbacks and webhooks.
- Supplier webhooks and polling.
- Delivery jobs.
- Commission transitions.
- Operations recovery.
- Cross-context projections.

Events can be duplicated, delayed, arrive out of order or fail after business state has already changed.

## Decision

YSim will implement:

1. A transactional outbox for events produced by canonical business state transitions.
2. A provider inbox for external payment and supplier events.
3. Idempotent consumers for all asynchronous processing.

## Transactional outbox

A business transaction that changes canonical state and publishes an event must commit both the state change and outbox record atomically.

Outbox records contain:

- Event ID.
- Event type and version.
- Producer context.
- Aggregate type and ID.
- Organization ID when applicable.
- Correlation ID.
- Causation ID.
- Payload.
- Publication status.
- Attempt count.
- Next-attempt timestamp.
- Last error.
- Created timestamp.
- Published timestamp.

## Provider inbox

External provider payloads are persisted before business processing.

Inbox records contain:

- Provider.
- Environment.
- External event ID when available.
- Payload hash.
- Signature-verification result.
- Secure raw-payload reference.
- Received timestamp.
- Processing status.
- Processing attempts.
- Related aggregate reference.
- Failure classification.

Invalid signatures are retained as security evidence but cannot trigger business transitions.

## Delivery semantics

The platform assumes at-least-once delivery.

Exactly-once business effect is achieved through:

- Inbox uniqueness.
- Idempotency records.
- Aggregate transition guards.
- Consumer deduplication.

## Ordering

No global event ordering is assumed.

Consumers rely on:

- Aggregate version.
- Event occurrence time.
- State-transition validation.
- Reconciliation for unknown or missing outcomes.

## Sensitive data

General events must not contain:

- QR payload.
- Activation code.
- Full provider secrets.
- Payment card data.

Events may include secure references.

## Failure handling

- Temporary publication failures are retried.
- Poison events enter an Operations Case.
- Projection failure does not roll back canonical business state.
- Unknown provider outcomes enter reconciliation.
- Failed raw-provider processing remains replayable.

## Consequences

### Positive

- Prevents lost business events.
- Supports retries and operational replay.
- Decouples provider receipt from business processing.
- Provides auditable evidence.

### Negative

- Requires workers, cleanup and monitoring.
- Eventual consistency affects projections.
- Schema and event-version discipline are required.

## Required metrics

- Oldest unpublished outbox age.
- Outbox retry count.
- Inbox duplicate count.
- Inbox signature failures.
- Poison-event count.
- Projection lag.

## Rejected alternatives

### Publish directly after database commit

Rejected because process failure can lose an event.

### Process provider webhook before persistence

Rejected because receipt cannot be reliably audited or replayed.
