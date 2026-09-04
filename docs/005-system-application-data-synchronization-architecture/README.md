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
| 005-H | Front-End State, Navigation, Component-System & Responsive Interaction Architecture | **Next** |
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

## Authoritative baseline through 005-G

005-A establishes the canonical [Architectural Foundation](../canonical/architecture/architectural-foundation.md) and `ARCH-001` through `ARCH-008`.

005-B establishes [Application Boundaries, Modules & Dependency Architecture](../canonical/architecture/application-boundaries.md) and `MOD-001` through `MOD-010`.

005-C establishes [Data, Persistence, Versioning, Provenance & Projection Architecture](../canonical/architecture/data-persistence.md) and `DATA-001` through `DATA-014`.

005-D establishes [Identity, Authentication, Access & Session Architecture](../canonical/architecture/identity-access-session.md) and `AUTH-001` through `AUTH-014`.

005-E establishes [Commands, Queries, API, Transaction & Concurrency Architecture](../canonical/architecture/commands-api-concurrency.md) and `API-001` through `API-015`.

005-F establishes [Draft Synchronization, Offline & Recovery Architecture](../canonical/architecture/synchronization-recovery.md) and `SYNC-001` through `SYNC-014`.

005-G establishes [External Representation, Artifact & Publication Architecture](../canonical/architecture/external-representation.md) and `REP-001` through `REP-015`.

The current external-representation baseline is:

- paper-origin evaluation remains Evaluation-module authority; Organizer capture does not become Judge authorship;
- each physical source has stable source reference and capture/verification provenance;
- verification confirms transcription fidelity and does not invent ambiguous Judge intent;
- relational storage owns semantic artifact/capture/publication metadata while large scans/PDFs/packages live in immutable object/blob storage behind a port;
- every durable Export/Artifact binds an exact source revision/basis, purpose, and audience/disclosure profile;
- disclosure applies to visible content plus metadata, filenames, links, QR/barcode payloads, machine-readable layers, accessibility text, manifests, previews, and delivery surfaces;
- retained Artifact bytes are immutable and carry stable identity plus cryptographic integrity digest;
- generation, validation/preview, publication, and delivery are distinct states;
- artifact generation is idempotent/retryable and may be asynchronous;
- Publication is an explicit authoritative distribution record bound to one exact Artifact;
- source corrections affect/supersede dependent representations but never rewrite historical artifact bytes;
- corrected/revised publication is successor-based and explicit;
- URLs, signed links, QR codes, printer jobs, CDN/object locations, and delivery channels are transport, not authority;
- external-representation provenance remains reconstructible end-to-end.

Concrete object-storage/CDN product, encryption policy implementation, artifact-rendering runtime/library, template technology, image/PDF scanning tools, malware/content scanning, signed-URL mechanism, retention/lifecycle automation, and AWS delivery topology remain open for 005-I.

## Next

005-H — **Front-End State, Navigation, Component-System & Responsive Interaction Architecture** will translate the established domain/UX and `ARCH-*`/`AUTH-*`/`API-*`/`SYNC-*`/`REP-*` boundaries into client application state ownership, route/navigation topology, server-state/local-Draft distinctions, component-system boundaries, responsive/accessibility behavior, and truthful command/synchronization/publication feedback without choosing UI convenience over semantic authority.