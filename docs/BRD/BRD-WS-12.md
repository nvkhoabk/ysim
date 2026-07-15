---
document_code: "BRD-WS-12"
title: "Communication Platform, Notification & Engagement"
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

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-12-001 — Communication Platform là Platform Capability độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-001-AC001",
      "given": "the applicable business context, actor, and input for Communication Platform là Platform Capability độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "BD-12-001-O001"
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
        "BD-12-001-AC001"
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
    "source_fingerprint": "a0c02fb36ec8068f3836e087d997fe4a9a6cd0aad4191e207c9481e4f8c4cdaa",
    "source_lines": "L636-L639",
    "source_section": "32. Business Decisions (Locked) > BD-12-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-002-AC001",
      "given": "the applicable business context, actor, and input for Notification sử dụng Event-Driven Architecture",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-12-002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Notification sử dụng Event-Driven Architecture",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-12-002-O001"
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
        "BD-12-002-AC001",
        "BD-12-002-AC002"
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
    "source_fingerprint": "ff4fc93634cb4b86db79abe8c8e2a81716f7fdcfcf9475209ca12aedf06ae6ee",
    "source_lines": "L642-L645",
    "source_section": "32. Business Decisions (Locked) > BD-12-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-003-AC001",
      "given": "the applicable business context, actor, and input for Notification được quyết định bằng Communication Matrix",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-12-003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Notification được quyết định bằng Communication Matrix",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-12-003-O001"
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
        "BD-12-003-AC001",
        "BD-12-003-AC002"
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
    "source_fingerprint": "b59981ea8de4d103bb297d569b7eb1a81f3d6e980a4fdb0f2d4490573da5d9d9",
    "source_lines": "L648-L651",
    "source_section": "32. Business Decisions (Locked) > BD-12-003"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-004-AC001",
      "given": "the applicable business context, actor, and input for Portal Announcement là một Communication Channel",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-12-004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Portal Announcement là một Communication Channel",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-12-004-O001"
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
        "BD-12-004-AC001",
        "BD-12-004-AC002"
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
    "source_fingerprint": "03a181245dbd21637a31530ad1b9de93482f5b951bb01baf09b65b456dae84d4",
    "source_lines": "L654-L657",
    "source_section": "32. Business Decisions (Locked) > BD-12-004"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-005-AC001",
      "given": "the applicable business context, actor, and input for Personal Inbox luôn là Delivery Channel cuối cùng",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-005-O001"
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
        "BD-12-005-AC001"
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
    "source_fingerprint": "89db25a37d9e71efe97e0efa13762f13a3b58cfd779ea9f56c8ed477495ee823",
    "source_lines": "L660-L663",
    "source_section": "32. Business Decisions (Locked) > BD-12-005"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-12-006-AC001",
      "given": "a candidate ContactPoint là Business Object record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-12-006-O001"
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
        "BD-12-006-AC001"
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
    "source_fingerprint": "5f185020e6cddb4a3e85a5865fa54b8bce2e6f24e1acfcd2a639db33575b67d6",
    "source_lines": "L666-L669",
    "source_section": "32. Business Decisions (Locked) > BD-12-006"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-007-AC001",
      "given": "the applicable business context, actor, and input for Notification Preference sử dụng Matrix",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-12-007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Notification Preference sử dụng Matrix",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-12-007-O001"
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
        "BD-12-007-AC001",
        "BD-12-007-AC002"
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
    "source_fingerprint": "dbb31a297a1537124414d5b31ce9c6361b688e793825a6ce4e843f8fac8b31fa",
    "source_lines": "L672-L675",
    "source_section": "32. Business Decisions (Locked) > BD-12-007"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-008-AC001",
      "given": "the applicable business context, actor, and input for Template hỗ trợ Parent Override",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "an override is accepted only for a policy marked override-eligible, with an explicit reason and the required approval; otherwise the inherited or system policy remains effective",
      "verifies": [
        "BD-12-008-O001"
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
        "BD-12-008-AC001"
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
    "source_fingerprint": "d80600888e9327eba88b77fa5e9d48446d8044afff4f2ea477e102044db12324",
    "source_lines": "L678-L681",
    "source_section": "32. Business Decisions (Locked) > BD-12-008"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-009-AC001",
      "given": "the applicable business context, actor, and input for Localization hỗ trợ nhiều chuẩn hiển thị",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-009-O001"
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
        "BD-12-009-AC001"
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
    "source_fingerprint": "25ad65f8d5e4e5e0a3cb028f14d027ddfe270c817c5303689034f1d1fdd88b4c",
    "source_lines": "L684-L687",
    "source_section": "32. Business Decisions (Locked) > BD-12-009"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-010-AC001",
      "given": "the applicable business context, actor, and input for Notification Routing dựa trên Business Event",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-12-010-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Notification Routing dựa trên Business Event",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-12-010-O001"
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
        "BD-12-010-AC001",
        "BD-12-010-AC002"
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
    "source_fingerprint": "fc4f6f86fe8c6f0961c87b0bdfbeed0dee9bdf8ba76e40d376801ea7492ceaa4",
    "source_lines": "L690-L693",
    "source_section": "32. Business Decisions (Locked) > BD-12-010"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-011-AC001",
      "given": "the applicable business context, actor, and input for Retry Policy mặc định là 03 lần, cách nhau 05 phút",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-011-O001"
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
        "BD-12-011-AC001"
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
    "source_fingerprint": "821bc2a315bc4f876c121b4de690dfd7ec8e6fde744037c1ce1ece188b78e4f9",
    "source_lines": "L696-L699",
    "source_section": "32. Business Decisions (Locked) > BD-12-011"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-012-AC001",
      "given": "the applicable business context, actor, and input for Communication Log hỗ trợ Search, Export và Retention",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-012-O001"
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
        "BD-12-012-AC001"
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
    "source_fingerprint": "59f035b98e49a0e8d9f3e06dd4b391d4340853aa673ea26482e749042fffac72",
    "source_lines": "L702-L705",
    "source_section": "32. Business Decisions (Locked) > BD-12-012"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-013-AC001",
      "given": "the applicable business context, actor, and input for Notification Subscription và Notification Category sử dụng Reference Data Management",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-013-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-12-013-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Notification Subscription và Notification Category sử dụng Reference Data Management",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-12-013-O001"
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
        "BD-12-013-AC001",
        "BD-12-013-AC002"
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
    "source_fingerprint": "f7335f4ed6e7b3432be1c29b76bb0d69afbe1474cbbc6ce2e7d9e0d388122e6c",
    "source_lines": "L708-L711",
    "source_section": "32. Business Decisions (Locked) > BD-12-013"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-014-AC001",
      "given": "the applicable business context, actor, and input for Version 2 sử dụng Real-time Notification",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-014-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-12-014-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Version 2 sử dụng Real-time Notification",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-12-014-O001"
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
        "BD-12-014-AC001",
        "BD-12-014-AC002"
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
    "source_fingerprint": "f34907371379ceef0ba2be38cd4c21deb7ab70f58b07c8c754c69fab9dc889b7",
    "source_lines": "L714-L717",
    "source_section": "32. Business Decisions (Locked) > BD-12-014"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-015-AC001",
      "given": "the applicable business context, actor, and input for Notification hỗ trợ Auto Translation",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-015-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-12-015-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Notification hỗ trợ Auto Translation",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-12-015-O001"
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
        "BD-12-015-AC001",
        "BD-12-015-AC002"
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
    "source_fingerprint": "1b34e4f08f33627a416e705f4f3bfa152e00f2b5b2732e52bd473f1c0fdd5262",
    "source_lines": "L720-L723",
    "source_section": "32. Business Decisions (Locked) > BD-12-015"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-016-AC001",
      "given": "the applicable business context, actor, and input for Communication Policy hỗ trợ nhiều tầng Override",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "an override is accepted only for a policy marked override-eligible, with an explicit reason and the required approval; otherwise the inherited or system policy remains effective",
      "verifies": [
        "BD-12-016-O001"
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
        "BD-12-016-AC001"
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
    "source_fingerprint": "e96b9e50a2866e7d244ba24a869cea71f51196e9d2b31db5a93ff598656c893e",
    "source_lines": "L726-L729",
    "source_section": "32. Business Decisions (Locked) > BD-12-016"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-017-AC001",
      "given": "the applicable business context, actor, and input for Do Not Disturb hỗ trợ Emergency Notification",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-017-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-12-017-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Do Not Disturb hỗ trợ Emergency Notification",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-12-017-O001"
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
        "BD-12-017-AC001",
        "BD-12-017-AC002"
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
    "source_fingerprint": "025804be15e2c104b4f6e1a6ecb1dc50bf58f77b6c2c28e574e5a89f81f82336",
    "source_lines": "L732-L735",
    "source_section": "32. Business Decisions (Locked) > BD-12-017"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-018-AC001",
      "given": "the applicable business context, actor, and input for Communication Platform sử dụng Message Queue",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-018-O001"
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
        "BD-12-018-AC001"
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
    "source_fingerprint": "eec4c519fc880124c47187addcd7527b6a2f627c7bc96d3a2ddcec336c43f0dd",
    "source_lines": "L738-L741",
    "source_section": "32. Business Decisions (Locked) > BD-12-018"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-12-019-AC001",
      "given": "the applicable business context, actor, and input for Communication Platform sử dụng Channel Adapter Pattern",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-12-019-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-12-019-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Communication Platform sử dụng Channel Adapter Pattern",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-12-019-O001"
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
        "BD-12-019-AC001",
        "BD-12-019-AC002"
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
    "source_fingerprint": "fea6d41f72cee1d5d63ac519541232cb4aa95c5f7c68158070b08d5a7d0fa8b0",
    "source_lines": "L744-L747",
    "source_section": "32. Business Decisions (Locked) > BD-12-019"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-12-R002-AC001",
      "given": "the applicable business context, actor, and input for Notification không được phép mất hoàn toàn",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-12-R002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-12-R002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Notification không được phép mất hoàn toàn",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-12-R002-O001"
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
        "BRD-WS-12-R002-AC001",
        "BRD-WS-12-R002-AC002"
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
    "source_lines": "L194",
    "source_section": "7. Notification Channels"
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
    "source_fingerprint": "0c08408b016c87d8fa18f3b17511efb9c58300c2e823856416bcffa6813583ad",
    "source_lines": "L232-L245",
    "source_section": "9. Personal Inbox"
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
    "source_fingerprint": "0908f88d6e022eb89e8e7b787e63cb9667b6ba0d7bbfb4cc460a39eb30b44601",
    "source_lines": "L331-L350",
    "source_section": "14. Localization"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-12-R005-AC001",
      "given": "the applicable business context, actor, and input for Communication Log phải hỗ trợ: - Search",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-12-R005-O001"
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
        "BRD-WS-12-R005-AC001"
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
    "source_lines": "L379-L381",
    "source_section": "17. Communication Log"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-12-R006-AC001",
      "given": "the applicable business context, actor, and input for Communication Log phải hỗ trợ: - Export",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-12-R006-O001"
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
        "BRD-WS-12-R006-AC001"
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
    "source_fingerprint": "800aa61c3107c68bbaf7bf872cafb707b6dc47ada0b9257f16928c6a1f305496",
    "source_lines": "L379-L382",
    "source_section": "17. Communication Log"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-12-R007-AC001",
      "given": "the applicable business context, actor, and input for Communication Log phải hỗ trợ: - Retention Policy",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-12-R007-O001"
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
        "BRD-WS-12-R007-AC001"
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
    "source_fingerprint": "af13aae3545555568dfd8d3114b2e6f71acb7fa85188b5823b8f1741a144c33d",
    "source_lines": "L379-L383",
    "source_section": "17. Communication Log"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-12-R008-AC001",
      "given": "the applicable business context, actor, and input for Communication Log phải hỗ trợ: - Auto Rotation",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-12-R008-O001"
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
        "BRD-WS-12-R008-AC001"
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
    "source_fingerprint": "194353a1c29ddb4580ed390e23ecc09b08b000d07aaa0fe5d653f61e8b5b2492",
    "source_lines": "L379-L384",
    "source_section": "17. Communication Log"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-12-R009-AC001",
      "given": "the applicable business context, actor, and input for Portal luôn hỗ trợ: - Read",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-12-R009-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-12-R009-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Portal luôn hỗ trợ: - Read",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-12-R009-O001"
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
        "BRD-WS-12-R009-AC001",
        "BRD-WS-12-R009-AC002"
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
    "source_lines": "L394-L396",
    "source_section": "18. Read Receipt"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-12-R010-AC001",
      "given": "the applicable business context, actor, and input for Portal luôn hỗ trợ: - Read Time",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-12-R010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-12-R010-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Portal luôn hỗ trợ: - Read Time",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-12-R010-O001"
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
        "BRD-WS-12-R010-AC001",
        "BRD-WS-12-R010-AC002"
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
    "source_fingerprint": "92a37d4858b46fb53eac60713b744de4b5b31421833b3060c56532d5eb186ece",
    "source_lines": "L394-L397",
    "source_section": "18. Read Receipt"
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
    "source_lines": "L409",
    "source_section": "19. Notification Subscription"
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
    "source_lines": "L465",
    "source_section": "23. Real-time Communication"
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
    "source_fingerprint": "7f7e1b6ec362444619a3f7b74e69c9d48be285e0eaa5921a8401e832c100ba91",
    "source_lines": "L481-L490",
    "source_section": "25. Attachment"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BRD-WS-12-R014-AC001",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Communication Consent tuân thủ GDPR",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BRD-WS-12-R014-O001"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "PRIVACY_POLICY_DENIAL_V1",
      "criterion_id": "BRD-WS-12-R014-AC002",
      "given": "a data action whose purpose, consent, scope, or effective policy does not permit the requested data use under Communication Consent tuân thủ GDPR",
      "observable_evidence": "actor, purpose, consent and scope, effective policies, denial reason, exposed-data comparison, and audit record",
      "then": "the data action is denied, no additional protected data is exposed or changed, and the policy reason is audited",
      "verifies": [
        "BRD-WS-12-R014-O001"
      ],
      "when": "privacy conformance is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-12-R014-AC001",
        "BRD-WS-12-R014-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-12-R014-O001",
      "obligation_text": "Communication Consent tuân thủ GDPR"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-12-R014 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-12-R014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-12-R014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-12-R014 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-12-R014-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-12-R014 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L568",
    "source_section": "29. Communication Consent"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-12-001-AC001",
      "given": "the applicable business context, actor, and input for Communication Platform độc lập với Business Domain",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "EP-12-001-O001"
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
        "EP-12-001-AC001"
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
    "source_fingerprint": "55f272bf9d277b251bcb74de4365afa549e1106cfa729bff3059be8b3754cf7a",
    "source_lines": "L752-L755",
    "source_section": "33. Enterprise Design Principles > EP-12-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-12-002-AC001",
      "given": "the applicable business context, actor, and input for Business Domain chỉ Publish Business Event",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-12-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-12-002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Domain chỉ Publish Business Event",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-12-002-O001"
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
        "EP-12-002-AC001",
        "EP-12-002-AC002"
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
    "source_fingerprint": "992001c742dc1a0365e4a25a558cc4e0cbe8d0803575b517a1e30ed386953992",
    "source_lines": "L758-L761",
    "source_section": "33. Enterprise Design Principles > EP-12-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-12-003-AC001",
      "given": "the applicable business context, actor, and input for Communication Matrix quyết định toàn bộ hành vi gửi Notification",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-12-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-12-003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Communication Matrix quyết định toàn bộ hành vi gửi Notification",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-12-003-O001"
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
        "EP-12-003-AC001",
        "EP-12-003-AC002"
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
    "source_fingerprint": "fdf33b8f7e1455ba7ca68c0d93a34c7bd99af4788722ffcdfa1e28fcbf7ae855",
    "source_lines": "L764-L767",
    "source_section": "33. Enterprise Design Principles > EP-12-003"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-12-004-AC001",
      "given": "the applicable business context, actor, and input for Personal Inbox là nơi lưu giữ Notification lâu dài",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-12-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-12-004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Personal Inbox là nơi lưu giữ Notification lâu dài",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-12-004-O001"
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
        "EP-12-004-AC001",
        "EP-12-004-AC002"
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
    "source_fingerprint": "fa3c5793657226f9a15248a09cddb40df0ff602fdcf5e9397be0767f21ecf012",
    "source_lines": "L770-L773",
    "source_section": "33. Enterprise Design Principles > EP-12-004"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-12-005-AC001",
      "given": "the applicable business context, actor, and input for Notification luôn hỗ trợ Localization và Auto Translation",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-12-005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-12-005-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Notification luôn hỗ trợ Localization và Auto Translation",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-12-005-O001"
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
        "EP-12-005-AC001",
        "EP-12-005-AC002"
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
    "source_fingerprint": "5a07e659932c14e0c4a2f067f806c173fffd113b4f76052f8e0d97b2d1fdf28b",
    "source_lines": "L776-L779",
    "source_section": "33. Enterprise Design Principles > EP-12-005"
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
### EP-12-006 — Communication Platform hỗ trợ mở rộng Channel mà không thay đổi Business Logic

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-12-006-AC001",
      "given": "the applicable business context, actor, and input for Communication Platform hỗ trợ mở rộng Channel mà không thay đổi Business Logic",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-12-006-O001"
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
        "EP-12-006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-12-006-O001",
      "obligation_text": "Communication Platform hỗ trợ mở rộng Channel mà không thay đổi Business Logic"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Communication Platform hỗ trợ mở rộng Channel mà không thay đổi Business Logic.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-12-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-12-006",
    "source_context_sha256": "a1a80a93c20b0452764c32a8e8b16b11f7cbb37f579027ef33ac5abc81f9bde5",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "d168f3ed2341ffd0ea3416d35adf67ca1efc1da408f946bf5744c7cfcde97744",
    "source_lines": "L782-L785",
    "source_section": "33. Enterprise Design Principles > EP-12-006"
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
  "title": "Communication Platform hỗ trợ mở rộng Channel mà không thay đổi Business Logic",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-12-007 — Message Queue và Channel Adapter là nền tảng mở rộng Performance

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "EP-12-007-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Message Queue và Channel Adapter là nền tảng mở rộng Performance",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "EP-12-007-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "EP-12-007-AC002",
      "given": "a proposed change with missing traceability or a boundary violation under Message Queue và Channel Adapter là nền tảng mở rộng Performance",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "EP-12-007-O001"
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
        "EP-12-007-AC001",
        "EP-12-007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-12-007-O001",
      "obligation_text": "Message Queue và Channel Adapter là nền tảng mở rộng Performance"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Message Queue và Channel Adapter là nền tảng mở rộng Performance.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006",
      "P2-DEC-009"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-12-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-12-007",
    "source_context_sha256": "f3dd7358382f7eb0d5bb37add5b6857ade11d9f5edbb4c20a36e0bdf875fecad",
    "source_document": "docs/BRD/BRD-WS-12.md",
    "source_fingerprint": "7ce50d9ee2f5e107a6ec83c678b58d50f3102504692cad923537e5d5b1847168",
    "source_lines": "L788-L791",
    "source_section": "33. Enterprise Design Principles > EP-12-007"
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
  "title": "Message Queue và Channel Adapter là nền tảng mở rộng Performance",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
