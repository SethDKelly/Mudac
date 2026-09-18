---
type: Phase Design Record
title: 014-G — Broader Genericity, Parameterization, Duplication & Specialization-Pressure Audit
description: "Tests the mature MUDAC concept system for safe broader parameterization, incidental product-specificity, duplicated semantic shapes and tempting super-concepts after familiarity/terminology closure, adopting only generalization that preserves independent purpose, authority, lifecycle, history and explanation."
status: stable
tags: [phase-014, jackson, genericity, parameterization, duplication, specialization, abstraction]
sources:
  - resource: 014-A-familiarity-reuse-genericity-scope-criteria-evidence-subphase-planning.md
  - resource: 014-C-competition-competitor-grouping-identity-participation-alias-access-familiarity-reuse-audit.md
  - resource: 014-D-evaluation-occurrence-obligation-rubric-scorecard-familiarity-reuse-audit.md
  - resource: 014-E-versioning-provenance-award-outcome-declaration-export-publication-familiarity-reuse-audit.md
  - resource: 014-F-cross-catalog-false-familiarity-terminology-expectation-transfer-audit.md
  - resource: ../010-project-purpose-candidate-specification-modularity/010-G-completeness-independence-genericity-for-boundary-audit.md
  - resource: ../canonical/concepts/
  - resource: ../canonical/project/domain-vocabulary-expectation-transfer.md
---

# Purpose

Perform the broader Phase-014 genericity audit after familiarity and terminology are known.

010-G already generalized peer references where needed for **Concept independence**. 014-G asks the broader reuse question:

> Can a sound current Concept remove incidental MUDAC-specificity or expose a more reusable parameter boundary **without weakening its independent user purpose or merging it with another Concept merely because their state shapes resemble one another?**

The audit also tests duplicate-looking concepts and candidate super-concepts before reusable-knowledge/catalog work begins in 014-H.

# Decision

**COMPLETE — PASS. Proceed to 014-H.**

```text
014-A start gate                                   COMPLETE — READY
014-B evidence / precedent baseline                COMPLETE — PASS
014-C Family-1 familiarity/reuse audit             COMPLETE — PASS
014-D Family-2 familiarity/reuse audit             COMPLETE — PASS
014-E Family-3 familiarity/reuse audit             COMPLETE — PASS
014-F cross-catalog terminology audit              COMPLETE — PASS
014-G broader genericity / duplication audit       COMPLETE — PASS
Concept merge / split / replacement                NONE
new super-Concept                                  NONE
adopted broader genericity refinement              TEAM: remove intrinsic student-specificity
new dependence edge / PF-01 change                 NONE
Phase-010 formal reopen                            NO
Phase-011 synchronization reopen                   NO
Phase-012 dependence/PF-01 reopen                  NO
Phase-013 mapping reopen                           NO
architecture / implementation influence            PROHIBITED
NEXT                                                014-H
```

# 1. Governing genericity rule

MUDAC adopts:

> **Generic at the boundary; specific in purpose.**

A Concept may accept abstract `Scope`, `Member`, `Subject`, `Evaluator`, `Basis`, `SourceBasis`, `Representation`, `Audience`, `Authority`, or other supplied semantic values without becoming a generic container for every Concept that uses similar values.

```text
shared parameter != shared purpose
shared fields != shared lifecycle
shared successor/history shape != shared authority
shared implementation possibility != Concept identity
```

Broader genericity is accepted only when it removes incidental specialization while preserving:

- the same independent purpose;
- the same operational principle;
- materially the same state/actions;
- the same authority/authorship semantics;
- the same history/correction promises;
- the same composition/dependence meaning;
- a clear user mental model.

# 2. Relationship to 010-G

010-G established the boundary-generic forms needed for independence, including:

```text
Division<Scope, Member>
Panel<Scope, Member, CapacityLabel>
Participation<Participant, Scope, Capacity>
EvaluationOccurrence<Subject, Evaluator, PresentedContext, BasisRef>
EvaluationObligation<Evaluator, Subject, Basis, Scope, OccurrenceRef, EvidenceRef>
Scorecard<Evaluator, Subject, OccurrenceContext, EvaluationBasis>
Alias<Subject, Scope, AliasValue>
Access<Principal, Capability, Resource, ContextFacts, Rule>
Versioning<Subject, Snapshot>
Provenance<Subject, StateRef, Actor, RepresentedAuthority, Scope, Source>
Award<Scope, Recipient, SelectionBasis>
OutcomeDeclaration<Scope, OutcomeBasis, DeclaringAuthority>
Export<SourceBasis, RepresentationProfile, AudienceProfile>
Publication<Representation, Audience, Channel, PublishingAuthority>
```

014-G confirms that this parameterization is generally sufficient. The mature design does not require another abstraction layer above these Concepts merely to reduce repeated parameter names.

# 3. Adopted broader-genericity refinement — Team

## Finding

Current Team purpose was expressed as the administrative representation of a **student group** participating as one competing unit.

`student` is true for current MUDAC product scope, but it is not required for Team's intrinsic purpose, lifecycle or behavior.

The reusable Concept is more accurately:

```text
Team<Scope>
  = stable scoped administrative representation
    of one competing group acting as a single unit
```

MUDAC then binds that generic competing group to a student team in PF-01.

## Decision

Adopt a narrow canonical refinement to Team:

- remove `student` from intrinsic description/purpose/operational-principle wording;
- retain `Team` and competing-group semantics;
- retain MUDAC composition/product context that current competitors are student teams;
- do not broaden Team into arbitrary individual competitors or a universal Group Concept.

This is a Phase-014 safe genericity refinement, not a purpose/boundary correction requiring Phase-010 reopen.

# 4. Whole-catalog genericity dispositions

| Concept | Current broader-genericity disposition | Rationale |
| --- | --- | --- |
| Competition | **retain purpose specificity** | a governed competition occurrence is the product's scope/lifecycle concept; generic `Event` loses competitive lifecycle meaning |
| Division | **already sufficiently parameterized** | `Scope + Member` is reusable; cohort/comparison purpose distinguishes it from Panel/Group |
| Team | **adopt narrow broader genericity** | remove incidental `student` specialization; retain competing-group purpose |
| Panel | **already sufficiently parameterized** | `Scope + Member + CapacityLabel`; evaluator-grouping purpose remains domain-significant |
| Identity | **retain human specificity** | continuity of the human actor is deliberate; generic `Principal/Subject` would blur Identity with Access/technical identity |
| Participation | **already sufficiently parameterized** | `Participant + Scope + Capacity`; do not reduce to generic Relationship/Membership |
| Alias | **already sufficiently parameterized** | `Subject + Scope + AliasValue`; alternate-identity/bias-control purpose is independent |
| Access | **already broadly parameterized** | contextual decision contract is already cross-domain; do not merge with Participation or technical authorization infrastructure |
| Evaluation Occurrence | **already sufficiently parameterized** | supplied subject/evaluator/context/basis; evaluation-event truth distinguishes it from generic Session/Occurrence |
| Evaluation Obligation | **already sufficiently parameterized** | supplied evaluator/subject/basis/scope; responsibility history distinguishes it from Task/Assignment |
| Rubric | **retain evaluation-instrument specificity** | generic Schema/Template would lose judgment-interpretation purpose |
| Scorecard | **already sufficiently parameterized** | evaluator/subject/context/basis are abstract; independent judgment purpose distinguishes it from Form/Submission/Record |
| Versioning | **already broadly generic** | one of the strongest reusable Concepts; no broader lifecycle should absorb owner-specific histories |
| Provenance | **already broadly generic** | actor/represented-authority/source explanation is already parameterized |
| Award | **already sufficiently parameterized** | `Scope + Recipient + SelectionBasis`; recognition purpose remains essential |
| Outcome Declaration | **already sufficiently parameterized** | `Scope + OutcomeBasis + DeclaringAuthority`; official declaration semantics must remain distinct from Versioning/Result |
| Export | **already broadly parameterized** | exact SourceBasis + representation/audience profile; representation purpose must remain distinct from source and release |
| Publication | **already broadly parameterized** | exact Representation + Audience/Channel/PublishingAuthority; release purpose remains distinct from Export/delivery |

# 5. Candidate super-concept audit

## `Group` over Team / Division / Panel

Rejected.

All three involve collections/groupings but answer different questions:

```text
Team     → who competes as one administrative unit
Division → which competitors belong to the same comparison cohort
Panel    → which evaluators are intended to operate together
```

A universal Group Concept would move domain-significant membership meaning into configuration and make authority/history harder to explain.

**Disposition:** shared collection mechanics may be implementation-reusable later; no shared application Concept.

## `Scoped Relationship` over Participation / Division assignment / Panel membership / Alias

Rejected.

The common shape `subject + scope + relationship/history` is structural only.

- Participation owns capacity involvement/lifecycle;
- Division owns competitive cohort assignment;
- Panel owns reusable evaluator grouping;
- Alias owns alternate identity within scope.

Their actions, correction semantics and user purposes differ.

**Disposition:** reusable modeling pattern candidate for 014-H, not a Concept.

## `Occurrence` over Competition / Evaluation Occurrence

Rejected.

Both preserve bounded happenings, but:

- Competition owns the overall competition lifecycle/context;
- Evaluation Occurrence preserves one bounded evaluation event and actual participants/context/basis.

A generic Occurrence super-concept would not have one singular application purpose and would create confusing inherited lifecycle expectations.

## `Work Item` / `Task` over Participation / Evaluation Obligation / Remaining Work

Rejected.

```text
Participation       = scoped capacity involvement
Evaluation Obligation = historical responsibility
Remaining Work      = derived projection over Outstanding obligations
```

The task abstraction would incorrectly introduce writable queue semantics and reopenable completion.

## `Evaluation Record` over Rubric / Scorecard / Aggregate / Rank

Rejected.

These own instrument semantics, individual judgment, numerical derivation, and ordering respectively. Similar evaluation vocabulary does not establish one purpose.

## `Historical / Versioned / Correctable Record`

Rejected as an application Concept.

Versioning already owns generic committed-snapshot lineage where that exact purpose applies. Other owners intentionally have different temporal promises:

```text
Scorecard amendment/correction
Award conferral/revocation/correction
Outcome Declaration Current/Affected/Superseded
Export Current/Affected/Stale/Superseded/Retired
Publication Published/Withdrawn/Superseded
```

Forcing them through one generic history lifecycle would erase owner-specific meanings.

## `Result` over Aggregate / Rank / Award / Outcome Declaration

Rejected.

```text
Aggregate           = calculated numerical derivation
Rank                = calculated ordering
Award               = recognized achievement
Outcome Declaration = explicit official authority
```

The distinction is fundamental to MUDAC's authority model.

## `Representation / Artifact` over Export / Publication

Rejected as a merger.

Export can already bind an abstract SourceBasis/representation contract. Publication binds an exact abstract Representation. Their interface is deliberately generic enough without merging representation creation/currentness and release authority.

# 6. Duplication versus reusable design pattern

014-G distinguishes **semantic duplication** from **repeated good design structure**.

Repeated structures worth preserving as patterns include:

### Scoped identity/reference

Many Concepts use an abstract Scope and opaque peer identities. This prevents false dependence without creating a `ScopedThing` Concept.

### Exact-basis binding

Evaluation Basis, OutcomeBasis and Export SourceBasis all demonstrate a reusable principle:

> consequential authority should identify the exact basis it relied on when later source change must be explainable.

The bases themselves have different owners and are not interchangeable.

### Explicit successor without historical rewrite

Several Concepts preserve predecessor/current/successor history. The reusable lesson is to avoid silent rewrite; the lifecycle vocabulary remains owner-specific.

### Actor versus represented authority versus source

Provenance's separation is broadly reusable and supports assisted/paper/correction scenarios without transferring authorship.

### Derive → recognize → declare → represent → release

MUDAC's outcome chain preserves independent purposes rather than one overloaded Result lifecycle.

These are **candidate reusable knowledge** for 014-H, not additional application Concepts.

# 7. Specialization-pressure audit

## Human Identity

Do not generalize Identity into arbitrary machine/service Principal identity merely because Access accepts an abstract Principal.

MUDAC Identity exists to maintain continuity of human Judges/Organizers. Technical/service identity belongs downstream unless a future product need establishes an independent human/product purpose.

## Panel

Do not generalize Panel into arbitrary group membership. Evaluator grouping, composition intent, historical membership and the non-equivalence with actual occurrence participation give Panel its useful specificity.

## Rubric

Do not generalize Rubric into Template/Form/Schema. Its purpose is to define valid judgment response semantics and interpretation.

## Scorecard

Do not generalize Scorecard into generic Record/Submission. The independent-evaluator judgment, fixed structural identity, Draft/Finalization and amendment semantics are material.

## Award

Do not generalize Award into arbitrary Outcome/Decision. Recognition is its singular purpose.

## Outcome Declaration

Do not generalize Outcome Declaration into generic Versioned Result. Explicit declaration and its Affected/latest-declared-authority semantics are distinct.

# 8. Genericity and implementation boundary

Nothing in this audit authorizes:

- a generic entity framework;
- inheritance/shared-base classes;
- generic database tables;
- a workflow engine;
- a universal status machine;
- a generic correction service;
- one common versioning implementation for every historical owner;
- schema/interface unification based solely on shared parameter names.

Future engineering may reuse implementation where appropriate, but implementation reuse must conform to the Concept distinctions rather than define them.

# 9. Reopen / propagation result

014-G finds no need to reopen Phases 010–013.

The one adopted current refinement is local and semantics-preserving:

```text
Team intrinsic semantics:
student competing group
  → competing group

PF-01 product binding:
competing group
  → student team
```

Required propagation:

- update canonical `Team` owner;
- update relevant Concept/Phase-014 index wording where the intrinsic description is repeated;
- preserve MUDAC project-purpose statements that correctly describe the actual student competition product.

No synchronization, dependence, PF-01 or Experience behavior changes.

# 10. Risk disposition

014-G materially addresses:

- **FRG-R05 — Over-generalization:** rejected super-concepts without singular purpose;
- **FRG-R06 — Similarity merge:** shared state/history/parameters do not justify merges;
- **FRG-R07 — Under-generalization:** removed incidental student-specificity from Team intrinsic semantics;
- **FRG-R08 — Catalog duplication:** reusable patterns are deferred to 014-H rather than creating parallel Concepts;
- **FRG-R12 — Profile conflation:** parameterization never unions capacity/disclosure;
- **FRG-R14 — Taxonomy for taxonomy's sake:** no speculative universal hierarchy adopted.

No known contradiction is deferred to Phase 015.

# 11. Carry-forward to 014-H

014-H should distinguish **reusable Concept candidates** from **reusable design-pattern knowledge**.

Strong reusable Concept-knowledge candidates include at least:

```text
Access
Versioning
Provenance
Alias
Participation
Export
Publication
Outcome Declaration
```

Potential reusable pattern candidates include:

```text
scoped opaque-reference parameterization
exact-basis binding
explicit successor without silent historical rewrite
actor vs represented authority vs source
historical satisfaction vs current eligibility
source authority → representation → release separation
derivation → recognition → official declaration separation
```

014-H must decide what deserves durable reusable-knowledge treatment without creating a second MUDAC canonical catalog.

# Exit

**014-G COMPLETE — PASS. Proceed to 014-H — Retained Novelty, Reusable Concept-Knowledge & Catalog-Candidate Audit.**
