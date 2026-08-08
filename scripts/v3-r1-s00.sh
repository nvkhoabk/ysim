#!/usr/bin/env bash
set -Eeuo pipefail
umask 027

MODE="${1:-}"
if [[ -z "$MODE" ]]; then
  printf '%s\n' \
    'USAGE=scripts/v3-r1-s00.sh {preflight|verify|known-bad|build-candidate|verify-candidate} [candidate-path]' >&2
  exit 2
fi
shift

REPOSITORY_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  printf '%s\n' 'RESULT=FAIL_REPOSITORY_ROOT' >&2
  exit 1
}
cd "$REPOSITORY_ROOT"

export PYTHONPATH="$REPOSITORY_ROOT/tools/ysf/src"
export PYTHONDONTWRITEBYTECODE=1
OUTPUT_ROOT="${YSF_S00_OUTPUT_ROOT:-}"
if [[ -z "$OUTPUT_ROOT" ]]; then
  OUTPUT_ROOT="$(mktemp -d /tmp/ysim-v3-r1-s00-output.XXXXXX)"
fi

run_factory() {
  python3 -m ysf.secure_factory.cli \
    "$@" \
    --output-root "$OUTPUT_ROOT" \
    --json
}

run_quality_gates_in_isolated_copy() (
  local validation_parent validation_repository

  validation_parent="$(
    mktemp -d /tmp/ysim-v3-r1-s00-validation.XXXXXX
  )"
  trap 'rm -rf -- "$validation_parent"' EXIT
  validation_repository="${validation_parent}/repository"
  cp -a -- "$REPOSITORY_ROOT" "$validation_repository"

  (
    cd "${validation_repository}/tools/ysf"
    python3 -m ruff check src/ysf tests
    python3 -m mypy src/ysf
    python3 -m pytest tests \
      --cov=ysf.secure_factory \
      --cov-branch \
      --cov-report=term-missing \
      --cov-fail-under=90
    python3 -m bandit -q -r src/ysf --severity-level medium
    python3 -m pip_audit \
      --require-hashes \
      --no-deps \
      -r requirements-s00-dev.lock
  )

)

case "$MODE" in
  preflight)
    [[ "$#" -eq 0 ]] || exit 2
    exec python3 -m ysf.secure_factory.cli \
      preflight --output-root "$OUTPUT_ROOT" --json
    ;;
  known-bad)
    [[ "$#" -eq 0 ]] || exit 2
    exec python3 -m ysf.secure_factory.cli \
      known-bad --output-root "$OUTPUT_ROOT" --json
    ;;
  verify)
    [[ "$#" -eq 0 ]] || exit 2
    run_factory verify
    run_quality_gates_in_isolated_copy
    printf '%s\n' 'RESULT=PASS_S00_VERIFY'
    ;;
  build-candidate)
    [[ "$#" -eq 0 ]] || exit 2
    exec python3 -m ysf.secure_factory.cli \
      build-candidate --output-root "$OUTPUT_ROOT" --json
    ;;
  verify-candidate)
    [[ "$#" -eq 1 ]] || exit 2
    CANDIDATE_PATH="$1"
    exec python3 -m ysf.secure_factory.cli \
      verify-candidate "$CANDIDATE_PATH" --output-root "$OUTPUT_ROOT" --json
    ;;
  *)
    printf 'RESULT=FAIL_UNSUPPORTED_MODE:%s\n' "$MODE" >&2
    exit 2
    ;;
esac
