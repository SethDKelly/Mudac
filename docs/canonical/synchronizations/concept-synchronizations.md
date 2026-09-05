---
type: Synchronization Contract
title: Concept Synchronization Contracts
description: Defines current cross-concept synchronization triggers, authority, preconditions, postconditions, temporal/history effects, failure/retry meaning, and authority seams for MUDAC.
status: stable
tags: [synchronization, concept-design, authority, lifecycle, correction, outcomes, publication]
sources:
  - resource: ../../007-design-refinement/007-C-cross-concept-synchronization-completeness-authority-seam-audit.md
  - resource: ../concepts/index.md
  - resource: ../mechanisms/readiness.md
  - resource: ../mechanisms/official-outcome-revision.md
  - resource: ../policies/evaluation-policy.md
  - resource: ../policies/correction-authority.md
  - resource: ../policies/awards-finalization.md
  - resource: ../policies/continuity-paper.md
  - resource: ../policies/anonymity-disclosure.md
---

# Purpose

Define how independent MUDAC Concepts coordinate so the application can produce coherent Competition behavior without moving cross-cutting workflow state into a catch-all Concept or allowing one Concept's action to impersonate another Concept's authority.

# Synchronization semantics

A synchronization coordinates existing owners. It does not create a new semantic owner merely because several concepts participate.

Two synchronization classes matter:

## Authority-establishing synchronization

The synchronization establishes or changes authoritative domain state. Its externally observable success requires the authoritative postconditions to hold together. Examples include Scorecard Finalization, paper-capture verification becoming authoritative, Competition Finalization establishing an Official Outcome Revision, and Publication establishment.

A partial technical write is not conceptual success. If the caller cannot know whether the authority-establishing effect committed, the outcome is uncertain and must be reconciled against authoritative state before a retry can create another semantic effect.

## Derived/convergent synchronization

The authoritative source change may commit before dependent projections or derived calculations refresh. Readiness, Coverage, Aggregate, Rank, and impact indicators may therefore converge after the source transition, but stale/affected state must not masquerade as current authoritative truth.

# Cross-cutting rules

- Preconditions are evaluated against current authoritative state at the consequential transition, not merely against an earlier browser/query snapshot.
- Synchronization does not transfer authorship or decision authority. Access may permit an action but does not make the actor the semantic author of another person's judgment.
- Historical snapshots do not silently rebind when current Team, Division, Alias, Panel, Rubric, policy, or outcome state changes.
- Repeating the same semantic intent must converge rather than create duplicate Competition, Encounter, Scorecard, Version, Award, outcome, Export, or Publication authority. Concrete idempotency mechanisms remain architecture/implementation concerns.
- A source correction may invalidate or affect downstream derived state without rewriting historical source evidence or an already-declared official/public state.
- Synchronization failure is explicit. Unknown/partial technical outcomes are not represented as success merely to simplify the experience.

<a id="concept-sync-01"></a>
# 01 — Identity proof, Participation enrollment and operating context

**Trigger:** a human establishes/reverifies Identity and begins or resumes Competition participation.

**Preconditions:** current Identity proof is adequate for the requested operation; the Competition permits the requested Participation capacity; no weak matching silently merges distinct Identities.

**Authority:** Identity owns human continuity; Participation owns Competition-scoped capacity; Access owns current capability. Authentication proof does not own any of those meanings.

**Postconditions:** enrollment creates or resolves one intended Participation rather than duplicating it; operating context identifies the exact Participation under which later Access is evaluated.

**Failure/retry:** failed proof creates no Participation authority. Repeated enrollment intent converges on the same current Participation when it represents the same person/Competition/capacity.

<a id="concept-sync-02"></a>
# 02 — Competition readiness and activation

**Trigger:** `Competition.markReady` or `Competition.activate`.

**Preconditions:** current [Readiness](../mechanisms/readiness.md) has no blocking conditions for the requested transition. Structural readiness includes valid Team/Division/Alias state; later evaluation/operations readiness includes the applicable judging configuration and authoritative evaluation basis needed for live judging.

**Authority:** Competition owns the lifecycle transition. Readiness is derived and cannot be manually asserted as a substitute for source state.

**Postconditions:** Ready/Active means the relevant source facts satisfied the gate at transition time. A later source change that invalidates Ready before activation requires readiness reassessment and ordinarily return to Draft; an Active Competition instead exposes an affected/degraded condition and governed correction rather than pretending live history never occurred.

**Failure/retry:** transition failure leaves lifecycle unchanged. Retrying `markReady`/`activate` reevaluates current source state.

<a id="concept-sync-03"></a>
# 03 — Event completion, Judge Participation and ordinary Access expiry

**Trigger:** successful `Competition.completeEvent`.

**Preconditions:** Competition is Active and the actor has authority to end live judging.

**Authority:** Competition owns Event Completed; Participation owns participation lifecycle; Access owns capability/disclosure expiry.

**Postconditions:** ordinary Judge private-evaluation Access for the Competition expires. Judge Participations that were operational for the event converge out of live Active use toward Completed; historical Participation and evaluation attribution remain. Organizer Participation may remain Active for reconciliation. No Scorecard, Note, Encounter, Identity or Provenance is deleted.

**Failure/retry:** Event Completed must never be displayed as successful while ordinary Judge private-evaluation capability is intentionally left active as the normal state. Derived/session propagation may lag technically, but every protected request still evaluates current Access against Event Completed.

<a id="concept-sync-04"></a>
# 04 — Exceptional event resume does not restore authority automatically

**Trigger:** exceptional `Competition.resumeEvent` before Finalization.

**Preconditions:** legitimate Organizer authority and reason; Competition is Event Completed rather than Finalized.

**Authority:** Competition may return to Active. That transition does not itself recreate Judge Participation eligibility, sessions, Panel membership, or Access grants.

**Postconditions:** live operation may resume only after relevant Judge Participations and Access are explicitly reevaluated/reactivated under current state. Prior temporary/cached capability is not presumed valid merely because the Competition is Active again.

**Failure/retry:** if reactivation cannot be established safely, affected Judges remain unable to act and operational fallback/reassignment is required.

<a id="concept-sync-05"></a>
# 05 — Team, Division and Alias readiness plus Encounter historical context

**Trigger:** Team creation/withdrawal/restoration, Division assignment/correction, Alias assignment/replacement/retirement, Competition readiness evaluation, or Encounter begin.

**Preconditions:** before Ready/Active, every non-withdrawn competing Team has exactly one valid active Division assignment and one active Competition Alias, and active Alias values are unique within scope.

**Authority:** Team owns administrative competitor continuity/status; Division owns competitive cohort assignment; Alias owns the Judge-facing alternate identity. None absorbs the others.

**Postconditions:** readiness recomputes from current state. When an Encounter begins, it snapshots the stable Team plus the Alias and Division context actually presented. Later current corrections do not rewrite that historical Encounter context.

**Failure/retry:** an invalid setup blocks readiness/activation. A correction after judging may affect derived eligibility/ranking but does not mutate past Scorecards or historical presentation snapshots.

<a id="concept-sync-06"></a>
# 06 — Participation and Panel produce Encounter effective participants

**Trigger:** `JudgingEncounter.begin` for a Panel/Team occurrence, plus later explicit participant adjustment.

**Preconditions:** Competition is Active; the Panel is available; each ordinary starting participant is a currently eligible Judge Participation in the same Competition; composition policy is satisfied or an allowed explicit exception is recorded.

**Authority:** Participation determines current capacity/eligibility, Panel determines intended grouping, and Judging Encounter owns the actual occurrence and its participant history.

**Postconditions:** Encounter opening records a starting participant/context snapshot. Explicit recusal/absence/replacement adjustments produce the effective evaluation-participant set. Nominal Panel membership alone does not create a Scorecard obligation.

**Failure/retry:** repeated begin intent for the same intended Panel/Team occurrence converges on one valid Encounter unless an explicit rejudge/replacement creates another occurrence. Once authoritative evaluation exists, removing it cannot be accomplished by silently editing the participant set.

<a id="concept-sync-07"></a>
# 07 — Rubric authoritative establishment

**Trigger:** a valid Rubric working definition is prepared for authoritative use.

**Preconditions:** Rubric validation succeeds; the actor has authority to establish the evaluation instrument; any applicability context needed to determine future Encounter basis is unambiguous.

**Authority:** Rubric owns evaluation semantics; Versioning owns immutable authoritative states; Provenance owns meaningful origin/authority history.

**Postconditions:** one immutable Rubric Version becomes authoritative for its lineage/applicability, and the establishment is attributable through Provenance. Existing Scorecards remain bound to the exact earlier Version they used.

**Failure/retry:** the system must not claim an authoritative Rubric Version if the immutable Version/provenance establishment did not succeed. Repeated establishment intent must not create multiple semantically current versions from one action.

<a id="concept-sync-08"></a>
# 08 — Encounter + exact Rubric Version create one logical Scorecard obligation

**Trigger:** Encounter becomes Open with an effective Judge participant and a resolvable applicable authoritative Rubric Version.

**Preconditions:** effective Judge participation is valid; one exact Rubric Version is applicable to the Encounter; the evaluation basis is not ambiguous; no structural duplicate logical Scorecard already exists for Judge Participation × Encounter.

**Authority:** Encounter owns the obligation context; Rubric Version owns the instrument semantics; Scorecard owns the Judge's judgment.

**Postconditions:** the application can resolve at most one logical Scorecard obligation/identity for that Judge Participation and Encounter with a fixed Rubric-Version basis. Starting work creates a non-authoritative Scorecard Draft; obligation existence alone is not a finalized Scorecard.

**Failure/retry:** if the Rubric basis is ambiguous or unavailable, judging cannot safely create a new authoritative evaluation obligation. Repeated `start` converges on the same logical Scorecard.

<a id="concept-sync-09"></a>
# 09 — Scorecard Finalization/Amendment establishes Version + Provenance and affects derived evidence

**Trigger:** `Scorecard.finalize` or `Scorecard.finalizeAmendment`.

**Preconditions:** the Scorecard represents a valid outstanding/continuing evaluation obligation; structural identity and exact Rubric Version are fixed; required responses/Notes are complete and valid; current Access permits the semantic author/capture path; an amendment is based on the current authoritative Version.

**Authority:** Scorecard owns judgment/finalization semantics; Versioning owns immutable authoritative snapshots; Provenance owns author/actor/channel/reason history. Derived mechanisms consume the resulting authoritative evidence but do not authorize it.

**Postconditions:** Finalization establishes exactly one current authoritative Scorecard Version and matching meaningful Provenance. Amendment Finalization supersedes the prior current Version without deleting it or adding evaluation weight. Encounter completion, Coverage, Aggregate and Rank may then recompute from the new source authority.

**Failure/retry:** Version/provenance establishment is authority-establishing and may not expose partial semantic success. Derived refresh may lag and must be identifiable as stale/affected. A lost response is reconciled against the logical Scorecard/current Version before retry can create another effect.

<a id="concept-sync-10"></a>
# 10 — Paper capture verification establishes the same Scorecard authority without authorship transfer

**Trigger:** Organizer captures a physical Judge evaluation and explicitly verifies the digital capture against the identified paper source.

**Preconditions:** physical source identity/context is unambiguous; Judge Participation, Encounter and exact Rubric Version are resolved; captured responses are complete/valid; source is legible enough to establish what the Judge actually recorded.

**Authority:** Judge remains evaluation author; Organizer is capture/verification actor; Scorecard owns evaluation content; Provenance owns source/channel/capture history.

**Postconditions:** before verification, capture remains a non-authoritative Draft. Successful verification/finalization establishes the same logical authoritative Scorecard Version semantics as electronic judging, with paper origin preserved in Provenance.

**Failure/retry:** ambiguous Judge intent remains unresolved rather than being invented by Organizer. Demonstrable transcription mismatch uses capture correction with preserved history. Duplicate capture of the same physical source must converge rather than create another Judge vote.

<a id="concept-sync-11"></a>
# 11 — Authoritative evidence derives Coverage, Aggregate and Rank

**Trigger:** authoritative Scorecard/Encounter/Division/Evaluation-Policy state changes or an applicable exception is resolved.

**Preconditions:** only eligible current authoritative evidence participates; missing is not zero; invalidated evidence is excluded according to policy; Rubric compatibility is explicit.

**Authority:** Coverage, Aggregate and Rank are derived mechanisms. They do not rewrite Scorecards, Encounters, Division assignment or Evaluation Policy.

**Postconditions:** Coverage reflects evidence sufficiency, Aggregate reflects eligible individual Judge evaluations under declared weighting, and Rank orders eligible Teams within Division under current authoritative policy. Calculation basis remains reconstructible.

**Failure/retry:** derived computation may be stale/affected while recalculation occurs. A calculated value is not automatically ranking-ready or official. Failure to refresh cannot silently preserve an old value as though it reflected new source state.

<a id="concept-sync-12"></a>
# 12 — Source correction propagates impact without silently changing official history

**Trigger:** authoritative Division, Encounter, Scorecard, Rubric-compatibility, Evaluation-Policy or other outcome-affecting source correction.

**Preconditions:** correction follows [Correction and Authority Policy](../policies/correction-authority.md); structural errors are not disguised as ordinary amendments; prior authority remains reconstructible.

**Authority:** the corrected source Concept owns the source transition; derived mechanisms recompute; Award/Official Outcome/Publication authority changes only through their own explicit actions.

**Postconditions:** affected Coverage/Aggregate/Rank is recomputed or marked affected; rank-derived Award candidates/conferrals are rechecked; an existing Official Outcome Revision remains historical/current-as-declared until explicit successor confirmation; already generated/published representations remain attributable to their original source and may become affected/stale/superseded.

**Failure/retry:** no downstream layer may silently mutate historical evidence or transfer an Award/publication merely because a calculation changed.

<a id="concept-sync-13"></a>
# 13 — Rank-derived Award candidate and explicit conferral

**Trigger:** an Award with rank-derived selection is ready for conferral or needs reassessment after Rank changes.

**Preconditions:** applicable Division/result is ranking-ready; the Award definition, scope, selection rule, eligibility, tie behavior and recipient cardinality are satisfied.

**Authority:** Rank derives the candidate; Award owns recognized achievement and conferral. Organizer confirmation cannot contradict a rank-derived rule while continuing to label the Award rank-derived.

**Postconditions:** successful conferral records the Award recipient(s) and supporting result basis. A later Rank change marks the prior conferral for review; it does not silently move recognition to another Team.

**Failure/retry:** repeated confirmation of the same intended conferral converges. Incompatible tie/cardinality or stale ranking blocks ordinary conferral.

<a id="concept-sync-14"></a>
# 14 — Competition Finalization establishes one Official Outcome Revision

**Trigger:** authorized `Competition.finalize`.

**Preconditions:** Competition is Event Completed; Finalization Readiness has no unresolved blockers; outcome-affecting policy/evidence basis is identified; required Awards and material reconciliation issues are resolved.

**Authority:** Competition owns Finalized lifecycle state. Official Outcome Revision is the reconstructible authoritative outcome snapshot established by that transition. Publication remains separate.

**Postconditions:** successful Finalization leaves Competition Finalized and establishes one corresponding immutable/reconstructible Official Outcome Revision identifying the accepted evidence/policy/Rank/Award basis. These are one authority-establishing semantic outcome: a Competition must not be considered successfully Finalized with no resolvable official-outcome revision.

**Failure/retry:** partial technical failure must reconcile before retry. Repeated same Finalization intent converges on the already-established revision rather than generating competing official declarations. Post-finalization correction leaves Competition Finalized and requires explicit successor outcome confirmation.

<a id="concept-sync-15"></a>
# 15 — Export generation and Publication release remain separate

**Trigger:** Export generation from an identified source and, later, explicit `Publication.publish`/`withdraw`/successor publication.

**Preconditions:** Export binds exact source basis, purpose and disclosure profile. Publication additionally requires the exact representation selected for release, current publication authority, audience/channel and disclosure safety appropriate to that release.

**Authority:** Export owns the representation; Publication owns deliberate distribution state. Transport/delivery infrastructure does not own either semantic authority.

**Postconditions:** generation alone leaves no Publication. Successful Publication identifies the exact Export/representation released and its audience/channel/authority. Source correction or regeneration never silently retargets an existing Publication; replacement requires a successor Export and explicit successor Publication. Withdrawal preserves the historical fact that the earlier Publication existed.

**Failure/retry:** transport propagation/delivery may fail independently after Publication intent/authority is recorded and must be represented separately. Repeating the same publication intent cannot create ambiguous duplicate current releases.

<a id="concept-sync-16"></a>
# 16 — Participation-context switching preserves Access/disclosure isolation

**Trigger:** a dual-role Identity changes the active Competition Participation context used by the application experience.

**Preconditions:** the target Participation is current/legitimate and Identity proof/session is sufficient for context selection; any required re-verification/step-up is satisfied.

**Authority:** context selection chooses which Participation is presented to Access evaluation. It does not union the capabilities of all Participations held by the Identity.

**Postconditions:** protected reads/actions are evaluated only against the selected/current Participation context plus current Access conditions. Judge mode does not inherit Organizer scoring/identity disclosure; Organizer mode does not rewrite Judge authorship. Cached/previous-context information is not authority for the new context.

**Failure/retry:** failed context switch leaves the prior context explicit or returns to a safe selection state; the UI must not silently combine capabilities to avoid interruption.

# Missing-concept result

These synchronizations do not expose another required catch-all workflow Concept. Their state belongs to accepted Concepts, subordinate mechanisms, derived projections, policy decisions, or historical snapshots.

In particular:

- readiness remains derived;
- evaluation-basis resolution composes Rubric applicability, authoritative Rubric Version and policy rather than creating an `EvaluationSession` Concept;
- Scorecard obligation remains Encounter/Scorecard synchronization rather than a separate `Vote` Concept;
- paper capture remains a Scorecard/Provenance path;
- reconciliation remains an Organizer process;
- Official Outcome Revision remains an authoritative snapshot mechanism;
- transport/delivery remains below Publication.

# Handoff

This owner closes current trigger/precondition/postcondition/authority-seam consolidation. Temporal overlay semantics—affected/stale/current/historical, invalidation versus supersession, correction windows, successor authority and ordering across these synchronizations—remain subject to the next design-refinement audit.
