---
document_code: "UXF-04"
title: "White-label, Localization & Runtime Context Resolution"
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

## v2.3 normative requirement appendix



<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R001 — The YSim Platform never renders pages directly

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-04-R001-AC001",
      "given": "a user in the applicable channel and context for The YSim Platform never renders pages directly",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-04-R001-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-04-R001-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The YSim Platform never renders pages directly",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-04-R001-O001"
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
        "UXF-04-R001-AC001",
        "UXF-04-R001-AC002"
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
    "source_lines": "L44",
    "source_section": "2. Runtime Resolution Philosophy"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-04-R002-AC001",
      "given": "a user in the applicable channel and context for URL Resolution never bypasses Storefront configuration",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-04-R002-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-04-R002-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for URL Resolution never bypasses Storefront configuration",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-04-R002-O001"
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
        "UXF-04-R002-AC001",
        "UXF-04-R002-AC002"
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
    "source_lines": "L198",
    "source_section": "5. URL Resolution"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-04-R003-AC001",
      "given": "a user in the applicable channel and context for Tracking must never bypass business policies",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-04-R003-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-04-R003-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Tracking must never bypass business policies",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-04-R003-O001"
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
        "UXF-04-R003-AC001",
        "UXF-04-R003-AC002"
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
    "source_lines": "L230",
    "source_section": "6. Tracking Resolution"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-04-R004-AC001",
      "given": "a user in the applicable channel and context for Identity never changes published business rules",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-04-R004-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-04-R004-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Identity never changes published business rules",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-04-R004-O001"
      ],
      "when": "the affected state is rendered or action is requested"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "UXF-04-R004-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Identity never changes published business rules",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "UXF-04-R004-O001"
      ],
      "when": "the violating input or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
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
      "criterion_references": [],
      "rationale": "UXF-04-R004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-04-R004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-04-R004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "UXF-04-R004-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-04-R004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-04-R004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L331",
    "source_section": "11. Identity Resolution"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "UXF-04-R005-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Feature Flags never replace authorization",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the prohibited security decision path produces no effective permission or protected-state change, and conformance evidence identifies the attempted bypass",
      "verifies": [
        "UXF-04-R005-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "UXF-04-R005-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Feature Flags never replace authorization",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "UXF-04-R005-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "UXF-04-R005-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Feature Flags never replace authorization",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "UXF-04-R005-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "UXF-04-R005-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Feature Flags never replace authorization",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "UXF-04-R005-O001"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-04-R005-AC001",
        "UXF-04-R005-AC002",
        "UXF-04-R005-AC003",
        "UXF-04-R005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R005-O001",
      "obligation_text": "Feature Flags never replace authorization"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "UXF-04-R005-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-04-R005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-04-R005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "UXF-04-R005-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-04-R005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-04-R005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L348",
    "source_section": "12. Feature Flag Resolution"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "UXF-04-R006-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by White-label configuration must not require source-code modification",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance evidence identifies the governing configuration and shows that an approved configuration change alters the governed result without a source-code variant",
      "verifies": [
        "UXF-04-R006-O001"
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
        "UXF-04-R006-AC001"
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
    "source_fingerprint": "53334c34dd3daf7dfb559007ed0add131a1d289885f02c18e4934a4b30ffbfff",
    "source_lines": "L512",
    "source_section": "17. White-label Architecture"
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
### UXF-04-R007 — Examples: - Guest Checkout - Mandatory Login - Country Restrictions - Product Visibility - Promo…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-04-R007-AC001",
      "given": "an operational task within the scope of Examples: - Guest Checkout - Mandatory Login - Country Restrictions - Product Visibility - Promo…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "UXF-04-R007-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-04-R007-AC002",
      "given": "an operational task within the scope of Examples: - Guest Checkout - Mandatory Login - Country Restrictions - Product Visibility - Promo…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "UXF-04-R007-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-04-R007-AC003",
      "given": "an operational task within the scope of Examples: - Guest Checkout - Mandatory Login - Country Restrictions - Product Visibility - Promo…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "UXF-04-R007-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-04-R007-AC004",
      "given": "an operational task within the scope of Examples: - Guest Checkout - Mandatory Login - Country Restrictions - Product Visibility - Promo…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "UXF-04-R007-O004"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-04-R007-AC005",
      "given": "an operational task within the scope of Examples: - Guest Checkout - Mandatory Login - Country Restrictions - Product Visibility - Promo…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "UXF-04-R007-O005"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "UXF-04-R007-AC006",
      "given": "an operational task within the scope of Examples: - Guest Checkout - Mandatory Login - Country Restrictions - Product Visibility - Promo…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "UXF-04-R007-O006"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "UXF-04-R007-AC007",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Examples: - Guest Checkout - Mandatory Login - Country Restrictions - Product Visibility - Promo…",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "UXF-04-R007-O001",
        "UXF-04-R007-O002",
        "UXF-04-R007-O003",
        "UXF-04-R007-O004",
        "UXF-04-R007-O005",
        "UXF-04-R007-O006"
      ],
      "when": "operational verification is performed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-04-R007-AC001",
        "UXF-04-R007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R007-O001",
      "obligation_text": "Examples: Guest Checkout."
    },
    {
      "acceptance_criterion_references": [
        "UXF-04-R007-AC002",
        "UXF-04-R007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R007-O002",
      "obligation_text": "Examples: Mandatory Login."
    },
    {
      "acceptance_criterion_references": [
        "UXF-04-R007-AC003",
        "UXF-04-R007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R007-O003",
      "obligation_text": "Examples: Country Restrictions."
    },
    {
      "acceptance_criterion_references": [
        "UXF-04-R007-AC004",
        "UXF-04-R007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R007-O004",
      "obligation_text": "Examples: Product Visibility."
    },
    {
      "acceptance_criterion_references": [
        "UXF-04-R007-AC005",
        "UXF-04-R007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R007-O005",
      "obligation_text": "Examples: Promotion Eligibility."
    },
    {
      "acceptance_criterion_references": [
        "UXF-04-R007-AC006",
        "UXF-04-R007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "UXF-04-R007-O006",
      "obligation_text": "Examples: Payment Availability."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "UXF-04-R007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "UXF-04-R007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "UXF-04-R007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "UXF-04-R007 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "UXF-04-R007-AC001",
        "UXF-04-R007-AC002",
        "UXF-04-R007-AC003",
        "UXF-04-R007-AC004",
        "UXF-04-R007-AC005",
        "UXF-04-R007-AC006"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "UXF-04-R007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Examples: - Guest Checkout - Mandatory Login - Country Restrictions - Product Visibility - Promotion Eligibility - Payment Availability",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008",
      "P2-DEC-010"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-UXF-04-007",
    "previous_temporary_key": "TMP-UXF-04-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Tracking Resolution",
    "source_context_sha256": "b80056705a6b803c3799b33afb736309daefdd125de1900660f1204177055081",
    "source_document": "docs/UXF/UXF-04.md",
    "source_fingerprint": "f2434bed7593bc69704e57de02a50d64198295f49e3e15040c837f20c3f6f95f",
    "source_lines": "L556-L563",
    "source_section": "20. Runtime Policies"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "UXF-04-R007",
  "title": "Examples: - Guest Checkout - Mandatory Login - Country Restrictions - Product Visibility - Promo…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### UXF-04-R008 — Editable configurations are never cached directly

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-04-R008-AC001",
      "given": "a user in the applicable channel and context for Editable configurations are never cached directly",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-04-R008-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-04-R008-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Editable configurations are never cached directly",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-04-R008-O001"
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
        "UXF-04-R008-AC001",
        "UXF-04-R008-AC002"
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
    "source_lines": "L581",
    "source_section": "21. Runtime Caching"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-04-R009-AC001",
      "given": "a user in the applicable channel and context for The Runtime Resolution Engine must: - validate domain ownership",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-04-R009-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-04-R009-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Runtime Resolution Engine must: - validate domain ownership",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-04-R009-O001"
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
        "UXF-04-R009-AC001",
        "UXF-04-R009-AC002"
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
    "source_lines": "L587-L589",
    "source_section": "22. Runtime Security"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-04-R010-AC001",
      "given": "a user in the applicable channel and context for The Runtime Resolution Engine must: - validate organization ownership",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-04-R010-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-04-R010-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Runtime Resolution Engine must: - validate organization ownership",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-04-R010-O001"
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
        "UXF-04-R010-AC001",
        "UXF-04-R010-AC002"
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
    "source_fingerprint": "e8dffd9b9aeb0b256da2cc81f6cc7230e2804de4cb25f7908dc6b45836d556aa",
    "source_lines": "L587-L590",
    "source_section": "22. Runtime Security"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-04-R011-AC001",
      "given": "a user in the applicable channel and context for The Runtime Resolution Engine must: - validate storefront publication status",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-04-R011-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-04-R011-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Runtime Resolution Engine must: - validate storefront publication status",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-04-R011-O001"
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
        "UXF-04-R011-AC001",
        "UXF-04-R011-AC002"
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
    "source_fingerprint": "55399aa87c3c19215b09bb7f937fad26ae3ae0afbfee796b36db9e5fe93f3f25",
    "source_lines": "L587-L591",
    "source_section": "22. Runtime Security"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-04-R012-AC001",
      "given": "a user in the applicable channel and context for The Runtime Resolution Engine must: - validate localization",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-04-R012-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-04-R012-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Runtime Resolution Engine must: - validate localization",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-04-R012-O001"
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
        "UXF-04-R012-AC001",
        "UXF-04-R012-AC002"
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
    "source_fingerprint": "32ec30b07107e5c6b958e372dfd08285170d881aaef42b9110d75b912c810fe1",
    "source_lines": "L587-L592",
    "source_section": "22. Runtime Security"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-04-R013-AC001",
      "given": "a user in the applicable channel and context for The Runtime Resolution Engine must: - validate feature flags",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-04-R013-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-04-R013-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Runtime Resolution Engine must: - validate feature flags",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-04-R013-O001"
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
        "UXF-04-R013-AC001",
        "UXF-04-R013-AC002"
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
    "source_fingerprint": "c10ed124b237306ace8397f67b5ef05d76c644215ae2cd8f29b6275525094e6a",
    "source_lines": "L587-L593",
    "source_section": "22. Runtime Security"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-04-R014-AC001",
      "given": "a user in the applicable channel and context for The Runtime Resolution Engine must: - validate runtime policies",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-04-R014-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-04-R014-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for The Runtime Resolution Engine must: - validate runtime policies",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-04-R014-O001"
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
        "UXF-04-R014-AC001",
        "UXF-04-R014-AC002"
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
    "source_fingerprint": "a43e8364b0d6d1c53a9ae3370a6b1b382bb5d875a1b7edbfbfbc9046412c4684",
    "source_lines": "L587-L594",
    "source_section": "22. Runtime Security"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-401-AC001",
      "given": "a user in the applicable channel and context for Every request is resolved through Runtime Context Resolution",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-401-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-401-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every request is resolved through Runtime Context Resolution",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-401-O001"
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
        "UXF-401-AC001",
        "UXF-401-AC002"
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
    "source_fingerprint": "84dcf74f73735397e842fe273776aa6e774855c6c346668cd50cfe59fc171348",
    "source_lines": "L618-L621",
    "source_section": "24. Architectural Principles > UXF-401"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-402-AC001",
      "given": "a user in the applicable channel and context for Domains determine storefront identity",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-402-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-402-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Domains determine storefront identity",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-402-O001"
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
        "UXF-402-AC001",
        "UXF-402-AC002"
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
    "source_fingerprint": "426995d29a2c3db7c834526585b4e47e7c5c743419c4c7a4e4cf822106ab0ea7",
    "source_lines": "L624-L627",
    "source_section": "24. Architectural Principles > UXF-402"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-403-AC001",
      "given": "a user in the applicable channel and context for Tracking participates in runtime experience generation",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-403-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-403-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Tracking participates in runtime experience generation",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-403-O001"
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
        "UXF-403-AC001",
        "UXF-403-AC002"
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
    "source_fingerprint": "bde3215ad6ca6177718e911b5b63b8ac7af1a370d1faf2cc24fd8f76438e5bbe",
    "source_lines": "L630-L633",
    "source_section": "24. Architectural Principles > UXF-403"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-404-AC001",
      "given": "a user in the applicable channel and context for Localization defines commercial experience",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-404-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-404-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Localization defines commercial experience",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-404-O001"
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
        "UXF-404-AC001",
        "UXF-404-AC002"
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
    "source_fingerprint": "ec1c2ae0761b9770ffbdabc796430afa8dcf56d27954155f40ed391c6240af74",
    "source_lines": "L636-L639",
    "source_section": "24. Architectural Principles > UXF-404"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-405-AC001",
      "given": "a user in the applicable channel and context for Storefronts inherit Organization configuration",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "a missing child value resolves to the parent configuration, an explicit child override wins only at its declared scope, and the rendered result identifies the effective source",
      "verifies": [
        "UXF-405-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_INHERITANCE_FAILURE_V1",
      "criterion_id": "UXF-405-AC002",
      "given": "a child experience with no local value and an invalid or unavailable parent configuration for Storefronts inherit Organization configuration",
      "observable_evidence": "child and parent configuration identities, resolution trace, fallback or failure result, and rendered value",
      "then": "resolution produces the declared deterministic fallback or a visible configuration failure and never renders an unexplained value",
      "verifies": [
        "UXF-405-O001"
      ],
      "when": "the inherited value is resolved"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-405-AC001",
        "UXF-405-AC002"
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
    "source_fingerprint": "9fd9e69c066cfadbf0aaaa5da8c7061a52fe82cf9a250889adc64a4d2c39bd5b",
    "source_lines": "L642-L645",
    "source_section": "24. Architectural Principles > UXF-405"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-406-AC001",
      "given": "a user in the applicable channel and context for Organizations inherit Platform configuration",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "a missing child value resolves to the parent configuration, an explicit child override wins only at its declared scope, and the rendered result identifies the effective source",
      "verifies": [
        "UXF-406-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_INHERITANCE_FAILURE_V1",
      "criterion_id": "UXF-406-AC002",
      "given": "a child experience with no local value and an invalid or unavailable parent configuration for Organizations inherit Platform configuration",
      "observable_evidence": "child and parent configuration identities, resolution trace, fallback or failure result, and rendered value",
      "then": "resolution produces the declared deterministic fallback or a visible configuration failure and never renders an unexplained value",
      "verifies": [
        "UXF-406-O001"
      ],
      "when": "the inherited value is resolved"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "UXF-406-AC001",
        "UXF-406-AC002"
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
    "source_fingerprint": "7351c5911c0c7d7060681d8392ca58782e03e7197607bb49027c314184a2171a",
    "source_lines": "L648-L651",
    "source_section": "24. Architectural Principles > UXF-406"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-407-AC001",
      "given": "a user in the applicable channel and context for Every configuration supports fallback",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output exposes every required content element and action, keeps prohibited content absent, and makes the applicable confirmation or fallback directly observable",
      "verifies": [
        "UXF-407-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-407-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Every configuration supports fallback",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-407-O001"
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
        "UXF-407-AC001",
        "UXF-407-AC002"
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
    "source_fingerprint": "c7a4d501827a817a86006b4f3ea165db7867fb06bb7daf6919e5ea2a360d5112",
    "source_lines": "L654-L657",
    "source_section": "24. Architectural Principles > UXF-407"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "UXF-408-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by White-label configuration requires no source-code changes",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance evidence identifies the governing configuration and shows that an approved configuration change alters the governed result without a source-code variant",
      "verifies": [
        "UXF-408-O001"
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
        "UXF-408-AC001"
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
    "source_fingerprint": "5fe48f231bce0afd24c9c5e79e949b310a8ea7a26e892cf81c185c810fa3b677",
    "source_lines": "L660-L663",
    "source_section": "24. Architectural Principles > UXF-408"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-409-AC001",
      "given": "a user in the applicable channel and context for Only published configurations participate in runtime rendering",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the rendered output identifies the applied runtime context, reflects the values resolved for that context, and contains no unresolved configuration token",
      "verifies": [
        "UXF-409-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-409-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Only published configurations participate in runtime rendering",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-409-O001"
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
        "UXF-409-AC001",
        "UXF-409-AC002"
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
    "source_fingerprint": "654ff26b786652d43b30be0c47eb2ee64a21a39500b8844131b0f9c312962f40",
    "source_lines": "L666-L669",
    "source_section": "24. Architectural Principles > UXF-409"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "UX_JOURNEY_OBSERVATION_V1",
      "criterion_id": "UXF-410-AC001",
      "given": "a user in the applicable channel and context for Supplier systems never participate in Experience Resolution",
      "observable_evidence": "rendered UI state, enabled or unavailable action, user-visible confirmation or fallback, and exposed payload fields",
      "then": "the prohibited content or action is absent from both the rendered state and its customer-facing payload, while the permitted journey remains usable",
      "verifies": [
        "UXF-410-O001"
      ],
      "when": "the user reaches the relevant journey state or invokes the available action"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "UX_BOUNDARY_FAILURE_V1",
      "criterion_id": "UXF-410-AC002",
      "given": "a missing, prohibited, inaccessible, or inapplicable journey input for Supplier systems never participate in Experience Resolution",
      "observable_evidence": "rendered state, payload-field inspection, unavailable action or fallback, and user-visible outcome",
      "then": "the prohibited information remains absent and the action is unavailable or follows the requirement-specific fallback with a visible outcome",
      "verifies": [
        "UXF-410-O001"
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
        "UXF-410-AC001",
        "UXF-410-AC002"
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
    "source_fingerprint": "c90264555fc73333416a9d97e58aed1a9a8a879854d0262f72a1507d2e8eae0f",
    "source_lines": "L672-L675",
    "source_section": "24. Architectural Principles > UXF-410"
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
