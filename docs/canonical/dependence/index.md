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
012-D  NEXT — Evaluation Structure, Responsibility, Basis & Judgment Dependence
```

The canonical graph is intentionally **partial through 012-C**. Later Phase 012 subgroups will extend the same owner as additional concept families are resolved.

## Current direct edge set

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

## Current scope rule

Every in-scope MUDAC product/application variant retains Competition as the live student-competition context.

This scope rule does not imply that Competition directly depends on every optional capability.

## Current explicit universal non-edges

```text
Competition ↛ Division
Competition ↛ Panel
Team        ↛ Alias
Identity    ↛ Competition
Identity    ↛ Participation
Access      ↛ Participation
Access      ↛ Identity
```

Protected Judge/Organizer actions still use Participation-derived context for Access through current synchronization semantics; that is not a universal Concept-inclusion edge.

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

Proceed to **012-D — Evaluation Structure, Responsibility, Basis & Judgment Dependence**.
