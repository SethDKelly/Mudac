---
type: Phase Record
title: 020-L — Phase-020 Consolidation, Pre-Implementation Audit, Exit Decision & Phase-021 Handoff
description: "Consolidates Phase 020, audits repository and implementation-entry controls, records completed exit repairs, and blocks Phase-020 closure / Phase-021 G2 until main branch enforcement is observed."
status: stable
tags: [phase-020, exit-audit, preimplementation, phase-021, branch-protection, ci]
sources:
  - resource: README.md
  - resource: ../routing/phase020_preimplementation_exit_audit.json
  - resource: ../routing/phase020_autonomous_implementation_roadmap.json
  - resource: ../routing/phase020_ci_supplychain_evidence_architecture.json
  - resource: ../canonical/governance/implementation-program-delivery.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-23T15:57:00-05:00 }
---

# Purpose

Perform the final Phase-020 consolidation and pre-implementation audit.

020-L is an **exit gate**, not a documentation-only closure.

It must prove that the autonomous implementation program is internally coherent, repository controls actually support the designed trust model, exact-head CI is clean, and Phase 021 can be handed off without silently manufacturing G2 authority.

# Entry state

~~~text
PHASE 020 ACTIVE
020-A/B/C/D/E/F/G/H/I/J/K COMPLETE
020-L NEXT ELIGIBLE / USER AUTHORIZED

retained implementation packages  15
G1 READY_FOR_AUTHORIZATION         15
G2 AUTHORIZED                       0
active packages                     0
implementation execution           NOT AUTHORIZED
release                             NOT AUTHORIZED
production                          NOT AUTHORIZED
~~~

Entry planning head:

> 66078e412bf0b996cb60fa803dd1062176b26098

# Audit decision

**020-L — BLOCKED.**

Phase 020 is **not** complete.

The repository planning corpus is coherent and exact-head CI was made clean during this audit. A correctly configured `main — protected` ruleset now exists, but its enforcement is currently disabled, so the administrative trust boundary required by 020-G and 020-K is still not enforced.

The blocking finding is:

> **P020L-001 — `main` is not protected.**

GitHub currently reports:

~~~text
main.protected                           false
main.protection.enabled                  false
required status-check enforcement        off
ruleset                                  main — protected
ruleset enforcement                      disabled
~~~

The ruleset contract has been validated: it targets the default branch, requires one approving review, dismisses stale approvals, requires approval of the most recent push and resolved review threads, requires the three expected GitHub Actions checks in strict mode, prohibits deletion/non-fast-forward updates, and grants no bypass actors.

`Knowledge Validation` now runs on every pull request targeting `main`, so its required check can no longer be skipped by PR path filtering.

The connected GitHub integration does not have repository-administration permission to activate the ruleset.

This blocker is tracked as:

> GitHub issue #10 — Phase 020 exit blocker: protect main before Phase 021 G2

# Repairs completed during 020-L

The audit found and repaired two repository-controlled defects before reaching the administrative blocker.

## P020L-R001 — immutable action pins

The three workflows used mutable action tags such as:

~~~text
actions/checkout@v6
github/codeql-action/*@v4
actions/setup-node@v6
actions/setup-python@v7
pnpm/action-setup@v6
opentofu/setup-opentofu@v2
~~~

020-G requires blocking/exit actions to use immutable full commit SHAs.

020-L resolved each current major tag to its current commit target and pinned all external actions to exact SHAs while retaining human-readable version comments.

Phase-020 validation now scans every workflow and fails if an external `uses:` reference is not a 40-character commit SHA.

A new negative mutation deliberately replaces a pin with `actions/checkout@v6`; the conformance suite must reject it.

The agentic negative-control count is now:

> **21**

## P020L-R002 — historical validator reconciliation

Knowledge Validation exposed stale assumptions in:

- `scripts/validate_implementation_program_framework.py`;
- `scripts/validate_phase019_architecture_control.py`.

Those validators still assumed the framework must forever remain exactly `PLANNING_READY` and that the package schema could never gain the review/repair/cross-cutting fields introduced by Phase 020.

020-L repaired the validators so they preserve the original Phase-019 guarantees while recognizing the governed Phase-020 roadmap states and current G1 package schema.

# Exact-head CI evidence

At audit candidate head:

> **e139155520e68f516709bfdfa68e359d5149c699**

all required workflows completed successfully:

| Workflow | Run | Result |
|---|---:|---|
| Knowledge Validation | 35919756102 | **PASS** |
| Implementation Verification | 35919755994 | **PASS** |
| CodeQL | 35919756085 | **PASS** |

This evidence is revision-bound.

It does **not** prove repository enforcement.

# Phase-020 exit criteria audit

| Exit criterion | Result |
|---|---|
| 020-A..L complete/dispositioned | **BLOCKED** — 020-L cannot close with P020L-001 open |
| Accepted architecture current | PASS |
| Implementation phase contract current/machine-checkable | PASS |
| Dependency-safe acyclic roadmap | PASS |
| 15/15 scenarios and applicable obligations mapped | PASS |
| Cursor/Codex roles, isolation and circuit breakers explicit | PASS |
| Non-production MCP/test-control design complete | PASS |
| Visible criteria / protected verification coherent | PASS |
| CI/scanning/review/adversarial/repair gates explicit | PASS |
| PF-01 v1 / whole-system final phase explicit | PASS |
| Evidence and residual-risk ownership explicit | PASS |
| No domain implementation package executed | PASS |
| Exact-head repository conformance / CI clean | PASS at named audit head |
| Phase-021 start-gate handoff | **BLOCKED** pending repository enforcement |

# Required main enforcement

Before this phase may pass, repository administration must change ruleset `main — protected` from **Disabled** to **Active**. Its configured controls already satisfy the accepted 020-G policy:

- pull-request integration to `main`;
- required **Validate agentic/documentation conformance** check;
- required **Implementation Verification** check;
- required **CodeQL JavaScript/TypeScript** check;
- branch freshness / up-to-date-before-merge or merge-queue equivalent;
- conversation resolution;
- force-push prohibition;
- branch-deletion prohibition;
- bypass limited to explicit human break-glass / repository-admin authority.

Autonomous agents, GitHub Actions identities and ordinary implementation credentials must not hold bypass authority.

# Phase-021 handoff

The implementation handoff is prepared but **not eligible for execution**.

~~~text
Phase                       021
Title                       Source Topology & Implementation Foundation
Package                     IMP-001
Package G1                  READY_FOR_AUTHORIZATION
Package G2                  NOT AUTHORIZED
Execution                   FORBIDDEN
~~~

After the ruleset is activated, 020-L must re-run the exit audit and verify:

1. Phase-020 authority is otherwise unchanged;
2. exact `main` SHA/tree is known;
3. main protection/ruleset enforcement is observable;
4. required status checks are actually enforced;
5. exact-head Knowledge Validation, Implementation Verification and CodeQL pass;
6. IMP-001 remains G1-ready;
7. no semantic/architecture blocker exists.

Only then may Phase 020 be marked COMPLETE.

Even after Phase 020 completes:

> **Phase 021 does not automatically receive G2.**

A separate explicit human/program authorization must name IMP-001.

# Durable audit authority

Machine audit:

> `docs/routing/phase020_preimplementation_exit_audit.json`

Administrative blocker:

> GitHub issue #10

# Current state

~~~text
PHASE 020 ACTIVE — EXIT BLOCKED BY REPOSITORY ENFORCEMENT
020-A/B/C/D/E/F/G/H/I/J/K COMPLETE
020-L NEXT ELIGIBLE — BLOCKED BY P020L-001

G1 READY_FOR_AUTHORIZATION         15
G2 AUTHORIZED                       0
active packages                     0

implementation execution           NOT AUTHORIZED
release                             NOT AUTHORIZED
production                          NOT AUTHORIZED
~~~

# Exit decision

**020-L — BLOCKED — P020L-001.**

Do not mark Phase 020 COMPLETE and do not begin Phase 021 implementation until main-branch enforcement is installed and independently re-observed.
