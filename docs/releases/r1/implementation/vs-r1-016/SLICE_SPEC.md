# VS-R1-016 Slice Specification

## Included
- Deterministic Gigago request ID derived from Procurement Request ID.
- Strict sandbox-only configuration and allowlisted base URL.
- Explicit enablement and PROBED contract requirement.
- PUT `/api/partner/createPartnerOrder`.
- `apiKey` header without logging or response exposure.
- Payload with one plan snapshot, quantity and HTTPS callback.
- Strict Gigago envelope and `extra` response validation.
- Transport injection for controlled contract testing.
- Runtime contract harness with one simulated provider request.

## Excluded
- No live Gigago request.
- No Procurement Request status mutation.
- No supplier order-attempt persistence.
- No query/polling of supplier order status.
- No eSIM asset or delivery workflow.
- No production activation.

## Activation safety
- Adapter classes remain unregistered in Nest.
- Application startup does not require a Gigago API key.
- A later slice must provide explicit injection tokens and submission-attempt persistence before activation.
