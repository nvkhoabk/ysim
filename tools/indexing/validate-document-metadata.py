#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from document_metadata import (
    ALLOWED_STATUSES,
    REQUIRED_FIELDS,
    extract_title,
    is_governed_document,
    is_navigation_file,
    normalize_filename_code,
    parse_frontmatter,
    relative_path,
)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    docs_root = repo_root / "docs"
    report_dir = repo_root / "factory" / "reports" / "s00"

    report_dir.mkdir(parents=True, exist_ok=True)

    json_output = (
        report_dir
        / "documentation-metadata-validation.json"
    )
    markdown_output = (
        report_dir
        / "documentation-metadata-validation.md"
    )

    files = sorted(docs_root.rglob("*.md"))

    errors: list[dict[str, object]] = []
    warnings: list[dict[str, object]] = []
    skipped: list[dict[str, object]] = []
    documents: list[dict[str, object]] = []

    code_locations: defaultdict[str, list[str]] = defaultdict(list)

    governed_count = 0
    navigation_count = 0

    for path in files:
        relative = relative_path(path, repo_root)

        if is_navigation_file(path, repo_root):
            navigation_count += 1

            skipped.append({
                "path": relative,
                "reason": "generated_navigation_document",
            })

            continue

        if not is_governed_document(path, docs_root):
            skipped.append({
                "path": relative,
                "reason": "unmanaged_document_set",
            })

            continue

        governed_count += 1
        metadata = parse_frontmatter(path)

        missing_fields = [
            field
            for field in REQUIRED_FIELDS
            if not metadata.get(field)
        ]

        if missing_fields:
            errors.append({
                "path": relative,
                "type": "missing_metadata",
                "fields": missing_fields,
            })

        document_code = metadata.get("document_code", "")

        if document_code:
            code_locations[document_code].append(relative)

            expected_code = normalize_filename_code(path)

            if document_code != expected_code:
                warnings.append({
                    "path": relative,
                    "type": "filename_code_mismatch",
                    "filenameCode": expected_code,
                    "documentCode": document_code,
                })

        status = metadata.get("status", "")

        if status and status not in ALLOWED_STATUSES:
            errors.append({
                "path": relative,
                "type": "invalid_status",
                "value": status,
            })

        project = metadata.get("project", "")

        if project and not project.startswith("YSim"):
            warnings.append({
                "path": relative,
                "type": "unexpected_project",
                "value": project,
            })

        version = metadata.get("version", "")

        if version and version != "2.1":
            warnings.append({
                "path": relative,
                "type": "legacy_document_version",
                "value": version,
            })

        title = extract_title(path)

        if not title:
            warnings.append({
                "path": relative,
                "type": "missing_h1_title",
            })

        documents.append({
            "path": relative,
            "documentCode": document_code or None,
            "documentName": metadata.get("document_name") or None,
            "documentSet": metadata.get("document_set") or None,
            "project": project or None,
            "version": version or None,
            "status": status or None,
            "language": metadata.get("language") or None,
            "title": title,
        })

    duplicate_codes: dict[str, list[str]] = {}

    for code, paths in sorted(code_locations.items()):
        if len(paths) > 1:
            duplicate_codes[code] = paths

            errors.append({
                "type": "duplicate_document_code",
                "documentCode": code,
                "paths": paths,
            })

    result = {
        "schemaVersion": "1.1",
        "generatedAt": datetime.now().astimezone().isoformat(),
        "status": "PASS" if not errors else "FAIL",
        "totalMarkdownCount": len(files),
        "governedDocumentCount": governed_count,
        "navigationDocumentCount": navigation_count,
        "skippedDocumentCount": len(skipped),
        "errorCount": len(errors),
        "warningCount": len(warnings),
        "duplicateDocumentCodes": duplicate_codes,
        "errors": errors,
        "warnings": warnings,
        "skipped": skipped,
        "documents": documents,
    }

    json_output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# Sprint-00 Documentation Metadata Validation",
        "",
        f"- Status: **{result['status']}**",
        f"- Total Markdown files: **{result['totalMarkdownCount']}**",
        f"- Governed documents: **{result['governedDocumentCount']}**",
        f"- Navigation documents: **{result['navigationDocumentCount']}**",
        f"- Errors: **{result['errorCount']}**",
        f"- Warnings: **{result['warningCount']}**",
        "",
        "## Errors",
        "",
    ]

    if errors:
        for error in errors:
            lines.append(
                "- `" + json.dumps(
                    error,
                    ensure_ascii=False,
                ) + "`"
            )
    else:
        lines.append("- None")

    lines.extend([
        "",
        "## Warnings",
        "",
    ])

    if warnings:
        for warning in warnings:
            lines.append(
                "- `" + json.dumps(
                    warning,
                    ensure_ascii=False,
                ) + "`"
            )
    else:
        lines.append("- None")

    lines.extend([
        "",
        "## Skipped Navigation Documents",
        "",
    ])

    if skipped:
        for entry in skipped:
            lines.append(
                f"- `{entry['path']}` — {entry['reason']}"
            )
    else:
        lines.append("- None")

    markdown_output.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )

    print(
        f"{result['status']}: "
        f"{governed_count} governed document(s), "
        f"{navigation_count} navigation document(s), "
        f"{len(errors)} error(s), "
        f"{len(warnings)} warning(s)."
    )

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
