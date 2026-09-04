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
| 005-D | [Identity, Authentication, Participation, Access & Session Architecture](005-D-identity-authentication-participation-access-session-architecture.md) | **Complete** |
| 005-E | [Commands, Queries, API Contracts, Transactions, Idempotency & Concurrency Architecture](005-E-commands-queries-api-contracts-transactions-idempotency-concurrency-architecture.md) | **Complete** |
| 005-F | [Draft Persistence, Synchronization, Offline/Degraded Operation & Conflict Recovery](005-F-draft-persistence-synchronization-offline-degraded-operation-conflict-recovery.md) | **Complete** |
| 005-G | Paper Capture, Export, Artifact, Publication & External-Representation Architecture | **Next** |
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

## Authoritative baseline through 005-F

005-A establishes the canonical [Architectural Foundation](../canonical/architecture/architectural-foundation.md) and `ARCH-001` through `ARCH-008`.

005-B establishes the canonical [Application Boundaries, Modules & Dependency Architecture](../canonical/architecture/application-boundaries.md) and `MOD-001` through `MOD-010`.

005-C establishes the canonical [Data, Persistence, Versioning, Provenance & Projection Architecture](../canonical/architecture/data-persistence.md) and `DATA-001` through `DATA-014`.

005-D establishes the canonical [Identity, Authentication, Access & Session Architecture](../canonical/architecture/identity-access-session.md) and `AUTH-001` through `AUTH-014`.

005-E establishes the canonical [Commands, Queries, API, Transaction & Concurrency Architecture](../canonical/architecture/commands-api-concurrency.md) and `API-001` through `API-015`.

005-F establishes the canonical [Draft Synchronization, Offline & Recovery Architecture](../canonical/architecture/synchronization-recovery.md) and `SYNC-001` through `SYNC-014`.

The current continuity baseline is:

- local/browser persistence may preserve eligible non-authoritative Draft working content and last-known read context;
- local Drafts bind to stable Identity/Participation/Competition/Encounter/Scorecard/Rubric identities and a last-confirmed server revision;
- synchronization is revision-aware and idempotent against the server-owned Draft rather than transparent multi-master replication;
- stale conflicts preserve both current server Draft and unsynchronized local Judge work; silent last-write-wins is prohibited;
- automatic merge is permitted only where semantic safety is demonstrable; otherwise Judge reconciliation is explicit;
- multiple devices converge on one logical Scorecard and never create duplicate evaluation weight to escape conflict;
- Finalization, Amendment Finalization, exceptional Access changes, Competition lifecycle, official outcomes, and publication require reachable server authority;
- lost/uncertain consequential responses reconcile using original idempotency/command context before another transition;
- reconnect re-establishes current authentication, Participation, Access, logical identity, and server revision before applying queued work;
- cached reads remain stale-capable/non-authoritative and disclosure-bounded;
- Access expiry/revocation blocks automatic upload of pending private work;
- paper/electronic overlap converges on one logical Scorecard while preserving Judge authorship, capture actor, physical source, and conflict evidence;
- sync status separately represents server confirmation, local pending work, conflict, uncertainty, Finalization, and recovery-required states;
- when digital authority cannot be trusted and the event must continue, paper is the preferred authoritative continuity fallback.

The exact browser persistence API, local encryption mechanism, service-worker/background-sync strategy, autosave cadence, WebSocket/SSE transport, merge UI, local retention period, queue/broker, and AWS connectivity/failover services remain deliberately open.

## Next

005-G — **Paper Capture, Export, Artifact, Publication & External-Representation Architecture** will define how physical evidence enters the authoritative system, how generated artifacts bind to source Versions/revisions, how disclosure profiles are applied, and how generation/publication/republication remain distinct and historically traceable.