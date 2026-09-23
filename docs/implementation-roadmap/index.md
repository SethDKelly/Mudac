# MUDAC Autonomous Implementation Roadmap

**Authority:** Phase 020-K final planning projection  
**Execution:** NOT AUTHORIZED  
**Package G1:** 15/15 READY_FOR_AUTHORIZATION  
**Package G2:** 0/15

Machine authority: `docs/routing/phase020_autonomous_implementation_roadmap.json`.

## Lifecycle rule

~~~text
Phase 020 planning
  -> package G1 READY_FOR_AUTHORIZATION
  -> explicit phase start gate
  -> explicit human/program G2 for named package set
  -> isolated autonomous implementation
  -> evidence / independent review / adversarial review
  -> G5 package completion
  -> next phase eligible, not authorized
~~~

G1 is planning completeness. It is not coding permission.

## Agent operating pattern

Each implementation phase uses one independent **Coordinator** run. The Coordinator owns the declared work-unit graph, context manifests, worktree allocation, serialized-surface leases, integration order and escalation.

Preferred tool profiles are deliberately non-normative:

- **Cursor** — preferred for browser-heavy and semantic-owner verticals where interactive repository-local context is especially useful.
- **Codex** — preferred for repository topology, persistence/runtime/evidence infrastructure and bounded cross-file transformations.
- **Reciprocal review** — prefer Codex review of Cursor-authored candidates and Cursor review of Codex-authored candidates. Same-provider independent review remains allowed if the run/context is independent.

Provider choice never creates semantic, lifecycle or gate authority.

## Serialized surfaces

Parallel work is allowed only through isolated worktrees. A phase Coordinator serializes overlapping:

- root lockfile/workspace manifests;
- migration catalogs;
- shared API contract indexes;
- shared client shell/navigation;
- test fixture/MCP capability registries;
- CI/evidence schemas;
- OpenTofu roots/backends;
- deployment workflows.

A serialized surface has one writer at a time even if the phase permits several concurrent work units.

## Implementation phases

| Phase | Packages | Parallelism | Purpose |
|---|---|---:|---|
| **021** | IMP-001 | 1 | Repair source topology and executable implementation foundation. |
| **022** | IMP-002, IMP-004, IMP-005, IMP-006 | ≤3 | Build persistence, browser/client, test-control and non-production runtime foundations. |
| **023** | IMP-003, IMP-014 | ≤2 | Build command/transaction/reconciliation and exact-revision verification/evidence foundations. |
| **024** | IMP-007 | 1 | Implement Competition Context natural-owner vertical. |
| **025** | IMP-008 | 1 | Implement Identity, Participation, Access and session vertical. |
| **026** | IMP-009 | 1 | Implement Evaluation natural-owner vertical. |
| **027** | IMP-010, IMP-011 | ≤2 | Implement continuity/reconciliation and Outcomes/Officiality in parallel. |
| **028** | IMP-012, IMP-013, IMP-015 | ≤3 | Complete external representation, projections and production-shaped runtime/recovery infrastructure. |
| **029** | V1-FINAL | ≤3 | Whole-system PF-01 integration/hardening and v1 implementation completion. |

## Phase 021 — Source Topology & Implementation Foundation

**Package:** IMP-001  
**Preferred implementer:** Codex  
**Preferred reviewer:** Cursor

Entry requires Phase 020 closure, exact baseline, observed repository enforcement needed by the current control model, IMP-001 still G1-ready, and explicit G2.

Exit requires IMP-001 G5. Later phases may not assume the repaired five-owner executable topology before this closes.

## Phase 022 — Persistence, Browser, Test-Control & Non-Production Runtime Foundations

**Packages:** IMP-002, IMP-004, IMP-005, IMP-006

After 021, these foundations are intentionally parallelizable. The Coordinator may run at most three independent work units concurrently; lockfile/shared configuration and provider roots remain serialized.

IMP-002 establishes real PostgreSQL/migration/history/projection substrate.  
IMP-004 establishes client state/accessibility foundations.  
IMP-005 establishes the non-production MCP/test-control foundation.  
IMP-006 establishes provider-backed NPT-P/NPT-S runtime infrastructure.

Phase exit requires G5 for all four packages plus their declared integration evidence.

## Phase 023 — Command, Transaction & Verification Evidence Foundations

**Packages:** IMP-003, IMP-014

IMP-003 realizes command/query, transaction, idempotency, lost-response and reconciliation contracts.

IMP-014 realizes exact-SHA evidence, protected evaluation and supply-chain verification infrastructure.

They may execute in isolated worktrees while shared CI/contract surfaces are serialized. Exit requires both G5.

## Phase 024 — Competition Context Vertical

**Package:** IMP-007  
**Preferred implementer:** Cursor  
**Preferred reviewer:** Codex

This is the first semantic-owner vertical. It realizes the Competition Context natural owner, organizer setup, owner persistence/history and stable downstream references.

No Identity/Access, Evaluation, Outcomes or Publication semantics may migrate into this phase.

## Phase 025 — Identity, Participation, Access & Session Vertical

**Package:** IMP-008  
**Preferred implementer:** Cursor  
**Preferred reviewer:** Codex

Requires Competition Context G5. Current contextual Access, session lifecycle, Cognito adapter and shared-device privacy are implemented without delegating MUDAC authority to the provider.

## Phase 026 — Evaluation Vertical

**Package:** IMP-009  
**Preferred implementer:** Cursor  
**Preferred reviewer:** Codex

Requires 025 closure. Implements Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard Draft/Finalization, authorship and correction history.

This is treated as a high-semantic-density phase; hidden complexity is not a reason to broaden scope.

## Phase 027 — Continuity & Outcomes Parallel Verticals

**Packages:** IMP-010, IMP-011

After Evaluation G5:

- IMP-010 implements offline/multi-device/paper/reconciliation continuity.
- IMP-011 implements Coverage/Aggregate/Rank, Award and Outcome Declaration officiality.

The packages may progress in parallel because neither is the semantic owner of the other. Shared Evaluation and organizer surfaces are integrated in a controlled order.

## Phase 028 — Representation, Projections & Production Runtime

**Packages:** IMP-012, IMP-013, IMP-015

This phase closes the remaining implementation packages:

- external Export/Artifact/Publication behavior;
- cross-owner read-only projections/operational views;
- production-shaped deployment, backup and recovery infrastructure.

IMP-015 implementation does not grant deployment, G6 or G7. Provider configuration is implementation evidence, not production authority.

## Phase 029 — PF-01 v1 Whole-System Integration & Hardening

**Logical alias:** V1-FINAL

029 owns only explicitly declared integration/hardening surfaces. It has no blanket authority to edit G5 package-owned source.

It qualifies one exact integrated PF-01 candidate against:

- V1-WS-01..12;
- JNY-01..09;
- SCN-01..15;
- accepted architecture;
- security/privacy/authority boundaries;
- migration/recovery;
- WCAG-oriented accessibility evidence;
- event-load/performance/cost evidence;
- supply-chain/provenance;
- independent and adversarial review.

A defect in completed package source uses 020-H reopen + explicit re-authorization.

Successful exit records:

> **V1_IMPLEMENTATION_COMPLETE**

and only advances to:

> **RELEASE_CANDIDATE_ELIGIBLE_NOT_AUTHORIZED**

## Package readiness

020-K records all fifteen retained package candidates as G1-complete because each now has:

- explicit scope and exclusions;
- semantic/architecture/engineering traceability;
- hard/integration/evidence dependencies;
- owned and serialized surfaces;
- package-specific visible success criteria;
- explicit evidence obligations;
- scenario and cross-cutting verification mappings;
- migration/security/accessibility/recovery/performance/cost classification;
- compatibility/rollback strategy;
- residual risks;
- review, repair, Gatekeeper and reopen policy;
- final implementation-phase assignment.

No package is active.

## Authorization order

G1 readiness does not imply every package can be authorized immediately.

Default G2 eligibility follows hard predecessors. The intended sequence is:

~~~text
021
 -> 022
 -> 023
 -> 024
 -> 025
 -> 026
 -> 027
 -> 028
 -> 029
~~~

Parallel packages inside a phase still require their named G2 inclusion.

An explicit independence finding may relax a hard-predecessor wait only where the governing gate permits it and evidence proves the downstream work cannot depend on unfinished semantics or surfaces.

## 020-L handoff

Phase 020-K does not start Phase 021.

020-L must first audit:

- roadmap/package completeness;
- G1 decisions;
- branch/ruleset enforcement evidence;
- validator/negative controls;
- status mirrors;
- residual risks;
- exact head;
- Phase-021 entry handoff.

Only after a successful 020-L exit may Phase 021 be presented for explicit G2 authorization.
