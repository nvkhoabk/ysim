---
document_code: BRD-EVENT-INDEX
document_name: Enterprise Business Event Registry
project: YSim v2.0
document_set: BRD
version: 1.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
---

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