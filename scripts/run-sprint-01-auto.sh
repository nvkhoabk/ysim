#!/usr/bin/env bash
set -euo pipefail

export GIT_PAGER=cat
export PAGER=cat
export LESS=-FRX

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

START_TASK="${START_TASK:-01}"
END_TASK="${END_TASK:-10}"
MAX_REPAIR_ATTEMPTS="${MAX_REPAIR_ATTEMPTS:-1}"
AUTO_PUSH="${AUTO_PUSH:-0}"
CODEX_SANDBOX="${CODEX_SANDBOX:-workspace-write}"

YSF="./scripts/ysf.sh"
LOG_ROOT="runtime/auto-runner/s01"
mkdir -p "$LOG_ROOT" factory/reports/s01

task_name() {
  case "$1" in
    00) echo "Repository Audit and Execution Plan" ;;
    01) echo "Monorepo and Workspace Foundation" ;;
    02) echo "NestJS API Bootstrap" ;;
    03) echo "Configuration and Environment Validation" ;;
    04) echo "Logging, Correlation, Errors, and Diagnostics" ;;
    05) echo "Local Infrastructure Baseline" ;;
    06) echo "BullMQ, Scheduler and Background Runtime Foundation" ;;
    07) echo "Health, Readiness, OpenAPI and Operational Endpoints" ;;
    08) echo "Frontend Shells, Design Tokens and Shared UI" ;;
    09) echo "Quality Gates, CI and Validation" ;;
    10) echo "Sprint Review, Evidence and Acceptance" ;;
  esac
}

commit_message() {
  case "$1" in
    01) echo "feat(s01-t01): establish monorepo workspace foundation" ;;
    02) echo "feat(s01-t02): bootstrap NestJS API application" ;;
    03) echo "feat(s01-t03): add typed configuration and environment validation" ;;
    04) echo "feat(s01-t04): add structured logging and platform error handling" ;;
    05) echo "feat(s01-t05): establish local infrastructure baseline" ;;
    06) echo "feat(s01-t06): add background runtime foundation" ;;
    07) echo "feat(s01-t07): add operational endpoints and OpenAPI" ;;
    08) echo "feat(s01-t08): add frontend shells and shared UI foundation" ;;
    09) echo "test(s01-t09): add quality gates and CI validation" ;;
    10) echo "chore(s01-t10): complete Sprint-01 acceptance" ;;
  esac
}

is_done() {
  git rev-parse "s01-t$1-complete" >/dev/null 2>&1
}

is_generated_path() {
  local path="$1"

  case "${path}" in
    factory/index/*)
      return 0
      ;;
    factory/contexts/generated/*)
      return 0
      ;;
    factory/prompts/generated/*)
      return 0
      ;;
    factory/executions/s00/*)
      return 0
      ;;
    knowledge/catalog/*)
      return 0
      ;;
    knowledge/normalized/*)
      return 0
      ;;
    runtime/*)
      return 0
      ;;
    logs/*)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}


require_clean_tree() {
  local line
  local path
  local source_changes=()

  while IFS= read -r line; do
    [[ -z "${line}" ]] && continue

    path="${line:3}"

    # Handle rename output: old -> new
    if [[ "${path}" == *" -> "* ]]; then
      path="${path##* -> }"
    fi

    if is_generated_path "${path}"; then
      continue
    fi

    source_changes+=("${line}")
  done < <(
    git status \
      --porcelain=v1 \
      --untracked-files=all
  )

  if (( ${#source_changes[@]} > 0 )); then
    echo "ERROR: Source working tree must be clean." >&2
    printf '%s\n' "${source_changes[@]}" >&2
    exit 10
  fi

  echo "[PASS] Source working tree is clean."
}

build_context() {
  if [[ ! -f factory/contexts/generated/s01/context.json ]]; then
    bash scripts/build-sprint-01-context.sh
  fi
  jq empty factory/contexts/generated/s01/context.json
}

build_prompt() {
  local task="$1"
  rm -rf "factory/prompts/generated/s01/t${task}"
  bash scripts/build-sprint-01-prompt.sh "t${task}"
  test -f "factory/prompts/generated/s01/t${task}/prompt.md"
  jq empty "factory/prompts/generated/s01/t${task}/prompt.json"
}

run_codex() {
  local task="$1" attempt="$2" repair="$3"
  local dir="${LOG_ROOT}/t${task}/attempt-${attempt}"
  local prompt="factory/prompts/generated/s01/t${task}/prompt.md"
  mkdir -p "$dir"

  {
    cat "$prompt"
    echo
    echo "Runner constraints:"
    echo "- Complete only S01-T${task}."
    echo "- Do not start later tasks."
    echo "- Use ./scripts/ysf.sh, not a bare ysf command."
    echo "- Do not commit; the runner commits after validation."
    echo "- Do not modify frozen docs under docs/BRD, docs/ABP, docs/AFM, docs/YADF, docs/DIP, docs/UXF, docs/CAP, docs/ECS, docs/PCS, or docs/POL."
    echo "- Keep Storefront isolated from suppliers."
    if [[ "$repair" == "1" ]]; then
      echo "- Repair only failures listed in ${LOG_ROOT}/t${task}/validation.log."
    fi
  } > "$dir/instruction.md"

  set +e
  codex exec \
    --sandbox "$CODEX_SANDBOX" \
    -C "$REPO_ROOT" \
    -o "$dir/last-message.txt" \
    - \
    < "$dir/instruction.md" \
    > "$dir/stdout.txt" \
    2> >(tee "$dir/stderr.txt" >&2)
  local status=$?
  set -e

  printf '%s\n' "$status" > "$dir/exit-code.txt"
  return "$status"
}

check_protected_paths() {
  local changed
  changed="$(git status --porcelain=v1 | awk '{print $2}')"
  local path
  for path in \
    docs/BRD/ docs/ABP/ docs/AFM/ docs/YADF/ docs/DIP/ \
    docs/UXF/ docs/CAP/ docs/ECS/ docs/PCS/ docs/POL/; do
    if grep -q "^${path}" <<< "$changed"; then
      echo "ERROR: Protected path modified: $path" >&2
      return 1
    fi
  done
}

check_supplier_leakage() {
  local dirs=()
  [[ -d apps/storefront-web ]] && dirs+=(apps/storefront-web)
  [[ -d packages/ui ]] && dirs+=(packages/ui)
  [[ -d packages/runtime-context ]] && dirs+=(packages/runtime-context)

  if (( ${#dirs[@]} > 0 )); then
    if grep -RInE 'supplier(Id|Code|Product|Mapping|Gateway)?' "${dirs[@]}" 2>/dev/null; then
      echo "ERROR: Supplier reference detected in Storefront/UI scope." >&2
      return 1
    fi
  fi
}

run_workspace_quality() {
  if [[ -f package.json ]]; then
    pnpm install
    pnpm -r --if-present run lint
    pnpm -r --if-present run typecheck
    pnpm -r --if-present run test
    pnpm -r --if-present run build
  fi
}

validate_task() {
  local task="$1"
  local log="${LOG_ROOT}/t${task}/validation.log"

  set +e
  {
    git diff --check
    check_protected_paths
    check_supplier_leakage
    run_workspace_quality
    if [[ "$task" == "05" ]] && \
       [[ -f docker-compose.yml || -f compose.yml || -f compose.yaml ]]; then
      docker compose config
    fi
    "$YSF" verify
  } 2>&1 | tee "$log"
  local status=${PIPESTATUS[0]}
  set -e
  return "$status"
}

commit_task() {
  local task="$1"
  local message
  message="$(commit_message "$task")"

  cat > "factory/reports/s01/s01-t${task}-runner-evidence.md" <<EOF
# Sprint-01 Auto Runner Evidence — S01-T${task}

- Task: $(task_name "$task")
- Branch: $(git branch --show-current)
- Validation: PASS
- Codex sandbox: ${CODEX_SANDBOX}
- Generated at: $(date --iso-8601=seconds)
EOF

  git add -A

  git restore --staged \
    runtime \
    logs \
    factory/index \
    factory/contexts/generated \
    factory/prompts/generated \
    factory/executions/s00 \
    knowledge/catalog \
    knowledge/normalized \
    2>/dev/null || true
  git diff --cached --check

  if ! git diff --cached --quiet; then
    git commit -m "$message"
  fi

git restore \
  factory/index \
  factory/contexts/generated/s00 \
  factory/prompts/generated/s00 \
  factory/executions/s00 \
  knowledge/catalog \
  knowledge/normalized \
  2>/dev/null || true


  git tag -a "s01-t${task}-complete" \
    -m "Sprint-01 task T${task} complete"

  if [[ "$AUTO_PUSH" == "1" ]]; then
    git push
    git push origin "s01-t${task}-complete"
  fi
}

run_task() {
  local task="$1" attempt=1

  echo
  echo "===================================================="
  echo "S01-T${task}: $(task_name "$task")"
  echo "===================================================="

  build_prompt "$task"

  if ! run_codex "$task" "$attempt" 0; then
    echo "ERROR: Codex failed for S01-T${task}." >&2
    exit 20
  fi

  while ! validate_task "$task"; do
    if (( attempt > MAX_REPAIR_ATTEMPTS )); then
      echo "ERROR: Validation failed after repair limit." >&2
      exit 21
    fi
    attempt=$((attempt + 1))
    echo "Validation failed; automatic repair attempt ${attempt}..."
    run_codex "$task" "$attempt" 1 || exit 22
  done

  commit_task "$task"
  echo "[PASS] S01-T${task}"
}

main() {
  require_clean_tree
  bash scripts/validate-sprint-01-pack.sh
  "$YSF" verify
  build_context

  local start=$((10#$START_TASK))
  local end=$((10#$END_TASK))
  local i task

  for i in $(seq "$start" "$end"); do
    task="$(printf '%02d' "$i")"
    if is_done "$task"; then
      echo "Skipping S01-T${task}: completion tag exists."
      continue
    fi
    run_task "$task"
  done

  "$YSF" verify
  git diff --check
  echo "[PASS] Sprint-01 auto-run completed."
}

main "$@"
