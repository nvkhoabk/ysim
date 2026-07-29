# R1A-02 — Domain Ownership Matrix

## 1. Purpose

This document identifies the canonical owner of each Release 1 business object and the permitted access patterns for other contexts.

Ownership means that the context controls:

* Lifecycle.
* State transitions.
* Validation.
* Persistence contract.
* Published events.
* Write authorization.
* Recovery behavior.

No other context may directly update the owned object.

---

## 2. Canonical ownership matrix

| Business object           | Owner | Referenced by                 | Write authority            |
| ------------------------- | ----- | ----------------------------- | -------------------------- |
| Identity                  | IAM   | All authenticated contexts    | IAM only                   |
| Authentication Session    | IAM   | Portals and APIs              | IAM only                   |
| Magic Link Grant          | IAM   | Customer Experience           | IAM only                   |
| Organization              | ORG   | IAM, AOF, ORD, COM, OPS       | ORG only                   |
| Organization Membership   | ORG   | IAM, Agency Portal            | ORG only                   |
| Agency Profile            | ORG   | AOF, ORD, COM, OPS            | ORG only                   |
| Destination               | CAT   | PRI, CHK, Storefront          | CAT only                   |
| Region                    | CAT   | Storefront and reporting      | CAT only                   |
| Product                   | CAT   | PRI, AOF, ORD                 | CAT only                   |
| Product Offer             | CAT   | SUP, PRI, AOF, ORD            | CAT only                   |
| Supplier                  | SUP   | PRO, OPS                      | SUP only                   |
| Supplier Plan             | SUP   | PRO                           | SUP only                   |
| Supplier Plan Mapping     | SUP   | ORD, PRO                      | SUP only                   |
| Supplier Contract Profile | SUP   | PRO                           | SUP only                   |
| Price Book                | PRI   | Checkout and Admin            | PRI only                   |
| Price Entry               | PRI   | Pricing Quote                 | PRI only                   |
| Pricing Quote             | PRI   | CHK, ORD                      | PRI only                   |
| Agency Offer              | AOF   | Agency Portal                 | AOF only                   |
| Agency Offer Version      | AOF   | REF, CHK, ORD, COM            | AOF only                   |
| Reference Artifact        | AOF   | Storefront and Checkout       | AOF only                   |
| Attribution Context       | AOF   | CHK and ORD                   | AOF creates; ORD snapshots |
| Checkout Session          | CHK   | Storefront and Order          | CHK only                   |
| Sales Order               | ORD   | PAY, PRO, FUL, DEL, COM, OPS  | ORD only                   |
| Order Item                | ORD   | PRO, FUL, DEL, COM            | ORD only                   |
| Customer Snapshot         | ORD   | CXP, OPS                      | ORD only                   |
| Commercial Snapshot       | ORD   | PAY, COM, reporting           | ORD only                   |
| Payment Intent            | PAY   | ORD projection, OPS           | PAY only                   |
| Payment Attempt           | PAY   | OPS and reconciliation        | PAY only                   |
| Payment Webhook Event     | PAY   | OPS                           | PAY only                   |
| Refund                    | PAY   | ORD projection, COM, OPS      | PAY only                   |
| Procurement Request       | PRO   | OPS                           | PRO only                   |
| Supplier Order            | PRO   | FUL and OPS                   | PRO only                   |
| Fulfillment               | FUL   | ORD projection, DEL, COM, OPS | FUL only                   |
| eSIM Asset                | FUL   | DEL, CXP, OPS, AUD            | FUL only                   |
| Delivery Request          | DEL   | CXP and OPS                   | DEL only                   |
| Delivery Attempt          | DEL   | OPS                           | DEL only                   |
| Commission Ledger         | COM   | Agency Portal and Finance     | COM only                   |
| Commission Statement      | COM   | Agency Portal and Finance     | COM only                   |
| Customer Support Request  | CXP   | OPS                           | CXP only                   |
| Customer Order View       | CXP   | Customer Portal               | Projection only            |
| Operations Case           | OPS   | Operations Console            | OPS only                   |
| Audit Event               | AUD   | Compliance and Operations     | AUD append only            |

---

## 3. Snapshot ownership

Snapshots are immutable records copied into a downstream transactional context.

### 3.1. Order-owned snapshots

The Order Context owns immutable copies of:

* Product Offer identity and presentation fields.
* Destination.
* Data allowance.
* Validity.
* Activation policy.
* Price.
* Currency.
* Market.
* Locale.
* Customer contact.
* Invoice information.
* Agency attribution.
* Agency Offer Version.
* Commission rule.
* Supplier Plan Mapping reference.

Changes in upstream contexts do not rewrite an existing Sales Order.

### 3.2. Payment-owned snapshots

Payment owns immutable provider-attempt information:

* Provider.
* Provider configuration version.
* Amount.
* Currency.
* Merchant reference.
* Provider transaction reference.
* Signature-verification result.
* Provider response metadata.

### 3.3. Procurement-owned snapshots

Procurement owns:

* Supplier.
* Supplier Plan.
* Supplier contract profile.
* Request payload hash.
* Supplier request ID.
* Retry and polling policy version.

### 3.4. Commission-owned snapshots

Commission owns:

* Agency.
* Order.
* Agency Offer Version.
* Commission calculation type.
* Commission rate or fixed amount.
* Currency.
* Eligible amount.
* Reversal relationship.

---

## 4. Organization scope

The following aggregates are organization-scoped:

* Organization Membership.
* Agency Profile.
* Agency Offer.
* Reference Artifact.
* Agency-attributed order projections.
* Commission Ledger.
* Commission Statement.
* Agency Operations views.

The following are platform-owned but market-scoped:

* Catalog.
* Product Offer.
* Supplier registry.
* Price Book.
* Payment-provider configuration.

Sales Order stores:

* Selling organization.
* Attribution agency organization, when present.
* Market.
* Storefront/channel.
* Locale.
* Currency.

Agency users must never query Sales Orders solely by user-supplied organization ID.

The active organization context must come from an authenticated and authorized session.

---

## 5. Sensitive-data ownership

### IAM owns

* Authentication secrets.
* Session identifiers.
* Magic-link token hashes.
* Authentication audit metadata.

### ORD owns

* Customer contact snapshot.
* Invoice-information snapshot.
* Customer-facing order reference.

### PAY owns

* Payment provider transaction references.
* Signature-verification data.
* Refund records.

Payment card details must never be stored by YSim unless explicitly required and compliant with the provider contract.

### FUL owns

* ICCID.
* QR payload.
* Activation code.
* Secure eSIM Asset references.

### AUD owns

* Sensitive-data access events.
* Administrative actions.
* Before/after metadata for manual replacement.

---

## 6. Read access rules

A context may read another context through one of the following:

1. Published query contract.
2. Immutable snapshot.
3. Event-driven projection.
4. Explicit application service.
5. Operational read model.

A context must not read another context through:

* Direct repository import.
* Direct table access.
* Shared mutable ORM model.
* Unrestricted SQL joins inside business services.
* Provider adapter access to business repositories.

Reporting and Operations may use dedicated projection stores.

Projection data is not canonical and cannot be used to bypass owner validation.

---

## 7. Write access rules

All writes must be issued as commands to the owning context.

Examples:

* Operations requests `ReplaceEsimAsset`; Fulfillment performs the replacement.
* Finance requests `MarkCommissionPaid`; Commission validates and applies the transition.
* Checkout requests `CreateSalesOrder`; Order creates the aggregate.
* Payment publishes `PaymentSucceeded`; Order updates its projection.
* Refund completion publishes an event; Commission performs reversal.
* Customer requests resend; Delivery creates a new Delivery Attempt.

No context may directly set another context's status field.

---

## 8. State ownership

| State                      | Canonical owner |
| -------------------------- | --------------- |
| Organization status        | ORG             |
| Product publication status | CAT             |
| Supplier status            | SUP             |
| Pricing Quote status       | PRI             |
| Reference Artifact status  | AOF             |
| Checkout Session status    | CHK             |
| Sales Order lifecycle      | ORD             |
| Payment status             | PAY             |
| Procurement status         | PRO             |
| Fulfillment status         | FUL             |
| Delivery status            | DEL             |
| Commission status          | COM             |
| Operations Case status     | OPS             |

Overall Order status is a derived projection.

It must not replace the canonical states above.

---

## 9. Ownership change policy

Changing canonical ownership requires:

1. A new architecture decision record.
2. Migration impact analysis.
3. API and event compatibility analysis.
4. Data migration plan.
5. Rollback plan.
6. Audit of all dependent contexts.
7. Human approval before implementation.

Existing ownership history must not be rewritten.
