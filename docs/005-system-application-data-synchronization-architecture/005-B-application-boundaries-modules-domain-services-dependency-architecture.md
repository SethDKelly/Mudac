---
type: Design Phase Record
title: 005-B — Application Boundaries, Modules, Domain Services & Dependency Architecture
description: Defines MUDAC's application responsibility boundaries, module ownership, cross-module coordination, dependency direction, and initial modular-monolith deployment posture.
status: stable
tags: [phase-005, architecture, modules, dependencies, modular-monolith, application-boundaries]
sources:
  - resource: 005-A-architectural-drivers-quality-attributes-trust-boundaries-decision-principles.md
  - resource: ../canonical/architecture/architectural-foundation.md
  - resource: ../canonical/concepts/competition.md
  - resource: ../canonical/concepts/participation.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/concepts/judging-encounter.md
  - resource: ../canonical/concepts/rubric.md
  - resource: ../canonical/concepts/scorecard.md
  - resource: ../canonical/concepts/award.md
  - resource: ../canonical/concepts/export.md
  - resource: ../canonical/mechanisms/index.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T04:20:00Z }
---

# Purpose

005-B determines how MUDAC's application responsibilities are separated before persistence, API, synchronization, front-end, and AWS choices are made.

The governing question is:

> Which semantic responsibilities require distinct ownership, how may those owners depend on one another, and what deployment posture gives MUDAC strong boundaries without introducing distributed-system complexity before a concrete driver exists?

005-B does **not** select a programming language, web framework, database, ORM, API protocol, queue/event bus, identity provider, front-end framework, or AWS service.

Its accepted current output is [Application Boundaries, Modules & Dependency Architecture](../canonical/architecture/application-boundaries.md).

# 1. Upstream constraints

The architecture must preserve:

- [ARCH-001](../canonical/architecture/architectural-foundation.md#arch-001) — upstream semantics constrain architecture;
- [ARCH-002](../canonical/architecture/architectural-foundation.md#arch-002) — authoritative transitions are validated at the authoritative boundary;
- [ARCH-004](../canonical/architecture/architectural-foundation.md#arch-004) — projections are not write authority;
- [ARCH-005](../canonical/architecture/architectural-foundation.md#arch-005) — actor/author/authorizer/capture attribution survives boundaries;
- [ARCH-006](../canonical/architecture/architectural-foundation.md#arch-006) — retries/failure preserve logical identity;
- [ARCH-007](../canonical/architecture/architectural-foundation.md#arch-007) — disclosure is enforced beyond presentation;
- [INV-002](../canonical/invariants/one-logical-scorecard.md#inv-002) — one logical Scorecard per Judge × Encounter;
- [ACC-001](../canonical/concepts/access.md#acc-001) and [ACC-002](../canonical/concepts/access.md#acc-002) — contextual Access without authority transfer.

The accepted Concept catalog does not imply one application module per Concept. Module boundaries are architecture decisions based on semantic cohesion, authority ownership, transaction/failure behavior, and change coupling.

# 2. Alternatives considered

## 2.1 Undifferentiated monolith

One application codebase with little enforced internal ownership would minimize initial ceremony.

Rejected as the target architecture because it would make it too easy for:

- Scorecard code to mutate Encounter or Participation data directly;
- reporting/query code to become accidental write authority;
- infrastructure/ORM models to become the domain model;
- future changes to couple unrelated concepts;
- canonical rule ownership to be lost in a generic service layer.

## 2.2 Independently deployed services from the start

Service-per-domain-boundary deployment could provide independent scaling and runtime isolation.

Not selected initially because current drivers do not justify the distributed cost:

- MUDAC has bounded event-shaped load rather than demonstrated independent hyperscale domains;
- several high-consequence workflows require coordinated current-state checks;
- network partitions and distributed transactions would create new authority/failure states before they solve a demonstrated problem;
- operating many services would conflict with cost proportionality and modest-team operability;
- independent deployment cadence/scaling needs have not yet been established.

Service extraction remains an evolutionary option if later evidence shows materially different scale, security isolation, availability, ownership, or deployment requirements.

## 2.3 Modular monolith

Selected as the initial authoritative application posture.

One deployable application authority can keep high-consequence coordination local while internal modules enforce semantic ownership, public contracts, dependency direction, and data-access boundaries.

The decision is **modular monolith first, not monolith forever**.

# 3. Application module map

005-B defines six authoritative business modules, one non-authoritative projection/query subsystem, and one thin application-coordination layer.

## 3.1 Competition Governance

Owns current semantic authority for:

- Competition lifecycle;
- Division;
- Team;
- Alias;
- Team Attributes and competition-scoped descriptive configuration;
- structural setup facts needed by readiness/operation.

It owns commands that directly change those subjects, including Competition lifecycle transitions when their preconditions have been established.

It does **not** own Judge evaluation, Panel/Encounter operation, ranking math, authentication, or publication.

## 3.2 Identity, Participation & Access

Owns application authority for:

- Identity continuity as represented inside MUDAC;
- Competition-scoped Participation;
- Judge/Organizer role participation state;
- Competition-scoped Access evaluation inputs/policies;
- event-day check-in/availability facts that belong to Participation.

Authentication-provider mechanics remain 005-D. This module consumes authenticated principal claims but does not outsource MUDAC Participation/Access semantics to the provider.

## 3.3 Judging Operations

Owns:

- Panel;
- Panel Membership and composition state;
- Judging Encounter lifecycle;
- effective Encounter participants;
- recusal/absence/substitution/replacement operational facts;
- Encounter evaluation obligations.

It references Team/Alias/Division and Judge Participation by stable identity/contracts rather than owning or mutating them.

## 3.4 Evaluation

Owns:

- Rubric lineage and authoritative Rubric Versions;
- Criterion and Note structure;
- Scorecard logical identity;
- Draft/Finalized/amendment evaluation state;
- Judge-authored evaluation content;
- paper-origin Scorecard capture semantics once physical evidence is being translated into the same logical evaluation.

Evaluation never owns Panel staffing or Judge Participation. It receives the validated Encounter/Participation basis through application contracts and preserves those identities as evidence.

## 3.5 Outcomes & Closeout

Owns:

- Evaluation Policy versions relevant to Coverage/Aggregate/Rank;
- Coverage;
- Aggregate;
- Rank;
- Reconciliation state/process projections requiring authoritative decisions;
- Award definitions/conferrals;
- ranking/finalization readiness facts specific to outcome evidence;
- Official Outcome Revision.

It consumes authoritative evidence from Competition, Judging Operations, and Evaluation through public contracts/facts. It does not directly mutate their owned state.

Competition Finalization remains a Competition lifecycle transition. The cross-module closeout use case is coordinated above the modules so Outcome authority and Competition lifecycle authority remain distinct.

## 3.6 External Representation

Owns:

- Export identity/state;
- artifact generation intent and source binding;
- publication/republication/withdrawal-of-current-distribution operations;
- representation audience/disclosure application;
- printable/electronic external representation state.

It consumes identified source state from owning modules. It cannot make its representation authoritative over the underlying source.

Paper **output** generation belongs here; paper-origin Judge evaluation **input** converges through Evaluation. Exact physical-source/artifact mechanics are deferred to 005-G.

# 4. Projection & Query subsystem

MUDAC needs operational and analytical reads that compose information from multiple owners:

- Organizer live-operations views;
- readiness summaries;
- Judge/Panel/Encounter status views;
- reconciliation exception queues;
- Coverage/Aggregate/Rank presentation;
- search/lookup;
- public/internal representation previews.

These are implemented through a projection/query subsystem that may consume published authoritative facts from multiple modules and optimize for read shape.

This subsystem:

- owns no product-domain command authority;
- may be stale where explicitly tolerated;
- must retain freshness/version information where consequential;
- cannot update module-owned state directly;
- is never the sole precondition source for a high-consequence command.

This is an architectural separation of reads from writes, **not** a commitment to a particular CQRS framework, event store, cache, or search product.

# 5. Application coordination layer

Some use cases legitimately span multiple modules. Examples include:

- marking Competition Ready after cross-module readiness checks;
- opening an Encounter after validating Competition/Team/Participation context;
- Competition Finalization after outcome readiness/award checks;
- paper capture that resolves physical context then creates/updates the authoritative logical Scorecard;
- post-finalization correction that affects evidence, outcome revision, and external representations.

These workflows are coordinated by a thin application/use-case layer above module public interfaces.

The coordinator:

- sequences/calls authoritative module operations;
- establishes the actor/use-case context;
- may own transaction/workflow coordination mechanics later defined in 005-E;
- does **not** become the semantic owner of module state;
- does not contain a second copy of module invariants;
- does not bypass public module contracts by writing repositories/tables directly.

A coordinator disappearing should not make ownership ambiguous: each changed fact still has a single module owner.

# 6. Dependency direction

The intended dependency shape is:

```text
UI / HTTP / jobs / external adapters
              ↓
      application coordination
              ↓
       module public contracts
      ↙       ↓        ↘
 module domain/application logic
              ↓
       module-owned ports
              ↑
 infrastructure implementations
```

Cross-module dependencies use explicit public contracts, stable identities, or published facts/events.

Modules must not:

- import another module's persistence/repository implementation;
- query another module's tables/collections as an authority shortcut;
- mutate another module's entities directly;
- share ORM/data objects as the cross-module domain contract;
- create circular application dependencies merely to make orchestration convenient.

Where synchronous cross-module information is required, the application coordinator or a declared public query contract supplies it. Where eventual propagation is safe, published facts/events may update projections or downstream module state.

Exact synchronous/asynchronous transport is deferred.

# 7. Shared foundation boundary

A small shared foundation is permitted for semantic-neutral or broadly architectural primitives such as:

- stable identifier value types;
- time/clock abstraction;
- actor/request context envelope;
- version/concurrency token primitives;
- result/error envelope conventions;
- event/message envelope primitives;
- common validation/serialization helpers without business ownership.

The shared foundation must **not** become a dumping ground containing:

- Competition/Scorecard/Panel entities;
- business policies;
- authorization decisions;
- generic "domain service" implementations that secretly own multiple modules;
- common repositories exposing cross-module storage.

If a shared abstraction begins carrying business meaning, ownership should move to the appropriate module and be consumed through its contract.

# 8. Versioning and Provenance as cross-cutting capabilities

[Versioning](../canonical/concepts/versioning.md) and [Provenance](../canonical/concepts/provenance.md) apply across multiple module-owned resources.

005-B explicitly rejects a generic central "Versioning service" or "Provenance service" that becomes the semantic owner of all change history.

Instead:

- each authoritative module owns the version/history semantics of its resources;
- shared technical primitives may standardize revision IDs, actor context, timestamps, reason metadata, event envelopes, or audit persistence interfaces;
- the module that owns the changed semantic state remains responsible for deciding what constitutes a Version, correction, invalidation, or meaningful provenance event.

This preserves semantic ownership while allowing implementation reuse.

# 9. Cross-module command ownership

Every command has one primary authoritative owner.

Examples:

| Command/use case | Primary owner |
| --- | --- |
| Change Team/Alias/Division | Competition Governance |
| Enroll/check in Judge Participation | Identity, Participation & Access |
| Form Panel / open or invalidate Encounter | Judging Operations |
| Finalize/amend Scorecard | Evaluation |
| Accept Coverage exception / confer Award | Outcomes & Closeout |
| Generate/publish/replace Export | External Representation |

A cross-module use case may invoke several owner commands, but it does not merge their authority into a generic workflow object.

# 10. Dependency graph posture

The authoritative modules should remain as close to acyclic as practical.

Rather than allow mutual direct dependencies, the preferred pattern is:

```text
source modules publish/answer owned facts
            ↓
application coordinator / downstream consumer
            ↓
consumer command or projection
```

Particularly:

- Competition Governance does not depend on Outcomes & Closeout merely because Finalization requires outcome readiness; the closeout coordinator obtains outcome readiness and invokes the Competition lifecycle transition.
- Evaluation does not mutate Judging Operations to resolve participant errors; structural correction is routed to the proper owner.
- Outcomes & Closeout consumes evaluation/encounter facts but Evaluation does not depend on Rank/Award state.
- External Representation consumes identified source state but upstream modules do not depend on generated artifacts to establish their own authority.

This dependency direction keeps outcome/representation concerns downstream of evidence creation.

# 11. Deployment boundary decision

Initial architecture selects **one authoritative server-side application deployment containing the modules above**.

This decision is based on current drivers:

- bounded live-event scale;
- strong cross-module consistency needs;
- modest operational/team footprint;
- no demonstrated independently scaling domain;
- no demonstrated need for independent service deployment cadence;
- desire to minimize network/distributed-transaction failure modes around authority-sensitive workflows.

This does not require all runtime work forever to share one process. Later groups may justify separate workers, projection builders, artifact jobs, or extracted services.

A module may be considered for independent deployment only when a concrete driver exists, such as:

- materially different scaling profile;
- security/isolation requirement;
- availability/failure-containment requirement;
- operational ownership/deployment cadence;
- technology/runtime requirement that cannot reasonably coexist;
- proven hotspot whose extraction has a better complexity tradeoff.

Extraction must preserve the same public contracts and authority boundaries rather than redefine semantics.

# 12. Architecture rules promoted by 005-B

005-B promotes the following stable architecture rules:

## MOD-001 — The initial authoritative application is a modular monolith

MUDAC begins with one authoritative application deployment divided into explicit semantic modules. Independent services require a demonstrated driver rather than speculative scale.

## MOD-002 — Each authoritative fact and command has one module owner

A business fact/transition has a primary module responsible for its semantics and write invariants. Other modules consume it through public contracts and do not directly mutate it.

## MOD-003 — Cross-module interaction cannot bypass public ownership boundaries

Modules may exchange stable IDs, public query contracts, commands, and published facts/events. They may not treat another module's repository, table, ORM entity, or internal service as a public authority shortcut.

## MOD-004 — Cross-module workflows coordinate above module owners

Use-case coordinators may sequence several module operations, but the coordinator does not become a new owner of their domain semantics and may not duplicate their invariants.

## MOD-005 — Dependency direction should remain acyclic and downstream-oriented

Evidence/configuration owners do not depend backward on downstream outcome or representation concerns. Circular module dependencies are architecture defects unless an explicit reviewed exception proves unavoidable.

## MOD-006 — Projection/query composition is non-authoritative

Cross-module read models may compose and optimize reads, but they have no product-domain write authority and cannot be the sole precondition source for consequential commands.

## MOD-007 — Cross-cutting technical reuse does not centralize semantic ownership

Versioning, Provenance, identity primitives, event envelopes, concurrency tokens, and similar technical capabilities may share implementation primitives while semantic decisions remain with the module owning the affected state.

## MOD-008 — Shared foundation remains small and business-neutral

Shared code may contain broadly reusable primitives/helpers, but business entities, policies, repositories, and authorization decisions remain module-owned.

## MOD-009 — Infrastructure depends inward through module/application ports

Persistence, external providers, transport, queues, artifact stores, telemetry, and framework adapters implement or invoke application/module contracts; domain/application code does not depend on vendor/framework APIs for its semantic rules.

## MOD-010 — Deployment boundaries may evolve without changing semantic boundaries

A module may later be extracted when a concrete scale/isolation/availability/ownership driver exists. Extraction preserves module contracts, stable identities, and authority semantics rather than using deployment as a redesign mechanism.

# 13. Consequences for later Phase 005 groups

## 005-C — Data/Persistence

Must define module-owned persistence boundaries without permitting shared-table/repository shortcuts. Physical use of one database remains possible; logical ownership is already fixed here.

## 005-D — Identity/Access

Must preserve the Identity/Participation/Access module boundary while allowing authentication to remain an external/provider-facing adapter concern.

## 005-E — Commands/API/Transactions

Must define how module public contracts are exposed, how cross-module coordination becomes transactional or recoverable, and how idempotency/concurrency work without bypassing ownership.

## 005-F — Synchronization

Must treat client/local state as outside module authority and recover through the same application contracts.

## 005-G — External Representation

Must preserve one-way source-to-representation authority while paper capture input converges into Evaluation through governed coordination.

## 005-H — Front End

Front-end state may mirror/module-compose read models but cannot become the module/domain boundary or write authority.

## 005-I — Runtime/AWS

AWS/service/container boundaries must implement these modules; they do not get to redefine module ownership because a managed service suggests a different topology.

# 14. Exit check

005-B is complete when:

- module responsibilities are mutually understandable and do not create new MUDAC Concepts;
- every major authoritative write category has an owner;
- cross-module workflows have an explicit non-owning coordination layer;
- read projections are separated from write authority;
- dependency direction prohibits repository/table bypass and circular convenience coupling;
- initial modular-monolith deployment is justified by current drivers;
- later service extraction remains possible without semantic redesign;
- no persistence/API/framework/cloud choice has been prematurely locked.

These conditions pass.

# 15. Exit principle

> **MUDAC should begin as one deployable authority composed of explicit semantic modules: ownership is strong inside the process, cross-module interaction is contractual, read composition is non-authoritative, and deployment may become distributed only when evidence justifies the added failure and operational complexity.**
