# Semantic Oracle Model C2 Review Pack

- Candidate: `V23-P2C-SEMANTIC-ORACLE-MODEL-C2`
- Operator suites: `40/40`
- Active mappings: `1152`
- Human mapping decisions: `27` (all PENDING)
- Retained reference contracts: `13`
- References reclassified to review: `3`

## Honest coverage

```json
{
  "active_atomic": 1152,
  "canonical_atomic": 1263,
  "criticality_by_disposition": {
    "CUSTOM_AST_REQUIRED": {
      "CRITICAL": 21,
      "HIGH": 19,
      "NORMAL": 19
    },
    "HUMAN_OPERATOR_MAPPING_REVIEW": {
      "CRITICAL": 5,
      "HIGH": 16,
      "NORMAL": 6
    },
    "HUMAN_PROCEDURE_REQUIRED": {
      "CRITICAL": 44,
      "HIGH": 86,
      "NORMAL": 26
    },
    "MODEL_EXECUTABLE_RUNTIME_ADAPTER_PENDING": {
      "CRITICAL": 270,
      "HIGH": 318,
      "NORMAL": 322
    }
  },
  "dispositions": {
    "CUSTOM_AST_REQUIRED": 59,
    "HUMAN_OPERATOR_MAPPING_REVIEW": 27,
    "HUMAN_PROCEDURE_REQUIRED": 156,
    "MODEL_EXECUTABLE_RUNTIME_ADAPTER_PENDING": 910
  },
  "fully_model_executable": 0,
  "inactive_atomic": 111,
  "missing_disposition": 0,
  "registry_records": 1326,
  "reusable_high_risk_subset_of_custom": 48
}
```

## Reference digest

### pre-fulfillment-commercial-gate

- Requirement: `BRD-WS-05-R021`
- Status: `RETAINED_EXECUTABLE`
- Operators: `POLICY_OUTCOME_EQUALS, APPROVAL_REQUIRED, PROCUREMENT_FEASIBLE, PAYMENT_INITIATION_ALLOWED, PAYMENT_INITIATION_BLOCKED`
- Executed mutations: `15`
- Statement: Trước payment initiation, Platform phải chứng minh toàn bộ order có commercial eligibility gồm pricing validity, minimum-margin/cost policy, supplier commercial terms, required approvals, inventory availability hoặc procurement feasibility, và khả năng fulfill toàn bộ order theo no-partial policy v2.3; khi có allocatable stock phải dùng reservation path, khi cần procurement phải xác nhận procurement feasibility, và mọi commercial/procurement validation failure phải block payment initiation.

### runtime-configuration-fallback

- Requirement: `UXF-00-R013`
- Status: `RETAINED_EXECUTABLE`
- Operators: `SAFE_FALLBACK_USED, FAIL_CLOSED`
- Executed mutations: `6`
- Statement: A missing or invalid business-critical configuration must fail closed: checkout, payment, allocation, fulfillment, authorization, and security flows must not continue with inferred unsafe defaults, and the failure must expose actionable recovery information.

### atomic-capability

- Requirement: `BRD-WS-01-R007`
- Status: `RETAINED_EXECUTABLE`
- Operators: `CAPABILITY_AVAILABLE, CAPABILITY_NOT_PLACEHOLDER, SCOPE_ACTIVE`
- Executed mutations: `9`
- Statement: Intelligent Allocation Engine is included in the active YSim v2.3 product scope.

### enum-reference-integrity

- Requirement: `BRD-CAP-INDEX-R029`
- Status: `RETAINED_EXECUTABLE`
- Operators: `ENUM_VALUE_ALLOWED, ROLE_LIST_CONSISTENT, REFERENCE_TARGET_VALID`
- Executed mutations: `9`
- Statement: Mỗi Capability phải khai báo event_role là PUBLISHER, SUBSCRIBER, BOTH hoặc NONE cùng published_event_ids và subscribed_event_ids; NONE yêu cầu hai danh sách rỗng, các role còn lại yêu cầu danh sách tương ứng không rỗng, và mọi tham chiếu phải trỏ tới Event Registry ID canonical active/approved, không được dùng alias, retired, tombstone hoặc dangling reference.

### mfa-enforcement

- Requirement: `BD-16-003`
- Status: `RETAINED_EXECUTABLE`
- Operators: `MFA_CHALLENGE_REQUIRED, ACTOR_DENIED, AUDIT_IMMUTABLE`
- Executed mutations: `9`
- Statement: Platform hỗ trợ Multi-Factor Authentication (MFA). MFA có thể áp dụng theo: - Platform - Organization - Role - User - API Client

### event-ordering-required

- Requirement: `BRD-EVENT-INDEX-R001`
- Status: `RETAINED_EXECUTABLE`
- Operators: `EVENT_ORDER_PRESERVED`
- Executed mutations: `3`
- Statement: Các event thuộc họ Payment, Settlement và Financial phải duy trì thứ tự xử lý.

### event-ordering-not-required

- Requirement: `BRD-EVENT-INDEX-R002`
- Status: `RETAINED_EXECUTABLE`
- Operators: `EVENT_ORDER_NOT_REQUIRED`
- Executed mutations: `3`
- Statement: Các event thuộc họ Marketing, Analytics và Notification không bắt buộc duy trì thứ tự xử lý.

### organization-relationship

- Requirement: `BRD-WS-11-R003`
- Status: `RETAINED_EXECUTABLE`
- Operators: `ACTOR_DENIED, TENANT_ISOLATED`
- Executed mutations: `6`
- Statement: Organization chỉ được quản lý Organization-scoped Customer Relationship và dữ liệu hoặc quyền được cấp trong relationship đó; Organization không được chiếm quyền sở hữu, hợp nhất hoặc sửa canonical Customer Identity ngoài policy được phép.

### tenant-isolation

- Requirement: `BRD-WS-03-R010`
- Status: `RETAINED_EXECUTABLE`
- Operators: `TENANT_ISOLATED, ACTOR_DENIED`
- Executed mutations: `6`
- Statement: Một Organization không được phép truy cập dữ liệu của Organization khác nếu không được phép theo Business Rule.

### state-transition

- Requirement: `BD-10-004`
- Status: `HUMAN_OPERATOR_MAPPING_REVIEW`
- Operators: `NONE`
- Executed mutations: `0`
- Statement: CommissionSnapshot phát sinh sau Payment Success và ở trạng thái Pending cho đến khi Settlement xác nhận.

### audit-immutability

- Requirement: `BD-14-016`
- Status: `RETAINED_EXECUTABLE`
- Operators: `AUDIT_IMMUTABLE, EVIDENCE_FIELD_PRESENT`
- Executed mutations: `6`
- Statement: Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version

### retry-limit

- Requirement: `BD-09-009`
- Status: `RETAINED_EXECUTABLE`
- Operators: `RETRY_LIMIT_NOT_EXCEEDED, DELIVERY_TERMINAL_STATE`
- Executed mutations: `6`
- Statement: Fulfillment Retry tối đa 3 lần.

### pricing-snapshot

- Requirement: `BD-02-007`
- Status: `RETAINED_EXECUTABLE`
- Operators: `POLICY_OUTCOME_EQUALS, EVIDENCE_FIELD_PRESENT`
- Executed mutations: `6`
- Statement: **Decision** Snapshot Pricing là nguyên tắc bắt buộc. **Rationale** Mọi Settlement và nghiệp vụ tài chính phải sử dụng giá tại thời điểm phát sinh giao dịch.

### settlement-reconciliation

- Requirement: `BD-10-004`
- Status: `HUMAN_OPERATOR_MAPPING_REVIEW`
- Operators: `NONE`
- Executed mutations: `0`
- Statement: CommissionSnapshot phát sinh sau Payment Success và ở trạng thái Pending cho đến khi Settlement xác nhận.

### accessibility

- Requirement: `UXF-02-R009`
- Status: `RETAINED_EXECUTABLE`
- Operators: `ACCESSIBILITY_CONFORMS`
- Executed mutations: `3`
- Statement: Accessibility cannot be disabled by Themes.

### performance-budget

- Requirement: `EP-12-007`
- Status: `HUMAN_OPERATOR_MAPPING_REVIEW`
- Operators: `NONE`
- Executed mutations: `0`
- Statement: Message Queue và Channel Adapter phải đáp ứng approved service tier, performance budget, SLO và channel-delivery contract, bao gồm capacity scaling, backpressure, observable delivery và failure isolation.
