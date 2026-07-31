# VS-R1-020 — Customer Delivery Request Core and Safe Delivery Outbox

Status: Proposed candidate.

This slice opens the Delivery bounded context. It creates one idempotent
customer eSIM delivery request from ordered READY eSIM Asset references
and records one safe integration-outbox event in the same transaction.

The outbox stores request, order, channel, locale, delivery version and
Asset count only. It does not store recipient email, Asset IDs, ICCID,
QR/LPA, short link, encrypted eSIM ciphertext or other installation data.

No transactional email provider is called and Sales Order remains
`UNFULFILLED`.
