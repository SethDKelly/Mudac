# 005-F — Draft Persistence, Synchronization, Offline/Degraded Operation & Conflict Recovery

Status: **Complete**

## Purpose

Define how MUDAC preserves Judge working Drafts and other explicitly recoverable local work through intermittent connectivity, multiple devices, retries, and degraded operation without allowing local state to impersonate server-confirmed authority.

This subgroup consumes the established architecture contracts:

- `ARCH-*` authority/failure/freshness boundaries;
- `DATA-*` relational authority, Versioning, projection, and durable-identity rules;
- `AUTH-*` first-party session, Access, device-loss, and Participation-context rules;
- `API-*` command/query, revision, idempotency, transaction, and uncertainty rules;
- `SC-001`/`SC-002`, `INV-002`, `INV-008`, `INV-010`, Continuity & Paper, and Judge Evaluation experience semantics.

## Core decision

MUDAC supports **local-first preservation of explicitly non-authoritative Draft work**, synchronized against a server-owned Draft through stable logical identity and revision/precondition semantics.

It does **not** provide general offline authoritative operation.

The boundary is:

```text
local/offline permitted
    preserve/edit eligible Draft working content
    queue Draft synchronization intent
    retain last-known read context with freshness markers

server authority required
    Finalize Scorecard
    Finalize Amendment
    create/activate exceptional correction grant
    alter Competition lifecycle
    perform outcome/reconciliation authority changes
    publish/release external representation
    other high-consequence authoritative transitions
```

If server authority cannot be reached reliably, MUDAC reports that condition honestly and uses established paper continuity where the event must continue.

## Draft identity and local state

Local Draft state is always attached to durable semantic identity:

```text
Competition ID
Participation ID
Encounter ID
logical Scorecard ID (once known)
exact Rubric Version ID
last confirmed server Draft revision
local edit sequence/revision
local save timestamp
sync state
```

A device-local Draft is never identified solely by browser tab, URL, Team Alias, or current display order.

Before a server Scorecard ID exists, a stable client-generated draft/intent identifier may be used for create-idempotency and then bound to the server-created logical Scorecard. This identifier cannot create a second evaluation when server uniqueness already resolves an existing Scorecard.

## Local persistence posture

The browser may use durable local application storage for eligible Draft working content so a reload, transient outage, or brief connection loss does not discard Judge work.

Local persistence must:

- be scoped to the authenticated Identity + selected Participation + Competition + logical Draft identity;
- preserve enough base revision information to detect stale synchronization;
- separate unconfirmed local content from last confirmed server state;
- avoid putting provider/session bearer credentials into the Draft store;
- support explicit secure clearing on logout, shared-device handoff, Participation-context switch, access expiry, and security/session revocation;
- minimize retained sensitive content and avoid indefinite post-event local retention.

The exact browser storage API and encryption-at-rest mechanism remain implementation/runtime decisions.

## Synchronization model

MUDAC uses revision-aware synchronization rather than transparent multi-master replication.

Normal connected flow:

```text
server Draft revision N
        ↓
client edits local working copy
        ↓
sync Draft command
    expected revision N
    stable Draft/Scorecard identity
    idempotency key
        ↓
server validates current Access + ownership + Rubric/Encounter basis
        ↓
commit revision N+1
        ↓
client marks local content confirmed at N+1
```

If the client is offline, it may continue editing its eligible local Draft and record pending synchronization intent. Reconnect never permits the client to assume that its base revision is still current.

## Conflict model

Last-write-wins is rejected for Judge-authored evaluation content.

If server revision has advanced since the local base:

```text
local base = 14
server current = 15
local pending edits exist
        ↓
CONFLICT
```

The system must preserve both:

- the current server Draft;
- the conflicting local work.

It must not silently overwrite either.

Where changes are demonstrably non-overlapping and semantically safe, an implementation may offer a deterministic merge preview. Automatic field-level merge is not a blanket rule: score/Note meaning, deletions, structural context, and amendment state can make apparently independent edits semantically incompatible.

The default safe recovery is explicit Judge reconciliation using current server state plus preserved local edits.

## Multi-device behavior

A Judge may legitimately move between devices. Both devices resolve the same Participation and logical Scorecard under `AUTH-011` and `INV-002`.

Optimistic revision checks determine whether one device's pending changes are stale. Device replacement never creates a new logical Scorecard merely to avoid synchronization conflict.

The UI should make it clear which state is:

- confirmed server Draft;
- unsynchronized local work;
- conflicting local work;
- Finalized authoritative Version.

## Finalization boundary

Scorecard Finalization is online-authoritative only.

A client may locally prepare/review a complete Draft, but it cannot create a Finalized Version while disconnected.

```text
complete local Draft
        ↓
network unavailable
        ↓
state = complete Draft, not Finalized
        ↓
reconnect
        ↓
synchronize/reconcile latest Draft
        ↓
explicit Finalize command
        ↓
server commit confirmed
        ↓
Finalized Version
```

If the Finalize request was sent and the response is lost, state is **uncertain**, not Draft and not Finalized by assumption. The client reconciles using the original command/idempotency context under `API-010`.

## Amendment boundary

An Amendment Draft may be locally preserved only after the server has authoritatively established that the Judge currently has the right to amend the target Scorecard and the amendment lineage/basis is known.

Offline state cannot independently open a post-event correction grant, reactivate expired Judge Access, change the authoritative predecessor Version, or Finalize the Amendment.

## Degraded read behavior

Previously loaded read context may remain visible while offline/degraded only when the UI identifies it as cached/last-confirmed information and preserves its freshness/basis.

A cached Team Alias/Division/Encounter/Rubric view does not establish current Access or authority. Sensitive cached data must not survive context expiry/handoff in ways that violate disclosure rules.

## Reconnect sequence

A reconnect should conceptually perform:

```text
1. re-establish current server session/authentication state
2. re-evaluate Participation context and Access
3. resolve logical Draft/Scorecard identity
4. retrieve current server revision / Finalization state
5. reconcile any previously uncertain command outcome
6. compare pending local Draft base revision with current server revision
7. synchronize, merge-with-review, or surface conflict
8. update local confirmed revision
9. resume normal connected operation
```

Local queued work does not bypass steps 1–6 simply because it was created while a valid session previously existed.

## Event completion and revocation

`AUTH-007` remains authoritative during disconnection.

A disconnected Judge device may temporarily be unaware that Event Completed has occurred. Therefore local content cannot prove continuing Access. Once connectivity/session validation resumes, ordinary Judge private-evaluation capability must be denied if Event Completed or another revocation has ended it.

Pending local Draft material is preserved for safe operational recovery only as policy permits; it is not automatically uploaded after Access expiry. Organizer-guided recovery or paper/correction governance may be required.

## Paper fallback and mixed traces

Paper is the authoritative continuity fallback when digital authority is unavailable and judging must continue.

If electronic Draft work and paper work exist for the same Judge × Encounter:

```text
same Participation
same Encounter
same exact Rubric Version
same logical Scorecard
```

must be preserved.

Organizer capture identifies the paper source and capture actor while the Judge remains semantic author. A paper transcription cannot silently overwrite conflicting electronic Judge intent; ambiguity is escalated for explicit reconciliation.

## Conflict classes

The architecture distinguishes at least:

1. **No conflict** — server base unchanged; pending Draft can synchronize.
2. **Idempotent replay** — same Draft mutation already committed; reuse committed result.
3. **Stale revision** — newer server Draft exists; explicit reconciliation required unless deterministic safe merge is proven.
4. **Server Finalized** — local Draft is now historical/uncommitted work and cannot overwrite the Finalized Version.
5. **Access expired/revoked** — local content exists but current principal lacks upload/edit authority.
6. **Structural mismatch** — Encounter/Rubric/Participation/logical identity no longer matches; no automatic merge.
7. **Uncertain consequential command** — reconcile authoritative outcome before allowing another transition.
8. **Paper/electronic overlap** — preserve both traces and converge on one logical Scorecard under capture-channel parity.

## Recovery UX requirements

Recovery surfaces must state:

- what operation was attempted;
- what is definitely confirmed by the server;
- what remains only local;
- whether server state has changed;
- whether Access is still valid;
- whether any consequential command outcome is uncertain;
- what work has been preserved;
- the safe next action.

A generic `Saved`, `Synced`, or `Offline` badge cannot collapse these dimensions.

## Deliberate deferrals

005-F does not select IndexedDB versus another browser store, encryption library, background-sync API, service-worker strategy, WebSocket/SSE transport, exact autosave interval, queue/broker, client-state framework, offline cache package, merge UI, local-retention duration, or AWS connectivity/failover service. 005-H and 005-I will choose client/runtime mechanisms after these semantics are fixed.

## Outcome

005-F establishes an **offline-capable Draft continuity model, not an offline authority model**. Local persistence protects Judge effort; server revision/idempotency semantics protect authority; conflicts preserve both traces; uncertainty remains explicit; and paper remains the safe event-continuity path when authoritative digital operation cannot be trusted.