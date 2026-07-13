# S01-T08 Frontend Foundation Evidence

## Repository Assessment

- The active runner constraints allow changes under `factory/`, `knowledge/`, `tools/`, `scripts/`, and `docs/ESPK/`.
- The task manifest for S01-T08 asks for `apps/admin-web/`, `apps/storefront-web/`, and `packages/*`, but those paths are not allowed by the active prompt and are absent from this checkout.
- The task was completed as a factory-owned frontend foundation baseline and verifier that future frontend source can implement without redefining design, context, localization, or accessibility contracts.

## Frontend Foundation Baseline

- `factory/config/frontend-foundation.yaml` defines Admin and Storefront shell expectations, shared package contracts, localization fallback, runtime context fields, accessibility defaults, responsive breakpoints, and the YSim green identity baseline.
- `knowledge/ui/design-tokens.json` defines the default YSim green design token contract.
- `knowledge/ui/runtime-context.json` defines request-scoped runtime-context fields for organization, storefront, locale, currency, theme, tracking, and preferences.
- `knowledge/ui/localization-resources.json` defines English and Vietnamese shell resources with English fallback coverage.

## Identified Risks

- Buildable frontend apps cannot be created until `apps/admin-web/`, `apps/storefront-web/`, `packages/design-tokens/`, `packages/ui/`, `packages/runtime-context/`, `packages/localization/`, `package.json`, and `pnpm-lock.yaml` are allowed for modification.
- The active prompt and the task manifest disagree on allowed paths. The active prompt was followed to avoid protected or out-of-scope edits.
- Visual smoke pages and browser screenshots remain pending because no frontend runtime source can be created in the current scope.

## Validation Result

- Added `ysf frontend-foundation verify` for frontend foundation contract verification.
- Added the frontend foundation verifier to `ysf verify`.
- Added unit coverage for the valid baseline, missing runtime-context fields, and prohibited infrastructure-provider context leakage.
- `./scripts/ysf.sh frontend-foundation verify`: PASS.
- `pytest tests/unit/test_frontend_verifier.py tests/unit/test_verification.py -q`: PASS when run through the YSF virtualenv.
- `git diff --check`: PASS.
- `./scripts/ysf.sh verify`: PASS.

## Implementation Recommendation

- In the first task that allows `apps/`, `packages/`, root `package.json`, and `pnpm-lock.yaml`, implement the Admin and Storefront shells directly from `factory/config/frontend-foundation.yaml` and the `knowledge/ui/*` contracts.
- Keep `ysf frontend-foundation verify` as the contract gate so future UI code continues to share tokens, localization, runtime context, accessibility defaults, and Storefront isolation rules.
