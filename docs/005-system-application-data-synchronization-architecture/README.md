# Phase 005 — System, Application, Data & Synchronization Architecture

Status: **In Progress**

## Purpose

Phase 005 translates the accepted MUDAC product, UX, and knowledge-governance contracts into a coherent system/application architecture before production implementation begins.

The phase chooses architecture mechanisms only after identifying the upstream canonical contracts they must satisfy. It does not treat framework, database, authentication, offline, or AWS convenience as permission to redefine MUDAC meaning.

Preferred current authority remains [Canonical Knowledge](../canonical/). Accepted architecture decisions become current owners under [Canonical Architecture](../canonical/architecture/); this numbered phase preserves architecture reasoning, alternatives, and decision lineage.

## Phase plan

| Group | Topic | Status |
| --- | --- | --- |
| 005-A | [Architectural Drivers, Quality Attributes, Trust Boundaries & Decision Principles](005-A-architectural-drivers-quality-attributes-trust-boundaries-decision-principles.md) | **Complete** |
| 005-B | [Application Boundaries, Modules, Domain Services & Dependency Architecture](005-B-application-boundaries-modules-domain-services-dependency-architecture.md) | **Complete** |
| 005-C | [Data Model, Persistence, Versioning, Provenance & Derived-Projection Architecture](005-C-data-model-persistence-versioning-provenance-derived-projection-architecture.md) | **Complete** |
| 005-D | Identity, Authentication, Participation, Access & Session Architecture | **Next** |
| 005-E | Commands, Queries, API Contracts, Transactions, Idempotency & Concurrency Architecture | Planned |
| 005-F | Draft Persistence, Synchronization, Offline/Degraded Operation & Conflict Recovery | Planned |
| 005-G | Paper Capture, Export, Artifact, Publication & External-Representation Architecture | Planned |
| 005-H | Front-End State, Navigation, Component-System & Responsive Interaction Architecture | Planned |
| 005-I | AWS Runtime, Deployment, Security, Observability, Backup & Cost Architecture | Planned |
| 005-J | Phase 005 Consolidation, Threat/Failure Review & Implementation-Readiness Exit | Planned |

## Architecture sequence

```text
architectural drivers / trust / quality attributes
        ↓
application boundaries and dependency direction
        ↓
data/persistence + identity/access
        ↓
command/query/API/transaction semantics
        ↓
synchronization and degraded recovery
        ↓
external representations + front-end state
        ↓
runtime/AWS/operations
        ↓
integrated failure/threat/readiness review
```

## Authoritative baseline through 005-C

005-A establishes the canonical [Architectural Foundation](../canonical/architecture/architectural-foundation.md) and `ARCH-001` through `ARCH-008`.

005-B establishes the canonical [Application Boundaries, Modules & Dependency Architecture](../canonical/architecture/application-boundaries.md) and `MOD-001` through `MOD-010`.

005-C establishes the canonical [Data, Persistence, Versioning, Provenance & Projection Architecture](../canonical/architecture/data-persistence.md) and `DATA-001` through `DATA-014`.

The current structural/data baseline is:

- one authoritative server-side application deployment begins as a modular monolith;
- six semantic authority modules own distinct state and storage namespaces;
- one PostgreSQL-compatible relational authority database is used initially;
- physical co-location does not permit cross-module storage bypass;
- durable resources use stable opaque application IDs independent of business labels/storage location;
- mutable working/current state is structurally distinct from immutable committed Versions;
- meaningful Provenance and committed Versions are append-stable;
- ordinary destructive cascade cannot erase referenced authoritative evidence;
- persisted derived calculations record reconstructible basis information;
- cross-module projections are disposable/rebuildable and remain non-authoritative;
- projection freshness/basis is observable;
- asynchronous change propagation uses a transactional outbox/change record where needed;
- MUDAC does not adopt primary event sourcing as the baseline persistence architecture;
- database constraints reinforce owner invariants but do not replace application/domain authority checks;
- core semantics remain explicit rather than hidden in semi-structured blobs.

AWS database hosting, ORM/migration tooling, exact identifier generator, transaction isolation/locking, identity provider, API protocol, queue/broker, offline Draft storage, and backup topology remain deliberately open.

## Next

005-D — **Identity, Authentication, Participation, Access & Session Architecture** will determine how external authentication establishes Identity continuity while MUDAC retains Competition-scoped Participation/Access authority, session security, event-day onboarding/reverification, role switching, shared-device safety, and post-event access expiry.