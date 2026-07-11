from __future__ import annotations

import re
from pathlib import Path

NAVIGATION_FILES = {
    "docs/INDEX.md",
    "docs/MASTER_INDEX.md",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = read_text(path).splitlines()

    if not lines or lines[0].strip() != "---":
        return {}

    metadata: dict[str, str] = {}
    closing_marker_found = False

    for line in lines[1:]:
        stripped = line.strip()

        if stripped == "---":
            closing_marker_found = True
            break

        if not stripped or stripped.startswith("#"):
            continue

        if ":" not in line:
            continue

        key, value = line.split(":", 1)

        key = key.strip()
        value = value.strip()

        if (
            len(value) >= 2
            and value[0] == value[-1]
            and value[0] in {"'", '"'}
        ):
            value = value[1:-1]

        metadata[key] = value

    return metadata if closing_marker_found else {}


def extract_title(path: Path) -> str | None:
    for line in read_text(path).splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)

        if match:
            return match.group(1).strip()

    return None


def is_navigation_document(
    path: Path,
    repository_root: Path,
) -> bool:
    relative = path.relative_to(repository_root).as_posix()
    return relative in NAVIGATION_FILES
