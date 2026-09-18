# MUDAC Competition Demo

MUDAC is a design-governed application effort for fair, traceable, resilient judging at live student data competitions.

The current product definition is representation-independent: volunteer Judges and competition Organizers need to conduct, preserve, coordinate and explain independent evaluation under real event-day constraints while protecting bias-sensitive identity, trustworthy authority and historical evidence.

## Start here

* [`AGENTS.md`](AGENTS.md) — repository-agent bootstrap and design-only boundary.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/`](docs/canonical/) — current conceptual product knowledge.
* [`docs/014-familiarity-reuse-genericity/`](docs/014-familiarity-reuse-genericity/) — active Phase 014.

## Current status

```text
Jackson Concept Design: IN PROGRESS
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
architecture: SUSPENDED PENDING DESIGN CLOSURE
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

## Current product scope

MUDAC adopts one current product/application variant:

> **PF-01 — MUDAC Live Competition Judging & Official Outcome**

## Phase-014 posture

014-B establishes the evidence hierarchy and precedent taxonomy for familiarity/reuse analysis.

014-C retains Family 1 without generic actor-model collapse:

```text
Identity != Participation != Access
Panel membership != occurrence participation != responsibility != evidence
Access permission != semantic authorship
```

014-D retains Family 2 while rejecting all-in-one session/task/form/submission semantics:

```text
Evaluation Occurrence ≈ bounded evaluation event
Evaluation Obligation ≈ scoped evaluation duty
Rubric                ≈ evaluation/scoring instrument
Scorecard             ≈ one evaluator's judgment record
```

Preserve:

```text
occurrence participation != responsibility
responsibility != judgment evidence
Rubric definition != exact authoritative Evaluation Basis
Scorecard Draft != authoritative judgment
historical obligation satisfaction != current evidence eligibility
```

014-D found no upstream contradiction requiring repair.

Historical `Judging Encounter` and `Official Outcome Revision` remain negative/counterexample precedents only.

## Current direction

Proceed to **014-E — Versioning, Provenance, Award, Outcome Declaration, Export & Publication Familiarity/Reuse Audit**.
