# Sprint-01 Scope

## 1. Sprint objective

Establish a production-oriented technical foundation for YSim so that all later business-domain sprints can be implemented consistently, tested automatically, and operated through the YSF workflow.

## 2. In scope

### Repository and workspace foundation

- pnpm workspace conventions
- root package scripts
- TypeScript strict-mode baseline
- shared linting and formatting configuration
- application and package naming conventions
- environment file conventions
- repository validation scripts

### Backend application foundation

- NestJS API bootstrap under `apps/api`
- configuration module
- environment validation
- structured logging
- correlation/request identifiers
- global error boundary
- health and readiness endpoints
- OpenAPI bootstrap
- test bootstrap

### Frontend application shells

- `apps/admin-web`
- `apps/storefront-web`
- shared design-token baseline
- shared UI package baseline
- runtime-context package baseline
- no completed business screens

### Shared packages

- config
- logging
- contracts
- errors
- testing
- design-tokens
- ui
- runtime-context

### Infrastructure foundation

- PostgreSQL
- Redis
- MinIO
- Mailpit
- Docker Compose baseline
- BullMQ bootstrap
- scheduler/background-job bootstrap
- database folder conventions
- integration folder conventions

### Engineering quality

- lint
- typecheck
- unit test
- integration test
- build
- CI workflow
- verification scripts
- Sprint evidence and acceptance report

## 3. Explicitly out of scope

The following must not be implemented as real business modules in Sprint-01:

- Product
- Catalog
- Pricing
- Promotion
- Shopping Cart
- Checkout business flow
- Order
- Payment business flow
- Refund
- Allocation
- Inventory
- Fulfillment
- Supplier Gateway
- Supplier mappings
- Settlement
- Commission
- Customer Care
- Reporting business logic
- White-label storefront business binding
- Published storefront snapshots
- Runtime supplier selection

Interfaces, placeholders, folder seams, and empty contracts may be created only where required to preserve architecture boundaries.

## 4. Architecture invariants

1. Storefront code must never reference a supplier.
2. Supplier selection belongs only to the future Allocation capability.
3. Runtime resolution may resolve references but must not execute business logic.
4. UI components must not embed business decisions.
5. All configuration must be compatible with PCS and ECS conventions.
6. Business policy execution must remain outside presentation code.
7. Shared packages must not depend on applications.
8. Infrastructure must not leak into domain contracts.
9. Generated files and runtime artifacts must not silently modify frozen documents.
10. Every task must pass YSF verification before the next task begins.

## 5. Sprint outcome

At Sprint completion, the repository must provide a stable platform skeleton that starts, builds, tests, reports health, documents its API, and is ready for the first business-domain sprint.
