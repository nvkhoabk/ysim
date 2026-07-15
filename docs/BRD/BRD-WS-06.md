---
document_code: "BRD-WS-06"
title: "Promotion, Coupon, Campaign & Sales Enablement"
product_baseline: "2.3"
document_revision: "2.3.0-draft.1"
lifecycle_status: "V2.3_DRAFT"
language: "vi-VN"
source_baseline: "v2.2"
generated_registry_role: "BRD_CANONICAL_SOURCE"
last_remediated_on: "2026-07-15"
---
## Thẩm quyền nguồn yêu cầu v2.3

Các khối `YSIM:REQUIREMENT` trong phụ lục chuẩn tắc là nguồn yêu cầu có thẩm quyền cho baseline 2.3. Nội dung legacy bên dưới được giữ làm ngữ cảnh; nếu có khác biệt, khối chuẩn tắc và các quyết định v2.3 đã phê duyệt được ưu tiên.

# BRD Workshop 06

# Promotion, Coupon, Campaign & Sales Enablement

---

# 1. Workshop Objective

Workshop này xác định toàn bộ mô hình Promotion, Coupon, Campaign và Sales Enablement của nền tảng YSim.

Workshop này xây dựng các công cụ hỗ trợ bán hàng dành cho Organization, Sales, Agency và Collaborator.

Workshop bao gồm:

- Promotion
- Coupon
- Campaign
- Landing Page
- Sales Enablement
- Reference QR
- Promotion QR
- Tracking
- Marketing Attribution
- Promotion Funding
- Promotion Snapshot

Workshop này là Foundation cho:

- Storefront
- Customer Portal
- Checkout
- Payment
- CRM
- Analytics

---

# 2. Business Objects Introduced

| Business Object | Status |
|-----------------|--------|
| Promotion | NEW |
| Coupon | NEW |
| Campaign | NEW |
| Promotion Rule | NEW |
| Promotion Audience | NEW |
| Promotion Funding | NEW |
| Promotion Snapshot | NEW |
| Landing Page | NEW |
| Reference QR | NEW |
| Promotion QR | NEW |
| Marketing Attribution | NEW |
| Tracking Link | NEW |
| Sales Tool | NEW |

---

# 3. Sales Enablement Domain

YSim xây dựng một Business Domain độc lập:

## Sales Enablement

Bao gồm:

- Landing Page
- Reference QR
- Tracking Link
- Marketing Attribution
- Campaign
- Sales Tool

Sales Enablement không phải Marketing.

Sales Enablement là tập hợp các công cụ giúp Distribution Network bán hàng hiệu quả hơn.

---

# 4. Promotion Ownership

Promotion thuộc Organization.

Promotion không thuộc:

- Product
- Storefront
- Landing Page
- Campaign

Campaign chỉ sử dụng Promotion.

Storefront chỉ Publish Promotion.

---

# 5. Coupon

Coupon là một loại Promotion.

Version 2.0 hỗ trợ:

- Fixed Amount
- Percentage
- Free Gift
- Bundle Promotion

Bundle nhiều dịch vụ được giữ lại cho các phiên bản sau.

---

# 6. Coupon Inheritance

Coupon kế thừa theo Distribution Network.

Ví dụ:

```text
YSim
    │
    ▼
ABC Travel
    │
    ▼
Agency
    │
    ▼
Collaborator
```

Child Organization có thể:

- Enable
- Disable
- Publish

Coupon kế thừa từ Parent.

Không cần tạo lại Coupon.

Coupon thuộc Price Book Owner nhưng có thể được kế thừa từ Parent giống như Price Book.

---

# 7. Campaign

Campaign là chiến lược bán hàng.

Campaign có thể bao gồm:

- Promotion
- Coupon
- Landing Page
- Reference QR
- Tracking
- Product Collection
- Analytics

Campaign không phải Landing Page.

Landing Page là Business Asset có thể tái sử dụng.

---

# 8. Landing Page

Landing Page thuộc Storefront.

Một Landing Page có thể được nhiều Campaign sử dụng.

Landing Page là công cụ kỹ thuật phục vụ bán hàng.

Campaign là chiến lược kinh doanh.

Hai khái niệm độc lập.

---

# 9. Reference QR

Reference QR là Business Object độc lập.

Reference QR không phải:

- Payment QR
- eSIM QR

Reference QR là điểm vào của Sales Funnel.

Reference QR có thể trỏ tới:

- Storefront
- Landing Page
- Product
- Product Collection

Reference QR luôn gắn Tracking ID.

Người dùng có quyền bán hàng có thể tạo:

- QR cho toàn Storefront
- QR cho Landing Page
- QR cho một Product
- QR cho một Collection

Reference QR có thể lọc sẵn Product để Customer chỉ cần thanh toán.

---

# 10. Promotion QR

Promotion QR là một loại QR riêng.

Customer trong quá trình Checkout có thể:

- Scan Promotion QR
- Upload Promotion QR

để áp dụng:

- Coupon
- Promotion
- Campaign

Promotion QR hoàn toàn khác:

- Payment QR
- eSIM QR
- Reference QR

---

# 11. Tracking

Tracking luôn gắn với User.

Tracking thuộc:

User

↓

Organization

↓

Distribution Network

Tracking dùng để:

- ghi nhận doanh số
- tính Commission
- Marketing Attribution

Tracking không phụ thuộc Campaign.

---

# 12. Marketing Attribution

Marketing Attribution là Business Object độc lập.

Một giao dịch cần Snapshot:

- Storefront
- Landing Page
- Campaign
- Reference QR
- Tracking ID
- Sales User
- Organization
- Distribution Path

Marketing Attribution phục vụ:

- Analytics
- Commission
- Reporting
- Settlement

---

# 13. Promotion Rule

Promotion Rule hỗ trợ:

- Country
- Product
- Category
- Collection
- Customer Group
- Organization
- Campaign
- Payment Method
- Date Range
- Order Value
- Quantity

Các Rule nâng cao sẽ triển khai ở phiên bản sau.

---

# 14. Promotion Audience

Promotion có Audience riêng.

Version 2.0 hỗ trợ:

- Public
- Customer Group
- Imported Customer List
- Invitation Only

Promotion có thể yêu cầu Customer xác thực thông tin trước khi áp dụng.

---

# 15. Coupon Eligibility

Coupon có thể yêu cầu Customer nhập hoặc xác thực thông tin.

Ví dụ:

- Email
- Phone Number
- Referral Phone
- Company Name
- Invitation Code
- Access Code

Có thể cấu hình:

- Exact Match
- Ignore Case
- Case Sensitive
- Regex
- Whitelist

Đây là tính năng Optional.

---

# 16. Promotion Funding

Mỗi Promotion phải có Funding Owner.

Funding Owner mặc định là Organization tạo Promotion.

Promotion Funding quản lý:

- Funding Owner
- Budget
- Used Budget
- Remaining Budget

Chi phí Promotion luôn được tính vào chi phí Marketing của Funding Owner.

Ví dụ:

Coupon do YSim tạo.

↓

ABC Travel kế thừa.

↓

YSim chịu chi phí Promotion.

ABC Travel vẫn hưởng doanh thu.

Ngược lại:

Coupon do ABC Travel tạo.

↓

ABC Travel tự chịu chi phí Promotion.

↓

Khoản thanh toán cho YSim không thay đổi.

---

# 17. Promotion Stack Policy

Promotion Engine hỗ trợ:

- Stackable
- Exclusive
- Highest Benefit

Version 2.0 mặc định:

Stackable.

Promotion hoặc Coupon có thể Override Stack Policy.

---

# 18. Promotion Snapshot

Promotion Snapshot được tạo sau Payment Success.

Snapshot bao gồm:

- Promotion
- Coupon
- Funding
- Audience
- Campaign
- Tracking
- Promotion Rule
- Stack Policy

Promotion Snapshot phục vụ:

- Settlement
- Audit
- Analytics

---

# 19. Sales Tool

Sales Tool bao gồm:

- Landing Page
- Reference QR
- Tracking Link
- Short URL

Các công cụ khác sẽ mở rộng trong các phiên bản sau.

---

# 20. Deferred Scope

Chưa triển khai trong Version 2.0:

- Loyalty
- Membership
- Referral Program
- Bundle nhiều dịch vụ
- AI Promotion
- AI Recommendation
- Social Campaign

Kiến trúc được giữ chỗ để mở rộng.

---

# 21. Business Decisions (Locked)

## BD-06-001

Promotion thuộc Organization.

---

## BD-06-002

Coupon thuộc Price Book Owner và hỗ trợ kế thừa theo Distribution Network.

---

## BD-06-003

Campaign là chiến lược bán hàng.

Landing Page là Business Asset.

---

## BD-06-004

Landing Page thuộc Storefront.

Một Landing Page có thể phục vụ nhiều Campaign.

---

## BD-06-005

Reference QR là Business Object độc lập.

---

## BD-06-006

Promotion QR là Business Object độc lập.

---

## BD-06-007

Tracking luôn gắn với User và Organization.

---

## BD-06-008

Marketing Attribution là Business Object độc lập.

---

## BD-06-009

Promotion Rule chỉ hỗ trợ các điều kiện đã thống nhất trong Version 2.0.

---

## BD-06-010

Coupon Eligibility là tính năng Optional.

---

## BD-06-011

Promotion Funding thuộc Organization tạo Promotion.

---

## BD-06-012

Chi phí Promotion luôn được ghi nhận vào chi phí Marketing của Funding Owner.

---

## BD-06-013

Promotion Engine hỗ trợ Stack Policy.

Version 2.0 mặc định là Stackable.

---

## BD-06-014

Promotion Snapshot được tạo sau Payment Success.

---

## BD-06-015

Sales Enablement là Domain độc lập.

---

## BD-06-016

Referral, Loyalty, Bundle nhiều dịch vụ và AI Promotion được đưa vào Deferred Scope.

---

# 22. Sales Enablement Architecture

```text
                         Organization
                               │
                               ▼
                     Sales Enablement Domain
                               │
      ┌──────────────┬──────────────┬──────────────┐
      │              │              │
 Landing Page   Reference QR   Tracking Link
      │              │              │
      └──────────────┼──────────────┘
                     ▼
           Marketing Attribution
                     │
                     ▼
                 Campaign
                     │
          ┌──────────┼──────────┐
          │          │          │
     Promotion    Coupon   Promotion Rule
          │          │          │
          └──────────┼──────────┘
                     ▼
             Promotion Engine
                     │
      ┌──────────────┼──────────────┐
      │              │              │
 Eligibility     Funding      Stack Policy
      │              │              │
      └──────────────┴──────────────┘
                     │
                     ▼
              Payment Success
                     │
                     ▼
           Promotion Snapshot
                     │
                     ▼
         Settlement / Analytics
```

---

# 23. Enterprise Design Principles

## EP-06-001

Sales Enablement là Domain độc lập với Product Domain và Commercial Domain.

---

## EP-06-002

Landing Page là Business Asset.

Không thuộc Campaign.

---

## EP-06-003

Reference QR, Promotion QR, Payment QR và eSIM QR là bốn Business Object độc lập.

---

## EP-06-004

Tracking luôn gắn với User và Organization.

---

## EP-06-005

Promotion Funding luôn thuộc Organization tạo Promotion.

---

## EP-06-006

Promotion Snapshot chỉ được tạo sau Payment Success.

---

# 24. Traceability

Workshop này kế thừa:

- BRD-WS-01
- BRD-WS-02
- BRD-WS-03
- BRD-WS-04
- BRD-WS-05

---

# 25. Impacts to Other Domains

Workshop này ảnh hưởng tới:

- Sales Enablement Domain
- Promotion Engine
- Campaign Management
- Checkout
- Payment
- Commission Engine
- Settlement
- CRM
- Analytics
- Reporting
- API
- DMS
- DBD

---

# 26. Workshop Status

**Status:** FROZEN

Workshop này là Foundation cho:

- Promotion Engine
- Campaign Management
- Sales Enablement
- Marketing Attribution
- Checkout
- CRM
- Analytics

---

# 27. Next Workshop

**BRD-WS-07 – Order Lifecycle, Cart & Checkout Flow**

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-001 — Promotion thuộc Organization

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-001-AC001",
      "given": "the applicable business context, actor, and input for Promotion thuộc Organization",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-06-001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Promotion thuộc Organization",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-06-001-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-001-AC001",
        "BD-06-001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-001-O001",
      "obligation_text": "Promotion thuộc Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Promotion thuộc Organization.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Promotion Ownership",
    "source_context_sha256": "b22ee6f1f8905617e89fde3116f5712a49a92cd1bf0f7d19f6b06fd726c87ebc",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "e858e38177c2f6ed4182f6bf1242498bf5a397565f8e8db376427f497851976d",
    "source_lines": "L468-L471",
    "source_section": "21. Business Decisions (Locked) > BD-06-001"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-001",
  "title": "Promotion thuộc Organization",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-002 — Coupon thuộc Price Book Owner và hỗ trợ kế thừa theo Distribution Network

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-002-AC001",
      "given": "the applicable business context, actor, and input for Coupon thuộc Price Book Owner và hỗ trợ kế thừa theo Distribution Network",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-06-002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Coupon thuộc Price Book Owner và hỗ trợ kế thừa theo Distribution Network",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-06-002-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-002-AC001",
        "BD-06-002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-002-O001",
      "obligation_text": "Coupon thuộc Price Book Owner và hỗ trợ kế thừa theo Distribution Network"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-06-002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-06-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-06-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-06-002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-06-002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-06-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Coupon thuộc Price Book Owner và hỗ trợ kế thừa theo Distribution Network.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-06-002",
    "source_context_sha256": "1acd51c4b0b0643fd26bc75f55273297179c68edfdffea32e1339a518dda7b05",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "ec5a2bec0f72ba7b02d24ab4ae6274909733c1eec7d4f8b0861e272cee93a8e3",
    "source_lines": "L474-L477",
    "source_section": "21. Business Decisions (Locked) > BD-06-002"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-002",
  "title": "Coupon thuộc Price Book Owner và hỗ trợ kế thừa theo Distribution Network",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-003 — Campaign là chiến lược bán hàng. Landing Page là Business Asset

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-003-AC001",
      "given": "the applicable business context, actor, and input for Campaign là chiến lược bán hàng. Landing Page là Business Asset",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-003-AC002",
      "given": "the applicable business context, actor, and input for Campaign là chiến lược bán hàng. Landing Page là Business Asset",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-003-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-003-O001",
      "obligation_text": "Campaign là chiến lược bán hàng"
    },
    {
      "acceptance_criterion_references": [
        "BD-06-003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-003-O002",
      "obligation_text": "Landing Page là Business Asset"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Campaign là chiến lược bán hàng. Landing Page là Business Asset.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Campaign",
    "source_context_sha256": "1524a66b1765e3841d30d3f29c295ca3da752ed5686bf451d5943adae8b0cfec",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "dd447a0600fc907c5ca7535bd3216e5b7a3ee5668d10783b35fed1b072deb3d0",
    "source_lines": "L480-L485",
    "source_section": "21. Business Decisions (Locked) > BD-06-003"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-003",
  "title": "Campaign là chiến lược bán hàng. Landing Page là Business Asset",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-004 — Landing Page thuộc Storefront. Một Landing Page có thể phục vụ nhiều Campaign

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-004-AC001",
      "given": "the applicable business context, actor, and input for Landing Page thuộc Storefront. Một Landing Page có thể phục vụ nhiều Campaign",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-004-AC002",
      "given": "the applicable business context, actor, and input for Landing Page thuộc Storefront. Một Landing Page có thể phục vụ nhiều Campaign",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-004-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-06-004-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Landing Page thuộc Storefront. Một Landing Page có thể phục vụ nhiều Campaign",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-06-004-O001",
        "BD-06-004-O002"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-004-AC001",
        "BD-06-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-004-O001",
      "obligation_text": "Landing Page thuộc Storefront"
    },
    {
      "acceptance_criterion_references": [
        "BD-06-004-AC002",
        "BD-06-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-004-O002",
      "obligation_text": "Một Landing Page có thể phục vụ nhiều Campaign"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Landing Page thuộc Storefront. Một Landing Page có thể phục vụ nhiều Campaign.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Landing Page",
    "source_context_sha256": "41d1fe46ed57d8d6b6de76667897be774d15bc82553d24a7bc2dfda4add73b6b",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "a90e04254a8d5a51e651ec4d0c9eac72342ce0caf613a45f1789856081fc9b80",
    "source_lines": "L488-L493",
    "source_section": "21. Business Decisions (Locked) > BD-06-004"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-004",
  "title": "Landing Page thuộc Storefront. Một Landing Page có thể phục vụ nhiều Campaign",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-005 — Reference QR là Business Object độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-06-005-AC001",
      "given": "a candidate Reference QR là Business Object độc lập record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-06-005-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-005-O001",
      "obligation_text": "Reference QR là Business Object độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference QR là Business Object độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Reference QR",
    "source_context_sha256": "d03b0444956171de0c3827bf7f5a9a82197e67aa86e71e110c5844fed1838211",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "9606e5cb2697db982ee70a8461dafc295d5139f3beaed5e48227b6e5a8e0c356",
    "source_lines": "L496-L499",
    "source_section": "21. Business Decisions (Locked) > BD-06-005"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-005",
  "title": "Reference QR là Business Object độc lập",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-006 — Promotion QR là Business Object độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-06-006-AC001",
      "given": "a candidate Promotion QR là Business Object độc lập record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-06-006-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-06-006-AC002",
      "given": "a Promotion QR là Business Object độc lập candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-06-006-O001"
      ],
      "when": "the candidate is validated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-006-AC001",
        "BD-06-006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-006-O001",
      "obligation_text": "Promotion QR là Business Object độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Promotion QR là Business Object độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-06-006",
    "source_context_sha256": "8e385d058633d190461c2dde56aa86c8839c38ccc4ae127125f754b62b227188",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "84dc23149ae49473a5689de85c8ede7d1cea3b790f6e7752e58e11355aed3424",
    "source_lines": "L502-L505",
    "source_section": "21. Business Decisions (Locked) > BD-06-006"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-006",
  "title": "Promotion QR là Business Object độc lập",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-007 — Tracking luôn gắn với User và Organization

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-007-AC001",
      "given": "the applicable business context, actor, and input for Tracking luôn gắn với User và Organization",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-007-O001",
      "obligation_text": "Tracking luôn gắn với User và Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Tracking luôn gắn với User và Organization.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-06-007",
    "source_context_sha256": "e922812df8ad5064b4acfd18194ad9cd349be6c356abff203f3b6cec669e8836",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "2cd95dbd5b7d05f2d83c3de053b03d8b4ff5b300e669c25ef24c4f729dfa6db1",
    "source_lines": "L508-L511",
    "source_section": "21. Business Decisions (Locked) > BD-06-007"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [
      "EP-06-004"
    ],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-007",
  "title": "Tracking luôn gắn với User và Organization",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-008 — Marketing Attribution là Business Object độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-06-008-AC001",
      "given": "a candidate Marketing Attribution là Business Object độc lập record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-06-008-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-008-O001",
      "obligation_text": "Marketing Attribution là Business Object độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Marketing Attribution là Business Object độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Marketing Attribution",
    "source_context_sha256": "8078fe61c2e520fe2f6d76cfdc6a4b7281723bc77dc40a7e12940d73981b5b13",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "4e170fa2a1794bfe5a4d1f0d4b2da31305180c5abedde51122edd6b514eebefc",
    "source_lines": "L514-L517",
    "source_section": "21. Business Decisions (Locked) > BD-06-008"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-008",
  "title": "Marketing Attribution là Business Object độc lập",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-009 — Promotion Rule chỉ hỗ trợ các điều kiện đã thống nhất trong Version 2.0

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-009-AC001",
      "given": "the applicable business context, actor, and input for Promotion Rule chỉ hỗ trợ các điều kiện đã thống nhất trong Version 2.0",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-009-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-06-009-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Promotion Rule chỉ hỗ trợ các điều kiện đã thống nhất trong Version 2.0",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-06-009-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-009-AC001",
        "BD-06-009-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-009-O001",
      "obligation_text": "Promotion Rule chỉ hỗ trợ các điều kiện đã thống nhất trong Version 2.0"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Promotion Rule chỉ hỗ trợ các điều kiện đã thống nhất trong Version 2.0.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-06-009",
    "source_context_sha256": "051f757971b59243d12dd2915db420cd2ce1b9eb81f70b4b3ea5ec254116c94d",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "d8d11515db7079fd4542fded720ceb92862b7522f1f4236f77ac182deadd73b1",
    "source_lines": "L520-L523",
    "source_section": "21. Business Decisions (Locked) > BD-06-009"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-009",
  "title": "Promotion Rule chỉ hỗ trợ các điều kiện đã thống nhất trong Version 2.0",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-010 — Coupon Eligibility là tính năng Optional

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-010-AC001",
      "given": "the applicable business context, actor, and input for Coupon Eligibility là tính năng Optional",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-010-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-010-O001",
      "obligation_text": "Coupon Eligibility là tính năng Optional"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Coupon Eligibility là tính năng Optional.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-06-010",
    "source_context_sha256": "4b51b94a0abfaae06b7375c294f7db4b86d5c3bbc02ba1b51c969c6a10137d77",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "64774f793b23fc17cb5c0f0a2a3a6aaabb6ecfbc57d2dcfa3bf6cf3f927d1280",
    "source_lines": "L526-L529",
    "source_section": "21. Business Decisions (Locked) > BD-06-010"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-010",
  "title": "Coupon Eligibility là tính năng Optional",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-011 — Promotion Funding thuộc Organization tạo Promotion

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-011-AC001",
      "given": "the applicable business context, actor, and input for Promotion Funding thuộc Organization tạo Promotion",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-06-011-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Promotion Funding thuộc Organization tạo Promotion",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-06-011-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-011-AC001",
        "BD-06-011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-011-O001",
      "obligation_text": "Promotion Funding thuộc Organization tạo Promotion"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-06-011 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-06-011 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-06-011 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-06-011 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-06-011-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-06-011 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Promotion Funding thuộc Organization tạo Promotion.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-06-011",
    "source_context_sha256": "1046d17cc8fd202133457cd54301a182b17c0391c8af5c9614b953d5e31d848b",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "a657ee3a4fa3d63d1137224f1ca6c51807ef908256df42a36c41cfbcf27a319f",
    "source_lines": "L532-L535",
    "source_section": "21. Business Decisions (Locked) > BD-06-011"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [
      "EP-06-005"
    ],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-011",
  "title": "Promotion Funding thuộc Organization tạo Promotion",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-012 — Chi phí Promotion luôn được ghi nhận vào chi phí Marketing của Funding Owner

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-012-AC001",
      "given": "the applicable business context, actor, and input for Chi phí Promotion luôn được ghi nhận vào chi phí Marketing của Funding Owner",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-012-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-06-012-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Chi phí Promotion luôn được ghi nhận vào chi phí Marketing của Funding Owner",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-06-012-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-012-AC001",
        "BD-06-012-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-012-O001",
      "obligation_text": "Chi phí Promotion luôn được ghi nhận vào chi phí Marketing của Funding Owner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-06-012 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-06-012 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-06-012 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-06-012 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-06-012-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-06-012 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Chi phí Promotion luôn được ghi nhận vào chi phí Marketing của Funding Owner.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-06-012",
    "source_context_sha256": "07d6768ea4f4b5fd828d179ada6f42cf7173dd355328d0c8d3b81f51e6092691",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "004f0406fcf51ad6c68c85d7c28ed306eb2455c88a208765235b3ffbc213b510",
    "source_lines": "L538-L541",
    "source_section": "21. Business Decisions (Locked) > BD-06-012"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-012",
  "title": "Chi phí Promotion luôn được ghi nhận vào chi phí Marketing của Funding Owner",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-013 — Promotion Engine hỗ trợ Stack Policy. Version 2.0 mặc định là Stackable

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-013-AC001",
      "given": "the applicable business context, actor, and input for Promotion Engine hỗ trợ Stack Policy. Version 2.0 mặc định là Stackable",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-013-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-013-AC002",
      "given": "the applicable business context, actor, and input for Promotion Engine hỗ trợ Stack Policy. Version 2.0 mặc định là Stackable",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-06-013-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-06-013-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Promotion Engine hỗ trợ Stack Policy. Version 2.0 mặc định là Stackable",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-06-013-O001",
        "BD-06-013-O002"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-013-AC001",
        "BD-06-013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-013-O001",
      "obligation_text": "Promotion Engine hỗ trợ Stack Policy"
    },
    {
      "acceptance_criterion_references": [
        "BD-06-013-AC002",
        "BD-06-013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-013-O002",
      "obligation_text": "Version 2.0 mặc định là Stackable"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Promotion Engine hỗ trợ Stack Policy. Version 2.0 mặc định là Stackable.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-06-013",
    "source_context_sha256": "2429ae63335a90416fa9de31b5af1b347791f57c10def75b6b432e874ce5a209",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "84130d0d767595ad363766d1fe3b6f43b5eedeb7caf77873e4cf994b9974ff6a",
    "source_lines": "L544-L549",
    "source_section": "21. Business Decisions (Locked) > BD-06-013"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-013",
  "title": "Promotion Engine hỗ trợ Stack Policy. Version 2.0 mặc định là Stackable",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-014 — Final Promotion Snapshot is created only after Payment Success

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-06-014-AC001",
      "given": "a candidate Final Promotion Snapshot is created only after Payment Success record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-06-014-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-06-014-AC002",
      "given": "a Final Promotion Snapshot is created only after Payment Success candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-06-014-O001"
      ],
      "when": "the candidate is validated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-014-AC001",
        "BD-06-014-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-014-O001",
      "obligation_text": "Final Promotion Snapshot is created only after Payment Success"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-06-014 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-06-014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-06-014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-06-014 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-06-014-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-06-014 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Final Promotion Snapshot is created only after Payment Success.",
  "provenance": {
    "approved_decisions": [
      "BDD-11",
      "BDD-12"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Promotion Snapshot",
    "source_context_sha256": "30804fdc122da7e85003455f019926575ee3931957b4cb9225106b5c0ee15c95",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "309f50cfb19e236658bb595f658503232e569adffa745aec51e205e97e3eca69",
    "source_lines": "L552-L555",
    "source_section": "21. Business Decisions (Locked) > BD-06-014"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [
      "EP-06-006"
    ],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-014",
  "title": "Final Promotion Snapshot is created only after Payment Success",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-015 — Sales Enablement là Domain độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-06-015-AC001",
      "given": "the applicable business context, actor, and input for Sales Enablement là Domain độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "BD-06-015-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-06-015-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Sales Enablement là Domain độc lập",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-06-015-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-06-015-AC001",
        "BD-06-015-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-015-O001",
      "obligation_text": "Sales Enablement là Domain độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sales Enablement là Domain độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-06-015",
    "source_context_sha256": "d55e3c8d29ab271ccafc955fca626b42230188319bd23b95a5932b8e18c1b754",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "e847a408a21738cf4c69cf0266c08c134e8404034f17b82048b2d3e7da75f7c2",
    "source_lines": "L558-L561",
    "source_section": "21. Business Decisions (Locked) > BD-06-015"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-06-015",
  "title": "Sales Enablement là Domain độc lập",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-016 — Referral, Loyalty, Bundle nhiều dịch vụ và AI Promotion được đưa vào Deferred Scope

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Referral, Loyalty, Bundle nhiều dịch vụ và AI Promotion được đưa vào Deferred Scope.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-06-016",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-06-016",
    "source_context_sha256": "fc4741096aa91612b0440169c8933ec342f379d926a3fad31fd03645bd32d11c",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "70596c7bbb9d1ecd07fabd0b9d4fefddb1622d22952ffd1ad82a272bc9ba70d3",
    "source_lines": "L564-L567",
    "source_section": "21. Business Decisions (Locked) > BD-06-016"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "DEFERRED",
  "stable_id": "BD-06-016",
  "title": "Referral, Loyalty, Bundle nhiều dịch vụ và AI Promotion được đưa vào Deferred Scope",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R001 — Sales Enablement không phải Marketing

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R001-AC001",
      "given": "the applicable business context, actor, and input for Sales Enablement không phải Marketing",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-06-R001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-06-R001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Sales Enablement không phải Marketing",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-06-R001-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R001-AC001",
        "BRD-WS-06-R001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R001-O001",
      "obligation_text": "Sales Enablement không phải Marketing"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sales Enablement không phải Marketing.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-001",
    "previous_temporary_key": "TMP-BRD-WS-06-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "Sales Enablement",
    "source_context_sha256": "26b80e593935945efdb831b7472ba2262349b8151d22c6b4a9c5e9c913292efd",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "304dab5262438979652550ee51caade026285cef61a5232586b2ce3ddc8411d0",
    "source_lines": "L86",
    "source_section": "3. Sales Enablement Domain > Sales Enablement"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R001",
  "title": "Sales Enablement không phải Marketing",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R002 — Bundle nhiều dịch vụ được giữ lại cho các phiên bản sau

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Bundle nhiều dịch vụ được giữ lại cho các phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-002",
    "previous_temporary_key": "TMP-BRD-WS-06-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Coupon",
    "source_context_sha256": "bc2c5583ae2948824f69049a0e3280b09e9d1d3d7e088cb0d39256e68a865c2a",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "0987f4d0e979b1e594435cc98aa63ce29ffcdf853682874f89b51df9f9e544ed",
    "source_lines": "L120",
    "source_section": "5. Coupon"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "FUTURE",
  "stable_id": "BRD-WS-06-R002",
  "title": "Bundle nhiều dịch vụ được giữ lại cho các phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R003 — Không cần tạo lại Coupon

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R003-AC001",
      "given": "the applicable business context, actor, and input for Không cần tạo lại Coupon",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-06-R003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R003-O001",
      "obligation_text": "Không cần tạo lại Coupon"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không cần tạo lại Coupon.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-003",
    "previous_temporary_key": "TMP-BRD-WS-06-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Coupon Inheritance",
    "source_context_sha256": "be151839578080f5353bc8d226d409dd2abcf64f41c9e37a171521497b7b356c",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
    "source_lines": "L151",
    "source_section": "6. Coupon Inheritance"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R003",
  "title": "Không cần tạo lại Coupon",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R004 — Campaign không phải Landing Page

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R004-AC001",
      "given": "the applicable business context, actor, and input for Campaign không phải Landing Page",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-06-R004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R004-O001",
      "obligation_text": "Campaign không phải Landing Page"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Campaign không phải Landing Page.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-004",
    "previous_temporary_key": "TMP-BRD-WS-06-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Campaign",
    "source_context_sha256": "1524a66b1765e3841d30d3f29c295ca3da752ed5686bf451d5943adae8b0cfec",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "20e23b2cb84047758a8466cf2d9c57fdeb2d66a614e143e54d87950b62170a9d",
    "source_lines": "L171",
    "source_section": "7. Campaign"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R004",
  "title": "Campaign không phải Landing Page",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R005 — Reference QR không phải: - Payment QR

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R005-AC001",
      "given": "the applicable business context, actor, and input for Reference QR không phải: - Payment QR",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-06-R005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-06-R005-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Reference QR không phải: - Payment QR",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-06-R005-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-06-R005-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Reference QR không phải: - Payment QR",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-06-R005-O001"
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
        "BRD-WS-06-R005-AC001",
        "BRD-WS-06-R005-AC002",
        "BRD-WS-06-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R005-O001",
      "obligation_text": "Reference QR không phải: - Payment QR"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-06-R005-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-06-R005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference QR không phải: - Payment QR",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-005",
    "previous_temporary_key": "TMP-BRD-WS-06-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Reference QR",
    "source_context_sha256": "d03b0444956171de0c3827bf7f5a9a82197e67aa86e71e110c5844fed1838211",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "0864b9d2c77582086492e08c726b21e4f2ddc146308c9e4af0bba1241a4733eb",
    "source_lines": "L195-L197",
    "source_section": "9. Reference QR"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R005",
  "title": "Reference QR không phải: - Payment QR",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R006 — Reference QR không phải: - eSIM QR

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R006-AC001",
      "given": "the applicable business context, actor, and input for Reference QR không phải: - eSIM QR",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-06-R006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R006-O001",
      "obligation_text": "Reference QR không phải: - eSIM QR"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference QR không phải: - eSIM QR",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-006",
    "previous_temporary_key": "TMP-BRD-WS-06-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Reference QR",
    "source_context_sha256": "d03b0444956171de0c3827bf7f5a9a82197e67aa86e71e110c5844fed1838211",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "5a978f967a95ccc94aab62b46a52897e8590ce0ff28f62dbceb17067fb39008a",
    "source_lines": "L195-L198",
    "source_section": "9. Reference QR"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R006",
  "title": "Reference QR không phải: - eSIM QR",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R007 — Reference QR luôn gắn Tracking ID

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R007-AC001",
      "given": "the applicable business context, actor, and input for Reference QR luôn gắn Tracking ID",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-06-R007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R007-O001",
      "obligation_text": "Reference QR luôn gắn Tracking ID"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference QR luôn gắn Tracking ID.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-007",
    "previous_temporary_key": "TMP-BRD-WS-06-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Reference QR",
    "source_context_sha256": "d03b0444956171de0c3827bf7f5a9a82197e67aa86e71e110c5844fed1838211",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "88815f92c8491c62edd9c9dce7ed0d4236521cc3d2e0ec14d27af0df6aad6e99",
    "source_lines": "L209",
    "source_section": "9. Reference QR"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R007",
  "title": "Reference QR luôn gắn Tracking ID",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R008 — Reference QR có thể lọc sẵn Product để Customer chỉ cần thanh toán

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R008-AC001",
      "given": "the applicable business context, actor, and input for Reference QR có thể lọc sẵn Product để Customer chỉ cần thanh toán",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-06-R008-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-06-R008-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Reference QR có thể lọc sẵn Product để Customer chỉ cần thanh toán",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-06-R008-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R008-AC001",
        "BRD-WS-06-R008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R008-O001",
      "obligation_text": "Reference QR có thể lọc sẵn Product để Customer chỉ cần thanh toán"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference QR có thể lọc sẵn Product để Customer chỉ cần thanh toán.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-008",
    "previous_temporary_key": "TMP-BRD-WS-06-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Reference QR",
    "source_context_sha256": "d03b0444956171de0c3827bf7f5a9a82197e67aa86e71e110c5844fed1838211",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "6f57018835e43ea7c17de23da748beea68d879dd7b42c40e2f53602bc643ae95",
    "source_lines": "L218",
    "source_section": "9. Reference QR"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R008",
  "title": "Reference QR có thể lọc sẵn Product để Customer chỉ cần thanh toán",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R009 — Tracking luôn gắn với User

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R009-AC001",
      "given": "the applicable business context, actor, and input for Tracking luôn gắn với User",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-06-R009-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R009-O001",
      "obligation_text": "Tracking luôn gắn với User"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Tracking luôn gắn với User.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-009",
    "previous_temporary_key": "TMP-BRD-WS-06-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Tracking",
    "source_context_sha256": "a519a092b71563d6479867e7ba338814902279588a3b6fda7ccd425718b39864",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "c0c7d4750b415ab5239769a59b1533448d1f961c2831ae8a71f1f66aa160b9db",
    "source_lines": "L247",
    "source_section": "11. Tracking"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R009",
  "title": "Tracking luôn gắn với User",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R010 — Một giao dịch cần Snapshot: - Storefront

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R010-AC001",
      "given": "a candidate Một giao dịch cần Snapshot: - Storefront record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-WS-06-R010-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-06-R010-AC002",
      "given": "a Một giao dịch cần Snapshot: - Storefront candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BRD-WS-06-R010-O001"
      ],
      "when": "the candidate is validated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R010-AC001",
        "BRD-WS-06-R010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R010-O001",
      "obligation_text": "Một giao dịch cần Snapshot: - Storefront"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một giao dịch cần Snapshot: - Storefront",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-010",
    "previous_temporary_key": "TMP-BRD-WS-06-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Marketing Attribution",
    "source_context_sha256": "8078fe61c2e520fe2f6d76cfdc6a4b7281723bc77dc40a7e12940d73981b5b13",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
    "source_lines": "L275-L277",
    "source_section": "12. Marketing Attribution"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R010",
  "title": "Một giao dịch cần Snapshot: - Storefront",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R011 — Một giao dịch cần Snapshot: - Landing Page

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R011-AC001",
      "given": "a candidate Một giao dịch cần Snapshot: - Landing Page record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-WS-06-R011-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R011-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R011-O001",
      "obligation_text": "Một giao dịch cần Snapshot: - Landing Page"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một giao dịch cần Snapshot: - Landing Page",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-011",
    "previous_temporary_key": "TMP-BRD-WS-06-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Marketing Attribution",
    "source_context_sha256": "8078fe61c2e520fe2f6d76cfdc6a4b7281723bc77dc40a7e12940d73981b5b13",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "d9cd326102941943ae94d0fd022ea9448ee4e2d571129573b7095d834447b707",
    "source_lines": "L275-L278",
    "source_section": "12. Marketing Attribution"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R011",
  "title": "Một giao dịch cần Snapshot: - Landing Page",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R012 — Một giao dịch cần Snapshot: - Campaign

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R012-AC001",
      "given": "a candidate Một giao dịch cần Snapshot: - Campaign record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-WS-06-R012-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R012-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R012-O001",
      "obligation_text": "Một giao dịch cần Snapshot: - Campaign"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một giao dịch cần Snapshot: - Campaign",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-012",
    "previous_temporary_key": "TMP-BRD-WS-06-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Marketing Attribution",
    "source_context_sha256": "8078fe61c2e520fe2f6d76cfdc6a4b7281723bc77dc40a7e12940d73981b5b13",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "31939f9b7dbddf810de0834d3daab570f60b8e601fdd0d403094f8ea7dc7d52a",
    "source_lines": "L275-L279",
    "source_section": "12. Marketing Attribution"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R012",
  "title": "Một giao dịch cần Snapshot: - Campaign",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R013 — Một giao dịch cần Snapshot: - Reference QR

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R013-AC001",
      "given": "a candidate Một giao dịch cần Snapshot: - Reference QR record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-WS-06-R013-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R013-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R013-O001",
      "obligation_text": "Một giao dịch cần Snapshot: - Reference QR"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một giao dịch cần Snapshot: - Reference QR",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-013",
    "previous_temporary_key": "TMP-BRD-WS-06-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Marketing Attribution",
    "source_context_sha256": "8078fe61c2e520fe2f6d76cfdc6a4b7281723bc77dc40a7e12940d73981b5b13",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "b7115a7d98c8ecd9bfb4d63502fb46d7d9d6761c32c91182a0d4f32c84c3a8dd",
    "source_lines": "L275-L280",
    "source_section": "12. Marketing Attribution"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R013",
  "title": "Một giao dịch cần Snapshot: - Reference QR",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R014 — Một giao dịch cần Snapshot: - Tracking ID

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R014-AC001",
      "given": "a candidate Một giao dịch cần Snapshot: - Tracking ID record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-WS-06-R014-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R014-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R014-O001",
      "obligation_text": "Một giao dịch cần Snapshot: - Tracking ID"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một giao dịch cần Snapshot: - Tracking ID",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-014",
    "previous_temporary_key": "TMP-BRD-WS-06-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Marketing Attribution",
    "source_context_sha256": "8078fe61c2e520fe2f6d76cfdc6a4b7281723bc77dc40a7e12940d73981b5b13",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "e2d22b775b805ab3efa27d857e70efdbc8a426c8207842869eac50e6346e4246",
    "source_lines": "L275-L281",
    "source_section": "12. Marketing Attribution"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R014",
  "title": "Một giao dịch cần Snapshot: - Tracking ID",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R015 — Một giao dịch cần Snapshot: - Sales User

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R015-AC001",
      "given": "a candidate Một giao dịch cần Snapshot: - Sales User record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-WS-06-R015-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-06-R015-AC002",
      "given": "a Một giao dịch cần Snapshot: - Sales User candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BRD-WS-06-R015-O001"
      ],
      "when": "the candidate is validated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R015-AC001",
        "BRD-WS-06-R015-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R015-O001",
      "obligation_text": "Một giao dịch cần Snapshot: - Sales User"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một giao dịch cần Snapshot: - Sales User",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-015",
    "previous_temporary_key": "TMP-BRD-WS-06-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Marketing Attribution",
    "source_context_sha256": "8078fe61c2e520fe2f6d76cfdc6a4b7281723bc77dc40a7e12940d73981b5b13",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "cc4fce92d61bbfda1493876ad3c6a288e48d4efe56ddcf73fcdadaa3fe4284a8",
    "source_lines": "L275-L282",
    "source_section": "12. Marketing Attribution"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R015",
  "title": "Một giao dịch cần Snapshot: - Sales User",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R016 — Một giao dịch cần Snapshot: - Organization

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R016-AC001",
      "given": "a candidate Một giao dịch cần Snapshot: - Organization record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-WS-06-R016-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R016-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R016-O001",
      "obligation_text": "Một giao dịch cần Snapshot: - Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một giao dịch cần Snapshot: - Organization",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-016",
    "previous_temporary_key": "TMP-BRD-WS-06-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Marketing Attribution",
    "source_context_sha256": "8078fe61c2e520fe2f6d76cfdc6a4b7281723bc77dc40a7e12940d73981b5b13",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "2994972beecfa4005c79a04fee92b861d482b9083fcdb5b8753839a8ad5a6a96",
    "source_lines": "L275-L283",
    "source_section": "12. Marketing Attribution"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R016",
  "title": "Một giao dịch cần Snapshot: - Organization",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R017 — Một giao dịch cần Snapshot: - Distribution Path

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R017-AC001",
      "given": "a candidate Một giao dịch cần Snapshot: - Distribution Path record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-WS-06-R017-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R017-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R017-O001",
      "obligation_text": "Một giao dịch cần Snapshot: - Distribution Path"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một giao dịch cần Snapshot: - Distribution Path",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-017",
    "previous_temporary_key": "TMP-BRD-WS-06-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Marketing Attribution",
    "source_context_sha256": "8078fe61c2e520fe2f6d76cfdc6a4b7281723bc77dc40a7e12940d73981b5b13",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "e4791748a8bd42ad125ab43c67a56c30af692e4e99a6e020bf9b487da99fb331",
    "source_lines": "L275-L284",
    "source_section": "12. Marketing Attribution"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R017",
  "title": "Một giao dịch cần Snapshot: - Distribution Path",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R018 — Các Rule nâng cao sẽ triển khai ở phiên bản sau

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Các Rule nâng cao sẽ triển khai ở phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-018",
    "previous_temporary_key": "TMP-BRD-WS-06-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Promotion Rule",
    "source_context_sha256": "bd4eea248e3c2ac9b884e76bc833ebb9d092cf2561b9ccf632589b742a0de787",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "dbff92cc7c6f6a3585214a02e7166c5b5ab7c696775b72b92d604c265b46186c",
    "source_lines": "L311",
    "source_section": "13. Promotion Rule"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "FUTURE",
  "stable_id": "BRD-WS-06-R018",
  "title": "Các Rule nâng cao sẽ triển khai ở phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R019 — Mỗi Promotion phải có Funding Owner

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R019-AC001",
      "given": "the applicable business context, actor, and input for Mỗi Promotion phải có Funding Owner",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-06-R019-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-06-R019-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Mỗi Promotion phải có Funding Owner",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-06-R019-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R019-AC001",
        "BRD-WS-06-R019-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R019-O001",
      "obligation_text": "Mỗi Promotion phải có Funding Owner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R019 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R019 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R019 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R019 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-06-R019-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R019 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Promotion phải có Funding Owner.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-019",
    "previous_temporary_key": "TMP-BRD-WS-06-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Promotion Funding",
    "source_context_sha256": "dfcb5d481c877f331e8f60db23bab28b1745dcf797e799d13a7a1847adcb91f5",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "8291619a7a45c192eb1ebfb3a889237f50dfc3800cb53b38d09001b2f829ce7f",
    "source_lines": "L357",
    "source_section": "16. Promotion Funding"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R019",
  "title": "Mỗi Promotion phải có Funding Owner",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R020 — Chi phí Promotion luôn được tính vào chi phí Marketing của Funding Owner

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-06-R020-AC001",
      "given": "the applicable business context, actor, and input for Chi phí Promotion luôn được tính vào chi phí Marketing của Funding Owner",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-06-R020-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-06-R020-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Chi phí Promotion luôn được tính vào chi phí Marketing của Funding Owner",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-06-R020-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-06-R020-AC001",
        "BRD-WS-06-R020-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R020-O001",
      "obligation_text": "Chi phí Promotion luôn được tính vào chi phí Marketing của Funding Owner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R020 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R020 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R020 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R020 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-06-R020-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-06-R020 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Chi phí Promotion luôn được tính vào chi phí Marketing của Funding Owner.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-020",
    "previous_temporary_key": "TMP-BRD-WS-06-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Promotion Funding",
    "source_context_sha256": "dfcb5d481c877f331e8f60db23bab28b1745dcf797e799d13a7a1847adcb91f5",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "509709ecd37f0c6c750670401fd1f3e9b653c2407f0929474b2f5b66c2e97eec",
    "source_lines": "L368",
    "source_section": "16. Promotion Funding"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-06-R020",
  "title": "Chi phí Promotion luôn được tính vào chi phí Marketing của Funding Owner",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R021 — Các công cụ khác sẽ mở rộng trong các phiên bản sau

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Các công cụ khác sẽ mở rộng trong các phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-021",
    "previous_temporary_key": "TMP-BRD-WS-06-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Sales Tool",
    "source_context_sha256": "787a0c0b991f2bb6bd5d4ebf5668adc0315b164567f3be6523bddfda6d48be2a",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "bd6edbb3d92e3ee3fe0f709088ed9153c54d150739a5409c44add6151936a5c6",
    "source_lines": "L446",
    "source_section": "19. Sales Tool"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "FUTURE",
  "stable_id": "BRD-WS-06-R021",
  "title": "Các công cụ khác sẽ mở rộng trong các phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R022 — Chưa triển khai trong Version 2.0: - Loyalty

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Chưa triển khai trong Version 2.0: - Loyalty",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-022",
    "previous_temporary_key": "TMP-BRD-WS-06-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Deferred Scope",
    "source_context_sha256": "30e934bd6f802193707e9c11724f025d5a99dce619adbde905fce72c1da930eb",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "48fbfd4368bb3499e3810519d29be5255138dce4ad5f4c015d335da5bf831941",
    "source_lines": "L452-L454",
    "source_section": "20. Deferred Scope"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-06-R022",
  "title": "Chưa triển khai trong Version 2.0: - Loyalty",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R023 — Chưa triển khai trong Version 2.0: - Membership

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Chưa triển khai trong Version 2.0: - Membership",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-023",
    "previous_temporary_key": "TMP-BRD-WS-06-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Deferred Scope",
    "source_context_sha256": "30e934bd6f802193707e9c11724f025d5a99dce619adbde905fce72c1da930eb",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "45838b4da009fa47fafdf0b556f4d94a261a5a5d45dd92d0ce37e1504e973cc6",
    "source_lines": "L452-L455",
    "source_section": "20. Deferred Scope"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-06-R023",
  "title": "Chưa triển khai trong Version 2.0: - Membership",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R024 — Chưa triển khai trong Version 2.0: - Referral Program

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Chưa triển khai trong Version 2.0: - Referral Program",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-024",
    "previous_temporary_key": "TMP-BRD-WS-06-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Deferred Scope",
    "source_context_sha256": "30e934bd6f802193707e9c11724f025d5a99dce619adbde905fce72c1da930eb",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "8dff6c007927f4477ae4b3de6515b12cfc60e19b1efa7d3bc07f7ccfbdfe8538",
    "source_lines": "L452-L456",
    "source_section": "20. Deferred Scope"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-06-R024",
  "title": "Chưa triển khai trong Version 2.0: - Referral Program",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R025 — Chưa triển khai trong Version 2.0: - Bundle nhiều dịch vụ

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Chưa triển khai trong Version 2.0: - Bundle nhiều dịch vụ",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-025",
    "previous_temporary_key": "TMP-BRD-WS-06-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Deferred Scope",
    "source_context_sha256": "30e934bd6f802193707e9c11724f025d5a99dce619adbde905fce72c1da930eb",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "f887ca7ea2ebb51198029be07bb963b0d744246aa6e58e399c5d921f96ce1e48",
    "source_lines": "L452-L457",
    "source_section": "20. Deferred Scope"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-06-R025",
  "title": "Chưa triển khai trong Version 2.0: - Bundle nhiều dịch vụ",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R026 — Chưa triển khai trong Version 2.0: - AI Promotion

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Chưa triển khai trong Version 2.0: - AI Promotion",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-026",
    "previous_temporary_key": "TMP-BRD-WS-06-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Deferred Scope",
    "source_context_sha256": "30e934bd6f802193707e9c11724f025d5a99dce619adbde905fce72c1da930eb",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "c56d4e80a62da5532fea84ef01ec67caf8d022e51d1028bedda7a1a2d387cf58",
    "source_lines": "L452-L458",
    "source_section": "20. Deferred Scope"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-06-R026",
  "title": "Chưa triển khai trong Version 2.0: - AI Promotion",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R027 — Chưa triển khai trong Version 2.0: - AI Recommendation

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Chưa triển khai trong Version 2.0: - AI Recommendation",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-027",
    "previous_temporary_key": "TMP-BRD-WS-06-027",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Deferred Scope",
    "source_context_sha256": "30e934bd6f802193707e9c11724f025d5a99dce619adbde905fce72c1da930eb",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "a6f958238b7614e30e4b59d2c0f1c4ab1585b0f54b12a15f967311b3903586ce",
    "source_lines": "L452-L459",
    "source_section": "20. Deferred Scope"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-06-R027",
  "title": "Chưa triển khai trong Version 2.0: - AI Recommendation",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-06-R028 — Chưa triển khai trong Version 2.0: - Social Campaign

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Chưa triển khai trong Version 2.0: - Social Campaign",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-06-028",
    "previous_temporary_key": "TMP-BRD-WS-06-028",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Deferred Scope",
    "source_context_sha256": "30e934bd6f802193707e9c11724f025d5a99dce619adbde905fce72c1da930eb",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "b2f70541494f987a7309b79d2d3e59e859f3eea16bd180d9bfbe43d45b9ea96f",
    "source_lines": "L452-L460",
    "source_section": "20. Deferred Scope"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "DEFERRED",
  "stable_id": "BRD-WS-06-R028",
  "title": "Chưa triển khai trong Version 2.0: - Social Campaign",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-06-001 — Sales Enablement là Domain độc lập với Product Domain và Commercial Domain

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-06-001-AC001",
      "given": "the applicable business context, actor, and input for Sales Enablement là Domain độc lập với Product Domain và Commercial Domain",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "EP-06-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-06-001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Sales Enablement là Domain độc lập với Product Domain và Commercial Domain",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-06-001-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-06-001-AC001",
        "EP-06-001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-06-001-O001",
      "obligation_text": "Sales Enablement là Domain độc lập với Product Domain và Commercial Domain"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sales Enablement là Domain độc lập với Product Domain và Commercial Domain.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-06-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-06-001",
    "source_context_sha256": "56f646d90930158ed838db05f8c3239a8fd07a7652e0956c3e7d377c02e536dc",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "fdba03892b4f3c51174ffd73ebdf777841988cb7dcf324ac32d086e0c7557d9e",
    "source_lines": "L617-L620",
    "source_section": "23. Enterprise Design Principles > EP-06-001"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-06-001",
  "title": "Sales Enablement là Domain độc lập với Product Domain và Commercial Domain",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-06-002 — Landing Page là Business Asset. Không thuộc Campaign

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-06-002-AC001",
      "given": "the applicable business context, actor, and input for Landing Page là Business Asset. Không thuộc Campaign",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-06-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-06-002-AC002",
      "given": "the applicable business context, actor, and input for Landing Page là Business Asset. Không thuộc Campaign",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-06-002-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-06-002-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-06-002-O001",
      "obligation_text": "Landing Page là Business Asset"
    },
    {
      "acceptance_criterion_references": [
        "EP-06-002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-06-002-O002",
      "obligation_text": "Không thuộc Campaign"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Landing Page là Business Asset. Không thuộc Campaign.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-06-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-06-003",
    "source_context_sha256": "c3b614ffb40c96d17595abaedced8c76093c8b210ceec8454f0c120e69b69f06",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "2ee8cebfa12b402b013f471dd364e7fb765e5c96b84206188ad099b79bc11516",
    "source_lines": "L623-L628",
    "source_section": "23. Enterprise Design Principles > EP-06-002"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-06-002",
  "title": "Landing Page là Business Asset. Không thuộc Campaign",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-06-003 — Reference QR, Promotion QR, Payment QR và eSIM QR là bốn Business Object độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "EP-06-003-AC001",
      "given": "a candidate Reference QR, Promotion QR, Payment QR và eSIM QR là bốn Business Object độc lập record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "EP-06-003-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "EP-06-003-AC002",
      "given": "a Reference QR, Promotion QR, Payment QR và eSIM QR là bốn Business Object độc lập candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "EP-06-003-O001"
      ],
      "when": "the candidate is validated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-06-003-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Reference QR, Promotion QR, Payment QR và eSIM QR là bốn Business Object độc lập",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-06-003-O001"
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
        "EP-06-003-AC001",
        "EP-06-003-AC002",
        "EP-06-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-06-003-O001",
      "obligation_text": "Reference QR, Promotion QR, Payment QR và eSIM QR là bốn Business Object độc lập"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-06-003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-06-003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-06-003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-06-003-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-06-003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-06-003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference QR, Promotion QR, Payment QR và eSIM QR là bốn Business Object độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-06-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-06-003",
    "source_context_sha256": "765b40b4a7f877d55af4b8f672a1c4a3878f9573404580ac6b5b86e086b03ecb",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "82c75c0450e9e40748e99b3a0400a434b9cfd1e3b3633d696e111c4446d54a5c",
    "source_lines": "L631-L634",
    "source_section": "23. Enterprise Design Principles > EP-06-003"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-06-003",
  "title": "Reference QR, Promotion QR, Payment QR và eSIM QR là bốn Business Object độc lập",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-06-004 — Tracking luôn gắn với User và Organization

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Alias evidence is inherited from the canonical target; the alias is not an acceptance unit.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Tracking luôn gắn với User và Organization.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-06-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-06-007",
    "source_context_sha256": "e922812df8ad5064b4acfd18194ad9cd349be6c356abff203f3b6cec669e8836",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "ce2aabce3e3902ec4c389fc9700b0ea3507d0684763878b6d5c9c9b1043d6f1d",
    "source_lines": "L637-L640",
    "source_section": "23. Enterprise Design Principles > EP-06-004"
  },
  "record_kind": "ALIAS",
  "relationships": {
    "alias_of": "BD-06-007",
    "aliases": [],
    "coverage_mode": "CANONICAL",
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-06-004",
  "title": "Tracking luôn gắn với User và Organization",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-06-005 — Promotion Funding luôn thuộc Organization tạo Promotion

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Alias evidence is inherited from the canonical target; the alias is not an acceptance unit.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Promotion Funding luôn thuộc Organization tạo Promotion.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-06-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-06-005",
    "source_context_sha256": "29080702dd348ff44063e920c03cb42c7780716303f47ecb03732ddb9e14b545",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "7e408df558c7bab659b485c2469ca545d6831fbaf2d0ba69ace55ea62d16f20f",
    "source_lines": "L643-L646",
    "source_section": "23. Enterprise Design Principles > EP-06-005"
  },
  "record_kind": "ALIAS",
  "relationships": {
    "alias_of": "BD-06-011",
    "aliases": [],
    "coverage_mode": "CANONICAL",
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-06-005",
  "title": "Promotion Funding luôn thuộc Organization tạo Promotion",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-06-006 — Promotion Snapshot chỉ được tạo sau Payment Success

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Alias evidence is inherited from the canonical target; the alias is not an acceptance unit.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Promotion Snapshot chỉ được tạo sau Payment Success.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-06-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-06-006",
    "source_context_sha256": "0c3b475a9e0fd5a779bf6ea939387e8cea78a91b275609a82aece459fb4a1c70",
    "source_document": "docs/BRD/BRD-WS-06.md",
    "source_fingerprint": "ac475ed75608037a566b4ce42b204ce5a2b3236e9ccae1bd4c3e476eddb47de3",
    "source_lines": "L649-L652",
    "source_section": "23. Enterprise Design Principles > EP-06-006"
  },
  "record_kind": "ALIAS",
  "relationships": {
    "alias_of": "BD-06-014",
    "aliases": [],
    "coverage_mode": "CANONICAL",
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-06-006",
  "title": "Promotion Snapshot chỉ được tạo sau Payment Success",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
