# Factory Index

This directory contains machine-generated indexes used by the YSim AI Software Factory.

## Files

- `documents.json`: catalog of documentation under `docs/`
- `knowledge.json`: catalog of AI-optimized knowledge under `knowledge/`
- `catalog.json`: master catalog referencing all indexes

## Source of Truth

- `docs/` is the authoritative human-readable documentation source.
- `knowledge/` is the AI-optimized knowledge source.
- Files in `factory/index/` are generated artifacts and must not be edited manually.

## Rebuild

```bash
bash scripts/build-factory-index.sh
