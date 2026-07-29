# R1A-04 — Release 1 Backlog

## 1. Purpose

This document converts the approved Release 1 capability map, bounded contexts and architecture decisions into an ordered implementation backlog.

The backlog is organized by executable vertical slices. A slice is complete only when it produces a working end-to-end outcome with automated and runtime evidence.

---

## 2. Prioritization model

Each backlog item is classified using:

- `P0`: required for the pilot critical path.
- `P1`: required for safe pilot operation but may run in parallel.
- `P2`: required for R1.1 or post-core activation.
- `DEFERRED`: outside Release 1.

Every item also identifies:

- Primary bounded context.
- Dependencies.
- External dependency, when applicable.
- Executable outcome.
- Required evidence.

---

## 3. R1.0 backlog

### EPIC-R1-01 — Platform and Organization Foundation

#### VS-R1-001 — Organization and Agency Bootstrap

- Priority: `P0`
- Primary context: `ORG`
- Supporting contexts: `IAM`, `AUD`
- Dependencies: R1 architecture baseline
- Estimated effort: 8–12 person-days

Scope:

- YSim platform organization.
- Agency organization.
- Agency lifecycle.
- Membership.
- Organization-scoped authorization.
- Organization-context audit.

Executable outcome:

- Platform Admin creates and activates an agency.
- Agency user signs in within the correct organization.
- Cross-agency access is denied.

Evidence:

- API tests.
- Authorization negative tests.
- Audit event evidence.
- Clean-checkout runtime evidence.

#### VS-R1-002 — Agency Portal Authenticated Shell

- Priority: `P0`
- Primary context: `IAM`
- Supporting contexts: `ORG`
- Dependencies: VS-R1-001
- Estimated effort: 5–8 person-days

Executable outcome:

- Agency user accesses an authenticated portal shell.
- Unauthorized users receive a deterministic denial.
- Active organization context is visible and audited.

---

### EPIC-R1-02 — Catalog and Supplier Foundation

#### VS-R1-003 — Canonical Destination and Product Offer

- Priority: `P0`
- Primary context: `CAT`
- Dependencies: VS-R1-001
- Estimated effort: 10–15 person-days

Scope:

- Destination.
- Region.
- Product.
- Product Offer.
- Data allowance.
- Validity.
- Activation policy.
- Network/operator metadata.
- Localization structure.

Executable outcome:

- Admin creates and publishes a Product Offer independent of Gigago schema.

#### VS-R1-004 — Gigago Supplier Plan Mapping

- Priority: `P0`
- Primary context: `SUP`
- Supporting contexts: `CAT`
- Dependencies: VS-R1-003
- External dependency: Gigago sandbox and production contract evidence
- Estimated effort: 8–12 person-days

Executable outcome:

- Gigago plan maps to a canonical Product Offer.
- Invalid or incomplete mappings are rejected.
- Sandbox and production methods/configuration remain separate.

#### VS-R1-005 — Storefront Catalog API

- Priority: `P0`
- Primary context: `CAT`
- Supporting contexts: `SUP`
- Dependencies: VS-R1-003, VS-R1-004
- External dependency: `ysim-storefront`
- Estimated effort: 8–12 person-days

Executable outcome:

- Storefront renders product listing and detail from YSim Platform API.
- WooCommerce remains content/SEO reference only.

---

### EPIC-R1-03 — Pricing and Agency Commerce

#### VS-R1-006 — Price Book and Pricing Quote

- Priority: `P0`
- Primary context: `PRI`
- Dependencies: VS-R1-003
- Estimated effort: 10–14 person-days

Scope:

- VND and USD Price Books.
- Market and effective period.
- Pricing Quote.
- Selling-price snapshot.
- Supplier-cost snapshot.

Executable outcome:

- Platform issues an immutable, expiring Pricing Quote.

#### VS-R1-007 — Agency Offer and Commission Rule

- Priority: `P0`
- Primary context: `AOF`
- Supporting contexts: `ORG`, `PRI`, `COM`
- Dependencies: VS-R1-001, VS-R1-006
- Estimated effort: 8–12 person-days

Executable outcome:

- Admin assigns a Product Offer, approved price and commission rule to an agency.
- Published Agency Offer Version is immutable.

#### VS-R1-008 — Signed Reference Link and QR

- Priority: `P0`
- Primary context: `AOF`
- Dependencies: VS-R1-007
- Estimated effort: 8–12 person-days

Executable outcome:

- Agency creates a reusable signed Reference QR.
- Price, agency, product, payment provider and commission cannot be changed by query-string tampering.
- Reference may expire or be revoked.

---

### EPIC-R1-04 — Checkout and Order

#### VS-R1-009 — Guest Checkout and Sales Order

- Priority: `P0`
- Primary contexts: `CHK`, `ORD`
- Dependencies: VS-R1-005, VS-R1-006, VS-R1-008
- Estimated effort: 12–18 person-days

Scope:

- Guest Checkout Session.
- Email and recipient information.
- Invoice-information capture.
- Market, locale and currency.
- Sales Order and Order Item.
- Product, price and agency snapshots.

Executable outcome:

- B2C and Reference QR checkout create a `PENDING_PAYMENT` Sales Order.
- Agency attribution survives checkout.
- Browser-provided commercial values are not trusted.

---

### EPIC-R1-05 — Payment

#### VS-R1-010 — Payment Provider Core

- Priority: `P0`
- Primary context: `PAY`
- Supporting capabilities: inbox, outbox, idempotency, reconciliation
- Dependencies: VS-R1-009
- Estimated effort: 10–15 person-days

Executable outcome:

- A normalized test provider moves Payment Intent through controlled states.
- Duplicate events create one business effect.

#### VS-R1-011 — GPay End-to-End

- Priority: `P0`
- Primary context: `PAY`
- Dependencies: VS-R1-010
- External dependencies: GPay credentials, certificate, webhook URL
- Estimated effort: 8–12 person-days

Executable outcome:

- Vietnamese customer completes GPay payment.
- Server-side evidence confirms success.
- Duplicate webhook and browser return are safe.

#### VS-R1-012 — OnePay End-to-End

- Priority: `P0`
- Primary context: `PAY`
- Dependencies: VS-R1-010
- External dependencies: OnePay sandbox/production credentials and contract
- Estimated effort: 8–12 person-days

Executable outcome:

- Customer completes supported international-card payment.
- Callback, verification, retry and reconciliation are idempotent.

#### VS-R1-012A — Full Refund Foundation

- Priority: `P1`
- Primary context: `PAY`
- Supporting contexts: `ORD`, `COM`, `OPS`
- Dependencies: VS-R1-011 or VS-R1-012
- Estimated effort: 6–10 person-days

Executable outcome:

- Operations requests a full refund.
- Provider result is recorded.
- Completed refund triggers order projection and commission reversal.

---

### EPIC-R1-06 — Procurement and Fulfillment

#### VS-R1-013 — Gigago Procurement

- Priority: `P0`
- Primary context: `PRO`
- Supporting context: `SUP`
- Dependencies: VS-R1-004 and at least one accepted payment adapter
- External dependency: Gigago API and stock behavior
- Estimated effort: 12–18 person-days

Executable outcome:

- Successful payment creates exactly one procurement.
- Supplier processing can be recovered by polling.
- Unknown outcome enters reconciliation.

#### VS-R1-014 — Secure eSIM Asset and Fulfillment

- Priority: `P0`
- Primary context: `FUL`
- Supporting contexts: `AUD`, `OPS`
- Dependencies: VS-R1-013
- Estimated effort: 12–18 person-days

Executable outcome:

- Supplier result becomes one secure eSIM Asset.
- QR and activation data are encrypted or stored through secure abstraction.
- Support access and manual replacement are audited.
- Duplicate assignment is prevented.

---

### EPIC-R1-07 — Delivery and Customer Experience

#### VS-R1-015 — Email Delivery

- Priority: `P0`
- Primary context: `DEL`
- Dependencies: VS-R1-014
- External dependency: transactional email provider
- Estimated effort: 8–12 person-days

Executable outcome:

- Fulfilled eSIM is sent in Vietnamese or English.
- Failure enters a retryable queue.
- Resend does not create another fulfillment.

#### VS-R1-016 — Customer Portal

- Priority: `P0`
- Primary context: `CXP`
- Supporting contexts: `IAM`, `ORD`, `FUL`, `DEL`
- Dependencies: VS-R1-014, VS-R1-015
- Estimated effort: 12–18 person-days

Executable outcome:

- Guest customer enters using a time-limited magic link.
- Customer views order, QR, activation code and installation guide.
- Portal remains available if email delivery failed.

---

### EPIC-R1-08 — Agency Reporting and Commission

#### VS-R1-017 — Agency Orders and Revenue Dashboard

- Priority: `P1`
- Primary projection consumers: Agency Portal
- Dependencies: VS-R1-002, VS-R1-009
- Estimated effort: 8–12 person-days

Executable outcome:

- Agency sees only its attributed orders and revenue.
- Customer information is masked according to policy.
- Report can be exported to CSV.

#### VS-R1-018 — Commission Ledger

- Priority: `P0`
- Primary context: `COM`
- Dependencies: VS-R1-007, accepted payment adapter, VS-R1-014
- Estimated effort: 10–15 person-days

Executable outcome:

- Commission moves through `ATTRIBUTED`, `ACCRUED`, `ELIGIBLE`, `REVERSED` and `PAID`.
- Fulfillment success makes commission eligible.
- Refund reverses applicable commission.
- Finance can record external payout.

---

### EPIC-R1-09 — Operations and Production Readiness

#### VS-R1-019 — Operations and Reconciliation Console

- Priority: `P0`
- Primary context: `OPS`
- Dependencies: payment, procurement, fulfillment, delivery and commission slices
- Estimated effort: 12–18 person-days

Scope:

- Payment exception queue.
- Supplier timeout queue.
- Fulfillment failure queue.
- Webhook failure queue.
- Delivery failure queue.
- Refund queue.
- Cross-context search.
- Transaction timeline.
- Manual resolution.

Executable outcome:

- Main failure cases can be resolved without direct database editing.

#### VS-R1-020 — Production Hardening and Pilot

- Priority: `P0`
- Primary responsibility: Platform Operations
- Dependencies: all required R1.0 slices
- External dependencies: production credentials and provider approval
- Estimated effort: 15–25 person-days

Scope:

- Environment and secret isolation.
- Production provider probes.
- Load and failure testing.
- Backup/restore.
- Monitoring and alerting.
- UAT.
- Runbooks and rollback.
- Internal pilot and two-agency pilot.

Executable outcome:

- Platform sustains the agreed 20 orders per minute test profile.
- No duplicate order, payment, procurement, fulfillment or commission occurs.
- Pilot production is authorized.

---

## 4. R1.1 Laos backlog

### VS-R1L-001 — Lao Localization and LAK Price Book

- Priority: `P2`
- Dependencies: catalog, pricing, customer and agency UI
- Estimated effort: 8–12 person-days

Executable outcome:

- Lao transactional content and LAK Price Book pass language and market review.

### VS-R1L-002 — uMoney Payment

- Priority: `P2`
- Dependencies: VS-R1-010 and uMoney documentation/credentials
- Estimated effort: 10–15 person-days

Executable outcome:

- uMoney payment, verification and reconciliation work in sandbox and production contract probe.

### VS-R1L-003 — Laos Pilot Readiness

- Priority: `P2`
- Dependencies: VS-R1L-001, VS-R1L-002, platform hardening
- Estimated effort: 8–12 person-days

Executable outcome:

- Lao-language UAT and first Laos agency pilot are authorized.

---

## 5. Deferred backlog

The following remain outside Release 1:

- Agency wallet.
- Credit limit and postpaid billing.
- Sub-agency.
- Multi-level commission.
- Automatic supplier optimization.
- Automatic supplier fallback.
- Partial refund.
- Top-up.
- Voice and SMS eSIM.
- Recommendation engine.
- Automated invoice issuance.
- Accounting integration.
- Partner Portal.
- Advanced white-label builder.

---

## 6. Backlog governance

A backlog item cannot enter implementation unless it has:

- Accepted upstream dependencies.
- Requirement and decision mapping.
- Named owner.
- Acceptance criteria.
- Test and runtime evidence plan.
- Security and organization-scope review.
- Migration and rollback strategy when data changes are involved.
- External credential or provider readiness assessment.

Priority changes require an update to this planning baseline or an approved delivery decision.
