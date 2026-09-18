---
type: Experience Contract
title: Accessibility, Responsive & Degraded-Operation Mapping
description: Current mapping for accessible interaction, responsive presentation, interruption/device recovery, degraded connectivity and paper fallback with semantic parity across MUDAC authority and disclosure rules.
status: stable
tags: [experience, mapping, accessibility, responsive, resilience, degraded-operation, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-J-accessibility-degraded-operation-status-feedback-recovery-semantic-parity-mapping.md
  - resource: ../concepts/access.md
  - resource: ../policies/continuity-paper.md
  - resource: ../invariants/accessibility-semantic-parity.md
  - resource: ../invariants/truthful-authority-under-uncertainty.md
  - resource: ../invariants/one-logical-scorecard.md
  - resource: judge-evaluation.md
  - resource: authority-lineage-correction.md
  - resource: external-representation-release.md
---

# Purpose

Define how alternate interaction and operating conditions preserve the same MUDAC semantics rather than creating a second product or lower-authority path.

# Semantic parity

Accessibility, responsive layout, degraded connectivity, device replacement and paper fallback may change mechanics, density, channel or timing.

They do not change domain meaning.

```text
ordinary-path authority
  = accessible-path authority
  = responsive-path authority
  = degraded/recovery-path authority
  = paper/assisted-path authority
```

where the same operation is available.

A degraded path may make an operation unavailable when its prerequisites cannot be established safely. It must not replace the operation with a weaker semantic shortcut.

# Accessibility is cross-cutting

Accessibility is not a product mode, Competition state or alternate workflow.

Core operations should reasonably support WCAG 2.2 AA-oriented interaction and must not depend solely on:

- mouse;
- hover;
- camera/QR;
- gesture-only interaction;
- color;
- one orientation;
- fine-pointer precision.

Keyboard, touch, nonvisual interaction, large text and alternate input must expose equivalent legitimate actions and explanations where those actions are available.

# Visual treatment cannot carry authority alone

Authority or status meaning must not depend only on color, iconography, spatial grouping, animation or hover.

Accessible representations must remain able to distinguish subjects such as:

```text
Scorecard Draft
Scorecard Finalized
Evaluation Obligation Outstanding
Competition Event Completed
Competition Finalized
Outcome Declaration Affected
Export Stale
Publication Withdrawn
```

These are not generic variants of `done` or `inactive`.

# Responsive semantic hierarchy

Responsive/narrow presentation may progressively disclose detail while preserving the consequence hierarchy:

```text
subject / current authority
  → material warning or blocker
  → basis / explanation
  → legitimate action
  → consequence / confirmation
```

This is not a prescribed layout.

Organizer dense views may compress tables/summaries, but a blocker or authority consequence cannot become undiscoverable before its related high-consequence action.

Judge work remains capable of phone-primary completion without changing obligation, Rubric, Scorecard or Finalization semantics.

# Assistance does not transfer authorship

Assistive technology and legitimate human assistance may help a user perceive, navigate or enter information.

They do not transfer semantic intent.

```text
assisted navigation != authority transfer
assisted entry != assistant becomes Judge author
alternate input != alternate Scorecard semantics
```

When another human materially captures content for a represented authority, 013-F actor-versus-represented-authority and Provenance rules apply. Ambiguous intent remains ambiguous.

# Interruption and device replacement

Resume re-establishes current protected-operation context rather than trusting stale navigation state:

```text
Identity
+ Participation / capacity
+ Competition
+ target resource
+ current Access
+ current authoritative resource state
```

A prior route, QR, browser session, cached view or device possession does not prove current Access.

Shared-device handoff must not expose the prior participant's private state simply because the same hardware remains in use.

# Resume existing logical work

For evaluation work:

```text
interruption / device replacement / retry
  → same Evaluation Obligation
  → same logical Scorecard
  != new evaluation weight
```

The same convergence principle applies to paper/electronic traces and later recovery.

Retries of other high-consequence operations likewise must not intentionally duplicate Award, Finalization, declaration, Export or Publication authority.

# Degraded/local working state

Where disconnected or partially connected working continuation exists, distinguish:

```text
local/device-held working state
server/application-confirmed persisted working state
confirmed authoritative domain state
```

For example:

```text
local Scorecard Draft
  != persisted Draft confirmed
  != Scorecard Finalized
  != Evaluation Obligation Satisfied
```

Local availability of data or artifacts cannot promote them into current authoritative state.

# Paper fallback

Paper fallback preserves one evaluation model:

```text
same Team
same Evaluation Occurrence
same Evaluation Obligation
same Judge semantic author
same exact Evaluation Basis
same logical Scorecard
same evaluation weight
```

Paper transcription remains non-authoritative until source fidelity and committed Judge intent are established under current policy.

Electronic and paper traces for the same obligation reconcile to one logical evaluation rather than two votes.

# Safe capability reduction

If degraded operation cannot safely establish current Access, basis, prior operation outcome or another high-consequence precondition, the legitimate operation may be unavailable.

The experience should preserve work and explain the known limitation rather than offer a lower-authority substitute.

# Privacy and disclosure parity

Degraded operation, print, shared devices, alternate input and recovery do not weaken disclosure policy.

```text
technical recovery capability
  != broader Access
  != broader audience disclosure
  != semantic authority
```

Judge-safe identity, peer-result non-disclosure, private Notes and Export AudienceProfile rules continue to apply.

A degraded path may expose less information when safe disclosure cannot be established; it must not expose more merely to maintain operational convenience.

# Export / Publication parity

013-I semantics remain unchanged across alternate paths:

```text
Export currency != Publication state
Publication Published != delivery
withdrawal/supersession != external-copy disappearance
recipient possession != current release authority / interactive Access
```

A previously downloaded/printed artifact does not become Current merely because it remains accessible during an outage.

# Related mapping

- uncertainty, feedback and retry/recovery grammar → [Status, Feedback & Recovery Mapping](status-feedback-recovery.md);
- Judge evaluation → [Judge Active Evaluation Mapping](judge-evaluation.md);
- paper/capture authority → [Authority Lineage, Capture & Correction Mapping](authority-lineage-correction.md);
- external representation/release → [External Representation, Disclosure & Release Mapping](external-representation-release.md).
