---
type: Implementation Planning Reconciliation
title: 008-C — Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix
description: Ingests the accepted 007-H/007-I residual register and 008-B evidence limits into explicit Phase 008 owners, maps historical 006-E through 006-M into the refreshed plan, records phase-local planning decisions, and prevents future-scope or superseded work from re-entering execution implicitly.
status: stable
tags: [phase-008, implementation-planning, residual-risk, supersession, decision-register, dependency, provenance]
sources:
  - resource: 008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md
  - resource: 008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md
  - resource: ../007-design-refinement/007-H-cross-layer-design-completeness-residual-semantic-risk-jackson-methodology-exit-readiness-audit.md
  - resource: ../007-design-refinement/007-I-formal-jackson-concept-design-methodology-exit-accepted-residual-uncertainty-implementation-resume-boundary-decision.md
  - resource: ../006-implementation-planning/README.md
  - resource: ../canonical/governance/design-implementation-boundary.md
  - resource: ../canonical/governance/change-governance.md
  - resource: ../canonical/implementation/implementation-foundation.md
  - resource: ../canonical/implementation/runtime-delivery-bootstrap.md
  - resource: ../canonical/implementation/verification-strategy.md
  - resource: ../canonical/implementation/source-topology.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T18:00:00Z }
---

# Purpose

Convert the accepted post-Concept-Design residual uncertainty into an explicit, dependency-safe implementation-planning ownership map before Phase 008 begins selecting concrete persistence, authentication, API, browser, domain-slice, externalization, or operational mechanisms.

008-C also closes the ambiguity around historical Phase 006. The old 006-E through 006-M sequence is preserved as provenance, but each item now receives an explicit current disposition rather than remaining a vague deferred queue that an agent could accidentally resume.

The governing questions are:

1. Does every 007-H Class 2 architecture detail have a current Phase 008 planning owner?
2. Does every 007-H Class 3 implementation/evidence question have a current Phase 008 planning owner and dependency placement?
3. Are all 007-H Class 4 items explicitly excluded from the current baseline unless change governance reopens them?
4. Are the two 008-B administration/evidence limitations carried into later gates rather than forgotten?
5. Is every historical 006-E through 006-M item explicitly preserved, split, merged, renamed, reordered, or superseded?
6. Are implementation choices that remain genuinely open distinguishable from decisions already made by 008-A through 008-C?

# Result

**PASS — all accepted residuals and historical deferred implementation-planning work now have explicit current ownership or explicit exclusion.**

No new semantic blocker was discovered. No historical 006-E through 006-M item remains an executable queue entry. No 007-H Class 2 or Class 3 item remains unowned. No Class 4 future-scope item is admitted into the current baseline.

The current posture is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — protected 006-D baseline qualified
008-C: COMPLETE — residual and historical-plan ownership closed
008-D: NEXT
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

008-C is reconciliation and planning only. It creates no domain schema, command, API, authentication/session behavior, browser domain state, feature implementation, or AWS application resource.

# Reconciliation principles

## Current authority beats historical slice labels

Historical 006-E through 006-M names describe the implementation plan as it existed before the renewed Phase 007 design work. They are evidence of dependency intent, not a source of current semantic or execution authority.

The refreshed Phase 008 owners may therefore split, combine, move, or narrow historical work where the completed design shows that doing so preserves authority more faithfully.

## One current owner, explicit downstream consumers

A residual may affect several later subgroups, but 008-C identifies a primary planning owner wherever possible. Required downstream consumers are recorded so a concern is not duplicated as several independent sources of truth.

## Mechanism decisions remain downstream

Where 007-H deliberately left a physical or operational mechanism open, 008-C assigns the decision to the correct subgroup rather than deciding it prematurely.

## Future scope remains outside the baseline

A future feature does not become baseline merely because a database column, route, queue, or component would be easier to add now. Bringing Class 4 scope into the current plan requires deliberate `CHG-*` governance and any necessary renewed Concept/experience/policy work.

# Class 2 residual ownership matrix

The six accepted Class 2 architecture details are all carried forward.

| 007-H residual | Primary Phase 008 owner | Required downstream consumers | Current disposition |
| --- | --- | --- | --- |
| A2-01 Physical temporal model | **008-D** | 008-F, 008-G, 008-H, 008-I, 008-J | Decide relational representation for stable identity, currentness, Version lineage, supersession, invalidation, replacement, occurrence/effective/correction time, Affected/Stale state and reconstructible history. No mandatory bitemporal implementation is assumed. |
| A2-02 Governed-exception realization | **008-D** for durable representation | 008-F command/authority contract; 008-H–J policy-specific use; 008-K evidence | Define a persistence envelope that preserves source condition, scope, authorizer, reason, consequence and history without creating a generic semantic override. Later command and domain-slice plans consume that substrate. |
| A2-03 Official Outcome Revision materialization | **008-D** for physical/versioning substrate | **008-J** for exact finalization/outcome semantics | Plan a durable immutable/reconstructible representation without promoting Official Outcome Revision to a Concept. 008-J binds it to exact Coverage/Rank/Award/policy/evidence basis and succession semantics. |
| A2-04 Artifact versus Export physical realization | **008-J** | 008-D only for generic storage/history primitives where needed; 008-K for security/retention evidence | Keep Export as the Concept and Artifact bytes/metadata as supporting representation machinery. Renderer, byte integrity, storage and delivery choices remain for 008-J. |
| A2-05 Cross-module atomicity/coordinator placement | **008-F** | 008-D transaction substrate; 008-H–J domain consumers | Decide application/coordinator placement and transaction ownership without centralizing semantic ownership. Shared-database atomicity remains available but not mandatory for every synchronization. |
| A2-06 Projection refresh/freshness implementation | **008-D** for outbox/projection substrate | 008-F query/freshness contract; 008-H–J projections; 008-K rebuild/operational evidence | Choose synchronous/asynchronous realization per projection while preserving source basis, currentness and uncertainty. Projection storage never becomes write authority. |

### Class 2 closure

All six Class 2 items are now **owned downstream implementation decisions**, not latent semantic work.

008-D is intentionally the first detailed planning group because four of the six residuals require a durable relational/history/outbox substrate before Identity, API, browser, or domain-slice planning can safely assume implementation mechanics.

# Class 3 implementation/evidence ownership matrix

| 007-H residual | Primary Phase 008 owner | Secondary / gate owner | Current disposition |
| --- | --- | --- | --- |
| I3-01 Persistence/schema/migration implementation | **008-D** | 008-K verification; 008-L authorization | Full persistence, migration, Version/Provenance, outbox and projection planning. |
| I3-02 Authentication/session/Access implementation | **008-E** | 008-K security/privacy evidence | Provider authentication, stable Identity linkage, Participation context, Access, sessions, invitations, reverification, device recovery, dual-role isolation and technical-authority separation. |
| I3-03 Command/query/API/concurrency realization | **008-F** | 008-K security/concurrency evidence | DTO boundaries, transactions, CAS, idempotency, lost-response reconciliation, semantic errors, CSRF/request integrity and projection freshness. |
| I3-04 Browser Draft and conflict continuity | **008-G** | 008-K accessibility/security evidence | IndexedDB lifecycle, synchronization, conflict preservation, Access-expiry cleanup, responsive behavior and no-offline-authority constraint. |
| I3-05 Paper capture tooling | **008-I** | 008-K accessibility/continuity evidence | Physical-source identity, capture/verification, duplicate convergence, retained evidence and event-day procedures tied to the same logical Scorecard authority. |
| I3-06 Export/Artifact/Publication tooling | **008-J** | 008-K security/accessibility/retention evidence | Renderer/template/print, byte integrity/storage, disclosure validation, delivery, regeneration/supersession and `EXPORT-003`/`PUB-001` realization. |
| I3-07 Governed-exception command/evidence implementation | **008-F** for command/authority shape | 008-D persistence; 008-H–J policy-specific consequence; 008-K evidence | No universal override endpoint. Each allowed exception must bind to its governing semantic owner and preserve source truth/provenance. |
| I3-08 Security/privacy verification | **008-K** | 008-L authorization gate | Derive threat/abuse, role isolation, replay, CSRF, disclosure, admin/break-glass and protected-artifact evidence from the completed plan. |
| I3-09 Accessibility verification | **008-K** | 008-G/I/J provide target flows/artifacts; 008-L gate | Automated/manual assistive-technology, responsive, confirmation, paper and external-representation evidence. |
| I3-10 Performance/continuity/DR evidence | **008-K** | 008-L gate | Workload assumptions, SLOs, load, restore, projection rebuild, paper fallback, regional recovery and operational exercises. |
| I3-11 Repository/delivery governance | **008-K** | **008-L** must classify any remaining external gate before authorization | Actual merge/deployment protection evidence, required-check policy, environment protection and release authority; documentation alone remains insufficient. |
| I3-12 Retention/deletion policy realization | **008-K** for requirement/evidence gate | **008-D** must plan safe non-destructive defaults and deletion-capable mechanisms only when authorized | Destructive automation cannot be enabled until applicable product/legal/operational retention requirements are known. Historical evidence is preserved by default where current semantics require it. |

### Class 3 closure

Every Class 3 item is assigned to a current Phase 008 owner. None is treated as implementation already completed merely because the qualified 006-D substrate contains tooling or placeholders relevant to it.

# 008-B residual ingestion

008-B produced two explicit evidence/administration limitations that were not part of the original 007-H list. They are now incorporated rather than left only in the qualification record.

| 008-B residual | Owner | Required closure |
| --- | --- | --- |
| Repository rulesets/branch-protection enforcement not established | **008-K**, with **008-L** authorization dependency | Re-query/configure through available repository administration outside this integration as appropriate; 008-L must not claim enforced merge governance unless evidence exists or explicitly bound the limitation for the authorized slice. |
| Dependabot alert inventory unavailable through current connector | **008-K** | Obtain an applicable dependency-security evidence source before production-readiness claims; configured Dependabot/CodeQL remains control evidence, not proof of zero findings. |

The final 008-B bootstrap head `959e2b55e2273c3b86e61779cf821bbc890a76f1` subsequently passed Implementation Verification and CodeQL. That evidence strengthens the qualified substrate but does not close either administration limitation and does not authorize domain implementation.

# Class 4 exclusion register

The seven 007-H Class 4 items remain explicitly outside the current baseline.

| Future-scope item | Current disposition | Re-entry rule |
| --- | --- | --- |
| F4-01 Formal Stage/Round | **EXCLUDED** | Requires fresh Concept discovery if brought into scope; do not overload Division/Competition lifecycle. |
| F4-02 Student application experience | **EXCLUDED** | Requires actor/experience/disclosure/policy design before implementation. |
| F4-03 Formal scheduling/room/time-slot optimization | **EXCLUDED** | Requires deliberate discovery; do not hide scheduling semantics inside Encounter fields. |
| F4-04 Notifications | **EXCLUDED** | Requires product/consent/preference/disclosure/delivery-history design; transport alone is not authority. |
| F4-05 Advanced Judge calibration/normalization | **EXCLUDED** | Requires explicit Evaluation Policy redesign before it can affect official scoring. |
| F4-06 Rich public-results application | **EXCLUDED** | Requires separate public experience/disclosure/indexing/correction/accessibility/freshness design. |
| F4-07 Advanced Award governance | **EXCLUDED** | Requires new Award-governance design for committees, nominations, appeals, external adjudicators or multi-approval authority. |

No Phase 008-D through 008-L plan may silently introduce these items as “supporting” schema, API, browser, infrastructure, fixture or test scope.

# Historical 006-E through 006-M supersession matrix

The historical plan remains useful because its dependency direction was broadly sound, but its decomposition is no longer the active roadmap.

| Historical group | Historical topic | Current Phase 008 disposition | Reason |
| --- | --- | --- | --- |
| 006-E | Persistence, Schema, Migration, Provenance, Outbox & Projection Foundation | **PRESERVE + EXPAND → 008-D** | Core dependency order remains correct, but current planning must add Phase 007 temporal truth, invalidation/replacement, governed exceptions, Official Outcome Revision substrate, Affected/Stale and retention safeguards. |
| 006-F | Identity, Session, Access, Security & Invitation Foundation | **PRESERVE + EXPAND + RENAME → 008-E** | Adds Participation context, reverification/device recovery, secrets boundary, explicit technical/semantic-authority separation and Event Completed access expiry. Security evidence itself moves to 008-K. |
| 006-G | API, Commands, Queries, Transactions, Idempotency & Concurrency Foundation | **PRESERVE + EXPAND → 008-F** | Adds CAS, unknown-commit/lost-response reconciliation, semantic error taxonomy, authority postcondition confirmation, CSRF/request integrity and projection-freshness contracts. |
| 006-H | Browser Shell, Routing, Remote/Local State, Component Primitives & Accessibility Foundation | **PRESERVE + NARROW/EXPAND → 008-G** | Browser shell and remote/local state remain here; Draft continuity/conflict work is deliberately pulled forward from old 006-J because browser authority/recovery must be designed before vertical feature slices. Accessibility behavior is planned here while cross-cutting evidence consolidates in 008-K. |
| 006-I | Competition Setup, Participation & Judging Operations Vertical Slice | **PRESERVE + EXPAND → 008-H** | Adds Team/Division/Alias/Rubric planning and explicit Panel-versus-effective-Encounter participation, snapshots, invalidation/replacement and exception-projection constraints. |
| 006-J | Evaluation, Scorecard, Draft Synchronization, Conflict & Paper-Capture Vertical Slice | **SPLIT → 008-G + 008-I** | Generic browser Draft/sync/conflict foundation moves to 008-G; authoritative Scorecard/evaluation/amendment/paper/convergence remains in 008-I. This prevents browser persistence mechanics from being invented inside the evaluation slice. |
| 006-K | Reconciliation, Coverage, Ranking, Awards, Finalization & Official Outcome Vertical Slice | **PRESERVE + EXPAND → 008-J** | Must add latest-declared-official + Affected, explicit successor official confirmation, non-editable projections, governed exceptions and exact official-basis semantics. |
| 006-L | Export, Artifact, Publication, Print & External Representation Vertical Slice | **MERGE INTO 008-J** | Externalization is downstream of reconciliation/finalization/outcome authority and should be planned in the same dependency group so Export/Publication cannot drift from exact source/disclosure/official-currentness semantics. Artifact remains supporting architecture, not a new Concept. |
| 006-M | Integrated Security, Observability, Performance, Recovery, Operational Readiness & Phase Exit | **SPLIT → 008-K + 008-L** | Cross-cutting security/privacy/accessibility/observability/performance/recovery/retention evidence belongs in 008-K. Consolidated roadmap, unresolved-risk classification, first-slice authorization and Phase 008 exit belong in 008-L. |

### Historical queue verdict

The 006-E through 006-M sequence is now **fully superseded as an executable roadmap**.

Its provenance remains valuable, but current planning proceeds only through 008-D through 008-L. Agents must not infer that “006-E was next historically” creates permission to implement persistence before 008-L authorization.

# Current refreshed dependency map

008-C confirms the Phase 008 dependency direction without yet designing the detailed contents of later groups:

```text
008-D durable relational / temporal / history / provenance / exception / outbox substrate
   ↓
008-E Identity / Participation / Access / session / invitation / secrets
   ↓
008-F commands / queries / transactions / CAS / idempotency / API
   ↓
008-G browser shell / remote state / local Draft / conflict / recovery / accessibility behavior
   ↓
008-H Competition preparation + Judging Operations
   ↓
008-I Scorecard evaluation evidence + amendment + paper convergence
   ↓
008-J reconciliation + derived outcomes + Finalization + official outcome + Export + Publication
   ↓
008-K cross-cutting security / privacy / accessibility / operations / performance / recovery / retention evidence
   ↓
008-L consolidated roadmap + explicit Phase 009 first-slice authorization decision
```

This is a planning dependency graph, not an instruction to begin coding each layer serially. 008-L may authorize later implementation parallelism where dependency evidence supports it.

# Phase-local decision register

The following decisions are made by 008-C. Their numbering is local to this phase record and intentionally does not create a new stable-rule namespace.

### Decision 1 — retain the qualified 006-D substrate

The 006-D non-domain workspace remains the implementation starting substrate. No replacement toolchain/topology migration is justified by current evidence.

### Decision 2 — supersede the historical 006-E through 006-M execution queue

The old queue remains historical provenance only. Current work must route through 008-D through 008-L.

### Decision 3 — preserve dependency intent, not historical slice boundaries

Persistence precedes Identity/Access; Identity/Access precedes transport; server authority precedes browser continuity; operational domain context precedes evaluation evidence; evaluation evidence precedes outcomes/externalization; cross-cutting evidence precedes first-slice authorization.

The exact historical slice boundaries are not preserved when Phase 007 demonstrates a cleaner authority boundary.

### Decision 4 — move browser Draft/synchronization foundation ahead of evaluation implementation planning

Old 006-J mixed evaluation semantics with browser continuity mechanics. 008-G now owns the generic browser Draft/conflict/recovery substrate so 008-I can consume it without redefining Scorecard authority.

### Decision 5 — combine outcomes and externalization planning

Old 006-K and 006-L become one 008-J dependency group. This keeps Coverage/Aggregate/Rank/Finalization/Official Outcome Revision/Export/Publication/disclosure in one downstream authority chain while preserving their semantic distinctions.

### Decision 6 — split integrated readiness from phase authorization

Old 006-M combined evidence generation with phase exit. 008-K owns evidence/readiness planning; 008-L independently decides whether the first Phase 009 slice is actually authorized.

### Decision 7 — keep Class 4 outside the baseline

No future-scope item is added merely to simplify implementation. Re-entry requires explicit change governance.

### Decision 8 — do not create a parallel canonical decision store yet

008-C itself is the planning/provenance owner for this mapping. Later subgroups must promote durable implementation choices into the applicable canonical implementation owner when `IMPL-015` requires it rather than accumulating a second generic “current decisions” document.

# Downstream decision register — intentionally open

008-C does not prematurely choose implementation details that belong to later groups. The following decisions remain intentionally open and are now explicitly owned:

| Open decision | Owner | Must preserve |
| --- | --- | --- |
| Physical relational temporal/history pattern | 008-D | current/history, Version lineage, invalidation, replacement, correction/as-known truth, Affected/Stale |
| Governed-exception persistence pattern | 008-D | source truth, explicit scope/authorizer/reason/consequence/history, no generic semantic override |
| Official Outcome Revision storage/materialization | 008-D + 008-J | exact declared basis, immutability/reconstructibility, explicit succession |
| Outbox/projection storage and refresh strategy | 008-D | authority-establishing vs convergent distinction, source basis/freshness |
| Authentication provider adapter/session representation details | 008-E | stable Identity, contextual Participation/Access, technical privilege separation |
| Transaction coordinator placement and cross-module atomicity | 008-F | module ownership, lost-response reconciliation, idempotency/CAS |
| API DTO/schema/error/idempotency-key details | 008-F | transport isolation, semantic pre/postconditions, truthful uncertainty |
| IndexedDB Draft data lifecycle and conflict protocol | 008-G | Draft non-authority, privacy, Access expiry, stale-base recovery |
| Domain slice internal decomposition for preparation/live operations | 008-H | Concept ownership, effective Encounter participation, current/history snapshots |
| Scorecard/paper capture physical mechanics | 008-I | one logical Scorecard, Judge authorship, exact Rubric Version, verified convergence |
| Renderer/artifact-byte/storage/delivery mechanisms | 008-J | `EXPORT-003`, `PUB-001`, disclosure, exact source basis, historical externalization |
| Security/accessibility/load/recovery/retention evidence thresholds | 008-K | current canonical risk/experience/operations contracts |
| Repository/admin merge/deploy protection sufficiency | 008-K + 008-L | do not promote workflow existence to enforced governance |
| Dependency-vulnerability evidence source | 008-K | do not infer zero findings from inaccessible alert inventory |
| First executable Phase 009 slice | 008-L | smallest dependency-safe authorized scope with explicit evidence gates |

An open decision is not a blocker merely because it is not decided in 008-C. It becomes a blocker only if its assigned owner cannot resolve it without contradicting upstream canonical meaning or if 008-L cannot bound it safely for authorization.

# No new semantic change discovered

The reconciliation did not identify:

- a missing Concept;
- a contradictory current canonical rule;
- a need for a generic Workflow/Exception/Override/Outcome/Artifact Concept;
- a reason to change the accepted modular-monolith architecture;
- a reason to replace the retained 006-D toolchain family;
- a need to admit Class 4 future scope.

Therefore no `CHG-*` design change is opened by 008-C.

# No new stable rule identifiers

008-C introduces no new durable normative rule family. The durable constraints already belong to canonical `DOC-*`, `CTX-*`, `CHG-*`, `IMPL-*`, architecture rules, temporal/synchronization rules, `OPG-*`, `EXPORT-003`, `PUB-001`, and the Design / Implementation Boundary.

The matrices and numbered decisions in this document are Phase 008 planning provenance and routing. They must not be copied into a new competing rule registry.

# Exit criteria

008-C is complete because:

- all six 007-H Class 2 residuals have primary planning owners and downstream consumers;
- all twelve 007-H Class 3 items have current owners/gates;
- all seven Class 4 items are explicitly excluded from baseline implementation;
- both 008-B administration/evidence residuals have later closure owners;
- every historical 006-E through 006-M item has an explicit supersession disposition;
- the current dependency map is explicit;
- decisions made now are distinguished from implementation decisions intentionally deferred to later owners;
- no semantic blocker or required `CHG-*` work was discovered;
- no new domain implementation has begun.

# Handoff

Proceed to **008-D — Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan**.

008-D may rely on the qualified 006-D substrate and the ownership decisions in this record. It must resolve the assigned durable-data implementation decisions at planning level only. It still must not create domain schema/migrations/repositories or other new executable domain behavior because first-slice authorization remains reserved to 008-L and actual domain implementation begins in Phase 009.