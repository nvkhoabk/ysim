# VS-R1-010 — Slice Specification

## Objective

Establish the cryptographic and schema foundation required before GPay
webhooks are allowed to mutate canonical Payment state.

## Included

- Sandbox-only configuration.
- Absolute external provider certificate path.
- RSA-SHA256 verification using the accepted GPay crypto boundary.
- Exact webhook body schema.
- Replay-window enforcement.
- Provider status normalization.
- Payment database constraints for `TEST` and `GPAY`.
- Repeatable PostgreSQL and cryptographic runtime proof.

## Excluded

- Public webhook controller.
- Payment state transition from a GPay event.
- GPay checkout-session creation.
- Production activation.
- Live external GPay requests.
- Procurement and fulfillment.

The public intake endpoint is intentionally deferred to the next slice so
cryptographic verification and provider-schema enablement can be accepted
independently.
