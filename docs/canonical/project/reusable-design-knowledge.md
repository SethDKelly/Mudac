---
type: Project Knowledge Registry
title: Reusable Concept Knowledge & Design Patterns
description: "Registry of MUDAC concept-knowledge candidates and reusable cross-cutting design patterns identified by Phase 014, linking to natural canonical owners while avoiding duplicate concept specifications or premature universal catalog claims."
status: stable
tags: [project, reuse, concept-knowledge, design-patterns, catalog-candidates, phase-014]
sources:
  - resource: ../../014-familiarity-reuse-genericity/014-H-retained-novelty-reusable-concept-knowledge-catalog-candidate-audit.md
  - resource: ../../014-familiarity-reuse-genericity/014-G-broader-genericity-parameterization-duplication-specialization-pressure-audit.md
  - resource: ../concepts/
  - resource: domain-vocabulary-expectation-transfer.md
---

# Purpose

Preserve reusable design knowledge discovered while designing MUDAC without creating a second source of Concept truth.

This registry records:

- which current MUDAC Concepts are plausible reusable concept-knowledge candidates;
- whether their likely reuse is broad or domain-family scoped;
- which transferable lessons and reuse constraints matter;
- which cross-cutting lessons are patterns rather than Concepts;
- what evidence would be needed before promoting a candidate into a shared/external concept catalog.

Natural Concept owners remain authoritative for current MUDAC semantics.

```text
canonical Concept owner
  = current MUDAC semantic truth

this registry
  = reusable-knowledge candidate index / cross-context lesson

shared external catalog
  = NOT established here
```

# Candidate classes

## CK-1 — Broad reusable Concept-knowledge candidate

The Concept purpose/behavior plausibly recurs across multiple application domains and carries non-trivial reusable design lessons.

## CK-2 — Domain-family reusable Concept-knowledge candidate

The Concept is plausibly reusable within a recognizable domain family, but broad universalization would weaken purpose clarity.

## PK — Reusable design-pattern knowledge

The lesson recurs across multiple Concepts but has no independent user-facing purpose and therefore is **not** a MUDAC Concept.

# CK-1 registry

| Concept | Natural owner | Transferable lesson | Principal reuse constraint |
| --- | --- | --- | --- |
| Identity | [Identity](../concepts/identity.md) | stable human attribution across scoped episodes | human continuity != Participation != Access; not generic machine principal identity |
| Participation | [Participation](../concepts/participation.md) | scoped, time-bounded involvement in a Capacity | do not reduce to static Role/membership or stored permission |
| Alias | [Alias](../concepts/alias.md) | scoped alternate/resolvable identity for controlled disclosure/bias reduction | alias != underlying identity replacement or cosmetic nickname only |
| Access | [Access](../concepts/access.md) | contextual capability/disclosure decision | permission does not transfer semantic authorship or ownership |
| Versioning | [Versioning](../concepts/versioning.md) | immutable committed snapshots, explicit currentness/successor/invalidation | no implied branch/merge/reset/revert or silent predecessor revival |
| Provenance | [Provenance](../concepts/provenance.md) | origin, transformation and authority explanation | Actor != represented authority != source; provenance does not create authority |
| Outcome Declaration | [Outcome Declaration](../concepts/outcome-declaration.md) | explicit official declaration over an exact basis | calculated/recognized/finalized != official; Affected remains latest declared authority until successor |
| Export | [Export](../concepts/export.md) | exact-source representation with independent current-use currency | file/download generation alone is insufficient; source authority != representation |
| Publication | [Publication](../concepts/publication.md) | deliberate release of an exact representation to audience/channel | published != public != delivered; withdrawal cannot erase external possession |

# CK-2 registry

| Concept | Natural owner | Transferable lesson | Principal reuse constraint |
| --- | --- | --- | --- |
| Competition | [Competition](../concepts/competition.md) | governed bounded competitive occurrence/lifecycle | do not flatten into generic Event when competitive closeout semantics matter |
| Division | [Division](../concepts/division.md) | scoped comparison-cohort definition and correctable assignment | cohort purpose != arbitrary group membership |
| Team | [Team](../concepts/team.md) | scoped competing group acting as one unit | not a universal Group/Entity abstraction; PF-01 binds it to student teams |
| Panel | [Panel](../concepts/panel.md) | reusable intended evaluator grouping distinct from actual event participation | membership != occurrence participation != responsibility != evidence |
| Evaluation Occurrence | [Evaluation Occurrence](../concepts/evaluation-occurrence.md) | historical truth about one bounded evaluation event/context/participants | occurrence completion != responsibility satisfaction |
| Evaluation Obligation | [Evaluation Obligation](../concepts/evaluation-obligation.md) | one historical responsibility to produce qualifying evidence | terminal satisfaction is not a reopenable task; new work uses successor responsibility |
| Rubric | [Rubric](../concepts/rubric.md) | evaluation instrument defines response meaning/validity | rubric != generic form/template/schema |
| Scorecard | [Scorecard](../concepts/scorecard.md) | one evaluator judgment under exact context/basis with Draft→authority→successor semantics | Scorecard != Aggregate/Rank/submission record; one logical judgment preserves weight |
| Award | [Award](../concepts/award.md) | explicit recognition under declared selection semantics | candidate/selection basis != conferral authority; basis change does not silently move recognition |

# Retained novelty worth preserving

## Evaluation Occurrence / Evaluation Obligation separation

```text
what happened
  != who owed work
```

This separation prevents event completion from falsely satisfying individual responsibility and preserves terminal obligation history independently from later evidence eligibility.

## Historical satisfaction / current eligibility separation

```text
historically satisfied responsibility
  != currently eligible evidence
```

Current unusability must not rewrite a legitimately satisfied historical duty.

## Outcome Declaration `Affected`

```text
Affected
  = latest explicitly declared official authority
    known to require correction/review
  != silently superseded
```

This makes officiality correction explicit rather than treating recalculation as declaration.

## Derivation / recognition / officiality

```text
Aggregate / Rank
  != Award
  != Outcome Declaration
```

Calculated state, recognized achievement and official declaration remain independently owned.

## Representation / release / delivery

```text
source authority
  != Export representation
  != Publication release
  != delivery / possession
```

This preserves disclosure, correction and historical-release truth.

# PK registry

## PK-01 — Scoped opaque-reference parameterization

A Concept may accept abstract peer identity/reference values without importing peer internals or becoming intrinsically dependent on those peer Concepts.

```text
association != semantic dependence
```

## PK-02 — Exact-basis binding

Consequential authority should retain the exact basis it relied on where later source changes must be explainable.

MUDAC examples include EvaluationBasis, OutcomeBasis and Export SourceBasis.

## PK-03 — Explicit successor without silent historical rewrite

Preserve predecessor truth and establish successor authority through the owning Concept rather than mutating authoritative history in place.

Do not infer one universal successor lifecycle; owner-specific semantics remain authoritative.

## PK-04 — Actor / represented authority / source separation

Keep separate:

```text
Actor
RepresentedAuthority / semantic author
Source
```

This supports assisted entry, paper transcription, imports, delegated operations and correction without accidental authorship transfer.

## PK-05 — Historical accomplishment versus current eligibility

Something may have been legitimately completed/satisfied in the past while no longer being currently usable after later correction/invalidation.

Represent both truths rather than rewriting the historical one.

## PK-06 — Derivation → recognition → declaration

Separate calculated/derived state, explicit recognition and official declaration when those steps have different authorities or correction consequences.

## PK-07 — Source → representation → release → delivery

Separate source authority, generated representation/currentness, deliberate release and external delivery/possession.

## PK-08 — Context capability without authorship transfer

Permission or assistance to perform an operation does not by itself change who is the semantic author or which Concept owns the decision.

# Non-candidates / rejected pseudo-catalog concepts

The following are intentionally **not** reusable MUDAC Concept candidates merely because common structure exists:

```text
Group
Scoped Relationship
Task / Work Item
Evaluation Record
Historical / Correctable Record
Result
universal Representation / Artifact owner
universal Status / Workflow / Revision
```

Their apparent commonality is structural or implementation-shaped; they do not possess one stable independent user purpose across the current Concepts.

# Promotion rule for a future shared catalog

A candidate should not be promoted from this registry into a shared/Base catalog based solely on MUDAC quality or abstractness.

Seek additional evidence such as:

1. an independently designed second application exhibiting substantially the same purpose/behavior;
2. a strong external conceptual precedent with compatible lifecycle/authority/history;
3. explicit counterexamples showing when reuse would fail;
4. stable generic parameters that preserve purpose rather than merely fields;
5. enough cross-context evidence to separate intrinsic semantics from MUDAC composition bindings.

Until then, candidate status remains informative rather than universal authority.

# Implementation boundary

This registry makes **no** decision about reusable code, schemas, frameworks, services, tables, libraries, workflow engines, authorization infrastructure, versioning infrastructure, report generation or publishing infrastructure.

```text
conceptual reuse != code reuse
pattern reuse != architecture mandate
shared parameter != base class
```

Any future implementation reuse must preserve the successfully closed Concept distinctions.

# Related authority

- current concept specifications → [Concepts](../concepts/)
- familiar-language rules → [MUDAC Domain Vocabulary & Expectation-Transfer Rules](domain-vocabulary-expectation-transfer.md)
- Phase-014 rationale → [014-H](../../014-familiarity-reuse-genericity/014-H-retained-novelty-reusable-concept-knowledge-catalog-candidate-audit.md)
