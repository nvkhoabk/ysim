from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any


class RepositorySnapshotError(RuntimeError):
    """Raised when repository information cannot be collected."""


def run_git(
    repository_root: Path,
    arguments: list[str],
) -> str:
    process = subprocess.run(
        ["git", *arguments],
        cwd=repository_root,
        capture_output=True,
        text=True,
        check=False,
    )

    if process.returncode != 0:
        message = (
            process.stderr.strip()
            or process.stdout.strip()
            or "Unknown Git error."
        )

        raise RepositorySnapshotError(message)

    return process.stdout.strip()


def build_repository_snapshot(
    repository_root: Path,
    configuration: dict[str, Any],
) -> str:
    sections: list[str] = []

    if configuration.get("include_branch", True):
        branch = run_git(
            repository_root,
            ["branch", "--show-current"],
        )

        sections.extend([
            "## Branch",
            "",
            branch or "(detached HEAD)",
            "",
        ])

    if configuration.get("include_status", True):
        status = run_git(
            repository_root,
            ["status", "--short"],
        )

        sections.extend([
            "## Working Tree",
            "",
            "```text",
            status or "clean",
            "```",
            "",
        ])

    commit_count = int(
        configuration.get(
            "include_recent_commits",
            10,
        )
    )

    commits = run_git(
        repository_root,
        [
            "log",
            "--oneline",
            "--decorate",
            f"-n{commit_count}",
        ],
    )

    sections.extend([
        "## Recent Commits",
        "",
        "```text",
        commits,
        "```",
        "",
    ])

    tree_depth = int(
        configuration.get(
            "include_tree_depth",
            2,
        )
    )

    process = subprocess.run(
        [
            "find",
            ".",
            "-maxdepth",
            str(tree_depth),
            "-not",
            "-path",
            "./.git*",
            "-print",
        ],
        cwd=repository_root,
        capture_output=True,
        text=True,
        check=False,
    )

    if process.returncode != 0:
        raise RepositorySnapshotError(
            process.stderr.strip()
            or "Cannot build repository tree."
        )

    tree_lines = sorted(
        line
        for line in process.stdout.splitlines()
        if line.strip()
    )

    sections.extend([
        "## Repository Tree",
        "",
        "```text",
        "\n".join(tree_lines),
        "```",
    ])

    return "\n".join(sections).strip()
