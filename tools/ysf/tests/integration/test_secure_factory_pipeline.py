from __future__ import annotations

import json
from pathlib import Path
from subprocess import CompletedProcess

import pytest

from ysf.cli import create_parser as create_ysf_parser
from ysf.secure_factory.cli import (
    _commit_timestamp,
    _identity,
    _known_bad,
    _preflight,
    _repository_root,
    create_parser,
    main,
)
from ysf.secure_factory.models import FactoryFailure, GateResult


def repository_root() -> Path:
    return Path(__file__).resolve().parents[4]


def test_all_required_repository_modes_parse() -> None:
    parser = create_parser()
    for mode in ("preflight", "verify", "known-bad", "build-candidate"):
        assert parser.parse_args([mode]).mode == mode
    parsed = parser.parse_args(["verify-candidate", "/tmp/candidate"])
    assert parsed.candidate_path == "/tmp/candidate"


def test_existing_ysf_cli_exposes_secure_factory_without_removing_old_commands() -> None:
    parser = create_ysf_parser()
    assert parser.parse_args(["doctor"]).command == "doctor"
    parsed = parser.parse_args(["secure-factory", "known-bad", "--json"])
    assert parsed.command == "secure-factory"
    assert parsed.mode == "known-bad"


def test_repository_entrypoint_applies_the_contract_bandit_threshold() -> None:
    entrypoint = repository_root() / "scripts/v3-r1-s00.sh"
    content = entrypoint.read_text(encoding="utf-8")
    assert "python3 -m bandit -q -r src/ysf --severity-level medium" in content
    assert "python3 -m bandit -q -r src/ysf\n" not in content


def test_known_bad_matrix_rejects_every_quarantined_fixture() -> None:
    gates = _known_bad(repository_root())
    assert [gate.gate for gate in gates] == [
        "known_bad_path_escape",
        "known_bad_secret",
        "known_bad_esim",
        "known_bad_tampered_manifest",
    ]
    assert all(gate.passed for gate in gates)


def test_known_bad_cli_writes_safe_immutable_evidence(tmp_path: Path, capsys: object) -> None:
    exit_code = main(
        [
            "known-bad",
            "--output-root",
            str(tmp_path / "evidence"),
            "--execution-id",
            "V3-R1-S00-INTEGRATION-0001",
            "--json",
        ]
    )
    assert exit_code == 0
    captured = capsys.readouterr()  # type: ignore[attr-defined]
    payload = json.loads(captured.out)
    assert payload["result"] == "PASS"
    evidence = Path(payload["evidence_directory"])
    assert (evidence / "execution-ledger.jsonl").is_file()
    assert (evidence / "result.json").is_file()


def test_cli_modes_and_failures_write_results(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: object
) -> None:
    monkeypatch.setattr("ysf.secure_factory.cli._repository_root", lambda: tmp_path)
    pass_gate = GateResult("synthetic", "PASS", "safe")
    monkeypatch.setattr("ysf.secure_factory.cli._preflight", lambda root, **kwargs: [pass_gate])
    output_base = tmp_path.parent / f"{tmp_path.name}-outputs"

    assert main(["preflight", "--output-root", str(output_base / "preflight")]) == 0
    assert "RESULT=PASS" in capsys.readouterr().out  # type: ignore[attr-defined]

    monkeypatch.setattr(
        "ysf.secure_factory.cli._identity",
        lambda root: ("nvkhoabk/ysim", "a" * 40, "b" * 40),
    )
    monkeypatch.setattr("ysf.secure_factory.cli._commit_timestamp", lambda root: 1)
    monkeypatch.setattr("ysf.secure_factory.cli.build_candidate", lambda *args, **kwargs: pass_gate)
    monkeypatch.setenv("YSF_S00_QUALITY_ROOT", str(tmp_path / "quality"))
    assert main(["build-candidate", "--output-root", str(output_base / "build")]) == 0

    monkeypatch.setattr("ysf.secure_factory.cli.verify_candidate", lambda path: pass_gate)
    assert (
        main(
            [
                "verify-candidate",
                str(tmp_path / "candidate"),
                "--output-root",
                str(output_base / "verify"),
            ]
        )
        == 0
    )

    def fail(_: Path) -> list[GateResult]:
        raise FactoryFailure("FAIL_TEST", "Synthetic safe failure.")

    monkeypatch.setattr("ysf.secure_factory.cli._preflight", fail)
    assert main(["verify", "--output-root", str(output_base / "failure")]) == 1
    assert "FAILURE_CODE=FAIL_TEST" in capsys.readouterr().out  # type: ignore[attr-defined]


def test_repository_root_and_commit_timestamp(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "ysf.secure_factory.cli.subprocess.run",
        lambda *args, **kwargs: CompletedProcess(args, 0, str(tmp_path) + "\n", ""),
    )
    assert _repository_root() == tmp_path.resolve()
    monkeypatch.setattr(
        "ysf.secure_factory.cli.subprocess.run",
        lambda *args, **kwargs: CompletedProcess(args, 0, "1700000000\n", ""),
    )
    assert _commit_timestamp(tmp_path) == 1_700_000_000
    monkeypatch.setattr(
        "ysf.secure_factory.cli.subprocess.run",
        lambda *args, **kwargs: CompletedProcess(args, 1, "", ""),
    )
    with pytest.raises(FactoryFailure) as captured:
        _repository_root()
    assert captured.value.code == "FAIL_REPOSITORY_ROOT"
    with pytest.raises(FactoryFailure) as captured:
        _commit_timestamp(tmp_path)
    assert captured.value.code == "FAIL_COMMIT_TIMESTAMP"


def test_candidate_source_identity(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "ysf.secure_factory.cli.load_expectation",
        lambda path: type("Expectation", (), {"repository": "nvkhoabk/ysim"})(),
    )
    calls = iter(
        [
            CompletedProcess([], 0, "a" * 40 + "\n", ""),
            CompletedProcess([], 0, "b" * 40 + "\n", ""),
        ]
    )
    monkeypatch.setattr(
        "ysf.secure_factory.cli.subprocess.run", lambda *args, **kwargs: next(calls)
    )
    assert _identity(tmp_path) == ("nvkhoabk/ysim", "a" * 40, "b" * 40)
    monkeypatch.setattr(
        "ysf.secure_factory.cli.subprocess.run",
        lambda *args, **kwargs: CompletedProcess([], 1, "", ""),
    )
    with pytest.raises(FactoryFailure) as captured:
        _identity(tmp_path)
    assert captured.value.code == "FAIL_CANDIDATE_SOURCE_IDENTITY"


def test_preflight_orchestrates_policy_and_safe_scan(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    context = tmp_path / "docs/v3/r1/g00/s00"
    context.mkdir(parents=True)
    source = tmp_path / "AGENTS.md"
    source.write_text("safe", encoding="utf-8")
    gate = GateResult("gate", "PASS", "safe")
    monkeypatch.setattr("ysf.secure_factory.cli.load_expectation", lambda path: object())
    monkeypatch.setattr("ysf.secure_factory.cli.observe_environment", lambda root: object())
    monkeypatch.setattr(
        "ysf.secure_factory.cli.validate_environment", lambda expected, observed: gate
    )
    monkeypatch.setattr("ysf.secure_factory.cli.verify_policy_self_protection", lambda path: gate)
    monkeypatch.setattr("ysf.secure_factory.cli.mutation_paths", lambda root: {"AGENTS.md"})
    monkeypatch.setattr("ysf.secure_factory.cli.validate_changed_paths", lambda root, paths: gate)
    monkeypatch.setattr("ysf.secure_factory.cli.verify_immutable_corpus", lambda root: gate)
    monkeypatch.setattr("ysf.secure_factory.cli.require_no_sensitive_values", lambda paths: gate)
    assert len(_preflight(tmp_path)) == 5


def test_known_bad_fixture_self_checks_fail_closed(tmp_path: Path) -> None:
    fixture_root = tmp_path / "tools/ysf/tests/fixtures/secure_factory/noncompliant"
    fixture_root.mkdir(parents=True)
    (fixture_root / "path-escape.json").write_text('{"path":"safe.txt"}\n', encoding="utf-8")
    (fixture_root / "synthetic-secret.txt").write_text("safe\n", encoding="utf-8")
    (fixture_root / "synthetic-esim-payload.txt").write_text("safe\n", encoding="utf-8")
    (fixture_root / "tampered-manifest.json").write_text('{"sha256":"wrong"}\n', encoding="utf-8")
    with pytest.raises(FactoryFailure) as captured:
        _known_bad(tmp_path)
    assert captured.value.code == "FAIL_KNOWN_BAD_ACCEPTED"
