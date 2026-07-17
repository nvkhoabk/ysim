---
document_code: "BRD-WS-15"
document_id: "BRD-WS-15"
title: "Integration Platform, API Gateway & Event Bus"
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

# BRD Workshop 15

# Integration Platform, API Gateway & Event Bus

---

# 1. Workshop Objective

Workshop này xác định toàn bộ nền tảng Integration của YSim.

Bao gồm:

- API Gateway
- Supplier Gateway
- Payment Gateway
- Partner Gateway
- Notification Gateway
- Integration Platform
- Connector
- Adapter
- Canonical Data Model
- Canonical Event Model
- Event Bus
- Business Event
- Event Contract
- Event Subscription
- Callback
- Webhook
- Integration Monitoring
- Integration Health
- Message Queue
- Dead Letter Queue
- Business Service Registry
- Connector Routing
- Integration Policy

Workshop này không bao gồm:

- Identity & Security
- Monitoring Infrastructure
- Audit Platform

(Các nội dung trên sẽ được triển khai trong các Workshop tiếp theo.)

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| Integration Connector | Master |
| Connector Profile | Master |
| Connector Policy | Master |
| Connector Capability | Master |
| Connector Routing Rule | Master |
| API Definition | Master |
| API Endpoint | Master |
| Event Definition | Master |
| Event Contract | Master |
| Event Subscription | Master |
| Event Publication | Transaction |
| Callback | Transaction |
| Webhook Endpoint | Master |
| Integration Session | Transaction |
| Message Queue | Master |
| Queue Message | Transaction |
| Dead Letter Message | Transaction |
| Business Service Registry | Master |

---

# 3. Integration Architecture

YSim sử dụng một Integration Platform thống nhất.

Kiến trúc tổng thể:

```text
Business Domain

↓

API Gateway

↓

------------------------------------------

Supplier Gateway

Payment Gateway

Partner Gateway

Notification Gateway

↓

Connector

↓

Adapter

↓

External Platform
```

Business Domain không được tích hợp trực tiếp với hệ thống bên ngoài.

Toàn bộ Integration phải đi qua Gateway, Connector và Adapter.

---

# 4. Integration Model

Integration Platform hỗ trợ đầy đủ các hình thức tích hợp:

- REST API
- Webhook
- Event Bus
- Message Queue
- Batch Import
- Batch Export

Kiến trúc được thiết kế mở để bổ sung các giao thức tích hợp mới trong tương lai.

---

# 5. API Gateway

API Gateway là thành phần bắt buộc của Platform.

API Gateway chịu trách nhiệm:

- Authentication
- Authorization
- Request Validation
- Response Normalization
- API Routing
- API Versioning
- Rate Limiting
- Logging

Business Domain không gọi trực tiếp Connector.

---

# 6. Connector

Connector là Business Object.

Connector đại diện cho kết nối với hệ thống bên ngoài.

Ví dụ:

- Gigago Connector
- WorldeSIM Connector
- GoHub Connector
- OnePay Connector
- Stripe Connector
- PayPal Connector
- Airwallex Connector

Một Connector có thể có nhiều Profile.

Connector không chứa Business Logic.

---

# 7. Adapter

Connector và Adapter là hai thành phần độc lập.

Connector chịu trách nhiệm:

- Authentication
- Connection
- Session
- Retry
- Health Check

Adapter chịu trách nhiệm:

- Mapping
- Transformation
- Data Conversion
- Canonical Conversion
- Response Normalization

Business Domain chỉ làm việc với Canonical Model.

---

# 8. Gateway Separation

Integration Platform được chia thành nhiều Gateway độc lập.

Bao gồm:

- API Gateway
- Supplier Gateway
- Payment Gateway
- Partner Gateway
- Notification Gateway

Các Gateway hoạt động độc lập.

Mỗi Gateway có thể có nhiều Connector.

Kiến trúc hỗ trợ mở rộng thêm Gateway mới khi cần.

---

# 9. Business Event

Business Event là Business Object.

Mọi Business Domain đều Publish Business Event.

Ví dụ:

- OrderCreated
- OrderConfirmed
- PaymentSucceeded
- PaymentFailed
- PurchaseOrderCreated
- InventoryReserved
- InventoryAllocated
- FulfillmentCompleted
- TicketCreated
- SettlementConfirmed

Business Event là cơ chế giao tiếp chuẩn giữa các Domain.

---

# 10. Event Subscription

Business Domain đăng ký Subscribe Business Event.

Publisher không biết Subscriber.

Event Bus chịu trách nhiệm:

- Routing
- Delivery
- Retry
- Ordering
- Dead Letter Queue

Subscriber có thể đăng ký hoặc hủy đăng ký Event thông qua Event Subscription.

------

# 11. Event Version

Business Event hỗ trợ Version.

Event Definition và Event Contract được quản lý theo Version độc lập.

Một Event mới không được phép phá vỡ khả năng tương thích ngược (Backward Compatibility) nếu vẫn còn Subscriber sử dụng Version cũ.

Event Version được sử dụng để:

- Quản lý thay đổi Schema
- Quản lý tương thích
- Hỗ trợ nâng cấp từng bước
- Theo dõi vòng đời của Event

---

# 12. Event Delivery

Integration Platform hỗ trợ nhiều cơ chế Event Delivery.

Bao gồm:

- At Most Once
- At Least Once
- Exactly Once

Mặc định toàn Platform sử dụng:

**At Least Once**

Các Business Event quan trọng có thể cấu hình Delivery Strategy riêng.

Event Delivery được cấu hình thông qua Integration Policy.

---

# 13. Idempotency

API và Event đều hỗ trợ Idempotency.

Idempotency Key được sử dụng để tránh xử lý trùng lặp.

Idempotency áp dụng cho:

- REST API
- Callback
- Webhook
- Business Event
- Queue Message

Business Domain không được tạo dữ liệu trùng khi nhận cùng một Request hoặc Event nhiều lần.

---

# 14. Retry Policy

Retry Policy là một phần của Connector Policy.

Retry được cấu hình.

Bao gồm:

- Retry Count
- Retry Interval
- Retry Strategy
- Exponential Backoff
- Maximum Retry Duration

Retry Policy có thể khác nhau giữa các Connector.

Ví dụ:

- Supplier Connector
- Payment Connector
- Notification Connector

Retry không được Hard-code.

---

# 15. Dead Letter Queue

Dead Letter Queue (DLQ) là Business Object.

Message sau khi Retry không thành công sẽ được chuyển vào DLQ.

DLQ hỗ trợ:

- Manual Review
- Manual Retry
- Automatic Retry
- Archive
- Delete

DLQ phải lưu đầy đủ:

- Message
- Event
- Connector
- Error
- Retry History
- Failure Reason

DLQ phục vụ vận hành và hỗ trợ kỹ thuật.

---

# 16. Callback

Callback là Business Object.

Callback được sử dụng cho:

- Payment Callback
- Supplier Callback
- Notification Callback
- Partner Callback

Callback luôn được:

- Authenticate
- Validate
- Audit
- Idempotent Check

Callback History được lưu đầy đủ để phục vụ đối soát và xử lý sự cố.

---

# 17. Webhook

Webhook là Business Object.

Webhook hỗ trợ:

- Internal Webhook
- Organization Webhook
- External Partner Webhook

Webhook Definition bao gồm:

- Endpoint
- Secret
- Version
- Retry Policy
- Signature
- Timeout

Webhook có thể Publish Business Event sau khi xử lý thành công.

---

# 18. API Version

API hỗ trợ Version.

Ví dụ:

- v1
- v2
- v3

API Version được quản lý độc lập với Business Domain.

Một API mới không được làm ảnh hưởng đến các Client đang sử dụng Version cũ.

Deprecation Policy phải được công bố trước khi loại bỏ một API Version.

---

# 19. Connector Profile

Connector Profile là Business Object.

Một Connector có thể có nhiều Profile.

Ví dụ:

- Mock
- Sandbox
- UAT
- Production

Mỗi Profile có thể có:

- Endpoint
- Authentication
- Credential
- Timeout
- Retry Policy
- Certificate
- Environment

Business Domain không cần biết Connector đang sử dụng Profile nào.

Runtime sẽ tự động lựa chọn Profile phù hợp.

---

# 20. Message Queue

Message Queue là Business Object.

Queue được tổ chức theo nghiệp vụ.

Ví dụ:

- Payment Queue
- Procurement Queue
- Inventory Queue
- Fulfillment Queue
- Notification Queue
- Settlement Queue
- Reporting Queue
- Marketing Queue

Mỗi Queue có thể cấu hình:

- Worker
- Concurrency
- Retry Policy
- DLQ
- Ordering Strategy
- Monitoring

Queue được quản lý tập trung bởi Integration Platform.

------

# 21. Queue Ordering

Message Queue hỗ trợ nhiều cơ chế xử lý.

Bao gồm:

- FIFO
- Priority Queue
- Partition Queue

Các Queue quan trọng được ưu tiên xử lý trước.

Ví dụ:

- Payment Queue
- Fulfillment Queue
- Procurement Queue

được ưu tiên cao hơn:

- Marketing Queue
- Analytics Queue
- Reporting Queue

Queue Ordering được cấu hình thông qua Queue Policy.

---

# 22. Integration Monitoring

Integration Platform hỗ trợ Integration Monitoring.

Monitoring bao gồm:

- Success Rate
- Failure Rate
- Retry Count
- Response Time
- Throughput
- Queue Length
- Pending Message
- DLQ Size
- Connector Availability

Monitoring được hiển thị trên Dashboard vận hành.

---

# 23. Integration Health

Integration Health được quản lý cho từng Connector.

Health Status bao gồm:

- Online
- Warning
- Offline
- Maintenance

Health được tính toán dựa trên:

- Success Rate
- Error Rate
- Response Time
- Timeout
- Circuit Breaker Status

Connector Health được sử dụng trong Routing Decision.

---

# 24. Rate Limiting

API Gateway hỗ trợ Rate Limiting.

Bao gồm:

- Request Per Second
- Burst Limit
- Daily Quota
- Monthly Quota

Rate Limit có thể áp dụng theo:

- API
- Organization
- User
- API Key
- Partner

Rate Limit được cấu hình.

Không Hard-code.

---

# 25. Circuit Breaker

Integration Platform hỗ trợ Circuit Breaker.

Connector khi phát sinh lỗi liên tục sẽ chuyển sang trạng thái:

```text
Closed

↓

Open

↓

Half Open

↓

Closed
```

Circuit Breaker giúp:

- Bảo vệ Platform
- Giảm Retry vô ích
- Tăng khả năng phục hồi

Circuit Breaker được cấu hình thông qua Connector Policy.

---

# 26. Scheduler Event

Scheduler có thể Publish Business Event.

Ví dụ:

- Product Synchronization
- Inventory Synchronization
- Exchange Rate Update
- Settlement Generation
- Report Generation
- Cleanup
- Health Check

Scheduler không gọi trực tiếp Business Service.

Scheduler luôn Publish Event.

---

# 27. Business Service Registry

Business Service Registry là Business Object.

Registry quản lý:

- Business Service
- API
- Published Event
- Consumed Event
- Dependency
- Owner
- Version

Registry phục vụ:

- Documentation
- Discovery
- Dependency Analysis
- Integration Governance

---

# 28. Canonical Data Model

Business Domain chỉ làm việc với Canonical Data Model.

Adapter chịu trách nhiệm Mapping:

```text
External Model

↓

Canonical Model

↓

Business Domain
```

Canonical Data Model giúp:

- Chuẩn hóa dữ liệu
- Không phụ thuộc Supplier
- Không phụ thuộc Payment Gateway
- Giảm Business Logic trong Adapter

---

# 29. Canonical Event Model

Business Domain chỉ xử lý Canonical Event.

Ví dụ:

```text
Stripe Payment Success

↓

OnePay Payment Success

↓

Airwallex Payment Success

↓

PaymentSucceeded
```

Business Domain không cần biết Event đến từ hệ thống nào.

Canonical Event là ngôn ngữ giao tiếp thống nhất của Platform.

---

# 30. Connector Policy

Connector Policy là Business Object.

Connector Policy quản lý:

- Timeout
- Retry Policy
- Circuit Breaker
- Rate Limit
- Concurrency
- Health Threshold
- Queue Priority

Policy được cấu hình.

Không Hard-code.

---

# 31. Connector Routing Rule

Connector Routing Rule là Business Object.

Routing Rule quyết định Connector sẽ được sử dụng.

Routing có thể dựa trên:

- Priority
- Connector Health
- Cost
- Country
- Region
- Inventory Availability
- Commercial Agreement
- Capability

Routing Rule được cấu hình.

Business Domain không quyết định Connector.

---

# 32. Integration Capability Matrix

Mỗi Connector phải khai báo Capability.

Ví dụ:

Supplier Connector:

- Product Synchronization
- Purchase
- Inventory
- Fulfillment
- Status Check
- Revoke
- Refund

Payment Connector:

- Payment
- Refund
- Callback
- Query
- Settlement File

Business Domain lựa chọn Connector dựa trên Capability.

---

# 33. Connector Lifecycle

Connector hỗ trợ Lifecycle.

```text
Draft

↓

Configured

↓

Validated

↓

Testing

↓

Active

↓

Suspended

↓

Retired
```

Lifecycle được quản lý độc lập với Connector Profile.

Connector chỉ được phép xử lý giao dịch khi ở trạng thái Active.

---

# 34. Connector Runtime Profile

Connector hỗ trợ nhiều Runtime Profile.

Bao gồm:

- Mock
- Sandbox
- UAT
- Production

Runtime Profile xác định:

- Endpoint
- Authentication
- Credential
- Certificate
- Timeout
- Retry Policy

Business Domain không cần biết Runtime Profile đang được sử dụng.

Runtime sẽ tự động lựa chọn Profile theo Environment.

Điều này cho phép:

- Phát triển
- Kiểm thử
- Demo
- UAT
- Production

sử dụng cùng một Business Logic.

------

# 35. Business Decisions (Locked)

## BD-15-001

Integration Platform hỗ trợ đầy đủ:

- REST API
- Webhook
- Event Bus
- Message Queue
- Batch Import
- Batch Export

---

## BD-15-002

API Gateway là thành phần bắt buộc.

Business Domain không được tích hợp trực tiếp với hệ thống bên ngoài.

---

## BD-15-003

Connector là Business Object.

Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài.

Business Logic không được đặt trong Connector.

---

## BD-15-004

Connector và Adapter là hai thành phần độc lập.

Connector quản lý:

- Connection
- Authentication
- Session
- Retry
- Health

Adapter quản lý:

- Mapping
- Transformation
- Canonical Conversion

---

## BD-15-005

Integration Platform được chia thành các Gateway độc lập:

- API Gateway
- Supplier Gateway
- Payment Gateway
- Partner Gateway
- Notification Gateway

Gateway có thể mở rộng trong tương lai.

---

## BD-15-006

Business Event là Business Object.

Mọi Business Domain đều Publish Business Event.

---

## BD-15-007

Business Domain đăng ký Subscribe Business Event.

Publisher không biết Subscriber.

Event Bus chịu trách nhiệm Routing và Delivery.

---

## BD-15-008

Business Event hỗ trợ Version.

Backward Compatibility phải được đảm bảo.

---

## BD-15-009

Event Delivery hỗ trợ:

- At Most Once
- At Least Once
- Exactly Once

Mặc định sử dụng:

**At Least Once**

---

## BD-15-010

API và Business Event đều hỗ trợ Idempotency.

---

## BD-15-011

Retry Policy được cấu hình.

Bao gồm:

- Retry Count
- Retry Interval
- Retry Strategy
- Exponential Backoff

---

## BD-15-012

Dead Letter Queue là Business Object.

Message Retry thất bại sẽ được chuyển vào DLQ.

---

## BD-15-013

Callback là Business Object.

Bao gồm:

- Payment Callback
- Supplier Callback
- Notification Callback
- Partner Callback

---

## BD-15-014

Webhook hỗ trợ:

- Internal
- Organization
- External Partner

---

## BD-15-015

API hỗ trợ Version.

API Version được quản lý độc lập.

---

## BD-15-016

Connector hỗ trợ nhiều Runtime Profile:

- Mock
- Sandbox
- UAT
- Production

---

## BD-15-017

Message Queue là Business Object.

Queue được tách theo từng nghiệp vụ.

---

## BD-15-018

Queue hỗ trợ:

- FIFO
- Priority
- Partition

Queue liên quan Payment, Procurement và Fulfillment có độ ưu tiên cao hơn.

---

## BD-15-019

Integration Platform hỗ trợ:

- Monitoring
- Health Check
- Retry
- DLQ
- Queue Monitoring

---

## BD-15-020

API Gateway hỗ trợ:

- Rate Limiting
- Burst
- Quota

---

## BD-15-021

Connector hỗ trợ Circuit Breaker.

---

## BD-15-022

Scheduler có thể Publish Business Event.

---

## BD-15-023

Business Service Registry là Business Object.

Registry quản lý:

- Service
- API
- Published Event
- Consumed Event
- Dependency
- Owner
- Version

---

## BD-15-024

Business Domain chỉ làm việc với Canonical Data Model.

---

## BD-15-025

Business Domain chỉ xử lý Canonical Event Model.

---

## BD-15-026

Connector Policy là Business Object.

Connector Policy quản lý:

- Timeout
- Retry
- Circuit Breaker
- Rate Limit
- Concurrency
- Queue Priority
- Health Threshold

---

## BD-15-027

Connector Routing Rule là Business Object.

Routing Rule được cấu hình.

Business Domain không quyết định Connector.

---

## BD-15-028

Connector phải khai báo Capability Matrix.

Business Domain lựa chọn Connector dựa trên Capability.

---

## BD-15-029

Connector hỗ trợ Lifecycle:

- Draft
- Configured
- Validated
- Testing
- Active
- Suspended
- Retired

---

## BD-15-030

Connector Runtime Profile hỗ trợ:

- Mock
- Sandbox
- UAT
- Production

Runtime tự động lựa chọn Profile theo Environment.

---

# 36. Enterprise Design Principles

## EP-15-001

Business Domain không được tích hợp trực tiếp với hệ thống bên ngoài.

---

## EP-15-002

Toàn bộ Integration phải đi qua Gateway, Connector và Adapter.

---

## EP-15-003

Business Domain chỉ sử dụng Canonical Data Model.

---

## EP-15-004

Business Domain chỉ sử dụng Canonical Event Model.

---

## EP-15-005

Toàn Platform giao tiếp nội bộ theo Event-Driven Architecture.

---

## EP-15-006

Mọi Business Domain đều Publish Business Event.

---

## EP-15-007

Connector Policy được cấu hình.

Không Hard-code.

---

## EP-15-008

Connector được lựa chọn bằng Routing Rule.

---

## EP-15-009

Integration Platform phải hỗ trợ Runtime Profile.

---

## EP-15-010

Integration Platform phải hỗ trợ Monitoring, Health, Retry, DLQ và Observability.

---

# 37. Published Business Events

Ví dụ các Business Event được Publish:

- OrderCreated
- OrderConfirmed
- PaymentSucceeded
- PaymentFailed
- PurchaseOrderCreated
- InventoryReserved
- InventoryAllocated
- FulfillmentCompleted
- SettlementConfirmed
- TicketCreated
- NotificationRequested
- ReportGenerated
- OrganizationCreated
- ConfigurationPublished

---

# 38. Consumed Business Events

Ví dụ các Business Event được Subscribe:

- SupplierProductUpdated
- SupplierInventoryChanged
- SupplierStatusChanged
- PaymentCallbackReceived
- WebhookReceived
- SchedulerTriggered
- NotificationDelivered
- ExchangeRateUpdated
- HealthStatusChanged

---

# 39. Business Capabilities Covered

Workshop này bao gồm các Business Capability:

- Integration Platform
- API Gateway
- Supplier Gateway
- Payment Gateway
- Partner Gateway
- Notification Gateway
- Connector Management
- Adapter Management
- Event Bus
- Event Registry
- Event Subscription
- Queue Management
- Dead Letter Queue Management
- Callback Management
- Webhook Management
- Canonical Data Management
- Canonical Event Management
- Connector Routing
- Integration Monitoring
- Integration Health
- Integration Policy Management

---

# 40. Traceability

Workshop này kế thừa toàn bộ các quyết định từ:

- BRD-WS-01 Business Vision
- BRD-WS-02 Product
- BRD-WS-03 Organization
- BRD-WS-04 Catalog
- BRD-WS-05 Commercial
- BRD-WS-06 Promotion
- BRD-WS-07 Order
- BRD-WS-08 Payment
- BRD-WS-09 Inventory & Fulfillment
- BRD-WS-10 Financial & Settlement
- BRD-WS-11 Customer Success
- BRD-WS-12 Communication Platform
- BRD-WS-13 Reporting, Analytics & Operational Intelligence
- BRD-WS-14 Platform Configuration, Reference Data & Business Rules

WS-15 cung cấp nền tảng Integration thống nhất cho toàn bộ Platform.

---

# 41. Impacts to Other Domains

Workshop này ảnh hưởng trực tiếp tới:

- Product
- Commercial
- Promotion
- Order
- Payment
- Procurement
- Inventory
- Fulfillment
- Settlement
- Customer Success
- Communication
- Reporting
- Analytics
- Security
- Monitoring
- Scheduler
- Platform Configuration

Tất cả Domain đều tích hợp thông qua Integration Platform.

---

# 42. Workshop Status

Status:

**FROZEN**

Workshop này xác định toàn bộ Enterprise Integration Foundation của YSim.

---

# 43. Next Workshop

**BRD-WS-16**

**Identity, Security, Authorization, Audit & Compliance**

Workshop tiếp theo sẽ xác định toàn bộ nền tảng bảo mật của YSim, bao gồm:

- Identity Platform
- Authentication
- Authorization
- Role-Based Access Control (RBAC)
- Attribute-Based Access Control (ABAC)
- Permission Model
- Session Management
- API Security
- Data Masking
- Audit Logging
- Compliance
- Privacy
- Encryption
- Secret Management
- Key Management
- Risk & Fraud Detection

WS-16 sẽ hoàn thiện lớp **Enterprise Security Foundation**, tạo nền tảng bảo mật thống nhất cho toàn bộ Business Domain và Integration Platform của YSim.

---

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-001 — Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Imp…

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
  "normative_statement": "Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Import - Batch Export",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-001",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-001",
    "source_context_sha256": "feba63776c4d2c75ef5f767a8cd3a7f770f7f7c9ab06b1d3a120720328d27d40",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "a5f2ca2359b25c15e1da9367db8839f772a70efaeebceb8bf0d597cb6f5764b8",
    "source_fingerprint_before_c3": "159d1351d50b80b6415544da4fefbb68dc6ff9ab094166a174a001e6739e7d88",
    "source_lines": "L1422-L1485",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-001"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-15-R027",
      "BRD-WS-15-R028",
      "BRD-WS-15-R029",
      "BRD-WS-15-R030",
      "BRD-WS-15-R031",
      "BRD-WS-15-R032"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-15-001",
  "title": "Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Imp…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-002 — API Gateway là thành phần bắt buộc. Business Domain không được tích hợp trực tiếp với hệ thống b…

```json
{
  "acceptance_contract": null,
  "acceptance_mechanism": null,
  "acceptance_rationale": "Composite parent coverage is satisfied only through ALL_CHILDREN; the parent is not an acceptance unit.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "STRUCTURAL_RECORD",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": false,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "API Gateway là thành phần bắt buộc. Business Domain không được tích hợp trực tiếp với hệ thống bên ngoài.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-002",
    "source_context_sha256": "6d1f156497f7d7655fbebca3c03fb857072962cf12c840eadf4b0aab06a87984",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "097b8d5b5ba9acfdf12593ac1c55f21ad91fdaadb3bf756f7f4ba6ce8d92fa84",
    "source_lines": "L1487-L1540",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-002"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-15-R026",
      "EP-15-001"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-15-002",
  "title": "API Gateway là thành phần bắt buộc. Business Domain không được tích hợp trực tiếp với hệ thống b…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-003 — Connector là Business Object. Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài. Bus…

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
  "normative_statement": "Connector là Business Object. Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài. Business Logic không được đặt trong Connector.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-003",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Connector",
    "source_context_sha256": "b4b269d9d838a068eef5bcaa82adf0a7ae24e95067a42c36d88725768e0eafbe",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "82aaa020a0bcc475a2bcc0e4c4c86088fa7042b15402d457148aa40f29a685f5",
    "source_fingerprint_before_c3": "23440f1d8c43318f34bfb666ffe29db0b564f8cb9e3a51d83536aebc7355f5dd",
    "source_lines": "L1542-L1603",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-003"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-15-R033",
      "BRD-WS-15-R034",
      "BRD-WS-15-R035"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-15-003",
  "title": "Connector là Business Object. Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài. Bus…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-004 — Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003",
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-004",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "f4bd22925014db3ccae2f696e08a983cab16a195c0dec5979edf8ed93fa17b6a"
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
        "BD-15-004-AC001",
        "BD-15-004-AC009",
        "BD-15-004-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O001",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Connection"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC002",
        "BD-15-004-AC009",
        "BD-15-004-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O002",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Authentication"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC003",
        "BD-15-004-AC009",
        "BD-15-004-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O003",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Session"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC004",
        "BD-15-004-AC009",
        "BD-15-004-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O004",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Retry"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC005",
        "BD-15-004-AC009",
        "BD-15-004-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O005",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Health Adapter quản lý"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC006",
        "BD-15-004-AC009",
        "BD-15-004-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O006",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Mapping"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC007",
        "BD-15-004-AC009",
        "BD-15-004-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O007",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Transformation"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC008",
        "BD-15-004-AC009",
        "BD-15-004-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O008",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Canonical Conversion"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-004-AC010"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-004-AC009"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-004-AC001",
        "BD-15-004-AC002",
        "BD-15-004-AC003",
        "BD-15-004-AC004",
        "BD-15-004-AC005",
        "BD-15-004-AC006",
        "BD-15-004-AC007",
        "BD-15-004-AC008"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication - Session - Retry - Health Adapter quản lý: - Mapping - Transformation - Canonical Conversion",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Adapter",
    "source_context_sha256": "882bb8d657e504eabdfbcdbed208b4558f0577123b79c13e6abbd609ef9e0810",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "f4bd22925014db3ccae2f696e08a983cab16a195c0dec5979edf8ed93fa17b6a",
    "source_lines": "L1605-L1798",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-004"
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
  "stable_id": "BD-15-004",
  "title": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-005 — Integration Platform được chia thành các Gateway độc lập: - API Gateway - Supplier Gateway - Pay…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-005",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "2439be9c3f5ec29812e89664ded2010ace37f4b03ea53622d8ac4fe634f62618"
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
        "BD-15-005-AC001",
        "BD-15-005-AC006",
        "BD-15-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-005-O001",
      "obligation_text": "Integration Platform được chia thành các Gateway độc lập: API Gateway"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-005-AC002",
        "BD-15-005-AC006",
        "BD-15-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-005-O002",
      "obligation_text": "Integration Platform được chia thành các Gateway độc lập: Supplier Gateway"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-005-AC003",
        "BD-15-005-AC006",
        "BD-15-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-005-O003",
      "obligation_text": "Integration Platform được chia thành các Gateway độc lập: Payment Gateway"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-005-AC004",
        "BD-15-005-AC006",
        "BD-15-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-005-O004",
      "obligation_text": "Integration Platform được chia thành các Gateway độc lập: Partner Gateway"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-005-AC005",
        "BD-15-005-AC006",
        "BD-15-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-005-O005",
      "obligation_text": "Integration Platform được chia thành các Gateway độc lập: Notification Gateway Gateway có thể mở rộng trong tương lai"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-005-AC007"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-005-AC006"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-005-AC001",
        "BD-15-005-AC002",
        "BD-15-005-AC003",
        "BD-15-005-AC004",
        "BD-15-005-AC005"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-005 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Integration Platform được chia thành các Gateway độc lập: - API Gateway - Supplier Gateway - Payment Gateway - Partner Gateway - Notification Gateway Gateway có thể mở rộng trong tương lai.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006",
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-005",
    "source_context_sha256": "a00c1d7ec6cdf01a7b34ed372544fa72d40282053b122cbaf64a02d34a1c995a",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "2439be9c3f5ec29812e89664ded2010ace37f4b03ea53622d8ac4fe634f62618",
    "source_lines": "L1800-L1960",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-005"
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
  "stable_id": "BD-15-005",
  "title": "Integration Platform được chia thành các Gateway độc lập: - API Gateway - Supplier Gateway - Pay…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-006 — Business Event là Business Object. Mọi Business Domain đều Publish Business Event

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
  "normative_statement": "Business Event là Business Object. Mọi Business Domain đều Publish Business Event.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-006",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Business Event",
    "source_context_sha256": "a32cea09e78e1790291b8be66975292424b4ef17c756b233ee9a07277d0ec8bd",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "2fb9baab01e0cac349cd61d261601e3ec95ab08739422dbf83b6aa7b23bd3070",
    "source_fingerprint_before_c3": "1ed7f0b9ad996ac715ff98804d18c420b07dbaf8b9d004cd1f9fa5cf92e5aa2b",
    "source_lines": "L1962-L2021",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-006"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-15-R036",
      "BRD-WS-15-R037"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-15-006",
  "title": "Business Event là Business Object. Mọi Business Domain đều Publish Business Event",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-007 — Business Domain đăng ký Subscribe Business Event. Publisher không biết Subscriber. Event Bus chị…

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
  "normative_statement": "Business Domain đăng ký Subscribe Business Event. Publisher không biết Subscriber. Event Bus chịu trách nhiệm Routing và Delivery.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-007",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Event Subscription",
    "source_context_sha256": "bac815a32b1342602e87b110b410c7d7123f30ef7b6dab5e98047a157c9fc326",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "d901b20ae6f66bb11b876a82f648e77eda525f9c468b7e4d0059dd590f717aef",
    "source_fingerprint_before_c3": "b5a096abadb58deedafb42f0047d2a296c7e3297ab576dd372877861df75008f",
    "source_lines": "L2023-L2083",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-007"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-15-R038",
      "BRD-WS-15-R039",
      "BRD-WS-15-R040"
    ]
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-15-007",
  "title": "Business Domain đăng ký Subscribe Business Event. Publisher không biết Subscriber. Event Bus chị…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-008 — Business Event hỗ trợ Version. Backward Compatibility phải được đảm bảo

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
      "requirement_id": "BD-15-008",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "6022fb8592988c2428623bcdb3c9760b4700100056803da3229a654e03e1872e"
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
        "BD-15-008-AC001",
        "BD-15-008-AC003",
        "BD-15-008-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-008-O001",
      "obligation_text": "Business Event hỗ trợ Version"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-008-AC002",
        "BD-15-008-AC003",
        "BD-15-008-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-008-O002",
      "obligation_text": "Backward Compatibility phải được đảm bảo"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event hỗ trợ Version. Backward Compatibility phải được đảm bảo.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Event Version",
    "source_context_sha256": "1b58dd9805ed55b8b493f1140abbd61c8a48c1ce0ff21d1dc37f3ee62a81dd31",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "6022fb8592988c2428623bcdb3c9760b4700100056803da3229a654e03e1872e",
    "source_lines": "L2085-L2170",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-008"
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
  "stable_id": "BD-15-008",
  "title": "Business Event hỗ trợ Version. Backward Compatibility phải được đảm bảo",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-009 — Event Delivery hỗ trợ: - At Most Once - At Least Once - Exactly Once Mặc định sử dụng: **At Leas…

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
      "requirement_id": "BD-15-009",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "7311cda702f0c2d5b7adfe715faa7828659db0544a82e36386d9c10d67937971"
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
        "BD-15-009-AC001",
        "BD-15-009-AC004",
        "BD-15-009-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-009-O001",
      "obligation_text": "Event Delivery hỗ trợ: At Most Once"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-009-AC002",
        "BD-15-009-AC004",
        "BD-15-009-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-009-O002",
      "obligation_text": "Event Delivery hỗ trợ: At Least Once"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-009-AC003",
        "BD-15-009-AC004",
        "BD-15-009-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-009-O003",
      "obligation_text": "Event Delivery hỗ trợ: Exactly Once Mặc định sử dụng: **At Least Once**"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Event Delivery hỗ trợ: - At Most Once - At Least Once - Exactly Once Mặc định sử dụng: **At Least Once**",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-009",
    "source_context_sha256": "c89aa41ca98f3efbe798969a42513ea498fd18ec52d0445d1832d467acdda7d5",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "7311cda702f0c2d5b7adfe715faa7828659db0544a82e36386d9c10d67937971",
    "source_lines": "L2172-L2267",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-009"
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
  "stable_id": "BD-15-009",
  "title": "Event Delivery hỗ trợ: - At Most Once - At Least Once - Exactly Once Mặc định sử dụng: **At Leas…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-010 — API và Business Event đều hỗ trợ Idempotency

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
      "requirement_id": "BD-15-010",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "530a4fe24842cd084082250e2be6928eb056e651eca25de5eed8a565ef4dcfcc"
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
        "BD-15-010-AC001",
        "BD-15-010-AC002",
        "BD-15-010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-010-O001",
      "obligation_text": "API và Business Event đều hỗ trợ Idempotency"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-010 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-010 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-010-AC003"
      ],
      "rationale": null
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-010-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-010-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-010 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "API và Business Event đều hỗ trợ Idempotency.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-010",
    "source_context_sha256": "02b5a91416bff3f415ec0f81d0c2a5537d4601f7ad27af92396217973a767906",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "530a4fe24842cd084082250e2be6928eb056e651eca25de5eed8a565ef4dcfcc",
    "source_lines": "L2269-L2379",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-010"
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
  "stable_id": "BD-15-010",
  "title": "API và Business Event đều hỗ trợ Idempotency",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-011 — Retry Policy được cấu hình. Bao gồm: - Retry Count - Retry Interval - Retry Strategy - Exponenti…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-011",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "6f6d5d6dd11ac2445548686e46f68ed9a9c84a3956b5a158476b6ccc5f1ab3ed"
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
        "BD-15-011-AC001",
        "BD-15-011-AC005",
        "BD-15-011-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-011-O001",
      "obligation_text": "Retry Policy được cấu hình. Bao gồm: Retry Count"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-011-AC002",
        "BD-15-011-AC005",
        "BD-15-011-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-011-O002",
      "obligation_text": "Retry Policy được cấu hình. Bao gồm: Retry Interval"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-011-AC003",
        "BD-15-011-AC005",
        "BD-15-011-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-011-O003",
      "obligation_text": "Retry Policy được cấu hình. Bao gồm: Retry Strategy"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-011-AC004",
        "BD-15-011-AC005",
        "BD-15-011-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-011-O004",
      "obligation_text": "Retry Policy được cấu hình. Bao gồm: Exponential Backoff"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Retry Policy được cấu hình. Bao gồm: - Retry Count - Retry Interval - Retry Strategy - Exponential Backoff",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-011",
    "source_context_sha256": "0f6d0782f47746dc3333e0613d73e0f591a6e8394e279ce7f420839f2deaa848",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "6f6d5d6dd11ac2445548686e46f68ed9a9c84a3956b5a158476b6ccc5f1ab3ed",
    "source_lines": "L2381-L2490",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-011"
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
  "stable_id": "BD-15-011",
  "title": "Retry Policy được cấu hình. Bao gồm: - Retry Count - Retry Interval - Retry Strategy - Exponenti…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-012 — Dead Letter Queue là Business Object. Message Retry thất bại sẽ được chuyển vào DLQ

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-012",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "866047fd80697c718a4b9628e553b8b2d62b0c5843cf3b3737960f7f86a41cd7"
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
        "BD-15-012-AC001",
        "BD-15-012-AC003",
        "BD-15-012-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-012-O001",
      "obligation_text": "Dead Letter Queue là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-012-AC002",
        "BD-15-012-AC003",
        "BD-15-012-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-012-O002",
      "obligation_text": "Message Retry thất bại sẽ được chuyển vào DLQ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Dead Letter Queue là Business Object. Message Retry thất bại sẽ được chuyển vào DLQ.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-012",
    "source_context_sha256": "f9c6af020939c42d7971c40590c3fc923f6ad78ae08f8504104f60483a8ce91e",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "866047fd80697c718a4b9628e553b8b2d62b0c5843cf3b3737960f7f86a41cd7",
    "source_lines": "L2492-L2581",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-012"
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
  "stable_id": "BD-15-012",
  "title": "Dead Letter Queue là Business Object. Message Retry thất bại sẽ được chuyển vào DLQ",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-013 — Callback là Business Object. Bao gồm: - Payment Callback - Supplier Callback - Notification Call…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-013",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "2a11d2d955ee20c5daa3d7a11e1fbf49228fcc689d2b992b4970b7649785097d"
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
        "BD-15-013-AC001",
        "BD-15-013-AC005",
        "BD-15-013-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-013-O001",
      "obligation_text": "Callback là Business Object. Bao gồm: Payment Callback"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-013-AC002",
        "BD-15-013-AC005",
        "BD-15-013-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-013-O002",
      "obligation_text": "Callback là Business Object. Bao gồm: Supplier Callback"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-013-AC003",
        "BD-15-013-AC005",
        "BD-15-013-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-013-O003",
      "obligation_text": "Callback là Business Object. Bao gồm: Notification Callback"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-013-AC004",
        "BD-15-013-AC005",
        "BD-15-013-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-013-O004",
      "obligation_text": "Callback là Business Object. Bao gồm: Partner Callback"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-013 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-013 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-013 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-013-AC005"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-013-AC001",
        "BD-15-013-AC002",
        "BD-15-013-AC003",
        "BD-15-013-AC004"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-013 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Callback là Business Object. Bao gồm: - Payment Callback - Supplier Callback - Notification Callback - Partner Callback",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Callback",
    "source_context_sha256": "6bf9d8ef8c33965e6d1f28ad0e20401e39c99b3462dbeb9d65e256015985b610",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "2a11d2d955ee20c5daa3d7a11e1fbf49228fcc689d2b992b4970b7649785097d",
    "source_lines": "L2583-L2728",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-013"
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
  "stable_id": "BD-15-013",
  "title": "Callback là Business Object. Bao gồm: - Payment Callback - Supplier Callback - Notification Call…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-014 — Webhook hỗ trợ: - Internal - Organization - External Partner

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-014",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "6c8de3010364bc96b834ca25f5fe0c53f04b0c8bfad0269808c505383bc037e8"
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
        "BD-15-014-AC001",
        "BD-15-014-AC004",
        "BD-15-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-014-O001",
      "obligation_text": "Webhook hỗ trợ: Internal"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-014-AC002",
        "BD-15-014-AC004",
        "BD-15-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-014-O002",
      "obligation_text": "Webhook hỗ trợ: Organization"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-014-AC003",
        "BD-15-014-AC004",
        "BD-15-014-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-014-O003",
      "obligation_text": "Webhook hỗ trợ: External Partner"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Webhook hỗ trợ: - Internal - Organization - External Partner",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Webhook",
    "source_context_sha256": "2f232ab53da3316795f97213561846bf634475d75e025122b4ff5b4cb28ad329",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "6c8de3010364bc96b834ca25f5fe0c53f04b0c8bfad0269808c505383bc037e8",
    "source_lines": "L2730-L2829",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-014"
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
  "stable_id": "BD-15-014",
  "title": "Webhook hỗ trợ: - Internal - Organization - External Partner",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-015 — API hỗ trợ Version. API Version được quản lý độc lập

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
      "requirement_id": "BD-15-015",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "88216dc510d94fa6730cdcc6f28781d8570924112bcfe2377ae5b6cf402c5857"
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
        "BD-15-015-AC001",
        "BD-15-015-AC003",
        "BD-15-015-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-015-O001",
      "obligation_text": "API hỗ trợ Version"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-015-AC002",
        "BD-15-015-AC003",
        "BD-15-015-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-015-O002",
      "obligation_text": "API Version được quản lý độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "API hỗ trợ Version. API Version được quản lý độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. API Version",
    "source_context_sha256": "5cc2c88ac803577e1e54b186c9e86282945e5a045224f703f737158cf75c0dd1",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "88216dc510d94fa6730cdcc6f28781d8570924112bcfe2377ae5b6cf402c5857",
    "source_lines": "L2831-L2916",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-015"
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
  "stable_id": "BD-15-015",
  "title": "API hỗ trợ Version. API Version được quản lý độc lập",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-016 — Connector hỗ trợ nhiều Runtime Profile: - Mock - Sandbox - UAT - Production

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-016",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "8c14dde807570aad07993ed6bfac265f57cada29eb27bb6207a51cc2e5c636b9"
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
        "BD-15-016-AC001",
        "BD-15-016-AC005",
        "BD-15-016-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-016-O001",
      "obligation_text": "Connector hỗ trợ nhiều Runtime Profile: Mock"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-016-AC002",
        "BD-15-016-AC005",
        "BD-15-016-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-016-O002",
      "obligation_text": "Connector hỗ trợ nhiều Runtime Profile: Sandbox"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-016-AC003",
        "BD-15-016-AC005",
        "BD-15-016-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-016-O003",
      "obligation_text": "Connector hỗ trợ nhiều Runtime Profile: UAT"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-016-AC004",
        "BD-15-016-AC005",
        "BD-15-016-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-016-O004",
      "obligation_text": "Connector hỗ trợ nhiều Runtime Profile: Production"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector hỗ trợ nhiều Runtime Profile: - Mock - Sandbox - UAT - Production",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-016",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-016",
    "source_context_sha256": "d54b5987732ed1af0b24f301d56fc3327a837238eea3e17e3ebd20f5c9879447",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "8c14dde807570aad07993ed6bfac265f57cada29eb27bb6207a51cc2e5c636b9",
    "source_lines": "L2918-L3027",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-016"
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
  "stable_id": "BD-15-016",
  "title": "Connector hỗ trợ nhiều Runtime Profile: - Mock - Sandbox - UAT - Production",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-017 — Message Queue là Business Object. Queue được tách theo từng nghiệp vụ

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
      "requirement_id": "BD-15-017",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "06701708c91531b7c4433561550208e38985d7afb020a70d6d4e0ea8c4a76eca"
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
        "BD-15-017-AC001",
        "BD-15-017-AC003",
        "BD-15-017-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-017-O001",
      "obligation_text": "Message Queue là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-017-AC002",
        "BD-15-017-AC003",
        "BD-15-017-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-017-O002",
      "obligation_text": "Queue được tách theo từng nghiệp vụ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Message Queue là Business Object. Queue được tách theo từng nghiệp vụ.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-017",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Message Queue",
    "source_context_sha256": "3bcd10940f30dc653eb73f6dc15dedd8e7944964d7f7525bd5c08481c8814c9f",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "06701708c91531b7c4433561550208e38985d7afb020a70d6d4e0ea8c4a76eca",
    "source_lines": "L3029-L3114",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-017"
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
  "stable_id": "BD-15-017",
  "title": "Message Queue là Business Object. Queue được tách theo từng nghiệp vụ",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-018 — Queue hỗ trợ: - FIFO - Priority - Partition Queue liên quan Payment, Procurement và Fulfillment …

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
      "requirement_id": "BD-15-018",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "1d22d055d913d05368c0a840031f8a2cae023ccfcf82015004d696c46cc8611d"
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
        "BD-15-018-AC001",
        "BD-15-018-AC004",
        "BD-15-018-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-018-O001",
      "obligation_text": "Queue hỗ trợ: FIFO"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-018-AC002",
        "BD-15-018-AC004",
        "BD-15-018-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-018-O002",
      "obligation_text": "Queue hỗ trợ: Priority"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-018-AC003",
        "BD-15-018-AC004",
        "BD-15-018-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-018-O003",
      "obligation_text": "Queue hỗ trợ: Partition Queue liên quan Payment, Procurement và Fulfillment có độ ưu tiên cao hơn"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-018 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-018 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-018 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-018-AC004"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-018-AC001",
        "BD-15-018-AC002",
        "BD-15-018-AC003"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-018 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Queue hỗ trợ: - FIFO - Priority - Partition Queue liên quan Payment, Procurement và Fulfillment có độ ưu tiên cao hơn.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-018",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-018",
    "source_context_sha256": "1ebb0d139b5650b61ed8af6862710b4353d05969cb1b64eb9cd421c5b3e36540",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "1d22d055d913d05368c0a840031f8a2cae023ccfcf82015004d696c46cc8611d",
    "source_lines": "L3116-L3246",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-018"
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
  "stable_id": "BD-15-018",
  "title": "Queue hỗ trợ: - FIFO - Priority - Partition Queue liên quan Payment, Procurement và Fulfillment …",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-019 — Integration Platform hỗ trợ: - Monitoring - Health Check - Retry - DLQ - Queue Monitoring

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-019",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "7c5da0be9d444361694434e3de0f4cb0994015f08aa822c476775c5fbd536cfb"
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
        "BD-15-019-AC001",
        "BD-15-019-AC006",
        "BD-15-019-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-019-O001",
      "obligation_text": "Integration Platform hỗ trợ: Monitoring"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-019-AC002",
        "BD-15-019-AC006",
        "BD-15-019-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-019-O002",
      "obligation_text": "Integration Platform hỗ trợ: Health Check"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-019-AC003",
        "BD-15-019-AC006",
        "BD-15-019-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-019-O003",
      "obligation_text": "Integration Platform hỗ trợ: Retry"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-019-AC004",
        "BD-15-019-AC006",
        "BD-15-019-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-019-O004",
      "obligation_text": "Integration Platform hỗ trợ: DLQ"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-019-AC005",
        "BD-15-019-AC006",
        "BD-15-019-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-019-O005",
      "obligation_text": "Integration Platform hỗ trợ: Queue Monitoring"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Integration Platform hỗ trợ: - Monitoring - Health Check - Retry - DLQ - Queue Monitoring",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-019",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-019",
    "source_context_sha256": "974758448c5e8c00e9ababf26859bfc55feab1fafbc3f4b75fd8c1c1901de3f0",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "7c5da0be9d444361694434e3de0f4cb0994015f08aa822c476775c5fbd536cfb",
    "source_lines": "L3248-L3367",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-019"
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
  "stable_id": "BD-15-019",
  "title": "Integration Platform hỗ trợ: - Monitoring - Health Check - Retry - DLQ - Queue Monitoring",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-020 — API Gateway hỗ trợ: - Rate Limiting - Burst - Quota

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-020",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "00b366ce412388f1ba86d8e5e9f25e946181d5501649cc7476e308f769dde38f"
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
        "BD-15-020-AC001",
        "BD-15-020-AC004",
        "BD-15-020-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-020-O001",
      "obligation_text": "API Gateway hỗ trợ: Rate Limiting"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-020-AC002",
        "BD-15-020-AC004",
        "BD-15-020-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-020-O002",
      "obligation_text": "API Gateway hỗ trợ: Burst"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-020-AC003",
        "BD-15-020-AC004",
        "BD-15-020-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-020-O003",
      "obligation_text": "API Gateway hỗ trợ: Quota"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "API Gateway hỗ trợ: - Rate Limiting - Burst - Quota",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-020",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-020",
    "source_context_sha256": "43a1fc9b573410dcc6cb8c8c69188f8c50cb665df3a0a752918546d949c530d3",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "00b366ce412388f1ba86d8e5e9f25e946181d5501649cc7476e308f769dde38f",
    "source_lines": "L3369-L3468",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-020"
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
  "stable_id": "BD-15-020",
  "title": "API Gateway hỗ trợ: - Rate Limiting - Burst - Quota",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-021 — Connector hỗ trợ Circuit Breaker

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-021",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "4ecc5093180afc7102cdc0bedca5e5c6b39fab1a77162261e26126a3be78d0aa"
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
        "BD-15-021-AC001",
        "BD-15-021-AC002",
        "BD-15-021-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-021-O001",
      "obligation_text": "Connector hỗ trợ Circuit Breaker"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector hỗ trợ Circuit Breaker.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-021",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-021",
    "source_context_sha256": "feb2150699e4059648fe00008258f1e84a63e07bf6e024ca6e9094343e99d9ea",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "4ecc5093180afc7102cdc0bedca5e5c6b39fab1a77162261e26126a3be78d0aa",
    "source_lines": "L3470-L3549",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-021"
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
  "stable_id": "BD-15-021",
  "title": "Connector hỗ trợ Circuit Breaker",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-022 — Scheduler có thể Publish Business Event

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
      "requirement_id": "BD-15-022",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "f8d97665fe0f667a9d85d337ab5c34ad70587e01666507017d05575cb011b221"
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
        "BD-15-022-AC001",
        "BD-15-022-AC002",
        "BD-15-022-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-022-O001",
      "obligation_text": "Scheduler có thể Publish Business Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Scheduler có thể Publish Business Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-022",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "26. Scheduler Event",
    "source_context_sha256": "2ed9a73a80a7abcb1dd76d776848940b0751afae088f5883f710138be984ef28",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "f8d97665fe0f667a9d85d337ab5c34ad70587e01666507017d05575cb011b221",
    "source_lines": "L3551-L3626",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-022"
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
  "stable_id": "BD-15-022",
  "title": "Scheduler có thể Publish Business Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-023 — Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Even…

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
  "normative_statement": "Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Event - Consumed Event - Dependency - Owner - Version",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-023",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Business Service Registry",
    "source_context_sha256": "cffc01224270ac2af85b76b8866141a249b861e7834694115b140112ebcc8665",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "3a35b90a805acc9dd205f1be2c171cdaccc598252bc9212e525342afc0f33287",
    "source_fingerprint_before_c3": "618dbae2e3ffc8e1c6b22d358371d29dc468cfe481201d7fdd4e3503b2a10f89",
    "source_lines": "L3628-L3692",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-023"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-15-R041",
      "BRD-WS-15-R042",
      "BRD-WS-15-R043",
      "BRD-WS-15-R044",
      "BRD-WS-15-R045",
      "BRD-WS-15-R046",
      "BRD-WS-15-R047"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-15-023",
  "title": "Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Even…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-024 — Business Domain chỉ làm việc với Canonical Data Model

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
      "requirement_id": "BD-15-024",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "39a85c2728367320a95b772e0e618b9340ba2a1eeeee82faf0f4448d132986ae"
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
        "BD-15-024-AC001",
        "BD-15-024-AC002",
        "BD-15-024-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-024-O001",
      "obligation_text": "Business Domain chỉ làm việc với Canonical Data Model"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain chỉ làm việc với Canonical Data Model.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-024",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Canonical Data Model",
    "source_context_sha256": "0e14e6e305b91016895941b8fc0092a1cbf89898a7958523850dd9ac36bfbad6",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "39a85c2728367320a95b772e0e618b9340ba2a1eeeee82faf0f4448d132986ae",
    "source_lines": "L3694-L3769",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-024"
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
  "stable_id": "BD-15-024",
  "title": "Business Domain chỉ làm việc với Canonical Data Model",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-025 — Business Domain chỉ xử lý Canonical Event Model

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
      "requirement_id": "BD-15-025",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "b9b5f9379c70298e23cdb7aa36b0e225b2d6b21606b277af030f582499142d37"
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
        "BD-15-025-AC001",
        "BD-15-025-AC002",
        "BD-15-025-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-025-O001",
      "obligation_text": "Business Domain chỉ xử lý Canonical Event Model"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain chỉ xử lý Canonical Event Model.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-025",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-025",
    "source_context_sha256": "42562cdb33f90f7ba20935fe3626b3f0638bd52459ec5ecc9c0420648ee3dc8d",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "b9b5f9379c70298e23cdb7aa36b0e225b2d6b21606b277af030f582499142d37",
    "source_lines": "L3771-L3846",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-025"
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
  "stable_id": "BD-15-025",
  "title": "Business Domain chỉ xử lý Canonical Event Model",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-026 — Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Break…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003",
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-026",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "7fa573efa3909ba7473fe8f2f9bb3ffe15628262cf248fa5be90db044e734a22"
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
        "BD-15-026-AC001",
        "BD-15-026-AC008",
        "BD-15-026-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O001",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Timeout"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC002",
        "BD-15-026-AC008",
        "BD-15-026-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O002",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Retry"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC003",
        "BD-15-026-AC008",
        "BD-15-026-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O003",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Circuit Breaker"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC004",
        "BD-15-026-AC008",
        "BD-15-026-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O004",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Rate Limit"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC005",
        "BD-15-026-AC008",
        "BD-15-026-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O005",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Concurrency"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC006",
        "BD-15-026-AC008",
        "BD-15-026-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O006",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Queue Priority"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC007",
        "BD-15-026-AC008",
        "BD-15-026-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O007",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Health Threshold"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-026 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-026-AC009"
      ],
      "rationale": null
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-026 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-026-AC008"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-15-026-AC001",
        "BD-15-026-AC002",
        "BD-15-026-AC003",
        "BD-15-026-AC004",
        "BD-15-026-AC005",
        "BD-15-026-AC006",
        "BD-15-026-AC007"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-15-026 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Breaker - Rate Limit - Concurrency - Queue Priority - Health Threshold",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003",
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-026",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Connector Policy",
    "source_context_sha256": "92b09aae5e17f80302beadb38c01cd2aa9ae245908d3e611081fe67fbf55d242",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "7fa573efa3909ba7473fe8f2f9bb3ffe15628262cf248fa5be90db044e734a22",
    "source_lines": "L3848-L4030",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-026"
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
  "stable_id": "BD-15-026",
  "title": "Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Break…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-027 — Connector Routing Rule là Business Object. Routing Rule được cấu hình. Business Domain không quy…

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
  "normative_statement": "Connector Routing Rule là Business Object. Routing Rule được cấu hình. Business Domain không quyết định Connector.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-027",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "31. Connector Routing Rule",
    "source_context_sha256": "2b5ae149f16258e6f19e3b618371fa39670739057e5cc4fda0dca2095e684d00",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "9729e808f032ca9183e1d33971aba1613361d233a61e50c5b30d9d433fe9d3e8",
    "source_fingerprint_before_c3": "e9e3168d969b135921fdb9730d00b783fc0ae99e7a5bd003c4f9959d2ae00eb9",
    "source_lines": "L4032-L4093",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-027"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-15-R048",
      "BRD-WS-15-R049",
      "BRD-WS-15-R050"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-15-027",
  "title": "Connector Routing Rule là Business Object. Routing Rule được cấu hình. Business Domain không quy…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-028 — Connector phải khai báo Capability Matrix. Business Domain lựa chọn Connector dựa trên Capabilit…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005",
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-028",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "b19d2a83845ba1205b1685fb6805ef3312cc9be8b31ac8e5da7904df5f2a8592"
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
        "BD-15-028-AC001",
        "BD-15-028-AC003",
        "BD-15-028-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-028-O001",
      "obligation_text": "Connector phải khai báo Capability Matrix"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-028-AC002",
        "BD-15-028-AC003",
        "BD-15-028-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-028-O002",
      "obligation_text": "Business Domain lựa chọn Connector dựa trên Capability"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector phải khai báo Capability Matrix. Business Domain lựa chọn Connector dựa trên Capability.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-028",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-028",
    "source_context_sha256": "3d4e8e0c467c004d7d4ccff2b1f2fbab812f2a82bc63d3809650bb6811a112a4",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "b19d2a83845ba1205b1685fb6805ef3312cc9be8b31ac8e5da7904df5f2a8592",
    "source_lines": "L4095-L4186",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-028"
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
  "stable_id": "BD-15-028",
  "title": "Connector phải khai báo Capability Matrix. Business Domain lựa chọn Connector dựa trên Capabilit…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-029 — Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Re…

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
  "normative_statement": "Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Retired",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-029",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-029",
    "source_context_sha256": "381d81c5ec93ae99263a5596851482557a81362364f9a3697b7362de3afe4299",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "a871a409aca73db8194c2606ffd3b3b51ce93b84f3a20fed830caf6cb85b6b58",
    "source_fingerprint_before_c3": "e8d452f617ad1ec6edccc5c056126f6d99cdf078db33429f4ff49089d5cc37f4",
    "source_lines": "L4188-L4253",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-029"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-15-R051",
      "BRD-WS-15-R052",
      "BRD-WS-15-R053",
      "BRD-WS-15-R054",
      "BRD-WS-15-R055",
      "BRD-WS-15-R056",
      "BRD-WS-15-R057"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-15-029",
  "title": "Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Re…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-030 — Connector Runtime Profile hỗ trợ: - Mock - Sandbox - UAT - Production Runtime tự động lựa chọn P…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-15-030",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "bf541178d104a495573d033bd9bb702b45e76c15eca1874351c19590eee990b6"
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
        "BD-15-030-AC001",
        "BD-15-030-AC005",
        "BD-15-030-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-030-O001",
      "obligation_text": "Connector Runtime Profile hỗ trợ: Mock"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-030-AC002",
        "BD-15-030-AC005",
        "BD-15-030-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-030-O002",
      "obligation_text": "Connector Runtime Profile hỗ trợ: Sandbox"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-030-AC003",
        "BD-15-030-AC005",
        "BD-15-030-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-030-O003",
      "obligation_text": "Connector Runtime Profile hỗ trợ: UAT"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-030-AC004",
        "BD-15-030-AC005",
        "BD-15-030-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-030-O004",
      "obligation_text": "Connector Runtime Profile hỗ trợ: Production Runtime tự động lựa chọn Profile theo Environment"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector Runtime Profile hỗ trợ: - Mock - Sandbox - UAT - Production Runtime tự động lựa chọn Profile theo Environment.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-030",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-030",
    "source_context_sha256": "b5789a54b46e1ae6310c5d023ec1e9d4648c84d99f0e1b046c31e2cb99f51215",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "bf541178d104a495573d033bd9bb702b45e76c15eca1874351c19590eee990b6",
    "source_lines": "L4255-L4364",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-15-030"
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
  "stable_id": "BD-15-030",
  "title": "Connector Runtime Profile hỗ trợ: - Mock - Sandbox - UAT - Production Runtime tự động lựa chọn P…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R003 — API Gateway là thành phần bắt buộc của Platform

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R003",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "49f0206c539501bf544ceba0f3a366eda96311582f95946ffabca1b98e481848"
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
        "BRD-WS-15-R003-AC001",
        "BRD-WS-15-R003-AC002",
        "BRD-WS-15-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R003-O001",
      "obligation_text": "API Gateway là thành phần bắt buộc của Platform"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "API Gateway là thành phần bắt buộc của Platform.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-003",
    "previous_temporary_key": "TMP-BRD-WS-15-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "5. API Gateway",
    "source_context_sha256": "f00be47d9102b41f83f1611ec92a82004b961de5f10607d12f5ae442f91eaf0e",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "49f0206c539501bf544ceba0f3a366eda96311582f95946ffabca1b98e481848",
    "source_lines": "L4366-L4445",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R003"
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
  "stable_id": "BRD-WS-15-R003",
  "title": "API Gateway là thành phần bắt buộc của Platform",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R004 — Gateway mới chỉ được bổ sung khi có approved integration requirement và phải tuân thủ connector/…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R004",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "2edb96132c8f393ee0b8c2d5c91f934422ecbe512397d630730bf664ed6ad2bb"
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
        "BRD-WS-15-R004-AC001",
        "BRD-WS-15-R004-AC003",
        "BRD-WS-15-R004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R004-O001",
      "obligation_text": "Gateway mới chỉ được bổ sung khi có approved integration requirement và phải tuân thủ connector/gateway lifecycle, credential governance, security review, observability và audit"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-15-R004-AC002",
        "BRD-WS-15-R004-AC003",
        "BRD-WS-15-R004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R004-O002",
      "obligation_text": "Business Logic không được đặt trong Gateway"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Gateway mới chỉ được bổ sung khi có approved integration requirement và phải tuân thủ connector/gateway lifecycle, credential governance, security review, observability và audit; Business Logic không được đặt trong Gateway.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-004",
    "phase_2c_c3_actions": [
      "C3_APPROVED_SEMANTIC_DIRECTIVE"
    ],
    "previous_temporary_key": "TMP-BRD-WS-15-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Gateway Separation",
    "source_context_sha256": "2594da7df7f45957b5539cb25689975d7ca2a586fb4a8bad50c763112d785a59",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "2edb96132c8f393ee0b8c2d5c91f934422ecbe512397d630730bf664ed6ad2bb",
    "source_fingerprint_before_c3": "431fc7238221528f8f818e767a6d9c7c05b440b31dab409e0fe3812e590a03d8",
    "source_lines": "L4447-L4544",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R004"
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
  "stable_id": "BRD-WS-15-R004",
  "title": "Gateway mới chỉ được bổ sung khi có approved integration requirement và phải tuân thủ connector/…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R005 — Một Event mới không được phép phá vỡ khả năng tương thích ngược (Backward Compatibility) nếu vẫn…

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
      "requirement_id": "BRD-WS-15-R005",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "b90131f4db3d5644bf8bf287144e54e01d6d478b4e3dad60e1aef0ec29633d40"
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
        "BRD-WS-15-R005-AC001",
        "BRD-WS-15-R005-AC002",
        "BRD-WS-15-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R005-O001",
      "obligation_text": "Một Event mới không được phép phá vỡ khả năng tương thích ngược (Backward Compatibility) nếu vẫn còn Subscriber sử dụng Version cũ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một Event mới không được phép phá vỡ khả năng tương thích ngược (Backward Compatibility) nếu vẫn còn Subscriber sử dụng Version cũ.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-005",
    "previous_temporary_key": "TMP-BRD-WS-15-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "11. Event Version",
    "source_context_sha256": "1b58dd9805ed55b8b493f1140abbd61c8a48c1ce0ff21d1dc37f3ee62a81dd31",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "b90131f4db3d5644bf8bf287144e54e01d6d478b4e3dad60e1aef0ec29633d40",
    "source_lines": "L4546-L4621",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R005"
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
  "stable_id": "BRD-WS-15-R005",
  "title": "Một Event mới không được phép phá vỡ khả năng tương thích ngược (Backward Compatibility) nếu vẫn…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R006 — Business Domain không được tạo dữ liệu trùng khi nhận cùng một Request hoặc Event nhiều lần

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
      "requirement_id": "BRD-WS-15-R006",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "0e405fdc3575b6f13556ff0ceed9fdf23fa1d2c9e9f97bf8ffe8b1962c396920"
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
        "BRD-WS-15-R006-AC001",
        "BRD-WS-15-R006-AC002",
        "BRD-WS-15-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R006-O001",
      "obligation_text": "Business Domain không được tạo dữ liệu trùng khi nhận cùng một Request hoặc Event nhiều lần"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R006 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-15-R006-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-15-R006-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R006 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain không được tạo dữ liệu trùng khi nhận cùng một Request hoặc Event nhiều lần.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-006",
    "previous_temporary_key": "TMP-BRD-WS-15-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Idempotency",
    "source_context_sha256": "99470888ae4506c6ee22020ed8098dd929537b42e570525948c0731d04b8be4c",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "0e405fdc3575b6f13556ff0ceed9fdf23fa1d2c9e9f97bf8ffe8b1962c396920",
    "source_lines": "L4623-L4731",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R006"
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
  "stable_id": "BRD-WS-15-R006",
  "title": "Business Domain không được tạo dữ liệu trùng khi nhận cùng một Request hoặc Event nhiều lần",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R007 — Retry không được Hard-code

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R007",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "84bbd6378fd6f96a6a161fa69733b362692dd78e249055a143c7c065c8ff2cda"
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
        "BRD-WS-15-R007-AC001",
        "BRD-WS-15-R007-AC002",
        "BRD-WS-15-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R007-O001",
      "obligation_text": "Retry không được Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Retry không được Hard-code.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-007",
    "previous_temporary_key": "TMP-BRD-WS-15-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "14. Retry Policy",
    "source_context_sha256": "02559ff81a3cdebbca8e1704ddea3699720442f24716d7b56eb0df1eab025762",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "84bbd6378fd6f96a6a161fa69733b362692dd78e249055a143c7c065c8ff2cda",
    "source_lines": "L4733-L4812",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R007"
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
  "stable_id": "BRD-WS-15-R007",
  "title": "Retry không được Hard-code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R008 — DLQ phải lưu đầy đủ: - Message

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Additional failure metadata may be present; Message remains mandatory"
    ],
    "concrete_bindings": [
      {
        "actual_set": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
            "source_type": "SOURCE_LITERAL",
            "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
          },
          "identifier": "RESOLVED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BRD-WS-15-R008.RESOLVED.COLLECTION",
          "origin": {
            "origin_id": "YSIM.BRD-WS-15-R008.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
            "source_lines": "L365-L367",
            "source_section": "15. Dead Letter Queue"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "OBSERVE.BRD-WS-15-R008.RESOLVED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
        },
        "required_members": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
            "source_type": "SOURCE_LITERAL",
            "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
          },
          "identifier": "GOVERNED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BRD-WS-15-R008.GOVERNED.COLLECTION",
          "origin": {
            "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
            "source_lines": "L365-L367",
            "source_section": "15. Dead Letter Queue"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "RESOLVE.BRD-WS-15-R008.GOVERNED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-15-R008",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Message is absent or dangling from DLQ record"
    ],
    "operator_composition": [
      "SET_CONTAINS"
    ],
    "positive_oracle": [
      "DLQ record contains the Message"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
      "source_lines": "L365-L367",
      "source_section": "15. Dead Letter Queue"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
          "source_type": "SOURCE_LITERAL",
          "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
        },
        "identifier": "BRD-WS-15-R008.BRD-WS-15-R008.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-15-R008.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-15.md",
          "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
          "source_lines": "L365-L367",
          "source_section": "15. Dead Letter Queue"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-15-R008.BRD-WS-15-R008.BRD-WS-15-R008.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-15-R008.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.DLQ_RECORD_ID",
        "FIELD.MESSAGE_ID",
        "FIELD.MESSAGE_PAYLOAD_REF",
        "FIELD.VALIDATION_RESULT"
      ],
      "producer": "BRD-WS-15-R008.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-15-R008.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.DLQ_RECORD_ID",
        "FIELD.MESSAGE_ID",
        "FIELD.MESSAGE_PAYLOAD_REF",
        "FIELD.VALIDATION_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-WS-15-R008.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-15-R008.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-15-R008.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-15-R008-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS",
          "evaluator_consumed_bindings": [
            "actual_set",
            "required_members"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
              "source_type": "SOURCE_LITERAL",
              "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
            },
            "identifier": "BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-15.md",
              "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
              "source_lines": "L365-L367",
              "source_section": "15. Dead Letter Queue"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-15-R008.BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                  "source_type": "SOURCE_LITERAL",
                  "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
                },
                "identifier": "BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
                  "source_lines": "L365-L367",
                  "source_section": "15. Dead Letter Queue"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BRD-WS-15-R008.BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-15.md",
              "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
              "source_lines": "L365-L367",
              "source_section": "15. Dead Letter Queue"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_set": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                  "source_type": "SOURCE_LITERAL",
                  "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
                },
                "identifier": "RESOLVED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BRD-WS-15-R008.RESOLVED.COLLECTION",
                "origin": {
                  "origin_id": "YSIM.BRD-WS-15-R008.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
                  "source_lines": "L365-L367",
                  "source_section": "15. Dead Letter Queue"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "OBSERVE.BRD-WS-15-R008.RESOLVED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
              },
              "required_members": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                  "source_type": "SOURCE_LITERAL",
                  "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
                },
                "identifier": "GOVERNED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BRD-WS-15-R008.GOVERNED.COLLECTION",
                "origin": {
                  "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
                  "source_lines": "L365-L367",
                  "source_section": "15. Dead Letter Queue"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "RESOLVE.BRD-WS-15-R008.GOVERNED_MEMBER_COLLECTION",
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
                        "BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                      "source_type": "SOURCE_LITERAL",
                      "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
                    },
                    "identifier": "BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-15.md",
                      "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
                      "source_lines": "L365-L367",
                      "source_section": "15. Dead Letter Queue"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BRD-WS-15-R008.BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
                  "source_lines": "L365-L367",
                  "source_section": "15. Dead Letter Queue"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "observed": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                      "source_type": "SOURCE_LITERAL",
                      "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
                    },
                    "identifier": "BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-15.md",
                      "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
                      "source_lines": "L365-L367",
                      "source_section": "15. Dead Letter Queue"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "OBSERVE.BRD-WS-15-R008.BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
                  "source_lines": "L365-L367",
                  "source_section": "15. Dead Letter Queue"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                "source_type": "SOURCE_LITERAL",
                "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
              },
              "identifier": "BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
                "source_lines": "L365-L367",
                "source_section": "15. Dead Letter Queue"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-15-R008.BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "SET_CONTAINS"
          },
          "obligation_id": "BRD-WS-15-R008-O001",
          "observed_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                  "source_type": "SOURCE_LITERAL",
                  "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
                },
                "identifier": "BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
                  "source_lines": "L365-L367",
                  "source_section": "15. Dead Letter Queue"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BRD-WS-15-R008.BRD-WS-15-R008.BRD-WS-15-R008.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-15.md",
              "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
              "source_lines": "L365-L367",
              "source_section": "15. Dead Letter Queue"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "operator_id": "SET_CONTAINS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_set": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                "source_type": "SOURCE_LITERAL",
                "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
              },
              "identifier": "RESOLVED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BRD-WS-15-R008.RESOLVED.COLLECTION",
              "origin": {
                "origin_id": "YSIM.BRD-WS-15-R008.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
                "source_lines": "L365-L367",
                "source_section": "15. Dead Letter Queue"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "OBSERVE.BRD-WS-15-R008.RESOLVED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
            },
            "required_members": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                "source_type": "SOURCE_LITERAL",
                "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
              },
              "identifier": "GOVERNED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BRD-WS-15-R008.GOVERNED.COLLECTION",
              "origin": {
                "origin_id": "BRD-WS-15-R008.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
                "source_lines": "L365-L367",
                "source_section": "15. Dead Letter Queue"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "RESOLVE.BRD-WS-15-R008.GOVERNED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Additional failure metadata may be present; Message remains mandatory"
      ],
      "contract_ast_sha256": "51ae891e827fb1f871e27df006a4448553bc9c95fae9ddc580b308eb337b4b77",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-15-R008",
      "criticality": "NORMAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
            "source_type": "SOURCE_LITERAL",
            "version": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061"
          },
          "identifier": "BRD-WS-15-R008.BRD-WS-15-R008.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-15-R008.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
            "source_lines": "L365-L367",
            "source_section": "15. Dead Letter Queue"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-15-R008.BRD-WS-15-R008.BRD-WS-15-R008.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-15-R008.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.DLQ_RECORD_ID",
          "FIELD.MESSAGE_ID",
          "FIELD.MESSAGE_PAYLOAD_REF",
          "FIELD.VALIDATION_RESULT"
        ],
        "producer": "BRD-WS-15-R008.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-15-R008.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.DLQ_RECORD_ID",
          "FIELD.MESSAGE_ID",
          "FIELD.MESSAGE_PAYLOAD_REF",
          "FIELD.VALIDATION_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-WS-15-R008.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-15-R008.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-15-R008.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-R2-FX-7B999F7625DE11D96D1E",
        "P2C-C4-R2-FX-CBB120B005E9BB3C3CA7",
        "P2C-C4-R2-FX-5A93B5D6B813E964FD66"
      ],
      "high_risk_audit_subset": false,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Message is absent or dangling from DLQ record"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-15-R008-O001",
          "obligation_text": "DLQ phải lưu đầy đủ: - Message"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-15-R008.O1.1.SET_CONTAINS"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-15-R008-O001"
        }
      ],
      "operator_composition": [
        "SET_CONTAINS"
      ],
      "positive_oracles": [
        "DLQ record contains the Message"
      ],
      "preconditions": [
        "The failed Message identity exists"
      ],
      "prohibitions": [
        "Message is absent or dangling from DLQ record"
      ],
      "requirement_id": "BRD-WS-15-R008",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-15.md",
        "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
        "source_lines": "L365-L367",
        "source_section": "15. Dead Letter Queue"
      },
      "source_statement": "DLQ phải lưu đầy đủ: - Message",
      "surrounding_source_context": "### BRD-WS-15-R008 — DLQ phải lưu đầy đủ: - Message"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-15-R008",
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
        "BRD-WS-15-R008-AC001",
        "BRD-WS-15-R008-AC002",
        "BRD-WS-15-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R008-O001",
      "obligation_text": "DLQ phải lưu đầy đủ: - Message"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "DLQ phải lưu đầy đủ: - Message",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-008",
    "previous_temporary_key": "TMP-BRD-WS-15-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Dead Letter Queue",
    "source_context_sha256": "48f0086783e1813e8ad468027dbfa9d75313f07b5ee2d90a1b86c9c408e8910b",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "14dd716e01b76f04d798b4b55130f05c88778ec7194d7da1279354e1f1e03061",
    "source_lines": "L4814-L5604",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R008"
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
  "stable_id": "BRD-WS-15-R008",
  "title": "DLQ phải lưu đầy đủ: - Message",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R009 — DLQ phải lưu đầy đủ: - Event

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Additional failure metadata may be present; Event remains mandatory"
    ],
    "concrete_bindings": [
      {
        "actual_set": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
            "source_type": "SOURCE_LITERAL",
            "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
          },
          "identifier": "RESOLVED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BRD-WS-15-R009.RESOLVED.COLLECTION",
          "origin": {
            "origin_id": "YSIM.BRD-WS-15-R009.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
            "source_lines": "L365-L368",
            "source_section": "15. Dead Letter Queue"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "OBSERVE.BRD-WS-15-R009.RESOLVED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
        },
        "required_members": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
            "source_type": "SOURCE_LITERAL",
            "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
          },
          "identifier": "GOVERNED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BRD-WS-15-R009.GOVERNED.COLLECTION",
          "origin": {
            "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
            "source_lines": "L365-L368",
            "source_section": "15. Dead Letter Queue"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "RESOLVE.BRD-WS-15-R009.GOVERNED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-15-R009",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Event is absent or dangling from DLQ record"
    ],
    "operator_composition": [
      "SET_CONTAINS"
    ],
    "positive_oracle": [
      "DLQ record contains the Event"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
      "source_lines": "L365-L368",
      "source_section": "15. Dead Letter Queue"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
          "source_type": "SOURCE_LITERAL",
          "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
        },
        "identifier": "BRD-WS-15-R009.BRD-WS-15-R009.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-15-R009.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-15.md",
          "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
          "source_lines": "L365-L368",
          "source_section": "15. Dead Letter Queue"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-15-R009.BRD-WS-15-R009.BRD-WS-15-R009.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-15-R009.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.DLQ_RECORD_ID",
        "FIELD.EVENT_ID",
        "FIELD.EVENT_PAYLOAD_REF",
        "FIELD.VALIDATION_RESULT"
      ],
      "producer": "BRD-WS-15-R009.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-15-R009.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.DLQ_RECORD_ID",
        "FIELD.EVENT_ID",
        "FIELD.EVENT_PAYLOAD_REF",
        "FIELD.VALIDATION_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-WS-15-R009.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-15-R009.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-15-R009.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-15-R009-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS",
          "evaluator_consumed_bindings": [
            "actual_set",
            "required_members"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
              "source_type": "SOURCE_LITERAL",
              "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
            },
            "identifier": "BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-15.md",
              "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
              "source_lines": "L365-L368",
              "source_section": "15. Dead Letter Queue"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-15-R009.BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                  "source_type": "SOURCE_LITERAL",
                  "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
                },
                "identifier": "BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
                  "source_lines": "L365-L368",
                  "source_section": "15. Dead Letter Queue"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BRD-WS-15-R009.BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-15.md",
              "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
              "source_lines": "L365-L368",
              "source_section": "15. Dead Letter Queue"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_set": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                  "source_type": "SOURCE_LITERAL",
                  "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
                },
                "identifier": "RESOLVED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BRD-WS-15-R009.RESOLVED.COLLECTION",
                "origin": {
                  "origin_id": "YSIM.BRD-WS-15-R009.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
                  "source_lines": "L365-L368",
                  "source_section": "15. Dead Letter Queue"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "OBSERVE.BRD-WS-15-R009.RESOLVED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
              },
              "required_members": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                  "source_type": "SOURCE_LITERAL",
                  "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
                },
                "identifier": "GOVERNED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BRD-WS-15-R009.GOVERNED.COLLECTION",
                "origin": {
                  "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
                  "source_lines": "L365-L368",
                  "source_section": "15. Dead Letter Queue"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "RESOLVE.BRD-WS-15-R009.GOVERNED_MEMBER_COLLECTION",
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
                        "BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                      "source_type": "SOURCE_LITERAL",
                      "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
                    },
                    "identifier": "BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-15.md",
                      "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
                      "source_lines": "L365-L368",
                      "source_section": "15. Dead Letter Queue"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BRD-WS-15-R009.BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
                  "source_lines": "L365-L368",
                  "source_section": "15. Dead Letter Queue"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "observed": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                      "source_type": "SOURCE_LITERAL",
                      "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
                    },
                    "identifier": "BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-15.md",
                      "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
                      "source_lines": "L365-L368",
                      "source_section": "15. Dead Letter Queue"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "OBSERVE.BRD-WS-15-R009.BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
                  "source_lines": "L365-L368",
                  "source_section": "15. Dead Letter Queue"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                "source_type": "SOURCE_LITERAL",
                "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
              },
              "identifier": "BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
                "source_lines": "L365-L368",
                "source_section": "15. Dead Letter Queue"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-15-R009.BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "SET_CONTAINS"
          },
          "obligation_id": "BRD-WS-15-R009-O001",
          "observed_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                  "source_type": "SOURCE_LITERAL",
                  "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
                },
                "identifier": "BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
                  "source_lines": "L365-L368",
                  "source_section": "15. Dead Letter Queue"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BRD-WS-15-R009.BRD-WS-15-R009.BRD-WS-15-R009.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-15.md",
              "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
              "source_lines": "L365-L368",
              "source_section": "15. Dead Letter Queue"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "operator_id": "SET_CONTAINS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_set": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                "source_type": "SOURCE_LITERAL",
                "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
              },
              "identifier": "RESOLVED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BRD-WS-15-R009.RESOLVED.COLLECTION",
              "origin": {
                "origin_id": "YSIM.BRD-WS-15-R009.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
                "source_lines": "L365-L368",
                "source_section": "15. Dead Letter Queue"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "OBSERVE.BRD-WS-15-R009.RESOLVED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
            },
            "required_members": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                "source_type": "SOURCE_LITERAL",
                "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
              },
              "identifier": "GOVERNED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BRD-WS-15-R009.GOVERNED.COLLECTION",
              "origin": {
                "origin_id": "BRD-WS-15-R009.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
                "source_lines": "L365-L368",
                "source_section": "15. Dead Letter Queue"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "RESOLVE.BRD-WS-15-R009.GOVERNED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Additional failure metadata may be present; Event remains mandatory"
      ],
      "contract_ast_sha256": "c4a9a8c131b40cebb124559e84292a6144a569fca5f052f0e74cc2af60b49fba",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-15-R009",
      "criticality": "NORMAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
            "source_type": "SOURCE_LITERAL",
            "version": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d"
          },
          "identifier": "BRD-WS-15-R009.BRD-WS-15-R009.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-15-R009.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
            "source_lines": "L365-L368",
            "source_section": "15. Dead Letter Queue"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-15-R009.BRD-WS-15-R009.BRD-WS-15-R009.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-15-R009.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.DLQ_RECORD_ID",
          "FIELD.EVENT_ID",
          "FIELD.EVENT_PAYLOAD_REF",
          "FIELD.VALIDATION_RESULT"
        ],
        "producer": "BRD-WS-15-R009.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-15-R009.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.DLQ_RECORD_ID",
          "FIELD.EVENT_ID",
          "FIELD.EVENT_PAYLOAD_REF",
          "FIELD.VALIDATION_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-WS-15-R009.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-15-R009.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-15-R009.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-R2-FX-CED7FAAFDC2A293BE1FA",
        "P2C-C4-R2-FX-9E947CE455965D47AA34",
        "P2C-C4-R2-FX-732BC7F0E7737AF20053"
      ],
      "high_risk_audit_subset": false,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Event is absent or dangling from DLQ record"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-15-R009-O001",
          "obligation_text": "DLQ phải lưu đầy đủ: - Event"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-15-R009.O1.1.SET_CONTAINS"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-15-R009-O001"
        }
      ],
      "operator_composition": [
        "SET_CONTAINS"
      ],
      "positive_oracles": [
        "DLQ record contains the Event"
      ],
      "preconditions": [
        "The failed Event identity exists"
      ],
      "prohibitions": [
        "Event is absent or dangling from DLQ record"
      ],
      "requirement_id": "BRD-WS-15-R009",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-15.md",
        "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
        "source_lines": "L365-L368",
        "source_section": "15. Dead Letter Queue"
      },
      "source_statement": "DLQ phải lưu đầy đủ: - Event",
      "surrounding_source_context": "### BRD-WS-15-R009 — DLQ phải lưu đầy đủ: - Event"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-15-R009",
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
        "BRD-WS-15-R009-AC001",
        "BRD-WS-15-R009-AC002",
        "BRD-WS-15-R009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R009-O001",
      "obligation_text": "DLQ phải lưu đầy đủ: - Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "DLQ phải lưu đầy đủ: - Event",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-009",
    "previous_temporary_key": "TMP-BRD-WS-15-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Dead Letter Queue",
    "source_context_sha256": "48f0086783e1813e8ad468027dbfa9d75313f07b5ee2d90a1b86c9c408e8910b",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "a82db052aeb5c98556a991ca22b7c8303c6efa9fcb58c069c6863ec894289e60",
    "source_lines": "L5606-L6396",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R009"
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
  "stable_id": "BRD-WS-15-R009",
  "title": "DLQ phải lưu đầy đủ: - Event",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R010 — DLQ phải lưu đầy đủ: - Connector

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Additional failure metadata may be present; Connector remains mandatory"
    ],
    "concrete_bindings": [
      {
        "actual_set": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
            "source_type": "SOURCE_LITERAL",
            "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
          },
          "identifier": "RESOLVED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BRD-WS-15-R010.RESOLVED.COLLECTION",
          "origin": {
            "origin_id": "YSIM.BRD-WS-15-R010.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
            "origin_type": "RUNTIME_OBSERVED"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
            "source_lines": "L365-L369",
            "source_section": "15. Dead Letter Queue"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "OBSERVE.BRD-WS-15-R010.RESOLVED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
        },
        "required_members": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
            "source_type": "SOURCE_LITERAL",
            "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
          },
          "identifier": "GOVERNED_MEMBER_COLLECTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.BRD-WS-15-R010.GOVERNED.COLLECTION",
          "origin": {
            "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
            "source_lines": "L365-L369",
            "source_section": "15. Dead Letter Queue"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
            "resolver_id": "RESOLVE.BRD-WS-15-R010.GOVERNED_MEMBER_COLLECTION",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-15-R010",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Connector reference is absent or dangling"
    ],
    "operator_composition": [
      "SET_CONTAINS"
    ],
    "positive_oracle": [
      "DLQ record contains the Connector reference"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-006"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
      "source_lines": "L365-L369",
      "source_section": "15. Dead Letter Queue"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
          "source_type": "SOURCE_LITERAL",
          "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
        },
        "identifier": "BRD-WS-15-R010.BRD-WS-15-R010.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-15-R010.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-006"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-15.md",
          "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
          "source_lines": "L365-L369",
          "source_section": "15. Dead Letter Queue"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-15-R010.BRD-WS-15-R010.BRD-WS-15-R010.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-15-R010.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.DLQ_RECORD_ID",
        "FIELD.CONNECTOR_ID",
        "FIELD.CONNECTOR_VERSION",
        "FIELD.VALIDATION_RESULT"
      ],
      "producer": "BRD-WS-15-R010.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-15-R010.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.DLQ_RECORD_ID",
        "FIELD.CONNECTOR_ID",
        "FIELD.CONNECTOR_VERSION",
        "FIELD.VALIDATION_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-WS-15-R010.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-15-R010.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-15-R010.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-15-R010-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS",
          "evaluator_consumed_bindings": [
            "actual_set",
            "required_members"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
              "source_type": "SOURCE_LITERAL",
              "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
            },
            "identifier": "BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-006"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-15.md",
              "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
              "source_lines": "L365-L369",
              "source_section": "15. Dead Letter Queue"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-15-R010.BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                  "source_type": "SOURCE_LITERAL",
                  "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
                },
                "identifier": "BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
                  "source_lines": "L365-L369",
                  "source_section": "15. Dead Letter Queue"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BRD-WS-15-R010.BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-006"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-15.md",
              "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
              "source_lines": "L365-L369",
              "source_section": "15. Dead Letter Queue"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actual_set": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                  "source_type": "SOURCE_LITERAL",
                  "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
                },
                "identifier": "RESOLVED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BRD-WS-15-R010.RESOLVED.COLLECTION",
                "origin": {
                  "origin_id": "YSIM.BRD-WS-15-R010.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
                  "source_lines": "L365-L369",
                  "source_section": "15. Dead Letter Queue"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "OBSERVE.BRD-WS-15-R010.RESOLVED_MEMBER_COLLECTION",
                  "version": "1.0.0"
                },
                "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
              },
              "required_members": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                  "source_type": "SOURCE_LITERAL",
                  "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
                },
                "identifier": "GOVERNED_MEMBER_COLLECTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.BRD-WS-15-R010.GOVERNED.COLLECTION",
                "origin": {
                  "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
                  "source_lines": "L365-L369",
                  "source_section": "15. Dead Letter Queue"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                  "resolver_id": "RESOLVE.BRD-WS-15-R010.GOVERNED_MEMBER_COLLECTION",
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
                        "BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                      "source_type": "SOURCE_LITERAL",
                      "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
                    },
                    "identifier": "BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-006"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-15.md",
                      "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
                      "source_lines": "L365-L369",
                      "source_section": "15. Dead Letter Queue"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "RESOLVE.BRD-WS-15-R010.BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
                  "source_lines": "L365-L369",
                  "source_section": "15. Dead Letter Queue"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              },
              "observed": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                      "source_type": "SOURCE_LITERAL",
                      "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
                    },
                    "identifier": "BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                      "origin_type": "RUNTIME_OBSERVED"
                    },
                    "provenance": {
                      "approved_decision_references": [
                        "P2-DEC-006"
                      ],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-WS-15.md",
                      "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
                      "source_lines": "L365-L369",
                      "source_section": "15. Dead Letter Queue"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "CANONICAL_ENUM_VALUE",
                      "resolver_id": "OBSERVE.BRD-WS-15-R010.BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "CANONICAL_ENUM_VALUE"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
                  "source_lines": "L365-L369",
                  "source_section": "15. Dead Letter Queue"
                },
                "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                "source_type": "SOURCE_LITERAL",
                "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
              },
              "identifier": "BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
                "source_lines": "L365-L369",
                "source_section": "15. Dead Letter Queue"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-15-R010.BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "SET_CONTAINS"
          },
          "obligation_id": "BRD-WS-15-R010-O001",
          "observed_operand": {
            "members": [
              {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER"
                  ],
                  "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                  "source_type": "SOURCE_LITERAL",
                  "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
                },
                "identifier": "BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.OBSERVED.ORIGIN.MEMBER.1",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
                  "source_lines": "L365-L369",
                  "source_section": "15. Dead Letter Queue"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "OBSERVE.BRD-WS-15-R010.BRD-WS-15-R010.BRD-WS-15-R010.O1.1.SET_CONTAINS.CANONICAL.RESULT.MEMBER",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              }
            ],
            "origin": {
              "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-006"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-15.md",
              "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
              "source_lines": "L365-L369",
              "source_section": "15. Dead Letter Queue"
            },
            "semantic_type": "SET_OF<CANONICAL_ENUM_VALUE>"
          },
          "operator_id": "SET_CONTAINS",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actual_set": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                "source_type": "SOURCE_LITERAL",
                "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
              },
              "identifier": "RESOLVED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BRD-WS-15-R010.RESOLVED.COLLECTION",
              "origin": {
                "origin_id": "YSIM.BRD-WS-15-R010.RESOLVED.COLLECTION.RESOLVED_MEMBER_COLLECTION.RUNTIME_OBSERVED",
                "origin_type": "RUNTIME_OBSERVED"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
                "source_lines": "L365-L369",
                "source_section": "15. Dead Letter Queue"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "OBSERVE.BRD-WS-15-R010.RESOLVED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "RUNTIME_SET_REF<CANONICAL_ENUM_VALUE>"
            },
            "required_members": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
                "source_type": "SOURCE_LITERAL",
                "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
              },
              "identifier": "GOVERNED_MEMBER_COLLECTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.BRD-WS-15-R010.GOVERNED.COLLECTION",
              "origin": {
                "origin_id": "BRD-WS-15-R010.O1.1.SET_CONTAINS.REQUIRED_MEMBERS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
                "source_lines": "L365-L369",
                "source_section": "15. Dead Letter Queue"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "SET_OF<CANONICAL_ENUM_VALUE>",
                "resolver_id": "RESOLVE.BRD-WS-15-R010.GOVERNED_MEMBER_COLLECTION",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_SET_REF<CANONICAL_ENUM_VALUE>"
            }
          }
        }
      ],
      "boundary_cases": [
        "Additional failure metadata may be present; Connector remains mandatory"
      ],
      "contract_ast_sha256": "fb9675e023da0493cf6b7b9aa2dcb136fdb27ba7ff01934f1a42327a78ae5438",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-15-R010",
      "criticality": "HIGH",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-15.md#15. Dead Letter Queue",
            "source_type": "SOURCE_LITERAL",
            "version": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1"
          },
          "identifier": "BRD-WS-15-R010.BRD-WS-15-R010.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-15-R010.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
            "source_lines": "L365-L369",
            "source_section": "15. Dead Letter Queue"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-15-R010.BRD-WS-15-R010.BRD-WS-15-R010.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-15-R010.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.DLQ_RECORD_ID",
          "FIELD.CONNECTOR_ID",
          "FIELD.CONNECTOR_VERSION",
          "FIELD.VALIDATION_RESULT"
        ],
        "producer": "BRD-WS-15-R010.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-15-R010.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.DLQ_RECORD_ID",
          "FIELD.CONNECTOR_ID",
          "FIELD.CONNECTOR_VERSION",
          "FIELD.VALIDATION_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-WS-15-R010.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-15-R010.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-15-R010.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-R2-FX-22B7F6660A5FC429FE9B",
        "P2C-C4-R2-FX-2EB43C4C69CAF0D897F3",
        "P2C-C4-R2-FX-BA8D91EDB751CDD1D948"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Connector reference is absent or dangling"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-15-R010-O001",
          "obligation_text": "DLQ phải lưu đầy đủ: - Connector"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-15-R010.O1.1.SET_CONTAINS"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-15-R010-O001"
        }
      ],
      "operator_composition": [
        "SET_CONTAINS"
      ],
      "positive_oracles": [
        "DLQ record contains the Connector reference"
      ],
      "preconditions": [
        "The Connector identity exists"
      ],
      "prohibitions": [
        "Connector reference is absent or dangling"
      ],
      "requirement_id": "BRD-WS-15-R010",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-006"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-15.md",
        "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
        "source_lines": "L365-L369",
        "source_section": "15. Dead Letter Queue"
      },
      "source_statement": "DLQ phải lưu đầy đủ: - Connector",
      "surrounding_source_context": "### BRD-WS-15-R010 — DLQ phải lưu đầy đủ: - Connector"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-15-R010",
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
        "BRD-WS-15-R010-AC001",
        "BRD-WS-15-R010-AC002",
        "BRD-WS-15-R010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R010-O001",
      "obligation_text": "DLQ phải lưu đầy đủ: - Connector"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "DLQ phải lưu đầy đủ: - Connector",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-010",
    "previous_temporary_key": "TMP-BRD-WS-15-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Dead Letter Queue",
    "source_context_sha256": "48f0086783e1813e8ad468027dbfa9d75313f07b5ee2d90a1b86c9c408e8910b",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "dbaf4800ca8242f611a0ea33708c9a7fe3ce463dd8f9f89d48692ad546dc3412",
    "source_lines": "L6398-L7230",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R010"
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
  "stable_id": "BRD-WS-15-R010",
  "title": "DLQ phải lưu đầy đủ: - Connector",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R011 — DLQ phải lưu đầy đủ: - Error

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
      "requirement_id": "BRD-WS-15-R011",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "5840cf59af454f7fcea1fb28b69b90c0dfa336215029e1796e60f264faf92d0e"
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
        "BRD-WS-15-R011-AC001",
        "BRD-WS-15-R011-AC002",
        "BRD-WS-15-R011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R011-O001",
      "obligation_text": "DLQ phải lưu đầy đủ: - Error"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "DLQ phải lưu đầy đủ: - Error",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-011",
    "previous_temporary_key": "TMP-BRD-WS-15-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Dead Letter Queue",
    "source_context_sha256": "48f0086783e1813e8ad468027dbfa9d75313f07b5ee2d90a1b86c9c408e8910b",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "5840cf59af454f7fcea1fb28b69b90c0dfa336215029e1796e60f264faf92d0e",
    "source_lines": "L7232-L7307",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R011"
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
  "stable_id": "BRD-WS-15-R011",
  "title": "DLQ phải lưu đầy đủ: - Error",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R012 — DLQ phải lưu đầy đủ: - Retry History

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R012",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "e42ec2dbaad081648ffd6774074009a498c98e094a4550507a10c2702773d357"
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
        "BRD-WS-15-R012-AC001",
        "BRD-WS-15-R012-AC002",
        "BRD-WS-15-R012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R012-O001",
      "obligation_text": "DLQ phải lưu đầy đủ: - Retry History"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "DLQ phải lưu đầy đủ: - Retry History",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-012",
    "previous_temporary_key": "TMP-BRD-WS-15-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Dead Letter Queue",
    "source_context_sha256": "48f0086783e1813e8ad468027dbfa9d75313f07b5ee2d90a1b86c9c408e8910b",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "e42ec2dbaad081648ffd6774074009a498c98e094a4550507a10c2702773d357",
    "source_lines": "L7309-L7388",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R012"
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
  "stable_id": "BRD-WS-15-R012",
  "title": "DLQ phải lưu đầy đủ: - Retry History",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R013 — DLQ phải lưu đầy đủ: - Failure Reason

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
      "requirement_id": "BRD-WS-15-R013",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "18de9e19640368a25617491389e3d2f395966a37bf58a145501d46e70a7f4889"
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
        "BRD-WS-15-R013-AC001",
        "BRD-WS-15-R013-AC002",
        "BRD-WS-15-R013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R013-O001",
      "obligation_text": "DLQ phải lưu đầy đủ: - Failure Reason"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "DLQ phải lưu đầy đủ: - Failure Reason",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-013",
    "previous_temporary_key": "TMP-BRD-WS-15-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Dead Letter Queue",
    "source_context_sha256": "48f0086783e1813e8ad468027dbfa9d75313f07b5ee2d90a1b86c9c408e8910b",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "18de9e19640368a25617491389e3d2f395966a37bf58a145501d46e70a7f4889",
    "source_lines": "L7390-L7465",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R013"
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
  "stable_id": "BRD-WS-15-R013",
  "title": "DLQ phải lưu đầy đủ: - Failure Reason",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R014 — Callback luôn được: - Authenticate

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
      "requirement_id": "BRD-WS-15-R014",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "5b8dcd83c0bf381ec4c902432e0b689a57ad17cb5fa7c1fd320ede5b5f6cb64f"
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
        "BRD-WS-15-R014-AC001",
        "BRD-WS-15-R014-AC002",
        "BRD-WS-15-R014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R014-O001",
      "obligation_text": "Callback luôn được: - Authenticate"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R014 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-15-R014-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-15-R014-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R014 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Callback luôn được: - Authenticate",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-014",
    "previous_temporary_key": "TMP-BRD-WS-15-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Callback",
    "source_context_sha256": "6bf9d8ef8c33965e6d1f28ad0e20401e39c99b3462dbeb9d65e256015985b610",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "5b8dcd83c0bf381ec4c902432e0b689a57ad17cb5fa7c1fd320ede5b5f6cb64f",
    "source_lines": "L7467-L7575",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R014"
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
  "stable_id": "BRD-WS-15-R014",
  "title": "Callback luôn được: - Authenticate",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R015 — Callback luôn được: - Validate

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
      "requirement_id": "BRD-WS-15-R015",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "68bb00d611444ab00781eb4a405f7c43ad3eb26f5e0e7708a40aa720b738bbd5"
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
        "BRD-WS-15-R015-AC001",
        "BRD-WS-15-R015-AC002",
        "BRD-WS-15-R015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R015-O001",
      "obligation_text": "Callback luôn được: - Validate"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Callback luôn được: - Validate",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-015",
    "previous_temporary_key": "TMP-BRD-WS-15-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Callback",
    "source_context_sha256": "6bf9d8ef8c33965e6d1f28ad0e20401e39c99b3462dbeb9d65e256015985b610",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "68bb00d611444ab00781eb4a405f7c43ad3eb26f5e0e7708a40aa720b738bbd5",
    "source_lines": "L7577-L7652",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R015"
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
  "stable_id": "BRD-WS-15-R015",
  "title": "Callback luôn được: - Validate",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R016 — Callback luôn được: - Audit

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
      "requirement_id": "BRD-WS-15-R016",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "4882d4373c6bfe3af7a19b19142f153bdb2d08ab85a88ce1e92d40a6256647b6"
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
        "BRD-WS-15-R016-AC001",
        "BRD-WS-15-R016-AC002",
        "BRD-WS-15-R016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R016-O001",
      "obligation_text": "Callback luôn được: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R016 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R016 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R016 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-15-R016-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-15-R016-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R016 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Callback luôn được: - Audit",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-016",
    "previous_temporary_key": "TMP-BRD-WS-15-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Callback",
    "source_context_sha256": "6bf9d8ef8c33965e6d1f28ad0e20401e39c99b3462dbeb9d65e256015985b610",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "4882d4373c6bfe3af7a19b19142f153bdb2d08ab85a88ce1e92d40a6256647b6",
    "source_lines": "L7654-L7762",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R016"
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
  "stable_id": "BRD-WS-15-R016",
  "title": "Callback luôn được: - Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R017 — Callback luôn được: - Idempotent Check

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
      "requirement_id": "BRD-WS-15-R017",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "bf8b4c972ee690ced25cf7d3cd13bc05960ce7e43824954fd3bc5db1882400d2"
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
        "BRD-WS-15-R017-AC001",
        "BRD-WS-15-R017-AC002",
        "BRD-WS-15-R017-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R017-O001",
      "obligation_text": "Callback luôn được: - Idempotent Check"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R017 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R017 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-15-R017-AC003"
      ],
      "rationale": null
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-15-R017-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-15-R017-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-15-R017 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Callback luôn được: - Idempotent Check",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-017",
    "previous_temporary_key": "TMP-BRD-WS-15-017",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Callback",
    "source_context_sha256": "6bf9d8ef8c33965e6d1f28ad0e20401e39c99b3462dbeb9d65e256015985b610",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "bf8b4c972ee690ced25cf7d3cd13bc05960ce7e43824954fd3bc5db1882400d2",
    "source_lines": "L7764-L7874",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R017"
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
  "stable_id": "BRD-WS-15-R017",
  "title": "Callback luôn được: - Idempotent Check",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R018 — Một API mới không được làm ảnh hưởng đến các Client đang sử dụng Version cũ

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
      "requirement_id": "BRD-WS-15-R018",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "d81018d6a5d93d04ba6368be00a6c61afdfb7c63fcd04b2ab3753cdb06e85c42"
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
        "BRD-WS-15-R018-AC001",
        "BRD-WS-15-R018-AC002",
        "BRD-WS-15-R018-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R018-O001",
      "obligation_text": "Một API mới không được làm ảnh hưởng đến các Client đang sử dụng Version cũ"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một API mới không được làm ảnh hưởng đến các Client đang sử dụng Version cũ.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-018",
    "previous_temporary_key": "TMP-BRD-WS-15-018",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. API Version",
    "source_context_sha256": "5cc2c88ac803577e1e54b186c9e86282945e5a045224f703f737158cf75c0dd1",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "d81018d6a5d93d04ba6368be00a6c61afdfb7c63fcd04b2ab3753cdb06e85c42",
    "source_lines": "L7876-L7951",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R018"
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
  "stable_id": "BRD-WS-15-R018",
  "title": "Một API mới không được làm ảnh hưởng đến các Client đang sử dụng Version cũ",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R019 — Deprecation Policy phải được công bố trước khi loại bỏ một API Version

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
      "requirement_id": "BRD-WS-15-R019",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "87863b239690a895ec52c403b03b0596fb5660c9ed6d10bbbe1fc492fb91a938"
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
        "BRD-WS-15-R019-AC001",
        "BRD-WS-15-R019-AC002",
        "BRD-WS-15-R019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R019-O001",
      "obligation_text": "Deprecation Policy phải được công bố trước khi loại bỏ một API Version"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Deprecation Policy phải được công bố trước khi loại bỏ một API Version.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-019",
    "previous_temporary_key": "TMP-BRD-WS-15-019",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. API Version",
    "source_context_sha256": "5cc2c88ac803577e1e54b186c9e86282945e5a045224f703f737158cf75c0dd1",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "87863b239690a895ec52c403b03b0596fb5660c9ed6d10bbbe1fc492fb91a938",
    "source_lines": "L7953-L8028",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R019"
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
  "stable_id": "BRD-WS-15-R019",
  "title": "Deprecation Policy phải được công bố trước khi loại bỏ một API Version",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R020 — Business Domain không cần biết Connector đang sử dụng Profile nào

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R020",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "305b0d60dfbfc370f87ac1fbb27a9b37db0fae6689b58123670638f52b9a2636"
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
        "BRD-WS-15-R020-AC001",
        "BRD-WS-15-R020-AC002",
        "BRD-WS-15-R020-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R020-O001",
      "obligation_text": "Business Domain không cần biết Connector đang sử dụng Profile nào"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain không cần biết Connector đang sử dụng Profile nào.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-020",
    "previous_temporary_key": "TMP-BRD-WS-15-020",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Connector Profile",
    "source_context_sha256": "c002910c841337988aa5146955ee0398fca576f4d4636e2c0eceabae619edd11",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "305b0d60dfbfc370f87ac1fbb27a9b37db0fae6689b58123670638f52b9a2636",
    "source_lines": "L8030-L8109",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R020"
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
  "stable_id": "BRD-WS-15-R020",
  "title": "Business Domain không cần biết Connector đang sử dụng Profile nào",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R021 — Scheduler luôn Publish Event

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
      "requirement_id": "BRD-WS-15-R021",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "a806247d72a200c6641010c9d9775d088f661fd975dce5f3a39d9664f56f27bd"
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
        "BRD-WS-15-R021-AC001",
        "BRD-WS-15-R021-AC002",
        "BRD-WS-15-R021-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R021-O001",
      "obligation_text": "Scheduler luôn Publish Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Scheduler luôn Publish Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-021",
    "previous_temporary_key": "TMP-BRD-WS-15-021",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "26. Scheduler Event",
    "source_context_sha256": "2ed9a73a80a7abcb1dd76d776848940b0751afae088f5883f710138be984ef28",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "a806247d72a200c6641010c9d9775d088f661fd975dce5f3a39d9664f56f27bd",
    "source_lines": "L8111-L8186",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R021"
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
  "stable_id": "BRD-WS-15-R021",
  "title": "Scheduler luôn Publish Event",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R022 — Business Domain không cần biết Event đến từ hệ thống nào

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
      "requirement_id": "BRD-WS-15-R022",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "2a8c8b64c8b22c3dd10b2bb584640852ab0842c68535d9ad94974ea8d95c5462"
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
        "BRD-WS-15-R022-AC001",
        "BRD-WS-15-R022-AC002",
        "BRD-WS-15-R022-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R022-O001",
      "obligation_text": "Business Domain không cần biết Event đến từ hệ thống nào"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain không cần biết Event đến từ hệ thống nào.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-022",
    "previous_temporary_key": "TMP-BRD-WS-15-022",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "29. Canonical Event Model",
    "source_context_sha256": "2846b12872f324c878232dd433fd6b3b10ed0126da20e6251262e73006fd49eb",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "2a8c8b64c8b22c3dd10b2bb584640852ab0842c68535d9ad94974ea8d95c5462",
    "source_lines": "L8188-L8263",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R022"
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
  "stable_id": "BRD-WS-15-R022",
  "title": "Business Domain không cần biết Event đến từ hệ thống nào",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R023 — Mỗi Connector phải khai báo Capability

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005",
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R023",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "bc95f0c14a051619d82059620b45d27d19d80d1e76cbc61a6ddab14871225113"
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
        "BRD-WS-15-R023-AC001",
        "BRD-WS-15-R023-AC002",
        "BRD-WS-15-R023-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R023-O001",
      "obligation_text": "Mỗi Connector phải khai báo Capability"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Connector phải khai báo Capability.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005",
      "P2-DEC-006"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-023",
    "previous_temporary_key": "TMP-BRD-WS-15-023",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "32. Integration Capability Matrix",
    "source_context_sha256": "6b7eafde4dae44bdb5e7c0cf59ee61d2d02652c005eefdb9316101551e4f6d6d",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "bc95f0c14a051619d82059620b45d27d19d80d1e76cbc61a6ddab14871225113",
    "source_lines": "L8265-L8346",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R023"
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
  "stable_id": "BRD-WS-15-R023",
  "title": "Mỗi Connector phải khai báo Capability",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R024 — Connector chỉ được phép xử lý giao dịch khi ở trạng thái Active

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "Active permits further validation; it does not guarantee downstream success"
    ],
    "concrete_bindings": [
      {
        "from_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-15-R024.FROM_STATE"
            ],
            "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
            "source_type": "SOURCE_LITERAL",
            "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
          },
          "identifier": "BRD-WS-15-R024.FROM_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.FROM_STATE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
            "source_lines": "L831",
            "source_section": "33. Connector Lifecycle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.FROM_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "prohibited_state": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-15-R024.PROHIBITED_STATE"
            ],
            "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
            "source_type": "SOURCE_LITERAL",
            "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
          },
          "identifier": "BRD-WS-15-R024.PROHIBITED_STATE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.PROHIBITED_STATE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
            "source_lines": "L831",
            "source_section": "33. Connector Lifecycle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_ID",
            "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.PROHIBITED_STATE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_ID"
        },
        "state_machine": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
            "source_type": "SOURCE_LITERAL",
            "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
          },
          "identifier": "BRD-WS-15-R024.STATE_MACHINE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.STATE_MACHINE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
            "source_lines": "L831",
            "source_section": "33. Connector Lifecycle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "STATE_MACHINE_ID",
            "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.STATE_MACHINE",
            "version": "1.0.0"
          },
          "semantic_type": "STATE_MACHINE_ID"
        },
        "trigger": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
            "source_type": "SOURCE_LITERAL",
            "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
          },
          "identifier": "BRD-WS-15-R024.TRIGGER",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.TRIGGER.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
            "source_lines": "L831",
            "source_section": "33. Connector Lifecycle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.TRIGGER",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-15-R024",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Non-Active Connector processes a transaction"
    ],
    "operator_composition": [
      "STATE_TRANSITION_REJECTED"
    ],
    "positive_oracle": [
      "Only Active Connector processes the transaction"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-006"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
      "source_lines": "L831",
      "source_section": "33. Connector Lifecycle"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
          "source_type": "SOURCE_LITERAL",
          "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
        },
        "identifier": "BRD-WS-15-R024.BRD-WS-15-R024.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-15-R024.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-006"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-15.md",
          "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
          "source_lines": "L831",
          "source_section": "33. Connector Lifecycle"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-15-R024.BRD-WS-15-R024.BRD-WS-15-R024.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-15-R024.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.CONNECTOR_ID",
        "FIELD.CONNECTOR_STATE",
        "FIELD.TRANSACTION_ID",
        "FIELD.PROCESSING_RESULT",
        "FIELD.REASON"
      ],
      "producer": "BRD-WS-15-R024.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-15-R024.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.CONNECTOR_ID",
        "FIELD.CONNECTOR_STATE",
        "FIELD.TRANSACTION_ID",
        "FIELD.PROCESSING_RESULT",
        "FIELD.REASON"
      ],
      "required_values_or_hashes": [
        "BRD-WS-15-R024.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-15-R024.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-15-R024.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-15-R024-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED",
          "evaluator_consumed_bindings": [
            "from_state",
            "prohibited_state",
            "state_machine",
            "trigger"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
              "source_type": "SOURCE_LITERAL",
              "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
            },
            "identifier": "BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-006"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-15.md",
              "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
              "source_lines": "L831",
              "source_section": "33. Connector Lifecycle"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-15-R024.BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
              "source_type": "SOURCE_LITERAL",
              "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
            },
            "identifier": "BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-006"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-15.md",
              "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
              "source_lines": "L831",
              "source_section": "33. Connector Lifecycle"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.CANONICAL.RESULT",
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
                    "BRD-WS-15-R024.FROM_STATE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
                },
                "identifier": "BRD-WS-15-R024.FROM_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.FROM_STATE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
                  "source_lines": "L831",
                  "source_section": "33. Connector Lifecycle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.FROM_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "prohibited_state": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-15-R024.PROHIBITED_STATE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
                },
                "identifier": "BRD-WS-15-R024.PROHIBITED_STATE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.PROHIBITED_STATE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
                  "source_lines": "L831",
                  "source_section": "33. Connector Lifecycle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.PROHIBITED_STATE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "state_machine": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
                },
                "identifier": "BRD-WS-15-R024.STATE_MACHINE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.STATE_MACHINE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
                  "source_lines": "L831",
                  "source_section": "33. Connector Lifecycle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_MACHINE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.STATE_MACHINE",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_MACHINE_ID"
              },
              "trigger": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
                },
                "identifier": "BRD-WS-15-R024.TRIGGER",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.TRIGGER.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
                  "source_lines": "L831",
                  "source_section": "33. Connector Lifecycle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.TRIGGER",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
                },
                "identifier": "BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
                  "source_lines": "L831",
                  "source_section": "33. Connector Lifecycle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
                  "source_type": "SOURCE_LITERAL",
                  "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
                },
                "identifier": "BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-006"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-15.md",
                  "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
                  "source_lines": "L831",
                  "source_section": "33. Connector Lifecycle"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "STATE_ID",
                  "resolver_id": "OBSERVE.BRD-WS-15-R024.BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "STATE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
                "source_type": "SOURCE_LITERAL",
                "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
              },
              "identifier": "BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
                "source_lines": "L831",
                "source_section": "33. Connector Lifecycle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-15-R024.BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "STATE_TRANSITION_REJECTED"
          },
          "obligation_id": "BRD-WS-15-R024-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
              "source_type": "SOURCE_LITERAL",
              "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
            },
            "identifier": "BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-006"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-15.md",
              "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
              "source_lines": "L831",
              "source_section": "33. Connector Lifecycle"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "STATE_ID",
              "resolver_id": "OBSERVE.BRD-WS-15-R024.BRD-WS-15-R024.BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "STATE_ID"
          },
          "operator_id": "STATE_TRANSITION_REJECTED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "from_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-15-R024.FROM_STATE"
                ],
                "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
                "source_type": "SOURCE_LITERAL",
                "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
              },
              "identifier": "BRD-WS-15-R024.FROM_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.FROM_STATE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
                "source_lines": "L831",
                "source_section": "33. Connector Lifecycle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.FROM_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "prohibited_state": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-15-R024.PROHIBITED_STATE"
                ],
                "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
                "source_type": "SOURCE_LITERAL",
                "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
              },
              "identifier": "BRD-WS-15-R024.PROHIBITED_STATE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.PROHIBITED_STATE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
                "source_lines": "L831",
                "source_section": "33. Connector Lifecycle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.PROHIBITED_STATE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            },
            "state_machine": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
                "source_type": "SOURCE_LITERAL",
                "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
              },
              "identifier": "BRD-WS-15-R024.STATE_MACHINE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.STATE_MACHINE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
                "source_lines": "L831",
                "source_section": "33. Connector Lifecycle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_MACHINE_ID",
                "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.STATE_MACHINE",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_MACHINE_ID"
            },
            "trigger": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
                "source_type": "SOURCE_LITERAL",
                "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
              },
              "identifier": "BRD-WS-15-R024.TRIGGER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED.TRIGGER.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-006"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-15.md",
                "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
                "source_lines": "L831",
                "source_section": "33. Connector Lifecycle"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.BRD-WS-15-R024.BRD-WS-15-R024.TRIGGER",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "Active permits further validation; it does not guarantee downstream success"
      ],
      "contract_ast_sha256": "2fae933bdd723aa769fa0aaf55a1e68b0cfa8e0fe92e50a39833a6978f24e6e6",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-15-R024",
      "criticality": "HIGH",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-15.md#33. Connector Lifecycle",
            "source_type": "SOURCE_LITERAL",
            "version": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad"
          },
          "identifier": "BRD-WS-15-R024.BRD-WS-15-R024.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-15-R024.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-006"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-15.md",
            "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
            "source_lines": "L831",
            "source_section": "33. Connector Lifecycle"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-15-R024.BRD-WS-15-R024.BRD-WS-15-R024.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-15-R024.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.CONNECTOR_ID",
          "FIELD.CONNECTOR_STATE",
          "FIELD.TRANSACTION_ID",
          "FIELD.PROCESSING_RESULT",
          "FIELD.REASON"
        ],
        "producer": "BRD-WS-15-R024.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-15-R024.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.CONNECTOR_ID",
          "FIELD.CONNECTOR_STATE",
          "FIELD.TRANSACTION_ID",
          "FIELD.PROCESSING_RESULT",
          "FIELD.REASON"
        ],
        "required_values_or_hashes": [
          "BRD-WS-15-R024.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-15-R024.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-15-R024.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-1079EF00E64B508240A2",
        "P2C-C4-FX-1A0E8632C82BC7CDF3EB",
        "P2C-C4-FX-1DAF1119733FADFAF355"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Non-Active Connector processes a transaction"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-15-R024-O001",
          "obligation_text": "Connector chỉ được phép xử lý giao dịch khi ở trạng thái Active"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-15-R024.O1.1.STATE_TRANSITION_REJECTED"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-15-R024-O001"
        }
      ],
      "operator_composition": [
        "STATE_TRANSITION_REJECTED"
      ],
      "positive_oracles": [
        "Only Active Connector processes the transaction"
      ],
      "preconditions": [
        "Connector lifecycle state is resolved"
      ],
      "prohibitions": [
        "Non-Active Connector processes a transaction"
      ],
      "requirement_id": "BRD-WS-15-R024",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-006"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-15.md",
        "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
        "source_lines": "L831",
        "source_section": "33. Connector Lifecycle"
      },
      "source_statement": "Connector chỉ được phép xử lý giao dịch khi ở trạng thái Active.",
      "surrounding_source_context": "### BRD-WS-15-R024 — Connector chỉ được phép xử lý giao dịch khi ở trạng thái Active"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-15-R024",
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
        "BRD-WS-15-R024-AC001",
        "BRD-WS-15-R024-AC002",
        "BRD-WS-15-R024-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R024-O001",
      "obligation_text": "Connector chỉ được phép xử lý giao dịch khi ở trạng thái Active"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector chỉ được phép xử lý giao dịch khi ở trạng thái Active.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-024",
    "previous_temporary_key": "TMP-BRD-WS-15-024",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "33. Connector Lifecycle",
    "source_context_sha256": "646962811da1413c47ede68481b5d2457555fd25f59473729bb668cc4be11486",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "59da518454f9537cecc7c16a3defeaad840d7442dcba16d5000498fff3ba5dad",
    "source_lines": "L8348-L9344",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R024"
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
  "stable_id": "BRD-WS-15-R024",
  "title": "Connector chỉ được phép xử lý giao dịch khi ở trạng thái Active",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R025 — Business Domain không cần biết Runtime Profile đang được sử dụng

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
      "requirement_id": "BRD-WS-15-R025",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "1afbf8c899e53ba7935f1fb5c85c9fc6d7b1634be4ed23d52d4c96c49246a88c"
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
        "BRD-WS-15-R025-AC001",
        "BRD-WS-15-R025-AC002",
        "BRD-WS-15-R025-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R025-O001",
      "obligation_text": "Business Domain không cần biết Runtime Profile đang được sử dụng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain không cần biết Runtime Profile đang được sử dụng.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-025",
    "previous_temporary_key": "TMP-BRD-WS-15-025",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "34. Connector Runtime Profile",
    "source_context_sha256": "c02c28fbbf3235756d11f12df5a0a2167cbda6a60fd9ee520f27c89ad1da1ab8",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "1afbf8c899e53ba7935f1fb5c85c9fc6d7b1634be4ed23d52d4c96c49246a88c",
    "source_lines": "L9346-L9421",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R025"
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
  "stable_id": "BRD-WS-15-R025",
  "title": "Business Domain không cần biết Runtime Profile đang được sử dụng",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R026 — API Gateway là thành phần bắt buộc

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R026",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "2d8998b7d6420ce0e148306f54bd3c9661c1ad9cb1c941ebe90b88fdd92119d2"
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
        "BRD-WS-15-R026-AC001",
        "BRD-WS-15-R026-AC002",
        "BRD-WS-15-R026-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R026-O001",
      "obligation_text": "API Gateway là thành phần bắt buộc"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "API Gateway là thành phần bắt buộc.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-026",
    "previous_temporary_key": "TMP-BRD-WS-15-026",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-002",
    "source_context_sha256": "6d1f156497f7d7655fbebca3c03fb857072962cf12c840eadf4b0aab06a87984",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "2d8998b7d6420ce0e148306f54bd3c9661c1ad9cb1c941ebe90b88fdd92119d2",
    "source_lines": "L9423-L9504",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R026"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-002"
    ],
    "derived_requirements": []
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R026",
  "title": "API Gateway là thành phần bắt buộc",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R027 — Integration Platform hỗ trợ đầy đủ: REST API

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
      "requirement_id": "BRD-WS-15-R027",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "fcf9fe03a273b1e6c14872a2d4473b07c9ec184e523edc5521668e843f280323"
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
        "BRD-WS-15-R027-AC001",
        "BRD-WS-15-R027-AC002",
        "BRD-WS-15-R027-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R027-O001",
      "obligation_text": "Integration Platform hỗ trợ đầy đủ: REST API"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Integration Platform hỗ trợ đầy đủ: REST API.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-001",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R027",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-001",
    "source_context_sha256": "feba63776c4d2c75ef5f767a8cd3a7f770f7f7c9ab06b1d3a120720328d27d40",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "fcf9fe03a273b1e6c14872a2d4473b07c9ec184e523edc5521668e843f280323",
    "source_fingerprint_before_c3": "fcf9fe03a273b1e6c14872a2d4473b07c9ec184e523edc5521668e843f280323",
    "source_lines": "L9506-L9598",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R027"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-001"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-001"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R027",
  "title": "Integration Platform hỗ trợ đầy đủ: REST API",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R028 — Integration Platform hỗ trợ đầy đủ: Webhook

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
      "requirement_id": "BRD-WS-15-R028",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "e2bbb588b47f30981630fac1ac07c7d75b5934ac99a6424faf9f0b53f3d28c11"
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
        "BRD-WS-15-R028-AC001",
        "BRD-WS-15-R028-AC002",
        "BRD-WS-15-R028-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R028-O001",
      "obligation_text": "Integration Platform hỗ trợ đầy đủ: Webhook"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Integration Platform hỗ trợ đầy đủ: Webhook.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-001",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R028",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-001",
    "source_context_sha256": "feba63776c4d2c75ef5f767a8cd3a7f770f7f7c9ab06b1d3a120720328d27d40",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "e2bbb588b47f30981630fac1ac07c7d75b5934ac99a6424faf9f0b53f3d28c11",
    "source_fingerprint_before_c3": "e2bbb588b47f30981630fac1ac07c7d75b5934ac99a6424faf9f0b53f3d28c11",
    "source_lines": "L9600-L9692",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R028"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-001"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-001"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R028",
  "title": "Integration Platform hỗ trợ đầy đủ: Webhook",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R029 — Integration Platform hỗ trợ đầy đủ: Event Bus

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
      "requirement_id": "BRD-WS-15-R029",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "4f6c06fc841c962e4d5609ea277eca18672f852c6bdd823ac0309d5cc86ae087"
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
        "BRD-WS-15-R029-AC001",
        "BRD-WS-15-R029-AC002",
        "BRD-WS-15-R029-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R029-O001",
      "obligation_text": "Integration Platform hỗ trợ đầy đủ: Event Bus"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Integration Platform hỗ trợ đầy đủ: Event Bus.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-001",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R029",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-001",
    "source_context_sha256": "feba63776c4d2c75ef5f767a8cd3a7f770f7f7c9ab06b1d3a120720328d27d40",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "4f6c06fc841c962e4d5609ea277eca18672f852c6bdd823ac0309d5cc86ae087",
    "source_fingerprint_before_c3": "4f6c06fc841c962e4d5609ea277eca18672f852c6bdd823ac0309d5cc86ae087",
    "source_lines": "L9694-L9786",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R029"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-001"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-001"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R029",
  "title": "Integration Platform hỗ trợ đầy đủ: Event Bus",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R030 — Integration Platform hỗ trợ đầy đủ: Message Queue

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
      "requirement_id": "BRD-WS-15-R030",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "11334c15d561595f3b0aef8ac68b6d29ba97a052fac12cc343c435f8748f5222"
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
        "BRD-WS-15-R030-AC001",
        "BRD-WS-15-R030-AC002",
        "BRD-WS-15-R030-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R030-O001",
      "obligation_text": "Integration Platform hỗ trợ đầy đủ: Message Queue"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Integration Platform hỗ trợ đầy đủ: Message Queue.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-001",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R030",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-001",
    "source_context_sha256": "feba63776c4d2c75ef5f767a8cd3a7f770f7f7c9ab06b1d3a120720328d27d40",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "11334c15d561595f3b0aef8ac68b6d29ba97a052fac12cc343c435f8748f5222",
    "source_fingerprint_before_c3": "11334c15d561595f3b0aef8ac68b6d29ba97a052fac12cc343c435f8748f5222",
    "source_lines": "L9788-L9880",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R030"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-001"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-001"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R030",
  "title": "Integration Platform hỗ trợ đầy đủ: Message Queue",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R031 — Integration Platform hỗ trợ đầy đủ: Batch Import

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
      "requirement_id": "BRD-WS-15-R031",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "22996b8c8e2860b4eef66150cafbeb240d05ce8a083277a5ae188cd81f2da4be"
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
        "BRD-WS-15-R031-AC001",
        "BRD-WS-15-R031-AC002",
        "BRD-WS-15-R031-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R031-O001",
      "obligation_text": "Integration Platform hỗ trợ đầy đủ: Batch Import"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Integration Platform hỗ trợ đầy đủ: Batch Import.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-001",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R031",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-001",
    "source_context_sha256": "feba63776c4d2c75ef5f767a8cd3a7f770f7f7c9ab06b1d3a120720328d27d40",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "22996b8c8e2860b4eef66150cafbeb240d05ce8a083277a5ae188cd81f2da4be",
    "source_fingerprint_before_c3": "22996b8c8e2860b4eef66150cafbeb240d05ce8a083277a5ae188cd81f2da4be",
    "source_lines": "L9882-L9974",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R031"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-001"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-001"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R031",
  "title": "Integration Platform hỗ trợ đầy đủ: Batch Import",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R032 — Integration Platform hỗ trợ đầy đủ: Batch Export

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
      "requirement_id": "BRD-WS-15-R032",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "1f0acd51e02ea6725ef78d3f4ab8ca79d55c352d2e14dc8f920cd857afcd9916"
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
        "BRD-WS-15-R032-AC001",
        "BRD-WS-15-R032-AC002",
        "BRD-WS-15-R032-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R032-O001",
      "obligation_text": "Integration Platform hỗ trợ đầy đủ: Batch Export"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Integration Platform hỗ trợ đầy đủ: Batch Export.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-001",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R032",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-001",
    "source_context_sha256": "feba63776c4d2c75ef5f767a8cd3a7f770f7f7c9ab06b1d3a120720328d27d40",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "1f0acd51e02ea6725ef78d3f4ab8ca79d55c352d2e14dc8f920cd857afcd9916",
    "source_fingerprint_before_c3": "1f0acd51e02ea6725ef78d3f4ab8ca79d55c352d2e14dc8f920cd857afcd9916",
    "source_lines": "L9976-L10068",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R032"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-001"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-001"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R032",
  "title": "Integration Platform hỗ trợ đầy đủ: Batch Export",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R033 — Connector là Business Object

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R033",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "23bcf6f28f55083a5d25930ab8394b4e95ad16975edde2a5ae662d7d313517df"
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
        "BRD-WS-15-R033-AC001",
        "BRD-WS-15-R033-AC002",
        "BRD-WS-15-R033-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R033-O001",
      "obligation_text": "Connector là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector là Business Object.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R033",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Connector",
    "source_context_sha256": "b4b269d9d838a068eef5bcaa82adf0a7ae24e95067a42c36d88725768e0eafbe",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "23bcf6f28f55083a5d25930ab8394b4e95ad16975edde2a5ae662d7d313517df",
    "source_fingerprint_before_c3": "23bcf6f28f55083a5d25930ab8394b4e95ad16975edde2a5ae662d7d313517df",
    "source_lines": "L10070-L10164",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R033"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-003"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R033",
  "title": "Connector là Business Object",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R034 — Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R034",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "4c30c659ec2279b810c284a75e4618a3b5cb366b0854c22d8b6c81c8994d94f5"
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
        "BRD-WS-15-R034-AC001",
        "BRD-WS-15-R034-AC002",
        "BRD-WS-15-R034-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R034-O001",
      "obligation_text": "Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R034",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Connector",
    "source_context_sha256": "b4b269d9d838a068eef5bcaa82adf0a7ae24e95067a42c36d88725768e0eafbe",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "4c30c659ec2279b810c284a75e4618a3b5cb366b0854c22d8b6c81c8994d94f5",
    "source_fingerprint_before_c3": "4c30c659ec2279b810c284a75e4618a3b5cb366b0854c22d8b6c81c8994d94f5",
    "source_lines": "L10166-L10260",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R034"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-003"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R034",
  "title": "Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R035 — Business Logic không được đặt trong Connector

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R035",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "6ffdde9491870ba7d3bae71e05e883393175e9d3b3ebde601780f7ac17b0312f"
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
        "BRD-WS-15-R035-AC001",
        "BRD-WS-15-R035-AC002",
        "BRD-WS-15-R035-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R035-O001",
      "obligation_text": "Business Logic không được đặt trong Connector"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Logic không được đặt trong Connector.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-003",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R035",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Connector",
    "source_context_sha256": "b4b269d9d838a068eef5bcaa82adf0a7ae24e95067a42c36d88725768e0eafbe",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "6ffdde9491870ba7d3bae71e05e883393175e9d3b3ebde601780f7ac17b0312f",
    "source_fingerprint_before_c3": "6ffdde9491870ba7d3bae71e05e883393175e9d3b3ebde601780f7ac17b0312f",
    "source_lines": "L10262-L10356",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R035"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-003"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-003"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R035",
  "title": "Business Logic không được đặt trong Connector",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R036 — Business Event là Business Object

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
      "requirement_id": "BRD-WS-15-R036",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "59d7823ac02df894d66976306f95ae970b34702b29653211e8baf5f64c081b8d"
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
        "BRD-WS-15-R036-AC001",
        "BRD-WS-15-R036-AC002",
        "BRD-WS-15-R036-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R036-O001",
      "obligation_text": "Business Event là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event là Business Object.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R036",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Business Event",
    "source_context_sha256": "a32cea09e78e1790291b8be66975292424b4ef17c756b233ee9a07277d0ec8bd",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "59d7823ac02df894d66976306f95ae970b34702b29653211e8baf5f64c081b8d",
    "source_fingerprint_before_c3": "59d7823ac02df894d66976306f95ae970b34702b29653211e8baf5f64c081b8d",
    "source_lines": "L10358-L10450",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R036"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-006"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R036",
  "title": "Business Event là Business Object",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R037 — Mọi Business Domain đều Publish Business Event

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
      "requirement_id": "BRD-WS-15-R037",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "d36cc7e0cbe3e6db7068517652b6948d53c4275a7a5034d4f3cc18d365c566a2"
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
        "BRD-WS-15-R037-AC001",
        "BRD-WS-15-R037-AC002",
        "BRD-WS-15-R037-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R037-O001",
      "obligation_text": "Mọi Business Domain đều Publish Business Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Business Domain đều Publish Business Event.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R037",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Business Event",
    "source_context_sha256": "a32cea09e78e1790291b8be66975292424b4ef17c756b233ee9a07277d0ec8bd",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "d36cc7e0cbe3e6db7068517652b6948d53c4275a7a5034d4f3cc18d365c566a2",
    "source_fingerprint_before_c3": "d36cc7e0cbe3e6db7068517652b6948d53c4275a7a5034d4f3cc18d365c566a2",
    "source_lines": "L10452-L10544",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R037"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-006"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R037",
  "title": "Mọi Business Domain đều Publish Business Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R038 — Business Domain đăng ký Subscribe Business Event

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
      "requirement_id": "BRD-WS-15-R038",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "1425167ddd80dcbc938167158d14e7f8b8037cc8379a0c92e7b6b3775746e6cf"
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
        "BRD-WS-15-R038-AC001",
        "BRD-WS-15-R038-AC002",
        "BRD-WS-15-R038-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R038-O001",
      "obligation_text": "Business Domain đăng ký Subscribe Business Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain đăng ký Subscribe Business Event.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-007",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R038",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Event Subscription",
    "source_context_sha256": "bac815a32b1342602e87b110b410c7d7123f30ef7b6dab5e98047a157c9fc326",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "1425167ddd80dcbc938167158d14e7f8b8037cc8379a0c92e7b6b3775746e6cf",
    "source_fingerprint_before_c3": "1425167ddd80dcbc938167158d14e7f8b8037cc8379a0c92e7b6b3775746e6cf",
    "source_lines": "L10546-L10638",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R038"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-007"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-007"
    ]
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R038",
  "title": "Business Domain đăng ký Subscribe Business Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R039 — Publisher không biết Subscriber

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
      "requirement_id": "BRD-WS-15-R039",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "ad210033e495efec3a9e53396e1ce35e788aac6e9710317853ef1c77920785a7"
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
        "BRD-WS-15-R039-AC001",
        "BRD-WS-15-R039-AC002",
        "BRD-WS-15-R039-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R039-O001",
      "obligation_text": "Publisher không biết Subscriber"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Publisher không biết Subscriber.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-007",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R039",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Event Subscription",
    "source_context_sha256": "bac815a32b1342602e87b110b410c7d7123f30ef7b6dab5e98047a157c9fc326",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "ad210033e495efec3a9e53396e1ce35e788aac6e9710317853ef1c77920785a7",
    "source_fingerprint_before_c3": "ad210033e495efec3a9e53396e1ce35e788aac6e9710317853ef1c77920785a7",
    "source_lines": "L10640-L10732",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R039"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-007"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-007"
    ]
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R039",
  "title": "Publisher không biết Subscriber",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R040 — Event Bus chịu trách nhiệm Routing và Delivery

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
      "requirement_id": "BRD-WS-15-R040",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "6a3d3fc497b45beb24752349de610eab34a14b5e64e7dfe6cf67f9d4ab20eecb"
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
        "BRD-WS-15-R040-AC001",
        "BRD-WS-15-R040-AC002",
        "BRD-WS-15-R040-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R040-O001",
      "obligation_text": "Event Bus chịu trách nhiệm Routing và Delivery"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Event Bus chịu trách nhiệm Routing và Delivery.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-007",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R040",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Event Subscription",
    "source_context_sha256": "bac815a32b1342602e87b110b410c7d7123f30ef7b6dab5e98047a157c9fc326",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "6a3d3fc497b45beb24752349de610eab34a14b5e64e7dfe6cf67f9d4ab20eecb",
    "source_fingerprint_before_c3": "6a3d3fc497b45beb24752349de610eab34a14b5e64e7dfe6cf67f9d4ab20eecb",
    "source_lines": "L10734-L10826",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R040"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-007"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-007"
    ]
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R040",
  "title": "Event Bus chịu trách nhiệm Routing và Delivery",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R041 — Business Service Registry là Business Object. Registry quản lý: Service

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
      "requirement_id": "BRD-WS-15-R041",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "cacd37a32d3288a0214157138f3a15ef831e26b4d7c8d9cfe6b25ee39a0bbf3b"
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
        "BRD-WS-15-R041-AC001",
        "BRD-WS-15-R041-AC003",
        "BRD-WS-15-R041-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R041-O001",
      "obligation_text": "Business Service Registry là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-15-R041-AC002",
        "BRD-WS-15-R041-AC003",
        "BRD-WS-15-R041-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R041-O002",
      "obligation_text": "Registry quản lý: Service"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Service Registry là Business Object. Registry quản lý: Service.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-023",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R041",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Business Service Registry",
    "source_context_sha256": "cffc01224270ac2af85b76b8866141a249b861e7834694115b140112ebcc8665",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "cacd37a32d3288a0214157138f3a15ef831e26b4d7c8d9cfe6b25ee39a0bbf3b",
    "source_fingerprint_before_c3": "cacd37a32d3288a0214157138f3a15ef831e26b4d7c8d9cfe6b25ee39a0bbf3b",
    "source_lines": "L10828-L10930",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R041"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-023"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-023"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R041",
  "title": "Business Service Registry là Business Object. Registry quản lý: Service",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R042 — Business Service Registry là Business Object. Registry quản lý: API

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
      "requirement_id": "BRD-WS-15-R042",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "f54177bee4ab9b23f9ff7021950a5b64d64930aa3f36f6f46cb002d3cd188ec0"
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
        "BRD-WS-15-R042-AC001",
        "BRD-WS-15-R042-AC003",
        "BRD-WS-15-R042-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R042-O001",
      "obligation_text": "Business Service Registry là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-15-R042-AC002",
        "BRD-WS-15-R042-AC003",
        "BRD-WS-15-R042-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R042-O002",
      "obligation_text": "Registry quản lý: API"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Service Registry là Business Object. Registry quản lý: API.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-023",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R042",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Business Service Registry",
    "source_context_sha256": "cffc01224270ac2af85b76b8866141a249b861e7834694115b140112ebcc8665",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "f54177bee4ab9b23f9ff7021950a5b64d64930aa3f36f6f46cb002d3cd188ec0",
    "source_fingerprint_before_c3": "f54177bee4ab9b23f9ff7021950a5b64d64930aa3f36f6f46cb002d3cd188ec0",
    "source_lines": "L10932-L11034",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R042"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-023"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-023"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R042",
  "title": "Business Service Registry là Business Object. Registry quản lý: API",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R043 — Business Service Registry là Business Object. Registry quản lý: Published Event

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
      "requirement_id": "BRD-WS-15-R043",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "8b31ea0a0637a3f2d26354f6858b34d04c090ce5f021ba0eef2445bdcd0b3240"
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
        "BRD-WS-15-R043-AC001",
        "BRD-WS-15-R043-AC003",
        "BRD-WS-15-R043-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R043-O001",
      "obligation_text": "Business Service Registry là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-15-R043-AC002",
        "BRD-WS-15-R043-AC003",
        "BRD-WS-15-R043-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R043-O002",
      "obligation_text": "Registry quản lý: Published Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Service Registry là Business Object. Registry quản lý: Published Event.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-023",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R043",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Business Service Registry",
    "source_context_sha256": "cffc01224270ac2af85b76b8866141a249b861e7834694115b140112ebcc8665",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "8b31ea0a0637a3f2d26354f6858b34d04c090ce5f021ba0eef2445bdcd0b3240",
    "source_fingerprint_before_c3": "8b31ea0a0637a3f2d26354f6858b34d04c090ce5f021ba0eef2445bdcd0b3240",
    "source_lines": "L11036-L11138",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R043"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-023"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-023"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R043",
  "title": "Business Service Registry là Business Object. Registry quản lý: Published Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R044 — Business Service Registry là Business Object. Registry quản lý: Consumed Event

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
      "requirement_id": "BRD-WS-15-R044",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "8d42965a756b6ae0876f7b727a29f719377499ce23008bfceed4b3428268f408"
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
        "BRD-WS-15-R044-AC001",
        "BRD-WS-15-R044-AC003",
        "BRD-WS-15-R044-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R044-O001",
      "obligation_text": "Business Service Registry là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-15-R044-AC002",
        "BRD-WS-15-R044-AC003",
        "BRD-WS-15-R044-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R044-O002",
      "obligation_text": "Registry quản lý: Consumed Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Service Registry là Business Object. Registry quản lý: Consumed Event.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-023",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R044",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Business Service Registry",
    "source_context_sha256": "cffc01224270ac2af85b76b8866141a249b861e7834694115b140112ebcc8665",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "8d42965a756b6ae0876f7b727a29f719377499ce23008bfceed4b3428268f408",
    "source_fingerprint_before_c3": "8d42965a756b6ae0876f7b727a29f719377499ce23008bfceed4b3428268f408",
    "source_lines": "L11140-L11242",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R044"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-023"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-023"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R044",
  "title": "Business Service Registry là Business Object. Registry quản lý: Consumed Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R045 — Business Service Registry là Business Object. Registry quản lý: Dependency

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
      "requirement_id": "BRD-WS-15-R045",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "ad8c9c3f3e7f0d19728395aff49a4001a06a0d96f551118501287c20c7a0e7fa"
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
        "BRD-WS-15-R045-AC001",
        "BRD-WS-15-R045-AC003",
        "BRD-WS-15-R045-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R045-O001",
      "obligation_text": "Business Service Registry là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-15-R045-AC002",
        "BRD-WS-15-R045-AC003",
        "BRD-WS-15-R045-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R045-O002",
      "obligation_text": "Registry quản lý: Dependency"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Service Registry là Business Object. Registry quản lý: Dependency.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-023",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R045",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Business Service Registry",
    "source_context_sha256": "cffc01224270ac2af85b76b8866141a249b861e7834694115b140112ebcc8665",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "ad8c9c3f3e7f0d19728395aff49a4001a06a0d96f551118501287c20c7a0e7fa",
    "source_fingerprint_before_c3": "ad8c9c3f3e7f0d19728395aff49a4001a06a0d96f551118501287c20c7a0e7fa",
    "source_lines": "L11244-L11346",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R045"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-023"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-023"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R045",
  "title": "Business Service Registry là Business Object. Registry quản lý: Dependency",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R046 — Business Service Registry là Business Object. Registry quản lý: Owner

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
      "requirement_id": "BRD-WS-15-R046",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "fc8354d11f62484c9d617facc8be951f8b5bc9951a40ca9e0dea14820065e02d"
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
        "BRD-WS-15-R046-AC001",
        "BRD-WS-15-R046-AC003",
        "BRD-WS-15-R046-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R046-O001",
      "obligation_text": "Business Service Registry là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-15-R046-AC002",
        "BRD-WS-15-R046-AC003",
        "BRD-WS-15-R046-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R046-O002",
      "obligation_text": "Registry quản lý: Owner"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Service Registry là Business Object. Registry quản lý: Owner.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-023",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R046",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Business Service Registry",
    "source_context_sha256": "cffc01224270ac2af85b76b8866141a249b861e7834694115b140112ebcc8665",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "fc8354d11f62484c9d617facc8be951f8b5bc9951a40ca9e0dea14820065e02d",
    "source_fingerprint_before_c3": "fc8354d11f62484c9d617facc8be951f8b5bc9951a40ca9e0dea14820065e02d",
    "source_lines": "L11348-L11450",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R046"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-023"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-023"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R046",
  "title": "Business Service Registry là Business Object. Registry quản lý: Owner",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R047 — Business Service Registry là Business Object. Registry quản lý: Version

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
      "requirement_id": "BRD-WS-15-R047",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "c03efa7a891c9b71495ae307befd58e1e5421ba5269946a73bca4150c7450f2c"
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
        "BRD-WS-15-R047-AC001",
        "BRD-WS-15-R047-AC003",
        "BRD-WS-15-R047-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R047-O001",
      "obligation_text": "Business Service Registry là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-15-R047-AC002",
        "BRD-WS-15-R047-AC003",
        "BRD-WS-15-R047-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R047-O002",
      "obligation_text": "Registry quản lý: Version"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Service Registry là Business Object. Registry quản lý: Version.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-023",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R047",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Business Service Registry",
    "source_context_sha256": "cffc01224270ac2af85b76b8866141a249b861e7834694115b140112ebcc8665",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "c03efa7a891c9b71495ae307befd58e1e5421ba5269946a73bca4150c7450f2c",
    "source_fingerprint_before_c3": "c03efa7a891c9b71495ae307befd58e1e5421ba5269946a73bca4150c7450f2c",
    "source_lines": "L11452-L11554",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R047"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-023"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-023"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R047",
  "title": "Business Service Registry là Business Object. Registry quản lý: Version",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R048 — Connector Routing Rule là Business Object

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R048",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "f176bb559cb897927c14d9093d48e362a20cf753622ac0f1f36bfb6463365db3"
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
        "BRD-WS-15-R048-AC001",
        "BRD-WS-15-R048-AC002",
        "BRD-WS-15-R048-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R048-O001",
      "obligation_text": "Connector Routing Rule là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector Routing Rule là Business Object.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-027",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R048",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "31. Connector Routing Rule",
    "source_context_sha256": "2b5ae149f16258e6f19e3b618371fa39670739057e5cc4fda0dca2095e684d00",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "f176bb559cb897927c14d9093d48e362a20cf753622ac0f1f36bfb6463365db3",
    "source_fingerprint_before_c3": "f176bb559cb897927c14d9093d48e362a20cf753622ac0f1f36bfb6463365db3",
    "source_lines": "L11556-L11650",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R048"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-027"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-027"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R048",
  "title": "Connector Routing Rule là Business Object",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R049 — Routing Rule được cấu hình

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R049",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "ca39cd50c7cbd4c69c5a78bf72eed8a19d71e2230a2179ab5fee35e9a8df217b"
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
        "BRD-WS-15-R049-AC001",
        "BRD-WS-15-R049-AC002",
        "BRD-WS-15-R049-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R049-O001",
      "obligation_text": "Routing Rule được cấu hình"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Routing Rule được cấu hình.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-027",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R049",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "31. Connector Routing Rule",
    "source_context_sha256": "2b5ae149f16258e6f19e3b618371fa39670739057e5cc4fda0dca2095e684d00",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "ca39cd50c7cbd4c69c5a78bf72eed8a19d71e2230a2179ab5fee35e9a8df217b",
    "source_fingerprint_before_c3": "ca39cd50c7cbd4c69c5a78bf72eed8a19d71e2230a2179ab5fee35e9a8df217b",
    "source_lines": "L11652-L11746",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R049"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-027"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-027"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R049",
  "title": "Routing Rule được cấu hình",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R050 — Business Domain không quyết định Connector

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R050",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "5255e08a528c9cc763d4c79ab7c8fa9ff25fc3f5306f8e55af1b0e3596b71c0c"
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
        "BRD-WS-15-R050-AC001",
        "BRD-WS-15-R050-AC002",
        "BRD-WS-15-R050-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R050-O001",
      "obligation_text": "Business Domain không quyết định Connector"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain không quyết định Connector.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-027",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R050",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "31. Connector Routing Rule",
    "source_context_sha256": "2b5ae149f16258e6f19e3b618371fa39670739057e5cc4fda0dca2095e684d00",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "5255e08a528c9cc763d4c79ab7c8fa9ff25fc3f5306f8e55af1b0e3596b71c0c",
    "source_fingerprint_before_c3": "5255e08a528c9cc763d4c79ab7c8fa9ff25fc3f5306f8e55af1b0e3596b71c0c",
    "source_lines": "L11748-L11842",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R050"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-027"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-027"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R050",
  "title": "Business Domain không quyết định Connector",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R051 — Connector hỗ trợ Lifecycle: Draft

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R051",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "efaf7ea318e3fed538b5fe5e90f69878f46a6d8f44d09af64550518e3c986f18"
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
        "BRD-WS-15-R051-AC001",
        "BRD-WS-15-R051-AC002",
        "BRD-WS-15-R051-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R051-O001",
      "obligation_text": "Connector hỗ trợ Lifecycle: Draft"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector hỗ trợ Lifecycle: Draft.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-029",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R051",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-029",
    "source_context_sha256": "381d81c5ec93ae99263a5596851482557a81362364f9a3697b7362de3afe4299",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "efaf7ea318e3fed538b5fe5e90f69878f46a6d8f44d09af64550518e3c986f18",
    "source_fingerprint_before_c3": "efaf7ea318e3fed538b5fe5e90f69878f46a6d8f44d09af64550518e3c986f18",
    "source_lines": "L11844-L11938",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R051"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-029"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-029"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R051",
  "title": "Connector hỗ trợ Lifecycle: Draft",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R052 — Connector hỗ trợ Lifecycle: Configured

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R052",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "5a80334b24d68622b7d62386ee0bf6096c0ab1cf2cd13b55046238247fc040fc"
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
        "BRD-WS-15-R052-AC001",
        "BRD-WS-15-R052-AC002",
        "BRD-WS-15-R052-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R052-O001",
      "obligation_text": "Connector hỗ trợ Lifecycle: Configured"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector hỗ trợ Lifecycle: Configured.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-029",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R052",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-029",
    "source_context_sha256": "381d81c5ec93ae99263a5596851482557a81362364f9a3697b7362de3afe4299",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "5a80334b24d68622b7d62386ee0bf6096c0ab1cf2cd13b55046238247fc040fc",
    "source_fingerprint_before_c3": "5a80334b24d68622b7d62386ee0bf6096c0ab1cf2cd13b55046238247fc040fc",
    "source_lines": "L11940-L12034",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R052"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-029"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-029"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R052",
  "title": "Connector hỗ trợ Lifecycle: Configured",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R053 — Connector hỗ trợ Lifecycle: Validated

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R053",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "7756d1c12d0a3c95f292af75ce275802f9b2136261a7da675119a8cd1511a9d0"
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
        "BRD-WS-15-R053-AC001",
        "BRD-WS-15-R053-AC002",
        "BRD-WS-15-R053-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R053-O001",
      "obligation_text": "Connector hỗ trợ Lifecycle: Validated"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector hỗ trợ Lifecycle: Validated.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-029",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R053",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-029",
    "source_context_sha256": "381d81c5ec93ae99263a5596851482557a81362364f9a3697b7362de3afe4299",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "7756d1c12d0a3c95f292af75ce275802f9b2136261a7da675119a8cd1511a9d0",
    "source_fingerprint_before_c3": "7756d1c12d0a3c95f292af75ce275802f9b2136261a7da675119a8cd1511a9d0",
    "source_lines": "L12036-L12130",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R053"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-029"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-029"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R053",
  "title": "Connector hỗ trợ Lifecycle: Validated",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R054 — Connector hỗ trợ Lifecycle: Testing

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R054",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "3565cb33697eaf7c5e188f363fed41c5418b7ddcbfb6799a496bdf053afe7af1"
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
        "BRD-WS-15-R054-AC001",
        "BRD-WS-15-R054-AC002",
        "BRD-WS-15-R054-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R054-O001",
      "obligation_text": "Connector hỗ trợ Lifecycle: Testing"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector hỗ trợ Lifecycle: Testing.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-029",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R054",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-029",
    "source_context_sha256": "381d81c5ec93ae99263a5596851482557a81362364f9a3697b7362de3afe4299",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "3565cb33697eaf7c5e188f363fed41c5418b7ddcbfb6799a496bdf053afe7af1",
    "source_fingerprint_before_c3": "3565cb33697eaf7c5e188f363fed41c5418b7ddcbfb6799a496bdf053afe7af1",
    "source_lines": "L12132-L12226",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R054"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-029"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-029"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R054",
  "title": "Connector hỗ trợ Lifecycle: Testing",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R055 — Connector hỗ trợ Lifecycle: Active

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R055",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "f117d64bdc051db5c70da8bcbfb5c2ebbe1c342f8c8904fe28e715c07221cdfe"
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
        "BRD-WS-15-R055-AC001",
        "BRD-WS-15-R055-AC002",
        "BRD-WS-15-R055-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R055-O001",
      "obligation_text": "Connector hỗ trợ Lifecycle: Active"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector hỗ trợ Lifecycle: Active.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-029",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R055",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-029",
    "source_context_sha256": "381d81c5ec93ae99263a5596851482557a81362364f9a3697b7362de3afe4299",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "f117d64bdc051db5c70da8bcbfb5c2ebbe1c342f8c8904fe28e715c07221cdfe",
    "source_fingerprint_before_c3": "f117d64bdc051db5c70da8bcbfb5c2ebbe1c342f8c8904fe28e715c07221cdfe",
    "source_lines": "L12228-L12322",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R055"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-029"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-029"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R055",
  "title": "Connector hỗ trợ Lifecycle: Active",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R056 — Connector hỗ trợ Lifecycle: Suspended

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R056",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "d9dc2b20a51583ec98dde43fa00603418727564e8d14117997b0d8a977b07cf9"
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
        "BRD-WS-15-R056-AC001",
        "BRD-WS-15-R056-AC002",
        "BRD-WS-15-R056-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R056-O001",
      "obligation_text": "Connector hỗ trợ Lifecycle: Suspended"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector hỗ trợ Lifecycle: Suspended.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-029",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R056",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-029",
    "source_context_sha256": "381d81c5ec93ae99263a5596851482557a81362364f9a3697b7362de3afe4299",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "d9dc2b20a51583ec98dde43fa00603418727564e8d14117997b0d8a977b07cf9",
    "source_fingerprint_before_c3": "d9dc2b20a51583ec98dde43fa00603418727564e8d14117997b0d8a977b07cf9",
    "source_lines": "L12324-L12418",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R056"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-029"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-029"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R056",
  "title": "Connector hỗ trợ Lifecycle: Suspended",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R057 — Connector hỗ trợ Lifecycle: Retired

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-15-R057",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "18b1b119e548bd4deaba2fab14fef7ef9d2284a767557cbc1170da8be72ee11e"
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
        "BRD-WS-15-R057-AC001",
        "BRD-WS-15-R057-AC002",
        "BRD-WS-15-R057-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R057-O001",
      "obligation_text": "Connector hỗ trợ Lifecycle: Retired"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector hỗ trợ Lifecycle: Retired.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-006",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-15-029",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-15-R057",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-029",
    "source_context_sha256": "381d81c5ec93ae99263a5596851482557a81362364f9a3697b7362de3afe4299",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "18b1b119e548bd4deaba2fab14fef7ef9d2284a767557cbc1170da8be72ee11e",
    "source_fingerprint_before_c3": "18b1b119e548bd4deaba2fab14fef7ef9d2284a767557cbc1170da8be72ee11e",
    "source_lines": "L12420-L12514",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-15-R057"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-15-029"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-15-029"
    ]
  },
  "requirement_type": "INTEGRATION_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-15-R057",
  "title": "Connector hỗ trợ Lifecycle: Retired",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-15-001 — Business Domain không được tích hợp trực tiếp với hệ thống bên ngoài

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
      "requirement_id": "EP-15-001",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "2bded670cd65acc24be3a4851b00b543a1a53dd24a20a48ea307bb8662137c50"
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
        "EP-15-001-AC001",
        "EP-15-001-AC002",
        "EP-15-001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-15-001-O001",
      "obligation_text": "Business Domain không được tích hợp trực tiếp với hệ thống bên ngoài"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain không được tích hợp trực tiếp với hệ thống bên ngoài.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-15-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Integration Architecture",
    "source_context_sha256": "fdb6296566620bf2c4f4a6aa0a5c03402b748f113034d6cab693b0002f99a0c6",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "2bded670cd65acc24be3a4851b00b543a1a53dd24a20a48ea307bb8662137c50",
    "source_lines": "L12516-L12591",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-15-001"
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
  "stable_id": "EP-15-001",
  "title": "Business Domain không được tích hợp trực tiếp với hệ thống bên ngoài",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-15-002 — Toàn bộ Integration phải đi qua Gateway, Connector và Adapter

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-15-002",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "20da42f94995fd246d3f848a35713fc4f7ec2fd5744760c4ba86dd44b634dded"
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
        "EP-15-002-AC001",
        "EP-15-002-AC002",
        "EP-15-002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-15-002-O001",
      "obligation_text": "Toàn bộ Integration phải đi qua Gateway, Connector và Adapter"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ Integration phải đi qua Gateway, Connector và Adapter.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-15-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Integration Architecture",
    "source_context_sha256": "fdb6296566620bf2c4f4a6aa0a5c03402b748f113034d6cab693b0002f99a0c6",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "20da42f94995fd246d3f848a35713fc4f7ec2fd5744760c4ba86dd44b634dded",
    "source_lines": "L12593-L12672",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-15-002"
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
  "stable_id": "EP-15-002",
  "title": "Toàn bộ Integration phải đi qua Gateway, Connector và Adapter",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-15-003 — Business Domain chỉ sử dụng Canonical Data Model

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
      "requirement_id": "EP-15-003",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "34da96114030818bf12619d52d0f3af5f43b03b7b321d9f1e5c67a0558144118"
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
        "EP-15-003-AC001",
        "EP-15-003-AC002",
        "EP-15-003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-15-003-O001",
      "obligation_text": "Business Domain chỉ sử dụng Canonical Data Model"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain chỉ sử dụng Canonical Data Model.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-15-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-15-003",
    "source_context_sha256": "c5170bd9b82afbd8abbbcf0abc08d36b0fa464dd4ff327370ea6f1832177fc74",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "34da96114030818bf12619d52d0f3af5f43b03b7b321d9f1e5c67a0558144118",
    "source_lines": "L12674-L12749",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-15-003"
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
  "stable_id": "EP-15-003",
  "title": "Business Domain chỉ sử dụng Canonical Data Model",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-15-004 — Business Domain chỉ sử dụng Canonical Event Model

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
      "requirement_id": "EP-15-004",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "abd7929dc8bf0953d8ed94031d77d441976fc941daa150a87049fbe2c1b61e89"
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
        "EP-15-004-AC001",
        "EP-15-004-AC002",
        "EP-15-004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-15-004-O001",
      "obligation_text": "Business Domain chỉ sử dụng Canonical Event Model"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain chỉ sử dụng Canonical Event Model.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-15-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-15-004",
    "source_context_sha256": "1caee75bc38e5393e9820708a3123493a099ab679bf7020351247e9a60f3370a",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "abd7929dc8bf0953d8ed94031d77d441976fc941daa150a87049fbe2c1b61e89",
    "source_lines": "L12751-L12826",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-15-004"
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
  "stable_id": "EP-15-004",
  "title": "Business Domain chỉ sử dụng Canonical Event Model",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-15-005 — Toàn Platform giao tiếp nội bộ theo Event-Driven Architecture

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
      "requirement_id": "EP-15-005",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "910c3caf9ec61710ae71670577678e974da25efb118dfe8d457b8cf223ef067d"
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
        "EP-15-005-AC001",
        "EP-15-005-AC002",
        "EP-15-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-15-005-O001",
      "obligation_text": "Toàn Platform giao tiếp nội bộ theo Event-Driven Architecture"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn Platform giao tiếp nội bộ theo Event-Driven Architecture.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-15-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-15-005",
    "source_context_sha256": "befef80e9cd805b584f0e5b1b668994511278bf7c8e288fd83f9432bfeb7b076",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "910c3caf9ec61710ae71670577678e974da25efb118dfe8d457b8cf223ef067d",
    "source_lines": "L12828-L12903",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-15-005"
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
  "stable_id": "EP-15-005",
  "title": "Toàn Platform giao tiếp nội bộ theo Event-Driven Architecture",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-15-006 — Mọi Business Domain đều Publish Business Event

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
      "requirement_id": "EP-15-006",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "d36cc7e0cbe3e6db7068517652b6948d53c4275a7a5034d4f3cc18d365c566a2"
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
        "EP-15-006-AC001",
        "EP-15-006-AC002",
        "EP-15-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-15-006-O001",
      "obligation_text": "Mọi Business Domain đều Publish Business Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Business Domain đều Publish Business Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-15-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Business Event",
    "source_context_sha256": "a32cea09e78e1790291b8be66975292424b4ef17c756b233ee9a07277d0ec8bd",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "d36cc7e0cbe3e6db7068517652b6948d53c4275a7a5034d4f3cc18d365c566a2",
    "source_lines": "L12905-L12980",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-15-006"
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
  "stable_id": "EP-15-006",
  "title": "Mọi Business Domain đều Publish Business Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-15-007 — Connector Policy được cấu hình. Không Hard-code

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-15-007",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "16d1d8317d70418554585062a0133c1d551472388658ba95373a7d317b031f8b"
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
        "EP-15-007-AC001",
        "EP-15-007-AC003",
        "EP-15-007-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-15-007-O001",
      "obligation_text": "Connector Policy được cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "EP-15-007-AC002",
        "EP-15-007-AC003",
        "EP-15-007-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-15-007-O002",
      "obligation_text": "Không Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector Policy được cấu hình. Không Hard-code.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-15-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-15-007",
    "source_context_sha256": "5c602b08b8daf12ce9500fd35422f17280dc32cd00d879d73a40daa4e6cb0271",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "16d1d8317d70418554585062a0133c1d551472388658ba95373a7d317b031f8b",
    "source_lines": "L12982-L13071",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-15-007"
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
  "stable_id": "EP-15-007",
  "title": "Connector Policy được cấu hình. Không Hard-code",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-15-008 — Connector được lựa chọn bằng Routing Rule

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-006"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-15-008",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "db64a8fea67d8d5d90c28e68c3a30d7309f01a542e4fc684ed3356097f9cd0a5"
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
        "EP-15-008-AC001",
        "EP-15-008-AC002",
        "EP-15-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-15-008-O001",
      "obligation_text": "Connector được lựa chọn bằng Routing Rule"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector được lựa chọn bằng Routing Rule.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-15-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-15-008",
    "source_context_sha256": "05e4e473f54faa9bdea263e84d64887bac73c8b968a4c5011dea4677bd809197",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "db64a8fea67d8d5d90c28e68c3a30d7309f01a542e4fc684ed3356097f9cd0a5",
    "source_lines": "L13073-L13152",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-15-008"
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
  "stable_id": "EP-15-008",
  "title": "Connector được lựa chọn bằng Routing Rule",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-15-009 — Integration Platform phải hỗ trợ Runtime Profile

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
      "requirement_id": "EP-15-009",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "af651ce4a2287833233ed1b882ecc113f651a7863f032c2e56d24c5bd66f6596"
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
        "EP-15-009-AC001",
        "EP-15-009-AC002",
        "EP-15-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-15-009-O001",
      "obligation_text": "Integration Platform phải hỗ trợ Runtime Profile"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Integration Platform phải hỗ trợ Runtime Profile.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-15-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-15-009",
    "source_context_sha256": "a6e9c48bb6678be16cde76580365a09df641277d859e545e5161b08d80456c95",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "af651ce4a2287833233ed1b882ecc113f651a7863f032c2e56d24c5bd66f6596",
    "source_lines": "L13154-L13229",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-15-009"
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
  "stable_id": "EP-15-009",
  "title": "Integration Platform phải hỗ trợ Runtime Profile",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-15-010 — Integration Platform phải hỗ trợ Monitoring, Health, Retry, DLQ và Observability

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-003"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-15-010",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "source_fingerprint": "b5ccaa645c115f1c0f26659a8b5410325f35f772d48c7f0d065abd1b7c077749"
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
        "EP-15-010-AC001",
        "EP-15-010-AC002",
        "EP-15-010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-15-010-O001",
      "obligation_text": "Integration Platform phải hỗ trợ Monitoring, Health, Retry, DLQ và Observability"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Integration Platform phải hỗ trợ Monitoring, Health, Retry, DLQ và Observability.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-003"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-15-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-15-010",
    "source_context_sha256": "4f52def356b923e638e25b97360ad81fd0aac136e26d6577c8691ea1f99983e0",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "b5ccaa645c115f1c0f26659a8b5410325f35f772d48c7f0d065abd1b7c077749",
    "source_lines": "L13231-L13310",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-15-010"
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
  "stable_id": "EP-15-010",
  "title": "Integration Platform phải hỗ trợ Monitoring, Health, Retry, DLQ và Observability",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
