---
type: Documentation Authority
title: Design / Implementation Boundary
description: Defines MUDAC's current design-reentry state, the 006-D implementation freeze, permitted maintenance, prohibited domain implementation, and the evidence required before implementation may resume.
status: stable
tags: [governance, methodology, design, implementation, freeze, jackson]
sources:
  - resource: ../../007-design-refinement/007-A-design-reentry-implementation-freeze-jackson-completion-criteria.md
  - resource: change-governance.md
  - resource: methodology-terminology.md
  - resource: ../implementation/runtime-delivery-bootstrap.md
  - resource: ../implementation/implementation-foundation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-05T01:23:00Z }
---

# Purpose

Keep MUDAC's current delivery state explicit after the human decision to stop implementation at the 006-D bootstrap boundary and return to deliberate design refinement.

This owner does not invalidate the historical Phase 005 architecture exit or erase Phase 006 work. It supersedes the earlier assumption that implementation should continue immediately from 006-D into persistence and feature foundations.

# Current state

MUDAC is in **design re-entry**.

Phase 006-A through 006-D remain accepted historical implementation-planning/bootstrap work. The executable workspace created in 006-D is retained as a **frozen non-domain bootstrap/prototype**.

006-E through 006-M are **deferred**. They are not the current work queue and must not be executed until a later explicit design-methodology exit authorizes implementation to resume.

# Frozen implementation boundary

The retained 006-D prototype may contain:

- pinned workspace/toolchain manifests and lockfile;
- empty/minimal API, worker and browser composition roots;
- package/module seams without domain behavior;
- local PostgreSQL service bootstrap without authoritative schema;
- CI, formatting, linting, type checking and dependency-boundary checks;
- OpenTofu environment/root scaffolding without production provisioning;
- supply-chain/security automation required to keep the prototype maintainable.

The freeze prohibits advancing into domain implementation, including by indirect or preparatory changes.

Do **not** add or materially implement:

- PostgreSQL domain schemas, migrations or authoritative persistence models;
- Kysely repositories for MUDAC domain state;
- Cognito integration, server sessions, Participation/Access enforcement or invitation flows;
- production API commands/queries, idempotency stores, transaction coordinators or generated domain clients;
- IndexedDB Draft semantics or domain browser-state implementations;
- Competition, Participation, Panel, Encounter, Rubric, Scorecard, Outcome, Award, Export, Artifact or Publication feature behavior;
- real AWS application-resource provisioning/deployment whose purpose is to support those deferred domain paths.

Creating a placeholder file or package for a prohibited path still counts as implementation advancement when it begins to encode the deferred behavior.

# Permitted work while frozen

The prototype may receive narrowly scoped maintenance needed to remain safe and usable as a future implementation substrate, for example:

- security fixes for existing bootstrap dependencies;
- compatibility fixes required to keep current validation/build checks functioning;
- documentation and design-routing updates;
- test/tooling fixes that do not add domain semantics;
- removal of accidental domain behavior if discovered.

Toolchain churn, architecture expansion, infrastructure provisioning, schema work, or feature scaffolding is not justified merely because the change can be described as maintenance.

# Design work is now authoritative work

Current work should return to product/concept/design refinement. Existing canonical concepts, mechanisms, policies, invariants, experience contracts and architecture remain inputs, not assumptions that the methodology has conclusively exited.

Where the renewed design finds a semantic defect or incomplete concept boundary, use `CHG-*` and update current canonical owners explicitly. Historical phase records remain append-stable provenance.

# Jackson-methodology completion gate

Implementation may resume only after an explicit later exit review demonstrates, at minimum:

1. **Concept completeness** — every accepted Concept has a current, traceable Purpose, State, Actions and Operational Principle, with subordinate state/mechanisms distinguished deliberately.
2. **Concept independence and genericity** — concept boundaries have been re-tested after later UX/architecture discoveries, with accidental application/UI/storage coupling removed.
3. **Synchronization completeness** — cross-concept synchronizations are consolidated with participating concepts, triggers, preconditions, postconditions, authority and failure/temporal consequences explicit.
4. **Temporal and correction closure** — Draft/finalized/current/historical/successor/invalidation/correction semantics compose without hidden state transitions.
5. **Scenario and adversarial pressure** — ordinary event-day, degraded, recovery, dual-role, paper/electronic, correction and authority-abuse scenarios do not expose missing concepts or contradictory synchronizations.
6. **Experience traceability** — Judge and Organizer experiences expose accepted concept actions/synchronizations rather than inventing semantics in interaction design.
7. **Policy/representation closure** — disclosure, anonymity, rights/authority, official/public distinction, paper capture, Export/Publication and operational policy remain conceptually consistent.
8. **Formal methodology exit** — a dedicated design exit review records remaining unknowns as implementation choices/evidence rather than unresolved concept or synchronization meaning.

A phase count by itself does not prove completion. The gate is evidence-based, but the renewed design runway is expected to continue through additional numbered phases rather than treating Phase 005 as the final design phase by default.

# Relationship to Phase 005 and Phase 006

005-J remains historical evidence of the earlier architecture assessment and must not be rewritten retroactively. Its conclusion that MUDAC was implementation-planning ready is superseded prospectively by the later human decision to require further design-methodology closure.

Phase 006 is **Frozen after 006-D** rather than complete. 006-E through 006-M remain preserved as a deferred implementation plan that may be revised or superseded after the design exit.

# Resume authority

Implementation beyond the frozen boundary resumes only through an explicit human/design decision after the later design exit. An agent must not infer resume authority from:

- the existence of executable code;
- green Implementation Verification;
- the prior 005-J exit;
- the existence of deferred 006-E through 006-M plans;
- a framework, database or infrastructure task appearing technically ready.
