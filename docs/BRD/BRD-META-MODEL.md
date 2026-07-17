---
document_code: "BRD-META-MODEL"
document_id: "BRD-META-MODEL"
title: "Enterprise Business Meta Model"
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

# Enterprise Business Meta Model

## BRD-META-MODEL

---

# 1. Purpose

Tài liệu này mô tả mô hình nghiệp vụ tổng thể (Business Meta Model) của nền tảng YSim.

Đây là tài liệu định hướng giúp thống nhất cách hiểu về:

- Business Capability
- Business Object
- Business Policy
- Business Rule
- Business Event
- Business Snapshot

Tài liệu không mô tả nghiệp vụ chi tiết mà chỉ mô tả mối quan hệ giữa các thành phần cốt lõi của Platform.

---

# 2. Business Meta Model

YSim sử dụng mô hình kiến trúc nghiệp vụ như sau.

```text
Business Requirement
        │
        ▼
Business Capability
        │
        ▼
Business Object
        │
        ▼
Business Policy
        │
        ▼
Business Rule
        │
        ▼
Business Event
        │
        ▼
Business Snapshot
```


---

# 2A. Commerce Meta Model (Version 2.1)

Version 2.1 mở rộng Business Meta Model để chuẩn hóa cách xây dựng và vận hành Commerce Experience.

```text
Business Model
        │
        ▼
Business Blueprint
        │
        ▼
Store Template
        │
        ▼
Store Instance
        │
        ▼
Commerce Experience
        │
        ▼
Publishing Target
```

Mô hình này bổ sung một lớp trừu tượng mới giữa Business Capability và Experience Delivery, giúp chuẩn hóa toàn bộ quá trình sinh Store và triển khai Commerce Experience.

---

# 2B. Commerce Meta Components

| Component | Responsibility |
|------------|----------------|
| Business Model | Mô hình kinh doanh chuẩn (Travel, Affiliate, OTA, Hotel, Enterprise...) |
| Business Blueprint | Chuẩn hóa Capability, Experience Flow và Business Rules của một Business Model |
| Store Template | Mẫu cấu hình mặc định để tạo Store |
| Store Instance | Cửa hàng cụ thể của từng Organization |
| Commerce Experience | Trải nghiệm mua hàng được cung cấp cho khách hàng |
| Publishing Target | Kênh xuất bản Commerce Experience |

Business Blueprint và Store Template không chứa dữ liệu vận hành của Organization mà đóng vai trò là tài sản có thể tái sử dụng (Reusable Business Assets).

---

# 2C. Business Factory

YSim áp dụng Business Factory Pattern để chuẩn hóa quá trình tạo Commerce Experience.

```text
Business Requirement
        │
        ▼
Business Model
        │
        ▼
Business Blueprint
        │
        ▼
Store Template
        │
        ▼
Store Instance
```

Business Factory giúp AI và đội phát triển tạo Store theo các Blueprint chuẩn thay vì triển khai từ đầu.


---

# 3. Component Responsibilities

| Component | Responsibility |
|------------|----------------|
| Business Capability | Hệ thống có khả năng làm gì |
| Business Object | Đối tượng nghiệp vụ được quản lý |
| Business Policy | Chính sách điều khiển hành vi |
| Business Rule | Logic xử lý chi tiết |
| Business Event | Điều đã xảy ra trong nghiệp vụ |
| Business Snapshot | Bằng chứng nghiệp vụ tại một thời điểm |

---

# 4. Runtime Flow

Luồng thực thi chuẩn của Platform.

```text
Business Request
        │
        ▼
Capability
        │
        ▼
Policy Decision
        │
        ▼
Business Rule
        │
        ▼
Business Transaction
        │
        ▼
Business Event
        │
        ▼
Business Snapshot
        │
        ├────► Notification
        ├────► Analytics
        ├────► Reporting
        └────► Settlement
```

---

# 5. Enterprise Registries

YSim quản lý các thành phần cốt lõi thông qua năm Registry.

| Registry | Purpose |
|----------|---------|
| BRD-BO-INDEX | Business Object Registry |
| BRD-CAP-INDEX | Business Capability Registry |
| BRD-EVENT-INDEX | Enterprise Business Event Registry |
| BRD-POLICY-INDEX | Enterprise Policy Registry |
| BRD-SNAPSHOT-INDEX | Enterprise Snapshot Registry |

Năm Registry này là **Source of Truth** cho toàn bộ Platform.

---

# 6. Design Principles

## Principle 1

Capability mô tả khả năng của Platform.

Không mô tả dữ liệu.

---

## Principle 2

Business Object là trung tâm của Business Domain.

---

## Principle 3

Policy quyết định cách Platform hoạt động.

Không Hard-code khi có thể cấu hình.

---

## Principle 4

Business Rule mô tả logic chi tiết.

Business Rule được Policy sử dụng.

---

## Principle 5

Business Event phản ánh điều đã xảy ra.

Không phản ánh điều sẽ xảy ra.

---

## Principle 6

Business Snapshot là Business Evidence.

Snapshot không phải History.

---

# 7. Traceability

Mọi thành phần đều có khả năng truy vết.

```text
Requirement
      │
      ▼
Capability
      │
      ▼
Business Object
      │
      ▼
Policy
      │
      ▼
Rule
      │
      ▼
Event
      │
      ▼
Snapshot
      │
      ▼
API
      │
      ▼
Test Case
```

---

# 8. Relationship to Architecture

Business Meta Model là nền tảng cho:

- Domain Model
- Database Design
- API Design
- Event-Driven Architecture
- Commerce Experience Platform (CXP)
- Business Blueprint
- Store Template
- Experience Composition
- Integration
- Security
- Reporting
- Analytics
- Operations

Mọi tài liệu kiến trúc phải tuân thủ Business Meta Model này và mọi Commerce Experience phải được xây dựng từ Business Model và Business Blueprint đã được chuẩn hóa.

---

# 9. Summary

Business Meta Model giúp toàn bộ nền tảng YSim thống nhất:

- Cách mô hình hóa nghiệp vụ.
- Cách đặt tên.
- Cách quản lý dữ liệu.
- Cách quản lý sự kiện.
- Cách quản lý chính sách.
- Cách quản lý bằng chứng nghiệp vụ.

Đây là tài liệu định hướng ở mức Enterprise và là điểm khởi đầu để đọc toàn bộ bộ tài liệu BRD.

---

# Document Status

**Status: FROZEN**

Business Meta Model là tài liệu nền tảng mô tả kiến trúc nghiệp vụ tổng thể của nền tảng YSim.

Mọi thay đổi đối với Business Capability, Business Object, Business Policy, Business Event hoặc Business Snapshot cần được xem xét dựa trên Business Meta Model này để đảm bảo tính nhất quán của toàn bộ hệ thống.

---

<!-- YSIM:PHASE_2C CANONICAL APPENDIX BEGIN -->

## Phụ lục yêu cầu chuẩn tắc v2.3 — C6-R1



<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-META-MODEL-R001 — Snapshot không phải History

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
      "requirement_id": "BRD-META-MODEL-R001",
      "source_document": "docs/BRD/BRD-META-MODEL.md",
      "source_fingerprint": "c175e74595915cb6092056aec89292bc21c059e3f770606d74a04ced4aa37aa1"
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
        "BRD-META-MODEL-R001-AC001",
        "BRD-META-MODEL-R001-AC002",
        "BRD-META-MODEL-R001-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-META-MODEL-R001-O001",
      "obligation_text": "Snapshot không phải History"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Snapshot không phải History.",
  "provenance": {
    "approved_decisions": [],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-META-MODEL-001",
    "previous_temporary_key": "TMP-BRD-META-MODEL-001",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "Principle 6",
    "source_context_sha256": "00228ef1ca6cf1d0b741a6abbf67989dfad1d669b911ce40c25cb0e5bd2bc07a",
    "source_document": "docs/BRD/BRD-META-MODEL.md",
    "source_fingerprint": "c175e74595915cb6092056aec89292bc21c059e3f770606d74a04ced4aa37aa1",
    "source_lines": "L339-L414",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-META-MODEL-R001"
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
  "stable_id": "BRD-META-MODEL-R001",
  "title": "Snapshot không phải History",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-META-MODEL-R003 — Mọi thay đổi đối với Business Capability, Business Object, Business Policy, Business Event hoặc …

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
      "requirement_id": "BRD-META-MODEL-R003",
      "source_document": "docs/BRD/BRD-META-MODEL.md",
      "source_fingerprint": "467c1013d61b65ea0ab9ae922db609dbeeadff1187818ea6e09c6c5e182c998c"
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
        "BRD-META-MODEL-R003-AC001",
        "BRD-META-MODEL-R003-AC002",
        "BRD-META-MODEL-R003-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-META-MODEL-R003-O001",
      "obligation_text": "Mọi thay đổi đối với Business Capability, Business Object, Business Policy, Business Event hoặc Business Snapshot cần được xem xét dựa trên Business Meta Model này để đảm bảo tính nhất quán của toàn bộ hệ thống"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi thay đổi đối với Business Capability, Business Object, Business Policy, Business Event hoặc Business Snapshot cần được xem xét dựa trên Business Meta Model này để đảm bảo tính nhất quán của toàn bộ hệ thống.",
  "provenance": {
    "approved_decisions": [
      "P2-DEC-005"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-META-MODEL-003",
    "previous_temporary_key": "TMP-BRD-META-MODEL-003",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "Document Status",
    "source_context_sha256": "5b3bf5e66b7dccfbfb4eabaa87f94499d118c1ec171939b1d57b0ffd7ae50b19",
    "source_document": "docs/BRD/BRD-META-MODEL.md",
    "source_fingerprint": "467c1013d61b65ea0ab9ae922db609dbeeadff1187818ea6e09c6c5e182c998c",
    "source_lines": "L416-L495",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-META-MODEL-R003"
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
  "stable_id": "BRD-META-MODEL-R003",
  "title": "Mọi thay đổi đối với Business Capability, Business Object, Business Policy, Business Event hoặc …",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-META-MODEL-R004 — Mọi tài liệu kiến trúc phải tuân thủ Business Meta Model này

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
      "requirement_id": "BRD-META-MODEL-R004",
      "source_document": "docs/BRD/BRD-META-MODEL.md",
      "source_fingerprint": "5bd5a650cf9aa829af19e48e83fbcddeb2bc516c3eb645fad09f283f3e6a0372"
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
        "BRD-META-MODEL-R004-AC001",
        "BRD-META-MODEL-R004-AC002",
        "BRD-META-MODEL-R004-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-META-MODEL-R004-O001",
      "obligation_text": "Mọi tài liệu kiến trúc phải tuân thủ Business Meta Model này"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi tài liệu kiến trúc phải tuân thủ Business Meta Model này.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-META-MODEL-002"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-META-MODEL-004",
    "previous_temporary_key": "TMP-BRD-META-MODEL-004",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "5bd5a650cf9aa829af19e48e83fbcddeb2bc516c3eb645fad09f283f3e6a0372",
    "source_document": "docs/BRD/BRD-META-MODEL.md",
    "source_fingerprint": "5bd5a650cf9aa829af19e48e83fbcddeb2bc516c3eb645fad09f283f3e6a0372",
    "source_lines": "L497-L575",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-META-MODEL-R004"
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
  "stable_id": "BRD-META-MODEL-R004",
  "title": "Mọi tài liệu kiến trúc phải tuân thủ Business Meta Model này",
  "verification_criticality": "NORMAL"
}
```
<!-- YSIM:REQUIREMENT END -->

<!-- YSIM:REQUIREMENT BEGIN -->
### BRD-META-MODEL-R005 — Mọi Commerce Experience phải được xây dựng từ Business Model và Business Blueprint đã được chuẩn…

```json
{
  "acceptance_contract": {
    "boundary_oracle": [
      "A new version may reference newer approved sources while preserving prior published lineage"
    ],
    "concrete_bindings": [
      {
        "allowed_lifecycle_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-META-MODEL-R005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                "source_type": "SOURCE_LITERAL",
                "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
              },
              "identifier": "BRD-META-MODEL-R005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-META-MODEL.md",
                "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                "source_lines": "L292",
                "source_section": "8. Relationship to Architecture"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-META-MODEL.md",
            "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
            "source_lines": "L292",
            "source_section": "8. Relationship to Architecture"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "allowed_states": {
          "members": [
            {
              "authoritative_source": {
                "allowed_identifiers": [
                  "BRD-META-MODEL-R005.ALLOWED_STATES.SOURCE.MEMBER"
                ],
                "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                "source_type": "SOURCE_LITERAL",
                "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
              },
              "identifier": "BRD-META-MODEL-R005.ALLOWED_STATES.SOURCE.MEMBER",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-META-MODEL.md",
                "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                "source_lines": "L292",
                "source_section": "8. Relationship to Architecture"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "STATE_ID",
                "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.ALLOWED_STATES.SOURCE.MEMBER",
                "version": "1.0.0"
              },
              "semantic_type": "STATE_ID"
            }
          ],
          "origin": {
            "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-META-MODEL.md",
            "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
            "source_lines": "L292",
            "source_section": "8. Relationship to Architecture"
          },
          "semantic_type": "SET_OF<STATE_ID>"
        },
        "reference": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
            "source_type": "SOURCE_LITERAL",
            "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
          },
          "identifier": "BRD-META-MODEL-R005.REFERENCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-META-MODEL.md",
            "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
            "source_lines": "L292",
            "source_section": "8. Relationship to Architecture"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.REFERENCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "registry": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
            "source_type": "SOURCE_LITERAL",
            "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
          },
          "identifier": "BRD-META-MODEL-R005.REGISTRY",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-META-MODEL.md",
            "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
            "source_lines": "L292",
            "source_section": "8. Relationship to Architecture"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.REGISTRY",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "registry_source": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
            "source_type": "SOURCE_LITERAL",
            "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
          },
          "identifier": "BRD-META-MODEL-R005.REGISTRY_SOURCE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-META-MODEL.md",
            "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
            "source_lines": "L292",
            "source_section": "8. Relationship to Architecture"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "REFERENCE_ID",
            "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.REGISTRY_SOURCE",
            "version": "1.0.0"
          },
          "semantic_type": "REFERENCE_ID"
        },
        "target_id": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
            "source_type": "SOURCE_LITERAL",
            "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
          },
          "identifier": "BRD-META-MODEL-R005.TARGET_ID",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-META-MODEL.md",
            "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
            "source_lines": "L292",
            "source_section": "8. Relationship to Architecture"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_ID",
            "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.TARGET_ID",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_ID"
        },
        "target_type": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
            "source_type": "SOURCE_LITERAL",
            "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
          },
          "identifier": "BRD-META-MODEL-R005.TARGET_TYPE",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
            "origin_type": "SOURCE_LITERAL"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-META-MODEL.md",
            "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
            "source_lines": "L292",
            "source_section": "8. Relationship to Architecture"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "ENTITY_TYPE",
            "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.TARGET_TYPE",
            "version": "1.0.0"
          },
          "semantic_type": "ENTITY_TYPE"
        }
      }
    ],
    "contract_id": "P2C.C4.CONTRACT.BRD-META-MODEL-R005",
    "inference": false,
    "mechanism": "APPROVED_TYPED_CUSTOM_AST",
    "mechanism_version": "C4-R3",
    "negative_oracle": [
      "The Experience has no Business Model or Business Blueprint lineage"
    ],
    "operator_composition": [
      "REFERENCE_TARGET_VALID"
    ],
    "positive_oracle": [
      "The Commerce Experience is traceably built from both identified canonical sources"
    ],
    "provenance": {
      "approved_decision_references": [],
      "inference": false,
      "source_document": "docs/BRD/BRD-META-MODEL.md",
      "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
      "source_lines": "L292",
      "source_section": "8. Relationship to Architecture"
    },
    "required_evidence": {
      "evidence_object_ref": {
        "authoritative_source": {
          "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
          "source_type": "SOURCE_LITERAL",
          "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
        },
        "identifier": "BRD-META-MODEL-R005.BRD-META-MODEL-R005.CONTRACT.EVIDENCE.OBJECT",
        "inference": false,
        "lifecycle": {
          "status": "ACTIVE",
          "version": "2.3"
        },
        "namespace": "YSIM.V2.3",
        "origin": {
          "origin_id": "BRD-META-MODEL-R005.CONTRACT.EVIDENCE.ORIGIN",
          "origin_type": "EVIDENCE_OBJECT"
        },
        "provenance": {
          "approved_decision_references": [],
          "inference": false,
          "source_document": "docs/BRD/BRD-META-MODEL.md",
          "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
          "source_lines": "L292",
          "source_section": "8. Relationship to Architecture"
        },
        "resolver_contract": {
          "deterministic": true,
          "input_types": [],
          "output_type": "EVIDENCE_OBJECT_REF",
          "resolver_id": "OBSERVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.BRD-META-MODEL-R005.CONTRACT.EVIDENCE.OBJECT",
          "version": "1.0.0"
        },
        "semantic_type": "EVIDENCE_OBJECT_REF"
      },
      "inference": false,
      "observed_collection_origin": "BRD-META-MODEL-R005.RUNTIME.OBSERVED.FIELDS",
      "observed_field_ids": [
        "FIELD.EXPERIENCE_ID",
        "FIELD.BUSINESS_MODEL_ID",
        "FIELD.BUSINESS_BLUEPRINT_ID",
        "FIELD.LINEAGE_REFS",
        "FIELD.PUBLISH_RESULT"
      ],
      "producer": "BRD-META-MODEL-R005.EVIDENCE.PRODUCER",
      "required_collection_origin": "BRD-META-MODEL-R005.SOURCE.REQUIRED.FIELDS",
      "required_field_ids": [
        "FIELD.EXPERIENCE_ID",
        "FIELD.BUSINESS_MODEL_ID",
        "FIELD.BUSINESS_BLUEPRINT_ID",
        "FIELD.LINEAGE_REFS",
        "FIELD.PUBLISH_RESULT"
      ],
      "required_values_or_hashes": [
        "BRD-META-MODEL-R005.EVIDENCE.CONTENT.HASH"
      ],
      "retrieval_method": "BRD-META-MODEL-R005.EVIDENCE.RETRIEVAL",
      "version_or_correlation": "BRD-META-MODEL-R005.EVIDENCE.VERSION.CORRELATION"
    },
    "runtime_evidence_executed": false,
    "runtime_status": "RUNTIME_ADAPTER_PENDING",
    "semantic_obligation_references": [
      "BRD-META-MODEL-R005-O001"
    ],
    "typed_contract_ast": {
      "approved_clarification": null,
      "assertions": [
        {
          "assertion_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID",
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
              "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
              "source_type": "SOURCE_LITERAL",
              "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
            },
            "identifier": "BRD-META-MODEL-R005.BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
              "origin_type": "EVIDENCE_OBJECT"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-META-MODEL.md",
              "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
              "source_lines": "L292",
              "source_section": "8. Relationship to Architecture"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "EVIDENCE_OBJECT_REF",
              "resolver_id": "OBSERVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "version": "1.0.0"
            },
            "semantic_type": "EVIDENCE_OBJECT_REF"
          },
          "expected_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
              "source_type": "SOURCE_LITERAL",
              "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
            },
            "identifier": "BRD-META-MODEL-R005.BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
              "origin_type": "SOURCE_LITERAL"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-META-MODEL.md",
              "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
              "source_lines": "L292",
              "source_section": "8. Relationship to Architecture"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                        "BRD-META-MODEL-R005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                      "source_type": "SOURCE_LITERAL",
                      "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
                    },
                    "identifier": "BRD-META-MODEL-R005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-META-MODEL.md",
                      "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                      "source_lines": "L292",
                      "source_section": "8. Relationship to Architecture"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-META-MODEL.md",
                  "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                  "source_lines": "L292",
                  "source_section": "8. Relationship to Architecture"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "allowed_states": {
                "members": [
                  {
                    "authoritative_source": {
                      "allowed_identifiers": [
                        "BRD-META-MODEL-R005.ALLOWED_STATES.SOURCE.MEMBER"
                      ],
                      "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                      "source_type": "SOURCE_LITERAL",
                      "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
                    },
                    "identifier": "BRD-META-MODEL-R005.ALLOWED_STATES.SOURCE.MEMBER",
                    "inference": false,
                    "lifecycle": {
                      "status": "ACTIVE",
                      "version": "2.3"
                    },
                    "namespace": "YSIM.V2.3",
                    "origin": {
                      "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                      "origin_type": "SOURCE_LITERAL"
                    },
                    "provenance": {
                      "approved_decision_references": [],
                      "inference": false,
                      "source_document": "docs/BRD/BRD-META-MODEL.md",
                      "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                      "source_lines": "L292",
                      "source_section": "8. Relationship to Architecture"
                    },
                    "resolver_contract": {
                      "deterministic": true,
                      "input_types": [],
                      "output_type": "STATE_ID",
                      "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.ALLOWED_STATES.SOURCE.MEMBER",
                      "version": "1.0.0"
                    },
                    "semantic_type": "STATE_ID"
                  }
                ],
                "origin": {
                  "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-META-MODEL.md",
                  "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                  "source_lines": "L292",
                  "source_section": "8. Relationship to Architecture"
                },
                "semantic_type": "SET_OF<STATE_ID>"
              },
              "reference": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                  "source_type": "SOURCE_LITERAL",
                  "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
                },
                "identifier": "BRD-META-MODEL-R005.REFERENCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-META-MODEL.md",
                  "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                  "source_lines": "L292",
                  "source_section": "8. Relationship to Architecture"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.REFERENCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "registry": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                  "source_type": "SOURCE_LITERAL",
                  "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
                },
                "identifier": "BRD-META-MODEL-R005.REGISTRY",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-META-MODEL.md",
                  "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                  "source_lines": "L292",
                  "source_section": "8. Relationship to Architecture"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.REGISTRY",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "registry_source": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                  "source_type": "SOURCE_LITERAL",
                  "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
                },
                "identifier": "BRD-META-MODEL-R005.REGISTRY_SOURCE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-META-MODEL.md",
                  "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                  "source_lines": "L292",
                  "source_section": "8. Relationship to Architecture"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.REGISTRY_SOURCE",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "target_id": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                  "source_type": "SOURCE_LITERAL",
                  "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
                },
                "identifier": "BRD-META-MODEL-R005.TARGET_ID",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-META-MODEL.md",
                  "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                  "source_lines": "L292",
                  "source_section": "8. Relationship to Architecture"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_ID",
                  "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.TARGET_ID",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_ID"
              },
              "target_type": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                  "source_type": "SOURCE_LITERAL",
                  "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
                },
                "identifier": "BRD-META-MODEL-R005.TARGET_TYPE",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-META-MODEL.md",
                  "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                  "source_lines": "L292",
                  "source_section": "8. Relationship to Architecture"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "ENTITY_TYPE",
                  "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.TARGET_TYPE",
                  "version": "1.0.0"
                },
                "semantic_type": "ENTITY_TYPE"
              }
            },
            "comparison": {
              "expected": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                  "source_type": "SOURCE_LITERAL",
                  "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
                },
                "identifier": "BRD-META-MODEL-R005.BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.AUTHORITY.ORIGIN",
                  "origin_type": "SOURCE_LITERAL"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-META-MODEL.md",
                  "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                  "source_lines": "L292",
                  "source_section": "8. Relationship to Architecture"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              },
              "observed": {
                "authoritative_source": {
                  "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                  "source_type": "SOURCE_LITERAL",
                  "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
                },
                "identifier": "BRD-META-MODEL-R005.BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                "inference": false,
                "lifecycle": {
                  "status": "ACTIVE",
                  "version": "2.3"
                },
                "namespace": "YSIM.V2.3",
                "origin": {
                  "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
                  "origin_type": "RUNTIME_OBSERVED"
                },
                "provenance": {
                  "approved_decision_references": [],
                  "inference": false,
                  "source_document": "docs/BRD/BRD-META-MODEL.md",
                  "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                  "source_lines": "L292",
                  "source_section": "8. Relationship to Architecture"
                },
                "resolver_contract": {
                  "deterministic": true,
                  "input_types": [],
                  "output_type": "REFERENCE_ID",
                  "resolver_id": "OBSERVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
                  "version": "1.0.0"
                },
                "semantic_type": "REFERENCE_ID"
              }
            },
            "evidence_object": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                "source_type": "SOURCE_LITERAL",
                "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
              },
              "identifier": "BRD-META-MODEL-R005.BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.ORIGIN",
                "origin_type": "EVIDENCE_OBJECT"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-META-MODEL.md",
                "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                "source_lines": "L292",
                "source_section": "8. Relationship to Architecture"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "EVIDENCE_OBJECT_REF",
                "resolver_id": "OBSERVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.EVIDENCE.OBJECT",
                "version": "1.0.0"
              },
              "semantic_type": "EVIDENCE_OBJECT_REF"
            },
            "operator_id": "REFERENCE_TARGET_VALID"
          },
          "obligation_id": "BRD-META-MODEL-R005-O001",
          "observed_operand": {
            "authoritative_source": {
              "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
              "source_type": "SOURCE_LITERAL",
              "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
            },
            "identifier": "BRD-META-MODEL-R005.BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
            "inference": false,
            "lifecycle": {
              "status": "ACTIVE",
              "version": "2.3"
            },
            "namespace": "YSIM.V2.3",
            "origin": {
              "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.OBSERVED.ORIGIN",
              "origin_type": "RUNTIME_OBSERVED"
            },
            "provenance": {
              "approved_decision_references": [],
              "inference": false,
              "source_document": "docs/BRD/BRD-META-MODEL.md",
              "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
              "source_lines": "L292",
              "source_section": "8. Relationship to Architecture"
            },
            "resolver_contract": {
              "deterministic": true,
              "input_types": [],
              "output_type": "REFERENCE_ID",
              "resolver_id": "OBSERVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.CANONICAL.RESULT",
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
                      "BRD-META-MODEL-R005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                    "source_type": "SOURCE_LITERAL",
                    "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
                  },
                  "identifier": "BRD-META-MODEL-R005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-META-MODEL.md",
                    "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                    "source_lines": "L292",
                    "source_section": "8. Relationship to Architecture"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.ALLOWED_LIFECYCLE_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_LIFECYCLE_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-META-MODEL.md",
                "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                "source_lines": "L292",
                "source_section": "8. Relationship to Architecture"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "allowed_states": {
              "members": [
                {
                  "authoritative_source": {
                    "allowed_identifiers": [
                      "BRD-META-MODEL-R005.ALLOWED_STATES.SOURCE.MEMBER"
                    ],
                    "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                    "source_type": "SOURCE_LITERAL",
                    "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
                  },
                  "identifier": "BRD-META-MODEL-R005.ALLOWED_STATES.SOURCE.MEMBER",
                  "inference": false,
                  "lifecycle": {
                    "status": "ACTIVE",
                    "version": "2.3"
                  },
                  "namespace": "YSIM.V2.3",
                  "origin": {
                    "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN.MEMBER.1",
                    "origin_type": "SOURCE_LITERAL"
                  },
                  "provenance": {
                    "approved_decision_references": [],
                    "inference": false,
                    "source_document": "docs/BRD/BRD-META-MODEL.md",
                    "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                    "source_lines": "L292",
                    "source_section": "8. Relationship to Architecture"
                  },
                  "resolver_contract": {
                    "deterministic": true,
                    "input_types": [],
                    "output_type": "STATE_ID",
                    "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.ALLOWED_STATES.SOURCE.MEMBER",
                    "version": "1.0.0"
                  },
                  "semantic_type": "STATE_ID"
                }
              ],
              "origin": {
                "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.ALLOWED_STATES.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-META-MODEL.md",
                "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                "source_lines": "L292",
                "source_section": "8. Relationship to Architecture"
              },
              "semantic_type": "SET_OF<STATE_ID>"
            },
            "reference": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                "source_type": "SOURCE_LITERAL",
                "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
              },
              "identifier": "BRD-META-MODEL-R005.REFERENCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.REFERENCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-META-MODEL.md",
                "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                "source_lines": "L292",
                "source_section": "8. Relationship to Architecture"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.REFERENCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "registry": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                "source_type": "SOURCE_LITERAL",
                "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
              },
              "identifier": "BRD-META-MODEL-R005.REGISTRY",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.REGISTRY.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-META-MODEL.md",
                "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                "source_lines": "L292",
                "source_section": "8. Relationship to Architecture"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.REGISTRY",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "registry_source": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                "source_type": "SOURCE_LITERAL",
                "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
              },
              "identifier": "BRD-META-MODEL-R005.REGISTRY_SOURCE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.REGISTRY_SOURCE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-META-MODEL.md",
                "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                "source_lines": "L292",
                "source_section": "8. Relationship to Architecture"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "REFERENCE_ID",
                "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.REGISTRY_SOURCE",
                "version": "1.0.0"
              },
              "semantic_type": "REFERENCE_ID"
            },
            "target_id": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                "source_type": "SOURCE_LITERAL",
                "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
              },
              "identifier": "BRD-META-MODEL-R005.TARGET_ID",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.TARGET_ID.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-META-MODEL.md",
                "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                "source_lines": "L292",
                "source_section": "8. Relationship to Architecture"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_ID",
                "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.TARGET_ID",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_ID"
            },
            "target_type": {
              "authoritative_source": {
                "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
                "source_type": "SOURCE_LITERAL",
                "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
              },
              "identifier": "BRD-META-MODEL-R005.TARGET_TYPE",
              "inference": false,
              "lifecycle": {
                "status": "ACTIVE",
                "version": "2.3"
              },
              "namespace": "YSIM.V2.3",
              "origin": {
                "origin_id": "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID.TARGET_TYPE.ORIGIN",
                "origin_type": "SOURCE_LITERAL"
              },
              "provenance": {
                "approved_decision_references": [],
                "inference": false,
                "source_document": "docs/BRD/BRD-META-MODEL.md",
                "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
                "source_lines": "L292",
                "source_section": "8. Relationship to Architecture"
              },
              "resolver_contract": {
                "deterministic": true,
                "input_types": [],
                "output_type": "ENTITY_TYPE",
                "resolver_id": "RESOLVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.TARGET_TYPE",
                "version": "1.0.0"
              },
              "semantic_type": "ENTITY_TYPE"
            }
          }
        }
      ],
      "boundary_cases": [
        "A new version may reference newer approved sources while preserving prior published lineage"
      ],
      "contract_ast_sha256": "c0b2dce9cc257d1cfa92d0f35cfd644755861ec0956884b1c732bd5b96f3f814",
      "contract_id": "P2C.C4.CONTRACT.BRD-META-MODEL-R005",
      "criticality": "HIGH",
      "disposition": "OPERATOR_REMAP_REQUIRED",
      "evidence_contract": {
        "evidence_object_ref": {
          "authoritative_source": {
            "source_id": "docs/BRD/BRD-META-MODEL.md#8. Relationship to Architecture",
            "source_type": "SOURCE_LITERAL",
            "version": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06"
          },
          "identifier": "BRD-META-MODEL-R005.BRD-META-MODEL-R005.CONTRACT.EVIDENCE.OBJECT",
          "inference": false,
          "lifecycle": {
            "status": "ACTIVE",
            "version": "2.3"
          },
          "namespace": "YSIM.V2.3",
          "origin": {
            "origin_id": "BRD-META-MODEL-R005.CONTRACT.EVIDENCE.ORIGIN",
            "origin_type": "EVIDENCE_OBJECT"
          },
          "provenance": {
            "approved_decision_references": [],
            "inference": false,
            "source_document": "docs/BRD/BRD-META-MODEL.md",
            "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
            "source_lines": "L292",
            "source_section": "8. Relationship to Architecture"
          },
          "resolver_contract": {
            "deterministic": true,
            "input_types": [],
            "output_type": "EVIDENCE_OBJECT_REF",
            "resolver_id": "OBSERVE.BRD-META-MODEL-R005.BRD-META-MODEL-R005.BRD-META-MODEL-R005.CONTRACT.EVIDENCE.OBJECT",
            "version": "1.0.0"
          },
          "semantic_type": "EVIDENCE_OBJECT_REF"
        },
        "inference": false,
        "observed_collection_origin": "BRD-META-MODEL-R005.RUNTIME.OBSERVED.FIELDS",
        "observed_field_ids": [
          "FIELD.EXPERIENCE_ID",
          "FIELD.BUSINESS_MODEL_ID",
          "FIELD.BUSINESS_BLUEPRINT_ID",
          "FIELD.LINEAGE_REFS",
          "FIELD.PUBLISH_RESULT"
        ],
        "producer": "BRD-META-MODEL-R005.EVIDENCE.PRODUCER",
        "required_collection_origin": "BRD-META-MODEL-R005.SOURCE.REQUIRED.FIELDS",
        "required_field_ids": [
          "FIELD.EXPERIENCE_ID",
          "FIELD.BUSINESS_MODEL_ID",
          "FIELD.BUSINESS_BLUEPRINT_ID",
          "FIELD.LINEAGE_REFS",
          "FIELD.PUBLISH_RESULT"
        ],
        "required_values_or_hashes": [
          "BRD-META-MODEL-R005.EVIDENCE.CONTENT.HASH"
        ],
        "retrieval_method": "BRD-META-MODEL-R005.EVIDENCE.RETRIEVAL",
        "version_or_correlation": "BRD-META-MODEL-R005.EVIDENCE.VERSION.CORRELATION"
      },
      "explicit_non_obligations": [
        "No runtime implementation topology is authorized by this semantic record.",
        "No production runtime evidence is claimed by this model-level candidate."
      ],
      "fixture_ids": [
        "P2C-C4-FX-F84C32523F74577D2186",
        "P2C-C4-FX-E085D8AE31E5DFFC770D",
        "P2C-C4-FX-49828118614F2C0EDFD9"
      ],
      "high_risk_audit_subset": true,
      "independent_contract_identity": true,
      "inference": false,
      "inherits_contract_ast": null,
      "negative_oracles": [
        "The Experience has no Business Model or Business Blueprint lineage"
      ],
      "normative_obligations": [
        {
          "applicability": "V2.3_ACTIVE",
          "obligation_id": "BRD-META-MODEL-R005-O001",
          "obligation_text": "Mọi Commerce Experience phải được xây dựng từ Business Model và Business Blueprint đã được chuẩn hóa"
        }
      ],
      "obligation_to_operator_coverage": [
        {
          "assertion_ids": [
            "BRD-META-MODEL-R005.O1.1.REFERENCE_TARGET_VALID"
          ],
          "coverage_count": 1,
          "obligation_id": "BRD-META-MODEL-R005-O001"
        }
      ],
      "operator_composition": [
        "REFERENCE_TARGET_VALID"
      ],
      "positive_oracles": [
        "The Commerce Experience is traceably built from both identified canonical sources"
      ],
      "preconditions": [
        "An identified standardized Business Model and Business Blueprint exist"
      ],
      "prohibitions": [
        "The Experience has no Business Model or Business Blueprint lineage"
      ],
      "requirement_id": "BRD-META-MODEL-R005",
      "runtime_status": "SLICE_RUNTIME_ADAPTER_REQUIRED",
      "semantic_family_id": null,
      "source_provenance": {
        "approved_decision_references": [],
        "inference": false,
        "source_document": "docs/BRD/BRD-META-MODEL.md",
        "source_fingerprint": "ebcf28b207fbe0bb7e2df6fbafebbfc3a8f3db2f023e536b6c518df80c07fb06",
        "source_lines": "L292",
        "source_section": "8. Relationship to Architecture"
      },
      "source_statement": "Mọi Commerce Experience phải được xây dựng từ Business Model và Business Blueprint đã được chuẩn hóa.",
      "surrounding_source_context": "### BRD-META-MODEL-R005 — Mọi Commerce Experience phải được xây dựng từ Business Model và Business Blueprint đã được chuẩn…"
    }
  },
  "acceptance_mechanism": {
    "contract_id": "P2C.C4.CONTRACT.BRD-META-MODEL-R005",
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
        "BRD-META-MODEL-R005-AC001",
        "BRD-META-MODEL-R005-AC002",
        "BRD-META-MODEL-R005-AC003"
      ],
      "applicability": "V2.3_ACTIVE",
      "obligation_id": "BRD-META-MODEL-R005-O001",
      "obligation_text": "Mọi Commerce Experience phải được xây dựng từ Business Model và Business Blueprint đã được chuẩn hóa"
    }
  ],
  "criticality_applicability": null,
  "criticality_unit": true,
  "delivery_commitment": "COMMITTED_FOR_V2.3",
  "implementation_unit": true,
  "lifecycle": "V2.3_DRAFT",
  "normative_statement": "Mọi Commerce Experience phải được xây dựng từ Business Model và Business Blueprint đã được chuẩn hóa.",
  "provenance": {
    "approved_decisions": [],
    "historical_derived_from": [
      "TMP-BRD-META-MODEL-002"
    ],
    "identity_origin": "APPROVED_TEMPORARY_KEY_MAPPING",
    "original_identity": "TMP-BRD-META-MODEL-005",
    "previous_temporary_key": "TMP-BRD-META-MODEL-005",
    "shared_glossary": "V23_SHARED_CANONICAL_GLOSSARY",
    "source_baseline": "v2.2",
    "source_context_heading": "SOURCE_STATEMENT_FALLBACK",
    "source_context_sha256": "42fa440b90875e3aca9e997a32c417e66ae67de0305006c31a7ae07a1c86c1fa",
    "source_document": "docs/BRD/BRD-META-MODEL.md",
    "source_fingerprint": "42fa440b90875e3aca9e997a32c417e66ae67de0305006c31a7ae07a1c86c1fa",
    "source_lines": "L577-L1929",
    "source_section": "Phase 2C C6-R1 canonical requirement appendix > BRD-META-MODEL-R005"
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
  "stable_id": "BRD-META-MODEL-R005",
  "title": "Mọi Commerce Experience phải được xây dựng từ Business Model và Business Blueprint đã được chuẩn…",
  "verification_criticality": "HIGH"
}
```
<!-- YSIM:REQUIREMENT END -->



<!-- YSIM:IDENTITY HISTORY BEGIN -->

```json

{
  "mapped": [
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-001",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-002",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-003",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-004",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-005",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-006",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-007",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-008",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-009",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-010",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-011",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-012",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-013",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-014",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-015",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-016",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-017",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R017"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-018",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R018"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-019",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R019"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-020",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R020"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-021",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R021"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-022",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-024",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-025",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-026",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R026"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-027",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R027"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-028",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R028"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-029",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R029"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-030",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R030"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-031",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R031"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-032",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R032"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-033",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R033"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-034",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R034"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-035",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R035"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-036",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R036"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-037",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R037"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-038",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R038"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-039",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R039"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-040",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R040"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-041",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R041"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-042",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R042"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-043",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R043"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-044",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R044"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-045",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R045"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-046",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R046"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-047",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R047"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-048",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R048"
    },
    {
      "previous_temporary_key": "TMP-BRD-BO-INDEX-049",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R049"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-001",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-002",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-003",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-004",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-005",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-006",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-007",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-009",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-010",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-011",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-012",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-013",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-014",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-015",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-016",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-017",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R017"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-018",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R018"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-019",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R019"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-020",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R020"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-021",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R021"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-022",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-023",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R023"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-024",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-025",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-026",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R026"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-027",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R027"
    },
    {
      "previous_temporary_key": "TMP-BRD-CAP-INDEX-028",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R028"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-001",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-002",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-003",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-004",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-005",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-006",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-007",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-008",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-009",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-010",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-011",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-012",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-013",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-014",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-025",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-026",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R026"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-027",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R027"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-028",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R028"
    },
    {
      "previous_temporary_key": "TMP-BRD-EVENT-INDEX-029",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R029"
    },
    {
      "previous_temporary_key": "TMP-BRD-META-MODEL-001",
      "source_document": "docs/BRD/BRD-META-MODEL.md",
      "stable_id": "BRD-META-MODEL-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-META-MODEL-003",
      "source_document": "docs/BRD/BRD-META-MODEL.md",
      "stable_id": "BRD-META-MODEL-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-META-MODEL-004",
      "source_document": "docs/BRD/BRD-META-MODEL.md",
      "stable_id": "BRD-META-MODEL-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-META-MODEL-005",
      "source_document": "docs/BRD/BRD-META-MODEL.md",
      "stable_id": "BRD-META-MODEL-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-001",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-002",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-003",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-004",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-005",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-006",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-007",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-008",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-009",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-020",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R020"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-021",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R021"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-022",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-023",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R023"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-024",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-025",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-026",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R026"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-027",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R027"
    },
    {
      "previous_temporary_key": "TMP-BRD-POLICY-INDEX-028",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R028"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-001",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-002",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-003",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-004",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-005",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-006",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-007",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-008",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-009",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-010",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-022",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-023",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R023"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-024",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-025",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-026",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R026"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-027",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R027"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-028",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R028"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-029",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R029"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-030",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R030"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-031",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R031"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-032",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R032"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-033",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R033"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-034",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R034"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-035",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R035"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-036",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R036"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-037",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R037"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-038",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R038"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-039",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R039"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-040",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R040"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-041",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R041"
    },
    {
      "previous_temporary_key": "TMP-BRD-SNAPSHOT-INDEX-042",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "BRD-SNAPSHOT-INDEX-R042"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-001",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-002",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-003",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-004",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-005",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-006",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-007",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-008",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-009",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-010",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-011",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-012",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-013",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-014",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-015",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-016",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-017",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R017"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-018",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R018"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-019",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R019"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-020",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R020"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-021",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R021"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-022",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-023",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R023"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-024",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-025",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-026",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R026"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-027",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R027"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-028",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R028"
    },
    {
      "previous_temporary_key": "TMP-BRD-UPDATE-01-029",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R029"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-001",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-002",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-003",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-004",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-005",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-006",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-007",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-008",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-009",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-010",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-011",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-012",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-013",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-014",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-015",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-016",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-017",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R017"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-018",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R018"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-019",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R019"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-020",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R020"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-021",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R021"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-022",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-023",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R023"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-024",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-025",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-026",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R026"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-027",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R027"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-028",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R028"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-029",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R029"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-030",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R030"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-031",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R031"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-032",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R032"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-033",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R033"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-034",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R034"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-035",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R035"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-01-036",
      "source_document": "docs/BRD/BRD-WS-01.md",
      "stable_id": "BRD-WS-01-R036"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-02-002",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "stable_id": "BRD-WS-02-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-02-003",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "stable_id": "BRD-WS-02-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-02-004",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "stable_id": "BRD-WS-02-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-02-005",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "stable_id": "BRD-WS-02-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-02-006",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "stable_id": "BRD-WS-02-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-03-002",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BRD-WS-03-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-03-003",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BRD-WS-03-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-03-004",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BRD-WS-03-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-03-005",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BRD-WS-03-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-03-006",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BRD-WS-03-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-03-007",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BRD-WS-03-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-03-008",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BRD-WS-03-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-03-009",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BRD-WS-03-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-03-010",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BRD-WS-03-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-001",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-002",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-003",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-004",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-005",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-006",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-007",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-008",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-009",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-010",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-011",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-012",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-013",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-014",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-015",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-04-016",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BRD-WS-04-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-001",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-002",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-003",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-004",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-005",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-006",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-007",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-008",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-009",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-011",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-012",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-013",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-014",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-015",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-016",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-017",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R017"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-018",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R018"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-019",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R019"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-020",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R020"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-021",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R021"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-022",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-023",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R023"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-024",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-025",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-026",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R026"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-027",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R027"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-028",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R028"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-05-029",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R029"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-001",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-002",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-003",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-004",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-005",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-006",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-007",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-008",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-009",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-010",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-011",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-012",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-013",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-014",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-015",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-016",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-017",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R017"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-018",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R018"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-019",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R019"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-020",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R020"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-021",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R021"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-022",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-023",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R023"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-024",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-025",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-026",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R026"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-027",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R027"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-06-028",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BRD-WS-06-R028"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-001",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-003",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-004",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-005",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-006",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-007",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-008",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-009",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-010",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-011",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-012",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-013",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-014",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-015",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-016",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-017",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R017"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-018",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R018"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-019",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R019"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-020",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R020"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-021",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R021"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-022",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-023",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R023"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-024",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-025",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-026",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R026"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-07-027",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BRD-WS-07-R027"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-08-002",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BRD-WS-08-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-08-003",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BRD-WS-08-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-08-004",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BRD-WS-08-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-08-005",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BRD-WS-08-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-08-006",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BRD-WS-08-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-08-007",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BRD-WS-08-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-08-008",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BRD-WS-08-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-08-010",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BRD-WS-08-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-08-011",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BRD-WS-08-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-08-012",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BRD-WS-08-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-001",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-003",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-004",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-005",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-006",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-007",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-008",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-009",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-010",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-011",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-012",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-013",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-09-014",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BRD-WS-09-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-10-001",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BRD-WS-10-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-10-002",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BRD-WS-10-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-10-003",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BRD-WS-10-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-10-004",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BRD-WS-10-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-10-007",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BRD-WS-10-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-001",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-002",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-003",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-004",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-005",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-006",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-007",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-008",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-009",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-010",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-011",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-012",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-013",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-014",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-015",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-016",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-11-017",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R017"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-002",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-003",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-004",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-005",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-006",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-007",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-008",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-009",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-010",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-011",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-012",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-013",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-12-014",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BRD-WS-12-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-001",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-002",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-003",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-004",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-005",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-006",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-007",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-008",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-009",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-010",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-011",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-012",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-013",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-014",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-015",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-016",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-017",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R017"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-018",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R018"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-019",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R019"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-020",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R020"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-021",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R021"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-022",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-023",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R023"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-024",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-13-025",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-001",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-003",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-004",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-005",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-006",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-007",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-008",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-009",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-010",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-011",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-012",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-013",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-014",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-015",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-016",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-017",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R017"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-018",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R018"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-019",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R019"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-020",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R020"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-021",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R021"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-022",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-023",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R023"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-024",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-025",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-026",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R026"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-028",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R028"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-029",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R029"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-030",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R030"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-031",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R031"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-032",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R032"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-033",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R033"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-034",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R034"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-035",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R035"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-036",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R036"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-037",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R037"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-14-038",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R038"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-003",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-004",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-005",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-006",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-007",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-008",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-009",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-010",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-011",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-012",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-013",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-014",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-015",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-016",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-017",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R017"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-018",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R018"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-019",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R019"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-020",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R020"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-021",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R021"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-022",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-023",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R023"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-024",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-025",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R025"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-15-026",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R026"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-001",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-002",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-003",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-004",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-005",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R005"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-006",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-007",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-008",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-010",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-011",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-012",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-013",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-014",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-015",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-16-016",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-001",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R001"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-002",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R002"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-003",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R003"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-004",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R004"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-006",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R006"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-007",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R007"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-008",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R008"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-009",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R009"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-010",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R010"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-011",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R011"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-012",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R012"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-013",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R013"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-014",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R014"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-015",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R015"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-016",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R016"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-017",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R017"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-018",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R018"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-019",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R019"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-020",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R020"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-021",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R021"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-022",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R022"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-023",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R023"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-024",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R024"
    },
    {
      "previous_temporary_key": "TMP-BRD-WS-17-025",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R025"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-001",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R001"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-002",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R002"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-003",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R003"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-004",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R004"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-005",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R005"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-006",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R006"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-007",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R007"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-008",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R008"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-009",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R009"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-010",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R010"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-011",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R011"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-012",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R012"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-013",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R013"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-014",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R014"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-015",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R015"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-016",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R016"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-017",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R017"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-018",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R018"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-019",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R019"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-020",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R020"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-021",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R021"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-022",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R022"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-023",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R023"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-024",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R024"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-025",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R025"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-026",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R026"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-027",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R027"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-028",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R028"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-029",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R029"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-030",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R030"
    },
    {
      "previous_temporary_key": "TMP-UXF-00-031",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-00-R031"
    },
    {
      "previous_temporary_key": "TMP-UXF-01-001",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-01-R001"
    },
    {
      "previous_temporary_key": "TMP-UXF-01-002",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-01-R002"
    },
    {
      "previous_temporary_key": "TMP-UXF-01-003",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-01-R003"
    },
    {
      "previous_temporary_key": "TMP-UXF-01-004",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-01-R004"
    },
    {
      "previous_temporary_key": "TMP-UXF-01-005",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-01-R005"
    },
    {
      "previous_temporary_key": "TMP-UXF-01-006",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-01-R006"
    },
    {
      "previous_temporary_key": "TMP-UXF-01-007",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-01-R007"
    },
    {
      "previous_temporary_key": "TMP-UXF-01-008",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-01-R008"
    },
    {
      "previous_temporary_key": "TMP-UXF-01-009",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-01-R009"
    },
    {
      "previous_temporary_key": "TMP-UXF-01-010",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-01-R010"
    },
    {
      "previous_temporary_key": "TMP-UXF-01-011",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-01-R011"
    },
    {
      "previous_temporary_key": "TMP-UXF-02-001",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-02-R001"
    },
    {
      "previous_temporary_key": "TMP-UXF-02-002",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-02-R002"
    },
    {
      "previous_temporary_key": "TMP-UXF-02-003",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-02-R003"
    },
    {
      "previous_temporary_key": "TMP-UXF-02-004",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-02-R004"
    },
    {
      "previous_temporary_key": "TMP-UXF-02-005",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-02-R005"
    },
    {
      "previous_temporary_key": "TMP-UXF-02-006",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-02-R006"
    },
    {
      "previous_temporary_key": "TMP-UXF-02-007",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-02-R007"
    },
    {
      "previous_temporary_key": "TMP-UXF-02-008",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-02-R008"
    },
    {
      "previous_temporary_key": "TMP-UXF-02-009",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-02-R009"
    },
    {
      "previous_temporary_key": "TMP-UXF-03-001",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-03-R001"
    },
    {
      "previous_temporary_key": "TMP-UXF-03-002",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-03-R002"
    },
    {
      "previous_temporary_key": "TMP-UXF-03-003",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-03-R003"
    },
    {
      "previous_temporary_key": "TMP-UXF-03-004",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-03-R004"
    },
    {
      "previous_temporary_key": "TMP-UXF-03-005",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-03-R005"
    },
    {
      "previous_temporary_key": "TMP-UXF-03-006",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-03-R006"
    },
    {
      "previous_temporary_key": "TMP-UXF-03-007",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-03-R007"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-001",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R001"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-002",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R002"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-003",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R003"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-004",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R004"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-005",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R005"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-006",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R006"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-007",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R007"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-008",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R008"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-009",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R009"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-010",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R010"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-011",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R011"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-012",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R012"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-013",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R013"
    },
    {
      "previous_temporary_key": "TMP-UXF-04-014",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-04-R014"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-001",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R001"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-002",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R002"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-003",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R003"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-004",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R004"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-005",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R005"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-006",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R006"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-007",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R007"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-008",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R008"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-009",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R009"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-010",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R010"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-011",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R011"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-012",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R012"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-014",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R014"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-015",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R015"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-016",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R016"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-017",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R017"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-018",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R018"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-019",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R019"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-020",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R020"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-021",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R021"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-022",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R022"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-033",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R033"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-034",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R034"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-035",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R035"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-036",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R036"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-037",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R037"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-038",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R038"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-039",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R039"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-040",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R040"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-041",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R041"
    },
    {
      "previous_temporary_key": "TMP-UXF-05-042",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R042"
    }
  ],
  "newly_allocated": [
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R050"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R051"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BRD-BO-INDEX-R052"
    },
    {
      "allocation_contract": "P2-ALLOC-001",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R029"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R030"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "BRD-CAP-INDEX-R031"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R030"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R031"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R032"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R033"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R034"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R035"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "BRD-EVENT-INDEX-R036"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R029"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R030"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R031"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R032"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "BRD-POLICY-INDEX-R033"
    },
    {
      "allocation_contract": "BUSINESS_PRINCIPLES_CHILD_RECONCILIATION",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R030"
    },
    {
      "allocation_contract": "BUSINESS_PRINCIPLES_CHILD_RECONCILIATION",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R031"
    },
    {
      "allocation_contract": "BUSINESS_PRINCIPLES_CHILD_RECONCILIATION",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R032"
    },
    {
      "allocation_contract": "BUSINESS_PRINCIPLES_CHILD_RECONCILIATION",
      "source_document": "docs/BRD/BRD-UPDATE-01.md",
      "stable_id": "BRD-UPDATE-01-R033"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R030"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BRD-WS-05-R031"
    },
    {
      "allocation_contract": "FRAUD_RISK_ACTIVE_DEFERRED_SPLIT",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BRD-WS-08-R013"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R018"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BRD-WS-11-R019"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R026"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R027"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R028"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R029"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R030"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R031"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R032"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R033"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R034"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R035"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R036"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R037"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R038"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R039"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R040"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R041"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R042"
    },
    {
      "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R043"
    },
    {
      "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R044"
    },
    {
      "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BRD-WS-13-R045"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R039"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R040"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R041"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R042"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R043"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R044"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R045"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R046"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R047"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R048"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R049"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R050"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R051"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R052"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BRD-WS-14-R053"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R027"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R028"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R029"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R030"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R031"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R032"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R033"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R034"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R035"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R036"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R037"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R038"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R039"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R040"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R041"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R042"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R043"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R044"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R045"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R046"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R047"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R048"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R049"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R050"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R051"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R052"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R053"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R054"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R055"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R056"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BRD-WS-15-R057"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R017"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R018"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R019"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R020"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R021"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R022"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R023"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R024"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R025"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R026"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R027"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R028"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R029"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R030"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R031"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R032"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R033"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R034"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R035"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R036"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R037"
    },
    {
      "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R038"
    },
    {
      "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R039"
    },
    {
      "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R040"
    },
    {
      "allocation_contract": "C3_APPROVED_DECISION_ATOMIC_SPLIT",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BRD-WS-16-R041"
    },
    {
      "allocation_contract": "ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R026"
    },
    {
      "allocation_contract": "ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R027"
    },
    {
      "allocation_contract": "ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R028"
    },
    {
      "allocation_contract": "ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R029"
    },
    {
      "allocation_contract": "ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R030"
    },
    {
      "allocation_contract": "ENTERPRISE_OPERATIONS_CHILD_RECONCILIATION",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R031"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R032"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R033"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R034"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R035"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R036"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R037"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R038"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R039"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R040"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R041"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R042"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BRD-WS-17-R043"
    },
    {
      "allocation_contract": "P2-ALLOC-002",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R054"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R055"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R056"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R057"
    },
    {
      "allocation_contract": "C3_STRUCTURAL_RECONCILIATION_CHILD",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-05-R058"
    }
  ],
  "preserved": [
    {
      "previous_identity": "BD-02-001",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "stable_id": "BD-02-001"
    },
    {
      "previous_identity": "BD-02-002",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "stable_id": "BD-02-002"
    },
    {
      "previous_identity": "BD-02-003",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "stable_id": "BD-02-003"
    },
    {
      "previous_identity": "BD-02-004",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "stable_id": "BD-02-004"
    },
    {
      "previous_identity": "BD-02-005",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "stable_id": "BD-02-005"
    },
    {
      "previous_identity": "BD-02-006",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "stable_id": "BD-02-006"
    },
    {
      "previous_identity": "BD-02-007",
      "source_document": "docs/BRD/BRD-WS-02.md",
      "stable_id": "BD-02-007"
    },
    {
      "previous_identity": "BD-03-001",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-001"
    },
    {
      "previous_identity": "BD-03-002",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-002"
    },
    {
      "previous_identity": "BD-03-003",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-003"
    },
    {
      "previous_identity": "BD-03-004",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-004"
    },
    {
      "previous_identity": "BD-03-005",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-005"
    },
    {
      "previous_identity": "BD-03-006",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-006"
    },
    {
      "previous_identity": "BD-03-007",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-007"
    },
    {
      "previous_identity": "BD-03-008",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-008"
    },
    {
      "previous_identity": "BD-03-009",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-009"
    },
    {
      "previous_identity": "BD-03-010",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-010"
    },
    {
      "previous_identity": "BD-03-011",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-011"
    },
    {
      "previous_identity": "BD-03-012",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-012"
    },
    {
      "previous_identity": "BD-03-013",
      "source_document": "docs/BRD/BRD-WS-03.md",
      "stable_id": "BD-03-013"
    },
    {
      "previous_identity": "BD-04-001",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BD-04-001"
    },
    {
      "previous_identity": "BD-04-002",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BD-04-002"
    },
    {
      "previous_identity": "BD-04-003",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BD-04-003"
    },
    {
      "previous_identity": "BD-04-004",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BD-04-004"
    },
    {
      "previous_identity": "BD-04-005",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BD-04-005"
    },
    {
      "previous_identity": "BD-04-006",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BD-04-006"
    },
    {
      "previous_identity": "BD-04-007",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BD-04-007"
    },
    {
      "previous_identity": "BD-04-008",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BD-04-008"
    },
    {
      "previous_identity": "BD-04-009",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BD-04-009"
    },
    {
      "previous_identity": "BD-04-010",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BD-04-010"
    },
    {
      "previous_identity": "BD-04-011",
      "source_document": "docs/BRD/BRD-WS-04.md",
      "stable_id": "BD-04-011"
    },
    {
      "previous_identity": "BD-05-001",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-001"
    },
    {
      "previous_identity": "BD-05-002",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-002"
    },
    {
      "previous_identity": "BD-05-003",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-003"
    },
    {
      "previous_identity": "BD-05-004",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-004"
    },
    {
      "previous_identity": "BD-05-005",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-005"
    },
    {
      "previous_identity": "BD-05-006",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-006"
    },
    {
      "previous_identity": "BD-05-007",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-007"
    },
    {
      "previous_identity": "BD-05-008",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-008"
    },
    {
      "previous_identity": "BD-05-009",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-009"
    },
    {
      "previous_identity": "BD-05-010",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-010"
    },
    {
      "previous_identity": "BD-05-011",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-011"
    },
    {
      "previous_identity": "BD-05-012",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-012"
    },
    {
      "previous_identity": "BD-05-013",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-013"
    },
    {
      "previous_identity": "BD-05-014",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-014"
    },
    {
      "previous_identity": "BD-05-015",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-015"
    },
    {
      "previous_identity": "BD-05-016",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-016"
    },
    {
      "previous_identity": "BD-05-017",
      "source_document": "docs/BRD/BRD-WS-05.md",
      "stable_id": "BD-05-017"
    },
    {
      "previous_identity": "BD-06-001",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-001"
    },
    {
      "previous_identity": "BD-06-002",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-002"
    },
    {
      "previous_identity": "BD-06-003",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-003"
    },
    {
      "previous_identity": "BD-06-004",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-004"
    },
    {
      "previous_identity": "BD-06-005",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-005"
    },
    {
      "previous_identity": "BD-06-006",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-006"
    },
    {
      "previous_identity": "BD-06-007",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-007"
    },
    {
      "previous_identity": "BD-06-008",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-008"
    },
    {
      "previous_identity": "BD-06-009",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-009"
    },
    {
      "previous_identity": "BD-06-010",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-010"
    },
    {
      "previous_identity": "BD-06-011",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-011"
    },
    {
      "previous_identity": "BD-06-012",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-012"
    },
    {
      "previous_identity": "BD-06-013",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-013"
    },
    {
      "previous_identity": "BD-06-014",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-014"
    },
    {
      "previous_identity": "BD-06-015",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-015"
    },
    {
      "previous_identity": "BD-06-016",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "BD-06-016"
    },
    {
      "previous_identity": "BD-07-001",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-001"
    },
    {
      "previous_identity": "BD-07-002",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-002"
    },
    {
      "previous_identity": "BD-07-003",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-003"
    },
    {
      "previous_identity": "BD-07-004",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-004"
    },
    {
      "previous_identity": "BD-07-005",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-005"
    },
    {
      "previous_identity": "BD-07-006",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-006"
    },
    {
      "previous_identity": "BD-07-007",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-007"
    },
    {
      "previous_identity": "BD-07-008",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-008"
    },
    {
      "previous_identity": "BD-07-009",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-009"
    },
    {
      "previous_identity": "BD-07-010",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-010"
    },
    {
      "previous_identity": "BD-07-011",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-011"
    },
    {
      "previous_identity": "BD-07-012",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-012"
    },
    {
      "previous_identity": "BD-07-013",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-013"
    },
    {
      "previous_identity": "BD-07-014",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-014"
    },
    {
      "previous_identity": "BD-07-015",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-015"
    },
    {
      "previous_identity": "BD-07-016",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-016"
    },
    {
      "previous_identity": "BD-07-017",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-017"
    },
    {
      "previous_identity": "BD-07-018",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-018"
    },
    {
      "previous_identity": "BD-07-019",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "BD-07-019"
    },
    {
      "previous_identity": "BD-08-001",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-001"
    },
    {
      "previous_identity": "BD-08-002",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-002"
    },
    {
      "previous_identity": "BD-08-003",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-003"
    },
    {
      "previous_identity": "BD-08-004",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-004"
    },
    {
      "previous_identity": "BD-08-005",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-005"
    },
    {
      "previous_identity": "BD-08-006",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-006"
    },
    {
      "previous_identity": "BD-08-007",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-007"
    },
    {
      "previous_identity": "BD-08-008",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-008"
    },
    {
      "previous_identity": "BD-08-009",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-009"
    },
    {
      "previous_identity": "BD-08-010",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-010"
    },
    {
      "previous_identity": "BD-08-011",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-011"
    },
    {
      "previous_identity": "BD-08-012",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-012"
    },
    {
      "previous_identity": "BD-08-013",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-013"
    },
    {
      "previous_identity": "BD-08-014",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-014"
    },
    {
      "previous_identity": "BD-08-015",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-015"
    },
    {
      "previous_identity": "BD-08-016",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-016"
    },
    {
      "previous_identity": "BD-08-017",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "BD-08-017"
    },
    {
      "previous_identity": "BD-09-001",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-001"
    },
    {
      "previous_identity": "BD-09-002",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-002"
    },
    {
      "previous_identity": "BD-09-003",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-003"
    },
    {
      "previous_identity": "BD-09-004",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-004"
    },
    {
      "previous_identity": "BD-09-005",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-005"
    },
    {
      "previous_identity": "BD-09-006",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-006"
    },
    {
      "previous_identity": "BD-09-007",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-007"
    },
    {
      "previous_identity": "BD-09-008",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-008"
    },
    {
      "previous_identity": "BD-09-009",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-009"
    },
    {
      "previous_identity": "BD-09-010",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-010"
    },
    {
      "previous_identity": "BD-09-011",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-011"
    },
    {
      "previous_identity": "BD-09-012",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-012"
    },
    {
      "previous_identity": "BD-09-013",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-013"
    },
    {
      "previous_identity": "BD-09-014",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-014"
    },
    {
      "previous_identity": "BD-09-015",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "BD-09-015"
    },
    {
      "previous_identity": "BD-10-001",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-001"
    },
    {
      "previous_identity": "BD-10-002",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-002"
    },
    {
      "previous_identity": "BD-10-003",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-003"
    },
    {
      "previous_identity": "BD-10-004",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-004"
    },
    {
      "previous_identity": "BD-10-005",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-005"
    },
    {
      "previous_identity": "BD-10-006",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-006"
    },
    {
      "previous_identity": "BD-10-007",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-007"
    },
    {
      "previous_identity": "BD-10-008",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-008"
    },
    {
      "previous_identity": "BD-10-009",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-009"
    },
    {
      "previous_identity": "BD-10-010",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-010"
    },
    {
      "previous_identity": "BD-10-011",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-011"
    },
    {
      "previous_identity": "BD-10-012",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-012"
    },
    {
      "previous_identity": "BD-10-013",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-013"
    },
    {
      "previous_identity": "BD-10-014",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-014"
    },
    {
      "previous_identity": "BD-10-015",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-015"
    },
    {
      "previous_identity": "BD-10-016",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-016"
    },
    {
      "previous_identity": "BD-10-017",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-017"
    },
    {
      "previous_identity": "BD-10-018",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-018"
    },
    {
      "previous_identity": "BD-10-019",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-019"
    },
    {
      "previous_identity": "BD-10-020",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-020"
    },
    {
      "previous_identity": "BD-10-021",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-021"
    },
    {
      "previous_identity": "BD-10-022",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-022"
    },
    {
      "previous_identity": "BD-10-023",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "BD-10-023"
    },
    {
      "previous_identity": "BD-11-001",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-001"
    },
    {
      "previous_identity": "BD-11-002",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-002"
    },
    {
      "previous_identity": "BD-11-003",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-003"
    },
    {
      "previous_identity": "BD-11-004",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-004"
    },
    {
      "previous_identity": "BD-11-005",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-005"
    },
    {
      "previous_identity": "BD-11-006",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-006"
    },
    {
      "previous_identity": "BD-11-007",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-007"
    },
    {
      "previous_identity": "BD-11-008",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-008"
    },
    {
      "previous_identity": "BD-11-009",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-009"
    },
    {
      "previous_identity": "BD-11-010",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-010"
    },
    {
      "previous_identity": "BD-11-011",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-011"
    },
    {
      "previous_identity": "BD-11-012",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-012"
    },
    {
      "previous_identity": "BD-11-013",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-013"
    },
    {
      "previous_identity": "BD-11-014",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-014"
    },
    {
      "previous_identity": "BD-11-015",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "BD-11-015"
    },
    {
      "previous_identity": "BD-12-001",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-001"
    },
    {
      "previous_identity": "BD-12-002",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-002"
    },
    {
      "previous_identity": "BD-12-003",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-003"
    },
    {
      "previous_identity": "BD-12-004",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-004"
    },
    {
      "previous_identity": "BD-12-005",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-005"
    },
    {
      "previous_identity": "BD-12-006",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-006"
    },
    {
      "previous_identity": "BD-12-007",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-007"
    },
    {
      "previous_identity": "BD-12-008",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-008"
    },
    {
      "previous_identity": "BD-12-009",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-009"
    },
    {
      "previous_identity": "BD-12-010",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-010"
    },
    {
      "previous_identity": "BD-12-011",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-011"
    },
    {
      "previous_identity": "BD-12-012",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-012"
    },
    {
      "previous_identity": "BD-12-013",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-013"
    },
    {
      "previous_identity": "BD-12-014",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-014"
    },
    {
      "previous_identity": "BD-12-015",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-015"
    },
    {
      "previous_identity": "BD-12-016",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-016"
    },
    {
      "previous_identity": "BD-12-017",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-017"
    },
    {
      "previous_identity": "BD-12-018",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-018"
    },
    {
      "previous_identity": "BD-12-019",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "BD-12-019"
    },
    {
      "previous_identity": "BD-13-001",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-001"
    },
    {
      "previous_identity": "BD-13-002",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-002"
    },
    {
      "previous_identity": "BD-13-003",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-003"
    },
    {
      "previous_identity": "BD-13-004",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-004"
    },
    {
      "previous_identity": "BD-13-005",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-005"
    },
    {
      "previous_identity": "BD-13-006",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-006"
    },
    {
      "previous_identity": "BD-13-007",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-007"
    },
    {
      "previous_identity": "BD-13-008",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-008"
    },
    {
      "previous_identity": "BD-13-009",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-009"
    },
    {
      "previous_identity": "BD-13-010",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-010"
    },
    {
      "previous_identity": "BD-13-011",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-011"
    },
    {
      "previous_identity": "BD-13-012",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-012"
    },
    {
      "previous_identity": "BD-13-013",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-013"
    },
    {
      "previous_identity": "BD-13-014",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-014"
    },
    {
      "previous_identity": "BD-13-015",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-015"
    },
    {
      "previous_identity": "BD-13-016",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-016"
    },
    {
      "previous_identity": "BD-13-017",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-017"
    },
    {
      "previous_identity": "BD-13-018",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-018"
    },
    {
      "previous_identity": "BD-13-019",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-019"
    },
    {
      "previous_identity": "BD-13-020",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "BD-13-020"
    },
    {
      "previous_identity": "BD-14-001",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-001"
    },
    {
      "previous_identity": "BD-14-002",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-002"
    },
    {
      "previous_identity": "BD-14-003",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-003"
    },
    {
      "previous_identity": "BD-14-004",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-004"
    },
    {
      "previous_identity": "BD-14-005",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-005"
    },
    {
      "previous_identity": "BD-14-006",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-006"
    },
    {
      "previous_identity": "BD-14-007",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-007"
    },
    {
      "previous_identity": "BD-14-008",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-008"
    },
    {
      "previous_identity": "BD-14-009",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-009"
    },
    {
      "previous_identity": "BD-14-010",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-010"
    },
    {
      "previous_identity": "BD-14-011",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-011"
    },
    {
      "previous_identity": "BD-14-012",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-012"
    },
    {
      "previous_identity": "BD-14-013",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-013"
    },
    {
      "previous_identity": "BD-14-014",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-014"
    },
    {
      "previous_identity": "BD-14-015",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-015"
    },
    {
      "previous_identity": "BD-14-016",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-016"
    },
    {
      "previous_identity": "BD-14-017",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-017"
    },
    {
      "previous_identity": "BD-14-018",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-018"
    },
    {
      "previous_identity": "BD-14-019",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-019"
    },
    {
      "previous_identity": "BD-14-020",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-020"
    },
    {
      "previous_identity": "BD-14-021",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-021"
    },
    {
      "previous_identity": "BD-14-022",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-022"
    },
    {
      "previous_identity": "BD-14-023",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-023"
    },
    {
      "previous_identity": "BD-14-024",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-024"
    },
    {
      "previous_identity": "BD-14-025",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-025"
    },
    {
      "previous_identity": "BD-14-026",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "BD-14-026"
    },
    {
      "previous_identity": "BD-15-001",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-001"
    },
    {
      "previous_identity": "BD-15-002",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-002"
    },
    {
      "previous_identity": "BD-15-003",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-003"
    },
    {
      "previous_identity": "BD-15-004",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-004"
    },
    {
      "previous_identity": "BD-15-005",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-005"
    },
    {
      "previous_identity": "BD-15-006",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-006"
    },
    {
      "previous_identity": "BD-15-007",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-007"
    },
    {
      "previous_identity": "BD-15-008",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-008"
    },
    {
      "previous_identity": "BD-15-009",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-009"
    },
    {
      "previous_identity": "BD-15-010",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-010"
    },
    {
      "previous_identity": "BD-15-011",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-011"
    },
    {
      "previous_identity": "BD-15-012",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-012"
    },
    {
      "previous_identity": "BD-15-013",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-013"
    },
    {
      "previous_identity": "BD-15-014",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-014"
    },
    {
      "previous_identity": "BD-15-015",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-015"
    },
    {
      "previous_identity": "BD-15-016",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-016"
    },
    {
      "previous_identity": "BD-15-017",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-017"
    },
    {
      "previous_identity": "BD-15-018",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-018"
    },
    {
      "previous_identity": "BD-15-019",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-019"
    },
    {
      "previous_identity": "BD-15-020",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-020"
    },
    {
      "previous_identity": "BD-15-021",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-021"
    },
    {
      "previous_identity": "BD-15-022",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-022"
    },
    {
      "previous_identity": "BD-15-023",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-023"
    },
    {
      "previous_identity": "BD-15-024",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-024"
    },
    {
      "previous_identity": "BD-15-025",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-025"
    },
    {
      "previous_identity": "BD-15-026",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-026"
    },
    {
      "previous_identity": "BD-15-027",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-027"
    },
    {
      "previous_identity": "BD-15-028",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-028"
    },
    {
      "previous_identity": "BD-15-029",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-029"
    },
    {
      "previous_identity": "BD-15-030",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "BD-15-030"
    },
    {
      "previous_identity": "BD-16-001",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-001"
    },
    {
      "previous_identity": "BD-16-002",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-002"
    },
    {
      "previous_identity": "BD-16-003",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-003"
    },
    {
      "previous_identity": "BD-16-004",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-004"
    },
    {
      "previous_identity": "BD-16-005",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-005"
    },
    {
      "previous_identity": "BD-16-006",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-006"
    },
    {
      "previous_identity": "BD-16-007",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-007"
    },
    {
      "previous_identity": "BD-16-008",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-008"
    },
    {
      "previous_identity": "BD-16-009",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-009"
    },
    {
      "previous_identity": "BD-16-010",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-010"
    },
    {
      "previous_identity": "BD-16-011",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-011"
    },
    {
      "previous_identity": "BD-16-012",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-012"
    },
    {
      "previous_identity": "BD-16-013",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-013"
    },
    {
      "previous_identity": "BD-16-014",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-014"
    },
    {
      "previous_identity": "BD-16-015",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-015"
    },
    {
      "previous_identity": "BD-16-016",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-016"
    },
    {
      "previous_identity": "BD-16-017",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-017"
    },
    {
      "previous_identity": "BD-16-018",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-018"
    },
    {
      "previous_identity": "BD-16-019",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-019"
    },
    {
      "previous_identity": "BD-16-020",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-020"
    },
    {
      "previous_identity": "BD-16-021",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-021"
    },
    {
      "previous_identity": "BD-16-022",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-022"
    },
    {
      "previous_identity": "BD-16-023",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-023"
    },
    {
      "previous_identity": "BD-16-024",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-024"
    },
    {
      "previous_identity": "BD-16-025",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-025"
    },
    {
      "previous_identity": "BD-16-026",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-026"
    },
    {
      "previous_identity": "BD-16-027",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-027"
    },
    {
      "previous_identity": "BD-16-028",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-028"
    },
    {
      "previous_identity": "BD-16-029",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-029"
    },
    {
      "previous_identity": "BD-16-030",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "BD-16-030"
    },
    {
      "previous_identity": "BD-17-001",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-001"
    },
    {
      "previous_identity": "BD-17-002",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-002"
    },
    {
      "previous_identity": "BD-17-003",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-003"
    },
    {
      "previous_identity": "BD-17-004",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-004"
    },
    {
      "previous_identity": "BD-17-005",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-005"
    },
    {
      "previous_identity": "BD-17-006",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-006"
    },
    {
      "previous_identity": "BD-17-007",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-007"
    },
    {
      "previous_identity": "BD-17-008",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-008"
    },
    {
      "previous_identity": "BD-17-009",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-009"
    },
    {
      "previous_identity": "BD-17-010",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-010"
    },
    {
      "previous_identity": "BD-17-011",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-011"
    },
    {
      "previous_identity": "BD-17-012",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-012"
    },
    {
      "previous_identity": "BD-17-013",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-013"
    },
    {
      "previous_identity": "BD-17-014",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-014"
    },
    {
      "previous_identity": "BD-17-015",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-015"
    },
    {
      "previous_identity": "BD-17-016",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-016"
    },
    {
      "previous_identity": "BD-17-017",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-017"
    },
    {
      "previous_identity": "BD-17-018",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-018"
    },
    {
      "previous_identity": "BD-17-019",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-019"
    },
    {
      "previous_identity": "BD-17-020",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-020"
    },
    {
      "previous_identity": "BD-17-021",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-021"
    },
    {
      "previous_identity": "BD-17-022",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-022"
    },
    {
      "previous_identity": "BD-17-023",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-023"
    },
    {
      "previous_identity": "BD-17-024",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-024"
    },
    {
      "previous_identity": "BD-17-025",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-025"
    },
    {
      "previous_identity": "BD-17-026",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-026"
    },
    {
      "previous_identity": "BD-17-027",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-027"
    },
    {
      "previous_identity": "BD-17-028",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-028"
    },
    {
      "previous_identity": "BD-17-029",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-029"
    },
    {
      "previous_identity": "BD-17-030",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-030"
    },
    {
      "previous_identity": "BD-17-031",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-031"
    },
    {
      "previous_identity": "BD-17-032",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "BD-17-032"
    },
    {
      "previous_identity": "BO-EP-001",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-EP-001"
    },
    {
      "previous_identity": "BO-EP-002",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-EP-002"
    },
    {
      "previous_identity": "BO-EP-003",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-EP-003"
    },
    {
      "previous_identity": "BO-EP-004",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-EP-004"
    },
    {
      "previous_identity": "BO-EP-005",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-EP-005"
    },
    {
      "previous_identity": "BO-EP-006",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-EP-006"
    },
    {
      "previous_identity": "BO-EP-007",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-EP-007"
    },
    {
      "previous_identity": "BO-EP-008",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-EP-008"
    },
    {
      "previous_identity": "BO-EP-009",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-EP-009"
    },
    {
      "previous_identity": "BO-EP-010",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-EP-010"
    },
    {
      "previous_identity": "BO-P01",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-P01"
    },
    {
      "previous_identity": "BO-P02",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-P02"
    },
    {
      "previous_identity": "BO-P03",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-P03"
    },
    {
      "previous_identity": "BO-P04",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-P04"
    },
    {
      "previous_identity": "BO-P05",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-P05"
    },
    {
      "previous_identity": "BO-P06",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-P06"
    },
    {
      "previous_identity": "BO-P07",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-P07"
    },
    {
      "previous_identity": "BO-R01",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-R01"
    },
    {
      "previous_identity": "BO-R02",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-R02"
    },
    {
      "previous_identity": "BO-R03",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-R03"
    },
    {
      "previous_identity": "BO-R04",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-R04"
    },
    {
      "previous_identity": "BO-R05",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-R05"
    },
    {
      "previous_identity": "BO-R06",
      "source_document": "docs/BRD/BRD-BO-INDEX.md",
      "stable_id": "BO-R06"
    },
    {
      "previous_identity": "CAP-EP-001",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-EP-001"
    },
    {
      "previous_identity": "CAP-EP-002",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-EP-002"
    },
    {
      "previous_identity": "CAP-EP-003",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-EP-003"
    },
    {
      "previous_identity": "CAP-EP-004",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-EP-004"
    },
    {
      "previous_identity": "CAP-EP-005",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-EP-005"
    },
    {
      "previous_identity": "CAP-EP-006",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-EP-006"
    },
    {
      "previous_identity": "CAP-EP-007",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-EP-007"
    },
    {
      "previous_identity": "CAP-EP-008",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-EP-008"
    },
    {
      "previous_identity": "CAP-EP-009",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-EP-009"
    },
    {
      "previous_identity": "CAP-EP-010",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-EP-010"
    },
    {
      "previous_identity": "CAP-P01",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-P01"
    },
    {
      "previous_identity": "CAP-P02",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-P02"
    },
    {
      "previous_identity": "CAP-P03",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-P03"
    },
    {
      "previous_identity": "CAP-P04",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-P04"
    },
    {
      "previous_identity": "CAP-P05",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-P05"
    },
    {
      "previous_identity": "CAP-P06",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-P06"
    },
    {
      "previous_identity": "CAP-P07",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-P07"
    },
    {
      "previous_identity": "CAP-P08",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-P08"
    },
    {
      "previous_identity": "CAP-R01",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-R01"
    },
    {
      "previous_identity": "CAP-R02",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-R02"
    },
    {
      "previous_identity": "CAP-R03",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-R03"
    },
    {
      "previous_identity": "CAP-R04",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-R04"
    },
    {
      "previous_identity": "CAP-R05",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-R05"
    },
    {
      "previous_identity": "CAP-R06",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-R06"
    },
    {
      "previous_identity": "CAP-R07",
      "source_document": "docs/BRD/BRD-CAP-INDEX.md",
      "stable_id": "CAP-R07"
    },
    {
      "previous_identity": "EP-06-001",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "EP-06-001"
    },
    {
      "previous_identity": "EP-06-002",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "EP-06-002"
    },
    {
      "previous_identity": "EP-06-003",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "EP-06-003"
    },
    {
      "previous_identity": "EP-06-004",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "EP-06-004"
    },
    {
      "previous_identity": "EP-06-005",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "EP-06-005"
    },
    {
      "previous_identity": "EP-06-006",
      "source_document": "docs/BRD/BRD-WS-06.md",
      "stable_id": "EP-06-006"
    },
    {
      "previous_identity": "EP-07-001",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "EP-07-001"
    },
    {
      "previous_identity": "EP-07-002",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "EP-07-002"
    },
    {
      "previous_identity": "EP-07-003",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "EP-07-003"
    },
    {
      "previous_identity": "EP-07-004",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "EP-07-004"
    },
    {
      "previous_identity": "EP-07-005",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "EP-07-005"
    },
    {
      "previous_identity": "EP-07-006",
      "source_document": "docs/BRD/BRD-WS-07.md",
      "stable_id": "EP-07-006"
    },
    {
      "previous_identity": "EP-08-001",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "EP-08-001"
    },
    {
      "previous_identity": "EP-08-002",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "EP-08-002"
    },
    {
      "previous_identity": "EP-08-003",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "EP-08-003"
    },
    {
      "previous_identity": "EP-08-004",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "EP-08-004"
    },
    {
      "previous_identity": "EP-08-005",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "EP-08-005"
    },
    {
      "previous_identity": "EP-08-006",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "EP-08-006"
    },
    {
      "previous_identity": "EP-08-007",
      "source_document": "docs/BRD/BRD-WS-08.md",
      "stable_id": "EP-08-007"
    },
    {
      "previous_identity": "EP-09-001",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "EP-09-001"
    },
    {
      "previous_identity": "EP-09-002",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "EP-09-002"
    },
    {
      "previous_identity": "EP-09-003",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "EP-09-003"
    },
    {
      "previous_identity": "EP-09-004",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "EP-09-004"
    },
    {
      "previous_identity": "EP-09-005",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "EP-09-005"
    },
    {
      "previous_identity": "EP-09-006",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "EP-09-006"
    },
    {
      "previous_identity": "EP-09-007",
      "source_document": "docs/BRD/BRD-WS-09.md",
      "stable_id": "EP-09-007"
    },
    {
      "previous_identity": "EP-10-001",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "EP-10-001"
    },
    {
      "previous_identity": "EP-10-002",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "EP-10-002"
    },
    {
      "previous_identity": "EP-10-003",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "EP-10-003"
    },
    {
      "previous_identity": "EP-10-004",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "EP-10-004"
    },
    {
      "previous_identity": "EP-10-005",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "EP-10-005"
    },
    {
      "previous_identity": "EP-10-006",
      "source_document": "docs/BRD/BRD-WS-10.md",
      "stable_id": "EP-10-006"
    },
    {
      "previous_identity": "EP-11-001",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "EP-11-001"
    },
    {
      "previous_identity": "EP-11-002",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "EP-11-002"
    },
    {
      "previous_identity": "EP-11-003",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "EP-11-003"
    },
    {
      "previous_identity": "EP-11-004",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "EP-11-004"
    },
    {
      "previous_identity": "EP-11-005",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "EP-11-005"
    },
    {
      "previous_identity": "EP-11-006",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "EP-11-006"
    },
    {
      "previous_identity": "EP-11-007",
      "source_document": "docs/BRD/BRD-WS-11.md",
      "stable_id": "EP-11-007"
    },
    {
      "previous_identity": "EP-12-001",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "EP-12-001"
    },
    {
      "previous_identity": "EP-12-002",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "EP-12-002"
    },
    {
      "previous_identity": "EP-12-003",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "EP-12-003"
    },
    {
      "previous_identity": "EP-12-004",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "EP-12-004"
    },
    {
      "previous_identity": "EP-12-005",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "EP-12-005"
    },
    {
      "previous_identity": "EP-12-006",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "EP-12-006"
    },
    {
      "previous_identity": "EP-12-007",
      "source_document": "docs/BRD/BRD-WS-12.md",
      "stable_id": "EP-12-007"
    },
    {
      "previous_identity": "EP-13-001",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "EP-13-001"
    },
    {
      "previous_identity": "EP-13-002",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "EP-13-002"
    },
    {
      "previous_identity": "EP-13-003",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "EP-13-003"
    },
    {
      "previous_identity": "EP-13-004",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "EP-13-004"
    },
    {
      "previous_identity": "EP-13-005",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "EP-13-005"
    },
    {
      "previous_identity": "EP-13-006",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "EP-13-006"
    },
    {
      "previous_identity": "EP-13-007",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "EP-13-007"
    },
    {
      "previous_identity": "EP-13-008",
      "source_document": "docs/BRD/BRD-WS-13.md",
      "stable_id": "EP-13-008"
    },
    {
      "previous_identity": "EP-14-001",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "EP-14-001"
    },
    {
      "previous_identity": "EP-14-002",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "EP-14-002"
    },
    {
      "previous_identity": "EP-14-003",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "EP-14-003"
    },
    {
      "previous_identity": "EP-14-004",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "EP-14-004"
    },
    {
      "previous_identity": "EP-14-005",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "EP-14-005"
    },
    {
      "previous_identity": "EP-14-006",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "EP-14-006"
    },
    {
      "previous_identity": "EP-14-007",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "EP-14-007"
    },
    {
      "previous_identity": "EP-14-008",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "EP-14-008"
    },
    {
      "previous_identity": "EP-14-009",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "EP-14-009"
    },
    {
      "previous_identity": "EP-14-010",
      "source_document": "docs/BRD/BRD-WS-14.md",
      "stable_id": "EP-14-010"
    },
    {
      "previous_identity": "EP-15-001",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "EP-15-001"
    },
    {
      "previous_identity": "EP-15-002",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "EP-15-002"
    },
    {
      "previous_identity": "EP-15-003",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "EP-15-003"
    },
    {
      "previous_identity": "EP-15-004",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "EP-15-004"
    },
    {
      "previous_identity": "EP-15-005",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "EP-15-005"
    },
    {
      "previous_identity": "EP-15-006",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "EP-15-006"
    },
    {
      "previous_identity": "EP-15-007",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "EP-15-007"
    },
    {
      "previous_identity": "EP-15-008",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "EP-15-008"
    },
    {
      "previous_identity": "EP-15-009",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "EP-15-009"
    },
    {
      "previous_identity": "EP-15-010",
      "source_document": "docs/BRD/BRD-WS-15.md",
      "stable_id": "EP-15-010"
    },
    {
      "previous_identity": "EP-16-001",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "EP-16-001"
    },
    {
      "previous_identity": "EP-16-002",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "EP-16-002"
    },
    {
      "previous_identity": "EP-16-003",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "EP-16-003"
    },
    {
      "previous_identity": "EP-16-004",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "EP-16-004"
    },
    {
      "previous_identity": "EP-16-005",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "EP-16-005"
    },
    {
      "previous_identity": "EP-16-006",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "EP-16-006"
    },
    {
      "previous_identity": "EP-16-007",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "EP-16-007"
    },
    {
      "previous_identity": "EP-16-008",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "EP-16-008"
    },
    {
      "previous_identity": "EP-16-009",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "EP-16-009"
    },
    {
      "previous_identity": "EP-16-010",
      "source_document": "docs/BRD/BRD-WS-16.md",
      "stable_id": "EP-16-010"
    },
    {
      "previous_identity": "EP-17-001",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "EP-17-001"
    },
    {
      "previous_identity": "EP-17-002",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "EP-17-002"
    },
    {
      "previous_identity": "EP-17-003",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "EP-17-003"
    },
    {
      "previous_identity": "EP-17-004",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "EP-17-004"
    },
    {
      "previous_identity": "EP-17-005",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "EP-17-005"
    },
    {
      "previous_identity": "EP-17-006",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "EP-17-006"
    },
    {
      "previous_identity": "EP-17-007",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "EP-17-007"
    },
    {
      "previous_identity": "EP-17-008",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "EP-17-008"
    },
    {
      "previous_identity": "EP-17-009",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "EP-17-009"
    },
    {
      "previous_identity": "EP-17-010",
      "source_document": "docs/BRD/BRD-WS-17.md",
      "stable_id": "EP-17-010"
    },
    {
      "previous_identity": "EVT-C01",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-C01"
    },
    {
      "previous_identity": "EVT-C02",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-C02"
    },
    {
      "previous_identity": "EVT-C03",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-C03"
    },
    {
      "previous_identity": "EVT-C04",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-C04"
    },
    {
      "previous_identity": "EVT-C05",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-C05"
    },
    {
      "previous_identity": "EVT-C06",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-C06"
    },
    {
      "previous_identity": "EVT-EP-001",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-EP-001"
    },
    {
      "previous_identity": "EVT-EP-002",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-EP-002"
    },
    {
      "previous_identity": "EVT-EP-003",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-EP-003"
    },
    {
      "previous_identity": "EVT-EP-004",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-EP-004"
    },
    {
      "previous_identity": "EVT-EP-005",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-EP-005"
    },
    {
      "previous_identity": "EVT-EP-006",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-EP-006"
    },
    {
      "previous_identity": "EVT-EP-007",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-EP-007"
    },
    {
      "previous_identity": "EVT-EP-008",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-EP-008"
    },
    {
      "previous_identity": "EVT-EP-009",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-EP-009"
    },
    {
      "previous_identity": "EVT-EP-010",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-EP-010"
    },
    {
      "previous_identity": "EVT-P01",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-P01"
    },
    {
      "previous_identity": "EVT-P02",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-P02"
    },
    {
      "previous_identity": "EVT-P03",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-P03"
    },
    {
      "previous_identity": "EVT-P04",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-P04"
    },
    {
      "previous_identity": "EVT-P05",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-P05"
    },
    {
      "previous_identity": "EVT-P06",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-P06"
    },
    {
      "previous_identity": "EVT-P07",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-P07"
    },
    {
      "previous_identity": "EVT-P08",
      "source_document": "docs/BRD/BRD-EVENT-INDEX.md",
      "stable_id": "EVT-P08"
    },
    {
      "previous_identity": "POL-EP-001",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-EP-001"
    },
    {
      "previous_identity": "POL-EP-002",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-EP-002"
    },
    {
      "previous_identity": "POL-EP-003",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-EP-003"
    },
    {
      "previous_identity": "POL-EP-004",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-EP-004"
    },
    {
      "previous_identity": "POL-EP-005",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-EP-005"
    },
    {
      "previous_identity": "POL-EP-006",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-EP-006"
    },
    {
      "previous_identity": "POL-EP-007",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-EP-007"
    },
    {
      "previous_identity": "POL-EP-008",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-EP-008"
    },
    {
      "previous_identity": "POL-EP-009",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-EP-009"
    },
    {
      "previous_identity": "POL-EP-010",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-EP-010"
    },
    {
      "previous_identity": "POL-P01",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-P01"
    },
    {
      "previous_identity": "POL-P02",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-P02"
    },
    {
      "previous_identity": "POL-P03",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-P03"
    },
    {
      "previous_identity": "POL-P04",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-P04"
    },
    {
      "previous_identity": "POL-P05",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-P05"
    },
    {
      "previous_identity": "POL-P06",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-P06"
    },
    {
      "previous_identity": "POL-P07",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-P07"
    },
    {
      "previous_identity": "POL-P08",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-P08"
    },
    {
      "previous_identity": "POL-P09",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-P09"
    },
    {
      "previous_identity": "POL-P10",
      "source_document": "docs/BRD/BRD-POLICY-INDEX.md",
      "stable_id": "POL-P10"
    },
    {
      "previous_identity": "SNP-EP-001",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-EP-001"
    },
    {
      "previous_identity": "SNP-EP-002",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-EP-002"
    },
    {
      "previous_identity": "SNP-EP-003",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-EP-003"
    },
    {
      "previous_identity": "SNP-EP-004",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-EP-004"
    },
    {
      "previous_identity": "SNP-EP-005",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-EP-005"
    },
    {
      "previous_identity": "SNP-EP-006",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-EP-006"
    },
    {
      "previous_identity": "SNP-EP-007",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-EP-007"
    },
    {
      "previous_identity": "SNP-EP-008",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-EP-008"
    },
    {
      "previous_identity": "SNP-EP-009",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-EP-009"
    },
    {
      "previous_identity": "SNP-EP-010",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-EP-010"
    },
    {
      "previous_identity": "SNP-P01",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-P01"
    },
    {
      "previous_identity": "SNP-P02",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-P02"
    },
    {
      "previous_identity": "SNP-P03",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-P03"
    },
    {
      "previous_identity": "SNP-P04",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-P04"
    },
    {
      "previous_identity": "SNP-P05",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-P05"
    },
    {
      "previous_identity": "SNP-P06",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-P06"
    },
    {
      "previous_identity": "SNP-P07",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-P07"
    },
    {
      "previous_identity": "SNP-P08",
      "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
      "stable_id": "SNP-P08"
    },
    {
      "previous_identity": "UXF-001",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-001"
    },
    {
      "previous_identity": "UXF-002",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-002"
    },
    {
      "previous_identity": "UXF-003",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-003"
    },
    {
      "previous_identity": "UXF-004",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-004"
    },
    {
      "previous_identity": "UXF-005",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-005"
    },
    {
      "previous_identity": "UXF-006",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-006"
    },
    {
      "previous_identity": "UXF-007",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-007"
    },
    {
      "previous_identity": "UXF-008",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-008"
    },
    {
      "previous_identity": "UXF-009",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-009"
    },
    {
      "previous_identity": "UXF-010",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-010"
    },
    {
      "previous_identity": "UXF-011",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-011"
    },
    {
      "previous_identity": "UXF-012",
      "source_document": "docs/UXF/UXF-00.md",
      "stable_id": "UXF-012"
    },
    {
      "previous_identity": "UXF-101",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-101"
    },
    {
      "previous_identity": "UXF-102",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-102"
    },
    {
      "previous_identity": "UXF-103",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-103"
    },
    {
      "previous_identity": "UXF-104",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-104"
    },
    {
      "previous_identity": "UXF-105",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-105"
    },
    {
      "previous_identity": "UXF-106",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-106"
    },
    {
      "previous_identity": "UXF-107",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-107"
    },
    {
      "previous_identity": "UXF-108",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-108"
    },
    {
      "previous_identity": "UXF-109",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-109"
    },
    {
      "previous_identity": "UXF-110",
      "source_document": "docs/UXF/UXF-01.md",
      "stable_id": "UXF-110"
    },
    {
      "previous_identity": "UXF-201",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-201"
    },
    {
      "previous_identity": "UXF-202",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-202"
    },
    {
      "previous_identity": "UXF-203",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-203"
    },
    {
      "previous_identity": "UXF-204",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-204"
    },
    {
      "previous_identity": "UXF-205",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-205"
    },
    {
      "previous_identity": "UXF-206",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-206"
    },
    {
      "previous_identity": "UXF-207",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-207"
    },
    {
      "previous_identity": "UXF-208",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-208"
    },
    {
      "previous_identity": "UXF-209",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-209"
    },
    {
      "previous_identity": "UXF-210",
      "source_document": "docs/UXF/UXF-02.md",
      "stable_id": "UXF-210"
    },
    {
      "previous_identity": "UXF-301",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-301"
    },
    {
      "previous_identity": "UXF-302",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-302"
    },
    {
      "previous_identity": "UXF-303",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-303"
    },
    {
      "previous_identity": "UXF-304",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-304"
    },
    {
      "previous_identity": "UXF-305",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-305"
    },
    {
      "previous_identity": "UXF-306",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-306"
    },
    {
      "previous_identity": "UXF-307",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-307"
    },
    {
      "previous_identity": "UXF-308",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-308"
    },
    {
      "previous_identity": "UXF-309",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-309"
    },
    {
      "previous_identity": "UXF-310",
      "source_document": "docs/UXF/UXF-03.md",
      "stable_id": "UXF-310"
    },
    {
      "previous_identity": "UXF-401",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-401"
    },
    {
      "previous_identity": "UXF-402",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-402"
    },
    {
      "previous_identity": "UXF-403",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-403"
    },
    {
      "previous_identity": "UXF-404",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-404"
    },
    {
      "previous_identity": "UXF-405",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-405"
    },
    {
      "previous_identity": "UXF-406",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-406"
    },
    {
      "previous_identity": "UXF-407",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-407"
    },
    {
      "previous_identity": "UXF-408",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-408"
    },
    {
      "previous_identity": "UXF-409",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-409"
    },
    {
      "previous_identity": "UXF-410",
      "source_document": "docs/UXF/UXF-04.md",
      "stable_id": "UXF-410"
    },
    {
      "previous_identity": "UXF-501",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-501"
    },
    {
      "previous_identity": "UXF-502",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-502"
    },
    {
      "previous_identity": "UXF-503",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-503"
    },
    {
      "previous_identity": "UXF-504",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-504"
    },
    {
      "previous_identity": "UXF-505",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-505"
    },
    {
      "previous_identity": "UXF-506",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-506"
    },
    {
      "previous_identity": "UXF-507",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-507"
    },
    {
      "previous_identity": "UXF-508",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-508"
    },
    {
      "previous_identity": "UXF-509",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-509"
    },
    {
      "previous_identity": "UXF-510",
      "source_document": "docs/UXF/UXF-05.md",
      "stable_id": "UXF-510"
    }
  ],
  "retired_key_count": 157,
  "retired_key_history": [
    "TMP-BRD-BO-INDEX-023",
    "TMP-BRD-CAP-INDEX-008",
    "TMP-BRD-EVENT-INDEX-015",
    "TMP-BRD-EVENT-INDEX-016",
    "TMP-BRD-EVENT-INDEX-017",
    "TMP-BRD-EVENT-INDEX-018",
    "TMP-BRD-EVENT-INDEX-019",
    "TMP-BRD-EVENT-INDEX-020",
    "TMP-BRD-EVENT-INDEX-021",
    "TMP-BRD-EVENT-INDEX-022",
    "TMP-BRD-EVENT-INDEX-023",
    "TMP-BRD-EVENT-INDEX-024",
    "TMP-BRD-META-MODEL-002",
    "TMP-BRD-POLICY-INDEX-010",
    "TMP-BRD-POLICY-INDEX-011",
    "TMP-BRD-POLICY-INDEX-012",
    "TMP-BRD-POLICY-INDEX-013",
    "TMP-BRD-POLICY-INDEX-014",
    "TMP-BRD-POLICY-INDEX-015",
    "TMP-BRD-POLICY-INDEX-016",
    "TMP-BRD-POLICY-INDEX-017",
    "TMP-BRD-POLICY-INDEX-018",
    "TMP-BRD-POLICY-INDEX-019",
    "TMP-BRD-SNAPSHOT-INDEX-011",
    "TMP-BRD-SNAPSHOT-INDEX-012",
    "TMP-BRD-SNAPSHOT-INDEX-013",
    "TMP-BRD-SNAPSHOT-INDEX-014",
    "TMP-BRD-SNAPSHOT-INDEX-015",
    "TMP-BRD-SNAPSHOT-INDEX-016",
    "TMP-BRD-SNAPSHOT-INDEX-017",
    "TMP-BRD-SNAPSHOT-INDEX-018",
    "TMP-BRD-SNAPSHOT-INDEX-019",
    "TMP-BRD-SNAPSHOT-INDEX-020",
    "TMP-BRD-SNAPSHOT-INDEX-021",
    "TMP-BRD-WS-01-037",
    "TMP-BRD-WS-01-038",
    "TMP-BRD-WS-01-039",
    "TMP-BRD-WS-01-040",
    "TMP-BRD-WS-01-041",
    "TMP-BRD-WS-02-001",
    "TMP-BRD-WS-03-001",
    "TMP-BRD-WS-05-010",
    "TMP-BRD-WS-06-029",
    "TMP-BRD-WS-07-002",
    "TMP-BRD-WS-08-001",
    "TMP-BRD-WS-08-009",
    "TMP-BRD-WS-09-002",
    "TMP-BRD-WS-10-005",
    "TMP-BRD-WS-10-006",
    "TMP-BRD-WS-12-001",
    "TMP-BRD-WS-14-002",
    "TMP-BRD-WS-14-027",
    "TMP-BRD-WS-15-001",
    "TMP-BRD-WS-15-002",
    "TMP-BRD-WS-15-027",
    "TMP-BRD-WS-16-009",
    "TMP-BRD-WS-17-005",
    "TMP-UXF-00-032",
    "TMP-UXF-00-033",
    "TMP-UXF-00-034",
    "TMP-UXF-00-035",
    "TMP-UXF-00-036",
    "TMP-UXF-00-037",
    "TMP-UXF-00-038",
    "TMP-UXF-00-039",
    "TMP-UXF-00-040",
    "TMP-UXF-00-041",
    "TMP-UXF-01-012",
    "TMP-UXF-01-013",
    "TMP-UXF-01-014",
    "TMP-UXF-01-015",
    "TMP-UXF-01-016",
    "TMP-UXF-01-017",
    "TMP-UXF-01-018",
    "TMP-UXF-01-019",
    "TMP-UXF-01-020",
    "TMP-UXF-01-021",
    "TMP-UXF-02-010",
    "TMP-UXF-02-011",
    "TMP-UXF-02-012",
    "TMP-UXF-02-013",
    "TMP-UXF-02-014",
    "TMP-UXF-02-015",
    "TMP-UXF-02-016",
    "TMP-UXF-02-017",
    "TMP-UXF-02-018",
    "TMP-UXF-02-019",
    "TMP-UXF-02-020",
    "TMP-UXF-02-021",
    "TMP-UXF-02-022",
    "TMP-UXF-02-023",
    "TMP-UXF-02-024",
    "TMP-UXF-02-025",
    "TMP-UXF-02-026",
    "TMP-UXF-02-027",
    "TMP-UXF-02-028",
    "TMP-UXF-02-029",
    "TMP-UXF-03-008",
    "TMP-UXF-03-009",
    "TMP-UXF-03-010",
    "TMP-UXF-03-011",
    "TMP-UXF-03-012",
    "TMP-UXF-03-013",
    "TMP-UXF-03-014",
    "TMP-UXF-03-015",
    "TMP-UXF-03-016",
    "TMP-UXF-03-017",
    "TMP-UXF-03-018",
    "TMP-UXF-03-019",
    "TMP-UXF-03-020",
    "TMP-UXF-03-021",
    "TMP-UXF-03-022",
    "TMP-UXF-03-023",
    "TMP-UXF-03-024",
    "TMP-UXF-03-025",
    "TMP-UXF-03-026",
    "TMP-UXF-04-015",
    "TMP-UXF-04-016",
    "TMP-UXF-04-017",
    "TMP-UXF-04-018",
    "TMP-UXF-04-019",
    "TMP-UXF-04-020",
    "TMP-UXF-04-021",
    "TMP-UXF-04-022",
    "TMP-UXF-04-023",
    "TMP-UXF-04-024",
    "TMP-UXF-04-025",
    "TMP-UXF-04-026",
    "TMP-UXF-04-027",
    "TMP-UXF-04-028",
    "TMP-UXF-04-029",
    "TMP-UXF-04-030",
    "TMP-UXF-04-031",
    "TMP-UXF-04-032",
    "TMP-UXF-04-033",
    "TMP-UXF-05-013",
    "TMP-UXF-05-023",
    "TMP-UXF-05-024",
    "TMP-UXF-05-025",
    "TMP-UXF-05-026",
    "TMP-UXF-05-027",
    "TMP-UXF-05-028",
    "TMP-UXF-05-029",
    "TMP-UXF-05-030",
    "TMP-UXF-05-031",
    "TMP-UXF-05-032",
    "TMP-UXF-05-043",
    "TMP-UXF-05-044",
    "TMP-UXF-05-045",
    "TMP-UXF-05-046",
    "TMP-UXF-05-047",
    "TMP-UXF-05-048",
    "TMP-UXF-05-049",
    "TMP-UXF-05-050",
    "TMP-UXF-05-051",
    "TMP-UXF-05-052",
    "TMP-UXF-05-053"
  ],
  "reuse_policy": "NEVER_REUSE_RETIRED_IDS_OR_KEYS"
}

```

<!-- YSIM:IDENTITY HISTORY END -->

<!-- YSIM:PHASE_2C CANONICAL APPENDIX END -->
