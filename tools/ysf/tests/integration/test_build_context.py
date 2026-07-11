from pathlib import Path

from ysf.context.service import (
    build_context,
)


def test_build_context_in_repository() -> None:
    repository_root = (
        Path.cwd().parents[1]
    )

    manifest = (
        repository_root
        / "factory/context-manifests/"
        "s00.yaml"
    )

    result = build_context(
        repository_root=repository_root,
        manifest_path=manifest,
    )

    assert result.successful
    assert (
        result.data["documentCount"]
        > 0
    )
    assert (
        repository_root
        / "factory/contexts/generated/"
        "s00/context.json"
    ).is_file()
