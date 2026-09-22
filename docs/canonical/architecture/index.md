# Architecture

This subtree now contains both **current accepted Phase-019 architecture authority** and **preserved downstream candidate architecture**.

## Current accepted architecture authority

- [Current Architecture Drivers, Quality Priorities, Workload & Trust Boundaries](architecture-drivers.md) — **ADQ-001 ACCEPTED in 019-B; DRV-001..012 current authority.**
- [Current Application Ownership, Boundary, Coordination & Dependency Architecture](application-ownership-boundaries.md) — **ADQ-002 ACCEPTED in 019-C; BND-001..012 current authority.**
- [Current Persistence, History, Provenance, Projection, Migration & Recovery Architecture](persistence-history-recovery.md) — **ADQ-003 ACCEPTED in 019-D; PST-001..016 current authority.**
- [Current Identity, Authentication, Participation, Access, Session & Technical-Authority Architecture](identity-access-authority.md) — **ADQ-004 ACCEPTED in 019-E; IAM-001..018 current authority.**
- [Current Interface, Command/Query, Transaction, Concurrency, Retry & Idempotency Architecture](interface-command-concurrency.md) — **ADQ-005 ACCEPTED in 019-F; CMD-001..022 current authority.**
- [Current Offline Draft, Multi-device, Degraded, Paper & Reconciliation Architecture](offline-continuity-reconciliation.md) — **ADQ-006 ACCEPTED in 019-G; RCV-001..018 current authority.**
- [Current Artifact, Export, Publication & External Delivery Architecture](artifact-export-publication-delivery.md) — **ADQ-007 ACCEPTED in 019-H; ART-001..020 current authority.**
- [Current Browser/Client State, Navigation, Accessibility & Degraded Interaction Architecture](browser-client-interaction.md) — **ADQ-008 ACCEPTED in 019-I after Q4R-004; CLT-001..020 current authority.**

Accepted architecture remains partial. Whole-architecture acceptance is still false until successful 019-L closure.

## Preserved candidate authority state

All other historical architecture documents listed below remain **downstream candidates**. Jackson-aligned Concept Design closed successfully in Phase 017; historical architecture does not become current merely because Phase 019 is active.

The controlling rules are:

- [Design / Implementation Boundary](../governance/design-implementation-boundary.md)
- [Downstream Architecture & Implementation Authority Quarantine](../governance/downstream-authority-quarantine.md)
- [Post-Concept-Design Architecture & Engineering Re-entry](../governance/post-concept-design-reentry.md)
- [Architecture Re-entry Evaluation & Decision Contract](../governance/architecture-reentry-evaluation.md)

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

## Permitted use before explicit architecture adoption

Architecture material may be consulted only to:

- detect implementation/architecture contamination of conceptual design;
- expose assumptions worth challenging;
- understand historical rationale;
- preserve evidence for later post-closure revalidation.

It must not be used to justify a Concept boundary, dependency, scope decision, mapping, familiar concept, synchronization, integrity trade-off, or misfit disposition because a framework/database/cloud/module design already expects it.

Phase 017 did not reactivate these candidates. Phase 018 qualified them as evidence; Phase 019 accepts only explicit bounded decisions. Current accepted families are DRV, BND, PST, IAM, CMD, RCV, ART and CLT. Historical candidates remain suspended unless explicitly adopted, revised, replaced or retired.


## Phase-017 audit result

017-F audited all nine documents in this subtree. Each now carries an explicit suspension notice at document level.

The corpus contains useful architectural forces and plausible hypotheses, but also stale semantic bindings and concrete topology/vendor decisions. It is therefore **not safe for automatic reactivation**. 018-J completed classification without adopting any candidate. 018-K defined the pre-selection question/dependency/evidence plan in `docs/routing/architecture_reentry_plan.json`; every selected option remains null and accepted architecture remains not established. 018-M has now authorized **Phase 019 — Architecture & Engineering Re-entry** to begin at 019-A. Phase 019 must compare and explicitly adopt, revise, replace or reject choices under the post-Concept-Design re-entry contract.


Current lifecycle: **PHASE 018 COMPLETE — PASS; PHASE 019 ACTIVE; 019-A/B/C/D/E/F/G/H/I COMPLETE / 019-J NEXT ELIGIBLE.** ADQ-001 through ADQ-008 are accepted; accepted whole architecture is still not established.


Current Phase-019 progression:

~~~text
PHASE 019 ACTIVE
019-A/B/C/D/E/F/G/H/I COMPLETE
019-J NEXT ELIGIBLE
ADQ-001 / ADQ-002 / ADQ-003 / ADQ-004 / ADQ-005 / ADQ-006 / ADQ-007 / ADQ-008 ACCEPTED
Q4R-001 / Q4R-002 / Q4R-003 / Q4R-004 COMPLETE
accepted whole architecture false
active implementation packages 0
implementation execution NOT AUTHORIZED
~~~
