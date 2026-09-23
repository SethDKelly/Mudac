---
type: Phase Record
title: 020-I — Migration, Recovery, Accessibility, Performance, Cost & Scenario Verification Design
description: "Defines cross-cutting implementation verification obligations for migration, recovery, accessibility, performance, cost and the complete fifteen-scenario validation set, including evidence floors, package applicability and G1–G7 gate bindings without granting implementation authority."
status: stable
tags: [phase-020, migration, recovery, accessibility, performance, cost, scenarios, verification]
sources:
  - resource: README.md
  - resource: 020-F-implementation-phase-contract-visible-criteria-evidence-classes-hidden-evaluation-architecture.md
  - resource: 020-G-ci-cd-security-supply-chain-exact-sha-verification-evidence-bundle-architecture.md
  - resource: 020-H-independent-code-review-adversarial-review-repair-reopen-exit-gate-governance.md
  - resource: ../canonical/governance/downstream-realization-obligations.md
  - resource: ../canonical/architecture/persistence-history-recovery.md
  - resource: ../canonical/architecture/frontend-interaction.md
  - resource: ../canonical/architecture/aws-runtime-operations.md
  - resource: ../canonical/experience/accessibility-resilience.md
  - resource: ../routing/implementation_program_framework.json
  - resource: ../routing/phase020_implementation_package_discovery.json
  - resource: ../routing/phase020_crosscutting_verification_architecture.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-23T13:56:00-05:00 }
---

# Purpose

020-I turns six cross-cutting concerns into explicit implementation-program evidence obligations:

1. schema/data/client-state migration;
2. command/data/application/disaster recovery;
3. accessibility and responsive semantic parity;
4. performance, concurrency, scale and overload behavior;
5. cost visibility and cost-control evidence; and
6. the complete fifteen-scenario downstream validation set preserved by ENG-014.

The goal is not to create one giant nonfunctional test suite.

The goal is to make each future package state exactly which cross-cutting claims apply, the material boundary that must be crossed, the minimum evidence class, what can be deferred to integration/release, and what may legitimately be not applicable.

# Entry state

~~~text
PHASE 020 ACTIVE
020-A/B/C/D/E/F/G/H COMPLETE
020-I NEXT ELIGIBLE / USER AUTHORIZED

proposed packages                 15
G1-ready packages                 0
G2-authorized packages            0
active implementation packages    0
implementation execution          NOT AUTHORIZED
release authority                 NOT GRANTED
production authority              NOT GRANTED
~~~

Exact planning baseline:

> 04612adffb9d295a81f20560db6d705db3e98588

# Decision

**020-I — ACCEPT CROSS-CUTTING VERIFICATION PROFILES PLUS A COMPLETE FIFTEEN-SCENARIO MATRIX.**

The central rule is:

> **Cross-cutting evidence follows the material risk boundary, not a generic checklist.**

A package that does not touch durable state should not manufacture migration tests.

A package that introduces consequential browser interaction cannot declare accessibility N/A merely because the backend is correct.

A runtime package cannot claim recovery because backups exist.

A load test cannot be trusted if its workload assumptions and acceptance thresholds are hidden.

A cost optimization cannot remove a trust guarantee merely because it is expensive.

# Threshold discipline

020-I preserves existing accepted thresholds and refuses to invent new ones.

Existing normative thresholds include:

- **WCAG 2.2 AA** for core browser workflows;
- production **at least two healthy API tasks across at least two AZs**;
- production RDS **35 days automated PITR**;
- active production in **us-east-2** with explicit cold regional recovery in **us-east-1**.

020-I does **not** invent:

- latency numbers;
- throughput numbers;
- event-size assumptions;
- dollar budgets;
- RTO;
- RPO.

When such a value becomes part of acceptance, it must be visible before the relevant implementation/release authorization and supported by evidence.

Hidden performance, recovery or cost thresholds are prohibited by the 020-F rule:

> **Hide the probe, never the requirement.**

# Migration verification profile

Migration verification applies whenever a package changes:

- authoritative database schema;
- module-owned durable state;
- client durable storage;
- evidence-bundle/schema state;
- stateful IaC topology;
- migration/deployment ordering.

A consequential migration plan identifies:

- owning module/technical owner;
- forward schema change;
- supported prior baseline;
- mixed-version compatibility where applicable;
- backfill/transformation;
- reconciliation/validation;
- history/Provenance impact;
- rollback or roll-forward-only rationale;
- partial-migration recovery;
- ordering/locking/checksum behavior;
- destructive-contraction prerequisites.

## Required migration evidence

At minimum, where applicable:

- **MIG-01** — current/fresh schema reaches expected state deterministically;
- **MIG-02** — every explicitly supported prior baseline upgrades successfully while preserving authority/history;
- **MIG-03** — old/new revisions coexist safely through declared rolling compatibility windows;
- **MIG-04** — partial/failing migration has deterministic fail-closed recovery or explicit safe roll-forward;
- **MIG-05** — history, Provenance and currentness survive transformation;
- **MIG-06** — destructive contraction occurs only after compatibility/retention prerequisites close.

PostgreSQL semantics are verified on real PostgreSQL where they matter.

SQLite/in-memory substitutes cannot prove PostgreSQL transaction, migration, constraint or locking semantics.

Application-startup auto-migration remains prohibited by accepted architecture.

# Recovery verification profile

The governing recovery rule is:

> **Recovery re-establishes truth; it never invents authority.**

020-I defines five recovery levels.

| Level | Boundary |
| --- | --- |
| **RCV-1** | command retry / uncertain-result reconciliation |
| **RCV-2** | local Draft, offline, shared-device and paper continuity |
| **RCV-3** | outbox, projection and derived-state rebuild |
| **RCV-4** | database/object backup restore + application validation |
| **RCV-5** | regional DR, one-authority promotion and paper continuity |

Readiness proceeds in order:

~~~text
authoritative storage restored
  ↓
application consistency verified
  ↓
projections rebuilt/current or truthfully unavailable
  ↓
external integrations reconciled
  ↓
service readiness explicitly declared
~~~

Backup creation alone is not recovery evidence.

Database restore alone is not semantic recovery.

A recovery process cannot turn unknown into success merely to obtain a clean state.

Regional recovery cannot create two independently writable MUDAC authorities.

RPO/RTO claims require measured exercises rather than documentation-only assertions.

# Accessibility verification profile

Normative target:

> **WCAG 2.2 AA semantic parity for core browser workflows**

Accessibility evidence must cover the actual semantic states MUDAC uses, not only a happy-path page.

Representative state classes include:

- ordinary success;
- validation failure;
- authorization denial;
- stale/conflict;
- uncertain outcome;
- degraded/unavailable;
- recovery;
- high-consequence confirmation.

Affected package G5 evidence includes, as applicable:

- semantic role/name/state checks;
- keyboard-operability tests;
- automated accessibility scanning;
- zoom/reflow/responsive checks;
- targeted manual review for novel/high-risk interactions.

Final integrated v1 / G6 evidence must include manual review of critical Judge and Organizer flows across:

- keyboard;
- screen reader/assistive technology;
- zoom/reflow;
- supported orientation changes;
- reduced motion where animation exists;
- relevant alternate/paper channel parity.

An automated scanner alone does not prove WCAG conformance.

Responsive layout cannot change authority, disclosure or legitimate recovery semantics.

# Performance verification profile

The governing performance rule is:

> **Performance may change capacity or latency; it may not change domain truth.**

For every material performance claim, the test contract exposes:

- acceptance threshold;
- workload profile;
- dataset shape;
- concurrency;
- environment/capacity;
- warmup and duration;
- result/error-class expectations.

Evidence records, where material:

- request/command latency distribution;
- throughput;
- confirmed/denied/conflict/unknown result distribution;
- DB connection/lock/transaction pressure;
- queue/outbox lag;
- projection freshness;
- browser responsiveness;
- Artifact/render throughput;
- CPU/memory saturation;
- abuse/rate-control behavior.

Performance evidence is tiered:

- **PERF-PKG — G3/G4 / E3+E5:** package/material runtime boundary;
- **PERF-EVENT — G6 / E6:** representative event profile, pre-scale and sustained/peak evidence;
- **PERF-PROD — G7 / E7:** later authorized production observation.

Known judging windows must be pre-scaled and load-tested before the event.

Load pressure cannot cause Access/domain validation to fail open.

Bulk pressure cannot flatten partial/unknown results into success.

# Cost verification profile

The governing cost rule is AWS-018:

> **Cost optimization removes unjustified infrastructure, not trust guarantees.**

Material runtime/provider packages model:

- steady-state runtime;
- peak/event capacity;
- database/storage growth;
- object storage/lifecycle;
- NAT/network/egress;
- logs/metrics/traces;
- backup/cross-region replication;
- KMS/secrets/security services;
- CI/evaluator/test infrastructure.

Evidence stages are:

- **COST-PLAN / E1** — visible provider/IaC estimate and assumptions;
- **COST-NP / E6** — measured nonproduction consumption where material;
- **COST-GUARD / E6** — Budgets/anomaly detection/allocation/retention controls where runtime exists;
- **COST-PROD / E7** — later production actuals.

020-I does not invent a dollar cap.

If a budget limit becomes an acceptance threshold, it must be visible and owned.

Production Multi-AZ, required API redundancy, backups, encryption, security logging and evidence preservation cannot be deleted merely to reduce cost.

# Fifteen-scenario verification matrix

All fifteen ENG-014 scenarios are now formal program-level verification obligations.

Each scenario has a stable program ID, package owners, material boundary, minimum evidence floor and explicit pass obligations in:

> docs/routing/phase020_crosscutting_verification_architecture.json

The mapping is:

| ID | Scenario | Primary package coverage | Floor |
| --- | --- | --- | --- |
| SCN-01 | lost-response retry after consequential authoritative action | IMP-003 + representative semantic owner | E3/E4/E5 |
| SCN-02 | duplicate/offline Draft convergence | IMP-010 | E3/E4/E5 |
| SCN-03 | shared-device context handoff | IMP-004/005/008/010 | E4/E5 |
| SCN-04 | stale Participation/Access/session state | IMP-008 | E3/E4/E5 |
| SCN-05 | paper/electronic capture disagreement | IMP-010 | E3/E4/E5 |
| SCN-06 | post-finalization correction | IMP-009 | E3/E4/E5 |
| SCN-07 | affected Outcome Declaration with same visible winner | IMP-011 | E3/E4/E5 |
| SCN-08 | exceptional no-result closeout | IMP-011 | E3/E4/E5 |
| SCN-09 | stale Export after source correction | IMP-012 | E3/E4/E5 |
| SCN-10 | withdrawn Publication while external copies remain | IMP-012 | E3/E4/E5 |
| SCN-11 | concurrent/repeated legitimate intent | IMP-002/003/007/009 | E3/E4/E5 |
| SCN-12 | partial bulk result | IMP-003 + representative semantic operation | E3/E4/E5 |
| SCN-13 | unknown/degraded result | IMP-002/003/004/005/006/010/012/013/015 | E3/E4/E5/E6 |
| SCN-14 | adversarial request volume | IMP-006/008/014/015 | E3/E5/E6 |
| SCN-15 | conflicting legitimate authority resolved at natural owner | IMP-007/009/011 | E3/E4/E5 |

A scenario is not closed merely because one package unit test mentions it.

Scenarios may span packages and evidence layers.

Final v1 verification must replay all fifteen at their material composed boundaries.

# Foundation-only scenario caution

Some scenarios initially map to infrastructure/foundation packages because those packages own the reusable mechanism.

That is not sufficient when the semantic risk requires a natural-owner realization.

For example:

- SCN-01 must eventually use a real consequential owner command;
- SCN-12 must exercise a real partial-result use case;
- SCN-14 must cross the actual nonproduction edge/API/runtime security boundary.

020-K/J will select the final representative semantic instantiations without changing the scenario category.

# Package applicability mapping

020-I assigns every IMP-001..015 package an explicit cross-cutting profile in the machine contract.

The map identifies:

- migration applicability;
- recovery profile;
- accessibility profile;
- performance profile;
- cost profile;
- scenario IDs.

This resolves the 020-E placeholder:

> **020-I final scenario/migration/recovery/accessibility/performance/cost evidence mapping**

It does **not** make any package G1-ready.

Package-specific success criteria, exact thresholds where still open, final evidence instantiation and phase assignment remain 020-K work.

# Gate bindings

## G1 — Package Planned

Before G1, each package must classify:

- migration applicability;
- recovery applicability;
- accessibility applicability;
- performance-sensitive boundaries;
- cost-sensitive/provider boundaries;
- scenario obligations;
- evidence floors;
- visible thresholds/assumptions where material.

N/A requires an explicit rationale.

## G2 — Package Authorized

G2 requires:

- no unresolved cross-cutting blocker;
- required nonproduction/test infrastructure dependency declared;
- H-defined review and bounded repair contract.

020-I itself grants no G2.

## G3 — Implementation Evidence

Package-local E1–E5 cross-cutting evidence passes where applicable.

## G4 — Compatibility / Integration

Migration/recovery integration and affected scenarios close at their material cross-package boundaries.

## G5 — Package Complete

Cross-cutting package obligations are either closed or explicitly assigned to a legitimate later gate.

There can be no hidden performance/accessibility/recovery/cost blocker.

## G6 — Release Candidate

As applicable:

- release migration/rollback evidence;
- backup/restore evidence;
- event-load/performance evidence;
- critical-flow manual accessibility evidence;
- runtime cost-control evidence.

## G7 — Production Readiness

Production-specific evidence remains separately authorized.

020-I creates no E7 requirement that would force production access during preproduction implementation.

# Relationship to 020-F/G/H

020-F answers:

> what must be visible and what evidence class is required?

020-G answers:

> how is that evidence bound to exact revisions/artifacts?

020-H answers:

> who independently reviews it and how are repair/reopen decisions governed?

020-I answers:

> which migration, recovery, accessibility, performance, cost and scenario evidence obligations apply across the implementation program?

Together:

~~~text
visible criterion
  ↓
cross-cutting applicability/profile
  ↓
exact-revision evidence
  ↓
independent + adversarial review
  ↓
Gatekeeper
~~~

# Machine contract

Current projection:

> docs/routing/phase020_crosscutting_verification_architecture.json

Validation must fail if:

- the scenario set no longer equals the fifteen ENG-014 seeds;
- a scenario loses all package ownership;
- migration can be declared complete without partial-failure/history handling;
- restore alone is treated as semantic recovery;
- automated accessibility scanning is allowed to prove WCAG by itself;
- hidden performance/cost thresholds are allowed;
- RTO/RPO are accepted without measured evidence;
- cost optimization may remove mandatory trust controls;
- a package becomes G1/G2 merely because 020-I mapping exists;
- Phase 020 gains execution/release/production authority.

# Phase-020 boundary after 020-I

~~~text
PHASE 020 ACTIVE
020-A/B/C/D/E/F/G/H/I COMPLETE
020-J NEXT ELIGIBLE

proposed packages                 15
G1-ready packages                 0
G2-authorized packages            0
active implementation packages    0
implementation execution          NOT AUTHORIZED
release authority                 NOT GRANTED
production authority              NOT GRANTED
~~~

# Carry-forward

- **020-J** defines whole-system v1 completion and final integration/hardening.
- **020-K** turns the accumulated A–J contracts into final implementation phases/packages, exact package criteria/evidence and agent assignment strategy.
- **020-L** performs the pre-implementation audit and Phase-021 handoff.

# Exit decision

**020-I — COMPLETE — PASS.**

The implementation program now has a complete cross-cutting verification architecture with all fifteen semantic scenarios preserved as executable evidence obligations and with migration, recovery, accessibility, performance and cost claims prevented from becoming undocumented implementation assumptions.

Next eligible:

> **020-J — v1 Scope, Whole-System Completion Criteria & Final Integration/Hardening Phase Design**

020-J is **NEXT ELIGIBLE / NOT AUTOMATICALLY AUTHORIZED**.
