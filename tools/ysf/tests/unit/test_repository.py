from pathlib import Path

from ysf.core.repository import find_repository_root


def test_find_repository_root() -> None:
    root = find_repository_root(Path.cwd())

    assert (root / ".git").exists()
    assert (root / "factory").is_dir()
    assert (root / "docs").is_dir()
