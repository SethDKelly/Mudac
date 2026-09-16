# Concept Dependence & Product-Family Inclusion

Current canonical knowledge for **extrinsic Concept inclusion dependence** and material **capability-conditioned co-inclusion** in the MUDAC application family.

Phase 012 owns this knowledge. It is distinct from intrinsic Concept specifications, Phase-011 synchronization/composition, and downstream implementation dependency.

## Current owner

- [MUDAC Application-Family Concept Dependence](application-family-dependence.md) — current direct edges, transitive consequences, explicit non-edges, capability rules, representative subsets, and scope carry-forwards.

## Current methodology state

```text
012-A  COMPLETE — READY
012-B  COMPLETE — PASS
012-C  COMPLETE — PASS
012-D  COMPLETE — PASS
012-E  COMPLETE — PASS
012-F  COMPLETE — PASS
012-G  COMPLETE — PASS
012-H  NEXT — Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets
```

All Concept-family dependence analysis is now complete through 012-G. 012-H validates the whole graph and capability model.

## Direct edge families

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

## Key separations

```text
Evaluation Occurrence / Evaluation Obligation / Scorecard
  are not a mandatory co-inclusion group

Award               ↛ Outcome Declaration
Outcome Declaration ↛ Award

Export              ↛ Publication
Outcome Declaration ↛ Export
Outcome Declaration ↛ Publication
Export              ↛ Outcome Declaration
Publication         ↛ Outcome Declaration
```

## Capability-conditioned rules

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

Current Rank is Division-scoped, so rank-derived recognition is Division-contextual without making `Award → Division` universal.

Paper capture continuity does not universally require Export. Export is required when a stable printable/external representation is itself part of the capability.

## Current scope rule

Every adopted in-scope MUDAC variant retains Competition as the live student-competition context. This scope rule does not imply direct `Competition → every optional capability` edges.

## Interpretation boundary

```text
intrinsic Concept dependence
  = upstream Concept-boundary defect

synchronization / composition
  = how included Concepts interact

extrinsic inclusion dependence
  = which Concepts must be co-included for the intended MUDAC role

capability-conditioned co-inclusion
  = a named capability requires a Concept set
    without making each Concept universally depend on that set

implementation dependency
  = out of scope
```

Do not infer edges from implementation structure, workflow, UI layout, traceability, or frequent synchronization alone.

## Next

Proceed to **012-H — Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets**.
