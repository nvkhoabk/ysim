from pathlib import Path

from ysf.prompt.service import build_prompt


def test_build_prompt_in_repository() -> None:
    repository_root = (
        Path.cwd().parents[1]
    )

    manifest = (
        repository_root
        / "factory/prompt-manifests/"
        "s00-t00.yaml"
    )

    result = build_prompt(
        repository_root=repository_root,
        manifest_path=manifest,
    )

    assert result.successful

    assert (
        repository_root
        / "factory/prompts/generated/"
        "s00/t00/prompt.md"
    ).is_file()
