# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md) and [`Downstream Architecture & Implementation Authority Quarantine`](docs/canonical/governance/downstream-authority-quarantine.md).
3. Read [Project Context & Purpose](docs/canonical/project/), [Concepts](docs/canonical/concepts/), [Synchronizations](docs/canonical/synchronizations/) and [Dependence](docs/canonical/dependence/).
4. Use [012-A](docs/012-concept-dependence-product-family-subset-scope/012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md) for Phase-012 semantics; treat [012-B](docs/012-concept-dependence-product-family-subset-scope/012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md) as provisional/candidate evidence only.
5. Use 012-C through [012-G](docs/012-concept-dependence-product-family-subset-scope/012-G-external-representation-release-dependence.md) for family-local decisions.
6. Use [012-H](docs/012-concept-dependence-product-family-subset-scope/012-H-whole-graph-transitivity-co-inclusion-optionality-minimal-unfamiliar-subsets.md) and [Whole-Graph Dependence & Subset Validation](docs/canonical/dependence/whole-graph-subset-validation.md) for the integrated dependence/subset model.
7. Use canonical synchronization owners for interaction rules; dependence never replaces composition.
8. Load older phase records only when rationale, alternatives, chronology or evidence materially help the current methodology question.

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
012-H: COMPLETE — PASS
012-I: NEXT
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

Never derive Concept dependence mechanically from synchronization, traceability, imports, schemas, service calls, UI layout, deployment topology, current workflow, or implementation convenience.

## Current direct dependence

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

Use transitivity rather than duplicating direct edges without a distinct application-role rationale.

## Whole-graph validation

012-H establishes:

```text
whole graph: ACYCLIC
mutual-dependence / co-inclusion cycles: NONE
new direct edge required by closure: NONE
```

`Award → Competition` is reachability-redundant through `Award → Team → Competition`, but remains semantically retained because Award scope and Award recipient are distinct roles.

Competition is the only universal **in-scope MUDAC family anchor**.

Every other Concept is globally optional. This means a coherent family variant exists without it; it does **not** mean the Concept is unimportant.

## Capability rules

Preserve at least:

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

Current Rank is Division-scoped. Current rank-derived Award capability therefore includes Division context without creating universal `Award → Division`.

Paper capture continuity does not universally require Export. Paper/electronic/mixed capture is a channel profile, not a Concept-subset axis.

## Validity versus scope

```text
dependence-valid
  != meaningful MUDAC family member
  != adopted in-scope variant
```

Do not treat singleton formal closures such as Access, Versioning, Provenance, Rubric or Export as supported products merely because they satisfy the direct graph.

012-I owns product-family scope selection.

## Coherent subset results to preserve

Dependence-coherent examples include:

- single-cohort operation without Division;
- ad-hoc Judge assignment without Panel;
- occurrence-history without Obligation/Scorecard;
- responsibility tracking without Occurrence/Scorecard;
- working Scorecard capture without Occurrence/Obligation;
- official outcome without Award;
- recognition without official declaration;
- judging/operation without Outcome Declaration;
- Export without Publication;
- official-but-non-public operation;
- public non-official material;
- discretionary Award without Division.

Conditional examples:

- no-Alias judging is coherent only when the variant does not claim the current blinded-judging profile;
- working Rubric/Scorecard may omit Versioning/Provenance only when no authoritative claim is made;
- no-Division ranked recognition requires Rank/Award policy/composition generalization if adopted.

Invalid examples include Publication without Export and any direct-edge closure violation.

## 012-I discipline

012-I must decide **scope**, not invent commercial tiers.

For each material coherent variant:

- classify it as in scope or coherent-but-out-of-scope;
- justify that decision from project purpose/mandate;
- identify capability-conditioned requirements;
- identify any variant-specific Phase-011 synchronization/policy revalidation;
- preserve capture channel as a profile rather than a false Concept variant;
- do not use implementation architecture or current UI as scope evidence.

## Reopening rules

- unjustified purpose/scope role → revisit the natural Phase-010 project/purpose owner;
- intrinsic Concept coupling → reopen the natural Phase-010 Concept owner;
- adopted subset exposes missing composition → reopen/refine the natural Phase-011 synchronization owner;
- derived mechanism appears to require Concept status → review upstream classification first;
- user-visible mapping issue without inclusion change → carry to Phase 013.

## Design-only rules for Phases 012–017

Do not resume implementation, derive Concept dependence from source/package/service/database structure, turn the dependence graph into architecture or implementation order, or design commercial tiers from Concept subsets.

Keep current meaning in canonical owners and exploratory/rejected reasoning in numbered phase history.

## Current next task

Proceed to:

> **012-I — Product-Family Variants, Scope Selection & Variant-Specific Composition Revalidation**
