# Concept Dependence & Product-Family Inclusion

Current canonical knowledge for **extrinsic Concept inclusion dependence** in the MUDAC application family.

Phase 012 owns this knowledge. It is distinct from intrinsic Concept specifications, Phase 011 synchronization/composition, and downstream implementation dependency.

## Current owner

- [MUDAC Application-Family Concept Dependence](application-family-dependence.md) — current accepted direct edges, transitive consequences, explicit non-edges and conditional capability/scope rules.

## Current methodology state

```text
012-A  COMPLETE — READY
012-B  COMPLETE — PASS
012-C  COMPLETE — PASS
012-D  COMPLETE — PASS
012-E  NEXT — Authority Lineage, Provenance & Correctability Dependence
```

The canonical graph is intentionally **partial through 012-D**. Later Phase 012 subgroups extend the same owner as additional concept families are resolved.

## Current direct edge families

### Competition / actor / competitor context

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
Evaluation Occurrence → Team
Evaluation Occurrence → Participation
Evaluation Occurrence → Rubric

Evaluation Obligation → Team
Evaluation Obligation → Participation
Evaluation Obligation → Rubric

Scorecard             → Team
Scorecard             → Participation
Scorecard             → Rubric
```

Evaluation edges inherit Competition through Team/Participation and Identity through Participation.

## Important evaluation non-edges

Occurrence, Obligation, and Scorecard are not a mandatory inclusion cycle. Each can support a coherent limited application role without the other two.

Rubric also remains independently meaningful as reusable evaluation-instrument definition.

Those contractions are dependence-valid only; Phase 012-I determines scope adoption.

## Current scope rule

Every in-scope MUDAC product/application variant retains Competition as the live student-competition context.

This scope rule does not imply that Competition directly depends on every optional capability.

## Interpretation boundary

```text
intrinsic Concept dependence
  = upstream Concept-boundary defect

synchronization / composition
  = how included Concepts interact

extrinsic inclusion dependence
  = which Concepts must be co-included for the intended MUDAC role

implementation dependency
  = out of scope
```

Do not infer edges from imports, schemas, service calls, UI layout, deployment topology, current workflows, or synchronization alone.

## Next

Proceed to **012-E — Authority Lineage, Provenance & Correctability Dependence**.
