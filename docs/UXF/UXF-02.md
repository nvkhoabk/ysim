---
document_code: "UXF-02"
title: "Design System, Theme & Experience Inheritance"
product_baseline: "2.3"
document_revision: "2.3.0-draft.1"
lifecycle_status: "V2.3_DRAFT"
language: "en"
source_baseline: "v2.2"
generated_registry_role: "UXF_CANONICAL_SOURCE"
last_remediated_on: "2026-07-15"
---
## v2.3 requirement authority

The `YSIM:REQUIREMENT` blocks in the normative appendix are authoritative for baseline 2.3. Legacy prose is retained as context; approved v2.3 decisions and the normative blocks take precedence where wording differs.

# UXF-02 — Design System, Theme & Experience Inheritance

---

# 1. Purpose

This document defines the Design Runtime Architecture used by the YSim Platform.

Unlike traditional frontend systems where themes only control visual appearance, YSim themes represent configurable experience layers that participate in runtime rendering.

This document specifies:

- Design System
- Design Tokens
- Theme Architecture
- Experience Profiles
- Theme Inheritance
- Fallback Strategy
- Asset Resolution
- Component Registry
- UI Composition Rules

---

# 2. Design Philosophy

The YSim Platform follows a **Single Design System** strategy.

All applications share the same visual language.

Applications include:

- Platform Portal
- Administration Portal
- Organization Portal
- Agency Portal
- Customer Portal
- White-label Storefront
- Embedded Commerce

No application may create an isolated component library.

---

# 3. Design Runtime

Rendering follows the Design Runtime pipeline.

```
Experience Context

↓

Theme Resolver

↓

Design Token Resolver

↓

Asset Resolver

↓

Component Registry

↓

Layout Resolver

↓

Rendered UI
```

Visual appearance is resolved dynamically.

---

# 4. Design System Layers

```
Design Tokens

↓

Theme

↓

Experience Profile

↓

Layout

↓

Components

↓

Pages

↓

Applications
```

Each layer depends only on its parent.

---

# 5. Design Tokens

The platform defines immutable Design Tokens.

Token categories include:

## Color

- Primary
- Secondary
- Accent
- Success
- Warning
- Error
- Background
- Surface
- Border
- Text
- Muted

---

## Typography

- Heading Font
- Body Font
- Code Font
- Font Scale
- Line Height
- Letter Spacing

---

## Layout

- Grid
- Container Width
- Radius
- Elevation
- Shadow
- Spacing
- Breakpoints

---

## Motion

- Transition
- Animation
- Hover
- Focus
- Loading
- Skeleton

---

## Icons

- Icon Set
- Size
- Weight
- Filled
- Outlined

---

# 6. Theme

A Theme is a configuration object.

A Theme is **NOT** a stylesheet.

Example:

```
Theme

├── Color Tokens

├── Typography

├── Icons

├── Illustration Style

├── Card Style

├── Navigation Style

├── Button Style

├── Input Style

├── Animation Profile

└── Assets
```

---

# 7. Theme Presets

The platform provides several built-in presets.

Recommended presets:

- YSim Green
- Ocean Blue
- Sunset Orange
- Ruby Red
- Violet
- Minimal White

Organizations may derive custom themes from these presets.

---

# 8. Experience Profile

A Theme only defines appearance.

An Experience Profile defines behavior.

Example:

```
Experience Profile

├── Theme

├── Navigation Profile

├── Hero Style

├── CTA Style

├── Content Density

├── Component Visibility

├── Interaction Style

├── Asset Profile

└── Motion Profile
```

Different Storefronts may share the same Theme while using different Experience Profiles.

---

# 9. Theme Inheritance

Themes support inheritance.

```
Platform Theme

↓

Organization Theme

↓

Storefront Theme

↓

Campaign Theme

↓

Runtime Override
```

Each level overrides only required properties.

---

# 10. Experience Inheritance

Experience inheritance extends beyond themes.

Inherited objects include:

- Theme
- Assets
- Navigation
- Typography
- Component Visibility
- Hero
- CTA
- Empty States
- Loading Style
- Icons
- Motion

Experience inheritance is resolved independently for every request.

---

# 11. Fallback Strategy

If a configuration cannot be resolved, runtime falls back to the nearest valid parent.

```
Runtime Override

↓

Campaign

↓

Storefront

↓

Organization

↓

Platform
```

Fallback applies to every configurable property.

No incomplete configuration may break rendering.

---

# 12. Asset Management

Assets are runtime resources.

Supported asset categories:

- Logo
- Favicon
- Hero Image
- Banner
- Background
- Illustration
- Icons
- Email Branding
- Social Preview
- Empty State Graphics

Assets are referenced by identifier rather than embedded.

---

# 13. Asset Resolution

Runtime asset resolution:

```
Platform Assets

↓

Organization Assets

↓

Storefront Assets

↓

Campaign Assets

↓

Runtime Assets
```

Asset resolution follows the same inheritance model as themes.

---

# 14. Component Registry

Every UI component belongs to a shared registry.

```
packages/ui

├── Layout

├── Navigation

├── Form

├── Table

├── Chart

├── Dialog

├── Notification

├── Card

├── Commerce

├── Storefront

└── Shared
```

Components are reusable across all channels.

---

# 15. Component Composition

Pages are assembled using components.

```
Page

↓

Sections

↓

Components

↓

Business Data

↓

Rendering
```

Components remain presentation-only.

Business logic belongs to application services.

---

# 16. Component Visibility

Visibility is configurable.

Example:

```
Hero

Enabled

↓

Storefront A

Disabled

↓

Storefront B
```

Component visibility may depend on:

- Storefront
- Campaign
- Locale
- Feature Flag
- Device

---

# 17. Design Tokens vs Business Configuration

The Design System controls presentation only.

Business behavior is configured separately.

Example:

```
Theme

↓

Primary Button Color
```

does not determine

```
Checkout Policy
```

Business configuration remains independent.

---

# 18. Design Accessibility

Every component must support:

- Keyboard Navigation
- Screen Readers
- Responsive Layout
- High Contrast
- Focus Indicators
- Touch Interaction

Accessibility cannot be disabled by Themes.

---

# 19. Responsive Design

Responsive behavior follows Design Tokens.

Supported breakpoints:

- Mobile
- Tablet
- Laptop
- Desktop
- Wide Display

Applications remain functionally identical across devices.

---

# 20. Design Principles

### UXF-201

One platform uses one Design System.

---

### UXF-202

Themes are configuration objects.

---

### UXF-203

Experience Profiles extend Themes.

---

### UXF-204

Themes support inheritance.

---

### UXF-205

Every configurable property supports fallback.

---

### UXF-206

Assets participate in runtime resolution.

---

### UXF-207

Component libraries are shared across all applications.

---

### UXF-208

Business behavior is independent from presentation.

---

### UXF-209

Accessibility is mandatory.

---

### UXF-210

Responsive behavior is defined by Design Tokens.

---

# 21. AI Implementation Guidelines

When generating frontend code, AI agents shall:

- Never hardcode colors.
- Never hardcode fonts.
- Never hardcode logos.
- Never hardcode branding assets.
- Never duplicate UI components.
- Always consume Design Tokens.
- Always resolve Themes through the Theme Engine.
- Always support Experience Inheritance.
- Always support runtime fallback.
- Separate presentation from business logic.

---

# 22. References

This document should be read together with:

- UXF-00 — User Experience Foundation Overview
- UXF-01 — Experience Channels, Personas & Navigation
- UXF-03 — Storefront Template & Page Composition
- UXF-04 — White-label, Localization & Runtime Context Resolution
- UXF-05 — Storefront Runtime Architecture & Business Binding

- BRD
- ABP
- AFM
- YADF
- DIP

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## v2.3 normative requirement appendix



<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-02-R001 — Each level overrides only required properties

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-02-R001-AC001",
      "given": "a user in the applicable channel and context for Each level overrides only required properties",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-02-R001-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R001-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-02-R001-O001",
      "obligation_text": "Each level overrides only required properties"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-030",
      "selected_disposition": "CONFIRM_NORMAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Each level overrides only required properties.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-02-001",
    "previous_temporary_key": "TMP-UXF-02-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Theme Inheritance",
    "source_context_sha256": "5dc9e734b8b4aebf62c32b62531fea465e9103546d9064c2de61035cc1cad474",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "ff2f28e78e949a0660ada234089bb62088e42b28e4b9df1593baf2afbb092ee3",
    "source_lines": "L302",
    "source_section": "9. Theme Inheritance"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-02-R001",
  "title": "Each level overrides only required properties",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-02-R002 — If a configuration cannot be resolved, runtime falls back to the nearest valid parent

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-02-R002-AC001",
      "given": "a user in the applicable channel and context for If a configuration cannot be resolved, runtime falls back to the nearest valid parent",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-02-R002-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-02-R002-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for If a configuration cannot be resolved, runtime falls back to the nearest valid parent",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-02-R002-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R002-AC001",
        "UXF-02-R002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-02-R002-O001",
      "obligation_text": "If a configuration cannot be resolved, runtime falls back to the nearest valid parent"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "If a configuration cannot be resolved, runtime falls back to the nearest valid parent.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-02-002",
    "previous_temporary_key": "TMP-UXF-02-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Fallback Strategy",
    "source_context_sha256": "3cee0633abdf2029603658d7939f9f631c05d647109c5ba337daf2dc390c5564",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "3cd3bf3026049326881f933c933bbdda3dbd18d69fd20fc8c229d3e85473ef24",
    "source_lines": "L330",
    "source_section": "11. Fallback Strategy"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-02-R002",
  "title": "If a configuration cannot be resolved, runtime falls back to the nearest valid parent",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-02-R003 — Every component must support: - Keyboard Navigation

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "ACCESSIBILITY_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-02-R003-AC001",
      "given": "the experience state and accessibility mode governed by Every component must support: - Keyboard Navigation",
      "observable_evidence": "before/after rendered state, enabled accessibility mode, available content and actions, interaction outcome, and any accessibility conformance result declared by the source",
      "then": "the accessible rendering or interaction is available without removing required content or actions, and its outcome remains perceivable and operable",
      "verifies": [
        "UXF-02-R003-O001"
      ],
      "when": "the named accessibility capability is enabled and the same content and actions are exercised"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "ACCESSIBILITY_CONFORMANCE_FAILURE_V1",
      "criterion_id": "UXF-02-R003-AC002",
      "given": "the experience with the accessibility capability named by Every component must support: - Keyboard Navigation unavailable or producing inaccessible content or actions",
      "observable_evidence": "enabled mode, rendered state, affected content or action, interaction result, and failed accessibility conformance evidence",
      "then": "accessibility conformance fails with the unavailable capability or inaccessible element identified; the state is not reported as conforming",
      "verifies": [
        "UXF-02-R003-O001"
      ],
      "when": "the applicable accessibility mode or interaction is used"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R003-AC001",
        "UXF-02-R003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-02-R003-O001",
      "obligation_text": "Every component must support: - Keyboard Navigation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every component must support: - Keyboard Navigation",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-02-003",
    "previous_temporary_key": "TMP-UXF-02-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Design Accessibility",
    "source_context_sha256": "005d03136b01fbfc51aecdb4957e3fd361c068c92883677b8242c37948911b84",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "efbb5c92b988996fa766f2e8eeba00eaf4f815406e98cb746742ed8783ca3084",
    "source_lines": "L531-L533",
    "source_section": "18. Design Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "ACCESSIBILITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-02-R003",
  "title": "Every component must support: - Keyboard Navigation",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-02-R004 — Every component must support: - Screen Readers

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "ACCESSIBILITY_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-02-R004-AC001",
      "given": "the experience state and accessibility mode governed by Every component must support: - Screen Readers",
      "observable_evidence": "before/after rendered state, enabled accessibility mode, available content and actions, interaction outcome, and any accessibility conformance result declared by the source",
      "then": "the accessible rendering or interaction is available without removing required content or actions, and its outcome remains perceivable and operable",
      "verifies": [
        "UXF-02-R004-O001"
      ],
      "when": "the named accessibility capability is enabled and the same content and actions are exercised"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "ACCESSIBILITY_CONFORMANCE_FAILURE_V1",
      "criterion_id": "UXF-02-R004-AC002",
      "given": "the experience with the accessibility capability named by Every component must support: - Screen Readers unavailable or producing inaccessible content or actions",
      "observable_evidence": "enabled mode, rendered state, affected content or action, interaction result, and failed accessibility conformance evidence",
      "then": "accessibility conformance fails with the unavailable capability or inaccessible element identified; the state is not reported as conforming",
      "verifies": [
        "UXF-02-R004-O001"
      ],
      "when": "the applicable accessibility mode or interaction is used"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R004-AC001",
        "UXF-02-R004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-02-R004-O001",
      "obligation_text": "Every component must support: - Screen Readers"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every component must support: - Screen Readers",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-02-004",
    "previous_temporary_key": "TMP-UXF-02-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Design Accessibility",
    "source_context_sha256": "005d03136b01fbfc51aecdb4957e3fd361c068c92883677b8242c37948911b84",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "646d186836291a4c69bec732b7ea52f538af18fabbe854d499cd4e009d77fce4",
    "source_lines": "L531-L534",
    "source_section": "18. Design Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "ACCESSIBILITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-02-R004",
  "title": "Every component must support: - Screen Readers",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-02-R005 — Every component must support: - Responsive Layout

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-02-R005-AC001",
      "given": "a user in the applicable channel and context for Every component must support: - Responsive Layout",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-02-R005-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-02-R005-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every component must support: - Responsive Layout",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-02-R005-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R005-AC001",
        "UXF-02-R005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-02-R005-O001",
      "obligation_text": "Every component must support: - Responsive Layout"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every component must support: - Responsive Layout",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-02-005",
    "previous_temporary_key": "TMP-UXF-02-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Design Accessibility",
    "source_context_sha256": "005d03136b01fbfc51aecdb4957e3fd361c068c92883677b8242c37948911b84",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "40cd7a7e8d060d8d29f2dec8bffc1c4d988c9f5421dc2ea10e835164c5070c68",
    "source_lines": "L531-L535",
    "source_section": "18. Design Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-02-R005",
  "title": "Every component must support: - Responsive Layout",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-02-R006 — Every component must support: - High Contrast

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "ACCESSIBILITY_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-02-R006-AC001",
      "given": "the experience state and accessibility mode governed by Every component must support: - High Contrast",
      "observable_evidence": "before/after rendered state, enabled accessibility mode, available content and actions, interaction outcome, and any accessibility conformance result declared by the source",
      "then": "the accessible rendering or interaction is available without removing required content or actions, and its outcome remains perceivable and operable",
      "verifies": [
        "UXF-02-R006-O001"
      ],
      "when": "the named accessibility capability is enabled and the same content and actions are exercised"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "ACCESSIBILITY_CONFORMANCE_FAILURE_V1",
      "criterion_id": "UXF-02-R006-AC002",
      "given": "the experience with the accessibility capability named by Every component must support: - High Contrast unavailable or producing inaccessible content or actions",
      "observable_evidence": "enabled mode, rendered state, affected content or action, interaction result, and failed accessibility conformance evidence",
      "then": "accessibility conformance fails with the unavailable capability or inaccessible element identified; the state is not reported as conforming",
      "verifies": [
        "UXF-02-R006-O001"
      ],
      "when": "the applicable accessibility mode or interaction is used"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R006-AC001",
        "UXF-02-R006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-02-R006-O001",
      "obligation_text": "Every component must support: - High Contrast"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every component must support: - High Contrast",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-02-006",
    "previous_temporary_key": "TMP-UXF-02-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Design Accessibility",
    "source_context_sha256": "005d03136b01fbfc51aecdb4957e3fd361c068c92883677b8242c37948911b84",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "4e97038ab2333b346cfcc4ae9175480315dd6da17fd5c537bd317fbb9380de4b",
    "source_lines": "L531-L536",
    "source_section": "18. Design Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "ACCESSIBILITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-02-R006",
  "title": "Every component must support: - High Contrast",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-02-R007 — Every component must support: - Focus Indicators

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-02-R007-AC001",
      "given": "a user in the applicable channel and context for Every component must support: - Focus Indicators",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-02-R007-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-02-R007-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every component must support: - Focus Indicators",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-02-R007-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R007-AC001",
        "UXF-02-R007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-02-R007-O001",
      "obligation_text": "Every component must support: - Focus Indicators"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every component must support: - Focus Indicators",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-02-007",
    "previous_temporary_key": "TMP-UXF-02-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Design Accessibility",
    "source_context_sha256": "005d03136b01fbfc51aecdb4957e3fd361c068c92883677b8242c37948911b84",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "f5d66b351e58194c70d1923bd217005efb97e30edf0fe34170872bf41aa175b5",
    "source_lines": "L531-L537",
    "source_section": "18. Design Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-02-R007",
  "title": "Every component must support: - Focus Indicators",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-02-R008 — Every component must support: - Touch Interaction

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-02-R008-AC001",
      "given": "a user in the applicable channel and context for Every component must support: - Touch Interaction",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-02-R008-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-02-R008-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every component must support: - Touch Interaction",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-02-R008-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R008-AC001",
        "UXF-02-R008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-02-R008-O001",
      "obligation_text": "Every component must support: - Touch Interaction"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every component must support: - Touch Interaction",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-02-008",
    "previous_temporary_key": "TMP-UXF-02-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Design Accessibility",
    "source_context_sha256": "005d03136b01fbfc51aecdb4957e3fd361c068c92883677b8242c37948911b84",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "d66da1fbef66ac045aa392985dc6ecfd0d1dfdccb410b078cb7d334a917f9182",
    "source_lines": "L531-L538",
    "source_section": "18. Design Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-02-R008",
  "title": "Every component must support: - Touch Interaction",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-02-R009 — Accessibility cannot be disabled by Themes

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "ACCESSIBILITY_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-02-R009-AC001",
      "given": "the experience state and accessibility mode governed by Accessibility cannot be disabled by Themes",
      "observable_evidence": "before/after rendered state, enabled accessibility mode, available content and actions, interaction outcome, and any accessibility conformance result declared by the source",
      "then": "the accessible rendering or interaction is available without removing required content or actions, and its outcome remains perceivable and operable",
      "verifies": [
        "UXF-02-R009-O001"
      ],
      "when": "the named accessibility capability is enabled and the same content and actions are exercised"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "ACCESSIBILITY_CONFORMANCE_FAILURE_V1",
      "criterion_id": "UXF-02-R009-AC002",
      "given": "the experience with the accessibility capability named by Accessibility cannot be disabled by Themes unavailable or producing inaccessible content or actions",
      "observable_evidence": "enabled mode, rendered state, affected content or action, interaction result, and failed accessibility conformance evidence",
      "then": "accessibility conformance fails with the unavailable capability or inaccessible element identified; the state is not reported as conforming",
      "verifies": [
        "UXF-02-R009-O001"
      ],
      "when": "the applicable accessibility mode or interaction is used"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R009-AC001",
        "UXF-02-R009-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-02-R009-O001",
      "obligation_text": "Accessibility cannot be disabled by Themes"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-031",
      "selected_disposition": "CONFIRM_HIGH"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Accessibility cannot be disabled by Themes.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-02-009",
    "previous_temporary_key": "TMP-UXF-02-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Design Accessibility",
    "source_context_sha256": "005d03136b01fbfc51aecdb4957e3fd361c068c92883677b8242c37948911b84",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "d27ea5dc7317fe49df4515b2158c294433af56d1cb2c82e9b2cd97edef310640",
    "source_lines": "L540",
    "source_section": "18. Design Accessibility"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "ACCESSIBILITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-02-R009",
  "title": "Accessibility cannot be disabled by Themes",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-201 — One platform uses one Design System

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-201-AC001",
      "given": "a user in the applicable channel and context for One platform uses one Design System",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-201-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-201-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for One platform uses one Design System",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-201-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-201-AC001",
        "UXF-201-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-201-O001",
      "obligation_text": "One platform uses one Design System"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "One platform uses one Design System.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-201",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-201",
    "source_context_sha256": "4248e919b7a92402cb8bf1101d8ae98dedffa3b0f5c3b6c5e9e98e3d50bd4699",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "d88247dc3155ce90c93042b273dfc35ee79e8f17934b9325f4a6c08689bc2497",
    "source_lines": "L562-L565",
    "source_section": "20. Design Principles > UXF-201"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-201",
  "title": "One platform uses one Design System",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-202 — Themes are versioned configuration objects rather than source-code variants

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "UXF-202-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Themes are versioned configuration objects rather than source-code variants",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance evidence identifies the governing configuration and shows that an approved configuration change alters the governed result without a source-code variant",
      "verifies": [
        "UXF-202-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-202-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-202-O001",
      "obligation_text": "Themes are versioned configuration objects rather than source-code variants"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-039",
      "selected_disposition": "ROUTE_TO_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Themes are versioned configuration objects rather than source-code variants.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-202",
    "previous_temporary_key": null,
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-202",
    "source_context_sha256": "70554271efc30f67ac846911b1d3d9a3c6b4cb1186dd5ec6af4624f0e5591ca1",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "6381b8b1454608536dc94487be94b75e703cfabb73923aa17c91fb4eb106749f",
    "source_lines": "L568-L571",
    "source_section": "20. Design Principles > UXF-202"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-202",
  "title": "Themes are versioned configuration objects rather than source-code variants",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-203 — Experience Profiles extend Themes through governed configuration

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "UXF-203-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Experience Profiles extend Themes through governed configuration",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance evidence identifies the governing configuration and shows that an approved configuration change alters the governed result without a source-code variant",
      "verifies": [
        "UXF-203-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-203-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-203-O001",
      "obligation_text": "Experience Profiles extend Themes through governed configuration"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-040",
      "selected_disposition": "ROUTE_TO_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Experience Profiles extend Themes through governed configuration.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-203",
    "previous_temporary_key": null,
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-203",
    "source_context_sha256": "2bc30fc1bead888652b7468c9678a3066c8990452e967979fbc446642db393f1",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "d32379ca5de696b63d8c4ff2ca56d306fa8643b26aea312fce3cba17e178b595",
    "source_lines": "L574-L577",
    "source_section": "20. Design Principles > UXF-203"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-203",
  "title": "Experience Profiles extend Themes through governed configuration",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-204 — Theme inheritance resolves deterministically through the approved configuration hierarchy

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "UXF-204-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Theme inheritance resolves deterministically through the approved configuration hierarchy",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance evidence identifies the governing configuration and shows that an approved configuration change alters the governed result without a source-code variant",
      "verifies": [
        "UXF-204-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-204-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-204-O001",
      "obligation_text": "Theme inheritance resolves deterministically through the approved configuration hierarchy"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-041",
      "selected_disposition": "ROUTE_TO_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Theme inheritance resolves deterministically through the approved configuration hierarchy.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-204",
    "previous_temporary_key": null,
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Theme Inheritance",
    "source_context_sha256": "5dc9e734b8b4aebf62c32b62531fea465e9103546d9064c2de61035cc1cad474",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "b4d646974deaf3be952211a8ba36437bcaf7b429c8b4962d4b52eee4657194a2",
    "source_lines": "L580-L583",
    "source_section": "20. Design Principles > UXF-204"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-204",
  "title": "Theme inheritance resolves deterministically through the approved configuration hierarchy",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-205 — Every configurable property supports fallback

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-205-AC001",
      "given": "a user in the applicable channel and context for Every configurable property supports fallback",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-205-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-205-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every configurable property supports fallback",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-205-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-205-AC001",
        "UXF-205-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-205-O001",
      "obligation_text": "Every configurable property supports fallback"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every configurable property supports fallback.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-205",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-205",
    "source_context_sha256": "0aa6cb83fef65e84ece116e231a46838af1754186867d52503389265df9e68ee",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "b1efdf8a5626ec522725a7f9c5fd147c1051743bf97791b48633cdfaf7d820f6",
    "source_lines": "L586-L589",
    "source_section": "20. Design Principles > UXF-205"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-205",
  "title": "Every configurable property supports fallback",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-206 — Assets participate in runtime resolution

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-206-AC001",
      "given": "a user in the applicable channel and context for Assets participate in runtime resolution",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-206-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-206-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Assets participate in runtime resolution",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-206-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-206-AC001",
        "UXF-206-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-206-O001",
      "obligation_text": "Assets participate in runtime resolution"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Assets participate in runtime resolution.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-206",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-206",
    "source_context_sha256": "92ed4e37693c4c6916dbf7f4d7343be7398e82e81a1fcf109079cd02d6a8f3e3",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "7302f56377ae7918d8bc95993e4735d734db941b76893e930b231ec2f6565f9c",
    "source_lines": "L592-L595",
    "source_section": "20. Design Principles > UXF-206"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-206",
  "title": "Assets participate in runtime resolution",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-207 — Component libraries are shared across all applications

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-207-AC001",
      "given": "a user in the applicable channel and context for Component libraries are shared across all applications",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-207-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-207-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Component libraries are shared across all applications",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-207-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-207-AC001",
        "UXF-207-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-207-O001",
      "obligation_text": "Component libraries are shared across all applications"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Component libraries are shared across all applications.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-207",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-207",
    "source_context_sha256": "274af73e9c245c7a1b3a201db3cae532b9bfa7f3a47bf37915907f58340ee04c",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "6a5f765181a11b894aef2372b5f4902bd7e4bced33a6548e370f29868766fb93",
    "source_lines": "L598-L601",
    "source_section": "20. Design Principles > UXF-207"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "UX_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-207",
  "title": "Component libraries are shared across all applications",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-208 — Business behavior remains independent from presentation composition

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "UXF-208-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Business behavior remains independent from presentation composition",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "UXF-208-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-208-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-208-O001",
      "obligation_text": "Business behavior remains independent from presentation composition"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-042",
      "selected_disposition": "ROUTE_TO_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business behavior remains independent from presentation composition.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-208",
    "previous_temporary_key": null,
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-208",
    "source_context_sha256": "d4d175ee3f61a413eac6184a502e4c0c1071c0bc7b76eae90cc454aa4ed990f0",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "0bc74316f7d4db9b48bf72b687b255a6941a34dc5bacdac92e2b2f9bced15866",
    "source_lines": "L604-L607",
    "source_section": "20. Design Principles > UXF-208"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-208",
  "title": "Business behavior remains independent from presentation composition",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-209 — Accessibility is mandatory

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "ACCESSIBILITY_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-209-AC001",
      "given": "the experience state and accessibility mode governed by Accessibility is mandatory",
      "observable_evidence": "before/after rendered state, enabled accessibility mode, available content and actions, interaction outcome, and any accessibility conformance result declared by the source",
      "then": "the accessible rendering or interaction is available without removing required content or actions, and its outcome remains perceivable and operable",
      "verifies": [
        "UXF-209-O001"
      ],
      "when": "the named accessibility capability is enabled and the same content and actions are exercised"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "ACCESSIBILITY_CONFORMANCE_FAILURE_V1",
      "criterion_id": "UXF-209-AC002",
      "given": "the experience with the accessibility capability named by Accessibility is mandatory unavailable or producing inaccessible content or actions",
      "observable_evidence": "enabled mode, rendered state, affected content or action, interaction result, and failed accessibility conformance evidence",
      "then": "accessibility conformance fails with the unavailable capability or inaccessible element identified; the state is not reported as conforming",
      "verifies": [
        "UXF-209-O001"
      ],
      "when": "the applicable accessibility mode or interaction is used"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-209-AC001",
        "UXF-209-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-209-O001",
      "obligation_text": "Accessibility is mandatory"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Accessibility is mandatory.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-209",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-209",
    "source_context_sha256": "3ec3e154e2514f1f8cb977d5567106ff41a872d7919d3a885dec673bbb8f2383",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "47d5cf0d2b9ba787c7919421eac0228594fba22381b7d6a86a679e5f55cdc92c",
    "source_lines": "L610-L613",
    "source_section": "20. Design Principles > UXF-209"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "ACCESSIBILITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-209",
  "title": "Accessibility is mandatory",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-210 — Responsive behavior is defined by Design Tokens

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "UXF-210-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Responsive behavior is defined by Design Tokens",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "UXF-210-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "UXF-210-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Responsive behavior is defined by Design Tokens",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "UXF-210-O001"
      ],
      "when": "the protected decision or action is attempted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-210-AC001",
        "UXF-210-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-210-O001",
      "obligation_text": "Responsive behavior is defined by Design Tokens"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-210 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-210 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-210 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "UXF-210 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-210-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-210 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Responsive behavior is defined by Design Tokens.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-210",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-210",
    "source_context_sha256": "cfbfe7eedba072c25a3ffff4d84032354f2b27bf8479deb28bcffe01b9f03fb8",
    "source_document": "docs/UXF/UXF-02.md",
    "source_fingerprint": "e170a425dc60222d14d0adf4ef04d24d23ce726a25d0bbb8c4498d318f9bdfde",
    "source_lines": "L616-L619",
    "source_section": "20. Design Principles > UXF-210"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-210",
  "title": "Responsive behavior is defined by Design Tokens",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
