#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

MANIFEST="factory/context-manifests/s01.yaml"

[[ -f "${MANIFEST}" ]] || {
  printf 'ERROR: Missing context manifest: %s\n' "${MANIFEST}" >&2
  exit 2
}

if ./scripts/ysf.sh build-context --help 2>&1 | grep -q -- '--manifest'; then
  exec ./scripts/ysf.sh build-context --manifest "${MANIFEST}"
fi

printf '%s\n' \
  "ERROR: Current YSF build-context command does not expose --manifest." \
  "Inspect './scripts/ysf.sh build-context --help' and update this wrapper to match" \
  "the installed YSF v0.1.0 CLI contract." >&2
exit 3
