#!/usr/bin/env bash

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

LOG_DIR="${REPO_ROOT}/runtime/reports/quality-gates"
mkdir -p "${LOG_DIR}"

STAGE_NAMES=()
STAGE_STATUSES=()
STAGE_DETAILS=()
FAILED=0

record_stage() {
  local name="$1"
  local status="$2"
  local detail="$3"

  STAGE_NAMES+=("${name}")
  STAGE_STATUSES+=("${status}")
  STAGE_DETAILS+=("${detail}")

  if [[ "${status}" == "FAIL" ]]; then
    FAILED=1
  fi
}

run_stage() {
  local name="$1"
  shift

  local log_file="${LOG_DIR}/${name}.log"
  printf '\n==> %s\n' "${name}"
  printf '$ %s\n' "$*" > "${log_file}"

  if "$@" >> "${log_file}" 2>&1; then
    record_stage "${name}" "PASS" "${log_file}"
    printf '[PASS] %s\n' "${name}"
  else
    local exit_code=$?
    record_stage "${name}" "FAIL" "${log_file} (exit ${exit_code})"
    printf '[FAIL] %s (exit %s)\n' "${name}" "${exit_code}" >&2
    tail -n 40 "${log_file}" >&2
  fi
}

skip_stage() {
  local name="$1"
  local reason="$2"

  record_stage "${name}" "SKIP" "${reason}"
  printf '[SKIP] %s: %s\n' "${name}" "${reason}"
}

run_node_stage() {
  local name="$1"
  shift

  if [[ ! -f package.json || ! -f pnpm-workspace.yaml ]]; then
    skip_stage "${name}" "No root package.json and pnpm-workspace.yaml are present in this checkout."
    return
  fi

  if ! command -v pnpm >/dev/null 2>&1; then
    record_stage "${name}" "FAIL" "pnpm is not installed or not on PATH."
    printf '[FAIL] %s: pnpm is not installed or not on PATH.\n' "${name}" >&2
    return
  fi

  run_stage "${name}" pnpm "$@"
}

printf '# YSim Platform Quality Gate\n'
printf 'Repository: %s\n' "${REPO_ROOT}"
printf 'Logs: %s\n' "${LOG_DIR}"

run_stage "repository-doctor" ./scripts/ysf.sh doctor

if [[ -f package.json && -f pnpm-lock.yaml ]]; then
  run_node_stage "install" install --frozen-lockfile
elif [[ -f package.json ]]; then
  run_node_stage "install" install
else
  skip_stage "install" "No root package.json is present in this checkout."
fi

run_node_stage "workspace-lint" -r --if-present run lint
run_node_stage "workspace-typecheck" -r --if-present run typecheck
run_node_stage "workspace-tests" -r --if-present run test
run_node_stage "workspace-build" -r --if-present run build

run_stage "ysf-verify" ./scripts/ysf.sh verify
run_stage "infrastructure-static" ./scripts/ysf.sh local-infra verify
run_stage "infrastructure-compose" ./scripts/ysf.sh local-infra verify --runtime
run_stage "protected-paths" bash scripts/check-protected-paths.sh
run_stage "supplier-boundary" bash scripts/check-supplier-boundary.sh
run_stage "secret-hygiene" bash scripts/check-secret-hygiene.sh
run_stage "diff-whitespace" git diff --check

printf '\n# Quality Gate Summary\n'
printf '%-24s %-6s %s\n' "Stage" "Status" "Detail"
printf '%-24s %-6s %s\n' "-----" "------" "------"

for index in "${!STAGE_NAMES[@]}"; do
  printf '%-24s %-6s %s\n' \
    "${STAGE_NAMES[${index}]}" \
    "${STAGE_STATUSES[${index}]}" \
    "${STAGE_DETAILS[${index}]}"
done

if (( FAILED != 0 )); then
  printf '\n[FAIL] Platform quality gate failed. Inspect the stage log paths above.\n' >&2
  exit 1
fi

printf '\n[PASS] Platform quality gate completed successfully.\n'
