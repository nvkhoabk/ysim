# ADR-R1-005 — eSIM Asset Encryption and Sensitive Access

## Status

PROPOSED

## Context

An eSIM QR payload and activation code can allow installation of a purchased eSIM. Unauthorized access can cause customer loss, supplier disputes and financial impact.

Release 1 allows Support to view full QR and activation data and allows manual eSIM replacement without a separate approval step. Every sensitive action must still be auditable.

## Decision

eSIM Asset sensitive values will be protected with application-level envelope encryption or an equivalent secure-storage abstraction.

Sensitive data must never be stored in public object storage, logs, analytics events or general-purpose domain events.

## Sensitive fields

At minimum:

- QR payload.
- Activation code.
- Matching ID when sensitive.
- Supplier delivery payload.
- Any secret required to install the eSIM.

ICCID is treated as confidential customer/order data even when not encrypted under the same mechanism.

## Encryption model

Each encrypted value or secure object stores:

- Ciphertext or secure-object reference.
- Encryption algorithm and version.
- Key identifier.
- Initialization vector or nonce where required.
- Authentication tag where required.
- Created timestamp.

Production and sandbox use different keys.

Keys are not stored in the application repository or database as plaintext.

## Access rules

### Customer

Customer access requires:

- Authenticated Customer Portal session or valid magic link.
- Authorization to the matching order.
- Expiry and revocation checks.
- Audit event for reveal or download.

### Support

Support may view full data in Release 1 when:

- The user has Support permission.
- The action is linked to an order or support workflow.
- The access creates an Audit Event.
- The response is not cached publicly.

No approval is required for Release 1.

### Operations replacement

Manual replacement requires:

- Operator identity.
- Fulfillment identifier.
- Reason.
- Before/after secure references.
- Idempotency key.
- Audit event.

## Logging rules

Logs must not contain:

- Full QR payload.
- Full activation code.
- Raw secure provider response.
- Magic-link token.

Logs may contain masked identifiers and secure references.

## Delivery rules

Email may contain the QR image or installation data according to the approved Release 1 delivery policy.

Customer Portal remains the durable secure retrieval channel.

Delivery retries must not generate another fulfillment.

## Backup and retention

Encrypted eSIM data may be backed up only in encrypted backups.

Deletion and retention must follow order, dispute and supplier requirements. Release 1 operational retention is at least six months.

## Incident response

The platform must support:

- Identify all accesses to an asset.
- Disable customer presentation when required.
- Replace an eSIM Asset.
- Resend delivery.
- Open an Operations Case.
- Preserve evidence.

## Consequences

### Positive

- Reduces impact of database or storage exposure.
- Enables audited Support access.
- Supports secure Customer Portal retrieval.

### Negative

- Key management and rotation add operational complexity.
- Search over encrypted fields is limited.
- Email remains a less controlled delivery channel.

## Rejected alternatives

### Plaintext QR data in the database

Rejected due to material customer and financial risk.

### Public image URL

Rejected because URLs can be shared, indexed or cached.
