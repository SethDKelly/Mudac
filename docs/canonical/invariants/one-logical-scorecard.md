---
type: Design Invariant
title: One Logical Evaluation per Evaluation Obligation
description: One Evaluation Obligation may be satisfied by at most one logical Scorecard unit of evaluation evidence; retries, drafts, capture paths, and amendments cannot multiply evaluation weight.
status: stable
tags: [invariant, scorecard, evidence, obligation]
sources:
  - resource: ../../002-concept-specification/002-D-rubric-criterion-scorecard-notes-specifications.md
  - resource: ../../010-project-purpose-candidate-specification-modularity/010-H-concept-boundary-convergence-respecification-canonical-reconciliation.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-12T03:12:00Z }
---

<a id="inv-002"></a>
# INV-002 — One Logical Evaluation per Evaluation Obligation

Within MUDAC:

`Evaluation Obligation → at most one logical qualifying Scorecard`.

Retries, device changes, multiple Draft traces, paper fallback, capture correction, and amendment must converge on the same logical Scorecard for that responsibility rather than creating additional evaluation weight.

Successor authoritative states of the same Scorecard preserve one logical evaluation. Paper and electronic traces of the same evaluation cannot both contribute weight.

If a historically satisfied obligation later requires legitimate re-evaluation because its evidence becomes unusable, [Evaluation Obligation](../concepts/evaluation-obligation.md) creates a **successor obligation**. A new Scorecard may satisfy that successor while the predecessor obligation/Scorecard remain historical. Eligibility rules determine which evidence may currently contribute; history is never erased to preserve the one-vote rule.

This invariant does not require Evaluation Obligation to author/finalize Scorecard or Scorecard to own responsibility. Their coordination belongs to synchronization.

See [Scorecard](../concepts/scorecard.md) and [Continuity & Paper](../policies/continuity-paper.md).