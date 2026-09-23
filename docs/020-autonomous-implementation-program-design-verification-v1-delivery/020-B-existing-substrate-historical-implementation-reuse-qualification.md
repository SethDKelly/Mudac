---
type: Phase Record
title: 020-B — Existing Substrate, Historical Implementation & Reuse Qualification
description: "Qualifies the live MUDAC repository/runtime/IaC/testing bootstrap and six retained historical implementation candidates against the accepted DRV/BND/PST/IAM/CMD/RCV/ART/CLT/RUN architecture, classifying material as reuse-as-is, reuse-with-revision, reference-only, replace, or defer before implementation-phase derivation."
status: stable
tags: [phase-020, substrate, implementation, reuse, qualification, source-topology, toolchain, testing, infrastructure]
sources:
  - resource: README.md
  - resource: ../canonical/architecture/accepted-architecture.md
  - resource: ../canonical/architecture/application-ownership-boundaries.md
  - resource: ../canonical/architecture/persistence-history-recovery.md
  - resource: ../canonical/architecture/identity-access-authority.md
  - resource: ../canonical/architecture/runtime-platform-operations.md
  - resource: ../canonical/governance/implementation-program-delivery.md
  - resource: ../canonical/implementation/implementation-foundation.md
  - resource: ../canonical/implementation/verification-strategy.md
  - resource: ../canonical/implementation/source-topology.md
  - resource: ../canonical/implementation/runtime-delivery-bootstrap.md
  - resource: ../canonical/implementation/persistence-history-projection.md
  - resource: ../canonical/implementation/identity-authentication-access-session.md
  - resource: ../routing/downstream_candidate_qualification.json
  - resource: ../routing/phase020_substrate_reuse_qualification.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-23T00:55:00-05:00 }
---

# Purpose

Determine what MUDAC already has that the autonomous v1 implementation program should preserve, revise, replace, use only as historical evidence, or defer.

020-B prevents two opposite errors:

1. rebuilding sound non-domain scaffolding merely because Phase 019 refreshed architecture; and
2. treating old executable scaffolding or historical Phase-006/008 implementation plans as current authority merely because they already exist.

# Entry state

~~~text
PHASE 020 ACTIVE
020-A COMPLETE
020-B NEXT ELIGIBLE / USER AUTHORIZED

whole architecture               ACCEPTED
G0                               SATISFIED
active implementation packages   0
implementation execution         NOT AUTHORIZED
~~~

Exact start baseline:

> 09411c8d1685c4a5abcace7dbc23fcefb7498f62

# Qualification classes

020-B uses five dispositions.

| Class | Meaning |
|---|---|
| **REUSE_AS_IS** | Keep the current substrate/structure as the Phase-021+ starting point. Later extension is expected, but no prerequisite replacement is required. |
| **REUSE_WITH_REVISION** | Preserve meaningful work, but repair known architecture, lifecycle, security, verification, ownership or provider mismatch before depending on it. |
| **REFERENCE_ONLY** | Retain for rationale/comparison; do not carry its concrete realization into the new implementation program. |
| **REPLACE** | Current realization conflicts materially with accepted architecture or implementation-program needs and must be replaced/merged before use. |
| **DEFER** | No justified decision/implementation should be made yet; later evidence/package scope owns it. |

A historical document receiving REUSE_WITH_REVISION does not become current authority. It remains evidence until Phase 020 promotes durable conclusions into new/current implementation governance.

# Live executable substrate inventory

At the 020-B baseline, the repository contains:

~~~text
13 pnpm workspace packages

apps/
  api       Fastify /healthz bootstrap
  web       React + Vite + Router + Query shell
  worker    process/lifecycle bootstrap

packages/
  application
  foundation
  projections
  test-support
  modules/
    competition
    identity-access
    judging-operations
    evaluation
    outcomes
    external-representation

local dependency
  PostgreSQL 17 Alpine via Docker Compose

testing/config
  Vitest configured
  Playwright configured
  zero authored *.test/*.spec files
  empty tests/e2e placeholder

infrastructure
  OpenTofu roots:
    nonproduction/us-east-2
    production/us-east-2
    recovery/us-east-1
  remote-state backend examples
  no application AWS resources yet

CI
  Knowledge Validation
  Implementation Verification
  CodeQL
  Dependabot configuration
~~~

No migration file exists.

No Kysely, node-postgres, AWS SDK, Cognito client, Testcontainers, accessibility library or OpenTelemetry package is currently installed.

No application-domain schema, repository, command, Access implementation, browser workflow, provider adapter, observability pipeline, deploy workflow or non-production MCP server exists.

This is a **bootstrap**, not a partially completed domain application.

# Live substrate qualification

| Substrate | Disposition | 020-B rationale |
|---|---|---|
| Node 24 + TypeScript 6 + pnpm 11 workspace/lockfile | **REUSE_AS_IS** | Executable, strict, reproducible and compatible with accepted container/browser architecture. Version upgrades remain ordinary evidence-gated maintenance. |
| strict TypeScript / ESLint / Prettier baseline | **REUSE_AS_IS** | Strong static-quality foundation with no semantic coupling. |
| Fastify API composition root and /healthz | **REUSE_WITH_REVISION** | Useful server host/bootstrap. Keep the root; later phases must add explicit transport contracts, readiness/semantic health and accepted application composition without making Fastify domain architecture. |
| React/Vite/Router/Query browser shell | **REUSE_WITH_REVISION** | Useful browser substrate with no conflicting domain behavior. Later CLT implementation must add actual routing/state/accessibility/degraded semantics and verify whether every library remains justified. |
| worker process bootstrap | **REUSE_WITH_REVISION** | RUN-008 accepts bounded workers, but current heartbeat is only a process shell. Actual SQS/idempotent work must be phase-derived. |
| `application`, `foundation`, `projections`, `test-support` package seams | **REUSE_WITH_REVISION** | The roles remain useful, but exact public contracts/dependencies must be re-derived from BND/PST/CMD and the autonomous test architecture. |
| six historical authoritative module packages | **REPLACE / MERGE WHERE REQUIRED** | BND-002 now accepts five modules. `judging-operations` cannot remain an independent authoritative module; its relevant implementation responsibility must merge into the accepted Evaluation owner. Other package identities/layout remain implementation questions rather than architecture facts. |
| dependency-cruiser package/module rules | **REUSE_WITH_REVISION** | Mechanism is valuable; six-module dependency assumptions are stale and must be regenerated from current BND-001..012. |
| local PostgreSQL Docker Compose | **REUSE_AS_IS** | PST selects PostgreSQL-compatible authority; local Compose is explicitly non-production and useful for development/integration. It does not select production engine patch/version. |
| Vitest configuration | **REUSE_WITH_REVISION** | Baseline runner is useful, but there are currently zero tests and later evidence classes must drive actual coverage. |
| Playwright configuration | **REUSE_WITH_REVISION** | Browser harness is useful; current desktop-Chromium-only empty suite cannot satisfy CLT/accessibility/shared-device/mobile evidence. |
| Knowledge Validation workflow | **REUSE_AS_IS** | Mature repository/authority conformance gate; remains distinct from product runtime evidence. |
| CodeQL workflow | **REUSE_AS_IS** | Useful JS/TS static-security baseline; does not replace behavioral security evidence. |
| Implementation Verification workflow | **REUSE_WITH_REVISION** | Strong exact-revision baseline for workspace/IaC checks; later phases must add real implementation evidence, scanners/evidence bundles and protected evaluator integration without turning one workflow into all evidence. |
| Dependabot npm/Actions configuration | **REUSE_AS_IS** | Useful supply-chain input. Configuration does not prove zero alerts/findings. |
| OpenTofu environment roots and S3-backend pattern | **REUSE_AS_IS AS SKELETON** | Environment/Region split matches RUN accepted topology and remains resource-light. Application resources, roles, networking, edge, data and recovery still need implementation. |
| `infra/modules/` placeholder | **REUSE_AS_IS AS LOCATION** | RUN capability modules may be added here when concrete resources exist; no speculative module set should be generated in advance. |
| `.env.example` | **REUSE_WITH_REVISION** | Good local bootstrap, but future configuration/secrets/test-control variables require typed/bounded treatment and production-safe separation. |
| empty `tests/e2e` location | **REUSE_AS_IS AS LOCATION** | Appropriate place for cross-system public tests; no verification credit exists until actual scenarios are implemented. |

# Critical topology mismatch — six historical packages vs five accepted owners

The historical implementation source graph contains:

~~~text
competition
identity-access
judging-operations
evaluation
outcomes
external-representation
~~~

BND-002 accepts:

~~~text
Competition Context
Identity & Access
Evaluation
Outcomes & Officiality
External Representation
~~~

The substantive change is not cosmetic.

The accepted Evaluation owner contains Panel, Evaluation Occurrence, Evaluation Obligation, Rubric and Scorecard.

The historical split placed portions of this authority in separate `judging-operations` and `evaluation` packages.

020-B therefore concludes:

> **The existing six-module dependency topology is not reusable as current authority.**

Before domain implementation, 020-E/K must derive the actual five-owner source/package realization.

Likely reuse of existing files/directories is allowed, but no package name or folder is protected merely because it exists.

# Historical implementation candidate qualification

All six retained implementation documents remain suspended evidence.

## 1. implementation-foundation.md

**Disposition: REUSE_WITH_REVISION.**

Retain:

- TypeScript/Node/pnpm baseline;
- strict static-quality posture;
- explicit transport contracts;
- reproducible lockfile/dependency discipline;
- OpenTofu direction;
- layered scanning;
- merge/release/production authority separation.

Revise:

- six-module/stale architecture references;
- old Phase-008/009 authorization language;
- Kysely/pg and other not-yet-installed mechanisms from “accepted implementation” into Phase-020-derived selections unless independently reaccepted;
- CI/review model to include autonomous roles, exact-SHA exit evidence and protected verification.

## 2. verification-strategy.md

**Disposition: REUSE_WITH_REVISION — HIGH-VALUE INPUT.**

Retain deterministic synthetic fixtures, real PostgreSQL where SQL semantics matter, external-provider fake plus targeted real nonproduction evidence, security/accessibility/concurrency/recovery behavioral testing, Playwright for consequential browser journeys, explicit flaky-test discipline and the distinction between revision evidence and production certification.

Add/repair:

- E1..E7 evidence-class terminology;
- non-production MCP action/observation/fault plane;
- protected hidden evaluator;
- implementer/reviewer separation;
- exact-SHA evidence bundles;
- current DRV/BND/PST/IAM/CMD/RCV/ART/CLT/RUN references;
- all 15 Phase-016 scenario seeds.

## 3. source-topology.md

**Disposition: REUSE_WITH_REVISION — MANDATORY OWNERSHIP REPAIR.**

Retain deployable apps as composition roots, restrictive public/private seams, application coordination above owners, non-authoritative projections, small business-neutral foundation, browser/server separation, test-support isolation, dependency-cruiser enforcement and no circular production dependencies.

Replace/rederive the six authoritative modules, old dependency allowlist, old rule-family references and any physical package identity that conflicts with BND-002.

This document cannot be promoted unchanged.

## 4. runtime-delivery-bootstrap.md

**Disposition: REUSE_WITH_REVISION; UNDERLYING EXECUTABLE BOOTSTRAP MOSTLY REUSE_AS_IS.**

Its repository-fact inventory remains substantially accurate: Node/pnpm/TypeScript workspace, Fastify/React/Vite shell, local PostgreSQL, CI workflows, OpenTofu environment roots and empty domain seams.

Revise the narrative before reuse as current authority because the old six-module topology is stale, historical 006/008 handoffs are closed, RUN-001..026 now own AWS runtime truth and Phase 020/021+ own autonomous implementation execution.

## 5. persistence-history-projection.md

**Disposition: REUSE_WITH_REVISION.**

Strongly reusable concepts include one PostgreSQL authority, owner-local persistence adapters, mutable current vs immutable committed history, append-stable Provenance, durable commit-coupled asynchronous propagation, rebuildable projections, explicit forward migrations, migration locking/checksum/compatibility and real-PostgreSQL integration evidence.

Mandatory re-derivation includes:

- historical schema/module count and names;
- obsolete Outcome Revision assumptions identified in Phase 018;
- exact Kysely/node-postgres/migration-runner selection;
- exact physical table/column layout;
- exact retention values.

PST-001..016 are authoritative; this candidate is a physical-pattern input.

## 6. identity-authentication-access-session.md

**Disposition: REUSE_WITH_REVISION — STRONG ALIGNMENT.**

Phase 019 subsequently accepted several compatible mechanisms:

- Cognito User Pools behind an application adapter;
- stable application-owned Identity;
- Competition-scoped Participation;
- current contextual Access;
- opaque first-party server session;
- initial relational session backing;
- separation of technical/operator authority.

Still revise historical rule-family references and Phase-008 boundaries, and rederive exact table shapes, token/session durations, provider SDK/configuration and invitation realization.

# Historical candidate summary

~~~text
historical implementation candidates          6

REUSE_WITH_REVISION                            6
REUSE_AS_IS document promotion                 0
REFERENCE_ONLY                                 0
REPLACE entire document                        0
DEFER entire document                          0

automatic current-authority promotion          0
~~~

A historical document is not promoted as-is merely because many of its ideas survive.

# Current provider/runtime alignment

Phase 019 materially reduces uncertainty that existed in Phase 018:

- AWS is selected;
- ECS/Fargate is selected;
- RDS PostgreSQL Multi-AZ DB instance is selected;
- Cognito User Pools is selected;
- S3/SQS are selected where ART/RUN require them;
- PostgreSQL-backed first-party sessions are selected initially;
- us-east-2 active and us-east-1 cold recovery are selected.

The existing AWS/PostgreSQL/Cognito-oriented historical plans are therefore more relevant than they were at Phase 018.

Provider capability selection still does not prove exact SDK/library choice, resource configuration, runtime behavior, deployment correctness, security behavior, recovery behavior or cost/performance adequacy.

# Repository-administration qualification

Current GitHub evidence at 020-B:

~~~text
repository rulesets endpoint      []
main branch protection read       unavailable to current GitHub integration (403)
workflow checks                   present
~~~

Workflow existence may be reused, but enforced merge policy must **not** be claimed.

020-G must retain repository-admin enforcement as an external configuration/evidence obligation. Autonomous development must not rely on prompt instructions as the only merge/security boundary.

# Gaps that Phase 020 must design around

The retained substrate has no implementation yet for:

- accepted five-owner domain topology;
- migrations/schema/history/Provenance/outbox;
- command/idempotency/concurrency/reconciliation;
- Cognito/Identity/Participation/Access/session behavior;
- RCV offline/local-Draft behavior;
- Artifact/Publication behavior;
- substantive browser journeys;
- synthetic fixture factory;
- MCP test-control plane;
- OpenTelemetry/semantic observability;
- AWS application resources;
- deployment/OIDC roles;
- hidden evaluator;
- independent autonomous code-review evidence;
- accessibility automation/manual evidence;
- load/failover/restore exercises.

These are inputs to 020-C..K and the later implementation roadmap.

# Reuse constraints handed to 020-C and 020-E

020-B establishes:

1. **Preserve working scaffolding unless a later phase has evidence to replace it.**
2. **Do not preserve the six-module semantic topology.**
3. **Do not let existing directories define implementation packages.**
4. **Do not promote any historical implementation document wholesale.**
5. **Translate historical rule references through current authority before reuse.**
6. **Treat uninstalled/planned libraries as hypotheses, not existing substrate.**
7. **Keep external/provider behavior behind application-owned boundaries.**
8. **Keep local/nonproduction/production authority distinct.**
9. **Do not claim GitHub merge protection from workflow existence.**
10. **Add MCP/testing foundations without semantic bypass authority.**

# Phase-020 impact

020-E must derive implementation phases/packages from:

~~~text
accepted five-owner architecture
+
qualified reusable technical bootstrap
+
new autonomous-development/test infrastructure needs
+
scenario/evidence obligations
~~~

—not from the existing 13-workspace layout.

# Implementation boundary verification

After 020-B:

~~~text
Phase 020                       ACTIVE
020-A/B                         COMPLETE
020-C                           NEXT ELIGIBLE

historical implementation docs  6 / 6 QUALIFIED
active implementation packages  0
G2 authorizations               0
domain implementation           NOT AUTHORIZED
~~~

No code/runtime feature implementation was authorized or performed.

# Exit decision

**020-B — COMPLETE — PASS.**

The repository contains a substantial reusable non-domain bootstrap, but the historical six-module source topology and all six implementation candidates require deliberate revision before becoming current implementation authority.

Next eligible:

> **020-C — Cursor/Codex Roles, Work Isolation, Context, Provenance & Autonomy Circuit Breakers**

020-C is **NEXT ELIGIBLE / NOT AUTOMATICALLY AUTHORIZED**.
