---
type: Phase Design Record
title: 015-C — Competition Context, Competitor Structure, Identity, Participation, Alias, Access & Panel Integrity
description: "Audits Cluster A purpose preservation across Competition lifecycle, Division/Team/Alias competitor context, Panel intended grouping, Identity continuity, Participation capacity and contextual Access, and dispositions DIR-001 through DIR-009."
status: stable
tags: [phase-015, integrity, competition, division, team, panel, identity, participation, alias, access]
sources:
  - resource: 015-A-integrity-audit-scope-interference-surfaces-whole-system-coverage-subphase-planning.md
  - resource: 015-B-purpose-preservation-baseline-integrity-inventory-directional-interference-register.md
  - resource: ../canonical/project/purpose-needs-success-tensions.md
  - resource: ../canonical/concepts/competition.md
  - resource: ../canonical/concepts/division.md
  - resource: ../canonical/concepts/team.md
  - resource: ../canonical/concepts/panel.md
  - resource: ../canonical/concepts/identity.md
  - resource: ../canonical/concepts/participation.md
  - resource: ../canonical/concepts/alias.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/synchronizations/competition-participation-access.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/experience/context-role-modes.md
  - resource: ../canonical/experience/judge-onboarding.md
  - resource: ../canonical/experience/organizer-preparation.md
  - resource: ../canonical/policies/anonymity-disclosure.md
  - resource: ../canonical/policies/panel-composition.md
  - resource: ../canonical/policies/operational-exception-governance.md
  - resource: ../canonical/mechanisms/panel-membership-composition.md
  - resource: ../canonical/invariants/current-vs-historical-truth.md
  - resource: ../canonical/invariants/judge-independence.md
  - resource: ../canonical/invariants/organizer-not-judge-author.md
---

# Purpose

Audit the first substantive Phase-015 integrity cluster:

```text
Competition
Division
Team
Panel
Identity
Participation
Alias
Access
```

The question is whether their composition still permits each owner to fulfill its own purpose without another owner silently changing lifecycle, identity, grouping, disclosure or semantic authority.

015-C primarily dispositions DIR-001 through DIR-009 from 015-B.

# Decision

**015-C COMPLETE — PASS. Proceed to 015-D.**

```text
DIR-001 through DIR-009                  DISPOSITIONED
confirmed integrity violation            NONE
INT-F corrective finding opened          NONE
upstream semantic reopen                 NONE
canonical semantic repair                NONE
purpose-preserved explicit limitations   2
cross-cluster rechecks retained          DIR-002 / 005 / 006 / 007 / 008 / 009
NEXT                                     015-D
```

The cluster preserves structural integrity.

Two explicit limitations are important and intentional:

1. a completed Judge Participation may remain attributable context for narrow continuation of an already-established Outstanding Evaluation Obligation when current policy and a fresh Access decision permit it;
2. Alias provides controlled bias-aware alternate identity, not absolute real-world anonymity or permanent non-resolvability.

Neither limitation transfers semantic authority or rewrites historical truth.

# 1. Purpose obligations exercised

015-C principally exercises:

- **P-02 — Fair and bias-aware Team treatment**;
- **P-03 — Low-friction and accessible participation**;
- **P-04 — Live operational coordination and completion**;
- **P-05 — Resilient evaluation continuity**, at the Event Completed seam;
- **P-08 — Contextual confidentiality and authority separation**.

Supporting concerns include P-01 where Judge independence/disclosure is affected and P-07 where current competitor/grouping corrections must not rewrite historical context.

Material tensions include T-01, T-02, T-03, T-04, T-06, T-08 and T-09.

# 2. Counterexample set

## C-P01 — Returning Identity in a new Competition

Counterexample attempt:

> Reuse a verified Identity and infer that the person is already a Judge in the new Competition.

Current composition rejects the inference:

```text
Identity continuity
  != Participation
  != Panel membership
  != Access
  != responsibility
```

A new Competition uses a new Participation.

## C-P02 — One human has Judge and Organizer Participation

Counterexample attempt:

> Organizer-sensitive visibility should become available while the human is in Judge context because the same Identity has both capacities.

Current mapping explicitly prohibits capability union.

Protected operations use one explicit Participation context plus a fresh Access decision.

## C-P03 — Competition becomes Active

Counterexample attempt:

> Activating Competition should automatically activate every Judge Participation and create judging responsibility.

Current synchronization rejects all three consequences.

Competition activation does not automatically activate Participations, create Panel membership, begin Evaluation Occurrences, establish Evaluation Obligations, or create Scorecards.

## C-P04 — Event Completed with unfinished Judge work

Counterexample attempt:

> Completing the live event must either keep the Judge fully Active or universally revoke all Judge work.

Both extremes are rejected.

```text
Event Completed
  → broad/new ordinary live-event capability closes
  != universal hidden Access revocation

existing Outstanding obligation
  + legitimate same binding
  + policy permits continuation
  + fresh Access permits specific work
  → same logical evaluation may continue
```

This is a purpose-preserving limitation on Completed Participation, not reactivation.

## C-P05 — Panel member absent at occurrence start

Counterexample attempt:

> Panel membership should be enough to record occurrence participation and responsibility.

Current composition rejects this. Only the confirmed actual starting evaluator set enters Evaluation Occurrence begin; obligations are then established separately.

## C-P06 — Panel membership changes after occurrence begin

Counterexample attempt:

> Changing Panel membership should update historical occurrence participants and obligations.

Current semantics preserve the begun occurrence and responsibility history. Panel changes affect reusable current grouping/future planning only unless a separate deliberate action changes another owner.

## C-P07 — Division/Alias correction after judging began

Counterexample attempt:

> Correcting current Division or Alias should rewrite what the Judge historically saw.

Current composition rejects this under INV-005.

Evaluation Occurrence preserves PresentedContext. Current correction changes current truth, not the historical snapshot.

## C-P08 — Organizer/support resolves Alias

Counterexample attempt:

> Because authorized Organizer/history contexts can identify the underlying Team, Alias has failed to provide anonymity and should be treated as globally exposed.

Current policy defines controlled identity disclosure rather than absolute real-world anonymity.

Judge-safe context remains Alias + Division. Authorized resolution in a distinct context does not itself change what Judge context may disclose.

If protected information was actually leaked into Judge context, that becomes attributable correction/integrity pressure rather than retrospective denial that the disclosure occurred.

## C-P09 — Technical support has broad system privilege

Counterexample attempt:

> Technical capability should allow support to perform Organizer or Judge semantic actions.

Current policy and Access boundaries reject this.

Technical privilege may restore/restrict operation but cannot create Judge authorship, Organizer decision authority, competition policy exceptions, protected disclosure permission, or outcome/publishing authority.

# 3. DIR-001 — Competition lifecycle → Participation

**Disposition: NO INTEGRITY VIOLATION.**

Competition and Participation retain independent purposes.

```text
Competition.activate
  != mass Participation.activate

Participation.activate
  != Competition.activate
```

At Event Completed, completing currently Active live Judge Participations is a legitimate coordinated consequence because ordinary live-event involvement has ended.

This does not erase Participation history or imply every other capacity must complete. Organizer Participation may remain current for post-event work.

Participation therefore remains one Participant taking part in one Scope for a limited period and Capacity; Competition supplies context rather than absorbing Participation authority.

# 4. DIR-002 — Competition + Participation lifecycle → Access

**Disposition: PURPOSE PRESERVED WITH EXPLICIT LIMITATION.**

Current design correctly avoids both integrity failures:

```text
Event Completed
  → every form of Judge work impossible
```

and:

```text
Outstanding obligation exists
  → Participation becomes Active again
  → broad live capability restored
```

Instead, narrow continuation uses completed Participation as attributable Competition/capacity context and requires a fresh Access decision for the specific pre-existing responsibility.

```text
completed Participation
  may remain relevant contextual fact
  != current broad live authority
```

**Recheck:** 015-D must confirm this composes correctly with Evaluation Obligation and Scorecard purpose.

# 5. DIR-003 — Identity reuse → Participation

**Disposition: NO INTEGRITY VIOLATION.**

```text
returning Identity
  → may reduce repeated identity establishment
  != resumed Participation
  != resumed Panel membership
  != Access
```

The composition preserves both P-03 low friction and P-08 authority separation.

# 6. DIR-004 — Participation/capacity → Identity

**Disposition: NO INTEGRITY VIOLATION.**

Participation never overwrites stable Identity continuity.

```text
Identity
  = human continuity

Participation
  = scoped capacity episode
```

Completing, withdrawing or changing a Participation does not change who the human is or rewrite historical attribution.

# 7. DIR-005 — Panel membership → Evaluation Occurrence / Obligation

**Disposition: NO INTEGRITY VIOLATION IN CLUSTER A; 015-D RECHECK RETAINED.**

Panel remains reusable intended grouping because membership itself creates neither actual occurrence participation nor evaluation responsibility.

```text
Panel membership
  → candidate evaluator set only

Participation + Access + presence/recusal + policy
  → confirmed starting evaluator set

EvaluationOccurrence.begin
  → actual occurrence participants
  + EvaluationObligation.establish × N
```

Panel changes after begin do not rewrite occurrence or obligation history.

A governed Panel-composition exception preserves the actual shortfall instead of inventing members.

# 8. DIR-006 — Team/Division/Alias correction → historical Evaluation Occurrence context

**Disposition: NO INTEGRITY VIOLATION.**

Before begin, a material competitor-context change that invalidates the prepared presentation blocks ordinary begin and permits cancellation/new preparation.

After begin:

```text
current Team/Division/Alias change
  != rewrite PresentedContext
```

Historical Evaluation Occurrence owns what was actually presented.

No owner must preserve known-wrong current state merely to preserve history.

**Recheck:** 015-D must confirm historical PresentedContext continues to bind evaluation work correctly.

# 9. DIR-007 — Alias resolution/disclosure → Team confidentiality

**Disposition: PURPOSE PRESERVED WITH EXPLICIT LIMITATION.**

Alias promises context-specific alternate identity and default non-exposure in that context.

It does not promise absolute real-world anonymity, non-resolvability to all authorities, authentication secrecy, or permanent separation from Team identity.

```text
Judge-safe context
  → Alias + Division

authorized Organizer/history context
  → may resolve underlying Team identity

Organizer visibility
  != Judge visibility
  != Export inclusion
  != public disclosure
```

A real disclosure into the wrong audience remains attributable and may require impact/correction analysis; later revocation cannot pretend it never happened.

**Recheck:** 015-I must confirm combined profile/mapping behavior keeps this distinction intelligible.

# 10. DIR-008 — Access/technical privilege → semantic authority

**Disposition: NO INTEGRITY VIOLATION.**

```text
Access permits operation
  != semantic authorship
  != Competition decision authority

support/admin privilege
  != Judge Participation
  != Organizer Participation
  != policy-exception authority
```

Governed exceptions remain scoped and attributable; generic override cannot bypass semantic invariants.

**Rechecks:** 015-H for coordinated/system-triggered actions; 015-I for profile representation.

# 11. DIR-009 — Phase-014 Team genericity → neighboring composition

**Disposition: NO INTEGRITY VIOLATION.**

Current Team means one competing group acting as a single unit within Scope. PF-01 binds that group to student teams.

No neighboring Concept requires student as intrinsic Team semantics.

Current neighbors rely on stable Team identity, Competition Scope, competing-unit status, Division assignment, Alias, occurrence Subject binding, and outcome Recipient/subject references.

```text
intrinsic Team genericity
  + PF-01 student-team binding
  → purpose-preserving composition
```

**Recheck:** 015-I must confirm user-visible PF-01 wording remains student-Team specific without re-specializing canonical Team.

# 12. Subject-purpose integrity summary

| Concept | Result |
| --- | --- |
| Competition | Purpose preserved; lifecycle remains context rather than downstream semantic authority |
| Division | Purpose preserved; current cohort correction does not rewrite historical presentation |
| Team | Purpose preserved; stable competing unit and Phase-014 genericity survive composition |
| Panel | Purpose preserved; intended grouping remains distinct from actual participation/responsibility |
| Identity | Purpose preserved; human continuity stays independent from scoped capacity |
| Participation | Purpose preserved with explicit post-event contextual limitation |
| Alias | Purpose preserved with explicit controlled-disclosure limitation |
| Access | Purpose preserved; capability/disclosure does not absorb identity, participation, authorship or decision authority |

# 13. Multi-Concept chain integrity

## Entry and ordinary context

```text
Identity
  → Competition-specific Participation
  → optional Panel planning context
  → one explicit current capacity context
  → fresh Access for protected operation
```

No step manufactures the next owner's state.

## Competitor context into evaluation

```text
current Team
+ current Division
+ current Alias
  → prepared Judge-facing PresentedContext

prepared context
  + actual current evaluator facts
  → begun Evaluation Occurrence
```

The historical occurrence snapshot then decouples from later current competitor-state correction.

## Event completion with unfinished work

```text
Competition.completeEvent
  → active live Judge Participations complete
  → broad ordinary live capability closes

existing Outstanding responsibility
  + policy
  + fresh scoped Access
  → same logical work may continue narrowly
```

This preserves event lifecycle truth and resilient work continuity.

# 14. Derived state and exception integrity

Cluster A uses derived readiness and Panel-composition state without promoting them to authority owners.

```text
Ready to Judge
  != Participation state
  != Panel membership
  != Evaluation Obligation
  != Access grant

Panel Composition = Degraded
  + governed exception
  → may permit proceed
  != Panel objectively Compliant
  != fictitious participant
```

Operational exceptions change permitted consequence only where policy allows and never rewrite source truth.

# 15. Material finding result

015-C opens no corrective INT-F finding.

Reason:

- every DIR-001 through DIR-009 candidate is purpose-preserving under current composition or a documented limitation compatible with current purpose;
- no current owner promises something composition makes impossible;
- no current mapping/synchronization attributes semantic authority to the wrong owner in this cluster;
- no Phase-014 Team refinement breaks neighboring Concept assumptions.

```text
INT-F corrective findings opened in 015-C = 0
```

# 16. Cross-cluster rechecks

These remain active rechecks, not unresolved defects:

- DIR-002 → 015-D;
- DIR-005 → 015-D;
- DIR-006 → 015-D;
- DIR-007 → 015-I;
- DIR-008 → 015-H and 015-I;
- DIR-009 → 015-I.

015-B remains the directional source register; this record supplies Cluster-A dispositions.

# 17. Implementation boundary

No conclusion depends on authentication/session implementation, authorization middleware, database structure, runtime transaction/orchestration design, timeout values, cache invalidation, UI component routing or executable tests.

```text
current context
current capacity
historical attribution
semantic authority
purpose-specific disclosure
intended grouping
actual participation
```

are conceptual meanings.

# Exit

**015-C COMPLETE — PASS.**

No semantic correction/reopen is required.

Proceed to **015-D — Evaluation Occurrence, Obligation, Rubric, Scorecard & Judge-Authorship Integrity**.
