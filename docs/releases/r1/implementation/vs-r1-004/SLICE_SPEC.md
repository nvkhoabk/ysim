# VS-R1-004 — Slice Specification

## 1. Business outcome

Platform Administration can import a Gigago package snapshot, validate it against a canonical published Product Offer, and activate a safe sandbox mapping without making Gigago-specific fields canonical Catalog state.

## 2. In scope

- Supplier registry.
- Gigago sandbox and production environment profiles.
- Secret references rather than plaintext credentials.
- Gigago `getPackages` payload normalization.
- Environment-specific HTTP contract metadata.
- Supplier Plan snapshot persistence.
- Compatibility assessment against a canonical Product Offer.
- Draft and active Supplier Plan Mapping lifecycle.
- Sandbox activation after a confirmed contract.
- Production activation block until production probing.
- PostgreSQL migration.
- Internal administration API.
- Fixture replay.
- Unit and runtime tests.

## 3. Out of scope

- Live Gigago credential use.
- Live `getPackages` call.
- Gigago order creation.
- Procurement.
- Fulfillment.
- Webhook processing.
- eSIM Asset.
- Supplier-price ownership.
- Automatic supplier selection.
- Automatic supplier fallback.
- Production contract confirmation.

## 4. Provider evidence applied

The Gigago documentation describes:

- Sandbox base URL: `https://sandbox-partners-api.gigago.com`.
- Production base URL: `https://partners-api.gigago.com`.
- `getPackages`: `POST`.
- `createPartnerOrder`: `PUT`.
- Documented `getMyOrdersAgency`: `PUT`.
- Package fields such as `ggg_plan_id`, `data`, `validity`, `countries`, `operator`, hotspot and phone-number flags.

Independent sandbox evidence already established that `getMyOrdersAgency` accepts `POST` while the provided document states `PUT`. Therefore:

- Sandbox confirmed query method is stored as `POST`.
- Production confirmed query method remains `NULL`.
- Production stays `DOCUMENTED_UNVERIFIED`.
- No production assumption is made from sandbox behavior.

## 5. Ownership

Primary context:

- `SUP — Supplier Management`

Supporting context:

- `CAT — Catalog`, through a read-only Product Offer query adapter.

Owned by SUP:

- Supplier.
- Supplier Environment.
- Supplier Plan snapshot.
- Supplier Plan Mapping.
- Supplier activity.

The mapping stores a stable Product Offer ID. It does not create a cross-context foreign key to Catalog.

## 6. Normalization rules

Gigago package normalization supports:

- Fixed data such as `5GB`.
- Daily data such as `1GB/day`.
- Unlimited data.
- Validity such as `7 days`.
- ISO Alpha-2 country arrays encoded as JSON strings.
- Operator arrays encoded as JSON strings.
- `Yes` and `No` capability values.
- Stable SHA-256 snapshot hash.

The documented sandbox plan `GIGA-DEMO` with `0GB` and `1 days` is accepted as a supplier fixture but is incompatible with a 5GB/7-day canonical offer.

## 7. Compatibility rules

Blocking checks:

- Canonical offer must be `PUBLISHED`.
- Duration must match.
- Data policy must match.
- Allowance must match.
- Every canonical destination must be covered.
- Required hotspot support must be present.
- Required phone-number capability must be present.

Warnings:

- Supplier plan covers extra destinations.
- Activation policy is not proven by Gigago package metadata.
- Network selection is retained but not a blocking rule in this slice.

## 8. Internal API

```text
GET  /internal/r1/suppliers/gigago/environments
POST /internal/r1/suppliers/gigago/plans/import
POST /internal/r1/suppliers/gigago/mappings
POST /internal/r1/suppliers/gigago/mappings/:mappingId/activate
GET  /internal/r1/suppliers/gigago/mappings/by-offer/:productOfferId
```

All routes require the internal bootstrap token. Write routes require an actor identity.

## 9. Runtime proof

The runtime proof must:

1. Start a real PostgreSQL container.
2. Apply all committed migrations.
3. Start the real API.
4. Verify sandbox and production environment separation.
5. Create and publish a canonical Japan 5GB/7-day Product Offer.
6. Import the documented `GIGA-DEMO` sandbox fixture.
7. Reject mapping `GIGA-DEMO` to the Japan offer.
8. Import a matching Japan sandbox fixture.
9. Create and activate the sandbox mapping.
10. Reject a duplicate mapping.
11. Import the same external plan ID into production as a separate Supplier Plan.
12. Create a production draft mapping.
13. Block production activation because the contract is unverified.
14. Read the active sandbox mapping by Product Offer.
15. Verify persisted Supplier Plan, Mapping and activity counts.
16. Stop the API and remove Docker resources.

## 10. Security

- No API key is committed.
- Environment records contain only `env://` credential references.
- Raw plan payload contains package metadata only.
- Supplier price is not promoted to canonical Pricing state.
- Production activation remains blocked.
- No provider network call occurs in validation.

## 11. Acceptance

The slice is accepted only after:

- Unit tests pass.
- PostgreSQL/API runtime proof passes.
- Candidate inventory is exact.
- Clean-checkout validation passes.
- Human review records an acceptance decision.
