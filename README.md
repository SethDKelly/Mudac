# MUDAC Competition Demo

MUDAC is a design-governed application effort for fair, traceable, resilient judging at live student data competitions.

The current product definition is representation-independent: volunteer Judges and competition Organizers need to conduct, preserve, coordinate and explain independent evaluation under real event-day constraints while protecting bias-sensitive identity, trustworthy authority and historical evidence.

## Start here

* [`AGENTS.md`](AGENTS.md) — repository-agent bootstrap and design-only boundary.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/`](docs/canonical/) — current conceptual product knowledge.
* [`docs/canonical/project/domain-vocabulary-expectation-transfer.md`](docs/canonical/project/domain-vocabulary-expectation-transfer.md) — current cross-catalog terminology/expectation-transfer authority.
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
014-E: COMPLETE — PASS
014-F: COMPLETE — PASS
014-G: NEXT
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

All three Concept-family familiarity audits retain the eighteen current Concept names/boundaries.

014-F now governs the language around those Concepts:

```text
T1 canonical semantic term
T2 qualified explanatory label
T3 analogy-only term
T4 high-risk generic term
```

The major false-familiarity risk is generic glue vocabulary rather than the canonical catalog itself.

Preserve:

```text
Identity != Participation != Access
Evaluation Occurrence != Evaluation Obligation != Scorecard
Versioning != Provenance
Rank / selection basis != Award recognition
Competition Finalized != Outcome Declaration
Outcome Declaration != Export != Publication != delivery
```

Avoid generic terminology such as `role`, `task`, `submit`, `final result`, `winner`, `revision`, `resolve`, `share` or universal `status` where it would hide the natural semantic owner.

Prefer owner-specific actions and states such as `Finalize Evaluation`, `Complete Live Event`, `Confirm Successor Outcome Declaration`, `Generate Export`, `Publish Representation` and `Withdraw Publication`.

## Current direction

Proceed to **014-G — Broader Genericity, Parameterization, Duplication & Specialization-Pressure Audit**.
