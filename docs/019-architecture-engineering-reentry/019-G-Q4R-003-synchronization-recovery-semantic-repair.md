---
type: Architecture Candidate Repair
title: 019-G Q4R-003 — Historical Synchronization / Offline Recovery Semantic Repair
description: "Repairs the suspended Draft Synchronization, Offline & Recovery candidate for current Phase-019 comparison by translating Encounter-era grouping assumptions to current Evaluation Occurrence, Evaluation Obligation, Scorecard and Evaluation Basis authority; separating reusable continuity hypotheses from superseded semantic bindings and inherited client/runtime mechanisms."
status: stable
tags: [phase-019, architecture, q4, repair, offline, draft, multi-device, degraded, paper, reconciliation]
sources:
  - resource: ../canonical/architecture/synchronization-recovery.md
  - resource: ../canonical/concepts/evaluation-occurrence.md
  - resource: ../canonical/concepts/evaluation-obligation.md
  - resource: ../canonical/concepts/scorecard.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../canonical/policies/continuity-paper.md
  - resource: ../canonical/invariants/one-logical-scorecard.md
  - resource: ../canonical/invariants/capture-channel-parity.md
  - resource: ../canonical/invariants/truthful-authority-under-uncertainty.md
  - resource: ../canonical/architecture/persistence-history-recovery.md
  - resource: ../canonical/architecture/identity-access-authority.md
  - resource: ../canonical/architecture/interface-command-concurrency.md
  - resource: ../canonical/governance/architecture-decision-authority.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T12:10:00-05:00 }
---

# Purpose

Complete Q4R-003 before the historical synchronization/recovery candidate participates in ADQ-006 comparison.

The historical source remains unchanged.

This record translates useful continuity hypotheses into current semantic language without inheriting obsolete ownership, old architecture identifiers, or historical implementation/runtime selections.

# Candidate

> docs/canonical/architecture/synchronization-recovery.md

Qualification before repair:

~~~text
Q1 / Q2 / Q4                 QUALIFIED_AFTER_REVISION
authority                    suspended candidate
comparison eligible          false
blocking repair              Q4R-003
stale binding                Encounter-era grouping assumptions
~~~

# Stale semantic binding

The historical candidate binds local Draft and synchronization identity to an `Encounter`-era grouping.

Current Concept Design separates those responsibilities.

Current translation:

~~~text
historical Encounter grouping
  → Evaluation Occurrence       actual evaluation event/context
  + Evaluation Obligation       responsibility that may be satisfied
  + logical Scorecard           one evaluation evidence lineage
  + exact Evaluation Basis      authoritative Rubric Version
  + Competition-scoped Participation / current Access
~~~

A local/device continuity record therefore cannot use an obsolete Encounter aggregate as its semantic owner.

It preserves the stable current identities needed to recover the same logical work.

# Current authority translation

A continuity target is resolved from current authority, as applicable:

~~~text
Competition
  + authenticated MUDAC Identity
  + selected Competition Participation
  + Evaluation Obligation
  + Evaluation Occurrence/context reference
  + logical Scorecard identity when established
  + exact Evaluation Basis / Rubric Version
  + last confirmed authoritative Draft revision
~~~

No one field above independently grants authority.

Current Access is re-evaluated at synchronization/command time.

# Retained candidate hypotheses

The following hypotheses survive semantic repair as comparison inputs:

1. local persistence is continuity state, not semantic authority;
2. local work is bound to stable semantic identity and a confirmed server base;
3. authoritative Draft currentness remains server-owned;
4. synchronization uses revision/current-state preconditions;
5. stale conflicts preserve both current server state and pending local Judge work;
6. automatic merge is allowed only where semantic safety is demonstrable;
7. multiple devices converge on one logical Scorecard;
8. authoritative transitions require reachable server authority;
9. uncertain consequential outcomes reconcile before repetition;
10. reconnect re-establishes Identity/Participation/Access and current owner state;
11. cached reads remain explicitly stale-capable and disclosure-bounded;
12. expired/revoked Access blocks ordinary automatic upload;
13. paper and electronic traces converge on one logical evaluation;
14. status distinguishes local durability, server confirmation, conflict, uncertainty and authority;
15. degraded operation may reduce capability rather than invent weaker authority.

# Excluded obsolete or premature content

The repaired candidate does **not** carry forward:

- `Encounter` as a current semantic owner/aggregate;
- historical `ARCH-*`, `AUTH-*`, `API-*`, `FE-*`, `AWS-*` or `SYNC-*` identifiers as current authority;
- historical module boundaries as already accepted;
- IndexedDB as an already selected storage mechanism;
- service workers/background synchronization as selected mechanisms;
- SQS or any queue as an already selected synchronization mechanism;
- AWS/runtime recovery choices as accepted by ADQ-006;
- provider/session bearer credentials as local Draft payload;
- general offline authoritative operation;
- automatic last-write-wins;
- automatic conflict merge when semantic safety is uncertain.

Client storage belongs to ADQ-008 / implementation selection.

Queue/runtime topology belongs to ADQ-009.

# Repaired comparison statement

The historical candidate may now be compared as this current hypothesis:

> **Preserve bounded non-authoritative local Draft continuity against a server-authoritative logical Scorecard and exact Evaluation Basis; bind each local trace to current Evaluation Occurrence/Obligation and Participation context plus a last-confirmed authoritative Draft revision; reconcile reconnects using current Identity/Participation/Access and optimistic current-state checks; preserve both sides of stale conflicts rather than silently overwrite; converge multiple devices and paper/electronic traces on one logical evaluation; prohibit disconnected authority-establishing transitions; and expose local, synchronized, stale, conflicting and unknown states truthfully.**

# Repair decision

**Q4R-003 — COMPLETE.**

~~~text
historical source rewritten        NO
current semantic translation       YES
comparison eligible                YES
candidate adopted                  NO
implementation selected            NO
~~~

Q4R-003 repairs evidence. It does not accept ADQ-006.
