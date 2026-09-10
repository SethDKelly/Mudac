---
type: Implementation Planning Authority
title: 008-A — Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails
description: Establishes the post-Concept-Design authority hierarchy, planning-only boundary, change-control route, decision taxonomy, progressive-disclosure rules, and execution guardrails governing Phase 008.
status: stable
tags: [phase-008, implementation-planning, authority, change-control, guardrails, canonical, progressive-disclosure]
sources:
  - resource: ../007-design-refinement/007-I-formal-jackson-concept-design-methodology-exit-accepted-residual-uncertainty-implementation-resume-boundary-decision.md
  - resource: ../canonical/governance/design-implementation-boundary.md
  - resource: ../canonical/governance/documentation-authority.md
  - resource: ../canonical/governance/change-governance.md
  - resource: ../canonical/governance/agent-context.md
  - resource: ../canonical/governance/methodology-terminology.md
  - resource: ../canonical/architecture/index.md
  - resource: ../canonical/implementation/index.md
  - resource: ../canonical/implementation/implementation-foundation.md
  - resource: ../006-implementation-planning/README.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T15:04:00Z }
---

# Purpose

Establish the authority and working rules for MUDAC's return to implementation planning after the formal Jackson Concept Design exit in 007-I.

008-A is deliberately **not** an implementation slice and does not select domain schema, authentication behavior, API shapes, browser state models, feature code, or application infrastructure. Its job is to make every later Phase 008 planning decision answerable against a known authority hierarchy without reconstructing current meaning from historical phase records or allowing implementation convenience to become accidental product design.

The governing question is:

> When a later implementation-planning task must make a concrete choice, which current owner constrains that choice, what kind of decision is being made, and what must happen if the proposed implementation does not fit the accepted design?

# Result

**PASS — implementation-planning authority is re-established for Phase 008 without authorizing domain implementation.**

The current posture is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
canonical semantic baseline: CURRENT AUTHORITY
accepted architecture: CURRENT DOWNSTREAM CONSTRAINT SET
implementation planning: ACTIVE
008-A: COMPLETE
008-B: NEXT
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

No new product Concept, policy, synchronization, architecture family, implementation technology, or stable-rule namespace is introduced by 008-A.

# Planning authority hierarchy

MUDAC does not use one undifferentiated document-precedence list for every question. Authority follows **subject ownership plus downstream constraint direction**.

The practical hierarchy is:

```text
explicit human product/design intent
        ↓  through CHG-* when meaning changes
canonical product / synchronization / policy / mechanism /
invariant / experience / governance owners
        ↓
canonical architecture owners
        ↓
canonical implementation owners
        ↓
Phase 008 implementation-planning decisions and records
        ↓
future code / schema / tests / generated contracts / IaC / runbooks
```

Separately, the current [Design / Implementation Boundary](../canonical/governance/design-implementation-boundary.md) owns **execution posture**: whether planning is active, whether a first executable domain slice has been authorized, and whether implementation has actually started.

Historical phase records, READMEs, indexes, registries, and `AGENTS.md` participate differently and are defined below.

## A. Current product and semantic meaning

For product behavior, user-visible authority, lifecycle, state/action meaning, synchronization, historical truth, correction, disclosure, policy, derived mechanisms, and conceptual experience semantics, current owners under `docs/canonical/` govern.

Relevant categories include:

- `canonical/concepts/`;
- `canonical/synchronizations/`;
- `canonical/mechanisms/`;
- `canonical/policies/`;
- `canonical/invariants/`;
- `canonical/experience/`;
- `canonical/governance/`.

Implementation planning must satisfy these owners. It must not reinterpret them to fit a preferred table shape, framework convention, endpoint style, UI state machine, infrastructure service, or test fixture.

`DOC-001`, `DOC-002`, `DOC-003`, `CHG-001`, `CHG-003`, `CHG-005`, and `IMPL-001` already provide the durable governance for this rule. 008-A does not duplicate or replace them.

## B. Current architecture meaning

For accepted structural realization choices—module boundaries, persistence architecture, identity/session architecture, command/query/concurrency architecture, browser synchronization/recovery, external representation, front-end interaction, and AWS runtime—the current owners under `canonical/architecture/` govern.

Architecture is downstream of product semantics. A Phase 008 implementation choice may specialize architecture where the owner intentionally leaves a choice open, but it cannot contradict architecture without an explicit architecture/design change.

A technology inconvenience does not make an architecture contract optional.

## C. Current implementation meaning

For accepted toolchain, source topology, verification strategy, runtime/bootstrap posture, and other durable implementation-level constraints, current owners under `canonical/implementation/` govern.

These owners may be refined by later Phase 008 subgroups when a concrete implementation-planning decision is accepted. When such a decision becomes durable current implementation meaning, the applicable canonical implementation owner is updated rather than leaving the decision solely in a numbered phase record.

A Phase 008 record supplies rationale and planning provenance; it does not become a permanent competing rule store.

## D. Execution authority

The [Design / Implementation Boundary](../canonical/governance/design-implementation-boundary.md) is the current owner for execution posture.

During 008-A through 008-K:

```text
planning decisions: ALLOWED
non-domain baseline qualification/maintenance: ALLOWED within boundary
new domain implementation: NOT AUTHORIZED
```

Only **008-L — Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** may make the Phase 008 decision to authorize a first executable domain slice.

Even an `AUTHORIZED` result in 008-L does not itself implement that slice. New domain implementation begins in Phase 009.

## E. Historical phase records

Numbered Phase 001–007 records and historical Phase 006 implementation-planning records remain append-stable provenance under `DOC-004`.

They are used when rationale, chronology, rejected alternatives, prior assumptions, or a supersession comparison is needed.

They do **not** override current canonical owners merely because they contain more detailed prose or an earlier statement that a task was “next.”

In particular, 006-E through 006-M remain planning lineage and cannot be invoked as current executable authority.

## F. Routing artifacts

`README.md`, `index.md`, stable-ID registries, traceability tables, and `AGENTS.md` route readers to authority under `DOC-005`.

They may summarize current posture, but a summary conflict is resolved by correcting the routing artifact against the owning canonical document—not by treating the summary as a second rule source.

## G. Code, tests, schemas, generated artifacts, IaC and runbooks

Future executable artifacts are realizations and evidence, not upstream semantic owners.

They may reveal a defect or contradiction in current design, but they cannot silently resolve it. If code or a proposed implementation cannot satisfy current authority, use the change-control path below.

# Canonical baseline for Phase 008 planning

Every Phase 008 subgroup starts with the smallest current owner set required by its scope rather than recursively loading the whole repository.

The baseline retrieval sequence is:

```text
AGENTS.md
   ↓
docs/index.md
   ↓
Design / Implementation Boundary
   ↓
Phase 008 README/index + current subgroup record
   ↓
task-relevant canonical owner(s)
   ↓
material historical source only when rationale/supersession requires it
```

This applies `CTX-001` through `CTX-005` to implementation planning.

The phrase **canonical baseline** does not mean every canonical document must be loaded for every subgroup. It means that current decisions must be traceable to the current owners that materially constrain them.

# Phase 008 planning decision taxonomy

To prevent ambiguous “ready” or “done” language, Phase 008 distinguishes the following states.

## 1. Existing canonical constraint

A rule or accepted choice already owned by canonical product, governance, architecture, or implementation knowledge.

A later subgroup consumes it; it does not re-decide it unless a real change is required.

## 2. Implementation-planning decision

A concrete downstream choice needed to make future implementation deterministic enough to execute—for example a persistence representation, idempotency-key scope, Draft-storage strategy, or test evidence boundary where upstream architecture intentionally leaves implementation latitude.

A planning decision may become durable current implementation knowledge, but it does **not** authorize code execution.

## 3. Provisional hypothesis / qualification finding

A finding requiring later confirmation, measurement, spike, provider evidence, or repository inspection.

A provisional hypothesis must be labeled as such. It must not be consumed by later planning as if it were an accepted contract.

## 4. First-slice authorization

A governance decision that a specifically identified implementation slice is dependency-safe, sufficiently specified, evidence-bounded, and allowed to begin.

Only 008-L may grant this authority for the Phase 009 entry slice.

## 5. Code start

The first domain-semantic executable change performed under an authorized Phase 009 slice.

Planning documents, schema sketches, pseudocode, or implementation contracts do not count as code start. Conversely, adding a real domain table, command handler, Access rule, browser domain Draft behavior, or feature implementation does count even if described as “scaffolding.”

## 6. Merge readiness

Evidence that an implemented change satisfies the applicable repository checks, review requirements, tests, migrations, documentation, and slice exit criteria.

Merge readiness is downstream of implementation and is not equivalent to deployment authority.

## 7. Deployment readiness / authority

Evidence and authorization to deploy a particular reviewed release to a particular environment.

This remains separately governed by environment, repository, and AWS controls. Merge success alone does not establish it.

## 8. Production readiness / certification

Evidence that the implemented system satisfies the required security, privacy, accessibility, performance, recovery, operations, retention, and event-readiness expectations for the intended production use.

Phase 008 cannot claim this state because the implementation and operational evidence do not yet exist.

# Change-control route during implementation planning

Implementation planning is expected to discover awkward constraints. Awkwardness is not automatically a design defect.

Use the following route.

## Case 1 — implementation mechanism conflicts with current canonical meaning

Default action: **change the implementation mechanism**.

This follows `CHG-005` and `IMPL-001`. Do not weaken the upstream rule in an implementation-plan document.

## Case 2 — two current canonical owners appear contradictory

Stop the affected downstream decision and use `CHG-003`.

Identify:

- the conflicting owners/rules;
- the exact scenario in which both cannot hold;
- intended ownership boundaries;
- known dependents;
- whether the conflict is editorial, a compatible refinement need, or a material semantic change.

Resolve the canonical conflict explicitly before the implementation plan relies on one interpretation.

Unaffected Phase 008 work may continue when genuinely independent; the contradiction does not automatically invalidate the whole phase.

## Case 3 — implementation exposes a missing product-semantic decision

Do not decide it implicitly through schema/API/UI defaults.

Classify whether the missing meaning is:

- an omitted detail already implied by current canonical authority and safely refinable;
- a material semantic change;
- a missing independent Concept/policy/synchronization/experience contract;
- or future scope outside the current baseline.

Use `CHG-*` and deliberate design work when required.

## Case 4 — the human explicitly requests a semantic change

The request is sufficient intent to enter canonical change governance.

Update the canonical owner, impact review, lineage, stable-rule compatibility, and affected downstream plan. Do not merely alter the Phase 008 record or future implementation.

## Case 5 — a future-scope item becomes tempting because implementation would be easier with it

Keep it outside the current baseline unless the human intentionally brings it into scope.

Stage/Round, student-facing workflows, formal scheduling, notifications, calibration/normalization, rich public-results applications, and advanced Award governance remain explicit future-scope examples from 007-H/007-I.

# Planning guardrails

## Guardrail A — no execution-by-accumulation

A series of individually “small” preparatory changes must not collectively implement domain behavior before 008-L.

Examples prohibited before authorization include:

- adding domain tables “for later”;
- implementing Access/session checks as scaffolding;
- adding real command handlers behind disabled routes;
- introducing IndexedDB Scorecard Draft behavior under a foundation label;
- provisioning application AWS resources because they are “only infrastructure.”

If the artifact begins to encode MUDAC domain behavior, it is implementation regardless of label.

## Guardrail B — no architecture back-drive

A library, database feature, AWS service, framework default, deployment constraint, or code-generation tool cannot redefine Concept boundaries, authority, temporal truth, evaluation semantics, disclosure, official outcomes, or Publication meaning.

## Guardrail C — no screen/API/schema ownership substitution

A route, React component, DTO, table, endpoint, queue message, object-storage key, or migration is never sufficient evidence of a new Concept or authoritative state by itself.

Implementation structures trace to accepted semantic owners rather than creating parallel ownership.

## Guardrail D — derived state remains derived

Coverage, Aggregate, Rank, readiness, reconciliation views, exception presentations, and other projections must not gain write authority merely because implementation stores or caches them.

## Guardrail E — authority-establishing and convergent work remain distinguishable

Planning must preserve the difference between actions that establish or replace authority and asynchronous/derived work that converges from committed source state.

Retry, idempotency, outbox, cache invalidation, and worker design must not blur that distinction.

## Guardrail F — uncertainty is represented, not guessed away

Unknown commit result, stale projection, disconnected Draft state, incomplete Coverage, Affected official outcome, or uncertain externalization state must remain truthfully representable.

Implementation convenience cannot silently convert uncertainty into success, failure, freshness, completion, or official status.

## Guardrail G — technical power remains separate from semantic authority

Repository administration, AWS/operator access, support tooling, break-glass capability, possession of a URL/join code/device, or database privilege cannot substitute for current Identity/Participation/Access and policy-specific semantic authority.

## Guardrail H — historical truth is not mutable convenience state

Planning for corrections, invalidation, supersession, replacement, amendment, official-outcome succession, Export regeneration, and Publication supersession must retain reconstructible history.

No implementation plan may rely on destructive overwrite as the only way to express correction where current design requires predecessor history.

# Phase 008 document ownership and anti-bloat rules

Phase 008 records exist for **planning rationale, dependency decisions, accepted implementation choices, unresolved implementation risks, and handoff evidence**.

They do not become a second canonical knowledge tree.

Each subgroup should therefore:

- cite task-relevant canonical owners instead of reproducing their full rule bodies;
- state the local implementation consequence of those owners;
- record only decisions actually made in that subgroup;
- label provisional findings distinctly from accepted decisions;
- update a canonical architecture/implementation owner when a durable current downstream contract changes;
- preserve historical 006/earlier rationale by reference rather than copying it forward wholesale;
- avoid creating a new summary/registry merely because the subgroup has many inputs;
- use stable rule IDs where they already exist rather than inventing Phase 008-specific aliases;
- stop context expansion once the material authority set is sufficient.

A useful Phase 008 record structure is:

```text
Purpose / scope
Authority inputs
Current-state findings
Decisions
Non-decisions / explicitly deferred items
Historical-plan disposition where relevant
Verification/evidence consequences
Risks / open downstream questions
Exit criteria
Handoff
```

Not every subgroup needs every heading if a section would add no information.

# Treatment of implementation decision records

`IMPL-015` remains the durable rule for material implementation decisions.

During Phase 008, a decision belongs in a dedicated implementation decision record only when it is cross-cutting enough to benefit future retrieval, alternatives/consequences matter independently of the subgroup narrative, and the decision has durable implementation ownership.

Do not create an ADR/decision record for every library option, table, endpoint, or minor reversible detail. The purpose is durable decision authority, not documentation volume.

A decision record remains downstream of canonical architecture and cannot serve as a semantic redesign mechanism.

# Relationship to verification

Tests and verification plans are downstream evidence.

A test may reveal a contradiction or underspecified behavior, but expected values must be derived from current semantic authority rather than establishing new semantics because a fixture happened to encode them.

008-K will consolidate the cross-cutting evidence strategy against the refreshed implementation plan. Earlier subgroups should still identify local verification consequences needed to judge whether their decisions are implementable and testable.

# Relationship to the protected 006-D baseline

The 006-D workspace remains a protected non-domain baseline while Phase 008 planning proceeds.

008-A does not certify that baseline as current or drift-free. That is the purpose of 008-B.

Therefore no later planning decision should assume the retained toolchain/source/runtime substrate is trustworthy merely because it exists. 008-B must verify whether it still satisfies current architecture/implementation constraints and whether any design-hiatus drift needs non-domain repair or explicit replacement planning.

# Historical 006-E–M treatment

The prior 006-E through 006-M plan is neither discarded nor resumed.

Its current status is:

```text
historical rationale: PRESERVED
useful dependency hypotheses: AVAILABLE FOR REVIEW
current planning authority: NO
current execution authority: NO
automatic Phase 009 mapping: NO
```

008-C will perform the explicit preserve/split/merge/reorder/rename/supersede mapping after 008-B qualifies the baseline.

No later subgroup should cite an old 006 task name as sufficient justification for a new slice boundary.

# 008-A exit criteria

008-A passes because the following are now explicit:

1. current product/governance owners constrain architecture and implementation planning;
2. current architecture owners constrain implementation mechanism;
3. current implementation owners constrain toolchain/source/runtime/verification realization;
4. the Design / Implementation Boundary uniquely owns current execution posture;
5. historical phase records provide provenance rather than current execution authority;
6. routing artifacts route rather than own rules;
7. code/tests/generated artifacts/IaC are downstream realization/evidence;
8. planning decisions are distinct from first-slice authorization, code start, merge readiness, deployment readiness, and production readiness;
9. semantic contradictions and implementation/design mismatches route through `CHG-*` rather than silent downstream normalization;
10. Phase 008 records use progressive disclosure and reference-first anti-bloat practices;
11. no new domain implementation is authorized before 008-L;
12. 008-L may authorize a Phase 009 entry slice but still does not execute it.

# Decision

**008-A — PASS.**

Implementation planning has a coherent current authority model and can proceed without treating design completion, historical implementation plans, executable substrate, or green CI as execution permission.

The current boundary becomes:

```text
Phase 008 planning authority: ESTABLISHED
008-A: COMPLETE
008-B: NEXT
protected 006-D baseline: NOT YET QUALIFIED BY PHASE 008
first executable domain slice: NOT AUTHORIZED
new domain implementation: NOT STARTED
```

# Handoff

Proceed to **008-B — Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation**.

008-B should inspect the retained executable substrate against current `MOD-*`, `IMPL-*`, runtime/toolchain, CI, environment, and Phase 007-derived constraints. It may perform only boundary-permitted non-domain maintenance; it must not begin domain implementation.