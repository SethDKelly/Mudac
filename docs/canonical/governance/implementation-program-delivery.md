---
type: Governance Contract
title: Implementation Program, Verification & Delivery-Gate Contract
description: Defines the technology-neutral implementation-program framework used after architecture acceptance, including package identity, lifecycle, dependency ordering, traceability, evidence classes, scenario carry-forward, migration/security/supply-chain gates, completion rules, merge/release separation, and explicit execution authorization.
status: stable
tags: [governance, implementation, program, packages, verification, evidence, delivery, gates, migration, security]
sources:
  - resource: architecture-reentry-evaluation.md
  - resource: downstream-realization-obligations.md
  - resource: design-implementation-boundary.md
  - resource: agentic-authority-scope.md
  - resource: ../../routing/downstream_candidate_qualification.json
  - resource: ../../018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/018-K-architecture-decision-questions-constraints-evaluation-evidence-reentry-decomposition.md
  - resource: ../implementation/verification-strategy.md
  - resource: ../implementation/implementation-foundation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T05:18:00Z }
---

# Purpose

Define the implementation-program structure MUDAC will use after a fresh architecture has been explicitly accepted.

This contract is intentionally technology-neutral.

It defines:

- how implementation packages are derived;
- what makes a package eligible for execution;
- how package dependencies and evidence are represented;
- what verification classes exist;
- what gates separate planning, implementation, merge, release and production claims;
- how semantic or architecture mismatches are escalated.

It does not derive current implementation packages because accepted architecture does not yet exist.

<a id="ipg-001"></a>
## IPG-001 — Phase-018 Implementation Framework Does Not Create Active Packages or Execution Authority

During Phase 018:

- accepted architecture remains not established;
- active implementation package count remains zero;
- package derivation remains blocked;
- domain implementation execution remains unauthorized.

The framework may define schemas, gates and evidence expectations only.

<a id="ipg-002"></a>
## IPG-002 — Implementation Packages Derive From Accepted Architecture and Current Semantic Authority

A future implementation package must trace to:

1. accepted current architecture decisions;
2. current semantic and governance owners;
3. applicable ENG obligations;
4. affected Phase-016 scenario obligations;
5. explicit predecessor packages where applicable.

Concepts do not imply one package each, and source folders do not define package boundaries merely because they already exist.

<a id="ipg-003"></a>
## IPG-003 — Package Identity Is Durable and Independent of Source Layout

Each package receives a stable implementation-package identifier when it is formally created.

Package identity survives:

- source-path moves;
- package/workspace renames;
- internal refactors;
- tooling changes;
- implementation-agent changes.

A package identifier is not reused for a different scope after completion or supersession.

<a id="ipg-004"></a>
## IPG-004 — Every Package Has an Explicit Scope and Evidence Contract

A package plan states at minimum:

- purpose;
- in-scope behavior;
- explicit exclusions;
- upstream semantic and architecture references;
- owned implementation surfaces;
- dependency/predecessor package IDs;
- data/schema/migration impact;
- security/privacy/disclosure impact;
- accessibility/degraded impact where relevant;
- failure/recovery impact;
- required evidence classes;
- Phase-016 scenario seeds affected;
- rollback/recovery or compatibility considerations;
- residual risks and later-gate assignments.

A package is not execution-ready merely because code locations are known.

<a id="ipg-005"></a>
## IPG-005 — Package Lifecycle Separates Planning, Authorization, Execution and Completion

The generic package lifecycle is:

~~~text
PROPOSED
  ↓
PLANNED
  ↓
READY_FOR_AUTHORIZATION
  ↓
AUTHORIZED
  ↓
IN_PROGRESS
  ↓
EVIDENCE_REVIEW
  ↓
COMPLETE
~~~

Additional non-success states may include:

~~~text
BLOCKED
SUPERSEDED
CANCELLED
~~~

Only an explicit authorization transition permits domain implementation work.

Planning status never implies authorization.

<a id="ipg-006"></a>
## IPG-006 — Package Execution Is Human-Directed and Cannot Auto-Advance

A human-selected authorized package establishes the implementation task envelope.

Completion of one package may identify the next dependency-safe package but does not authorize an agent to begin it automatically.

This inherits AGT-001, AGT-009 and AGT-010.

<a id="ipg-007"></a>
## IPG-007 — Package Dependencies Must Be Explicit and Acyclic

The implementation program maintains a package dependency graph.

A package may enter execution only when:

- required predecessors are COMPLETE;
- or the package is demonstrably independent of their unresolved outputs.

Parallel execution is allowed only where ownership, migration and shared-resource conflicts are explicitly controlled.

The program must prevent package ordering from being inferred from file order, numbering convenience or historical 006/008 sequences.

<a id="ipg-008"></a>
## IPG-008 — Verification Evidence Uses Explicit Evidence Classes

Implementation evidence is classified at least as:

- **E1 — documentation/static**: schemas, static analysis, type/lint/format, generated contract checks, documentation conformance;
- **E2 — unit/component**: isolated deterministic behavior;
- **E3 — integration/runtime**: real material process/database/provider/runtime boundary where semantics depend on it;
- **E4 — scenario/end-to-end**: cross-boundary consequential workflow evidence;
- **E5 — security/accessibility/recovery**: authority/disclosure, abuse, accessibility, concurrency/recovery and other specialized behavioral evidence;
- **E6 — operational/deployment**: migration, rollout, restore, load, observability, DR and environment evidence;
- **E7 — production evidence**: evidence from an authorized production context.

A weaker class cannot be reported as a stronger class.

<a id="ipg-009"></a>
## IPG-009 — Use the Smallest Trustworthy Evidence Layer That Crosses the Material Boundary

Evidence choice follows the protected authority or failure boundary, not a universal test pyramid or coverage target.

Examples:

- pure calculations may close at E2;
- database transaction semantics require E3 against the selected real database semantics;
- browser interaction/accessibility may require E4/E5;
- restore/DR or deployment correctness requires E6;
- production behavior requires E7.

Coverage percentages and snapshots are diagnostic tools, not correctness authority.

<a id="ipg-010"></a>
## IPG-010 — Phase-016 Scenario Seeds Must Survive Into Package and Program Verification

The fifteen downstream semantic scenarios preserved by ENG-014 remain verification obligations.

Each package identifies which scenarios it affects.

Program-level verification must demonstrate that the composed implementation preserves all applicable scenarios, including retry, stale state, offline convergence, paper/electronic parity, correction, externalization, partial results, uncertainty, adversarial load and conflicting authority.

A scenario may be discharged across multiple evidence layers, but it cannot disappear from traceability.

<a id="ipg-011"></a>
## IPG-011 — Data, Schema and Migration Changes Require Compatibility and Recovery Evidence

A package that changes durable state must define:

- forward migration behavior;
- compatibility with the currently deployed/application transition state;
- backfill or transformation semantics where needed;
- rollback strategy or explicit roll-forward-only rationale;
- recovery from partial migration;
- historical/Provenance preservation;
- data-loss and destructive-operation boundaries;
- migration execution authority.

Application rollback must not assume destructive schema rollback is safe.

Exact migration tooling is selected only after architecture acceptance.

<a id="ipg-012"></a>
## IPG-012 — Supply Chain, Secrets, Fixtures and Sensitive Data Are Package Gates

Before an affected package can complete:

- dependencies and generated artifacts are reproducible and reviewable;
- secret material is excluded from source, fixtures and unsafe logs;
- real sensitive Competition/Judge/Team data is not used where synthetic data is sufficient;
- external-provider credentials and privileges follow least-authority task/environment boundaries;
- relevant dependency, static, IaC, container or artifact scanning is performed where the accepted architecture makes it applicable.

A scanner PASS does not replace behavioral security evidence.

<a id="ipg-013"></a>
## IPG-013 — Review, Merge, Release and Deployment Are Distinct Authorities

The implementation program distinguishes:

~~~text
package COMPLETE
  != merged
  != release candidate
  != deployed
  != production ready
~~~

Repository checks may gate review/merge.

Release/deployment requires separate environment and release authority.

Production readiness requires its own applicable E6/E7 evidence and is not created by successful CI.

<a id="ipg-014"></a>
## IPG-014 — Package Completion Requires Evidence Closure, Not Merely Code Completion

A package may become COMPLETE only when:

- planned scope is implemented;
- applicable evidence classes pass;
- stable semantic/architecture traceability is current;
- migration/compatibility impact is closed or explicitly assigned;
- security/privacy/accessibility impacts are addressed;
- documentation and generated routing remain coherent;
- residual risks have named owners and revisit gates;
- no known blocker is hidden by retries, quarantined tests or TODO prose.

Completion evidence is revision-specific.

<a id="ipg-015"></a>
## IPG-015 — Semantic and Architecture Mismatches Escalate Instead of Being Hidden in Implementation

If implementation work reveals:

- a product-semantic contradiction, route through CHG governance;
- an accepted-architecture contradiction, route through architecture re-entry/change authority;
- an evidence gap, add proportionate evidence rather than weakening the obligation.

Code, schema defaults, framework behavior or test expectations may not silently redefine upstream authority.

<a id="ipg-016"></a>
## IPG-016 — Implementation Program Exit Requires Whole-System Evidence and Explicit Next Authority

Completing all packages is not by itself production authorization.

Implementation-program exit requires:

- package dependency closure;
- whole-system scenario/evidence reconciliation;
- unresolved-risk disposition;
- migration/recovery readiness;
- security/accessibility evidence appropriate to the accepted architecture;
- current documentation/traceability;
- explicit statement of what release, environment or production-readiness authority is granted next.

The program must stop at the selected lifecycle boundary.

# Generic package schema

The machine-readable pre-architecture framework is:

docs/routing/implementation_program_framework.json

It defines the package fields, lifecycle and gates.

During Phase 018 the active package set must remain empty.

# Delivery-gate model

The generic delivery gates are:

| Gate | Meaning |
| --- | --- |
| G0 — Architecture Accepted | Package derivation is allowed only after accepted architecture exists |
| G1 — Package Planned | Scope, dependencies, traceability, risks and evidence contract are explicit |
| G2 — Package Authorized | Explicit human/program authority permits implementation execution |
| G3 — Implementation Evidence | Applicable E1–E5 package evidence passes |
| G4 — Compatibility / Integration | Shared-state, migration, integration and composed-scenario evidence passes |
| G5 — Package Complete | Evidence closure, docs/traceability and residual-risk assignment complete |
| G6 — Release Candidate | Release-specific E6 evidence and release authority requirements satisfied |
| G7 — Production Readiness | Applicable E6/E7, operational, recovery, security and external requirements satisfied |

G0 through G5 govern implementation-program delivery.

G6 and G7 are later release/production boundaries and are never implied by G5.

# Historical verification candidate use

The suspended historical verification strategy contains reusable Q1 verification principles.

Those principles may inform this framework only where they align with current ENG, ARE and IPG authority.

Concrete historical choices such as Vitest, Playwright, PostgreSQL/Testcontainers, Fastify test hosts or AWS-specific scanners remain Q3 implementation hypotheses until architecture and package planning make them applicable.

# Future implementation-program start gate

After accepted architecture exists, a future implementation-program start gate should:

1. confirm the exact accepted architecture baseline;
2. create the implementation-package namespace;
3. derive package boundaries from architecture and current semantics;
4. create the package dependency graph;
5. assign scenario/evidence obligations;
6. qualify reusable Q3/Q5 implementation substrate;
7. establish environment/supply-chain/secrets/migration baselines;
8. identify which packages are planning-ready;
9. explicitly decide whether any package receives execution authorization.

The actual package decomposition cannot be responsibly frozen before architecture acceptance.
