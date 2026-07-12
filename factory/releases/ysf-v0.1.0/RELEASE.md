# YSF v0.1.0 — Dry-Run Factory Engine

## Status

Frozen baseline for the YSim Software Factory dry-run execution engine.

## Pipeline

| Order | Stage | Status |
|---:|---|---|
| 10 | Index | Production baseline |
| 20 | Knowledge | Production baseline |
| 30 | Context | Production baseline |
| 40 | Prompt | Production baseline |
| 50 | Execution | Dry-run only |

## Available commands

```bash
ysf doctor
ysf build-index
ysf build-knowledge
ysf build-context
ysf build-prompt
ysf pipeline
ysf run --dry-run
ysf verify
```

## Safety boundary

YSF v0.1.0 does not invoke Codex during pipeline execution.

The execution stage:

validates the prompt artifact;
creates an execution plan;
captures the Git workspace state;
resolves the provider;
generates dry-run reports;
reports zero provider-modified files.

## Deferred to the next version

Real Codex CLI invocation
Workspace-write execution
Protected-path enforcement after execution
Automatic rollback
Retry and resume
Multi-task sprint orchestration