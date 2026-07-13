from pathlib import Path

from ysf.frontend.verifier import (
    BASELINE_FILE,
    verify_frontend_foundation,
)

DESIGN_TOKENS = """
{
  "schemaVersion": "1.0",
  "theme": "ysim-green",
  "tokens": {
    "color": {
      "primary": "#2BA84A"
    },
    "typography": {
      "letterSpacing": 0
    },
    "focus": {
      "outlineColor": "color.focus"
    }
  }
}
"""

LOCALIZATION_RESOURCES = """
{
  "schemaVersion": "1.0",
  "fallbackLocale": "en",
  "locales": {
    "en": {
      "shell.brand": "YSim",
      "shell.skipToContent": "Skip to content",
      "shell.admin.home": "Admin overview",
      "shell.storefront.home": "Travel eSIM",
      "shell.status.ready": "Ready"
    },
    "vi": {
      "shell.brand": "YSim"
    }
  }
}
"""

RUNTIME_CONTEXT = """
{
  "schemaVersion": "1.0",
  "fields": {
    "organization": {},
    "storefront": {},
    "locale": {},
    "currency": {},
    "theme": {},
    "tracking": {},
    "preferences": {}
  }
}
"""

RUNTIME_CONTEXT_MISSING_PREFERENCES = """
{
  "schemaVersion": "1.0",
  "fields": {
    "organization": {},
    "storefront": {},
    "locale": {},
    "currency": {},
    "theme": {},
    "tracking": {}
  }
}
"""


def write_frontend_baseline(
    repository_root: Path,
    runtime_context: str = RUNTIME_CONTEXT,
) -> None:
    baseline_path = repository_root / BASELINE_FILE
    tokens_path = repository_root / "knowledge/ui/design-tokens.json"
    localization_path = (
        repository_root
        / "knowledge/ui/localization-resources.json"
    )
    runtime_context_path = (
        repository_root
        / "knowledge/ui/runtime-context.json"
    )

    baseline_path.parent.mkdir(parents=True)
    tokens_path.parent.mkdir(parents=True)

    baseline_path.write_text(
        """
schemaVersion: "1.0"
applications:
  admin-web:
    buildCommand: pnpm --filter admin-web build
    consumes:
      - "@ysim/design-tokens"
      - "@ysim/ui"
      - "@ysim/runtime-context"
      - "@ysim/localization"
    shell:
      navigation:
        responsive: true
        keyboard: true
        focusVisible: true
  storefront-web:
    buildCommand: pnpm --filter storefront-web build
    consumes:
      - "@ysim/design-tokens"
      - "@ysim/ui"
      - "@ysim/runtime-context"
      - "@ysim/localization"
    shell:
      navigation:
        responsive: true
        keyboard: true
        focusVisible: true
packages:
  design-tokens: {}
  ui: {}
  runtime-context: {}
  localization: {}
theme:
  tokenContract: knowledge/ui/design-tokens.json
localization:
  resourceContract: knowledge/ui/localization-resources.json
runtimeContext:
  contract: knowledge/ui/runtime-context.json
accessibility:
  skipLink: true
  keyboardNavigation: true
  visibleFocus: true
  ariaLandmarks: true
  minTouchTargetPx: 44
  colorContrast: WCAG-AA
responsive:
  breakpoints:
    mobile: 360
    tablet: 768
    laptop: 1024
    desktop: 1280
    wide: 1536
""",
        encoding="utf-8",
    )
    tokens_path.write_text(DESIGN_TOKENS, encoding="utf-8")
    localization_path.write_text(
        LOCALIZATION_RESOURCES,
        encoding="utf-8",
    )
    runtime_context_path.write_text(
        runtime_context,
        encoding="utf-8",
    )


def test_verify_frontend_foundation_passes_for_baseline(
    tmp_path: Path,
) -> None:
    write_frontend_baseline(tmp_path)

    result = verify_frontend_foundation(
        tmp_path
    )

    assert result.successful
    assert result.data["failedChecks"] == []


def test_verify_frontend_foundation_rejects_missing_runtime_field(
    tmp_path: Path,
) -> None:
    write_frontend_baseline(
        tmp_path,
        runtime_context=RUNTIME_CONTEXT_MISSING_PREFERENCES,
    )

    result = verify_frontend_foundation(
        tmp_path
    )

    assert not result.successful
    assert (
        "runtime-context-required-fields"
        in result.data["failedChecks"]
    )


def test_verify_frontend_foundation_rejects_prohibited_context_field(
    tmp_path: Path,
) -> None:
    write_frontend_baseline(
        tmp_path,
        runtime_context=RUNTIME_CONTEXT.replace(
            '    "preferences": {}\n',
            (
                '    "preferences": {},\n'
                '    "providerProduct": {}\n'
            ),
        ),
    )

    result = verify_frontend_foundation(
        tmp_path
    )

    assert not result.successful
    assert (
        "runtime-context-no-prohibited-fields"
        in result.data["failedChecks"]
    )
