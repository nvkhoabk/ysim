#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path


def extract_code_and_title(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()

    metadata: dict[str, str] = {}

    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip().strip("\"'")

    code = metadata.get("document_code", path.stem)
    title = metadata.get("document_name", "")

    if not title:
        for line in lines:
            if line.startswith("# "):
                title = line[2:].strip()
                break

    return code, title or path.stem


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    docs_dir = repo_root / "docs"
    output = docs_dir / "INDEX.md"

    document_sets = sorted(
        path for path in docs_dir.iterdir() if path.is_dir()
    )

    lines = [
        "# YSim Documentation Index",
        "",
        "Project baseline: **YSim v2.1**",
        "",
        "This index is generated from the documentation repository.",
        "",
    ]

    total = 0

    for document_set in document_sets:
        files = sorted(document_set.glob("*.md"))
        files = [
            path for path in files
            if path.name not in {"INDEX.md", "MASTER_INDEX.md"}
        ]

        if not files:
            continue

        lines.extend(
            [
                f"## {document_set.name}",
                "",
                "| Code | Document | File |",
                "|---|---|---|",
            ]
        )

        for path in files:
            code, title = extract_code_and_title(path)
            relative = path.relative_to(docs_dir).as_posix()

            lines.append(
                f"| {code} | {title} | "
                f"[{path.name}]({relative}) |"
            )
            total += 1

        lines.append("")

    lines.extend(
        [
            "## Summary",
            "",
            f"Total indexed documents: **{total}**",
            "",
        ]
    )

    output.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    print(f"Generated {output.relative_to(repo_root)}")


if __name__ == "__main__":
    main()
