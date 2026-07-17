---
document_code: "BRD-WS-06"
document_id: "BRD-WS-06"
title: "Promotion, Coupon, Campaign & Sales Enablement"
version: "2.3.0-draft.3"
document_revision: "2.3.0-draft.3"
status: "V2.3_DRAFT"
lifecycle_status: "V2.3_DRAFT"
language: "vi-VN"
baseline: "2.3"
product_baseline: "2.3"
source_lineage: "v2.2 + approved Phase 1/2A/2B + accepted Acceptance Model C1 + accepted Mapping C3"
source_baseline: "v2.2"
last_reviewed_date: "2026-07-15"
last_remediated_on: "2026-07-17"
applicable_scope: "V2.3_ACTIVE_AND_RETAINED_SCOPE_RECORDS"
generated_registry_role: "BRD_CANONICAL_SOURCE"
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

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-06-001 — Promotion thuộc Organization

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
      "requirement_id": "BD-06-001",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "e7e92e12fbbdf1af7c2a808e5e33ec7493ef0a182168d0db69163235fdf8fc7e"
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
        "BD-06-001-AC001",
        "BD-06-001-AC002",
        "BD-06-001-AC003"
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
    "source_fingerprint": "e7e92e12fbbdf1af7c2a808e5e33ec7493ef0a182168d0db69163235fdf8fc7e",
    "source_lines": "L722-L797",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-002",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "dd33f6c1877a16d6aef5f87e018b5eb3c85d2ffce8d0f3de8f0e302966a8eaac"
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
        "BD-06-002-AC001",
        "BD-06-002-AC002",
        "BD-06-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-002-O001",
      "obligation_text": "Coupon thuộc Price Book Owner và hỗ trợ kế thừa theo Distribution Network"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-002 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-06-002-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-06-002-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-002 does not define a recovery obligation."
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
    "source_fingerprint": "dd33f6c1877a16d6aef5f87e018b5eb3c85d2ffce8d0f3de8f0e302966a8eaac",
    "source_lines": "L799-L907",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-003",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "61c7a4cce4beebe26daf1689797a394103340602b24bde204871d320a837390b"
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
        "BD-06-003-AC001",
        "BD-06-003-AC003",
        "BD-06-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-003-O001",
      "obligation_text": "Campaign là chiến lược bán hàng"
    },
    {
      "acceptance_criterion_references": [
        "BD-06-003-AC002",
        "BD-06-003-AC003",
        "BD-06-003-AC004"
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
    "source_fingerprint": "61c7a4cce4beebe26daf1689797a394103340602b24bde204871d320a837390b",
    "source_lines": "L909-L994",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-004",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "1b3146e4cfe5993f7fb97af7a9f4e5013adae5ec4afc0ed6b200dbfcf39100da"
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
        "BD-06-004-AC001",
        "BD-06-004-AC003",
        "BD-06-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-004-O001",
      "obligation_text": "Landing Page thuộc Storefront"
    },
    {
      "acceptance_criterion_references": [
        "BD-06-004-AC002",
        "BD-06-004-AC003",
        "BD-06-004-AC004"
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
    "source_fingerprint": "1b3146e4cfe5993f7fb97af7a9f4e5013adae5ec4afc0ed6b200dbfcf39100da",
    "source_lines": "L996-L1081",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-005",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "e712b2777a6c0c69b0464a47cb36c6c7e6589fca3a274de125440fb1b6dab1aa"
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
        "BD-06-005-AC001",
        "BD-06-005-AC002",
        "BD-06-005-AC003"
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
    "source_fingerprint": "e712b2777a6c0c69b0464a47cb36c6c7e6589fca3a274de125440fb1b6dab1aa",
    "source_lines": "L1083-L1158",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-006",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "df8360c5cdd0cd8f05168a9df60d2620bffd4bc45f0331ca635dbaddba38c0e1"
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
        "BD-06-006-AC001",
        "BD-06-006-AC002",
        "BD-06-006-AC003"
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
    "source_fingerprint": "df8360c5cdd0cd8f05168a9df60d2620bffd4bc45f0331ca635dbaddba38c0e1",
    "source_lines": "L1160-L1235",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-006"
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
      "requirement_id": "BD-06-007",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "92def6b8d901bb3025f6729b02ba67f9d952a1b1f3133e07008980ebbbcafa68"
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
        "BD-06-007-AC001",
        "BD-06-007-AC002",
        "BD-06-007-AC003"
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
    "source_fingerprint": "92def6b8d901bb3025f6729b02ba67f9d952a1b1f3133e07008980ebbbcafa68",
    "source_lines": "L1237-L1318",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-008",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "ed1d08f19932cd4284f25a11a5c854c787de75748b51620cdd289772a4739495"
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
        "BD-06-008-AC001",
        "BD-06-008-AC002",
        "BD-06-008-AC003"
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
    "source_fingerprint": "ed1d08f19932cd4284f25a11a5c854c787de75748b51620cdd289772a4739495",
    "source_lines": "L1320-L1395",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-009",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "07384ed0062c5920d648d034f0676ff881039d8cd36a55d26621d8451bafcc5d"
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
        "BD-06-009-AC001",
        "BD-06-009-AC002",
        "BD-06-009-AC003"
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
    "source_fingerprint": "07384ed0062c5920d648d034f0676ff881039d8cd36a55d26621d8451bafcc5d",
    "source_lines": "L1397-L1472",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-010",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "84ade1dbd175cfcc0c8f2e6c3469c97ceac026380d261adc682d3928e0c7a80a"
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
        "BD-06-010-AC001",
        "BD-06-010-AC002",
        "BD-06-010-AC003"
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
    "source_fingerprint": "84ade1dbd175cfcc0c8f2e6c3469c97ceac026380d261adc682d3928e0c7a80a",
    "source_lines": "L1474-L1549",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-011",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "aede4ed090e0b68bda8d0360d5790f928d6d931ab46e96bbae40e5e9c4c416b6"
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
        "BD-06-011-AC001",
        "BD-06-011-AC002",
        "BD-06-011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-011-O001",
      "obligation_text": "Promotion Funding thuộc Organization tạo Promotion"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-011 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-011 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-011 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-06-011-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-06-011-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-011 does not define a recovery obligation."
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
    "source_fingerprint": "aede4ed090e0b68bda8d0360d5790f928d6d931ab46e96bbae40e5e9c4c416b6",
    "source_lines": "L1551-L1661",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-011"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-012",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "fe61973ced75b8f880419aec650a96013fc31a37a3040a9be7eeea9cd1354c1d"
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
        "BD-06-012-AC001",
        "BD-06-012-AC002",
        "BD-06-012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-012-O001",
      "obligation_text": "Chi phí Promotion luôn được ghi nhận vào chi phí Marketing của Funding Owner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-012 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-012 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-012 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-06-012-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-06-012-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-012 does not define a recovery obligation."
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
    "source_fingerprint": "fe61973ced75b8f880419aec650a96013fc31a37a3040a9be7eeea9cd1354c1d",
    "source_lines": "L1663-L1771",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-012"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-013",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "605f261a46fb35afdad42d43b6b0a01a7b8e7d44e8f4e0abe84f91ff4c5e2a88"
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
        "BD-06-013-AC001",
        "BD-06-013-AC003",
        "BD-06-013-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-013-O001",
      "obligation_text": "Promotion Engine hỗ trợ Stack Policy"
    },
    {
      "acceptance_criterion_references": [
        "BD-06-013-AC002",
        "BD-06-013-AC003",
        "BD-06-013-AC004"
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
    "source_fingerprint": "605f261a46fb35afdad42d43b6b0a01a7b8e7d44e8f4e0abe84f91ff4c5e2a88",
    "source_lines": "L1773-L1858",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-013"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-11",
        "BDD-12"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-014",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "c44bc81e427ce2097cb6eab7face0a6ea4e2dfe4e85b1d3d864e9acb52e87c13"
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
        "BD-06-014-AC001",
        "BD-06-014-AC002",
        "BD-06-014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-06-014-O001",
      "obligation_text": "Final Promotion Snapshot is created only after Payment Success"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-014 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-06-014-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-06-014-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-06-014 does not define a recovery obligation."
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
    "source_fingerprint": "c44bc81e427ce2097cb6eab7face0a6ea4e2dfe4e85b1d3d864e9acb52e87c13",
    "source_lines": "L1860-L1976",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-014"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-06-015",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "4e75bf035e9b96f889e883220c4d3e8352d4aaecfdeb26fcf70ab7b6cee6f119"
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
        "BD-06-015-AC001",
        "BD-06-015-AC002",
        "BD-06-015-AC003"
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
    "source_fingerprint": "4e75bf035e9b96f889e883220c4d3e8352d4aaecfdeb26fcf70ab7b6cee6f119",
    "source_lines": "L1978-L2053",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-015"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BD-06-016",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_fingerprint": "d06e12869ccd18d9659b71a546847272fde797bfd304a35b46a89b00d45a0002",
    "source_lines": "L2055-L2113",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-06-016"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R001",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "304dab5262438979652550ee51caade026285cef61a5232586b2ce3ddc8411d0"
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
        "BRD-WS-06-R001-AC001",
        "BRD-WS-06-R001-AC002",
        "BRD-WS-06-R001-AC003"
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
    "source_lines": "L2115-L2190",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-06-R002",
    "scope_status": "FUTURE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_lines": "L2192-L2250",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R002"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "A new Coupon is required when identity or applicability differs"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-06-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                "source_type": "SOURCE_LITERAL",
                "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
              },
              "identifier": "BRD-WS-06-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                "source_lines": "L151",
                "source_section": "6. Coupon Inheritance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-06.md",
            "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
            "source_lines": "L151",
            "source_section": "6. Coupon Inheritance"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-06-R003.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                "source_type": "SOURCE_LITERAL",
                "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
              },
              "identifier": "BRD-WS-06-R003.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                "source_lines": "L151",
                "source_section": "6. Coupon Inheritance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-06.md",
            "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
            "source_lines": "L151",
            "source_section": "6. Coupon Inheritance"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
            "source_type": "SOURCE_LITERAL",
            "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
          },
          "identifier": "BRD-WS-06-R003.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-06.md",
            "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
            "source_lines": "L151",
            "source_section": "6. Coupon Inheritance"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
            "source_type": "SOURCE_LITERAL",
            "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
          },
          "identifier": "BRD-WS-06-R003.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-06.md",
            "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
            "source_lines": "L151",
            "source_section": "6. Coupon Inheritance"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
            "source_type": "SOURCE_LITERAL",
            "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
          },
          "identifier": "BRD-WS-06-R003.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-06.md",
            "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
            "source_lines": "L151",
            "source_section": "6. Coupon Inheritance"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
            "source_type": "SOURCE_LITERAL",
            "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
          },
          "identifier": "BRD-WS-06-R003.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-06.md",
            "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
            "source_lines": "L151",
            "source_section": "6. Coupon Inheritance"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
            "source_type": "SOURCE_LITERAL",
            "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
          },
          "identifier": "BRD-WS-06-R003.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-06.md",
            "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
            "source_lines": "L151",
            "source_section": "6. Coupon Inheritance"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-06-R003",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "A duplicate Coupon is created solely for the same applicable reuse"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID"
    ],
    "positive_oracle": [
      "The existing Coupon is reused without creating a duplicate Coupon"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
      "source_lines": "L151",
      "source_section": "6. Coupon Inheritance"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
          "source_type": "SOURCE_LITERAL",
          "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
        },
        "identifier": "BRD-WS-06-R003.BRD-WS-06-R003.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-06-R003.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-06.md",
          "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
          "source_lines": "L151",
          "source_section": "6. Coupon Inheritance"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-06-R003.BRD-WS-06-R003.BRD-WS-06-R003.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-06-R003.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.COUPON_ID",
        "FIELD.REUSE_CONTEXT",
        "FIELD.LIFECYCLE_STATE",
        "FIELD.APPLICABILITY_RESULT",
        "FIELD.CREATED_COUPON_IDS"
      ],
      "producer": "BRD-WS-06-R003.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-06-R003.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.COUPON_ID",
        "FIELD.REUSE_CONTEXT",
        "FIELD.LIFECYCLE_STATE",
        "FIELD.APPLICABILITY_RESULT",
        "FIELD.CREATED_COUPON_IDS"
      ],
      "required_values_or_hashes": [
        "BRD-WS-06-R003.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-06-R003.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-06-R003.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-06-R003-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID",
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
              "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
              "source_type": "SOURCE_LITERAL",
              "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
            },
            "identifier": "BRD-WS-06-R003.BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-06.md",
              "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
              "source_lines": "L151",
              "source_section": "6. Coupon Inheritance"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-06-R003.BRD-WS-06-R003.BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
              "source_type": "SOURCE_LITERAL",
              "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
            },
            "identifier": "BRD-WS-06-R003.BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-06.md",
              "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
              "source_lines": "L151",
              "source_section": "6. Coupon Inheritance"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                        "BRD-WS-06-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
                    },
                    "identifier": "BRD-WS-06-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-06.md",
                      "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                      "source_lines": "L151",
                      "source_section": "6. Coupon Inheritance"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                  "source_lines": "L151",
                  "source_section": "6. Coupon Inheritance"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-06-R003.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
                    },
                    "identifier": "BRD-WS-06-R003.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-06.md",
                      "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                      "source_lines": "L151",
                      "source_section": "6. Coupon Inheritance"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                  "source_lines": "L151",
                  "source_section": "6. Coupon Inheritance"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
                },
                "identifier": "BRD-WS-06-R003.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                  "source_lines": "L151",
                  "source_section": "6. Coupon Inheritance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
                },
                "identifier": "BRD-WS-06-R003.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                  "source_lines": "L151",
                  "source_section": "6. Coupon Inheritance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
                },
                "identifier": "BRD-WS-06-R003.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                  "source_lines": "L151",
                  "source_section": "6. Coupon Inheritance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
                },
                "identifier": "BRD-WS-06-R003.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                  "source_lines": "L151",
                  "source_section": "6. Coupon Inheritance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
                },
                "identifier": "BRD-WS-06-R003.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                  "source_lines": "L151",
                  "source_section": "6. Coupon Inheritance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
                },
                "identifier": "BRD-WS-06-R003.BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                  "source_lines": "L151",
                  "source_section": "6. Coupon Inheritance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
                },
                "identifier": "BRD-WS-06-R003.BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                  "source_lines": "L151",
                  "source_section": "6. Coupon Inheritance"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-06-R003.BRD-WS-06-R003.BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                "source_type": "SOURCE_LITERAL",
                "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
              },
              "identifier": "BRD-WS-06-R003.BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                "source_lines": "L151",
                "source_section": "6. Coupon Inheritance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-06-R003.BRD-WS-06-R003.BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "BRD-WS-06-R003-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
              "source_type": "SOURCE_LITERAL",
              "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
            },
            "identifier": "BRD-WS-06-R003.BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-06.md",
              "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
              "source_lines": "L151",
              "source_section": "6. Coupon Inheritance"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.BRD-WS-06-R003.BRD-WS-06-R003.BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                      "BRD-WS-06-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
                  },
                  "identifier": "BRD-WS-06-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-06.md",
                    "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                    "source_lines": "L151",
                    "source_section": "6. Coupon Inheritance"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                "source_lines": "L151",
                "source_section": "6. Coupon Inheritance"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-WS-06-R003.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
                  },
                  "identifier": "BRD-WS-06-R003.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-06.md",
                    "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                    "source_lines": "L151",
                    "source_section": "6. Coupon Inheritance"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                "source_lines": "L151",
                "source_section": "6. Coupon Inheritance"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                "source_type": "SOURCE_LITERAL",
                "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
              },
              "identifier": "BRD-WS-06-R003.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                "source_lines": "L151",
                "source_section": "6. Coupon Inheritance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                "source_type": "SOURCE_LITERAL",
                "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
              },
              "identifier": "BRD-WS-06-R003.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                "source_lines": "L151",
                "source_section": "6. Coupon Inheritance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                "source_type": "SOURCE_LITERAL",
                "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
              },
              "identifier": "BRD-WS-06-R003.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                "source_lines": "L151",
                "source_section": "6. Coupon Inheritance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                "source_type": "SOURCE_LITERAL",
                "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
              },
              "identifier": "BRD-WS-06-R003.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                "source_lines": "L151",
                "source_section": "6. Coupon Inheritance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
                "source_type": "SOURCE_LITERAL",
                "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
              },
              "identifier": "BRD-WS-06-R003.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
                "source_lines": "L151",
                "source_section": "6. Coupon Inheritance"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.BRD-WS-06-R003.BRD-WS-06-R003.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        }
      ],
      "boundary_cases": [
        "A new Coupon is required when identity or applicability differs"
      ],
      "contract_ast_sha256": "5bcb0e6985d23001b1364c75e595117403236439c60f6ccd2ab94a6bd8431036",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-06-R003",
      "criticality": "NORMAL",
      "disposition": "OPERATOR_REMAP_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-06.md#6. Coupon Inheritance",
            "source_type": "SOURCE_LITERAL",
            "version": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b"
          },
          "identifier": "BRD-WS-06-R003.BRD-WS-06-R003.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-06-R003.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-06.md",
            "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
            "source_lines": "L151",
            "source_section": "6. Coupon Inheritance"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-06-R003.BRD-WS-06-R003.BRD-WS-06-R003.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-06-R003.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.COUPON_ID",
          "FIELD.REUSE_CONTEXT",
          "FIELD.LIFECYCLE_STATE",
          "FIELD.APPLICABILITY_RESULT",
          "FIELD.CREATED_COUPON_IDS"
        ],
        "producer": "BRD-WS-06-R003.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-06-R003.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.COUPON_ID",
          "FIELD.REUSE_CONTEXT",
          "FIELD.LIFECYCLE_STATE",
          "FIELD.APPLICABILITY_RESULT",
          "FIELD.CREATED_COUPON_IDS"
        ],
        "required_values_or_hashes": [
          "BRD-WS-06-R003.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-06-R003.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-06-R003.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-D4D5600D4340028EFB47",
        "P2C-C4-FX-C9447772FC2666DBF428",
        "P2C-C4-FX-C6CD7FB7D7DAB6A19547"
      ],
      "high_risk_audit_subset": false,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "A duplicate Coupon is created solely for the same applicable reuse"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-06-R003-O001",
          "obligation_text": "Không cần tạo lại Coupon"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-06-R003.O1.1.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-06-R003-O001"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID"
      ],
      "positive_oracles": [
        "The existing Coupon is reused without creating a duplicate Coupon"
      ],
      "preconditions": [
        "The Coupon identity, lifecycle and applicability are valid"
      ],
      "prohibitions": [
        "A duplicate Coupon is created solely for the same applicable reuse"
      ],
      "requirement_id": "BRD-WS-06-R003",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-06.md",
        "source_fingerprint": "b09255c9916150a4d3d71b4e7edb71cce05ae60c5fbc177fe43ddec3ecaaff3b",
        "source_lines": "L151",
        "source_section": "6. Coupon Inheritance"
      },
      "source_statement": "Không cần tạo lại Coupon.",
      "surrounding_source_context": "### BRD-WS-06-R003 — Không cần tạo lại Coupon"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-06-R003",
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
        "BRD-WS-06-R003-AC001",
        "BRD-WS-06-R003-AC002",
        "BRD-WS-06-R003-AC003"
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
    "source_lines": "L2252-L3601",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R004",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "20e23b2cb84047758a8466cf2d9c57fdeb2d66a614e143e54d87950b62170a9d"
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
        "BRD-WS-06-R004-AC001",
        "BRD-WS-06-R004-AC002",
        "BRD-WS-06-R004-AC003"
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
    "source_lines": "L3603-L3678",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R005",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "0864b9d2c77582086492e08c726b21e4f2ddc146308c9e4af0bba1241a4733eb"
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-06-R005 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-06-R005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-06-R005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-06-R005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-06-R005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-06-R005 does not define a recovery obligation."
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
    "source_lines": "L3680-L3788",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R006",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "fdb322926bb35deafa88d32c3101ae7a6f58f17f9f37b4d9b66ebdebb86ee8af"
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
        "BRD-WS-06-R006-AC001",
        "BRD-WS-06-R006-AC002",
        "BRD-WS-06-R006-AC003"
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
    "source_fingerprint": "fdb322926bb35deafa88d32c3101ae7a6f58f17f9f37b4d9b66ebdebb86ee8af",
    "source_lines": "L3790-L3865",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R007",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "88815f92c8491c62edd9c9dce7ed0d4236521cc3d2e0ec14d27af0df6aad6e99"
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
        "BRD-WS-06-R007-AC001",
        "BRD-WS-06-R007-AC002",
        "BRD-WS-06-R007-AC003"
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
    "source_lines": "L3867-L3942",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R007"
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
      "requirement_id": "BRD-WS-06-R008",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "6f57018835e43ea7c17de23da748beea68d879dd7b42c40e2f53602bc643ae95"
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
        "BRD-WS-06-R008-AC001",
        "BRD-WS-06-R008-AC002",
        "BRD-WS-06-R008-AC003"
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
    "source_lines": "L3944-L4023",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R008"
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
      "requirement_id": "BRD-WS-06-R009",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "c0c7d4750b415ab5239769a59b1533448d1f961c2831ae8a71f1f66aa160b9db"
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
        "BRD-WS-06-R009-AC001",
        "BRD-WS-06-R009-AC002",
        "BRD-WS-06-R009-AC003"
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
    "source_lines": "L4025-L4104",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R009"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "A transaction without a valid Storefront fails Snapshot completeness validation"
    ],
    "concrete_bindings": [
      {
        "actual_set": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
            "source_type": "SOURCE_LITERAL",
            "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
          },
          "identifier": "RESOLVED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BRD-WS-06-R010.RESOLVED.COLLECTION",
          "origin": {
            "origin_id": "YSIM.BRD-WS-06-R010.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-06.md",
            "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
            "source_lines": "L275-L277",
            "source_section": "12. Marketing Attribution"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "OBSERVE.BRD-WS-06-R010.RESOLVED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
        },
        "required_members": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
            "source_type": "SOURCE_LITERAL",
            "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
          },
          "identifier": "GOVERNED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BRD-WS-06-R010.GOVERNED.COLLECTION",
          "origin": {
            "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-06.md",
            "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
            "source_lines": "L275-L277",
            "source_section": "12. Marketing Attribution"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "RESOLVE.BRD-WS-06-R010.GOVERNED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-06-R010",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Storefront reference is absent or dangling"
    ],
    "operator_composition": [
      "SET_CONTAINS"
    ],
    "positive_oracle": [
      "The Snapshot contains the Storefront reference"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
      "source_lines": "L275-L277",
      "source_section": "12. Marketing Attribution"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
          "source_type": "SOURCE_LITERAL",
          "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
        },
        "identifier": "BRD-WS-06-R010.BRD-WS-06-R010.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-06-R010.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-06.md",
          "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
          "source_lines": "L275-L277",
          "source_section": "12. Marketing Attribution"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-06-R010.BRD-WS-06-R010.BRD-WS-06-R010.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-06-R010.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.TRANSACTION_ID",
        "FIELD.SNAPSHOT_ID",
        "FIELD.STOREFRONT_ID",
        "FIELD.REFERENCE_STATE",
        "FIELD.VALIDATION_RESULT"
      ],
      "producer": "BRD-WS-06-R010.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-06-R010.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.TRANSACTION_ID",
        "FIELD.SNAPSHOT_ID",
        "FIELD.STOREFRONT_ID",
        "FIELD.REFERENCE_STATE",
        "FIELD.VALIDATION_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-WS-06-R010.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-06-R010.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-06-R010.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-06-R010-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS",
          "evaluator_consumed_bindings": [
            "actual_set",
            "required_members"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
              "source_type": "SOURCE_LITERAL",
              "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
            },
            "identifier": "BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-06.md",
              "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
              "source_lines": "L275-L277",
              "source_section": "12. Marketing Attribution"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-06-R010.BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
                  "source_type": "SOURCE_LITERAL",
                  "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
                },
                "identifier": "BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
                  "source_lines": "L275-L277",
                  "source_section": "12. Marketing Attribution"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BRD-WS-06-R010.BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-06.md",
              "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
              "source_lines": "L275-L277",
              "source_section": "12. Marketing Attribution"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_set": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
                  "source_type": "SOURCE_LITERAL",
                  "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
                },
                "identifier": "RESOLVED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BRD-WS-06-R010.RESOLVED.COLLECTION",
                "origin": {
                  "origin_id": "YSIM.BRD-WS-06-R010.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
                  "source_lines": "L275-L277",
                  "source_section": "12. Marketing Attribution"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "OBSERVE.BRD-WS-06-R010.RESOLVED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
              },
              "required_members": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
                  "source_type": "SOURCE_LITERAL",
                  "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
                },
                "identifier": "GOVERNED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BRD-WS-06-R010.GOVERNED.COLLECTION",
                "origin": {
                  "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
                  "source_lines": "L275-L277",
                  "source_section": "12. Marketing Attribution"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "RESOLVE.BRD-WS-06-R010.GOVERNED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
              }
            },
            "comparison": {
              "expected": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
                      "source_type": "SOURCE_LITERAL",
                      "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
                    },
                    "identifier": "BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-06.md",
                      "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
                      "source_lines": "L275-L277",
                      "source_section": "12. Marketing Attribution"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BRD-WS-06-R010.BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
                  "source_lines": "L275-L277",
                  "source_section": "12. Marketing Attribution"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "observed": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
                      "source_type": "SOURCE_LITERAL",
                      "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
                    },
                    "identifier": "BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-06.md",
                      "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
                      "source_lines": "L275-L277",
                      "source_section": "12. Marketing Attribution"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "OBSERVE.BRD-WS-06-R010.BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
                  "source_lines": "L275-L277",
                  "source_section": "12. Marketing Attribution"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
                "source_type": "SOURCE_LITERAL",
                "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
              },
              "identifier": "BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
                "source_lines": "L275-L277",
                "source_section": "12. Marketing Attribution"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-06-R010.BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "SET_CONTAINS"
          },
          "obligation_id": "BRD-WS-06-R010-O001",
          "observed_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
                  "source_type": "SOURCE_LITERAL",
                  "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
                },
                "identifier": "BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-06.md",
                  "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
                  "source_lines": "L275-L277",
                  "source_section": "12. Marketing Attribution"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BRD-WS-06-R010.BRD-WS-06-R010.BRD-WS-06-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-06.md",
              "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
              "source_lines": "L275-L277",
              "source_section": "12. Marketing Attribution"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "operator_id": "SET_CONTAINS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_set": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
                "source_type": "SOURCE_LITERAL",
                "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
              },
              "identifier": "RESOLVED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BRD-WS-06-R010.RESOLVED.COLLECTION",
              "origin": {
                "origin_id": "YSIM.BRD-WS-06-R010.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
                "source_lines": "L275-L277",
                "source_section": "12. Marketing Attribution"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "OBSERVE.BRD-WS-06-R010.RESOLVED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
            },
            "required_members": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
                "source_type": "SOURCE_LITERAL",
                "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
              },
              "identifier": "GOVERNED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BRD-WS-06-R010.GOVERNED.COLLECTION",
              "origin": {
                "origin_id": "BRD-WS-06-R010.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-06.md",
                "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
                "source_lines": "L275-L277",
                "source_section": "12. Marketing Attribution"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "RESOLVE.BRD-WS-06-R010.GOVERNED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
            }
          }
        }
      ],
      "boundary_cases": [
        "A transaction without a valid Storefront fails Snapshot completeness validation"
      ],
      "contract_ast_sha256": "6b5c5c0a5d30e7b5b03787a47a3ebaf19084e7679ad636c41a76daab2a8b200a",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-06-R010",
      "criticality": "HIGH",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-06.md#12. Marketing Attribution",
            "source_type": "SOURCE_LITERAL",
            "version": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50"
          },
          "identifier": "BRD-WS-06-R010.BRD-WS-06-R010.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-06-R010.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-06.md",
            "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
            "source_lines": "L275-L277",
            "source_section": "12. Marketing Attribution"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-06-R010.BRD-WS-06-R010.BRD-WS-06-R010.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-06-R010.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.TRANSACTION_ID",
          "FIELD.SNAPSHOT_ID",
          "FIELD.STOREFRONT_ID",
          "FIELD.REFERENCE_STATE",
          "FIELD.VALIDATION_RESULT"
        ],
        "producer": "BRD-WS-06-R010.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-06-R010.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.TRANSACTION_ID",
          "FIELD.SNAPSHOT_ID",
          "FIELD.STOREFRONT_ID",
          "FIELD.REFERENCE_STATE",
          "FIELD.VALIDATION_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-WS-06-R010.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-06-R010.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-06-R010.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-R2-FX-68AE9ACECE66A9667FF6",
        "P2C-C4-R2-FX-6C31126B17BB862FB600",
        "P2C-C4-R2-FX-A5247A49295697DB35D6"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Storefront reference is absent or dangling"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-06-R010-O001",
          "obligation_text": "Một giao dịch cần Snapshot: - Storefront"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-06-R010.O1.1.SET_CONTAINS"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-06-R010-O001"
        }
      ],
      "operator_composition": [
        "SET_CONTAINS"
      ],
      "positive_oracles": [
        "The Snapshot contains the Storefront reference"
      ],
      "preconditions": [
        "The originating Storefront identity is known"
      ],
      "prohibitions": [
        "Storefront reference is absent or dangling"
      ],
      "requirement_id": "BRD-WS-06-R010",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-06.md",
        "source_fingerprint": "084cbd6515925bce541e8f6385c15b9b5efb2b95ea237faf91f5dcb304f68d50",
        "source_lines": "L275-L277",
        "source_section": "12. Marketing Attribution"
      },
      "source_statement": "Một giao dịch cần Snapshot: - Storefront",
      "surrounding_source_context": "### BRD-WS-06-R010 — Một giao dịch cần Snapshot: - Storefront"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-06-R010",
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
        "BRD-WS-06-R010-AC001",
        "BRD-WS-06-R010-AC002",
        "BRD-WS-06-R010-AC003"
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
    "source_lines": "L4106-L4900",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R011",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "174bba8a0a9d02e128ec80becb06866ff1be4e26f64f69a63a1aa997cbfeee8c"
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
        "BRD-WS-06-R011-AC001",
        "BRD-WS-06-R011-AC002",
        "BRD-WS-06-R011-AC003"
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
    "source_fingerprint": "174bba8a0a9d02e128ec80becb06866ff1be4e26f64f69a63a1aa997cbfeee8c",
    "source_lines": "L4902-L4977",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R011"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R012",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "27960f5536009a59dceb8ae7ba44cc258ce8bc6c6804ea8922173dd2ebdf9298"
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
        "BRD-WS-06-R012-AC001",
        "BRD-WS-06-R012-AC002",
        "BRD-WS-06-R012-AC003"
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
    "source_fingerprint": "27960f5536009a59dceb8ae7ba44cc258ce8bc6c6804ea8922173dd2ebdf9298",
    "source_lines": "L4979-L5054",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R012"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R013",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "e75ac086d12f0f5ea7cca09fb9cfd4a279d09b34cebfdd5e9274458f64258d1a"
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
        "BRD-WS-06-R013-AC001",
        "BRD-WS-06-R013-AC002",
        "BRD-WS-06-R013-AC003"
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
    "source_fingerprint": "e75ac086d12f0f5ea7cca09fb9cfd4a279d09b34cebfdd5e9274458f64258d1a",
    "source_lines": "L5056-L5131",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R013"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R014",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "cf406c5ec820d8eab868266717f84fd5b3369044bf5e4f348a03065aeac52869"
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
        "BRD-WS-06-R014-AC001",
        "BRD-WS-06-R014-AC002",
        "BRD-WS-06-R014-AC003"
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
    "source_fingerprint": "cf406c5ec820d8eab868266717f84fd5b3369044bf5e4f348a03065aeac52869",
    "source_lines": "L5133-L5208",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R014"
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
      "requirement_id": "BRD-WS-06-R015",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "22c4097b973828e5e28c73e2d49b950a858f467738b0848f7bb67bc64ee7d855"
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
        "BRD-WS-06-R015-AC001",
        "BRD-WS-06-R015-AC002",
        "BRD-WS-06-R015-AC003"
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
    "source_fingerprint": "22c4097b973828e5e28c73e2d49b950a858f467738b0848f7bb67bc64ee7d855",
    "source_lines": "L5210-L5289",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R015"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R016",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "907389ad4d1175b3951ae867d1511981795aabdd2c5a683b2f6b76fd0ea09b35"
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
        "BRD-WS-06-R016-AC001",
        "BRD-WS-06-R016-AC002",
        "BRD-WS-06-R016-AC003"
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
    "source_fingerprint": "907389ad4d1175b3951ae867d1511981795aabdd2c5a683b2f6b76fd0ea09b35",
    "source_lines": "L5291-L5366",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R016"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R017",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "005799ce044ac83ff0cbd12d1c2d65cfb4688ddd2cacb310f9bcab1676fc5db0"
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
        "BRD-WS-06-R017-AC001",
        "BRD-WS-06-R017-AC002",
        "BRD-WS-06-R017-AC003"
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
    "source_fingerprint": "005799ce044ac83ff0cbd12d1c2d65cfb4688ddd2cacb310f9bcab1676fc5db0",
    "source_lines": "L5368-L5443",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R017"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-06-R018",
    "scope_status": "FUTURE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_lines": "L5445-L5503",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R018"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R019",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "8291619a7a45c192eb1ebfb3a889237f50dfc3800cb53b38d09001b2f829ce7f"
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
        "BRD-WS-06-R019-AC001",
        "BRD-WS-06-R019-AC002",
        "BRD-WS-06-R019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R019-O001",
      "obligation_text": "Mỗi Promotion phải có Funding Owner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-06-R019 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-06-R019 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-06-R019 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-06-R019-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-06-R019-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-06-R019 does not define a recovery obligation."
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
    "source_lines": "L5505-L5613",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R019"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-06-R020",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "509709ecd37f0c6c750670401fd1f3e9b653c2407f0929474b2f5b66c2e97eec"
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
        "BRD-WS-06-R020-AC001",
        "BRD-WS-06-R020-AC002",
        "BRD-WS-06-R020-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-06-R020-O001",
      "obligation_text": "Chi phí Promotion luôn được tính vào chi phí Marketing của Funding Owner"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-06-R020 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-06-R020 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-06-R020 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-06-R020-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-06-R020-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-06-R020 does not define a recovery obligation."
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
    "source_lines": "L5615-L5723",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R020"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-06-R021",
    "scope_status": "FUTURE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is retained for a future baseline and is excluded from v2.3 delivery.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_lines": "L5725-L5783",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R021"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-06-R022",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_lines": "L5785-L5843",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R022"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-06-R023",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_fingerprint": "53536e50e6d238519542149ee56e471651f374295050393e8795af21b914080e",
    "source_lines": "L5845-L5903",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R023"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-06-R024",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_fingerprint": "fc750c8f921ae6d9b5ec4939b5dcccaa33ec83e36cb874be1fcf7a63cd0bf98f",
    "source_lines": "L5905-L5963",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R024"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-06-R025",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_fingerprint": "58c367247371c88b485dbcd9eba40b65d104912d898263c5bab871bdaae35c46",
    "source_lines": "L5965-L6023",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R025"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-06-R026",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_fingerprint": "a33414f0b82530425bcec5ae2b2ae572844c284f8072940354419713593d18b3",
    "source_lines": "L6025-L6083",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R026"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-06-R027",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_fingerprint": "48593098bd2806ec00bba987a3575ec66cf2341e3caf6d70f3b144915a37b122",
    "source_lines": "L6085-L6143",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R027"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-06-R028",
    "scope_status": "DEFERRED"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly deferred beyond v2.3 by an approved scope decision.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_fingerprint": "a4adfebae9d6f7e536510acf068a5f2981f46acc809aff1af71651ef18108e92",
    "source_lines": "L6145-L6203",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-06-R028"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-06-001",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "9e46724abc7af75f90a82ab2443668774aabc16e872261dd9fd30b78d7ad2f29"
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
        "EP-06-001-AC001",
        "EP-06-001-AC002",
        "EP-06-001-AC003"
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
    "source_fingerprint": "9e46724abc7af75f90a82ab2443668774aabc16e872261dd9fd30b78d7ad2f29",
    "source_lines": "L6205-L6280",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-06-001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-06-002",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "ee45af4dd8db0aa6270ec7352e14bf4e1d571ad8fa2da3832a6d6ecc7bcbac2e"
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
        "EP-06-002-AC001",
        "EP-06-002-AC003",
        "EP-06-002-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-06-002-O001",
      "obligation_text": "Landing Page là Business Asset"
    },
    {
      "acceptance_criterion_references": [
        "EP-06-002-AC002",
        "EP-06-002-AC003",
        "EP-06-002-AC004"
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
    "source_fingerprint": "ee45af4dd8db0aa6270ec7352e14bf4e1d571ad8fa2da3832a6d6ecc7bcbac2e",
    "source_lines": "L6282-L6367",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-06-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-06-003",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "source_fingerprint": "6fae7ec4d336414e3f33f29f35084a5f6998c8860e2f47282aa7b889da8734e9"
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
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-06-003-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-06-003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-06-003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-06-003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-06-003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-06-003 does not define a recovery obligation."
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
    "source_fingerprint": "6fae7ec4d336414e3f33f29f35084a5f6998c8860e2f47282aa7b889da8734e9",
    "source_lines": "L6369-L6479",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-06-003"
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
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "Alias evidence is inherited from the canonical target; the alias is not an acceptance unit.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
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
    "source_fingerprint": "92def6b8d901bb3025f6729b02ba67f9d952a1b1f3133e07008980ebbbcafa68",
    "source_lines": "L6481-L6531",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-06-004"
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
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "Alias evidence is inherited from the canonical target; the alias is not an acceptance unit.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
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
    "source_fingerprint": "13ee91cd8c321bc501b12b6876df35ad474abaa5a93bc02aafaea54ee5d0ff65",
    "source_lines": "L6533-L6581",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-06-005"
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
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "Alias evidence is inherited from the canonical target; the alias is not an acceptance unit.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
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
    "source_fingerprint": "81e785338042be2c9d25ed4362376a782fa7b706aaf49240c031c98e3fe2635b",
    "source_lines": "L6583-L6631",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-06-006"
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
