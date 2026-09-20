---
type: Phase Design Record
title: 015-D — Evaluation Occurrence, Obligation, Rubric, Scorecard & Judge-Authorship Integrity
description: "Audits Cluster B purpose preservation across Evaluation Occurrence truth, Evaluation Obligation responsibility, exact Rubric basis, one logical Scorecard, explicit Finalization, Judge authorship, paper/assisted capture and contextual Access, and dispositions DIR-005 plus DIR-010 through DIR-017."
status: stable
tags: [phase-015, integrity, evaluation-occurrence, evaluation-obligation, rubric, scorecard, judge-authorship, access]
sources:
  - resource: 015-A-integrity-audit-scope-interference-surfaces-whole-system-coverage-subphase-planning.md
  - resource: 015-B-purpose-preservation-baseline-integrity-inventory-directional-interference-register.md
  - resource: 015-C-competition-context-competitor-structure-identity-participation-alias-access-panel-integrity.md
  - resource: ../canonical/project/purpose-needs-success-tensions.md
  - resource: ../canonical/concepts/evaluation-occurrence.md
  - resource: ../canonical/concepts/evaluation-obligation.md
  - resource: ../canonical/concepts/rubric.md
  - resource: ../canonical/concepts/scorecard.md
  - resource: ../canonical/concepts/panel.md
  - resource: ../canonical/concepts/participation.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: ../canonical/experience/judge-evaluation.md
  - resource: ../canonical/experience/authority-lineage-correction.md
  - resource: ../canonical/invariants/judge-independence.md
  - resource: ../canonical/invariants/one-logical-scorecard.md
  - resource: ../canonical/invariants/missing-never-zero.md
  - resource: ../canonical/invariants/organizer-not-judge-author.md
  - resource: ../canonical/invariants/current-vs-historical-truth.md
  - resource: ../canonical/invariants/truthful-authority-under-uncertainty.md
---

# Purpose

Audit the Phase-015 evaluation truth chain:

```text
what happened
  → Evaluation Occurrence

who owed judgment
  → Evaluation Obligation

what semantics governed judgment
  → exact authoritative Rubric Version / Evaluation Basis

what the Judge authored
  → one logical Scorecard
```

The integrity question is whether these meanings remain independently truthful after begin/completion, reassignment, Draft work, Finalization, post-event continuation, capture-channel changes and current Access decisions are composed.

015-D dispositions:

- DIR-005 recheck from 015-C;
- DIR-010 through DIR-017 from 015-B.

# Decision

**015-D COMPLETE — PASS. Proceed to 015-E.**

```text
DIR-005 recheck                         CLOSED — PURPOSE PRESERVED
DIR-010 through DIR-017                 DISPOSITIONED
confirmed integrity violation           NONE
INT-F corrective finding opened         NONE
upstream semantic reopen                NONE
canonical semantic repair               NONE
purpose-preserved explicit limitations  2
cross-cluster rechecks retained         DIR-014 / 015 / 016 / 017
NEXT                                    015-E
```

Two explicit limitations remain intentional:

1. Evaluation responsibility may remain Outstanding and actionable after Evaluation Occurrence or live-event completion when the same responsibility remains legitimate and current Access permits it;
2. paper/assisted capture may use a non-Judge Actor while preserving the Judge as RepresentedAuthority and semantic author, but only when source evidence supports the Judge content without inference.

# 1. Purpose obligations exercised

015-D principally exercises:

- **P-01 — Independent human judgment**;
- **P-02 — Fair and bias-aware Team treatment**;
- **P-03 — Low-friction and accessible participation**;
- **P-04 — Live operational coordination and completion**;
- **P-05 — Resilient evaluation continuity**;
- **P-06 — Trustworthy and explainable outcome formation**;
- **P-07 — Correctable authority and historical truth**;
- **P-08 — Contextual confidentiality and authority separation**.

Material invariants:

```text
INV-001 Judge Independence
INV-002 One Logical Evaluation per Evaluation Obligation
INV-003 Missing Is Never Zero
INV-004 Organizer Does Not Become Judge Author
INV-005 Current vs Historical Truth
INV-008 Capture-Channel Parity
INV-010 Truthful Authority Under Uncertainty
```

# 2. Counterexample set

## D-P01 — Panel member never actually evaluates

Attempt:

> Because a Judge belongs to the Panel, they should already count as a participant/responsible evaluator.

Rejected.

```text
Panel membership
  → candidate grouping

EvaluationOccurrence.begin
  → confirmed actual starting evaluators
  + explicit obligations
```

No fictitious occurrence participant or obligation is created.

## D-P02 — Occurrence ends before a Judge finishes

Attempt:

> Complete occurrence means all obligations are complete.

Rejected.

```text
Occurrence = Complete
Obligation = Outstanding
Scorecard = absent or Draft
```

is valid.

## D-P03 — Obligation says Satisfied but Scorecard content is not authoritative

Attempt:

> Responsibility state should be allowed to establish judgment authority by itself.

Rejected.

Ordinary satisfaction is composition-only through confirmed Scorecard Finalization with authoritative Version/Provenance establishment.

## D-P04 — Draft becomes complete

Attempt:

> All required fields are complete, so evaluation should count.

Rejected.

```text
Draft complete
  != Finalized
  != authoritative Scorecard Version
  != obligation Satisfied
```

## D-P05 — New Rubric Version exists

Attempt:

> Judge's current Draft should automatically use the latest Rubric.

Rejected.

Existing occurrence/obligation/Scorecard remain bound to their exact earlier authoritative Rubric Version.

## D-P06 — Judge is replaced midway

Attempt:

> Replace evaluator identity inside the same Scorecard/obligation.

Rejected.

Structural identity is not editable successor content.

A true responsibility transfer uses predecessor/successor obligation semantics and the replacement evaluator's work is a distinct logical Scorecard where required.

## D-P07 — Organizer transcribes a paper Scorecard

Attempt:

> Organizer typed the responses, so Organizer is author.

Rejected.

```text
Actor = Organizer/capture actor
RepresentedAuthority = Judge
semantic author = Judge
Source = identified Judge-origin evidence
```

Ambiguous source/intent cannot be guessed.

## D-P08 — Event Completed, Judge still has a Draft

Attempt:

> Either discard the Draft because Participation completed or restore full Judge event authority.

Both are rejected.

Existing legitimate responsibility may remain narrowly actionable under policy and fresh Access.

# 3. DIR-005 recheck — Panel membership → Occurrence / Obligation

**Disposition: NO INTEGRITY VIOLATION — RECHECK CLOSED FOR CLUSTER B.**

015-C established that Panel is intended grouping only.

015-D confirms the downstream owners preserve the same seam:

```text
Panel members
  → candidate starting evaluators only

confirmed current evaluator facts
  → EvaluationOccurrence.begin

begin
  → actual participant history
  + one initial EvaluationObligation per qualifying responsible evaluator
```

The occurrence therefore preserves what actually happened rather than what planning intended.

The obligation preserves who actually owed judgment rather than who belonged to a reusable group.

# 4. DIR-010 — Evaluation Occurrence completion → Evaluation Obligation

**Disposition: PURPOSE PRESERVED WITH EXPLICIT LIMITATION.**

Occurrence purpose is bounded event truth.

Obligation purpose is responsibility.

Therefore:

```text
Occurrence Complete
  != obligation terminal
```

This is necessary rather than anomalous.

A Judge may still owe one evaluation after the bounded presentation/evaluation event ends.

Current design preserves:

- occurrence completion timing/history;
- Outstanding obligation truth;
- existing Draft/absent Scorecard truth;
- current Access as separate capability.

A completed occurrence does not Finalize a Scorecard, satisfy/excuse/cancel an obligation, or fabricate missing evidence.

The limitation is explicit: responsibility can outlive the bounded occurrence in which it arose.

# 5. DIR-011 — Evaluation Obligation lifecycle → Evaluation Occurrence

**Disposition: NO INTEGRITY VIOLATION.**

Obligation changes do not rewrite actual occurrence history.

```text
obligation Satisfied
obligation Excused
obligation Cancelled
successor obligation established
  != occurrence participant history rewrite
```

For participant changes, occurrence history is recorded explicitly and responsibility disposition is separately chosen.

A Judge can leave the physical/operational occurrence and still owe evaluation; or be excused; or be legitimately replaced.

Occurrence remains truthful regardless of responsibility outcome.

# 6. DIR-012 — Evaluation Obligation status → Scorecard

**Disposition: NO INTEGRITY VIOLATION.**

Responsibility and judgment authority remain distinct.

```text
Outstanding
  != Scorecard Draft necessarily exists

Satisfied
  != Scorecard owns responsibility

Excused / Cancelled
  != zero Scorecard
  != fabricated evidence
```

Ordinary initial satisfaction requires authoritative Finalization composition, but the obligation does not define response content or Scorecard authority itself.

Historical satisfaction later remains distinct from current evidence eligibility.

That later temporal dimension is rechecked in 015-E.

# 7. DIR-013 — Scorecard Finalization → Evaluation Obligation

**Disposition: NO INTEGRITY VIOLATION.**

Finalize Evaluation is a coordinated semantic action, but its owners remain independent.

Conditions require:

- intended Outstanding obligation;
- one logical Scorecard for that obligation;
- structural identity matching responsibility;
- exact bound Rubric Version;
- valid/completed responses;
- explicit Judge finalization intent or legitimate represented-authority capture path;
- current Access/authority;
- no existing initial authoritative Scorecard;
- obligation not already terminal by another legitimate path.

Semantic success requires:

```text
authoritative Scorecard established
+ one immutable current Scorecard Version
+ meaningful Provenance
+ intended EvaluationObligation.satisfy
+ EvidenceRef = logical Scorecard
+ one evaluation weight
```

This prevents:

- satisfying the wrong obligation;
- counting repeated Finalization as additional weight;
- treating persistence/completeness as commitment;
- allowing obligation state to manufacture Scorecard authority.

INV-002 remains preserved.

# 8. DIR-014 — Rubric current definition → historical Scorecard / Occurrence

**Disposition: NO INTEGRITY VIOLATION IN CLUSTER B; REQUIRED 015-E RECHECK RETAINED.**

Evaluation Basis is explicitly:

> the exact authoritative Rubric Version selected for the evaluation.

That exact basis flows through:

```text
Evaluation Occurrence BasisRef
  → Evaluation Obligation Basis
  → Scorecard EvaluationBasis
```

A later Rubric Version does not silently rebind:

- existing occurrences;
- obligations;
- Scorecard Drafts;
- finalized judgments.

This preserves Rubric's interpretation purpose and Scorecard's fixed-basis judgment purpose.

015-E must recheck supersession/invalidation and historical authority.

# 9. DIR-015 — reassignment/substitution → Scorecard authorship

**Disposition: NO INTEGRITY VIOLATION IN ORDINARY EVALUATION; REQUIRED 015-E RECHECK RETAINED.**

Current composition never changes Evaluator identity in place simply to make substitution operationally convenient.

For a true substitution:

```text
occurrence participant adjustment
+ predecessor responsibility disposition
+ successor responsibility
→ replacement evaluator performs their own qualifying work
```

Scorecard structural identity includes:

```text
Evaluator
Subject
OccurrenceContext
EvaluationBasis
```

These cannot be changed by ordinary amendment/capture correction.

Therefore replacement responsibility cannot silently inherit another Judge's authorship.

015-E must recheck structural invalidation/successor-work history.

# 10. DIR-016 — paper/assisted capture → Scorecard authorship

**Disposition: PURPOSE PRESERVED WITH EXPLICIT LIMITATION.**

Paper/electronic/assisted capture are channels for the same evaluation semantics.

The Judge remains semantic author when the source unambiguously represents the Judge's content.

```text
Actor
  may be Organizer/capture/verification actor

RepresentedAuthority
  = Judge

semantic author
  = Judge
```

The limitation is strict:

- the source must be identifiable;
- structural binding must be resolvable;
- Judge content must be supported by source;
- ambiguous intent stays ambiguous;
- capture actor cannot infer missing answers or Finalization intent.

Before source verification/finalization, transcription remains non-authoritative.

This preserves INV-004 and INV-008.

015-E rechecks source-faithful correction versus Judge semantic amendment.
015-I rechecks paper/degraded representation.

# 11. DIR-017 — Access change → existing Scorecard work

**Disposition: PURPOSE PRESERVED WITH EXPLICIT CAPABILITY SEPARATION; TEMPORAL RECHECK RETAINED.**

An Evaluation Obligation can remain Outstanding while current Access denies work.

```text
responsibility exists
  != capability currently permitted
```

Conversely, current Access cannot create responsibility.

For ordinary work:

```text
Outstanding obligation
+ legitimate fixed bindings
+ current Access
→ Start/resume/finalize same logical Scorecard
```

At Event Completed, the same narrow rule from 015-C applies.

History inspection may also remain available under separately permitted Access without restoring work authority.

Thus Access can limit current capability without rewriting obligation/Scorecard history.

This is an intentional composition boundary, not an integrity defect.

015-E rechecks retained Version/Provenance history after current Access ends.

# 12. One-logical-evaluation integrity

Cluster B preserves:

```text
one Evaluation Obligation
  → at most one logical Scorecard
```

The following do not multiply evaluation weight:

- repeated Start Evaluation;
- reload/device change;
- Draft traces;
- paper fallback;
- transcription;
- retry;
- amendment;
- capture correction.

A later legitimate re-evaluation after unusable prior evidence uses a successor obligation and a new logical Scorecard rather than duplicating weight under the predecessor.

Temporal details move to 015-E.

# 13. Missing / zero / not-applicable integrity

Rubric owns response semantics.

Scorecard records responses under that exact basis.

Obligation/occurrence state never fabricates a numeric value.

```text
Outstanding with no Scorecard
  = missing evaluation

Draft response missing
  != zero

Rubric-defined zero
  = actual response only when Judge/source supplied it
```

Excusing/cancelling obligation also does not create zero evidence.

INV-003 remains preserved.

# 14. Judge-independence integrity

Evaluation work composes with Access/disclosure while preserving Judge independence.

Ordinary judging permits the Judge's own evaluation work but withholds peer judgment/outcome signals such as:

- peer Scorecards/Notes;
- Panel mean;
- Coverage;
- Aggregate;
- Rank;
- standings.

Finalizing one's own Scorecard does not unlock these signals.

The Evaluation Occurrence, Obligation, Rubric or Scorecard concepts therefore do not accidentally acquire peer-result disclosure semantics.

# 15. Finalization-under-uncertainty integrity

Current mapping preserves:

```text
Draft preserved
!= Finalize in progress / authority unknown
!= confirmed authoritative Finalization
!= known rejected/failed attempt
```

Unknown persistence/authority cannot be promoted into:

- authoritative Scorecard;
- Satisfied obligation;
- confirmed evaluation weight.

Retry/resume must converge on the same logical evaluation conceptually.

Runtime retry/transaction realization remains outside Phase 015.

# 16. Subject-purpose integrity summary

| Subject | Integrity result |
| --- | --- |
| Evaluation Occurrence | Purpose preserved; occurrence completion/participant history remain independent from responsibility/judgment |
| Evaluation Obligation | Purpose preserved with explicit possibility that responsibility outlives occurrence/current capability |
| Rubric | Purpose preserved; exact Version semantics remain authoritative for bound evaluation |
| Scorecard | Purpose preserved; one logical Judge-authored judgment retains Draft/authority and fixed structural identity |
| Panel | Recheck closed; intended grouping does not become actual evaluation truth |
| Participation | 015-C limitation composes correctly; Completed participation can remain attributable context without reactivation |
| Access | Purpose preserved; permission gates current operations without creating responsibility/authorship |
| Judge authorship | Preserved across electronic, paper and assisted capture when source/represented-authority conditions are satisfied |

# 17. Material finding result

015-D opens no corrective INT-F finding.

```text
INT-F corrective findings opened in 015-D = 0
```

Reason:

- DIR-005 and DIR-010 through DIR-017 are compatible with the retained purposes;
- responsibility/capability/judgment/authority/eligibility remain separate;
- no current action silently creates duplicate evaluation weight;
- no current substitution/capture path transfers Judge authorship;
- exact basis remains stable;
- no mapping claims occurrence completion or Draft completeness equals Finalization.

# 18. Cross-cluster carry/recheck

The following are later rechecks, not unresolved Cluster-B defects:

- DIR-014 → 015-E: Rubric Version supersession/invalidation and historical authority;
- DIR-015 → 015-E: structural misbinding, invalidation and successor responsibility;
- DIR-016 → 015-E and 015-I: source-faithful correction and paper/degraded mapping;
- DIR-017 → 015-E: retained Version/Provenance/history after current capability changes.

015-E also owns DIR-018 through DIR-025 and can reopen a Cluster-B conclusion if temporal composition exposes a genuine purpose violation.

# 19. Implementation boundary

015-D does not prescribe:

- autosave implementation;
- offline database shape;
- synchronization transactions;
- locking/CAS;
- client/server retry mechanics;
- authorization middleware;
- device/session architecture;
- paper-scanning/OCR implementation;
- UI layouts or controls.

```text
semantic Finalization
  != database commit design

same logical Scorecard
  != storage key design

fresh Access
  != middleware architecture

paper capture parity
  != scanner/transcription technology
```

# Exit

**015-D COMPLETE — PASS.**

No semantic correction or upstream reopen is required.

Proceed to **015-E — Versioning, Provenance, Temporal Correction, Successor Work & Historical-Truth Integrity**.
