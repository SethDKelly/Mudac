---
type: Phase Record
title: 020-K — Full Autonomous Implementation Roadmap, Agent Assignment Strategy, Phase/Package Definitions & Entry Readiness
description: "Finalizes the Phase-021..029 autonomous implementation roadmap, package-specific visible success/evidence contracts, preferred Cursor/Codex role profiles, concurrency/serialized-surface policy and G1 readiness decisions while preserving explicit G2 authorization."
status: stable
tags: [phase-020, roadmap, autonomous-development, cursor, codex, g1, implementation-planning]
sources:
  - resource: README.md
  - resource: ../routing/phase020_autonomous_implementation_roadmap.json
  - resource: ../implementation-roadmap/index.md
  - resource: ../routing/phase020_implementation_package_discovery.json
  - resource: ../routing/phase020_implementation_phase_contract.json
  - resource: ../routing/autonomous_implementation_operating_model.json
  - resource: ../routing/phase020_nonproduction_test_control_architecture.json
  - resource: ../routing/phase020_ci_supplychain_evidence_architecture.json
  - resource: ../routing/phase020_review_repair_exit_gate_governance.json
  - resource: ../routing/phase020_crosscutting_verification_architecture.json
  - resource: ../routing/phase020_v1_completion_integration_design.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-23T14:20:00-05:00 }
---

# Purpose

Turn the accumulated 020-A..J design into the actual implementation-program roadmap that future autonomous development phases can execute after explicit authorization.

020-K finalizes:

- implementation phase sequence;
- retained package set;
- package-specific success criteria and evidence obligations;
- phase/package assignment;
- preferred Cursor/Codex implementer/reviewer profiles;
- worktree and serialized-surface concurrency rules;
- repair/review/Gatekeeper/reopen policy;
- G1 planning-readiness decisions;
- Phase-021 entry candidate.

It still does **not** grant G2.

# Entry state

~~~text
PHASE 020 ACTIVE
020-A/B/C/D/E/F/G/H/I/J COMPLETE
020-K NEXT ELIGIBLE / USER AUTHORIZED

proposed package candidates       15
G1-ready packages                  0
G2-authorized packages             0
active implementation packages     0
implementation execution          NOT AUTHORIZED
release authority                 NOT GRANTED
production authority              NOT GRANTED
~~~

Exact planning baseline:

> 94828250c21d4ffe6299b75cc5f620a3bdf842a6

# Decision

**020-K — ACCEPT THE NINE-PHASE AUTONOMOUS IMPLEMENTATION ROADMAP AND MARK ALL FIFTEEN RETAINED PACKAGES G1 COMPLETE / READY FOR AUTHORIZATION.**

The governing distinction is:

> **G1 means the package is planned well enough to review for execution authority. It does not permit execution.**

And:

> **Only G2 names the packages that may actually be implemented.**

# Final retained package set

020-K retains all fifteen discovered package identities:

~~~text
IMP-001  Source Topology & Implementation Foundation
IMP-002  Persistence, Migration, History & Projection Substrate
IMP-003  Application Interface, Command, Transaction, Idempotency & Reconciliation Foundation
IMP-004  Browser Client, State & Accessibility Foundation
IMP-005  Non-Production Test-Control, Fixtures & Observability Foundation
IMP-006  AWS Non-Production Runtime, Deployment & Provider Foundation
IMP-007  Competition Context Owner Vertical
IMP-008  Identity, Participation, Access & Session Vertical
IMP-009  Evaluation Owner Vertical
IMP-010  Offline, Multi-Device, Paper & Reconciliation Continuity
IMP-011  Outcomes & Officiality Owner Vertical
IMP-012  External Representation, Artifact & Publication Vertical
IMP-013  Cross-Owner Operational Projections & Read Models
IMP-014  Verification, Protected Evaluator & Supply-Chain Evidence Infrastructure
IMP-015  Production Runtime, Deployment, Backup & Recovery Infrastructure
~~~

No package is split, merged, superseded or cancelled in 020-K.

The detailed final package contracts live in:

> `docs/routing/phase020_autonomous_implementation_roadmap.json`

# Final implementation phase sequence

The accepted implementation program is:

~~~text
021  IMP-001
  ↓
022  IMP-002 + IMP-004 + IMP-005 + IMP-006
  ↓
023  IMP-003 + IMP-014
  ↓
024  IMP-007
  ↓
025  IMP-008
  ↓
026  IMP-009
  ↓
027  IMP-010 + IMP-011
  ↓
028  IMP-012 + IMP-013 + IMP-015
  ↓
029  V1-FINAL
~~~

This sequence preserves hard dependencies while exploiting safe parallelism inside 022, 023, 027 and 028.

# Phase 021

**Source Topology & Implementation Foundation**

Package:

> IMP-001

This is the first possible implementation phase after Phase 020.

It repairs the executable repository to the accepted five-owner topology and establishes the package/dependency seams that every downstream phase relies on.

Preferred assignment:

- Implementer: **Codex**
- Independent Reviewer: **Cursor**

This preference is operational guidance, not authority.

021 is not authorized by 020-K.

# Phase 022

**Persistence, Browser, Test-Control & Non-Production Runtime Foundations**

Packages:

- IMP-002
- IMP-004
- IMP-005
- IMP-006

These may execute in parallel after 021 because their hard dependency is the repaired foundation, not one another.

Maximum ordinary concurrency:

> 3 work units

The Coordinator serializes root lockfile/configuration, shared environment configuration and overlapping provider/test surfaces.

# Phase 023

**Command, Transaction & Verification Evidence Foundations**

Packages:

- IMP-003
- IMP-014

IMP-003 establishes authoritative command/query, transaction, idempotency, result/reconciliation and partial-result foundations.

IMP-014 establishes independent exact-revision CI/evidence/protected-evaluator/supply-chain infrastructure.

Maximum concurrency:

> 2 work units

# Phases 024–026

These phases deliberately proceed in semantic dependency order:

~~~text
024  Competition Context          IMP-007
025  Identity / Participation /
     Access / Session             IMP-008
026  Evaluation                   IMP-009
~~~

They are single-primary-package phases because each next owner depends materially on current semantics from the previous one.

Preferred implementation profile is Cursor with independent Codex review.

# Phase 027

**Continuity & Outcomes Parallel Verticals**

Packages:

- IMP-010
- IMP-011

Both depend on the completed Evaluation owner but neither is the semantic owner of the other.

They therefore may proceed in isolated parallel worktrees while shared Evaluation and Organizer surfaces are coordinated.

# Phase 028

**Representation, Projections & Production Runtime**

Packages:

- IMP-012
- IMP-013
- IMP-015

These close the remaining v1 implementation packages:

- Export/Artifact/Publication;
- operational projections/read models;
- production-shaped runtime/deployment/backup/recovery infrastructure.

IMP-015 completion is infrastructure implementation evidence, not production authorization.

# Phase 029

**PF-01 v1 Whole-System Integration & Hardening**

Logical alias:

> **V1-FINAL**

029 qualifies one exact integrated PF-01 revision against:

- V1-WS-01..12;
- JNY-01..09;
- SCN-01..15;
- architecture conformance;
- security/privacy/authority;
- migration/recovery;
- accessibility;
- event-load/performance/cost;
- supply-chain/provenance;
- independent and adversarial review.

029 has no blanket write authority over completed package code.

A source-changing defect in a G5 package uses 020-H reopen and explicit re-authorization.

Successful 029 exit records:

> **V1_IMPLEMENTATION_COMPLETE**

and advances only to:

> **RELEASE_CANDIDATE_ELIGIBLE_NOT_AUTHORIZED**

# Package-specific contracts

020-K instantiates the reusable 020-F contract for every package.

Every retained package now has:

- final purpose and scope;
- exclusions;
- semantic/architecture/engineering references;
- hard/integration/evidence dependencies;
- owned surfaces;
- serialized surfaces;
- migration impact;
- security/privacy impact;
- accessibility/degraded impact;
- failure/recovery impact;
- required evidence classes;
- scenario obligations;
- compatibility/rollback strategy;
- residual risks;
- review/adversarial-review policy;
- bounded repair budget;
- Gatekeeper policy;
- reopen policy;
- visible success criteria;
- evidence obligations;
- required NPT tiers;
- allowed external actions;
- circuit breakers;
- final phase assignment.

The package-specific criteria are intentionally obligation-oriented rather than test-name-oriented.

# G1 decision

All fifteen retained package contracts satisfy the current G1 contract.

Therefore:

~~~text
packages retained                 15
packages G1 COMPLETE              15
packages READY_FOR_AUTHORIZATION  15
packages G2 AUTHORIZED             0
active packages                    0
~~~

This is the first point in Phase 020 at which any package is legitimately G1-ready.

# Why all packages may be G1-ready before their predecessors finish

G1 means **planned**.

It does not mean **eligible for immediate execution**.

Hard predecessors are primarily a G2/start-gate constraint.

For example, IMP-009 can be fully planned now while still being ineligible for G2 until its required predecessor state is satisfied.

This distinction allows the entire roadmap to be reviewed as a coherent program before implementation begins.

# Repair budget

Each package receives the visible default repair envelope:

~~~text
ordinary repair cycles                 3
repeated identical mandatory failures  2
scope expansion                         FORBIDDEN
extension                               explicit Coordinator +
                                        human/program authority
~~~

These are implementation-governance limits, not product acceptance thresholds.

A phase may tighten them before G2 if its visible contract requires it.

# Cursor / Codex assignment strategy

Tool assignment is a preferred operating profile.

It is not semantic authority and is not an immutable provider requirement.

## Cursor preference

Cursor is preferred for:

- semantic-owner verticals;
- browser-heavy work;
- interactive feature integration;
- local UI/accessibility/reconciliation work.

## Codex preference

Codex is preferred for:

- repository topology;
- persistence/migration substrate;
- non-production/runtime infrastructure;
- CI/evidence/protected-evaluator infrastructure;
- bounded large cross-file transforms.

## Reciprocal review

When Cursor implements, prefer an independent Codex review.

When Codex implements, prefer an independent Cursor review.

020-H remains authoritative:

- reviewer run/context must be independent;
- provider diversity is preferred, not required;
- Reviewer edits convert that reviewer into an Implementer for the changed revision.

# Coordinator strategy

Every phase gets one named Coordinator run.

The Coordinator:

- receives G2 scope;
- resolves exact baseline;
- creates work-unit/context manifests;
- allocates isolated worktrees;
- leases serialized surfaces;
- limits concurrency;
- integrates package candidates;
- records provenance;
- routes circuit breakers.

The Coordinator cannot:

- grant G2;
- enlarge scope;
- redefine requirements;
- waive evidence;
- authorize release/production.

Delegation depth remains one.

# Serialized-surface policy

Parallel autonomous development is bounded by one-writer ownership of shared control surfaces.

Examples include:

- root workspace/lockfile;
- migration catalog;
- API contract index;
- shared browser shell;
- MCP fixture/capability registry;
- CI/evidence schema;
- OpenTofu state/backend/root;
- deployment workflows.

Parallel package work never implies parallel writes to the same serialized surface.

# Entry readiness

020-K establishes planning readiness for the complete implementation program.

It does not establish Phase-021 execution readiness by itself.

The first possible execution candidate is:

> **Phase 021 / IMP-001**

Before G2 it still requires:

- successful 020-L Phase-020 exit;
- exact Phase-021 start baseline;
- current IMP-001 G1 status;
- no semantic/architecture blocker;
- repository-enforcement observation required by current controls;
- explicit human/program G2 naming IMP-001.

# Machine authority

The final roadmap and package contracts are:

> `docs/routing/phase020_autonomous_implementation_roadmap.json`

Human-oriented progressive disclosure is:

> `docs/implementation-roadmap/index.md`

Validation must reject any future drift that:

- reduces the retained package set without explicit disposition;
- marks a package G1-ready without a complete contract;
- makes G1 execution authority;
- grants any package G2 during Phase 020;
- activates a package;
- removes explicit hard dependencies;
- allows recursive delegation;
- removes isolated-worktree/serialized-surface controls;
- converts Cursor/Codex preference into lifecycle authority;
- lets 029 edit completed package source without 020-H reopen;
- makes V1 completion equal G6/G7;
- auto-authorizes Phase 021.

# Phase-020 boundary after 020-K

~~~text
PHASE 020 ACTIVE
020-A/B/C/D/E/F/G/H/I/J/K COMPLETE
020-L NEXT ELIGIBLE

G1-ready packages                 15
READY_FOR_AUTHORIZATION packages  15
G2-authorized packages             0
active implementation packages     0

implementation execution          NOT AUTHORIZED
release authority                 NOT GRANTED
production authority              NOT GRANTED
~~~

# Exit decision

**020-K — COMPLETE — PASS.**

The MUDAC implementation program is now fully decomposed and planning-ready.

020-L must still audit the complete Phase-020 corpus, repository-control evidence, G1 decisions, exact head and Phase-021 handoff before implementation may begin.

Next eligible:

> **020-L — Phase-020 Consolidation, Pre-Implementation Audit, Exit Decision & Phase-021 Handoff**

020-L is **NEXT ELIGIBLE / NOT AUTOMATICALLY AUTHORIZED**.
