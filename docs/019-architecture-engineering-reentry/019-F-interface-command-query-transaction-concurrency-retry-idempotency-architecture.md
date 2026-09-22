---
type: Architecture Decision
title: 019-F — Interface, Command/Query, Transaction, Concurrency, Retry & Idempotency Architecture
description: "Resolves ADQ-005 after Q4R-002 repair by comparing broad CRUD/resource mutation, queue-first asynchronous command handling, globally strong-locking transactions, and explicit synchronous command-query contracts with optimistic concurrency, durable operation idempotency and narrow atomic coordination; accepts the latter while preserving truthful partial/unknown outcomes."
status: stable
tags: [phase-019, architecture, adq-005, interface, commands, queries, transactions, concurrency, retry, idempotency]
sources:
  - resource: ../canonical/architecture/interface-command-concurrency.md
  - resource: ../canonical/architecture/commands-api-concurrency.md
  - resource: 019-F-Q4R-002-commands-api-concurrency-semantic-repair.md
  - resource: ../canonical/architecture/architecture-drivers.md
  - resource: ../canonical/architecture/application-ownership-boundaries.md
  - resource: ../canonical/architecture/persistence-history-recovery.md
  - resource: ../canonical/architecture/identity-access-authority.md
  - resource: ../canonical/synchronizations/application-action-surface-composition.md
  - resource: ../canonical/synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../canonical/synchronizations/evaluation-outcome-finalization-declaration.md
  - resource: ../canonical/experience/status-feedback-recovery.md
  - resource: ../canonical/invariants/one-logical-scorecard.md
  - resource: ../canonical/invariants/current-vs-historical-truth.md
  - resource: ../canonical/invariants/truthful-authority-under-uncertainty.md
  - resource: ../routing/phase019_architecture_decision_control.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T10:04:00-05:00 }
---

# Purpose

019-F resolves ADQ-005.

It first repairs the obsolete Outcome Revision binding in the historical Commands/API/Concurrency candidate, then decides how MUDAC receives intent, reads state, establishes authoritative transactions, handles stale concurrent intent, converges retries, reports partial results and preserves unknown outcomes.

# 1. Entry state

~~~text
Phase 019                       ACTIVE
019-A/B/C/D/E                   COMPLETE
019-F                           NEXT ELIGIBLE / USER AUTHORIZED

ADQ-001..004                    ACCEPTED
ADQ-005                         PLANNED
ADQ-006..010                    PLANNED

Q4R-001                         COMPLETE
Q4R-002                         REQUIRED
Q4 repairs complete             1 / 4
technical probes                0

accepted whole architecture     false
implementation packages         0
implementation execution        false
~~~

# 2. Q4 prerequisite

019-F completed:

> **Q4R-002 — Historical Commands/API/Concurrency Semantic Repair**

The repair translates:

~~~text
Official Outcome Revision
  → current Outcome Declaration
  + Affected state
  + predecessor/successor declaration history
  + explicit confirmSuccessor authority
~~~

It also prevents old ARCH/MOD/DATA/AUTH references and provider/runtime selections from participating as current authority.

The historical candidate remains unchanged.

# 3. Decision

**ADQ-005 — ACCEPTED.**

Selected architecture:

> **Versioned HTTPS/JSON command-query request/response boundary; explicit semantic commands and side-effect-free queries; synchronously commit-confirmed authoritative transitions by default; natural-owner transactions plus narrowly justified atomic cross-module coordination; optimistic concurrency/current-state preconditions; durable logical-operation idempotency plus domain uniqueness; truthful lost-response reconciliation; per-item partial bulk results; and asynchronous completion only for semantically separable long-running work.**

Current owner:

> docs/canonical/architecture/interface-command-concurrency.md

Stable rules:

> CMD-001 through CMD-022

# 4. Current constraints

ADQ-005 preserves:

- ENG-005 — high-consequence actions remain explicit and traceable;
- ENG-007 — concurrency/retry/current-state handling preserves authority;
- ENG-009 — calculated/official distinctions remain explicit;
- ENG-014 — Phase-016 scenario families survive downstream;
- ENG-015 — evidence strength matches claims;
- ENG-017 — historical architecture remains evidence;
- INV-002 — one logical evaluation per Evaluation Obligation;
- INV-003 — finalization does not create additional evaluation weight;
- INV-005 — current and historical truth remain distinct;
- INV-010 — unknown is not promoted to success/failure;
- DRV-001/002/003/005/007/010/011;
- BND-004/005/006/008/011/012;
- PST-002/003/009/011/016;
- IAM-005/006/007/017.

# 5. Historical candidate qualification

Input:

> docs/canonical/architecture/commands-api-concurrency.md

After Q4R-002:

~~~text
Q1 / Q2 / Q4
QUALIFIED_AFTER_REVISION
semantic repair complete       yes
comparison eligible            yes
historical authority           suspended
technology/runtime choices     require fresh selection
~~~

Useful retained hypotheses include:

- command/query separation;
- explicit semantic commands;
- commit-confirmed authority;
- owner transaction boundaries;
- narrow cross-module atomicity;
- optimistic concurrency;
- durable retry idempotency;
- lost-response reconciliation;
- projection non-authority;
- semantically typed results;
- transport/domain DTO separation.

# 6. Alternatives

## Alternative A — Adopt repaired historical Commands/API/Concurrency design unchanged

Strengths:

- strong retry/currentness reasoning;
- explicit command-query semantics;
- mature idempotency and transaction concepts.

Weaknesses:

- includes fixed historical defaults such as specific isolation language;
- embeds obsolete/currently unselected downstream runtime references;
- current BND/PST/IAM decisions alter the authority chain;
- historical chronology still cannot establish current authority.

**Rejected as-is.**

Its strongest ideas are re-established under CMD-*.

## Alternative B — Broad resource-oriented CRUD interface

Pattern:

~~~text
GET/POST/PATCH/DELETE resource representations
  → generic service/repository mutation
~~~

Strengths:

- simple mental model;
- common tooling;
- lower contract count for basic edits.

Weaknesses:

- high-consequence semantic transitions become hidden inside generic mutation;
- weak operation identity for lost-response reconciliation;
- easier to confuse Draft persistence with Finalization;
- poor fit for coordinated actions such as closeout/correction;
- encourages client-provided state rather than current owner preconditions.

**Rejected as primary authority model.**

Resource-oriented simple edits remain permissible where they are genuinely simple, but consequential transitions use explicit commands.

## Alternative C — Queue/job-first asynchronous command architecture

All state-changing intent becomes queued work and returns an accepted/job identifier.

Strengths:

- natural load smoothing;
- easy worker scaling;
- resilient background retry.

Weaknesses:

- ordinary event-day authority becomes unnecessarily indirect;
- accepted request can be confused with semantic success;
- introduces generic job/workflow state across actions that are currently local/transactional;
- complicates Judge feedback and unknown-result handling;
- current bounded workload does not justify queueing every authoritative transition.

**Rejected as baseline.**

Asynchronous completion remains allowed only where semantics/workload justify it.

## Alternative D — Globally strong-locking/serializable transaction posture

Use pessimistic locking or strongest isolation broadly.

Strengths:

- straightforward conceptual serial ordering;
- fewer stale-write classes if implemented correctly.

Weaknesses:

- unnecessary contention/operational complexity for ordinary Draft/current-state changes;
- does not replace semantic idempotency/lost-response reconciliation;
- broad locking can harm live-event responsiveness;
- stronger isolation is warranted only for demonstrated invariants.

**Rejected as global default.**

Targeted locks/isolation remain available.

## Alternative E — Explicit synchronous command/query contracts + optimistic concurrency + durable idempotency

Characteristics:

- versioned HTTPS/JSON request/response boundary;
- explicit high-consequence commands;
- current IAM + owner validation at execution;
- natural-owner transactions;
- narrow atomic coordinator transactions where semantics require;
- optimistic revision/current-state preconditions;
- constraints/targeted locks where needed;
- durable logical-operation idempotency;
- truthful unknown/lost-response reconciliation;
- non-authoritative projection queries;
- partial bulk results;
- asynchronous completion only where semantically separable.

**Selected.**

# 7. External application interface

The baseline browser contract is versioned HTTPS/JSON.

This establishes a conventional interoperable boundary without coupling internal domain or persistence objects to the wire representation.

019-F does not select:

- web framework;
- route naming convention;
- generated client;
- schema tooling;
- serialization library.

GraphQL/gRPC are not baseline authority transports, but may later be added for a demonstrated specialized need.

# 8. Command semantics

Commands represent semantic intent.

The command boundary receives, as applicable:

~~~text
command kind
stable target/scope IDs
payload
server-derived IAM context
logical operation / idempotency ID
expected revision/current-state precondition
request/correlation ID
governed reason/purpose
~~~

Client actor/capacity fields never substitute for server-derived IAM authority.

# 9. Transaction model

## Natural-owner command

Default:

~~~text
one command
  → one natural BND owner
  → one authoritative transaction
~~~

The transaction re-evaluates current Access and owner preconditions before mutation.

## Semantically indivisible coordination

A narrow application coordinator may use one database transaction across module public contracts while the accepted architecture remains a modular monolith over one logical authority database.

Current primary seam:

~~~text
Finalize Competition & Declare Outcome
  → Competition.finalize
  + OutcomeDeclaration.declare
  → one semantic success condition
~~~

Atomicity here preserves the current composition without merging owners.

## Separate legitimate actions

Correction, derived recomputation, Export replacement and Publication release remain separate when current semantics say they are separate.

Architecture does not create all-or-nothing transactions merely to avoid exposing legitimate partial progress.

# 10. Concurrency

Optimistic current-state/revision checking is the default.

A command must not overwrite newer authority merely because its caller observed an older state.

When a previously valid intent becomes stale after another commit, the result may be:

- conflict;
- no longer applicable;
- no longer authorized;
- already established/current.

Relational constraints, targeted row locks and stronger isolation supplement this where specific invariants justify them.

No exact PostgreSQL isolation level is mandated globally by 019-F.

# 11. Idempotency and logical uniqueness

019-F distinguishes:

~~~text
domain identity
logical operation identity
transport/request identity
~~~

Retrying one semantic intent retains logical operation identity even if the HTTP request/correlation identity changes.

A durable operation record or equivalent state is committed with the authoritative command where required.

Equivalent replay returns the same semantic result.

But:

~~~text
different idempotency key
  != permission to create duplicate domain authority
~~~

Domain uniqueness/current-state rules remain authoritative.

# 12. Lost-response retry

After a timeout/disconnect:

~~~text
response missing
  != command failed
~~~

Recovery first reconciles using:

- operation identity;
- current resource identity/revision/state;
- current authority.

If the original committed, replay returns/reconstructs it.

If the result cannot be established, it remains **unknown**.

# 13. Query model

Queries are side-effect-free and may consume:

- current owner state;
- immutable history;
- read projections.

Projection-backed reads preserve material freshness/basis distinctions.

A stale dashboard/read model cannot authorize a later command.

Current Outcome Declaration history replaces the obsolete Official Outcome Revision representation.

# 14. Result model

The public application contract can distinguish:

~~~text
confirmed success
validation/precondition rejection
Access denial
concealed/not-found
concurrency/current-state conflict
idempotent replay / already established
idempotency misuse
temporary infrastructure failure
result unknown / reconciliation needed
~~~

Transport statuses are mappings, not the semantic owner of these distinctions.

# 15. Bulk operations

A convenience bulk action over independent subjects is not one domain transaction.

Each item retains its own:

- authority;
- operation identity;
- concurrency state;
- semantic result.

Therefore one bulk response may legitimately contain success, rejection, conflict, unknown and not-attempted outcomes together.

This directly preserves the Phase-016 partial-bulk scenario.

# 16. Asynchronous completion boundary

The baseline is not queue-first.

Asynchronous completion is used only when:

- the domain already distinguishes request from completion; or
- long-running/external workload makes synchronous completion disproportionate.

The technical operation/receipt does not become a new semantic Workflow/Task/Case owner.

Exact queue/worker infrastructure belongs to ADQ-009.

# 17. Security interaction

Cookie-session state-changing requests require deliberate CSRF/request-origin defense appropriate to final deployment.

Idempotency keys, correlation IDs and concurrency tokens are never authentication credentials.

Current IAM Access remains independently enforced.

# 18. Evidence

Acceptance evidence class:

> **DOCUMENTATION_REASONING**

No technical probe is needed to choose the command/concurrency architecture.

Later implementation must provide executable evidence for:

- same-key replay;
- same-key/different-intent rejection;
- different-key domain duplicate prevention;
- stale revision conflict;
- lost-response reconciliation;
- cross-module atomic closeout;
- partial bulk results;
- unknown-result behavior.

# 19. Reversibility / lock-in

The decision intentionally commits to:

- HTTPS/JSON as baseline browser contract;
- explicit application command/query semantics;
- optimistic concurrency posture;
- durable operation identity for retryable commands.

It does not commit to:

- server framework;
- ORM;
- exact route layout;
- exact revision encoding;
- exact idempotency table/schema;
- exact DB isolation level;
- message broker/queue;
- managed runtime.

Future service extraction will require redesign of currently narrow cross-module atomic transactions but does not require changing command semantics.

# 20. Residual uncertainty

Open downstream questions include:

- exact route/API versioning convention;
- exact revision token encoding;
- exact idempotency-key scope/retention/privacy policy;
- exact PostgreSQL locking/isolation choices per command;
- exact CSRF mechanism;
- exact generated-client/OpenAPI approach;
- exact async operation storage/queue where needed;
- exact pagination strategy per query family;
- exact rate/abuse-control implementation.

# 21. Scenario impact

ADQ-005 directly closes architecture posture for:

- lost-response retry after consequential action;
- concurrent/repeated legitimate intent;
- partial bulk result;
- unknown/degraded result.

Executable scenario evidence remains a Phase-020/019-K validation concern as applicable.

# 22. Risk disposition

## ERI-02 — historical candidate mistaken for accepted architecture

**Controlled.**

Current authority is CMD-*; historical API-* remains candidate evidence.

## ERI-04 — stale semantic binding survives reuse

**CLOSED for Commands/API/Concurrency.**

Official Outcome Revision has been translated to current Outcome Declaration authority through Q4R-002.

## ERI-09 — coordination/derived-authority leakage

**Materially reduced; carried to 019-K.**

Natural-owner transactions, narrow coordinator atomicity, projection non-authority and explicit results now constrain realization.

## Retry/unknown-result risk

**Architecturally controlled; executable validation remains later.**

# 23. Implementation boundary

After 019-F:

~~~text
accepted bounded decisions       5 / 10
Q4 repairs complete              2 / 4
technical probes                 0

accepted whole architecture      false

implementation packages          0
package derivation               false
implementation execution         false
~~~

G0 remains unsatisfied.

# 24. Exit decision

**019-F — COMPLETE — PASS.**

**Q4R-002 — COMPLETE.**

**ADQ-005 — ACCEPTED.**

Next eligible:

> **019-G — Offline Draft, Multi-device, Degraded, Paper & Reconciliation Architecture**

019-G is not automatically authorized.
