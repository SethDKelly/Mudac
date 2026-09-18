# Canonical MUDAC Knowledge

This subtree is the preferred source for current MUDAC conceptual product meaning and governance. Architecture and implementation remain **suspended downstream candidates** while Jackson Concept Design is in progress.

# Current conceptual knowledge

* [Project Context & Purpose](project/)
* [Concepts](concepts/)
* [Synchronizations](synchronizations/)
* [Dependence](dependence/)
* [Mechanisms](mechanisms/)
* [Policies](policies/)
* [Invariants](invariants/)
* [Experience](experience/)
* [Mapping Authority Baseline](experience/mapping-authority-baseline.md) — current Phase-013 authority/evidence topology through 013-I.
* [Award, Finalization & Outcome Officiality Mapping](experience/outcome-officiality.md) — accepted 013-H mapping.
* [External Representation, Disclosure & Release Mapping](experience/external-representation-release.md) — accepted 013-I mapping.

# Governance

* [Governance](governance/) — methodology, documentation/change governance and design/implementation boundary.

# Suspended downstream knowledge

* [Architecture](architecture/) — preserved downstream candidates; suspended.
* [Implementation](implementation/) — preserved downstream candidates/tooling plus frozen bootstrap facts; suspended as current domain authority.

# Current methodology posture

```text
Jackson Concept Design: REOPENED / IN PROGRESS
009: COMPLETE — PASS
010: COMPLETE — PASS
011: COMPLETE — PASS
012: COMPLETE — PASS
013: IN PROGRESS
013-A: COMPLETE — READY
013-B: COMPLETE — PASS
013-C: COMPLETE — PASS
013-D: COMPLETE — PASS
013-E: COMPLETE — PASS
013-F: COMPLETE — PASS
013-G: COMPLETE — PASS
013-H: COMPLETE — PASS
013-I: COMPLETE — PASS
013-J: NEXT
architecture authority: SUSPENDED
implementation-planning authority: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

# Current mapping authority

Current mapping knowledge follows:

```text
Purpose / Concepts / Synchronizations / Dependence / PF-01
  ↓
Policies / Invariants
  ↓
Phase 013 Mapping Entry Authority
  ↓
Mapping Authority Baseline
  ↓
accepted Experience owners
```

013-I adds:

```text
source authority != Export representation != Publication release != delivery
actor Access != audience disclosure
Export SourceBasis = exact / historically stable
Export generation != Publication
Export currency != Publication distribution state
new/corrected source → new Export
successor Outcome Declaration != successor Export != successor Publication
withdrawal/supersession != historical release erasure
recipient possession != current release authority / Access
Publication Published != delivery/viewing success
```

The old `paper-export-publication.md` and `reconciliation-finalization.md` files are historical evidence only.

# Retrieval rule during Phase 013

1. load the active Phase-013 record;
2. load [Mapping Authority Baseline](experience/mapping-authority-baseline.md);
3. load relevant current Project / Concepts / Synchronizations / Dependence / Policies / Invariants;
4. load accepted Experience owners relevant to the task;
5. use historical Experience material only as evidence;
6. do not preload architecture/implementation except for explicit contamination/history analysis.

Next: **013-J — Accessibility, Degraded Operation, Status/Feedback, Recovery & Semantic-Parity Mapping**.
