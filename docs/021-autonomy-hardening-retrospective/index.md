# Phase 021-R — Autonomy-Hardening Retrospective & Pre-022 Control-Plane Design

## Status

```text
PHASE 021 / IMP-001                  COMPLETE / INTEGRATED
PHASE 021-R RETROSPECTIVE            ACTIVE — PLANNING/DESIGN ONLY
021-R-A                              COMPLETE
021-R-B                              COMPLETE — PASS
021-R-C                              COMPLETE — PASS
021-R-D                              COMPLETE — PASS
021-R-E                              COMPLETE — PASS
021-R-F                              NEXT ELIGIBLE
021-R-G                              PLANNED
PHASE 022                            NEXT ELIGIBLE / NOT AUTHORIZED
AUTONOMY RUNTIME IMPLEMENTATION      NOT AUTHORIZED
RELEASE / PRODUCTION                 NOT AUTHORIZED
```

Phase 021-R is an append-only post-completion retrospective boundary. It does not reopen Phase 021, IMP-001, its G5 decision, or its integration evidence. It converts the successful Phase-021 operating process into a safer machine-routed autonomy design.

## Governing principles

> **More autonomy does not mean more authority.**

Automate transitions whose eligibility/evidence can be mechanically established while retaining explicit human authority for consequential scope, architecture, merge, release, production, reopen, and next-phase decisions.

> **Hide the probe, never the requirement.**

Protected evaluator implementation may remain hidden; semantic requirements, criteria, material boundaries, and evidence obligations may not.

## Subphase plan

| Subphase | Purpose | State |
|---|---|---|
| **021-R-A** | Retrospective authority, coordination debt, lifecycle truth | **COMPLETE** |
| **021-R-B** | Orchestrator state machine, guards, human stops, fail-closed semantics | **COMPLETE — PASS** |
| **021-R-C** | Evidence dependency graph, invalidation, equivalence, evidence reuse | **COMPLETE — PASS** |
| **021-R-D** | Agent dispatcher, role identity, session isolation, context generation, provenance | **COMPLETE — PASS** |
| **021-R-E** | GitHub event integration, deduplication/idempotency, PR/CI choreography, reconciliation | **COMPLETE — PASS** |
| **021-R-F** | Development-control MCP interfaces, authorization/security boundary, test-control composition | **NEXT ELIGIBLE** |
| **021-R-G** | Shadow replay, failure injection, exit review, autonomy implementation recommendation | PLANNED |

## 021-R-B result

R-B defines the guarded lifecycle state machine and immutable-fact projection. GitHub events, agent outputs, CI, G5, or MCP calls cannot synthesize human authority.

Machine contract: `docs/routing/autonomy_orchestrator_contract.json`.

## 021-R-C result

R-C defines append-only evidence dependencies, material-surface manifests, deterministic revision classification, content-equivalence proof, minimal transitive reverification, and reuse by binding rather than evidence relabeling.

Machine contract: `docs/routing/autonomy_evidence_dependency_contract.json`.

## 021-R-D result

R-D defines provider-neutral agent dispatch and provenance: exact revision/authority-bound dispatch packets, implementer/reviewer isolation, evidentiary session freshness, minimum-sufficient context manifests, append-only technical provenance, deterministic repair/review generation, and serialized-surface reservations.

Machine contract: `docs/routing/autonomy_agent_dispatch_contract.json`.

## 021-R-E result

R-E defines GitHub event ingestion and reconciliation.

Key results:

- a webhook/check/workflow event is a notification, not lifecycle truth;
- raw delivery identity and semantic fact identity are separate, making redelivery/retry idempotent;
- duplicate, late, stale, and out-of-order events cannot advance state without reconciliation;
- current PR/ref/check/workflow truth is fetched/reconciled before consequential transitions;
- required CI is evaluated against the exact current head and current required-check set;
- legacy combined-status output cannot override exact check-run/workflow evidence when semantically different;
- PR head/base drift freezes merge eligibility and routes through R-C invalidation/equivalence;
- implementation and closure PR dependency/synchronization choreography is explicit;
- post-merge SHA/tree identity and integration evidence are separately registered;
- missed webhook delivery can be recovered by startup/periodic reconciliation;
- bounded GitHub side effects use idempotent operation IDs and optimistic preconditions;
- R-D serialized-surface reservations now have immutable event lifecycle semantics;
- GitHub events cannot create G2, merge, release, production, reopen, or Phase-022 authority.

Machine contract: `docs/routing/autonomy_github_event_contract.json`.

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
- `docs/routing/autonomy_github_event_contract.json`
- `docs/routing/autonomy_control_plane_interfaces.json`

These contracts do not authorize runtime execution.

## Next eligible work

> **021-R-F — Development-Control MCP Interfaces, Authorization, Production Denial & Composition with the 020-D Test-Control Plane**

Phase 022 remains **NEXT ELIGIBLE / NOT AUTHORIZED**; completing R-E does not alter that boundary.
