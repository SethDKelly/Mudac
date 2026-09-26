# Implementation

This subtree preserves MUDAC implementation/tooling decisions and planning produced before the latest Jackson methodology completion reassessment.

## Current authority state

**IMPLEMENTATION PLANNING IS ENABLED UNDER G0; DOMAIN IMPLEMENTATION EXECUTION REMAINS SUSPENDED.**

Jackson-aligned Concept Design is closed. Phases 018 and 019 are complete and whole architecture is accepted. **Phase 020 is ACTIVE — 020-A COMPLETE / 020-B NEXT ELIGIBLE** to design the autonomous implementation program. No MUDAC domain implementation package is authorized for execution; the historical Phase-008 queue remains halted after 008-E.

The controlling current owners are:

- [Design / Implementation Boundary](../governance/design-implementation-boundary.md)
- [Downstream Architecture & Implementation Authority Quarantine](../governance/downstream-authority-quarantine.md)
- [Post-Concept-Design Architecture & Engineering Re-entry](../governance/post-concept-design-reentry.md)
- [Implementation Program, Verification & Delivery-Gate Contract](../governance/implementation-program-delivery.md)

Current posture:

```text
Jackson Concept Design: CLOSED — PHASE 017 PASS
PHASE 018 COMPLETE — PASS
018-A/B/C/D/E/F/G/H/I/J/K/L/M COMPLETE
PHASE 019 COMPLETE — 019-A/B/C/D/E/F/G/H/I/J/K/L COMPLETE
implementation readiness: READY FOR POST-CLOSURE PREPARATION
implementation program framework: PLANNING_READY / G0 SATISFIED / PHASE 020 DESIGN ACTIVE
active implementation packages: 0
implementation planning: PHASE 020 AUTONOMOUS PROGRAM DESIGN ACTIVE
new domain implementation: NOT STARTED
implementation execution authorization: NOT GRANTED
006-D bootstrap: FROZEN HISTORICAL NON-DOMAIN SUBSTRATE
008-D persistence realization: SUSPENDED DOWNSTREAM CANDIDATE
008-E identity/auth realization: SUSPENDED DOWNSTREAM CANDIDATE
008-F..L: NOT ACTIVE
```

## Preserved material

* [Implementation Authority, Toolchain & Delivery Governance](implementation-foundation.md) — historical implementation/toolchain governance and bootstrap constraints; not authority to resume domain implementation.
* [Verification Strategy, Evidence & Quality Gates](verification-strategy.md) — historical downstream verification planning; executable evidence work waits for downstream re-entry except narrow repository-knowledge validation.
* [Source Topology, Package Boundaries & Dependency Enforcement](source-topology.md) — preserved candidate source topology, not a Concept Design boundary.
* [Runtime, Environment & Delivery Bootstrap](runtime-delivery-bootstrap.md) — records the frozen 006-D non-domain executable substrate.
* [Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract](persistence-history-projection.md) — **suspended 008-D downstream candidate**; must be revalidated after successful Concept Design closure before adoption.
* [Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical Authority Implementation Contract](identity-authentication-access-session.md) — **suspended 008-E downstream candidate**; must be revalidated after successful Concept Design closure before adoption.

## Frozen bootstrap rule

Existing executable substrate may receive only narrow safety/build maintenance that adds no MUDAC domain semantics. Frameworks, packages, database technology, cloud services, source topology and test tooling present in the repository are historical implementation facts, not conceptual requirements.

## No automatic reactivation

Phase 017 closure authorized only the post-closure preparation/re-entry process now represented by Phase 018. It did not restore this subtree as accepted current implementation authority, resume 008-F, authorize a first slice, or ratify 008-D/E physical choices.

A later downstream re-entry must explicitly decide which prior choices remain justified against the closed conceptual design.


## Phase-017 audit result

017-F audited all six documents in this subtree. Each now carries an explicit suspension notice at document level.

The retained runtime/bootstrap remains non-domain. 018-J has qualified all six implementation documents under Q1–Q6; `docs/routing/downstream_candidate_qualification.json` records their current dispositions. Concrete package, PostgreSQL, outbox, Cognito, framework/toolchain and historical Phase-008 planning choices remain candidate/factual downstream knowledge, not accepted implementation authority. 008-F..L remains inactive and no historical first-slice gate has current authority.


## Current Phase-018 implementation-program framework

018-L defines the technology-neutral package lifecycle, evidence classes and delivery gates in `docs/canonical/governance/implementation-program-delivery.md`, with machine-readable pre-architecture state in `docs/routing/implementation_program_framework.json`.

That framework is current governance. The six documents in this Implementation subtree remain suspended historical candidates. After 020-A, the framework remains PLANNING_READY while Phase 020 designs the autonomous implementation program; package derivation is allowed, the active package set remains empty, and execution remains unauthorized until explicit G2.


Current Phase-019 progression:

~~~text
PHASE 019 COMPLETE
019-A/B/C/D/E/F/G/H/I/J/K/L COMPLETE
ADQ-001 / ADQ-002 / ADQ-003 / ADQ-004 / ADQ-005 / ADQ-006 / ADQ-007 / ADQ-008 / ADQ-009 / ADQ-010 ACCEPTED
Q4R-001 / Q4R-002 / Q4R-003 / Q4R-004 COMPLETE
accepted whole architecture true
G0 package derivation ALLOWED
PHASE 020 COMPLETE
020-A/B/C/D/E/F/G/H/I/J/K/L COMPLETE
Phase 021 START GATE COMPLETE — READY FOR G2 DECISION — G2 NOT AUTHORIZED
active implementation packages 0
implementation execution NOT AUTHORIZED
~~~


## Program

- [Roadmap](../../implementation-roadmap/index.md)
- [Phase-021 gate](../../routing/phase021_start_gate_control.json)
- [Cursor/Codex runbook](../../implementation-roadmap/cursor-codex-autonomous-coding-runbook.md)


## Phase 021

[Start gate](../../021-source-topology-implementation-foundation/021-start-gate.md): **READY FOR G2 DECISION**. G2 NOT AUTHORIZED.
