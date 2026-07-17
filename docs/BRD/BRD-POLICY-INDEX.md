---
document_code: "BRD-POLICY-INDEX"
document_id: "BRD-POLICY-INDEX"
title: "Enterprise Policy Registry"
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

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R001 — Không phải mọi Policy đều hỗ trợ toàn bộ Scope

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
      "requirement_id": "BRD-POLICY-INDEX-R001",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "20fbc6e5aa1d3d54c9f4b86b18f871b9369b62c15224ddbee482fc3aadb15a06"
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
        "BRD-POLICY-INDEX-R001-AC001",
        "BRD-POLICY-INDEX-R001-AC002",
        "BRD-POLICY-INDEX-R001-AC003"
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
    "source_lines": "L956-L1031",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R002",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "822b8721ae0f51071ef8787dec66d5d19575a0575f04c973e534f2d08be9d366"
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
        "BRD-POLICY-INDEX-R002-AC001",
        "BRD-POLICY-INDEX-R002-AC002",
        "BRD-POLICY-INDEX-R002-AC003"
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
    "source_lines": "L1033-L1108",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R003",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "b441e2c779cbb94f42ae8f77ec9baca70cfcedb1de3a4da5a1d1e3897956fd89"
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
        "BRD-POLICY-INDEX-R003-AC001",
        "BRD-POLICY-INDEX-R003-AC002",
        "BRD-POLICY-INDEX-R003-AC003"
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
    "source_lines": "L1110-L1185",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R003"
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
### BRD-POLICY-INDEX-R004 — Policy scheduling phải hỗ trợ Publish, Activate và Expire mà không cần redeploy hệ thống

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
      "requirement_id": "BRD-POLICY-INDEX-R004",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "dc17db171aa295e702170f70a51183acdc70a06126d3708c408e1101dbf136c1"
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
        "BRD-POLICY-INDEX-R004-AC001",
        "BRD-POLICY-INDEX-R004-AC002",
        "BRD-POLICY-INDEX-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R004-O001",
      "obligation_text": "Policy scheduling phải hỗ trợ Publish, Activate và Expire mà không cần redeploy hệ thống"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Policy scheduling phải hỗ trợ Publish, Activate và Expire mà không cần redeploy hệ thống.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-POLICY-INDEX.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "10. Effective Date"
    },
    "deterministic_transformation": "EXPAND_PRECEDING_SUBJECT_AND_ACTION_LIST",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-POLICY-INDEX-004",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-POLICY-INDEX-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Effective Date",
    "source_context_sha256": "6365a8620005c6299a4561ebed94dda0a3c8e23acd21758b5de0d3baa3b8ccbc",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "dc17db171aa295e702170f70a51183acdc70a06126d3708c408e1101dbf136c1",
    "source_fingerprint_before_c3": "4609a19224cb80841f6599cab41d3dfb2ac6b90e2c03e94447c1b8b33b561dde",
    "source_lines": "L1187-L1283",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-POLICY-INDEX.md",
      "lines": "L287",
      "section": "10. Effective Date"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R004"
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
  "title": "Policy scheduling phải hỗ trợ Publish, Activate và Expire mà không cần redeploy hệ thống",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R005 — Policy chỉ được Publish sau khi hoàn thành Approval Workflow

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R005",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "d3c9452fbd136e0230216bf30d1badd85fad942a30a090d6e95271a9148cce45"
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
        "BRD-POLICY-INDEX-R005-AC001",
        "BRD-POLICY-INDEX-R005-AC002",
        "BRD-POLICY-INDEX-R005-AC003"
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
    "source_lines": "L1285-L1366",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R006",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "24eea879eab7054106efed23811b322e969835db273c520293c142e5c8ad740f"
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
        "BRD-POLICY-INDEX-R006-AC001",
        "BRD-POLICY-INDEX-R006-AC002",
        "BRD-POLICY-INDEX-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R006-O001",
      "obligation_text": "Mọi Approval phải được ghi Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R006 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R006-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R006-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R006 does not define a recovery obligation."
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
    "source_lines": "L1368-L1482",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R007",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "75e338810613993a3ab72d169fb64b54e8989e68da6baeb9d0c8fd48f9cf3423"
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
        "BRD-POLICY-INDEX-R007-AC001",
        "BRD-POLICY-INDEX-R007-AC002",
        "BRD-POLICY-INDEX-R007-AC003"
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
    "source_lines": "L1484-L1559",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R008",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "f294b84c836ee5f6c680b85e80309b8b46127bc62a57634d85429fa2b5e00cef"
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
        "BRD-POLICY-INDEX-R008-AC001",
        "BRD-POLICY-INDEX-R008-AC002",
        "BRD-POLICY-INDEX-R008-AC003"
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
    "source_lines": "L1561-L1636",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R009",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "d2beba6ede61fe451033d2c5d26126da3d62a33fc73586af646a7a21f689191e"
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
        "BRD-POLICY-INDEX-R009-AC001",
        "BRD-POLICY-INDEX-R009-AC002",
        "BRD-POLICY-INDEX-R009-AC003"
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
    "source_lines": "L1638-L1713",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R020",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "a8b2ba49d182690ff6c798be2649743521183443ef88afb1316496b4c3b862ba"
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
        "BRD-POLICY-INDEX-R020-AC001",
        "BRD-POLICY-INDEX-R020-AC002",
        "BRD-POLICY-INDEX-R020-AC003"
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
    "source_lines": "L1715-L1790",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R020"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R021",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "3bcb4ef5c9ca3d206835b9c0671152b849ce85e1160f6b1f24d9018b83731055"
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
        "BRD-POLICY-INDEX-R021-AC001",
        "BRD-POLICY-INDEX-R021-AC002",
        "BRD-POLICY-INDEX-R021-AC003"
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
    "source_fingerprint": "3bcb4ef5c9ca3d206835b9c0671152b849ce85e1160f6b1f24d9018b83731055",
    "source_lines": "L1792-L1873",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R021"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R022",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "19f866b7c72f124d22f260f53eb57c68a249858082947f12c1268b4bf2d92d93"
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
        "BRD-POLICY-INDEX-R022-AC001",
        "BRD-POLICY-INDEX-R022-AC002",
        "BRD-POLICY-INDEX-R022-AC003"
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
    "source_fingerprint": "19f866b7c72f124d22f260f53eb57c68a249858082947f12c1268b4bf2d92d93",
    "source_lines": "L1875-L1950",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R022"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R023",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "323d85cf99b6e6a826a26b99c7d5bf2c7042029c9a05103c7c3d62264b3bc83f"
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
        "BRD-POLICY-INDEX-R023-AC001",
        "BRD-POLICY-INDEX-R023-AC002",
        "BRD-POLICY-INDEX-R023-AC003"
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
    "source_fingerprint": "323d85cf99b6e6a826a26b99c7d5bf2c7042029c9a05103c7c3d62264b3bc83f",
    "source_lines": "L1952-L2027",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R023"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R024",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "96837d423b1aeba248e9f2c3ff2c845abacac42d0de4959bed2dd09ec3819be2"
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
        "BRD-POLICY-INDEX-R024-AC001",
        "BRD-POLICY-INDEX-R024-AC002",
        "BRD-POLICY-INDEX-R024-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R024-O001",
      "obligation_text": "Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R024 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R024 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R024 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R024-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R024-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R024 does not define a recovery obligation."
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
    "source_fingerprint": "96837d423b1aeba248e9f2c3ff2c845abacac42d0de4959bed2dd09ec3819be2",
    "source_lines": "L2029-L2137",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R024"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R025",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "c62f757e5a730206213f18a45e289e26d990ec41297621a31f6c1dcebcfd83ca"
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
        "BRD-POLICY-INDEX-R025-AC001",
        "BRD-POLICY-INDEX-R025-AC002",
        "BRD-POLICY-INDEX-R025-AC003"
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
    "source_fingerprint": "c62f757e5a730206213f18a45e289e26d990ec41297621a31f6c1dcebcfd83ca",
    "source_lines": "L2139-L2214",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R025"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R026",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "04e25c56333d50b5d443ea3b0fc7478933bee2569fe2b02ad60e43f86742a289"
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
        "BRD-POLICY-INDEX-R026-AC001",
        "BRD-POLICY-INDEX-R026-AC002",
        "BRD-POLICY-INDEX-R026-AC003"
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
    "source_fingerprint": "04e25c56333d50b5d443ea3b0fc7478933bee2569fe2b02ad60e43f86742a289",
    "source_lines": "L2216-L2294",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R026"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R027",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "3c3bb7bcfa9748efd6111f280a9f8f6b2db4d48b4b1d606434e3058894ea3c88"
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
        "BRD-POLICY-INDEX-R027-AC001",
        "BRD-POLICY-INDEX-R027-AC002",
        "BRD-POLICY-INDEX-R027-AC003"
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
    "source_fingerprint": "3c3bb7bcfa9748efd6111f280a9f8f6b2db4d48b4b1d606434e3058894ea3c88",
    "source_lines": "L2296-L2374",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R027"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R028",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "e2222992ae22e28ddbc62e1b9d1ad12dc841480bc00fa5cdf3fc777e1a617220"
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
        "BRD-POLICY-INDEX-R028-AC001",
        "BRD-POLICY-INDEX-R028-AC002",
        "BRD-POLICY-INDEX-R028-AC003"
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
    "source_fingerprint": "e2222992ae22e28ddbc62e1b9d1ad12dc841480bc00fa5cdf3fc777e1a617220",
    "source_lines": "L2376-L2454",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R028"
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
### BRD-POLICY-INDEX-R029 — Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R029",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "e162eb3c362cfff60291516cafa2490178832f74713b9b4b47d9befe96325c53"
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
        "BRD-POLICY-INDEX-R029-AC001",
        "BRD-POLICY-INDEX-R029-AC003",
        "BRD-POLICY-INDEX-R029-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R029-O001",
      "obligation_text": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance"
    },
    {
      "acceptance_criterion_references": [
        "BRD-POLICY-INDEX-R029-AC002",
        "BRD-POLICY-INDEX-R029-AC003",
        "BRD-POLICY-INDEX-R029-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R029-O002",
      "obligation_text": "Mọi Policy mới phải trải qua: Architecture Review"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R029 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R029 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R029 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R029-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R029-AC001",
        "BRD-POLICY-INDEX-R029-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R029 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: Architecture Review.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "BDD-27",
      "SD-03",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "POL-P10",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-POLICY-INDEX-R029",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P10 — Enterprise Governance",
    "source_context_sha256": "d75e2a532d3025daa8bda2543b0d948ad6e54482c4e0aafd3337a14bc5f21837",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "e162eb3c362cfff60291516cafa2490178832f74713b9b4b47d9befe96325c53",
    "source_fingerprint_before_c3": "e162eb3c362cfff60291516cafa2490178832f74713b9b4b47d9befe96325c53",
    "source_lines": "L2456-L2596",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R029"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "POL-P10"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "POL-P10"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R029",
  "title": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R030 — Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R030",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "f0f6eb3a98b9d558c01756ed3df0d8d06dc74f655369837d01ecb07d7312a3da"
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
        "BRD-POLICY-INDEX-R030-AC001",
        "BRD-POLICY-INDEX-R030-AC003",
        "BRD-POLICY-INDEX-R030-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R030-O001",
      "obligation_text": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance"
    },
    {
      "acceptance_criterion_references": [
        "BRD-POLICY-INDEX-R030-AC002",
        "BRD-POLICY-INDEX-R030-AC003",
        "BRD-POLICY-INDEX-R030-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R030-O002",
      "obligation_text": "Mọi Policy mới phải trải qua: Approval"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R030 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R030 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R030 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R030-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R030-AC001",
        "BRD-POLICY-INDEX-R030-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R030 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: Approval.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "BDD-27",
      "SD-03",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "POL-P10",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-POLICY-INDEX-R030",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P10 — Enterprise Governance",
    "source_context_sha256": "d75e2a532d3025daa8bda2543b0d948ad6e54482c4e0aafd3337a14bc5f21837",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "f0f6eb3a98b9d558c01756ed3df0d8d06dc74f655369837d01ecb07d7312a3da",
    "source_fingerprint_before_c3": "f0f6eb3a98b9d558c01756ed3df0d8d06dc74f655369837d01ecb07d7312a3da",
    "source_lines": "L2598-L2738",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R030"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "POL-P10"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "POL-P10"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R030",
  "title": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R031 — Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R031",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "7c2746b758753b6e090a2c0b7a35625273680cbbbfa8f9edd0ff1a9c8aa170db"
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
        "BRD-POLICY-INDEX-R031-AC001",
        "BRD-POLICY-INDEX-R031-AC003",
        "BRD-POLICY-INDEX-R031-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R031-O001",
      "obligation_text": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance"
    },
    {
      "acceptance_criterion_references": [
        "BRD-POLICY-INDEX-R031-AC002",
        "BRD-POLICY-INDEX-R031-AC003",
        "BRD-POLICY-INDEX-R031-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R031-O002",
      "obligation_text": "Mọi Policy mới phải trải qua: Versioning"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R031 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R031 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R031 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R031-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R031-AC001",
        "BRD-POLICY-INDEX-R031-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R031 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: Versioning.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "BDD-27",
      "SD-03",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "POL-P10",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-POLICY-INDEX-R031",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P10 — Enterprise Governance",
    "source_context_sha256": "d75e2a532d3025daa8bda2543b0d948ad6e54482c4e0aafd3337a14bc5f21837",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "7c2746b758753b6e090a2c0b7a35625273680cbbbfa8f9edd0ff1a9c8aa170db",
    "source_fingerprint_before_c3": "7c2746b758753b6e090a2c0b7a35625273680cbbbfa8f9edd0ff1a9c8aa170db",
    "source_lines": "L2740-L2880",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R031"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "POL-P10"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "POL-P10"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R031",
  "title": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R032 — Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R032",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "76b33876a98d8a7a419c3dff5087471f0e1cc35fa0018d5593f9a9a69379ae04"
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
        "BRD-POLICY-INDEX-R032-AC001",
        "BRD-POLICY-INDEX-R032-AC003",
        "BRD-POLICY-INDEX-R032-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R032-O001",
      "obligation_text": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance"
    },
    {
      "acceptance_criterion_references": [
        "BRD-POLICY-INDEX-R032-AC002",
        "BRD-POLICY-INDEX-R032-AC003",
        "BRD-POLICY-INDEX-R032-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R032-O002",
      "obligation_text": "Mọi Policy mới phải trải qua: Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R032 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R032 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R032 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R032-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R032-AC001",
        "BRD-POLICY-INDEX-R032-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R032 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: Audit.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "BDD-27",
      "SD-03",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "POL-P10",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-POLICY-INDEX-R032",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P10 — Enterprise Governance",
    "source_context_sha256": "d75e2a532d3025daa8bda2543b0d948ad6e54482c4e0aafd3337a14bc5f21837",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "76b33876a98d8a7a419c3dff5087471f0e1cc35fa0018d5593f9a9a69379ae04",
    "source_fingerprint_before_c3": "76b33876a98d8a7a419c3dff5087471f0e1cc35fa0018d5593f9a9a69379ae04",
    "source_lines": "L2882-L3022",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R032"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "POL-P10"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "POL-P10"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R032",
  "title": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-POLICY-INDEX-R033 — Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-POLICY-INDEX-R033",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "6eb9c70f70de73399e894f0559ae12ec62a1fce9a0147c35278af97bf17f8e2a"
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
        "BRD-POLICY-INDEX-R033-AC001",
        "BRD-POLICY-INDEX-R033-AC003",
        "BRD-POLICY-INDEX-R033-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R033-O001",
      "obligation_text": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance"
    },
    {
      "acceptance_criterion_references": [
        "BRD-POLICY-INDEX-R033-AC002",
        "BRD-POLICY-INDEX-R033-AC003",
        "BRD-POLICY-INDEX-R033-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-POLICY-INDEX-R033-O002",
      "obligation_text": "Mọi Policy mới phải trải qua: Traceability"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R033 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R033 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R033 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R033-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-POLICY-INDEX-R033-AC001",
        "BRD-POLICY-INDEX-R033-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-POLICY-INDEX-R033 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: Traceability.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "BDD-27",
      "SD-03",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "POL-P10",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-POLICY-INDEX-R033",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P10 — Enterprise Governance",
    "source_context_sha256": "d75e2a532d3025daa8bda2543b0d948ad6e54482c4e0aafd3337a14bc5f21837",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "6eb9c70f70de73399e894f0559ae12ec62a1fce9a0147c35278af97bf17f8e2a",
    "source_fingerprint_before_c3": "6eb9c70f70de73399e894f0559ae12ec62a1fce9a0147c35278af97bf17f8e2a",
    "source_lines": "L3024-L3164",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-POLICY-INDEX-R033"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "POL-P10"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "POL-P10"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-POLICY-INDEX-R033",
  "title": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### POL-EP-001 — Policy phản ánh quyết định nghiệp vụ

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
      "requirement_id": "POL-EP-001",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "558c0dcc269b3f98562ec892324abdc6b4c45e8c3afd55e07cb744e08da960ef"
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
        "POL-EP-001-AC001",
        "POL-EP-001-AC002",
        "POL-EP-001-AC003"
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
    "source_fingerprint": "558c0dcc269b3f98562ec892324abdc6b4c45e8c3afd55e07cb744e08da960ef",
    "source_lines": "L3166-L3241",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-EP-001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-EP-002",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "a28fb022cd529a9dfb6b0b3ac9248cbecb4a8e7dad55c28a432a2547a04ee400"
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
        "POL-EP-002-AC001",
        "POL-EP-002-AC002",
        "POL-EP-002-AC003"
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
    "source_fingerprint": "a28fb022cd529a9dfb6b0b3ac9248cbecb4a8e7dad55c28a432a2547a04ee400",
    "source_lines": "L3243-L3318",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-EP-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-EP-003",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "49dcfb18de7c010f8695abbfbe92b3fba934e72180605dca032b351cc006e31a"
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
        "POL-EP-003-AC001",
        "POL-EP-003-AC002",
        "POL-EP-003-AC003"
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
    "source_fingerprint": "49dcfb18de7c010f8695abbfbe92b3fba934e72180605dca032b351cc006e31a",
    "source_lines": "L3320-L3395",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-EP-003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-EP-004",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "cbf42bbf0d0026492e7352f6d6aec0c3007ddd08f94959e82a81f10a944b2bbd"
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
        "POL-EP-004-AC001",
        "POL-EP-004-AC002",
        "POL-EP-004-AC003"
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
    "source_fingerprint": "cbf42bbf0d0026492e7352f6d6aec0c3007ddd08f94959e82a81f10a944b2bbd",
    "source_lines": "L3397-L3472",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-EP-004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-EP-005",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "12fa93c66a9f6799f4157bd2e192e6849a56b00461df5420daac1823c454a3e5"
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
        "POL-EP-005-AC001",
        "POL-EP-005-AC002",
        "POL-EP-005-AC003"
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
    "source_fingerprint": "12fa93c66a9f6799f4157bd2e192e6849a56b00461df5420daac1823c454a3e5",
    "source_lines": "L3474-L3549",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-EP-005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-EP-006",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "2d4cce3178c92ff2adb452c26b89a9b7278a32ad4288c855271d87805df23ee4"
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
        "POL-EP-006-AC001",
        "POL-EP-006-AC002",
        "POL-EP-006-AC003"
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
    "source_fingerprint": "2d4cce3178c92ff2adb452c26b89a9b7278a32ad4288c855271d87805df23ee4",
    "source_lines": "L3551-L3626",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-EP-006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-EP-007",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "236ef00bf1c5ba3361194ccbafa88fff363c03b417a60903adb352f37f9f2af6"
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
        "POL-EP-007-AC001",
        "POL-EP-007-AC002",
        "POL-EP-007-AC003"
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
    "source_fingerprint": "236ef00bf1c5ba3361194ccbafa88fff363c03b417a60903adb352f37f9f2af6",
    "source_lines": "L3628-L3703",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-EP-007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-EP-008",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "9265640d117e5f32c9696ba89867d9ebbdf3fdf6cf83ddd746c15f8242d5327a"
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
        "POL-EP-008-AC001",
        "POL-EP-008-AC002",
        "POL-EP-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-EP-008-O001",
      "obligation_text": "Policy hỗ trợ Approval và Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "POL-EP-008 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "POL-EP-008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "POL-EP-008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "POL-EP-008-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "POL-EP-008-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "POL-EP-008 does not define a recovery obligation."
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
    "source_fingerprint": "9265640d117e5f32c9696ba89867d9ebbdf3fdf6cf83ddd746c15f8242d5327a",
    "source_lines": "L3705-L3819",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-EP-008"
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
      "requirement_id": "POL-EP-009",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "63430466cfe2d07e1119b2088bbeceb152e46b78434ac28e506c9c48362bafef"
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
        "POL-EP-009-AC001",
        "POL-EP-009-AC002",
        "POL-EP-009-AC003"
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
    "source_fingerprint": "63430466cfe2d07e1119b2088bbeceb152e46b78434ac28e506c9c48362bafef",
    "source_lines": "L3821-L3900",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-EP-009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-EP-010",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "44a50558e567b2bcfe563706a8de108e4529eb84424b018842d7687221cfc6af"
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
        "POL-EP-010-AC001",
        "POL-EP-010-AC002",
        "POL-EP-010-AC003"
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
    "source_fingerprint": "44a50558e567b2bcfe563706a8de108e4529eb84424b018842d7687221cfc6af",
    "source_lines": "L3902-L3977",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-EP-010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-P01",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "e6489f38b215baf5bca86ec34f1035750b4d0b254c1dc4cbbed2175888962cd9"
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
        "POL-P01-AC001",
        "POL-P01-AC003",
        "POL-P01-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P01-O001",
      "obligation_text": "Policy ưu tiên được cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "POL-P01-AC002",
        "POL-P01-AC003",
        "POL-P01-AC004"
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
    "source_fingerprint": "e6489f38b215baf5bca86ec34f1035750b4d0b254c1dc4cbbed2175888962cd9",
    "source_lines": "L3979-L4064",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-P01"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-P02",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "4620eef7d213552c656fd24705238efc8904397d389c2ed44581be4e2645a7b9"
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
        "POL-P02-AC001",
        "POL-P02-AC003",
        "POL-P02-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P02-O001",
      "obligation_text": "Policy ưu tiên kế thừa"
    },
    {
      "acceptance_criterion_references": [
        "POL-P02-AC002",
        "POL-P02-AC003",
        "POL-P02-AC004"
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
    "source_fingerprint": "4620eef7d213552c656fd24705238efc8904397d389c2ed44581be4e2645a7b9",
    "source_lines": "L4066-L4151",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-P02"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-P03",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "6de2072a36839706d017f9d2b88a25c7ac7259517fb26a7b87e89ea1aa0115c2"
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
        "POL-P03-AC001",
        "POL-P03-AC002",
        "POL-P03-AC003"
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
    "source_fingerprint": "6de2072a36839706d017f9d2b88a25c7ac7259517fb26a7b87e89ea1aa0115c2",
    "source_lines": "L4153-L4228",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-P03"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-P04",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "41e9f2fac4bfea184ecbd3b3f4eda2ff119d67cab3d07c2ba9ebcc2cc4917169"
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
        "POL-P04-AC001",
        "POL-P04-AC002",
        "POL-P04-AC003"
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
    "source_fingerprint": "41e9f2fac4bfea184ecbd3b3f4eda2ff119d67cab3d07c2ba9ebcc2cc4917169",
    "source_lines": "L4230-L4305",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-P04"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "BDD-27",
        "SD-03"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-P05",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "1f76aede58bc7540e23df10a5bbce29ce52246b80e5b91c2c7165fadb91887f5"
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
        "POL-P05-AC001",
        "POL-P05-AC002",
        "POL-P05-AC003"
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
    "source_fingerprint": "1f76aede58bc7540e23df10a5bbce29ce52246b80e5b91c2c7165fadb91887f5",
    "source_lines": "L4307-L4388",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-P05"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-P06",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "e7b5d5e4991ac6d41413adc14443cba4b43858ac59aa4eefd533506b7137e893"
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
        "POL-P06-AC001",
        "POL-P06-AC002",
        "POL-P06-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P06-O001",
      "obligation_text": "Mọi thay đổi Policy phải được Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "POL-P06 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "POL-P06 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "POL-P06 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "POL-P06-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "POL-P06-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "POL-P06 does not define a recovery obligation."
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
    "source_fingerprint": "e7b5d5e4991ac6d41413adc14443cba4b43858ac59aa4eefd533506b7137e893",
    "source_lines": "L4390-L4498",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-P06"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-P07",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "21c7b4e0a0aa016ca0362c547f5f1a2456278f8b4e280e896f72df0c642307f2"
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
        "POL-P07-AC001",
        "POL-P07-AC002",
        "POL-P07-AC003"
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
    "source_fingerprint": "21c7b4e0a0aa016ca0362c547f5f1a2456278f8b4e280e896f72df0c642307f2",
    "source_lines": "L4500-L4575",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-P07"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-P08",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "ccce0392eb2bd9e62db990893846479d0d8bff5470ddb7bb81fe6d21e5a06e58"
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
        "POL-P08-AC001",
        "POL-P08-AC003",
        "POL-P08-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "POL-P08-O001",
      "obligation_text": "Policy phản ánh quyết định nghiệp vụ"
    },
    {
      "acceptance_criterion_references": [
        "POL-P08-AC002",
        "POL-P08-AC003",
        "POL-P08-AC004"
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
    "source_fingerprint": "ccce0392eb2bd9e62db990893846479d0d8bff5470ddb7bb81fe6d21e5a06e58",
    "source_lines": "L4577-L4662",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-P08"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "POL-P09",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "source_fingerprint": "b6fb0966f89d4875095340097a8c404c402d4bf7ded7227118dddd33ec932484"
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
        "POL-P09-AC001",
        "POL-P09-AC002",
        "POL-P09-AC003"
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
    "source_fingerprint": "b6fb0966f89d4875095340097a8c404c402d4bf7ded7227118dddd33ec932484",
    "source_lines": "L4664-L4739",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-P09"
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
  "normative_statement": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: - Architecture Review - Approval - Versioning - Audit - Traceability",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "POL-P10",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "POL-P10 — Enterprise Governance",
    "source_context_sha256": "d75e2a532d3025daa8bda2543b0d948ad6e54482c4e0aafd3337a14bc5f21837",
    "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
    "source_fingerprint": "66ff1e5c63ddf47133f348bb18615313db863c86e8ec3fc530641c2a2fbda710",
    "source_fingerprint_before_c3": "90e5c7232a187a2d7bb5f34e22879f9d463f1703fa3ce361c3aba2742a2a79fc",
    "source_lines": "L4741-L4805",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > POL-P10"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-POLICY-INDEX-R029",
      "BRD-POLICY-INDEX-R030",
      "BRD-POLICY-INDEX-R031",
      "BRD-POLICY-INDEX-R032",
      "BRD-POLICY-INDEX-R033"
    ]
  },
  "requirement_type": "OPERATIONAL_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "POL-P10",
  "title": "Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
