---
type: Phase Design Record
title: 013-E — Evaluation Occurrence, Obligation, Judgment, Action Availability & Feedback Mapping
description: "Maps prepared judging into actual occurrence participation, evaluator responsibility, Judge-authored Scorecard work, explicit Finalization, action availability and truthful feedback while preserving independence, exact evaluation basis and one-logical-evaluation semantics."
status: stable
tags: [phase-013, jackson, mapping, evaluation-occurrence, evaluation-obligation, scorecard, judge, action-availability, feedback]
sources:
  - resource: 013-D-competition-preparation-competitor-panel-rubric-setup-readiness-organizer-configuration-mapping.md
  - resource: ../canonical/experience/mapping-authority-baseline.md
  - resource: ../canonical/experience/judge-evaluation.md
  - resource: ../canonical/concepts/evaluation-occurrence.md
  - resource: ../canonical/concepts/evaluation-obligation.md
  - resource: ../canonical/concepts/scorecard.md
  - resource: ../canonical/concepts/rubric.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../canonical/synchronizations/application-action-surface-composition.md
  - resource: ../canonical/policies/anonymity-disclosure.md
  - resource: ../canonical/policies/evaluation-policy.md
  - resource: ../canonical/invariants/judge-independence.md
  - resource: ../canonical/invariants/one-logical-scorecard.md
  - resource: ../canonical/invariants/organizer-not-judge-author.md
  - resource: ../canonical/invariants/truthful-authority-under-uncertainty.md
---

# Purpose

Map the active evaluation experience from a prepared evaluation situation through actual occurrence participation, individual responsibility, Judge-authored working judgment and explicit authoritative Finalization.

013-E defines how users distinguish:

- reusable Panel planning from actual Evaluation Occurrence participation;
- actual participation from Evaluation Obligation responsibility;
- responsibility from Scorecard existence;
- Scorecard Draft work from authoritative judgment;
- occurrence completion from obligation satisfaction;
- ordinary active evaluation from later amendment/correction/history work;
- action unavailability from missing, denied, completed, superseded or exceptional conditions;
- confirmed authoritative success from uncertain persistence/communication state.

It does not prescribe screen hierarchy, component behavior, autosave implementation, API/session mechanics, storage, synchronization transport, or runtime orchestration.

# Decision

**COMPLETE — PASS. Proceed to 013-F.**

```text
013-A START GATE                                COMPLETE — READY
013-B AUTHORITY / CORPUS BASELINE              COMPLETE — PASS
013-C CONTEXT / JUDGE ENTRY MAPPING            COMPLETE — PASS
013-D ORGANIZER PREPARATION MAPPING            COMPLETE — PASS
013-E ACTIVE EVALUATION MAPPING                COMPLETE — PASS
JUDGE-EVALUATION OWNER REWRITTEN               YES
ENCOUNTER AS CURRENT CONCEPT                    PROHIBITED
PANEL MEMBERSHIP == OCCURRENCE PARTICIPATION   PROHIBITED
OCCURRENCE PARTICIPATION == RESPONSIBILITY     PROHIBITED
RESPONSIBILITY == SCORECARD                     PROHIBITED
COMPLETE DRAFT == AUTHORITATIVE JUDGMENT        PROHIBITED
OCCURRENCE COMPLETE == OBLIGATION SATISFIED     PROHIBITED
FINALIZATION BY PRESENTATION END                PROHIBITED
PEER/AGGREGATE/RANK DISCLOSURE DURING JUDGING  PROHIBITED
UNCERTAIN FINALIZATION SHOWN AS SUCCESS         PROHIBITED
GENERIC VERSIONING/PROVENANCE CONTROLS          PROHIBITED
AMENDMENT/CORRECTION DETAIL REMAINS 013-F       YES
PHASE-010 REOPEN REQUIRED                       NO
PHASE-011 REOPEN REQUIRED                       NO
PHASE-012 REOPEN REQUIRED                       NO
NEXT                                             013-F
ARCHITECTURE / IMPLEMENTATION                   SUSPENDED
```

# 1. Governing active-evaluation model

The mapping must preserve the current semantic chain:

```text
prepared Evaluation Occurrence
  → confirmed actual starting evaluators
  → begin occurrence
  → Evaluation Obligation × responsible evaluator
  → optional Start Evaluation
  → one logical Scorecard Draft per obligation
  → explicit Finalize Evaluation
  → authoritative Scorecard Version + Provenance
  → obligation Satisfied
```

Every arrow represents supplied facts or coordinated application behavior, not ownership transfer.

The application must not compress the chain into a single generic `Encounter`, `Assignment`, `Judging Session`, or `Score` state that obscures who owns each meaning.

# 2. Evaluation Occurrence mapping

Evaluation Occurrence is the user-visible historical truth of one bounded evaluation event.

Its mapped meaning includes, where material:

- Competition/scope;
- Team subject;
- Judge-facing presented context such as Alias + Division;
- exact evaluation-basis identity;
- Prepared/Open/Complete/Cancelled/Invalidated state as applicable;
- starting evaluators;
- actual participant adjustments/history;
- timing and replacement relation where applicable.

The experience must not imply that current Team, Division, Alias or Panel changes rewrite the presented context already captured for a begun occurrence.

## Prepared occurrence

A Prepared occurrence means a bounded evaluation situation has been assembled with intended subject/context/basis. It does not mean:

- the occurrence has begun;
- Panel candidates actually participated;
- any Evaluation Obligation exists;
- any Scorecard exists;
- judging authority has been exercised.

## Begin occurrence

`Begin Evaluation Occurrence` is a coordinated application action.

At begin, the application confirms the actual starting evaluators using current Participation, Access, absence/recusal and applicable Panel/policy facts. The confirmed starting set becomes occurrence history and initial Evaluation Obligations are established compositionally.

The mapping must therefore make clear enough, before begin where ambiguity matters:

```text
planned Panel membership
  != confirmed starting evaluator set
```

A nominal Panel member who is absent before begin must not be shown as having participated or owing an evaluation merely because they were planned.

## Participant adjustment

After begin, a participant adjustment changes occurrence-participation history but does not silently decide responsibility.

The representation must not imply that removing a participant from an occurrence automatically excuses, cancels or reassigns the evaluator's obligation. Exceptional responsibility disposition is a separate governed action and receives deeper live-operations/correction treatment in 013-G/013-F.

## Complete occurrence

`Complete Evaluation Occurrence` records that the bounded event ended.

It must not be represented as:

```text
all Judges finished
all obligations Satisfied
all Scorecards Finalized
presentation end == Finalization
```

Outstanding Judge work may legitimately remain after occurrence completion if current Access/policy still permits completion.

# 3. Evaluation Obligation mapping

Evaluation Obligation is one evaluator's responsibility to produce one qualifying independent evaluation under the supplied subject/basis/context.

A Judge-facing work representation should make responsibility intelligible through the current obligation rather than through Panel membership or generic assignment language.

Material obligation state includes:

```text
Outstanding
Satisfied
Excused
Cancelled
```

and predecessor/successor relationship where applicable later.

## Outstanding does not mean Scorecard exists

Before `Scorecard.start`:

```text
Evaluation Obligation = Outstanding
Scorecard = absent
```

The experience may describe this as `Not started` work, but `Not started` is a representation of obligation/work status, not a Scorecard lifecycle value.

## Satisfied means qualifying evidence was established

Ordinary satisfaction occurs only through successful Finalize Evaluation composition.

The representation must not show responsibility as Satisfied merely because:

- the occurrence completed;
- the Judge filled every visible criterion;
- a Draft was saved;
- a score total can be computed;
- the Judge left the task;
- the UI believes submission probably succeeded.

Historical satisfaction later becoming ineligible is a distinct correction/currentness question for 013-F/G, not reopening the obligation to Outstanding.

## Missing is explicit

Outstanding/missing evaluation work remains visibly missing responsibility rather than zero-valued evidence or a fabricated empty Scorecard.

# 4. Judge work context

Before a Judge changes judgment, the experience must provide enough stable context to avoid evaluating the wrong subject or basis.

At minimum where relevant, the Judge must be able to understand:

- current Competition/capacity context under 013-C;
- Judge-safe Team identity: Alias + Division during blinded judging;
- the occurrence/work subject;
- that this Judge has the relevant Outstanding obligation;
- exact applicable evaluation basis/Rubric context sufficient to understand the instrument;
- whether current Access permits the action;
- whether the work is Not Started, Draft, or already Finalized/Satisfied.

The mapping does not require a particular page/header arrangement.

# 5. Exact Evaluation Basis mapping

Judge work is bound to the exact authoritative Rubric Version supplied through the Evaluation Occurrence/Obligation.

The active evaluation experience must not behave as though the latest working Rubric automatically governs existing work.

Preserve:

```text
current working Rubric
  != exact bound Evaluation Basis
```

A later Rubric successor does not silently rebind an existing occurrence, obligation or Scorecard Draft.

The Judge must receive the criterion definitions, response domains, instructions/guidance and note requirements corresponding to the bound basis.

Whether a different basis invalidates/replaces existing work belongs to 013-F temporal authority mapping.

# 6. Start Evaluation and one logical Scorecard

`Start Evaluation` is a direct Judge application action on an Outstanding Evaluation Obligation when current Access and structural/basis conditions permit it.

Successful start establishes or resolves the **same one logical Scorecard** for that obligation.

Repeated start/resume intent, device changes, reloads or recovery must not appear to create additional independent evaluations.

The mapping invariant is:

```text
one Evaluation Obligation
  → at most one logical Scorecard
```

The Judge may resume the existing Draft when legitimate rather than starting another evaluation.

If the obligation is terminal or a logical Scorecard has already been authoritatively finalized, ordinary `Start Evaluation` is unavailable; later legitimate changes use amendment/correction/successor semantics rather than another initial Scorecard.

# 7. Scorecard Draft mapping

A Scorecard Draft is working Judge judgment and remains non-authoritative.

The experience must clearly preserve:

```text
Draft exists
  != Draft complete
  != Finalized
  != authoritative Scorecard Version
  != obligation Satisfied
```

A complete Draft may be review-ready while still non-authoritative.

Draft interaction may expose criterion responses, criterion Notes, overall Notes and completeness/validation feedback supplied by the exact Rubric basis.

`clear`/missing, zero, and any configured not-applicable semantics must not be conflated.

Leaving or deferring a Draft does not implicitly abandon the obligation or Finalize the evaluation.

# 8. Independent judgment disclosure

During ordinary judging the Judge may access their own evaluation work but not peer judgment or outcome signals that could anchor the evaluation.

The active evaluation mapping therefore withholds:

- peer Scorecards and Notes;
- Panel means;
- Coverage;
- Aggregate;
- Rank;
- standings.

Finalizing one's own Scorecard does not unlock those signals while ordinary judging remains in effect.

Judge-safe subject disclosure remains Alias + Division unless current policy explicitly permits additional attributes.

# 9. Action availability model

Action visibility/availability should reflect current semantic preconditions without turning disabled controls into the authority model itself.

The following action meanings apply.

| Application action | Primary semantic availability | Result |
| --- | --- | --- |
| Prepare Evaluation Occurrence | legitimate Organizer/current Competition preparation context | Prepared occurrence; no responsibility yet |
| Begin Evaluation Occurrence | Competition Active; prepared context/basis valid; actual evaluator set confirmed; policy/access conditions satisfied | occurrence Open + initial Outstanding obligations |
| Complete Evaluation Occurrence | legitimate authority over an Open occurrence | occurrence Complete only |
| Start Evaluation | Judge has applicable Outstanding obligation, legitimate bound basis/context and current Access | one logical Scorecard Draft exists/resumes |
| Draft response/note edits | current Judge-authored Draft and current Access | working non-authoritative state changes |
| Finalize Evaluation | Draft valid/complete under exact basis; current obligation Outstanding; Judge intent explicit; current Access and authority conditions satisfied | authoritative Scorecard + obligation Satisfied |

Unavailable actions should be explainable in terms of the source condition when doing so does not disclose protected information.

Examples include:

```text
no obligation exists
obligation already Satisfied/Excused/Cancelled
Competition/context does not permit work
current Access denies action
evaluation basis unavailable/ineligible
Draft incomplete or invalid under bound Rubric
occurrence not yet begun
current correction/invalidation condition blocks authority establishment
```

The mapping must avoid a single generic `disabled` or `unauthorized` explanation when distinct source conditions imply different legitimate next actions.

# 10. Draft validation and review feedback

Draft feedback must distinguish at least:

- response recorded versus not recorded;
- semantically valid versus invalid under bound Rubric;
- required Note missing versus optional Note absent;
- Draft complete/valid versus incomplete/invalid;
- saved/preserved working state versus authoritative Finalization.

A calculated subtotal/total, if represented, is working interpretation under the bound Rubric and does not itself establish authoritative evaluation evidence.

Review before Finalization may summarize what will be committed, but review completion is not Finalization.

# 11. Explicit Finalize Evaluation

Judge Finalization must be an explicit semantic commitment.

Presentation end, navigation away, occurrence completion, all fields becoming complete, auto-save, inactivity or organizer event control must not substitute for Judge Finalization intent.

Successful Finalize Evaluation coordinates:

```text
Scorecard.finalize
  + authoritative Scorecard Version establishment
  + meaningful Provenance
  + EvaluationObligation.satisfy
```

The application-facing success explanation should communicate the semantic result without exposing generic Versioning/Provenance machinery as separate controls.

After confirmed success:

- the Scorecard is authoritative;
- the ordinary initial Draft is no longer editable as though still unfinalized;
- the obligation is Satisfied;
- one logical evaluation weight is preserved.

# 12. Truthful Finalization feedback under uncertainty

The representation must distinguish:

```text
working Draft preserved
Finalize request in progress/unknown
Finalize confirmed successful
Finalize rejected/failed with known reason
```

If the authoritative result is uncertain, the experience must not claim success.

A retry/resume path must converge on the same logical Scorecard/obligation rather than presenting the Judge with a second independent submission opportunity.

Stale local state must not silently overwrite a newer authoritative state.

The exact offline/sync/runtime mechanism is deferred to architecture/implementation and cross-cutting 013-J mapping.

# 13. Organizer and support boundary during Judge work

Organizer/support capability to coordinate, inspect operational status or assist recovery does not make that actor the semantic author of Judge judgment.

The active evaluation experience must not expose an Organizer control that simply sets Judge criterion responses or Finalizes a Judge Scorecard as though the Organizer were the Judge.

Paper/assisted capture and source-faithful correction have distinct represented-authority semantics and belong to 013-F.

Technical support may restore operation/context but cannot manufacture a Scorecard, obligation satisfaction or Judge Finalization authority.

# 14. Active evaluation versus amendment/correction

The older Experience owner coupled initial judging and later amendment. 013-E deliberately separates them.

This workstream owns:

```text
Outstanding obligation
  → Start Evaluation
  → initial Scorecard Draft
  → explicit Finalize Evaluation
  → Satisfied obligation
```

013-F owns the user-visible semantics for:

- Judge amendment after Finalization;
- paper/assisted capture authority;
- source-faithful correction;
- invalidation;
- structural error;
- predecessor/successor authoritative states;
- replacement occurrence/evidence;
- successor evaluation responsibility;
- historical/current authority distinction.

The active-evaluation owner may point to those paths but must not flatten them into ordinary `Edit` or `Reopen` behavior.

# 15. State explanation matrix

| User-visible work meaning | Evaluation Occurrence | Evaluation Obligation | Scorecard | Authority meaning |
| --- | --- | --- | --- | --- |
| Planned evaluation | Prepared | absent | absent | no Judge responsibility/evidence |
| Ready active participant work | Open | Outstanding | absent | responsibility exists, judgment not started |
| Judge working | Open or Complete | Outstanding | Draft | non-authoritative judgment work |
| Occurrence ended, Judge unfinished | Complete | Outstanding | absent or Draft | event ended; responsibility remains |
| Judge finalized | Open or Complete | Satisfied | authoritative finalized state | qualifying evidence established |
| Judge legitimately excused | Open or Complete | Excused | no qualifying initial evidence required | responsibility ended by governed authority |
| Work cancelled | applicable historical occurrence state | Cancelled | no qualifying evidence | responsibility ended without fabricated judgment |

This matrix is semantic explanation, not a prescribed status component or database schema.

# 16. Mapping risks closed or reduced

013-E closes/reduces:

- **MAP-R01** — deprecated Encounter collapse: active Judge work now maps through Occurrence + Obligation + Scorecard;
- **MAP-R03** — raw Concept-action leakage: P/X mechanics stay hidden behind application actions;
- **MAP-R05** — Panel / participant / responsibility / evidence collapse: explicitly separated;
- **MAP-R06** — Draft / persistence / authority collapse: explicitly separated;
- **MAP-R07** — missing / zero / incomplete collapse: active evaluation retains missing as missing and Rubric validation distinctions;
- **MAP-R12** — semantic parity: active evaluation states/actions now define obligations later re-audited across accessibility/degraded modes in 013-J;
- **MAP-R15** — support privilege as domain authority: prohibited for Judge authorship/finalization.

MAP-R10 correction/history remains intentionally open for 013-F rather than being prematurely solved here.

# 17. Reopen audit

No new Concept, synchronization, dependence or PF-01 inclusion problem was found.

The current model supports the required mapping without inventing a generic Encounter/Assignment/Task/Workflow owner.

```text
Phase-010 reopen: NO
Phase-011 reopen: NO
Phase-012 reopen: NO
```

# 18. Canonical ownership result

013-E rewrites and accepts:

- `docs/canonical/experience/judge-evaluation.md`

for ordinary active evaluation mapping.

The owner is narrowed so amendment/correction/history detail no longer lives there as coequal active-evaluation semantics; those meanings move to the 013-F `authority-lineage-correction.md` owner when substantive mapping is created.

Cross-cutting status/recovery grammar remains scheduled for 013-J; 013-E establishes only the domain-specific feedback obligations needed to map active evaluation correctly.

# Exit review

013-E passes because:

1. Evaluation Occurrence, Evaluation Obligation and Scorecard have distinct visible meanings;
2. Panel membership no longer stands in for participation/responsibility;
3. actual beginning establishes obligations rather than planning state;
4. obligation existence and Scorecard existence are distinct;
5. one logical Scorecard per obligation is preserved across resume/retry;
6. Draft completeness/persistence never implies authority;
7. Judge Finalization is explicit and coordinated with obligation satisfaction;
8. occurrence completion remains independent from evaluation completion;
9. Judge Independence and Judge-safe disclosure are preserved;
10. uncertain Finalization is not represented as confirmed authority;
11. Organizer/support capability does not become Judge authorship;
12. amendment/correction/history is cleanly handed to 013-F;
13. no upstream reopen is required;
14. architecture and implementation remain suspended.

# Handoff to 013-F

Proceed to:

> **013-F — Authority Lineage, Paper Capture, Amendment, Correction & Historical-State Mapping**

013-F inherits these hard boundaries:

```text
finalized Scorecard authority must not be silently edited
historical obligation satisfaction != current evidence eligibility
amendment != capture correction != structural correction
supersession != invalidation != replacement != successor
Organizer/capture actor != Judge semantic author
paper/electronic capture must preserve semantic parity
terminal obligation never reopens; legitimate re-evaluation uses successor responsibility
prior authoritative state remains historical and attributable
```

Architecture and implementation remain suspended.