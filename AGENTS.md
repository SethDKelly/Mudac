# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md).
3. Read current [Project](docs/canonical/project/), [Concepts](docs/canonical/concepts/), [Synchronizations](docs/canonical/synchronizations/) and [Dependence](docs/canonical/dependence/).
4. Use [MUDAC Product-Family Scope](docs/canonical/dependence/product-family-scope.md) for PF-01.
5. Read the final [Phase 013 Mapping Authority Baseline](docs/canonical/experience/mapping-authority-baseline.md) and relevant Experience owners.
6. For current methodology work, read [Phase 014 — Familiarity, Reuse & Genericity](docs/014-familiarity-reuse-genericity/) and the active Phase-014 record.
7. Treat older Experience adapters and deprecated Concepts as historical evidence only.
8. Use current synchronization/dependence owners for composition/scope; Phase 014 does not supersede them.
9. Load external/domain familiar precedents only as comparison evidence and test semantic fit explicitly.
10. Do not preload architecture/implementation except for explicit contamination/history analysis.

## Current methodology posture

```text
009: COMPLETE — PASS
010: COMPLETE — PASS
011: COMPLETE — PASS
012: COMPLETE — PASS
013: COMPLETE — PASS
014: IN PROGRESS
014-A: COMPLETE — READY
014-B: NEXT
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
- historical obligation satisfaction != current evidence eligibility;
- Event Completed != universal hidden Access revocation;
- Remaining Work = current Outstanding-obligation projection;
- Coverage factual state != exception disposition;
- Rank is derived/non-editable;
- calculated != recognized != Competition Finalized != official != public != delivered;
- Outcome Declaration != Export != Publication != delivery;
- Export currency != Publication distribution state;
- accessible/responsive/degraded/paper paths preserve the same domain semantics;
- result unknown != confirmed success or confirmed failure;
- stale local state cannot overwrite newer authority.

Map the established action surface:

```text
D — direct application action
C — coordinated application action
P — composition-only participant
S — system-triggered conceptual reaction
X — intentionally unavailable generic application action
```

Do not expose `P` or `X` as generic user actions.

## Phase-014 familiarity / reuse discipline

Phase 014 asks whether prior conceptual understanding would transfer correctly.

```text
familiarity != implementation mimicry
reuse != Concept merging by resemblance
genericity != abstraction for abstraction's sake
common vocabulary != lost authority boundary
profile reuse != capability union
```

For a proposed familiar precedent, compare materially relevant:

- purpose and operational principle;
- state, actions and queries;
- lifecycle/finality/reversibility;
- authority/authorship/delegation;
- history/correction semantics;
- scope/parameters;
- synchronization/dependence consequences;
- mapped/disclosure expectations.

Popularity, framework similarity, UI shape or database resemblance is not sufficient evidence.

If a familiarity/generalization finding exposes an actual purpose/boundary defect, composition defect, scope defect or mapping defect, route it to the natural Phase-010/011/012/013 owner instead of silently rewriting semantics in Phase 014.

## Explanation-order rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
explanation order != mandatory screen order
```

## Historical Experience adapters

- `docs/canonical/experience/reconciliation-finalization.md` — historical only.
- `docs/canonical/experience/paper-export-publication.md` — historical only.

## Current next task

Proceed to:

> **014-B — Familiarity Evidence Baseline, Precedent Taxonomy & Comparison Register**
