---
type: Phase Design Record
title: 014-F — Cross-Catalog False Familiarity, Terminology & Expectation-Transfer Audit
description: "Reconciles terminology and expectation transfer across all eighteen current Concepts plus derived/work-context vocabulary, retaining the canonical catalog while constraining ambiguous generic nouns, states and verbs that could collapse authority, lifecycle, history, officiality, representation or release semantics."
status: stable
tags: [phase-014, jackson, familiarity, terminology, false-familiarity, expectation-transfer, vocabulary]
sources:
  - resource: 014-A-familiarity-reuse-genericity-scope-criteria-evidence-subphase-planning.md
  - resource: 014-B-familiarity-evidence-baseline-precedent-taxonomy-comparison-register.md
  - resource: 014-C-competition-competitor-grouping-identity-participation-alias-access-familiarity-reuse-audit.md
  - resource: 014-D-evaluation-occurrence-obligation-rubric-scorecard-familiarity-reuse-audit.md
  - resource: 014-E-versioning-provenance-award-outcome-declaration-export-publication-familiarity-reuse-audit.md
  - resource: ../canonical/concepts/
  - resource: ../canonical/mechanisms/
  - resource: ../canonical/experience/action-authority-traceability.md
  - resource: ../canonical/experience/status-feedback-recovery.md
  - resource: ../canonical/project/domain-vocabulary-expectation-transfer.md
---

# Purpose

Audit the completed Phase-014 family dispositions as one language system.

014-F asks whether names, explanatory labels, states and action verbs transfer correct expectations **across concept boundaries**, especially where one familiar word could refer to multiple independent owners.

This is not a synonym-generation exercise and does not seek maximal vocabulary uniformity. Uniform terminology is harmful when the underlying meanings are intentionally different.

# Decision

**COMPLETE — PASS. Proceed to 014-G.**

```text
014-A start gate                                   COMPLETE — READY
014-B evidence / precedent baseline                COMPLETE — PASS
014-C Family-1 familiarity/reuse audit             COMPLETE — PASS
014-D Family-2 familiarity/reuse audit             COMPLETE — PASS
014-E Family-3 familiarity/reuse audit             COMPLETE — PASS
014-F cross-catalog terminology audit              COMPLETE — PASS
Concept rename / merge / replacement               NONE
new Concept                                        NONE
new canonical vocabulary owner                     YES
Phase-010 Concept-boundary reopen                  NO
Phase-011 synchronization reopen                   NO
Phase-012 dependence/PF-01 reopen                  NO
Phase-013 semantic mapping reopen                  NO
architecture / implementation influence            PROHIBITED
NEXT                                                014-G
```

# 1. Cross-catalog conclusion

All eighteen current Concept names remain acceptable after family and whole-catalog expectation-transfer review.

The primary false-familiarity risk is not the catalog itself. It is **generic glue vocabulary** that can silently flatten distinct owners:

```text
User / Account / Role / Permission / Group
Session / Encounter / Attempt
Task / Assignment / Work Item
Form / Submission
Status / Current / Complete / Final
Result / Winner / Score
Revision / Edit / Reopen / Revert
Resolve / Fix / Override / Force
Report / Download / Share / Publish / Deliver
```

These words are not all prohibited. They require explicit semantic qualification when their ordinary meaning could imply the wrong owner, authority transition, lifecycle, history rule or disclosure consequence.

# 2. Terminology classes

MUDAC adopts four terminology classes.

## T1 — Canonical semantic term

A current Concept, mechanism, policy/invariant term or explicitly defined owner state/action.

Use T1 vocabulary in canonical design authority when precision matters.

Examples:

```text
Participation
Access
Evaluation Occurrence
Evaluation Obligation
Scorecard Draft
Finalize Evaluation
Outcome Declaration
Export Affected
Publication Withdrawn
```

## T2 — Qualified explanatory label

A more familiar phrase may be used in user-facing explanation or prose when it clearly maps to one current owner and does not change semantics.

Examples:

```text
Judge mode                 → Judge Participation context
assigned evaluation        → Evaluation Obligation
judging/evaluation event   → Evaluation Occurrence
scoring guide              → Rubric
Judge Scorecard            → Scorecard
official outcome           → current Outcome Declaration
```

The familiar phrase is not a new Concept or action.

## T3 — Analogy-only term

Useful for comparison or explanation but unsafe as a current owner/action/state label because it imports materially wrong expectations.

Examples include `session`, `attempt`, `task`, `form`, `ballot`, `revision`, `leaderboard`, `ticket`, and generic `workflow` where the imported semantics would conflict with current authority.

## T4 — High-risk generic term

A generic word whose meaning is too ambiguous for a consequential unqualified action/state.

Examples include `Submit`, `Done`, `Complete`, `Final`, `Close`, `Edit`, `Reopen`, `Reset`, `Revert`, `Undo`, `Delete`, `Resolve`, `Fix`, `Force`, `Override`, `Share`, and unqualified `Status`.

T4 terms may appear only when ordinary language is harmless or the semantic owner/consequence is made explicit enough to prevent false expectation transfer.

# 3. Actor, identity and authorization vocabulary

## `User` / `Account`

May describe a generic product/operator notion outside canonical domain semantics, but neither replaces Identity.

```text
Identity != account
Identity != authenticated session
Identity != Participation
```

## `Role`

`Judge role` / `Organizer role` may be colloquial explanatory language only when it clearly means the current Participation **Capacity**.

Canonical authority remains:

```text
Identity
  + Competition-scoped Participation / Capacity
  + current Access
```

A role label must not imply a persistent permission bundle.

## `Permission`

May describe the result of an Access decision in ordinary language, but MUDAC does not reduce Access to stored RBAC-style permission state.

```text
Access decision != semantic authorship
permission != Participation
permission != technical possession
```

## `Group`

Use the actual owner where semantics matter:

```text
Team     = competing unit
Division = competitive cohort
Panel    = intended evaluator grouping
```

Generic `group` must not imply those concepts are interchangeable.

# 4. Evaluation-work vocabulary

## `Session`, `Encounter`, `Attempt`

These remain analogy-only for Evaluation Occurrence.

They must not imply that occurrence completion satisfies responsibility or establishes judgment authority.

`Judging Encounter` remains deprecated historical terminology.

## `Assignment`, `Task`, `Work Item`

`assigned evaluation` or `evaluation responsibility` may explain an Evaluation Obligation.

But generic task semantics are rejected where they imply:

- arbitrary creation/closure;
- mutable assignee identity;
- reopening terminal historical responsibility;
- task completion = current evidence eligibility;
- writable Remaining Work queue state.

```text
Evaluation Obligation Satisfied
  != current evidence eligibility

Remaining Work
  = projection over Outstanding obligations
  != independent task authority
```

## `Form`

May describe a representation used to enter a Scorecard Draft or define a Rubric, but it owns neither semantic meaning.

```text
form/template != Rubric authority
form fields != Scorecard authority
```

## `Submission` / `Submit`

Do not use `Submit` as the authoritative semantic label for Judge judgment commitment.

```text
Draft persisted/sent
  != Finalize Evaluation succeeded
```

The canonical high-consequence action is **Finalize Evaluation**.

`submission` may describe transport/request mechanics only when it is clearly not authority.

## `Score`

A criterion response or Rubric-derived total may legitimately be called a score where the Rubric defines that meaning.

Unqualified `Score` must not mean Scorecard, Aggregate, Rank, Award or official outcome.

# 5. Lifecycle and status vocabulary

MUDAC has no universal domain `Status`.

State words must normally be **subject-qualified** because the same familiar term can mean different things under different owners.

## Draft

Examples include Competition Draft, Rubric working Draft and Scorecard Draft. These are not one shared lifecycle.

## Ready

Preserve:

```text
Competition lifecycle Ready
  != Competition Readiness projection
  != Ranking Readiness
  != Finalization Readiness
```

## Active

Competition Active, Participation Active and other owner-specific active states must not be treated as one global operating state.

## Complete / Completed

Preserve:

```text
Evaluation Occurrence Complete
  != Evaluation Obligation Satisfied
  != Scorecard Finalized

Competition Event Completed
  != Competition Finalized
```

Avoid unqualified `evaluation complete`, `event done` or `all done` where the owner is unclear.

## Final / Finalized

`Finalized` is owner-specific.

```text
Scorecard Finalized
  != Competition Finalized
  != official Outcome Declaration
```

Avoid `final result` as a canonical state label because official authority can later become Affected and receive an explicit successor without rolling Competition lifecycle backward.

## Current

`Current` is meaningful only relative to an owner/basis:

```text
current Participation
current eligible Version
Outcome Declaration Current
Export Current
current derived result
```

Do not present one global `Current` badge as though these meanings were equivalent.

# 6. Historical/currentness vocabulary

These terms are not synonyms and must normally identify their owner or subject.

```text
Superseded
Invalidated
Replaced
Affected
Stale
Retired
Withdrawn
```

Core distinctions:

- **Superseded** — a legitimate successor became current for the relevant owner/lineage.
- **Invalidated** — retained historical state is no longer eligible for its authoritative purpose; no successor is implied.
- **Replaced** — a distinct subject/occurrence stands in place of another; not ordinary Version supersession.
- **Affected** — a material dependency changed and review/correction is required; this does not necessarily mean known-wrong. Outcome Declaration Affected remains the latest declared official authority until successor confirmation.
- **Stale** — an Export is known not to reflect the applicable current basis for its intended ordinary current use while remaining historically faithful to its bound source.
- **Retired** — retained historical material is removed from ordinary use; does not imply Publication withdrawal.
- **Withdrawn** — owner-specific cessation such as Publication release authority, Team Participation context, or other explicitly defined owner semantics; it is never a universal deletion meaning.

Never flatten these into generic `old`, `inactive`, `revised`, `closed` or `deleted` when the difference affects authority/history.

# 7. Change/correction action vocabulary

## `Edit`

Safe for clearly non-authoritative working content where ordinary edit semantics apply.

Once authoritative/history consequences exist, use the natural action:

```text
Judge changes judgment          → amendment
capture differs from source     → source-faithful correction
structural binding wrong        → invalidation / distinct replacement
Award recognition wrong         → revoke / correct conferral / new conferral
Outcome basis corrected         → successor Outcome Declaration
Export needs newer source       → new Export / supersession
released representation changes → withdraw / successor Publication
```

## `Revision`

Avoid as a cross-catalog current noun/action.

The deprecated `Official Outcome Revision` demonstrated why generic revision terminology is unsafe.

Use Version, amendment, correction, successor declaration, successor Export or successor Publication according to the actual owner.

## `Reopen`, `Reset`, `Revert`, `Undo`

These are high-risk generic actions because they often imply history can be rolled backward.

MUDAC instead preserves predecessor/current/successor truth and owner-specific correction actions.

In particular:

```text
terminal Evaluation Obligation != reopenable task
invalidated Version != automatic revert to predecessor
Competition Finalized != rolled backward by result correction
```

## `Delete`

Must not stand in for invalidation, revocation, withdrawal, retirement or historical supersession where retained history is required.

# 8. Outcome and recognition vocabulary

## `Result`

Generic explanatory word only. It can refer to a calculation result, action result or declared outcome, so it must not itself imply officiality.

## `Winner`

A particularly high-risk familiar term.

```text
top-ranked Team
  != recognized Award recipient by implication
  != official winner by implication
```

Use `winner` only when the applicable Award/Outcome semantics actually define that meaning and the relevant authority state is clear.

## `Award`

Award is recognition, not a synonym for rank position.

Prefer `conferred Award` when distinguishing recognition from a calculated candidate.

## `Official`

Only explicit Outcome Declaration establishes official outcome authority.

```text
calculated != recognized != official
Competition Finalized alone != official outcome
```

An `official Award` label should not be inferred merely from conferral; if official-result semantics include the Award, describe that through the applicable Outcome Declaration/basis.

## `Final result`

Avoid as canonical language. Prefer `current official Outcome Declaration` or subject-specific explanatory wording.

# 9. Representation, release and delivery vocabulary

## `Report`, `Snapshot`, `Extract`

May be explanatory names for an Export representation when the artifact actually follows Export semantics.

They must not weaken:

```text
exact SourceBasis
+ purpose / RepresentationProfile
+ AudienceProfile
+ representation currency
```

A disposable generated file is not automatically equivalent to the Export Concept.

## `Download`, `Print`

Transport/realization operations. They do not themselves establish Publication authority.

## `Share`, `Send`

High-risk generic verbs.

If the user intent is deliberate release to an audience/channel, map to Publication semantics. If it is only transport of an already-authorized representation, it remains downstream delivery/realization.

Do not let `Share` bypass AudienceProfile/disclosure or PublishingAuthority.

## `Publish` / `Release`

Use **Publish Representation** for the current Publication authority action.

`release` is a valid explanatory synonym when the exact representation, audience/channel and publishing authority remain explicit.

Publication need not be public.

## `Public`

An AudienceProfile/disclosure idea, not a synonym for Publication state.

```text
Publication Published != public audience necessarily
Outcome Declaration Current != public
```

## `Delivered`, `Viewed`, `Possessed`

Downstream realization/recipient conditions only.

```text
Publication Published != delivery
recipient possession != current Publication authority
recipient possession != Access
```

# 10. Derived mechanism and work-context vocabulary

## Readiness

Always qualify the target where ambiguity exists:

- Competition Readiness;
- Ranking Readiness;
- Finalization Readiness.

Readiness is derived permission/explanation, not writable authority.

## Remaining Work

Projection over current Outstanding obligations, not a user-maintained task list.

## Coverage

`Incomplete` is factual sufficiency. A governed exception may permit a consequence without relabeling Coverage `Satisfied`.

## Aggregate

Derived numerical combination, not automatically a final/official score.

## Rank

Derived ordering over the supplied eligible set. `Leaderboard` is analogy-only and must not imply editable/public/official standings.

## Reconciliation

Organizer work/process context, not a ticket/case Concept and not owner of generic `Resolve` state.

## Live Operations

Work context, not Competition lifecycle state.

# 11. Generic high-consequence verbs

The following are unsafe as stand-alone consequential actions when multiple owner meanings are possible:

```text
Submit
Done
Complete
Close
Finalize
Edit
Reopen
Reset
Revert
Undo
Delete
Resolve
Fix
Force
Override
Approve
Share
Send
```

Prefer owner-specific verbs already established by the action surface, for example:

```text
Mark Competition Ready
Begin Evaluation Occurrence
Start Evaluation
Finalize Evaluation
Begin / Finalize Amendment
Correct Authoritative Capture
Invalidate Evaluation Occurrence / evidence through owner-specific composition
Require Successor Evaluation
Complete Live Event
Confer / Revoke / Correct Award
Finalize Competition & Declare Outcome
Confirm Successor Outcome Declaration
Generate Export
Publish Representation
Withdraw Publication
Publish Successor Representation
```

`Finalize` itself is therefore acceptable only when the subject is explicit.

# 12. Historical/deprecated vocabulary

The following remain historical adapters and are not restored as familiar current terminology:

```text
Judging Encounter / Encounter
Official Outcome Revision
```

Familiarity is not a reason to revive them.

# 13. Profile and accessibility consistency

A terminology choice must preserve the same semantics across Judge, Organizer, Ceremony/Public, history/audit, accessible, degraded and paper-assisted representations.

Wording may be simplified, but simplification may not:

- union capabilities;
- reveal protected identity/evidence;
- turn derived state writable;
- hide Draft versus authority;
- turn official into public;
- turn publication into delivery;
- erase historical/currentness distinctions.

# 14. Canonical vocabulary owner

014-F establishes:

`docs/canonical/project/domain-vocabulary-expectation-transfer.md`

as the durable cross-catalog vocabulary/expectation-transfer authority.

That owner does **not** redefine Concept semantics. Natural Concept, synchronization, mechanism and Experience owners remain authoritative for meaning. The vocabulary owner records which familiar terms are safe, qualified, analogy-only or high-risk when referring to those meanings.

# 15. Reopen / propagation result

014-F found no semantic defect requiring Phase 010/011/012/013 reopen.

The prior 014-C event-completion Access correction remains the only Phase-014 upstream semantic repair so far.

014-F propagation is terminology/navigation only:

- add the canonical vocabulary owner;
- route project/canonical/bootstrap indexes through it;
- advance Phase 014 to 014-G;
- preserve existing natural semantic owners unchanged unless later propagation discovers stale wording that contradicts this decision.

# 16. Risk disposition

014-F directly closes or materially reduces:

- **FRG-R01 — Name-equals-fit:** names are now separated from expectation-transfer constraints;
- **FRG-R03 — False familiarity:** cross-catalog ambiguous nouns/states/verbs are explicitly classified;
- **FRG-R06 — Similarity merge:** common vocabulary cannot justify owner collapse;
- **FRG-R10 — Mapping drift:** terminology propagation has an explicit durable owner;
- **FRG-R13 — Historical-adapter revival:** Encounter and Official Outcome Revision remain historical only;
- **FRG-R14 — Taxonomy for taxonomy's sake:** the terminology classes are operational rules, not a speculative domain hierarchy.

Remaining Phase-014 risks around broader genericity, under-generalization, retained novelty and reusable/catalog knowledge continue into 014-G/H.

# 17. Phase-015 carry-forward

Phase 015 should later test whether cross-concept interactions still create interference even when vocabulary is correct, especially:

- one action affecting multiple independently qualified states;
- repeated state words such as Current/Superseded across owners;
- closeout/correction chains whose wording is precise but whose composition may still interfere;
- profile/context changes where explanatory labels could conceal authority changes;
- externalization chains where representation/release/delivery remain semantically separate under combined scenarios.

These are integrity/interference questions, not unresolved 014-F terminology defects.

# 18. Handoff to 014-G

014-G may now evaluate broader genericity and safe parameterization against a stabilized vocabulary.

It must not use a generic name as evidence that two Concepts should share a boundary or super-concept.

```text
same vocabulary shape
  != same purpose
  != same authority
  != safe generalization
```

**014-F COMPLETE — PASS. Proceed to 014-G — Broader Genericity, Parameterization, Duplication & Specialization-Pressure Audit.**
