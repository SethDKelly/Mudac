# Phase 021-R — Autonomy-Hardening Retrospective & Pre-022 Control-Plane Design

## Status

```text
PHASE 021 / IMP-001                  COMPLETE / INTEGRATED
PHASE 021-R RETROSPECTIVE            ACTIVE — PLANNING/DESIGN ONLY
021-R-A                              COMPLETE
021-R-B                              COMPLETE — PASS
021-R-C                              COMPLETE — PASS
021-R-D                              COMPLETE — PASS
021-R-E                              NEXT ELIGIBLE
021-R-F..G                           NOT YET COMPLETE
PHASE 022                            NEXT ELIGIBLE / NOT AUTHORIZED
AUTONOMY RUNTIME IMPLEMENTATION      NOT AUTHORIZED
RELEASE / PRODUCTION                 NOT AUTHORIZED
```

Phase 021-R is an **append-only post-completion retrospective boundary**. It does not reopen Phase 021, IMP-001, its G5 decision, or its integration evidence. It converts the successful Phase-021 operating process into a safer machine-routed autonomy design.

## Governing principles

> **More autonomy does not mean more authority.**

Automate transitions whose eligibility/evidence can be mechanically established while retaining explicit human authority for consequential scope, architecture, merge, release, production, reopen, and next-phase decisions.

> **Hide the probe, never the requirement.**

Protected evaluator implementation may remain hidden; semantic requirements, criteria, material boundaries, and evidence obligations may not.

## Retrospective objective

Design a repository-native autonomy layer that can resolve lifecycle state, dispatch bounded agents, isolate work, register candidates, gather verification/reviews, watch GitHub, classify revision drift, invalidate/reuse evidence safely, assemble G5, stop at human decisions, capture integration/closure evidence, and never infer next-phase authority.

## Non-goals

This retrospective does **not** authorize:

- application/domain implementation;
- IMP-002/004/005/006 execution;
- Phase-022 G2;
- autonomy runtime implementation;
- production/release/provider deployment;
- arbitrary shell/cloud/SQL/HTTP/browser-eval/secret access;
- weakening exact-revision evidence, independent/adversarial review, G5, or human merge authority;
- rewriting historical evidence to make later revisions appear previously reviewed.

## Subphase plan

| Subphase | Purpose | State |
|---|---|---|
| **021-R-A** | Retrospective authority, coordination debt, lifecycle truth | **COMPLETE** |
| **021-R-B** | Orchestrator state machine, guards, human stops, fail-closed semantics | **COMPLETE — PASS** |
| **021-R-C** | Evidence dependency graph, invalidation, equivalence, evidence reuse | **COMPLETE — PASS** |
| **021-R-D** | Agent dispatcher, role identity, session isolation, context generation, provenance | **COMPLETE — PASS** |
| **021-R-E** | GitHub event integration, deduplication/idempotency, PR/CI choreography, reconciliation | **NEXT ELIGIBLE** |
| **021-R-F** | Development-control MCP interfaces, authorization/security boundary, test-control composition | PLANNED |
| **021-R-G** | Shadow replay, failure injection, exit review, autonomy implementation recommendation | PLANNED |

## 021-R-B result

R-B defines the guarded lifecycle state machine and immutable-fact projection. It prevents GitHub events, agent outputs, CI, G5, or MCP calls from synthesizing human authority.

Machine contract: `docs/routing/autonomy_orchestrator_contract.json`.

## 021-R-C result

R-C defines append-only evidence dependencies, material-surface manifests, deterministic revision classification, content-equivalence proof, minimal transitive reverification, and reuse by binding rather than evidence relabeling.

Machine contract: `docs/routing/autonomy_evidence_dependency_contract.json`.

## 021-R-D result

R-D defines provider-neutral agent dispatch and provenance.

Key results:

- role identity is separate from Cursor/Codex/provider identity;
- agents cannot self-select the next task;
- every dispatch is immutable and bound to exact revision, current authority digest, lifecycle state, work unit, material surfaces, and allowed actions;
- implementers use isolated writable worktrees while reviewers use read-only exact-candidate checkouts;
- independent and adversarial freshness is represented by run/session/worktree identity rather than prose assertions;
- context manifests follow minimum-sufficient progressive retrieval and reference canonical owners rather than copying them into shadow authority;
- protected evaluator detail and secret/sensitive data remain segregated;
- every run emits an append-only R-C-ingestible provenance manifest without private chain-of-thought/full provider transcripts;
- repair and reviewer instructions can be generated deterministically from repository contracts;
- concurrent writers require serialized-surface reservations.

Machine contract: `docs/routing/autonomy_agent_dispatch_contract.json`.

## Architectural layers

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

The components may be deployed differently later; this is responsibility decomposition, not runtime authority.

## Human-only decisions retained

At minimum:

- G2 authorization;
- material scope expansion;
- architecture/semantic re-entry;
- repair-budget override;
- protected implementation merge;
- closure merge where required;
- reopened implementation execution;
- release;
- production;
- next-phase authorization.

## Durable design outputs

Current machine projections:

- `docs/routing/phase021_autonomy_hardening_retrospective.json`
- `docs/routing/autonomy_orchestrator_contract.json`
- `docs/routing/autonomy_evidence_dependency_contract.json`
- `docs/routing/autonomy_agent_dispatch_contract.json`
- `docs/routing/autonomy_control_plane_interfaces.json`

These contracts do not authorize runtime execution.

## Next eligible work

> **021-R-E — GitHub Event Integration, Deduplication/Idempotency, PR/CI Choreography & Reconciliation**

Phase 022 remains **NEXT ELIGIBLE / NOT AUTHORIZED**; completing R-D does not alter that boundary.
