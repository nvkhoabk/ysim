---
document_code: ESP-03
document_name: Enterprise Naming Standards
project: YSim v2.1
document_set: Engineering Standards Pack
version: 2.1
status: FROZEN
language: en-US
---

# Enterprise Naming Standards

## ESP-03

---

# 1. Purpose

Enterprise Naming Standards định nghĩa hệ thống quy tắc đặt tên thống nhất cho toàn bộ nền tảng YSim.

Tiêu chuẩn này áp dụng cho:

- Business Objects
- Business Capabilities
- Domains
- Modules
- Applications
- APIs
- Events
- Snapshots
- Source Code
- Database Objects
- Configuration
- Infrastructure
- AI Artifacts
- Documentation
- Frontend
- Design System
- Experience Components

Naming là ngôn ngữ chung của toàn bộ Platform.

---

# 2. Objectives

Enterprise Naming nhằm:

- Chuẩn hóa ngôn ngữ kỹ thuật.
- Tăng khả năng đọc hiểu.
- Tăng khả năng tìm kiếm.
- Hỗ trợ AI Repository Discovery.
- Hỗ trợ Traceability.
- Giảm trùng lặp thuật ngữ.

---

# 3. Naming Principles

Tên phải:

- Meaningful
- Consistent
- Domain Driven
- Business Aligned
- Technology Neutral
- Predictable
- Search Friendly
- AI Friendly
- Full-stack Consistency
- Experience-aware Naming

Tên không được phụ thuộc vào cá nhân.

---

# 4. Enterprise Naming Hierarchy

Naming được chuẩn hóa theo thứ tự:

```text
Business Domain
        │
Business Capability
        │
Business Object
        │
Module
        │
Component
        │
Class
        │
Method
        │
Variable
```

Tên ở tầng dưới phải phản ánh đúng tầng trên.

---

# 5. Language Standards

Toàn bộ tên phải sử dụng:

- English
- Singular form (đối với Business Object và Entity)
- PascalCase, camelCase hoặc kebab-case theo từng loại Artifact

Không sử dụng:

- tiếng Việt;
- viết tắt nội bộ;
- tên không có nghĩa.

---

# 6. Business Naming

Business Object:

```text
Customer
Order
Payment
Settlement
Partner
Agency
Package
Activation
```

Không sử dụng:

```text
CustomerData
OrderInfo
PackageObject
```

Business Object chỉ sử dụng danh từ.

---

# 7. Capability Naming

Capability sử dụng:

```text
Customer Management

Payment Processing

Package Catalog

Settlement Management
```

Capability sử dụng:

> Noun + Action

hoặc

> Business Function

Không sử dụng tên mang tính kỹ thuật.

---

# 8. Module Naming

Module sử dụng:

```text
customer

payment

pricing

settlement

notification
```

Quy tắc:

- lowercase
- singular
- kebab-case nếu nhiều từ

Ví dụ:

```text
customer-care

payment-gateway

partner-management
```

---

# 8A. Frontend & Experience Naming

Frontend được chuẩn hóa theo Capability.

Ví dụ:

```text
pages/

login/

product-catalog/

checkout/

order-history/
```

Component:

```text
ProductCard

CheckoutSummary

PaymentMethodSelector

OrderStatusBadge
```

Design System:

```text
Button

Input

Modal

Toast

ThemeProvider
```

Capability Demonstration:

```text
demo-login

demo-checkout

demo-payment

demo-order
```

Tên phải phản ánh đúng Business Capability, không phụ thuộc Framework hoặc UI Library.


---

# 9. Application Naming

Applications sử dụng:

```text
portal

admin

api

agency

worker

scheduler
```

Không đặt tên theo công nghệ.

Ví dụ:

❌ nest-api

❌ node-api

---

# 10. Package Naming

Packages:

```text
core

shared

contracts

events

utils

sdk
```

Package Name phải phản ánh chức năng.

---

# 11. Class Naming

Class:

- PascalCase

Ví dụ:

```text
CustomerService

CreateOrderUseCase

PaymentRepository

SettlementEvent
```

Không sử dụng:

```text
customerService

Customer_Service

ServiceCustomer
```

---

# 12. Interface Naming

Interface:

```text
PaymentGateway

CustomerRepository

NotificationProvider
```

Không thêm tiền tố:

```text
IPayment

ICustomerRepository
```

Trừ khi ngôn ngữ/framework bắt buộc.

---

# 13. Method Naming

Method:

- camelCase
- Verb + Object

Ví dụ:

```text
createOrder()

activateEsim()

calculatePrice()

findCustomer()

sendNotification()
```

Không sử dụng:

```text
doIt()

process()

run()

executeTask()
```

trừ khi đó là tên chuẩn của Framework hoặc Pattern.

---

# 14. Variable Naming

Variable:

- camelCase

Ví dụ:

```text
customerId

paymentAmount

activationResult

orderStatus
```

Không sử dụng:

```text
tmp

data

obj

var1
```

ngoại trừ biến lặp ngắn trong phạm vi rất nhỏ (`i`, `j`, `item`) khi ngữ cảnh rõ ràng.

---

# 15. Constant Naming

Constant:

```text
MAX_RETRY_COUNT

DEFAULT_TIMEOUT

SYSTEM_USER
```

Toàn bộ viết:

UPPER_SNAKE_CASE

---

# 16. API Naming

Endpoint:

```text
GET /customers

POST /orders

POST /payments

GET /packages
```

Quy tắc:

- lowercase
- plural resource
- kebab-case nếu nhiều từ

Ví dụ:

```text
/partner-orders

/customer-profiles
```

---

# 17. Event Naming

Event:

```text
OrderCreated

PaymentSucceeded

PackageAssigned

SettlementCompleted
```

Pattern:

```text
BusinessObject + PastTenseVerb
```

---

# 18. Snapshot Naming

Snapshot:

```text
CustomerSnapshot

PackageSnapshot

SettlementSnapshot
```

Pattern:

```text
BusinessObject + Snapshot
```

---

# 19. Database Naming

Table:

```text
customers

orders

payments

packages
```

Primary Key:

```text
id
```

Foreign Key:

```text
customer_id

order_id

package_id
```

Index:

```text
idx_customer_phone

idx_order_status
```

Unique Constraint:

```text
uk_partner_code
```

---

# 20. Configuration Naming

Environment Variable:

```text
DATABASE_URL

REDIS_URL

JWT_SECRET

ONEPAY_API_KEY
```

Toàn bộ:

UPPER_SNAKE_CASE

---

# 21. AI Artifact Naming

AI Workspace:

```text
SPR-017.yaml

verification-report.md

evidence.json

planning-report.md
```

Tên phải phản ánh loại Artifact và mục đích sử dụng.

Capability Demonstration:

```text
demo-login.md

demo-checkout.md

demo-order-payment.md
```

Screenshot:

```text
login-page.png

checkout-page.png

payment-success.png
```


---

# 22. Prohibited Naming

Không sử dụng:

- temp
- test1
- data
- object
- abc
- xyz
- newCustomer2
- finalVersion
- tmp

Tên phải có ý nghĩa nghiệp vụ hoặc kỹ thuật rõ ràng.

---

# 23. Naming Rules

NS-001 — Toàn bộ tên sử dụng tiếng Anh.

NS-002 — Business Object sử dụng danh từ số ít.

NS-003 — Method sử dụng Verb + Object.

NS-004 — Event sử dụng BusinessObject + PastTenseVerb.

NS-005 — Snapshot sử dụng BusinessObject + Snapshot.

NS-006 — API sử dụng resource dạng số nhiều.

NS-007 — Không sử dụng viết tắt nội bộ.

NS-008 — Không sử dụng tên mơ hồ.

NS-009 — Naming phải thống nhất trên toàn Platform.

NS-010 — AI phải tuân thủ Enterprise Naming Standards.

NS-011 — Frontend Page, Component và Route phải đặt tên theo Business Capability.

NS-012 — Capability Demonstration Asset phải sử dụng tiền tố `demo-`.


---

# 24. Naming Compliance Checklist

| Rule | Validation |
|------|------------|
| ENC-0301 | Business Naming đúng chuẩn |
| ENC-0302 | Module Naming đúng chuẩn |
| ENC-0303 | Class Naming đúng chuẩn |
| ENC-0304 | Method Naming đúng chuẩn |
| ENC-0305 | Variable Naming đúng chuẩn |
| ENC-0306 | API Naming đúng chuẩn |
| ENC-0307 | Event Naming đúng chuẩn |
| ENC-0308 | Database Naming đúng chuẩn |
| ENC-0309 | Configuration Naming đúng chuẩn |
| ENC-0310 | AI Artifact Naming đúng chuẩn |
| ENC-0311 | Frontend Naming đúng chuẩn |
| ENC-0312 | Demonstration Naming đúng chuẩn |

---

# 25. Relationship to Other Documents

ESP-03 liên kết với:

- BRD Business Object Registry
- BRD Capability Registry
- YADF Meta Model
- ABP-04 Domain Architecture
- ABP-05 Event Architecture
- ESP-01 Repository Architecture Standards
- ESP-02 Source Code Engineering Standards
- ESP-04 API Standards

Enterprise Naming Standards là ngôn ngữ thống nhất giữa Business Architecture, Engineering Architecture, Frontend, Design System và Capability Demonstration.

---

# 26. Document Status

**Status: FROZEN**

ESP-03 là tài liệu chuẩn hóa hệ thống đặt tên của nền tảng YSim.

Mọi Business Artifact, Engineering Artifact và AI Artifact phải tuân thủ Enterprise Naming Standards.

---