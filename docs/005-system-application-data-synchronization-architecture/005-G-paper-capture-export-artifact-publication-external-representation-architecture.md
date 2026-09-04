---
type: Architecture Design Record
title: 005-G — Paper Capture, Export, Artifact, Publication & External-Representation Architecture
description: Resolves physical-evidence intake, immutable artifact storage, exact source/disclosure binding, generation validation, publication lifecycle, supersession, and external-representation integrity.
status: stable
tags: [phase-005, architecture, paper, export, artifact, publication, representation]
sources:
  - resource: ../canonical/concepts/export.md
  - resource: ../canonical/policies/continuity-paper.md
  - resource: ../canonical/policies/anonymity-disclosure.md
  - resource: ../canonical/policies/correction-authority.md
  - resource: ../canonical/experience/paper-export-publication.md
  - resource: ../canonical/mechanisms/official-outcome-revision.md
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/architecture/data-persistence.md
  - resource: ../canonical/architecture/commands-api-concurrency.md
  - resource: ../canonical/architecture/synchronization-recovery.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T05:07:00Z }
---

# 005-G — Paper Capture, Export, Artifact, Publication & External-Representation Architecture

Status: **Complete**

## Purpose

Translate MUDAC's paper-continuity, Export, disclosure, correction, official-outcome, and publication contracts into a system architecture that preserves exact source identity and provenance across physical intake and external representation.

005-G must prevent three classes of drift:

1. **capture drift** — Organizer transcription or scanning silently becoming Judge authorship/intent;
2. **representation drift** — a generated PDF/print/QR becoming detached from the exact source revision and disclosure basis it represents;
3. **publication drift** — generation, storage, distribution, replacement, or withdrawal being collapsed into one implicit state.

The governing pipeline is therefore intentionally split:

```text
PHYSICAL INTAKE
physical paper source
    ↓ stable source reference / custody
capture Draft
    ↓ verification against source
paper-origin Scorecard Version

EXTERNALIZATION
authoritative source Version/revision
    + purpose
    + audience/disclosure profile
    ↓
Export intent / representation record
    ↓ generation
immutable Artifact bytes + digest
    ↓ validation/preview
publication decision
    ↓
Publication record / distribution
```

The [Evaluation module](../canonical/architecture/application-boundaries.md) remains owner of paper-origin Scorecard authority. The External Representation module owns Export, artifact-generation, and publication state. Blob/object infrastructure stores bytes but owns neither meaning nor publication authority.

## Upstream constraints

005-G particularly realizes:

- [EXPORT-001](../canonical/concepts/export.md#export-001) — Export represents source truth; it does not replace it;
- [EXPORT-002](../canonical/concepts/export.md#export-002) — generation and publication are distinct;
- [DISC-002](../canonical/policies/anonymity-disclosure.md#disc-002) — disclosure is audience/purpose specific and applies beyond page bodies;
- [INV-004](../canonical/invariants/organizer-not-judge-author.md#inv-004) — Organizer capture does not become Judge authorship;
- [INV-007](../canonical/invariants/official-not-automatically-public.md#inv-007) — official does not imply public;
- [INV-008](../canonical/invariants/capture-channel-parity.md#inv-008) — paper/electronic channels preserve one evaluation meaning/weight;
- [INV-010](../canonical/invariants/truthful-authority-under-uncertainty.md#inv-010) — ambiguous/failed generation or capture cannot fabricate success;
- [OUT-001](../canonical/mechanisms/official-outcome-revision.md#out-001) / [OUT-002](../canonical/mechanisms/official-outcome-revision.md#out-002) — official outcome revisions are immutable/successor-based;
- [DATA-006](../canonical/architecture/data-persistence.md#data-006) / [DATA-007](../canonical/architecture/data-persistence.md#data-007) — committed history/provenance remain append-stable;
- [API-004](../canonical/architecture/commands-api-concurrency.md#api-004) — consequential state becomes confirmed only after authoritative commit;
- [SYNC-012](../canonical/architecture/synchronization-recovery.md#sync-012) — paper/electronic traces converge on one logical evaluation.

## Decision 1 — Physical paper intake belongs to Evaluation authority

Paper-origin judging does not create a second evaluation subsystem.

A physical sheet receives a stable `PaperSource`/source-reference identity sufficient to locate the retained physical evidence and, where captured, any image/blob representation. The source reference identifies physical evidence; it is not a Scorecard ID and does not itself authorize transcription.

Organizer transcription creates a non-authoritative capture Draft linked to:

- Judge Participation;
- Competition and Encounter;
- logical Scorecard identity;
- exact Rubric Version;
- physical source reference;
- capture actor and capture timestamp;
- transcription content;
- optional image/blob reference where a source image was captured.

Verification compares the transcription to the identified physical source. A successful verification transition creates/advances the same logical Scorecard lineage through the Evaluation module and records paper origin plus capture/verification provenance.

Verification confirms **transcription fidelity**, not invented interpretation. Illegible, contradictory, or ambiguous Judge intent remains unresolved until Judge clarification or another governed correction path is available.

### Capture correction

A demonstrable transcription mismatch is repaired as a capture correction:

```text
physical source
    ↓
prior captured representation (preserved)
    ↓ correction reason / actor / source evidence
corrected capture
    ↓
successor authoritative state where applicable
```

The original physical evidence and prior capture/provenance are not overwritten or erased.

## Decision 2 — Binary evidence/artifacts use object/blob storage; relational metadata remains authoritative

MUDAC should not store large PDFs/scans/print packages as ordinary relational authority rows.

The architecture therefore uses:

```text
PostgreSQL authority database
    Export identity/source/disclosure metadata
    PaperSource/capture metadata
    Artifact metadata + digest + storage locator
    Generation job/result state
    Publication/distribution state
    Provenance / supersession

object/blob storage behind module-owned port
    scan/image bytes when captured
    generated PDF/print/package bytes
    other immutable external-representation payloads
```

The concrete object-storage product is deferred to 005-I. An object key, bucket path, CDN URL, or signed URL is a locator, not semantic identity.

Artifact metadata records at least stable artifact ID, Export/source basis, media/format, generation implementation/template version where material, byte length, cryptographic digest algorithm/value, storage locator, creation time, and generation result identity.

Published/retained artifact bytes are immutable. Re-generation creates another Artifact record/object rather than overwriting the old bytes in place.

## Decision 3 — Export identity includes exact source and disclosure basis

An Export is modeled as an audience/purpose-specific representation request/resource, not as "whatever the current PDF contains."

The source basis is explicit and immutable for a generated Artifact. Depending on subject it may include:

- exact Scorecard Version;
- exact Rubric Version;
- Competition configuration revision;
- exact Official Outcome Revision;
- identified derived-calculation basis where a non-official operational export is permitted;
- source watermark/version set for bounded operational representations.

The Export also records:

- representation purpose/type;
- requested audience/disclosure profile;
- requesting/authorizing context where applicable;
- locale/timezone/layout options that materially affect meaning;
- requested generation format.

A `Public` artifact and `Organizer-sensitive` artifact from the same source are distinct representations. Disclosure is not an after-the-fact cosmetic toggle.

## Decision 4 — Disclosure is enforced across the complete artifact surface

Artifact generation applies the selected disclosure profile to:

- visible content;
- hidden document metadata/properties;
- filenames and suggested download names;
- embedded links;
- QR/barcode payloads;
- machine-readable layers/attachments;
- accessibility text/labels;
- generated indexes/manifests;
- preview/cache/CDN representations.

This prevents institution identity, Judge Notes, peer evidence, internal IDs, or Organizer-only information from leaking through non-body channels.

The artifact generator receives an already-authorized representation contract or a disclosure-safe data projection; it does not independently infer what a role should be allowed to see.

## Decision 5 — Artifact generation is an idempotent, potentially asynchronous operation

Generating complex print/PDF packages may be asynchronous. The external command can create/reuse one logical generation request using idempotency semantics.

A generation job records:

```text
Export/source/disclosure basis
requested format
idempotency/request identity
generation implementation/template version
queued/running/succeeded/failed state
resulting Artifact ID(s)
error category safe for operator/user exposure
```

Generation may retry after infrastructure failure. A retry may produce a new byte Artifact if the earlier attempt was not confirmed/retained, but one published Artifact is always identified explicitly rather than inferred from "latest file in storage."

A generation job succeeding means artifact bytes were generated and durably registered. It does **not** mean the artifact was semantically approved, published, printed, or distributed.

## Decision 6 — Artifact validation/preview is separate from generation and publication

Before an artifact is used for a consequence-sensitive purpose, the relevant workflow may validate:

- source/disclosure basis still matches the intended representation;
- byte integrity/digest;
- expected media type/page/rendering characteristics;
- required sections/content presence;
- print layout/margins/page orientation where relevant;
- QR/barcode readability where relevant;
- accessibility/tagging/text alternatives where required by the output contract;
- absence of prohibited disclosure fields/metadata where mechanically testable.

Automated validation does not infer subjective correctness that only a human can establish. Previewing or validating an artifact also does not publish it.

## Decision 7 — Publication is an explicit authoritative distribution transition

Publication/distribution is modeled as a separate command/state owned by External Representation.

A `Publication`/distribution record identifies:

- exact Artifact ID;
- exact Export/source basis inherited from that Artifact;
- audience/disclosure profile;
- channel/destination;
- publication actor/authorizer;
- publication timestamp;
- current state such as current, withdrawn, or superseded;
- successor/predecessor relationship where replaced.

Publication success is confirmed only after the authoritative Publication state transaction commits. External delivery/cache propagation may continue after that and must not be confused with the commit itself.

Official Outcome Finalization does not automatically create a public Publication, and generation of a public-shaped artifact does not publish it.

## Decision 8 — Source changes affect artifacts; they do not rewrite them

Artifacts and publications are immutable historical representations of their identified source basis.

If a source changes—such as a successor Scorecard Version, corrected configuration revision, or successor Official Outcome Revision—the system determines which dependent Export/Artifact/Publication records are affected.

Possible representation states include `Current`, `Affected`, `Stale`, `Superseded`, or withdrawn-from-distribution as appropriate to the subject/use case. These states do not edit the historical bytes or claim that the old artifact never existed.

Replacement follows:

```text
source revision N
    ↓ Artifact A / Publication A
source correction
    ↓ source revision N+1
new Export/generation
    ↓ Artifact B
explicit publish/republication
    ↓ Publication B
Publication A → superseded/withdrawn as applicable
```

A source correction does not silently repoint Publication A to Artifact B.

## Decision 9 — Public/private delivery mechanisms are transport, not authority

External URLs, signed URLs, object locations, QR codes, download tokens, printer jobs, CDN objects, and email/message attachments are delivery mechanisms.

They do not establish:

- Access;
- Judge authorship;
- official outcome authority;
- current publication state;
- source Version identity beyond what the authoritative metadata records.

Private/unpublished artifact retrieval re-evaluates current Access. Time-bounded signed delivery URLs may be used by infrastructure but must not outlive/recreate application authorization semantics. Truly public artifacts are made public only through an explicit Publication whose audience is public.

## Decision 10 — External representation retains audit-grade provenance

For a distributed artifact MUDAC must be able to answer:

- what exact authoritative source/revision was represented;
- which purpose and audience/disclosure profile was applied;
- what generator/template/format produced the bytes;
- what immutable Artifact/digest was distributed;
- whether/when/who published or withdrew it;
- whether a later source change affected or superseded it;
- which successor artifact/publication replaced it, if any.

This provenance remains data-plane history and is distinct from OKF documentation `generated`/`verified` metadata.

## Alternatives considered

### Store all binary files directly in PostgreSQL

Rejected as the baseline. The relational store should own semantic metadata and transactions; large binary payloads are better isolated in blob/object storage. This also permits later CDN/retention/lifecycle choices without moving semantic authority.

### Regenerate files on every request and keep no Artifact identity

Rejected for consequence-sensitive outputs. Without immutable Artifact identity/digest, MUDAC cannot reconstruct exactly what was printed/published/distributed after templates, renderers, or sources change.

On-demand ephemeral previews may exist, but a representation that is printed, published, or relied upon externally receives a durable Artifact record.

### One mutable "current.pdf" object

Rejected. Overwriting a stable path destroys historical attribution and creates cache/publication ambiguity. Stable publication aliases may point to a current Publication, but historical Artifact objects remain immutable and individually addressable by internal identity.

### Treat Finalization as automatic publication

Rejected by `INV-007` and `EXPORT-002`. Official authority and public disclosure remain deliberately separate.

### Treat paper transcription as an Organizer-authored Scorecard

Rejected by `INV-004`/`INV-008`. Organizer is capture actor; Judge remains semantic evaluator.

## Failure and recovery scenarios

### Paper transcription fails verification

Capture Draft remains non-authoritative; physical source remains available for correction/review. No Scorecard Version is invented.

### Artifact generator crashes after object upload but before database registration

Unregistered/orphan bytes are not discoverable as authoritative artifacts and may be garbage-collected after reconciliation. Retry uses the generation request/idempotency record to converge on a registered Artifact.

### Database records Artifact but delivery/CDN publish fails

Artifact remains generated/retained but Publication/delivery state does not falsely report complete distribution. Retry delivery without regenerating source authority.

### Official Outcome Revision changes after public PDF release

Existing Publication remains historical; it becomes affected/superseded/withdrawn according to policy. A new artifact is generated from the successor Official Outcome Revision and requires explicit publication.

### Public artifact accidentally requests sensitive profile

Authorization/disclosure validation rejects publication. The existence of generated sensitive bytes does not grant public distribution authority; private artifact storage/retrieval remains Access-controlled.

### QR points to superseded public artifact

The encoded representation must either identify that historical artifact honestly or resolve through an application-controlled publication alias that can communicate supersession. It must not make an old artifact appear current without disclosure.

## Architecture consequences for later groups

### 005-H — Front-end

The UI must represent capture Draft vs verified paper-origin Version, generated vs validated vs published, current vs affected/superseded artifacts, and private/public disclosure state without collapsing these dimensions.

### 005-I — Runtime/AWS

Runtime design must select concrete object storage, encryption, access policy, CDN/public-delivery approach, malware/content scanning where relevant, lifecycle/retention, artifact generator execution, signed-delivery strategy, backups, and observability while preserving the architecture here.

### Implementation/testing

Tests will need fixtures for exact source binding, disclosure leakage, immutable artifact identity/digest, idempotent generation, publish-without-generation prevention, source-change supersession, paper capture attribution, and storage/database partial-failure reconciliation.

## Exit assessment

005-G requires no Product/Concept redesign. It realizes existing paper, Export, disclosure, correction, and publication semantics with explicit storage and state boundaries.

Current authority is extracted to [External Representation, Artifact & Publication Architecture](../canonical/architecture/external-representation.md) with `REP-*` stable architecture rules.

**Next:** 005-H — Front-End State, Navigation, Component-System & Responsive Interaction Architecture.