---
type: Design Invariant
title: Current and Historical Truth Remain Distinct
description: Current corrected operational state must not overwrite the historical state actually observed by prior events or authoritative versions.
status: stable
tags: [invariant, history, provenance]
sources:
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
---

<a id="inv-005"></a>
# INV-005 — Current and Historical Truth Remain Distinct

Current operational truth and historical observed truth may legitimately differ; both remain explicit.

Examples include current corrected Division vs Encounter-presented Division, current Alias vs Encounter-presented Alias, current Panel membership vs historical Encounter participants, current Scorecard Version vs prior authoritative Versions, current Official Outcome Revision vs prior declared revisions, and current Publication vs what was previously released.

Correction changes what is current; it does not silently rewrite what was observed, authored, declared, or released.

A later verified correction may also show that MUDAC's **historical record itself was inaccurate**. In that case the prior recorded/as-known claim remains attributable while a corrected historical assertion becomes the current best-known account of what actually happened. The correction lineage must remain explainable through [Provenance](../concepts/provenance.md).

Therefore these questions are distinct:

- what is current now;
- what MUDAC considered authoritative at a prior time; and
- what MUDAC now believes actually happened at that prior occurrence after later evidence/correction.

See [Versioning](../concepts/versioning.md), [Provenance](../concepts/provenance.md), and [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md).
