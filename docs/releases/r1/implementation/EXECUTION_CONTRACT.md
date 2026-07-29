# R1B-00 — Implementation Execution Contract

## 1. Purpose

This document defines how Release 1 executable slices are prepared, implemented, validated, tagged and accepted.

It prevents incomplete scaffolding, mixed candidates and validation that does not represent the committed software.

---

## 2. Unit of delivery

The unit of delivery is an executable vertical slice.

A slice must cross all layers required to produce a real outcome:

```text
Actor action
→ API or command contract
→ Application behavior
→ Domain state transition
→ Persistence
→ Projection or integration
→ Observable result
→ Automated evidence
→ Runtime evidence
```

The following are not completed slices by themselves:

- Database schema.
- DTO definitions.
- Adapter interface.
- UI mock.
- Health endpoint.
- Generated report.
- Candidate manifest without runtime evidence.

---

## 3. Package lifecycle

Every slice follows these states:

1. `PLANNED`
2. `IMPLEMENTING`
3. `VALIDATING`
4. `CANDIDATE`
5. `HUMAN_REVIEW`
6. `ACCEPTED` or `REJECTED`
7. `SUPERSEDED` when replaced

No automatic transition from Candidate to Accepted is allowed.

---

## 4. Branch and tag naming

Recommended branch:

```text
release/vs-r1-001-organization-agency-bootstrap
```

Candidate tags:

```text
candidate/vs-r1-001/v1
candidate/vs-r1-001/v2
```

Accepted tag:

```text
baseline/r1/vs-r1-001/accepted-v1
```

Accepted tags must point directly to the candidate commit:

```text
candidate/vs-r1-001/v1^{}
```

Rejected or superseded tags remain immutable historical evidence.

---

## 5. Candidate isolation

A candidate must contain only the files required by the slice contract.

Before validation:

- Working tree inventory is reviewed.
- Generated folders are excluded.
- Unrelated staged files are prohibited.
- Prior experiment artifacts are prohibited.
- Secret-like values are prohibited.
- Candidate base commit is recorded.
- Candidate tree hash is recorded.

Mixed staged, unstaged and unrelated untracked candidate state is prohibited.

---

## 6. Required slice specification

Before implementation, each slice defines:

- Slice ID and name.
- Business outcome.
- In-scope requirements.
- Out-of-scope items.
- Owning contexts.
- Actor and authorization rules.
- API and event contracts.
- Data model ownership.
- Migration and rollback strategy.
- Idempotency scope.
- Failure and recovery behavior.
- Security and privacy treatment.
- Automated test plan.
- Runtime evidence plan.
- Candidate inventory policy.
- Human acceptance steps.

---

## 7. Validation stages

### Stage 1 — Static integrity

- Candidate inventory.
- Secret scan.
- Formatting.
- Typecheck.
- Lint.
- Import and module-boundary checks.
- Contract compatibility.

### Stage 2 — Automated behavior

- Unit tests.
- Application tests.
- Integration tests.
- Negative authorization tests.
- Duplicate and concurrency tests.
- Migration and integrity tests when applicable.

### Stage 3 — Runtime proof

- Start real API or worker.
- Execute the accepted scenario.
- Verify persisted state.
- Verify emitted events and projections.
- Verify failure and recovery path.
- Capture sanitized evidence.
- Stop processes and clean temporary resources.

### Stage 4 — Clean checkout

- Create a fresh checkout from the candidate commit.
- Install from committed lockfile.
- Run required validation.
- Prove candidate tree identity.
- Prove cleanup.
- Preserve command results.

### Stage 5 — Human acceptance

- Reviewer reads implementation report.
- Reviewer executes or observes acceptance scenario.
- Reviewer checks evidence authenticity.
- Reviewer records Accepted or Rejected decision.
- No self-generated PASS result replaces human acceptance.

---

## 8. Automated repair policy

Automated implementation agents may attempt at most two repair iterations after a failed validation cycle unless a human explicitly authorizes more.

A repair iteration must:

- Preserve the original failure evidence.
- Record changed files.
- Explain the defect classification.
- Rerun the full affected validation set.
- Not weaken acceptance criteria.

After the retry limit, the package becomes blocked for human review.

---

## 9. Database-change contract

A slice with schema changes must provide:

- Forward migration.
- Ownership for every table.
- Deterministic test fixtures.
- Migration verification against a real PostgreSQL instance.
- Integrity tests.
- Cleanup proof.
- Rollback or forward-fix plan.
- Data compatibility statement.
- No production secret in migration or fixture.

Generated ORM files are not accepted as the only database evidence.

---

## 10. External-provider contract

A slice integrating a provider must prove:

- Adapter boundary.
- Signature or authentication handling.
- Timeout and retry behavior.
- Idempotency identity.
- Unknown-outcome handling.
- Raw-event inbox persistence.
- Reconciliation path.
- Sandbox evidence.
- Production contract probe plan.
- Secret isolation.

Sandbox behavior must not be generalized to production without confirmation.

---

## 11. Security contract

Every slice must evaluate:

- Organization scope.
- Authentication and authorization.
- Sensitive-data exposure.
- Logging and error content.
- Secret handling.
- Audit requirements.
- Abuse and replay behavior.
- Data retention.
- Public API input trust.

A critical security defect blocks candidate creation.

---

## 12. Acceptance authority

The Authorized Approver records the final human decision.

The approval record includes:

- Candidate tag.
- Candidate commit.
- Candidate tree.
- Evidence run ID.
- Decision.
- Approver name.
- Timestamp.
- Conditions or follow-up actions.

A Markdown signature is sufficient for Release 1 governance.

---

## 13. Rejection and supersession

A rejected candidate is not deleted or retagged.

A corrected candidate receives a new version.

Accepted history is never rewritten to conceal a defect.

If a baseline is superseded:

- The new baseline references the prior baseline.
- Migration and compatibility impact are recorded.
- Old tags remain available.

---

## 14. Execution-contract acceptance

The contract is accepted when:

1. Candidate isolation is mandatory.
2. Clean checkout is mandatory.
3. Runtime proof is mandatory.
4. Human acceptance is mandatory.
5. Repair limits are explicit.
6. Database and provider rules are explicit.
7. Rejected history remains immutable.
8. R1B-00 does not implement runtime functionality.
