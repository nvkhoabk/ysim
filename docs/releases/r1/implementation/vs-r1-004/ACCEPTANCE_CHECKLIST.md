# VS-R1-004 Acceptance Checklist

## A. Baseline

- [ ] Branch was created from `baseline/r1/vs-r1-003/accepted-v1`.
- [ ] Branch name is `release/vs-r1-004-gigago-plan-mapping`.
- [ ] VS-R1-003 accepted baseline remains unchanged.
- [ ] Source repository is clean before candidate validation.
- [ ] No secret or real API credential is included.
- [ ] No prior Storefront fulfillment implementation is copied into Platform.

## B. Supplier environments

- [ ] Gigago Supplier is seeded once.
- [ ] Sandbox base URL is explicit.
- [ ] Production base URL is explicit.
- [ ] Credentials use `env://` references only.
- [ ] `getPackages` method is stored per environment.
- [ ] Sandbox order-query method records confirmed `POST`.
- [ ] Production order-query method remains unconfirmed.
- [ ] Production environment status is `DOCUMENTED_UNVERIFIED`.

## C. Supplier Plan

- [ ] Documented Gigago plan fields are represented.
- [ ] Fixed data is normalized.
- [ ] Daily data is normalized.
- [ ] Unlimited data is normalized.
- [ ] Validity is normalized to days.
- [ ] Countries are normalized to ISO Alpha-2 codes.
- [ ] Operators are normalized.
- [ ] Capability flags are normalized.
- [ ] Raw snapshot hash is deterministic.
- [ ] Environment plus external plan ID is unique.
- [ ] `GIGA-DEMO` fixture is accepted as a zero-data supplier plan.

## D. Mapping policy

- [ ] Canonical offer is queried through a read-only adapter.
- [ ] No cross-context Catalog write occurs.
- [ ] No cross-context Catalog foreign key is created.
- [ ] Unpublished offer is rejected.
- [ ] Duration mismatch is rejected.
- [ ] Data-policy mismatch is rejected.
- [ ] Allowance mismatch is rejected.
- [ ] Missing destination is rejected.
- [ ] Missing hotspot capability is rejected.
- [ ] Missing phone-number capability is rejected.
- [ ] Extra supplier destinations produce a warning.
- [ ] Activation and network verification warnings are retained.

## E. Mapping lifecycle

- [ ] Compatible mapping is created as `DRAFT`.
- [ ] Sandbox mapping can become `ACTIVE`.
- [ ] Duplicate mapping is rejected.
- [ ] Only one active Gigago mapping exists per Product Offer and environment.
- [ ] Production activation is blocked until production probing.
- [ ] Mapping activity is recorded.

## F. Runtime evidence

- [ ] Real PostgreSQL is used.
- [ ] Real API process is used.
- [ ] Canonical Catalog data is created through API contracts.
- [ ] Documented `GIGA-DEMO` is replayed.
- [ ] Incompatible mapping returns HTTP 422.
- [ ] Compatible sandbox mapping activates.
- [ ] Production activation returns a controlled conflict.
- [ ] Database persistence is independently verified.
- [ ] API process and Docker resources are cleaned.
- [ ] No live Gigago call occurs.

## G. Scope integrity

- [ ] No Procurement aggregate is introduced.
- [ ] No Supplier Order is created.
- [ ] No eSIM or QR data is handled.
- [ ] No webhook endpoint is introduced.
- [ ] No canonical selling price is introduced.
- [ ] No automatic supplier fallback is introduced.
- [ ] Storefront repository remains outside this candidate.

## H. Candidate inventory

- [ ] Candidate contains exactly 22 approved paths.
- [ ] Catalog migration remains unchanged.
- [ ] Supplier migration is included.
- [ ] Supplier contracts are included.
- [ ] Fixture JSON is included.
- [ ] `pnpm-lock.yaml` remains unchanged.
- [ ] `git diff --check` succeeds.
- [ ] No generated or Windows metadata path is staged.
- [ ] Working tree is clean after commit.
- [ ] Candidate tag is created.

## Acceptance result

```text
VS-R1-004_RESULT=PENDING
```

After human approval:

```text
VS-R1-004_RESULT=PASS
```
