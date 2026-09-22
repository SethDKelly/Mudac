---
type: Accepted Architecture Decision
title: Current Interface, Command/Query, Transaction, Concurrency, Retry & Idempotency Architecture
description: "Accepted ADQ-005 interface architecture for MUDAC: versioned HTTPS/JSON request-response contracts, explicit semantic commands and side-effect-free queries, commit-confirmed synchronous authority by default, owner-scoped and narrowly coordinated atomic transactions, optimistic concurrency, durable logical-operation idempotency, truthful lost-response reconciliation, partial-result bulk semantics, non-authoritative projection reads and bounded asynchronous completion."
status: stable
tags: [architecture, current, interface, api, commands, queries, transactions, concurrency, retries, idempotency]
sources:
  - resource: architecture-drivers.md
  - resource: application-ownership-boundaries.md
  - resource: persistence-history-recovery.md
  - resource: identity-access-authority.md
  - resource: commands-api-concurrency.md
  - resource: ../synchronizations/application-action-surface-composition.md
  - resource: ../synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../synchronizations/evaluation-outcome-finalization-declaration.md
  - resource: ../experience/status-feedback-recovery.md
  - resource: ../invariants/one-logical-scorecard.md
  - resource: ../invariants/current-vs-historical-truth.md
  - resource: ../invariants/truthful-authority-under-uncertainty.md
  - resource: ../governance/downstream-realization-obligations.md
  - resource: ../../019-architecture-engineering-reentry/019-F-Q4R-002-commands-api-concurrency-semantic-repair.md
  - resource: ../../019-architecture-engineering-reentry/019-F-interface-command-query-transaction-concurrency-retry-idempotency-architecture.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T09:55:00-05:00 }
---

# Authority

This document is **current accepted architecture authority for ADQ-005**.

It establishes application interface, command/query, transaction, concurrency, retry, idempotency, result and partial-bulk semantics.

It does not select the server framework, ORM/unit-of-work library, generated-client tool, exact route hierarchy, exact PostgreSQL isolation level, queue/broker, CSRF implementation, or transport serialization library.

<a id="cmd-001"></a>
## CMD-001 — Commands and queries are distinct application contracts

Queries are side-effect-free application reads.

Commands express semantic intent to change authoritative state and route to:

- one natural module owner; or
- one explicit application coordinator for a current composed action.

Consequential transitions use owner-qualified intent rather than generic record mutation.

Examples include:

- Finalize Evaluation;
- invalidate evidence/occurrence;
- Finalize Competition & Declare Outcome;
- confirm successor Outcome Declaration;
- publish/withdraw/supersede Publication.

<a id="cmd-002"></a>
## CMD-002 — The baseline browser application interface is versioned HTTPS/JSON request-response

The core browser-facing application boundary uses HTTPS request/response contracts with JSON payloads.

The application contract is versioned independently of internal domain/persistence types.

This selects the baseline external interface family, not:

- an exact web framework;
- exact URL layout;
- generated-client tooling;
- GraphQL/gRPC for every use case.

A later specialized interface may be added for a demonstrated need without changing current command/query semantics.

<a id="cmd-003"></a>
## CMD-003 — Transport adapters translate intent; they do not own authorization or domain state

Routes, handlers, serializers, DTOs and middleware translate external requests into application contracts.

They do not:

- mutate persistence directly;
- trust client-supplied actor/capacity as authority;
- infer current Access from UI visibility;
- own domain invariants.

Current IAM context and natural-owner preconditions are evaluated inside protected application/module boundaries.

<a id="cmd-004"></a>
## CMD-004 — Confirmed command success requires authoritative commit

For commands that establish authoritative state, success is confirmed only after the required authoritative transaction commits.

Request receipt, validation start, queue acceptance or optimistic UI state is not authoritative success.

Where required by the command, the commit includes in one durable boundary:

- authoritative owner mutation;
- Version/Provenance;
- logical-operation/idempotency record;
- durable change/outbox intent.

<a id="cmd-005"></a>
## CMD-005 — Ordinary state-changing commands use the natural owner's transaction boundary

The default command transaction is owned by one BND module.

Conceptually:

~~~text
resolve current authority
  → evaluate current IAM Access
  → evaluate owner lifecycle/resource preconditions
  → idempotency / stale-intent checks
  → enforce owner invariants
  → persist owner state + history/provenance
  → record durable propagation intent if required
  → commit
~~~

Storage co-location does not permit bypassing public module contracts.

<a id="cmd-006"></a>
## CMD-006 — Semantically indivisible composed actions may use a narrow cross-module atomic transaction

Because the accepted initial architecture is a modular monolith over one logical authority database, an application coordinator may deliberately use one database transaction across module public contracts when current semantics define one user-visible transition whose success requires all participating postconditions.

Primary current example:

~~~text
Finalize Competition & Declare Outcome
  = Competition.finalize
  + OutcomeDeclaration.declare
~~~

Semantic success requires both.

The coordinator owns transaction/orchestration mechanics only.

It does not mutate another module's storage directly or acquire semantic ownership.

If future service extraction removes shared atomicity, that seam must be explicitly redesigned before extraction.

<a id="cmd-007"></a>
## CMD-007 — Cross-owner work is not made atomic merely for convenience

Separate legitimate owner actions remain separate transactions unless current semantics require all-or-nothing establishment.

Examples include:

- source correction versus later Export regeneration;
- Outcome Declaration correction versus Publication successor release;
- derived recomputation versus Award correction;
- bulk actions over independent subjects.

Avoiding partial result handling is not sufficient reason to create a large transaction.

<a id="cmd-008"></a>
## CMD-008 — Optimistic concurrency is the default stale-intent defense

Mutable authoritative roots expose or internally maintain a monotonic revision/current-state precondition suitable for concurrency control.

Commands whose correctness depends on previously observed state must provide or derive an expected current-state condition.

If current authority has changed incompatibly, the command returns a concurrency/current-state conflict rather than silently overwriting newer authority.

The exact revision encoding is implementation detail.

<a id="cmd-009"></a>
## CMD-009 — Constraints, targeted locking and stronger isolation supplement optimistic concurrency

Optimistic revision checks are not the only integrity mechanism.

Use, as appropriate:

- relational uniqueness/check constraints;
- targeted row locks for same-root transition races;
- stronger transaction isolation for demonstrated multi-row/predicate invariants.

Stronger locking/isolation is command-specific and evidence-driven, not a system-wide default selected by 019-F.

Exact SQL/isolation configuration remains downstream detail.

<a id="cmd-010"></a>
## CMD-010 — Logical operation identity is distinct from request correlation and domain identity

Retry-safe commands distinguish:

- **domain resource identity** — what product object is affected;
- **logical operation/idempotency identity** — which semantic intent is being retried;
- **request/correlation identity** — one transport attempt/trace.

These identifiers must not be conflated.

A retry may have a new request/correlation ID while retaining the same logical operation identity.

<a id="cmd-011"></a>
## CMD-011 — Consequential externally retryable commands use durable idempotency

Commands vulnerable to double-click, reconnect, client retry or lost response carry a logical operation/idempotency key or equivalent stable operation identity.

The authoritative boundary durably records enough information to establish:

- command family/scope;
- authenticated application context where relevant;
- normalized intent fingerprint;
- completion/result identity;
- resulting authoritative revision/reference.

Equivalent replay converges on the same committed semantic result.

Reusing the same operation identity for materially different intent is rejected.

<a id="cmd-012"></a>
## CMD-012 — Idempotency supplements domain uniqueness; it does not replace it

A different idempotency key must not create duplicate semantic authority that the domain forbids.

Natural invariants remain the ultimate backstop, including:

- one logical Scorecard per Evaluation Obligation;
- one qualifying evaluation weight;
- one ordinary initial Outcome Declaration per closeout scope;
- explicit predecessor/successor declaration history;
- explicit Publication successor identity.

Idempotency protects retry intent; domain constraints protect product truth.

<a id="cmd-013"></a>
## CMD-013 — Concurrent/repeated legitimate intent may resolve to one success and one current-state result

Two actors may each be legitimately authorized when they begin.

Authorization at intent time does not guarantee both intents remain valid after the first commit changes current state.

The second execution may therefore:

- replay the same logical result;
- report already established/current state;
- return a concurrency/precondition conflict;
- become unauthorized/inapplicable under newly current facts.

It must not manufacture duplicate authority merely because both requests were initially legitimate.

<a id="cmd-014"></a>
## CMD-014 — Lost responses reconcile against committed authority before blind repetition

A transport timeout or disconnect is not proof of command failure.

Recovery checks, as applicable:

- durable logical-operation record;
- stable resource identity/current revision;
- current semantic state.

If a prior attempt committed, retry returns/reconstructs the committed result.

If the result cannot yet be established, the client-visible state remains **unknown** rather than being converted to failure or success.

<a id="cmd-015"></a>
## CMD-015 — Public result contracts distinguish semantic outcome classes

Application interfaces preserve meaningful distinctions such as:

- confirmed success;
- validation/precondition rejection;
- Access denial;
- concealed/not-found result where disclosure requires it;
- concurrency/current-state conflict;
- idempotent replay/already-established result;
- idempotency misuse;
- temporary infrastructure failure before known commit;
- result unknown / reconciliation required.

HTTP status codes may map to these classes but do not define their semantic meaning.

Sensitive internal/security details are not exposed merely to improve error specificity.

<a id="cmd-016"></a>
## CMD-016 — Successful command responses return authoritative result identity/currentness, not projection promises

A successful authoritative command returns enough information for safe continuation, such as applicable:

- stable resource identity;
- resulting revision;
- authoritative Version/reference;
- owner-qualified lifecycle/currentness state;
- logical operation identity.

The response does not imply asynchronously maintained projections, dashboards or search views have already caught up.

<a id="cmd-017"></a>
## CMD-017 — Queries may read owner state or projections, with material freshness/basis explicit

Queries are side-effect-free.

They may read:

- current authoritative owner state;
- immutable history;
- non-authoritative read projections.

Projection-backed reads expose material freshness/basis state where needed to distinguish current-enough, stale, rebuilding, failed or uncertain data.

High-consequence commands independently revalidate current authority.

Historical Outcome Declaration history uses current predecessor/successor declaration identity, not the obsolete Official Outcome Revision mechanism.

<a id="cmd-018"></a>
## CMD-018 — Bulk convenience does not create one giant semantic transaction

When a user requests the same legitimate action over independent subjects, the interface may offer a bulk convenience contract.

Unless current semantics require all-or-nothing behavior, each item preserves its own command identity, authorization, preconditions and result.

A bulk result may therefore contain:

~~~text
confirmed success
confirmed rejection/failure
concurrency conflict
result unknown
not attempted / pending
~~~

The bulk wrapper is a convenience/result aggregation mechanism, not a new domain authority owner.

<a id="cmd-019"></a>
## CMD-019 — Asynchronous completion is reserved for semantically separable long-running work

Ordinary authoritative state transitions are synchronously commit-confirmed where proportionate.

Asynchronous handling is appropriate when current semantics already distinguish the initiating request from later completion, or when runtime workload genuinely requires separation.

Examples may include later Export generation or external delivery work.

An asynchronous technical operation receipt:

- does not become a Workflow/Task/Case Concept;
- does not imply the downstream semantic action succeeded;
- must preserve durable linkage to the initiating authoritative intent/state.

Exact queue/worker/runtime mechanism remains ADQ-009.

<a id="cmd-020"></a>
## CMD-020 — Cookie-session mutations require deliberate request-forgery and replay protection

State-changing browser requests under IAM first-party cookie sessions use a CSRF/request-origin defense appropriate to the eventual origin/deployment topology.

CSRF, correlation IDs, concurrency tokens and idempotency keys are not authentication credentials.

The exact defense mechanism is deferred to runtime/implementation detail.

<a id="cmd-021"></a>
## CMD-021 — Interface DTOs are application contracts, not serialized persistence/domain internals

Request/response contracts remain separate from:

- PostgreSQL schema;
- ORM models;
- internal module objects;
- projection storage layout.

Additive compatible evolution is preferred.

Breaking externally consumed contract changes require explicit version transition or coordinated client migration.

<a id="cmd-022"></a>
## CMD-022 — Client reconciliation is a first-class interface capability

For high-consequence or retry-prone operations, the interface provides enough stable identity/currentness to answer:

> **What authoritative result exists now for the semantic intent I attempted?**

Recovery may use:

- command replay under the same logical operation identity;
- authoritative resource query;
- dedicated reconciliation/result lookup where justified.

This capability is required by truthful-uncertainty semantics; its exact route shape is not prescribed.

# Baseline interface shape

Conceptually:

~~~text
browser
  → versioned HTTPS/JSON query
  → application query contract
  → owner state or projection

browser
  → versioned HTTPS/JSON command
      + server-derived IAM context
      + stable target IDs
      + expected revision when required
      + logical operation ID when retryable
  → owner/coordinator command contract
  → authoritative transaction
  → committed semantic result
~~~

# Command confirmation posture

Ordinary authoritative commands aim for:

~~~text
request
  → transaction
  → commit
  → confirmed authoritative response
~~~

When transport fails around commit:

~~~text
request
  → commit may or may not have happened
  → response lost
  → result unknown
  → reconcile by operation/resource identity
  → confirmed current result
~~~

# Partial/bulk posture

Independent bulk items do not inherit false all-or-nothing semantics.

The interface preserves per-item authority and uncertainty even when the UI initiated one bulk request.

# Revisit triggers

Reopen ADQ-005 when credible evidence shows:

- browser/API workload needs a different baseline transport family;
- cross-module atomic seams become incompatible with justified service extraction;
- contention makes optimistic concurrency materially inadequate;
- high-latency/long-running authoritative work requires broader asynchronous semantics;
- durable idempotency retention creates unacceptable cost/privacy constraints;
- whole-architecture validation finds unsafe retry, ambiguity, partial-result or transaction behavior.

Whole-architecture acceptance remains false until 019-L.
