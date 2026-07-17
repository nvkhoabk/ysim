---
document_code: "UXF-04"
document_id: "UXF-04"
title: "White-label, Localization & Runtime Context Resolution"
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

# UXF-04 — White-label, Localization & Runtime Context Resolution

---

# 1. Purpose

This document defines the runtime resolution engine responsible for generating every customer experience within the YSim Platform.

Rather than rendering static websites, YSim dynamically resolves runtime contexts and composes the final commercial experience.

The Runtime Resolution Engine determines:

- Branding
- Storefront
- Theme
- Navigation
- Localization
- Catalog
- Pricing
- Payment
- Checkout
- Support
- Content
- Runtime Policies

before rendering any user interface.

---

# 2. Runtime Resolution Philosophy

The YSim Platform never renders pages directly.

Instead, every request is resolved through a sequence of independent context providers.

```
Incoming Request

↓

Context Resolution

↓

Experience Resolution

↓

Business Resolution

↓

Commercial Resolution

↓

Rendered Experience
```

Every rendered storefront is therefore generated dynamically.

---

# 3. Runtime Context Providers

The Runtime Resolution Engine collects information from multiple providers.

```
Platform Context

↓

Organization Context

↓

Storefront Context

↓

Domain Context

↓

Campaign Context

↓

Tracking Context

↓

Localization Context

↓

Identity Context

↓

Device Context

↓

Feature Flag Context

↓

User Preference Context

↓

Runtime Experience
```

Each provider contributes part of the final experience.

---

# 4. Domain Resolution

The first runtime context is Domain.

Example:

```
ysim.vn

↓

Platform Storefront
```

```
travel.partner.com

↓

Partner Storefront
```

```
agency-a.ysim.vn

↓

Agency Storefront
```

Domains determine:

- Organization
- Default Storefront
- Branding
- Default Locale
- Default Currency

---

# 5. URL Resolution

URL paths further refine the experience.

Example:

```
/japan

↓

Destination

↓

Japan Catalog
```

```
/campaign/summer

↓

Campaign Storefront
```

URL Resolution never bypasses Storefront configuration.

---

# 6. Tracking Resolution

Tracking identifiers participate in runtime resolution.

Examples:

```
tracking-id

affiliate-id

agency-id

campaign-id

qr-id
```

Tracking may influence:

- Promotion
- Hero Banner
- Featured Products
- CTA
- Commission Attribution
- Analytics
- Support Contact

Tracking must never bypass business policies.

---

# 7. Organization Resolution

Organizations define business defaults.

Examples:

- Branding
- Themes
- Navigation
- Supported Locales
- Payment Profiles
- Storefront Templates

Organizations inherit Platform defaults.

---

# 8. Storefront Resolution

Storefronts define commercial experiences.

Each storefront references:

- Experience Profile
- Theme
- Template
- Business Bindings
- Localization
- Runtime Policies

Storefronts inherit Organization configuration.

---

# 9. Localization Resolution

Localization extends beyond language translation.

Localization may resolve:

- Language
- Currency
- Date Format
- Number Format
- Timezone
- Support Information
- FAQ
- Legal Content
- Email Templates
- SMS Templates
- Payment Methods
- Promotions

Localization produces a localized commercial experience.

---

# 10. Device Resolution

Supported device categories:

- Mobile
- Tablet
- Laptop
- Desktop
- Kiosk

Device context affects:

- Layout
- Navigation
- Hero
- Grid
- CTA Position

Business behavior remains identical.

---

# 11. Identity Resolution

Identity context includes:

- Anonymous Visitor
- Customer
- Agency User
- Organization User
- Platform User

Identity affects:

- Navigation
- Available Capabilities
- Checkout
- Customer Portal
- Personalization

Identity never changes published business rules.

---

# 12. Feature Flag Resolution

Feature Flags support progressive rollout.

Flags may enable:

- Components
- Sections
- Pages
- Promotions
- Checkout Variants
- Payment Methods

Feature Flags never replace authorization.

---

# 13. User Preference Resolution

Runtime preferences may include:

- Preferred Language
- Preferred Currency
- Theme Preference
- Accessibility Settings

User Preferences override only permitted properties.

---

# 14. Runtime Resolution Order

The platform resolves contexts in the following order.

```
Platform

↓

Organization

↓

Storefront

↓

Domain

↓

Campaign

↓

Tracking

↓

Localization

↓

Identity

↓

Device

↓

Feature Flags

↓

User Preference

↓

Runtime Overrides

↓

Final Experience
```

---

# 15. Experience Inheritance

Every context supports inheritance.

```
Platform

↓

Organization

↓

Storefront

↓

Campaign

↓

Tracking

↓

Runtime
```

Only overridden properties are replaced.

---

# 16. Runtime Fallback

Missing configurations fall back automatically.

Example:

```
Tracking

↓

Campaign

↓

Storefront

↓

Organization

↓

Platform
```

Fallback applies independently to:

- Theme
- Assets
- Navigation
- Localization
- Support
- Payment
- Catalog
- Checkout

---

# 17. White-label Architecture

Every organization may own multiple storefronts.

Each storefront may configure:

- Domain
- Branding
- Theme
- Logo
- Assets
- Localization
- Navigation
- Catalog
- Payment Profile
- Checkout Flow
- Support Profile

White-label customization never requires code modification.

---

# 18. Multi-domain Support

One organization may expose multiple domains.

Example:

```
ysim.vn

travel.partner.com

agency-a.com

holiday-esim.jp
```

Each domain may resolve a different storefront.

---

# 19. Multi-storefront Support

One organization may own multiple storefronts.

Examples:

- Retail Storefront
- Agency Storefront
- Campaign Storefront
- Partner Storefront
- Embedded Commerce

Each storefront is independently configurable.

---

# 20. Runtime Policies

Policies may influence runtime rendering.

Examples:

- Guest Checkout
- Mandatory Login
- Country Restrictions
- Product Visibility
- Promotion Eligibility
- Payment Availability

Policies are evaluated before rendering.

---

# 21. Runtime Caching

Runtime Resolution may cache published snapshots.

Cache keys may include:

- Storefront
- Domain
- Locale
- Theme
- Device

Editable configurations are never cached directly.

---

# 22. Runtime Security

The Runtime Resolution Engine must:

- validate domain ownership
- validate organization ownership
- validate storefront publication status
- validate localization
- validate feature flags
- validate runtime policies

before rendering.

---

# 23. AI Implementation Guidelines

AI agents shall:

- Never hardcode domains.
- Never hardcode storefronts.
- Never hardcode localization.
- Never bypass Runtime Resolution.
- Never resolve suppliers directly.
- Always use inheritance.
- Always support fallback.
- Always resolve published configurations.
- Separate runtime resolution from rendering.

---

# 24. Architectural Principles

### UXF-401

Every request is resolved through Runtime Context Resolution.

---

### UXF-402

Domains determine storefront identity.

---

### UXF-403

Tracking participates in runtime experience generation.

---

### UXF-404

Localization defines commercial experience.

---

### UXF-405

Storefronts inherit Organization configuration.

---

### UXF-406

Organizations inherit Platform configuration.

---

### UXF-407

Every configuration supports fallback.

---

### UXF-408

White-label customization requires no source code changes.

---

### UXF-409

Only published configurations participate in runtime rendering.

---

### UXF-410

Supplier systems never participate in Experience Resolution.

---

# 25. References

This document should be read together with:

- UXF-00 — User Experience Foundation Overview
- UXF-01 — Experience Channels, Personas & Navigation
- UXF-02 — Design System, Theme & Experience Inheritance
- UXF-03 — Storefront Template & Page Composition
- UXF-05 — Storefront Runtime Architecture & Business Binding

- BRD
- ABP
- AFM
- YADF
- DIP

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## v2.3 normative requirement appendix — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R001 — The YSim Platform never renders pages directly

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
      "requirement_id": "UXF-04-R001",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "94bfb26a2c34981496c848654c140d3a28d4c8faee2d65c9c34fe64bfef632f4"
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
        "UXF-04-R001-AC001",
        "UXF-04-R001-AC002",
        "UXF-04-R001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R001-O001",
      "obligation_text": "The YSim Platform never renders pages directly"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The YSim Platform never renders pages directly.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-001",
    "previous_temporary_key": "TMP-UXF-04-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "2. Runtime Resolution Philosophy",
    "source_context_sha256": "a9fa0e29cfae8fd0e54fde1313145b78b5fd7ba4e3a0679e26d6724aba0030a7",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "94bfb26a2c34981496c848654c140d3a28d4c8faee2d65c9c34fe64bfef632f4",
    "source_lines": "L710-L785",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R001"
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
  "stable_id": "UXF-04-R001",
  "title": "The YSim Platform never renders pages directly",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R002 — URL Resolution never bypasses Storefront configuration

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
      "requirement_id": "UXF-04-R002",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "8e92f6de3dbb6c2309eb6c9bdd7af1622202b77a1e932a2f2a02f6809d3ff7bf"
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
        "UXF-04-R002-AC001",
        "UXF-04-R002-AC002",
        "UXF-04-R002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R002-O001",
      "obligation_text": "URL Resolution never bypasses Storefront configuration"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "URL Resolution never bypasses Storefront configuration.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-002",
    "previous_temporary_key": "TMP-UXF-04-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. URL Resolution",
    "source_context_sha256": "39c39a4a23aad839fdfac11a2051a0c5b308ce761f508de6595386adc519c51d",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "8e92f6de3dbb6c2309eb6c9bdd7af1622202b77a1e932a2f2a02f6809d3ff7bf",
    "source_lines": "L787-L862",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R002"
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
  "stable_id": "UXF-04-R002",
  "title": "URL Resolution never bypasses Storefront configuration",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R003 — Tracking must never bypass business policies

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
      "requirement_id": "UXF-04-R003",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "0447b6d43c490841f73daab152721ce6d9330862c3907b101bce2195673e3bda"
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
        "UXF-04-R003-AC001",
        "UXF-04-R003-AC002",
        "UXF-04-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R003-O001",
      "obligation_text": "Tracking must never bypass business policies"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Tracking must never bypass business policies.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-003",
    "previous_temporary_key": "TMP-UXF-04-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Tracking Resolution",
    "source_context_sha256": "b80056705a6b803c3799b33afb736309daefdd125de1900660f1204177055081",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "0447b6d43c490841f73daab152721ce6d9330862c3907b101bce2195673e3bda",
    "source_lines": "L864-L939",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R003"
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
  "stable_id": "UXF-04-R003",
  "title": "Tracking must never bypass business policies",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R004 — Identity never changes published business rules

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-04-R004",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "ec5c3ed1bc7bd66ca0588ac249fae3779e998dfc895177408e10a19cc58ee767"
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
        "UXF-04-R004-AC001",
        "UXF-04-R004-AC002",
        "UXF-04-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R004-O001",
      "obligation_text": "Identity never changes published business rules"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-04-R004 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-04-R004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-04-R004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-04-R004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-04-R004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-04-R004 does not define a recovery obligation."
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-032",
      "selected_disposition": "CONFIRM_CRITICAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Identity never changes published business rules.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-004",
    "previous_temporary_key": "TMP-UXF-04-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Identity Resolution",
    "source_context_sha256": "5257bf47fa1f0786df2f1633691f098007aa7eaa51140f46a77c0e92dfab5e07",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "ec5c3ed1bc7bd66ca0588ac249fae3779e998dfc895177408e10a19cc58ee767",
    "source_lines": "L941-L1062",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R004"
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
  "stable_id": "UXF-04-R004",
  "title": "Identity never changes published business rules",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R005 — Feature Flags never replace authorization

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
      "requirement_id": "UXF-04-R005",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "2959a4ad7a97abd5ddac955d67f46c232135d7e11d9bc3c4d12db7bb59817b68"
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
        "UXF-04-R005-AC001",
        "UXF-04-R005-AC002",
        "UXF-04-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R005-O001",
      "obligation_text": "Feature Flags never replace authorization"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-04-R005-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-04-R005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-04-R005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-04-R005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "UXF-04-R005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "UXF-04-R005 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Feature Flags never replace authorization.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-005",
    "previous_temporary_key": "TMP-UXF-04-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Feature Flag Resolution",
    "source_context_sha256": "2f4ab5238d04666fcdbcef46d77c790804657b97f4b9d2bd6d94e12d6d5088af",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "2959a4ad7a97abd5ddac955d67f46c232135d7e11d9bc3c4d12db7bb59817b68",
    "source_lines": "L1064-L1174",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R005"
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
  "stable_id": "UXF-04-R005",
  "title": "Feature Flags never replace authorization",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R006 — White-label configuration must not require source-code modification

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
      "requirement_id": "UXF-04-R006",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "c1d29364303d17973a158aaaf1005c8a91f12502f035c1ac39088c8b3c84770f"
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
        "UXF-04-R006-AC001",
        "UXF-04-R006-AC002",
        "UXF-04-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R006-O001",
      "obligation_text": "White-label configuration must not require source-code modification"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-033",
      "selected_disposition": "ROUTE_TO_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "White-label configuration must not require source-code modification.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-006",
    "previous_temporary_key": "TMP-UXF-04-006",
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. White-label Architecture",
    "source_context_sha256": "430166e9aaeec91c826891a31703942cf157862d7f1a2b251983308a7ea5828c",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "c1d29364303d17973a158aaaf1005c8a91f12502f035c1ac39088c8b3c84770f",
    "source_lines": "L1176-L1263",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R006"
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
  "stable_id": "UXF-04-R006",
  "title": "White-label configuration must not require source-code modification",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R007 — Guest Checkout, Mandatory Login, Country Restrictions, Product Visibility, Promotion Eligibility…

```json
{
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "The extracted text is an example or explanatory statement, not a standalone requirement.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Guest Checkout, Mandatory Login, Country Restrictions, Product Visibility, Promotion Eligibility, and Payment Availability are examples of runtime policies, not a standalone requirement set.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008",
      "P2-DEC-010",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/UXF/UXF-04.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "20. Runtime Policies"
    },
    "deterministic_transformation": "EXPAND_RANGE_AND_RETIRE_EXAMPLE_EXTRACTION",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-007",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-UXF-04-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Tracking Resolution",
    "source_context_sha256": "b80056705a6b803c3799b33afb736309daefdd125de1900660f1204177055081",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "8dd8232d2ca7eba64899bda40a082ed4028c2a89d46a5b862de58106c8da687a",
    "source_fingerprint_before_c3": "f2434bed7593bc69704e57de02a50d64198295f49e3e15040c837f20c3f6f95f",
    "source_lines": "L1265-L1335",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/UXF/UXF-04.md",
      "lines": "L556-L563",
      "section": "20. Runtime Policies"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R007"
  },
  "record_kind": "RETIRED_RECORD",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "retirement_reason": "EXPAND_RANGE_AND_RETIRE_EXAMPLE_EXTRACTION",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-04-R007",
  "title": "Guest Checkout, Mandatory Login, Country Restrictions, Product Visibility, Promotion Eligibility…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R008 — Editable configurations are never cached directly

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
      "requirement_id": "UXF-04-R008",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "83b6a751505535b9a7d643fae1cb3751cae53219f301d47d29e6c14ac3505498"
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
        "UXF-04-R008-AC001",
        "UXF-04-R008-AC002",
        "UXF-04-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R008-O001",
      "obligation_text": "Editable configurations are never cached directly"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Editable configurations are never cached directly.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-008",
    "previous_temporary_key": "TMP-UXF-04-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "21. Runtime Caching",
    "source_context_sha256": "eb022b48e145254f722d446a178ba552aea016e74318efc4724866325169980b",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "83b6a751505535b9a7d643fae1cb3751cae53219f301d47d29e6c14ac3505498",
    "source_lines": "L1337-L1412",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R008"
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
  "stable_id": "UXF-04-R008",
  "title": "Editable configurations are never cached directly",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R009 — The Runtime Resolution Engine must: - validate domain ownership

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
      "requirement_id": "UXF-04-R009",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "eb6031104bd2ccfc70094f063a17492d42cce8441769ad38385b7a3b13646691"
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
        "UXF-04-R009-AC001",
        "UXF-04-R009-AC002",
        "UXF-04-R009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R009-O001",
      "obligation_text": "The Runtime Resolution Engine must: - validate domain ownership"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Runtime Resolution Engine must: - validate domain ownership",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-009",
    "previous_temporary_key": "TMP-UXF-04-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Runtime Security",
    "source_context_sha256": "7d47aad18619caa194cbed84a0bab8a507c37cbeeccb9582a8366b26ca2d242f",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "eb6031104bd2ccfc70094f063a17492d42cce8441769ad38385b7a3b13646691",
    "source_lines": "L1414-L1489",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R009"
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
  "stable_id": "UXF-04-R009",
  "title": "The Runtime Resolution Engine must: - validate domain ownership",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R010 — The Runtime Resolution Engine must: - validate organization ownership

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
      "requirement_id": "UXF-04-R010",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "4a5a7d605ce16e8b58d0f69f08059d543a62317767023c5c7fa5295c5bce7c72"
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
        "UXF-04-R010-AC001",
        "UXF-04-R010-AC002",
        "UXF-04-R010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R010-O001",
      "obligation_text": "The Runtime Resolution Engine must: - validate organization ownership"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Runtime Resolution Engine must: - validate organization ownership",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-010",
    "previous_temporary_key": "TMP-UXF-04-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Runtime Security",
    "source_context_sha256": "7d47aad18619caa194cbed84a0bab8a507c37cbeeccb9582a8366b26ca2d242f",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "4a5a7d605ce16e8b58d0f69f08059d543a62317767023c5c7fa5295c5bce7c72",
    "source_lines": "L1491-L1566",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R010"
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
  "stable_id": "UXF-04-R010",
  "title": "The Runtime Resolution Engine must: - validate organization ownership",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R011 — The Runtime Resolution Engine must: - validate storefront publication status

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
      "requirement_id": "UXF-04-R011",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "4fbb863392f0af1835c30fcf5aa2baf2887c25a2b4762b934f39edbf692b3263"
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
        "UXF-04-R011-AC001",
        "UXF-04-R011-AC002",
        "UXF-04-R011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R011-O001",
      "obligation_text": "The Runtime Resolution Engine must: - validate storefront publication status"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Runtime Resolution Engine must: - validate storefront publication status",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-011",
    "previous_temporary_key": "TMP-UXF-04-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Runtime Security",
    "source_context_sha256": "7d47aad18619caa194cbed84a0bab8a507c37cbeeccb9582a8366b26ca2d242f",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "4fbb863392f0af1835c30fcf5aa2baf2887c25a2b4762b934f39edbf692b3263",
    "source_lines": "L1568-L1643",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R011"
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
  "stable_id": "UXF-04-R011",
  "title": "The Runtime Resolution Engine must: - validate storefront publication status",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R012 — The Runtime Resolution Engine must: - validate localization

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
      "requirement_id": "UXF-04-R012",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "370edde21e9ebb090797cc26c0889f0f95964c3744c2f266227e494cb6e7e5e5"
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
        "UXF-04-R012-AC001",
        "UXF-04-R012-AC002",
        "UXF-04-R012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R012-O001",
      "obligation_text": "The Runtime Resolution Engine must: - validate localization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Runtime Resolution Engine must: - validate localization",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-012",
    "previous_temporary_key": "TMP-UXF-04-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Runtime Security",
    "source_context_sha256": "7d47aad18619caa194cbed84a0bab8a507c37cbeeccb9582a8366b26ca2d242f",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "370edde21e9ebb090797cc26c0889f0f95964c3744c2f266227e494cb6e7e5e5",
    "source_lines": "L1645-L1720",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R012"
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
  "stable_id": "UXF-04-R012",
  "title": "The Runtime Resolution Engine must: - validate localization",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R013 — The Runtime Resolution Engine must: - validate feature flags

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
      "requirement_id": "UXF-04-R013",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "d9a99e201b37c4794c8e46c9a09fa1cb098e367f91c6e1274efdc1d672c53b80"
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
        "UXF-04-R013-AC001",
        "UXF-04-R013-AC002",
        "UXF-04-R013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R013-O001",
      "obligation_text": "The Runtime Resolution Engine must: - validate feature flags"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Runtime Resolution Engine must: - validate feature flags",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-013",
    "previous_temporary_key": "TMP-UXF-04-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Runtime Security",
    "source_context_sha256": "7d47aad18619caa194cbed84a0bab8a507c37cbeeccb9582a8366b26ca2d242f",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "d9a99e201b37c4794c8e46c9a09fa1cb098e367f91c6e1274efdc1d672c53b80",
    "source_lines": "L1722-L1797",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R013"
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
  "stable_id": "UXF-04-R013",
  "title": "The Runtime Resolution Engine must: - validate feature flags",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R014 — The Runtime Resolution Engine must: - validate runtime policies

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
      "requirement_id": "UXF-04-R014",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "7e05b8853490711eeb6d9a88879c728e05dfe4b7715a5736ed1498277bad990d"
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
        "UXF-04-R014-AC001",
        "UXF-04-R014-AC002",
        "UXF-04-R014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R014-O001",
      "obligation_text": "The Runtime Resolution Engine must: - validate runtime policies"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "The Runtime Resolution Engine must: - validate runtime policies",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-014",
    "previous_temporary_key": "TMP-UXF-04-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Runtime Security",
    "source_context_sha256": "7d47aad18619caa194cbed84a0bab8a507c37cbeeccb9582a8366b26ca2d242f",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "7e05b8853490711eeb6d9a88879c728e05dfe4b7715a5736ed1498277bad990d",
    "source_lines": "L1799-L1874",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-04-R014"
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
  "stable_id": "UXF-04-R014",
  "title": "The Runtime Resolution Engine must: - validate runtime policies",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-401 — Every request is resolved through Runtime Context Resolution

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
      "requirement_id": "UXF-401",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "39b343c9f45218f79e809dac11bc7298937b3d0aa9472df1ef1593f257fb2836"
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
        "UXF-401-AC001",
        "UXF-401-AC002",
        "UXF-401-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-401-O001",
      "obligation_text": "Every request is resolved through Runtime Context Resolution"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every request is resolved through Runtime Context Resolution.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-401",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-401",
    "source_context_sha256": "dff3523e962ad8de27a3b1af88c6d3b0e4833dfdeef6fc7991aedf9916d3df7f",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "39b343c9f45218f79e809dac11bc7298937b3d0aa9472df1ef1593f257fb2836",
    "source_lines": "L1876-L1951",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-401"
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
  "stable_id": "UXF-401",
  "title": "Every request is resolved through Runtime Context Resolution",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-402 — Domains determine storefront identity

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "A domain without configuration follows the governed not-found boundary and does not infer a Storefront"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "UXF-402.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                "source_type": "SOURCE_LITERAL",
                "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
              },
              "identifier": "UXF-402.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                "source_lines": "L624-L627",
                "source_section": "24. Architectural Principles > UXF-402"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.UXF-402.UXF-402.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
            "source_lines": "L624-L627",
            "source_section": "24. Architectural Principles > UXF-402"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "UXF-402.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                "source_type": "SOURCE_LITERAL",
                "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
              },
              "identifier": "UXF-402.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                "source_lines": "L624-L627",
                "source_section": "24. Architectural Principles > UXF-402"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.UXF-402.UXF-402.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
            "source_lines": "L624-L627",
            "source_section": "24. Architectural Principles > UXF-402"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
            "source_type": "SOURCE_LITERAL",
            "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
          },
          "identifier": "UXF-402.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
            "source_lines": "L624-L627",
            "source_section": "24. Architectural Principles > UXF-402"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.UXF-402.UXF-402.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
            "source_type": "SOURCE_LITERAL",
            "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
          },
          "identifier": "UXF-402.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
            "source_lines": "L624-L627",
            "source_section": "24. Architectural Principles > UXF-402"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.UXF-402.UXF-402.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
            "source_type": "SOURCE_LITERAL",
            "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
          },
          "identifier": "UXF-402.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
            "source_lines": "L624-L627",
            "source_section": "24. Architectural Principles > UXF-402"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.UXF-402.UXF-402.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
            "source_type": "SOURCE_LITERAL",
            "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
          },
          "identifier": "UXF-402.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
            "source_lines": "L624-L627",
            "source_section": "24. Architectural Principles > UXF-402"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.UXF-402.UXF-402.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
            "source_type": "SOURCE_LITERAL",
            "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
          },
          "identifier": "UXF-402.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
            "source_lines": "L624-L627",
            "source_section": "24. Architectural Principles > UXF-402"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.UXF-402.UXF-402.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.UXF-402",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "The domain resolves to another Storefront or dangling identity"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID"
    ],
    "positive_oracle": [
      "The domain resolves to its configured Storefront identity"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-008"
      ],
      "inference": false,
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
      "source_lines": "L624-L627",
      "source_section": "24. Architectural Principles > UXF-402"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
          "source_type": "SOURCE_LITERAL",
          "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
        },
        "identifier": "UXF-402.UXF-402.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "UXF-402.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-008"
          ],
          "inference": false,
          "source_document": "docs/UXF/UXF-04.md",
          "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
          "source_lines": "L624-L627",
          "source_section": "24. Architectural Principles > UXF-402"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.UXF-402.UXF-402.UXF-402.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "UXF-402.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.DOMAIN",
        "FIELD.CONFIGURED_STOREFRONT_ID",
        "FIELD.RESOLVED_STOREFRONT_ID",
        "FIELD.MAPPING_VERSION",
        "FIELD.RESOLUTION_RESULT"
      ],
      "producer": "UXF-402.EVIDENCE.PRODUCER",
      "required_collection_origin": "UXF-402.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.DOMAIN",
        "FIELD.CONFIGURED_STOREFRONT_ID",
        "FIELD.RESOLVED_STOREFRONT_ID",
        "FIELD.MAPPING_VERSION",
        "FIELD.RESOLUTION_RESULT"
      ],
      "required_values_or_hashes": [
        "UXF-402.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "UXF-402.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "UXF-402.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "UXF-402-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID",
          "evaluator_consumed_bindings": [
            "allowed_lifecycle_states",
            "allowed_states",
            "reference",
            "registry",
            "registry_source",
            "target_id",
            "target_type"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
              "source_type": "SOURCE_LITERAL",
              "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
            },
            "identifier": "UXF-402.UXF-402.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/UXF/UXF-04.md",
              "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
              "source_lines": "L624-L627",
              "source_section": "24. Architectural Principles > UXF-402"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.UXF-402.UXF-402.UXF-402.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
              "source_type": "SOURCE_LITERAL",
              "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
            },
            "identifier": "UXF-402.UXF-402.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/UXF/UXF-04.md",
              "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
              "source_lines": "L624-L627",
              "source_section": "24. Architectural Principles > UXF-402"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.UXF-402.UXF-402.UXF-402.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "allowed_lifecycle_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "UXF-402.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                      "source_type": "SOURCE_LITERAL",
                      "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
                    },
                    "identifier": "UXF-402.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/UXF/UXF-04.md",
                      "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                      "source_lines": "L624-L627",
                      "source_section": "24. Architectural Principles > UXF-402"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.UXF-402.UXF-402.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                  "source_lines": "L624-L627",
                  "source_section": "24. Architectural Principles > UXF-402"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "UXF-402.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                      "source_type": "SOURCE_LITERAL",
                      "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
                    },
                    "identifier": "UXF-402.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/UXF/UXF-04.md",
                      "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                      "source_lines": "L624-L627",
                      "source_section": "24. Architectural Principles > UXF-402"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.UXF-402.UXF-402.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                  "source_lines": "L624-L627",
                  "source_section": "24. Architectural Principles > UXF-402"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                  "source_type": "SOURCE_LITERAL",
                  "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
                },
                "identifier": "UXF-402.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                  "source_lines": "L624-L627",
                  "source_section": "24. Architectural Principles > UXF-402"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.UXF-402.UXF-402.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                  "source_type": "SOURCE_LITERAL",
                  "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
                },
                "identifier": "UXF-402.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                  "source_lines": "L624-L627",
                  "source_section": "24. Architectural Principles > UXF-402"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.UXF-402.UXF-402.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                  "source_type": "SOURCE_LITERAL",
                  "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
                },
                "identifier": "UXF-402.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                  "source_lines": "L624-L627",
                  "source_section": "24. Architectural Principles > UXF-402"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.UXF-402.UXF-402.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                  "source_type": "SOURCE_LITERAL",
                  "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
                },
                "identifier": "UXF-402.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                  "source_lines": "L624-L627",
                  "source_section": "24. Architectural Principles > UXF-402"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.UXF-402.UXF-402.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                  "source_type": "SOURCE_LITERAL",
                  "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
                },
                "identifier": "UXF-402.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                  "source_lines": "L624-L627",
                  "source_section": "24. Architectural Principles > UXF-402"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.UXF-402.UXF-402.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                  "source_type": "SOURCE_LITERAL",
                  "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
                },
                "identifier": "UXF-402.UXF-402.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                  "source_lines": "L624-L627",
                  "source_section": "24. Architectural Principles > UXF-402"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.UXF-402.UXF-402.UXF-402.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                  "source_type": "SOURCE_LITERAL",
                  "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
                },
                "identifier": "UXF-402.UXF-402.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                  "source_lines": "L624-L627",
                  "source_section": "24. Architectural Principles > UXF-402"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.UXF-402.UXF-402.UXF-402.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                "source_type": "SOURCE_LITERAL",
                "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
              },
              "identifier": "UXF-402.UXF-402.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                "source_lines": "L624-L627",
                "source_section": "24. Architectural Principles > UXF-402"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.UXF-402.UXF-402.UXF-402.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "UXF-402-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
              "source_type": "SOURCE_LITERAL",
              "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
            },
            "identifier": "UXF-402.UXF-402.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/UXF/UXF-04.md",
              "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
              "source_lines": "L624-L627",
              "source_section": "24. Architectural Principles > UXF-402"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.UXF-402.UXF-402.UXF-402.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "operator_id": "REFERENCE_TARGET_VALID",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "allowed_lifecycle_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "UXF-402.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                    "source_type": "SOURCE_LITERAL",
                    "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
                  },
                  "identifier": "UXF-402.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/UXF/UXF-04.md",
                    "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                    "source_lines": "L624-L627",
                    "source_section": "24. Architectural Principles > UXF-402"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.UXF-402.UXF-402.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                "source_lines": "L624-L627",
                "source_section": "24. Architectural Principles > UXF-402"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "UXF-402.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                    "source_type": "SOURCE_LITERAL",
                    "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
                  },
                  "identifier": "UXF-402.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/UXF/UXF-04.md",
                    "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                    "source_lines": "L624-L627",
                    "source_section": "24. Architectural Principles > UXF-402"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.UXF-402.UXF-402.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                "source_lines": "L624-L627",
                "source_section": "24. Architectural Principles > UXF-402"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                "source_type": "SOURCE_LITERAL",
                "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
              },
              "identifier": "UXF-402.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                "source_lines": "L624-L627",
                "source_section": "24. Architectural Principles > UXF-402"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.UXF-402.UXF-402.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                "source_type": "SOURCE_LITERAL",
                "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
              },
              "identifier": "UXF-402.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                "source_lines": "L624-L627",
                "source_section": "24. Architectural Principles > UXF-402"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.UXF-402.UXF-402.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                "source_type": "SOURCE_LITERAL",
                "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
              },
              "identifier": "UXF-402.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                "source_lines": "L624-L627",
                "source_section": "24. Architectural Principles > UXF-402"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.UXF-402.UXF-402.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                "source_type": "SOURCE_LITERAL",
                "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
              },
              "identifier": "UXF-402.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                "source_lines": "L624-L627",
                "source_section": "24. Architectural Principles > UXF-402"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.UXF-402.UXF-402.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
                "source_type": "SOURCE_LITERAL",
                "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
              },
              "identifier": "UXF-402.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-402.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
                "source_lines": "L624-L627",
                "source_section": "24. Architectural Principles > UXF-402"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.UXF-402.UXF-402.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        }
      ],
      "boundary_cases": [
        "A domain without configuration follows the governed not-found boundary and does not infer a Storefront"
      ],
      "contract_ast_sha256": "783a1075248527bc3f646f9d83636e5f773061a8dd64d05c8342406cce2e0c75",
      "contract_id": "P2C.C4.CONTRACT.UXF-402",
      "criticality": "HIGH",
      "disposition": "OPERATOR_REMAP_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/UXF/UXF-04.md#24. Architectural Principles > UXF-402",
            "source_type": "SOURCE_LITERAL",
            "version": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7"
          },
          "identifier": "UXF-402.UXF-402.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-402.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
            "source_lines": "L624-L627",
            "source_section": "24. Architectural Principles > UXF-402"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.UXF-402.UXF-402.UXF-402.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "UXF-402.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.DOMAIN",
          "FIELD.CONFIGURED_STOREFRONT_ID",
          "FIELD.RESOLVED_STOREFRONT_ID",
          "FIELD.MAPPING_VERSION",
          "FIELD.RESOLUTION_RESULT"
        ],
        "producer": "UXF-402.EVIDENCE.PRODUCER",
        "required_collection_origin": "UXF-402.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.DOMAIN",
          "FIELD.CONFIGURED_STOREFRONT_ID",
          "FIELD.RESOLVED_STOREFRONT_ID",
          "FIELD.MAPPING_VERSION",
          "FIELD.RESOLUTION_RESULT"
        ],
        "required_values_or_hashes": [
          "UXF-402.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "UXF-402.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "UXF-402.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-616B42B810B22D6B2010",
        "P2C-C4-FX-0AFA5FD7D757533DFA12",
        "P2C-C4-FX-5DD8407D4888FF13F881"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "The domain resolves to another Storefront or dangling identity"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "UXF-402-O001",
          "obligation_text": "Domains determine storefront identity"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "UXF-402.O1.1.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "UXF-402-O001"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID"
      ],
      "positive_oracles": [
        "The domain resolves to its configured Storefront identity"
      ],
      "preconditions": [
        "The domain mapping is active and canonical Storefront exists"
      ],
      "prohibitions": [
        "The domain resolves to another Storefront or dangling identity"
      ],
      "requirement_id": "UXF-402",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-008"
        ],
        "inference": false,
        "source_document": "docs/UXF/UXF-04.md",
        "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
        "source_lines": "L624-L627",
        "source_section": "24. Architectural Principles > UXF-402"
      },
      "source_statement": "Domains determine storefront identity.",
      "surrounding_source_context": "### UXF-402\n\nDomains determine storefront identity.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.UXF-402",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "SEMANTIC_ACCEPTANCE_RENDERER_C2",
    "runtime_status": "RUNTIME_ADAPTER_PENDING"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "ACCEPTANCE_READY",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-402-AC001",
        "UXF-402-AC002",
        "UXF-402-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-402-O001",
      "obligation_text": "Domains determine storefront identity"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CONTROLLED_FAST_TRACK_BULK_HUMAN_AUTHORIZATION",
      "exception_id": "P2-CRIT-EXC-043",
      "selected_disposition": "CONFIRM_HIGH"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Domains determine storefront identity.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-402",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-402",
    "source_context_sha256": "48ff2e31ff392d36d51e96ef8e2c18098301c416b881fb5192aa20dfb50a0b44",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "bb9b9ac2a6978597d8ebcb6397f061a792ffde75d8dda1a9c77af06e89f7128d",
    "source_lines": "L1953-L3387",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-402"
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
  "stable_id": "UXF-402",
  "title": "Domains determine storefront identity",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-403 — Tracking participates in runtime experience generation

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
      "requirement_id": "UXF-403",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "cae177e4e6b99caab62a512dee27ab30c30c29ac1e6bd8d764bd8487ee8b313a"
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
        "UXF-403-AC001",
        "UXF-403-AC002",
        "UXF-403-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-403-O001",
      "obligation_text": "Tracking participates in runtime experience generation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Tracking participates in runtime experience generation.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-403",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-403",
    "source_context_sha256": "d50fccfba4f952728a401e1bb9bc3ab2c594d3b1d312f415674b9486b29441a1",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "cae177e4e6b99caab62a512dee27ab30c30c29ac1e6bd8d764bd8487ee8b313a",
    "source_lines": "L3389-L3464",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-403"
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
  "stable_id": "UXF-403",
  "title": "Tracking participates in runtime experience generation",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-404 — Localization defines commercial experience

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
      "requirement_id": "UXF-404",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "dd4a5e941ddc150cbe7dade1286d8960bb1040854f9b38fdc122bff485060a12"
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
        "UXF-404-AC001",
        "UXF-404-AC002",
        "UXF-404-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-404-O001",
      "obligation_text": "Localization defines commercial experience"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Localization defines commercial experience.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-404",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-404",
    "source_context_sha256": "84be5cf9ca995d6ea9ee516890aaa346f03f13c337a0efba6fdc6f8b6b9552dc",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "dd4a5e941ddc150cbe7dade1286d8960bb1040854f9b38fdc122bff485060a12",
    "source_lines": "L3466-L3541",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-404"
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
  "stable_id": "UXF-404",
  "title": "Localization defines commercial experience",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-405 — Storefronts inherit Organization configuration

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Explicit allowed Storefront override wins only at its declared precedence"
    ],
    "concrete_bindings": [
      {
        "configuration_key": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "UXF-405.CONFIGURATION_KEY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.CONFIGURATION_KEY.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-UXF-405-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
            "source_lines": "L642-L645",
            "source_section": "24. Architectural Principles > UXF-405"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CONFIGURATION_KEY",
            "resolver_id": "RESOLVE.UXF-405.UXF-405.CONFIGURATION_KEY",
            "version": "1.0.0"
          },
          "semantic_type": "CONFIGURATION_KEY"
        },
        "precedence_order": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "CONFIGURATION.PRECEDENCE.PLATFORM.SECURITY.JURISDICTION.MARKET.ORGANIZATION.STOREFRONT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.PRECEDENCE_ORDER.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-UXF-405-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
            "source_lines": "L642-L645",
            "source_section": "24. Architectural Principles > UXF-405"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
            "resolver_id": "RESOLVE.UXF-405.CONFIGURATION.PRECEDENCE.PLATFORM.SECURITY.JURISDICTION.MARKET.ORGANIZATION.STOREFRONT",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
        },
        "resolved_source": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "UXF-405.RESOLVED_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.RESOLVED_SOURCE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-UXF-405-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
            "source_lines": "L642-L645",
            "source_section": "24. Architectural Principles > UXF-405"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CONFIGURATION_SOURCE_ID",
            "resolver_id": "RESOLVE.UXF-405.UXF-405.RESOLVED_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "CONFIGURATION_SOURCE_ID"
        },
        "resolved_value": {
          "authoritative_source": {
            "allowed_identifiers": [
              "UXF-405.RESOLVED_VALUE"
            ],
            "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "UXF-405.RESOLVED_VALUE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.RESOLVED_VALUE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-UXF-405-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
            "source_lines": "L642-L645",
            "source_section": "24. Architectural Principles > UXF-405"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "RESOLVE.UXF-405.UXF-405.RESOLVED_VALUE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "source_values": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "PLATFORM.SECURITY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN.MEMBER.1",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_SOURCE_ID",
                "resolver_id": "RESOLVE.UXF-405.PLATFORM.SECURITY",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_SOURCE_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "JURISDICTION.MARKET",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN.MEMBER.2",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_SOURCE_ID",
                "resolver_id": "RESOLVE.UXF-405.JURISDICTION.MARKET",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_SOURCE_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "ORGANIZATION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN.MEMBER.3",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_SOURCE_ID",
                "resolver_id": "RESOLVE.UXF-405.ORGANIZATION",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_SOURCE_ID"
            },
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "STOREFRONT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN.MEMBER.4",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_SOURCE_ID",
                "resolver_id": "RESOLVE.UXF-405.STOREFRONT",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_SOURCE_ID"
            }
          ],
          "origin": {
            "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-UXF-405-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
            "source_lines": "L642-L645",
            "source_section": "24. Architectural Principles > UXF-405"
          },
          "semantic_type": "SET_OF<CONFIGURATION_SOURCE_ID>"
        },
        "source_versions": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "UXF-405.SOURCE_VERSIONS.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.UXF-405.UXF-405.SOURCE_VERSIONS.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          ],
          "origin": {
            "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VERSIONS.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-UXF-405-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
            "source_lines": "L642-L645",
            "source_section": "24. Architectural Principles > UXF-405"
          },
          "semantic_type": "SET_OF<POLICY_VERSION>"
        }
      },
      {
        "configuration_key": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "UXF-405.CONFIGURATION_KEY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.CONFIGURATION_KEY.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-UXF-405-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
            "source_lines": "L642-L645",
            "source_section": "24. Architectural Principles > UXF-405"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CONFIGURATION_KEY",
            "resolver_id": "RESOLVE.UXF-405.UXF-405.CONFIGURATION_KEY",
            "version": "1.0.0"
          },
          "semantic_type": "CONFIGURATION_KEY"
        },
        "configuration_sources": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "UXF-405.CONFIGURATION_SOURCES",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.CONFIGURATION_SOURCES.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-UXF-405-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
            "source_lines": "L642-L645",
            "source_section": "24. Architectural Principles > UXF-405"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
            "resolver_id": "RESOLVE.UXF-405.UXF-405.CONFIGURATION_SOURCES",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
        },
        "expected_value": {
          "authoritative_source": {
            "allowed_identifiers": [
              "UXF-405.CANONICAL.CONFIGURATION.VALUE"
            ],
            "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "UXF-405.CANONICAL.CONFIGURATION.VALUE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.EXPECTED_VALUE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-UXF-405-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
            "source_lines": "L642-L645",
            "source_section": "24. Architectural Principles > UXF-405"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "RESOLVE.UXF-405.UXF-405.CANONICAL.CONFIGURATION.VALUE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "resolved_source": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "UXF-405.RESOLVED_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.RESOLVED_SOURCE.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-UXF-405-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
            "source_lines": "L642-L645",
            "source_section": "24. Architectural Principles > UXF-405"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CONFIGURATION_SOURCE_ID",
            "resolver_id": "RESOLVE.UXF-405.UXF-405.RESOLVED_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "CONFIGURATION_SOURCE_ID"
        },
        "source_versions": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "UXF-405.SOURCE_VERSIONS.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.UXF-405.UXF-405.SOURCE_VERSIONS.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          ],
          "origin": {
            "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN",
            "origin_type": "APPROVED_DECISION"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-UXF-405-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
            "source_lines": "L642-L645",
            "source_section": "24. Architectural Principles > UXF-405"
          },
          "semantic_type": "SET_OF<POLICY_VERSION>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.UXF-405",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Applicable Organization value is ignored without an allowed override"
    ],
    "operator_composition": [
      "CONFIGURATION_PRECEDENCE",
      "CONFIGURATION_RESOLVES"
    ],
    "positive_oracle": [
      "Storefront inherits applicable Organization configuration subject to governed override precedence"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2C-OBT-C1-UXF-405-OPT-1"
      ],
      "inference": false,
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
      "source_lines": "L642-L645",
      "source_section": "24. Architectural Principles > UXF-405"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
          "source_type": "APPROVED_DECISION",
          "version": "2026-07-16"
        },
        "identifier": "UXF-405.UXF-405.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "UXF-405.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2C-OBT-C1-UXF-405-OPT-1"
          ],
          "inference": false,
          "source_document": "docs/UXF/UXF-04.md",
          "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
          "source_lines": "L642-L645",
          "source_section": "24. Architectural Principles > UXF-405"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.UXF-405.UXF-405.UXF-405.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "UXF-405.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.STOREFRONT_ID",
        "FIELD.ORGANIZATION_ID",
        "FIELD.ORGANIZATION_CONFIGURATION",
        "FIELD.STOREFRONT_OVERRIDE",
        "FIELD.PRECEDENCE",
        "FIELD.EFFECTIVE_CONFIGURATION"
      ],
      "producer": "UXF-405.EVIDENCE.PRODUCER",
      "required_collection_origin": "UXF-405.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.STOREFRONT_ID",
        "FIELD.ORGANIZATION_ID",
        "FIELD.ORGANIZATION_CONFIGURATION",
        "FIELD.STOREFRONT_OVERRIDE",
        "FIELD.PRECEDENCE",
        "FIELD.EFFECTIVE_CONFIGURATION"
      ],
      "required_values_or_hashes": [
        "UXF-405.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "UXF-405.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "UXF-405.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "UXF-405-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": {
        "meaning": "Configuration precedence is Platform/Security, Jurisdiction/Market, Organization, then Storefront within governed override boundaries.",
        "non_inferences": [
          "No configuration key is invented.",
          "Lower scopes cannot override business, security or regulatory invariants."
        ],
        "option_id": "P2C-OBT-C1-UXF-405-OPT-1"
      },
      "assertions": [
        {
          "assertion_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE",
          "evaluator_consumed_bindings": [
            "configuration_key",
            "precedence_order",
            "resolved_source",
            "resolved_value",
            "source_values",
            "source_versions"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "UXF-405.UXF-405.O1.1.CONFIGURATION_PRECEDENCE.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-UXF-405-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/UXF/UXF-04.md",
              "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
              "source_lines": "L642-L645",
              "source_section": "24. Architectural Principles > UXF-405"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.UXF-405.UXF-405.UXF-405.O1.1.CONFIGURATION_PRECEDENCE.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "UXF-405.UXF-405.O1.1.CONFIGURATION_PRECEDENCE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-UXF-405-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/UXF/UXF-04.md",
              "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
              "source_lines": "L642-L645",
              "source_section": "24. Architectural Principles > UXF-405"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CONFIGURATION_SOURCE_ID",
              "resolver_id": "RESOLVE.UXF-405.UXF-405.UXF-405.O1.1.CONFIGURATION_PRECEDENCE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CONFIGURATION_SOURCE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "configuration_key": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "UXF-405.CONFIGURATION_KEY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.CONFIGURATION_KEY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CONFIGURATION_KEY",
                  "resolver_id": "RESOLVE.UXF-405.UXF-405.CONFIGURATION_KEY",
                  "version": "1.0.0"
                },
                "semantic_type": "CONFIGURATION_KEY"
              },
              "precedence_order": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "CONFIGURATION.PRECEDENCE.PLATFORM.SECURITY.JURISDICTION.MARKET.ORGANIZATION.STOREFRONT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.PRECEDENCE_ORDER.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
                  "resolver_id": "RESOLVE.UXF-405.CONFIGURATION.PRECEDENCE.PLATFORM.SECURITY.JURISDICTION.MARKET.ORGANIZATION.STOREFRONT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
              },
              "resolved_source": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "UXF-405.RESOLVED_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.RESOLVED_SOURCE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CONFIGURATION_SOURCE_ID",
                  "resolver_id": "RESOLVE.UXF-405.UXF-405.RESOLVED_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "CONFIGURATION_SOURCE_ID"
              },
              "resolved_value": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "UXF-405.RESOLVED_VALUE"
                  ],
                  "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "UXF-405.RESOLVED_VALUE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.RESOLVED_VALUE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.UXF-405.UXF-405.RESOLVED_VALUE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "source_values": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "PLATFORM.SECURITY",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN.MEMBER.1",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-UXF-405-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/UXF/UXF-04.md",
                      "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                      "source_lines": "L642-L645",
                      "source_section": "24. Architectural Principles > UXF-405"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CONFIGURATION_SOURCE_ID",
                      "resolver_id": "RESOLVE.UXF-405.PLATFORM.SECURITY",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CONFIGURATION_SOURCE_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "JURISDICTION.MARKET",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN.MEMBER.2",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-UXF-405-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/UXF/UXF-04.md",
                      "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                      "source_lines": "L642-L645",
                      "source_section": "24. Architectural Principles > UXF-405"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CONFIGURATION_SOURCE_ID",
                      "resolver_id": "RESOLVE.UXF-405.JURISDICTION.MARKET",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CONFIGURATION_SOURCE_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "ORGANIZATION",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN.MEMBER.3",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-UXF-405-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/UXF/UXF-04.md",
                      "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                      "source_lines": "L642-L645",
                      "source_section": "24. Architectural Principles > UXF-405"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CONFIGURATION_SOURCE_ID",
                      "resolver_id": "RESOLVE.UXF-405.ORGANIZATION",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CONFIGURATION_SOURCE_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "STOREFRONT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN.MEMBER.4",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-UXF-405-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/UXF/UXF-04.md",
                      "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                      "source_lines": "L642-L645",
                      "source_section": "24. Architectural Principles > UXF-405"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CONFIGURATION_SOURCE_ID",
                      "resolver_id": "RESOLVE.UXF-405.STOREFRONT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CONFIGURATION_SOURCE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "semantic_type": "SET_OF<CONFIGURATION_SOURCE_ID>"
              },
              "source_versions": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "UXF-405.SOURCE_VERSIONS.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-UXF-405-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/UXF/UXF-04.md",
                      "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                      "source_lines": "L642-L645",
                      "source_section": "24. Architectural Principles > UXF-405"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "POLICY_VERSION",
                      "resolver_id": "RESOLVE.UXF-405.UXF-405.SOURCE_VERSIONS.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "POLICY_VERSION"
                  }
                ],
                "origin": {
                  "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VERSIONS.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "semantic_type": "SET_OF<POLICY_VERSION>"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "UXF-405.UXF-405.O1.1.CONFIGURATION_PRECEDENCE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CONFIGURATION_SOURCE_ID",
                  "resolver_id": "RESOLVE.UXF-405.UXF-405.UXF-405.O1.1.CONFIGURATION_PRECEDENCE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CONFIGURATION_SOURCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "UXF-405.UXF-405.O1.1.CONFIGURATION_PRECEDENCE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CONFIGURATION_SOURCE_ID",
                  "resolver_id": "OBSERVE.UXF-405.UXF-405.UXF-405.O1.1.CONFIGURATION_PRECEDENCE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CONFIGURATION_SOURCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "UXF-405.UXF-405.O1.1.CONFIGURATION_PRECEDENCE.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.UXF-405.UXF-405.UXF-405.O1.1.CONFIGURATION_PRECEDENCE.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "CONFIGURATION_PRECEDENCE"
          },
          "obligation_id": "UXF-405-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "UXF-405.UXF-405.O1.1.CONFIGURATION_PRECEDENCE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-UXF-405-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/UXF/UXF-04.md",
              "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
              "source_lines": "L642-L645",
              "source_section": "24. Architectural Principles > UXF-405"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CONFIGURATION_SOURCE_ID",
              "resolver_id": "OBSERVE.UXF-405.UXF-405.UXF-405.O1.1.CONFIGURATION_PRECEDENCE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CONFIGURATION_SOURCE_ID"
          },
          "operator_id": "CONFIGURATION_PRECEDENCE",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "configuration_key": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "UXF-405.CONFIGURATION_KEY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.CONFIGURATION_KEY.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_KEY",
                "resolver_id": "RESOLVE.UXF-405.UXF-405.CONFIGURATION_KEY",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_KEY"
            },
            "precedence_order": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "CONFIGURATION.PRECEDENCE.PLATFORM.SECURITY.JURISDICTION.MARKET.ORGANIZATION.STOREFRONT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.PRECEDENCE_ORDER.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
                "resolver_id": "RESOLVE.UXF-405.CONFIGURATION.PRECEDENCE.PLATFORM.SECURITY.JURISDICTION.MARKET.ORGANIZATION.STOREFRONT",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
            },
            "resolved_source": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "UXF-405.RESOLVED_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.RESOLVED_SOURCE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_SOURCE_ID",
                "resolver_id": "RESOLVE.UXF-405.UXF-405.RESOLVED_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_SOURCE_ID"
            },
            "resolved_value": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "UXF-405.RESOLVED_VALUE"
                ],
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "UXF-405.RESOLVED_VALUE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.RESOLVED_VALUE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.UXF-405.UXF-405.RESOLVED_VALUE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "source_values": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "PLATFORM.SECURITY",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN.MEMBER.1",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-UXF-405-OPT-1"
                    ],
                    "inference": false,
                    "source_document": "docs/UXF/UXF-04.md",
                    "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                    "source_lines": "L642-L645",
                    "source_section": "24. Architectural Principles > UXF-405"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CONFIGURATION_SOURCE_ID",
                    "resolver_id": "RESOLVE.UXF-405.PLATFORM.SECURITY",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CONFIGURATION_SOURCE_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "JURISDICTION.MARKET",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN.MEMBER.2",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-UXF-405-OPT-1"
                    ],
                    "inference": false,
                    "source_document": "docs/UXF/UXF-04.md",
                    "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                    "source_lines": "L642-L645",
                    "source_section": "24. Architectural Principles > UXF-405"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CONFIGURATION_SOURCE_ID",
                    "resolver_id": "RESOLVE.UXF-405.JURISDICTION.MARKET",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CONFIGURATION_SOURCE_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "ORGANIZATION",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN.MEMBER.3",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-UXF-405-OPT-1"
                    ],
                    "inference": false,
                    "source_document": "docs/UXF/UXF-04.md",
                    "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                    "source_lines": "L642-L645",
                    "source_section": "24. Architectural Principles > UXF-405"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CONFIGURATION_SOURCE_ID",
                    "resolver_id": "RESOLVE.UXF-405.ORGANIZATION",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CONFIGURATION_SOURCE_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "STOREFRONT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN.MEMBER.4",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-UXF-405-OPT-1"
                    ],
                    "inference": false,
                    "source_document": "docs/UXF/UXF-04.md",
                    "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                    "source_lines": "L642-L645",
                    "source_section": "24. Architectural Principles > UXF-405"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "CONFIGURATION_SOURCE_ID",
                    "resolver_id": "RESOLVE.UXF-405.STOREFRONT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "CONFIGURATION_SOURCE_ID"
                }
              ],
              "origin": {
                "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VALUES.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "semantic_type": "SET_OF<CONFIGURATION_SOURCE_ID>"
            },
            "source_versions": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "UXF-405.SOURCE_VERSIONS.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-UXF-405-OPT-1"
                    ],
                    "inference": false,
                    "source_document": "docs/UXF/UXF-04.md",
                    "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                    "source_lines": "L642-L645",
                    "source_section": "24. Architectural Principles > UXF-405"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "POLICY_VERSION",
                    "resolver_id": "RESOLVE.UXF-405.UXF-405.SOURCE_VERSIONS.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "POLICY_VERSION"
                }
              ],
              "origin": {
                "origin_id": "UXF-405.O1.1.CONFIGURATION_PRECEDENCE.SOURCE_VERSIONS.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "semantic_type": "SET_OF<POLICY_VERSION>"
            }
          }
        },
        {
          "assertion_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES",
          "evaluator_consumed_bindings": [
            "configuration_key",
            "configuration_sources",
            "expected_value",
            "resolved_source",
            "source_versions"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-UXF-405-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/UXF/UXF-04.md",
              "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
              "source_lines": "L642-L645",
              "source_section": "24. Architectural Principles > UXF-405"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.UXF-405.UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
              ],
              "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.AUTHORITY.ORIGIN",
              "origin_type": "APPROVED_DECISION"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-UXF-405-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/UXF/UXF-04.md",
              "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
              "source_lines": "L642-L645",
              "source_section": "24. Architectural Principles > UXF-405"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "RESOLVE.UXF-405.UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "configuration_key": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "UXF-405.CONFIGURATION_KEY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.CONFIGURATION_KEY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CONFIGURATION_KEY",
                  "resolver_id": "RESOLVE.UXF-405.UXF-405.CONFIGURATION_KEY",
                  "version": "1.0.0"
                },
                "semantic_type": "CONFIGURATION_KEY"
              },
              "configuration_sources": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "UXF-405.CONFIGURATION_SOURCES",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.CONFIGURATION_SOURCES.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
                  "resolver_id": "RESOLVE.UXF-405.UXF-405.CONFIGURATION_SOURCES",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
              },
              "expected_value": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "UXF-405.CANONICAL.CONFIGURATION.VALUE"
                  ],
                  "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "UXF-405.CANONICAL.CONFIGURATION.VALUE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.EXPECTED_VALUE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.UXF-405.UXF-405.CANONICAL.CONFIGURATION.VALUE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "resolved_source": {
                "authoritative_source": {
                  "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "UXF-405.RESOLVED_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.RESOLVED_SOURCE.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CONFIGURATION_SOURCE_ID",
                  "resolver_id": "RESOLVE.UXF-405.UXF-405.RESOLVED_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "CONFIGURATION_SOURCE_ID"
              },
              "source_versions": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                      "source_type": "APPROVED_DECISION",
                      "version": "2026-07-16"
                    },
                    "identifier": "UXF-405.SOURCE_VERSIONS.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                      "origin_type": "APPROVED_DECISION"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2C-OBT-C1-UXF-405-OPT-1"
                      ],
                      "inference": false,
                      "source_document": "docs/UXF/UXF-04.md",
                      "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                      "source_lines": "L642-L645",
                      "source_section": "24. Architectural Principles > UXF-405"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "POLICY_VERSION",
                      "resolver_id": "RESOLVE.UXF-405.UXF-405.SOURCE_VERSIONS.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "POLICY_VERSION"
                  }
                ],
                "origin": {
                  "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "semantic_type": "SET_OF<POLICY_VERSION>"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
                  ],
                  "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.AUTHORITY.ORIGIN",
                  "origin_type": "APPROVED_DECISION"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.UXF-405.UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
                  ],
                  "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                  "source_type": "APPROVED_DECISION",
                  "version": "2026-07-16"
                },
                "identifier": "UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2C-OBT-C1-UXF-405-OPT-1"
                  ],
                  "inference": false,
                  "source_document": "docs/UXF/UXF-04.md",
                  "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                  "source_lines": "L642-L645",
                  "source_section": "24. Architectural Principles > UXF-405"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.UXF-405.UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.UXF-405.UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "CONFIGURATION_RESOLVES"
          },
          "obligation_id": "UXF-405-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.CANONICAL.RESULT"
              ],
              "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
              "source_type": "APPROVED_DECISION",
              "version": "2026-07-16"
            },
            "identifier": "UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2C-OBT-C1-UXF-405-OPT-1"
              ],
              "inference": false,
              "source_document": "docs/UXF/UXF-04.md",
              "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
              "source_lines": "L642-L645",
              "source_section": "24. Architectural Principles > UXF-405"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_ENUM_VALUE",
              "resolver_id": "OBSERVE.UXF-405.UXF-405.UXF-405.O1.2.CONFIGURATION_RESOLVES.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_ENUM_VALUE"
          },
          "operator_id": "CONFIGURATION_RESOLVES",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "configuration_key": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "UXF-405.CONFIGURATION_KEY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.CONFIGURATION_KEY.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_KEY",
                "resolver_id": "RESOLVE.UXF-405.UXF-405.CONFIGURATION_KEY",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_KEY"
            },
            "configuration_sources": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "UXF-405.CONFIGURATION_SOURCES",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.CONFIGURATION_SOURCES.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CONFIGURATION_SOURCE_ID>",
                "resolver_id": "RESOLVE.UXF-405.UXF-405.CONFIGURATION_SOURCES",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CONFIGURATION_SOURCE_ID>"
            },
            "expected_value": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "UXF-405.CANONICAL.CONFIGURATION.VALUE"
                ],
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "UXF-405.CANONICAL.CONFIGURATION.VALUE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.EXPECTED_VALUE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.UXF-405.UXF-405.CANONICAL.CONFIGURATION.VALUE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "resolved_source": {
              "authoritative_source": {
                "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                "source_type": "APPROVED_DECISION",
                "version": "2026-07-16"
              },
              "identifier": "UXF-405.RESOLVED_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.RESOLVED_SOURCE.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CONFIGURATION_SOURCE_ID",
                "resolver_id": "RESOLVE.UXF-405.UXF-405.RESOLVED_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "CONFIGURATION_SOURCE_ID"
            },
            "source_versions": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
                    "source_type": "APPROVED_DECISION",
                    "version": "2026-07-16"
                  },
                  "identifier": "UXF-405.SOURCE_VERSIONS.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN.MEMBER.1",
                    "origin_type": "APPROVED_DECISION"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2C-OBT-C1-UXF-405-OPT-1"
                    ],
                    "inference": false,
                    "source_document": "docs/UXF/UXF-04.md",
                    "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                    "source_lines": "L642-L645",
                    "source_section": "24. Architectural Principles > UXF-405"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "POLICY_VERSION",
                    "resolver_id": "RESOLVE.UXF-405.UXF-405.SOURCE_VERSIONS.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "POLICY_VERSION"
                }
              ],
              "origin": {
                "origin_id": "UXF-405.O1.2.CONFIGURATION_RESOLVES.SOURCE_VERSIONS.ORIGIN",
                "origin_type": "APPROVED_DECISION"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2C-OBT-C1-UXF-405-OPT-1"
                ],
                "inference": false,
                "source_document": "docs/UXF/UXF-04.md",
                "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
                "source_lines": "L642-L645",
                "source_section": "24. Architectural Principles > UXF-405"
              },
              "semantic_type": "SET_OF<POLICY_VERSION>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Explicit allowed Storefront override wins only at its declared precedence"
      ],
      "contract_ast_sha256": "b7a072590cf46fbc0bb038a8b575b73fd94767a1eaae2d275efafb2b2d1e5f36",
      "contract_id": "P2C.C4.CONTRACT.UXF-405",
      "criticality": "HIGH",
      "disposition": "SOURCE_CLARIFICATION_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "P2C-OBT-C1-UXF-405-OPT-1",
            "source_type": "APPROVED_DECISION",
            "version": "2026-07-16"
          },
          "identifier": "UXF-405.UXF-405.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "UXF-405.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2C-OBT-C1-UXF-405-OPT-1"
            ],
            "inference": false,
            "source_document": "docs/UXF/UXF-04.md",
            "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
            "source_lines": "L642-L645",
            "source_section": "24. Architectural Principles > UXF-405"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.UXF-405.UXF-405.UXF-405.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "UXF-405.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.STOREFRONT_ID",
          "FIELD.ORGANIZATION_ID",
          "FIELD.ORGANIZATION_CONFIGURATION",
          "FIELD.STOREFRONT_OVERRIDE",
          "FIELD.PRECEDENCE",
          "FIELD.EFFECTIVE_CONFIGURATION"
        ],
        "producer": "UXF-405.EVIDENCE.PRODUCER",
        "required_collection_origin": "UXF-405.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.STOREFRONT_ID",
          "FIELD.ORGANIZATION_ID",
          "FIELD.ORGANIZATION_CONFIGURATION",
          "FIELD.STOREFRONT_OVERRIDE",
          "FIELD.PRECEDENCE",
          "FIELD.EFFECTIVE_CONFIGURATION"
        ],
        "required_values_or_hashes": [
          "UXF-405.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "UXF-405.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "UXF-405.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-69F4ED51ADA6F8627E9F",
        "P2C-C4-FX-6161CCADBA2D8E4893FC",
        "P2C-C4-FX-EF30ABD2CC11E5FB8EE1"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Applicable Organization value is ignored without an allowed override"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "UXF-405-O001",
          "obligation_text": "Storefronts inherit Organization configuration"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "UXF-405.O1.1.CONFIGURATION_PRECEDENCE",
            "UXF-405.O1.2.CONFIGURATION_RESOLVES"
          ],
          "coverage_count": 1,
          "obligation_id": "UXF-405-O001"
        }
      ],
      "operator_composition": [
        "CONFIGURATION_PRECEDENCE",
        "CONFIGURATION_RESOLVES"
      ],
      "positive_oracles": [
        "Storefront inherits applicable Organization configuration subject to governed override precedence"
      ],
      "preconditions": [
        "Storefront and parent Organization configurations are available"
      ],
      "prohibitions": [
        "Applicable Organization value is ignored without an allowed override"
      ],
      "requirement_id": "UXF-405",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2C-OBT-C1-UXF-405-OPT-1"
        ],
        "inference": false,
        "source_document": "docs/UXF/UXF-04.md",
        "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
        "source_lines": "L642-L645",
        "source_section": "24. Architectural Principles > UXF-405"
      },
      "source_statement": "Storefronts inherit Organization configuration.",
      "surrounding_source_context": "### UXF-405\n\nStorefronts inherit Organization configuration.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.UXF-405",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "SEMANTIC_ACCEPTANCE_RENDERER_C2",
    "runtime_status": "RUNTIME_ADAPTER_PENDING"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "ACCEPTANCE_READY",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-405-AC001",
        "UXF-405-AC002",
        "UXF-405-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-405-O001",
      "obligation_text": "Storefronts inherit Organization configuration"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Storefronts inherit Organization configuration.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-405",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Storefront Resolution",
    "source_context_sha256": "a4aa48d3f1cd6774c912e3d0d9a71261ec02ed64d28e7dfcc54b93457d19fae5",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "4d296e5e199b5b32c07a37a74c93d51bc3df0c295dacd687c71d61bc2a1fe896",
    "source_lines": "L3543-L6045",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-405"
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
  "stable_id": "UXF-405",
  "title": "Storefronts inherit Organization configuration",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-406 — Organizations inherit Platform configuration

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
      "requirement_id": "UXF-406",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "3329d3f6aad0696edd7325dc0cb830e645a51b7d11c0ff1edc3aba3ed3eb32a3"
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
        "UXF-406-AC001",
        "UXF-406-AC002",
        "UXF-406-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-406-O001",
      "obligation_text": "Organizations inherit Platform configuration"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organizations inherit Platform configuration.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-406",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-406",
    "source_context_sha256": "2bdfd28c1b5f6d340dd278ae52fcdf2b8b9289f1657337d49797142788564e0b",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "3329d3f6aad0696edd7325dc0cb830e645a51b7d11c0ff1edc3aba3ed3eb32a3",
    "source_lines": "L6047-L6122",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-406"
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
  "stable_id": "UXF-406",
  "title": "Organizations inherit Platform configuration",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-407 — Every configuration supports fallback

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
      "requirement_id": "UXF-407",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "0ac63466542570fc6e9fa3a8da5cd0d873de4152c0cb8a348765674f816789e7"
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
        "UXF-407-AC001",
        "UXF-407-AC002",
        "UXF-407-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-407-O001",
      "obligation_text": "Every configuration supports fallback"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Every configuration supports fallback.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-407",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-407",
    "source_context_sha256": "b8df707f36cccb52ea8bcddb9bae470ce2aaaab074606e001e9b1b9f85dc8fdc",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "0ac63466542570fc6e9fa3a8da5cd0d873de4152c0cb8a348765674f816789e7",
    "source_lines": "L6124-L6199",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-407"
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
  "stable_id": "UXF-407",
  "title": "Every configuration supports fallback",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-408 — White-label configuration requires no source-code changes

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
      "requirement_id": "UXF-408",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "d1b8aac3984d44d9b7d4562765bfc03d6b0975197908776d82317ecabe49c5a7"
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
        "UXF-408-AC001",
        "UXF-408-AC002",
        "UXF-408-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-408-O001",
      "obligation_text": "White-label configuration requires no source-code changes"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-044",
      "selected_disposition": "ROUTE_TO_REMEDIATION"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "White-label configuration requires no source-code changes.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-408",
    "previous_temporary_key": null,
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-408",
    "source_context_sha256": "62e9ef2761c9a5dc17d5500dd8e10ff07eadb88fb52400d8f88078839255be17",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "d1b8aac3984d44d9b7d4562765bfc03d6b0975197908776d82317ecabe49c5a7",
    "source_lines": "L6201-L6288",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-408"
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
  "stable_id": "UXF-408",
  "title": "White-label configuration requires no source-code changes",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-409 — Only published configurations participate in runtime rendering

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
      "requirement_id": "UXF-409",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "2e97b65a4b62a2de2dac71cd4300cfc763c6d3cd7a71facc37cda63653d0fe2e"
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
        "UXF-409-AC001",
        "UXF-409-AC002",
        "UXF-409-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-409-O001",
      "obligation_text": "Only published configurations participate in runtime rendering"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Only published configurations participate in runtime rendering.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-409",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-409",
    "source_context_sha256": "4484c8e269377f0820f3dd32d8574eb6bd0c403382769765bedc8151c1abe2c8",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "2e97b65a4b62a2de2dac71cd4300cfc763c6d3cd7a71facc37cda63653d0fe2e",
    "source_lines": "L6290-L6365",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-409"
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
  "stable_id": "UXF-409",
  "title": "Only published configurations participate in runtime rendering",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-410 — Supplier systems never participate in Experience Resolution

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "UXF-410",
      "source_document": "docs/UXF/UXF-04.md",
      "source_fingerprint": "3e263107edefcffb98fb70963687b830729a385f4df25cf164d978ab5c2db546"
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
        "UXF-410-AC001",
        "UXF-410-AC002",
        "UXF-410-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-410-O001",
      "obligation_text": "Supplier systems never participate in Experience Resolution"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier systems never participate in Experience Resolution.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "UXF-410",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "UXF-410",
    "source_context_sha256": "7d5bfd0da0867e66c52dd4a295a6afcab62ffe1d9a046263082295711f42745a",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "3e263107edefcffb98fb70963687b830729a385f4df25cf164d978ab5c2db546",
    "source_lines": "L6367-L6446",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > UXF-410"
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
  "stable_id": "UXF-410",
  "title": "Supplier systems never participate in Experience Resolution",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
