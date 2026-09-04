---
type: Design Invariant
title: Truthful Authority Under Uncertainty
description: Connectivity or persistence uncertainty must never be promoted into confirmed authoritative state.
status: stable
tags: [invariant, resilience, authority]
sources:
  - resource: ../../003-conceptual-ux-architecture/003-H-accessibility-mobile-responsive-degraded-mode-interaction-architecture.md
  - resource: ../../003-conceptual-ux-architecture/003-I-cross-cutting-status-feedback-privacy-disclosure-recovery-patterns.md
---

# Invariant

Where disconnected Draft continuation is later supported, local working state remains distinguishable from server-confirmed persistence.

The system must not claim Finalized, Completed, Invalidated, Coverage exception accepted, Competition Finalized, Published, or similar authoritative success when the authoritative outcome is unknown.

Retries must converge safely; stale state must not silently overwrite newer authority.

See [Status, Feedback & Recovery](../experience/status-feedback-recovery.md).