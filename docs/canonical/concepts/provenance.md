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
---

# Purpose

Preserve the meaningful origin and transformation history needed to explain authoritative application state.

# Canonical contract

Provenance records meaningful domain transitions: who acted, what changed, when, under which origin/capture path, under what authority, and where material why.

It distinguishes semantic author, capture actor, and authorizer. For example, a Judge may remain evaluation author while an Organizer is the paper capture actor.

Provenance is not an obligation to log every keystroke or read.

# Boundary with OKF

This MUDAC Concept concerns Competition-domain authority lineage. OKF `sources`, `generated`, and `verified` metadata describe documentation lineage and trust; they do not replace this Concept.

See [Versioning](versioning.md) and [Correction & Authority](../policies/correction-authority.md).