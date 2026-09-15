# MUDAC Competition Demo

MUDAC is a design-governed application effort for fair, traceable, resilient judging at live student data competitions.

The current product definition is representation-independent: volunteer Judges and competition Organizers need to conduct, preserve, coordinate and explain independent evaluation under real event-day constraints while protecting bias-sensitive identity, trustworthy authority and historical evidence.

## Start here

* [`AGENTS.md`](AGENTS.md) — repository-agent bootstrap and current design-only boundary.
* [`docs/index.md`](docs/index.md) — preferred OKF progressive-disclosure entry point.
* [`docs/canonical/project/`](docs/canonical/project/) — current mandate and purpose baseline.
* [`docs/canonical/concepts/`](docs/canonical/concepts/) — current eighteen-Concept catalog established by Phase 010.
* [`docs/canonical/synchronizations/`](docs/canonical/synchronizations/) — current reconciled composition/synchronization authority after Phase 011.
* [`docs/canonical/dependence/`](docs/canonical/dependence/) — current Phase 012 dependence/capability authority, partial through 012-F.
* [`docs/012-concept-dependence-product-family-subset-scope/`](docs/012-concept-dependence-product-family-subset-scope/) — active Phase 012 work.
* [`docs/012-concept-dependence-product-family-subset-scope/012-F-outcome-recognition-official-authority-dependence.md`](docs/012-concept-dependence-product-family-subset-scope/012-F-outcome-recognition-official-authority-dependence.md) — current outcome/recognition dependence result.
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
012-E: COMPLETE — PASS
012-F: COMPLETE — PASS
012-G: NEXT
```

## Current Concept catalog

Phase 010 canonically converged the model to eighteen Concepts:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

The former `Judging Encounter` and `Official Outcome Revision` paths remain deprecated historical adapters.

Coverage remains derived factual sufficiency with exception disposition separate; Aggregate, Rank and Readiness remain derived mechanisms; Reconciliation remains process/work context rather than an authority-owning Concept.

## Current Phase 012 dependence

The current direct graph includes:

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
```

The graph deliberately does **not** collapse Evaluation Occurrence/Obligation/Scorecard or Award/Outcome Declaration into mandatory cycles.

012-E authority profiles remain:

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance

Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance
```

012-F preserves:

```text
Award               ↛ Outcome Declaration
Outcome Declaration ↛ Award
```

and rejects direct Outcome Declaration → Team/Scorecard/Obligation/Occurrence/Rubric edges based only on traceability.

Current capability rules include:

```text
Ordinary Official Closeout
  ⇒ Competition + Outcome Declaration

Rank-Derived Award capability
  ⇒ Award + legitimate Ranking Ready supplied Rank basis
```

Current Rank is Division-scoped, so rank-derived recognition is Division-contextual without making `Award → Division` universal.

Official OutcomeBasis must be reconstructible, but its exact source Concept set is variant-specific.

## Completion runway

```text
010 project/purpose/discovery/specification/modularity          COMPLETE — PASS
  ↓
011 composition / synchronization revalidation                 COMPLETE — PASS
  ↓
012 dependence / product family / subsets / scope              IN PROGRESS — 012-G NEXT
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

A successful future Phase 017 may establish readiness for a separate architecture/engineering re-entry. It will not automatically reactivate prior implementation planning or authorize coding.

## Current direction

Proceed to **012-G — External Representation & Release Dependence**.
