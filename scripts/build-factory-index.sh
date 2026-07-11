#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

bash tools/indexing/build-document-index.sh
bash tools/indexing/build-knowledge-index.sh
bash tools/indexing/build-master-catalog.sh

printf '\nFactory index generated successfully.\n'
