---
document_code: "BRD-WS-12"
document_id: "BRD-WS-12"
title: "Communication Platform, Notification & Engagement"
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

# BRD Workshop 12

# Communication Platform, Notification & Engagement

---

# 1. Workshop Objective

Workshop này xác định toàn bộ Communication Platform của YSim.

Bao gồm:

- Communication Platform
- Notification Management
- Personal Inbox
- Portal Announcement
- Communication Policy
- Communication Matrix
- Contact Point
- Message Template
- Localization
- Auto Translation
- Communication Queue
- Delivery Tracking
- Engagement

Workshop này không bao gồm:

- AI Chat
- Voice Bot
- Call Center
- Customer Timeline

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| Notification | Transaction |
| NotificationEvent | Transaction |
| NotificationTemplate | Master |
| NotificationPreference | Master |
| NotificationSubscription | Master |
| NotificationPolicy | Master |
| CommunicationMatrix | Master |
| CommunicationLog | Transaction |
| CommunicationQueue | Transaction |
| DeliveryAttempt | Transaction |
| ContactPoint | Master |
| PersonalInbox | Master |
| InboxMessage | Transaction |
| PortalAnnouncement | Transaction |
| LocalizationPackage | Master |
| TranslationResource | Master |

---

# 3. Communication Platform Principle

Communication Platform là Platform Capability.

Communication Platform không thuộc:

- Customer Domain
- Payment Domain
- Fulfillment Domain
- Financial Domain

Mọi Business Domain chỉ phát sinh Business Event.

Communication Platform quyết định:

- Có gửi Notification hay không
- Gửi cho ai
- Gửi qua Channel nào
- Template nào
- Chính sách Retry
- Chính sách Localization
- Chính sách Translation

---

# 4. Event-Driven Communication

Communication Platform hoạt động theo mô hình:

```text
Business Event

↓

Communication Matrix

↓

Communication Decision

↓

Template

↓

Communication Queue

↓

Channel Adapter

↓

Gateway

↓

Delivery Result
```

Không Business Domain nào được phép gửi Notification trực tiếp.

---

# 5. Communication Matrix

Communication Matrix quyết định toàn bộ hành vi gửi Notification.

Communication Matrix xác định:

- Business Event
- Recipient
- Notification Category
- Delivery Channel
- Priority
- Retry Policy
- Escalation Policy

Communication Matrix được cấu hình trên Admin Portal.

Không Hard-code.

---

# 6. Notification Event

Notification có thể phát sinh từ mọi Business Event.

Ví dụ:

- Payment Success
- Fulfillment Completed
- Ticket Assigned
- Settlement Approved
- Promotion Started
- Organization Activated
- Security Alert
- Customer Feedback

Notification Message sử dụng UTF-8.

UI hỗ trợ Auto Translation.

---

# 7. Notification Channels

Version 2 hỗ trợ:

- Email
- SMS
- Push Notification
- WhatsApp
- Telegram
- Facebook Messenger
- Zalo OA
- Portal Announcement
- Personal Inbox

Personal Inbox luôn là Delivery Channel cuối cùng.

Notification không được phép mất hoàn toàn.

---

# 8. Portal Announcement

Portal Announcement là một Communication Channel.

Portal Announcement hỗ trợ:

- Banner
- Header Announcement
- Running Text

Portal Announcement có thể áp dụng theo:

- Global
- Organization
- Storefront
- User Group

---

# 9. Personal Inbox

Mỗi User và Customer đều có Personal Inbox.

Personal Inbox lưu toàn bộ Notification.

Phân loại mặc định:

- Marketing
- Account / Personal
- Ticket
- Other

Notification Ticket cho phép phản hồi nhanh trực tiếp từ Inbox.

Inbox hỗ trợ:

- Read
- Read All
- Search
- Filter

Kiến trúc mở để hỗ trợ:

- Archive
- Star
- Pin

ở các phiên bản sau.

---

# 10. Contact Point

ContactPoint là Business Object.

Một ContactPoint có thể là:

- Email
- Phone
- WhatsApp
- Telegram
- Facebook
- Google Identity
- Apple Identity
- Portal Inbox

Communication Platform sử dụng ContactPoint để lựa chọn Delivery Channel.

---

# 11. Notification Preference

Customer có thể cấu hình Notification Preference theo dạng Matrix.

Ví dụ:

| Notification Type | Email | Push | Portal | Inbox |
|-------------------|-------|------|--------|-------|
| Payment | ✔ | ✖ | ✔ | ✔ |
| Promotion | ✖ | ✔ | ✔ | ✔ |
| Ticket | ✔ | ✖ | ✔ | ✔ |

Mặc định:

All Channels.

Unsubscribe trên Email chỉ ảnh hưởng tới Notification Category tương ứng.

---

# 12. Communication Priority

Communication Platform sử dụng Priority.

Các mức ưu tiên:

- Critical
- High
- Normal
- Low

Priority ảnh hưởng tới:

- Queue
- Retry
- Escalation

---

# 13. Notification Template

Template thuộc Organization.

Template kế thừa theo Distribution Hierarchy:

```text
YSim

↓

Parent Organization

↓

Organization Override
```

Organization có thể tùy chỉnh Template của mình.

---

# 14. Localization

Localization bao gồm:

- Language
- Currency
- Timezone
- Measurement
- Temperature
- Distance
- Weight
- Date Format
- Time Format
- Decimal Format
- First Day Of Week

Kiến trúc mở để hỗ trợ:

- Left-To-Right
- Right-To-Left

ở các phiên bản sau.

---

# 15. Notification Routing

Notification Routing được quyết định bởi Business Event.

Không phụ thuộc Organization Hierarchy.

---

# 16. Delivery Attempt

DeliveryAttempt là Business Object.

Retry Policy mặc định:

- Retry tối đa 03 lần
- Khoảng cách 05 phút

Retry Policy có thể cấu hình.

---

# 17. Communication Log

Communication Platform lưu Communication Log.

Communication Log phải hỗ trợ:

- Search
- Export
- Retention Policy
- Auto Rotation

Chi tiết Implementation sẽ được mô tả trong SDD.

---

# 18. Read Receipt

Read Receipt được hỗ trợ nếu Gateway cho phép.

Portal luôn hỗ trợ:

- Read
- Read Time

---

# 19. Notification Subscription

Version 2 hỗ trợ:

- Marketing
- System
- Support

Kiến trúc mở để bổ sung Subscription Category trong các phiên bản sau.

---

# 20. Notification Category

Version 2 hỗ trợ:

- System
- Payment
- Fulfillment
- Promotion
- Ticket
- Organization
- Security
- Marketing

Category sử dụng Reference Data Management.

---

# 21. User Portal Notification

User Portal cũng nhận Notification.

Ví dụ:

- Payment Success
- Ticket Assigned
- Commission Pending
- Settlement Ready
- Organization Alert

---

# 22. Customer Inbox

Customer Inbox lưu toàn bộ Notification.

Customer có thể:

- Read
- Read All
- Search
- Filter

Notification không bị mất sau khi Email gửi thành công.

---

# 23. Real-time Communication

Version 2 sử dụng:

Real-time Notification.

Notification Digest được giữ chỗ cho phiên bản sau.

---

# 24. Auto Translation

Notification hỗ trợ:

- Original Language
- Auto Translation
- View Original

Translation dựa trên User Language Preference.

---

# 25. Attachment

Notification hỗ trợ:

- Image
- PDF
- Invoice
- QR Code

Không hỗ trợ Video trong Version 2.

---

# 26. Communication Policy

Communication Policy hỗ trợ nhiều tầng:

```text
Global

↓

Parent

↓

Organization

↓

Storefront

↓

User

↓

Customer
```

Organization có thể Override theo Policy.

---

# 27. Do Not Disturb

Customer có thể cấu hình:

Do Not Disturb.

Mặc định:

22:00 → 07:00

Organization có thể cấu hình Blacklist.

Emergency Notification không bị ảnh hưởng bởi Do Not Disturb.

---

# 28. Escalation Retry

Nếu Delivery thất bại:

```text
Email

↓

Retry

↓

Alternative Channel

↓

Personal Inbox
```

Escalation Policy được cấu hình.

---

# 29. Communication Consent

Communication Consent tuân thủ GDPR.

Consent được quản lý độc lập theo:

- Marketing
- Support
- Promotion
- Transaction

---

# 30. Communication Queue

Communication Platform sử dụng Message Queue.

Kiến trúc:

```text
Business Event

↓

Communication Queue

↓

Worker

↓

Channel Adapter

↓

Gateway

↓

Delivery Result
```

Communication Queue được thiết kế mở.

Có thể triển khai Communication Server riêng trong tương lai.

---

# 31. Communication Adapter

Communication Platform sử dụng Adapter Pattern.

Bao gồm:

- Email Adapter
- SMS Adapter
- Push Adapter
- Portal Adapter
- WhatsApp Adapter
- Telegram Adapter
- Facebook Adapter
- Zalo Adapter

Business Logic không phụ thuộc Gateway.

---

# 32. Business Decisions (Locked)

## BD-12-001

Communication Platform là Platform Capability độc lập.

---

## BD-12-002

Notification sử dụng Event-Driven Architecture.

---

## BD-12-003

Notification được quyết định bằng Communication Matrix.

---

## BD-12-004

Portal Announcement là một Communication Channel.

---

## BD-12-005

Personal Inbox luôn là Delivery Channel cuối cùng.

---

## BD-12-006

ContactPoint là Business Object.

---

## BD-12-007

Notification Preference sử dụng Matrix.

---

## BD-12-008

Template hỗ trợ Parent Override.

---

## BD-12-009

Localization hỗ trợ nhiều chuẩn hiển thị.

---

## BD-12-010

Notification Routing dựa trên Business Event.

---

## BD-12-011

Retry Policy mặc định là 03 lần, cách nhau 05 phút.

---

## BD-12-012

Communication Log hỗ trợ Search, Export và Retention.

---

## BD-12-013

Notification Subscription và Notification Category sử dụng Reference Data Management.

---

## BD-12-014

Version 2 sử dụng Real-time Notification.

---

## BD-12-015

Notification hỗ trợ Auto Translation.

---

## BD-12-016

Communication Policy hỗ trợ nhiều tầng Override.

---

## BD-12-017

Do Not Disturb hỗ trợ Emergency Notification.

---

## BD-12-018

Communication Platform sử dụng Message Queue.

---

## BD-12-019

Communication Platform sử dụng Channel Adapter Pattern.

---

# 33. Enterprise Design Principles

## EP-12-001

Communication Platform độc lập với Business Domain.

---

## EP-12-002

Business Domain chỉ Publish Business Event.

---

## EP-12-003

Communication Matrix quyết định toàn bộ hành vi gửi Notification.

---

## EP-12-004

Personal Inbox là nơi lưu giữ Notification lâu dài.

---

## EP-12-005

Notification luôn hỗ trợ Localization và Auto Translation.

---

## EP-12-006

Communication Platform hỗ trợ mở rộng Channel mà không thay đổi Business Logic.

---

## EP-12-007

Message Queue và Channel Adapter là nền tảng mở rộng Performance.

---

# 34. Business Capabilities Covered

- Communication Platform
- Notification Management
- Communication Matrix Management
- Contact Point Management
- Personal Inbox Management
- Portal Announcement Management
- Template Management
- Localization Management
- Translation Management
- Delivery Tracking
- Communication Policy Management
- Notification Subscription Management
- Communication Queue Management
- Channel Adapter Management

---

# 35. Traceability

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
- BRD-WS-11

---

# 36. Impacts to Other Domains

Workshop này ảnh hưởng tới:

- Customer Portal
- User Portal
- Notification Platform
- Reporting & BI
- Customer Success
- API
- DMS
- DBD

---

# 37. Workshop Status

**Status:** FROZEN

Workshop này hoàn thiện toàn bộ Communication Platform Domain của YSim.

---

# 38. Next Workshop

**BRD-WS-13 – Reporting, Analytics & Operational Intelligence**

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-001 — Communication Platform là Platform Capability độc lập

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
      "requirement_id": "BD-12-001",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "074b0454365c0c2b231d58870d3ef142630e82f0edabd388f641dbab68d0399b"
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
        "BD-12-001-AC001",
        "BD-12-001-AC002",
        "BD-12-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-001-O001",
      "obligation_text": "Communication Platform là Platform Capability độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Platform là Platform Capability độc lập.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-001",
    "source_context_sha256": "84f565c7041691e217fdb4ce25d8228f299223e4e080133d2e7dda5e8e8ce5d5",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "074b0454365c0c2b231d58870d3ef142630e82f0edabd388f641dbab68d0399b",
    "source_lines": "L873-L952",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-001"
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
  "stable_id": "BD-12-001",
  "title": "Communication Platform là Platform Capability độc lập",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-002 — Notification sử dụng Event-Driven Architecture

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
      "requirement_id": "BD-12-002",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "b8c56cf3d414a934c6bfe374dd5df3b8531c8266e712bbff8729c0f675d3a0e3"
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
        "BD-12-002-AC001",
        "BD-12-002-AC002",
        "BD-12-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-002-O001",
      "obligation_text": "Notification sử dụng Event-Driven Architecture"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Notification sử dụng Event-Driven Architecture.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-002",
    "source_context_sha256": "5084214ae5f46abb676a4395d948701b520580f6e8b57fbfaf8064e89339f3fa",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "b8c56cf3d414a934c6bfe374dd5df3b8531c8266e712bbff8729c0f675d3a0e3",
    "source_lines": "L954-L1029",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-002"
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
  "stable_id": "BD-12-002",
  "title": "Notification sử dụng Event-Driven Architecture",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-003 — Notification được quyết định bằng Communication Matrix

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
      "requirement_id": "BD-12-003",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "c09260288943aace54e08290cec5da8fd2c876bf09e76571fc71aa79d5a838a0"
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
        "BD-12-003-AC001",
        "BD-12-003-AC002",
        "BD-12-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-003-O001",
      "obligation_text": "Notification được quyết định bằng Communication Matrix"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Notification được quyết định bằng Communication Matrix.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-003",
    "source_context_sha256": "ec0ea77853c1a49415c9efed5178e889cdd46ce70732601bd2ea5b3ed1b759b7",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "c09260288943aace54e08290cec5da8fd2c876bf09e76571fc71aa79d5a838a0",
    "source_lines": "L1031-L1106",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-003"
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
  "stable_id": "BD-12-003",
  "title": "Notification được quyết định bằng Communication Matrix",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-004 — Portal Announcement là một Communication Channel

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
      "requirement_id": "BD-12-004",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "2d8865eeef25bab7006d8842cde8e9620976c408c5e97eb41d1334fd108acb1c"
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
        "BD-12-004-AC001",
        "BD-12-004-AC002",
        "BD-12-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-004-O001",
      "obligation_text": "Portal Announcement là một Communication Channel"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Portal Announcement là một Communication Channel.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Portal Announcement",
    "source_context_sha256": "4789f9288084f39e38cd7a5ef1ccdf625132a5c35868251fd289dbfa429e00be",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "2d8865eeef25bab7006d8842cde8e9620976c408c5e97eb41d1334fd108acb1c",
    "source_lines": "L1108-L1183",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-004"
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
  "stable_id": "BD-12-004",
  "title": "Portal Announcement là một Communication Channel",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-005 — Personal Inbox luôn là Delivery Channel cuối cùng

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
      "requirement_id": "BD-12-005",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "55efd1cdedada8d45c5864d194cd8a4e8ab3433a8bef3bb653692415d7b32277"
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
        "BD-12-005-AC001",
        "BD-12-005-AC002",
        "BD-12-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-005-O001",
      "obligation_text": "Personal Inbox luôn là Delivery Channel cuối cùng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Personal Inbox luôn là Delivery Channel cuối cùng.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Notification Channels",
    "source_context_sha256": "90bd1cf3f3651bd46f29b7ceb59908692086b6ed82da7d9d14025f2b27d4222b",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "55efd1cdedada8d45c5864d194cd8a4e8ab3433a8bef3bb653692415d7b32277",
    "source_lines": "L1185-L1260",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-005"
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
  "stable_id": "BD-12-005",
  "title": "Personal Inbox luôn là Delivery Channel cuối cùng",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-006 — ContactPoint là Business Object

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
      "requirement_id": "BD-12-006",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "5a047fe23f1f3fdd7a0459ac1a007c457d7c07353af832d178c80debe5948ab1"
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
        "BD-12-006-AC001",
        "BD-12-006-AC002",
        "BD-12-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-006-O001",
      "obligation_text": "ContactPoint là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "ContactPoint là Business Object.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Contact Point",
    "source_context_sha256": "d1dd5beefa9dc482d525d996b365c2b9e046b25964a79e489bc339354baa6915",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "5a047fe23f1f3fdd7a0459ac1a007c457d7c07353af832d178c80debe5948ab1",
    "source_lines": "L1262-L1337",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-006"
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
  "stable_id": "BD-12-006",
  "title": "ContactPoint là Business Object",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-007 — Notification Preference sử dụng Matrix

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
      "requirement_id": "BD-12-007",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "b6b467e110b2132d0795a7c0d9c8882e0e6f8a909f5ae5295b364cee4dd4daf3"
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
        "BD-12-007-AC001",
        "BD-12-007-AC002",
        "BD-12-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-007-O001",
      "obligation_text": "Notification Preference sử dụng Matrix"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Notification Preference sử dụng Matrix.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-007",
    "source_context_sha256": "856abdf1a4bae501d02ecc087e6f9f2d60e27d17b45b5f7dd473ec9a5d7c4c04",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "b6b467e110b2132d0795a7c0d9c8882e0e6f8a909f5ae5295b364cee4dd4daf3",
    "source_lines": "L1339-L1414",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-007"
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
  "stable_id": "BD-12-007",
  "title": "Notification Preference sử dụng Matrix",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-008 — Template hỗ trợ Parent Override

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
      "requirement_id": "BD-12-008",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "66110ca40bc5e85714f8eb8076c66e877620f9744ec40de54bf66effbdef7efc"
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
        "BD-12-008-AC001",
        "BD-12-008-AC002",
        "BD-12-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-008-O001",
      "obligation_text": "Template hỗ trợ Parent Override"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Template hỗ trợ Parent Override.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-008",
    "source_context_sha256": "efffcca92f8526e7c4d4410b30cc0f9c9ad7972fae3ea16420e7aea427876d53",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "66110ca40bc5e85714f8eb8076c66e877620f9744ec40de54bf66effbdef7efc",
    "source_lines": "L1416-L1491",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-008"
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
  "stable_id": "BD-12-008",
  "title": "Template hỗ trợ Parent Override",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-009 — Localization hỗ trợ nhiều chuẩn hiển thị

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
      "requirement_id": "BD-12-009",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "a2a56af162a55c3ddebee93cf4412b369ea67e0544d56c88c455917e5b0f0b34"
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
        "BD-12-009-AC001",
        "BD-12-009-AC002",
        "BD-12-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-009-O001",
      "obligation_text": "Localization hỗ trợ nhiều chuẩn hiển thị"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Localization hỗ trợ nhiều chuẩn hiển thị.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-009",
    "source_context_sha256": "e406450975ee97a60ba44381df20aec293cae86624e5b6a2060188f56bc59d78",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "a2a56af162a55c3ddebee93cf4412b369ea67e0544d56c88c455917e5b0f0b34",
    "source_lines": "L1493-L1568",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-009"
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
  "stable_id": "BD-12-009",
  "title": "Localization hỗ trợ nhiều chuẩn hiển thị",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-010 — Notification Routing dựa trên Business Event

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
      "requirement_id": "BD-12-010",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "97bde57c5bb12a69a99d33c8a25c6926a777503bfab24d23634f6fbd116795e7"
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
        "BD-12-010-AC001",
        "BD-12-010-AC002",
        "BD-12-010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-010-O001",
      "obligation_text": "Notification Routing dựa trên Business Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Notification Routing dựa trên Business Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-010",
    "source_context_sha256": "f24173fbad650b972a4675ebcc5caacdc1b7a3a0aa5c6b60b2dad98560fafc7f",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "97bde57c5bb12a69a99d33c8a25c6926a777503bfab24d23634f6fbd116795e7",
    "source_lines": "L1570-L1645",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-010"
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
  "stable_id": "BD-12-010",
  "title": "Notification Routing dựa trên Business Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-011 — Retry Policy mặc định là 03 lần, cách nhau 05 phút

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-12-011",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "a9503318626c5189a4de89bb4062ced5b1010d14d3d3ce563f51c28d4b2046c2"
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
        "BD-12-011-AC001",
        "BD-12-011-AC002",
        "BD-12-011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-011-O001",
      "obligation_text": "Retry Policy mặc định là 03 lần, cách nhau 05 phút"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Retry Policy mặc định là 03 lần, cách nhau 05 phút.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-011",
    "source_context_sha256": "2924f4b5a641111002d5b646237d74c05c720f6fd408d40bc5b02808287f10f5",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "a9503318626c5189a4de89bb4062ced5b1010d14d3d3ce563f51c28d4b2046c2",
    "source_lines": "L1647-L1726",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-011"
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
  "stable_id": "BD-12-011",
  "title": "Retry Policy mặc định là 03 lần, cách nhau 05 phút",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-012 — Communication Log hỗ trợ Search, Export và Retention

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
      "requirement_id": "BD-12-012",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "a58f2f12357b48988a1ab5895abfdc18403b7f2ce6bc9c212648fc20e46a431a"
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
        "BD-12-012-AC001",
        "BD-12-012-AC002",
        "BD-12-012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-012-O001",
      "obligation_text": "Communication Log hỗ trợ Search, Export và Retention"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Log hỗ trợ Search, Export và Retention.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-012",
    "source_context_sha256": "9be6de91706ab11192ad2a6bfc1907fba6590ae41837aaa89a9324aa5c7756f1",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "a58f2f12357b48988a1ab5895abfdc18403b7f2ce6bc9c212648fc20e46a431a",
    "source_lines": "L1728-L1803",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-012"
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
  "stable_id": "BD-12-012",
  "title": "Communication Log hỗ trợ Search, Export và Retention",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-013 — Notification Subscription và Notification Category sử dụng Reference Data Management

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
      "requirement_id": "BD-12-013",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "041e7bfd5d60b015d164004067ebf821e67618375eae6dc8de5dc67695df0d1b"
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
        "BD-12-013-AC001",
        "BD-12-013-AC002",
        "BD-12-013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-013-O001",
      "obligation_text": "Notification Subscription và Notification Category sử dụng Reference Data Management"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Notification Subscription và Notification Category sử dụng Reference Data Management.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-013",
    "source_context_sha256": "83e099e63968e1f63fd8cef0f1140a0e0e2a0d3c65f203a3e8cd6268ff1b5473",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "041e7bfd5d60b015d164004067ebf821e67618375eae6dc8de5dc67695df0d1b",
    "source_lines": "L1805-L1880",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-013"
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
  "stable_id": "BD-12-013",
  "title": "Notification Subscription và Notification Category sử dụng Reference Data Management",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-014 — Version 2 sử dụng Real-time Notification

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
      "requirement_id": "BD-12-014",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "0c8bc5bc0212878d6e112673627f9caf4cd19fec7fde1af6b1b08ad97ab5a438"
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
        "BD-12-014-AC001",
        "BD-12-014-AC002",
        "BD-12-014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-014-O001",
      "obligation_text": "Version 2 sử dụng Real-time Notification"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Version 2 sử dụng Real-time Notification.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-014",
    "source_context_sha256": "f0245700c68f527ce043e394163376ee697596758a2e5f4f57756773b96f5708",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "0c8bc5bc0212878d6e112673627f9caf4cd19fec7fde1af6b1b08ad97ab5a438",
    "source_lines": "L1882-L1957",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-014"
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
  "stable_id": "BD-12-014",
  "title": "Version 2 sử dụng Real-time Notification",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-015 — Notification hỗ trợ Auto Translation

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-010"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-12-015",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "006bc1caa7993fe4763a7fb17ab33c5a636367120fad2efbbfe6207532ccad6d"
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
        "BD-12-015-AC001",
        "BD-12-015-AC002",
        "BD-12-015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-015-O001",
      "obligation_text": "Notification hỗ trợ Auto Translation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Notification hỗ trợ Auto Translation.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-010"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-015",
    "source_context_sha256": "d8c15e95e28cbb26045a28dab5f8e5854054d95749ba4bada1c0e63aff637360",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "006bc1caa7993fe4763a7fb17ab33c5a636367120fad2efbbfe6207532ccad6d",
    "source_lines": "L1959-L2038",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-015"
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
  "stable_id": "BD-12-015",
  "title": "Notification hỗ trợ Auto Translation",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-016 — Communication Policy hỗ trợ nhiều tầng Override

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
      "requirement_id": "BD-12-016",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "17a3a1befffa16477af157be03dd573fac4cb072f5146452a2b99b45720267fd"
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
        "BD-12-016-AC001",
        "BD-12-016-AC002",
        "BD-12-016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-016-O001",
      "obligation_text": "Communication Policy hỗ trợ nhiều tầng Override"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Policy hỗ trợ nhiều tầng Override.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-016",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-016",
    "source_context_sha256": "a446876a2b49a1f811741ec77bec14294a146201b4a61b0106f7da5a0e99a49c",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "17a3a1befffa16477af157be03dd573fac4cb072f5146452a2b99b45720267fd",
    "source_lines": "L2040-L2115",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-016"
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
  "stable_id": "BD-12-016",
  "title": "Communication Policy hỗ trợ nhiều tầng Override",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-017 — Do Not Disturb hỗ trợ Emergency Notification

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
      "requirement_id": "BD-12-017",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "3f6c3c2985b882b1b0ee7ba85e948b4972509162042e306b7ccbec1dc256c2e6"
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
        "BD-12-017-AC001",
        "BD-12-017-AC002",
        "BD-12-017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-017-O001",
      "obligation_text": "Do Not Disturb hỗ trợ Emergency Notification"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Do Not Disturb hỗ trợ Emergency Notification.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-017",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-017",
    "source_context_sha256": "00a9d13ee530da2f67e3a8a52d5155a0be45c7be481094a34680c933c2a502de",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "3f6c3c2985b882b1b0ee7ba85e948b4972509162042e306b7ccbec1dc256c2e6",
    "source_lines": "L2117-L2192",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-017"
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
  "stable_id": "BD-12-017",
  "title": "Do Not Disturb hỗ trợ Emergency Notification",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-018 — Communication Platform sử dụng Message Queue

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
      "requirement_id": "BD-12-018",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "2759219429f90cc5fc5de6a3c65a3dc42d4d0e1e61af1986646f2cebc90dfa80"
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
        "BD-12-018-AC001",
        "BD-12-018-AC002",
        "BD-12-018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-018-O001",
      "obligation_text": "Communication Platform sử dụng Message Queue"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Platform sử dụng Message Queue.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-018",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Communication Queue",
    "source_context_sha256": "e435f3b49f43a3bbefdb75ec065376ca27bfb749584307d9c7f5237982eca9e3",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "2759219429f90cc5fc5de6a3c65a3dc42d4d0e1e61af1986646f2cebc90dfa80",
    "source_lines": "L2194-L2269",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-018"
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
  "stable_id": "BD-12-018",
  "title": "Communication Platform sử dụng Message Queue",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-019 — Communication Platform sử dụng Channel Adapter Pattern

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-12-019",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "f6f680d7c03cd63024b77e4cc3c2bbe6cc49b763ad36ac7c7e0d0a6abf700795"
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
        "BD-12-019-AC001",
        "BD-12-019-AC002",
        "BD-12-019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-12-019-O001",
      "obligation_text": "Communication Platform sử dụng Channel Adapter Pattern"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Platform sử dụng Channel Adapter Pattern.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-12-019",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-12-019",
    "source_context_sha256": "23cab54d784e337b404bb3b4bc814b813d226ea95cf4d66fc3404f1758290cb4",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "f6f680d7c03cd63024b77e4cc3c2bbe6cc49b763ad36ac7c7e0d0a6abf700795",
    "source_lines": "L2271-L2350",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-12-019"
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
  "stable_id": "BD-12-019",
  "title": "Communication Platform sử dụng Channel Adapter Pattern",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R002 — Notification không được phép mất hoàn toàn

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
      "requirement_id": "BRD-WS-12-R002",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "380b92e0cffdea70ee40f69b9622589a7dbba7450b4b261237a84d9054007999"
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
        "BRD-WS-12-R002-AC001",
        "BRD-WS-12-R002-AC002",
        "BRD-WS-12-R002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-12-R002-O001",
      "obligation_text": "Notification không được phép mất hoàn toàn"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Notification không được phép mất hoàn toàn.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-002",
    "previous_temporary_key": "TMP-BRD-WS-12-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Notification Channels",
    "source_context_sha256": "90bd1cf3f3651bd46f29b7ceb59908692086b6ed82da7d9d14025f2b27d4222b",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "380b92e0cffdea70ee40f69b9622589a7dbba7450b4b261237a84d9054007999",
    "source_lines": "L2352-L2427",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R002"
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
  "stable_id": "BRD-WS-12-R002",
  "title": "Notification không được phép mất hoàn toàn",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R003 — Trong phạm vi Personal Inbox, Archive, Star và Pin chưa được triển khai trong v2.3; kiến trúc đư…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-12-R003",
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
  "normative_statement": "Trong phạm vi Personal Inbox, Archive, Star và Pin chưa được triển khai trong v2.3; kiến trúc được để mở để hỗ trợ các năng lực này ở phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-003",
    "previous_temporary_key": "TMP-BRD-WS-12-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "44a4748bf88809027391bc781b8c1b55a2e03112cc82ccbbd2b002f05ea312e4",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "44a4748bf88809027391bc781b8c1b55a2e03112cc82ccbbd2b002f05ea312e4",
    "source_lines": "L2429-L2487",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R003"
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
  "stable_id": "BRD-WS-12-R003",
  "title": "Trong phạm vi Personal Inbox, Archive, Star và Pin chưa được triển khai trong v2.3; kiến trúc đư…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R004 — Trong phạm vi Localization, hỗ trợ Left-To-Right và Right-To-Left chưa được triển khai trong v2.…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-12-R004",
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
  "normative_statement": "Trong phạm vi Localization, hỗ trợ Left-To-Right và Right-To-Left chưa được triển khai trong v2.3; kiến trúc được để mở để hỗ trợ ở phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-004",
    "previous_temporary_key": "TMP-BRD-WS-12-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "9d58e0ef0e9e6d2953c444f43ec7dcc9a8f9502da6849818caae9d0487f996a1",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "9d58e0ef0e9e6d2953c444f43ec7dcc9a8f9502da6849818caae9d0487f996a1",
    "source_lines": "L2489-L2547",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R004"
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
  "stable_id": "BRD-WS-12-R004",
  "title": "Trong phạm vi Localization, hỗ trợ Left-To-Right và Right-To-Left chưa được triển khai trong v2.…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R005 — Communication Log phải hỗ trợ: - Search

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
      "requirement_id": "BRD-WS-12-R005",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "dabd20555e16a650abca847cfa63977533172e20be49aa2d79fb5fd0aadf2ce9"
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
        "BRD-WS-12-R005-AC001",
        "BRD-WS-12-R005-AC002",
        "BRD-WS-12-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-12-R005-O001",
      "obligation_text": "Communication Log phải hỗ trợ: - Search"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Log phải hỗ trợ: - Search",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-005",
    "previous_temporary_key": "TMP-BRD-WS-12-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Communication Log",
    "source_context_sha256": "0ad7e46463be45b126392e9324ee62ad15c4a491921212c41ba9392e1b54ff59",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "dabd20555e16a650abca847cfa63977533172e20be49aa2d79fb5fd0aadf2ce9",
    "source_lines": "L2549-L2624",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R005"
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
  "stable_id": "BRD-WS-12-R005",
  "title": "Communication Log phải hỗ trợ: - Search",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R006 — Communication Log phải hỗ trợ: - Export

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
      "requirement_id": "BRD-WS-12-R006",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "7a0e739a39fd05e619b9c424ba50d16a7ca30d5039e9f9ede5fca3e15de98e28"
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
        "BRD-WS-12-R006-AC001",
        "BRD-WS-12-R006-AC002",
        "BRD-WS-12-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-12-R006-O001",
      "obligation_text": "Communication Log phải hỗ trợ: - Export"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Log phải hỗ trợ: - Export",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-006",
    "previous_temporary_key": "TMP-BRD-WS-12-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Communication Log",
    "source_context_sha256": "0ad7e46463be45b126392e9324ee62ad15c4a491921212c41ba9392e1b54ff59",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "7a0e739a39fd05e619b9c424ba50d16a7ca30d5039e9f9ede5fca3e15de98e28",
    "source_lines": "L2626-L2701",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R006"
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
  "stable_id": "BRD-WS-12-R006",
  "title": "Communication Log phải hỗ trợ: - Export",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R007 — Communication Log phải hỗ trợ: - Retention Policy

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
      "requirement_id": "BRD-WS-12-R007",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "b00402e49bd965585129487dd4094e8d5a403a93156c3d51c76b1ff508562a47"
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
        "BRD-WS-12-R007-AC001",
        "BRD-WS-12-R007-AC002",
        "BRD-WS-12-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-12-R007-O001",
      "obligation_text": "Communication Log phải hỗ trợ: - Retention Policy"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Log phải hỗ trợ: - Retention Policy",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-007",
    "previous_temporary_key": "TMP-BRD-WS-12-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Communication Log",
    "source_context_sha256": "0ad7e46463be45b126392e9324ee62ad15c4a491921212c41ba9392e1b54ff59",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "b00402e49bd965585129487dd4094e8d5a403a93156c3d51c76b1ff508562a47",
    "source_lines": "L2703-L2778",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R007"
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
  "stable_id": "BRD-WS-12-R007",
  "title": "Communication Log phải hỗ trợ: - Retention Policy",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R008 — Communication Log phải hỗ trợ: - Auto Rotation

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
      "requirement_id": "BRD-WS-12-R008",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "f6e2fad4caf80462ef32e76b4ae011c4f422ea2ded9efbcad82b5290e43d27c9"
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
        "BRD-WS-12-R008-AC001",
        "BRD-WS-12-R008-AC002",
        "BRD-WS-12-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-12-R008-O001",
      "obligation_text": "Communication Log phải hỗ trợ: - Auto Rotation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Log phải hỗ trợ: - Auto Rotation",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-008",
    "previous_temporary_key": "TMP-BRD-WS-12-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Communication Log",
    "source_context_sha256": "0ad7e46463be45b126392e9324ee62ad15c4a491921212c41ba9392e1b54ff59",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "f6e2fad4caf80462ef32e76b4ae011c4f422ea2ded9efbcad82b5290e43d27c9",
    "source_lines": "L2780-L2855",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R008"
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
  "stable_id": "BRD-WS-12-R008",
  "title": "Communication Log phải hỗ trợ: - Auto Rotation",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R009 — Portal luôn hỗ trợ: - Read

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
      "requirement_id": "BRD-WS-12-R009",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "03a08f9c4a9d4b19c7099efae2eb2cb496bcbb15f451e38e39589e113932730d"
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
        "BRD-WS-12-R009-AC001",
        "BRD-WS-12-R009-AC002",
        "BRD-WS-12-R009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-12-R009-O001",
      "obligation_text": "Portal luôn hỗ trợ: - Read"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Portal luôn hỗ trợ: - Read",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-009",
    "previous_temporary_key": "TMP-BRD-WS-12-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Read Receipt",
    "source_context_sha256": "66144d8198f032f2a017e345faf5b173eba2ec28865bac31c3babb4f1680bc55",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "03a08f9c4a9d4b19c7099efae2eb2cb496bcbb15f451e38e39589e113932730d",
    "source_lines": "L2857-L2932",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R009"
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
  "stable_id": "BRD-WS-12-R009",
  "title": "Portal luôn hỗ trợ: - Read",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R010 — Portal luôn hỗ trợ: - Read Time

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
      "requirement_id": "BRD-WS-12-R010",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "3a41e3b665e0b75520a16de314d5439eeaebb9aab41d3a56667fd56f7bd48990"
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
        "BRD-WS-12-R010-AC001",
        "BRD-WS-12-R010-AC002",
        "BRD-WS-12-R010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-12-R010-O001",
      "obligation_text": "Portal luôn hỗ trợ: - Read Time"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Portal luôn hỗ trợ: - Read Time",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-010",
    "previous_temporary_key": "TMP-BRD-WS-12-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Read Receipt",
    "source_context_sha256": "66144d8198f032f2a017e345faf5b173eba2ec28865bac31c3babb4f1680bc55",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "3a41e3b665e0b75520a16de314d5439eeaebb9aab41d3a56667fd56f7bd48990",
    "source_lines": "L2934-L3009",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R010"
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
  "stable_id": "BRD-WS-12-R010",
  "title": "Portal luôn hỗ trợ: - Read Time",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R011 — Kiến trúc mở để bổ sung Subscription Category trong các phiên bản sau

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-12-R011",
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
  "normative_statement": "Kiến trúc mở để bổ sung Subscription Category trong các phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-011",
    "previous_temporary_key": "TMP-BRD-WS-12-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Notification Subscription",
    "source_context_sha256": "e3f9e84cfbf079ac649ba3940d8533a365a99957f34d1966f0774ce33cde08eb",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "e5370aac32111e982d5d32911edcdd6e6e5b374933043a25f2965d5d738ae9b6",
    "source_lines": "L3011-L3069",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R011"
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
  "stable_id": "BRD-WS-12-R011",
  "title": "Kiến trúc mở để bổ sung Subscription Category trong các phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R012 — Notification Digest được giữ chỗ cho phiên bản sau

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-12-R012",
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
  "normative_statement": "Notification Digest được giữ chỗ cho phiên bản sau.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-012",
    "previous_temporary_key": "TMP-BRD-WS-12-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Real-time Communication",
    "source_context_sha256": "7b2be4033a23acc02b77df0920035c0f413672f8454ad78d887b98b2241ea15b",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "fe5640329f0965d9c83c5021db145df925f82e2a1eb258b700c70b8244550df8",
    "source_lines": "L3071-L3129",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R012"
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
  "stable_id": "BRD-WS-12-R012",
  "title": "Notification Digest được giữ chỗ cho phiên bản sau",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R013 — Attachment của Notification không hỗ trợ Video trong v2.3

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-12-R013",
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
  "normative_statement": "Attachment của Notification không hỗ trợ Video trong v2.3.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-013",
    "previous_temporary_key": "TMP-BRD-WS-12-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "f109fce1d00a8982d4b9c7630eb502ac5f29e293f848b39b367c82fa532ade51",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "f109fce1d00a8982d4b9c7630eb502ac5f29e293f848b39b367c82fa532ade51",
    "source_lines": "L3131-L3189",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R013"
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
  "stable_id": "BRD-WS-12-R013",
  "title": "Attachment của Notification không hỗ trợ Video trong v2.3",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-12-R014 — Communication Consent tuân thủ GDPR

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
      "requirement_id": "BRD-WS-12-R014",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "dc38bb4bdf9a9ae2a4efc51aed679ad659b0a249fe52a746576b7145211d29a0"
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
        "BRD-WS-12-R014-AC001",
        "BRD-WS-12-R014-AC002",
        "BRD-WS-12-R014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-12-R014-O001",
      "obligation_text": "Communication Consent tuân thủ GDPR"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-12-R014-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-12-R014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-12-R014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-12-R014-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-12-R014-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-12-R014 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Consent tuân thủ GDPR.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-12-014",
    "previous_temporary_key": "TMP-BRD-WS-12-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "29. Communication Consent",
    "source_context_sha256": "826e9f1b4bc5de78ba4f7cdfb668229fb27c4aa6592fded0e8825e3872eacde1",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "dc38bb4bdf9a9ae2a4efc51aed679ad659b0a249fe52a746576b7145211d29a0",
    "source_lines": "L3191-L3301",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-12-R014"
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
  "stable_id": "BRD-WS-12-R014",
  "title": "Communication Consent tuân thủ GDPR",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-12-001 — Communication Platform độc lập với Business Domain

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
      "requirement_id": "EP-12-001",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "890b1cfe2f2d9b98f45fe852af25e5bacf18b5c1e95698131241c939256cea2a"
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
        "EP-12-001-AC001",
        "EP-12-001-AC002",
        "EP-12-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-12-001-O001",
      "obligation_text": "Communication Platform độc lập với Business Domain"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Platform độc lập với Business Domain.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-12-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-12-001",
    "source_context_sha256": "6ed33c1419fb6d3ace0c68c57d98ec5c45d5b24e0852e263456cf46c1c8cb578",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "890b1cfe2f2d9b98f45fe852af25e5bacf18b5c1e95698131241c939256cea2a",
    "source_lines": "L3303-L3378",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-12-001"
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
  "stable_id": "EP-12-001",
  "title": "Communication Platform độc lập với Business Domain",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-12-002 — Business Domain chỉ Publish Business Event

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
      "requirement_id": "EP-12-002",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "7b8371f27605d2da6d97708c9db7fae59debc25c0309d59d4bbc00c595d226b8"
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
        "EP-12-002-AC001",
        "EP-12-002-AC002",
        "EP-12-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-12-002-O001",
      "obligation_text": "Business Domain chỉ Publish Business Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain chỉ Publish Business Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-12-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-12-002",
    "source_context_sha256": "04703b7655d311f42797f1039521a7be85785506f66a8e8eb97d02422469d37f",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "7b8371f27605d2da6d97708c9db7fae59debc25c0309d59d4bbc00c595d226b8",
    "source_lines": "L3380-L3455",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-12-002"
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
  "stable_id": "EP-12-002",
  "title": "Business Domain chỉ Publish Business Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-12-003 — Communication Matrix quyết định toàn bộ hành vi gửi Notification

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-017",
        "option_id": "OPT-AST"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-12-003",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "e71995f4da332465a86fb1b978771c0a0825ba87548f52a7e07924a6d655f03b"
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
        "EP-12-003-AC001",
        "EP-12-003-AC002",
        "EP-12-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-12-003-O001",
      "obligation_text": "Communication Matrix quyết định toàn bộ hành vi gửi Notification"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Matrix quyết định toàn bộ hành vi gửi Notification.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-12-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Communication Matrix",
    "source_context_sha256": "2a489cfe1633eb750fa40b19db53add3f859b2a074404f00e32c7fe48f8024d5",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "e71995f4da332465a86fb1b978771c0a0825ba87548f52a7e07924a6d655f03b",
    "source_lines": "L3457-L3536",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-12-003"
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
  "stable_id": "EP-12-003",
  "title": "Communication Matrix quyết định toàn bộ hành vi gửi Notification",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-12-004 — Personal Inbox là nơi lưu giữ Notification lâu dài

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
      "requirement_id": "EP-12-004",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "e4549bda7d0be0c9caca1a47150e4996b0e7fb9146fbcac942ef1fff1cf06087"
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
        "EP-12-004-AC001",
        "EP-12-004-AC002",
        "EP-12-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-12-004-O001",
      "obligation_text": "Personal Inbox là nơi lưu giữ Notification lâu dài"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Personal Inbox là nơi lưu giữ Notification lâu dài.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-12-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-12-004",
    "source_context_sha256": "8f62c0f13cd39a7d358a2e3851339f4e90130923b641d2f24285b51a669d46d6",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "e4549bda7d0be0c9caca1a47150e4996b0e7fb9146fbcac942ef1fff1cf06087",
    "source_lines": "L3538-L3613",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-12-004"
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
  "stable_id": "EP-12-004",
  "title": "Personal Inbox là nơi lưu giữ Notification lâu dài",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-12-005 — Notification luôn hỗ trợ Localization và Auto Translation

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-010"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-12-005",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "ccc5e017e918bac9135cf8e6ef5b9911c819f94ddbb48bdd75c5e43ca6a3f6d0"
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
        "EP-12-005-AC001",
        "EP-12-005-AC002",
        "EP-12-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-12-005-O001",
      "obligation_text": "Notification luôn hỗ trợ Localization và Auto Translation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Notification luôn hỗ trợ Localization và Auto Translation.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-010"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-12-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-12-005",
    "source_context_sha256": "d5f8b6b894c8df7f025f64804d8562aec03287916d90f76442acb806848bb7c6",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "ccc5e017e918bac9135cf8e6ef5b9911c819f94ddbb48bdd75c5e43ca6a3f6d0",
    "source_lines": "L3615-L3694",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-12-005"
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
  "stable_id": "EP-12-005",
  "title": "Notification luôn hỗ trợ Localization và Auto Translation",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-12-006 — Communication Channel or Adapter mới phải có thể được bổ sung mà không sửa domain business logic…

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
      "requirement_id": "EP-12-006",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "efe2924e5ee7f5a1b2ec64a15c47421364a437c8593706ce6c033e96c4c586fc"
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
        "EP-12-006-AC001",
        "EP-12-006-AC002",
        "EP-12-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-12-006-O001",
      "obligation_text": "Communication Channel or Adapter mới phải có thể được bổ sung mà không sửa domain business logic và phải tuân thủ governed configuration, credential, approval, security, retry và audit contracts"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Channel or Adapter mới phải có thể được bổ sung mà không sửa domain business logic và phải tuân thủ governed configuration, credential, approval, security, retry và audit contracts.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-12-006",
    "phase_2c_c3_actions": [
      "C3_APPROVED_SEMANTIC_DIRECTIVE"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-12-006",
    "source_context_sha256": "a1a80a93c20b0452764c32a8e8b16b11f7cbb37f579027ef33ac5abc81f9bde5",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "efe2924e5ee7f5a1b2ec64a15c47421364a437c8593706ce6c033e96c4c586fc",
    "source_fingerprint_before_c3": "d168f3ed2341ffd0ea3416d35adf67ca1efc1da408f946bf5744c7cfcde97744",
    "source_lines": "L3696-L3781",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-12-006"
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
  "stable_id": "EP-12-006",
  "title": "Communication Channel or Adapter mới phải có thể được bổ sung mà không sửa domain business logic…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-12-007 — Message Queue và Channel Adapter phải đáp ứng approved service tier, performance budget, SLO và …

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "P2-DEC-009",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-12-007",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "source_fingerprint": "1c08d6ac5478e1546c37a4465473dae2147718d534a760a7df6ac0adb2d856bb"
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
        "EP-12-007-AC001",
        "EP-12-007-AC002",
        "EP-12-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-12-007-O001",
      "obligation_text": "Message Queue và Channel Adapter phải đáp ứng approved service tier, performance budget, SLO và channel-delivery contract, bao gồm capacity scaling, backpressure, observable delivery và failure isolation"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Message Queue và Channel Adapter phải đáp ứng approved service tier, performance budget, SLO và channel-delivery contract, bao gồm capacity scaling, backpressure, observable delivery và failure isolation.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006",
      "P2-DEC-009",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-12-007",
    "phase_2c_c3_actions": [
      "C3_APPROVED_SEMANTIC_DIRECTIVE"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-12-007",
    "source_context_sha256": "f3dd7358382f7eb0d5bb37add5b6857ade11d9f5edbb4c20a36e0bdf875fecad",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "1c08d6ac5478e1546c37a4465473dae2147718d534a760a7df6ac0adb2d856bb",
    "source_fingerprint_before_c3": "7ce50d9ee2f5e107a6ec83c678b58d50f3102504692cad923537e5d5b1847168",
    "source_lines": "L3783-L3872",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-12-007"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "PERFORMANCE_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-12-007",
  "title": "Message Queue và Channel Adapter phải đáp ứng approved service tier, performance budget, SLO và …",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
