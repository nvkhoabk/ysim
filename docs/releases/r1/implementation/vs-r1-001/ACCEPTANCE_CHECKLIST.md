# VS-R1-001 Acceptance Checklist

## A. Baseline

- [ ] Branch was created from `baseline/r1/r1b-00/accepted-v1`.
- [ ] Branch name is `release/vs-r1-001-organization-agency-bootstrap`.
- [ ] R1B-00 accepted baseline remains unchanged.
- [ ] VS001 recovery worktree remains unchanged.
- [ ] Runtime versions match the accepted baseline.
- [ ] No secret or real credential is included.

## B. Contracts

- [ ] Organization types are defined.
- [ ] Organization states are defined.
- [ ] Membership roles are defined.
- [ ] Membership states are defined.
- [ ] Create Agency contract is defined.
- [ ] Grant Membership contract is defined.
- [ ] Organization Context contract is defined.
- [ ] Contract exports build successfully.

## C. Database

- [ ] Migration creates the `organization_agency` schema.
- [ ] Organization table is owned by ORG.
- [ ] Agency profile table is owned by ORG.
- [ ] Membership table is owned by ORG.
- [ ] Activity table is append-only by application contract.
- [ ] Organization code is unique.
- [ ] Agency code is unique.
- [ ] Active membership uniqueness is enforced.
- [ ] YSim platform organization is inserted deterministically.
- [ ] Migration runs on real PostgreSQL.
- [ ] Database resources are cleaned after validation.

## D. API and domain behavior

- [ ] Agency creation requires bootstrap authorization.
- [ ] New agency starts in `DRAFT`.
- [ ] Agency activation is supported.
- [ ] Membership grant is supported.
- [ ] Active context resolution is supported.
- [ ] Draft organization context is denied.
- [ ] Cross-agency context is denied.
- [ ] Duplicate organization code returns conflict.
- [ ] Organization activity is recorded.
- [ ] SQL uses parameterized queries.
- [ ] No provider-specific code is introduced.

## E. Automated evidence

- [ ] Policy unit tests pass.
- [ ] Contracts typecheck.
- [ ] API typecheck.
- [ ] API build passes.
- [ ] Runtime proof passes.
- [ ] Duplicate behavior is tested.
- [ ] Cross-agency denial is tested.
- [ ] Persisted state is verified.
- [ ] Process and Docker cleanup are verified.

## F. Scope integrity

- [ ] No Catalog module is introduced.
- [ ] No Pricing module is introduced.
- [ ] No Payment module is introduced.
- [ ] No Fulfillment module is introduced.
- [ ] No public identity trust boundary is claimed.
- [ ] No Agency Portal UI is introduced.
- [ ] No prior VS001 artifact is merged.

## G. Candidate inventory

The committed candidate is expected to contain only the documented VS-R1-001 implementation, contracts, migration, tests, scripts, package manifests and lockfile.

- [ ] `pnpm-lock.yaml` is updated by pnpm.
- [ ] No `Zone.Identifier` file exists.
- [ ] Tracked `.gitignore` excludes `node_modules`, `dist`, `.next`, coverage and test-report outputs.
- [ ] No generated `node_modules`, `dist`, `.next`, coverage or test-report directory is staged.
- [ ] `git diff --check` succeeds.
- [ ] Candidate contains exactly 24 approved paths from the R1B-00 baseline.
- [ ] Candidate tag is created.
- [ ] Clean-checkout evidence is produced.

## Acceptance result

```text
VS-R1-001_RESULT=PENDING
```

After human approval:

```text
VS-R1-001_RESULT=PASS
```
