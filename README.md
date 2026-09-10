# MUDAC Competition Demo

MUDAC is a design-governed web application effort for fair, traceable, resilient judging at live student data competitions.

Student Teams present analyses to Panels of volunteer Judges. Each Judge independently authors a Rubric-based Scorecard in a Judging Encounter; authoritative Scorecards feed explicit Coverage, aggregation, ranking, Awards, and controlled official-closeout semantics while preserving Judge independence, provenance, anonymity, accessibility, and paper continuity.

## Start here

* [`AGENTS.md`](AGENTS.md) — repository-agent bootstrap and current Phase 008 execution boundary.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/`](docs/canonical/) — current product/domain, synchronization, temporal/correction, UX, governance, architecture, and implementation authority.
* [`docs/canonical/governance/design-implementation-boundary.md`](docs/canonical/governance/design-implementation-boundary.md) — current planning/execution authority boundary.
* [`docs/008-implementation-reentry/`](docs/008-implementation-reentry/) — active implementation re-entry, plan refresh, and execution-readiness phase.

Numbered phase directories preserve rationale and planning history; canonical owners govern current meaning.

## Status

* Phase 001 — Concept Design Foundation: **Complete**
* Phase 002 — Concept Specification: **Complete**
* Phase 003 — Conceptual UX Architecture: **Complete**
* Phase 004 — Knowledge Architecture / OKF Governance: **Complete**
* Phase 005 — System/Application/Data/Synchronization Architecture: **Complete as historical architecture exit**
* Phase 006 — Implementation Planning & Delivery: **Historical after 006-D**
  * 006-A through 006-D: completed historical planning/bootstrap work
  * 006-D executable portion: retained and re-qualified by 008-B as the protected non-domain baseline
  * 006-E through 006-M: superseded as executable authority; retained as planning lineage
* Phase 007 — Jackson Design Refinement & Methodology Closure: **Complete — formal methodology exit passed**
* Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness: **In Progress**
  * 008-A — Implementation Re-entry Authority, Canonical Baseline, Change Control & Planning Guardrails: **Complete**
  * 008-B — Protected 006-D Baseline Qualification, Drift Audit & Toolchain/Environment Reconciliation: **Complete — PASS AFTER NARROW REMEDIATION**
  * 008-C — Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix: **Next**

## Current posture

The renewed Jackson Concept Design methodology is complete for the current MUDAC baseline. Implementation planning is active, but no executable domain slice has yet been authorized.

008-B has qualified the retained 006-D executable substrate for use as Phase 008 planning input. The qualification confirms that the current toolchain/lockfile, package/source skeleton, local PostgreSQL bootstrap, dependency enforcement, CI configuration, and separated resource-free OpenTofu roots remain coherent and contain no accidental MUDAC domain implementation.

The current boundary is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
008-C: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

A qualified bootstrap is not implementation authorization. Phase 008 remains planning, qualification, reconciliation, and authorization work. Only 008-L may authorize a first executable domain slice, and actual new domain implementation then begins in Phase 009.

## Qualified executable bootstrap

The retained bootstrap contains:

- minimal API/worker/web composition roots;
- six authoritative module package seams plus application/projection/foundation/test-support boundaries;
- local PostgreSQL as a development service without authoritative MUDAC schema;
- strict TypeScript/lint/format/dependency-boundary verification;
- Knowledge Validation, Implementation Verification, CodeQL, and Dependabot configuration;
- separated OpenTofu nonproduction, production, and recovery roots without AWS application resources.

008-B corrected two narrow drift items: stale bootstrap UI copy that still pointed to later Phase 006 slices, and an obsolete `phase-006-*` special push trigger in Implementation Verification.

Repository protection remains an external administration/evidence limit: no repository rulesets are currently visible and branch-protection state cannot be read through the connected integration. Dependabot is configured, but its alert inventory is not available through the current connector; neither control is overstated as clean/enforced.

## Current direction

Proceed to **008-C — Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix**.

008-C will map the accepted Phase 007 residual register and historical 006-E–M planning work into explicit current owners and dispositions before the detailed persistence/security/API/client/domain-slice plans are refreshed.
