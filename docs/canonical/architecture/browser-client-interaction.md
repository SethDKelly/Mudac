---
type: Architecture Contract
title: Current Browser/Client State, Navigation, Accessibility & Degraded Interaction Architecture
description: "Accepted ADQ-008 browser architecture: client-rich but server-authoritative interaction, explicit state partitioning, context-safe navigation, bounded local Draft continuity, truthful command/recovery state, phone-primary judging, responsive Organizer density, accessibility semantic parity, and replaceable browser mechanisms."
status: stable
tags: [architecture, current, browser, client, navigation, accessibility, responsive, degraded, recovery]
sources:
  - resource: architecture-drivers.md
  - resource: application-ownership-boundaries.md
  - resource: identity-access-authority.md
  - resource: interface-command-concurrency.md
  - resource: offline-continuity-reconciliation.md
  - resource: artifact-export-publication-delivery.md
  - resource: frontend-interaction.md
  - resource: ../experience/mapping-authority-baseline.md
  - resource: ../experience/context-role-modes.md
  - resource: ../experience/judge-onboarding.md
  - resource: ../experience/judge-evaluation.md
  - resource: ../experience/live-operations.md
  - resource: ../experience/accessibility-resilience.md
  - resource: ../experience/status-feedback-recovery.md
  - resource: ../policies/anonymity-disclosure.md
  - resource: ../invariants/accessibility-semantic-parity.md
  - resource: ../invariants/truthful-authority-under-uncertainty.md
  - resource: ../../019-architecture-engineering-reentry/019-I-Q4R-004-frontend-interaction-semantic-repair.md
  - resource: ../../019-architecture-engineering-reentry/019-I-browser-client-state-navigation-accessibility-degraded-interaction-architecture.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T14:05:00-05:00 }
---

# Authority

This document is **current accepted architecture authority for ADQ-008**.

It selects a **client-rich browser architecture with explicit server-authority and state-boundary discipline**.

It does not select React, TypeScript, React Router, TanStack Query, IndexedDB, a global-state library, a component library, CSS system, service worker, push transport, build system or testing framework.

<a id="clt-001"></a>
## CLT-001 — The browser coordinates interaction; it never becomes semantic authority

Browser state may help a user navigate, edit, inspect, reconcile and recover, but authoritative product state remains owned by accepted application/domain boundaries.

Route presence, visible controls, cached data, local persistence, device possession or browser session continuity cannot establish semantic authority.

<a id="clt-002"></a>
## CLT-002 — The baseline is client-rich interaction over server-authoritative application contracts

MUDAC uses a browser client capable of rich local interaction, responsive workspaces, local Draft continuity and explicit recovery states while relying on accepted IAM/CMD/PST/RCV/ART contracts for authority.

The architecture does not require all pages to be client-rendered or prohibit server rendering/progressive enhancement where useful.

<a id="clt-003"></a>
## CLT-003 — Navigation represents context but does not define authority or Concept order

Routes, layouts, workspaces, tabs, breadcrumbs and navigation state may reflect Competition, Participation, resource and task context.

They do not create:

- Participation;
- Access;
- Evaluation Obligation;
- source authority;
- lifecycle state;
- Publication authority.

Dependence order, synchronization order and explanation order are not mandatory route or wizard order.

<a id="clt-004"></a>
## CLT-004 — Client state is partitioned by semantic responsibility

The browser keeps these state classes distinguishable:

- bounded session/current-context hints;
- remote server/query state;
- command/outcome state;
- local Draft continuity state;
- ephemeral interaction/view state.

No undifferentiated client store may erase these authority boundaries.

<a id="clt-005"></a>
## CLT-005 — Remote client cache is non-authoritative, freshness-capable and context-partitioned

Cached server/projection data may improve responsiveness but remains stale-capable.

Protected commands re-evaluate current server authority regardless of cached UI state.

Cache keys/partitions preserve material Competition, Participation, resource, audience/disclosure and other context needed to prevent cross-context leakage.

<a id="clt-006"></a>
## CLT-006 — Context transitions isolate disclosure and private state

Competition switch, Participation/capacity switch, logout, session invalidation and shared-device handoff cause relevant private client state to be cleared, partitioned or rendered inaccessible before the new context proceeds.

A new context cannot inherit prior Judge/Organizer disclosure merely because it shares the same browser process or device.

<a id="clt-007"></a>
## CLT-007 — Local Draft continuity is an RCV recovery adapter, not a browser domain replica

Eligible local working state preserves bounded recovery envelopes under RCV-001..018.

The exact browser persistence API, wrapper, encryption mechanism and autosave cadence remain implementation choices.

Local durability must remain distinguishable from server-confirmed Draft persistence and authoritative Finalization.

<a id="clt-008"></a>
## CLT-008 — High-consequence command state is explicit and never optimistically authoritative

For consequential commands the client represents, as applicable:

- ready/not attempted;
- submitting/in progress;
- confirmed authoritative success;
- validation rejection;
- Access denial;
- concurrency/current-state conflict;
- temporary transport failure;
- result unknown / reconciliation required.

Optimistic presentation may be used for reversible client-owned interaction, but not to declare authoritative success before CMD confirmation.

<a id="clt-009"></a>
## CLT-009 — Reconciliation and uncertainty are first-class interaction states

A lost response, stale Draft, expired Access, conflicting local/server work or uncertain asynchronous result receives a recovery path that preserves:

- what was attempted;
- what authority is definitely known;
- what remains uncertain;
- retained local work;
- legitimate next actions.

Unknown is not silently converted to success or failure.

<a id="clt-010"></a>
## CLT-010 — Judge workflows remain complete on narrow/phone viewports

Core Judge work is phone-primary capable.

Responsive presentation may reduce density or progressively disclose detail, but must preserve current Competition/Participation context, Judge-safe Team representation, exact evaluation basis, Scorecard work, material blockers, local/server/finality state and legitimate actions.

<a id="clt-011"></a>
## CLT-011 — Organizer work supports dense responsive composition without semantic flattening

Organizer live-operation and preparation views may use tables, summaries, dashboards or exception-first composition.

Responsive transformation may change grouping/density but cannot hide material blockers, merge independent status dimensions, alter disclosure, or convert derived projections into source authority.

<a id="clt-012"></a>
## CLT-012 — Core browser interaction targets WCAG 2.2 AA-oriented semantic parity

Core workflows preserve meaningful operation across keyboard, touch, pointer, screen reader, zoom/reflow, reduced motion and supported orientation changes.

No core operation relies solely on mouse, hover, camera/QR, color, gesture or fine-pointer precision.

Accessible paths preserve the same authority, privacy, evidence and recovery semantics.

<a id="clt-013"></a>
## CLT-013 — Semantic structure and equivalent input paths precede custom interaction convenience

The client favors platform/semantic controls and accessible primitives before custom interaction where practical.

Camera/QR, drag/drop, gesture, hover, visual spatial arrangement or other convenience mechanisms require equivalent legitimate paths when they would otherwise block a core operation.

Assistance does not transfer semantic authorship.

<a id="clt-014"></a>
## CLT-014 — Responsive transformation preserves consequence hierarchy and disclosure

Across viewport changes, the client keeps material subject/current state, warning/blocker, basis/explanation, legitimate action and consequence discoverable in a semantically appropriate order.

Responsive adaptation cannot reveal Judge-prohibited information or hide authority-relevant qualifications.

<a id="clt-015"></a>
## CLT-015 — Client composition separates accessible primitives, semantic patterns, domain features and workspaces

The architecture favors layered composition:

~~~text
accessible interaction primitives
  → reusable semantic patterns
  → domain feature components
  → route/workspace composition
~~~

A UI/component package may implement these layers but does not define MUDAC semantics.

<a id="clt-016"></a>
## CLT-016 — Client validation assists; authoritative validation remains server-owned

Client validation may provide immediate format/completeness feedback and prevent obvious invalid requests.

Access, lifecycle, concurrency, structural authority, disclosure and domain validation remain authoritative at accepted application boundaries.

A disabled button is not the authority decision.

<a id="clt-017"></a>
## CLT-017 — Degraded operation reduces capability rather than weakening semantics

When current Access, source basis, command outcome or another consequential precondition cannot be established safely, the client may preserve work and make the operation unavailable.

It must not substitute a lower-authority path merely to preserve apparent availability.

Paper fallback and bounded local Draft continuity remain governed by RCV.

<a id="clt-018"></a>
## CLT-018 — Real-time push is an accelerator, not a correctness dependency

Push, SSE, WebSocket or similar notification may trigger refresh/invalidation and improve live-event latency.

Correctness remains achievable through authoritative query/command/reconciliation behavior without relying on push as the sole source of truth.

Exact push mechanism remains downstream.

<a id="clt-019"></a>
## CLT-019 — Client error boundaries contain presentation failure without inventing source-state loss

Route, feature or component failures are isolated where practical.

A rendering/network/projection failure does not imply source data disappeared or changed.

Error/recovery surfaces distinguish unavailable, stale, denied, conflicted, uncertain and unexpected conditions where their recovery differs, while preserving eligible local work.

<a id="clt-020"></a>
## CLT-020 — Browser technology remains replaceable behind the client architecture contract

Framework, language, router, query/cache library, local-storage adapter, state library, component system, form library, CSS tooling, build system, service worker, telemetry SDK and test framework are implementation selections.

Existing React/TypeScript substrate may be reused if later qualification shows it satisfies CLT-001..019 proportionately.

Historical implementation convenience cannot override these rules.

# Selected topology

~~~text
browser client
  ├─ navigation/context coordination
  ├─ remote non-authoritative cache
  ├─ command/outcome/reconciliation state
  ├─ bounded local Draft continuity
  ├─ ephemeral interaction state
  └─ accessible responsive presentation
           |
           v
versioned CMD query/command contracts
           |
           v
server-side IAM + authoritative owners
~~~

# Evidence posture

ADQ-008 acceptance uses **DOCUMENTATION_REASONING**.

No framework-specific technical probe is required to select this architecture.

Later executable evidence must demonstrate at least:

- Competition/Participation context switch without private-state leakage;
- logout/shared-device handoff cleanup/isolation;
- stale cache cannot authorize a protected action;
- local Draft versus server-confirmed versus Finalized distinction;
- two-device/conflict recovery surfaces;
- unknown command result reconciliation;
- narrow-phone Judge completion;
- Organizer responsive/dense semantic parity;
- keyboard/nonvisual/reflow operation for core workflows;
- no sole dependence on QR/camera/color/hover;
- accessible status and error semantics;
- push loss without correctness loss.

# Revisit triggers

Reopen ADQ-008 when credible evidence shows:

- client-rich state complexity exceeds its live-event/offline value;
- a server-rendered/progressively enhanced approach can materially simplify implementation without degrading RCV or Experience obligations;
- browser storage/security constraints cannot preserve shared-device privacy;
- target-device/browser support cannot meet semantic accessibility/degraded requirements;
- measured client performance makes current partitioning disproportionate;
- 019-K finds unresolved state-leakage, accessibility, degraded-mode or recovery risk.

Whole-architecture acceptance remains false until 019-L.
