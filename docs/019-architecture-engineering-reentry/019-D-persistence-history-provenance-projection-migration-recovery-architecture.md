---
type: Architecture Decision
title: 019-D — Persistence, History, Provenance, Projection, Migration & Recovery Architecture
description: "Resolves ADQ-003 by comparing relational current-state plus explicit history, provider-neutral/hybrid persistence and event/log-oriented models, then accepts one logical PostgreSQL-compatible relational authority store with append-stable committed history/Provenance, rebuildable projections, forward-compatible migrations and authority-first recovery."
status: stable
tags: [phase-019, architecture, adq-003, persistence, history, provenance, projection, migration, recovery]
sources:
  - resource: ../canonical/architecture/persistence-history-recovery.md
  - resource: ../canonical/architecture/data-persistence.md
  - resource: ../canonical/architecture/architecture-drivers.md
  - resource: ../canonical/architecture/application-ownership-boundaries.md
  - resource: ../canonical/concepts/versioning.md
  - resource: ../canonical/concepts/provenance.md
  - resource: ../canonical/invariants/current-vs-historical-truth.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: ../canonical/governance/downstream-realization-obligations.md
  - resource: ../routing/phase019_architecture_decision_control.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T08:09:00-05:00 }
---

# Purpose

019-D resolves ADQ-003.

It establishes how MUDAC will persist authoritative current state, immutable committed history and Provenance, build non-authoritative projections, evolve schema safely, and recover from migration/storage/projection failure.

# 1. Entry state

~~~text
Phase 019                       ACTIVE
019-A/B/C                       COMPLETE
019-D                           NEXT ELIGIBLE / USER AUTHORIZED

ADQ-001                         ACCEPTED
ADQ-002                         ACCEPTED
ADQ-003                         PLANNED
ADQ-004..010                    PLANNED

Q4 repairs complete             1 / 4
technical probes                0

accepted whole architecture     false
implementation packages         0
implementation execution        false
~~~

# 2. Decision

**ADQ-003 — ACCEPTED.**

Selected architecture:

> **One logical PostgreSQL-compatible relational authority store with module-owned logical storage, explicit mutable-current versus immutable-committed history, append-stable Provenance, rebuildable non-authoritative projections, durable commit-coupled change propagation where asynchronous work is later selected, additive/forward-compatible migrations, and authority-first backup/restore and recovery.**

Current owner:

> docs/canonical/architecture/persistence-history-recovery.md

Stable rules:

> PST-001 through PST-016

# 3. Current semantic constraints

ADQ-003 preserves:

- ENG-006 — currentness/history/Provenance/correction must remain reconstructible;
- ENG-007 — current-state/concurrency/retry/uncertainty preserve owner truth;
- ENG-009 — calculated state remains distinct from official authority;
- ENG-010 — source/Export/Publication remain distinct;
- ENG-013 — recovery preserves truthful authority;
- ENG-015 — evidence strength matches claims;
- ENG-016 — migration/recovery controls precede implementation sprawl;
- ENG-017 — historical persistence architecture remains evidence;
- INV-003 / INV-005 / INV-010;
- DRV-001/002/003/005/010/011;
- BND-002/003/004/006/008/011/012.

# 4. Historical persistence candidate

Input:

> docs/canonical/architecture/data-persistence.md

Qualification:

~~~text
Q2 / Q3
QUALIFIED_COMPARISON_INPUT
authority = suspended-candidate
semantic repair required = false
technology revalidation required = true
~~~

The historical candidate contains strong current-compatible ideas:

- relational authority storage;
- one logical authority database initially;
- module-owned logical storage;
- stable identities;
- mutable Draft/current state distinct from committed Versions;
- append-stable Version/Provenance history;
- rebuildable/non-authoritative projections;
- transactional propagation intent;
- no baseline system-wide event sourcing.

019-D revalidated those principles against current DRV/BND/ENG authority.

The old document itself remains downstream candidate evidence.

# 5. Alternatives

## Alternative A — Adopt the historical PostgreSQL/RDS design unchanged

Strengths:

- mature relational model;
- strong integrity/transaction fit;
- existing candidate reasoning;
- compatible with AWS delivery target.

Weaknesses:

- conflates persistence family with later runtime/provider selection;
- names old module boundaries;
- assumes RDS/Multi-AZ before ADQ-009;
- does not fully specify migration/restore semantic readiness states.

**Rejected as-is.**

Its PostgreSQL-compatible relational family and several history/projection principles are retained in a new current owner.

## Alternative B — Provider-neutral relational/hybrid authority store

Use a relational authority model while postponing database-family selection.

Strengths:

- maximum provider/engine flexibility;
- lower early technology lock-in;
- compatible with current ownership/history requirements.

Weaknesses:

- leaves consequential relational capabilities too weakly specified for later implementation planning;
- would force later architecture to reopen database semantics such as constraint/transaction/history expectations;
- current AWS target and qualified PostgreSQL candidate make total engine-family neutrality less useful than explicit reversibility.

**Rejected as insufficiently specific.**

Provider hosting remains neutral, but the persistence family is selected as PostgreSQL-compatible.

## Alternative C — System-wide event sourcing / log-as-authority

Strengths:

- complete temporal event history;
- natural replay;
- potentially strong audit narrative.

Weaknesses:

- current Versioning already requires complete immutable authoritative snapshots rather than universal event reconstruction;
- not every meaningful product state transition is naturally an event-log aggregate;
- current workload does not justify event-sourcing operational/query complexity;
- projection/replay dependency would increase recovery and cognitive burden;
- introduces a stronger persistence paradigm than the semantic requirements demand.

**Rejected.**

Append-stable Version/Provenance/change records remain sufficient.

## Alternative D — PostgreSQL-compatible relational current state plus explicit append-stable semantic history

Strengths:

- aligns with transactional integrity and constrained current state;
- directly supports stable relationships and uniqueness;
- preserves immutable Version/Provenance history without requiring full event sourcing;
- keeps projections rebuildable and secondary;
- works naturally with the accepted modular monolith;
- preserves future service extraction;
- can be hosted by multiple PostgreSQL-compatible/runtime options later.

**Selected.**

# 6. Authoritative current versus historical state

The accepted structure preserves at least three distinct persistence meanings:

~~~text
working / Draft state
        !=
current committed authoritative state
        !=
retained historical authoritative state
~~~

A committed Version is immutable.

A superseded Version remains historical authority.

An invalidated Version remains retained but ineligible.

A lineage may have no current eligible Version.

These truths must be represented explicitly rather than inferred from row deletion or replacement.

# 7. Provenance

Meaningful Provenance remains append-stable.

Persistence must preserve, where applicable:

- Actor;
- RepresentedAuthority;
- Scope;
- source/capture channel;
- reason/authorizer;
- prior/resulting state references;
- correction/invalidation/replacement relation;
- material timing distinctions.

Technical logs remain separate observability evidence.

# 8. Database topology

The initial topology is:

~~~text
one logical PostgreSQL-compatible authority database
    ├─ Competition Context logical ownership
    ├─ Identity & Access logical ownership
    ├─ Evaluation logical ownership
    ├─ Outcomes & Officiality logical ownership
    ├─ External Representation logical ownership
    ├─ non-authoritative projection/read storage
    └─ narrow integration/change-propagation records
~~~

Exact schema names remain implementation detail.

Physical co-location does not allow cross-module storage bypass.

# 9. Projection model

Read projections may be denormalized and optimized aggressively.

They must be:

- non-authoritative;
- reconstructible from source authority;
- freshness/basis aware;
- safely markable stale/rebuilding/failed/unknown;
- disposable relative to authoritative state.

Projection loss is repaired by rebuild.

High-consequence commands do not trust a projection as sole precondition authority.

# 10. Change propagation

If later ADQs use asynchronous processing, authoritative mutation and durable propagation intent must be committed together.

The selected requirement is semantic equivalence to a transactional outbox.

019-D does not yet choose:

- event broker;
- queue;
- dispatcher;
- exact outbox schema;
- event serialization.

Those belong to later interface/runtime decisions.

# 11. Migration posture

Schema/data evolution is additive-first and owner-scoped.

A consequential migration must document:

- owner;
- forward change;
- compatibility period;
- backfill/transformation;
- validation;
- current/history/Provenance impact;
- rollback or roll-forward-only rationale;
- recovery from partial completion.

Destructive contraction occurs only after compatibility and historical-retention obligations are satisfied.

Exact migration tooling is deferred to Phase 020.

# 12. Backup and restore posture

The recovery target is not merely database restoration.

It is:

~~~text
authoritative database restored
        ↓
current/history/Provenance consistency verified
        ↓
projection state rebuilt
        ↓
integration/change propagation reconciled
        ↓
service readiness established
~~~

A restored but semantically inconsistent database is not application recovery.

RTO/RPO, backup frequency, retention, replicas and Multi-AZ remain 019-J decisions/evidence.

# 13. Failure and uncertainty

Persistence/recovery must preserve:

~~~text
unknown != failed != succeeded
stale projection != current authority
partial migration != valid completed migration
restore complete != application ready
~~~

If an operation's authoritative result is uncertain, recovery checks current owner state rather than inventing a completion result.

# 14. Core relational modeling posture

Core semantic fields remain explicit.

Semi-structured storage is acceptable only for genuinely extensible descriptive metadata.

JSON/semi-structured columns cannot hide:

- lifecycle;
- Access;
- evaluation identity;
- scoring/evaluation basis;
- Version currentness;
- outcome authority;
- canonical constraints.

# 15. Evidence

Acceptance evidence class:

> **DOCUMENTATION_REASONING**

No technical probe is required to accept the architecture family.

Runtime claims such as exact PostgreSQL performance, failover behavior, managed-service recovery, backup guarantees or provider-specific limits remain unproven and belong to later evidence.

# 16. Reversibility / lock-in

This decision introduces intentional PostgreSQL-family coupling.

Accepted reasons:

- strong match to relational identity/integrity requirements;
- mature transaction/constraint model;
- current AWS target has plausible managed realizations;
- one logical database fits the modular-monolith boundary;
- migration away remains possible through owner-scoped contracts and stable application identities.

Not accepted yet:

- RDS-specific APIs;
- Aurora-specific behavior;
- database-per-service assumptions;
- provider-specific replication/failover semantics.

# 17. Residual uncertainty

Still open:

- exact PostgreSQL-compatible runtime/provider;
- exact ORM/query builder;
- exact migration tool;
- exact table/schema layout;
- exact cross-module FK policy;
- exact transaction/isolation choices;
- exact outbox/queue mechanics;
- exact backup interval and retention;
- exact RTO/RPO;
- jurisdiction-specific retention/deletion requirements;
- projection storage technology.

These questions are assigned to ADQ-005, ADQ-009 or Phase 020 as appropriate.

# 18. Scenario impact

ADQ-003 directly constrains:

- post-finalization correction;
- affected Outcome Declaration with the same visible winner;
- stale Export after source correction.

It also supplies persistence/recovery prerequisites for retry, offline convergence and unknown-result scenarios.

# 19. Risk disposition

## ERI-02 — historical candidate mistaken for accepted architecture

**Controlled.**

Current authority is PST-*; DATA-* remains candidate evidence.

## ERI-03 — architecture emerges from executable scaffold

**Controlled.**

The selected persistence family is justified from semantic/quality evidence, not existing code.

## ERI-09 — cross-owner coupling

**Further reduced.**

One database is accepted, but BND ownership prohibits direct cross-module storage authority and destructive coupling.

## Migration/recovery risk

**Bounded and carried forward.**

PST-014 through PST-016 establish architecture requirements. Exact tools, measurable recovery targets and executable evidence remain later work.

# 20. Implementation boundary

After 019-D:

~~~text
accepted bounded decisions       3 / 10
Q4 repairs complete              1 / 4
technical probes                 0

accepted whole architecture      false

implementation packages          0
package derivation               false
implementation execution         false
~~~

G0 remains unsatisfied.

# 21. Exit decision

**019-D — COMPLETE — PASS.**

**ADQ-003 — ACCEPTED.**

Next eligible:

> **019-E — Identity, Authentication, Participation, Access, Session & Technical-Authority Architecture**

019-E is not automatically authorized.
