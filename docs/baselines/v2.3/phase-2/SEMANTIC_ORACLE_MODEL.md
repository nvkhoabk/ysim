# Semantic Oracle Model C2

- Candidate: `V23-P2C-SEMANTIC-ORACLE-MODEL-C2`
- Supersedes: `V23-P2C-SEMANTIC-ORACLE-MODEL-C1`
- Reason: `NON_EXECUTABLE_METADATA_DERIVED_MUTATION_RESULTS`
- Status: `CANDIDATE`
- Approval: `PENDING_HUMAN_APPROVAL`
- Approval scope: `EXECUTABLE_SEMANTIC_ORACLE_ENGINE_OPERATOR_CATALOG_AND_REFERENCE_EVALUATION_MODEL`
- Blocker: `SEMANTIC_ORACLE_MODEL_NOT_APPROVED`
- Next gate: `HUMAN_SEMANTIC_ORACLE_MODEL_C2_APPROVAL`

The engine evaluates structured fixtures through a closed evaluator registry, applies mutations to exact targets, hashes original and mutant states, and derives `actual_detection` only from baseline and mutant execution. Model conformance is not a product-runtime claim.

Non-claims: the 27 human mapping decisions, 59 custom AST candidates, 48 reusable high-risk candidates, BRD/UXF acceptance materialization, final document baseline, and YADF implementation are not approved.
