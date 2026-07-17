---
document_code: "UXF-02"
document_id: "UXF-02"
title: "Design System, Theme & Experience Inheritance"
version: "2.3.0-draft.3"
document_revision: "2.3.0-draft.3"
status: "V2.3_DRAFT"
lifecycle_status: "V2.3_DRAFT"
language: "en"
baseline: "2.3"
product_baseline: "2.3"
source_lineage: "v2.2 + approved Phase 1/2A/2B + accepted Acceptance Model C1 + accepted Mapping C3"
source_baseline: "v2.2"
last_reviewed_date: "2026-07-15"
last_remediated_on: "2026-07-17"
applicable_scope: "V2.3_ACTIVE_AND_RETAINED_SCOPE_RECORDS"
generated_registry_role: "UXF_CANONICAL_SOURCE"
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

## v2.3 normative requirement appendix — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-02-R001 — Each level overrides only required properties

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-02-R001",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "ff2f28e78e949a0660ada234089bb62088e42b28e4b9df1593baf2afbb092ee3"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R001-AC001",
        "UXF-02-R001-AC002",
        "UXF-02-R001-AC003"
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
    "source_lines": "L671-L755",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-02-R001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-02-R002",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "3cd3bf3026049326881f933c933bbdda3dbd18d69fd20fc8c229d3e85473ef24"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R002-AC001",
        "UXF-02-R002-AC002",
        "UXF-02-R002-AC003"
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
    "source_lines": "L757-L832",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-02-R002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-02-R003",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "efbb5c92b988996fa766f2e8eeba00eaf4f815406e98cb746742ed8783ca3084"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R003-AC001",
        "UXF-02-R003-AC002",
        "UXF-02-R003-AC003"
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
    "source_lines": "L834-L909",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-02-R003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-02-R004",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "8aef9afb69a20df7da0d4221100e387a024b6a185e124ab65040a7ec11012bda"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R004-AC001",
        "UXF-02-R004-AC002",
        "UXF-02-R004-AC003"
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
    "source_fingerprint": "8aef9afb69a20df7da0d4221100e387a024b6a185e124ab65040a7ec11012bda",
    "source_lines": "L911-L986",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-02-R004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-02-R005",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "585d027ef135d99a8bd7e809d092ed4fecbe55a73de6fdce22c5c61ede0264da"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R005-AC001",
        "UXF-02-R005-AC002",
        "UXF-02-R005-AC003"
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
    "source_fingerprint": "585d027ef135d99a8bd7e809d092ed4fecbe55a73de6fdce22c5c61ede0264da",
    "source_lines": "L988-L1063",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-02-R005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-02-R006",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "1cffb584f29626086e3effb7aed86a130673f43fb4dc8ce87fef498d0bf3c9be"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R006-AC001",
        "UXF-02-R006-AC002",
        "UXF-02-R006-AC003"
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
    "source_fingerprint": "1cffb584f29626086e3effb7aed86a130673f43fb4dc8ce87fef498d0bf3c9be",
    "source_lines": "L1065-L1140",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-02-R006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-02-R007",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "c47f1a2ff4ef8a1297155aa5c7cb501b1205751497359e763269906ac13876a4"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R007-AC001",
        "UXF-02-R007-AC002",
        "UXF-02-R007-AC003"
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
    "source_fingerprint": "c47f1a2ff4ef8a1297155aa5c7cb501b1205751497359e763269906ac13876a4",
    "source_lines": "L1142-L1217",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-02-R007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-02-R008",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "c7779f2a44860ef0c8acf3b0b419a595ed7d6a660c980edf6a94bce4746869a6"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R008-AC001",
        "UXF-02-R008-AC002",
        "UXF-02-R008-AC003"
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
    "source_fingerprint": "c7779f2a44860ef0c8acf3b0b419a595ed7d6a660c980edf6a94bce4746869a6",
    "source_lines": "L1219-L1294",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-02-R008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-024",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-02-R009",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "d27ea5dc7317fe49df4515b2158c294433af56d1cb2c82e9b2cd97edef310640"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-02-R009-AC001",
        "UXF-02-R009-AC002",
        "UXF-02-R009-AC003"
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
    "source_lines": "L1296-L1384",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-02-R009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-201",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "e5d0c9e56a39d827e32929f391c2436d733981b7346bb48d2b66a26e2a2ff8c7"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-201-AC001",
        "UXF-201-AC002",
        "UXF-201-AC003"
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
    "source_fingerprint": "e5d0c9e56a39d827e32929f391c2436d733981b7346bb48d2b66a26e2a2ff8c7",
    "source_lines": "L1386-L1461",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-201"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-202",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "0e8459de723c9342d6b4a0adf0b85cae9fb9feff40f16002b0c9d4df4a7da50a"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-202-AC001",
        "UXF-202-AC002",
        "UXF-202-AC003"
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
    "source_fingerprint": "0e8459de723c9342d6b4a0adf0b85cae9fb9feff40f16002b0c9d4df4a7da50a",
    "source_lines": "L1463-L1550",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-202"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-203",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "7237113bffc1154f8b68bf88ee97715a76a7fe9daba50442c17eae3533c89367"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-203-AC001",
        "UXF-203-AC002",
        "UXF-203-AC003"
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
    "source_fingerprint": "7237113bffc1154f8b68bf88ee97715a76a7fe9daba50442c17eae3533c89367",
    "source_lines": "L1552-L1642",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-203"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R024"
    ]
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-204",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "cb4c20c6b920ffbf9f10b8507c6e9a20c070aa3e30309f7546287b360313869a"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-204-AC001",
        "UXF-204-AC002",
        "UXF-204-AC003"
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
    "source_fingerprint": "cb4c20c6b920ffbf9f10b8507c6e9a20c070aa3e30309f7546287b360313869a",
    "source_lines": "L1644-L1731",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-204"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-205",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "175793623c78f85cd1d30c574aa3f7b9c4c3115d0f4c53a693de4da44b744b69"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-205-AC001",
        "UXF-205-AC002",
        "UXF-205-AC003"
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
    "source_fingerprint": "175793623c78f85cd1d30c574aa3f7b9c4c3115d0f4c53a693de4da44b744b69",
    "source_lines": "L1733-L1808",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-205"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-206",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "d924a940c94b860bc036677c42fc3dd036cd58b3b7ef59f332c573c6fea3d111"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-206-AC001",
        "UXF-206-AC002",
        "UXF-206-AC003"
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
    "source_fingerprint": "d924a940c94b860bc036677c42fc3dd036cd58b3b7ef59f332c573c6fea3d111",
    "source_lines": "L1810-L1885",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-206"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-207",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "2ac7fcd36af17b23fe4f932aa8e9f456a14741cd2c26fc568751d72346dd822b"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-207-AC001",
        "UXF-207-AC002",
        "UXF-207-AC003"
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
    "source_fingerprint": "2ac7fcd36af17b23fe4f932aa8e9f456a14741cd2c26fc568751d72346dd822b",
    "source_lines": "L1887-L1962",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-207"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-208",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "ea3471c0d6794503d80a1ad88002be52b19d35f78d2d56d9bb5fb89ae319529d"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-208-AC001",
        "UXF-208-AC002",
        "UXF-208-AC003"
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
    "source_fingerprint": "ea3471c0d6794503d80a1ad88002be52b19d35f78d2d56d9bb5fb89ae319529d",
    "source_lines": "L1964-L2051",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-208"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-025",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-209",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "7b164066e6e54df0a706772cc1cff47aab3dc1e5f3fe9d65ad26b59e7fae0cd7"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-209-AC001",
        "UXF-209-AC002",
        "UXF-209-AC003"
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
    "source_fingerprint": "7b164066e6e54df0a706772cc1cff47aab3dc1e5f3fe9d65ad26b59e7fae0cd7",
    "source_lines": "L2053-L2132",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-209"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-210",
      "source_document": "docs/UXF/UXF-02.md",
      "source_fingerprint": "05bd715bb6a85af8de9a7ca10d386c03a51b8d13675fbcbbe088404ba3be691d"
    }
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "runtime_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-210-AC001",
        "UXF-210-AC002",
        "UXF-210-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-210-O001",
      "obligation_text": "Responsive behavior is defined by Design Tokens"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-210-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-210 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-210 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-210-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-210-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-210 does not define a recovery obligation."
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
    "source_fingerprint": "05bd715bb6a85af8de9a7ca10d386c03a51b8d13675fbcbbe088404ba3be691d",
    "source_lines": "L2134-L2244",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-210"
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
