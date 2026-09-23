---
type: Phase Record
title: 020-F — Implementation Phase Contract, Visible Criteria, Evidence Classes & Hidden Evaluation Architecture
description: "Defines the reusable autonomous implementation phase/package contract, visible success-criterion and evidence schemas, E1-E7 claim boundaries, protected evaluator secrecy limits, anti-gaming rules, failure diagnostics, repair routing and exact-revision exit predicates without making proposed packages G1/G2 ready."
status: stable
tags: [phase-020, implementation-contract, success-criteria, evidence, hidden-evaluation, anti-gaming, verification]
sources:
  - resource: README.md
  - resource: 020-C-cursor-codex-roles-work-isolation-context-provenance-autonomy-circuit-breakers.md
  - resource: 020-D-nonproduction-environment-synthetic-data-observability-mcp-agent-test-control-plane-architecture.md
  - resource: 020-E-implementation-phase-package-discovery-dependency-graph-parallelism-sequencing.md
  - resource: ../canonical/governance/implementation-program-delivery.md
  - resource: ../canonical/governance/agentic-authority-scope.md
  - resource: ../canonical/governance/agentic-conformance.md
  - resource: ../routing/implementation_program_framework.json
  - resource: ../routing/phase020_implementation_package_discovery.json
  - resource: ../routing/phase020_implementation_phase_contract.json
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/001/purpose-success-contract.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/001/exit-review-template.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-23T11:19:00-05:00 }
---

# Purpose

Define the reusable contract by which a future Phase-021+ autonomous implementation phase can move explicitly planned packages through authorization, implementation, evidence review and exit without teaching the implementer the exact evaluator probes.

020-F preserves two goals simultaneously:

1. the Implementer must know what success actually means; and
2. the Implementer need not know the exact tests used to detect superficial or overfit implementations.

# Entry state

~~~text
PHASE 020 ACTIVE
020-A/B/C/D/E COMPLETE
020-F NEXT ELIGIBLE / USER AUTHORIZED

proposed packages                 15
G1-ready packages                 0
G2-authorized packages            0
active implementation packages    0
implementation execution          NOT AUTHORIZED
~~~

# Decision

**020-F — ACCEPT A VISIBLE-OBLIGATION / PROTECTED-PROBE IMPLEMENTATION CONTRACT.**

The governing rule is:

> **Hide the probe, never the requirement.**

An implementation phase exposes its real scope, constraints, normative success criteria, required evidence class/material boundary, mandatory scenario categories and normative thresholds.

The protected evaluator may keep the exact test source, fixtures, randomized values, timing, interleavings and probe composition private.

# Relationship to Base phase design

The implementation lifecycle retains the Base pattern:

~~~text
START GATE
    |
    v
PHASE DEFINITION
    |
    v
VISIBLE SUCCESS CRITERIA
    |
    v
G2 AUTHORIZATION
    |
    v
IMPLEMENTATION
    |
    v
EXIT REVIEW
~~~

MUDAC strengthens the exit side because autonomous implementation requires independent code review, protected verification, exact-revision evidence and security/conformance checks in addition to reviewing the visible success criteria.

# Phase versus package

An **implementation package** is a durable independently reviewable responsibility such as IMP-009 Evaluation.

An **implementation phase** is a delivery envelope that may contain one or more dependency-safe packages/work units.

A multi-package phase may receive execution authority only when every included package:

- is individually G1-complete;
- is explicitly named in the human G2 authorization set;
- has its predecessor/independence state satisfied;
- has no unresolved semantic/architecture blocker.

A phase identifier is not blanket authorization for packages not listed in its G2 record.

# Required implementation-phase definition

Before G2, an implementation phase defines at least:

- phase identity and purpose;
- included package IDs and package G1 state;
- exact entry baseline;
- scope and explicit exclusions;
- current semantic/architecture/engineering references;
- hard/integration/evidence dependencies;
- owned and serialized surfaces;
- Coordinator and role policy;
- declared work-unit graph;
- context-manifest rules;
- visible success criteria;
- evidence obligations;
- scenario obligations;
- security/privacy/disclosure impacts;
- migration/compatibility impacts;
- accessibility/degraded impacts;
- failure/recovery impacts;
- performance/cost obligations;
- required non-production evidence tiers;
- allowed external actions;
- circuit breakers;
- repair/escalation rules;
- rollback/recovery plan;
- known residual risks;
- explicit G2 authorization record;
- exit-gate contract.

# Package G1 contract

020-F defines the reusable G1 structure but does not promote the 15 discovered packages.

A package may be G1 only after its package-specific plan has:

- complete scope/exclusions;
- semantic/architecture/engineering traceability;
- dependency/serialized-surface mapping;
- instantiated visible success criteria;
- instantiated evidence obligations;
- scenario obligations;
- migration/security/accessibility/recovery/performance/cost classifications;
- compatibility/rollback plan;
- residual risks and reopen triggers;
- an implementation-phase planning owner/assignment.

G1 means **planned**, not **authorized**.

# Visible success criteria

Every criterion has a stable ID and includes:

~~~text
criterion ID
statement
criterion type
required / optional disposition
authority references
evidence floor
material evidence boundary
verification visibility
failure class
applies-to package/phase/work units

optional:
  visible normative threshold
  environment tiers
  scenario references
  dependency references
~~~

The statement is outcome/obligation-oriented.

Poor criterion:

> Pass `evaluation-finalize-hidden.spec.ts`.

Better criterion:

> A consequential Evaluation Finalization retry after an uncertain response resolves to one committed logical operation and returns current authoritative result identity without duplicating evaluation weight.

The criterion tells the Implementer what must be true without revealing how the evaluator will perturb timing.

# Criterion types

The reusable vocabulary includes semantic behavior, functional behavior, authority/security/disclosure, data/history/migration, accessibility/interaction, failure/recovery, concurrency/idempotency, performance/capacity, cost/operability, observability, compatibility, static quality, and documentation/traceability.

020-I will instantiate the cross-cutting requirements against specific packages.

# Normative thresholds are visible

020-F does **not** hide a real product or acceptance target under the label of hidden testing.

If a package must satisfy a normative limit—such as a defined accessibility target, supported browser contract, recovery condition, accepted capacity floor, cost envelope, timeout requirement or compatibility constraint—the normative threshold must be visible before implementation.

The evaluator may hide which exact cases hit the threshold.

It may not invent the threshold privately.

Non-normative harness timeouts used only to keep test infrastructure from hanging may remain private.

# Evidence classes

020-F retains E1–E7 but gives them claim boundaries.

## E1 — documentation/static

Supports documentation conformance, type/lint/format, static analysis and generated-contract integrity.

E1 alone cannot prove runtime/provider/production behavior.

## E2 — unit/component

Supports pure logic, isolated component behavior and deterministic local contracts.

E2 alone cannot prove real PostgreSQL/provider/whole-journey behavior.

## E3 — integration/runtime

Supports real selected database semantics, material provider/runtime contracts, transaction/concurrency boundaries and deployed non-production runtime behavior.

## E4 — scenario/end-to-end

Supports consequential cross-boundary workflows and integrated browser/API journeys.

## E5 — security/accessibility/recovery

Supports authority/disclosure/abuse behavior, accessibility and adverse failure/recovery/concurrency evidence.

## E6 — operational/deployment

Supports migration, rollout, restore, load, observability and disaster-recovery evidence.

## E7 — production

Supports authorized production behavior/operations.

Ordinary implementation package completion does not require E7 unless a later G7 contract explicitly says otherwise.

# Evidence floor

Each visible success criterion names its minimum material evidence boundary.

A package may use stronger/composed evidence.

It cannot satisfy a criterion with weaker evidence merely because that evidence is cheaper.

Examples:

~~~text
pure ranking function
  E2 may be sufficient

PostgreSQL optimistic-concurrency behavior
  requires E3

Judge phone workflow and lost-response reconciliation
  requires E4/E5 composition

restore from authoritative backup
  requires E6

actual production behavior
  requires E7
~~~

# Evidence obligation

An evidence obligation links one or more criteria to evidence class, claim, material boundary, environment tier, required/conditional state, exact-revision rule, reproducibility expectation, public/protected visibility, evidence producer, and retained evidence reference.

020-G will define the exact evidence-bundle implementation.

# Public versus protected verification

## Public before implementation

The Implementer sees every real requirement, scope/exclusions, current authority references, every success criterion, normative thresholds, evidence floors/material boundaries, required environment tiers, mandatory scenario categories, security/accessibility/recovery/compatibility obligations, circuit breakers and exit predicates.

## Protected evaluator detail

The evaluator may conceal:

- test source;
- internal probe names;
- exact fixture seeds;
- exact sample values;
- randomized generation;
- precise concurrency interleavings;
- precise fault timing;
- request ordering;
- mutation variants;
- probe selection/sampling distribution;
- evaluator-only credentials/infrastructure;
- non-normative harness timeouts.

## Protected evaluator may never conceal

- a semantic/product requirement;
- accepted architecture rule;
- normative acceptance threshold;
- required evidence class/material boundary;
- required environment tier;
- mandatory scenario category;
- security/disclosure property;
- accessibility target;
- compatibility obligation;
- migration/recovery obligation;
- normative performance/cost requirement;
- a known pre-existing blocker.

A hidden test that relies on one of those undisclosed items is invalid evaluator behavior, not an implementation defect.

# Protected evaluator architecture

The protected evaluator is separate from the ordinary Implementer runtime/context.

It evaluates the exact candidate SHA, derives probes only from the visible contract, may use the non-production MCP/test-control capabilities, cannot use production, cannot modify candidate source, cannot grant G2, cannot authorize the next phase, cannot use a secret semantic bypass, and cannot count fixture seeding as evidence for a bypassed command.

The evaluator's internal test corpus is not required in the Implementer's context.

# Anti-gaming contract

An implementation cannot obtain PASS by detecting the evaluator rather than satisfying the obligation.

Prohibited strategies include:

- evaluator-specific product behavior;
- hidden fixture/seed hard-coding;
- giving synthetic actors bypass authority;
- disabling mandatory tests/scanners;
- fabricating or rewriting evidence;
- creating test-only domain semantics;
- treating hidden-probe exfiltration as the solution.

Ordinary test seams are allowed when they preserve the same semantic behavior and exist to make material boundaries controllable.

# Evaluation outcomes

Each required criterion resolves to:

~~~text
PASS
FAIL
BLOCKED
INCONCLUSIVE
NOT_APPLICABLE_WITH_APPROVED_RATIONALE
~~~

For a required criterion, FAIL, BLOCKED and INCONCLUSIVE all fail closed for exit.

NOT_APPLICABLE requires explicit governed rationale; an Implementer cannot self-declare it to remove a difficult criterion.

# Protected failure diagnostics

A hidden evaluator failure must reveal enough to support a legitimate repair loop without turning the hidden test into a public answer key.

Diagnostics identify at least:

- criterion ID;
- obligation/failure category;
- candidate SHA;
- evidence/environment boundary;
- enough repair direction to understand the violated visible obligation.

It may retain the exact hidden fixture, seed, probe source, interleaving or fault timing when revealing those details would destroy the probe's anti-overfitting value.

When practical, the reviewer/verifier should reduce a hidden failure to a minimal public reproduction that still tests the same visible requirement.

# Failure taxonomy

020-F distinguishes:

- implementation defect;
- integration/compatibility defect;
- security/authority defect;
- accessibility/interaction defect;
- migration/recovery defect;
- performance/cost defect;
- observability/evidence defect;
- test-harness/evaluator defect;
- environment/provider defect;
- nondeterministic evidence;
- requirement/architecture contradiction.

This matters because not every red result should send an Implementer into the same repair loop.

A requirement/architecture contradiction invokes the 020-C circuit breaker rather than encouraging the agent to code around it.

# Exit contract

A future implementation phase can close only against a frozen exact candidate revision.

Its mandatory exit predicates include:

~~~text
visible criteria satisfied
required evidence obligations satisfied
public CI clean
declared protected evaluation clean
independent code review clean
adversarial conformance review clean
evidence bundle complete
traceability/docs current
no unresolved blocker
~~~

The Implementer cannot self-close.

A pre-authorized Gatekeeper may record COMPLETE only after every mandatory predicate passes.

The next phase becomes **NEXT ELIGIBLE / NOT AUTHORIZED**.

# 020-F effect on IMP-001..015

020-F establishes the reusable schema.

It deliberately does **not** invent all package-specific success criteria now.

Those require 020-I's final scenario/migration/recovery/accessibility/performance/cost mapping, 020-K's final phase/package definitions and assignments, and package-specific traceability from accepted architecture/current semantics.

Therefore after 020-F:

~~~text
proposed packages       15
G1-ready packages       0
G2 packages             0
active packages         0
~~~

This avoids a false G1 transition caused merely by defining the template.

# Carry-forward

- **020-G** turns the evidence obligation into exact-SHA CI/scanning/evidence bundles and protected-evaluator execution.
- **020-H** defines independent review, adversarial review, repair/reopen and Gatekeeper behavior.
- **020-I** instantiates cross-cutting evidence/scenario obligations.
- **020-J** defines the final integrated v1 completion contract.
- **020-K** instantiates package criteria, completes G1-ready package plans and groups them into implementation phases.

# Exit decision

**020-F — COMPLETE — PASS.**

MUDAC now has a reusable implementation-phase/package contract that exposes genuine success obligations while protecting evaluator probes from superficial optimization.

Next eligible:

> **020-G — CI/CD, Security, Supply Chain, Exact-SHA Verification & Evidence-Bundle Architecture**

020-G is **NEXT ELIGIBLE / NOT AUTOMATICALLY AUTHORIZED**.
