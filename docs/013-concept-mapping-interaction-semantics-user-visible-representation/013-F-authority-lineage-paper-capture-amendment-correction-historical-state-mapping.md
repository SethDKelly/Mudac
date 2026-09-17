---
type: Phase Design Record
title: 013-F — Authority Lineage, Paper Capture, Amendment, Correction & Historical-State Mapping
description: "Maps post-Finalization authority change, paper/assisted capture, Judge amendment, source-faithful correction, invalidation, replacement, successor responsibility and current-versus-historical truth without destructive rewrite or authorship transfer."
status: stable
tags: [phase-013, jackson, mapping, authority-lineage, paper, amendment, correction, invalidation, replacement, history]
sources:
  - resource: 013-E-evaluation-occurrence-obligation-judgment-action-availability-feedback-mapping.md
  - resource: ../canonical/experience/mapping-authority-baseline.md
  - resource: ../canonical/experience/judge-evaluation.md
  - resource: ../canonical/experience/paper-export-publication.md
  - resource: ../canonical/concepts/scorecard.md
  - resource: ../canonical/concepts/evaluation-occurrence.md
  - resource: ../canonical/concepts/evaluation-obligation.md
  - resource: ../canonical/concepts/versioning.md
  - resource: ../canonical/concepts/provenance.md
  - resource: ../canonical/synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: ../canonical/policies/correction-authority.md
  - resource: ../canonical/policies/continuity-paper.md
  - resource: ../canonical/invariants/current-vs-historical-truth.md
  - resource: ../canonical/invariants/capture-channel-parity.md
  - resource: ../canonical/invariants/one-logical-scorecard.md
  - resource: ../canonical/invariants/organizer-not-judge-author.md
  - resource: ../canonical/invariants/truthful-authority-under-uncertainty.md
---

# Purpose

Map how MUDAC represents authoritative evaluation history after or around initial Scorecard Finalization when the application must preserve both current truth and attributable historical truth.

013-F defines user-visible semantics for:

- paper and assisted capture;
- represented Judge authority versus capture/verification Actor;
- Judge semantic amendment;
- source-faithful capture/transcription correction;
- structural Scorecard misbinding;
- Version supersession versus invalidation;
- Evaluation Occurrence invalidation and replacement;
- Evaluation Obligation successor responsibility;
- corrected historical assertions;
- current versus historical authority;
- action availability and consequence explanation for high-consequence corrections.

It does not prescribe storage, event sourcing, audit-log implementation, database version fields, conflict-resolution algorithms, scanning/OCR systems, queues, workflows, or UI component structure.

# Decision

**COMPLETE — PASS. Proceed to 013-G.**

```text
013-A START GATE                                COMPLETE — READY
013-B AUTHORITY / CORPUS BASELINE              COMPLETE — PASS
013-C CONTEXT / JUDGE ENTRY MAPPING            COMPLETE — PASS
013-D ORGANIZER PREPARATION MAPPING            COMPLETE — PASS
013-E ACTIVE EVALUATION MAPPING                COMPLETE — PASS
013-F AUTHORITY / CORRECTION MAPPING           COMPLETE — PASS
AUTHORITY-LINEAGE OWNER CREATED                YES
PAPER CAPTURE AS SEPARATE EVALUATION MODEL     PROHIBITED
CAPTURE ACTOR == JUDGE AUTHOR                   PROHIBITED
FINALIZED SCORECARD EDITED IN PLACE            PROHIBITED
AMENDMENT == CAPTURE CORRECTION                 PROHIBITED
SUPERSESSION == INVALIDATION                    PROHIBITED
INVALIDATION == REPLACEMENT                     PROHIBITED
TERMINAL OBLIGATION REOPEN                      PROHIBITED
REPLACEMENT AUTO-CLONES RESPONSIBILITY          PROHIBITED
HISTORICAL RECORD SILENTLY REWRITTEN            PROHIBITED
GENERIC VERSIONING/PROVENANCE ADMINISTRATION   PROHIBITED
PHASE-010 REOPEN REQUIRED                       NO
PHASE-011 REOPEN REQUIRED                       NO
PHASE-012 REOPEN REQUIRED                       NO
NEXT                                             013-G
ARCHITECTURE / IMPLEMENTATION                   SUSPENDED
```

# 1. Governing authority-lineage model

MUDAC represents post-authority change by first asking **what semantic fact is actually changing**.

```text
Judge changes judgment
  → semantic amendment of same logical Scorecard

recorded capture differs from unchanged source
  → source-faithful capture correction of same logical Scorecard

Evaluator / Subject / OccurrenceContext / EvaluationBasis is wrong
  → structural invalidation / distinct correctly bound evidence if provable

occurrence itself is unusable
  → occurrence invalidation + optional distinct replacement occurrence

historical terminal responsibility must genuinely be performed again
  → successor Evaluation Obligation + new logical Scorecard

recorded historical assertion is wrong
  → attributable corrected historical assertion + owner-specific consequence if required
```

No generic `Edit`, `Fix`, `Reopen`, `Undo`, `Revision`, or `Correction` control may obscure these distinctions where authority or consequence differs.

# 2. Temporal vocabulary must remain distinct

The mapped experience must distinguish:

```text
Draft
  = non-authoritative working state

Current authoritative Version
  = currently eligible committed authority for one logical lineage

Superseded Version
  = predecessor retained after explicit successor became current

Invalidated Version
  = retained committed state no longer eligible for the authoritative purpose

Replacement
  = distinct logical subject/occurrence standing in place of another

Affected / Stale
  = owner-specific dependency-currentness meaning
```

Therefore:

```text
superseded != invalidated != replaced != affected != stale
```

The experience may simplify labels for a particular audience, but it must not collapse meanings when doing so would misstate current authority or history.

# 3. Current versus historical authority

User-visible history must answer three different questions when they differ:

```text
What is current now?
What was considered authoritative at the earlier time?
What does MUDAC now believe actually happened at that earlier time after later evidence/correction?
```

A correction changes current/best-known truth; it does not erase what was previously recorded, authored, relied upon, declared or released.

History therefore remains attributable rather than looking like a mutable row that always shows only the latest value.

# 4. Paper / assisted capture is the same evaluation model

Paper and assisted capture preserve the same:

- Judge/evaluator;
- Team/subject;
- Evaluation Occurrence/context;
- Evaluation Obligation;
- exact Evaluation Basis;
- criterion/note semantics;
- logical Scorecard identity;
- Judge authorship;
- evaluation weight.

Changing capture channel does not create a new kind of Scorecard or a second vote.

## Paper source representation

Where a physical source is used, the experience must preserve enough source identity to explain which retained source supports the captured judgment.

The mapped lineage is:

```text
identified physical Judge source
  → capture/transcription Draft
  → source verification
  → authoritative paper-origin Scorecard Version
```

The transcription Draft remains non-authoritative until source fidelity and the Judge's completed/committed evaluation intent are sufficiently established under current policy.

## Actor versus represented authority

Paper/assisted paths may legitimately have:

```text
Actor                = Organizer / capture / verification actor
RepresentedAuthority = Judge
Semantic author      = Judge
Source               = identified physical/external source
```

The representation must not imply that the capture actor authored the judgment.

If Judge intent is ambiguous, Organizer/support cannot infer missing values or Finalization intent. Ambiguity remains explicit until legitimately resolved.

# 5. Judge semantic amendment

After a Scorecard has been authoritatively Finalized, a legitimate Judge change to their own judgment is a **Judge amendment**.

The experience must represent it as successor work rather than reopening the initial Draft.

```text
current authoritative Scorecard Version
  → Begin Amendment
  → non-authoritative amendment Draft
  → explicit Finalize Amendment
  → successor authoritative Scorecard Version
```

While the amendment Draft exists, the predecessor remains current authority.

After successful amendment Finalization:

- the successor becomes current authority for the same logical Scorecard;
- the predecessor becomes Superseded historical authority;
- Judge remains semantic author;
- Provenance explains amendment lineage;
- the original Evaluation Obligation remains Satisfied by the same logical Scorecard;
- no additional evaluation weight is created.

Abandoning an amendment Draft leaves predecessor authority unchanged.

# 6. Source-faithful capture/transcription correction

If authoritative digital content demonstrably mismatches an identified unchanged external source, and structural identity remains correct, MUDAC uses source-faithful capture correction.

The user-visible path must communicate that this is a correction **to the recorded representation**, not a change in Judge judgment.

```text
current authoritative paper-origin Scorecard Version
  + verified source mismatch
  → Correct Authoritative Capture
  → successor authoritative Scorecard Version
```

Preserve:

```text
same logical Scorecard
same Judge semantic author
same Evaluation Obligation
same evaluation weight
capture/correction Actor may differ from Judge
```

Provenance should make the source and actor/represented-authority distinction inspectable where relevant.

A capture correction must not be labeled `Judge amended` merely because the Scorecard Version changed.

# 7. Amendment versus capture correction

The experience must make these different enough to avoid authority confusion:

| Question | Judge amendment | Capture correction |
| --- | --- | --- |
| Did Judge judgment change? | yes | no |
| Semantic author | Judge | Judge |
| Acting person may be Organizer/support? | ordinarily no for semantic change | yes, with capture-correction authority |
| Source of successor values | Judge's new intent | verified unchanged external source |
| Same logical Scorecard? | yes | yes |
| Obligation satisfied again? | no | no |
| Extra evaluation weight? | no | no |

If the system cannot determine which class applies, it must not silently choose one merely to permit editing.

# 8. Structural Scorecard error

Evaluator, Subject, OccurrenceContext and EvaluationBasis are structural Scorecard identity.

They cannot be changed through ordinary amendment or capture correction.

When structural identity is wrong:

1. preserve the incorrect Scorecard/history;
2. invalidate the unusable current Version for evaluation use where warranted;
3. do not silently rebind the logical Scorecard;
4. establish distinct correctly bound evidence only when a trustworthy source proves both correct structural binding and Judge-authored content without inference;
5. otherwise leave current evidence ineligible and let policy decide whether new evaluation work is required.

The user-visible experience must distinguish `correct content recording` from `wrong evaluation identity/context` because their authority paths differ materially.

# 9. Version supersession and invalidation mapping

## Supersession

Supersession means a legitimate successor for the **same logical lineage** became current.

The predecessor remains valid historical authority for the interval in which it was current.

## Invalidation

Invalidation means a committed Version is retained but is no longer eligible for its authoritative purpose.

After invalidation:

- the Version remains inspectable/reconstructible under appropriate Access;
- an older predecessor does not silently become current again;
- the lineage may legitimately have no current eligible Version;
- downstream evidence currentness may change;
- historical Evaluation Obligation satisfaction remains separate.

The representation must not imply that invalidating current evidence deleted it or automatically selected a replacement.

# 10. Evaluation Occurrence invalidation

An invalidated Evaluation Occurrence **happened** but is no longer eligible for its intended evaluative use.

The experience should preserve:

- occurrence identity;
- what was presented;
- actual participant history;
- timing;
- Judge-authored Scorecards;
- obligation history;
- invalidation reason/authority where appropriate;
- replacement relation if one is later established.

Invalidation is not cancellation and does not erase authentic Judge evidence merely because that evidence becomes ineligible for current aggregation.

# 11. Replacement occurrence

Re-evaluation uses a distinct replacement Evaluation Occurrence.

```text
Occurrence A = Invalidated
Occurrence B = distinct prepared/begun occurrence
A → replacement link → B
```

The mapping must make clear that replacement does not automatically copy:

- participants;
- Panel membership;
- obligations;
- Scorecards;
- Access;
- presented context;
- basis.

The replacement is new historical truth, not a mutation of the predecessor occurrence.

# 12. Responsibility after invalidation

## Outstanding predecessor responsibility

An Outstanding obligation tied to an invalid occurrence cannot remain satisfiable against that invalid context.

The application explicitly ends/cancels that responsibility as appropriate. Missing work remains missing; no empty Scorecard is fabricated.

If replacement work is required, a new responsibility is deliberately established against the replacement occurrence.

## Historically Satisfied responsibility

A Satisfied obligation remains historically Satisfied even if its linked evidence later becomes ineligible.

```text
historical obligation satisfaction
  != current evidence eligibility
```

If policy requires another evaluation, the predecessor obligation is not reopened.

`requireSuccessorEvaluation` creates a distinct Outstanding successor obligation, and that successor is satisfied by a **new logical Scorecard**.

## Successor work is never automatic

Evidence invalidation does not by itself decide that another Judge evaluation must happen.

Current policy may instead permit an exception, accept a preserved shortfall, or require another consequence. The mapping must present successor work as an explicit governed decision rather than an automatic cascade.

# 13. Corrected historical assertions

Current Team/Division/Alias/Panel state does not rewrite historical occurrence context.

If later evidence proves that MUDAC's recorded historical assertion itself was wrong, the experience must preserve both:

```text
as-recorded / as-known history
corrected best-known historical assertion
```

The corrected assertion needs attributable explanation through Provenance.

If the new historical truth changes evaluative validity, that consequence requires the natural owner-specific invalidation/correction action separately. Updating explanatory history alone does not silently change evidence eligibility.

# 14. Provenance representation

Provenance should be visible to the degree needed to explain meaningful authority transitions without becoming a generic administrative subsystem.

Where relevant, users should be able to distinguish:

- who acted;
- whose semantic authority/content was represented;
- source/capture channel;
- reason/classification;
- predecessor/resulting authority;
- occurrence/effective time versus later capture/correction time.

Do not expose generic `Record Provenance`, `Commit Version`, or `Invalidate Version` controls. Those remain composition-only participants in purpose-specific application actions.

# 15. Action availability and confirmation

High-consequence correction actions must communicate what authority they are about to change and what they will **not** change.

Examples:

## Finalize Judge Amendment

Before commitment, the Judge should be able to understand:

- current authoritative predecessor;
- amendment Draft differences relevant to judgment;
- that predecessor authority remains historical;
- that this remains the same logical evaluation and one vote.

## Correct Authoritative Capture

Before commitment, the actor should be able to understand:

- identified source;
- demonstrated mismatch;
- represented Judge authority;
- that Judge semantic intent is not being changed;
- that structural identity cannot be modified through this action.

## Invalidate Evaluation Evidence / Occurrence

Before commitment, the authorized actor should be able to understand:

- exact target authority/context;
- reason/evidence basis;
- loss of current eligibility;
- history retained;
- no automatic predecessor revival;
- no automatic replacement or successor Judge work.

Confirmation is a semantic consequence-understanding requirement, not a prescribed modal/dialog pattern.

# 16. Truthful feedback after correction actions

Feedback must distinguish successful authority transitions from uncertain or merely working state.

Examples include:

```text
amendment Draft started
amendment successor confirmed
capture correction Draft/review in progress
capture correction confirmed
Version invalidation confirmed
occurrence invalidation confirmed
replacement occurrence linked
successor responsibility established
historical assertion correction recorded
operation outcome unknown / requires re-resolution
```

An uncertain high-consequence result must not be displayed as confirmed merely because a request was sent.

# 17. Organizer/support authority boundary

Organizer/support authority may legitimately coordinate, capture, verify, invalidate, or correct within explicitly granted semantic boundaries.

It does not permit:

- inventing Judge judgment;
- inferring ambiguous paper intent;
- using capture correction to change Judge semantic content;
- using support privilege to manufacture correction authority;
- silently changing Scorecard structural identity;
- creating successor responsibility without governing authority.

Technical privilege and domain correction authority remain separate.

# 18. Boundary with active evaluation

013-E remains the current owner for ordinary initial evaluation:

```text
Outstanding obligation
  → Start Evaluation
  → initial Scorecard Draft
  → explicit Finalize Evaluation
  → Satisfied obligation
```

013-F owns what happens **after or around authoritative-history change**.

The active-evaluation owner must not reopen an initial Draft when 013-F semantics require an amendment, correction, invalidation, replacement, or successor responsibility.

# 19. Boundary with downstream currentness/outcomes

013-F establishes how source/evaluation authority changes and how affectedness begins.

It does not finish the user-visible mapping of:

- remaining work / operational exception surfaces;
- Coverage/Aggregate/Rank/current derived outcomes;
- reconciliation work;
- Awards;
- Competition Finalization;
- Outcome Declaration currentness/successor authority;
- Export/Publication currentness/release.

Those move to 013-G through 013-I.

# 20. Mapping-risk disposition

013-F closes or materially reduces:

- **MAP-R06** — Draft/persistence/authority collapse: predecessor authority remains explicit while successor Draft exists;
- **MAP-R10** — amendment/invalidation/replacement/successor flattened to edit/delete: explicitly separated;
- **MAP-R12** — paper/degraded semantics losing authority parity: paper mapped to same evaluation/lineage model;
- **MAP-R15** — support privilege appearing to create semantic authority: prohibited;
- historical/current-authority confusion carried from MAP-R16: split into a dedicated natural owner rather than old paper/export document boundary.

Remaining downstream currentness/outcome/distribution representation risks continue to 013-G/H/I/J/K.

# 21. Reopen test

No upstream reopen is required.

The current Concept and synchronization model already distinguishes the necessary authority classes:

- Scorecard amendment;
- Version supersession/invalidation;
- Provenance actor/represented-authority/source;
- occurrence invalidation/replacement;
- obligation successor responsibility;
- current versus historical truth.

013-F maps those distinctions rather than inventing a new correction/workflow Concept.

# 22. Canonical owner decision

Create:

- `docs/canonical/experience/authority-lineage-correction.md` as the natural Experience owner for amendment, paper/assisted capture authority, source-faithful correction, invalidation, replacement, successor responsibility and historical/current authority representation.

Migrate the paper/correction meaning formerly bundled in `paper-export-publication.md` to that new owner.

Retain `paper-export-publication.md` only as admitted legacy evidence for its still-unreconciled Export/Publication portion until 013-I establishes `external-representation-release.md`; it no longer owns current paper/correction mapping after 013-F.

# Handoff to 013-G

013-G must inherit:

1. current eligible evidence can diverge from historical satisfaction;
2. source invalidation may create outstanding operational/reconciliation pressure without automatic successor work;
3. successor Evaluation Obligation is distinct from predecessor history;
4. replacement occurrence does not copy responsibility/evidence;
5. missing/ineligible evidence remains missing rather than zero;
6. derived Coverage/Aggregate/Rank must consume current eligible authority without rewriting source history;
7. operational exception/reconciliation representation cannot become a hidden workflow Concept;
8. correction-derived Affected/Stale state must remain owner-specific and explainable.

Architecture and implementation remain suspended.
