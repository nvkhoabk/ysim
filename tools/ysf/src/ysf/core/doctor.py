from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Any

from ysf.core.result import CommandResult

REQUIRED_COMMANDS = (
    "git",
    "python3",
    "jq",
)

OPTIONAL_COMMANDS = (
    "node",
    "pnpm",
    "docker",
    "codex",
)


def command_version(command: str) -> str | None:
    executable = shutil.which(command)

    if executable is None:
        return None

    process = subprocess.run(
        [executable, "--version"],
        capture_output=True,
        text=True,
        check=False,
    )

    output = process.stdout.strip() or process.stderr.strip()

    return output.splitlines()[0] if output else "available"


def run_doctor(repository_root: Path) -> CommandResult:
    tools: dict[str, Any] = {}
    missing_required: list[str] = []

    for command in REQUIRED_COMMANDS:
        version = command_version(command)
        tools[command] = version

        if version is None:
            missing_required.append(command)

    for command in OPTIONAL_COMMANDS:
        tools[command] = command_version(command)

    paths = {
        "docs": (repository_root / "docs").is_dir(),
        "factory": (repository_root / "factory").is_dir(),
        "knowledge": (repository_root / "knowledge").is_dir(),
        "scripts": (repository_root / "scripts").is_dir(),
        "documentIndex": (
            repository_root / "factory/index/documents.json"
        ).is_file(),
        "knowledgeSummary": (
            repository_root / "knowledge/catalog/summary.json"
        ).is_file(),
    }

    missing_paths = [
        name
        for name, exists in paths.items()
        if not exists
    ]

    status = (
        "PASS"
        if not missing_required and not missing_paths
        else "FAIL"
    )

    message = (
        "YSF environment is ready."
        if status == "PASS"
        else "YSF environment is incomplete."
    )

    return CommandResult(
        command="doctor",
        status=status,
        message=message,
        data={
            "repositoryRoot": str(repository_root),
            "tools": tools,
            "paths": paths,
            "missingRequiredTools": missing_required,
            "missingPaths": missing_paths,
        },
    )
