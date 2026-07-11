---
document_code: BRD-WS-03
document_name: Identity, Organization & Access Control Model
project: YSim v2.0
document_set: BRD
version: 2.0
status: FROZEN
language: vi-VN
author: ChatGPT + Project Team
last_updated: 2026-07
workshop: WS-03
---

# BRD Workshop 03

# Identity, Organization & Access Control Model

---

# 1. Workshop Objective

Workshop này xác định nền tảng quản lý Identity, Organization, User, Customer, Portal, Storefront và mô hình phân quyền của toàn bộ hệ thống YSim.

Workshop này là Foundation Layer cho toàn bộ:

- CRM
- Customer Support
- Admin Portal
- Partner Portal
- Customer Portal
- White-label
- Storefront
- Notification
- Settlement
- Reporting
- Audit
- Security

Sau Workshop này, toàn bộ Identity Foundation được đóng băng.

---

# 2. Organization Model

YSim quản lý toàn bộ kênh bán hàng theo mô hình Organization.

Một Organization có thể là:

- Doanh nghiệp
- Chi nhánh
- Phòng ban
- Cá nhân kinh doanh

Ví dụ:

```text
ABC Travel

├── Hanoi Branch
│      ├── Sales Department
│      ├── Accounting
│      ├── Customer Support
│      └── Director
│
└── HCM Branch
       ├── Sales Department
       └── Customer Support
```

Một Organization có thể chỉ bao gồm một cá nhân nhưng vẫn được xem là một Organization hợp lệ.

---

# 3. Organization Structure

Organization Structure mô tả cơ cấu nội bộ của Organization.

Ví dụ:

- Branch
- Department
- Team

Đây là mô hình phục vụ:

- Permission
- Reporting
- Internal Management

Organization Structure độc lập với Distribution Network.

---

# 4. Distribution Network

Distribution Network mô tả mạng lưới phân phối.

Ví dụ:

```text
YSim

└── ABC Travel

      ├── Agency A

      │      ├── Seller A

      │      └── Seller B

      └── Agency B

             └── Seller C
```

Distribution Network được sử dụng cho:

- Commission
- Settlement
- Customer Ownership
- Support Escalation

---

# 5. Internal Organization

YSim cũng là một Organization.

Bao gồm:

- Product
- Operations
- Customer Support
- Finance
- Sales
- Marketing
- Management

YSim sử dụng chính nền tảng của mình để triển khai hoạt động bán hàng và chăm sóc khách hàng.

---

# 6. Portal

Portal là giao diện dành cho User nội bộ của Organization.

Ví dụ:

- portal.ysim.vn
- portal.abctravel.vn

Portal hỗ trợ:

- Sales
- CRM
- Product Management
- Payment Configuration
- Settlement
- Reporting
- Customer Support
- Operations

Portal không dành cho End Customer.

---

# 7. Storefront

Storefront là giao diện dành cho End Customer.

Một Organization có thể có nhiều Storefront.

Ví dụ:

- esim.abctravel.vn
- thailand.abctravel.vn
- vietnam.abctravel.vn
- Landing Page
- Campaign Page
- QR Landing

Storefront hỗ trợ:

- giới thiệu sản phẩm
- đặt hàng
- thanh toán
- fulfillment
- customer portal
- hướng dẫn sử dụng
- hỗ trợ khách hàng

Storefront không hiển thị:

- giá vốn
- commission
- settlement
- dữ liệu nội bộ

---

# 8. Customer Portal

Customer Portal là Storefront mở rộng.

Customer Portal cho phép:

- xem đơn hàng
- xem QR Code
- tải lại eSIM
- xem hướng dẫn
- gửi yêu cầu hỗ trợ
- theo dõi Ticket
- nhận Notification

Customer Portal được truy cập thông qua:

- Email
- SMS
- WhatsApp
- Telegram
- Line
- các Identity Provider khác

---

# 9. Identity Domain

Identity là Foundation Domain.

Identity không thuộc User.

Identity không thuộc Customer.

Identity chỉ là phương thức định danh.

Ví dụ:

- Email
- Phone
- Google
- Apple
- Facebook
- WhatsApp
- Line
- WeChat
- Telegram

Một Identity có thể liên kết tới:

- User
- Customer

User và Customer luôn là hai Business Entity độc lập.

---

# 10. User

User là người sử dụng Portal.

Mỗi User chỉ thuộc duy nhất một Organization.

Nếu một người làm việc cho nhiều Organization thì phải có nhiều User khác nhau.

Một User có thể được cấp quyền trên nhiều Storefront của Organization.

---

# 11. Customer

Customer là Person sử dụng eSIM.

Customer độc lập với User.

Customer có thể:

- chỉ quan tâm sản phẩm
- đăng ký thông tin
- mua hàng
- kích hoạt eSIM
- sử dụng dịch vụ
- yêu cầu hỗ trợ

Customer có thể Merge nếu phát hiện trùng.

Customer có thể Group theo:

- Tour
- Đơn hàng
- Đoàn khách
- Campaign

---

# 12. Roles

Role thuộc Organization.

Ví dụ:

- Director
- Sales
- Accountant
- Customer Support
- Marketing
- Operations
- Collaborator

Organization có thể:

- tạo Role
- sửa Role
- xóa Role
- gán Permission

YSim cung cấp Role Template mặc định.

---

# 13. Collaborator

Collaborator không phải Organization.

Collaborator là User thuộc một Organization.

Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem:

- khách hàng của mình
- doanh thu của mình
- commission của mình

Collaborator không được xem dữ liệu nội bộ của Organization nếu không được cấp quyền.

---

# 14. Permission Model

Permission gồm:

- Action Permission
- Resource Scope
- Data Scope
- Masking Policy
- Time Policy
- Audit Policy

Permission được gán thông qua Role.

---

# 15. Data Scope

Data Scope xác định phạm vi dữ liệu được truy cập.

Ví dụ:

- Own
- Team
- Department
- Organization
- Distribution Tree
- Assigned
- Global

Role và Data Scope là hai khái niệm độc lập.

---

# 16. Data Masking

Các trường dữ liệu nhạy cảm phải hỗ trợ Masking.

Ví dụ:

Sales:

```text
kh***@gmail.com
```

Customer Support:

```text
khoa@gmail.com
```

Accountant:

```text
*************
```

Masking được cấu hình theo từng trường dữ liệu.

---

# 17. Organization Boundary

Organization là ranh giới dữ liệu.

Một Organization không được phép truy cập dữ liệu của Organization khác nếu không được phép theo Business Rule.

---

# 18. Customer Ownership

Customer thuộc Distribution Network.

Ví dụ:

```text
YSim

└── ABC Travel

      └── Agency A

            └── Seller A

                    └── Customer
```

Customer Ownership phục vụ:

- CRM
- Commission
- Settlement
- Analytics
- Customer Support

---

# 19. Support Governance

Support Governance độc lập với Ownership.

Support Policy gồm:

- SELF_SUPPORT
- PARENT_SUPPORT (Default)
- HYBRID

Trong chế độ PARENT_SUPPORT, yêu cầu hỗ trợ sẽ tự động chuyển lên Organization cha theo Distribution Network.

Nếu Organization cha tiếp tục sử dụng PARENT_SUPPORT thì yêu cầu sẽ tiếp tục được chuyển lên cấp cao hơn cho đến khi gặp Organization có khả năng hỗ trợ.

---

# 20. Support Access

Quyền xem dữ liệu Customer được xác định dựa trên:

- Role
- Data Scope
- Organization Policy
- Support Policy
- Customer Ownership
- Distribution Hierarchy
- Masking Policy

Ví dụ:

- Seller xem khách hàng của mình.
- Agency Support xem khách hàng của Seller trực thuộc nếu được cấu hình.
- Partner cấp trên hỗ trợ Partner cấp dưới theo Support Policy.
- YSim Customer Support chỉ truy cập khi yêu cầu được chuyển lên theo chuỗi Support.

---

# 21. Tracking Model

Tracking ID là Business Object.

Tracking liên kết:

- Storefront
- Campaign
- Sales
- Customer
- Order
- Commission
- Settlement
- Analytics

Mọi giao dịch đều được ghi nhận theo Tracking ID.

---

# 22. Identity & Access Foundation Model

```text
Identity
        │
        ▼
User
        │
        ▼
Organization
        │
        ├── Portal
        ├── Storefront
        ├── Roles
        ├── Permissions
        ├── Policies
        └── Distribution Network
                │
                ▼
            Customer
                │
                ▼
       Support Governance
                │
                ▼
         Access Decision
```

---

# 23. Business Decisions (Locked)

## BD-03-001

Organization là Business Entity quản lý toàn bộ kênh bán hàng.

---

## BD-03-002

Organization Structure và Distribution Network là hai mô hình độc lập.

---

## BD-03-003

Portal và Storefront là hai thành phần độc lập.

---

## BD-03-004

Customer Portal là Storefront mở rộng.

---

## BD-03-005

Identity là Foundation Domain.

---

## BD-03-006

User và Customer là hai Business Entity độc lập.

---

## BD-03-007

Mỗi User chỉ thuộc một Organization.

---

## BD-03-008

Role thuộc Organization.

---

## BD-03-009

Permission được xác định theo:

Role + Resource Scope + Data Scope + Policy.

---

## BD-03-010

Customer Ownership được quản lý theo Distribution Network.

---

## BD-03-011

Support Governance được điều khiển bởi Support Policy.

Support Policy gồm:

- SELF_SUPPORT
- PARENT_SUPPORT
- HYBRID

---

## BD-03-012

Mọi dữ liệu nhạy cảm phải hỗ trợ Data Masking.

---

## BD-03-013

Mọi thao tác truy cập dữ liệu nhạy cảm phải được Audit.

---

# 24. Traceability

Workshop được xây dựng dựa trên:

- BRD Workshop 01
- BRD Workshop 02
- Kinh nghiệm triển khai YSim v1.0
- Mô hình White-label Commerce Platform
- Mô hình Multi-level Distribution

---

# 25. Workshop Status

**Status:** FROZEN

Workshop này là Foundation cho:

- Identity Domain
- Organization Domain
- User Domain
- Portal
- Storefront
- CRM
- Customer Support
- Permission Framework
- Notification
- Audit
- Security

---

# 26. Next Workshop

**BRD-WS-04 – Product Catalog, Supplier & Product Intelligence**