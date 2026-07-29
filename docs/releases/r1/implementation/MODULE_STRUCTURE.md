# R1B-00 — Module Structure

## 1. Purpose

This document defines the target code organization for the Release 1 modular monolith.

It establishes package and dependency boundaries before the first business slice is implemented.

The exact framework-specific file names may evolve, but ownership and dependency direction must remain consistent with the accepted bounded-context model.

---

## 2. API module layout

Target structure:

```text
apps/api/src/
├── app/
├── platform/
│   ├── config/
│   ├── database/
│   ├── events/
│   ├── idempotency/
│   ├── observability/
│   ├── security/
│   └── workers/
└── modules/
    ├── identity-access/
    ├── organization-agency/
    ├── catalog/
    ├── supplier-management/
    ├── pricing/
    ├── agency-commerce/
    ├── checkout/
    ├── order/
    ├── payment/
    ├── procurement/
    ├── fulfillment/
    ├── delivery/
    ├── commission/
    ├── customer-experience/
    ├── operations/
    └── audit/
```

R1B-00 does not create these directories. Each directory is introduced only when an accepted slice requires it.

---

## 3. Module internal layout

A business module should separate:

```text
<module>/
├── domain/
│   ├── aggregates/
│   ├── entities/
│   ├── value-objects/
│   ├── events/
│   ├── policies/
│   └── errors/
├── application/
│   ├── commands/
│   ├── queries/
│   ├── handlers/
│   ├── ports/
│   └── process-managers/
├── infrastructure/
│   ├── persistence/
│   ├── adapters/
│   ├── projections/
│   └── workers/
├── presentation/
│   ├── http/
│   └── dto/
└── index.ts
```

Not every slice must create every folder. Empty architectural scaffolding is not a completed increment.

---

## 4. Dependency rules

Permitted direction inside a module:

```text
presentation
    ↓
application
    ↓
domain

infrastructure
    → application ports
    → domain types where required
```

Prohibited:

- Domain importing infrastructure.
- Domain importing framework HTTP types.
- Application handlers importing another context's repository implementation.
- Presentation writing directly to persistence.
- Provider adapter writing arbitrary business tables.
- Shared package containing business aggregate logic from multiple contexts.

---

## 5. Cross-context interaction

Contexts communicate through:

- Published application commands.
- Published queries.
- Versioned contract types.
- Domain or integration events.
- Process managers.
- Read-model projections.

A context references another context using stable identifiers or immutable snapshots.

Direct ORM navigation across contexts is prohibited.

---

## 6. Shared packages

### `packages/contracts`

May contain:

- Versioned external and inter-context DTOs.
- Event envelopes.
- Command and query schemas.
- Public error codes.
- Locale-independent enum values.

Must not contain:

- Repository implementations.
- Database clients.
- Provider credentials.
- Mutable business aggregates.
- Framework-specific runtime state.

### `packages/shared`

May contain only infrastructure-neutral primitives with broad reuse, such as:

- Identifier utilities.
- Time abstractions.
- Money primitives.
- Result and error primitives.
- Correlation metadata.
- Safe serialization helpers.

A type belongs in a business module unless reuse is proven.

"Shared" is not a default location.

---

## 7. Database ownership mapping

Database artifacts must make context ownership visible.

Recommended conventions:

- Migration name includes slice or context.
- Schema comments or ownership manifest identify the context.
- Repository path matches owning module.
- Projection tables are explicitly named or documented as projections.
- Sensitive columns identify encryption or secure-reference strategy.

R1B-00 does not prescribe one database schema per context.

---

## 8. Provider adapters

Target adapter locations:

```text
modules/payment/infrastructure/adapters/
├── gpay/
├── onepay/
└── umoney/

modules/procurement/infrastructure/adapters/
└── gigago/
```

Provider adapters depend on normalized application ports.

Core domains do not import provider-specific payload types.

---

## 9. Storefront boundary

`ysim-storefront` remains a separate repository.

The Platform exposes versioned channel APIs through:

- Public catalog contracts.
- Pricing and Reference Artifact resolution.
- Checkout and Order contracts.
- Payment-action contracts.
- Customer Portal contracts.

The Storefront cannot submit trusted price, commission or provider-success status.

---

## 10. Boundary enforcement

Each executable slice must introduce or update automated checks for:

- Forbidden imports.
- Cross-context repository imports.
- Direct infrastructure imports from domain.
- Provider-specific types leaking into core contracts.
- Unapproved candidate paths.
- Secret-like content.
- Public exposure of sensitive eSIM data.

Boundary checks must run in both the working tree and clean checkout.

---

## 11. First slice mapping

`VS-R1-001 — Organization and Agency Bootstrap` may introduce:

```text
apps/api/src/modules/organization-agency/
packages/contracts/src/organization-agency/
database migration and deterministic fixtures
tests for organization scope and authorization
```

Identity integration should use the minimum accepted contract required for the slice.

The first slice must not scaffold unrelated Catalog, Payment or Fulfillment modules.
