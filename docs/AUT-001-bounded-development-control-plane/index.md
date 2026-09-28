# AUT-001 — Bounded Development-Control Plane Implementation

## Current status

```text
PHASE 021 / IMP-001                  COMPLETE / INTEGRATED
PHASE 021-R RETROSPECTIVE            COMPLETE / PASS
AUT-001 START GATE                   COMPLETE / PASS
AUT-001 G1                           READY FOR AUTHORIZATION
AUT-001 G2                           NOT AUTHORIZED
AUT-001 IMPLEMENTATION               NOT AUTHORIZED
AUT-001-F / FULL COMPOSED            DEPENDENCY BLOCKED — 020-D RUNTIME NOT OPERATIONAL
PHASE 022                            NEXT ELIGIBLE / NOT AUTHORIZED
RELEASE / PRODUCTION                 NOT AUTHORIZED
```

## Purpose

AUT-001 implements the bounded autonomy-control design established by Phase 021-R. It is development-process infrastructure, not application/domain behavior and not a new MUDAC semantic owner.

The package is designed to automate mechanically provable coordination while retaining explicit human/program authority for G2, material scope or architecture changes, protected merge, reopen execution, release, production and next-phase authorization.

## Authoritative package records

- [AUT-001 Start Gate](AUT-001-start-gate.md)
- `docs/routing/aut001_start_gate.json`
- `docs/routing/aut001_implementation_package_contract.json`
- `docs/routing/aut001_material_surface_manifest.json`

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
| **AUT-001-A** | Control-plane substrate, append-only facts, deterministic replay, lifecycle/evidence core | **G1 READY / NOT AUTHORIZED** |
| **AUT-001-B** | Live read-only shadow and GitHub reconciliation | PLANNED / NOT AUTHORIZED |
| **AUT-001-C** | Dispatcher, Cursor/Codex adapters, isolation and provenance | PLANNED / NOT AUTHORIZED |
| **AUT-001-D** | Development-control MCP query/record and authorization boundary | PLANNED / NOT AUTHORIZED |
| **AUT-001-E** | Bounded non-human side effects | PLANNED / NOT AUTHORIZED |
| **AUT-001-F** | 020-D nonproduction test-control evidence bridge | **DEPENDENCY BLOCKED / NOT AUTHORIZED** |
| **AUT-001-G** | Independent exit, executable replay/failure injection, shadow qualification and G5 | PLANNED / NOT AUTHORIZED |

## Acceptance profiles

**CORE_COORDINATION** requires A–E plus core G qualification. It remains disabled until a separate human operational-enablement decision, and it cannot coordinate Phase 022 without a separate Phase-022 G2.

**FULL_COMPOSED** additionally requires F and full-composed G evidence after the independent 020-D runtime becomes operationally accepted. No production test-control capability is introduced.

## Preferred provider/review pattern

The start gate recommends alternating Cursor and Codex between implementer and independent reviewer by subphase, while keeping role identity, session isolation and exact-revision evidence authoritative. Provider diversity is a quality mechanism, not an authority mechanism.

## Next decision

The start gate has passed but grants no execution authority.

> **Next action: explicit human/program G2 decision for the initial AUT-001 envelope: A–E plus G CORE qualification.**

AUT-001-F / FULL_COMPOSED remains deferred until the 020-D runtime dependency is independently satisfied.
