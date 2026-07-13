#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

TARGET_ROOTS=(
  "apps/storefront-web"
  "packages/ui"
  "packages/runtime-context"
  "packages/localization"
  "knowledge/ui"
)

supplier_pattern='(^|[^A-Za-z0-9_])(supplier|suppliers|gigago|onepay|gpay|providerSystem|providerProduct|providerMapping|providerRouting)([^A-Za-z0-9_]|$)'
files_to_scan=()

for root in "${TARGET_ROOTS[@]}"; do
  [[ -e "${root}" ]] || continue
  while IFS= read -r file; do
    [[ -f "${file}" ]] && files_to_scan+=("${file}")
  done < <(find "${root}" -type f | sort)
done

if (( ${#files_to_scan[@]} == 0 )); then
  printf '[SKIP] Supplier boundary check found no storefront/UI files to scan.\n'
  exit 0
fi

violations=()

for file in "${files_to_scan[@]}"; do
  if LC_ALL=C grep -Iq . "${file}" \
    && grep -niE "${supplier_pattern}" "${file}" >/tmp/ysim-supplier-boundary-match.$$ 2>/dev/null; then
    while IFS= read -r match; do
      line_number="${match%%:*}"
      violations+=("${file}:${line_number}: supplier/infrastructure term in storefront/UI boundary")
    done < /tmp/ysim-supplier-boundary-match.$$
    rm -f /tmp/ysim-supplier-boundary-match.$$
  fi
done

rm -f /tmp/ysim-supplier-boundary-match.$$

if (( ${#violations[@]} > 0 )); then
  printf '[FAIL] Storefront/UI supplier boundary violations found:\n' >&2
  printf '  %s\n' "${violations[@]}" >&2
  exit 1
fi

printf '[PASS] Storefront/UI supplier boundary is clean.\n'
