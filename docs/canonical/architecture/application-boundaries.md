---
type: Architecture Contract
title: Application Boundaries, Modules & Dependency Architecture
description: Defines MUDAC's authoritative application modules, non-authoritative projection/query subsystem, cross-module coordination, dependency direction, and initial modular-monolith posture.
status: stable
tags: [architecture, modules, dependencies, modular-monolith, application-boundaries]
sources:
  - resource: ../../005-system-application-data-synchronization-architecture/005-B-application-boundaries-modules-domain-services-dependency-architecture.md
  - resource: architectural-foundation.md
  - resource: ../concepts/competition.md
  - resource: ../concepts/participation.md
  - resource: ../concepts/access.md
  - resource: ../concepts/judging-encounter.md
  - resource: ../concepts/rubric.md
  - resource: ../concepts/scorecard.md
  - resource: ../concepts/award.md
  - resource: ../concepts/export.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T04:20:00Z }
---

# Purpose

Define the current application responsibility boundaries and dependency rules that later persistence, API, synchronization, front-end, and runtime architecture must implement.

MUDAC begins with one authoritative server-side application deployment composed of explicit semantic modules. The application is modular by domain/authority responsibility, not by one module per Concept and not by current vendor/framework constraints.

# Module map

## Competition Governance

Owns Competition lifecycle, Division, Team, Alias, Team Attributes, and structural competition configuration facts.

## Identity, Participation & Access

Owns MUDAC Identity continuity, Competition-scoped Participation, role participation state, and Access semantics. Authentication-provider technology remains an adapter concern.

## Judging Operations

Owns Panel, Panel Membership/composition, Judging Encounter lifecycle, effective participants, recusal/absence/substitution/replacement, and Encounter obligations.

## Evaluation

Owns Rubric/Criteria/Notes, Rubric Versions, Scorecard logical identity, Draft/Finalized/amendment state, Judge-authored evaluation content, and paper-origin Scorecard capture once physical evidence is translated into the same logical evaluation.

## Outcomes & Closeout

Owns Evaluation Policy relevant to outcome derivation, Coverage, Aggregate, Rank, Reconciliation, Award, outcome-readiness facts, and Official Outcome Revision. Competition Finalization itself remains a Competition lifecycle transition coordinated with this module rather than absorbed by it.

## External Representation

Owns Export identity/state, source binding, artifact generation intent, publication/republication/current-distribution state, and audience/disclosure application for external representations.

# Non-authoritative projection/query subsystem

Cross-module operational/search/reporting views may be materialized or optimized independently. They own read shape, not product-domain write authority.

Operational dashboards, search, readiness summaries, reconciliation queues, and similar projections may be stale where explicitly tolerated. Consequential commands revalidate authoritative state through module owners in accordance with [ARCH-004](architectural-foundation.md#arch-004).

# Application coordination layer

Cross-module use cases are coordinated above module owners through explicit application interfaces.

The coordination layer may sequence several owner operations and later host transaction/workflow mechanics, but it does not become a second semantic owner and does not copy module invariants.

Examples include Competition readiness/finalization, Encounter start with cross-context validation, paper capture coordination, and post-finalization correction propagation.

<a id="mod-001"></a>
## MOD-001 — The initial authoritative application is a modular monolith

MUDAC begins with one authoritative application deployment divided into explicit semantic modules. Independent services require a demonstrated scale, isolation, availability, ownership, or technology driver rather than speculative distribution.

<a id="mod-002"></a>
## MOD-002 — Each authoritative fact and command has one module owner

Every authoritative business fact and state-changing command has one primary semantic owner. Other modules may reference/consume that fact through declared contracts but do not directly mutate it.

<a id="mod-003"></a>
## MOD-003 — Cross-module interaction cannot bypass public ownership boundaries

Cross-module interaction uses stable identities, public query/command contracts, or published facts/events. A module must not directly use another module's repository, table/collection, ORM/data entity, or internal service as an authority shortcut.

<a id="mod-004"></a>
## MOD-004 — Cross-module workflows coordinate above module owners

Application/use-case coordinators may sequence multiple owner operations. They do not become semantic owners of the participating module state and may not recreate those modules' business invariants.

<a id="mod-005"></a>
## MOD-005 — Dependency direction remains acyclic and downstream-oriented

Module dependencies should remain acyclic. Evidence/configuration-producing modules do not depend backward on downstream outcome or representation concerns merely to simplify orchestration.

Particularly, Evaluation does not depend on Rank/Award, and upstream authoritative modules do not depend on Export artifacts to establish their own state.

<a id="mod-006"></a>
## MOD-006 — Projection/query composition is non-authoritative

Cross-module read models may compose, denormalize, cache, search, and optimize current information, but they have no product-domain write authority and cannot be the sole precondition source for consequential commands.

<a id="mod-007"></a>
## MOD-007 — Cross-cutting technical reuse does not centralize semantic ownership

Versioning, Provenance, identity/request primitives, event envelopes, concurrency tokens, and related technical capabilities may use shared implementation primitives. The module owning the affected state remains responsible for the semantic meaning of versions, corrections, attribution, and authoritative transitions.

<a id="mod-008"></a>
## MOD-008 — Shared foundation remains small and business-neutral

Shared application/domain code is limited to broadly reusable primitives and helpers. Business entities, policies, authorization decisions, repositories, and generic multi-domain "services" do not belong in a common dumping ground.

<a id="mod-009"></a>
## MOD-009 — Infrastructure depends inward through application/module ports

Persistence, external providers, transports, queues, artifact stores, telemetry, and framework adapters implement or invoke application/module contracts. Business rules do not depend directly on vendor/framework APIs.

<a id="mod-010"></a>
## MOD-010 — Deployment boundaries may evolve without changing semantic boundaries

A module may later be extracted into a separate deployable unit only when a concrete driver justifies the additional network, consistency, and operational complexity. Extraction preserves module contracts, stable identities, and authority semantics.

# Dependency shape

```text
UI / HTTP / jobs / external adapters
              ↓
      application coordination
              ↓
       module public contracts
              ↓
 module domain/application logic
              ↓
       module-owned ports
              ↑
 infrastructure implementations
```

Cross-module state changes never occur by writing through another module's storage implementation.

# Shared/cross-cutting concepts

[Versioning](../concepts/versioning.md) and [Provenance](../concepts/provenance.md) remain cross-cutting product concepts rather than a central god-module. Each authoritative module owns the version/provenance semantics of its resources while shared technical primitives may standardize IDs, timestamps, actor context, revision envelopes, and persistence mechanisms.

# Evolution posture

The selected posture is **modular monolith first, not monolith forever**.

Service extraction must be justified by evidence such as materially different scaling, security/isolation, availability/failure containment, team ownership/deployment cadence, or an incompatible runtime requirement. Physical deployment topology is allowed to change later without changing the semantic ownership map established here.
