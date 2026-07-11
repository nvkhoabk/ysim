#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(git -C "${SCRIPT_DIR}" rev-parse --show-toplevel 2>/dev/null || git rev-parse --show-toplevel)"
DOCUMENT_INDEX="${REPO_ROOT}/factory/index/documents.json"
GENERATOR="${REPO_ROOT}/tools/knowledge/generate-knowledge.py"
SUMMARY="${REPO_ROOT}/knowledge/catalog/summary.json"
REPORT_DIR="${REPO_ROOT}/factory/reports/s00"
REPORT_FILE="${REPORT_DIR}/step-07-knowledge-factory.md"

log() { printf '[build-knowledge] %s\n' "$*"; }
fail() { printf '[build-knowledge] ERROR: %s\n' "$*" >&2; exit 1; }
require_command() { command -v "$1" >/dev/null 2>&1 || fail "Required command not found: $1"; }
require_file() { [[ -f "$1" ]] || fail "Required file not found: ${1#${REPO_ROOT}/}"; }
validate_json() { require_file "$1"; jq empty "$1" || fail "Invalid JSON: ${1#${REPO_ROOT}/}"; }

cd "${REPO_ROOT}"
require_command python3
require_command jq
require_command git
require_file "${GENERATOR}"
require_file "${DOCUMENT_INDEX}"

log "Validating Python syntax"
python3 -m py_compile "${GENERATOR}"

log "Generating knowledge catalogs"
python3 "${GENERATOR}" \
  --repo-root "${REPO_ROOT}" \
  --input "${DOCUMENT_INDEX}" \
  --output "${REPO_ROOT}/knowledge"

files=(
  "${REPO_ROOT}/knowledge/raw/documents.json"
  "${REPO_ROOT}/knowledge/normalized/documents.json"
  "${REPO_ROOT}/knowledge/catalog/documents.json"
  "${REPO_ROOT}/knowledge/catalog/document-sets.json"
  "${REPO_ROOT}/knowledge/catalog/capabilities.json"
  "${REPO_ROOT}/knowledge/catalog/integrations.json"
  "${REPO_ROOT}/knowledge/catalog/relationships.json"
  "${REPO_ROOT}/knowledge/catalog/knowledge-graph.json"
  "${REPO_ROOT}/knowledge/catalog/summary.json"
)

log "Validating generated JSON"
for file in "${files[@]}"; do validate_json "${file}"; done

status="$(jq -r '.status' "${SUMMARY}")"
null_codes="$(jq -r '.nullGovernedDocumentCodes' "${SUMMARY}")"
[[ "${status}" == "PASS" ]] || fail "Knowledge summary status is ${status}"
[[ "${null_codes}" == "0" ]] || fail "Found ${null_codes} governed document(s) without documentCode"

mkdir -p "${REPORT_DIR}"
cat > "${REPORT_FILE}" <<EOF
# Sprint-00 Step 7 — Knowledge Factory Commissioning

Generated at: $(date --iso-8601=seconds)

## Result

\`\`\`json
$(jq '{status, documentCount, documentSetCount, capabilityCount, integrationCount, relationshipCount, nullGovernedDocumentCodes, documentsBySet}' "${SUMMARY}")
\`\`\`

## Generated Catalogs

- \`knowledge/raw/documents.json\`
- \`knowledge/normalized/documents.json\`
- \`knowledge/catalog/documents.json\`
- \`knowledge/catalog/document-sets.json\`
- \`knowledge/catalog/capabilities.json\`
- \`knowledge/catalog/integrations.json\`
- \`knowledge/catalog/relationships.json\`
- \`knowledge/catalog/knowledge-graph.json\`
- \`knowledge/catalog/summary.json\`

## Limitation

Capability and integration relationships are generated from deterministic title and document-code matching. They are bootstrap knowledge and require review before being treated as authoritative semantic knowledge.

## Source of Truth

The Markdown documents under \`docs/\` remain authoritative.
EOF

log "Checking repository diff"
git diff --check

log "Knowledge Factory PASS"
jq '{status, documentCount, capabilityCount, integrationCount, relationshipCount}' "${SUMMARY}"
