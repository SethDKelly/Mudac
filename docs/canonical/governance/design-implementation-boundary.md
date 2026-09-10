---
type: Documentation Authority
title: Design / Implementation Boundary
description: Defines MUDAC's current design-reentry state, the 006-D implementation freeze, permitted maintenance, prohibited domain implementation, and the evidence required before implementation may resume.
status: stable
tags: [governance, methodology, design, implementation, freeze, jackson]
sources:
  - resource: ../../007-design-refinement/007-A-design-reentry-implementation-freeze-jackson-completion-criteria.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
  - resource: ../../007-design-refinement/007-C-cross-concept-synchronization-completeness-authority-seam-audit.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
  - resource: ../../007-design-refinement/007-E-end-to-end-scenario-exception-failure-adversarial-authority-validation.md
  - resource: ../../007-design-refinement/007-F-judge-organizer-experience-concept-action-synchronization-authority-traceability-audit.md
  - resource: ../../007-design-refinement/007-G-policy-representation-outcome-disclosure-operational-governance-closure-audit.md
  - resource: ../../007-design-refinement/007-H-cross-layer-design-completeness-residual-semantic-risk-jackson-methodology-exit-readiness-audit.md
  - resource: change-governance.md
  - resource: methodology-terminology.md
  - resource: ../synchronizations/concept-synchronizations.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../policies/operational-exception-governance.md
  - resource: ../experience/action-authority-traceability.md
  - resource: ../implementation/runtime-delivery-bootstrap.md
  - resource: ../implementation/implementation-foundation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T08:12:00Z }
---

# Purpose

Keep MUDAC's current delivery state explicit after the human decision to stop implementation at the 006-D bootstrap boundary and return to deliberate design refinement.

This owner does not invalidate the historical Phase 005 architecture exit or erase Phase 006 work. It supersedes the earlier assumption that implementation should continue immediately from 006-D into persistence and feature foundations.

# Current state

MUDAC remains in **design re-entry**, but the design has now passed the 007-H cross-layer semantic exit-readiness audit.

That means:

```text
semantic exit readiness: PASS
formal Jackson methodology exit: NOT YET PERFORMED
implementation resume: NOT AUTHORIZED
```

Phase 006-A through 006-D remain accepted historical implementation-planning/bootstrap work. The executable workspace created in 006-D is retained as a **frozen non-domain bootstrap/prototype**.

006-E through 006-M remain **deferred**. They are not the current work queue and must not be executed until a later explicit design-methodology exit and implementation-resume decision authorize that transition.

# Frozen implementation boundary

The retained 006-D prototype may contain pinned workspace/toolchain manifests and lockfile; empty/minimal API, worker and browser composition roots; package/module seams without domain behavior; local PostgreSQL service bootstrap without authoritative schema; CI/static/dependency checks; OpenTofu environment/root scaffolding without production provisioning; and supply-chain/security automation needed to keep the prototype maintainable.

The freeze prohibits advancing into domain implementation, including by indirect or preparatory changes.

Do **not** add or materially implement domain PostgreSQL schema/migrations/repositories; Cognito/session/Participation/Access/invitation behavior; production domain command/query/idempotency/transaction behavior; IndexedDB Draft semantics; Competition/Judging/Evaluation/Outcome/Award/Export/Publication feature behavior; or real AWS application-resource provisioning intended to advance those deferred paths.

Creating a placeholder file or package for a prohibited path still counts as implementation advancement when it begins to encode the deferred behavior.

# Permitted work while frozen

The prototype may receive narrowly scoped maintenance needed to remain safe and usable as a future substrate, such as dependency security fixes, compatibility repairs required to keep existing checks functioning, documentation/design-routing updates, non-domain test/tooling fixes, or removal of accidental domain behavior.

Toolchain churn, architecture expansion, infrastructure provisioning, schema work, or feature scaffolding is not justified merely because it can be described as maintenance.

# Design work is now authoritative work

Current work remains product/concept/design refinement until the dedicated formal methodology-exit decision is made. Existing canonical concepts, synchronizations, mechanisms, policies, invariants, experience contracts and architecture are current inputs to that decision.

Where renewed design finds a semantic defect, use `CHG-*` and update current canonical owners explicitly. Historical phase records remain append-stable provenance.

# Current design-progress evidence

## 007-B — Concept catalog evidence

007-B completed the post-architecture Concept catalog audit: all fifteen prior Concepts survived independence/genericity review, current owners expose Purpose/State/Actions/Operational Principle, Publication was promoted as the sixteenth Concept, and subordinate/derived candidates were re-tested without promotion merely because architecture gives them technical state.

## 007-C — Synchronization evidence

007-C consolidated current cross-concept composition into [Concept Synchronization Contracts](../synchronizations/concept-synchronizations.md): material triggers, preconditions, authority seams and postconditions are explicit; authority-establishing versus derived/convergent effects are distinguished; duplicate/lost-response/uncertain-outcome meaning is explicit at the design level; exceptional event resume does not auto-restore authority; and no synchronization revealed another missing Concept.

## 007-D — Temporal/correction evidence

007-D consolidated [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md): lifecycle, working/committed authority, lineage currentness, validity/eligibility, affected/stale currency, replacement, release state and historical observation are independent dimensions; correction families remain distinct; invalidation does not revive an older predecessor automatically; historical evidence remains reconstructible; latest-declared-official + Affected semantics preserve official authority before explicit successor confirmation; and Export currency remains distinct from Publication distribution state.

## 007-E — Scenario/adversarial evidence

007-E pressure-tested ordinary, exceptional, degraded, concurrent, malicious, and recovery paths including Judge/Panel changes, dual roles, device loss/handoff, interrupted authoritative commands, paper recovery, duplicate/stale input, invalidation/rejudge, post-event amendment, post-Finalization correction, disclosure exposure, technical/break-glass misuse, replay, stale projections, and regional failure.

The sixteen-Concept system survived without a generic Workflow, Recovery, Incident, Conflict, Break-glass, or Reconciliation Concept. Technical/system power remains distinct from Competition semantic authority and actual disclosure exposure remains historical occurrence rather than something later revocation can erase.

## 007-F — Experience traceability evidence

007-F revalidated Judge/Organizer experience against the current Concept/action/synchronization/authority system. Material interaction maps to Concept action/query, synchronization consequence, derived projection, working state, or implementation-only interaction state.

[Experience Action, State & Authority Traceability](../experience/action-authority-traceability.md) now makes explicit that routes, work modes, controls, confirmations, exception rows, responsive variants, and recovery affordances cannot independently establish domain authority.

## 007-G — Policy/representation evidence

007-G integrated Evaluation Policy, Coverage, Panel composition, correction, Awards/Finalization, continuity, disclosure, Official Outcome Revision, Export/Publication, and operational governance.

[Operational Exception & Override Governance](../policies/operational-exception-governance.md) now prevents generic exception/force behavior from falsifying source truth, transferring Judge authorship, creating official/public authority, bypassing uncertainty, or converting technical privilege into Competition authority. Export/Publication owners also explicitly preserve representation authority monotonicity and purpose/source-specific Publication prerequisites.

## 007-H — Cross-layer exit-readiness evidence

007-H reconciled all current product/UX/policy/synchronization/architecture layers and classified residual work.

Its decisive result is:

- **no unresolved baseline semantic/design blocker is currently known**;
- remaining architecture questions are adequately constrained downstream choices;
- remaining persistence/API/auth/synchronization/rendering/security/operational work is implementation-planning or evidence work;
- Stage/Round, student self-service, formal scheduling, notifications, calibrated scoring, rich public-results browsing, and advanced Award governance remain deliberate future scope;
- the frozen 006-E through 006-M plan remains useful lineage but must be refreshed against Phase 007 before execution;
- MUDAC is ready for a dedicated formal Jackson methodology-exit decision.

007-H does **not** itself authorize implementation.

# Jackson-methodology completion gate

Implementation may resume only after an explicit later exit review demonstrates and records the following:

1. **Concept completeness** — current Purpose, State, Actions and Operational Principle for every accepted Concept. **PASS evidence: 007-B; revalidated by 007-H.**
2. **Concept independence and genericity** — boundaries re-tested after UX/architecture discoveries. **PASS evidence: 007-B; Publication added through that pressure; revalidated by 007-H.**
3. **Synchronization completeness** — participants, triggers, preconditions, postconditions, authority and failure consequences explicit. **PASS evidence: 007-C; survived 007-D through 007-H pressure.**
4. **Temporal and correction closure** — Draft/finalized/current/historical/successor/invalidation/correction semantics compose without hidden transitions. **PASS evidence: 007-D; survived later pressure.**
5. **Scenario and adversarial pressure** — ordinary event-day, degraded, recovery, dual-role, paper/electronic, correction and authority-abuse scenarios do not expose missing Concepts or contradictory synchronizations. **PASS evidence: 007-E.**
6. **Experience traceability** — Judge and Organizer experiences expose accepted Concept actions/synchronizations rather than inventing semantics. **PASS evidence: 007-F.**
7. **Policy/representation closure** — disclosure, anonymity, correction, official/public distinction, paper capture, Export/Publication and operational exceptions remain conceptually consistent. **PASS evidence: 007-G.**
8. **Cross-layer residual-risk classification** — design, architecture, implementation and future-scope unknowns are distinguishable; no known semantic blocker is deferred into implementation. **PASS evidence: 007-H.**
9. **Formal methodology exit** — a dedicated design exit records accepted residual uncertainty and the exact implementation-resume boundary. **NEXT — not yet performed.**

A phase count by itself does not prove completion. The gate is evidence-based.

# Relationship to Phase 005 and Phase 006

005-J remains historical evidence of the earlier architecture assessment and is not rewritten retroactively. Its implementation-planning-ready conclusion is still useful as architecture evidence, but the later human decision required explicit full-methodology closure before implementation could continue.

Phase 006 remains **Frozen after 006-D** rather than complete. 006-E through 006-M remain preserved as a deferred implementation plan that may be revised or superseded after the formal design exit.

007-H specifically recommends that any later implementation resume first refresh that dependency plan against the Phase 007 refinements rather than executing 006-E mechanically.

# Resume authority

Implementation beyond the frozen boundary resumes only through an explicit human/design decision after the dedicated formal methodology exit.

An agent must not infer resume authority from:

- the 007-H semantic exit-readiness result;
- executable code or toolchain readiness;
- green CI;
- the prior 005-J architecture exit;
- deferred 006-E–M plans;
- an apparently implementation-ready framework/database/infrastructure task.

# Current handoff

Proceed to **007-I — Formal Jackson Concept Design Methodology Exit, Accepted Residual Uncertainty & Implementation-Resume Boundary Decision**.

007-I must explicitly decide whether the methodology exits for the current baseline. If it passes, it must establish the exact post-exit governance posture and state whether implementation planning is authorized to resume, what plan-refresh step precedes domain coding, and which residual uncertainties remain accepted downstream decisions rather than unresolved design.
