---
type: Phase Design Record
title: 013-C — Context, Identity, Participation, Access, Bias-Control & Judge Entry Mapping
description: "Maps current MUDAC person/context semantics into user-visible operating-context, multi-capacity, disclosure, access, readiness and Judge-entry obligations without allowing role modes, navigation or support privilege to manufacture domain authority."
status: stable
tags: [phase-013, jackson, mapping, context, identity, participation, access, bias-control, judge-entry]
sources:
  - resource: 013-B-experience-corpus-reconciliation-terminology-mapping-authority-canonical-ownership-baseline.md
  - resource: ../canonical/experience/mapping-authority-baseline.md
  - resource: ../canonical/concepts/identity.md
  - resource: ../canonical/concepts/participation.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/concepts/alias.md
  - resource: ../canonical/concepts/panel.md
  - resource: ../canonical/synchronizations/competition-participation-access.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/synchronizations/application-action-surface-composition.md
  - resource: ../canonical/policies/anonymity-disclosure.md
  - resource: ../canonical/invariants/judge-independence.md
  - resource: ../canonical/experience/context-role-modes.md
  - resource: ../canonical/experience/judge-onboarding.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/007/concept-mapping-contract.md
---

# Purpose

Map how a person understands **who they are, which Competition/capacity they are acting under, what they may currently perceive or invoke, and whether they are prepared to enter Judge work** without allowing interface organization to become semantic authority.

013-C is the first substantive Phase-013 mapping workstream. It rewrites the natural Experience owners for operating context and Judge entry under the converged Identity / Participation / Access / Panel / Evaluation Occurrence / Evaluation Obligation model.

It does **not** define the detailed evaluation-task representation, scoring basis, Scorecard Draft/Finalization experience, Organizer preparation workspace, live-operations exception views, correction/history experience, frontend navigation architecture, authentication implementation or route/session mechanics.

# Decision

**COMPLETE — PASS. Proceed to 013-D.**

```text
013-A START GATE                         COMPLETE — READY
013-B AUTHORITY / CORPUS BASELINE       COMPLETE — PASS
013-C CONTEXT / JUDGE ENTRY MAPPING     COMPLETE — PASS
CONTEXT-ROLE OWNER REWRITTEN             YES
JUDGE-ONBOARDING OWNER REWRITTEN         YES
IDENTITY / PARTICIPATION / ACCESS SPLIT  PRESERVED
MULTI-CAPACITY CAPABILITY UNION          PROHIBITED
JUDGE-SAFE DISCLOSURE POSTURE            MAPPED
READY-TO-JUDGE WRITABLE STATE            PROHIBITED
PANEL MEMBERSHIP AS RESPONSIBILITY       PROHIBITED
SUPPORT PRIVILEGE AS DOMAIN AUTHORITY    PROHIBITED
PHASE-010 REOPEN REQUIRED                NO
PHASE-011 REOPEN REQUIRED                NO
PHASE-012 REOPEN REQUIRED                NO
NEXT                                     013-D
ARCHITECTURE / IMPLEMENTATION            SUSPENDED
```

# 1. Governing conceptual separation

The user-visible model must preserve:

```text
Identity
  = who the human is / continuity

Participation
  = this human taking part in this Competition in one capacity

Access
  = whether this current principal/context may perform or perceive this protected thing now

Panel
  = reusable intended evaluator grouping

Evaluation Occurrence
  = actual bounded evaluation event/history

Evaluation Obligation
  = one evaluator's current/historical responsibility
```

None may be represented as a synonym for another.

The principal mapping invariant is:

> **A person may be recognized, enrolled, checked in, assigned to a Panel, shown a Judge work area, and still not possess authority for a particular protected evaluation action.**

Conversely, a valid current protected action must not be hidden merely because the representation is organized differently from the conceptual graph.

# 2. User-visible operating context

Every protected operation is interpreted under one explicit current Participation context.

The experience must make sufficiently perceptible, whenever ambiguity could change meaning:

- current human/Identity continuity;
- current Competition;
- current Participation capacity such as Judge or Organizer;
- whether that Participation is current/eligible enough for the intended work;
- target/resource context where needed;
- protected disclosure posture where it affects what can be seen;
- current Access denial/permission consequence where material.

This is a **semantic context requirement**, not a prescribed header, breadcrumb, route tree, account menu or screen shell.

The natural conceptual order is:

```text
Identity continuity
  → current Participation selection
  → Competition/capacity context
  → fresh Access evaluation per protected read/action
  → role-specific operational subject/task context
```

It is not a mandatory click sequence.

# 3. Role mode is a representation of Participation context

`Judge mode` and `Organizer mode` remain useful user-facing organizational language, but they are not Concepts and do not grant authority.

A role/capacity mode means:

> **the application is currently presenting work under one explicit Participation context and its corresponding disclosure posture.**

Therefore:

- selecting Judge mode does not enroll/activate Judge Participation;
- selecting Organizer mode does not create Organizer Participation;
- switching modes does not mutate either Participation;
- a visible mode does not satisfy Access;
- a stale/cached mode does not preserve Access after underlying facts change;
- possession of a route/link/QR code cannot establish mode authority;
- mode presentation may disappear while historical Participation remains true.

Where the same Identity has multiple current Participations, the current capacity must be sufficiently clear before a consequential action or protected disclosure can be misunderstood.

# 4. Multi-capacity identities

One Identity may legitimately have more than one Participation, including Judge and Organizer Participations in the same Competition.

The experience must never union their capabilities.

```text
Identity I
  + Judge Participation J
  + Organizer Participation O

current context = J
  → Judge-supplied context facts only

current context = O
  → Organizer-supplied context facts only

J ∪ O capability union
  → prohibited
```

A context switch is therefore representational selection of another already-legitimate Participation context. Protected operations after the switch use fresh current Access facts.

The switch should make the destination Competition/capacity and materially changed disclosure posture intelligible before or at the point where protected information/action meaning changes.

No exact modal, menu or confirmation implementation is prescribed.

# 5. Judge-safe disclosure posture

During blinded judging, Judge-facing competitor identity is **Alias + Division**.

Institution/administrative Team identity and optional Team Name remain hidden by default. Peer Scorecards/Notes, Aggregate, Coverage, Rank and standings remain unavailable during ordinary judging under Judge Independence.

013-C establishes the context-level mapping rule:

> **Judge capacity implies a Judge-safe disclosure posture, not merely a different navigation area.**

A Judge/Organizer multi-capacity Identity must not inherit Organizer-sensitive competitor identity or outcome information while operating under Judge Participation merely because the same human could see it in another legitimate capacity.

Switching to an Organizer context may legitimately change disclosure only when the Organizer Participation and current Access independently permit it.

If protected information was actually exposed, a later role switch or Access denial cannot represent that exposure as though it never happened. Consequence/correction semantics remain attributable under current policy.

# 6. Competition entry and Identity continuity mapping

Judge entry must answer the semantic questions:

```text
Which Competition am I entering?
Which human Identity is being used?
Is that Identity sufficiently established/reverified for this event context?
Do I have a current Judge Participation for this Competition?
What current Participation state/attributes still require attention?
```

A first-time volunteer may establish and verify Identity. A returning volunteer may reuse Identity continuity and reverify as required.

The representation must not imply:

- returning Identity = current Judge Participation;
- successful authentication = current Competition authority;
- prior Competition history = current Participation;
- prior Panel membership = current Panel membership;
- prior Access = current Access.

Identity recovery/reverification feedback should confirm Identity continuity or the need for further action without implying event authorization that has not been established.

Exact authentication proof, provider, session or credential mechanics remain outside Phase 013.

# 7. Judge Participation mapping

A Judge must be able to understand the current Competition-specific Participation independently from Identity.

Material state may include, as applicable:

- enrollment/current Judge capacity;
- check-in state;
- current-event declared expertise/profile attributes;
- active/completed/withdrawn state;
- whether restoration or another authorized action is required.

The experience may summarize this as event participation status, but it must not hide the distinction between stable Identity and event-scoped Participation.

Relevant direct/coordinated application actions remain the Phase-011 action surface:

| Semantic intent | Action class | Mapping obligation |
| --- | --- | --- |
| establish/verify/reverify/recover Identity | D | expose only when current entry context requires it; confirm Identity result without implying Participation/Access |
| enroll Judge Participation | D | target Competition and Judge capacity must be unambiguous |
| check in | D | confirm Participation state; check-in is not Access or obligation creation |
| update current-event declared attributes | D | make scope/current-event meaning clear |
| activate Participation | C | represent blocking readiness/eligibility reason when unavailable; activation is not Competition activation |
| withdraw | D / consequential | make Competition/capacity and consequence clear; withdrawal is not Access edit |
| restore | C / exceptional | make restored Participation distinct from restored Access/Panel/work |
| Access.check | P/S guard | never expose as generic business control; protected action availability/denial reflects current result |

# 8. Panel assignment mapping at entry

Panel is intended grouping, not actual judging participation or responsibility.

Judge entry may show a current Panel assignment when operationally useful, but it must communicate it as planning/context rather than as proof that:

- the Judge will participate in every Evaluation Occurrence involving that Panel;
- an Evaluation Occurrence has begun;
- an Evaluation Obligation exists;
- a Scorecard exists;
- the Judge currently has Access to a specific evaluation artifact.

If no Panel is currently assigned, the experience must not invent a universal blocked state unless current policy/readiness actually requires Panel assignment for this Competition profile.

This preserves PF-01 profile flexibility and avoids turning the incumbent Panel workflow into a product-family requirement.

# 9. `Ready to Judge` mapping

`Ready to Judge` remains a **derived explanatory projection**, not a Concept, Participation lifecycle value or editable checklist item.

Its semantic question is:

> **Is this Judge currently prepared to enter ordinary judging work for this Competition, and if not, which authoritative source condition still prevents that preparation?**

The projection may compose current facts such as:

- legitimate Identity continuity/reverification;
- current Judge Participation for the Competition;
- required check-in/activation or event-specific declared attributes;
- required Organizer-governed grouping/preparation facts where policy makes them relevant;
- Competition lifecycle/readiness facts relevant to Judge entry;
- current contextual capability/disclosure expectations.

It must not claim that:

```text
Ready to Judge
  = Panel membership
  = occurrence participant
  = Evaluation Obligation
  = Scorecard existence
  = permanent Access grant
```

The representation should explain the source of a blocking condition and point toward the legitimate source action when the current actor can perform one. It must not offer a generic `Set Ready`/`Mark Ready to Judge` control.

A displayed ready projection is not a substitute for fresh Access evaluation when a protected operation is actually attempted.

# 10. Action availability and denial

The experience should distinguish at least these semantic cases when they change the legitimate next action:

- no current Participation for this Competition;
- Participation exists but has not reached the required state;
- Participation has completed/withdrawn;
- Competition lifecycle currently prevents ordinary Judge work;
- a protected resource/action is denied by current Access;
- Judge entry is prepared but no Evaluation Obligation/work currently exists;
- current work exists but belongs to a later mapping workstream.

A generic disabled control or `Unauthorized` message is insufficient when it would make the user infer the wrong semantic owner or next action.

At the same time, denial explanations must not leak protected information. The experience may explain the category of denial without revealing the hidden resource or identity that policy protects.

# 11. Entry mechanisms do not create authority

QR codes, event codes, deep links, invitations, bookmarked routes, device possession, authentication success and previously rendered pages may accelerate discovery/navigation.

They do not create:

- Identity continuity by themselves;
- Participation;
- check-in or activation;
- Panel membership;
- Evaluation Occurrence participation;
- Evaluation Obligation;
- Access;
- Judge authorship.

A non-camera path remains semantically required because camera/QR is an optional navigation mechanism rather than authority.

The exact alternate input/UI implementation belongs downstream; semantic parity is re-audited in 013-J.

# 12. Shared-device and stale-context obligations

Where device handoff, interruption or context switching could expose another person's or another capacity's protected state, the representation must not leave stale private context appearing current.

Before consequential protected interaction resumes, the experience must re-establish enough current Identity / Participation / Competition / resource context to avoid ambiguity.

This establishes the semantic obligation only. Session clearing, storage, timeout, reauthentication and device-management implementation remain downstream.

# 13. Support / technical-administrator mapping

Technical administration/support privilege is not a substitute Participation and does not create Judge/Organizer semantic authority.

Support may legitimately help recover access to the application, re-establish technical context, diagnose a failure or invoke an already-authorized technical recovery mechanism.

The experience must not represent support capability as permission to:

- enroll/activate themselves as Judge or Organizer without legitimate Participation semantics;
- author Judge judgment;
- accept competition-policy exceptions merely because of technical privilege;
- finalize outcomes;
- expose protected Team identity outside permitted disclosure;
- restore a user's prior domain authority merely by restoring a session.

If a support actor also independently holds a legitimate Competition Participation, that Participation is a separate semantic context subject to the same no-capability-union rule.

# 14. Current versus historical context

Historical Participation, prior Panel membership, prior Judge work and prior Competition access may be shown for legitimate inspection/recovery purposes, but must not appear current merely because the same Identity is recognized.

Representations must preserve:

```text
returning human identity
  != returning event authority

historical Participation
  != active Participation

past Panel membership
  != current grouping

past Access
  != present permission
```

Detailed current-versus-historical evaluation/correction mapping remains in 013-F.

# 15. Structural representation constraints

013-C establishes only semantically necessary structural constraints:

1. current Competition and current capacity must be discoverable where ambiguity can cause a protected action/disclosure error;
2. Identity continuity and Competition Participation status must not be collapsed into one generic `account/role` state;
3. Judge-safe and Organizer-sensitive disclosure postures must remain distinguishable;
4. multi-capacity contexts must not visually/linguistically imply capability union;
5. derived `Ready to Judge` must be distinguishable from authoritative source state and actual evaluation responsibility;
6. historical context must not be visually indistinguishable from current context;
7. denial/blocking explanations should identify the semantic category/source without leaking protected information.

No exact page hierarchy, tabs, top bar, drawer, wizard, route or component is authorized by these constraints.

# 16. Mapping-risk disposition

| Risk | 013-C result |
| --- | --- |
| MAP-R03 raw Concept action exposed generically | **Partially closed** — Access generic grant/revoke remains X; entry maps only current D/C surface |
| MAP-R04 Identity / Participation / Access collapse | **Closed for context/entry** |
| MAP-R05 Panel / participant / responsibility / evidence collapse | **Closed for entry boundary; detailed evaluation mapping continues 013-E** |
| MAP-R11 PF-01 profile mistaken for product variant | **Closed for Panel/entry optionality** |
| MAP-R12 accessibility/degraded parity loss | **Constraint established; final closure 013-J** |
| MAP-R13 navigation/role mode appears to create authority | **Closed** |
| MAP-R15 support privilege appears to create domain authority | **Closed for context/entry; rechecked 013-J/K** |

No new mapping risk requires upstream redesign.

# 17. Canonical owner updates

013-C rewrites and accepts as current mapping authority for their subjects:

- `docs/canonical/experience/context-role-modes.md`;
- `docs/canonical/experience/judge-onboarding.md`.

`action-authority-traceability.md` remains cross-cutting admitted evidence pending incremental revalidation through 013-K. 013-C does not rewrite its evaluation/outcome examples prematurely.

The Mapping Authority Baseline and Experience index are advanced to record these two accepted owners.

# 18. Reopen audit

```text
missing Identity semantics:            NO
missing Participation semantics:       NO
missing Access semantics:              NO
missing Panel/Occurrence seam:         NO
missing application action:            NO
incorrect PF-01 scope assumption:      NO
purpose contradiction:                 NO
Phase-010 reopen:                      NO
Phase-011 reopen:                      NO
Phase-012 reopen:                      NO
```

The existing conceptual model is sufficient. The work was representation mapping, not Concept repair.

# 19. Exclusions / downstream handoff

013-C intentionally leaves these for later workstreams:

- Organizer preparation/configuration/readiness → 013-D;
- exact evaluation task, occurrence/obligation, Rubric basis, Scorecard action/feedback → 013-E;
- amendment/correction/paper/history → 013-F;
- live exception/reconciliation state → 013-G;
- officiality/outcome declaration → 013-H;
- Export/Publication/external recipient → 013-I;
- full accessibility/degraded/status/recovery parity → 013-J;
- whole-experience terminology/authority consistency → 013-K.

# Current state

```text
013-A  COMPLETE — READY
013-B  COMPLETE — PASS
013-C  COMPLETE — PASS
013-D  NEXT
architecture authority: SUSPENDED
implementation planning: SUSPENDED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

# Next

Proceed to **013-D — Competition Preparation, Competitor/Panel/Rubric Setup, Readiness & Organizer Configuration Mapping**.
