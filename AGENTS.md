# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md).
3. Read current [Project](docs/canonical/project/), [Concepts](docs/canonical/concepts/), [Synchronizations](docs/canonical/synchronizations/) and [Dependence](docs/canonical/dependence/).
4. Use [MUDAC Product-Family Scope](docs/canonical/dependence/product-family-scope.md) for PF-01.
5. Read the final [Phase 013 Mapping Authority Baseline](docs/canonical/experience/mapping-authority-baseline.md) and relevant current Experience owners.
6. For Phase 014, read [014-A](docs/014-familiarity-reuse-genericity/014-A-familiarity-reuse-genericity-scope-criteria-evidence-subphase-planning.md), [014-B](docs/014-familiarity-reuse-genericity/014-B-familiarity-evidence-baseline-precedent-taxonomy-comparison-register.md), and the completed family audits 014-C through 014-E before cross-catalog terminology work.
7. Treat historical adapters as evidence only unless a current canonical owner explicitly says otherwise.
8. Do not preload architecture/implementation except for explicit contamination/history analysis.

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
014-F: NEXT
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

Do not infer semantic fit from name similarity, popularity, UI resemblance or implementation reuse.

## Accepted family constraints

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
Outcome Declaration != Export
Export currency != Publication state
Publication Published != delivery / recipient possession
```

Do not replace these with generic `User`, `Role`, `Permission`, `Session`, `Task`, `Form`, `Submission`, `Revision`, `Result`, `Report`, or `Publish` abstractions when those terms erase ownership or history.

## Family-3 familiarity result

014-E retains:

```text
Versioning          → authoritative version/snapshot lineage with strong constraints
Provenance          → origin / derivation / represented-authority explanation
Award               → explicit recognition
Outcome Declaration → explicit official-result declaration with Affected/successor semantics
Export              → exact-source representation + currency
Publication         → deliberate audience/channel release
```

Versioning is not generic user-facing edit/revert/branch authority. Provenance does not create authority. Award recognition is not implied by Rank. Officiality is not implied by Finalization or publication. Export generation does not publish. Publication does not prove delivery or erase external copies after withdrawal.

## Current next task

Proceed to:

> **014-F — Cross-Catalog False Familiarity, Terminology & Expectation-Transfer Audit**
