# VS-R1-015 — Procurement Request Core and Payment Success Sink

Status: Proposed candidate.

This slice consumes `payment.succeeded.v1` through the accepted Payment outbox
publisher and creates one idempotent Procurement Request with immutable Order,
Supplier Mapping and Supplier Plan snapshots. It does not call Gigago.
