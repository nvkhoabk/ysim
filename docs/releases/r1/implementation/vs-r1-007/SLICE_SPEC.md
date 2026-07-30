# VS-R1-007 Slice Specification

## 1. Boundary

`ORD — Sales Order` owns the canonical commercial order after a Pricing
Quote is accepted by a B2C customer.

Pricing continues to own Price Books, supplier cost snapshots and Pricing
Quotes. ORD copies only the public selling-price snapshot required to
preserve the commercial agreement.

## 2. Invariants

1. One Pricing Quote can produce at most one Sales Order.
2. A quote must exist and remain active at conversion time.
3. The public route accepts only `B2C` quotes.
4. Repeating the same quote, idempotency key and request fingerprint returns
   the existing order.
5. Reusing the quote with different request data returns a conflict.
6. The order total must equal unit amount multiplied by quantity.
7. Order money is stored as integer minor units.
8. Initial state is:
   - order `PENDING_PAYMENT`;
   - payment `UNPAID`;
   - fulfillment `UNFULFILLED`.
9. The public contract never exposes supplier cost, supplier identifiers,
   idempotency hashes, request fingerprints or token hashes.
10. Order reads require an order-specific access token.
11. Raw order access tokens are never stored.
12. Public order responses are private and non-cacheable.

## 3. Public conversion contract

```text
POST /api/r1/orders
Idempotency-Key: <16-128 stable characters>
Cache-Control: private, no-store
```

Request:

```json
{
  "quoteId": "uuid",
  "customerName": "Customer name",
  "customerEmail": "customer@example.com",
  "recipientEmail": "recipient@example.com",
  "locale": "vi"
}
```

Response contains:

- immutable order snapshot;
- deterministic order access token;
- `idempotentReplay` marker.

The token is derived with HMAC-SHA-256 from:

- server-side `YSIM_ORDER_ACCESS_SECRET`;
- order UUID;
- normalized idempotency key.

Only the token hash is stored.

## 4. Public read contract

```text
GET /api/r1/orders/:orderId
x-ysim-order-access-token: <token>
Cache-Control: private, no-store
```

A missing token returns `401`. An unknown order or invalid token returns
`404`, avoiding order-existence disclosure.

## 5. Data model

### `sales_order.orders`

Stores:

- quote and Product Offer identity;
- market, currency and B2C channel;
- unit, quantity, subtotal and total snapshots;
- Price Book and entry versions;
- quote issue and expiration timestamps;
- initial order/payment/fulfillment state;
- normalized customer and recipient contacts;
- locale;
- idempotency, request and access-token hashes;
- version and creation timestamp.

### `sales_order.order_activity`

Append-only ORD activity. This slice records one
`ORDER_CREATED_FROM_QUOTE` event for a newly created order. Idempotent
replays do not mutate order state or add activity.

## 6. Idempotency

The repository locks the Pricing Quote row before checking for an existing
order. This serializes concurrent conversion attempts for one quote.

A replay is accepted only when both hashes match:

- normalized idempotency key hash;
- normalized request fingerprint.

## 7. Security and privacy

- `YSIM_ORDER_ACCESS_SECRET` must contain at least 32 UTF-8 bytes.
- Customer emails are normalized to lowercase.
- Access and idempotency values are SHA-256 hashes at rest.
- Public contracts contain no supplier or internal integrity fields.
- No bootstrap token is required by the public routes.
- No Customer Portal or long-lived account authentication is claimed.

## 8. Error behavior

| Condition | HTTP |
|---|---:|
| Invalid request or unsupported channel | 400 |
| Missing order access token | 401 |
| Quote or token-protected order not found | 404 |
| Quote already converted with different data | 409 |
| Quote expired | 410 |
| Order access secret not configured | 503 |

## 9. Acceptance runtime

The runtime proof must demonstrate:

1. Missing idempotency key is rejected.
2. Unknown quote is rejected.
3. Active B2C quote converts exactly.
4. Public order response contains no prohibited internal fields.
5. Order read requires the access token.
6. Correct token returns the immutable order.
7. Exact replay returns the same order and token.
8. Changed replay data is rejected.
9. A second idempotency key for the same quote is rejected.
10. Expired quote conversion is rejected.
11. AGENCY quote conversion is rejected on the public route.
12. Exactly one order and one ORD activity exist after replay attempts.
