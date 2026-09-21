---
type: Project Vocabulary Authority
title: MUDAC Domain Vocabulary & Expectation-Transfer Rules
description: "Cross-catalog vocabulary authority for canonical terms, qualified explanatory labels, analogy-only language and high-risk generic words whose ordinary meanings could collapse MUDAC authority, lifecycle, history, disclosure or release semantics."
status: stable
tags: [project, vocabulary, terminology, familiarity, expectation-transfer, phase-014]
sources:
  - resource: ../../014-familiarity-reuse-genericity/014-C-competition-competitor-grouping-identity-participation-alias-access-familiarity-reuse-audit.md
  - resource: ../../014-familiarity-reuse-genericity/014-D-evaluation-occurrence-obligation-rubric-scorecard-familiarity-reuse-audit.md
  - resource: ../../014-familiarity-reuse-genericity/014-E-versioning-provenance-award-outcome-declaration-export-publication-familiarity-reuse-audit.md
  - resource: ../../014-familiarity-reuse-genericity/014-F-cross-catalog-false-familiarity-terminology-expectation-transfer-audit.md
  - resource: ../concepts/
  - resource: ../mechanisms/
  - resource: ../experience/action-authority-traceability.md
  - resource: ../experience/status-feedback-recovery.md
---

# Purpose

Keep familiar language from changing MUDAC meaning.

This owner does not redefine Concept, synchronization, dependence, mechanism or Experience semantics. Natural canonical owners remain authoritative. This document records how common words may safely refer to those meanings and where familiar vocabulary would import materially incorrect expectations.

# Governing rule

> Prefer the most familiar wording that preserves the correct owner, authority, lifecycle, history and disclosure expectations.

Familiarity is helpful only when it does not collapse semantic seams.

```text
familiar word != semantic owner
same noun != same lifecycle
same state label != same authority
same verb != same consequence
```

# Terminology classes

## T1 — Canonical semantic term

Current Concept, mechanism, owner-qualified state/action, policy or invariant language.

Use when semantic precision matters.

## T2 — Qualified explanatory label

Familiar user-facing/prose wording that clearly maps to one T1 owner and preserves its semantics.

The label does not create another Concept/action/state.

## T3 — Analogy-only term

Useful for explanation or comparison but unsafe as a current semantic label because ordinary expectations materially differ.

## T4 — High-risk generic term

Ambiguous vocabulary that must not stand alone for a consequential action/state when multiple owners or history consequences are possible.

# Current Concept vocabulary

All eighteen current Concept names remain canonical:

```text
Competition
Division
Team
Panel
Evaluation Occurrence
Evaluation Obligation
Rubric
Scorecard
Award
Identity
Participation
Alias
Access
Versioning
Provenance
Outcome Declaration
Export
Publication
```

`Judging Encounter` / `Encounter` and `Official Outcome Revision` are historical adapters only.

# Familiar explanatory labels

These phrases may be used when the mapping remains explicit:

| Explanatory label | Canonical meaning | Constraint |
| --- | --- | --- |
| Judge/Organizer mode | current Participation/Capacity context | mode never creates Participation or Access |
| Judge/Organizer role | Participation Capacity in ordinary prose | never a persistent permission bundle |
| permission | result of current Access evaluation | never semantic authorship or Participation |
| judging/evaluation event | Evaluation Occurrence | event completion does not satisfy responsibility |
| assigned evaluation / evaluation responsibility | Evaluation Obligation | not a generic reopenable task |
| scoring guide / evaluation instrument | Rubric | current definition != authoritative historical basis |
| Judge Scorecard | Scorecard | not Aggregate, Rank or official result |
| official outcome | Outcome Declaration authority | official does not mean public |
| report / snapshot / extract | Export where Export contract is actually satisfied | exact SourceBasis/purpose/audience/currency remain required |
| release | Publication action/state | release != delivery; Publication need not be public |

# Actor and capability words

## User / Account

Generic product words only. They do not replace Identity, Participation or Access.

```text
Identity != account
Identity != authentication/session
```

## Role

Use as human-friendly shorthand only for a Participation Capacity when context is clear.

```text
role label != Participation lifecycle
role label != Access decision
```

## Permission

Use only as ordinary explanation of a current Access result.

```text
permission != authorship
permission != authority owner
```

## Group

Prefer Team, Division or Panel according to the actual semantic owner.

# Evaluation-work words

## Session / Encounter / Attempt

T3 analogies for Evaluation Occurrence only.

`Session` must not imply transient/non-historical state; `Attempt` must not imply one actor's success/retry lifecycle; `Encounter` must not restore the deprecated overloaded model.

## Assignment / Task / Work Item

May explain an Evaluation Obligation only when responsibility semantics remain explicit.

Never use generic task semantics to imply writable Remaining Work, mutable assignee identity, reopening terminal responsibility or current evidence eligibility.

## Form

Representation only. A form is neither Rubric authority nor Scorecard authority.

## Submission / Submit

T4 for authority-establishing Judge actions.

Use **Finalize Evaluation** for semantic Judge commitment.

```text
sent / saved / persisted != Finalized
```

## Score

Owner-qualified only. Criterion score, Rubric-derived total, Aggregate and Rank are different meanings.

# State and lifecycle words

MUDAC has no universal `Status`.

Prefer `state` plus the owning subject when ambiguity matters.

## Draft

Owner-qualified: Competition Draft, Rubric Draft/working definition, Scorecard Draft.

## Ready

```text
Competition Ready lifecycle
!= Competition Readiness
!= Ranking Readiness
!= Finalization Readiness
```

## Complete / Completed

```text
Evaluation Occurrence Complete
!= Evaluation Obligation Satisfied
!= Scorecard Finalized

Competition Event Completed
!= Competition Finalized
```

Use subject-specific action labels such as **Complete Evaluation Occurrence** and **Complete Live Event**.

## Final / Finalized

`Finalized` is subject-specific. Avoid unqualified `final result`.

```text
Scorecard Finalized
!= Competition Finalized
!= official Outcome Declaration
```

## Current

Always interpret relative to an owner/basis: current Participation, current eligible Version, Outcome Declaration Current, Export Current, current derived result.

# Historical/currentness words

These are intentionally distinct:

```text
Superseded
Invalidated
Replaced
Affected
Stale
Retired
Withdrawn
```

- **Superseded** — explicit successor became current for the relevant owner/lineage.
- **Invalidated** — retained historical state is no longer eligible; successor is not implied.
- **Replaced** — a distinct subject/occurrence stands in place of another; not ordinary supersession.
- **Affected** — material dependency changed and review/correction is required; not necessarily known-wrong.
- **Stale** — Export known not to represent the applicable current basis for ordinary current use while remaining historical representation truth.
- **Retired** — removed from ordinary use while retained historically; not Publication withdrawal.
- **Withdrawn** — owner-specific cessation; never generic deletion.

Do not flatten these to `old`, `inactive`, `closed`, `revised` or `deleted` when the difference is material.

# Change and correction verbs

## Edit

Safe for non-authoritative working state where ordinary edit semantics are true.

For authoritative/history-bearing state use the owner-specific action:

```text
Judge judgment change           → amendment
capture/source mismatch         → source-faithful correction
structural binding defect       → invalidation / replacement
Award recognition correction   → revoke / correct conferral / new conferral
official outcome correction     → successor Outcome Declaration
new source representation       → new/successor Export
released representation change → withdraw / successor Publication
```

## Revision

T3/T4 cross-catalog vocabulary. Do not create a generic Revision owner.

Use Version, amendment, correction or successor according to the natural owner.

## Reopen / Reset / Revert / Undo

T4 for authority/history-bearing state. They often imply history rollback that MUDAC intentionally rejects.

## Delete

Must not substitute for invalidation, revocation, withdrawal, retirement or supersession where history is retained.

## Resolve / Fix / Force / Override

T4 high-consequence verbs. Route to the natural source/correction/exception action instead.

# Recognition and officiality words

## Result

Generic explanatory noun only. It does not establish officiality.

## Winner

Use only when the governing Award/Outcome semantics actually define a winner and the current authority state is clear.

```text
top-ranked Team
!= Award recipient by implication
!= official winner by implication
```

## Award

Recognition owner. Prefer `conferred Award` where distinction from a calculated candidate matters.

## Official

Outcome authority requires explicit Outcome Declaration.

```text
calculated != recognized != official
Competition Finalized alone != official
```

Do not infer `official Award` from conferral alone; describe official outcome inclusion through the applicable Outcome Declaration when required.

## Final result

Avoid as canonical state language. Prefer current official Outcome Declaration or a context-specific phrase that preserves correction/successor semantics.

# Representation and release words

## Report / Snapshot / Extract

T2 only when the object actually obeys Export semantics. Otherwise they are realization artifacts, not automatically Export Concepts.

## Download / Print

Transport/realization operations. Not Publication authority.

## Share / Send

T4 where release authority could be implied. Deliberate audience/channel release maps to Publication; downstream transport of an already-authorized representation does not create a new Publication by itself.

## Publish / Release

Use **Publish Representation** for the authoritative Publication action. `Release` is an acceptable explanatory synonym if exact Representation, Audience/Channel and PublishingAuthority remain clear.

## Public

Audience/disclosure qualifier, not Publication state.

```text
Published != necessarily public
official != public
```

## Delivered / Viewed / Possessed

Downstream recipient/transport observations only.

```text
Published != delivered
possession != Access
possession != current release authority
```

# Derived and work-context vocabulary

## Readiness

Always qualify where necessary: Competition Readiness, Ranking Readiness, Finalization Readiness. Readiness is derived/non-writable.

## Remaining Work

Projection over Outstanding Evaluation Obligations, not an independent task list.

## Coverage

Factual sufficiency only. `Incomplete + accepted exception for a consequence` is valid; exception does not rewrite Coverage to Satisfied.

## Aggregate

Derived numerical state, not automatically `final score` or official result.

## Rank

Derived ordering. `Leaderboard` is analogy-only and must not imply editable/public/official state.

## Reconciliation

Organizer work/process context, not a ticket/case lifecycle and not owner of generic `Resolve`.

## Live Operations

Work context, not Competition lifecycle.

# User-visible action vocabulary

Prefer owner-specific verbs already established by synchronization/mapping authority:

```text
Mark Competition Ready
Prepare / Begin / Complete Evaluation Occurrence
Start Evaluation
Finalize Evaluation
Begin / Finalize Amendment
Complete Live Event
Confer / Revoke / Correct Award
Finalize Competition & Declare Outcome
Confirm Successor Outcome Declaration
Generate Export
Publish Representation
Withdraw Publication
Publish Successor Representation
```

Generic verbs such as `Submit`, `Done`, `Close`, `Edit`, `Reopen`, `Reset`, `Delete`, `Resolve`, `Fix`, `Force`, `Override`, `Approve`, `Share` and `Send` must not obscure a materially different semantic consequence.

# Profile and representation rule

Judge-safe, Organizer-sensitive, Ceremony/Public, history/audit, accessible, degraded and paper-assisted representations may simplify wording but must preserve the same semantic mapping.

A simpler label may not:

- union capacities;
- grant Access;
- transfer semantic authorship;
- make a derived state writable;
- turn Draft into authority;
- turn calculated into official;
- turn official into public;
- turn Publication into delivery;
- erase current/historical distinctions.

# Writing / agent rules

1. Use current Concept names in canonical semantic specifications.
2. Use T2 familiar labels when they improve comprehension and their mapping is unambiguous.
3. Keep action/state labels subject-qualified when owner confusion could change behavior.
4. Do not infer authority from familiar words such as role, submit, final, winner, published or approved.
5. Do not introduce generic Revision, Task, Workflow, Status or Result Concepts to normalize vocabulary.
6. Preserve owner-specific currentness/history words rather than collapsing them into generic active/inactive/old/deleted labels.
7. When a user-facing label differs from the Concept name, maintain traceability to the natural semantic owner.
8. If clearer wording would require changing semantics rather than explanation, route the issue to the natural owner instead of solving it here.

# Historical non-term closure

The word **Minding** appears in a historical Phase-016 subphase title as a planning/documentation artifact. It is not a MUDAC Concept, mechanism, policy, invariant, action, state, or approved explanatory term. Do not infer semantic meaning from it or introduce it into current product vocabulary.

# Related authority

- Concept definitions → [`../concepts/`](../concepts/)
- application actions/composition → [`../synchronizations/`](../synchronizations/)
- derived mechanisms/work contexts → [`../mechanisms/`](../mechanisms/)
- interaction/action traceability → [`../experience/action-authority-traceability.md`](../experience/action-authority-traceability.md)
- multidimensional status/finality/recovery → [`../experience/status-feedback-recovery.md`](../experience/status-feedback-recovery.md)
- Phase-014 evidence and decisions → [`../../014-familiarity-reuse-genericity/`](../../014-familiarity-reuse-genericity/)

This vocabulary owner governs expectation transfer only. It never overrides the natural semantic owner.


# Phase-017 terminology closure

017-D confirms there is no unresolved current terminology blocker. The eighteen Concept names remain canonical; historical adapters remain historical; high-risk generic vocabulary remains qualified; and the historical "Minding" artifact is explicitly non-semantic.
