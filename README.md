# YSim Sprint-01 Definition Pack

## Purpose

This pack defines the official scope, execution model, target repository structure, acceptance criteria, and governance rules for **Sprint-01 — Platform Foundation**.

It replaces the earlier starter package and is intended to be reviewed and approved before generating the detailed task manifests `s01-t00` through `s01-t10`.

## Baseline

- Project: YSim Platform v2.1
- Architecture baseline: v2.2
- YSF baseline: v0.1.0
- Sprint code: S01
- Sprint name: Platform Foundation
- Execution model: sequential, task-by-task
- AI implementation agent: Codex CLI
- Orchestration and quality gate: YSF

## Pack contents

```text
ysim-sprint-01-definition-pack/
├── README.md
├── sprint.json
├── SCOPE.md
├── TARGET_STRUCTURE.md
├── ACCEPTANCE.md
├── EXECUTION_ORDER.md
├── DOCUMENT_BASELINE.md
├── GOVERNANCE.md
└── ai/
    └── sprints/
        └── s01-platform-foundation.yaml
```

## Important boundary

Sprint-01 establishes the technical platform foundation only.

It does **not** implement production business domains such as Product, Pricing, Order, Payment, Allocation, Supplier Gateway, or Settlement.

## Installation target

Copy this pack into the repository root:

```bash
cp -R ysim-sprint-01-definition-pack/* ~/projects/ysim-v2.1/ysim/
```

Review and commit the definition pack before creating the detailed task manifests.
