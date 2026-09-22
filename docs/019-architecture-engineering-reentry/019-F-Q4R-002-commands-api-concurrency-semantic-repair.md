---
type: Architecture Candidate Repair
title: 019-F Q4R-002 — Historical Commands/API/Concurrency Semantic Repair
description: "Repairs the historical Commands, Queries, API, Transaction & Concurrency candidate for current Phase-019 comparison by translating the obsolete Official Outcome Revision binding to current Outcome Declaration affected/successor authority and separating reusable command/concurrency hypotheses from superseded owner references and fixed downstream runtime assumptions."
status: stable
tags: [phase-019, architecture, q4, repair, interface, commands, concurrency, retry]
sources:
  - resource: ../canonical/architecture/commands-api-concurrency.md
  - resource: ../canonical/concepts/outcome-declaration.md
  - resource: ../canonical/synchronizations/evaluation-outcome-finalization-declaration.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: ../canonical/synchronizations/application-action-surface-composition.md
  - resource: ../canonical/architecture/application-ownership-boundaries.md
  - resource: ../canonical/architecture/persistence-history-recovery.md
  - resource: ../canonical/architecture/identity-access-authority.md
  - resource: ../canonical/governance/architecture-decision-authority.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T09:42:00-05:00 }
---

# Purpose

Complete Q4R-002 before the historical Commands/API/Concurrency candidate participates in ADQ-005 comparison.

The historical source remains unchanged.

This record repairs the obsolete outcome-authority binding and defines the exact candidate hypothesis that may be compared under current DRV/BND/PST/IAM authority.

# Candidate

> docs/canonical/architecture/commands-api-concurrency.md

Qualification:

~~~text
Q1 / Q2 / Q4
QUALIFIED_AFTER_REVISION
authority = suspended-candidate
comparison eligible before repair = false
~~~

# Stale binding — Official Outcome Revision

The historical query posture refers to stable access to "Official Outcome Revisions."

That mechanism is no longer a current semantic owner.

Current translation:

~~~text
initial official authority
  → OutcomeDeclaration.declare

material dependency correction
  → OutcomeDeclaration.identifyAffected

explicit corrected official authority
  → OutcomeDeclaration.confirmSuccessor

history
  → stable predecessor/successor Outcome Declaration identities
~~~

Current query/history contracts therefore expose:

- current Outcome Declaration;
- Affected state;
- predecessor/successor declaration lineage;
- immutable declaration basis/history;

rather than a separate Official Outcome Revision resource/owner.

# Current owner translation

Historical candidate references to ARCH-*, MOD-*, DATA-* and AUTH-* rules remain provenance to the old architecture stack.

For comparison, their current equivalents are:

~~~text
ARCH-* driver assumptions
  → DRV-*

MOD-* module ownership
  → BND-*

DATA-* persistence/currentness/outbox
  → PST-*

AUTH-* authentication/access/session
  → IAM-*
~~~

This mapping does not reactivate those historical stable IDs.

# Retained comparison hypotheses

The following historical ideas survive repair and may be evaluated:

1. commands and queries are distinct application contracts;
2. consequential semantic transitions use explicit intent contracts rather than generic record mutation;
3. transport adapters do not own domain authority;
4. confirmed command success follows authoritative commit, not request acceptance;
5. ordinary single-owner commands use the natural owner's transaction boundary;
6. narrow cross-module atomic transactions are legitimate while the accepted modular monolith shares one authority database;
7. optimistic concurrency/current-state preconditions are the default stale-write defense;
8. stronger locking/isolation is targeted rather than global;
9. retryable consequential commands need durable idempotency/convergence semantics;
10. a lost response is reconciled against authoritative state rather than treated as failure;
11. read projections may be stale and remain non-authoritative;
12. public results distinguish validation, authorization, conflict, replay, infrastructure failure and unknown outcome;
13. transport DTOs remain separate from persistence/internal models;
14. cookie-session mutations require request-forgery protection appropriate to final origin/runtime topology.

# Revalidated rather than inherited defaults

The following historical choices are not carried into comparison as already accepted facts:

- HTTPS/JSON as the external contract;
- exact use of HTTP verbs/routes;
- GraphQL/gRPC exclusion;
- READ COMMITTED as a fixed database isolation default;
- exact revision-token representation;
- exact idempotency-key format or retention period;
- exact CSRF mechanism;
- OpenAPI tooling;
- web framework;
- ORM/unit-of-work library;
- ECS/Fargate, SQS or any provider/runtime mechanism.

ADQ-005 must independently decide the architectural contract level that is justified now.

# Revised comparison statement

The historical candidate may now be compared as this repaired hypothesis:

> **Use explicit synchronous request/response command-query contracts for ordinary authoritative application work; commit authoritative commands transactionally at their natural owner or a narrowly justified atomic coordinator boundary; protect stale intent with current-state/revision preconditions and targeted locking; converge retries through durable logical-operation/idempotency records plus domain uniqueness; reconcile lost responses against committed authority; permit non-authoritative projection reads with explicit freshness; and reserve asynchronous command completion for semantically separable long-running work rather than wrapping every domain action in a job model.**

# Current semantic preservation evidence

The repaired hypothesis is grounded in:

- one logical evaluation per Evaluation Obligation;
- truthful authority under uncertainty;
- current-versus-historical truth;
- current application action/chaining rules;
- explicit official closeout composition;
- BND-004/005/006/008;
- PST-002/003/009/011/016;
- IAM-005/006/007;
- ENG-005/007/009/014/015/017.

# Repair decision

**Q4R-002 — COMPLETE.**

~~~text
historical source rewritten        NO
current semantic translation       YES
comparison eligible                YES
candidate adopted                  NO
~~~

This repair establishes comparison eligibility only.
