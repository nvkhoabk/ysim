#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

MODE="${1:---dry-run}"

if [[ "${MODE}" != "--dry-run" ]]; then
  printf 'ERROR: Sprint-01 full runner supports --dry-run only.\n' >&2
  exit 2
fi

for task in $(seq -w 0 10); do
  printf '\n=== Sprint-01 t%s ===\n' "${task}"
  bash scripts/run-sprint-01-task.sh "t${task}" --dry-run
done

printf '\n[PASS] Sprint-01 dry-run completed for t00 through t10.\n'
