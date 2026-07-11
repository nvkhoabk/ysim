#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
INDEX_DIR="${REPO_ROOT}/factory/index"
OUTPUT_FILE="${INDEX_DIR}/catalog.json"

DOCUMENT_INDEX="${INDEX_DIR}/documents.json"
KNOWLEDGE_INDEX="${INDEX_DIR}/knowledge.json"

[[ -f "${DOCUMENT_INDEX}" ]] || {
  printf 'Missing %s\n' "${DOCUMENT_INDEX}" >&2
  exit 1
}

[[ -f "${KNOWLEDGE_INDEX}" ]] || {
  printf 'Missing %s\n' "${KNOWLEDGE_INDEX}" >&2
  exit 1
}

jq -n \
  --arg schemaVersion "1.0" \
  --arg generatedAt "$(date --iso-8601=seconds)" \
  --slurpfile documents "${DOCUMENT_INDEX}" \
  --slurpfile knowledge "${KNOWLEDGE_INDEX}" \
  '{
    schemaVersion: $schemaVersion,
    generatedAt: $generatedAt,
    project: "YSim",
    factoryVersion: "2.1",
    sources: {
      documentation: {
        index: "factory/index/documents.json",
        count: $documents[0].documentCount
      },
      knowledge: {
        index: "factory/index/knowledge.json",
        count: $knowledge[0].knowledgeCount
      }
    }
  }' > "${OUTPUT_FILE}"

jq empty "${OUTPUT_FILE}"

printf 'Generated %s\n' "${OUTPUT_FILE#${REPO_ROOT}/}"
