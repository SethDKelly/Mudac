# Implementation

This subtree preserves MUDAC implementation/tooling decisions and planning produced before the latest Jackson methodology completion reassessment.

## Current authority state

**DOMAIN IMPLEMENTATION AUTHORITY AND IMPLEMENTATION PLANNING ARE SUSPENDED.**

Jackson-aligned Concept Design is closed. No new MUDAC domain implementation is authorized; Phase 018 is active repository qualification and architecture/engineering re-entry preparation, and the historical Phase 008 queue remains halted after 008-E.

The controlling current owners are:

- [Design / Implementation Boundary](../governance/design-implementation-boundary.md)
- [Downstream Architecture & Implementation Authority Quarantine](../governance/downstream-authority-quarantine.md)
- [Post-Concept-Design Architecture & Engineering Re-entry](../governance/post-concept-design-reentry.md)

Current posture:

```text
Jackson Concept Design: CLOSED — PHASE 017 PASS
Phase 018: IN PROGRESS — 018-A/B COMPLETE / 018-C NEXT
implementation readiness: READY FOR POST-CLOSURE PREPARATION
implementation planning: NOT YET ACCEPTED
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

The retained runtime/bootstrap remains non-domain. Concrete package, PostgreSQL, outbox, Cognito, framework/toolchain and historical Phase-008 planning choices are preserved only as candidate/factual downstream knowledge. They remain candidates for Phase-018 qualification/revalidation; 008-F..L remains inactive and no historical first-slice gate has current authority.
