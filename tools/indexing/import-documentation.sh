#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
SOURCE_DIR="${1:-}"

if [[ -z "${SOURCE_DIR}" ]]; then
  printf 'Usage: %s <extracted-document-directory>\n' "$0" >&2
  exit 1
fi

if [[ ! -d "${SOURCE_DIR}" ]]; then
  printf 'Source directory does not exist: %s\n' "${SOURCE_DIR}" >&2
  exit 1
fi

SOURCE_DIR="$(cd "${SOURCE_DIR}" && pwd)"
DOCS_DIR="${REPO_ROOT}/docs"

DOCUMENT_SETS=(
  AAP
  ABP
  AFM
  BRD
  DIP
  ESP
  ESPK
  ROP
  SGP
  YADF
)

mkdir -p "${DOCS_DIR}"

for set_name in "${DOCUMENT_SETS[@]}"; do
  mkdir -p "${DOCS_DIR}/${set_name}"
done

copy_set_directory() {
  local set_name="$1"
  local source_set="${SOURCE_DIR}/${set_name}"
  local target_set="${DOCS_DIR}/${set_name}"

  if [[ -d "${source_set}" ]]; then
    find "${source_set}" \
      -maxdepth 1 \
      -type f \
      -name '*.md' \
      -exec cp -f {} "${target_set}/" \;
  fi
}

copy_root_documents() {
  local prefix="$1"
  local target_set="${DOCS_DIR}/${prefix}"

  find "${SOURCE_DIR}" \
    -maxdepth 1 \
    -type f \
    -name "${prefix}-*.md" \
    -exec cp -f {} "${target_set}/" \;
}

for set_name in AAP ABP AFM BRD DIP ESP ESPK ROP SGP YADF; do
  copy_set_directory "${set_name}"
done

# copy_root_documents AFM
# copy_root_documents YADF

printf 'Documentation imported into %s\n' "${DOCS_DIR}"
