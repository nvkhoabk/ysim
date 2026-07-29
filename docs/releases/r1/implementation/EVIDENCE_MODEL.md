# R1B-00 — Evidence Model

## 1. Purpose

This document defines the evidence required to prove that a Release 1 slice is implemented, executable, reproducible and safely cleaned up.

Evidence is not a substitute for working software. It records proof of working software.

---

## 2. Evidence directory

Recommended structure:

```text
artifacts/r1/<slice-id>/<candidate-version>/<run-id>/
├── candidate-manifest.json
├── command-results.json
├── implementation-report.md
├── test-results/
├── runtime-evidence/
├── database-evidence/
├── security-evidence/
├── screenshots/
├── cleanup-proof.json
└── evidence-manifest.json
```

The exact path may be adapted by a slice contract, but all required evidence classes remain present.

---

## 3. Run identity

Every evidence run has:

- Run ID.
- Slice ID.
- Candidate tag.
- Candidate commit.
- Candidate tree.
- Base tag and commit.
- Start and end timestamps.
- Runtime versions.
- Host or environment classification.
- Validator version.
- Result classification.

Evidence generated from an uncommitted tree must be clearly marked preliminary and cannot support final acceptance.

---

## 4. Candidate manifest

The candidate manifest records:

- Exact changed paths.
- File status.
- File size.
- Content hash.
- Allowed-path decision.
- Secret-scan result.
- Base and candidate tree.
- Generated-file classification.
- Candidate inventory result.

The manifest must be generated from the staged or committed candidate delta, not from a zero-path status scan.

---

## 5. Command results

Each executed command records:

- Command ID.
- Command and arguments with secrets redacted.
- Working directory.
- Start timestamp.
- End timestamp.
- Exit code.
- Standard output reference.
- Standard error reference.
- Timeout classification.
- Required or optional status.
- Result.

A summary PASS cannot hide a failed required command.

---

## 6. Automated-test evidence

Required evidence may include:

- Unit-test report.
- Integration-test report.
- Authorization negative tests.
- Duplicate-event tests.
- Concurrency tests.
- Contract tests.
- Provider-fixture replay.
- Migration and database-integrity tests.
- Browser or API end-to-end tests.

The report records skipped tests and their justification.

Unexpected skipped tests block acceptance.

---

## 7. Runtime evidence

Runtime evidence proves the actual scenario.

It records:

- Started process identity.
- Listening endpoint or worker identity.
- Sanitized request.
- Sanitized response.
- Persisted aggregate identifiers.
- State transitions.
- Events or outbox records.
- Projection result.
- Audit result.
- Failure-path or recovery result.
- Process shutdown.

Mock-only evidence is insufficient when the slice claims a real provider, database or browser flow.

---

## 8. Database evidence

When a slice changes persistence, evidence includes:

- PostgreSQL instance identity classification.
- Migration list before and after.
- Migration command result.
- Schema or table ownership.
- Fixture result.
- Integrity assertions.
- Duplicate and uniqueness assertions.
- Forced-failure cleanup where applicable.
- Database teardown or preservation decision.
- No production data or credential.

---

## 9. Security evidence

Security evidence may include:

- Organization-isolation tests.
- Authorization denial.
- Secret scan.
- Signature-verification test.
- Replay and duplicate handling.
- Sensitive-log scan.
- Audit Event proof.
- Encrypted-value proof without exposing plaintext.
- Public-route exposure check.

Evidence must be sanitized before commit.

---

## 10. Screenshot and visual evidence

Screenshots are required only when visual behavior is part of acceptance.

Screenshots must:

- Identify the candidate and scenario.
- Avoid exposing customer secrets.
- Avoid exposing QR activation payload unless stored in a protected review artifact.
- Include relevant viewport or route.
- Not replace executable browser tests.

---

## 11. Cleanup proof

Cleanup proof records:

- Stopped processes.
- Released ports.
- Removed temporary files.
- Removed temporary database or container.
- Preserved resources and reason.
- Worktree status.
- Remaining background jobs.
- Cleanup result.

A passing test that leaves processes, ports or containers behind is incomplete.

---

## 12. Evidence manifest

The final evidence manifest contains:

- Every evidence file.
- Size.
- SHA-256 hash.
- Evidence class.
- Sanitization status.
- Required or optional status.
- Producer command.
- Creation timestamp.

Missing required evidence produces a failed or blocked candidate.

---

## 13. Implementation report

The implementation report summarizes:

- Business outcome.
- Scope.
- Files changed.
- Architecture decisions applied.
- Commands run.
- Test results.
- Runtime scenario.
- Failure and recovery results.
- Known limitations.
- External dependencies.
- Security review.
- Evidence locations.
- Candidate result.
- Human-review request.

The report must distinguish observed facts from conclusions.

---

## 14. Evidence retention and secrets

Release candidate evidence is retained with the candidate according to project policy.

Evidence must not contain:

- Provider API keys.
- Private certificates.
- Production database credentials.
- Full activation codes.
- Full QR payloads.
- Magic-link tokens.
- Payment card data.

Sensitive proof uses masked values, hashes or secure references.

---

## 15. Evidence acceptance

The evidence model is accepted when:

1. Candidate identity is cryptographically anchored.
2. Required command failures cannot be hidden.
3. Runtime proof is distinct from static reports.
4. Database and cleanup evidence are explicit.
5. Security evidence is sanitized.
6. Human review can reproduce the result.
7. Evidence does not expose secrets.
