# 021-R-C — Evidence Dependency Graph, Invalidation, Content Equivalence & Evidence Reuse

## Status

**COMPLETE — PASS.**

021-R-C converts Phase-020 exact-revision evidence rules and the Phase-021 rebinding experience into a deterministic evidence-dependency model. It answers a narrow question:

> When a revision, authority record, evaluator, or integration identity changes, exactly which evidence remains valid, which evidence requires review/rebinding, and which evidence must be rerun?

It does not authorize implementation, merge, release, production, or Phase 022.

Machine projection: `docs/routing/autonomy_evidence_dependency_contract.json`.

## Governing rules retained

R-C specializes existing authority; it does not replace it.

| Contract | Rule preserved |
|---|---|
| **020-F implementation contract** | visible criteria identify material boundaries and evidence floors; stronger evidence cannot substitute for weaker evidence unless it exercises the same claim boundary |
| **020-G exact-revision evidence** | evidence names exact SHA/tree; changed trees require affected evidence reconsideration; proven content equivalence may allow reuse |
| **020-H review/repair/exit** | source change invalidates affected approval; G5 is immutable; integration differences are classified; post-completion invalidation creates reopen obligations |
| **021-R-B orchestrator** | head drift cannot advance state until materiality/evidence impact is classified; unknown materiality fails closed |

## Core principle: reuse by reference, never by relabeling

An evidence record is permanently attached to the revision/material boundary it actually evaluated.

If later revision `B` is proven equivalent to earlier revision `A` for a particular claim, the system creates:

1. an **equivalence proof** describing what was compared;
2. a new **binding record** for `B` that references the immutable evidence for `A`; and
3. any required new delta review / gate binding.

The old record is never edited so that it appears to have evaluated `B`.

This preserves exact-SHA provenance while avoiding unnecessary full reruns.

## Graph model

The evidence graph is an append-only directed validation graph.

Principal node types:

- `AUTHORITY`
- `SOURCE_SURFACE`
- `MATERIAL_SURFACE`
- `VISIBLE_CRITERION`
- `EVIDENCE_OBLIGATION`
- `VERIFICATION_RESULT`
- `INDEPENDENT_REVIEW`
- `ADVERSARIAL_REVIEW`
- `CI_CHECK`
- `EQUIVALENCE_PROOF`
- `BINDING`
- `GATE_DECISION`
- `CANDIDATE_IDENTITY`
- `INTEGRATION_IDENTITY`
- `FINDING`
- `RESIDUAL_RISK`
- `REOPEN_RECORD`
- `CLOSURE_RECORD`

Principal edge semantics:

- `DEPENDS_ON`
- `PROVES`
- `BOUND_TO`
- `INVALIDATES_ON_CHANGE`
- `REQUIRES_REVIEW_IF_CHANGED`
- `CARRIES_FORWARD_IF_EQUIVALENT`
- `SUPERSEDES`
- `DERIVED_FROM`
- `CLOSES`

The validation dependency subgraph must be acyclic. Historical supersession links may refer backward in time but do not create a validation cycle.

## Material-surface manifest

Every implementation package must define its material-surface manifest before G2.

A material surface is not merely a file list. It states:

- stable `surface_id`;
- class;
- path/object selectors;
- visible criteria affected;
- evidence obligations affected;
- change effect;
- allowed equivalence method;
- owner; and
- whether the surface is serialized/shared.

Supported selector forms include:

- exact path;
- path prefix;
- glob;
- Git tree;
- generated inventory; and
- external definition identity.

Hashing/comparison considers path plus Git object/content identity and, where material, file mode or symlink target.

### Fail-closed mapping rule

Every changed path/object must map to at least one declared surface.

An unmatched or ambiguously classified changed path results in `INCONCLUSIVE`; it cannot be silently treated as non-material.

When multiple surface classes overlap, the most restrictive change effect wins unless an explicit rule resolves the overlap.

## Material classes

### `EXECUTABLE_MATERIAL`

Examples:

- application/module source;
- dependency rules;
- manifests/lockfile;
- runtime/build configuration;
- migrations.

Default effect: invalidate the transitive affected verification/review/CI/G5 closure.

### `AUTHORITY_GOVERNANCE_MATERIAL`

Examples:

- G2/scope record;
- lifecycle profile;
- review/gate contract;
- validator defining acceptance.

Executable evidence may remain reusable only if executable/evaluator material is equivalent **and** independent review establishes that the authority meaning was not expanded or weakened.

### `CI_EVALUATOR_MATERIAL`

Examples:

- workflows;
- test harnesses;
- protected evaluators;
- scanner policy;
- evidence collector.

Changing evaluator material invalidates affected evaluator evidence even when application source is unchanged.

### `EVIDENCE_ONLY`

Examples:

- append-only review result;
- run reference;
- equivalence proof;
- integration binding;
- closure evidence.

Ordinary append-only evidence additions do not invalidate implementation acceptance, but provenance/integrity must remain valid.

### `ROUTING_PROJECTION`

Indexes/status projections normally have no acceptance effect unless the change modifies authority resolution or validator input.

### `HISTORICAL_NONCURRENT`

Historical records have no current acceptance effect unless current authority explicitly depends on them. Rewriting historical evidence remains prohibited.

## Evidence node validity states

An evidence node projects to one of:

- `VALID_EXACT`
- `VALID_REUSED_BY_EQUIVALENCE`
- `STALE_BINDING`
- `REVIEW_REQUIRED`
- `INVALIDATED`
- `BLOCKED`
- `INCONCLUSIVE`
- `SUPERSEDED_HISTORICAL`

These are projections from immutable records; they are not mutable truth stored back into old evidence.

## Revision classification algorithm

For any old/new revision pair:

1. establish old/new commit and tree SHA;
2. establish merge-base or other declared relationship;
3. compute the complete changed path/object set;
4. map every changed item to declared material surfaces;
5. fail closed if anything is unmapped/ambiguous;
6. compare material-surface manifests/hashes;
7. classify authority/evaluator semantic deltas where relevant;
8. seed evidence effects from changed-surface rules;
9. compute the transitive invalidation/review closure;
10. create equivalence proof(s) for every reused node;
11. create new binding node(s) for the new revision; and
12. leave every original evidence record unchanged.

## Revision classes

| Class | Meaning | Default action |
|---|---|---|
| `IDENTICAL_REVISION` | same commit | none |
| `PROVENANCE_ONLY_CHANGE` | new commit, identical tree | new exact-head/integration binding where required |
| `NON_MATERIAL_TREE_CHANGE` | changed tree but all acceptance material proven equivalent | delta proof + binding refresh |
| `GOVERNANCE_MATERIAL_DELTA` | authority/validator changes, executable/evaluator material equal | independent authority delta review + adversarial delta review + gate rebinding |
| `EVALUATOR_MATERIAL_DELTA` | evaluator/CI semantics changed | rerun affected evaluator evidence and review evaluator integrity |
| `EXECUTABLE_MATERIAL_DELTA` | executable material changed | invalidate affected closure and return to earliest required stage |
| `MIXED_MATERIAL_DELTA` | multiple material classes changed | union of effects; most restrictive rule wins |
| `INCONCLUSIVE` | classification/equivalence cannot be proven | fail closed |

## Content-equivalence proof levels

Preferred strongest-to-weakest proof order:

1. `FULL_TREE_IDENTITY`
2. `DECLARED_SURFACE_OBJECT_IDENTITY`
3. `DECLARED_SURFACE_CONTENT_DIGEST_IDENTITY`
4. `SEMANTIC_EQUIVALENCE_WITH_INDEPENDENT_REVIEW`

Semantic equivalence is not self-asserting.

A prose statement that “nothing material changed” is not sufficient. A proof must name old/new revisions, compared surfaces, method, complete changed-path set, unmapped paths, result, review references when semantic, and a proof digest.

PASS requires zero unmapped paths.

## Minimal reverification closure

R-C defines a deterministic minimal closure algorithm.

```text
changed material surfaces
        ↓
seed direct invalidation/review edges
        ↓
reverse-traverse DEPENDS_ON consumers
        ↓
stop only where a valid equivalence proof satisfies
CARRIES_FORWARD_IF_EQUIVALENT
        ↓
create new BINDING nodes for every reused result
        ↓
include revision-specific G5/integration bindings
        ↓
return earliest R-B lifecycle state required
by remaining invalid/review-required nodes
```

This makes **full rerun non-default**, but does not allow under-verification.

If the graph is incomplete or a dependency path is unknown, the result is `INCONCLUSIVE`, not optimistic reuse.

A minimal rerun may never weaken the visible evidence floor defined by 020-F.

## Criterion/evidence mapping

Before G2:

- every visible criterion maps to one or more material boundaries;
- every required criterion maps to at least one required evidence obligation;
- every evidence obligation declares an E1–E7 evidence class;
- every evidence obligation maps to the material boundary it proves;
- package-specific mapping is complete enough to calculate invalidation.

This is the prerequisite that makes selective invalidation safe.

## Review, CI, G5 and integration effects

### Independent review

A review becomes invalid for the changed revision when a material dependency it reviewed changes, unless the graph proves that dependency unaffected/equivalent.

### Adversarial review

Same rule as independent review, plus any required adversarial delta review must be a fresh session/run.

### CI

A CI result depends both on its subject material and the workflow/evaluator definition that produced it. Changing either can invalidate the result.

### G5

Historical G5 is immutable.

A different candidate SHA/tree intended for merge requires a new exact-head binding or a new G5 cycle, according to the calculated invalidation closure. Old G5 is never silently retargeted.

### Integration

Every merge creates a distinct `INTEGRATION_IDENTITY`. It receives a material-difference classification even when tree-equivalent to the approved candidate.

### Reopen

Post-completion invalidation adds an immutable `REOPEN_RECORD`; it does not edit or erase the completion record.

## Candidate generations

Candidate generations are monotonic.

A repair that changes source creates a new candidate generation.

Evidence records must name generation plus SHA/tree. Failed, blocked, inconclusive, superseded, and passing attempts remain retained.

## Phase-021 replay oracle

The actual IMP-001 history is retained as the first shadow-test oracle.

### Case 1 — original → repaired candidate

`dc8d4dd… → 1c36dbed…`

Expected classification:

`EXECUTABLE_MATERIAL_DELTA`

Expected effects:

- new generation;
- affected verification rerun;
- fresh independent review;
- fresh adversarial review;
- original evidence retained only as historical.

### Case 2 — repaired candidate → rebound PR head

`1c36dbed… → 280c896c…`

Expected classification:

`GOVERNANCE_MATERIAL_DELTA`

Expected effects:

- executable acceptance reused through equivalence proof;
- independent authority/integration-delta review;
- fresh adversarial delta review;
- new exact-head G5 binding;
- original G5 remains historical fact.

### Case 3 — rebound head → implementation merge

`280c896c… → a38d9cb3…`

The trees were identical.

Expected classification:

`PROVENANCE_ONLY_CHANGE`

Expected effects:

- tree-identity proof;
- new integration identity/binding;
- post-merge evidence as declared;
- no evidence relabeling.

### Case 4 — implementation merge → final Phase-021 closure

`a38d9cb3… → 29637b92…`

Expected effect:

- implementation acceptance preserved;
- closure/governance evidence added;
- final Phase-021 state complete;
- Phase 022 remains unauthorized.

R-G will replay these cases through the eventual shadow implementation.

## Required graph queries

The eventual implementation must answer deterministically:

- Why is this evidence valid for this revision?
- What changed between these revisions?
- Which material surfaces changed?
- Which evidence nodes are invalidated?
- Which evidence nodes can be reused, and under what proof?
- What is the minimal required reverification set?
- Which review/G5/integration bindings must be refreshed?
- What historical failures and superseded results exist?

The storage technology remains deferred; the contract requires only that these queries be reconstructable from immutable records.

## Fail-closed conditions

R-C requires `INCONCLUSIVE`/`BLOCKED` rather than reuse when:

- any changed path is unmapped;
- material-surface selectors conflict ambiguously;
- an equivalence proof is missing;
- authority semantic delta is unreviewed;
- evaluator semantic delta is unreviewed;
- the evidence graph is incomplete for the claim;
- revision/tree identity cannot be established;
- reuse would require editing original evidence identity;
- a mandatory evidence floor would be weakened; or
- a hidden requirement would be needed to justify invalidation.

## Exit review

R-C closes PASS because:

1. evidence graph node/edge semantics are explicit;
2. material surfaces have a pre-G2 manifest contract;
3. revision classification is deterministic and fail-closed;
4. content-equivalence proof levels are explicit;
5. invalidation is minimal but transitively safe;
6. reuse is by reference/binding rather than relabeling;
7. review/CI/G5/integration effects are defined;
8. candidate generations and historical evidence are immutable; and
9. the actual Phase-021 sequence is encoded as a replay oracle.

## Handoff

**021-R-D — Agent Dispatcher, Role Identity, Session Isolation, Context Generation & Provenance Manifests** is next eligible.

R-D should consume the graph contract by ensuring every agent dispatch/run produces identities and provenance that can become evidence-graph nodes without exposing chain-of-thought or protected evaluator probes.
