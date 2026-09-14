---
type: Design Invariant
title: Official Is Not Automatically Public
description: Explicit internal outcome authority and external representation/release are separate authority and disclosure operations.
status: stable
tags: [invariant, outcome, publication, disclosure]
sources:
  - resource: ../../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
  - resource: ../../011-concept-composition-synchronization/011-H-export-publication-representation-currency-release-composition.md
  - resource: ../synchronizations/external-representation-publication-release.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T16:58:00-05:00 }
---

<a id="inv-007"></a>
# INV-007 — Official Is Not Automatically Public

`Outcome Declaration exists ≠ Representation generated ≠ Representation Published ≠ Representation delivered`.

An internal [Outcome Declaration](../concepts/outcome-declaration.md) establishes declared outcome authority. Externalization requires a separate audience/disclosure-aware [Export](../concepts/export.md), and deliberate release requires [Publication](../concepts/publication.md). Transport/delivery realization is separate again.

Competition Finalization likewise does not automatically disclose results.

A Publication failure does not weaken internal declared authority. A successor Outcome Declaration does not silently rewrite already generated or released historical representations; replacement requires explicit successor Export/Publication where appropriate.

Source correction may make an Export `Affected` or `Stale`, but it does not automatically withdraw or retarget an existing Publication. Withdrawal/supersession preserves the historical fact that the prior representation was released, even when distributed copies can no longer be recalled.