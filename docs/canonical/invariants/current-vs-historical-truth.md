---
type: Design Invariant
title: Current and Historical Truth Remain Distinct
description: Current corrected operational state must not overwrite historical state actually observed, authored, declared, or released.
status: stable
tags: [invariant, history, provenance]
sources:
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

<a id="inv-005"></a>
# INV-005 — Current and Historical Truth Remain Distinct

Current operational truth and historical observed/authoritative truth may legitimately differ; both remain explicit.

Examples include:

- current corrected Division versus the Division/presentation context recorded by a past [Evaluation Occurrence](../concepts/evaluation-occurrence.md);
- current Alias versus the Alias presented in that occurrence;
- current Panel membership versus historical Evaluation Occurrence participants;
- current Evaluation Obligation responsibility versus predecessor/successor obligation history;
- current Scorecard authoritative state versus prior authoritative states;
- current eligible Version versus superseded/invalidated Versions;
- current [Outcome Declaration](../concepts/outcome-declaration.md) versus prior declared outcome authority;
- current Export currency versus the source basis it historically represented;
- current Publication versus what was previously released.

Correction changes what is current; it does not silently rewrite what was observed, authored, declared, or released.

A later verified correction may also show that MUDAC's **historical record itself was inaccurate**. In that case the prior recorded/as-known claim remains attributable while a corrected historical assertion becomes the current best-known account of what actually happened. The correction lineage remains explainable through [Provenance](../concepts/provenance.md).

Therefore these questions remain distinct:

- what is current now;
- what MUDAC considered authoritative at a prior time; and
- what MUDAC now believes actually happened at that prior occurrence after later evidence/correction.

See [Versioning](../concepts/versioning.md), [Provenance](../concepts/provenance.md), and [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md).