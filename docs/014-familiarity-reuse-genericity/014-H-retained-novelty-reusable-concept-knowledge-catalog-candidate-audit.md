---
type: Phase Design Record
title: 014-H — Retained Novelty, Reusable Concept-Knowledge & Catalog-Candidate Audit
description: "Audits the mature MUDAC concept system for justified retained novelty, reusable concept knowledge, reusable cross-cutting design patterns, and responsible catalog candidacy without creating a second canonical concept specification or universal taxonomy."
status: stable
tags: [phase-014, jackson, novelty, reuse, concept-knowledge, catalog-candidate, design-pattern]
sources:
  - resource: 014-A-familiarity-reuse-genericity-scope-criteria-evidence-subphase-planning.md
  - resource: 014-B-familiarity-evidence-baseline-precedent-taxonomy-comparison-register.md
  - resource: 014-C-competition-competitor-grouping-identity-participation-alias-access-familiarity-reuse-audit.md
  - resource: 014-D-evaluation-occurrence-obligation-rubric-scorecard-familiarity-reuse-audit.md
  - resource: 014-E-versioning-provenance-award-outcome-declaration-export-publication-familiarity-reuse-audit.md
  - resource: 014-F-cross-catalog-false-familiarity-terminology-expectation-transfer-audit.md
  - resource: 014-G-broader-genericity-parameterization-duplication-specialization-pressure-audit.md
  - resource: ../canonical/concepts/
  - resource: ../canonical/project/domain-vocabulary-expectation-transfer.md
  - resource: ../canonical/project/reusable-design-knowledge.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/008/phase-definition.md
---

# Purpose

Complete the Phase-014 design-knowledge audit after familiarity, terminology and broader genericity are settled.

014-H asks:

1. Which current Concepts contain reusable behavioral design knowledge beyond MUDAC?
2. Which recurring lessons are better preserved as cross-cutting design patterns rather than Concepts?
3. Which distinctions remain intentionally novel or unusually strict because familiar alternatives import the wrong authority, lifecycle or history model?
4. Which subjects are responsible **catalog candidates**, and under what constraints?
5. What should remain local to MUDAC rather than being generalized merely because it is well designed?

This phase does **not** create a universal concept catalog and does not duplicate current Concept specifications.

# Decision

**COMPLETE — PASS. Proceed to 014-I.**

```text
014-A start gate                                   COMPLETE — READY
014-B evidence / precedent baseline                COMPLETE — PASS
014-C Family-1 familiarity/reuse audit             COMPLETE — PASS
014-D Family-2 familiarity/reuse audit             COMPLETE — PASS
014-E Family-3 familiarity/reuse audit             COMPLETE — PASS
014-F cross-catalog terminology audit              COMPLETE — PASS
014-G broader genericity / duplication audit       COMPLETE — PASS
014-H novelty / reusable-knowledge audit           COMPLETE — PASS
Concept rename / merge / replacement               NONE
new Concept                                        NONE
new super-Concept                                  NONE
new reusable-knowledge registry                    YES
external/universal catalog publication             NO
Phase-010 Concept-boundary reopen                  NO
Phase-011 synchronization reopen                   NO
Phase-012 dependence/PF-01 reopen                  NO
Phase-013 mapping reopen                           NO
architecture / implementation influence            PROHIBITED
NEXT                                                014-I
```

# 1. Governing reuse rule

MUDAC adopts:

> **Reuse the behavioral idea and accumulated design knowledge, not merely the noun, data shape, workflow, or implementation mechanism.**

Catalog candidacy therefore requires more than abstract parameterization.

A reusable concept-knowledge candidate should have:

- a stable singular purpose that plausibly recurs outside MUDAC;
- a transferable operational principle;
- abstract state/actions/invariants that remain meaningful outside PF-01;
- clear generic parameters or intentionally retained domain scope;
- useful false-familiarity / misuse lessons;
- meaningful authority, history, correction or mapping constraints worth carrying forward;
- no dependence on MUDAC-specific implementation or UI structure.

```text
catalog candidate != universal concept
catalog candidate != implementation module
catalog candidate != duplicate canonical specification
pattern candidate != new MUDAC Concept
```

# 2. Candidate classes

014-H uses three knowledge dispositions.

## CK-1 — Broad reusable Concept-knowledge candidate

The Concept's purpose and behavior plausibly recur across multiple application domains and its current specification contains meaningful reusable design lessons.

## CK-2 — Domain-family reusable Concept-knowledge candidate

The Concept is reusable within a recognizable application/domain family such as competitions, evaluation, review, governance or recognition, but broad universalization would erase useful purpose specificity.

## PK — Reusable design-pattern knowledge

The lesson recurs across multiple Concepts but does not have one independent user-facing purpose. It should be preserved as a pattern/caution rather than promoted to a Concept.

A fourth implicit disposition is **local current Concept only**: a sound MUDAC Concept may remain current without any catalog claim.

# 3. Broad reusable Concept-knowledge candidates — CK-1

## Identity

**Candidate:** CK-1.

Reusable lesson:

```text
human continuity
  != scoped participation
  != current access
```

The useful knowledge is not generic authentication. It is preserving stable human attribution across episodes while requiring new scoped involvement and current authorization.

Constraint: retain human-identity purpose; do not generalize into arbitrary technical principal identity merely to share infrastructure.

## Participation

**Candidate:** CK-1.

Reusable form:

```text
Participation<Participant, Scope, Capacity>
```

Transferable lesson: scoped, time-bounded capacity involvement is distinct from identity continuity and permission. Historical Participation remains attributable after current capability ends.

Constraint: do not reduce to a static `Role` or generic membership row.

## Alias

**Candidate:** CK-1.

Reusable form:

```text
Alias<Subject, Scope, AliasValue>
```

Transferable lesson: alternate identity may be scoped, resolvable and authority-neutral, supporting bias control or controlled disclosure without replacing the underlying subject.

Constraint: nickname/display-name expectations are insufficient when resolution/disclosure boundaries matter.

## Access

**Candidate:** CK-1 — strong.

Reusable form:

```text
Access<Principal, Capability, Resource, ContextFacts, Rule>
```

Transferable lesson: authorization/disclosure is contextual and does not confer semantic authorship or ownership of the protected action.

Constraint: do not collapse into role membership, stored permission state, navigation visibility or technical possession.

## Versioning

**Candidate:** CK-1 — strong.

Reusable form:

```text
Versioning<Subject, Snapshot>
```

Transferable lesson: retain immutable committed snapshots, explicit successor/currentness and invalidation while avoiding silent predecessor revival.

Constraint: source-control operations such as branch/merge/reset/revert are not implied.

## Provenance

**Candidate:** CK-1 — strong.

Reusable form:

```text
Provenance<Subject, StateRef, Actor, RepresentedAuthority, Scope, Source>
```

Transferable lesson: distinguish the actor performing an operation from represented/semantic authority and from the source used to establish state.

This is especially reusable for assisted entry, import, transcription, delegated operation and correction without authorship transfer.

## Outcome Declaration

**Candidate:** CK-1 with strong authority constraints.

Reusable form:

```text
OutcomeDeclaration<Scope, OutcomeBasis, DeclaringAuthority>
```

Transferable lesson: officiality may require an explicit immutable declaration over an exact basis, distinct from calculation, recognition, lifecycle closeout, representation and publication.

Particularly reusable novelty:

```text
Affected
  = latest explicitly declared authority
    known to require correction/review
  != silently superseded
```

Constraint: do not reduce to a Versioned Result merely because predecessor/successor history exists.

## Export

**Candidate:** CK-1 with representation-currentness constraints.

Reusable form:

```text
Export<SourceBasis, RepresentationProfile, AudienceProfile>
```

Transferable lesson: an external representation can remain historically faithful to an exact source basis while separately having current-use currency such as Current/Affected/Stale/Superseded/Retired.

Constraint: file generation/download alone is not this Concept.

## Publication

**Candidate:** CK-1 with release-authority constraints.

Reusable form:

```text
Publication<Representation, Audience, Channel, PublishingAuthority>
```

Transferable lesson: release authority is distinct from representation creation, source authority and downstream delivery/possession; withdrawal cannot erase copies already distributed.

Constraint: `published` need not mean public and does not prove delivery.

# 4. Domain-family reusable Concept-knowledge candidates — CK-2

## Competition

**Candidate:** CK-2.

Reusable in competition/event-governance applications where a bounded occurrence has a meaningful lifecycle and final closeout.

Retain purpose specificity; a generic `Event` loses competitive-governance meaning.

## Division

**Candidate:** CK-2.

Reusable in competition/classification contexts where scoped members belong to comparison cohorts with correctable assignment history.

Do not generalize into arbitrary group membership.

## Team

**Candidate:** CK-2.

After 014-G, Team is a reusable scoped competing-group concept rather than intrinsically student-specific.

Constraint: its purpose remains one group acting as a single competing unit, not universal group/entity modeling.

## Panel

**Candidate:** CK-2.

Reusable in evaluation/review domains where intended evaluator grouping must remain distinct from actual participation, individual responsibility and evidence.

## Evaluation Occurrence

**Candidate:** CK-2 — strong within evaluation/review domains.

Reusable lesson: preserve what bounded evaluation event actually happened, who participated, what subject/context/basis was presented and whether the occurrence itself ended—independently of whether downstream evaluator responsibility is satisfied.

## Evaluation Obligation

**Candidate:** CK-2 — strong within evaluation/review domains.

Reusable lesson: preserve one historical responsibility to produce qualifying evidence, including terminal history and explicit successor responsibility instead of reopening a previously satisfied duty.

## Rubric

**Candidate:** CK-2.

Reusable as an evaluation-instrument Concept that defines response semantics/validity rather than merely form structure.

## Scorecard

**Candidate:** CK-2.

Reusable as one evaluator's independent judgment under an exact context/basis, with non-authoritative Draft, explicit Finalization and legitimate successor amendment/correction semantics.

## Award

**Candidate:** CK-2.

Reusable in recognition-oriented domains where selection basis and conferral authority must remain distinct.

Transferable lesson:

```text
candidate / selection basis
  != recognition
```

A later change to the basis must not silently move recognition.

# 5. Retained novelty and why it remains necessary

014-H distinguishes unfamiliar naming from actual novelty. Much of MUDAC uses familiar concepts with stricter seams. The following design choices deserve explicit retained-novelty treatment because familiar alternatives repeatedly encourage materially wrong expectation transfer.

## N-01 — Evaluation Occurrence != Evaluation Obligation

Plausible familiar alternatives:

```text
session
encounter
assignment
task
attempt
```

Why they fail when collapsed:

- what happened is not the same as who owes work;
- occurrence completion does not satisfy responsibility;
- participant history is not responsibility history;
- a terminal obligation should not be reopened merely because later evidence becomes ineligible.

Learning burden: two terms instead of one familiar workflow object.

Justification: the extra distinction directly preserves historical truth and prevents fabricated or duplicated evaluation work.

## N-02 — Historical satisfaction != current evidence eligibility

A previously satisfied Evaluation Obligation remains historically Satisfied even if the associated evidence later becomes ineligible.

```text
historical responsibility truth
  != current evidence usefulness
```

Familiar task systems commonly collapse these meanings into `done/not done`.

This distinction is retained because correction must not rewrite what actually happened.

## N-03 — Outcome Declaration and `Affected`

A generic `final result` or `revision` model does not adequately represent MUDAC officiality.

```text
Current official declaration
  → material source change
  → Affected latest declared authority
  → explicit successor confirmation
  → predecessor Superseded
```

The design deliberately avoids silently treating recalculated state as newly official.

## N-04 — Derive → recognize → declare

```text
Aggregate / Rank
  != Award
  != Outcome Declaration
```

Familiar competition software often visually compresses these into a single winner/result experience.

MUDAC retains the separation because calculation, recognition and official declaration have different authorities and correction consequences.

## N-05 — Source authority → Export → Publication → delivery

```text
source authority
  != external representation
  != release authority
  != possession / delivery
```

This is intentionally stricter than ordinary report/share workflows so corrections, disclosure and historical release remain reconstructible.

## N-06 — Actor != represented authority != source

Assisted/paper/import/correction paths may involve one person performing the operation while another remains the semantic author and a third artifact/source provides evidence.

A generic `modifiedBy` audit field is insufficient.

## N-07 — Identity != Participation != Access

The individual concepts are familiar; the retained novelty is the refusal to collapse them into a conventional `User + Role + Permission` package.

This separation preserves context-specific capability, multi-capacity isolation and historical attribution without permission union.

# 6. Reusable design-pattern candidates — PK

These patterns recur across multiple current Concepts but do **not** have independent user-facing purposes and must not become new MUDAC Concepts.

## PK-01 — Scoped opaque-reference parameterization

Accept peer identities or bases abstractly rather than importing peer internals.

Use when a Concept needs association but not intrinsic semantic dependence.

## PK-02 — Exact-basis binding

High-consequence state should identify the exact basis used when later source change must be explainable.

MUDAC examples include EvaluationBasis, OutcomeBasis and Export SourceBasis.

## PK-03 — Explicit successor without silent historical rewrite

When authoritative state changes, preserve the predecessor and establish a successor through the owning authority rather than mutating history in place.

Vocabulary remains owner-specific; this pattern does not imply one universal successor lifecycle.

## PK-04 — Actor / represented authority / source separation

Record who performed an operation, whose semantic authority the result represents, and what source justified/captured the state as separate dimensions.

## PK-05 — Historical accomplishment versus current eligibility

A fact that was legitimately accomplished in history need not remain currently usable after later invalidation/correction.

Do not rewrite the historical accomplishment to express present ineligibility.

## PK-06 — Derivation → recognition → declaration

Calculation/ordering, recognition and official authority are separate semantic steps with separate owners.

## PK-07 — Source → representation → release → delivery

Source authority, generated representation, release authority and external transport/possession are separate layers.

## PK-08 — Context capability without authorship transfer

Permission to act or assist never by itself changes semantic authorship or decision ownership.

# 7. Catalog-candidate discipline

014-H does **not** create an external/shared catalog.

The durable [Reusable Concept Knowledge & Design Patterns](../canonical/project/reusable-design-knowledge.md) registry records candidate status and transferable lessons while linking to the existing natural Concept owners.

A future shared/Base catalog entry should require evidence beyond this one project, such as:

- successful use in another independently designed application;
- a well-defined external precedent with materially compatible semantics;
- a deliberate cross-project comparison confirming that the same purpose/behavior recurs;
- enough misfit examples to state when the concept/pattern should **not** be reused.

Until then:

```text
MUDAC canonical Concept owner = current MUDAC truth
reusable registry = candidate / lesson index
external concept catalog = not created here
```

# 8. Subjects intentionally not promoted to catalog concepts

The following remain valuable but do not justify new catalog concepts:

- `Group` — structural commonality only;
- `Scoped Relationship` — shared shape across materially different purposes;
- generic `Occurrence` — insufficient singular purpose across Competition/Evaluation Occurrence;
- `Task / Work Item` — would corrupt historical responsibility and derived Remaining Work;
- `Historical / Correctable Record` — owner-specific temporal semantics differ;
- generic `Result` — collapses calculation, recognition and officiality;
- generic `Representation` as a merged Export/Publication owner — creation/currentness and release authority differ;
- universal `Status` / `Workflow` / `Revision` — vocabulary or implementation abstractions, not application Concepts.

# 9. Mental-model and mapping obligations for retained novelty

Where novelty or unusually strict semantics survive, downstream representation must help users understand them without requiring Concept-Design vocabulary everywhere.

Examples:

- explain an Evaluation Obligation as an `assigned evaluation` where useful, while preserving terminal/successor semantics;
- use `Judge Scorecard` where `Scorecard` could be mistaken for Aggregate/standings;
- represent `Affected` official outcome as still the latest declared authority requiring review, not as silently unofficial;
- explain stale/affected Export currentness separately from Publication withdrawal;
- use owner-specific actions such as `Finalize Evaluation`, `Confirm Successor Outcome Declaration`, `Generate Export`, and `Withdraw Publication` instead of generic `Submit`, `Revise`, `Share`, or `Delete`.

The canonical vocabulary owner remains the current authority for these expectation-transfer rules.

# 10. Reopen / propagation result

014-H finds no semantic defect requiring Phase-010/011/012/013 reopen.

The new durable reusable-knowledge registry adds cross-context candidate/disposition knowledge only. It does not redefine any current Concept.

Required propagation:

- add the reusable-knowledge registry to Project/canonical navigation;
- update Phase-014 and repository handoff surfaces to 014-I;
- keep current Concept specifications as the sole semantic owners;
- carry the 014-G Team refinement into the later 014-I propagation/integrity check;
- preserve implementation quarantine.

# 11. Phase-015 carry-forward candidates

No known contradiction is deferred, but Phase 015 should deliberately stress these subtle interference risks:

1. whether separate reusable history/currentness patterns accidentally behave like one generic revision system in composition;
2. whether Identity/Participation/Access isolation survives multi-capacity and support scenarios without hidden capability union;
3. whether exact-basis binding across evaluation, declaration and Export can coexist without circular currentness dependencies;
4. whether derive→recognize→declare and source→represent→release chains remain compositional under correction bursts;
5. whether successor work creates duplicate semantic weight or ambiguous currentness under concurrency/recovery;
6. whether retained novel vocabulary remains explainable without UI-owned workflow state.

These are integrity probes, not known defects.

# 12. Risk disposition

014-H materially addresses:

- **FRG-R08 — Catalog duplication:** reusable registry links to natural owners instead of cloning specifications;
- **FRG-R09 — Novelty without justification:** retained unusual seams now have explicit alternatives/misfit rationale;
- **FRG-R13 — Historical-adapter revival:** `Encounter` and `Official Outcome Revision` remain negative precedents, not catalog candidates;
- **FRG-R14 — Taxonomy for taxonomy's sake:** candidate classes are pragmatic disposition labels, not a universal ontology;
- **FRG-R15 — Integrity deferral abuse:** no known contradiction is deferred to Phase 015.

# Exit

**014-H COMPLETE — PASS. Proceed to 014-I — Refinement Propagation, Reopen/Repair Decisions & Obvious Integrity Check.**
