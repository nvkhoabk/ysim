#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
KNOWLEDGE_DIR="${REPO_ROOT}/knowledge"
OUTPUT_DIR="${REPO_ROOT}/factory/index"
OUTPUT_FILE="${OUTPUT_DIR}/knowledge.json"
TEMP_FILE="$(mktemp)"

cleanup() {
  rm -f "${TEMP_FILE}"
}
trap cleanup EXIT

mkdir -p "${OUTPUT_DIR}"
printf '[]' > "${TEMP_FILE}"

if [[ -d "${KNOWLEDGE_DIR}" ]]; then
  while IFS= read -r -d '' file; do
    relative_path="${file#${REPO_ROOT}/}"
    filename="$(basename "${file}")"
    extension="${filename##*.}"

    relative_to_knowledge="${file#${KNOWLEDGE_DIR}/}"

    if [[ "${relative_to_knowledge}" == "${file}" ]]; then
      category="UNKNOWN"
    elif [[ "${relative_to_knowledge}" == */* ]]; then
      category="${relative_to_knowledge%%/*}"
    else
      category="ROOT"
    fi

    jq \
      --arg path "${relative_path}" \
      --arg filename "${filename}" \
      --arg extension "${extension}" \
      --arg category "${category}" \
      '. + [{
        path: $path,
        filename: $filename,
        extension: $extension,
        category: $category
      }]' \
      "${TEMP_FILE}" > "${TEMP_FILE}.next"

    mv "${TEMP_FILE}.next" "${TEMP_FILE}"
  done < <(
    find "${KNOWLEDGE_DIR}" \
      -type f \
      ! -name '.gitkeep' \
      \( -name '*.md' -o -name '*.yaml' -o -name '*.yml' -o -name '*.json' \) \
      -print0 |
      sort -z
  )
fi

knowledge_count="$(jq 'length' "${TEMP_FILE}")"
generated_at="$(date --iso-8601=seconds)"

jq -n \
  --arg schemaVersion "1.0" \
  --arg generatedAt "${generated_at}" \
  --arg repositoryRoot "." \
  --argjson knowledgeCount "${knowledge_count}" \
  --slurpfile entries "${TEMP_FILE}" \
  '{
    schemaVersion: $schemaVersion,
    generatedAt: $generatedAt,
    repositoryRoot: $repositoryRoot,
    knowledgeCount: $knowledgeCount,
    entries: $entries[0]
  }' > "${OUTPUT_FILE}"

jq empty "${OUTPUT_FILE}"

printf 'Generated %s with %s knowledge file(s).\n' \
  "${OUTPUT_FILE#${REPO_ROOT}/}" \
  "${knowledge_count}"
