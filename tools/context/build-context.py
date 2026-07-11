#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


class ContextBuildError(RuntimeError):
    pass


def read_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ContextBuildError(f"Missing JSON file: {path}")

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ContextBuildError(
            f"Invalid JSON in {path}: {exc}"
        ) from exc

    if not isinstance(data, dict):
        raise ContextBuildError(f"Expected object in {path}")

    return data


def parse_simple_yaml(path: Path) -> dict[str, Any]:
    """
    Minimal YAML parser for this manifest structure.

    Supports:
    - key: value
    - nested mappings by indentation
    - list items using "- value"

    No external dependency is required.
    """
    if not path.is_file():
        raise ContextBuildError(f"Missing manifest: {path}")

    lines = path.read_text(encoding="utf-8-sig").splitlines()
    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]

    for line_number, raw_line in enumerate(lines, start=1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = raw_line.strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()

        parent = stack[-1][1]

        if stripped.startswith("- "):
            if not isinstance(parent, list):
                raise ContextBuildError(
                    f"Invalid list at {path}:{line_number}"
                )

            value = stripped[2:].strip().strip("\"'")
            parent.append(value)
            continue

        if ":" not in stripped:
            raise ContextBuildError(
                f"Invalid YAML line at {path}:{line_number}: {stripped}"
            )

        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value:
            parsed_value: Any = value.strip("\"'")

            if parsed_value.isdigit():
                parsed_value = int(parsed_value)

            if isinstance(parent, dict):
                parent[key] = parsed_value
            else:
                raise ContextBuildError(
                    f"Invalid mapping at {path}:{line_number}"
                )

            continue

        next_nonempty = None

        for future_line in lines[line_number:]:
            if future_line.strip() and not future_line.lstrip().startswith("#"):
                next_nonempty = future_line
                break

        is_list = (
            next_nonempty is not None
            and len(next_nonempty) - len(next_nonempty.lstrip(" ")) > indent
            and next_nonempty.strip().startswith("- ")
        )

        container: Any = [] if is_list else {}

        if not isinstance(parent, dict):
            raise ContextBuildError(
                f"Invalid nested mapping at {path}:{line_number}"
            )

        parent[key] = container
        stack.append((indent, container))

    return root


def strip_frontmatter(text: str) -> str:
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        return text.strip()

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[index + 1:]).strip()

    return text.strip()


def compact_markdown(text: str) -> str:
    text = strip_frontmatter(text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def select_documents(
    documents: list[dict[str, Any]],
    manifest: dict[str, Any],
    knowledge: dict[str, Any],
) -> list[dict[str, Any]]:
    document_sets = set(
        manifest.get("document_sets", {}).get("include", [])
    )

    required_codes = set(
        manifest.get("documents", {}).get("required", [])
    )

    capabilities = set(manifest.get("capabilities", []))

    capability_document_ids: set[str] = set()

    for capability in knowledge.get("capabilities", []):
        if capability.get("id") in capabilities:
            capability_document_ids.update(
                capability.get("documentIds", [])
            )

    selected: list[dict[str, Any]] = []
    seen_paths: set[str] = set()

    for document in documents:
        if document.get("generatedNavigation"):
            continue

        code = document.get("documentCode")
        document_id = code or document.get("id")
        document_set = document.get("documentSet")
        path = document.get("path")

        include = (
            code in required_codes
            or document_id in capability_document_ids
            or document_set in document_sets
        )

        if include and path and path not in seen_paths:
            selected.append(document)
            seen_paths.add(path)

    required_found = {
        document.get("documentCode")
        for document in selected
        if document.get("documentCode")
    }

    missing_required = sorted(required_codes - required_found)

    if missing_required:
        raise ContextBuildError(
            "Missing required documents: "
            + ", ".join(missing_required)
        )

    selected.sort(
        key=lambda item: (
            item.get("documentSet", ""),
            item.get("documentCode") or item.get("filename", ""),
        )
    )

    max_documents = int(
        manifest.get("limits", {}).get("max_documents", 30)
    )

    return selected[:max_documents]


def build_context(
    repo_root: Path,
    manifest_path: Path,
) -> None:
    manifest = parse_simple_yaml(manifest_path)

    documents_index = read_json(
        repo_root / "factory" / "index" / "documents.json"
    )

    capability_catalog = read_json(
        repo_root / "knowledge" / "catalog" / "capabilities.json"
    )

    documents = documents_index.get("documents", [])

    if not isinstance(documents, list):
        raise ContextBuildError(
            "documents.json does not contain a documents array"
        )

    selected = select_documents(
        documents=documents,
        manifest=manifest,
        knowledge=capability_catalog,
    )

    output_directory = manifest.get(
        "output", {}
    ).get(
        "directory",
        "factory/contexts/generated/default",
    )

    output_root = repo_root / output_directory
    output_root.mkdir(parents=True, exist_ok=True)

    max_characters = int(
        manifest.get("limits", {}).get("max_characters", 250000)
    )

    context_sections: list[str] = []
    included_documents: list[dict[str, Any]] = []
    total_characters = 0

    for document in selected:
        relative_path = document["path"]
        source_path = repo_root / relative_path

        if not source_path.is_file():
            raise ContextBuildError(
                f"Document does not exist: {relative_path}"
            )

        content = compact_markdown(
            source_path.read_text(encoding="utf-8-sig")
        )

        section = (
            f"# Source: {document.get('documentCode') or relative_path}\n\n"
            f"- Path: `{relative_path}`\n"
            f"- Set: `{document.get('documentSet')}`\n"
            f"- Version: `{document.get('version')}`\n"
            f"- Status: `{document.get('status')}`\n\n"
            f"{content}\n"
        )

        if total_characters + len(section) > max_characters:
            continue

        context_sections.append(section)
        total_characters += len(section)

        included_documents.append({
            "documentCode": document.get("documentCode"),
            "path": relative_path,
            "documentSet": document.get("documentSet"),
            "version": document.get("version"),
            "status": document.get("status"),
            "characters": len(section),
        })

    context_id = manifest.get("context_id", "unknown-context")
    generated_at = datetime.now().astimezone().isoformat()

    context_markdown = "\n\n---\n\n".join(context_sections) + "\n"

    context_file = output_root / "context.md"
    context_file.write_text(
        context_markdown,
        encoding="utf-8",
    )

    context_manifest = {
        "schemaVersion": "1.0",
        "contextId": context_id,
        "generatedAt": generated_at,
        "sourceManifest": manifest_path.relative_to(repo_root).as_posix(),
        "documentCount": len(included_documents),
        "characterCount": total_characters,
        "documents": included_documents,
        "output": context_file.relative_to(repo_root).as_posix(),
    }

    manifest_file = output_root / "context.json"
    manifest_file.write_text(
        json.dumps(
            context_manifest,
            indent=2,
            ensure_ascii=False,
        ) + "\n",
        encoding="utf-8",
    )

    summary_file = output_root / "README.md"
    summary_file.write_text(
        "\n".join([
            f"# Context Package — {context_id}",
            "",
            f"- Generated: {generated_at}",
            f"- Documents: {len(included_documents)}",
            f"- Characters: {total_characters}",
            "",
            "## Files",
            "",
            "- `context.md` — assembled context",
            "- `context.json` — traceability manifest",
            "",
        ]),
        encoding="utf-8",
    )

    print(
        f"Context build PASS: "
        f"{len(included_documents)} documents, "
        f"{total_characters} characters."
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        required=True,
        type=Path,
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
    )

    args = parser.parse_args()

    try:
        repo_root = (
            args.repo_root.resolve()
            if args.repo_root
            else Path.cwd().resolve()
        )

        build_context(
            repo_root=repo_root,
            manifest_path=args.manifest.resolve(),
        )

        return 0

    except ContextBuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    except KeyboardInterrupt:
        print("ERROR: Interrupted.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
