#!/usr/bin/env python3
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any
import sys
import yaml

REQUIRED = {"objective", "context", "completion"}

def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise SystemExit(f"ERROR: Missing YAML file: {path}")
    payload = yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise SystemExit(f"ERROR: Expected YAML mapping: {path}")
    return payload

def replace_strings(value: Any, replacements: dict[str, str]) -> Any:
    if isinstance(value, str):
        result = value
        for old, new in replacements.items():
            result = result.replace(old, new)
        return result
    if isinstance(value, list):
        return [replace_strings(item, replacements) for item in value]
    if isinstance(value, dict):
        return {key: replace_strings(item, replacements) for key, item in value.items()}
    return value

def validate(payload: dict[str, Any], path: Path) -> None:
    missing = sorted(REQUIRED - set(payload))
    if missing:
        raise SystemExit(f"ERROR: {path} missing sections: " + ", ".join(missing))

def main() -> int:
    root = Path.cwd()
    canonical_path = root / "factory/prompt-manifests/s01-t00.yaml"
    canonical = load_yaml(canonical_path)
    validate(canonical, canonical_path)

    for index in range(1, 11):
        task = f"t{index:02d}"
        code = f"s01-{task}"
        task_path = root / "ai/manifests" / f"{code}.yaml"
        task_payload = load_yaml(task_path)

        objective = task_payload.get("objective")
        if not isinstance(objective, str) or not objective.strip():
            raise SystemExit(f"ERROR: Missing objective in {task_path}")

        payload = deepcopy(canonical)
        payload = replace_strings(
            payload,
            {
                "s01-t00": code,
                "S01-T00": code.upper(),
                "/t00/": f"/{task}/",
                "/t00": f"/{task}",
                "t00": task,
                "T00": task.upper(),
            },
        )
        payload["objective"] = objective.strip()

        target = root / "factory/prompt-manifests" / f"{code}.yaml"
        validate(payload, target)
        target.write_text(
            yaml.safe_dump(payload, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        print(f"Generated: {target.relative_to(root)}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
