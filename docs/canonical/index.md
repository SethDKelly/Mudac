# Canonical MUDAC Knowledge

This subtree is the preferred source for current MUDAC conceptual product meaning and governance. Architecture and implementation remain **suspended downstream candidates** while Jackson Concept Design is still in progress.

# Current conceptual knowledge

* [Project Context & Purpose](project/) — current mandate, scope, constraints, purpose obligations, needs, success situations and tensions.
* [Concepts](concepts/) — current **eighteen-Concept** catalog after Phase 010 convergence.
* [Synchronizations](synchronizations/) — current reconciled Phase 011 composition/synchronization authority.
* [Dependence](dependence/) — current accepted Phase 012 extrinsic inclusion-dependence authority, partial through 012-D.
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
012-E: NEXT
```

# Current Concept authority

The current eighteen Concepts are:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

`Judging Encounter` and `Official Outcome Revision` remain only deprecated historical adapters.

# Current composition authority

Phase 011 is complete. Current interaction rules live under [Synchronizations](synchronizations/).

Dependence does not replace synchronization. Concepts may synchronize without having inclusion edges, and inclusion edges do not prescribe implementation calls or runtime orchestration.

# Current dependence authority

[MUDAC Application-Family Concept Dependence](dependence/application-family-dependence.md) owns accepted current Phase 012 inclusion dependence.

The model is partial through 012-D.

012-C established Competition/actor/competitor context. 012-D adds:

```text
Evaluation Occurrence → Team / Participation / Rubric
Evaluation Obligation → Team / Participation / Rubric
Scorecard             → Team / Participation / Rubric
```

Team and Participation supply Competition transitively; Participation supplies Identity transitively.

Evaluation Occurrence, Evaluation Obligation, and Scorecard are explicitly **not** a universal co-inclusion cycle. Each has a coherent limited application role without the other two, while the full current application may include and synchronize all three.

Rubric remains independently meaningful as reusable evaluation-instrument definition.

# Product-family implications

Dependence-valid does not mean in scope.

Current contraction probes include separate occurrence-history, responsibility/remaining-work, and Scorecard-capture capabilities plus the full evaluation capability. Phase 012-I decides scope adoption.

Versioning/Provenance inclusion around authoritative and correctable state remains unresolved until 012-E.

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
012 dependence / subsets / product-family / scope             IN PROGRESS — 012-E NEXT
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

The immediate next work is **012-E — Authority Lineage, Provenance & Correctability Dependence**.
