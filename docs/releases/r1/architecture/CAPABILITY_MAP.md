# R1A-01 — Release 1 Capability Map

## 1. Purpose

This document translates the approved Release 1 definition into an implementation capability map.

It identifies:

* Business capabilities required for R1.0 Core Pilot.
* Capabilities activated in R1.1 Laos Activation.
* Deferred capabilities.
* Canonical ownership.
* Dependencies between domains.
* Minimum operational capabilities required for pilot production.

This document does not define database tables, API payloads or user-interface components.

---

## 2. Release boundaries

### R1.0 — Core Pilot

R1.0 delivers pilot production for:

* YSim B2C Storefront.
* Agency referral channel.
* Vietnam market.
* VND and USD.
* Vietnamese and English.
* GPay.
* OnePay.
* Gigago.
* Customer Portal.
* Agency Portal.
* Commission.
* Operations and reconciliation.

R1.0 must include architecture readiness for:

* Laos market.
* LAK.
* Lao language.
* uMoney.

### R1.1 — Laos Activation

R1.1 activates:

* Lao localization.
* LAK production Price Book.
* uMoney payment.
* Laos payment reconciliation.
* Agency pilot in Laos.

---

## 3. Canonical ownership principles

| Information               | Canonical owner               |
| ------------------------- | ----------------------------- |
| Organization              | YSim Platform                 |
| Agency                    | YSim Platform                 |
| Product Offer             | YSim Platform                 |
| Supplier Plan Mapping     | YSim Platform                 |
| Price Book                | YSim Platform                 |
| Agency Offer              | YSim Platform                 |
| Reference QR              | YSim Platform                 |
| Checkout Session          | YSim Platform                 |
| Sales Order               | YSim Platform                 |
| Payment                   | YSim Platform                 |
| Procurement               | YSim Platform                 |
| Fulfillment               | YSim Platform                 |
| eSIM Asset                | YSim Platform                 |
| Delivery                  | YSim Platform                 |
| Commission                | YSim Platform                 |
| Refund                    | YSim Platform                 |
| Audit Event               | YSim Platform                 |
| Marketing content and SEO | WooCommerce during transition |
| Storefront presentation   | `ysim-storefront`             |

No bidirectional synchronization is allowed for Order, Payment, Fulfillment or Commission.

---

## 4. Capability domains

### 4.1. Identity and access

| ID     | Capability                 |     R1.0 |  R1.1 |
| ------ | -------------------------- | -------: | ----: |
| IAM-01 | User identity              | Required | Reuse |
| IAM-02 | Authentication             | Required | Reuse |
| IAM-03 | Role and permission        | Required | Reuse |
| IAM-04 | Organization context       | Required | Reuse |
| IAM-05 | Agency membership          | Required | Reuse |
| IAM-06 | Magic-link customer access | Required | Reuse |
| IAM-07 | Support access logging     | Required | Reuse |

Minimum roles:

* Platform Admin.
* Operations.
* Support.
* Finance Read-only.
* Agency Admin.
* Agency User.
* Customer magic-link principal.

### 4.2. Organization and agency

| ID     | Capability                 |     R1.0 |  R1.1 |
| ------ | -------------------------- | -------: | ----: |
| ORG-01 | Organization lifecycle     | Required | Reuse |
| ORG-02 | Agency profile             | Required | Reuse |
| ORG-03 | Agency status control      | Required | Reuse |
| ORG-04 | Agency-scoped data access  | Required | Reuse |
| ORG-05 | Agency product entitlement | Required | Reuse |
| ORG-06 | Agency reporting scope     | Required | Reuse |

Deferred:

* Sub-agency.
* Multi-level hierarchy.
* Agency wallet.
* Agency credit limit.
* Wholesale prepaid balance.

### 4.3. Catalog

| ID     | Capability                      |     R1.0 |   R1.1 |
| ------ | ------------------------------- | -------: | -----: |
| CAT-01 | Destination and region          | Required |  Reuse |
| CAT-02 | Canonical product               | Required |  Reuse |
| CAT-03 | Product Offer                   | Required |  Reuse |
| CAT-04 | Data and validity normalization | Required |  Reuse |
| CAT-05 | Activation policy               | Required |  Reuse |
| CAT-06 | Network and operator metadata   | Required |  Reuse |
| CAT-07 | Product localization            |    VI/EN | Add LO |
| CAT-08 | Storefront catalog API          | Required |  Reuse |
| CAT-09 | WooCommerce content reference   | Required |  Reuse |

### 4.4. Supplier management

| ID     | Capability                      |     R1.0 |  R1.1 |
| ------ | ------------------------------- | -------: | ----: |
| SUP-01 | Supplier registry               | Required | Reuse |
| SUP-02 | Supplier Plan                   | Required | Reuse |
| SUP-03 | Product-to-plan mapping         | Required | Reuse |
| SUP-04 | Supplier credential scope       | Required | Reuse |
| SUP-05 | Supplier Gateway contract       | Required | Reuse |
| SUP-06 | Gigago adapter                  | Required | Reuse |
| SUP-07 | Supplier health and diagnostics | Required | Reuse |

Architecture must support approximately six suppliers within twelve months.

Automatic supplier optimization and fallback are deferred.

### 4.5. Pricing

| ID     | Capability                |     R1.0 |     R1.1 |
| ------ | ------------------------- | -------: | -------: |
| PRI-01 | Price Book                | Required |    Reuse |
| PRI-02 | Market-specific pricing   |  Vietnam | Add Laos |
| PRI-03 | Currency-specific pricing |  VND/USD |  Add LAK |
| PRI-04 | Price effective period    | Required |    Reuse |
| PRI-05 | Immutable price snapshot  | Required |    Reuse |
| PRI-06 | Supplier cost snapshot    | Required |    Reuse |
| PRI-07 | Internal FX reference     | Optional | Optional |
| PRI-08 | Pricing quote             | Required |    Reuse |

Selling prices are approved values in each currency. Checkout prices are not calculated directly from real-time FX rates.

### 4.6. Agency offers and references

| ID     | Capability             |     R1.0 |  R1.1 |
| ------ | ---------------------- | -------: | ----: |
| AOF-01 | Agency Offer           | Required | Reuse |
| AOF-02 | Agency Offer Version   | Required | Reuse |
| AOF-03 | Product entitlement    | Required | Reuse |
| AOF-04 | Commission rule        | Required | Reuse |
| REF-01 | Reference Link         | Required | Reuse |
| REF-02 | Reference QR           | Required | Reuse |
| REF-03 | Signed reference token | Required | Reuse |
| REF-04 | Expiry and revocation  | Required | Reuse |
| REF-05 | Attribution snapshot   | Required | Reuse |

Agency cannot provide an arbitrary selling price in Release 1.

### 4.7. Checkout and order

| ID     | Capability                          |     R1.0 |  R1.1 |
| ------ | ----------------------------------- | -------: | ----: |
| CHK-01 | Guest checkout                      | Required | Reuse |
| CHK-02 | Checkout Session                    | Required | Reuse |
| CHK-03 | Market, locale and currency context | Required | Reuse |
| CHK-04 | Invoice information capture         | Required | Reuse |
| ORD-01 | Sales Order                         | Required | Reuse |
| ORD-02 | Order Item                          | Required | Reuse |
| ORD-03 | Immutable commercial snapshots      | Required | Reuse |
| ORD-04 | Derived overall status              | Required | Reuse |
| ORD-05 | Agency attribution                  | Required | Reuse |

Sales Order is created before payment with `PENDING_PAYMENT`.

### 4.8. Payment

| ID     | Capability                   |              R1.0 |     R1.1 |
| ------ | ---------------------------- | ----------------: | -------: |
| PAY-01 | Payment provider contract    |          Required |    Reuse |
| PAY-02 | Payment Intent               |          Required |    Reuse |
| PAY-03 | Payment Attempt              |          Required |    Reuse |
| PAY-04 | Signature verification       |          Required |    Reuse |
| PAY-05 | Idempotent webhook inbox     |          Required |    Reuse |
| PAY-06 | Payment expiration and retry |          Required |    Reuse |
| PAY-07 | GPay adapter                 |          Required |    Reuse |
| PAY-08 | OnePay adapter               |          Required |    Reuse |
| PAY-09 | uMoney adapter               | Architecture only | Required |
| PAY-10 | Payment reconciliation       |          Required |   Extend |
| PAY-11 | Full refund                  |          Required |   Extend |

Partial refund is deferred.

### 4.9. Procurement and fulfillment

| ID     | Capability                       |     R1.0 |  R1.1 |
| ------ | -------------------------------- | -------: | ----: |
| PRO-01 | Procurement validation           | Required | Reuse |
| PRO-02 | Supplier order                   | Required | Reuse |
| PRO-03 | Supplier request correlation     | Required | Reuse |
| PRO-04 | Polling and recovery             | Required | Reuse |
| FUL-01 | Fulfillment state machine        | Required | Reuse |
| FUL-02 | Duplicate fulfillment prevention | Required | Reuse |
| FUL-03 | eSIM Asset                       | Required | Reuse |
| FUL-04 | ICCID and activation data        | Required | Reuse |
| FUL-05 | Manual eSIM replacement          | Required | Reuse |
| FUL-06 | Supplier reconciliation          | Required | Reuse |

Payment success must never create more than one valid procurement for the same fulfillment attempt.

### 4.10. Delivery and customer experience

| ID     | Capability              |     R1.0 |   R1.1 |
| ------ | ----------------------- | -------: | -----: |
| DEL-01 | Email delivery          |    VI/EN | Add LO |
| DEL-02 | Delivery retry          | Required |  Reuse |
| DEL-03 | Customer Portal         | Required |  Reuse |
| DEL-04 | Secure QR display       | Required |  Reuse |
| DEL-05 | Activation-code display | Required |  Reuse |
| DEL-06 | Resend email            | Required |  Reuse |
| DEL-07 | Installation guide      |    VI/EN | Add LO |
| DEL-08 | Support request         | Required |  Reuse |

eSIM QR and activation data must not be stored in publicly accessible storage.

### 4.11. Commission

| ID     | Capability           |     R1.0 |  R1.1 |
| ------ | -------------------- | -------: | ----: |
| COM-01 | Commission rule      | Required | Reuse |
| COM-02 | Commission snapshot  | Required | Reuse |
| COM-03 | Commission ledger    | Required | Reuse |
| COM-04 | ATTRIBUTED state     | Required | Reuse |
| COM-05 | ACCRUED state        | Required | Reuse |
| COM-06 | ELIGIBLE state       | Required | Reuse |
| COM-07 | REVERSED state       | Required | Reuse |
| COM-08 | PAID state           | Required | Reuse |
| COM-09 | Commission statement | Required | Reuse |
| COM-10 | CSV export           | Required | Reuse |

Commission becomes eligible only after fulfillment succeeds.

### 4.12. Operations and support

| ID     | Capability                      |     R1.0 |   R1.1 |
| ------ | ------------------------------- | -------: | -----: |
| OPS-01 | Payment exception queue         | Required | Extend |
| OPS-02 | Supplier timeout queue          | Required |  Reuse |
| OPS-03 | Fulfillment failure queue       | Required |  Reuse |
| OPS-04 | Webhook failure queue           | Required | Extend |
| OPS-05 | Email failure queue             | Required |  Reuse |
| OPS-06 | Refund queue                    | Required | Extend |
| OPS-07 | Search and transaction timeline | Required |  Reuse |
| OPS-08 | Manual resolution               | Required |  Reuse |
| OPS-09 | Audit Event                     | Required |  Reuse |

Support may view full QR and activation code in Release 1, but every access must create an Audit Event.

### 4.13. Platform operations

| ID     | Capability                   |     R1.0 |   R1.1 |
| ------ | ---------------------------- | -------: | -----: |
| PLT-01 | PostgreSQL persistence       | Required |  Reuse |
| PLT-02 | Background worker and queue  | Required |  Reuse |
| PLT-03 | Transactional outbox         | Required |  Reuse |
| PLT-04 | Idempotency store            | Required |  Reuse |
| PLT-05 | Secret separation            | Required | Extend |
| PLT-06 | Sandbox/production isolation | Required | Extend |
| PLT-07 | Monitoring and alerting      | Required | Extend |
| PLT-08 | Backup and restore           | Required | Extend |
| PLT-09 | Six-month retention          | Required |  Reuse |
| PLT-10 | Correlation ID               | Required |  Reuse |

---

## 5. Deferred capabilities

The following capabilities are outside Release 1:

* Agency wallet.
* Agency credit or postpaid billing.
* Sub-agency and multi-level commissions.
* Supplier price optimization.
* Automatic supplier fallback.
* Advanced promotion engine.
* Partial refund.
* Top-up.
* Voice and SMS eSIM.
* Recommendation engine.
* Automated invoice issuance.
* Accounting integration.
* Partner Portal.
* Advanced white-label builder.

---

## 6. Capability acceptance

The capability map is accepted when:

1. Every capability has a canonical owner.
2. Every capability is assigned to R1.0, R1.1 or Deferred.
3. No required business flow depends on a Deferred capability.
4. Agency attribution is represented across pricing, checkout, order and commission.
5. Payment and fulfillment recovery are included.
6. Multi-language and multi-currency responsibilities are explicit.
7. Runtime implementation has not started within R1A-01.
