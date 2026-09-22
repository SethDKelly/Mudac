---
type: Architecture Decision
title: 019-B — Architecture Drivers, Quality Attributes, Workload, Trust Boundary & Constraint Qualification
description: Resolves ADQ-001 by deriving and accepting the current architecture driver baseline from closed semantic authority, qualifying historical foundation evidence without reactivating it, establishing quality priorities, bounded live-event workload assumptions, trust boundaries, safe degraded-operation posture, operability/cost/reversibility constraints, evidence thresholds and revisit triggers.
status: stable
tags: [phase-019, architecture, adq-001, drivers, quality-attributes, workload, trust, evidence]
sources:
  - resource: ../canonical/architecture/architecture-drivers.md
  - resource: ../canonical/architecture/architectural-foundation.md
  - resource: ../canonical/project/mandate-context.md
  - resource: ../canonical/project/purpose-needs-success-tensions.md
  - resource: ../canonical/experience/accessibility-resilience.md
  - resource: ../canonical/experience/status-feedback-recovery.md
  - resource: ../canonical/experience/live-operations.md
  - resource: ../canonical/governance/downstream-realization-obligations.md
  - resource: ../canonical/governance/architecture-decision-authority.md
  - resource: ../routing/phase019_architecture_decision_control.json
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T06:31:00Z }
---

# Purpose

019-B resolves ADQ-001.

This is the first accepted bounded architecture decision in Phase 019.

It decides the constraints and tradeoff posture that later architecture choices must use.

It does not select a technology.

# 1. Entry state

~~~text
Phase 019                       ACTIVE
019-A                           COMPLETE
019-B                           NEXT ELIGIBLE / USER AUTHORIZED

ADQ-001                         PLANNED
ADQ-002..010                    PLANNED
accepted ADQ decisions          0 / 10
accepted whole architecture     false

historical architecture         SUSPENDED
Q4 repairs complete             0 / 4
technical probes                0

implementation packages         0
package derivation              false
implementation execution        false
~~~

# 2. Decision

**ADQ-001 — ACCEPTED.**

Selected foundation:

> **Current-semantics-derived, trust-first architecture driver baseline for a bounded bursty live event, with safe degradation/paper continuity, explicit trust boundaries, proportional operational complexity, explicit reversibility, and evidence-bounded quantitative targets.**

Current owner:

> docs/canonical/architecture/architecture-drivers.md

Stable rules:

> DRV-001 through DRV-012

# 3. Current semantic evidence

The decision derives from current authority rather than from historical architecture chronology.

## Project mandate

Current project evidence establishes that MUDAC:

- supports operational judging and outcome lifecycle for a live student data competition;
- is time-bounded and operationally dynamic;
- must support first-time users, phones, interruptions, poor connectivity, accessibility needs and paper operation;
- must preserve meaningful history through correction;
- must keep outcomes explainable;
- must preserve authority separation between technical operation and competition meaning.

The current delivery target remains GitHub → GitHub Actions → AWS ecosystem, but the mandate explicitly states that this does not select particular services or topology.

## Purpose evidence

P-01 through P-09 establish architecture-relevant pressure toward:

- independent judgment;
- fair and bias-aware treatment;
- low-friction accessible participation;
- live operational coordination;
- resilient continuity;
- explainable outcome formation;
- correctable historical authority;
- contextual confidentiality;
- faithful external representation.

The material tensions show why architecture cannot optimize one attribute independently.

## Experience evidence

Current Experience authority requires:

- phone-primary Judge usability;
- accessibility and alternate-input semantic parity;
- safe capability reduction under degraded conditions;
- shared-device/privacy-safe recovery;
- distinction among local working state, confirmed persistence and authoritative state;
- first-class unknown outcome;
- safe convergence rather than duplicate retry;
- paper/electronic continuity on one logical evaluation;
- Organizer live visibility without transferring Judge authorship or leaking protected signals.

## ENG / invariant evidence

ADQ-001 is constrained directly by:

- ENG-001 — semantics precede mechanism;
- ENG-011 — security/disclosure protects semantic authority;
- ENG-012 — accessibility/device continuity preserves parity;
- ENG-013 — availability/recovery preserves truthful authority;
- ENG-014 — Phase-016 scenarios survive downstream;
- ENG-015 — evidence strength matches claim;
- ENG-017 — historical architecture remains evidence;
- INV-009 — accessibility is semantic parity;
- INV-010 — truthful authority under uncertainty.

# 4. Historical candidate qualification

Input:

> docs/canonical/architecture/architectural-foundation.md

Qualification:

~~~text
candidate role               downstream-candidate
Q classes                    Q1 / Q2
semantic repair required     false
technology revalidation      true
eligible comparison input    true
~~~

The candidate contains useful technology-neutral hypotheses:

- semantic/trust integrity before lower-priority quality goals;
- event continuity with safe degradation;
- explicit trust boundaries;
- bounded live-event burst workload;
- distributed complexity only with a driver;
- uncertainty/freshness representation;
- architecture decisions evaluated for cost, reversibility and evidence.

019-B independently revalidated those forces against current owners.

The historical document itself is **not adopted** and its ARCH-* stable IDs remain downstream-candidate IDs.

# 5. Alternatives considered

ADQ-001 is a foundation decision rather than a technology selection, but competing driver postures were still considered.

## Alternative A — Adopt historical Architectural Foundation unchanged

Rejected.

Reason:

The candidate is useful evidence but chronology cannot create authority. Its current-compatible forces must be re-derived from current Project/Experience/Invariant/ENG authority.

## Alternative B — Treat all quality attributes as unranked peers

Rejected.

Reason:

This provides no safe decision rule when live-event speed/availability conflicts with authority correctness, confidentiality or truthful uncertainty.

Current product meaning requires semantic/trust integrity to constrain lower-level optimization.

## Alternative C — Scale-first / distributed-first architecture posture

Rejected.

Reason:

Current evidence shows bounded, bursty live-event operation but no evidence of global/internet-scale traffic or independent service-scaling needs.

Speculative distribution would add coordination, operational and recovery burden without a demonstrated driver.

## Alternative D — Current-semantics-derived, trust-first bounded-live-event baseline

**Selected.**

Reason:

It best explains the current purpose, Experience and ENG obligations while leaving mechanisms open.

# 6. Accepted quality priority

The accepted order is:

~~~text
Tier 1 — semantic / trust integrity
    authority correctness
    fairness / bias protection
    confidentiality / disclosure
    security boundaries
    Provenance / historical truth
    truthful uncertainty

Tier 2 — event-critical continuity
    accessibility
    responsive participation
    interruption resilience
    safe degraded operation
    paper continuity
    recovery

Tier 3 — sustaining quality
    maintainability
    operability
    observability
    recoverability
    cost proportionality
    evolvability
~~~

Tier 2 or Tier 3 cannot justify violating Tier 1.

Within one tier, later decisions must state their specific tradeoffs.

# 7. Workload qualification

Current evidence supports:

- time-bounded event bursts;
- concurrent Judge Draft work;
- bursts of Finalization and other consequential commands;
- frequent Organizer operational reads;
- reconciliation and exception work near live-event closure;
- intermittent recovery/correction;
- less frequent external artifact generation/release.

Current evidence does not establish exact:

- Judge concurrency;
- Organizer concurrency;
- request rate;
- data volume;
- p95/p99 latency;
- uptime SLO;
- RTO;
- RPO.

019-B therefore refuses to invent numbers.

Later runtime/platform work must qualify quantitative targets before claiming sufficiency.

# 8. Trust-boundary qualification

The accepted minimum trust-boundary set is:

1. human ↔ browser/device;
2. browser/device ↔ application authority;
3. authentication ↔ Identity/Participation/Access;
4. application command processing ↔ authoritative persistence;
5. authoritative state ↔ projection/cache/search;
6. Judge authorship ↔ Organizer/support/technical operation;
7. internal authority ↔ Export/Publication/external possession;
8. paper evidence ↔ digital authority;
9. application ↔ external provider;
10. runtime/operator authority ↔ product/data authority.

Later architecture may identify additional boundaries.

It may not remove these without reopening ADQ-001.

# 9. Availability and degraded-operation posture

The accepted posture is:

~~~text
unsafe digital continuation
    ↓
preserve work/evidence
    ↓
report unavailable / pending / unknown truthfully
    ↓
use safe paper continuity where applicable
    ↓
reconcile later to current authority
~~~

This explicitly rejects fabricated digital success as an availability strategy.

It also means later architecture need not build a stronger offline-authority mechanism unless its benefit and semantic safety are demonstrated.

# 10. Accessibility posture

Architecture must preserve accessibility as semantic parity rather than a later UI test.

Later choices must remain compatible with:

- keyboard/nonvisual/alternate input;
- touch and phone-primary use;
- non-color-only status meaning;
- accessible high-consequence confirmation;
- device replacement/re-entry;
- privacy-safe shared-device handling;
- degraded paths that may expose less but not more.

# 11. Operability and cost posture

No exact operating budget is currently established.

The accepted rule is proportionality:

> additional deployment units, services, asynchronous infrastructure, replicated state, caches or provider-specific coupling require a demonstrated quality/workload/security/recovery benefit.

Historical scaffold reuse may be recorded as migration/reuse cost.

It cannot be the primary architecture justification.

# 12. Reversibility posture

Every later material ADQ must identify:

- durable data coupling;
- protocol coupling;
- provider/service dependency;
- migration complexity;
- whether dual-running is plausible;
- what evidence justifies accepting lock-in.

This does not require maximum portability.

It requires conscious lock-in.

# 13. AWS/GitHub delivery constraint

Current Project authority preserves:

~~~text
GitHub → GitHub Actions → AWS ecosystem
~~~

019-B treats this as an environmental delivery constraint.

It does not select:

- compute service;
- persistence service;
- identity service;
- storage service;
- messaging service;
- topology;
- networking;
- backup/DR mechanism.

Those choices remain for their proper ADQs, especially 019-J.

# 14. Evidence calibration

ADQ-001 acceptance uses:

> DOCUMENTATION_REASONING

This evidence is sufficient because the decision concerns current product-derived drivers, not provider/runtime behavior.

019-B authorizes:

~~~text
technical probes = 0
~~~

No executable probe can improve the truth of the current semantic obligations.

# 15. Residual uncertainty

Accepted with bounded uncertainty:

- exact event concurrency and traffic distribution;
- exact latency/SLO targets;
- exact RTO/RPO;
- venue connectivity distribution;
- operating-cost ceiling;
- jurisdiction-specific retention/compliance;
- future provider-specific limits/pricing/behavior.

These items are not blocking because no mechanism that depends on their exact values is selected in 019-B.

# 16. Revisit triggers

ADQ-001 reopens if:

- measured event scale materially exceeds the bounded-event assumption;
- a binding SLO/RTO/RPO appears;
- law/contract changes trust/retention/disclosure constraints;
- a later ADQ cannot satisfy accepted drivers simultaneously;
- the AWS ecosystem delivery constraint changes;
- provider/runtime evidence changes cost/recovery assumptions materially;
- a new product family has materially different workload/trust needs.

# 17. Scenario impact

The ADQ-001 decision directly establishes architecture-evaluation posture for:

- unknown/degraded result;
- adversarial request volume;
- conflicting legitimate authority.

It also supplies cross-cutting constraints for every later Phase-016 scenario.

# 18. Risk disposition

## ERI-02 — historical candidate mistaken for accepted architecture

**Further controlled.**

The historical Architectural Foundation was used as qualified evidence but remains a downstream candidate.

## ERI-03 — architecture emerges from existing implementation

**Further controlled.**

The driver decision is explicitly mechanism-neutral and rejects scaffold convenience as primary evidence.

## ERI-07 / ERI-08 — evidence overclaiming

**Controlled for ADQ-001.**

Acceptance uses documentation reasoning only and makes no runtime/production claim.

## ERI-09 — cross-owner coupling / derived authority leakage

**Carried forward.**

DRV-001/007/008 establish the constraints, but the topology-specific analysis belongs to 019-C and whole-system validation in 019-K.

# 19. Implementation boundary

After ADQ-001 acceptance:

~~~text
accepted bounded architecture decisions  1 / 10
accepted whole architecture              false

active implementation packages            0
package derivation                        false
implementation execution                  false
~~~

G0 — Architecture Accepted remains unsatisfied.

# 20. Exit decision

**019-B — COMPLETE — PASS.**

**ADQ-001 — ACCEPTED.**

Current Phase-019 progression becomes:

~~~text
019-A COMPLETE
019-B COMPLETE
019-C NEXT ELIGIBLE

ADQ-001 ACCEPTED
ADQ-002..010 PLANNED

Q4 repairs complete          0 / 4
technical probes             0
accepted whole architecture  false

implementation packages      0
implementation execution     false
~~~

Next eligible work:

> **019-C — Application Ownership, Boundary, Coordination & Dependency Architecture**

019-C is not automatically authorized by 019-B completion.
