---
type: Design Invariant
title: Calculated Is Not Official
description: A computable result or ranking-ready projection does not itself become the Competition's declared official outcome.
status: stable
tags: [invariant, ranking, finalization]
sources:
  - resource: ../../002-concept-specification/002-G-awards-reconciliation-finalization-official-outcomes.md
  - resource: ../../003-conceptual-ux-architecture/003-F-reconciliation-coverage-ranking-awards-finalization-experience.md
---

# Invariant

MUDAC preserves the sequence:

`calculated result ≠ ranking-ready result ≠ official outcome`.

Calculations may update as evidence changes. Ranking readiness derives from resolved source state. Official authority arises only through explicit Competition Finalization and an [Official Outcome Revision](../mechanisms/official-outcome-revision.md).

A corrected latest calculation cannot silently replace the current official revision.