# YSim V3-R1 G00-S00 Agent Policy

This policy applies to the whole repository while working on Slice
`V3-R1-G00-S00`.

## Bound authority

- Repository: `nvkhoabk/ysim`.
- Protected source line: `v3/main`.
- Implementation branch: `feature/v3-r1-g00-s00-secure-factory`.
- Approved seed commit: `5be8413d3c22d1345b3088424af40ca2eb9d1115`.
- Approved seed tree: `4631630f4d57872e08f6b523ab8adf0a94453673`.
- Approved Contract SHA-256:
  `0c1c0e76c6ff55afd77c6c3aeaebae4a89bd2341870766c05d2ba8610a62b8dd`.
- External-effect budget: `DENY_ALL`.

## Required behavior

1. Change only an exact path listed in
   `docs/v3/r1/g00/s00/source-and-delivery-policy.md`.
2. Treat every other repository path as protected and default-deny.
3. Never edit any file under `docs/BRD/` or `docs/UXF/`; their seed bytes are
   immutable evidence. All 86 requirements remain `PROPOSED` until S01 exact
   source-anchor review.
4. Use only synthetic disposable test data. Never read, write or emit a real
   credential, PII, ICCID, LPA or QR payload.
5. Do not call payment, supplier, email, customer, order, agency or production
   services. Do not deploy or install the proof wheel into an application
   runtime.
6. Preserve failed executions under new immutable execution IDs. Never
   overwrite or silently repair evidence from a failed run.
7. Keep generated candidate and evidence bytes outside the Git checkout in a
   unique temporary execution directory. Generated output must not be committed.
8. Stop on repository, ref, tree, ruleset, environment, corpus, approval,
   allowlist, dependency-lock, sensitive-data or evidence mismatch.

## Forbidden source-control actions

Do not merge to `v3/main`, change the default branch, weaken or bypass ruleset
`20583674`, create a tag or release, or mutate any remote ref outside the exact
Contract authority. A later Human decision is required before merge or
promotion.

## Verification boundary

The only proof artifact for S00 is a reproducible `ysf` Python wheel plus its
checksummed evidence. RP-D is a separate clean-room, non-rebuilding,
non-installing verification job with read-only repository permission, no
secrets and no business external effect.
