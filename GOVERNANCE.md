# Sprint-01 Governance

## 1. Branching

Recommended working branch:

```text
feat/s01-platform-foundation
```

Create it from the approved architecture baseline commit or tag.

## 2. Protected content

Sprint-01 implementation must not modify frozen foundation documents unless an explicit architecture change is approved.

Protected areas include, at minimum:

- `docs/BRD/`
- `docs/ABP/`
- `docs/AFM/`
- `docs/YADF/`
- `docs/DIP/`
- `docs/UXF/`
- `docs/CAP/`
- `docs/ECS/`
- `docs/PCS/`
- `docs/POL/`

Generated indexes may be rebuilt through YSF, but source documents must not be silently edited.

## 3. Allowed implementation areas

- `apps/`
- `packages/`
- `database/`
- `integrations/`
- `infrastructure/`
- `.github/`
- implementation scripts
- Sprint-specific factory manifests, prompts, reports, and runtime outputs

## 4. Secrets

- Never commit real API keys.
- Never commit payment credentials.
- Never commit supplier credentials.
- Use `.env.example` with non-sensitive placeholders.
- Keep local values outside Git.

## 5. Supplier boundary

Sprint-01 must not introduce supplier-specific product, storefront, catalog, checkout, or UI structures.

Any future supplier integration must sit behind YSim-owned contracts and the Allocation/Supplier Gateway boundary.

## 6. Evidence

Each task report must include:

- objective;
- files changed;
- commands executed;
- validation results;
- unresolved issues;
- deferred work;
- commit identifier.

## 7. Scope control

Any requirement that introduces a real business aggregate must be deferred unless it is strictly necessary for platform bootstrap and approved as a contract-only placeholder.

## 8. Completion

Sprint-01 may be accepted only after `s01-t10` confirms all prior task reports, quality gates, and architecture invariants.
