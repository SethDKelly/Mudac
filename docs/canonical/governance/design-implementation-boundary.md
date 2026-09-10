---
type: Documentation Authority
title: Design / Implementation Boundary
description: Defines MUDAC's current post-Concept-Design posture, Phase 008 planning authority, qualified protected 006-D baseline, and the explicit gate before new domain implementation begins.
status: stable
tags: [governance, methodology, design, implementation, boundary, jackson, planning]
sources:
  - resource: ../../007-design-refinement/007-I-formal-jackson-concept-design-methodology-exit-accepted-residual-uncertainty-implementation-resume-boundary-decision.md
  - resource: ../../008-implementation-reentry/README.md
  - resource: ../../008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md
  - resource: ../../008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md
  - resource: change-governance.md
  - resource: methodology-terminology.md
  - resource: ../synchronizations/concept-synchronizations.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../policies/operational-exception-governance.md
  - resource: ../experience/action-authority-traceability.md
  - resource: ../implementation/runtime-delivery-bootstrap.md
  - resource: ../implementation/implementation-foundation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T17:23:00Z }
---

# Purpose

Keep the boundary between completed MUDAC Concept Design, active implementation planning, the qualified bootstrap substrate, future domain implementation, deployment authority, and production readiness explicit.

# Current state

MUDAC has formally exited the renewed Jackson Concept Design methodology for the current accepted baseline. 008-A established current implementation-planning authority and guardrails. 008-B has now qualified the retained 006-D executable substrate after narrow non-domain remediation.

The governing status is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
Phase 008 subdivision: COMPLETE
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
008-C: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

The formal design exit is scoped to the current baseline. New scope or a genuine later contradiction may require renewed design under canonical change governance.

# Current planning authority

Phase 008 follows the authority direction established in 008-A:

```text
canonical product / synchronization / policy / mechanism /
invariant / experience / governance meaning
        ↓
canonical architecture
        ↓
canonical implementation contracts
        ↓
Phase 008 implementation-planning decisions
        ↓
future executable realization and evidence
```

The Design / Implementation Boundary separately owns **execution posture**.

Historical phase records provide rationale/provenance. Routing artifacts route. Code, tests, schema, generated artifacts and IaC realize downstream choices. None silently replaces its upstream owner.

# Qualified protected 006-D baseline

008-B audited the retained non-domain workspace against current authority and found no semantic, architectural, or accidental-domain-implementation blocker.

The baseline is now qualified for later Phase 008 planning and contains only the accepted bootstrap class:

- pinned Node/pnpm/TypeScript/application-tool manifests and committed lockfile;
- minimal API, worker and browser composition roots;
- six authoritative module package seams without domain behavior;
- `application`, `projections`, `foundation`, and `test-support` boundaries;
- Docker Compose PostgreSQL without authoritative MUDAC schema/migrations;
- CI/static/dependency enforcement and supply-chain configuration;
- separate OpenTofu nonproduction/production/recovery roots without AWS application resources.

008-B repaired stale browser phase guidance and removed the historical `phase-006-*` special push trigger from Implementation Verification. Those were non-domain maintenance changes within the permitted boundary.

Qualification means the substrate may be relied upon as **planning input**. It does not authorize domain extension of that substrate.

# What Phase 008 planning authority permits

Current work may:

- use the qualified 006-D substrate as a concrete starting assumption;
- map 007-H/007-I residuals and historical 006-E–M work into current planning owners;
- refresh implementation slices and dependency ordering;
- define concrete downstream mechanisms where accepted architecture and semantics leave implementation latitude;
- create implementation decision records where `IMPL-015` warrants them;
- update canonical architecture/implementation owners when durable downstream contracts change;
- define verification/evidence gates and explicit implementation-entry criteria;
- prepare a specifically bounded first domain implementation slice for 008-L authorization.

# What Phase 008 does not authorize

Completion of 008-A or 008-B does **not** authorize domain implementation.

Until **008-L — Consolidated Dependency Graph, Implementation Roadmap, First-Slice Authorization & Phase Exit Review** explicitly authorizes a first executable slice, do not create new:

- authoritative domain PostgreSQL schemas, migrations, repositories, outbox or projections;
- Cognito/session/Identity/Participation/Access/invitation behavior;
- production domain commands, queries, APIs, transactions or idempotency behavior;
- IndexedDB domain Draft/synchronization behavior;
- Competition/Judging/Evaluation/Outcome/Award/Export/Publication feature behavior;
- domain-purpose AWS application provisioning/deployment.

The status distinctions remain:

```text
qualified bootstrap
    ≠
planning decision
    ≠
first executable slice authorized
    ≠
domain implementation started
    ≠
merge ready
    ≠
deployment ready
    ≠
production ready
```

008-L may authorize a Phase 009 entry slice. 008-L itself performs no domain implementation.

# Phase 006 treatment

Phase 006 remains historical implementation-planning/bootstrap provenance.

006-A through 006-D accurately record the prior planning/bootstrap work. The executable portion of 006-D has now been re-qualified by 008-B rather than silently resumed.

006-E through 006-M remain useful dependency reasoning but are superseded as current executable authority. 008-C owns their explicit preserve/split/merge/reorder/rename/supersede disposition against the current residual register and qualified baseline.

# Open evidence and administration limits

008-B revalidated two important limits:

1. the repository rulesets endpoint currently exposes no rulesets, while branch-protection status is unreadable by the current integration; therefore intended `IMPL-013` protection must not be claimed as enforced;
2. Dependabot configuration is visible, but the current connector does not expose its alert inventory for this audit; therefore zero open dependency findings must not be inferred.

Neither limit blocks continued Phase 008 planning. Both must remain visible to later planning/evidence gates where they become consequential.

# Change control during implementation planning

Completed Concept Design remains current semantic authority, not immutable dogma.

If planning or later implementation discovers a genuine canonical contradiction, missing independent Concept, impossible synchronization/authority requirement, unmodeled correction/history condition, or material new product scope, return through `CHG-*` and deliberate design as necessary.

If an implementation mechanism merely conflicts with current canonical meaning, the mechanism changes by default under `CHG-005` and `IMPL-001`.

Implementation inconvenience, framework preference, storage convenience, UI convenience, testing convenience, or technical/operator privilege alone does not authorize semantic weakening.

# Documentation and context boundary

Phase 008 follows `DOC-*` and `CTX-*`:

- canonical owners control durable current meaning;
- numbered Phase 008 records preserve planning rationale and evidence without becoming a parallel rule store;
- historical phases are loaded only when rationale, chronology, or supersession requires them;
- routing artifacts summarize and link rather than own rules;
- agents stop expanding context once the material authority set is sufficient.

No Phase 008-specific stable-rule namespace is created merely to restate existing governance.

# Current handoff

Proceed to **008-C — Residual-Risk Ingestion, Historical 006 Mapping, Decision Register & Supersession Matrix** under [Phase 008](../../008-implementation-reentry/).

008-C may rely on the qualified bootstrap as planning input, but new domain implementation remains **NOT STARTED** and no first executable slice is authorized until 008-L explicitly changes this boundary.