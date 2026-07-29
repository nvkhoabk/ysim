# VS-R1-004 — Gigago Supplier Plan Mapping

## Documents

1. [Slice Specification](./SLICE_SPEC.md)
2. [Acceptance Checklist](./ACCEPTANCE_CHECKLIST.md)

## Executable outcome

The slice proves that:

- Gigago supplier environments are explicitly separated.
- Sandbox and production credentials are represented only by secret references.
- The documented Gigago package payload can be normalized.
- A supplier plan can map only to a compatible published Product Offer.
- Invalid or incomplete mappings are rejected.
- Sandbox mapping can become active after the sandbox contract is probed.
- Production mapping cannot become active before a production contract probe.
- No real API key or live Gigago purchase is required by this slice.

## Status

`PROPOSED`
