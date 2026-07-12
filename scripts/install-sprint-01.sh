#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

required=(
  "ai/sprints/s01-platform-foundation.yaml"
  "sprint.json"
  "SCOPE.md"
  "TARGET_STRUCTURE.md"
  "ACCEPTANCE.md"
  "EXECUTION_ORDER.md"
  "DOCUMENT_BASELINE.md"
  "GOVERNANCE.md"
  "factory/context-manifests/s01.yaml"
)

for path in "${required[@]}"; do
  if [[ ! -f "${path}" ]]; then
    printf 'ERROR: Missing required file: %s\n' "${path}" >&2
    exit 2
  fi
done

for task in $(seq -w 0 10); do
  manifest="ai/manifests/s01-t${task}.yaml"
  prompt="factory/prompt-manifests/s01-t${task}.yaml"

  [[ -f "${manifest}" ]] || {
    printf 'ERROR: Missing task manifest: %s\n' "${manifest}" >&2
    exit 3
  }

  [[ -f "${prompt}" ]] || {
    printf 'ERROR: Missing prompt manifest: %s\n' "${prompt}" >&2
    exit 4
  }
done

printf '[PASS] Sprint-01 files are installed.\n'
