# Canonical MUDAC Knowledge

This subtree is the preferred source for current MUDAC conceptual product meaning and governance. Architecture and implementation remain **suspended downstream candidates** while Jackson Concept Design is still in progress.

# Current conceptual knowledge

* [Project Context & Purpose](project/) — current mandate, scope, constraints, purpose obligations, needs, success situations and tensions.
* [Concepts](concepts/) — current eighteen-Concept catalog after Phase 010 convergence.
* [Synchronizations](synchronizations/) — current reconciled Phase-011 composition/synchronization authority.
* [Dependence](dependence/) — current accepted Phase-012 inclusion dependence and capability-conditioned co-inclusion, partial through 012-E.
* [Mechanisms](mechanisms/) — current derived/supporting subjects and processes.
* [Policies](policies/) — current governing/configurable competition semantics.
* [Invariants](invariants/) — current cross-cutting conceptual constraints.
* [Experience](experience/) — current mapping/experience evidence, subject to Phase 013 revalidation.

# Governance

* [Governance](governance/) — methodology, documentation/change governance, validation, stable identifiers, and the current design/implementation boundary.

# Suspended downstream knowledge

* [Architecture](architecture/) — preserved pre-closure architecture candidates; suspended as Concept Design constraints.
* [Implementation](implementation/) — preserved implementation candidates/tooling knowledge plus frozen 006-D bootstrap facts; suspended as current domain realization authority.

# Current methodology posture

```text
Jackson Concept Design: REOPENED / IN PROGRESS
007-I previous closure: SUPERSEDED
008 implementation re-entry: HALTED AFTER 008-E
architecture authority: SUSPENDED
implementation-planning authority: SUSPENDED
006-D executable bootstrap: FROZEN HISTORICAL NON-DOMAIN SUBSTRATE
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
009: COMPLETE — PASS
010: COMPLETE — PASS
011: COMPLETE — PASS
012: IN PROGRESS
012-A: COMPLETE — READY
012-B: COMPLETE — PASS
012-C: COMPLETE — PASS
012-D: COMPLETE — PASS
012-E: COMPLETE — PASS
012-F: NEXT
```

# Current Concept authority

The current eighteen Concepts are:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

`Judging Encounter` and `Official Outcome Revision` remain deprecated historical adapters.

# Current composition authority

Phase 011 is complete. Current interaction rules live under [Synchronizations](synchronizations/).

Dependence does not replace synchronization. A pair of Concepts may synchronize without an inclusion edge, and an inclusion rule does not prescribe runtime orchestration or implementation calls.

# Current dependence authority

[MUDAC Application-Family Concept Dependence](dependence/application-family-dependence.md) owns current Phase-012 dependence truth.

The direct graph currently covers the Competition/actor/competitor and evaluation families established in 012-C/D.

012-E establishes that authority-history support is capability-conditioned rather than a global graph sink:

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance

Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance

Rubric/Scorecard authoritative correction or invalidation
  ⇒ Versioning + Provenance
```

Versioning and Provenance remain independent Concepts:

```text
Versioning ↛ Provenance
Provenance ↛ Versioning
```

Working Rubric/Scorecard capability can therefore be dependence-coherent without the support pair, but may not claim current MUDAC authoritative-evaluation semantics.

Outcome Declaration is not routed through generic Versioning/Provenance merely because it is authoritative; it owns immutable declaration basis, declaring authority, affected/superseded state, and predecessor/successor history intrinsically.

Outcome-affecting Evaluation Policy remains a reconstructibility requirement once judging begins, not a Concept vertex.

The dependence owner is explicitly **partial through 012-E**. Do not infer outcome or release non-edges until 012-F/G complete.

# Retrieval rule during reopened design

For Phases 012–017:

1. load the current phase record relevant to the task;
2. load [Project Context & Purpose](project/) when project/purpose/scope assumptions matter;
3. load task-relevant [Concepts](concepts/), [Synchronizations](synchronizations/) and [Dependence](dependence/);
4. use older phase records for rationale/evidence rather than current ownership;
5. load the [Design / Implementation Boundary](governance/design-implementation-boundary.md) and downstream quarantine;
6. do not preload architecture/implementation except for explicit contamination/history work.

# Completion runway

```text
010 project/purpose / discovery / specification / modularity   COMPLETE — PASS
  ↓
011 composition / synchronization revalidation                COMPLETE — PASS
  ↓
012 dependence / subsets / product-family / scope             IN PROGRESS — 012-F NEXT
  ↓
013 mapping / representation revalidation
  ↓
014 familiarity / reuse / genericity / catalog refinement
  ↓
015 integrity / interference
  ↓
016 scenario / misfit / adversarial validation
  ↓
017 methodology completeness / canonical closure
```

The immediate next work is **012-F — Outcome, Recognition & Official-Authority Dependence**.
