from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from ysf.context.models import ContextDocument


def strip_frontmatter(
    text: str,
) -> str:
    lines = text.splitlines()

    if (
        not lines
        or lines[0].strip() != "---"
    ):
        return text.strip()

    for index, line in enumerate(
        lines[1:],
        start=1,
    ):
        if line.strip() == "---":
            return "\n".join(
                lines[index + 1 :]
            ).strip()

    return text.strip()


def compact_markdown(
    text: str,
) -> str:
    body = strip_frontmatter(text)

    return re.sub(
        r"\n{4,}",
        "\n\n\n",
        body,
    ).strip()


def assemble_context(
    repository_root: Path,
    selected_documents: list[
        dict[str, Any]
    ],
    maximum_characters: int,
) -> tuple[
    str,
    list[ContextDocument],
    int,
]:
    sections: list[str] = []
    included: list[ContextDocument] = []
    total_characters = 0

    for document in selected_documents:
        relative_path = str(
            document["path"]
        )

        source_path = (
            repository_root
            / relative_path
        )

        if not source_path.is_file():
            raise FileNotFoundError(
                "Context source document "
                f"not found: {relative_path}"
            )

        content = compact_markdown(
            source_path.read_text(
                encoding="utf-8-sig",
            )
        )

        document_code = str(
            document.get(
                "documentCode",
            )
            or relative_path
        )

        section = (
            f"# Source: {document_code}\n\n"
            f"- Path: `{relative_path}`\n"
            f"- Set: "
            f"`{document.get('documentSet')}`\n"
            f"- Version: "
            f"`{document.get('version')}`\n"
            f"- Status: "
            f"`{document.get('status')}`\n\n"
            f"{content}\n"
        )

        if (
            total_characters
            + len(section)
            > maximum_characters
        ):
            continue

        sections.append(section)
        total_characters += len(section)

        included.append(
            ContextDocument(
                document_code=document_code,
                path=relative_path,
                document_set=str(
                    document.get(
                        "documentSet",
                        "",
                    )
                ),
                version=(
                    str(
                        document.get(
                            "version"
                        )
                    )
                    if document.get(
                        "version"
                    )
                    is not None
                    else None
                ),
                status=(
                    str(
                        document.get(
                            "status"
                        )
                    )
                    if document.get(
                        "status"
                    )
                    is not None
                    else None
                ),
                characters=len(section),
            )
        )

    context_text = (
        "\n\n---\n\n".join(
            sections
        )
        + "\n"
    )

    return (
        context_text,
        included,
        total_characters,
    )
