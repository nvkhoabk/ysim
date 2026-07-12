# Sprint-01 Execution Plan

## Baseline

- Branch: `feat/s01-platform-foundation`
- Current HEAD: `3a8982808b16d869976e9304bdb7230cdb272871`
- Architecture baseline: `architecture-v2.2` at `5be8413d3c22d1345b3088424af40ca2eb9d1115`
- YSF baseline: `0.1.0`
- Execution mode: sequential, fail fast

## Gate Policy

Run task-specific validation first, then:

```bash
git diff --check
./scripts/ysf.sh verify
```

The bare `ysf verify` command is required by the Sprint pack but is not on PATH in this shell. The repository wrapper resolves the installed `../.venv-ysf/bin/ysf` executable and passed verification during T00.

## Ordered Tasks

| Order | Task | Objective | Primary outputs | Validation focus |
|---:|---|---|---|---|
| 0 | `s01-t00` | Audit baseline and plan execution. | `factory/reports/s01/s01-t00-repository-audit.md`, gap matrix, this plan | YSF wrapper verify, diff check |
| 1 | `s01-t01` | Establish pnpm workspace, strict TypeScript, root scripts, env conventions, and tracked top-level implementation dirs. | `package.json`, `pnpm-workspace.yaml`, `tsconfig.base.json`, `.env.example`, `scripts/validate-workspace.sh` | install, workspace validation, no secrets |
| 2 | `s01-t02` | Bootstrap NestJS API without business modules. | `apps/api/`, API test harness, optional bootstrap smoke endpoint | API build/lint/typecheck/test |
| 3 | `s01-t03` | Add typed configuration and environment validation. | `packages/config/`, `apps/api/src/config/`, updated `.env.example` | valid/invalid config tests, secret redaction |
| 4 | `s01-t04` | Add structured logging, correlation IDs, standard errors, and diagnostics. | `packages/logging/`, `packages/errors/`, API exception/correlation integration | logging/error tests, no secret leakage |
| 5 | `s01-t05` | Add local infrastructure baseline. | `docker-compose.yml`, `infrastructure/`, `database/`, infra scripts | Docker config, service health/connectivity |
| 6 | `s01-t06` | Add BullMQ, scheduler, and background runtime foundation. | queue registry, worker framework, scheduler bootstrap | no business jobs, Redis seam works |
| 7 | `s01-t07` | Add health, readiness, OpenAPI, version, and operational endpoints. | health/readiness modules, OpenAPI bootstrap | endpoint tests, dependency readiness |
| 8 | `s01-t08` | Add admin/storefront shells, shared design tokens, shared UI, runtime context. | `apps/admin-web/`, `apps/storefront-web/`, `packages/design-tokens/`, `packages/ui/`, `packages/runtime-context/` | frontend build/test, no supplier refs |
| 9 | `s01-t09` | Add full quality gates and CI. | `.github/workflows/ci.yml`, `scripts/verify-sprint-01.sh`, validation reports | full workspace build/lint/typecheck/test |
| 10 | `s01-t10` | Final review, evidence, acceptance, and handover. | acceptance report, evidence manifest, final changed-file summary | all gates pass, no scope violations |

## Stop Conditions

- Any frozen architecture source document must be edited to pass.
- A real business aggregate, supplier mapping, payment flow, allocation implementation, or storefront business binding is required.
- A production secret is discovered or required.
- Validation cannot pass without expanding Sprint-01 scope.
- Existing untracked artifacts conflict with task outputs and cannot be reconciled without user review.

## Implementation Recommendation

Proceed to `s01-t01` only after deciding whether to expose `ysf` on PATH or standardize task gates on `./scripts/ysf.sh`. Keep one implementation commit per task after task-specific validation and unified YSF verification pass.
