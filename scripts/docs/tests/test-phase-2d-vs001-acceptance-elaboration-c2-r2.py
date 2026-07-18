#!/usr/bin/env python3
"""Final 187-mutation, regression, and executed-builder probes for C2-R2."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "scripts/docs/validate-phase-2d-vs001-acceptance-elaboration-c2-r2.py"
SOURCE_PATH = ROOT / "docs/baselines/v2.3/phase-2d/vs001-acceptance-elaboration-c2-r2.json"
MARKDOWN_PATH = ROOT / "docs/baselines/v2.3/phase-2d/VS001_ACCEPTANCE_ELABORATION_C2_R2_CANDIDATE.md"
MANIFEST_PATH = ROOT / "docs/baselines/v2.3/phase-2d/vs001-acceptance-elaboration-c2-r2-manifest.json"
BUILDER_PATH = ROOT / "scripts/docs/build-phase-2d-vs001-acceptance-elaboration-c2-r2.py"

spec = importlib.util.spec_from_file_location("c2r2_batch_c_validator", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def expect_code(expected: str, action, label: str) -> None:
    try:
        action()
    except validator.ValidationError as exc:
        if exc.code != expected:
            raise AssertionError(f"{label}: expected {expected}, got {exc.code}: {exc.detail}") from exc
        return
    raise AssertionError(f"{label}: mutation survived")


def validate_clauses(payload: dict, authorities: dict) -> None:
    validator.validate_clauses(payload, authorities, check_similarity=False)


def clause_for(payload: dict, rule_id: str) -> dict:
    return next(c for c in payload["decision_derived_acceptance_clauses"] if c["authoritative_rule_id"] == rule_id)


def clause_by_id(payload: dict, clause_id: str) -> dict:
    return next(c for c in payload["decision_derived_acceptance_clauses"] if c["clause_id"] == clause_id)


def contract_at(payload: dict, batch: str, index: int) -> dict:
    return payload[batch][index]


def run_modified_builder_probe(
    canonical_payload: dict,
    injection: str,
    expected_code: str,
    label: str,
) -> None:
    """Execute a genuinely modified builder and reject its actual output independently."""
    with tempfile.TemporaryDirectory(prefix="ysim-c2r2-builder-probe-") as raw:
        temp_root = Path(raw)
        for relative in validator.EXPECTED_FILES:
            target = temp_root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, target)
        copied_builder = temp_root / validator.EXPECTED_FILES[3]
        source = copied_builder.read_text(encoding="utf-8")
        marker = "    # BUILDER_CONFORMANCE_MUTATION_POINT"
        if marker not in source:
            raise AssertionError(f"{label}: mutation marker missing")
        copied_builder.write_text(source.replace(marker, injection + "\n" + marker, 1), encoding="utf-8", newline="\n")
        before_json = (temp_root / validator.EXPECTED_FILES[1]).read_bytes()
        result = subprocess.run(["python3", str(copied_builder)], cwd=temp_root, capture_output=True, text=True)
        if result.returncode:
            raise AssertionError(f"{label}: modified builder did not execute: {result.stderr}")
        if (temp_root / validator.EXPECTED_FILES[1]).read_bytes() != before_json:
            raise AssertionError(f"{label}: canonical JSON was modified")
        inventory = {str(path.relative_to(temp_root)) for path in temp_root.rglob("*") if path.is_file()}
        if inventory != set(validator.EXPECTED_FILES):
            raise AssertionError(f"{label}: undeclared writes: {sorted(inventory)}")
        files = {relative: (temp_root / relative).read_bytes() for relative in validator.EXPECTED_FILES}
        # The modified builder coherently refreshes its own and output hashes.
        # Manifest conformance alone must therefore pass and cannot authorize output.
        try:
            validator.validate_manifest(json.loads(files[validator.EXPECTED_FILES[2]]), files)
        except validator.ValidationError as exc:
            if exc.code == expected_code:
                return
            raise AssertionError(f"{label}: unexpected manifest rejection {exc.code}: {exc.detail}") from exc
        expect_code(
            expected_code,
            lambda: validator.validate_markdown(canonical_payload, files[validator.EXPECTED_FILES[0]]),
            label,
        )


def main() -> None:
    original = SOURCE_PATH.read_bytes()
    original_hash = hashlib.sha256(original).hexdigest()
    payload = json.loads(original)
    authorities = validator.load_authorities()
    validator.validate_payload(payload, authorities)

    # One real evidence-path mutation per authoritative rule.  Rule identity,
    # fingerprint, group membership and authority metadata remain untouched.
    semantic_killed = 0
    mutated_rules = []
    for original_clause in payload["decision_derived_acceptance_clauses"]:
        rid = original_clause["authoritative_rule_id"]
        mutated = copy.deepcopy(payload)
        target = clause_by_id(mutated, original_clause["clause_id"])
        target["observable_evidence_contract"]["observed_state"] = ""
        expect_code(
            "CONCRETE_EVIDENCE_MISSING",
            lambda m=mutated: validate_clauses(m, authorities),
            f"semantic-enforcement:{rid}",
        )
        semantic_killed += 1
        mutated_rules.append(rid)

    regressions = []

    # 1. Complete authoritative metadata cannot legitimize wrapper prose.
    mutated = copy.deepcopy(payload)
    target = mutated["decision_derived_acceptance_clauses"][0]
    target["concrete_assertion_or_prohibition"]["required_observation"] = (
        "Within BD-02-001, the accepted CANONICAL_PRODUCT_EXISTS rule binds Product."
    )
    regressions.append(("TEMPLATE_RULE_WRAPPER", mutated, "template-wrapper"))

    # 2. Evidence must identify a channel/state/comparison, not demonstrate an ID.
    mutated = copy.deepcopy(payload)
    target = mutated["decision_derived_acceptance_clauses"][0]
    target["observable_evidence_contract"]["observed_state"] = (
        "observe subject and demonstrate CANONICAL_PRODUCT_EXISTS"
    )
    regressions.append(("RULE_ID_ONLY_EVIDENCE", mutated, "rule-id-only-evidence"))

    # 3. Affected requirement metadata by itself is not enforcement.
    mutated = copy.deepcopy(payload)
    target = mutated["decision_derived_acceptance_clauses"][1]
    target["concrete_assertion_or_prohibition"]["required_observation"] = ""
    regressions.append(("CONCRETE_ENFORCEMENT_MISSING", mutated, "context-only-mapping"))

    # 4. Exclusion/prohibition requires an observable prohibited outcome.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "EXCLUDE_FROM_PUBLIC_LIST")
    target["concrete_assertion_or_prohibition"]["prohibited_observation"] = ""
    regressions.append(("PROHIBITED_OUTCOME_MISSING", mutated, "missing-prohibited-outcome"))

    # 5. Uniform public behavior must compare distinct controlled internal states.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "NO_PUBLIC_FAILURE_REASON")
    target["controlled_fixtures"] = [target["controlled_fixtures"][0]]
    regressions.append(("CONTROLLED_FIXTURES_MISSING", mutated, "uniform-result-one-fixture"))

    # 6. Observed authority cannot be the accepted expected-value authority.
    mutated = copy.deepcopy(payload)
    target = mutated["decision_derived_acceptance_clauses"][2]
    evidence = target["observable_evidence_contract"]
    evidence["observed_authority"] = evidence["expected_authority"]
    regressions.append(("EXPECTED_DERIVED_EVIDENCE", mutated, "expected-derived-evidence"))

    # 7. A BRD/UXF context is not the authority owner of a Decision C1 clause.
    mutated = copy.deepcopy(payload)
    mutated["decision_derived_acceptance_clauses"][3]["authority_owner"] = "BD-04-001"
    regressions.append(("DECISION_AUTHORITY_OWNER_MISMATCH", mutated, "false-requirement-authority"))

    # 8. Unrelated retained requirement plus missing justification is rejected.
    mutated = copy.deepcopy(payload)
    target = mutated["decision_derived_acceptance_clauses"][4]
    target["affected_requirement_contexts"] = ["UXF-405"]
    target["applicability"] = ""
    regressions.append(("UNRELATED_CONTEXT_OR_APPLICABILITY", mutated, "unrelated-context"))

    # 9. A mandatory list field needs an independent observation source.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "LIST_LOCALIZED_NAME")
    target["observable_evidence_contract"]["observed_authority"] = ""
    regressions.append(("CONCRETE_EVIDENCE_MISSING", mutated, "list-field-no-evidence-source"))

    # 10. An amount without its mandatory currency is an incomplete price tuple.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "LIST_BASE_PRICE_CURRENCY")
    target["concrete_assertion_or_prohibition"]["required_observation"] = ""
    regressions.append(("PRICE_AMOUNT_CURRENCY_PAIR_INCOMPLETE", mutated, "price-currency-missing"))

    # 11. Price evidence must remain independent from the expected authority.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "LIST_BASE_PRICE_AMOUNT")
    evidence = target["observable_evidence_contract"]
    evidence["observed_authority"] = evidence["expected_authority"]
    regressions.append(("EXPECTED_DERIVED_EVIDENCE", mutated, "expected-price-reused"))

    # 12. Slug equality cannot be weakened into mismatch tolerance.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "LIST_DETAIL_SLUG_EQUAL")
    target["concrete_assertion_or_prohibition"]["required_observation"] = "List and detail slugs may differ."
    target["concrete_assertion_or_prohibition"]["prohibited_observation"] = "Aliases can be accepted."
    regressions.append(("LIST_DETAIL_SLUG_CONSISTENCY_WEAKENED", mutated, "slug-mismatch-allowed"))

    # 13. Price equality cannot be weakened inside one snapshot.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "LIST_DETAIL_PRICE_EQUAL_WITHIN_SNAPSHOT")
    target["concrete_assertion_or_prohibition"]["required_observation"] = "List and detail prices may differ."
    target["concrete_assertion_or_prohibition"]["prohibited_observation"] = "Differences are tolerated."
    regressions.append(("LIST_DETAIL_PRICE_CONSISTENCY_WEAKENED", mutated, "price-mismatch-allowed"))

    # 14. Conditional fields need an explicit applicability predicate.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "DETAIL_VALIDITY_IF_DEFINED")
    target["applicability"] = ""
    regressions.append(("CONDITIONAL_APPLICABILITY_MISSING", mutated, "conditional-no-predicate"))

    # 15. Conditional fields require a real condition-false fixture.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "DETAIL_HOTSPOT_SUPPORT_IF_DEFINED")
    target["controlled_fixtures"][1]["controlled_state"] = "SPEC-B explicitly defines hotspot support value HS-B."
    regressions.append(("CONDITIONAL_FALSE_FIXTURE_MISSING", mutated, "conditional-no-false-fixture"))

    # 16. Product name cannot become a specification parser.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "NO_ATTRIBUTE_INFERENCE_FROM_PRODUCT_NAME")
    target["concrete_assertion_or_prohibition"]["prohibited_observation"] = "Product name is accepted as the attribute authority."
    regressions.append(("ATTRIBUTE_INFERENCE_PROHIBITION_WEAKENED", mutated, "name-attribute-inference"))

    # 17. Supplier purchase cost cannot serve as public base price.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "NO_PUBLIC_PURCHASE_COST")
    target["concrete_assertion_or_prohibition"]["prohibited_observation"] = "Internal commercial value may populate the public base amount."
    regressions.append(("SUPPLIER_COST_BOUNDARY_WEAKENED", mutated, "supplier-cost-as-price"))

    # 18. Promotion/discount/tax semantics remain outside the closed display contract.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "NO_PROMOTIONAL_PRICE")
    target["concrete_assertion_or_prohibition"]["prohibited_observation"] = "Promotional price may be public."
    regressions.append(("EXCLUDED_COMMERCIAL_FIELD_INTRODUCED", mutated, "promotion-introduced"))

    # 19. Read-only browse cannot gain a purchase action.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "NO_CART_OR_PURCHASE_ACTION")
    target["concrete_assertion_or_prohibition"]["prohibited_observation"] = "Cart action may be present."
    regressions.append(("PURCHASE_ACTION_INTRODUCED", mutated, "cart-action-introduced"))

    # 20. A sample path is not an accepted technical selection.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "NO_API_URL_DECISION")
    target["concrete_assertion_or_prohibition"]["required_observation"] = "/api/products is the selected approved URL."
    regressions.append(("TECHNICAL_CHOICE_PREMATURELY_SELECTED", mutated, "api-path-selected"))

    # 21. Two unrelated rules cannot share one copied semantic assertion.
    mutated = copy.deepcopy(payload)
    source = clause_for(mutated, "LIST_LOCALIZED_NAME")
    target = clause_for(mutated, "NO_DISCOUNT")
    target["concrete_assertion_or_prohibition"]["required_observation"] = source["concrete_assertion_or_prohibition"]["required_observation"]
    regressions.append(("DUPLICATE_SEMANTIC_ASSERTION", mutated, "copied-unrelated-assertion"))

    # 22. Evidence that only restates the rule is not observable evidence.
    mutated = copy.deepcopy(payload)
    target = clause_for(mutated, "PRICE_STOREFRONT_SCOPED")
    target["observable_evidence_contract"]["observed_state"] = "observe subject and demonstrate PRICE_STOREFRONT_SCOPED"
    regressions.append(("RULE_ID_ONLY_EVIDENCE", mutated, "dec002-rule-id-only-evidence"))

    # 23-31. Slug grammar, scope, stability and identity protections.
    for rule_id, weakened, label in (
        ("SLUG_NON_EMPTY", "Empty slug is accepted.", "empty-slug-accepted"),
        ("SLUG_LOWERCASE", "Uppercase slug is accepted.", "uppercase-slug-accepted"),
        ("SLUG_ASCII", "Non-ASCII slug is accepted.", "nonascii-slug-accepted"),
        ("SLUG_KEBAB_CASE", "Whitespace and underscore slug is allowed.", "invalid-kebab-accepted"),
        ("SLUG_UNIQUE_WITHIN_STOREFRONT", "Duplicate slug is allowed and may choose one Product.", "duplicate-slug-accepted"),
        ("SLUG_STABLE_FOR_PUBLISHED_PRODUCT", "Post-publication slug replacement is allowed.", "slug-change-accepted"),
        ("SLUG_NO_DATABASE_IDENTITY", "Internal database ID is accepted as the slug.", "database-id-slug"),
        ("SLUG_NO_SUPPLIER_REFERENCE", "Supplier reference is accepted as the slug.", "supplier-id-slug"),
        ("LIST_DETAIL_SLUG_CONSISTENT", "A different slug is allowed in detail.", "list-detail-slug-mismatch"),
    ):
        mutated = copy.deepcopy(payload)
        target = clause_by_id(mutated, f"DEC003-{rule_id}")
        target["concrete_assertion_or_prohibition"]["prohibited_observation"] = weakened
        regressions.append(("DEC003_PROHIBITION_REVERSED", mutated, label))

    # 32. Unknown and unavailable causes may not gain distinct public bodies.
    mutated = copy.deepcopy(payload)
    target = clause_by_id(mutated, "DEC003-UNKNOWN_SLUG")
    target["concrete_assertion_or_prohibition"]["prohibited_observation"] = "The public body may identify UNKNOWN_SLUG and distinguish it."
    regressions.append(("UNIFORM_NOT_FOUND_DISCLOSURE_ALLOWED", mutated, "unknown-unpublished-distinction"))

    # 33. Wrong-Storefront response cannot reveal its Storefront cause.
    mutated = copy.deepcopy(payload)
    target = clause_by_id(mutated, "DEC003-WRONG_STOREFRONT")
    target["concrete_assertion_or_prohibition"]["prohibited_observation"] = "The public body may identify SF-B."
    regressions.append(("UNIFORM_NOT_FOUND_DISCLOSURE_ALLOWED", mutated, "wrong-storefront-disclosure"))

    # 34. Malformed input cannot expose grammar diagnostics.
    mutated = copy.deepcopy(payload)
    target = clause_by_id(mutated, "DEC003-MALFORMED_SLUG")
    target["concrete_assertion_or_prohibition"]["prohibited_observation"] = "The public body may reveal malformed character details."
    regressions.append(("UNIFORM_NOT_FOUND_DISCLOSURE_ALLOWED", mutated, "malformed-diagnostic"))

    # 35-37. Redirect, alias and waitlist/replacement capabilities remain excluded.
    for rule_id, weakened, label in (
        ("NO_HISTORICAL_SLUG_REDIRECT", "Historical slug redirect is allowed.", "historical-redirect"),
        ("NO_ALIAS_RESOLUTION", "Alias input may resolve the Product.", "alias-resolution"),
        ("NO_WAITLIST", "Waitlist action is allowed on not-found.", "waitlist-introduced"),
    ):
        mutated = copy.deepcopy(payload)
        target = clause_by_id(mutated, f"DEC003-{rule_id}")
        target["concrete_assertion_or_prohibition"]["prohibited_observation"] = weakened
        regressions.append(("DEC003_PROHIBITION_REVERSED", mutated, label))

    # 38. Uniformity requires two distinct controlled internal fixtures.
    mutated = copy.deepcopy(payload)
    target = clause_by_id(mutated, "DEC003-PRODUCT_UNPUBLISHED")
    target["controlled_fixtures"] = [target["controlled_fixtures"][0]]
    regressions.append(("CONTROLLED_FIXTURES_MISSING", mutated, "uniformity-one-fixture"))

    # 39. Observed public evidence cannot originate from the expected cause/value.
    mutated = copy.deepcopy(payload)
    target = clause_by_id(mutated, "DEC003-PRICE_UNRESOLVED")
    evidence = target["observable_evidence_contract"]
    evidence["observed_authority"] = evidence["expected_authority"]
    regressions.append(("EXPECTED_DERIVED_EVIDENCE", mutated, "expected-cause-reused"))

    # 40. Generic not-found prose without exact outcome is rejected.
    mutated = copy.deepcopy(payload)
    target = clause_by_id(mutated, "DEC003-HTTP_STATUS_404")
    target["concrete_assertion_or_prohibition"]["required_observation"] = "return not found"
    regressions.append(("GENERIC_DECISION_CLAUSE", mutated, "generic-not-found"))

    # 41. Route examples cannot become approved implementation choices.
    mutated = copy.deepcopy(payload)
    target = clause_by_id(mutated, "DEC003-SLUG_LOWERCASE")
    target["concrete_assertion_or_prohibition"]["required_observation"] = "/products/:slug is the approved selected route."
    regressions.append(("TECHNICAL_CHOICE_PREMATURELY_SELECTED", mutated, "route-example-approved"))

    # 42. Affected requirement metadata alone is not semantic enforcement.
    mutated = copy.deepcopy(payload)
    target = clause_by_id(mutated, "DEC003-NO_PUBLIC_ADMIN_DIAGNOSTICS")
    target["concrete_assertion_or_prohibition"]["required_observation"] = ""
    regressions.append(("CONCRETE_ENFORCEMENT_MISSING", mutated, "context-only-dec003"))

    for expected, mutated, label in regressions:
        expect_code(expected, lambda m=mutated: validate_clauses(m, authorities), label)

    # Original 63-case population: 48 source-derived semantics, 9 retained
    # identities, and 6 structural/accounting mutations.
    source_mutations = {"obligation_disconnect": 0, "generic_outcome": 0, "expected_derived": 0}
    for batch, index, contract in list(validator.all_contracts(payload)):
        rid = contract["requirement_id"]

        mutated = copy.deepcopy(payload)
        contract_at(mutated, batch, index)["obligation_mapping"][0]["criterion_ids"] = []
        expect_code(
            "UNCOVERED_OBLIGATION",
            lambda m=mutated: validator.validate_sources_and_contracts(m, authorities, False),
            f"source-obligation:{rid}",
        )
        source_mutations["obligation_disconnect"] += 1

        mutated = copy.deepcopy(payload)
        contract_at(mutated, batch, index)["acceptance_criteria"][0]["expected_semantic_outcome"] = "works as expected"
        expect_code(
            "GENERIC_ACCEPTANCE",
            lambda m=mutated: validator.validate_sources_and_contracts(m, authorities, False),
            f"source-generic:{rid}",
        )
        source_mutations["generic_outcome"] += 1

        mutated = copy.deepcopy(payload)
        criterion = contract_at(mutated, batch, index)["acceptance_criteria"][0]
        criterion["observed_evidence_authority"] = criterion["expected_authority"]
        expect_code(
            "EXPECTED_DERIVED_OBSERVATION",
            lambda m=mutated: validator.validate_sources_and_contracts(m, authorities, False),
            f"source-derived-authority:{rid}",
        )
        source_mutations["expected_derived"] += 1

    retained_killed = 0
    for index, retained in enumerate(payload["retained_contracts"]):
        mutated = copy.deepcopy(payload)
        mutated["retained_contracts"][index]["canonical_contract_sha256"] = "0" * 64
        expect_code(
            "RETAINED_CONTRACT_HASH_MISMATCH",
            lambda m=mutated: validator.validate_retained(m, authorities),
            f"retained:{retained['requirement_id']}",
        )
        retained_killed += 1

    structural = []
    mutated = copy.deepcopy(payload); mutated["population"]["total"] = 24
    structural.append(("POPULATION_ACCOUNTING_MISMATCH", lambda m=mutated: validator.validate_metadata(m), "wrong-total"))
    mutated = copy.deepcopy(payload); mutated["batch_1_contracts"].pop()
    structural.append(("ELABORATED_REQUIREMENT_SET_MISMATCH", lambda m=mutated: validator.all_contracts(m), "missing-requirement"))
    mutated = copy.deepcopy(payload); mutated["batch_1_contracts"][1]["requirement_id"] = mutated["batch_1_contracts"][0]["requirement_id"]
    structural.append(("ELABORATED_REQUIREMENT_SET_MISMATCH", lambda m=mutated: validator.all_contracts(m), "duplicate-requirement"))
    mutated = copy.deepcopy(payload); mutated["governing_decisions"][0]["selected_option"] = "OPT-WRONG"
    structural.append(("EFFECTIVE_DECISION_SELECTION_MISMATCH", lambda m=mutated: validator.validate_metadata(m), "wrong-decision"))
    mutated = copy.deepcopy(payload); mutated["implementation_authorized"] = True
    structural.append(("CANDIDATE_METADATA_MISMATCH", lambda m=mutated: validator.validate_metadata(m), "implementation-authorized"))
    mutated = copy.deepcopy(payload); mutated["runtime_evidence_status"] = "EXECUTED"
    structural.append(("CANDIDATE_METADATA_MISMATCH", lambda m=mutated: validator.validate_metadata(m), "runtime-executed"))
    for expected, action, label in structural:
        expect_code(expected, action, label)

    # Ten actual modified-builder executions. Every builder runs in an
    # isolated six-file copy and refreshes its manifest coherently; the
    # independent Markdown projection validator still rejects its output.
    builder_probes = [
        ("    payload['decision_derived_acceptance_clauses'].pop()", "MARKDOWN_PROJECTION_COUNT_MISMATCH", "builder-omit-clause"),
        ("    payload['decision_derived_acceptance_clauses'][0]['concrete_assertion_or_prohibition']['required_observation'] = 'works as expected'", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH", "builder-generic-enforcement"),
        ("    payload['decision_derived_acceptance_clauses'][1]['observable_evidence_contract']['observed_state'] = 'observe subject and demonstrate rule'", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH", "builder-generic-evidence"),
        ("    payload['decision_derived_acceptance_clauses'][2]['concrete_assertion_or_prohibition']['prohibited_observation'] = 'prohibited behavior is allowed'", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH", "builder-prohibited-outcome"),
        ("    payload['decision_derived_acceptance_clauses'].reverse()", "MARKDOWN_PROJECTION_ORDER_OR_INVENTORY_MISMATCH", "builder-ordering"),
        ("    payload['retained_contracts'][0].pop('independently_recomputed_current_source_provenance')", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH", "builder-omit-retained-provenance"),
        ("    payload['runtime_evidence_status'] = 'PASS'", "MANIFEST_STATE_MISMATCH", "builder-false-runtime-pass"),
        ("    payload['decision_derived_acceptance_clauses'][0]['technical_choices_deferred'][0]['choice'] = '/products/:slug is selected'", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH", "builder-select-implementation"),
        ("    payload['decision_derived_acceptance_clauses'][3]['concrete_assertion_or_prohibition']['required_observation'] = 'coherently altered builder and manifest'", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH", "builder-coherent-manifest"),
        ("    payload['non_claims'] = ['COHERENT_BUT_DEFECTIVE_BUILDER_OUTPUT']", "MARKDOWN_SEMANTIC_PROJECTION_MISMATCH", "builder-markdown-manifest-coherent"),
    ]
    for injection, expected, label in builder_probes:
        run_modified_builder_probe(payload, injection, expected, label)

    if SOURCE_PATH.read_bytes() != original or hashlib.sha256(SOURCE_PATH.read_bytes()).hexdigest() != original_hash:
        raise AssertionError("candidate JSON changed during in-memory mutation tests")
    dec001_killed = sum(1 for c in payload["decision_derived_acceptance_clauses"] if c["decision_id"].endswith("DEC-001"))
    dec002_killed = sum(1 for c in payload["decision_derived_acceptance_clauses"] if c["decision_id"].endswith("DEC-002"))
    dec003_killed = semantic_killed - dec001_killed - dec002_killed
    source_total = sum(source_mutations.values())
    required_total = source_total + retained_killed + len(structural) + semantic_killed
    if semantic_killed != 124 or (dec001_killed, dec002_killed, dec003_killed) != (27, 54, 43) or len(mutated_rules) != 124 or len(regressions) != 42:
        raise AssertionError((semantic_killed, len(mutated_rules), len(regressions)))
    if source_mutations != {"obligation_disconnect": 16, "generic_outcome": 16, "expected_derived": 16}:
        raise AssertionError(source_mutations)
    if (source_total, retained_killed, len(structural), required_total, len(builder_probes)) != (48, 9, 6, 187, 10):
        raise AssertionError((source_total, retained_killed, len(structural), required_total, len(builder_probes)))

    print(json.dumps({
        "dec001_semantic_enforcement_mutations": {
            "executed": 27, "killed_for_semantic_reason": 27,
            "metadata_mismatch_kills": 0, "no_op": 0, "survivors": 0,
        },
        "dec002_semantic_enforcement_mutations": {
            "executed": 54, "killed_for_semantic_reason": 54,
            "metadata_mismatch_kills": 0, "no_op": 0, "survivors": 0,
        },
        "dec003_semantic_enforcement_mutations": {
            "executed": 43, "killed_for_semantic_reason": 43,
            "metadata_mismatch_kills": 0, "no_op": 0, "survivors": 0,
        },
        "cumulative_semantic_enforcement_mutations": {"executed": 124, "killed": 124, "survivors": 0},
        "source_derived_mutations": {**source_mutations, "executed": 48, "killed": 48, "survivors": 0},
        "retained_identity_mutations": {"executed": 9, "killed": 9, "survivors": 0},
        "structural_mutations": {"executed": 6, "killed": 6, "survivors": 0},
        "required_total_mutations": {"executed": 187, "killed": 187, "survivors": 0, "wrong_reason": 0, "metadata_only": 0, "no_op": 0, "parse_error_semantic_kills": 0},
        "focused_regressions": {"executed": 42, "killed": 42, "survivors": 0},
        "actual_modified_builder_executions": {"executed": 10, "rejected": 10, "coherent_defective_survivors": 0},
        "mutated_rule_ids": mutated_rules,
        "repository_candidate_unchanged": True,
    }, sort_keys=True))
    print("VALID_C2_R2_FINAL_187_MUTATIONS_42_REGRESSIONS_10_MODIFIED_BUILDERS")


if __name__ == "__main__":
    main()
