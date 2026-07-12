# YSim Local Infrastructure Baseline

This directory contains the reproducible local infrastructure baseline for
Sprint-01 platform development.

Services:

- PostgreSQL for relational persistence.
- Redis for cache and lightweight queue primitives.
- MinIO for S3-compatible object storage.
- Mailpit for local email capture.

Usage:

```bash
cp factory/config/local-infra/.env.example factory/config/local-infra/.env
./scripts/local-infra.sh up
./scripts/verify-local-infra.sh
./scripts/local-infra.sh down
```

The baseline is stored under `factory/config/` because S01-T05 allows changes
only inside factory-owned implementation assets and scripts.
