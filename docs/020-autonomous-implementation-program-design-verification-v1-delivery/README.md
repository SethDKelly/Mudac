---
type: Phase Definition
title: Phase 020 — Autonomous Implementation Program Design, Verification Architecture & v1 Delivery Planning
description: "Final pre-implementation phase that converts the accepted MUDAC architecture into a dependency-safe autonomous development program for Cursor/Codex, including agent roles, non-production MCP test control, visible criteria with independent hidden verification, exact-SHA CI/review exit gates, evidence contracts, and a strong v1 completion boundary."
status: stable
tags: [phase-020, implementation-design, autonomous-development, cursor, codex, mcp, verification, v1]
sources:
  - resource: ../canonical/architecture/accepted-architecture.md
  - resource: ../canonical/governance/implementation-program-delivery.md
  - resource: ../019-architecture-engineering-reentry/019-L-architecture-consolidation-acceptance-candidate-supersession-implementation-handoff.md
  - resource: ../routing/implementation_program_framework.json
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/methodology/phase-lifecycle.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/methodology/agentic-development-governance.md
---

# Phase 020 — Autonomous Implementation Program Design, Verification Architecture & v1 Delivery Planning

## Status

~~~text
PHASE 020 ACTIVE
020-A/B COMPLETE
020-C NEXT ELIGIBLE

accepted whole architecture       true
G0 Architecture Accepted          SATISFIED

active implementation packages    0
domain implementation execution   NOT AUTHORIZED
release authority                 NOT GRANTED
production authority              NOT GRANTED
~~~

Phase 020 is the **final pre-implementation design phase**.

It designs how MUDAC v1 will be implemented autonomously and verified independently. It does not implement application/domain features.

# Purpose

Convert the accepted Phase-019 architecture into an implementation program that Cursor, Codex and repository CI can execute safely without allowing agent convenience, visible tests, existing source layout or historical implementation to redefine MUDAC authority.

Phase 020 must design:

- autonomous implementation phase/package boundaries and dependency order;
- Cursor/Codex implementer/reviewer role assignment and work isolation;
- the non-production MCP agent test-control plane;
- deterministic synthetic fixtures and test-environment semantics;
- visible success criteria plus independently controlled exact acceptance probes;
- CI/CD, security, supply-chain and exact-SHA verification;
- independent code review and adversarial conformance review;
- repair, reopen and architecture-escalation paths;
- evidence bundles and scenario traceability;
- migration, recovery, accessibility, performance and cost verification;
- a complete implementation roadmap terminating in a strong MUDAC v1 whole-system integration/hardening phase.

# Method

Phase 020 reuses the proven Base-style phase lifecycle:

~~~text
Start Gate
  → Phase Definition
  → Visible Success Criteria / Evidence Contract
  → Autonomous Work
  → Independent Verification / Review
  → Exit Gate
  → next phase eligible
~~~

For later implementation phases, the implementer may declare **IMPLEMENTATION COMPLETE / EXIT REVIEW REQUESTED**, but may not mark its own phase COMPLETE.

Completion belongs to the exit gate at an exact repository revision.

# Verification visibility principle

Agents receive the real requirements.

Agents may see:

- phase purpose and scope;
- architecture/semantic obligations;
- visible success criteria;
- evidence classes;
- affected scenario obligations;
- public CI expectations.

Independent evaluation may keep private:

- exact input values;
- fault timing/order;
- hidden scenario combinations;
- acceptance probe implementation;
- detailed assertions.

Hidden verification may test generality but **must never introduce a requirement absent from visible authority**.

# Non-production MCP test-control principle

Phase 020 will design a non-production MCP control plane that allows agents and independent evaluators to:

- create deterministic synthetic fixtures;
- exercise real application/user actions through normal application boundaries;
- drive supported browser journeys;
- inspect health, metrics, traces and release identity;
- correlate test actions with command/trace identifiers;
- inject explicitly approved non-production faults.

The MCP plane must not:

- target production;
- become an alternate semantic authority;
- write arbitrary database rows;
- grant Access directly;
- finalize/publish/declare through test-only semantic bypasses;
- expose arbitrary shell/cloud/secret access.

Ordinary behavior testing must traverse the same IAM/CMD/PST/application contracts used by the application.

# High-level decomposition

| Subphase | Purpose |
|---|---|
| **020-A** | Start Gate, Authority, Accepted Baseline & Autonomous-Development Method |
| **020-B** | Existing Substrate, Historical Implementation & Reuse Qualification — **COMPLETE — PASS** |
| **020-C** | Cursor/Codex Roles, Work Isolation, Context, Provenance & Autonomy Circuit Breakers — **NEXT ELIGIBLE** |
| **020-D** | Non-Production Environment, Synthetic Data, Observability & MCP Agent Test-Control-Plane Architecture |
| **020-E** | Implementation Phase/Package Discovery, Dependency Graph, Parallelism & Sequencing |
| **020-F** | Implementation Phase Contract, Visible Criteria, Evidence Classes & Hidden Evaluation Architecture |
| **020-G** | CI/CD, Security, Supply Chain, Exact-SHA Verification & Evidence-Bundle Architecture |
| **020-H** | Independent Code Review, Adversarial Review, Repair/Reopen & Exit-Gate Governance |
| **020-I** | Migration, Recovery, Accessibility, Performance, Cost & Scenario Verification Design |
| **020-J** | v1 Scope, Whole-System Completion Criteria & Final Integration/Hardening Phase Design |
| **020-K** | Full Autonomous Implementation Roadmap, Agent Assignment Strategy, Phase/Package Definitions & Entry Readiness |
| **020-L** | Phase-020 Consolidation, Pre-Implementation Audit, Exit Decision & Phase-021 Handoff |

The decomposition is dependency-driven rather than aesthetically fixed. 020-A has reviewed and accepted this A–L structure as the current Phase-020 plan; later work may reopen it if evidence demonstrates a material dependency mistake.

# Entry criteria

Phase 020 may begin only because:

- Phase 019 is COMPLETE;
- ADQ-001..010 are accepted;
- whole architecture is accepted;
- G0 is satisfied;
- historical architecture candidates are explicitly superseded/retained;
- the implementation framework is PLANNING_READY;
- active implementation package count is zero;
- implementation execution is unauthorized.

# Explicit exclusions

Phase 020 does not authorize:

- MUDAC domain feature implementation;
- production MCP/test-control deployment;
- package G2 execution;
- release/deployment;
- production data use for ordinary fixtures;
- production credentials or production mutation;
- speculative technology changes that contradict accepted architecture.

Small repository-governance changes required to define or validate Phase 020 itself are permitted.

# Durable outputs expected

By exit, Phase 020 should establish durable current authority for:

- the autonomous implementation phase contract;
- agent role/isolation/provenance rules;
- MCP/non-production test-control architecture;
- verification visibility and hidden-evaluator trust boundary;
- evidence-bundle and exact-SHA exit requirements;
- independent/adversarial review protocol;
- implementation phase/package catalog and dependency graph;
- v1 completion matrix and final integration/hardening phase;
- Phase-021 start gate and execution-authorization boundary.

# Exit criteria

Phase 020 exits only when:

1. 020-A..L are complete or explicitly dispositioned;
2. accepted architecture remains unchanged or any required re-entry is closed;
3. the autonomous implementation phase contract is current and machine-checkable where practical;
4. the implementation roadmap is dependency-safe and acyclic;
5. all 15 scenario seeds and applicable ENG/IPG obligations map into implementation/verification work;
6. Cursor/Codex roles, isolation and circuit breakers are explicit;
7. the non-production MCP/test-control plane is fully designed with a hard production boundary;
8. visible criteria and independent hidden-verification rules are coherent;
9. CI/scanning/code-review/adversarial-review/repair gates are explicit;
10. v1 scope and final whole-system completion phase are explicit;
11. implementation evidence and residual risks have owners;
12. no domain implementation package has been executed;
13. exact-head repository conformance and CI are clean;
14. Phase 021 receives an explicit start-gate handoff.

# Exit semantics

A successful Phase-020 exit means:

> **MUDAC has a complete autonomous implementation design and may begin Phase 021 under its start gate.**

It does not mean:

- implementation is already complete;
- the first package is automatically G2-authorized;
- v1 is a release candidate;
- production is authorized.


## 020-B qualification result

020-B found a substantial reusable non-domain bootstrap, but not an already-implemented MUDAC application. Preserve sound Node/TypeScript/pnpm, PostgreSQL, CI and OpenTofu scaffolding; revise runtime/testing seams as responsibilities arrive; replace/merge the historical six-owner topology into the accepted five-owner BND topology; keep all six historical implementation documents as REUSE_WITH_REVISION evidence; and preserve zero active packages / zero G2 execution authority.

Machine evidence: `docs/routing/phase020_substrate_reuse_qualification.json`.
