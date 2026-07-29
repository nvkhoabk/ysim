# ADR-R1-001 — Modular Monolith for Release 1

## Status

PROPOSED

## Context

Release 1 must support B2C commerce, agency sales, three currencies, three languages, multiple payment providers, Gigago fulfillment, Customer Portal, Agency Portal, commission, operations and audit.

The pilot load is approximately:

- 300 orders per day.
- Peak 20 orders per minute.
- About 20 agencies.
- About six suppliers within twelve months.

The platform requires strict domain ownership but does not yet justify the deployment and operational cost of many independent microservices.

## Decision

Release 1 will use a modular monolith.

The application may run multiple process types, such as API and background worker, but they share one versioned application codebase and one release lifecycle.

Each bounded context must expose explicit application contracts and must own its domain model, repositories, state transitions and events.

Cross-context repository imports and direct table mutation are prohibited.

## Required module boundaries

The implementation must preserve separate modules for:

- Identity and Access.
- Organization and Agency.
- Catalog.
- Supplier Management.
- Pricing.
- Agency Commerce.
- Checkout.
- Order.
- Payment.
- Procurement.
- Fulfillment.
- Delivery.
- Commission.
- Customer Experience.
- Operations.
- Audit.

## Deployment model

Release 1 may deploy:

- One API process.
- One or more background workers.
- One PostgreSQL database per environment.
- One Redis or queue service per environment when introduced.
- Separate sandbox and production credentials and namespaces.

These processes remain part of one modular application release.

## Consequences

### Positive

- Lower operational complexity.
- Easier transactional consistency.
- Faster delivery for the pilot.
- Clear migration path to services later.
- Easier local and clean-checkout testing.

### Negative

- A defective release can affect multiple modules.
- Resource scaling is coarser than independent services.
- Boundary discipline must be enforced in code review and tests.

## Guardrails

- No cross-context repository imports.
- No provider-specific logic inside core aggregates.
- No shared mutable domain model.
- No context may update another context's canonical state.
- Boundary tests must run in CI.
- Process managers coordinate cross-context workflows.

## Service extraction criteria

A context may be extracted only when at least one condition is proven:

- Independent scaling is materially required.
- Regulatory or security isolation is required.
- Deployment cadence is independently constrained.
- Reliability isolation is required.
- Team ownership justifies the operational cost.

Extraction requires a new ADR.

## Rejected alternatives

### Microservices from Release 1

Rejected because operational overhead is disproportionate to pilot scale and team size.

### Single-layer monolith

Rejected because it would allow uncontrolled coupling and make future supplier, agency and payment growth unsafe.
