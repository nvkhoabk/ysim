#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = (
    "document_code",
    "document_name",
    "project",
    "document_set",
    "version",
    "status",
    "language",
)

ALLOWED_STATUSES = {
    "DRAFT",
    "REVIEW",
    "APPROVED",
    "FROZEN",
    "DEPRECATED",
    "ARCHIVED",
}

NAVIGATION_FILES = {
    "docs/INDEX.md",
    "docs/MASTER_INDEX.md",
}

GOVERNED_DOCUMENT_SETS = {
    "AAP",
    "ABP",
    "AFM",
    "BRD",
    "DIP",
    "ESP",
    "ESPK",
    "ROP",
    "SGP",
    "YADF",
}


def read_text(path: Path) -> str:
    """
    utf-8-sig removes a UTF-8 BOM when present.
    splitlines() handles LF, CRLF and CR safely.
    """
    return path.read_text(encoding="utf-8-sig")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = read_text(path)
    lines = text.splitlines()

    if not lines:
        return {}

    if lines[0].strip() != "---":
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

    if not closing_marker_found:
        return {}

    return metadata


def extract_title(path: Path) -> str | None:
    text = read_text(path)

    for line in text.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)

        if match:
            return match.group(1).strip()

    return None


def relative_path(path: Path, repo_root: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def document_set_for(path: Path, docs_root: Path) -> str:
    relative = path.relative_to(docs_root)

    if len(relative.parts) == 1:
        return "ROOT"

    return relative.parts[0]


def is_navigation_file(path: Path, repo_root: Path) -> bool:
    return relative_path(path, repo_root) in NAVIGATION_FILES


def is_governed_document(path: Path, docs_root: Path) -> bool:
    document_set = document_set_for(path, docs_root)
    return document_set in GOVERNED_DOCUMENT_SETS


def normalize_filename_code(path: Path) -> str:
    return path.stem


def metadata_record(
    path: Path,
    repo_root: Path,
    docs_root: Path,
) -> dict[str, Any]:
    metadata = parse_frontmatter(path)

    return {
        "path": relative_path(path, repo_root),
        "filename": path.name,
        "extension": path.suffix.lstrip("."),
        "documentSet": document_set_for(path, docs_root),
        "documentCode": metadata.get("document_code") or None,
        "documentName": metadata.get("document_name") or None,
        "title": extract_title(path),
        "project": metadata.get("project") or None,
        "version": metadata.get("version") or None,
        "status": metadata.get("status") or None,
        "language": metadata.get("language") or None,
        "generatedNavigation": is_navigation_file(path, repo_root),
    }
