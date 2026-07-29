# ADR-R1-002 — Multi-Organization Tenancy Model

## Status

PROPOSED

## Context

Release 1 includes:

- The YSim platform organization.
- Agency organizations.
- At least two agencies shortly after launch.
- A target of about 20 agencies.
- Agency-specific offers, references, orders, revenue and commission.

One identity may participate in more than one organization. Organization context must not be trusted from client-provided identifiers alone.

## Decision

YSim will use a shared-database, shared-schema multi-organization model for Release 1.

Canonical platform data and organization-scoped data remain distinct.

An authenticated session resolves an active organization context. Authorization checks use that resolved context rather than a user-supplied organization ID.

## Organization types

Release 1 supports:

- `PLATFORM`
- `AGENCY`

Sub-agency hierarchy is deferred.

## Scope rules

Organization-scoped records include:

- Membership.
- Agency profile.
- Agency Offer.
- Reference Artifact.
- Agency reporting projections.
- Commission Ledger.
- Commission Statement.

Platform-owned but market-scoped data includes:

- Catalog.
- Supplier registry.
- Product Offer.
- Price Book.
- Payment-provider configuration.

Sales Order stores both:

- Selling platform organization.
- Attribution agency organization when applicable.

## Authorization rules

- Every organization-scoped command resolves organization context from the authenticated principal.
- Agency users cannot select an arbitrary organization through a request parameter.
- Cross-organization reads are denied by default.
- Platform roles may access multiple organizations only through explicit permissions.
- Organization suspension prevents new commercial activity without deleting history.
- Organization context switches are audited.

## Data access implementation

Repository methods for organization-scoped aggregates must require organization context.

Read-model projections must preserve organization scope.

Database indexes should include organization identifiers where appropriate.

Row-level security may be evaluated later but is not required for Release 1 if application enforcement and tests are adequate.

## Consequences

### Positive

- Supports pilot agencies without separate databases.
- Lower infrastructure cost.
- Easier consolidated reporting.
- Supports one identity across organizations.

### Negative

- Application authorization defects could expose cross-agency data.
- Every scoped query requires disciplined filtering.
- Operational tools need explicit platform permissions.

## Required tests

- Agency A cannot access Agency B orders.
- Agency A cannot use Agency B Reference Artifact.
- Suspended agency cannot create new references.
- Platform Operations access is audited.
- User-supplied organization ID cannot override session context.

## Rejected alternatives

### Database per agency

Rejected for Release 1 due to operational complexity and the small number of agencies.

### Organization ID trusted from the client

Rejected because it enables horizontal authorization attacks.
