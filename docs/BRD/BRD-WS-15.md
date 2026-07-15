---
document_code: "BRD-WS-15"
title: "Integration Platform, API Gateway & Event Bus"
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

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-001 — Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Imp…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-001-AC001",
      "given": "a contract interaction at the integration boundary defined by Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Imp…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-001-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-001-AC002",
      "given": "a contract interaction at the integration boundary defined by Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Imp…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-001-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-001-AC003",
      "given": "a contract interaction at the integration boundary defined by Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Imp…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-001-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-001-AC004",
      "given": "a contract interaction at the integration boundary defined by Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Imp…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-001-O004"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-001-AC005",
      "given": "a contract interaction at the integration boundary defined by Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Imp…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-001-O005"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-001-AC006",
      "given": "a contract interaction at the integration boundary defined by Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Imp…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-001-O006"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-001-AC007",
      "given": "an interaction that violates the contract or ownership boundary for Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Imp…",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-001-O001",
        "BD-15-001-O002",
        "BD-15-001-O003",
        "BD-15-001-O004",
        "BD-15-001-O005",
        "BD-15-001-O006"
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
        "BD-15-001-AC001",
        "BD-15-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-001-O001",
      "obligation_text": "Integration Platform hỗ trợ đầy đủ: REST API."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-001-AC002",
        "BD-15-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-001-O002",
      "obligation_text": "Integration Platform hỗ trợ đầy đủ: Webhook."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-001-AC003",
        "BD-15-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-001-O003",
      "obligation_text": "Integration Platform hỗ trợ đầy đủ: Event Bus."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-001-AC004",
        "BD-15-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-001-O004",
      "obligation_text": "Integration Platform hỗ trợ đầy đủ: Message Queue."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-001-AC005",
        "BD-15-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-001-O005",
      "obligation_text": "Integration Platform hỗ trợ đầy đủ: Batch Import."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-001-AC006",
        "BD-15-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-001-O006",
      "obligation_text": "Integration Platform hỗ trợ đầy đủ: Batch Export."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Import - Batch Export",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-001",
    "source_context_sha256": "feba63776c4d2c75ef5f767a8cd3a7f770f7f7c9ab06b1d3a120720328d27d40",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "159d1351d50b80b6415544da4fefbb68dc6ff9ab094166a174a001e6739e7d88",
    "source_lines": "L873-L883",
    "source_section": "35. Business Decisions (Locked) > BD-15-001"
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
  "stable_id": "BD-15-001",
  "title": "Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Imp…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-002 — API Gateway là thành phần bắt buộc. Business Domain không được tích hợp trực tiếp với hệ thống b…

```json
{
  "acceptance_contract": [],
  "acceptance_rationale": "Composite parent coverage is satisfied only through ALL_CHILDREN; the parent is not an acceptance unit.",
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
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
    "source_fingerprint": "f031b70591de7d42955b3c9e9fcc42c2078b36efc1f5041d83f087cf0d5688ae",
    "source_lines": "L886-L891",
    "source_section": "35. Business Decisions (Locked) > BD-15-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-003-AC001",
      "given": "a contract interaction at the integration boundary defined by Connector là Business Object. Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài. Bus…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-003-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-003-AC002",
      "given": "a contract interaction at the integration boundary defined by Connector là Business Object. Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài. Bus…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-003-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-003-AC003",
      "given": "a contract interaction at the integration boundary defined by Connector là Business Object. Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài. Bus…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-003-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-003-AC004",
      "given": "an interaction that violates the contract or ownership boundary for Connector là Business Object. Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài. Bus…",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-003-O001",
        "BD-15-003-O002",
        "BD-15-003-O003"
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
        "BD-15-003-AC001",
        "BD-15-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-003-O001",
      "obligation_text": "Connector là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-003-AC002",
        "BD-15-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-003-O002",
      "obligation_text": "Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-003-AC003",
        "BD-15-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-003-O003",
      "obligation_text": "Business Logic không được đặt trong Connector"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector là Business Object. Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài. Business Logic không được đặt trong Connector.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Connector",
    "source_context_sha256": "b4b269d9d838a068eef5bcaa82adf0a7ae24e95067a42c36d88725768e0eafbe",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "23440f1d8c43318f34bfb666ffe29db0b564f8cb9e3a51d83536aebc7355f5dd",
    "source_lines": "L894-L901",
    "source_section": "35. Business Decisions (Locked) > BD-15-003"
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
  "stable_id": "BD-15-003",
  "title": "Connector là Business Object. Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài. Bus…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-004 — Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-15-004-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-15-004-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-15-004-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-15-004-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-15-004-AC003",
      "given": "an identified principal, applicable assurance context, and policy inputs for Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-15-004-O003"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-15-004-AC004",
      "given": "an identified principal, applicable assurance context, and policy inputs for Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-15-004-O004"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-15-004-AC005",
      "given": "an identified principal, applicable assurance context, and policy inputs for Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-15-004-O005"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-15-004-AC006",
      "given": "an identified principal, applicable assurance context, and policy inputs for Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-15-004-O006"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-15-004-AC007",
      "given": "an identified principal, applicable assurance context, and policy inputs for Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-15-004-O007"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-15-004-AC008",
      "given": "an identified principal, applicable assurance context, and policy inputs for Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-15-004-O008"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-15-004-AC009",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-15-004-O001",
        "BD-15-004-O002",
        "BD-15-004-O003",
        "BD-15-004-O004",
        "BD-15-004-O005",
        "BD-15-004-O006",
        "BD-15-004-O007",
        "BD-15-004-O008"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-15-004-AC010",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-15-004-O001",
        "BD-15-004-O002",
        "BD-15-004-O003",
        "BD-15-004-O004",
        "BD-15-004-O005",
        "BD-15-004-O006",
        "BD-15-004-O007",
        "BD-15-004-O008"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "IDEMPOTENCY",
      "controlled_contract": "EXPLICIT_IDEMPOTENCY_CONTRACT_V1",
      "criterion_id": "BD-15-004-AC011",
      "given": "a repeated request, retry, replay, or duplicate explicitly governed by Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication…",
      "observable_evidence": "original and repeated action identities, both outcomes, side-effect count, and resulting business state",
      "then": "the repeated action produces the requirement-specific stable result without an additional prohibited side effect",
      "verifies": [
        "BD-15-004-O001",
        "BD-15-004-O002",
        "BD-15-004-O003",
        "BD-15-004-O004",
        "BD-15-004-O005",
        "BD-15-004-O006",
        "BD-15-004-O007",
        "BD-15-004-O008"
      ],
      "when": "the same governed action is presented again under the declared identity or deduplication boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC001",
        "BD-15-004-AC009",
        "BD-15-004-AC010",
        "BD-15-004-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O001",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Connection."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC002",
        "BD-15-004-AC009",
        "BD-15-004-AC010",
        "BD-15-004-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O002",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Authentication."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC003",
        "BD-15-004-AC009",
        "BD-15-004-AC010",
        "BD-15-004-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O003",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Session."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC004",
        "BD-15-004-AC009",
        "BD-15-004-AC010",
        "BD-15-004-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O004",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Retry."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC005",
        "BD-15-004-AC009",
        "BD-15-004-AC010",
        "BD-15-004-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O005",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Health Adapter quản lý."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC006",
        "BD-15-004-AC009",
        "BD-15-004-AC010",
        "BD-15-004-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O006",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Mapping."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC007",
        "BD-15-004-AC009",
        "BD-15-004-AC010",
        "BD-15-004-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O007",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Transformation."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-004-AC008",
        "BD-15-004-AC009",
        "BD-15-004-AC010",
        "BD-15-004-AC011"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-004-O008",
      "obligation_text": "Connector và Adapter là hai thành phần độc lập. Connector quản lý: Canonical Conversion."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-15-004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-15-004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [
        "BD-15-004-AC011"
      ],
      "status": "APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-15-004-AC010"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-15-004-AC001",
        "BD-15-004-AC002",
        "BD-15-004-AC003",
        "BD-15-004-AC004",
        "BD-15-004-AC005",
        "BD-15-004-AC006",
        "BD-15-004-AC007",
        "BD-15-004-AC008"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-15-004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "959e4183a9384bed5328e05d0dfcd4ddedfb85b2acadc042a26c457b6fbbba96",
    "source_lines": "L904-L921",
    "source_section": "35. Business Decisions (Locked) > BD-15-004"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-005-AC001",
      "given": "a contract interaction at the integration boundary defined by Integration Platform được chia thành các Gateway độc lập: - API Gateway - Supplier Gateway - Pay…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "each boundary object keeps a distinct identity, owner, reference, and lifecycle; changing one does not implicitly mutate the other",
      "verifies": [
        "BD-15-005-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-005-AC002",
      "given": "a contract interaction at the integration boundary defined by Integration Platform được chia thành các Gateway độc lập: - API Gateway - Supplier Gateway - Pay…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "each boundary object keeps a distinct identity, owner, reference, and lifecycle; changing one does not implicitly mutate the other",
      "verifies": [
        "BD-15-005-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-005-AC003",
      "given": "a contract interaction at the integration boundary defined by Integration Platform được chia thành các Gateway độc lập: - API Gateway - Supplier Gateway - Pay…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "each boundary object keeps a distinct identity, owner, reference, and lifecycle; changing one does not implicitly mutate the other",
      "verifies": [
        "BD-15-005-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-005-AC004",
      "given": "a contract interaction at the integration boundary defined by Integration Platform được chia thành các Gateway độc lập: - API Gateway - Supplier Gateway - Pay…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "each boundary object keeps a distinct identity, owner, reference, and lifecycle; changing one does not implicitly mutate the other",
      "verifies": [
        "BD-15-005-O004"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-005-AC005",
      "given": "a contract interaction at the integration boundary defined by Integration Platform được chia thành các Gateway độc lập: - API Gateway - Supplier Gateway - Pay…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "each boundary object keeps a distinct identity, owner, reference, and lifecycle; changing one does not implicitly mutate the other",
      "verifies": [
        "BD-15-005-O005"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-005-AC006",
      "given": "an interaction that violates the contract or ownership boundary for Integration Platform được chia thành các Gateway độc lập: - API Gateway - Supplier Gateway - Pay…",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-005-O001",
        "BD-15-005-O002",
        "BD-15-005-O003",
        "BD-15-005-O004",
        "BD-15-005-O005"
      ],
      "when": "the interaction reaches the integration boundary"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-15-005-AC007",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Integration Platform được chia thành các Gateway độc lập: - API Gateway - Supplier Gateway - Pay…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-15-005-O001",
        "BD-15-005-O002",
        "BD-15-005-O003",
        "BD-15-005-O004",
        "BD-15-005-O005"
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
        "BD-15-005-AC001",
        "BD-15-005-AC006",
        "BD-15-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-005-O001",
      "obligation_text": "Integration Platform được chia thành các Gateway độc lập: API Gateway."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-005-AC002",
        "BD-15-005-AC006",
        "BD-15-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-005-O002",
      "obligation_text": "Integration Platform được chia thành các Gateway độc lập: Supplier Gateway."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-005-AC003",
        "BD-15-005-AC006",
        "BD-15-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-005-O003",
      "obligation_text": "Integration Platform được chia thành các Gateway độc lập: Payment Gateway."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-005-AC004",
        "BD-15-005-AC006",
        "BD-15-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-005-O004",
      "obligation_text": "Integration Platform được chia thành các Gateway độc lập: Partner Gateway."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-005-AC005",
        "BD-15-005-AC006",
        "BD-15-005-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-005-O005",
      "obligation_text": "Integration Platform được chia thành các Gateway độc lập: Notification Gateway Gateway có thể mở rộng trong tương lai."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-15-005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-15-005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-15-005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-15-005-AC007"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-15-005-AC001",
        "BD-15-005-AC002",
        "BD-15-005-AC003",
        "BD-15-005-AC004",
        "BD-15-005-AC005"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-15-005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "751e62c9e50b1b344603c7df2c224025db4a9cb0512d28138079f4c35269f83d",
    "source_lines": "L924-L935",
    "source_section": "35. Business Decisions (Locked) > BD-15-005"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-15-006-AC001",
      "given": "a candidate Business Event là Business Object. Mọi Business Domain đều Publish Business Event record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-15-006-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-15-006-AC002",
      "given": "a candidate Business Event là Business Object. Mọi Business Domain đều Publish Business Event record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-15-006-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-006-AC003",
      "given": "a Business Event là Business Object. Mọi Business Domain đều Publish Business Event candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-15-006-O001",
        "BD-15-006-O002"
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
        "BD-15-006-AC001",
        "BD-15-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-006-O001",
      "obligation_text": "Business Event là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-006-AC002",
        "BD-15-006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-006-O002",
      "obligation_text": "Mọi Business Domain đều Publish Business Event"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Event là Business Object. Mọi Business Domain đều Publish Business Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Business Event",
    "source_context_sha256": "a32cea09e78e1790291b8be66975292424b4ef17c756b233ee9a07277d0ec8bd",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "1ed7f0b9ad996ac715ff98804d18c420b07dbaf8b9d004cd1f9fa5cf92e5aa2b",
    "source_lines": "L938-L943",
    "source_section": "35. Business Decisions (Locked) > BD-15-006"
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
  "stable_id": "BD-15-006",
  "title": "Business Event là Business Object. Mọi Business Domain đều Publish Business Event",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-007 — Business Domain đăng ký Subscribe Business Event. Publisher không biết Subscriber. Event Bus chị…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-007-AC001",
      "given": "the applicable business context, actor, and input for Business Domain đăng ký Subscribe Business Event. Publisher không biết Subscriber. Event Bus chị…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-007-AC002",
      "given": "the applicable business context, actor, and input for Business Domain đăng ký Subscribe Business Event. Publisher không biết Subscriber. Event Bus chị…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-007-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-007-AC003",
      "given": "the applicable business context, actor, and input for Business Domain đăng ký Subscribe Business Event. Publisher không biết Subscriber. Event Bus chị…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-007-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-15-007-AC004",
      "given": "an unsupported or invalid business input at the boundary governed by Business Domain đăng ký Subscribe Business Event. Publisher không biết Subscriber. Event Bus chị…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-15-007-O001",
        "BD-15-007-O002",
        "BD-15-007-O003"
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
        "BD-15-007-AC001",
        "BD-15-007-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-007-O001",
      "obligation_text": "Business Domain đăng ký Subscribe Business Event"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-007-AC002",
        "BD-15-007-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-007-O002",
      "obligation_text": "Publisher không biết Subscriber"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-007-AC003",
        "BD-15-007-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-007-O003",
      "obligation_text": "Event Bus chịu trách nhiệm Routing và Delivery"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Domain đăng ký Subscribe Business Event. Publisher không biết Subscriber. Event Bus chịu trách nhiệm Routing và Delivery.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Event Subscription",
    "source_context_sha256": "bac815a32b1342602e87b110b410c7d7123f30ef7b6dab5e98047a157c9fc326",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "b5a096abadb58deedafb42f0047d2a296c7e3297ab576dd372877861df75008f",
    "source_lines": "L946-L953",
    "source_section": "35. Business Decisions (Locked) > BD-15-007"
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
  "stable_id": "BD-15-007",
  "title": "Business Domain đăng ký Subscribe Business Event. Publisher không biết Subscriber. Event Bus chị…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-008 — Business Event hỗ trợ Version. Backward Compatibility phải được đảm bảo

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-008-AC001",
      "given": "the applicable business context, actor, and input for Business Event hỗ trợ Version. Backward Compatibility phải được đảm bảo",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-008-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-008-AC002",
      "given": "the applicable business context, actor, and input for Business Event hỗ trợ Version. Backward Compatibility phải được đảm bảo",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-008-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-15-008-AC003",
      "given": "an unsupported or invalid business input at the boundary governed by Business Event hỗ trợ Version. Backward Compatibility phải được đảm bảo",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-15-008-O001",
        "BD-15-008-O002"
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
        "BD-15-008-AC001",
        "BD-15-008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-008-O001",
      "obligation_text": "Business Event hỗ trợ Version"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-008-AC002",
        "BD-15-008-AC003"
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
    "source_fingerprint": "154f859e041acfaf3be78c4a1169ec0a62ca7703878b4a42269755477184ee5e",
    "source_lines": "L956-L961",
    "source_section": "35. Business Decisions (Locked) > BD-15-008"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-009-AC001",
      "given": "the applicable business context, actor, and input for Event Delivery hỗ trợ: - At Most Once - At Least Once - Exactly Once Mặc định sử dụng: **At Leas…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-009-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-009-AC002",
      "given": "the applicable business context, actor, and input for Event Delivery hỗ trợ: - At Most Once - At Least Once - Exactly Once Mặc định sử dụng: **At Leas…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-009-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-009-AC003",
      "given": "the applicable business context, actor, and input for Event Delivery hỗ trợ: - At Most Once - At Least Once - Exactly Once Mặc định sử dụng: **At Leas…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-009-O003"
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
        "BD-15-009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-009-O001",
      "obligation_text": "Event Delivery hỗ trợ: At Most Once."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-009-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-009-O002",
      "obligation_text": "Event Delivery hỗ trợ: At Least Once."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-009-O003",
      "obligation_text": "Event Delivery hỗ trợ: Exactly Once Mặc định sử dụng: **At Least Once**."
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
    "source_fingerprint": "11858e1ad3dfa75e93016916a5fa32948389a2c3d8845883dbf6cc22af5cde90",
    "source_lines": "L964-L975",
    "source_section": "35. Business Decisions (Locked) > BD-15-009"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-010-AC001",
      "given": "a contract interaction at the integration boundary defined by API và Business Event đều hỗ trợ Idempotency",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-010-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-010-AC002",
      "given": "an interaction that violates the contract or ownership boundary for API và Business Event đều hỗ trợ Idempotency",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-010-O001"
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
        "BD-15-010-AC001",
        "BD-15-010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-010-O001",
      "obligation_text": "API và Business Event đều hỗ trợ Idempotency"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-15-010 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-15-010 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-15-010 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-15-010 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-15-010-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-15-010 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "09c1db6df30bf9c2aaaef50d4f222d34b97cb4fa24d4d26c127a73eb2224ad30",
    "source_lines": "L978-L981",
    "source_section": "35. Business Decisions (Locked) > BD-15-010"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-011-AC001",
      "given": "the applicable business context, actor, and input for Retry Policy được cấu hình. Bao gồm: - Retry Count - Retry Interval - Retry Strategy - Exponenti…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-15-011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-011-AC002",
      "given": "the applicable business context, actor, and input for Retry Policy được cấu hình. Bao gồm: - Retry Count - Retry Interval - Retry Strategy - Exponenti…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-15-011-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-011-AC003",
      "given": "the applicable business context, actor, and input for Retry Policy được cấu hình. Bao gồm: - Retry Count - Retry Interval - Retry Strategy - Exponenti…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-15-011-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-011-AC004",
      "given": "the applicable business context, actor, and input for Retry Policy được cấu hình. Bao gồm: - Retry Count - Retry Interval - Retry Strategy - Exponenti…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BD-15-011-O004"
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
        "BD-15-011-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-011-O001",
      "obligation_text": "Retry Policy được cấu hình. Bao gồm: Retry Count."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-011-O002",
      "obligation_text": "Retry Policy được cấu hình. Bao gồm: Retry Interval."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-011-O003",
      "obligation_text": "Retry Policy được cấu hình. Bao gồm: Retry Strategy."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-011-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-011-O004",
      "obligation_text": "Retry Policy được cấu hình. Bao gồm: Exponential Backoff."
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
    "source_fingerprint": "822503078fd7326b95c3290531baac77924f7f2217c990579845232c60e6b182",
    "source_lines": "L984-L994",
    "source_section": "35. Business Decisions (Locked) > BD-15-011"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-15-012-AC001",
      "given": "a candidate Dead Letter Queue là Business Object. Message Retry thất bại sẽ được chuyển vào DLQ record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-15-012-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-15-012-AC002",
      "given": "a candidate Dead Letter Queue là Business Object. Message Retry thất bại sẽ được chuyển vào DLQ record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-15-012-O002"
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
        "BD-15-012-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-012-O001",
      "obligation_text": "Dead Letter Queue là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-012-AC002"
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
    "source_fingerprint": "f64773b076cfda639e1c202c15563ecaed4fb574fb0b8c26b6370b59d76f1c97",
    "source_lines": "L997-L1002",
    "source_section": "35. Business Decisions (Locked) > BD-15-012"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-15-013-AC001",
      "given": "a candidate Callback là Business Object. Bao gồm: - Payment Callback - Supplier Callback - Notification Call… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-15-013-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-15-013-AC002",
      "given": "a candidate Callback là Business Object. Bao gồm: - Payment Callback - Supplier Callback - Notification Call… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-15-013-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-15-013-AC003",
      "given": "a candidate Callback là Business Object. Bao gồm: - Payment Callback - Supplier Callback - Notification Call… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-15-013-O003"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-15-013-AC004",
      "given": "a candidate Callback là Business Object. Bao gồm: - Payment Callback - Supplier Callback - Notification Call… record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-15-013-O004"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DATA_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-013-AC005",
      "given": "a Callback là Business Object. Bao gồm: - Payment Callback - Supplier Callback - Notification Call… candidate containing an unsupported value, inconsistent relationship, or unresolved reference",
      "observable_evidence": "rejection result, field or relationship reason, unresolved reference, and unchanged persisted state",
      "then": "the candidate is rejected without persisting the invalid state, and each invalid field or relationship has a deterministic reason",
      "verifies": [
        "BD-15-013-O001",
        "BD-15-013-O002",
        "BD-15-013-O003",
        "BD-15-013-O004"
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
        "BD-15-013-AC001",
        "BD-15-013-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-013-O001",
      "obligation_text": "Callback là Business Object. Bao gồm: Payment Callback."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-013-AC002",
        "BD-15-013-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-013-O002",
      "obligation_text": "Callback là Business Object. Bao gồm: Supplier Callback."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-013-AC003",
        "BD-15-013-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-013-O003",
      "obligation_text": "Callback là Business Object. Bao gồm: Notification Callback."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-013-AC004",
        "BD-15-013-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-013-O004",
      "obligation_text": "Callback là Business Object. Bao gồm: Partner Callback."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-15-013 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-15-013 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-15-013 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-15-013 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-15-013-AC001",
        "BD-15-013-AC002",
        "BD-15-013-AC003",
        "BD-15-013-AC004"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-15-013 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "0c1011e792c6a68f12bc7ee8f4b54601b5c55ab7ea510d7e24779268157c3e43",
    "source_lines": "L1005-L1015",
    "source_section": "35. Business Decisions (Locked) > BD-15-013"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-014-AC001",
      "given": "a contract interaction at the integration boundary defined by Webhook hỗ trợ: - Internal - Organization - External Partner",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-014-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-014-AC002",
      "given": "a contract interaction at the integration boundary defined by Webhook hỗ trợ: - Internal - Organization - External Partner",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-014-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-014-AC003",
      "given": "a contract interaction at the integration boundary defined by Webhook hỗ trợ: - Internal - Organization - External Partner",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-014-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-014-AC004",
      "given": "an interaction that violates the contract or ownership boundary for Webhook hỗ trợ: - Internal - Organization - External Partner",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-014-O001",
        "BD-15-014-O002",
        "BD-15-014-O003"
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
        "BD-15-014-AC001",
        "BD-15-014-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-014-O001",
      "obligation_text": "Webhook hỗ trợ: Internal."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-014-AC002",
        "BD-15-014-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-014-O002",
      "obligation_text": "Webhook hỗ trợ: Organization."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-014-AC003",
        "BD-15-014-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-014-O003",
      "obligation_text": "Webhook hỗ trợ: External Partner."
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
    "source_fingerprint": "a98ec11d5cb4c5b2bd008dd96727b0dfde9fc88c5ce76aaa79f0e8679452320e",
    "source_lines": "L1018-L1025",
    "source_section": "35. Business Decisions (Locked) > BD-15-014"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-015-AC001",
      "given": "a contract interaction at the integration boundary defined by API hỗ trợ Version. API Version được quản lý độc lập",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-015-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-015-AC002",
      "given": "a contract interaction at the integration boundary defined by API hỗ trợ Version. API Version được quản lý độc lập",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "each boundary object keeps a distinct identity, owner, reference, and lifecycle; changing one does not implicitly mutate the other",
      "verifies": [
        "BD-15-015-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-015-AC003",
      "given": "an interaction that violates the contract or ownership boundary for API hỗ trợ Version. API Version được quản lý độc lập",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-015-O001",
        "BD-15-015-O002"
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
        "BD-15-015-AC001",
        "BD-15-015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-015-O001",
      "obligation_text": "API hỗ trợ Version"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-015-AC002",
        "BD-15-015-AC003"
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
    "source_fingerprint": "06900b113b3dc83482390b9212fe1522cafb32ef0fd2d6203943b58d03d2fa35",
    "source_lines": "L1028-L1033",
    "source_section": "35. Business Decisions (Locked) > BD-15-015"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-016-AC001",
      "given": "a contract interaction at the integration boundary defined by Connector hỗ trợ nhiều Runtime Profile: - Mock - Sandbox - UAT - Production",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-016-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-016-AC002",
      "given": "a contract interaction at the integration boundary defined by Connector hỗ trợ nhiều Runtime Profile: - Mock - Sandbox - UAT - Production",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-016-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-016-AC003",
      "given": "a contract interaction at the integration boundary defined by Connector hỗ trợ nhiều Runtime Profile: - Mock - Sandbox - UAT - Production",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-016-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-016-AC004",
      "given": "a contract interaction at the integration boundary defined by Connector hỗ trợ nhiều Runtime Profile: - Mock - Sandbox - UAT - Production",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-016-O004"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-016-AC005",
      "given": "an interaction that violates the contract or ownership boundary for Connector hỗ trợ nhiều Runtime Profile: - Mock - Sandbox - UAT - Production",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-016-O001",
        "BD-15-016-O002",
        "BD-15-016-O003",
        "BD-15-016-O004"
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
        "BD-15-016-AC001",
        "BD-15-016-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-016-O001",
      "obligation_text": "Connector hỗ trợ nhiều Runtime Profile: Mock."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-016-AC002",
        "BD-15-016-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-016-O002",
      "obligation_text": "Connector hỗ trợ nhiều Runtime Profile: Sandbox."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-016-AC003",
        "BD-15-016-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-016-O003",
      "obligation_text": "Connector hỗ trợ nhiều Runtime Profile: UAT."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-016-AC004",
        "BD-15-016-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-016-O004",
      "obligation_text": "Connector hỗ trợ nhiều Runtime Profile: Production."
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
    "source_fingerprint": "0cbd0d423f8f59ac84188a964a816060903265c335f6d99db553637e48a4c5ad",
    "source_lines": "L1036-L1044",
    "source_section": "35. Business Decisions (Locked) > BD-15-016"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-15-017-AC001",
      "given": "a candidate Message Queue là Business Object. Queue được tách theo từng nghiệp vụ record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-15-017-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-15-017-AC002",
      "given": "a candidate Message Queue là Business Object. Queue được tách theo từng nghiệp vụ record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-15-017-O002"
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
        "BD-15-017-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-017-O001",
      "obligation_text": "Message Queue là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-017-AC002"
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
    "source_fingerprint": "b4c44b27572b89cc3bc1622f784c39315fa9c6ec0216be365dcdd23ed51ddb62",
    "source_lines": "L1047-L1052",
    "source_section": "35. Business Decisions (Locked) > BD-15-017"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-018-AC001",
      "given": "the applicable business context, actor, and input for Queue hỗ trợ: - FIFO - Priority - Partition Queue liên quan Payment, Procurement và Fulfillment …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-018-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-018-AC002",
      "given": "the applicable business context, actor, and input for Queue hỗ trợ: - FIFO - Priority - Partition Queue liên quan Payment, Procurement và Fulfillment …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-018-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-018-AC003",
      "given": "the applicable business context, actor, and input for Queue hỗ trợ: - FIFO - Priority - Partition Queue liên quan Payment, Procurement và Fulfillment …",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-018-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-15-018-AC004",
      "given": "an unsupported or invalid business input at the boundary governed by Queue hỗ trợ: - FIFO - Priority - Partition Queue liên quan Payment, Procurement và Fulfillment …",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-15-018-O001",
        "BD-15-018-O002",
        "BD-15-018-O003"
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
        "BD-15-018-AC001",
        "BD-15-018-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-018-O001",
      "obligation_text": "Queue hỗ trợ: FIFO."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-018-AC002",
        "BD-15-018-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-018-O002",
      "obligation_text": "Queue hỗ trợ: Priority."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-018-AC003",
        "BD-15-018-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-018-O003",
      "obligation_text": "Queue hỗ trợ: Partition Queue liên quan Payment, Procurement và Fulfillment có độ ưu tiên cao hơn."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-15-018 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-15-018 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-15-018 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-15-018 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-15-018-AC001",
        "BD-15-018-AC002",
        "BD-15-018-AC003"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-15-018 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "7c597cd851e35b22caab060836bb9ada7723f1a772d92d1eb5a5a15e8f624662",
    "source_lines": "L1055-L1064",
    "source_section": "35. Business Decisions (Locked) > BD-15-018"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-019-AC001",
      "given": "an operational task within the scope of Integration Platform hỗ trợ: - Monitoring - Health Check - Retry - DLQ - Queue Monitoring",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-15-019-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-019-AC002",
      "given": "an operational task within the scope of Integration Platform hỗ trợ: - Monitoring - Health Check - Retry - DLQ - Queue Monitoring",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-15-019-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-019-AC003",
      "given": "an operational task within the scope of Integration Platform hỗ trợ: - Monitoring - Health Check - Retry - DLQ - Queue Monitoring",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-15-019-O003"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-019-AC004",
      "given": "an operational task within the scope of Integration Platform hỗ trợ: - Monitoring - Health Check - Retry - DLQ - Queue Monitoring",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-15-019-O004"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-019-AC005",
      "given": "an operational task within the scope of Integration Platform hỗ trợ: - Monitoring - Health Check - Retry - DLQ - Queue Monitoring",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-15-019-O005"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-15-019-AC006",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Integration Platform hỗ trợ: - Monitoring - Health Check - Retry - DLQ - Queue Monitoring",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-15-019-O001",
        "BD-15-019-O002",
        "BD-15-019-O003",
        "BD-15-019-O004",
        "BD-15-019-O005"
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
        "BD-15-019-AC001",
        "BD-15-019-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-019-O001",
      "obligation_text": "Integration Platform hỗ trợ: Monitoring."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-019-AC002",
        "BD-15-019-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-019-O002",
      "obligation_text": "Integration Platform hỗ trợ: Health Check."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-019-AC003",
        "BD-15-019-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-019-O003",
      "obligation_text": "Integration Platform hỗ trợ: Retry."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-019-AC004",
        "BD-15-019-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-019-O004",
      "obligation_text": "Integration Platform hỗ trợ: DLQ."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-019-AC005",
        "BD-15-019-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-019-O005",
      "obligation_text": "Integration Platform hỗ trợ: Queue Monitoring."
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
    "source_fingerprint": "311fd6457592bcced97cb5a5972d8f68324edfbf85f77031022165bba8572f4a",
    "source_lines": "L1067-L1076",
    "source_section": "35. Business Decisions (Locked) > BD-15-019"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-020-AC001",
      "given": "a contract interaction at the integration boundary defined by API Gateway hỗ trợ: - Rate Limiting - Burst - Quota",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-020-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-020-AC002",
      "given": "a contract interaction at the integration boundary defined by API Gateway hỗ trợ: - Rate Limiting - Burst - Quota",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-020-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-020-AC003",
      "given": "a contract interaction at the integration boundary defined by API Gateway hỗ trợ: - Rate Limiting - Burst - Quota",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-020-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-020-AC004",
      "given": "an interaction that violates the contract or ownership boundary for API Gateway hỗ trợ: - Rate Limiting - Burst - Quota",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-020-O001",
        "BD-15-020-O002",
        "BD-15-020-O003"
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
        "BD-15-020-AC001",
        "BD-15-020-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-020-O001",
      "obligation_text": "API Gateway hỗ trợ: Rate Limiting."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-020-AC002",
        "BD-15-020-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-020-O002",
      "obligation_text": "API Gateway hỗ trợ: Burst."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-020-AC003",
        "BD-15-020-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-020-O003",
      "obligation_text": "API Gateway hỗ trợ: Quota."
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
    "source_fingerprint": "3ec2c70df0c46977335d186b5c0d3c3fc416c521dd4719cf9ee886ce6143544a",
    "source_lines": "L1079-L1086",
    "source_section": "35. Business Decisions (Locked) > BD-15-020"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-021-AC001",
      "given": "a contract interaction at the integration boundary defined by Connector hỗ trợ Circuit Breaker",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-021-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-021-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Connector hỗ trợ Circuit Breaker",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-021-O001"
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
        "BD-15-021-AC001",
        "BD-15-021-AC002"
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
    "source_fingerprint": "0760f03d1b41e768a211f0c3acac39c029f53f748c693dab669282ed04a5472e",
    "source_lines": "L1089-L1092",
    "source_section": "35. Business Decisions (Locked) > BD-15-021"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-022-AC001",
      "given": "the applicable business context, actor, and input for Scheduler có thể Publish Business Event",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-022-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-15-022-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Scheduler có thể Publish Business Event",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-15-022-O001"
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
        "BD-15-022-AC001",
        "BD-15-022-AC002"
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
    "source_fingerprint": "e0b0970b86eee3d7081d70052cd70bb73c51488159d3c7e06a125c78c74dded7",
    "source_lines": "L1095-L1098",
    "source_section": "35. Business Decisions (Locked) > BD-15-022"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-023-AC001",
      "given": "a contract interaction at the integration boundary defined by Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Even…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-023-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-023-AC002",
      "given": "a contract interaction at the integration boundary defined by Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Even…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-023-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-023-AC003",
      "given": "a contract interaction at the integration boundary defined by Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Even…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-023-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-023-AC004",
      "given": "a contract interaction at the integration boundary defined by Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Even…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-023-O004"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-023-AC005",
      "given": "a contract interaction at the integration boundary defined by Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Even…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-023-O005"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-023-AC006",
      "given": "a contract interaction at the integration boundary defined by Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Even…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-023-O006"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-023-AC007",
      "given": "a contract interaction at the integration boundary defined by Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Even…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-023-O007"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-023-AC008",
      "given": "an interaction that violates the contract or ownership boundary for Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Even…",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-023-O001",
        "BD-15-023-O002",
        "BD-15-023-O003",
        "BD-15-023-O004",
        "BD-15-023-O005",
        "BD-15-023-O006",
        "BD-15-023-O007"
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
        "BD-15-023-AC001",
        "BD-15-023-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-023-O001",
      "obligation_text": "Business Service Registry là Business Object. Registry quản lý: Service."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-023-AC002",
        "BD-15-023-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-023-O002",
      "obligation_text": "Business Service Registry là Business Object. Registry quản lý: API."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-023-AC003",
        "BD-15-023-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-023-O003",
      "obligation_text": "Business Service Registry là Business Object. Registry quản lý: Published Event."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-023-AC004",
        "BD-15-023-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-023-O004",
      "obligation_text": "Business Service Registry là Business Object. Registry quản lý: Consumed Event."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-023-AC005",
        "BD-15-023-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-023-O005",
      "obligation_text": "Business Service Registry là Business Object. Registry quản lý: Dependency."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-023-AC006",
        "BD-15-023-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-023-O006",
      "obligation_text": "Business Service Registry là Business Object. Registry quản lý: Owner."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-023-AC007",
        "BD-15-023-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-023-O007",
      "obligation_text": "Business Service Registry là Business Object. Registry quản lý: Version."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Event - Consumed Event - Dependency - Owner - Version",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-023",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Business Service Registry",
    "source_context_sha256": "cffc01224270ac2af85b76b8866141a249b861e7834694115b140112ebcc8665",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "618dbae2e3ffc8e1c6b22d358371d29dc468cfe481201d7fdd4e3503b2a10f89",
    "source_lines": "L1101-L1114",
    "source_section": "35. Business Decisions (Locked) > BD-15-023"
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
  "stable_id": "BD-15-023",
  "title": "Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Even…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-024 — Business Domain chỉ làm việc với Canonical Data Model

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-15-024-AC001",
      "given": "a candidate Business Domain chỉ làm việc với Canonical Data Model record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-15-024-O001"
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
        "BD-15-024-AC001"
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
    "source_fingerprint": "159f74aa37de54a9b3465f045e96d44ba8246329657eb06d05f6f02df7abf606",
    "source_lines": "L1117-L1120",
    "source_section": "35. Business Decisions (Locked) > BD-15-024"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-15-025-AC001",
      "given": "the applicable business context, actor, and input for Business Domain chỉ xử lý Canonical Event Model",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-15-025-O001"
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
        "BD-15-025-AC001"
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
    "source_fingerprint": "f2a9cb5a8a058b996c0c460221cc82b93916b29b00f8063984e1e410b8e164c1",
    "source_lines": "L1123-L1126",
    "source_section": "35. Business Decisions (Locked) > BD-15-025"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-026-AC001",
      "given": "a contract interaction at the integration boundary defined by Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Break…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-026-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-026-AC002",
      "given": "a contract interaction at the integration boundary defined by Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Break…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-026-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-026-AC003",
      "given": "a contract interaction at the integration boundary defined by Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Break…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-026-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-026-AC004",
      "given": "a contract interaction at the integration boundary defined by Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Break…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-026-O004"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-026-AC005",
      "given": "a contract interaction at the integration boundary defined by Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Break…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-026-O005"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-026-AC006",
      "given": "a contract interaction at the integration boundary defined by Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Break…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-026-O006"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-026-AC007",
      "given": "a contract interaction at the integration boundary defined by Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Break…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-026-O007"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-026-AC008",
      "given": "an interaction that violates the contract or ownership boundary for Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Break…",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-026-O001",
        "BD-15-026-O002",
        "BD-15-026-O003",
        "BD-15-026-O004",
        "BD-15-026-O005",
        "BD-15-026-O006",
        "BD-15-026-O007"
      ],
      "when": "the interaction reaches the integration boundary"
    },
    {
      "case": "CONCURRENCY",
      "controlled_contract": "EXPLICIT_CONCURRENCY_CONTRACT_V1",
      "criterion_id": "BD-15-026-AC009",
      "given": "two or more concurrent actions covered by an explicit concurrency boundary in Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Break…",
      "observable_evidence": "concurrent inputs, individual outcomes, final state, and invariant comparison",
      "then": "the resulting decisions and state preserve the concurrency invariant stated by the referenced obligation",
      "verifies": [
        "BD-15-026-O001",
        "BD-15-026-O002",
        "BD-15-026-O003",
        "BD-15-026-O004",
        "BD-15-026-O005",
        "BD-15-026-O006",
        "BD-15-026-O007"
      ],
      "when": "the actions contend for the same governed business state"
    },
    {
      "case": "IDEMPOTENCY",
      "controlled_contract": "EXPLICIT_IDEMPOTENCY_CONTRACT_V1",
      "criterion_id": "BD-15-026-AC010",
      "given": "a repeated request, retry, replay, or duplicate explicitly governed by Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Break…",
      "observable_evidence": "original and repeated action identities, both outcomes, side-effect count, and resulting business state",
      "then": "the repeated action produces the requirement-specific stable result without an additional prohibited side effect",
      "verifies": [
        "BD-15-026-O001",
        "BD-15-026-O002",
        "BD-15-026-O003",
        "BD-15-026-O004",
        "BD-15-026-O005",
        "BD-15-026-O006",
        "BD-15-026-O007"
      ],
      "when": "the same governed action is presented again under the declared identity or deduplication boundary"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC001",
        "BD-15-026-AC008",
        "BD-15-026-AC009",
        "BD-15-026-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O001",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Timeout."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC002",
        "BD-15-026-AC008",
        "BD-15-026-AC009",
        "BD-15-026-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O002",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Retry."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC003",
        "BD-15-026-AC008",
        "BD-15-026-AC009",
        "BD-15-026-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O003",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Circuit Breaker."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC004",
        "BD-15-026-AC008",
        "BD-15-026-AC009",
        "BD-15-026-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O004",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Rate Limit."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC005",
        "BD-15-026-AC008",
        "BD-15-026-AC009",
        "BD-15-026-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O005",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Concurrency."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC006",
        "BD-15-026-AC008",
        "BD-15-026-AC009",
        "BD-15-026-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O006",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Queue Priority."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-026-AC007",
        "BD-15-026-AC008",
        "BD-15-026-AC009",
        "BD-15-026-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-026-O007",
      "obligation_text": "Connector Policy là Business Object. Connector Policy quản lý: Health Threshold."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-15-026 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [
        "BD-15-026-AC009"
      ],
      "status": "APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [
        "BD-15-026-AC010"
      ],
      "status": "APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-15-026 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-15-026-AC001",
        "BD-15-026-AC002",
        "BD-15-026-AC003",
        "BD-15-026-AC004",
        "BD-15-026-AC005",
        "BD-15-026-AC006",
        "BD-15-026-AC007"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-15-026 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "ee03d86aebb32e8f73e9869bdeafedecb9cd82b42b231a2380c83f3973d444ac",
    "source_lines": "L1129-L1142",
    "source_section": "35. Business Decisions (Locked) > BD-15-026"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-027-AC001",
      "given": "a contract interaction at the integration boundary defined by Connector Routing Rule là Business Object. Routing Rule được cấu hình. Business Domain không quy…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-027-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-027-AC002",
      "given": "a contract interaction at the integration boundary defined by Connector Routing Rule là Business Object. Routing Rule được cấu hình. Business Domain không quy…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-027-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-027-AC003",
      "given": "a contract interaction at the integration boundary defined by Connector Routing Rule là Business Object. Routing Rule được cấu hình. Business Domain không quy…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-027-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-027-AC004",
      "given": "an interaction that violates the contract or ownership boundary for Connector Routing Rule là Business Object. Routing Rule được cấu hình. Business Domain không quy…",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-027-O001",
        "BD-15-027-O002",
        "BD-15-027-O003"
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
        "BD-15-027-AC001",
        "BD-15-027-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-027-O001",
      "obligation_text": "Connector Routing Rule là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-027-AC002",
        "BD-15-027-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-027-O002",
      "obligation_text": "Routing Rule được cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-027-AC003",
        "BD-15-027-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-027-O003",
      "obligation_text": "Business Domain không quyết định Connector"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector Routing Rule là Business Object. Routing Rule được cấu hình. Business Domain không quyết định Connector.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-027",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "31. Connector Routing Rule",
    "source_context_sha256": "2b5ae149f16258e6f19e3b618371fa39670739057e5cc4fda0dca2095e684d00",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "e9e3168d969b135921fdb9730d00b783fc0ae99e7a5bd003c4f9959d2ae00eb9",
    "source_lines": "L1145-L1152",
    "source_section": "35. Business Decisions (Locked) > BD-15-027"
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
  "stable_id": "BD-15-027",
  "title": "Connector Routing Rule là Business Object. Routing Rule được cấu hình. Business Domain không quy…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-028 — Connector phải khai báo Capability Matrix. Business Domain lựa chọn Connector dựa trên Capabilit…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-028-AC001",
      "given": "a contract interaction at the integration boundary defined by Connector phải khai báo Capability Matrix. Business Domain lựa chọn Connector dựa trên Capabilit…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-028-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-028-AC002",
      "given": "a contract interaction at the integration boundary defined by Connector phải khai báo Capability Matrix. Business Domain lựa chọn Connector dựa trên Capabilit…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-028-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-028-AC003",
      "given": "an interaction that violates the contract or ownership boundary for Connector phải khai báo Capability Matrix. Business Domain lựa chọn Connector dựa trên Capabilit…",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-028-O001",
        "BD-15-028-O002"
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
        "BD-15-028-AC001",
        "BD-15-028-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-028-O001",
      "obligation_text": "Connector phải khai báo Capability Matrix"
    },
    {
      "acceptance_criterion_references": [
        "BD-15-028-AC002",
        "BD-15-028-AC003"
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
    "source_fingerprint": "b2513ea88b32b9ff47a589964b78086265aeb923a5f1f5c114738c09308862b0",
    "source_lines": "L1155-L1160",
    "source_section": "35. Business Decisions (Locked) > BD-15-028"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-029-AC001",
      "given": "a contract interaction at the integration boundary defined by Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Re…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-029-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-029-AC002",
      "given": "a contract interaction at the integration boundary defined by Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Re…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-029-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-029-AC003",
      "given": "a contract interaction at the integration boundary defined by Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Re…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-029-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-029-AC004",
      "given": "a contract interaction at the integration boundary defined by Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Re…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-029-O004"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-029-AC005",
      "given": "a contract interaction at the integration boundary defined by Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Re…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-029-O005"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-029-AC006",
      "given": "a contract interaction at the integration boundary defined by Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Re…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-029-O006"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-029-AC007",
      "given": "a contract interaction at the integration boundary defined by Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Re…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-029-O007"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-029-AC008",
      "given": "an interaction that violates the contract or ownership boundary for Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Re…",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-029-O001",
        "BD-15-029-O002",
        "BD-15-029-O003",
        "BD-15-029-O004",
        "BD-15-029-O005",
        "BD-15-029-O006",
        "BD-15-029-O007"
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
        "BD-15-029-AC001",
        "BD-15-029-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-029-O001",
      "obligation_text": "Connector hỗ trợ Lifecycle: Draft."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-029-AC002",
        "BD-15-029-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-029-O002",
      "obligation_text": "Connector hỗ trợ Lifecycle: Configured."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-029-AC003",
        "BD-15-029-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-029-O003",
      "obligation_text": "Connector hỗ trợ Lifecycle: Validated."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-029-AC004",
        "BD-15-029-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-029-O004",
      "obligation_text": "Connector hỗ trợ Lifecycle: Testing."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-029-AC005",
        "BD-15-029-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-029-O005",
      "obligation_text": "Connector hỗ trợ Lifecycle: Active."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-029-AC006",
        "BD-15-029-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-029-O006",
      "obligation_text": "Connector hỗ trợ Lifecycle: Suspended."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-029-AC007",
        "BD-15-029-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-029-O007",
      "obligation_text": "Connector hỗ trợ Lifecycle: Retired."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Retired",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-15-029",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-15-029",
    "source_context_sha256": "381d81c5ec93ae99263a5596851482557a81362364f9a3697b7362de3afe4299",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "e8d452f617ad1ec6edccc5c056126f6d99cdf078db33429f4ff49089d5cc37f4",
    "source_lines": "L1163-L1174",
    "source_section": "35. Business Decisions (Locked) > BD-15-029"
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
  "stable_id": "BD-15-029",
  "title": "Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Re…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-15-030 — Connector Runtime Profile hỗ trợ: - Mock - Sandbox - UAT - Production Runtime tự động lựa chọn P…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-030-AC001",
      "given": "a contract interaction at the integration boundary defined by Connector Runtime Profile hỗ trợ: - Mock - Sandbox - UAT - Production Runtime tự động lựa chọn P…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-030-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-030-AC002",
      "given": "a contract interaction at the integration boundary defined by Connector Runtime Profile hỗ trợ: - Mock - Sandbox - UAT - Production Runtime tự động lựa chọn P…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-030-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-030-AC003",
      "given": "a contract interaction at the integration boundary defined by Connector Runtime Profile hỗ trợ: - Mock - Sandbox - UAT - Production Runtime tự động lựa chọn P…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-030-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BD-15-030-AC004",
      "given": "a contract interaction at the integration boundary defined by Connector Runtime Profile hỗ trợ: - Mock - Sandbox - UAT - Production Runtime tự động lựa chọn P…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BD-15-030-O004"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BD-15-030-AC005",
      "given": "an interaction that violates the contract or ownership boundary for Connector Runtime Profile hỗ trợ: - Mock - Sandbox - UAT - Production Runtime tự động lựa chọn P…",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BD-15-030-O001",
        "BD-15-030-O002",
        "BD-15-030-O003",
        "BD-15-030-O004"
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
        "BD-15-030-AC001",
        "BD-15-030-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-030-O001",
      "obligation_text": "Connector Runtime Profile hỗ trợ: Mock."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-030-AC002",
        "BD-15-030-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-030-O002",
      "obligation_text": "Connector Runtime Profile hỗ trợ: Sandbox."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-030-AC003",
        "BD-15-030-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-030-O003",
      "obligation_text": "Connector Runtime Profile hỗ trợ: UAT."
    },
    {
      "acceptance_criterion_references": [
        "BD-15-030-AC004",
        "BD-15-030-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-15-030-O004",
      "obligation_text": "Connector Runtime Profile hỗ trợ: Production Runtime tự động lựa chọn Profile theo Environment."
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
    "source_fingerprint": "339e0c51785e863f5cd6103e0a346c4c80dbcbc069cc436c0cc6baa7b7d7d78f",
    "source_lines": "L1177-L1187",
    "source_section": "35. Business Decisions (Locked) > BD-15-030"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R003-AC001",
      "given": "a contract interaction at the integration boundary defined by API Gateway là thành phần bắt buộc của Platform",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BRD-WS-15-R003-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-15-R003-AC002",
      "given": "an interaction that violates the contract or ownership boundary for API Gateway là thành phần bắt buộc của Platform",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BRD-WS-15-R003-O001"
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
        "BRD-WS-15-R003-AC001",
        "BRD-WS-15-R003-AC002"
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
    "source_lines": "L146",
    "source_section": "5. API Gateway"
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
### BRD-WS-15-R004 — Kiến trúc hỗ trợ mở rộng thêm Gateway mới khi cần

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R004-AC001",
      "given": "a contract interaction at the integration boundary defined by Kiến trúc hỗ trợ mở rộng thêm Gateway mới khi cần",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BRD-WS-15-R004-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-15-R004-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Kiến trúc hỗ trợ mở rộng thêm Gateway mới khi cần",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BRD-WS-15-R004-O001"
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
        "BRD-WS-15-R004-AC001",
        "BRD-WS-15-R004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R004-O001",
      "obligation_text": "Kiến trúc hỗ trợ mở rộng thêm Gateway mới khi cần"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Kiến trúc hỗ trợ mở rộng thêm Gateway mới khi cần.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-006"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-15-004",
    "previous_temporary_key": "TMP-BRD-WS-15-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Gateway Separation",
    "source_context_sha256": "2594da7df7f45957b5539cb25689975d7ca2a586fb4a8bad50c763112d785a59",
    "source_document": "docs/BRD/BRD-WS-15.md",
    "source_fingerprint": "431fc7238221528f8f818e767a6d9c7c05b440b31dab409e0fe3812e590a03d8",
    "source_lines": "L225",
    "source_section": "8. Gateway Separation"
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
  "title": "Kiến trúc hỗ trợ mở rộng thêm Gateway mới khi cần",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-15-R005 — Một Event mới không được phép phá vỡ khả năng tương thích ngược (Backward Compatibility) nếu vẫn…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R005-AC001",
      "given": "the applicable business context, actor, and input for Một Event mới không được phép phá vỡ khả năng tương thích ngược (Backward Compatibility) nếu vẫn…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-15-R005-O001"
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
        "BRD-WS-15-R005-AC001"
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
    "source_lines": "L276",
    "source_section": "11. Event Version"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R006-AC001",
      "given": "the applicable business context, actor, and input for Business Domain không được tạo dữ liệu trùng khi nhận cùng một Request hoặc Event nhiều lần",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-15-R006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-15-R006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Domain không được tạo dữ liệu trùng khi nhận cùng một Request hoặc Event nhiều lần",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-15-R006-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-15-R006-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Business Domain không được tạo dữ liệu trùng khi nhận cùng một Request hoặc Event nhiều lần",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-15-R006-O001"
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
      "criterion_references": [],
      "rationale": "BRD-WS-15-R006 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-15-R006-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-15-R006-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L321",
    "source_section": "13. Idempotency"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R007-AC001",
      "given": "the applicable business context, actor, and input for Retry không được Hard-code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-15-R007-O001"
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
        "BRD-WS-15-R007-AC001"
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
    "source_lines": "L347",
    "source_section": "14. Retry Policy"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R008-AC001",
      "given": "a candidate DLQ phải lưu đầy đủ: - Message record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "the accepted record contains the field named by the obligation, preserves its submitted attribution, and exposes that stored value when the record is inspected",
      "verifies": [
        "BRD-WS-15-R008-O001"
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
        "BRD-WS-15-R008-AC001"
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
    "source_lines": "L365-L367",
    "source_section": "15. Dead Letter Queue"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R009-AC001",
      "given": "a candidate DLQ phải lưu đầy đủ: - Event record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "the accepted record contains the field named by the obligation, preserves its submitted attribution, and exposes that stored value when the record is inspected",
      "verifies": [
        "BRD-WS-15-R009-O001"
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
        "BRD-WS-15-R009-AC001"
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
    "source_fingerprint": "8ea559bcbbd1fcac430d72b7f0dac1f7df94b681ea905df55e136290e71a701d",
    "source_lines": "L365-L368",
    "source_section": "15. Dead Letter Queue"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R010-AC001",
      "given": "a contract interaction at the integration boundary defined by DLQ phải lưu đầy đủ: - Connector",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BRD-WS-15-R010-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-15-R010-AC002",
      "given": "an interaction that violates the contract or ownership boundary for DLQ phải lưu đầy đủ: - Connector",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BRD-WS-15-R010-O001"
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
        "BRD-WS-15-R010-AC001",
        "BRD-WS-15-R010-AC002"
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
    "source_fingerprint": "9f83a8ed5134079b8c647e1023dde12ec5f0884cba14c6f9d9d0aa34d08bfac1",
    "source_lines": "L365-L369",
    "source_section": "15. Dead Letter Queue"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R011-AC001",
      "given": "a candidate DLQ phải lưu đầy đủ: - Error record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "the accepted record contains the field named by the obligation, preserves its submitted attribution, and exposes that stored value when the record is inspected",
      "verifies": [
        "BRD-WS-15-R011-O001"
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
        "BRD-WS-15-R011-AC001"
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
    "source_fingerprint": "9e8f7f015b429d042fc83fddc3e2f96f567a45a5e8ff2f5860962c2f13f8eb89",
    "source_lines": "L365-L370",
    "source_section": "15. Dead Letter Queue"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R012-AC001",
      "given": "a candidate DLQ phải lưu đầy đủ: - Retry History record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "the accepted record contains the field named by the obligation, preserves its submitted attribution, and exposes that stored value when the record is inspected",
      "verifies": [
        "BRD-WS-15-R012-O001"
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
        "BRD-WS-15-R012-AC001"
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
    "source_fingerprint": "d18be71d1f648bedd8c2998b0107696462565f435cf070bcc85a843d02742358",
    "source_lines": "L365-L371",
    "source_section": "15. Dead Letter Queue"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R013-AC001",
      "given": "a candidate DLQ phải lưu đầy đủ: - Failure Reason record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "the accepted record contains the field named by the obligation, preserves its submitted attribution, and exposes that stored value when the record is inspected",
      "verifies": [
        "BRD-WS-15-R013-O001"
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
        "BRD-WS-15-R013-AC001"
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
    "source_fingerprint": "3ce54c21f663ce49e8a5cfb0ce836eb8815e79cd6fe528a36826b26c3a5ff6e8",
    "source_lines": "L365-L372",
    "source_section": "15. Dead Letter Queue"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R014-AC001",
      "given": "the applicable business context, actor, and input for Callback luôn được: - Authenticate",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-15-R014-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-15-R014-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Callback luôn được: - Authenticate",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-15-R014-O001"
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
        "BRD-WS-15-R014-AC001",
        "BRD-WS-15-R014-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R014-O001",
      "obligation_text": "Callback luôn được: - Authenticate"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R014 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R014 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-15-R014-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R014 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_lines": "L389-L391",
    "source_section": "16. Callback"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R015-AC001",
      "given": "the applicable business context, actor, and input for Callback luôn được: - Validate",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-15-R015-O001"
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
        "BRD-WS-15-R015-AC001"
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
    "source_fingerprint": "9b645c0491b45d006c3c14a1290cf2997ff1f234a782946250457a4bf261379d",
    "source_lines": "L389-L392",
    "source_section": "16. Callback"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R016-AC001",
      "given": "an operational task within the scope of Callback luôn được: - Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-15-R016-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-15-R016-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Callback luôn được: - Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-15-R016-O001"
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
        "BRD-WS-15-R016-AC001",
        "BRD-WS-15-R016-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R016-O001",
      "obligation_text": "Callback luôn được: - Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R016 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R016 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R016 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R016 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-15-R016-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R016 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "5bbaccb26b3b6d310d6ffaffe5c9714e9e9a22a2bbdd190f3e8a7e4f73eebc76",
    "source_lines": "L389-L393",
    "source_section": "16. Callback"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R017-AC001",
      "given": "the applicable business context, actor, and input for Callback luôn được: - Idempotent Check",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-15-R017-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-15-R017-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Callback luôn được: - Idempotent Check",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-15-R017-O001"
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
        "BRD-WS-15-R017-AC001",
        "BRD-WS-15-R017-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-15-R017-O001",
      "obligation_text": "Callback luôn được: - Idempotent Check"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R017 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R017 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R017 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R017 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-15-R017-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-15-R017 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
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
    "source_fingerprint": "c9417cee3c91312d70997b61285f3197ec10fb8f449cb3d8cf347f584ffcc887",
    "source_lines": "L389-L394",
    "source_section": "16. Callback"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R018-AC001",
      "given": "a contract interaction at the integration boundary defined by Một API mới không được làm ảnh hưởng đến các Client đang sử dụng Version cũ",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BRD-WS-15-R018-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-15-R018-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Một API mới không được làm ảnh hưởng đến các Client đang sử dụng Version cũ",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BRD-WS-15-R018-O001"
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
        "BRD-WS-15-R018-AC001",
        "BRD-WS-15-R018-AC002"
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
    "source_lines": "L435",
    "source_section": "18. API Version"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R019-AC001",
      "given": "a contract interaction at the integration boundary defined by Deprecation Policy phải được công bố trước khi loại bỏ một API Version",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BRD-WS-15-R019-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-15-R019-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Deprecation Policy phải được công bố trước khi loại bỏ một API Version",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BRD-WS-15-R019-O001"
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
        "BRD-WS-15-R019-AC001",
        "BRD-WS-15-R019-AC002"
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
    "source_lines": "L437",
    "source_section": "18. API Version"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R020-AC001",
      "given": "a contract interaction at the integration boundary defined by Business Domain không cần biết Connector đang sử dụng Profile nào",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BRD-WS-15-R020-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-15-R020-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Business Domain không cần biết Connector đang sử dụng Profile nào",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BRD-WS-15-R020-O001"
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
        "BRD-WS-15-R020-AC001",
        "BRD-WS-15-R020-AC002"
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
    "source_lines": "L464",
    "source_section": "19. Connector Profile"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R021-AC001",
      "given": "the applicable business context, actor, and input for Scheduler luôn Publish Event",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-15-R021-O001"
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
        "BRD-WS-15-R021-AC001"
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
    "source_lines": "L644",
    "source_section": "26. Scheduler Event"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R022-AC001",
      "given": "the applicable business context, actor, and input for Business Domain không cần biết Event đến từ hệ thống nào",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-15-R022-O001"
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
        "BRD-WS-15-R022-AC001"
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
    "source_lines": "L720",
    "source_section": "29. Canonical Event Model"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R023-AC001",
      "given": "a contract interaction at the integration boundary defined by Mỗi Connector phải khai báo Capability",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BRD-WS-15-R023-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-15-R023-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Mỗi Connector phải khai báo Capability",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BRD-WS-15-R023-O001"
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
        "BRD-WS-15-R023-AC001",
        "BRD-WS-15-R023-AC002"
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
    "source_lines": "L771",
    "source_section": "32. Integration Capability Matrix"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R024-AC001",
      "given": "a contract interaction at the integration boundary defined by Connector chỉ được phép xử lý giao dịch khi ở trạng thái Active",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BRD-WS-15-R024-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-15-R024-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Connector chỉ được phép xử lý giao dịch khi ở trạng thái Active",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BRD-WS-15-R024-O001"
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
        "BRD-WS-15-R024-AC001",
        "BRD-WS-15-R024-AC002"
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
    "source_lines": "L831",
    "source_section": "33. Connector Lifecycle"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R025-AC001",
      "given": "the applicable business context, actor, and input for Business Domain không cần biết Runtime Profile đang được sử dụng",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-15-R025-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-15-R025-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Business Domain không cần biết Runtime Profile đang được sử dụng",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-15-R025-O001"
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
        "BRD-WS-15-R025-AC001",
        "BRD-WS-15-R025-AC002"
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
    "source_lines": "L855",
    "source_section": "34. Connector Runtime Profile"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "BRD-WS-15-R026-AC001",
      "given": "a contract interaction at the integration boundary defined by API Gateway là thành phần bắt buộc",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "BRD-WS-15-R026-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "BRD-WS-15-R026-AC002",
      "given": "an interaction that violates the contract or ownership boundary for API Gateway là thành phần bắt buộc",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "BRD-WS-15-R026-O001"
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
        "BRD-WS-15-R026-AC001",
        "BRD-WS-15-R026-AC002"
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
    "source_fingerprint": "f031b70591de7d42955b3c9e9fcc42c2078b36efc1f5041d83f087cf0d5688ae",
    "source_lines": "L886-L891",
    "source_section": "35. Business Decisions (Locked) > BD-15-002"
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
### EP-15-001 — Business Domain không được tích hợp trực tiếp với hệ thống bên ngoài

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-15-001-AC001",
      "given": "the applicable business context, actor, and input for Business Domain không được tích hợp trực tiếp với hệ thống bên ngoài",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "EP-15-001-O001"
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
        "EP-15-001-AC001"
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
    "source_fingerprint": "2f9afb0529f43f4d2dc76ee8d75fbd1e499536bb9be9ad6691b821432927af14",
    "source_lines": "L1192-L1195",
    "source_section": "36. Enterprise Design Principles > EP-15-001"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EP-15-002-AC001",
      "given": "a contract interaction at the integration boundary defined by Toàn bộ Integration phải đi qua Gateway, Connector và Adapter",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EP-15-002-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "EP-15-002-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Toàn bộ Integration phải đi qua Gateway, Connector và Adapter",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "EP-15-002-O001"
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
        "EP-15-002-AC001",
        "EP-15-002-AC002"
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
    "source_fingerprint": "37b42908adece8386e4a4c27f36201344abb18d3fdfd2d7830db885db568acf0",
    "source_lines": "L1198-L1201",
    "source_section": "36. Enterprise Design Principles > EP-15-002"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "EP-15-003-AC001",
      "given": "a candidate Business Domain chỉ sử dụng Canonical Data Model record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "EP-15-003-O001"
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
        "EP-15-003-AC001"
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
    "source_fingerprint": "61c653acae008bf350a9ab724669f38df667dd28ac1c3ac26871b66244bbde46",
    "source_lines": "L1204-L1207",
    "source_section": "36. Enterprise Design Principles > EP-15-003"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-15-004-AC001",
      "given": "the applicable business context, actor, and input for Business Domain chỉ sử dụng Canonical Event Model",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-15-004-O001"
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
        "EP-15-004-AC001"
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
    "source_fingerprint": "1a908eaa0623f7e9f9c5955c725639a9ec625de4ed4d518ed876dbdc60ea557c",
    "source_lines": "L1210-L1213",
    "source_section": "36. Enterprise Design Principles > EP-15-004"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-15-005-AC001",
      "given": "the applicable business context, actor, and input for Toàn Platform giao tiếp nội bộ theo Event-Driven Architecture",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-15-005-O001"
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
        "EP-15-005-AC001"
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
    "source_fingerprint": "b591ec9e9650ac07fae0aa4b14334f9e85faace1eb3ee5b641872e61d44e4e2f",
    "source_lines": "L1216-L1219",
    "source_section": "36. Enterprise Design Principles > EP-15-005"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-15-006-AC001",
      "given": "the applicable business context, actor, and input for Mọi Business Domain đều Publish Business Event",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-15-006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "EP-15-006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Mọi Business Domain đều Publish Business Event",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "EP-15-006-O001"
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
        "EP-15-006-AC001",
        "EP-15-006-AC002"
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
    "source_fingerprint": "fee64b071c9204d2832f1628396dc4435ad6a80cf86c3b71f52e9edb22c2cea9",
    "source_lines": "L1222-L1225",
    "source_section": "36. Enterprise Design Principles > EP-15-006"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EP-15-007-AC001",
      "given": "a contract interaction at the integration boundary defined by Connector Policy được cấu hình. Không Hard-code",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EP-15-007-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EP-15-007-AC002",
      "given": "a contract interaction at the integration boundary defined by Connector Policy được cấu hình. Không Hard-code",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EP-15-007-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "EP-15-007-AC003",
      "given": "an interaction that violates the contract or ownership boundary for Connector Policy được cấu hình. Không Hard-code",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "EP-15-007-O001",
        "EP-15-007-O002"
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
        "EP-15-007-AC001",
        "EP-15-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-15-007-O001",
      "obligation_text": "Connector Policy được cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "EP-15-007-AC002",
        "EP-15-007-AC003"
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
    "source_fingerprint": "11737fba2f7cf87234d09c393829fad73b99d60862efc4a188c1ee543cb805d9",
    "source_lines": "L1228-L1233",
    "source_section": "36. Enterprise Design Principles > EP-15-007"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EP-15-008-AC001",
      "given": "a contract interaction at the integration boundary defined by Connector được lựa chọn bằng Routing Rule",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EP-15-008-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "EP-15-008-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Connector được lựa chọn bằng Routing Rule",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "EP-15-008-O001"
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
        "EP-15-008-AC001",
        "EP-15-008-AC002"
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
    "source_fingerprint": "6380f512ef34a1da0f7a83830038183938d601a415279a3e5f81f0a12e264fdb",
    "source_lines": "L1236-L1239",
    "source_section": "36. Enterprise Design Principles > EP-15-008"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EP-15-009-AC001",
      "given": "a contract interaction at the integration boundary defined by Integration Platform phải hỗ trợ Runtime Profile",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EP-15-009-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "EP-15-009-AC002",
      "given": "an interaction that violates the contract or ownership boundary for Integration Platform phải hỗ trợ Runtime Profile",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "EP-15-009-O001"
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
        "EP-15-009-AC001",
        "EP-15-009-AC002"
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
    "source_fingerprint": "dd4aa5fb20499f8d00bf4123ec4fbbef30d2f1bf541ab1f07478479add011c0c",
    "source_lines": "L1242-L1245",
    "source_section": "36. Enterprise Design Principles > EP-15-009"
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
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-15-010-AC001",
      "given": "an operational task within the scope of Integration Platform phải hỗ trợ Monitoring, Health, Retry, DLQ và Observability",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "EP-15-010-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "EP-15-010-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Integration Platform phải hỗ trợ Monitoring, Health, Retry, DLQ và Observability",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "EP-15-010-O001"
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
        "EP-15-010-AC001",
        "EP-15-010-AC002"
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
    "source_fingerprint": "7a9ccd02436f561733ad515ccf8142cf18610e672dfe37782c22e6d22d0a9fe2",
    "source_lines": "L1248-L1251",
    "source_section": "36. Enterprise Design Principles > EP-15-010"
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
