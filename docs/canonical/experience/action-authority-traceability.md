---
type: Experience Contract
title: Experience Action, State & Authority Traceability
description: Cross-cutting contract requiring Judge and Organizer interaction semantics to trace to accepted Concept actions, synchronizations, derived projections, and current authority rather than inventing UI-owned product state.
status: stable
tags: [experience, traceability, authority, actions, synchronization]
sources:
  - resource: ../../003-conceptual-ux-architecture/003-J-phase-consolidation-ux-architecture-exit-review.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
  - resource: ../../007-design-refinement/007-C-cross-concept-synchronization-completeness-authority-seam-audit.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
  - resource: ../../007-design-refinement/007-E-end-to-end-scenario-exception-failure-adversarial-authority-validation.md
---

# Purpose

Keep interaction architecture subordinate to the accepted MUDAC Concept model.

Screens, routes, buttons, dialogs, work modes, status labels, exception rows, previews, recovery affordances, and client-side state may help a person understand or invoke product behavior. They do not independently own Competition truth, evaluation authorship, lifecycle, correction, official outcome, disclosure, or publication authority.

# Canonical contract

Every material Judge or Organizer interaction must be explainable as one or more of:

1. **Concept action invocation** — an authorized intent to perform an action owned by an accepted Concept;
2. **Concept query/read** — presentation of current or historical Concept state under current Access/disclosure rules;
3. **synchronization consequence** — a cross-Concept effect whose authority boundary and success semantics are owned by the canonical synchronization contract;
4. **derived projection** — readiness, Coverage, Aggregate, Rank, exception, currency, or similar computed state that remains subordinate to authoritative sources;
5. **working-state interaction** — non-authoritative Draft/editing behavior owned by the relevant Concept; or
6. **implementation-only interaction state** — focus, expansion, sorting, filtering, navigation, optimistic presentation, local transport state, or similar UI mechanics that create no domain authority.

If a material interaction cannot be classified this way, it is a design defect until an accepted semantic owner is established.

# Interaction does not create authority

A visible or enabled control is not proof that the action is currently authorized.

At execution time, consequential actions must still satisfy:

`Identity + Participation + Access + target state + relationship + Competition state/policy + action-specific preconditions`.

Frontend hiding, disabled controls, route guards, work-mode selection, possession of a URL, or completion of a confirmation dialog are experience mechanisms. They never substitute for the current semantic authority check.

Likewise, a successful click/tap is not itself authoritative success. Authority exists only when the owning Concept action and any authority-establishing synchronization have truthfully established their required postconditions.

# Work modes are organization, not lifecycle

Judge/Organizer modes and Organizer work areas such as Preparation, Live Operations, Reconciliation, Outcomes, Materials, Publication, and History organize attention and navigation.

They do not create extra Competition lifecycle values or generic workflow state.

Examples:

- `Reconciliation` is Organizer work over an Event Completed Competition, not a Competition lifecycle state;
- `Ready to Judge` is a derived projection over current Identity/Participation/Panel/Encounter/Access conditions, not a Participation or Competition action;
- `Exception resolved` is never authoritative merely because an exception row was dismissed or acknowledged.

# User-visible verbs must preserve semantic ownership

High-consequence interaction labels and confirmation language should identify the actual semantic action rather than collapse materially different actions behind a generic verb.

Examples that must remain distinguishable include:

- `Presentation complete` versus `Encounter complete`;
- `Save Draft`/working preservation versus `Finalize Scorecard`;
- `Begin amendment` versus ordinary editing;
- `Replace Panel member` versus one-Encounter participant adjustment;
- `Correct Division assignment` versus routine cohort reassignment;
- `Invalidate Encounter` versus delete/hide;
- `Complete event` versus `Finalize Competition`;
- `Generate Export` versus `Publish`;
- `Withdraw Publication` versus delete historical release.

Generic UI labels such as `Resolve`, `Fix`, `Done`, `Close`, or `Override` may be used only when the underlying semantic action and consequence remain unambiguous in context. They must not create a generic domain action that bypasses the owning Concept.

# Confirmation is intent evidence, not authority

Confirmation friction is an experience safeguard proportional to consequence. It may establish that the user deliberately requested an action, but confirmation alone does not satisfy the action's domain preconditions or establish its postconditions.

For example:

- confirming Scorecard Finalization does not make a failed/unknown Finalization successful;
- confirming Competition Finalization does not bypass unresolved finalization readiness;
- confirming Publication does not make an unvalidated disclosure profile permissible;
- confirming an invalidation does not grant an actor correction authority they do not otherwise possess.

# Derived projections are not editable sources

Readiness, Panel-composition warnings, Scorecard obligations, Coverage, Aggregate, Rank, finalization readiness, affected/stale indicators, and similar projections may drive attention and explain what blocks an action.

They are not independent editable records whose manual mutation can repair source truth.

An Organizer resolves an exception by acting on its authoritative source or by invoking an explicitly governed exception/correction action. Hiding, acknowledging, suppressing, or manually changing the projection cannot substitute for source correction.

Where policy permits an accepted exception, the exception authority must itself be explicit and must preserve the underlying observed shortfall or source facts.

# Judge interaction traceability

Judge interaction remains centered on:

`Identity/reverification → Participation → Access/context → Encounter → Scorecard Draft → explicit Finalization → Version/Provenance → optional controlled Amendment`.

Navigation between Teams/Encounters never changes the evaluated subject implicitly. Team Alias + Division context must remain sufficiently visible to prevent accidental cross-subject scoring.

Judge UI must not expose peer evaluation, Aggregate, Coverage, Rank, or standings as a convenience projection because disclosure itself would violate the accepted evaluation model.

After Event Completed, ordinary Judge private-evaluation interaction disappears because Access expires; a legitimate later amendment uses narrow reauthorization rather than restoring a general historical Judge mode.

# Organizer interaction traceability

Organizer interaction coordinates many Concepts without becoming a catch-all authority owner.

Preparation invokes source actions on Competition, Division, Team, Alias, Rubric, Award definition, Participation, Panel, Export/materials, and applicable policy configuration; readiness remains derived.

Live Operations invokes or coordinates Participation, Panel, Encounter, Access, Scorecard/paper-capture, correction, and Competition `completeEvent` semantics; urgency does not transfer Judge authorship.

Reconciliation/Outcomes primarily presents authoritative evidence and derived Coverage/Aggregate/Rank/finalization readiness, then invokes explicit source corrections, Award actions, and Competition `finalize` where authorized.

Materials/Publication invokes Export actions followed by separate Publication actions. Preview and generation do not establish distribution authority.

# Current versus historical interaction

UI presentation must preserve the temporal dimensions established by the canonical temporal/correction contract.

Current source state, historical occurrence state, superseded Version, invalidated evidence, replacement occurrence, affected/stale derived representation, latest declared official revision, and Publication distribution state must not be flattened into one convenient screen-level status.

An interaction operating on historical state must make clear whether it is:

- read-only historical inspection;
- correction of current source truth;
- amendment creating a successor Version;
- invalidation of retained evidence;
- creation/linking of a replacement occurrence;
- confirmation of a successor official outcome; or
- withdrawal/supersession of a Publication.

# Uncertainty and recovery

When the outcome of an authority-establishing action is unknown, the experience must expose uncertainty rather than quietly offering a fresh action that might duplicate authority.

Recovery first reconciles current authoritative state and then offers the legitimate next action under current preconditions.

A stale client cannot use its old enabled controls, prior route, cached role mode, or local Draft state to overwrite newer authority or bypass revoked Access.

# Accessibility and representation parity

Accessible, responsive, keyboard, nonvisual, narrow-screen, paper-assisted, and degraded experiences must expose the same semantic actions and authority distinctions.

A compact/mobile or assistive representation may reorganize interaction, but it must not omit a material consequence, turn a high-consequence action into an accidental gesture, or provide a weaker authorization/disclosure path.

# Design consequence

Downstream component, route, API, persistence, and application architecture should be able to trace every consequential interaction to its semantic owner without treating UI structure as domain structure.

No component hierarchy, page name, route, modal, wizard step, status badge, table row, or client state machine becomes a MUDAC Concept merely because implementation needs it.

See [Experience Context and Role Modes](context-role-modes.md), [Status, Feedback, Privacy and Recovery Grammar](status-feedback-recovery.md), [Access](../concepts/access.md), [Concept Synchronization Contracts](../synchronizations/concept-synchronizations.md), and [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md).
