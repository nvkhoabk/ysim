---
document_code: "BRD-WS-03"
title: "Identity, Organization & Access Control Model"
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

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-001 — Organization là Business Entity quản lý toàn bộ kênh bán hàng

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-001-AC001",
      "given": "the applicable business context, actor, and input for Organization là Business Entity quản lý toàn bộ kênh bán hàng",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-03-001-O001"
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
        "BD-03-001-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-001-O001",
      "obligation_text": "Organization là Business Entity quản lý toàn bộ kênh bán hàng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization là Business Entity quản lý toàn bộ kênh bán hàng.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-001",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-03-001",
    "source_context_sha256": "db317bc3fccb7c9ea6354dbaccd8a563826be423254516cc5f09738a7a4d03c2",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "3f2b4aea8ab2a49c4a1c71699e4d809de56ecd80e00a377165523df811a1679f",
    "source_lines": "L521-L524",
    "source_section": "23. Business Decisions (Locked) > BD-03-001"
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
  "stable_id": "BD-03-001",
  "title": "Organization là Business Entity quản lý toàn bộ kênh bán hàng",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-002 — Organization Structure và Distribution Network là hai mô hình độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-002-AC001",
      "given": "the applicable business context, actor, and input for Organization Structure và Distribution Network là hai mô hình độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "BD-03-002-O001"
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
        "BD-03-002-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-002-O001",
      "obligation_text": "Organization Structure và Distribution Network là hai mô hình độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Organization Structure và Distribution Network là hai mô hình độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-002",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-03-002",
    "source_context_sha256": "6cd6b35393b4edcc7449a9e0dfd0db48f4b13338237b2509ec454333d19ae380",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "da716f10c04a9f990b9e634a105722332f620aaf23b8780e3e6e565fcfa1533f",
    "source_lines": "L527-L530",
    "source_section": "23. Business Decisions (Locked) > BD-03-002"
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
  "stable_id": "BD-03-002",
  "title": "Organization Structure và Distribution Network là hai mô hình độc lập",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-003 — Portal và Storefront là hai thành phần độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-003-AC001",
      "given": "the applicable business context, actor, and input for Portal và Storefront là hai thành phần độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "BD-03-003-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-03-003-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Portal và Storefront là hai thành phần độc lập",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-03-003-O001"
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
        "BD-03-003-AC001",
        "BD-03-003-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-003-O001",
      "obligation_text": "Portal và Storefront là hai thành phần độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Portal và Storefront là hai thành phần độc lập.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-003",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-03-003",
    "source_context_sha256": "04651c9a640a33ed53742eaa3ed78ad7fafc81a5f5409decafdc0df729b5eff5",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "9fef18a9d441e606dab2711c2f0e10239339ab102d47fe75c0853870c2cb7614",
    "source_lines": "L533-L536",
    "source_section": "23. Business Decisions (Locked) > BD-03-003"
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
  "stable_id": "BD-03-003",
  "title": "Portal và Storefront là hai thành phần độc lập",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-004 — Customer Portal là Storefront mở rộng

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-004-AC001",
      "given": "the applicable business context, actor, and input for Customer Portal là Storefront mở rộng",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-03-004-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-03-004-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Customer Portal là Storefront mở rộng",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-03-004-O001"
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
        "BD-03-004-AC001",
        "BD-03-004-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-004-O001",
      "obligation_text": "Customer Portal là Storefront mở rộng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Portal là Storefront mở rộng.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-004",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Customer Portal",
    "source_context_sha256": "b73c5a3d6ad20ff0ef172f55091368a9f50bb0c487bf5f28fd809c9eda50e2fa",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "e751f8baf4c1190a9ba562a5dbe23a1aa7e3b6b9329a09c38476c58fe38492db",
    "source_lines": "L539-L542",
    "source_section": "23. Business Decisions (Locked) > BD-03-004"
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
  "stable_id": "BD-03-004",
  "title": "Customer Portal là Storefront mở rộng",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-005 — Identity là Foundation Domain

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-005-AC001",
      "given": "the applicable business context, actor, and input for Identity là Foundation Domain",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-03-005-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-03-005-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Identity là Foundation Domain",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-03-005-O001"
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
        "BD-03-005-AC001",
        "BD-03-005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-005-O001",
      "obligation_text": "Identity là Foundation Domain"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-03-005 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-03-005 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-03-005 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-03-005 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-03-005-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-03-005 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Identity là Foundation Domain.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-005",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "9. Identity Domain",
    "source_context_sha256": "8c3a6cf06bf4b767d2a26f66329d9f83306c044a8016a28aa261c827918bcc74",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "959211fed7630c135d78ac57741016c38d2e5ee6fec4b1eff11c1aeb5d7ca277",
    "source_lines": "L545-L548",
    "source_section": "23. Business Decisions (Locked) > BD-03-005"
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
  "stable_id": "BD-03-005",
  "title": "Identity là Foundation Domain",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-006 — User và Customer là hai Business Entity độc lập

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-006-AC001",
      "given": "the applicable business context, actor, and input for User và Customer là hai Business Entity độc lập",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "each named business concept has a distinct identity, owner or reference, and lifecycle evidence; an action on one does not implicitly act on the other",
      "verifies": [
        "BD-03-006-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-03-006-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by User và Customer là hai Business Entity độc lập",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-03-006-O001"
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
        "BD-03-006-AC001",
        "BD-03-006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-006-O001",
      "obligation_text": "User và Customer là hai Business Entity độc lập"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "User và Customer là hai Business Entity độc lập.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-006",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-03-006",
    "source_context_sha256": "4d9d497e4baaaeac83bd0f9ee5cd4ae27e70e42b3152458363e104006410ef93",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "f9343e4fd814cb247cd98bd6017fa0ea550e44a4b6472e2f0743fef2877e0bbf",
    "source_lines": "L551-L554",
    "source_section": "23. Business Decisions (Locked) > BD-03-006"
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
  "stable_id": "BD-03-006",
  "title": "User và Customer là hai Business Entity độc lập",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-007 — Mỗi User chỉ thuộc một Organization

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-007-AC001",
      "given": "the applicable business context, actor, and input for Mỗi User chỉ thuộc một Organization",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-03-007-O001"
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
        "BD-03-007-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-007-O001",
      "obligation_text": "Mỗi User chỉ thuộc một Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi User chỉ thuộc một Organization.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-007",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-03-007",
    "source_context_sha256": "6106b6e8fd1ed35d0a13c9c96b2bedcff03284228a98f5cdf00be7927983c272",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "1701420870ec58434348e9177b0503909dc3edf1cc946e8cc4e7105917b81a37",
    "source_lines": "L557-L560",
    "source_section": "23. Business Decisions (Locked) > BD-03-007"
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
  "stable_id": "BD-03-007",
  "title": "Mỗi User chỉ thuộc một Organization",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-008 — Role thuộc Organization

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-008-AC001",
      "given": "the applicable business context, actor, and input for Role thuộc Organization",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-03-008-O001"
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
        "BD-03-008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-008-O001",
      "obligation_text": "Role thuộc Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Role thuộc Organization.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-008",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "12. Roles",
    "source_context_sha256": "d2c31e6c928e3897a3f35fe602e15ccfc92e9e7960bb1b406c1f4624d36de36f",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "3af4b9d9a6bf05498fd15e61586e7b924eae5c62382f74c6ae7b9a30fb3163b1",
    "source_lines": "L563-L566",
    "source_section": "23. Business Decisions (Locked) > BD-03-008"
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
  "stable_id": "BD-03-008",
  "title": "Role thuộc Organization",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-009 — Permission được xác định theo: Role + Resource Scope + Data Scope + Policy

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BD-03-009-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Permission được xác định theo: Role + Resource Scope + Data Scope + Policy",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the effective security policy produces the required allow, challenge, block, review, or denial result; protected state and audit evidence agree with that decision",
      "verifies": [
        "BD-03-009-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BD-03-009-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Permission được xác định theo: Role + Resource Scope + Data Scope + Policy",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BD-03-009-O001"
      ],
      "when": "the protected decision or action is attempted"
    },
    {
      "case": "NEGATIVE_FAIL_CLOSED",
      "controlled_contract": "REQUIREMENT_SPECIFIC_FAIL_CLOSED_V1",
      "criterion_id": "BD-03-009-AC003",
      "given": "an input or attempted state change that violates a mandatory boundary explicitly stated by Permission được xác định theo: Role + Resource Scope + Data Scope + Policy",
      "observable_evidence": "violating input, decision and reason, before/after protected state, and audit or conformance evidence",
      "then": "the violated obligation produces its specified rejection, denial, block, review, or non-conforming result without recording a contradictory success",
      "verifies": [
        "BD-03-009-O001"
      ],
      "when": "the violating input or action is evaluated"
    },
    {
      "case": "AUTHORIZATION_BOUNDARY",
      "controlled_contract": "EXPLICIT_AUTHORIZATION_BOUNDARY_V1",
      "criterion_id": "BD-03-009-AC004",
      "given": "an actor lacking the permission, role, identity assurance, consent, or access condition stated by Permission được xác định theo: Role + Resource Scope + Data Scope + Policy",
      "observable_evidence": "actor and scope, effective policy or assurance, decision, protected-state comparison, reason, and audit evidence",
      "then": "access is denied or challenged according to the referenced obligation, protected state remains unchanged, and the decision is auditable",
      "verifies": [
        "BD-03-009-O001"
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
        "BD-03-009-AC001",
        "BD-03-009-AC002",
        "BD-03-009-AC003",
        "BD-03-009-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-009-O001",
      "obligation_text": "Permission được xác định theo: Role + Resource Scope + Data Scope + Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [
        "BD-03-009-AC004"
      ],
      "status": "APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-03-009 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-03-009 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [
        "BD-03-009-AC003"
      ],
      "status": "APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-03-009-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-03-009 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Permission được xác định theo: Role + Resource Scope + Data Scope + Policy.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-009",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-03-009",
    "source_context_sha256": "254bc78542a628528656decc6508efcf7814c7010bb8cec0ebeb0d7f2cafb605",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "474cb6ab2cfff3518154130c4bd5229571436d164f7d2509ea96c91d0bc2b674",
    "source_lines": "L569-L574",
    "source_section": "23. Business Decisions (Locked) > BD-03-009"
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
  "stable_id": "BD-03-009",
  "title": "Permission được xác định theo: Role + Resource Scope + Data Scope + Policy",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-010 — Customer Ownership được quản lý theo Distribution Network

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-010-AC001",
      "given": "the applicable business context, actor, and input for Customer Ownership được quản lý theo Distribution Network",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-03-010-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "BUSINESS_BOUNDARY_FAILURE_V1",
      "criterion_id": "BD-03-010-AC002",
      "given": "an unsupported or invalid business input at the boundary governed by Customer Ownership được quản lý theo Distribution Network",
      "observable_evidence": "input, policy or rule decision, before/after state, reason, and customer/operator-visible result",
      "then": "no unsupported success or state transition is recorded; a deterministic business outcome and reason identify the violated obligation",
      "verifies": [
        "BD-03-010-O001"
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
        "BD-03-010-AC001",
        "BD-03-010-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-010-O001",
      "obligation_text": "Customer Ownership được quản lý theo Distribution Network"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Ownership được quản lý theo Distribution Network.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-010",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-03-010",
    "source_context_sha256": "e0edea78e82f7bddf4f7dad0ea1cf1adb18aa4358c8f71f43d926a59de80acfa",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "2c30b95405d8f4d2d21af445e98ad0d7beaf5bddbe9c7861368933e7a96d3849",
    "source_lines": "L577-L580",
    "source_section": "23. Business Decisions (Locked) > BD-03-010"
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
  "stable_id": "BD-03-010",
  "title": "Customer Ownership được quản lý theo Distribution Network",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-011 — Support Governance được điều khiển bởi Support Policy. Support Policy gồm: - SELF_SUPPORT - PARE…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-011-AC001",
      "given": "the applicable business context, actor, and input for Support Governance được điều khiển bởi Support Policy. Support Policy gồm: - SELF_SUPPORT - PARE…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-03-011-O001"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-011-AC002",
      "given": "the applicable business context, actor, and input for Support Governance được điều khiển bởi Support Policy. Support Policy gồm: - SELF_SUPPORT - PARE…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-03-011-O002"
      ],
      "when": "the governing policy, calculation, state transition, or business action is evaluated"
    },
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-011-AC003",
      "given": "the applicable business context, actor, and input for Support Governance được điều khiển bởi Support Policy. Support Policy gồm: - SELF_SUPPORT - PARE…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-03-011-O003"
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
        "BD-03-011-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-011-O001",
      "obligation_text": "Support Governance được điều khiển bởi Support Policy. Support Policy gồm: SELF_SUPPORT."
    },
    {
      "acceptance_criterion_references": [
        "BD-03-011-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-011-O002",
      "obligation_text": "Support Governance được điều khiển bởi Support Policy. Support Policy gồm: PARENT_SUPPORT."
    },
    {
      "acceptance_criterion_references": [
        "BD-03-011-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-011-O003",
      "obligation_text": "Support Governance được điều khiển bởi Support Policy. Support Policy gồm: HYBRID."
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Support Governance được điều khiển bởi Support Policy. Support Policy gồm: - SELF_SUPPORT - PARENT_SUPPORT - HYBRID",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-011",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-03-011",
    "source_context_sha256": "240ccc1db8ab14c7398513aef7ca273fe7925a87aeaabfaf6632a8b071f24a35",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "22d0e0bf868fc3b94aa944ee25d6910edec09374e8dd36e47b0bf520c9dbe46f",
    "source_lines": "L583-L592",
    "source_section": "23. Business Decisions (Locked) > BD-03-011"
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
  "stable_id": "BD-03-011",
  "title": "Support Governance được điều khiển bởi Support Policy. Support Policy gồm: - SELF_SUPPORT - PARE…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-012 — Mọi dữ liệu nhạy cảm phải hỗ trợ Data Masking

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-012-AC001",
      "given": "the applicable business context, actor, and input for Mọi dữ liệu nhạy cảm phải hỗ trợ Data Masking",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BD-03-012-O001"
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
        "BD-03-012-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-012-O001",
      "obligation_text": "Mọi dữ liệu nhạy cảm phải hỗ trợ Data Masking"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi dữ liệu nhạy cảm phải hỗ trợ Data Masking.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-012",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-03-012",
    "source_context_sha256": "eb70729d0348f0f05edce1a153bf7e09410435f5b1f8a73b61bbcc0f05d56e03",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "c1d857f5648a94ffa9178cc85c6a5ba619c92b90655eb5079c496aca5d12801a",
    "source_lines": "L595-L598",
    "source_section": "23. Business Decisions (Locked) > BD-03-012"
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
  "stable_id": "BD-03-012",
  "title": "Mọi dữ liệu nhạy cảm phải hỗ trợ Data Masking",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-013 — Mọi thao tác truy cập dữ liệu nhạy cảm phải được Audit

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "OPERATIONAL_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BD-03-013-AC001",
      "given": "an operational task within the scope of Mọi thao tác truy cập dữ liệu nhạy cảm phải được Audit",
      "observable_evidence": "operation identity, state, outcome, timestamps, relevant signals, audit record, and operator-visible result",
      "then": "the operator can distinguish running, completed, and failed state as applicable and can inspect the resulting outcome, relevant signals, and evidence named by the obligation",
      "verifies": [
        "BD-03-013-O001"
      ],
      "when": "the task runs, completes, fails, or is inspected by an operator"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "OPERATIONAL_VERIFICATION_FAILURE_V1",
      "criterion_id": "BD-03-013-AC002",
      "given": "an operational task missing an outcome, required signal, audit evidence, or recovery evidence for Mọi thao tác truy cập dữ liệu nhạy cảm phải được Audit",
      "observable_evidence": "operator-visible verification result, missing-evidence identifier, operation state, and relevant signal or audit record",
      "then": "verification reports the specific missing evidence as a detectable failure and does not report the task as conforming",
      "verifies": [
        "BD-03-013-O001"
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
        "BD-03-013-AC001",
        "BD-03-013-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-013-O001",
      "obligation_text": "Mọi thao tác truy cập dữ liệu nhạy cảm phải được Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BD-03-013 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BD-03-013 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BD-03-013 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BD-03-013 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BD-03-013-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BD-03-013 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thao tác truy cập dữ liệu nhạy cảm phải được Audit.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-013",
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "BD-03-013",
    "source_context_sha256": "f74d90780d69f616ba5feb4d004c2a5233ebca6e46d8793b571323c7a891a8bd",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "414d75237ba7d8658a2b20f62f4a1765aac40ac72826d0ca05d67c8705760c54",
    "source_lines": "L601-L604",
    "source_section": "23. Business Decisions (Locked) > BD-03-013"
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
  "stable_id": "BD-03-013",
  "title": "Mọi thao tác truy cập dữ liệu nhạy cảm phải được Audit",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-03-R002 — Mỗi User chỉ thuộc duy nhất một Organization

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-03-R002-AC001",
      "given": "the applicable business context, actor, and input for Mỗi User chỉ thuộc duy nhất một Organization",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-03-R002-O001"
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
        "BRD-WS-03-R002-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-03-R002-O001",
      "obligation_text": "Mỗi User chỉ thuộc duy nhất một Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mỗi User chỉ thuộc duy nhất một Organization.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-03-002",
    "previous_temporary_key": "TMP-BRD-WS-03-002",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. User",
    "source_context_sha256": "15bb3286979968838425c21aa0b2010af29e00425e8d4699255ce32c9a35055b",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "4dfeea5fb2fd754d788ea2cb4e534189f3af49a29753a7bf65ab2ba44bfed066",
    "source_lines": "L261",
    "source_section": "10. User"
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
  "stable_id": "BRD-WS-03-R002",
  "title": "Mỗi User chỉ thuộc duy nhất một Organization",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-03-R003 — Nếu một người làm việc cho nhiều Organization thì phải có nhiều User khác nhau

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-03-R003-AC001",
      "given": "the applicable business context, actor, and input for Nếu một người làm việc cho nhiều Organization thì phải có nhiều User khác nhau",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-03-R003-O001"
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
        "BRD-WS-03-R003-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-03-R003-O001",
      "obligation_text": "Nếu một người làm việc cho nhiều Organization thì phải có nhiều User khác nhau"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Nếu một người làm việc cho nhiều Organization thì phải có nhiều User khác nhau.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-03-003",
    "previous_temporary_key": "TMP-BRD-WS-03-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "10. User",
    "source_context_sha256": "15bb3286979968838425c21aa0b2010af29e00425e8d4699255ce32c9a35055b",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
    "source_lines": "L263",
    "source_section": "10. User"
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
  "stable_id": "BRD-WS-03-R003",
  "title": "Nếu một người làm việc cho nhiều Organization thì phải có nhiều User khác nhau",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-03-R004 — Collaborator không phải Organization

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-03-R004-AC001",
      "given": "the applicable business context, actor, and input for Collaborator không phải Organization",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-03-R004-O001"
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
        "BRD-WS-03-R004-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-03-R004-O001",
      "obligation_text": "Collaborator không phải Organization"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Collaborator không phải Organization.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-03-004",
    "previous_temporary_key": "TMP-BRD-WS-03-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Collaborator",
    "source_context_sha256": "bdfacee3d82369bcbdd5f4d618bfec5abe6327dc34c1bcf15a6790dd53cf4862",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "f37c8b2fcfc805ba591651aae0e91102ded4ec84307acf686ae251d734833594",
    "source_lines": "L322",
    "source_section": "13. Collaborator"
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
  "stable_id": "BRD-WS-03-R004",
  "title": "Collaborator không phải Organization",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-03-R005 — Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - khách hàng của mình

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-03-R005-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - khách hàng của mình",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the actor can retrieve only customer identities attributed to that actor; a customer attributed to another actor is absent and access to it is denied",
      "verifies": [
        "BRD-WS-03-R005-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-03-R005-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - khách hàng của mình",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-03-R005-O001"
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
        "BRD-WS-03-R005-AC001",
        "BRD-WS-03-R005-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-03-R005-O001",
      "obligation_text": "Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - khách hàng của mình"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - khách hàng của mình",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-03-005",
    "previous_temporary_key": "TMP-BRD-WS-03-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Collaborator",
    "source_context_sha256": "bdfacee3d82369bcbdd5f4d618bfec5abe6327dc34c1bcf15a6790dd53cf4862",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "7a3b81cc54cc7f02c2d4d2400fe1218de9aebccea6d8988b1755c302e2d61ea4",
    "source_lines": "L326-L328",
    "source_section": "13. Collaborator"
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
  "stable_id": "BRD-WS-03-R005",
  "title": "Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - khách hàng của mình",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-03-R006 — Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - doanh thu của mình

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-03-R006-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - doanh thu của mình",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the actor can retrieve only customer identities attributed to that actor; a customer attributed to another actor is absent and access to it is denied",
      "verifies": [
        "BRD-WS-03-R006-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-03-R006-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - doanh thu của mình",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-03-R006-O001"
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
        "BRD-WS-03-R006-AC001",
        "BRD-WS-03-R006-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-03-R006-O001",
      "obligation_text": "Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - doanh thu của mình"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - doanh thu của mình",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-03-006",
    "previous_temporary_key": "TMP-BRD-WS-03-006",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Collaborator",
    "source_context_sha256": "bdfacee3d82369bcbdd5f4d618bfec5abe6327dc34c1bcf15a6790dd53cf4862",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "e38498c7d95e71bfecf885209478fa9324a65d76d0a6b138dba5b4d7b3f21e34",
    "source_lines": "L326-L329",
    "source_section": "13. Collaborator"
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
  "stable_id": "BRD-WS-03-R006",
  "title": "Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - doanh thu của mình",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-03-R007 — Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - commission của mình

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-03-R007-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - commission của mình",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the actor can retrieve only customer identities attributed to that actor; a customer attributed to another actor is absent and access to it is denied",
      "verifies": [
        "BRD-WS-03-R007-O001"
      ],
      "when": "the protected decision or action is evaluated"
    },
    {
      "case": "PRINCIPAL_FAILURE_OR_EDGE",
      "controlled_contract": "SECURITY_FAIL_CLOSED_V1",
      "criterion_id": "BRD-WS-03-R007-AC002",
      "given": "a principal or request that does not satisfy the assurance, policy, consent, or authorization boundary for Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - commission của mình",
      "observable_evidence": "decision result, protected-state comparison, reason, effective policy, and audit record",
      "then": "the result is challenge, block, review, or denial as required; protected state is unchanged and the reason is audited",
      "verifies": [
        "BRD-WS-03-R007-O001"
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
        "BRD-WS-03-R007-AC001",
        "BRD-WS-03-R007-AC002"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-03-R007-O001",
      "obligation_text": "Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - commission của mình"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "criterion_references": [],
      "rationale": "BRD-WS-03-R007 does not define a authorization boundary obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "CONCURRENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-03-R007 does not define a concurrency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "IDEMPOTENCY": {
      "criterion_references": [],
      "rationale": "BRD-WS-03-R007 does not define a idempotency obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "NEGATIVE_FAIL_CLOSED": {
      "criterion_references": [],
      "rationale": "BRD-WS-03-R007 does not define a negative fail closed obligation or boundary.",
      "status": "NOT_APPLICABLE"
    },
    "POSITIVE": {
      "criterion_references": [
        "BRD-WS-03-R007-AC001"
      ],
      "status": "APPLICABLE"
    },
    "RECOVERY": {
      "criterion_references": [],
      "rationale": "BRD-WS-03-R007 does not define a recovery obligation or boundary.",
      "status": "NOT_APPLICABLE"
    }
  },
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - commission của mình",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-03-007",
    "previous_temporary_key": "TMP-BRD-WS-03-007",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Collaborator",
    "source_context_sha256": "bdfacee3d82369bcbdd5f4d618bfec5abe6327dc34c1bcf15a6790dd53cf4862",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "2e695e1e742d8d39de8a990d1a1f46a33c802e2f27eacc555f1a13594c3c7e4f",
    "source_lines": "L326-L330",
    "source_section": "13. Collaborator"
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
  "stable_id": "BRD-WS-03-R007",
  "title": "Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - commission của mình",
  "verification_criticality": "CRITICAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-03-R008 — Collaborator không được xem dữ liệu nội bộ của Organization nếu không được cấp quyền

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "SECURITY_DECISION_OBSERVATION_V1",
      "criterion_id": "BRD-WS-03-R008-AC001",
      "given": "an identified principal, applicable assurance context, and policy inputs for Collaborator không được xem dữ liệu nội bộ của Organization nếu không được cấp quyền",
      "observable_evidence": "decision result, effective assurance or policy, denied or changed state, reason, and audit evidence",
      "then": "the prohibited security decision path produces no effective permission or protected-state change, and conformance evidence identifies the attempted bypass",
      "verifies": [
        "BRD-WS-03-R008-O001"
      ],
      "when": "the protected decision or action is evaluated"
    }
  ],
  "acceptance_rationale": null,
  "acceptance_schema_version": "2.0.0-OBLIGATION_COVERAGE",
  "acceptance_status": "DIRECT",
  "acceptance_unit": true,
  "atomic_obligations": [
    {
      "acceptance_criterion_references": [
        "BRD-WS-03-R008-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-03-R008-O001",
      "obligation_text": "Collaborator không được xem dữ liệu nội bộ của Organization nếu không được cấp quyền"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Collaborator không được xem dữ liệu nội bộ của Organization nếu không được cấp quyền.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-03-008",
    "previous_temporary_key": "TMP-BRD-WS-03-008",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "13. Collaborator",
    "source_context_sha256": "bdfacee3d82369bcbdd5f4d618bfec5abe6327dc34c1bcf15a6790dd53cf4862",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "a2a1b86b5ce9fdf53b8804c4d73188f3e4c5bbf9bb800f8e5bb9e4e3fd04bf28",
    "source_lines": "L332",
    "source_section": "13. Collaborator"
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
  "stable_id": "BRD-WS-03-R008",
  "title": "Collaborator không được xem dữ liệu nội bộ của Organization nếu không được cấp quyền",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-03-R009 — Các trường dữ liệu nhạy cảm phải hỗ trợ Masking

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-03-R009-AC001",
      "given": "the applicable business context, actor, and input for Các trường dữ liệu nhạy cảm phải hỗ trợ Masking",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the applicable policy or rule produces a named decision, calculation, state transition, or visible business outcome with its governing input and reason recorded",
      "verifies": [
        "BRD-WS-03-R009-O001"
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
        "BRD-WS-03-R009-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-03-R009-O001",
      "obligation_text": "Các trường dữ liệu nhạy cảm phải hỗ trợ Masking"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Các trường dữ liệu nhạy cảm phải hỗ trợ Masking.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-03-009",
    "previous_temporary_key": "TMP-BRD-WS-03-009",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "16. Data Masking",
    "source_context_sha256": "e5b0e53de650c84d8f80b77705241244197f0bd27e301200205cfe7d8e9d4dcb",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "170ae36983a23db4f520bd8934721f072dbbdb868577d944c488c678cd7ad58b",
    "source_lines": "L371",
    "source_section": "16. Data Masking"
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
  "stable_id": "BRD-WS-03-R009",
  "title": "Các trường dữ liệu nhạy cảm phải hỗ trợ Masking",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-WS-03-R010 — Một Organization không được phép truy cập dữ liệu của Organization khác nếu không được phép theo…

```json
{
  "acceptance_contract": [
    {
      "case": "POSITIVE",
      "controlled_contract": "BUSINESS_OUTCOME_OBSERVATION_V1",
      "criterion_id": "BRD-WS-03-R010-AC001",
      "given": "the applicable business context, actor, and input for Một Organization không được phép truy cập dữ liệu của Organization khác nếu không được phép theo…",
      "observable_evidence": "business input, policy or rule version, decision or state transition, calculated result where applicable, and visible outcome",
      "then": "the prohibited decision or state transition is absent, the attempted action has a deterministic rejection outcome, and no contradictory success is recorded",
      "verifies": [
        "BRD-WS-03-R010-O001"
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
        "BRD-WS-03-R010-AC001"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-03-R010-O001",
      "obligation_text": "Một Organization không được phép truy cập dữ liệu của Organization khác nếu không được phép theo Business Rule"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Một Organization không được phép truy cập dữ liệu của Organization khác nếu không được phép theo Business Rule.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-WS-03-010",
    "previous_temporary_key": "TMP-BRD-WS-03-010",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "17. Organization Boundary",
    "source_context_sha256": "db01ee79d47f9f42b0bc1486243582bf659c30b61443a0d612f1fb13a0747cc2",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "b1919b8370faf679a072286e43c92a187a5da2df976736a074d38a19fcda7cec",
    "source_lines": "L401",
    "source_section": "17. Organization Boundary"
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
  "stable_id": "BRD-WS-03-R010",
  "title": "Một Organization không được phép truy cập dữ liệu của Organization khác nếu không được phép theo…",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
