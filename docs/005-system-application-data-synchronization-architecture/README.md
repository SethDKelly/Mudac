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
| 005-E | Commands, Queries, API Contracts, Transactions, Idempotency & Concurrency Architecture | **Next** |
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

## Authoritative baseline through 005-D

005-A establishes the canonical [Architectural Foundation](../canonical/architecture/architectural-foundation.md) and `ARCH-001` through `ARCH-008`.

005-B establishes the canonical [Application Boundaries, Modules & Dependency Architecture](../canonical/architecture/application-boundaries.md) and `MOD-001` through `MOD-010`.

005-C establishes the canonical [Data, Persistence, Versioning, Provenance & Projection Architecture](../canonical/architecture/data-persistence.md) and `DATA-001` through `DATA-014`.

005-D establishes the canonical [Identity, Authentication, Access & Session Architecture](../canonical/architecture/identity-access-session.md) and `AUTH-001` through `AUTH-014`.

The current structural/security baseline is:

- one authoritative server-side application begins as a modular monolith with module-owned relational state;
- authentication is provider-backed and standards-compatible but does not grant Competition authority;
- external authenticated subjects map explicitly to stable MUDAC Identity rather than email/name/device;
- Competition Participation remains MUDAC-owned current-event state and dual-role contexts remain explicit;
- capability-oriented Access is recomputed from current authoritative context at protected application/module boundaries;
- the browser uses an opaque first-party server session rather than long-lived script-readable bearer credentials;
- session/selected Participation context improves continuity but cannot extend revoked/expired Access;
- Event Completed expires ordinary Judge private-evaluation capability through source-state authorization, even if a stale session remains authenticated;
- invitation/QR/event-code possession alone never establishes Identity or Access;
- post-event Judge correction uses narrow temporary Access plus Identity reverification;
- lost/shared device handling revokes/clears session context without changing semantic Identity/Participation/Scorecard identity;
- step-up authentication increases proof confidence but does not create capability;
- routine system administration and break-glass remain distinct from Competition decision authority;
- provider replacement/federation expansion is isolated behind an authentication adapter and cannot rewrite MUDAC authorship/history.

The concrete identity provider, default passwordless/federated/passkey mechanism, exact session durations/store, CSRF mechanics, transaction/locking rules, API protocol, queue/broker, offline Draft storage, and AWS security/runtime services remain deliberately open.

## Next

005-E — **Commands, Queries, API Contracts, Transactions, Idempotency & Concurrency Architecture** will define how authenticated/authorized requests cross module boundaries, how transaction and optimistic-concurrency rules protect authoritative state, how idempotent retries converge, and how query/API contracts expose fresh/stale state without turning transport semantics into product authority.