---
document_code: "BRD-POLICY-INDEX"
title: "Enterprise Policy Registry"
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

# Enterprise Policy Registry

## BRD-POLICY-INDEX

---

# 1. Purpose

Enterprise Policy Registry là tài liệu quản lý tập trung toàn bộ **Business Policy** của nền tảng YSim.

Policy định nghĩa cách Platform đưa ra quyết định, xử lý nghiệp vụ và điều khiển hành vi của hệ thống.

Business Policy không mô tả Business Requirement và cũng không mô tả Source Code.

Business Policy trả lời câu hỏi:

> **Platform sẽ xử lý như thế nào khi một Business Situation xảy ra?**

Enterprise Policy Registry là **Source of Truth** cho toàn bộ Business Policy của nền tảng YSim.

---

# 2. Objectives

Enterprise Policy Registry được xây dựng nhằm:

- Chuẩn hóa toàn bộ Business Policy.
- Chuẩn hóa Commercial Policy.
- Chuẩn hóa Financial Policy.
- Chuẩn hóa Security Policy.
- Chuẩn hóa Communication Policy.
- Chuẩn hóa Operational Policy.
- Chuẩn hóa Policy Governance.
- Chuẩn hóa Policy Override.
- Chuẩn hóa Policy Versioning.
- Chuẩn hóa Policy Inheritance.

Enterprise Policy Registry là nền tảng để:

- Configuration Management
- Business Rules
- Runtime Decision
- Approval Workflow
- Feature Toggle
- Enterprise Governance

---

# 3. Scope

Enterprise Policy Registry bao gồm toàn bộ Policy thuộc các Domain:

- Organization
- Commercial
- Pricing
- Promotion
- Order
- Payment
- Inventory
- Fulfillment
- Settlement
- Customer Success
- Communication
- Analytics
- Configuration
- Integration
- Security
- Operations

Ngoài ra còn bao gồm:

- Cross Platform Policy
- Compliance Policy
- Runtime Policy

---

# 4. Policy Classification

Policy được phân loại theo nhóm.

| Type | Description |
|------|-------------|
| Business | Chính sách nghiệp vụ |
| Commercial | Chính sách thương mại |
| Financial | Chính sách tài chính |
| Security | Chính sách bảo mật |
| Communication | Chính sách truyền thông |
| Integration | Chính sách tích hợp |
| Operational | Chính sách vận hành |
| Compliance | Chính sách tuân thủ |
| Platform | Chính sách nền tảng |

Mỗi Policy chỉ thuộc một Type chính.

---

# 5. Policy Scope

Policy có thể được áp dụng ở nhiều Scope khác nhau.

```text
Global

↓

Parent Organization

↓

Organization

↓

Storefront

↓

Department

↓

Team

↓

User
```

Không phải mọi Policy đều hỗ trợ toàn bộ Scope.

Khả năng áp dụng được xác định bởi từng loại Policy.

---

# 6. Policy Inheritance

YSim sử dụng cơ chế kế thừa Policy.

```text
Global

↓

Parent Organization

↓

Organization

↓

Storefront
```

Policy có thể:

- Inherit
- Override
- Disable
- Extend

Policy Inheritance phải được quản lý tập trung.

---

# 7. Policy Priority

Khi có nhiều Policy cùng áp dụng, Platform sử dụng thứ tự ưu tiên sau.

```text
System Policy

↓

Global Policy

↓

Parent Policy

↓

Organization Policy

↓

Storefront Policy

↓

User Policy
```

Policy có Priority cao hơn sẽ được ưu tiên.

---

# 8. Policy Lifecycle

Policy có Lifecycle riêng.

```text
Draft

↓

Pending Approval

↓

Approved

↓

Published

↓

Effective

↓

Deprecated

↓

Archived
```

Chỉ Policy ở trạng thái **Effective** mới được Runtime sử dụng.

---

# 9. Policy Identifier

Mỗi Policy được cấp một mã định danh duy nhất.

Quy ước:

```text
POL-000001

POL-000002

POL-000003
```

Policy ID được sử dụng trong:

- BRD
- Configuration
- API
- Runtime
- Audit
- Architecture Review

Policy ID là bất biến.

---

# 10. Effective Date

Mọi Policy đều có thể hỗ trợ:

- Effective From
- Effective Until

Policy có thể được lập lịch để:

- Publish
- Activate
- Expire

mà không cần triển khai lại hệ thống.

---

# 11. Approval

Policy chỉ được Publish sau khi hoàn thành Approval Workflow.

Approval Rule phụ thuộc:

- Policy Type
- Policy Scope
- Organization
- Role

Mọi Approval phải được ghi Audit.

---

# 12. Runtime Behaviour

Policy được Runtime Engine đọc thông qua Configuration.

Policy không được Hard-code trong Source Code khi có thể cấu hình.

Platform hỗ trợ:

- Runtime Reload
- Version Selection
- Rollback
- Validation

theo các nguyên tắc đã định nghĩa trong WS-14.

---

# 13. Policy Principles

## POL-P01 — Configuration First

Policy ưu tiên được cấu hình.

Không Hard-code khi có thể cấu hình.

---

## POL-P02 — Inheritance

Policy ưu tiên kế thừa.

Chỉ Override khi thực sự cần thiết.

---

## POL-P03 — Versioned

Policy luôn hỗ trợ Version.

---

## POL-P04 — Effective Date

Policy hỗ trợ Effective Date.

---

## POL-P05 — Approval Required

Policy chỉ có hiệu lực sau Approval.

---

## POL-P06 — Auditable

Mọi thay đổi Policy phải được Audit.

---

## POL-P07 — Runtime Ready

Policy được Runtime Engine sử dụng trực tiếp.

---

## POL-P08 — Business Driven

Policy phản ánh quyết định nghiệp vụ.

Không phản ánh thiết kế kỹ thuật.

---

## POL-P09 — Conflict Managed

Policy phải có cơ chế xử lý xung đột giữa các Scope.

---

## POL-P10 — Enterprise Governance

Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance.

Mọi Policy mới phải trải qua:

- Architecture Review
- Approval
- Versioning
- Audit
- Traceability

---

# 14. Relationship to Other Documents

Enterprise Policy Registry có quan hệ với:

| Document | Relationship |
|----------|--------------|
| BRD Workshop | Nguồn gốc Business Policy |
| BRD-BO-INDEX | Policy điều khiển Business Object |
| BRD-CAP-INDEX | Policy điều khiển Capability |
| BRD-EVENT-INDEX | Policy điều khiển Event Processing |
| DMS | Business Rule |
| Configuration Registry | Runtime Configuration |
| SDD | Policy Engine |
| API Specification | Runtime Behaviour |
| CIP | Implementation |

Enterprise Policy Registry là **Enterprise Policy Dictionary** và là tài liệu tham chiếu thống nhất cho toàn bộ Platform.

------

# 15. Enterprise Policy Registry

## 15.1 Organization Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-000001 | Organization Policy | Business | Organization | Organization Management | Organization | Yes | Yes | Yes | WS-03 |
| POL-000002 | Organization Capability Policy | Business | Organization Capability | Organization Capability Management | Organization | Yes | Yes | Yes | WS-03 |
| POL-000003 | Storefront Policy | Business | Storefront | Storefront Management | Storefront | Yes | Yes | Yes | WS-03 |
| POL-000004 | Organization Hierarchy Policy | Business | Organization Relationship | Organization Hierarchy | Global | No | Yes | Yes | WS-03 |
| POL-000005 | Organization Onboarding Policy | Business | Organization Onboarding Checklist | Organization Onboarding | Organization | Yes | Yes | Yes | WS-11 |

---

## 15.2 Commercial Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-010001 | Commercial Policy | Commercial | Commercial Agreement | Commercial Management | Organization | Yes | Yes | Yes | WS-05 |
| POL-010002 | Pricing Policy | Commercial | Price Book | Pricing Engine | Organization | Yes | Yes | Yes | WS-05 |
| POL-010003 | Revenue Sharing Policy | Commercial | Revenue Sharing Rule | Revenue Sharing | Organization | Yes | Yes | Yes | WS-05 |
| POL-010004 | Payment Owner Policy | Commercial | Payment Owner | Payment Owner Management | Organization | Yes | Yes | Yes | WS-05 |

---

## 15.3 Promotion Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-020001 | Promotion Policy | Business | Promotion | Promotion Management | Organization | Yes | Yes | Yes | WS-06 |
| POL-020002 | Coupon Policy | Business | Coupon | Coupon Management | Organization | Yes | Yes | Yes | WS-06 |
| POL-020003 | Campaign Policy | Business | Campaign | Campaign Management | Organization | Yes | Yes | Yes | WS-06 |
| POL-020004 | Promotion Funding Policy | Commercial | Promotion Funding | Promotion Funding | Organization | Yes | Yes | Yes | WS-06 |

---

## 15.4 Order Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-030001 | Shopping Cart Policy | Business | Shopping Cart | Shopping Cart | Storefront | Yes | No | Yes | WS-07 |
| POL-030002 | Checkout Policy | Business | Checkout Session | Checkout | Storefront | Yes | No | Yes | WS-07 |
| POL-030003 | Sales Order Policy | Business | Sales Order | Sales Order Management | Organization | Yes | Yes | Yes | WS-07 |
| POL-030004 | Procurement Policy | Business | Purchase Order | Purchase Order Management | Organization | Yes | Yes | Yes | WS-07 |
| POL-030005 | Order Cancellation Policy | Business | Sales Order | Sales Order Management | Organization | Yes | Yes | Yes | WS-07 |

---

## 15.5 Payment Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-040001 | Payment Policy | Financial | Payment | Payment Management | Organization | Yes | Yes | Yes | WS-08 |
| POL-040002 | Payment Retry Policy | Financial | Payment Attempt | Payment Retry | Platform | Yes | Yes | Yes | WS-08 |
| POL-040003 | Refund Policy | Financial | Refund | Refund Management | Organization | Yes | Yes | Yes | WS-08 |
| POL-040004 | Offline Payment Policy | Financial | Payment | Offline Payment | Organization | Yes | Yes | Yes | WS-08 |
| POL-040005 | Merchant Policy | Commercial | Merchant Account | Merchant Account Management | Organization | Yes | Yes | Yes | WS-08 |

---

## 15.6 Inventory & Fulfillment Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-050001 | Inventory Allocation Policy | Business | Inventory Allocation | Allocation Engine | Platform | Yes | Yes | Yes | WS-09 |
| POL-050002 | Inventory Reservation Policy | Business | Inventory Reservation | Inventory Reservation | Platform | Yes | Yes | Yes | WS-09 |
| POL-050003 | Fulfillment Policy | Business | Fulfillment Session | Fulfillment Management | Platform | Yes | Yes | Yes | WS-09 |
| POL-050004 | Delivery Retry Policy | Operational | Fulfillment Task | Delivery Retry | Platform | Yes | Yes | Yes | WS-09 |
| POL-050005 | Customer Assignment Policy | Business | Customer Assignment | Customer Assignment | Organization | Yes | Yes | Yes | WS-09 |

---

## 15.7 Financial & Settlement Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-060001 | Settlement Policy | Financial | Settlement | Settlement Management | Organization | Yes | Yes | Yes | WS-10 |
| POL-060002 | Settlement Approval Policy | Financial | Settlement | Settlement Approval | Organization | Yes | Yes | Yes | WS-10 |
| POL-060003 | Commission Policy | Financial | Commission Snapshot | Commission Management | Organization | Yes | Yes | Yes | WS-10 |
| POL-060004 | Wallet Policy | Financial | Wallet | Wallet Management | Organization | Yes | Yes | Yes | WS-10 |
| POL-060005 | Ledger Policy | Financial | Ledger Entry | Financial Ledger | Platform | No | Yes | Yes | WS-10 |

------

# 15.8 Customer Success Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-070001 | Support Policy | Business | Ticket | Customer Support | Organization | Yes | Yes | Yes | WS-11 |
| POL-070002 | Ticket Assignment Policy | Business | Ticket | Ticket Management | Organization | Yes | Yes | Yes | WS-11 |
| POL-070003 | Ticket Escalation Policy | Business | Support Queue | Support Queue Routing | Organization | Yes | Yes | Yes | WS-11 |
| POL-070004 | SLA Policy | Business | SLA | Customer Support | Organization | Yes | Yes | Yes | WS-11 |
| POL-070005 | Knowledge Base Policy | Business | Knowledge Base Article | Knowledge Base | Organization | Yes | Yes | Yes | WS-11 |
| POL-070006 | Satisfaction Survey Policy | Business | Satisfaction Survey | Satisfaction Survey | Organization | Yes | Yes | Yes | WS-11 |
| POL-070007 | Feature Request Policy | Business | Feature Request | Feature Request Management | Platform | Yes | Yes | Yes | WS-11 |

---

# 15.9 Communication Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-080001 | Notification Policy | Communication | Notification | Notification Management | Organization | Yes | Yes | Yes | WS-12 |
| POL-080002 | Notification Routing Policy | Communication | Notification Event | Notification Routing | Platform | Yes | Yes | Yes | WS-12 |
| POL-080003 | Communication Policy | Communication | Communication Policy | Communication Policy | Organization | Yes | Yes | Yes | WS-12 |
| POL-080004 | Subscription Policy | Communication | Notification Subscription | Customer Subscription | Customer | Yes | No | Yes | WS-12 |
| POL-080005 | Do Not Disturb Policy | Communication | User Preference | Notification Management | User | Yes | No | Yes | WS-12 |
| POL-080006 | Localization Policy | Platform | Localization Resource | Multi-language Notification | Organization | Yes | Yes | Yes | WS-12 |
| POL-080007 | Retry Policy | Operational | Delivery Attempt | Notification Routing | Platform | Yes | Yes | Yes | WS-12 |
| POL-080008 | Communication Retention Policy | Compliance | Communication Log | Communication Management | Platform | Yes | Yes | Yes | WS-12 |

---

# 15.10 Analytics & Reporting Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-090001 | Dashboard Policy | Business | Dashboard | Dashboard Management | Organization | Yes | Yes | Yes | WS-13 |
| POL-090002 | Report Policy | Business | Report | Report Management | Organization | Yes | Yes | Yes | WS-13 |
| POL-090003 | Report Permission Policy | Security | Report | Report Management | Organization | Yes | Yes | Yes | WS-13 |
| POL-090004 | Report Schedule Policy | Operational | Report Schedule | Report Scheduling | Organization | Yes | Yes | Yes | WS-13 |
| POL-090005 | Alert Policy | Operational | Alert Rule | Alert Management | Organization | Yes | Yes | Yes | WS-13 |
| POL-090006 | KPI Evaluation Policy | Business | KPI Definition | KPI Management | Organization | Yes | Yes | Yes | WS-13 |

---

# 15.11 Platform Configuration Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-100001 | Configuration Policy | Platform | Configuration | Configuration Management | Platform | Yes | Yes | Yes | WS-14 |
| POL-100002 | Reference Data Policy | Platform | Reference Data | Reference Data Management | Platform | Yes | Yes | Yes | WS-14 |
| POL-100003 | Dictionary Policy | Platform | Dictionary | Dictionary Management | Platform | Yes | Yes | Yes | WS-14 |
| POL-100004 | Business Rule Policy | Platform | Business Rule | Business Rule Management | Platform | Yes | Yes | Yes | WS-14 |
| POL-100005 | Metadata Policy | Platform | Metadata | Metadata Management | Platform | Yes | Yes | Yes | WS-14 |
| POL-100006 | Runtime Configuration Policy | Platform | Configuration | Runtime Configuration Reload | Platform | Yes | Yes | Yes | WS-14 |
| POL-100007 | Organization Template Policy | Platform | Organization Template | Organization Template | Platform | Yes | Yes | Yes | WS-14 |

---

# 15.12 Integration Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-110001 | Connector Policy | Integration | Connector | Connector Management | Platform | Yes | Yes | Yes | WS-15 |
| POL-110002 | Connector Routing Policy | Integration | Connector Routing Rule | Connector Routing | Platform | Yes | Yes | Yes | WS-15 |
| POL-110003 | Callback Policy | Integration | Callback | Callback Management | Platform | Yes | Yes | Yes | WS-15 |
| POL-110004 | Queue Policy | Operational | Queue | Queue Management | Platform | Yes | Yes | Yes | WS-15 |
| POL-110005 | Event Publishing Policy | Integration | Business Event | Business Event Platform | Platform | Yes | Yes | Yes | WS-15 |
| POL-110006 | API Version Policy | Integration | API Version | API Gateway | Platform | Yes | Yes | Yes | WS-15 |
| POL-110007 | Circuit Breaker Policy | Operational | Connector | Connector Management | Platform | Yes | Yes | Yes | WS-15 |
| POL-110008 | Rate Limiting Policy | Operational | Connector | API Gateway | Platform | Yes | Yes | Yes | WS-15 |

---

# 15.13 Security Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-120001 | Authentication Policy | Security | Session | Authentication | Platform | Yes | Yes | Yes | WS-16 |
| POL-120002 | Authorization Policy | Security | Permission | Authorization | Platform | Yes | Yes | Yes | WS-16 |
| POL-120003 | Data Classification Policy | Security | Data Classification | Data Protection | Platform | Yes | Yes | Yes | WS-16 |
| POL-120004 | Data Masking Policy | Security | Permission | Data Protection | Platform | Yes | Yes | Yes | WS-16 |
| POL-120005 | Consent Policy | Compliance | Customer Consent | Customer Consent | Platform | Yes | Yes | Yes | WS-16 |
| POL-120006 | Secret Rotation Policy | Security | Secret | Secret Management | Platform | Yes | Yes | Yes | WS-16 |
| POL-120007 | Risk Policy | Security | Risk Rule | Risk Management | Platform | Yes | Yes | Yes | WS-16 |
| POL-120008 | Account Lock Policy | Security | Session | Authentication | Platform | Yes | Yes | Yes | WS-16 |
| POL-120009 | Audit Retention Policy | Compliance | Audit Log | Audit Logging | Platform | Yes | Yes | Yes | WS-16 |

---

# 15.14 Platform Operations Domain

| Policy ID | Policy | Type | Main Business Object | Main Capability | Default Scope | Override | Approval | Runtime | Workshop |
|------------|---------|------|----------------------|-----------------|---------------|----------|----------|---------|----------|
| POL-130001 | Monitoring Policy | Operational | Monitoring Profile | Monitoring | Platform | Yes | Yes | Yes | WS-17 |
| POL-130002 | Alert Policy | Operational | Alert Rule | Alert Management | Platform | Yes | Yes | Yes | WS-17 |
| POL-130003 | Scheduler Policy | Operational | Scheduler Job | Scheduler | Platform | Yes | Yes | Yes | WS-17 |
| POL-130004 | Worker Policy | Operational | Worker | Worker Management | Platform | Yes | Yes | Yes | WS-17 |
| POL-130005 | Maintenance Policy | Operational | Maintenance Window | Maintenance Management | Platform | Yes | Yes | Yes | WS-17 |
| POL-130006 | Backup Policy | Operational | Backup Policy | Backup Management | Platform | Yes | Yes | Yes | WS-17 |
| POL-130007 | Disaster Recovery Policy | Operational | Disaster Recovery Policy | Disaster Recovery | Platform | Yes | Yes | Yes | WS-17 |
| POL-130008 | Capacity Policy | Operational | Capacity Policy | Capacity Management | Platform | Yes | Yes | Yes | WS-17 |
| POL-130009 | Feature Flag Policy | Platform | Feature Flag | Feature Flag Management | Platform | Yes | Yes | Yes | WS-17 |
| POL-130010 | Kill Switch Policy | Platform | Feature Flag | Feature Flag Management | Platform | Yes | Yes | Yes | WS-17 |

------

# 16. Enterprise Policy Matrix

Business Policy là cầu nối giữa Business Capability và Business Event.

| Policy | Main Business Object | Main Capability | Primary Event | Runtime Decision |
|---------|----------------------|-----------------|---------------|------------------|
| Organization Policy | Organization | Organization Management | OrganizationActivated | Organization Lifecycle |
| Commercial Policy | Commercial Agreement | Commercial Management | CommercialAgreementActivated | Commercial Decision |
| Pricing Policy | Price Book | Pricing Engine | PriceBookPublished | Pricing Decision |
| Promotion Policy | Promotion | Promotion Management | PromotionActivated | Promotion Decision |
| Checkout Policy | Checkout Session | Checkout | CheckoutCompleted | Checkout Validation |
| Payment Policy | Payment | Payment Management | PaymentSucceeded | Payment Decision |
| Inventory Allocation Policy | Inventory Allocation | Allocation Engine | InventoryAllocated | Allocation Decision |
| Fulfillment Policy | Fulfillment Session | Fulfillment Management | FulfillmentCompleted | Fulfillment Decision |
| Settlement Policy | Settlement | Settlement Management | SettlementCompleted | Settlement Decision |
| Support Policy | Ticket | Customer Support | TicketCreated | Support Routing |
| Notification Policy | Notification | Notification Management | NotificationCreated | Communication Routing |
| Security Policy | Permission | Authorization | PermissionChanged | Access Decision |
| Scheduler Policy | Scheduler Job | Scheduler | SchedulerTriggered | Job Scheduling |

---

# 17. Policy Decision Flow

Business Event không trực tiếp thực hiện hành động.

Platform luôn đánh giá Policy trước.

```text
Business Event
       │
       ▼
Policy Decision Engine
       │
       ▼
Business Rule Engine
       │
       ▼
Capability Execution
       │
       ▼
Business Event
```

Ví dụ:

```text
PaymentSucceeded
       │
       ▼
Payment Policy
       │
       ▼
Settlement Policy
       │
       ▼
Inventory Allocation Policy
       │
       ▼
Fulfillment Policy
```

Mô hình này giúp thay đổi hành vi nghiệp vụ thông qua cấu hình Policy mà không cần thay đổi mã nguồn.

---

# 18. Policy Inheritance Matrix

| Scope | Inherit | Override | Disable |
|--------|---------|----------|----------|
| Global | N/A | No | No |
| Parent Organization | Yes | Yes | No |
| Organization | Yes | Yes | Yes |
| Storefront | Yes | Yes | Yes |
| Department | Yes | Yes | Yes |
| Team | Yes | Yes | Yes |
| User | Yes | Yes | Yes |

Nguyên tắc:

- Scope thấp hơn ưu tiên kế thừa.
- Chỉ Override khi thực sự cần thiết.
- Không được Override các System Policy bắt buộc.

---

# 19. Policy Conflict Resolution

Khi nhiều Policy cùng áp dụng, Platform sử dụng thứ tự ưu tiên sau:

```text
System Policy
        │
        ▼
Compliance Policy
        │
        ▼
Global Policy
        │
        ▼
Parent Organization Policy
        │
        ▼
Organization Policy
        │
        ▼
Storefront Policy
        │
        ▼
User Policy
```

Nếu vẫn còn xung đột:

- Chính sách có Priority cao hơn được ưu tiên.
- Nếu Priority bằng nhau:
  - Policy cụ thể hơn thắng.
- Nếu vẫn không xác định:
  - Runtime từ chối thực hiện và ghi Audit.

---

# 20. Policy & Business Rule Relationship

Business Policy và Business Rule có vai trò khác nhau.

```text
Business Policy
        │
        ▼
Business Rule
        │
        ▼
Capability Execution
        │
        ▼
Business Event
```

| Business Policy | Business Rule |
|-----------------|---------------|
| Quy định nguyên tắc | Logic xử lý chi tiết |
| Có Approval | Có Version |
| Có Scope | Có Parameter |
| Có Effective Date | Có Expression |
| Có Inheritance | Được Policy sử dụng |

Ví dụ:

Promotion Policy:

- Có cho phép cộng nhiều Promotion?

Business Rule:

- Công thức giảm giá.
- Điều kiện áp dụng Promotion.

---

# 21. Policy Traceability

Mỗi Policy phải có khả năng Trace tới:

- Business Requirement
- Business Capability
- Business Object
- Business Rule
- Business Event
- Configuration
- API
- Permission
- Test Case

Ví dụ:

| Policy | Traceability |
|----------|--------------|
| Payment Policy | BRD → Payment → Rule → Event → API → Test |
| Settlement Policy | BRD → Settlement → Ledger → Report |
| Notification Policy | BRD → Notification → Communication |

---

# 22. Policy Statistics

## 22.1 Statistics by Domain

| Domain | Estimated Policies |
|---------|-------------------:|
| Organization | 5 |
| Commercial | 4 |
| Promotion | 4 |
| Order | 5 |
| Payment | 5 |
| Inventory & Fulfillment | 5 |
| Settlement | 5 |
| Customer Success | 7 |
| Communication | 8 |
| Analytics | 6 |
| Configuration | 7 |
| Integration | 8 |
| Security | 9 |
| Operations | 10 |

---

## 22.2 Statistics by Type

| Type | Estimated Policies |
|------|-------------------:|
| Business | 25+ |
| Commercial | 10+ |
| Financial | 10+ |
| Communication | 8+ |
| Security | 12+ |
| Operational | 15+ |
| Compliance | 6+ |
| Platform | 10+ |

---

## 22.3 Total

Tổng số Enterprise Policy hiện tại:

**Khoảng 110 Policies**

Policy mới sẽ được bổ sung theo từng phiên bản.

Policy ID hiện có không thay đổi.

---

# 23. Enterprise Policy Principles

## POL-EP-001

Policy phản ánh quyết định nghiệp vụ.

---

## POL-EP-002

Policy độc lập với Source Code.

---

## POL-EP-003

Policy độc lập với Database.

---

## POL-EP-004

Policy ưu tiên Configuration.

---

## POL-EP-005

Policy hỗ trợ Runtime Reload.

---

## POL-EP-006

Policy hỗ trợ Versioning.

---

## POL-EP-007

Policy hỗ trợ Inheritance.

---

## POL-EP-008

Policy hỗ trợ Approval và Audit.

---

## POL-EP-009

Policy được Policy Decision Engine đánh giá trước khi Capability được thực thi.

---

## POL-EP-010

Enterprise Policy Registry là Enterprise Policy Dictionary của nền tảng YSim.

---

# 24. Relationship to Enterprise Registries

Enterprise Policy Registry là một phần của Enterprise Registry Layer.

| Registry | Purpose |
|----------|---------|
| BRD-BO-INDEX | Business Object Registry |
| BRD-CAP-INDEX | Business Capability Registry |
| BRD-EVENT-INDEX | Business Event Registry |
| BRD-POLICY-INDEX | Enterprise Policy Registry |
| BRD-SNAPSHOT-INDEX | Snapshot Registry |

Năm Registry này tạo thành Meta Model thống nhất của nền tảng YSim.

---

# 25. Document Status

Status:

**FROZEN**

Enterprise Policy Registry là tài liệu nền tảng quản lý toàn bộ Business Policy của nền tảng YSim.

Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua:

- Architecture Review
- Approval
- Versioning
- Effective Date
- Audit
- Traceability

trước khi được đưa vào Runtime của Platform.

---

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R001 — Không phải mọi Policy đều hỗ trợ toàn bộ Scope

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R001-AC001",
      "given": "the applicable business context, actor, and input for Không phải mọi Policy đều hỗ trợ toàn bộ Scope",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-POLICY-INDEX-R001-O001"
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
        "BRD-POLICY-INDEX-R001-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R001-O001",
      "obligation_text": "Không phải mọi Policy đều hỗ trợ toàn bộ Scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không phải mọi Policy đều hỗ trợ toàn bộ Scope.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-001",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. Policy Scope",
    "source_context_sha256": "34d9a8b5830a3c61092223e74ef583002adc0651ae961b1cb99106259a0b49f6",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "20fbc6e5aa1d3d54c9f4b86b18f871b9369b62c15224ddbee482fc3aadb15a06",
    "source_lines": "L142",
    "source_section": "5. Policy Scope"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_RULE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R001",
  "title": "Không phải mọi Policy đều hỗ trợ toàn bộ Scope",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R002 — Policy Inheritance phải được quản lý tập trung

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R002-AC001",
      "given": "the applicable business context, actor, and input for Policy Inheritance phải được quản lý tập trung",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-POLICY-INDEX-R002-O001"
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
        "BRD-POLICY-INDEX-R002-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R002-O001",
      "obligation_text": "Policy Inheritance phải được quản lý tập trung"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy Inheritance phải được quản lý tập trung.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-002",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Policy Inheritance",
    "source_context_sha256": "c9cbfadd20217ca79389856679a3614c3dccb0ea33097b4b5d14576918e6397a",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "822b8721ae0f51071ef8787dec66d5d19575a0575f04c973e534f2d08be9d366",
    "source_lines": "L175",
    "source_section": "6. Policy Inheritance"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_RULE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R002",
  "title": "Policy Inheritance phải được quản lý tập trung",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R003 — Mỗi Policy được cấp một mã định danh duy nhất

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R003-AC001",
      "given": "the applicable business context, actor, and input for Mỗi Policy được cấp một mã định danh duy nhất",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-POLICY-INDEX-R003-O001"
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
        "BRD-POLICY-INDEX-R003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R003-O001",
      "obligation_text": "Mỗi Policy được cấp một mã định danh duy nhất"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Policy được cấp một mã định danh duy nhất.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-003",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Policy Identifier",
    "source_context_sha256": "92d716710b719c4a8b4bab2866004fe52a665ebf396df1536480587e0a09a37b",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "b441e2c779cbb94f42ae8f77ec9baca70cfcedb1de3a4da5a1d1e3897956fd89",
    "source_lines": "L249",
    "source_section": "9. Policy Identifier"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_RULE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R003",
  "title": "Mỗi Policy được cấp một mã định danh duy nhất",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R004 — mà không cần triển khai lại hệ thống

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R004-AC001",
      "given": "the applicable business context, actor, and input for mà không cần triển khai lại hệ thống",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-POLICY-INDEX-R004-O001"
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
        "BRD-POLICY-INDEX-R004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R004-O001",
      "obligation_text": "mà không cần triển khai lại hệ thống"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "mà không cần triển khai lại hệ thống.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-004",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Effective Date",
    "source_context_sha256": "6365a8620005c6299a4561ebed94dda0a3c8e23acd21758b5de0d3baa3b8ccbc",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "4609a19224cb80841f6599cab41d3dfb2ac6b90e2c03e94447c1b8b33b561dde",
    "source_lines": "L287",
    "source_section": "10. Effective Date"
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
  "stable_id": "BRD-POLICY-INDEX-R004",
  "title": "mà không cần triển khai lại hệ thống",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R005 — Policy chỉ được Publish sau khi hoàn thành Approval Workflow

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R005-AC001",
      "given": "the applicable business context, actor, and input for Policy chỉ được Publish sau khi hoàn thành Approval Workflow",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BRD-POLICY-INDEX-R005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_APPROVAL_BOUNDARY_V1",
      "criterion_id": "BRD-POLICY-INDEX-R005-AC002",
      "given": "a governed change with missing, expired, rejected, or unauthorized approval under Policy chỉ được Publish sau khi hoàn thành Approval Workflow",
      "observable_evidence": "change identity, approval policy and status, approver authorization, rejection or pending reason, and unchanged accepted state",
      "then": "the change does not enter the accepted state and the approval reason and status remain observable",
      "verifies": [
        "BRD-POLICY-INDEX-R005-O001"
      ],
      "when": "the change is requested"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-POLICY-INDEX-R005-AC001",
        "BRD-POLICY-INDEX-R005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R005-O001",
      "obligation_text": "Policy chỉ được Publish sau khi hoàn thành Approval Workflow"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy chỉ được Publish sau khi hoàn thành Approval Workflow.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-005",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Approval",
    "source_context_sha256": "cdef4f316d19879bb16bbf6e6a67c594cc9f13bda339f095c0ff6a2e06002089",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "d3c9452fbd136e0230216bf30d1badd85fad942a30a090d6e95271a9148cce45",
    "source_lines": "L293",
    "source_section": "11. Approval"
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
  "stable_id": "BRD-POLICY-INDEX-R005",
  "title": "Policy chỉ được Publish sau khi hoàn thành Approval Workflow",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R006 — Mọi Approval phải được ghi Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R006-AC001",
      "given": "an operational task within the scope of Mọi Approval phải được ghi Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-POLICY-INDEX-R006-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-POLICY-INDEX-R006-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Mọi Approval phải được ghi Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-POLICY-INDEX-R006-O001"
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
        "BRD-POLICY-INDEX-R006-AC001",
        "BRD-POLICY-INDEX-R006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R006-O001",
      "obligation_text": "Mọi Approval phải được ghi Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R006 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R006 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-POLICY-INDEX-R006-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Approval phải được ghi Audit.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-006",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Approval",
    "source_context_sha256": "cdef4f316d19879bb16bbf6e6a67c594cc9f13bda339f095c0ff6a2e06002089",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "24eea879eab7054106efed23811b322e969835db273c520293c142e5c8ad740f",
    "source_lines": "L302",
    "source_section": "11. Approval"
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
  "stable_id": "BRD-POLICY-INDEX-R006",
  "title": "Mọi Approval phải được ghi Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R007 — Policy không được Hard-code trong Source Code khi có thể cấu hình

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R007-AC001",
      "given": "the applicable business context, actor, and input for Policy không được Hard-code trong Source Code khi có thể cấu hình",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-POLICY-INDEX-R007-O001"
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
        "BRD-POLICY-INDEX-R007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R007-O001",
      "obligation_text": "Policy không được Hard-code trong Source Code khi có thể cấu hình"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy không được Hard-code trong Source Code khi có thể cấu hình.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-007",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Runtime Behaviour",
    "source_context_sha256": "f3aeb7787f9b5cc0ebc7eddf9c4cc088c6989b00812b896be5edd9ad6ecf3f9c",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "75e338810613993a3ab72d169fb64b54e8989e68da6baeb9d0c8fd48f9cf3423",
    "source_lines": "L310",
    "source_section": "12. Runtime Behaviour"
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
  "stable_id": "BRD-POLICY-INDEX-R007",
  "title": "Policy không được Hard-code trong Source Code khi có thể cấu hình",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R008 — Platform luôn đánh giá Policy trước

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R008-AC001",
      "given": "the applicable business context, actor, and input for Platform luôn đánh giá Policy trước",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-POLICY-INDEX-R008-O001"
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
        "BRD-POLICY-INDEX-R008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R008-O001",
      "obligation_text": "Platform luôn đánh giá Policy trước"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform luôn đánh giá Policy trước.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-008",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Policy Decision Flow",
    "source_context_sha256": "9db8ad49640c2b85217d8ec62156218a8e33edf81317a2741e1aea41f8126dfa",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "f294b84c836ee5f6c680b85e80309b8b46127bc62a57634d85429fa2b5e00cef",
    "source_lines": "L633",
    "source_section": "17. Policy Decision Flow"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_RULE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R008",
  "title": "Platform luôn đánh giá Policy trước",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R009 — Mô hình này giúp thay đổi hành vi nghiệp vụ thông qua cấu hình Policy mà không cần thay đổi mã n…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R009-AC001",
      "given": "the applicable business context, actor, and input for Mô hình này giúp thay đổi hành vi nghiệp vụ thông qua cấu hình Policy mà không cần thay đổi mã n…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-POLICY-INDEX-R009-O001"
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
        "BRD-POLICY-INDEX-R009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R009-O001",
      "obligation_text": "Mô hình này giúp thay đổi hành vi nghiệp vụ thông qua cấu hình Policy mà không cần thay đổi mã nguồn"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mô hình này giúp thay đổi hành vi nghiệp vụ thông qua cấu hình Policy mà không cần thay đổi mã nguồn.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-009",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Policy Decision Flow",
    "source_context_sha256": "9db8ad49640c2b85217d8ec62156218a8e33edf81317a2741e1aea41f8126dfa",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "d2beba6ede61fe451033d2c5d26126da3d62a33fc73586af646a7a21f689191e",
    "source_lines": "L669",
    "source_section": "17. Policy Decision Flow"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_RULE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R009",
  "title": "Mô hình này giúp thay đổi hành vi nghiệp vụ thông qua cấu hình Policy mà không cần thay đổi mã n…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R020 — Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Architecture Review

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R020-AC001",
      "given": "the applicable business context, actor, and input for Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Architecture Review",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-POLICY-INDEX-R020-O001"
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
        "BRD-POLICY-INDEX-R020-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R020-O001",
      "obligation_text": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Architecture Review"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Architecture Review",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-020",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Document Status",
    "source_context_sha256": "4919ee457ea116de0db7e12c801c4c7a9933eeec2926421bfc4c721717936a4f",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "a8b2ba49d182690ff6c798be2649743521183443ef88afb1316496b4c3b862ba",
    "source_lines": "L927-L929",
    "source_section": "25. Document Status"
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
  "stable_id": "BRD-POLICY-INDEX-R020",
  "title": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Architecture Review",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R021 — Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Approval

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R021-AC001",
      "given": "the applicable business context, actor, and input for Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Approval",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BRD-POLICY-INDEX-R021-O001"
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
        "BRD-POLICY-INDEX-R021-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R021-O001",
      "obligation_text": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Approval"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Approval",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-021",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Document Status",
    "source_context_sha256": "4919ee457ea116de0db7e12c801c4c7a9933eeec2926421bfc4c721717936a4f",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "fe887bbbc685ffda2cf70165937a01399b2a29ffdc4a712a7e12ab95330b3a2e",
    "source_lines": "L927-L930",
    "source_section": "25. Document Status"
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
  "stable_id": "BRD-POLICY-INDEX-R021",
  "title": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Approval",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R022 — Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Versioning

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R022-AC001",
      "given": "the applicable business context, actor, and input for Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Versioning",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-POLICY-INDEX-R022-O001"
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
        "BRD-POLICY-INDEX-R022-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R022-O001",
      "obligation_text": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Versioning"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Versioning",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-022",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Document Status",
    "source_context_sha256": "4919ee457ea116de0db7e12c801c4c7a9933eeec2926421bfc4c721717936a4f",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "6d3f3d39b8d065930d8258b2865dc190e7a99e0623b03abc3ac7d9c578326e0c",
    "source_lines": "L927-L931",
    "source_section": "25. Document Status"
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
  "stable_id": "BRD-POLICY-INDEX-R022",
  "title": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Versioning",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R023 — Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Effective Date

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R023-AC001",
      "given": "the applicable business context, actor, and input for Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Effective Date",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-POLICY-INDEX-R023-O001"
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
        "BRD-POLICY-INDEX-R023-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R023-O001",
      "obligation_text": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Effective Date"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Effective Date",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-023",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Document Status",
    "source_context_sha256": "4919ee457ea116de0db7e12c801c4c7a9933eeec2926421bfc4c721717936a4f",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "2eaad09557781434bb0126e2957b0c032c08f37762180286e82a2e2048992a1a",
    "source_lines": "L927-L932",
    "source_section": "25. Document Status"
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
  "stable_id": "BRD-POLICY-INDEX-R023",
  "title": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Effective Date",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R024 — Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R024-AC001",
      "given": "an operational task within the scope of Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-POLICY-INDEX-R024-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-POLICY-INDEX-R024-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-POLICY-INDEX-R024-O001"
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
        "BRD-POLICY-INDEX-R024-AC001",
        "BRD-POLICY-INDEX-R024-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R024-O001",
      "obligation_text": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R024 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R024 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R024 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R024 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-POLICY-INDEX-R024-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R024 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Audit",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-024",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Document Status",
    "source_context_sha256": "4919ee457ea116de0db7e12c801c4c7a9933eeec2926421bfc4c721717936a4f",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "e1637d1d0ef6438815e752a05bae811fb531cc9d1eabbfbb5ac531d71a5f22b9",
    "source_lines": "L927-L933",
    "source_section": "25. Document Status"
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
  "stable_id": "BRD-POLICY-INDEX-R024",
  "title": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R025 — Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Traceability

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R025-AC001",
      "given": "the applicable business context, actor, and input for Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Traceability",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-POLICY-INDEX-R025-O001"
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
        "BRD-POLICY-INDEX-R025-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R025-O001",
      "obligation_text": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Traceability"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Traceability",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-025",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Document Status",
    "source_context_sha256": "4919ee457ea116de0db7e12c801c4c7a9933eeec2926421bfc4c721717936a4f",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "bc168a871a130210d841b9c1a5870d4c0f9d86f11a277c24dba162994f23e1ff",
    "source_lines": "L927-L934",
    "source_section": "25. Document Status"
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
  "stable_id": "BRD-POLICY-INDEX-R025",
  "title": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Traceability",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R026 — Nguyên tắc: - Scope thấp hơn ưu tiên kế thừa

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R026-AC001",
      "given": "the applicable business context, actor, and input for Nguyên tắc: - Scope thấp hơn ưu tiên kế thừa",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-POLICY-INDEX-R026-O001"
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
        "BRD-POLICY-INDEX-R026-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R026-O001",
      "obligation_text": "Nguyên tắc: - Scope thấp hơn ưu tiên kế thừa"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Scope thấp hơn ưu tiên kế thừa.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-POLICY-INDEX-010"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-026",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Policy Inheritance Matrix",
    "source_context_sha256": "937afbac2c05ef6280329dcccb2044708ad9b7fd11ed81b9def34213a1a0e00f",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "d26388f52e8ded44ba12e92f54a9f2e888d81ff1d6b6544f3b5163499c83fc17",
    "source_lines": "L685-L689",
    "source_section": "18. Policy Inheritance Matrix"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_RULE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R026",
  "title": "Nguyên tắc: - Scope thấp hơn ưu tiên kế thừa",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R027 — Nguyên tắc: - Chỉ Override khi thực sự cần thiết

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R027-AC001",
      "given": "the applicable business context, actor, and input for Nguyên tắc: - Chỉ Override khi thực sự cần thiết",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "an override is accepted only for a policy marked override-eligible, with an explicit reason and the required approval; otherwise the inherited or system policy remains effective",
      "verifies": [
        "BRD-POLICY-INDEX-R027-O001"
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
        "BRD-POLICY-INDEX-R027-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R027-O001",
      "obligation_text": "Nguyên tắc: - Chỉ Override khi thực sự cần thiết"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Chỉ Override khi thực sự cần thiết.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-POLICY-INDEX-010"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-027",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-027",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Policy Inheritance Matrix",
    "source_context_sha256": "937afbac2c05ef6280329dcccb2044708ad9b7fd11ed81b9def34213a1a0e00f",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "d26388f52e8ded44ba12e92f54a9f2e888d81ff1d6b6544f3b5163499c83fc17",
    "source_lines": "L685-L689",
    "source_section": "18. Policy Inheritance Matrix"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_RULE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R027",
  "title": "Nguyên tắc: - Chỉ Override khi thực sự cần thiết",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R028 — Nguyên tắc: - Không được Override các System Policy bắt buộc

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-POLICY-INDEX-R028-AC001",
      "given": "the applicable business context, actor, and input for Nguyên tắc: - Không được Override các System Policy bắt buộc",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-POLICY-INDEX-R028-O001"
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
        "BRD-POLICY-INDEX-R028-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R028-O001",
      "obligation_text": "Nguyên tắc: - Không được Override các System Policy bắt buộc"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Không được Override các System Policy bắt buộc.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-POLICY-INDEX-010"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-028",
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-028",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Policy Inheritance Matrix",
    "source_context_sha256": "937afbac2c05ef6280329dcccb2044708ad9b7fd11ed81b9def34213a1a0e00f",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "d26388f52e8ded44ba12e92f54a9f2e888d81ff1d6b6544f3b5163499c83fc17",
    "source_lines": "L685-L689",
    "source_section": "18. Policy Inheritance Matrix"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_RULE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R028",
  "title": "Nguyên tắc: - Không được Override các System Policy bắt buộc",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-EP-001 — Policy phản ánh quyết định nghiệp vụ

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-EP-001-AC001",
      "given": "the applicable business context, actor, and input for Policy phản ánh quyết định nghiệp vụ",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-EP-001-O001"
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
        "POL-EP-001-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-EP-001-O001",
      "obligation_text": "Policy phản ánh quyết định nghiệp vụ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy phản ánh quyết định nghiệp vụ.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-EP-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P08 — Business Driven",
    "source_context_sha256": "c4b192d53589bf500334080ecc376cdb79467abdc71e8486592c2e51fd1562c9",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "f9bd03cae0b89a174553144300be1691211a4e3fdd41893b3f469bdd71021600",
    "source_lines": "L843-L846",
    "source_section": "23. Enterprise Policy Principles > POL-EP-001"
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
  "stable_id": "POL-EP-001",
  "title": "Policy phản ánh quyết định nghiệp vụ",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-EP-002 — Policy độc lập với Source Code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-EP-002-AC001",
      "given": "the applicable business context, actor, and input for Policy độc lập với Source Code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "POL-EP-002-O001"
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
        "POL-EP-002-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-EP-002-O001",
      "obligation_text": "Policy độc lập với Source Code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy độc lập với Source Code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-EP-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-EP-002",
    "source_context_sha256": "d53176dad5d08ad69b3db0b1f459ec6a63b22beb9d13b07d3a6ab9b0f7d81d5e",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "1d32f0f927a05c52b922dc690bbe74e77ffc8349e01f0d1478af359894f70858",
    "source_lines": "L849-L852",
    "source_section": "23. Enterprise Policy Principles > POL-EP-002"
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
  "stable_id": "POL-EP-002",
  "title": "Policy độc lập với Source Code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-EP-003 — Policy độc lập với Database

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-EP-003-AC001",
      "given": "the applicable business context, actor, and input for Policy độc lập với Database",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "POL-EP-003-O001"
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
        "POL-EP-003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-EP-003-O001",
      "obligation_text": "Policy độc lập với Database"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy độc lập với Database.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-EP-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-EP-003",
    "source_context_sha256": "44db2b94220426e96c7df8e4793cf594be5f6f4d1169b5368726c68f1dc023bf",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "a4dde9f3da9905f58a34955f8e696d0f0badc333cc7a526fdf900a32bff54989",
    "source_lines": "L855-L858",
    "source_section": "23. Enterprise Policy Principles > POL-EP-003"
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
  "stable_id": "POL-EP-003",
  "title": "Policy độc lập với Database",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-EP-004 — Policy ưu tiên Configuration

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-EP-004-AC001",
      "given": "the applicable business context, actor, and input for Policy ưu tiên Configuration",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "POL-EP-004-O001"
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
        "POL-EP-004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-EP-004-O001",
      "obligation_text": "Policy ưu tiên Configuration"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy ưu tiên Configuration.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-EP-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-EP-004",
    "source_context_sha256": "2632b91e179ac8694d7911e2d46ed97657293ce6c96fc67800d3e6e77b2bb965",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "74b1fd99523a4ee5cffc0fbdbd94ee9455d35fd88394e185319cb1662e2e2d20",
    "source_lines": "L861-L864",
    "source_section": "23. Enterprise Policy Principles > POL-EP-004"
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
  "stable_id": "POL-EP-004",
  "title": "Policy ưu tiên Configuration",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-EP-005 — Policy hỗ trợ Runtime Reload

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-EP-005-AC001",
      "given": "the applicable business context, actor, and input for Policy hỗ trợ Runtime Reload",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-EP-005-O001"
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
        "POL-EP-005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-EP-005-O001",
      "obligation_text": "Policy hỗ trợ Runtime Reload"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy hỗ trợ Runtime Reload.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-EP-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-EP-005",
    "source_context_sha256": "1062baeed1c627f0138f115afd959fedc0e4cbff7daaf202c0c495e5c890ca46",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "7c4c79aac0853038c651e7e23fd134a60030a54eaafed318fa2c9276c95e0010",
    "source_lines": "L867-L870",
    "source_section": "23. Enterprise Policy Principles > POL-EP-005"
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
  "stable_id": "POL-EP-005",
  "title": "Policy hỗ trợ Runtime Reload",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-EP-006 — Policy hỗ trợ Versioning

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-EP-006-AC001",
      "given": "the applicable business context, actor, and input for Policy hỗ trợ Versioning",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-EP-006-O001"
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
        "POL-EP-006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-EP-006-O001",
      "obligation_text": "Policy hỗ trợ Versioning"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy hỗ trợ Versioning.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-EP-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-EP-006",
    "source_context_sha256": "a3f79cba61b0634ce1c7b079323a021331be6ab867f89eacaf55b8242ca77aaa",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "f1d5bde3ee99048504e4f0096c91aaf23dfe146532499a84e58371afc253576d",
    "source_lines": "L873-L876",
    "source_section": "23. Enterprise Policy Principles > POL-EP-006"
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
  "stable_id": "POL-EP-006",
  "title": "Policy hỗ trợ Versioning",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-EP-007 — Policy hỗ trợ Inheritance

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-EP-007-AC001",
      "given": "the applicable business context, actor, and input for Policy hỗ trợ Inheritance",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-EP-007-O001"
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
        "POL-EP-007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-EP-007-O001",
      "obligation_text": "Policy hỗ trợ Inheritance"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy hỗ trợ Inheritance.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-EP-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-EP-007",
    "source_context_sha256": "e14b45fedecf869dbe5d0905fd9d28f2e6eca0fe6a92730435ccbe1f7c6e3c2f",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "bde553a3424634809f14fcd99dfb52d190950cca280c1435c49663cd072a7228",
    "source_lines": "L879-L882",
    "source_section": "23. Enterprise Policy Principles > POL-EP-007"
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
  "stable_id": "POL-EP-007",
  "title": "Policy hỗ trợ Inheritance",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-EP-008 — Policy hỗ trợ Approval và Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-EP-008-AC001",
      "given": "an operational task within the scope of Policy hỗ trợ Approval và Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "POL-EP-008-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "POL-EP-008-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Policy hỗ trợ Approval và Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "POL-EP-008-O001"
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
        "POL-EP-008-AC001",
        "POL-EP-008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-EP-008-O001",
      "obligation_text": "Policy hỗ trợ Approval và Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "POL-EP-008 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "POL-EP-008 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "POL-EP-008 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "POL-EP-008 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "POL-EP-008-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "POL-EP-008 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy hỗ trợ Approval và Audit.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-EP-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-EP-008",
    "source_context_sha256": "53ff6a4b1816b1b39993ac88433698574868663b97111405e1394dcc00cf7960",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "25a9d6be419182395199bf0e0e91543a1a73b45f87bf1134cbc201e8a3e68926",
    "source_lines": "L885-L888",
    "source_section": "23. Enterprise Policy Principles > POL-EP-008"
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
  "stable_id": "POL-EP-008",
  "title": "Policy hỗ trợ Approval và Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-EP-009 — Policy được Policy Decision Engine đánh giá trước khi Capability được thực thi

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-EP-009-AC001",
      "given": "the applicable business context, actor, and input for Policy được Policy Decision Engine đánh giá trước khi Capability được thực thi",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-EP-009-O001"
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
        "POL-EP-009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-EP-009-O001",
      "obligation_text": "Policy được Policy Decision Engine đánh giá trước khi Capability được thực thi"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy được Policy Decision Engine đánh giá trước khi Capability được thực thi.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-EP-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-EP-009",
    "source_context_sha256": "c8bc2404ace6bb02391bb1089693d2af07c62b6dc0ee0092ffb89af1885cb015",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "9db9f1e9c4a86fa2acbfa135f9cfeeac79b75df83dab32879bd10c5ecdf31014",
    "source_lines": "L891-L894",
    "source_section": "23. Enterprise Policy Principles > POL-EP-009"
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
  "stable_id": "POL-EP-009",
  "title": "Policy được Policy Decision Engine đánh giá trước khi Capability được thực thi",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-EP-010 — Enterprise Policy Registry là Enterprise Policy Dictionary của nền tảng YSim

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-EP-010-AC001",
      "given": "the applicable business context, actor, and input for Enterprise Policy Registry là Enterprise Policy Dictionary của nền tảng YSim",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-EP-010-O001"
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
        "POL-EP-010-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-EP-010-O001",
      "obligation_text": "Enterprise Policy Registry là Enterprise Policy Dictionary của nền tảng YSim"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Enterprise Policy Registry là Enterprise Policy Dictionary của nền tảng YSim.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-EP-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-EP-010",
    "source_context_sha256": "8e8afdee32197b54daf3607fff91badfea6cf2566ccc87305f9f939377a2448e",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "0a9d437ffe0082a8a67bfafa3ad17ecb1c1b45299263edc875bf7bd1ad202020",
    "source_lines": "L897-L900",
    "source_section": "23. Enterprise Policy Principles > POL-EP-010"
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
  "stable_id": "POL-EP-010",
  "title": "Enterprise Policy Registry là Enterprise Policy Dictionary của nền tảng YSim",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-P01 — Policy ưu tiên được cấu hình. Không Hard-code khi có thể cấu hình

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P01-AC001",
      "given": "the applicable business context, actor, and input for Policy ưu tiên được cấu hình. Không Hard-code khi có thể cấu hình",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "POL-P01-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P01-AC002",
      "given": "the applicable business context, actor, and input for Policy ưu tiên được cấu hình. Không Hard-code khi có thể cấu hình",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "POL-P01-O002"
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
        "POL-P01-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P01-O001",
      "obligation_text": "Policy ưu tiên được cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "POL-P01-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P01-O002",
      "obligation_text": "Không Hard-code khi có thể cấu hình"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy ưu tiên được cấu hình. Không Hard-code khi có thể cấu hình.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-P01",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P01 — Configuration First",
    "source_context_sha256": "88ca6b21fdfb83a64388f6da22f53260941392cc5d71eccb6a9fc7f26280ebda",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "00acb5404bfafac5368bacebaaae3fee645a332a22f20f79c0cb50d6ae044bf5",
    "source_lines": "L325-L330",
    "source_section": "13. Policy Principles > POL-P01 — Configuration First"
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
  "stable_id": "POL-P01",
  "title": "Policy ưu tiên được cấu hình. Không Hard-code khi có thể cấu hình",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-P02 — Policy ưu tiên kế thừa. Chỉ Override khi thực sự cần thiết

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P02-AC001",
      "given": "the applicable business context, actor, and input for Policy ưu tiên kế thừa. Chỉ Override khi thực sự cần thiết",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-P02-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P02-AC002",
      "given": "the applicable business context, actor, and input for Policy ưu tiên kế thừa. Chỉ Override khi thực sự cần thiết",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "an override is accepted only for a policy marked override-eligible, with an explicit reason and the required approval; otherwise the inherited or system policy remains effective",
      "verifies": [
        "POL-P02-O002"
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
        "POL-P02-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P02-O001",
      "obligation_text": "Policy ưu tiên kế thừa"
    },
    {
      "acceptance_criterion_references": [
        "POL-P02-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P02-O002",
      "obligation_text": "Chỉ Override khi thực sự cần thiết"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy ưu tiên kế thừa. Chỉ Override khi thực sự cần thiết.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-P02",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P02 — Inheritance",
    "source_context_sha256": "db0a39465cb4a29f84d4d2eef0ac503b63f279bb1a8f119c7b6b28db311dd770",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "e33f4ad7c611d2261c6b560e19a8593f5dfeb5210c967798e838512fb646fa52",
    "source_lines": "L333-L338",
    "source_section": "13. Policy Principles > POL-P02 — Inheritance"
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
  "stable_id": "POL-P02",
  "title": "Policy ưu tiên kế thừa. Chỉ Override khi thực sự cần thiết",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-P03 — Policy luôn hỗ trợ Version

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P03-AC001",
      "given": "the applicable business context, actor, and input for Policy luôn hỗ trợ Version",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-P03-O001"
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
        "POL-P03-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P03-O001",
      "obligation_text": "Policy luôn hỗ trợ Version"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy luôn hỗ trợ Version.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-P03",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P03 — Versioned",
    "source_context_sha256": "fde6fbc0a32454feb502d4050241a435b7f9f29752e56b43b4bb1bbec8df3bbd",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "fb20023400335c322821ac1b1cc47d00842785c90bcef25b1874294b36b2bb6f",
    "source_lines": "L341-L344",
    "source_section": "13. Policy Principles > POL-P03 — Versioned"
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
  "stable_id": "POL-P03",
  "title": "Policy luôn hỗ trợ Version",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-P04 — Policy hỗ trợ Effective Date

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P04-AC001",
      "given": "the applicable business context, actor, and input for Policy hỗ trợ Effective Date",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-P04-O001"
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
        "POL-P04-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P04-O001",
      "obligation_text": "Policy hỗ trợ Effective Date"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy hỗ trợ Effective Date.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-P04",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P04 — Effective Date",
    "source_context_sha256": "91cd6f94d3b2f6029096802ce64a3dccb04edecaa6f09c738f05e032adcb7c7a",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "8de63a8a2e8184743fde5b682c340d66136a38bfba173e7d1b81335c98b54609",
    "source_lines": "L347-L350",
    "source_section": "13. Policy Principles > POL-P04 — Effective Date"
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
  "stable_id": "POL-P04",
  "title": "Policy hỗ trợ Effective Date",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-P05 — Policy chỉ có hiệu lực sau Approval

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P05-AC001",
      "given": "the applicable business context, actor, and input for Policy chỉ có hiệu lực sau Approval",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "POL-P05-O001"
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
        "POL-P05-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P05-O001",
      "obligation_text": "Policy chỉ có hiệu lực sau Approval"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy chỉ có hiệu lực sau Approval.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-P05",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P05 — Approval Required",
    "source_context_sha256": "3855924285656847d9cd8da63e84358b81e40e26be24286612a10dc957b44528",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "d128edfee753299bd3a4681145406c4ccd4939c65bbc152006b736d3d686fad0",
    "source_lines": "L353-L356",
    "source_section": "13. Policy Principles > POL-P05 — Approval Required"
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
  "stable_id": "POL-P05",
  "title": "Policy chỉ có hiệu lực sau Approval",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-P06 — Mọi thay đổi Policy phải được Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P06-AC001",
      "given": "an operational task within the scope of Mọi thay đổi Policy phải được Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "POL-P06-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "POL-P06-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Mọi thay đổi Policy phải được Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "POL-P06-O001"
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
        "POL-P06-AC001",
        "POL-P06-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P06-O001",
      "obligation_text": "Mọi thay đổi Policy phải được Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "POL-P06 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "POL-P06 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "POL-P06 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "POL-P06 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "POL-P06-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "POL-P06 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thay đổi Policy phải được Audit.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-P06",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P06 — Auditable",
    "source_context_sha256": "371b7e73f5fba02dc9551045738108a0dbfb492b538b33c9e049e9201dcaa86e",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "623be2af9f8eda0bf4a1cda12e8300b2cc3ca1c0aa5600a1b9ccc22d3754141c",
    "source_lines": "L359-L362",
    "source_section": "13. Policy Principles > POL-P06 — Auditable"
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
  "stable_id": "POL-P06",
  "title": "Mọi thay đổi Policy phải được Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-P07 — Policy được Runtime Engine sử dụng trực tiếp

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P07-AC001",
      "given": "the applicable business context, actor, and input for Policy được Runtime Engine sử dụng trực tiếp",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-P07-O001"
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
        "POL-P07-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P07-O001",
      "obligation_text": "Policy được Runtime Engine sử dụng trực tiếp"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy được Runtime Engine sử dụng trực tiếp.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-P07",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P07 — Runtime Ready",
    "source_context_sha256": "76315587359072fa6af2beb29722671fda7fcd99c088ca67ec19a7bb66cfe287",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "2c5e33395c50b7b9f2d9634e79ffa85451874e571e768e9f889349ee777135f5",
    "source_lines": "L365-L368",
    "source_section": "13. Policy Principles > POL-P07 — Runtime Ready"
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
  "stable_id": "POL-P07",
  "title": "Policy được Runtime Engine sử dụng trực tiếp",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-P08 — Policy phản ánh quyết định nghiệp vụ. Không phản ánh thiết kế kỹ thuật

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P08-AC001",
      "given": "the applicable business context, actor, and input for Policy phản ánh quyết định nghiệp vụ. Không phản ánh thiết kế kỹ thuật",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-P08-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P08-AC002",
      "given": "the applicable business context, actor, and input for Policy phản ánh quyết định nghiệp vụ. Không phản ánh thiết kế kỹ thuật",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-P08-O002"
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
        "POL-P08-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P08-O001",
      "obligation_text": "Policy phản ánh quyết định nghiệp vụ"
    },
    {
      "acceptance_criterion_references": [
        "POL-P08-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P08-O002",
      "obligation_text": "Không phản ánh thiết kế kỹ thuật"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy phản ánh quyết định nghiệp vụ. Không phản ánh thiết kế kỹ thuật.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-P08",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P08 — Business Driven",
    "source_context_sha256": "c4b192d53589bf500334080ecc376cdb79467abdc71e8486592c2e51fd1562c9",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "8a212d9eaba03540e47fa3fb5162a7d9bf6a323ed1ae7391aa8ea452759e6729",
    "source_lines": "L371-L376",
    "source_section": "13. Policy Principles > POL-P08 — Business Driven"
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
  "stable_id": "POL-P08",
  "title": "Policy phản ánh quyết định nghiệp vụ. Không phản ánh thiết kế kỹ thuật",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-P09 — Policy phải có cơ chế xử lý xung đột giữa các Scope

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P09-AC001",
      "given": "the applicable business context, actor, and input for Policy phải có cơ chế xử lý xung đột giữa các Scope",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "POL-P09-O001"
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
        "POL-P09-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P09-O001",
      "obligation_text": "Policy phải có cơ chế xử lý xung đột giữa các Scope"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy phải có cơ chế xử lý xung đột giữa các Scope.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-P09",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P09 — Conflict Managed",
    "source_context_sha256": "511ca4d8d9f7a069347a14a36e91733f24076d23d7bb9ba542695944b26c7087",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "b7f4c7aa514fc3cc2100a036eb944e1cad9fc84870b079f651410cfd784f0ceb",
    "source_lines": "L379-L382",
    "source_section": "13. Policy Principles > POL-P09 — Conflict Managed"
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
  "stable_id": "POL-P09",
  "title": "Policy phải có cơ chế xử lý xung đột giữa các Scope",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-P10 — Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P10-AC001",
      "given": "an operational task within the scope of Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "POL-P10-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P10-AC002",
      "given": "an operational task within the scope of Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "POL-P10-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P10-AC003",
      "given": "an operational task within the scope of Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "POL-P10-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P10-AC004",
      "given": "an operational task within the scope of Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "POL-P10-O004"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "POL-P10-AC005",
      "given": "an operational task within the scope of Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "POL-P10-O005"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "POL-P10-AC006",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "POL-P10-O001",
        "POL-P10-O002",
        "POL-P10-O003",
        "POL-P10-O004",
        "POL-P10-O005"
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
        "POL-P10-AC001",
        "POL-P10-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P10-O001",
      "obligation_text": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: Architecture Review."
    },
    {
      "acceptance_criterion_references": [
        "POL-P10-AC002",
        "POL-P10-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P10-O002",
      "obligation_text": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: Approval."
    },
    {
      "acceptance_criterion_references": [
        "POL-P10-AC003",
        "POL-P10-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P10-O003",
      "obligation_text": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: Versioning."
    },
    {
      "acceptance_criterion_references": [
        "POL-P10-AC004",
        "POL-P10-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P10-O004",
      "obligation_text": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: Audit."
    },
    {
      "acceptance_criterion_references": [
        "POL-P10-AC005",
        "POL-P10-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P10-O005",
      "obligation_text": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: Traceability."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "POL-P10 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "POL-P10 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "POL-P10 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "POL-P10 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "POL-P10-AC001",
        "POL-P10-AC002",
        "POL-P10-AC003",
        "POL-P10-AC004",
        "POL-P10-AC005"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "POL-P10 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: - Architecture Review - Approval - Versioning - Audit - Traceability",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-P10",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P10 — Enterprise Governance",
    "source_context_sha256": "d75e2a532d3025daa8bda2543b0d948ad6e54482c4e0aafd3337a14bc5f21837",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "90e5c7232a187a2d7bb5f34e22879f9d463f1703fa3ce361c3aba2742a2a79fc",
    "source_lines": "L385-L396",
    "source_section": "13. Policy Principles > POL-P10 — Enterprise Governance"
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
  "stable_id": "POL-P10",
  "title": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
