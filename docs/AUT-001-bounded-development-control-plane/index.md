# AUT-001 — Bounded Development-Control Plane Implementation

## Current status

```text
PHASE 021 / IMP-001                  COMPLETE / INTEGRATED
PHASE 021-R RETROSPECTIVE            COMPLETE / PASS
AUT-001 START GATE                   COMPLETE / PASS
AUT-001 CORE G2                      AUTHORIZED — A/B/C/D/E + G CORE
AUT-001-A                            G5 COMPLETE / MERGED / INTEGRATION PASS
AUT-001-B START GATE                 PASS / READY FOR IMPLEMENTATION / NOT STARTED
AUT-001-C                            PREDECESSOR BLOCKED BY B
AUT-001-F / FULL COMPOSED            DEPENDENCY BLOCKED — 020-D RUNTIME NOT OPERATIONAL
PHASE 022                            NOT AUTHORIZED
RELEASE / PRODUCTION                 NOT AUTHORIZED
```

## Purpose

AUT-001 implements the bounded autonomy-control design established by Phase 021-R. It is development-process infrastructure, not application/domain behavior and not a new MUDAC semantic owner.

The package automates mechanically provable coordination while retaining explicit human/program authority for G2, material scope or architecture changes, protected merge, reopen execution, release, production and next-phase authorization.

## Authoritative package records

- [AUT-001 Start Gate](AUT-001-start-gate.md)
- [AUT-001 G2 authorization](AUT-001-g2-authorization.md)
- [AUT-001-B Stage Transition / Start Gate](AUT-001-B-start-gate.md)
- `docs/routing/aut001_start_gate.json`
- `docs/routing/aut001_g2_authorization.json`
- `docs/routing/aut001_implementation_package_contract.json`
- `docs/routing/aut001_material_surface_manifest.json`
- `docs/routing/aut001_b_stage_transition_start_gate.json`

Inherited machine contracts:

- `docs/routing/autonomy_orchestrator_contract.json`
- `docs/routing/autonomy_evidence_dependency_contract.json`
- `docs/routing/autonomy_agent_dispatch_contract.json`
- `docs/routing/autonomy_github_event_contract.json`
- `docs/routing/autonomy_development_control_mcp_contract.json`
- `docs/routing/autonomy_control_plane_interfaces.json`
- `docs/routing/autonomy_shadow_replay_exit_contract.json`

## Subphase plan

| Subphase | Purpose | State |
|---|---|---|
| **AUT-001-A** | Control-plane substrate, append-only facts, deterministic replay, lifecycle/evidence core | **G5 COMPLETE / INTEGRATED** |
| **AUT-001-B** | Live read-only shadow and GitHub reconciliation | **START GATE PASS / READY FOR IMPLEMENTATION / NOT STARTED** |
| **AUT-001-C** | Dispatcher, Cursor/Codex adapters, isolation and provenance | PREDECESSOR BLOCKED BY B |
| **AUT-001-D** | Development-control MCP query/record and authorization boundary | PREDECESSOR BLOCKED |
| **AUT-001-E** | Bounded non-human side effects | PREDECESSOR BLOCKED |
| **AUT-001-F** | 020-D nonproduction test-control evidence bridge | **DEPENDENCY BLOCKED / NOT AUTHORIZED** |
| **AUT-001-G** | Independent exit, executable replay/failure injection, shadow qualification and G5 | CORE PROFILE AUTHORIZED / PREDECESSOR BLOCKED |

## AUT-001-A integration baseline

AUT-001-A was human-authorized for merge after exact-candidate G5 COMPLETE.

- reviewed candidate: `9133eabeb18dfd10d533ab399dc1c3b3c0ae4c1a`
- integration: `e69e76398aedfe17bc8a800c235d16548ff42d44`
- tree: `dff68862e95c2be6a05bc8385b6f4d6df3fe9790`
- integration classification: `PROVENANCE_ONLY_CHANGE / CONTENT_EQUIVALENT`
- post-merge Knowledge Validation: `36458789685` — SUCCESS

This satisfies B's predecessor requirement without rebinding historical A review evidence to changed content.

## AUT-001-B boundary

B is the current stage projection within the existing core G2 envelope. It is strictly read-only with respect to GitHub and external coordination.

B observes and reconciles PR/ref/check/workflow truth, feeds trustworthy facts into the A projection core, reconstructs missed/restart state, and records explainable shadow divergence. It may not write GitHub state, dispatch agents, invoke MCP side effects, access production, merge, release, or create Phase-022 authority.

The stage-transition record supersedes only the prior `current_executable_subphase=AUT-001-A` projection. It does not rewrite or expand the original G2 authorization.

## Acceptance profiles

**CORE_COORDINATION** requires A–E plus core G qualification. It remains operationally disabled until its later enablement boundary, and it cannot coordinate Phase 022 without a separate Phase-022 G2.

**FULL_COMPOSED** additionally requires F and full-composed G evidence after the independent 020-D runtime becomes operationally accepted. No production test-control capability is introduced.

## Preferred provider/review pattern

For AUT-001-B the package preference is:

- implementation: Cursor
- independent review: Codex
- adversarial review: fresh separate session

Role/session/worktree independence and exact-revision evidence are authoritative; provider diversity itself grants no authority.

## Next action

AUT-001-B's stage-transition/start gate has passed and its predecessor is satisfied.

> **Next action: create the exact B implementation branch from the final B start-gate head and begin the bounded read-only shadow/reconciliation implementation.**

This does not authorize AUT-001-F, Phase 022, protected merge, release, or production.
