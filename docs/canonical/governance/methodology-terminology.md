---
type: Documentation Authority
title: Methodology, OKF Adoption & Terminology
description: Defines the authority relationship among Daniel Jackson Concept Design, the Base lifecycle operationalization, OKF, MUDAC terminology, and downstream architecture/implementation structure.
status: stable
tags: [governance, methodology, jackson, base, okf, terminology]
sources:
  - resource: ../../004-knowledge-architecture/004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md
  - resource: ../../004-knowledge-architecture/004-F-documentation-governance-agent-context-anti-drift-rules.md
  - resource: ../../009-jackson-methodology-realignment/009-A-methodology-authority-reset-prior-exit-reopen-design-only-guardrails.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/methodology/concept-design-lifecycle.md
---

# Canonical contract

Daniel Jackson Concept Design determines MUDAC product meaning. OKF v0.2 structures and exposes MUDAC knowledge. The `SethDKelly/Base` lifecycle is the currently adopted completion-control operationalization used to ensure Jackson's substantive design concerns are exercised in a dependency-safe order.

```text
Daniel Jackson Concept Design
    = methodology / product-design authority

Base lifecycle
    = project-process operationalization and completion control

OKF v0.2
    = knowledge representation, linking and progressive disclosure

MUDAC numbered phases
    = project-specific execution and evidence history
```

Base phase numbering is **not** represented as Daniel Jackson's official prescribed lifecycle. Where phase numbering differs, substantive methodology coverage controls.

# Current methodology posture

The previous MUDAC 007-I methodology exit has been reopened. Phase 009 established the current gap map and Phase 010–017 completion runway.

Until successful Phase 017 closure:

- Jackson Concept Design is not complete;
- implementation readiness remains not ready;
- architecture and implementation material are downstream candidates, not Concept Design constraints;
- current work follows the design-only boundary.

# OKF version authority

MUDAC currently adopts OKF **v0.2**. A newer upstream OKF release is not automatically adopted; it requires explicit compatibility review and repository adoption.

OKF does not redefine MUDAC Concepts, authority, lifecycle, policies, synchronizations or scope.

# Concept terminology

`MUDAC Concept` means a Daniel Jackson application Concept accepted through the current Concept Design process.

An `OKF knowledge document` is a unit of repository knowledge. Creating a document for Coverage, Rank, a policy, an invariant, a mapping, an architecture decision or an implementation choice does not promote that subject into the MUDAC Concept catalog.

# Design versus downstream terminology

`Concept Design` refers to representation-independent product meaning: purposes, concepts, state/actions/operational principles, composition, dependence/scope, mapping obligations, familiarity/reuse, integrity and contextual fit.

`Architecture` and `implementation` are downstream realization layers. During the reopened methodology they may provide historical evidence or contamination probes, but they do not define conceptual meaning.

# Provenance terminology

`OKF/source lineage` explains why a knowledge document says what it says and which sources materially produced or refined it.

The MUDAC `Provenance` Concept explains how Competition-domain state arose or changed and through whose authority.

These are separate layers.

# Verification terminology

OKF/document verification metadata describes verification of a knowledge artifact. It must not be confused with Competition-domain verification such as paper Scorecard transcription verification or later implementation/testing evidence.

# Structure boundary

Knowledge topology is a retrieval/authority structure, not a mandate for source-code package, service, database, API, AWS topology or implementation sequence.

Future downstream engineering may organize implementation differently as long as it satisfies the successfully closed conceptual design and preserves traceability.
