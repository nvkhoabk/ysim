# R1A-04 — Release 1 Delivery Milestones

## 1. Purpose

This document defines planning milestones, exit criteria and indicative timing for Release 1.

The dates are relative to implementation start and must be reforecast when team capacity or external-provider readiness changes.

---

## 2. Assumptions

Primary forecast assumes:

- Four to six active contributors.
- One technical lead.
- Backend, frontend and QA/automation capacity.
- Product and Operations participation.
- DevOps support during integration and pilot.
- OnePay reference implementation becomes available early.
- Gigago sandbox remains available.
- R1.0 may launch before uMoney if Laos activation is blocked.

---

## 3. Milestone plan

### M0 — Architecture and Planning Accepted

Target:

- Week 0.

Includes:

- R1D-01.
- R1A-01.
- R1A-02.
- R1A-03.
- R1A-04.

Exit criteria:

- Release scope accepted.
- Domain ownership accepted.
- ADRs accepted.
- Ordered backlog and critical path accepted.
- Initial owners assigned.
- External dependencies registered.

### M1 — Organization and Agency Foundation

Target:

- End of Week 2.

Includes:

- VS-R1-001.
- VS-R1-002.

Exit criteria:

- YSim and pilot agency organizations exist.
- Agency users authenticate.
- Cross-agency access tests pass.
- Agency Portal shell is available.
- Organization actions are audited.

### M2 — Catalog, Supplier Mapping and Pricing

Target:

- End of Week 5.

Includes:

- VS-R1-003.
- VS-R1-004.
- VS-R1-005.
- VS-R1-006.

Exit criteria:

- Canonical Product Offer is operational.
- Gigago plan mapping is validated.
- Storefront consumes YSim catalog API.
- VND and USD Pricing Quotes are issued.
- WooCommerce is not canonical for commercial state.

### M3 — Agency Commerce and Checkout

Target:

- End of Week 7.

Includes:

- VS-R1-007.
- VS-R1-008.
- VS-R1-009.

Exit criteria:

- Agency Offer Version is immutable.
- Reference QR is signed, revocable and tamper-resistant.
- B2C and agency checkout create Sales Orders.
- Commercial and attribution snapshots are stored.

### M4 — Payment Ready

Target:

- End of Week 10.

Includes:

- VS-R1-010.
- VS-R1-011.
- VS-R1-012.
- Initial VS-R1-012A foundation.

Exit criteria:

- Payment provider core is accepted.
- GPay sandbox end-to-end passes.
- OnePay sandbox end-to-end passes.
- Duplicate callbacks/webhooks are safe.
- Reconciliation cases are observable.
- Production activation checklists exist.

### M5 — Automated Fulfillment Ready

Target:

- End of Week 13.

Includes:

- VS-R1-013.
- VS-R1-014.

Exit criteria:

- Payment success creates one Gigago procurement.
- Processing orders recover through polling.
- Secure eSIM Asset is created.
- Duplicate assignment is prevented.
- Support view and replacement are audited.

### M6 — Customer and Agency Experience Ready

Target:

- End of Week 15.

Includes:

- VS-R1-015.
- VS-R1-016.
- VS-R1-017.
- VS-R1-018.

Exit criteria:

- Email delivery and retry work.
- Customer Portal retrieves eSIM securely.
- Agency sees attributed orders and revenue.
- Commission lifecycle works through eligibility and reversal.
- CSV reporting is available.

### M7 — Operational Readiness

Target:

- End of Week 17.

Includes:

- VS-R1-019.
- Full refund operational completion.
- Monitoring and runbook preparation.

Exit criteria:

- Operations queues cover major failure types.
- Transaction timeline traces Reference QR through commission.
- Main failures are resolved without direct database edits.
- Refund and commission reversal are proven.
- Alerts and dashboards are available.

### M8 — Internal Pilot

Target:

- End of Week 18.

Includes:

- Initial VS-R1-020.

Exit criteria:

- Production-like environment is deployed.
- Secrets, databases and webhook URLs are isolated.
- Backup and restore test passes.
- Internal transactions complete end-to-end.
- Load test reaches 20 orders per minute without duplication.
- Rollback procedure is tested.

### M9 — Two-Agency Pilot

Target:

- Weeks 19–20.

Exit criteria:

- Two pilot agencies are onboarded.
- Agency QR and reporting work with real operational users.
- Payment-to-eSIM delivery SLA is measured.
- Incident and support process are exercised.
- Go/no-go review approves expanded pilot.

### M10 — Expanded R1.0 Pilot

Target:

- After Week 20, based on M9 evidence.

Exit criteria:

- Stable fulfillment success rate.
- Acceptable payment-to-delivery duration.
- Manual intervention rate within agreed threshold.
- No unresolved critical security or financial defect.
- Controlled expansion toward approximately 20 agencies.

### M11 — Laos Activation

Target:

- Three to five weeks after uMoney dependency readiness.
- May overlap with late R1.0 work.

Includes:

- VS-R1L-001.
- VS-R1L-002.
- VS-R1L-003.

Exit criteria:

- Lao localization passes review.
- LAK Price Book is active.
- uMoney payment and reconciliation pass.
- Laos Operations runbook is accepted.
- First Laos agency pilot is authorized.

---

## 4. Evidence required at every milestone

Every milestone review includes:

- Accepted candidate and baseline tags.
- Requirement and decision mapping.
- Automated-test results.
- Runtime evidence.
- Negative and duplicate-event evidence.
- Security and organization-scope evidence.
- Open defect list.
- External-dependency status.
- Updated forecast.
- Human acceptance result.

---

## 5. Forecast ranges

| Delivery model | R1.0 estimate | R1.1 additional estimate |
|---|---:|---:|
| Team of 4–6 | 16–20 weeks | 3–5 weeks |
| One primary developer with Codex support | 24–30 weeks | 4–6 weeks |

The estimate does not include uncontrolled delays from provider contracts, production credentials or external approvals.

---

## 6. Reforecast triggers

The release must be reforecast when:

- Team capacity changes by more than 20%.
- Provider credentials are delayed by more than one week.
- Production contract differs materially from sandbox.
- Product or agency scope increases.
- A critical security architecture decision changes.
- Data migration from previous MVP becomes larger than planned.
- Load or reliability testing reveals architectural remediation.
- uMoney becomes a mandatory R1.0 release gate.

---

## 7. Pilot success measures

The pilot must measure:

- Payment success rate.
- Fulfillment success rate.
- Payment-success-to-eSIM-delivery time.
- Email delivery success rate.
- Manual-intervention rate.
- Duplicate-event prevention.
- Revenue by market, currency and channel.
- Agency-attributed revenue.
- Eligible and reversed commission.
- Supplier processing duration.
- Operations case volume and resolution time.

Target thresholds are finalized before M8 Internal Pilot using sandbox evidence.
