---
type: Phase Start Gate
title: 020-A — Start Gate, Authority, Accepted Baseline & Autonomous-Development Method
description: "Opens Phase 020, verifies the accepted Phase-019 baseline and G0 handoff, establishes the final pre-implementation design boundary, validates the A–L subphase decomposition, and defines the autonomous-development/verification principles that later Phase-020 work must refine."
status: stable
tags: [phase-020, start-gate, autonomous-development, cursor, codex, mcp, verification, v1]
sources:
  - resource: README.md
  - resource: ../019-architecture-engineering-reentry/019-L-architecture-consolidation-acceptance-candidate-supersession-implementation-handoff.md
  - resource: ../canonical/architecture/accepted-architecture.md
  - resource: ../canonical/governance/implementation-program-delivery.md
  - resource: ../routing/implementation_program_framework.json
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/methodology/phase-lifecycle.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/methodology/agentic-development-governance.md
---

# Purpose

Open Phase 020 as the final pre-implementation design lifecycle and determine the logical work required before autonomous implementation may begin.

020-A is a start gate, not a coding phase.

# Entry verification

The exact Phase-019 closure baseline entering 020-A is:

~~~text
Phase 019                       COMPLETE — PASS
019-A..L                        COMPLETE
ADQ-001..010                    ACCEPTED
Q4R-001..004                    COMPLETE
whole architecture              ACCEPTED
G0 Architecture Accepted        SATISFIED

implementation framework        PLANNING_READY
package derivation allowed      true
active implementation packages  0
implementation execution        false
~~~

**Entry result: PASS.**

No unresolved Phase-019 architecture blocker prevents implementation-program design.

# Phase intention review

Phase 020 is not the implementation itself.

Its purpose is to produce the engineering control system and dependency-safe v1 roadmap under which implementation can later execute.

The phase must answer five broad questions:

1. **What should be built, and in what dependency order?**
2. **How should Cursor/Codex autonomously implement bounded work without gaining lifecycle authority?**
3. **How can running application behavior be exercised and observed independently through non-production infrastructure?**
4. **How is phase completion evaluated independently of the implementer's own tests and claims?**
5. **What exact integrated state constitutes a strong MUDAC v1 implementation?**

# Base-method adaptation

The Base lifecycle is adopted as a structural pattern, not copied mechanically.

Every later implementation phase should instantiate:

~~~text
Start Gate
  → Phase Definition
      + visible scope
      + visible success criteria
      + required evidence
  → explicit G2 implementation authorization
  → autonomous implementation
  → IMPLEMENTATION COMPLETE / EXIT REVIEW REQUESTED
  → public CI + independent hidden verification
  → independent code review
  → adversarial semantic/conformance review
  → repair loop if required
  → exact-SHA Exit Gate
  → COMPLETE
~~~

The implementer cannot self-authorize execution and cannot self-close the phase.

# Success-criteria visibility model

020-A accepts a hybrid evaluation model.

## Visible to the implementation agent

The implementation agent must receive:

- the real requirement;
- scope and exclusions;
- architecture/semantic constraints;
- visible success criteria;
- required evidence classes;
- affected scenarios;
- public checks and repository rules.

## Independently controlled

The evaluator may withhold:

- exact probe implementation;
- exact scenario data;
- failure timing/order;
- concurrency scheduling;
- hidden input combinations;
- detailed assertion values.

This avoids superficial test-targeting while preserving fair requirements.

**Hidden checks may not introduce hidden requirements.**

# Autonomous role model

Phase 020 will refine these logical roles:

| Role | Responsibility |
|---|---|
| **Implementer** | Performs only explicitly G2-authorized implementation work. Cursor or Codex may fill this role. |
| **Reviewer** | Independently reviews implementation/code/design fidelity. Prefer a different agent from the implementer where practical. |
| **Verifier** | Runs public and protected verification against the exact revision. |
| **Gatekeeper** | Integrates evidence and determines PASS / REPAIR REQUIRED / NOT READY. |
| **Authorizer** | Human/program authority that grants G2 or later release/production authority. |

Cursor and Codex are interchangeable candidates for roles rather than permanently assigned frontend/backend identities.

Role rotation is permitted.

# Non-production MCP design requirement

020-A accepts the MCP test-control plane as a required Phase-020 design workstream.

The target capability is:

~~~text
agent / private evaluator
        │
        ▼
non-production MCP test-control plane
        ├─ fixture plane
        ├─ action/browser plane
        ├─ observation plane
        └─ approved fault plane
        │
        ▼
real non-production MUDAC boundaries
~~~

Mandatory design properties:

- production target is impossible by configuration and authorization;
- ordinary application actions traverse normal IAM/CMD/application contracts;
- fixtures are synthetic and deterministic by default;
- health/metrics/traces/release SHA are observable;
- action-to-trace correlation is explicit;
- browser behavior can be tested through a real browser adapter where required;
- fault injection is bounded and non-production only;
- arbitrary SQL, shell, cloud administration and secret retrieval are not generic MCP tools;
- the hidden evaluator remains outside the MCP server and can use the same public control capabilities without exposing its exact tests.

020-D owns the detailed architecture.

# Autonomy circuit-breaker requirement

Later Phase-020 work must define mandatory stop/escalation conditions.

At minimum an autonomous agent must stop rather than improvise when it encounters:

- accepted semantic or architecture contradiction;
- destructive/ambiguous migration;
- production target or credential ambiguity;
- required secret/protected data;
- unexpected cross-package ownership conflict;
- repeated verifier failure suggesting a requirement/design mismatch;
- scope expansion beyond the authorized phase/package;
- inability to restore a deterministic clean test state;
- security issue whose safe resolution changes upstream authority.

# Evidence and phase-exit principle

A later implementation phase may close only at an exact Git revision after applicable:

- build/type/lint/static checks;
- unit/component evidence;
- integration/runtime evidence;
- scenario/end-to-end evidence;
- security/accessibility/recovery evidence;
- operational/deployment evidence where required;
- dependency/IaC/container/secret scans;
- hidden criteria-derived verification;
- independent code review;
- adversarial conformance review;
- documentation/current-authority reconciliation.

A green test suite alone is insufficient.

# v1 completion requirement

Phase 020 must design a final implementation phase whose primary purpose is **whole-system v1 integration, hardening and acceptance**, not feature accumulation.

That phase must reconcile:

- all implementation phases/packages;
- the accepted architecture;
- all 15 scenario seeds;
- security and disclosure;
- accessibility and responsive behavior;
- degraded/offline/recovery behavior;
- migration/restore;
- observability;
- representative performance;
- cost evidence;
- technical debt/blockers;
- final code and dependency review.

~~~text
v1 implementation complete
  != release candidate
  != production ready
~~~

G6/G7 remain separate later authorities.

# Dependency analysis and subphase plan

The work has the following dependency order:

~~~text
authority/baseline
  → substrate truth
  → agent execution controls
  → non-prod/MCP testability
  → implementation decomposition
  → phase/evidence contract
  → CI/supply-chain/evidence bundle
  → independent review/repair gates
  → cross-cutting verification mapping
  → v1 completion boundary
  → full roadmap/readiness
  → consolidation/exit
~~~

This produces the accepted Phase-020 A–L decomposition:

1. **020-A** — Start Gate, Authority, Accepted Baseline & Autonomous-Development Method.
2. **020-B** — Existing Substrate, Historical Implementation & Reuse Qualification.
3. **020-C** — Cursor/Codex Roles, Work Isolation, Context, Provenance & Autonomy Circuit Breakers.
4. **020-D** — Non-Production Environment, Synthetic Data, Observability & MCP Agent Test-Control-Plane Architecture.
5. **020-E** — Implementation Phase/Package Discovery, Dependency Graph, Parallelism & Sequencing.
6. **020-F** — Implementation Phase Contract, Visible Criteria, Evidence Classes & Hidden Evaluation Architecture.
7. **020-G** — CI/CD, Security, Supply Chain, Exact-SHA Verification & Evidence-Bundle Architecture.
8. **020-H** — Independent Code Review, Adversarial Review, Repair/Reopen & Exit-Gate Governance.
9. **020-I** — Migration, Recovery, Accessibility, Performance, Cost & Scenario Verification Design.
10. **020-J** — v1 Scope, Whole-System Completion Criteria & Final Integration/Hardening Phase Design.
11. **020-K** — Full Autonomous Implementation Roadmap, Agent Assignment Strategy, Phase/Package Definitions & Entry Readiness.
12. **020-L** — Consolidation, Pre-Implementation Audit, Exit Decision & Phase-021 Handoff.

**Decomposition result: ACCEPTED.**

# Completion evidence by subphase

| Subphase | Minimum completion evidence |
|---|---|
| 020-B | repository/static substrate inventory; six historical implementation candidates dispositioned for reuse/revision/reference/replace/defer |
| 020-C | role/branch/worktree/context/provenance/circuit-breaker model; collision and human-authority rules |
| 020-D | non-prod environment + MCP planes/trust boundary/tool classes/production denial/telemetry model |
| 020-E | implementation phase/package candidates and acyclic dependency graph; parallelism/shared-state analysis |
| 020-F | reusable phase contract; criteria visibility rules; verifier isolation; evidence-class mapping |
| 020-G | exact-SHA CI/scanning/supply-chain/evidence-bundle contract and protected verifier integration |
| 020-H | independent review/adversarial review/repair/reopen/exit state machine |
| 020-I | all 15 scenarios plus migration/recovery/accessibility/performance/cost mapped to later evidence |
| 020-J | explicit v1 boundary and final whole-system integration/hardening phase contract |
| 020-K | complete 021–0XX roadmap with dependencies, role strategy, package mappings and readiness |
| 020-L | full audit, clean exact-head CI, no hidden execution, Phase-021 handoff |

# Documentation / authority plan

Expected durable owners are not created prematurely.

Likely current owners to be established/refined later in Phase 020 include:

- autonomous implementation phase governance;
- non-production agent testing/MCP governance;
- verification/evidence and hidden-evaluator governance;
- implementation-program routing/control;
- v1 completion/acceptance contract.

Phase records preserve analysis; durable rules must end in their natural canonical/governance owners.

# Risks identified

Key Phase-020 design risks are:

- designing phases around existing folders rather than accepted authority;
- over-sharing exact acceptance probes and encouraging verifier gaming;
- hiding genuine requirements in private tests;
- giving MCP tools semantic bypass authority;
- allowing autonomous agents to infer production access;
- correlated implementer/reviewer failure;
- auto-advancing phases after a green CI run;
- creating giant long-lived branches that defeat reviewability;
- over-specifying late implementation phases before dependency evidence exists;
- confusing v1 implementation completion with release/production readiness;
- documentation/agent-rule bloat that harms retrieval.

Each risk has a dedicated downstream subphase.

# Implementation boundary

During Phase 020:

~~~text
repository governance/design edits   AUTHORIZED
implementation-program design        AUTHORIZED
package/phase derivation              AUTHORIZED
MUDAC domain implementation           NOT AUTHORIZED
G2 package execution                  NONE
production MCP deployment             FORBIDDEN
release/deployment                     NOT AUTHORIZED
~~~

No agent may interpret Phase-020 activity as blanket coding authorization.

# 020-A exit decision

**020-A — COMPLETE — PASS.**

Phase 020 is formally defined and active.

The A–L decomposition is accepted.

Next eligible:

> **020-B — Existing Substrate, Historical Implementation & Reuse Qualification**

020-B is **NEXT ELIGIBLE / NOT AUTOMATICALLY AUTHORIZED**.
