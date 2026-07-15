# Acceptance Mapping Review Pack

- Candidate: `V23-P2C-ACCEPTANCE-MODEL-C1`
- Active atomic denominator: `1076`
- Stratified sample size: `902`
- Sample result: `PASS` (routing correctness only; profile/model approval remains pending)

## Disposition accounting

```json
{
  "HUMAN_MAPPING_REVIEW": 871,
  "INLINE_CONTRACT_REQUIRED": 161,
  "INVALID_OR_BLOCKED": 0,
  "PROFILE_BINDING_HIGH_CONFIDENCE": 44
}
```

## Profile mappings

```json
{
  "ACP-AUDITABILITY": 1,
  "ACP-AUTHENTICATION_REQUIREMENT": 3,
  "ACP-DATA_RETENTION": 1,
  "ACP-DESIGN_CONFORMANCE_TRACE": 1,
  "ACP-ENUM_REFERENCE_INTEGRITY": 1,
  "ACP-EVENT_ORDERING": 1,
  "ACP-MFA_ENFORCEMENT": 1,
  "ACP-OPERATION_OBSERVABILITY": 1,
  "ACP-REQUIRED_CAPABILITY_SET": 21,
  "ACP-ROLE_AND_PERMISSION_ENFORCEMENT": 3,
  "ACP-SCOPE_EXCLUSION": 4,
  "ACP-UX_ACCESSIBILITY": 6
}
```

## Inline categories

```json
{
  "ALLOCATION": 19,
  "COMPLEX_WORKFLOW": 9,
  "FINANCIAL_RECONCILIATION": 25,
  "FRAUD_RISK_DECISION": 3,
  "FULFILLMENT": 13,
  "PAYMENT": 56,
  "PRICING": 6,
  "PROCUREMENT": 13,
  "PROMOTION": 14,
  "REFUND": 3
}
```

## Unresolved mapping review groups

```json
{
  "NO_NARROW_PROFILE_MATCH": 530,
  "REQUIRED_BINDINGS_NOT_SOURCE_GROUNDED": 341
}
```

## Stratified semantic sample

### BD-02-001

- Mechanism: `INLINE_CONTRACT_REQUIRED`
- Criticality: `CRITICAL`
- Profile/category: `PRICING`
- Statement: **Decision** Business Entity trung tâm của YSim là Product. **Rationale** Product là đối tượng được khách hàng lựa chọn, là nền tảng của Catalog, Pricing, Allocation, Inventory, Fulfillment và Reporting.
- Rationale: PRICING combines domain-specific outcome/failure semantics; a shared profile would require conditional bindings or lose meaning.
- Semantic audit: `PASS`

### BD-02-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: **Decision** Supplier Product và YSim Product là hai Business Object khác nhau. **Rationale** Supplier Product phản ánh sản phẩm gốc của nhà cung cấp. YSim Product là sản phẩm thương mại hóa do YSim xây dựng.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-02-003

- Mechanism: `INLINE_CONTRACT_REQUIRED`
- Criticality: `CRITICAL`
- Profile/category: `ALLOCATION`
- Statement: **Decision** Allocation Engine chỉ lựa chọn Fulfillment Source. Không quản lý Product Catalog. **Rationale** Tách biệt trách nhiệm giữa Catalog Management và Fulfillment giúp hệ thống mở rộng dễ dàng.
- Rationale: ALLOCATION combines domain-specific outcome/failure semantics; a shared profile would require conditional bindings or lose meaning.
- Semantic audit: `PASS`

### BD-02-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: **Decision** Inventory được định nghĩa là Digital Asset Inventory. Không chỉ là Warehouse. **Rationale** Mọi Product Item đều là tài sản số có giá trị kinh tế và cần được quản lý trong suốt vòng đời.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-02-005

- Mechanism: `INLINE_CONTRACT_REQUIRED`
- Criticality: `CRITICAL`
- Profile/category: `REFUND`
- Statement: **Decision** Mọi Product Item đều phải có Inventory Record. Kể cả mua tức thời. **Rationale** Đảm bảo Accounting, Audit, Traceability, Refund và Customer Support.
- Rationale: REFUND combines domain-specific outcome/failure semantics; a shared profile would require conditional bindings or lose meaning.
- Semantic audit: `PASS`

### BD-02-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: **Decision** Product Intelligence là Business Capability bắt buộc. **Rationale** Giúp đồng bộ Catalog, phát hiện thay đổi từ Supplier và hỗ trợ vận hành Product hiệu quả.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: capability_subject, required_capabilities
- Semantic audit: `PASS`

### BD-02-007

- Mechanism: `INLINE_CONTRACT_REQUIRED`
- Criticality: `CRITICAL`
- Profile/category: `FINANCIAL_RECONCILIATION`
- Statement: **Decision** Snapshot Pricing là nguyên tắc bắt buộc. **Rationale** Mọi Settlement và nghiệp vụ tài chính phải sử dụng giá tại thời điểm phát sinh giao dịch.
- Rationale: FINANCIAL_RECONCILIATION combines domain-specific outcome/failure semantics; a shared profile would require conditional bindings or lose meaning.
- Semantic audit: `PASS`

### BD-03-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization là Business Entity quản lý toàn bộ kênh bán hàng.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-03-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization Structure và Distribution Network là hai mô hình độc lập.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-03-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Portal và Storefront là hai thành phần độc lập.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-03-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Portal là Storefront mở rộng.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-03-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Identity là Foundation Domain.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-03-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: User và Customer là hai Business Entity độc lập.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-03-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi User chỉ thuộc một Organization.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name
- Semantic audit: `PASS`

### BD-03-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Role thuộc Organization.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name
- Semantic audit: `PASS`

### BD-03-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Permission được xác định theo: Role + Resource Scope + Data Scope + Policy.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY, policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-03-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Ownership được quản lý theo Distribution Network.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-03-011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Support Governance được điều khiển bởi Support Policy. Support Policy gồm: - SELF_SUPPORT - PARENT_SUPPORT - HYBRID
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-03-012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi dữ liệu nhạy cảm phải hỗ trợ Data Masking.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-03-013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi thao tác truy cập dữ liệu nhạy cảm phải được Audit.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BD-04-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: YSim sử dụng mô hình Four-Level Catalog: - Supplier Catalog - Master Catalog - Sales Catalog - Storefront Catalog
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-04-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sales Catalog thuộc Organization.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-04-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sales Catalog chỉ tham chiếu Master Product. Không sao chép Product.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-04-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Product Specification chỉ được quản lý tại Master Catalog.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-04-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization chỉ được thay đổi: - Selling Price - Currency - Collection - Visibility - Marketing Content - Product Code Prefix/Postfix
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-04-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Product Version được tạo khi Supplier thay đổi Policy hoặc Specification.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-04-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier Attribute Mapping phải hỗ trợ cấu hình. Không hardcode.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-04-009

- Mechanism: `INLINE_CONTRACT_REQUIRED`
- Criticality: `HIGH`
- Profile/category: `COMPLEX_WORKFLOW`
- Statement: Catalog Publish sử dụng Workflow. Không Publish trực tiếp.
- Rationale: COMPLEX_WORKFLOW combines domain-specific outcome/failure semantics; a shared profile would require conditional bindings or lose meaning.
- Semantic audit: `PASS`

### BD-04-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Currency là một phần của Commercial Agreement giữa Organization và Parent.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-04-011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Product Intelligence phiên bản 2.0 chỉ tập trung vào Synchronization và Difference Detection.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-05-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Price thuộc Catalog.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-05-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Product chỉ lưu Reference Price.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-05-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Cost được tính theo Distribution Network.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-05-004

- Mechanism: `INLINE_CONTRACT_REQUIRED`
- Criticality: `CRITICAL`
- Profile/category: `PAYMENT`
- Statement: Chỉ Payment Owner được tạo Price Book.
- Rationale: PAYMENT combines domain-specific outcome/failure semantics; a shared profile would require conditional bindings or lose meaning.
- Semantic audit: `PASS`

### BD-05-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Price Book hỗ trợ Multi Currency.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-05-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Currency thuộc Commercial Agreement.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-05-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Partner được phép bán dưới Cost nhưng phải có Warning và Audit.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BD-05-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Price Book thay đổi thông qua Price Change Set.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-05-011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Revenue Sharing độc lập với Commission.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-05-013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commercial Agreement là Business Object trung tâm.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-05-016

- Mechanism: `INLINE_CONTRACT_REQUIRED`
- Criticality: `CRITICAL`
- Profile/category: `FULFILLMENT`
- Statement: Bắt buộc Pre-Fulfillment Commercial Validation.
- Rationale: FULFILLMENT combines domain-specific outcome/failure semantics; a shared profile would require conditional bindings or lose meaning.
- Semantic audit: `PASS`

### BD-06-001

- Mechanism: `INLINE_CONTRACT_REQUIRED`
- Criticality: `HIGH`
- Profile/category: `PROMOTION`
- Statement: Promotion thuộc Organization.
- Rationale: PROMOTION combines domain-specific outcome/failure semantics; a shared profile would require conditional bindings or lose meaning.
- Semantic audit: `PASS`

### BD-06-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Campaign là chiến lược bán hàng. Landing Page là Business Asset.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-06-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Landing Page thuộc Storefront. Một Landing Page có thể phục vụ nhiều Campaign.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-06-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Reference QR là Business Object độc lập.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: TWO_EXPLICIT_INDEPENDENT_ENTITIES
- Semantic audit: `PASS`

### BD-06-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Tracking luôn gắn với User và Organization.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name
- Semantic audit: `PASS`

### BD-06-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Marketing Attribution là Business Object độc lập.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: TWO_EXPLICIT_INDEPENDENT_ENTITIES
- Semantic audit: `PASS`

### BD-06-015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sales Enablement là Domain độc lập.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-07-002

- Mechanism: `INLINE_CONTRACT_REQUIRED`
- Criticality: `HIGH`
- Profile/category: `PROCUREMENT`
- Statement: YSim hỗ trợ hai loại Order: Sales Order và Purchase Order.
- Rationale: PROCUREMENT combines domain-specific outcome/failure semantics; a shared profile would require conditional bindings or lose meaning.
- Semantic audit: `PASS`

### BD-07-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sales Order được tạo theo Model C.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-07-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Cart thuộc Storefront.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-07-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một Cart không chứa nhiều Storefront hoặc nhiều Organization.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-07-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Checkout Session là Transaction Object.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-07-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Primary Email là thông tin bắt buộc duy nhất.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-08-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: GatewayFee được cấu hình theo CommercialAgreement.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-09-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Inventory và Product Item Lifecycle là hai Business Concept độc lập.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-09-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Inventory luôn thuộc YSim.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-09-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Portal là Capability độc lập.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-09-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: SMS không truyền QR Code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-09-011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Revoked Inventory yêu cầu Manual Verification.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-09-012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: QR gốc chỉ Download một lần trên Distribution Network.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-09-013

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `CRITICAL`
- Profile/category: `ACP-AUTHENTICATION_REQUIREMENT`
- Statement: Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc.
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "assurance_requirement": "Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc.",
  "principal_type": "Customer",
  "protected_action": "Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc."
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Customer, given assurance cannot be resolved or has expired, when authentication is evaluated, then no previous success is reused outside its validity boundary.",
  "negative": "Given missing or invalid assurance evidence, when Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc. is attempted, then authentication is denied or challenged without granting the protected action.",
  "positive": "Given Customer presents evidence satisfying Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc., when Customer Portal yêu cầu Two-Factor Authentication để xem QR gốc. is attempted, then authentication succeeds at the bound assurance level."
}
```
- Semantic audit: `PASS`

### BD-09-015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Delivery và Activation là hai Business Capability độc lập.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-10-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Transaction đều sinh FinancialEvent.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-10-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Revenue Sharing tính theo Bottom-Up Distribution.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-10-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: RevenueRecipient là Business Object.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-10-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: FinancialAccount là Business Object độc lập.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: TWO_EXPLICIT_INDEPENDENT_ENTITIES
- Semantic audit: `PASS`

### BD-10-010

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `NORMAL`
- Profile/category: `ACP-REQUIRED_CAPABILITY_SET`
- Statement: Wallet hỗ trợ Organization và Collaborator.
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "capability_subject": "Wallet",
  "required_capabilities": [
    "Organization",
    "Collaborator"
  ]
}
```
- Rendered contract:

```json
{
  "edge_boundary": "Given a capability outside Organization, Collaborator, when conformance is evaluated, then it is not used as evidence that a missing bound capability exists.",
  "negative": "For Wallet, given one bound capability is absent or attributed to another subject, when completeness is evaluated, then the missing or misattributed member is reported.",
  "positive": "Given Wallet, when its capability inventory is inspected, then every member of Organization, Collaborator is independently available and attributable to that subject."
}
```
- Semantic audit: `PASS`

### BD-10-013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Financial Domain hỗ trợ FX Gain/Loss.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-10-018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: FinancialExport hỗ trợ Excel, CSV và REST API.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BD-10-021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: ManualAdjustment yêu cầu Approval và Audit.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: approval_outcomes, required_audit_fields
- Semantic audit: `PASS`

### BD-10-023

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Money Flow và Product Flow là hai Business Flow độc lập.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-11-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Portal là Capability thống nhất của Customer.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-11-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Identity thuộc Platform. Customer Relationship thuộc Organization.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name
- Semantic audit: `PASS`

### BD-11-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Ticket hỗ trợ nhiều Source.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-11-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Ticket Category sử dụng Reference Data Management.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-11-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability Routing quyết định Support Queue.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-11-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Support Policy gồm: - SELF_SUPPORT - PARENT_SUPPORT - HYBRID
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-11-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier chỉ nhận Supplier Case.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-11-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Knowledge Base, FAQ và Troubleshooting Wizard là ba Capability độc lập.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-11-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization Onboarding là Business Capability.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-11-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Feedback hỗ trợ nhiều nguồn.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-11-011

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `NORMAL`
- Profile/category: `ACP-REQUIRED_CAPABILITY_SET`
- Statement: Platform hỗ trợ CSAT, CES, NPS và Rating.
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "capability_subject": "Platform",
  "required_capabilities": [
    "CSAT",
    "CES",
    "NPS",
    "Rating"
  ]
}
```
- Rendered contract:

```json
{
  "edge_boundary": "Given a capability outside CSAT, CES, NPS, Rating, when conformance is evaluated, then it is not used as evidence that a missing bound capability exists.",
  "negative": "For Platform, given one bound capability is absent or attributed to another subject, when completeness is evaluated, then the missing or misattributed member is reported.",
  "positive": "Given Platform, when its capability inventory is inspected, then every member of CSAT, CES, NPS, Rating is independently available and attributable to that subject."
}
```
- Semantic audit: `PASS`

### BD-11-012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Support sử dụng Consent Based Data Access.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-11-013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Feature Request là Business Capability của Platform.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-12-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Communication Platform là Platform Capability độc lập.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-12-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Notification sử dụng Event-Driven Architecture.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-12-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Notification được quyết định bằng Communication Matrix.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-12-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Portal Announcement là một Communication Channel.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-12-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Personal Inbox luôn là Delivery Channel cuối cùng.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-12-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: ContactPoint là Business Object.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-12-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Notification Preference sử dụng Matrix.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-12-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Template hỗ trợ Parent Override.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-12-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Localization hỗ trợ nhiều chuẩn hiển thị.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-12-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Notification Routing dựa trên Business Event.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-12-011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Retry Policy mặc định là 03 lần, cách nhau 05 phút.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-12-013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Notification Subscription và Notification Category sử dụng Reference Data Management.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-12-014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Version 2 sử dụng Real-time Notification.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-12-015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Notification hỗ trợ Auto Translation.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-12-016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Communication Policy hỗ trợ nhiều tầng Override.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-12-017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Do Not Disturb hỗ trợ Emergency Notification.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-12-018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Communication Platform sử dụng Message Queue.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-12-019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Communication Platform sử dụng Channel Adapter Pattern.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name
- Semantic audit: `PASS`

### BD-13-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: KPI Definition được cấu hình. Kiến trúc hỗ trợ mở rộng thêm các nhóm KPI và tiêu chuẩn đo lường.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### BD-13-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Report là Business Object độc lập. System Report chỉ dành cho YSim Internal. Business Report hỗ trợ kế thừa: YSim ↓ Parent Organization ↓ Organization Override
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: TWO_EXPLICIT_INDEPENDENT_ENTITIES
- Semantic audit: `PASS`

### BD-13-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Saved View là Business Object. Saved View thuộc User.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-13-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Report hỗ trợ: - Download - Email - Portal - Personal Inbox - API
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BD-13-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Dashboard hỗ trợ Drill-down tới Business Object.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-13-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Metric là Business Object. Metric là đơn vị đo lường chuẩn để xây dựng Dashboard, KPI và Report.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-13-011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Operational Dashboard có thể: - Real-time - Near Real-time Tùy theo yêu cầu nghiệp vụ và khả năng triển khai.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-13-012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Version 2 hỗ trợ Business Intelligence theo mô hình OLAP. Chưa triển khai: - AI Analytics - Machine Learning - Predictive Analytics
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: MIXED_ACTIVE_AND_DEFERRED_OBLIGATIONS
- Semantic audit: `PASS`

### BD-13-013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Report Permission được xác định theo: - Organization - Role - Permission - Data Scope - Support Policy Có thể Mask dữ liệu theo Permission.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY, policy_name
- Semantic audit: `PASS`

### BD-13-014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Dashboard hiển thị dữ liệu theo: - Localization - Currency Preference - Measurement Preference Report mặc định sử dụng Currency chuẩn của Report.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-13-015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Report luôn đọc dữ liệu từ Snapshot. Không đọc trực tiếp Transaction đang thay đổi.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-13-016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier Analytics chỉ dành cho YSim Internal. Supplier không có Dashboard riêng.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-13-017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization chỉ được Benchmark dữ liệu của chính Organization đó. Không được phép xem dữ liệu của Organization khác.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-13-018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Version 2 hỗ trợ Custom Report Builder. Report được cấu hình thay vì Hard-code.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### BD-13-019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Widget Library là Platform Capability. Widget được tái sử dụng trên: - Dashboard - Workspace - Admin Portal - Organization Portal - Customer Portal
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name
- Semantic audit: `PASS`

### BD-13-020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Insight là Business Object. Insight được sinh từ Rule Engine và Analytics. Version 2 chưa sử dụng AI.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-14-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration hỗ trợ Override theo mô hình Layer. Effective Configuration được tính tại Runtime.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-14-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Reference Data là Business Object. Reference Data quản lý toàn bộ dữ liệu tham chiếu của Platform. Reference Data hỗ trợ: - Multi-language - Parent / Child - Alias - Effective Date
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-14-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Dictionary là Business Object độc lập. Dictionary không thay thế Reference Data. Dictionary quản lý Label, Enum, Caption và Translation.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: TWO_EXPLICIT_INDEPENDENT_ENTITIES, allowed_values, dependent_fields, enum_field, prohibited_reference_states, reference_registry
- Semantic audit: `PASS`

### BD-14-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Lookup là Business Object. Lookup hỗ trợ Dynamic Form, Search và API.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BD-14-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Rule là Business Object. Business Rule được cấu hình. Không Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-14-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Rule hỗ trợ nhiều Scope. Rule có thể áp dụng theo: - Platform - Organization - Department - Storefront - Product - Campaign - Category - Customer Group
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW, policy_name
- Semantic audit: `PASS`

### BD-14-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Rule hỗ trợ: - Priority - Sequence - Stop Policy Stop Policy được cấu hình.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### BD-14-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Rule chỉnh sửa trực tiếp. Lịch sử thay đổi được lưu thông qua Configuration Version và Audit.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states, required_audit_fields
- Semantic audit: `PASS`

### BD-14-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Feature Flag là Business Object. Feature Flag hỗ trợ: - Global - Parent Organization - Organization - Storefront - User
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-14-011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Toàn bộ tham số hệ thống được quản lý bằng Parameter. Parameter hỗ trợ Override theo Scope.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes, required_capabilities
- Semantic audit: `PASS`

### BD-14-012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Metadata là Business Object. Metadata phục vụ: - Dynamic Form - Dynamic API - Validation - Import - Export - Report Builder - Dashboard
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BD-14-013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration hỗ trợ Version. Lifecycle: Draft ↓ Validate ↓ Approval ↓ Published ↓ Effective
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### BD-14-014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration bắt buộc Approval trước Publish. Approval theo Role và Permission.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY, approval_outcomes, policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-14-016

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `CRITICAL`
- Profile/category: `ACP-AUDITABILITY`
- Statement: Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "audit_trigger": "Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version",
  "audited_subject": "Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version",
  "required_audit_fields": [
    "reason",
    "version",
    "before",
    "after"
  ]
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version, given an override, failure, or recovery outcome, when auditing applies, then both original and effective outcome remain distinguishable where bound.",
  "negative": "For Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version, given a record missing one bound audit field, when audit completeness is verified, then it is reported non-conforming with the missing field identified.",
  "positive": "Given Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version for Configuration Audit lưu đầy đủ: - Who - When - Before - After - Reason - Version, when the outcome is recorded, then reason, version, before, after are present and attributable to that same subject."
}
```
- Semantic audit: `PASS`

### BD-14-017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration hỗ trợ: - JSON - YAML - Excel - CSV Import luôn Validate trước Apply.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### BD-14-021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration hỗ trợ Runtime Reload. Không yêu cầu Restart đối với đa số Configuration.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-14-022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization Template hỗ trợ Bootstrap toàn bộ Organization. Template tự động tạo: - Role - Dashboard - Storefront - Theme - Report - Notification - KB - FAQ - Survey - Support Policy - Configuration
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW, policy_name
- Semantic audit: `PASS`

### BD-14-023

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration áp dụng theo mô hình Layering. Effective Configuration luôn được tính theo Scope.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-14-024

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration Capability Matrix xác định: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Required - Runtime Reload
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-15-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Integration Platform hỗ trợ đầy đủ: - REST API - Webhook - Event Bus - Message Queue - Batch Import - Batch Export
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer, provider
- Semantic audit: `PASS`

### BD-15-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector là Business Object. Connector chỉ chịu trách nhiệm kết nối với hệ thống bên ngoài. Business Logic không được đặt trong Connector.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BD-15-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector và Adapter là hai thành phần độc lập. Connector quản lý: - Connection - Authentication - Session - Retry - Health Adapter quản lý: - Mapping - Transformation - Canonical Conversion
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: principal_type
- Semantic audit: `PASS`

### BD-15-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event là Business Object. Mọi Business Domain đều Publish Business Event.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-15-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain đăng ký Subscribe Business Event. Publisher không biết Subscriber. Event Bus chịu trách nhiệm Routing và Delivery.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-15-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event hỗ trợ Version. Backward Compatibility phải được đảm bảo.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-15-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Event Delivery hỗ trợ: - At Most Once - At Least Once - Exactly Once Mặc định sử dụng: **At Least Once**
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### BD-15-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: API và Business Event đều hỗ trợ Idempotency.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, idempotency_identity, producer, provider, stable_outcome
- Semantic audit: `PASS`

### BD-15-011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Retry Policy được cấu hình. Bao gồm: - Retry Count - Retry Interval - Retry Strategy - Exponential Backoff
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### BD-15-012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Dead Letter Queue là Business Object. Message Retry thất bại sẽ được chuyển vào DLQ.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-15-014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Webhook hỗ trợ: - Internal - Organization - External Partner
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-15-015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: API hỗ trợ Version. API Version được quản lý độc lập.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: TWO_EXPLICIT_INDEPENDENT_ENTITIES, consumer, provider
- Semantic audit: `PASS`

### BD-15-016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector hỗ trợ nhiều Runtime Profile: - Mock - Sandbox - UAT - Production
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BD-15-017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Message Queue là Business Object. Queue được tách theo từng nghiệp vụ.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-15-020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: API Gateway hỗ trợ: - Rate Limiting - Burst - Quota
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BD-15-021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector hỗ trợ Circuit Breaker.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BD-15-022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Scheduler có thể Publish Business Event.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-15-023

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Service Registry là Business Object. Registry quản lý: - Service - API - Published Event - Consumed Event - Dependency - Owner - Version
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer, provider
- Semantic audit: `PASS`

### BD-15-024

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain chỉ làm việc với Canonical Data Model.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: allowed_values, dependent_fields, enum_field, prohibited_reference_states, reference_registry
- Semantic audit: `PASS`

### BD-15-025

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain chỉ xử lý Canonical Event Model.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-15-026

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector Policy là Business Object. Connector Policy quản lý: - Timeout - Retry - Circuit Breaker - Rate Limit - Concurrency - Queue Priority - Health Threshold
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider, retry_limit, terminal_outcome
- Semantic audit: `PASS`

### BD-15-027

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector Routing Rule là Business Object. Routing Rule được cấu hình. Business Domain không quyết định Connector.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BD-15-028

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector phải khai báo Capability Matrix. Business Domain lựa chọn Connector dựa trên Capability.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BD-15-029

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector hỗ trợ Lifecycle: - Draft - Configured - Validated - Testing - Active - Suspended - Retired
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BD-15-030

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector Runtime Profile hỗ trợ: - Mock - Sandbox - UAT - Production Runtime tự động lựa chọn Profile theo Environment.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BD-16-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Identity Platform hỗ trợ nhiều Identity Provider. Bao gồm: - Local Account - Google - Apple - Facebook - Microsoft - Line - WeChat Kiến trúc hỗ trợ mở rộng thêm Identity Provider trong tương lai.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW, policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-16-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Authentication hỗ trợ: - Password - Email OTP - SMS OTP - Passkey - OAuth2 - OpenID Connect (OIDC) - SAML - API Key Authentication Method được cấu hình.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: principal_type
- Semantic audit: `PASS`

### BD-16-003

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `CRITICAL`
- Profile/category: `ACP-MFA_ENFORCEMENT`
- Statement: Platform hỗ trợ Multi-Factor Authentication (MFA). MFA có thể áp dụng theo: - Platform - Organization - Role - User - API Client
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "challenge_requirement": "MFA challenge required by the effective policy",
  "mfa_scopes": [
    "Platform",
    "Organization",
    "Role",
    "User",
    "API Client"
  ],
  "principal_types": [
    "User",
    "API Client"
  ]
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Platform, Organization, Role, User, API Client, given overlapping scope policies or an applicable approved recovery flow, when MFA is evaluated, then effective scopes and recovery-specific assurance are explicit without silently disabling MFA.",
  "negative": "For Platform, Organization, Role, User, API Client, given a required challenge is missing, invalid, or bypassed, when the protected action is attempted, then access is denied and the attempt is audited.",
  "positive": "Given MFA policies at Platform, Organization, Role, User, API Client for User, API Client, when effective policy is resolved, then MFA challenge required by the effective policy is presented and must be satisfied."
}
```
- Semantic audit: `PASS`

### BD-16-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Authorization sử dụng mô hình kết hợp: - RBAC - ABAC Permission được đánh giá động.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### BD-16-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Permission là Business Object. Permission không được Hard-code.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### BD-16-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Permission hỗ trợ Scope linh hoạt. Bao gồm: - Platform - Organization - Department - Team - Storefront - Customer Portal - User
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY, policy_name
- Semantic audit: `PASS`

### BD-16-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Permission hỗ trợ Data Scope. Data Scope được kết hợp với: - Organization Relationship - Support Policy - Capability - Security Policy
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY, policy_scopes
- Semantic audit: `PASS`

### BD-16-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform hỗ trợ Field-Level Permission. Permission có thể áp dụng tới từng Field.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY, policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-16-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform hỗ trợ Data Masking. Masking được quyết định bởi: - Permission - Data Classification - Customer Consent - Security Policy
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-16-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform hỗ trợ Customer Consent. Customer có quyền: - Chia sẻ - Thu hồi - Quản lý dữ liệu cá nhân
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-16-011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Session là Business Object. Platform hỗ trợ Concurrent Login trên nhiều thiết bị.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-16-012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: API Security hỗ trợ nhiều phương thức. Bao gồm: - OAuth2 - JWT - API Key - HMAC - Digital Signature
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-16-013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Secret là Business Object. Secret được quản lý tập trung.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-16-014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform hỗ trợ Encryption In Transit. Kiến trúc mở để hỗ trợ Encryption At Rest trong các phiên bản tiếp theo.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-16-015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform hỗ trợ Key Rotation. Key Management được quản lý tập trung.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes, required_capabilities
- Semantic audit: `PASS`

### BD-16-016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Audit Log là Business Object. Audit ghi nhận đầy đủ các Security Event và Business Event quan trọng.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BD-16-017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform hỗ trợ Compliance. Phiên bản hiện tại hỗ trợ: - GDPR
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW, policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-16-018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer có quyền bảo vệ dữ liệu cá nhân. Bao gồm: - Export Data - Delete Identity - Customer Consent
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-16-019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: API Permission được quản lý độc lập với Portal Permission.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### BD-16-020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Organization có Security Policy riêng. Organization có thể Override theo Capability được cấp.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: approval_outcomes, authorized_approver_scope, policy_scopes, policy_set, precedence_order
- Semantic audit: `PASS`

### BD-16-021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Risk Rule là Business Object. Risk Rule được cấu hình. Không Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-16-022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform hỗ trợ Temporary Account Lock.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes, required_capabilities
- Semantic audit: `PASS`

### BD-16-023

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `CRITICAL`
- Profile/category: `ACP-DATA_RETENTION`
- Statement: Audit Log được lưu trực tuyến 03 tháng. Sau đó được Archive.
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "data_subject": "Audit",
  "post_retention_outcome": "Archive",
  "retention_period": "03 tháng"
}
```
- Rendered contract:

```json
{
  "edge_boundary": "Given the retention boundary is crossed, when policy applies, then Archive occurs with transition evidence tied to the same data identity.",
  "negative": "Given Audit beyond 03 tháng, when online availability is inspected, then it is not retained online contrary to policy.",
  "positive": "Given Audit within 03 tháng, when availability is inspected, then the bound online or retained state is observable."
}
```
- Semantic audit: `PASS`

### BD-16-024

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Permission Evaluation Engine là thành phần trung tâm của Security Platform. Business Domain không tự đánh giá Permission.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY, policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-16-025

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Security Policy là Business Object. Security Policy hỗ trợ: - Version - Effective Date - Approval - Audit
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: approval_outcomes, required_audit_fields
- Semantic audit: `PASS`

### BD-16-026

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Identity Platform hỗ trợ Federation.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes, required_capabilities
- Semantic audit: `PASS`

### BD-16-027

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Security Platform Publish Business Event.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-16-028

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Data Classification là Business Object.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-16-029

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform áp dụng Zero Trust Principle.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-16-030

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Toàn bộ truy cập dữ liệu phải được đánh giá động thông qua Permission Evaluation Engine và Security Policy.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### BD-17-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform có một Platform Operations Center thống nhất. Operations Center là trung tâm điều hành toàn bộ nền tảng.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Health Check hỗ trợ đầy đủ các thành phần của Platform. Health Status được chuẩn hóa.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes, required_capabilities
- Semantic audit: `PASS`

### BD-17-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Metrics được chuẩn hóa. Metrics là nguồn dữ liệu cho: - Dashboard - Alert - Capacity Planning - SLO - SLA
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Alert Rule là Business Object. Alert Rule được cấu hình. Không Hard-code.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states
- Semantic audit: `PASS`

### BD-17-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Alert được gửi theo Notification Preference. Personal Inbox luôn là kênh nhận mặc định.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Scheduler là Business Object. Scheduler hỗ trợ: - Cron - Fixed Interval - Manual Trigger - Business Event Trigger
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Job Execution là Business Object. Mọi Job đều sinh Job Execution.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Worker là Business Object. Một Job có thể được xử lý bởi nhiều Worker.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Operation Retry độc lập Connector Retry.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: retry_limit, terminal_outcome
- Semantic audit: `PASS`

### BD-17-012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Maintenance Window là Business Object. Maintenance hỗ trợ nhiều cấp.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Backup Policy là Business Object.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capacity Policy là Business Object. Kiến trúc hỗ trợ Auto Scaling trong tương lai.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform có Operational Dashboard dành riêng cho Operator.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Operator sử dụng Permission riêng. Mọi thao tác đều được Security Platform kiểm soát.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY, policy_name, policy_scopes
- Semantic audit: `PASS`

### BD-17-018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Maintenance phải gửi Notification trước khi thực hiện.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Scheduler hỗ trợ Priority. Business Critical Job luôn được ưu tiên.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### BD-17-020

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `NORMAL`
- Profile/category: `ACP-SCOPE_EXCLUSION`
- Statement: Kiến trúc hỗ trợ Auto Scaling. Version hiện tại chưa triển khai.
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "current_baseline": "2.3",
  "excluded_capability": "Auto Scaling",
  "scope_status": "DEFERRED"
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Auto Scaling, given architectural readiness without implementation, when conformance is evaluated, then readiness evidence is distinguishable from active product availability.",
  "negative": "For Auto Scaling, given an exposed action or contract claiming the excluded capability is active, when scope conformance is checked, then the claim is rejected as outside the bound baseline.",
  "positive": "Given 2.3, when capability inventory is inspected, then Auto Scaling is marked DEFERRED and is not represented as active delivery."
}
```
- Semantic audit: `PASS`

### BD-17-021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Operational Audit ghi nhận toàn bộ thao tác vận hành.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BD-17-022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Operation Policy là Business Object. Operation Policy được Versioning.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: activation_condition, configuration_subject, lifecycle_states
- Semantic audit: `PASS`

### BD-17-023

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Scheduler hỗ trợ Business Event Trigger.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-17-024

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization không có Operations Capability. Operations chỉ thuộc Platform.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-025

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Maintenance hỗ trợ nhiều Scope.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes, required_capabilities
- Semantic audit: `PASS`

### BD-17-026

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Operations Platform Publish Business Event.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: activation_condition, configuration_subject, consumer, delivery_outcome, event_name, lifecycle_states, producer
- Semantic audit: `PASS`

### BD-17-027

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Runbook là Business Object.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BD-17-029

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform hỗ trợ Operational Command Center.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-17-030

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform hỗ trợ Replay.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BD-17-031

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `NORMAL`
- Profile/category: `ACP-SCOPE_EXCLUSION`
- Statement: Kiến trúc hỗ trợ Chaos Readiness. Version hiện tại chưa triển khai.
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "current_baseline": "2.3",
  "excluded_capability": "Chaos Readiness",
  "scope_status": "DEFERRED"
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Chaos Readiness, given architectural readiness without implementation, when conformance is evaluated, then readiness evidence is distinguishable from active product availability.",
  "negative": "For Chaos Readiness, given an exposed action or contract claiming the excluded capability is active, when scope conformance is checked, then the claim is rejected as outside the bound baseline.",
  "positive": "Given 2.3, when capability inventory is inspected, then Chaos Readiness is marked DEFERRED and is not represented as active delivery."
}
```
- Semantic audit: `PASS`

### BO-EP-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object là trung tâm của Enterprise Model.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-EP-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object độc lập với Database.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: TWO_EXPLICIT_INDEPENDENT_ENTITIES
- Semantic audit: `PASS`

### BO-EP-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object độc lập với Source Code.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: TWO_EXPLICIT_INDEPENDENT_ENTITIES
- Semantic audit: `PASS`

### BO-EP-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object độc lập với UI.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: TWO_EXPLICIT_INDEPENDENT_ENTITIES
- Semantic audit: `PASS`

### BO-EP-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object độc lập với Integration Technology.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: TWO_EXPLICIT_INDEPENDENT_ENTITIES, consumer, provider
- Semantic audit: `PASS`

### BO-EP-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object được sở hữu bởi đúng một Business Domain.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-EP-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object có thể Publish Business Event.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-EP-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object sử dụng Canonical Vocabulary trên toàn Platform.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: allowed_values, dependent_fields, enum_field, prohibited_reference_states, reference_registry
- Semantic audit: `PASS`

### BO-EP-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object được quản lý tập trung trong Business Object Registry.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-EP-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object Registry là Enterprise Dictionary của nền tảng YSim.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-P01

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một Business Object chỉ có một định nghĩa duy nhất trên toàn Platform.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-P02

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object phản ánh nghiệp vụ. Không phản ánh cấu trúc Database hoặc Source Code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-P03

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Business Object có đúng một Owner Domain. Owner Domain chịu trách nhiệm quản lý vòng đời và nghiệp vụ của Business Object.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-P04

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Business Object phải có khả năng tham chiếu tới: - Workshop - DMS - DBD - API - SDD để đảm bảo Traceability.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BO-P05

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object ID là bất biến. Tên có thể Version nhưng Business Object ID không thay đổi.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-P07

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi thay đổi Business Object đều phải được: - Review - Approval - Versioning - Audit - Traceability
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: activation_condition, approval_outcomes, configuration_subject, lifecycle_states, required_audit_fields
- Semantic audit: `PASS`

### BO-R01

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Business Object chỉ có một Owner Domain.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-R02

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object chỉ được tham chiếu thông qua Business Identity. Không tham chiếu trực tiếp Database Key.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-R03

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot không được cập nhật. Snapshot chỉ được tạo mới.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-R04

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object Publish Business Event. Business Object khác Subscribe Business Event. Không gọi trực tiếp khi không cần thiết.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BO-R05

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object giữa các Domain phải giảm phụ thuộc trực tiếp. Ưu tiên: - Business Event - Canonical Model - Business Service
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: allowed_values, dependent_fields, enum_field, prohibited_reference_states, reference_registry
- Semantic audit: `PASS`

### BO-R06

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object sử dụng Configuration và Policy. Không Hard-code hành vi nghiệp vụ.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object phải tuân thủ các quy tắc đặt tên sau:
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Tên phải phản ánh đúng khái niệm nghiệp vụ.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sau khi Business Object được công bố và sử dụng trong Platform, tên không được thay đổi nếu không có quyết định kiến trúc.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nếu cần thay đổi phải: - Review Impact
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nếu cần thay đổi phải: - Approval
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nếu cần thay đổi phải: - Versioning
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nếu cần thay đổi phải: - Traceability
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một Business Object chỉ được tồn tại với một tên duy nhất trong toàn Platform.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không được phép tồn tại các trường hợp: - Customer / Client
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không được phép tồn tại các trường hợp: - Store / Shop
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không được phép tồn tại các trường hợp: - User Account / Account
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Business Object được cấp một mã định danh duy nhất.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không phải mọi Business Object đều có Lifecycle.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object Registry tuân thủ các nguyên tắc sau.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot chỉ được tạo mới, không chỉnh sửa.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object tuân thủ các nguyên tắc quan hệ sau.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object chỉ được tạo mới khi: - Có Business Requirement.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object chỉ được tạo mới khi: - Có Owner Domain.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object chỉ được tạo mới khi: - Có Business Definition.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object chỉ được tạo mới khi: - Có Architecture Review.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object chỉ được tạo mới khi: - Có Approval.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Object không được tạo ra chỉ để phục vụ kỹ thuật.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R031

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `NORMAL`
- Profile/category: `ACP-SCOPE_EXCLUSION`
- Statement: Các Business Object dự kiến bổ sung trong các phiên bản sau: - Recommendation Engine
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "current_baseline": "2.3",
  "excluded_capability": "Recommendation Engine",
  "scope_status": "FUTURE"
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Recommendation Engine, given architectural readiness without implementation, when conformance is evaluated, then readiness evidence is distinguishable from active product availability.",
  "negative": "For Recommendation Engine, given an exposed action or contract claiming the excluded capability is active, when scope conformance is checked, then the claim is rejected as outside the bound baseline.",
  "positive": "Given 2.3, when capability inventory is inspected, then Recommendation Engine is marked FUTURE and is not represented as active delivery."
}
```
- Semantic audit: `PASS`

### BRD-BO-INDEX-R033

- Mechanism: `INLINE_CONTRACT_REQUIRED`
- Criticality: `NORMAL`
- Profile/category: `FRAUD_RISK_DECISION`
- Statement: Các Business Object dự kiến bổ sung trong các phiên bản sau: - Fraud Detection
- Rationale: FRAUD_RISK_DECISION combines domain-specific outcome/failure semantics; a shared profile would require conditional bindings or lose meaning.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R043

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Architecture Review
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R044

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Approval
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R045

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Versioning
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R046

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Audit
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-BO-INDEX-R047

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Business Object mới hoặc thay đổi Business Object hiện có phải được: - Traceability
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R048

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi tài liệu YSim phải sử dụng đúng Business Object được định nghĩa trong Business Object Registry.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-BO-INDEX-R049

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không được tạo Business Object mới ngoài Registry nếu chưa được Architecture Review.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-CAP-INDEX-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không phải mọi Capability đều khả dụng cho mọi đối tượng.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-CAP-INDEX-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Capability được cấp một mã định danh duy nhất.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-CAP-INDEX-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability Registry tuân thủ các nguyên tắc sau.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-CAP-INDEX-R020

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `NORMAL`
- Profile/category: `ACP-SCOPE_EXCLUSION`
- Statement: | Capability | Planned Version | | Recommendation Engine | Future |
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "current_baseline": "2.3",
  "excluded_capability": "Recommendation Engine | Future",
  "scope_status": "FUTURE"
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Recommendation Engine | Future, given architectural readiness without implementation, when conformance is evaluated, then readiness evidence is distinguishable from active product availability.",
  "negative": "For Recommendation Engine | Future, given an exposed action or contract claiming the excluded capability is active, when scope conformance is checked, then the claim is rejected as outside the bound baseline.",
  "positive": "Given 2.3, when capability inventory is inspected, then Recommendation Engine | Future is marked FUTURE and is not represented as active delivery."
}
```
- Semantic audit: `PASS`

### BRD-CAP-INDEX-R024

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Architecture Review
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-CAP-INDEX-R025

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Approval
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-CAP-INDEX-R026

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Versioning
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-CAP-INDEX-R027

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Audit
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-CAP-INDEX-R028

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Capability mới hoặc thay đổi Capability hiện có phải được: - Traceability
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-CAP-INDEX-R029

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `HIGH`
- Profile/category: `ACP-ENUM_REFERENCE_INTEGRITY`
- Statement: Mỗi Capability phải khai báo event_role là PUBLISHER, SUBSCRIBER, BOTH hoặc NONE cùng published_event_ids và subscribed_event_ids; NONE yêu cầu hai danh sách rỗng, các role còn lại yêu cầu danh sách tương ứng không rỗng, và mọi tham chiếu phải trỏ tới Event Registry ID canonical active/approved, không được dùng alias, retired, tombstone hoặc dangling reference.
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "allowed_values": [
    "PUBLISHER",
    "SUBSCRIBER",
    "BOTH",
    "NONE"
  ],
  "dependent_fields": [
    "published_event_ids",
    "subscribed_event_ids"
  ],
  "enum_field": "event_role",
  "prohibited_reference_states": [
    "alias",
    "retired",
    "tombstone",
    "dangling"
  ],
  "reference_registry": "Event Registry"
}
```
- Rendered contract:

```json
{
  "edge_boundary": "Given references in alias, retired, tombstone, dangling, when canonical resolution runs, then every prohibited or dangling reference is rejected.",
  "negative": "Given an unsupported event_role value or inconsistent published_event_ids, subscribed_event_ids, when validation runs, then the record is rejected and the invalid field is identified.",
  "positive": "Given event_role and published_event_ids, subscribed_event_ids, when a record is validated, then only PUBLISHER, SUBSCRIBER, BOTH, NONE and role-consistent fields with references resolving in Event Registry are accepted."
}
```
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R002

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `NORMAL`
- Profile/category: `ACP-EVENT_ORDERING`
- Statement: Các event thuộc họ Marketing, Analytics và Notification không bắt buộc duy trì thứ tự xử lý.
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "event_families": [
    "Marketing",
    "Analytics",
    "Notification"
  ],
  "observation_boundary": "processing order for the bound event family",
  "ordering_policy": "NOT_REQUIRED"
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Marketing, Analytics, Notification, given interleaved events across bound families, when conformance is reviewed, then the policy is evaluated per family and does not infer cross-family ordering.",
  "negative": "Given an event family outside Marketing, Analytics, Notification, when ordering is evaluated, then this profile binding is not used as its ordering authority.",
  "positive": "Given events from Marketing, Analytics, Notification, when processing is observed at processing order for the bound event family, then behavior conforms to NOT_REQUIRED without applying another family's policy."
}
```
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Event được cấp một mã định danh duy nhất.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Tên Event phải phản ánh **điều đã xảy ra**, không phản ánh **hành động sẽ thực hiện**.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Connector phải chuyển đổi dữ liệu giữa định dạng riêng của đối tác và Canonical Event Model trước khi Publish hoặc Consume trong Platform.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer, provider
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event chỉ được tạo mới khi: - Có Business Requirement.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event chỉ được tạo mới khi: - Có Business Object nguồn.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event chỉ được tạo mới khi: - Có Capability sở hữu.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event chỉ được tạo mới khi: - Có Publisher rõ ràng.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event chỉ được tạo mới khi: - Có Subscriber rõ ràng.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event chỉ được tạo mới khi: - Có Version.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event chỉ được tạo mới khi: - Có Review.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event chỉ được tạo mới khi: - Có Approval.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R025

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Architecture Review
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R026

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Approval
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R027

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Versioning
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R028

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Audit
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer, required_audit_fields
- Semantic audit: `PASS`

### BRD-EVENT-INDEX-R029

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Business Event mới hoặc thay đổi Business Event hiện có phải trải qua: - Traceability
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-META-MODEL-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot không phải History.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-META-MODEL-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi thay đổi đối với Business Capability, Business Object, Business Policy, Business Event hoặc Business Snapshot cần được xem xét dựa trên Business Meta Model này để đảm bảo tính nhất quán của toàn bộ hệ thống.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-META-MODEL-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi tài liệu kiến trúc phải tuân thủ Business Meta Model này.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-META-MODEL-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Commerce Experience phải được xây dựng từ Business Model và Business Blueprint đã được chuẩn hóa.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không phải mọi Policy đều hỗ trợ toàn bộ Scope.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy Inheritance phải được quản lý tập trung.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Policy được cấp một mã định danh duy nhất.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: mà không cần triển khai lại hệ thống.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Approval phải được ghi Audit.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: approval_outcomes, required_audit_fields
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy không được Hard-code trong Source Code khi có thể cấu hình.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform luôn đánh giá Policy trước.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mô hình này giúp thay đổi hành vi nghiệp vụ thông qua cấu hình Policy mà không cần thay đổi mã nguồn.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Architecture Review
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Approval
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Versioning
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R023

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Effective Date
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R024

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Audit
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R025

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Policy mới hoặc thay đổi Policy hiện có phải trải qua: - Traceability
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R026

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Scope thấp hơn ưu tiên kế thừa.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes, policy_set, precedence_order
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R027

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Chỉ Override khi thực sự cần thiết.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: approval_outcomes, authorized_approver_scope, policy_set, precedence_order
- Semantic audit: `PASS`

### BRD-POLICY-INDEX-R028

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Không được Override các System Policy bắt buộc.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: approval_outcomes, authorized_approver_scope, policy_set, precedence_order
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Snapshot được cấp một mã định danh duy nhất.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nếu dữ liệu nghiệp vụ thay đổi: Platform phải tạo Snapshot mới.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Snapshot không phải: - Audit Log
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Snapshot không phải: - History Record
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Snapshot không phải: - Temporary Cache
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot tuân thủ Retention Policy.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot Content vẫn luôn bất biến.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Snapshot phải lưu toàn bộ **Business Context** cần thiết để có thể tái hiện chính xác quyết định nghiệp vụ tại thời điểm Snapshot được tạo.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot không được cập nhật để phản ánh trạng thái mới.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot có thể được nhiều hệ thống sử dụng lại mà không cần đọc dữ liệu Runtime.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới phải có: - Snapshot ID
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R023

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới phải có: - Source Business Object
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R024

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới phải có: - Trigger Event
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R025

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới phải có: - Snapshot Type
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R026

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới phải có: - Version
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R027

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới phải có: - Retention Policy
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R028

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới phải có: - Visibility
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R029

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới phải có: - Owner
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R030

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới phải có: - Approval
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R031

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot chỉ được tạo khi có Business Requirement rõ ràng.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R032

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Business Review
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R033

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Architecture Review
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R034

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Approval
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R035

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Versioning
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R036

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Security Review
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R037

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Audit
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R038

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Snapshot mới hoặc thay đổi Snapshot Definition phải trải qua: - Traceability
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R039

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Event không thay thế Snapshot.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R040

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Snapshot không thay thế Audit.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R041

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Audit không thay thế History.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-SNAPSHOT-INDEX-R042

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - History không phải Business Evidence.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Đối tác không cần sử dụng nền tảng Website hoặc E-Commerce của bên thứ ba để bán eSIM và các Digital Connectivity Products.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: CXP phải cho phép: ✓ tạo Store mới.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Store không được tạo từ đầu một cách thủ công.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Blueprint không phải Source Code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Blueprint cũng không phải giao diện.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Blueprint là tập hợp các Capability, Business Rules và Experience Flow cần có để triển khai một Business Model.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: AI không được phép Publish Blueprint khi chưa được phê duyệt.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-UPDATE-01-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Blueprint tuân thủ các nguyên tắc sau.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Store chỉ được phép nhận giao dịch khi ở trạng thái **Active**.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: source_states, target_states, trigger
- Semantic audit: `PASS`

### BRD-UPDATE-01-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Experience không được xây dựng bằng cách kết nối trực tiếp từng Business Domain vào giao diện.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Store phải hỗ trợ Tracking xuyên suốt hành trình khách hàng: Visitor
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-UPDATE-01-R013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Store phải hỗ trợ: - Brand Name
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-UPDATE-01-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Store phải hỗ trợ: - Logo
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-UPDATE-01-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Store phải hỗ trợ: - Domain
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-UPDATE-01-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Store phải hỗ trợ: - Theme
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-UPDATE-01-R017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Store phải hỗ trợ: - Language
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-UPDATE-01-R018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Store phải hỗ trợ: - Currency
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-UPDATE-01-R019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Store phải hỗ trợ: - Contact Information
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-UPDATE-01-R020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Experience Platform tuân thủ: - Commerce First
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_trace
- Semantic audit: `PASS`

### BRD-UPDATE-01-R021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Experience Platform tuân thủ: - Configuration over Customization
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states
- Semantic audit: `PASS`

### BRD-UPDATE-01-R022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Experience Platform tuân thủ: - White-label by Default
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R023

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Experience Platform tuân thủ: - Publish in Minutes
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: activation_condition, configuration_subject, lifecycle_states
- Semantic audit: `PASS`

### BRD-UPDATE-01-R024

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Experience Platform tuân thủ: - Multi-tenant
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R025

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Experience Platform tuân thủ: - Multi-brand
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R026

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Experience Platform tuân thủ: - Multi-language
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R027

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Experience Platform tuân thủ: - Multi-country
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R028

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Experience Platform tuân thủ: - API First
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BRD-UPDATE-01-R029

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Experience phải ưu tiên trải nghiệm người dùng trong các quyết định trình bày mà không thay đổi hành vi nghiệp vụ chuẩn.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R030

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `NORMAL`
- Profile/category: `ACP-DESIGN_CONFORMANCE_TRACE`
- Statement: Business Model là điểm khởi đầu của mọi Commerce Experience trên nền tảng YSim.
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "governed_artifact": "6I. Business Principles",
  "principle": "Business Model là điểm khởi đầu của mọi Commerce Experience trên nền tảng YSim.",
  "required_trace": [
    "identified Business Model",
    "Commerce Experience creation trace",
    "Commerce Experience publication trace"
  ]
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Business Model là điểm khởi đầu của mọi Commerce Experience trên nền tảng YSim., given the principle is not applicable to an artifact, when review runs, then non-applicability is justified from scope rather than treated as conformance evidence.",
  "negative": "For Business Model là điểm khởi đầu của mọi Commerce Experience trên nền tảng YSim., given a missing trace or direct violation of the bound principle, when conformance is reviewed, then the artifact is reported non-conforming with the exact gap identified.",
  "positive": "Given 6I. Business Principles, when conformance to Business Model là điểm khởi đầu của mọi Commerce Experience trên nền tảng YSim. is reviewed, then identified Business Model, Commerce Experience creation trace, Commerce Experience publication trace is complete and the applicable design or configuration boundary is explicit."
}
```
- Semantic audit: `PASS`

### BRD-UPDATE-01-R031

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Commerce Experience phải được khởi tạo từ Store Template được phê duyệt thay vì xây dựng thủ công từ đầu.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R032

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Experience phải có khả năng sử dụng các contract API chuẩn mà không phụ thuộc vào một lớp trình bày cụ thể.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-UPDATE-01-R033

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nền tảng phải chuẩn bị contract và metadata có quản trị để hỗ trợ khả năng AI trong tương lai; nguyên tắc này không được diễn giải thành một tính năng sản phẩm AI active nếu chưa có yêu cầu được phê duyệt.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_trace
- Semantic audit: `PASS`

### BRD-WS-01-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: YSim không được định vị là một website bán eSIM đơn lẻ mà là một White-label Commerce Platform dành riêng cho ngành eSIM.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-01-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: - eSIM Commerce
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-01-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: YSim phải cung cấp năng lực thương mại white-label như một nguyên tắc sản phẩm, với hành vi cụ thể được quy định bởi các yêu cầu kênh và cấu hình liên quan.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states
- Semantic audit: `PASS`

### BRD-WS-01-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: - Multi-level Distribution
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-01-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: - Multi-supplier Integration
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BRD-WS-01-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: - Campaign
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-01-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: - Checkout
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-01-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: - Activation
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-01-R017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: - CRM
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-01-R018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: - Customer Support
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-01-R019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: - Analytics
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-01-R027

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: YSim không phải Marketplace.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-01-R028

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Hệ thống phải hỗ trợ: - Direct Website
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-01-R029

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Hệ thống phải hỗ trợ: - White-label Website
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-01-R030

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Hệ thống phải hỗ trợ: - Agency
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-01-R031

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Hệ thống phải hỗ trợ: - Multi-level Distribution
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-01-R032

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Hệ thống phải hỗ trợ: - Online Seller
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-01-R033

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Hệ thống phải hỗ trợ: - Social Commerce
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-01-R034

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Hệ thống phải hỗ trợ: - Marketplace
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-01-R035

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Hệ thống phải hỗ trợ: - API Partner
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BRD-WS-01-R036

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Hệ thống phải hỗ trợ: - Enterprise Customer
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-02-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi YSim Product phải có Product Specification chuẩn.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-02-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Tuy nhiên Product Specification phải phản ánh đúng khả năng sử dụng thực tế của eSIM.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-02-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Inventory luôn tồn tại.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-02-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Dù theo hình thức nào, mọi Product Item đều phải được ghi nhận vào Inventory.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-03-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi User chỉ thuộc duy nhất một Organization.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-03-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nếu một người làm việc cho nhiều Organization thì phải có nhiều User khác nhau.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-03-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Collaborator không phải Organization.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-03-R005

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `HIGH`
- Profile/category: `ACP-ROLE_AND_PERMISSION_ENFORCEMENT`
- Statement: Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - khách hàng của mình
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "actor_scope": "Collaborator",
  "allowed_actions": [
    "view - khách hàng của mình"
  ],
  "governed_resource": "- khách hàng của mình",
  "prohibited_actions": [
    "view outside the bound scope of - khách hàng của mình"
  ]
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Collaborator, given ownership or scope attribution is missing or conflicting, when access is evaluated, then no broader access is inferred and the unresolved boundary is denied.",
  "negative": "Given the same actor requests view outside the bound scope of - khách hàng của mình, when authorization is evaluated, then the action is denied and protected state remains unchanged.",
  "positive": "Given Collaborator, when access to - khách hàng của mình is evaluated, then only view - khách hàng của mình are available within the bound scope."
}
```
- Semantic audit: `PASS`

### BRD-WS-03-R006

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `HIGH`
- Profile/category: `ACP-ROLE_AND_PERMISSION_ENFORCEMENT`
- Statement: Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - doanh thu của mình
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "actor_scope": "Collaborator",
  "allowed_actions": [
    "view - doanh thu của mình"
  ],
  "governed_resource": "- doanh thu của mình",
  "prohibited_actions": [
    "view outside the bound scope of - doanh thu của mình"
  ]
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Collaborator, given ownership or scope attribution is missing or conflicting, when access is evaluated, then no broader access is inferred and the unresolved boundary is denied.",
  "negative": "Given the same actor requests view outside the bound scope of - doanh thu của mình, when authorization is evaluated, then the action is denied and protected state remains unchanged.",
  "positive": "Given Collaborator, when access to - doanh thu của mình is evaluated, then only view - doanh thu của mình are available within the bound scope."
}
```
- Semantic audit: `PASS`

### BRD-WS-03-R007

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `CRITICAL`
- Profile/category: `ACP-ROLE_AND_PERMISSION_ENFORCEMENT`
- Statement: Collaborator sử dụng công cụ bán hàng tương tự Sales nhưng chỉ được xem: - commission của mình
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "actor_scope": "Collaborator",
  "allowed_actions": [
    "view - commission của mình"
  ],
  "governed_resource": "- commission của mình",
  "prohibited_actions": [
    "view outside the bound scope of - commission của mình"
  ]
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Collaborator, given ownership or scope attribution is missing or conflicting, when access is evaluated, then no broader access is inferred and the unresolved boundary is denied.",
  "negative": "Given the same actor requests view outside the bound scope of - commission của mình, when authorization is evaluated, then the action is denied and protected state remains unchanged.",
  "positive": "Given Collaborator, when access to - commission của mình is evaluated, then only view - commission của mình are available within the bound scope."
}
```
- Semantic audit: `PASS`

### BRD-WS-03-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Collaborator không được xem dữ liệu nội bộ của Organization nếu không được cấp quyền.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### BRD-WS-03-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Các trường dữ liệu nhạy cảm phải hỗ trợ Masking.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-03-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một Organization không được phép truy cập dữ liệu của Organization khác nếu không được phép theo Business Rule.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Master Catalog là nguồn dữ liệu chuẩn duy nhất (Single Source of Truth).
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization không được phép thay đổi: - Product Specification
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization không được phép thay đổi: - Coverage
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization không được phép thay đổi: - Data Package
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization không được phép thay đổi: - Duration
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization không được phép thay đổi: - Activation Policy
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization không được phép thay đổi: - Product Attribute chuẩn
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization không được phép thay đổi: - Product Version
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Specification chỉ được quản lý tại Master Catalog.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: UUID mới là Identity duy nhất.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Reason Required
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sales Catalog không được sửa Product Specification.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization chỉ được sử dụng Currency đã được Parent Organization phê duyệt.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-04-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Việc thay đổi Exchange Rate phải được thống nhất giữa Organization và Parent.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Unit Price
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier MSRP
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Discount Price
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Discount Rate
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Tax
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Supplier Fee
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Khi tạo Master Product từ Supplier Product, hệ thống cần lưu: - Suggested Retail Price
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không phải Selling Price.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Price Book phải có: - Base Currency
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Parent và Child phải thống nhất: - Exchange Rate Source
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Parent và Child phải thống nhất: - Effective Date
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Parent và Child phải thống nhất: - Exchange Policy
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: thì hệ thống phải: - Warning
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: thì hệ thống phải: - Reason Required
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: thì hệ thống phải: - Parent Notification
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: thì hệ thống phải: - Audit
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-05-R020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi thay đổi Price Book phải được thực hiện thông qua Price Change Set.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-05-R024

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Trước khi Publish Price Change Set, hệ thống phải: - cho phép Review
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-WS-05-R025

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Trước khi Publish Price Change Set, hệ thống phải: - cho phép Delay Publish
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-WS-05-R026

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Trước khi Publish Price Change Set, hệ thống phải: - cho phép Continue Publish
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-WS-06-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sales Enablement không phải Marketing.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-06-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Campaign không phải Landing Page.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-06-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Reference QR không phải: - eSIM QR
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-06-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Reference QR luôn gắn Tracking ID.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-06-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Tracking luôn gắn với User.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-06-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một giao dịch cần Snapshot: - Storefront
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-06-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một giao dịch cần Snapshot: - Landing Page
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-06-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một giao dịch cần Snapshot: - Campaign
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-06-R013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một giao dịch cần Snapshot: - Reference QR
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-06-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một giao dịch cần Snapshot: - Tracking ID
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-06-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một giao dịch cần Snapshot: - Sales User
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-06-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một giao dịch cần Snapshot: - Organization
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-06-R017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một giao dịch cần Snapshot: - Distribution Path
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-07-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Identity sẽ Merge sau nếu cần.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-07-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Version 2.0 chỉ bắt buộc: Primary Email.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-07-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Primary Email luôn nhận: - Invoice
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-07-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không cho phép sửa: - Product
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-07-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không cho phép sửa: - Quantity
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-07-R017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không cho phép sửa: - Currency
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-07-R019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không cho phép sửa: - Price
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-07-R020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi thay đổi đều phải Audit.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-08-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Callback phải được Audit.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-09-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Inventory **không phải** là trạng thái của Product Item.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: source_states, target_states, trigger
- Semantic audit: `PASS`

### BRD-WS-09-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không cho phép đổi Recipient.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-09-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: QR gốc chỉ được Download một lần trong Distribution Network.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-09-R013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Portal muốn xem lại QR gốc: Bắt buộc:
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-09-R014

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `CRITICAL`
- Profile/category: `ACP-AUTHENTICATION_REQUIREMENT`
- Statement: Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP).
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "assurance_requirement": "Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP).",
  "principal_type": "Customer",
  "protected_action": "Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP)."
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Customer, given assurance cannot be resolved or has expired, when authentication is evaluated, then no previous success is reused outside its validity boundary.",
  "negative": "Given missing or invalid assurance evidence, when Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP). is attempted, then authentication is denied or challenged without granting the protected action.",
  "positive": "Given Customer presents evidence satisfying Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP)., when Customer Portal muốn xem lại QR gốc: Bắt buộc: - Two-Factor Authentication (OTP). is attempted, then authentication succeeds at the bound assurance level."
}
```
- Semantic audit: `PASS`

### BRD-WS-10-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Rollback luôn sinh FinancialEvent mới.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, producer
- Semantic audit: `PASS`

### BRD-WS-10-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: ManualAdjustment luôn sinh: FinancialEvent.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, producer
- Semantic audit: `PASS`

### BRD-WS-11-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Identity luôn thuộc YSim.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-11-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization chỉ được cấp quyền quản lý Relationship.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-11-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Ticket luôn lưu: - Source
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-11-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Ticket luôn lưu: - Creator
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-11-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Ticket luôn lưu: - Owner
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-11-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier Case luôn được YSim Staff theo dõi.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-11-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Có thể cấu hình: - Always - Random - Disabled
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-12-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Notification không được phép mất hoàn toàn.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-12-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Communication Log phải hỗ trợ: - Search
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-12-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Communication Log phải hỗ trợ: - Export
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-12-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Communication Log phải hỗ trợ: - Retention Policy
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-12-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Communication Log phải hỗ trợ: - Auto Rotation
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### BRD-WS-12-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Portal luôn hỗ trợ: - Read
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### BRD-WS-12-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Portal luôn hỗ trợ: - Read Time
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### BRD-WS-12-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Communication Consent tuân thủ GDPR.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Dashboard và Widget phải hỗ trợ Drill-down tới module hoặc Business Object tương ứng.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Widget Library cho phép Organization lựa chọn Widget cần hiển thị hoặc ẩn.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Drill-down phải tôn trọng Permission và Data Scope của User.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY, policy_name, policy_scopes
- Semantic audit: `PASS`

### BRD-WS-13-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không bắt buộc toàn bộ Dashboard phải Real-time.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Currency
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Rate
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Conversion Rule
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nếu Report sử dụng Currency khác thì phải hiển thị rõ: - Exchange Time
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Dashboard luôn chuyển đổi đơn vị hiển thị theo cấu hình Localization của User.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: source_states, state_subject, target_states, trigger
- Semantic audit: `PASS`

### BRD-WS-13-R013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Report luôn đọc dữ liệu từ Snapshot.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Analytics không được chia sẻ giữa các Organization.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Tuân thủ Relationship Policy và Data Permission.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### BRD-WS-13-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization chỉ được xem Benchmark của chính Organization đó.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: actor_scope
- Semantic audit: `PASS`

### BRD-WS-13-R017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không được phép xem: - Revenue của Organization khác
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không được phép xem: - KPI của Organization khác
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không được phép xem: - Customer của Organization khác
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization có thể lựa chọn Widget cần hiển thị.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-13-R023

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Report không được Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration luôn được tính theo mô hình **Effective Configuration**.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Reference Data không được Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Rule không được Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Rule luôn lưu: - Current Version
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Rule luôn lưu: - Modified By
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Rule luôn lưu: - Modified Time
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Rule luôn lưu: - Change Summary
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Lịch sử thay đổi không được phép xóa.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Feature Flag luôn được Runtime Reload.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Parameter không được Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Bao gồm: - Field Name - Data Type - Required - Default Value - Validation Rule - Searchable - Sortable - Filterable - Exportable - Importable - Permission - Localization - Tooltip - Description
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### BRD-WS-14-R013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Version cũ luôn được lưu lại.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration phải được Approval trước khi Publish.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-WS-14-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Audit không được chỉnh sửa.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-14-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Audit luôn được lưu vĩnh viễn theo chính sách lưu trữ của Platform.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-14-R017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Import luôn thực hiện: - Validation
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Import luôn thực hiện: - Dependency Check
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Import luôn thực hiện: - Conflict Check
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration phải được Validate trước khi Save và trước khi Publish.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-WS-14-R021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration không hợp lệ không được phép Publish.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-WS-14-R022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Rollback không được làm mất: - Audit
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-14-R023

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Rollback không được làm mất: - Version History
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R024

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Rollback không được làm mất: - Approval History
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R025

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Rollback luôn tạo một Version mới.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R026

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một số Configuration đặc biệt có thể yêu cầu Restart và phải được cảnh báo trước khi Publish.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-WS-14-R028

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không phải mọi Configuration đều được phép Override.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R029

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Configuration phải định nghĩa Capability Matrix.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R030

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Bao gồm: - Read - Create - Edit - Delete - Override - Clone - Import - Export - Approval Required - Runtime Reload Supported
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: capability_subject
- Semantic audit: `PASS`

### BRD-WS-14-R031

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nếu một Configuration thay đổi, hệ thống phải xác định toàn bộ các Configuration và Business Capability bị ảnh hưởng.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R032

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Scope thấp hơn có thể Override các thuộc tính được phép.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R033

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Các thuộc tính không được Override sẽ kế thừa.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R034

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Effective Configuration luôn được tính tại Runtime.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R035

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Scope thấp hơn có độ ưu tiên cao hơn.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R036

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Chỉ các thuộc tính được phép mới được Override.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R037

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Các thuộc tính khác kế thừa từ Scope phía trên.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-14-R038

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Nguyên tắc: - Effective Configuration luôn được tính tại Runtime.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-15-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: API Gateway là thành phần bắt buộc của Platform.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BRD-WS-15-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Kiến trúc hỗ trợ mở rộng thêm Gateway mới khi cần.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-15-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một Event mới không được phép phá vỡ khả năng tương thích ngược (Backward Compatibility) nếu vẫn còn Subscriber sử dụng Version cũ.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-WS-15-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain không được tạo dữ liệu trùng khi nhận cùng một Request hoặc Event nhiều lần.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-WS-15-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Retry không được Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-15-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: DLQ phải lưu đầy đủ: - Message
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-15-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: DLQ phải lưu đầy đủ: - Event
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-WS-15-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: DLQ phải lưu đầy đủ: - Connector
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BRD-WS-15-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: DLQ phải lưu đầy đủ: - Error
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-15-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: DLQ phải lưu đầy đủ: - Retry History
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-15-R013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: DLQ phải lưu đầy đủ: - Failure Reason
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-15-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Callback luôn được: - Authenticate
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-15-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Callback luôn được: - Validate
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-15-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Callback luôn được: - Audit
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-15-R017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Callback luôn được: - Idempotent Check
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-15-R018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một API mới không được làm ảnh hưởng đến các Client đang sử dụng Version cũ.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BRD-WS-15-R019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Deprecation Policy phải được công bố trước khi loại bỏ một API Version.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BRD-WS-15-R020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain không cần biết Connector đang sử dụng Profile nào.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BRD-WS-15-R021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Scheduler luôn Publish Event.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-WS-15-R022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain không cần biết Event đến từ hệ thống nào.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### BRD-WS-15-R023

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Connector phải khai báo Capability.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BRD-WS-15-R024

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector chỉ được phép xử lý giao dịch khi ở trạng thái Active.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BRD-WS-15-R025

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain không cần biết Runtime Profile đang được sử dụng.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-15-R026

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: API Gateway là thành phần bắt buộc.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### BRD-WS-16-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Permission không được xác định chỉ dựa trên Role.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY, policy_name, policy_scopes
- Semantic audit: `PASS`

### BRD-WS-16-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Authorization phải hỗ trợ mở rộng để đáp ứng các mô hình phân quyền phức tạp trong tương lai.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### BRD-WS-16-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Permission không được Hard-code trong mã nguồn.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### BRD-WS-16-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không được Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-16-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Secret không được lưu dưới dạng Plain Text.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-16-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Audit Log chỉ được phép đọc.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-16-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không được phép chỉnh sửa hoặc xóa trực tiếp.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-16-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Privacy Protection tuân thủ Compliance Policy và Security Policy.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-16-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi đánh giá Permission đều phải đi qua Permission Evaluation Engine.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### BRD-WS-16-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Security Policy không được Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-16-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Identity Federation cho phép Organization sử dụng hệ thống Identity hiện có mà không cần tạo lại User trên YSim.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-16-R013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sau thời gian này: - Audit được Archive
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: data_subject, required_audit_fields, retention_period
- Semantic audit: `PASS`

### BRD-WS-16-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sau thời gian này: - Archive chỉ đọc
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: data_subject, retention_period
- Semantic audit: `PASS`

### BRD-WS-16-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sau thời gian này: - Không được chỉnh sửa
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-16-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sau thời gian này: - Không được xóa trực tiếp
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-17-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Personal Inbox là kênh bắt buộc.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-17-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Scheduler Trigger được cấu hình và có thể thay đổi mà không cần sửa mã nguồn.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-17-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Operation Retry chỉ được thực hiện bởi Operator có Permission phù hợp.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: allowed_actions, governed_resource, prohibited_actions
- Semantic audit: `PASS`

### BRD-WS-17-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Maintenance phải gửi Notification trước khi bắt đầu.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-17-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Critical Job luôn được ưu tiên.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-17-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Operational Audit tuân thủ Security Policy.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-17-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Audit không được phép chỉnh sửa.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-17-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Operation Policy không được Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-17-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Scheduler giúp tự động hóa quy trình nghiệp vụ mà không cần lập trình bổ sung.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-17-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization chỉ được xem các thông tin Monitoring được Platform chia sẻ theo Permission.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: actor_scope, policy_name
- Semantic audit: `PASS`

### BRD-WS-17-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Không cần Deploy lại hệ thống.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-17-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi thao tác yêu cầu: - Permission
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### BRD-WS-17-R017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi thao tác yêu cầu: - Audit
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-17-R018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi thao tác yêu cầu: - Runbook (nếu có)
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-17-R019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Replay giúp xử lý các trường hợp lỗi mà không cần viết Script hoặc thao tác trực tiếp trên Database.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-17-R020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Replay chỉ được thực hiện bởi Operator có Permission phù hợp.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: allowed_actions, governed_resource, prohibited_actions
- Semantic audit: `PASS`

### BRD-WS-17-R021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi thao tác đều: - Kiểm tra Permission
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### BRD-WS-17-R022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi thao tác đều: - Ghi Audit
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-17-R023

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi thao tác đều: - Tuân thủ Security Policy
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### BRD-WS-17-R026

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `HIGH`
- Profile/category: `ACP-OPERATION_OBSERVABILITY`
- Statement: Mọi tác vụ vận hành phải có khả năng quan sát được thông qua trạng thái, kết quả và tín hiệu vận hành phù hợp.
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "operation_subject": "Mọi tác vụ vận hành phải có khả năng quan sát được thông qua trạng thái, kết quả và tín hiệu vận hành phù hợp.",
  "required_signals": [
    "state",
    "outcome",
    "relevant operational signals"
  ],
  "required_states": [
    "running",
    "completed",
    "failed"
  ]
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Mọi tác vụ vận hành phải có khả năng quan sát được thông qua trạng thái, kết quả và tín hiệu vận hành phù hợp., given the operation changes from running to completed or failed, when observations are compared, then the terminal outcome and relevant signals remain attributable to the same operation.",
  "negative": "For Mọi tác vụ vận hành phải có khả năng quan sát được thông qua trạng thái, kết quả và tín hiệu vận hành phù hợp., given required state, outcome, or signal evidence is absent, when observability is verified, then a detectable failure identifies the missing evidence.",
  "positive": "Given Mọi tác vụ vận hành phải có khả năng quan sát được thông qua trạng thái, kết quả và tín hiệu vận hành phù hợp. is in running, completed, failed, when an operator inspects it, then the matching state, outcome, and state, outcome, relevant operational signals are observable."
}
```
- Semantic audit: `PASS`

### BRD-WS-17-R027

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi tác vụ vận hành phải tạo bằng chứng audit bất biến, gắn với actor, thời điểm, phạm vi và kết quả.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-17-R028

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi tác vụ vận hành phải được cấu hình bằng policy có version thay vì hard-code quyết định vận hành.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states
- Semantic audit: `PASS`

### BRD-WS-17-R030

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi tác vụ vận hành phải có contract cho phép tự động hóa có kiểm soát, permission và audit.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### BRD-WS-17-R031

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Operator không được thao tác trực tiếp trên hạ tầng khi Platform đã cung cấp thao tác tương ứng.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes
- Semantic audit: `PASS`

### CAP-EP-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability phản ánh năng lực của Platform.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-EP-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability độc lập với UI.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-EP-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability độc lập với Database.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-EP-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability độc lập với Source Code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-EP-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability được cấu hình thay vì Hard-code khi phù hợp.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-EP-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability hỗ trợ Multi-tenant.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### CAP-EP-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability hỗ trợ White-label.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### CAP-EP-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability hỗ trợ mở rộng theo Version.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### CAP-EP-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability Registry là Enterprise Capability Dictionary của YSim.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-P01

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability phản ánh năng lực nghiệp vụ hoặc nền tảng. Không phản ánh thiết kế kỹ thuật.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-P02

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Một Capability chỉ có một định nghĩa duy nhất. Không tồn tại nhiều Capability có cùng ý nghĩa.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-P03

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability ID là bất biến. Tên Capability có thể được cải tiến nhưng Capability ID không thay đổi.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-P04

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability phải có khả năng được cấu hình khi phù hợp. Không Hard-code nếu có thể cấu hình.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-P05

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability có thể được cấp quyền. Permission luôn tham chiếu Capability.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### CAP-P06

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability có thể được bật hoặc tắt thông qua Feature Flag hoặc Configuration.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-P07

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability có thể Publish hoặc Subscribe Business Event.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### CAP-P08

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability Registry là tài liệu nền tảng phục vụ Enterprise Architecture Governance. Mọi Capability mới phải trải qua: - Architecture Review - Approval - Versioning - Audit - Traceability
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: activation_condition, approval_outcomes, configuration_subject, lifecycle_states, required_audit_fields
- Semantic audit: `PASS`

### CAP-R01

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability phản ánh năng lực nghiệp vụ. Không phản ánh thiết kế kỹ thuật.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-R02

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mỗi Capability phải có ít nhất một Business Object chính.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-R03

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability ưu tiên Publish hoặc Subscribe Business Event.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### CAP-R04

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability phải ưu tiên Configuration thay vì Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-R05

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability được kiểm soát bởi Permission Model.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### CAP-R06

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability có khả năng bật/tắt thông qua Feature Flag.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### CAP-R07

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Capability có thể được: - kế thừa từ Parent Organization - Override bởi Organization - giới hạn theo Commercial Agreement - giới hạn theo Capability Policy
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-06-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sales Enablement là Domain độc lập với Product Domain và Commercial Domain.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-06-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Landing Page là Business Asset. Không thuộc Campaign.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-07-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Transaction Domain chỉ tham chiếu Master Object và Commercial Object thông qua Snapshot.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-09-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Inventory chỉ quản lý Product Item.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-09-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Portal là điểm truy cập thống nhất sau bán hàng.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-09-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: QR Code là Digital Asset có yêu cầu bảo mật cao.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-09-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Product Item là Digital Asset có Lifecycle và Traceability xuyên suốt hệ thống.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-10-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Financial Domain chỉ đọc Snapshot, không sửa Transaction.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-10-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi điều chỉnh tài chính đều được biểu diễn bằng FinancialEvent mới.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, producer
- Semantic audit: `PASS`

### EP-10-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Financial Visibility tuân thủ Distribution Hierarchy.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-10-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Money Flow độc lập với Product Flow.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-11-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Portal là điểm truy cập thống nhất trong toàn bộ Customer Lifecycle.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-11-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Identity và Customer Relationship được tách biệt.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-11-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Support Routing dựa trên Capability, không dựa trên cấu trúc tổ chức cố định.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-11-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Reference Data được quản lý tập trung.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-11-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Knowledge Management hỗ trợ tái sử dụng nội dung giữa KB, FAQ và Troubleshooting Wizard.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### EP-11-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customer Privacy tuân thủ Consent Based Data Access.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-11-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Feature Request là một phần của Customer Success Lifecycle.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-12-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Communication Platform độc lập với Business Domain.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-12-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain chỉ Publish Business Event.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EP-12-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Communication Matrix quyết định toàn bộ hành vi gửi Notification.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-12-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Personal Inbox là nơi lưu giữ Notification lâu dài.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-12-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Notification luôn hỗ trợ Localization và Auto Translation.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### EP-12-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Communication Platform hỗ trợ mở rộng Channel mà không thay đổi Business Logic.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### EP-12-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Message Queue và Channel Adapter là nền tảng mở rộng Performance.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_trace
- Semantic audit: `PASS`

### EP-13-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Dashboard là cửa ngõ truy cập nhanh tới Business Object. Mọi Widget đều hỗ trợ Drill-down tới dữ liệu chi tiết theo Permission.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### EP-13-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Reporting luôn sử dụng Snapshot. Snapshot là nguồn dữ liệu chuẩn cho: - Dashboard - KPI - Report - Analytics - Business Intelligence
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-13-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Widget là Platform Capability. Widget không thuộc Dashboard. Một Widget có thể tái sử dụng trên nhiều Portal và Workspace.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-13-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Analytics phục vụ Decision Making. Dashboard không chỉ hiển thị dữ liệu mà còn hỗ trợ phát hiện bất thường và đề xuất hành động.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### EP-13-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Report, Dashboard và Widget đều được quản lý theo mô hình Configuration. Organization có thể Enable, Disable hoặc Override theo Permission.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY, approval_outcomes, authorized_approver_scope, policy_name, policy_scopes, policy_set, precedence_order
- Semantic audit: `PASS`

### EP-13-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Localization được áp dụng xuyên suốt: - Dashboard - Report - Widget - Analytics Bao gồm: - Currency - Language - Measurement - Temperature - Date Time Format
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### EP-13-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Operational Intelligence và Business Intelligence phải phục vụ trực tiếp cho việc vận hành Platform và hỗ trợ ra quyết định.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: capability_subject, required_capabilities
- Semantic audit: `PASS`

### EP-14-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration over Customization là nguyên tắc cốt lõi của Platform.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-14-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Toàn bộ Business Domain ưu tiên Configuration trước khi Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-14-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Reference Data là nguồn dữ liệu chuẩn của toàn Platform.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-14-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Rule được cấu hình, không Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-14-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Metadata điều khiển Dynamic Form, Dynamic API, Validation và Reporting.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### EP-14-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration luôn có: - Version - Approval - Audit
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: approval_outcomes, lifecycle_states, required_audit_fields
- Semantic audit: `PASS`

### EP-14-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Configuration hỗ trợ Runtime Reload.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### EP-14-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization được khởi tạo bằng Template nhằm giảm thời gian Onboarding.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-15-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain không được tích hợp trực tiếp với hệ thống bên ngoài.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-15-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Toàn bộ Integration phải đi qua Gateway, Connector và Adapter.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### EP-15-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain chỉ sử dụng Canonical Data Model.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: allowed_values, dependent_fields, enum_field, prohibited_reference_states, reference_registry
- Semantic audit: `PASS`

### EP-15-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain chỉ sử dụng Canonical Event Model.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EP-15-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Toàn Platform giao tiếp nội bộ theo Event-Driven Architecture.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EP-15-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi Business Domain đều Publish Business Event.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EP-15-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector Policy được cấu hình. Không Hard-code.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### EP-15-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector được lựa chọn bằng Routing Rule.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### EP-15-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Integration Platform phải hỗ trợ Runtime Profile.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### EP-16-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Identity không phụ thuộc User. Một Identity có thể được sử dụng cho: - Customer - User - Organization Owner - API Client - Service Account
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### EP-16-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Permission được đánh giá động. Không sử dụng Permission tĩnh.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### EP-16-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Permission Evaluation Engine là điểm đánh giá Permission duy nhất. Business Domain không tự xử lý Permission.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY
- Semantic audit: `PASS`

### EP-16-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Security Policy được cấu hình. Không Hard-code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-16-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform áp dụng Zero Trust Principle. Không có Request nào được mặc định tin cậy.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-16-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Data Protection được quyết định bởi: - Permission - Data Scope - Data Classification - Customer Consent - Security Policy
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-16-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: API Security độc lập với Portal Security.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-16-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Toàn bộ truy cập dữ liệu và chức năng đều phải được đánh giá động dựa trên: - Identity - Role - Permission - Data Scope - Organization Relationship - Support Policy - Customer Consent - Data Classification - Security Policy
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-17-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform Operations được quản lý tập trung thông qua Platform Operations Center.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-17-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Monitoring phải bao phủ toàn Platform.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-17-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Scheduler, Queue, Worker, Alert và Runbook đều là Business Object.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### EP-17-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Operation Policy được cấu hình. Không Hard-code.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states
- Semantic audit: `PASS`

### EP-17-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Platform hỗ trợ Feature Flag và Kill Switch. Không cần Deploy để bật hoặc tắt chức năng.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### EP-17-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi thao tác Operations đều phải: - Kiểm tra Permission - Ghi Audit - Tuân thủ Runbook (nếu có)
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: EXPLICIT_ALLOWED_AND_PROHIBITED_BOUNDARY, required_audit_fields
- Semantic audit: `PASS`

### EVT-C01

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain chỉ Publish Canonical Event.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-C02

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Connector chịu trách nhiệm chuyển đổi giữa: - External Event - Canonical Event
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer, provider
- Semantic audit: `PASS`

### EVT-C03

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain không phụ thuộc định dạng Event của đối tác.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-C04

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Canonical Event được Version độc lập.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-C05

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Canonical Event là Contract giữa các Domain.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-C06

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event ưu tiên tái sử dụng Canonical Vocabulary.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-EP-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event phản ánh sự kiện đã xảy ra.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-EP-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event là Immutable.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-EP-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event độc lập với Database.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-EP-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event độc lập với UI.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-EP-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event độc lập với Connector.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: TWO_EXPLICIT_INDEPENDENT_ENTITIES, consumer, delivery_outcome, event_name, producer, provider
- Semantic audit: `PASS`

### EVT-EP-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event sử dụng Canonical Event Model.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-EP-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event ưu tiên Asynchronous Processing.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-EP-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event hỗ trợ Versioning.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer, required_capabilities
- Semantic audit: `PASS`

### EVT-EP-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event hỗ trợ Replay theo Policy.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer, required_capabilities
- Semantic audit: `PASS`

### EVT-EP-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event Registry là Enterprise Event Dictionary của YSim.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-P01

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event là bất biến. Sau khi Publish không được sửa.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-P02

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event phản ánh sự kiện nghiệp vụ. Không phản ánh kỹ thuật.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-P03

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Domain giao tiếp thông qua Business Event. Ưu tiên Loose Coupling.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer
- Semantic audit: `PASS`

### EVT-P04

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event hỗ trợ Version. Không thay đổi Contract cũ.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer, required_capabilities
- Semantic audit: `PASS`

### EVT-P05

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event hỗ trợ Replay nếu Policy cho phép.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer, required_capabilities
- Semantic audit: `PASS`

### EVT-P06

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event phải có khả năng: - Monitoring - Logging - Tracing - Auditing
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer, required_audit_fields
- Semantic audit: `PASS`

### EVT-P07

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event ưu tiên sử dụng Canonical Event Model. Không phụ thuộc Connector cụ thể.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, delivery_outcome, event_name, producer, provider
- Semantic audit: `PASS`

### EVT-P08

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Event Registry là tài liệu nền tảng phục vụ Enterprise Event Governance. Mọi Event mới phải được: - Architecture Review - Approval - Versioning - Audit - Traceability
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: activation_condition, approval_outcomes, configuration_subject, consumer, delivery_outcome, event_name, lifecycle_states, producer, required_audit_fields
- Semantic audit: `PASS`

### POL-EP-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy phản ánh quyết định nghiệp vụ.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### POL-EP-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy độc lập với Source Code.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### POL-EP-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy độc lập với Database.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### POL-EP-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy ưu tiên Configuration.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### POL-EP-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy hỗ trợ Runtime Reload.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### POL-EP-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy hỗ trợ Versioning.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### POL-EP-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy hỗ trợ Inheritance.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### POL-EP-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy được Policy Decision Engine đánh giá trước khi Capability được thực thi.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### POL-EP-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Enterprise Policy Registry là Enterprise Policy Dictionary của nền tảng YSim.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### POL-P01

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy ưu tiên được cấu hình. Không Hard-code khi có thể cấu hình.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### POL-P02

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy ưu tiên kế thừa. Chỉ Override khi thực sự cần thiết.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### POL-P03

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy luôn hỗ trợ Version.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### POL-P04

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy hỗ trợ Effective Date.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### POL-P05

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy chỉ có hiệu lực sau Approval.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### POL-P06

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Mọi thay đổi Policy phải được Audit.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### POL-P07

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy được Runtime Engine sử dụng trực tiếp.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### POL-P08

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy phản ánh quyết định nghiệp vụ. Không phản ánh thiết kế kỹ thuật.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### POL-P09

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Policy phải có cơ chế xử lý xung đột giữa các Scope.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### POL-P10

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Enterprise Policy Registry là tài liệu nền tảng phục vụ Enterprise Policy Governance. Mọi Policy mới phải trải qua: - Architecture Review - Approval - Versioning - Audit - Traceability
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: activation_condition, approval_outcomes, configuration_subject, lifecycle_states, required_audit_fields
- Semantic audit: `PASS`

### SNP-EP-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot là Business Evidence.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### SNP-EP-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot là Immutable.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### SNP-EP-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot được tạo từ Business Event hoặc Business State Transition.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### SNP-EP-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot phải chứa đầy đủ Business Context để tái hiện quyết định nghiệp vụ.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### SNP-EP-005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot độc lập với Runtime Database.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: TWO_EXPLICIT_INDEPENDENT_ENTITIES
- Semantic audit: `PASS`

### SNP-EP-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot hỗ trợ Versioning.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### SNP-EP-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Enterprise Snapshot Registry là Enterprise Snapshot Dictionary của nền tảng YSim.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### SNP-P01

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot là bất biến.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### SNP-P02

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot là bằng chứng nghiệp vụ.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### SNP-P03

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot hỗ trợ Version.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### SNP-P04

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot được tạo từ Business Event.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### SNP-P05

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot hỗ trợ Trace đầy đủ.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### SNP-P06

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot hỗ trợ Audit.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields, required_capabilities
- Semantic audit: `PASS`

### SNP-P07

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Snapshot chịu sự điều khiển của Retention Policy và Security Policy.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### SNP-P08

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Enterprise Snapshot Registry là tài liệu nền tảng phục vụ Snapshot Governance. Mọi Snapshot mới phải trải qua: - Architecture Review - Approval - Versioning - Traceability
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every Storefront must be connected to business capabilities.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Without valid business bindings a Storefront **cannot be published**.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Storefronts never communicate with suppliers directly.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier products are never exposed to: - Storefront
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier products are never exposed to: - Portal
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier products are never exposed to: - Customer
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier products are never exposed to: - Agency
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier products are never exposed to: - Reseller
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Each level only overrides the required configuration.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every runtime configuration must support fallback.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: If a configuration cannot be resolved, the runtime automatically falls back to the nearest valid parent configuration.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: No runtime request should fail solely because a child configuration is incomplete.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: All applications must reuse the same component library.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: UI duplication is prohibited.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: White-label configuration must not require source-code modification.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states
- Semantic audit: `PASS`

### UXF-00-R017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Runtime rendering must use immutable published configurations.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: available_actions, fallback_outcome
- Semantic audit: `PASS`

### UXF-00-R018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The runtime never renders directly from editable configurations.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: fallback_outcome
- Semantic audit: `PASS`

### UXF-00-R019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime must provide: - Dynamic Rendering
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: available_actions, fallback_outcome
- Semantic audit: `PASS`

### UXF-00-R020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime must provide: - White-label Support
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime must provide: - Multi-tenant Isolation
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime must provide: - Localization
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R023

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime must provide: - Runtime Resolution
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R024

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime must provide: - Experience Inheritance
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R025

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime must provide: - Safe Fallback
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R026

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime must provide: - Versioning
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R027

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime must provide: - Preview
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R028

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime must provide: - Publish
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R029

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime must provide: - Rollback
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-00-R030

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime must provide: - Auditability
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_audit_fields
- Semantic audit: `PASS`

### UXF-00-R031

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The following principles are mandatory.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Experience is resolved at runtime.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Storefronts represent commercial experiences rather than websites.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Storefronts consume YSim Products only.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier systems are internal infrastructure.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: allowed_disclosure, budget, channel, measurement_condition, metric, prohibited_fields
- Semantic audit: `PASS`

### UXF-006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every runtime configuration supports inheritance.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### UXF-007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every runtime configuration supports fallback.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### UXF-008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Localization defines customer experience, not only language.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Tracking participates in experience generation.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-01-R001

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `CRITICAL`
- Profile/category: `ACP-AUTHENTICATION_REQUIREMENT`
- Statement: Platform Administration Portal requires authentication.
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "assurance_requirement": "Platform Administration Portal requires authentication.",
  "principal_type": "Admin",
  "protected_action": "Platform Administration Portal requires authentication."
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For Admin, given assurance cannot be resolved or has expired, when authentication is evaluated, then no previous success is reused outside its validity boundary.",
  "negative": "Given missing or invalid assurance evidence, when Platform Administration Portal requires authentication. is attempted, then authentication is denied or challenged without granting the protected action.",
  "positive": "Given Admin presents evidence satisfying Platform Administration Portal requires authentication., when Platform Administration Portal requires authentication. is attempted, then authentication succeeds at the bound assurance level."
}
```
- Semantic audit: `PASS`

### UXF-01-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organization Portal requires authentication.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: policy_name, policy_scopes, principal_type
- Semantic audit: `PASS`

### UXF-01-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Agency Portal requires authentication.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: principal_type
- Semantic audit: `PASS`

### UXF-01-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Authentication: Optional or Required depending on Storefront Policy
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: principal_type
- Semantic audit: `PASS`

### UXF-01-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customers never interact with suppliers.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-01-R006

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `HIGH`
- Profile/category: `ACP-UX_ACCESSIBILITY`
- Statement: Every experience should support: - Keyboard navigation
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "accessibility_capability": "Keyboard",
  "affected_content_or_action": "Every experience should support: - Keyboard navigation",
  "ux_surface": "12. Accessibility"
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For 12. Accessibility, given fallback content or an unavailable primary interaction, when the accessible alternative applies, then the alternative is perceivable, operable, and exposes the same required outcome.",
  "negative": "For 12. Accessibility, given the accessibility capability is absent or broken, when the affected interaction is tested, then conformance fails with the inaccessible content or action identified.",
  "positive": "Given Keyboard is enabled on 12. Accessibility, when Every experience should support: - Keyboard navigation is rendered or used, then the bound content remains perceivable and the action remains operable."
}
```
- Semantic audit: `PASS`

### UXF-01-R007

- Mechanism: `PROFILE_BINDING_HIGH_CONFIDENCE`
- Criticality: `HIGH`
- Profile/category: `ACP-UX_ACCESSIBILITY`
- Statement: Every experience should support: - Screen readers
- Rationale: Type compatibility, semantic structure, complete source-grounded bindings, and all three rendered-oracle audits passed; keyword presence alone was not sufficient.
- Concrete bindings:

```json
{
  "accessibility_capability": "Screen Reader",
  "affected_content_or_action": "Every experience should support: - Screen readers",
  "ux_surface": "12. Accessibility"
}
```
- Rendered contract:

```json
{
  "edge_boundary": "For 12. Accessibility, given fallback content or an unavailable primary interaction, when the accessible alternative applies, then the alternative is perceivable, operable, and exposes the same required outcome.",
  "negative": "For 12. Accessibility, given the accessibility capability is absent or broken, when the affected interaction is tested, then conformance fails with the inaccessible content or action identified.",
  "positive": "Given Screen Reader is enabled on 12. Accessibility, when Every experience should support: - Screen readers is rendered or used, then the bound content remains perceivable and the action remains operable."
}
```
- Semantic audit: `PASS`

### UXF-01-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every experience should support: - Responsive layouts
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-01-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every experience should support: - Touch interaction
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: available_actions, fallback_outcome
- Semantic audit: `PASS`

### UXF-01-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every experience should support: - Mobile-first behavior
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every published storefront must pass business binding validation.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Runtime rendering must use published snapshots.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Design System components are shared across every portal.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-02-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Each level overrides only required properties.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-02-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: If a configuration cannot be resolved, runtime falls back to the nearest valid parent.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-02-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every component must support: - Responsive Layout
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-02-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every component must support: - Focus Indicators
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-02-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every component must support: - Touch Interaction
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: available_actions, fallback_outcome
- Semantic audit: `PASS`

### UXF-02-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Accessibility cannot be disabled by Themes.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: accessibility_capability, affected_content_or_action
- Semantic audit: `PASS`

### UXF-03-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Templates never contain business data.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-03-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Widgets never query suppliers directly.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-03-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Components never depend on: - Supplier
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-03-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Components never depend on: - Database
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-03-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Components never depend on: - External APIs
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### UXF-03-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Drag-and-drop editing is not required for MVP.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-03-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Navigation is never hardcoded.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: available_actions, fallback_outcome
- Semantic audit: `PASS`

### UXF-04-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The YSim Platform never renders pages directly.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: available_actions, fallback_outcome
- Semantic audit: `PASS`

### UXF-04-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: URL Resolution never bypasses Storefront configuration.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-04-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Tracking must never bypass business policies.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-04-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Identity never changes published business rules.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-04-R005

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Feature Flags never replace authorization.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-04-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: White-label configuration must not require source-code modification.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states
- Semantic audit: `PASS`

### UXF-04-R008

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Editable configurations are never cached directly.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-04-R009

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Runtime Resolution Engine must: - validate domain ownership
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-04-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Runtime Resolution Engine must: - validate organization ownership
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-04-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Runtime Resolution Engine must: - validate storefront publication status
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-04-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Runtime Resolution Engine must: - validate localization
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-04-R013

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Runtime Resolution Engine must: - validate feature flags
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-04-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Runtime Resolution Engine must: - validate runtime policies
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R001

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Experience Runtime never performs business decisions.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: budget, measurement_condition, metric
- Semantic audit: `PASS`

### UXF-05-R002

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: The Commerce Runtime never renders UI.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: available_actions, fallback_outcome
- Semantic audit: `PASS`

### UXF-05-R003

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Infrastructure never communicates directly with Storefront UI.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R004

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Storefronts never own: - Products
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R006

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Storefronts never own: - Supplier
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R007

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Storefronts never own: - Inventory
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R010

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: The UI never queries business objects directly.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R011

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Widgets never access databases.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R012

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Widgets never call suppliers.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R014

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier objects are prohibited from appearing inside: - Storefront
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R015

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier objects are prohibited from appearing inside: - Components
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R016

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier objects are prohibited from appearing inside: - Widgets
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R017

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier objects are prohibited from appearing inside: - Pages
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R018

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier objects are prohibited from appearing inside: - Catalog
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R019

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier objects are prohibited from appearing inside: - Checkout
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R020

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Editable configuration never participates directly.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R021

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: If runtime cannot resolve a binding: ``` Runtime
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-05-R022

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Rendering should continue whenever possible.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: available_actions, fallback_outcome
- Semantic audit: `PASS`

### UXF-05-R037

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Examples include: - Recommendation engines
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: QUALIFIER_PRESERVATION_REQUIRES_REVIEW
- Semantic audit: `PASS`

### UXF-101

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Experience is channel-specific.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-102

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Navigation is capability-driven.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: available_actions, fallback_outcome
- Semantic audit: `PASS`

### UXF-103

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Menus are resolved dynamically.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-104

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Experience inherits from parent configurations.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-105

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Customers never interact directly with suppliers.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-107

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every channel shares the same design system.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-108

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every navigation tree supports localization.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: available_actions, fallback_outcome, required_capabilities
- Semantic audit: `PASS`

### UXF-109

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Experience must remain consistent across Portal, Storefront and APIs.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### UXF-110

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business capabilities remain independent from presentation contracts.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-201

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: One platform uses one Design System.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-202

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Themes are versioned configuration objects rather than source-code variants.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states
- Semantic audit: `PASS`

### UXF-203

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Experience Profiles extend Themes through governed configuration.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states
- Semantic audit: `PASS`

### UXF-204

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Theme inheritance resolves deterministically through the approved configuration hierarchy.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states
- Semantic audit: `PASS`

### UXF-205

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every configurable property supports fallback.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### UXF-206

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Assets participate in runtime resolution.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-207

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Component libraries are shared across all applications.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-208

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business behavior remains independent from presentation composition.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-209

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Accessibility is mandatory.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: accessibility_capability, affected_content_or_action
- Semantic audit: `PASS`

### UXF-210

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Responsive behavior is defined by Design Tokens.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-301

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Storefronts are runtime experiences.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-302

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Templates define structure only.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-303

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Layouts are reusable.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-304

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Pages are configuration driven.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-305

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Sections are independently configurable.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-306

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Widgets bind to platform capabilities.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-307

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Storefronts never communicate with suppliers.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-308

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Published snapshots are immutable.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-309

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Preview is isolated from production.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-310

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every storefront is composed from reusable components.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-401

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every request is resolved through Runtime Context Resolution.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-402

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Domains determine storefront identity.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-403

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Tracking participates in runtime experience generation.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-404

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Localization defines commercial experience.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-405

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Storefronts inherit Organization configuration.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-406

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Organizations inherit Platform configuration.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-407

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Every configuration supports fallback.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### UXF-408

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: White-label configuration requires no source-code changes.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: lifecycle_states
- Semantic audit: `PASS`

### UXF-409

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Only published configurations participate in runtime rendering.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: available_actions, fallback_outcome
- Semantic audit: `PASS`

### UXF-410

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Supplier systems never participate in Experience Resolution.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: budget, measurement_condition, metric
- Semantic audit: `PASS`

### UXF-501

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `NORMAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Experience Runtime owns presentation while business domains retain ownership of business behavior.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-502

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Commerce Runtime owns business capabilities.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-503

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Infrastructure Runtime owns integrations.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: consumer, provider
- Semantic audit: `PASS`

### UXF-504

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Binding connects Experience with Commerce.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-505

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Storefronts never know suppliers.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-507

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Configuration supports inheritance.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### UXF-508

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Business Configuration supports fallback.
- Rationale: Potential profile semantics found, but required bindings are absent or not deterministically extractable: required_capabilities
- Semantic audit: `PASS`

### UXF-509

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `CRITICAL`
- Profile/category: `HUMAN_REVIEW`
- Statement: Published snapshots are immutable.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`

### UXF-510

- Mechanism: `HUMAN_MAPPING_REVIEW`
- Criticality: `HIGH`
- Profile/category: `HUMAN_REVIEW`
- Statement: Experience Runtime and Commerce Runtime remain independent.
- Rationale: No narrow profile passed type, structural-semantic, binding, and oracle checks; no fallback prose was generated.
- Semantic audit: `PASS`
