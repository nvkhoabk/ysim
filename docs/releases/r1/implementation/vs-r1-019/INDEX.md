# VS-R1-019 — eSIM Asset Core and Encrypted Installation Data Persistence

Status: Proposed candidate.

This slice opens the Fulfillment bounded context and persists each
supplier-delivered eSIM as a `READY` asset. ICCID, QR/LPA, short link and
phone number are stored only inside an AES-256-GCM authenticated envelope.
A keyed HMAC fingerprint supports uniqueness without exposing ICCID.

The slice does not send customer email, expose a customer portal record,
change Sales Order fulfillment status, or start an automatic delivery
worker.
