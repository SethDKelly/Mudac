---
type: Architecture Contract
title: Current Offline Draft, Multi-device, Degraded, Paper & Reconciliation Architecture
description: "Accepted ADQ-006 continuity architecture for MUDAC: server-authoritative Draft identity/currentness, bounded non-authoritative local continuity, revision-aware reconnect, explicit conflict preservation, one-logical-Scorecard multi-device convergence, safe shared-device privacy, no disconnected authoritative transitions, truthful uncertainty, and paper/electronic reconciliation through one evaluation model."
status: stable
tags: [architecture, current, offline, draft, multi-device, degraded, paper, reconciliation, recovery]
sources:
  - resource: architecture-drivers.md
  - resource: application-ownership-boundaries.md
  - resource: persistence-history-recovery.md
  - resource: identity-access-authority.md
  - resource: interface-command-concurrency.md
  - resource: synchronization-recovery.md
  - resource: ../concepts/evaluation-occurrence.md
  - resource: ../concepts/evaluation-obligation.md
  - resource: ../concepts/scorecard.md
  - resource: ../synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../policies/continuity-paper.md
  - resource: ../experience/accessibility-resilience.md
  - resource: ../experience/status-feedback-recovery.md
  - resource: ../experience/authority-lineage-correction.md
  - resource: ../invariants/one-logical-scorecard.md
  - resource: ../invariants/capture-channel-parity.md
  - resource: ../invariants/accessibility-semantic-parity.md
  - resource: ../invariants/truthful-authority-under-uncertainty.md
  - resource: ../../019-architecture-engineering-reentry/019-G-Q4R-003-synchronization-recovery-semantic-repair.md
  - resource: ../../019-architecture-engineering-reentry/019-G-offline-draft-multi-device-degraded-paper-reconciliation-architecture.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T12:10:00-05:00 }
---

# Authority

This document is **current accepted architecture authority for ADQ-006**.

It establishes continuity, local Draft, multi-device, degraded-operation, paper fallback and reconciliation architecture.

It does not select the exact browser storage API/library, client encryption implementation, autosave cadence, service worker/background-sync mechanism, conflict UI, network detector, queue/broker, cloud runtime, or device-management product.

<a id="rcv-001"></a>
## RCV-001 — The server remains authoritative for logical Draft identity and currentness

A client may preserve working content locally, but authoritative Draft identity/current revision remains owned by the server-side application/persistence boundary.

Local durability does not establish:

- an authoritative Draft revision;
- Finalization;
- Scorecard authority;
- Evaluation Obligation satisfaction;
- Access;
- Competition lifecycle state;
- Outcome authority;
- Publication authority.

<a id="rcv-002"></a>
## RCV-002 — Local continuity records are semantic recovery envelopes, not offline domain replicas

Eligible local state is the minimum continuity material needed to resume the same logical work.

A recovery envelope is bound, as applicable, to:

- Competition;
- authenticated MUDAC Identity;
- selected Competition Participation;
- Evaluation Obligation;
- Evaluation Occurrence/context reference;
- logical Scorecard identity when known;
- exact Evaluation Basis / authoritative Rubric Version;
- last confirmed authoritative Draft revision;
- pending local working content and local edit metadata.

Browser tab, URL, Team Alias, display order or device identity is not sufficient semantic identity.

Provider bearer/refresh credentials are never Draft payload.

<a id="rcv-003"></a>
## RCV-003 — Local persistence is explicitly non-authoritative and privacy-bounded

Local working persistence exists to reduce work loss during transient interruption.

It is:

- scoped to an explicit MUDAC Identity/Participation/Competition context;
- minimized to continuity need;
- distinguishable from server-confirmed state;
- subject to cleanup/expiry policy;
- inaccessible to a later shared-device participant through ordinary application flow.

Exact storage technology and cryptographic mechanism remain downstream choices.

<a id="rcv-004"></a>
## RCV-004 — Reconnect begins with current identity, authority and basis resolution

Before pending work can affect authoritative Draft state, the application re-establishes:

1. valid application session / MUDAC Identity;
2. selected Competition Participation;
3. current Access;
4. current Evaluation Obligation and Evaluation Occurrence/context;
5. exact current-relevant Evaluation Basis relationship;
6. logical Scorecard identity/state;
7. current authoritative Draft revision or Finalized state.

A disconnected client does not carry indefinite authority forward from an earlier session.

<a id="rcv-005"></a>
## RCV-005 — Ordinary Draft synchronization is revision-aware and uses current CMD authority

Eligible Draft synchronization uses the accepted command/concurrency architecture:

- stable semantic target;
- expected authoritative revision/current-state precondition;
- current server-side Access evaluation;
- domain uniqueness;
- operation identity/idempotency where retry exposure warrants it.

A local save is never reported as server-confirmed merely because browser persistence succeeded.

<a id="rcv-006"></a>
## RCV-006 — Stale conflicts preserve both authoritative state and pending authored work

If the server Draft has advanced incompatibly beyond the local confirmed base:

- current server state remains intact;
- pending local Judge-authored work is preserved;
- the application exposes a conflict/reconciliation state;
- silent last-write-wins is prohibited.

Recovery must not erase either newer authority or recoverable unsynchronized intent merely to simplify state.

<a id="rcv-007"></a>
## RCV-007 — Automatic merge requires demonstrable semantic independence

Automatic merge is allowed only where the system can demonstrate that the changes commute without changing evaluation meaning, basis, deletion intent, authorship, structural identity or authority.

When that cannot be established, reconciliation is explicit.

A generic field-level or CRDT merge does not become safe merely because it is mechanically possible.

<a id="rcv-008"></a>
## RCV-008 — Multiple devices converge on one logical Scorecard

Device replacement, concurrent devices, tabs, retries or recovered local traces do not create additional evaluation weight or parallel logical Scorecards.

All legitimate traces for one Evaluation Obligation converge against the same logical Scorecard lineage under INV-002.

Concurrency may produce:

- clean synchronization;
- stale conflict;
- already-current result;
- Access denial;
- Finalized/current-state rejection;
- recovery-required state.

It must not manufacture a second evaluation.

<a id="rcv-009"></a>
## RCV-009 — Disconnected clients cannot establish high-consequence authority

MUDAC does not provide general offline authoritative operation.

While disconnected, a client may preserve eligible Draft work but cannot authoritatively:

- Finalize a Scorecard;
- establish an amendment/correction authority transition;
- grant Access;
- change Competition lifecycle;
- declare an official outcome;
- publish/release an external representation.

Authority-establishing commands require reachable authoritative application state and current precondition evaluation.

<a id="rcv-010"></a>
## RCV-010 — Consequential intent is not blindly auto-executed after disconnection

A user may locally preserve working preparation for a later consequential action, but a disconnected authority-establishing command is not converted into a blind durable outbox command that later executes under stale assumptions.

On reconnect, the application first resolves current authority and then requires the accepted command contract to establish the transition.

Where a previously transmitted command has an uncertain outcome, CMD-014/CMD-022 reconciliation applies before any new transition is attempted.

<a id="rcv-011"></a>
## RCV-011 — Shared-device handoff terminates recoverability through the prior active context

Logout, explicit capacity/Participation handoff, security invalidation or shared-device reuse must prevent the next participant from receiving ordinary access to the prior participant's private local continuity state.

Recovery for an interrupted prior participant may remain possible only through a deliberately reauthenticated/re-authorized path that restores the matching MUDAC Identity and Participation context.

Exact local erasure/locking/encryption mechanics are selected later, but semantic isolation is mandatory.

<a id="rcv-012"></a>
## RCV-012 — Cached reads are stale-capable evidence, never current authority

Previously loaded Rubric, Team, status or event context may support continuity while degraded only with truthful last-confirmed/freshness semantics where material.

Cached data:

- cannot establish current Access;
- cannot prove an authoritative action succeeded;
- cannot override a newer server state;
- cannot broaden disclosure during a role/context change.

High-consequence action resumes against current server authority.

<a id="rcv-013"></a>
## RCV-013 — Expired or revoked Access blocks automatic synchronization

If current Access no longer permits ordinary Judge editing, pending private local work is not automatically uploaded merely because it was created while Access previously existed.

The material may be:

- retained locally within governed recovery bounds;
- reconciled through an authorized recovery/correction process;
- represented through paper/source recovery where applicable;
- discarded under policy.

It does not revive stale Judge authority.

<a id="rcv-014"></a>
## RCV-014 — Paper fallback is an alternate capture channel, not offline digital authority

When digital authoritative continuity cannot be trusted and event operation must continue, paper may become the operational capture fallback under current Continuity & Paper policy.

Paper preserves:

- the same Judge/evaluator;
- Evaluation Occurrence/context;
- Evaluation Obligation;
- exact Evaluation Basis;
- Criterion/Note/Scorecard meaning;
- evaluation weight.

Paper capture does not create a second evaluation model.

<a id="rcv-015"></a>
## RCV-015 — Paper and electronic traces reconcile to one logical evaluation with provenance

When local/electronic and paper traces overlap:

- both are associated with the same intended Evaluation Obligation/logical Scorecard;
- capture Actor and represented Judge authority remain distinct;
- physical source identity/provenance is preserved;
- ambiguous intent remains ambiguous;
- duplicate traces do not become duplicate votes.

A paper transcription remains non-authoritative until the current source-fidelity and Judge-intent conditions are satisfied.

If one path already established authority, another conflicting trace cannot silently supersede it.

<a id="rcv-016"></a>
## RCV-016 — Continuity status preserves durability, synchronization, authority, conflict and uncertainty separately

The client-visible model can distinguish, where applicable:

- local working state;
- local durable / not yet server-confirmed;
- synchronizing;
- server-confirmed Draft revision;
- stale-base conflict;
- Access-expired/recovery-required;
- authoritative Finalized Version;
- consequential result unknown / reconciliation required;
- paper capture pending verification;
- paper-origin authority confirmed.

Generic `Saved`, `Synced`, `Offline`, `Submitted` or `Done` labels must not collapse these distinctions.

<a id="rcv-017"></a>
## RCV-017 — Degraded operation reduces capability rather than weakening semantics

If current Access, exact basis, prior command outcome or another consequential precondition cannot be established safely, the operation may become unavailable.

The system should preserve recoverable work and explain known limitations.

It must not offer a lower-authority shortcut merely to appear continuously available.

<a id="rcv-018"></a>
## RCV-018 — Continuity mechanisms remain replaceable behind the architecture contract

ADQ-006 intentionally selects semantic continuity behavior, not a specific browser/runtime mechanism.

Later ADQ-008/implementation work may choose among appropriate:

- browser durable storage;
- in-memory plus durable hybrid state;
- encrypted local records;
- cross-tab coordination;
- background retry facilities.

ADQ-009 may select queue/runtime mechanisms for semantically separable asynchronous work.

Those choices must preserve RCV-001..017.

# Baseline continuity topology

~~~text
Judge edits
  → local working state
  → optional bounded local durable continuity
  → reconnect/current session
  → resolve Identity + Participation + Access
  → resolve Obligation + Occurrence + Basis + logical Scorecard
  → compare last-confirmed revision with current authoritative Draft
      ├─ compatible → synchronize through CMD boundary
      ├─ stale      → preserve both + reconcile
      ├─ Finalized  → local work cannot overwrite authority
      └─ no Access  → governed recovery path
~~~

# Multi-device topology

~~~text
device A local trace ─┐
device B local trace ─┼─> one logical Scorecard
paper source ─────────┘      + one current authority lineage
~~~

No trace independently multiplies evaluation weight.

# Failure / uncertainty boundary

~~~text
local save succeeded
  != server Draft confirmed
  != Scorecard Finalized

request timed out
  != command failed

paper captured
  != paper-origin Scorecard authority confirmed
~~~

# Evidence posture

ADQ-006 acceptance uses **DOCUMENTATION_REASONING**.

No bounded technical probe is required to decide the semantic architecture.

Implementation must later supply executable evidence for at least:

- local-vs-server state distinction;
- stale revision conflict preservation;
- two-device convergence;
- same-logical-Scorecard uniqueness;
- logout/shared-device privacy boundary;
- revoked-Access reconnect;
- uncertain transmitted command reconciliation;
- offline Finalization prohibition;
- paper/electronic duplicate convergence;
- paper/electronic disagreement preservation.

# Revisit triggers

Reopen ADQ-006 when credible evidence shows:

- event operation requires general disconnected authority rather than bounded Draft continuity;
- browser/platform constraints cannot preserve continuity/privacy safely;
- measured multi-device conflict frequency makes explicit reconciliation operationally unacceptable;
- local continuity retention creates unacceptable privacy/compliance risk;
- current paper fallback cannot preserve required basis/provenance at event scale;
- service extraction invalidates the assumed command/current-state reconciliation boundary;
- whole-architecture validation exposes unresolved duplication, stale-authority or degraded-operation risk.

Whole-architecture acceptance remains false until 019-L.
