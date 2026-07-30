# VS-R1-006 — Price Book and Pricing Quote

## 1. Objective

Create the `PRI — Pricing` bounded context and expose a public, immutable Pricing Quote contract that later Order and Checkout slices can consume.

## 2. Supported commercial dimensions

### Markets and currencies

| Market | Currency | Minor-unit exponent |
|---|---|---:|
| `VN` | `VND` | 0 |
| `LA` | `LAK` | 0 |
| `INTERNATIONAL` | `USD` | 2 |

No FX conversion is performed in this slice. A Price Book is authored directly in its selling currency.

### Sales channels

- `B2C`
- `AGENCY`

Agency-specific overrides, referral attribution and commission calculation remain outside this slice.

## 3. Price Book lifecycle

```text
DRAFT -> ACTIVE -> SUSPENDED
```

Rules:

- Entries may only be added while the Price Book is `DRAFT`.
- Activation requires at least one entry.
- Two active Price Books for the same market, currency and channel may not overlap.
- Active Price Books are immutable in this slice.
- A suspended Price Book cannot issue new quotes.

## 4. Supplier cost snapshot

Supplier cost is not read directly from an untyped provider payload when a quote is issued.

An operator creates an immutable `SupplierCostSnapshot` with:

- Active Supplier Plan Mapping ID.
- Product Offer ID resolved from that mapping.
- Explicit supplier environment.
- Explicit currency.
- Integer-string unit cost in minor units.
- Supplier plan snapshot SHA-256 hash.
- Observed timestamp.

The hash must match the currently active normalized Supplier Plan snapshot.

Supplier cost never appears in the public Pricing Quote response.

## 5. Price Book entry

Each entry binds:

- One draft Price Book.
- One published canonical Product Offer.
- One selling unit amount.
- One matching immutable Supplier Cost Snapshot.

A Product Offer may appear only once in a Price Book.

## 6. Pricing Quote

Public routes:

```text
POST /api/r1/pricing/quotes
GET  /api/r1/pricing/quotes/:quoteId
```

The create request contains:

- Product Offer code.
- Market.
- Currency.
- Channel.
- Quantity from 1 to 20.
- Optional TTL from 1 to 900 seconds.

A quote is issued only when:

- Product Offer is `PUBLISHED`.
- A matching active Price Book is effective.
- Its entry has an active Supplier Plan Mapping in the configured supplier environment.
- Supplier environment contract is `PROBED`.
- Supplier and Supplier Plan remain active.

The public quote snapshots:

- Selling unit amount.
- Quantity.
- Subtotal and total.
- Currency exponent.
- Price Book code/version.
- Entry version.
- Issue and expiry timestamps.

The quote remains an immutable snapshot after its Price Book is suspended. Its status is derived from `expiresAt`. Public quote responses use `Cache-Control: private, no-store`.

## 7. Money rules

All input and output money amounts use positive decimal strings in minor units.

Examples:

- `169000` VND means 169,000 VND.
- `250000` LAK means 250,000 LAK.
- `1299` USD means USD 12.99.

JavaScript floating-point arithmetic is prohibited. Multiplication uses `BigInt`, while PostgreSQL stores amounts as exact `NUMERIC(20,0)` values.

## 8. Internal administration routes

```text
POST /internal/r1/pricing/price-books
POST /internal/r1/pricing/supplier-cost-snapshots
POST /internal/r1/pricing/price-books/:priceBookId/entries
POST /internal/r1/pricing/price-books/:priceBookId/activate
POST /internal/r1/pricing/price-books/:priceBookId/suspend
```

These routes require the accepted bootstrap token and actor identity headers.

## 9. Persistence ownership

The Pricing context owns:

- `pricing.price_books`
- `pricing.supplier_cost_snapshots`
- `pricing.price_book_entries`
- `pricing.pricing_quotes`
- `pricing.pricing_activity`

Cross-context Product Offer and Supplier Mapping identifiers are stable references without database foreign keys.

## 10. Explicit exclusions

VS-R1-006 does not implement:

- FX conversion.
- Discounts, tax or promotion rules.
- Agency-specific price overrides.
- Commission calculation.
- Cart, Checkout, Order or Payment.
- Quote reservation of inventory.
- Live Gigago calls.
- Any change to the separate `ysim-storefront` repository.
