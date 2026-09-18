# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md).
3. Read current [Project](docs/canonical/project/), [Concepts](docs/canonical/concepts/), [Synchronizations](docs/canonical/synchronizations/) and [Dependence](docs/canonical/dependence/).
4. Use [MUDAC Product-Family Scope](docs/canonical/dependence/product-family-scope.md) for PF-01.
5. Read the final [Phase 013 Mapping Authority Baseline](docs/canonical/experience/mapping-authority-baseline.md).
6. Read current accepted Experience owners relevant to the work, especially [Whole-Experience Action, Explanation & Authority Traceability](docs/canonical/experience/action-authority-traceability.md).
7. For current methodology work, read [Phase 014 — Familiarity, Reuse & Genericity](docs/014-familiarity-reuse-genericity/).
8. Treat older Experience adapters as historical evidence unless the Mapping Authority Baseline says otherwise.
9. Use current synchronization owners for composition; mapping does not replace composition.
10. Do not preload architecture/implementation except for explicit contamination/history analysis.

## Current methodology posture

```text
009: COMPLETE — PASS
010: COMPLETE — PASS
011: COMPLETE — PASS
012: COMPLETE — PASS
013: COMPLETE — PASS
014: NOT STARTED — START GATE NEXT
architecture authority: SUSPENDED
implementation-planning authority: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

## Current Concept authority

The canonical catalog contains eighteen Concepts:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

`Judging Encounter` and `Official Outcome Revision` remain deprecated historical adapters.

Coverage, Aggregate, Rank and Readiness remain derived mechanisms. Reconciliation and Live Operations remain work/process contexts rather than Concepts.

## Final Phase-013 mapping authority

Preserve:

- Identity != Participation != Access;
- Panel membership != Evaluation Occurrence participation != Evaluation Obligation != Scorecard evidence;
- one Evaluation Obligation maps to at most one logical Scorecard;
- Scorecard Draft != authority;
- capture Actor != Judge semantic author / RepresentedAuthority;
- Judge amendment != source-faithful capture correction;
- supersession != invalidation != replacement != affectedness/staleness;
- historical obligation satisfaction != current evidence eligibility;
- Event Completed != universal hidden Access revocation;
- Remaining Work = current Outstanding-obligation projection;
- Coverage factual state != exception disposition;
- Rank is derived/non-editable;
- calculated != recognized != Competition Finalized != official != public != delivered;
- Outcome Declaration != Export != Publication != delivery;
- actor Access != audience disclosure permission;
- Export currency != Publication distribution state;
- successor Outcome Declaration != successor Export != successor Publication;
- withdrawal/supersession never erases historical release or external copies;
- accessible/responsive/degraded/paper paths preserve the same domain semantics;
- assistance does not transfer semantic authorship;
- device/session/route/QR possession != current Access;
- local working state != confirmed persistence != authoritative domain state;
- unknown authoritative result != confirmed success or confirmed failure;
- retry/recovery must reconcile current authority and converge rather than duplicate effects;
- stale local state cannot overwrite newer authority;
- status is multidimensional and subject-qualified;
- technical recovery privilege != broader Access, disclosure or domain authority.

Map the established action surface:

```text
D — direct application action
C — coordinated application action
P — composition-only participant
S — system-triggered conceptual reaction
X — intentionally unavailable generic application action
```

Do not expose `P` or `X` as generic user actions.

## Explanation-order rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
explanation order != mandatory screen order
```

The final Phase-013 Experience corpus is complete and non-competing. `reconciliation-finalization.md` and `paper-export-publication.md` remain historical evidence only.

## Phase 014 boundary

Phase 014 evaluates familiarity, reuse and genericity of the existing design. It must not treat familiar implementation/UI conventions as authority, merge Concepts merely because they resemble one another, or introduce abstraction for abstraction's sake.

The start gate owns Phase-014 subgroup planning before substantive work.

## Current next task

Proceed to:

> **Phase 014 start gate — Familiarity, Reuse & Genericity**
