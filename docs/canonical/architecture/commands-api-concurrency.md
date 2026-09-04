---
type: Architecture Contract
title: Commands, Queries, API, Transaction & Concurrency Architecture
description: Defines MUDAC's HTTPS/JSON command-query boundary, authoritative transaction semantics, idempotency, optimistic concurrency, targeted locking, result contracts, and projection-aware read behavior.
status: stable
tags: [architecture, api, commands, queries, transactions, idempotency, concurrency]
sources:
  - resource: ../../005-system-application-data-synchronization-architecture/005-E-commands-queries-api-contracts-transactions-idempotency-concurrency-architecture.md
  - resource: architectural-foundation.md
  - resource: application-boundaries.md
  - resource: data-persistence.md
  - resource: identity-access-session.md
  - resource: ../concepts/scorecard.md
  - resource: ../invariants/truthful-authority-under-uncertainty.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T05:52:55Z }
---

# Purpose

Define how MUDAC reads state and executes authoritative intent across the application boundary while preserving current authorization, module ownership, transactional integrity, retry convergence, and truthful uncertainty.

<a id="api-001"></a>
## API-001 — Commands and queries are distinct application contracts

Queries are side-effect-free reads. Commands express semantic intent to change authoritative state and route to one primary owner or an explicit cross-module coordinator.

High-consequence transitions use explicit command semantics rather than hiding Finalization, invalidation, exception acceptance, official closeout, or publication behind generic record updates.

<a id="api-002"></a>
## API-002 — The primary browser application contract is versioned HTTPS/JSON

The initial external application API uses HTTPS with JSON request/response contracts. `GET` is used for side-effect-free retrieval; ordinary resource mutation verbs may be used for genuinely simple edits; high-consequence semantic transitions use explicit command/action resources.

GraphQL and gRPC are not baseline browser-authority contracts. They may be reconsidered later for a concrete read/service-boundary need without changing the application semantics defined here.

<a id="api-003"></a>
## API-003 — Transport adapters do not own domain authority

HTTP routes, DTOs, serializers, middleware, and framework handlers map requests into application/module contracts. They do not own MUDAC invariants, authorize from client claims alone, or mutate repositories directly.

Current Access and resource/lifecycle preconditions are evaluated at protected application/module boundaries under [AUTH-004](identity-access-session.md#auth-004).

<a id="api-004"></a>
## API-004 — A successful authoritative command is confirmed only after transaction commit

A command reports confirmed success only after the owning authoritative transaction has committed its state changes and any required Version, Provenance, and transactional outbox/change records.

Pre-commit validation or an accepted request is not equivalent to authoritative success. This realizes [ARCH-002](architectural-foundation.md#arch-002).

<a id="api-005"></a>
## API-005 — Single-module commands use one owning transaction boundary

The default state-changing command executes inside one owning module transaction: resolve current state, re-evaluate Access/preconditions, check idempotency/concurrency, apply invariants, persist authority/Version/Provenance/outbox, then commit.

Module storage ownership remains intact under [MOD-002](application-boundaries.md#mod-002) and [DATA-004](data-persistence.md#data-004).

<a id="api-006"></a>
## API-006 — Cross-module atomic transactions are narrow and coordinator-owned

While MUDAC is a modular monolith over one authority database, an application coordinator may deliberately use one database transaction across module public contracts when a single user-visible authoritative transition must be atomic across those owners.

The coordinator does not mutate another module's storage directly or absorb its invariants. Work that does not require atomic authority propagates after commit through facts/outbox. Future service extraction must explicitly redesign any cross-module transaction seam.

<a id="api-007"></a>
## API-007 — Optimistic concurrency is the default mutable-state strategy

Mutable authoritative roots carry a monotonic revision/concurrency token. Commands whose correctness depends on previously observed state supply or derive an expected revision/precondition.

A stale expected revision fails as a concurrency conflict rather than silently overwriting newer authority. Database constraints continue to enforce structurally expressible uniqueness/invariants.

<a id="api-008"></a>
## API-008 — Pessimistic locking and stronger isolation are targeted tools, not global defaults

The relational baseline uses `READ COMMITTED` together with explicit revision checks, constraints, and narrow row locking where same-root transition races require it.

A command may use stronger isolation such as `SERIALIZABLE` for a demonstrated multi-row/predicate invariant that is safer to protect transactionally. Lock/isolation elevation remains command-specific, bounded, retry-aware, and observable.

<a id="api-009"></a>
## API-009 — Externally retryable commands have durable idempotency semantics

State-changing commands vulnerable to duplicate client/network retry use an idempotency key scoped to the relevant authenticated command context. The application records enough execution/result identity to return the same committed semantic result on equivalent replay.

Reusing a key for materially different intent is rejected. Idempotency complements rather than replaces logical uniqueness and domain constraints.

<a id="api-010"></a>
## API-010 — Lost responses reconcile to committed authority instead of inviting blind repetition

If a command may have committed but its response is lost, retry/recovery can determine the existing authoritative result through the same idempotency key or stable resource state.

Clients must represent unresolved outcome as uncertain until reconciliation. A timeout alone is never proof that a command failed. See [INV-010](../invariants/truthful-authority-under-uncertainty.md#inv-010).

<a id="api-011"></a>
## API-011 — Query freshness is explicit and never becomes command authority

Queries may read owner state or non-authoritative projections. Projection-backed responses expose basis/freshness metadata where material so clients can distinguish current-enough, stale, rebuilding, failed, or uncertain read state.

A subsequent command independently revalidates authoritative state under [ARCH-004](architectural-foundation.md#arch-004) and [DATA-010](data-persistence.md#data-010).

<a id="api-012"></a>
## API-012 — Application results distinguish semantic failure classes

Public command/query contracts distinguish confirmed success, validation/precondition failure, authorization denial, appropriate not-found/concealed result, concurrency conflict, idempotent replay, idempotency misuse, temporary infrastructure failure, and uncertain outcome where applicable.

Transport status codes map to these semantics but do not replace them. Internal stack/database details and sensitive authorization rationale are not exposed as public error detail.

<a id="api-013"></a>
## API-013 — Command responses return authoritative identity/revision, not assumed projection freshness

Successful command results include enough stable identity and resulting authoritative revision/Version/lifecycle information for safe continuation and reconciliation.

The response does not claim that asynchronously maintained dashboards/search/read projections have already caught up to the committed command.

<a id="api-014"></a>
## API-014 — Public API DTOs remain separate from internal module/domain models

Transport contracts are versioned application interfaces rather than serialized ORM/domain objects. Additive compatible evolution is preferred; breaking external behavior/schema changes require an explicit contract/version transition or coordinated client migration.

This keeps framework/API evolution from silently redefining module or product semantics.

<a id="api-015"></a>
## API-015 — Cookie-authenticated mutations require deliberate request-forgery protection

State-changing browser requests protected by first-party cookie sessions include a CSRF defense appropriate to the final origin/SameSite/deployment topology. CSRF mechanics are transport/security infrastructure and do not replace `AUTH-*` authorization.

Client-provided actor/role fields, idempotency keys, correlation IDs, and concurrency tokens are not authentication credentials.

# Command envelope

A command conceptually carries:

```text
command intent
target/scope stable ID(s)
payload
server-derived Identity + Participation context
idempotency key where required
expected revision/precondition where required
request/correlation ID
reason/purpose where governed
```

# Command transaction shape

```text
BEGIN
  resolve current authoritative state
  current AUTH-* Access check
  lifecycle/resource preconditions
  idempotency + expected revision checks
  owner invariant enforcement
  authoritative state mutation
  Version / Provenance as required
  transactional outbox/change facts as required
COMMIT
return confirmed result
```

# Query posture

Cross-module dashboards, search, readiness, reconciliation queues, and similar operational reads may use projections. Immutable historical Versions and Official Outcome Revisions remain directly addressable by stable identity. Cursor-style pagination and deterministic ordering are preferred for large/volatile collections where offset pagination would create duplicate/skip hazards.

# Retry/concurrency examples

- Two devices edit Draft revision 14: the first commits revision 15; the second receives a conflict rather than overwriting it.
- A double-tap Finalize replays one committed semantic result; domain uniqueness prevents duplicate evaluation weight even if a different idempotency key is used.
- A stale Organizer dashboard says Ready: the Finalize command rechecks authoritative prerequisites and may reject.
- A commit succeeds but the response is lost: retry with the same idempotency key returns the committed result.
- A projection consumer fails after commit: the durable outbox fact retries independently; command authority remains committed and projection lag is represented honestly.

# Selected downstream mechanisms and remaining implementation detail

Concrete downstream architecture now realizes parts of this contract: [FE-001](frontend-interaction.md#fe-001) and [FE-002](frontend-interaction.md#fe-002) establish the browser framework/router boundary, while [AWS-003](aws-runtime-operations.md#aws-003) selects ECS/Fargate for the authoritative application runtime and [AWS-008](aws-runtime-operations.md#aws-008) selects SQS for retryable asynchronous work.

OpenAPI generation strategy, server-side web framework, ORM/unit-of-work library, exact route hierarchy, idempotency-key format/retention, command-specific lock SQL, CSRF mechanism, optional cache use, and optional push mechanics remain implementation choices. They must preserve the `API-*` command/query, authority, retry, concurrency, and uncertainty semantics defined here.
