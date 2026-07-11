---
document_code: BRD-WS-15
document_name: Integration Platform, API Gateway & Event Bus
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-15
---

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