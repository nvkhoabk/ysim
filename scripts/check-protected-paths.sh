#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

PROTECTED_PATHS=(
  "docs/BRD/"
  "docs/ABP/"
  "docs/AFM/"
  "docs/YADF/"
  "docs/DIP/"
  "docs/UXF/"
  "docs/CAP/"
  "docs/ECS/"
  "docs/PCS/"
  "docs/POL/"
)

mapfile -t CHANGED_FILES < <(
  {
    git diff --name-only
    git diff --cached --name-only
    git ls-files --others --exclude-standard
  } | sort -u
)

violations=()

for file in "${CHANGED_FILES[@]}"; do
  for protected_path in "${PROTECTED_PATHS[@]}"; do
    if [[ "${file}" == "${protected_path}"* ]]; then
      violations+=("${file}")
      break
    fi
  done
done

if (( ${#violations[@]} > 0 )); then
  printf '[FAIL] Protected architecture paths were modified:\n' >&2
  printf '  %s\n' "${violations[@]}" >&2
  exit 1
fi

printf '[PASS] Protected architecture paths are unchanged.\n'
