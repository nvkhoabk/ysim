# Target Repository Structure

The following structure is the target baseline. Empty directories should not be created unless they contain a tracked placeholder, README, configuration, or implementation artifact.

```text
.
├── apps/
│   ├── api/
│   │   ├── src/
│   │   ├── test/
│   │   ├── package.json
│   │   └── tsconfig.json
│   ├── admin-web/
│   │   ├── src/
│   │   ├── package.json
│   │   └── tsconfig.json
│   └── storefront-web/
│       ├── src/
│       ├── package.json
│       └── tsconfig.json
├── packages/
│   ├── config/
│   ├── contracts/
│   ├── design-tokens/
│   ├── errors/
│   ├── logging/
│   ├── runtime-context/
│   ├── testing/
│   └── ui/
├── database/
│   ├── migrations/
│   ├── seeds/
│   └── README.md
├── integrations/
│   └── README.md
├── infrastructure/
│   ├── docker/
│   ├── compose/
│   └── README.md
├── scripts/
│   ├── validate-workspace.sh
│   ├── verify-sprint-01.sh
│   └── run-sprint-01.sh
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
├── factory/
├── knowledge/
├── tools/
│   └── ysf/
├── pnpm-workspace.yaml
├── package.json
├── tsconfig.base.json
├── eslint.config.*
├── .env.example
└── docker-compose.yml
```

## Dependency rules

```text
apps
  └── may depend on packages

packages
  └── may depend on other lower-level packages only

infrastructure
  └── may implement contracts from packages

integrations
  └── may implement gateway contracts, but no supplier implementation is required in Sprint-01

docs/factory/knowledge/tools
  └── remain independent from product runtime code
```

## Frontend boundaries

`admin-web` and `storefront-web` must share:

- design tokens
- base UI components
- accessibility rules
- localization primitives
- runtime-context types

They must not duplicate foundational components.

## Backend boundaries

The API application may contain bootstrap modules, but must not introduce production business aggregates in Sprint-01.
