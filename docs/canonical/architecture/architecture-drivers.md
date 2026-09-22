---
type: Accepted Architecture Foundation
title: Current Architecture Drivers, Quality Priorities, Workload & Trust Boundaries
description: Accepted ADQ-001 architecture foundation for MUDAC: current semantic constraints, quality-attribute ordering, bounded live-event workload assumptions, trust boundaries, safe degraded/availability posture, operability/cost/reversibility expectations, downstream delivery context, evidence thresholds and revisit triggers.
status: stable
tags: [architecture, current, drivers, quality-attributes, workload, trust, resilience, accessibility, operability]
sources:
  - resource: ../project/mandate-context.md
  - resource: ../project/purpose-needs-success-tensions.md
  - resource: ../experience/accessibility-resilience.md
  - resource: ../experience/status-feedback-recovery.md
  - resource: ../experience/live-operations.md
  - resource: ../invariants/accessibility-semantic-parity.md
  - resource: ../invariants/truthful-authority-under-uncertainty.md
  - resource: ../governance/downstream-realization-obligations.md
  - resource: ../governance/architecture-decision-authority.md
  - resource: architectural-foundation.md
  - resource: ../../019-architecture-engineering-reentry/019-B-architecture-drivers-quality-attributes-workload-trust-boundary-constraint-qualification.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T06:28:00Z }
---

# Authority

This document is **current accepted architecture authority for ADQ-001 only**.

It establishes the driver/constraint baseline used by later Phase-019 architecture decisions.

It does not select application decomposition, persistence, identity provider, API shape, offline mechanism, client framework, AWS services, or implementation packages.

The preserved historical Architectural Foundation remains downstream-candidate evidence. Its ARCH-* IDs are not reactivated by this decision.

<a id="drv-001"></a>
## DRV-001 — Current semantic authority is the first architecture constraint

Architecture must preserve the current Project, Concept, Synchronization, Dependence, Experience, Policy, Mechanism and Invariant model plus applicable ENG-* obligations.

Implementation convenience, historical code, cloud familiarity or existing topology cannot override that meaning.

A genuine contradiction routes through change governance rather than being hidden as an architecture exception.

<a id="drv-002"></a>
## DRV-002 — Quality priority is semantic/trust integrity, then event continuity, then sustaining quality

Tradeoffs use this ordered posture:

1. **Semantic and trust integrity** — correct authority, fair/bias-aware treatment, privacy/disclosure, evidence/provenance, truthful state and security boundaries.
2. **Event-critical continuity** — accessible participation, responsive live operation, interruption/degraded continuity and safe recovery.
3. **Sustaining quality** — maintainability, operability, observability, recoverability, proportional cost and evolvability.

A Tier-2 or Tier-3 benefit cannot justify violating Tier 1.

Within a tier, later decisions must make material tradeoffs explicit rather than assuming one attribute always dominates.

<a id="drv-003"></a>
## DRV-003 — Safe unavailability or uncertainty is preferred to fabricated authority

For high-consequence operations, failure or degraded service may reduce capability.

It must not create false success, invent failure where the outcome is unknown, duplicate semantic authority, or silently overwrite newer current truth.

Where current authority cannot be established safely, preserve work/evidence and expose the limitation.

<a id="drv-004"></a>
## DRV-004 — Paper continuity is a valid resilience path, not a second authority model

Paper is an established continuity/accommodation channel for live judging.

Architecture may use paper when digital operation cannot safely continue, provided later reconciliation preserves:

- the same logical evaluation;
- Judge semantic authorship;
- exact Evaluation Basis;
- provenance of capture/transcription;
- one evaluation weight;
- current Access/disclosure rules.

Architecture therefore does not need to manufacture unsafe offline authority merely to claim uninterrupted digital availability.

<a id="drv-005"></a>
## DRV-005 — The baseline workload is bounded, bursty and live-event shaped

Current evidence supports a workload characterized by:

- time-bounded competition/event windows;
- concurrent Judge Draft/evaluation activity;
- bursts of Finalization or other consequential actions;
- frequent Organizer operational reads and exception/reconciliation work;
- intermittent correction/recovery activity;
- comparatively occasional Export/Publication generation.

Current evidence does **not** establish a need for speculative internet-scale or globally distributed traffic.

Distributed complexity requires a demonstrated driver.

<a id="drv-006"></a>
## DRV-006 — Exact capacity, latency and recovery targets remain evidence-bounded until quantified

No current authority establishes exact concurrent-user counts, requests/second, p95 latency targets, uptime percentage, RTO or RPO.

Later architecture decisions may use qualitative event-critical needs now, but 019-J/019-K must qualify measurable targets before claiming runtime/platform sufficiency.

The architecture must keep those targets measurable and revisitable rather than burying them in implementation defaults.

<a id="drv-007"></a>
## DRV-007 — Trust boundaries require explicit re-establishment of relevant authority

At minimum, later architecture must treat these as explicit trust boundaries:

- human ↔ browser/device;
- browser/device ↔ application authority;
- authentication proof ↔ Identity/Participation/Access;
- application command processing ↔ authoritative persistence;
- authoritative state ↔ projection/cache/search;
- Judge authorship ↔ Organizer/support/technical operation;
- internal authority ↔ Export/Publication/external possession;
- physical paper evidence ↔ digital authoritative record;
- application ↔ external provider;
- runtime/operator authority ↔ product/data authority.

Crossing a boundary requires relevant identity, authorization, integrity, confidentiality, freshness, provenance or semantic-authority assumptions to be re-established rather than inherited implicitly.

<a id="drv-008"></a>
## DRV-008 — Security and disclosure are semantic-boundary obligations

Architecture must enforce current Access and disclosure meaning at consequential boundaries, not only through presentation.

Technical or administrative privilege does not become Judge/Organizer semantic authority.

When context is uncertain, disclosure may become narrower; it must not broaden for operational convenience.

Abuse/rate/flood controls must protect system and semantic authority without fabricating domain outcomes.

<a id="drv-009"></a>
## DRV-009 — Accessibility, device continuity and degraded operation preserve semantic parity

Accessible, responsive, shared-device, recovery and degraded paths may change mechanics or available capability.

Where an operation remains available, its authority, status, evidence and consequences remain equivalent.

Architecture must not rely exclusively on mouse, hover, QR/camera, color, one orientation, fine-pointer input or a single device context for consequential operation.

A degraded path may safely withhold an operation when prerequisites cannot be established.

<a id="drv-010"></a>
## DRV-010 — Operability and cost must be proportional to demonstrated event needs

Architecture should minimize operational burden and unnecessary distributed coordination while preserving the higher-priority drivers.

Additional services, asynchronous infrastructure, deployment units, replicated stores, caches or provider-specific complexity require a concrete benefit tied to workload, trust, recovery, availability or evolution evidence.

Existing scaffold reuse may reduce migration cost, but is secondary evidence only.

<a id="drv-011"></a>
## DRV-011 — Reversibility and provider/service lock-in are explicit decision dimensions

Later architecture decisions must identify:

- what can be changed without semantic migration;
- what creates durable data/protocol/runtime coupling;
- what would require migration or dual-running;
- what provider-specific capabilities become material dependencies;
- what evidence would justify accepting that lock-in.

Reversibility is not absolute portability; it is an explicit tradeoff against demonstrated benefits.

<a id="drv-012"></a>
## DRV-012 — The current delivery environment constrains context, not service topology

The current Project mandate retains the downstream delivery target:

~~~text
GitHub → GitHub Actions → AWS ecosystem
~~~

For Phase 019 this is treated as an environmental delivery constraint unless later governance explicitly changes it.

It does **not** preselect:

- ECS, Lambda or another compute model;
- RDS or a specific database;
- Cognito or another identity provider;
- S3, SQS or another managed service;
- one deployment topology;
- one networking or disaster-recovery design.

019-J must evaluate the actual AWS realization against these drivers and record any material provider-specific lock-in.

# Evidence and validation posture

ADQ-001 is accepted on current authored semantic/documentation evidence.

No technical probe is necessary to establish these drivers.

Later decisions must use the evidence class capable of closing their specific claim:

- documentation reasoning for semantic/architectural fit;
- external/vendor facts for provider guarantees, limits or pricing;
- bounded probes where documented evidence cannot resolve material behavior;
- integration/runtime evidence for selected mechanisms where necessary;
- production evidence only for production claims.

# Explicitly bounded uncertainties

The following remain open without blocking ADQ-001 acceptance:

- exact event concurrency and request-volume distribution;
- exact latency/SLO requirements;
- exact RTO/RPO;
- concrete venue connectivity distributions;
- concrete operating-cost ceiling;
- jurisdiction-specific retention/compliance requirements;
- provider-specific limits, pricing and operational behavior.

These are not architecture permission to guess.

They are later evidence obligations.

# Revisit triggers

Reopen this driver baseline when credible evidence shows any of the following:

- actual event scale materially exceeds the bounded live-event posture;
- a binding SLO/RTO/RPO or contractual requirement is introduced;
- a jurisdiction/legal requirement changes a trust, retention or disclosure assumption;
- a later ADQ cannot satisfy two accepted drivers simultaneously;
- the AWS ecosystem delivery constraint is explicitly changed;
- provider/runtime evidence materially changes cost, recovery or operability assumptions;
- a new product family introduces materially different workload or trust conditions.

# ADQ-001 accepted decision

Selected foundation:

> **Current-semantics-derived, trust-first architecture driver baseline for a bounded bursty live event, with safe degradation/paper continuity, explicit trust boundaries, proportional operational complexity, explicit reversibility, and evidence-bounded quantitative targets.**

This decision supersedes the historical architectural-foundation.md **for current ADQ-001 driver authority only**.

The historical candidate remains preserved and downstream-classified until final candidate disposition in 019-L.
