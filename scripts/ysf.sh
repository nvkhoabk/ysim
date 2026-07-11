#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
VENV_PATH="${REPO_ROOT}/../.venv-ysf"

if [[ ! -x "${VENV_PATH}/bin/ysf" ]]; then
  printf 'ERROR: YSF virtual environment is not installed at %s\n' \
    "${VENV_PATH}" >&2
  printf 'Run: python3 -m pip install -e "%s/tools/ysf[dev]"\n' \
    "${REPO_ROOT}" >&2
  exit 4
fi

exec "${VENV_PATH}/bin/ysf" "$@"
