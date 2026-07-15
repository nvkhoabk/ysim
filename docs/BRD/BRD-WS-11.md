---
document_code: "BRD-WS-11"
title: "Customer Service, Ticketing & Customer Lifecycle"
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

# BRD Workshop 11

# Customer Service, Ticketing & Customer Lifecycle

---

# 1. Workshop Objective

Workshop này xác định toàn bộ Customer Success Domain của YSim.

Bao gồm:

- Customer Lifecycle
- Customer Portal
- Customer Support
- Ticket Management
- Knowledge Base
- FAQ
- Troubleshooting Wizard
- SLA
- Capability Routing
- Customer Satisfaction
- Organization Onboarding

Workshop này không mô tả:

- Loyalty
- CRM Marketing Automation
- AI Customer Support
- Call Center

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| CustomerProfile | Master |
| CustomerRelationship | Transaction |
| CustomerLifecycle | Master |
| CustomerPortal | Capability |
| SupportTicket | Transaction |
| TicketComment | Transaction |
| TicketAttachment | Transaction |
| TicketAssignment | Transaction |
| TicketEscalation | Transaction |
| SupportQueue | Master |
| SLA | Master |
| KnowledgeArticle | Master |
| FAQArticle | Master |
| TroubleshootingFlow | Master |
| CustomerFeedback | Transaction |
| FeatureRequest | Transaction |

---

# 3. Customer Lifecycle

Customer Lifecycle:

```text
Visitor

↓

Lead

↓

Customer

↓

Traveller

↓

Returning Customer

↓

Inactive
```

Lifecycle được thiết kế mở để mở rộng trong các phiên bản sau.

---

# 4. Enterprise Customer Principle

Customer là tài sản của Platform.

Relationship là tài sản của Organization.

Customer Identity luôn thuộc YSim.

Organization chỉ được cấp quyền quản lý Relationship.

Ví dụ:

```text
Customer Identity

↓

YSim Platform

↓

Relationship

↓

ABC Travel

↓

Relationship

↓

XYZ Travel
```

Một Customer có thể có nhiều Relationship.

Không tạo Customer mới.

---

# 5. Customer Portal

Customer Portal là Capability thống nhất của Customer.

Customer Portal bao gồm:

- Product Discovery
- Product Suggestion
- Product Purchase
- Payment
- Order Management
- Download Purchased QR
- Customer Support
- Ticket
- Knowledge Base
- FAQ
- Troubleshooting Wizard
- Notification Center
- Promotion Center
- Marketing Preference
- Reorder

Customer Portal hỗ trợ:

- Multi-language
- Multi-currency
- Theme
- Multiple Identity Switching
- Notification Center

Trang chủ Customer Portal hiển thị:

- Product Search
- Region Search
- Featured Products
- Recent Orders
- Notification Summary

Customer Portal cũng hoạt động như một Storefront đầy đủ.

---

# 6. Customer Preferences

Customer có thể cấu hình:

- Marketing Subscription
- Marketing Unsubscribe
- Notification Preference
- Preferred Language
- Preferred Currency

Marketing Preference được sử dụng trên toàn Platform.

---

# 7. Customer Support

Customer Support hỗ trợ:

- Ticket
- Knowledge Base
- FAQ
- Troubleshooting Wizard
- Contact Center

Customer Portal hiển thị các thông tin liên hệ theo cấu hình của Organization:

- Phone
- Email
- Facebook Page
- WhatsApp
- Telegram
- Zalo OA

---

# 8. Ticket Management

Ticket có thể phát sinh từ:

- Customer
- Organization
- User
- Sales
- Portal
- API
- Email
- Internal System

Email hoặc API có thể tự động tạo Ticket.

Ticket luôn lưu:

- Source
- Creator
- Owner

---

# 9. Ticket Owner

Nếu Ticket phát sinh từ Customer:

Owner mặc định là Customer.

Nếu Ticket phát sinh từ Organization:

Owner mặc định là Organization.

Creator có thể chỉ định Customer Relationship.

SalesOrder chỉ đóng vai trò Reference.

---

# 10. Ticket Category

Ticket Category sử dụng:

Reference Data Management.

Admin Portal có thể:

- Thêm
- Sửa
- Vô hiệu hóa

Category.

Không Hard-code.

---

# 11. Reference Data Management

YSim sử dụng Reference Data Management.

Ví dụ:

- Ticket Category
- KB Category
- FAQ Category
- Customer Group
- Notification Type
- Country
- Currency
- Language

Reference Data được quản lý tập trung trên Admin Portal.

---

# 12. SLA

SLA được xác định theo:

- Organization
- Category
- Priority
- Commercial Agreement
- Capability

Tiêu chí quan trọng nhất:

Processing Time.

---

# 13. Capability Routing

Support Queue không cố định.

Routing được xác định theo:

Capability Routing.

Ví dụ:

```text
Organization

↓

Parent

↓

YSim

↓

Supplier
```

Capability Routing dựa trên:

- Support Policy
- Category
- Language
- Capability
- Organization Configuration

---

# 14. Support Policy

Support Policy gồm:

- SELF_SUPPORT
- PARENT_SUPPORT
- HYBRID

Mặc định:

PARENT_SUPPORT.

---

# 15. Escalation

Escalation:

```text
Organization

↓

Parent

↓

YSim

↓

Supplier
```

Supplier không tham gia Ticket.

Supplier chỉ nhận:

Supplier Case.

Supplier Case luôn được YSim Staff theo dõi.

---

# 16. Knowledge Management

Knowledge Management gồm:

- Knowledge Base
- FAQ
- Troubleshooting Wizard

Ba Capability độc lập.

Organization có thể tùy chỉnh:

- Payment Guide
- Contact Information
- Branding
- Support Information

---

# 17. Troubleshooting Wizard

Troubleshooting Wizard hỗ trợ:

- Activation Guide
- Issue Resolver
- Decision Tree

Được thiết kế mở để mở rộng trong các phiên bản sau.

---

# 18. Organization Onboarding

Organization được tạo theo quy trình:

```text
Created

↓

Setup Wizard

↓

Configuration Checklist

↓

Completed

↓

Activated
```

Checklist bao gồm:

- Theme
- Storefront
- Merchant Account
- Payment Configuration
- Support Configuration
- Knowledge Base
- Contact Information
- Notification
- Currency
- Language

Organization có thể Active chi chưa hoàn thành toán bộ Checklist.

---

# 19. Customer Feedback

Customer Feedback có thể phát sinh từ:

- Product
- Fulfillment
- Ticket
- Customer Portal

Feedback được tổng hợp theo Distribution Hierarchy.

---

# 20. Satisfaction Survey

Platform hỗ trợ:

- CSAT
- CES
- NPS
- Rating
- Emoji Rating

Có thể cấu hình:

- Always
- Random
- Disabled

Organization có thể chủ động câu hình thiết lập các Satisfaction Survey này hoặc sử dụng từ Parent.

---

# 21. Customer Privacy

Support mặc định chỉ xem:

Masked Data.

Customer có thể chủ động chia sẻ:

- Email
- Phone
- QR
- All Information

theo nguyên tắc:

Consent Based Data Access.

---

# 22. Ticket Visibility

Organization chỉ xem Ticket thuộc:

- Customer Relationship của mình
- Portal của mình

Parent xem theo Support Policy.

Grand Parent và Grand Child không nhìn thấy Ticket của nhau.

---

# 23. Internal Note

Ticket hỗ trợ:

- Customer Comment
- Internal Note

Internal Note không hiển thị cho Customer.

---

# 24. Attachment

Ticket hỗ trợ:

- Image
- PDF
- QR
- Invoice

Không hỗ trợ Video trong Version 2.0.

---

# 25. Feature Request

Platform hỗ trợ Feature Request.

Feature Request có thể phát sinh từ:

- Customer
- User
- Organization

Ví dụ:

- Đề nghị phát triển tính năng
- Đề nghị tích hợp Payment Gateway
- Đề nghị tích hợp Supplier
- Đề nghị cải tiến UI/UX

Feature Request được chuyển tới:

YSim Customer Success Team.

Sau khi Technical Team đánh giá sẽ phản hồi kết quả.

Feature Request là Business Capability của Platform.

---

# 26. AI & Translation

Version 2.0:

Không triển khai AI Answer.

Triển khai:

- Auto Translation
- Multi-language Knowledge Base

AI Customer Support được giữ chỗ cho phiên bản sau.

---

# 27. Future Capability

Giữ chỗ cho các Capability:

- Customer Timeline
- WebRTC Call trên Customer Portal
- AI Customer Support
- Voice Bot
- Chat Bot

WebRTC chỉ được kích hoạt khi Customer chủ động sử dụng.

---

# 28. Business Decisions (Locked)

## BD-11-001

Customer Portal là Capability thống nhất của Customer.

---

## BD-11-002

Customer Identity thuộc Platform.

Customer Relationship thuộc Organization.

---

## BD-11-003

Ticket hỗ trợ nhiều Source.

---

## BD-11-004

Ticket Category sử dụng Reference Data Management.

---

## BD-11-005

Capability Routing quyết định Support Queue.

---

## BD-11-006

Support Policy gồm:

- SELF_SUPPORT
- PARENT_SUPPORT
- HYBRID

---

## BD-11-007

Supplier chỉ nhận Supplier Case.

---

## BD-11-008

Knowledge Base, FAQ và Troubleshooting Wizard là ba Capability độc lập.

---

## BD-11-009

Organization Onboarding là Business Capability.

---

## BD-11-010

Customer Feedback hỗ trợ nhiều nguồn.

---

## BD-11-011

Platform hỗ trợ CSAT, CES, NPS và Rating.

---

## BD-11-012

Support sử dụng Consent Based Data Access.

---

## BD-11-013

Feature Request là Business Capability của Platform.

---

## BD-11-014

Version 2.0 triển khai Auto Translation.

AI Customer Support được giữ chỗ.

---

## BD-11-015

Customer Timeline và WebRTC Customer Portal được giữ chỗ cho phiên bản sau.

---

# 29. Enterprise Design Principles

## EP-11-001

Customer Portal là điểm truy cập thống nhất trong toàn bộ Customer Lifecycle.

---

## EP-11-002

Customer Identity và Customer Relationship được tách biệt.

---

## EP-11-003

Support Routing dựa trên Capability, không dựa trên cấu trúc tổ chức cố định.

---

## EP-11-004

Reference Data được quản lý tập trung.

---

## EP-11-005

Knowledge Management hỗ trợ tái sử dụng nội dung giữa KB, FAQ và Troubleshooting Wizard.

---

## EP-11-006

Customer Privacy tuân thủ Consent Based Data Access.

---

## EP-11-007

Feature Request là một phần của Customer Success Lifecycle.

---

# 30. Business Capabilities Covered

- Customer Lifecycle Management
- Customer Relationship Management
- Customer Portal
- Ticket Management
- Knowledge Base Management
- FAQ Management
- Troubleshooting Management
- Customer Support
- Capability Routing
- SLA Management
- Organization Onboarding
- Customer Feedback
- Customer Satisfaction
- Feature Request Management

---

# 31. Traceability

Workshop này kế thừa:

- BRD-WS-01
- BRD-WS-02
- BRD-WS-03
- BRD-WS-04
- BRD-WS-05
- BRD-WS-06
- BRD-WS-07
- BRD-WS-08
- BRD-WS-09
- BRD-WS-10

---

# 32. Impacts to Other Domains

Workshop này ảnh hưởng tới:

- Customer Portal
- CRM
- Notification Platform
- Reporting & BI
- Organization Management
- API
- DMS
- DBD

---

# 33. Workshop Status

**Status:** FROZEN

Workshop này hoàn thiện toàn bộ Customer Success Domain của YSim.

---

# 34. Next Workshop

**BRD-WS-12 – Notification, Communication & Engagement Platform**

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-001 — Customer Portal là Capability thống nhất của Customer

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-001-AC001",
      "given": "the applicable business context, actor, and input for Customer Portal là Capability thống nhất của Customer",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-11-001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Customer Portal là Capability thống nhất của Customer",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-11-001-O001"
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
        "BD-11-001-AC001",
        "BD-11-001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-001-O001",
      "obligation_text": "Customer Portal là Capability thống nhất của Customer"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Portal là Capability thống nhất của Customer.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Customer Portal",
    "source_context_sha256": "b1edef472fca783ec9be9bfc1dd0988af02e50ccfadf3e6fa59b735f0fc25204",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "57ccba27b9b2f3ff0540333a6ccb46011e8bd2aa6d14524fc3ad9f8e15637e60",
    "source_lines": "L612-L615",
    "source_section": "28. Business Decisions (Locked) > BD-11-001"
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
  "stable_id": "BD-11-001",
  "title": "Customer Portal là Capability thống nhất của Customer",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-002 — Customer Identity thuộc Platform. Customer Relationship thuộc Organization

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-002-AC001",
      "given": "the applicable business context, actor, and input for Customer Identity thuộc Platform. Customer Relationship thuộc Organization",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-002-AC002",
      "given": "the applicable business context, actor, and input for Customer Identity thuộc Platform. Customer Relationship thuộc Organization",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-002-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-11-002-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Customer Identity thuộc Platform. Customer Relationship thuộc Organization",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-11-002-O001",
        "BD-11-002-O002"
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
        "BD-11-002-AC001",
        "BD-11-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-002-O001",
      "obligation_text": "Customer Identity thuộc Platform"
    },
    {
      "acceptance_criterion_references": [
        "BD-11-002-AC002",
        "BD-11-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-002-O002",
      "obligation_text": "Customer Relationship thuộc Organization"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-11-002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-11-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-11-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-11-002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-11-002-AC001",
        "BD-11-002-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-11-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Identity thuộc Platform. Customer Relationship thuộc Organization.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-002",
    "source_context_sha256": "82d9b57e86d4c8c4d27fdfa0263486952617fe0711ae4899f1d3bfdfc6aef08a",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "56f3d7615fb2ba346b532c2871c9df47f97aec9700b1bfff829e6718468808a0",
    "source_lines": "L618-L623",
    "source_section": "28. Business Decisions (Locked) > BD-11-002"
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
  "stable_id": "BD-11-002",
  "title": "Customer Identity thuộc Platform. Customer Relationship thuộc Organization",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-003 — Ticket hỗ trợ nhiều Source

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-003-AC001",
      "given": "the applicable business context, actor, and input for Ticket hỗ trợ nhiều Source",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-003-O001"
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
        "BD-11-003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-003-O001",
      "obligation_text": "Ticket hỗ trợ nhiều Source"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Ticket hỗ trợ nhiều Source.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-003",
    "source_context_sha256": "0fd7e4b62a6645131f8e2c6f7cf08d805cbb1ca9361214f46ce83f367e4521ef",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "e5fa4ae430e74b4e0bf7a9cf789fbe448dcf1a0b03bad4eb906aa9785523d352",
    "source_lines": "L626-L629",
    "source_section": "28. Business Decisions (Locked) > BD-11-003"
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
  "stable_id": "BD-11-003",
  "title": "Ticket hỗ trợ nhiều Source",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-004 — Ticket Category sử dụng Reference Data Management

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-004-AC001",
      "given": "the applicable business context, actor, and input for Ticket Category sử dụng Reference Data Management",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-004-O001"
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
        "BD-11-004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-004-O001",
      "obligation_text": "Ticket Category sử dụng Reference Data Management"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Ticket Category sử dụng Reference Data Management.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-004",
    "source_context_sha256": "628232c2d2731cb0949b1b2f30422bc700945d3b3046e23d7649108723163ff9",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "6ae985a2214a7ff5e38245a786247f43b466ba18c65b572e6cfc38f6215f93c2",
    "source_lines": "L632-L635",
    "source_section": "28. Business Decisions (Locked) > BD-11-004"
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
  "stable_id": "BD-11-004",
  "title": "Ticket Category sử dụng Reference Data Management",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-005 — Capability Routing quyết định Support Queue

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-005-AC001",
      "given": "the applicable business context, actor, and input for Capability Routing quyết định Support Queue",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-005-O001"
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
        "BD-11-005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-005-O001",
      "obligation_text": "Capability Routing quyết định Support Queue"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Capability Routing quyết định Support Queue.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-005",
    "source_context_sha256": "d87c95733079fe9eff14f0e72dccc923c55873b5829e6405cbd4110a8f519044",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "16995cb8c3ea01a17439dd862e874bb601d9ee9fd67a19ce9a028f450d82f004",
    "source_lines": "L638-L641",
    "source_section": "28. Business Decisions (Locked) > BD-11-005"
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
  "stable_id": "BD-11-005",
  "title": "Capability Routing quyết định Support Queue",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-006 — Support Policy gồm: - SELF_SUPPORT - PARENT_SUPPORT - HYBRID

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-006-AC001",
      "given": "the applicable business context, actor, and input for Support Policy gồm: - SELF_SUPPORT - PARENT_SUPPORT - HYBRID",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-006-AC002",
      "given": "the applicable business context, actor, and input for Support Policy gồm: - SELF_SUPPORT - PARENT_SUPPORT - HYBRID",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-006-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-006-AC003",
      "given": "the applicable business context, actor, and input for Support Policy gồm: - SELF_SUPPORT - PARENT_SUPPORT - HYBRID",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-006-O003"
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
        "BD-11-006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-006-O001",
      "obligation_text": "Support Policy gồm: SELF_SUPPORT."
    },
    {
      "acceptance_criterion_references": [
        "BD-11-006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-006-O002",
      "obligation_text": "Support Policy gồm: PARENT_SUPPORT."
    },
    {
      "acceptance_criterion_references": [
        "BD-11-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-006-O003",
      "obligation_text": "Support Policy gồm: HYBRID."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Support Policy gồm: - SELF_SUPPORT - PARENT_SUPPORT - HYBRID",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "14. Support Policy",
    "source_context_sha256": "a72d3e71d7b7aac537d275f153378d13fc6cd9d649303f441cd9b9426e54f528",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "a585d6b4a5165e9c629473ec32b09970cd16794d9a0488a6fcdc95879334ea2a",
    "source_lines": "L644-L651",
    "source_section": "28. Business Decisions (Locked) > BD-11-006"
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
  "stable_id": "BD-11-006",
  "title": "Support Policy gồm: - SELF_SUPPORT - PARENT_SUPPORT - HYBRID",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-007 — Supplier chỉ nhận Supplier Case

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-007-AC001",
      "given": "the applicable business context, actor, and input for Supplier chỉ nhận Supplier Case",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-007-O001"
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
        "BD-11-007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-007-O001",
      "obligation_text": "Supplier chỉ nhận Supplier Case"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier chỉ nhận Supplier Case.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-007",
    "source_context_sha256": "65e7aa628dc9aa4ade49e7c3eec75657fb3bac7817442f2bc0c0cc51890beb6b",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "a4c1e68adee18c36fc107010fa43ffb392deba0d9ee5e69d971eb200b9f1fa5e",
    "source_lines": "L654-L657",
    "source_section": "28. Business Decisions (Locked) > BD-11-007"
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
  "stable_id": "BD-11-007",
  "title": "Supplier chỉ nhận Supplier Case",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-008 — Knowledge Base, FAQ và Troubleshooting Wizard là ba Capability độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-008-AC001",
      "given": "the applicable business context, actor, and input for Knowledge Base, FAQ và Troubleshooting Wizard là ba Capability độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "BD-11-008-O001"
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
        "BD-11-008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-008-O001",
      "obligation_text": "Knowledge Base, FAQ và Troubleshooting Wizard là ba Capability độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Knowledge Base, FAQ và Troubleshooting Wizard là ba Capability độc lập.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-008",
    "source_context_sha256": "ada24aa4e960116073b1690735521f4e5de63847877fc9da2baf8b65ce83e44b",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "4a8edd3e0f2b25f09aef2d8fd48552b636fe46a659019e992b89014e9e3de65b",
    "source_lines": "L660-L663",
    "source_section": "28. Business Decisions (Locked) > BD-11-008"
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
  "stable_id": "BD-11-008",
  "title": "Knowledge Base, FAQ và Troubleshooting Wizard là ba Capability độc lập",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-009 — Organization Onboarding là Business Capability

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-009-AC001",
      "given": "the applicable business context, actor, and input for Organization Onboarding là Business Capability",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-009-O001"
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
        "BD-11-009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-009-O001",
      "obligation_text": "Organization Onboarding là Business Capability"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization Onboarding là Business Capability.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-009",
    "source_context_sha256": "375e8756a949005c564a6a8739897165f9f210f25d9432e7e84a5c21e596bc3b",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "a8fc90815e1e323410491bd626bf6c9ea2d9cc443977756e52f2631bc8248f86",
    "source_lines": "L666-L669",
    "source_section": "28. Business Decisions (Locked) > BD-11-009"
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
  "stable_id": "BD-11-009",
  "title": "Organization Onboarding là Business Capability",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-010 — Customer Feedback hỗ trợ nhiều nguồn

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "CUSTOMER_FEEDBACK_SOURCE_ATTRIBUTION_V1",
      "criterion_id": "BD-11-010-AC001",
      "given": "valid Customer Feedback originating from Product",
      "observable_evidence": "accepted feedback identity, source=Product, attribution reference, and ingestion outcome",
      "then": "the feedback is accepted and attributed to Product",
      "verifies": [
        "BD-11-010-O001"
      ],
      "when": "the feedback is submitted"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "CUSTOMER_FEEDBACK_SOURCE_ATTRIBUTION_V1",
      "criterion_id": "BD-11-010-AC002",
      "given": "valid Customer Feedback originating from Fulfillment",
      "observable_evidence": "accepted feedback identity, source=Fulfillment, attribution reference, and ingestion outcome",
      "then": "the feedback is accepted and attributed to Fulfillment",
      "verifies": [
        "BD-11-010-O002"
      ],
      "when": "the feedback is submitted"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "CUSTOMER_FEEDBACK_SOURCE_ATTRIBUTION_V1",
      "criterion_id": "BD-11-010-AC003",
      "given": "valid Customer Feedback originating from Ticket",
      "observable_evidence": "accepted feedback identity, source=Ticket, attribution reference, and ingestion outcome",
      "then": "the feedback is accepted and attributed to Ticket",
      "verifies": [
        "BD-11-010-O003"
      ],
      "when": "the feedback is submitted"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "CUSTOMER_FEEDBACK_SOURCE_ATTRIBUTION_V1",
      "criterion_id": "BD-11-010-AC004",
      "given": "valid Customer Feedback originating from Customer Portal",
      "observable_evidence": "accepted feedback identity, source=Customer Portal, attribution reference, and ingestion outcome",
      "then": "the feedback is accepted and attributed to Customer Portal",
      "verifies": [
        "BD-11-010-O004"
      ],
      "when": "the feedback is submitted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "CUSTOMER_FEEDBACK_SOURCE_REJECTION_V1",
      "criterion_id": "BD-11-010-AC005",
      "given": "Customer Feedback with an unsupported source or malformed source attribution",
      "observable_evidence": "submitted source, validation reason, rejection outcome, and absence of accepted feedback identity",
      "then": "the input is rejected with a deterministic source-validation reason and is not recorded as accepted feedback",
      "verifies": [
        "BD-11-010-O005"
      ],
      "when": "the feedback is submitted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-11-010-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-010-O001",
      "obligation_text": "Customer Feedback from Product is ingested and attributed to Product."
    },
    {
      "acceptance_criterion_references": [
        "BD-11-010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-010-O002",
      "obligation_text": "Customer Feedback from Fulfillment is ingested and attributed to Fulfillment."
    },
    {
      "acceptance_criterion_references": [
        "BD-11-010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-010-O003",
      "obligation_text": "Customer Feedback from Ticket is ingested and attributed to Ticket."
    },
    {
      "acceptance_criterion_references": [
        "BD-11-010-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-010-O004",
      "obligation_text": "Customer Feedback from Customer Portal is ingested and attributed to Customer Portal."
    },
    {
      "acceptance_criterion_references": [
        "BD-11-010-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-010-O005",
      "obligation_text": "Unsupported or malformed Customer Feedback source input has a deterministic rejection outcome."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Feedback hỗ trợ nhiều nguồn.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-010",
    "source_context_sha256": "a584ef3f194a2bb4ec05e8b01ce64617b50092461754aea3b14faa4e1a56ed03",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "6f8d90d64bee7d9030dae0bc234b7c37d2837774c7203748d1cec6ed86b5281e",
    "source_lines": "L672-L675",
    "source_section": "28. Business Decisions (Locked) > BD-11-010"
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
  "stable_id": "BD-11-010",
  "title": "Customer Feedback hỗ trợ nhiều nguồn",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-011 — Platform hỗ trợ CSAT, CES, NPS và Rating

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-011-AC001",
      "given": "the applicable business context, actor, and input for Platform hỗ trợ CSAT, CES, NPS và Rating",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-011-O001"
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
        "BD-11-011-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-011-O001",
      "obligation_text": "Platform hỗ trợ CSAT, CES, NPS và Rating"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ CSAT, CES, NPS và Rating.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-011",
    "source_context_sha256": "025e8d12e5e4c2da9d9361a52d3808718a2523aa2effd780ce6f9583cf1ecbf1",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "39d7337c51485be888a61f6d3aa16cc98da2a782176fb8e5742efee43615a204",
    "source_lines": "L678-L681",
    "source_section": "28. Business Decisions (Locked) > BD-11-011"
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
  "stable_id": "BD-11-011",
  "title": "Platform hỗ trợ CSAT, CES, NPS và Rating",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-012 — Support sử dụng Consent Based Data Access

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BD-11-012-AC001",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Support sử dụng Consent Based Data Access",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BD-11-012-O001"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "PRIVACY_POLICY_DENIAL_V1",
      "criterion_id": "BD-11-012-AC002",
      "given": "a data action whose purpose, consent, scope, or effective policy does not permit the requested data use under Support sử dụng Consent Based Data Access",
      "observable_evidence": "actor, purpose, consent and scope, effective policies, denial reason, exposed-data comparison, and audit record",
      "then": "the data action is denied, no additional protected data is exposed or changed, and the policy reason is audited",
      "verifies": [
        "BD-11-012-O001"
      ],
      "when": "privacy conformance is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-11-012-AC003",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Support sử dụng Consent Based Data Access",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-11-012-O001"
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
        "BD-11-012-AC001",
        "BD-11-012-AC002",
        "BD-11-012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-012-O001",
      "obligation_text": "Support sử dụng Consent Based Data Access"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-11-012-AC003"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-11-012 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-11-012 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-11-012 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-11-012-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-11-012 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Support sử dụng Consent Based Data Access.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-012",
    "source_context_sha256": "17e41395671d76acc6ead919db625c6fc6b005231df94a3bd430cf0d0d0d84e4",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "1d1c1966af8d627414229dd66d5337918f04e8dd1bf7749e8745a6f67d3c46f8",
    "source_lines": "L684-L687",
    "source_section": "28. Business Decisions (Locked) > BD-11-012"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-11-012",
  "title": "Support sử dụng Consent Based Data Access",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-013 — Feature Request là Business Capability của Platform

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-013-AC001",
      "given": "the applicable business context, actor, and input for Feature Request là Business Capability của Platform",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-013-O001"
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
        "BD-11-013-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-013-O001",
      "obligation_text": "Feature Request là Business Capability của Platform"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Feature Request là Business Capability của Platform.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Feature Request",
    "source_context_sha256": "b436f55bd70f4c1a97682da99f82fd0303c73e194b963b4dc454c1b436c8a6f3",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "e6790de2ef3a28be293063e56f9735e5022eae894e34e769a070258c1b32d0a1",
    "source_lines": "L690-L693",
    "source_section": "28. Business Decisions (Locked) > BD-11-013"
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
  "stable_id": "BD-11-013",
  "title": "Feature Request là Business Capability của Platform",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-014 — Version 2.0 triển khai Auto Translation. AI Customer Support được giữ chỗ

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-014-AC001",
      "given": "the applicable business context, actor, and input for Version 2.0 triển khai Auto Translation. AI Customer Support được giữ chỗ",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-014-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-11-014-AC002",
      "given": "the applicable business context, actor, and input for Version 2.0 triển khai Auto Translation. AI Customer Support được giữ chỗ",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-11-014-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-11-014-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Version 2.0 triển khai Auto Translation. AI Customer Support được giữ chỗ",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-11-014-O001",
        "BD-11-014-O002"
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
        "BD-11-014-AC001",
        "BD-11-014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-014-O001",
      "obligation_text": "Version 2.0 triển khai Auto Translation"
    },
    {
      "acceptance_criterion_references": [
        "BD-11-014-AC002",
        "BD-11-014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-014-O002",
      "obligation_text": "AI Customer Support được giữ chỗ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Version 2.0 triển khai Auto Translation. AI Customer Support được giữ chỗ.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008",
      "P2-DEC-010"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-014",
    "source_context_sha256": "be16150cdac5e1af4dc76dd0fe7bd066913d50b895f3dd61f9ab1212324ba1a6",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "88cc36f91e728d29e24d38e276deed7a73929f5b456a658b7694ef1bc01bdc2b",
    "source_lines": "L696-L701",
    "source_section": "28. Business Decisions (Locked) > BD-11-014"
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
  "stable_id": "BD-11-014",
  "title": "Version 2.0 triển khai Auto Translation. AI Customer Support được giữ chỗ",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-015 — Customer Timeline và WebRTC Customer Portal được giữ chỗ cho phiên bản sau

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
  "normative_statement": "Customer Timeline và WebRTC Customer Portal được giữ chỗ cho phiên bản sau.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-015",
    "source_context_sha256": "25bee1d1c16864501db07b5891ed4a215c2fcbe2c1b83e9937d7d690bfc86403",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "a4f571f234982cc33ff119d6513b593d8c81e53154af81d832e9b7ccc82061cc",
    "source_lines": "L704-L707",
    "source_section": "28. Business Decisions (Locked) > BD-11-015"
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
  "stable_id": "BD-11-015",
  "title": "Customer Timeline và WebRTC Customer Portal được giữ chỗ cho phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R001 — Lifecycle được thiết kế mở để mở rộng trong các phiên bản sau

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
  "normative_statement": "Lifecycle được thiết kế mở để mở rộng trong các phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-001",
    "previous_temporary_key": "TMP-BRD-WS-11-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Customer Lifecycle",
    "source_context_sha256": "d839226d833de8be1f4fa7c4ef837dab8d7131772336c8d6b507021a40d4357b",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "919c286d8f34027e37ce750b513b0865d52427e6526ffcc508229c579e9e7b80",
    "source_lines": "L98",
    "source_section": "3. Customer Lifecycle"
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
  "stable_id": "BRD-WS-11-R001",
  "title": "Lifecycle được thiết kế mở để mở rộng trong các phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R002 — Customer Identity luôn thuộc YSim

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-WS-11-R002-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Customer Identity luôn thuộc YSim",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-WS-11-R002-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BRD-WS-11-R002-AC002",
      "given": "a proposed change with missing traceability or a boundary violation under Customer Identity luôn thuộc YSim",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BRD-WS-11-R002-O001"
      ],
      "when": "design conformance is reviewed"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-11-R002-AC001",
        "BRD-WS-11-R002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R002-O001",
      "obligation_text": "Customer Identity luôn thuộc YSim"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-11-R002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-11-R002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-11-R002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-11-R002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-11-R002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-11-R002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-021",
      "selected_disposition": "CONFIRM_CRITICAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Identity luôn thuộc YSim.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-002",
    "previous_temporary_key": "TMP-BRD-WS-11-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Enterprise Customer Principle",
    "source_context_sha256": "cfa9fa544137f2b7842d75f211e25bfbee6947004cc59ba6b21a3c2a6dea4f8b",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "a2a8c12f1b01f70ea27bee878874489bf37b80a4d48ec3e7102ffa7e0317c556",
    "source_lines": "L108",
    "source_section": "4. Enterprise Customer Principle"
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
  "stable_id": "BRD-WS-11-R002",
  "title": "Customer Identity luôn thuộc YSim",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R003 — Organization chỉ được cấp quyền quản lý Relationship

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-WS-11-R003-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Organization chỉ được cấp quyền quản lý Relationship",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BRD-WS-11-R003-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BRD-WS-11-R003-AC002",
      "given": "a proposed change with missing traceability or a boundary violation under Organization chỉ được cấp quyền quản lý Relationship",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BRD-WS-11-R003-O001"
      ],
      "when": "design conformance is reviewed"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-11-R003-AC003",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Organization chỉ được cấp quyền quản lý Relationship",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-11-R003-O001"
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
        "BRD-WS-11-R003-AC001",
        "BRD-WS-11-R003-AC002",
        "BRD-WS-11-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R003-O001",
      "obligation_text": "Organization chỉ được cấp quyền quản lý Relationship"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-11-R003-AC003"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-11-R003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-11-R003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-11-R003 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-11-R003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-11-R003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "CRITICALITY_RULE_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-022",
      "selected_disposition": "CONFIRM_CRITICAL"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization chỉ được cấp quyền quản lý Relationship.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-003",
    "previous_temporary_key": "TMP-BRD-WS-11-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Enterprise Customer Principle",
    "source_context_sha256": "cfa9fa544137f2b7842d75f211e25bfbee6947004cc59ba6b21a3c2a6dea4f8b",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "d3e7dc2818ea7c66f717446a5a6b87bf5b6c298dbc7b7c2ede1251b1ed2191d2",
    "source_lines": "L110",
    "source_section": "4. Enterprise Customer Principle"
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
  "stable_id": "BRD-WS-11-R003",
  "title": "Organization chỉ được cấp quyền quản lý Relationship",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R004 — Ticket luôn lưu: - Source

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-11-R004-AC001",
      "given": "the applicable business context, actor, and input for Ticket luôn lưu: - Source",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-11-R004-O001"
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
        "BRD-WS-11-R004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R004-O001",
      "obligation_text": "Ticket luôn lưu: - Source"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Ticket luôn lưu: - Source",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-004",
    "previous_temporary_key": "TMP-BRD-WS-11-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Ticket Management",
    "source_context_sha256": "7b4c9a0e09dcd84b0017631e492be206e60efcdfcdfb9e128a03aefbf4507437",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "9140047fe5091d1572ad2617eec30554bc2aeae94e75e00c3a44be280c9c01b1",
    "source_lines": "L236-L238",
    "source_section": "8. Ticket Management"
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
  "stable_id": "BRD-WS-11-R004",
  "title": "Ticket luôn lưu: - Source",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R005 — Ticket luôn lưu: - Creator

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-11-R005-AC001",
      "given": "the applicable business context, actor, and input for Ticket luôn lưu: - Creator",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-11-R005-O001"
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
        "BRD-WS-11-R005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R005-O001",
      "obligation_text": "Ticket luôn lưu: - Creator"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Ticket luôn lưu: - Creator",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-005",
    "previous_temporary_key": "TMP-BRD-WS-11-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Ticket Management",
    "source_context_sha256": "7b4c9a0e09dcd84b0017631e492be206e60efcdfcdfb9e128a03aefbf4507437",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "993a6ccd604c5a1bd035bb494b7a1300c5a931c208be9996a950007566fe61b2",
    "source_lines": "L236-L239",
    "source_section": "8. Ticket Management"
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
  "stable_id": "BRD-WS-11-R005",
  "title": "Ticket luôn lưu: - Creator",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R006 — Ticket luôn lưu: - Owner

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-11-R006-AC001",
      "given": "the applicable business context, actor, and input for Ticket luôn lưu: - Owner",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-11-R006-O001"
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
        "BRD-WS-11-R006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R006-O001",
      "obligation_text": "Ticket luôn lưu: - Owner"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Ticket luôn lưu: - Owner",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-006",
    "previous_temporary_key": "TMP-BRD-WS-11-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Ticket Management",
    "source_context_sha256": "7b4c9a0e09dcd84b0017631e492be206e60efcdfcdfb9e128a03aefbf4507437",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "9bbbb5a43a6d8807122bbf7b7131b344f86da98d637fad207f707ab48cb1a78c",
    "source_lines": "L236-L240",
    "source_section": "8. Ticket Management"
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
  "stable_id": "BRD-WS-11-R006",
  "title": "Ticket luôn lưu: - Owner",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R007 — Supplier Case luôn được YSim Staff theo dõi

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-11-R007-AC001",
      "given": "the applicable business context, actor, and input for Supplier Case luôn được YSim Staff theo dõi",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-11-R007-O001"
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
        "BRD-WS-11-R007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R007-O001",
      "obligation_text": "Supplier Case luôn được YSim Staff theo dõi"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Supplier Case luôn được YSim Staff theo dõi.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-007",
    "previous_temporary_key": "TMP-BRD-WS-11-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Escalation",
    "source_context_sha256": "0ba80de2bfecde2d441e53cad68ca849f9f14fe818e96aae1bb75b9aa8287500",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "3da6724c89e641752b6041e9aaca12f54a7ac171d32c773f89675d84252fa009",
    "source_lines": "L389",
    "source_section": "15. Escalation"
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
  "stable_id": "BRD-WS-11-R007",
  "title": "Supplier Case luôn được YSim Staff theo dõi",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R008 — Được thiết kế mở để mở rộng trong các phiên bản sau

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
  "normative_statement": "Được thiết kế mở để mở rộng trong các phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-008",
    "previous_temporary_key": "TMP-BRD-WS-11-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Troubleshooting Wizard",
    "source_context_sha256": "e5cb123717d7964399535259d5bb35b4980897efeb62b8fa750739cdb8e8035a",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "f6d53e58f387de89950fd9e67809fe13ddbace905228d73c93428c15bdc27e9e",
    "source_lines": "L420",
    "source_section": "17. Troubleshooting Wizard"
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
  "stable_id": "BRD-WS-11-R008",
  "title": "Được thiết kế mở để mở rộng trong các phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R009 — Có thể cấu hình: - Always - Random - Disabled

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-11-R009-AC001",
      "given": "the applicable business context, actor, and input for Có thể cấu hình: - Always - Random - Disabled",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-11-R009-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-11-R009-AC002",
      "given": "the applicable business context, actor, and input for Có thể cấu hình: - Always - Random - Disabled",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-11-R009-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-11-R009-AC003",
      "given": "the applicable business context, actor, and input for Có thể cấu hình: - Always - Random - Disabled",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-11-R009-O003"
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
        "BRD-WS-11-R009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R009-O001",
      "obligation_text": "Có thể cấu hình: Always."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-11-R009-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R009-O002",
      "obligation_text": "Có thể cấu hình: Random."
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-11-R009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R009-O003",
      "obligation_text": "Có thể cấu hình: Disabled."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Có thể cấu hình: - Always - Random - Disabled",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-009",
    "previous_temporary_key": "TMP-BRD-WS-11-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Satisfaction Survey",
    "source_context_sha256": "8806162cf1df0bbf7231cb5413e25279dd62867ba20c94ebb0d0709dc704c235",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "b76ca46f932582704b3dc1e2c4ca890dc1e68b40a6d850e7dbe25f900859eb5d",
    "source_lines": "L488-L492",
    "source_section": "20. Satisfaction Survey"
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
  "stable_id": "BRD-WS-11-R009",
  "title": "Có thể cấu hình: - Always - Random - Disabled",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R010 — Attachment của Customer Support Ticket không hỗ trợ Video trong v2.3

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "EXCLUDED_FROM_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Attachment của Customer Support Ticket không hỗ trợ Video trong v2.3.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-010",
    "previous_temporary_key": "TMP-BRD-WS-11-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "50e82988ceb8b2081f6e29bdde5d67407e0528ab218b37d7027cde21c04748ed",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "c966fc046f6deb715dfaf84e5b00eaddac97b3edff992d5152ba2a8fdc812028",
    "source_lines": "L541-L550",
    "source_section": "24. Attachment"
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
  "scope_status": "OUT_OF_SCOPE",
  "stable_id": "BRD-WS-11-R010",
  "title": "Attachment của Customer Support Ticket không hỗ trợ Video trong v2.3",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R011 — AI Customer Support được giữ chỗ cho phiên bản sau

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
  "normative_statement": "AI Customer Support được giữ chỗ cho phiên bản sau.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-011",
    "previous_temporary_key": "TMP-BRD-WS-11-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "26. AI & Translation",
    "source_context_sha256": "b5da41892d1bccc8c1dd849d101b4c687ac3da6e8c6a3a867d1b1503c5826d87",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "73c4feb3a06ddd6d7ce8238f4950aafc5b82c034013ed888fc1d46b6ccd4293f",
    "source_lines": "L592",
    "source_section": "26. AI & Translation"
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
  "stable_id": "BRD-WS-11-R011",
  "title": "AI Customer Support được giữ chỗ cho phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R012 — Giữ chỗ cho các Capability: - Customer Timeline

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
  "normative_statement": "Giữ chỗ cho các Capability: - Customer Timeline",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-012",
    "previous_temporary_key": "TMP-BRD-WS-11-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Future Capability",
    "source_context_sha256": "00343bcfac7b2991460da2a67b2b5aa50f513da8cc4544c72b587f39666ba129",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "b083a8d89f7a333c09fe00bb68a222c742d49c3b959ae6f8bfc732ed1771311a",
    "source_lines": "L598-L600",
    "source_section": "27. Future Capability"
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
  "stable_id": "BRD-WS-11-R012",
  "title": "Giữ chỗ cho các Capability: - Customer Timeline",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R013 — Giữ chỗ cho các Capability: - WebRTC Call trên Customer Portal

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
  "normative_statement": "Giữ chỗ cho các Capability: - WebRTC Call trên Customer Portal",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-013",
    "previous_temporary_key": "TMP-BRD-WS-11-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Future Capability",
    "source_context_sha256": "00343bcfac7b2991460da2a67b2b5aa50f513da8cc4544c72b587f39666ba129",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "ebcd2947652a234ad943bce8ea5c72d9823e94b7bb500161c63675beda586d8b",
    "source_lines": "L598-L601",
    "source_section": "27. Future Capability"
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
  "stable_id": "BRD-WS-11-R013",
  "title": "Giữ chỗ cho các Capability: - WebRTC Call trên Customer Portal",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R014 — Giữ chỗ cho các Capability: - AI Customer Support

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
  "normative_statement": "Giữ chỗ cho các Capability: - AI Customer Support",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-014",
    "previous_temporary_key": "TMP-BRD-WS-11-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Future Capability",
    "source_context_sha256": "00343bcfac7b2991460da2a67b2b5aa50f513da8cc4544c72b587f39666ba129",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "9f8968ee10a2c1a85a210de34dd4a8c7ca2b6b155cd9f9dea3dcf411902e4d8e",
    "source_lines": "L598-L602",
    "source_section": "27. Future Capability"
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
  "stable_id": "BRD-WS-11-R014",
  "title": "Giữ chỗ cho các Capability: - AI Customer Support",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R015 — Giữ chỗ cho các Capability: - Voice Bot

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
  "normative_statement": "Giữ chỗ cho các Capability: - Voice Bot",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-015",
    "previous_temporary_key": "TMP-BRD-WS-11-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Future Capability",
    "source_context_sha256": "00343bcfac7b2991460da2a67b2b5aa50f513da8cc4544c72b587f39666ba129",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "7b18f9ff39c2d0e484c74bb1088dbc871f294c48598341cce372fa7b2372923a",
    "source_lines": "L598-L603",
    "source_section": "27. Future Capability"
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
  "stable_id": "BRD-WS-11-R015",
  "title": "Giữ chỗ cho các Capability: - Voice Bot",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R016 — Giữ chỗ cho các Capability: - Chat Bot

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
  "normative_statement": "Giữ chỗ cho các Capability: - Chat Bot",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-016",
    "previous_temporary_key": "TMP-BRD-WS-11-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Future Capability",
    "source_context_sha256": "00343bcfac7b2991460da2a67b2b5aa50f513da8cc4544c72b587f39666ba129",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "03e2624d984da46f32e14996d552c6f19791b550b30da950bffcfe3a2e9dd1b1",
    "source_lines": "L598-L604",
    "source_section": "27. Future Capability"
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
  "stable_id": "BRD-WS-11-R016",
  "title": "Giữ chỗ cho các Capability: - Chat Bot",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R017 — WebRTC chỉ được kích hoạt khi Customer chủ động sử dụng

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
  "normative_statement": "WebRTC chỉ được kích hoạt khi Customer chủ động sử dụng.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-017",
    "previous_temporary_key": "TMP-BRD-WS-11-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Future Capability",
    "source_context_sha256": "00343bcfac7b2991460da2a67b2b5aa50f513da8cc4544c72b587f39666ba129",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "869079b684d009dce5ff1052db137de3d82bdc0ba880fd1b67d1ec3ea20998b1",
    "source_lines": "L606",
    "source_section": "27. Future Capability"
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
  "stable_id": "BRD-WS-11-R017",
  "title": "WebRTC chỉ được kích hoạt khi Customer chủ động sử dụng",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-11-001 — Customer Portal là điểm truy cập thống nhất trong toàn bộ Customer Lifecycle

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-11-001-AC001",
      "given": "the applicable business context, actor, and input for Customer Portal là điểm truy cập thống nhất trong toàn bộ Customer Lifecycle",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-11-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-11-001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Customer Portal là điểm truy cập thống nhất trong toàn bộ Customer Lifecycle",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-11-001-O001"
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
        "EP-11-001-AC001",
        "EP-11-001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-11-001-O001",
      "obligation_text": "Customer Portal là điểm truy cập thống nhất trong toàn bộ Customer Lifecycle"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Portal là điểm truy cập thống nhất trong toàn bộ Customer Lifecycle.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-11-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-11-001",
    "source_context_sha256": "2bab1ff8de2e2ff3dc37e08c14561b08afdae4ff9632c3c087b420bd5089d901",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "77d0721560e731e96839b761924ddbf0ebc3421f06432c372a46a2cb8e520784",
    "source_lines": "L712-L715",
    "source_section": "29. Enterprise Design Principles > EP-11-001"
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
  "stable_id": "EP-11-001",
  "title": "Customer Portal là điểm truy cập thống nhất trong toàn bộ Customer Lifecycle",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-11-002 — Customer Identity và Customer Relationship được tách biệt

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-11-002-AC001",
      "given": "the applicable business context, actor, and input for Customer Identity và Customer Relationship được tách biệt",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "EP-11-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-11-002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Customer Identity và Customer Relationship được tách biệt",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-11-002-O001"
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
        "EP-11-002-AC001",
        "EP-11-002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-11-002-O001",
      "obligation_text": "Customer Identity và Customer Relationship được tách biệt"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-11-002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-11-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-11-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EP-11-002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-11-002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-11-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Identity và Customer Relationship được tách biệt.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-11-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-11-002",
    "source_context_sha256": "cd6d5f521ccee7a970107ab31c30a02e6b894682fe1cceedaf6c54fba168db38",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
    "source_lines": "L718-L721",
    "source_section": "29. Enterprise Design Principles > EP-11-002"
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
  "stable_id": "EP-11-002",
  "title": "Customer Identity và Customer Relationship được tách biệt",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-11-003 — Support Routing dựa trên Capability, không dựa trên cấu trúc tổ chức cố định

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-11-003-AC001",
      "given": "the applicable business context, actor, and input for Support Routing dựa trên Capability, không dựa trên cấu trúc tổ chức cố định",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-11-003-O001"
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
        "EP-11-003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-11-003-O001",
      "obligation_text": "Support Routing dựa trên Capability, không dựa trên cấu trúc tổ chức cố định"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Support Routing dựa trên Capability, không dựa trên cấu trúc tổ chức cố định.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-11-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-11-003",
    "source_context_sha256": "ba269611c57250000df7282fd01d7ecd69888325485250301412c1f266dffbc1",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "b0b7583541188d8a83208f9b9abe78109a278472e0b1af7d15e19e944be1dc3d",
    "source_lines": "L724-L727",
    "source_section": "29. Enterprise Design Principles > EP-11-003"
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
  "stable_id": "EP-11-003",
  "title": "Support Routing dựa trên Capability, không dựa trên cấu trúc tổ chức cố định",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-11-004 — Reference Data được quản lý tập trung

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-11-004-AC001",
      "given": "the applicable business context, actor, and input for Reference Data được quản lý tập trung",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-11-004-O001"
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
        "EP-11-004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-11-004-O001",
      "obligation_text": "Reference Data được quản lý tập trung"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Reference Data được quản lý tập trung.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-11-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-11-004",
    "source_context_sha256": "9dd5a6988dc831f14c6e868982ddf375a213ba9b310b6e574a03b74b61b9a9dd",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "761ee9f49129db0366e1ecb9435285ff8cf3b7e8d6fea80d99951d352ebd4878",
    "source_lines": "L730-L733",
    "source_section": "29. Enterprise Design Principles > EP-11-004"
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
  "stable_id": "EP-11-004",
  "title": "Reference Data được quản lý tập trung",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-11-005 — Knowledge Management hỗ trợ tái sử dụng nội dung giữa KB, FAQ và Troubleshooting Wizard

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-11-005-AC001",
      "given": "the applicable business context, actor, and input for Knowledge Management hỗ trợ tái sử dụng nội dung giữa KB, FAQ và Troubleshooting Wizard",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-11-005-O001"
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
        "EP-11-005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-11-005-O001",
      "obligation_text": "Knowledge Management hỗ trợ tái sử dụng nội dung giữa KB, FAQ và Troubleshooting Wizard"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Knowledge Management hỗ trợ tái sử dụng nội dung giữa KB, FAQ và Troubleshooting Wizard.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-11-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-11-005",
    "source_context_sha256": "2052bf07c6375849c66a1590eb4132772df46b56ef4146feeeb6aaf979374923",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "1305a60b48eea00a89c932d553166d26e7b01a3dc4e4d502d1e0e15a1706efe9",
    "source_lines": "L736-L739",
    "source_section": "29. Enterprise Design Principles > EP-11-005"
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
  "stable_id": "EP-11-005",
  "title": "Knowledge Management hỗ trợ tái sử dụng nội dung giữa KB, FAQ và Troubleshooting Wizard",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-11-006 — Customer Privacy tuân thủ Consent Based Data Access

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-11-006-AC001",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Customer Privacy tuân thủ Consent Based Data Access",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-11-006-O001"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "PRIVACY_POLICY_DENIAL_V1",
      "criterion_id": "EP-11-006-AC002",
      "given": "a data action whose purpose, consent, scope, or effective policy does not permit the requested data use under Customer Privacy tuân thủ Consent Based Data Access",
      "observable_evidence": "actor, purpose, consent and scope, effective policies, denial reason, exposed-data comparison, and audit record",
      "then": "the data action is denied, no additional protected data is exposed or changed, and the policy reason is audited",
      "verifies": [
        "EP-11-006-O001"
      ],
      "when": "privacy conformance is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-11-006-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Customer Privacy tuân thủ Consent Based Data Access",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-11-006-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "EP-11-006-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Customer Privacy tuân thủ Consent Based Data Access",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "EP-11-006-O001"
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
        "EP-11-006-AC001",
        "EP-11-006-AC002",
        "EP-11-006-AC003",
        "EP-11-006-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-11-006-O001",
      "obligation_text": "Customer Privacy tuân thủ Consent Based Data Access"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "EP-11-006-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-11-006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-11-006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-11-006-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-11-006-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-11-006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Privacy tuân thủ Consent Based Data Access.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-11-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-11-006",
    "source_context_sha256": "6e981331f4e2dd452b1d1b2440f7c9aa234375b9299eb5a2ff925408c33af4c8",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "b6ce395b1e9d9f89e2f9da3f83208258f1a10d8abdbea154897ba1f6453475a4",
    "source_lines": "L742-L745",
    "source_section": "29. Enterprise Design Principles > EP-11-006"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-11-006",
  "title": "Customer Privacy tuân thủ Consent Based Data Access",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-11-007 — Feature Request là một phần của Customer Success Lifecycle

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-11-007-AC001",
      "given": "the applicable business context, actor, and input for Feature Request là một phần của Customer Success Lifecycle",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-11-007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-11-007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Feature Request là một phần của Customer Success Lifecycle",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-11-007-O001"
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
        "EP-11-007-AC001",
        "EP-11-007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-11-007-O001",
      "obligation_text": "Feature Request là một phần của Customer Success Lifecycle"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Feature Request là một phần của Customer Success Lifecycle.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-11-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-11-007",
    "source_context_sha256": "033d855c8d19c2a9a5b1a8f8476f5c8279dd79456c1d0ac2a5194d6008b02c99",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "6701b7f4cce5fde663e6e94bcb94ba9801bd9176c75031a5bc8a06c988273eed",
    "source_lines": "L748-L751",
    "source_section": "29. Enterprise Design Principles > EP-11-007"
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
  "stable_id": "EP-11-007",
  "title": "Feature Request là một phần của Customer Success Lifecycle",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
