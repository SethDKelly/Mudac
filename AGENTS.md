# MUDAC Repository Agent Rules

This file is a bootstrap adapter. Current authority lives under [`docs/`](docs/), especially canonical conceptual/governance owners and the active methodology phase.

## Required start

1. Start at [`docs/index.md`](docs/index.md).
2. Read [`Design / Implementation Boundary`](docs/canonical/governance/design-implementation-boundary.md).
3. Read current [Project](docs/canonical/project/), [Concepts](docs/canonical/concepts/), [Synchronizations](docs/canonical/synchronizations/) and [Dependence](docs/canonical/dependence/).
4. Use [MUDAC Product-Family Scope](docs/canonical/dependence/product-family-scope.md) for PF-01.
5. Read [Phase 013 Mapping Authority Baseline](docs/canonical/experience/mapping-authority-baseline.md).
6. Read current accepted Experience owners relevant to the work, including [Outcome Officiality](docs/canonical/experience/outcome-officiality.md) and [External Representation, Disclosure & Release](docs/canonical/experience/external-representation-release.md).
7. Read the active [Phase 013](docs/013-concept-mapping-interaction-semantics-user-visible-representation/) record.
8. Treat older Experience adapters as historical/admitted evidence unless the Mapping Authority Baseline says otherwise.
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
013-J: NEXT
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
- Panel membership != Evaluation Occurrence participation != Evaluation Obligation != Scorecard evidence;
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
- Outcome Declaration Current/Affected/Superseded currentness remains explicit;
- source authority != Export representation != Publication release != delivery;
- actor Access != audience disclosure permission;
- Export generation != Publication;
- Export SourceBasis remains exact and historically stable;
- Export currency != Publication distribution state;
- corrected/new source that must be represented uses a new Export;
- successor Outcome Declaration != successor Export != successor Publication;
- withdrawal/supersession never erases historical release or external copies;
- possession of URL/QR/file/printout != current release authority or Access;
- Publication Published != transport/delivery/viewing success;
- Organizer/support/technical privilege != Judge, exception, declaring, disclosure or publishing authority.

Map the established action surface:

```text
D — direct application action
C — coordinated application action
P — composition-only participant
S — system-triggered conceptual reaction
X — intentionally unavailable generic application action
```

Do not expose `P` or `X` as generic user actions. Automatic declaration→publication, correction→auto-withdraw/regenerate/republish, generic Versioning/Provenance administration, manual Coverage/Rank editing and universal override remain unavailable.

## Explanation-order rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
```

## Historical Experience adapters

- `docs/canonical/experience/reconciliation-finalization.md` — historical only; current semantics migrated in 013-G/H.
- `docs/canonical/experience/paper-export-publication.md` — historical only; current semantics migrated in 013-F/I.

## Current next task

Proceed to:

> **013-J — Accessibility, Degraded Operation, Status/Feedback, Recovery & Semantic-Parity Mapping**
