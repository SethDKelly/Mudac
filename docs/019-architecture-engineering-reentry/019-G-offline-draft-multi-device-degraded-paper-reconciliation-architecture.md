---
type: Architecture Decision
title: 019-G — Offline Draft, Multi-device, Degraded, Paper & Reconciliation Architecture
description: "Resolves ADQ-006 after Q4R-003 by comparing online-only continuity, general local-first/offline authority, blind command-outbox recovery, and bounded non-authoritative local Draft continuity with server-authoritative revision reconciliation and paper fallback; accepts the bounded continuity model."
status: stable
tags: [phase-019, architecture, adq-006, offline, draft, multi-device, degraded, paper, reconciliation]
sources:
  - resource: ../canonical/architecture/offline-continuity-reconciliation.md
  - resource: ../canonical/architecture/synchronization-recovery.md
  - resource: 019-G-Q4R-003-synchronization-recovery-semantic-repair.md
  - resource: ../canonical/architecture/architecture-drivers.md
  - resource: ../canonical/architecture/application-ownership-boundaries.md
  - resource: ../canonical/architecture/persistence-history-recovery.md
  - resource: ../canonical/architecture/identity-access-authority.md
  - resource: ../canonical/architecture/interface-command-concurrency.md
  - resource: ../canonical/policies/continuity-paper.md
  - resource: ../canonical/experience/accessibility-resilience.md
  - resource: ../canonical/experience/status-feedback-recovery.md
  - resource: ../canonical/experience/authority-lineage-correction.md
  - resource: ../canonical/invariants/one-logical-scorecard.md
  - resource: ../canonical/invariants/capture-channel-parity.md
  - resource: ../canonical/invariants/accessibility-semantic-parity.md
  - resource: ../canonical/invariants/truthful-authority-under-uncertainty.md
  - resource: ../routing/phase019_architecture_decision_control.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T12:10:00-05:00 }
---

# Purpose

019-G resolves ADQ-006.

It defines how MUDAC preserves Judge work through transient disconnection, multiple devices, shared-device handoff, degraded operation and paper fallback while preserving one logical evaluation and refusing to manufacture offline authority.

# 1. Entry state

~~~text
Phase 019                       ACTIVE
019-A/B/C/D/E/F                 COMPLETE
019-G                           NEXT ELIGIBLE / USER AUTHORIZED

ADQ-001..005                    ACCEPTED
ADQ-006                         PLANNED
ADQ-007..010                    PLANNED

Q4R-001 / Q4R-002              COMPLETE
Q4R-003                         REQUIRED
Q4 repairs complete             2 / 4
technical probes                0

accepted whole architecture     false
implementation packages         0
implementation execution        false
~~~

# 2. Q4 prerequisite

019-G completed:

> **Q4R-003 — Historical Synchronization / Offline Recovery Semantic Repair**

The repair translates the historical Encounter-era grouping into current:

- Evaluation Occurrence;
- Evaluation Obligation;
- logical Scorecard;
- exact Evaluation Basis / Rubric Version;
- current Competition Participation and Access.

It excludes historical client/runtime selections including IndexedDB, service-worker/background-sync assumptions, SQS and AWS recovery choices from inherited authority.

The historical candidate remains unchanged.

# 3. Decision

**ADQ-006 — ACCEPTED.**

Selected architecture:

> **Server-authoritative logical Draft identity/currentness with bounded non-authoritative local Draft continuity; stable current semantic binding; revision-aware reconnect through current IAM/CMD authority; explicit stale-conflict preservation; one-logical-Scorecard multi-device convergence; no disconnected high-consequence authority or blind consequential outbox execution; privacy-safe shared-device recovery; stale-capable cached reads; truthful continuity status; and paper/electronic fallback converging through one evaluation model with preserved provenance and ambiguity.**

Current owner:

> docs/canonical/architecture/offline-continuity-reconciliation.md

Stable rules:

> RCV-001 through RCV-018

# 4. Current constraints

ADQ-006 preserves:

- ENG-005 — one logical evaluation/evidence/authorship integrity;
- ENG-007 — current-state, retry, concurrency and uncertainty preserve owner truth;
- ENG-008 — offline/device/paper traces preserve continuity without independent authority;
- ENG-011 — Access/disclosure security remains current;
- ENG-012 — device/degraded paths preserve semantic parity;
- ENG-014 — Phase-016 scenario seeds remain mandatory;
- ENG-017 — historical architecture remains evidence;
- INV-002 — one logical Scorecard per Evaluation Obligation;
- INV-008 — capture-channel parity;
- INV-009 — accessibility semantic parity;
- INV-010 — truthful authority under uncertainty;
- DRV-001/002/003/005/006/007/010/011;
- PST-001/002/003/009/011/016;
- IAM-005/006/007/009/017;
- CMD-004/008/011/013/014/015/022.

# 5. Historical candidate qualification

Input:

> docs/canonical/architecture/synchronization-recovery.md

After Q4R-003:

~~~text
Q1 / Q2 / Q4                   QUALIFIED_AFTER_REVISION
semantic repair complete       yes
comparison eligible            yes
historical authority           suspended
mechanism/runtime choices      require fresh selection
~~~

Useful retained hypotheses include:

- local continuity is non-authoritative;
- stable semantic identity + confirmed base;
- revision-aware synchronization;
- conflict preservation;
- safe-only automatic merge;
- multi-device convergence;
- server-only authoritative transitions;
- uncertain-result reconciliation;
- reconnect Access/currentness checks;
- cached-state disclosure bounds;
- paper/electronic convergence;
- multidimensional status.

# 6. Alternatives

## Alternative A — Adopt the repaired historical candidate unchanged

Strengths:

- already addresses most continuity failure modes;
- strong conflict and paper convergence reasoning;
- conservative authority posture.

Weaknesses:

- still carries historical mechanism selections and old architecture references;
- exact local client storage belongs to ADQ-008;
- queue/runtime choices belong to ADQ-009;
- current IAM/CMD/PST decisions now provide stronger upstream contracts.

**Rejected as-is.**

Its strongest semantic hypotheses are re-established under RCV-*.

## Alternative B — Online-only digital operation with paper fallback

Pattern:

~~~text
connected → server Draft only
disconnected → no digital Draft persistence
event continuity → paper
~~~

Strengths:

- smallest client state/privacy surface;
- minimal digital conflict complexity;
- very clear server authority.

Weaknesses:

- transient connectivity can discard substantial Judge work;
- unnecessary paper switching for short interruptions;
- weak device-replacement continuity;
- poorer fit for live event resilience.

**Rejected as baseline.**

Paper remains fallback, but bounded local Draft continuity is justified.

## Alternative C — General local-first / CRDT-style offline application authority

Pattern:

~~~text
each client owns durable local replica
  → edits/finalization proceed offline
  → peers/server merge later
~~~

Strengths:

- strongest disconnected availability;
- flexible multi-device editing;
- reduced dependence on immediate server connectivity.

Weaknesses:

- difficult to preserve current Access and exact authority preconditions;
- semantic merge of scores, deletions, basis and Finalization is not generally commutative;
- risks duplicate evaluation authority;
- increases privacy and synchronization state substantially;
- current event evidence does not justify this complexity.

**Rejected.**

MUDAC preserves Draft work offline, not authority.

## Alternative D — Durable offline command outbox with automatic replay of all intent

Pattern:

~~~text
offline action
  → local outbox
  → reconnect
  → auto-execute command
~~~

Strengths:

- simple offline interaction model;
- eventual delivery for user intent;
- convenient for transient disconnects.

Weaknesses:

- high-consequence intent may become stale or unauthorized before replay;
- can hide changed basis/currentness;
- makes “queued” easy to confuse with “committed”;
- duplicates CMD lost-response handling with a second command authority model.

**Rejected for consequential actions.**

Ordinary Draft synchronization may resume automatically after current revalidation; authority-establishing commands do not blindly replay.

## Alternative E — Bounded local Draft continuity + server-authoritative reconciliation + paper fallback

Characteristics:

- local persistence only for eligible non-authoritative continuity;
- stable semantic binding to current Evaluation Occurrence/Obligation/Scorecard/Basis;
- server authoritative Draft currentness/revision;
- current IAM revalidation on reconnect;
- optimistic current-state synchronization;
- preserve both sides on stale conflict;
- automatic merge only where demonstrably safe;
- one logical Scorecard across devices;
- no disconnected authoritative Finalization;
- no blind consequential outbox replay;
- paper parity and provenance;
- truthful local/sync/conflict/unknown status.

**Selected.**

# 7. Local continuity boundary

A local record is a recovery envelope around one intended logical evaluation.

It contains only the current identifiers and working state needed to re-associate work safely.

It does not become a complete local domain database.

The architecture deliberately avoids defining browser technology in 019-G.

# 8. Reconnect and synchronization

Reconnect is not “flush pending writes.”

It is:

~~~text
reauthenticate / re-establish session as needed
  → resolve Identity + Participation
  → evaluate current Access
  → resolve current Obligation / Occurrence / Basis / logical Scorecard
  → resolve current Draft revision / Finalized state
  → compare local confirmed base
  → synchronize, conflict, reject or enter recovery
~~~

This composes IAM, CMD and PST rather than creating a parallel synchronization authority.

# 9. Conflict model

At minimum 019-G recognizes:

- no-conflict Draft synchronization;
- equivalent retry/replay;
- stale authoritative Draft revision;
- logical Scorecard already Finalized;
- Participation/Access expired or revoked;
- Evaluation Basis/structural-context mismatch;
- uncertain previously transmitted consequential command;
- multiple-device competing local traces;
- paper/electronic overlap or disagreement.

Conflicts preserve evidence instead of guessing.

# 10. Multi-device model

Each device is a continuity surface, not an evaluation owner.

Two devices with pending work still target one logical Scorecard.

The server-side current revision and domain uniqueness prevent device count from multiplying evaluation weight.

019-G does not select peer-to-peer synchronization.

# 11. Disconnected consequential actions

A disconnected client may help a Judge prepare work, but cannot establish authority.

If a command was actually sent before transport failed, the result is **unknown** until CMD reconciliation resolves it.

If a command was never sent because the client was offline, it remains uncommitted user intent and is not automatically treated as a successful or pending authority transition.

# 12. Shared-device/privacy boundary

Local continuity is partitioned by application Identity/Participation context.

Handoff does not merely change visible navigation; it ends ordinary access to the prior private context.

Exact browser erasure, encryption-at-rest, key handling and retention window remain downstream selection/evidence questions.

# 13. Paper boundary

Paper is not a failure-mode shadow domain.

It is an alternate capture/source channel governed by the same:

- Evaluation Occurrence;
- Evaluation Obligation;
- Judge authorship;
- Evaluation Basis;
- Scorecard meaning;
- evaluation weight.

Organizer transcription/capture does not make Organizer the semantic evaluator.

# 14. Paper/electronic reconciliation

When both channels exist:

~~~text
same intended obligation
  + electronic/local trace
  + identified paper source
  → one logical Scorecard
  → provenance-preserved reconciliation
~~~

If authority has already been established, a conflicting second trace cannot silently overwrite it.

Current amendment/capture-correction semantics apply where legitimate.

# 15. Status model

Continuity state is multidimensional.

A usable implementation must not collapse:

~~~text
local durable
server confirmed
synchronized
stale
conflicting
Finalized authoritative
Access expired
paper pending verification
result unknown
~~~

into one generic “saved” state.

# 16. Evidence

Acceptance evidence class:

> **DOCUMENTATION_REASONING**

No bounded technical probe is necessary to select ADQ-006.

Later executable evidence must cover:

- two-device stale conflict;
- same logical evaluation uniqueness;
- offline Draft recovery;
- current Access revalidation;
- logout/shared-device privacy;
- offline Finalization prohibition;
- uncertain sent-command reconciliation;
- paper/electronic duplicate convergence;
- paper/electronic disagreement;
- truthful status transitions.

# 17. Reversibility / lock-in

The decision intentionally commits to:

- server-authoritative Draft currentness;
- bounded local non-authoritative continuity;
- revision-aware reconciliation;
- no general offline authoritative execution;
- one-logical-evaluation device/paper convergence.

It does not commit to:

- IndexedDB;
- localStorage;
- a state-management library;
- service workers;
- background sync;
- client-side encryption library;
- a queue/broker;
- cloud provider/runtime;
- exact retention window.

This keeps ADQ-008 and ADQ-009 free to choose mechanisms against current evidence.

# 18. Residual uncertainty

Open downstream questions include:

- exact browser durable-storage mechanism;
- exact local encryption/locking strategy;
- exact local retention/cleanup window;
- autosave cadence and write batching;
- cross-tab coordination;
- whether background retry materially improves experience;
- safe automatic-merge field classes, if any;
- local storage quota/eviction behavior;
- exact offline/online detection behavior;
- conflict-resolution interaction design;
- event-specific paper identifier/printing mechanics.

# 19. Scenario impact

ADQ-006 directly closes architecture posture for:

- duplicate/offline Draft convergence;
- shared-device context handoff;
- paper/electronic capture disagreement;
- unknown/degraded result;
- multiple legitimate device traces.

Executable scenario evidence remains later validation work.

# 20. Risk disposition

## ERI-02 — historical candidate mistaken for current architecture

**Controlled.**

Current authority is RCV-*; historical SYNC-* remains candidate evidence.

## ERI-04 — stale semantic binding survives reuse

**CLOSED for synchronization/recovery.**

Encounter-era grouping is translated to Evaluation Occurrence + Evaluation Obligation + Scorecard + Evaluation Basis through Q4R-003.

## ERI-07 — degraded/offline complexity

**Materially reduced; carried to 019-K.**

The selected model intentionally rejects general offline authority and unrestricted merge.

## ERI-09 — coordination/derived-authority leakage

**Materially reduced; carried to 019-K.**

Continuity traces coordinate with natural owners and cannot establish independent product authority.

# 21. Implementation boundary

After 019-G:

~~~text
accepted bounded decisions       6 / 10
Q4 repairs complete              3 / 4
technical probes                 0

accepted whole architecture      false

implementation packages          0
package derivation               false
implementation execution         false
~~~

G0 remains unsatisfied.

# 22. Exit decision

**019-G — COMPLETE — PASS.**

**Q4R-003 — COMPLETE.**

**ADQ-006 — ACCEPTED.**

Next eligible:

> **019-H — Artifact, Export, Publication, External Representation & Delivery Architecture**

019-H is not automatically authorized.
