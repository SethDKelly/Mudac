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
  - resource: change-governance.md
  - resource: methodology-terminology.md
  - resource: ../synchronizations/concept-synchronizations.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../implementation/runtime-delivery-bootstrap.md
  - resource: ../implementation/implementation-foundation.md
---

# Purpose

Keep MUDAC's current delivery state explicit after the human decision to stop implementation at the 006-D bootstrap boundary and return to deliberate design refinement.

This owner does not invalidate the historical Phase 005 architecture exit or erase Phase 006 work. It supersedes the earlier assumption that implementation should continue immediately from 006-D into persistence and feature foundations.

# Current state

MUDAC is in **design re-entry**.

Phase 006-A through 006-D remain accepted historical implementation-planning/bootstrap work. The executable workspace created in 006-D is retained as a **frozen non-domain bootstrap/prototype**.

006-E through 006-M are **deferred**. They are not the current work queue and must not be executed until a later explicit design-methodology exit authorizes implementation to resume.

# Frozen implementation boundary

The retained 006-D prototype may contain pinned workspace/toolchain manifests and lockfile; empty/minimal API, worker and browser composition roots; package/module seams without domain behavior; local PostgreSQL service bootstrap without authoritative schema; CI/static/dependency checks; OpenTofu environment/root scaffolding without production provisioning; and supply-chain/security automation needed to keep the prototype maintainable.

The freeze prohibits advancing into domain implementation, including by indirect or preparatory changes.

Do **not** add or materially implement domain PostgreSQL schema/migrations/repositories; Cognito/session/Participation/Access/invitation behavior; production domain command/query/idempotency/transaction behavior; IndexedDB Draft semantics; Competition/Judging/Evaluation/Outcome/Award/Export/Publication feature behavior; or real AWS application-resource provisioning intended to advance those deferred paths.

Creating a placeholder file or package for a prohibited path still counts as implementation advancement when it begins to encode the deferred behavior.

# Permitted work while frozen

The prototype may receive narrowly scoped maintenance needed to remain safe and usable as a future substrate, such as dependency security fixes, compatibility repairs required to keep existing checks functioning, documentation/design-routing updates, non-domain test/tooling fixes, or removal of accidental domain behavior.

Toolchain churn, architecture expansion, infrastructure provisioning, schema work, or feature scaffolding is not justified merely because it can be described as maintenance.

# Design work is now authoritative work

Current work proceeds through product/concept/design refinement. Existing canonical concepts, synchronizations, mechanisms, policies, invariants, experience contracts and architecture remain inputs, not assumptions that the methodology has conclusively exited.

Where renewed design finds a semantic defect, use `CHG-*` and update current canonical owners explicitly. Historical phase records remain append-stable provenance.

# Current design-progress evidence

## 007-B — Concept catalog evidence

007-B completed the post-architecture Concept catalog audit: all fifteen prior Concepts survived independence/genericity review, current owners expose Purpose/State/Actions/Operational Principle, Publication was promoted as the sixteenth Concept, and subordinate/derived candidates were re-tested without promotion merely because architecture gives them technical state.

## 007-C — Synchronization evidence

007-C consolidated current cross-concept composition into [Concept Synchronization Contracts](../synchronizations/concept-synchronizations.md): material triggers, preconditions, authority seams and postconditions are explicit; authority-establishing versus derived/convergent effects are distinguished; duplicate/lost-response/uncertain-outcome meaning is explicit at the design level; exceptional event resume does not auto-restore authority; and no synchronization revealed another missing Concept.

## 007-D — Temporal/correction evidence

007-D consolidated [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md):

- lifecycle, working/committed authority, lineage currentness, validity/eligibility, affected/stale currency, replacement, release state and historical observation are independent dimensions;
- semantic amendment, capture correction, structural correction, provenance correction and official/public correction remain distinct;
- invalidation never silently revives an older predecessor and may leave no current eligible authority;
- invalidated Encounter evidence remains historical while becoming ineligible for ordinary official use;
- as-known historical authority is distinguishable from later corrected best-known occurrence history;
- occurrence/effective time can differ from later capture/authority/correction time without mandating a particular database model;
- latest-declared-official + Affected semantics preserve the official boundary before explicit successor confirmation;
- Export currency and Publication distribution state remain separate.

These close substantial portions of the methodology gate but **do not authorize implementation**. Scenario/adversarial, experience-traceability, policy/representation and formal-exit evidence remain open.

# Jackson-methodology completion gate

Implementation may resume only after an explicit later exit review demonstrates, at minimum:

1. **Concept completeness** — every accepted Concept has current, traceable Purpose, State, Actions and Operational Principle, with subordinate state/mechanisms deliberately distinguished. **007-B evidence exists; final exit must confirm it remains valid.**
2. **Concept independence and genericity** — boundaries have been re-tested after later UX/architecture discoveries. **007-B evidence exists; Publication was added from this pressure test.**
3. **Synchronization completeness** — cross-concept synchronizations have explicit participants, triggers, preconditions, postconditions, authority and failure consequences. **007-C evidence exists; final exit must confirm it survives later pressure.**
4. **Temporal and correction closure** — Draft/finalized/current/historical/successor/invalidation/correction semantics compose without hidden transitions. **007-D evidence exists; final exit must confirm it survives scenario and experience pressure.**
5. **Scenario and adversarial pressure** — ordinary event-day, degraded, recovery, dual-role, paper/electronic, correction and authority-abuse scenarios do not expose missing Concepts or contradictory synchronizations.
6. **Experience traceability** — Judge and Organizer experiences expose accepted Concept actions/synchronizations rather than inventing semantics.
7. **Policy/representation closure** — disclosure, anonymity, rights/authority, official/public distinction, paper capture, Export/Publication and operational policy remain conceptually consistent.
8. **Formal methodology exit** — a dedicated design exit records remaining unknowns as implementation choices/evidence rather than unresolved semantic meaning.

A phase count by itself does not prove completion. The gate is evidence-based and the renewed design runway continues until these conditions are explicitly satisfied.

# Relationship to Phase 005 and Phase 006

005-J remains historical evidence of the earlier architecture assessment and is not rewritten retroactively. Its implementation-planning-ready conclusion is superseded prospectively by the later human decision to require further design-methodology closure.

Phase 006 is **Frozen after 006-D** rather than complete. 006-E through 006-M remain preserved as a deferred implementation plan that may be revised or superseded after the design exit.

# Resume authority

Implementation beyond the frozen boundary resumes only through an explicit human/design decision after the later design exit. An agent must not infer resume authority from executable code, green CI, the prior 005-J exit, deferred 006-E–M plans, or a technically ready framework/database/infrastructure task.
