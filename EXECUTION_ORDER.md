# Sprint-01 Execution Order

Tasks must execute sequentially.

| Order | Task | Purpose |
|---:|---|---|
| 0 | `s01-t00` | Repository audit, baseline confirmation, detailed execution plan |
| 1 | `s01-t01` | Root monorepo and workspace foundation |
| 2 | `s01-t02` | NestJS API bootstrap |
| 3 | `s01-t03` | Configuration, environment validation, secrets boundary |
| 4 | `s01-t04` | Logging, correlation, errors, diagnostics |
| 5 | `s01-t05` | PostgreSQL, Redis, MinIO, Mailpit, Docker baseline |
| 6 | `s01-t06` | BullMQ, scheduler, background runtime foundation |
| 7 | `s01-t07` | Health, readiness, OpenAPI, operational endpoints |
| 8 | `s01-t08` | Admin/storefront shells, design tokens, shared UI baseline |
| 9 | `s01-t09` | Tests, build, CI, validation scripts |
| 10 | `s01-t10` | Final review, evidence, acceptance, handover |

## Task gate

Before moving to the next task:

```bash
git diff --check
ysf verify
```

Task-specific validations must also pass.

## Commit rule

One implementation commit per task is preferred:

```text
feat(s01-t01): establish monorepo foundation
feat(s01-t02): bootstrap NestJS API
...
test(s01-t09): add quality and CI gates
docs(s01-t10): complete sprint acceptance
```

## Failure handling

When a task fails:

1. stop execution;
2. preserve logs;
3. do not start the next task;
4. identify whether the failure is code, environment, manifest, or baseline related;
5. repair and rerun the failed task only;
6. rerun the full quality gate before continuing.

## Parallelism

Tasks must not run in parallel during Sprint-01 because later tasks depend on artifacts created by earlier tasks.
