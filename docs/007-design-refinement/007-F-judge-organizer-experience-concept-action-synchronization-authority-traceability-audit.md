---
type: Design Audit
title: 007-F — Judge & Organizer Experience-to-Concept Action, Synchronization & Authority Traceability Audit
description: Traces material Judge and Organizer interaction semantics to the current sixteen Concepts, Concept actions, synchronization contracts, derived projections, Access/disclosure rules, temporal semantics, and authority-establishing postconditions.
status: stable
tags: [phase-007, jackson, experience, traceability, actions, synchronization, authority]
sources:
  - resource: ../007-design-refinement/007-A-design-reentry-implementation-freeze-jackson-completion-criteria.md
  - resource: ../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
  - resource: ../007-design-refinement/007-C-cross-concept-synchronization-completeness-authority-seam-audit.md
  - resource: ../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
  - resource: ../007-design-refinement/007-E-end-to-end-scenario-exception-failure-adversarial-authority-validation.md
  - resource: ../003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md
  - resource: ../canonical/concepts/index.md
  - resource: ../canonical/experience/index.md
  - resource: ../canonical/experience/action-authority-traceability.md
  - resource: ../canonical/synchronizations/concept-synchronizations.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: ../canonical/governance/design-implementation-boundary.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-10T06:51:00Z }
---

# Purpose

Establish the sixth evidence gate in the renewed Jackson-methodology runway by proving that the conceptual Judge and Organizer experiences remain presentations and invocations of the accepted Concept system rather than a second, UI-owned domain model.

Phases 003 and 005 already established a coherent interaction architecture, but 007-B through 007-E materially sharpened the current model: Publication became a Concept, synchronization authority became explicit, temporal/correction dimensions were separated, and adversarial scenarios clarified emergency technical authority and irreversible disclosure exposure.

007-F therefore re-audits experience semantics against the **current** post-refinement model rather than assuming the Phase 003 exit automatically remains sufficient.

The governing question is:

> For every material Judge or Organizer interaction, can MUDAC identify the owning Concept action or query, participating synchronization, current authority/preconditions, authoritative versus derived state, failure/uncertainty meaning, and historical consequence without inventing a screen-owned action or lifecycle?

# Principal result

**007-F passes. The Judge and Organizer experience architecture remains traceable to the current sixteen-Concept system and does not require another Concept or domain action family.**

No screen, route, work mode, wizard step, exception row, confirmation dialog, recovery state, or status badge needs to own product semantics independently.

The audit finds one representational gap worth closing canonically: the experience layer previously expressed these rules across several owners but lacked one explicit current contract stating that consequential interactions must trace to Concept actions/synchronizations and that UI affordance, confirmation, mode, or projection never creates authority.

That gap is now closed by [Experience Action, State & Authority Traceability](../canonical/experience/action-authority-traceability.md).

No accepted Concept action is added, removed, or repurposed by 007-F.

# Audit method

Each material experience behavior is classified as one of:

1. **Concept action invocation**;
2. **Concept query/read**;
3. **authority-establishing synchronization**;
4. **derived/convergent projection**;
5. **non-authoritative working-state interaction**; or
6. **implementation-only interaction state** with no domain authority.

For actions, the audit additionally asks:

- which Identity/Participation context acts;
- what current Access and semantic authority are required;
- which Concept state/preconditions must be re-evaluated at execution time;
- whether success establishes authority immediately or triggers derived convergence;
- what an unknown outcome means;
- what historical state must remain preserved;
- whether the UI wording risks collapsing two distinct semantic actions.

Any interaction that could not be classified would return to Concept/synchronization design.

# Core experience rule confirmed

The complete UX authority chain is:

```text
visible affordance / navigation
          ↓
user intent
          ↓
current Identity + Participation context
          ↓
Access + semantic-authority check
          ↓
Concept action preconditions
          ↓
Concept action
          ↓
required authority-establishing synchronization
          ↓
truthful authoritative postcondition
          ↓
derived/convergent refresh
          ↓
user-visible confirmed state
```

The experience may optimize, preview, explain, confirm, retry, or recover this path. It may not shorten it semantically.

# Judge experience traceability

## J01 — Competition entry and routing

Judge entry through a URL, QR code, join code, bookmark, or event link is navigation only.

**Trace:** Competition context query + Identity establishment/reverification + Participation lookup/enrollment + Access check.

**Not authority:** possession of the route or code.

**Finding:** PASS. Existing onboarding correctly treats routing mechanisms as accelerators rather than Identity/Participation/Access.

## J02 — Returning Judge recognition

A returning person may reuse Identity continuity.

**Concept actions:** `Identity.recognizeReturningIdentity`, `verify`/`reverify`; current Competition involvement then uses a distinct `Participation.enroll` when needed.

**Boundary:** a historical Judge role never resumes automatically.

**Finding:** PASS.

## J03 — Check-in and Ready to Judge

Judge check-in maps to `Participation.checkIn`; later active event participation may map to `Participation.activate` under current operational rules.

`Ready to Judge` is not a Concept action or lifecycle state. It is a derived projection over current Competition, Participation, Panel/Encounter context, Access, and other required operational conditions.

**Failure rule:** the UX cannot offer a manual `mark Judge ready` field that bypasses source conditions.

**Finding:** PASS.

## J04 — Panel context

A Judge views the current Panel assignment and relevant event information.

**Trace:** Panel/Participation query under Judge-safe Access.

Panel assignment itself is Organizer-governed through Panel actions such as `addMember`, `replaceMember`, or membership termination. Merely opening a Panel screen does not create membership.

**Finding:** PASS.

## J05 — Encounter selection / confirmation

Judge navigation resolves the current eligible Encounter and presents Alias + Division prominently.

Selecting or viewing the Encounter is not equivalent to `JudgingEncounter.begin`, `confirmPresentationComplete`, or `complete` unless that semantic action is explicitly intended and authorized.

**Synchronization:** effective Participation + Panel/Encounter state + exact Rubric Version establishes the logical Scorecard obligation.

**Finding:** PASS WITH WORDING GUARDRAIL. Future UI must preserve `presentation complete`, `Encounter complete`, and navigation/selection as distinct meanings.

## J06 — Start Scorecard

Beginning evaluation maps to `Scorecard.start` for the one logical Judge Participation × Encounter subject.

**Preconditions:** effective Encounter participation, one exact authoritative applicable Rubric Version, current Judge Access, and no competing logical Scorecard identity.

**Synchronization:** Encounter + Rubric Version → logical Scorecard obligation.

**Finding:** PASS.

## J07 — Draft scoring and Notes

Criterion scoring and Notes map directly to Scorecard working actions such as `setCriterionScore`, `clearCriterionScore`, note setters/clearers, and equivalent Draft changes.

Autosave/persistence feedback is not a domain action and must not be labeled as authority.

**Finding:** PASS.

## J08 — Scorecard review and Finalization

Review is presentation/query behavior. The explicit consequential action is `Scorecard.finalize`.

**Authority-establishing synchronization:** Scorecard Finalization + immutable Version + meaningful Provenance form one semantic success boundary.

Coverage/Aggregate/Rank are downstream derived refreshes and may converge later.

**Uncertainty:** if the response is lost, the UX shows unknown/uncertain authority and reconciles the logical Scorecard before retry; it does not assume failure.

**Finding:** PASS.

## J09 — Deferred unfinished Draft

Leaving an Encounter with an unfinished Draft is navigation plus retained working state, not Encounter completion, Scorecard Finalization, recusal, or obligation satisfaction.

The outstanding obligation remains visible to authorized event operation.

**Finding:** PASS.

## J10 — Amendment

Amendment maps to `Scorecard.beginAmendment`, Draft editing, `abandonAmendment`, and `finalizeAmendment`.

**Temporal rule:** the existing authoritative Version remains current until amendment Finalization establishes a successor Version.

**Post-event authority:** after Event Completed, narrow temporary Access may be established for the specific correction rather than restoring general Judge history.

**Finding:** PASS.

## J11 — Judge history

In-event Judge history is a query over the Judge's current Participation, Encounters, and own Scorecards under current Access.

It is not an archival entitlement attached permanently to Identity. At Event Completed, ordinary private-evaluation Access expires.

**Finding:** PASS.

## J12 — Peer-result and identity shielding

Peer Scorecards, Aggregate, Coverage, Rank, standings, and protected Team identity are not merely hidden navigation items; they are outside ordinary Judge disclosure authority.

A responsive/mobile/accessibility representation cannot expose them as a shortcut.

**Finding:** PASS.

# Organizer preparation traceability

## O01 — Competition creation/details

Organizer preparation maps to `Competition.create` and `updateDetails`.

Ready/Active remain separate explicit lifecycle actions.

**Finding:** PASS.

## O02 — Division configuration

Division definition maps to `Division.define`/`updateDefinition`; Team assignment maps to `assign` and post-use error correction maps specifically to `correctAssignment`.

The experience must not present ordinary drag-and-drop cohort movement after judging as though it were semantically identical to correction.

**Finding:** PASS.

## O03 — Team administration

Team setup maps to `Team.create`/`updateAdministrativeRecord`; withdrawal/restoration uses explicit Team actions while preserving existing historical relationships.

Team Name and descriptive attributes remain metadata and do not silently change Alias or competitive identity.

**Finding:** PASS.

## O04 — Alias preparation and Judge-safe preview

Alias setup maps to `Alias.assign`, `replace`, `retire`, and authorized `resolve`.

Judge-safe preview is a representation of the Judge disclosure profile, not an Organizer becoming a Judge Participation or gaining Judge authorship.

**Finding:** PASS.

## O05 — Rubric preparation

Rubric editing maps to its working-definition actions (`createDraft`, configuration/edit actions, `validate`, `prepareForUse`).

**Authority-establishing synchronization:** working Rubric → authoritative immutable Rubric Version through Versioning/Provenance.

Preview/validation of a working definition is not itself authoritative Version establishment.

**Finding:** PASS.

## O06 — Judge Participation and Panel planning

Judge event involvement maps to Identity/Participation actions; Panel grouping maps to Panel membership/composition actions.

Expertise metadata helps composition policy but does not grant Access. Planned Panel membership does not create historical Encounter participation or a Scorecard obligation.

**Finding:** PASS.

## O07 — Competition readiness

Readiness workspace is a projection over current source configuration/policies.

`Competition.markReady` is the explicit lifecycle commitment after current gates pass. Readiness-invalidating source changes may require `returnToDraft` rather than mutating a checklist projection.

**Finding:** PASS.

# Organizer live-operations traceability

## O08 — Competition activation

Activation maps to `Competition.activate` and must re-evaluate current readiness/preconditions.

A button rendered while stale cannot establish Active state if current source state no longer permits it.

**Finding:** PASS.

## O09 — Judge no-show/withdrawal

A no-show does not create a zero Scorecard or mutate Identity.

Organizer action affects Participation availability/lifecycle and, where needed, Panel membership prospectively. Encounter obligations arise only from effective Encounter participation.

**Finding:** PASS.

## O10 — Panel replacement

Permanent/current grouping changes map to Panel `replaceMember`/membership actions.

A one-occurrence substitution or recusal maps to `JudgingEncounter.recordParticipantAdjustment` instead of falsifying Panel history.

**Finding:** PASS.

## O11 — Encounter operation

Prepared/open/presentation-complete/complete/cancel/invalidated meanings trace to explicit Judging Encounter actions.

The UX must not use one generic `complete` or `resolve` control to blur:

- presentation completion;
- obligation resolution;
- Encounter completion;
- cancellation; or
- invalidation.

**Finding:** PASS WITH WORDING GUARDRAIL.

## O12 — Paper fallback and capture

Paper-mode UI is not a new Scorecard Concept or Organizer-authored evaluation mode.

The Organizer transcribes identified physical evidence into non-authoritative capture working state. Verification synchronizes that evidence into the same logical Scorecard authority while preserving Judge semantic authorship and Organizer capture actor in Provenance.

The capture UI must therefore be framed as transcription/verification rather than ordinary editing of a Judge's finalized score.

**Finding:** PASS.

## O13 — Duplicate paper/electronic evidence

The UI may surface a reconciliation exception, but the exception row is only a projection.

The source resolution must preserve one logical Scorecard and explicitly determine source/correction authority; dismissing the exception cannot create a second vote or choose truth by itself.

**Finding:** PASS.

## O14 — Live exception workspace

Blocked, incomplete, degraded, uncertain, composition, Coverage, and similar exception indicators are derived views over owned source state.

Organizer may act on the source or invoke a governed exception/correction path. `Acknowledge`, `hide`, or `close` must not be confused with domain resolution.

**Finding:** PASS WITH CANONICAL TRACEABILITY CLARIFICATION.

## O15 — Event completion

Ending live judging maps to `Competition.completeEvent`.

**Synchronization:** Event Completed → ordinary Judge private-evaluation Access expiry and role/lifecycle coordination.

Unresolved paper capture, correction, or evidence work may continue for Organizer reconciliation. The experience must not imply `completeEvent` means all Scorecards resolved, Ranking ready, or results official.

**Finding:** PASS.

## O16 — Exceptional resumeEvent

If a prematurely completed event is legitimately resumed, the UI invokes explicit `Competition.resumeEvent`.

It must not present `resume` as automatic restoration of previous Judge sessions, Access, Participation state, or Panel eligibility. Those contexts are re-evaluated/reactivated explicitly.

**Finding:** PASS.

# Organizer reconciliation and outcome traceability

## O17 — Evidence inspection

Drill-down from Aggregate/Team result to Encounter → Scorecard → Criterion → Rubric Version/Provenance is query/explainability behavior over authoritative sources.

Inspecting a calculated result does not make it official.

**Finding:** PASS.

## O18 — Coverage

Coverage is a derived sufficiency projection, not editable evidence.

Missing evaluation remains missing rather than zero. Where policy supports an accepted Coverage exception, the exception authority must preserve the actual shortfall and be explicit; manually changing the displayed ratio is never correction.

**Finding:** PASS.

## O19 — Aggregate and Rank

Aggregate and Rank are derived mechanisms. The Organizer may inspect/explain them but does not directly edit them.

A source correction changes the applicable inputs/policy and causes derived recomputation; it does not authorize manual Rank repair.

**Finding:** PASS.

## O20 — Awards

Award definition/conferral/revocation/correction maps to `Award.define`, `updateDefinition`, `confer`, `revoke`, and `correctConferral` as applicable.

For rank-derived Awards, the candidate comes from ready Rank under declared selection semantics. Organizer confirmation cannot contradict the rule while retaining a rank-derived label.

**Finding:** PASS.

## O21 — Finalization readiness

Finalization readiness is derived from authoritative evidence, Coverage/eligibility, Ranking readiness, Awards/policy, and unresolved outcome-affecting conditions.

It is not a manually closable checklist.

**Finding:** PASS.

## O22 — Competition Finalization

The consequential action is `Competition.finalize`.

**Authority-establishing synchronization:** successful Finalization establishes both Finalized Competition state and one resolvable Official Outcome Revision.

A confirmation modal records deliberate intent but cannot bypass current finalization gates. Unknown outcome is reconciled rather than optimistically labeled successful or blindly retried.

**Finding:** PASS.

## O23 — Post-Finalization correction

Corrected sources/derived calculations may be shown while the prior revision remains the latest declared official revision and is marked Affected where appropriate.

The UI cannot silently replace official authority just because a recomputed Rank differs. Successor official authority follows the explicit correction/confirmation semantics established in 007-D.

**Finding:** PASS.

# Organizer material, Export and Publication traceability

## O24 — Generate/preview Export

Export workflow maps to `request`, `validateDisclosure`, `generate`, `retrieve`, regeneration, and retirement actions as appropriate.

Preview is query/representation behavior. It does not make the artifact public.

**Finding:** PASS.

## O25 — Publication

Actual release maps to `Publication.publish`; later removal from current distribution maps to `withdraw`; replacement release maps to successor Publication semantics.

**Synchronization:** Export → explicit Publication.

`Competition Finalized`, `Export generated`, `preview approved`, and `Publication established` remain different states/actions.

**Finding:** PASS.

## O26 — Corrected public output

Source correction may make an Export/Publication Affected or Stale without rewriting what was released.

The corrective user path must explicitly generate/select a successor Export and establish/withdraw/supersede Publication as policy requires.

**Finding:** PASS.

# Cross-cutting authority audit

The experience model preserves all important authority separations:

```text
screen/route availability        != Access
Access                           != semantic authorship
Organizer operational capability != Judge authorship
technical/admin capability        != Competition authority
confirmation dialog               != authoritative success
work mode                         != Competition lifecycle
readiness indicator               != lifecycle transition
exception row                     != source state
calculated Rank                   != official outcome
Export preview                    != Publication
Publication                      != transport delivery success
```

No interaction architecture examined by 007-F violates these seams.

# Status and temporal traceability audit

The current UX grammar survives 007-D's temporal refinement.

A future interface must be able to show independent dimensions rather than one overloaded status:

- domain lifecycle;
- Draft versus authoritative state;
- eligible current Version versus superseded/invalidated state;
- current versus historical occurrence context;
- replacement relationship;
- affected/stale dependency currency;
- latest declared official revision;
- Export currency;
- Publication distribution state;
- persistence/commit uncertainty.

A badge/component may summarize a dimension; it may not collapse these into a new universal state machine.

# Disclosure and role-mode audit

Judge/Organizer modes are interaction context, not permanent Identity role or authorization storage.

Switching mode must re-establish the selected Participation context and evaluate Access/disclosure for that context. Organizer-sensitive state must not remain visible merely because the same Identity was authorized for it in another mode.

Judge-safe preview is an Organizer-authorized representation test, not a switch into Judge semantic authority.

Actual disclosure failure remains governed by the 007-E clarification: later revocation prevents future exposure but cannot erase a disclosure that already occurred.

**Result:** PASS.

# Accessibility/responsive audit

The action trace does not depend on one interaction modality.

Phone, wide-screen, keyboard, screen-reader, zoomed, narrow, assisted, and paper/degraded representations may reorganize navigation but must preserve:

- action identity;
- consequence/confirmation meaning;
- Access/disclosure boundary;
- current subject/context;
- Draft versus authoritative distinction;
- uncertainty/recovery state;
- correction/invalidation semantics.

No accessible or degraded path may become a weaker semantic-authority route.

**Result:** PASS.

# Hidden-semantic pressure test

007-F re-tests several UX-shaped candidates that could have appeared Concept-like.

| Candidate | Decision | Reason |
| --- | --- | --- |
| Work Mode | reject | organizes attention/navigation; does not own Competition state |
| Ready to Judge | reject | derived projection over current source/authority state |
| Readiness Workspace | reject | view/projection over source configuration |
| Exception / Issue | reject | projection identifying source conditions; resolution occurs at owning source/policy |
| Confirmation | reject | interaction safeguard/evidence of intent, not authority state |
| Recovery State | reject | communicates uncertainty and next action; source authority remains elsewhere |
| Preview | reject | representation/query interaction; does not establish Publication or Judge authority |
| Scorecard Obligation | reject | derived from Encounter effective participation + Rubric basis |
| Finalization Readiness | reject | derived gate over existing authoritative sources |
| Publication Approval Step | reject for current scope | preview/confirmation may precede Publication but no independent lifecycle/purpose is established |

No candidate has a sufficiently independent user purpose/state/actions to become a seventeenth Concept.

# Semantic wording hazards closed

The audit identifies wording as a real downstream implementation risk even when the Concept model is correct.

Future visual/component design should avoid collapsing these pairs:

```text
check in                   != Ready to Judge
select Encounter           != begin Encounter
presentation complete      != Encounter complete
Draft saved                != Scorecard Finalized
begin amendment            != edit finalized Version in place
replace Panel member       != adjust one Encounter participant
correct Division           != routine reassignment after judging
acknowledge exception      != resolve source condition
complete event             != finalize Competition
calculated                 != official
generate Export            != publish
withdraw Publication       != delete history
retry                      != create another semantic effect
```

This is a traceability constraint, not prescribed UI copy.

# Canonical change from 007-F

007-F creates one new current experience owner:

`docs/canonical/experience/action-authority-traceability.md`

It consolidates the rule that material interactions must trace to accepted Concept actions, queries, synchronizations, projections, working state, or implementation-only state.

The new owner also makes explicit that:

- UI visibility/enabling is not authorization;
- confirmation is intent evidence, not authority;
- work modes are not lifecycle;
- exception/status projections are not editable source truth;
- user-visible verbs must preserve materially distinct Concept actions;
- unknown authoritative outcomes reconcile before retry;
- accessible/responsive variants preserve identical semantic authority.

This does not add a Concept, synchronization, policy, stable rule namespace, component model, route model, or API contract.

# Implementation-freeze consequence

007-F is design-only and does not authorize screen/component implementation.

In particular, it does **not** authorize:

- React routes/components;
- forms or client state machines;
- authentication/session UX;
- domain API endpoints;
- server authorization implementation;
- offline Draft storage;
- conflict-resolution components;
- status-enum implementation;
- paper capture UI;
- finalization/publication UI;
- accessibility test automation for domain screens.

The retained 006-D non-domain executable substrate remains the ceiling until a later formal methodology exit explicitly resumes implementation.

# Methodology-gate decision

**007-F passes the Judge & Organizer Experience-to-Concept Action, Synchronization & Authority Traceability gate.**

Evidence established:

- all material Judge interactions trace to accepted Identity, Participation, Access, Encounter, Scorecard, Versioning and Provenance behavior;
- all material Organizer preparation/live/reconciliation/outcome/material interactions trace to accepted Concept actions, synchronizations or derived projections;
- UI work modes do not introduce lifecycle state;
- Ready/exception/Coverage/Rank/finalization-readiness views remain derived rather than editable authority;
- Scorecard and Competition Finalization preserve authority-establishing synchronization boundaries under uncertainty;
- paper capture remains transcription/verification without Organizer authorship transfer;
- role switching re-evaluates Participation/Access rather than unioning capabilities;
- temporal/correction dimensions remain presentable without a universal status concept;
- Export/Publication remain distinct in user interaction;
- no inaccessible/responsive/degraded path requires a semantic fork;
- no hidden UX Concept or action family is required.

The sixth Jackson completion gate now has substantive evidence.

# Remaining methodology runway

007-A's remaining pre-exit evidence includes integrated policy/representation closure and then a dedicated formal methodology exit.

The next audit should therefore re-evaluate anonymity/disclosure, evaluation policy, Panel composition, correction authority, Awards/finalization, paper continuity, official outcome semantics, Export/Publication, and operational governance as one integrated policy/representation system rather than as isolated documents.

# Handoff

Proceed to **007-G — Policy, Representation, Outcome, Disclosure & Operational-Governance Closure Audit**.
