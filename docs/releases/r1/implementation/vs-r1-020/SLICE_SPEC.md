# VS-R1-020 Slice Specification

## Included

- New Delivery bounded context and Nest module.
- `delivery.customer_delivery_requests`.
- Ordered `delivery.customer_delivery_assets` references.
- `delivery.integration_outbox`.
- Same-context foreign keys only.
- One request identity per Sales Order, channel and delivery version.
- Exact replay returning existing request and outbox IDs.
- Immutable conflict detection for order number, locale, count, Asset
  order and Asset-set hash.
- Reference-only outbox payload.
- Delivery locales: Vietnamese, Lao and English.
- Delivery channel: Email.
- Human Review Manifest for recipient-resolution and redelivery rules.

## Safe outbox contract

Event type:

```text
delivery.customer_esim_requested.v1
```

Outbox payload contains:

- schema version;
- delivery request ID;
- Sales Order ID;
- order number;
- channel;
- locale;
- delivery version;
- Asset count.

Outbox payload must not contain:

- recipient email;
- Asset IDs;
- ICCID;
- QR/LPA;
- short link;
- phone number;
- encrypted eSIM ciphertext;
- eSIM decryption keys.

## Idempotency

The identity scope is:

```text
Sales Order ID + channel + delivery version
```

Exact replay requires the same immutable metadata and ordered Asset
references. Any mismatch returns `CONFLICT`.

## Excluded

- No recipient-email snapshot.
- No eSIM Asset decryption.
- No transactional email adapter.
- No email send attempt.
- No outbox publisher.
- No Sales Order fulfillment transition.
- No automatic delivery worker.
- No live external request.
- No production activation.
