---
type: Experience Contract
title: Organizer Live Operations & Remaining Work Mapping
description: Current Organizer mapping for event-day coordination, actual occurrence/obligation/Scorecard state, remaining Judge work, operational warnings/blockers/exceptions, and transition into reconciliation without creating workflow authority.
status: stable
tags: [experience, mapping, organizer, live-operations, remaining-work, exceptions, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-G-live-operations-remaining-work-exception-reconciliation-derived-outcome-state-mapping.md
  - resource: judge-evaluation.md
  - resource: authority-lineage-correction.md
  - resource: ../synchronizations/evaluation-occurrence-obligation.md
  - resource: ../synchronizations/temporal-truth-correction.md
  - resource: ../policies/operational-exception-governance.md
---

# Purpose

Define the current Organizer-facing semantics for coordinating live Competition activity and understanding remaining work without confusing planning, participation, responsibility, judgment evidence, derived projections or exception presentation with domain authority.

# Live Operations is a work context

`Live Operations` is a user-facing Organizer work context, not a Concept or lifecycle state.

It may compose visibility over:

- Competition lifecycle;
- Judge Participation/readiness;
- Panel planning/composition;
- Evaluation Occurrence state and actual participants;
- Evaluation Obligation state;
- Scorecard absent/Draft/finalized authority;
- paper/assisted capture status;
- uncertain authority/capture conditions;
- correction/invalidation/replacement pressure;
- warnings, blockers and governed exceptions.

The live view may prioritize what needs legitimate attention, but it owns none of those states.

# Planned grouping is not live evaluation truth

Preserve:

```text
Panel membership
  != actual Evaluation Occurrence participation
  != Evaluation Obligation responsibility
  != Scorecard evidence
```

A Panel membership change is different from an occurrence-specific participant adjustment.

Current Panel edits never rewrite who actually participated in a begun/completed occurrence.

Any responsibility consequence of substitution/absence/recusal must use the proper occurrence/obligation semantics rather than being inferred from visual grouping.

# Remaining Judge work

Remaining evaluation work is a derived projection over current **Outstanding Evaluation Obligations** and relevant context.

```text
Outstanding obligation + no Scorecard
  → not-started remaining work

Outstanding obligation + Scorecard Draft
  → in-progress/deferred remaining work

Satisfied obligation
  → not remaining work merely because linked evidence later becomes ineligible
```

If previously satisfying evidence becomes ineligible, represent that as an evidence/reconciliation condition.

New Judge work exists only when a legitimate successor Evaluation Obligation has actually been established.

```text
ineligible evidence
  != reopened predecessor obligation
  != automatic successor responsibility
```

# Event Completed does not mean all work complete

Competition `Event Completed` records the end of ordinary live-event activity.

It does not prove:

- all occurrences are complete;
- all obligations are terminal;
- all Scorecards are Finalized;
- Coverage is Satisfied;
- reconciliation is complete;
- the Competition is Finalization Ready.

A Judge may still have legitimate remaining work after an occurrence or Competition event has completed if current policy and Access permit it.

Event completion alone must not be represented as a universal hidden revocation of all Judge work capability.

# Operational condition taxonomy

Live Operations distinguishes:

```text
warning
  = informative condition; does not itself block authority

blocking precondition
  = required condition is false; action cannot proceed

governed exception
  = scoped permission despite preserved source condition

correction
  = source truth/authority requires legitimate owner-specific change

technical intervention
  = restore/restrict operation without substituting semantic authority
```

These are not interchangeable states of an issue ticket.

# Governed exceptions

A governed exception may alter only the explicitly permitted consequence under current policy.

It does not rewrite the underlying fact.

Examples:

```text
Panel = Degraded + permitted exception
  → occurrence may proceed where policy allows
  → Panel remains Degraded

Coverage = Incomplete + permitted consequence exception
  → later ranking/closeout may be permitted where policy allows
  → Coverage remains Incomplete
```

Material exception presentation should preserve, where relevant:

- affected Competition/resource/policy condition;
- preserved source shortfall;
- specific consequence permitted;
- acting/authorizing authority;
- reason.

An exception never silently waives unrelated policy or invariants.

# Acknowledgement and attention management

Acknowledging, hiding, suppressing, dismissing or viewing an operational warning/condition is presentation state only.

It never repairs source truth.

A condition becomes semantically resolved only when its source changes, a specifically permitted governed exception changes the consequence, or another owner-defined semantic action establishes the required postcondition.

# Organizer actions during live operation

Organizer Live Operations may expose purpose-specific actions such as:

- prepare/begin/complete an Evaluation Occurrence where current authority permits;
- record legitimate occurrence participant adjustment;
- coordinate Judge work and surface Outstanding obligations;
- establish permitted responsibility consequences through current composition;
- manage Panel planning separately from actual occurrence history;
- use paper/assisted capture through the 013-F authority-preserving path;
- invoke purpose-specific correction/invalidation/replacement paths;
- apply specifically governed exception actions;
- complete the Competition event when lifecycle conditions are met.

The experience must not expose a generic `Resolve`, `Force`, or `Override` control as universal semantic authority.

# Organizer authorship boundary

Operational urgency never makes the Organizer the Judge semantic author.

Organizer/support may coordinate, capture verified paper content, invoke legitimate exception/correction actions, or assist technical recovery.

They may not:

- invent Judge responses;
- Finalize a Judge's judgment merely because it is late;
- fabricate evidence to clear a gate;
- turn missing into zero;
- create duplicate evaluation weight;
- manufacture successor Judge work solely to make an operational condition disappear;
- use technical privilege as policy exception authority.

# Judge independence during live operation

Live Operations should not become a leaderboard surface that leaks peer/outcome signals into ordinary Judge evaluation.

Judge-facing disclosure remains governed by 013-C/E. Organizer visibility of operational status does not imply those values become Judge-visible.

# Transition into reconciliation

Reconciliation is a source-directed Organizer work context that becomes especially important as the event ends and outcome-affecting conditions remain.

Live Operations may surface reconciliation-relevant conditions before Event Completed; no mandatory navigation boundary or new lifecycle transition is required.

The natural derived/reconciliation owner is [Reconciliation & Derived Outcome-State Mapping](reconciliation-derived-state.md).

# Related mapping

- ordinary Judge work → [Judge Active Evaluation Mapping](judge-evaluation.md);
- paper/correction/invalidation/successor responsibility → [Authority Lineage, Capture & Correction Mapping](authority-lineage-correction.md);
- reconciliation/Coverage/Aggregate/Rank/readiness → [Reconciliation & Derived Outcome-State Mapping](reconciliation-derived-state.md).
