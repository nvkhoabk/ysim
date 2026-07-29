# R1B-00 — Implementation Baseline

## 1. Purpose

This document defines the source, environment, branch, runtime and repository baseline from which Release 1 business implementation begins.

R1B-00 does not implement business functionality. It establishes the controlled starting point for `VS-R1-001 — Organization and Agency Bootstrap`.

---

## 2. Source baseline

Release 1 implementation begins from:

```text
baseline/r1/r1a-04/accepted-v1
```

The accepted baseline must resolve to the same commit as the accepted R1A-04 candidate.

No uncommitted work from prior VS001 experiments may be mixed into the Release 1 implementation worktree.

The existing VS001 recovery worktree remains preserved separately until an explicit disposition decision is approved.

---

## 3. Repository and worktree policy

Primary repository:

```text
/root/projects/ysim-v2.1/ysim
```

Release 1 implementation work must use a dedicated branch and clean worktree.

Rules:

- One active implementation package per branch.
- No unrelated staged or unstaged files.
- No generated dependency folders in candidate inventory.
- No `Zone.Identifier` metadata.
- No backup, temporary or editor-swap files.
- No secrets or credentials.
- No direct implementation on accepted baseline tags.
- No force-push of accepted baseline tags.

Before creating a candidate:

```text
git status --short
```

must be empty except for the exact package inventory that is intentionally staged.

---

## 4. Runtime identity

The implementation uses the runtime identities already pinned by the repository.

The source of truth is:

- `.node-version`
- package-manager configuration
- `package.json`
- `pnpm-lock.yaml`
- commissioning version audit
- container and orchestration configuration

At the current baseline, the expected local identities are:

- Node.js `24.18.0`
- pnpm `11.13.1`

The implementation package must not silently relax or change pinned versions.

A version change requires:

1. A dedicated architecture or platform decision.
2. Lockfile and compatibility review.
3. Clean-checkout validation.
4. Explicit migration impact.
5. Human acceptance.

---

## 5. Environment model

Required logical environments:

- Local Development.
- Sandbox / Staging.
- Production.

Sandbox and production must use separate:

- PostgreSQL databases.
- Redis or queue namespaces when introduced.
- Provider credentials.
- Certificate and signing material.
- Webhook URLs.
- Encryption keys.
- eSIM secure-storage namespaces.
- Logs and monitoring destinations.
- Cache namespaces.
- Object-storage buckets or prefixes when introduced.

Production secrets must never be used in local or sandbox environments.

---

## 6. Application processes

Release 1 may run multiple process types from one modular-monolith codebase:

- API process.
- Background worker process.
- Migration and maintenance commands.
- Validation and evidence commands.

These processes share one release version but do not bypass bounded-context ownership.

The API process must not perform unbounded background recovery work inline with user requests.

---

## 7. Persistence baseline

Release 1 uses PostgreSQL through the repository's approved database and migration toolchain.

Rules:

- Every new table has one owning bounded context.
- Every migration identifies the owning context.
- Cross-context foreign keys are prohibited by default.
- Commercial history is not removed through cascade deletion.
- Schema changes require migration evidence.
- Seed data is deterministic and environment-safe.
- Production credentials are never embedded in migrations or fixtures.
- Rollback or forward-fix strategy is documented for every migration package.

R1B-00 itself does not add or change database schema.

---

## 8. Clean-checkout baseline

Every executable slice must be validated in a fresh detached or temporary checkout created from the candidate commit.

Clean-checkout validation must prove:

- Dependency installation from the committed lockfile.
- Typecheck.
- Lint and boundary checks applicable to the slice.
- Automated tests.
- Build.
- Database migration and integrity checks when applicable.
- Runtime smoke test.
- Cleanup of temporary processes and containers.
- Candidate tree identity.

A successful run in the developer's existing working directory is not sufficient evidence.

---

## 9. External dependency baseline

The following provider implementations remain external dependencies:

- GPay.
- OnePay.
- Gigago.
- uMoney for R1.1.
- Transactional email provider.

Provider-specific runtime work must not begin before its corresponding adapter contract and evidence requirements are accepted.

Sandbox behavior is not treated as proof of production behavior.

---

## 10. Security baseline

Before implementing business domains:

- Secret references must remain outside source control.
- Sensitive eSIM values must not be logged.
- Organization context must be resolved from an authenticated session.
- Reference QR commercial values must be verified server-side.
- External events must enter through provider inbox handling.
- Repeatable commands must define idempotency scope.
- Privileged and sensitive access must create Audit Events.

---

## 11. Baseline acceptance

The implementation baseline is accepted when:

1. The source tag and commit are unambiguous.
2. The runtime identity is explicit.
3. Environment isolation is explicit.
4. Clean-checkout validation is mandatory.
5. Module boundaries are defined.
6. Candidate and accepted lifecycle is defined.
7. Evidence requirements are defined.
8. R1B-00 contains no runtime or database change.
