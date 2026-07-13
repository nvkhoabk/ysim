# Sprint-01 Execution Plan

## Baseline

- Branch: `feat/s01-platform-foundation`
- Current HEAD: `5d9f8d425a7150550abfe54ab9f925538afe1fcf`
- HEAD tag: `s01-t09-complete`
- Architecture baseline: `architecture-v2.2` at `5be8413d3c22d1345b3088424af40ca2eb9d1115`
- YSF baseline: `0.1.0`
- Execution mode: sequential, fail fast
- Product runtime source state: not yet present in the current tree

## Gate Policy

Run task-specific validation first, then:

```bash
git diff --check
./scripts/ysf.sh verify
```

The runner requires the repository wrapper rather than a bare `ysf` command. `./scripts/ysf.sh verify` resolves YSF v0.1.0 and passed during T00.

## Ordered Tasks

| Order | Task | Objective | Required outputs | Validation focus | Current gap |
|---:|---|---|---|---|---|
| 0 | `s01-t00` | Audit baseline and plan execution. | `factory/reports/s01/s01-t00-repository-audit.md`, gap matrix, this plan | YSF wrapper verify, diff check | Complete |
| 1 | `s01-t01` | Establish pnpm workspace, strict TypeScript, root scripts, env conventions, and tracked top-level implementation dirs. | `package.json`, `pnpm-workspace.yaml`, `tsconfig.base.json`, `.env.example`, workspace validation | install, workspace validation, no secrets | Missing |
| 2 | `s01-t02` | Bootstrap NestJS API without business modules. | `apps/api/`, API test harness, platform contract/testing seams | API build/lint/typecheck/test | Missing |
| 3 | `s01-t03` | Add typed configuration and environment validation. | `packages/config/`, API config integration, safe env examples | valid/invalid config tests, secret redaction | Missing |
| 4 | `s01-t04` | Add structured logging, correlation IDs, standard errors, and diagnostics. | `packages/logging/`, `packages/errors/`, API exception/correlation integration | logging/error tests, no secret leakage | Missing |
| 5 | `s01-t05` | Add local infrastructure baseline. | `docker-compose.yml`, `infrastructure/`, `database/`, `integrations/` conventions | Docker config, static infra validation | Missing |
| 6 | `s01-t06` | Add BullMQ, scheduler, and background runtime foundation. | queue registry, worker framework, scheduler bootstrap | no business jobs, Redis seam works | Missing |
| 7 | `s01-t07` | Add health, readiness, OpenAPI, version, and operational endpoints. | health/readiness modules, OpenAPI bootstrap | endpoint tests, dependency readiness | Missing |
| 8 | `s01-t08` | Add admin/storefront shells, shared design tokens, shared UI, runtime context. | `apps/admin-web/`, `apps/storefront-web/`, `packages/design-tokens/`, `packages/ui/`, `packages/runtime-context/` | frontend build/test, no supplier refs | Missing |
| 9 | `s01-t09` | Add full quality gates and CI. | `.github/workflows/ci.yml`, `scripts/verify-sprint-01.sh`, validation reports | full workspace build/lint/typecheck/test | Missing source CI workflow |
| 10 | `s01-t10` | Final review, evidence, acceptance, and handover. | acceptance report, evidence manifest, final changed-file summary | all gates pass, no scope violations | Pending implementation |

## Deterministic Sequence

1. Treat `s01-t00` as complete after the audit report, gap matrix, execution plan, and validation result are present.
2. Start implementation at `s01-t01` because no workspace foundation exists in the current HEAD tree.
3. Do not skip directly to later tasks based on tag names. Advance only when the task's required source artifacts and validation reports exist.
4. Commit only after each task's validation passes. The current runner instruction says not to commit during this T00 execution.
5. Stop immediately if implementation requires changes to frozen architecture documents or real business-domain source.

## Stop Conditions

- Any frozen architecture source document must be edited to pass.
- A real business aggregate, supplier mapping, payment flow, allocation implementation, or storefront business binding is required.
- A production secret is discovered or required.
- Validation cannot pass without expanding Sprint-01 scope.
- Existing generated artifacts conflict with task outputs and cannot be reconciled without user review.

## Implementation Recommendation

Proceed to `s01-t01` after the runner records this T00 evidence. Use `./scripts/ysf.sh verify` as the unified YSF gate, maintain strict sequential execution, and require source artifacts to prove each task rather than relying on completion tags alone.
