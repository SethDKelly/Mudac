---
type: Experience Contract
title: Status, Feedback & Recovery Mapping
description: Current cross-cutting mapping for multidimensional state, authoritative feedback, uncertainty, retry/recovery, privacy and safe reconciliation after interrupted or degraded operations.
status: stable
tags: [experience, mapping, status, feedback, recovery, uncertainty, privacy, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-J-accessibility-degraded-operation-status-feedback-recovery-semantic-parity-mapping.md
  - resource: ../invariants/truthful-authority-under-uncertainty.md
  - resource: ../invariants/one-logical-scorecard.md
  - resource: ../concepts/access.md
  - resource: judge-evaluation.md
  - resource: authority-lineage-correction.md
  - resource: live-operations.md
  - resource: reconciliation-derived-state.md
  - resource: outcome-officiality.md
  - resource: external-representation-release.md
---

# Purpose

Define the cross-cutting language by which MUDAC explains state, authority, uncertainty and recovery without collapsing independent semantic owners.

# Status is multidimensional

MUDAC does not have one universal domain `status`.

Relevant independent dimensions may include:

- subject lifecycle/state;
- work responsibility state;
- Draft versus authoritative state;
- persistence/confirmation confidence;
- validity/eligibility;
- version/currentness/currency;
- readiness;
- warning/blocker/exception/correction condition;
- Access/disclosure posture;
- Publication distribution state;
- downstream transport/delivery observation.

Only dimensions relevant to the current subject need be visible, but one generic badge must not silently collapse them.

# Subject-qualified finality

Ambiguous words such as `done`, `complete`, `submitted`, `saved`, `final`, `current`, `published` or `resolved` must not imply a stronger owner-specific postcondition than actually exists.

Preserve distinctions such as:

```text
Draft complete != Scorecard Finalized
Evaluation Occurrence Complete != Evaluation Obligation Satisfied
Competition Event Completed != Competition Finalized
Ranking Ready != official
Competition Finalized != Published
Outcome Declaration Affected != Superseded
Export Current != Publication Published
Publication Published != delivered
Acknowledged != source resolved
```

# Working persistence versus semantic commitment

Working-state feedback may describe local, synchronizing or confirmed persisted Draft state.

It remains distinct from semantic authority.

```text
Draft saved != Finalize Evaluation succeeded
Export request recorded != Export generated
Publication request sent != Publication Published
```

When `saved` or similar language is used, the persistence scope must be clear enough not to imply Finalization or another authority transition.

# Authoritative-result feedback

For high-consequence operations, user-visible success corresponds to confirmed authoritative state.

The experience must not infer success from optimistic local presentation, navigation away, elapsed time or request dispatch alone.

This applies to, among others:

- Scorecard Finalization/amendment/capture correction;
- evidence/occurrence invalidation;
- governed exception acceptance;
- Award conferral/correction;
- Competition Finalization plus Outcome Declaration;
- successor Outcome Declaration;
- Export generation/revalidation;
- Publication publish/withdraw/supersede.

# Unknown is neither success nor failure

Represent at least the semantic distinction:

```text
not attempted
in progress / pending
result unknown
confirmed success
confirmed rejection/failure
```

`result unknown` is a first-class condition.

When authoritative outcome cannot currently be determined, the experience must not claim the target state or fabricate failure merely to simplify recovery.

# Retry converges; it does not duplicate

After uncertainty, recovery should reconcile against current authoritative state before repeating a high-consequence intent where possible.

```text
same intended operation
  + current authority check
  → converge on one legitimate semantic result
```

Retries, device changes or reconnects must not intentionally create duplicate Scorecards, evaluation weight, Award conferrals, declarations or releases.

# Stale state cannot overwrite newer authority

A cached/local/degraded state cannot silently replace a newer authoritative state discovered during recovery.

This applies to:

- Scorecard Versions and terminal obligation state;
- correction/invalidation history;
- Award history;
- Outcome Declaration currentness;
- Export currency/successor relations;
- Publication withdrawal/supersession.

When a conflict exists, preserve the newer authority and explain the local/pending work strongly enough to support a legitimate next action.

# Recovery explanation grammar

Where relevant, recovery should explain:

1. the attempted action;
2. definitely known authoritative state;
3. what remains uncertain;
4. preserved Draft/local/paper work;
5. current authority discovered after reconnection/re-entry;
6. the legitimate next action;
7. privacy/disclosure constraints on the recovery representation.

Legitimate next actions may include resume, reconcile then retry, discard a duplicate local trace, use an owner-specific correction path, escalate, or wait for required source availability.

Recovery is not a generic `reset` workflow.

# Consequence-scaled confirmation

Higher-consequence actions should make the semantic target and effect intelligible before commitment.

This applies especially to:

- invalidation/replacement/successor responsibility;
- Award revocation/correction;
- Finalize Competition & Declare Outcome;
- Confirm Successor Outcome Declaration;
- Publication withdrawal;
- successor release.

The mapping does not prescribe a confirmation-dialog implementation.

Use owner-specific verbs where vague labels such as `force`, `reset`, `fix`, `delete` or `resolve` would obscure retained history or authority consequences.

# Status after confirmed success

Feedback should state the authority that was actually established and keep downstream meanings separate.

Examples:

```text
Scorecard Finalized
  → Evaluation Obligation Satisfied
  != Coverage automatically Satisfied

Competition Finalized + Outcome Declaration Current
  != Export generated
  != Publication

Publication Published
  != transport/delivery/viewing success
```

# Bulk and summary status

A bulk interaction or operational summary may compress many owner-specific actions for usability, but it does not become a new semantic status owner.

If subjects produce mixed outcomes, the summary must preserve the ability to distinguish, as applicable:

- confirmed success;
- confirmed rejection/failure;
- result unknown;
- not attempted/pending;
- owner-specific blockers or retained work.

A label such as "completed" for a bulk request must not imply that every underlying semantic action established its postcondition.

~~~text
bulk operation summary
  != per-owner authority
  != permission to flatten partial success / failure / unknown
~~~

# Privacy during recovery

Recovery views remain subject to current Access and disclosure rules.

A support/admin actor may help restore operation without gaining semantic authorship or unrestricted source visibility.

Device possession, cached content, URL/QR possession or prior authentication does not substitute for current Access.

If safe disclosure cannot be established, recovery may show less rather than expose protected information.

# Acknowledgement versus resolution

Operational attention-management states remain presentation-only:

```text
viewed
acknowledged
hidden
suppressed
```

They do not resolve source truth.

Resolution occurs only through source change, a specifically governed exception affecting a permitted consequence, or another owner-defined semantic action.

# Accessibility/degraded parity

The feedback grammar in this owner applies equally across accessible, responsive, degraded, paper-assisted and ordinary digital paths.

An alternate path may change wording density or interaction mechanics, but not whether an action is Draft, authoritative, uncertain, Affected, Published, Withdrawn or otherwise owner-defined.

See [Accessibility, Responsive & Degraded-Operation Mapping](accessibility-resilience.md).
