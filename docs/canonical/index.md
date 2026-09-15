# Canonical MUDAC Knowledge

This subtree is the preferred source for current MUDAC conceptual product meaning and governance. Architecture and implementation remain **suspended downstream candidates** while Jackson Concept Design is still in progress.

# Current conceptual knowledge

* [Project Context & Purpose](project/) — current mandate, scope, constraints, purpose obligations, needs, success situations and tensions.
* [Concepts](concepts/) — current **eighteen-Concept** catalog after Phase 010 convergence.
* [Synchronizations](synchronizations/) — current reconciled Phase 011 composition/synchronization authority.
* [Dependence](dependence/) — current accepted Phase 012 extrinsic inclusion-dependence authority, partial through 012-C.
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
012-D: NEXT
```

# Current Concept authority

The current eighteen Concepts are:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

`Judging Encounter` and `Official Outcome Revision` remain only deprecated historical adapters.

# Current composition authority

Phase 011 is complete. Current interaction rules live under [Synchronizations](synchronizations/).

Dependence does not replace synchronization. A pair of Concepts may synchronize without having an inclusion edge, and an inclusion edge does not prescribe runtime orchestration or implementation calls.

# Current dependence authority

[MUDAC Application-Family Concept Dependence](dependence/application-family-dependence.md) owns accepted current Phase 012 inclusion dependence.

Direct edges through 012-C are:

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

Transitive consequences include:

```text
Division → Team → Competition
Alias    → Team → Competition
Panel    → Participation → Competition
Panel    → Participation → Identity
```

Current explicit universal non-edges include:

```text
Competition ↛ Division
Competition ↛ Panel
Team        ↛ Alias
Identity    ↛ Competition
Identity    ↛ Participation
Access      ↛ Participation
Access      ↛ Identity
```

These non-edges do not erase conditional composition. For example, protected Judge/Organizer actions still use Participation-derived context plus Access.

# Current product-family scope rules

- every in-scope MUDAC application variant retains Competition as the family context;
- blinded-judging variants include Alias;
- multi-cohort variants include Division;
- reusable evaluator-grouping variants include Panel;
- ad-hoc evaluator assignment may omit Panel;
- single-cohort operation may omit Division at the dependence level;
- adopting a blinded no-Division variant would require later policy/composition revalidation because current disclosure policy names Division in Judge-facing blinded representation.

The dependence owner is explicitly **partial through 012-C**. Do not infer non-edges for unresolved Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Versioning, Provenance, Award, Outcome Declaration, Export or Publication questions until their owning Phase 012 subphases complete.

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
012 dependence / subsets / product-family / scope             IN PROGRESS — 012-D NEXT
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

The immediate next work is **012-D — Evaluation Structure, Responsibility, Basis & Judgment Dependence**.
