---
document_code: "BRD-EVENT-INDEX"
title: "Enterprise Business Event Registry"
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

# Enterprise Business Event Registry

## BRD-EVENT-INDEX

---

# 1. Purpose

Enterprise Business Event Registry là tài liệu quản lý tập trung toàn bộ **Business Event** của nền tảng YSim.

Business Event phản ánh những sự kiện nghiệp vụ quan trọng phát sinh trong quá trình hoạt động của Platform.

Business Event là nền tảng của kiến trúc **Event-Driven Architecture (EDA)** và được sử dụng để kết nối các Business Domain theo mô hình Loose Coupling.

Event Registry là **Source of Truth** cho toàn bộ Business Event của hệ thống.

---

# 2. Objectives

Business Event Registry được xây dựng nhằm các mục tiêu:

- Chuẩn hóa Business Event trên toàn Platform.
- Chuẩn hóa Event Naming.
- Chuẩn hóa Event Metadata.
- Chuẩn hóa Publisher / Subscriber.
- Chuẩn hóa Event Version.
- Chuẩn hóa Event Delivery.
- Chuẩn hóa Event Replay.
- Chuẩn hóa Event Governance.
- Làm cơ sở cho Event Bus.
- Làm cơ sở cho Integration Platform.
- Làm cơ sở cho Workflow.
- Làm cơ sở cho Analytics.

---

# 3. Scope

Business Event Registry bao gồm toàn bộ Event phát sinh từ:

- Organization
- Customer
- Product
- Commercial
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

- Cross Platform Events
- System Events
- Integration Events
- Notification Events
- Audit Events

---

# 4. Event Classification

Business Event được phân loại theo Type.

| Type | Description |
|------|-------------|
| Business | Sự kiện nghiệp vụ |
| Domain | Sự kiện nội bộ Domain |
| Integration | Sự kiện tích hợp |
| System | Sự kiện hệ thống |
| Security | Sự kiện bảo mật |
| Notification | Sự kiện truyền thông |
| Operational | Sự kiện vận hành |
| Audit | Sự kiện phục vụ kiểm toán |

Mỗi Event chỉ có một Type chính.

---

# 5. Event Category

Event được nhóm theo Business Domain.

Ví dụ:

- Organization
- Customer
- Commercial
- Promotion
- Order
- Payment
- Inventory
- Fulfillment
- Settlement
- Support
- Notification
- Reporting
- Configuration
- Integration
- Security
- Operations

Category giúp:

- Routing
- Monitoring
- Analytics
- Replay
- Governance

---

# 6. Event Lifecycle

Business Event có vòng đời như sau.

```text
Raised
    │
    ▼
Published
    │
    ▼
Delivered
    │
    ▼
Processed
    │
    ▼
Completed
    │
    ▼
Archived
```

Một Event không bị sửa đổi sau khi Publish.

Nếu có thay đổi sẽ phát sinh Event mới.

---

# 7. Event Delivery Principles

Business Event được truyền theo một trong các chế độ sau.

| Delivery Mode | Description |
|---------------|-------------|
| Sync | Đồng bộ |
| Async | Bất đồng bộ |
| Hybrid | Kết hợp |

Mặc định YSim ưu tiên **Asynchronous Event Processing**.

---

Business Event hỗ trợ các mức bảo đảm sau.

| Delivery Guarantee | Description |
|-------------------|-------------|
| At Most Once | Không Retry |
| At Least Once | Có Retry |
| Exactly Once (Logical) | Đảm bảo ở mức nghiệp vụ |

Tùy từng loại Event sẽ lựa chọn cơ chế phù hợp.

---

Business Event có thể yêu cầu Event Ordering.

Ví dụ:

- Payment
- Settlement
- Financial Event

phải đảm bảo thứ tự xử lý.

Trong khi:

- Marketing
- Analytics
- Notification

không bắt buộc Ordering.

---

# 8. Event Metadata Standard

Mọi Business Event nên có Metadata chuẩn.

| Metadata | Description |
|----------|-------------|
| Event ID | Định danh Event |
| Event Name | Tên Event |
| Event Version | Phiên bản |
| Event Time | Thời điểm phát sinh |
| Correlation ID | Chuỗi liên kết Transaction |
| Causation ID | Event sinh ra Event |
| Tenant ID | Tenant |
| Organization ID | Organization |
| User ID | User |
| Customer ID | Customer |
| Source System | Hệ thống phát sinh |
| Priority | Độ ưu tiên |
| Trace ID | Truy vết |

Metadata giúp:

- Trace
- Replay
- Audit
- Monitoring
- Analytics

---

# 9. Event Identifier

Mỗi Event được cấp một mã định danh duy nhất.

Quy ước:

```text
EVT-000001
EVT-000002
EVT-000003
...
```

Event ID được sử dụng trong:

- BRD
- API
- Integration
- Monitoring
- Audit
- Architecture Review

Event ID là bất biến.

---

# 10. Event Naming Convention

Business Event sử dụng quy tắc:

```text
BusinessObject + Past Tense
```

Ví dụ:

- OrderCreated
- OrderCancelled
- PaymentSucceeded
- PaymentFailed
- SettlementCompleted
- TicketOpened
- TicketClosed
- NotificationDelivered

Không sử dụng:

- CreateOrder
- PaymentDone
- TicketHandle

Tên Event phải phản ánh **điều đã xảy ra**, không phản ánh **hành động sẽ thực hiện**.

---

# 11. Event Principles

## EVT-P01 — Immutable

Business Event là bất biến.

Sau khi Publish không được sửa.

---

## EVT-P02 — Business First

Business Event phản ánh sự kiện nghiệp vụ.

Không phản ánh kỹ thuật.

---

## EVT-P03 — Event Driven

Business Domain giao tiếp thông qua Business Event.

Ưu tiên Loose Coupling.

---

## EVT-P04 — Versioned

Business Event hỗ trợ Version.

Không thay đổi Contract cũ.

---

## EVT-P05 — Replay Ready

Business Event hỗ trợ Replay nếu Policy cho phép.

---

## EVT-P06 — Observable

Business Event phải có khả năng:

- Monitoring
- Logging
- Tracing
- Auditing

---

## EVT-P07 — Canonical

Business Event ưu tiên sử dụng Canonical Event Model.

Không phụ thuộc Connector cụ thể.

---

## EVT-P08 — Enterprise Governance

Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance.

Mọi Event mới phải được:

- Architecture Review
- Approval
- Versioning
- Audit
- Traceability

---

# 12. Relationship to Other Documents

Business Event Registry có quan hệ với các tài liệu sau.

| Document | Relationship |
|----------|--------------|
| BRD Workshop | Định nghĩa Event |
| BRD-BO-INDEX | Event phát sinh từ Business Object |
| BRD-CAP-INDEX | Capability Publish / Subscribe Event |
| DMS | Domain Event |
| API Specification | API Publish Event |
| SDD | Event-Driven Architecture |
| Integration Specification | Event Routing |
| CIP | Event Implementation |

Business Event Registry là **Enterprise Event Dictionary** và là tài liệu tham chiếu thống nhất cho toàn bộ nền tảng YSim.

------

# 13. Enterprise Business Event Registry

## 13.1 Organization Domain

| EVT ID | Business Event | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-000001 | OrganizationCreated | Organization Domain | Configuration, Analytics, Notification | High | Async | No | Yes | v1 | WS-03 |
| EVT-000002 | OrganizationUpdated | Organization Domain | Analytics | Normal | Async | No | Yes | v1 | WS-03 |
| EVT-000003 | OrganizationActivated | Organization Domain | Storefront, Notification | High | Async | No | Yes | v1 | WS-03 |
| EVT-000004 | OrganizationSuspended | Organization Domain | Security, Operations | Critical | Async | Yes | Yes | v1 | WS-03 |
| EVT-000005 | StorefrontCreated | Organization Domain | Analytics | Normal | Async | No | Yes | v1 | WS-03 |
| EVT-000006 | StorefrontPublished | Organization Domain | Customer Portal | High | Async | No | Yes | v1 | WS-03 |
| EVT-000007 | UserInvited | Organization Domain | Notification | Normal | Async | No | Yes | v1 | WS-03 |
| EVT-000008 | UserRoleChanged | Security Domain | Audit, Analytics | High | Async | No | Yes | v1 | WS-03 |

---

## 13.2 Customer Domain

| EVT ID | Business Event | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-010001 | CustomerRegistered | Customer Domain | Notification, Analytics | Normal | Async | No | Yes | v1 | WS-03 |
| EVT-010002 | CustomerIdentityMerged | Customer Domain | Analytics | High | Async | Yes | Yes | v1 | WS-03 |
| EVT-010003 | CustomerPreferenceChanged | Customer Domain | Communication | Normal | Async | No | Yes | v1 | WS-11 |
| EVT-010004 | CustomerConsentUpdated | Security Domain | Audit | High | Async | No | Yes | v1 | WS-16 |
| EVT-010005 | CustomerPortalAccountCreated | Customer Domain | Notification | Normal | Async | No | Yes | v1 | WS-11 |

---

## 13.3 Product Domain

| EVT ID | Business Event | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-020001 | ProductCreated | Product Domain | Analytics | Normal | Async | No | Yes | v1 | WS-04 |
| EVT-020002 | ProductUpdated | Product Domain | Storefront, Analytics | Normal | Async | No | Yes | v1 | WS-04 |
| EVT-020003 | ProductPublished | Product Domain | Storefront | High | Async | No | Yes | v1 | WS-04 |
| EVT-020004 | ProductArchived | Product Domain | Storefront | Normal | Async | No | Yes | v1 | WS-04 |

---

## 13.4 Commercial Domain

| EVT ID | Business Event | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-030001 | PriceBookPublished | Commercial Domain | Storefront, Pricing | High | Async | Yes | Yes | v1 | WS-05 |
| EVT-030002 | PriceBookActivated | Commercial Domain | Pricing Engine | High | Async | Yes | Yes | v1 | WS-05 |
| EVT-030003 | CommercialAgreementActivated | Commercial Domain | Settlement | High | Async | Yes | Yes | v1 | WS-05 |
| EVT-030004 | RevenueSharingUpdated | Commercial Domain | Settlement | High | Async | Yes | Yes | v1 | WS-05 |

---

## 13.5 Promotion Domain

| EVT ID | Business Event | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-040001 | PromotionPublished | Promotion Domain | Storefront | Normal | Async | No | Yes | v1 | WS-06 |
| EVT-040002 | PromotionActivated | Promotion Domain | Pricing Engine | High | Async | No | Yes | v1 | WS-06 |
| EVT-040003 | CouponIssued | Promotion Domain | Customer | Normal | Async | No | Yes | v1 | WS-06 |
| EVT-040004 | CouponRedeemed | Promotion Domain | Analytics, Settlement | High | Async | Yes | Yes | v1 | WS-06 |
| EVT-040005 | PromotionExpired | Promotion Domain | Storefront | Normal | Async | No | Yes | v1 | WS-06 |

---

## 13.6 Order Domain

| EVT ID | Business Event | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-050001 | CartCreated | Order Domain | Analytics | Low | Async | No | Yes | v1 | WS-07 |
| EVT-050002 | CartAbandoned | Order Domain | Marketing | Low | Async | No | Yes | v1 | WS-07 |
| EVT-050003 | CheckoutStarted | Order Domain | Analytics | Normal | Async | No | Yes | v1 | WS-07 |
| EVT-050004 | CheckoutCompleted | Order Domain | Payment | High | Async | Yes | Yes | v1 | WS-07 |
| EVT-050005 | SalesOrderCreated | Order Domain | Payment, Analytics | Critical | Async | Yes | Yes | v1 | WS-07 |
| EVT-050006 | SalesOrderConfirmed | Order Domain | Payment | Critical | Async | Yes | Yes | v1 | WS-07 |
| EVT-050007 | SalesOrderCancelled | Order Domain | Payment, Inventory, Settlement | Critical | Async | Yes | Yes | v1 | WS-07 |

---

## 13.7 Payment Domain

| EVT ID | Business Event | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-060001 | PaymentSessionCreated | Payment Domain | Analytics | Normal | Async | Yes | Yes | v1 | WS-08 |
| EVT-060002 | PaymentStarted | Payment Domain | Analytics | High | Async | Yes | Yes | v1 | WS-08 |
| EVT-060003 | PaymentSucceeded | Payment Domain | Inventory, Settlement, Notification, Analytics | Critical | Async | Yes | Yes | v1 | WS-08 |
| EVT-060004 | PaymentFailed | Payment Domain | Notification | High | Async | Yes | Yes | v1 | WS-08 |
| EVT-060005 | PaymentExpired | Payment Domain | Notification | High | Async | Yes | Yes | v1 | WS-08 |
| EVT-060006 | RefundRequested | Payment Domain | Settlement | High | Async | Yes | Yes | v1 | WS-08 |
| EVT-060007 | RefundCompleted | Payment Domain | Settlement, Notification | Critical | Async | Yes | Yes | v1 | WS-08 |
| EVT-060008 | OfflinePaymentConfirmed | Payment Domain | Inventory, Settlement | Critical | Async | Yes | Yes | v1 | WS-08 |

---

## Design Notes

### Event Criticality

Business Event được phân loại theo mức độ ưu tiên:

| Level | Typical Domains |
|--------|-----------------|
| Critical | Payment, Settlement, Financial |
| High | Order, Inventory, Fulfillment |
| Normal | Customer, Support, Notification |
| Low | Analytics, Marketing |

Criticality là cơ sở để cấu hình:

- Queue Priority
- Retry Policy
- Alert Rule
- Monitoring
- Disaster Recovery
- SLA

------

# 13.8 Financial & Settlement Domain

| EVT ID | Business Event | Source BO | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-070001 | FinancialEventCreated | Financial Event | Settlement Domain | Ledger, Analytics | Critical | Async | Yes | Yes | v1 | WS-10 |
| EVT-070002 | SettlementStarted | Settlement | Settlement Domain | Analytics | High | Async | Yes | Yes | v1 | WS-10 |
| EVT-070003 | SettlementCompleted | Settlement | Settlement Domain | Notification, Analytics | Critical | Async | Yes | Yes | v1 | WS-10 |
| EVT-070004 | SettlementDenied | Settlement | Settlement Domain | Notification | Critical | Async | Yes | Yes | v1 | WS-10 |
| EVT-070005 | CommissionCalculated | Commission Snapshot | Settlement Domain | Wallet | High | Async | Yes | Yes | v1 | WS-10 |
| EVT-070006 | WalletCredited | Wallet | Settlement Domain | Notification | High | Async | Yes | Yes | v1 | WS-10 |
| EVT-070007 | RefundRolledBack | Settlement | Settlement Domain | Ledger | Critical | Async | Yes | Yes | v1 | WS-10 |

---

# 13.9 Customer Success Domain

| EVT ID | Business Event | Source BO | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-080001 | TicketCreated | Ticket | Customer Success | Notification | High | Async | No | Yes | v1 | WS-11 |
| EVT-080002 | TicketAssigned | Ticket | Customer Success | Notification | Normal | Async | No | Yes | v1 | WS-11 |
| EVT-080003 | TicketEscalated | Ticket | Customer Success | Notification | High | Async | Yes | Yes | v1 | WS-11 |
| EVT-080004 | TicketResolved | Ticket | Customer Success | Notification, Survey | High | Async | Yes | Yes | v1 | WS-11 |
| EVT-080005 | TicketReopened | Ticket | Customer Success | Notification | High | Async | Yes | Yes | v1 | WS-11 |
| EVT-080006 | KnowledgeArticlePublished | Knowledge Base Article | Customer Success | Customer Portal | Normal | Async | No | Yes | v1 | WS-11 |
| EVT-080007 | FeatureRequestSubmitted | Feature Request | Customer Success | Product Team | Normal | Async | No | Yes | v1 | WS-11 |

---

# 13.10 Communication Domain

| EVT ID | Business Event | Source BO | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-090001 | NotificationCreated | Notification | Communication | Delivery Queue | Normal | Async | No | Yes | v1 | WS-12 |
| EVT-090002 | NotificationQueued | Notification | Communication | Queue | Normal | Async | No | Yes | v1 | WS-12 |
| EVT-090003 | NotificationSent | Notification | Communication | Analytics | High | Async | No | Yes | v1 | WS-12 |
| EVT-090004 | NotificationDelivered | Notification | Communication | Analytics | High | Async | No | Yes | v1 | WS-12 |
| EVT-090005 | NotificationFailed | Notification | Communication | Retry Engine | High | Async | Yes | Yes | v1 | WS-12 |
| EVT-090006 | NotificationRead | Notification | Customer Portal | Analytics | Normal | Async | No | Yes | v1 | WS-12 |
| EVT-090007 | PortalAnnouncementPublished | Portal Announcement | Communication | Customer Portal | Normal | Async | No | Yes | v1 | WS-12 |

---

# 13.11 Analytics & Reporting Domain

| EVT ID | Business Event | Source BO | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-100001 | DashboardViewed | Dashboard | Analytics | Analytics | Low | Async | No | Yes | v1 | WS-13 |
| EVT-100002 | ReportGenerated | Report | Analytics | Notification | Normal | Async | No | Yes | v1 | WS-13 |
| EVT-100003 | ReportScheduled | Report Schedule | Analytics | Scheduler | Normal | Async | No | Yes | v1 | WS-13 |
| EVT-100004 | KPIThresholdExceeded | KPI Definition | Analytics | Notification | High | Async | No | Yes | v1 | WS-13 |
| EVT-100005 | AlertTriggered | Alert Rule | Analytics | Operations | High | Async | No | Yes | v1 | WS-13 |

---

# 13.12 Platform Configuration Domain

| EVT ID | Business Event | Source BO | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-110001 | ConfigurationPublished | Configuration | Configuration | All Domains | Critical | Async | Yes | Yes | v1 | WS-14 |
| EVT-110002 | ConfigurationApproved | Configuration | Configuration | Notification | High | Async | Yes | Yes | v1 | WS-14 |
| EVT-110003 | ReferenceDataChanged | Reference Data | Configuration | All Domains | High | Async | Yes | Yes | v1 | WS-14 |
| EVT-110004 | BusinessRuleChanged | Business Rule | Configuration | All Domains | High | Async | Yes | Yes | v1 | WS-14 |

---

# 13.13 Integration Domain

| EVT ID | Business Event | Source BO | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-120001 | ConnectorConnected | Connector | Integration | Monitoring | Normal | Async | No | Yes | v1 | WS-15 |
| EVT-120002 | ConnectorDisconnected | Connector | Integration | Monitoring | High | Async | No | Yes | v1 | WS-15 |
| EVT-120003 | CallbackReceived | Callback | Integration | Business Domain | Critical | Async | Yes | Yes | v1 | WS-15 |
| EVT-120004 | QueueMessagePublished | Queue | Integration | Queue Worker | High | Async | Yes | Yes | v1 | WS-15 |
| EVT-120005 | QueueMessageCompleted | Queue | Integration | Monitoring | High | Async | Yes | Yes | v1 | WS-15 |
| EVT-120006 | QueueMessageFailed | Queue | Integration | Retry Engine | High | Async | Yes | Yes | v1 | WS-15 |

---

# 13.14 Security Domain

| EVT ID | Business Event | Source BO | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-130001 | UserAuthenticated | Session | Security | Audit | High | Async | No | Yes | v1 | WS-16 |
| EVT-130002 | AuthenticationFailed | Session | Security | Risk Engine | High | Async | No | Yes | v1 | WS-16 |
| EVT-130003 | PermissionChanged | Permission | Security | Audit | High | Async | No | Yes | v1 | WS-16 |
| EVT-130004 | SecretRotated | Secret | Security | Operations | High | Async | No | Yes | v1 | WS-16 |
| EVT-130005 | RiskDetected | Risk Rule | Security | Operations | Critical | Async | Yes | Yes | v1 | WS-16 |
| EVT-130006 | CustomerConsentChanged | Customer Consent | Security | Audit | High | Async | No | Yes | v1 | WS-16 |

---

# 13.15 Platform Operations Domain

| EVT ID | Business Event | Source BO | Publisher | Primary Subscribers | Criticality | Delivery | Ordering | Replay | Version | Workshop |
|---------|----------------|-----------|-----------|---------------------|------------|----------|----------|--------|---------|----------|
| EVT-140001 | SchedulerTriggered | Scheduler Job | Operations | Worker | High | Async | Yes | Yes | v1 | WS-17 |
| EVT-140002 | JobStarted | Job Execution | Operations | Monitoring | Normal | Async | Yes | Yes | v1 | WS-17 |
| EVT-140003 | JobCompleted | Job Execution | Operations | Monitoring | Normal | Async | Yes | Yes | v1 | WS-17 |
| EVT-140004 | JobFailed | Job Execution | Operations | Retry Engine | High | Async | Yes | Yes | v1 | WS-17 |
| EVT-140005 | MaintenanceStarted | Maintenance Window | Operations | Notification | High | Async | Yes | Yes | v1 | WS-17 |
| EVT-140006 | MaintenanceCompleted | Maintenance Window | Operations | Notification | High | Async | Yes | Yes | v1 | WS-17 |
| EVT-140007 | FeatureFlagChanged | Feature Flag | Operations | All Domains | High | Async | Yes | Yes | v1 | WS-17 |

---

# 13.16 Canonical Event Mapping

YSim sử dụng Canonical Event Model để tách biệt Business Domain với Integration Connector.

Ví dụ:

| Canonical Event | Internal Publisher | External Mapping Examples |
|-----------------|--------------------|---------------------------|
| OrderCreated | Order Domain | Supplier Order API, CRM |
| PaymentSucceeded | Payment Domain | OnePay, GPay, Internal Ledger |
| InventoryAllocated | Inventory Domain | Supplier Stock API |
| FulfillmentCompleted | Fulfillment Domain | Email Gateway, Customer Portal |
| SettlementCompleted | Settlement Domain | Financial Export |
| TicketCreated | Customer Success | CRM, Helpdesk |
| NotificationDelivered | Communication | Email, WhatsApp, Telegram, Zalo OA |

Mọi Connector phải chuyển đổi dữ liệu giữa định dạng riêng của đối tác và Canonical Event Model trước khi Publish hoặc Consume trong Platform.

------

# 14. Enterprise Event Matrix

Business Event là cầu nối giữa Business Object, Business Capability và Event-Driven Architecture.

| Business Event | Source Business Object | Main Capability | Primary Publisher | Primary Subscribers | Snapshot | Policy |
|----------------|------------------------|-----------------|------------------|---------------------|----------|--------|
| OrganizationCreated | Organization | Organization Management | Organization | Configuration, Analytics | No | Organization Policy |
| CustomerRegistered | Customer | Customer Management | Customer | Notification | No | Customer Policy |
| ProductPublished | Product | Product Management | Product | Storefront | No | Product Policy |
| PriceBookPublished | Price Book | Commercial Management | Commercial | Pricing Engine | No | Commercial Policy |
| PromotionActivated | Promotion | Promotion Management | Promotion | Pricing Engine | No | Promotion Policy |
| SalesOrderCreated | Sales Order | Sales Order Management | Order | Payment | Order Snapshot | Order Policy |
| PaymentSucceeded | Payment | Payment Management | Payment | Inventory, Settlement, Notification | Commercial Snapshot | Payment Policy |
| InventoryAllocated | Inventory Allocation | Inventory Allocation | Inventory | Fulfillment | Inventory Snapshot | Allocation Policy |
| FulfillmentCompleted | Fulfillment Session | Fulfillment Management | Fulfillment | Notification | Fulfillment Snapshot | Fulfillment Policy |
| SettlementCompleted | Settlement | Settlement Management | Settlement | Analytics | Financial Snapshot | Settlement Policy |
| TicketCreated | Ticket | Customer Support | Customer Success | Notification | No | Support Policy |
| NotificationDelivered | Notification | Notification Management | Communication | Analytics | No | Communication Policy |

---

# 15. Publisher / Subscriber Matrix

Business Domain giao tiếp thông qua Business Event.

| Publisher | Main Subscribers |
|------------|------------------|
| Organization | Configuration, Analytics, Notification |
| Customer | Notification, Analytics |
| Product | Storefront, Analytics |
| Commercial | Pricing Engine, Settlement |
| Promotion | Pricing Engine, Storefront |
| Order | Payment, Analytics |
| Payment | Inventory, Settlement, Notification, Analytics |
| Inventory | Fulfillment |
| Fulfillment | Communication, Customer Portal |
| Settlement | Ledger, Analytics |
| Customer Success | Notification, Survey |
| Communication | Analytics |
| Configuration | All Domains |
| Integration | Business Domains |
| Security | Audit, Operations |
| Operations | Monitoring |

Business Domain không nên gọi trực tiếp nhau khi có thể sử dụng Business Event.

---

# 16. Event Dependency

Business Event được xử lý theo chuỗi nghiệp vụ.

```text
SalesOrderCreated
        │
        ▼
PaymentSucceeded
        │
        ├─────────────► CommercialSnapshotCreated
        │
        ├─────────────► FinancialEventCreated
        │
        ├─────────────► InventoryAllocationStarted
        │
        ▼
InventoryAllocated
        │
        ▼
FulfillmentStarted
        │
        ▼
FulfillmentCompleted
        │
        ├─────────────► NotificationCreated
        │
        ├─────────────► CustomerPortalUpdated
        │
        ▼
SettlementCompleted
        │
        ▼
AnalyticsUpdated
```

Workflow có thể mở rộng thêm Subscriber mà không cần thay đổi Publisher.

---

# 17. Canonical Event Principles

YSim sử dụng Canonical Event Model.

Nguyên tắc:

## EVT-C01

Business Domain chỉ Publish Canonical Event.

---

## EVT-C02

Connector chịu trách nhiệm chuyển đổi giữa:

- External Event
- Canonical Event

---

## EVT-C03

Business Domain không phụ thuộc định dạng Event của đối tác.

---

## EVT-C04

Canonical Event được Version độc lập.

---

## EVT-C05

Canonical Event là Contract giữa các Domain.

---

## EVT-C06

Business Event ưu tiên tái sử dụng Canonical Vocabulary.

---

# 18. Event Governance

Business Event chỉ được tạo mới khi:

- Có Business Requirement.
- Có Business Object nguồn.
- Có Capability sở hữu.
- Có Publisher rõ ràng.
- Có Subscriber rõ ràng.
- Có Version.
- Có Review.
- Có Approval.

Không Publish Event chỉ phục vụ kỹ thuật.

---

# 19. Event Traceability

Mỗi Business Event phải có khả năng Trace tới:

- Business Requirement
- Business Capability
- Business Object
- Business Rule
- Business Policy
- Snapshot
- API
- Queue
- Connector
- Test Case

Ví dụ:

| Business Event | Traceability |
|----------------|--------------|
| PaymentSucceeded | BRD → Capability → Payment → Snapshot → API → Queue → Test |
| SettlementCompleted | BRD → Settlement → Ledger → Report → Test |
| TicketCreated | BRD → Ticket → Notification → Test |

---

# 20. Event Statistics

## 20.1 Statistics by Domain

| Domain | Estimated Events |
|---------|-----------------:|
| Organization | 8 |
| Customer | 5 |
| Product | 4 |
| Commercial | 4 |
| Promotion | 5 |
| Order | 7 |
| Payment | 8 |
| Inventory & Fulfillment | 10 |
| Settlement | 7 |
| Customer Success | 7 |
| Communication | 7 |
| Analytics | 5 |
| Configuration | 4 |
| Integration | 6 |
| Security | 6 |
| Operations | 7 |

---

## 20.2 Statistics by Type

| Type | Estimated Events |
|------|-----------------:|
| Business | 55+ |
| Domain | 15+ |
| Integration | 10+ |
| Notification | 8+ |
| Security | 8+ |
| Operational | 10+ |
| Audit | 6+ |

---

## 20.3 Total

Tổng số Business Event hiện tại:

**Khoảng 140 Business Events**

Số lượng Event sẽ tăng theo từng phiên bản nhưng Event ID hiện có không thay đổi.

---

# 21. Enterprise Event Principles

## EVT-EP-001

Business Event phản ánh sự kiện đã xảy ra.

---

## EVT-EP-002

Business Event là Immutable.

---

## EVT-EP-003

Business Event độc lập với Database.

---

## EVT-EP-004

Business Event độc lập với UI.

---

## EVT-EP-005

Business Event độc lập với Connector.

---

## EVT-EP-006

Business Event sử dụng Canonical Event Model.

---

## EVT-EP-007

Business Event ưu tiên Asynchronous Processing.

---

## EVT-EP-008

Business Event hỗ trợ Versioning.

---

## EVT-EP-009

Business Event hỗ trợ Replay theo Policy.

---

## EVT-EP-010

Business Event Registry là Enterprise Event Dictionary của YSim.

---

# 22. Relationship to Enterprise Registries

Business Event Registry là một phần của Enterprise Registry Layer.

| Registry | Purpose |
|----------|---------|
| BRD-BO-INDEX | Business Object Registry |
| BRD-CAP-INDEX | Business Capability Registry |
| BRD-EVENT-INDEX | Business Event Registry |
| BRD-POLICY-INDEX | Business Policy Registry |
| BRD-SNAPSHOT-INDEX | Snapshot Registry |

Năm Registry này tạo thành Meta Model thống nhất của nền tảng YSim.

---

# 23. Document Status

Status:

**FROZEN**

Enterprise Business Event Registry là tài liệu nền tảng quản lý toàn bộ Business Event của nền tảng YSim.

Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua:

- Architecture Review
- Approval
- Versioning
- Audit
- Traceability

trước khi được sử dụng trong Platform.

---

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R001 — Ordered financial event families

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R001-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Ordered financial event families",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance evidence identifies the applicable event family and shows sequence preservation only for the families that declare ordering",
      "verifies": [
        "BRD-EVENT-INDEX-R001-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BRD-EVENT-INDEX-R001-AC002",
      "given": "a proposed change with missing traceability or a boundary violation under Ordered financial event families",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BRD-EVENT-INDEX-R001-O001"
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
        "BRD-EVENT-INDEX-R001-AC001",
        "BRD-EVENT-INDEX-R001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R001-O001",
      "obligation_text": "Các event thuộc họ Payment, Settlement và Financial phải duy trì thứ tự xử lý"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-EVENT-INDEX-R001 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-EVENT-INDEX-R001 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-EVENT-INDEX-R001 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-EVENT-INDEX-R001 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-EVENT-INDEX-R001-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-EVENT-INDEX-R001 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Các event thuộc họ Payment, Settlement và Financial phải duy trì thứ tự xử lý.",
  "provenance": {
    "approved_decision_contracts": {
      "P2-DEC-002": {
        "decision_id": "P2-DEC-002",
        "sections": [
          {
            "heading": "Mandatory event types",
            "items": [
              "security.authentication.succeeded",
              "security.authentication.failed",
              "security.mfa.challenge.succeeded",
              "security.mfa.challenge.failed",
              "security.account.locked",
              "security.account.unlocked",
              "security.session.revoked",
              "security.identity.linked",
              "security.identity.unlinked",
              "security.access.denied",
              "security.privilege.changed",
              "security.policy.changed",
              "security.credential.lifecycle.changed",
              "security.federation.trust.changed",
              "security.risk.decision.made",
              "security.suspicious_activity.detected",
              "security.break_glass.started",
              "security.break_glass.ended"
            ]
          },
          {
            "heading": "Shared envelope",
            "items": [
              "event_id",
              "event_type",
              "event_version",
              "occurred_at",
              "producer",
              "organization_id/platform_scope",
              "actor",
              "subject",
              "correlation_id",
              "causation_id",
              "classification",
              "outcome",
              "reason_code",
              "typed payload"
            ]
          },
          {
            "heading": "Contract",
            "items": [
              "Event Registry owns canonical schema and producer declarations.",
              "No password, OTP, token, private key, raw assertion, or secret is allowed.",
              "PII is minimized and stable references are preferred.",
              "Delivery is at least once; consumers deduplicate by event_id.",
              "There is no global ordering; explicit per-subject ordering is used only where declared.",
              "Replay preserves original event identity and adds replay metadata.",
              "Schema changes within a major version are backward-compatible.",
              "Consumer authorization is constrained by Organization, event type, and classification.",
              "Retry, DLQ, alerting, retention, and publish observability are mandatory.",
              "A durable audit/event record exists before a security state-changing operation completes.",
              "Transport topology remains architecture-owned."
            ]
          }
        ],
        "selected_option": 1,
        "status": "DECIDED_PENDING_PACK_APPROVAL",
        "title": "Mandatory Security Platform events"
      }
    },
    "approved_decisions": [
      "P2-DEC-002"
    ],
    "approved_effective_statement_candidate": "Payment, Settlement, and Financial events must preserve processing order.",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-001",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-001",
    "related_non_exception_defect": "EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT",
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Event Delivery Principles",
    "source_context_sha256": "2e7c1ed9552883e1bd1ecd397103a7ec0af0d8a4ff7f069c02ae508cc8aefdca",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "caf87a1651b05ee0f4ce8535fe95f79b475cbefdf72346473ab6b7435b6d7992",
    "source_lines": "L197",
    "source_section": "7. Event Delivery Principles"
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
  "stable_id": "BRD-EVENT-INDEX-R001",
  "title": "Ordered financial event families",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R002 — Unordered non-financial event families

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R002-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Unordered non-financial event families",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance evidence identifies the applicable event family and shows sequence preservation only for the families that declare ordering",
      "verifies": [
        "BRD-EVENT-INDEX-R002-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-EVENT-INDEX-R002-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R002-O001",
      "obligation_text": "Các event thuộc họ Marketing, Analytics và Notification không bắt buộc duy trì thứ tự xử lý"
    }
  ],
  "criticality_applicability": null,
  "criticality_dispositions": [
    {
      "application_status": "APPLIED_IN_PHASE_2C",
      "approved_pack": "V23-P2B-CRITICALITY-DECISION-C1",
      "decision_basis": "DETERMINISTIC_OR_POLICY_REMEDIATION_RECOMMENDATION",
      "exception_id": "P2-CRIT-EXC-004",
      "selected_disposition": "EXPAND_SOURCE_RANGE_AND_REWRITE_EFFECTIVE_STATEMENT"
    }
  ],
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Các event thuộc họ Marketing, Analytics và Notification không bắt buộc duy trì thứ tự xử lý.",
  "provenance": {
    "approved_decisions": [],
    "approved_effective_statement_candidate": "Marketing, Analytics, and Notification events are not required to preserve processing order.",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-002",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-002",
    "remediation_contracts": [
      "V23-P2B-CRITICALITY-DECISION-C1"
    ],
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Event Delivery Principles",
    "source_context_sha256": "2e7c1ed9552883e1bd1ecd397103a7ec0af0d8a4ff7f069c02ae508cc8aefdca",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "c14ec46a5c8f39c83af25e5991bc1592f5787f42bbab120d790d918761c48035",
    "source_lines": "L205",
    "source_section": "7. Event Delivery Principles"
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
  "stable_id": "BRD-EVENT-INDEX-R002",
  "title": "Unordered non-financial event families",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R003 — Mỗi Event được cấp một mã định danh duy nhất

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R003-AC001",
      "given": "the applicable business context, actor, and input for Mỗi Event được cấp một mã định danh duy nhất",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-EVENT-INDEX-R003-O001"
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
        "BRD-EVENT-INDEX-R003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R003-O001",
      "obligation_text": "Mỗi Event được cấp một mã định danh duy nhất"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Event được cấp một mã định danh duy nhất.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-003",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Event Identifier",
    "source_context_sha256": "c10845bd945bf5acf4a52d795b2d4b552e7cc7a995090848e110548d5a88915d",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "2ed5c8b016404af1c3ddc07e39d7bd6df2f76723334cdf4fd0a0e4c02a010c27",
    "source_lines": "L241",
    "source_section": "9. Event Identifier"
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
  "stable_id": "BRD-EVENT-INDEX-R003",
  "title": "Mỗi Event được cấp một mã định danh duy nhất",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R004 — Tên Event phải phản ánh **điều đã xảy ra**, không phản ánh **hành động sẽ thực hiện**

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R004-AC001",
      "given": "the applicable business context, actor, and input for Tên Event phải phản ánh **điều đã xảy ra**, không phản ánh **hành động sẽ thực hiện**",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-EVENT-INDEX-R004-O001"
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
        "BRD-EVENT-INDEX-R004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R004-O001",
      "obligation_text": "Tên Event phải phản ánh **điều đã xảy ra**, không phản ánh **hành động sẽ thực hiện**"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Tên Event phải phản ánh **điều đã xảy ra**, không phản ánh **hành động sẽ thực hiện**.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-004",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Event Naming Convention",
    "source_context_sha256": "bf7b95731b93dc4e2040d96d8c36018db7debd508f1c1b27ed6b55169490e444",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "496a0209c3e2430ca2d44566f53a5da5d2099f2a700c9c7c1ad761679fa351b2",
    "source_lines": "L290",
    "source_section": "10. Event Naming Convention"
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
  "stable_id": "BRD-EVENT-INDEX-R004",
  "title": "Tên Event phải phản ánh **điều đã xảy ra**, không phản ánh **hành động sẽ thực hiện**",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R005 — Mọi Connector phải chuyển đổi dữ liệu giữa định dạng riêng của đối tác và Canonical Event Model …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R005-AC001",
      "given": "a contract interaction at the integration boundary defined by Mọi Connector phải chuyển đổi dữ liệu giữa định dạng riêng của đối tác và Canonical Event Model …",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BRD-EVENT-INDEX-R005-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R005-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Mọi Connector phải chuyển đổi dữ liệu giữa định dạng riêng của đối tác và Canonical Event Model …",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BRD-EVENT-INDEX-R005-O001"
      ],
      "when": "the interaction reaches the integration boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-EVENT-INDEX-R005-AC001",
        "BRD-EVENT-INDEX-R005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R005-O001",
      "obligation_text": "Mọi Connector phải chuyển đổi dữ liệu giữa định dạng riêng của đối tác và Canonical Event Model trước khi Publish hoặc Consume trong Platform"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Connector phải chuyển đổi dữ liệu giữa định dạng riêng của đối tác và Canonical Event Model trước khi Publish hoặc Consume trong Platform.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-005",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13.16 Canonical Event Mapping",
    "source_context_sha256": "dea54e5e4ca47c9e24b8ecf81c2000d9088f9096a257d715472f2815e73495ab",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "56f50cf10683b80e26f9ebd93f99b065993533ddd6c8eac2453b4db792728475",
    "source_lines": "L623",
    "source_section": "13.16 Canonical Event Mapping"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-EVENT-INDEX-R005",
  "title": "Mọi Connector phải chuyển đổi dữ liệu giữa định dạng riêng của đối tác và Canonical Event Model …",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R006 — Workflow có thể mở rộng thêm Subscriber mà không cần thay đổi Publisher

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R006-AC001",
      "given": "the applicable business context, actor, and input for Workflow có thể mở rộng thêm Subscriber mà không cần thay đổi Publisher",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-EVENT-INDEX-R006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-EVENT-INDEX-R006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Workflow có thể mở rộng thêm Subscriber mà không cần thay đổi Publisher",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-EVENT-INDEX-R006-O001"
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
        "BRD-EVENT-INDEX-R006-AC001",
        "BRD-EVENT-INDEX-R006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R006-O001",
      "obligation_text": "Workflow có thể mở rộng thêm Subscriber mà không cần thay đổi Publisher"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Workflow có thể mở rộng thêm Subscriber mà không cần thay đổi Publisher.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-006",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Event Dependency",
    "source_context_sha256": "5e7b2a369549335e8567d19affaecaa338c5cc587caa29ab39e192196a7cbed9",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "3e0fe81fedef0f8afa3c242e5d21f4a6057cbb842dc915e2610198fdfac96d3e",
    "source_lines": "L711",
    "source_section": "16. Event Dependency"
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
  "stable_id": "BRD-EVENT-INDEX-R006",
  "title": "Workflow có thể mở rộng thêm Subscriber mà không cần thay đổi Publisher",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R007 — Business Event chỉ được tạo mới khi: - Có Business Requirement

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R007-AC001",
      "given": "the applicable business context, actor, and input for Business Event chỉ được tạo mới khi: - Có Business Requirement",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-EVENT-INDEX-R007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-EVENT-INDEX-R007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event chỉ được tạo mới khi: - Có Business Requirement",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-EVENT-INDEX-R007-O001"
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
        "BRD-EVENT-INDEX-R007-AC001",
        "BRD-EVENT-INDEX-R007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R007-O001",
      "obligation_text": "Business Event chỉ được tạo mới khi: - Có Business Requirement"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event chỉ được tạo mới khi: - Có Business Requirement.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-007",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Event Governance",
    "source_context_sha256": "ec8476e03e92d884ab03cc2bf1ed465bde36747168c31cc0ce25b07bb9794f06",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "4518e5d9ad5eef35729536e5792d92939d1406b1c673b8c7c1fe9c9058386acb",
    "source_lines": "L762-L764",
    "source_section": "18. Event Governance"
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
  "stable_id": "BRD-EVENT-INDEX-R007",
  "title": "Business Event chỉ được tạo mới khi: - Có Business Requirement",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R008 — Business Event chỉ được tạo mới khi: - Có Business Object nguồn

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R008-AC001",
      "given": "a candidate Business Event chỉ được tạo mới khi: - Có Business Object nguồn record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-EVENT-INDEX-R008-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R008-AC002",
      "given": "a Business Event chỉ được tạo mới khi: - Có Business Object nguồn candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BRD-EVENT-INDEX-R008-O001"
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
        "BRD-EVENT-INDEX-R008-AC001",
        "BRD-EVENT-INDEX-R008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R008-O001",
      "obligation_text": "Business Event chỉ được tạo mới khi: - Có Business Object nguồn"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event chỉ được tạo mới khi: - Có Business Object nguồn.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-008",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Event Governance",
    "source_context_sha256": "ec8476e03e92d884ab03cc2bf1ed465bde36747168c31cc0ce25b07bb9794f06",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "b4536357c1c49f7815c6380b54fb134af92b27288427220ea2512e4cd3cbbde3",
    "source_lines": "L762-L765",
    "source_section": "18. Event Governance"
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
  "stable_id": "BRD-EVENT-INDEX-R008",
  "title": "Business Event chỉ được tạo mới khi: - Có Business Object nguồn",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R009 — Business Event chỉ được tạo mới khi: - Có Capability sở hữu

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R009-AC001",
      "given": "the applicable business context, actor, and input for Business Event chỉ được tạo mới khi: - Có Capability sở hữu",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-EVENT-INDEX-R009-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-EVENT-INDEX-R009-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event chỉ được tạo mới khi: - Có Capability sở hữu",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-EVENT-INDEX-R009-O001"
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
        "BRD-EVENT-INDEX-R009-AC001",
        "BRD-EVENT-INDEX-R009-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R009-O001",
      "obligation_text": "Business Event chỉ được tạo mới khi: - Có Capability sở hữu"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event chỉ được tạo mới khi: - Có Capability sở hữu.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-009",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Event Governance",
    "source_context_sha256": "ec8476e03e92d884ab03cc2bf1ed465bde36747168c31cc0ce25b07bb9794f06",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "5969b6c0782488b4d67dc74157b22685dbf63774dbda3e58a2705937fc456d97",
    "source_lines": "L762-L766",
    "source_section": "18. Event Governance"
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
  "stable_id": "BRD-EVENT-INDEX-R009",
  "title": "Business Event chỉ được tạo mới khi: - Có Capability sở hữu",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R010 — Business Event chỉ được tạo mới khi: - Có Publisher rõ ràng

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R010-AC001",
      "given": "the applicable business context, actor, and input for Business Event chỉ được tạo mới khi: - Có Publisher rõ ràng",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-EVENT-INDEX-R010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-EVENT-INDEX-R010-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event chỉ được tạo mới khi: - Có Publisher rõ ràng",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-EVENT-INDEX-R010-O001"
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
        "BRD-EVENT-INDEX-R010-AC001",
        "BRD-EVENT-INDEX-R010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R010-O001",
      "obligation_text": "Business Event chỉ được tạo mới khi: - Có Publisher rõ ràng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event chỉ được tạo mới khi: - Có Publisher rõ ràng.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-010",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Event Governance",
    "source_context_sha256": "ec8476e03e92d884ab03cc2bf1ed465bde36747168c31cc0ce25b07bb9794f06",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "23505456d167bafce9c51d3be8e1d8e669f97a850d4088bf888a26258a727df1",
    "source_lines": "L762-L767",
    "source_section": "18. Event Governance"
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
  "stable_id": "BRD-EVENT-INDEX-R010",
  "title": "Business Event chỉ được tạo mới khi: - Có Publisher rõ ràng",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R011 — Business Event chỉ được tạo mới khi: - Có Subscriber rõ ràng

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R011-AC001",
      "given": "the applicable business context, actor, and input for Business Event chỉ được tạo mới khi: - Có Subscriber rõ ràng",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-EVENT-INDEX-R011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-EVENT-INDEX-R011-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event chỉ được tạo mới khi: - Có Subscriber rõ ràng",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-EVENT-INDEX-R011-O001"
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
        "BRD-EVENT-INDEX-R011-AC001",
        "BRD-EVENT-INDEX-R011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R011-O001",
      "obligation_text": "Business Event chỉ được tạo mới khi: - Có Subscriber rõ ràng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event chỉ được tạo mới khi: - Có Subscriber rõ ràng.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-011",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Event Governance",
    "source_context_sha256": "ec8476e03e92d884ab03cc2bf1ed465bde36747168c31cc0ce25b07bb9794f06",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "32d54134f6f9a2ae840a6aa91c58ca78cb84ecc9faf5e45465766f35d06ad9d8",
    "source_lines": "L762-L768",
    "source_section": "18. Event Governance"
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
  "stable_id": "BRD-EVENT-INDEX-R011",
  "title": "Business Event chỉ được tạo mới khi: - Có Subscriber rõ ràng",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R012 — Business Event chỉ được tạo mới khi: - Có Version

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R012-AC001",
      "given": "the applicable business context, actor, and input for Business Event chỉ được tạo mới khi: - Có Version",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-EVENT-INDEX-R012-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-EVENT-INDEX-R012-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event chỉ được tạo mới khi: - Có Version",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-EVENT-INDEX-R012-O001"
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
        "BRD-EVENT-INDEX-R012-AC001",
        "BRD-EVENT-INDEX-R012-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R012-O001",
      "obligation_text": "Business Event chỉ được tạo mới khi: - Có Version"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event chỉ được tạo mới khi: - Có Version.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-012",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Event Governance",
    "source_context_sha256": "ec8476e03e92d884ab03cc2bf1ed465bde36747168c31cc0ce25b07bb9794f06",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "683e2f6ccb77ccc8b7bacdf1ff0ccdd710f916f3986913a68e13a936976a6637",
    "source_lines": "L762-L769",
    "source_section": "18. Event Governance"
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
  "stable_id": "BRD-EVENT-INDEX-R012",
  "title": "Business Event chỉ được tạo mới khi: - Có Version",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R013 — Business Event chỉ được tạo mới khi: - Có Review

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R013-AC001",
      "given": "the applicable business context, actor, and input for Business Event chỉ được tạo mới khi: - Có Review",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-EVENT-INDEX-R013-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-EVENT-INDEX-R013-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event chỉ được tạo mới khi: - Có Review",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-EVENT-INDEX-R013-O001"
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
        "BRD-EVENT-INDEX-R013-AC001",
        "BRD-EVENT-INDEX-R013-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R013-O001",
      "obligation_text": "Business Event chỉ được tạo mới khi: - Có Review"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event chỉ được tạo mới khi: - Có Review.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-013",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Event Governance",
    "source_context_sha256": "ec8476e03e92d884ab03cc2bf1ed465bde36747168c31cc0ce25b07bb9794f06",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "fa7c850d6c275e89cbdaee0d1960c8d48c21a2b517cb8fee70d95120c789cade",
    "source_lines": "L762-L770",
    "source_section": "18. Event Governance"
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
  "stable_id": "BRD-EVENT-INDEX-R013",
  "title": "Business Event chỉ được tạo mới khi: - Có Review",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R014 — Business Event chỉ được tạo mới khi: - Có Approval

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R014-AC001",
      "given": "the applicable business context, actor, and input for Business Event chỉ được tạo mới khi: - Có Approval",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BRD-EVENT-INDEX-R014-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_APPROVAL_BOUNDARY_V1",
      "criterion_id": "BRD-EVENT-INDEX-R014-AC002",
      "given": "a governed change with missing, expired, rejected, or unauthorized approval under Business Event chỉ được tạo mới khi: - Có Approval",
      "observable_evidence": "change identity, approval policy and status, approver authorization, rejection or pending reason, and unchanged accepted state",
      "then": "the change does not enter the accepted state and the approval reason and status remain observable",
      "verifies": [
        "BRD-EVENT-INDEX-R014-O001"
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
        "BRD-EVENT-INDEX-R014-AC001",
        "BRD-EVENT-INDEX-R014-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R014-O001",
      "obligation_text": "Business Event chỉ được tạo mới khi: - Có Approval"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event chỉ được tạo mới khi: - Có Approval.",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-014",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Event Governance",
    "source_context_sha256": "ec8476e03e92d884ab03cc2bf1ed465bde36747168c31cc0ce25b07bb9794f06",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "2709a16d1fadbdfeb14c0ae2aaae90ac10110800bb6fe66586d2986ac633aee1",
    "source_lines": "L762-L771",
    "source_section": "18. Event Governance"
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
  "stable_id": "BRD-EVENT-INDEX-R014",
  "title": "Business Event chỉ được tạo mới khi: - Có Approval",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R025 — Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Architecture Review

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R025-AC001",
      "given": "the applicable business context, actor, and input for Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Architecture Review",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-EVENT-INDEX-R025-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-EVENT-INDEX-R025-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Architecture Review",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-EVENT-INDEX-R025-O001"
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
        "BRD-EVENT-INDEX-R025-AC001",
        "BRD-EVENT-INDEX-R025-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R025-O001",
      "obligation_text": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Architecture Review"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Architecture Review",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-025",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Document Status",
    "source_context_sha256": "a507d145b1852e82de360ae97ec9ccb19d2c1f8c38935b4134a6e455e9e87280",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "4b1dda7cba54c40a86e2b63f3d9287bde844cb5e09528add06b66923009222b9",
    "source_lines": "L937-L939",
    "source_section": "23. Document Status"
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
  "stable_id": "BRD-EVENT-INDEX-R025",
  "title": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Architecture Review",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R026 — Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Approval

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R026-AC001",
      "given": "the applicable business context, actor, and input for Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Approval",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BRD-EVENT-INDEX-R026-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_APPROVAL_BOUNDARY_V1",
      "criterion_id": "BRD-EVENT-INDEX-R026-AC002",
      "given": "a governed change with missing, expired, rejected, or unauthorized approval under Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Approval",
      "observable_evidence": "change identity, approval policy and status, approver authorization, rejection or pending reason, and unchanged accepted state",
      "then": "the change does not enter the accepted state and the approval reason and status remain observable",
      "verifies": [
        "BRD-EVENT-INDEX-R026-O001"
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
        "BRD-EVENT-INDEX-R026-AC001",
        "BRD-EVENT-INDEX-R026-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R026-O001",
      "obligation_text": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Approval"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Approval",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-026",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Document Status",
    "source_context_sha256": "a507d145b1852e82de360ae97ec9ccb19d2c1f8c38935b4134a6e455e9e87280",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "8aecfb5a9c08bade116a67be37d1592dbaccfd19c7565e4433e8749ca39c48b5",
    "source_lines": "L937-L940",
    "source_section": "23. Document Status"
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
  "stable_id": "BRD-EVENT-INDEX-R026",
  "title": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Approval",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R027 — Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Versioning

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R027-AC001",
      "given": "the applicable business context, actor, and input for Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Versioning",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-EVENT-INDEX-R027-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-EVENT-INDEX-R027-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Versioning",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-EVENT-INDEX-R027-O001"
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
        "BRD-EVENT-INDEX-R027-AC001",
        "BRD-EVENT-INDEX-R027-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R027-O001",
      "obligation_text": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Versioning"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Versioning",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-027",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-027",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Document Status",
    "source_context_sha256": "a507d145b1852e82de360ae97ec9ccb19d2c1f8c38935b4134a6e455e9e87280",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "8597d8fc475e75807abb33654657f7bbe667b0123f302a3ce3272b4e771a201c",
    "source_lines": "L937-L941",
    "source_section": "23. Document Status"
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
  "stable_id": "BRD-EVENT-INDEX-R027",
  "title": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Versioning",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R028 — Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R028-AC001",
      "given": "an operational task within the scope of Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-EVENT-INDEX-R028-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-EVENT-INDEX-R028-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-EVENT-INDEX-R028-O001"
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
        "BRD-EVENT-INDEX-R028-AC001",
        "BRD-EVENT-INDEX-R028-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R028-O001",
      "obligation_text": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-EVENT-INDEX-R028 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-EVENT-INDEX-R028 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-EVENT-INDEX-R028 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-EVENT-INDEX-R028 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-EVENT-INDEX-R028-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-EVENT-INDEX-R028 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Audit",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-028",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-028",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Document Status",
    "source_context_sha256": "a507d145b1852e82de360ae97ec9ccb19d2c1f8c38935b4134a6e455e9e87280",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "cd97f070eb7411035b5658cb1a685237060571de9111aedf51764225fd2f7b0b",
    "source_lines": "L937-L942",
    "source_section": "23. Document Status"
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
  "stable_id": "BRD-EVENT-INDEX-R028",
  "title": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-EVENT-INDEX-R029 — Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Traceability

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-EVENT-INDEX-R029-AC001",
      "given": "the applicable business context, actor, and input for Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Traceability",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-EVENT-INDEX-R029-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-EVENT-INDEX-R029-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Traceability",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-EVENT-INDEX-R029-O001"
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
        "BRD-EVENT-INDEX-R029-AC001",
        "BRD-EVENT-INDEX-R029-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-EVENT-INDEX-R029-O001",
      "obligation_text": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Traceability"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Traceability",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-EVENT-INDEX-029",
    "previous_temporary_key": "TMP-BRD-EVENT-INDEX-029",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Document Status",
    "source_context_sha256": "a507d145b1852e82de360ae97ec9ccb19d2c1f8c38935b4134a6e455e9e87280",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "6ca4d90a85777a113d9e4a10b27715fac549c7f213444bef371d75116bf225b0",
    "source_lines": "L937-L943",
    "source_section": "23. Document Status"
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
  "stable_id": "BRD-EVENT-INDEX-R029",
  "title": "Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Traceability",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-C01 — Business Domain chỉ Publish Canonical Event

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-C01-AC001",
      "given": "the applicable business context, actor, and input for Business Domain chỉ Publish Canonical Event",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-C01-O001"
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
        "EVT-C01-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-C01-O001",
      "obligation_text": "Business Domain chỉ Publish Canonical Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain chỉ Publish Canonical Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-C01",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-C01",
    "source_context_sha256": "aae6c537a76b81bfd0edfc2e64c6046ee959e057a3288ce9185285dcf885dfcd",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "c15df88066447cf2be2404e03ec629608a3c09be789a86c986763638b417e957",
    "source_lines": "L721-L724",
    "source_section": "17. Canonical Event Principles > EVT-C01"
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
  "stable_id": "EVT-C01",
  "title": "Business Domain chỉ Publish Canonical Event",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-C02 — Connector chịu trách nhiệm chuyển đổi giữa: - External Event - Canonical Event

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EVT-C02-AC001",
      "given": "a contract interaction at the integration boundary defined by Connector chịu trách nhiệm chuyển đổi giữa: - External Event - Canonical Event",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EVT-C02-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EVT-C02-AC002",
      "given": "a contract interaction at the integration boundary defined by Connector chịu trách nhiệm chuyển đổi giữa: - External Event - Canonical Event",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EVT-C02-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "EVT-C02-AC003",
      "given": "an interaction that violates the contract or ownership boundary for Connector chịu trách nhiệm chuyển đổi giữa: - External Event - Canonical Event",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "EVT-C02-O001",
        "EVT-C02-O002"
      ],
      "when": "the interaction reaches the integration boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EVT-C02-AC001",
        "EVT-C02-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-C02-O001",
      "obligation_text": "Connector chịu trách nhiệm chuyển đổi giữa: External Event."
    },
    {
      "acceptance_criterion_references": [
        "EVT-C02-AC002",
        "EVT-C02-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-C02-O002",
      "obligation_text": "Connector chịu trách nhiệm chuyển đổi giữa: Canonical Event."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector chịu trách nhiệm chuyển đổi giữa: - External Event - Canonical Event",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-C02",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-C02",
    "source_context_sha256": "bdf65c73f3f834315d1d3c70bb6226b21154323acef2740eabe2ea68452131c2",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "9dc172ca1dd08c4d3663972a77bd31de4a60c3d9dcd71ade6326fee718cd8a0d",
    "source_lines": "L727-L733",
    "source_section": "17. Canonical Event Principles > EVT-C02"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EVT-C02",
  "title": "Connector chịu trách nhiệm chuyển đổi giữa: - External Event - Canonical Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-C03 — Business Domain không phụ thuộc định dạng Event của đối tác

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-C03-AC001",
      "given": "the applicable business context, actor, and input for Business Domain không phụ thuộc định dạng Event của đối tác",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-C03-O001"
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
        "EVT-C03-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-C03-O001",
      "obligation_text": "Business Domain không phụ thuộc định dạng Event của đối tác"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain không phụ thuộc định dạng Event của đối tác.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-C03",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-C03",
    "source_context_sha256": "94b72476e80c7618c00ab22cab4bb6db56d3e5d20ba6b5ec26974da16ae4b082",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "5cf679a8d7c9ef933c4f4d02613a54d3073ececf7e79d9c2abddae4fdbba4b8f",
    "source_lines": "L736-L739",
    "source_section": "17. Canonical Event Principles > EVT-C03"
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
  "stable_id": "EVT-C03",
  "title": "Business Domain không phụ thuộc định dạng Event của đối tác",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-C04 — Canonical Event được Version độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-C04-AC001",
      "given": "the applicable business context, actor, and input for Canonical Event được Version độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "EVT-C04-O001"
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
        "EVT-C04-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-C04-O001",
      "obligation_text": "Canonical Event được Version độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Canonical Event được Version độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-C04",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-C04",
    "source_context_sha256": "5a1bc2ec0ef7bfb6a731b68f215171c7a00e30d3a5cc6463c6b4cddaa92bd881",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "b4ac232940b3740200df00c774d481c7d9d8c5ea1d7fdb89f48bdb428a5cc961",
    "source_lines": "L742-L745",
    "source_section": "17. Canonical Event Principles > EVT-C04"
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
  "stable_id": "EVT-C04",
  "title": "Canonical Event được Version độc lập",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-C05 — Canonical Event là Contract giữa các Domain

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-C05-AC001",
      "given": "the applicable business context, actor, and input for Canonical Event là Contract giữa các Domain",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-C05-O001"
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
        "EVT-C05-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-C05-O001",
      "obligation_text": "Canonical Event là Contract giữa các Domain"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Canonical Event là Contract giữa các Domain.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-C05",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-C05",
    "source_context_sha256": "dddb91342a6ac4fd685ec43149873633637c48aad1526101585c4520b063afc9",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "5558efdae899a16cd037c122f487e9e7168a24fca4fccf6c28ef0d85b51005f9",
    "source_lines": "L748-L751",
    "source_section": "17. Canonical Event Principles > EVT-C05"
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
  "stable_id": "EVT-C05",
  "title": "Canonical Event là Contract giữa các Domain",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-C06 — Business Event ưu tiên tái sử dụng Canonical Vocabulary

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-C06-AC001",
      "given": "the applicable business context, actor, and input for Business Event ưu tiên tái sử dụng Canonical Vocabulary",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-C06-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-C06-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event ưu tiên tái sử dụng Canonical Vocabulary",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-C06-O001"
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
        "EVT-C06-AC001",
        "EVT-C06-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-C06-O001",
      "obligation_text": "Business Event ưu tiên tái sử dụng Canonical Vocabulary"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event ưu tiên tái sử dụng Canonical Vocabulary.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-C06",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-C06",
    "source_context_sha256": "f2551cd11884c51c6500f8631b39a8902699de3601141263f53e90484e225fe4",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "30414c4e9e7bff7b811daa059bafdc599a9ddf827db7f2d3a9682c8d704aaa7c",
    "source_lines": "L754-L757",
    "source_section": "17. Canonical Event Principles > EVT-C06"
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
  "stable_id": "EVT-C06",
  "title": "Business Event ưu tiên tái sử dụng Canonical Vocabulary",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-EP-001 — Business Event phản ánh sự kiện đã xảy ra

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-EP-001-AC001",
      "given": "the applicable business context, actor, and input for Business Event phản ánh sự kiện đã xảy ra",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-EP-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-EP-001-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event phản ánh sự kiện đã xảy ra",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-EP-001-O001"
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
        "EVT-EP-001-AC001",
        "EVT-EP-001-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-EP-001-O001",
      "obligation_text": "Business Event phản ánh sự kiện đã xảy ra"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event phản ánh sự kiện đã xảy ra.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-EP-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-EP-001",
    "source_context_sha256": "a7f5a8e90e24bde7ccc93eaf28d742555b83ebb9f97e1f70472d2991b2c26d49",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "a99a73926a0bedb0b852f6a4900cc747585071de73af887d14cdc79285f8af35",
    "source_lines": "L853-L856",
    "source_section": "21. Enterprise Event Principles > EVT-EP-001"
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
  "stable_id": "EVT-EP-001",
  "title": "Business Event phản ánh sự kiện đã xảy ra",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-EP-002 — Business Event là Immutable

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-EP-002-AC001",
      "given": "the applicable business context, actor, and input for Business Event là Immutable",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-EP-002-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-EP-002-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event là Immutable",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-EP-002-O001"
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
        "EVT-EP-002-AC001",
        "EVT-EP-002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-EP-002-O001",
      "obligation_text": "Business Event là Immutable"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EVT-EP-002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EVT-EP-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EVT-EP-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EVT-EP-002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EVT-EP-002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EVT-EP-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event là Immutable.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-EP-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-EP-002",
    "source_context_sha256": "01a97ae3d5336104d9c51c7a61e4029edfe0f0b0aeeb7aa9de88a158bcb1c8c1",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "ee6ef4799d6c1d9e463426388704b01ca509c0680da9e410f097b9ab74ac4311",
    "source_lines": "L859-L862",
    "source_section": "21. Enterprise Event Principles > EVT-EP-002"
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
  "stable_id": "EVT-EP-002",
  "title": "Business Event là Immutable",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-EP-003 — Business Event độc lập với Database

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-EP-003-AC001",
      "given": "the applicable business context, actor, and input for Business Event độc lập với Database",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "EVT-EP-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-EP-003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event độc lập với Database",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-EP-003-O001"
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
        "EVT-EP-003-AC001",
        "EVT-EP-003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-EP-003-O001",
      "obligation_text": "Business Event độc lập với Database"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event độc lập với Database.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-EP-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-EP-003",
    "source_context_sha256": "604089de19b3ae80ddc68abd0d11abb3a4236c8874af06fbeb4d08b68d189a57",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "2144ee7d42af678461ae6c5bd628c3e84f86b781d2728403c25ab72866fcaa11",
    "source_lines": "L865-L868",
    "source_section": "21. Enterprise Event Principles > EVT-EP-003"
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
  "stable_id": "EVT-EP-003",
  "title": "Business Event độc lập với Database",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-EP-004 — Business Event độc lập với UI

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-EP-004-AC001",
      "given": "the applicable business context, actor, and input for Business Event độc lập với UI",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "EVT-EP-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-EP-004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event độc lập với UI",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-EP-004-O001"
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
        "EVT-EP-004-AC001",
        "EVT-EP-004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-EP-004-O001",
      "obligation_text": "Business Event độc lập với UI"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event độc lập với UI.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-EP-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-EP-004",
    "source_context_sha256": "091a72bdd72f2c463af718e903641b8dba38f2fbb4340cac8b9ddce21390cef4",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "9d28b61b760ccbf9c8f8d77f25cb7d4b935f6eb8feb110c3b2e87f84a59a06dd",
    "source_lines": "L871-L874",
    "source_section": "21. Enterprise Event Principles > EVT-EP-004"
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
  "stable_id": "EVT-EP-004",
  "title": "Business Event độc lập với UI",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-EP-005 — Business Event độc lập với Connector

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EVT-EP-005-AC001",
      "given": "a contract interaction at the integration boundary defined by Business Event độc lập với Connector",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "each boundary object keeps a distinct identity, owner, reference, and lifecycle; changing one does not implicitly mutate the other",
      "verifies": [
        "EVT-EP-005-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "EVT-EP-005-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Business Event độc lập với Connector",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "EVT-EP-005-O001"
      ],
      "when": "the interaction reaches the integration boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EVT-EP-005-AC001",
        "EVT-EP-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-EP-005-O001",
      "obligation_text": "Business Event độc lập với Connector"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event độc lập với Connector.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-EP-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-EP-005",
    "source_context_sha256": "8771e958aad2a70da69a06fead5d00acc4a3ffc0cd4b352cc561b2b4a55918c5",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "993b03efbef621efc9e23c0dee2a24c91c67805a1c9e388040aba04c0cbb961b",
    "source_lines": "L877-L880",
    "source_section": "21. Enterprise Event Principles > EVT-EP-005"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EVT-EP-005",
  "title": "Business Event độc lập với Connector",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-EP-006 — Business Event sử dụng Canonical Event Model

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-EP-006-AC001",
      "given": "the applicable business context, actor, and input for Business Event sử dụng Canonical Event Model",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-EP-006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-EP-006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event sử dụng Canonical Event Model",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-EP-006-O001"
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
        "EVT-EP-006-AC001",
        "EVT-EP-006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-EP-006-O001",
      "obligation_text": "Business Event sử dụng Canonical Event Model"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event sử dụng Canonical Event Model.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-EP-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-EP-006",
    "source_context_sha256": "537409b3aed83529e3fff33ae22c141114c686a845b033b077493ce6de40bb68",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "5c6e0aac1cc8546793a1326404a82b42a64355750f9942ad4bb10200bc97ba8d",
    "source_lines": "L883-L886",
    "source_section": "21. Enterprise Event Principles > EVT-EP-006"
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
  "stable_id": "EVT-EP-006",
  "title": "Business Event sử dụng Canonical Event Model",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-EP-007 — Business Event ưu tiên Asynchronous Processing

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-EP-007-AC001",
      "given": "the applicable business context, actor, and input for Business Event ưu tiên Asynchronous Processing",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-EP-007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-EP-007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event ưu tiên Asynchronous Processing",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-EP-007-O001"
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
        "EVT-EP-007-AC001",
        "EVT-EP-007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-EP-007-O001",
      "obligation_text": "Business Event ưu tiên Asynchronous Processing"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event ưu tiên Asynchronous Processing.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-EP-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-EP-007",
    "source_context_sha256": "ea9d2d39ca745fcb6815bda67bc3f5b57c8b5201f4cf44253d7c08df3521dc8a",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "fa63f286440bb225bb7e1426e0ca743c4f30f7b832445d3a80be45eabf52ea58",
    "source_lines": "L889-L892",
    "source_section": "21. Enterprise Event Principles > EVT-EP-007"
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
  "stable_id": "EVT-EP-007",
  "title": "Business Event ưu tiên Asynchronous Processing",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-EP-008 — Business Event hỗ trợ Versioning

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-EP-008-AC001",
      "given": "the applicable business context, actor, and input for Business Event hỗ trợ Versioning",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-EP-008-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-EP-008-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event hỗ trợ Versioning",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-EP-008-O001"
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
        "EVT-EP-008-AC001",
        "EVT-EP-008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-EP-008-O001",
      "obligation_text": "Business Event hỗ trợ Versioning"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event hỗ trợ Versioning.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-EP-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-EP-008",
    "source_context_sha256": "91acc7f4806bf561d436451394cfd1f279efb11759390a3734b6b1a51b5d2f86",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "3bf60974ba13f9e1636fe4cb6f92421d79c6f4ceb3b5470a9eee58c829ae86d0",
    "source_lines": "L895-L898",
    "source_section": "21. Enterprise Event Principles > EVT-EP-008"
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
  "stable_id": "EVT-EP-008",
  "title": "Business Event hỗ trợ Versioning",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-EP-009 — Business Event hỗ trợ Replay theo Policy

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-EP-009-AC001",
      "given": "an operational task within the scope of Business Event hỗ trợ Replay theo Policy",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EVT-EP-009-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EVT-EP-009-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Business Event hỗ trợ Replay theo Policy",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EVT-EP-009-O001"
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
        "EVT-EP-009-AC001",
        "EVT-EP-009-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-EP-009-O001",
      "obligation_text": "Business Event hỗ trợ Replay theo Policy"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event hỗ trợ Replay theo Policy.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-EP-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-EP-009",
    "source_context_sha256": "6353c3e460cad15fec1015db2daec24c1f86ce5946cea805e42f4066ca41946c",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "4876c37cca0e764340fc7e870de37219d65d6b683e3818a28ca58a05ee9a8009",
    "source_lines": "L901-L904",
    "source_section": "21. Enterprise Event Principles > EVT-EP-009"
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
  "stable_id": "EVT-EP-009",
  "title": "Business Event hỗ trợ Replay theo Policy",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-EP-010 — Business Event Registry là Enterprise Event Dictionary của YSim

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-EP-010-AC001",
      "given": "the applicable business context, actor, and input for Business Event Registry là Enterprise Event Dictionary của YSim",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-EP-010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-EP-010-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event Registry là Enterprise Event Dictionary của YSim",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-EP-010-O001"
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
        "EVT-EP-010-AC001",
        "EVT-EP-010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-EP-010-O001",
      "obligation_text": "Business Event Registry là Enterprise Event Dictionary của YSim"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event Registry là Enterprise Event Dictionary của YSim.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-002"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-EP-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-EP-010",
    "source_context_sha256": "43ed424ec7432d57c6acedc11f945c4e1b9f6503dcab82699db23d138cc90b1c",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "1eba054e26a298b4a9cde6b2e237529c437ca39005c72a1f3b4b73eb30294634",
    "source_lines": "L907-L910",
    "source_section": "21. Enterprise Event Principles > EVT-EP-010"
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
  "stable_id": "EVT-EP-010",
  "title": "Business Event Registry là Enterprise Event Dictionary của YSim",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-P01 — Business Event là bất biến. Sau khi Publish không được sửa

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P01-AC001",
      "given": "the applicable business context, actor, and input for Business Event là bất biến. Sau khi Publish không được sửa",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-P01-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P01-AC002",
      "given": "the applicable business context, actor, and input for Business Event là bất biến. Sau khi Publish không được sửa",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "EVT-P01-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-P01-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event là bất biến. Sau khi Publish không được sửa",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-P01-O001",
        "EVT-P01-O002"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EVT-P01-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Business Event là bất biến. Sau khi Publish không được sửa",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EVT-P01-O001",
        "EVT-P01-O002"
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
        "EVT-P01-AC001",
        "EVT-P01-AC003",
        "EVT-P01-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P01-O001",
      "obligation_text": "Business Event là bất biến"
    },
    {
      "acceptance_criterion_references": [
        "EVT-P01-AC002",
        "EVT-P01-AC003",
        "EVT-P01-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P01-O002",
      "obligation_text": "Sau khi Publish không được sửa"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EVT-P01 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EVT-P01 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EVT-P01 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EVT-P01-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EVT-P01-AC001",
        "EVT-P01-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EVT-P01 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event là bất biến. Sau khi Publish không được sửa.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-P01",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-P01 — Immutable",
    "source_context_sha256": "848ff9a6967db7dd0237b87aba5cc98e92c5fc389a3a530c58ab862b7deb72d4",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "9a4163b325d9daf42b011f03991df2763f7d8fe0769c5cabb3905e3d1ee60ab8",
    "source_lines": "L296-L301",
    "source_section": "11. Event Principles > EVT-P01 — Immutable"
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
  "stable_id": "EVT-P01",
  "title": "Business Event là bất biến. Sau khi Publish không được sửa",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-P02 — Business Event phản ánh sự kiện nghiệp vụ. Không phản ánh kỹ thuật

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P02-AC001",
      "given": "the applicable business context, actor, and input for Business Event phản ánh sự kiện nghiệp vụ. Không phản ánh kỹ thuật",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-P02-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P02-AC002",
      "given": "the applicable business context, actor, and input for Business Event phản ánh sự kiện nghiệp vụ. Không phản ánh kỹ thuật",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-P02-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-P02-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event phản ánh sự kiện nghiệp vụ. Không phản ánh kỹ thuật",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-P02-O001",
        "EVT-P02-O002"
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
        "EVT-P02-AC001",
        "EVT-P02-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P02-O001",
      "obligation_text": "Business Event phản ánh sự kiện nghiệp vụ"
    },
    {
      "acceptance_criterion_references": [
        "EVT-P02-AC002",
        "EVT-P02-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P02-O002",
      "obligation_text": "Không phản ánh kỹ thuật"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event phản ánh sự kiện nghiệp vụ. Không phản ánh kỹ thuật.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-P02",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-P02 — Business First",
    "source_context_sha256": "3e4568483a5f746351fa826792e923b758b2698fe7f65767ff16be26859eba3d",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "8a32683b1df127109523c27e81224c277e0a30bf51fc2f4052ad5b4d7c00138e",
    "source_lines": "L304-L309",
    "source_section": "11. Event Principles > EVT-P02 — Business First"
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
  "stable_id": "EVT-P02",
  "title": "Business Event phản ánh sự kiện nghiệp vụ. Không phản ánh kỹ thuật",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-P03 — Business Domain giao tiếp thông qua Business Event. Ưu tiên Loose Coupling

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P03-AC001",
      "given": "the applicable business context, actor, and input for Business Domain giao tiếp thông qua Business Event. Ưu tiên Loose Coupling",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-P03-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P03-AC002",
      "given": "the applicable business context, actor, and input for Business Domain giao tiếp thông qua Business Event. Ưu tiên Loose Coupling",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-P03-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-P03-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Business Domain giao tiếp thông qua Business Event. Ưu tiên Loose Coupling",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-P03-O001",
        "EVT-P03-O002"
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
        "EVT-P03-AC001",
        "EVT-P03-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P03-O001",
      "obligation_text": "Business Domain giao tiếp thông qua Business Event"
    },
    {
      "acceptance_criterion_references": [
        "EVT-P03-AC002",
        "EVT-P03-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P03-O002",
      "obligation_text": "Ưu tiên Loose Coupling"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain giao tiếp thông qua Business Event. Ưu tiên Loose Coupling.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-P03",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-P03 — Event Driven",
    "source_context_sha256": "49e43023c2ec865f1b9c6ead8ebd772886ee288cbfb5786c4ee6c1aa014cf3d2",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "0b57d3814d1b19f53510a91794ba5eda51bce2877a8646abb58fb90756069f16",
    "source_lines": "L312-L317",
    "source_section": "11. Event Principles > EVT-P03 — Event Driven"
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
  "stable_id": "EVT-P03",
  "title": "Business Domain giao tiếp thông qua Business Event. Ưu tiên Loose Coupling",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-P04 — Business Event hỗ trợ Version. Không thay đổi Contract cũ

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P04-AC001",
      "given": "the applicable business context, actor, and input for Business Event hỗ trợ Version. Không thay đổi Contract cũ",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-P04-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P04-AC002",
      "given": "the applicable business context, actor, and input for Business Event hỗ trợ Version. Không thay đổi Contract cũ",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EVT-P04-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EVT-P04-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event hỗ trợ Version. Không thay đổi Contract cũ",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EVT-P04-O001",
        "EVT-P04-O002"
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
        "EVT-P04-AC001",
        "EVT-P04-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P04-O001",
      "obligation_text": "Business Event hỗ trợ Version"
    },
    {
      "acceptance_criterion_references": [
        "EVT-P04-AC002",
        "EVT-P04-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P04-O002",
      "obligation_text": "Không thay đổi Contract cũ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event hỗ trợ Version. Không thay đổi Contract cũ.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-P04",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-P04 — Versioned",
    "source_context_sha256": "a7b25876d5c6c40bcf44c869d0fa504f9a5a4616c157663a93c3385bdfbfa932",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "9221718f6071894bbe8b0989e16cc664661fa4e0eca7e4a32354de2a57c68077",
    "source_lines": "L320-L325",
    "source_section": "11. Event Principles > EVT-P04 — Versioned"
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
  "stable_id": "EVT-P04",
  "title": "Business Event hỗ trợ Version. Không thay đổi Contract cũ",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-P05 — Business Event hỗ trợ Replay nếu Policy cho phép

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P05-AC001",
      "given": "an operational task within the scope of Business Event hỗ trợ Replay nếu Policy cho phép",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EVT-P05-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EVT-P05-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Business Event hỗ trợ Replay nếu Policy cho phép",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EVT-P05-O001"
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
        "EVT-P05-AC001",
        "EVT-P05-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P05-O001",
      "obligation_text": "Business Event hỗ trợ Replay nếu Policy cho phép"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event hỗ trợ Replay nếu Policy cho phép.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-P05",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-P05 — Replay Ready",
    "source_context_sha256": "483bc90527822efbb15c83d75aa620fb482a77c5879e328b542b2aacf5ec3168",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "ce388322c60fdec54f4efa86cfaa7e449d6cb41aaa408df05697ce920e7cc319",
    "source_lines": "L328-L331",
    "source_section": "11. Event Principles > EVT-P05 — Replay Ready"
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
  "stable_id": "EVT-P05",
  "title": "Business Event hỗ trợ Replay nếu Policy cho phép",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-P06 — Business Event phải có khả năng: - Monitoring - Logging - Tracing - Auditing

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P06-AC001",
      "given": "an operational task within the scope of Business Event phải có khả năng: - Monitoring - Logging - Tracing - Auditing",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EVT-P06-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P06-AC002",
      "given": "an operational task within the scope of Business Event phải có khả năng: - Monitoring - Logging - Tracing - Auditing",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EVT-P06-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P06-AC003",
      "given": "an operational task within the scope of Business Event phải có khả năng: - Monitoring - Logging - Tracing - Auditing",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EVT-P06-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P06-AC004",
      "given": "an operational task within the scope of Business Event phải có khả năng: - Monitoring - Logging - Tracing - Auditing",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EVT-P06-O004"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EVT-P06-AC005",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Business Event phải có khả năng: - Monitoring - Logging - Tracing - Auditing",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EVT-P06-O001",
        "EVT-P06-O002",
        "EVT-P06-O003",
        "EVT-P06-O004"
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
        "EVT-P06-AC001",
        "EVT-P06-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P06-O001",
      "obligation_text": "Business Event phải có khả năng: Monitoring."
    },
    {
      "acceptance_criterion_references": [
        "EVT-P06-AC002",
        "EVT-P06-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P06-O002",
      "obligation_text": "Business Event phải có khả năng: Logging."
    },
    {
      "acceptance_criterion_references": [
        "EVT-P06-AC003",
        "EVT-P06-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P06-O003",
      "obligation_text": "Business Event phải có khả năng: Tracing."
    },
    {
      "acceptance_criterion_references": [
        "EVT-P06-AC004",
        "EVT-P06-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P06-O004",
      "obligation_text": "Business Event phải có khả năng: Auditing."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EVT-P06 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EVT-P06 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EVT-P06 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EVT-P06 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EVT-P06-AC001",
        "EVT-P06-AC002",
        "EVT-P06-AC003",
        "EVT-P06-AC004"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EVT-P06 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event phải có khả năng: - Monitoring - Logging - Tracing - Auditing",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-P06",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-P06 — Observable",
    "source_context_sha256": "8950d8b356ceb6a147cb9f81361cec4da0d60e0d64e9f4c1337562a3b2bf5407",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "6195dbf284a99e9537b04f3f1ed37ab826f7b023f0d2f77d3041dc7787d70c99",
    "source_lines": "L334-L342",
    "source_section": "11. Event Principles > EVT-P06 — Observable"
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
  "stable_id": "EVT-P06",
  "title": "Business Event phải có khả năng: - Monitoring - Logging - Tracing - Auditing",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-P07 — Business Event ưu tiên sử dụng Canonical Event Model. Không phụ thuộc Connector cụ thể

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EVT-P07-AC001",
      "given": "a contract interaction at the integration boundary defined by Business Event ưu tiên sử dụng Canonical Event Model. Không phụ thuộc Connector cụ thể",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EVT-P07-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EVT-P07-AC002",
      "given": "a contract interaction at the integration boundary defined by Business Event ưu tiên sử dụng Canonical Event Model. Không phụ thuộc Connector cụ thể",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EVT-P07-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "EVT-P07-AC003",
      "given": "an interaction that violates the contract or ownership boundary for Business Event ưu tiên sử dụng Canonical Event Model. Không phụ thuộc Connector cụ thể",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "EVT-P07-O001",
        "EVT-P07-O002"
      ],
      "when": "the interaction reaches the integration boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EVT-P07-AC001",
        "EVT-P07-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P07-O001",
      "obligation_text": "Business Event ưu tiên sử dụng Canonical Event Model"
    },
    {
      "acceptance_criterion_references": [
        "EVT-P07-AC002",
        "EVT-P07-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P07-O002",
      "obligation_text": "Không phụ thuộc Connector cụ thể"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event ưu tiên sử dụng Canonical Event Model. Không phụ thuộc Connector cụ thể.",
  "provenance": {
    "approved_decision_contracts": {
      "P2-DEC-006": {
        "decision_id": "P2-DEC-006",
        "sections": [
          {
            "heading": "Normative matrix",
            "items": [
              "External client to YSim API: Gateway required; Connector normally not required; Adapter required when contracts differ.",
              "Provider to YSim webhook: Gateway and Connector required; Adapter required when mapping is required.",
              "YSim to provider API: Connector and Adapter required; API Gateway not required.",
              "YSim to partner/customer webhook: delivery Connector and Adapter required; API Gateway not required.",
              "External asynchronous event/message: bridge/Connector and Adapter required; API Gateway not required.",
              "Batch/SFTP/file: Connector and Adapter required.",
              "Portal/Storefront/Web SDK to public YSim API: Gateway required; Connector/Adapter not required when the API is canonical.",
              "Internal domain API/event is not governed by the external Connector/Adapter matrix."
            ]
          },
          {
            "heading": "Additional invariants",
            "items": [
              "A Business Domain never connects directly to an external system.",
              "Gateway owns ingress policy, routing, limits, and observability and contains no business logic.",
              "Connector owns connectivity, authentication, protocol, retry, and provider health and contains no domain decisions.",
              "Adapter owns schema/semantic translation and contains no business logic.",
              "Provider-specific models must not leak into Business Domains.",
              "Direct browser/mobile-to-provider interaction is allowed only through an approved short-lived scoped token/session pattern; backend webhook/status remains authoritative.",
              "Production bypass is prohibited.",
              "An exception requires architecture/security review, expiry, and audit."
            ]
          }
        ],
        "selected_option": 1,
        "status": "DECIDED_PENDING_PACK_APPROVAL",
        "title": "External integration applicability matrix"
      }
    },
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-P07",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-P07 — Canonical",
    "source_context_sha256": "241a19fc09bbc88fecaeeb4bbd7584fefb0a4793293c032f7c502c818e8c34de",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "1c19075029422117e34501c5aa2b2bdd6a2a36333899ff276e02b11807424fc9",
    "source_lines": "L345-L350",
    "source_section": "11. Event Principles > EVT-P07 — Canonical"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EVT-P07",
  "title": "Business Event ưu tiên sử dụng Canonical Event Model. Không phụ thuộc Connector cụ thể",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EVT-P08 — Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P08-AC001",
      "given": "an operational task within the scope of Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EVT-P08-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P08-AC002",
      "given": "an operational task within the scope of Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EVT-P08-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P08-AC003",
      "given": "an operational task within the scope of Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EVT-P08-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P08-AC004",
      "given": "an operational task within the scope of Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EVT-P08-O004"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EVT-P08-AC005",
      "given": "an operational task within the scope of Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới …",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EVT-P08-O005"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EVT-P08-AC006",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới …",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EVT-P08-O001",
        "EVT-P08-O002",
        "EVT-P08-O003",
        "EVT-P08-O004",
        "EVT-P08-O005"
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
        "EVT-P08-AC001",
        "EVT-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P08-O001",
      "obligation_text": "Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới phải được: Architecture Review."
    },
    {
      "acceptance_criterion_references": [
        "EVT-P08-AC002",
        "EVT-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P08-O002",
      "obligation_text": "Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới phải được: Approval."
    },
    {
      "acceptance_criterion_references": [
        "EVT-P08-AC003",
        "EVT-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P08-O003",
      "obligation_text": "Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới phải được: Versioning."
    },
    {
      "acceptance_criterion_references": [
        "EVT-P08-AC004",
        "EVT-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P08-O004",
      "obligation_text": "Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới phải được: Audit."
    },
    {
      "acceptance_criterion_references": [
        "EVT-P08-AC005",
        "EVT-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EVT-P08-O005",
      "obligation_text": "Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới phải được: Traceability."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EVT-P08 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EVT-P08 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EVT-P08 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "EVT-P08 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EVT-P08-AC001",
        "EVT-P08-AC002",
        "EVT-P08-AC003",
        "EVT-P08-AC004",
        "EVT-P08-AC005"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EVT-P08 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới phải được: - Architecture Review - Approval - Versioning - Audit - Traceability",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "P2-DEC-002",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EVT-P08",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EVT-P08 — Enterprise Governance",
    "source_context_sha256": "97c279c78186c8c558b02a462b70bf32add02f453b40d0924e9580fec21f5008",
    "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
    "source_fingerprint": "880585e11b342cffe1e45a5b464a85a0f161c7d789991955e9f82a3c9f60c04c",
    "source_lines": "L353-L364",
    "source_section": "11. Event Principles > EVT-P08 — Enterprise Governance"
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
  "stable_id": "EVT-P08",
  "title": "Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới …",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
