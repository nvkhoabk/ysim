from __future__ import annotations

import subprocess
from pathlib import Path


class RepositoryError(RuntimeError):
    """Raised when the YSim repository cannot be resolved."""


def find_repository_root(start: Path | None = None) -> Path:
    working_directory = (start or Path.cwd()).resolve()

    process = subprocess.run(
        ["git", "-C", str(working_directory), "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )

    if process.returncode != 0:
        message = process.stderr.strip() or "Not inside a Git repository."
        raise RepositoryError(message)

    root = Path(process.stdout.strip()).resolve()

    if not (root / "factory").is_dir():
        raise RepositoryError(
            f"Repository does not contain factory/: {root}"
        )

    if not (root / "docs").is_dir():
        raise RepositoryError(
            f"Repository does not contain docs/: {root}"
        )

    return root
