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
* Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy: **Historical after 006-D; 006-E–M explicitly mapped/superseded by 008-C**
  * 006-A through 006-C: complete historical planning
  * 006-D: complete historical bootstrap; re-qualified by 008-B as the protected non-domain baseline
  * 006-E through 006-M: preserved historical planning lineage; no longer executable authority
* Phase 007 — Jackson Design Refinement & Methodology Closure: **Complete — formal methodology exit passed**
  * 007-A through 007-H: Complete
  * 007-I — Formal Jackson Concept Design Methodology Exit, Accepted Residual Uncertainty & Implementation-Resume Boundary Decision: **Complete — PASS**
* Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness: **In Progress**
  * 008-A — Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails: **Complete**
  * 008-B — Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation: **Complete — PASS AFTER NARROW REMEDIATION**
  * 008-C — Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix: **Complete — PASS**
  * 008-D — Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan: **Next**

## Current posture

MUDAC has formally exited the renewed Jackson Concept Design methodology for the current accepted baseline.

The current execution boundary is owned by [Design / Implementation Boundary](canonical/governance/design-implementation-boundary.md).

[008-A](008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) establishes the Phase 008 authority model. [008-B](008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) qualifies the retained 006-D executable substrate. [008-C](008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md) closes residual and historical-plan ownership.

The current status is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
008-C: COMPLETE — PASS
residual ownership: CLOSED FOR CURRENT BASELINE
historical 006-E–M executable queue: SUPERSEDED / MAPPED
008-D: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

008-C assigns every 007-H Class 2/3 residual to a current later planning owner, preserves every Class 4 item outside the baseline, carries the 008-B repository-protection/dependency-alert evidence limitations to 008-K/008-L, and gives each historical 006-E–M item an explicit preserve/split/merge/expand disposition.

The key decomposition changes are deliberate: old 006-J splits between 008-G and 008-I; old 006-L merges into 008-J; old 006-M splits between 008-K and 008-L.

## Phase 008 structure

[Phase 008](008-implementation-reentry/) proceeds through:

```text
008-A authority / canonical baseline / change control          COMPLETE
   ↓
008-B protected substrate qualification                       COMPLETE
   ↓
008-C residual-risk + historical-plan reconciliation          COMPLETE
   ↓
008-D persistence / temporal / provenance / exception plan    NEXT
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

A qualified bootstrap, planning decision, first-slice authorization, code start, merge readiness, deployment readiness, and production readiness are separate states.

If implementation planning conflicts with current canonical meaning, the downstream mechanism changes by default. A genuine semantic contradiction, missing semantic owner, or intentional product change routes through `CHG-*`; it is not resolved silently in schema, APIs, UI, tests, IaC, or implementation-planning documents.

Phase 008 follows `CTX-*` progressive disclosure and `DOC-*` one-owner discipline. 008-C is the planning/provenance owner for residual and historical-plan disposition; it does not create a second canonical rule store.

## Why Phase 005 and Phase 006 were not erased

[005-J](005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md) remains historical provenance for the earlier architecture-readiness conclusion.

[007-A](007-design-refinement/007-A-design-reentry-implementation-freeze-jackson-completion-criteria.md) later froze execution and reopened deliberate Concept Design; [007-I](007-design-refinement/007-I-formal-jackson-concept-design-methodology-exit-accepted-residual-uncertainty-implementation-resume-boundary-decision.md) closed that renewed methodology. 008-B re-qualified the retained 006-D executable portion, and 008-C now explicitly maps rather than deletes the deferred 006-E–M lineage.

Historical records remain append-stable provenance. Current planning authority now belongs to 008-D through 008-L.

## Current next work

Proceed to **008-D — Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan**.

New domain implementation remains **not started** until 008-L explicitly authorizes the first executable slice.
