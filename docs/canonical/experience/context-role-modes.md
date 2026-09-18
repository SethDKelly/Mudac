---
type: Experience Contract
title: Experience Context and Participation Modes
description: Current user-visible operating-context semantics for Identity, Competition-scoped Participation, capacity modes, contextual Access, multi-capacity isolation and historical context.
status: stable
tags: [experience, mapping, context, participation, access, role, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-C-context-identity-participation-access-bias-control-judge-entry-mapping.md
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-K-whole-experience-explanation-order-cross-role-profile-consistency-mapping-integrity-audit.md
  - resource: ../concepts/identity.md
  - resource: ../concepts/participation.md
  - resource: ../concepts/access.md
  - resource: ../synchronizations/competition-participation-access.md
  - resource: ../policies/anonymity-disclosure.md
  - resource: ../invariants/current-vs-historical-truth.md
---

# Purpose

Define how MUDAC represents a human's current Competition/capacity context without allowing navigation, role-mode selection, session state or technical privilege to create semantic authority.

# Canonical context model

```text
Identity continuity
  → one current Participation context
  → Competition + capacity
  → fresh Access decision for each protected read/action
  → role-specific operational subject/task context
```

This is an explanation model, not a mandatory navigation sequence.

Where ambiguity could change a protected action or disclosure, the experience must make sufficiently clear:

- which Competition is current;
- which Participation/capacity is current;
- whether that Participation is current enough for the intended work;
- which protected subject/resource is being acted on where relevant;
- which disclosure posture applies;
- whether current Access permits or denies the protected operation when that distinction matters.

# Identity is not active capacity

Identity answers who the human is and may persist across Competitions.

A recognized/verified Identity does not imply:

- current Competition Participation;
- current Judge/Organizer capacity;
- Panel membership;
- current Access;
- evaluation responsibility;
- semantic authorship.

Historical attribution remains attached to stable Identity even after current Participation or Access ends.

# Participation modes

Labels such as `Judge mode` and `Organizer mode` are permitted as organizational language when they clearly represent **one current Competition-scoped Participation context**.

A mode is not an authority-owning state.

Selecting or navigating to a mode does not:

- enroll or activate Participation;
- create or restore Access;
- create Panel membership;
- create Evaluation Occurrence participation or Evaluation Obligation;
- change Competition lifecycle;
- transfer semantic authorship.

A stale route, cached mode or previously visible control is not evidence that current authority still exists.

# Multi-capacity isolation

The same Identity may hold multiple current Participations, including Judge and Organizer capacities in one Competition.

Capabilities never union across those Participations.

```text
current Judge context
  → Judge Participation facts + Judge disclosure posture

current Organizer context
  → Organizer Participation facts + Organizer disclosure posture

Judge + Organizer capability union
  → prohibited
```

Switching context selects another already-legitimate Participation for representation. It does not mutate either Participation.

Protected reads/actions after a switch use fresh current Access facts.

Where disclosure materially changes, destination Competition/capacity must be intelligible before or at the point protected information becomes visible.

# Disclosure posture is part of context meaning

During blinded judging, Judge context uses **Alias + Division**.

Institution/administrative Team identity and optional Team Name remain hidden by default. Judge context also preserves Judge Independence by withholding peer Scorecards/Notes, Aggregate, Coverage, Rank and standings during ordinary judging.

An Identity that may legitimately see Organizer-sensitive information in Organizer context does not inherit that visibility in Judge context.

Capacity switching therefore changes not just navigation but the semantic disclosure context supplied to Access.

# Access is contextual, not a mode property

A visible mode or Participation does not itself prove that a protected operation is permitted.

Access is evaluated from current principal, Competition/capacity, lifecycle, relationship, target/resource, purpose and other applicable facts.

A denial/unavailable action should be understandable enough to identify the legitimate semantic category or next action where doing so does not leak protected information.

Generic Access administration is not a user-facing role-mode control.

# Operational contexts are not lifecycle states

Organizer work areas such as Preparation, Live Operations, Reconciliation/Outcomes, Materials/Publication and History organize attention. They do not create Competition lifecycle values or authority.

Judge areas similarly organize entry, current work and permitted history. They do not create evaluation responsibility.

`Reconciliation` remains work/process context, not a Competition state.

# Current versus historical context

Current and historical contexts remain distinguishable whenever history could be mistaken for current authority.

```text
returning Identity != current Participation
historical Participation != current Participation
past Panel membership != current Panel membership
past Access != current Access
historical evaluation context != current work authority
```

Historical inspection may be legitimate without restoring ordinary live-event capability.

# Shared-device / stale-context rule

After interruption, device handoff or context switch, stale protected state must not continue to appear as though it belongs to the newly current Identity/Participation context.

Before consequential protected interaction resumes, enough current Identity / Participation / Competition / resource context must be re-established to avoid ambiguity.

Session clearing, authentication UX, storage and timeout realization remain downstream implementation concerns.

# Technical support boundary

Technical administration/support privilege is not Judge or Organizer Participation and cannot be represented as Competition decision authority.

Support may restore technical operation or help re-establish legitimate context, but it cannot manufacture Judge authorship, Organizer authority, disclosure permission or historical Participation.

If a support actor separately holds legitimate Competition Participation, that Participation is a distinct context subject to the same no-capability-union rule.

# Structural representation obligations

The mapping requires these structural properties:

- current Competition/capacity is discoverable where ambiguity matters;
- Identity and Participation are not collapsed into one generic `account/role` state;
- Judge-safe and Organizer-sensitive contexts remain distinguishable;
- multi-capacity contexts do not imply merged capability;
- current and historical state are not visually/linguistically conflated;
- action availability cannot be inferred merely from navigation position.

No exact header, breadcrumb, tabs, route tree, menu, page hierarchy or component structure is prescribed.

# Related mapping

- Judge entry/readiness → [Judge Entry, Participation & Readiness Mapping](judge-onboarding.md);
- active evaluation → [Judge Active Evaluation Mapping](judge-evaluation.md);
- Organizer preparation → [Organizer Competition Preparation & Readiness Mapping](organizer-preparation.md);
- live operations → [Organizer Live Operations & Remaining Work Mapping](live-operations.md);
- accessibility/recovery → [Accessibility, Responsive & Degraded-Operation Mapping](accessibility-resilience.md) and [Status, Feedback & Recovery Mapping](status-feedback-recovery.md);
- whole-experience action/explanation integrity → [Whole-Experience Action, Explanation & Authority Traceability](action-authority-traceability.md).

See [Phase 013 Mapping Authority Baseline](mapping-authority-baseline.md), [Access](../concepts/access.md), [Participation](../concepts/participation.md), [Anonymity & Disclosure](../policies/anonymity-disclosure.md), and [Current vs Historical Truth](../invariants/current-vs-historical-truth.md).
