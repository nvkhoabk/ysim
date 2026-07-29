# R1A-04 Acceptance Checklist

## A. Baseline

- [ ] Branch was created from `baseline/r1/r1a-03/accepted-v1`.
- [ ] Branch name is `release/r1a-04-release-planning`.
- [ ] R1A-03 accepted baseline remains unchanged.
- [ ] VS001 recovery worktree remains unchanged.
- [ ] No runtime file is modified.
- [ ] No database file is modified.
- [ ] No package manifest is modified.
- [ ] No secret or credential is included.

## B. Release backlog

- [ ] Every R1.0 vertical slice is represented.
- [ ] R1.1 Laos slices are represented.
- [ ] Priorities are assigned.
- [ ] Primary contexts are identified.
- [ ] Dependencies are identified.
- [ ] Executable outcomes are stated.
- [ ] Evidence expectations are stated.
- [ ] Deferred capabilities remain outside Release 1.
- [ ] Backlog entry conditions are defined.

## C. Dependency graph

- [ ] Critical path is explicit.
- [ ] Payment core precedes payment adapters.
- [ ] Payment success precedes procurement.
- [ ] Procurement precedes fulfillment.
- [ ] Fulfillment precedes delivery and commission eligibility.
- [ ] Allowed parallel lanes are defined.
- [ ] External dependencies are registered.
- [ ] Blocking rules are defined.
- [ ] Dependency change control is defined.

## D. Delivery milestones

- [ ] Architecture milestone is defined.
- [ ] Organization and Agency milestone is defined.
- [ ] Catalog and Pricing milestone is defined.
- [ ] Checkout milestone is defined.
- [ ] Payment milestone is defined.
- [ ] Fulfillment milestone is defined.
- [ ] Customer and Agency experience milestone is defined.
- [ ] Operations milestone is defined.
- [ ] Internal pilot milestone is defined.
- [ ] Two-agency pilot milestone is defined.
- [ ] Expanded pilot milestone is defined.
- [ ] Laos activation milestone is defined.
- [ ] Evidence requirements are defined.
- [ ] Reforecast triggers are defined.
- [ ] Pilot measures are defined.

## E. Scope integrity

- [ ] R1.0 remains releasable without uMoney activation.
- [ ] GPay and OnePay remain R1.0.
- [ ] Gigago remains the first supplier runtime.
- [ ] Agency Portal remains R1.0.
- [ ] Customer Portal and email delivery remain R1.0.
- [ ] Full refund remains R1.0.
- [ ] Partial refund remains deferred.
- [ ] Agency wallet remains deferred.
- [ ] Automatic supplier fallback remains deferred.
- [ ] Runtime implementation has not started in R1A-04.

## F. Candidate inventory

The candidate must contain exactly:

```text
docs/releases/r1/INDEX.md
docs/releases/r1/planning/INDEX.md
docs/releases/r1/planning/RELEASE_BACKLOG.md
docs/releases/r1/planning/DEPENDENCY_GRAPH.md
docs/releases/r1/planning/DELIVERY_MILESTONES.md
docs/releases/r1/planning/R1A_04_ACCEPTANCE_CHECKLIST.md
```

Validation:

- [ ] Candidate contains exactly six files from the R1A-03 baseline.
- [ ] `git diff --check` succeeds.
- [ ] All files exist and are non-empty.
- [ ] All files use LF line endings.
- [ ] Release Index links Planning Index.
- [ ] Planning Index links all R1A-04 documents.
- [ ] No `Zone.Identifier` file exists.
- [ ] No runtime, database, package or artifact path is changed.
- [ ] Working tree is clean after commit.
- [ ] Candidate tag is created.

## Acceptance result

```text
R1A-04_RESULT=PENDING
```

After approval:

```text
R1A-04_RESULT=PASS
```
