# MUDAC Competition Demo

MUDAC is a design-governed application effort for fair, traceable, resilient judging at live student data competitions.

The current product definition is representation-independent: volunteer Judges and competition Organizers need to conduct, preserve, coordinate and explain independent evaluation under real event-day constraints while protecting bias-sensitive identity, trustworthy authority and historical evidence.

## Start here

* [`AGENTS.md`](AGENTS.md) — repository-agent bootstrap and current design-only boundary.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/project/`](docs/canonical/project/) — current mandate and purpose baseline.
* [`docs/canonical/concepts/`](docs/canonical/concepts/) — current eighteen-Concept catalog established by Phase 010.
* [`docs/canonical/synchronizations/`](docs/canonical/synchronizations/) — current reconciled composition/synchronization authority after Phase 011.
* [`docs/canonical/dependence/`](docs/canonical/dependence/) — current Phase 012 accepted extrinsic inclusion-dependence authority, partial through 012-C.
* [`docs/012-concept-dependence-product-family-subset-scope/`](docs/012-concept-dependence-product-family-subset-scope/) — active Phase 012 dependence/product-family/subset/scope work.
* [`docs/012-concept-dependence-product-family-subset-scope/012-C-competition-actor-competitor-context-bias-control-dependence.md`](docs/012-concept-dependence-product-family-subset-scope/012-C-competition-actor-competitor-context-bias-control-dependence.md) — current accepted Competition/actor/competitor/bias-control dependence result.
* [`docs/canonical/governance/design-implementation-boundary.md`](docs/canonical/governance/design-implementation-boundary.md) — current execution/readiness boundary.

## Current status

```text
Jackson Concept Design: REOPENED / IN PROGRESS
007-I previous closure: SUPERSEDED AS CURRENT CLOSURE AUTHORITY
008 implementation re-entry: HALTED AFTER 008-E
006-D executable bootstrap: FROZEN HISTORICAL NON-DOMAIN SUBSTRATE
architecture: SUSPENDED PENDING DESIGN CLOSURE
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
009 methodology realignment: COMPLETE — PASS
010 foundational completion: COMPLETE — PASS
011 composition/synchronization revalidation: COMPLETE — PASS
012 dependence/product-family/subset/scope: IN PROGRESS
012-A: COMPLETE — READY
012-B: COMPLETE — PASS
012-C: COMPLETE — PASS
012-D: NEXT
```

## Current Concept catalog

Phase 010 canonically converged the model to eighteen Concepts:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

The former `Judging Encounter` and `Official Outcome Revision` paths remain deprecated historical adapters.

Coverage remains derived factual sufficiency with exception disposition separate; Aggregate, Rank and Readiness remain derived mechanisms; Reconciliation remains work/process context rather than an authority-owning Concept.

## Current Phase 012 dependence

012-C establishes the first durable direct edges:

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

The graph is minimal: Division/Alias reach Competition through Team, and Panel reaches Competition/Identity through Participation.

Current explicit universal non-edges include:

```text
Competition ↛ Division
Competition ↛ Panel
Team        ↛ Alias
Identity    ↛ Competition
Identity    ↛ Participation
Access      ↛ Participation
Access      ↛ Identity
```

These non-edges do not remove current composition requirements. Protected Judge/Organizer actions still use Participation-derived context for Access.

Competition is the family anchor for every in-scope MUDAC variant, but that scope rule does not imply Competition depends on every optional capability.

Division remains optional for single-cohort operation; Panel remains optional for ad-hoc evaluator assignment; Alias is required for variants claiming the current blinded-judging role but is not a universal Team dependency.

A single-cohort no-Division variant is dependence-coherent but would require later policy/composition revalidation before adoption because current disclosure policy names Division in the blinded Judge-facing representation.

## Completion runway

```text
010 project/purpose/discovery/specification/modularity          COMPLETE — PASS
  ↓
011 composition / synchronization revalidation                 COMPLETE — PASS
  ↓
012 dependence / product family / subsets / scope              IN PROGRESS — 012-D NEXT
  ↓
013 mapping / interaction / representation revalidation
  ↓
014 familiarity / reuse / genericity
  ↓
015 integrity / cross-concept interference
  ↓
016 scenario / misfit / exception / failure / adversarial validation
  ↓
017 methodology completeness / canonical consolidation / closure
```

`GitHub → GitHub Actions → AWS ecosystem` remains only a downstream delivery constraint and does not shape Concept Design.

## Downstream work

Phase 005 architecture, Phase 006 implementation planning/bootstrap and Phase 008 planning remain preserved as historical/downstream evidence. They are not current Concept Design constraints.

A successful future Phase 017 may establish readiness for a **separate architecture/engineering re-entry**. It will not automatically reactivate Phase 008 or authorize coding.

## Current direction

Proceed to **012-D — Evaluation Structure, Responsibility, Basis & Judgment Dependence**.
