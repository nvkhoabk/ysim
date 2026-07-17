# Product Implementation Commissioning C1 Approval

- Decision: `APPROVED`
- Candidate: `V23-P2D-PRODUCT-IMPLEMENTATION-COMMISSIONING-C1`
- Candidate commit: `0d55ce58dbef66cc0f9d02db765d0ba52fd4ee59`
- Candidate parent: `487e806f03899ebc7571d47e72055ea28236efb4`
- Candidate tree: `6faed0e044d176070d2625166b029cfca13f33bd`
- Authorized approver: Khoa, Nguyen
- Approval scope: `PRODUCT_IMPLEMENTATION_COMMISSIONING_CONTRACT_AND_COMMISSIONING_IMPLEMENTATION`
- Generated payload aggregate: `550f9c5a3759003ed08ae285ee89ce1d503e69302c51193fb2320c9e5fae15cf`
- Git-content aggregate: `dfbde225b3d3d325e48a2afb828cc1ea13d2d0b151c9d3a000171b605e9ce497`
- Manifest SHA-256: `c5e411f004f32c2e19d18a75cc2d2005a18f49739bfe6a3b3ab8ddd02bf1caf3`

The signed candidate remains byte-identical with all seven `selected_option` fields null. The selections below are effective only through this detached approval.

## Effective technology selections

### TECH-COM-001 — Runtime and package manager

- Node.js `24.18.0` LTS; Node.js 26 Current is prohibited.
- pnpm `11.13.1` through Corepack.
- `packageManager`: `pnpm@11.13.1`.
- `.node-version`: `24.18.0`.

### TECH-COM-002 — API framework

- `@nestjs/core` `11.1.28`
- `@nestjs/common` `11.1.28`
- `@nestjs/platform-fastify` `11.1.28`
- `fastify` `5.10.0`
- TypeScript ESM; no business module.

### TECH-COM-003 — UI framework

- `next` `16.2.10`; Next.js 16.3 Preview is prohibited.
- `react` `19.2.7`
- `react-dom` `19.2.7`
- App Router, TypeScript, and Next.js 16.2-supported Turbopack defaults.

### TECH-COM-004 — Database

- PostgreSQL `18.4`.
- Local/CI image `postgres:18.4-bookworm`, with immutable digest recorded by implementation.
- UTF-8 database and UTC server/application timestamps.
- No product or other business schema.

### TECH-COM-005 — Migration and data access

- `prisma` `7.8.0`
- `@prisma/client` `7.8.0`
- `@prisma/adapter-pg` `7.8.0`
- `pg` `8.22.0`
- Prisma 7 ESM, centralized forward-only migrations, no destructive automatic migration, no business model, disposable PostgreSQL verification.

### TECH-COM-006 — Test toolchain

- `vitest` `4.1.10`
- `@playwright/test` `1.61.1`
- `typescript` `5.9.3`
- `eslint` `9.39.5`; ESLint 10 is prohibited.
- Unit/integration tests use Vitest; browser/UI smoke uses Playwright; API health may use Fastify injection or an HTTP process test.
- Direct and transitive dependencies are locked through `pnpm-lock.yaml`.

### TECH-COM-007 — Ephemeral database orchestration

- Docker Compose v2 with digest-pinned `postgres:18.4-bookworm`.
- Health check uses `pg_isready`.
- Disposable named project and disposable volume; no fixed `container_name` or host PostgreSQL dependency.
- Cleanup runs after success and failure.
- CI may use an equivalent PostgreSQL 18.4 service container with identical migration-verification behavior.

## Non-claims

- VS001 business acceptance is not approved.
- Product, catalog, storefront or pricing schema/API/UI is not approved.
- Production deployment, identity, payment, inventory, procurement, providers, other platform services and business seed data are not approved.
- Authorization is limited to the accepted commissioning boundary and its implementation candidate.
