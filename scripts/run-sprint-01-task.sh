#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

TASK="${1:-}"
shift || true

if [[ ! "${TASK}" =~ ^t(0[0-9]|10)$ ]]; then
  printf 'Usage: %s t00|t01|...|t10 [--dry-run]\n' "$0" >&2
  exit 2
fi

DRY_RUN=true

for arg in "$@"; do
  case "${arg}" in
    --dry-run)
      DRY_RUN=true
      ;;
    *)
      printf 'ERROR: Unsupported argument: %s\n' "${arg}" >&2
      exit 3
      ;;
  esac
done

bash scripts/validate-sprint-01-pack.sh
bash scripts/build-sprint-01-context.sh
bash scripts/build-sprint-01-prompt.sh "${TASK}"

PROMPT_ARTIFACT="factory/prompts/generated/s01/${TASK}/prompt.json"

[[ -f "${PROMPT_ARTIFACT}" ]] || {
  printf 'ERROR: Prompt artifact was not generated: %s\n' \
    "${PROMPT_ARTIFACT}" >&2
  exit 4
}

if [[ "${DRY_RUN}" == true ]]; then
  exec ./scripts/ysf.sh run \
    --provider codex \
    --prompt-artifact "${PROMPT_ARTIFACT}" \
    --execution-id "s01-${TASK}-dry-run" \
    --dry-run
fi

printf 'ERROR: Apply execution is intentionally disabled.\n' >&2
exit 5
