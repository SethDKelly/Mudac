---
type: Concept Composition Revalidation
title: 011-E — Evaluation Basis, Scorecard Authority, Versioning/Provenance & Paper-Capture Composition
description: "Establishes current MUDAC composition semantics for authoritative Rubric basis establishment, one logical Scorecard per Evaluation Obligation, Scorecard finalization/amendment authority, Versioning/Provenance participation, obligation satisfaction, and paper/electronic capture convergence without transferring Judge authorship."
status: stable
tags: [phase-011, composition, synchronization, rubric, scorecard, versioning, provenance, paper, authority]
sources:
  - resource: 011-A-composition-scope-evidence-reuse-synchronization-risk-subphase-planning.md
  - resource: 011-B-legacy-synchronization-inventory-composition-obligation-map-application-action-baseline.md
  - resource: 011-C-competition-lifecycle-identity-participation-access-operating-context-composition.md
  - resource: 011-D-team-division-alias-panel-evaluation-occurrence-evaluation-obligation-establishment.md
  - resource: ../canonical/concepts/rubric.md
  - resource: ../canonical/concepts/scorecard.md
  - resource: ../canonical/concepts/versioning.md
  - resource: ../canonical/concepts/provenance.md
  - resource: ../canonical/concepts/evaluation-obligation.md
  - resource: ../canonical/concepts/evaluation-occurrence.md
  - resource: ../canonical/mechanisms/criterion-notes.md
  - resource: ../canonical/policies/evaluation-policy.md
  - resource: ../canonical/policies/continuity-paper.md
  - resource: ../canonical/policies/correction-authority.md
  - resource: ../canonical/invariants/judge-independence.md
  - resource: ../canonical/invariants/one-logical-scorecard.md
  - resource: ../canonical/invariants/organizer-not-judge-author.md
  - resource: ../canonical/invariants/capture-channel-parity.md
  - resource: ../canonical/invariants/truthful-authority-under-uncertainty.md
  - resource: ../002-concept-specification/002-D-rubric-criterion-scorecard-notes-specifications.md
  - resource: ../002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md
  - resource: ../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../007-design-refinement/007-C-cross-concept-synchronization-completeness-authority-seam-audit.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/005/composition-synchronization-contract.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T11:58:00-05:00 }
---

# Purpose

Establish the current MUDAC composition by which an already-existing evaluation responsibility becomes one Judge-authored authoritative evaluation under one exact evaluation basis, while preserving immutable authority history, meaningful provenance and capture-channel parity.

011-D already established that an Evaluation Occurrence may be Complete while one or more Evaluation Obligations remain Outstanding. 011-E therefore begins from a responsibility that already exists and answers:

1. What exact state counts as the evaluation basis?
2. How is an authoritative Rubric basis established without making Versioning or Provenance own Rubric semantics?
3. How does one Outstanding Evaluation Obligation resolve to at most one logical Scorecard?
4. What must be true for Scorecard Finalization to establish authoritative evaluation evidence and satisfy the obligation?
5. How do legitimate Judge amendments preserve one logical vote while creating successor authoritative Scorecard state?
6. How do paper, assisted and electronic capture paths converge without changing semantic authorship, evaluation meaning or weight?
7. Which Versioning and Provenance actions are composition-only rather than generic MUDAC application actions?

011-E owns:

- legacy synchronization 07 — Rubric authoritative establishment;
- the Scorecard/basis half of legacy synchronization 08;
- the authority-establishment / Versioning / Provenance / obligation-satisfaction portion of legacy synchronization 09;
- legacy synchronization 10 — paper capture verification;
- CO-05, CO-06's ordinary authority-establishment portion, and CO-07;
- CG-02 — qualifying finalized Scorecard satisfies the intended Evaluation Obligation;
- the 011-B action-surface decisions for Rubric, Scorecard, Versioning, Provenance, Evaluation Obligation `satisfy`, and paper-capture application actions.

011-E does **not** own:

- invalidation of a Rubric/Scorecard Version or Evaluation Occurrence;
- structural correction or replacement;
- successor Evaluation Obligation creation after evidence becomes unusable;
- post-authority paper transcription correction;
- Coverage/Aggregate/Rank recalculation;
- Competition Finalization or Outcome Declaration;
- Export/Publication;
- UI controls, signatures, QR mechanics, scanning, storage or runtime transaction design.

Those concerns remain with 011-F/G/H or later mapping/engineering work.

# Decision summary

**PASS — 011-E is complete.**

The existing Concept set is sufficient. No `Evaluation Basis`, `Evaluation Submission`, `Paper Scorecard`, `Capture Verification`, `Vote`, `Commit`, or generic workflow Concept is required.

The key current decisions are:

1. For current MUDAC judging, the exact authoritative **Rubric Version** is the Evaluation Basis supplied to Evaluation Occurrence, Evaluation Obligation and Scorecard.
2. Rubric working state becomes authoritative only through application composition of Rubric validity/preparation with Versioning and Provenance. `Rubric.prepareForUse` alone is not authoritative publication.
3. A later authoritative Rubric Version governs only uses to which it is subsequently bound. It never silently rebinds an already-prepared/begun Evaluation Occurrence, existing Evaluation Obligation, Scorecard Draft or historical authoritative Scorecard.
4. An Outstanding Evaluation Obligation may resolve/start **at most one logical Scorecard**. Repeated start intent resolves the same logical Scorecard rather than creating another evaluation.
5. Scorecard Draft work is non-authoritative and does not create Versioning or authority Provenance for every edit.
6. Successful initial Finalization is one conceptual authority-establishing application action whose required postconditions are: the Scorecard is authoritative; one immutable initial Scorecard Version is current/eligible; meaningful Provenance explains author/actor/source; and the intended Evaluation Obligation is Satisfied.
7. The Satisfied Evaluation Obligation's `EvidenceRef` binds to the **logical Scorecard identity**, not one particular Scorecard Version. Versioning separately identifies the Scorecard's current eligible authoritative snapshot.
8. A legitimate Judge amendment produces a successor authoritative Scorecard Version with Provenance while the same Evaluation Obligation remains Satisfied by the same logical Scorecard. Amendment never creates another vote or responsibility.
9. Paper/electronic/assisted capture paths converge on the same logical Scorecard. Capture actor may differ from semantic author, but the Judge remains RepresentedAuthority/evaluator.
10. Organizer paper verification may establish captured authority only when the identified physical source unambiguously represents the Judge's completed/committed evaluation. The Organizer may not infer missing or ambiguous Judge judgment or finalization intent.
11. A paper transcription remains non-authoritative until verified against its identified source. After authority exists, a discovered transcription mismatch is 011-F correction work rather than ordinary 011-E finalization.
12. Generic Versioning and Provenance actions remain composition-only; they are not standalone admin controls merely because the Concepts expose them.

Durable current rules are promoted to [Evaluation Basis, Scorecard Authority & Capture Composition](../canonical/synchronizations/evaluation-basis-scorecard-authority.md).

# 1. Authority model

011-E preserves five independently owned meanings:

```text
Rubric
  = evaluation instrument semantics

Versioning<Rubric>
  = immutable authoritative Rubric snapshots and currentness

Scorecard
  = one evaluator's logical judgment

Versioning<Scorecard>
  = immutable authoritative Scorecard snapshots and currentness

Provenance
  = who acted / whose authority-content is represented / source / reason / timing

Evaluation Obligation
  = responsibility to produce one qualifying independent evaluation
```

No owner above can impersonate another.

In particular:

```text
Rubric prepared for use
    != authoritative Rubric Version

Scorecard Draft complete
    != authoritative Scorecard

Version committed
    != semantic authorship transfer

Organizer capture
    != Organizer judgment

Evaluation Obligation satisfied
    != Evaluation Obligation owns Scorecard content
```

# 2. Establishing an authoritative evaluation basis

## 2.1 Working Rubric versus authoritative Rubric basis

Rubric owns working-definition semantics and validation. Draft editing, validation and `prepareForUse` remain Rubric actions.

A working Rubric becomes a MUDAC authoritative evaluation basis only when the application establishes an immutable Version of the complete prepared Rubric definition and records meaningful Provenance for that establishment.

Application action: **Establish Authoritative Rubric Version**.

Participants:

- `Rubric.prepareForUse` when needed to establish that the working definition is valid/prepared;
- `Versioning.initializeLineage` + `commitInitialVersion` for first authority in a Rubric lineage, or `commitSuccessor(expectedCurrent, snapshot)` for a later authoritative definition;
- `Provenance.record` for the authority-establishment event.

The authoritative Rubric snapshot must contain enough complete Rubric semantics to reconstruct response validation and scoring interpretation exactly. A version number/identity alone is not the semantics.

## 2.2 Preconditions

Ordinary establishment requires:

- the working Rubric definition is internally valid under Rubric semantics;
- scoring/response/note semantics are complete enough for the intended use;
- the acting configuration authority is legitimate under current Access/context;
- the lineage/application context is unambiguous;
- a successor commit is based on the actual expected current eligible Rubric Version;
- the resulting authoritative state is attributable through Provenance.

## 2.3 Postconditions

Successful establishment yields:

- one immutable authoritative Rubric Version in the lineage;
- at most one current eligible authoritative Rubric Version for that linear lineage;
- a Provenance record identifying the meaningful acting/represented authority and source/reason where material;
- no mutation of historical Scorecards or occurrences that used an earlier Rubric Version.

Rubric itself still owns the meaning of the evaluation instrument. Versioning does not reinterpret criteria/responses.

## 2.4 BasisRef in current MUDAC

For the current MUDAC judging model:

> **Evaluation Basis = exact authoritative Rubric Version identity/snapshot selected for the occurrence/responsibility.**

Evaluation Policy may govern whether Rubric Versions are compatible for downstream aggregation and may constrain applicability, but it does not silently change the response semantics of a Scorecard already bound to one exact Rubric Version.

When 011-D prepares an Evaluation Occurrence, its `BasisRef` therefore resolves one exact eligible authoritative Rubric Version for that occurrence.

## 2.5 No silent rebinding

A later Rubric Version does not rebind:

- a Prepared/Open/Complete Evaluation Occurrence;
- an existing Evaluation Obligation;
- a Scorecard Draft;
- a finalized historical Scorecard.

If a newer Rubric is intended before an occurrence begins, the occurrence may be cancelled/reprepared under the legitimate new basis rather than mutating its snapshot in place.

If an already-bound Rubric Version becomes **invalid** rather than merely superseded, ordinary authority consequences belong to 011-F.

# 3. Resolving one logical Scorecard from one obligation

## 3.1 Scorecard identity arises after responsibility

011-D deliberately establishes responsibility before Scorecard work begins.

Application action: **Start Evaluation**.

Primary participant:

- `Scorecard.start`.

Composition resolves or creates one logical Scorecard for the target Evaluation Obligation using structural bindings:

```text
Evaluator         = obligation Evaluator
Subject           = obligation Subject
OccurrenceContext = obligation OccurrenceRef / supplied occurrence context
EvaluationBasis   = obligation Basis / occurrence BasisRef
```

The Scorecard must not allow the evaluator/capture actor to arbitrarily choose a different Team, occurrence or Rubric Version for an already-established obligation.

## 3.2 Preconditions

Ordinary start requires:

- the Evaluation Obligation is Outstanding;
- current Access permits the Judge-authored evaluation operation under the correct Participation context;
- the structural bindings are resolvable and mutually consistent;
- the Evaluation Basis remains legitimate for this obligation;
- no distinct logical Scorecard already exists for the same responsibility.

An occurrence does **not** have to remain Open merely for the Judge to finish an existing responsibility. Because 011-D allows `completeOccurrence` while obligations remain Outstanding, Scorecard work may continue after occurrence completion when current Competition/Access policy legitimately permits it.

Likewise Event Completed may close ordinary Judge capability under 011-C; if work must continue afterward, current Access/policy must explicitly permit that circumstance rather than 011-E bypassing Access.

## 3.3 Duplicate start intent

Repeated semantic intent to start/resume work for the same obligation resolves the same logical Scorecard.

Conceptually:

```text
one Evaluation Obligation
        ↓
at most one logical Scorecard
```

This is the application realization of INV-002. It does not prescribe a database key, idempotency token or transaction design.

# 4. Draft work remains non-authoritative

Once started, ordinary Judge Draft actions remain Scorecard-owned:

- set/clear Criterion responses;
- set/clear Criterion Notes;
- set/clear overall Note.

Rubric Version semantics validate responses and completed-response requirements.

Draft edits do **not**:

- satisfy the Evaluation Obligation;
- create authoritative Scorecard Versions;
- cause every edit to become domain Provenance;
- contribute to Coverage/Aggregate/Rank;
- expose peer evaluation signals.

Draft completeness is still not authority under SC-001.

# 5. Initial Scorecard Finalization

## 5.1 Application action

Application action: **Finalize Evaluation**.

Concept participants:

- `Scorecard.finalize`;
- Scorecard `Versioning.initializeLineage` + `commitInitialVersion`;
- `Provenance.record`;
- `EvaluationObligation.satisfy`.

This is a conceptual **authority-establishing synchronization**. It does not imply one implementation transaction or service.

## 5.2 Preconditions

Ordinary finalization requires:

- the target logical Scorecard belongs to the intended Outstanding Evaluation Obligation;
- Scorecard Evaluator matches obligation Evaluator;
- Subject, OccurrenceContext and EvaluationBasis match the established responsibility/context;
- Rubric validation confirms all required responses/Notes are complete and semantically valid under the exact bound Rubric Version;
- the Judge's semantic finalization intent is explicit through the applicable capture path;
- current Access permits the action or legitimate represented-authority capture path;
- no authoritative Scorecard Version already exists for ordinary first Finalization;
- the obligation has not already been Satisfied/Excused/Cancelled through another legitimate resolution;
- the bound basis/evidence path has not become ineligible under a condition that 011-F must resolve.

## 5.3 Required postconditions

The application action is semantically successful only when all of these truths are established:

1. the logical Scorecard has current authoritative judgment state;
2. Versioning has one current eligible immutable initial Scorecard snapshot matching that authoritative state;
3. Provenance can explain the establishment, including semantic author, acting/capture actor when different, source/channel and meaningful timing/reason facts;
4. the intended Evaluation Obligation is `Satisfied`;
5. the obligation's `EvidenceRef` identifies the **logical Scorecard**, not a particular Version;
6. no second evaluation weight has been created.

Derived Coverage/Aggregate/Rank effects are not part of 011-E's authority-establishing postcondition; 011-G owns them.

## 5.4 Why EvidenceRef is the logical Scorecard

Binding `EvidenceRef` to one immutable Scorecard Version would create a problem on legitimate amendment: the Evaluation Obligation Concept has no reason to reopen or rewrite responsibility merely because the same Judge corrected the same logical evaluation.

MUDAC therefore binds:

```text
Evaluation Obligation.EvidenceRef
        = logical Scorecard identity
```

and separately uses Versioning to answer:

```text
which immutable Scorecard snapshot is current eligible authority?
```

This preserves both truths:

- the responsibility was satisfied by one logical evaluation;
- that logical evaluation may have successive authoritative states.

# 6. Legitimate Judge amendment

## 6.1 Beginning amendment

`Scorecard.beginAmendment` creates an Amendment Draft from the current authoritative Scorecard state while the predecessor remains authoritative under SC-002.

Ordinary amendment remains available only under legitimate Judge/authority/access policy. Organizer process authority cannot become Judge authorship.

## 6.2 Finalizing amendment

Application action: **Finalize Judge Amendment**.

Participants:

- `Scorecard.finalizeAmendment`;
- `Versioning.commitSuccessor(expectedCurrent, snapshot)` for the same Scorecard lineage;
- `Provenance.record`.

The already-Satisfied Evaluation Obligation does **not** call `satisfy` again and does not receive a new responsibility identity.

Postconditions:

- the new Scorecard Version becomes current eligible authority;
- the predecessor Version remains immutable historical authority and becomes Superseded;
- Provenance identifies the amendment as Judge-authored and records meaningful reason/source facts where required;
- the same logical Scorecard remains the one evidence identity satisfying the obligation;
- evaluation weight remains one.

A stale amendment based on a no-longer-current Scorecard Version cannot silently establish another current successor. The actor must reconcile/review current authority before a later legitimate amendment is finalized.

## 6.3 Amendment boundary

Ordinary amendment changes evaluator-authored response/note content only.

It cannot silently change:

- Evaluator;
- Subject;
- OccurrenceContext;
- EvaluationBasis.

Structural error, occurrence invalidation, Version invalidation, post-authority transcription error and replacement/successor responsibility belong to 011-F.

# 7. Versioning and Provenance remain independent supporting Concepts

## 7.1 Versioning role

Versioning answers:

- what immutable authoritative Rubric/Scorecard states existed;
- which committed Version is currently eligible;
- which Version superseded which predecessor;
- whether a Version was later invalidated.

It does not decide:

- whether Rubric content is valid;
- whether a Judge intended to finalize;
- whether a correction is legitimate;
- who authored judgment content.

## 7.2 Provenance role

Provenance answers:

- who performed the meaningful action;
- whose semantic authority/content the result represents;
- what source/channel supplied the evidence;
- why the action occurred when material;
- which prior/resulting authoritative states are related;
- effective/occurrence time versus later capture/verification time where meaningful.

It does not create the Scorecard judgment or Version itself.

## 7.3 Generic action exposure

`Versioning.initializeLineage`, `commitInitialVersion`, `commitSuccessor`, `invalidateVersion` and `Provenance.record` are not generic direct MUDAC admin actions.

They participate through purpose-specific application actions. Invalidation remains 011-F work.

# 8. Paper / assisted capture composition

## 8.1 One evaluation model, multiple capture channels

Paper is not a separate judgment Concept.

The logical identity remains:

```text
Evaluation Obligation
        ↓
one logical Scorecard
        ↓
current authoritative Scorecard Version
```

Capture channel affects Provenance and operational continuity, not evaluator identity, Evaluation Basis or evaluation weight.

## 8.2 Paper source identity

A paper-origin evaluation accepted into capture must be traceable to one identified physical source and unambiguous evaluation context.

Before authority can be established, the application must resolve at least:

- the intended Evaluation Obligation / Judge Participation;
- Evaluation Occurrence/context;
- Subject;
- exact Rubric Version / Evaluation Basis;
- unique paper-source reference sufficient to avoid indistinguishable duplicate sources.

A QR/barcode may encode references, but possession/scanning is not authority.

## 8.3 Capture is initially Draft

Application action: **Capture Paper Evaluation**.

The Organizer/capture actor may enter the Judge's paper-recorded responses into the same logical Scorecard Draft associated with the responsibility.

Before verification/finalization:

- the captured digital state is non-authoritative;
- the Evaluation Obligation remains Outstanding;
- no Scorecard Version exists merely because transcription is complete;
- Organizer capture does not make the Organizer evaluator/author.

Draft transcription errors may be corrected before authority establishment without creating authoritative correction history because the digital capture has not yet become authoritative.

## 8.4 Verification requires source fidelity and Judge commit intent

Application action: **Verify & Finalize Paper Evaluation**.

The capture path may establish authority only when:

- the physical source identity/context is unambiguous;
- captured content has been explicitly checked against the source;
- the source is sufficiently legible/unambiguous to establish what the Judge recorded;
- the paper procedure/source provides unambiguous evidence that the Judge completed/committed the evaluation for authoritative use;
- Rubric validation succeeds under the exact bound Rubric Version;
- the same logical Scorecard/obligation has not already been authoritatively satisfied by another path;
- the acting Organizer has legitimate capture/verification capability.

The exact physical representation of Judge commit intent—signature, marked completion field, controlled collection procedure or other equivalent mapping—is Phase 013/operational design. 011-E requires only that semantic intent not be invented by the Organizer.

## 8.5 Paper authority-establishment participants

Successful verified paper finalization establishes the **same** semantic postconditions as electronic Finalization:

- `Scorecard.finalize` represents the Judge-authored completed evaluation;
- Versioning commits the initial immutable authoritative Scorecard snapshot;
- Provenance records:
  - Actor = Organizer/capture verifier where appropriate;
  - RepresentedAuthority / semantic author = Judge;
  - Source = identified paper source;
  - capture/verification time distinct from occurrence/Judge-authorship time where material;
- `EvaluationObligation.satisfy` binds the responsibility to the logical Scorecard.

The Organizer's ability to perform capture/verification does not authorize changing the Judge's responses or filling ambiguity.

## 8.6 Mixed electronic + paper convergence

If an electronic Draft already exists for the same obligation and paper fallback is used, both traces converge on the same logical Scorecard.

They do **not** create:

- two Scorecards;
- two Evaluation Obligations;
- two votes;
- automatic merging of conflicting judgment content.

If no authoritative version yet exists, the verified source that legitimately establishes final Judge intent may provide the content for the one authoritative Scorecard.

If an authoritative Scorecard already exists and a later paper/electronic source conflicts materially, 011-E does not silently supersede it. The conflict enters 011-F correction/invalidation authority rather than creating a second current evaluation.

Duplicate capture of the same physical source similarly resolves the same logical Scorecard/source provenance rather than another vote.

# 9. Truth under uncertain authority establishment

The application must distinguish:

- Draft saved/captured;
- Finalization requested;
- authoritative Finalization confirmed;
- outcome uncertain.

MUDAC must not claim `Finalized`/`Satisfied` if it cannot establish whether the authority-establishing postconditions hold.

A repeated semantic intent must reconcile against the current logical Scorecard, Versioning and Evaluation Obligation state before another authority effect can occur.

This is a conceptual convergence/truthfulness requirement under INV-010, not a prescribed retry/idempotency/transaction mechanism.

# 10. Current application-action surface for this family

| Application / Concept action | Current MUDAC status |
| --- | --- |
| Rubric `createDraft` and ordinary edit/configuration actions | direct |
| Rubric `validateDefinition`, `prepareForUse` | direct preparation actions; not authority by themselves |
| Establish Authoritative Rubric Version | coordinated authority-establishing application action |
| Versioning `initializeLineage`, `commitInitialVersion`, `commitSuccessor` | composition-only participants |
| Versioning `invalidateVersion` | deferred to 011-F; not generic direct action |
| Provenance `record` | composition-only participant |
| Scorecard `start` | direct Judge application action gated/bound by Outstanding obligation |
| Scorecard Draft edit actions | direct Judge actions |
| Scorecard `finalize` | coordinated authority-establishing application action |
| Evaluation Obligation `satisfy` | composition-only participant in successful initial Finalization |
| Scorecard `beginAmendment`, `abandonAmendment` | direct/controlled Judge actions under amendment policy |
| Scorecard `finalizeAmendment` | coordinated authority-establishing successor action |
| Capture Paper Evaluation | direct Organizer operational action producing non-authoritative Draft capture |
| Verify & Finalize Paper Evaluation | coordinated authority-establishing capture action; Judge remains author |
| post-authority paper transcription correction | deferred to 011-F |

# 11. Legacy synchronization disposition after 011-E

## Legacy 07 — Rubric authoritative establishment

**REVALIDATED / REPLACED BY CURRENT OWNER.**

The reusable core survives: Rubric validity + Versioning + Provenance establishes authoritative evaluation basis. Current semantics now explicitly distinguish `prepareForUse` from authoritative Version establishment and bind occurrence/obligation/Scorecard to one exact Rubric Version.

## Legacy 08 — occurrence/basis → Scorecard obligation

**FULLY REPLACED ACROSS 011-D + 011-E.**

011-D now owns responsibility establishment at occurrence begin. 011-E separately owns logical Scorecard resolution/start from that already-existing obligation. Scorecard creation no longer implies responsibility creation.

## Legacy 09 — Scorecard Finalization/Amendment

**AUTHORITY-ESTABLISHMENT PORTION REPLACED.**

011-E now separates:

- Scorecard semantic Finalization;
- immutable Version authority;
- meaningful Provenance;
- Evaluation Obligation satisfaction;
- amendment successor authority.

Invalidation/successor-work effects remain 011-F and derived refresh remains 011-G.

## Legacy 10 — paper capture verification

**REVALIDATED / REPLACED BY CURRENT OWNER.**

Paper/electronic capture now converges on the same logical Scorecard tied to the explicit Evaluation Obligation. Judge authorship, capture actor, physical source and verification are explicitly separated through Provenance.

# 12. Boundary / missing-Concept audit

011-E does not expose a missing Concept.

Rejected promotions:

- **Evaluation Basis** — current MUDAC only requires an exact authoritative Rubric Version reference plus application applicability rules; no independent lifecycle/purpose is missing.
- **Evaluation Submission** — Finalization is Scorecard behavior plus composition, not another source-of-truth object.
- **Paper Scorecard** — capture channel does not change logical judgment purpose/state.
- **Capture Verification** — verification is an application-level authority condition/action with Provenance, not a reusable stateful Concept with independent purpose.
- **Vote** — Evaluation Obligation + Scorecard + eligibility/derived mechanisms already express responsibility, judgment and weight without collapsing them.
- **Audit Event** — Provenance already owns meaningful authority history; low-level telemetry remains outside Concept Design.

No Rubric, Scorecard, Versioning, Provenance or Evaluation Obligation intrinsic defect requires reopening Phase 010.

# 13. Composition invariants

1. One exact authoritative Rubric Version governs one Scorecard's EvaluationBasis.
2. Rubric Version supersession never silently rebinds existing occurrences, obligations or Scorecards.
3. One Evaluation Obligation maps to at most one logical Scorecard.
4. Scorecard Draft state is non-authoritative.
5. Initial authority establishment must preserve Scorecard authority, immutable Version history, explanatory Provenance and obligation satisfaction as one coherent semantic result.
6. Evaluation Obligation `EvidenceRef` identifies the logical Scorecard, not one transient/current Version.
7. Judge amendment creates a successor Scorecard Version, not another evaluation/vote/obligation.
8. Versioning cannot create semantic authorship.
9. Provenance records actor and represented author separately where they differ.
10. Organizer capture/verification cannot invent Judge content or intent.
11. Capture channel does not change Evaluation Basis, author or weight.
12. Mixed paper/electronic traces converge on one logical Scorecard.
13. Post-authority transcription correction cannot be disguised as ordinary capture or Judge amendment.
14. Uncertain authority establishment cannot be reported as confirmed success.
15. Finalization does not itself expose peer judgments or derived standings.

# 14. Conceptual chaining summary

```text
Rubric working definition
  → Rubric.validateDefinition / prepareForUse
  → Versioning commit authoritative Rubric snapshot
  → Provenance record establishment
  → exact Rubric Version available as Evaluation Basis
```

```text
Outstanding Evaluation Obligation
  → Scorecard.start / resolve one logical Scorecard
  → non-authoritative Draft work
  → Scorecard.finalize
  → Versioning initial Scorecard Version
  → Provenance authority/source record
  → EvaluationObligation.satisfy(EvidenceRef = logical Scorecard)
```

```text
Satisfied obligation + current authoritative Scorecard Version
  → Scorecard.beginAmendment
  → amendment Draft
  → Scorecard.finalizeAmendment
  → Versioning.commitSuccessor(expectedCurrent, snapshot)
  → Provenance amendment record
  → same logical Scorecard / same Satisfied obligation / one vote
```

```text
identified paper source
  → capture into same logical Scorecard Draft
  → verify source fidelity + Judge commit intent
  → same Finalize Evaluation authority postconditions
  → Provenance Actor = capture verifier, RepresentedAuthority = Judge
```

These chains are conceptual relationships, not API calls, transactions, queues, workflow engines, retries or persistence choreography.

# 15. Deferred work

011-F must determine:

- Scorecard/Rubric/Occurrence Version invalidation consequences;
- post-authority paper transcription correction;
- structural misattribution;
- occurrence replacement;
- successor Evaluation Obligation after previously satisfying evidence becomes unusable;
- affected-state propagation while preserving prior authority/history.

011-G must determine:

- eligibility of current authoritative Scorecard evidence for Coverage/Aggregate/Rank;
- derived recalculation after Finalization/amendment/correction;
- Award and Outcome Declaration composition.

011-I will re-audit the whole application action surface/chaining/automation model after all family owners exist.

# 16. Exit criteria

| Criterion | Result |
| --- | --- |
| exact MUDAC Evaluation Basis identified | PASS |
| Rubric authoritative-establishment composition explicit | PASS |
| one logical Scorecard per responsibility explicit | PASS |
| initial Finalization authority postconditions explicit | PASS |
| Evaluation Obligation satisfaction binding explicit | PASS |
| amendment / one-vote semantics explicit | PASS |
| Versioning versus Provenance ownership preserved | PASS |
| paper/electronic capture parity and authorship preserved | PASS |
| ambiguous paper intent prevented from becoming authority | PASS |
| generic Versioning/Provenance actions not over-exposed | PASS |
| correction/invalidation work left to 011-F | PASS |
| no hidden runtime architecture introduced | PASS |
| no Phase 010 reopen required | PASS |

# Final decision

**PASS — 011-E closes evaluation-basis, Scorecard-authority, Versioning/Provenance and paper-capture composition sufficiently to proceed to 011-F.**

# Phase 011 handoff

Next:

> **011-F — Temporal Correction, Invalidation, Replacement, Successor Work & Affected-State Propagation**

011-F now starts from a precise authority baseline: a qualifying evaluation is one logical Judge-authored Scorecard bound to one exact Rubric Version, with current authoritative state represented by Versioning, meaningful actor/author/source history represented by Provenance, and responsibility represented independently by Evaluation Obligation.