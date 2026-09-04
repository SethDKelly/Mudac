---
type: Architecture Contract
title: Front-End State, Navigation & Interaction Architecture
description: Defines MUDAC's React/TypeScript browser baseline, route/context ownership, explicit client-state classes, remote cache and local Draft boundaries, command/recovery states, component layering, responsive parity, and accessibility architecture.
status: stable
tags: [architecture, frontend, react, typescript, state, navigation, accessibility, responsive]
sources:
  - resource: ../../005-system-application-data-synchronization-architecture/005-H-front-end-state-navigation-component-system-responsive-interaction-architecture.md
  - resource: architectural-foundation.md
  - resource: identity-access-session.md
  - resource: commands-api-concurrency.md
  - resource: synchronization-recovery.md
  - resource: external-representation.md
  - resource: ../experience/context-role-modes.md
  - resource: ../experience/judge-evaluation.md
  - resource: ../experience/live-operations.md
  - resource: ../experience/accessibility-resilience.md
  - resource: ../experience/status-feedback-recovery.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T05:18:00Z }
---

# Purpose

Define how the browser realizes MUDAC navigation, state, recovery, component, accessibility, and responsive interaction semantics without becoming a second source of authority.

<a id="fe-001"></a>
## FE-001 — The browser baseline is React + TypeScript with explicit architectural adapters

The initial browser application uses React and TypeScript. Framework/components consume versioned application contracts through explicit API, query, session, local-Draft, and artifact adapters rather than importing infrastructure or persistence concerns directly.

Front-end framework convenience cannot redefine upstream product or architecture meaning under [ARCH-001](architectural-foundation.md#arch-001).

<a id="fe-002"></a>
## FE-002 — React Router owns route/navigation boundaries, not domain authority

React Router Data mode is the baseline navigation architecture for nested layouts, route identity, navigation/pending behavior, error boundaries, and route-aware prefetch/orchestration.

A URL, route match, loader result, or visible navigation item never proves current Access or resource authority. Protected server operations continue to re-evaluate [AUTH-004](identity-access-session.md#auth-004).

<a id="fe-003"></a>
## FE-003 — Client state is partitioned by semantic ownership

The browser keeps session/Participation context, remote server/query state, command outcome state, durable local Draft continuity, and ephemeral view state as distinct classes. They may coordinate but are not flattened into one undifferentiated mutable global store.

State architecture must preserve which values are server-confirmed, projected/cached, local-only, pending, conflicted, or uncertain.

<a id="fe-004"></a>
## FE-004 — TanStack Query owns remote client cache and never becomes authoritative state

TanStack Query is the baseline cache/lifecycle layer for remote resources and projections. Query entries may be stale, invalidated, refetched, or context-partitioned and therefore cannot authorize a consequential command.

Route loaders may prefetch or ensure query data but do not create a competing remote-data cache. Commands independently revalidate authority under [API-011](commands-api-concurrency.md#api-011).

<a id="fe-005"></a>
## FE-005 — Durable local Draft continuity uses an IndexedDB-backed adapter and remains non-authoritative

Eligible Scorecard/Amendment Draft continuity is persisted through an IndexedDB-backed browser adapter implementing the [SYNC-*](synchronization-recovery.md) contract. Records remain bound to stable semantic identity and confirmed server basis/revision.

If durable local persistence is unavailable or unsafe, MUDAC degrades to server-only continuity and, when necessary, paper rather than inventing alternate local authority.

<a id="fe-006"></a>
## FE-006 — High-consequence command state is explicit and never optimistically final

Authoritative mutations expose semantic client states such as submitting, confirmed, rejected/validation, denied, concurrency conflict, temporary failure, and uncertain outcome/reconciliation-required.

The UI may optimistically update reversible local working interactions, but it cannot optimistically declare Scorecard/Competition Finalization, Official Outcome change, exceptional Access, or Publication before server-confirmed commit under [API-004](commands-api-concurrency.md#api-004).

<a id="fe-007"></a>
## FE-007 — Role/Participation mode is explicit and changes disclosure as well as navigation

The application shell follows `Identity → Participation/role mode → Competition → role workspace → task/resource`.

Judge and Organizer modes remain explicit. A dual-role Identity does not receive a unioned client capability surface; switching mode triggers relevant route, cache, disclosure, and protected-context re-evaluation under [AUTH-009](identity-access-session.md#auth-009).

<a id="fe-008"></a>
## FE-008 — Context transitions partition or clear private client state

Competition switch, role/Participation switch, logout, session revocation, or shared-device handoff invalidates or partitions private query cache, clears inappropriate ephemeral state, and prevents locally persisted Draft material from attaching to the wrong Identity/Participation/resource.

Protected routes re-resolve current Access after a context transition. Client cache hygiene is a privacy boundary, not only a performance concern.

<a id="fe-009"></a>
## FE-009 — Judge interaction is phone-primary and task-centered

Judge workflows remain complete on narrow phone viewports. The shell prioritizes current Competition/role, Panel/Encounter context, Team Alias + Division, Scorecard work, truthful save/sync/finality state, and permitted own-history access.

No core Judge operation may require desktop width, hover, mouse precision, landscape orientation, or a secondary desktop-only workflow.

<a id="fe-010"></a>
## FE-010 — Organizer interaction is exception-first and responsively composable

Organizer desktop work may use dense tables, split panes, and multi-column command views, but narrow layouts preserve the same operational semantics through `summary → exception → detail → legitimate action` drill-down.

Responsive adaptation changes composition/density, not authority, visibility policy, or available legitimate recovery paths.

<a id="fe-011"></a>
## FE-011 — Component architecture separates primitives, semantic patterns, domain features, and route compositions

The component system layers design tokens → accessible primitives → semantic interaction patterns → domain feature components → route/workspace compositions.

Reusable primitives do not own MUDAC state machines. Feature components compose application contracts and semantic patterns but do not become alternate domain-policy owners.

<a id="fe-012"></a>
## FE-012 — Semantic status presentation preserves independent state dimensions

Lifecycle, persistence/authority confidence, readiness, validity, version/freshness, issue severity, disclosure, synchronization, and publication state remain independently representable.

A generic badge, color, icon, or `status` prop must not collapse `Draft`, `server-confirmed`, `Finalized`, `stale`, `affected`, `published`, `uncertain`, or similar meanings into one ambiguous visual state.

<a id="fe-013"></a>
## FE-013 — Core browser workflows target WCAG 2.2 AA semantic parity

Core workflows preserve meaningful operation across keyboard, touch, pointer, screen reader, zoom/reflow, reduced motion, and supported orientation changes. Semantic HTML is preferred before custom ARIA behavior.

Critical distinctions cannot rely only on color, iconography, camera/QR, gesture, hover, or fine-pointer precision. This realizes the upstream accessibility contract and `INV-009`.

<a id="fe-014"></a>
## FE-014 — Client validation assists; server validation remains authoritative

Client-side form validation may provide immediate feedback, but Access, lifecycle, concurrency, structural, and domain validation remain server-authoritative.

Rejected commands preserve entered work where safe and expose specific corrective action. High-consequence confirmations use precise semantic verbs rather than ambiguous generic confirmation labels.

<a id="fe-015"></a>
## FE-015 — Conflict/recovery UI preserves evidence instead of reducing failure to a toast

Draft conflict, uncertain command, expired Access, projection failure, paper/electronic overlap, and artifact-generation/publication failure receive recovery surfaces appropriate to their semantics.

Conflict UI preserves both local and server work where required by [SYNC-004](synchronization-recovery.md#sync-004), states what is definitely known versus uncertain, and gives the safest next action.

<a id="fe-016"></a>
## FE-016 — Real-time push is an accelerator, not a correctness dependency

Correctness relies on authoritative queries/commands, invalidation, explicit refresh, and bounded revalidation/polling. SSE, WebSocket, or another push mechanism may reduce latency for Live Operations but cannot become the sole source of truth or bypass API ownership/preconditions.

Push notifications trigger identified refresh/state updates whose authority remains server-owned.

<a id="fe-017"></a>
## FE-017 — Dense/tabular information may transform responsively without semantic loss

Data that is genuinely tabular uses semantic table structure where appropriate. Narrow layouts may transform rows into grouped lists/cards or focused detail views only when relationships, exception visibility, ordering, and legitimate actions remain equivalent.

Responsive representation cannot reveal Judge-prohibited Rank/peer-result information or hide fairness-relevant exceptions.

<a id="fe-018"></a>
## FE-018 — Client error boundaries contain failure without inventing source-state loss

Route and feature error boundaries isolate rendering/network failures from unrelated work and preserve recoverable local Draft state where possible.

A failed projection, renderer, route, or UI component does not imply authoritative source data is absent or changed. Error surfaces distinguish unavailable, stale, denied, conflicted, uncertain, and unexpected states where recovery differs.

# Front-end state topology

```text
React Router
    route/layout/context/error navigation
          ↓
TanStack Query
    remote server + projection cache
          ↓
API command/query adapters
    authoritative server boundary

IndexedDB Draft adapter
    non-authoritative local continuity

React local/reducer/context state
    ephemeral interaction + narrowly scoped shell context
```

A general-purpose global application store is not selected as baseline. A specialized state library may be introduced later only for a demonstrated client-owned state problem that does not duplicate remote cache, Draft persistence, or server authority.

# Representative interaction states

```text
Draft editing
  local saved → sync pending → server confirmed
                              ↘ conflict

Finalize
  idle → submitting → confirmed
                    ↘ rejected
                    ↘ conflict
                    ↘ uncertain → reconcile

Artifact
  requested → generating → generated → validated → published
                     ↘ failed               ↘ publication failed
```

# Component-system posture

The architecture defines a MUDAC semantic component layer, not a mandatory third-party visual library. Accessible primitives may later be implemented with native elements and/or a proven low-level primitive library, but their API must express MUDAC semantic states rather than inherit product meaning from the vendor component vocabulary.

Design tokens govern visual consistency while semantic state remains explicit in component contracts.

# Deliberate deferrals

This contract does not select the package manager/build system, CSS architecture, primitive/component library, icon/chart library, form library, IndexedDB wrapper, service-worker implementation, telemetry SDK, testing framework, push transport, or concrete design tokens. Implementation choices must satisfy `FE-*` and their upstream owners.