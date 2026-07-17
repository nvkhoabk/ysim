---
document_code: "BRD-WS-16"
document_id: "BRD-WS-16"
title: "Identity, Security, Authorization, Audit & Compliance"
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

Security Platform phải publish Security Business Event theo Versioned Security Event Catalog quản trị event type, trigger, correlation và payload contract; requirement này không thiết lập danh sách event cố định và không khẳng định runtime implementation.

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

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-001 — Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Fa…

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
  "normative_statement": "Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Facebook - Microsoft - Line - WeChat Kiến trúc hỗ trợ mở rộng thêm Identity Provider trong tương lai.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-007",
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-001",
    "phase_2c_c3_actions": [
      "C3_APPROVED_DECISION_COMPOSITE_SPLIT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Identity Platform",
    "source_context_sha256": "ca12b94f6cb8f68e320a33d7aac6af2a3ebdccbb25d4606c21fddb218b322bd9",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "14b25379eba6c6c0873a75bb6a7142b583f27a954b2ce1b1963f35db2c922273",
    "source_fingerprint_before_c3": "0541d21d79f5ae0be70c2a668f13d7eb511d72a99e9edfd6d5f6c4524a68ff4f",
    "source_lines": "L1297-L1358",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-001"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-16-R038",
      "BRD-WS-16-R039"
    ]
  },
  "requirement_type": "BUSINESS_DECISION",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-16-001",
  "title": "Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Fa…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-002 — Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OID…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-001"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-002",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "c3ff6fa31fdae6b9e2862000bffb7044437db26be69c7f6aba405773254bde58"
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
        "BD-16-002-AC001",
        "BD-16-002-AC009",
        "BD-16-002-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O001",
      "obligation_text": "Authentication hỗ trợ: Password"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC002",
        "BD-16-002-AC009",
        "BD-16-002-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O002",
      "obligation_text": "Authentication hỗ trợ: Email OTP"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC003",
        "BD-16-002-AC009",
        "BD-16-002-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O003",
      "obligation_text": "Authentication hỗ trợ: SMS OTP"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC004",
        "BD-16-002-AC009",
        "BD-16-002-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O004",
      "obligation_text": "Authentication hỗ trợ: Passkey"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC005",
        "BD-16-002-AC009",
        "BD-16-002-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O005",
      "obligation_text": "Authentication hỗ trợ: OAuth2"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC006",
        "BD-16-002-AC009",
        "BD-16-002-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O006",
      "obligation_text": "Authentication hỗ trợ: OpenID Connect (OIDC)"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC007",
        "BD-16-002-AC009",
        "BD-16-002-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O007",
      "obligation_text": "Authentication hỗ trợ: SAML"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-002-AC008",
        "BD-16-002-AC009",
        "BD-16-002-AC010"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-002-O008",
      "obligation_text": "Authentication hỗ trợ: API Key Authentication Method được cấu hình"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-002-AC010"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-002-AC009"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-002-AC001",
        "BD-16-002-AC002",
        "BD-16-002-AC003",
        "BD-16-002-AC004",
        "BD-16-002-AC005",
        "BD-16-002-AC006",
        "BD-16-002-AC007",
        "BD-16-002-AC008"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-002 does not define a recovery obligation."
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
    "source_fingerprint": "c3ff6fa31fdae6b9e2862000bffb7044437db26be69c7f6aba405773254bde58",
    "source_lines": "L1360-L1551",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-003",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "06618f41661fb85c9033fc48c0da0334d1b3c0f3a91281a7fa9246859ab37f08"
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
        "BD-16-003-AC001",
        "BD-16-003-AC006",
        "BD-16-003-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-003-O001",
      "obligation_text": "Platform hỗ trợ Multi-Factor Authentication (MFA). MFA có thể áp dụng theo: Platform"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-003-AC002",
        "BD-16-003-AC006",
        "BD-16-003-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-003-O002",
      "obligation_text": "Platform hỗ trợ Multi-Factor Authentication (MFA). MFA có thể áp dụng theo: Organization"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-003-AC003",
        "BD-16-003-AC006",
        "BD-16-003-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-003-O003",
      "obligation_text": "Platform hỗ trợ Multi-Factor Authentication (MFA). MFA có thể áp dụng theo: Role"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-003-AC004",
        "BD-16-003-AC006",
        "BD-16-003-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-003-O004",
      "obligation_text": "Platform hỗ trợ Multi-Factor Authentication (MFA). MFA có thể áp dụng theo: User"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-003-AC005",
        "BD-16-003-AC006",
        "BD-16-003-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-003-O005",
      "obligation_text": "Platform hỗ trợ Multi-Factor Authentication (MFA). MFA có thể áp dụng theo: API Client"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-003-AC007"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-003-AC006"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-003-AC001",
        "BD-16-003-AC002",
        "BD-16-003-AC003",
        "BD-16-003-AC004",
        "BD-16-003-AC005"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-003 does not define a recovery obligation."
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
    "source_fingerprint": "06618f41661fb85c9033fc48c0da0334d1b3c0f3a91281a7fa9246859ab37f08",
    "source_lines": "L1553-L1711",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-004",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "9153aa1c8ef3df49f95ddcb2510f96cd6d028e33b69c107dcd995ee909824f5e"
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
        "BD-16-004-AC001",
        "BD-16-004-AC003",
        "BD-16-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-004-O001",
      "obligation_text": "Authorization sử dụng mô hình kết hợp: RBAC"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-004-AC002",
        "BD-16-004-AC003",
        "BD-16-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-004-O002",
      "obligation_text": "Authorization sử dụng mô hình kết hợp: ABAC Permission được đánh giá động"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-004-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-004-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-004-AC001",
        "BD-16-004-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-004 does not define a recovery obligation."
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
    "source_fingerprint": "9153aa1c8ef3df49f95ddcb2510f96cd6d028e33b69c107dcd995ee909824f5e",
    "source_lines": "L1713-L1834",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-004"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-005",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "8bd1439067e763b51c8734132087c9fdf10c95edb7bf9104a535dd71330a322f"
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
        "BD-16-005-AC001",
        "BD-16-005-AC003",
        "BD-16-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-005-O001",
      "obligation_text": "Permission là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-005-AC002",
        "BD-16-005-AC003",
        "BD-16-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-005-O002",
      "obligation_text": "Permission không được Hard-code"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-005-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-005-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-005-AC001",
        "BD-16-005-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-005 does not define a recovery obligation."
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
    "source_fingerprint": "8bd1439067e763b51c8734132087c9fdf10c95edb7bf9104a535dd71330a322f",
    "source_lines": "L1836-L1957",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-005"
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
  "normative_statement": "Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Storefront - Customer Portal - User",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-006",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-006",
    "source_context_sha256": "f07eaa73f91bac65267fd0ce84085c9976ac9a47f2daf786e9d6b4f500317bb7",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "3ba4c30c163f6ca2e88fb21f912d29875c5425a2b57d467f2d560f66eb406493",
    "source_fingerprint_before_c3": "d0598fbf0bc728157230ccd378cda70e59a8ae6da7ee1d559feae44154c28d36",
    "source_lines": "L1959-L2027",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-006"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-16-R017",
      "BRD-WS-16-R018",
      "BRD-WS-16-R019",
      "BRD-WS-16-R020",
      "BRD-WS-16-R021",
      "BRD-WS-16-R022",
      "BRD-WS-16-R023"
    ],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R024"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-16-006",
  "title": "Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Stor…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-007 — Permission hỗ trợ Data Scope. Data Scope được kết hợp với: - Organization Relationship - Support…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-007",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "16525f1e33257424164b85a0dffd46ec6f6a625b68a33db6e7e477c9daafc187"
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
        "BD-16-007-AC001",
        "BD-16-007-AC005",
        "BD-16-007-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-007-O001",
      "obligation_text": "Permission hỗ trợ Data Scope. Data Scope được kết hợp với: Organization Relationship"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-007-AC002",
        "BD-16-007-AC005",
        "BD-16-007-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-007-O002",
      "obligation_text": "Permission hỗ trợ Data Scope. Data Scope được kết hợp với: Support Policy"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-007-AC003",
        "BD-16-007-AC005",
        "BD-16-007-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-007-O003",
      "obligation_text": "Permission hỗ trợ Data Scope. Data Scope được kết hợp với: Capability"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-007-AC004",
        "BD-16-007-AC005",
        "BD-16-007-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-007-O004",
      "obligation_text": "Permission hỗ trợ Data Scope. Data Scope được kết hợp với: Security Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-007-AC006"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-007-AC005"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-007-AC001",
        "BD-16-007-AC002",
        "BD-16-007-AC003",
        "BD-16-007-AC004"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-007 does not define a recovery obligation."
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
    "source_fingerprint": "16525f1e33257424164b85a0dffd46ec6f6a625b68a33db6e7e477c9daafc187",
    "source_lines": "L2029-L2176",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-008",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "9deb4659e8a3e4fd30be446e594c01b880b845f23e6a9706f305c88df0a4f266"
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
        "BD-16-008-AC001",
        "BD-16-008-AC003",
        "BD-16-008-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-008-O001",
      "obligation_text": "Platform hỗ trợ Field-Level Permission"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-008-AC002",
        "BD-16-008-AC003",
        "BD-16-008-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-008-O002",
      "obligation_text": "Permission có thể áp dụng tới từng Field"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-008-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-008-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-008-AC001",
        "BD-16-008-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-008 does not define a recovery obligation."
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
    "source_fingerprint": "9deb4659e8a3e4fd30be446e594c01b880b845f23e6a9706f305c88df0a4f266",
    "source_lines": "L2178-L2299",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-009",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "ae9f8a064e9d15323e0d4fa60ce62ce6cc400e40df662210ce91b5510e116101"
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
        "BD-16-009-AC001",
        "BD-16-009-AC005",
        "BD-16-009-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-009-O001",
      "obligation_text": "Platform hỗ trợ Data Masking. Masking được quyết định bởi: Permission"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-009-AC002",
        "BD-16-009-AC005",
        "BD-16-009-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-009-O002",
      "obligation_text": "Platform hỗ trợ Data Masking. Masking được quyết định bởi: Data Classification"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-009-AC003",
        "BD-16-009-AC005",
        "BD-16-009-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-009-O003",
      "obligation_text": "Platform hỗ trợ Data Masking. Masking được quyết định bởi: Customer Consent"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-009-AC004",
        "BD-16-009-AC005",
        "BD-16-009-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-009-O004",
      "obligation_text": "Platform hỗ trợ Data Masking. Masking được quyết định bởi: Security Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-009-AC006"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-009 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-009 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-009-AC005"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-009-AC001",
        "BD-16-009-AC002",
        "BD-16-009-AC003",
        "BD-16-009-AC004"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-009 does not define a recovery obligation."
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
    "source_fingerprint": "ae9f8a064e9d15323e0d4fa60ce62ce6cc400e40df662210ce91b5510e116101",
    "source_lines": "L2301-L2448",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-010",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "d8461f7891030eda804da02eb18688cb42cdb3ab7b2242001b42491c6eb22e1e"
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
        "BD-16-010-AC001",
        "BD-16-010-AC004",
        "BD-16-010-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-010-O001",
      "obligation_text": "Platform hỗ trợ Customer Consent. Customer có quyền: Chia sẻ"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-010-AC002",
        "BD-16-010-AC004",
        "BD-16-010-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-010-O002",
      "obligation_text": "Platform hỗ trợ Customer Consent. Customer có quyền: Thu hồi"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-010-AC003",
        "BD-16-010-AC004",
        "BD-16-010-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-010-O003",
      "obligation_text": "Platform hỗ trợ Customer Consent. Customer có quyền: Quản lý dữ liệu cá nhân"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-010-AC005"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-010 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-010 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-010-AC004"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-010-AC001",
        "BD-16-010-AC002",
        "BD-16-010-AC003"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-010 does not define a recovery obligation."
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
    "source_fingerprint": "d8461f7891030eda804da02eb18688cb42cdb3ab7b2242001b42491c6eb22e1e",
    "source_lines": "L2450-L2586",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-011",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "fc86224b7a632938909c94e8019a5ac926f6aaf9fd54b039142b5b74490f45cd"
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-011 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-011-AC004"
      ],
      "rationale": null
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-011 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-011-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-011-AC001",
        "BD-16-011-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-011 does not define a recovery obligation."
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
    "source_fingerprint": "fc86224b7a632938909c94e8019a5ac926f6aaf9fd54b039142b5b74490f45cd",
    "source_lines": "L2588-L2709",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-011"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-012",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "60041b9c32a02442812fb4aa4d7e344e203d62d60668660effd4513c1a8854be"
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
        "BD-16-012-AC001",
        "BD-16-012-AC006",
        "BD-16-012-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-012-O001",
      "obligation_text": "API Security hỗ trợ nhiều phương thức. Bao gồm: OAuth2"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-012-AC002",
        "BD-16-012-AC006",
        "BD-16-012-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-012-O002",
      "obligation_text": "API Security hỗ trợ nhiều phương thức. Bao gồm: JWT"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-012-AC003",
        "BD-16-012-AC006",
        "BD-16-012-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-012-O003",
      "obligation_text": "API Security hỗ trợ nhiều phương thức. Bao gồm: API Key"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-012-AC004",
        "BD-16-012-AC006",
        "BD-16-012-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-012-O004",
      "obligation_text": "API Security hỗ trợ nhiều phương thức. Bao gồm: HMAC"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-012-AC005",
        "BD-16-012-AC006",
        "BD-16-012-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-012-O005",
      "obligation_text": "API Security hỗ trợ nhiều phương thức. Bao gồm: Digital Signature"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-012-AC007"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-012 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-012 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-012-AC006"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-012-AC001",
        "BD-16-012-AC002",
        "BD-16-012-AC003",
        "BD-16-012-AC004",
        "BD-16-012-AC005"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-012 does not define a recovery obligation."
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
    "source_fingerprint": "60041b9c32a02442812fb4aa4d7e344e203d62d60668660effd4513c1a8854be",
    "source_lines": "L2711-L2865",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-012"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-013",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "2742cbcd39612511b8efc2760109fa3563d82fabad0fbbad226259495bcfae02"
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
        "BD-16-013-AC001",
        "BD-16-013-AC003",
        "BD-16-013-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-013-O001",
      "obligation_text": "Secret là Business Object"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-013-AC002",
        "BD-16-013-AC003",
        "BD-16-013-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-013-O002",
      "obligation_text": "Secret được quản lý tập trung"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-013-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-013 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-013 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-013-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-013-AC001",
        "BD-16-013-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-013 does not define a recovery obligation."
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
    "source_fingerprint": "2742cbcd39612511b8efc2760109fa3563d82fabad0fbbad226259495bcfae02",
    "source_lines": "L2867-L2988",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-013"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-014",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "8721d60f3d3bfb181b8012bc48a9947129f0a4103fa192a3512f90d10cdfdf05"
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
        "BD-16-014-AC001",
        "BD-16-014-AC003",
        "BD-16-014-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-014-O001",
      "obligation_text": "Platform hỗ trợ Encryption In Transit"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-014-AC002",
        "BD-16-014-AC003",
        "BD-16-014-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-014-O002",
      "obligation_text": "Kiến trúc mở để hỗ trợ Encryption At Rest trong các phiên bản tiếp theo"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-014-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-014-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-014-AC001",
        "BD-16-014-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-014 does not define a recovery obligation."
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
    "source_fingerprint": "8721d60f3d3bfb181b8012bc48a9947129f0a4103fa192a3512f90d10cdfdf05",
    "source_lines": "L2990-L3111",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-014"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-015",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "a9efeb3ee6526f3c32537a97b509ebbba4ad949f8333498dfb7501e89d587879"
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
        "BD-16-015-AC001",
        "BD-16-015-AC003",
        "BD-16-015-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-015-O001",
      "obligation_text": "Platform hỗ trợ Key Rotation"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-015-AC002",
        "BD-16-015-AC003",
        "BD-16-015-AC004"
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
    "source_fingerprint": "a9efeb3ee6526f3c32537a97b509ebbba4ad949f8333498dfb7501e89d587879",
    "source_lines": "L3113-L3198",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-015"
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
  "normative_statement": "Audit Log là Business Object. Audit ghi nhận đầy đủ các Security Event và Business Event quan trọng.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-002",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-016",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Audit Logging",
    "source_context_sha256": "c3a223ed8456790c07473f29edd0f53592bcc7df96f85b5cef84a1546f158902",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "23e133c517ba5900cc823b393cc9ddc5429aac86ee37764d63b8f8b2bdd9cdc0",
    "source_fingerprint_before_c3": "8f89387031df2e67dcabbd440fa88eb66bc5c0cdea4c93f5bb0149dfc57d00e3",
    "source_lines": "L3200-L3260",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-016"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-16-R024",
      "BRD-WS-16-R025"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-16-016",
  "title": "Audit Log là Business Object. Audit ghi nhận đầy đủ các Security Event và Business Event quan tr…",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-017 — Platform hỗ trợ Compliance. Phiên bản hiện tại hỗ trợ: - GDPR

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
      "requirement_id": "BD-16-017",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "4dccfe72804ae52532e94b012151106001c5d42456663c8538abee2b85760197"
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
        "BD-16-017-AC001",
        "BD-16-017-AC003",
        "BD-16-017-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-017-O001",
      "obligation_text": "Platform hỗ trợ Compliance"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-017-AC002",
        "BD-16-017-AC003",
        "BD-16-017-AC004"
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
    "source_fingerprint": "4dccfe72804ae52532e94b012151106001c5d42456663c8538abee2b85760197",
    "source_lines": "L3262-L3347",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-017"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-018",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "7b269ccf14928692df3b360b7bb88aa4b009163a874d87fb9d66b3e82dca7ba8"
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
        "BD-16-018-AC001",
        "BD-16-018-AC004",
        "BD-16-018-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-018-O001",
      "obligation_text": "Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: Export Data"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-018-AC002",
        "BD-16-018-AC004",
        "BD-16-018-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-018-O002",
      "obligation_text": "Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: Delete Identity"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-018-AC003",
        "BD-16-018-AC004",
        "BD-16-018-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-018-O003",
      "obligation_text": "Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: Customer Consent"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-018-AC005"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-018 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-018 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-018-AC004"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-018-AC001",
        "BD-16-018-AC002",
        "BD-16-018-AC003"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-018 does not define a recovery obligation."
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
    "source_fingerprint": "7b269ccf14928692df3b360b7bb88aa4b009163a874d87fb9d66b3e82dca7ba8",
    "source_lines": "L3349-L3485",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-018"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-019",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "48720ff851b2a1d352f074905c621dae3908e907970b02b3ccb8a64aa2d91360"
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
        "BD-16-019-AC001",
        "BD-16-019-AC002",
        "BD-16-019-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-019-O001",
      "obligation_text": "API Permission được quản lý độc lập với Portal Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-019 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-019 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-019 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-019-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-019-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-019 does not define a recovery obligation."
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
    "source_fingerprint": "48720ff851b2a1d352f074905c621dae3908e907970b02b3ccb8a64aa2d91360",
    "source_lines": "L3487-L3595",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-019"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-005"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-020",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "e7687c7b58073a60bebf20385d25dfc04f9eaf7bfe8927cdc7a717f17d7a5572"
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
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-020-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-020 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-020 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-020-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-020-AC001",
        "BD-16-020-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-020 does not define a recovery obligation."
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
    "source_fingerprint": "e7687c7b58073a60bebf20385d25dfc04f9eaf7bfe8927cdc7a717f17d7a5572",
    "source_lines": "L3597-L3722",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-020"
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
  "normative_statement": "Risk Rule là Business Object. Risk Rule được cấu hình. Không Hard-code.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-021",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Risk Rule",
    "source_context_sha256": "79a6378d5d297d3ac4b6561a2c177377d25cd033018faace37cf7d681b9ad773",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "7c3934988f2d9c78cc4522c37408e53b12d3c494733f86551d2c0f2951a77a15",
    "source_fingerprint_before_c3": "dfb0c2af2ef6e28af30469baf3d44f2397673230f9a1df6770fefc36218e05a1",
    "source_lines": "L3724-L3784",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-021"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-16-R026",
      "BRD-WS-16-R027",
      "BRD-WS-16-R028"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BD-16-021",
  "title": "Risk Rule là Business Object. Risk Rule được cấu hình. Không Hard-code",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-022 — Platform hỗ trợ Temporary Account Lock

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
      "requirement_id": "BD-16-022",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "5ff1ac908095f92ac556721342a62db1d039cdb62d06580e7ecca629c834e023"
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
        "BD-16-022-AC001",
        "BD-16-022-AC002",
        "BD-16-022-AC003"
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
    "source_fingerprint": "5ff1ac908095f92ac556721342a62db1d039cdb62d06580e7ecca629c834e023",
    "source_lines": "L3786-L3861",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-022"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-023",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "9b9f890d4d6d030437aecc880a524da049b596615648d28079e71a7fea7d6a95"
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
        "BD-16-023-AC001",
        "BD-16-023-AC003",
        "BD-16-023-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-023-O001",
      "obligation_text": "Audit Log được lưu trực tuyến 03 tháng"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-023-AC002",
        "BD-16-023-AC003",
        "BD-16-023-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-023-O002",
      "obligation_text": "Sau đó được Archive"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-023 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-023 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-023 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-023-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-023-AC001",
        "BD-16-023-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-023 does not define a recovery obligation."
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
    "source_fingerprint": "9b9f890d4d6d030437aecc880a524da049b596615648d28079e71a7fea7d6a95",
    "source_lines": "L3863-L3982",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-023"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-024",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "5f49037eacf9b132ed98d2467906e55d75e4f5686f4e6206a3e2e0668d1d6eee"
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
        "BD-16-024-AC001",
        "BD-16-024-AC003",
        "BD-16-024-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-024-O001",
      "obligation_text": "Permission Evaluation Engine là thành phần trung tâm của Security Platform"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-024-AC002",
        "BD-16-024-AC003",
        "BD-16-024-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-024-O002",
      "obligation_text": "Business Domain không tự đánh giá Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-024-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-024 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-024 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-024-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-024-AC001",
        "BD-16-024-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-024 does not define a recovery obligation."
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
    "source_fingerprint": "5f49037eacf9b132ed98d2467906e55d75e4f5686f4e6206a3e2e0668d1d6eee",
    "source_lines": "L3984-L4105",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-024"
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
      "requirement_id": "BD-16-025",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "77f49c655034f801ebdb3469276285be86391d2c76da06f3d923534eb92c6ed7"
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
        "BD-16-025-AC001",
        "BD-16-025-AC005",
        "BD-16-025-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-025-O001",
      "obligation_text": "Security Policy là Business Object. Security Policy hỗ trợ: Version"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-025-AC002",
        "BD-16-025-AC005",
        "BD-16-025-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-025-O002",
      "obligation_text": "Security Policy là Business Object. Security Policy hỗ trợ: Effective Date"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-025-AC003",
        "BD-16-025-AC005",
        "BD-16-025-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-025-O003",
      "obligation_text": "Security Policy là Business Object. Security Policy hỗ trợ: Approval"
    },
    {
      "acceptance_criterion_references": [
        "BD-16-025-AC004",
        "BD-16-025-AC005",
        "BD-16-025-AC006"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-025-O004",
      "obligation_text": "Security Policy là Business Object. Security Policy hỗ trợ: Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-025-AC006"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-025 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-025 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-025-AC005"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-025-AC001",
        "BD-16-025-AC002",
        "BD-16-025-AC003",
        "BD-16-025-AC004"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-025 does not define a recovery obligation."
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
    "source_fingerprint": "77f49c655034f801ebdb3469276285be86391d2c76da06f3d923534eb92c6ed7",
    "source_lines": "L4107-L4256",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-025"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-001",
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-026",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "2e348ea0b95ff6b984766ef1147b16c1b7ab2338088d2dbed543b932629313f2"
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
        "BD-16-026-AC001",
        "BD-16-026-AC002",
        "BD-16-026-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-026-O001",
      "obligation_text": "Identity Platform hỗ trợ Federation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-026-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-026 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-026 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-026-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-026-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-026 does not define a recovery obligation."
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
    "source_fingerprint": "2e348ea0b95ff6b984766ef1147b16c1b7ab2338088d2dbed543b932629313f2",
    "source_lines": "L4258-L4376",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-026"
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
### BD-16-027 — Security Platform phải publish Security Business Event theo Versioned Security Event Catalog quản trị event type, tri…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2C-SC-C1-DEC-004/OPT-A"
      ],
      "approved_semantic_completion_selection": {
        "decision_id": "P2C-SC-C1-DEC-004",
        "option_id": "OPT-A"
      },
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-027",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "55c0ba597387cbec72e1d227d440f2fb58f3c02f446fbc146d47677668fe2b34"
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
        "BD-16-027-AC001",
        "BD-16-027-AC002",
        "BD-16-027-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-027-O001",
      "obligation_text": "Security Platform phải publish Security Business Event theo Versioned Security Event Catalog quản trị event type, trigger, correlation và payload contract; requirement này không thiết lập danh sách event cố định và không khẳng định runtime implementation"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-027-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-027 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-027 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-027-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-027-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-027 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Security Platform phải publish Security Business Event theo Versioned Security Event Catalog quản trị event type, trigger, correlation và payload contract; requirement này không thiết lập danh sách event cố định và không khẳng định runtime implementation.",
  "provenance": {
    "approved_decisions": [
      "P2C-SC-C1-DEC-004/OPT-A"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-16-027",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "29. Security Business Events",
    "source_context_sha256": "6bd0565e1d201ed4d938250bfe47c7cda8fc6c1a9bde6f1e0558bdc02dd3c34a",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "55c0ba597387cbec72e1d227d440f2fb58f3c02f446fbc146d47677668fe2b34",
    "source_lines": "L4378-L4498",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-027"
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
  "title": "Security Platform phải publish Security Business Event theo Versioned Security Event Catalog quản trị event type, tri…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-16-028 — Data Classification là Business Object

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
      "requirement_id": "BD-16-028",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "90207012c4b59b743fb4462d9159781dda4f0277eeaeba1dacd27a052dd7ef05"
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
        "BD-16-028-AC001",
        "BD-16-028-AC002",
        "BD-16-028-AC003"
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
    "source_fingerprint": "90207012c4b59b743fb4462d9159781dda4f0277eeaeba1dacd27a052dd7ef05",
    "source_lines": "L4500-L4575",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-028"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-029",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "09ed1e962c560f86c4e31167463cee899c65e3db89ef3a6eee4da7fdddc16e19"
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
        "BD-16-029-AC001",
        "BD-16-029-AC002",
        "BD-16-029-AC003"
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
    "source_fingerprint": "09ed1e962c560f86c4e31167463cee899c65e3db89ef3a6eee4da7fdddc16e19",
    "source_lines": "L4577-L4652",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-029"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-16-030",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "88ab980b1b45c7fe4f26de0a727e8881224c287f580fbe0ca190706ff17f8555"
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
        "BD-16-030-AC001",
        "BD-16-030-AC002",
        "BD-16-030-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-16-030-O001",
      "obligation_text": "Toàn bộ truy cập dữ liệu phải được đánh giá động thông qua Permission Evaluation Engine và Security Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-030-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-030 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-030 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-030-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-16-030-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-16-030 does not define a recovery obligation."
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
    "source_fingerprint": "88ab980b1b45c7fe4f26de0a727e8881224c287f580fbe0ca190706ff17f8555",
    "source_lines": "L4654-L4764",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-16-030"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R001",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "d90990c2f3e9737ee237623199fed3c3cbc69a819abe0c32b053d0b32c3cb015"
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
        "BRD-WS-16-R001-AC001",
        "BRD-WS-16-R001-AC002",
        "BRD-WS-16-R001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R001-O001",
      "obligation_text": "Permission không được xác định chỉ dựa trên Role"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R001-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R001 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R001 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R001-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R001-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R001 does not define a recovery obligation."
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
    "source_lines": "L4766-L4876",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R001"
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
  "normative_statement": "Authorization phải hỗ trợ mở rộng để đáp ứng các mô hình phân quyền phức tạp trong tương lai.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-002",
    "phase_2c_c3_actions": [
      "C3_APPROVED_DECISION_COMPOSITE_SPLIT"
    ],
    "previous_temporary_key": "TMP-BRD-WS-16-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Authorization Model",
    "source_context_sha256": "056a4758658cb438ed24160bbd341ea1563558eba2f30d3492f97a940f925c9c",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "0f3674ea96cbdabaf8ac81a95ec1fab7cdb5502d76c1b2a640532a71f9ec1eae",
    "source_fingerprint_before_c3": "0f3674ea96cbdabaf8ac81a95ec1fab7cdb5502d76c1b2a640532a71f9ec1eae",
    "source_lines": "L4878-L4937",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R002"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-16-R040",
      "BRD-WS-16-R041"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R002",
  "title": "Authorization phải hỗ trợ mở rộng để đáp ứng các mô hình phân quyền phức tạp trong tương lai",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R003 — Permission không được Hard-code trong mã nguồn

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
      "requirement_id": "BRD-WS-16-R003",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "2387386fcb1ef0ac81da400842049aa05d4dc98f6e674f7096772706733df0e5"
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
        "BRD-WS-16-R003-AC001",
        "BRD-WS-16-R003-AC002",
        "BRD-WS-16-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R003-O001",
      "obligation_text": "Permission không được Hard-code trong mã nguồn"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R003-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R003-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R003-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R003 does not define a recovery obligation."
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
    "source_lines": "L4939-L5049",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R003"
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
### BRD-WS-16-R004 — Field-Level Permission phải được đánh giá cùng Data Scope và Permission, và không được hard-code

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
      "requirement_id": "BRD-WS-16-R004",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "2516696e4f8404f676ef202db089c726e7d66a49ffa34585b924fe094e27f66c"
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
        "BRD-WS-16-R004-AC001",
        "BRD-WS-16-R004-AC002",
        "BRD-WS-16-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R004-O001",
      "obligation_text": "Field-Level Permission phải được đánh giá cùng Data Scope và Permission, và không được hard-code"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R004-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R004-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R004-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R004 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Field-Level Permission phải được đánh giá cùng Data Scope và Permission, và không được hard-code.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-16.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "10. Field-Level Permission"
    },
    "deterministic_transformation": "RESTORE_FIELD_PERMISSION_SUBJECT",
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-004",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-16-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. Field-Level Permission",
    "source_context_sha256": "f1685ea7a9aa9d5e51c3fe9ba88512a113b60dcaf1ef65fab2dea61565df803c",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "2516696e4f8404f676ef202db089c726e7d66a49ffa34585b924fe094e27f66c",
    "source_fingerprint_before_c3": "4621b7640c0dcd2270db940c6e871c9dfa60a401b1675b7473403baf1ab00536",
    "source_lines": "L5051-L5182",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-16.md",
      "lines": "L266",
      "section": "10. Field-Level Permission"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R004"
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
  "title": "Field-Level Permission phải được đánh giá cùng Data Scope và Permission, và không được hard-code",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R005 — Secret không được lưu dưới dạng Plain Text

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
      "requirement_id": "BRD-WS-16-R005",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "bb7f6387a9e545ae525ed99c44cf792e70fb1c8fd3db2d195090a9bc32d9e46b"
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
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R005-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R005 does not define a recovery obligation."
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
    "source_lines": "L5184-L5294",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R006",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "5b1e2df25c21481767865381aea37f1835ce20b091ab2c6b581e4eed2f8c0434"
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
        "BRD-WS-16-R006-AC001",
        "BRD-WS-16-R006-AC002",
        "BRD-WS-16-R006-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R006-O001",
      "obligation_text": "Audit Log chỉ được phép đọc"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R006 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R006-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R006-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R006 does not define a recovery obligation."
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
    "source_lines": "L5296-L5404",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R007",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "05f1ee6e083ef88c3b6dc032e51b2e644e902a9289d9f3f6d89f81bfeb258330"
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
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R007 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R007 does not define a recovery obligation."
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
    "source_lines": "L5406-L5514",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R008",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "d65bc83f5e5e25e2eafdbfafd330a6eb95b75520bdf76b53b3ecc65930633eb7"
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
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R008-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R008 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R008 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R008-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R008-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R008 does not define a recovery obligation."
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
    "source_lines": "L5516-L5626",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R010",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "25e19b2a4d1740fe9c741a21e86c9245bf0c634c0ae12fccaf7ba20344dbe3dd"
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
        "BRD-WS-16-R010-AC001",
        "BRD-WS-16-R010-AC002",
        "BRD-WS-16-R010-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R010-O001",
      "obligation_text": "Mọi đánh giá Permission đều phải đi qua Permission Evaluation Engine"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R010-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R010 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R010 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R010-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R010-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R010 does not define a recovery obligation."
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
    "source_lines": "L5628-L5738",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R011",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "2909b3d7d18d5f7c670bed650c9cf5306087c5c7857f30506c0ba837c519f14a"
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
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R011-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R011 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R011 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R011-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R011-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R011 does not define a recovery obligation."
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
    "source_lines": "L5740-L5850",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R011"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "A locally managed account may still exist when separately required; federation does not mandate duplication"
    ],
    "concrete_bindings": [
      {
        "capability": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
            "source_type": "SOURCE_LITERAL",
            "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
          },
          "identifier": "BRD-WS-16-R012.CAPABILITY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.CAPABILITY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-001",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
            "source_lines": "L681",
            "source_section": "28. Identity Federation"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CAPABILITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-16-R012.BRD-WS-16-R012.CAPABILITY",
            "version": "1.0.0"
          },
          "semantic_type": "CAPABILITY_ID"
        },
        "scope": {
          "authoritative_source": {
            "allowed_identifiers": [
              "BRD-WS-16-R012.SCOPE"
            ],
            "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
            "source_type": "SOURCE_LITERAL",
            "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
          },
          "identifier": "BRD-WS-16-R012.SCOPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.SCOPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-001",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
            "source_lines": "L681",
            "source_section": "28. Identity Federation"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_ENUM_VALUE",
            "resolver_id": "RESOLVE.BRD-WS-16-R012.BRD-WS-16-R012.SCOPE",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_ENUM_VALUE"
        },
        "subject": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
            "source_type": "SOURCE_LITERAL",
            "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
          },
          "identifier": "BRD-WS-16-R012.SUBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.SUBJECT.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-001",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
            "source_lines": "L681",
            "source_section": "28. Identity Federation"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-WS-16-R012.BRD-WS-16-R012.SUBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-16-R012",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Federation requires creation of a duplicate local User"
    ],
    "operator_composition": [
      "CAPABILITY_AVAILABLE"
    ],
    "positive_oracle": [
      "Organization uses existing identity through federation without creating a duplicate YSim User"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-001",
        "P2-DEC-008"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
      "source_lines": "L681",
      "source_section": "28. Identity Federation"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
          "source_type": "SOURCE_LITERAL",
          "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
        },
        "identifier": "BRD-WS-16-R012.BRD-WS-16-R012.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-16-R012.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-001",
            "P2-DEC-008"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-16.md",
          "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
          "source_lines": "L681",
          "source_section": "28. Identity Federation"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-16-R012.BRD-WS-16-R012.BRD-WS-16-R012.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-16-R012.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.ORGANIZATION_ID",
        "FIELD.IDENTITY_PROVIDER",
        "FIELD.EXTERNAL_SUBJECT",
        "FIELD.FEDERATION_RESULT",
        "FIELD.LOCAL_USER_CREATED"
      ],
      "producer": "BRD-WS-16-R012.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-16-R012.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.ORGANIZATION_ID",
        "FIELD.IDENTITY_PROVIDER",
        "FIELD.EXTERNAL_SUBJECT",
        "FIELD.FEDERATION_RESULT",
        "FIELD.LOCAL_USER_CREATED"
      ],
      "required_values_or_hashes": [
        "BRD-WS-16-R012.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-16-R012.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-16-R012.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-16-R012-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE",
          "evaluator_consumed_bindings": [
            "capability",
            "scope",
            "subject"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
              "source_type": "SOURCE_LITERAL",
              "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
            },
            "identifier": "BRD-WS-16-R012.BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-001",
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-16.md",
              "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
              "source_lines": "L681",
              "source_section": "28. Identity Federation"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-16-R012.BRD-WS-16-R012.BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
              "source_type": "SOURCE_LITERAL",
              "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
            },
            "identifier": "BRD-WS-16-R012.BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-001",
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-16.md",
              "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
              "source_lines": "L681",
              "source_section": "28. Identity Federation"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "ENTITY_ID",
              "resolver_id": "RESOLVE.BRD-WS-16-R012.BRD-WS-16-R012.BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "ENTITY_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "capability": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
                },
                "identifier": "BRD-WS-16-R012.CAPABILITY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.CAPABILITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-001",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
                  "source_lines": "L681",
                  "source_section": "28. Identity Federation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CAPABILITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-16-R012.BRD-WS-16-R012.CAPABILITY",
                  "version": "1.0.0"
                },
                "semantic_type": "CAPABILITY_ID"
              },
              "scope": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "BRD-WS-16-R012.SCOPE"
                  ],
                  "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
                },
                "identifier": "BRD-WS-16-R012.SCOPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.SCOPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-001",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
                  "source_lines": "L681",
                  "source_section": "28. Identity Federation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_ENUM_VALUE",
                  "resolver_id": "RESOLVE.BRD-WS-16-R012.BRD-WS-16-R012.SCOPE",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_ENUM_VALUE"
              },
              "subject": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
                },
                "identifier": "BRD-WS-16-R012.SUBJECT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.SUBJECT.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-001",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
                  "source_lines": "L681",
                  "source_section": "28. Identity Federation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-16-R012.BRD-WS-16-R012.SUBJECT",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
                },
                "identifier": "BRD-WS-16-R012.BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-001",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
                  "source_lines": "L681",
                  "source_section": "28. Identity Federation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-16-R012.BRD-WS-16-R012.BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
                  "source_type": "SOURCE_LITERAL",
                  "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
                },
                "identifier": "BRD-WS-16-R012.BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-001",
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
                  "source_lines": "L681",
                  "source_section": "28. Identity Federation"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "OBSERVE.BRD-WS-16-R012.BRD-WS-16-R012.BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
                "source_type": "SOURCE_LITERAL",
                "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
              },
              "identifier": "BRD-WS-16-R012.BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-001",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
                "source_lines": "L681",
                "source_section": "28. Identity Federation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-16-R012.BRD-WS-16-R012.BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "CAPABILITY_AVAILABLE"
          },
          "obligation_id": "BRD-WS-16-R012-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
              "source_type": "SOURCE_LITERAL",
              "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
            },
            "identifier": "BRD-WS-16-R012.BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-001",
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-16.md",
              "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
              "source_lines": "L681",
              "source_section": "28. Identity Federation"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "ENTITY_ID",
              "resolver_id": "OBSERVE.BRD-WS-16-R012.BRD-WS-16-R012.BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "ENTITY_ID"
          },
          "operator_id": "CAPABILITY_AVAILABLE",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "capability": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
                "source_type": "SOURCE_LITERAL",
                "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
              },
              "identifier": "BRD-WS-16-R012.CAPABILITY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.CAPABILITY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-001",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
                "source_lines": "L681",
                "source_section": "28. Identity Federation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CAPABILITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-16-R012.BRD-WS-16-R012.CAPABILITY",
                "version": "1.0.0"
              },
              "semantic_type": "CAPABILITY_ID"
            },
            "scope": {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-WS-16-R012.SCOPE"
                ],
                "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
                "source_type": "SOURCE_LITERAL",
                "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
              },
              "identifier": "BRD-WS-16-R012.SCOPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.SCOPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-001",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
                "source_lines": "L681",
                "source_section": "28. Identity Federation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_ENUM_VALUE",
                "resolver_id": "RESOLVE.BRD-WS-16-R012.BRD-WS-16-R012.SCOPE",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_ENUM_VALUE"
            },
            "subject": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
                "source_type": "SOURCE_LITERAL",
                "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
              },
              "identifier": "BRD-WS-16-R012.SUBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE.SUBJECT.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-001",
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
                "source_lines": "L681",
                "source_section": "28. Identity Federation"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-WS-16-R012.BRD-WS-16-R012.SUBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "A locally managed account may still exist when separately required; federation does not mandate duplication"
      ],
      "contract_ast_sha256": "1b1fce170b6d66d16f214246da7fa20cfbf9c359c71f81a6bf56df2ac5056fbe",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-16-R012",
      "criticality": "CRITICAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-16.md#28. Identity Federation",
            "source_type": "SOURCE_LITERAL",
            "version": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c"
          },
          "identifier": "BRD-WS-16-R012.BRD-WS-16-R012.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-16-R012.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-001",
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
            "source_lines": "L681",
            "source_section": "28. Identity Federation"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-16-R012.BRD-WS-16-R012.BRD-WS-16-R012.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-16-R012.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.ORGANIZATION_ID",
          "FIELD.IDENTITY_PROVIDER",
          "FIELD.EXTERNAL_SUBJECT",
          "FIELD.FEDERATION_RESULT",
          "FIELD.LOCAL_USER_CREATED"
        ],
        "producer": "BRD-WS-16-R012.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-16-R012.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.ORGANIZATION_ID",
          "FIELD.IDENTITY_PROVIDER",
          "FIELD.EXTERNAL_SUBJECT",
          "FIELD.FEDERATION_RESULT",
          "FIELD.LOCAL_USER_CREATED"
        ],
        "required_values_or_hashes": [
          "BRD-WS-16-R012.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-16-R012.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-16-R012.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-E31EC023B6BB042A44F2",
        "P2C-C4-FX-5EE36270DDFC0C85A2E4",
        "P2C-C4-FX-300E2CF3E81F4A6716BA"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Federation requires creation of a duplicate local User"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-16-R012-O001",
          "obligation_text": "Identity Federation cho phép Organization sử dụng hệ thống Identity hiện có mà không cần tạo lại User trên YSim"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-16-R012.O1.1.CAPABILITY_AVAILABLE"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-16-R012-O001"
        }
      ],
      "operator_composition": [
        "CAPABILITY_AVAILABLE"
      ],
      "positive_oracles": [
        "Organization uses existing identity through federation without creating a duplicate YSim User"
      ],
      "preconditions": [
        "An approved federation configuration and external identity exist"
      ],
      "prohibitions": [
        "Federation requires creation of a duplicate local User"
      ],
      "requirement_id": "BRD-WS-16-R012",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-001",
          "P2-DEC-008"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-16.md",
        "source_fingerprint": "918262213147360a86464cad6c9afdce73b1587b37827e01415a15dbfa5bb31c",
        "source_lines": "L681",
        "source_section": "28. Identity Federation"
      },
      "source_statement": "Identity Federation cho phép Organization sử dụng hệ thống Identity hiện có mà không cần tạo lại User trên YSim.",
      "surrounding_source_context": "### BRD-WS-16-R012 — Identity Federation cho phép Organization sử dụng hệ thống Identity hiện có mà không cần tạo lại…"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-16-R012",
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
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R012-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R012 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R012 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R012-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R012-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R012 does not define a recovery obligation."
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
    "source_lines": "L5852-L6830",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R012"
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
### BRD-WS-16-R013 — Sau thời hạn ba tháng lưu Audit Log trực tuyến, Audit Log phải được archive

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
      "requirement_id": "BRD-WS-16-R013",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "fa24a610f189d989a08981b5d29ae53769a82727f34e522133a879eb172d713b"
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
        "BRD-WS-16-R013-AC001",
        "BRD-WS-16-R013-AC002",
        "BRD-WS-16-R013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R013-O001",
      "obligation_text": "Sau thời hạn ba tháng lưu Audit Log trực tuyến, Audit Log phải được archive"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R013 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R013 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R013 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R013-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R013-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R013 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sau thời hạn ba tháng lưu Audit Log trực tuyến, Audit Log phải được archive.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-16.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "25. Audit Retention"
    },
    "deterministic_transformation": "RESTORE_RETENTION_PERIOD_AND_AUDIT_SUBJECT",
    "historical_derived_from": [
      "TMP-BRD-WS-16-009"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-013",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-16-013",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Audit Retention",
    "source_context_sha256": "4b1929c0009643385713951a5e369bab3e7359126f368a83a9f1080fa43ecd78",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "fa24a610f189d989a08981b5d29ae53769a82727f34e522133a879eb172d713b",
    "source_fingerprint_before_c3": "88528833f051f4faf92eba801f45a615bbedb5f70a520d765b7b907152562384",
    "source_lines": "L6832-L6964",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-16.md",
      "lines": "L597-L602",
      "section": "25. Audit Retention"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R013"
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
  "title": "Sau thời hạn ba tháng lưu Audit Log trực tuyến, Audit Log phải được archive",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R014 — Sau thời hạn ba tháng lưu Audit Log trực tuyến, bản archive phải chỉ đọc

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
      "requirement_id": "BRD-WS-16-R014",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "7773213bea146b97250d5c5f849d722a69389ca6b6c0ddc3cb0bfd19cd3d5b39"
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
        "BRD-WS-16-R014-AC001",
        "BRD-WS-16-R014-AC002",
        "BRD-WS-16-R014-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R014-O001",
      "obligation_text": "Sau thời hạn ba tháng lưu Audit Log trực tuyến, bản archive phải chỉ đọc"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R014 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R014 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R014 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R014-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R014-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R014 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sau thời hạn ba tháng lưu Audit Log trực tuyến, bản archive phải chỉ đọc.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-16.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "25. Audit Retention"
    },
    "deterministic_transformation": "RESTORE_RETENTION_PERIOD_AND_AUDIT_SUBJECT",
    "historical_derived_from": [
      "TMP-BRD-WS-16-009"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-014",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-16-014",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Audit Retention",
    "source_context_sha256": "4b1929c0009643385713951a5e369bab3e7359126f368a83a9f1080fa43ecd78",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "7773213bea146b97250d5c5f849d722a69389ca6b6c0ddc3cb0bfd19cd3d5b39",
    "source_fingerprint_before_c3": "88528833f051f4faf92eba801f45a615bbedb5f70a520d765b7b907152562384",
    "source_lines": "L6966-L7098",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-16.md",
      "lines": "L597-L602",
      "section": "25. Audit Retention"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R014"
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
  "title": "Sau thời hạn ba tháng lưu Audit Log trực tuyến, bản archive phải chỉ đọc",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R015 — Sau thời hạn ba tháng lưu Audit Log trực tuyến, bản archive không được sửa

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
      "requirement_id": "BRD-WS-16-R015",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "5562d406d7ef87121c16fe6cc24dcf9bedcdd059a9fb7eaea5487eb2db9dbb6a"
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
        "BRD-WS-16-R015-AC001",
        "BRD-WS-16-R015-AC002",
        "BRD-WS-16-R015-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R015-O001",
      "obligation_text": "Sau thời hạn ba tháng lưu Audit Log trực tuyến, bản archive không được sửa"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R015 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R015 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R015 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R015-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R015-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R015 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sau thời hạn ba tháng lưu Audit Log trực tuyến, bản archive không được sửa.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-16.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "25. Audit Retention"
    },
    "deterministic_transformation": "RESTORE_RETENTION_PERIOD_AND_AUDIT_SUBJECT",
    "historical_derived_from": [
      "TMP-BRD-WS-16-009"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-015",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-16-015",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Audit Retention",
    "source_context_sha256": "4b1929c0009643385713951a5e369bab3e7359126f368a83a9f1080fa43ecd78",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "5562d406d7ef87121c16fe6cc24dcf9bedcdd059a9fb7eaea5487eb2db9dbb6a",
    "source_fingerprint_before_c3": "88528833f051f4faf92eba801f45a615bbedb5f70a520d765b7b907152562384",
    "source_lines": "L7100-L7232",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-16.md",
      "lines": "L597-L602",
      "section": "25. Audit Retention"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R015"
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
  "title": "Sau thời hạn ba tháng lưu Audit Log trực tuyến, bản archive không được sửa",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R016 — Sau thời hạn ba tháng lưu Audit Log trực tuyến, bản archive không được xóa trực tiếp

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
      "requirement_id": "BRD-WS-16-R016",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "5b1ce0551258d239bef7e338a5f8acfb961840520186f4c1ed6e8de102ad0fb1"
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
        "BRD-WS-16-R016-AC001",
        "BRD-WS-16-R016-AC002",
        "BRD-WS-16-R016-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R016-O001",
      "obligation_text": "Sau thời hạn ba tháng lưu Audit Log trực tuyến, bản archive không được xóa trực tiếp"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R016 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R016 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R016 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R016-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R016-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R016 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Sau thời hạn ba tháng lưu Audit Log trực tuyến, bản archive không được xóa trực tiếp.",
  "provenance": {
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "corrected_source_range": {
      "document": "docs/BRD/BRD-WS-16.md",
      "range_rule": "INCLUDE_GOVERNED_SUBJECT_TRIGGER_PREDICATE_AND_REQUIRED_LIST",
      "section": "25. Audit Retention"
    },
    "deterministic_transformation": "RESTORE_RETENTION_PERIOD_AND_AUDIT_SUBJECT",
    "historical_derived_from": [
      "TMP-BRD-WS-16-009"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-16-016",
    "phase_2c_c3_actions": [
      "C3_DETERMINISTIC_SOURCE_NORMALIZATION"
    ],
    "previous_temporary_key": "TMP-BRD-WS-16-016",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "25. Audit Retention",
    "source_context_sha256": "4b1929c0009643385713951a5e369bab3e7359126f368a83a9f1080fa43ecd78",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "5b1ce0551258d239bef7e338a5f8acfb961840520186f4c1ed6e8de102ad0fb1",
    "source_fingerprint_before_c3": "88528833f051f4faf92eba801f45a615bbedb5f70a520d765b7b907152562384",
    "source_lines": "L7234-L7369",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_range_before_c3": {
      "document": "docs/BRD/BRD-WS-16.md",
      "lines": "L597-L602",
      "section": "25. Audit Retention"
    },
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R016"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R024"
    ]
  },
  "requirement_type": "BUSINESS_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R016",
  "title": "Sau thời hạn ba tháng lưu Audit Log trực tuyến, bản archive không được xóa trực tiếp",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R017 — Permission hỗ trợ Scope linh hoạt. Bao gồm: Platform

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R017",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "93bb51d090462c7d00fe1091915b4ed60203d032c0b21eb0a209f1e59dc488ed"
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
        "BRD-WS-16-R017-AC001",
        "BRD-WS-16-R017-AC003",
        "BRD-WS-16-R017-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R017-O001",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-16-R017-AC002",
        "BRD-WS-16-R017-AC003",
        "BRD-WS-16-R017-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R017-O002",
      "obligation_text": "Bao gồm: Platform"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R017-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R017 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R017 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R017-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R017-AC001",
        "BRD-WS-16-R017-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R017 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Platform.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R017",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-006",
    "source_context_sha256": "f07eaa73f91bac65267fd0ce84085c9976ac9a47f2daf786e9d6b4f500317bb7",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "93bb51d090462c7d00fe1091915b4ed60203d032c0b21eb0a209f1e59dc488ed",
    "source_fingerprint_before_c3": "93bb51d090462c7d00fe1091915b4ed60203d032c0b21eb0a209f1e59dc488ed",
    "source_lines": "L7371-L7511",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R017"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-006"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R017",
  "title": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Platform",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R018 — Permission hỗ trợ Scope linh hoạt. Bao gồm: Organization

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R018",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "cd50288eaff2984d8574d82d05ae7fc1eb0d0a14ca3253993d3296d4ff83f0f5"
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
        "BRD-WS-16-R018-AC001",
        "BRD-WS-16-R018-AC003",
        "BRD-WS-16-R018-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R018-O001",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-16-R018-AC002",
        "BRD-WS-16-R018-AC003",
        "BRD-WS-16-R018-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R018-O002",
      "obligation_text": "Bao gồm: Organization"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R018-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R018 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R018 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R018-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R018-AC001",
        "BRD-WS-16-R018-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R018 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Organization.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R018",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-006",
    "source_context_sha256": "f07eaa73f91bac65267fd0ce84085c9976ac9a47f2daf786e9d6b4f500317bb7",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "cd50288eaff2984d8574d82d05ae7fc1eb0d0a14ca3253993d3296d4ff83f0f5",
    "source_fingerprint_before_c3": "cd50288eaff2984d8574d82d05ae7fc1eb0d0a14ca3253993d3296d4ff83f0f5",
    "source_lines": "L7513-L7653",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R018"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-006"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R018",
  "title": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Organization",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R019 — Permission hỗ trợ Scope linh hoạt. Bao gồm: Department

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R019",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "a4deaf584307e475169c8459a90f8d0e273edf048a69b4e7a7fd8bbbd04c4bf5"
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
        "BRD-WS-16-R019-AC001",
        "BRD-WS-16-R019-AC003",
        "BRD-WS-16-R019-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R019-O001",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-16-R019-AC002",
        "BRD-WS-16-R019-AC003",
        "BRD-WS-16-R019-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R019-O002",
      "obligation_text": "Bao gồm: Department"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R019-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R019 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R019 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R019-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R019-AC001",
        "BRD-WS-16-R019-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R019 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Department.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R019",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-006",
    "source_context_sha256": "f07eaa73f91bac65267fd0ce84085c9976ac9a47f2daf786e9d6b4f500317bb7",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "a4deaf584307e475169c8459a90f8d0e273edf048a69b4e7a7fd8bbbd04c4bf5",
    "source_fingerprint_before_c3": "a4deaf584307e475169c8459a90f8d0e273edf048a69b4e7a7fd8bbbd04c4bf5",
    "source_lines": "L7655-L7795",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R019"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-006"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R019",
  "title": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Department",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R020 — Permission hỗ trợ Scope linh hoạt. Bao gồm: Team

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R020",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "7fd4227e5c0eb49abab7cb395345492de5f7eadce2a2bb97f9e8dd220ce3c190"
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
        "BRD-WS-16-R020-AC001",
        "BRD-WS-16-R020-AC003",
        "BRD-WS-16-R020-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R020-O001",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-16-R020-AC002",
        "BRD-WS-16-R020-AC003",
        "BRD-WS-16-R020-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R020-O002",
      "obligation_text": "Bao gồm: Team"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R020-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R020 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R020 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R020-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R020-AC001",
        "BRD-WS-16-R020-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R020 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Team.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R020",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-006",
    "source_context_sha256": "f07eaa73f91bac65267fd0ce84085c9976ac9a47f2daf786e9d6b4f500317bb7",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "7fd4227e5c0eb49abab7cb395345492de5f7eadce2a2bb97f9e8dd220ce3c190",
    "source_fingerprint_before_c3": "7fd4227e5c0eb49abab7cb395345492de5f7eadce2a2bb97f9e8dd220ce3c190",
    "source_lines": "L7797-L7937",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R020"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-006"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R020",
  "title": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Team",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R021 — Permission hỗ trợ Scope linh hoạt. Bao gồm: Storefront

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R021",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "1dbbab0b68863db048db8374eb191f908bbb1a55481791f425fc8c647a5cbaee"
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
        "BRD-WS-16-R021-AC001",
        "BRD-WS-16-R021-AC003",
        "BRD-WS-16-R021-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R021-O001",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-16-R021-AC002",
        "BRD-WS-16-R021-AC003",
        "BRD-WS-16-R021-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R021-O002",
      "obligation_text": "Bao gồm: Storefront"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R021 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R021 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R021 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R021-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R021-AC001",
        "BRD-WS-16-R021-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R021 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Storefront.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R021",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-006",
    "source_context_sha256": "f07eaa73f91bac65267fd0ce84085c9976ac9a47f2daf786e9d6b4f500317bb7",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "1dbbab0b68863db048db8374eb191f908bbb1a55481791f425fc8c647a5cbaee",
    "source_fingerprint_before_c3": "1dbbab0b68863db048db8374eb191f908bbb1a55481791f425fc8c647a5cbaee",
    "source_lines": "L7939-L8077",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R021"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-006"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R021",
  "title": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Storefront",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R022 — Permission hỗ trợ Scope linh hoạt. Bao gồm: Customer Portal

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R022",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "000c7a30a2fe2639429933bdb77e5c4cd83bd8adee144d377d06ef42cae634f7"
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
        "BRD-WS-16-R022-AC001",
        "BRD-WS-16-R022-AC003",
        "BRD-WS-16-R022-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R022-O001",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-16-R022-AC002",
        "BRD-WS-16-R022-AC003",
        "BRD-WS-16-R022-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R022-O002",
      "obligation_text": "Bao gồm: Customer Portal"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R022 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R022 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R022 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R022-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R022-AC001",
        "BRD-WS-16-R022-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R022 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Customer Portal.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R022",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-006",
    "source_context_sha256": "f07eaa73f91bac65267fd0ce84085c9976ac9a47f2daf786e9d6b4f500317bb7",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "000c7a30a2fe2639429933bdb77e5c4cd83bd8adee144d377d06ef42cae634f7",
    "source_fingerprint_before_c3": "000c7a30a2fe2639429933bdb77e5c4cd83bd8adee144d377d06ef42cae634f7",
    "source_lines": "L8079-L8217",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R022"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-006"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R022",
  "title": "Permission hỗ trợ Scope linh hoạt. Bao gồm: Customer Portal",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R023 — Permission hỗ trợ Scope linh hoạt. Bao gồm: User

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R023",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "1e12703e395f928653537493f3d2d640ce52a1bb351182052c163f5921200559"
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
        "BRD-WS-16-R023-AC001",
        "BRD-WS-16-R023-AC003",
        "BRD-WS-16-R023-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R023-O001",
      "obligation_text": "Permission hỗ trợ Scope linh hoạt"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-16-R023-AC002",
        "BRD-WS-16-R023-AC003",
        "BRD-WS-16-R023-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R023-O002",
      "obligation_text": "Bao gồm: User"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R023-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R023 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R023 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R023-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R023-AC001",
        "BRD-WS-16-R023-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R023 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission hỗ trợ Scope linh hoạt. Bao gồm: User.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-006",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R023",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-16-006",
    "source_context_sha256": "f07eaa73f91bac65267fd0ce84085c9976ac9a47f2daf786e9d6b4f500317bb7",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "1e12703e395f928653537493f3d2d640ce52a1bb351182052c163f5921200559",
    "source_fingerprint_before_c3": "1e12703e395f928653537493f3d2d640ce52a1bb351182052c163f5921200559",
    "source_lines": "L8219-L8359",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R023"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-006"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-006"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R023",
  "title": "Permission hỗ trợ Scope linh hoạt. Bao gồm: User",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R024 — Audit Log là Business Object

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-002",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R024",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "9322b5dfb2a676b271adf34de61d4034891c534ac2a0483066db27c9f258050a"
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
        "BRD-WS-16-R024-AC001",
        "BRD-WS-16-R024-AC002",
        "BRD-WS-16-R024-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R024-O001",
      "obligation_text": "Audit Log là Business Object"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R024-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R024 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R024 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R024-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R024-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R024 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Audit Log là Business Object.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-002",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-016",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R024",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Audit Logging",
    "source_context_sha256": "c3a223ed8456790c07473f29edd0f53592bcc7df96f85b5cef84a1546f158902",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "9322b5dfb2a676b271adf34de61d4034891c534ac2a0483066db27c9f258050a",
    "source_fingerprint_before_c3": "9322b5dfb2a676b271adf34de61d4034891c534ac2a0483066db27c9f258050a",
    "source_lines": "L8361-L8490",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R024"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-016"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-016"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R024",
  "title": "Audit Log là Business Object",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R025 — Audit ghi nhận đầy đủ các Security Event và Business Event quan trọng

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-002",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R025",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "878acc47ed9cbac87aa6d2686ca2f2350ac0e450d28381bc1c095b795224e217"
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
        "BRD-WS-16-R025-AC001",
        "BRD-WS-16-R025-AC002",
        "BRD-WS-16-R025-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R025-O001",
      "obligation_text": "Audit ghi nhận đầy đủ các Security Event và Business Event quan trọng"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R025-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R025 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R025 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R025-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R025-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R025 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Audit ghi nhận đầy đủ các Security Event và Business Event quan trọng.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-002",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-016",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R025",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "18. Audit Logging",
    "source_context_sha256": "c3a223ed8456790c07473f29edd0f53592bcc7df96f85b5cef84a1546f158902",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "878acc47ed9cbac87aa6d2686ca2f2350ac0e450d28381bc1c095b795224e217",
    "source_fingerprint_before_c3": "878acc47ed9cbac87aa6d2686ca2f2350ac0e450d28381bc1c095b795224e217",
    "source_lines": "L8492-L8621",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R025"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-016"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-016"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R025",
  "title": "Audit ghi nhận đầy đủ các Security Event và Business Event quan trọng",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R026 — Risk Rule là Business Object

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
      "requirement_id": "BRD-WS-16-R026",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "0592952aaa533ef2c78b6579b2d65df7de2f48101bfd3918e68419848d3d64ea"
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
        "BRD-WS-16-R026-AC001",
        "BRD-WS-16-R026-AC002",
        "BRD-WS-16-R026-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R026-O001",
      "obligation_text": "Risk Rule là Business Object"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Risk Rule là Business Object.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-021",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R026",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Risk Rule",
    "source_context_sha256": "79a6378d5d297d3ac4b6561a2c177377d25cd033018faace37cf7d681b9ad773",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "0592952aaa533ef2c78b6579b2d65df7de2f48101bfd3918e68419848d3d64ea",
    "source_fingerprint_before_c3": "0592952aaa533ef2c78b6579b2d65df7de2f48101bfd3918e68419848d3d64ea",
    "source_lines": "L8623-L8715",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R026"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-021"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-021"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R026",
  "title": "Risk Rule là Business Object",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R027 — Risk Rule được cấu hình

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
      "requirement_id": "BRD-WS-16-R027",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "d9bda01c6ac298659746a870ae17ab83fedd4fac8b72ee4c96bf464f17a85574"
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
        "BRD-WS-16-R027-AC001",
        "BRD-WS-16-R027-AC002",
        "BRD-WS-16-R027-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R027-O001",
      "obligation_text": "Risk Rule được cấu hình"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Risk Rule được cấu hình.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-021",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R027",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Risk Rule",
    "source_context_sha256": "79a6378d5d297d3ac4b6561a2c177377d25cd033018faace37cf7d681b9ad773",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "d9bda01c6ac298659746a870ae17ab83fedd4fac8b72ee4c96bf464f17a85574",
    "source_fingerprint_before_c3": "d9bda01c6ac298659746a870ae17ab83fedd4fac8b72ee4c96bf464f17a85574",
    "source_lines": "L8717-L8809",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R027"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-021"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-021"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R027",
  "title": "Risk Rule được cấu hình",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R028 — Không Hard-code

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
      "requirement_id": "BRD-WS-16-R028",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "4a4f9fc70196c62582583bd1f5a465fcfd49191969988f4db3f00452e0acf501"
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
        "BRD-WS-16-R028-AC001",
        "BRD-WS-16-R028-AC002",
        "BRD-WS-16-R028-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R028-O001",
      "obligation_text": "Không Hard-code"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Không Hard-code.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-021",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R028",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "23. Risk Rule",
    "source_context_sha256": "79a6378d5d297d3ac4b6561a2c177377d25cd033018faace37cf7d681b9ad773",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "4a4f9fc70196c62582583bd1f5a465fcfd49191969988f4db3f00452e0acf501",
    "source_fingerprint_before_c3": "4a4f9fc70196c62582583bd1f5a465fcfd49191969988f4db3f00452e0acf501",
    "source_lines": "L8811-L8903",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R028"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-021"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-021"
    ]
  },
  "requirement_type": "DATA_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R028",
  "title": "Không Hard-code",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R029 — Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Identity

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R029",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "3a7027786c0edf699d82612bc66d2ac9328a84722c9ca8b79c263e9d0e81859a"
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
        "BRD-WS-16-R029-AC001",
        "BRD-WS-16-R029-AC002",
        "BRD-WS-16-R029-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R029-O001",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Identity"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R029-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R029 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R029 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R029-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R029-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R029 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Identity.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-16-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R029",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-010",
    "source_context_sha256": "1c09cca794138eb3a085b4ae5d2fcfdfff8a1512233750352fe24b0e570d1c62",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "3a7027786c0edf699d82612bc66d2ac9328a84722c9ca8b79c263e9d0e81859a",
    "source_fingerprint_before_c3": "3a7027786c0edf699d82612bc66d2ac9328a84722c9ca8b79c263e9d0e81859a",
    "source_lines": "L8905-L9034",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R029"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-16-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-16-010"
    ]
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R029",
  "title": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Identity",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R030 — Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Role

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R030",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "d1ebb6aa1c599d56220c727104ab6589af3339142f254f491797a5f9becf8f3e"
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
        "BRD-WS-16-R030-AC001",
        "BRD-WS-16-R030-AC002",
        "BRD-WS-16-R030-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R030-O001",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Role"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R030 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R030 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R030 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R030-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R030-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R030 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Role.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-16-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R030",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-010",
    "source_context_sha256": "1c09cca794138eb3a085b4ae5d2fcfdfff8a1512233750352fe24b0e570d1c62",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "d1ebb6aa1c599d56220c727104ab6589af3339142f254f491797a5f9becf8f3e",
    "source_fingerprint_before_c3": "d1ebb6aa1c599d56220c727104ab6589af3339142f254f491797a5f9becf8f3e",
    "source_lines": "L9036-L9163",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R030"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-16-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-16-010"
    ]
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R030",
  "title": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Role",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R031 — Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Permission

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R031",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "7a3cf66e84bac141e106a31055b10d51ebb5ddb9d4c9f6d54206360f295c9d31"
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
        "BRD-WS-16-R031-AC001",
        "BRD-WS-16-R031-AC002",
        "BRD-WS-16-R031-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R031-O001",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R031-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R031 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R031 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R031-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R031-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R031 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Permission.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-16-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R031",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-010",
    "source_context_sha256": "1c09cca794138eb3a085b4ae5d2fcfdfff8a1512233750352fe24b0e570d1c62",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "7a3cf66e84bac141e106a31055b10d51ebb5ddb9d4c9f6d54206360f295c9d31",
    "source_fingerprint_before_c3": "7a3cf66e84bac141e106a31055b10d51ebb5ddb9d4c9f6d54206360f295c9d31",
    "source_lines": "L9165-L9294",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R031"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-16-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-16-010"
    ]
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R031",
  "title": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Permission",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R032 — Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Data Scope

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R032",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "1f827be6a74aac1d26a1457f323e54fc03b495a86b3ef924221a7ceba05866c3"
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
        "BRD-WS-16-R032-AC001",
        "BRD-WS-16-R032-AC002",
        "BRD-WS-16-R032-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R032-O001",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Data Scope"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R032 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R032 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R032 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R032-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R032-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R032 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Data Scope.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-16-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R032",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-010",
    "source_context_sha256": "1c09cca794138eb3a085b4ae5d2fcfdfff8a1512233750352fe24b0e570d1c62",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "1f827be6a74aac1d26a1457f323e54fc03b495a86b3ef924221a7ceba05866c3",
    "source_fingerprint_before_c3": "1f827be6a74aac1d26a1457f323e54fc03b495a86b3ef924221a7ceba05866c3",
    "source_lines": "L9296-L9423",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R032"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-16-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-16-010"
    ]
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R032",
  "title": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Data Scope",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R033 — Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Organization Relatio…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R033",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "32614e39d0e182bf2c15fc624d3e2003377898cac0d193629198e8a866de1a57"
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
        "BRD-WS-16-R033-AC001",
        "BRD-WS-16-R033-AC002",
        "BRD-WS-16-R033-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R033-O001",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Organization Relationship"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R033 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R033 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R033 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R033-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R033-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R033 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Organization Relationship.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-16-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R033",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-010",
    "source_context_sha256": "1c09cca794138eb3a085b4ae5d2fcfdfff8a1512233750352fe24b0e570d1c62",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "32614e39d0e182bf2c15fc624d3e2003377898cac0d193629198e8a866de1a57",
    "source_fingerprint_before_c3": "32614e39d0e182bf2c15fc624d3e2003377898cac0d193629198e8a866de1a57",
    "source_lines": "L9425-L9552",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R033"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-16-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-16-010"
    ]
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R033",
  "title": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Organization Relatio…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R034 — Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Support Policy

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R034",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "919a8c35fb2dc867e1a18a7f4c5b5820ccc2c4e1bb71d6f863dd803c3998f2ef"
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
        "BRD-WS-16-R034-AC001",
        "BRD-WS-16-R034-AC002",
        "BRD-WS-16-R034-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R034-O001",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Support Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R034 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R034 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R034 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R034-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R034-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R034 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Support Policy.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-16-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R034",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-010",
    "source_context_sha256": "1c09cca794138eb3a085b4ae5d2fcfdfff8a1512233750352fe24b0e570d1c62",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "919a8c35fb2dc867e1a18a7f4c5b5820ccc2c4e1bb71d6f863dd803c3998f2ef",
    "source_fingerprint_before_c3": "919a8c35fb2dc867e1a18a7f4c5b5820ccc2c4e1bb71d6f863dd803c3998f2ef",
    "source_lines": "L9554-L9681",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R034"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-16-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-16-010"
    ]
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R034",
  "title": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Support Policy",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R035 — Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Customer Consent

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R035",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "dd4ef479f8632cd0257581f0f0b7a62229929483c8caa1a486368dbc32b3c1b9"
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
        "BRD-WS-16-R035-AC001",
        "BRD-WS-16-R035-AC002",
        "BRD-WS-16-R035-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R035-O001",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Customer Consent"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R035-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R035 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R035 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R035-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R035-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R035 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Customer Consent.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-16-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R035",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-010",
    "source_context_sha256": "1c09cca794138eb3a085b4ae5d2fcfdfff8a1512233750352fe24b0e570d1c62",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "dd4ef479f8632cd0257581f0f0b7a62229929483c8caa1a486368dbc32b3c1b9",
    "source_fingerprint_before_c3": "dd4ef479f8632cd0257581f0f0b7a62229929483c8caa1a486368dbc32b3c1b9",
    "source_lines": "L9683-L9812",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R035"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-16-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-16-010"
    ]
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R035",
  "title": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Customer Consent",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R036 — Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Data Classification

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R036",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "5e3421d1935ecbdadd8271367153d867b5f0018f4acde20c6681a6f26f1a4313"
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
        "BRD-WS-16-R036-AC001",
        "BRD-WS-16-R036-AC002",
        "BRD-WS-16-R036-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R036-O001",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Data Classification"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R036 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R036 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R036 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R036-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R036-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R036 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Data Classification.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-16-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R036",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-010",
    "source_context_sha256": "1c09cca794138eb3a085b4ae5d2fcfdfff8a1512233750352fe24b0e570d1c62",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "5e3421d1935ecbdadd8271367153d867b5f0018f4acde20c6681a6f26f1a4313",
    "source_fingerprint_before_c3": "5e3421d1935ecbdadd8271367153d867b5f0018f4acde20c6681a6f26f1a4313",
    "source_lines": "L9814-L9941",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R036"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-16-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-16-010"
    ]
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R036",
  "title": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Data Classification",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R037 — Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Security Policy

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R037",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "58d914728df6c58bd5e6becf2a0459d7a8bd21a22463522fe73fce9c201d3108"
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
        "BRD-WS-16-R037-AC001",
        "BRD-WS-16-R037-AC002",
        "BRD-WS-16-R037-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R037-O001",
      "obligation_text": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Security Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R037-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R037 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R037 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R037-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R037-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R037 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Security Policy.",
  "provenance": {
    "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "EP-16-010",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R037",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_CHILD"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-010",
    "source_context_sha256": "1c09cca794138eb3a085b4ae5d2fcfdfff8a1512233750352fe24b0e570d1c62",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "58d914728df6c58bd5e6becf2a0459d7a8bd21a22463522fe73fce9c201d3108",
    "source_fingerprint_before_c3": "58d914728df6c58bd5e6becf2a0459d7a8bd21a22463522fe73fce9c201d3108",
    "source_lines": "L9943-L10072",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R037"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "EP-16-010"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "EP-16-010"
    ]
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R037",
  "title": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: Security Policy",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R038 — Identity Platform phải triển khai active provider set v2.3 gồm Local Account, Google, Apple, Fac…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007",
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R038",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "28686d4d3518524c274adaeb0797a7e015e56c8542384319950767fa4db040c5"
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
        "BRD-WS-16-R038-AC001",
        "BRD-WS-16-R038-AC002",
        "BRD-WS-16-R038-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R038-O001",
      "obligation_text": "Identity Platform phải triển khai active provider set v2.3 gồm Local Account, Google, Apple, Facebook, Microsoft, Line và WeChat"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R038-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R038 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R038 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R038-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R038-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R038 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Identity Platform phải triển khai active provider set v2.3 gồm Local Account, Google, Apple, Facebook, Microsoft, Line và WeChat.",
  "provenance": {
    "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
    "approved_decisions": [
      "P2-DEC-007",
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-001",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R038",
    "phase_2c_c3_actions": [
      "C3_APPROVED_DECISION_ATOMIC_SPLIT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Identity Platform",
    "source_context_sha256": "ca12b94f6cb8f68e320a33d7aac6af2a3ebdccbb25d4606c21fddb218b322bd9",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "28686d4d3518524c274adaeb0797a7e015e56c8542384319950767fa4db040c5",
    "source_fingerprint_before_c3": "28686d4d3518524c274adaeb0797a7e015e56c8542384319950767fa4db040c5",
    "source_lines": "L10074-L10205",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R038"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-001"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-001"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R038",
  "title": "Identity Platform phải triển khai active provider set v2.3 gồm Local Account, Google, Apple, Fac…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R039 — Identity provider connector phải có khả năng bổ sung provider tương lai mà không thay đổi Identi…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-007",
        "P2-DEC-008",
        "V23-P2C-ACCEPTANCE-MAPPING-C3"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-16-R039",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "55bdd72e28eccb77d78c0e767f9ff137c0588c69f1bc0a5e08c5c7da3094dce4"
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
        "BRD-WS-16-R039-AC001",
        "BRD-WS-16-R039-AC003",
        "BRD-WS-16-R039-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R039-O001",
      "obligation_text": "Identity provider connector phải có khả năng bổ sung provider tương lai mà không thay đổi Identity Domain business logic"
    },
    {
      "acceptance_criterion_references": [
        "BRD-WS-16-R039-AC002",
        "BRD-WS-16-R039-AC003",
        "BRD-WS-16-R039-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R039-O002",
      "obligation_text": "provider tương lai không được tính là active implementation khi chưa có approved requirement"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Identity provider connector phải có khả năng bổ sung provider tương lai mà không thay đổi Identity Domain business logic; provider tương lai không được tính là active implementation khi chưa có approved requirement.",
  "provenance": {
    "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
    "approved_decisions": [
      "P2-DEC-007",
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BD-16-001",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R039",
    "phase_2c_c3_actions": [
      "C3_APPROVED_DECISION_ATOMIC_SPLIT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "3. Identity Platform",
    "source_context_sha256": "ca12b94f6cb8f68e320a33d7aac6af2a3ebdccbb25d4606c21fddb218b322bd9",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "55bdd72e28eccb77d78c0e767f9ff137c0588c69f1bc0a5e08c5c7da3094dce4",
    "source_fingerprint_before_c3": "55bdd72e28eccb77d78c0e767f9ff137c0588c69f1bc0a5e08c5c7da3094dce4",
    "source_lines": "L10207-L10313",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R039"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BD-16-001"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BD-16-001"
    ]
  },
  "requirement_type": "DESIGN_PRINCIPLE",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R039",
  "title": "Identity provider connector phải có khả năng bổ sung provider tương lai mà không thay đổi Identi…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R040 — Authorization và Permission model đã được phê duyệt cho v2.3 phải được thực thi trong active sco…

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
      "requirement_id": "BRD-WS-16-R040",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "3337ad932f16697b05539a806cc32cff015a3297720802fa7b7caed525bd7411"
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
        "BRD-WS-16-R040-AC001",
        "BRD-WS-16-R040-AC002",
        "BRD-WS-16-R040-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-16-R040-O001",
      "obligation_text": "Authorization và Permission model đã được phê duyệt cho v2.3 phải được thực thi trong active scope"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R040-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R040 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R040 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R040-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-16-R040-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-16-R040 does not define a recovery obligation."
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Authorization và Permission model đã được phê duyệt cho v2.3 phải được thực thi trong active scope.",
  "provenance": {
    "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BRD-WS-16-R002",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R040",
    "phase_2c_c3_actions": [
      "C3_APPROVED_DECISION_ATOMIC_SPLIT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Authorization Model",
    "source_context_sha256": "056a4758658cb438ed24160bbd341ea1563558eba2f30d3492f97a940f925c9c",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "3337ad932f16697b05539a806cc32cff015a3297720802fa7b7caed525bd7411",
    "source_fingerprint_before_c3": "3337ad932f16697b05539a806cc32cff015a3297720802fa7b7caed525bd7411",
    "source_lines": "L10315-L10442",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R040"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-WS-16-R002"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-WS-16-R002"
    ]
  },
  "requirement_type": "SECURITY_REQUIREMENT",
  "scope_coverage_unit": true,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "BRD-WS-16-R040",
  "title": "Authorization và Permission model đã được phê duyệt cho v2.3 phải được thực thi trong active sco…",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-16-R041 — Advanced complex authorization model là future extensibility và không phải active v2.3 feature

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "NOT_APPLICABLE_FOR_V2.3",
    "inference": false,
    "requirement_id": "BRD-WS-16-R041",
    "scope_status": "FUTURE"
  },
  "acceptance_mechanism": {
    "inference": false,
    "mechanism": "NOT_APPLICABLE_FOR_V2.3",
    "runtime_status": "NOT_APPLICABLE_FOR_V2.3"
  },
  "acceptance_rationale": "This record is not an active canonical atomic v2.3 acceptance unit.",
  "acceptance_schema_version": "PROGRESSIVE-1.0.0",
  "acceptance_status": "NOT_APPLICABLE_FOR_V2.3",
  "acceptance_unit": false,
  "atomic_obligations": [],
  "criticality_applicability": null,
  "criticality_unit": false,
  "delivery_commitment": "POST_V2.3",
  "implementation_unit": false,
  "lifecycle": "RETAINED_SCOPE_RECORD",
  "normative_statement": "Advanced complex authorization model là future extensibility và không phải active v2.3 feature.",
  "provenance": {
    "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
    "approved_decisions": [
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "derived_from_parent": "BRD-WS-16-R002",
    "identity_origin": "PHASE_2C_C3_NEW_STABLE_ID_ALLOCATION",
    "original_identity": "BRD-WS-16-R041",
    "phase_2c_c3_actions": [
      "C3_APPROVED_DECISION_ATOMIC_SPLIT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "6. Authorization Model",
    "source_context_sha256": "056a4758658cb438ed24160bbd341ea1563558eba2f30d3492f97a940f925c9c",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "4516152c3615ea4941e93aa566b7ad035dbc6e87d854a275993fa3b74d2d65cc",
    "source_fingerprint_before_c3": "4516152c3615ea4941e93aa566b7ad035dbc6e87d854a275993fa3b74d2d65cc",
    "source_lines": "L10444-L10517",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-16-R041"
  },
  "record_kind": "CANONICAL_ATOMIC",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": null,
    "derived_from": [
      "BRD-WS-16-R002"
    ],
    "derived_requirements": [],
    "satisfies_composite_parents": [
      "BRD-WS-16-R002"
    ]
  },
  "requirement_type": "SCOPE_CONSTRAINT",
  "scope_coverage_unit": false,
  "scope_status": "FUTURE",
  "stable_id": "BRD-WS-16-R041",
  "title": "Advanced complex authorization model là future extensibility và không phải active v2.3 feature",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### EP-16-001 — Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: - Customer - User - Organiz…

```json
{
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-16-001",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "7acc68f882f1ccccf56a0d8a373b69cc7697e1309a80c76e6e9188dd6710f01a"
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
        "EP-16-001-AC001",
        "EP-16-001-AC006",
        "EP-16-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-001-O001",
      "obligation_text": "Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: Customer"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-001-AC002",
        "EP-16-001-AC006",
        "EP-16-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-001-O002",
      "obligation_text": "Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: User"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-001-AC003",
        "EP-16-001-AC006",
        "EP-16-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-001-O003",
      "obligation_text": "Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: Organization Owner"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-001-AC004",
        "EP-16-001-AC006",
        "EP-16-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-001-O004",
      "obligation_text": "Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: API Client"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-001-AC005",
        "EP-16-001-AC006",
        "EP-16-001-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-001-O005",
      "obligation_text": "Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: Service Account"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-001-AC007"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-001 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-001 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-001-AC006"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-001-AC001",
        "EP-16-001-AC002",
        "EP-16-001-AC003",
        "EP-16-001-AC004",
        "EP-16-001-AC005"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-001 does not define a recovery obligation."
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
    "source_fingerprint": "7acc68f882f1ccccf56a0d8a373b69cc7697e1309a80c76e6e9188dd6710f01a",
    "source_lines": "L10519-L10677",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-16-001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-16-002",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "d9d827ac99559396f6b9bcf03aa6f3bd794e23d4cbc299d092afc0d8f4cb30bc"
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
        "EP-16-002-AC001",
        "EP-16-002-AC003",
        "EP-16-002-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-002-O001",
      "obligation_text": "Permission được đánh giá động"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-002-AC002",
        "EP-16-002-AC003",
        "EP-16-002-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-002-O002",
      "obligation_text": "Không sử dụng Permission tĩnh"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-002-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-002 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-002 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-002-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-002-AC001",
        "EP-16-002-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-002 does not define a recovery obligation."
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
    "source_fingerprint": "d9d827ac99559396f6b9bcf03aa6f3bd794e23d4cbc299d092afc0d8f4cb30bc",
    "source_lines": "L10679-L10800",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-16-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-16-003",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "6b9f65c14c393f45631bcefe1b1169ebd9099e08f86aed85d672a35680099e85"
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
        "EP-16-003-AC001",
        "EP-16-003-AC003",
        "EP-16-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-003-O001",
      "obligation_text": "Permission Evaluation Engine là điểm đánh giá Permission duy nhất"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-003-AC002",
        "EP-16-003-AC003",
        "EP-16-003-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-003-O002",
      "obligation_text": "Business Domain không tự xử lý Permission"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-003-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-003 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-003 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-003-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-003-AC001",
        "EP-16-003-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-003 does not define a recovery obligation."
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
    "source_fingerprint": "6b9f65c14c393f45631bcefe1b1169ebd9099e08f86aed85d672a35680099e85",
    "source_lines": "L10802-L10923",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-16-003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-16-004",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "81619193a7b7b15925803efa0df7503c683e238a6282e11b0d3f528fccfa0977"
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
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-004-AC004"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-004 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-004 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-004-AC003"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-004-AC001",
        "EP-16-004-AC002"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-004 does not define a recovery obligation."
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
    "source_fingerprint": "81619193a7b7b15925803efa0df7503c683e238a6282e11b0d3f528fccfa0977",
    "source_lines": "L10925-L11046",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-16-004"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "Previously authenticated context may inform policy but never bypass current evaluation"
    ],
    "concrete_bindings": [
      {
        "expected_outcome": {
          "authoritative_source": {
            "allowed_identifiers": [
              "EP-16-005.POLICY.OUTCOME.CONFORMING"
            ],
            "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
            "source_type": "SOURCE_LITERAL",
            "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
          },
          "identifier": "EP-16-005.POLICY.OUTCOME.CONFORMING",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
            "source_lines": "L1095-L1100",
            "source_section": "32. Enterprise Design Principles > EP-16-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "CANONICAL_OUTCOME",
            "resolver_id": "RESOLVE.EP-16-005.EP-16-005.POLICY.OUTCOME.CONFORMING",
            "version": "1.0.0"
          },
          "semantic_type": "CANONICAL_OUTCOME"
        },
        "policy": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
            "source_type": "SOURCE_LITERAL",
            "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
          },
          "identifier": "EP-16-005.POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
            "source_lines": "L1095-L1100",
            "source_section": "32. Enterprise Design Principles > EP-16-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.EP-16-005.EP-16-005.POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "policy_inputs": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
            "source_type": "SOURCE_LITERAL",
            "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
          },
          "identifier": "EP-16-005.POLICY_INPUTS",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
            "source_lines": "L1095-L1100",
            "source_section": "32. Enterprise Design Principles > EP-16-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "RESOLVE.EP-16-005.EP-16-005.POLICY_INPUTS",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "policy_version": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
            "source_type": "SOURCE_LITERAL",
            "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
          },
          "identifier": "EP-16-005.POLICY_VERSION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
            "source_lines": "L1095-L1100",
            "source_section": "32. Enterprise Design Principles > EP-16-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_VERSION",
            "resolver_id": "RESOLVE.EP-16-005.EP-16-005.POLICY_VERSION",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_VERSION"
        }
      },
      {
        "action": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
            "source_type": "SOURCE_LITERAL",
            "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
          },
          "identifier": "EP-16-005.ACTION",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.ACTION.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
            "source_lines": "L1095-L1100",
            "source_section": "32. Enterprise Design Principles > EP-16-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ACTION_ID",
            "resolver_id": "RESOLVE.EP-16-005.EP-16-005.ACTION",
            "version": "1.0.0"
          },
          "semantic_type": "ACTION_ID"
        },
        "actor": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
            "source_type": "SOURCE_LITERAL",
            "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
          },
          "identifier": "EP-16-005.ACTOR",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.ACTOR.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
            "source_lines": "L1095-L1100",
            "source_section": "32. Enterprise Design Principles > EP-16-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "PRINCIPAL_ID",
            "resolver_id": "RESOLVE.EP-16-005.EP-16-005.ACTOR",
            "version": "1.0.0"
          },
          "semantic_type": "PRINCIPAL_ID"
        },
        "effective_policy": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
            "source_type": "SOURCE_LITERAL",
            "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
          },
          "identifier": "EP-16-005.EFFECTIVE_POLICY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.EFFECTIVE_POLICY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
            "source_lines": "L1095-L1100",
            "source_section": "32. Enterprise Design Principles > EP-16-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.EP-16-005.EP-16-005.EFFECTIVE_POLICY",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "resource": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
            "source_type": "SOURCE_LITERAL",
            "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
          },
          "identifier": "EP-16-005.RESOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.RESOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
            "source_lines": "L1095-L1100",
            "source_section": "32. Enterprise Design Principles > EP-16-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "RESOURCE_ID",
            "resolver_id": "RESOLVE.EP-16-005.EP-16-005.RESOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "RESOURCE_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.EP-16-005",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "Request is allowed because it is implicitly trusted"
    ],
    "operator_composition": [
      "POLICY_OUTCOME_EQUALS",
      "ACTOR_DENIED"
    ],
    "positive_oracle": [
      "Request receives explicit allow, challenge, deny or review outcome; no request is trusted by default"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
      "source_lines": "L1095-L1100",
      "source_section": "32. Enterprise Design Principles > EP-16-005"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
          "source_type": "SOURCE_LITERAL",
          "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
        },
        "identifier": "EP-16-005.EP-16-005.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "EP-16-005.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-16.md",
          "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
          "source_lines": "L1095-L1100",
          "source_section": "32. Enterprise Design Principles > EP-16-005"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.EP-16-005.EP-16-005.EP-16-005.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "EP-16-005.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.REQUEST_ID",
        "FIELD.PRINCIPAL_ID",
        "FIELD.CONTEXT",
        "FIELD.POLICY_VERSION",
        "FIELD.DECISION",
        "FIELD.REASON",
        "FIELD.AUDIT_RECORD"
      ],
      "producer": "EP-16-005.EVIDENCE.PRODUCER",
      "required_collection_origin": "EP-16-005.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.REQUEST_ID",
        "FIELD.PRINCIPAL_ID",
        "FIELD.CONTEXT",
        "FIELD.POLICY_VERSION",
        "FIELD.DECISION",
        "FIELD.REASON",
        "FIELD.AUDIT_RECORD"
      ],
      "required_values_or_hashes": [
        "EP-16-005.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "EP-16-005.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "EP-16-005.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "EP-16-005-O001",
      "EP-16-005-O002"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS",
          "evaluator_consumed_bindings": [
            "expected_outcome",
            "policy",
            "policy_inputs",
            "policy_version"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
              "source_type": "SOURCE_LITERAL",
              "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
            },
            "identifier": "EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-16.md",
              "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
              "source_lines": "L1095-L1100",
              "source_section": "32. Enterprise Design Principles > EP-16-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.EP-16-005.EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
              "source_type": "SOURCE_LITERAL",
              "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
            },
            "identifier": "EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-16.md",
              "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
              "source_lines": "L1095-L1100",
              "source_section": "32. Enterprise Design Principles > EP-16-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "RESOLVE.EP-16-005.EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
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
                    "EP-16-005.POLICY.OUTCOME.CONFORMING"
                  ],
                  "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
                },
                "identifier": "EP-16-005.POLICY.OUTCOME.CONFORMING",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                  "source_lines": "L1095-L1100",
                  "source_section": "32. Enterprise Design Principles > EP-16-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.EP-16-005.EP-16-005.POLICY.OUTCOME.CONFORMING",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "policy": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
                },
                "identifier": "EP-16-005.POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                  "source_lines": "L1095-L1100",
                  "source_section": "32. Enterprise Design Principles > EP-16-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.EP-16-005.EP-16-005.POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "policy_inputs": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
                },
                "identifier": "EP-16-005.POLICY_INPUTS",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                  "source_lines": "L1095-L1100",
                  "source_section": "32. Enterprise Design Principles > EP-16-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "EVIDENCE_OBJECT_REF",
                  "resolver_id": "RESOLVE.EP-16-005.EP-16-005.POLICY_INPUTS",
                  "version": "1.0.0"
                },
                "semantic_type": "EVIDENCE_OBJECT_REF"
              },
              "policy_version": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
                },
                "identifier": "EP-16-005.POLICY_VERSION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                  "source_lines": "L1095-L1100",
                  "source_section": "32. Enterprise Design Principles > EP-16-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_VERSION",
                  "resolver_id": "RESOLVE.EP-16-005.EP-16-005.POLICY_VERSION",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_VERSION"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
                },
                "identifier": "EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                  "source_lines": "L1095-L1100",
                  "source_section": "32. Enterprise Design Principles > EP-16-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "RESOLVE.EP-16-005.EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              },
              "observed": {
                "authoritative_source": {
                  "allowed_identifiers": [
                    "EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
                  ],
                  "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
                },
                "identifier": "EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                  "source_lines": "L1095-L1100",
                  "source_section": "32. Enterprise Design Principles > EP-16-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "CANONICAL_OUTCOME",
                  "resolver_id": "OBSERVE.EP-16-005.EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "CANONICAL_OUTCOME"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                "source_type": "SOURCE_LITERAL",
                "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
              },
              "identifier": "EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                "source_lines": "L1095-L1100",
                "source_section": "32. Enterprise Design Principles > EP-16-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.EP-16-005.EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "POLICY_OUTCOME_EQUALS"
          },
          "obligation_id": "EP-16-005-O001",
          "observed_operand": {
            "authoritative_source": {
              "allowed_identifiers": [
                "EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT"
              ],
              "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
              "source_type": "SOURCE_LITERAL",
              "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
            },
            "identifier": "EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-16.md",
              "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
              "source_lines": "L1095-L1100",
              "source_section": "32. Enterprise Design Principles > EP-16-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "CANONICAL_OUTCOME",
              "resolver_id": "OBSERVE.EP-16-005.EP-16-005.EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.CANONICAL.RESULT",
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
                  "EP-16-005.POLICY.OUTCOME.CONFORMING"
                ],
                "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                "source_type": "SOURCE_LITERAL",
                "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
              },
              "identifier": "EP-16-005.POLICY.OUTCOME.CONFORMING",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.EXPECTED_OUTCOME.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                "source_lines": "L1095-L1100",
                "source_section": "32. Enterprise Design Principles > EP-16-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "CANONICAL_OUTCOME",
                "resolver_id": "RESOLVE.EP-16-005.EP-16-005.POLICY.OUTCOME.CONFORMING",
                "version": "1.0.0"
              },
              "semantic_type": "CANONICAL_OUTCOME"
            },
            "policy": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                "source_type": "SOURCE_LITERAL",
                "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
              },
              "identifier": "EP-16-005.POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.POLICY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                "source_lines": "L1095-L1100",
                "source_section": "32. Enterprise Design Principles > EP-16-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.EP-16-005.EP-16-005.POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "policy_inputs": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                "source_type": "SOURCE_LITERAL",
                "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
              },
              "identifier": "EP-16-005.POLICY_INPUTS",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.POLICY_INPUTS.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                "source_lines": "L1095-L1100",
                "source_section": "32. Enterprise Design Principles > EP-16-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "RESOLVE.EP-16-005.EP-16-005.POLICY_INPUTS",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "policy_version": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                "source_type": "SOURCE_LITERAL",
                "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
              },
              "identifier": "EP-16-005.POLICY_VERSION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS.POLICY_VERSION.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                "source_lines": "L1095-L1100",
                "source_section": "32. Enterprise Design Principles > EP-16-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_VERSION",
                "resolver_id": "RESOLVE.EP-16-005.EP-16-005.POLICY_VERSION",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_VERSION"
            }
          }
        },
        {
          "assertion_id": "EP-16-005.O2.1.ACTOR_DENIED",
          "evaluator_consumed_bindings": [
            "action",
            "actor",
            "effective_policy",
            "resource"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
              "source_type": "SOURCE_LITERAL",
              "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
            },
            "identifier": "EP-16-005.EP-16-005.O2.1.ACTOR_DENIED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-16.md",
              "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
              "source_lines": "L1095-L1100",
              "source_section": "32. Enterprise Design Principles > EP-16-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.EP-16-005.EP-16-005.EP-16-005.O2.1.ACTOR_DENIED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
              "source_type": "SOURCE_LITERAL",
              "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
            },
            "identifier": "EP-16-005.EP-16-005.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-16.md",
              "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
              "source_lines": "L1095-L1100",
              "source_section": "32. Enterprise Design Principles > EP-16-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "PRINCIPAL_ID",
              "resolver_id": "RESOLVE.EP-16-005.EP-16-005.EP-16-005.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "PRINCIPAL_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "action": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
                },
                "identifier": "EP-16-005.ACTION",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.ACTION.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                  "source_lines": "L1095-L1100",
                  "source_section": "32. Enterprise Design Principles > EP-16-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ACTION_ID",
                  "resolver_id": "RESOLVE.EP-16-005.EP-16-005.ACTION",
                  "version": "1.0.0"
                },
                "semantic_type": "ACTION_ID"
              },
              "actor": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
                },
                "identifier": "EP-16-005.ACTOR",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.ACTOR.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                  "source_lines": "L1095-L1100",
                  "source_section": "32. Enterprise Design Principles > EP-16-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "PRINCIPAL_ID",
                  "resolver_id": "RESOLVE.EP-16-005.EP-16-005.ACTOR",
                  "version": "1.0.0"
                },
                "semantic_type": "PRINCIPAL_ID"
              },
              "effective_policy": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
                },
                "identifier": "EP-16-005.EFFECTIVE_POLICY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.EFFECTIVE_POLICY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                  "source_lines": "L1095-L1100",
                  "source_section": "32. Enterprise Design Principles > EP-16-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.EP-16-005.EP-16-005.EFFECTIVE_POLICY",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "resource": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
                },
                "identifier": "EP-16-005.RESOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.RESOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                  "source_lines": "L1095-L1100",
                  "source_section": "32. Enterprise Design Principles > EP-16-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "RESOURCE_ID",
                  "resolver_id": "RESOLVE.EP-16-005.EP-16-005.RESOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "RESOURCE_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
                },
                "identifier": "EP-16-005.EP-16-005.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                  "source_lines": "L1095-L1100",
                  "source_section": "32. Enterprise Design Principles > EP-16-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "PRINCIPAL_ID",
                  "resolver_id": "RESOLVE.EP-16-005.EP-16-005.EP-16-005.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "PRINCIPAL_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                  "source_type": "SOURCE_LITERAL",
                  "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
                },
                "identifier": "EP-16-005.EP-16-005.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-16.md",
                  "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                  "source_lines": "L1095-L1100",
                  "source_section": "32. Enterprise Design Principles > EP-16-005"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "PRINCIPAL_ID",
                  "resolver_id": "OBSERVE.EP-16-005.EP-16-005.EP-16-005.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "PRINCIPAL_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                "source_type": "SOURCE_LITERAL",
                "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
              },
              "identifier": "EP-16-005.EP-16-005.O2.1.ACTOR_DENIED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                "source_lines": "L1095-L1100",
                "source_section": "32. Enterprise Design Principles > EP-16-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.EP-16-005.EP-16-005.EP-16-005.O2.1.ACTOR_DENIED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "ACTOR_DENIED"
          },
          "obligation_id": "EP-16-005-O002",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
              "source_type": "SOURCE_LITERAL",
              "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
            },
            "identifier": "EP-16-005.EP-16-005.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-16.md",
              "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
              "source_lines": "L1095-L1100",
              "source_section": "32. Enterprise Design Principles > EP-16-005"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "PRINCIPAL_ID",
              "resolver_id": "OBSERVE.EP-16-005.EP-16-005.EP-16-005.O2.1.ACTOR_DENIED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "PRINCIPAL_ID"
          },
          "operator_id": "ACTOR_DENIED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "action": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                "source_type": "SOURCE_LITERAL",
                "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
              },
              "identifier": "EP-16-005.ACTION",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.ACTION.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                "source_lines": "L1095-L1100",
                "source_section": "32. Enterprise Design Principles > EP-16-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ACTION_ID",
                "resolver_id": "RESOLVE.EP-16-005.EP-16-005.ACTION",
                "version": "1.0.0"
              },
              "semantic_type": "ACTION_ID"
            },
            "actor": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                "source_type": "SOURCE_LITERAL",
                "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
              },
              "identifier": "EP-16-005.ACTOR",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.ACTOR.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                "source_lines": "L1095-L1100",
                "source_section": "32. Enterprise Design Principles > EP-16-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "PRINCIPAL_ID",
                "resolver_id": "RESOLVE.EP-16-005.EP-16-005.ACTOR",
                "version": "1.0.0"
              },
              "semantic_type": "PRINCIPAL_ID"
            },
            "effective_policy": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                "source_type": "SOURCE_LITERAL",
                "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
              },
              "identifier": "EP-16-005.EFFECTIVE_POLICY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.EFFECTIVE_POLICY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                "source_lines": "L1095-L1100",
                "source_section": "32. Enterprise Design Principles > EP-16-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.EP-16-005.EP-16-005.EFFECTIVE_POLICY",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "resource": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
                "source_type": "SOURCE_LITERAL",
                "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
              },
              "identifier": "EP-16-005.RESOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "EP-16-005.O2.1.ACTOR_DENIED.RESOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-16.md",
                "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
                "source_lines": "L1095-L1100",
                "source_section": "32. Enterprise Design Principles > EP-16-005"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "RESOURCE_ID",
                "resolver_id": "RESOLVE.EP-16-005.EP-16-005.RESOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "RESOURCE_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "Previously authenticated context may inform policy but never bypass current evaluation"
      ],
      "contract_ast_sha256": "b5c1e28c05244d25b9accfbf3c80666daf9e48e343ac93483446fe1debfe81eb",
      "contract_id": "P2C.C4.CONTRACT.EP-16-005",
      "criticality": "NORMAL",
      "disposition": "COMPOUND_AST_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-16.md#32. Enterprise Design Principles > EP-16-005",
            "source_type": "SOURCE_LITERAL",
            "version": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e"
          },
          "identifier": "EP-16-005.EP-16-005.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "EP-16-005.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-16.md",
            "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
            "source_lines": "L1095-L1100",
            "source_section": "32. Enterprise Design Principles > EP-16-005"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.EP-16-005.EP-16-005.EP-16-005.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "EP-16-005.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.REQUEST_ID",
          "FIELD.PRINCIPAL_ID",
          "FIELD.CONTEXT",
          "FIELD.POLICY_VERSION",
          "FIELD.DECISION",
          "FIELD.REASON",
          "FIELD.AUDIT_RECORD"
        ],
        "producer": "EP-16-005.EVIDENCE.PRODUCER",
        "required_collection_origin": "EP-16-005.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.REQUEST_ID",
          "FIELD.PRINCIPAL_ID",
          "FIELD.CONTEXT",
          "FIELD.POLICY_VERSION",
          "FIELD.DECISION",
          "FIELD.REASON",
          "FIELD.AUDIT_RECORD"
        ],
        "required_values_or_hashes": [
          "EP-16-005.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "EP-16-005.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "EP-16-005.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-2C4A6288D3A64E622C46",
        "P2C-C4-FX-7C624AC589E2E67F4079",
        "P2C-C4-FX-4DF831E267366ECFAD99"
      ],
      "high_risk_audit_subset": false,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "Request is allowed because it is implicitly trusted"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "EP-16-005-O001",
          "obligation_text": "Platform áp dụng Zero Trust Principle"
        },
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "EP-16-005-O002",
          "obligation_text": "Không có Request nào được mặc định tin cậy"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "EP-16-005.O1.1.POLICY_OUTCOME_EQUALS"
          ],
          "coverage_count": 1,
          "obligation_id": "EP-16-005-O001"
        },
        {
          "assertion_ids": [
            "EP-16-005.O2.1.ACTOR_DENIED"
          ],
          "coverage_count": 1,
          "obligation_id": "EP-16-005-O002"
        }
      ],
      "operator_composition": [
        "POLICY_OUTCOME_EQUALS",
        "ACTOR_DENIED"
      ],
      "positive_oracles": [
        "Request receives explicit allow, challenge, deny or review outcome; no request is trusted by default"
      ],
      "preconditions": [
        "Identity, context and effective policy are evaluated"
      ],
      "prohibitions": [
        "Request is allowed because it is implicitly trusted"
      ],
      "requirement_id": "EP-16-005",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-16.md",
        "source_fingerprint": "36dbbdfc23adb04950e874424e415ac97f5a0ce2aa35e91c11d8226e71fc3f4e",
        "source_lines": "L1095-L1100",
        "source_section": "32. Enterprise Design Principles > EP-16-005"
      },
      "source_statement": "Platform áp dụng Zero Trust Principle. Không có Request nào được mặc định tin cậy.",
      "surrounding_source_context": "## EP-16-005\n\nPlatform áp dụng Zero Trust Principle.\n\nKhông có Request nào được mặc định tin cậy.\n\n---"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.EP-16-005",
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
        "EP-16-005-AC001",
        "EP-16-005-AC003",
        "EP-16-005-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-005-O001",
      "obligation_text": "Platform áp dụng Zero Trust Principle"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-005-AC002",
        "EP-16-005-AC003",
        "EP-16-005-AC004"
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
    "source_fingerprint": "42fa464e1cfc4134041d16b728ced48ef78a8a9a68642dea3d44082a761cab9d",
    "source_lines": "L11048-L12658",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-16-005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [
        "P2-DEC-008"
      ],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-16-006",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "a45c06d451bdca42a937a38924a542987df0c7a8434df8996a528c893a88bdf9"
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
        "EP-16-006-AC001",
        "EP-16-006-AC006",
        "EP-16-006-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-006-O001",
      "obligation_text": "Data Protection được quyết định bởi: Permission"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-006-AC002",
        "EP-16-006-AC006",
        "EP-16-006-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-006-O002",
      "obligation_text": "Data Protection được quyết định bởi: Data Scope"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-006-AC003",
        "EP-16-006-AC006",
        "EP-16-006-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-006-O003",
      "obligation_text": "Data Protection được quyết định bởi: Data Classification"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-006-AC004",
        "EP-16-006-AC006",
        "EP-16-006-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-006-O004",
      "obligation_text": "Data Protection được quyết định bởi: Customer Consent"
    },
    {
      "acceptance_criterion_references": [
        "EP-16-006-AC005",
        "EP-16-006-AC006",
        "EP-16-006-AC007"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "EP-16-006-O005",
      "obligation_text": "Data Protection được quyết định bởi: Security Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-006-AC007"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-006 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-006 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-006-AC006"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-006-AC001",
        "EP-16-006-AC002",
        "EP-16-006-AC003",
        "EP-16-006-AC004",
        "EP-16-006-AC005"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-006 does not define a recovery obligation."
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
    "source_fingerprint": "a45c06d451bdca42a937a38924a542987df0c7a8434df8996a528c893a88bdf9",
    "source_lines": "L12660-L12818",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-16-006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "EP-16-007",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "source_fingerprint": "6f0b848969ced0030404b390096b05c5a65659ecb23bfdd15bc1cebbb194ef09"
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
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-007-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "EP-16-007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "EP-16-007 does not define a recovery obligation."
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
    "source_fingerprint": "6f0b848969ced0030404b390096b05c5a65659ecb23bfdd15bc1cebbb194ef09",
    "source_lines": "L12820-L12930",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-16-007"
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
    "source_fingerprint": "1404a65d036d934de8365625062f1d12cfff6fcb9212f3f22107c386d8ceb94e",
    "source_lines": "L12932-L12980",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-16-008"
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
    "source_fingerprint": "2e348ea0b95ff6b984766ef1147b16c1b7ab2338088d2dbed543b932629313f2",
    "source_lines": "L12982-L13033",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-16-009"
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
  "normative_statement": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - Permission - Data Scope - Organization Relationship - Support Policy - Customer Consent - Data Classification - Security Policy",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "EP-16-010",
    "phase_2c_c3_actions": [
      "C3_STRUCTURAL_RECONCILIATION_PARENT"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "EP-16-010",
    "source_context_sha256": "1c09cca794138eb3a085b4ae5d2fcfdfff8a1512233750352fe24b0e570d1c62",
    "source_document": "docs/BRD/BRD-WS-16.md",
    "source_fingerprint": "b5390e9bff4344f7f65e192711cea1db44d4472944739679f3c442482616b415",
    "source_fingerprint_before_c3": "ca6d6e6c157444c582243876a077f8bad3b7efb8a877149c17125e04f7740a02",
    "source_lines": "L13035-L13105",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > EP-16-010"
  },
  "record_kind": "COMPOSITE_PARENT",
  "relationships": {
    "alias_of": null,
    "aliases": [],
    "coverage_mode": "ALL_CHILDREN",
    "derived_from": [],
    "derived_requirements": [
      "BRD-WS-16-R029",
      "BRD-WS-16-R030",
      "BRD-WS-16-R031",
      "BRD-WS-16-R032",
      "BRD-WS-16-R033",
      "BRD-WS-16-R034",
      "BRD-WS-16-R035",
      "BRD-WS-16-R036",
      "BRD-WS-16-R037"
    ],
    "satisfies_composite_parents": [
      "BRD-UPDATE-01-R024"
    ]
  },
  "requirement_type": "PRIVACY_REQUIREMENT",
  "scope_coverage_unit": false,
  "scope_status": "V2.3_ACTIVE",
  "stable_id": "EP-16-010",
  "title": "Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - …",
  "verification_criticality": "NOT_APPLICABLE"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
