---
document_code: BRD-WS-11
document_name: Customer Service, Ticketing & Customer Lifecycle
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-11
---

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