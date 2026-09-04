---
type: Design Phase Record
title: 005-E — Commands, Queries, API Contracts, Transactions, Idempotency & Concurrency Architecture
description: Architecture decisions for MUDAC request boundaries, HTTP/JSON contracts, authoritative transactions, retry/idempotency, concurrency control, cross-module coordination, and projection-aware queries.
status: stable
tags: [phase-005, architecture, api, commands, queries, transactions, idempotency, concurrency]
sources:
  - resource: ../canonical/architecture/architectural-foundation.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/architecture/data-persistence.md
  - resource: ../canonical/architecture/identity-access-session.md
  - resource: ../canonical/concepts/scorecard.md
  - resource: ../canonical/concepts/competition.md
  - resource: ../canonical/invariants/truthful-authority-under-uncertainty.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T04:42:00Z }
---

# 005-E — Commands, Queries, API Contracts, Transactions, Idempotency & Concurrency Architecture

Status: **Complete**

## Purpose

Define how authenticated MUDAC requests read current/projection state and perform authoritative state transitions without allowing transport conventions, stale projections, retry behavior, or concurrent event-day activity to weaken semantic authority.

005-E builds on:

- `ARCH-*` authoritative-boundary and failure semantics;
- `MOD-*` module ownership and coordination;
- `DATA-*` PostgreSQL-compatible persistence, Version/Provenance, projections, and transactional outbox;
- `AUTH-*` current-context authorization and first-party sessions.

It does not choose a web framework, ORM, database driver, queue/broker, or AWS gateway/runtime product.

## Decision summary

MUDAC uses a first-party **HTTPS/JSON application API** with two deliberately different interaction classes:

1. **Queries** — side-effect-free reads, frequently served from current authoritative module state or explicitly non-authoritative projections.
2. **Commands** — explicit intent-bearing mutations executed by the owning module or application coordinator under one authoritative transaction boundary.

Resource-shaped CRUD may be used where the domain action is genuinely ordinary editing, but high-consequence semantic transitions are explicit commands such as `finalizeScorecard`, `completeEvent`, `invalidateEncounter`, `acceptCoverageException`, `finalizeCompetition`, and `publishExport` rather than being hidden behind generic record updates.

## Alternatives considered

### Generic CRUD-only REST

Rejected as the sole command model. Generic `PATCH status=finalized` obscures semantic preconditions, authorization, Provenance, idempotency, and high-consequence intent.

### GraphQL as primary API

Deferred/rejected for the primary authoritative browser boundary. GraphQL could improve some composed read experiences, but projection/query composition already supplies read flexibility and GraphQL does not simplify MUDAC's explicit command authority/concurrency semantics enough to justify another schema/runtime layer now.

### gRPC as primary client API

Rejected for the initial browser application. It may later be useful behind an extracted service boundary, but does not fit the current modular-monolith/browser posture as cleanly as HTTP/JSON.

### Last-write-wins mutation

Rejected. It can silently erase newer Draft work, structural changes, or lifecycle transitions.

### Pessimistic locking everywhere

Rejected. It increases contention and failure coupling unnecessarily for a bounded application where most edits can safely use optimistic concurrency.

### Serializable isolation everywhere

Rejected. Stronger isolation is valuable for narrow invariant-sensitive workflows but should not become an application-wide performance/operability tax without need.

## Request boundary

The normal request path is:

```text
browser / client
      ↓ HTTPS + first-party session
transport adapter
      ↓ typed command/query request
application/module boundary
      ↓ AUTH-* current-context Access
      ↓ current authoritative preconditions
      ↓ concurrency/idempotency controls
owning transaction
      ↓ state + Version + Provenance + outbox
COMMIT
      ↓
confirmed command result
```

A transport adapter maps HTTP/JSON into application contracts; it does not own product invariants.

## Query architecture

Queries are side-effect free from the client's semantic perspective.

A query may read:

- authoritative module state when freshness/ownership requires it;
- projection/read models for cross-module dashboards, search, readiness, reconciliation queues, and reporting;
- an immutable historical Version or Official Outcome Revision by stable ID.

Projection-backed responses must expose enough freshness/basis information for UX to distinguish current-enough, stale, rebuilding, failed, or uncertain state where that distinction matters.

A query response never grants later command authority. The command independently revalidates current state.

## Command architecture

Commands express semantic intent and route to one primary owner under `MOD-002`.

A command envelope conceptually carries:

```text
command type
stable target identity / scope
command payload
current Identity + Participation context (server-derived)
idempotency key when retryable externally
expected revision/version/precondition token when applicable
request/correlation identifier
optional reason/purpose for governed actions
```

The server derives authenticated actor/session context; clients do not self-assert Judge authorship, Organizer authority, or elevated role claims.

## HTTP/JSON posture

The initial API uses versioned HTTPS/JSON application contracts.

Preferred shape:

- `GET` for side-effect-free resource/query retrieval;
- ordinary `POST`/`PUT`/`PATCH` only where semantics are genuinely simple and explicit;
- explicit `POST` command/action resources for high-consequence transitions;
- stable opaque resource IDs in URLs/payloads;
- normalized machine-readable error/result envelopes;
- schema validation at the transport/application boundary.

Exact route naming and framework annotations remain implementation details.

## Transaction model

### Single-module command

The default authoritative command executes inside one owning database transaction:

```text
BEGIN
resolve current state
re-evaluate Access/resource preconditions
check idempotency / expected revision
apply owner invariants
write current state
write Version/Provenance if applicable
write outbox/change facts if applicable
COMMIT
```

The command reports confirmed success only after commit.

### Cross-module high-consequence workflow

Because the initial modular monolith uses one authority database, an application coordinator may deliberately open one transaction and invoke multiple module public contracts when the user-visible transition must be atomic across module-owned state.

Examples may include Competition Finalization together with creation/activation of the corresponding Official Outcome Revision.

This does **not** permit direct cross-module repository/table mutation. Each module still owns its checks and writes.

Cross-module atomicity is used narrowly. Work that need not be atomically authoritative propagates through committed facts/outbox and converges asynchronously.

A later service extraction must revisit such transaction seams explicitly rather than pretending the original database transaction still exists across a network.

## Concurrency model

### Default — optimistic concurrency

Mutable authoritative roots expose/store a monotonic revision/concurrency token. Commands that depend on a previously observed mutable state send or derive an expected revision/precondition.

If the current revision differs, the command fails with a conflict/precondition result rather than overwriting newer state.

This is especially important for Scorecard Draft edits, Competition configuration, Panel/Encounter administration, reconciliation, and other human-edited state.

### Database constraints

Uniqueness/check constraints remain the final structural guard for invariants expressible at storage level, including one logical Scorecard per Judge Participation × Encounter.

### Targeted pessimistic locking

`SELECT ... FOR UPDATE`-style row locking or an equivalent narrow lock may be used inside commands where concurrent transitions on the same authoritative root would otherwise race or where contention is known to be high.

Locks are scoped narrowly and held only for the authoritative transaction.

### Stronger transaction isolation

`READ COMMITTED` is the baseline relational isolation expectation, combined with explicit revision checks, constraints, and targeted locks.

A command/workflow may use stronger isolation such as `SERIALIZABLE` when correctness depends on a multi-row/predicate invariant that cannot be protected more simply and safely. Such elevation is command-specific, observable, retry-aware, and not the global default.

## Idempotency and retry

Externally retriable state-changing commands that could create duplicate semantic effect use an idempotency key scoped to the authenticated principal/Participation and command boundary as appropriate.

The idempotency record stores enough information to distinguish:

- first execution in progress;
- committed success and its canonical result/resource identity;
- deterministic rejected result where replay semantics make that useful;
- key reuse with a materially different payload, which is rejected.

Idempotency retention lasts at least through the relevant retry/recovery horizon; exact duration is an operational configuration decision.

Idempotency complements rather than replaces domain uniqueness. A retry with a new idempotency key must still converge safely through logical identity constraints such as `INV-002`.

## Lost-response recovery

If commit succeeds but the network response is lost:

```text
client sees uncertain outcome
      ↓
retry same command + idempotency key
      ↓
server returns prior committed result
```

The application must not instruct the user to repeat a high-consequence action blindly without a way to determine whether the original command committed.

For commands without an idempotency key, stable resource/query endpoints must still allow the client to reconcile current authority before retrying.

## Result and error semantics

Transport status codes are useful but not sufficient. Application results distinguish at least:

- **confirmed success** — authoritative transaction committed;
- **validation/precondition failure** — request invalid for current domain state;
- **authorization denial** — current Access does not permit the action/disclosure;
- **not found / concealed** — resource unavailable under appropriate disclosure semantics;
- **concurrency conflict** — observed revision/preconditions are stale;
- **idempotent replay** — prior equivalent command result returned;
- **idempotency misuse** — key reused for a materially different command;
- **temporary infrastructure failure** — no confirmed application result;
- **uncertain outcome** — client cannot know from the failed exchange whether authority committed and must reconcile/retry safely.

Internal implementation details, sensitive authorization rationale, database errors, and stack traces are not exposed as public API detail.

## Command response posture

A successful command response returns enough authoritative result metadata for the client to continue safely, typically including:

- command/request ID;
- target stable resource ID;
- resulting authoritative revision/Version ID where relevant;
- authoritative lifecycle/result state;
- whether the response was an idempotent replay where operationally useful;
- links/identifiers for subsequent queries.

The response should not pretend asynchronously updated projections are already current. Projection freshness may lag behind the committed command.

## Pagination and read consistency

Collection queries use stable deterministic ordering and cursor-style pagination where scale/volatility warrants it rather than offset semantics that can easily duplicate/skip changing event-day results.

A multi-page projection query is not automatically a consistent historical snapshot unless the endpoint explicitly promises such semantics.

## API evolution

The application API is versioned as a contract. Additive compatible changes are preferred. Breaking behavior/schema changes require an explicit new API contract/version or coordinated client migration.

Internal module interfaces remain separate from public HTTP DTOs so transport evolution does not become domain-object evolution.

## Security consequences

- CSRF protection is required for cookie-authenticated state-changing browser requests; exact mechanism remains implementation-specific but must align with the chosen SameSite/deployment topology.
- authorization executes server-side at protected application/module boundaries under `AUTH-004`.
- client-provided actor/role fields are treated as request data at most, never authentication authority.
- sensitive fields are purpose-filtered in queries/DTOs under `ARCH-007`.
- replay/idempotency identifiers are non-secret correlation controls, not credentials.

## Observability consequences

Commands and asynchronous consequences carry correlation/causation identifiers across request, transaction, Provenance, outbox dispatch, and projection processing where practical.

Logging/telemetry must allow operators to answer:

- did this command reach the authoritative boundary?;
- did it commit?;
- what resource/revision resulted?;
- was it an idempotent replay?;
- did outbox/projection processing lag or fail?;

without logging private Judge content or credentials unnecessarily.

## Failure scenarios reviewed

### Double-tap Scorecard Finalize

Same idempotency key returns one committed Version. Even a different key cannot create a second logical Scorecard vote because owner invariants/uniqueness still apply.

### Two devices edit one Draft

Both begin from revision 14. Device A commits revision 15; device B's later command expecting 14 receives a conflict rather than silently overwriting A.

### Organizer acts from stale dashboard

The dashboard may say Ranking Ready. `finalizeCompetition` re-reads current authoritative prerequisites in its transaction and rejects if newer evidence invalidated readiness.

### Commit succeeds; response is lost

Retry with the same idempotency key returns the committed result rather than performing the transition twice.

### Projection update fails after authoritative commit

The transactionally written outbox/change fact remains available for retry. Command authority remains committed; query responses expose projection lag rather than rolling back truth implicitly.

### Concurrent high-consequence closeout

The command uses current preconditions plus revision/lock/isolation strategy appropriate to the invariant. Only one authoritative successor transition may commit; competing attempts receive deterministic conflict/replay results.

## Deliberate deferrals

005-E does not yet select:

- web framework/router;
- OpenAPI code-generation tooling;
- exact route hierarchy;
- exact UUID/idempotency-key format;
- ORM/unit-of-work library;
- exact lock SQL for each command;
- Redis or other session/idempotency acceleration;
- queue/broker;
- WebSocket/SSE transport;
- offline Draft synchronization protocol;
- API gateway/WAF/runtime service.

005-F will use this command/concurrency contract to define disconnected Draft persistence, synchronization, conflict recovery, and safe degraded operation.
