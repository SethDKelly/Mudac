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

Phase 019 has now established accepted architecture and satisfied G0. This contract therefore permits Phase-020 package derivation, but it does not itself create a package or authorize implementation execution.

<a id="ipg-001"></a>
## IPG-001 — Implementation Framework Does Not Create Active Packages or Execution Authority

Phase 018 created this framework while architecture was not yet accepted and therefore kept package derivation blocked.

Successful Phase 019 closure now satisfies G0 and permits package derivation through the Phase-020 planning lifecycle.

The framework itself still does not:

- create an implementation package automatically;
- authorize package execution;
- authorize merge, release, deployment or production.

At the Phase-019 → Phase-020 handoff, active package count remains zero and implementation execution remains unauthorized.

Phase 020 is the final **pre-implementation program-design lifecycle**. It may derive the phase/package roadmap, evidence contracts and readiness state, but it does not grant G2 or execute MUDAC domain implementation. The first implementation execution may occur only in Phase 021 or later after the relevant package/phase receives explicit G2 human/program authorization.

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
- residual risks and later-gate assignments;
- autonomous execution mode (single-agent or coordinated multi-agent);
- Coordinator/Implementer/Reviewer role policy;
- declared work-unit graph where delegation is allowed;
- exact-base/worktree isolation and serialized-surface rules;
- context-manifest and technical-provenance requirements;
- bounded external actions, autonomy circuit breakers and repair/escalation boundaries.

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
## IPG-006 — Package Execution Is Human-Directed at the Lifecycle Boundary and Cannot Auto-Advance

A human-selected G2-authorized package establishes the implementation task envelope.

Inside that envelope, the package may authorize a named Coordinator to schedule declared dependency-safe work units among autonomous agents without per-edit human approval. That bounded delegation is execution of the selected package, not autonomous package selection.

The package plan must preserve:

- coordinator-only delegation;
- no recursive undeclared implementation delegation;
- exact-base work isolation;
- shared-writer serialization;
- independent review;
- circuit-breaker escalation;
- separate merge/release/deployment authority.

Completion of one package may identify the next dependency-safe package but does not authorize an agent to begin it automatically.

This inherits AGT-001, AGT-009 and AGT-010.

<a id="ipg-007"></a>
## IPG-007 — Package Dependencies Must Be Explicit and Acyclic

The implementation program maintains a package dependency graph.

A package may enter execution only when:

- required predecessors are COMPLETE;
- or the package is demonstrably independent of their unresolved outputs.

Parallel execution is allowed only where ownership, migration and shared-resource conflicts are explicitly controlled.

Within a package, parallel work units require isolated worktrees/checkouts plus an explicit serialized-surface set for shared control points such as migration order, lockfiles, root CI, common infrastructure authority, generated registries and overlapping owner-private code.

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

A G2 package may pre-authorize bounded branch/PR mechanics required for its work envelope, but merge remains distinct and cannot be inferred from green CI or reviewer approval.

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

The machine-readable framework is:

docs/routing/implementation_program_framework.json

It defines package fields, lifecycle and gates.

At Phase-019 closure it is in PLANNING_READY state with G0 satisfied, package derivation allowed, zero active packages and no implementation execution authority.

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

# Phase-020 autonomous implementation-program design

Accepted architecture now exists and 020-A has opened the final pre-implementation design lifecycle. Phase 020 must:

1. confirm the exact accepted architecture baseline;
2. create the implementation-package namespace;
3. derive package boundaries from architecture and current semantics;
4. create the package dependency graph;
5. assign scenario/evidence obligations;
6. qualify reusable Q3/Q5 implementation substrate;
7. establish environment/supply-chain/secrets/migration baselines;
8. identify which packages are planning-ready;
9. explicitly decide whether any package receives execution authorization.

Package decomposition was deliberately not frozen before architecture acceptance. Phase 020 may now derive it from the accepted architecture, current semantic authority and the retained scenario/evidence obligations.


# Autonomous implementation operating projection

Phase 020-C defines the current tool-neutral role/isolation/delegation projection at:

> docs/routing/autonomous_implementation_operating_model.json

That projection is subordinate to this contract plus canonical agent governance.

It defines Human Authorizer, Coordinator, Implementer, Reviewer, Verifier and Gatekeeper roles; coordinator-only delegation; worktree isolation; context/provenance fields; serialized surfaces; and fail-closed circuit breakers.

Phase 020 itself remains pre-implementation. These rules become executable only for a later G2-authorized package/phase.


# Non-production agent test-control architecture

Phase 020-D defines the current implementation-program testability contract at:

> docs/routing/phase020_nonproduction_test_control_architecture.json

The control plane is non-production-only and uses MCP as an agent protocol around real MUDAC application/runtime boundaries.

Implementation packages that use it must preserve:

- worktree-local deterministic testing as the default repair-loop boundary;
- escalation to isolated/shared AWS non-production only when the material evidence boundary requires it;
- deterministic synthetic FixtureBlueprints and explicit synthetic actor identities;
- separation of MCP technical caller authority from MUDAC Identity / Participation / Access;
- real application command/query/browser paths for behavior evidence;
- direct fixture seeding only as setup basis, never as evidence for the command path bypassed;
- RUN-020/RUN-021 structured/OpenTelemetry observability rather than MCP protocol logging as a second telemetry authority;
- registered bounded fault profiles rather than arbitrary shell/cloud/database controls;
- a separate protected evaluator that hides probes, not requirements;
- deterministic production-denial controls in IaC/configuration/runtime.

Remote MCP authorization must be resource/audience-bound to the test-control plane and must not pass through credentials issued for another downstream resource.

The test-control plane may support E2–E5 and selected E6 evidence. It cannot establish E7 production evidence.

Phase 020 remains design-only: this contract does not itself deploy a non-production environment, implement an MCP server or grant G2.


# Phase-020 proposed implementation-package graph

Phase 020-E derives the current proposed package catalog and dependency graph at:

> docs/routing/phase020_implementation_package_discovery.json

The catalog currently contains **IMP-001 through IMP-015** in lifecycle state **PROPOSED**.

These identities are planning outputs under G0. They are not active implementation packages and do not satisfy G1 or G2.

The graph distinguishes:

- hard G2 predecessor edges;
- integration/G4 dependencies that may allow implementation overlap;
- evidence dependencies that may close later than ordinary coding;
- serialized shared surfaces that constrain otherwise parallel work.

The hard dependency graph must remain acyclic.

All Phase-016/IPG mandatory scenario seeds must have at least one proposed package owner before Phase 020-E may remain closed.

Final implementation-phase grouping remains owned by 020-K. The final whole-system v1 integration/hardening phase remains owned by 020-J.

A package becomes G1-ready only after later Phase-020 work completes its visible success/evidence contract, CI/evidence bindings, cross-cutting scenario obligations and final package/phase assignment.


# Implementation phase, success-criterion and protected-evaluation contract

Phase 020-F defines the reusable implementation contract at:

> docs/routing/phase020_implementation_phase_contract.json

The governing rule is:

> **Hide the probe, never the requirement.**

Before G2, a future implementation phase exposes its actual scope, package set, exact baseline, authority references, dependencies, work graph, success criteria, evidence obligations, scenario/security/accessibility/recovery/performance/cost obligations, allowed external actions, circuit breakers and exit predicates.

Each real acceptance threshold that defines required product/runtime behavior is visible. Protected evaluation may hide exact fixtures, samples, randomized generation, interleavings, fault timing, request ordering, mutation variants, test source and evaluator-only infrastructure; it may not hide the requirement, architecture rule, normative threshold, evidence floor, material boundary, required environment tier, mandatory scenario category or known blocker.

Success criteria are outcome/obligation statements with stable IDs and explicit minimum evidence boundaries. A stronger evidence composition may satisfy a criterion; a weaker evidence class may not be substituted merely for convenience.

The protected evaluator:

- is independent of the ordinary Implementer run/context;
- evaluates the exact candidate revision;
- derives probes only from the visible contract;
- cannot use production;
- cannot alter candidate code, acceptance criteria, G2 or next-phase authority;
- cannot use secret semantic bypasses;
- cannot count fixture seeding as proof of the application command it bypassed.

Required criterion outcomes fail closed on **FAIL**, **BLOCKED** or **INCONCLUSIVE**. `NOT_APPLICABLE` requires governed rationale and is not an Implementer escape hatch.

A multi-package implementation phase may receive G2 only when every package in its explicit authorization set is G1-complete and its predecessor/independence state is satisfied.

Defining this reusable contract does not itself make the Phase-020 proposed packages G1-ready. Package-specific criteria/evidence are instantiated later under 020-I/020-K.


# CI, supply-chain, exact-revision and evidence-bundle architecture

Phase 020-G defines the current delivery/evidence projection at:

> docs/routing/phase020_ci_supplychain_evidence_architecture.json

Exit-relevant evidence must bind to the exact source commit/tree it evaluates. Public CI, protected evaluation, independent review, release/promotion and production remain separate control planes; PASS at one plane never grants the authority of the next.

Future blocking/exit GitHub Actions dependencies must be pinned to immutable full commit SHAs, releaseable artifacts must be built once and promoted by digest, and deployable artifacts require explicit SBOM/provenance/attestation evidence. Security scanners supplement rather than replace behavioral E5 evidence.

Package/phase evidence is represented as an immutable, content-addressed manifest plus referenced evidence. The bundle preserves failed/retried attempts, criterion/evidence mappings, public/protected boundaries, artifact digests, exceptions, review references and residual risks. Protected evaluator probes remain outside ordinary implementer context when secrecy is material.

Repository workflow existence does not prove main-branch protection. Phase 021 may rely on protected-main enforcement only after the administrative configuration is independently observed and recorded.

Phase 020-G remains design-only. It does not implement IMP-014/015, grant G1/G2, authorize release or authorize production.


# Independent review, repair, reopen and exit-gate governance

Phase 020-H defines the current review/exit projection at:

> docs/routing/phase020_review_repair_exit_gate_governance.json

A future G5 candidate requires two independent review passes: ordinary code/design-fidelity review and adversarial conformance review. Neither may be the same authoring run as the candidate Implementer. Reviewer edits convert the reviewer into an Implementer for the changed revision and require fresh independent review.

Review findings bind to an exact candidate SHA. Open blocking findings are incompatible with PASS. Risk acceptance requires an actor with actual authority; reviewers and Gatekeepers cannot manufacture that authority.

Pre-G5 repair may continue under the current G2 only when it remains inside original scope and preserves visible criteria/evidence obligations. Source-changing repair creates a new candidate revision and reruns affected evidence/review. Scope expansion, semantic/architecture contradiction, repeated mandatory failure, unsafe migration/recovery ambiguity or authority-boundary change escalates rather than broadening G2.

The Gatekeeper integrates evidence and review; it does not override mandatory failures, change criteria, edit candidate source, grant next-phase G2, merge or deploy. COMPLETE creates an immutable G5 completion record whose successor state is NEXT_ELIGIBLE_NOT_AUTHORIZED.

After G5 the old G2 envelope is closed. Later invalidation may create REOPEN_REQUIRED, but renewed implementation needs explicit re-authorization and a fresh candidate/evidence/review/exit cycle. Historical completion records are linked, not rewritten.


# Cross-cutting verification architecture

Phase 020-I defines the current migration/recovery/accessibility/performance/cost/scenario projection at:

> docs/routing/phase020_crosscutting_verification_architecture.json

Every implementation package classifies cross-cutting applicability before G1. The classification does not make a package G1-ready by itself; package-specific success criteria, open normative thresholds and final phase assignment remain explicit later planning work.

The complete ENG-014 set is retained as fifteen program scenario IDs SCN-01..SCN-15. Scenario evidence must cross the material boundary: a unit test that merely names a scenario cannot close a required E3/E4/E5/E6 claim. Foundation-owned mechanisms require representative natural-owner integration where foundation-only proof would be semantically artificial.

Migration evidence is owner-scoped, additive-first, history-preserving and covers supported prior baselines, rolling compatibility where declared, partial failure, recovery and destructive-contraction prerequisites. Real PostgreSQL semantics require real PostgreSQL evidence.

Recovery evidence distinguishes command reconciliation, client/paper continuity, projection rebuild, backup/restore and regional DR. Backup existence or database restore alone is not semantic recovery; readiness follows authoritative restore -> application consistency -> derived-state/currentness -> external reconciliation -> service readiness.

Core browser workflows target WCAG 2.2 AA semantic parity. Automated scanners are supporting evidence, not proof of conformance; critical flows require manual accessibility evidence before release candidate readiness.

Performance acceptance thresholds, workload profiles and environment capacity are visible when material. Load/latency pressure cannot alter Access, authority, partial-result or unknown-result semantics. RTO/RPO are measured exercise claims, not invented documentation targets.

Cost evidence models material steady-state/event/runtime/storage/network/telemetry/backup/security/test infrastructure drivers. Cost optimization cannot remove mandatory availability, backup, encryption, security-logging or evidence-preservation controls.


# v1 whole-system completion and terminal integration/hardening

Phase 020-J defines the current v1 implementation-completion projection at:

> docs/routing/phase020_v1_completion_integration_design.json

The initial implementation target is the sole adopted PF-01 product variant. All eighteen current Concepts remain in v1 product scope, while the current explicit project non-goals remain excluded unless separate change authority activates them.

Package G5 closure is necessary but insufficient for v1 completion. The terminal program must qualify one composed exact revision against nine integrated journey families, all fifteen ENG-014 scenarios and twelve whole-system blocking criteria. A collection of package-local PASS records is not itself whole-system proof.

The logical terminal phase is V1-FINAL; 020-K assigns its final implementation-phase number/title. It owns only explicitly declared integration/hardening surfaces. It may not use final hardening as blanket authority to edit completed package-owned source: a source-changing defect in a G5 package follows 020-H reopen/re-authorization.

Successful terminal completion records V1_IMPLEMENTATION_COMPLETE and advances only to RELEASE_CANDIDATE_ELIGIBLE_NOT_AUTHORIZED. It does not grant G6, deployment authority, G7 or production readiness. G6 remains a separate release-authority boundary and G7 remains separately authorized.

V1 completion requires zero known blocking findings. Non-blocking residual risk may remain only with owner, rationale, impact and revisit trigger; residual-risk labeling cannot hide an unsatisfied visible criterion, semantic contradiction or architecture contradiction.


# Final autonomous implementation roadmap and G1 readiness

Phase 020-K defines the final implementation roadmap at:

> docs/routing/phase020_autonomous_implementation_roadmap.json

Human-oriented progressive disclosure is:

> docs/implementation-roadmap/index.md

The retained implementation program contains phases 021 through 029 and all fifteen IMP-001..IMP-015 package identities. 020-K instantiates the package-specific success/evidence contracts required by 020-F and records all fifteen packages as **G1 complete / READY_FOR_AUTHORIZATION**.

G1 is planning completeness only. It does not authorize implementation. During Phase 020 the G2-authorized count remains zero and active package count remains zero. The first possible execution candidate is Phase 021 / IMP-001 only after successful 020-L closure plus an exact Phase-021 start gate and explicit human/program G2.

Preferred Cursor/Codex assignments are operating profiles, not lifecycle or semantic authority. Work remains isolated by declared work unit/worktree; shared lockfile, migration, API-contract, client-shell, CI/evidence and IaC surfaces remain one-writer serialized controls.

The final roadmap sequence is:

~~~text
021 IMP-001
022 IMP-002/004/005/006
023 IMP-003/014
024 IMP-007
025 IMP-008
026 IMP-009
027 IMP-010/011
028 IMP-012/013/015
029 V1-FINAL
~~~

Phase 029 remains constrained by 020-H/020-J: it owns declared integration/hardening surfaces only and cannot silently reopen or edit G5 package-owned source.
