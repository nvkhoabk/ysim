#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
MANIFEST="${1:-factory/context-manifests/s00.yaml}"

cd "${REPO_ROOT}"

[[ -f "${MANIFEST}" ]] || {
  printf 'Missing context manifest: %s\n' "${MANIFEST}" >&2
  exit 1
}

python3 -m py_compile tools/context/build-context.py

python3 tools/context/build-context.py \
  --repo-root "${REPO_ROOT}" \
  --manifest "${REPO_ROOT}/${MANIFEST}"

git diff --check

printf 'Context package generated successfully.\n'
