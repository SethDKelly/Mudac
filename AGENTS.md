# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md).
3. Read current [Project](docs/canonical/project/), [Concepts](docs/canonical/concepts/), [Synchronizations](docs/canonical/synchronizations/) and [Dependence](docs/canonical/dependence/).
4. Read [MUDAC Domain Vocabulary & Expectation-Transfer Rules](docs/canonical/project/domain-vocabulary-expectation-transfer.md) before introducing familiar cross-domain labels or generic actions/statuses.
5. Use [MUDAC Product-Family Scope](docs/canonical/dependence/product-family-scope.md) for PF-01.
6. Read the final [Phase 013 Mapping Authority Baseline](docs/canonical/experience/mapping-authority-baseline.md) and relevant current Experience owners.
7. For Phase 014, read [014-A](docs/014-familiarity-reuse-genericity/014-A-familiarity-reuse-genericity-scope-criteria-evidence-subphase-planning.md), [014-B](docs/014-familiarity-reuse-genericity/014-B-familiarity-evidence-baseline-precedent-taxonomy-comparison-register.md), and the completed 014-C through 014-F records relevant to the current question.
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
014-G: NEXT
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

## Phase-014 familiarity rule

Only current MUDAC canonical semantics define MUDAC meaning. Familiar precedents are comparison evidence.

Do not infer semantic fit or safe generalization from name similarity, popularity, UI resemblance, implementation reuse or shared state vocabulary.

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

## Vocabulary / expectation-transfer rules

014-F retains all eighteen canonical Concept names and classifies vocabulary as:

```text
T1 canonical semantic term
T2 qualified explanatory label
T3 analogy-only term
T4 high-risk generic term
```

Do not replace current owners with generic `User`, `Role`, `Permission`, `Session`, `Task`, `Form`, `Submission`, `Revision`, `Result`, `Report`, `Workflow` or `Status` concepts merely for familiarity.

Keep materially ambiguous state/action words owner-qualified:

```text
Competition Ready != Competition Readiness != Ranking Readiness != Finalization Readiness
Occurrence Complete != Obligation Satisfied != Scorecard Finalized
Event Completed != Competition Finalized
Affected != Superseded != Invalidated != Replaced != Stale != Retired != Withdrawn
Published != public != delivered
```

High-consequence generic verbs such as `Submit`, `Done`, `Close`, `Edit`, `Reopen`, `Reset`, `Revert`, `Delete`, `Resolve`, `Fix`, `Force`, `Override`, `Approve`, `Share` and `Send` must not obscure natural owner-specific actions.

Prefer established labels such as `Finalize Evaluation`, `Complete Live Event`, `Finalize Competition & Declare Outcome`, `Generate Export`, `Publish Representation`, and `Withdraw Publication`.

## Current next task

Proceed to:

> **014-G — Broader Genericity, Parameterization, Duplication & Specialization-Pressure Audit**
