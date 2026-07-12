#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(git rev-parse --show-toplevel)"
MANIFEST="${1:-factory/prompt-manifests/s00-t00.yaml}"
cd "$REPO_ROOT"
python3 -m py_compile tools/prompt/build-prompt.py
python3 tools/prompt/build-prompt.py --repo-root "$REPO_ROOT" --manifest "$MANIFEST"
jq empty factory/prompts/generated/s00/t00/prompt.json >/dev/null
jq empty factory/prompts/generated/s00/t00/manifest.json >/dev/null
git diff --check
echo "Prompt Factory PASS"
