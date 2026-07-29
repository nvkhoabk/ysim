# ADR-R1-008 — Database Ownership and Cross-Context Foreign Keys

## Status

PROPOSED

## Context

Release 1 uses a modular monolith and may use one PostgreSQL database per environment.

A shared physical database can accidentally create direct lifecycle coupling through ORM relations, cascade deletes and unrestricted joins.

## Decision

Each table has exactly one owning bounded context.

Cross-context references use stable identifiers and application contracts.

Cross-context foreign keys are disallowed by default and require an explicit exception recorded in an ADR or approved schema decision.

## Ownership rules

- Repository implementations remain inside the owning module.
- A context cannot import another context's repository implementation.
- A context cannot update another context's tables.
- Cross-context ORM navigation is prohibited.
- Canonical state is changed only through the owning application service.
- Read projections may combine multiple contexts but are non-canonical.

## Same-context foreign keys

Foreign keys inside one bounded context are permitted and encouraged when they enforce aggregate or context invariants.

Examples:

- Order Item to Sales Order.
- Payment Attempt to Payment Intent.
- Delivery Attempt to Delivery Request.

## Cross-context references

A cross-context record stores the referenced stable ID and, when required, an immutable snapshot.

The owning context validates the reference through:

- Published query contract.
- Command contract.
- Event projection.
- Creation-time snapshot.

## Exception criteria

A cross-context foreign key may be considered only when:

- The referenced lifecycle is strictly stable.
- Deletion semantics are safe.
- It does not imply write ownership.
- It does not create cascade behavior across contexts.
- Migration and service-extraction impact is documented.
- The architecture owner approves it.

## Delete policy

Commercial and audit records use explicit lifecycle states rather than cascade deletion.

Required behavior:

- Orders are not deleted when a Product Offer changes.
- Payment history is not deleted when an agency is suspended.
- eSIM access audit is append-only.
- Supplier deactivation does not delete historical Supplier Orders.
- Organization deletion is not a Release 1 operation.

## Projection tables

Projection tables:

- May join or denormalize multiple contexts.
- Must be named or documented as projections.
- Are rebuildable.
- Cannot be used to authorize canonical writes without owner validation.
- Have observable rebuild and lag status.

## Migration rules

Each migration must identify:

- Owning context for every new table.
- Whether references are same-context or cross-context.
- Snapshot strategy.
- Rollback or forward-fix strategy.
- Retention and sensitive-data treatment.

## Consequences

### Positive

- Preserves modular boundaries.
- Reduces accidental cascade coupling.
- Simplifies future service extraction.
- Makes ownership reviewable in migrations.

### Negative

- Some integrity checks move to application logic.
- Reporting requires projections.
- Developers cannot rely on unrestricted ORM graphs.

## Rejected alternatives

### Foreign keys everywhere

Rejected because physical integrity would create hidden domain ownership and lifecycle coupling.

### Separate database per context in Release 1

Rejected because it increases operational and transactional complexity beyond pilot needs.
