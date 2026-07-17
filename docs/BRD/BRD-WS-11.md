---
document_code: "BRD-WS-11"
document_id: "BRD-WS-11"
title: "Customer Service, Ticketing & Customer Lifecycle"
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

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-001 — Customer Portal là Capability thống nhất của Customer

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005",
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-11-001",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "48a401e66d3c261871c1fc064969928736a829122b84513d4c6a37e16ae37777"
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
        "BD-11-001-AC001",
        "BD-11-001-AC002",
        "BD-11-001-AC003"
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
    "source_fingerprint": "48a401e66d3c261871c1fc064969928736a829122b84513d4c6a37e16ae37777",
    "source_lines": "L832-L913",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-001"
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
      "requirement_id": "BD-11-002",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "597327ba51312eea6fee51c814a779122af1bb903b2e4dd7aba8f3cf7c669adc"
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
        "BD-11-002-AC001",
        "BD-11-002-AC003",
        "BD-11-002-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-002-O001",
      "obligation_text": "Customer Identity thuộc Platform"
    },
    {
      "acceptance_criterion_references": [
        "BD-11-002-AC002",
        "BD-11-002-AC003",
        "BD-11-002-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-002-O002",
      "obligation_text": "Customer Relationship thuộc Organization"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-11-002-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-11-002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-11-002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-11-002-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-11-002-AC001",
        "BD-11-002-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-11-002 does not define a recovery obligation."
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
    "source_fingerprint": "597327ba51312eea6fee51c814a779122af1bb903b2e4dd7aba8f3cf7c669adc",
    "source_lines": "L915-L1040",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-11-003",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "b846e1a708ccfe7c56039a9fcf8dde75137b588d666e8a647956bc727ce5a9e8"
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
        "BD-11-003-AC001",
        "BD-11-003-AC002",
        "BD-11-003-AC003"
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
    "source_fingerprint": "b846e1a708ccfe7c56039a9fcf8dde75137b588d666e8a647956bc727ce5a9e8",
    "source_lines": "L1042-L1117",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-11-004",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "50d105a5e7e903cd3c52d35ffe0185ad34bcb935fed10479f225c518888908c0"
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
        "BD-11-004-AC001",
        "BD-11-004-AC002",
        "BD-11-004-AC003"
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
    "source_fingerprint": "50d105a5e7e903cd3c52d35ffe0185ad34bcb935fed10479f225c518888908c0",
    "source_lines": "L1119-L1194",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-11-005",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "18be755155bea32ed1d2a7694f7115b0d8681e2bbcba5e004d8b53dd810d62d8"
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
        "BD-11-005-AC001",
        "BD-11-005-AC002",
        "BD-11-005-AC003"
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
    "source_fingerprint": "18be755155bea32ed1d2a7694f7115b0d8681e2bbcba5e004d8b53dd810d62d8",
    "source_lines": "L1196-L1275",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-11-006",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "355fbae56739bcac3e233763b9c0a06ba591d6aa58f0ae522ed2cad348b91776"
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
        "BD-11-006-AC001",
        "BD-11-006-AC004",
        "BD-11-006-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-006-O001",
      "obligation_text": "Support Policy gồm: SELF_SUPPORT"
    },
    {
      "acceptance_criterion_references": [
        "BD-11-006-AC002",
        "BD-11-006-AC004",
        "BD-11-006-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-006-O002",
      "obligation_text": "Support Policy gồm: PARENT_SUPPORT"
    },
    {
      "acceptance_criterion_references": [
        "BD-11-006-AC003",
        "BD-11-006-AC004",
        "BD-11-006-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-006-O003",
      "obligation_text": "Support Policy gồm: HYBRID"
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
    "source_fingerprint": "355fbae56739bcac3e233763b9c0a06ba591d6aa58f0ae522ed2cad348b91776",
    "source_lines": "L1277-L1372",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-006"
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
      "requirement_id": "BD-11-007",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "e5d2a2f4d2baff85b49ee5ac27617a8b876b6b4b7f769aecc25062b4ee20cfcb"
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
        "BD-11-007-AC001",
        "BD-11-007-AC002",
        "BD-11-007-AC003"
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
    "source_fingerprint": "e5d2a2f4d2baff85b49ee5ac27617a8b876b6b4b7f769aecc25062b4ee20cfcb",
    "source_lines": "L1374-L1453",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-11-008",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "0e9c49186c7bf8b8672792ec69c13f27f3ea444fe04c55d553587490ec94d120"
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
        "BD-11-008-AC001",
        "BD-11-008-AC002",
        "BD-11-008-AC003"
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
    "source_fingerprint": "0e9c49186c7bf8b8672792ec69c13f27f3ea444fe04c55d553587490ec94d120",
    "source_lines": "L1455-L1534",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-11-009",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "cbc194eab390da9ea03cba85ed5b212f1907ac14b425047432da80e00e5feb78"
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
        "BD-11-009-AC001",
        "BD-11-009-AC002",
        "BD-11-009-AC003"
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
    "source_fingerprint": "cbc194eab390da9ea03cba85ed5b212f1907ac14b425047432da80e00e5feb78",
    "source_lines": "L1536-L1615",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-009"
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
      "requirement_id": "BD-11-010",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "f239c38b49f990ec987dd74f56196ef3736b5457164cdf92536d920505e828ae"
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
        "BD-11-010-AC001",
        "BD-11-010-AC002",
        "BD-11-010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-11-010-O001",
      "obligation_text": "Customer Feedback hỗ trợ nhiều nguồn"
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
    "source_fingerprint": "f239c38b49f990ec987dd74f56196ef3736b5457164cdf92536d920505e828ae",
    "source_lines": "L1617-L1696",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-11-011",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "95874d4947b5938cf4e3a11e3ca40e21041831a8dcda2e17550d0c90c3c962c5"
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
        "BD-11-011-AC001",
        "BD-11-011-AC002",
        "BD-11-011-AC003"
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
    "source_fingerprint": "95874d4947b5938cf4e3a11e3ca40e21041831a8dcda2e17550d0c90c3c962c5",
    "source_lines": "L1698-L1773",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-011"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-11-012",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "d8a0fb4b9c208f4a5d3dbe9f7ddeca7f0a602928fb2f14553002982cb12775f8"
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
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-11-012-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-11-012 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-11-012 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-11-012-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-11-012-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-11-012 does not define a recovery obligation."
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
    "source_fingerprint": "d8a0fb4b9c208f4a5d3dbe9f7ddeca7f0a602928fb2f14553002982cb12775f8",
    "source_lines": "L1775-L1885",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-012"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-11-013",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "eb873db4c8d104ad1a3d8c9d3eeb7ede69e1a3d0d909370f81843da9e486f89a"
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
        "BD-11-013-AC001",
        "BD-11-013-AC002",
        "BD-11-013-AC003"
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
    "source_fingerprint": "eb873db4c8d104ad1a3d8c9d3eeb7ede69e1a3d0d909370f81843da9e486f89a",
    "source_lines": "L1887-L1966",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-013"
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
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "Composite parent coverage is satisfied only through ALL_CHILDREN; the parent is not an implementation, acceptance, scope-coverage, or criticality unit.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Version 2.0 triển khai Auto Translation. AI Customer Support được giữ chỗ.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008",
      "P2-DEC-010",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-11-014",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-014",
    "source_context_sha256": "be16150cdac5e1af4dc76dd0fe7bd066913d50b895f3dd61f9ab1212324ba1a6",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "a0176a2063826c369797ce45e2e1e689c841327bb8a94a78cab819c54ee4d1c6",
    "source_fingerprint_before_c3": "88cc36f91e728d29e24d38e276deed7a73929f5b456a658b7694ef1bc01bdc2b",
    "source_lines": "L1968-L2029",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-014"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-11-R018",
      "BRD-WS-11-R019"
    ]
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-11-014",
  "title": "Version 2.0 triển khai Auto Translation. AI Customer Support được giữ chỗ",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-11-015 — Customer Timeline và WebRTC Customer Portal được giữ chỗ cho phiên bản sau

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BD-11-015",
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
    "source_fingerprint": "895f1480dda6aeeb2c47bd909b1367f5da6aa7edbc0b9ad58208c6cf0a84bd94",
    "source_lines": "L2031-L2091",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-11-015"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-11-R001",
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
    "source_lines": "L2093-L2151",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R001"
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
### BRD-WS-11-R002 — Customer Identity là canonical identity record do YSim Platform quản lý; điều này không xác lập …

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-11-R002",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "9d0904dfb3fa582b15f6d912c86920a8afbfb57be5785195b0bf0860a20746dc"
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
        "BRD-WS-11-R002-AC001",
        "BRD-WS-11-R002-AC003",
        "BRD-WS-11-R002-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R002-O001",
      "obligation_text": "Customer Identity là canonical identity record do YSim Platform quản lý"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-11-R002-AC002",
        "BRD-WS-11-R002-AC003",
        "BRD-WS-11-R002-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R002-O002",
      "obligation_text": "điều này không xác lập quyền sở hữu pháp lý dữ liệu cá nhân, và Organization chỉ được truy cập, quản lý trong phạm vi relationship, consent, purpose, policy và jurisdiction được phép"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-11-R002-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-11-R002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-11-R002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-11-R002-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-11-R002-AC001",
        "BRD-WS-11-R002-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-11-R002 does not define a recovery obligation."
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
  "normative_statement": "Customer Identity là canonical identity record do YSim Platform quản lý; điều này không xác lập quyền sở hữu pháp lý dữ liệu cá nhân, và Organization chỉ được truy cập, quản lý trong phạm vi relationship, consent, purpose, policy và jurisdiction được phép.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-002",
    "phase_2c_c3_actions": [
      "C3_APPROVED_SEMANTIC_DIRECTIVE"
    ],
    "previous_temporary_key": "TMP-BRD-WS-11-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Enterprise Customer Principle",
    "source_context_sha256": "cfa9fa544137f2b7842d75f211e25bfbee6947004cc59ba6b21a3c2a6dea4f8b",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "9d0904dfb3fa582b15f6d912c86920a8afbfb57be5785195b0bf0860a20746dc",
    "source_fingerprint_before_c3": "a2a8c12f1b01f70ea27bee878874489bf37b80a4d48ec3e7102ffa7e0317c556",
    "source_lines": "L2153-L2295",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R002"
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
  "title": "Customer Identity là canonical identity record do YSim Platform quản lý; điều này không xác lập …",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R003 — Organization chỉ được quản lý Organization-scoped Customer Relationship và dữ liệu hoặc quyền đư…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-11-R003",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "8b014a3a00a1e523fcfdc825c69d163ace56d18cdbcf1d1e42e40858e701bf25"
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
        "BRD-WS-11-R003-AC001",
        "BRD-WS-11-R003-AC003",
        "BRD-WS-11-R003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R003-O001",
      "obligation_text": "Organization chỉ được quản lý Organization-scoped Customer Relationship và dữ liệu hoặc quyền được cấp trong relationship đó"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-11-R003-AC002",
        "BRD-WS-11-R003-AC003",
        "BRD-WS-11-R003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R003-O002",
      "obligation_text": "Organization không được chiếm quyền sở hữu, hợp nhất hoặc sửa canonical Customer Identity ngoài policy được phép"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-11-R003-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-11-R003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-11-R003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-11-R003-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-11-R003-AC001",
        "BRD-WS-11-R003-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-11-R003 does not define a recovery obligation."
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
  "normative_statement": "Organization chỉ được quản lý Organization-scoped Customer Relationship và dữ liệu hoặc quyền được cấp trong relationship đó; Organization không được chiếm quyền sở hữu, hợp nhất hoặc sửa canonical Customer Identity ngoài policy được phép.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-11-003",
    "phase_2c_c3_actions": [
      "C3_APPROVED_SEMANTIC_DIRECTIVE"
    ],
    "previous_temporary_key": "TMP-BRD-WS-11-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "4. Enterprise Customer Principle",
    "source_context_sha256": "cfa9fa544137f2b7842d75f211e25bfbee6947004cc59ba6b21a3c2a6dea4f8b",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "8b014a3a00a1e523fcfdc825c69d163ace56d18cdbcf1d1e42e40858e701bf25",
    "source_fingerprint_before_c3": "d3e7dc2818ea7c66f717446a5a6b87bf5b6c298dbc7b7c2ede1251b1ed2191d2",
    "source_lines": "L2297-L2437",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R003"
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
  "title": "Organization chỉ được quản lý Organization-scoped Customer Relationship và dữ liệu hoặc quyền đư…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R004 — Ticket luôn lưu: - Source

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
      "requirement_id": "BRD-WS-11-R004",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "9140047fe5091d1572ad2617eec30554bc2aeae94e75e00c3a44be280c9c01b1"
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
        "BRD-WS-11-R004-AC001",
        "BRD-WS-11-R004-AC002",
        "BRD-WS-11-R004-AC003"
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
    "source_lines": "L2439-L2514",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-11-R005",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "37f05cd235c2425c4c262a44309a80d9c74cc945eb550dc1c6a5c96604b0849b"
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
        "BRD-WS-11-R005-AC001",
        "BRD-WS-11-R005-AC002",
        "BRD-WS-11-R005-AC003"
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
    "source_fingerprint": "37f05cd235c2425c4c262a44309a80d9c74cc945eb550dc1c6a5c96604b0849b",
    "source_lines": "L2516-L2591",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-11-R006",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "1bf215969b0f478562cf300ea0d6adfa18abdf0ccc49cc4d216a134e6069d8d8"
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
        "BRD-WS-11-R006-AC001",
        "BRD-WS-11-R006-AC002",
        "BRD-WS-11-R006-AC003"
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
    "source_fingerprint": "1bf215969b0f478562cf300ea0d6adfa18abdf0ccc49cc4d216a134e6069d8d8",
    "source_lines": "L2593-L2668",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R006"
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
      "requirement_id": "BRD-WS-11-R007",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "3da6724c89e641752b6041e9aaca12f54a7ac171d32c773f89675d84252fa009"
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
        "BRD-WS-11-R007-AC001",
        "BRD-WS-11-R007-AC002",
        "BRD-WS-11-R007-AC003"
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
    "source_lines": "L2670-L2749",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-11-R008",
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
    "source_lines": "L2751-L2809",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-010",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-11-R009",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "b76ca46f932582704b3dc1e2c4ca890dc1e68b40a6d850e7dbe25f900859eb5d"
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
        "BRD-WS-11-R009-AC001",
        "BRD-WS-11-R009-AC004",
        "BRD-WS-11-R009-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R009-O001",
      "obligation_text": "Có thể cấu hình: Always"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-11-R009-AC002",
        "BRD-WS-11-R009-AC004",
        "BRD-WS-11-R009-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R009-O002",
      "obligation_text": "Có thể cấu hình: Random"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-11-R009-AC003",
        "BRD-WS-11-R009-AC004",
        "BRD-WS-11-R009-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R009-O003",
      "obligation_text": "Có thể cấu hình: Disabled"
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
    "source_lines": "L2811-L2910",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-11-R010",
    "scope_status": "OUT_OF_SCOPE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "Requirement is explicitly outside the v2.3 product scope.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
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
    "source_fingerprint": "50e82988ceb8b2081f6e29bdde5d67407e0528ab218b37d7027cde21c04748ed",
    "source_lines": "L2912-L2972",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-11-R011",
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
    "source_lines": "L2974-L3034",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R011"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-11-R012",
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
    "source_lines": "L3036-L3097",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R012"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-11-R013",
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
    "source_fingerprint": "bf27ecdd9c45ce63ffe2fdb944942b1afbba8986e2df1c6ca1bda2b7cdf65497",
    "source_lines": "L3099-L3160",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R013"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-11-R014",
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
    "source_fingerprint": "109ef5acc89d490738bc738eca27fae5559cbf8a718d2e905e02dbe910a4b9d8",
    "source_lines": "L3162-L3223",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R014"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-11-R015",
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
    "source_fingerprint": "5a591416538c1107d8d2b8e9d6d00f70094de11ad1cfdef098200fe30cd20f29",
    "source_lines": "L3225-L3285",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R015"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-11-R016",
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
    "source_fingerprint": "371048e44d5efd2ea56ef6bee1c91d7e3fddd8d456dc8990d7a6b1fb53966974",
    "source_lines": "L3287-L3347",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R016"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-11-R017",
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
    "source_lines": "L3349-L3409",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R017"
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
### BRD-WS-11-R018 — Version 2.0 triển khai Auto Translation

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "P2-DEC-010",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-11-R018",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "44d6949e417a0053ee360012d7c8bab4a112b5a055d94f57e34a3cd64860f4af"
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
        "BRD-WS-11-R018-AC001",
        "BRD-WS-11-R018-AC002",
        "BRD-WS-11-R018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-11-R018-O001",
      "obligation_text": "Version 2.0 triển khai Auto Translation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Version 2.0 triển khai Auto Translation.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "P2-DEC-010",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-11-014",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-11-R018",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-014",
    "source_context_sha256": "be16150cdac5e1af4dc76dd0fe7bd066913d50b895f3dd61f9ab1212324ba1a6",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "44d6949e417a0053ee360012d7c8bab4a112b5a055d94f57e34a3cd64860f4af",
    "source_fingerprint_before_c3": "44d6949e417a0053ee360012d7c8bab4a112b5a055d94f57e34a3cd64860f4af",
    "source_lines": "L3411-L3507",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R018"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-11-014"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-11-014"
    ]
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-11-R018",
  "title": "Version 2.0 triển khai Auto Translation",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-11-R019 — AI Customer Support được giữ chỗ

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-11-R019",
    "scope_status": "FUTURE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "This record is not an active canonical atomic v2.3 acceptance unit.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "AI Customer Support được giữ chỗ.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "P2-DEC-010",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-11-014",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-11-R019",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-11-014",
    "source_context_sha256": "be16150cdac5e1af4dc76dd0fe7bd066913d50b895f3dd61f9ab1212324ba1a6",
    "source_document": "docs/BRD/BRD-WS-11.md",
    "source_fingerprint": "a3246827a2ff08e2951791ef68b51de7eb5ce1fb5c7d1d1289fe38907f5a5b29",
    "source_fingerprint_before_c3": "a3246827a2ff08e2951791ef68b51de7eb5ce1fb5c7d1d1289fe38907f5a5b29",
    "source_lines": "L3509-L3584",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-11-R019"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-11-014"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-11-014"
    ]
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": false,
  "scope_status": "FUTURE",
  "stable_id": "BRD-WS-11-R019",
  "title": "AI Customer Support được giữ chỗ",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-11-001 — Customer Portal là điểm truy cập thống nhất trong toàn bộ Customer Lifecycle

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
      "requirement_id": "EP-11-001",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "3cc218b893453e30c82dfafa136c91b73db394a2e70dc75065a69fc61af7b4aa"
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
        "EP-11-001-AC001",
        "EP-11-001-AC002",
        "EP-11-001-AC003"
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
    "source_fingerprint": "3cc218b893453e30c82dfafa136c91b73db394a2e70dc75065a69fc61af7b4aa",
    "source_lines": "L3586-L3665",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-11-001"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "A Relationship references Identity without transferring canonical identity authority"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "EP-11-002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                "source_type": "SOURCE_LITERAL",
                "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
              },
              "identifier": "EP-11-002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-11.md",
                "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                "source_lines": "L718-L721",
                "source_section": "29. Enterprise Design Principles > EP-11-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.EP-11-002.EP-11-002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-11.md",
            "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
            "source_lines": "L718-L721",
            "source_section": "29. Enterprise Design Principles > EP-11-002"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "EP-11-002.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                "source_type": "SOURCE_LITERAL",
                "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
              },
              "identifier": "EP-11-002.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-11.md",
                "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                "source_lines": "L718-L721",
                "source_section": "29. Enterprise Design Principles > EP-11-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.EP-11-002.EP-11-002.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-11.md",
            "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
            "source_lines": "L718-L721",
            "source_section": "29. Enterprise Design Principles > EP-11-002"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
            "source_type": "SOURCE_LITERAL",
            "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
          },
          "identifier": "EP-11-002.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-11.md",
            "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
            "source_lines": "L718-L721",
            "source_section": "29. Enterprise Design Principles > EP-11-002"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.EP-11-002.EP-11-002.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
            "source_type": "SOURCE_LITERAL",
            "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
          },
          "identifier": "EP-11-002.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-11.md",
            "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
            "source_lines": "L718-L721",
            "source_section": "29. Enterprise Design Principles > EP-11-002"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.EP-11-002.EP-11-002.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
            "source_type": "SOURCE_LITERAL",
            "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
          },
          "identifier": "EP-11-002.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-11.md",
            "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
            "source_lines": "L718-L721",
            "source_section": "29. Enterprise Design Principles > EP-11-002"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.EP-11-002.EP-11-002.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
            "source_type": "SOURCE_LITERAL",
            "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
          },
          "identifier": "EP-11-002.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-11.md",
            "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
            "source_lines": "L718-L721",
            "source_section": "29. Enterprise Design Principles > EP-11-002"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.EP-11-002.EP-11-002.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
            "source_type": "SOURCE_LITERAL",
            "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
          },
          "identifier": "EP-11-002.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-11.md",
            "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
            "source_lines": "L718-L721",
            "source_section": "29. Enterprise Design Principles > EP-11-002"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.EP-11-002.EP-11-002.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.EP-11-002",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "They are merged into one record or one lifecycle mutation changes the other improperly"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID"
    ],
    "positive_oracle": [
      "Identity and Relationship retain independent identities, ownership references and lifecycles"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-008"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
      "source_lines": "L718-L721",
      "source_section": "29. Enterprise Design Principles > EP-11-002"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
          "source_type": "SOURCE_LITERAL",
          "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
        },
        "identifier": "EP-11-002.EP-11-002.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "EP-11-002.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-008"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-11.md",
          "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
          "source_lines": "L718-L721",
          "source_section": "29. Enterprise Design Principles > EP-11-002"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.EP-11-002.EP-11-002.EP-11-002.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "EP-11-002.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.CUSTOMER_IDENTITY_ID",
        "FIELD.RELATIONSHIP_ID",
        "FIELD.ORGANIZATION_ID",
        "FIELD.IDENTITY_LIFECYCLE",
        "FIELD.RELATIONSHIP_LIFECYCLE",
        "FIELD.REFERENCE_RESULT"
      ],
      "producer": "EP-11-002.EVIDENCE.PRODUCER",
      "required_collection_origin": "EP-11-002.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.CUSTOMER_IDENTITY_ID",
        "FIELD.RELATIONSHIP_ID",
        "FIELD.ORGANIZATION_ID",
        "FIELD.IDENTITY_LIFECYCLE",
        "FIELD.RELATIONSHIP_LIFECYCLE",
        "FIELD.REFERENCE_RESULT"
      ],
      "required_values_or_hashes": [
        "EP-11-002.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "EP-11-002.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "EP-11-002.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "EP-11-002-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID",
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
              "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
              "source_type": "SOURCE_LITERAL",
              "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
            },
            "identifier": "EP-11-002.EP-11-002.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-11.md",
              "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
              "source_lines": "L718-L721",
              "source_section": "29. Enterprise Design Principles > EP-11-002"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.EP-11-002.EP-11-002.EP-11-002.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
              "source_type": "SOURCE_LITERAL",
              "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
            },
            "identifier": "EP-11-002.EP-11-002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-11.md",
              "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
              "source_lines": "L718-L721",
              "source_section": "29. Enterprise Design Principles > EP-11-002"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.EP-11-002.EP-11-002.EP-11-002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                        "EP-11-002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                      "source_type": "SOURCE_LITERAL",
                      "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
                    },
                    "identifier": "EP-11-002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-11.md",
                      "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                      "source_lines": "L718-L721",
                      "source_section": "29. Enterprise Design Principles > EP-11-002"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.EP-11-002.EP-11-002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-11.md",
                  "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                  "source_lines": "L718-L721",
                  "source_section": "29. Enterprise Design Principles > EP-11-002"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "EP-11-002.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                      "source_type": "SOURCE_LITERAL",
                      "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
                    },
                    "identifier": "EP-11-002.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-008"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-11.md",
                      "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                      "source_lines": "L718-L721",
                      "source_section": "29. Enterprise Design Principles > EP-11-002"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.EP-11-002.EP-11-002.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-11.md",
                  "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                  "source_lines": "L718-L721",
                  "source_section": "29. Enterprise Design Principles > EP-11-002"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                  "source_type": "SOURCE_LITERAL",
                  "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
                },
                "identifier": "EP-11-002.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-11.md",
                  "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                  "source_lines": "L718-L721",
                  "source_section": "29. Enterprise Design Principles > EP-11-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.EP-11-002.EP-11-002.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                  "source_type": "SOURCE_LITERAL",
                  "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
                },
                "identifier": "EP-11-002.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-11.md",
                  "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                  "source_lines": "L718-L721",
                  "source_section": "29. Enterprise Design Principles > EP-11-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.EP-11-002.EP-11-002.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                  "source_type": "SOURCE_LITERAL",
                  "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
                },
                "identifier": "EP-11-002.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-11.md",
                  "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                  "source_lines": "L718-L721",
                  "source_section": "29. Enterprise Design Principles > EP-11-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.EP-11-002.EP-11-002.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                  "source_type": "SOURCE_LITERAL",
                  "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
                },
                "identifier": "EP-11-002.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-11.md",
                  "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                  "source_lines": "L718-L721",
                  "source_section": "29. Enterprise Design Principles > EP-11-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.EP-11-002.EP-11-002.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                  "source_type": "SOURCE_LITERAL",
                  "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
                },
                "identifier": "EP-11-002.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-11.md",
                  "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                  "source_lines": "L718-L721",
                  "source_section": "29. Enterprise Design Principles > EP-11-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.EP-11-002.EP-11-002.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                  "source_type": "SOURCE_LITERAL",
                  "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
                },
                "identifier": "EP-11-002.EP-11-002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-11.md",
                  "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                  "source_lines": "L718-L721",
                  "source_section": "29. Enterprise Design Principles > EP-11-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.EP-11-002.EP-11-002.EP-11-002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                  "source_type": "SOURCE_LITERAL",
                  "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
                },
                "identifier": "EP-11-002.EP-11-002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-11.md",
                  "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                  "source_lines": "L718-L721",
                  "source_section": "29. Enterprise Design Principles > EP-11-002"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.EP-11-002.EP-11-002.EP-11-002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                "source_type": "SOURCE_LITERAL",
                "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
              },
              "identifier": "EP-11-002.EP-11-002.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-11.md",
                "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                "source_lines": "L718-L721",
                "source_section": "29. Enterprise Design Principles > EP-11-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.EP-11-002.EP-11-002.EP-11-002.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "EP-11-002-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
              "source_type": "SOURCE_LITERAL",
              "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
            },
            "identifier": "EP-11-002.EP-11-002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-11.md",
              "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
              "source_lines": "L718-L721",
              "source_section": "29. Enterprise Design Principles > EP-11-002"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.EP-11-002.EP-11-002.EP-11-002.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                      "EP-11-002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                    "source_type": "SOURCE_LITERAL",
                    "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
                  },
                  "identifier": "EP-11-002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-11.md",
                    "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                    "source_lines": "L718-L721",
                    "source_section": "29. Enterprise Design Principles > EP-11-002"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.EP-11-002.EP-11-002.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-11.md",
                "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                "source_lines": "L718-L721",
                "source_section": "29. Enterprise Design Principles > EP-11-002"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "EP-11-002.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                    "source_type": "SOURCE_LITERAL",
                    "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
                  },
                  "identifier": "EP-11-002.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [
                      "P2-DEC-008"
                    ],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-WS-11.md",
                    "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                    "source_lines": "L718-L721",
                    "source_section": "29. Enterprise Design Principles > EP-11-002"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.EP-11-002.EP-11-002.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-11.md",
                "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                "source_lines": "L718-L721",
                "source_section": "29. Enterprise Design Principles > EP-11-002"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                "source_type": "SOURCE_LITERAL",
                "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
              },
              "identifier": "EP-11-002.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-11.md",
                "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                "source_lines": "L718-L721",
                "source_section": "29. Enterprise Design Principles > EP-11-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.EP-11-002.EP-11-002.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                "source_type": "SOURCE_LITERAL",
                "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
              },
              "identifier": "EP-11-002.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-11.md",
                "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                "source_lines": "L718-L721",
                "source_section": "29. Enterprise Design Principles > EP-11-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.EP-11-002.EP-11-002.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                "source_type": "SOURCE_LITERAL",
                "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
              },
              "identifier": "EP-11-002.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-11.md",
                "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                "source_lines": "L718-L721",
                "source_section": "29. Enterprise Design Principles > EP-11-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.EP-11-002.EP-11-002.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                "source_type": "SOURCE_LITERAL",
                "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
              },
              "identifier": "EP-11-002.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-11.md",
                "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                "source_lines": "L718-L721",
                "source_section": "29. Enterprise Design Principles > EP-11-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.EP-11-002.EP-11-002.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
                "source_type": "SOURCE_LITERAL",
                "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
              },
              "identifier": "EP-11-002.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-11-002.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-11.md",
                "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
                "source_lines": "L718-L721",
                "source_section": "29. Enterprise Design Principles > EP-11-002"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.EP-11-002.EP-11-002.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        }
      ],
      "boundary_cases": [
        "A Relationship references Identity without transferring canonical identity authority"
      ],
      "contract_ast_sha256": "e9a09396f0ca0ddd627d7fa3b768e0325f0485be3d73885d8766e56892fd5843",
      "contract_id": "P2C.C4.CONTRACT.EP-11-002",
      "criticality": "CRITICAL",
      "disposition": "OPERATOR_REMAP_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-11.md#29. Enterprise Design Principles > EP-11-002",
            "source_type": "SOURCE_LITERAL",
            "version": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426"
          },
          "identifier": "EP-11-002.EP-11-002.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-11-002.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-11.md",
            "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
            "source_lines": "L718-L721",
            "source_section": "29. Enterprise Design Principles > EP-11-002"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.EP-11-002.EP-11-002.EP-11-002.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "EP-11-002.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.CUSTOMER_IDENTITY_ID",
          "FIELD.RELATIONSHIP_ID",
          "FIELD.ORGANIZATION_ID",
          "FIELD.IDENTITY_LIFECYCLE",
          "FIELD.RELATIONSHIP_LIFECYCLE",
          "FIELD.REFERENCE_RESULT"
        ],
        "producer": "EP-11-002.EVIDENCE.PRODUCER",
        "required_collection_origin": "EP-11-002.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.CUSTOMER_IDENTITY_ID",
          "FIELD.RELATIONSHIP_ID",
          "FIELD.ORGANIZATION_ID",
          "FIELD.IDENTITY_LIFECYCLE",
          "FIELD.RELATIONSHIP_LIFECYCLE",
          "FIELD.REFERENCE_RESULT"
        ],
        "required_values_or_hashes": [
          "EP-11-002.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "EP-11-002.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "EP-11-002.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-FB7CDA0110288A7631C7",
        "P2C-C4-FX-317006A90F0344147F1F",
        "P2C-C4-FX-46B561282EB30BB265FF"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "They are merged into one record or one lifecycle mutation changes the other improperly"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "EP-11-002-O001",
          "obligation_text": "Customer Identity và Customer Relationship được tách biệt"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "EP-11-002.O1.1.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "EP-11-002-O001"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID"
      ],
      "positive_oracles": [
        "Identity and Relationship retain independent identities, ownership references and lifecycles"
      ],
      "preconditions": [
        "Canonical Customer Identity and Organization-scoped Relationship identities are available"
      ],
      "prohibitions": [
        "They are merged into one record or one lifecycle mutation changes the other improperly"
      ],
      "requirement_id": "EP-11-002",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-008"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-11.md",
        "source_fingerprint": "247314328e164073bfb71a5d459f7f538394c2848fe86c77cd48ee63531b1426",
        "source_lines": "L718-L721",
        "source_section": "29. Enterprise Design Principles > EP-11-002"
      },
      "source_statement": "Customer Identity và Customer Relationship được tách biệt.",
      "surrounding_source_context": "## EP-11-002\n\nCustomer Identity và Customer Relationship được tách biệt.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.EP-11-002",
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
        "EP-11-002-AC001",
        "EP-11-002-AC002",
        "EP-11-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-11-002-O001",
      "obligation_text": "Customer Identity và Customer Relationship được tách biệt"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-11-002-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-11-002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-11-002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-11-002-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-11-002-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-11-002 does not define a recovery obligation."
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
    "source_fingerprint": "fa4497e97210b4af1a91c036cf17b83acf1747a43c3e3f7efb156f128885b634",
    "source_lines": "L3667-L5131",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-11-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-11-003",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "826294142c43895cc1dc8b110be9bd24bc966b20589666fc6f689ef696e36733"
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
        "EP-11-003-AC001",
        "EP-11-003-AC002",
        "EP-11-003-AC003"
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
    "source_fingerprint": "826294142c43895cc1dc8b110be9bd24bc966b20589666fc6f689ef696e36733",
    "source_lines": "L5133-L5212",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-11-003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-11-004",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "5713d0e6b38f2ad58047202c1180ca7a32948ad851b15575019399f7c63e71d9"
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
        "EP-11-004-AC001",
        "EP-11-004-AC002",
        "EP-11-004-AC003"
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
    "source_fingerprint": "5713d0e6b38f2ad58047202c1180ca7a32948ad851b15575019399f7c63e71d9",
    "source_lines": "L5214-L5289",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-11-004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-11-005",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "39ee36fc533e84531bd10bb2fe489d2a96180ca421bbd4f58e2fa6118244857e"
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
        "EP-11-005-AC001",
        "EP-11-005-AC002",
        "EP-11-005-AC003"
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
    "source_fingerprint": "39ee36fc533e84531bd10bb2fe489d2a96180ca421bbd4f58e2fa6118244857e",
    "source_lines": "L5291-L5366",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-11-005"
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
      "requirement_id": "EP-11-006",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "c95d2e874963ed165c2efe8bebc0114e390170004a8454f453ef81afe073be3d"
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
        "EP-11-006-AC001",
        "EP-11-006-AC002",
        "EP-11-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-11-006-O001",
      "obligation_text": "Customer Privacy tuân thủ Consent Based Data Access"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-11-006-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-11-006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-11-006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-11-006-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-11-006-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-11-006 does not define a recovery obligation."
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
    "source_fingerprint": "c95d2e874963ed165c2efe8bebc0114e390170004a8454f453ef81afe073be3d",
    "source_lines": "L5368-L5482",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-11-006"
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
      "requirement_id": "EP-11-007",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "source_fingerprint": "f43e20290af2f812fa73bc2945df2a743b6172fd9d7cec559924bc1ab017080b"
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
        "EP-11-007-AC001",
        "EP-11-007-AC002",
        "EP-11-007-AC003"
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
    "source_fingerprint": "f43e20290af2f812fa73bc2945df2a743b6172fd9d7cec559924bc1ab017080b",
    "source_lines": "L5484-L5563",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-11-007"
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
