#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

TASK="${1:-}"

if [[ ! "${TASK}" =~ ^t(0[0-9]|10)$ ]]; then
  printf 'Usage: %s t00|t01|...|t10\n' "$0" >&2
  exit 2
fi

MANIFEST="factory/prompt-manifests/s01-${TASK}.yaml"

[[ -f "${MANIFEST}" ]] || {
  printf 'ERROR: Missing prompt manifest: %s\n' "${MANIFEST}" >&2
  exit 3
}

if ./scripts/ysf.sh build-prompt --help 2>&1 | grep -q -- '--manifest'; then
  exec ./scripts/ysf.sh build-prompt --manifest "${MANIFEST}"
fi

printf '%s\n' \
  "ERROR: Current YSF build-prompt command does not expose --manifest." \
  "Inspect './scripts/ysf.sh build-prompt --help' and update this wrapper to match" \
  "the installed YSF v0.1.0 CLI contract." >&2
exit 4
