# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md).
3. Read [Project Context & Purpose](docs/canonical/project/), [Concepts](docs/canonical/concepts/), [Synchronizations](docs/canonical/synchronizations/) and [Dependence](docs/canonical/dependence/).
4. Use [MUDAC Product-Family Scope](docs/canonical/dependence/product-family-scope.md) for PF-01.
5. Read [Phase 013 Mapping Authority Baseline](docs/canonical/experience/mapping-authority-baseline.md).
6. Read current accepted Experience owners relevant to the work. Through 013-E these include [Context and Participation Modes](docs/canonical/experience/context-role-modes.md), [Judge Entry, Participation & Readiness Mapping](docs/canonical/experience/judge-onboarding.md), [Organizer Competition Preparation & Readiness Mapping](docs/canonical/experience/organizer-preparation.md), and [Judge Active Evaluation Mapping](docs/canonical/experience/judge-evaluation.md).
7. Read the active [Phase 013](docs/013-concept-mapping-interaction-semantics-user-visible-representation/) record.
8. Treat remaining older `docs/canonical/experience/` contracts as admitted evidence/candidates unless their assigned Phase-013 workstream has explicitly accepted/reworked/superseded them.
9. Use current synchronization owners for interaction/composition rules; mapping does not replace composition.
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
013-F: NEXT
architecture authority: SUSPENDED
implementation-planning authority: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

## Current Concept authority

The canonical catalog contains eighteen Concepts:

Competition, Division, Team, Panel, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Identity, Participation, Alias, Access, Versioning, Provenance, Outcome Declaration, Export, and Publication.

`Judging Encounter` and `Official Outcome Revision` remain deprecated historical adapters. Do not restore them because older UX material uses those terms.

Coverage, Aggregate, Rank and Readiness remain derived mechanisms. Reconciliation remains process/work context.

## Composition and mapping authority

Preserve:

- Identity != Participation != Access;
- one protected operation uses one explicit current Participation context;
- role/capacity mode is representation, not authority;
- one Identity with Judge and Organizer Participations never receives unioned capability;
- Judge context carries Judge-safe disclosure posture;
- preparation/readiness is source-derived rather than workflow authority;
- Panel membership != Evaluation Occurrence participation != Evaluation Obligation != Scorecard evidence;
- Prepared occurrence != begun occurrence != responsibility;
- occurrence completion != obligation satisfaction != Scorecard Finalization;
- Outstanding obligation + no Scorecard is legitimate Not Started work;
- one Evaluation Obligation maps to at most one logical Scorecard;
- Scorecard Draft != authority;
- Draft complete/valid != Finalized;
- exact bound Evaluation Basis != latest working Rubric;
- missing evaluation != zero;
- Judge Finalization requires explicit semantic intent;
- uncertain authoritative result != confirmed success;
- Organizer/support privilege != Judge authorship;
- Coverage/Aggregate/Rank != Award authority != Outcome Declaration;
- Competition Finalization != Outcome Declaration;
- calculated != recognized != official != public != delivered;
- source authority != Export != Publication != transport delivery.

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
```

## Current next task

Proceed to:

> **013-F — Authority Lineage, Paper Capture, Amendment, Correction & Historical-State Mapping**
