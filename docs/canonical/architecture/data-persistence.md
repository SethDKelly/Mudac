---
type: Architecture Contract
title: Data, Persistence, Versioning, Provenance & Projection Architecture
description: Defines authoritative relational persistence, module-owned storage boundaries, immutable Version/provenance semantics, rebuildable projections, and reliable change propagation for MUDAC.
status: stable
tags: [architecture, data, persistence, versioning, provenance, projections]
sources:
  - resource: ../../005-system-application-data-synchronization-architecture/005-C-data-model-persistence-versioning-provenance-derived-projection-architecture.md
  - resource: architectural-foundation.md
  - resource: application-boundaries.md
  - resource: ../concepts/versioning.md
  - resource: ../concepts/provenance.md
  - resource: ../concepts/scorecard.md
  - resource: ../mechanisms/official-outcome-revision.md
  - resource: ../policies/correction-authority.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T05:52:55Z }
---

# Purpose

Define how MUDAC stores authoritative current state, committed history, provenance, and read projections without allowing physical storage topology to override application ownership or product semantics.

The initial persistence model is a single PostgreSQL-compatible relational authority store with module-owned logical namespaces, plus non-authoritative projection storage within the same deployment boundary as appropriate.

<a id="data-001"></a>
## DATA-001 — Authoritative persistence is relational and PostgreSQL-compatible

MUDAC's primary authoritative data store uses a PostgreSQL-compatible relational model because the system requires explicit identity relationships, uniqueness, transactionality, constrained lifecycle state, stable Version references, and event-day concurrency integrity.

Concrete AWS hosting is owned by [AWS-005](aws-runtime-operations.md#aws-005), which currently realizes this contract with Amazon RDS for PostgreSQL Multi-AZ. `DATA-001` remains the database-family/semantic persistence owner rather than duplicating runtime topology here.

<a id="data-002"></a>
## DATA-002 — One logical authority database initially; storage ownership remains module-scoped

The modular monolith begins with one logical authority database. Competition Governance, Identity/Participation/Access, Judging Operations, Evaluation, Outcomes/Closeout, and External Representation each own their schema/namespace, migrations, constraints, and persistence ports.

Physical co-location is an operational choice and does not merge semantic ownership.

<a id="data-003"></a>
## DATA-003 — Durable identities are stable and independent of storage/business labels

Durable resources use opaque stable application identifiers that survive schema moves, Version creation, projection rebuild, artifact generation, and future module/service extraction.

Aliases, emails, labels, titles, ordinal positions, and other mutable business values are not durable resource identity.

<a id="data-004"></a>
## DATA-004 — Physical co-location does not permit cross-module storage bypass

A module may not directly mutate another module's tables/repositories because they share a database. Cross-module references use stable IDs and module contracts under [MOD-003](application-boundaries.md#mod-003).

Cross-module foreign keys are not assumed as a default ownership mechanism; any such constraint must remain acyclic/non-cascading and must not make domain meaning depend on storage coupling.

Semantically required historical snapshots—such as Alias/Division observed by an Encounter—are permitted because the downstream module owns that historical observation rather than caching another module's current truth.

<a id="data-005"></a>
## DATA-005 — Working/current state and committed Versions remain structurally distinct

Mutable working/current records may be updated under owning-module command/concurrency rules. A persisted Draft remains a Draft.

When the domain establishes a committed Version, persistence creates a distinct immutable Version record and, where appropriate, advances a current-authoritative Version pointer for the logical lineage.

See [SC-001](../concepts/scorecard.md#sc-001) and [SC-002](../concepts/scorecard.md#sc-002).

<a id="data-006"></a>
## DATA-006 — Committed Versions and meaningful Provenance are append-stable

Committed Version records are immutable. Semantic corrections/amendments create successor state rather than editing prior committed truth.

Meaningful Provenance is appended with actor/author/authorizer/capture/source/reason context where applicable. Shared technical envelopes may standardize representation, but each owning module retains semantic responsibility under [MOD-007](application-boundaries.md#mod-007).

<a id="data-007"></a>
## DATA-007 — Referenced authoritative evidence is not erased through ordinary destructive cascade

Once an authoritative resource participates in retained evidence, Version history, provenance, outcome basis, or external representation lineage, ordinary deletion/cascade behavior must not erase that history.

Withdrawal, invalidation, supersession, replacement, and correction are represented explicitly where the domain provides those semantics. Hard deletion is limited to domain-permitted unreferenced setup/Draft mistakes.

<a id="data-008"></a>
## DATA-008 — Persisted derived calculations remain reconstructible from an identified basis

Coverage, Aggregate, Rank, readiness, and similar derived values may be materialized for performance only when the persisted result records enough source/policy/calculation basis to determine what produced it and whether it is stale or affected.

Derived rows are not independently editable authority. A changed basis invalidates/recomputes them.

An [Official Outcome Revision](../mechanisms/official-outcome-revision.md#out-001) is different: explicit Finalization freezes an immutable official snapshot/basis, and later correction produces a successor revision under `OUT-002`.

<a id="data-009"></a>
## DATA-009 — Read projections are disposable, rebuildable, and non-authoritative

Cross-module dashboards, search indexes, reconciliation queues, readiness summaries, and presentation-oriented calculated views may use separate projection tables/indexes.

No user-authored, official, or otherwise authoritative fact may exist only in projection storage. Projection loss is recovered by rebuild rather than treating projection backups as primary domain authority.

See [ARCH-004](architectural-foundation.md#arch-004) and [MOD-006](application-boundaries.md#mod-006).

<a id="data-010"></a>
## DATA-010 — Projection freshness and authority basis remain observable

Projection sets retain enough source watermark/version and build/update metadata for the application to distinguish current-enough read state from stale, rebuilding, failed, or uncertain projection state.

A consequential command still revalidates authoritative module state rather than trusting the projection watermark as write authority.

<a id="data-011"></a>
## DATA-011 — Asynchronous change propagation is transactionally coupled to the source change

When an authoritative mutation must feed projections or asynchronous consumers, the owning transaction writes a durable outbox/change record atomically with authoritative state/Version/Provenance changes.

Dispatch occurs after commit. Consumers are designed for repeat delivery and idempotent application so that committed authority cannot be silently separated from the notification needed to rebuild downstream read state.

<a id="data-012"></a>
## DATA-012 — Outbox/events do not replace authoritative state or require primary event sourcing

Outbox messages and published facts describe committed authoritative changes. They may be durable/replayable for projection/integration purposes, but they are not the primary source from which all current domain state must be reconstructed.

MUDAC does not adopt event sourcing as its baseline persistence architecture.

<a id="data-013"></a>
## DATA-013 — Database constraints reinforce owner invariants but do not replace domain authority checks

Within an owning module, primary/unique keys, local foreign keys, check constraints, nullability, and concurrency/idempotency uniqueness should encode structurally expressible invariants.

Database constraints do not replace contextual Access, lifecycle preconditions, Judge authorship semantics, disclosure policy, or cross-module coordination logic.

<a id="data-014"></a>
## DATA-014 — Core semantic fields remain explicit; semi-structured storage is reserved for genuinely extensible data

Lifecycle, authority, evidence identity, Version basis, participation, scoring basis, and other fields used by canonical invariants/queries remain explicitly modeled.

JSON/semi-structured storage may support genuinely extensible descriptive metadata, but must not become an escape hatch for avoiding schema evolution of core product semantics.

# Logical topology

The initial logical storage shape is:

```text
authority database
├── Competition Governance namespace
├── Identity / Participation / Access namespace
├── Judging Operations namespace
├── Evaluation namespace
├── Outcomes & Closeout namespace
├── External Representation namespace
├── Projection namespace (non-authoritative)
└── narrow platform/integration records (for example outbox)
```

Exact SQL schema names remain implementation details.

# Version / Provenance posture

MUDAC uses **current-state relational persistence plus append-stable committed history**, not system-wide event sourcing.

Typical versioned subjects use:

```text
logical lineage/root
   ↓ current_authoritative_version_id
immutable Version 1
immutable Version 2
...

plus append-only meaningful provenance
```

Draft persistence may coexist with Version history but cannot be confused with committed authority.

# Projection posture

Projection data may be denormalized and optimized aggressively because it is rebuildable. It must preserve enough freshness/basis metadata to support [ARCH-008](architectural-foundation.md#arch-008), and high-consequence writes always return to authoritative module state for validation.

# Evolution posture

A future service extraction may separate a module's database/schema when a real driver justifies it. Stable IDs, explicit module contracts, module-owned migrations, non-authoritative projections, and transactional published facts are chosen now so that later extraction does not require changing product meaning.
