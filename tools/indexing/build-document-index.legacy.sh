#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
DOCS_DIR="${REPO_ROOT}/docs"
OUTPUT_DIR="${REPO_ROOT}/factory/index"
OUTPUT_FILE="${OUTPUT_DIR}/documents.json"
TEMP_FILE="$(mktemp)"

cleanup() {
  rm -f "${TEMP_FILE}"
}
trap cleanup EXIT

mkdir -p "${OUTPUT_DIR}"

extract_frontmatter_value() {
  local file="$1"
  local key="$2"

  awk -v target="${key}" '
    BEGIN {
      in_frontmatter = 0
      frontmatter_seen = 0
    }

    NR == 1 && $0 == "---" {
      in_frontmatter = 1
      frontmatter_seen = 1
      next
    }

    in_frontmatter && $0 == "---" {
      exit
    }

    in_frontmatter {
      split($0, parts, ":")
      current_key = parts[1]

      if (current_key == target) {
        sub(/^[^:]*:[[:space:]]*/, "", $0)
        gsub(/^["'\'']|["'\'']$/, "", $0)
        print $0
        exit
      }
    }

    END {
      if (!frontmatter_seen) {
        exit 0
      }
    }
  ' "${file}"
}

extract_title() {
  local file="$1"

  awk '
    /^# / {
      sub(/^# /, "", $0)
      print $0
      exit
    }
  ' "${file}"
}

printf '[]' > "${TEMP_FILE}"

if [[ -d "${DOCS_DIR}" ]]; then
  while IFS= read -r -d '' file; do
    relative_path="${file#${REPO_ROOT}/}"
    filename="$(basename "${file}")"
    extension="${filename##*.}"

    relative_to_docs="${file#${DOCS_DIR}/}"

    if [[ "${relative_to_docs}" == "${file}" ]]; then
      document_set="UNKNOWN"
    elif [[ "${relative_to_docs}" == */* ]]; then
      document_set="${relative_to_docs%%/*}"
    else
      document_set="ROOT"
    fi

    document_code="$(extract_frontmatter_value "${file}" "document_code" || true)"
    version="$(extract_frontmatter_value "${file}" "version" || true)"
    status="$(extract_frontmatter_value "${file}" "status" || true)"
    title="$(extract_title "${file}" || true)"

    document_code="${document_code:-}"
    version="${version:-}"
    status="${status:-}"
    title="${title:-}"

    jq \
      --arg path "${relative_path}" \
      --arg filename "${filename}" \
      --arg extension "${extension}" \
      --arg documentSet "${document_set}" \
      --arg documentCode "${document_code}" \
      --arg title "${title}" \
      --arg version "${version}" \
      --arg status "${status}" \
      '. + [{
        path: $path,
        filename: $filename,
        extension: $extension,
        documentSet: $documentSet,
        documentCode: (if $documentCode == "" then null else $documentCode end),
        title: (if $title == "" then null else $title end),
        version: (if $version == "" then null else $version end),
        status: (if $status == "" then null else $status end)
      }]' \
      "${TEMP_FILE}" > "${TEMP_FILE}.next"

    mv "${TEMP_FILE}.next" "${TEMP_FILE}"
  done < <(
    find "${DOCS_DIR}" \
      -type f \
      \( -name '*.md' -o -name '*.yaml' -o -name '*.yml' -o -name '*.json' \) \
      -print0 |
      sort -z
  )
fi

document_count="$(jq 'length' "${TEMP_FILE}")"
generated_at="$(date --iso-8601=seconds)"

jq -n \
  --arg schemaVersion "1.0" \
  --arg generatedAt "${generated_at}" \
  --arg repositoryRoot "." \
  --argjson documentCount "${document_count}" \
  --slurpfile documents "${TEMP_FILE}" \
  '{
    schemaVersion: $schemaVersion,
    generatedAt: $generatedAt,
    repositoryRoot: $repositoryRoot,
    documentCount: $documentCount,
    documents: $documents[0]
  }' > "${OUTPUT_FILE}"

jq empty "${OUTPUT_FILE}"

printf 'Generated %s with %s document(s).\n' \
  "${OUTPUT_FILE#${REPO_ROOT}/}" \
  "${document_count}"
