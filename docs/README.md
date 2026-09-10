# MUDAC Design Documentation

The repository is the durable design and implementation authority; conversation history is working context.

## Preferred navigation

Start at [index.md](index.md), the OKF v0.2 bundle root. Current product/domain, synchronization, temporal/correction, UX, governance, architecture, and retained implementation meaning lives under [Canonical Knowledge](canonical/). Root [`AGENTS.md`](../AGENTS.md) is only a bootstrap adapter into those owners.

Use numbered phase directories for rationale, design evolution, alternatives, implementation planning, and provenance.

## Status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification, Policy & Synchronization Refinement: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture, OKF Retrofit & Documentation Governance: **Complete**
* Phase 005 — System, Application, Data & Synchronization Architecture: **Complete as historical architecture exit**
* Phase 006 — Implementation Planning, Delivery Slices & Verification Strategy: **Frozen after 006-D**
  * 006-A — implementation authority/toolchain: Complete
  * 006-B — verification/evidence strategy: Complete
  * 006-C — source/package/dependency topology: Complete
  * 006-D — environment/IaC/CI/CD/local/runtime bootstrap: Complete and retained as a frozen non-domain prototype
  * 006-E through 006-M: **Deferred**
* Phase 007 — Jackson Design Refinement & Methodology Closure: **In Progress**
  * 007-A — design re-entry, implementation freeze & Jackson completion criteria: Complete
  * 007-B — Concept Completeness, Independence & Genericity Audit: **Complete**
  * 007-C — Cross-Concept Synchronization Completeness, Trigger, Preconditions/Postconditions & Authority-Seam Audit: **Complete**
  * 007-D — Temporal State, Correction, Invalidation, Supersession & Historical-Truth Closure: **Complete**
  * 007-E — End-to-End Scenario, Exception, Failure & Adversarial Authority Validation: **Complete**
  * 007-F — Judge & Organizer Experience-to-Concept Action, Synchronization & Authority Traceability Audit: **Complete**
  * **007-G — Policy, Representation, Outcome, Disclosure & Operational-Governance Closure Audit: Next**

## Current design posture

MUDAC remains in deliberate design refinement before any domain schema, persistence, authentication, API, browser-domain, feature, or application-AWS implementation proceeds.

The current execution boundary is owned by [Design / Implementation Boundary](canonical/governance/design-implementation-boundary.md).

007-B established the sixteen-Concept catalog. 007-C established the current [Synchronization](canonical/synchronizations/) layer. 007-D added [Temporal Truth, Correction & Historical Authority](canonical/synchronizations/temporal-truth-correction.md), separating lifecycle, working/committed authority, supersession, invalidation, replacement, affected/stale currency, distribution state, and historical observation.

007-E pressure-tested the model through end-to-end ordinary operation, Judge/Panel exceptions, dual-role behavior, lost/shared devices, interrupted authoritative transitions, paper recovery, duplicate/concurrent inputs, invalid Encounter/rejudge, post-event amendments, post-Finalization correction, disclosure failures, Administrator/break-glass misuse, stale derived state, and regional infrastructure failure. The sixteen-Concept catalog survived without a generic Workflow/Recovery/Incident/Conflict/Break-glass/Reconciliation Concept.

007-F then re-audited the Phase 003 Judge/Organizer experience architecture against that refined current model. Material interactions remain traceable to Concept actions, queries, synchronizations, derived projections, working state, or implementation-only interaction state. UI modes, confirmations, exception rows, readiness indicators, and enabled controls do not create semantic authority. Current cross-cutting UX authority now lives in [Experience Action, State & Authority Traceability](canonical/experience/action-authority-traceability.md).

The 006-D executable substrate remains in the repository because it is intentionally semantically thin. It is **not** authority to continue 006-E onward.

While frozen, executable changes are limited to narrow maintenance required to keep that prototype safe/buildable and must not encode MUDAC domain semantics.

## Why Phase 005 was not erased

[005-J](005-system-application-data-synchronization-architecture/005-J-phase-005-consolidation-threat-failure-review-implementation-readiness-exit.md) remains historical provenance for the earlier conclusion that architecture was implementation-planning ready. The later human decision recorded in [007-A](007-design-refinement/007-A-design-reentry-implementation-freeze-jackson-completion-criteria.md) supersedes the assumption that implementation should continue immediately.

Historical records are preserved rather than rewritten to make earlier decisions appear never to have happened.

## Current next work

Proceed through [Phase 007](007-design-refinement/) with **007-G — Policy, Representation, Outcome, Disclosure & Operational-Governance Closure Audit**. The renewed design runway continues until a dedicated later Jackson-methodology exit explicitly authorizes implementation to resume.
