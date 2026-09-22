# Architecture

This subtree preserves the architecture MUDAC selected before the latest Jackson methodology completion reassessment.

## Current authority state

**SUSPENDED AS A CONCEPT-DESIGN CONSTRAINT.**

Jackson-aligned Concept Design closed successfully in Phase 017. These documents remain **candidate downstream architecture knowledge**, not current authority over product meaning, until an explicit downstream architecture/engineering decision adopts, revises, replaces, or retires them.

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

Phase 017 closure did **not** automatically reactivate these documents. Phase 018 now qualifies the repository and prepares architecture/engineering re-entry; candidate architecture must still be compared against the closed conceptual design and explicitly dispositioned before it gains current downstream authority.


## Phase-017 audit result

017-F audited all nine documents in this subtree. Each now carries an explicit suspension notice at document level.

The corpus contains useful architectural forces and plausible hypotheses, but also stale semantic bindings and concrete topology/vendor decisions. It is therefore **not safe for automatic reactivation**. 018-J completed classification without adopting any candidate. 018-K defined the pre-selection question/dependency/evidence plan in `docs/routing/architecture_reentry_plan.json`; every selected option remains null and accepted architecture remains not established. 018-M has now authorized **Phase 019 — Architecture & Engineering Re-entry** to begin at 019-A. Phase 019 must compare and explicitly adopt, revise, replace or reject choices under the post-Concept-Design re-entry contract.


Current lifecycle: **PHASE 018 COMPLETE — PASS; PHASE 019 AUTHORIZED; 019-A NEXT ELIGIBLE.** Accepted architecture is still not established.
