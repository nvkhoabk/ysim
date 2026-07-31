# VS-R1-017 — Supplier Submission Persistence and Safe Gigago Sandbox Activation

Status: Proposed candidate.

This slice persists a single idempotent Gigago supplier submission for a
Procurement Request. It adds claim leases, attempt fencing, retry evidence,
provider references and the atomic transition to `SUBMITTED`.

The adapter becomes injectable without loading credentials at application
startup. There is no automatic worker and runtime proof does not call
Gigago.
