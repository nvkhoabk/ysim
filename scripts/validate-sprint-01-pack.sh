#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

required=(
  "ai/sprints/s01-platform-foundation.yaml"
  "sprint.json"
  "SCOPE.md"
  "TARGET_STRUCTURE.md"
  "ACCEPTANCE.md"
  "EXECUTION_ORDER.md"
  "DOCUMENT_BASELINE.md"
  "GOVERNANCE.md"
  "factory/context-manifests/s01.yaml"
)

for path in "${required[@]}"; do
  [[ -f "${path}" ]] || {
    printf 'ERROR: Missing required file: %s\n' "${path}" >&2
    exit 2
  }
done

for task in $(seq -w 0 10); do
  [[ -f "ai/manifests/s01-t${task}.yaml" ]] || {
    printf 'ERROR: Missing task manifest: s01-t%s\n' "${task}" >&2
    exit 3
  }
  [[ -f "factory/prompt-manifests/s01-t${task}.yaml" ]] || {
    printf 'ERROR: Missing prompt manifest: s01-t%s\n' "${task}" >&2
    exit 4
  }
done

printf '[PASS] Sprint-01 files are installed.\n'

python3 - <<'PY'
from pathlib import Path
import json
import yaml

root = Path.cwd()

sprint = json.loads((root / "sprint.json").read_text(encoding="utf-8"))
assert sprint["sprintCode"] == "S01"
assert sprint["taskCount"] == 11
assert [item["code"] for item in sprint["tasks"]] == [
    f"s01-t{i:02d}" for i in range(11)
]
print("[PASS] sprint.json")

for index in range(11):
    code = f"s01-t{index:02d}"
    task_path = root / "ai/manifests" / f"{code}.yaml"
    task = yaml.safe_load(task_path.read_text(encoding="utf-8-sig"))
    assert task["task"]["code"] == code
    assert task["task"]["order"] == index
print("[PASS] task manifests")

required_sections = {"objective", "context", "completion"}

for index in range(11):
    code = f"s01-t{index:02d}"
    prompt_path = root / "factory/prompt-manifests" / f"{code}.yaml"
    prompt = yaml.safe_load(prompt_path.read_text(encoding="utf-8-sig"))
    missing = sorted(required_sections - set(prompt))
    if missing:
        raise AssertionError(
            f"{prompt_path}: missing sections: " + ", ".join(missing)
        )
    if not isinstance(prompt["objective"], str) or not prompt["objective"].strip():
        raise AssertionError(f"{prompt_path}: invalid objective")
print("[PASS] prompt manifests")
PY

git diff --check
printf '[PASS] Sprint-01 pack validation completed.\n'
