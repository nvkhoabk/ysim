# VS-R1-012 Slice Specification

## Goal

Allow the public Payment Intent API to accept `provider=GPAY` and reserve
an internal, normalized GPay Payment Intent safely.

## Included

- A provider-aware Payment Intent selection policy.
- A sandbox-only `GPayIntentProvider`.
- A normalized `GPY-<UUIDHEX>` provider reference.
- Fifteen-minute Payment Intent expiry.
- Provider routing in `PaymentService`.
- Existing idempotency, order-token and active-intent protections.
- PostgreSQL runtime proof from GPAY reservation through signed webhook
  completion.
- No raw credential, certificate or private-key response fields.

## Excluded

- No live outbound GPay checkout request.
- No GPay QR or redirect URL.
- No production activation.
- No procurement or fulfillment.
- No OnePay or uMoney implementation.

## Security and lifecycle

GPAY reservation requires:

- `YSIM_GPAY_PAYMENT_ENABLED=true`
- `YSIM_GPAY_ENVIRONMENT=SANDBOX`
- `YSIM_GPAY_CONTRACT_STATUS=PROBED`

Production remains fail-closed. Live provider checkout initiation must
wait for a separately accepted external contract slice.
