#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

mapfile -t CANDIDATE_FILES < <(
  {
    git ls-files
    git ls-files --others --exclude-standard
  } | sort -u
)

forbidden_path_pattern='(^|/)(\.env|\.env\.[^.]+|id_rsa|id_dsa|id_ed25519|.*\.(pem|p12|pfx|key))$'
secret_pattern='(AKIA[0-9A-Z]{16}|ASIA[0-9A-Z]{16}|sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9_]{20,}|xox[baprs]-[A-Za-z0-9-]{20,}|-----BEGIN (RSA |DSA |EC |OPENSSH |)PRIVATE KEY-----|SECRET_ACCESS_KEY[[:space:]]*=[[:space:]]*[A-Za-z0-9/+=]{20,}|TOKEN[[:space:]]*=[[:space:]]*[A-Za-z0-9._-]{30,})'

violations=()

for file in "${CANDIDATE_FILES[@]}"; do
  [[ -f "${file}" ]] || continue

  if [[ "${file}" =~ ${forbidden_path_pattern} ]]; then
    case "${file}" in
      *.example|*.sample|factory/config/local-infra/.env.example)
        ;;
      *)
        violations+=("${file}: sensitive filename is tracked or unignored")
        ;;
    esac
  fi

  if LC_ALL=C grep -Iq . "${file}" \
    && grep -nE "${secret_pattern}" "${file}" >/tmp/ysim-secret-hygiene-match.$$ 2>/dev/null; then
    while IFS= read -r match; do
      line_number="${match%%:*}"
      violations+=("${file}:${line_number}: high-confidence secret pattern")
    done < /tmp/ysim-secret-hygiene-match.$$
    rm -f /tmp/ysim-secret-hygiene-match.$$
  fi
done

rm -f /tmp/ysim-secret-hygiene-match.$$

if (( ${#violations[@]} > 0 )); then
  printf '[FAIL] Secret hygiene check found potential secrets:\n' >&2
  printf '  %s\n' "${violations[@]}" >&2
  exit 1
fi

printf '[PASS] Secret hygiene check found no high-confidence secrets.\n'
