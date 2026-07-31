# VS-R1-019 Slice Specification

## Included

- New Fulfillment bounded context and Nest module.
- `fulfillment.esim_assets` table owned by Fulfillment.
- No cross-context foreign keys.
- One asset identity per supplier detail ID.
- HMAC-SHA-256 ICCID fingerprint for duplicate detection.
- AES-256-GCM authenticated encryption for:
  - ICCID;
  - QR/LPA;
  - short link;
  - phone number.
- Stable AAD derived only from immutable non-sensitive identifiers.
- Lazy key loading so API startup does not require eSIM keys.
- Exact replay returns existing asset identities.
- Metadata or fingerprint conflict fails closed.
- Runtime proof verifies encrypted persistence and authenticated
  decryption without printing sensitive values.
- Human Review Manifest for secure-storage business decisions.

## Security model

Required environment references:

```text
YSIM_ESIM_ASSET_KEY_ID
YSIM_ESIM_ASSET_ENCRYPTION_KEY_B64
YSIM_ESIM_ASSET_FINGERPRINT_KEY_B64
```

Both keys must decode to exactly 32 bytes. The encryption and fingerprint
keys are distinct. The key ID is stored in the envelope; key material is
never stored in PostgreSQL or evidence.

## Asset creation policy

Asset creation requires:

- supplier code `GIGAGO`;
- supplier environment `SANDBOX`;
- exact expected-count match;
- every item status `DELIVERED`;
- valid unique supplier detail IDs;
- valid unique ICCIDs;
- QR/LPA or short link for every item.

## Excluded

- No customer delivery record.
- No delivery email.
- No customer portal exposure.
- No Sales Order fulfillment transition.
- No automatic worker.
- No key rotation or re-encryption workflow.
- No live Gigago request in runtime proof.
- No production activation.
