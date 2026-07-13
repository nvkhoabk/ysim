---
document_code: ESPK-S01-T09-CI
document_name: S01-T09 CI Workflow Template
project: YSim v2.1
document_set: Sprint
version: 2.1
status: Draft
language: en-US
---

# S01-T09 CI Workflow Template

This template keeps CI aligned with the local quality gate while `.github/`
changes are outside the current task permissions.

```yaml
name: platform-quality

on:
  pull_request:
  push:
    branches:
      - feat/s01-platform-foundation

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: "22"

      - name: Enable pnpm
        run: corepack enable

      - name: Install YSF
        run: python -m pip install -e tools/ysf[dev]

      - name: Verify platform
        run: bash scripts/verify-platform.sh
```

When `.github/` is allowed, install this as `.github/workflows/ci.yml`.
