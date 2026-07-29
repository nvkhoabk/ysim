# R1A-04 — Release 1 Dependency Graph

## 1. Purpose

This document records implementation dependencies, allowed parallel lanes and external blockers for Release 1.

---

## 2. Critical path

```text
VS-R1-001 Organization and Agency Bootstrap
  ↓
VS-R1-003 Canonical Product Offer
  ↓
VS-R1-004 Gigago Supplier Mapping
  ↓
VS-R1-005 Storefront Catalog API
  ↓
VS-R1-006 Price Book and Pricing Quote
  ↓
VS-R1-007 Agency Offer and Commission Rule
  ↓
VS-R1-008 Signed Reference QR
  ↓
VS-R1-009 Guest Checkout and Sales Order
  ↓
VS-R1-010 Payment Provider Core
  ├──→ VS-R1-011 GPay
  └──→ VS-R1-012 OnePay
            ↓
VS-R1-013 Gigago Procurement
  ↓
VS-R1-014 Secure eSIM Fulfillment
  ├──→ VS-R1-015 Email Delivery
  ├──→ VS-R1-016 Customer Portal
  └──→ VS-R1-018 Commission Ledger
            ↓
VS-R1-019 Operations and Reconciliation
  ↓
VS-R1-020 Production Hardening and Pilot
```

---

## 3. Dependency matrix

| Slice | Must wait for | May run in parallel with |
|---|---|---|
| VS-R1-001 | Architecture baseline | None |
| VS-R1-002 | VS-R1-001 | VS-R1-003 |
| VS-R1-003 | VS-R1-001 | VS-R1-002 |
| VS-R1-004 | VS-R1-003 | VS-R1-006 design |
| VS-R1-005 | VS-R1-003, VS-R1-004 | Agency Portal shell |
| VS-R1-006 | VS-R1-003 | VS-R1-004 |
| VS-R1-007 | VS-R1-001, VS-R1-006 | VS-R1-005 |
| VS-R1-008 | VS-R1-007 | Storefront integration preparation |
| VS-R1-009 | VS-R1-005, VS-R1-006, VS-R1-008 | Payment core design |
| VS-R1-010 | VS-R1-009 contract | Operations read-model design |
| VS-R1-011 | VS-R1-010 | VS-R1-012 |
| VS-R1-012 | VS-R1-010 | VS-R1-011 |
| VS-R1-012A | At least one provider adapter | Procurement development |
| VS-R1-013 | VS-R1-004 and payment success contract | Delivery template work |
| VS-R1-014 | VS-R1-013 | Customer Portal shell |
| VS-R1-015 | VS-R1-014 | VS-R1-018 |
| VS-R1-016 | VS-R1-014, VS-R1-015 contract | VS-R1-017 |
| VS-R1-017 | VS-R1-002, VS-R1-009 | Payment and fulfillment |
| VS-R1-018 | VS-R1-007, payment events, VS-R1-014 | VS-R1-015, VS-R1-017 |
| VS-R1-019 | Accepted operational events from core contexts | Portal completion |
| VS-R1-020 | All required R1.0 slices | R1.1 preparation |
| VS-R1L-001 | Catalog, pricing and UI foundations | Late R1.0 hardening |
| VS-R1L-002 | VS-R1-010 and uMoney readiness | Late R1.0 hardening |
| VS-R1L-003 | VS-R1L-001, VS-R1L-002, VS-R1-020 | None |

---

## 4. Delivery lanes

### Foundation lane

- VS-R1-001.
- VS-R1-002.
- Shared authorization and audit.
- Platform module boundaries.

### Commerce lane

- VS-R1-003.
- VS-R1-005.
- VS-R1-006.
- VS-R1-007.
- VS-R1-008.
- VS-R1-009.

### Payment lane

- VS-R1-010.
- VS-R1-011.
- VS-R1-012.
- VS-R1-012A.

### Fulfillment lane

- VS-R1-004.
- VS-R1-013.
- VS-R1-014.
- VS-R1-015.
- VS-R1-016.

### Agency lane

- VS-R1-002.
- VS-R1-007.
- VS-R1-008.
- VS-R1-017.
- VS-R1-018.

### Operations lane

- Cross-context projections.
- VS-R1-019.
- VS-R1-020.

Parallel work must not bypass acceptance of shared contracts.

---

## 5. External dependency register

| ID | Dependency | Required for | Risk | Mitigation |
|---|---|---|---|---|
| EXT-01 | GPay production credential and certificate | VS-R1-011, VS-R1-020 | Medium | Complete sandbox evidence early; prepare production checklist |
| EXT-02 | OnePay sandbox and production contract | VS-R1-012, VS-R1-020 | Medium | Reuse Storefront lessons; preserve adapter boundary |
| EXT-03 | Gigago production contract confirmation | VS-R1-013, VS-R1-020 | High | Probe production method and payload before activation |
| EXT-04 | Gigago stock and processing behavior | VS-R1-013 | High | Polling, recovery and Operations queue |
| EXT-05 | Transactional email provider | VS-R1-015 | Medium | Provider adapter and retry queue |
| EXT-06 | uMoney documentation and credentials | VS-R1L-002 | High | Keep R1.0 releasable without uMoney activation |
| EXT-07 | Lao-language business review | VS-R1L-001, VS-R1L-003 | Medium | Early translation review and UAT |
| EXT-08 | Two pilot agencies | VS-R1-020 | Medium | Agree agency profile, commission and UAT schedule early |
| EXT-09 | Production domain, HTTPS and webhook routing | VS-R1-020 | High | Validate infrastructure before provider production probes |
| EXT-10 | Secrets and encryption-key operations | VS-R1-014, VS-R1-020 | High | Establish environment-specific secret runbook |

---

## 6. Blocking rules

A slice is blocked when:

- Required upstream contract is not accepted.
- Required provider documentation or credential is unavailable.
- Organization or authorization model is unresolved.
- Candidate would introduce a second canonical owner.
- Required idempotency identity is unknown.
- Production contract is assumed from sandbox without confirmation.
- Sensitive-data storage lacks an approved security design.
- Runtime evidence cannot be produced.

Blocked work must record:

- Blocking dependency.
- Owner.
- Date identified.
- Next review date.
- Safe parallel work.
- Release impact.

---

## 7. Change control

Changing a dependency requires:

1. Impact analysis on the critical path.
2. Domain-owner review.
3. API, event and migration impact review.
4. Updated milestone forecast.
5. Approval before implementation starts under the new order.
