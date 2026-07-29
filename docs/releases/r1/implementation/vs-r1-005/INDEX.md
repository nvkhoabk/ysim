# VS-R1-005 — Storefront Catalog API

## Documents

1. [Slice Specification](./SLICE_SPEC.md)
2. [Acceptance Checklist](./ACCEPTANCE_CHECKLIST.md)

## Executable outcome

The slice proves that an unauthenticated channel client can:

- List active destinations that have at least one published Product Offer with an active Supplier Plan Mapping.
- List available Product Offers for a destination.
- Read one available Product Offer by stable code.
- Request `en`, `vi` or `lo` localization.
- Receive English fallback when the requested localization is unavailable.
- Receive no supplier identifiers, supplier cost or selling price.
- Observe deterministic cache headers.

## Status

`PROPOSED`
