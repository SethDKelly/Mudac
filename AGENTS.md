# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md).
3. Read current [Project](docs/canonical/project/), [Concepts](docs/canonical/concepts/), [Synchronizations](docs/canonical/synchronizations/) and [Dependence](docs/canonical/dependence/).
4. Use [MUDAC Product-Family Scope](docs/canonical/dependence/product-family-scope.md) for PF-01.
5. Read [Phase 013 Mapping Authority Baseline](docs/canonical/experience/mapping-authority-baseline.md).
6. Read current accepted Experience owners relevant to the work, including [Accessibility, Responsive & Degraded-Operation Mapping](docs/canonical/experience/accessibility-resilience.md) and [Status, Feedback & Recovery Mapping](docs/canonical/experience/status-feedback-recovery.md).
7. Read the active [Phase 013](docs/013-concept-mapping-interaction-semantics-user-visible-representation/) record.
8. Treat older Experience adapters as historical evidence unless the Mapping Authority Baseline says otherwise.
9. Use current synchronization owners for composition; mapping does not replace composition.
10. Do not preload architecture/implementation except for explicit contamination/history analysis.

## Current methodology posture

```text
009: COMPLETE — PASS
010: COMPLETE — PASS
011: COMPLETE — PASS
012: COMPLETE — PASS
013: IN PROGRESS
013-A: COMPLETE — READY
013-B: COMPLETE — PASS
013-C: COMPLETE — PASS
013-D: COMPLETE — PASS
013-E: COMPLETE — PASS
013-F: COMPLETE — PASS
013-G: COMPLETE — PASS
013-H: COMPLETE — PASS
013-I: COMPLETE — PASS
013-J: COMPLETE — PASS
013-K: NEXT
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

## Composition and mapping authority

Preserve:

- Identity != Participation != Access;
- Panel membership != occurrence participation != Evaluation Obligation != Scorecard evidence;
- one Evaluation Obligation maps to at most one logical Scorecard;
- Scorecard Draft != authority;
- capture Actor != Judge semantic author / RepresentedAuthority;
- Judge amendment != source-faithful capture correction;
- supersession != invalidation != replacement != affectedness/staleness;
- historical obligation satisfaction != current evidence eligibility;
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
- paper fallback != second evaluation model;
- unknown authoritative result != confirmed success or confirmed failure;
- retry/recovery must reconcile current authority and converge rather than duplicate effects;
- stale local state cannot overwrite newer authority;
- status is multidimensional and subject-qualified, not one universal badge;
- working persistence feedback != semantic commitment;
- technical recovery privilege != broader Access, disclosure or domain authority.

Map the established action surface:

```text
D — direct application action
C — coordinated application action
P — composition-only participant
S — system-triggered conceptual reaction
X — intentionally unavailable generic application action
```

Do not expose `P` or `X` as generic user actions. Accessibility/recovery does not invent new authority actions or weaker substitutes for unavailable high-consequence actions.

## Explanation-order rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
```

Accessible/responsive/degraded presentation may change mechanics or information density but cannot waive semantic prerequisites or consequences.

## Historical Experience adapters

- `docs/canonical/experience/reconciliation-finalization.md` — historical only.
- `docs/canonical/experience/paper-export-publication.md` — historical only.

## Current next task

Proceed to:

> **013-K — Whole-Experience Explanation Order, Cross-Role/Profile Consistency & Mapping-Integrity Audit**
