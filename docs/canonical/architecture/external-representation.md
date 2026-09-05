---
type: Architecture Contract
title: External Representation, Artifact & Publication Architecture
description: Defines paper-evidence intake boundaries, exact source/disclosure binding, immutable artifact storage, generation validation, publication lifecycle, and supersession for external MUDAC representations.
status: stable
tags: [architecture, paper, export, artifact, publication, representation, disclosure]
sources:
  - resource: ../../005-system-application-data-synchronization-architecture/005-G-paper-capture-export-artifact-publication-external-representation-architecture.md
  - resource: ../../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
  - resource: application-boundaries.md
  - resource: data-persistence.md
  - resource: commands-api-concurrency.md
  - resource: synchronization-recovery.md
  - resource: ../concepts/export.md
  - resource: ../concepts/publication.md
  - resource: ../policies/continuity-paper.md
  - resource: ../policies/anonymity-disclosure.md
  - resource: ../policies/correction-authority.md
  - resource: ../experience/paper-export-publication.md
  - resource: ../mechanisms/official-outcome-revision.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-05T02:12:00Z }
---

# Purpose

Define how MUDAC ingests physical evidence and realizes [Export](../concepts/export.md) and [Publication](../concepts/publication.md) without allowing transcription, binary storage, generated artifacts, URLs, or publication infrastructure to replace the authoritative source state they represent.

<a id="rep-001"></a>
## REP-001 — Paper-origin Scorecard authority remains owned by Evaluation

Paper judging is an alternate capture channel for the same logical Scorecard, not a second evaluation system. A physical source is linked to a non-authoritative capture Draft; only the Evaluation module's governed verification transition can establish a paper-origin authoritative Scorecard Version.

Organizer remains capture actor and Judge remains semantic author under [INV-004](../invariants/organizer-not-judge-author.md#inv-004) and [INV-008](../invariants/capture-channel-parity.md#inv-008).

<a id="rep-002"></a>
## REP-002 — Physical evidence has a stable source reference and preserved capture provenance

Each paper source used for authoritative capture has a stable source-reference identity sufficient to locate/reconcile the retained physical evidence and any captured image/blob. Capture records preserve source reference, Judge Participation, Encounter, exact Rubric Version, logical Scorecard identity, capture actor/time, and relevant verification provenance.

A source reference is evidence identity, not Access or Scorecard authority.

<a id="rep-003"></a>
## REP-003 — Paper verification establishes transcription fidelity, not invented Judge intent

Verification confirms that the digital capture faithfully represents the identified physical source. Illegible, ambiguous, contradictory, or otherwise indeterminate Judge intent is preserved as unresolved and cannot be inferred by Organizer merely to complete capture.

A demonstrated transcription mismatch uses provenance-preserving capture correction rather than destructive overwrite.

<a id="rep-004"></a>
## REP-004 — Binary evidence and generated artifacts use immutable object/blob storage behind authoritative metadata

Large scans, PDFs, print packages, and similar binary payloads are stored through an object/blob-storage port rather than treated as ordinary relational authority fields. PostgreSQL-owned metadata remains authoritative for semantic identity, source/disclosure basis, lifecycle, provenance, digest, and storage locator.

Bucket/object names, paths, URLs, and CDN keys are locators, not semantic identity.

<a id="rep-005"></a>
## REP-005 — Every durable Export/Artifact binds an exact source basis, purpose, and disclosure profile

A durable external representation records the exact source Version/revision/basis it represents, the representation purpose, and the audience/disclosure profile applied. It never means merely "the latest current state."

Different audience/disclosure profiles over the same source are distinct representations under [EXPORT-001](../concepts/export.md#export-001) and [DISC-002](../policies/anonymity-disclosure.md#disc-002).

<a id="rep-006"></a>
## REP-006 — Disclosure applies to the complete artifact surface

The selected disclosure profile governs visible content plus filenames, document metadata, embedded links, QR/barcode payloads, machine-readable layers/attachments, accessibility text, manifests/indexes, preview caches, and public-delivery representations.

Artifact generation cannot rely on UI hiding as a disclosure boundary.

<a id="rep-007"></a>
## REP-007 — Durable Artifact bytes are immutable and integrity-addressable

An Artifact receives a stable application ID and records immutable byte identity through a cryptographic digest plus media/format, size, generation time, storage locator, and material generator/template version information.

Regeneration creates a new Artifact record/object rather than overwriting published/retained historical bytes in place.

<a id="rep-008"></a>
## REP-008 — Generation, validation, Publication, and delivery are distinct states

Generating durable bytes means only that an Artifact was produced and registered. Preview/validation, [Publication](../concepts/publication.md), print dispatch, CDN propagation, download, or other delivery are separate operations/states and must not be inferred from generation success.

This realizes [EXPORT-002](../concepts/export.md#export-002) and [INV-007](../invariants/official-not-automatically-public.md#inv-007).

<a id="rep-009"></a>
## REP-009 — Artifact generation is idempotent/retryable and may be asynchronous

A consequence-sensitive generation request has stable request/idempotency identity and records source/disclosure/format/generator basis plus queued/running/succeeded/failed result state. Infrastructure retry converges on an identified registered Artifact rather than treating an arbitrary object-storage upload as success.

Generation failure cannot create Publication authority.

<a id="rep-010"></a>
## REP-010 — Artifact validation is purpose-specific and does not create source authority

Where required, generated artifacts are checked for integrity, expected format/rendering, required content, print/layout constraints, QR/barcode usability, accessibility properties, and mechanically detectable disclosure leakage before external use.

Validation/preview does not change the underlying source Version or automatically publish the Artifact.

<a id="rep-011"></a>
## REP-011 — Publication is an explicit authoritative distribution record bound to one Artifact

The [Publication](../concepts/publication.md) Concept owns the deliberate domain act of release/distribution. This architecture realizes it as an authoritative record that identifies the exact Artifact/Export representation, inherited source/disclosure basis, audience, channel/destination, actor/authorizer, publication time, and current distribution state.

A generated or official artifact is not public until an applicable Publication transition succeeds after authoritative commit.

<a id="rep-012"></a>
## REP-012 — Source changes affect dependent representations without rewriting historical artifacts

When an identified source basis changes or receives a successor Version/revision, dependent Export/Artifact/Publication records may become affected, stale, superseded, or withdrawn as appropriate. Existing Artifact bytes and historical Publication records remain immutable evidence of what was represented/distributed at that time.

A source correction never silently rewrites an old artifact.

<a id="rep-013"></a>
## REP-013 — Replacement Publication is explicit and successor-based

A corrected/revised representation is generated as a new Export/Artifact and requires an explicit successor [Publication](../concepts/publication.md). Prior Publications retain predecessor/successor history and are marked superseded/withdrawn/current as applicable rather than being repointed invisibly.

This mirrors successor-based authority in [OUT-002](../mechanisms/official-outcome-revision.md#out-002) without making Publication itself an Official Outcome Revision.

<a id="rep-014"></a>
## REP-014 — URLs, QR codes, signed links, print jobs, and delivery channels do not confer authority

External references and delivery mechanisms can locate or transport an artifact but do not establish Access, Judge authorship, source Version authority, official outcome authority, or current Publication status.

Private/unpublished retrieval re-evaluates current Access; truly public availability follows an explicit public Publication.

<a id="rep-015"></a>
## REP-015 — External-representation provenance remains reconstructible end-to-end

For a retained/distributed artifact MUDAC can reconstruct the exact source revision/basis, purpose/disclosure profile, generator/template/format basis, immutable Artifact/digest, publication/withdrawal actor and time, affected/superseded state, and successor representation where applicable.

This data-plane provenance is distinct from OKF documentation metadata.

# Logical topology

```text
paper source
    ↓ PaperSource / capture provenance
Evaluation capture Draft
    ↓ verification
paper-origin Scorecard Version

source Version/revision/basis
    ↓
Export representation record
    ↓
generation request/job
    ↓
Artifact metadata ──→ immutable object/blob bytes
    ↓ validation/preview
Publication
    ↓
channel / public or controlled distribution
```

# Storage/runtime posture

Relational authority stores semantic metadata and lifecycle/provenance. Object/blob storage stores large immutable binary payloads behind application-owned ports. Concrete AWS realization is owned by [AWS-007](aws-runtime-operations.md#aws-007) for private versioned/encrypted S3 Artifact/evidence storage, [AWS-008](aws-runtime-operations.md#aws-008) for retryable asynchronous work, and [AWS-002](aws-runtime-operations.md#aws-002) for the CloudFront/private-origin delivery boundary.

Exact renderer/template stack, signed-delivery implementation, malware/content-scanning mechanism, retention automation, and print integration remain implementation details constrained by `REP-*`, the Publication Concept, and the applicable `AWS-*` contracts.

# Failure posture

- unverified paper transcription remains non-authoritative;
- orphan object bytes never become Artifact authority merely by existing;
- a registered Artifact whose delivery fails remains generated but not falsely distributed;
- source correction creates affected/successor representation state rather than byte overwrite;
- sensitive generated bytes cannot be publicly distributed without a matching authorized Publication;
- stale/superseded external references communicate historical/current status rather than silently masquerading as current.
