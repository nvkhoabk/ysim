# Semantic Acceptance Renderer C2

- Candidate: `V23-P2C-SEMANTIC-ACCEPTANCE-RENDERER-C2`
- Supersedes: `V23-P2C-SEMANTIC-ACCEPTANCE-RENDERER-C1`
- Reason: `REFERENCE_GOOD_HASH_LOCK_CONTAINED_OPAQUE_ORIGIN_IDENTIFIERS`
- Status: `CANDIDATE`
- Approval: `PENDING_HUMAN_APPROVAL`
- Scope: `ELEVEN_TYPED_CUSTOM_CONTRACT_ORIGIN_NORMALIZATIONS_ONLY`
- Next gate: `HUMAN_PHASE_2C_SEMANTIC_ACCEPTANCE_RENDERER_C2_APPROVAL`

C2 corrects only eleven nested origin identifiers in typed custom contracts. The 937 AST/decision previews, 156 procedures, and the other 48 typed custom contracts remain byte-identical to accepted Renderer C1. The correction changes no business obligation, operator composition, oracle prose, evidence contract, BRD/UXF source, or runtime claim.

Renderer C1's `opaque identifiers = 0` result was a false negative: its audit did not descend through every typed custom binding and model fixture.

## Non-claims

- No C6 or C6-R1 document baseline is created or approved.
- No BRD/UXF source is modified.
- No runtime adapter, runtime mutation score, YADF, production implementation, commit, tag, push or approval is authorized.
