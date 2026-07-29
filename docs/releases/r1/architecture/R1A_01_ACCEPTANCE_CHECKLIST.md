# R1A-01 Acceptance Checklist

## A. Baseline

* [ ] Branch was created from `baseline/r1/r1d-01/accepted-v1`.
* [ ] Branch name is `release/r1a-01-capability-map`.
* [ ] R1D-01 accepted baseline remains unchanged.
* [ ] VS001 recovery worktree remains unchanged.
* [ ] No database files are modified.
* [ ] No runtime files are modified.
* [ ] No credential or secret is included.

## B. Capability map

* [ ] Identity and access capabilities are defined.
* [ ] Organization and Agency capabilities are defined.
* [ ] Catalog capabilities are defined.
* [ ] Supplier capabilities are defined.
* [ ] Pricing capabilities are defined.
* [ ] Agency Offer and Reference QR capabilities are defined.
* [ ] Checkout and Order capabilities are defined.
* [ ] Payment capabilities are defined.
* [ ] Procurement and Fulfillment capabilities are defined.
* [ ] Delivery and Customer Portal capabilities are defined.
* [ ] Commission capabilities are defined.
* [ ] Operations capabilities are defined.
* [ ] Platform-operation capabilities are defined.
* [ ] R1.0 and R1.1 responsibilities are separated.
* [ ] Deferred capabilities are explicit.

## C. Vertical slice plan

* [ ] Critical path is defined.
* [ ] Organization and Agency foundation comes before Agency Portal.
* [ ] Product Offer comes before pricing and checkout.
* [ ] Agency Offer comes before Reference QR.
* [ ] Reference QR comes before attributed checkout.
* [ ] Sales Order is created before payment.
* [ ] Payment provider core comes before provider adapters.
* [ ] Payment success comes before procurement.
* [ ] Procurement comes before eSIM fulfillment.
* [ ] Fulfillment comes before delivery and commission eligibility.
* [ ] Operations recovery is included.
* [ ] R1.1 Laos slices are defined.
* [ ] Each slice has an executable result.
* [ ] Each slice has dependencies.
* [ ] Definition of Done is defined.

## D. Scope integrity

* [ ] Agency wallet remains deferred.
* [ ] Credit limit remains deferred.
* [ ] Sub-agency remains deferred.
* [ ] Automatic supplier fallback remains deferred.
* [ ] Partial refund remains deferred.
* [ ] Voice, SMS and top-up remain deferred.
* [ ] OnePay remains in R1.0.
* [ ] GPay remains in R1.0.
* [ ] uMoney activation remains in R1.1.
* [ ] Gigago remains the first supplier runtime.
* [ ] Architecture remains multi-supplier ready.

## E. Candidate validation

The candidate must contain only:

```text
docs/releases/r1/INDEX.md
docs/releases/r1/architecture/INDEX.md
docs/releases/r1/architecture/CAPABILITY_MAP.md
docs/releases/r1/architecture/VERTICAL_SLICE_PLAN.md
docs/releases/r1/architecture/R1A_01_ACCEPTANCE_CHECKLIST.md
```

Validation:

* [ ] Candidate contains exactly five files.
* [ ] `git diff --cached --check` succeeds.
* [ ] All required files exist and are non-empty.
* [ ] Architecture Index links all R1A-01 documents.
* [ ] Release 1 Index links Architecture Index.
* [ ] No runtime, database, package or artifact path is staged.
* [ ] Working tree is clean after commit.
* [ ] Candidate tag is created.

## Acceptance result

```text
R1A-01_RESULT=PENDING
```

After approval:

```text
R1A-01_RESULT=PASS
```
