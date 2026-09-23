---
type: Phase Record
title: 020-C — Cursor/Codex Roles, Work Isolation, Context, Provenance & Autonomy Circuit Breakers
description: "Defines MUDAC's tool-neutral autonomous implementation operating model: human G2 authority, coordinator-bounded delegation, Cursor/Codex role portability, isolated worktrees/branches, minimum-sufficient context manifests, technical agent provenance, shared-writer serialization, repair boundaries, and fail-closed autonomy circuit breakers."
status: stable
tags: [phase-020, autonomous-development, cursor, codex, worktrees, roles, provenance, context, circuit-breakers, isolation]
sources:
  - resource: README.md
  - resource: 020-B-existing-substrate-historical-implementation-reuse-qualification.md
  - resource: ../canonical/governance/agentic-authority-scope.md
  - resource: ../canonical/governance/agent-workflow-portability.md
  - resource: ../canonical/governance/agent-context.md
  - resource: ../canonical/governance/implementation-program-delivery.md
  - resource: ../routing/agentic_action_policy.json
  - resource: ../routing/agent_tool_compatibility.json
  - resource: ../routing/autonomous_implementation_operating_model.json
  - resource: https://openai.com/index/introducing-the-codex-app/
  - resource: https://openai.com/index/running-codex-safely/
  - resource: https://cursor.com/docs/configuration/worktrees
  - resource: https://cursor.com/docs/rules
generated: { by: openai/gpt-5.6-sol, at: 2026-09-23T01:15:00-05:00 }
---

# Purpose

Define how autonomous coding agents may work inside the future MUDAC implementation program without turning agent orchestration, provider features, green CI or repository write access into lifecycle or semantic authority.

020-C is **implementation operating-model design**.

It does not authorize domain implementation.

# Entry state

~~~text
PHASE 020 ACTIVE
020-A/B COMPLETE
020-C NEXT ELIGIBLE / USER AUTHORIZED

accepted architecture              true
G0                                 SATISFIED
active implementation packages     0
G2 authorizations                  0
domain implementation              NOT AUTHORIZED
~~~

# Decision

**020-C — ACCEPT TOOL-NEUTRAL COORDINATED AUTONOMY WITH HUMAN LIFECYCLE AUTHORITY.**

The implementation program will use a hybrid model:

~~~text
human authorizer
     │
     │ G2 selects one phase/package envelope
     ▼
coordinator
     │
     ├─ declared work unit → isolated worktree → implementer
     ├─ declared work unit → isolated worktree → implementer
     └─ declared work unit → isolated worktree → implementer
                     │
                     ▼
             independent review
                     +
             protected verification
                     │
                     ▼
                 exit gate
                     │
                     ▼
                  COMPLETE
                     │
                     ▼
              next phase ELIGIBLE
              (not auto-authorized)
~~~

This is human-directed at the **lifecycle boundary** and autonomous inside a **bounded authorized execution envelope**.

# Provider posture

Cursor and Codex are treated as replaceable agent runtimes.

Current provider documentation supports isolated/parallel agent workflows and worktrees. MUDAC uses those capabilities as execution mechanics only.

The repository does not encode:

- Cursor as the permanent frontend agent;
- Codex as the permanent backend agent;
- one provider as semantic authority;
- one model version as a design assumption.

Agent role is selected per implementation phase/work unit.

Provider-runtime behavior remains evidence-calibrated under the existing tool compatibility contract.

# Role model

## Human Authorizer

Only human/program authority may:

- select the implementation phase/package for execution;
- grant G2;
- approve A3 actions not already explicitly included in the selected envelope;
- approve A4 semantic/accepted-architecture change;
- grant merge/release/deployment/production authority where later governance requires it.

The Authorizer does not need to approve every ordinary implementation edit inside an already authorized G2 envelope.

## Coordinator

The Coordinator is the only agent role permitted to delegate implementation work inside an authorized phase/package.

It may:

- materialize only work units already allowed by the active phase/package plan;
- assign Cursor/Codex implementer roles;
- select dependency-safe units for parallel execution;
- enforce concurrency and serialized-surface rules;
- integrate completed work-unit commits into the phase branch;
- request independent review and verification;
- run bounded repair iterations.

It may not:

- invent a new package/phase;
- broaden visible success criteria;
- change accepted semantics/architecture;
- waive required evidence;
- create undeclared work units;
- authorize itself or another agent at G2;
- merge/deploy because work is green.

## Implementer

An Implementer receives exactly one bounded work unit.

It may:

- edit only the unit's owned/directly necessary surfaces;
- run allowed validation;
- make proportional supporting changes;
- repair failures inside the original unit scope;
- report IMPLEMENTATION COMPLETE / REVIEW REQUESTED.

It may not:

- recursively delegate implementation;
- acquire another work unit automatically;
- merge its own work;
- satisfy independent review with self-review;
- weaken requirements/tests to make the unit pass.

## Reviewer

A Reviewer is an independent agent run.

The Reviewer:

- inspects the actual diff/head;
- resolves governing current authority independently;
- reviews correctness, architecture fidelity, security, maintainability and unnecessary complexity;
- distinguishes blocking defects from non-blocking improvements.

The Reviewer must not be the same agent run that authored the work unit.

Provider diversity (Cursor reviewing Codex or vice versa) is preferred where practical, but **independent run/context is mandatory; provider diversity is not**.

A Reviewer remains read-only unless a repair assignment is separately created.

## Verifier

The Verifier is public CI plus later protected evaluator infrastructure.

The Verifier evaluates the exact candidate revision.

It does not edit requirements or source merely to obtain PASS.

The protected evaluator remains inaccessible to ordinary Implementers.

## Gatekeeper

The Gatekeeper integrates:

- visible success criteria;
- required evidence;
- public CI/scans;
- protected evaluation;
- independent review;
- unresolved risk.

The Gatekeeper may record completion only when the active phase contract explicitly allows that status mutation and all mandatory predicates pass.

A Gatekeeper cannot override a failed mandatory check or grant the next phase G2.

# Delegation boundary

The former blanket prohibition on agent delegation is refined.

Delegation is ordinary bounded A2 implementation activity only when **all** of these are true:

1. an implementation phase/package has explicit G2;
2. its plan declares coordinated multi-agent execution;
3. a Coordinator is named;
4. each delegated work unit is within the accepted scope/dependency graph;
5. maximum concurrency and serialized surfaces are explicit;
6. each unit receives an exact base revision and context manifest;
7. delegated agents cannot recursively create further implementation work;
8. no delegation changes merge/deploy/production authority.

Outside that envelope, spawning implementation agents remains A3 scope expansion.

Phase 020 has no G2, so this rule creates **future operating authority only**, not current execution authority.

# Work-unit state

A work unit uses:

~~~text
DECLARED
  ↓
READY
  ↓
ASSIGNED
  ↓
IN_PROGRESS
  ↓
IMPLEMENTATION_COMPLETE
  ↓
REVIEW_VERIFICATION
  ├─ REPAIR_REQUIRED → IN_PROGRESS
  ├─ BLOCKED
  └─ ACCEPTED_FOR_INTEGRATION
~~~

A work unit is not an implementation package and does not create independent semantic authority.

# Work isolation

Every writable autonomous work unit must begin from an exact recorded base SHA in an isolated checkout/worktree.

Recommended branch namespace:

~~~text
work/<phase-or-package-id>/<work-unit-id>-<slug>
~~~

The phase/package integration branch is separate from individual work-unit branches.

Required isolation rules:

- agents do not directly implement against the ordinary shared `main` checkout;
- one writable worktree belongs to one active work unit;
- another work unit cannot reuse that worktree as a shortcut;
- local generated/build state is not shared as authority across worktrees;
- changes are integrated by reviewed commits/diffs, not by copying arbitrary untracked files;
- the candidate is revalidated after integration because individually green branches do not prove the composed branch.

Cursor-specific worktree configuration may automate repository setup, but it cannot carry MUDAC semantic rules.

Codex/Cursor built-in worktree features are conveniences; ordinary Git worktree isolation remains the conceptual contract.

# Parallelism and serialized surfaces

Parallelism is permitted only when the active dependency graph shows the units are safe to run concurrently.

The phase plan must identify likely shared-writer/control surfaces.

Default serialized classes include:

- root package lockfile when dependency changes overlap;
- migration ordering/ledger/catalog;
- shared database/bootstrap migration mechanics;
- root CI/workflow configuration;
- shared OpenTofu backend/bootstrap or common environment authority;
- generated registries/indexes;
- canonical/routing authority files;
- the same source file or private owner implementation.

A single unit may own a serialized surface for an integration window.

Agents must not resolve a concurrent-write collision by silently taking the other unit's changes as authority.

# Context manifest

Every implementation work unit must have a compact context manifest.

It records pointers and constraints, not copied canonical prose.

Minimum fields:

- work-unit ID;
- parent implementation phase/package ID;
- role;
- exact base SHA;
- purpose and in-scope behavior;
- explicit exclusions;
- current canonical/architecture references;
- owned/touchable surfaces;
- dependency/predecessor work units;
- visible success criteria;
- required evidence;
- allowed external actions;
- serialized/conflict surfaces;
- circuit breakers.

The agent then uses CTX progressive retrieval to load only the smallest required current owners.

A context manifest is an **operational scope record**, not a new semantic owner.

# Context independence for review

Independent review must not rely solely on:

- implementer summary;
- implementer-selected excerpts;
- implementer self-review;
- provider conversation memory.

Reviewer context begins with:

1. phase/package/work-unit contract;
2. exact base/head diff;
3. relevant current authority;
4. evidence outputs.

Implementer rationale is optional evidence after those sources are resolved.

# Technical agent provenance

Agent provenance is technical/change provenance and must never be confused with MUDAC domain Provenance or human semantic authorship.

The eventual evidence bundle for each work unit/phase records at least:

- parent phase/package;
- work-unit ID;
- agent role;
- provider/tool;
- run/session identifier when available and safe to retain;
- exact base SHA;
- exact candidate/head SHA;
- branch/worktree identifier;
- commits/diff identity;
- current authority references used;
- public verification evidence;
- reviewer/verifier identity;
- explicitly performed external actions;
- final disposition and residual findings.

Do **not** require private chain-of-thought, full prompt transcripts, secrets or provider-internal reasoning as completion evidence.

# External actions

G2 does not automatically authorize every external mutation.

The implementation phase/package start gate may explicitly pre-authorize bounded repetitive actions such as:

- push the implementation branch;
- update the already-selected pull request;
- create a pull request for the authorized branch.

Those permissions are listed in the work envelope.

The following remain separate unless explicitly governed later:

- merge to protected integration/main;
- deploy;
- cloud-resource mutation;
- production access;
- secrets/credential expansion;
- destructive data actions.

# Autonomy circuit breakers

An agent must stop the affected work unit and report/escalate rather than improvise when a circuit breaker fires.

## Hard authority/safety stops

- accepted semantic or architecture contradiction;
- request would require A4 without explicit change intent;
- undeclared scope/package expansion;
- production target, credential or data ambiguity;
- secret/sensitive-data exposure outside established permissions;
- destructive/irreversible operation not explicitly authorized;
- shared-writer collision on a serialized surface;
- unauthorized merge/deploy/cloud mutation;
- inability to distinguish technical privilege from MUDAC semantic authority.

## Engineering-integrity stops

- exact base has become materially stale against a changed dependency/predecessor;
- migration ordering or compatibility cannot be established safely;
- environment cannot be restored to a deterministic clean state;
- evidence is flaky/nondeterministic and cannot be trusted;
- verifier failures repeat in a way suggesting requirement/design mismatch rather than a local defect;
- safe repair requires a new dependency/service or cross-package contract outside authorized scope;
- security remediation would change accepted architecture or authority.

Ordinary compile/test/lint failures inside scope are **not** circuit breakers; they are normal repair-loop input.

# Repair loop

An Implementer may repair its own work repeatedly while:

- repair stays inside the authorized unit;
- no circuit breaker has fired;
- evidence becomes more trustworthy rather than increasingly suppressed;
- the phase's repair budget/timeout has not been exceeded.

020-F/H will define exact phase-exit/repair mechanics.

A repair loop may not:

- quarantine a mandatory failing test indefinitely;
- lower acceptance criteria;
- disable a scanner;
- broaden scope by convenience;
- turn an unknown state into assumed success.

# Baseline drift

Every work unit starts from an exact base revision.

If a predecessor or integration branch changes materially while the unit is in progress:

1. classify whether the unit remains independent;
2. if not, stop integration;
3. update/rebase onto an approved new base;
4. rerun affected verification;
5. preserve both old/new revision identity in technical provenance.

A green result for an obsolete base is not evidence for the new base.

# Exit recording versus next-phase authority

A phase exit process may be pre-authorized to record COMPLETE after all required exact-SHA predicates pass.

That optimization removes ceremonial human clicks; it does not transfer lifecycle authority.

After completion:

~~~text
current phase COMPLETE
next phase NEXT ELIGIBLE
next phase G2 NOT GRANTED
~~~

The human/program Authorizer still chooses whether the next implementation phase executes.

# Provider-specific conclusions

Current external documentation confirms:

- Codex supports parallel agent work and built-in worktree isolation;
- Cursor supports isolated worktrees, parallel/multitask agents and cloud agent environments;
- both support repository-carried instruction/workflow mechanisms.

020-C therefore does **not** need a provider-specific semantic fork.

MUDAC retains:

~~~text
AGENTS.md
  → canonical governance
  → .agents/skills
  → provider adapter/mechanics
~~~

# Carry-forward to 020-D/E/F/G/H

020-C establishes constraints that later subphases must honor:

- **020-D**: MCP/environment tooling must fit the same nonproduction/role/provenance/circuit-breaker model.
- **020-E**: package/work-unit dependency graph must identify parallel and serialized surfaces.
- **020-F**: phase contract must instantiate context manifest, role assignments, visible criteria and bounded delegation.
- **020-G**: evidence bundles/CI must carry exact base/head and technical agent provenance.
- **020-H**: independent review, repair and gatekeeper state transitions must enforce role separation.

# Implementation boundary verification

After 020-C:

~~~text
PHASE 020 ACTIVE
020-A/B/C COMPLETE
020-D NEXT ELIGIBLE

active implementation packages   0
G2 authorizations                0
domain implementation            NOT AUTHORIZED
~~~

No MUDAC domain implementation was performed.

# Exit decision

**020-C — COMPLETE — PASS.**

MUDAC now has a bounded autonomous-engineering operating model suitable for Cursor, Codex or future agents without granting provider or orchestration authority over lifecycle, semantics, merge, release or production.

Next eligible:

> **020-D — Non-Production Environment, Synthetic Data, Observability & MCP Agent Test-Control-Plane Architecture**

020-D is **NEXT ELIGIBLE / NOT AUTOMATICALLY AUTHORIZED**.
