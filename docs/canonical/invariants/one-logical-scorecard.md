---
type: Design Invariant
title: One Logical Scorecard per Judge and Encounter
description: One Judge Participation in one Encounter contributes at most one logical unit of evaluation weight.
status: stable
tags: [invariant, scorecard, evidence]
sources:
  - resource: ../../002-concept-specification/002-D-rubric-criterion-scorecard-notes-specifications.md
  - resource: ../../002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md
  - resource: ../../002-concept-specification/002-H-export-print-operational-continuity-external-representations.md
---

<a id="inv-002"></a>
# INV-002 — One Logical Scorecard per Judge × Encounter

`Judge Participation × Judging Encounter → at most one logical Scorecard`.

Retries, device changes, multiple Drafts, paper fallback, capture correction, and amendment must converge on that same logical evaluation.

Successor Scorecard Versions supersede prior authority without adding another vote. Paper and electronic traces for the same evaluation cannot both contribute weight.

See [Scorecard](../concepts/scorecard.md) and [Continuity & Paper](../policies/continuity-paper.md).