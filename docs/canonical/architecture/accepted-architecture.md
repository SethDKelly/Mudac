---
type: Architecture Authority
title: Accepted MUDAC Architecture
description: "Whole-architecture authority accepted at Phase 019 closure. Routes to the nine normative architecture families and the ADQ-001..010 decision/validation record without duplicating their rule bodies."
status: stable
tags: [architecture, current, accepted, phase-019, authority, routing]
sources:
  - resource: architecture-drivers.md
  - resource: application-ownership-boundaries.md
  - resource: persistence-history-recovery.md
  - resource: identity-access-authority.md
  - resource: interface-command-concurrency.md
  - resource: offline-continuity-reconciliation.md
  - resource: artifact-export-publication-delivery.md
  - resource: browser-client-interaction.md
  - resource: runtime-platform-operations.md
  - resource: ../../019-architecture-engineering-reentry/019-K-whole-architecture-integration-threat-failure-recovery-performance-cost-scenario-validation.md
  - resource: ../../019-architecture-engineering-reentry/019-L-architecture-consolidation-acceptance-candidate-supersession-implementation-handoff.md
  - resource: ../../routing/phase019_architecture_decision_control.json
  - resource: ../../routing/phase019_architecture_candidate_disposition.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T19:35:00-05:00 }
---

# Authority

This document is the **current accepted whole-architecture routing authority for MUDAC**.

Phase 019 accepted the architecture after:

- ADQ-001 through ADQ-010 were accepted;
- all four Q4 repairs completed;
- whole-system integration validation passed;
- 15/15 mandatory scenarios passed;
- 10/10 cross-cutting invariants remained satisfied;
- zero cross-decision contradictions remained;
- zero blocking architecture risks remained;
- all historical architecture candidates received explicit disposition.

This document consolidates authority. It does **not** copy or replace the normative rule bodies owned by the architecture-family documents below.

# Accepted architecture families

| Family | Current owner | Scope |
|---|---|---|
| DRV-001..012 | [Architecture Drivers](architecture-drivers.md) | quality priorities, workload, trust, continuity, cost and evidence boundaries |
| BND-001..012 | [Application Ownership & Boundaries](application-ownership-boundaries.md) | modular-monolith ownership, dependency and coordination topology |
| PST-001..016 | [Persistence, History & Recovery](persistence-history-recovery.md) | relational authority, history, Provenance, projections, migration and recovery |
| IAM-001..018 | [Identity, Access & Session](identity-access-authority.md) | authentication, Identity, Participation, Access, sessions and technical authority |
| CMD-001..022 | [Interface, Command & Concurrency](interface-command-concurrency.md) | commands/queries, transactions, concurrency, retry, idempotency and reconciliation |
| RCV-001..018 | [Offline & Reconciliation](offline-continuity-reconciliation.md) | local Draft continuity, multi-device, degraded, paper and convergence semantics |
| ART-001..020 | [Artifact, Export & Publication](artifact-export-publication-delivery.md) | durable representations, disclosure, Publication, withdrawal and delivery |
| CLT-001..020 | [Browser/Client Interaction](browser-client-interaction.md) | client state, navigation, responsive/accessibility and degraded interaction |
| RUN-001..026 | [Runtime Platform & Operations](runtime-platform-operations.md) | AWS runtime, security, deployment, availability, observability, backup and DR |

Stable rule identifiers resolve to these owners through the stable-reference index.

# Accepted topology

~~~text
current semantic authority
  → ownership-preserving modular monolith
  → current contextual Access
  → validated command / natural-owner transaction
  → PostgreSQL-compatible authoritative state + history
  → bounded downstream recovery / representation work
  → non-authoritative browser interaction
  → single-active AWS runtime

reverse authority: prohibited
~~~

Provider, browser, queue, object-store, projection, telemetry and recovery mechanisms cannot become semantic owners merely because they execute or retain technical state.

# Whole-architecture validation

019-K established:

~~~text
cross-decision contradictions     0
mandatory scenario seeds          15 / 15 PASS
cross-cutting invariants          10 / 10 PASS
blocking architecture risks       0
~~~

Architecture evidence is not production evidence.

Capacity, load, failover, restore, cost, security integration, accessibility and provider behavior still require the evidence classes assigned by IPG/RUN and the implementation program.

# Accepted runtime posture

The initial production runtime is AWS:

- active Region: us-east-2;
- single-active-region authority;
- Multi-AZ production;
- CloudFront/WAF private-origin edge;
- ECS/Fargate authoritative application and bounded workers;
- RDS PostgreSQL Multi-AZ DB instance;
- Cognito User Pools behind MUDAC IAM;
- private/versioned S3;
- SQS for semantically separable async work;
- cold recovery target: us-east-1.

No contractual uptime, RTO, RPO, capacity or cost claim is created by architecture acceptance.

# Historical architecture candidates

The nine preserved Phase-018 architecture candidates are **superseded as current architecture authority and retained as historical comparison evidence**.

Their exact dispositions and replacement owners are recorded in:

> docs/routing/phase019_architecture_candidate_disposition.json

They must not be used as current authority merely because they remain under `docs/canonical/architecture/`.

# Implementation handoff

Successful 019-L satisfies:

> **G0 — Architecture Accepted**

Therefore implementation **package derivation may begin only through the Phase-020 implementation-program start gate**.

At Phase-019 closure:

~~~text
accepted architecture              true
package derivation allowed         true
active implementation packages     0
implementation execution           false
release authority                  false
production authority               false
~~~

G0 is planning authority, not execution authority.

Only G2 plus explicit human/program authorization can permit implementation execution for a specific package.

# Change boundary

A later change that contradicts accepted architecture must use architecture change/re-entry governance rather than being hidden in implementation.

Revisit triggers from the family decisions and 019-K remain binding evidence/change triggers.
