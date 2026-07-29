# R1A-01 — Release 1 Vertical Slice Plan

## 1. Purpose

This document defines the implementation order for Release 1.

Each vertical slice must produce an end-to-end executable increment across the required layers:

```text
User or operator action
→ API contract
→ Application service
→ Domain behavior
→ Persistence
→ Integration
→ Observable result
→ Automated and runtime evidence
```

A database schema, UI mock, adapter skeleton or isolated API endpoint is not a completed vertical slice.

---

## 2. Delivery principles

1. Implement a modular monolith.
2. Keep business domains separated by application boundaries.
3. Use provider adapters for payment and supplier integrations.
4. Persist immutable commercial and attribution snapshots.
5. Require idempotency for externally triggered operations.
6. Include failure and recovery behavior in the same slice as the happy path.
7. Do not merge a slice without runtime evidence.
8. Do not begin a dependent slice before its required contracts are accepted.
9. Maintain sandbox and production configuration separation.
10. Keep `ysim-storefront` as a separate repository and API consumer.

---

## 3. Critical path

```text
Organization
→ Agency
→ Product Offer
→ Supplier Mapping
→ Price Book
→ Agency Offer
→ Reference QR
→ Guest Checkout
→ Sales Order
→ Payment
→ Procurement
→ Fulfillment
→ eSIM Delivery
→ Operations Recovery
→ Pilot UAT
```

Customer Portal, Agency Portal reporting and Commission UI may be developed partly in parallel after their underlying domain contracts are stable.

---

## 4. R1.0 implementation slices

### VS-R1-001 — Organization and Agency Bootstrap

Scope:

* YSim organization.
* Agency organization.
* Agency lifecycle.
* Agency membership.
* Organization-scoped access.

Executable result:

* Admin creates an agency.
* Agency user signs in.
* Agency user can access only its organization.

Dependencies:

* Platform foundation.

### VS-R1-002 — Agency Portal Authenticated Shell

Scope:

* Agency login.
* Agency navigation.
* Role enforcement.
* Empty dashboard states.
* Session and organization context.

Executable result:

* Authorized agency user enters the correct agency portal.
* Unauthorized organization access is denied and audited.

Dependencies:

* VS-R1-001.

### VS-R1-003 — Canonical Destination and Product Offer

Scope:

* Destination.
* Region.
* Product.
* Product Offer.
* Data allowance.
* Validity.
* Activation policy.
* Network metadata.

Executable result:

* Admin creates or imports a normalized Product Offer.
* API returns the Product Offer independently of Gigago structure.

Dependencies:

* VS-R1-001.

### VS-R1-004 — Gigago Supplier Plan Mapping

Scope:

* Supplier registry.
* Supplier Plan.
* Gigago normalization.
* Product Offer mapping.
* Sandbox/production method configuration.

Executable result:

* A Gigago plan is mapped to a canonical Product Offer.
* Mapping validation detects incomplete or invalid supplier metadata.

Dependencies:

* VS-R1-003.

### VS-R1-005 — Storefront Catalog API

Scope:

* Public product query.
* Destination filter.
* Locale.
* Market.
* Product content reference.
* Availability projection.

Executable result:

* `ysim-storefront` can render a product list and detail from YSim API.
* WooCommerce remains content/SEO reference only.

Dependencies:

* VS-R1-003.
* VS-R1-004.

### VS-R1-006 — Price Book and Pricing Quote

Scope:

* VND and USD Price Books.
* Market and effective period.
* Price quote.
* Selling-price snapshot.
* Supplier-cost snapshot.

Executable result:

* Checkout obtains an approved price quote.
* Quote remains immutable for its validity period.

Dependencies:

* VS-R1-003.

### VS-R1-007 — Agency Offer and Commission Rule

Scope:

* Product entitlement.
* Agency Offer.
* Agency Offer Version.
* Fixed or percentage commission.
* Effective period.

Executable result:

* Admin assigns a sellable offer and commission rule to an agency.
* Agency cannot modify the approved selling price.

Dependencies:

* VS-R1-001.
* VS-R1-006.

### VS-R1-008 — Signed Reference Link and QR

Scope:

* Signed reference token.
* Agency Offer Version reference.
* Locale.
* Currency.
* Payment provider.
* Expiry.
* Revocation.
* QR image generation.

Executable result:

* Agency generates a reusable QR.
* Customer opens the QR and reaches the correct checkout.
* Query-parameter tampering cannot change price, agency or commission.

Dependencies:

* VS-R1-007.

### VS-R1-009 — Guest Checkout and Sales Order

Scope:

* Guest Checkout Session.
* Customer email.
* Market, locale and currency.
* Invoice information.
* Sales Order.
* Order Item.
* Product, price and agency snapshots.

Executable result:

* B2C and Reference QR checkout both create a `PENDING_PAYMENT` Sales Order.
* Agency attribution survives checkout creation.

Dependencies:

* VS-R1-005.
* VS-R1-006.
* VS-R1-008.

### VS-R1-010 — Payment Provider Core

Scope:

* Payment provider contract.
* Payment Intent.
* Payment Attempt.
* Webhook inbox.
* Signature verification contract.
* Idempotency.
* Expiration.
* Retry.
* Reconciliation contract.

Executable result:

* A test provider can move a Payment Intent through controlled states.
* Duplicate external events do not create duplicate transitions.

Dependencies:

* VS-R1-009.

### VS-R1-011 — GPay End-to-End

Scope:

* GPay initiation.
* Redirect.
* Callback.
* Webhook.
* Verification.
* Reconciliation.
* Failure and expiration.

Executable result:

* A Vietnamese customer pays using GPay.
* Server-side verification confirms payment.
* Duplicate webhook does not create duplicate success.

Dependencies:

* VS-R1-010.

### VS-R1-012 — OnePay End-to-End

Scope:

* OnePay initiation.
* International card payment.
* Callback.
* Verification.
* Reconciliation.
* Failure behavior.

Executable result:

* A customer pays by supported international credit card.
* Payment state remains correct despite repeated redirect or callback.

Dependencies:

* VS-R1-010.

This slice should reuse proven evidence and lessons from the `ysim-storefront` OnePay integration without copying channel-specific code directly.

### VS-R1-013 — Gigago Procurement

Scope:

* Supplier Gateway.
* Procurement validation.
* Supplier order.
* Request correlation.
* Configurable sandbox/production contract.
* Retry and polling.

Executable result:

* A successful payment creates exactly one Gigago procurement.
* A processing supplier order can be recovered by polling.

Dependencies:

* VS-R1-004.
* VS-R1-011 or VS-R1-012.

### VS-R1-014 — Secure eSIM Asset and Fulfillment

Scope:

* Fulfillment state machine.
* ICCID.
* QR payload.
* Activation code.
* Secure storage.
* Duplicate prevention.
* Manual replacement.
* Support access audit.

Executable result:

* Supplier result is normalized into one eSIM Asset.
* Support can view and replace the eSIM.
* Every sensitive access and replacement is audited.

Dependencies:

* VS-R1-013.

### VS-R1-015 — Email Delivery

Scope:

* Email delivery job.
* Vietnamese and English templates.
* Retry.
* Delivery status.
* Resend.

Executable result:

* Fulfilled eSIM is sent automatically.
* Email failure enters a recoverable queue.
* Resend does not create another fulfillment.

Dependencies:

* VS-R1-014.

### VS-R1-016 — Customer Portal

Scope:

* Magic link.
* Order list.
* Order detail.
* QR display.
* Activation code.
* Installation guide.
* Support request.

Executable result:

* Guest customer accesses the order without creating a password.
* Customer can retrieve the eSIM even if the original email failed.

Dependencies:

* VS-R1-014.
* VS-R1-015.

### VS-R1-017 — Agency Orders and Revenue Dashboard

Scope:

* Agency-attributed order list.
* Revenue summary.
* Filters.
* Masked customer information.
* CSV export.

Executable result:

* Agency sees only its attributed orders and revenue.
* Cross-agency access is denied.

Dependencies:

* VS-R1-009.
* VS-R1-002.

### VS-R1-018 — Commission Ledger

Scope:

* ATTRIBUTED.
* ACCRUED.
* ELIGIBLE.
* REVERSED.
* PAID.
* Commission statement.
* Manual mark as paid.

Executable result:

* Fulfillment success makes commission eligible.
* Refund reverses the corresponding commission.
* Finance can mark an external payment as paid.

Dependencies:

* VS-R1-007.
* VS-R1-011 or VS-R1-012.
* VS-R1-014.

### VS-R1-019 — Operations and Reconciliation Console

Scope:

* Payment exception queue.
* Supplier timeout queue.
* Fulfillment failure queue.
* Webhook failure queue.
* Delivery failure queue.
* Refund queue.
* Search.
* Transaction timeline.
* Manual resolution.

Executable result:

* Operations can recover main failure cases without editing the database.
* A transaction can be traced from Reference QR to commission.

Dependencies:

* VS-R1-011.
* VS-R1-012.
* VS-R1-013.
* VS-R1-014.
* VS-R1-015.
* VS-R1-018.

### VS-R1-020 — Production Hardening and Pilot

Scope:

* Environment separation.
* Secret separation.
* Production provider probes.
* Load testing.
* Backup and restore.
* Monitoring.
* Alerting.
* UAT.
* Rollback.
* Runbooks.

Executable result:

* System sustains 20 orders per minute under the agreed test profile.
* No order, payment, fulfillment or commission duplication occurs.
* Pilot can begin with YSim internal users and two agencies.

Dependencies:

* VS-R1-001 through VS-R1-019.

---

## 5. R1.1 Laos activation slices

### VS-R1L-001 — Lao Localization and LAK Price Book

Scope:

* Lao interface content.
* Lao transactional content.
* LAK Price Book.
* Laos market policy.

Dependencies:

* VS-R1-005.
* VS-R1-006.
* VS-R1-016.
* VS-R1-017.

### VS-R1L-002 — uMoney Payment

Scope:

* uMoney adapter.
* Payment initiation.
* Webhook or polling.
* Signature verification.
* Reconciliation.
* Refund behavior where supported.

Dependencies:

* VS-R1-010.
* Provider documentation and credentials.

### VS-R1L-003 — Laos Pilot Readiness

Scope:

* Laos operations runbook.
* uMoney production probe.
* Lao-language UAT.
* Agency pilot in Laos.
* Settlement validation.

Dependencies:

* VS-R1L-001.
* VS-R1L-002.
* VS-R1-020 platform hardening.

---

## 6. Parallel delivery lanes

After VS-R1-009, the work may be divided into lanes:

### Commerce lane

* VS-R1-010.
* VS-R1-011.
* VS-R1-012.

### Fulfillment lane

* VS-R1-013.
* VS-R1-014.
* VS-R1-015.
* VS-R1-016.

### Agency lane

* VS-R1-017.
* VS-R1-018.

### Operations lane

* VS-R1-019.
* VS-R1-020.

Parallel work must not bypass domain contract acceptance.

---

## 7. Slice Definition of Done

Every vertical slice must have:

* Requirement and decision mapping.
* Accepted API contract.
* Accepted data model.
* Migration and rollback strategy.
* Authorization rules.
* Locale behavior where applicable.
* Idempotency behavior where applicable.
* Happy-path automated tests.
* Negative and duplicate-event tests.
* Runtime evidence.
* Clean-checkout evidence.
* Human acceptance result.
* Candidate tag.
* Accepted tag after approval.

---

## 8. Release timing baseline

With a team of four to six contributors:

* Architecture and planning: 1–2 weeks.
* Foundation through checkout: 6–9 weeks.
* Payment and fulfillment: 5–7 weeks.
* Customer and agency portals: 3–5 weeks.
* Operations and hardening: 3–5 weeks.

R1.0 Core Pilot baseline:

* Approximately 16–20 weeks.

R1.1 Laos Activation:

* Approximately 3–5 additional weeks.
* May overlap with late R1.0 work if uMoney dependencies are available.
