---
type: Architecture Contract
title: Draft Synchronization, Offline & Recovery Architecture
description: Defines bounded local Draft persistence, revision-aware synchronization, conflict preservation, reconnect/access revalidation, uncertain-command recovery, and paper convergence without offline authority.
status: stable
tags: [architecture, synchronization, offline, draft, recovery, conflict]
sources:
  - resource: ../../005-system-application-data-synchronization-architecture/005-F-draft-persistence-synchronization-offline-degraded-operation-conflict-recovery.md
  - resource: architectural-foundation.md
  - resource: data-persistence.md
  - resource: identity-access-session.md
  - resource: commands-api-concurrency.md
  - resource: ../concepts/scorecard.md
  - resource: ../policies/continuity-paper.md
  - resource: ../experience/judge-evaluation.md
  - resource: ../experience/status-feedback-recovery.md
  - resource: ../invariants/capture-channel-parity.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T05:00:00Z }
---

# Purpose

Define how MUDAC preserves non-authoritative Judge working state through intermittent connectivity and device changes while ensuring that synchronization, recovery, and degraded operation never fabricate server authority.

<a id="sync-001"></a>
## SYNC-001 — Local persistence is bounded to non-authoritative continuity state

The browser may durably preserve eligible Scorecard/Amendment Draft working content and last-known read context for continuity. Local state cannot independently establish Finalization, Competition lifecycle changes, Access grants, outcome authority, publication, or another high-consequence transition.

This realizes [SC-001](../concepts/scorecard.md#sc-001) and [ARCH-003](architectural-foundation.md#arch-003).

<a id="sync-002"></a>
## SYNC-002 — Local Draft state is bound to stable semantic identity and a confirmed server base

Locally persisted Draft work is scoped to the authenticated Identity/Participation context, Competition, Encounter, logical Scorecard identity, exact Rubric Version, and last confirmed server Draft revision/basis.

Browser tab, URL, Team Alias, display order, or device identity is insufficient to identify authoritative synchronization target.

<a id="sync-003"></a>
## SYNC-003 — Server Draft revision remains authoritative and synchronization is revision-aware

A Draft synchronization attempt uses stable resource/create-intent identity, idempotency semantics, and an expected server revision/precondition. The server revalidates current Access, ownership, structural basis, and concurrency before committing a new Draft revision.

A local save is never reported as server-confirmed merely because durable browser storage succeeded.

<a id="sync-004"></a>
## SYNC-004 — Stale Draft conflicts preserve both server and local Judge work

MUDAC rejects silent last-write-wins for Judge-authored evaluation content. When the server Draft advanced beyond the local base, the current server Draft and pending local work are both preserved until reconciliation.

Conflict recovery may not silently discard newer server authority or unsynchronized Judge intent.

<a id="sync-005"></a>
## SYNC-005 — Automatic merge is permitted only when semantic safety is demonstrable

An implementation may propose a deterministic merge for changes proven non-overlapping and semantically safe, but automatic field-level merging is not the default authority rule.

Score/Note meaning, deletions, structural context, Rubric/Encounter basis, Finalization, and amendment lineage can make mechanically separate edits semantically incompatible. When safety is not demonstrable, the Judge explicitly reconciles preserved local work against current server state.

<a id="sync-006"></a>
## SYNC-006 — Multiple devices converge on one logical Scorecard

Device replacement or concurrent device use never creates a new evaluation merely to avoid synchronization conflict. Devices resolve the same Participation, Encounter, and logical Scorecard under [INV-002](../invariants/one-logical-scorecard.md#inv-002), while optimistic concurrency determines whether pending local edits are stale.

<a id="sync-007"></a>
## SYNC-007 — Finalization and other authoritative transitions require reachable server authority

A disconnected client may prepare and preserve a complete Draft but cannot create a Finalized Scorecard Version, Finalized Amendment, exceptional Access grant, Competition lifecycle transition, official outcome change, or publication transition offline.

Authoritative transitions occur only through the server command/transaction boundary defined by [API-004](commands-api-concurrency.md#api-004).

<a id="sync-008"></a>
## SYNC-008 — Uncertain consequential outcomes are reconciled before another transition is attempted

If a consequential request may have reached/committed at the server but its response was lost, the client preserves the original idempotency/command context and treats outcome as uncertain.

Reconnect/retry resolves the existing authoritative result under [API-010](commands-api-concurrency.md#api-010) before permitting a duplicate or contradictory transition.

<a id="sync-009"></a>
## SYNC-009 — Reconnect re-establishes authentication, Access, identity, and current server state before applying queued work

Pending local work does not inherit indefinite authority from the session state that existed when it was created. Reconnect re-establishes current session/Identity/Participation context, reevaluates Access, resolves current logical resource identity and revision/Finalization state, then synchronizes or surfaces conflict.

<a id="sync-010"></a>
## SYNC-010 — Cached reads remain explicitly stale-capable and disclosure-bounded

Previously loaded Team/Encounter/Rubric/status context may remain visible while degraded only with its last-confirmed/freshness basis represented honestly. Cached information never establishes current Access or command authority.

Sensitive cached information is partitioned/cleared sufficiently to preserve current Participation/disclosure boundaries during logout, shared-device handoff, role-context switch, expiry, and revocation.

<a id="sync-011"></a>
## SYNC-011 — Access expiry or revocation blocks automatic synchronization of private pending work

A disconnected device may be unaware that Event Completed, Participation withdrawal, session revocation, or another authority change occurred. Once current state is known, expired/revoked Access prevents ordinary automatic upload/edit activity even when local Draft content remains recoverable.

Preserved local material is handled through the applicable Organizer-guided recovery, correction, retention, or paper process rather than reviving stale Judge authority.

<a id="sync-012"></a>
## SYNC-012 — Paper and electronic traces converge on one logical evaluation with preserved provenance

When paper fallback and electronic Draft traces overlap, both channels preserve the same Judge Participation, Encounter, Rubric Version, and logical Scorecard identity under [INV-008](../invariants/capture-channel-parity.md#inv-008).

Organizer transcription identifies capture actor/source while Judge authorship remains distinct. Ambiguous conflict between paper and electronic Judge intent is preserved and explicitly reconciled rather than guessed.

<a id="sync-013"></a>
## SYNC-013 — Synchronization status preserves authority, freshness, conflict, and uncertainty as distinct dimensions

UX/API state distinguishes at minimum confirmed server Draft, unsynchronized local work, synchronizing, stale-base conflict, uncertain consequential outcome, Finalized authoritative Version, and access-expired/recovery-required conditions where applicable.

A generic `Saved`, `Synced`, `Offline`, or success indicator must not collapse local durability into server authority. See [Truthful status/recovery experience](../experience/status-feedback-recovery.md).

<a id="sync-014"></a>
## SYNC-014 — Degraded digital operation yields to paper when authoritative continuity cannot be trusted

MUDAC optimizes for preserving Judge work during transient disconnection, but does not attempt general offline authoritative operation. When the event must continue and digital authority cannot be reached/reconciled safely, the established paper continuity model is the preferred authoritative capture fallback.

Recovery later reconciles physical and digital traces into the same logical evaluation without changing authorship or weight.

# Local Draft topology

A local Draft record conceptually contains:

```text
local draft identity
Identity + Participation context
Competition + Encounter
logical Scorecard/server resource ID when known
exact Rubric Version
last confirmed server revision
last confirmed content/basis as needed for reconciliation
current local working content
local edit sequence / saved-at
pending command/idempotency identity
synchronization/conflict state
```

Provider/session bearer credentials are not part of the Draft record.

# Reconnect topology

```text
network available
    ↓
re-establish current session / Identity
    ↓
resolve selected Participation + Access
    ↓
resolve server Scorecard identity + state
    ↓
reconcile uncertain command outcome
    ↓
compare server revision with local base
    ├── same → synchronize pending Draft
    ├── advanced → preserve + reconcile conflict
    ├── Finalized → local work cannot overwrite authority
    └── Access expired → recovery path, no automatic upload
```

# Conflict classes

MUDAC distinguishes at least no-conflict synchronization, idempotent replay, stale-revision conflict, server-already-Finalized, Access-expired/revoked, structural-basis mismatch, uncertain consequential command, and paper/electronic overlap.

# Deliberate deferrals

This contract does not select IndexedDB or another browser persistence API, client-side encryption library, service worker/background-sync mechanics, autosave cadence, WebSocket/SSE transport, offline cache library, merge UI, exact local-retention limits, queue/broker, or AWS connectivity/failover services. These mechanisms must satisfy the `SYNC-*` semantics when selected.