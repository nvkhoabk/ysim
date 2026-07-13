# Sprint-01 Task T06 Background Runtime Foundation

## Repository Assessment

- The current execution scope permits `factory/`, `knowledge/`, `tools/`,
  `scripts/`, and `docs/ESPK/` only.
- The canonical S01-T06 manifest references `packages/queue/`,
  `packages/scheduler/`, `apps/api/`, and `pnpm`, but those paths are outside
  the active task prompt scope and are not present in this repository snapshot.
- The background foundation is therefore implemented as YSF factory runtime
  contracts, deterministic verification, and test coverage under `tools/ysf`
  with configuration under `factory/config/`.
- Protected frozen documentation paths were not modified.

## Implemented Foundation

- Added generic queue naming rules: `ysim:{environment}:{capability}:{purpose}`.
- Added versioned job envelope, job result, error, failed-job, queue default,
  worker lifecycle, and scheduled-job contracts.
- Added a BullMQ adapter seam through a queue backend protocol while keeping the
  test backend deterministic and Redis-free.
- Added retry, exponential backoff, timeout, concurrency, completion retention,
  failure retention, and graceful shutdown defaults.
- Added a scheduler abstraction for delayed and recurring jobs.
- Added test-only enqueue-process-complete and retry-to-failure coverage.
- Added background runtime verification to the unified YSF quality gate.

## Identified Risks

- Production BullMQ package implementation remains deferred until a task allows
  canonical `packages/` and `apps/` paths.
- Runtime Redis integration is represented by configuration and adapter seam in
  this constrained task; no Redis connection is opened during validation.
- The foundation intentionally defines no production business job.

## Validation Result

- `python -m pytest -q tests/unit/test_background_runtime.py tests/unit/test_background_verifier.py`: PASS
- `./scripts/ysf.sh verify`: PASS
- `git diff --check`: PASS

## Implementation Recommendation

Use this factory baseline as the shared contract for the later application
implementation. When `packages/queue/`, `packages/scheduler/`, and `apps/api/`
are explicitly in scope, bind the queue backend protocol to BullMQ and keep the
same envelope, naming, lifecycle, retry, failed-job, and observability contracts.
