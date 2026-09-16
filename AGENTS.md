# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md) and [`Downstream Architecture & Implementation Authority Quarantine`](docs/canonical/governance/downstream-authority-quarantine.md).
3. Read [Project Context & Purpose](docs/canonical/project/), [Concepts](docs/canonical/concepts/), [Synchronizations](docs/canonical/synchronizations/) and [Dependence](docs/canonical/dependence/).
4. Use [012-A](docs/012-concept-dependence-product-family-subset-scope/012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md) for Phase-012 semantics; treat [012-B](docs/012-concept-dependence-product-family-subset-scope/012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md) as candidate evidence only.
5. Use 012-C through [012-G](docs/012-concept-dependence-product-family-subset-scope/012-G-external-representation-release-dependence.md) plus [MUDAC Application-Family Concept Dependence](docs/canonical/dependence/application-family-dependence.md) for accepted current dependence.
6. Use canonical synchronization owners for current interaction rules; dependence never replaces composition.
7. Load older phase records only when rationale, alternatives, chronology or evidence materially help the current methodology question.

## Current methodology posture

```text
Jackson Concept Design: REOPENED / IN PROGRESS
007-I previous closure: SUPERSEDED AS CURRENT CLOSURE AUTHORITY
008 implementation re-entry: HALTED AFTER 008-E
006-D bootstrap: FROZEN HISTORICAL NON-DOMAIN SUBSTRATE
architecture authority: SUSPENDED
implementation-planning authority: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
009: COMPLETE — PASS
010: COMPLETE — PASS
011: COMPLETE — PASS
012: IN PROGRESS
012-A: COMPLETE — READY
012-B: COMPLETE — PASS
012-C: COMPLETE — PASS
012-D: COMPLETE — PASS
012-E: COMPLETE — PASS
012-F: COMPLETE — PASS
012-G: COMPLETE — PASS
012-H: NEXT
```

## Current Concept authority

The canonical catalog contains eighteen Concepts:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

`Judging Encounter` and `Official Outcome Revision` remain deprecated historical adapters.

Coverage, Aggregate, Rank and Readiness remain derived mechanisms. Reconciliation remains process/work context. Recovery/Continuity remains a cross-cutting purpose obligation.

## Composition authority

Phase 011 remains authoritative for how included Concepts interact. Preserve:

- Identity continuity ≠ Participation authority ≠ Access permission;
- Panel membership ≠ occurrence participation ≠ Evaluation Obligation responsibility ≠ Scorecard evidence;
- Scorecard Draft ≠ authority;
- Versioning ≠ semantic authorship;
- Provenance ≠ domain authority;
- historical satisfaction ≠ current evidence eligibility;
- missing evidence is never zero;
- Coverage/Aggregate/Rank ≠ Award authority ≠ official declaration;
- Competition Finalization ≠ Outcome Declaration;
- calculated ≠ recognized ≠ official ≠ public ≠ delivered;
- source authority ≠ Export representation ≠ Publication release ≠ transport delivery.

Governing automation rule:

> **Automation may propagate knowledge/currentness and execute already-authorized bounded composition consequences; automation may not manufacture semantic authority.**

## Dependence semantics

```text
intrinsic Concept dependence
  = upstream Concept-boundary defect

synchronization/composition
  = how already-included Concepts interact

extrinsic inclusion dependence
  = including A requires B for A's intended MUDAC role

capability-conditioned co-inclusion
  = a named application capability requires a Concept set
    without making each Concept universally depend on that set

implementation dependency
  = out of scope
```

Do not derive dependence from synchronization, traceability, imports, schemas, service calls, UI layout, deployment topology, or ordinary workflow.

## Current direct dependence through 012-G

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation

Evaluation Occurrence → Team / Participation / Rubric
Evaluation Obligation → Team / Participation / Rubric
Scorecard             → Team / Participation / Rubric

Award               → Competition
Award               → Team
Outcome Declaration → Competition

Publication → Export
```

Use transitivity rather than duplicating edges without a distinct role rationale.

## Key non-cycles and separations

Do not turn ordinary composition into mandatory inclusion:

```text
Evaluation Occurrence / Evaluation Obligation / Scorecard
  are not a co-inclusion cycle

Award               ↛ Outcome Declaration
Outcome Declaration ↛ Award

Export              ↛ Publication
Outcome Declaration ↛ Export
Outcome Declaration ↛ Publication
Export              ↛ Outcome Declaration
Publication         ↛ Outcome Declaration
```

Outcome Declaration has no direct Team/Scorecard/Obligation/Occurrence/Rubric edge merely because its accepted basis can be traced to those sources.

## Capability rules

Preserve:

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance

Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance

Ordinary Official Closeout
  ⇒ Competition + Outcome Declaration

Rank-Derived Award capability
  ⇒ Award + legitimate Ranking Ready supplied Rank basis

External Representation
  ⇒ Export + exact SourceBasis + RepresentationProfile + AudienceProfile

Public Official-Result Release
  ⇒ Outcome Declaration + Export + Publication
```

Current Rank is Division-scoped, making current rank-derived recognition Division-contextual without universal `Award → Division`.

Paper capture continuity does not universally require Export. Export is required only where a stable printable/external representation is part of the capability.

## Externalization discipline

`Publication → Export` is current application-family dependence because Export is the MUDAC owner of stable source-bound representation identity/currentness.

Do not infer the reverse edge. Generated Export can remain internal/unreleased.

Do not make official authority depend on externalization. Official-but-non-public is coherent.

Do not make Publication depend on Outcome Declaration. Legitimate non-official material can be published.

Publication means authorized release, not delivery success. Delivery/transport remains downstream realization.

## Canonical dependence authority

[`docs/canonical/dependence/application-family-dependence.md`](docs/canonical/dependence/application-family-dependence.md) is current dependence authority through all family-local analysis completed in 012-G.

012-H now owns whole-graph validation: transitive closure, genuine co-inclusion groups/cycles, optionality, minimal meaningful subsets, unfamiliar subsets, redundant edges, and consistency between direct edges and capability rules.

## Approved Phase 012 order

```text
012-A  scope / semantics / questions / plan                            COMPLETE — READY
012-B  application-family roles / candidate inventory                  COMPLETE — PASS
012-C  Competition / actor / competitor / bias-control dependence      COMPLETE — PASS
012-D  evaluation structure / responsibility / basis / judgment        COMPLETE — PASS
012-E  authority lineage / Provenance / correctability                  COMPLETE — PASS
012-F  outcome / Award / official-authority dependence                  COMPLETE — PASS
012-G  Export / Publication / external-representation dependence        COMPLETE — PASS
012-H  whole graph / transitivity / co-inclusion / minimal subsets      NEXT
012-I  product-family variants / scope / composition revalidation       PLANNED
012-J  counterexamples / upstream reopen / Phase 013 handoff audit      PLANNED
012-K  canonical reconciliation / Phase 012 exit / Phase 013 handoff    PLANNED
```

## Reopening rules

- unjustified purpose/scope role → revisit the natural Phase-010 project/purpose owner;
- intrinsic Concept coupling → reopen the natural Phase-010 Concept owner;
- accepted subset exposes missing composition → reopen/refine the natural Phase-011 synchronization owner;
- derived mechanism appears to require Concept status → review upstream classification first;
- user-visible mapping issue without inclusion change → carry to Phase 013.

## Design-only rules for Phases 012–017

Do not resume implementation, derive Concept dependence from source/package/service/database structure, turn the dependence graph into architecture or implementation order, or design commercial tiers from Concept subsets.

Keep accepted current meaning in canonical owners and rejected/counterexample reasoning in numbered phase history.

## Current next task

Proceed to:

> **012-H — Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets**
