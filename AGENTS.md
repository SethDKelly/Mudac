# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md).
3. Read current [Project](docs/canonical/project/), [Concepts](docs/canonical/concepts/), [Synchronizations](docs/canonical/synchronizations/) and [Dependence](docs/canonical/dependence/).
4. Read [MUDAC Domain Vocabulary & Expectation-Transfer Rules](docs/canonical/project/domain-vocabulary-expectation-transfer.md) before introducing familiar cross-domain labels or generic actions/statuses.
5. Use [MUDAC Product-Family Scope](docs/canonical/dependence/product-family-scope.md) for PF-01.
6. Read the final [Phase 013 Mapping Authority Baseline](docs/canonical/experience/mapping-authority-baseline.md) and relevant current Experience owners.
7. For Phase 014, read [014-A](docs/014-familiarity-reuse-genericity/014-A-familiarity-reuse-genericity-scope-criteria-evidence-subphase-planning.md), [014-B](docs/014-familiarity-reuse-genericity/014-B-familiarity-evidence-baseline-precedent-taxonomy-comparison-register.md), and completed records through the current subphase.
8. Treat historical adapters as evidence only unless a current canonical owner explicitly says otherwise.
9. Do not preload architecture/implementation except for explicit contamination/history analysis.

## Current methodology posture

```text
009: COMPLETE — PASS
010: COMPLETE — PASS
011: COMPLETE — PASS
012: COMPLETE — PASS
013: COMPLETE — PASS
014: IN PROGRESS
014-A: COMPLETE — READY
014-B: COMPLETE — PASS
014-C: COMPLETE — PASS
014-D: COMPLETE — PASS
014-E: COMPLETE — PASS
014-F: COMPLETE — PASS
014-G: COMPLETE — PASS
014-H: NEXT
architecture authority: SUSPENDED
implementation-planning authority: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

## Current Concept authority

The canonical catalog contains eighteen Concepts:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

`Judging Encounter` and `Official Outcome Revision` remain deprecated historical adapters.

Coverage, Aggregate, Rank and Readiness remain derived mechanisms. Reconciliation and Live Operations remain work/process contexts rather than Concepts.

## Phase-014 familiarity / genericity rules

Only current MUDAC canonical semantics define MUDAC meaning. Familiar precedents are comparison evidence.

Do not infer semantic fit or safe generalization from name similarity, popularity, UI resemblance, implementation reuse, shared parameter names, shared status labels or predecessor/successor shape.

```text
Generic at the boundary; specific in purpose.
shared parameter != shared purpose
shared history shape != shared lifecycle
implementation reuse != Concept identity
```

014-G adopts one narrow genericity refinement: Team intrinsically represents a competing group/unit; PF-01 binds that Concept to student teams.

Do not introduce generic `Group`, `Scoped Relationship`, `Occurrence`, `Task`, `Evaluation Record`, `Historical/Correctable Record`, `Result` or merged Export/Publication super-concepts merely to reduce repeated shapes.

## Accepted cross-catalog constraints

Preserve at least:

```text
Identity != Participation != Access
Panel membership != occurrence participation != responsibility != evidence
Evaluation Occurrence != Evaluation Obligation != Scorecard
Rubric definition != exact authoritative Evaluation Basis
Scorecard Draft != authoritative judgment
historical obligation satisfaction != current evidence eligibility
Versioning != Provenance
Rank / selection basis != Award recognition
Competition Finalized != Outcome Declaration
Outcome Declaration Affected != Superseded
Outcome Declaration != Export != Publication != delivery
Export currency != Publication state
```

## Reusable-pattern boundary

014-G carries possible reusable **design-pattern knowledge** into 014-H without creating new Concepts:

```text
scoped opaque-reference parameterization
exact-basis binding
explicit successor without silent historical rewrite
actor vs represented authority vs source
historical satisfaction vs current eligibility
derivation → recognition → official declaration
source authority → representation → release
```

014-H decides which concepts/patterns deserve reusable-knowledge treatment. Do not create a second canonical MUDAC concept catalog.

## Current next task

Proceed to:

> **014-H — Retained Novelty, Reusable Concept-Knowledge & Catalog-Candidate Audit**
