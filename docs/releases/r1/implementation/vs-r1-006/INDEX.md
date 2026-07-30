# VS-R1-006 — Price Book and Pricing Quote

## Purpose

Introduce the first Pricing bounded context for Release 1.

This slice owns market/channel Price Books, explicit supplier-cost snapshots and immutable public Pricing Quotes.

## Documents

1. [Slice Specification](./SLICE_SPEC.md)
2. [Acceptance Checklist](./ACCEPTANCE_CHECKLIST.md)

## Runtime proof

```bash
corepack pnpm runtime:vs-r1-006
```

## Candidate validation

```bash
corepack pnpm validate:vs-r1-006
```
