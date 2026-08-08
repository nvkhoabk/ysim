---
document_code: V3-R1-G00-S00-README
document_name: Secure Source and Delivery Factory
project: YSim v3
document_set: V3-R1-G00-S00
version: 0.2.0
status: FROZEN
language: en
---
# V3-R1 G00 S00 — Secure Source and Delivery Factory

This directory is the repository context freeze for Slice
`V3-R1-G00-S00`. It does not claim Human Acceptance, merge, deployment,
promotion, release or production activation.

## Frozen authority

- Baseline: `YSIM-V3-R1-DOCSET-2026-08-08 v0.2.0`, archive SHA-256
  `4f183a6537a126b56f7a7b8680e71b976b2c2045793fc6abd9e59ef99cc91a4d`.
- Contract: `V3-R1-G00-S00-CONTRACT-001 v0.2.0`, SHA-256
  `337519fcf7d08104ba0e53cbf33dcc4b4a75ec32aac18601cb097c778aa0ae35`.
- Human approval: `HUMAN_CONTRACT_APPROVED` by Khoa Nguyen as Business Owner
  and Technical Owner.
- Protected source: `v3/main` at commit
  `5be8413d3c22d1345b3088424af40ca2eb9d1115`, tree
  `4631630f4d57872e08f6b523ab8adf0a94453673`.
- Ruleset: `20583674`, active with no bypass actor and four required S00 checks.
- Implementation checkout and branch:
  `/root/projects/ysim-v3-r1/ysim` and
  `feature/v3-r1-g00-s00-secure-factory`.

The approved Contract file is preserved byte-exact in `slice-contract.yaml`.
Its pre-approval status fields are historical frozen content; approval is bound
separately by the decision digest and the records named in
`context-receipt.yaml`.

## Scope

S00 builds repository-local source/security/candidate-delivery controls. It
does not implement Identity, Catalog, Order, Payment, Supplier, Fulfillment,
Email or Agency business behavior. Requirements `V3-R1-OPS-004`,
`V3-R1-SEC-002`, `V3-R1-REL-002` and `V3-R1-REL-010` remain `PROPOSED`; exact
source anchors are deferred to S01.

The immutable input corpus contains 24 BRD and seven UXF files. No file in
either corpus may be edited during S00. The exact 36-path implementation
allowlist and default-deny policy are recorded in
`source-and-delivery-policy.md`.

## Stage boundary

Context Freeze B4-R1 creates only this directory and root `AGENTS.md`. It does
not change dependencies, implement factory code, commit, push, open a pull
request, run provider-facing actions, build the candidate or deploy anything.
The next permitted preparation step is separately reviewed dependency and
toolchain locking.
