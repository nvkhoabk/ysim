# VS-R1-005 — Slice Specification

## 1. Business outcome

`ysim-storefront` and other read-only channel clients can consume a stable, unauthenticated Catalog API backed by canonical Product Offers and active Supplier Plan Mappings.

## 2. In scope

- Public read-only Catalog routes.
- Destination listing.
- Product Offer listing by Destination.
- Product Offer detail by stable code.
- Locale resolution from query parameter or `Accept-Language`.
- English fallback.
- Supplier-availability gating by configured environment.
- Cache-Control and Vary headers.
- Public contract types.
- Policy tests.
- PostgreSQL/API runtime proof.
- Exact candidate validation.

## 3. Out of scope

- Selling price.
- Pricing Quote.
- Cart or Checkout.
- Customer identity.
- Agency attribution.
- WooCommerce synchronization.
- Supplier identifiers in public responses.
- Supplier price or cost.
- Live Gigago calls.
- Storefront repository modification.

## 4. API routes

```text
GET /api/r1/catalog/destinations
GET /api/r1/catalog/destinations/:destinationCode/offers
GET /api/r1/catalog/offers/:offerCode
```

Supported locale inputs:

```text
?locale=en
?locale=vi
?locale=lo
Accept-Language: vi-VN
```

An explicit unsupported query locale is rejected.

## 5. Availability rule

A Product Offer is public only when all conditions are true:

- Product Offer status is `PUBLISHED`.
- At least one active Supplier Plan Mapping exists.
- The mapped Supplier Plan is active.
- The Supplier and Supplier Environment are active and usable.
- Supplier Environment matches `YSIM_CATALOG_SUPPLIER_ENVIRONMENT`.
- Supplier Environment contract status is `PROBED`.
- Referenced Destination and Region are active.

The selected environment must be explicitly configured as:

```text
SANDBOX
```

or:

```text
PRODUCTION
```

No default is assumed.

## 6. Response boundary

Public responses may include:

- Stable Catalog codes.
- Localized names and descriptions.
- Duration and data policy.
- Activation policy.
- Hotspot and phone-number capabilities.
- Network display name.
- Destination coverage.
- Catalog version.

Public responses must not include:

- Internal UUIDs.
- Supplier code.
- Supplier Plan ID.
- External Supplier Plan ID.
- Supplier cost or raw price.
- Selling price.
- Credential reference.
- Raw supplier payload.
- API key.
- Mapping ID.

## 7. Cache contract

Successful public responses include:

```text
Cache-Control: public, max-age=60, stale-while-revalidate=300
Vary: Accept-Language
```

## 8. Cross-context rule

The Storefront Catalog query repository is read-only.

It may compose Catalog and Supplier Management tables for a channel projection, but it cannot mutate either owning context.

## 9. Runtime proof

Runtime validation must:

1. Start PostgreSQL.
2. Apply all accepted migrations.
3. Start the real NestJS API.
4. Create and publish a Japan Product Offer.
5. Prove the offer is absent before Supplier mapping activation.
6. Create and activate a compatible Sandbox mapping.
7. List Japan as an available destination without authentication.
8. List only mapped and published offers.
9. Verify Vietnamese localization.
10. Verify Lao request falls back to English.
11. Verify cache headers.
12. Reject an invalid locale.
13. Return `404` for unavailable or unknown offer code.
14. Prove supplier, cost and price fields are absent.
15. Suspend the Product Offer and prove it disappears.
16. Stop API and remove Docker resources.

## 10. Acceptance

The slice is accepted only after:

- Candidate validation passes.
- Clean-checkout runtime evidence passes.
- Exact candidate inventory is proven.
- Human review records an acceptance decision.
