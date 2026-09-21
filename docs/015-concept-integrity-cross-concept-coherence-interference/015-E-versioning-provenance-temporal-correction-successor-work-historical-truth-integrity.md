---
type: Phase Design Record
title: 015-E — Versioning, Provenance, Temporal Correction, Successor Work & Historical-Truth Integrity
description: "Audits Cluster C purpose preservation across Versioning, Provenance, amendment, source-faithful correction, structural invalidation, occurrence replacement, obligation succession, exact-basis history, evidence eligibility, corrected historical assertions and Access-retained-history boundaries, and dispositions DIR-014 through DIR-025."
status: stable
tags: [phase-015, integrity, versioning, provenance, correction, invalidation, replacement, successor, history]
sources:
  - resource: 015-A-integrity-audit-scope-interference-surfaces-whole-system-coverage-subphase-planning.md
  - resource: 015-B-purpose-preservation-baseline-integrity-inventory-directional-interference-register.md
  - resource: 015-D-evaluation-occurrence-obligation-rubric-scorecard-judge-authorship-integrity.md
  - resource: ../canonical/concepts/versioning.md
  - resource: ../canonical/concepts/provenance.md
  - resource: ../canonical/concepts/evaluation-occurrence.md
  - resource: ../canonical/concepts/evaluation-obligation.md
  - resource: ../canonical/concepts/rubric.md
  - resource: ../canonical/concepts/scorecard.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: ../canonical/synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../canonical/experience/authority-lineage-correction.md
  - resource: ../canonical/policies/correction-authority.md
  - resource: ../canonical/invariants/current-vs-historical-truth.md
  - resource: ../canonical/invariants/one-logical-scorecard.md
  - resource: ../canonical/invariants/organizer-not-judge-author.md
---

# Purpose

Audit whether MUDAC can correct authoritative evaluation truth without destroying historical truth, transferring authorship, reopening terminal responsibility, or letting generic history mechanisms become domain authority.

The temporal chain under audit is:

```text
authoritative state changes legitimately
  → Versioning preserves immutable predecessor/successor authority

why/how/source/actor differs
  → Provenance preserves explanatory history

source/domain fact later proves unusable or wrong
  → smallest semantic owner corrects / invalidates / replaces

historical responsibility already terminal
  → remains historical

new legitimate work required
  → explicit successor responsibility

dependent result no longer reflects source
  → dependent owner becomes Affected / Stale / recomputed as appropriate
  != silent replacement
```

015-E dispositions DIR-014 through DIR-025, including the temporal rechecks carried from 015-D.

# Decision

**015-E COMPLETE — PASS. Proceed to 015-F.**

```text
DIR-014 through DIR-025                 DISPOSITIONED
confirmed integrity violation           NONE
INT-F corrective finding opened         NONE
upstream semantic reopen                NONE
canonical semantic repair               NONE
purpose-preserved explicit limitations  3
cross-cluster rechecks retained         DIR-022 / 025
NEXT                                    015-F
```

The three explicit limitations are:

1. a Version may remain current/eligible within its own logical lineage while the composed evidence is ineligible for another purpose because a dependency such as Evaluation Occurrence is invalid;
2. Provenance correction changes explanatory/best-known history, but separate natural-owner correction is still required when the corrected fact changes domain validity;
3. retained Version/Provenance/history can continue to exist after current Access ends, even when the former actor may no longer inspect or act on that history.

# 1. Purpose obligations exercised

015-E principally exercises:

- **P-05 — Resilient evaluation continuity**;
- **P-06 — Trustworthy and explainable outcome formation**;
- **P-07 — Correctable authority and historical truth**;
- **P-08 — Contextual confidentiality and authority separation**.

Supporting obligations include P-01 where authorship can be threatened by correction and P-04 where replacement/successor work affects operational continuation.

Primary invariants:

```text
INV-002 One Logical Evaluation per Evaluation Obligation
INV-004 Organizer Does Not Become Judge Author
INV-005 Current vs Historical Truth
INV-008 Capture-Channel Parity
INV-010 Truthful Authority Under Uncertainty
```

# 2. Temporal model under audit

The current design deliberately preserves independent temporal dimensions:

```text
domain lifecycle
working vs committed authority
lineage currentness
validity / eligibility
replacement
dependency currency
distribution state
historical observation
```

Therefore:

```text
Superseded
  != Invalidated
  != Replaced
  != Affected
  != Stale
  != Withdrawn
```

Integrity depends on keeping those meanings owner-specific.

# 3. Counterexample set

## E-P01 — new Rubric Version exists

Attempt:

> Rebind every historical evaluation to the latest Rubric.

Rejected.

Ordinary Rubric supersession is prospective. Existing occurrences, obligations and Scorecards stay bound to the exact Version actually used.

## E-P02 — current Rubric Version is invalidated

Attempt:

> Automatically invalidate every historical dependent object.

Rejected.

Impact is selective and reason-sensitive. A prepared occurrence may become unusable, an open/complete occurrence may require invalidation, or a defect may affect only one Scorecard. The dependency is assessed rather than destructively cascaded.

## E-P03 — current Scorecard Version invalidated

Attempt:

> Revive the last superseded Version as current.

Rejected.

The lineage may legitimately have no current eligible Version.

## E-P04 — occurrence invalidated after Scorecard finalized

Attempt:

> Delete/invalidate all Judge-authored history because the occurrence is no longer eligible.

Rejected.

The occurrence, Scorecard and obligation history remain attributable. Current use/eligibility changes separately.

## E-P05 — satisfied evidence becomes ineligible

Attempt:

> Set the old obligation back to Outstanding.

Rejected.

Historical satisfaction remains terminal. If another evaluation is legitimately required, create a successor obligation and new logical Scorecard.

## E-P06 — evidence invalidated

Attempt:

> Automatically create new Judge work.

Rejected.

Successor work is a deliberate, policy-governed action and may not be required at all.

## E-P07 — Organizer corrects a transcription error

Attempt:

> Treat correction Actor as Judge or classify correction as Judge amendment.

Rejected.

Actor, RepresentedAuthority, Source and classification remain distinct.

## E-P08 — Provenance metadata was wrong

Attempt:

> Correct Provenance and assume domain validity changed automatically.

Rejected.

Provenance correction is explanatory. A separate domain transition is required if the corrected fact changes domain validity.

## E-P09 — Judge Access ends

Attempt:

> Remove or forget prior Version/Provenance/history because the Judge can no longer inspect it.

Rejected.

Retention/history and current capability are separate. Appropriate Access governs current inspection.

# 4. DIR-014 — Rubric current definition → historical Scorecard / Occurrence

**Disposition: NO INTEGRITY VIOLATION — TEMPORAL RECHECK CLOSED.**

015-D established exact-basis binding.

015-E confirms temporal behavior:

```text
new Rubric Version
  → prospective successor authority

historical occurrence / obligation / Scorecard
  → remain bound to exact earlier Rubric Version
```

Rubric supersession therefore does not reinterpret earlier judgment.

Rubric invalidation is different from supersession and requires reason-sensitive dependency assessment.

This preserves both Rubric interpretation semantics and historical Scorecard truth.

# 5. DIR-015 — reassignment/substitution → Scorecard authorship

**Disposition: NO INTEGRITY VIOLATION — TEMPORAL RECHECK CLOSED.**

Structural Scorecard identity remains:

```text
Evaluator
Subject
OccurrenceContext
EvaluationBasis
```

A later staffing/responsibility change never mutates those values in place.

If evaluator responsibility changes:

```text
predecessor obligation ends appropriately
  + successor obligation if legitimate
  → replacement evaluator performs distinct work
  → new logical Scorecard
```

If the structural binding of an already-recorded Scorecard is wrong, ordinary amendment/capture correction cannot repair it.

The bad record/history is preserved and current eligibility is corrected through explicit invalidation/replacement paths.

# 6. DIR-016 — paper/assisted capture → authorship over time

**Disposition: PURPOSE PRESERVED — TEMPORAL RECHECK CLOSED; 015-I MAPPING RECHECK RETAINED.**

015-D established:

```text
Actor                = capture/correction actor
RepresentedAuthority = Judge
semantic author      = Judge
Source               = identified Judge-origin source
```

015-E confirms correction semantics.

## Judge semantic amendment

Judge's judgment changes.

```text
current Version
  → amendment Draft
  → explicit Finalize Amendment
  → successor Version
```

The predecessor remains current until successor establishment.

## Source-faithful capture correction

Judge judgment does not change; digital representation is corrected to match verified unchanged source.

```text
same logical Scorecard
same Judge author
same obligation
same evaluation weight
different correction Actor permitted
```

Versioning can provide the same successor mechanics while Provenance/policy preserve the semantic difference.

Therefore shared history machinery does not flatten authorship meaning.

# 7. DIR-017 — Access change → retained evaluation authority/history

**Disposition: NO INTEGRITY VIOLATION — TEMPORAL RECHECK CLOSED.**

Current Access may end while historical evaluation state remains retained.

```text
Access revoked / Participation complete
  → current capability may end

retained Scorecard Versions
retained Provenance
retained occurrence/obligation history
  → do not disappear
```

Current inspection remains subject to appropriate Access.

Thus:

```text
retention != visibility
visibility != authorship
current capability != historical existence
```

# 8. DIR-018 — amendment/capture correction → Versioning

**Disposition: NO INTEGRITY VIOLATION.**

Both Judge amendment and capture correction may legitimately use same-lineage successor Version mechanics.

Versioning answers:

> what committed authoritative snapshots existed and which is current/eligible for the lineage?

It does not answer:

> why the successor was legitimate or whose semantic intent changed?

That meaning remains in Scorecard/Provenance/policy.

```text
same Versioning mechanism
  != same semantic correction class
```

The predecessor remains immutable history in both cases.

# 9. DIR-019 — Versioning currentness → domain correction semantics

**Disposition: NO INTEGRITY VIOLATION.**

Versioning does not own correction legitimacy.

```text
domain/policy authorizes correction
  → Versioning may record successor/invalidation

Versioning state
  != authority to decide correction
```

Generic Commit/Invalidate administration is intentionally not a MUDAC user-facing semantic action.

Purpose-specific application actions invoke Versioning.

This prevents a reusable history Concept from becoming universal domain authority.

# 10. DIR-020 — occurrence invalidation → obligation history

**Disposition: NO INTEGRITY VIOLATION.**

Occurrence invalidation distinguishes Outstanding from terminal obligations.

## Outstanding predecessor

An Outstanding obligation tied to invalid occurrence cannot remain satisfiable against that invalid context.

It is explicitly ended/cancelled as appropriate.

Replacement work is separately established.

## Historically Satisfied predecessor

```text
Satisfied
  remains Satisfied historically

linked evidence/current context becomes ineligible
  != obligation reopens
```

If another evaluation is required, successor responsibility is created.

This protects historical accomplishment and current eligibility simultaneously.

# 11. DIR-021 — occurrence/basis/evidence invalidation → Scorecard

**Disposition: PURPOSE PRESERVED WITH EXPLICIT OWNER-LOCAL ELIGIBILITY LIMITATION.**

This is the most important temporal subtlety in Cluster C.

A Scorecard can remain authentic historical Judge-authored evidence while becoming unusable for a current downstream purpose because an external dependency is invalid.

For example:

```text
Scorecard Version
  = authentic retained Judge judgment

Evaluation Occurrence
  = Invalidated

therefore:
  Scorecard historical/authorship truth remains
  current aggregation eligibility may be lost
```

MUDAC does not need to destructively invalidate every dependent Scorecard Version merely to express the loss of composition-level eligibility.

Versioning currentness is therefore **owner-local**, not a universal statement that the Version is usable in every composed context.

When the Scorecard content itself is unusable, its Version may separately be invalidated.

This distinction preserves both Versioning and Scorecard purposes.

# 12. DIR-022 — evidence ineligibility → successor responsibility

**Disposition: NO INTEGRITY VIOLATION; 015-H AUTOMATION RECHECK RETAINED.**

Evidence becoming ineligible does not automatically create new Judge work.

```text
evidence ineligible
  → factual gap / affected downstream state

policy/authority decision
  → maybe exception
  → maybe successor evaluation
  → maybe other consequence
```

Only a deliberate governed action creates successor obligation.

If created:

- predecessor remains terminal;
- successor is Outstanding;
- successor uses a new logical Scorecard;
- no predecessor history is rewritten.

015-H must ensure automation/chaining never turns dependency propagation into automatic discretionary successor authority.

# 13. DIR-023 — Provenance roles → Scorecard authorship

**Disposition: NO INTEGRITY VIOLATION.**

Provenance explains roles; it does not redefine them.

```text
Actor
RepresentedAuthority
Source
classification
  → explanatory evidence

Scorecard semantic author
  → remains Scorecard/domain truth
```

Provenance can truthfully state that Organizer performed capture/correction while Judge remained represented semantic authority.

It cannot use metadata to manufacture Judge authorship where the source/domain evidence does not support it.

# 14. DIR-024 — Provenance correction → historical/domain authority

**Disposition: PURPOSE PRESERVED WITH EXPLICIT EXPLANATORY-ONLY LIMITATION.**

Incorrect Provenance is corrected append-stably.

That can change the best-known explanation of:

- who acted;
- whose authority was represented;
- source/channel;
- effective/capture time;
- classification.

It does not by itself mutate the domain subject.

If corrected provenance demonstrates that:

- wrong Judge was represented;
- wrong basis was used;
- occurrence facts were incorrect;
- evidence is structurally invalid;

then the natural domain owner must perform the separate correction/invalidation transition.

```text
Provenance correction
  != business/domain correction
```

This limitation is necessary for Provenance to remain explanatory rather than become a universal mutation mechanism.

# 15. DIR-025 — Access completion/revocation → retained Version/Provenance

**Disposition: PURPOSE PRESERVED WITH EXPLICIT RETENTION/VISIBILITY LIMITATION; 015-I RECHECK RETAINED.**

Historical authority survives loss of current actor capability.

```text
Access ends
  != Version deleted
  != Provenance deleted
  != occurrence/obligation history deleted
```

But retained history does not imply unrestricted inspection.

```text
history retained
  + current audience/capability context
  → Access decides whether current inspection/action is permitted
```

This preserves P-07 history and P-08 confidentiality together.

015-I must verify combined history/audit/Judge/Organizer mappings explain this without implying that unavailable means nonexistent.

# 16. Corrected historical assertions integrity

Current truth and best-known history can both change without erasing prior recorded history.

When later evidence shows a recorded historical assertion was wrong, preserve:

```text
as-recorded / as-known claim
corrected best-known historical assertion
correction Provenance
```

If the corrected fact affects domain validity, the natural owner separately changes eligibility/validity.

This allows three questions to remain distinct:

```text
what is current now?
what was considered authoritative then?
what does MUDAC now believe actually happened then?
```

INV-005 remains preserved.

# 17. Supersession / invalidation / replacement integrity

The cluster maintains:

```text
same logical lineage + explicit successor
  → Superseded predecessor

retained committed state no longer eligible
  → Invalidated

distinct subject/occurrence stands in place of another
  → Replacement
```

No transition silently implies another.

Especially:

- invalidation does not revive older predecessor;
- invalidation does not create successor;
- replacement does not clone participants/responsibility/evidence;
- successor Version does not imply predecessor was erroneous.

# 18. Successor-work integrity

A terminal obligation never reopens.

```text
terminal predecessor
  + legitimate need for new evaluation
  → successor obligation
  → new logical Scorecard
```

Successor work is conditional and policy-governed.

This preserves:

- historical responsibility truth;
- one-logical-evaluation invariant;
- fair accounting of actual work;
- no hidden automation authority.

# 19. Downstream affectedness boundary

Cluster C establishes source-side truth and the need to re-evaluate dependent currency.

It does not own downstream outcome decisions.

```text
source correction / invalidation
  → actual dependents may become Affected / Stale / require recomputation

but:
  != Award moves automatically
  != Outcome Declaration silently replaced
  != Export SourceBasis rewritten
  != Publication withdrawn/retargeted
```

Those consequences are audited in 015-F through 015-H.

# 20. Subject-purpose integrity summary

| Subject | Integrity result |
| --- | --- |
| Versioning | Purpose preserved; immutable successive authority/currentness remains domain-neutral and owner-local |
| Provenance | Purpose preserved with explicit explanatory-only correction boundary |
| Evaluation Occurrence | Purpose preserved; invalidation changes eligibility without erasing event truth |
| Evaluation Obligation | Purpose preserved; terminal history remains terminal and successor work is separate |
| Rubric / exact basis | Purpose preserved; supersession prospective, invalidation selective |
| Scorecard | Purpose preserved; authentic authored history survives external dependency invalidation |
| Access | Purpose preserved; current visibility/capability can end without deleting retained history |

# 21. Material finding result

015-E opens no corrective INT-F finding.

```text
INT-F corrective findings opened in 015-E = 0
```

Reason:

- no temporal transition requires destructive historical rewrite;
- generic Versioning/Provenance do not acquire domain correction authority;
- invalidation does not silently revive or replace;
- terminal responsibility does not reopen;
- successor work is deliberate rather than automatic;
- authorship survives capture/correction;
- owner-local currentness and composition-level evidence eligibility remain distinguishable.

# 22. Cross-cluster carry/recheck

The following remain later rechecks, not unresolved Cluster-C defects:

- **DIR-022 → 015-H** — system-triggered dependency propagation must not manufacture successor responsibility;
- **DIR-025 → 015-I** — combined history/profile mapping must distinguish retained existence from current visibility;
- source correction / affectedness → **015-F** for Coverage/Aggregate/Rank/Award/Outcome Declaration;
- source correction / external representations → **015-G** for Export/Publication;
- multi-owner correction chains → **015-H**.

# 23. Implementation boundary

015-E does not prescribe:

- storage/event-sourcing architecture;
- transaction isolation;
- CAS implementation;
- database history tables;
- audit-log technology;
- event buses/queues;
- automatic cascade implementation;
- authorization middleware;
- retention storage mechanism.

```text
immutable history
  != event-sourcing mandate

expected-current semantics
  != specific CAS/storage design

affected-state propagation
  != event bus

Access-controlled history
  != authorization middleware design
```

# Exit

**015-E COMPLETE — PASS.**

No semantic correction or upstream reopen is required.

Proceed to **015-F — Coverage, Aggregate, Rank, Award, Competition Finalization & Outcome Declaration Integrity**.
