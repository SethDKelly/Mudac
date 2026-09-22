---
type: Accepted Architecture Decision
title: Current Persistence, History, Provenance, Projection, Migration & Recovery Architecture
description: "Accepted ADQ-003 persistence architecture for MUDAC: one logical PostgreSQL-compatible relational authority store, module-owned logical storage, explicit mutable-current versus immutable-committed history, append-stable Provenance, rebuildable non-authoritative projections, additive/forward-compatible migrations, and authority-first backup/restore and recovery."
status: stable
tags: [architecture, current, persistence, history, provenance, projections, migration, recovery, relational]
sources:
  - resource: architecture-drivers.md
  - resource: application-ownership-boundaries.md
  - resource: data-persistence.md
  - resource: ../concepts/versioning.md
  - resource: ../concepts/provenance.md
  - resource: ../invariants/current-vs-historical-truth.md
  - resource: ../invariants/truthful-authority-under-uncertainty.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../governance/downstream-realization-obligations.md
  - resource: ../governance/implementation-program-delivery.md
  - resource: ../../019-architecture-engineering-reentry/019-D-persistence-history-provenance-projection-migration-recovery-architecture.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T08:03:00-05:00 }
---

# Authority

This document is **current accepted architecture authority for ADQ-003**.

It establishes durable authority storage, current/history representation, Provenance, projection, migration and recovery posture.

It does not select the ORM/query layer, exact migration tool, exact AWS managed database service, final backup schedule, exact RTO/RPO, or jurisdiction-specific retention period.

<a id="pst-001"></a>
## PST-001 — The authoritative persistence family is PostgreSQL-compatible relational storage

MUDAC uses a PostgreSQL-compatible relational model for authoritative application state.

The architecture requires:

- durable opaque identity;
- explicit relationships and constrained state;
- transactional atomicity within the accepted application boundary;
- uniqueness and integrity constraints;
- explicit current/history linkage;
- reconstructible Version/Provenance references;
- event-day concurrent update integrity.

The exact managed runtime realization is deferred to ADQ-009.

<a id="pst-002"></a>
## PST-002 — One logical authority database is the initial storage topology

The accepted five-module modular monolith begins with one logical authority database.

Physical co-location does not merge semantic ownership.

Each accepted module owns its logical persistence boundary, schema evolution and persistence contracts:

- Competition Context;
- Identity & Access;
- Evaluation;
- Outcomes & Officiality;
- External Representation.

A future service extraction may separate physical storage only through an explicit later architecture change justified by accepted drivers.

<a id="pst-003"></a>
## PST-003 — Storage ownership follows BND application ownership

A module may not establish authority by directly mutating another module's persistence representation.

Cross-module references use stable application identities and owner contracts.

Within one physical database, storage convenience does not authorize:

- another module's repository access;
- another module's ORM/data object as an authority shortcut;
- destructive cross-module cascades;
- storage coupling that changes semantic ownership.

Local relational constraints may reinforce owner-local invariants.

<a id="pst-004"></a>
## PST-004 — Durable resource identity is independent of mutable business labels and physical storage

Authoritative resources use stable opaque application identifiers.

Mutable values such as alias, title, email, display label, ordinal position or source-row key are not durable identity.

Stable identity survives:

- Version creation;
- schema migration;
- projection rebuild;
- correction;
- artifact generation;
- future module/service extraction.

<a id="pst-005"></a>
## PST-005 — Working/current state and committed authoritative history are structurally distinct

Mutable working state may change under the natural owner's rules.

A persisted Draft remains a Draft.

Where the domain establishes committed Version authority, persistence records a distinct immutable committed snapshot and explicit current-eligible lineage state.

Typical shape:

~~~text
logical subject / lineage
        ↓
current eligible Version reference
        ↓
immutable Version records
        +
append-stable Provenance
~~~

The exact table design is implementation detail; the semantic distinction is not.

<a id="pst-006"></a>
## PST-006 — Committed Versions are immutable and may legitimately have no current eligible successor

Committed Version state is append-stable.

Supersession creates a successor and preserves its predecessor.

Invalidation preserves the Version while removing eligibility.

No persistence mechanism may silently revive an older Version merely because the current Version becomes invalid.

A lineage may therefore have:

~~~text
retained history
+ no current eligible authoritative Version
~~~

when that is the current semantic truth.

<a id="pst-007"></a>
## PST-007 — Meaningful Provenance is append-stable and distinct from technical telemetry

Persistence records enough Provenance to explain authoritative state where current semantics require it, including as applicable:

- Actor;
- RepresentedAuthority;
- Scope;
- source/capture channel;
- material reason;
- prior/resulting state references;
- correction/invalidation/replacement relationships;
- occurrence versus later capture/verification timing.

Low-level logs and observability traces do not substitute for product Provenance.

Incorrect Provenance is corrected through attributable successor evidence, not silent overwrite.

<a id="pst-008"></a>
## PST-008 — Ordinary destructive operations cannot erase referenced authoritative history

Once state participates materially in:

- committed Version history;
- Provenance;
- evaluation evidence;
- OutcomeBasis;
- correction lineage;
- Export/Publication lineage;
- historical occurrence/context truth,

ordinary deletion or database cascade must not erase that history.

Domain-permitted deletion may remain available for genuinely unreferenced setup or Draft mistakes where current semantics allow it.

Exact legally required retention/deletion behavior remains evidence-bounded under ENG-002.

<a id="pst-009"></a>
## PST-009 — Derived calculations and read projections are non-authoritative and reconstructible

Coverage, Aggregate, Rank, readiness summaries, dashboards, search indexes and similar read models may be materialized for performance.

They must retain enough basis/currentness metadata to explain:

- what source authority produced them;
- whether they are current, stale, rebuilding, failed or uncertain;
- which policy/basis was used where material.

No authoritative user-authored or official fact may exist only in projection storage.

High-consequence commands revalidate against authoritative owner state.

<a id="pst-010"></a>
## PST-010 — Projection loss is recovered by rebuild, not by promoting projection backups to authority

Projection/read-model storage is disposable relative to the authority store.

Recovery order is:

~~~text
restore / establish authoritative source state
        ↓
verify source/history consistency
        ↓
rebuild projections
        ↓
verify projection basis/freshness
        ↓
resume dependent read paths
~~~

A projection may be unavailable while authoritative state remains valid.

The system must expose that limitation rather than infer authority from stale projection data.

<a id="pst-011"></a>
## PST-011 — Asynchronous propagation, when used, is durably coupled to the authoritative commit

If a later ADQ selects asynchronous propagation for projections or integrations, the source change and its durable propagation intent must not be separable by an ordinary process crash.

The architecture therefore requires a transactional durable-change pattern equivalent in semantics to an outbox.

Exact table/event/queue mechanism is deferred to ADQ-005 and ADQ-009.

Published change facts remain downstream descriptions of committed authority; they do not become the primary source of domain truth.

<a id="pst-012"></a>
## PST-012 — System-wide event sourcing is not the baseline persistence architecture

MUDAC does not require every current state to be reconstructed from an append-only event log.

Current-state relational persistence plus explicit immutable committed history/Provenance satisfies the present semantic requirements with lower operational and conceptual burden.

Targeted append-only change/provenance records remain compatible with this decision.

Reopening full event sourcing requires evidence that current/history, audit, temporal query or integration needs cannot be met proportionately by the accepted model.

<a id="pst-013"></a>
## PST-013 — Core semantic fields remain explicit; semi-structured storage is bounded

Fields that participate in current authority, lifecycle, Access, scoring basis, evaluation identity, Versioning, outcome basis or other canonical invariants remain explicitly modeled.

Semi-structured relational storage may hold genuinely extensible descriptive metadata where:

- the extension does not hide a core invariant;
- validation remains explicit;
- migrations remain possible;
- query/currentness behavior remains understandable.

Semi-structured storage is not a substitute for semantic schema evolution.

<a id="pst-014"></a>
## PST-014 — Schema migration is owner-scoped, forward-compatible and history-preserving

Database evolution follows an additive-first posture.

A consequential migration plan must identify:

- owning module;
- forward schema change;
- compatibility window if old/new application revisions can overlap;
- data transformation/backfill where required;
- validation/reconciliation step;
- history/Provenance impact;
- rollback or roll-forward-only rationale;
- partial-migration recovery.

Destructive contraction occurs only after compatibility and retained-history obligations are satisfied.

Cross-module migration sequencing must preserve BND ownership.

Exact migration tooling is deferred to Phase 020.

<a id="pst-015"></a>
## PST-015 — Data recovery restores authoritative consistency before service availability is claimed

Backup/restore and disaster recovery must recover a mutually consistent authoritative database state, including committed history and Provenance required to explain that state.

Recovery must distinguish:

- database restoration complete;
- application consistency verified;
- projections rebuilt/current;
- external integrations reconciled;
- service fully ready.

A database restore alone does not prove semantic recovery.

Exact backup interval, retention, Multi-AZ topology, RTO and RPO remain ADQ-009 evidence obligations.

<a id="pst-016"></a>
## PST-016 — Recovery never fabricates authority after uncertain or partial failure

After a partial migration, restore, projection failure or interrupted propagation:

- retained committed authority is not silently rewritten;
- missing propagation is replayed/rebuilt where safe;
- uncertain command results remain unknown until authoritative state is checked;
- derived/projected state is marked stale or unavailable rather than guessed;
- correction follows natural-owner semantics.

Persistence recovery cannot create a new Scorecard, declaration, Award, Export or Publication merely to make data look internally complete.

# Selected architecture

ADQ-003 selects:

> **One logical PostgreSQL-compatible relational authority store with module-owned logical storage, explicit mutable-current versus immutable-committed history, append-stable Provenance, rebuildable non-authoritative projections, durable commit-coupled change propagation where asynchronous work is later selected, additive/forward-compatible migrations, and authority-first backup/restore and recovery.**

# Provider/runtime boundary

This decision selects the relational/PostgreSQL-compatible persistence family.

It does **not** select Amazon RDS, Aurora PostgreSQL, self-managed PostgreSQL, Multi-AZ topology, replica topology or a specific backup service.

Those runtime/provider choices belong to ADQ-009 and must be evaluated using current AWS constraints, recovery targets, cost and operability evidence.

# Revisit triggers

Reopen ADQ-003 if credible evidence shows:

- required scale or access pattern cannot be met proportionately by the relational authority model;
- independent module storage becomes necessary after justified service extraction;
- retention/legal obligations conflict with immutable-history assumptions;
- temporal/audit requirements make full event/log reconstruction materially superior;
- selected concurrency/transaction architecture cannot preserve current/history semantics;
- selected recovery targets cannot be met by the accepted storage model;
- whole-architecture validation identifies unacceptable coupling, migration or recovery risk.

Whole-architecture acceptance remains false until 019-L.
