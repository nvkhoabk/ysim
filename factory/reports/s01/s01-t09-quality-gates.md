# S01-T09 Quality Gates, CI, Validation and Developer Workflow

## Repository Assessment

- Current checkout is the S01 platform-foundation factory/tooling repository.
- Existing executable verification is centered on `./scripts/ysf.sh verify`, which already runs doctor, background runtime, operational API, frontend foundation, ruff, mypy, pytest, YSF pipeline, and `git diff --check`.
- This checkout does not include root `package.json`, `pnpm-workspace.yaml`, `apps/`, or `packages/`; Node workspace stages are therefore implemented as explicit conditional stages that run when a Node workspace exists and otherwise emit SKIP with a reason.
- Local infrastructure validation is already represented by `./scripts/ysf.sh local-infra verify`; S01-T09 adds the runtime Docker Compose config gate through `./scripts/ysf.sh local-infra verify --runtime`.

## Implemented Pipeline

Run the complete local gate:

```bash
bash scripts/verify-platform.sh
```

The gate executes:

- repository doctor;
- install when a root Node workspace exists;
- workspace lint, typecheck, tests, and build when a root Node workspace exists;
- YSF verification;
- local infrastructure static validation;
- Docker Compose config validation;
- protected architecture path check;
- Storefront/UI supplier-boundary check;
- high-confidence secret hygiene check;
- whitespace diff check.

## Security And Boundary Checks

- `scripts/check-protected-paths.sh` fails when the working tree modifies frozen architecture paths.
- `scripts/check-supplier-boundary.sh` scans Storefront/UI-owned paths for supplier/provider leakage terms.
- `scripts/check-secret-hygiene.sh` detects sensitive filenames and high-confidence credential patterns without printing secret values.

## Identified Risks

- CI workflow creation is requested by the task manifest, but this execution's allowed paths do not include `.github/`; no workflow file was created in this task.
- Root Node workspace commands cannot be executed in this checkout because the root workspace files are absent. The platform verifier records these stages as SKIP rather than PASS.
- Docker Compose config validation requires Docker Compose on PATH. Missing Docker in a CI runner will fail the infrastructure stage clearly.

## Validation Result

Validated locally:

- `bash scripts/verify-platform.sh` — PASS
- `git diff --check` — PASS
- `./scripts/ysf.sh verify` — PASS

The platform verifier produced PASS for repository doctor, YSF verification,
infrastructure static validation, Docker Compose config validation,
protected-path checks, supplier-boundary checks, secret hygiene, and whitespace
diff checks. Node install/lint/typecheck/test/build stages were SKIP because
the checkout has no root Node workspace files.

## Implementation Recommendation

- Add `.github/workflows/ci.yml` in a task or execution context where `.github/` is explicitly allowed.
- Use `docs/ESPK/S01-T09-CI-WORKFLOW.md` as the workflow template when `.github/` changes are permitted.
- Use `bash scripts/verify-platform.sh` as the CI entrypoint so local and CI quality gates stay aligned.
- When the Node workspace is introduced, keep root `package.json`, `pnpm-workspace.yaml`, and package scripts aligned with the existing conditional stage names: lint, typecheck, test, and build.
