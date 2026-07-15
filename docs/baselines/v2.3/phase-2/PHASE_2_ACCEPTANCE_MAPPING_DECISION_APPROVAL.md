# Phase 2C Acceptance Mapping Decision Approval

- Candidate: `V23-P2C-ACCEPTANCE-MAPPING-C3`
- Candidate commit: `f4f4a5e8a3dba1fb1cadc3e3daa3881dbbc6ba39`
- Candidate parent / accepted Acceptance Model commit: `a989367a6f69f1a03a8269562ce43bda3968b71a`
- Decision: `APPROVED`
- Approval scope: `ACCEPTANCE_MAPPING_DECISIONS_AND_REMEDIATION_ROUTES_ONLY`
- Authorized Approver: `Khoa, Nguyen`
- Signature: `Khoa, Nguyen`
- Approval date: `2026-07-15`
- Timezone: `Asia/Ho_Chi_Minh`

## Selected OPT-1

- `P2C-AC-C3-DEC-005-OPT-1`
- `P2C-AC-C3-DEC-023-OPT-1`
- `P2C-AC-C3-DEC-027-OPT-1`
- `P2C-AC-C3-DEC-030-OPT-1`
- `P2C-AC-C3-DEC-PREFULFILLMENT-OPT-1`

## Selected OPT-3

- `P2C-AC-C3-DEC-001-OPT-3`
- `P2C-AC-C3-DEC-002-OPT-3`
- `P2C-AC-C3-DEC-003-OPT-3`
- `P2C-AC-C3-DEC-009-OPT-3`
- `P2C-AC-C3-DEC-010-OPT-3`
- `P2C-AC-C3-DEC-011-OPT-3`
- `P2C-AC-C3-DEC-018-OPT-3`
- `P2C-AC-C3-DEC-019-OPT-3`
- `P2C-AC-C3-DEC-029-OPT-3`
- `P2C-AC-C3-DEC-031-OPT-3`
- `P2C-AC-C3-DEC-032-OPT-3`
- `P2C-AC-C3-DEC-034-OPT-3`
- `P2C-AC-C3-DEC-035-OPT-3`
- `P2C-AC-C3-DEC-036-OPT-3`

## Semantic directives

### 1. Touch and responsive experience

UXF-01-R010, UXF-01-R008 và UXF-01-R011 phải được chuẩn hóa thành nghĩa vụ bắt buộc đối với mọi V2.3_ACTIVE experience channel trên supported browser, mobile và WebView.

Không được có thao tác chỉ hoạt động bằng hover. Layout, navigation, action và critical workflow phải usable trên touch-capable supported devices.

Partner Portal chưa triển khai không bị đưa vào active implementation scope.

### 2. KPI Definition

BD-13-003 phải được tách thành:

- các KPI groups và measurement standards bắt buộc của v2.3;
- KPI Definition được cấu hình;
- khả năng mở rộng thêm KPI/measurement standards bằng governed configuration.

Không dùng một compound acceptance contract cho cả ba nghĩa vụ.

### 3. Identity Providers

BD-16-001 phải phân biệt:

- active v2.3 provider set: Local Account, Google, Apple, Facebook, Microsoft, Line và WeChat;
- future provider extension point.

Active provider set là nghĩa vụ triển khai. Future extension không được tính là active provider implementation nhưng kiến trúc connector/provider phải mở rộng được mà không thay đổi Identity Domain business logic.

### 4. Commerce First

BRD-UPDATE-01-R020 là principle/composite non-unit.

Không có implementation, acceptance, scope-coverage hoặc criticality unit trực tiếp. Coverage phải được suy ra từ các commerce capability và experience requirements cụ thể.

### 5. Authorization future extensibility

BRD-WS-16-R002 không được biến future complex authorization models thành active v2.3 feature.

Phải tách:

- authorization/permission model thực sự active trong v2.3;
- advanced future authorization extensibility ở FUTURE/NOT_APPLICABLE_FOR_V2.3.

### 6. Communication channel extensibility

EP-12-006 phải được chuẩn hóa thành active architecture boundary:

Communication Channel/Adapter mới có thể được bổ sung mà không sửa domain business logic.

Channel connector vẫn phải tuân theo governed configuration, credential, approval, security, retry và audit contracts.

### 7. Communication performance

EP-12-007 phải tham chiếu các approved service-tier, performance-budget, SLO và channel-delivery requirements.

Không chấp nhận câu chung “mở rộng Performance” làm acceptance criterion.

Message Queue và Channel Adapter phải hỗ trợ capacity scaling, backpressure, observable delivery và failure isolation theo service tier.

### 8. Customer Portal

BD-03-004 phải được thay thế nghĩa “Storefront mở rộng” bằng quyết định đã phê duyệt:

- Customer Portal là experience channel độc lập;
- có stable shell;
- organization/storefront scoped;
- không có YSim global consolidated portal;
- sử dụng một default Storefront và giữ originating Storefront context;
- có Dashboard widgets và commerce menu;
- Storefront vẫn là channel thực hiện bán hàng.

### 9. Multi-tenant

BRD-UPDATE-01-R024 là principle/composite non-unit.

Coverage phải được delegated tới Organization isolation, identity/user context, data access, configuration, branding, audit và tenant-boundary requirements cụ thể.

Không dùng câu “Multi-tenant” đơn lẻ làm acceptance unit.

### 10. Experience First

BRD-UPDATE-01-R029 là active design-boundary requirement:

Commerce Experience phải ưu tiên UX trong presentation/composition decisions nhưng không được thay đổi canonical business behavior, pricing, policy, authorization, payment, allocation hoặc fulfillment semantics.

### 11. Customer Identity ownership

BRD-WS-11-R002 phải được chuẩn hóa:

Customer Identity là canonical identity record do YSim Platform quản lý.

Điều này không có nghĩa YSim sở hữu pháp lý dữ liệu cá nhân. Organization chỉ truy cập và quản lý dữ liệu trong phạm vi relationship, consent, purpose, policy và jurisdiction được phép.

### 12. Organization Relationship rights

BRD-WS-11-R003 là active strong boundary:

Organization chỉ quản lý Organization-scoped Customer Relationship và các dữ liệu/quyền được cấp trong relationship đó.

Organization không được chiếm quyền sở hữu, hợp nhất hoặc sửa canonical Customer Identity ngoài policy được phép.

### 13. Gateway extensibility

BRD-WS-15-R004 phải được chuẩn hóa thành governed integration-extension contract.

Gateway mới chỉ được bổ sung khi có approved integration requirement và phải đi qua connector/gateway lifecycle, credential governance, security review, observability và audit.

Business logic không được đặt trong Gateway.

### 14. Configuration over hard-code

CAP-P04 là canonical requirement.

CAP-EP-005 phải được reconcile thành alias hoặc supporting principle của CAP-P04, không phải acceptance unit trùng lặp.

Phải cấu hình khi behavior thay đổi theo organization, market, channel, jurisdiction, policy hoặc environment. Platform invariants và security invariants có thể được thực thi trong code nhưng phải versioned và auditable.

### 15. Runtime rendering fallback

UXF-05-R022 và UXF-00-R013 phải tuân theo quyết định:

- UX/presentation thiếu hoặc không hợp lệ: dùng safe fallback và tiếp tục render khi có thể;
- business-critical configuration thiếu hoặc không hợp lệ: fail-closed;
- không được tiếp tục checkout, payment, allocation, fulfillment, authorization hoặc security flow bằng inferred unsafe defaults;
- failure phải observable và cung cấp actionable recovery information.

### 16. Pre-Fulfillment Commercial Validation

Chọn comprehensive commercial eligibility:

- pricing validity;
- minimum-margin/cost policy;
- supplier commercial terms;
- required approvals;
- inventory availability hoặc procurement feasibility;
- ability to fulfill toàn bộ order theo no-partial policy của v2.3.

Procurement Validation vẫn là sub-obligation riêng.

Khi có allocatable stock, reservation path được sử dụng.

Khi không có item phù hợp và cần procurement, procurement feasibility phải được xác nhận trước khi bắt đầu payment.

Commercial/procurement validation failure phải block payment initiation.

Không được thu tiền nếu chưa chứng minh được order có commercial eligibility và khả năng procurement/fulfillment theo policy hiện hành.

## Signed hashes

- Generated Payload Aggregate: `09127e4ead4ab143953d47004d71dc85027e3976c5921f22899037f92aab6df9`
- Staged Git-content Aggregate: `626a53c67b83cd34310d53b0c3f75747ad000b9a5184f70f6d3e16af359798c3`
- Mapping: `9f1e1a62ff16149b7c1af849590db07d7cb87847f523a5c5b4d2bf06d6a145a8`
- Manifest: `7f00d4171abe59039e6099c16d311e8953de92b7b091389dd8a4e5450b5e83f6`
- Verification Shapes: `080cbd2f9f2e744ec88beef5a08a1f6cea107fcb5519436911c04acf2bfdcd61`
- Clusters: `c0d16237bbc102549ea19fd17ade90885209b86e306cc1797d32698f2a7ad8d5`
- Decisions: `d9bd1c409e91fe222c042ecc829b127812876b60e3267e93182f4e65d9843fcd`
- Inline Archetype Catalog: `e5d729d4966d60e4fd25c622e30ba10d8371cdd02d9a9ce4ad4528c7ca2d61c0`
- Source Normalization Plan: `4520b87782b7c259692871608903d78b261a7fd76eaf1ef32927f0b451dfd85a`
- Structural Reconciliation Plan: `4c7960738e2c6754f21280d767da435e1bc166ef3c065a08787eb0cef5e48c3c`

## Approval non-claims

- This approval approves 19 decision selections and the 16 semantic directives.
- This approval approves remediation routes only within `ACCEPTANCE_MAPPING_DECISIONS_AND_REMEDIATION_ROUTES_ONLY`.
- `NOT_APPROVAL_OF_C1_C2_ACCEPTANCE_CONTRACTS`
- `NOT_APPROVAL_OF_MATERIALIZED_SOURCE_ACCEPTANCE_CONTRACTS`
- `NOT_FINAL_BRD_UXF_DOCUMENT_BASELINE_APPROVAL`
- `NOT_YADF_IMPLEMENTATION_AUTHORIZATION`
- `NOT_AUTHORIZATION_TO_SKIP_CLEAN_CHECKOUT_OR_HUMAN_SEMANTIC_SAMPLING`

## Validator Applicability Matrix

### A. HISTORICAL_REGISTRY_AND_PHASE_2_VALIDATORS

Run only at `0df2d424e00f9cd27b8dcb6645eef827ce97b60e`.

### B. ACCEPTED_ACCEPTANCE_MODEL_VALIDATORS

Run only at `a989367a6f69f1a03a8269562ce43bda3968b71a`.

### C. C3 PRE-COMMIT/INDEX VALIDATORS

Run with HEAD `a989367a6f69f1a03a8269562ce43bda3968b71a`, exactly 32 staged C3 files, candidate-equivalent staged tree, and no approval layer.

### D. C3 COMMITTED CANDIDATE VERIFICATION

Verify `f4f4a5e8a3dba1fb1cadc3e3daa3881dbbc6ba39` through ancestry, Git tree, signed blobs and aggregates, candidate state, inventory, clean status, and absence of approval files. Do not execute index-mode validators on the descendant HEAD.

### E. C3 ACCEPTED DECISION VERIFICATION

Verify the accepted descendant through this detached approval validator, direct-parent ancestry, signed candidate Git objects, and the exact two-file approval diff. Do not execute historical or index-mode validators on the accepted descendant HEAD.
