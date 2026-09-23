---
type: Phase Record
title: 020-E — Implementation Phase/Package Discovery, Dependency Graph, Parallelism & Sequencing
description: "Derives proposed durable implementation-package identities from accepted architecture, qualified substrate and autonomous testability infrastructure; defines hard/integration/evidence dependencies, safe parallel tracks, serialized shared surfaces, scenario coverage and sequencing without granting G1/G2 or freezing final implementation-phase grouping."
status: stable
tags: [phase-020, implementation-packages, dependency-graph, parallelism, sequencing, autonomous-development]
sources:
  - resource: README.md
  - resource: 020-B-existing-substrate-historical-implementation-reuse-qualification.md
  - resource: 020-C-cursor-codex-roles-work-isolation-context-provenance-autonomy-circuit-breakers.md
  - resource: 020-D-nonproduction-environment-synthetic-data-observability-mcp-agent-test-control-plane-architecture.md
  - resource: ../canonical/architecture/accepted-architecture.md
  - resource: ../canonical/architecture/application-ownership-boundaries.md
  - resource: ../canonical/governance/implementation-program-delivery.md
  - resource: ../canonical/governance/downstream-realization-obligations.md
  - resource: ../routing/phase020_substrate_reuse_qualification.json
  - resource: ../routing/autonomous_implementation_operating_model.json
  - resource: ../routing/phase020_nonproduction_test_control_architecture.json
  - resource: ../routing/phase020_implementation_package_discovery.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-23T06:57:00-05:00 }
---

# Purpose

Derive an implementation work graph that is coarse enough to remain reviewable and autonomous-agent friendly, but fine enough to preserve ownership, evidence and dependency boundaries.

020-E answers what independently reviewable implementation responsibilities exist, which responsibilities must precede others, which may run concurrently, which shared surfaces require serialization despite otherwise independent work, and which candidate package carries each mandatory scenario seed.

It does **not** finish package planning.

# Entry state

~~~text
PHASE 020 ACTIVE
020-A/B/C/D COMPLETE
020-E NEXT ELIGIBLE / USER AUTHORIZED

accepted architecture             true
qualified substrate               complete
autonomous operating model        established
nonproduction test architecture   established

active implementation packages    0
G2 authorizations                 0
domain implementation             NOT AUTHORIZED
~~~

# Package-discovery rule

The package graph is derived from:

~~~text
accepted architecture
+
current semantic owners
+
qualified executable substrate
+
autonomous-development controls
+
nonproduction testability needs
+
verification/realization obligations
~~~

It is **not** derived from current folders, the historical six-module implementation skeleton, one package per Concept, one package per architecture family, arbitrary frontend/backend layering, or historical Phase-008 ordering.

# Candidate lifecycle meaning

020-E uses the existing IPG lifecycle state **PROPOSED**.

A proposed package has a durable candidate ID, an implementation purpose/boundary hypothesis, and may participate in dependency analysis. It is not active implementation work, has not passed G1, and cannot receive G2 yet.

Every discovered package explicitly remains missing 020-F visible-success/evidence contract completion, 020-G exact-SHA CI/supply-chain/evidence-bundle binding, 020-I final cross-cutting evidence/scenario mapping, and 020-K final package plan and implementation-phase assignment.

~~~text
PROPOSED
  != PLANNED
  != READY_FOR_AUTHORIZATION
  != AUTHORIZED
~~~

# Dependency semantics

020-E distinguishes three edge classes.

## HARD_G2_PREDECESSOR

Default predecessor completion is required before the downstream package receives G2. A later gate may prove independence explicitly, but silence does not erase the edge.

## INTEGRATION_G4_DEPENDENCY

Implementation may proceed in parallel when contracts are sufficiently stable. The downstream package cannot close integration/completion until the dependency is reconciled.

## EVIDENCE_DEPENDENCY

The referenced package supplies a material verification/provider/environment boundary needed for the downstream claim. It may not have to precede ordinary coding, but relevant evidence cannot close without it.

# Proposed package catalog

| ID | Proposed package | Kind | Hard predecessor posture |
|---|---|---|---|
| **IMP-001** | Source Topology & Implementation Foundation | foundation | root |
| **IMP-002** | Persistence, Migration, History & Projection Substrate | foundation | IMP-001 |
| **IMP-003** | Application Interface, Command, Transaction, Idempotency & Reconciliation Foundation | foundation | IMP-001/002 |
| **IMP-004** | Browser Client, State & Accessibility Foundation | foundation | IMP-001 |
| **IMP-005** | Non-Production Test-Control, Fixtures & Observability Foundation | verification foundation | IMP-001 |
| **IMP-006** | AWS Non-Production Runtime, Deployment & Provider Foundation | runtime foundation | IMP-001 |
| **IMP-007** | Competition Context Owner Vertical | owner vertical | IMP-002/003/004 |
| **IMP-008** | Identity, Participation, Access & Session Vertical | owner vertical | IMP-002/003/004/007 |
| **IMP-009** | Evaluation Owner Vertical | owner vertical | IMP-002/003/004/007/008 |
| **IMP-010** | Offline, Multi-Device, Paper & Reconciliation Continuity | cross-cutting | IMP-003/004/008/009 |
| **IMP-011** | Outcomes & Officiality Owner Vertical | owner vertical | IMP-003/004/007/009 |
| **IMP-012** | External Representation, Artifact & Publication Vertical | owner vertical | IMP-003/004/011 |
| **IMP-013** | Cross-Owner Operational Projections & Read Models | derived read | IMP-003/004/007/009 |
| **IMP-014** | Verification, Protected Evaluator & Supply-Chain Evidence Infrastructure | verification foundation | IMP-001/005 |
| **IMP-015** | Production Runtime, Deployment, Backup & Recovery Infrastructure | runtime | IMP-006/014 |

Machine detail is in:

> docs/routing/phase020_implementation_package_discovery.json

# Why these boundaries

## Foundations are capabilities, not god-modules

IMP-002/003 provide physical persistence/command primitives while preserving natural-owner authority.

They may provide libraries/adapters/common transaction machinery. They do not own every owner's data or commands.

Likewise IMP-004 is browser architecture, not browser semantic ownership. IMP-005 is test infrastructure, not an alternate product API.

## Owner verticals stay aligned to the accepted five-owner topology

~~~text
IMP-007 Competition Context
        |
        v
IMP-008 Identity & Access
        |
        v
IMP-009 Evaluation
        |
        v
IMP-011 Outcomes & Officiality
        |
        v
IMP-012 External Representation
~~~

This preserves BND-007.

The historical judging-operations package does not reappear. Evaluation remains one owner.

## RCV remains cross-cutting around Evaluation

IMP-010 implements continuity/reconciliation mechanisms around accepted IAM/Evaluation/client contracts. It does not own a generic Reconciliation Concept or second Scorecard authority.

## Operational projections remain derived

IMP-013 owns disposable/rebuildable cross-owner read models and dashboards. It explicitly excludes Coverage/Aggregate/Rank semantic ownership, which remains in Outcomes & Officiality.

## Runtime work is separated from semantic work

IMP-006 builds the non-production provider/runtime boundary used for evidence.

IMP-015 implements production/recovery infrastructure.

Neither package grants release or production authority, and neither AWS resource becomes domain authority.

# Hard topological layers

~~~text
L0
  IMP-001

L1
  IMP-002   IMP-004   IMP-005   IMP-006

L2
  IMP-003   IMP-014

L3
  IMP-007   IMP-015

L4
  IMP-008

L5
  IMP-009

L6
  IMP-010   IMP-011   IMP-013

L7
  IMP-012
~~~

These layers are dependency eligibility, not final Phase-021+ grouping. 020-K owns final implementation-phase grouping.

# Semantic critical path

~~~text
IMP-001
  |
  v
IMP-002
  |
  v
IMP-003
  |
  v
IMP-007 Competition
  |
  v
IMP-008 Identity & Access
  |
  v
IMP-009 Evaluation
  |
  v
IMP-011 Outcomes
  |
  v
IMP-012 External Representation
~~~

This reflects authority flow rather than forcing every support package into one serialized chain.

# Parallel tracks

The largest early parallel region is:

~~~text
                IMP-002 Persistence
               /
IMP-001 ------+-- IMP-004 Browser foundation
               +-- IMP-005 Test-control foundation
               +-- IMP-006 AWS nonproduction foundation
~~~

Then IMP-002 enables IMP-003, while IMP-005 enables IMP-014.

After Evaluation stabilizes:

~~~text
                  +-- IMP-010 Continuity
IMP-009 Evaluation+-- IMP-011 Outcomes
                  +-- IMP-013 Operational read models
~~~

This fan-out is the largest later semantic parallelism opportunity.

# Competition and IAM sequencing

BND's default dependency tendency is Competition Context → Identity & Access.

020-E therefore records IMP-007 as a hard predecessor of IMP-008.

This is conservative. 020-K may decide that a single implementation phase can overlap some technical IAM work after IMP-007 exposes a stable Competition reference contract, but it must prove that overlap explicitly rather than erasing BND direction.

# Production runtime sequencing

IMP-015 becomes dependency-eligible relatively early because its hard prerequisites are nonproduction runtime and verification infrastructure.

That does **not** mean it should necessarily be the third implementation phase.

The package can begin reusable infrastructure/recovery work while later application contracts are evolving, but its integration dependencies prevent completion until relevant application/provider surfaces are stable.

020-K decides actual G2 timing.

# Shared serialized surfaces

Parallel packages still collide on some technical control points.

**SER-LOCK** serializes overlapping root package-manifest/lockfile integration.

**SER-MIG** allows owner-local migration authoring to parallelize while global migration registration/order/bootstrap integration remains serialized.

**SER-CI** gives root workflow/check integration one owner/window at a time.

**SER-IAC-NP** serializes common nonproduction backend/module/deployment-role changes.

**SER-IAC-PRD** assigns production/recovery infrastructure to IMP-015 by default.

**SER-AUTH** prevents ordinary implementation packages from casually editing canonical/routing authority or generated indexes.

# Scenario coverage at discovery time

All 15 mandatory Phase-016/IPG scenario seeds have at least one proposed package owner.

Key mappings include lost-response retry to IMP-003 plus consequential owners; duplicate/offline Draft convergence and paper/electronic disagreement to IMP-010; shared-device/stale Access to IMP-008/010/004; post-finalization correction to IMP-009; affected declaration and no-result closeout to IMP-011; stale Export and withdrawn Publication to IMP-012; concurrent intent/partial bulk/unknown result to IMP-003 and owners; adversarial volume to command/runtime/verification packages; and conflicting legitimate authority to the natural-owner verticals.

020-I still owns the final scenario/evidence matrix. 020-E only proves package discovery has not orphaned a mandatory seed.

# G1 readiness

**0 / 15 proposed packages are G1-ready.**

That is intentional.

020-F/G/I/K still need to complete the rest of each package contract.

# Package IDs and later refinement

IMP-001..IMP-015 are durable candidate IDs.

020-K may retain/promote a candidate, split it if evidence shows it is too broad, or supersede it if the boundary is wrong.

If a candidate ID is superseded, it is never reused for unrelated work.

020-K may not silently repurpose an existing candidate ID.

# Implementation-phase grouping

No Phase-021+ mapping is frozen here.

~~~text
implementation package
  = durable independently reviewable responsibility

implementation phase
  = controlled delivery envelope that may contain one or more dependency-safe packages/work units
~~~

020-K will group packages into implementation phases after 020-F through 020-J establish verification, review, scenario and v1-completion contracts.

# v1 integration

020-E does not create an IMP-v1-final package.

Whole-system v1 integration/hardening is a program/phase-level acceptance boundary, not another semantic implementation owner.

020-J owns that final phase definition.

# Exit decision

**020-E — COMPLETE — PASS.**

The repository now has 15 durable proposed implementation-package candidates, an acyclic hard dependency graph, explicit integration/evidence dependencies, safe parallel tracks, serialized shared-surface groups, complete initial coverage of all 15 mandatory scenario seeds, zero G1-ready packages, and zero G2-authorized packages.

Next eligible:

> **020-F — Implementation Phase Contract, Visible Criteria, Evidence Classes & Hidden Evaluation Architecture**

020-F is **NEXT ELIGIBLE / NOT AUTOMATICALLY AUTHORIZED**.
