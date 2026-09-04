---
type: Documentation Authority
title: Source Lineage and Historical Design Records
description: Governs how current canonical knowledge cites historical design sources and how historical records route forward to current owners.
status: stable
tags: [governance, provenance, lineage, history]
sources:
  - resource: ../../004-knowledge-architecture/004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md
  - resource: ../../004-knowledge-architecture/004-B-knowledge-bundle-topology-canonical-authority-layers-progressive-disclosure.md
  - resource: ../../004-knowledge-architecture/004-C-canonical-concept-policy-invariant-experience-knowledge-extraction.md
  - resource: ../../004-knowledge-architecture/004-D-historical-phase-migration-provenance-source-lineage-retrofit.md
---

# Canonical rule

Historical phase records preserve design rationale and chronology; canonical knowledge states current accepted meaning.

Canonical documents identify material historical inputs through OKF `sources[].resource`. Numbered phase `index.md` files provide the reverse navigation by pointing historical work toward its current canonical successors.

# Source selection

A source belongs in canonical provenance when it materially introduced, specified, refined, pressure-tested, or phase-confirmed the current contract. Mere textual repetition does not make a record a material source.

Specific specification records and phase-exit consolidations may both be cited when they play different lineage roles.

Compatible post-exit refinements remain explicit sources when they contribute current truth.

# Historical preservation

Numbered phase records remain at their established paths. They should not be rewritten to erase prior decisions simply because later work supersedes them.

A later correction or refinement should create explicit successor knowledge and update the current canonical owner while retaining the earlier record as evidence of design evolution.

# Retrieval

For current meaning, retrieve canonical knowledge first. Follow historical sources only when rationale, chronology, rejected alternatives, or audit evidence is required.

When starting from history, enter through the phase `index.md` and follow its current-successor links.

# Layer distinction

This documentation/source lineage is distinct from the MUDAC [Provenance](../concepts/provenance.md) Concept. OKF lineage explains the origin of knowledge documents; MUDAC Provenance explains the authority history of Competition-domain state.