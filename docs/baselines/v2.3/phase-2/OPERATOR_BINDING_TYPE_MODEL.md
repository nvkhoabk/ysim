# Phase 2C Operator Binding Business-Semantic Type Model C1

- Candidate: `V23-P2C-OPERATOR-BINDING-TYPE-MODEL-C1`
- Status: `CANDIDATE`
- Approval: `PENDING_HUMAN_APPROVAL`
- Next gate: `HUMAN_OPERATOR_BINDING_TYPE_MODEL_AND_SOURCE_CLARIFICATION_APPROVAL`

Natural-language predicates, labels and complete requirement statements are not typed values.

## Type catalog

- Named semantic types: 39
- Generic types: `SET_OF<T>`, `CANONICAL_SET_REF<T>`, `RUNTIME_SET_REF<T>`
- Expected and observed origin IDs and resolvers must be independent.

## Operator schemas

- Complete schemas: 40/40
- Each schema declares semantic types, cardinality, origins, resolvers, evidence, invariants and evaluator consumption.

## Read-only C3-R1 reassessment

- Records: 59
- COMPOUND_AST_REQUIRED: 6
- CORRECTABLE_WITH_APPROVED_TYPE_MODEL: 35
- OPERATOR_REMAP_REQUIRED: 12
- SOURCE_CLARIFICATION_REQUIRED: 6

## Non-claims

- Does not regenerate custom ASTs or fixtures.
- Does not modify BRD/UXF.
- Does not claim runtime evidence or runtime mutation coverage.
- Does not approve the final document baseline, runtime adapters or YADF implementation.
