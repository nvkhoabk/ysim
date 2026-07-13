# S01-T07 Operational Endpoints Evidence

## Repository Assessment

- The active execution constraints allow changes under `factory/`, `knowledge/`, `tools/`, `scripts/`, and `docs/ESPK/`.
- This checkout does not contain `apps/`, `packages/`, or root `package.json`, so application source endpoints cannot be implemented without expanding scope.
- The task was completed as a factory-owned operational API baseline and verifier that can be consumed by the future API application implementation.

## Operational Baseline

- `factory/config/operational-api.yaml` defines `/health`, `/ready`, `/version`, `/openapi.json`, and `/docs`.
- `/health` has no external dependencies.
- `/ready` requires bounded checks for PostgreSQL, Redis, MinIO, and required configuration.
- `/version` is constrained to non-sensitive build metadata.
- OpenAPI documentation is stored at `knowledge/api/operational-endpoints.openapi.yaml`.

## Identified Risks

- The API application layer is absent in this checkout; runtime HTTP behavior must be wired when `apps/api` becomes available.
- The task manifest and the active prompt disagree on allowed paths. The active prompt was narrower and was followed to avoid protected or out-of-scope edits.
- Dependency checks are specified and verified as contract metadata, not executed against live PostgreSQL, Redis, or MinIO from an API process.

## Validation Result

- Added `ysf operational-api verify` for operational endpoint contract verification.
- Added the operational API verifier to `ysf verify`.
- Added unit coverage for the valid baseline, liveness dependency rejection, prohibited OpenAPI terms, and missing OpenAPI operation documentation.
- The verifier now checks that every foundation OpenAPI path includes the expected operation method and at least one documented response.
- `ysf operational-api verify`: PASS.
- `pytest tools/ysf/tests/unit/test_operational_verifier.py tools/ysf/tests/unit/test_verification.py -q`: PASS.
- `ruff check src tests`: PASS.
- `mypy src`: PASS.
- `pytest -q`: PASS.
- `git diff --check`: PASS.
- `./scripts/ysf.sh verify`: PASS.

## Implementation Recommendation

- In the first task that allows `apps/api`, implement the HTTP controllers directly from `factory/config/operational-api.yaml` and `knowledge/api/operational-endpoints.openapi.yaml`.
- Keep the YSF verifier as the contract gate so future API code cannot add business or supplier-facing paths to foundation OpenAPI.
