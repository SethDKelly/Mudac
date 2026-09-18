# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md).
3. Read current [Project](docs/canonical/project/), [Concepts](docs/canonical/concepts/), [Synchronizations](docs/canonical/synchronizations/) and [Dependence](docs/canonical/dependence/).
4. Use [MUDAC Product-Family Scope](docs/canonical/dependence/product-family-scope.md) for PF-01.
5. Read the final [Phase 013 Mapping Authority Baseline](docs/canonical/experience/mapping-authority-baseline.md) and relevant current Experience owners.
6. For current methodology work, read [Phase 014](docs/014-familiarity-reuse-genericity/), especially 014-A/014-B and the latest completed family audit.
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
014-E: NEXT
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

## Phase-014 familiarity evidence rule

014-B establishes E1 current MUDAC authority as the semantic target and E2–E7 precedent classes as comparison evidence only. The PT-01..PT-13 taxonomy creates no Concepts or authority.

Do not infer semantic fit from name similarity, popularity, UI resemblance or implementation reuse.

## Accepted Family-1 dispositions from 014-C

```text
Competition    → semantic fit / bounded competition occurrence
Division       → semantic fit / scoped competitive cohort
Team           → semantic fit / competing unit
Panel          → semantic fit with constraints / intended evaluator grouping
Identity       → semantic fit / stable human identity continuity
Participation  → semantic fit with constraints / scoped involvement/capacity
Alias          → semantic fit with constraints / scoped alternate identity
Access         → semantic fit with constraints / contextual authorization
```

Preserve:

```text
Identity != Participation != Access
Panel membership != occurrence participation != responsibility != evidence
Access permission != semantic authorship
```

Do not replace this model with generic `User / Role / Permission / Group` semantics.

## Accepted Family-2 dispositions from 014-D

```text
Evaluation Occurrence → semantic fit with constraints / bounded evaluation event
Evaluation Obligation → semantic fit with constraints / scoped evaluation duty
Rubric                → strong semantic fit / evaluation instrument
Scorecard             → semantic fit with constraints / one evaluator judgment record
```

Preserve:

```text
occurrence participation != responsibility
responsibility != judgment evidence
Rubric definition != exact authoritative Evaluation Basis
Scorecard Draft != authoritative judgment
historical obligation satisfaction != current evidence eligibility
```

Do not collapse these Concepts into generic `Session / Assignment / Task / Form / Submission / Attempt` semantics.

`Encounter` remains a negative historical precedent; `Session`, `Attempt`, `Assignment`, `Task`, `Ballot`, `Submission` and `Form` are analogies only where their transferred expectations remain valid.

## Corrected event-completion seam

014-C repaired the current Phase-011 synchronization rule:

```text
Event Completed
  → broad/new ordinary live-event Judge capability closes
  != universal hidden Access revocation

existing Outstanding obligation
  + current policy permits continuation
  + fresh Access permits the specific operation
  → same logical evaluation may continue
```

This does not reactivate Participation, reopen Competition, create another obligation or restore general event-day capability.

## Retained authority invariants

Preserve at least:

- one Evaluation Obligation → at most one logical Scorecard;
- Scorecard Draft != authority;
- historical obligation satisfaction != current evidence eligibility;
- Rank != Award authority;
- Competition Finalization != Outcome Declaration;
- Outcome Declaration != Export != Publication != delivery;
- accessible/degraded/paper paths preserve the same authority model;
- result unknown != success != failure.

## Current next task

Proceed to:

> **014-E — Versioning, Provenance, Award, Outcome Declaration, Export & Publication Familiarity/Reuse Audit**
