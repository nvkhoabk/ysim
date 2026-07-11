---
document_code: BRD-SNAPSHOT-INDEX
document_name: Enterprise Snapshot Registry
project: YSim v2.0
document_set: BRD
version: 1.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
---

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