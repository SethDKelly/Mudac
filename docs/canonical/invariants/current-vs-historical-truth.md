---
type: Design Invariant
title: Current and Historical Truth Remain Distinct
description: Current corrected operational state must not overwrite the historical state actually observed by prior events or authoritative versions.
status: stable
tags: [invariant, history, provenance]
sources:
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
---

# Invariant

Current operational truth and historical observed truth may legitimately differ; both remain explicit.

Examples include current corrected Division vs Encounter-presented Division, current Alias vs Encounter-presented Alias, current Panel membership vs historical Encounter participants, current Scorecard Version vs prior authoritative Versions, and current Official Outcome Revision vs prior declared revisions.

Correction changes what is current; it does not rewrite what happened.

See [Versioning](../concepts/versioning.md) and [Provenance](../concepts/provenance.md).