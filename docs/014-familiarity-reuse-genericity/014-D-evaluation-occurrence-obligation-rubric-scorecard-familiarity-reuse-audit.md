---
type: Phase Design Record
title: 014-D — Evaluation Occurrence, Obligation, Rubric & Scorecard Familiarity/Reuse Audit
description: "Audits Phase-014 Family-2 evaluation Concepts against event/session, responsibility/task, rubric/instrument and scorecard/ballot/submission precedents, retaining familiar semantics while explicitly preventing collapse of occurrence, responsibility, basis and judgment authority."
status: stable
tags: [phase-014, jackson, familiarity, reuse, evaluation-occurrence, evaluation-obligation, rubric, scorecard]
sources:
  - resource: 014-A-familiarity-reuse-genericity-scope-criteria-evidence-subphase-planning.md
  - resource: 014-B-familiarity-evidence-baseline-precedent-taxonomy-comparison-register.md
  - resource: ../canonical/concepts/evaluation-occurrence.md
  - resource: ../canonical/concepts/evaluation-obligation.md
  - resource: ../canonical/concepts/rubric.md
  - resource: ../canonical/concepts/scorecard.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../canonical/experience/judge-evaluation.md
  - resource: ../canonical/experience/authority-lineage-correction.md
  - resource: ../canonical/invariants/one-logical-scorecard.md
  - resource: ../canonical/invariants/missing-never-zero.md
  - resource: https://teaching.cornell.edu/teaching-resources/assessing-student-learning/using-rubrics
    title: Cornell Center for Teaching Innovation — Using Rubrics
  - resource: https://www.cmu.edu/teaching/assessment/assesslearning/rubrics.html
    title: Carnegie Mellon Eberly Center — Creating and Using Rubrics
---

# Purpose

Perform the Phase-014 Family-2 familiarity/reuse audit over:

```text
Evaluation Occurrence
Evaluation Obligation
Rubric
Scorecard
```

The audit asks whether common evaluation-domain precedents transfer mostly correct expectations about each Concept, whether familiar terms would collapse current authority/history seams, whether any current name/boundary should change, and whether the comparison exposes a genuine upstream semantic defect.

# Decision

**COMPLETE — PASS. Proceed to 014-E.**

```text
014-A start gate                              COMPLETE — READY
014-B evidence / precedent baseline           COMPLETE — PASS
014-C Family-1 familiarity/reuse audit        COMPLETE — PASS
014-D Family-2 familiarity/reuse audit        COMPLETE — PASS
Concept rename / merge / replacement          NONE
new Concept                                   NONE
Phase-010 Concept-boundary reopen             NO
Phase-011 synchronization reopen              NO
Phase-012 dependence/PF-01 reopen             NO
Phase-013 mapping reopen                      NO
architecture / implementation influence       PROHIBITED
NEXT                                           014-E
```

# 1. Family-level result

The current Family-2 model is understandable through familiar evaluation concepts only when four meanings remain separate:

```text
Evaluation Occurrence = what bounded evaluation event actually happened
Evaluation Obligation = who was responsible to produce one qualifying evaluation
Rubric                = what instrument/response semantics governed judgment
Scorecard             = what one evaluator actually judged/authored
```

Preserve:

```text
occurrence participation != responsibility
responsibility != judgment evidence
Rubric definition != exact authoritative Evaluation Basis
Scorecard Draft != authoritative judgment
historical obligation satisfaction != current evidence eligibility
```

The principal reuse result is:

```text
Evaluation Occurrence ≈ bounded assessment/evaluation event
Evaluation Obligation ≈ scoped evaluation duty/responsibility
Rubric                ≈ scoring/evaluation rubric
Scorecard             ≈ one evaluator's scored evaluation record
```

The approximation symbol means familiar conceptual family, not equivalence to every application using those words.

# 2. Disposition summary

| MUDAC Concept | Primary familiar precedent | Disposition | Current-name decision | Main expectation-transfer constraint |
| --- | --- | --- | --- | --- |
| Evaluation Occurrence | assessment/evaluation event or occurrence | **SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS** | retain | event history must not own responsibility, judgment or automatic completion of work |
| Evaluation Obligation | obligation/duty/review assignment | **SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS** | retain | terminal responsibility history must not behave like a reopenable task/work item |
| Rubric | rubric/scoring guide/evaluation instrument | **SEMANTIC FIT / REUSE CANDIDATE** | retain | mutable working definition must remain distinct from exact authoritative Version used as Evaluation Basis |
| Scorecard | judge scorecard/evaluation response record | **SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS** | retain pending 014-F terminology audit | scorecard must not imply aggregate/final score, automatic submission, mutable post-finalization record or responsibility itself |

No Family-2 concept requires a new boundary or upstream reopen.

# 3. Evaluation Occurrence

## Current meaning

Evaluation Occurrence preserves one bounded historical evaluation event:

- supplied Subject;
- presented context;
- exact basis reference;
- starting evaluators and participant changes;
- timing;
- lifecycle/validity;
- optional replacement relationship.

Completion records that the bounded event ended. It does not prove all evaluator work was satisfied.

## Familiar precedents

Useful precedents include:

```text
assessment event
evaluation event
review occurrence
session
attempt
encounter
```

The strongest semantic fit is the generic idea of a **bounded evaluation event/occurrence**.

`Session`, `attempt` and `encounter` are useful analogies only.

## False-familiarity pressure

### Session

`Session` often imports runtime/login/meeting continuity, a single continuous interaction period, or temporary state that disappears when the session ends.

MUDAC requires durable historical truth even after the event ends.

### Attempt

`Attempt` often implies one actor trying to complete work and commonly owns success/failure or retry semantics.

Evaluation Occurrence can include multiple evaluators and does not own their individual responsibility or judgment completion.

### Encounter

The deprecated `Judging Encounter` demonstrated the exact overloading risk Phase 014 is meant to avoid. It accumulated presentation context, participants, responsibility and evaluation meaning behind one familiar-sounding event concept.

MUDAC now preserves:

```text
Evaluation Occurrence
  != Evaluation Obligation
  != Scorecard
  != Panel
```

## History/finality fit

Familiar event concepts often treat cancellation and invalidation loosely. MUDAC's distinction is semantically important:

```text
Cancelled  = intended occurrence stopped before meaningful qualifying use
Invalidated = occurrence happened but later became ineligible for intended authoritative use
Replacement = distinct successor occurrence
```

A familiar substitute is acceptable only if it does not erase this historical distinction.

## Disposition

**SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS — retain `Evaluation Occurrence`.**

The name is more explicit than `Session` or `Encounter`, but the reduced familiarity is useful because it prevents responsibility/judgment expectations from being imported accidentally.

No rename to `Judging Session`, `Attempt` or `Encounter` is adopted.

# 4. Evaluation Obligation

## Current meaning

Evaluation Obligation represents one evaluator's responsibility to produce one qualifying independent evaluation for a supplied Scope, Subject and Basis, optionally associated with one occurrence.

Its core lifecycle is:

```text
Outstanding
Satisfied
Excused
Cancelled
```

Terminal historical obligations are never silently reopened. Legitimate later responsibility uses a successor obligation.

## Familiar precedents

Useful precedents include:

```text
obligation
duty
review assignment
assignment
task
work item
```

`Obligation`/`duty` best transfer the semantic fact that responsibility exists independently of whether the evaluator has started a Scorecard.

`Assignment` is useful as explanatory language where it means responsibility allocation.

## False-familiarity pressure

Generic task/work-item systems often imply:

- arbitrary manual creation/closure;
- editable assignee identity in place;
- reopening a completed item;
- completion state identical to current usefulness of the produced artifact;
- deletion when work is cancelled;
- queue status as the source of truth.

Those expectations are incompatible with MUDAC.

Preserve:

```text
Satisfied obligation
  != currently eligible Scorecard evidence

terminal predecessor obligation
  != reopenable task

legitimate new responsibility
  → successor Evaluation Obligation
```

Reassignment likewise preserves predecessor/successor responsibility rather than silently changing evaluator identity.

## Why `Obligation` remains preferable to `Assignment`

`Evaluation Assignment` would be more colloquial but risks importing a mutable scheduler/task mental model. `Evaluation Obligation` more accurately communicates a responsibility with historical consequences.

The current name therefore carries a small learning cost in exchange for substantially safer expectation transfer.

## Disposition

**SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS — retain `Evaluation Obligation`.**

`Assignment`, `duty` and `task` remain explanatory analogies only. No generic Task/Work Item Concept is introduced.

# 5. Rubric

## Current meaning

Rubric defines the structured evaluation instrument and the semantics by which judgment responses are interpreted and validated.

It owns, among other things:

- criteria;
- response/score domains;
- scoring model;
- guidance/descriptors;
- contribution/weighting configuration;
- note policies;
- semantic validation/interpretation rules.

Rubric itself does not own authoritative Version lineage or evaluator judgment.

## Familiar precedent evidence

Educational assessment literature uses `rubric` consistently as a scoring/evaluation guide that makes criteria, performance expectations and rating levels explicit. Cornell's Center for Teaching Innovation describes a rubric as a scoring guide articulating components and expectations, while Carnegie Mellon's Eberly Center describes criteria, descriptors and performance levels.

That transfers directly useful expectations to MUDAC:

```text
criteria
+ response/performance levels
+ interpretation guidance
+ consistent evaluation semantics
```

## False-familiarity pressure

The main risk is not the word `Rubric`; it is **template/form mutability**.

Many applications let a current form/template be edited and then treat the latest version as implicitly governing all responses.

MUDAC explicitly requires:

```text
working/current Rubric definition
  != exact authoritative Rubric Version
  != Evaluation Basis already bound to historical work
```

A later semantic Rubric change does not reinterpret existing Occurrences, Obligations or Scorecards.

A second risk is treating Rubric as merely a list of numeric weights. MUDAC Rubric also owns response meaning, validation, guidance and note policy.

## Disposition

**SEMANTIC FIT / REUSE CANDIDATE — retain `Rubric`.**

This is the strongest Family-2 familiarity fit. `Scoring Guide` and `Evaluation Instrument` are useful explanatory synonyms but are less precise as the primary current concept name.

# 6. Scorecard

## Current meaning

Scorecard captures one evaluator's independent judgment for one Subject under one OccurrenceContext and exact EvaluationBasis.

Conceptually:

```text
Scorecard<Evaluator, Subject, OccurrenceContext, EvaluationBasis>
```

It owns one logical evaluation identity, working Draft, current authoritative judgment when established, Notes/responses and legitimate successor/amendment state.

## Familiar precedents

Useful precedents include:

```text
judge scorecard
score sheet
evaluation response
assessment record
ballot
submission
completed evaluation form
```

In judging/competition contexts, `Scorecard` transfers the useful idea of **one evaluator's recorded scoring/judgment**.

## False-familiarity pressure

### Aggregate/final-score interpretation

`Scorecard` in dashboards/business contexts can mean a summarized KPI/aggregate result. MUDAC Scorecard is not Aggregate, Rank, Panel mean or official outcome.

Where ambiguity matters, mapped language should make `Judge Scorecard` or equivalent subject-qualified meaning clear rather than changing the Concept identity prematurely.

### Submission interpretation

A `submission` model often implies that persistence or sending establishes authority.

MUDAC requires:

```text
Draft persisted
  != Draft complete
  != Finalized
  != authoritative Scorecard Version
  != Evaluation Obligation Satisfied
```

Only explicit successful Finalization through the current composition establishes authoritative judgment and satisfies responsibility.

### Ballot interpretation

`Ballot` is useful for independent-vote intuition but often implies a single irrevocable choice and does not naturally carry rich criteria, Notes, amendment lineage, source-faithful capture correction or exact Rubric basis.

### Editable-record interpretation

Finalized Scorecard authority is not a mutable row/form. Later legitimate Judge change uses amendment/successor authority, while structural identity error requires invalidation/replacement rather than rebinding Evaluator/Subject/Occurrence/Basis in place.

## One logical Scorecard

The familiar score-sheet metaphor must preserve:

```text
one Evaluation Obligation
  → at most one logical Scorecard

retry / device change / paper fallback / amendment
  != second evaluation weight
```

Paper and electronic paths are capture channels for the same judgment Concept.

## Disposition

**SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS — retain `Scorecard` pending 014-F terminology audit.**

The name is strong in the judging domain, but mapped experience should avoid unqualified `Scorecard` where users could reasonably read it as aggregate standings or a generic editable form.

# 7. Cross-concept familiarity result

The Family-2 concepts should not be collapsed into a common `Evaluation`, `Assignment`, `Form`, `Submission` or `Attempt` entity.

Reject conceptual shortcuts such as:

```text
Judging Session
  owns assignees
  owns form/template
  owns responses
  owns completion
```

or:

```text
Evaluation Assignment
  → opens one form
  → submit = complete
```

because they erase current distinctions:

```text
what happened        → Evaluation Occurrence
who owed work        → Evaluation Obligation
what governed it     → exact Rubric / Evaluation Basis
what Judge authored  → Scorecard
```

This separation is not conceptual bloat. Each Concept owns a distinct purpose, history and correction rule that familiar all-in-one workflow models would obscure.

# 8. Counterexample probes

## Probe A — Panel member never actually evaluates

A Panel member absent before occurrence begin should have neither occurrence participation nor obligation merely because the Panel grouping exists.

**Result:** confirms occurrence/responsibility independence.

## Probe B — Occurrence ends while Draft remains

Occurrence becomes Complete while one obligation remains Outstanding and the Scorecard remains Draft.

**Result:** rejects `session complete = task complete = submitted` familiarity.

## Probe C — finalized evidence later becomes ineligible

A Scorecard legitimately Finalized and satisfied its obligation, then its occurrence or basis later becomes ineligible.

**Result:** obligation remains historically Satisfied while current evidence eligibility changes; generic task reopening is incorrect.

## Probe D — Rubric successor after judging

A new Rubric Version becomes current after an occurrence was already bound to an earlier exact basis.

**Result:** familiar mutable-template semantics are rejected; historical work retains exact basis.

## Probe E — paper fallback after electronic Draft

A Judge has an electronic Draft, finishes on paper, and the paper source is legitimately verified/captured.

**Result:** one logical Scorecard/evaluation weight remains; channel changes do not create another submission.

## Probe F — amendment after Finalization

Judge legitimately changes judgment after initial Finalization.

**Result:** predecessor authority remains historical, successor authority is explicit, and the same logical Scorecard/obligation weight is preserved.

# 9. Upstream/current-authority check

014-D found **no current contradiction requiring repair**.

The canonical owners already agree that:

- occurrence completion is independent from responsibility completion;
- obligation satisfaction is historical and distinct from current evidence eligibility;
- exact Evaluation Basis is one authoritative Rubric Version;
- later Rubric changes never silently rebind historical work;
- one obligation maps to at most one logical Scorecard;
- Draft persistence/completeness is not authority;
- Finalization establishes authority/satisfaction through composition;
- retries/capture channels/amendments do not multiply evaluation weight;
- structural Scorecard identity is not ordinary editable content.

No Phase 010/011/012/013 reopen is required.

# 10. Familiarity risks carried to 014-F

Carry forward these terminology/expectation-transfer questions:

- whether mapped `Evaluation Occurrence` needs a more familiar user-facing explanatory label in some contexts without renaming the Concept;
- whether `Evaluation Obligation` should sometimes be explained as `assigned evaluation`/`evaluation responsibility` while preserving the obligation semantics;
- whether `Scorecard` should be qualified as `Judge Scorecard` where aggregate-score ambiguity exists;
- whether generic `Submit`, `Complete`, `Reopen`, `Edit`, `Task`, `Session`, `Attempt`, `Form` or `Assignment` labels would import wrong authority/finality/history semantics;
- whether `Rubric Version`, `Evaluation Basis` and current working Rubric remain sufficiently distinguishable in all mapped contexts.

These are cross-catalog terminology issues, not current Concept-boundary defects.

# 11. Broader-genericity questions carried to 014-G

014-D adopts no new genericity change, but records later probes:

- Evaluation Occurrence is already parameterized over Scope/Subject/Evaluator/PresentedContext/BasisRef; test whether the `Evaluation` qualifier is essential reusable meaning or MUDAC-specific wording.
- Evaluation Obligation is already generic over Scope/Evaluator/Subject/Basis/Occurrence/Evidence; test whether its model is reusable beyond judging without becoming an abstract Task super-concept.
- Rubric appears strongly reusable beyond MUDAC and already independent of Competition/Team/Judge internals.
- Scorecard is parameterized and potentially reusable for independent criterion-based judgments, but broader generalization must not turn it into a vague `Response`/`Record` concept.

# 12. Retained-novelty/catalog questions carried to 014-H

Potential reusable-knowledge candidates include:

- Evaluation Occurrence's separation of bounded historical event from responsibility/results;
- Evaluation Obligation's distinction between historical satisfaction and current evidence eligibility;
- Rubric's exact-basis binding and no-silent-reinterpretation rule;
- Scorecard's Draft-versus-authority distinction, fixed structural identity and one-logical-evaluation semantics.

Catalog candidacy is not decided here.

# 13. Risk disposition

014-D materially advances:

- **FRG-R01 Name-equals-fit** — familiar session/task/form/submission terms were tested behaviorally rather than accepted by name;
- **FRG-R03 False familiarity** — high-consequence finality/history/authority mismatches are explicit;
- **FRG-R06 Similarity merge** — occurrence, responsibility, basis and judgment remain separate despite workflow resemblance;
- **FRG-R09 Novelty without justification** — the less-colloquial `Occurrence`/`Obligation` names now have explicit rationale;
- **FRG-R13 Historical-adapter revival** — `Encounter` remains a negative precedent, not a restoration candidate.

No new blocking risk is introduced.

# 14. Implementation state

```text
architecture authority: SUSPENDED
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

Phase 014 remains design-only.

# Decision / handoff

**014-D COMPLETE — PASS.**

Proceed to **014-E — Versioning, Provenance, Award, Outcome Declaration, Export & Publication Familiarity/Reuse Audit**.