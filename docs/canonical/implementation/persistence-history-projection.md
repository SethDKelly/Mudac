---
type: Implementation Contract
title: Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract
description: Defines the accepted physical PostgreSQL realization for module-owned authority, Version/history persistence, Provenance, governed exceptions, Official Outcome Revision substrate, transactional outbox, rebuildable projections, migrations, and conservative retention defaults.
status: stable
tags: [implementation, persistence, postgresql, temporal, versioning, provenance, exceptions, outbox, projections, migrations]
sources:
  - resource: ../../008-implementation-reentry/008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md
  - resource: ../architecture/data-persistence.md
  - resource: ../architecture/application-boundaries.md
  - resource: ../architecture/commands-api-concurrency.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../concepts/versioning.md
  - resource: ../concepts/provenance.md
  - resource: ../policies/correction-authority.md
  - resource: ../policies/operational-exception-governance.md
  - resource: ../mechanisms/official-outcome-revision.md
  - resource: implementation-foundation.md
  - resource: source-topology.md
  - resource: verification-strategy.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T19:13:00Z }
---

# Purpose

Define the durable implementation choices that realize the accepted MUDAC persistence architecture before any authoritative schema is created.

This contract is downstream of `DATA-*`, `MOD-*`, `API-*`, the Temporal Truth synchronization contract, Versioning, Provenance, Correction & Authority, and Operational Exception Governance. It chooses physical conventions where those owners intentionally left implementation latitude. It does not redefine their semantics.

This owner introduces no new stable-rule namespace. Tests and later implementation should cite the existing upstream rule IDs plus this implementation owner when the physical consequence matters.

# Current execution boundary

This contract is a **Phase 008 implementation-planning result**. It does not authorize creating the schemas, migrations, repositories, outbox, projections, or other domain persistence described below.

Until 008-L explicitly authorizes a Phase 009 entry slice:

- local PostgreSQL remains schema-free with respect to MUDAC authority;
- module packages remain placeholder/minimal semantic seams;
- no migration runner or authoritative tables are added;
- no persistence decision below is evidence that domain implementation has started.

# Accepted PostgreSQL namespace model

The initial single authority database uses PostgreSQL schemas as physical ownership boundaries:

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

The first six correspond to the six authoritative server modules. `projection` is explicitly non-authoritative. `platform` is limited to narrow shared technical persistence required to operate one logical database, such as migration bookkeeping and transactional outbox delivery machinery.

A PostgreSQL schema does not become a Concept, service, or semantic owner. Schema names are implementation vocabulary and remain subordinate to the module map.

## Ownership rules

- each authoritative module owns its tables, constraints, row types, repositories and migrations inside its schema;
- `@mudac/projections` owns projection tables and projection-generation metadata;
- shared technical `platform` tables contain no Competition-domain facts whose meaning belongs to a module;
- no module directly mutates another module's schema;
- cross-module foreign keys are **not** the default and never use cascading deletion across owner boundaries;
- owner-local foreign keys, unique constraints, check constraints and nullability should enforce structurally expressible invariants;
- one runtime database credential may initially serve the modular monolith, but source/package ownership remains the authority boundary; per-module database credentials are not required merely to simulate service separation;
- migration execution uses separately privileged database authority from ordinary application DML when deployed.

# Core SQL representation conventions

The initial physical conventions are:

```text
stable resource identity      PostgreSQL uuid
mutable root revision         bigint, monotonic per root
recorded/authority time       timestamptz, server-assigned
occurrence/effective time     explicit timestamptz only where semantically material
free-form/extensible data     jsonb only when genuinely extensible
core lifecycle/authority      explicit typed columns/relations, not jsonb
```

Stable application resource IDs are allocated before persistence through an application-owned ID generator so they can participate in retries, composition and tests without depending on database row identity. Exact UUID generation algorithm is not product semantics and may evolve compatibly.

Database ordering never relies on UUID lexical order. Domain ordering uses explicit ordinal/revision fields.

Mutable authoritative roots use a monotonic `bigint` revision/concurrency token. 008-F owns its command/API serialization and comparison contract.

`recorded_at`/authority timestamps are assigned by trusted server-side persistence/application infrastructure, never accepted as client authority. Occurrence/effective timestamps are separate fields when the canonical temporal model requires them. The implementation does **not** introduce a universal bitemporal table pattern.

PostgreSQL enum types are not the default for evolvable domain lifecycle values. Initial domain state columns use explicit text-like values constrained by owner-local checks or tables so forward schema evolution does not require enum-type mutation as the only safe deployment path.

There is no universal `status`, `deleted_at`, `is_active`, or JSON catch-all that collapses lifecycle, currentness, validity, dependency currency, replacement and distribution state.

# Mutable current state versus retained history

MUDAC uses **current-state relational authority plus explicit append-stable history**, not event sourcing.

A mutable current/root row exists to answer current operational questions efficiently. Historical truth is retained separately through the mechanism appropriate to the semantic owner:

- immutable committed Version rows for Versioning subjects;
- owner-local Provenance records for meaningful authority transitions;
- explicit correction/invalidation/replacement records where those semantics apply;
- immutable historical observation snapshots where the downstream owner must preserve what was actually presented/used;
- immutable Official Outcome Revision records for declared outcomes;
- immutable Export/Publication lineage owned downstream when those slices are planned.

The current row is never treated as the sole historical record.

# Versioned subject physical pattern

Subjects that use the Versioning Concept use an owner-local **lineage + immutable version** pattern.

Conceptually:

```text
<subject>_lineage
  logical_subject_id
  current_authoritative_version_id nullable
  revision

<subject>_version
  version_id
  logical_subject_id
  predecessor_version_id nullable
  ordinal
  complete authoritative snapshot fields
  recorded_at
  provenance_id/reference
```

Required properties:

- a committed Version row is immutable;
- `(logical_subject_id, ordinal)` is unique;
- a predecessor cannot silently acquire two competing committed successors in a linear lineage;
- the current authoritative pointer is advanced only in the same authoritative transaction that commits the new Version/provenance consequence;
- `current_authoritative_version_id` may be null when no committed Version is currently eligible;
- null current authority never causes automatic fallback to an older predecessor;
- a later legitimate successor may reference retained prior lineage state even after invalidation when the owning semantic action permits it;
- Draft state is stored separately from committed Version rows and is never promoted merely by persistence.

A complete authoritative Version must remain reconstructible even if large subordinate structures are normalized into immutable child tables rather than one wide row.

# Supersession, invalidation, replacement and correction

These remain independent physical meanings.

## Supersession

Supersession is represented by an explicit successor Version/current-pointer advance. The predecessor row is not mutated to erase its prior authority.

## Invalidation

Invalidation is represented by an owner-local append-stable invalidation/eligibility decision referencing the retained target, actor/authorizer/provenance, reason and recorded time. If invalidation removes the only eligible current authority, the owner current pointer becomes null or otherwise represents no eligible current authority.

An `invalidated=true` update on the immutable Version snapshot itself is not the primary history mechanism.

## Replacement

Replacement uses an owner-local relationship/record between distinct stable subject identities. It is not encoded as Version supersession merely because one occurrence stands in place of another.

## Correction

Correction uses the semantic family's own mechanism: working-state edit, successor Version, capture correction, structural correction, provenance correction, official-outcome succession or later Publication succession. Generic destructive overwrite is not the correction substrate.

Affected/Stale are dependency-currency consequences. They are derived from basis changes and may be materialized in non-authoritative/current calculation state, but are not written into immutable historical source rows as a universal status.

# Provenance persistence pattern

Provenance remains **module-local semantic history with a common structural envelope**, not one central cross-domain audit table.

Each module that records Provenance owns its records in its own schema. A common implementation helper may standardize column names/serialization, but semantic event types and required fields remain owner-defined.

The common envelope supports, where applicable:

```text
provenance_id
subject stable id / Version id
owner-defined event classification
Competition scope
acting Identity
acting Participation
semantic author Identity/Participation when different
exceptional authorizer Identity/Participation when applicable
prior authoritative revision/Version reference
resulting authoritative revision/Version reference
source/capture channel and stable source reference
reason when materially required
occurrence/effective time when materially distinct
recorded_at
correction_of_provenance_id when correcting provenance itself
request/correlation reference for operational traceability
```

Actor, semantic author and exceptional authorizer remain independently representable. Nullability reflects semantic non-applicability, not convenience omission.

Owner-local Provenance may use supplemental `jsonb` only for genuinely variable diagnostic/source metadata. The core authority fields above remain explicit when they are semantically applicable.

A Provenance correction appends attributable successor/correction evidence. Prior provenance rows are not silently edited away.

Low-level logs, traces and security telemetry remain outside this Concept and are not copied into the domain Provenance ledger by default.

# Governed-exception persistence pattern

MUDAC does **not** create a universal `override` table or generic exception command.

Where a specific policy permits an exception, the semantic owner persists an **owner/policy-specific immutable exception decision** in its own schema. Implementations use a common structural convention sufficient to preserve `OPG-*`:

```text
exception_decision_id
subject / Competition scope
policy/condition identifier
exact source-condition basis or source revision references
permitted consequence
acting/authorizing Identity + Participation as applicable
reason
recorded_at
predecessor/correction reference if the exception decision itself is superseded or corrected
provenance reference
```

The persisted decision records what consequence was permitted despite a preserved condition. It never rewrites the condition as satisfied.

Current applicability may be derived from the latest eligible decision plus current source/policy state; it is not represented by mutating the original exception row into a generic resolved flag.

Because exception semantics are policy-specific, persistence helpers may standardize mechanics but cannot supply a shared semantic `force=true` path.

# Official Outcome Revision physical substrate

`outcomes` owns the physical Official Outcome Revision family.

The implementation uses:

- an outcomes-owned lineage/current-state record keyed by Competition;
- immutable `official_outcome_revision` records with stable revision identity and predecessor relation;
- immutable owner-specific basis/content rows sufficient to reconstruct the declared Evaluation Policy, Coverage/exception basis, Aggregate/Rank basis, and Award conferrals represented by that revision;
- explicit declaring Identity/Participation, recorded time and Provenance linkage.

Exact outcome/content columns are finalized by 008-J. 008-D fixes the **immutability/current-pointer/basis pattern**, not the domain payload ahead of that slice.

A source correction does not mutate an Official Outcome Revision. Affected/Stale is evaluated from its persisted basis against current source state. A successor official revision becomes latest declared official only through the explicit later authority-establishing transition defined by `OUT-002`.

# Transactional outbox implementation pattern

The single authority database uses a narrow shared technical outbox in the `platform` schema to realize `DATA-011` without centralizing domain ownership.

The pattern separates immutable committed message identity/content from mutable delivery mechanics:

```text
platform.outbox_message
  message_id
  producer_module
  fact_type
  fact_schema_version
  subject stable id/reference
  Competition scope where applicable
  source revision/Version reference where material
  provenance/correlation reference where material
  minimal payload jsonb
  recorded_at

platform.outbox_delivery
  message_id
  destination/consumer key
  delivery state
  attempt count
  next-attempt / last-attempt metadata
  last error classification/diagnostic reference
```

The message row is written in the same database transaction as the authoritative mutation/Version/Provenance it describes. Delivery state is updated only after commit.

Outbox semantics are **at-least-once**, not exactly-once. Consumers must be idempotent by stable message identity plus their own source revision/Version checks. A successful source commit remains authoritative even while delivery is delayed or retrying.

The outbox payload is intentionally minimal. Free-form Judge notes, hidden Team identity, secrets and other sensitive/private data are not duplicated into a generic outbox payload unless a specific consumer contract requires them and disclosure/security review permits it. Prefer stable references and owner-defined public facts over copying whole rows.

No global outbox sequence is treated as authoritative commit order. Projection correctness relies on source identities/revisions/Versions, not on assuming database sequence allocation equals cross-transaction commit order.

008-F owns the concrete transaction/outbox writer interface and lost-response/idempotency composition. 008-K owns operational retry/alert/dead-letter evidence.

# Projection implementation pattern

`@mudac/projections` owns cross-module presentation/search/operational read models. Authoritative modules remain the source of write preconditions.

## Basis and freshness

Every consequential persisted projection records an explicit source basis appropriate to that projection: stable source IDs plus root revisions, committed Version IDs, policy identifiers/Versions, Official Outcome Revision IDs, or equivalent owner-defined basis.

A generic basis hash or build timestamp may supplement but never replace the explicit basis needed to explain freshness.

Projection read state may distinguish implementation conditions such as current-enough, stale, rebuilding, failed or uncertain. These are read-model freshness states, not domain lifecycle authority.

## Incremental updates

Outbox-driven projection handlers apply messages idempotently and ignore/reconcile obsolete source revisions rather than trusting arrival order. At-least-once or out-of-order delivery must not regress a projection to older authority.

## Rebuilds

The default pattern for non-trivial cross-module projections is **generation-based rebuild**:

1. create a new projection generation marked building;
2. reconstruct from owner-provided public snapshot/query contracts rather than directly mutating/owning module tables;
3. catch the generation up with committed change facts while preserving source revision checks;
4. validate its basis/completeness;
5. atomically select the generation as current;
6. retain or remove older projection generations according to technical retention because they are non-authoritative.

A small projection may rebuild transactionally in place only when readers cannot observe a misleading partial state and the same authority/freshness requirements remain satisfied.

Projection rebuild machinery never becomes a route for changing authoritative module state.

# Database access and transaction composition

Application runtime composition creates the PostgreSQL pool/database infrastructure. Authoritative modules do not create independent connection pools merely because they are separate packages.

Each module defines only its owner-local Kysely table/row mappings and repository adapters. Other modules do not import those mappings.

The persistence layer must permit an application coordinator to bind several owner-local repository adapters to the same PostgreSQL transaction when `API-006` requires narrow cross-module atomicity. 008-F owns the exact transaction-context/unit-of-work interface and command-side locking/isolation choices.

Ordinary module code depends inward on ports/contracts rather than on `pg`, Kysely internals, transaction objects or SQL helpers leaking across public module boundaries.

# Migration ownership and execution

MUDAC uses **SQL-first, explicit, forward migration files**. Kysely remains the typed application query layer; migrations are intentionally inspectable SQL executed by a small Node/`pg` migration runner rather than application startup or automatic schema synchronization.

## Ownership layout

When implementation is authorized, the planned source layout is:

```text
packages/modules/competition/migrations/
packages/modules/identity-access/migrations/
packages/modules/judging-operations/migrations/
packages/modules/evaluation/migrations/
packages/modules/outcomes/migrations/
packages/modules/external-representation/migrations/
packages/projections/migrations/
packages/application/migrations/platform/   # narrow shared technical tables only
scripts/db/migrate.ts                       # orchestration, not semantic ownership
```

No empty migration directories are created before an authorized slice needs them.

A deterministic migration catalog gathers only these declared owner roots. Migration IDs are globally unique, sortable UTC timestamp + owner + descriptive slug identifiers. Duplicate IDs fail validation.

## Migration ledger

The runner maintains a narrow `platform.schema_migration` ledger containing at least:

- immutable migration ID;
- owner;
- SHA-256 checksum of applied content;
- applied timestamp;
- execution duration/result metadata needed for diagnosis.

An already-applied migration whose checksum/content has changed is a blocking defect. Applied migration files are append-stable; corrections use new forward migrations.

## Execution rules

- acquire a PostgreSQL advisory lock so only one migration runner mutates schema at a time;
- run each migration transactionally by default;
- a migration that genuinely requires non-transactional PostgreSQL DDL must declare that explicitly and receive separate review/evidence;
- never run production migrations automatically from API/worker startup;
- runtime startup may verify required migration presence/compatibility and fail safely when prerequisites are missing;
- use a separately privileged migrator role in deployed environments; ordinary application runtime credentials do not require DDL authority;
- schema changes follow expand/migrate/contract when old and new application revisions may overlap;
- rollback relies on compatible application rollback plus forward-fix migrations, not destructive automatic `down` execution against production data;
- cross-module DDL dependencies are avoided; if unavoidable, ordering/dependency is explicit and does not create cross-module mutation authority.

# Deletion, retention and cascade defaults

Until 008-K establishes applicable operational/legal/product retention requirements, authoritative historical evidence uses a **conservative non-destructive default**.

No automated TTL/hard-delete job is planned for:

- committed Versions;
- Provenance;
- correction/invalidation/replacement records;
- authoritative evaluation evidence;
- Official Outcome Revisions;
- evidence/source basis required to reconstruct official or externalized history.

Hard deletion remains available only where the owning domain explicitly permits deletion of unreferenced setup/Draft mistakes and no retained evidence/history depends on the record.

`ON DELETE CASCADE` is therefore not the default for authoritative history. It may be used inside an owner for truly subordinate ephemeral rows only when deleting the parent is itself semantically permitted and cannot erase retained evidence.

Projection generations are disposable after a successful replacement because projections are non-authoritative. Outbox messages/delivery records may eventually use bounded technical retention only after 008-K defines replay/recovery/evidence requirements and confirms every required consumer/rebuild path no longer depends on them.

No generic `deleted_at` soft-delete convention is introduced as a substitute for domain withdrawal, invalidation, revocation, supersession or retention policy.

# Persistence verification requirements

When the first persistence implementation is authorized, verification must use disposable real PostgreSQL and cover the physical contracts that mocks cannot prove.

At minimum, later evidence must include:

- clean database → current migration set;
- supported prior schema fixture → current migration set;
- migration ordering, advisory lock and checksum-tamper failure;
- owner-local uniqueness/check/FK constraints;
- no destructive cross-module cascade;
- monotonic root revision/CAS behavior where implemented;
- immutable committed Version rows and linear successor constraints;
- no-current-authority state after invalidation where applicable;
- actor/author/authorizer Provenance distinctions;
- provenance correction without rewrite;
- policy-specific exception preservation of source condition;
- atomic authority + Version/Provenance/outbox write;
- outbox replay/duplicate delivery convergence;
- projection out-of-order handling, stale basis detection and rebuild generation swap;
- migration/application compatibility during expand/contract rollout;
- backup/restore/rebuild evidence later under 008-K.

Fixtures and migration samples use synthetic data. Database tests do not bypass module ownership by directly mutating another module's private tables except where a migration/constraint test specifically owns that storage boundary.

# Explicit non-decisions

008-D deliberately does not decide:

- exact Competition, Identity, Encounter, Scorecard, Award, Export or Publication table columns;
- command DTOs, route shapes, idempotency-key format or transaction-context API (`008-F`);
- Cognito/Identity/session/Access persistence payloads (`008-E`);
- IndexedDB/browser Draft representation (`008-G`);
- Scorecard/paper-capture schema details (`008-I`);
- exact Official Outcome content, Export/Artifact/Publication payloads (`008-J`);
- production RDS sizing, backup retention, SLOs, recovery exercises, destructive retention schedules or repository/deployment administration (`008-K`);
- the Phase 009 entry slice (`008-L`).

# Handoff

008-E may now rely on:

- the eight-schema ownership model;
- owner-local Kysely/repository/migration boundaries;
- stable UUID resource identity and monotonic root revision convention;
- append-stable Provenance/correction history;
- conservative retention defaults;
- separate runtime versus migrator database authority.

008-F may rely on:

- one shared PostgreSQL transaction capability across owner-local adapters when explicitly coordinated;
- atomic state + Version/Provenance/outbox persistence;
- at-least-once outbox delivery;
- source revision/Version-based convergence rather than queue ordering;
- migrations never running inside request/runtime startup.

No executable domain persistence is authorized by this handoff.