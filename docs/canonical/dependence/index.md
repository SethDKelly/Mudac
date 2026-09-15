# Concept Dependence & Product-Family Inclusion

Current canonical knowledge for **extrinsic Concept inclusion dependence** and material **capability-conditioned co-inclusion** in the MUDAC application family.

Phase 012 owns this knowledge. It is distinct from intrinsic Concept specifications, Phase-011 synchronization/composition, and downstream implementation dependency.

## Current owner

- [MUDAC Application-Family Concept Dependence](application-family-dependence.md) — current accepted direct edges, transitive consequences, explicit non-edges, conditional capability rules, and authority-profile co-inclusion.

## Current methodology state

```text
012-A  COMPLETE — READY
012-B  COMPLETE — PASS
012-C  COMPLETE — PASS
012-D  COMPLETE — PASS
012-E  COMPLETE — PASS
012-F  COMPLETE — PASS
012-G  NEXT — External Representation & Release Dependence
```

The canonical model is intentionally **partial through 012-F**. External representation/release remains unresolved until 012-G.

## Current direct edge families

### Competition / actor / competitor

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

### Evaluation

```text
Evaluation Occurrence → Team / Participation / Rubric
Evaluation Obligation → Team / Participation / Rubric
Scorecard             → Team / Participation / Rubric
```

### Outcome / recognition

```text
Award               → Competition
Award               → Team
Outcome Declaration → Competition
```

## Key non-cycles

```text
Evaluation Occurrence / Evaluation Obligation / Scorecard
  are not a mandatory co-inclusion group

Award               ↛ Outcome Declaration
Outcome Declaration ↛ Award
```

Outcome Declaration also does not gain direct Team/Scorecard/Obligation/Occurrence/Rubric edges solely from basis traceability.

## Authority-profile co-inclusion

012-E remains current:

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance

Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance

Rubric/Scorecard authoritative correction or invalidation
  ⇒ Versioning + Provenance
```

Versioning and Provenance remain distinct support Concepts rather than universal sinks.

## Outcome capability rules

```text
Ordinary Official Closeout
  ⇒ Competition + Outcome Declaration

Rank-Derived Award capability
  ⇒ Award + legitimate Ranking Ready supplied Rank basis
```

Current Rank is Division-scoped; that makes current rank-derived recognition Division-contextual without establishing universal `Award → Division`.

Any official Outcome Declaration requires a reconstructible accepted OutcomeBasis, but the exact source Concept set is variant-specific rather than one fixed direct graph bundle.

## Current scope rule

Every in-scope MUDAC product/application variant retains Competition as the live student-competition context.

This does not imply Competition directly depends on every optional capability.

## Interpretation boundary

```text
intrinsic Concept dependence
  = upstream Concept-boundary defect

synchronization / composition
  = how included Concepts interact

extrinsic inclusion dependence
  = which Concepts must be co-included for the intended MUDAC role

capability-conditioned co-inclusion
  = a named application capability requires a Concept set
    without making every underlying Concept universally depend on that set

implementation dependency
  = out of scope
```

Do not infer edges from imports, schemas, service calls, UI layout, deployment topology, current workflows, or traceability alone.

## Next

Proceed to **012-G — External Representation & Release Dependence**.
