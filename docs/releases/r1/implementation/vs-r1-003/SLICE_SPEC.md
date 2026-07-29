# VS-R1-003 — Slice Specification

## 1. Business outcome

YSim Platform owns a supplier-independent canonical catalog containing Region,
Destination, Product and Product Offer. Platform Administration can create and
publish a localized eSIM data offer without using WooCommerce or Gigago as the
canonical source.

## 2. In scope

- Canonical Region.
- Canonical Destination.
- Region and Destination localization.
- Stable Product family.
- Sellable technical Product Offer.
- Multi-destination coverage.
- Fixed, daily and unlimited data policies.
- Duration and activation policy.
- Hotspot and phone-number indicators.
- English and Vietnamese mandatory localization.
- Lao optional localization.
- Draft, published and suspended Product Offer lifecycle.
- Internal Platform Administration API.
- PostgreSQL migration.
- Append-only catalog activity.
- Unit, API and database runtime evidence.

## 3. Out of scope

- Supplier plan mapping.
- Gigago API.
- Price Book and selling price.
- Agency Offer.
- Reference QR.
- Storefront public catalog API.
- WooCommerce content synchronization.
- Product images and SEO.
- Inventory or procurement.
- Automatic supplier selection.

## 4. Bounded context

Primary:

- `CAT — Catalog`

Supporting:

- `IAM — temporary internal bootstrap actor carrier`
- `AUD — future projection from append-only catalog activity`

Catalog owns all tables under the `catalog` schema introduced by this slice.

## 5. Canonical entities

### Region

A stable grouping such as Asia or Europe.

### Destination

A country or destination assigned to one Region.

### Product

A stable product family independent of supplier plans and selling terms.

### Product Offer

A sellable technical configuration containing:

- Duration.
- Data policy and allowance.
- Activation policy.
- Hotspot support.
- Phone-number inclusion.
- Network display name.
- Destination coverage.
- Localized title and short description.

Price, currency and supplier mapping are deliberately absent.

## 6. Localization policy

Supported locales:

- `en`
- `vi`
- `lo`

Every Region, Destination and Product Offer must include:

- Canonical English localization.
- Mandatory Vietnamese localization.

Lao is optional in R1.0.

When a requested locale is unavailable, the read contract falls back to
English and reports the source locale.

## 7. Product Offer lifecycle

```text
DRAFT → PUBLISHED → SUSPENDED
```

Rules:

- New Product Offers start in `DRAFT`.
- Only a draft offer can be published.
- Only a published offer can be suspended.
- Publishing records `published_at`.
- Suspending preserves the original publication timestamp.
- Published and suspended lifecycle transitions are idempotent when repeated
  in the same terminal state.
- Re-publishing a suspended offer is outside this slice.

## 8. Internal API

All routes require:

- `YSIM_BOOTSTRAP_TOKEN`
- `x-ysim-bootstrap-token`
- `x-ysim-actor-id`

Routes:

```text
POST /internal/r1/catalog/regions
POST /internal/r1/catalog/destinations
POST /internal/r1/catalog/products
POST /internal/r1/catalog/offers
POST /internal/r1/catalog/offers/:offerId/publish
POST /internal/r1/catalog/offers/:offerId/suspend
GET  /internal/r1/catalog/offers/:offerId
GET  /internal/r1/catalog/offers
```

Query parameters:

```text
locale=en|vi|lo
status=DRAFT|PUBLISHED|SUSPENDED
```

These routes are internal administration and verification contracts. The
Storefront-facing API remains assigned to VS-R1-005.

## 9. Data invariants

- Region code is globally unique.
- Destination code is globally unique.
- Product code is globally unique.
- Product Offer code is globally unique.
- Catalog codes use uppercase stable identifiers.
- Every Destination references an active Region at creation.
- Every Product Offer references an existing Product.
- Every Product Offer covers at least one active Destination.
- Coverage cannot contain duplicate Destinations.
- Product Offer data fields match its data policy.
- English and Vietnamese localizations are required.
- Cross-context foreign keys are not introduced.

## 10. Runtime proof

The runtime proof must:

1. Start real PostgreSQL.
2. Apply all committed migrations.
3. Start the real API.
4. Create Region `ASIA`.
5. Reject duplicate Region code.
6. Create Destination `JP`.
7. Create Product `JAPAN_DATA_ESIM`.
8. Reject an invalid fixed-data offer without allowance.
9. Create draft offer `JP_FIXED_5GB_7D`.
10. Prove the draft is absent from the published list.
11. Publish the offer.
12. Read Vietnamese localization.
13. Request Lao and prove English fallback.
14. Reject duplicate Product Offer code.
15. Suspend the offer.
16. Prove the suspended offer is absent from the published list.
17. Verify persisted rows and six catalog activity records.
18. Stop the API and remove temporary Docker resources.

## 11. Acceptance

The slice is accepted only after:

- Static and automated validation pass.
- PostgreSQL/API runtime proof passes.
- Candidate inventory is exact.
- Clean-checkout evidence is produced.
- Human acceptance records the final decision.
