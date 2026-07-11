#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


REQUIRED_FIELDS = (
    "document_code",
    "document_name",
    "project",
    "document_set",
    "version",
    "status",
    "language",
)

ALLOWED_STATUS = {
    "DRAFT",
    "REVIEW",
    "APPROVED",
    "FROZEN",
    "DEPRECATED",
    "ARCHIVED",
}

SKIP_FILES = {
    "INDEX.md",
    "MASTER_INDEX.md"
}

def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8-sig")

    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        return {}

    metadata: dict[str, str] = {}

    for line in lines[1:]:
        if line.strip() == "---":
            break

        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("\"'")

    return metadata


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    docs_dir = repo_root / "docs"
    output_dir = repo_root / "factory" / "reports" / "s00"
    output_dir.mkdir(parents=True, exist_ok=True)

    json_output = output_dir / "documentation-metadata-validation.json"
    md_output = output_dir / "documentation-metadata-validation.md"

    files = sorted(docs_dir.rglob("*.md"))

    records: list[dict[str, object]] = []
    code_locations: dict[str, list[str]] = defaultdict(list)

    error_count = 0
    warning_count = 0

    for path in files:
        if path.name in SKIP_FILES:
            continue

        relative_path = path.relative_to(repo_root).as_posix()
        metadata = parse_frontmatter(path)

        errors: list[str] = []
        warnings: list[str] = []

        missing_fields = [
            field for field in REQUIRED_FIELDS if not metadata.get(field)
        ]

        if missing_fields:
            errors.append(
                "Missing metadata: " + ", ".join(missing_fields)
            )

        document_code = metadata.get("document_code", "")

        if document_code:
            code_locations[document_code].append(relative_path)

            filename_stem = path.stem
            if filename_stem != document_code:
                warnings.append(
                    f"Filename '{filename_stem}' differs from "
                    f"document_code '{document_code}'"
                )

        status = metadata.get("status", "")
        if status and status not in ALLOWED_STATUS:
            warnings.append(f"Unknown status: {status}")

        project = metadata.get("project", "")
        if project and project != "YSim v2.1":
            warnings.append(
                f"Legacy project metadata retained: {project}"
            )

        version = metadata.get("version", "")
        if version and version != "2.1":
            warnings.append(
                f"Legacy document version retained: {version}"
            )

        error_count += len(errors)
        warning_count += len(warnings)

        records.append(
            {
                "path": relative_path,
                "metadata": metadata,
                "errors": errors,
                "warnings": warnings,
            }
        )

    duplicate_codes = {
        code: locations
        for code, locations in code_locations.items()
        if len(locations) > 1
    }

    for code, locations in duplicate_codes.items():
        error_count += 1
        records.append(
            {
                "path": None,
                "metadata": {"document_code": code},
                "errors": [
                    "Duplicate document_code found in: "
                    + ", ".join(locations)
                ],
                "warnings": [],
            }
        )

    result = {
        "schemaVersion": "1.0",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "documentCount": len(files),
        "errorCount": error_count,
        "warningCount": warning_count,
        "duplicateDocumentCodes": duplicate_codes,
        "documents": records,
    }

    json_output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# Sprint-00 Documentation Metadata Validation",
        "",
        f"- Documents: {len(files)}",
        f"- Errors: {error_count}",
        f"- Warnings: {warning_count}",
        "",
        "## Errors",
        "",
    ]

    error_records = [
        record for record in records if record["errors"]
    ]

    if not error_records:
        lines.append("No errors.")
    else:
        for record in error_records:
            lines.append(f"### {record['path'] or 'Global'}")
            for error in record["errors"]:
                lines.append(f"- {error}")
            lines.append("")

    lines.extend(
        [
            "## Warnings",
            "",
        ]
    )

    warning_records = [
        record for record in records if record["warnings"]
    ]

    if not warning_records:
        lines.append("No warnings.")
    else:
        for record in warning_records:
            lines.append(f"### {record['path']}")
            for warning in record["warnings"]:
                lines.append(f"- {warning}")
            lines.append("")

    md_output.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )

    print(
        f"Validated {len(files)} documents: "
        f"{error_count} error(s), {warning_count} warning(s)."
    )
    print(md_output.relative_to(repo_root))

    return 1 if error_count else 0


if __name__ == "__main__":
    sys.exit(main())
