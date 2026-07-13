from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from ysf.core.result import CommandResult

BASELINE_FILE = Path("factory/config/frontend-foundation.yaml")
EXPECTED_APPS = {"admin-web", "storefront-web"}
EXPECTED_PACKAGES = {
    "design-tokens",
    "ui",
    "runtime-context",
    "localization",
}
EXPECTED_CONTEXT_FIELDS = {
    "organization",
    "storefront",
    "locale",
    "currency",
    "theme",
    "tracking",
    "preferences",
}
EXPECTED_LOCALES = {"en", "vi"}
PROHIBITED_CONTEXT_FIELDS = {
    "providerSystem",
    "providerProduct",
    "providerMapping",
    "providerRouting",
}


def _load_yaml(path: Path) -> dict[str, Any]:
    loaded = yaml.safe_load(path.read_text(encoding="utf-8"))

    if not isinstance(loaded, dict):
        msg = f"{path} must contain a YAML mapping."
        raise ValueError(msg)

    return loaded


def _load_json(path: Path) -> dict[str, Any]:
    loaded = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(loaded, dict):
        msg = f"{path} must contain a JSON object."
        raise ValueError(msg)

    return loaded


def verify_frontend_foundation(
    repository_root: Path,
) -> CommandResult:
    baseline_path = repository_root / BASELINE_FILE
    checks: list[dict[str, Any]] = [{
        "name": "frontend-config-exists",
        "status": "PASS" if baseline_path.is_file() else "FAIL",
        "path": str(BASELINE_FILE),
    }]

    if baseline_path.is_file():
        config = _load_yaml(baseline_path)
        checks.extend(_baseline_checks(repository_root, config))

    failed_checks = [
        check["name"]
        for check in checks
        if check["status"] != "PASS"
    ]
    status = "PASS" if not failed_checks else "FAIL"

    return CommandResult(
        command="frontend-foundation",
        status=status,
        message=(
            "Frontend foundation baseline is valid."
            if status == "PASS"
            else "Frontend foundation baseline is invalid."
        ),
        data={
            "configFile": str(BASELINE_FILE),
            "checkCount": len(checks),
            "failedCheckCount": len(failed_checks),
            "failedChecks": failed_checks,
            "checks": checks,
        },
    )


def _baseline_checks(
    repository_root: Path,
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    checks.extend(_application_checks(config))
    checks.extend(_package_checks(config))
    checks.extend(_accessibility_checks(config))
    checks.extend(_responsive_checks(config))
    checks.extend(_token_checks(repository_root, config))
    checks.extend(_localization_checks(repository_root, config))
    checks.extend(_runtime_context_checks(repository_root, config))

    return checks


def _application_checks(
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    applications = config.get("applications", {})
    app_names = (
        set(applications)
        if isinstance(applications, dict)
        else set()
    )
    checks: list[dict[str, Any]] = [{
        "name": "frontend-application-set",
        "status": (
            "PASS"
            if app_names == EXPECTED_APPS
            else "FAIL"
        ),
        "applications": sorted(app_names),
    }]

    if not isinstance(applications, dict):
        return checks

    for app_name in EXPECTED_APPS:
        app = applications.get(app_name, {})
        shell = (
            app.get("shell", {})
            if isinstance(app, dict)
            else {}
        )
        navigation = (
            shell.get("navigation", {})
            if isinstance(shell, dict)
            else {}
        )
        consumes = (
            app.get("consumes", [])
            if isinstance(app, dict)
            else []
        )

        checks.append({
            "name": f"{app_name}-build-command",
            "status": (
                "PASS"
                if isinstance(app.get("buildCommand"), str)
                and "pnpm --filter" in app["buildCommand"]
                else "FAIL"
            ),
        })
        checks.append({
            "name": f"{app_name}-shared-package-consumption",
            "status": (
                "PASS"
                if isinstance(consumes, list)
                and {
                    "@ysim/design-tokens",
                    "@ysim/ui",
                    "@ysim/runtime-context",
                    "@ysim/localization",
                }.issubset(set(consumes))
                else "FAIL"
            ),
        })
        checks.append({
            "name": f"{app_name}-accessible-navigation",
            "status": (
                "PASS"
                if (
                    isinstance(navigation, dict)
                    and navigation.get("responsive") is True
                    and navigation.get("keyboard") is True
                    and navigation.get("focusVisible") is True
                )
                else "FAIL"
            ),
        })

    return checks


def _package_checks(
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    packages = config.get("packages", {})
    package_names = (
        set(packages)
        if isinstance(packages, dict)
        else set()
    )

    return [{
        "name": "frontend-package-set",
        "status": (
            "PASS"
            if package_names == EXPECTED_PACKAGES
            else "FAIL"
        ),
        "packages": sorted(package_names),
    }]


def _accessibility_checks(
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    accessibility = config.get("accessibility", {})
    required_flags = (
        "skipLink",
        "keyboardNavigation",
        "visibleFocus",
        "ariaLandmarks",
    )

    return [{
        "name": "accessibility-defaults",
        "status": (
            "PASS"
            if (
                isinstance(accessibility, dict)
                and all(
                    accessibility.get(flag) is True
                    for flag in required_flags
                )
                and accessibility.get("minTouchTargetPx", 0) >= 44
                and accessibility.get("colorContrast") == "WCAG-AA"
            )
            else "FAIL"
        ),
    }]


def _responsive_checks(
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    responsive = config.get("responsive", {})
    breakpoints = (
        responsive.get("breakpoints", {})
        if isinstance(responsive, dict)
        else {}
    )
    expected = {"mobile", "tablet", "laptop", "desktop", "wide"}

    return [{
        "name": "responsive-breakpoints",
        "status": (
            "PASS"
            if (
                isinstance(breakpoints, dict)
                and expected.issubset(set(breakpoints))
                and all(
                    isinstance(value, int)
                    and value > 0
                    for value in breakpoints.values()
                )
            )
            else "FAIL"
        ),
    }]


def _token_checks(
    repository_root: Path,
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    theme = config.get("theme", {})
    token_contract = (
        theme.get("tokenContract")
        if isinstance(theme, dict)
        else None
    )
    token_path = (
        repository_root / token_contract
        if isinstance(token_contract, str)
        else Path()
    )
    checks: list[dict[str, Any]] = [{
        "name": "design-token-contract-exists",
        "status": (
            "PASS"
            if token_contract
            and token_path.is_file()
            else "FAIL"
        ),
        "path": token_contract,
    }]

    if not token_contract or not token_path.is_file():
        return checks

    document = _load_json(token_path)
    tokens = document.get("tokens", {})
    colors = (
        tokens.get("color", {})
        if isinstance(tokens, dict)
        else {}
    )
    typography = (
        tokens.get("typography", {})
        if isinstance(tokens, dict)
        else {}
    )
    focus = (
        tokens.get("focus", {})
        if isinstance(tokens, dict)
        else {}
    )

    checks.append({
        "name": "ysim-green-default-theme",
        "status": (
            "PASS"
            if (
                document.get("theme") == "ysim-green"
                and colors.get("primary") == "#2BA84A"
            )
            else "FAIL"
        ),
    })
    checks.append({
        "name": "token-accessibility-values",
        "status": (
            "PASS"
            if (
                typography.get("letterSpacing") == 0
                and focus.get("outlineColor") == "color.focus"
            )
            else "FAIL"
        ),
    })

    return checks


def _localization_checks(
    repository_root: Path,
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    localization = config.get("localization", {})
    resource_contract = (
        localization.get("resourceContract")
        if isinstance(localization, dict)
        else None
    )
    resource_path = (
        repository_root / resource_contract
        if isinstance(resource_contract, str)
        else Path()
    )
    checks: list[dict[str, Any]] = [{
        "name": "localization-resource-contract-exists",
        "status": (
            "PASS"
            if resource_contract
            and resource_path.is_file()
            else "FAIL"
        ),
        "path": resource_contract,
    }]

    if not resource_contract or not resource_path.is_file():
        return checks

    resources = _load_json(resource_path)
    locales = resources.get("locales", {})
    fallback_locale = resources.get("fallbackLocale")
    locale_names = (
        set(locales)
        if isinstance(locales, dict)
        else set()
    )
    fallback_keys = (
        set(locales.get(fallback_locale, {}))
        if isinstance(locales, dict)
        and isinstance(locales.get(fallback_locale), dict)
        else set()
    )

    checks.append({
        "name": "localization-fallback-locale",
        "status": (
            "PASS"
            if fallback_locale == "en"
            else "FAIL"
        ),
    })
    checks.append({
        "name": "localization-locale-set",
        "status": (
            "PASS"
            if EXPECTED_LOCALES.issubset(locale_names)
            else "FAIL"
        ),
        "locales": sorted(locale_names),
    })
    checks.append({
        "name": "localization-fallback-covers-visible-shell",
        "status": (
            "PASS"
            if {
                "shell.brand",
                "shell.skipToContent",
                "shell.admin.home",
                "shell.storefront.home",
                "shell.status.ready",
            }.issubset(fallback_keys)
            else "FAIL"
        ),
    })

    return checks


def _runtime_context_checks(
    repository_root: Path,
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    runtime_context = config.get("runtimeContext", {})
    contract = (
        runtime_context.get("contract")
        if isinstance(runtime_context, dict)
        else None
    )
    contract_path = (
        repository_root / contract
        if isinstance(contract, str)
        else Path()
    )
    checks: list[dict[str, Any]] = [{
        "name": "runtime-context-contract-exists",
        "status": (
            "PASS"
            if contract
            and contract_path.is_file()
            else "FAIL"
        ),
        "path": contract,
    }]

    if not contract or not contract_path.is_file():
        return checks

    document = _load_json(contract_path)
    fields = document.get("fields", {})
    field_names = (
        set(fields)
        if isinstance(fields, dict)
        else set()
    )
    content = contract_path.read_text(encoding="utf-8")

    checks.append({
        "name": "runtime-context-required-fields",
        "status": (
            "PASS"
            if EXPECTED_CONTEXT_FIELDS.issubset(field_names)
            else "FAIL"
        ),
        "fields": sorted(field_names),
    })
    checks.append({
        "name": "runtime-context-no-prohibited-fields",
        "status": (
            "PASS"
            if (
                PROHIBITED_CONTEXT_FIELDS.isdisjoint(field_names)
                and not any(
                    prohibited in content
                    for prohibited in PROHIBITED_CONTEXT_FIELDS
                )
            )
            else "FAIL"
        ),
    })

    return checks
