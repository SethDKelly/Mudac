---
type: Phase Design Record
title: 013-H — Award, Competition Finalization, Outcome Declaration, Officiality & Successor-Authority Mapping
description: "Maps Award recognition, coordinated Competition Finalization and initial Outcome Declaration, official-result currentness, affected declarations and explicit successor authority without collapsing calculated, recognized, finalized, official, public or delivered meanings."
status: stable
tags: [phase-013, jackson, mapping, award, finalization, outcome-declaration, officiality, successor-authority]
sources:
  - resource: 013-G-live-operations-remaining-work-exception-reconciliation-derived-outcome-state-mapping.md
  - resource: ../canonical/experience/mapping-authority-baseline.md
  - resource: ../canonical/experience/reconciliation-derived-state.md
  - resource: ../canonical/experience/reconciliation-finalization.md
  - resource: ../canonical/concepts/award.md
  - resource: ../canonical/concepts/competition.md
  - resource: ../canonical/concepts/outcome-declaration.md
  - resource: ../canonical/synchronizations/evaluation-outcome-finalization-declaration.md
  - resource: ../canonical/policies/awards-finalization.md
  - resource: ../canonical/invariants/calculated-not-official.md
  - resource: ../canonical/invariants/official-not-automatically-public.md
  - resource: ../canonical/invariants/current-vs-historical-truth.md
---

# Purpose

Map the high-consequence authority boundary from reconciled/derived Competition state into recognized Awards, closed Competition lifecycle and explicit official Outcome Declaration authority.

013-H defines user-visible semantics for:

- rank-derived versus discretionary Award recognition;
- Award conferral, revocation and corrected conferral as explicit authority;
- Finalization Readiness versus Competition Finalization;
- coordinated ordinary `Finalize Competition & Declare Outcome` closeout;
- Competition lifecycle closure versus official-result declaration ownership;
- Outcome Declaration `Current`, `Affected` and `Superseded` currentness;
- post-Finalization source correction;
- explicit successor official authority;
- current official authority versus historical declared authority;
- official-but-non-public operation.

013-H stops before Export generation, Publication release, audience disclosure realization and delivery. Those mappings belong to 013-I.

It does not prescribe modal layout, confirmation component design, transaction boundaries, databases, event buses, audit-table schemas, message delivery, report formats or implementation architecture.

# Decision

**COMPLETE — PASS. Proceed to 013-I.**

```text
013-A START GATE                                  COMPLETE — READY
013-B AUTHORITY / CORPUS BASELINE                COMPLETE — PASS
013-C CONTEXT / JUDGE ENTRY MAPPING              COMPLETE — PASS
013-D ORGANIZER PREPARATION MAPPING              COMPLETE — PASS
013-E ACTIVE EVALUATION MAPPING                  COMPLETE — PASS
013-F AUTHORITY / CORRECTION MAPPING             COMPLETE — PASS
013-G LIVE OPS / RECONCILIATION MAPPING          COMPLETE — PASS
013-H AWARD / OFFICIALITY MAPPING                COMPLETE — PASS
OUTCOME-OFFICIALITY OWNER CREATED                YES
RANK == AWARD AUTHORITY                          PROHIBITED
RANK-DERIVED AWARD == AUTOMATIC CONFERRAL        PROHIBITED
DISCRETIONARY AWARD == MATHEMATICAL RESULT       PROHIBITED
FINALIZATION READINESS == FINALIZED               PROHIBITED
COMPETITION FINALIZED == OFFICIAL RESULT          PROHIBITED
CALCULATED / RANKING READY == OFFICIAL            PROHIBITED
OUTCOME DECLARATION == PUBLICATION                PROHIBITED
AFFECTED == SUPERSEDED                            PROHIBITED
CORRECTED CALCULATION == SUCCESSOR OFFICIALITY    PROHIBITED
SUCCESSOR DECLARATION RE-FINALIZES COMPETITION   PROHIBITED
OFFICIAL OUTCOME REVISION RESTORED               NO
PHASE-010 REOPEN REQUIRED                        NO
PHASE-011 REOPEN REQUIRED                        NO
PHASE-012 REOPEN REQUIRED                        NO
NEXT                                               013-I
ARCHITECTURE / IMPLEMENTATION                     SUSPENDED
```

# 1. Governing authority model

013-G ends with reconciled current sources and derived readiness. 013-H begins when an authorized actor deliberately establishes recognition and official authority.

```text
current eligible evidence
  → Coverage / Aggregate / Rank / readiness
  → required Award decisions
  → reconciled Closeout Basis
  → explicit Finalize Competition & Declare Outcome
  → Competition = Finalized
  + Outcome Declaration = Current official authority
```

The arrows represent application composition and explanation, not ownership transfer.

Preserve throughout:

```text
calculated
  != ranking ready
  != recognized
  != Competition Finalized
  != official
  != public
  != delivered
```

# 2. Award recognition is explicit authority

Award owns recognition definition and conferral history. Rank may supply a SelectionBasis but never owns recognition.

## Rank-derived Award

A rank-derived Award must be represented as recognition conferred **from** a current Ranking Ready basis under its declared Award rule.

```text
Ranking Ready Rank basis
  + Award rule / scope / eligibility / tie-cardinality semantics
  + legitimate conferral authority
  → Confer Rank-Derived Award
  → Award recognition exists
```

The experience must not imply that a calculated first-place position automatically creates an Award.

Where useful before conferral, a derived candidate may be shown as a candidate implied by the rule, but it must remain visibly distinct from conferred recognition.

An Organizer cannot override a rank-derived Award's declared rule while continuing to represent the Award as rank-derived.

## Discretionary Award

A discretionary Award is an authorized human recognition choice under a definition that permits discretionary selection.

The experience must not portray a discretionary recipient as mathematically implied merely because Rank, Scorecards, Notes or statistics are available.

Preserve:

```text
rank-derived selection
  != discretionary selection
```

# 3. Award correction and source change

A later Rank or source change never silently transfers recognition.

If current basis makes an existing Award inconsistent, the representation should identify the Award as requiring review/correction as applicable, while preserving the existing recognition history until explicit Award authority changes it.

Legitimate actions remain owner-specific, such as:

- revoke an existing conferral;
- correct a conferral;
- confer the appropriate recognition under the current basis.

A recalculated candidate is not itself a corrected Award.

# 4. Finalization Readiness is not lifecycle authority

013-G established Finalization Readiness as a derived permission-to-proceed projection.

013-H preserves:

```text
Finalization Readiness = true
  != Competition = Finalized
  != Outcome Declaration exists
```

Finalization Readiness may make the high-consequence closeout action available, but it does not perform that action.

If closeout conditions change before commitment, current source/derived state must be revalidated rather than relying on an older readiness display.

# 5. Closeout Basis

Before ordinary official closeout, the experience must make the accepted basis sufficiently intelligible for the authorized actor to understand what is being finalized/declared.

The Closeout Basis is composition data rather than a Concept and may identify, as applicable:

- the Competition in `Event Completed`;
- applicable Evaluation Policy and evaluation basis;
- current factual Coverage and separate exception dispositions;
- current Ranking Ready result scopes;
- current Aggregate/Rank basis for required ranked outcomes;
- tie/policy resolution;
- required/current Award decisions;
- unresolved correction/reconciliation conditions relevant to closeout;
- the exact OutcomeBasis intended for declaration.

The experience may summarize these inputs, but a summary does not become a separate source of truth.

# 6. Ordinary Finalize Competition & Declare Outcome

MUDAC ordinary closeout is one coordinated application action with two separately owned semantic results:

```text
Competition.finalize
+
OutcomeDeclaration.declare
```

User-visible success means both are established:

```text
Competition lifecycle = Finalized
AND
one explicit current Outcome Declaration exists
```

This must not be represented as one merged Concept.

Competition owns lifecycle closure.

Outcome Declaration owns official-result content, immutable OutcomeBasis, declaring authority, currentness and declaration history.

# 7. Consequence preview for closeout

Because closeout is high consequence, the representation should make material consequences intelligible before commitment, including:

- the Competition lifecycle will close as Finalized;
- the identified OutcomeBasis will become explicitly declared official authority;
- current required Award decisions included in the basis remain separately owned recognition;
- ordinary event operation does not reopen merely because a later correction occurs;
- officiality does not publish or disclose results externally.

This is a semantic consequence requirement, not a prescribed confirmation-dialog design.

# 8. Official authority is Outcome Declaration

Official outcome authority is established only through explicit Outcome Declaration.

Preserve:

```text
calculated Rank
  != Ranking Readiness
  != Competition Finalized alone
  != official Outcome Declaration
```

A Competition may conceptually be lifecycle-closed only as part of the coordinated ordinary MUDAC closeout path, but lifecycle state still does not own official-result content/history.

The mapping must not introduce a separate `Official Outcome Revision` object/state. That historical model remains deprecated.

# 9. Outcome Declaration currentness

The user-visible officiality model uses:

```text
Current
Affected
Superseded
```

## Current

`Current` means this declaration is the current explicitly declared official authority for its scope.

## Affected

`Affected` means the latest declaration materially depends on source/basis that has changed or become invalid/ineligible and requires official correction/review.

An Affected declaration:

- remains the latest explicitly declared official authority;
- retains its immutable declared OutcomeBasis;
- is not silently rewritten from newer calculations;
- is not equivalent to Superseded;
- does not make the Competition non-Finalized.

## Superseded

`Superseded` means an explicit successor Outcome Declaration has become current.

The predecessor remains historical declared authority and reconstructible.

# 10. Post-Finalization correction

A legitimate source correction after closeout:

```text
Competition remains Finalized
source/current evidence changes
  → derived state re-evaluates/recomputes
  → Award consistency reviewed/corrected explicitly if required
  → current Outcome Declaration identified Affected when its basis materially depends on changed source
```

The experience must not imply that source correction automatically rolls back Competition lifecycle or silently creates a new official outcome.

The latest corrected Aggregate/Rank may be visible for reconciliation/explanation while the Affected declaration remains the latest declared official authority.

# 11. Affected is not superseded

This distinction is critical for honest official-state representation.

```text
Outcome Declaration = Affected
  != no official declaration
  != corrected calculations are official
  != predecessor is Superseded
```

An Affected label should communicate that the declared authority requires correction/review without pretending that a replacement declaration already exists.

# 12. Confirm Successor Outcome Declaration

After corrected source, derived and Award state is reconciled, an authorized declaring actor may explicitly confirm a successor declaration.

```text
Affected current declaration
  + reconciled corrected OutcomeBasis
  + successor closeout conditions satisfied
  + explicit declaring authority
  → Confirm Successor Outcome Declaration
  → successor = Current
  → predecessor = Superseded
```

The successor has its own immutable declared OutcomeBasis and declaration time/authority.

A successor declaration does **not** re-finalize Competition. Competition remains Finalized throughout.

# 13. Same visible result can still require successor authority

If the corrected basis materially differs but winner/rank/Award values happen to remain visually identical, the affected predecessor is not silently cleared.

The experience must preserve:

```text
same visible result
  != same declared basis
```

Where the prior declared basis was materially affected, explicit successor confirmation remains required to establish official authority over the corrected basis.

# 14. Award and declaration history remain separately attributable

Outcome Declaration may include identified Award state in its OutcomeBasis, but it does not own Award history.

Likewise, Award correction does not by itself rewrite an Outcome Declaration.

If a declared basis depended materially on an Award that is later corrected, the current declaration may become Affected and requires the normal successor-declaration path after reconciliation.

# 15. Competition Finalization history

Competition Finalization is a lifecycle transition with its own history.

Post-Finalization correction does not change that historical fact or roll lifecycle backward.

A successor Outcome Declaration therefore changes official-result authority while preserving:

```text
one already-Finalized Competition lifecycle
+
multiple attributable declaration states over time where correction required
```

# 16. Official is not public

013-H establishes explicit internal official authority only.

Preserve:

```text
Outcome Declaration exists
  != Export generated
  != Publication released
  != result delivered
```

Competition Finalization likewise does not publish results.

An official-but-non-public Competition is a normal PF-01 state/profile, not an error or incomplete officiality state.

013-I owns audience/disclosure-aware representation and release mapping.

# 17. Action availability and feedback

High-consequence action availability should remain source-explainable.

| Action | Semantic availability | Result |
| --- | --- | --- |
| Confer Rank-Derived Award | Award definition current + Ranking Ready SelectionBasis + recipient/tie/cardinality consistency + authority | explicit Award recognition |
| Confer Discretionary Award | discretionary Award permits recipient + actor authorized | explicit human recognition |
| Revoke/Correct Award | existing conferral + applicable correction authority/reason | attributable Award history transition |
| Finalize Competition & Declare Outcome | Competition Event Completed + Finalization Ready/reconciled Closeout Basis + declaring authority | Competition Finalized + current Outcome Declaration |
| Identify Official Outcome Affected | current declaration materially depends on changed/ineligible source basis | declaration becomes Affected; content unchanged |
| Confirm Successor Outcome Declaration | current declaration Affected + corrected basis reconciled + authority | successor Current; predecessor Superseded |

Unavailable actions should explain the semantic blocker when doing so does not disclose protected information.

# 18. Truthful feedback under uncertainty

The experience must not claim Award conferral, Finalization, declaration, affectedness transition or successor confirmation when the authoritative result is unknown.

Feedback should distinguish, where relevant:

```text
request/action pending or result unknown
confirmed authority established
known rejection/failure and source reason
```

The exact runtime retry/transaction behavior remains downstream. Cross-cutting degraded/status semantics are re-audited in 013-J.

# 19. Authority and privilege boundary

Technical/admin privilege does not grant Award-selection, Finalization or declaring authority.

Organizer capability to inspect current state also does not imply authority to:

- contradict a derived Award rule;
- confer a discretionary Award without applicable authority;
- bypass Finalization blockers using a generic override;
- mark calculated results official;
- clear an Affected declaration without successor confirmation;
- publish official results merely because they are official.

Applicable Participation, Access, policy and exception authority remain explicit.

# 20. State explanation matrix

| User-visible meaning | Derived state | Award | Competition | Outcome Declaration | Authority meaning |
| --- | --- | --- | --- | --- | --- |
| Calculated/reconciled | current derived state | may be absent/pending | Event Completed | absent | not official |
| Recognition established | Ranking Ready/current basis | current conferral(s) | Event Completed | absent | recognized but not official closeout |
| Ready to close | Finalization Ready | required decisions current | Event Completed | absent | closeout permitted, not performed |
| Official closeout | accepted basis | current conferral(s) | Finalized | Current | explicit official authority exists |
| Source correction impacts official basis | corrected/recomputed | current/reviewed as applicable | Finalized | Affected | prior declaration still latest official authority but requires correction |
| Corrected official authority confirmed | corrected current basis | corrected/current as applicable | Finalized | successor Current; predecessor Superseded | corrected basis explicitly official |

This matrix is semantic explanation, not a database/status-widget specification.

# 21. Mapping risks closed or reduced

013-H closes/reduces:

- **MAP-R08** — Rank/Award/official declaration collapse: explicitly separated;
- **MAP-R09** — official/Export/Publication/delivery collapse: official boundary established; external half remains 013-I;
- **MAP-R10** — successor authority flattened to edit: Outcome Declaration successor path explicit;
- **MAP-R11** — official-but-non-public remains PF-01 profile, not product split;
- **MAP-R14** — Finalization Readiness remains derived, not editable/lifecycle authority;
- **MAP-R15** — technical privilege cannot establish Award/finalization/declaration authority.

No new Concept, synchronization or dependence defect requires upstream reopen.

# 22. 013-I handoff

013-I inherits these boundaries:

```text
Outcome Declaration
  = internal official authority
  != Export representation
  != Publication release
  != delivery

Competition Finalization
  != Publication

successor Outcome Declaration
  != silent rewrite of old Export/Publication

Affected official basis
  may affect representation currency
  but does not automatically withdraw Publication
```

013-I must map audience/disclosure-aware Export, representation currentness, Publication release/withdrawal/succession and external-recipient semantics without weakening current internal official authority.

# Exit decision

```text
013-H: COMPLETE — PASS
Award authority: EXPLICIT / OWNER-PRESERVING
Competition Finalization: EXPLICIT / DISTINCT
Outcome Declaration officiality: EXPLICIT / DISTINCT
Affected/successor authority: EXPLICIT / HISTORY-PRESERVING
Official Outcome Revision adapter: NOT RESTORED
Phase-010/011/012 reopen: NOT REQUIRED
Architecture/implementation: SUSPENDED
Next: 013-I
```
