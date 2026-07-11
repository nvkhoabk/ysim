---
document_code: BRD-WS-12
document_name: Communication Platform, Notification & Engagement
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-12
---

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