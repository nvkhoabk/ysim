---
document_code: "BRD-WS-16"
title: "Identity, Security, Authorization, Audit & Compliance"
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

# BRD Workshop 16

# Identity, Security, Authorization, Audit & Compliance

---

# 1. Workshop Objective

Workshop này xác định toàn bộ nền tảng Identity, Security, Authorization, Audit và Compliance của YSim.

Bao gồm:

- Identity Platform
- Authentication
- Multi-Factor Authentication (MFA)
- Authorization
- Role-Based Access Control (RBAC)
- Attribute-Based Access Control (ABAC)
- Permission Management
- Permission Evaluation Engine
- Session Management
- API Security
- Data Scope
- Field-Level Permission
- Data Masking
- Customer Consent
- Secret Management
- Encryption
- Key Management
- Audit Logging
- Security Policy
- Risk Management
- Privacy Protection
- Compliance
- Data Classification

Workshop này không bao gồm:

- Monitoring Platform
- Infrastructure Security
- Background Scheduler
- Platform Operation

(Các nội dung trên sẽ được triển khai trong Workshop tiếp theo.)

---

# 2. Business Objects Introduced

| Business Object | Type |
|-----------------|------|
| Identity Provider | Master |
| Authentication Method | Master |
| Authorization Policy | Master |
| Permission | Master |
| Permission Set | Master |
| Role Template | Master |
| Session | Transaction |
| API Key | Master |
| Access Token | Transaction |
| Refresh Token | Transaction |
| Secret | Master |
| Encryption Key | Master |
| Security Policy | Master |
| Data Masking Policy | Master |
| Compliance Policy | Master |
| Risk Rule | Master |
| Audit Log | Transaction |
| Data Classification | Master |

---

# 3. Identity Platform

Identity Platform hỗ trợ nhiều Identity Provider.

Bao gồm:

- Local Account
- Google
- Apple
- Facebook
- Microsoft
- Line
- WeChat

Kiến trúc được thiết kế mở để bổ sung thêm các Identity Provider khác trong tương lai.

Identity không phụ thuộc User.

Một Identity có thể được sử dụng cho:

- Customer
- Internal User
- Organization Owner
- API Client
- Service Account

Identity là thực thể trung tâm của toàn bộ nền tảng bảo mật.

---

# 4. Authentication

Authentication Platform hỗ trợ nhiều phương thức xác thực.

Bao gồm:

- Username / Password
- Email OTP
- SMS OTP
- Passkey
- OAuth2
- OpenID Connect (OIDC)
- SAML
- API Key

Authentication Method được cấu hình.

Không Hard-code.

Authentication có thể được bật hoặc tắt theo Security Policy.

---

# 5. Multi-Factor Authentication (MFA)

Platform hỗ trợ Multi-Factor Authentication.

Các phương thức MFA bao gồm:

- Email OTP
- SMS OTP
- Authenticator Application
- Passkey

MFA có thể được áp dụng theo:

- Platform
- Organization
- Role
- User
- API Client

MFA Policy được quản lý thông qua Security Policy.

---

# 6. Authorization Model

YSim sử dụng mô hình Authorization kết hợp.

Bao gồm:

- Role-Based Access Control (RBAC)
- Attribute-Based Access Control (ABAC)

Permission không được xác định chỉ dựa trên Role.

Permission được đánh giá động thông qua Permission Evaluation Engine.

Authorization phải hỗ trợ mở rộng để đáp ứng các mô hình phân quyền phức tạp trong tương lai.

---

# 7. Permission

Permission là Business Object.

Permission có thể được áp dụng cho:

- Menu
- Screen
- Business Object
- API
- Dashboard
- Report
- Action
- Field

Permission được quản lý tập trung.

Permission không được Hard-code trong mã nguồn.

---

# 8. Permission Scope

Permission hỗ trợ nhiều Scope.

Bao gồm:

- Platform
- Organization
- Department
- Team
- Storefront
- Customer Portal
- User

Permission Scope được cấu hình.

Kiến trúc hỗ trợ bổ sung thêm Scope mới trong tương lai.

---

# 9. Data Scope

Permission hỗ trợ Data Scope.

Ví dụ:

- Own Data
- Department Data
- Organization Data
- Parent Organization Data
- Global Data

Data Scope được kết hợp với:

- Organization Relationship
- Support Policy
- Capability
- Security Policy

Data Scope quyết định phạm vi dữ liệu mà người dùng được phép truy cập.

---

# 10. Field-Level Permission

Permission hỗ trợ phân quyền tới từng Field.

Mỗi Field có thể được cấu hình:

- Read
- Create
- Update
- Delete
- Hidden
- Masked

Ví dụ:

- Customer Email
- Customer Phone
- Supplier Cost
- Commission
- Payment Information

Field-Level Permission được đánh giá đồng thời với Data Scope và Permission.

Không được Hard-code.

---

# 11. Data Masking

Platform hỗ trợ Data Masking trên toàn hệ thống.

Các trường dữ liệu thường được Mask:

- Email
- Phone Number
- Passport Number
- QR Code
- Supplier Cost
- Payment Information

Data Masking được quyết định dựa trên:

- Permission
- Data Classification
- Customer Consent
- Security Policy

Masking có thể áp dụng trên:

- Portal
- API
- Report
- Export

------

# 12. Customer Consent

Customer Consent là cơ chế cho phép Customer kiểm soát việc chia sẻ dữ liệu cá nhân.

Customer có thể:

- Cho phép chia sẻ Email
- Cho phép chia sẻ Phone Number
- Cho phép chia sẻ QR Code
- Cho phép chia sẻ các thông tin khác theo từng mục đích
- Thu hồi quyền chia sẻ bất kỳ lúc nào

Customer Consent được áp dụng trong:

- Customer Support
- Ticket Processing
- Customer Portal
- API
- Third-party Integration

Consent được ghi nhận đầy đủ trong Audit Log.

---

# 13. Session Management

Session là Business Object.

Session quản lý:

- Login Time
- Logout Time
- Expiration Time
- Device
- Browser
- Operating System
- IP Address
- Location (nếu được phép)
- Authentication Method
- Session Status

Platform hỗ trợ Concurrent Login trên nhiều thiết bị.

Session Policy được cấu hình theo Security Policy.

---

# 14. API Security

API Security hỗ trợ nhiều cơ chế bảo mật.

Bao gồm:

- OAuth2
- JWT
- API Key
- HMAC Signature
- Digital Signature
- Mutual TLS (mở rộng)

API Security được áp dụng cho:

- Internal API
- Organization API
- Partner API
- Public API

API Security được quản lý độc lập với Portal Security.

---

# 15. Secret Management

Secret là Business Object.

Secret được sử dụng để quản lý:

- API Secret
- Client Secret
- Gateway Secret
- Webhook Secret
- Certificate Password
- Signing Secret

Secret được:

- Mã hóa
- Versioning
- Rotation
- Audit

Secret không được lưu dưới dạng Plain Text.

---

# 16. Encryption

Platform hỗ trợ:

- Encryption In Transit (TLS)

Kiến trúc được thiết kế mở để hỗ trợ:

- Encryption At Rest
- Database Encryption
- File Encryption

trong các phiên bản tiếp theo.

Thuật toán mã hóa và tiêu chuẩn truyền thông được cấu hình theo Security Policy.

---

# 17. Key Management

Encryption Key được quản lý tập trung.

Platform hỗ trợ:

- Key Generation
- Key Version
- Key Rotation
- Key Expiration
- Key Revocation

Key Rotation được cấu hình tự động hoặc thực hiện thủ công theo Security Policy.

Mọi thay đổi đều được ghi nhận trong Audit Log.

---

# 18. Audit Logging

Audit Log là Business Object.

Audit Log ghi nhận đầy đủ các hoạt động quan trọng.

Bao gồm:

- Login
- Logout
- Authentication Failure
- Permission Change
- Configuration Change
- API Access
- Payment
- Export
- Customer Support
- Data Modification
- Security Event

Audit Log chỉ được phép đọc.

Không được phép chỉnh sửa hoặc xóa trực tiếp.

---

# 19. Compliance

Platform hỗ trợ Compliance.

Phiên bản hiện tại hỗ trợ:

- GDPR

Kiến trúc được thiết kế mở để bổ sung:

- PDPA
- PCI DSS
- ISO 27001
- SOC 2

và các tiêu chuẩn khác trong tương lai.

Compliance Policy được cấu hình.

---

# 20. Privacy Protection

Customer có quyền bảo vệ dữ liệu cá nhân.

Bao gồm:

- Export dữ liệu cá nhân
- Xóa Identity theo chính sách
- Xóa Account theo chính sách
- Quản lý Customer Consent
- Quản lý Subscription

Privacy Protection tuân thủ Compliance Policy và Security Policy.

---

# 21. API Permission

API Permission được quản lý độc lập.

Portal Permission và API Permission không phụ thuộc lẫn nhau.

API Permission có thể đánh giá dựa trên:

- API Client
- API Key
- OAuth Scope
- Organization
- Permission
- Data Scope

API Permission được xử lý bởi Permission Evaluation Engine.

---

# 22. Organization Security Policy

Mỗi Organization có Security Policy riêng.

Organization Security Policy có thể cấu hình:

- Password Policy
- MFA Policy
- Session Timeout
- Allowed Country
- Allowed IP
- Allowed Identity Provider
- Allowed Authentication Method
- API Security Policy

Organization có thể Override các thiết lập được Platform cho phép.

Các Security Policy được kế thừa theo mô hình Organization Relationship nếu phù hợp.

------

# 23. Risk Rule

Risk Rule là Business Object.

Risk Rule được sử dụng để phát hiện các hành vi bất thường và giảm thiểu rủi ro bảo mật.

Ví dụ:

- Too Many Login Attempts
- Too Many Failed OTP
- Too Many Payment Attempts
- Suspicious Country
- Impossible Travel
- Suspicious Device
- Abnormal API Usage
- Excessive Export
- Unusual Data Access

Risk Rule được cấu hình.

Không Hard-code.

Risk Rule có thể Trigger:

- Notification
- Audit
- Account Lock
- MFA Challenge
- Security Review

---

# 24. Account Lock

Platform hỗ trợ Account Lock.

Version hiện tại hỗ trợ:

- Temporary Lock

Các điều kiện Lock được cấu hình thông qua Security Policy.

Ví dụ:

- Sai mật khẩu nhiều lần
- OTP thất bại nhiều lần
- Phát hiện hành vi bất thường

Account có thể được mở lại:

- Tự động sau thời gian quy định
- Bởi Administrator
- Sau khi Customer xác minh lại danh tính

Mọi thao tác Lock và Unlock đều được ghi nhận trong Audit Log.

---

# 25. Audit Retention

Audit Log được lưu trực tuyến trong:

**03 tháng**

Sau thời gian này:

- Audit được Archive
- Archive chỉ đọc
- Không được chỉnh sửa
- Không được xóa trực tiếp

Audit Archive phục vụ:

- Điều tra sự cố
- Đối soát
- Compliance
- Kiểm toán

Chính sách lưu trữ có thể được cấu hình theo Compliance Policy.

---

# 26. Permission Evaluation Engine

Permission Evaluation Engine là thành phần trung tâm của Security Platform.

Engine đánh giá Permission dựa trên:

- RBAC
- ABAC
- Organization Relationship
- Organization Capability
- Permission Scope
- Data Scope
- Support Policy
- Customer Consent
- Data Classification
- Security Policy

Kết quả cuối cùng là:

**Effective Permission**

Business Domain không tự tính Permission.

Mọi đánh giá Permission đều phải đi qua Permission Evaluation Engine.

---

# 27. Security Policy

Security Policy là Business Object.

Security Policy quản lý:

- Password Policy
- Authentication Policy
- MFA Policy
- Session Policy
- API Security Policy
- Device Policy
- IP Policy
- Risk Policy
- Lock Policy

Security Policy hỗ trợ:

- Version
- Effective Date
- Approval
- Audit

Security Policy không được Hard-code.

---

# 28. Identity Federation

Identity Platform hỗ trợ Federation.

Ví dụ:

- Azure Active Directory
- Google Workspace
- Microsoft Entra ID
- Enterprise Identity Provider
- SAML Identity Provider

Identity Federation cho phép Organization sử dụng hệ thống Identity hiện có mà không cần tạo lại User trên YSim.

Federation được cấu hình thông qua Identity Provider.

---

# 29. Security Business Events

Security Platform Publish Business Event.

Ví dụ:

- LoginSucceeded
- LoginFailed
- LogoutSucceeded
- PasswordChanged
- MFAEnabled
- MFADisabled
- PermissionChanged
- SessionExpired
- AccountLocked
- AccountUnlocked
- ConsentUpdated
- SecurityPolicyChanged

Các Security Event được sử dụng bởi:

- Notification Platform
- Analytics
- Monitoring
- Audit
- Risk Engine

Security Domain cũng có thể Subscribe Business Event từ các Domain khác để đánh giá Risk.

---

# 30. Data Classification

Data Classification là Business Object.

Platform hỗ trợ các mức phân loại dữ liệu:

- Public
- Internal
- Confidential
- Restricted

Ví dụ:

| Data | Classification |
|------|----------------|
| Product Name | Public |
| Product Description | Public |
| Customer Email | Confidential |
| Customer Phone | Confidential |
| Passport Number | Restricted |
| Supplier Cost | Restricted |
| Payment Information | Restricted |
| Encryption Key | Restricted |

Data Classification được sử dụng để quyết định:

- Permission
- Data Scope
- Field-Level Permission
- Data Masking
- API Access
- Export
- Audit
- Backup
- Customer Consent

Data Classification có thể được cấu hình và mở rộng theo Business Requirement.

------

# 31. Business Decisions (Locked)

## BD-16-001

Identity Platform hỗ trợ nhiều Identity Provider.

Bao gồm:

- Local Account
- Google
- Apple
- Facebook
- Microsoft
- Line
- WeChat

Kiến trúc hỗ trợ mở rộng thêm Identity Provider trong tương lai.

---

## BD-16-002

Authentication hỗ trợ:

- Password
- Email OTP
- SMS OTP
- Passkey
- OAuth2
- OpenID Connect (OIDC)
- SAML
- API Key

Authentication Method được cấu hình.

---

## BD-16-003

Platform hỗ trợ Multi-Factor Authentication (MFA).

MFA có thể áp dụng theo:

- Platform
- Organization
- Role
- User
- API Client

---

## BD-16-004

Authorization sử dụng mô hình kết hợp:

- RBAC
- ABAC

Permission được đánh giá động.

---

## BD-16-005

Permission là Business Object.

Permission không được Hard-code.

---

## BD-16-006

Permission hỗ trợ Scope linh hoạt.

Bao gồm:

- Platform
- Organization
- Department
- Team
- Storefront
- Customer Portal
- User

---

## BD-16-007

Permission hỗ trợ Data Scope.

Data Scope được kết hợp với:

- Organization Relationship
- Support Policy
- Capability
- Security Policy

---

## BD-16-008

Platform hỗ trợ Field-Level Permission.

Permission có thể áp dụng tới từng Field.

---

## BD-16-009

Platform hỗ trợ Data Masking.

Masking được quyết định bởi:

- Permission
- Data Classification
- Customer Consent
- Security Policy

---

## BD-16-010

Platform hỗ trợ Customer Consent.

Customer có quyền:

- Chia sẻ
- Thu hồi
- Quản lý dữ liệu cá nhân

---

## BD-16-011

Session là Business Object.

Platform hỗ trợ Concurrent Login trên nhiều thiết bị.

---

## BD-16-012

API Security hỗ trợ nhiều phương thức.

Bao gồm:

- OAuth2
- JWT
- API Key
- HMAC
- Digital Signature

---

## BD-16-013

Secret là Business Object.

Secret được quản lý tập trung.

---

## BD-16-014

Platform hỗ trợ Encryption In Transit.

Kiến trúc mở để hỗ trợ Encryption At Rest trong các phiên bản tiếp theo.

---

## BD-16-015

Platform hỗ trợ Key Rotation.

Key Management được quản lý tập trung.

---

## BD-16-016

Audit Log là Business Object.

Audit ghi nhận đầy đủ các Security Event và Business Event quan trọng.

---

## BD-16-017

Platform hỗ trợ Compliance.

Phiên bản hiện tại hỗ trợ:

- GDPR

---

## BD-16-018

Customer có quyền bảo vệ dữ liệu cá nhân.

Bao gồm:

- Export Data
- Delete Identity
- Customer Consent

---

## BD-16-019

API Permission được quản lý độc lập với Portal Permission.

---

## BD-16-020

Mỗi Organization có Security Policy riêng.

Organization có thể Override theo Capability được cấp.

---

## BD-16-021

Risk Rule là Business Object.

Risk Rule được cấu hình.

Không Hard-code.

---

## BD-16-022

Platform hỗ trợ Temporary Account Lock.

---

## BD-16-023

Audit Log được lưu trực tuyến 03 tháng.

Sau đó được Archive.

---

## BD-16-024

Permission Evaluation Engine là thành phần trung tâm của Security Platform.

Business Domain không tự đánh giá Permission.

---

## BD-16-025

Security Policy là Business Object.

Security Policy hỗ trợ:

- Version
- Effective Date
- Approval
- Audit

---

## BD-16-026

Identity Platform hỗ trợ Federation.

---

## BD-16-027

Security Platform Publish Business Event.

---

## BD-16-028

Data Classification là Business Object.

---

## BD-16-029

Platform áp dụng Zero Trust Principle.

---

## BD-16-030

Toàn bộ truy cập dữ liệu phải được đánh giá động thông qua Permission Evaluation Engine và Security Policy.

---

# 32. Enterprise Design Principles

## EP-16-001

Identity không phụ thuộc User.

Một Identity có thể được sử dụng cho:

- Customer
- User
- Organization Owner
- API Client
- Service Account

---

## EP-16-002

Permission được đánh giá động.

Không sử dụng Permission tĩnh.

---

## EP-16-003

Permission Evaluation Engine là điểm đánh giá Permission duy nhất.

Business Domain không tự xử lý Permission.

---

## EP-16-004

Security Policy được cấu hình.

Không Hard-code.

---

## EP-16-005

Platform áp dụng Zero Trust Principle.

Không có Request nào được mặc định tin cậy.

---

## EP-16-006

Data Protection được quyết định bởi:

- Permission
- Data Scope
- Data Classification
- Customer Consent
- Security Policy

---

## EP-16-007

API Security độc lập với Portal Security.

---

## EP-16-008

Security Platform Publish Business Event.

---

## EP-16-009

Identity Platform hỗ trợ Federation.

---

## EP-16-010

Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên:

- Identity
- Role
- Permission
- Data Scope
- Organization Relationship
- Support Policy
- Customer Consent
- Data Classification
- Security Policy

---

# 33. Published Business Events

Ví dụ:

- LoginSucceeded
- LoginFailed
- LogoutSucceeded
- PasswordChanged
- MFAEnabled
- MFADisabled
- PermissionChanged
- SessionExpired
- AccountLocked
- AccountUnlocked
- ConsentUpdated
- SecurityPolicyChanged

---

# 34. Consumed Business Events

Ví dụ:

- OrganizationCreated
- UserCreated
- CustomerCreated
- ConfigurationPublished
- APIAccessRequested
- TicketCreated
- PaymentSucceeded
- RiskAlertRaised

---

# 35. Business Capabilities Covered

Workshop này bao gồm các Business Capability:

- Identity Management
- Authentication
- Authorization
- Permission Management
- Permission Evaluation Engine
- Session Management
- API Security
- Secret Management
- Key Management
- Security Policy Management
- Data Masking
- Customer Consent
- Data Classification
- Compliance Management
- Privacy Protection
- Audit Logging
- Risk Management
- Identity Federation

---

# 36. Traceability

Workshop này kế thừa toàn bộ các quyết định từ:

- BRD-WS-01 → BRD-WS-15

WS-16 cung cấp Enterprise Security Foundation cho toàn bộ nền tảng YSim.

---

# 37. Impacts to Other Domains

Workshop này ảnh hưởng trực tiếp tới:

- Organization
- Customer
- User
- Identity
- Order
- Payment
- Inventory
- Fulfillment
- Settlement
- Communication
- Customer Success
- Reporting
- Analytics
- Integration Platform
- Configuration Platform
- Monitoring Platform

Mọi Business Domain đều sử dụng Security Platform làm nền tảng xác thực, phân quyền và bảo vệ dữ liệu.

---

# 38. Workshop Status

Status:

**FROZEN**

Workshop này xác định toàn bộ Enterprise Security Foundation của YSim.

---

# 39. Next Workshop

**BRD-WS-17**

**Platform Operations, Monitoring, Scheduler & Background Processing**

Workshop tiếp theo sẽ xác định toàn bộ nền tảng vận hành của YSim, bao gồm:

- Platform Operations Center
- Monitoring
- Health Check
- Metrics
- Alerting
- Scheduler
- Background Jobs
- Worker Management
- Queue Operations
- Distributed Task Processing
- Operational Dashboard
- Operational Policy
- Maintenance Mode
- Backup & Restore
- Disaster Recovery
- Performance & Capacity Management

WS-17 sẽ hoàn thiện lớp **Enterprise Operations Foundation**, khép lại nhóm Platform Foundation của YSim.

---

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-001 — Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Fa…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-001-AC001",
      "given": "the applicable business context, actor, and input for Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Fa…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-001-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-001-AC002",
      "given": "the applicable business context, actor, and input for Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Fa…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-001-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-001-AC003",
      "given": "the applicable business context, actor, and input for Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Fa…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-001-O003"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-001-AC004",
      "given": "the applicable business context, actor, and input for Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Fa…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-001-O004"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-001-AC005",
      "given": "the applicable business context, actor, and input for Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Fa…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-001-O005"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-001-AC006",
      "given": "the applicable business context, actor, and input for Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Fa…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-001-O006"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-001-AC007",
      "given": "the applicable business context, actor, and input for Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Fa…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-001-O007"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-16-001-AC008",
      "given": "an unsupported or invalid business input at the boundary governed by Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Fa…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-16-001-O001",
        "BD-16-001-O002",
        "BD-16-001-O003",
        "BD-16-001-O004",
        "BD-16-001-O005",
        "BD-16-001-O006",
        "BD-16-001-O007"
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
        "BD-16-001-AC001",
        "BD-16-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-001-O001",
      "obligation_text": "Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: Local Account."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-001-AC002",
        "BD-16-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-001-O002",
      "obligation_text": "Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: Google."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-001-AC003",
        "BD-16-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-001-O003",
      "obligation_text": "Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: Apple."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-001-AC004",
        "BD-16-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-001-O004",
      "obligation_text": "Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: Facebook."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-001-AC005",
        "BD-16-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-001-O005",
      "obligation_text": "Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: Microsoft."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-001-AC006",
        "BD-16-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-001-O006",
      "obligation_text": "Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: Line."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-001-AC007",
        "BD-16-001-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-001-O007",
      "obligation_text": "Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: WeChat Kiến trúc hỗ trợ mở rộng thêm Identity Provider trong tương lai."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-16-001 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-001 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-001 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-16-001 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-001-AC001",
        "BD-16-001-AC002",
        "BD-16-001-AC003",
        "BD-16-001-AC004",
        "BD-16-001-AC005",
        "BD-16-001-AC006",
        "BD-16-001-AC007"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-001 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Facebook - Microsoft - Line - WeChat Kiến trúc hỗ trợ mở rộng thêm Identity Provider trong tương lai.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007",
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Identity Platform",
    "source_context_sha256": "ca12b94f6cb8f68e320a33d7aac6af2a3ebdccbb25d4606c21fddb218b322bd9",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "0541d21d79f5ae0be70c2a668f13d7eb511d72a99e9edfd6d5f6c4524a68ff4f",
    "source_lines": "L760-L775",
    "source_section": "31. Business Decisions (Locked) > BD-16-001"
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
  "stable_id": "BD-16-001",
  "title": "Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Fa…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-002 — Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OID…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-002-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OID…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-002-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-002-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OID…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-002-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-002-AC003",
      "given": "an identified principal, applicable assurance context, and policy inputs for Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OID…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-002-O003"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-002-AC004",
      "given": "an identified principal, applicable assurance context, and policy inputs for Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OID…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-002-O004"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-002-AC005",
      "given": "an identified principal, applicable assurance context, and policy inputs for Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OID…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-002-O005"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-002-AC006",
      "given": "an identified principal, applicable assurance context, and policy inputs for Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OID…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-002-O006"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-002-AC007",
      "given": "an identified principal, applicable assurance context, and policy inputs for Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OID…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-002-O007"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-002-AC008",
      "given": "an identified principal, applicable assurance context, and policy inputs for Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OID…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-002-O008"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-002-AC009",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OID…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-002-O001",
        "BD-16-002-O002",
        "BD-16-002-O003",
        "BD-16-002-O004",
        "BD-16-002-O005",
        "BD-16-002-O006",
        "BD-16-002-O007",
        "BD-16-002-O008"
      ],
      "when": "the protected decision or action is attempted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC001",
        "BD-16-002-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O001",
      "obligation_text": "Authentication hỗ trợ: Password."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC002",
        "BD-16-002-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O002",
      "obligation_text": "Authentication hỗ trợ: Email OTP."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC003",
        "BD-16-002-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O003",
      "obligation_text": "Authentication hỗ trợ: SMS OTP."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC004",
        "BD-16-002-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O004",
      "obligation_text": "Authentication hỗ trợ: Passkey."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC005",
        "BD-16-002-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O005",
      "obligation_text": "Authentication hỗ trợ: OAuth2."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC006",
        "BD-16-002-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O006",
      "obligation_text": "Authentication hỗ trợ: OpenID Connect (OIDC)."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC007",
        "BD-16-002-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O007",
      "obligation_text": "Authentication hỗ trợ: SAML."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC008",
        "BD-16-002-AC009"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O008",
      "obligation_text": "Authentication hỗ trợ: API Key Authentication Method được cấu hình."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-16-002 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-16-002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-002-AC001",
        "BD-16-002-AC002",
        "BD-16-002-AC003",
        "BD-16-002-AC004",
        "BD-16-002-AC005",
        "BD-16-002-AC006",
        "BD-16-002-AC007",
        "BD-16-002-AC008"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OIDC) - SAML - API Key Authentication Method được cấu hình.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-001"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-002",
    "source_context_sha256": "c7422183c3559649b1fafb9ef6478efd48c507553b2c8715ea2627ad181b20c2",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "0d5756f398fbf3bb56ce2db9c4ab16aaea6d48dbe8cbc1a81543e12d3f554ea3",
    "source_lines": "L778-L792",
    "source_section": "31. Business Decisions (Locked) > BD-16-002"
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
  "stable_id": "BD-16-002",
  "title": "Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OID…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-003 — Platform hỗ trợ Multi-Factor Authentication (MFA). MFA có thể áp dụng theo: - Platform - Organiz…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "MFA_SCOPE_ENFORCEMENT_V1",
      "criterion_id": "BD-16-003-AC001",
      "given": "an MFA policy configured at Platform scope",
      "observable_evidence": "Platform policy, principal scope binding, effective-policy trace, and challenge result",
      "then": "the effective policy includes the scope-specific MFA requirement and presents the required challenge",
      "verifies": [
        "BD-16-003-O001"
      ],
      "when": "a principal governed by that scope attempts an action requiring MFA"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "MFA_SCOPE_ENFORCEMENT_V1",
      "criterion_id": "BD-16-003-AC002",
      "given": "an MFA policy configured at Organization scope",
      "observable_evidence": "Organization policy, principal scope binding, effective-policy trace, and challenge result",
      "then": "the effective policy includes the scope-specific MFA requirement and presents the required challenge",
      "verifies": [
        "BD-16-003-O002"
      ],
      "when": "a principal governed by that scope attempts an action requiring MFA"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "MFA_SCOPE_ENFORCEMENT_V1",
      "criterion_id": "BD-16-003-AC003",
      "given": "an MFA policy configured at Role scope",
      "observable_evidence": "Role policy, principal scope binding, effective-policy trace, and challenge result",
      "then": "the effective policy includes the scope-specific MFA requirement and presents the required challenge",
      "verifies": [
        "BD-16-003-O003"
      ],
      "when": "a principal governed by that scope attempts an action requiring MFA"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "MFA_SCOPE_ENFORCEMENT_V1",
      "criterion_id": "BD-16-003-AC004",
      "given": "an MFA policy configured at User scope",
      "observable_evidence": "User policy, principal scope binding, effective-policy trace, and challenge result",
      "then": "the effective policy includes the scope-specific MFA requirement and presents the required challenge",
      "verifies": [
        "BD-16-003-O004"
      ],
      "when": "a principal governed by that scope attempts an action requiring MFA"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "MFA_SCOPE_ENFORCEMENT_V1",
      "criterion_id": "BD-16-003-AC005",
      "given": "an MFA policy configured at API Client scope",
      "observable_evidence": "API Client policy, principal scope binding, effective-policy trace, and challenge result",
      "then": "the effective policy includes the scope-specific MFA requirement and presents the required challenge",
      "verifies": [
        "BD-16-003-O005"
      ],
      "when": "a principal governed by that scope attempts an action requiring MFA"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "MFA_EFFECTIVE_POLICY_RESOLUTION_V1",
      "criterion_id": "BD-16-003-AC006",
      "given": "overlapping MFA policies at more than one applicable scope",
      "observable_evidence": "all applicable policies, precedence or composition result, effective policy, and challenge",
      "then": "the effective-policy result identifies each contributing scope and the challenge that must be satisfied",
      "verifies": [
        "BD-16-003-O006"
      ],
      "when": "effective MFA policy is resolved"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "MFA_BYPASS_DENIAL_V1",
      "criterion_id": "BD-16-003-AC007",
      "given": "a principal that has not satisfied a required MFA challenge",
      "observable_evidence": "challenge status, denial result, protected-state comparison, reason, and audit record",
      "then": "the protected action is denied, protected state remains unchanged, and the bypass attempt is audited",
      "verifies": [
        "BD-16-003-O007"
      ],
      "when": "the principal attempts to bypass the challenge"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-16-003-AC008",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Platform hỗ trợ Multi-Factor Authentication (MFA). MFA có thể áp dụng theo: - Platform - Organiz…",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-16-003-O001",
        "BD-16-003-O002",
        "BD-16-003-O003",
        "BD-16-003-O004",
        "BD-16-003-O005",
        "BD-16-003-O006",
        "BD-16-003-O007"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-003-AC001",
        "BD-16-003-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-003-O001",
      "obligation_text": "MFA policy is independently configurable and enforceable at Platform scope."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-003-AC002",
        "BD-16-003-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-003-O002",
      "obligation_text": "MFA policy is independently configurable and enforceable at Organization scope."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-003-AC003",
        "BD-16-003-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-003-O003",
      "obligation_text": "MFA policy is independently configurable and enforceable at Role scope."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-003-AC004",
        "BD-16-003-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-003-O004",
      "obligation_text": "MFA policy is independently configurable and enforceable at User scope."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-003-AC005",
        "BD-16-003-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-003-O005",
      "obligation_text": "MFA policy is independently configurable and enforceable at API Client scope."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-003-AC006",
        "BD-16-003-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-003-O006",
      "obligation_text": "Effective MFA policy resolution produces the required MFA challenge for the applicable principal and scope."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-003-AC007",
        "BD-16-003-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-003-O007",
      "obligation_text": "An attempted bypass of a required MFA challenge is denied and audited."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-16-003-AC008"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-16-003 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-003-AC001",
        "BD-16-003-AC002",
        "BD-16-003-AC003",
        "BD-16-003-AC004",
        "BD-16-003-AC005",
        "BD-16-003-AC006"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Multi-Factor Authentication (MFA). MFA có thể áp dụng theo: - Platform - Organization - Role - User - API Client",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-003",
    "source_context_sha256": "0a54eea37a289d34ddab77fc2503b323ed462f6daad1ef94e15a8c422258a2b5",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "b52f2437882642c2d7180f802cc18f6bd19a636ea242296d2404594b8aae2cc0",
    "source_lines": "L795-L806",
    "source_section": "31. Business Decisions (Locked) > BD-16-003"
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
  "stable_id": "BD-16-003",
  "title": "Platform hỗ trợ Multi-Factor Authentication (MFA). MFA có thể áp dụng theo: - Platform - Organiz…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-004 — Authorization sử dụng mô hình kết hợp: - RBAC - ABAC Permission được đánh giá động

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-004-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Authorization sử dụng mô hình kết hợp: - RBAC - ABAC Permission được đánh giá động",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-004-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-004-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Authorization sử dụng mô hình kết hợp: - RBAC - ABAC Permission được đánh giá động",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the permission decision is recalculated from the current applicable attributes and policy; changing a governing input changes the effective decision without relying on a stored static permission result",
      "verifies": [
        "BD-16-004-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-004-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Authorization sử dụng mô hình kết hợp: - RBAC - ABAC Permission được đánh giá động",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-004-O001",
        "BD-16-004-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-004-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Authorization sử dụng mô hình kết hợp: - RBAC - ABAC Permission được đánh giá động",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-004-O001",
        "BD-16-004-O002"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-16-004-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Authorization sử dụng mô hình kết hợp: - RBAC - ABAC Permission được đánh giá động",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-16-004-O001",
        "BD-16-004-O002"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-004-AC001",
        "BD-16-004-AC003",
        "BD-16-004-AC004",
        "BD-16-004-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-004-O001",
      "obligation_text": "Authorization sử dụng mô hình kết hợp: RBAC."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-004-AC002",
        "BD-16-004-AC003",
        "BD-16-004-AC004",
        "BD-16-004-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-004-O002",
      "obligation_text": "Authorization sử dụng mô hình kết hợp: ABAC Permission được đánh giá động."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-16-004-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-004-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-004-AC001",
        "BD-16-004-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Authorization sử dụng mô hình kết hợp: - RBAC - ABAC Permission được đánh giá động.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-004",
    "source_context_sha256": "77b0cfa84c4e704817978bcecffba11c5727d8c5573504da4749ba48cd521894",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "a3ae0f5f93cc58b150b25cef69034dd002e76820d1803c2f1703d2681afb6a74",
    "source_lines": "L809-L817",
    "source_section": "31. Business Decisions (Locked) > BD-16-004"
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
  "stable_id": "BD-16-004",
  "title": "Authorization sử dụng mô hình kết hợp: - RBAC - ABAC Permission được đánh giá động",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-005 — Permission là Business Object. Permission không được Hard-code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-005-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission là Business Object. Permission không được Hard-code",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-005-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-005-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission là Business Object. Permission không được Hard-code",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the prohibited security decision path produces no effective permission or protected-state change, and conformance evidence identifies the attempted bypass",
      "verifies": [
        "BD-16-005-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-005-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Permission là Business Object. Permission không được Hard-code",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-005-O001",
        "BD-16-005-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-005-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Permission là Business Object. Permission không được Hard-code",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-005-O001",
        "BD-16-005-O002"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-16-005-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Permission là Business Object. Permission không được Hard-code",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-16-005-O001",
        "BD-16-005-O002"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-005-AC001",
        "BD-16-005-AC003",
        "BD-16-005-AC004",
        "BD-16-005-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-005-O001",
      "obligation_text": "Permission là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-005-AC002",
        "BD-16-005-AC003",
        "BD-16-005-AC004",
        "BD-16-005-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-005-O002",
      "obligation_text": "Permission không được Hard-code"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-16-005-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-005-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-005-AC001",
        "BD-16-005-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission là Business Object. Permission không được Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Permission",
    "source_context_sha256": "3d3ab73af16e4a1750956c224ac2159a10ec60b5d687a57e6587480e9b2681d8",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "3e3ad30f1410bae22e5de732edcc3d0ab4dadfb199ff07ede0dc8bad03f965e9",
    "source_lines": "L820-L825",
    "source_section": "31. Business Decisions (Locked) > BD-16-005"
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
  "stable_id": "BD-16-005",
  "title": "Permission là Business Object. Permission không được Hard-code",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-006 — Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-006-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-006-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-006-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-006-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-006-AC003",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-006-O003"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-006-AC004",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-006-O004"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-006-AC005",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-006-O005"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-006-AC006",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-006-O006"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-006-AC007",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-006-O007"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-006-AC008",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-006-O001",
        "BD-16-006-O002",
        "BD-16-006-O003",
        "BD-16-006-O004",
        "BD-16-006-O005",
        "BD-16-006-O006",
        "BD-16-006-O007"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-006-AC009",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-006-O001",
        "BD-16-006-O002",
        "BD-16-006-O003",
        "BD-16-006-O004",
        "BD-16-006-O005",
        "BD-16-006-O006",
        "BD-16-006-O007"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-16-006-AC010",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-16-006-O001",
        "BD-16-006-O002",
        "BD-16-006-O003",
        "BD-16-006-O004",
        "BD-16-006-O005",
        "BD-16-006-O006",
        "BD-16-006-O007"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-006-AC001",
        "BD-16-006-AC008",
        "BD-16-006-AC009",
        "BD-16-006-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-006-O001",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Platform."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-006-AC002",
        "BD-16-006-AC008",
        "BD-16-006-AC009",
        "BD-16-006-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-006-O002",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Organization."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-006-AC003",
        "BD-16-006-AC008",
        "BD-16-006-AC009",
        "BD-16-006-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-006-O003",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Department."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-006-AC004",
        "BD-16-006-AC008",
        "BD-16-006-AC009",
        "BD-16-006-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-006-O004",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Team."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-006-AC005",
        "BD-16-006-AC008",
        "BD-16-006-AC009",
        "BD-16-006-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-006-O005",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Storefront."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-006-AC006",
        "BD-16-006-AC008",
        "BD-16-006-AC009",
        "BD-16-006-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-006-O006",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Customer Portal."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-006-AC007",
        "BD-16-006-AC008",
        "BD-16-006-AC009",
        "BD-16-006-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-006-O007",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt. Bao gồm: User."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-16-006-AC010"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-006-AC009"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-006-AC001",
        "BD-16-006-AC002",
        "BD-16-006-AC003",
        "BD-16-006-AC004",
        "BD-16-006-AC005",
        "BD-16-006-AC006",
        "BD-16-006-AC007"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Storefront - Customer Portal - User",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-006",
    "source_context_sha256": "f07eaa73f91bac65267fd0ce84085c9976ac9a47f2daf786e9d6b4f500317bb7",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "d0598fbf0bc728157230ccd378cda70e59a8ae6da7ee1d559feae44154c28d36",
    "source_lines": "L828-L841",
    "source_section": "31. Business Decisions (Locked) > BD-16-006"
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
  "stable_id": "BD-16-006",
  "title": "Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-007 — Permission hỗ trợ Data Scope. Data Scope được kết hợp với: - Organization Relationship - Support…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-007-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission hỗ trợ Data Scope. Data Scope được kết hợp với: - Organization Relationship - Support…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-007-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-007-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission hỗ trợ Data Scope. Data Scope được kết hợp với: - Organization Relationship - Support…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-007-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-007-AC003",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission hỗ trợ Data Scope. Data Scope được kết hợp với: - Organization Relationship - Support…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-007-O003"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-007-AC004",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission hỗ trợ Data Scope. Data Scope được kết hợp với: - Organization Relationship - Support…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-007-O004"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-007-AC005",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Permission hỗ trợ Data Scope. Data Scope được kết hợp với: - Organization Relationship - Support…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-007-O001",
        "BD-16-007-O002",
        "BD-16-007-O003",
        "BD-16-007-O004"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-007-AC006",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Permission hỗ trợ Data Scope. Data Scope được kết hợp với: - Organization Relationship - Support…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-007-O001",
        "BD-16-007-O002",
        "BD-16-007-O003",
        "BD-16-007-O004"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-16-007-AC007",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Permission hỗ trợ Data Scope. Data Scope được kết hợp với: - Organization Relationship - Support…",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-16-007-O001",
        "BD-16-007-O002",
        "BD-16-007-O003",
        "BD-16-007-O004"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-007-AC001",
        "BD-16-007-AC005",
        "BD-16-007-AC006",
        "BD-16-007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-007-O001",
      "obligation_text": "Permission hỗ trợ Data Scope. Data Scope được kết hợp với: Organization Relationship."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-007-AC002",
        "BD-16-007-AC005",
        "BD-16-007-AC006",
        "BD-16-007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-007-O002",
      "obligation_text": "Permission hỗ trợ Data Scope. Data Scope được kết hợp với: Support Policy."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-007-AC003",
        "BD-16-007-AC005",
        "BD-16-007-AC006",
        "BD-16-007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-007-O003",
      "obligation_text": "Permission hỗ trợ Data Scope. Data Scope được kết hợp với: Capability."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-007-AC004",
        "BD-16-007-AC005",
        "BD-16-007-AC006",
        "BD-16-007-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-007-O004",
      "obligation_text": "Permission hỗ trợ Data Scope. Data Scope được kết hợp với: Security Policy."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-16-007-AC007"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-007-AC006"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-007-AC001",
        "BD-16-007-AC002",
        "BD-16-007-AC003",
        "BD-16-007-AC004"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission hỗ trợ Data Scope. Data Scope được kết hợp với: - Organization Relationship - Support Policy - Capability - Security Policy",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Data Scope",
    "source_context_sha256": "4b2004f50daa2484c322d511931bca319413f4723993aec4d160ef434e758070",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "5c2f7c89868cbae6ddbd35933323529d703b66279274de6e683a8bcd651aacac",
    "source_lines": "L844-L854",
    "source_section": "31. Business Decisions (Locked) > BD-16-007"
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
  "stable_id": "BD-16-007",
  "title": "Permission hỗ trợ Data Scope. Data Scope được kết hợp với: - Organization Relationship - Support…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-008 — Platform hỗ trợ Field-Level Permission. Permission có thể áp dụng tới từng Field

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-008-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Platform hỗ trợ Field-Level Permission. Permission có thể áp dụng tới từng Field",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-008-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-008-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Platform hỗ trợ Field-Level Permission. Permission có thể áp dụng tới từng Field",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-008-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-008-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Platform hỗ trợ Field-Level Permission. Permission có thể áp dụng tới từng Field",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-008-O001",
        "BD-16-008-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-008-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Platform hỗ trợ Field-Level Permission. Permission có thể áp dụng tới từng Field",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-008-O001",
        "BD-16-008-O002"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-16-008-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Platform hỗ trợ Field-Level Permission. Permission có thể áp dụng tới từng Field",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-16-008-O001",
        "BD-16-008-O002"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-008-AC001",
        "BD-16-008-AC003",
        "BD-16-008-AC004",
        "BD-16-008-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-008-O001",
      "obligation_text": "Platform hỗ trợ Field-Level Permission"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-008-AC002",
        "BD-16-008-AC003",
        "BD-16-008-AC004",
        "BD-16-008-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-008-O002",
      "obligation_text": "Permission có thể áp dụng tới từng Field"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-16-008-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-008 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-008 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-008-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-008-AC001",
        "BD-16-008-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-008 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Field-Level Permission. Permission có thể áp dụng tới từng Field.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-008",
    "source_context_sha256": "018f48b603c70d674c802a1602932809734d6ed76b3b4f99acdef16fdb3c3698",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "7b674720c5203c2205b49e6ef56b3bcd4b44307d0d922889129e2d3a80a87d67",
    "source_lines": "L857-L862",
    "source_section": "31. Business Decisions (Locked) > BD-16-008"
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
  "stable_id": "BD-16-008",
  "title": "Platform hỗ trợ Field-Level Permission. Permission có thể áp dụng tới từng Field",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-009 — Platform hỗ trợ Data Masking. Masking được quyết định bởi: - Permission - Data Classification - …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BD-16-009-AC001",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Platform hỗ trợ Data Masking. Masking được quyết định bởi: - Permission - Data Classification - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BD-16-009-O001"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BD-16-009-AC002",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Platform hỗ trợ Data Masking. Masking được quyết định bởi: - Permission - Data Classification - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BD-16-009-O002"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BD-16-009-AC003",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Platform hỗ trợ Data Masking. Masking được quyết định bởi: - Permission - Data Classification - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BD-16-009-O003"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BD-16-009-AC004",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Platform hỗ trợ Data Masking. Masking được quyết định bởi: - Permission - Data Classification - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BD-16-009-O004"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "PRIVACY_POLICY_DENIAL_V1",
      "criterion_id": "BD-16-009-AC005",
      "given": "a data action whose purpose, consent, scope, or effective policy does not permit the requested data use under Platform hỗ trợ Data Masking. Masking được quyết định bởi: - Permission - Data Classification - …",
      "observable_evidence": "actor, purpose, consent and scope, effective policies, denial reason, exposed-data comparison, and audit record",
      "then": "the data action is denied, no additional protected data is exposed or changed, and the policy reason is audited",
      "verifies": [
        "BD-16-009-O001",
        "BD-16-009-O002",
        "BD-16-009-O003",
        "BD-16-009-O004"
      ],
      "when": "privacy conformance is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-009-AC006",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Platform hỗ trợ Data Masking. Masking được quyết định bởi: - Permission - Data Classification - …",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-009-O001",
        "BD-16-009-O002",
        "BD-16-009-O003",
        "BD-16-009-O004"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-16-009-AC007",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Platform hỗ trợ Data Masking. Masking được quyết định bởi: - Permission - Data Classification - …",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-16-009-O001",
        "BD-16-009-O002",
        "BD-16-009-O003",
        "BD-16-009-O004"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-009-AC001",
        "BD-16-009-AC005",
        "BD-16-009-AC006",
        "BD-16-009-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-009-O001",
      "obligation_text": "Platform hỗ trợ Data Masking. Masking được quyết định bởi: Permission."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-009-AC002",
        "BD-16-009-AC005",
        "BD-16-009-AC006",
        "BD-16-009-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-009-O002",
      "obligation_text": "Platform hỗ trợ Data Masking. Masking được quyết định bởi: Data Classification."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-009-AC003",
        "BD-16-009-AC005",
        "BD-16-009-AC006",
        "BD-16-009-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-009-O003",
      "obligation_text": "Platform hỗ trợ Data Masking. Masking được quyết định bởi: Customer Consent."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-009-AC004",
        "BD-16-009-AC005",
        "BD-16-009-AC006",
        "BD-16-009-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-009-O004",
      "obligation_text": "Platform hỗ trợ Data Masking. Masking được quyết định bởi: Security Policy."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-16-009-AC007"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-009 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-009 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-009-AC006"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-009-AC001",
        "BD-16-009-AC002",
        "BD-16-009-AC003",
        "BD-16-009-AC004"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-009 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Data Masking. Masking được quyết định bởi: - Permission - Data Classification - Customer Consent - Security Policy",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-009",
    "source_context_sha256": "d3365a8f0319771be2084e215e4a5f6759694252ab2d77ee5b3dd2e0c50e1800",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "b8be7484a684c4f9a4d2c79dbfe69716d08df2cc09b6c2380608b9b318f1230f",
    "source_lines": "L865-L875",
    "source_section": "31. Business Decisions (Locked) > BD-16-009"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-16-009",
  "title": "Platform hỗ trợ Data Masking. Masking được quyết định bởi: - Permission - Data Classification - …",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-010 — Platform hỗ trợ Customer Consent. Customer có quyền: - Chia sẻ - Thu hồi - Quản lý dữ liệu cá nh…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BD-16-010-AC001",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Platform hỗ trợ Customer Consent. Customer có quyền: - Chia sẻ - Thu hồi - Quản lý dữ liệu cá nh…",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BD-16-010-O001"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BD-16-010-AC002",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Platform hỗ trợ Customer Consent. Customer có quyền: - Chia sẻ - Thu hồi - Quản lý dữ liệu cá nh…",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BD-16-010-O002"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BD-16-010-AC003",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Platform hỗ trợ Customer Consent. Customer có quyền: - Chia sẻ - Thu hồi - Quản lý dữ liệu cá nh…",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BD-16-010-O003"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "PRIVACY_POLICY_DENIAL_V1",
      "criterion_id": "BD-16-010-AC004",
      "given": "a data action whose purpose, consent, scope, or effective policy does not permit the requested data use under Platform hỗ trợ Customer Consent. Customer có quyền: - Chia sẻ - Thu hồi - Quản lý dữ liệu cá nh…",
      "observable_evidence": "actor, purpose, consent and scope, effective policies, denial reason, exposed-data comparison, and audit record",
      "then": "the data action is denied, no additional protected data is exposed or changed, and the policy reason is audited",
      "verifies": [
        "BD-16-010-O001",
        "BD-16-010-O002",
        "BD-16-010-O003"
      ],
      "when": "privacy conformance is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-16-010-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Platform hỗ trợ Customer Consent. Customer có quyền: - Chia sẻ - Thu hồi - Quản lý dữ liệu cá nh…",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-16-010-O001",
        "BD-16-010-O002",
        "BD-16-010-O003"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-010-AC001",
        "BD-16-010-AC004",
        "BD-16-010-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-010-O001",
      "obligation_text": "Platform hỗ trợ Customer Consent. Customer có quyền: Chia sẻ."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-010-AC002",
        "BD-16-010-AC004",
        "BD-16-010-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-010-O002",
      "obligation_text": "Platform hỗ trợ Customer Consent. Customer có quyền: Thu hồi."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-010-AC003",
        "BD-16-010-AC004",
        "BD-16-010-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-010-O003",
      "obligation_text": "Platform hỗ trợ Customer Consent. Customer có quyền: Quản lý dữ liệu cá nhân."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-16-010-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-010 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-010 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-16-010 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-010-AC001",
        "BD-16-010-AC002",
        "BD-16-010-AC003"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-010 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Customer Consent. Customer có quyền: - Chia sẻ - Thu hồi - Quản lý dữ liệu cá nhân",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-010",
    "source_context_sha256": "936320b0d9c23fc5d9009696237029baa1ea1cce9ea1ceb283890d88999091ee",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "ca54fbfe8cf457153801e4a48a4e1e270589725434d14ca3f3e5b9d6231d642b",
    "source_lines": "L878-L887",
    "source_section": "31. Business Decisions (Locked) > BD-16-010"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-16-010",
  "title": "Platform hỗ trợ Customer Consent. Customer có quyền: - Chia sẻ - Thu hồi - Quản lý dữ liệu cá nh…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-011 — Session là Business Object. Platform hỗ trợ Concurrent Login trên nhiều thiết bị

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BD-16-011-AC001",
      "given": "a v2.3 capability, configuration, or design change governed by Session là Business Object. Platform hỗ trợ Concurrent Login trên nhiều thiết bị",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BD-16-011-O001"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DESIGN_CONFORMANCE_OBSERVATION_V1",
      "criterion_id": "BD-16-011-AC002",
      "given": "a v2.3 capability, configuration, or design change governed by Session là Business Object. Platform hỗ trợ Concurrent Login trên nhiều thiết bị",
      "observable_evidence": "conformance decision, requirement-to-design trace, applicable configuration evidence, and recorded boundary violations",
      "then": "the conformance review identifies the applicable principle, links it to the governed requirement and design boundary, and records no prohibited coupling",
      "verifies": [
        "BD-16-011-O002"
      ],
      "when": "conformance is reviewed before the change is accepted"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "DESIGN_CONFORMANCE_FAILURE_V1",
      "criterion_id": "BD-16-011-AC003",
      "given": "a proposed change with missing traceability or a boundary violation under Session là Business Object. Platform hỗ trợ Concurrent Login trên nhiều thiết bị",
      "observable_evidence": "conformance result, violated principle, missing trace or configuration evidence, and review record",
      "then": "the change receives a non-conforming decision identifying the missing trace or violated boundary and is not accepted as conforming",
      "verifies": [
        "BD-16-011-O001",
        "BD-16-011-O002"
      ],
      "when": "design conformance is reviewed"
    },
    {
      "case": "CONCURRENCY",
      "controlled_contract": "EXPLICIT_CONCURRENCY_CONTRACT_V1",
      "criterion_id": "BD-16-011-AC004",
      "given": "two or more concurrent actions covered by an explicit concurrency boundary in Session là Business Object. Platform hỗ trợ Concurrent Login trên nhiều thiết bị",
      "observable_evidence": "concurrent inputs, individual outcomes, final state, and invariant comparison",
      "then": "the resulting decisions and state preserve the concurrency invariant stated by the referenced obligation",
      "verifies": [
        "BD-16-011-O001",
        "BD-16-011-O002"
      ],
      "when": "the actions contend for the same governed business state"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-011-AC001",
        "BD-16-011-AC003",
        "BD-16-011-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-011-O001",
      "obligation_text": "Session là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-011-AC002",
        "BD-16-011-AC003",
        "BD-16-011-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-011-O002",
      "obligation_text": "Platform hỗ trợ Concurrent Login trên nhiều thiết bị"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-16-011 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [
        "BD-16-011-AC004"
      ],
      "status": "APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-011 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-16-011 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-011-AC001",
        "BD-16-011-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-011 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Session là Business Object. Platform hỗ trợ Concurrent Login trên nhiều thiết bị.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Session Management",
    "source_context_sha256": "60b36a518190dac174096d936c416e4f475e1d528e6db65dbf1385e4e2038708",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "866f25db65a56b184c54d1cd39bd27f1d4b0329bf790c2f4cb54e342dcbfe492",
    "source_lines": "L890-L895",
    "source_section": "31. Business Decisions (Locked) > BD-16-011"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "PERFORMANCE_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-16-011",
  "title": "Session là Business Object. Platform hỗ trợ Concurrent Login trên nhiều thiết bị",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-012 — API Security hỗ trợ nhiều phương thức. Bao gồm: - OAuth2 - JWT - API Key - HMAC - Digital Signat…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-012-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for API Security hỗ trợ nhiều phương thức. Bao gồm: - OAuth2 - JWT - API Key - HMAC - Digital Signat…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-012-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-012-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for API Security hỗ trợ nhiều phương thức. Bao gồm: - OAuth2 - JWT - API Key - HMAC - Digital Signat…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-012-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-012-AC003",
      "given": "an identified principal, applicable assurance context, and policy inputs for API Security hỗ trợ nhiều phương thức. Bao gồm: - OAuth2 - JWT - API Key - HMAC - Digital Signat…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-012-O003"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-012-AC004",
      "given": "an identified principal, applicable assurance context, and policy inputs for API Security hỗ trợ nhiều phương thức. Bao gồm: - OAuth2 - JWT - API Key - HMAC - Digital Signat…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-012-O004"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-012-AC005",
      "given": "an identified principal, applicable assurance context, and policy inputs for API Security hỗ trợ nhiều phương thức. Bao gồm: - OAuth2 - JWT - API Key - HMAC - Digital Signat…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-012-O005"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-012-AC006",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for API Security hỗ trợ nhiều phương thức. Bao gồm: - OAuth2 - JWT - API Key - HMAC - Digital Signat…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-012-O001",
        "BD-16-012-O002",
        "BD-16-012-O003",
        "BD-16-012-O004",
        "BD-16-012-O005"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-012-AC007",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by API Security hỗ trợ nhiều phương thức. Bao gồm: - OAuth2 - JWT - API Key - HMAC - Digital Signat…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-012-O001",
        "BD-16-012-O002",
        "BD-16-012-O003",
        "BD-16-012-O004",
        "BD-16-012-O005"
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
        "BD-16-012-AC001",
        "BD-16-012-AC006",
        "BD-16-012-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-012-O001",
      "obligation_text": "API Security hỗ trợ nhiều phương thức. Bao gồm: OAuth2."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-012-AC002",
        "BD-16-012-AC006",
        "BD-16-012-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-012-O002",
      "obligation_text": "API Security hỗ trợ nhiều phương thức. Bao gồm: JWT."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-012-AC003",
        "BD-16-012-AC006",
        "BD-16-012-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-012-O003",
      "obligation_text": "API Security hỗ trợ nhiều phương thức. Bao gồm: API Key."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-012-AC004",
        "BD-16-012-AC006",
        "BD-16-012-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-012-O004",
      "obligation_text": "API Security hỗ trợ nhiều phương thức. Bao gồm: HMAC."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-012-AC005",
        "BD-16-012-AC006",
        "BD-16-012-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-012-O005",
      "obligation_text": "API Security hỗ trợ nhiều phương thức. Bao gồm: Digital Signature."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-16-012 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-012 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-012 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-012-AC007"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-012-AC001",
        "BD-16-012-AC002",
        "BD-16-012-AC003",
        "BD-16-012-AC004",
        "BD-16-012-AC005"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-012 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "API Security hỗ trợ nhiều phương thức. Bao gồm: - OAuth2 - JWT - API Key - HMAC - Digital Signature",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-012",
    "source_context_sha256": "a2bb459a948f0d0c711cb1fd20b5d07a1b1c5c08a293954e3bd8105ad0149460",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "b03c0dddf7ccb039407f8ee53a0da20b065b5a7c64f99b22f7c2972206a4bca0",
    "source_lines": "L898-L909",
    "source_section": "31. Business Decisions (Locked) > BD-16-012"
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
  "stable_id": "BD-16-012",
  "title": "API Security hỗ trợ nhiều phương thức. Bao gồm: - OAuth2 - JWT - API Key - HMAC - Digital Signat…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-013 — Secret là Business Object. Secret được quản lý tập trung

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-013-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Secret là Business Object. Secret được quản lý tập trung",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-013-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-013-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Secret là Business Object. Secret được quản lý tập trung",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-013-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-013-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Secret là Business Object. Secret được quản lý tập trung",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-013-O001",
        "BD-16-013-O002"
      ],
      "when": "the protected decision or action is attempted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-013-AC001",
        "BD-16-013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-013-O001",
      "obligation_text": "Secret là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-013-AC002",
        "BD-16-013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-013-O002",
      "obligation_text": "Secret được quản lý tập trung"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-16-013 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-013 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-013 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-16-013 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-013-AC001",
        "BD-16-013-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-013 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Secret là Business Object. Secret được quản lý tập trung.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Secret Management",
    "source_context_sha256": "14a6650ddc3674e6733d1838f7b37163663d95831323d14dc203b4d7dab54c7b",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "af3746b0ea8a6068421df1104d5ed51ebae6d30ac65b62c7fb9c5a3532637e1b",
    "source_lines": "L912-L917",
    "source_section": "31. Business Decisions (Locked) > BD-16-013"
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
  "stable_id": "BD-16-013",
  "title": "Secret là Business Object. Secret được quản lý tập trung",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-014 — Platform hỗ trợ Encryption In Transit. Kiến trúc mở để hỗ trợ Encryption At Rest trong các phiên…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-014-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Platform hỗ trợ Encryption In Transit. Kiến trúc mở để hỗ trợ Encryption At Rest trong các phiên…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-014-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-014-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Platform hỗ trợ Encryption In Transit. Kiến trúc mở để hỗ trợ Encryption At Rest trong các phiên…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-014-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-014-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Platform hỗ trợ Encryption In Transit. Kiến trúc mở để hỗ trợ Encryption At Rest trong các phiên…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-014-O001",
        "BD-16-014-O002"
      ],
      "when": "the protected decision or action is attempted"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-014-AC001",
        "BD-16-014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-014-O001",
      "obligation_text": "Platform hỗ trợ Encryption In Transit"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-014-AC002",
        "BD-16-014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-014-O002",
      "obligation_text": "Kiến trúc mở để hỗ trợ Encryption At Rest trong các phiên bản tiếp theo"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-16-014 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-16-014 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-014-AC001",
        "BD-16-014-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-014 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Encryption In Transit. Kiến trúc mở để hỗ trợ Encryption At Rest trong các phiên bản tiếp theo.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-014",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-014",
    "source_context_sha256": "bf5757db2c4220c74a42b8ed3d24d78a7a60cc043d9b0b34481e3169a3461f2b",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "570a9a04ea5996836403e2537979e9c8829c65992f9f1cc7d04c079ff2878c7d",
    "source_lines": "L920-L925",
    "source_section": "31. Business Decisions (Locked) > BD-16-014"
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
  "stable_id": "BD-16-014",
  "title": "Platform hỗ trợ Encryption In Transit. Kiến trúc mở để hỗ trợ Encryption At Rest trong các phiên…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-015 — Platform hỗ trợ Key Rotation. Key Management được quản lý tập trung

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-015-AC001",
      "given": "the applicable business context, actor, and input for Platform hỗ trợ Key Rotation. Key Management được quản lý tập trung",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-015-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-015-AC002",
      "given": "the applicable business context, actor, and input for Platform hỗ trợ Key Rotation. Key Management được quản lý tập trung",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-015-O002"
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
        "BD-16-015-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-015-O001",
      "obligation_text": "Platform hỗ trợ Key Rotation"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-015-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-015-O002",
      "obligation_text": "Key Management được quản lý tập trung"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Key Rotation. Key Management được quản lý tập trung.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-015",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-015",
    "source_context_sha256": "d0e794590415b48f73ea25d7367f4b77e0da884e65758844d2a6c25de6e2e5da",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "9906ef886de101761f545f508424176aa5837dd579751e305b9d71d8e570a995",
    "source_lines": "L928-L933",
    "source_section": "31. Business Decisions (Locked) > BD-16-015"
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
  "stable_id": "BD-16-015",
  "title": "Platform hỗ trợ Key Rotation. Key Management được quản lý tập trung",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-016 — Audit Log là Business Object. Audit ghi nhận đầy đủ các Security Event và Business Event quan tr…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-016-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Audit Log là Business Object. Audit ghi nhận đầy đủ các Security Event và Business Event quan tr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-016-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-016-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Audit Log là Business Object. Audit ghi nhận đầy đủ các Security Event và Business Event quan tr…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-016-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-016-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Audit Log là Business Object. Audit ghi nhận đầy đủ các Security Event và Business Event quan tr…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-016-O001",
        "BD-16-016-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-016-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Audit Log là Business Object. Audit ghi nhận đầy đủ các Security Event và Business Event quan tr…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-016-O001",
        "BD-16-016-O002"
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
        "BD-16-016-AC001",
        "BD-16-016-AC003",
        "BD-16-016-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-016-O001",
      "obligation_text": "Audit Log là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-016-AC002",
        "BD-16-016-AC003",
        "BD-16-016-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-016-O002",
      "obligation_text": "Audit ghi nhận đầy đủ các Security Event và Business Event quan trọng"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-16-016 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-016 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-016 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-016-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-016-AC001",
        "BD-16-016-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-016 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Audit Log là Business Object. Audit ghi nhận đầy đủ các Security Event và Business Event quan trọng.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-002"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-016",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Audit Logging",
    "source_context_sha256": "c3a223ed8456790c07473f29edd0f53592bcc7df96f85b5cef84a1546f158902",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "8f89387031df2e67dcabbd440fa88eb66bc5c0cdea4c93f5bb0149dfc57d00e3",
    "source_lines": "L936-L941",
    "source_section": "31. Business Decisions (Locked) > BD-16-016"
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
  "stable_id": "BD-16-016",
  "title": "Audit Log là Business Object. Audit ghi nhận đầy đủ các Security Event và Business Event quan tr…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-017 — Platform hỗ trợ Compliance. Phiên bản hiện tại hỗ trợ: - GDPR

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-017-AC001",
      "given": "the applicable business context, actor, and input for Platform hỗ trợ Compliance. Phiên bản hiện tại hỗ trợ: - GDPR",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-017-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-017-AC002",
      "given": "the applicable business context, actor, and input for Platform hỗ trợ Compliance. Phiên bản hiện tại hỗ trợ: - GDPR",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-017-O002"
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
        "BD-16-017-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-017-O001",
      "obligation_text": "Platform hỗ trợ Compliance"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-017-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-017-O002",
      "obligation_text": "Phiên bản hiện tại hỗ trợ: - GDPR"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Compliance. Phiên bản hiện tại hỗ trợ: - GDPR",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-017",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "19. Compliance",
    "source_context_sha256": "8ecd51fd46339fcaf0af2b349c704ad4cbf3995e4f34d984346e3529d5f08c54",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "b007d98b99e2624724427a438e44f1167beaae2f64ff747cfce5550cba6fecfd",
    "source_lines": "L944-L951",
    "source_section": "31. Business Decisions (Locked) > BD-16-017"
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
  "stable_id": "BD-16-017",
  "title": "Platform hỗ trợ Compliance. Phiên bản hiện tại hỗ trợ: - GDPR",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-018 — Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: - Export Data - Delete Identity - Customer Co…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BD-16-018-AC001",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: - Export Data - Delete Identity - Customer Co…",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BD-16-018-O001"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BD-16-018-AC002",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: - Export Data - Delete Identity - Customer Co…",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BD-16-018-O002"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BD-16-018-AC003",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: - Export Data - Delete Identity - Customer Co…",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BD-16-018-O003"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "PRIVACY_POLICY_DENIAL_V1",
      "criterion_id": "BD-16-018-AC004",
      "given": "a data action whose purpose, consent, scope, or effective policy does not permit the requested data use under Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: - Export Data - Delete Identity - Customer Co…",
      "observable_evidence": "actor, purpose, consent and scope, effective policies, denial reason, exposed-data comparison, and audit record",
      "then": "the data action is denied, no additional protected data is exposed or changed, and the policy reason is audited",
      "verifies": [
        "BD-16-018-O001",
        "BD-16-018-O002",
        "BD-16-018-O003"
      ],
      "when": "privacy conformance is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-16-018-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: - Export Data - Delete Identity - Customer Co…",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-16-018-O001",
        "BD-16-018-O002",
        "BD-16-018-O003"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-018-AC001",
        "BD-16-018-AC004",
        "BD-16-018-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-018-O001",
      "obligation_text": "Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: Export Data."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-018-AC002",
        "BD-16-018-AC004",
        "BD-16-018-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-018-O002",
      "obligation_text": "Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: Delete Identity."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-018-AC003",
        "BD-16-018-AC004",
        "BD-16-018-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-018-O003",
      "obligation_text": "Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: Customer Consent."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-16-018-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-018 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-018 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-16-018 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-018-AC001",
        "BD-16-018-AC002",
        "BD-16-018-AC003"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-018 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: - Export Data - Delete Identity - Customer Consent",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-018",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Privacy Protection",
    "source_context_sha256": "8c4487e761be8cd1fc9f35b9aaf6ab86e769fd621880eeffec2d39cd985c1792",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "628377e4da987fc51aea735cbb87ef7c565a62ee03591cde11317d207bfccde3",
    "source_lines": "L954-L963",
    "source_section": "31. Business Decisions (Locked) > BD-16-018"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-16-018",
  "title": "Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: - Export Data - Delete Identity - Customer Co…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-019 — API Permission được quản lý độc lập với Portal Permission

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-019-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for API Permission được quản lý độc lập với Portal Permission",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-019-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-019-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for API Permission được quản lý độc lập với Portal Permission",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-019-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-019-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by API Permission được quản lý độc lập với Portal Permission",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-019-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-16-019-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by API Permission được quản lý độc lập với Portal Permission",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-16-019-O001"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-019-AC001",
        "BD-16-019-AC002",
        "BD-16-019-AC003",
        "BD-16-019-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-019-O001",
      "obligation_text": "API Permission được quản lý độc lập với Portal Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-16-019-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-019 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-019 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-019-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-019-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-019 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "API Permission được quản lý độc lập với Portal Permission.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-019",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-019",
    "source_context_sha256": "2872aba530640785779b2e860754c52290a9df4d2317d9ff348a4e705ee809e6",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "eb70ae86ec188cab31ab5c92a5061c1fe981159f0b6526485afa0ace14e69231",
    "source_lines": "L966-L969",
    "source_section": "31. Business Decisions (Locked) > BD-16-019"
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
  "stable_id": "BD-16-019",
  "title": "API Permission được quản lý độc lập với Portal Permission",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-020 — Mỗi Organization có Security Policy riêng. Organization có thể Override theo Capability được cấp

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-020-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Mỗi Organization có Security Policy riêng. Organization có thể Override theo Capability được cấp",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-020-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-020-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Mỗi Organization có Security Policy riêng. Organization có thể Override theo Capability được cấp",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-020-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-020-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Mỗi Organization có Security Policy riêng. Organization có thể Override theo Capability được cấp",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-020-O001",
        "BD-16-020-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-020-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Mỗi Organization có Security Policy riêng. Organization có thể Override theo Capability được cấp",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-020-O001",
        "BD-16-020-O002"
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
        "BD-16-020-AC001",
        "BD-16-020-AC003",
        "BD-16-020-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-020-O001",
      "obligation_text": "Mỗi Organization có Security Policy riêng"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-020-AC002",
        "BD-16-020-AC003",
        "BD-16-020-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-020-O002",
      "obligation_text": "Organization có thể Override theo Capability được cấp"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-16-020 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-020 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-020 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-020-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-020-AC001",
        "BD-16-020-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-020 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi Organization có Security Policy riêng. Organization có thể Override theo Capability được cấp.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-020",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "22. Organization Security Policy",
    "source_context_sha256": "54d90c2050256c34b477a399014f03d90c11b92f7bcc18b24d19bbe679fbfc25",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "41582cc4233be4c676103b92d931d27f07d11a6cda70026bd1c48a59f0fd6f84",
    "source_lines": "L972-L977",
    "source_section": "31. Business Decisions (Locked) > BD-16-020"
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
  "stable_id": "BD-16-020",
  "title": "Mỗi Organization có Security Policy riêng. Organization có thể Override theo Capability được cấp",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-021 — Risk Rule là Business Object. Risk Rule được cấu hình. Không Hard-code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-16-021-AC001",
      "given": "a candidate Risk Rule là Business Object. Risk Rule được cấu hình. Không Hard-code record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-16-021-O001"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-16-021-AC002",
      "given": "a candidate Risk Rule là Business Object. Risk Rule được cấu hình. Không Hard-code record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-16-021-O002"
      ],
      "when": "the candidate is evaluated against its declared data contract"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-16-021-AC003",
      "given": "a candidate Risk Rule là Business Object. Risk Rule được cấu hình. Không Hard-code record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-16-021-O003"
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
        "BD-16-021-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-021-O001",
      "obligation_text": "Risk Rule là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-021-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-021-O002",
      "obligation_text": "Risk Rule được cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-021-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-021-O003",
      "obligation_text": "Không Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Risk Rule là Business Object. Risk Rule được cấu hình. Không Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-021",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Risk Rule",
    "source_context_sha256": "79a6378d5d297d3ac4b6561a2c177377d25cd033018faace37cf7d681b9ad773",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "dfb0c2af2ef6e28af30469baf3d44f2397673230f9a1df6770fefc36218e05a1",
    "source_lines": "L980-L987",
    "source_section": "31. Business Decisions (Locked) > BD-16-021"
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
  "stable_id": "BD-16-021",
  "title": "Risk Rule là Business Object. Risk Rule được cấu hình. Không Hard-code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-022 — Platform hỗ trợ Temporary Account Lock

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-022-AC001",
      "given": "the applicable business context, actor, and input for Platform hỗ trợ Temporary Account Lock",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-022-O001"
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
        "BD-16-022-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-022-O001",
      "obligation_text": "Platform hỗ trợ Temporary Account Lock"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform hỗ trợ Temporary Account Lock.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-022",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-022",
    "source_context_sha256": "90b580d8730cc6a91a614608e6ca0b6277dfc3109e1f6b04c3fa9d62ffc70ff6",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "76cdcf19bc3b272b7469e626def2e8c5ebea5147aaf12dbe1ea4e2300bcad58f",
    "source_lines": "L990-L993",
    "source_section": "31. Business Decisions (Locked) > BD-16-022"
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
  "stable_id": "BD-16-022",
  "title": "Platform hỗ trợ Temporary Account Lock",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-023 — Audit Log được lưu trực tuyến 03 tháng. Sau đó được Archive

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-023-AC001",
      "given": "an operational task within the scope of Audit Log được lưu trực tuyến 03 tháng. Sau đó được Archive",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-16-023-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-023-AC002",
      "given": "an operational task within the scope of Audit Log được lưu trực tuyến 03 tháng. Sau đó được Archive",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-16-023-O002"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-16-023-AC003",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Audit Log được lưu trực tuyến 03 tháng. Sau đó được Archive",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-16-023-O001",
        "BD-16-023-O002"
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
        "BD-16-023-AC001",
        "BD-16-023-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-023-O001",
      "obligation_text": "Audit Log được lưu trực tuyến 03 tháng"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-023-AC002",
        "BD-16-023-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-023-O002",
      "obligation_text": "Sau đó được Archive"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-16-023 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-023 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-023 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-16-023 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-023-AC001",
        "BD-16-023-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-023 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Audit Log được lưu trực tuyến 03 tháng. Sau đó được Archive.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-023",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-023",
    "source_context_sha256": "79c1d827e263bc44c412c946c7c3639fecea0a57fc5395fa41c60496f8e15493",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "c091a9d2008eab92bda4b96076e11040c245cd59b9d05c6012eb0f553a0dc15c",
    "source_lines": "L996-L1001",
    "source_section": "31. Business Decisions (Locked) > BD-16-023"
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
  "stable_id": "BD-16-023",
  "title": "Audit Log được lưu trực tuyến 03 tháng. Sau đó được Archive",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-024 — Permission Evaluation Engine là thành phần trung tâm của Security Platform. Business Domain khôn…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-024-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission Evaluation Engine là thành phần trung tâm của Security Platform. Business Domain khôn…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-024-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-024-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission Evaluation Engine là thành phần trung tâm của Security Platform. Business Domain khôn…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-024-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-024-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Permission Evaluation Engine là thành phần trung tâm của Security Platform. Business Domain khôn…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-024-O001",
        "BD-16-024-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-024-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Permission Evaluation Engine là thành phần trung tâm của Security Platform. Business Domain khôn…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-024-O001",
        "BD-16-024-O002"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-16-024-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Permission Evaluation Engine là thành phần trung tâm của Security Platform. Business Domain khôn…",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-16-024-O001",
        "BD-16-024-O002"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-024-AC001",
        "BD-16-024-AC003",
        "BD-16-024-AC004",
        "BD-16-024-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-024-O001",
      "obligation_text": "Permission Evaluation Engine là thành phần trung tâm của Security Platform"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-024-AC002",
        "BD-16-024-AC003",
        "BD-16-024-AC004",
        "BD-16-024-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-024-O002",
      "obligation_text": "Business Domain không tự đánh giá Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-16-024-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-024 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-024 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-024-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-024-AC001",
        "BD-16-024-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-024 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission Evaluation Engine là thành phần trung tâm của Security Platform. Business Domain không tự đánh giá Permission.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-024",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "26. Permission Evaluation Engine",
    "source_context_sha256": "402f52e10aa02d37c06ea1e68cdf503a4e3d105037834ecbdd82428c3cd33ded",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "6451f8de8bc8fe2a09e8c222237086596a41ee9707fcb2d85fb926e43a63ee44",
    "source_lines": "L1004-L1009",
    "source_section": "31. Business Decisions (Locked) > BD-16-024"
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
  "stable_id": "BD-16-024",
  "title": "Permission Evaluation Engine là thành phần trung tâm của Security Platform. Business Domain khôn…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-025 — Security Policy là Business Object. Security Policy hỗ trợ: - Version - Effective Date - Approva…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-025-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Security Policy là Business Object. Security Policy hỗ trợ: - Version - Effective Date - Approva…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-025-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-025-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Security Policy là Business Object. Security Policy hỗ trợ: - Version - Effective Date - Approva…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-025-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-025-AC003",
      "given": "an identified principal, applicable assurance context, and policy inputs for Security Policy là Business Object. Security Policy hỗ trợ: - Version - Effective Date - Approva…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-025-O003"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-025-AC004",
      "given": "an identified principal, applicable assurance context, and policy inputs for Security Policy là Business Object. Security Policy hỗ trợ: - Version - Effective Date - Approva…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-025-O004"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-025-AC005",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Security Policy là Business Object. Security Policy hỗ trợ: - Version - Effective Date - Approva…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-025-O001",
        "BD-16-025-O002",
        "BD-16-025-O003",
        "BD-16-025-O004"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-025-AC006",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Security Policy là Business Object. Security Policy hỗ trợ: - Version - Effective Date - Approva…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-025-O001",
        "BD-16-025-O002",
        "BD-16-025-O003",
        "BD-16-025-O004"
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
        "BD-16-025-AC001",
        "BD-16-025-AC005",
        "BD-16-025-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-025-O001",
      "obligation_text": "Security Policy là Business Object. Security Policy hỗ trợ: Version."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-025-AC002",
        "BD-16-025-AC005",
        "BD-16-025-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-025-O002",
      "obligation_text": "Security Policy là Business Object. Security Policy hỗ trợ: Effective Date."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-025-AC003",
        "BD-16-025-AC005",
        "BD-16-025-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-025-O003",
      "obligation_text": "Security Policy là Business Object. Security Policy hỗ trợ: Approval."
    },
    {
      "acceptance_criterion_references": [
        "BD-16-025-AC004",
        "BD-16-025-AC005",
        "BD-16-025-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-025-O004",
      "obligation_text": "Security Policy là Business Object. Security Policy hỗ trợ: Audit."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-16-025 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-025 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-025 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-025-AC006"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-025-AC001",
        "BD-16-025-AC002",
        "BD-16-025-AC003",
        "BD-16-025-AC004"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-025 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Security Policy là Business Object. Security Policy hỗ trợ: - Version - Effective Date - Approval - Audit",
  "provenance": {
    "approved_decisions": [
      "BDD-27",
      "SD-03"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-025",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Security Policy",
    "source_context_sha256": "0994ea9a1e4c603b96e321b12126ab92e5272fbb18e5a83932e55c88b1836a05",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "652461eb68fdedf2e1c01a26ca9093b171fb37690a866ba3439dc2bf5f850a3e",
    "source_lines": "L1012-L1022",
    "source_section": "31. Business Decisions (Locked) > BD-16-025"
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
  "stable_id": "BD-16-025",
  "title": "Security Policy là Business Object. Security Policy hỗ trợ: - Version - Effective Date - Approva…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-026 — Identity Platform hỗ trợ Federation

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-026-AC001",
      "given": "the applicable business context, actor, and input for Identity Platform hỗ trợ Federation",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-026-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-16-026-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Identity Platform hỗ trợ Federation",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-16-026-O001"
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
        "BD-16-026-AC001",
        "BD-16-026-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-026-O001",
      "obligation_text": "Identity Platform hỗ trợ Federation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-16-026 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-026 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-026 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-16-026 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-026-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-026 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Identity Platform hỗ trợ Federation.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-001",
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-026",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Identity Federation",
    "source_context_sha256": "79bf64ca17e2729d4ed0d69b3e1c1637fdcc8ad8d217df27372de3d0eec305a5",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "97fad0d260b86cd8ba22d969ea8479f264ee93e7d0db83757732dd2cf507ce64",
    "source_lines": "L1025-L1028",
    "source_section": "31. Business Decisions (Locked) > BD-16-026"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [
      "EP-16-009"
    ],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-16-026",
  "title": "Identity Platform hỗ trợ Federation",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-027 — Security Platform Publish Business Event

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-027-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Security Platform Publish Business Event",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-16-027-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-027-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Security Platform Publish Business Event",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-027-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-027-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Security Platform Publish Business Event",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-027-O001"
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
        "BD-16-027-AC001",
        "BD-16-027-AC002",
        "BD-16-027-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-027-O001",
      "obligation_text": "Security Platform Publish Business Event"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-16-027 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-027 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-027 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-027-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-027-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-027 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Security Platform Publish Business Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-027",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "29. Security Business Events",
    "source_context_sha256": "6bd0565e1d201ed4d938250bfe47c7cda8fc6c1a9bde6f1e0558bdc02dd3c34a",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "f683049be7eafcfa2591845c50ac54b23555c809358f2afcef3b5d0311e606fb",
    "source_lines": "L1031-L1034",
    "source_section": "31. Business Decisions (Locked) > BD-16-027"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [
      "EP-16-008"
    ],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-16-027",
  "title": "Security Platform Publish Business Event",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-028 — Data Classification là Business Object

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "DATA_CONTRACT_OBSERVATION_V1",
      "criterion_id": "BD-16-028-AC001",
      "given": "a candidate Data Classification là Business Object record and the canonical records it references",
      "observable_evidence": "validation outcome, accepted field values, resolved canonical references, and resulting persisted business state",
      "then": "validation returns ACCEPTED only with all required values present, relationship cardinalities satisfied, canonical references resolved, and the resulting business record exposing those evaluated values",
      "verifies": [
        "BD-16-028-O001"
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
        "BD-16-028-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-028-O001",
      "obligation_text": "Data Classification là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Data Classification là Business Object.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-028",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "30. Data Classification",
    "source_context_sha256": "4d1d81f73888c349be07e2382bbdd5215a83352a43dcd5e1ec014766edf9a88f",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "0f3f465cd6b0fe68db5a7dd35e27c418725d1820289804ca7ca89dadb92e84ae",
    "source_lines": "L1037-L1040",
    "source_section": "31. Business Decisions (Locked) > BD-16-028"
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
  "stable_id": "BD-16-028",
  "title": "Data Classification là Business Object",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-029 — Platform áp dụng Zero Trust Principle

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-16-029-AC001",
      "given": "the applicable business context, actor, and input for Platform áp dụng Zero Trust Principle",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-16-029-O001"
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
        "BD-16-029-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-029-O001",
      "obligation_text": "Platform áp dụng Zero Trust Principle"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform áp dụng Zero Trust Principle.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-029",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-029",
    "source_context_sha256": "61a8613b355c91eb9ac3f561abb2caaa5ac01cf0ee115e5c7673d3a53488c189",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "f4e8696a3c98ffc53f3824898df29e54f80b26b91d2b9f1570914682812d25fc",
    "source_lines": "L1043-L1046",
    "source_section": "31. Business Decisions (Locked) > BD-16-029"
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
  "stable_id": "BD-16-029",
  "title": "Platform áp dụng Zero Trust Principle",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-030 — Toàn bộ truy cập dữ liệu phải được đánh giá động thông qua Permission Evaluation Engine và Secur…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-16-030-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Toàn bộ truy cập dữ liệu phải được đánh giá động thông qua Permission Evaluation Engine và Secur…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the permission decision is recalculated from the current applicable attributes and policy; changing a governing input changes the effective decision without relying on a stored static permission result",
      "verifies": [
        "BD-16-030-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-030-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Toàn bộ truy cập dữ liệu phải được đánh giá động thông qua Permission Evaluation Engine và Secur…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-16-030-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-16-030-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Toàn bộ truy cập dữ liệu phải được đánh giá động thông qua Permission Evaluation Engine và Secur…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-16-030-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-16-030-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Toàn bộ truy cập dữ liệu phải được đánh giá động thông qua Permission Evaluation Engine và Secur…",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-16-030-O001"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BD-16-030-AC001",
        "BD-16-030-AC002",
        "BD-16-030-AC003",
        "BD-16-030-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-030-O001",
      "obligation_text": "Toàn bộ truy cập dữ liệu phải được đánh giá động thông qua Permission Evaluation Engine và Security Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-16-030-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-16-030 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-16-030 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-16-030-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-16-030-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-16-030 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ truy cập dữ liệu phải được đánh giá động thông qua Permission Evaluation Engine và Security Policy.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-030",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-030",
    "source_context_sha256": "9d43e991e1c760451b45cbfb913b428fdbdb2da416ef45a515a92c4a37df903d",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "8b97c5a2ae024d1475b0feaf3aa54c31f05c4553ba04e57c9fe66f1cf9739e03",
    "source_lines": "L1049-L1052",
    "source_section": "31. Business Decisions (Locked) > BD-16-030"
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
  "stable_id": "BD-16-030",
  "title": "Toàn bộ truy cập dữ liệu phải được đánh giá động thông qua Permission Evaluation Engine và Secur…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R001 — Permission không được xác định chỉ dựa trên Role

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R001-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission không được xác định chỉ dựa trên Role",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the prohibited security decision path produces no effective permission or protected-state change, and conformance evidence identifies the attempted bypass",
      "verifies": [
        "BRD-WS-16-R001-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R001-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Permission không được xác định chỉ dựa trên Role",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-16-R001-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R001-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Permission không được xác định chỉ dựa trên Role",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-16-R001-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-16-R001-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Permission không được xác định chỉ dựa trên Role",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-16-R001-O001"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-16-R001-AC001",
        "BRD-WS-16-R001-AC002",
        "BRD-WS-16-R001-AC003",
        "BRD-WS-16-R001-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R001-O001",
      "obligation_text": "Permission không được xác định chỉ dựa trên Role"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-16-R001-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R001 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R001 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-16-R001-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R001-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R001 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission không được xác định chỉ dựa trên Role.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-001",
    "previous_temporary_key": "TMP-BRD-WS-16-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Authorization Model",
    "source_context_sha256": "056a4758658cb438ed24160bbd341ea1563558eba2f30d3492f97a940f925c9c",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "d90990c2f3e9737ee237623199fed3c3cbc69a819abe0c32b053d0b32c3cb015",
    "source_lines": "L171",
    "source_section": "6. Authorization Model"
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
  "stable_id": "BRD-WS-16-R001",
  "title": "Permission không được xác định chỉ dựa trên Role",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R002 — Authorization phải hỗ trợ mở rộng để đáp ứng các mô hình phân quyền phức tạp trong tương lai

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R002-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Authorization phải hỗ trợ mở rộng để đáp ứng các mô hình phân quyền phức tạp trong tương lai",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-16-R002-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R002-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Authorization phải hỗ trợ mở rộng để đáp ứng các mô hình phân quyền phức tạp trong tương lai",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-16-R002-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-16-R002-AC003",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Authorization phải hỗ trợ mở rộng để đáp ứng các mô hình phân quyền phức tạp trong tương lai",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-16-R002-O001"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-16-R002-AC001",
        "BRD-WS-16-R002-AC002",
        "BRD-WS-16-R002-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R002-O001",
      "obligation_text": "Authorization phải hỗ trợ mở rộng để đáp ứng các mô hình phân quyền phức tạp trong tương lai"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-16-R002-AC003"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R002 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R002-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Authorization phải hỗ trợ mở rộng để đáp ứng các mô hình phân quyền phức tạp trong tương lai.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-002",
    "previous_temporary_key": "TMP-BRD-WS-16-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Authorization Model",
    "source_context_sha256": "056a4758658cb438ed24160bbd341ea1563558eba2f30d3492f97a940f925c9c",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "0f3674ea96cbdabaf8ac81a95ec1fab7cdb5502d76c1b2a640532a71f9ec1eae",
    "source_lines": "L175",
    "source_section": "6. Authorization Model"
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
  "stable_id": "BRD-WS-16-R002",
  "title": "Authorization phải hỗ trợ mở rộng để đáp ứng các mô hình phân quyền phức tạp trong tương lai",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R003 — Permission không được Hard-code trong mã nguồn

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R003-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission không được Hard-code trong mã nguồn",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the prohibited security decision path produces no effective permission or protected-state change, and conformance evidence identifies the attempted bypass",
      "verifies": [
        "BRD-WS-16-R003-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R003-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Permission không được Hard-code trong mã nguồn",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-16-R003-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R003-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Permission không được Hard-code trong mã nguồn",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-16-R003-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-16-R003-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Permission không được Hard-code trong mã nguồn",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-16-R003-O001"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-16-R003-AC001",
        "BRD-WS-16-R003-AC002",
        "BRD-WS-16-R003-AC003",
        "BRD-WS-16-R003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R003-O001",
      "obligation_text": "Permission không được Hard-code trong mã nguồn"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-16-R003-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-16-R003-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R003-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission không được Hard-code trong mã nguồn.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-003",
    "previous_temporary_key": "TMP-BRD-WS-16-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "7. Permission",
    "source_context_sha256": "3d3ab73af16e4a1750956c224ac2159a10ec60b5d687a57e6587480e9b2681d8",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "2387386fcb1ef0ac81da400842049aa05d4dc98f6e674f7096772706733df0e5",
    "source_lines": "L196",
    "source_section": "7. Permission"
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
  "stable_id": "BRD-WS-16-R003",
  "title": "Permission không được Hard-code trong mã nguồn",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R004 — Không được Hard-code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R004-AC001",
      "given": "the applicable business context, actor, and input for Không được Hard-code",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the effective configuration and version are visible in the decision evidence, and an approved configuration change changes the governed result without a code change",
      "verifies": [
        "BRD-WS-16-R004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-16-R004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Không được Hard-code",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-16-R004-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R004-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Không được Hard-code",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-16-R004-O001"
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
        "BRD-WS-16-R004-AC001",
        "BRD-WS-16-R004-AC002",
        "BRD-WS-16-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R004-O001",
      "obligation_text": "Không được Hard-code"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-16-R004-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R004-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không được Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-004",
    "previous_temporary_key": "TMP-BRD-WS-16-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Field-Level Permission",
    "source_context_sha256": "f1685ea7a9aa9d5e51c3fe9ba88512a113b60dcaf1ef65fab2dea61565df803c",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "4621b7640c0dcd2270db940c6e871c9dfa60a401b1675b7473403baf1ab00536",
    "source_lines": "L266",
    "source_section": "10. Field-Level Permission"
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
  "stable_id": "BRD-WS-16-R004",
  "title": "Không được Hard-code",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R005 — Secret không được lưu dưới dạng Plain Text

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R005-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Secret không được lưu dưới dạng Plain Text",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the prohibited security decision path produces no effective permission or protected-state change, and conformance evidence identifies the attempted bypass",
      "verifies": [
        "BRD-WS-16-R005-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R005-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Secret không được lưu dưới dạng Plain Text",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-16-R005-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R005-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Secret không được lưu dưới dạng Plain Text",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-16-R005-O001"
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
        "BRD-WS-16-R005-AC001",
        "BRD-WS-16-R005-AC002",
        "BRD-WS-16-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R005-O001",
      "obligation_text": "Secret không được lưu dưới dạng Plain Text"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-16-R005-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Secret không được lưu dưới dạng Plain Text.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-005",
    "previous_temporary_key": "TMP-BRD-WS-16-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "15. Secret Management",
    "source_context_sha256": "14a6650ddc3674e6733d1838f7b37163663d95831323d14dc203b4d7dab54c7b",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "bb7f6387a9e545ae525ed99c44cf792e70fb1c8fd3db2d195090a9bc32d9e46b",
    "source_lines": "L390",
    "source_section": "15. Secret Management"
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
  "stable_id": "BRD-WS-16-R005",
  "title": "Secret không được lưu dưới dạng Plain Text",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R006 — Audit Log chỉ được phép đọc

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R006-AC001",
      "given": "an operational task within the scope of Audit Log chỉ được phép đọc",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-16-R006-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-16-R006-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Audit Log chỉ được phép đọc",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-16-R006-O001"
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
        "BRD-WS-16-R006-AC001",
        "BRD-WS-16-R006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R006-O001",
      "obligation_text": "Audit Log chỉ được phép đọc"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R006 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R006 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R006-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Audit Log chỉ được phép đọc.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-006",
    "previous_temporary_key": "TMP-BRD-WS-16-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Audit Logging",
    "source_context_sha256": "c3a223ed8456790c07473f29edd0f53592bcc7df96f85b5cef84a1546f158902",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "5b1e2df25c21481767865381aea37f1835ce20b091ab2c6b581e4eed2f8c0434",
    "source_lines": "L450",
    "source_section": "18. Audit Logging"
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
  "stable_id": "BRD-WS-16-R006",
  "title": "Audit Log chỉ được phép đọc",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R007 — Không được phép chỉnh sửa hoặc xóa trực tiếp

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R007-AC001",
      "given": "the applicable business context, actor, and input for Không được phép chỉnh sửa hoặc xóa trực tiếp",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-16-R007-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-16-R007-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Không được phép chỉnh sửa hoặc xóa trực tiếp",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-16-R007-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R007-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Không được phép chỉnh sửa hoặc xóa trực tiếp",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-16-R007-O001"
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
        "BRD-WS-16-R007-AC001",
        "BRD-WS-16-R007-AC002",
        "BRD-WS-16-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R007-O001",
      "obligation_text": "Không được phép chỉnh sửa hoặc xóa trực tiếp"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-16-R007-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R007-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không được phép chỉnh sửa hoặc xóa trực tiếp.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-007",
    "previous_temporary_key": "TMP-BRD-WS-16-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Audit Logging",
    "source_context_sha256": "c3a223ed8456790c07473f29edd0f53592bcc7df96f85b5cef84a1546f158902",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "05f1ee6e083ef88c3b6dc032e51b2e644e902a9289d9f3f6d89f81bfeb258330",
    "source_lines": "L452",
    "source_section": "18. Audit Logging"
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
  "stable_id": "BRD-WS-16-R007",
  "title": "Không được phép chỉnh sửa hoặc xóa trực tiếp",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R008 — Privacy Protection tuân thủ Compliance Policy và Security Policy

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "BRD-WS-16-R008-AC001",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Privacy Protection tuân thủ Compliance Policy và Security Policy",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "BRD-WS-16-R008-O001"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "PRIVACY_POLICY_DENIAL_V1",
      "criterion_id": "BRD-WS-16-R008-AC002",
      "given": "a data action whose purpose, consent, scope, or effective policy does not permit the requested data use under Privacy Protection tuân thủ Compliance Policy và Security Policy",
      "observable_evidence": "actor, purpose, consent and scope, effective policies, denial reason, exposed-data comparison, and audit record",
      "then": "the data action is denied, no additional protected data is exposed or changed, and the policy reason is audited",
      "verifies": [
        "BRD-WS-16-R008-O001"
      ],
      "when": "privacy conformance is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R008-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Privacy Protection tuân thủ Compliance Policy và Security Policy",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-16-R008-O001"
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
        "BRD-WS-16-R008-AC001",
        "BRD-WS-16-R008-AC002",
        "BRD-WS-16-R008-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R008-O001",
      "obligation_text": "Privacy Protection tuân thủ Compliance Policy và Security Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R008 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R008 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R008 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-16-R008-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R008-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R008 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Privacy Protection tuân thủ Compliance Policy và Security Policy.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-008",
    "previous_temporary_key": "TMP-BRD-WS-16-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "20. Privacy Protection",
    "source_context_sha256": "8c4487e761be8cd1fc9f35b9aaf6ab86e769fd621880eeffec2d39cd985c1792",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "d65bc83f5e5e25e2eafdbfafd330a6eb95b75520bdf76b53b3ecc65930633eb7",
    "source_lines": "L489",
    "source_section": "20. Privacy Protection"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R008",
  "title": "Privacy Protection tuân thủ Compliance Policy và Security Policy",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R010 — Mọi đánh giá Permission đều phải đi qua Permission Evaluation Engine

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R010-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Mọi đánh giá Permission đều phải đi qua Permission Evaluation Engine",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BRD-WS-16-R010-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R010-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Mọi đánh giá Permission đều phải đi qua Permission Evaluation Engine",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-16-R010-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R010-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Mọi đánh giá Permission đều phải đi qua Permission Evaluation Engine",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-16-R010-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BRD-WS-16-R010-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Mọi đánh giá Permission đều phải đi qua Permission Evaluation Engine",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BRD-WS-16-R010-O001"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-16-R010-AC001",
        "BRD-WS-16-R010-AC002",
        "BRD-WS-16-R010-AC003",
        "BRD-WS-16-R010-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R010-O001",
      "obligation_text": "Mọi đánh giá Permission đều phải đi qua Permission Evaluation Engine"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BRD-WS-16-R010-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R010 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R010 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-16-R010-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R010-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R010 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi đánh giá Permission đều phải đi qua Permission Evaluation Engine.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-010",
    "previous_temporary_key": "TMP-BRD-WS-16-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "26. Permission Evaluation Engine",
    "source_context_sha256": "402f52e10aa02d37c06ea1e68cdf503a4e3d105037834ecbdd82428c3cd33ded",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "25e19b2a4d1740fe9c741a21e86c9245bf0c634c0ae12fccaf7ba20344dbe3dd",
    "source_lines": "L638",
    "source_section": "26. Permission Evaluation Engine"
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
  "stable_id": "BRD-WS-16-R010",
  "title": "Mọi đánh giá Permission đều phải đi qua Permission Evaluation Engine",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R011 — Security Policy không được Hard-code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R011-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Security Policy không được Hard-code",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the prohibited security decision path produces no effective permission or protected-state change, and conformance evidence identifies the attempted bypass",
      "verifies": [
        "BRD-WS-16-R011-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R011-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Security Policy không được Hard-code",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-16-R011-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R011-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Security Policy không được Hard-code",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-16-R011-O001"
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
        "BRD-WS-16-R011-AC001",
        "BRD-WS-16-R011-AC002",
        "BRD-WS-16-R011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R011-O001",
      "obligation_text": "Security Policy không được Hard-code"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R011 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R011 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R011 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-16-R011-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R011-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R011 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Security Policy không được Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-011",
    "previous_temporary_key": "TMP-BRD-WS-16-011",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "27. Security Policy",
    "source_context_sha256": "0994ea9a1e4c603b96e321b12126ab92e5272fbb18e5a83932e55c88b1836a05",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "2909b3d7d18d5f7c670bed650c9cf5306087c5c7857f30506c0ba837c519f14a",
    "source_lines": "L665",
    "source_section": "27. Security Policy"
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
  "stable_id": "BRD-WS-16-R011",
  "title": "Security Policy không được Hard-code",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R012 — Identity Federation cho phép Organization sử dụng hệ thống Identity hiện có mà không cần tạo lại…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R012-AC001",
      "given": "the applicable business context, actor, and input for Identity Federation cho phép Organization sử dụng hệ thống Identity hiện có mà không cần tạo lại…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-16-R012-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-16-R012-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Identity Federation cho phép Organization sử dụng hệ thống Identity hiện có mà không cần tạo lại…",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-16-R012-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R012-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Identity Federation cho phép Organization sử dụng hệ thống Identity hiện có mà không cần tạo lại…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-16-R012-O001"
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
        "BRD-WS-16-R012-AC001",
        "BRD-WS-16-R012-AC002",
        "BRD-WS-16-R012-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R012-O001",
      "obligation_text": "Identity Federation cho phép Organization sử dụng hệ thống Identity hiện có mà không cần tạo lại User trên YSim"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R012 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R012 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R012 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-16-R012-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R012-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R012 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Identity Federation cho phép Organization sử dụng hệ thống Identity hiện có mà không cần tạo lại User trên YSim.",
  "provenance": {
    "approved_decision_contracts": {
      "P2-DEC-001": {
        "decision_id": "P2-DEC-001",
        "sections": [
          {
            "heading": "Approved scope",
            "items": [
              "Protocols are OIDC Authorization Code with PKCE and SAML 2.0 Web Browser SSO.",
              "YSim acts as relying party/service provider.",
              "Federation applies to Organization, Agency, and limited Partner workforce portals.",
              "Platform Admin federation uses a separate YSim-operator trust.",
              "Customer Portal and Storefront authentication are outside enterprise federation."
            ]
          },
          {
            "heading": "Identity and claims",
            "items": [
              "The immutable federation identity key is Organization + Issuer + Subject.",
              "Email is not an immutable identity key and may be consumed only when verified.",
              "Claims use an allowlist.",
              "JIT provisioning follows Organization policy and defaults to least privilege.",
              "JIT provisioning must not assign privileged roles."
            ]
          },
          {
            "heading": "Assurance and policy",
            "items": [
              "Privileged roles must still meet MFA assurance; YSim performs step-up when IdP assurance is insufficient.",
              "Organization policy is LOCAL_ALLOWED, FEDERATION_OPTIONAL, or FEDERATION_REQUIRED.",
              "FEDERATION_REQUIRED retains a controlled, audited break-glass recovery account."
            ]
          },
          {
            "heading": "Linking, validation, lifecycle, and audit",
            "items": [
              "Account linking requires an authenticated existing session or admin approval.",
              "A privileged account must never be auto-linked by email.",
              "Signature, issuer, audience, time, nonce/replay, and tenant binding are validated fail-closed.",
              "Disabling a trust or User blocks new login and revokes sessions according to policy.",
              "Audit covers login, failure, JIT, link/unlink, conflict, and trust changes."
            ]
          },
          {
            "heading": "Out of v2.3",
            "items": [
              "Outbound IdP.",
              "SCIM.",
              "Cross-Organization federation linking.",
              "Automatic privileged-role assignment."
            ]
          }
        ],
        "selected_option": 1,
        "status": "DECIDED_PENDING_PACK_APPROVAL",
        "title": "Inbound workforce federation"
      }
    },
    "approved_decisions": [
      "P2-DEC-001",
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-012",
    "previous_temporary_key": "TMP-BRD-WS-16-012",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Identity Federation",
    "source_context_sha256": "79bf64ca17e2729d4ed0d69b3e1c1637fdcc8ad8d217df27372de3d0eec305a5",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
    "source_lines": "L681",
    "source_section": "28. Identity Federation"
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
  "stable_id": "BRD-WS-16-R012",
  "title": "Identity Federation cho phép Organization sử dụng hệ thống Identity hiện có mà không cần tạo lại…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R013 — Sau thời gian này: - Audit được Archive

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R013-AC001",
      "given": "an operational task within the scope of Sau thời gian này: - Audit được Archive",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-16-R013-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-16-R013-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Sau thời gian này: - Audit được Archive",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-16-R013-O001"
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
        "BRD-WS-16-R013-AC001",
        "BRD-WS-16-R013-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R013-O001",
      "obligation_text": "Sau thời gian này: - Audit được Archive"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R013 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R013 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R013 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R013 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R013-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R013 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sau thời gian này: - Audit được Archive",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-16-009"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-013",
    "previous_temporary_key": "TMP-BRD-WS-16-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Audit Retention",
    "source_context_sha256": "4b1929c0009643385713951a5e369bab3e7359126f368a83a9f1080fa43ecd78",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "88528833f051f4faf92eba801f45a615bbedb5f70a520d765b7b907152562384",
    "source_lines": "L597-L602",
    "source_section": "25. Audit Retention"
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
  "stable_id": "BRD-WS-16-R013",
  "title": "Sau thời gian này: - Audit được Archive",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R014 — Sau thời gian này: - Archive chỉ đọc

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R014-AC001",
      "given": "an operational task within the scope of Sau thời gian này: - Archive chỉ đọc",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BRD-WS-16-R014-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BRD-WS-16-R014-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Sau thời gian này: - Archive chỉ đọc",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BRD-WS-16-R014-O001"
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
        "BRD-WS-16-R014-AC001",
        "BRD-WS-16-R014-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R014-O001",
      "obligation_text": "Sau thời gian này: - Archive chỉ đọc"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R014 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R014 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R014 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R014 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R014-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R014 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sau thời gian này: - Archive chỉ đọc",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-16-009"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-014",
    "previous_temporary_key": "TMP-BRD-WS-16-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Audit Retention",
    "source_context_sha256": "4b1929c0009643385713951a5e369bab3e7359126f368a83a9f1080fa43ecd78",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "88528833f051f4faf92eba801f45a615bbedb5f70a520d765b7b907152562384",
    "source_lines": "L597-L602",
    "source_section": "25. Audit Retention"
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
  "stable_id": "BRD-WS-16-R014",
  "title": "Sau thời gian này: - Archive chỉ đọc",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R015 — Sau thời gian này: - Không được chỉnh sửa

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R015-AC001",
      "given": "the applicable business context, actor, and input for Sau thời gian này: - Không được chỉnh sửa",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-16-R015-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-16-R015-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Sau thời gian này: - Không được chỉnh sửa",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-16-R015-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R015-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Sau thời gian này: - Không được chỉnh sửa",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-16-R015-O001"
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
        "BRD-WS-16-R015-AC001",
        "BRD-WS-16-R015-AC002",
        "BRD-WS-16-R015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R015-O001",
      "obligation_text": "Sau thời gian này: - Không được chỉnh sửa"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R015 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R015 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R015 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-16-R015-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R015-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R015 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sau thời gian này: - Không được chỉnh sửa",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-16-009"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-015",
    "previous_temporary_key": "TMP-BRD-WS-16-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Audit Retention",
    "source_context_sha256": "4b1929c0009643385713951a5e369bab3e7359126f368a83a9f1080fa43ecd78",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "88528833f051f4faf92eba801f45a615bbedb5f70a520d765b7b907152562384",
    "source_lines": "L597-L602",
    "source_section": "25. Audit Retention"
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
  "stable_id": "BRD-WS-16-R015",
  "title": "Sau thời gian này: - Không được chỉnh sửa",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R016 — Sau thời gian này: - Không được xóa trực tiếp

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-16-R016-AC001",
      "given": "the applicable business context, actor, and input for Sau thời gian này: - Không được xóa trực tiếp",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-16-R016-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BRD-WS-16-R016-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Sau thời gian này: - Không được xóa trực tiếp",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BRD-WS-16-R016-O001"
      ],
      "when": "the governing policy, rule, calculation, transition, or action is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-16-R016-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Sau thời gian này: - Không được xóa trực tiếp",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BRD-WS-16-R016-O001"
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
        "BRD-WS-16-R016-AC001",
        "BRD-WS-16-R016-AC002",
        "BRD-WS-16-R016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R016-O001",
      "obligation_text": "Sau thời gian này: - Không được xóa trực tiếp"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R016 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R016 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R016 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BRD-WS-16-R016-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-16-R016-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-16-R016 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sau thời gian này: - Không được xóa trực tiếp",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-WS-16-009"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-016",
    "previous_temporary_key": "TMP-BRD-WS-16-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Audit Retention",
    "source_context_sha256": "4b1929c0009643385713951a5e369bab3e7359126f368a83a9f1080fa43ecd78",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "88528833f051f4faf92eba801f45a615bbedb5f70a520d765b7b907152562384",
    "source_lines": "L597-L602",
    "source_section": "25. Audit Retention"
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
  "stable_id": "BRD-WS-16-R016",
  "title": "Sau thời gian này: - Không được xóa trực tiếp",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-16-001 — Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: - Customer - User - Organiz…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EP-16-001-AC001",
      "given": "a contract interaction at the integration boundary defined by Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: - Customer - User - Organiz…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EP-16-001-O001"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EP-16-001-AC002",
      "given": "a contract interaction at the integration boundary defined by Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: - Customer - User - Organiz…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EP-16-001-O002"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EP-16-001-AC003",
      "given": "a contract interaction at the integration boundary defined by Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: - Customer - User - Organiz…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EP-16-001-O003"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EP-16-001-AC004",
      "given": "a contract interaction at the integration boundary defined by Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: - Customer - User - Organiz…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EP-16-001-O004"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "INTEGRATION_BOUNDARY_OBSERVATION_V1",
      "criterion_id": "EP-16-001-AC005",
      "given": "a contract interaction at the integration boundary defined by Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: - Customer - User - Organiz…",
      "observable_evidence": "contract validation result, boundary ownership record, external outcome, and reconciliation evidence where the contract requires it",
      "then": "the interaction is accepted only at the declared boundary, names the responsible owner, and exposes the external outcome or reconciliation result required by the contract",
      "verifies": [
        "EP-16-001-O005"
      ],
      "when": "a conforming interaction is submitted and its ownership boundary is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "INTEGRATION_CONTRACT_REJECTION_V1",
      "criterion_id": "EP-16-001-AC006",
      "given": "an interaction that violates the contract or ownership boundary for Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: - Customer - User - Organiz…",
      "observable_evidence": "contract rejection or reconciliation result, reason, boundary owner, and external outcome",
      "then": "the interaction is rejected or reconciled according to the declared contract without transferring ownership to the wrong boundary",
      "verifies": [
        "EP-16-001-O001",
        "EP-16-001-O002",
        "EP-16-001-O003",
        "EP-16-001-O004",
        "EP-16-001-O005"
      ],
      "when": "the interaction reaches the integration boundary"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-16-001-AC007",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: - Customer - User - Organiz…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-16-001-O001",
        "EP-16-001-O002",
        "EP-16-001-O003",
        "EP-16-001-O004",
        "EP-16-001-O005"
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
        "EP-16-001-AC001",
        "EP-16-001-AC006",
        "EP-16-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-001-O001",
      "obligation_text": "Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: Customer."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-001-AC002",
        "EP-16-001-AC006",
        "EP-16-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-001-O002",
      "obligation_text": "Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: User."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-001-AC003",
        "EP-16-001-AC006",
        "EP-16-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-001-O003",
      "obligation_text": "Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: Organization Owner."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-001-AC004",
        "EP-16-001-AC006",
        "EP-16-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-001-O004",
      "obligation_text": "Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: API Client."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-001-AC005",
        "EP-16-001-AC006",
        "EP-16-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-001-O005",
      "obligation_text": "Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: Service Account."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-16-001 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-16-001 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-16-001 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-16-001-AC007"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-16-001-AC001",
        "EP-16-001-AC002",
        "EP-16-001-AC003",
        "EP-16-001-AC004",
        "EP-16-001-AC005"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-16-001 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: - Customer - User - Organization Owner - API Client - Service Account",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-16-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Identity Platform",
    "source_context_sha256": "ca12b94f6cb8f68e320a33d7aac6af2a3ebdccbb25d4606c21fddb218b322bd9",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "3e8ee6404b7968118a8ba2a1a34a862adc4eb88f87a2bd88690f14a1c201a397",
    "source_lines": "L1057-L1068",
    "source_section": "32. Enterprise Design Principles > EP-16-001"
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
  "stable_id": "EP-16-001",
  "title": "Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: - Customer - User - Organiz…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-16-002 — Permission được đánh giá động. Không sử dụng Permission tĩnh

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-16-002-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission được đánh giá động. Không sử dụng Permission tĩnh",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the permission decision is recalculated from the current applicable attributes and policy; changing a governing input changes the effective decision without relying on a stored static permission result",
      "verifies": [
        "EP-16-002-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-16-002-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission được đánh giá động. Không sử dụng Permission tĩnh",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the permission decision is recalculated from the current applicable attributes and policy; changing a governing input changes the effective decision without relying on a stored static permission result",
      "verifies": [
        "EP-16-002-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "EP-16-002-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Permission được đánh giá động. Không sử dụng Permission tĩnh",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "EP-16-002-O001",
        "EP-16-002-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-16-002-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Permission được đánh giá động. Không sử dụng Permission tĩnh",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-16-002-O001",
        "EP-16-002-O002"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "EP-16-002-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Permission được đánh giá động. Không sử dụng Permission tĩnh",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "EP-16-002-O001",
        "EP-16-002-O002"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-16-002-AC001",
        "EP-16-002-AC003",
        "EP-16-002-AC004",
        "EP-16-002-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-002-O001",
      "obligation_text": "Permission được đánh giá động"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-002-AC002",
        "EP-16-002-AC003",
        "EP-16-002-AC004",
        "EP-16-002-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-002-O002",
      "obligation_text": "Không sử dụng Permission tĩnh"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "EP-16-002-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-16-002 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-16-002 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-16-002-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-16-002-AC001",
        "EP-16-002-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-16-002 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission được đánh giá động. Không sử dụng Permission tĩnh.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-16-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-004",
    "source_context_sha256": "77b0cfa84c4e704817978bcecffba11c5727d8c5573504da4749ba48cd521894",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "2d637f8d85f7b28aff039a2fee165c0fc5fa51900c50a26db7ae456389f8502d",
    "source_lines": "L1071-L1076",
    "source_section": "32. Enterprise Design Principles > EP-16-002"
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
  "stable_id": "EP-16-002",
  "title": "Permission được đánh giá động. Không sử dụng Permission tĩnh",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-16-003 — Permission Evaluation Engine là điểm đánh giá Permission duy nhất. Business Domain không tự xử l…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-16-003-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission Evaluation Engine là điểm đánh giá Permission duy nhất. Business Domain không tự xử l…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the permission decision trace identifies Permission Evaluation Engine as the sole decision authority and contains no independent Business Domain permission decision",
      "verifies": [
        "EP-16-003-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-16-003-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission Evaluation Engine là điểm đánh giá Permission duy nhất. Business Domain không tự xử l…",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "EP-16-003-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "EP-16-003-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Permission Evaluation Engine là điểm đánh giá Permission duy nhất. Business Domain không tự xử l…",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "EP-16-003-O001",
        "EP-16-003-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-16-003-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Permission Evaluation Engine là điểm đánh giá Permission duy nhất. Business Domain không tự xử l…",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-16-003-O001",
        "EP-16-003-O002"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "EP-16-003-AC005",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Permission Evaluation Engine là điểm đánh giá Permission duy nhất. Business Domain không tự xử l…",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "EP-16-003-O001",
        "EP-16-003-O002"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-16-003-AC001",
        "EP-16-003-AC003",
        "EP-16-003-AC004",
        "EP-16-003-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-003-O001",
      "obligation_text": "Permission Evaluation Engine là điểm đánh giá Permission duy nhất"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-003-AC002",
        "EP-16-003-AC003",
        "EP-16-003-AC004",
        "EP-16-003-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-003-O002",
      "obligation_text": "Business Domain không tự xử lý Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "EP-16-003-AC005"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-16-003 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-16-003 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-16-003-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-16-003-AC001",
        "EP-16-003-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-16-003 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission Evaluation Engine là điểm đánh giá Permission duy nhất. Business Domain không tự xử lý Permission.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-16-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-003",
    "source_context_sha256": "14158c7c83a2fd98e7e443bd60e1a3b381c668a9f3ee103936fe69829f594d3f",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "15bbbf22ee1bffd4d09f87b616f064a16c9580c221642b3ca39d384af4514108",
    "source_lines": "L1079-L1084",
    "source_section": "32. Enterprise Design Principles > EP-16-003"
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
  "stable_id": "EP-16-003",
  "title": "Permission Evaluation Engine là điểm đánh giá Permission duy nhất. Business Domain không tự xử l…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-16-004 — Security Policy được cấu hình. Không Hard-code

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-16-004-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Security Policy được cấu hình. Không Hard-code",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "EP-16-004-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-16-004-AC002",
      "given": "an identified principal, applicable assurance context, and policy inputs for Security Policy được cấu hình. Không Hard-code",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "EP-16-004-O002"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "EP-16-004-AC003",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Security Policy được cấu hình. Không Hard-code",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "EP-16-004-O001",
        "EP-16-004-O002"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-16-004-AC004",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Security Policy được cấu hình. Không Hard-code",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-16-004-O001",
        "EP-16-004-O002"
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
        "EP-16-004-AC001",
        "EP-16-004-AC003",
        "EP-16-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-004-O001",
      "obligation_text": "Security Policy được cấu hình"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-004-AC002",
        "EP-16-004-AC003",
        "EP-16-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-004-O002",
      "obligation_text": "Không Hard-code"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-16-004 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-16-004 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-16-004 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-16-004-AC004"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-16-004-AC001",
        "EP-16-004-AC002"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-16-004 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Security Policy được cấu hình. Không Hard-code.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-16-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-004",
    "source_context_sha256": "deade9814f06b2df96bceb95845bd276ac8f61d080c4acde3a57feb6e758eb43",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "bfe2145868ac193af615958fbe4dcabb58759193f65a53201a65000eb94a2e28",
    "source_lines": "L1087-L1092",
    "source_section": "32. Enterprise Design Principles > EP-16-004"
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
  "stable_id": "EP-16-004",
  "title": "Security Policy được cấu hình. Không Hard-code",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-16-005 — Platform áp dụng Zero Trust Principle. Không có Request nào được mặc định tin cậy

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-16-005-AC001",
      "given": "the applicable business context, actor, and input for Platform áp dụng Zero Trust Principle. Không có Request nào được mặc định tin cậy",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-16-005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "EP-16-005-AC002",
      "given": "the applicable business context, actor, and input for Platform áp dụng Zero Trust Principle. Không có Request nào được mặc định tin cậy",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "EP-16-005-O002"
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
        "EP-16-005-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-005-O001",
      "obligation_text": "Platform áp dụng Zero Trust Principle"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-005-O002",
      "obligation_text": "Không có Request nào được mặc định tin cậy"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Platform áp dụng Zero Trust Principle. Không có Request nào được mặc định tin cậy.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-16-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-029",
    "source_context_sha256": "61a8613b355c91eb9ac3f561abb2caaa5ac01cf0ee115e5c7673d3a53488c189",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
    "source_lines": "L1095-L1100",
    "source_section": "32. Enterprise Design Principles > EP-16-005"
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
  "stable_id": "EP-16-005",
  "title": "Platform áp dụng Zero Trust Principle. Không có Request nào được mặc định tin cậy",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-16-006 — Data Protection được quyết định bởi: - Permission - Data Scope - Data Classification - Customer …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-006-AC001",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Data Protection được quyết định bởi: - Permission - Data Scope - Data Classification - Customer …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-006-O001"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-006-AC002",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Data Protection được quyết định bởi: - Permission - Data Scope - Data Classification - Customer …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-006-O002"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-006-AC003",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Data Protection được quyết định bởi: - Permission - Data Scope - Data Classification - Customer …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-006-O003"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-006-AC004",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Data Protection được quyết định bởi: - Permission - Data Scope - Data Classification - Customer …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-006-O004"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-006-AC005",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Data Protection được quyết định bởi: - Permission - Data Scope - Data Classification - Customer …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-006-O005"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "PRIVACY_POLICY_DENIAL_V1",
      "criterion_id": "EP-16-006-AC006",
      "given": "a data action whose purpose, consent, scope, or effective policy does not permit the requested data use under Data Protection được quyết định bởi: - Permission - Data Scope - Data Classification - Customer …",
      "observable_evidence": "actor, purpose, consent and scope, effective policies, denial reason, exposed-data comparison, and audit record",
      "then": "the data action is denied, no additional protected data is exposed or changed, and the policy reason is audited",
      "verifies": [
        "EP-16-006-O001",
        "EP-16-006-O002",
        "EP-16-006-O003",
        "EP-16-006-O004",
        "EP-16-006-O005"
      ],
      "when": "privacy conformance is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-16-006-AC007",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Data Protection được quyết định bởi: - Permission - Data Scope - Data Classification - Customer …",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-16-006-O001",
        "EP-16-006-O002",
        "EP-16-006-O003",
        "EP-16-006-O004",
        "EP-16-006-O005"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "EP-16-006-AC008",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Data Protection được quyết định bởi: - Permission - Data Scope - Data Classification - Customer …",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "EP-16-006-O001",
        "EP-16-006-O002",
        "EP-16-006-O003",
        "EP-16-006-O004",
        "EP-16-006-O005"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-16-006-AC001",
        "EP-16-006-AC006",
        "EP-16-006-AC007",
        "EP-16-006-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-006-O001",
      "obligation_text": "Data Protection được quyết định bởi: Permission."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-006-AC002",
        "EP-16-006-AC006",
        "EP-16-006-AC007",
        "EP-16-006-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-006-O002",
      "obligation_text": "Data Protection được quyết định bởi: Data Scope."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-006-AC003",
        "EP-16-006-AC006",
        "EP-16-006-AC007",
        "EP-16-006-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-006-O003",
      "obligation_text": "Data Protection được quyết định bởi: Data Classification."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-006-AC004",
        "EP-16-006-AC006",
        "EP-16-006-AC007",
        "EP-16-006-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-006-O004",
      "obligation_text": "Data Protection được quyết định bởi: Customer Consent."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-006-AC005",
        "EP-16-006-AC006",
        "EP-16-006-AC007",
        "EP-16-006-AC008"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-006-O005",
      "obligation_text": "Data Protection được quyết định bởi: Security Policy."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "EP-16-006-AC008"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-16-006 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-16-006 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-16-006-AC007"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-16-006-AC001",
        "EP-16-006-AC002",
        "EP-16-006-AC003",
        "EP-16-006-AC004",
        "EP-16-006-AC005"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-16-006 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Data Protection được quyết định bởi: - Permission - Data Scope - Data Classification - Customer Consent - Security Policy",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-16-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-006",
    "source_context_sha256": "64225a4c132dc3598a812cc8df8ac7fcf23290623f97af4b3ea3b3e8505c5b28",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "5b383d334baef5109420a6fb0cf1bf6eee72378360e25c24eadb44ce45655115",
    "source_lines": "L1103-L1112",
    "source_section": "32. Enterprise Design Principles > EP-16-006"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-16-006",
  "title": "Data Protection được quyết định bởi: - Permission - Data Scope - Data Classification - Customer …",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-16-007 — API Security độc lập với Portal Security

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "EP-16-007-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for API Security độc lập với Portal Security",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "EP-16-007-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "EP-16-007-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for API Security độc lập với Portal Security",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "EP-16-007-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-16-007-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by API Security độc lập với Portal Security",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-16-007-O001"
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
        "EP-16-007-AC001",
        "EP-16-007-AC002",
        "EP-16-007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-007-O001",
      "obligation_text": "API Security độc lập với Portal Security"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "EP-16-007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-16-007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-16-007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-16-007-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-16-007-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-16-007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "API Security độc lập với Portal Security.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-16-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-007",
    "source_context_sha256": "4796589be5e5cfbfe86c994494d7cac324ec09831af72ed0209aacde5a844b56",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "7ba4d69497f7e4aaefd33b7d9e30f4f7d21991bc7bb76fff39b035e5ddea514d",
    "source_lines": "L1115-L1118",
    "source_section": "32. Enterprise Design Principles > EP-16-007"
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
  "stable_id": "EP-16-007",
  "title": "API Security độc lập với Portal Security",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-16-008 — Security Platform Publish Business Event

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
  "normative_statement": "Security Platform Publish Business Event.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-16-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "29. Security Business Events",
    "source_context_sha256": "6bd0565e1d201ed4d938250bfe47c7cda8fc6c1a9bde6f1e0558bdc02dd3c34a",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "a2bc6c93d0b85610b75352bbfe765762ae2475772e3141b596a12ff29ddee8cd",
    "source_lines": "L1121-L1124",
    "source_section": "32. Enterprise Design Principles > EP-16-008"
  },
  "record_kind": "ALIAS",
  "relationships": {
    "alias_of": "BD-16-027",
    "aliases": [],
    "coverage_mode": "CANONICAL",
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-16-008",
  "title": "Security Platform Publish Business Event",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-16-009 — Identity Platform hỗ trợ Federation

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
  "normative_statement": "Identity Platform hỗ trợ Federation.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-001",
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-16-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "28. Identity Federation",
    "source_context_sha256": "79bf64ca17e2729d4ed0d69b3e1c1637fdcc8ad8d217df27372de3d0eec305a5",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "44ade3a53147f36ab3db872b9631aae13370ab7648a00fcb6fb039fcbe75056a",
    "source_lines": "L1127-L1130",
    "source_section": "32. Enterprise Design Principles > EP-16-009"
  },
  "record_kind": "ALIAS",
  "relationships": {
    "alias_of": "BD-16-026",
    "aliases": [],
    "coverage_mode": "CANONICAL",
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-16-009",
  "title": "Identity Platform hỗ trợ Federation",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-16-010 — Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-010-AC001",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-010-O001"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-010-AC002",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-010-O002"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-010-AC003",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-010-O003"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-010-AC004",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-010-O004"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-010-AC005",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-010-O005"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-010-AC006",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-010-O006"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-010-AC007",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-010-O007"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-010-AC008",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-010-O008"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "PRIVACY_POLICY_CONFORMANCE_V1",
      "criterion_id": "EP-16-010-AC009",
      "given": "a data action with actor, purpose, scope, consent where required, and the effective policies for Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
      "observable_evidence": "actor, purpose, scope, consent state where applicable, effective policy versions, allow or deny result, exposed data set, reason, and audit record",
      "then": "the action proceeds only when Compliance Policy and Security Policy permit the stated purpose and scope, with the permitted data outcome and audit evidence aligned",
      "verifies": [
        "EP-16-010-O009"
      ],
      "when": "privacy conformance and the protected data action are evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "PRIVACY_POLICY_DENIAL_V1",
      "criterion_id": "EP-16-010-AC010",
      "given": "a data action whose purpose, consent, scope, or effective policy does not permit the requested data use under Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
      "observable_evidence": "actor, purpose, consent and scope, effective policies, denial reason, exposed-data comparison, and audit record",
      "then": "the data action is denied, no additional protected data is exposed or changed, and the policy reason is audited",
      "verifies": [
        "EP-16-010-O001",
        "EP-16-010-O002",
        "EP-16-010-O003",
        "EP-16-010-O004",
        "EP-16-010-O005",
        "EP-16-010-O006",
        "EP-16-010-O007",
        "EP-16-010-O008",
        "EP-16-010-O009"
      ],
      "when": "privacy conformance is evaluated"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "EP-16-010-AC011",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "EP-16-010-O001",
        "EP-16-010-O002",
        "EP-16-010-O003",
        "EP-16-010-O004",
        "EP-16-010-O005",
        "EP-16-010-O006",
        "EP-16-010-O007",
        "EP-16-010-O008",
        "EP-16-010-O009"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "EP-16-010-AC012",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "EP-16-010-O001",
        "EP-16-010-O002",
        "EP-16-010-O003",
        "EP-16-010-O004",
        "EP-16-010-O005",
        "EP-16-010-O006",
        "EP-16-010-O007",
        "EP-16-010-O008",
        "EP-16-010-O009"
      ],
      "when": "the actor attempts the governed action"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "EP-16-010-AC001",
        "EP-16-010-AC010",
        "EP-16-010-AC011",
        "EP-16-010-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-010-O001",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Identity."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-010-AC002",
        "EP-16-010-AC010",
        "EP-16-010-AC011",
        "EP-16-010-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-010-O002",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Role."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-010-AC003",
        "EP-16-010-AC010",
        "EP-16-010-AC011",
        "EP-16-010-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-010-O003",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Permission."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-010-AC004",
        "EP-16-010-AC010",
        "EP-16-010-AC011",
        "EP-16-010-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-010-O004",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Data Scope."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-010-AC005",
        "EP-16-010-AC010",
        "EP-16-010-AC011",
        "EP-16-010-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-010-O005",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Organization Relationship."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-010-AC006",
        "EP-16-010-AC010",
        "EP-16-010-AC011",
        "EP-16-010-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-010-O006",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Support Policy."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-010-AC007",
        "EP-16-010-AC010",
        "EP-16-010-AC011",
        "EP-16-010-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-010-O007",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Customer Consent."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-010-AC008",
        "EP-16-010-AC010",
        "EP-16-010-AC011",
        "EP-16-010-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-010-O008",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Data Classification."
    },
    {
      "acceptance_criterion_references": [
        "EP-16-010-AC009",
        "EP-16-010-AC010",
        "EP-16-010-AC011",
        "EP-16-010-AC012"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-010-O009",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Security Policy."
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "EP-16-010-AC012"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "EP-16-010 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "EP-16-010 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "EP-16-010-AC011"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "EP-16-010-AC001",
        "EP-16-010-AC002",
        "EP-16-010-AC003",
        "EP-16-010-AC004",
        "EP-16-010-AC005",
        "EP-16-010-AC006",
        "EP-16-010-AC007",
        "EP-16-010-AC008",
        "EP-16-010-AC009"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "EP-16-010 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - Permission - Data Scope - Organization Relationship - Support Policy - Customer Consent - Data Classification - Security Policy",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-16-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-010",
    "source_context_sha256": "1c09cca794138eb3a085b4ae5d2fcfdfff8a1512233750352fe24b0e570d1c62",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "ca6d6e6c157444c582243876a077f8bad3b7efb8a877149c17125e04f7740a02",
    "source_lines": "L1133-L1146",
    "source_section": "32. Enterprise Design Principles > EP-16-010"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": []
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-16-010",
  "title": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
