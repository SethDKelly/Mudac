# Concept Dependence & Product-Family Inclusion

Current canonical knowledge for **extrinsic Concept inclusion dependence**, material **capability-conditioned co-inclusion**, and whole-graph subset validation in the MUDAC application family.

Phase 012 owns this knowledge. It remains distinct from intrinsic Concept specifications, Phase-011 synchronization/composition, and downstream implementation dependency.

## Current owners

- [MUDAC Application-Family Concept Dependence](application-family-dependence.md) — current direct edges, universal non-edges and capability-conditioned rules established through family-local analysis.
- [Whole-Graph Dependence & Subset Validation](whole-graph-subset-validation.md) — current whole-model acyclicity, transitive closure, optionality, minimal closures, unfamiliar-subset validation and the scope-decision set for 012-I.

## Current methodology state

```text
012-A  COMPLETE — READY
012-B  COMPLETE — PASS
012-C  COMPLETE — PASS
012-D  COMPLETE — PASS
012-E  COMPLETE — PASS
012-F  COMPLETE — PASS
012-G  COMPLETE — PASS
012-H  COMPLETE — PASS
012-I  NEXT — Product-Family Variants, Scope Selection & Variant-Specific Composition Revalidation
```

## Whole-graph result

012-H validates the current model without adding a new direct edge:

```text
whole direct graph: ACYCLIC
strongly connected Concept groups > 1: NONE
new direct edge required by closure: NONE
```

Competition is the only universal **in-scope MUDAC family anchor**. Every other Concept is globally optional, while named capabilities may make particular Concepts mandatory.

`Award → Competition` is reachability-redundant through `Award → Team → Competition`, but remains semantically retained because recognition scope and recipient type are distinct Award-role reasons.

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

Current rank-derived recognition is Division-contextual because current Rank is Division-scoped, without creating universal `Award → Division`.

## Validity versus scope

```text
dependence-valid
  != meaningful MUDAC family member
  != adopted in-scope variant
```

012-H confirms many unfamiliar reductions are coherent, including single-cohort/no-Division, ad-hoc/no-Panel, judging-only, official-without-Award, official-but-non-public, Export-without-Publication, and public non-official material. Publication-without-Export remains invalid.

Working-only evaluation may omit Versioning/Provenance; authoritative evaluation may not.

Paper versus electronic capture is a channel profile, not a Concept-subset axis.

## Interpretation boundary

Do not infer Concept edges from implementation structure, current workflow, UI layout, traceability, synchronized action, or deployment topology.

Do not interpret optionality as low value. It means only that at least one coherent family variant omits the Concept.

## Next

Proceed to **012-I — Product-Family Variants, Scope Selection & Variant-Specific Composition Revalidation**.
