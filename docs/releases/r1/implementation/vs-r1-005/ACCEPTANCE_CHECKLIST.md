# VS-R1-005 Acceptance Checklist

## A. Baseline

- [ ] Branch was created from `baseline/r1/vs-r1-004/accepted-v1`.
- [ ] Branch name is `release/vs-r1-005-storefront-catalog-api`.
- [ ] VS-R1-004 accepted baseline remains unchanged.
- [ ] Working tree contains only VS-R1-005 paths.
- [ ] No secret or real provider credential is included.

## B. Public API

- [ ] Public routes require no bootstrap token.
- [ ] Destination listing is implemented.
- [ ] Offer listing by Destination is implemented.
- [ ] Offer detail by stable code is implemented.
- [ ] Explicit locale query is supported.
- [ ] `Accept-Language` is supported.
- [ ] Unsupported explicit locale is rejected.
- [ ] Unknown or unavailable offer returns `404`.
- [ ] Cache-Control header is present.
- [ ] Vary header is present.

## C. Availability

- [ ] Only `PUBLISHED` Product Offers are visible.
- [ ] Active Supplier Plan Mapping is required.
- [ ] Active Supplier Plan is required.
- [ ] Supplier Environment must match explicit configuration.
- [ ] Supplier Environment contract must be `PROBED`.
- [ ] Active Destination and Region are required.
- [ ] Unmapped offer is excluded.
- [ ] Suspended offer is excluded.

## D. Public response safety

- [ ] Internal UUIDs are absent.
- [ ] Supplier code is absent.
- [ ] Supplier Plan and Mapping IDs are absent.
- [ ] External Supplier Plan ID is absent.
- [ ] Supplier cost is absent.
- [ ] Selling price is absent.
- [ ] Credential reference is absent.
- [ ] Raw supplier payload is absent.
- [ ] API key is absent.

## E. Localization

- [ ] English response is supported.
- [ ] Vietnamese response is supported.
- [ ] Lao response is supported when localization exists.
- [ ] Missing Lao localization falls back to English.
- [ ] Response identifies requested and source locale.

## F. Tests and runtime

- [ ] Policy tests pass.
- [ ] All earlier slice tests remain passing.
- [ ] Typecheck passes.
- [ ] Build passes.
- [ ] PostgreSQL/API runtime proof passes.
- [ ] Cache headers are runtime-tested.
- [ ] Public-field leakage is runtime-tested.
- [ ] Cleanup is verified.

## G. Candidate inventory

- [ ] Candidate contains exactly 17 approved paths.
- [ ] `pnpm-lock.yaml` is unchanged.
- [ ] No database migration is added.
- [ ] No Storefront repository file is changed.
- [ ] No generated or metadata path is staged.
- [ ] `git diff --check` succeeds.
- [ ] Candidate tag is created.

## Acceptance result

```text
VS-R1-005_RESULT=PENDING
```

After human approval:

```text
VS-R1-005_RESULT=PASS
```
