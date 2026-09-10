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
* Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness: **In Progress**
  * 008-A — Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails: **Complete**
  * 008-B — Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation: **Complete — PASS AFTER NARROW REMEDIATION**
  * 008-C — Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix: **Complete — PASS**
  * 008-D — Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan: **Complete — PASS**
  * 008-E — Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan: **Next**

## Current posture

MUDAC has formally exited the renewed Jackson Concept Design methodology for the current accepted baseline. Implementation planning is active; no executable domain slice has yet been authorized.

[008-A](008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) establishes Phase 008 authority. [008-B](008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) qualifies the retained 006-D substrate. [008-C](008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md) closes residual/historical-plan ownership. [008-D](008-implementation-reentry/008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md) now fixes the persistence/history implementation substrate.

The current status is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
008-C: COMPLETE — PASS
008-D: COMPLETE — PASS
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
persistence/history implementation plan: ACCEPTED / NOT IMPLEMENTED
008-E: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

## Accepted 008-D implementation substrate

Durable current detail lives in [Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract](canonical/implementation/persistence-history-projection.md).

The accepted plan uses one PostgreSQL authority database with six module-owned schemas plus `projection` and narrow `platform` schemas. Mutable current rows stay separate from immutable semantic Version/history records. Provenance remains module-local, governed exceptions remain policy-specific, and Official Outcome Revision uses immutable outcome-owned revisions rather than mutable result rows.

The transactional outbox is at-least-once and does not claim queue order is authority order. Projection state preserves explicit source basis and uses idempotent/out-of-order convergence with generation rebuilds for non-trivial cross-module read models.

Migrations are SQL-first, owner-scoped, checksum-verified, advisory-lock protected, separately privileged and never run automatically by application startup. Authoritative history is retained conservatively until 008-K defines applicable retention requirements.

None of these decisions creates database objects during Phase 008.

## Phase 008 structure

```text
008-A authority / canonical baseline / change control          COMPLETE
   ↓
008-B protected substrate qualification                       COMPLETE
   ↓
008-C residual-risk + historical-plan reconciliation          COMPLETE
   ↓
008-D persistence / temporal / provenance / exception plan    COMPLETE
   ↓
008-E Identity / Participation / Access / session plan        NEXT
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

A qualified bootstrap, accepted implementation plan, first-slice authorization, code start, merge readiness, deployment readiness, and production readiness are separate states.

If implementation planning conflicts with current canonical meaning, the downstream mechanism changes by default. A genuine semantic contradiction, missing semantic owner, or intentional product change routes through `CHG-*`; it is not resolved silently in schema, APIs, UI, tests, IaC, or implementation-planning documents.

Phase 008 follows `CTX-*` progressive disclosure and `DOC-*` one-owner discipline. Durable 008-D implementation meaning is canonicalized under `docs/canonical/implementation/`, while the numbered 008-D record preserves rationale and decisions.

## Why Phase 005 and Phase 006 were not erased

[005-J](005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md) remains historical provenance for the earlier architecture-readiness conclusion.

[007-A](007-design-refinement/007-A-design-reentry-implementation-freeze-jackson-completion-criteria.md) later froze execution and reopened deliberate Concept Design; [007-I](007-design-refinement/007-I-formal-jackson-concept-design-methodology-exit-accepted-residual-uncertainty-implementation-resume-boundary-decision.md) closed that renewed methodology. 008-B re-qualified the retained 006-D executable portion, 008-C mapped the deferred 006-E–M lineage, and 008-D replaces the old 006-E persistence-planning authority with a current post-design plan.

Historical records remain append-stable provenance.

## Current next work

Proceed to **008-E — Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan**.

New domain implementation remains **not started** until 008-L explicitly authorizes the first executable slice.
