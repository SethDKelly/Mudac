---
type: Architecture Design Record
title: 005-H — Front-End State, Navigation, Component-System & Responsive Interaction Architecture
description: Establishes MUDAC's React/TypeScript browser architecture, role/context routing, explicit client-state classes, server/query caching, IndexedDB Draft continuity, command/recovery state machines, accessible component layering, and responsive interaction rules.
status: stable
tags: [phase-005, architecture, frontend, react, state, navigation, accessibility, responsive]
sources:
  - resource: ../canonical/experience/context-role-modes.md
  - resource: ../canonical/experience/judge-evaluation.md
  - resource: ../canonical/experience/live-operations.md
  - resource: ../canonical/experience/accessibility-resilience.md
  - resource: ../canonical/experience/status-feedback-recovery.md
  - resource: ../canonical/architecture/architectural-foundation.md
  - resource: ../canonical/architecture/identity-access-session.md
  - resource: ../canonical/architecture/commands-api-concurrency.md
  - resource: ../canonical/architecture/synchronization-recovery.md
  - resource: ../canonical/architecture/external-representation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T05:18:00Z }
---

# Purpose

Translate the accepted MUDAC experience and system contracts into a browser architecture that keeps authority, freshness, local continuity, role context, and recovery truthful across phone-primary Judge work and dense Organizer operations.

005-H intentionally chooses a concrete front-end baseline where the architecture now provides enough evidence, while keeping visual branding and replaceable implementation details subordinate to semantic UI contracts.

# Decision summary

MUDAC's browser application will use **React + TypeScript** with **React Router in Data mode** for route/layout/navigation/error boundaries and **TanStack Query** for remote server/query cache. Durable non-authoritative Draft continuity uses an **IndexedDB-backed local Draft adapter**. Ephemeral interaction state remains local to components/features by default; no general-purpose global client store is selected as baseline.

The browser is a client of the MUDAC HTTPS/JSON API. It does not become a second domain runtime or authority layer.

# State architecture

Client state is partitioned into distinct classes:

```text
session / participation context
        authoritative server-derived identity context

remote resource/query state
        server resources + projections, cached with freshness

command state
        submitting / confirmed / rejected / conflict / uncertain

local Draft continuity state
        IndexedDB-backed, non-authoritative, revision-bound

ephemeral view state
        focus, disclosure, local filters, dialogs, transient selection
```

These classes may coordinate, but one store does not flatten their semantics.

# Navigation architecture

The route/context hierarchy follows the accepted experience stack:

```text
Identity
  ↓
Participation / explicit role mode
  ↓
Competition
  ↓
role workspace
  ↓
resource / task
```

Representative route shape:

```text
/app
  /competitions/:competitionId
    /judge
      /panel
      /encounters/:encounterId
      /scorecards/:scorecardId
      /history
    /organizer
      /preparation
      /live
      /reconciliation
      /materials
```

URLs carry navigation identity only. Every protected query/command still resolves current session, Participation, Access, resource, and lifecycle state on the server.

# Judge shell

Judge navigation minimizes persistent chrome and prioritizes current event context:

```text
Competition / role context
Current Panel / Encounter
Team Alias + Division
Scorecard Draft / Finalization task
Own permitted live-event history
```

The primary Scorecard workflow must remain fully usable on a narrow phone viewport, with interruption/resume and sync status visible without forcing desktop-style navigation.

# Organizer shell

Organizer navigation is workspace-oriented:

```text
Preparation
Live Operations
Reconciliation & Outcomes
Materials & Publication
```

Dense desktop views may use tables, split panes, and multi-column layouts. Narrow layouts preserve the same operational semantics through `summary → exception → detail → legitimate action` drill-down rather than hiding capabilities behind desktop-only affordances.

# Server/query state

TanStack Query owns fetch/cache/invalidation lifecycle for remote resources and projections. Query keys incorporate stable semantic context such as Competition, Participation/role mode, resource identity, and representation profile where disclosure differs.

Query cache entries may be stale and must never be used as proof that a consequential command remains valid. Commands go through explicit API clients and server-side revalidation.

Route loaders may prefetch/ensure query data, but React Router does not maintain a competing copy of domain data. The route layer coordinates navigation, errors, pending transitions, and route-scoped context.

# Local Draft state

An IndexedDB-backed adapter implements the `SYNC-*` durable Draft contract. It stores only eligible continuity data, stable semantic identity, confirmed server basis/revision, pending edits, and synchronization/recovery state.

IndexedDB is an implementation mechanism, not authority. When unavailable or unsafe, MUDAC degrades to server-only Draft continuity and then paper continuity as required rather than inventing another local authority path.

# Command interaction state

High-consequence commands use an explicit state model:

```text
idle
  ↓
submitting
  ├── confirmed
  ├── rejected / validation
  ├── authorization denied
  ├── concurrency conflict
  ├── temporary failure
  └── uncertain outcome → reconcile
```

The UI may optimistically reflect purely local/working interactions where reversibility is clear, but it may not optimistically declare Scorecard Finalization, Competition Finalization, Official Outcome change, Access grant, artifact Publication, or another authoritative transition.

# Conflict and recovery UI

Conflict screens preserve the user's local work and current server state simultaneously. They identify:

- what action was attempted;
- the last confirmed server revision;
- what changed locally;
- what changed on the server;
- whether authority or Access changed;
- what can safely be merged or must be manually reconciled;
- the next safe action.

A generic error toast is insufficient for authority-sensitive recovery.

# Component-system architecture

The component system is layered:

```text
Design tokens
  ↓
Accessible primitives
  ↓
Semantic interaction patterns
  ↓
Domain feature components
  ↓
Route/workspace compositions
```

Accessible primitives include controls such as Button, Link, Input, Select, Checkbox, RadioGroup, Dialog, Disclosure, Tabs, Menu, Table/List, Status, Alert, Progress, and FormField. Native semantic HTML is preferred where it provides the required behavior.

Semantic patterns include ConfirmAction, CommandStatus, SyncStatus, ConflictResolution, ContextHeader, ExceptionSummary, ProvenanceSummary, ArtifactStatus, and SourceBasisSummary.

Feature components such as ScorecardEditor, EncounterCard, LiveOpsExceptionList, PaperCaptureReview, OutcomeRevisionSummary, and PublicationPanel compose those patterns but do not own domain authority rules.

# Design tokens and semantics

Tokens centralize typography, spacing, density, shape, focus, motion, elevation, and semantic state presentation. Semantic states are not encoded by color alone.

Visual variants name meaning such as `danger`, `warning`, `success`, `uncertain`, `draft`, `finalized`, or `stale` only where that meaning is precise. One generic `status` visual must not collapse lifecycle, authority, freshness, validity, disclosure, and publication dimensions.

# Responsive behavior

Responsive changes alter composition, density, navigation, and disclosure of secondary detail—not domain meaning or authority.

Judge:
- phone-primary;
- single-column task flow by default;
- touch targets appropriate to coarse pointers;
- critical context and sync/finality state remain visible.

Organizer:
- desktop may expose dense tables/split panes;
- narrow screens move through summary, exception queue, detail, and action;
- no critical action depends on hover, horizontal precision, fixed landscape orientation, or wide viewport.

# Accessibility posture

Core flows target WCAG 2.2 AA and preserve semantic parity across keyboard, touch, pointer, zoom, screen reader, reduced-motion, and alternate orientation use.

Architecture requirements include:

- semantic landmarks/headings;
- logical focus order and visible focus;
- focus restoration after dialogs/navigation where appropriate;
- keyboard-complete controls;
- accessible names/descriptions/error associations;
- status changes announced when material without creating notification noise;
- no color-only or icon-only critical distinctions;
- reduced-motion respect;
- zoom/reflow compatibility;
- accessible alternatives to QR/camera-driven entry.

# Forms and validation

Client validation improves immediacy but the server remains authoritative for Access, lifecycle, concurrency, and domain validation.

On rejection, user-entered work is preserved where safe. Validation messages identify the relevant field/action and corrective next step. High-consequence confirmation uses semantic action language such as `Finalize Scorecard` or `Publish Results`, not generic `Confirm` where ambiguity matters.

# Tables and dense information

Semantic table structure is used where relationships are genuinely tabular. Organizer desktop tables may provide sorting/filtering and row-level action entry points.

On narrow screens, tables may become grouped lists/cards or focused detail sequences, but data meaning, exception visibility, and legitimate actions remain equivalent. Rank/standings remain excluded from judging views under upstream disclosure/fairness rules.

# Context switching and cache hygiene

Competition switch, Participation/role-mode switch, logout, session revocation, or shared-device handoff triggers deliberate client cleanup/revalidation:

- private query caches are invalidated or partitioned by context;
- pending local Draft records remain scoped to their original Identity/Participation/resource and are not attached to a new user/context;
- ephemeral feature state is cleared as appropriate;
- protected routes re-resolve current Access.

A role switch changes disclosure posture as well as navigation.

# Real-time posture

Correctness does not depend on a push channel. Query invalidation, explicit refresh, and bounded polling/revalidation form the correctness baseline.

SSE, WebSocket, or another push mechanism may later reduce Live Operations latency, but push events trigger refetch/invalidation or identified state updates; they do not bypass authoritative API/resource checks or become the only source of truth.

# Error boundaries

Route and feature boundaries contain rendering/network failures without collapsing unrelated work. A Scorecard editing failure should preserve local Draft continuity where possible; a broken Organizer projection should not imply the underlying authoritative state is lost.

Error/recovery surfaces distinguish unavailable data, stale data, denied Access, conflict, failed projection, generation failure, uncertain command, and unexpected client failure when those states require different recovery.

# Security and disclosure

The UI may hide or disable unavailable controls for usability, but server-side `AUTH-*` remains authoritative. Sensitive data is not fetched merely to hide it in the DOM.

Private data must not leak through cache reuse across role/context switches, URLs, browser storage keys, diagnostic messages, filenames, client telemetry, or generated representation previews.

# Alternatives considered

## One global client store

Rejected as the baseline because it encourages authoritative server state, query cache, local Draft continuity, command state, and ephemeral UI state to collapse into one mutable graph with unclear freshness/ownership.

## React Router as the sole data cache

Rejected. Route loaders are useful for route-aware orchestration and prefetch, but MUDAC's projection freshness, background refetch, mutation invalidation, and cross-route resource reuse benefit from an explicit remote-state cache. One cache remains authoritative for remote client copies: TanStack Query.

## Full-stack React framework/server rendering as the product authority layer

Not required initially. MUDAC's authenticated event application is primarily an interactive client of the versioned HTTPS/JSON API. Pre-rendering/server rendering may later be used for genuinely public/static surfaces without moving MUDAC domain authority into route rendering code.

## Desktop-first Organizer UI with responsive shrink

Rejected because narrow-screen operation is an accepted continuity/accessibility path, not a visually compressed desktop dashboard.

## Component library defines domain states

Rejected. A third-party component library may implement primitives later, but component-library terminology cannot define Scorecard, Competition, Publication, sync, authority, or lifecycle semantics.

# Deliberate deferrals

005-H does not select the exact package manager/build tool, CSS strategy, third-party primitive/component library, icon library, charting package, form library, IndexedDB wrapper, service-worker library, telemetry SDK, testing framework, SSE/WebSocket implementation, or design-brand token values. Those implementation selections must satisfy the architecture defined here.