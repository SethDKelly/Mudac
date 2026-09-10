# MUDAC Design Documentation

The repository is the durable design and implementation authority; conversation history is working context.

## Preferred navigation

Start at [index.md](index.md), the OKF v0.2 bundle root. Current product/domain, synchronization, temporal/correction, policy, UX, governance, architecture, and implementation meaning lives under [Canonical Knowledge](canonical/). Root [`AGENTS.md`](../AGENTS.md) is only a bootstrap adapter into those owners.

Use numbered phase directories for rationale, design evolution, alternatives, implementation planning, and provenance.

## Status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification, Policy & Synchronization Refinement: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance: **Complete**
* Phase 005 — System, Application, Data & Synchronization Architecture: **Complete as historical architecture exit**
* Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy: **Historical/frozen after 006-D; 006-E–M superseded as current execution queue**
  * 006-A — implementation authority/toolchain: Complete
  * 006-B — verification/evidence strategy: Complete
  * 006-C — source/package/dependency topology: Complete
  * 006-D — environment/IaC/CI/CD/local/runtime bootstrap: Complete and retained as a protected non-domain implementation baseline
  * 006-E through 006-M: historical deferred planning lineage; must be refreshed before execution
* Phase 007 — Jackson Design Refinement & Methodology Closure: **Complete — formal methodology exit passed**
  * 007-A through 007-H: Complete
  * 007-I — Formal Jackson Concept Design Methodology Exit, Accepted Residual Uncertainty & Implementation-Resume Boundary Decision: **Complete — PASS**
* Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness: **In Progress**
  * 008-A — Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails: **Complete**
  * 008-B — Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation: **Next**

## Current posture

MUDAC has formally exited the renewed Jackson Concept Design methodology for the current accepted baseline.

The current execution boundary is owned by [Design / Implementation Boundary](canonical/governance/design-implementation-boundary.md).

[008-A](008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) now establishes the Phase 008 authority model: current canonical semantic/governance owners constrain architecture, architecture constrains implementation, current implementation contracts constrain downstream mechanism, and numbered Phase 008 records capture planning rationale without becoming a competing canonical tree.

The current status is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: NEXT / NOT STARTED
protected 006-D baseline: NOT YET QUALIFIED BY PHASE 008
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

The retained 006-D substrate remains a protected non-domain baseline. The old 006-E through 006-M queue is not executable authority.

## Phase 008 structure

[Phase 008](008-implementation-reentry/) proceeds through:

```text
008-A authority / canonical baseline / change control          COMPLETE
   ↓
008-B protected substrate qualification                       NEXT
   ↓
008-C residual-risk + historical-plan reconciliation
   ↓
008-D persistence / temporal / provenance / exception plan
   ↓
008-E Identity / Participation / Access / session plan
   ↓
008-F commands / API / transaction / concurrency plan
   ↓
008-G browser / Draft / sync / recovery / accessibility plan
   ↓
008-H Competition + judging-operations slice plan
   ↓
008-I Scorecard + evaluation-evidence + paper slice plan
   ↓
008-J outcomes + finalization + representation slice plan
   ↓
008-K cross-cutting verification / operational evidence plan
   ↓
008-L consolidated roadmap + first-slice authorization
   ↓
Phase 009 implementation
```

No Phase 008 subgroup implements new domain behavior. If 008-L passes, Phase 009 will begin the first explicitly authorized domain implementation slice.

## Planning authority and change control

008-A distinguishes planning decision, first-slice authorization, code start, merge readiness, deployment readiness, and production readiness. None implies the next.

If implementation planning conflicts with current canonical meaning, the downstream mechanism changes by default. A genuine semantic contradiction, missing semantic owner, or intentional product change routes through `CHG-*`; it is not resolved silently in schema, APIs, UI, tests, IaC, or implementation-planning documents.

Phase 008 follows `CTX-*` progressive disclosure and `DOC-*` one-owner discipline. Historical phase records are used for rationale and supersession analysis, not reconstructed as current rule stores.

## Why Phase 005 and Phase 006 were not erased

[005-J](005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md) remains historical provenance for the earlier conclusion that architecture was implementation-planning ready.

[007-A](007-design-refinement/007-A-design-reentry-implementation-freeze-jackson-completion-criteria.md) later superseded the assumption that implementation should continue immediately, froze domain implementation, and reopened deliberate Concept Design. [007-I](007-design-refinement/007-I-formal-jackson-concept-design-methodology-exit-accepted-residual-uncertainty-implementation-resume-boundary-decision.md) closed that renewed methodology after the intervening evidence gates passed.

Historical records are preserved rather than rewritten to make earlier decisions appear never to have happened. Phase 008 uses them as lineage while deriving a current plan from the completed canonical design.

## Current next work

Proceed to **008-B — Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation**.

New domain implementation remains **not started** until 008-L explicitly authorizes the first executable slice.
