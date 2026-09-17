# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md).
3. Read [Project Context & Purpose](docs/canonical/project/), [Concepts](docs/canonical/concepts/), [Synchronizations](docs/canonical/synchronizations/) and [Dependence](docs/canonical/dependence/).
4. Use [MUDAC Product-Family Scope](docs/canonical/dependence/product-family-scope.md) for PF-01.
5. Read [Phase 013 Mapping Authority Baseline](docs/canonical/experience/mapping-authority-baseline.md).
6. Read current accepted Experience owners relevant to the work. Through 013-H these include Context/Participation Modes, Judge Entry, Organizer Preparation, Judge Active Evaluation, Authority Lineage/Correction, Live Operations/Remaining Work, Reconciliation/Derived Outcome State, and [Award, Finalization & Outcome Officiality Mapping](docs/canonical/experience/outcome-officiality.md).
7. Read the active [Phase 013](docs/013-concept-mapping-interaction-semantics-user-visible-representation/) record.
8. Treat remaining older `docs/canonical/experience/` contracts as admitted/historical evidence unless explicitly accepted/reworked/superseded by Phase 013.
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
013-F: COMPLETE — PASS
013-G: COMPLETE — PASS
013-H: COMPLETE — PASS
013-I: NEXT
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

Coverage, Aggregate, Rank and Readiness remain derived mechanisms. Reconciliation and Live Operations remain work/process contexts rather than Concepts.

## Composition and mapping authority

Preserve:

- Identity != Participation != Access;
- role/capacity mode is representation, not authority;
- multi-capacity capabilities never union;
- Judge context carries Judge-safe disclosure posture;
- preparation/readiness is source-derived rather than workflow authority;
- Panel membership != Evaluation Occurrence participation != Evaluation Obligation != Scorecard evidence;
- occurrence completion != obligation satisfaction != Scorecard Finalization;
- one Evaluation Obligation maps to at most one logical Scorecard;
- Scorecard Draft != authority;
- exact bound Evaluation Basis != latest working Rubric;
- uncertain authoritative result != confirmed success;
- capture Actor != Judge semantic author / RepresentedAuthority;
- Judge amendment != source-faithful capture correction;
- supersession != invalidation != replacement != affectedness/staleness;
- historical Evaluation Obligation satisfaction != current evidence eligibility;
- terminal obligations never reopen;
- legitimate repeated responsibility uses a successor obligation + new logical Scorecard;
- Remaining Work is projected from current Outstanding obligations;
- ineligible evidence != reopened obligation != automatic successor responsibility;
- Reconciliation is source-directed work, not ticket/lifecycle authority;
- Coverage factual state != governed exception disposition;
- Aggregate existence != Coverage satisfaction or rank eligibility;
- Rank is derived and non-editable;
- Ranking Readiness and Finalization Readiness are derived/non-editable;
- calculated != ranking ready != recognized != Competition Finalized != official != public != delivered;
- Ranking Ready candidate != conferred Award;
- rank-derived Award selection != discretionary Award selection;
- later Rank/source change != automatic Award transfer;
- Finalization Readiness != Competition Finalized;
- ordinary closeout coordinates Competition.finalize + OutcomeDeclaration.declare;
- ordinary closeout success requires Competition Finalized + a current Outcome Declaration;
- Competition lifecycle ownership != Outcome Declaration content/currentness ownership;
- Outcome Declaration currentness = Current | Affected | Superseded;
- Affected != Superseded;
- corrected calculations do not become successor official authority automatically;
- an Affected declaration remains latest declared official authority until explicit successor confirmation;
- materially changed declared basis requires successor confirmation even if visible result is unchanged;
- successor Outcome Declaration does not re-finalize Competition;
- Outcome Declaration != Export != Publication != delivery;
- Organizer/support/technical privilege != Judge authorship, exception authority, Award authority, Finalization authority, or declaring authority.

Map the established action surface:

```text
D — direct application action
C — coordinated application action
P — composition-only participant
S — system-triggered conceptual reaction
X — intentionally unavailable generic application action
```

Do not expose `P` or `X` as generic user actions. Generic Versioning/Provenance administration, manual Coverage/Rank editing, generic reconciliation `resolve`, universal `override`, generic declaration editing and automatic Publication remain unavailable.

## Explanation-order rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
```

## Historical Experience adapter rules

- `docs/canonical/experience/reconciliation-finalization.md` is historical evidence only; all current semantics migrated to 013-G/H owners.
- `docs/canonical/experience/paper-export-publication.md` is historical/evidence only; remaining Export/Publication evidence awaits 013-I.

## Current next task

Proceed to:

> **013-I — Export, Publication, Audience Disclosure, External Recipient & Representation/Release Mapping**
