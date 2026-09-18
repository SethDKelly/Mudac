---
type: Phase Design Record
title: 013-J — Accessibility, Degraded Operation, Status/Feedback, Recovery & Semantic-Parity Mapping
description: "Audits accessible/responsive interaction, degraded and paper operation, uncertainty, status grammar, retry/recovery and privacy continuity so alternate paths preserve the same authority, disclosure, evidence and historical semantics established by 013-C through 013-I."
status: stable
tags: [phase-013, jackson, mapping, accessibility, degraded-operation, status, feedback, recovery, semantic-parity]
sources:
  - resource: 013-I-export-publication-audience-disclosure-external-recipient-representation-release-mapping.md
  - resource: ../canonical/experience/mapping-authority-baseline.md
  - resource: ../canonical/experience/accessibility-resilience.md
  - resource: ../canonical/experience/status-feedback-recovery.md
  - resource: ../canonical/experience/judge-evaluation.md
  - resource: ../canonical/experience/authority-lineage-correction.md
  - resource: ../canonical/experience/live-operations.md
  - resource: ../canonical/experience/reconciliation-derived-state.md
  - resource: ../canonical/experience/outcome-officiality.md
  - resource: ../canonical/experience/external-representation-release.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/policies/continuity-paper.md
  - resource: ../canonical/invariants/accessibility-semantic-parity.md
  - resource: ../canonical/invariants/truthful-authority-under-uncertainty.md
  - resource: ../canonical/invariants/one-logical-scorecard.md
---

# Purpose

Audit how the established MUDAC experience semantics survive alternate interaction and operating conditions without creating a second authority model.

013-J defines user-visible obligations for:

- accessible keyboard/touch/nonvisual/large-text/alternate-input operation;
- responsive and narrow-screen representation;
- assisted interaction without authorship transfer;
- interruptions, device replacement and shared-device handoff;
- partial connectivity, disconnected Draft work and paper fallback;
- authoritative-result uncertainty;
- safe retry, resume and state reconciliation;
- multidimensional status/feedback language;
- high-consequence confirmation and failure feedback;
- privacy/disclosure continuity through degraded/recovery paths;
- semantic parity for Export/Publication and other high-consequence actions.

It does not prescribe component libraries, browser APIs, offline databases, service workers, synchronization protocols, queue architecture, retry algorithms, WCAG test tooling, screen-reader implementation, responsive breakpoints or infrastructure recovery design.

# Decision

**COMPLETE — PASS. Proceed to 013-K.**

```text
013-A START GATE                                   COMPLETE — READY
013-B AUTHORITY / CORPUS BASELINE                 COMPLETE — PASS
013-C CONTEXT / JUDGE ENTRY MAPPING               COMPLETE — PASS
013-D ORGANIZER PREPARATION MAPPING               COMPLETE — PASS
013-E ACTIVE EVALUATION MAPPING                   COMPLETE — PASS
013-F AUTHORITY / CORRECTION MAPPING              COMPLETE — PASS
013-G LIVE OPS / RECONCILIATION MAPPING           COMPLETE — PASS
013-H AWARD / OFFICIALITY MAPPING                 COMPLETE — PASS
013-I REPRESENTATION / RELEASE MAPPING             COMPLETE — PASS
013-J ACCESSIBILITY / RECOVERY MAPPING             COMPLETE — PASS
ACCESSIBILITY-RESILIENCE OWNER REWRITTEN           YES
STATUS-FEEDBACK-RECOVERY OWNER REWRITTEN           YES
ACCESSIBLE PATH == ALTERNATE AUTHORITY MODEL       PROHIBITED
RESPONSIVE LAYOUT HIDES SEMANTIC BLOCKER           PROHIBITED
ASSISTANCE == AUTHORSHIP TRANSFER                  PROHIBITED
DEVICE/SESSION POSSESSION == ACCESS                PROHIBITED
LOCAL DRAFT == CONFIRMED AUTHORITY                 PROHIBITED
UNKNOWN RESULT == SUCCESS                          PROHIBITED
RETRY CREATES DUPLICATE DOMAIN EFFECT              PROHIBITED
RECOVERY OVERWRITES NEWER AUTHORITY                PROHIBITED
PAPER FALLBACK CREATES SECOND EVALUATION           PROHIBITED
GENERIC STATUS COLLAPSES AUTHORITY DIMENSIONS      PROHIBITED
WITHDRAWAL == EXTERNAL COPY DISAPPEARANCE          PROHIBITED
PHASE-010 REOPEN REQUIRED                          NO
PHASE-011 REOPEN REQUIRED                          NO
PHASE-012 REOPEN REQUIRED                          NO
NEXT                                                013-K
ARCHITECTURE / IMPLEMENTATION                      SUSPENDED
```

# 1. Governing semantic-parity rule

Accessibility, responsive presentation, degraded operation and recovery may change **interaction mechanics, representation density, capture channel, connectivity assumptions or timing**.

They may not change the domain meaning of the operation being attempted.

```text
ordinary path semantics
  = accessible path semantics
  = responsive path semantics
  = degraded/recovery path semantics
  = paper/assisted path semantics
```

where the same domain action is available.

A degraded path may legitimately make an action unavailable. It must not offer a weaker substitute that quietly changes authority.

# 2. Accessibility is not a product mode

Accessibility is a cross-cutting representation obligation over PF-01, not another product variant or lifecycle state.

Core operations should reasonably support WCAG 2.2 AA-oriented interaction and must not require any of the following as the sole semantic path:

- mouse;
- hover;
- camera/QR scanning;
- gesture-only control;
- color-only distinction;
- one device orientation;
- fine-pointer precision.

Keyboard, touch, nonvisual interaction, large text and alternate input must reach equivalent legitimate domain actions and explanations where those actions are available.

# 3. Semantic meaning cannot depend on visual treatment

Status, authority and disclosure meaning must not be conveyed only by:

- color;
- icon shape without accessible meaning;
- spatial position;
- animation;
- hover text;
- visual grouping alone.

The experience must expose the semantic subject and state strongly enough that an accessible presentation can distinguish, for example:

```text
Scorecard Draft
Scorecard Finalized
Evaluation Obligation Outstanding
Competition Event Completed
Competition Finalized
Outcome Declaration Affected
Export Stale
Publication Withdrawn
```

These are not interchangeable forms of a generic `complete` or `inactive` state.

# 4. Responsive representation preserves consequence hierarchy

Narrow/mobile presentation may progressively disclose detail but cannot hide the information needed to understand a consequential action.

A responsive path should preserve a coherent order such as:

```text
subject / current authority
  → material warning or blocker
  → basis / explanation
  → legitimate action
  → consequence / confirmation
```

This is an explanation obligation, not a prescribed component layout.

Organizer dense views may collapse summaries or tables, but material blockers, uncertainty and authority consequences must remain discoverable before the related high-consequence action.

Judge work remains capable of phone-primary completion without changing Rubric, obligation, Scorecard or Finalization semantics.

# 5. Accessible assistance does not transfer authority

Assistive technology and legitimate human assistance may help a user perceive, navigate or enter information.

They do not change who owns semantic intent.

Examples:

```text
assistance with navigation
  != Organizer becomes Judge

assistance entering Judge-spoken content
  != assistant authors judgment

screen-reader / switch / alternate input
  != different Scorecard semantics
```

Where a human actor materially captures content on behalf of another authority, actor-versus-represented-authority distinctions from 013-F apply. Ambiguous semantic intent may not be inferred merely to complete an accessible path.

# 6. Context must be re-established after interruption/device change

Resume after interruption or device replacement re-establishes the current context rather than trusting stale navigation state.

At minimum, the protected operation is interpreted against current:

```text
Identity
+ Participation / capacity
+ Competition
+ target resource
+ Access decision
+ authoritative resource state
```

A previous route, browser session, QR, cached screen or device possession does not prove current Access.

Shared-device handoff must not expose the prior participant's private state merely because the same hardware remains in use.

# 7. Resume converges on existing logical work

For Judge evaluation:

```text
interruption / device replacement / retry
  → resume or recover the same logical Scorecard for the same obligation
  != new evaluation weight
```

The one-logical-Scorecard invariant applies across accessible, online, degraded, paper and recovered traces.

Likewise, retrying other high-consequence operations must not be presented as permission to duplicate semantic effects such as:

- Award conferral;
- Competition Finalization;
- Outcome Declaration;
- Export generation where identity/currentness matters;
- Publication release.

Exact duplicate-prevention realization is downstream, but user-visible recovery must assume convergence rather than intentional duplication.

# 8. Local/degraded working state is not confirmed authority

Where disconnected or partially connected working continuation is supported, the representation must distinguish at least:

```text
local / device-held working state
server/application-confirmed persisted working state
confirmed authoritative domain state
```

For example:

```text
local Scorecard Draft exists
  != Draft persistence confirmed
  != Scorecard Finalized
  != obligation Satisfied
```

A local calculation or locally rendered representation likewise cannot be presented as current authoritative Aggregate, official Outcome Declaration, Current Export or Published Publication unless that authority is actually confirmed.

# 9. Paper fallback preserves one model

Full digital failure may move evaluation capture to identified paper evidence.

It does not create a separate judging model.

Preserve 013-F semantics:

```text
same Team
same Evaluation Occurrence
same Evaluation Obligation
same Judge semantic author
same exact Evaluation Basis
same logical Scorecard
same evaluation weight
```

Paper transcription remains non-authoritative until source fidelity and completed/committed Judge intent are established under current policy.

If an electronic Draft also exists, paper/electronic traces reconcile to the same logical evaluation rather than contributing twice.

# 10. Degraded operation may reduce capability, not semantics

When the application cannot safely establish prerequisites for a high-consequence operation, the legitimate degraded behavior may be **unavailable now**.

Examples may include inability to confirm:

- current Access;
- exact authoritative basis;
- whether Finalization already succeeded;
- whether an exception was accepted;
- whether Competition closeout succeeded;
- whether an Export was generated/current;
- whether Publication was released/withdrawn.

The experience must explain the known limitation and preserve work where possible rather than offering a lower-authority shortcut.

# 11. Unknown authoritative result is a first-class state

A request can be attempted without the application knowing its authoritative outcome.

The mapping must distinguish:

```text
not attempted
in progress / pending
result unknown
confirmed success
confirmed rejection/failure
```

`result unknown` is not success and is not necessarily failure.

This applies to high-consequence operations across Phase 013, including:

- Scorecard Finalization/amendment/capture correction;
- governed exception acceptance;
- Award conferral/correction;
- Competition Finalization + Outcome Declaration;
- successor declaration confirmation;
- Export generation/revalidation;
- Publication publish/withdraw/supersede.

# 12. Retry and reconciliation rule

After uncertainty, retry/recovery must first determine or reconcile against current authoritative state where possible.

The semantic goal is:

```text
same intended operation
  + current authority check
  → converge on one legitimate result
```

not:

```text
uncertainty
  → assume failure
  → create duplicate semantic effect
```

If the current result remains unknowable, the experience continues to represent uncertainty and routes to legitimate escalation/recovery rather than inventing certainty.

# 13. Stale local state cannot overwrite newer authority

Recovery must compare local/degraded state with current authoritative state before applying pending changes.

A stale local Draft, cached screen or queued intent cannot silently overwrite:

- a newer Scorecard Version;
- terminal obligation state;
- corrected/invalidation state;
- Award correction;
- current/successor Outcome Declaration;
- Export currentness/successor relation;
- Publication withdrawal/supersession.

Where a conflict exists, the user-visible recovery path must preserve the newer authority and explain the local work/conflict strongly enough to choose a legitimate next action.

# 14. Status is multidimensional

MUDAC must not collapse independent meanings into one generic `status` badge.

Relevant dimensions include, as applicable:

- lifecycle/state of the subject itself;
- work responsibility state;
- Draft versus authoritative state;
- persistence/confirmation confidence;
- validity/eligibility;
- currentness/currency/version lineage;
- readiness;
- warning/blocker/exception/correction condition;
- Access/disclosure posture;
- Publication distribution state;
- downstream transport/delivery observation.

Only dimensions meaningful to the current subject need be shown, but they must remain conceptually separate.

# 15. Use subject-qualified finality language

Ambiguous words such as `done`, `complete`, `submitted`, `saved`, `final`, `published`, `resolved` or `current` should be qualified when multiple owners could plausibly be meant.

Preserve examples such as:

```text
Draft complete != Scorecard Finalized
Evaluation Occurrence Complete != obligation Satisfied
Competition Event Completed != Competition Finalized
Ranking Ready != official
Competition Finalized != Published
Outcome Declaration Affected != Superseded
Export Current != Publication Published
Publication Published != delivered
Acknowledged != source resolved
```

A status label must not imply a stronger postcondition than the owner actually established.

# 16. Working persistence feedback is distinct from semantic commitment

For low-consequence working edits, feedback may explain whether work is locally held, synchronizing or confirmed persisted.

That feedback must not be confused with semantic commitment.

Examples:

```text
Draft saved
  != Finalize Evaluation succeeded

Export request recorded
  != Export generated

Publication request sent
  != Publication Published
```

Where `saved` is used, the represented persistence scope should be clear enough to avoid implying authority establishment.

# 17. High-consequence success requires authoritative confirmation

For actions that create/succeed/invalidate meaningful authority, success feedback must correspond to confirmed authoritative state rather than optimistic local UI state.

The representation should make clear enough:

- what action was attempted;
- what authority/result is confirmed;
- what remains unchanged;
- any downstream step that is still separate.

Examples:

```text
Scorecard Finalized
  → obligation Satisfied
  != Coverage automatically Satisfied

Competition Finalized + Outcome Declaration Current
  != Publication

Publication Published
  != delivery/viewing success
```

# 18. Confirmation friction follows semantic consequence

Higher-consequence actions should make the target and consequence intelligible before commitment.

The mapping does not prescribe dialogs, but it does require semantic clarity for operations such as:

- invalidate evidence/occurrence;
- establish successor responsibility;
- revoke/correct Award;
- Finalize Competition & Declare Outcome;
- confirm successor Outcome Declaration;
- withdraw Publication;
- publish a successor representation.

Corrective actions should use owner-specific verbs rather than vague destructive labels such as `reset`, `force`, `fix` or `delete` when those terms obscure actual history/authority consequences.

# 19. Recovery explanation grammar

When recovery is needed, the experience should explain, where relevant:

1. **attempted action** — what the user tried to do;
2. **definitely known state** — authoritative facts that are confirmed;
3. **uncertain state** — what is not currently known;
4. **preserved work** — local/Draft/paper work that still exists;
5. **current authority discovered on reconnect** — including newer versions or terminal state;
6. **legitimate next action** — resume, retry after reconciliation, discard local duplicate trace, correct, escalate, or wait for source recovery as appropriate;
7. **privacy/disclosure posture** — what may safely be shown while recovering.

This is semantic recovery guidance, not a prescribed incident-management workflow.

# 20. Privacy/disclosure survives degraded paths

Connectivity loss, paper fallback, shared devices, print, screenshots, alternate input or recovery interfaces do not weaken disclosure rules.

Preserve:

```text
technical recovery capability
  != broader Access
  != broader audience disclosure
  != semantic authority
```

Judge-safe Team identity, peer-evidence non-disclosure, private Notes, Organizer-sensitive information and Export AudienceProfile rules remain in effect.

A degraded path may legitimately show less information when safe disclosure cannot be established; it may not expose more merely to keep operation moving.

# 21. Export/Publication parity under degraded/recovery conditions

013-I semantics survive alternate paths:

```text
Export currency != Publication state
Publication Published != delivery
withdrawal/supersession != external-copy disappearance
recipient possession != Access/current release authority
```

A local download or previously printed artifact cannot be relabeled `Current` solely because it is available during an outage.

An uncertain publish/withdraw request remains uncertain until Publication authority is confirmed.

# 22. Accessibility and degraded operation do not change explanation order

The global Phase-013 rules remain:

```text
dependence order != navigation order
synchronization chain != mandatory wizard
```

Accessible/responsive/degraded presentation may reorder or progressively disclose information for usability, but must preserve the semantic prerequisites and consequences of the action.

A missing visual step does not waive a source condition; an alternate input path does not create a different synchronization.

# 23. Mapping risks closed or reduced

013-J closes/reduces:

- **MAP-R06** — persistence versus authority collapse: working persistence, uncertainty and semantic commitment separated;
- **MAP-R12** — accessible/degraded semantic parity: explicitly mapped across all completed Experience owners;
- **MAP-R13** — route/device/QR possession cannot create Access or authority;
- **MAP-R15** — technical recovery privilege cannot become domain authority;
- cross-cutting uncertainty risk — unknown result cannot be promoted into success;
- duplicate-effect risk — retry/device/paper paths converge rather than multiply authority/evidence.

No new Concept, synchronization or dependence defect requires upstream reopen.

# 24. 013-K handoff

013-K inherits a now-complete set of subject owners from 013-C through 013-J.

It must audit whole-experience consistency across:

- explanation order;
- terminology;
- role/capacity views;
- direct/coordinated/system application action representation;
- current versus historical state;
- accessible/degraded parity;
- PF-01 profile consistency;
- remaining cross-cutting `action-authority-traceability.md` evidence;
- duplicate or superseded Experience material.

013-K should not introduce a new workflow architecture. Its purpose is whole-experience integrity and mapping consistency.

# Exit decision

```text
013-J: COMPLETE — PASS
accessibility mapping: CURRENT / ACCEPTED
degraded operation mapping: CURRENT / ACCEPTED
status/feedback mapping: CURRENT / ACCEPTED
recovery mapping: CURRENT / ACCEPTED
semantic parity across 013-C–I: REQUIRED
unknown authority != success: LOCKED
retry/recovery convergence: LOCKED
privacy/disclosure parity: LOCKED
013-K: NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
implementation readiness: NOT READY
implementation authorization: NOT YET
```
