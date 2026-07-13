---
document_code: V23-DOCUMENT-BASELINE
document_name: YSim v2.3 Document Baseline
project: YSim Platform
document_set: Baseline Governance
version: 1.0
status: DRAFT
language: en-US
baseline: v2.3
source_commit: 5be8413
---

# YSim v2.3 Document Baseline

## 1. Purpose

This document declares the documentation baseline used to rebuild YSim Platform v2.3.

The v2.3 baseline inherits approved business and architecture knowledge from
Architecture Baseline v2.2 while replacing the failed AI-assisted implementation
and Sprint execution model.

## 2. Source baseline

- Source Git commit: `5be8413`
- Source Git tag: `architecture-v2.2`
- v2.3 branch: `rebuild/v2.3-foundation`
- Previous implementation branch: `feat/s01-platform-foundation`

The previous Sprint-01 implementation branch is retained for audit purposes. It
is not an approved source-code baseline for v2.3.

## 3. Baseline principles

1. Business knowledge may be inherited without inheriting the failed delivery process.
2. Existing document codes and filenames remain stable during baseline review.
3. Document versions must not be changed to v2.3 through a mechanical bulk replacement.
4. Existing FROZEN status means frozen in the previous baseline, not automatically approved for v2.3.
5. AI development and Sprint governance documents require explicit re-approval.
6. Generated indexes and knowledge catalogs are not authoritative source documents.
7. No Sprint implementation may start before the v2.3 delivery framework is approved.
8. Human-operable runtime evidence is mandatory for future implementation acceptance.

## 4. Document classification

| Document set | v2.3 classification | Action |
|---|---|---|
| BRD | ADOPTED | Retain as business source of truth |
| ABP-00 to ABP-14 | ADOPTED_WITH_REVIEW | Retain and review incrementally |
| ABP-15 | REWRITE_REQUIRED | Replace AI implementation architecture |
| ABP-16 to ABP-18 | ADOPTED_WITH_REVIEW | Retain subject to implementation review |
| AFM | SUPERSEDED_PENDING | Replace with a v2.3 freeze manifest |
| YADF | REWRITE_REQUIRED | Replace delivery framework |
| AAP | REWRITE_REQUIRED | Replace AI collaboration model |
| SGP | REWRITE_REQUIRED | Replace Sprint governance model |
| DIP | REWRITE_REQUIRED | Replace with executable vertical-slice delivery |
| ESP | REVIEW_REQUIRED | Review engineering standards |
| ROP | REVIEW_REQUIRED | Review operational procedures |
| ESPK-S00 | HISTORICAL | Retain for audit; do not execute |
| UXF | DRAFT_REVIEW | Complete and approve |
| CAP | DRAFT_REVIEW | Complete and approve |
| ECS | DRAFT_REVIEW | Complete and approve |
| PCS | DRAFT_REVIEW | Complete and approve |
| POL | DRAFT_REVIEW | Complete and approve |

## 5. Prohibited carry-over

The following v2.2/Sprint-01 mechanisms must not be reused without redesign:

- Auto-runner completion based only on process exit code.
- Completion tags created without required product artifacts.
- Validation stages that treat missing mandatory components as SKIP.
- Factory-owned substitutes for required application runtime code.
- Empty human-acceptance templates presented as evidence.
- Generated reports used as substitutes for working software.
- Task prompts whose allowed paths conflict with task manifests.
- Automated acceptance or sign-off on behalf of human reviewers.

## 6. Required v2.3 replacements

Before implementation begins, v2.3 must define:

- YADF v2.3;
- structured Codex task-result protocol;
- executable vertical-slice Sprint model;
- artifact and dependency gates;
- runtime smoke-test model;
- browser-based frontend verification;
- machine-verification policy;
- human-acceptance gate;
- evidence integrity model;
- environment and ARM64 compatibility baseline.

## 7. Current decision

The documentation baseline is accepted for review only.

No document classified as `REWRITE_REQUIRED`, `REVIEW_REQUIRED`,
`DRAFT_REVIEW`, or `SUPERSEDED_PENDING` is approved for controlling v2.3
implementation until separately reviewed and approved.
