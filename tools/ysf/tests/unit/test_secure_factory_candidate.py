from __future__ import annotations

import json
import shutil
from pathlib import Path
from subprocess import CompletedProcess

import pytest

from ysf.secure_factory.candidate import (
    _parse_lock_components,
    build_candidate,
    verify_candidate,
    write_reproducible_zip,
)
from ysf.secure_factory.evidence import build_manifest, sha256_file
from ysf.secure_factory.models import FactoryFailure


def test_reproducible_zip_bytes_match(tmp_path: Path) -> None:
    files = {"ysf/data.txt": b"deterministic", "ysf/__init__.py": b""}
    first = tmp_path / "first.whl"
    second = tmp_path / "second.whl"
    write_reproducible_zip(first, files, source_date_epoch=1_700_000_000)
    write_reproducible_zip(second, files, source_date_epoch=1_700_000_000)
    assert first.read_bytes() == second.read_bytes()


def _synthetic_candidate(root: Path) -> Path:
    candidate = root / "candidate"
    artifacts = candidate / "artifacts"
    reports = candidate / "reports"
    artifacts.mkdir(parents=True)
    reports.mkdir()
    write_reproducible_zip(
        artifacts / "ysf-0.1.0-py3-none-any.whl",
        {"ysf/__init__.py": b""},
        source_date_epoch=1_700_000_000,
    )
    (reports / "gates.json").write_text('{"result":"PASS"}\n', encoding="utf-8")
    for name in (
        "test-and-coverage.json",
        "lint-type-sast-dependency.json",
        "leak-scan.json",
    ):
        (reports / name).write_text('{"result":"PASS"}\n', encoding="utf-8")
    (candidate / "environment-identity.json").write_text(
        '{"environment":"synthetic"}\n', encoding="utf-8"
    )
    (candidate / "execution-ledger.jsonl").write_text('{"result":"PASS"}\n', encoding="utf-8")
    (candidate / "sbom.cdx.json").write_text(
        '{"bomFormat":"CycloneDX","specVersion":"1.6","version":1}\n', encoding="utf-8"
    )
    (candidate / "provenance.json").write_text(
        '{"_type":"https://in-toto.io/Statement/v1"}\n', encoding="utf-8"
    )
    paths = [
        path.relative_to(candidate).as_posix() for path in candidate.rglob("*") if path.is_file()
    ]
    manifest = [item.to_dict() for item in build_manifest(candidate, paths)]
    (candidate / "artifact-manifest.json").write_text(
        json.dumps(manifest, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    checksum_paths = sorted(paths + ["artifact-manifest.json"])
    (candidate / "SHA256SUMS").write_text(
        "".join(f"{sha256_file(candidate / path)}  {path}\n" for path in checksum_paths),
        encoding="ascii",
    )
    return candidate


def test_candidate_verification_is_non_rebuilding_and_tamper_evident(
    tmp_path: Path,
) -> None:
    candidate = _synthetic_candidate(tmp_path)
    assert verify_candidate(candidate).passed
    (candidate / "reports/gates.json").write_text('{"result":"FAIL"}\n', encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        verify_candidate(candidate)
    assert captured.value.code == "FAIL_MANIFEST_TAMPER"


def test_build_candidate_refuses_second_build(tmp_path: Path) -> None:
    repository = tmp_path / "repo"
    repository.mkdir()
    candidate = tmp_path / "candidate"
    candidate.mkdir()
    with pytest.raises(FactoryFailure) as captured:
        build_candidate(
            repository,
            candidate,
            repository="nvkhoabk/ysim",
            commit="a" * 40,
            tree="b" * 40,
            contract_sha256="c" * 64,
            source_date_epoch=1_700_000_000,
            gate_report={"result": "PASS"},
            report_root=tmp_path,
        )
    assert captured.value.code == "FAIL_SECOND_BUILD"


def test_lock_components_are_sorted_and_conflicts_fail(tmp_path: Path) -> None:
    first = tmp_path / "first.lock"
    second = tmp_path / "second.lock"
    first.write_text("Zulu_Pkg==2.0 --hash=sha256:" + "a" * 64 + "\n", encoding="utf-8")
    second.write_text("alpha==1.0 --hash=sha256:" + "b" * 64 + "\n", encoding="utf-8")
    assert [item["name"] for item in _parse_lock_components([first, second])] == [
        "alpha",
        "zulu-pkg",
    ]
    second.write_text("zulu-pkg==3.0 --hash=sha256:" + "c" * 64 + "\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        _parse_lock_components([first, second])
    assert captured.value.code == "FAIL_LOCK_CONFLICT"
    second.write_text("# no package\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        _parse_lock_components([second])
    assert captured.value.code == "FAIL_LOCK_EMPTY"


def test_build_candidate_success_and_build_failure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repository = tmp_path / "repo"
    lock_root = repository / "tools/ysf"
    lock_root.mkdir(parents=True)
    for name in ("requirements-s00-build.lock", "requirements-s00-dev.lock"):
        (lock_root / name).write_text(
            "example-package==1.2.3 --hash=sha256:" + "a" * 64 + "\n",
            encoding="utf-8",
        )
    report_root = tmp_path / "reports"
    report_root.mkdir()
    for name in (
        "test-and-coverage.json",
        "lint-type-sast-dependency.json",
        "leak-scan.json",
        "environment-identity.json",
        "execution-ledger.jsonl",
    ):
        report_root.joinpath(name).write_text('{"result":"PASS"}\n', encoding="utf-8")

    observed_build_sources: list[Path] = []

    def successful_run(command: list[str], **_: object) -> CompletedProcess[str]:
        output = Path(command[command.index("--outdir") + 1])
        build_source = Path(command[-1])
        assert build_source.is_dir()
        assert build_source != repository / "tools/ysf"
        assert repository not in build_source.parents
        observed_build_sources.append(build_source)
        write_reproducible_zip(
            output / "ysf-0.1.0-py3-none-any.whl",
            {"ysf/__init__.py": b""},
            source_date_epoch=1_700_000_000,
        )
        return CompletedProcess(command, 0, "", "")

    monkeypatch.setattr("ysf.secure_factory.candidate.subprocess.run", successful_run)
    candidate = tmp_path / "candidate"
    result = build_candidate(
        repository,
        candidate,
        repository="nvkhoabk/ysim",
        commit="a" * 40,
        tree="b" * 40,
        contract_sha256="c" * 64,
        source_date_epoch=1_700_000_000,
        gate_report={"result": "PASS"},
        report_root=report_root,
    )
    assert result.passed
    assert verify_candidate(candidate).passed
    assert len(observed_build_sources) == 1
    assert not observed_build_sources[0].exists()
    assert not (repository / "tools/ysf/build").exists()
    assert not (repository / "tools/ysf/src/ysf.egg-info").exists()

    incomplete_reports = tmp_path / "incomplete-reports"
    incomplete_reports.mkdir()
    with pytest.raises(FactoryFailure) as captured:
        build_candidate(
            repository,
            tmp_path / "incomplete-candidate",
            repository="nvkhoabk/ysim",
            commit="a" * 40,
            tree="b" * 40,
            contract_sha256="c" * 64,
            source_date_epoch=1_700_000_000,
            gate_report={"result": "PASS"},
            report_root=incomplete_reports,
        )
    assert captured.value.code == "FAIL_CANDIDATE_REPORT_BUNDLE"

    monkeypatch.setattr(
        "ysf.secure_factory.candidate.subprocess.run",
        lambda *args, **kwargs: CompletedProcess(args, 7, "", ""),
    )
    with pytest.raises(FactoryFailure) as captured:
        build_candidate(
            repository,
            tmp_path / "failed-candidate",
            repository="nvkhoabk/ysim",
            commit="a" * 40,
            tree="b" * 40,
            contract_sha256="c" * 64,
            source_date_epoch=1_700_000_000,
            gate_report={"result": "PASS"},
            report_root=report_root,
        )
    assert captured.value.code == "FAIL_CANDIDATE_BUILD"


def test_candidate_requires_exact_manifest_and_checksum_file_sets(
    tmp_path: Path,
) -> None:
    candidate = _synthetic_candidate(tmp_path)
    (candidate / "unexpected.txt").write_text("safe", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        verify_candidate(candidate)
    assert captured.value.code == "FAIL_MANIFEST_FILE_SET"

    candidate = _synthetic_candidate(tmp_path / "second")
    lines = (candidate / "SHA256SUMS").read_text(encoding="ascii").splitlines()
    (candidate / "SHA256SUMS").write_text("\n".join(lines[1:]) + "\n", encoding="ascii")
    with pytest.raises(FactoryFailure) as captured:
        verify_candidate(candidate)
    assert captured.value.code == "FAIL_CHECKSUM_FILE_SET"


def test_candidate_rejects_missing_malformed_tampered_and_symlink_inputs(
    tmp_path: Path,
) -> None:
    with pytest.raises(FactoryFailure) as captured:
        verify_candidate(tmp_path / "missing")
    assert captured.value.code == "FAIL_CANDIDATE_PATH"

    candidate = _synthetic_candidate(tmp_path / "link-source")
    link = tmp_path / "candidate-link"
    link.symlink_to(candidate, target_is_directory=True)
    with pytest.raises(FactoryFailure) as captured:
        verify_candidate(link)
    assert captured.value.code == "FAIL_CANDIDATE_PATH"

    candidate = _synthetic_candidate(tmp_path / "missing-required")
    (candidate / "sbom.cdx.json").unlink()
    with pytest.raises(FactoryFailure) as captured:
        verify_candidate(candidate)
    assert captured.value.code == "FAIL_CANDIDATE_INCOMPLETE"

    candidate = _synthetic_candidate(tmp_path / "two-wheels")
    wheel = next((candidate / "artifacts").glob("*.whl"))
    shutil.copyfile(wheel, candidate / "artifacts/other.whl")
    with pytest.raises(FactoryFailure) as captured:
        verify_candidate(candidate)
    assert captured.value.code == "FAIL_WHEEL_COUNT"

    candidate = _synthetic_candidate(tmp_path / "member-link")
    (candidate / "link").symlink_to(candidate / "reports/gates.json")
    with pytest.raises(FactoryFailure) as captured:
        verify_candidate(candidate)
    assert captured.value.code == "FAIL_CANDIDATE_SYMLINK"

    candidate = _synthetic_candidate(tmp_path / "bad-manifest")
    (candidate / "artifact-manifest.json").write_text("{}\n", encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        verify_candidate(candidate)
    assert captured.value.code == "FAIL_MANIFEST_FORMAT"

    candidate = _synthetic_candidate(tmp_path / "bad-checksum")
    (candidate / "SHA256SUMS").write_text("invalid\n", encoding="ascii")
    with pytest.raises(FactoryFailure) as captured:
        verify_candidate(candidate)
    assert captured.value.code == "FAIL_CHECKSUM_FORMAT"

    candidate = _synthetic_candidate(tmp_path / "tampered-checksum")
    lines = (candidate / "SHA256SUMS").read_text(encoding="ascii").splitlines()
    relative = lines[0][66:]
    lines[0] = "0" * 64 + "  " + relative
    (candidate / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="ascii")
    with pytest.raises(FactoryFailure) as captured:
        verify_candidate(candidate)
    assert captured.value.code == "FAIL_CANDIDATE_TAMPER"
