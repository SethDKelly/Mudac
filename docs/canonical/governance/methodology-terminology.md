---
type: Documentation Authority
title: Methodology, OKF Adoption & Terminology
description: Defines the authority relationship between Daniel Jackson Concept Design, OKF, MUDAC terminology, and future implementation structure.
status: stable
tags: [governance, methodology, okf, terminology]
sources:
  - resource: ../../004-knowledge-architecture/004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md
  - resource: ../../004-knowledge-architecture/004-F-documentation-governance-agent-context-anti-drift-rules.md
---

# Canonical contract

Daniel Jackson Concept Design determines MUDAC product meaning. OKF v0.2 is the adopted knowledge representation, metadata, linking, provenance, and progressive-disclosure convention.

```text
Concept Design
    discovers / specifies product meaning

OKF
    structures and exposes the resulting knowledge
```

OKF does not redefine MUDAC application Concepts, authority, lifecycle, policies, or architecture.

# OKF version authority

MUDAC currently adopts OKF **v0.2**. A newer upstream OKF release is not automatically adopted; it requires explicit compatibility review and repository adoption.

The dedicated `GoogleCloudPlatform/open-knowledge-format` repository is the upstream authority identified by Phase 004. Historical frozen copies are not the MUDAC implementation baseline.

# Concept terminology

`MUDAC Concept` means a Daniel Jackson application Concept accepted through Concept Design.

An `OKF knowledge document` is a unit of repository knowledge. Creating a document for Coverage, Rank, a policy, an invariant, or an experience contract does not promote that subject into the MUDAC Concept catalog.

# Provenance terminology

`OKF/source lineage` explains why a knowledge document says what it says and which design sources materially produced/refined it.

The MUDAC `Provenance` Concept explains how Competition-domain state arose or changed and through whose authority.

These are separate layers.

# Verification terminology

OKF/document verification metadata describes verification of a knowledge artifact. It must not be confused with Competition-domain verification such as paper Scorecard transcription verification.

Detailed trust/verification metadata conventions are defined in 004-G.

# Structure boundary

Knowledge topology is a retrieval/authority structure, not a mandate for source-code package, service, database, API, or AWS topology.

Future architecture may organize implementation differently as long as it satisfies the canonical product/UX contracts and preserves traceable relationships back to them.