# Architecture

This subtree preserves the architecture MUDAC selected before the latest Jackson methodology completion reassessment.

## Current authority state

**SUSPENDED AS A CONCEPT-DESIGN CONSTRAINT.**

Concept Design is reopened through the Phase 009 realignment. Until successful Phase 017 closure and a separate downstream architecture/engineering re-entry, these documents are **candidate downstream architecture knowledge**, not current authority over product meaning.

The controlling rules are:

- [Design / Implementation Boundary](../governance/design-implementation-boundary.md)
- [Downstream Architecture & Implementation Authority Quarantine](../governance/downstream-authority-quarantine.md)

## Preserved candidate architecture

* [Architectural Foundation, Quality Attributes & Trust Boundaries](architectural-foundation.md)
* [Application Boundaries, Modules & Dependency Architecture](application-boundaries.md)
* [Data, Persistence, Versioning, Provenance & Projection Architecture](data-persistence.md)
* [Identity, Authentication, Access & Session Architecture](identity-access-session.md)
* [Commands, Queries, API, Transaction & Concurrency Architecture](commands-api-concurrency.md)
* [Draft Synchronization, Offline & Recovery Architecture](synchronization-recovery.md)
* [External Representation, Artifact & Publication Architecture](external-representation.md)
* [Front-End State, Navigation & Interaction Architecture](frontend-interaction.md)
* [AWS Runtime, Security & Operations Architecture](aws-runtime-operations.md)

## Permitted use during Phases 010–017

Architecture material may be consulted only to:

- detect implementation/architecture contamination of conceptual design;
- expose assumptions worth challenging;
- understand historical rationale;
- preserve evidence for later post-closure revalidation.

It must not be used to justify a Concept boundary, dependency, scope decision, mapping, familiar concept, synchronization, integrity trade-off, or misfit disposition because a framework/database/cloud/module design already expects it.

A successful Phase 017 closure will **not automatically reactivate** these documents. A separate downstream re-entry must compare them against the closed conceptual design and decide what remains justified.
