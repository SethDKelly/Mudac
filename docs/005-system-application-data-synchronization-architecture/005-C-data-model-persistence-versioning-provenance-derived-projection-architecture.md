---
type: Design Phase Record
title: 005-C — Data Model, Persistence, Versioning, Provenance & Derived-Projection Architecture
description: Defines MUDAC's authoritative relational persistence model, module-owned storage boundaries, stable identity references, immutable Version/provenance representation, transactional change propagation, and rebuildable derived projections.
status: stable
tags: [phase-005, architecture, data, persistence, versioning, provenance, projections]
sources:
  - resource: 005-A-architectural-drivers-quality-attributes-trust-boundaries-decision-principles.md
  - resource: 005-B-application-boundaries-modules-domain-services-dependency-architecture.md
  - resource: ../canonical/architecture/architectural-foundation.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/concepts/versioning.md
  - resource: ../canonical/concepts/provenance.md
  - resource: ../canonical/concepts/scorecard.md
  - resource: ../canonical/mechanisms/official-outcome-revision.md
  - resource: ../canonical/policies/correction-authority.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T04:30:00Z }
---

# Purpose

005-C translates the authority and module boundaries established in 005-A/005-B into a durable data architecture.

The governing question is:

> How should MUDAC persist current authoritative state, immutable committed history, provenance, cross-module references, and derived read models so that event-day concurrency, correction, auditability, and future service extraction remain safe without turning storage convenience into semantic authority?

This subgroup selects a persistence **model** and database-family assumptions. It does not select the AWS hosting product, ORM, migration library, connection pool, backup product, or concrete runtime topology.

Its accepted output is the canonical [Data, Persistence, Versioning & Projection Architecture](../canonical/architecture/data-persistence.md).

# 1. Upstream constraints

The data architecture must preserve at least:

- [ARCH-002](../canonical/architecture/architectural-foundation.md#arch-002) — consequential state changes are validated at the authoritative boundary;
- [ARCH-004](../canonical/architecture/architectural-foundation.md#arch-004) — derived projections are not write authority;
- [ARCH-005](../canonical/architecture/architectural-foundation.md#arch-005) — actor/author/authorizer/capture attribution survives boundaries;
- [ARCH-006](../canonical/architecture/architectural-foundation.md#arch-006) — retry/recovery preserve logical identity/evidence;
- [ARCH-008](../canonical/architecture/architectural-foundation.md#arch-008) — freshness and uncertainty remain representable;
- [MOD-002](../canonical/architecture/application-boundaries.md#mod-002) — every authoritative fact/command has one module owner;
- [MOD-003](../canonical/architecture/application-boundaries.md#mod-003) — module boundaries cannot be bypassed through another module's storage internals;
- [MOD-006](../canonical/architecture/application-boundaries.md#mod-006) — cross-module projections remain non-authoritative;
- [MOD-007](../canonical/architecture/application-boundaries.md#mod-007) — shared Versioning/Provenance primitives do not centralize semantic ownership;
- [Versioning](../canonical/concepts/versioning.md) — committed Versions are immutable and prior Versions remain addressable;
- [Provenance](../canonical/concepts/provenance.md) — meaningful origin/authority history remains reconstructible;
- [SC-001](../canonical/concepts/scorecard.md#sc-001), [SC-002](../canonical/concepts/scorecard.md#sc-002), and [SC-003](../canonical/concepts/scorecard.md#sc-003);
- [OUT-001](../canonical/mechanisms/official-outcome-revision.md#out-001) and [OUT-002](../canonical/mechanisms/official-outcome-revision.md#out-002);
- [Correction & Authority](../canonical/policies/correction-authority.md).

# 2. Persistence alternatives considered

## 2.1 One relational database, module-owned logical schemas — selected

A single PostgreSQL-compatible relational authority store is the initial persistence model. Each authoritative module owns a logical schema/namespace and its migrations. Cross-module communication remains through application/module contracts even though the storage is physically co-located.

Reasons:

- MUDAC has strongly relational identity/evidence structures;
- high-consequence workflows benefit from ACID transactions and database constraints;
- uniqueness/idempotency requirements such as one Scorecard per Judge × Encounter map cleanly to relational constraints;
- current state plus immutable Versions is straightforward to query and audit;
- one database avoids distributed consistency overhead before a real service-extraction driver exists;
- PostgreSQL gives a portable, mature relational contract without deciding whether AWS later hosts it through RDS PostgreSQL, Aurora PostgreSQL, or another compatible deployment.

## 2.2 Database-per-module — rejected initially

Separate databases would physically reinforce ownership, but would prematurely introduce distributed transactions, cross-database consistency, operational replication, recovery coordination, and event-delivery failure modes. 005-B found no current driver sufficient to justify those costs.

Later module extraction may separate storage together with deployment if a concrete driver appears.

## 2.3 Event sourcing as primary authority — rejected

MUDAC requires immutable Versions and meaningful provenance, but that does not require rebuilding all current state by replaying an append-only event stream.

Primary event sourcing would add:

- event-schema evolution complexity;
- replay/versioning operational burden;
- harder ad-hoc authoritative queries;
- greater coupling between current-state correctness and historical event completeness;
- accidental pressure to log low-value mutations merely because the storage model expects events.

MUDAC instead stores current authoritative state directly, preserves immutable committed Versions where required, and appends meaningful provenance/change records. Published facts/outbox messages support projections/integration but are not the primary authority.

## 2.4 Document database as primary authority — rejected

Flexible documents are useful for genuinely extensible descriptive metadata, but the core domain needs explicit relationships, uniqueness, lifecycle constraints, version references, and transactional integrity. Hiding those semantics in large mutable documents would make concurrency and auditability less explicit.

# 3. Logical database topology

The initial authority store is one logical PostgreSQL-compatible database with module-owned namespaces corresponding to the 005-B owners:

```text
authoritative database
├── competition
├── access
├── judging
├── evaluation
├── outcomes
├── representation
├── projection          # non-authoritative read models
└── platform/integration # narrowly scoped technical records
```

Exact SQL schema names are implementation details, but ownership is not.

A module owns:

- its authoritative tables;
- its indexes/constraints;
- its migration history;
- its version/provenance records for state it owns;
- its persistence ports/repositories.

Another module must not directly mutate those structures.

# 4. Stable identity architecture

## 4.1 Application identity is independent of storage location

Every durable logical resource uses an opaque stable application identifier that survives:

- table/schema migration;
- correction/version creation;
- projection rebuild;
- artifact generation;
- future service/database extraction.

Business labels such as Team Alias, Division label, email address, Panel display name, or Award title are not primary identity.

The implementation should use a globally unique identifier representation suitable for generation outside a database sequence. The exact UUID variant/library remains implementation-level unless later concurrency/sorting requirements justify standardizing it.

## 4.2 Cross-module references carry IDs, not foreign domain objects

A downstream module stores the stable ID of an upstream resource plus any **semantically required snapshot facts** it owns.

For example, Judging Operations may preserve the Alias/Division actually presented during an Encounter. That is not a denormalized cache: it is an authoritative historical observation required by [Current and Historical Truth](../canonical/invariants/current-vs-historical-truth.md#inv-005).

By contrast, copying a Team's current descriptive state merely to avoid a module query creates stale duplicated authority and should instead be handled through a projection.

## 4.3 Cross-module database constraints are not ownership contracts

Within a module schema, relational foreign keys/unique/check constraints should strongly enforce local integrity.

Cross-module physical foreign keys are **not the default architectural contract**. They may be introduced only when they reinforce an acyclic upstream identity relationship without cascades, direct cross-module writes, or preventing foreseeable module extraction. Domain authorization/meaning must never depend solely on a cross-schema foreign key.

# 5. Current state, Drafts and immutable Versions

MUDAC does not impose one persistence pattern on every row.

## 5.1 Mutable working/current records

State that is legitimately mutable may use a current-state row with an explicit concurrency/version token.

Examples include:

- Competition current lifecycle/configuration;
- current Participation state;
- current Panel membership;
- Scorecard working Draft;
- current Export distribution state.

Mutation is still performed through the owning module and governed command semantics.

## 5.2 Committed Versions are append-only

Where the product Concept requires a committed Version, persistence uses an immutable Version record.

Typical structure:

```text
logical lineage/root
    id
    current_authoritative_version_id?
    working-state metadata where applicable

immutable version
    version_id
    lineage_id
    ordinal / predecessor reference
    committed/finalized timestamp
    exact semantic basis
    immutable content/reference set
    provenance link(s)
```

Committed Version rows are never edited in place to represent later truth. A correction/amendment creates successor state according to the owning Concept/policy.

This applies directly to Rubric Versions and finalized Scorecard Versions. It also informs other immutable/reconstructible revision records such as Official Outcome Revision.

## 5.3 Draft is not a Version

A mutable Scorecard/Rubric working Draft may be persisted durably for continuity, but that persistence does not make it an authoritative Version. Draft state and committed Version history remain distinguishable in both schema and queries.

# 6. Scorecard persistence shape

The Evaluation module should model Scorecard persistence around **logical identity plus authoritative Versions** rather than treating each submission as a new Scorecard row.

Illustrative logical shape:

```text
Scorecard
    scorecard_id
    judge_participation_id
    encounter_id
    current_authoritative_version_id?
    draft_state / draft_revision
    concurrency_token

ScorecardVersion (append-only)
    scorecard_version_id
    scorecard_id
    predecessor_version_id?
    rubric_version_id
    finalized_at
    immutable evaluation content/basis
    semantic_author
    provenance references
```

A database-level uniqueness constraint should enforce the owning invariant equivalent to:

```text
Judge Participation × Encounter → one logical Scorecard
```

Retry/idempotency semantics are refined in 005-E/F, but storage must make duplicate logical evaluation weight difficult by construction.

# 7. Provenance architecture

Provenance is stored as append-only meaningful transition history associated with the owning module/resource.

A shared technical envelope may standardize fields such as:

```text
provenance_id
module / subject type
subject_id
subject_version_id?
action / transition kind
occurred_at
actor_identity_id?
actor_participation_id?
semantic_author_id?
authorizer_id?
capture_actor_id?
source/capture channel
reason / reason code when material
correlation_id / causation_id
```

But module-specific semantics remain owned by the module. A generic provenance table/service does not decide whether a Judge amendment, Organizer capture correction, invalidation, or Competition Finalization was semantically valid.

Provenance records are append-only. Corrections append new provenance; they do not rewrite the old actor/reason to make history look cleaner.

The architecture intentionally does **not** require logging every read, keystroke, autosave, or low-value technical operation as product Provenance. Security/operational audit logs may separately capture infrastructure/security activity.

# 8. Deletion, invalidation and referential history

Referenced authoritative evidence should not disappear through destructive cascade deletion.

Where domain semantics require withdrawal, invalidation, supersession, or replacement, those states are represented explicitly while the historical resource remains addressable.

Hard deletion is reserved for cases the domain already permits, such as an unreferenced Draft/setup mistake, and must not strand historical Version/provenance references.

Database cascade-delete behavior across authoritative aggregates should therefore be used sparingly and never as a substitute for domain lifecycle semantics.

# 9. Derived calculations and outcome persistence

Coverage, Aggregate, Rank, and readiness are derived from authoritative evidence/policy.

The architecture allows persisting calculated results for performance, but persisted derived state must record enough **basis identity** to determine what produced it, for example:

```text
Competition / Division / Team identity
source Scorecard Version IDs or source-set revision
Evaluation Policy identity/version
calculation version
computed_at
basis watermark/fingerprint
```

Persisted calculated state does not become independently editable authority. If the basis changes, it is stale/affected and must be recomputed.

An [Official Outcome Revision](../canonical/mechanisms/official-outcome-revision.md#out-001) is different: Finalization deliberately freezes an immutable/reconstructible official snapshot/basis. Later correction produces a successor revision rather than rewriting the prior official revision.

# 10. Projection architecture

## 10.1 Projection storage is disposable

Cross-module read models live in a separate projection namespace/store role and can be dropped/rebuilt from authoritative state plus durable change history needed for projection replay.

A projection may contain:

- Organizer live-operation summaries;
- Judge readiness lists;
- search/autocomplete documents;
- reconciliation queues;
- Coverage/Aggregate/Rank display rows;
- public/ceremony preview datasets.

No user-authored or official fact may exist **only** in projection storage.

## 10.2 Projection freshness is explicit

Projection records/sets retain enough metadata to expose freshness, such as source watermark/version, last successfully applied change, and build/update time.

This supports [ARCH-008](../canonical/architecture/architectural-foundation.md#arch-008): the application may say a view is stale or refreshing rather than treating a cached result as contemporaneous authority.

## 10.3 Projection rebuild is a designed operation

Projection code should be deterministic from authoritative inputs. Schema/data-loss recovery for projections is therefore rebuild-oriented rather than backup-authority-oriented.

Projection rebuild does not mutate authoritative module state.

# 11. Transactional change propagation / outbox

When an authoritative transaction produces a fact needed by projections, asynchronous work, or later external integration, the fact is recorded in a **transactional outbox/change record in the same authority transaction** as the source state change.

Conceptually:

```text
BEGIN
  validate authoritative state
  write authoritative mutation/version/provenance
  append outbox fact
COMMIT
```

A dispatcher may then deliver that fact to in-process or external consumers.

This prevents the classic dual-write failure where authoritative state commits but the projection/event notification is silently lost.

Outbox consumers must be idempotent because delivery may be at-least-once. Detailed message semantics and command idempotency belong to 005-E/F.

# 12. Outbox/events do not become event-sourced authority

Published facts may be durable and replayable for rebuilding projections, but they remain **integration/projection records about authoritative changes**, not a replacement for the authoritative module state and Version records.

A projection consumer cannot reinterpret an outbox message to create a new authoritative business fact.

If later service extraction requires a stronger event contract, the event can evolve from the same module-owned public fact boundary without redefining product semantics.

# 13. Constraint and concurrency posture

The database should enforce invariant-shaped facts that can be expressed safely at the owning storage boundary, including:

- primary/stable identity uniqueness;
- one logical Scorecard per Judge Participation × Encounter;
- Version identity/lineage uniqueness;
- one current-authoritative Version pointer where relevant;
- local foreign-key integrity;
- valid nullability/check constraints for structurally impossible states;
- idempotency/outbox uniqueness where later specified.

Database constraints are defense in depth. They do not replace application-level Access, lifecycle, authorship, or cross-module precondition logic.

Concurrency-token strategy, transaction isolation, lock behavior, idempotency keys, and multi-module orchestration are finalized in 005-E.

# 14. Extensible metadata posture

Relational columns/tables remain the default for lifecycle, authority, evidence identity, scoring basis, and other semantics used by invariants/queries.

Semi-structured JSON-like storage may be used for genuinely extensible descriptive metadata where schema flexibility is part of the product model—for example some Team Attributes—but core semantic fields should not be hidden inside opaque JSON merely to avoid migrations.

# 15. Schema evolution and migrations

Each module owns the migrations for its storage namespace.

Migrations must preserve:

- stable IDs;
- immutable Version addressability;
- provenance attribution;
- current-authoritative pointers;
- cross-module public identity contracts;
- historical observed facts;
- projection rebuild compatibility or an explicit rebuild plan.

Schema migration is an implementation evolution mechanism, not a domain correction mechanism. A migration must not rewrite historical business meaning merely to simplify a new model.

# 16. Canonical data architecture rules

005-C promotes the following rules to the canonical architecture owner:

- `DATA-001` — Authoritative persistence is relational and PostgreSQL-compatible.
- `DATA-002` — One logical authority database initially; storage ownership remains module-scoped.
- `DATA-003` — Durable identities are stable and independent of storage/business labels.
- `DATA-004` — Physical co-location does not permit cross-module storage bypass.
- `DATA-005` — Working/current state and committed Versions remain structurally distinct.
- `DATA-006` — Committed Versions and meaningful Provenance are append-stable.
- `DATA-007` — Referenced authoritative evidence is not erased through ordinary destructive cascade.
- `DATA-008` — Persisted derived calculations remain reconstructible from an identified basis.
- `DATA-009` — Read projections are disposable/rebuildable and non-authoritative.
- `DATA-010` — Projection freshness/authority basis remains observable.
- `DATA-011` — Authoritative change propagation uses a transactional outbox/change record where asynchronous consumers depend on the change.
- `DATA-012` — Outbox/events do not replace authoritative state or require primary event sourcing.
- `DATA-013` — Database constraints reinforce owner invariants but do not replace domain authority checks.
- `DATA-014` — Core semantic fields remain explicit; semi-structured storage is reserved for genuinely extensible data.

# 17. Decisions deliberately deferred

005-C does not yet choose:

- AWS RDS PostgreSQL vs Aurora PostgreSQL or another hosting topology;
- ORM/query builder;
- migration framework;
- connection pool/proxy;
- exact UUID variant/generator;
- exact transaction isolation per command;
- locking/optimistic-concurrency implementation;
- API/event serialization format;
- queue/broker;
- offline Draft store/sync protocol;
- backup retention/RPO/RTO;
- object storage/artifact repository.

Those belong to later 005 groups once their specific constraints are available.

# 18. 005-C exit review

005-C is ready to close because the persistence model now answers:

- what is authoritative;
- which module owns storage/migrations;
- how cross-module identity survives physical change;
- how current mutable state differs from committed immutable Versions;
- how meaningful Provenance remains append-stable;
- why event sourcing is not required;
- how derived calculations remain reconstructible;
- how projections stay rebuildable/non-authoritative;
- how reliable asynchronous propagation avoids dual-write loss;
- where database constraints reinforce but do not replace domain authority.

No upstream product semantic required redesign.

The next subgroup is **005-D — Identity, Authentication, Participation, Access & Session Architecture**.
