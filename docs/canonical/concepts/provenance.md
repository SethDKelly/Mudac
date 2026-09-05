---
type: Design Concept
title: Provenance
description: Meaningful application-state origin, transformation, and authority history.
status: stable
tags: [concept, provenance, audit]
sources:
  - resource: ../../001-concept-design/001-H-phase-consolidation-initial-concept-catalog.md
  - resource: ../../002-concept-specification/002-E-versioning-provenance-correction-authority-preservation.md
  - resource: ../../002-concept-specification/002-I-phase-consolidation-specification-exit-review.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
  - resource: ../../007-design-refinement/007-D-temporal-state-correction-invalidation-supersession-historical-truth-closure.md
---

# Purpose

Preserve the meaningful origin and transformation history needed to explain authoritative application state.

# State

Provenance owns append-stable meaningful domain events identifying the target subject/Version, event classification, acting Identity/Participation, represented semantic author or authority when different, Competition scope, prior/resulting authoritative state where applicable, capture/source channel/reference, exceptional authorizer, reason, and correction/replacement/invalidation relationships as needed.

When materially different, Provenance also preserves enough temporal context to distinguish the **occurrence/effective time** of the underlying domain event or source from the later time MUDAC captured, verified, corrected, or established authority for that information.

# Actions

Conceptual actions are `record`, `historyFor`, `originOf`, `traceVersion`, `traceCorrection`, and `traceReplacement`.

An incorrect provenance statement is corrected by attributable successor evidence rather than silent historical rewrite.

# Operational Principle

When a meaningful domain action establishes, changes, invalidates, or replaces authoritative state, the application records enough provenance to reconstruct who acted, whose authority the resulting content represents, why the action occurred when material, what prior state or source it depended on, and when the underlying occurrence versus later capture/authority establishment happened when those differ materially.

# Canonical contract

Provenance distinguishes semantic author, acting/capture actor, and exceptional authorizer. For example, a Judge may remain evaluation author while an Organizer is the paper capture actor.

Provenance is not an obligation to log every keystroke, read, or UI interaction.

A later correction to a historical assertion can improve MUDAC's current best-known account of what happened while preserving what MUDAC previously recorded or considered authoritative. See [Temporal Truth, Correction & Historical Authority](../synchronizations/temporal-truth-correction.md).

# Boundary with OKF

This MUDAC Concept concerns Competition-domain authority lineage. OKF `sources`, `generated`, and `verified` metadata describe documentation lineage and trust; they do not replace this Concept.

# Boundaries

Provenance explains meaningful origin/authority history; it does not preserve the content snapshots themselves ([Versioning](versioning.md)) and is distinct from low-level security/observability telemetry.

See [Correction & Authority](../policies/correction-authority.md).
