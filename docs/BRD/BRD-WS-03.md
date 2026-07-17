---
document_code: "BRD-WS-03"
document_id: "BRD-WS-03"
title: "Identity, Organization & Access Control Model"
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

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-001 — Organization là Business Entity quản lý toàn bộ kênh bán hàng

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
      "requirement_id": "BD-03-001",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "40465985dbd881cb51278b7a68cde953c1c119985d1f93ef287ec920af46d1c8"
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
        "BD-03-001-AC001",
        "BD-03-001-AC002",
        "BD-03-001-AC003"
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
    "source_fingerprint": "40465985dbd881cb51278b7a68cde953c1c119985d1f93ef287ec920af46d1c8",
    "source_lines": "L658-L733",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-001"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-03-002",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "9ecd244822075ddcb30e64db8f8f3d6f33efa44a2521df161662dd6dda0528b6"
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
        "BD-03-002-AC001",
        "BD-03-002-AC002",
        "BD-03-002-AC003"
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
    "source_fingerprint": "9ecd244822075ddcb30e64db8f8f3d6f33efa44a2521df161662dd6dda0528b6",
    "source_lines": "L735-L810",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-002"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-03-003",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "2fba44e8e342fe619789636883a562afd18bb289facd4087b113a89dd5310f32"
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
        "BD-03-003-AC001",
        "BD-03-003-AC002",
        "BD-03-003-AC003"
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
    "source_fingerprint": "2fba44e8e342fe619789636883a562afd18bb289facd4087b113a89dd5310f32",
    "source_lines": "L812-L887",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-003"
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
### BD-03-004 — Customer Portal là experience channel độc lập có stable shell, được scope theo Organization và S…

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
      "requirement_id": "BD-03-004",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "d0cfc5e940f9259747aa8f5f3bbb5e146498ffdc8e571a934b9cfc9d90f919fc"
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
        "BD-03-004-AC001",
        "BD-03-004-AC003",
        "BD-03-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-004-O001",
      "obligation_text": "Customer Portal là experience channel độc lập có stable shell, được scope theo Organization và Storefront, không tạo YSim global consolidated portal, sử dụng một default Storefront đồng thời giữ originating Storefront context, cung cấp Dashboard widgets và commerce menu"
    },
    {
      "acceptance_criterion_references": [
        "BD-03-004-AC002",
        "BD-03-004-AC003",
        "BD-03-004-AC004"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-004-O002",
      "obligation_text": "Storefront vẫn là kênh thực hiện bán hàng"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Customer Portal là experience channel độc lập có stable shell, được scope theo Organization và Storefront, không tạo YSim global consolidated portal, sử dụng một default Storefront đồng thời giữ originating Storefront context, cung cấp Dashboard widgets và commerce menu; Storefront vẫn là kênh thực hiện bán hàng.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-008",
      "V23-P2C-ACCEPTANCE-MAPPING-C3"
    ],
    "identity_origin": "PRESERVED_STABLE_ID",
    "original_identity": "BD-03-004",
    "phase_2c_c3_actions": [
      "C3_APPROVED_SEMANTIC_DIRECTIVE"
    ],
    "previous_temporary_key": null,
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "8. Customer Portal",
    "source_context_sha256": "b73c5a3d6ad20ff0ef172f55091368a9f50bb0c487bf5f28fd809c9eda50e2fa",
    "source_document": "docs/BRD/BRD-WS-03.md",
    "source_fingerprint": "d0cfc5e940f9259747aa8f5f3bbb5e146498ffdc8e571a934b9cfc9d90f919fc",
    "source_fingerprint_before_c3": "e751f8baf4c1190a9ba562a5dbe23a1aa7e3b6b9329a09c38476c58fe38492db",
    "source_lines": "L889-L986",
    "source_mapping_decision_commit": "a90476e8b053bf86c11638477736c8c418a33025",
    "source_mapping_decision_tag": "baseline/v2.3/phase-2/acceptance-mapping/c3-accepted",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-004"
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
  "title": "Customer Portal là experience channel độc lập có stable shell, được scope theo Organization và S…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BD-03-005 — Identity là Foundation Domain

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
      "requirement_id": "BD-03-005",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "c07d5a9fc849da69487484b11a6870eb9653c22e90f3053048c15fb848e48d0d"
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
        "BD-03-005-AC001",
        "BD-03-005-AC002",
        "BD-03-005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-005-O001",
      "obligation_text": "Identity là Foundation Domain"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-03-005-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-03-005 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-03-005 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-03-005-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-03-005-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-03-005 does not define a recovery obligation."
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
    "source_fingerprint": "c07d5a9fc849da69487484b11a6870eb9653c22e90f3053048c15fb848e48d0d",
    "source_lines": "L988-L1102",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-005"
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
      "requirement_id": "BD-03-006",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "c46de6e33abffdcf7475c60385280c3d512dddc1e1b1dfffc82aef2bbb6e7d5c"
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
        "BD-03-006-AC001",
        "BD-03-006-AC002",
        "BD-03-006-AC003"
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
    "source_fingerprint": "c46de6e33abffdcf7475c60385280c3d512dddc1e1b1dfffc82aef2bbb6e7d5c",
    "source_lines": "L1104-L1183",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-006"
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
      "requirement_id": "BD-03-007",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "36e5825a055f4cbd670a04340ffb9556ecba8320bd95d6d12d690ae31acde6c3"
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
        "BD-03-007-AC001",
        "BD-03-007-AC002",
        "BD-03-007-AC003"
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
    "source_fingerprint": "36e5825a055f4cbd670a04340ffb9556ecba8320bd95d6d12d690ae31acde6c3",
    "source_lines": "L1185-L1264",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-03-008",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "bcb6fd643e14d956d4471065f30c6ea602f552e0bdb6fe5097c22d0cf209bfb9"
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
        "BD-03-008-AC001",
        "BD-03-008-AC002",
        "BD-03-008-AC003"
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
    "source_fingerprint": "bcb6fd643e14d956d4471065f30c6ea602f552e0bdb6fe5097c22d0cf209bfb9",
    "source_lines": "L1266-L1341",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-03-009",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "1eef7a3665ab26e650831622f9bfcd38e64075513774cfbaa2f58e0fede0d610"
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
        "BD-03-009-AC001",
        "BD-03-009-AC002",
        "BD-03-009-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-009-O001",
      "obligation_text": "Permission được xác định theo: Role + Resource Scope + Data Scope + Policy"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-03-009-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-03-009 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-03-009 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-03-009-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-03-009-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-03-009 does not define a recovery obligation."
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
    "source_fingerprint": "1eef7a3665ab26e650831622f9bfcd38e64075513774cfbaa2f58e0fede0d610",
    "source_lines": "L1343-L1453",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-009"
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
      "requirement_id": "BD-03-010",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "0fc915fca84ca72ca02ba7679fdb4cbb3c42b8ef915fe89c761ab464ee1df0f7"
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
        "BD-03-010-AC001",
        "BD-03-010-AC002",
        "BD-03-010-AC003"
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
    "source_fingerprint": "0fc915fca84ca72ca02ba7679fdb4cbb3c42b8ef915fe89c761ab464ee1df0f7",
    "source_lines": "L1455-L1534",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-010"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-03-011",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "44c843519206fba39e9fe949805fb0f20153b5845abe428d7e3b498f130b5218"
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
        "BD-03-011-AC001",
        "BD-03-011-AC004",
        "BD-03-011-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-011-O001",
      "obligation_text": "Support Governance được điều khiển bởi Support Policy. Support Policy gồm: SELF_SUPPORT"
    },
    {
      "acceptance_criterion_references": [
        "BD-03-011-AC002",
        "BD-03-011-AC004",
        "BD-03-011-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-011-O002",
      "obligation_text": "Support Governance được điều khiển bởi Support Policy. Support Policy gồm: PARENT_SUPPORT"
    },
    {
      "acceptance_criterion_references": [
        "BD-03-011-AC003",
        "BD-03-011-AC004",
        "BD-03-011-AC005"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-011-O003",
      "obligation_text": "Support Governance được điều khiển bởi Support Policy. Support Policy gồm: HYBRID"
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
    "source_fingerprint": "44c843519206fba39e9fe949805fb0f20153b5845abe428d7e3b498f130b5218",
    "source_lines": "L1536-L1631",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-011"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-03-012",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "5eedd184dbb7b075bfecad3049ba7d29d15487946c13054256543724d02f4fe6"
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
        "BD-03-012-AC001",
        "BD-03-012-AC002",
        "BD-03-012-AC003"
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
    "source_fingerprint": "5eedd184dbb7b075bfecad3049ba7d29d15487946c13054256543724d02f4fe6",
    "source_lines": "L1633-L1708",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-012"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BD-03-013",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "d78ca94a664f0aa3db9e7b2a4dd51ab1a7976d166cff8ac3bc4eaf04589830e4"
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
        "BD-03-013-AC001",
        "BD-03-013-AC002",
        "BD-03-013-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BD-03-013-O001",
      "obligation_text": "Mọi thao tác truy cập dữ liệu nhạy cảm phải được Audit"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-03-013 does not define a authorization boundary obligation."
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-03-013 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-03-013 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-03-013-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BD-03-013-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BD-03-013 does not define a recovery obligation."
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
    "source_fingerprint": "d78ca94a664f0aa3db9e7b2a4dd51ab1a7976d166cff8ac3bc4eaf04589830e4",
    "source_lines": "L1710-L1818",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BD-03-013"
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
      "requirement_id": "BRD-WS-03-R002",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "4dfeea5fb2fd754d788ea2cb4e534189f3af49a29753a7bf65ab2ba44bfed066"
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
        "BRD-WS-03-R002-AC001",
        "BRD-WS-03-R002-AC002",
        "BRD-WS-03-R002-AC003"
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
    "source_lines": "L1820-L1899",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-03-R002"
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
  "acceptance_contract": {
    "boundary_oracle": [
      "The same person identity may link the Users without merging Organization-scoped User records"
    ],
    "concrete_bindings": [
      {
        "actor_tenant": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-03.md#10. User",
            "source_type": "SOURCE_LITERAL",
            "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
          },
          "identifier": "BRD-WS-03-R003.ACTOR_TENANT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.ACTOR_TENANT.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-03.md",
            "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
            "source_lines": "L263",
            "source_section": "10. User"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "TENANT_ID",
            "resolver_id": "RESOLVE.BRD-WS-03-R003.BRD-WS-03-R003.ACTOR_TENANT",
            "version": "1.0.0"
          },
          "semantic_type": "TENANT_ID"
        },
        "permission_context": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-03.md#10. User",
            "source_type": "SOURCE_LITERAL",
            "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
          },
          "identifier": "BRD-WS-03-R003.PERMISSION_CONTEXT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.PERMISSION_CONTEXT.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-03.md",
            "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
            "source_lines": "L263",
            "source_section": "10. User"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "POLICY_ID",
            "resolver_id": "RESOLVE.BRD-WS-03-R003.BRD-WS-03-R003.PERMISSION_CONTEXT",
            "version": "1.0.0"
          },
          "semantic_type": "POLICY_ID"
        },
        "resource_tenant": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-03.md#10. User",
            "source_type": "SOURCE_LITERAL",
            "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
          },
          "identifier": "BRD-WS-03-R003.RESOURCE_TENANT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.RESOURCE_TENANT.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-03.md",
            "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
            "source_lines": "L263",
            "source_section": "10. User"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "TENANT_ID",
            "resolver_id": "RESOLVE.BRD-WS-03-R003.BRD-WS-03-R003.RESOURCE_TENANT",
            "version": "1.0.0"
          },
          "semantic_type": "TENANT_ID"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-03-R003",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "One User record is shared across multiple Organizations"
    ],
    "operator_composition": [
      "TENANT_ISOLATED"
    ],
    "positive_oracle": [
      "A distinct User record exists for each Organization membership"
    ],
    "provenance": {
      "approved_decision_references": [
        "P2-DEC-008"
      ],
      "inference": false,
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
      "source_lines": "L263",
      "source_section": "10. User"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-WS-03.md#10. User",
          "source_type": "SOURCE_LITERAL",
          "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
        },
        "identifier": "BRD-WS-03-R003.BRD-WS-03-R003.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-WS-03-R003.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [
            "P2-DEC-008"
          ],
          "inference": false,
          "source_document": "docs/BRD/BRD-WS-03.md",
          "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
          "source_lines": "L263",
          "source_section": "10. User"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-WS-03-R003.BRD-WS-03-R003.BRD-WS-03-R003.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-WS-03-R003.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.PERSON_ID",
        "FIELD.ORGANIZATION_IDS",
        "FIELD.USER_IDS",
        "FIELD.RELATIONSHIP_REFS",
        "FIELD.ISOLATION_RESULT"
      ],
      "producer": "BRD-WS-03-R003.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-WS-03-R003.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.PERSON_ID",
        "FIELD.ORGANIZATION_IDS",
        "FIELD.USER_IDS",
        "FIELD.RELATIONSHIP_REFS",
        "FIELD.ISOLATION_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-WS-03-R003.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-WS-03-R003.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-WS-03-R003.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-WS-03-R003-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED",
          "evaluator_consumed_bindings": [
            "actor_tenant",
            "permission_context",
            "resource_tenant"
          ],
          "evidence_object": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-03.md#10. User",
              "source_type": "SOURCE_LITERAL",
              "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
            },
            "identifier": "BRD-WS-03-R003.BRD-WS-03-R003.O1.1.TENANT_ISOLATED.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-03.md",
              "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
              "source_lines": "L263",
              "source_section": "10. User"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-WS-03-R003.BRD-WS-03-R003.BRD-WS-03-R003.O1.1.TENANT_ISOLATED.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-03.md#10. User",
              "source_type": "SOURCE_LITERAL",
              "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
            },
            "identifier": "BRD-WS-03-R003.BRD-WS-03-R003.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-03.md",
              "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
              "source_lines": "L263",
              "source_section": "10. User"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "TENANT_ID",
              "resolver_id": "RESOLVE.BRD-WS-03-R003.BRD-WS-03-R003.BRD-WS-03-R003.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "TENANT_ID"
          },
          "inference": false,
          "model_conformance_fixture": {
            "bindings": {
              "actor_tenant": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-03.md#10. User",
                  "source_type": "SOURCE_LITERAL",
                  "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
                },
                "identifier": "BRD-WS-03-R003.ACTOR_TENANT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.ACTOR_TENANT.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-03.md",
                  "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
                  "source_lines": "L263",
                  "source_section": "10. User"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "TENANT_ID",
                  "resolver_id": "RESOLVE.BRD-WS-03-R003.BRD-WS-03-R003.ACTOR_TENANT",
                  "version": "1.0.0"
                },
                "semantic_type": "TENANT_ID"
              },
              "permission_context": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-03.md#10. User",
                  "source_type": "SOURCE_LITERAL",
                  "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
                },
                "identifier": "BRD-WS-03-R003.PERMISSION_CONTEXT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.PERMISSION_CONTEXT.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-03.md",
                  "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
                  "source_lines": "L263",
                  "source_section": "10. User"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "POLICY_ID",
                  "resolver_id": "RESOLVE.BRD-WS-03-R003.BRD-WS-03-R003.PERMISSION_CONTEXT",
                  "version": "1.0.0"
                },
                "semantic_type": "POLICY_ID"
              },
              "resource_tenant": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-03.md#10. User",
                  "source_type": "SOURCE_LITERAL",
                  "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
                },
                "identifier": "BRD-WS-03-R003.RESOURCE_TENANT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.RESOURCE_TENANT.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-03.md",
                  "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
                  "source_lines": "L263",
                  "source_section": "10. User"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "TENANT_ID",
                  "resolver_id": "RESOLVE.BRD-WS-03-R003.BRD-WS-03-R003.RESOURCE_TENANT",
                  "version": "1.0.0"
                },
                "semantic_type": "TENANT_ID"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-03.md#10. User",
                  "source_type": "SOURCE_LITERAL",
                  "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
                },
                "identifier": "BRD-WS-03-R003.BRD-WS-03-R003.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-03.md",
                  "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
                  "source_lines": "L263",
                  "source_section": "10. User"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "TENANT_ID",
                  "resolver_id": "RESOLVE.BRD-WS-03-R003.BRD-WS-03-R003.BRD-WS-03-R003.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "TENANT_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-WS-03.md#10. User",
                  "source_type": "SOURCE_LITERAL",
                  "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
                },
                "identifier": "BRD-WS-03-R003.BRD-WS-03-R003.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [
                    "P2-DEC-008"
                  ],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-WS-03.md",
                  "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
                  "source_lines": "L263",
                  "source_section": "10. User"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "TENANT_ID",
                  "resolver_id": "OBSERVE.BRD-WS-03-R003.BRD-WS-03-R003.BRD-WS-03-R003.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "TENANT_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-03.md#10. User",
                "source_type": "SOURCE_LITERAL",
                "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
              },
              "identifier": "BRD-WS-03-R003.BRD-WS-03-R003.O1.1.TENANT_ISOLATED.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-03.md",
                "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
                "source_lines": "L263",
                "source_section": "10. User"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-WS-03-R003.BRD-WS-03-R003.BRD-WS-03-R003.O1.1.TENANT_ISOLATED.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "TENANT_ISOLATED"
          },
          "obligation_id": "BRD-WS-03-R003-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-WS-03.md#10. User",
              "source_type": "SOURCE_LITERAL",
              "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
            },
            "identifier": "BRD-WS-03-R003.BRD-WS-03-R003.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [
                "P2-DEC-008"
              ],
              "inference": false,
              "source_document": "docs/BRD/BRD-WS-03.md",
              "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
              "source_lines": "L263",
              "source_section": "10. User"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "TENANT_ID",
              "resolver_id": "OBSERVE.BRD-WS-03-R003.BRD-WS-03-R003.BRD-WS-03-R003.O1.1.TENANT_ISOLATED.CANONICAL.RESULT",
              "version": "1.0.0"
            },
            "semantic_type": "TENANT_ID"
          },
          "operator_id": "TENANT_ISOLATED",
          "operator_version": "1.0.0-candidate.2",
          "typed_bindings": {
            "actor_tenant": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-03.md#10. User",
                "source_type": "SOURCE_LITERAL",
                "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
              },
              "identifier": "BRD-WS-03-R003.ACTOR_TENANT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.ACTOR_TENANT.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-03.md",
                "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
                "source_lines": "L263",
                "source_section": "10. User"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "TENANT_ID",
                "resolver_id": "RESOLVE.BRD-WS-03-R003.BRD-WS-03-R003.ACTOR_TENANT",
                "version": "1.0.0"
              },
              "semantic_type": "TENANT_ID"
            },
            "permission_context": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-03.md#10. User",
                "source_type": "SOURCE_LITERAL",
                "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
              },
              "identifier": "BRD-WS-03-R003.PERMISSION_CONTEXT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.PERMISSION_CONTEXT.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-03.md",
                "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
                "source_lines": "L263",
                "source_section": "10. User"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "POLICY_ID",
                "resolver_id": "RESOLVE.BRD-WS-03-R003.BRD-WS-03-R003.PERMISSION_CONTEXT",
                "version": "1.0.0"
              },
              "semantic_type": "POLICY_ID"
            },
            "resource_tenant": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-WS-03.md#10. User",
                "source_type": "SOURCE_LITERAL",
                "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
              },
              "identifier": "BRD-WS-03-R003.RESOURCE_TENANT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-WS-03-R003.O1.1.TENANT_ISOLATED.RESOURCE_TENANT.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [
                  "P2-DEC-008"
                ],
                "inference": false,
                "source_document": "docs/BRD/BRD-WS-03.md",
                "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
                "source_lines": "L263",
                "source_section": "10. User"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "TENANT_ID",
                "resolver_id": "RESOLVE.BRD-WS-03-R003.BRD-WS-03-R003.RESOURCE_TENANT",
                "version": "1.0.0"
              },
              "semantic_type": "TENANT_ID"
            }
          }
        }
      ],
      "boundary_cases": [
        "The same person identity may link the Users without merging Organization-scoped User records"
      ],
      "contract_ast_sha256": "2f41e7dac88b18ad1b11ec4df00b21f1d1bfa709eda9f310a43190d6d9cea829",
      "contract_id": "P2C.C4.CONTRACT.BRD-WS-03-R003",
      "criticality": "NORMAL",
      "disposition": "CORRECTABLE_WITH_APPROVED_TYPE_MODEL",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-WS-03.md#10. User",
            "source_type": "SOURCE_LITERAL",
            "version": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8"
          },
          "identifier": "BRD-WS-03-R003.BRD-WS-03-R003.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-WS-03-R003.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [
              "P2-DEC-008"
            ],
            "inference": false,
            "source_document": "docs/BRD/BRD-WS-03.md",
            "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
            "source_lines": "L263",
            "source_section": "10. User"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-WS-03-R003.BRD-WS-03-R003.BRD-WS-03-R003.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-WS-03-R003.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.PERSON_ID",
          "FIELD.ORGANIZATION_IDS",
          "FIELD.USER_IDS",
          "FIELD.RELATIONSHIP_REFS",
          "FIELD.ISOLATION_RESULT"
        ],
        "producer": "BRD-WS-03-R003.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-WS-03-R003.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.PERSON_ID",
          "FIELD.ORGANIZATION_IDS",
          "FIELD.USER_IDS",
          "FIELD.RELATIONSHIP_REFS",
          "FIELD.ISOLATION_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-WS-03-R003.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-WS-03-R003.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-WS-03-R003.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-F38086DE567528869A52",
        "P2C-C4-FX-F4A94F6D26FB7B323729",
        "P2C-C4-FX-D9A9153A3AC910084103"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "One User record is shared across multiple Organizations"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-WS-03-R003-O001",
          "obligation_text": "Nếu một người làm việc cho nhiều Organization thì phải có nhiều User khác nhau"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-WS-03-R003.O1.1.TENANT_ISOLATED"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-WS-03-R003-O001"
        }
      ],
      "operator_composition": [
        "TENANT_ISOLATED"
      ],
      "positive_oracles": [
        "A distinct User record exists for each Organization membership"
      ],
      "preconditions": [
        "The person and Organization memberships are identified"
      ],
      "prohibitions": [
        "One User record is shared across multiple Organizations"
      ],
      "requirement_id": "BRD-WS-03-R003",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [
          "P2-DEC-008"
        ],
        "inference": false,
        "source_document": "docs/BRD/BRD-WS-03.md",
        "source_fingerprint": "c6a0c2a900052e61f0e7f51472022b57b248d27f3fc0b3d6745184cf4c6a6db8",
        "source_lines": "L263",
        "source_section": "10. User"
      },
      "source_statement": "Nếu một người làm việc cho nhiều Organization thì phải có nhiều User khác nhau.",
      "surrounding_source_context": "### BRD-WS-03-R003 — Nếu một người làm việc cho nhiều Organization thì phải có nhiều User khác nhau"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-WS-03-R003",
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
        "BRD-WS-03-R003-AC001",
        "BRD-WS-03-R003-AC002",
        "BRD-WS-03-R003-AC003"
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
    "source_lines": "L1901-L2758",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-03-R003"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-03-R004",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "f37c8b2fcfc805ba591651aae0e91102ded4ec84307acf686ae251d734833594"
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
        "BRD-WS-03-R004-AC001",
        "BRD-WS-03-R004-AC002",
        "BRD-WS-03-R004-AC003"
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
    "source_lines": "L2760-L2835",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-03-R004"
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
      "requirement_id": "BRD-WS-03-R005",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "7a3b81cc54cc7f02c2d4d2400fe1218de9aebccea6d8988b1755c302e2d61ea4"
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
        "BRD-WS-03-R005-AC001",
        "BRD-WS-03-R005-AC002",
        "BRD-WS-03-R005-AC003"
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
    "source_lines": "L2837-L2916",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-03-R005"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-03-R006",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "1d7e11640597c3b9fb2d0ccbe393f7c2219fb6a9e5aab7a191d657df63916eae"
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
        "BRD-WS-03-R006-AC001",
        "BRD-WS-03-R006-AC002",
        "BRD-WS-03-R006-AC003"
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
    "source_fingerprint": "1d7e11640597c3b9fb2d0ccbe393f7c2219fb6a9e5aab7a191d657df63916eae",
    "source_lines": "L2918-L2993",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-03-R006"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-03-R007",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "ecafd73308b8ea281dbaccf45df0b97205df20f8ba9730d7dbdb2a0242f40e33"
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
        "BRD-WS-03-R007-AC001",
        "BRD-WS-03-R007-AC002",
        "BRD-WS-03-R007-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-WS-03-R007-O001",
      "obligation_text": "Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - commission của mình"
    }
  ],
  "criticality_applicability": {
    "AUTHORIZATION_BOUNDARY": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-03-R007-AC003"
      ],
      "rationale": null
    },
    "CONCURRENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-03-R007 does not define a concurrency obligation."
    },
    "IDEMPOTENCY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-03-R007 does not define a idempotency obligation."
    },
    "NEGATIVE_FAIL_CLOSED": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-03-R007-AC002"
      ]
    },
    "POSITIVE": {
      "applicability": "APPLICABLE",
      "criterion_references": [
        "BRD-WS-03-R007-AC001"
      ]
    },
    "RECOVERY": {
      "applicability": "NOT_APPLICABLE",
      "criterion_references": [],
      "rationale": "BRD-WS-03-R007 does not define a recovery obligation."
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
    "source_fingerprint": "ecafd73308b8ea281dbaccf45df0b97205df20f8ba9730d7dbdb2a0242f40e33",
    "source_lines": "L2995-L3105",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-03-R007"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-03-R008",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "a2a1b86b5ce9fdf53b8804c4d73188f3e4c5bbf9bb800f8e5bb9e4e3fd04bf28"
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
        "BRD-WS-03-R008-AC001",
        "BRD-WS-03-R008-AC002",
        "BRD-WS-03-R008-AC003"
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
    "source_lines": "L3107-L3182",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-03-R008"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-03-R009",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "170ae36983a23db4f520bd8934721f072dbbdb868577d944c488c678cd7ad58b"
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
        "BRD-WS-03-R009-AC001",
        "BRD-WS-03-R009-AC002",
        "BRD-WS-03-R009-AC003"
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
    "source_lines": "L3184-L3259",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-03-R009"
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
  "acceptance_contract": {
    "acceptance_content": null,
    "acceptance_state": "PENDING_VERTICAL_SLICE_ACCEPTANCE_ELABORATION",
    "implementation_entry_policy": "SLICE_SPECIFIC_ACCEPTANCE_APPROVAL_REQUIRED_BEFORE_IMPLEMENTATION",
    "traceability": {
      "approved_business_decisions": [],
      "governing_decision": "V23-P2C-PROGRESSIVE-ACCEPTANCE-DECISION-001",
      "inference": false,
      "requirement_id": "BRD-WS-03-R010",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "source_fingerprint": "b1919b8370faf679a072286e43c92a187a5da2df976736a074d38a19fcda7cec"
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
        "BRD-WS-03-R010-AC001",
        "BRD-WS-03-R010-AC002",
        "BRD-WS-03-R010-AC003"
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
    "source_lines": "L3261-L3336",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-WS-03-R010"
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
