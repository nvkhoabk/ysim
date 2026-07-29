# R1B-00 Acceptance Checklist

## A. Baseline

- [ ] Branch was created from `baseline/r1/r1a-04/accepted-v1`.
- [ ] Branch name is `release/r1b-00-implementation-baseline`.
- [ ] R1A-04 accepted baseline remains unchanged.
- [ ] VS001 recovery worktree remains unchanged.
- [ ] No runtime file is modified.
- [ ] No database file is modified.
- [ ] No package manifest is modified.
- [ ] No secret or credential is included.

## B. Implementation baseline

- [ ] Source baseline is explicit.
- [ ] Repository and worktree policy is explicit.
- [ ] Runtime identity is explicit.
- [ ] Environment isolation is explicit.
- [ ] Application process model is explicit.
- [ ] Persistence baseline is explicit.
- [ ] Clean-checkout baseline is explicit.
- [ ] External dependencies are explicit.
- [ ] Security baseline is explicit.

## C. Module structure

- [ ] Target bounded-context modules are listed.
- [ ] Module internal layering is defined.
- [ ] Dependency direction is defined.
- [ ] Cross-context interaction is defined.
- [ ] Shared-package rules are defined.
- [ ] Database ownership mapping is defined.
- [ ] Provider adapter locations are defined.
- [ ] Storefront boundary is preserved.
- [ ] Boundary enforcement is required.
- [ ] First slice avoids unrelated scaffolding.

## D. Execution contract

- [ ] Unit of delivery is an executable vertical slice.
- [ ] Lifecycle states are defined.
- [ ] Branch and tag naming is defined.
- [ ] Candidate isolation is mandatory.
- [ ] Slice specification is required before implementation.
- [ ] Static, automated, runtime and clean-checkout validation are defined.
- [ ] Human acceptance is mandatory.
- [ ] Automated repair limit is defined.
- [ ] Database-change contract is defined.
- [ ] Provider-integration contract is defined.
- [ ] Security contract is defined.
- [ ] Rejected candidates remain immutable.

## E. Evidence model

- [ ] Evidence directory structure is defined.
- [ ] Run identity is defined.
- [ ] Candidate manifest is defined.
- [ ] Command results are defined.
- [ ] Automated-test evidence is defined.
- [ ] Runtime evidence is defined.
- [ ] Database evidence is defined.
- [ ] Security evidence is defined.
- [ ] Cleanup proof is defined.
- [ ] Evidence manifest is defined.
- [ ] Implementation report is defined.
- [ ] Secret restrictions are defined.

## F. Scope integrity

- [ ] R1B-00 does not create business modules.
- [ ] R1B-00 does not change database schema.
- [ ] R1B-00 does not change runtime dependencies.
- [ ] R1B-00 does not modify provider credentials.
- [ ] R1B-00 does not revive or merge prior VS001 work.
- [ ] VS-R1-001 remains the next executable slice.

## G. Candidate inventory

The candidate must contain exactly:

```text
docs/releases/r1/INDEX.md
docs/releases/r1/implementation/INDEX.md
docs/releases/r1/implementation/IMPLEMENTATION_BASELINE.md
docs/releases/r1/implementation/MODULE_STRUCTURE.md
docs/releases/r1/implementation/EXECUTION_CONTRACT.md
docs/releases/r1/implementation/EVIDENCE_MODEL.md
docs/releases/r1/implementation/R1B_00_ACCEPTANCE_CHECKLIST.md
```

Validation:

- [ ] Candidate contains exactly seven files from the R1A-04 baseline.
- [ ] `git diff --check` succeeds.
- [ ] All files exist and are non-empty.
- [ ] All files use LF line endings.
- [ ] Release Index links Implementation Index.
- [ ] Implementation Index links all R1B-00 documents.
- [ ] No `Zone.Identifier` file exists.
- [ ] No runtime, database, package, script, test or artifact path is changed.
- [ ] Working tree is clean after commit.
- [ ] Candidate tag is created.

## Acceptance result

```text
R1B-00_RESULT=PENDING
```

After approval:

```text
R1B-00_RESULT=PASS
```
