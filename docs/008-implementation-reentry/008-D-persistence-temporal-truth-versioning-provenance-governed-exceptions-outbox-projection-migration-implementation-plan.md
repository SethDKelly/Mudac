---
type: Implementation Planning Record
title: 008-D — Persistence, Temporal Truth, Versioning, Provenance, Governed Exceptions, Outbox, Projection & Migration Implementation Plan
description: Resolves the physical persistence decisions assigned by 008-C while preserving temporal truth, module ownership, Version/Provenance semantics, governed exceptions, Official Outcome Revision basis, reliable change propagation, rebuildable projections, migration safety, and conservative retention without beginning domain implementation.
status: stable
tags: [phase-008, implementation-planning, persistence, temporal, versioning, provenance, exceptions, outbox, projection, migration]
sources:
  - resource: 008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md
  - resource: ../007-design-refinement/007-H-cross-layer-design-completeness-residual-semantic-risk-jackson-methodology-exit-readiness-audit.md
  - resource: ../canonical/governance/design-implementation-boundary.md
  - resource: ../canonical/architecture/data-persistence.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/architecture/commands-api-concurrency.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: ../canonical/concepts/versioning.md
  - resource: ../canonical/concepts/provenance.md
  - resource: ../canonical/policies/correction-authority.md
  - resource: ../canonical/policies/operational-exception-governance.md
  - resource: ../canonical/mechanisms/official-outcome-revision.md
  - resource: ../canonical/implementation/implementation-foundation.md
  - resource: ../canonical/implementation/source-topology.md
  - resource: ../canonical/implementation/verification-strategy.md
  - resource: ../canonical/implementation/persistence-history-projection.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T19:13:00Z }
---

# Purpose

Turn the 008-C persistence/history residual assignments into an implementation-ready physical plan without creating any MUDAC domain schema or executable persistence behavior.

008-D is the first detailed implementation-planning subgroup because later Identity/Access, command/API, browser continuity, domain vertical slices, outcomes/externalization, and operational evidence all need a shared answer to several questions first:

- where authoritative data physically lives;
- how current mutable state differs from immutable committed Version/history;
- how current authority can legitimately become absent after invalidation;
- how correction, replacement and Provenance remain reconstructible;
- how governed exceptions are recorded without inventing a universal override;
- how Official Outcome Revision history can later be materialized without mutating declared history;
- how committed authority reliably feeds asynchronous/convergent work;
- how projections expose freshness without becoming write authority;
- how one logical database evolves through safe, owner-scoped migrations;
- what is preserved by default until retention requirements are explicitly resolved.

# Result

**PASS — the persistence, temporal/history, Provenance, governed-exception, outbox, projection and migration implementation decisions required before 008-E/F are now sufficiently resolved.**

The durable current implementation result is promoted to [Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract](../canonical/implementation/persistence-history-projection.md).

008-D introduces no domain implementation and no new stable semantic rule family.

Current posture:

```text
Jackson Concept Design: COMPLETE / EXITED
008-A: COMPLETE
008-B: COMPLETE
008-C: COMPLETE
008-D: COMPLETE — persistence implementation plan accepted
008-E: NEXT
protected 006-D baseline: QUALIFIED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

# Authority boundary

008-D consumes rather than redefines:

- `DATA-*` relational authority/history/projection architecture;
- `MOD-*` semantic module ownership and coordination boundaries;
- `API-*` transaction/commit/concurrency architecture;
- Temporal Truth distinctions among lifecycle, currentness, validity, Affected/Stale, replacement, distribution and historical observation;
- Versioning's immutable linear lineage semantics;
- Provenance actor/author/authorizer and occurrence/recorded-time semantics;
- `OPG-*` governed-exception constraints;
- `OUT-*` Official Outcome Revision immutability/succession semantics;
- `IMPL-*` Kysely/node-postgres/explicit-migration and planning-versus-execution constraints.

Where implementation latitude remained, 008-D chooses a concrete mechanism. Where the exact payload belongs to later domain groups, 008-D fixes only the substrate pattern.

# Residuals closed by 008-D

## A2-01 — Physical temporal model

**CLOSED FOR IMPLEMENTATION PLANNING.**

MUDAC will not use one universal bitemporal table, one global status field, or event sourcing as the primary persistence model.

The physical pattern is:

```text
mutable owner current/root state
        +
immutable Version snapshots where Versioning applies
        +
append-stable owner Provenance
        +
explicit owner correction/invalidation/replacement records
        +
immutable historical observation snapshots where required
        +
derived basis-aware Affected/Stale projection state
```

This preserves current operational efficiency while satisfying current/historical/as-known/best-known reconstruction requirements.

## A2-02 — Governed-exception realization

**CLOSED FOR SUBSTRATE PLANNING.**

No universal exception table owns semantics. Each policy-owning module persists policy-specific immutable exception decisions with a common structural envelope for source condition, scope, consequence, authorizer, reason, time and Provenance.

008-F owns the later command envelope; 008-H–J own policy-specific uses.

## A2-03 — Official Outcome Revision materialization

**CLOSED FOR PHYSICAL PATTERN; CONTENT REMAINS 008-J.**

Outcomes will use an immutable revision family plus a separate current/latest-declared pointer and immutable basis/content rows. Affected status is derived from basis drift and never written back as destructive mutation of the declared revision.

## A2-05 — Cross-module atomicity support

**CLOSED FOR PERSISTENCE CAPABILITY; COORDINATOR API REMAINS 008-F.**

One PostgreSQL pool/database authority supports transaction-scoped owner-local adapters. A coordinator may bind several module adapters to one transaction when `API-006` requires it, but no module imports another module's tables/repositories.

## A2-06 — Projection refresh/freshness implementation

**CLOSED FOR SUBSTRATE PLANNING.**

Cross-module projections are basis-aware, outbox-driven where asynchronous, idempotent under duplicate/out-of-order delivery, and generation-rebuildable. They never become command authority.

# Physical database ownership

008-D fixes the initial PostgreSQL schema namespace set:

```text
competition
identity_access
judging_operations
evaluation
outcomes
external_representation
projection
platform
```

The first six are authoritative-module storage boundaries. `projection` is non-authoritative read storage. `platform` contains only narrow technical records shared by one logical database, initially migration bookkeeping and outbox machinery.

This is an implementation organization choice, not a claim that schemas are Concepts or future services.

## Database roles

Initial runtime uses one application database credential for the modular monolith rather than manufacturing per-module credentials inside one process. Semantic/source boundaries still prohibit cross-module persistence access.

Deployment later separates:

```text
runtime role   DML needed by application
migrator role  controlled DDL/schema evolution
```

Exact RDS role/IAM/secret provisioning belongs to 008-E/008-K and later authorized implementation.

# Relational primitives and conventions

008-D selects:

- PostgreSQL `uuid` for stable application resource identity;
- application-owned ID generation before persistence;
- per-root monotonic `bigint` revision tokens for mutable authority/concurrency;
- `timestamptz` for recorded and explicit occurrence/effective timestamps;
- snake_case SQL naming;
- explicit relational columns for lifecycle/authority/evidence/version basis;
- `jsonb` only for genuinely extensible metadata or technical event payloads;
- text/check-style evolvable lifecycle values rather than PostgreSQL enum types as the default;
- no global soft-delete/status convention.

The database never uses UUID lexical order as semantic or commit order.

Recorded authority timestamps are trusted server-side values. A client may provide an occurrence/source time where the use case permits it, but that value cannot masquerade as the time MUDAC recorded/established authority.

# Versioning implementation plan

Versioning subjects use owner-local lineage and immutable Version records.

Planned invariant shape:

```text
lineage/root
  stable logical subject id
  nullable current authoritative Version id
  mutable root revision

immutable Version
  stable Version id
  logical subject id
  predecessor Version id
  ordinal
  complete reconstructible authoritative content
  recorded time
  Provenance reference
```

Database constraints should ensure one linear successor chain and unique ordinals per lineage.

The current pointer is a mutable optimization/authority selection, not historical truth itself. It can become null after invalidation. An older Version is never silently reselected merely because the latest authority becomes ineligible.

Large/versioned structures may normalize immutable child rows, but a committed Version remains reconstructible as a complete state.

# Current-state revision versus Concept Versioning

008-D explicitly prevents a common implementation mistake:

**the `revision` used for optimistic concurrency is not automatically a Versioning Concept Version.**

A mutable Competition, Participation, Panel or other root may increment its technical/authoritative concurrency revision without producing a committed content Version unless the semantic owner actually invokes Versioning.

Conversely, Rubric/Scorecard Version identities are durable semantic history and cannot be replaced by a single integer row revision.

008-F must preserve this distinction in command preconditions and API results.

# Correction, invalidation and replacement implementation plan

Correction is represented by the owner-specific mechanism rather than generic update/delete.

- working Draft edits update Draft/current working storage under concurrency;
- semantic amendments create successor Version authority;
- capture correction preserves the original captured authority plus attributable corrected successor evidence;
- structural correction changes the owning relationship/state while historical observation snapshots remain unchanged;
- provenance correction appends a correcting provenance record;
- invalidation creates an explicit retained ineligibility decision and may leave no current eligible authority;
- replacement links distinct stable subject identities;
- official/public correction remains downstream succession, not source-row mutation.

No default `ON DELETE CASCADE` may erase committed evidence/history through these paths.

# Provenance implementation plan

Provenance is physically module-local.

A common structural envelope is standardized, but each module owns the meaning of its event classification and required fields. The envelope can represent:

- target subject/Version;
- Competition scope where applicable;
- acting Identity/Participation;
- semantic author separately from actor;
- exceptional authorizer separately from actor/author;
- prior/resulting revision or Version;
- source/capture channel and source reference;
- reason;
- occurrence/effective time where distinct;
- server-recorded time;
- provenance-correction link;
- request/correlation reference.

This avoids both extremes:

```text
bad: one central audit blob with no semantic ownership
bad: every module invents incompatible actor/time/source meanings

chosen: module-owned provenance + common technical envelope
```

Provenance tables are append-stable. They are not generic telemetry stores.

# Governed exceptions implementation plan

Policy-specific exception decisions are immutable records owned by the module/policy that permits them.

A decision stores enough explicit basis to answer:

- what observed/source condition existed;
- which exact policy condition was being addressed;
- which subject/Competition scope was affected;
- what consequence was permitted;
- who acted/authorized;
- why;
- when MUDAC recorded the decision;
- what prior decision it corrects/supersedes, if any.

The source condition is referenced/preserved rather than rewritten to appear satisfied.

No generic `force`, `override`, `resolve`, `accepted=true`, or administrative row mutation is accepted as the persistence model.

# Official Outcome Revision substrate plan

008-D establishes the physical family but leaves outcome payload design to 008-J.

Planned shape:

```text
outcomes official lineage/current record
   ↓ latest_declared_official_revision_id
immutable official_outcome_revision
   ├── predecessor revision
   ├── declaring authority + recorded time + provenance
   └── immutable basis/content children
          policy basis
          Coverage/exception basis
          Aggregate/Rank basis
          Award conferral basis
```

A post-Finalization source correction changes current calculations/basis comparison. It does not edit the immutable official revision. Until an explicit successor is declared, the prior revision remains latest declared official and can be presented as Affected.

008-J will specify exact basis rows, outcome payloads and succession commands.

# Transactional outbox plan

008-D chooses one narrow technical outbox under `platform`.

An immutable message row is atomically inserted with the authoritative mutation it describes. Delivery/retry metadata is stored separately so operational retries do not mutate the committed fact identity/payload.

The message envelope contains explicit producer/fact/schema/source identity fields plus minimal `jsonb` payload where needed. It prefers stable IDs/revisions/Versions over copied domain rows.

Security/privacy constraint: generic outbox payloads do not duplicate free-form Judge notes, hidden Team identity, secrets or other private content unless a later explicit consumer contract requires it.

Delivery is at-least-once. Exactly-once delivery is not assumed.

Consumers converge through:

- stable message identity;
- consumer-side deduplication;
- owner source revision/Version checks;
- idempotent application;
- explicit stale/rebuild state on failure.

A database-generated sequence or queue arrival order is never treated as global authoritative commit order.

# Projection plan

Cross-module projection tables live under `projection` and are owned by `@mudac/projections`.

Every consequential projection stores enough **explicit basis** to explain what authoritative source revisions/Versions/policies produced it. A build time or basis hash alone is insufficient.

## Incremental convergence

Projection handlers consume committed facts and refuse to regress to obsolete source revisions simply because messages arrive out of order.

A failed handler leaves committed source authority untouched; projection freshness becomes stale/failed/uncertain until convergence.

## Rebuild strategy

The default non-trivial rebuild pattern is generation-based:

```text
create generation G2: BUILDING
        ↓
reconstruct from owner public snapshot/query contracts
        ↓
catch up using committed change facts + revision checks
        ↓
validate completeness/basis
        ↓
atomically select G2 as current
        ↓
G1 becomes disposable projection history
```

This prevents readers from observing a half-rebuilt cross-module view.

Small projections may use transactional in-place rebuild only where partial state cannot become visible/misleading.

No projection rebuild directly writes authoritative module state.

# Migration implementation plan

008-D chooses **SQL-first forward migrations** executed by a small Node/`pg` migration runner.

Kysely remains the application query/access layer. The migration mechanism is deliberately plain/inspectable and does not require ORM schema synchronization.

Planned ownership:

```text
packages/modules/<owner>/migrations/
packages/projections/migrations/
packages/application/migrations/platform/
scripts/db/migrate.ts
```

The `application` migration area is limited to narrow cross-module technical records such as `platform` migration/outbox infrastructure. It may not become a location for domain tables that lack an owner.

## Migration identity and ledger

Migration files use globally unique sortable UTC timestamp + owner + slug identities. The migration runner records applied ID, owner and SHA-256 checksum in `platform.schema_migration`.

Changing an already-applied migration checksum is a blocking error. Fixes are new forward migrations.

## Migration execution

The runner:

1. acquires a PostgreSQL advisory migration lock;
2. validates catalog uniqueness and checksums;
3. executes unapplied migrations in deterministic order;
4. uses a transaction by default;
5. records successful application in the migration ledger;
6. stops on failure without allowing application startup to pretend the schema is current.

A genuinely non-transactional PostgreSQL change must be declared explicitly and reviewed/tested separately.

The API/worker do not auto-migrate on startup.

## Deployment compatibility posture

Schema evolution follows expand/migrate/contract when old/new application revisions can overlap.

Production rollback means compatible application rollback and/or a new forward repair migration. Automatic destructive `down` migration is not the production recovery model.

Runtime may verify that required migrations exist; it does not acquire DDL authority to repair the database itself.

# Data deletion and retention plan

008-D resolves the safe default but deliberately does not invent legal/product retention periods.

Until 008-K defines applicable retention requirements:

**authoritative historical data needed to reconstruct current or past authority is retained by default.**

No automated destructive lifecycle is enabled for committed Versions, Provenance, corrections, invalidations, replacements, official revisions, evaluation evidence or required source basis.

Owner-permitted unreferenced setup/Draft mistakes may eventually be hard-deletable when no retained evidence depends on them. This is an explicit owner rule, not a generic repository method.

Projection generations are disposable after safe replacement. Outbox retention remains undecided until replay/recovery/consumer requirements are fixed by 008-K.

# Kysely / node-postgres ownership plan

Later implementation will keep SQL access private to owner adapters:

```text
module domain/application
        ↓ port
module-owned PostgreSQL adapter
        ↓
owner-local Kysely table mappings
        ↓
shared PostgreSQL connection/transaction supplied by composition
```

A module's Kysely table/row types are private implementation details and may not become cross-module entities.

A cross-module application transaction can bind multiple owner adapters to one transaction-scoped database executor. 008-F defines the exact transaction-context API and transaction coordinator placement.

No additional generic persistence package is introduced by 008-D. The existing source topology is sufficient.

# Verification plan inherited by later implementation

Persistence implementation is not considered trustworthy from unit mocks alone.

When implementation is authorized, disposable real PostgreSQL evidence must cover:

- clean migration to current schema;
- supported prior fixture migration to current schema;
- checksum tamper/duplicate-ID/advisory-lock behavior;
- module-local keys/constraints and absence of destructive cross-owner cascade;
- mutable revision conflict behavior;
- immutable Version and successor-lineage constraints;
- no-current-authority after invalidation where applicable;
- Provenance actor/author/authorizer separation and correction;
- policy-specific exception source-condition preservation;
- atomic authoritative change + Version/Provenance + outbox;
- duplicate/out-of-order outbox delivery;
- projection stale detection and generation rebuild/swap;
- expand/migrate/contract compatibility;
- later backup/restore/rebuild evidence under 008-K.

No empty test suite will be represented as evidence before the corresponding implementation exists.

# 008-D decision register

These identifiers are local to the phase and are not stable-rule IDs.

| Decision | Accepted implementation choice |
| --- | --- |
| D-01 | One PostgreSQL authority database with eight physical schemas: six module owners + `projection` + narrow `platform`. |
| D-02 | UUID stable resource IDs generated before persistence; explicit ordering/revision rather than UUID order. |
| D-03 | Per-root `bigint` mutable revision tokens remain distinct from semantic Version identities. |
| D-04 | Current mutable rows plus explicit append-stable history; no primary event sourcing and no universal bitemporal table. |
| D-05 | Versioned subjects use owner-local lineage/current pointer + immutable complete Version rows; null current authority is representable. |
| D-06 | Supersession, invalidation, replacement, correction and Affected/Stale remain distinct physical mechanisms. |
| D-07 | Provenance is module-local with one compatible structural envelope; no central semantic audit god-table. |
| D-08 | Governed exceptions use policy-specific immutable decision rows; no universal override table/flag. |
| D-09 | Official Outcome Revision uses immutable outcome-owned revisions/basis plus a separate latest-declared pointer; exact content deferred to 008-J. |
| D-10 | Shared `platform` transactional outbox separates immutable message content from mutable delivery state; delivery is at-least-once. |
| D-11 | Projection correctness depends on explicit source revisions/Versions, not queue/sequence order; non-trivial rebuilds use generation swap. |
| D-12 | Module persistence stays private behind owner ports; shared transaction capability does not expose other modules' tables. |
| D-13 | Migrations are SQL-first, forward-only in production posture, checksum-verified, owner-scoped, globally ordered and advisory-lock protected. |
| D-14 | Application startup never auto-migrates; deployed migration authority is separately privileged. |
| D-15 | No generic destructive retention/soft-delete scheme; authoritative history is conserved until 008-K defines retention requirements. |
| D-16 | No new generic persistence/infrastructure workspace package is justified at this point. |

# Explicit non-decisions / later ownership

008-D does **not** preempt:

- 008-E Identity/authentication/Participation/Access/session/invitation/secrets persistence details;
- 008-F exact transaction context, command/result/idempotency/CAS/API shapes;
- 008-G IndexedDB Draft lifecycle and browser synchronization;
- 008-H Competition/Team/Division/Alias/Rubric/Panel/Encounter table and slice detail;
- 008-I Scorecard/amendment/paper-capture schema and verification flow;
- 008-J exact Coverage/Aggregate/Rank/Award/official outcome/Export/Publication records;
- 008-K production retention periods, backup/restore/SLO/security/DR evidence;
- 008-L implementation-entry authorization.

# Exit review

008-D exit criteria are satisfied:

- A2-01 physical temporal model has a concrete implementation pattern;
- A2-02 governed-exception persistence has a concrete non-generic pattern;
- A2-03 Official Outcome Revision has a physical immutability/currentness substrate without preempting 008-J;
- A2-06 outbox/projection freshness/rebuild mechanics are defined;
- I3-01 persistence/schema/migration planning is sufficiently closed for downstream planning;
- I3-12 receives a safe non-destructive default without inventing retention policy;
- module/data ownership remains consistent with `MOD-*`/`DATA-*`;
- no domain implementation was created;
- no new semantic Concept/policy/synchronization is required.

# Handoff to 008-E

008-E — **Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan** — may now assume the persistence substrate above.

008-E should define its owner-local persistent records, provider-link strategy, session/token/credential boundaries, revocation/expiry/history, Event Completed access behavior, dual-role partitioning, invitation/join-code storage, and secret/key handling while preserving the actor/author/authorizer and technical-versus-semantic-authority distinctions.

008-E remains planning only. No first executable domain slice is authorized before 008-L.