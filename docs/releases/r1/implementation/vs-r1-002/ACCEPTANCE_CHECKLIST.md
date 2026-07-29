# VS-R1-002 Acceptance Checklist

## A. Baseline

- [ ] Branch was created from `baseline/r1/vs-r1-001/accepted-v1`.
- [ ] Branch name is `release/vs-r1-002-agency-portal-shell`.
- [ ] VS-R1-001 accepted baseline remains unchanged.
- [ ] Runtime versions match the accepted baseline.
- [ ] No secret or real credential is included.

## B. API context

- [ ] Portal context endpoint is internal.
- [ ] Agency roles are required.
- [ ] Active membership is required.
- [ ] Draft organization returns inactive state.
- [ ] Suspended organization returns inactive state.
- [ ] Cross-agency access is denied.
- [ ] Suspend operation records organization activity.
- [ ] Existing VS-R1-001 context behavior remains valid.

## C. Session security

- [ ] Session cookie is HMAC signed.
- [ ] Signature comparison is timing-safe.
- [ ] Session expiry is enforced.
- [ ] Modified token is rejected.
- [ ] Secret minimum length is enforced.
- [ ] Bootstrap token remains server-only.
- [ ] Organization context is re-authorized by the API.

## D. Portal shell

- [ ] Unauthenticated state is rendered.
- [ ] Denied state is rendered.
- [ ] Draft state is rendered.
- [ ] Suspended state is rendered.
- [ ] Unavailable state is rendered.
- [ ] Ready shell is rendered.
- [ ] Organization name and code are displayed.
- [ ] Role and market are displayed.
- [ ] Agency Admin sees Team navigation.
- [ ] Agency User does not see Team navigation.
- [ ] Empty dashboard contains no fabricated business data.
- [ ] Layout is responsive.
- [ ] Vietnamese and English copy are available.

## E. Automated evidence

- [ ] VS-R1-001 unit tests remain green.
- [ ] Session unit tests pass.
- [ ] Navigation unit tests pass.
- [ ] Contracts build.
- [ ] API typecheck and build pass.
- [ ] Web typecheck and production build pass.
- [ ] Chromium browser is installed.
- [ ] Browser runtime proof passes.
- [ ] PostgreSQL state is verified.
- [ ] Processes and Docker resources are cleaned.

## F. Scope integrity

- [ ] No revenue implementation is introduced.
- [ ] No order-list implementation is introduced.
- [ ] No commission implementation is introduced.
- [ ] No Reference QR implementation is introduced.
- [ ] No public login endpoint is introduced.
- [ ] No provider integration is introduced.
- [ ] No database migration is introduced.
- [ ] No prior experiment artifact is merged.

## G. Candidate integrity

- [ ] Candidate contains exactly 26 approved VS-R1-002 paths.
- [ ] No `Zone.Identifier` exists.
- [ ] `apps/web/package.json` and `pnpm-lock.yaml` remain unchanged from the accepted baseline.
- [ ] No generated dependency or build directory is tracked.
- [ ] `git diff --check` succeeds.
- [ ] Candidate validator passes.
- [ ] Clean-checkout validator passes.
- [ ] Human acceptance is recorded.

## Acceptance result

```text
VS-R1-002_RESULT=PENDING
```

After human approval:

```text
VS-R1-002_RESULT=PASS
```
