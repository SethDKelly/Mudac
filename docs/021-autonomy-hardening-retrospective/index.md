# Phase 021-R — Autonomy-Hardening Retrospective & Pre-022 Control-Plane Design

## Status

```text
PHASE 021 / IMP-001                  COMPLETE / INTEGRATED
PHASE 021-R RETROSPECTIVE            ACTIVE — PLANNING/DESIGN ONLY
021-R-A                              COMPLETE
021-R-B                              COMPLETE — PASS
021-R-C                              COMPLETE — PASS
021-R-D                              NEXT ELIGIBLE
021-R-E..G                           NOT YET COMPLETE
PHASE 022                            NEXT ELIGIBLE / NOT AUTHORIZED
AUTONOMY RUNTIME IMPLEMENTATION      NOT AUTHORIZED
RELEASE / PRODUCTION                 NOT AUTHORIZED
```

Phase 021-R is an **append-only post-completion retrospective boundary**. It does not reopen Phase 021, IMP-001, its G5 decision, or its integration evidence. It exists because Phase 021 successfully proved the operating model while also exposing coordination work that can be mechanized safely.

## Governing principle

> **More autonomy does not mean more authority.**
>
> Increase autonomy by automating transitions whose eligibility and evidence can be mechanically established, while preserving explicit human authority for consequential scope, merge, release, production, architecture and next-phase decisions.

A second retained principle remains:

> **Hide the probe, never the requirement.**

The autonomy layer may route protected evaluation but may not invent hidden requirements or expose protected probes to implementers.

## Retrospective objective

Design a repository-native autonomy layer that can perform the coordination work humans manually performed during Phase 021:

1. resolve the current authorized lifecycle state;
2. provision isolated agent work;
3. register immutable candidates;
4. run and collect deterministic verification;
5. dispatch independent and fresh adversarial review;
6. route bounded repairs;
7. watch GitHub PR/CI events;
8. detect head drift and classify materiality;
9. invalidate only affected evidence;
10. assemble G5 evidence;
11. pause at human merge authority;
12. capture integration identity and post-merge evidence;
13. prepare closure evidence; and
14. stop before any next-phase authority is inferred.

## Non-goals

This retrospective does **not** authorize:

- application/domain implementation;
- IMP-002/004/005/006 execution;
- Phase-022 G2;
- production or release actions;
- provider deployment;
- arbitrary shell, cloud, SQL, HTTP, browser-eval or secret access through MCP;
- weakening independent review, adversarial review, CI, G5, exact-SHA evidence or human merge authority;
- rewriting historical Phase-021 evidence to make later revisions appear previously reviewed.

## Subphase plan

| Subphase | Purpose | State |
|---|---|---|
| **021-R-A** | Retrospective authority, observed coordination debt, lifecycle-truth defects & scope boundary | **COMPLETE** |
| **021-R-B** | Orchestrator state machine, transition guards, human authority stops & fail-closed semantics | **COMPLETE — PASS** |
| **021-R-C** | Evidence dependency graph, invalidation, content equivalence & evidence reuse | **COMPLETE — PASS** |
| **021-R-D** | Agent dispatcher, role identity, session isolation, context generation & provenance manifests | **NEXT ELIGIBLE** |
| **021-R-E** | GitHub event integration, deduplication/idempotency, PR/CI choreography & reconciliation | PLANNED |
| **021-R-F** | Development-control MCP interfaces, authorization, production denial & composition with the 020-D test-control plane | PLANNED |
| **021-R-G** | Shadow simulation, failure injection, exit review, implementation package recommendation & Phase-022 handoff | PLANNED |

## 021-R-B result

021-R-B reconciled the orchestrator against the existing 020-C operating model, 020-G exact-revision/evidence architecture, and 020-H review/repair/reopen governance.

The resulting state machine has explicit event envelopes, named transition guards, guarded principal/repair/reopen transitions, precise exception semantics, predeclared lifecycle profiles, and machine-enforced human authority stops.

Machine contract: `docs/routing/autonomy_orchestrator_contract.json`.

## 021-R-C result

021-R-C establishes an append-only evidence graph and deterministic invalidation/reuse model.

Key results:

- evidence remains permanently bound to the revision/material boundary it actually evaluated;
- reuse occurs only through explicit equivalence proof plus a new binding record;
- every package must declare material surfaces and criterion/evidence mappings before G2;
- every changed path/object must map to a declared material surface or classification is `INCONCLUSIVE`;
- revision deltas distinguish provenance-only, non-material, governance, evaluator, executable, mixed, and inconclusive cases;
- invalidation propagates transitively through declared evidence dependencies;
- propagation may stop only where an explicit content-equivalence rule is satisfied;
- review, CI, G5, integration and reopen effects are separately defined;
- full rerun is not the default, but incomplete graph knowledge fails closed rather than permitting optimistic reuse; and
- the real Phase-021 IMP-001 sequence is encoded as the first replay oracle.

Machine contract: `docs/routing/autonomy_evidence_dependency_contract.json`.

## Architectural layers

The planned autonomy control plane has six responsibilities:

```text
Authority
   ↓
Lifecycle State Machine
   ↓
Agent Dispatcher ───── Evidence Dependency Graph
   ↓                           ↓
GitHub Event Adapter ─── Evidence Collector
   ↓                           ↓
Gatekeeper Preparation / Human Authority Stops
   ↓
Development-Control MCP Interface
```

The components may be deployed differently later; this is a responsibility decomposition, not technology authority.

## Human-only decisions retained

At minimum, the autonomy layer must stop for explicit human/program authority at:

- phase/package G2 authorization;
- material scope expansion;
- accepted-architecture contradiction or semantic re-entry;
- repair-budget override;
- protected implementation merge decision;
- closure merge when required;
- reopened implementation execution;
- release authority;
- production authority; and
- next-phase authorization.

No event, passing check, review PASS, G5 result or merged PR may imply the next one of these decisions.

## Durable design outputs

Phase 021-R is expected to leave:

- a machine-readable retrospective authority record;
- an orchestrator state-machine contract;
- an evidence dependency/invalidation contract;
- an agent-dispatch/provenance contract;
- a GitHub event/reconciliation contract;
- a development-control MCP interface contract;
- a shadow-simulation acceptance plan; and
- a bounded recommendation for implementing the autonomy layer before Phase 022.

## Current machine projections

- `docs/routing/phase021_autonomy_hardening_retrospective.json`
- `docs/routing/autonomy_orchestrator_contract.json`
- `docs/routing/autonomy_evidence_dependency_contract.json`
- `docs/routing/autonomy_control_plane_interfaces.json`

These are design contracts. Their existence does not authorize runtime execution.

## Next eligible work

> **021-R-D — Agent Dispatcher, Role Identity, Session Isolation, Context Generation & Provenance Manifests**

Phase 022 remains eligible but **not authorized**; completing R-C does not alter that boundary.