---
type: Experience Contract
title: Accessibility, Responsive and Degraded Operation
description: Same domain semantics across accessible interaction, device sizes, interruptions, connectivity loss, and paper fallback.
status: stable
tags: [experience, accessibility, resilience]
sources:
  - resource: ../../003-conceptual-ux-architecture/003-H-accessibility-mobile-responsive-degraded-mode-interaction-architecture.md
---

# Canonical contract

Accessibility is semantic parity, not a separate product mode. Core workflows should reasonably target WCAG 2.2 AA and must not depend solely on mouse, hover, camera/QR, gesture, color, one orientation, or fine-pointer precision.

Judge work is fully phone-primary. Organizer dense wide-screen views must retain a coherent narrow `summary → exception → detail → legitimate action` path.

Interruption/device replacement re-establishes Identity, Participation, Competition, resource, and Access context rather than duplicating work. Shared-device handoff clears prior private state.

Disconnected Draft work may exist only if local state remains distinguishable from confirmed authority. Full digital failure uses identified paper evidence, not a second authority model.

See [Accessibility Semantic Parity](../invariants/accessibility-semantic-parity.md).