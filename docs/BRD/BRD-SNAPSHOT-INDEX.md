---
document_code: "BRD-SNAPSHOT-INDEX"
title: "Enterprise Snapshot Registry"
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

# Enterprise Snapshot Registry

## BRD-SNAPSHOT-INDEX

---

# 1. Purpose

Enterprise Snapshot Registry là tài liệu quản lý tập trung toàn bộ **Business Snapshot** của nền tảng YSim.

Business Snapshot là một bản ghi nghiệp vụ bất biến (**Immutable Business Record**) phản ánh trạng thái của một hoặc nhiều Business Object tại một thời điểm xác định.

Business Snapshot được sử dụng để:

- Settlement
- Audit
- Financial Evidence
- Analytics
- Reporting
- Compliance
- Historical Reconstruction
- Data Reconciliation

Enterprise Snapshot Registry là **Source of Truth** cho toàn bộ Snapshot của nền tảng.

---

# 2. Objectives

Snapshot Registry được xây dựng nhằm:

- Chuẩn hóa toàn bộ Business Snapshot.
- Chuẩn hóa Snapshot Lifecycle.
- Chuẩn hóa Snapshot Metadata.
- Chuẩn hóa Snapshot Governance.
- Chuẩn hóa Snapshot Retention.
- Chuẩn hóa Snapshot Versioning.
- Chuẩn hóa Snapshot Traceability.
- Chuẩn hóa Snapshot Visibility.

Snapshot Registry là nền tảng cho:

- Settlement Engine
- Financial Audit
- Reporting
- Analytics
- Compliance
- Data Recovery

---

# 3. Scope

Enterprise Snapshot Registry bao gồm toàn bộ Snapshot thuộc các Domain:

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
- Security
- Operations

Ngoài ra còn bao gồm:

- Cross Domain Snapshot
- Financial Snapshot
- Compliance Snapshot
- Historical Snapshot

---

# 4. Snapshot Classification

Business Snapshot được phân loại theo Type.

| Type | Description |
|------|-------------|
| Commercial | Snapshot thương mại |
| Financial | Snapshot tài chính |
| Order | Snapshot đơn hàng |
| Inventory | Snapshot tồn kho |
| Fulfillment | Snapshot giao hàng |
| Customer | Snapshot khách hàng |
| Configuration | Snapshot cấu hình |
| Analytics | Snapshot báo cáo |
| Security | Snapshot bảo mật |
| Operational | Snapshot vận hành |

Mỗi Snapshot chỉ có một Type chính.

---

# 5. Snapshot Purpose

Snapshot được tạo ra nhằm các mục đích khác nhau.

| Purpose | Description |
|----------|-------------|
| Settlement | Đối soát |
| Financial | Chứng từ tài chính |
| Audit | Kiểm toán |
| Reporting | Báo cáo |
| Analytics | Phân tích |
| Compliance | Tuân thủ |
| Historical Reconstruction | Khôi phục trạng thái nghiệp vụ |
| Evidence | Bằng chứng nghiệp vụ |

Một Snapshot có thể phục vụ nhiều Purpose.

---

# 6. Snapshot Lifecycle

Snapshot có Lifecycle riêng.

```text
Created
     │
     ▼
Frozen
     │
     ▼
Referenced
     │
     ▼
Archived
     │
     ▼
Purged
```

Nguyên tắc:

- Snapshot không Update.
- Snapshot không Merge.
- Snapshot không Rewrite.

Snapshot chỉ:

- Create
- Archive
- Purge (theo Retention Policy)

---

# 7. Snapshot Scope

Snapshot có thể thuộc các Scope:

```text
Platform

↓

Organization

↓

Storefront

↓

Customer
```

Visibility của Snapshot phụ thuộc:

- Permission
- Organization Relationship
- Security Policy
- Compliance Policy

---

# 8. Snapshot Identifier

Mỗi Snapshot được cấp một mã định danh duy nhất.

Quy ước:

```text
SNP-000001

SNP-000002

SNP-000003
```

Snapshot ID được sử dụng trong:

- BRD
- Settlement
- Audit
- Reporting
- Analytics
- Architecture Review

Snapshot ID là bất biến.

---

# 9. Snapshot Metadata

Mọi Snapshot nên có Metadata chuẩn.

| Metadata | Description |
|----------|-------------|
| Snapshot ID | Định danh Snapshot |
| Snapshot Type | Loại Snapshot |
| Source Business Object | Business Object nguồn |
| Trigger Event | Event tạo Snapshot |
| Snapshot Time | Thời điểm tạo |
| Organization ID | Organization |
| Tenant ID | Tenant |
| User ID | User (nếu có) |
| Version | Phiên bản |
| Visibility | Phạm vi truy cập |
| Retention Policy | Chính sách lưu trữ |
| Archive Status | Trạng thái lưu trữ |

Metadata giúp:

- Trace
- Audit
- Analytics
- Compliance
- Historical Reconstruction

---

# 10. Immutable Principle

Business Snapshot là bất biến.

Sau khi Snapshot được tạo:

- Không Update.
- Không Merge.
- Không Replace.
- Không Rewrite.

Nếu dữ liệu nghiệp vụ thay đổi:

Platform phải tạo Snapshot mới.

Không sửa Snapshot cũ.

---

# 11. Business Evidence Principle

Business Snapshot được xem là **Business Evidence**.

Business Snapshot không phải:

- Audit Log
- History Record
- Temporary Cache

Business Snapshot là bằng chứng nghiệp vụ tại một thời điểm xác định.

Ví dụ:

- Commercial Snapshot tại thời điểm thanh toán.
- Financial Snapshot tại thời điểm Settlement.
- Fulfillment Snapshot tại thời điểm giao QR.
- Configuration Snapshot tại thời điểm Publish.

Business Evidence là nền tảng phục vụ:

- Financial Audit
- Customer Dispute
- Settlement Verification
- Regulatory Compliance

---

# 12. Snapshot Retention

Snapshot tuân thủ Retention Policy.

Ví dụ:

| Snapshot Type | Default Retention |
|---------------|------------------|
| Commercial | 7 năm |
| Financial | 10 năm |
| Order | 5 năm |
| Fulfillment | 5 năm |
| Notification | 12 tháng |
| Analytics | Theo Policy |
| Configuration | Theo Version |

Retention có thể Override theo:

- Compliance
- Organization Policy
- Country Regulation

---

# 13. Snapshot Principles

## SNP-P01 — Immutable

Snapshot là bất biến.

---

## SNP-P02 — Business Evidence

Snapshot là bằng chứng nghiệp vụ.

---

## SNP-P03 — Versioned

Snapshot hỗ trợ Version.

---

## SNP-P04 — Event Driven

Snapshot được tạo từ Business Event.

---

## SNP-P05 — Traceable

Snapshot hỗ trợ Trace đầy đủ.

---

## SNP-P06 — Auditable

Snapshot hỗ trợ Audit.

---

## SNP-P07 — Policy Controlled

Snapshot chịu sự điều khiển của Retention Policy và Security Policy.

---

## SNP-P08 — Enterprise Governance

Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance.

Mọi Snapshot mới phải trải qua:

- Architecture Review
- Approval
- Versioning
- Traceability

---

# 14. Relationship to Other Documents

Enterprise Snapshot Registry có quan hệ với:

| Document | Relationship |
|----------|--------------|
| BRD Workshop | Xác định thời điểm tạo Snapshot |
| BRD-BO-INDEX | Snapshot của Business Object |
| BRD-CAP-INDEX | Capability tạo Snapshot |
| BRD-EVENT-INDEX | Event Trigger Snapshot |
| BRD-POLICY-INDEX | Policy điều khiển Snapshot |
| DMS | Snapshot Model |
| DBD | Snapshot Entity |
| SDD | Snapshot Architecture |
| CIP | Snapshot Implementation |

Enterprise Snapshot Registry là **Enterprise Snapshot Dictionary** và là tài liệu tham chiếu thống nhất cho toàn bộ nền tảng YSim.

------

# 15. Enterprise Snapshot Registry

## 15.1 Commercial Domain

| Snapshot ID | Snapshot | Type | Source Business Object | Trigger Event | Creation Strategy | Primary Purpose | Retention | Workshop |
|--------------|----------|------|------------------------|---------------|-------------------|-----------------|------------|----------|
| SNP-000001 | Commercial Snapshot | Commercial | Commercial Agreement | CommercialAgreementActivated | Event | Commercial Evidence | 7 Years | WS-05 |
| SNP-000002 | Price Book Snapshot | Commercial | Price Book | PriceBookPublished | Event | Pricing Audit | 7 Years | WS-05 |
| SNP-000003 | Promotion Snapshot | Commercial | Promotion | PromotionActivated | Event | Promotion Audit | 5 Years | WS-06 |
| SNP-000004 | Coupon Snapshot | Commercial | Coupon | CouponRedeemed | Event | Audit | 5 Years | WS-06 |

---

## 15.2 Order Domain

| Snapshot ID | Snapshot | Type | Source Business Object | Trigger Event | Creation Strategy | Primary Purpose | Retention | Workshop |
|--------------|----------|------|------------------------|---------------|-------------------|-----------------|------------|----------|
| SNP-010001 | Shopping Cart Snapshot | Order | Shopping Cart | CheckoutStarted | State Transition | Analytics | 12 Months | WS-07 |
| SNP-010002 | Checkout Snapshot | Order | Checkout Session | CheckoutCompleted | Event | Audit | 5 Years | WS-07 |
| SNP-010003 | Sales Order Snapshot | Order | Sales Order | SalesOrderCreated | Event | Order Evidence | 7 Years | WS-07 |
| SNP-010004 | Order Status Snapshot | Order | Sales Order | SalesOrderStatusChanged | State Transition | Historical Reconstruction | 7 Years | WS-07 |

---

## 15.3 Payment Domain

| Snapshot ID | Snapshot | Type | Source Business Object | Trigger Event | Creation Strategy | Primary Purpose | Retention | Workshop |
|--------------|----------|------|------------------------|---------------|-------------------|-----------------|------------|----------|
| SNP-020001 | Payment Snapshot | Financial | Payment | PaymentSucceeded | Event | Financial Evidence | 10 Years | WS-08 |
| SNP-020002 | Refund Snapshot | Financial | Refund | RefundCompleted | Event | Audit | 10 Years | WS-08 |
| SNP-020003 | Merchant Settlement Snapshot | Financial | Merchant Account | SettlementCompleted | Event | Settlement | 10 Years | WS-08 |

---

## 15.4 Inventory & Fulfillment Domain

| Snapshot ID | Snapshot | Type | Source Business Object | Trigger Event | Creation Strategy | Primary Purpose | Retention | Workshop |
|--------------|----------|------|------------------------|---------------|-------------------|-----------------|------------|----------|
| SNP-030001 | Inventory Snapshot | Inventory | Inventory | InventoryAllocated | Event | Allocation Evidence | 5 Years | WS-09 |
| SNP-030002 | Inventory Reservation Snapshot | Inventory | Inventory Reservation | InventoryReserved | Event | Audit | 5 Years | WS-09 |
| SNP-030003 | Fulfillment Snapshot | Fulfillment | Fulfillment Session | FulfillmentCompleted | Event | Fulfillment Evidence | 7 Years | WS-09 |
| SNP-030004 | QR Delivery Snapshot | Fulfillment | QR Distribution | QRDelivered | Event | Customer Dispute | 5 Years | WS-09 |

---

## 15.5 Financial & Settlement Domain

| Snapshot ID | Snapshot | Type | Source Business Object | Trigger Event | Creation Strategy | Primary Purpose | Retention | Workshop |
|--------------|----------|------|------------------------|---------------|-------------------|-----------------|------------|----------|
| SNP-040001 | Settlement Snapshot | Financial | Settlement | SettlementCompleted | Event | Settlement Evidence | 10 Years | WS-10 |
| SNP-040002 | Commission Snapshot | Financial | Commission | CommissionCalculated | Event | Commission Audit | 10 Years | WS-10 |
| SNP-040003 | Financial Ledger Snapshot | Financial | Ledger Entry | FinancialEventCreated | Event | Financial Audit | 10 Years | WS-10 |
| SNP-040004 | Wallet Snapshot | Financial | Wallet | WalletCredited | Event | Financial Evidence | 10 Years | WS-10 |

---

# 16. Snapshot Creation Strategy

YSim chuẩn hóa bốn chiến lược tạo Snapshot.

| Strategy | Description | Typical Examples |
|----------|-------------|------------------|
| Event Triggered | Snapshot được tạo ngay khi Business Event xảy ra | PaymentSucceeded, SettlementCompleted |
| State Transition | Snapshot được tạo khi Business Object chuyển trạng thái | Sales Order, Ticket |
| Scheduled | Snapshot được tạo theo lịch | Daily KPI, Monthly Financial Summary |
| Manual | Snapshot được tạo theo yêu cầu có thẩm quyền | Audit Investigation, Compliance Review |

Creation Strategy được xác định theo từng loại Snapshot.

---

# 17. Snapshot Visibility

Snapshot có Visibility riêng.

| Visibility | Description |
|------------|-------------|
| Internal | Chỉ YSim Internal |
| Organization | Organization được phép xem |
| Customer | Customer được xem |
| Compliance | Chỉ Compliance/Auditor |
| Financial | Chỉ Finance và Auditor |

Visibility được quyết định bởi:

- Security Policy
- Permission
- Organization Relationship
- Data Classification

---

# 18. Snapshot Version

Snapshot hỗ trợ Version.

Version được sử dụng khi:

- Snapshot Schema thay đổi.
- Business Structure thay đổi.
- Regulatory Requirement thay đổi.

Snapshot Content vẫn luôn bất biến.

Version không làm thay đổi Snapshot đã được tạo trước đó.

------

# 15.6 Customer Success Domain

| Snapshot ID | Snapshot | Type | Source Business Object | Trigger Event | Creation Strategy | Primary Purpose | Retention | Workshop |
|--------------|----------|------|------------------------|---------------|-------------------|-----------------|------------|----------|
| SNP-050001 | Ticket Snapshot | Customer | Ticket | TicketCreated | Event Triggered | Support Evidence | 5 Years | WS-11 |
| SNP-050002 | Ticket Resolution Snapshot | Customer | Ticket | TicketResolved | Event Triggered | Audit | 5 Years | WS-11 |
| SNP-050003 | Customer Feedback Snapshot | Customer | Customer Feedback | FeedbackSubmitted | Event Triggered | Analytics | 3 Years | WS-11 |
| SNP-050004 | Satisfaction Survey Snapshot | Customer | Satisfaction Survey | SurveyCompleted | Event Triggered | Customer Experience | 3 Years | WS-11 |

---

# 15.7 Communication Domain

| Snapshot ID | Snapshot | Type | Source Business Object | Trigger Event | Creation Strategy | Primary Purpose | Retention | Workshop |
|--------------|----------|------|------------------------|---------------|-------------------|-----------------|------------|----------|
| SNP-060001 | Notification Snapshot | Communication | Notification | NotificationDelivered | Event Triggered | Delivery Evidence | 12 Months | WS-12 |
| SNP-060002 | Communication Log Snapshot | Communication | Communication Log | NotificationCompleted | Event Triggered | Audit | 12 Months | WS-12 |
| SNP-060003 | Portal Announcement Snapshot | Communication | Portal Announcement | AnnouncementPublished | Event Triggered | Historical Reference | 12 Months | WS-12 |

---

# 15.8 Analytics & Reporting Domain

| Snapshot ID | Snapshot | Type | Source Business Object | Trigger Event | Creation Strategy | Primary Purpose | Retention | Workshop |
|--------------|----------|------|------------------------|---------------|-------------------|-----------------|------------|----------|
| SNP-070001 | Dashboard Snapshot | Analytics | Dashboard | DashboardGenerated | Scheduled | Historical Dashboard | Configurable | WS-13 |
| SNP-070002 | Report Snapshot | Analytics | Report | ReportGenerated | Event Triggered | Reporting | Configurable | WS-13 |
| SNP-070003 | KPI Snapshot | Analytics | KPI Definition | KPICalculated | Scheduled | KPI Analysis | Configurable | WS-13 |
| SNP-070004 | Alert Snapshot | Analytics | Alert Rule | AlertTriggered | Event Triggered | Audit | 3 Years | WS-13 |

---

# 15.9 Platform Configuration Domain

| Snapshot ID | Snapshot | Type | Source Business Object | Trigger Event | Creation Strategy | Primary Purpose | Retention | Workshop |
|--------------|----------|------|------------------------|---------------|-------------------|-----------------|------------|----------|
| SNP-080001 | Configuration Snapshot | Configuration | Configuration | ConfigurationPublished | Event Triggered | Configuration Recovery | Permanent | WS-14 |
| SNP-080002 | Reference Data Snapshot | Configuration | Reference Data | ReferenceDataChanged | Event Triggered | Historical Reference | Permanent | WS-14 |
| SNP-080003 | Business Rule Snapshot | Configuration | Business Rule | RulePublished | Event Triggered | Rule Audit | Permanent | WS-14 |
| SNP-080004 | Metadata Snapshot | Configuration | Metadata | MetadataPublished | Event Triggered | Metadata Recovery | Permanent | WS-14 |

---

# 15.10 Integration Domain

| Snapshot ID | Snapshot | Type | Source Business Object | Trigger Event | Creation Strategy | Primary Purpose | Retention | Workshop |
|--------------|----------|------|------------------------|---------------|-------------------|-----------------|------------|----------|
| SNP-090001 | Connector Snapshot | Integration | Connector | ConnectorActivated | Event Triggered | Integration Audit | 5 Years | WS-15 |
| SNP-090002 | Queue Snapshot | Integration | Queue Message | QueueMessageCompleted | Event Triggered | Replay | 90 Days | WS-15 |
| SNP-090003 | Callback Snapshot | Integration | Callback | CallbackReceived | Event Triggered | Audit | 3 Years | WS-15 |
| SNP-090004 | API Transaction Snapshot | Integration | API Transaction | APICompleted | Event Triggered | API Audit | 3 Years | WS-15 |

---

# 15.11 Security Domain

| Snapshot ID | Snapshot | Type | Source Business Object | Trigger Event | Creation Strategy | Primary Purpose | Retention | Workshop |
|--------------|----------|------|------------------------|---------------|-------------------|-----------------|------------|----------|
| SNP-100001 | Authentication Snapshot | Security | Session | UserAuthenticated | Event Triggered | Security Audit | 12 Months | WS-16 |
| SNP-100002 | Authorization Snapshot | Security | Permission | PermissionEvaluated | Event Triggered | Audit | 12 Months | WS-16 |
| SNP-100003 | Risk Assessment Snapshot | Security | Risk Rule | RiskDetected | Event Triggered | Investigation | 5 Years | WS-16 |
| SNP-100004 | Consent Snapshot | Security | Customer Consent | ConsentChanged | Event Triggered | GDPR Compliance | Configurable | WS-16 |

---

# 15.12 Platform Operations Domain

| Snapshot ID | Snapshot | Type | Source Business Object | Trigger Event | Creation Strategy | Primary Purpose | Retention | Workshop |
|--------------|----------|------|------------------------|---------------|-------------------|-----------------|------------|----------|
| SNP-110001 | Scheduler Snapshot | Operational | Scheduler Job | SchedulerTriggered | Event Triggered | Job Audit | 12 Months | WS-17 |
| SNP-110002 | Job Execution Snapshot | Operational | Job Execution | JobCompleted | Event Triggered | Replay | 12 Months | WS-17 |
| SNP-110003 | Monitoring Snapshot | Operational | Monitoring Profile | MonitoringCollected | Scheduled | Trend Analysis | Configurable | WS-17 |
| SNP-110004 | Maintenance Snapshot | Operational | Maintenance Window | MaintenanceCompleted | Event Triggered | Audit | 5 Years | WS-17 |

---

# 16. Snapshot Composition Principle

Business Snapshot không chỉ lưu Business Object.

Business Snapshot phải lưu toàn bộ **Business Context** cần thiết để có thể tái hiện chính xác quyết định nghiệp vụ tại thời điểm Snapshot được tạo.

Ví dụ:

```text
Payment Snapshot

├── Payment
├── Sales Order
├── Commercial Agreement
├── Price Book
├── Promotion
├── Exchange Rate
├── Currency
├── Tax
├── Fee
├── Organization
├── Storefront
├── Customer
├── Payment Gateway
├── Supplier
├── Localization
├── Policy Version
└── Business Rule Version
```

Sau này dù:

- Giá thay đổi
- Promotion thay đổi
- Configuration thay đổi
- Policy thay đổi

thì Snapshot vẫn phản ánh đúng trạng thái lịch sử.

---

# 17. Snapshot Visibility Matrix

| Snapshot Type | Platform | Organization | Customer | Auditor |
|---------------|:--------:|:------------:|:--------:|:-------:|
| Commercial | ✓ | ✓ | ✗ | ✓ |
| Financial | ✓ | ✓ | ✗ | ✓ |
| Order | ✓ | ✓ | ✓ | ✓ |
| Fulfillment | ✓ | ✓ | ✓ | ✓ |
| Customer Support | ✓ | ✓ | ✓ | ✓ |
| Notification | ✓ | ✓ | ✓ | ✗ |
| Configuration | ✓ | ✗ | ✗ | ✓ |
| Security | ✓ | ✗ | ✗ | ✓ |
| Operations | ✓ | ✗ | ✗ | ✓ |

Visibility thực tế còn phụ thuộc:

- Permission
- Security Policy
- Data Scope
- Organization Relationship

---

# 18. Snapshot Relationship

Snapshot có thể được tạo thành chuỗi theo Business Flow.

```text
Sales Order Snapshot
          │
          ▼
Payment Snapshot
          │
          ▼
Commercial Snapshot
          │
          ▼
Inventory Snapshot
          │
          ▼
Fulfillment Snapshot
          │
          ▼
Settlement Snapshot
          │
          ▼
Financial Ledger Snapshot
          │
          ▼
Analytics Snapshot
```

Mỗi Snapshot tham chiếu Snapshot trước đó thông qua Business Identity và Trace Metadata.

Snapshot không được cập nhật để phản ánh trạng thái mới.

Mỗi thay đổi nghiệp vụ quan trọng sẽ tạo ra một Snapshot mới.

------

# 19. Enterprise Snapshot Matrix

Business Snapshot là kết quả của Business Event và là bằng chứng nghiệp vụ phục vụ Audit, Settlement, Reporting và Analytics.

| Snapshot | Source Business Object | Trigger Event | Main Capability | Primary Purpose |
|-----------|------------------------|---------------|-----------------|-----------------|
| Commercial Snapshot | Commercial Agreement | PaymentSucceeded | Commercial Management | Commercial Evidence |
| Price Book Snapshot | Price Book | PriceBookPublished | Pricing Engine | Pricing Audit |
| Promotion Snapshot | Promotion | PromotionActivated | Promotion Management | Promotion Evidence |
| Sales Order Snapshot | Sales Order | SalesOrderCreated | Sales Order Management | Order Evidence |
| Payment Snapshot | Payment | PaymentSucceeded | Payment Management | Financial Evidence |
| Inventory Snapshot | Inventory Allocation | InventoryAllocated | Inventory Allocation | Inventory Evidence |
| Fulfillment Snapshot | Fulfillment Session | FulfillmentCompleted | Fulfillment Management | Fulfillment Evidence |
| Settlement Snapshot | Settlement | SettlementCompleted | Settlement Management | Settlement Evidence |
| Financial Ledger Snapshot | Ledger Entry | FinancialEventCreated | Financial Ledger | Financial Audit |
| Ticket Snapshot | Ticket | TicketCreated | Customer Support | Customer Support Evidence |
| Notification Snapshot | Notification | NotificationDelivered | Communication Management | Communication Evidence |
| Configuration Snapshot | Configuration | ConfigurationPublished | Configuration Management | Configuration Recovery |
| Authentication Snapshot | Session | UserAuthenticated | Authentication | Security Evidence |
| Scheduler Snapshot | Scheduler Job | SchedulerTriggered | Scheduler | Operational Evidence |

---

# 20. Snapshot Relationship

Business Snapshot được hình thành từ Business Event.

```text
Business Object
        │
        ▼
Business Event
        │
        ▼
Business Snapshot
        │
        ▼
Reporting
        │
        ▼
Analytics
```

Snapshot có thể được nhiều hệ thống sử dụng lại mà không cần đọc dữ liệu Runtime.

---

# 21. Snapshot vs Event vs Audit vs History

Đây là bốn khái niệm khác nhau.

| Concept | Purpose | Mutable | Business Meaning |
|----------|---------|:-------:|------------------|
| Business Event | Một sự kiện đã xảy ra | No | Business Fact |
| Business Snapshot | Trạng thái nghiệp vụ tại thời điểm xác định | No | Business Evidence |
| Audit Log | Nhật ký thao tác | No | Operational Evidence |
| History | Lịch sử thay đổi dữ liệu | Yes | Data History |

Ví dụ:

| Situation | Correct Artifact |
|------------|------------------|
| Payment thành công | Business Event |
| Thông tin giao dịch tại thời điểm thanh toán | Payment Snapshot |
| Admin thay đổi Payment Policy | Audit Log |
| Price Book thay đổi nhiều lần | History |

Nguyên tắc:

- Event không thay thế Snapshot.
- Snapshot không thay thế Audit.
- Audit không thay thế History.
- History không phải Business Evidence.

---

# 22. Snapshot Traceability

Mỗi Snapshot phải có khả năng truy vết tới:

- Business Requirement
- Business Capability
- Business Object
- Business Policy
- Business Rule
- Business Event
- API Transaction
- Queue Message
- Integration Transaction
- Test Case

Ví dụ:

| Snapshot | Traceability |
|-----------|--------------|
| Payment Snapshot | BRD → Payment → Policy → Rule → Event → API → Queue → Snapshot |
| Settlement Snapshot | BRD → Settlement → Ledger → Event → Snapshot |
| Fulfillment Snapshot | BRD → Fulfillment → QR Delivery → Event → Snapshot |

---

# 23. Snapshot Governance

Snapshot chịu sự quản trị tập trung.

Mọi Snapshot mới phải có:

- Snapshot ID
- Source Business Object
- Trigger Event
- Snapshot Type
- Version
- Retention Policy
- Visibility
- Owner
- Approval

Snapshot chỉ được tạo khi có Business Requirement rõ ràng.

Không tạo Snapshot chỉ để phục vụ mục đích kỹ thuật.

---

# 24. Snapshot Statistics

## 24.1 Statistics by Domain

| Domain | Estimated Snapshots |
|---------|--------------------:|
| Commercial | 4 |
| Order | 4 |
| Payment | 3 |
| Inventory & Fulfillment | 4 |
| Settlement | 4 |
| Customer Success | 4 |
| Communication | 3 |
| Analytics | 4 |
| Configuration | 4 |
| Integration | 4 |
| Security | 4 |
| Operations | 4 |

---

## 24.2 Statistics by Purpose

| Purpose | Estimated Snapshots |
|----------|--------------------:|
| Settlement | 8+ |
| Financial Audit | 8+ |
| Reporting | 10+ |
| Analytics | 10+ |
| Compliance | 6+ |
| Historical Reconstruction | 8+ |
| Operational Evidence | 6+ |

---

## 24.3 Total

Tổng số Snapshot hiện tại:

**Khoảng 60–80 Business Snapshots**

Số lượng Snapshot sẽ tăng theo từng phiên bản nhưng Snapshot ID hiện có không thay đổi.

---

# 25. Enterprise Snapshot Principles

## SNP-EP-001

Snapshot là Business Evidence.

---

## SNP-EP-002

Snapshot là Immutable.

---

## SNP-EP-003

Snapshot được tạo từ Business Event hoặc Business State Transition.

---

## SNP-EP-004

Snapshot phải chứa đầy đủ Business Context để tái hiện quyết định nghiệp vụ.

---

## SNP-EP-005

Snapshot độc lập với Runtime Database.

---

## SNP-EP-006

Snapshot hỗ trợ Versioning.

---

## SNP-EP-007

Snapshot chịu sự điều khiển của Security Policy và Retention Policy.

---

## SNP-EP-008

Snapshot hỗ trợ Audit và Regulatory Compliance.

---

## SNP-EP-009

Snapshot là nguồn dữ liệu ưu tiên cho Reporting, Analytics và Settlement.

---

## SNP-EP-010

Enterprise Snapshot Registry là Enterprise Snapshot Dictionary của nền tảng YSim.

---

# 26. Relationship to Enterprise Registries

Enterprise Snapshot Registry là một phần của Enterprise Registry Layer.

| Registry | Purpose |
|----------|---------|
| BRD-BO-INDEX | Business Object Registry |
| BRD-CAP-INDEX | Business Capability Registry |
| BRD-EVENT-INDEX | Business Event Registry |
| BRD-POLICY-INDEX | Enterprise Policy Registry |
| BRD-SNAPSHOT-INDEX | Enterprise Snapshot Registry |

Năm Registry này tạo thành **Enterprise Business Meta Model** thống nhất của nền tảng YSim.

---

# 27. Document Status

**Status: FROZEN**

Enterprise Snapshot Registry là tài liệu nền tảng quản lý toàn bộ Business Snapshot của nền tảng YSim.

Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua:

- Business Review
- Architecture Review
- Approval
- Versioning
- Security Review
- Audit
- Traceability

trước khi được sử dụng trong Platform.

---

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R001 — Mỗi Snapshot được cấp một mã định danh duy nhất

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R001-AC001",
      "given": "a candidate Mỗi Snapshot được cấp một mã định danh duy nhất record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R001-O001"
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
        "BRD-SNAPSHOT-INDEX-R001-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R001-O001",
      "obligation_text": "Mỗi Snapshot được cấp một mã định danh duy nhất"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Snapshot được cấp một mã định danh duy nhất.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-001",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Snapshot Identifier",
    "source_context_sha256": "8dcb0835c4ec9f25efbd4e09dbf5cf84db0db5f565e30c97c0e2b719da3e78b1",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "41f37cccd07fa8865723025b53240edeba8bb89c1e518931d727872f117c4a5d",
    "source_lines": "L196",
    "source_section": "8. Snapshot Identifier"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R001",
  "title": "Mỗi Snapshot được cấp một mã định danh duy nhất",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R002 — Nếu dữ liệu nghiệp vụ thay đổi: Platform phải tạo Snapshot mới

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R002-AC001",
      "given": "a candidate Nếu dữ liệu nghiệp vụ thay đổi: Platform phải tạo Snapshot mới record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R002-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R002-AC002",
      "given": "a Nếu dữ liệu nghiệp vụ thay đổi: Platform phải tạo Snapshot mới candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R002-O001"
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
        "BRD-SNAPSHOT-INDEX-R002-AC001",
        "BRD-SNAPSHOT-INDEX-R002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R002-O001",
      "obligation_text": "Nếu dữ liệu nghiệp vụ thay đổi: Platform phải tạo Snapshot mới"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu dữ liệu nghiệp vụ thay đổi: Platform phải tạo Snapshot mới.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-002",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Immutable Principle",
    "source_context_sha256": "514f52a4bf9b723e0c71a97e83b50f2b220fd282c5bd267f77a6ad52ca1d9910",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
    "source_lines": "L261-L263",
    "source_section": "10. Immutable Principle"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R002",
  "title": "Nếu dữ liệu nghiệp vụ thay đổi: Platform phải tạo Snapshot mới",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R003 — Business Snapshot không phải: - Audit Log

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R003-AC001",
      "given": "an operational task within the scope of Business Snapshot không phải: - Audit Log",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R003-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R003-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Business Snapshot không phải: - Audit Log",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R003-O001"
      ],
      "when": "operational verification is performed"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R003-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Business Snapshot không phải: - Audit Log",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R003-O001"
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
        "BRD-SNAPSHOT-INDEX-R003-AC001",
        "BRD-SNAPSHOT-INDEX-R003-AC002",
        "BRD-SNAPSHOT-INDEX-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R003-O001",
      "obligation_text": "Business Snapshot không phải: - Audit Log"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R003 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R003-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Snapshot không phải: - Audit Log",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-003",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Business Evidence Principle",
    "source_context_sha256": "390418eb19985a215320f63bad6bc942609c40765a9d243f8b32c548712c6500",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "d329bff77b71dccf548a57f9ecc262634d8a7e035bad170339dd5d624bc4e759",
    "source_lines": "L273-L275",
    "source_section": "11. Business Evidence Principle"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R003",
  "title": "Business Snapshot không phải: - Audit Log",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R004 — Business Snapshot không phải: - History Record

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R004-AC001",
      "given": "a candidate Business Snapshot không phải: - History Record record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns REJECTED when the prohibited value or relationship is present, and no rejected state is persisted",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R004-O001"
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
        "BRD-SNAPSHOT-INDEX-R004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R004-O001",
      "obligation_text": "Business Snapshot không phải: - History Record"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Snapshot không phải: - History Record",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-004",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Business Evidence Principle",
    "source_context_sha256": "390418eb19985a215320f63bad6bc942609c40765a9d243f8b32c548712c6500",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "d0dbda4269278322728b2a2021c57f63f56f0c14916bc18072fe262820bde811",
    "source_lines": "L273-L276",
    "source_section": "11. Business Evidence Principle"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R004",
  "title": "Business Snapshot không phải: - History Record",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R005 — Business Snapshot không phải: - Temporary Cache

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R005-AC001",
      "given": "a candidate Business Snapshot không phải: - Temporary Cache record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns REJECTED when the prohibited value or relationship is present, and no rejected state is persisted",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R005-O001"
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
        "BRD-SNAPSHOT-INDEX-R005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R005-O001",
      "obligation_text": "Business Snapshot không phải: - Temporary Cache"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Snapshot không phải: - Temporary Cache",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-005",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Business Evidence Principle",
    "source_context_sha256": "390418eb19985a215320f63bad6bc942609c40765a9d243f8b32c548712c6500",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "345cec95fa56693d7dd5474d25b4b5b95c7b1d1168ec6e5c5d794621c0f43515",
    "source_lines": "L273-L277",
    "source_section": "11. Business Evidence Principle"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R005",
  "title": "Business Snapshot không phải: - Temporary Cache",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R006 — Snapshot tuân thủ Retention Policy

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R006-AC001",
      "given": "a candidate Snapshot tuân thủ Retention Policy record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R006-O001"
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
        "BRD-SNAPSHOT-INDEX-R006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R006-O001",
      "obligation_text": "Snapshot tuân thủ Retention Policy"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot tuân thủ Retention Policy.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-006",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Snapshot Retention",
    "source_context_sha256": "7e3c42acb5cefb9022dc9845a2b659e22bb4b493c9c7b835055a6890544c9443",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "29cb7f87f924a5756aa901510eb95bc5dff237fe268da955b5c1347acce27176",
    "source_lines": "L299",
    "source_section": "12. Snapshot Retention"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R006",
  "title": "Snapshot tuân thủ Retention Policy",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R007 — Snapshot Content vẫn luôn bất biến

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R007-AC001",
      "given": "a candidate Snapshot Content vẫn luôn bất biến record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R007-O001"
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
        "BRD-SNAPSHOT-INDEX-R007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R007-O001",
      "obligation_text": "Snapshot Content vẫn luôn bất biến"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot Content vẫn luôn bất biến.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-007",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Snapshot Version",
    "source_context_sha256": "3740076553a35d4da15770d92202901baf1c645a1a062074c1aaafa2e51081f8",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
    "source_lines": "L500",
    "source_section": "18. Snapshot Version"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R007",
  "title": "Snapshot Content vẫn luôn bất biến",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R008 — Business Snapshot phải lưu toàn bộ **Business Context** cần thiết để có thể tái hiện chính xác q…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R008-AC001",
      "given": "a candidate Business Snapshot phải lưu toàn bộ **Business Context** cần thiết để có thể tái hiện chính xác q… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "the accepted record contains the field named by the obligation, preserves its submitted attribution, and exposes that stored value when the record is inspected",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R008-O001"
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
        "BRD-SNAPSHOT-INDEX-R008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R008-O001",
      "obligation_text": "Business Snapshot phải lưu toàn bộ **Business Context** cần thiết để có thể tái hiện chính xác quyết định nghiệp vụ tại thời điểm Snapshot được tạo"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Snapshot phải lưu toàn bộ **Business Context** cần thiết để có thể tái hiện chính xác quyết định nghiệp vụ tại thời điểm Snapshot được tạo.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-008",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Snapshot Composition Principle",
    "source_context_sha256": "b845b8ad2b61ab8dfa787bdf242f43c538eaffbbf997f6914a7160574bfc110e",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
    "source_lines": "L586",
    "source_section": "16. Snapshot Composition Principle"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R008",
  "title": "Business Snapshot phải lưu toàn bộ **Business Context** cần thiết để có thể tái hiện chính xác q…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R009 — Snapshot không được cập nhật để phản ánh trạng thái mới

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R009-AC001",
      "given": "a candidate Snapshot không được cập nhật để phản ánh trạng thái mới record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns REJECTED when the prohibited value or relationship is present, and no rejected state is persisted",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R009-O001"
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
        "BRD-SNAPSHOT-INDEX-R009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R009-O001",
      "obligation_text": "Snapshot không được cập nhật để phản ánh trạng thái mới"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot không được cập nhật để phản ánh trạng thái mới.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-009",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Snapshot Relationship",
    "source_context_sha256": "81526bbe525e34ef718b513e9db39a758cf3dcdcafe59000f27d0d000d2553aa",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "86a0e9f3fb3692208b23b8cd27161d70b3389ea85bc0444a5de9939ba7f4c83c",
    "source_lines": "L677",
    "source_section": "18. Snapshot Relationship"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R009",
  "title": "Snapshot không được cập nhật để phản ánh trạng thái mới",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R010 — Snapshot có thể được nhiều hệ thống sử dụng lại mà không cần đọc dữ liệu Runtime

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R010-AC001",
      "given": "a candidate Snapshot có thể được nhiều hệ thống sử dụng lại mà không cần đọc dữ liệu Runtime record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R010-O001"
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
        "BRD-SNAPSHOT-INDEX-R010-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R010-O001",
      "obligation_text": "Snapshot có thể được nhiều hệ thống sử dụng lại mà không cần đọc dữ liệu Runtime"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot có thể được nhiều hệ thống sử dụng lại mà không cần đọc dữ liệu Runtime.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-010",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Snapshot Relationship",
    "source_context_sha256": "99049378b18d84b9b04ce87e4567d1065229649c9953ea486459e23df7c3250d",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
    "source_lines": "L726",
    "source_section": "20. Snapshot Relationship"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R010",
  "title": "Snapshot có thể được nhiều hệ thống sử dụng lại mà không cần đọc dữ liệu Runtime",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R022 — Mọi Snapshot mới phải có: - Snapshot ID

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R022-AC001",
      "given": "a candidate Mọi Snapshot mới phải có: - Snapshot ID record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R022-O001"
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
        "BRD-SNAPSHOT-INDEX-R022-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R022-O001",
      "obligation_text": "Mọi Snapshot mới phải có: - Snapshot ID"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới phải có: - Snapshot ID",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-022",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Snapshot Governance",
    "source_context_sha256": "4e01ef7cf97fffd270369a5bba2b860d977cdc58934c032a88d79217d8428c04",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "d79abaeb6233657c4b6738aba199591cc2a7c9eaa210f57b5fd9d4ce7150aa74",
    "source_lines": "L788-L790",
    "source_section": "23. Snapshot Governance"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R022",
  "title": "Mọi Snapshot mới phải có: - Snapshot ID",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R023 — Mọi Snapshot mới phải có: - Source Business Object

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R023-AC001",
      "given": "a candidate Mọi Snapshot mới phải có: - Source Business Object record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R023-O001"
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
        "BRD-SNAPSHOT-INDEX-R023-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R023-O001",
      "obligation_text": "Mọi Snapshot mới phải có: - Source Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới phải có: - Source Business Object",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-023",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Snapshot Governance",
    "source_context_sha256": "4e01ef7cf97fffd270369a5bba2b860d977cdc58934c032a88d79217d8428c04",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "d487d2dcfef67df8ac19673d7a2ba39896eb324745718bc2a422018e88a93947",
    "source_lines": "L788-L791",
    "source_section": "23. Snapshot Governance"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R023",
  "title": "Mọi Snapshot mới phải có: - Source Business Object",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R024 — Mọi Snapshot mới phải có: - Trigger Event

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R024-AC001",
      "given": "a candidate Mọi Snapshot mới phải có: - Trigger Event record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R024-O001"
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
        "BRD-SNAPSHOT-INDEX-R024-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R024-O001",
      "obligation_text": "Mọi Snapshot mới phải có: - Trigger Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới phải có: - Trigger Event",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-024",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Snapshot Governance",
    "source_context_sha256": "4e01ef7cf97fffd270369a5bba2b860d977cdc58934c032a88d79217d8428c04",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "72433ef307ab5f5623192e7958768d393262d98cb0ff1b8cb415d5dedf7a0051",
    "source_lines": "L788-L792",
    "source_section": "23. Snapshot Governance"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R024",
  "title": "Mọi Snapshot mới phải có: - Trigger Event",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R025 — Mọi Snapshot mới phải có: - Snapshot Type

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R025-AC001",
      "given": "a candidate Mọi Snapshot mới phải có: - Snapshot Type record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R025-O001"
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
        "BRD-SNAPSHOT-INDEX-R025-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R025-O001",
      "obligation_text": "Mọi Snapshot mới phải có: - Snapshot Type"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới phải có: - Snapshot Type",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-025",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Snapshot Governance",
    "source_context_sha256": "4e01ef7cf97fffd270369a5bba2b860d977cdc58934c032a88d79217d8428c04",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "c22a0f867ac71cd886318b194342707ebd776566bcd54431ef71657fa0fab54a",
    "source_lines": "L788-L793",
    "source_section": "23. Snapshot Governance"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R025",
  "title": "Mọi Snapshot mới phải có: - Snapshot Type",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R026 — Mọi Snapshot mới phải có: - Version

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R026-AC001",
      "given": "a candidate Mọi Snapshot mới phải có: - Version record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R026-O001"
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
        "BRD-SNAPSHOT-INDEX-R026-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R026-O001",
      "obligation_text": "Mọi Snapshot mới phải có: - Version"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới phải có: - Version",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-026",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Snapshot Governance",
    "source_context_sha256": "4e01ef7cf97fffd270369a5bba2b860d977cdc58934c032a88d79217d8428c04",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "f5deac80f9174ce98ac190b51aee6f445a03bbe1148451b2bd573f330957f935",
    "source_lines": "L788-L794",
    "source_section": "23. Snapshot Governance"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R026",
  "title": "Mọi Snapshot mới phải có: - Version",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R027 — Mọi Snapshot mới phải có: - Retention Policy

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R027-AC001",
      "given": "a candidate Mọi Snapshot mới phải có: - Retention Policy record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R027-O001"
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
        "BRD-SNAPSHOT-INDEX-R027-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R027-O001",
      "obligation_text": "Mọi Snapshot mới phải có: - Retention Policy"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới phải có: - Retention Policy",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-027",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-027",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Snapshot Governance",
    "source_context_sha256": "4e01ef7cf97fffd270369a5bba2b860d977cdc58934c032a88d79217d8428c04",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "9f99534c05a0aca0613d80c7b883c85920d1c36e5a43b043ba94c518bfad7eea",
    "source_lines": "L788-L795",
    "source_section": "23. Snapshot Governance"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R027",
  "title": "Mọi Snapshot mới phải có: - Retention Policy",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R028 — Mọi Snapshot mới phải có: - Visibility

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R028-AC001",
      "given": "a candidate Mọi Snapshot mới phải có: - Visibility record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R028-O001"
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
        "BRD-SNAPSHOT-INDEX-R028-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R028-O001",
      "obligation_text": "Mọi Snapshot mới phải có: - Visibility"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới phải có: - Visibility",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-028",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-028",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Snapshot Governance",
    "source_context_sha256": "4e01ef7cf97fffd270369a5bba2b860d977cdc58934c032a88d79217d8428c04",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "031107b8fa1286afbc468d065fff4bb3dfb9e8ae9dc4ef6b23c5b6fe1040bc88",
    "source_lines": "L788-L796",
    "source_section": "23. Snapshot Governance"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R028",
  "title": "Mọi Snapshot mới phải có: - Visibility",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R029 — Mọi Snapshot mới phải có: - Owner

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R029-AC001",
      "given": "a candidate Mọi Snapshot mới phải có: - Owner record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R029-O001"
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
        "BRD-SNAPSHOT-INDEX-R029-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R029-O001",
      "obligation_text": "Mọi Snapshot mới phải có: - Owner"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới phải có: - Owner",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-029",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-029",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Snapshot Governance",
    "source_context_sha256": "4e01ef7cf97fffd270369a5bba2b860d977cdc58934c032a88d79217d8428c04",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "3b07a28940a2564893c319192f2d7c2feb4c8d4874d1c00cfcb0efc80bbedb7b",
    "source_lines": "L788-L797",
    "source_section": "23. Snapshot Governance"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R029",
  "title": "Mọi Snapshot mới phải có: - Owner",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R030 — Mọi Snapshot mới phải có: - Approval

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R030-AC001",
      "given": "the applicable business context, actor, and input for Mọi Snapshot mới phải có: - Approval",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R030-O001"
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
        "BRD-SNAPSHOT-INDEX-R030-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R030-O001",
      "obligation_text": "Mọi Snapshot mới phải có: - Approval"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới phải có: - Approval",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-030",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-030",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Snapshot Governance",
    "source_context_sha256": "4e01ef7cf97fffd270369a5bba2b860d977cdc58934c032a88d79217d8428c04",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "054e4cf7b3ca340772f181f273e42e3555c1af6936b22f3acbd581d60c837e1b",
    "source_lines": "L788-L798",
    "source_section": "23. Snapshot Governance"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R030",
  "title": "Mọi Snapshot mới phải có: - Approval",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R031 — Snapshot chỉ được tạo khi có Business Requirement rõ ràng

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R031-AC001",
      "given": "a candidate Snapshot chỉ được tạo khi có Business Requirement rõ ràng record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R031-O001"
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
        "BRD-SNAPSHOT-INDEX-R031-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R031-O001",
      "obligation_text": "Snapshot chỉ được tạo khi có Business Requirement rõ ràng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot chỉ được tạo khi có Business Requirement rõ ràng.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-031",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-031",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Snapshot Governance",
    "source_context_sha256": "4e01ef7cf97fffd270369a5bba2b860d977cdc58934c032a88d79217d8428c04",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "c76f97bfbaad890f76cec8779dd7c9f5a2398fabafa5c0f9d895a76f5dea066d",
    "source_lines": "L800",
    "source_section": "23. Snapshot Governance"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R031",
  "title": "Snapshot chỉ được tạo khi có Business Requirement rõ ràng",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R032 — Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Business Review

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R032-AC001",
      "given": "a candidate Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Business Review record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R032-O001"
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
        "BRD-SNAPSHOT-INDEX-R032-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R032-O001",
      "obligation_text": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Business Review"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Business Review",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-032",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-032",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Document Status",
    "source_context_sha256": "98965dda7c28f27757b88183c2b5b4f260b78247893888c0f78db1c33286e1c7",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "51df16604a41f2f91fcc16aa188f7e3168b80466074cf44bc7d6273557ee1516",
    "source_lines": "L935-L937",
    "source_section": "27. Document Status"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R032",
  "title": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Business Review",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R033 — Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Architecture Review

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R033-AC001",
      "given": "a candidate Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Architecture Review record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R033-O001"
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
        "BRD-SNAPSHOT-INDEX-R033-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R033-O001",
      "obligation_text": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Architecture Review"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Architecture Review",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-033",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-033",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Document Status",
    "source_context_sha256": "98965dda7c28f27757b88183c2b5b4f260b78247893888c0f78db1c33286e1c7",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "f92e4189cdd61a69bf91d55bba7296dce174c8d933e39c4086776faff1bd4b2d",
    "source_lines": "L935-L938",
    "source_section": "27. Document Status"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R033",
  "title": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Architecture Review",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R034 — Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Approval

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R034-AC001",
      "given": "the applicable business context, actor, and input for Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Approval",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R034-O001"
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
        "BRD-SNAPSHOT-INDEX-R034-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R034-O001",
      "obligation_text": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Approval"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Approval",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-034",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-034",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Document Status",
    "source_context_sha256": "98965dda7c28f27757b88183c2b5b4f260b78247893888c0f78db1c33286e1c7",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "63d01a30e3fc15af396d98ce695e9aeabbb907b918a760e6b4ad6a87bf1bda35",
    "source_lines": "L935-L939",
    "source_section": "27. Document Status"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R034",
  "title": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Approval",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R035 — Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Versioning

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R035-AC001",
      "given": "a candidate Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Versioning record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R035-O001"
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
        "BRD-SNAPSHOT-INDEX-R035-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R035-O001",
      "obligation_text": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Versioning"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Versioning",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-035",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-035",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Document Status",
    "source_context_sha256": "98965dda7c28f27757b88183c2b5b4f260b78247893888c0f78db1c33286e1c7",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "d8120d316e5f2d93b46a1f45d7ead015d34f6ff374060671e8be247a22803a62",
    "source_lines": "L935-L940",
    "source_section": "27. Document Status"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R035",
  "title": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Versioning",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R036 — Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Security Review

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R036-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Security Review",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R036-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R036-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Security Review",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R036-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R036-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Security Review",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R036-O001"
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
        "BRD-SNAPSHOT-INDEX-R036-AC001",
        "BRD-SNAPSHOT-INDEX-R036-AC002",
        "BRD-SNAPSHOT-INDEX-R036-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R036-O001",
      "obligation_text": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Security Review"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R036 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R036 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R036 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R036-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R036-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R036 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Security Review",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-036",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-036",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Document Status",
    "source_context_sha256": "98965dda7c28f27757b88183c2b5b4f260b78247893888c0f78db1c33286e1c7",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "e7b09b745721a38aea7ca1aa94d219880311ea1b5aa116d40f3b33c21eec32a5",
    "source_lines": "L935-L941",
    "source_section": "27. Document Status"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-SNAPSHOT-INDEX-R036",
  "title": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Security Review",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R037 — Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R037-AC001",
      "given": "an operational task within the scope of Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R037-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R037-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R037-O001"
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
        "BRD-SNAPSHOT-INDEX-R037-AC001",
        "BRD-SNAPSHOT-INDEX-R037-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R037-O001",
      "obligation_text": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R037 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R037 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R037 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R037 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R037-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R037 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Audit",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-037",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-037",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Document Status",
    "source_context_sha256": "98965dda7c28f27757b88183c2b5b4f260b78247893888c0f78db1c33286e1c7",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "ca2315476b08391456cbfe13bb7ad78555b5da1d74ddadf1191df10c53ae1100",
    "source_lines": "L935-L942",
    "source_section": "27. Document Status"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R037",
  "title": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R038 — Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Traceability

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R038-AC001",
      "given": "a candidate Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Traceability record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R038-O001"
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
        "BRD-SNAPSHOT-INDEX-R038-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R038-O001",
      "obligation_text": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Traceability"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Traceability",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-038",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-038",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Document Status",
    "source_context_sha256": "98965dda7c28f27757b88183c2b5b4f260b78247893888c0f78db1c33286e1c7",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "96aefb76ce032287bcf2a08467b0e267a1425562690f068abb77fec914e4fd2e",
    "source_lines": "L935-L943",
    "source_section": "27. Document Status"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R038",
  "title": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Traceability",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R039 — Nguyên tắc: - Event không thay thế Snapshot

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R039-AC001",
      "given": "a candidate Nguyên tắc: - Event không thay thế Snapshot record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R039-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R039-AC002",
      "given": "a Nguyên tắc: - Event không thay thế Snapshot candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R039-O001"
      ],
      "when": "the candidate is validated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R039-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Nguyên tắc: - Event không thay thế Snapshot",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R039-O001"
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
        "BRD-SNAPSHOT-INDEX-R039-AC001",
        "BRD-SNAPSHOT-INDEX-R039-AC002",
        "BRD-SNAPSHOT-INDEX-R039-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R039-O001",
      "obligation_text": "Nguyên tắc: - Event không thay thế Snapshot"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R039 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R039 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R039 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R039-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R039-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R039 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Event không thay thế Snapshot.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-SNAPSHOT-INDEX-011"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-039",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-039",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Snapshot Lifecycle",
    "source_context_sha256": "4a5c772c53fafe9d0340da8bbec9c9925eda952c6f91fabad0c558818d8abb09",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
    "source_lines": "L750-L755",
    "source_section": "21. Snapshot vs Event vs Audit vs History"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R039",
  "title": "Nguyên tắc: - Event không thay thế Snapshot",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R040 — Nguyên tắc: - Snapshot không thay thế Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R040-AC001",
      "given": "an operational task within the scope of Nguyên tắc: - Snapshot không thay thế Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R040-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R040-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Nguyên tắc: - Snapshot không thay thế Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R040-O001"
      ],
      "when": "operational verification is performed"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R040-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Nguyên tắc: - Snapshot không thay thế Audit",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R040-O001"
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
        "BRD-SNAPSHOT-INDEX-R040-AC001",
        "BRD-SNAPSHOT-INDEX-R040-AC002",
        "BRD-SNAPSHOT-INDEX-R040-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R040-O001",
      "obligation_text": "Nguyên tắc: - Snapshot không thay thế Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R040 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R040 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R040 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R040-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R040-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R040 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Snapshot không thay thế Audit.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-SNAPSHOT-INDEX-011"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-040",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-040",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Snapshot Lifecycle",
    "source_context_sha256": "4a5c772c53fafe9d0340da8bbec9c9925eda952c6f91fabad0c558818d8abb09",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
    "source_lines": "L750-L755",
    "source_section": "21. Snapshot vs Event vs Audit vs History"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R040",
  "title": "Nguyên tắc: - Snapshot không thay thế Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R041 — Nguyên tắc: - Audit không thay thế History

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R041-AC001",
      "given": "an operational task within the scope of Nguyên tắc: - Audit không thay thế History",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R041-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R041-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Nguyên tắc: - Audit không thay thế History",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R041-O001"
      ],
      "when": "operational verification is performed"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R041-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Nguyên tắc: - Audit không thay thế History",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R041-O001"
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
        "BRD-SNAPSHOT-INDEX-R041-AC001",
        "BRD-SNAPSHOT-INDEX-R041-AC002",
        "BRD-SNAPSHOT-INDEX-R041-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R041-O001",
      "obligation_text": "Nguyên tắc: - Audit không thay thế History"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R041 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R041 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R041 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R041-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R041-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R041 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - Audit không thay thế History.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-SNAPSHOT-INDEX-011"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-041",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-041",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Snapshot Lifecycle",
    "source_context_sha256": "4a5c772c53fafe9d0340da8bbec9c9925eda952c6f91fabad0c558818d8abb09",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
    "source_lines": "L750-L755",
    "source_section": "21. Snapshot vs Event vs Audit vs History"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R041",
  "title": "Nguyên tắc: - Audit không thay thế History",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R042 — Nguyên tắc: - History không phải Business Evidence

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R042-AC001",
      "given": "the applicable business context, actor, and input for Nguyên tắc: - History không phải Business Evidence",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R042-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R042-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Nguyên tắc: - History không phải Business Evidence",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R042-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-SNAPSHOT-INDEX-R042-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Nguyên tắc: - History không phải Business Evidence",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-SNAPSHOT-INDEX-R042-O001"
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
        "BRD-SNAPSHOT-INDEX-R042-AC001",
        "BRD-SNAPSHOT-INDEX-R042-AC002",
        "BRD-SNAPSHOT-INDEX-R042-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R042-O001",
      "obligation_text": "Nguyên tắc: - History không phải Business Evidence"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R042 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R042 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R042 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R042-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R042-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R042 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nguyên tắc: - History không phải Business Evidence.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-SNAPSHOT-INDEX-011"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-SNAPSHOT-INDEX-042",
    "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-042",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Snapshot Lifecycle",
    "source_context_sha256": "4a5c772c53fafe9d0340da8bbec9c9925eda952c6f91fabad0c558818d8abb09",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
    "source_lines": "L750-L755",
    "source_section": "21. Snapshot vs Event vs Audit vs History"
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
  "stable_id": "BRD-SNAPSHOT-INDEX-R042",
  "title": "Nguyên tắc: - History không phải Business Evidence",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-EP-001 — Snapshot là Business Evidence

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-EP-001-AC001",
      "given": "a candidate Snapshot là Business Evidence record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-EP-001-O001"
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
        "SNP-EP-001-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-EP-001-O001",
      "obligation_text": "Snapshot là Business Evidence"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot là Business Evidence.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-EP-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-EP-001",
    "source_context_sha256": "6d84ccafdd3319e0cad5c3877cbe010a15aabbc47a052ce8a1e9125cae81a807",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "1a6f19b28bc75ff872db4d9468e9aea3f70f7a692ae779630c9df24af8a66705",
    "source_lines": "L853-L856",
    "source_section": "25. Enterprise Snapshot Principles > SNP-EP-001"
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
  "stable_id": "SNP-EP-001",
  "title": "Snapshot là Business Evidence",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-EP-002 — Snapshot là Immutable

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-EP-002-AC001",
      "given": "a candidate Snapshot là Immutable record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-EP-002-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "SNP-EP-002-AC002",
      "given": "a Snapshot là Immutable candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "SNP-EP-002-O001"
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
        "SNP-EP-002-AC001",
        "SNP-EP-002-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-EP-002-O001",
      "obligation_text": "Snapshot là Immutable"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "SNP-EP-002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "SNP-EP-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "SNP-EP-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "SNP-EP-002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "SNP-EP-002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "SNP-EP-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot là Immutable.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-EP-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-EP-002",
    "source_context_sha256": "7c4f12cffee86c4e1fe05d1cd084d2da1120e6c86e457d6243d96462bfc1b19d",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "eaba64ec5dbc5c8e8886d2e3424843d523609cc5f6aba1ef69d59044803b3d26",
    "source_lines": "L859-L862",
    "source_section": "25. Enterprise Snapshot Principles > SNP-EP-002"
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
  "stable_id": "SNP-EP-002",
  "title": "Snapshot là Immutable",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-EP-003 — Snapshot được tạo từ Business Event hoặc Business State Transition

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-EP-003-AC001",
      "given": "a candidate Snapshot được tạo từ Business Event hoặc Business State Transition record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-EP-003-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "SNP-EP-003-AC002",
      "given": "a Snapshot được tạo từ Business Event hoặc Business State Transition candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "SNP-EP-003-O001"
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
        "SNP-EP-003-AC001",
        "SNP-EP-003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-EP-003-O001",
      "obligation_text": "Snapshot được tạo từ Business Event hoặc Business State Transition"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot được tạo từ Business Event hoặc Business State Transition.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-EP-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-EP-003",
    "source_context_sha256": "b7e8e33ed83a948f61632be8d68c708956fa73e8f6986bc6ab4a2eb7b3cb5b8c",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "d2c1d483b57968b35e7dfcdbb6b0883047c58e4af2739c077e3850f6117e7687",
    "source_lines": "L865-L868",
    "source_section": "25. Enterprise Snapshot Principles > SNP-EP-003"
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
  "stable_id": "SNP-EP-003",
  "title": "Snapshot được tạo từ Business Event hoặc Business State Transition",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-EP-004 — Snapshot phải chứa đầy đủ Business Context để tái hiện quyết định nghiệp vụ

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-EP-004-AC001",
      "given": "a candidate Snapshot phải chứa đầy đủ Business Context để tái hiện quyết định nghiệp vụ record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-EP-004-O001"
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
        "SNP-EP-004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-EP-004-O001",
      "obligation_text": "Snapshot phải chứa đầy đủ Business Context để tái hiện quyết định nghiệp vụ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot phải chứa đầy đủ Business Context để tái hiện quyết định nghiệp vụ.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-EP-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-EP-004",
    "source_context_sha256": "5c62c7532bb806bd2a3216e8369ceaaf8777666d9abb3881633deea31b44508d",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
    "source_lines": "L871-L874",
    "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
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
  "stable_id": "SNP-EP-004",
  "title": "Snapshot phải chứa đầy đủ Business Context để tái hiện quyết định nghiệp vụ",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-EP-005 — Snapshot độc lập với Runtime Database

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-EP-005-AC001",
      "given": "a candidate Snapshot độc lập với Runtime Database record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-EP-005-O001"
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
        "SNP-EP-005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-EP-005-O001",
      "obligation_text": "Snapshot độc lập với Runtime Database"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot độc lập với Runtime Database.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-EP-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-EP-005",
    "source_context_sha256": "d0387fd087188164c4898826e78fea7796394d714f210d11867a9feeca8f7aea",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "f90b5f1327452acdc580a21e8b2e3c5cb6016313adba48f67a161b3743101614",
    "source_lines": "L877-L880",
    "source_section": "25. Enterprise Snapshot Principles > SNP-EP-005"
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
  "stable_id": "SNP-EP-005",
  "title": "Snapshot độc lập với Runtime Database",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-EP-006 — Snapshot hỗ trợ Versioning

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-EP-006-AC001",
      "given": "a candidate Snapshot hỗ trợ Versioning record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-EP-006-O001"
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
        "SNP-EP-006-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-EP-006-O001",
      "obligation_text": "Snapshot hỗ trợ Versioning"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot hỗ trợ Versioning.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-EP-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-EP-006",
    "source_context_sha256": "a0bfda95caa864291185dd16e018d1cb1d773af45b0a4da9f2ce3537d0538264",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "372f12a419b20ec632a7811865fab56d93cda4132f51a1e2e111e7603eedf0b1",
    "source_lines": "L883-L886",
    "source_section": "25. Enterprise Snapshot Principles > SNP-EP-006"
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
  "stable_id": "SNP-EP-006",
  "title": "Snapshot hỗ trợ Versioning",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-EP-007 — Snapshot chịu sự điều khiển của Security Policy và Retention Policy

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Alias evidence is inherited from the canonical target; the alias is not an acceptance unit.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot chịu sự điều khiển của Security Policy và Retention Policy.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-EP-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-EP-007",
    "source_context_sha256": "2b278e4e7e78a74ebb9a4818643d1490a7d915e886c95f33b651d901d132c1bf",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "def2ef852578e1bd9e0980babc7d11f8a1103e3a4f4e1d1ff7e8094fb2ed8855",
    "source_lines": "L889-L892",
    "source_section": "25. Enterprise Snapshot Principles > SNP-EP-007"
  },
  "record_kind": "ALIAS",
  "relationships": {
    "alias_of": "SNP-P07",
    "aliases": [],
    "coverage_mode": "CANONICAL",
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "SNP-EP-007",
  "title": "Snapshot chịu sự điều khiển của Security Policy và Retention Policy",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-EP-008 — Snapshot hỗ trợ Audit và Regulatory Compliance

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "SNP-EP-008-AC001",
      "given": "an operational task within the scope of Snapshot hỗ trợ Audit và Regulatory Compliance",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "SNP-EP-008-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "SNP-EP-008-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Snapshot hỗ trợ Audit và Regulatory Compliance",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "SNP-EP-008-O001"
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
        "SNP-EP-008-AC001",
        "SNP-EP-008-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-EP-008-O001",
      "obligation_text": "Snapshot hỗ trợ Audit và Regulatory Compliance"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "SNP-EP-008 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "SNP-EP-008 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "SNP-EP-008 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "SNP-EP-008 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "SNP-EP-008-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "SNP-EP-008 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot hỗ trợ Audit và Regulatory Compliance.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-EP-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-EP-008",
    "source_context_sha256": "33df28cfdd6866295d36ccf49ce1c9d999b82019fbab5400505085be4cfa1a0e",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "67c121a632bf9d53c7e3dee94120c40be80394b2a63e24d626c1045f49856596",
    "source_lines": "L895-L898",
    "source_section": "25. Enterprise Snapshot Principles > SNP-EP-008"
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
  "stable_id": "SNP-EP-008",
  "title": "Snapshot hỗ trợ Audit và Regulatory Compliance",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-EP-009 — Snapshot là nguồn dữ liệu ưu tiên cho Reporting, Analytics và Settlement

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-EP-009-AC001",
      "given": "a candidate Snapshot là nguồn dữ liệu ưu tiên cho Reporting, Analytics và Settlement record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-EP-009-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "SNP-EP-009-AC002",
      "given": "a Snapshot là nguồn dữ liệu ưu tiên cho Reporting, Analytics và Settlement candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "SNP-EP-009-O001"
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
        "SNP-EP-009-AC001",
        "SNP-EP-009-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-EP-009-O001",
      "obligation_text": "Snapshot là nguồn dữ liệu ưu tiên cho Reporting, Analytics và Settlement"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot là nguồn dữ liệu ưu tiên cho Reporting, Analytics và Settlement.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-EP-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-EP-009",
    "source_context_sha256": "183ba011992771d49494d62aae619732bed5882fabe815ee83dea16204fb0855",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "2fa23f97c8966201e0af3ba016948bb19554f7567e83b223f53eca2518534ebe",
    "source_lines": "L901-L904",
    "source_section": "25. Enterprise Snapshot Principles > SNP-EP-009"
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
  "stable_id": "SNP-EP-009",
  "title": "Snapshot là nguồn dữ liệu ưu tiên cho Reporting, Analytics và Settlement",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-EP-010 — Enterprise Snapshot Registry là Enterprise Snapshot Dictionary của nền tảng YSim

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-EP-010-AC001",
      "given": "a candidate Enterprise Snapshot Registry là Enterprise Snapshot Dictionary của nền tảng YSim record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-EP-010-O001"
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
        "SNP-EP-010-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-EP-010-O001",
      "obligation_text": "Enterprise Snapshot Registry là Enterprise Snapshot Dictionary của nền tảng YSim"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Enterprise Snapshot Registry là Enterprise Snapshot Dictionary của nền tảng YSim.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-EP-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-EP-010",
    "source_context_sha256": "4fad0e29b071afd721ea20bab7c0dbfaabb5c828a89e13654402beefda572e46",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "20bf077ebf4fd3faeecc02598e17cb42ddcc8bccb67c02f88696d10532963403",
    "source_lines": "L907-L910",
    "source_section": "25. Enterprise Snapshot Principles > SNP-EP-010"
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
  "stable_id": "SNP-EP-010",
  "title": "Enterprise Snapshot Registry là Enterprise Snapshot Dictionary của nền tảng YSim",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-P01 — Snapshot là bất biến

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-P01-AC001",
      "given": "a candidate Snapshot là bất biến record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-P01-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "SNP-P01-AC002",
      "given": "a Snapshot là bất biến candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "SNP-P01-O001"
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
        "SNP-P01-AC001",
        "SNP-P01-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P01-O001",
      "obligation_text": "Snapshot là bất biến"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "SNP-P01 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "SNP-P01 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "SNP-P01 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "SNP-P01 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "SNP-P01-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "SNP-P01 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot là bất biến.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-P01",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Immutable Principle",
    "source_context_sha256": "514f52a4bf9b723e0c71a97e83b50f2b220fd282c5bd267f77a6ad52ca1d9910",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "e7e840edb1300c405b298d322e96869c675047e5dd68208b8601bef081852f79",
    "source_lines": "L323-L326",
    "source_section": "13. Snapshot Principles > SNP-P01 — Immutable"
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
  "stable_id": "SNP-P01",
  "title": "Snapshot là bất biến",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-P02 — Snapshot là bằng chứng nghiệp vụ

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-P02-AC001",
      "given": "a candidate Snapshot là bằng chứng nghiệp vụ record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-P02-O001"
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
        "SNP-P02-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P02-O001",
      "obligation_text": "Snapshot là bằng chứng nghiệp vụ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot là bằng chứng nghiệp vụ.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-P02",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-P02 — Business Evidence",
    "source_context_sha256": "3e2e67dde04d3cac595b75fb06c84b0804bdfd29e413a57f5063017011f535fc",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "4a223f47d9ea1b63d7014ead965ef10937ee4f1689dda405eb32268c4d02ba64",
    "source_lines": "L329-L332",
    "source_section": "13. Snapshot Principles > SNP-P02 — Business Evidence"
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
  "stable_id": "SNP-P02",
  "title": "Snapshot là bằng chứng nghiệp vụ",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-P03 — Snapshot hỗ trợ Version

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-P03-AC001",
      "given": "a candidate Snapshot hỗ trợ Version record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-P03-O001"
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
        "SNP-P03-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P03-O001",
      "obligation_text": "Snapshot hỗ trợ Version"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot hỗ trợ Version.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-P03",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-P03 — Versioned",
    "source_context_sha256": "d3f19319cb6a308052f441623cdec6eb8413c3d2855f575f47c30406e4c61001",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "f93086daddde5d8dc0003b3e5210af9c47c6a73d6f817de2b50a11ffacff1405",
    "source_lines": "L335-L338",
    "source_section": "13. Snapshot Principles > SNP-P03 — Versioned"
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
  "stable_id": "SNP-P03",
  "title": "Snapshot hỗ trợ Version",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-P04 — Snapshot được tạo từ Business Event

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-P04-AC001",
      "given": "a candidate Snapshot được tạo từ Business Event record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-P04-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "SNP-P04-AC002",
      "given": "a Snapshot được tạo từ Business Event candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "SNP-P04-O001"
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
        "SNP-P04-AC001",
        "SNP-P04-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P04-O001",
      "obligation_text": "Snapshot được tạo từ Business Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot được tạo từ Business Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-P04",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-P04 — Event Driven",
    "source_context_sha256": "ed2506e05f2443c4689b9a631accbfaf6e44f07a274eb3d35b712217aae58a50",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "ce5c4c220cd4b8818e92b41202d31316010d9e8f714862a8f87202cc2d90a123",
    "source_lines": "L341-L344",
    "source_section": "13. Snapshot Principles > SNP-P04 — Event Driven"
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
  "stable_id": "SNP-P04",
  "title": "Snapshot được tạo từ Business Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-P05 — Snapshot hỗ trợ Trace đầy đủ

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "SNP-P05-AC001",
      "given": "a candidate Snapshot hỗ trợ Trace đầy đủ record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "SNP-P05-O001"
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
        "SNP-P05-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P05-O001",
      "obligation_text": "Snapshot hỗ trợ Trace đầy đủ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot hỗ trợ Trace đầy đủ.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-P05",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-P05 — Traceable",
    "source_context_sha256": "dd44f97c49c6ffd720555376f346c745ee11a336704c25c10a1b0d8fc08432da",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "f4e60cad82c48767692880864e29b6b8767a419c2ad6865271c08674657df54c",
    "source_lines": "L347-L350",
    "source_section": "13. Snapshot Principles > SNP-P05 — Traceable"
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
  "stable_id": "SNP-P05",
  "title": "Snapshot hỗ trợ Trace đầy đủ",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-P06 — Snapshot hỗ trợ Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "SNP-P06-AC001",
      "given": "an operational task within the scope of Snapshot hỗ trợ Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "SNP-P06-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "SNP-P06-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Snapshot hỗ trợ Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "SNP-P06-O001"
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
        "SNP-P06-AC001",
        "SNP-P06-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P06-O001",
      "obligation_text": "Snapshot hỗ trợ Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "SNP-P06 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "SNP-P06 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "SNP-P06 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "SNP-P06 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "SNP-P06-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "SNP-P06 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot hỗ trợ Audit.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-P06",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-P06 — Auditable",
    "source_context_sha256": "dede127af75da0268d4a832708e0f412039902057db8ada979e425e249438837",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "fa35c719afd3c31f20766fd9417b169022039668897a9dd216d31b7fc4d74830",
    "source_lines": "L353-L356",
    "source_section": "13. Snapshot Principles > SNP-P06 — Auditable"
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
  "stable_id": "SNP-P06",
  "title": "Snapshot hỗ trợ Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-P07 — Snapshot chịu sự điều khiển của Retention Policy và Security Policy

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "SNP-P07-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Snapshot chịu sự điều khiển của Retention Policy và Security Policy",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "SNP-P07-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "SNP-P07-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Snapshot chịu sự điều khiển của Retention Policy và Security Policy",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "SNP-P07-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "SNP-P07-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Snapshot chịu sự điều khiển của Retention Policy và Security Policy",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "SNP-P07-O001"
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
        "SNP-P07-AC001",
        "SNP-P07-AC002",
        "SNP-P07-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P07-O001",
      "obligation_text": "Snapshot chịu sự điều khiển của Retention Policy và Security Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "SNP-P07 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "SNP-P07 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "SNP-P07 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "SNP-P07-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "SNP-P07-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "SNP-P07 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot chịu sự điều khiển của Retention Policy và Security Policy.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-P07",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-P07 — Policy Controlled",
    "source_context_sha256": "a1c3377960ed4f75c9219a0102504b9fa51870830cc6ad2cce3b36a0f780158a",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "165b5c6c3a8718da2fc0e4486aaced8e973a6bce58c137ca173574fafd065730",
    "source_lines": "L359-L362",
    "source_section": "13. Snapshot Principles > SNP-P07 — Policy Controlled"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [
      "SNP-EP-007"
    ],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "SNP-P07",
  "title": "Snapshot chịu sự điều khiển của Retention Policy và Security Policy",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### SNP-P08 — Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "SNP-P08-AC001",
      "given": "the applicable business context, actor, and input for Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "SNP-P08-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "SNP-P08-AC002",
      "given": "the applicable business context, actor, and input for Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the proposed change remains pending until the required approval decision is recorded, and only an approved decision permits the accepted state change",
      "verifies": [
        "SNP-P08-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "SNP-P08-AC003",
      "given": "the applicable business context, actor, and input for Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "SNP-P08-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "SNP-P08-AC004",
      "given": "the applicable business context, actor, and input for Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "SNP-P08-O004"
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
        "SNP-P08-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P08-O001",
      "obligation_text": "Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới phải trải qua: Architecture Review."
    },
    {
      "acceptance_criterion_references": [
        "SNP-P08-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P08-O002",
      "obligation_text": "Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới phải trải qua: Approval."
    },
    {
      "acceptance_criterion_references": [
        "SNP-P08-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P08-O003",
      "obligation_text": "Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới phải trải qua: Versioning."
    },
    {
      "acceptance_criterion_references": [
        "SNP-P08-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P08-O004",
      "obligation_text": "Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới phải trải qua: Traceability."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới phải trải qua: - Architecture Review - Approval - Versioning - Traceability",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "SNP-P08",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SNP-P08 — Enterprise Governance",
    "source_context_sha256": "6ef4025b1002154498fbfec31759020302ba1157a554968a68688b4077eb6801",
    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
    "source_fingerprint": "49ca8060490a246d0478f6b2124386fb9dfb37eecec9011da914e786199b0d53",
    "source_lines": "L365-L375",
    "source_section": "13. Snapshot Principles > SNP-P08 — Enterprise Governance"
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
  "stable_id": "SNP-P08",
  "title": "Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới …",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
