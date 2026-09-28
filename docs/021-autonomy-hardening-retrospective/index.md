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
021-R-F                              COMPLETE — PASS
021-R-G                              NEXT ELIGIBLE
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
| **021-R-F** | Development-control MCP interfaces, authorization/security boundary, test-control composition | **COMPLETE — PASS** |
| **021-R-G** | Shadow replay, failure injection, exit review, autonomy implementation recommendation | **NEXT ELIGIBLE** |

## R-B through R-E result

R-B defines the guarded lifecycle state machine and immutable-fact projection; R-C defines evidence dependency/invalidation and content-equivalence reuse; R-D defines provider-neutral dispatch, isolation, context and provenance; and R-E defines idempotent GitHub event/reconciliation choreography.

Machine contracts:

- `docs/routing/autonomy_orchestrator_contract.json`
- `docs/routing/autonomy_evidence_dependency_contract.json`
- `docs/routing/autonomy_agent_dispatch_contract.json`
- `docs/routing/autonomy_github_event_contract.json`

## 021-R-F result

R-F defines the development-control MCP capability and security boundary.

Key results:

- MCP capability exposes already-resolved authority; it never creates authority;
- query, record/compute and bounded-action capability classes are distinct;
- consequential requests bind principal, role/dispatch, exact SHA/tree, R-B state and authority digest;
- agent-callable G2, scope expansion, merge approval, reopen authorization, release, production and next-phase tools are intentionally absent;
- arbitrary shell, Git/GitHub API, HTTP, SQL, AWS/cloud, browser-eval, filesystem escape, secret retrieval and generic deploy/merge capabilities are forbidden;
- GitHub mutations route through R-E optimistic preconditions/idempotency;
- agent launches route through R-D dispatch/session isolation;
- evidence/G5 validity remains governed by R-C and 020-H;
- development-control MCP is separate from the 020-D non-production application test-control MCP;
- `implementation.request_test_control_run` may request only a declared evidence profile and cannot bypass 020-D environment, capability, actor or production-denial checks;
- 020-D evidence returns through a bounded provenance/evidence-reference bridge and cannot itself advance implementation lifecycle state;
- production control/test composition remains structurally forbidden;
- stable error classes, idempotency, concurrency and audit/provenance envelopes are defined.

Machine contract: `docs/routing/autonomy_development_control_mcp_contract.json`.

## Control-plane composition

```text
Authority / immutable program records
              ↓
      R-B lifecycle state
              ↓
R-D Dispatcher ───────── R-C Evidence Graph
      ↓                         ↑
R-E GitHub Adapter              │
      ↓                         │
Development-Control MCP ────────┤
      │                         │
      └─ declared evidence request
                 ↓
       020-D Test-Control MCP
                 ↓
       real NON-PRODUCTION MUDAC
```

Development-control and test-control remain distinct technical authority planes. Neither becomes a MUDAC semantic owner.

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
- `docs/routing/autonomy_development_control_mcp_contract.json`
- `docs/routing/autonomy_control_plane_interfaces.json`

These contracts do not authorize runtime execution.

## Next eligible work

> **021-R-G — Shadow Replay, Failure Injection, Exit Review & Autonomy Implementation Recommendation**

R-G must validate the R-B..F design against the actual Phase-021 sequence and adversarial authority/failure cases before recommending any bounded autonomy implementation work. Phase 022 remains **NEXT ELIGIBLE / NOT AUTHORIZED**; completing R-F does not alter that boundary.
