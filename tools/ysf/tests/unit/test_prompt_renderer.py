from pathlib import Path

from ysf.prompt.renderer import (
    render_template,
)


def test_render_template(
    tmp_path: Path,
) -> None:
    template = tmp_path / "template.md"

    template.write_text(
        "# OBJECTIVE\n\n{{ objective }}\n",
        encoding="utf-8",
    )

    result = render_template(
        template_path=template,
        values={
            "objective": "Build safely.",
        },
    )

    assert "Build safely." in result
    assert "{{" not in result
