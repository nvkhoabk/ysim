---
document_code: "BRD-SNAPSHOT-INDEX"
document_id: "BRD-SNAPSHOT-INDEX"
title: "Enterprise Snapshot Registry"
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

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-SNAPSHOT-INDEX-R001 — Mỗi Snapshot được cấp một mã định danh duy nhất

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
      "requirement_id": "BRD-SNAPSHOT-INDEX-R001",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "41f37cccd07fa8865723025b53240edeba8bb89c1e518931d727872f117c4a5d"
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
        "BRD-SNAPSHOT-INDEX-R001-AC001",
        "BRD-SNAPSHOT-INDEX-R001-AC002",
        "BRD-SNAPSHOT-INDEX-R001-AC003"
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
    "source_lines": "L965-L1040",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R001"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "A non-business technical change does not create a business Snapshot unless separately required"
    ],
    "concrete_bindings": [
      {
        "from_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-SNAPSHOT-INDEX-R002.FROM_STATE"
            ],
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
            "source_type": "SOURCE_LITERAL",
            "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R002.FROM_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
            "source_lines": "L261-L263",
            "source_section": "10. Immutable Principle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.FROM_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "state_machine": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
            "source_type": "SOURCE_LITERAL",
            "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R002.STATE_MACHINE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
            "source_lines": "L261-L263",
            "source_section": "10. Immutable Principle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_MACHINE_ID",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.STATE_MACHINE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_MACHINE_ID"
        },
        "to_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-SNAPSHOT-INDEX-R002.TO_STATE"
            ],
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
            "source_type": "SOURCE_LITERAL",
            "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R002.TO_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
            "source_lines": "L261-L263",
            "source_section": "10. Immutable Principle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.TO_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "trigger": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
            "source_type": "SOURCE_LITERAL",
            "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R002.TRIGGER",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
            "source_lines": "L261-L263",
            "source_section": "10. Immutable Principle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.TRIGGER",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R002",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Existing Snapshot is edited or no new Snapshot is created after the change"
    ],
    "operator_composition": [
      "STATE_TRANSITION_ALLOWED"
    ],
    "positive_oracle": [
      "A new Snapshot is created for the changed business state"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
      "source_lines": "L261-L263",
      "source_section": "10. Immutable Principle"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
          "source_type": "SOURCE_LITERAL",
          "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
        },
        "identifier": "BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-SNAPSHOT-INDEX-R002.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
          "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
          "source_lines": "L261-L263",
          "source_section": "10. Immutable Principle"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-SNAPSHOT-INDEX-R002.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.BUSINESS_OBJECT_ID",
        "FIELD.CHANGE_ID",
        "FIELD.PRIOR_SNAPSHOT_ID",
        "FIELD.NEW_SNAPSHOT_ID",
        "FIELD.CHANGE_TIME",
        "FIELD.SNAPSHOT_TIME"
      ],
      "producer": "BRD-SNAPSHOT-INDEX-R002.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-SNAPSHOT-INDEX-R002.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.BUSINESS_OBJECT_ID",
        "FIELD.CHANGE_ID",
        "FIELD.PRIOR_SNAPSHOT_ID",
        "FIELD.NEW_SNAPSHOT_ID",
        "FIELD.CHANGE_TIME",
        "FIELD.SNAPSHOT_TIME"
      ],
      "required_values_or_hashes": [
        "BRD-SNAPSHOT-INDEX-R002.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-SNAPSHOT-INDEX-R002.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-SNAPSHOT-INDEX-R002.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-SNAPSHOT-INDEX-R002-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED",
          "evaluator_consumed_bindings": [
            "from_state",
            "state_machine",
            "to_state",
            "trigger"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
              "source_type": "SOURCE_LITERAL",
              "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
              "source_lines": "L261-L263",
              "source_section": "10. Immutable Principle"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
              "source_type": "SOURCE_LITERAL",
              "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
              "source_lines": "L261-L263",
              "source_section": "10. Immutable Principle"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "from_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-SNAPSHOT-INDEX-R002.FROM_STATE"
                  ],
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R002.FROM_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
                  "source_lines": "L261-L263",
                  "source_section": "10. Immutable Principle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.FROM_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "state_machine": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R002.STATE_MACHINE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
                  "source_lines": "L261-L263",
                  "source_section": "10. Immutable Principle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_MACHINE_ID",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.STATE_MACHINE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_MACHINE_ID"
              },
              "to_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-SNAPSHOT-INDEX-R002.TO_STATE"
                  ],
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R002.TO_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
                  "source_lines": "L261-L263",
                  "source_section": "10. Immutable Principle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.TO_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "trigger": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R002.TRIGGER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
                  "source_lines": "L261-L263",
                  "source_section": "10. Immutable Principle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.TRIGGER",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
                  "source_lines": "L261-L263",
                  "source_section": "10. Immutable Principle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
                  "source_lines": "L261-L263",
                  "source_section": "10. Immutable Principle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
                "source_type": "SOURCE_LITERAL",
                "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
                "source_lines": "L261-L263",
                "source_section": "10. Immutable Principle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "STATE_TRANSITION_ALLOWED"
          },
          "obligation_id": "BRD-SNAPSHOT-INDEX-R002-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
              "source_type": "SOURCE_LITERAL",
              "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
              "source_lines": "L261-L263",
              "source_section": "10. Immutable Principle"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "operator_id": "STATE_TRANSITION_ALLOWED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "from_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-SNAPSHOT-INDEX-R002.FROM_STATE"
                ],
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
                "source_type": "SOURCE_LITERAL",
                "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R002.FROM_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.FROM_STATE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
                "source_lines": "L261-L263",
                "source_section": "10. Immutable Principle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.FROM_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "state_machine": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
                "source_type": "SOURCE_LITERAL",
                "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R002.STATE_MACHINE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.STATE_MACHINE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
                "source_lines": "L261-L263",
                "source_section": "10. Immutable Principle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_MACHINE_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.STATE_MACHINE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_MACHINE_ID"
            },
            "to_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-SNAPSHOT-INDEX-R002.TO_STATE"
                ],
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
                "source_type": "SOURCE_LITERAL",
                "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R002.TO_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.TO_STATE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
                "source_lines": "L261-L263",
                "source_section": "10. Immutable Principle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.TO_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "trigger": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
                "source_type": "SOURCE_LITERAL",
                "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R002.TRIGGER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED.TRIGGER.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
                "source_lines": "L261-L263",
                "source_section": "10. Immutable Principle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.TRIGGER",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "A non-business technical change does not create a business Snapshot unless separately required"
      ],
      "contract_ast_sha256": "76f3b32c3e986a07244ef39ab9fddac0aec814221dbe085bc25ea34acd396f2c",
      "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R002",
      "criticality": "CRITICAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#10. Immutable Principle",
            "source_type": "SOURCE_LITERAL",
            "version": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R002.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
            "source_lines": "L261-L263",
            "source_section": "10. Immutable Principle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.BRD-SNAPSHOT-INDEX-R002.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-SNAPSHOT-INDEX-R002.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.BUSINESS_OBJECT_ID",
          "FIELD.CHANGE_ID",
          "FIELD.PRIOR_SNAPSHOT_ID",
          "FIELD.NEW_SNAPSHOT_ID",
          "FIELD.CHANGE_TIME",
          "FIELD.SNAPSHOT_TIME"
        ],
        "producer": "BRD-SNAPSHOT-INDEX-R002.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-SNAPSHOT-INDEX-R002.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.BUSINESS_OBJECT_ID",
          "FIELD.CHANGE_ID",
          "FIELD.PRIOR_SNAPSHOT_ID",
          "FIELD.NEW_SNAPSHOT_ID",
          "FIELD.CHANGE_TIME",
          "FIELD.SNAPSHOT_TIME"
        ],
        "required_values_or_hashes": [
          "BRD-SNAPSHOT-INDEX-R002.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-SNAPSHOT-INDEX-R002.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-SNAPSHOT-INDEX-R002.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-9FB7B6C737CF0404CCDA",
        "P2C-C4-FX-A527986521876D198C99",
        "P2C-C4-FX-7A899C239A276DD37FCB"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Existing Snapshot is edited or no new Snapshot is created after the change"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-SNAPSHOT-INDEX-R002-O001",
          "obligation_text": "Nếu dữ liệu nghiệp vụ thay đổi: Platform phải tạo Snapshot mới"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-SNAPSHOT-INDEX-R002.O1.1.STATE_TRANSITION_ALLOWED"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-SNAPSHOT-INDEX-R002-O001"
        }
      ],
      "operator_composition": [
        "STATE_TRANSITION_ALLOWED"
      ],
      "positive_oracles": [
        "A new Snapshot is created for the changed business state"
      ],
      "preconditions": [
        "The prior business state and committed change are identifiable"
      ],
      "prohibitions": [
        "Existing Snapshot is edited or no new Snapshot is created after the change"
      ],
      "requirement_id": "BRD-SNAPSHOT-INDEX-R002",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
        "source_fingerprint": "051635b7d42715cb1d418b299a476129f7d947b9abec2033c3e1104c6ab9d2f6",
        "source_lines": "L261-L263",
        "source_section": "10. Immutable Principle"
      },
      "source_statement": "Nếu dữ liệu nghiệp vụ thay đổi: Platform phải tạo Snapshot mới.",
      "surrounding_source_context": "### BRD-SNAPSHOT-INDEX-R002 — Nếu dữ liệu nghiệp vụ thay đổi: Platform phải tạo Snapshot mới"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R002",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "SEMANTIC_ACCEPTANCE_RENDERER_C2",
    "runtime_status": "RUNTIME_ADAPTER_PENDING"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "ACCEPTANCE_READY",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-SNAPSHOT-INDEX-R002-AC001",
        "BRD-SNAPSHOT-INDEX-R002-AC002",
        "BRD-SNAPSHOT-INDEX-R002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R002-O001",
      "obligation_text": "Nếu dữ liệu nghiệp vụ thay đổi: Platform phải tạo Snapshot mới"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R002 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R002-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R002-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R002 does not define a recovery obligation."
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
    "source_lines": "L1042-L2029",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R003",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "d329bff77b71dccf548a57f9ecc262634d8a7e035bad170339dd5d624bc4e759"
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R003 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R003 does not define a recovery obligation."
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
    "source_lines": "L2031-L2139",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R004",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "4f279af6cc4a838d95b8cfc89adf00a420cb873c1d4b5177ef212e180fa3b19d"
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
        "BRD-SNAPSHOT-INDEX-R004-AC001",
        "BRD-SNAPSHOT-INDEX-R004-AC002",
        "BRD-SNAPSHOT-INDEX-R004-AC003"
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
    "source_fingerprint": "4f279af6cc4a838d95b8cfc89adf00a420cb873c1d4b5177ef212e180fa3b19d",
    "source_lines": "L2141-L2216",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R005",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "b70f2b2049d48521cbdd2d462ebb401605d6e82e2e175527f08ba8cea4ef4f74"
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
        "BRD-SNAPSHOT-INDEX-R005-AC001",
        "BRD-SNAPSHOT-INDEX-R005-AC002",
        "BRD-SNAPSHOT-INDEX-R005-AC003"
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
    "source_fingerprint": "b70f2b2049d48521cbdd2d462ebb401605d6e82e2e175527f08ba8cea4ef4f74",
    "source_lines": "L2218-L2293",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R006",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "29cb7f87f924a5756aa901510eb95bc5dff237fe268da955b5c1347acce27176"
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
        "BRD-SNAPSHOT-INDEX-R006-AC001",
        "BRD-SNAPSHOT-INDEX-R006-AC002",
        "BRD-SNAPSHOT-INDEX-R006-AC003"
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
    "source_lines": "L2295-L2370",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R006"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "Creating different content in a new Snapshot is allowed; changing existing content is not"
    ],
    "concrete_bindings": [
      {
        "after_hash": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
            "source_type": "SOURCE_LITERAL",
            "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R007.AFTER_HASH",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.AFTER_HASH.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
            "source_lines": "L500",
            "source_section": "18. Snapshot Version"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "HASH",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.AFTER_HASH",
            "version": "1.0.0"
          },
          "semantic_type": "HASH"
        },
        "audit_record": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
            "source_type": "SOURCE_LITERAL",
            "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R007.AUDIT_RECORD",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.AUDIT_RECORD.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
            "source_lines": "L500",
            "source_section": "18. Snapshot Version"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.AUDIT_RECORD",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "before_hash": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
            "source_type": "SOURCE_LITERAL",
            "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R007.BEFORE_HASH",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.BEFORE_HASH.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
            "source_lines": "L500",
            "source_section": "18. Snapshot Version"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "HASH",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.BEFORE_HASH",
            "version": "1.0.0"
          },
          "semantic_type": "HASH"
        },
        "immutability_boundary": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
            "source_type": "SOURCE_LITERAL",
            "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R007.IMMUTABILITY_BOUNDARY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.IMMUTABILITY_BOUNDARY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
            "source_lines": "L500",
            "source_section": "18. Snapshot Version"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.IMMUTABILITY_BOUNDARY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "protected_fields": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "FIELD.SNAPSHOT_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.SNAPSHOT_ID",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "FIELD.CONTENT_HASH_BEFORE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.2",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.CONTENT_HASH_BEFORE",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "FIELD.CONTENT_HASH_AFTER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.3",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.CONTENT_HASH_AFTER",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "FIELD.WRITE_RESULT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.4",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.WRITE_RESULT",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "FIELD.AUDIT_RECORD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.5",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.AUDIT_RECORD",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
            "source_lines": "L500",
            "source_section": "18. Snapshot Version"
          },
          "semantic_type": "SET_OF<FIELD_ID>"
        },
        "required_fields": {
          "members": [
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "FIELD.SNAPSHOT_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.SNAPSHOT_ID",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "FIELD.CONTENT_HASH_BEFORE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.2",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.CONTENT_HASH_BEFORE",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "FIELD.CONTENT_HASH_AFTER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.3",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.CONTENT_HASH_AFTER",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "FIELD.WRITE_RESULT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.4",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.WRITE_RESULT",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            },
            {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "FIELD.AUDIT_RECORD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.5",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "FIELD_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.AUDIT_RECORD",
                "version": "1.0.0"
              },
              "semantic_type": "FIELD_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
            "source_lines": "L500",
            "source_section": "18. Snapshot Version"
          },
          "semantic_type": "SET_OF<FIELD_ID>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R007",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Snapshot Content is modified or deleted"
    ],
    "operator_composition": [
      "AUDIT_IMMUTABLE"
    ],
    "positive_oracle": [
      "Stored Snapshot Content remains unchanged"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
      "source_lines": "L500",
      "source_section": "18. Snapshot Version"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
          "source_type": "SOURCE_LITERAL",
          "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
        },
        "identifier": "BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-SNAPSHOT-INDEX-R007.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
          "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
          "source_lines": "L500",
          "source_section": "18. Snapshot Version"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-SNAPSHOT-INDEX-R007.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.SNAPSHOT_ID",
        "FIELD.CONTENT_HASH_BEFORE",
        "FIELD.CONTENT_HASH_AFTER",
        "FIELD.WRITE_RESULT",
        "FIELD.AUDIT_RECORD"
      ],
      "producer": "BRD-SNAPSHOT-INDEX-R007.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-SNAPSHOT-INDEX-R007.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.SNAPSHOT_ID",
        "FIELD.CONTENT_HASH_BEFORE",
        "FIELD.CONTENT_HASH_AFTER",
        "FIELD.WRITE_RESULT",
        "FIELD.AUDIT_RECORD"
      ],
      "required_values_or_hashes": [
        "BRD-SNAPSHOT-INDEX-R007.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-SNAPSHOT-INDEX-R007.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-SNAPSHOT-INDEX-R007.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-SNAPSHOT-INDEX-R007-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE",
          "evaluator_consumed_bindings": [
            "after_hash",
            "audit_record",
            "before_hash",
            "immutability_boundary",
            "protected_fields",
            "required_fields"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
              "source_type": "SOURCE_LITERAL",
              "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
              "source_lines": "L500",
              "source_section": "18. Snapshot Version"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
              "source_type": "SOURCE_LITERAL",
              "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
              "source_lines": "L500",
              "source_section": "18. Snapshot Version"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "after_hash": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R007.AFTER_HASH",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.AFTER_HASH.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                  "source_lines": "L500",
                  "source_section": "18. Snapshot Version"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "HASH",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.AFTER_HASH",
                  "version": "1.0.0"
                },
                "semantic_type": "HASH"
              },
              "audit_record": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R007.AUDIT_RECORD",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.AUDIT_RECORD.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                  "source_lines": "L500",
                  "source_section": "18. Snapshot Version"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.AUDIT_RECORD",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "before_hash": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R007.BEFORE_HASH",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.BEFORE_HASH.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                  "source_lines": "L500",
                  "source_section": "18. Snapshot Version"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "HASH",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.BEFORE_HASH",
                  "version": "1.0.0"
                },
                "semantic_type": "HASH"
              },
              "immutability_boundary": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R007.IMMUTABILITY_BOUNDARY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.IMMUTABILITY_BOUNDARY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                  "source_lines": "L500",
                  "source_section": "18. Snapshot Version"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.IMMUTABILITY_BOUNDARY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "protected_fields": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                    },
                    "identifier": "FIELD.SNAPSHOT_ID",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                      "source_lines": "L500",
                      "source_section": "18. Snapshot Version"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.SNAPSHOT_ID",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                    },
                    "identifier": "FIELD.CONTENT_HASH_BEFORE",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.2",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                      "source_lines": "L500",
                      "source_section": "18. Snapshot Version"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.CONTENT_HASH_BEFORE",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                    },
                    "identifier": "FIELD.CONTENT_HASH_AFTER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.3",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                      "source_lines": "L500",
                      "source_section": "18. Snapshot Version"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.CONTENT_HASH_AFTER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                    },
                    "identifier": "FIELD.WRITE_RESULT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.4",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                      "source_lines": "L500",
                      "source_section": "18. Snapshot Version"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.WRITE_RESULT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                    },
                    "identifier": "FIELD.AUDIT_RECORD",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.5",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                      "source_lines": "L500",
                      "source_section": "18. Snapshot Version"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.AUDIT_RECORD",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                  "source_lines": "L500",
                  "source_section": "18. Snapshot Version"
                },
                "semantic_type": "SET_OF<FIELD_ID>"
              },
              "required_fields": {
                "members": [
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                    },
                    "identifier": "FIELD.SNAPSHOT_ID",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                      "source_lines": "L500",
                      "source_section": "18. Snapshot Version"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.SNAPSHOT_ID",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                    },
                    "identifier": "FIELD.CONTENT_HASH_BEFORE",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.2",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                      "source_lines": "L500",
                      "source_section": "18. Snapshot Version"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.CONTENT_HASH_BEFORE",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                    },
                    "identifier": "FIELD.CONTENT_HASH_AFTER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.3",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                      "source_lines": "L500",
                      "source_section": "18. Snapshot Version"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.CONTENT_HASH_AFTER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                    },
                    "identifier": "FIELD.WRITE_RESULT",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.4",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                      "source_lines": "L500",
                      "source_section": "18. Snapshot Version"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.WRITE_RESULT",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  },
                  {
                    "authoritative_source": {
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                      "source_type": "SOURCE_LITERAL",
                      "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                    },
                    "identifier": "FIELD.AUDIT_RECORD",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.5",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                      "source_lines": "L500",
                      "source_section": "18. Snapshot Version"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "FIELD_ID",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.AUDIT_RECORD",
                      "version": "1.0.0"
                    },
                    "semantic_type": "FIELD_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                  "source_lines": "L500",
                  "source_section": "18. Snapshot Version"
                },
                "semantic_type": "SET_OF<FIELD_ID>"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                  "source_lines": "L500",
                  "source_section": "18. Snapshot Version"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                  "source_type": "SOURCE_LITERAL",
                  "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                  "source_lines": "L500",
                  "source_section": "18. Snapshot Version"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "AUDIT_IMMUTABLE"
          },
          "obligation_id": "BRD-SNAPSHOT-INDEX-R007-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
              "source_type": "SOURCE_LITERAL",
              "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
              "source_lines": "L500",
              "source_section": "18. Snapshot Version"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "operator_id": "AUDIT_IMMUTABLE",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "after_hash": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R007.AFTER_HASH",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.AFTER_HASH.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "HASH",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.AFTER_HASH",
                "version": "1.0.0"
              },
              "semantic_type": "HASH"
            },
            "audit_record": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R007.AUDIT_RECORD",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.AUDIT_RECORD.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.AUDIT_RECORD",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "before_hash": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R007.BEFORE_HASH",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.BEFORE_HASH.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "HASH",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.BEFORE_HASH",
                "version": "1.0.0"
              },
              "semantic_type": "HASH"
            },
            "immutability_boundary": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                "source_type": "SOURCE_LITERAL",
                "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R007.IMMUTABILITY_BOUNDARY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.IMMUTABILITY_BOUNDARY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.IMMUTABILITY_BOUNDARY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "protected_fields": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                  },
                  "identifier": "FIELD.SNAPSHOT_ID",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                    "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                    "source_lines": "L500",
                    "source_section": "18. Snapshot Version"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.SNAPSHOT_ID",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                  },
                  "identifier": "FIELD.CONTENT_HASH_BEFORE",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.2",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                    "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                    "source_lines": "L500",
                    "source_section": "18. Snapshot Version"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.CONTENT_HASH_BEFORE",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                  },
                  "identifier": "FIELD.CONTENT_HASH_AFTER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.3",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                    "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                    "source_lines": "L500",
                    "source_section": "18. Snapshot Version"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.CONTENT_HASH_AFTER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                  },
                  "identifier": "FIELD.WRITE_RESULT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.4",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                    "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                    "source_lines": "L500",
                    "source_section": "18. Snapshot Version"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.WRITE_RESULT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                  },
                  "identifier": "FIELD.AUDIT_RECORD",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN.MEMBER.5",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                    "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                    "source_lines": "L500",
                    "source_section": "18. Snapshot Version"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.AUDIT_RECORD",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.PROTECTED_FIELDS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "semantic_type": "SET_OF<FIELD_ID>"
            },
            "required_fields": {
              "members": [
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                  },
                  "identifier": "FIELD.SNAPSHOT_ID",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                    "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                    "source_lines": "L500",
                    "source_section": "18. Snapshot Version"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.SNAPSHOT_ID",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                  },
                  "identifier": "FIELD.CONTENT_HASH_BEFORE",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.2",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                    "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                    "source_lines": "L500",
                    "source_section": "18. Snapshot Version"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.CONTENT_HASH_BEFORE",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                  },
                  "identifier": "FIELD.CONTENT_HASH_AFTER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.3",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                    "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                    "source_lines": "L500",
                    "source_section": "18. Snapshot Version"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.CONTENT_HASH_AFTER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                  },
                  "identifier": "FIELD.WRITE_RESULT",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.4",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                    "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                    "source_lines": "L500",
                    "source_section": "18. Snapshot Version"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.WRITE_RESULT",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                },
                {
                  "authoritative_source": {
                    "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
                    "source_type": "SOURCE_LITERAL",
                    "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
                  },
                  "identifier": "FIELD.AUDIT_RECORD",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN.MEMBER.5",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                    "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                    "source_lines": "L500",
                    "source_section": "18. Snapshot Version"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "FIELD_ID",
                    "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R007.FIELD.AUDIT_RECORD",
                    "version": "1.0.0"
                  },
                  "semantic_type": "FIELD_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE.REQUIRED_FIELDS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
                "source_lines": "L500",
                "source_section": "18. Snapshot Version"
              },
              "semantic_type": "SET_OF<FIELD_ID>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Creating different content in a new Snapshot is allowed; changing existing content is not"
      ],
      "contract_ast_sha256": "5153fdfb79432722f7f22de2329aad82ee2555e0df7104288c91591c46219453",
      "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R007",
      "criticality": "NORMAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#18. Snapshot Version",
            "source_type": "SOURCE_LITERAL",
            "version": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R007.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
            "source_lines": "L500",
            "source_section": "18. Snapshot Version"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.BRD-SNAPSHOT-INDEX-R007.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-SNAPSHOT-INDEX-R007.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.SNAPSHOT_ID",
          "FIELD.CONTENT_HASH_BEFORE",
          "FIELD.CONTENT_HASH_AFTER",
          "FIELD.WRITE_RESULT",
          "FIELD.AUDIT_RECORD"
        ],
        "producer": "BRD-SNAPSHOT-INDEX-R007.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-SNAPSHOT-INDEX-R007.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.SNAPSHOT_ID",
          "FIELD.CONTENT_HASH_BEFORE",
          "FIELD.CONTENT_HASH_AFTER",
          "FIELD.WRITE_RESULT",
          "FIELD.AUDIT_RECORD"
        ],
        "required_values_or_hashes": [
          "BRD-SNAPSHOT-INDEX-R007.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-SNAPSHOT-INDEX-R007.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-SNAPSHOT-INDEX-R007.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-0D2FA07EE7B028DEF4A7",
        "P2C-C4-FX-C697285AE81FD7E18DEE",
        "P2C-C4-FX-FA007196443E92D4C073"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Snapshot Content is modified or deleted"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-SNAPSHOT-INDEX-R007-O001",
          "obligation_text": "Snapshot Content vẫn luôn bất biến"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-SNAPSHOT-INDEX-R007.O1.1.AUDIT_IMMUTABLE"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-SNAPSHOT-INDEX-R007-O001"
        }
      ],
      "operator_composition": [
        "AUDIT_IMMUTABLE"
      ],
      "positive_oracles": [
        "Stored Snapshot Content remains unchanged"
      ],
      "preconditions": [
        "The Snapshot Content identity and hash exist"
      ],
      "prohibitions": [
        "Snapshot Content is modified or deleted"
      ],
      "requirement_id": "BRD-SNAPSHOT-INDEX-R007",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
        "source_fingerprint": "b3afe512e328dbfa2d4c6544e182efbeb905f3f92f29415f6710013a1042a951",
        "source_lines": "L500",
        "source_section": "18. Snapshot Version"
      },
      "source_statement": "Snapshot Content vẫn luôn bất biến.",
      "surrounding_source_context": "### BRD-SNAPSHOT-INDEX-R007 — Snapshot Content vẫn luôn bất biến"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R007",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "SEMANTIC_ACCEPTANCE_RENDERER_C2",
    "runtime_status": "RUNTIME_ADAPTER_PENDING"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "ACCEPTANCE_READY",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-SNAPSHOT-INDEX-R007-AC001",
        "BRD-SNAPSHOT-INDEX-R007-AC002",
        "BRD-SNAPSHOT-INDEX-R007-AC003"
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
    "source_lines": "L2372-L4416",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R007"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "Later context changes do not alter the historical Snapshot; a new Snapshot captures new context"
    ],
    "concrete_bindings": [
      {
        "actual_set": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
            "source_type": "SOURCE_LITERAL",
            "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
          },
          "identifier": "RESOLVED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BRD-SNAPSHOT-INDEX-R008.RESOLVED.COLLECTION",
          "origin": {
            "origin_id": "YSIM.BRD-SNAPSHOT-INDEX-R008.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
            "source_lines": "L586",
            "source_section": "16. Snapshot Composition Principle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R008.RESOLVED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
        },
        "required_members": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
            "source_type": "SOURCE_LITERAL",
            "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
          },
          "identifier": "GOVERNED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BRD-SNAPSHOT-INDEX-R008.GOVERNED.COLLECTION",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
            "source_lines": "L586",
            "source_section": "16. Snapshot Composition Principle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R008.GOVERNED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R008",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "A required context value or version is absent, preventing exact reproduction"
    ],
    "operator_composition": [
      "SET_CONTAINS"
    ],
    "positive_oracle": [
      "The Snapshot stores all context needed to reproduce the decision as it was made at creation time"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
      "source_lines": "L586",
      "source_section": "16. Snapshot Composition Principle"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
          "source_type": "SOURCE_LITERAL",
          "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
        },
        "identifier": "BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-SNAPSHOT-INDEX-R008.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
          "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
          "source_lines": "L586",
          "source_section": "16. Snapshot Composition Principle"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-SNAPSHOT-INDEX-R008.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.SNAPSHOT_ID",
        "FIELD.DECISION_ID",
        "FIELD.CONTEXT_FIELDS",
        "FIELD.POLICY_VERSIONS",
        "FIELD.CREATION_TIME",
        "FIELD.REPLAY_RESULT"
      ],
      "producer": "BRD-SNAPSHOT-INDEX-R008.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-SNAPSHOT-INDEX-R008.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.SNAPSHOT_ID",
        "FIELD.DECISION_ID",
        "FIELD.CONTEXT_FIELDS",
        "FIELD.POLICY_VERSIONS",
        "FIELD.CREATION_TIME",
        "FIELD.REPLAY_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-SNAPSHOT-INDEX-R008.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-SNAPSHOT-INDEX-R008.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-SNAPSHOT-INDEX-R008.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-SNAPSHOT-INDEX-R008-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS",
          "evaluator_consumed_bindings": [
            "actual_set",
            "required_members"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
              "source_type": "SOURCE_LITERAL",
              "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
              "source_lines": "L586",
              "source_section": "16. Snapshot Composition Principle"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
                  "source_lines": "L586",
                  "source_section": "16. Snapshot Composition Principle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
              "source_lines": "L586",
              "source_section": "16. Snapshot Composition Principle"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_set": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
                },
                "identifier": "RESOLVED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BRD-SNAPSHOT-INDEX-R008.RESOLVED.COLLECTION",
                "origin": {
                  "origin_id": "YSIM.BRD-SNAPSHOT-INDEX-R008.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
                  "source_lines": "L586",
                  "source_section": "16. Snapshot Composition Principle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R008.RESOLVED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
              },
              "required_members": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
                },
                "identifier": "GOVERNED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BRD-SNAPSHOT-INDEX-R008.GOVERNED.COLLECTION",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
                  "source_lines": "L586",
                  "source_section": "16. Snapshot Composition Principle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R008.GOVERNED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
              }
            },
            "comparison": {
              "expected": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
                      "source_type": "SOURCE_LITERAL",
                      "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
                    },
                    "identifier": "BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
                      "source_lines": "L586",
                      "source_section": "16. Snapshot Composition Principle"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
                  "source_lines": "L586",
                  "source_section": "16. Snapshot Composition Principle"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "observed": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
                      "source_type": "SOURCE_LITERAL",
                      "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
                    },
                    "identifier": "BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
                      "source_lines": "L586",
                      "source_section": "16. Snapshot Composition Principle"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
                  "source_lines": "L586",
                  "source_section": "16. Snapshot Composition Principle"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
                "source_type": "SOURCE_LITERAL",
                "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
                "source_lines": "L586",
                "source_section": "16. Snapshot Composition Principle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "SET_CONTAINS"
          },
          "obligation_id": "BRD-SNAPSHOT-INDEX-R008-O001",
          "observed_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
                  "source_lines": "L586",
                  "source_section": "16. Snapshot Composition Principle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
              "source_lines": "L586",
              "source_section": "16. Snapshot Composition Principle"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "operator_id": "SET_CONTAINS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_set": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
                "source_type": "SOURCE_LITERAL",
                "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
              },
              "identifier": "RESOLVED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BRD-SNAPSHOT-INDEX-R008.RESOLVED.COLLECTION",
              "origin": {
                "origin_id": "YSIM.BRD-SNAPSHOT-INDEX-R008.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
                "source_lines": "L586",
                "source_section": "16. Snapshot Composition Principle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R008.RESOLVED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
            },
            "required_members": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
                "source_type": "SOURCE_LITERAL",
                "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
              },
              "identifier": "GOVERNED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BRD-SNAPSHOT-INDEX-R008.GOVERNED.COLLECTION",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
                "source_lines": "L586",
                "source_section": "16. Snapshot Composition Principle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R008.GOVERNED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Later context changes do not alter the historical Snapshot; a new Snapshot captures new context"
      ],
      "contract_ast_sha256": "fcb596696bc9a0fbef6047c73917b3895facd78fe0745451405f3569385e40a9",
      "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R008",
      "criticality": "NORMAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#16. Snapshot Composition Principle",
            "source_type": "SOURCE_LITERAL",
            "version": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R008.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
            "source_lines": "L586",
            "source_section": "16. Snapshot Composition Principle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.BRD-SNAPSHOT-INDEX-R008.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-SNAPSHOT-INDEX-R008.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.SNAPSHOT_ID",
          "FIELD.DECISION_ID",
          "FIELD.CONTEXT_FIELDS",
          "FIELD.POLICY_VERSIONS",
          "FIELD.CREATION_TIME",
          "FIELD.REPLAY_RESULT"
        ],
        "producer": "BRD-SNAPSHOT-INDEX-R008.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-SNAPSHOT-INDEX-R008.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.SNAPSHOT_ID",
          "FIELD.DECISION_ID",
          "FIELD.CONTEXT_FIELDS",
          "FIELD.POLICY_VERSIONS",
          "FIELD.CREATION_TIME",
          "FIELD.REPLAY_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-SNAPSHOT-INDEX-R008.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-SNAPSHOT-INDEX-R008.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-SNAPSHOT-INDEX-R008.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-R2-FX-3792BAEAD544320CB3A1",
        "P2C-C4-R2-FX-0FA05C68938009B233F6",
        "P2C-C4-R2-FX-E9141CFF3D71F3E5E2DA"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "A required context value or version is absent, preventing exact reproduction"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-SNAPSHOT-INDEX-R008-O001",
          "obligation_text": "Business Snapshot phải lưu toàn bộ **Business Context** cần thiết để có thể tái hiện chính xác quyết định nghiệp vụ tại thời điểm Snapshot được tạo"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-SNAPSHOT-INDEX-R008.O1.1.SET_CONTAINS"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-SNAPSHOT-INDEX-R008-O001"
        }
      ],
      "operator_composition": [
        "SET_CONTAINS"
      ],
      "positive_oracles": [
        "The Snapshot stores all context needed to reproduce the decision as it was made at creation time"
      ],
      "preconditions": [
        "The business decision and its effective context are known"
      ],
      "prohibitions": [
        "A required context value or version is absent, preventing exact reproduction"
      ],
      "requirement_id": "BRD-SNAPSHOT-INDEX-R008",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
        "source_fingerprint": "14703fc43530d77989c2bcd17407d70aff2677628faea2bdb0c6c30d329e3d9a",
        "source_lines": "L586",
        "source_section": "16. Snapshot Composition Principle"
      },
      "source_statement": "Business Snapshot phải lưu toàn bộ **Business Context** cần thiết để có thể tái hiện chính xác quyết định nghiệp vụ tại thời điểm Snapshot được tạo.",
      "surrounding_source_context": "### BRD-SNAPSHOT-INDEX-R008 — Business Snapshot phải lưu toàn bộ **Business Context** cần thiết để có thể tái hiện chính xác q…"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R008",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "SEMANTIC_ACCEPTANCE_RENDERER_C2",
    "runtime_status": "RUNTIME_ADAPTER_PENDING"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "ACCEPTANCE_READY",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-SNAPSHOT-INDEX-R008-AC001",
        "BRD-SNAPSHOT-INDEX-R008-AC002",
        "BRD-SNAPSHOT-INDEX-R008-AC003"
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
    "source_lines": "L4418-L5216",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R009",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "86a0e9f3fb3692208b23b8cd27161d70b3389ea85bc0444a5de9939ba7f4c83c"
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
        "BRD-SNAPSHOT-INDEX-R009-AC001",
        "BRD-SNAPSHOT-INDEX-R009-AC002",
        "BRD-SNAPSHOT-INDEX-R009-AC003"
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
    "source_lines": "L5218-L5293",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R009"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "Authorization lookup may occur, but historical business context comes from Snapshot"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-SNAPSHOT-INDEX-R010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                "source_type": "SOURCE_LITERAL",
                "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                "source_lines": "L726",
                "source_section": "20. Snapshot Relationship"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
            "source_lines": "L726",
            "source_section": "20. Snapshot Relationship"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-SNAPSHOT-INDEX-R010.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                "source_type": "SOURCE_LITERAL",
                "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R010.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                "source_lines": "L726",
                "source_section": "20. Snapshot Relationship"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
            "source_lines": "L726",
            "source_section": "20. Snapshot Relationship"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
            "source_type": "SOURCE_LITERAL",
            "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R010.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
            "source_lines": "L726",
            "source_section": "20. Snapshot Relationship"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
            "source_type": "SOURCE_LITERAL",
            "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R010.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
            "source_lines": "L726",
            "source_section": "20. Snapshot Relationship"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
            "source_type": "SOURCE_LITERAL",
            "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R010.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
            "source_lines": "L726",
            "source_section": "20. Snapshot Relationship"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
            "source_type": "SOURCE_LITERAL",
            "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R010.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
            "source_lines": "L726",
            "source_section": "20. Snapshot Relationship"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
            "source_type": "SOURCE_LITERAL",
            "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R010.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
            "source_lines": "L726",
            "source_section": "20. Snapshot Relationship"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R010",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Snapshot consumption requires a mutable Runtime lookup to determine the historical decision"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID"
    ],
    "positive_oracle": [
      "The consumer can use the Snapshot without reading mutable Runtime data"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
      "source_lines": "L726",
      "source_section": "20. Snapshot Relationship"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
          "source_type": "SOURCE_LITERAL",
          "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
        },
        "identifier": "BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-SNAPSHOT-INDEX-R010.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
          "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
          "source_lines": "L726",
          "source_section": "20. Snapshot Relationship"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-SNAPSHOT-INDEX-R010.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.CONSUMER_ID",
        "FIELD.SNAPSHOT_ID",
        "FIELD.AUTHORIZATION_RESULT",
        "FIELD.RUNTIME_READS",
        "FIELD.REPLAY_RESULT"
      ],
      "producer": "BRD-SNAPSHOT-INDEX-R010.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-SNAPSHOT-INDEX-R010.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.CONSUMER_ID",
        "FIELD.SNAPSHOT_ID",
        "FIELD.AUTHORIZATION_RESULT",
        "FIELD.RUNTIME_READS",
        "FIELD.REPLAY_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-SNAPSHOT-INDEX-R010.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-SNAPSHOT-INDEX-R010.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-SNAPSHOT-INDEX-R010.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-SNAPSHOT-INDEX-R010-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID",
          "evaluator_consumed_bindings": [
            "allowed_lifecycle_states",
            "allowed_states",
            "reference",
            "registry",
            "registry_source",
            "target_id",
            "target_type"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
              "source_type": "SOURCE_LITERAL",
              "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
              "source_lines": "L726",
              "source_section": "20. Snapshot Relationship"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
              "source_type": "SOURCE_LITERAL",
              "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
              "source_lines": "L726",
              "source_section": "20. Snapshot Relationship"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "allowed_lifecycle_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-SNAPSHOT-INDEX-R010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                      "source_type": "SOURCE_LITERAL",
                      "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
                    },
                    "identifier": "BRD-SNAPSHOT-INDEX-R010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                      "source_lines": "L726",
                      "source_section": "20. Snapshot Relationship"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                  "source_lines": "L726",
                  "source_section": "20. Snapshot Relationship"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-SNAPSHOT-INDEX-R010.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                      "source_type": "SOURCE_LITERAL",
                      "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
                    },
                    "identifier": "BRD-SNAPSHOT-INDEX-R010.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                      "source_lines": "L726",
                      "source_section": "20. Snapshot Relationship"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                  "source_lines": "L726",
                  "source_section": "20. Snapshot Relationship"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R010.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                  "source_lines": "L726",
                  "source_section": "20. Snapshot Relationship"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R010.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                  "source_lines": "L726",
                  "source_section": "20. Snapshot Relationship"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R010.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                  "source_lines": "L726",
                  "source_section": "20. Snapshot Relationship"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R010.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                  "source_lines": "L726",
                  "source_section": "20. Snapshot Relationship"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R010.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                  "source_lines": "L726",
                  "source_section": "20. Snapshot Relationship"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                  "source_lines": "L726",
                  "source_section": "20. Snapshot Relationship"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                  "source_type": "SOURCE_LITERAL",
                  "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                  "source_lines": "L726",
                  "source_section": "20. Snapshot Relationship"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                "source_type": "SOURCE_LITERAL",
                "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                "source_lines": "L726",
                "source_section": "20. Snapshot Relationship"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "BRD-SNAPSHOT-INDEX-R010-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
              "source_type": "SOURCE_LITERAL",
              "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
              "source_lines": "L726",
              "source_section": "20. Snapshot Relationship"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "REFERENCE_ID"
          },
          "operator_id": "REFERENCE_TARGET_VALID",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "allowed_lifecycle_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-SNAPSHOT-INDEX-R010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                    "source_type": "SOURCE_LITERAL",
                    "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
                  },
                  "identifier": "BRD-SNAPSHOT-INDEX-R010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                    "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                    "source_lines": "L726",
                    "source_section": "20. Snapshot Relationship"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                "source_lines": "L726",
                "source_section": "20. Snapshot Relationship"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-SNAPSHOT-INDEX-R010.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                    "source_type": "SOURCE_LITERAL",
                    "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
                  },
                  "identifier": "BRD-SNAPSHOT-INDEX-R010.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                    "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                    "source_lines": "L726",
                    "source_section": "20. Snapshot Relationship"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                "source_lines": "L726",
                "source_section": "20. Snapshot Relationship"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                "source_type": "SOURCE_LITERAL",
                "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R010.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                "source_lines": "L726",
                "source_section": "20. Snapshot Relationship"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                "source_type": "SOURCE_LITERAL",
                "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R010.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                "source_lines": "L726",
                "source_section": "20. Snapshot Relationship"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                "source_type": "SOURCE_LITERAL",
                "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R010.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                "source_lines": "L726",
                "source_section": "20. Snapshot Relationship"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                "source_type": "SOURCE_LITERAL",
                "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R010.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                "source_lines": "L726",
                "source_section": "20. Snapshot Relationship"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
                "source_type": "SOURCE_LITERAL",
                "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R010.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
                "source_lines": "L726",
                "source_section": "20. Snapshot Relationship"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        }
      ],
      "boundary_cases": [
        "Authorization lookup may occur, but historical business context comes from Snapshot"
      ],
      "contract_ast_sha256": "a0181dec50a483a6c3ba515eb74c4e72bc1485050612116734b292810b14243e",
      "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R010",
      "criticality": "NORMAL",
      "disposition": "OPERATOR_REMAP_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#20. Snapshot Relationship",
            "source_type": "SOURCE_LITERAL",
            "version": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R010.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
            "source_lines": "L726",
            "source_section": "20. Snapshot Relationship"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.BRD-SNAPSHOT-INDEX-R010.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-SNAPSHOT-INDEX-R010.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.CONSUMER_ID",
          "FIELD.SNAPSHOT_ID",
          "FIELD.AUTHORIZATION_RESULT",
          "FIELD.RUNTIME_READS",
          "FIELD.REPLAY_RESULT"
        ],
        "producer": "BRD-SNAPSHOT-INDEX-R010.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-SNAPSHOT-INDEX-R010.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.CONSUMER_ID",
          "FIELD.SNAPSHOT_ID",
          "FIELD.AUTHORIZATION_RESULT",
          "FIELD.RUNTIME_READS",
          "FIELD.REPLAY_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-SNAPSHOT-INDEX-R010.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-SNAPSHOT-INDEX-R010.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-SNAPSHOT-INDEX-R010.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-155F24FDA13F9597C700",
        "P2C-C4-FX-CA53DB31AC56D84D3FF3",
        "P2C-C4-FX-8AA30A4AE990BB319AF1"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Snapshot consumption requires a mutable Runtime lookup to determine the historical decision"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-SNAPSHOT-INDEX-R010-O001",
          "obligation_text": "Snapshot có thể được nhiều hệ thống sử dụng lại mà không cần đọc dữ liệu Runtime"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-SNAPSHOT-INDEX-R010.O1.1.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-SNAPSHOT-INDEX-R010-O001"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID"
      ],
      "positive_oracles": [
        "The consumer can use the Snapshot without reading mutable Runtime data"
      ],
      "preconditions": [
        "The Snapshot and consumer authorization exist"
      ],
      "prohibitions": [
        "Snapshot consumption requires a mutable Runtime lookup to determine the historical decision"
      ],
      "requirement_id": "BRD-SNAPSHOT-INDEX-R010",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
        "source_fingerprint": "2ace6436ed635bec617a96776998d027f468d4b0ad94ca5b699e6c9b4eee0328",
        "source_lines": "L726",
        "source_section": "20. Snapshot Relationship"
      },
      "source_statement": "Snapshot có thể được nhiều hệ thống sử dụng lại mà không cần đọc dữ liệu Runtime.",
      "surrounding_source_context": "### BRD-SNAPSHOT-INDEX-R010 — Snapshot có thể được nhiều hệ thống sử dụng lại mà không cần đọc dữ liệu Runtime"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R010",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "SEMANTIC_ACCEPTANCE_RENDERER_C2",
    "runtime_status": "RUNTIME_ADAPTER_PENDING"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "ACCEPTANCE_READY",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-SNAPSHOT-INDEX-R010-AC001",
        "BRD-SNAPSHOT-INDEX-R010-AC002",
        "BRD-SNAPSHOT-INDEX-R010-AC003"
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
    "source_lines": "L5295-L6644",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R022",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "d79abaeb6233657c4b6738aba199591cc2a7c9eaa210f57b5fd9d4ce7150aa74"
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
        "BRD-SNAPSHOT-INDEX-R022-AC001",
        "BRD-SNAPSHOT-INDEX-R022-AC002",
        "BRD-SNAPSHOT-INDEX-R022-AC003"
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
    "source_lines": "L6646-L6721",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R022"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R023",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "4aff778f04dab8d22803c3f0ee5eafbe4aa757081a96fcdc9aa531a572fbecf1"
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
        "BRD-SNAPSHOT-INDEX-R023-AC001",
        "BRD-SNAPSHOT-INDEX-R023-AC002",
        "BRD-SNAPSHOT-INDEX-R023-AC003"
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
    "source_fingerprint": "4aff778f04dab8d22803c3f0ee5eafbe4aa757081a96fcdc9aa531a572fbecf1",
    "source_lines": "L6723-L6798",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R023"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R024",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "66556071f53b324dda3bf3e647124626df792e1e6b6501dc2753d693ab845d52"
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
        "BRD-SNAPSHOT-INDEX-R024-AC001",
        "BRD-SNAPSHOT-INDEX-R024-AC002",
        "BRD-SNAPSHOT-INDEX-R024-AC003"
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
    "source_fingerprint": "66556071f53b324dda3bf3e647124626df792e1e6b6501dc2753d693ab845d52",
    "source_lines": "L6800-L6875",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R024"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R025",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "f994253ff523c501f95efe06578cba7dcb1801e920a17af868a19307af060791"
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
        "BRD-SNAPSHOT-INDEX-R025-AC001",
        "BRD-SNAPSHOT-INDEX-R025-AC002",
        "BRD-SNAPSHOT-INDEX-R025-AC003"
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
    "source_fingerprint": "f994253ff523c501f95efe06578cba7dcb1801e920a17af868a19307af060791",
    "source_lines": "L6877-L6952",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R025"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R026",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "40b431be9c4a04f19a7400d54a9f474b87583716c69ecb6961ee7bc1c539e9cf"
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
        "BRD-SNAPSHOT-INDEX-R026-AC001",
        "BRD-SNAPSHOT-INDEX-R026-AC002",
        "BRD-SNAPSHOT-INDEX-R026-AC003"
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
    "source_fingerprint": "40b431be9c4a04f19a7400d54a9f474b87583716c69ecb6961ee7bc1c539e9cf",
    "source_lines": "L6954-L7029",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R026"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R027",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "4d74df792277ca7581f2422eb5dbbd4b44f7bb2a698d9e4c47f21a40bec3de2a"
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
        "BRD-SNAPSHOT-INDEX-R027-AC001",
        "BRD-SNAPSHOT-INDEX-R027-AC002",
        "BRD-SNAPSHOT-INDEX-R027-AC003"
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
    "source_fingerprint": "4d74df792277ca7581f2422eb5dbbd4b44f7bb2a698d9e4c47f21a40bec3de2a",
    "source_lines": "L7031-L7106",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R027"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R028",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "03d53939959747f058d3fa72528823613d787aeeba1a8ff4c93efe73a9190662"
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
        "BRD-SNAPSHOT-INDEX-R028-AC001",
        "BRD-SNAPSHOT-INDEX-R028-AC002",
        "BRD-SNAPSHOT-INDEX-R028-AC003"
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
    "source_fingerprint": "03d53939959747f058d3fa72528823613d787aeeba1a8ff4c93efe73a9190662",
    "source_lines": "L7108-L7183",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R028"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R029",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "8ae4a551bc35377fb01e5a7ea4c8516438119a31021fe5c6f5f120c3c76c34c0"
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
        "BRD-SNAPSHOT-INDEX-R029-AC001",
        "BRD-SNAPSHOT-INDEX-R029-AC002",
        "BRD-SNAPSHOT-INDEX-R029-AC003"
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
    "source_fingerprint": "8ae4a551bc35377fb01e5a7ea4c8516438119a31021fe5c6f5f120c3c76c34c0",
    "source_lines": "L7185-L7260",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R029"
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
      "requirement_id": "BRD-SNAPSHOT-INDEX-R030",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "b855dc4db8732531e93270b9d2cadb4763196193cb9028959e4db14d0e95aad4"
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
        "BRD-SNAPSHOT-INDEX-R030-AC001",
        "BRD-SNAPSHOT-INDEX-R030-AC002",
        "BRD-SNAPSHOT-INDEX-R030-AC003"
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
    "source_fingerprint": "b855dc4db8732531e93270b9d2cadb4763196193cb9028959e4db14d0e95aad4",
    "source_lines": "L7262-L7343",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R030"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R031",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "c76f97bfbaad890f76cec8779dd7c9f5a2398fabafa5c0f9d895a76f5dea066d"
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
        "BRD-SNAPSHOT-INDEX-R031-AC001",
        "BRD-SNAPSHOT-INDEX-R031-AC002",
        "BRD-SNAPSHOT-INDEX-R031-AC003"
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
    "source_lines": "L7345-L7420",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R031"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R032",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "51df16604a41f2f91fcc16aa188f7e3168b80466074cf44bc7d6273557ee1516"
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
        "BRD-SNAPSHOT-INDEX-R032-AC001",
        "BRD-SNAPSHOT-INDEX-R032-AC002",
        "BRD-SNAPSHOT-INDEX-R032-AC003"
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
    "source_lines": "L7422-L7497",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R032"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R033",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "0ae585019a02f6852b59af93dff6a9a5e3964e66c4690b81b382e6ba181a5be1"
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
        "BRD-SNAPSHOT-INDEX-R033-AC001",
        "BRD-SNAPSHOT-INDEX-R033-AC002",
        "BRD-SNAPSHOT-INDEX-R033-AC003"
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
    "source_fingerprint": "0ae585019a02f6852b59af93dff6a9a5e3964e66c4690b81b382e6ba181a5be1",
    "source_lines": "L7499-L7574",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R033"
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
      "requirement_id": "BRD-SNAPSHOT-INDEX-R034",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "a78f4cb29360290868ca6e8eebbb5d5fb5f4c0e77c281adabccbaa68401ccb56"
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
        "BRD-SNAPSHOT-INDEX-R034-AC001",
        "BRD-SNAPSHOT-INDEX-R034-AC002",
        "BRD-SNAPSHOT-INDEX-R034-AC003"
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
    "source_fingerprint": "a78f4cb29360290868ca6e8eebbb5d5fb5f4c0e77c281adabccbaa68401ccb56",
    "source_lines": "L7576-L7657",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R034"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R035",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "83b833875e57b8098c1346a81822e681e7add76605a3d36f9b1099b949bde61d"
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
        "BRD-SNAPSHOT-INDEX-R035-AC001",
        "BRD-SNAPSHOT-INDEX-R035-AC002",
        "BRD-SNAPSHOT-INDEX-R035-AC003"
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
    "source_fingerprint": "83b833875e57b8098c1346a81822e681e7add76605a3d36f9b1099b949bde61d",
    "source_lines": "L7659-L7734",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R035"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R036",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "ac0bcd17f2c175d50911f949195b9a6afadffd2d8a4c721809a9be20bcfaf012"
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
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R036-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R036 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R036 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R036-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R036-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R036 does not define a recovery obligation."
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
    "source_fingerprint": "ac0bcd17f2c175d50911f949195b9a6afadffd2d8a4c721809a9be20bcfaf012",
    "source_lines": "L7736-L7846",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R036"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R037",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "bdfcb5fb534c6865932cb22d62aa685105091ea18987554a75d7e120f985ddf5"
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
        "BRD-SNAPSHOT-INDEX-R037-AC001",
        "BRD-SNAPSHOT-INDEX-R037-AC002",
        "BRD-SNAPSHOT-INDEX-R037-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-SNAPSHOT-INDEX-R037-O001",
      "obligation_text": "Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R037 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R037 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R037 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R037-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R037-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R037 does not define a recovery obligation."
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
    "source_fingerprint": "bdfcb5fb534c6865932cb22d62aa685105091ea18987554a75d7e120f985ddf5",
    "source_lines": "L7848-L7956",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R037"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R038",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "d2cd21efea5ab925ababcf869c03fe134181bf5870b107f4378935d02a117ab9"
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
        "BRD-SNAPSHOT-INDEX-R038-AC001",
        "BRD-SNAPSHOT-INDEX-R038-AC002",
        "BRD-SNAPSHOT-INDEX-R038-AC003"
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
    "source_fingerprint": "d2cd21efea5ab925ababcf869c03fe134181bf5870b107f4378935d02a117ab9",
    "source_lines": "L7958-L8033",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R038"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "An Event may reference a Snapshot but cannot remove the Snapshot obligation"
    ],
    "concrete_bindings": [
      {
        "expected_outcome": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-SNAPSHOT-INDEX-R039.POLICY.OUTCOME.CONFORMING"
            ],
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
            "source_type": "SOURCE_LITERAL",
            "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R039.POLICY.OUTCOME.CONFORMING",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
            "source_lines": "L750-L755",
            "source_section": "21. Snapshot vs Event vs Audit vs History"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_OUTCOME",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.POLICY.OUTCOME.CONFORMING",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_OUTCOME"
        },
        "policy": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
            "source_type": "SOURCE_LITERAL",
            "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R039.POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
            "source_lines": "L750-L755",
            "source_section": "21. Snapshot vs Event vs Audit vs History"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "policy_inputs": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
            "source_type": "SOURCE_LITERAL",
            "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R039.POLICY_INPUTS",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
            "source_lines": "L750-L755",
            "source_section": "21. Snapshot vs Event vs Audit vs History"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.POLICY_INPUTS",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "policy_version": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
            "source_type": "SOURCE_LITERAL",
            "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R039.POLICY_VERSION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
            "source_lines": "L750-L755",
            "source_section": "21. Snapshot vs Event vs Audit vs History"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_VERSION",
            "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.POLICY_VERSION",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_VERSION"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R039",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Event payload is treated as replacement for the required Snapshot"
    ],
    "operator_composition": [
      "POLICY_OUTCOME_EQUALS"
    ],
    "positive_oracle": [
      "Event communicates occurrence while Snapshot preserves reproducible business state"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
      "source_lines": "L750-L755",
      "source_section": "21. Snapshot vs Event vs Audit vs History"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
          "source_type": "SOURCE_LITERAL",
          "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
        },
        "identifier": "BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-SNAPSHOT-INDEX-R039.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
          "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
          "source_lines": "L750-L755",
          "source_section": "21. Snapshot vs Event vs Audit vs History"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-SNAPSHOT-INDEX-R039.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.EVENT_ID",
        "FIELD.SNAPSHOT_ID",
        "FIELD.EVENT_CONTRACT",
        "FIELD.SNAPSHOT_CONTRACT",
        "FIELD.REPLAY_RESULT"
      ],
      "producer": "BRD-SNAPSHOT-INDEX-R039.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-SNAPSHOT-INDEX-R039.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.EVENT_ID",
        "FIELD.SNAPSHOT_ID",
        "FIELD.EVENT_CONTRACT",
        "FIELD.SNAPSHOT_CONTRACT",
        "FIELD.REPLAY_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-SNAPSHOT-INDEX-R039.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-SNAPSHOT-INDEX-R039.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-SNAPSHOT-INDEX-R039.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-SNAPSHOT-INDEX-R039-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS",
          "evaluator_consumed_bindings": [
            "expected_outcome",
            "policy",
            "policy_inputs",
            "policy_version"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
              "source_type": "SOURCE_LITERAL",
              "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
              "source_lines": "L750-L755",
              "source_section": "21. Snapshot vs Event vs Audit vs History"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
              "source_type": "SOURCE_LITERAL",
              "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
              "source_lines": "L750-L755",
              "source_section": "21. Snapshot vs Event vs Audit vs History"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_OUTCOME"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "expected_outcome": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-SNAPSHOT-INDEX-R039.POLICY.OUTCOME.CONFORMING"
                  ],
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
                  "source_type": "SOURCE_LITERAL",
                  "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R039.POLICY.OUTCOME.CONFORMING",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
                  "source_lines": "L750-L755",
                  "source_section": "21. Snapshot vs Event vs Audit vs History"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.POLICY.OUTCOME.CONFORMING",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "policy": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
                  "source_type": "SOURCE_LITERAL",
                  "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R039.POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
                  "source_lines": "L750-L755",
                  "source_section": "21. Snapshot vs Event vs Audit vs History"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "policy_inputs": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
                  "source_type": "SOURCE_LITERAL",
                  "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R039.POLICY_INPUTS",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
                  "source_lines": "L750-L755",
                  "source_section": "21. Snapshot vs Event vs Audit vs History"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.POLICY_INPUTS",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "policy_version": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
                  "source_type": "SOURCE_LITERAL",
                  "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R039.POLICY_VERSION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
                  "source_lines": "L750-L755",
                  "source_section": "21. Snapshot vs Event vs Audit vs History"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_VERSION",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.POLICY_VERSION",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_VERSION"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
                  "source_type": "SOURCE_LITERAL",
                  "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
                  "source_lines": "L750-L755",
                  "source_section": "21. Snapshot vs Event vs Audit vs History"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
                  "source_type": "SOURCE_LITERAL",
                  "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
                },
                "identifier": "BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
                  "source_lines": "L750-L755",
                  "source_section": "21. Snapshot vs Event vs Audit vs History"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
                "source_type": "SOURCE_LITERAL",
                "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
                "source_lines": "L750-L755",
                "source_section": "21. Snapshot vs Event vs Audit vs History"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "POLICY_OUTCOME_EQUALS"
          },
          "obligation_id": "BRD-SNAPSHOT-INDEX-R039-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
              "source_type": "SOURCE_LITERAL",
              "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
            },
            "identifier": "BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
              "source_lines": "L750-L755",
              "source_section": "21. Snapshot vs Event vs Audit vs History"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "CANONICAL_OUTCOME"
          },
          "operator_id": "POLICY_OUTCOME_EQUALS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "expected_outcome": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-SNAPSHOT-INDEX-R039.POLICY.OUTCOME.CONFORMING"
                ],
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
                "source_type": "SOURCE_LITERAL",
                "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R039.POLICY.OUTCOME.CONFORMING",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
                "source_lines": "L750-L755",
                "source_section": "21. Snapshot vs Event vs Audit vs History"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_OUTCOME",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.POLICY.OUTCOME.CONFORMING",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_OUTCOME"
            },
            "policy": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
                "source_type": "SOURCE_LITERAL",
                "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R039.POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
                "source_lines": "L750-L755",
                "source_section": "21. Snapshot vs Event vs Audit vs History"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "policy_inputs": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
                "source_type": "SOURCE_LITERAL",
                "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R039.POLICY_INPUTS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
                "source_lines": "L750-L755",
                "source_section": "21. Snapshot vs Event vs Audit vs History"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.POLICY_INPUTS",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "policy_version": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
                "source_type": "SOURCE_LITERAL",
                "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
              },
              "identifier": "BRD-SNAPSHOT-INDEX-R039.POLICY_VERSION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
                "source_lines": "L750-L755",
                "source_section": "21. Snapshot vs Event vs Audit vs History"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.POLICY_VERSION",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          }
        }
      ],
      "boundary_cases": [
        "An Event may reference a Snapshot but cannot remove the Snapshot obligation"
      ],
      "contract_ast_sha256": "7d2ed4024aff95111ed2d651b1b2edfa8b0e06b259209dae398ee2bbb74d544e",
      "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R039",
      "criticality": "CRITICAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#21. Snapshot vs Event vs Audit vs History",
            "source_type": "SOURCE_LITERAL",
            "version": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633"
          },
          "identifier": "BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-SNAPSHOT-INDEX-R039.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
            "source_lines": "L750-L755",
            "source_section": "21. Snapshot vs Event vs Audit vs History"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.BRD-SNAPSHOT-INDEX-R039.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-SNAPSHOT-INDEX-R039.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.EVENT_ID",
          "FIELD.SNAPSHOT_ID",
          "FIELD.EVENT_CONTRACT",
          "FIELD.SNAPSHOT_CONTRACT",
          "FIELD.REPLAY_RESULT"
        ],
        "producer": "BRD-SNAPSHOT-INDEX-R039.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-SNAPSHOT-INDEX-R039.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.EVENT_ID",
          "FIELD.SNAPSHOT_ID",
          "FIELD.EVENT_CONTRACT",
          "FIELD.SNAPSHOT_CONTRACT",
          "FIELD.REPLAY_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-SNAPSHOT-INDEX-R039.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-SNAPSHOT-INDEX-R039.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-SNAPSHOT-INDEX-R039.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-90AD70B61C5F5BE579C5",
        "P2C-C4-FX-8AC223E933E54395DCF0",
        "P2C-C4-FX-5986869CAA59E7EFD7CE"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Event payload is treated as replacement for the required Snapshot"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-SNAPSHOT-INDEX-R039-O001",
          "obligation_text": "Nguyên tắc: - Event không thay thế Snapshot"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-SNAPSHOT-INDEX-R039.O1.1.POLICY_OUTCOME_EQUALS"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-SNAPSHOT-INDEX-R039-O001"
        }
      ],
      "operator_composition": [
        "POLICY_OUTCOME_EQUALS"
      ],
      "positive_oracles": [
        "Event communicates occurrence while Snapshot preserves reproducible business state"
      ],
      "preconditions": [
        "Both Event and Snapshot contracts are identified"
      ],
      "prohibitions": [
        "Event payload is treated as replacement for the required Snapshot"
      ],
      "requirement_id": "BRD-SNAPSHOT-INDEX-R039",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
        "source_fingerprint": "069962b1f0514f9c71e4c64513df50567d5bbb684f3ee37832a90553b2958633",
        "source_lines": "L750-L755",
        "source_section": "21. Snapshot vs Event vs Audit vs History"
      },
      "source_statement": "Nguyên tắc: - Event không thay thế Snapshot.",
      "surrounding_source_context": "### BRD-SNAPSHOT-INDEX-R039 — Nguyên tắc: - Event không thay thế Snapshot"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-SNAPSHOT-INDEX-R039",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "SEMANTIC_ACCEPTANCE_RENDERER_C2",
    "runtime_status": "RUNTIME_ADAPTER_PENDING"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "ACCEPTANCE_READY",
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R039 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R039 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R039 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R039-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R039-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R039 does not define a recovery obligation."
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
    "source_fingerprint": "213a907e73a724f685f079362a3cc764e5a1c48f3c172636286ddcae7ec30a85",
    "source_lines": "L8035-L9012",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R039"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R040",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "4cc4224fc1131e95895f21bfec6423dd811692dace3daeaa9b3c324f197d1446"
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R040 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R040 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R040 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R040-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R040-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R040 does not define a recovery obligation."
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
    "source_fingerprint": "4cc4224fc1131e95895f21bfec6423dd811692dace3daeaa9b3c324f197d1446",
    "source_lines": "L9014-L9125",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R040"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R041",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "803d78aa0b7eddf3687d671ba4ad07cef5e7094ad53a5a09bb441aaae5fc1aa5"
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R041 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R041 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R041 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R041-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R041-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R041 does not define a recovery obligation."
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
    "source_fingerprint": "803d78aa0b7eddf3687d671ba4ad07cef5e7094ad53a5a09bb441aaae5fc1aa5",
    "source_lines": "L9127-L9238",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R041"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-SNAPSHOT-INDEX-R042",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "c39b552ec4e5ecce5c80fbadcb3caa99da8ba881b34a812c5015b4fb294e730c"
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R042 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R042 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R042 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R042-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-SNAPSHOT-INDEX-R042-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-SNAPSHOT-INDEX-R042 does not define a recovery obligation."
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
    "source_fingerprint": "c39b552ec4e5ecce5c80fbadcb3caa99da8ba881b34a812c5015b4fb294e730c",
    "source_lines": "L9240-L9351",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-SNAPSHOT-INDEX-R042"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-EP-001",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "15198451d478e5f4b85819554a4fe750a357896153771ea9354bad66f9f390f4"
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
        "SNP-EP-001-AC001",
        "SNP-EP-001-AC002",
        "SNP-EP-001-AC003"
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
    "source_fingerprint": "15198451d478e5f4b85819554a4fe750a357896153771ea9354bad66f9f390f4",
    "source_lines": "L9353-L9428",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-EP-001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-EP-002",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "8643d5feafd228d459b7f0d2058484c769d1bf974b6e24d6576dc3ba9a26b3f3"
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
        "SNP-EP-002-AC001",
        "SNP-EP-002-AC002",
        "SNP-EP-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-EP-002-O001",
      "obligation_text": "Snapshot là Immutable"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-EP-002 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-EP-002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-EP-002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "SNP-EP-002-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "SNP-EP-002-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-EP-002 does not define a recovery obligation."
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
    "source_fingerprint": "8643d5feafd228d459b7f0d2058484c769d1bf974b6e24d6576dc3ba9a26b3f3",
    "source_lines": "L9430-L9538",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-EP-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-EP-003",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "349f26e573e66d01d69d3959c82cc682917d382c77cb156795a136b1fba3fa58"
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
        "SNP-EP-003-AC001",
        "SNP-EP-003-AC002",
        "SNP-EP-003-AC003"
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
    "source_fingerprint": "349f26e573e66d01d69d3959c82cc682917d382c77cb156795a136b1fba3fa58",
    "source_lines": "L9540-L9615",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-EP-003"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "Later context changes create a new Snapshot and do not mutate historical context"
    ],
    "concrete_bindings": [
      {
        "actual_set": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
            "source_type": "SOURCE_LITERAL",
            "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
          },
          "identifier": "RESOLVED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.SNP-EP-004.RESOLVED.COLLECTION",
          "origin": {
            "origin_id": "YSIM.SNP-EP-004.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
            "source_lines": "L871-L874",
            "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "OBSERVE.SNP-EP-004.RESOLVED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
        },
        "required_members": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
            "source_type": "SOURCE_LITERAL",
            "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
          },
          "identifier": "GOVERNED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.SNP-EP-004.GOVERNED.COLLECTION",
          "origin": {
            "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
            "source_lines": "L871-L874",
            "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "RESOLVE.SNP-EP-004.GOVERNED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.SNP-EP-004",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "A required input or version is absent and replay differs"
    ],
    "operator_composition": [
      "SET_CONTAINS"
    ],
    "positive_oracle": [
      "Snapshot contains the complete Business Context needed to reproduce the decision"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
      "source_lines": "L871-L874",
      "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
          "source_type": "SOURCE_LITERAL",
          "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
        },
        "identifier": "SNP-EP-004.SNP-EP-004.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "SNP-EP-004.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
          "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
          "source_lines": "L871-L874",
          "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.SNP-EP-004.SNP-EP-004.SNP-EP-004.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "SNP-EP-004.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.SNAPSHOT_ID",
        "FIELD.DECISION_ID",
        "FIELD.BUSINESS_CONTEXT_FIELDS",
        "FIELD.POLICY_VERSIONS",
        "FIELD.REPLAY_RESULT"
      ],
      "producer": "SNP-EP-004.EVIDENCE.PRODUCER",
      "required_collection_origin": "SNP-EP-004.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.SNAPSHOT_ID",
        "FIELD.DECISION_ID",
        "FIELD.BUSINESS_CONTEXT_FIELDS",
        "FIELD.POLICY_VERSIONS",
        "FIELD.REPLAY_RESULT"
      ],
      "required_values_or_hashes": [
        "SNP-EP-004.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "SNP-EP-004.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "SNP-EP-004.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "SNP-EP-004-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "SNP-EP-004.O1.1.SET_CONTAINS",
          "evaluator_consumed_bindings": [
            "actual_set",
            "required_members"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
              "source_type": "SOURCE_LITERAL",
              "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
            },
            "identifier": "SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
              "source_lines": "L871-L874",
              "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.SNP-EP-004.SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
                },
                "identifier": "SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
                  "source_lines": "L871-L874",
                  "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.SNP-EP-004.SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
              "source_lines": "L871-L874",
              "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_set": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
                },
                "identifier": "RESOLVED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.SNP-EP-004.RESOLVED.COLLECTION",
                "origin": {
                  "origin_id": "YSIM.SNP-EP-004.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
                  "source_lines": "L871-L874",
                  "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "OBSERVE.SNP-EP-004.RESOLVED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
              },
              "required_members": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
                },
                "identifier": "GOVERNED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.SNP-EP-004.GOVERNED.COLLECTION",
                "origin": {
                  "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
                  "source_lines": "L871-L874",
                  "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "RESOLVE.SNP-EP-004.GOVERNED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
              }
            },
            "comparison": {
              "expected": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
                      "source_type": "SOURCE_LITERAL",
                      "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
                    },
                    "identifier": "SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
                      "source_lines": "L871-L874",
                      "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.SNP-EP-004.SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
                  "source_lines": "L871-L874",
                  "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "observed": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
                      "source_type": "SOURCE_LITERAL",
                      "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
                    },
                    "identifier": "SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                      "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
                      "source_lines": "L871-L874",
                      "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "OBSERVE.SNP-EP-004.SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
                  "source_lines": "L871-L874",
                  "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
                "source_type": "SOURCE_LITERAL",
                "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
              },
              "identifier": "SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
                "source_lines": "L871-L874",
                "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.SNP-EP-004.SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "SET_CONTAINS"
          },
          "obligation_id": "SNP-EP-004-O001",
          "observed_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
                  "source_type": "SOURCE_LITERAL",
                  "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
                },
                "identifier": "SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                  "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
                  "source_lines": "L871-L874",
                  "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.SNP-EP-004.SNP-EP-004.SNP-EP-004.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
              "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
              "source_lines": "L871-L874",
              "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "operator_id": "SET_CONTAINS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_set": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
                "source_type": "SOURCE_LITERAL",
                "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
              },
              "identifier": "RESOLVED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.SNP-EP-004.RESOLVED.COLLECTION",
              "origin": {
                "origin_id": "YSIM.SNP-EP-004.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
                "source_lines": "L871-L874",
                "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "OBSERVE.SNP-EP-004.RESOLVED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
            },
            "required_members": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
                "source_type": "SOURCE_LITERAL",
                "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
              },
              "identifier": "GOVERNED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.SNP-EP-004.GOVERNED.COLLECTION",
              "origin": {
                "origin_id": "SNP-EP-004.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
                "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
                "source_lines": "L871-L874",
                "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "RESOLVE.SNP-EP-004.GOVERNED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Later context changes create a new Snapshot and do not mutate historical context"
      ],
      "contract_ast_sha256": "9d06412faf3293473a43214a361a66233655c1e82f40828371dbae223f5d6a3a",
      "contract_id": "P2C.C4.CONTRACT.SNP-EP-004",
      "criticality": "NORMAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-SNAPSHOT-INDEX.md#25. Enterprise Snapshot Principles > SNP-EP-004",
            "source_type": "SOURCE_LITERAL",
            "version": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926"
          },
          "identifier": "SNP-EP-004.SNP-EP-004.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "SNP-EP-004.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
            "source_lines": "L871-L874",
            "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.SNP-EP-004.SNP-EP-004.SNP-EP-004.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "SNP-EP-004.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.SNAPSHOT_ID",
          "FIELD.DECISION_ID",
          "FIELD.BUSINESS_CONTEXT_FIELDS",
          "FIELD.POLICY_VERSIONS",
          "FIELD.REPLAY_RESULT"
        ],
        "producer": "SNP-EP-004.EVIDENCE.PRODUCER",
        "required_collection_origin": "SNP-EP-004.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.SNAPSHOT_ID",
          "FIELD.DECISION_ID",
          "FIELD.BUSINESS_CONTEXT_FIELDS",
          "FIELD.POLICY_VERSIONS",
          "FIELD.REPLAY_RESULT"
        ],
        "required_values_or_hashes": [
          "SNP-EP-004.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "SNP-EP-004.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "SNP-EP-004.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-R2-FX-42EFF4E7AE8085FED5C4",
        "P2C-C4-R2-FX-986B43BA6B3ABBBB86E7",
        "P2C-C4-R2-FX-05AA3A76E5C3821D7DDD"
      ],
      "high_risk_audit_subset": false,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "A required input or version is absent and replay differs"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "SNP-EP-004-O001",
          "obligation_text": "Snapshot phải chứa đầy đủ Business Context để tái hiện quyết định nghiệp vụ"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "SNP-EP-004.O1.1.SET_CONTAINS"
          ],
          "coverage_count": 1,
          "obligation_id": "SNP-EP-004-O001"
        }
      ],
      "operator_composition": [
        "SET_CONTAINS"
      ],
      "positive_oracles": [
        "Snapshot contains the complete Business Context needed to reproduce the decision"
      ],
      "preconditions": [
        "The decision inputs and effective policy versions are known"
      ],
      "prohibitions": [
        "A required input or version is absent and replay differs"
      ],
      "requirement_id": "SNP-EP-004",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
        "source_fingerprint": "806fd37857b266e16fa974ddd360853695928305a7b2f177f13bab7db6ea1926",
        "source_lines": "L871-L874",
        "source_section": "25. Enterprise Snapshot Principles > SNP-EP-004"
      },
      "source_statement": "Snapshot phải chứa đầy đủ Business Context để tái hiện quyết định nghiệp vụ.",
      "surrounding_source_context": "## SNP-EP-004\n\nSnapshot phải chứa đầy đủ Business Context để tái hiện quyết định nghiệp vụ.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.SNP-EP-004",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "SEMANTIC_ACCEPTANCE_RENDERER_C2",
    "runtime_status": "RUNTIME_ADAPTER_PENDING"
  },
  "acceptance_rationale": null,
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "ACCEPTANCE_READY",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "SNP-EP-004-AC001",
        "SNP-EP-004-AC002",
        "SNP-EP-004-AC003"
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
    "source_fingerprint": "f8ef82dd3d2b835a0c688cf111da467f9d4abbb027c87e2a93045430b9388dc7",
    "source_lines": "L9617-L10411",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-EP-004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-EP-005",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "9f7234ff8adb1ec2097645dd497c9109d7ca48c4b807a4c59944631f85c751d0"
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
        "SNP-EP-005-AC001",
        "SNP-EP-005-AC002",
        "SNP-EP-005-AC003"
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
    "source_fingerprint": "9f7234ff8adb1ec2097645dd497c9109d7ca48c4b807a4c59944631f85c751d0",
    "source_lines": "L10413-L10488",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-EP-005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-EP-006",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "09137b2a16c1847f9203fc4635b366110ab36d6b5ea4bc0bc494d1577ae4f7cb"
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
        "SNP-EP-006-AC001",
        "SNP-EP-006-AC002",
        "SNP-EP-006-AC003"
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
    "source_fingerprint": "09137b2a16c1847f9203fc4635b366110ab36d6b5ea4bc0bc494d1577ae4f7cb",
    "source_lines": "L10490-L10565",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-EP-006"
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
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "Alias evidence is inherited from the canonical target; the alias is not an acceptance unit.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
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
    "source_fingerprint": "2abaccdbf807675f50262550bca8de9a6cd314d04b4873cf7303b1529c36c021",
    "source_lines": "L10567-L10615",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-EP-007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-EP-008",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "07d1e0b11e55354bb20bdf8219d29da5050163a3b11eda48afb7b216b7c0e3c7"
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
        "SNP-EP-008-AC001",
        "SNP-EP-008-AC002",
        "SNP-EP-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-EP-008-O001",
      "obligation_text": "Snapshot hỗ trợ Audit và Regulatory Compliance"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-EP-008 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-EP-008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-EP-008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "SNP-EP-008-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "SNP-EP-008-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-EP-008 does not define a recovery obligation."
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
    "source_fingerprint": "07d1e0b11e55354bb20bdf8219d29da5050163a3b11eda48afb7b216b7c0e3c7",
    "source_lines": "L10617-L10725",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-EP-008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-EP-009",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "c469f63270652fb0c1a34d0e003943b1b895cbbd5578b2b9518fc8ff9dde418f"
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
        "SNP-EP-009-AC001",
        "SNP-EP-009-AC002",
        "SNP-EP-009-AC003"
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
    "source_fingerprint": "c469f63270652fb0c1a34d0e003943b1b895cbbd5578b2b9518fc8ff9dde418f",
    "source_lines": "L10727-L10802",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-EP-009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-EP-010",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "9841f64d2eb097c3d413b80d6171844eba6da21954a5b8f03ba063da04b78def"
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
        "SNP-EP-010-AC001",
        "SNP-EP-010-AC002",
        "SNP-EP-010-AC003"
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
    "source_fingerprint": "9841f64d2eb097c3d413b80d6171844eba6da21954a5b8f03ba063da04b78def",
    "source_lines": "L10804-L10879",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-EP-010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-P01",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "699f6dffc39898c0a6f88e428f249724258b40fe5f9d8191d1880ce7ac8d4068"
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
        "SNP-P01-AC001",
        "SNP-P01-AC002",
        "SNP-P01-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P01-O001",
      "obligation_text": "Snapshot là bất biến"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-P01 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-P01 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-P01 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "SNP-P01-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "SNP-P01-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-P01 does not define a recovery obligation."
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
    "source_fingerprint": "699f6dffc39898c0a6f88e428f249724258b40fe5f9d8191d1880ce7ac8d4068",
    "source_lines": "L10881-L10989",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-P01"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-P02",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "1351af836702077ecd2eaa3bf38060f7cec68337ee63eb3292dd2944fcfc0fa2"
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
        "SNP-P02-AC001",
        "SNP-P02-AC002",
        "SNP-P02-AC003"
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
    "source_fingerprint": "1351af836702077ecd2eaa3bf38060f7cec68337ee63eb3292dd2944fcfc0fa2",
    "source_lines": "L10991-L11066",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-P02"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-P03",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "ae48312e6dcf717e2bff289c804efc953e17614d9f9e0e1ad4ad4d42bc37c9a7"
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
        "SNP-P03-AC001",
        "SNP-P03-AC002",
        "SNP-P03-AC003"
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
    "source_fingerprint": "ae48312e6dcf717e2bff289c804efc953e17614d9f9e0e1ad4ad4d42bc37c9a7",
    "source_lines": "L11068-L11143",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-P03"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-P04",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "1da06c6c7eccc11a4d9b94c4e1f9679f4a00ef44ed3a42b9594da49a17790bbc"
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
        "SNP-P04-AC001",
        "SNP-P04-AC002",
        "SNP-P04-AC003"
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
    "source_fingerprint": "1da06c6c7eccc11a4d9b94c4e1f9679f4a00ef44ed3a42b9594da49a17790bbc",
    "source_lines": "L11145-L11220",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-P04"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-P05",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "6e308ffa3b71a4920a95c79ca6daa165cdaf57065e6f83e9ee58b031927e575b"
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
        "SNP-P05-AC001",
        "SNP-P05-AC002",
        "SNP-P05-AC003"
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
    "source_fingerprint": "6e308ffa3b71a4920a95c79ca6daa165cdaf57065e6f83e9ee58b031927e575b",
    "source_lines": "L11222-L11297",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-P05"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-P06",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "c5e5059ec400eb32f553676b52ffb0683e5fbf1ebb67ee615c3c155cea412192"
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
        "SNP-P06-AC001",
        "SNP-P06-AC002",
        "SNP-P06-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P06-O001",
      "obligation_text": "Snapshot hỗ trợ Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-P06 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-P06 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-P06 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "SNP-P06-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "SNP-P06-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-P06 does not define a recovery obligation."
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
    "source_fingerprint": "c5e5059ec400eb32f553676b52ffb0683e5fbf1ebb67ee615c3c155cea412192",
    "source_lines": "L11299-L11407",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-P06"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "SNP-P07",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "d37981147077bb44d1af1c4ae5a4c1ee292210ed141dd429b642e31b7912c20e"
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
      "applicability": "APPLICABLE",
      "criterion_references": [
        "SNP-P07-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-P07 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-P07 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "SNP-P07-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "SNP-P07-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "SNP-P07 does not define a recovery obligation."
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
    "source_fingerprint": "d37981147077bb44d1af1c4ae5a4c1ee292210ed141dd429b642e31b7912c20e",
    "source_lines": "L11409-L11521",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-P07"
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
      "requirement_id": "SNP-P08",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "source_fingerprint": "89187490bce29468622900c87c16023e8044a57cce155efeb06c539ebe3a5c99"
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
        "SNP-P08-AC001",
        "SNP-P08-AC005",
        "SNP-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P08-O001",
      "obligation_text": "Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới phải trải qua: Architecture Review"
    },
    {
      "acceptance_criterion_references": [
        "SNP-P08-AC002",
        "SNP-P08-AC005",
        "SNP-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P08-O002",
      "obligation_text": "Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới phải trải qua: Approval"
    },
    {
      "acceptance_criterion_references": [
        "SNP-P08-AC003",
        "SNP-P08-AC005",
        "SNP-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P08-O003",
      "obligation_text": "Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới phải trải qua: Versioning"
    },
    {
      "acceptance_criterion_references": [
        "SNP-P08-AC004",
        "SNP-P08-AC005",
        "SNP-P08-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "SNP-P08-O004",
      "obligation_text": "Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới phải trải qua: Traceability"
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
    "source_fingerprint": "89187490bce29468622900c87c16023e8044a57cce155efeb06c539ebe3a5c99",
    "source_lines": "L11523-L11634",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > SNP-P08"
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
