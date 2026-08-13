from __future__ import annotations

import hashlib
import os
import subprocess
from collections.abc import Iterator
from pathlib import Path

import pytest


def _run_git(root: Path, *arguments: str) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(root), *arguments],
        check=True,
        capture_output=True,
    )
    return completed.stdout


def _canonical_root() -> Path:
    return Path(__file__).resolve().parents[4]


def _canonical_snapshot(root: Path) -> tuple[bytes, tuple[tuple[str, str], ...]]:
    status = _run_git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all")
    tracked = tuple(
        path.decode("utf-8")
        for path in _run_git(root, "ls-files", "-z").split(b"\0")
        if path
    )
    digests = tuple(
        (relative, hashlib.sha256((root / relative).read_bytes()).hexdigest())
        for relative in tracked
    )
    return status, digests


@pytest.fixture(scope="session", autouse=True)
def isolated_integration_repository(
    tmp_path_factory: pytest.TempPathFactory,
) -> Iterator[Path]:
    canonical = _canonical_root()
    before = _canonical_snapshot(canonical)
    temporary_parent = tmp_path_factory.mktemp("ysim-integration-repository")
    repository = temporary_parent / "repository"
    subprocess.run(
        ["git", "clone", "--quiet", "--no-hardlinks", str(canonical), str(repository)],
        check=True,
    )
    branch = _run_git(canonical, "branch", "--show-current").decode("utf-8").strip()
    subprocess.run(
        ["git", "-C", str(repository), "switch", "--quiet", branch],
        check=True,
    )
    previous = Path.cwd()
    os.chdir(repository / "tools/ysf")
    try:
        yield repository
    finally:
        os.chdir(previous)
        assert _canonical_snapshot(canonical) == before


@pytest.fixture(autouse=True)
def canonical_checkout_is_unchanged(
    isolated_integration_repository: Path,
) -> Iterator[None]:
    del isolated_integration_repository
    canonical = _canonical_root()
    before = _canonical_snapshot(canonical)
    yield
    assert _canonical_snapshot(canonical) == before
