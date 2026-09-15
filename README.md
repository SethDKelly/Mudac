# MUDAC Competition Demo

MUDAC is a design-governed application effort for fair, traceable, resilient judging at live student data competitions.

The current product definition is representation-independent: volunteer Judges and competition Organizers need to conduct, preserve, coordinate and explain independent evaluation under real event-day constraints while protecting bias-sensitive identity, trustworthy authority and historical evidence.

## Start here

* [`AGENTS.md`](AGENTS.md) — repository-agent bootstrap and current design-only boundary.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/project/`](docs/canonical/project/) — current mandate and purpose baseline.
* [`docs/canonical/concepts/`](docs/canonical/concepts/) — current eighteen-Concept catalog established by Phase 010.
* [`docs/canonical/synchronizations/`](docs/canonical/synchronizations/) — current reconciled composition/synchronization authority after Phase 011.
* [`docs/canonical/dependence/`](docs/canonical/dependence/) — current Phase 012 accepted extrinsic inclusion-dependence authority, partial through 012-D.
* [`docs/012-concept-dependence-product-family-subset-scope/`](docs/012-concept-dependence-product-family-subset-scope/) — active Phase 012 dependence/product-family/subset/scope work.
* [`docs/012-concept-dependence-product-family-subset-scope/012-D-evaluation-structure-responsibility-basis-judgment-dependence.md`](docs/012-concept-dependence-product-family-subset-scope/012-D-evaluation-structure-responsibility-basis-judgment-dependence.md) — current evaluation-family dependence result.
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
012-D: COMPLETE — PASS
012-E: NEXT
```

## Current Concept catalog

Phase 010 canonically converged the model to eighteen Concepts:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

The former `Judging Encounter` and `Official Outcome Revision` paths remain deprecated historical adapters.

Coverage remains derived factual sufficiency with exception disposition separate; Aggregate, Rank and Readiness remain derived mechanisms; Reconciliation remains work/process context rather than an authority-owning Concept.

## Current Phase 012 dependence

Current canonical dependence is partial through 012-D.

Competition/actor/competitor direct edges are:

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

012-D adds the evaluation family:

```text
Evaluation Occurrence → Team / Participation / Rubric
Evaluation Obligation → Team / Participation / Rubric
Scorecard             → Team / Participation / Rubric
```

Team/Participation provide Competition transitively, and Participation provides Identity transitively.

A key 012-D result is that Evaluation Occurrence, Evaluation Obligation, and Scorecard are **not** an automatic co-inclusion group. The full current application synchronizes them, but coherent contractions can separately support occurrence history, responsibility tracking, or judgment capture. Rubric also remains independently useful as reusable evaluation-instrument definition.

These contractions are not adopted product variants yet. Phase 012-I owns scope selection; selected contractions may require variant-specific Phase-011 composition refinement.

## Completion runway

```text
010 project/purpose/discovery/specification/modularity          COMPLETE — PASS
  ↓
011 composition / synchronization revalidation                 COMPLETE — PASS
  ↓
012 dependence / product family / subsets / scope              IN PROGRESS — 012-E NEXT
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

Proceed to **012-E — Authority Lineage, Provenance & Correctability Dependence**.
