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
| 005-G | [Paper Capture, Export, Artifact, Publication & External-Representation Architecture](005-G-paper-capture-export-artifact-publication-external-representation-architecture.md) | **Complete** |
| 005-H | [Front-End State, Navigation, Component-System & Responsive Interaction Architecture](005-H-front-end-state-navigation-component-system-responsive-interaction-architecture.md) | **Complete** |
| 005-I | AWS Runtime, Deployment, Security, Observability, Backup & Cost Architecture | **Next** |
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

## Authoritative baseline through 005-H

005-A establishes [Architectural Foundation](../canonical/architecture/architectural-foundation.md) and `ARCH-001` through `ARCH-008`.

005-B establishes [Application Boundaries](../canonical/architecture/application-boundaries.md) and `MOD-001` through `MOD-010`.

005-C establishes [Data & Persistence Architecture](../canonical/architecture/data-persistence.md) and `DATA-001` through `DATA-014`.

005-D establishes [Identity, Authentication, Access & Session Architecture](../canonical/architecture/identity-access-session.md) and `AUTH-001` through `AUTH-014`.

005-E establishes [Commands, Queries, API, Transaction & Concurrency Architecture](../canonical/architecture/commands-api-concurrency.md) and `API-001` through `API-015`.

005-F establishes [Draft Synchronization, Offline & Recovery Architecture](../canonical/architecture/synchronization-recovery.md) and `SYNC-001` through `SYNC-014`.

005-G establishes [External Representation, Artifact & Publication Architecture](../canonical/architecture/external-representation.md) and `REP-001` through `REP-015`.

005-H establishes [Front-End State, Navigation & Interaction Architecture](../canonical/architecture/frontend-interaction.md) and `FE-001` through `FE-018`.

The current browser baseline is:

- React + TypeScript is the initial browser implementation family;
- React Router Data mode owns route/layout/navigation/error boundaries without becoming domain authority;
- TanStack Query owns remote client caching; route loaders may prefetch but do not create a second remote-data cache;
- client state is partitioned across session/Participation context, remote state, command state, IndexedDB-backed local Draft continuity, and ephemeral view state;
- a general-purpose global application store is not part of the baseline;
- local Draft persistence remains non-authoritative and degrades safely when unavailable;
- high-consequence commands expose confirmed/rejected/conflict/uncertain states and are never optimistically declared final;
- Judge UI remains phone-primary/task-centered; Organizer UI remains exception-first with semantic narrow-screen drill-down;
- component architecture layers design tokens, accessible primitives, semantic patterns, domain feature components, and route/workspace compositions;
- responsive changes may alter composition/density but not semantics, Access, disclosure, or legitimate recovery paths;
- core workflows target WCAG 2.2 AA semantic parity;
- context/role/logout/shared-device transitions partition or clear private query/local state appropriately;
- real-time push is optional latency optimization; correctness remains based on authoritative query/command/revalidation paths;
- route/feature error boundaries contain client failure without implying authoritative source-state loss.

Concrete package manager/build tool, CSS implementation, component primitive library, IndexedDB wrapper, service-worker library, telemetry/testing stack, and push transport remain implementation choices constrained by `FE-*`.

## Next

005-I — **AWS Runtime, Deployment, Security, Observability, Backup & Cost Architecture** will bind the accepted modular-monolith, PostgreSQL, server-session, artifact, browser, synchronization, and CI/CD contracts to a concrete AWS production topology. It will choose runtime/database/object/CDN/auth/network/secret/monitoring/backup mechanisms, define environment/deployment and failure boundaries, establish security/operations posture, and model cost without allowing AWS services to redefine upstream MUDAC authority.