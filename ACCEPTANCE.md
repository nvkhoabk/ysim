# Sprint-01 Acceptance Criteria

## A. Repository

- [ ] `pnpm install` succeeds.
- [ ] Workspace package discovery succeeds.
- [ ] TypeScript strict mode is enabled.
- [ ] Root scripts expose build, lint, typecheck, test, and verify.
- [ ] No generated runtime cache is committed accidentally.

## B. API

- [ ] NestJS API starts successfully.
- [ ] `GET /health` returns a successful response.
- [ ] `GET /ready` reports dependency readiness.
- [ ] Configuration is validated at startup.
- [ ] Invalid required environment variables fail fast.
- [ ] Structured logging is enabled.
- [ ] Request/correlation identifier is available.
- [ ] Global error handling is configured.
- [ ] OpenAPI document is generated.

## C. Infrastructure

- [ ] PostgreSQL service is defined.
- [ ] Redis service is defined.
- [ ] MinIO service is defined.
- [ ] Mailpit service is defined.
- [ ] Services use named volumes where appropriate.
- [ ] Health checks are present where practical.
- [ ] No production secret is committed.

## D. Background runtime

- [ ] BullMQ foundation is configured.
- [ ] Queue naming conventions are documented.
- [ ] Scheduler/background-job bootstrap exists.
- [ ] No production business jobs are implemented.

## E. Frontend

- [ ] Admin application shell builds.
- [ ] Storefront application shell builds.
- [ ] Shared design-token package exists.
- [ ] Shared UI package exists.
- [ ] Runtime-context package exists.
- [ ] Localization bootstrap exists.
- [ ] No supplier reference appears in storefront code.

## F. Quality

- [ ] Lint passes.
- [ ] Typecheck passes.
- [ ] Unit tests pass.
- [ ] Integration tests pass.
- [ ] Build passes for all workspace projects.
- [ ] CI workflow executes the quality commands.
- [ ] `git diff --check` passes.
- [ ] `ysf verify` passes.

## G. Documentation and evidence

- [ ] Each task produces an implementation report.
- [ ] Final report records changed files and validation output.
- [ ] Target structure is satisfied or deviations are documented.
- [ ] Deferred items are listed explicitly.
- [ ] Sprint acceptance is signed off before Sprint-02 begins.

## Definition of Done

Sprint-01 is complete only when all mandatory criteria above pass and no out-of-scope business capability has been implemented.
