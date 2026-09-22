---
type: Architecture Decision
title: 019-I — Browser/Client State, Navigation, Accessibility & Degraded Interaction Architecture
description: "Completes Q4R-004 and resolves ADQ-008 by comparing the repaired historical front-end candidate, minimal server-rendered/progressive enhancement, local-first browser authority, framework-specific SPA adoption, and a framework-neutral client-rich browser architecture with explicit server authority and state partitioning."
status: stable
tags: [phase-019, architecture, adq-008, q4r-004, browser, client, accessibility, degraded]
sources:
  - resource: 019-I-Q4R-004-frontend-interaction-semantic-repair.md
  - resource: ../canonical/architecture/browser-client-interaction.md
  - resource: ../canonical/architecture/frontend-interaction.md
  - resource: ../canonical/experience/mapping-authority-baseline.md
  - resource: ../canonical/experience/context-role-modes.md
  - resource: ../canonical/experience/judge-evaluation.md
  - resource: ../canonical/experience/live-operations.md
  - resource: ../canonical/experience/accessibility-resilience.md
  - resource: ../canonical/experience/status-feedback-recovery.md
  - resource: ../canonical/policies/anonymity-disclosure.md
  - resource: ../canonical/invariants/accessibility-semantic-parity.md
  - resource: ../canonical/invariants/truthful-authority-under-uncertainty.md
  - resource: ../canonical/architecture/identity-access-authority.md
  - resource: ../canonical/architecture/interface-command-concurrency.md
  - resource: ../canonical/architecture/offline-continuity-reconciliation.md
  - resource: ../canonical/architecture/artifact-export-publication-delivery.md
  - resource: ../routing/phase019_architecture_decision_control.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T14:10:00-05:00 }
---

# Purpose

019-I repairs the historical front-end candidate under Q4R-004 and resolves ADQ-008.

The decision covers browser composition, client-state boundaries, navigation/context isolation, responsive behavior, accessibility semantic parity, degraded interaction and recovery.

# Entry state

~~~text
Phase 019                       ACTIVE
019-A/B/C/D/E/F/G/H             COMPLETE
019-I                           NEXT ELIGIBLE / USER AUTHORIZED

ADQ-001..007                    ACCEPTED
ADQ-008                         PLANNED
ADQ-009..010                    PLANNED

Q4R-001 / Q4R-002 / Q4R-003    COMPLETE
Q4R-004                         REQUIRED
Q4 repairs complete             3 / 4
technical probes                0

accepted whole architecture     false
implementation packages         0
implementation execution        false
~~~

# Q4 prerequisite

019-I completed:

> **Q4R-004 — Historical Front-End Interaction Semantic Repair**

The repair:

- translates Encounter to Evaluation Occurrence;
- translates generic task assignment to Evaluation Obligation + logical Scorecard;
- treats role mode as one current Competition-scoped Participation context rather than authority;
- maps historical AUTH/API/SYNC dependencies to accepted IAM/CMD/RCV authority;
- applies current Phase-013 Experience mapping;
- separates explanation/dependence order from navigation order;
- removes React, TypeScript, React Router, TanStack Query and IndexedDB from inherited authority.

The historical candidate remains unchanged.

# Decision

**ADQ-008 — ACCEPTED.**

Selected architecture:

> **A client-rich browser architecture subordinate to server authority, with explicit partitioning of remote cache, command/outcome state, bounded local Draft continuity, Participation/context hints and ephemeral interaction state; context-safe navigation and private-state isolation; phone-primary Judge work; responsive dense Organizer work; WCAG 2.2 AA-oriented semantic parity; explicit degraded/conflict/unknown recovery; and replaceable framework/router/query/storage/component mechanisms.**

Current owner:

> docs/canonical/architecture/browser-client-interaction.md

Stable rules:

> CLT-001 through CLT-020

# Constraints preserved

ADQ-008 preserves:

- ENG-004 — Identity/Participation/Access/authorship/technical privilege remain distinct;
- ENG-007 — current-state, retry and uncertainty preserve owner truth;
- ENG-008 — local/device/offline traces do not become authority;
- ENG-011 — disclosure/security remains consequential-boundary enforced;
- ENG-012 — accessibility/device continuity preserve semantic parity;
- ENG-014 — shared-device, offline convergence and unknown-result scenarios remain verification seeds;
- ENG-017 — historical candidates remain evidence until explicit acceptance;
- ACC-001 — Access is contextual;
- DISC-002 — disclosure is audience/purpose specific;
- INV-009 — accessibility is semantic parity;
- INV-010 — uncertainty never becomes fabricated authority;
- IAM shared-device/current Access boundaries;
- CMD commit confirmation/reconciliation;
- RCV local Draft/degraded continuity;
- ART disclosure/externalization boundaries.

# Historical candidate treatment

Input:

> docs/canonical/architecture/frontend-interaction.md

After Q4R-004:

~~~text
Q2 / Q3 / Q4                 QUALIFIED_AFTER_REVISION
semantic repair complete     yes
technology revalidation      still required downstream
comparison eligible          yes
historical authority         suspended
~~~

Retained hypotheses include state partitioning, non-authoritative cache, non-optimistic high-consequence state, context isolation, phone-primary judging, responsive Organizer density, component layering, accessibility parity, server-authoritative validation, explicit conflict/recovery, push as accelerator and error containment.

Package/framework selections are not inherited.

# Alternatives

## Alternative A — Adopt repaired historical FE architecture including its React/Router/Query/IndexedDB selections

Strengths:

- coherent full client stack;
- likely close to existing executable substrate;
- direct implementation path;
- strong prior reasoning.

Weaknesses:

- Phase-018 explicitly requires fresh technology revalidation;
- current ADQ-008 defers exact router/query packages;
- existing code reduces migration cost but is not architecture authority;
- IndexedDB and package choices should be tested against actual browser/privacy/runtime needs;
- selecting packages here would unnecessarily constrain implementation-program comparison.

**Rejected as an architecture-level selection.**

The existing stack remains a favored implementation candidate only if later evidence supports it.

## Alternative B — Minimal server-rendered / progressively enhanced browser with very limited client state

Characteristics:

- server renders most state;
- conventional navigation;
- minimal remote cache;
- little or no persistent client Draft state;
- JavaScript used only for local enhancement.

Strengths:

- low browser-state complexity;
- strong natural server-authority posture;
- reduced client bundle/state-management burden;
- simple cache invalidation model.

Weaknesses:

- weaker fit for bounded offline Draft continuity required by RCV;
- more disruptive transient-network behavior during active judging;
- less natural support for rich conflict/unknown-result recovery;
- dense Organizer live-operation views would incur more round trips/navigation churn;
- phone-primary judging benefits from richer local interaction.

**Rejected as the baseline architecture.**

Server rendering/progressive enhancement remain permitted within the selected architecture where useful.

## Alternative C — General local-first browser architecture with offline authority and broad merge

Characteristics:

- client database/replica as primary interaction state;
- offline authoritative actions;
- eventual synchronization;
- broad automatic conflict merge.

Strengths:

- maximum disconnected availability;
- strong local responsiveness;
- reduced dependency on immediate connectivity.

Weaknesses:

- directly conflicts with RCV-009/010 and current Access revalidation;
- stale authority/disclosure may persist offline;
- high-consequence operations are not generally merge-safe;
- increases shared-device/privacy exposure;
- risks turning browser state into a second authority model.

**Rejected.**

MUDAC supports bounded local Draft continuity, not general offline domain authority.

## Alternative D — Thin browser around a framework-specific server-driven interaction platform

Characteristics:

- server remains strongly authoritative;
- navigation/forms primarily server-driven;
- selected framework may provide partial-page updates and server-managed UI state.

Strengths:

- can simplify client ownership;
- may reduce duplicate data state;
- accessible progressive enhancement can be strong.

Weaknesses:

- still requires explicit local Draft continuity and conflict recovery for judging;
- framework-specific server/UI coupling can constrain portability;
- does not remove the need for client state classes or semantic recovery;
- current evidence does not justify selecting a server-driven framework over the existing client-rich direction.

**Rejected as the baseline selection.**

## Alternative E — Framework-neutral client-rich browser with explicit server-authority and state partitioning

Characteristics:

- rich browser interaction;
- routes/workspaces remain non-authoritative;
- remote cache is stale-capable and context-partitioned;
- command outcome state is explicit;
- bounded local Draft continuity composes with RCV;
- context changes isolate disclosure/private state;
- phone-primary Judge workflows;
- responsive dense Organizer workflows;
- WCAG 2.2 AA-oriented semantic parity;
- degraded capability reduction rather than weaker authority;
- push optional, correctness independent;
- framework/router/query/storage packages deferred.

**Selected.**

# Why client-rich is justified

The decision is driven by current product obligations rather than front-end fashion.

MUDAC needs:

- interruption-resistant active Scorecard work;
- bounded local Draft recovery;
- explicit multi-device/conflict reconciliation;
- clear pending/unknown/confirmed command outcomes;
- responsive phone-primary Judge interaction;
- dense Organizer live-operation presentation;
- context switching without disclosure leakage;
- accessible interaction across multiple input modes.

These needs justify meaningful browser-owned interaction state.

They do not justify browser-owned semantic authority.

# Client state model

The architecture recognizes five distinct classes:

~~~text
session / current-context hints
remote server/query cache
command / outcome / reconciliation state
bounded local Draft continuity
ephemeral view/interaction state
~~~

Implementation may use different libraries or processes, but these classes must remain distinguishable in behavior and security semantics.

# Navigation/context model

Navigation is a representation layer.

A browser may use URLs and nested workspaces for Competition, Participation and task context, but protected reads/actions re-evaluate current Access.

Switching Competition/capacity is a disclosure/security transition, not merely a route change.

No Phase-013 explanation or Concept-dependence order becomes a mandatory screen sequence.

# Accessibility and responsive model

Accessibility is architecture, not later visual polish.

Core paths target WCAG 2.2 AA-oriented semantic parity and avoid sole dependence on color, hover, camera, QR, gesture, fine pointer or one orientation.

Judge work must remain complete on narrow phones.

Organizer density may transform responsively while preserving blockers, authority consequences and disclosure.

# Degraded/recovery model

The client can preserve eligible Draft work locally, but:

~~~text
local durable
  != server-confirmed Draft
  != authoritative Finalized state
~~~

Unknown high-consequence result remains unknown until reconciliation.

Where current authority cannot be safely established, capability reduces rather than weakening semantics.

# Real-time and cache model

Remote client cache and optional push exist for latency/usability only.

Push loss cannot break correctness.

Stale cache cannot authorize commands.

Context transition must prevent prior private cache/Draft state from appearing under another Participation or user.

# Evidence

Acceptance evidence class:

> **DOCUMENTATION_REASONING**

No bounded technical probe is required to choose the architectural class.

Later implementation evidence must test:

- context-switch cache/private-state isolation;
- logout/shared-device handoff;
- local versus server-confirmed versus Finalized state;
- stale-cache protected action;
- duplicate/offline Draft convergence;
- conflict and unknown-result recovery;
- narrow-phone Judge workflow;
- Organizer responsive parity;
- keyboard/screen-reader/zoom/reflow core workflows;
- alternate path without QR/camera/hover/color reliance;
- push outage correctness;
- route/feature failure containment.

# Reversibility / lock-in

Intentional commitments:

- client-rich browser interaction;
- server-authoritative product semantics;
- explicit client state classes;
- non-authoritative remote cache;
- bounded RCV local Draft continuity;
- context/private-state isolation;
- explicit command uncertainty/recovery;
- phone-primary Judge completeness;
- responsive Organizer semantic parity;
- accessibility as semantic architecture.

Not selected:

- React;
- TypeScript;
- React Router;
- TanStack Query;
- IndexedDB or wrapper;
- global state library;
- UI/component library;
- CSS/design-token implementation;
- service worker/background sync;
- SSE/WebSocket mechanism;
- build/package manager;
- test framework.

# Residual uncertainty

Open downstream questions include:

- whether existing React/TypeScript substrate should be retained;
- exact router and remote-cache library;
- exact local Draft storage/encryption adapter;
- route/data loading strategy;
- component/accessibility primitive system;
- form state/validation tooling;
- cross-tab coordination;
- browser/device support matrix;
- bundle/performance budgets;
- push transport, if any;
- offline detection mechanics;
- telemetry and client-error collection;
- accessibility automated/manual test tooling.

# Scenario impact

ADQ-008 closes architecture posture for:

- shared-device context handoff;
- duplicate/offline Draft convergence;
- stale Participation/Access navigation;
- unknown/degraded result;
- phone-primary Judge operation;
- responsive Organizer live operation;
- accessibility semantic parity.

# Risk disposition

## ERI-02 — historical candidate mistaken for current architecture

**Controlled.**

Current authority is CLT-*; historical FE-* remains evidence.

## ERI-04 — stale semantic bindings survive candidate reuse

**CLOSED for front-end interaction.**

Pre-Phase-013 Encounter/role/navigation assumptions were translated by Q4R-004.

## ERI-09 — cross-owner coupling / derived-authority leakage

**Materially reduced; carried to 019-K.**

Navigation/cache/local state are explicitly non-authoritative and protected operations use current owner contracts.

## browser complexity / state leakage risk

**Explicit implementation/validation risk.**

The selected architecture requires evidence that state partitioning, context handoff and accessibility remain correct in the actual client stack.

# Implementation boundary

After 019-I:

~~~text
accepted bounded decisions       8 / 10
Q4 repairs complete              4 / 4
technical probes                 0

accepted whole architecture      false
implementation packages          0
package derivation               false
implementation execution         false
~~~

G0 remains unsatisfied.

# Exit decision

**019-I — COMPLETE — PASS.**

**Q4R-004 — COMPLETE.**

**ADQ-008 — ACCEPTED.**

Next eligible:

> **019-J — Runtime, Deployment, Availability, Observability, Security & Cost Architecture**

019-J is not automatically authorized.
