---
type: Phase Design Record
title: 015-F — Coverage, Aggregate, Rank, Award, Competition Finalization & Outcome Declaration Integrity
description: "Audits Cluster D purpose preservation from current eligible evaluation evidence through factual Coverage, Aggregate/Rank derivation, Ranking/Finalization Readiness, Award recognition, Competition Finalization and explicit Outcome Declaration authority, including post-finalization correction and dispositions DIR-026 through DIR-034."
status: stable
tags: [phase-015, integrity, coverage, aggregate, rank, readiness, award, finalization, outcome-declaration, officiality]
sources:
  - resource: 015-A-integrity-audit-scope-interference-surfaces-whole-system-coverage-subphase-planning.md
  - resource: 015-B-purpose-preservation-baseline-integrity-inventory-directional-interference-register.md
  - resource: 015-D-evaluation-occurrence-obligation-rubric-scorecard-judge-authorship-integrity.md
  - resource: 015-E-versioning-provenance-temporal-correction-successor-work-historical-truth-integrity.md
  - resource: ../canonical/concepts/competition.md
  - resource: ../canonical/concepts/award.md
  - resource: ../canonical/concepts/outcome-declaration.md
  - resource: ../canonical/mechanisms/coverage.md
  - resource: ../canonical/mechanisms/aggregate.md
  - resource: ../canonical/mechanisms/rank.md
  - resource: ../canonical/mechanisms/readiness.md
  - resource: ../canonical/policies/evaluation-policy.md
  - resource: ../canonical/policies/awards-finalization.md
  - resource: ../canonical/policies/operational-exception-governance.md
  - resource: ../canonical/synchronizations/evaluation-outcome-finalization-declaration.md
  - resource: ../canonical/experience/reconciliation-derived-state.md
  - resource: ../canonical/experience/outcome-officiality.md
  - resource: ../canonical/invariants/missing-never-zero.md
  - resource: ../canonical/invariants/calculated-not-official.md
  - resource: ../canonical/invariants/official-not-automatically-public.md
---

# Purpose

Audit whether MUDAC can move from current eligible evaluation evidence to a recognized and explicitly official competition outcome without allowing a derived mechanism, exception, lifecycle transition or recalculation to silently acquire authority owned elsewhere.

The authority ladder under audit is:

```text
current eligible authoritative Scorecards
  → factual Coverage
  + Aggregate
  → rank eligibility / Ranking Readiness
  → Rank
  → optional Award recognition
  → Finalization Readiness
  → coordinated Competition Finalization
  + explicit Outcome Declaration
```

Preserve throughout:

```text
calculated
  != sufficient
  != ranking ready
  != recognized
  != Competition Finalized
  != official
  != public
```

015-F dispositions DIR-026 through DIR-034.

# Decision

**015-F COMPLETE — PASS. Proceed to 015-G.**

```text
DIR-026 through DIR-034                 DISPOSITIONED
confirmed integrity violation           NONE
INT-F corrective finding opened         NONE
upstream semantic reopen                NONE
canonical semantic repair               NONE
purpose-preserved explicit limitations  3
cross-cluster rechecks retained         DIR-026 / 034
NEXT                                    015-G
```

The three explicit limitations are:

1. Aggregate/Rank may be calculable while factual Coverage is Incomplete or Ranking Readiness is false, provided consequential use preserves those distinctions;
2. a governed exception may permit a specific downstream consequence while Coverage truth remains Incomplete;
3. an Affected Outcome Declaration remains the latest declared official authority until explicit successor confirmation, even when corrected derived state already exists or visible winner values are unchanged.

# 1. Purpose obligations exercised

015-F principally exercises:

- **P-02 — Fair and bias-aware Team treatment**;
- **P-04 — Live operational coordination and completion**;
- **P-06 — Trustworthy and explainable outcome formation**;
- **P-07 — Correctable authority and historical truth**;
- **P-09 — Faithful external representation and controlled release**, insofar as official authority must be settled before externalization.

Primary invariants:

```text
INV-003 Missing Is Never Zero
INV-005 Current vs Historical Truth
INV-006 Calculated Is Not Declared Official
INV-007 Official Is Not Automatically Public
INV-010 Truthful Authority Under Uncertainty
```

Material tensions include:

```text
T-05 speed vs outcome correctness
T-06 exception handling vs consistent Team treatment
T-07 correctability vs immutability
T-10 transparency vs controlled disclosure/currentness
```

# 2. Outcome model under audit

Current MUDAC outcome formation intentionally preserves distinct ownership:

```text
Scorecard / Occurrence / Obligation / Rubric
  → current evidence eligibility facts

Coverage
  → factual sufficiency

Aggregate
  → numeric derivation over eligible evidence

Rank
  → ordering over a supplied rank-eligible Team set

Readiness
  → whether a consequential operation may legitimately proceed

Award
  → explicit recognition

Competition
  → lifecycle Finalization

Outcome Declaration
  → explicit official outcome authority/currentness/history

Export / Publication
  → later representation/release
```

No owner above may substitute for another.

# 3. Counterexample set

## F-P01 — Aggregate exists with missing evaluation evidence

Attempt:

> Because a numeric Aggregate exists, Coverage should be treated as Satisfied and the Team should be rank eligible.

Rejected.

Aggregate may be numerically computable over eligible evidence while factual Coverage remains Incomplete.

## F-P02 — Coverage exception is accepted

Attempt:

> Rewrite Coverage from Incomplete to Satisfied so downstream logic is easier.

Rejected.

```text
Coverage = Incomplete
Exception = Accepted for ranking
```

may both be true.

The exception changes a permitted consequence only where policy explicitly allows it.

## F-P03 — Rank can be calculated

Attempt:

> A calculated Rank is enough to confer a derived Award.

Rejected.

A rank-derived Award requires a current **Ranking Ready** supplied basis and explicit Award conferral.

## F-P04 — Rank changes after Award conferral

Attempt:

> Move the Award automatically to the new top-ranked Team.

Rejected.

Rank recalculation creates review/correction pressure only. Award authority changes through explicit Award actions.

## F-P05 — Award basis changes after official closeout

Attempt:

> Edit the existing Outcome Declaration so it matches corrected Award state.

Rejected.

The current immutable declaration becomes Affected when materially dependent on the changed Award/source basis.

## F-P06 — Current evidence is corrected after Finalization

Attempt:

> Roll Competition back from Finalized so new results can become official.

Rejected.

Competition remains Finalized. Derived state can recompute and Outcome Declaration may become Affected.

## F-P07 — Corrected ranking yields the same visible winner

Attempt:

> Leave the old declaration Current because the visible winner did not change.

Rejected when the immutable declared basis was materially affected.

```text
same visible result
  != same declared basis
```

Explicit successor confirmation is still required.

## F-P08 — Finalization Readiness becomes true

Attempt:

> Automatically Finalize Competition and mark current results official.

Rejected.

Readiness only makes the coordinated authority action legitimately available.

## F-P09 — Competition becomes Finalized

Attempt:

> Treat Finalized lifecycle state itself as official-result authority.

Rejected.

Ordinary MUDAC closeout coordinates Finalization with an Outcome Declaration, but the owners remain distinct.

# 4. DIR-026 — evidence eligibility change → Coverage / Aggregate / Rank

**Disposition: NO INTEGRITY VIOLATION; 015-H PROPAGATION/AUTOMATION RECHECK RETAINED.**

015-E established that source evidence may become ineligible without erasing historical Scorecard or obligation truth.

015-F confirms the downstream currentness consequence:

```text
eligible evidence changes
  → prior Coverage/Aggregate/Rank basis is non-current/affected
  → recompute against current authoritative basis
```

Derived state is basis-relative.

Recomputation:

- does not mutate the Scorecard/Occurrence/Obligation source;
- does not treat prior results as still current merely because they were once calculated;
- may retain prior basis/result for historical explanation;
- does not automatically create an Award or official declaration.

This preserves P-06 and P-07.

015-H must recheck that system-triggered propagation does not cross from deterministic affectedness/recomputation into discretionary Award/successor authority.

# 5. DIR-027 — exception disposition → Coverage

**Disposition: PURPOSE PRESERVED WITH EXPLICIT FACT/CONSEQUENCE LIMITATION.**

Coverage answers factual sufficiency only.

```text
Coverage = Incomplete
Exception = Accepted for a stated consequence
```

is legitimate.

An exception may permit, for example:

- ranking despite preserved shortfall;
- closeout under an explicitly allowed policy condition;

but only within its declared scope.

It does not:

- fabricate evidence;
- convert missing evidence to zero;
- mutate an obligation;
- make Coverage read Satisfied;
- waive Rubric/basis compatibility;
- grant Award or declaring authority;
- silently authorize unrelated consequences.

This limitation is necessary to preserve both factual truth and operational flexibility.

# 6. DIR-028 — missing obligation/evidence → Aggregate / Rank

**Disposition: NO INTEGRITY VIOLATION.**

Missing remains missing.

```text
missing evaluation
  != Judge score of zero
```

Aggregate consumes only current eligible authoritative Scorecards according to Evaluation Policy.

A numeric Aggregate may exist over the available eligible evidence while Coverage remains Incomplete.

Rank consumes only the supplied **rank-eligible** Team set.

Thus:

```text
Aggregate exists
  != Coverage Satisfied
  != Team rank eligible
  != Ranking Ready
```

If policy allows an explicit exception, eligibility changes through that policy decision while the underlying shortfall remains visible.

No Team is silently penalized by converting absence into zero.

# 7. DIR-029 — Rank → Award

**Disposition: NO INTEGRITY VIOLATION.**

Rank is derivation, not recognition.

For rank-derived recognition:

```text
current Rank
+ Ranking Ready
+ Award definition/rule
+ recipient/tie/cardinality consistency
+ legitimate Award authority
  → Award.confer
```

The system may identify the candidate implied by the rule, but:

```text
candidate
  != recognized recipient
```

Award owns the conferral.

Discretionary Awards remain explicitly discretionary; Rank visibility never converts them into derived recognition.

# 8. DIR-030 — Rank change → existing Award

**Disposition: NO INTEGRITY VIOLATION.**

A later Rank/source change does not silently transfer, revoke or rewrite recognition.

```text
Rank changes
  → Award basis consistency review

Award changes
  → explicit revoke / correctConferral / new conferral
```

Recognition history remains attributable.

A prior Award may remain historically true as an earlier conferral even when current correction requires explicit change.

Thus calculation currentness does not become recognition authority.

# 9. DIR-031 — Award correction → Outcome Declaration

**Disposition: NO INTEGRITY VIOLATION.**

Outcome Declaration may identify Award state in its immutable supplied OutcomeBasis, but it does not own Award history.

Award correction therefore does not edit a declaration.

If the current declaration materially depends on the changed recognition basis:

```text
Award correction
  → declaration dependency review
  → current declaration identifyAffected
```

The declaration content remains unchanged.

Later corrected officiality uses explicit successor confirmation.

This preserves Award and Outcome Declaration as independent owners.

# 10. DIR-032 — evidence/policy correction → Outcome Declaration

**Disposition: PURPOSE PRESERVED WITH EXPLICIT AFFECTED-AUTHORITY LIMITATION.**

When a material dependency of the current declaration changes:

```text
current Outcome Declaration
  → Affected
```

Affected means:

> latest explicitly declared official authority known to require correction/review.

It does **not** mean:

- silently unofficial;
- silently Superseded;
- replaced by the latest calculation;
- erased from history.

Corrected evidence/Aggregate/Rank/Award state may exist before corrected official authority does.

```text
latest calculation
  != latest declared authority
```

After reconciliation:

```text
Affected declaration
+ corrected accepted OutcomeBasis
+ declaring authority
  → explicit successor Current
  → predecessor Superseded
```

This limitation preserves both explicit official authority and correctability.

# 11. DIR-033 — Competition Finalization → Outcome Declaration

**Disposition: NO INTEGRITY VIOLATION.**

Competition Finalization owns lifecycle closure.

Outcome Declaration owns official content/currentness/history.

Ordinary MUDAC closeout coordinates both:

```text
Competition.finalize
+
OutcomeDeclaration.declare
```

Semantic closeout success requires:

```text
Competition = Finalized
AND
Outcome Declaration = Current
```

The coordinated action does not merge the Concepts.

Especially:

```text
Competition Finalized
  != official content authority
```

After later source correction:

```text
Competition remains Finalized

Outcome Declaration
  may become Affected
  may later receive explicit successor
```

Official correction therefore does not reopen Competition lifecycle.

# 12. DIR-034 — readiness/calculation → officiality

**Disposition: NO INTEGRITY VIOLATION; 015-I MAPPING RECHECK RETAINED.**

Ranking Readiness and Finalization Readiness are derived projections.

```text
Ranking Ready
  != Award conferred

Finalization Ready
  != Competition Finalized
  != Outcome Declaration exists
```

They may make consequential actions available but cannot perform them.

The closeout action revalidates current authoritative/reconciled basis rather than trusting a stale previously rendered readiness value.

Thus Readiness remains explanation/permission-to-proceed evidence rather than authority.

015-I must confirm that combined user-visible mapping does not present a green/readiness state as recognized or official.

# 13. Derived currentness integrity

Coverage, Aggregate, Rank and Readiness remain derived and basis-relative.

When material source/policy input changes:

```text
old derived result
  → no longer ordinary-current
  → recompute

new derived result
  → current calculation
  != retrospective rewrite of old decision history
```

Derived state can be reconstructed for historical explanation where needed.

No generic user action edits:

- Coverage;
- Aggregate;
- Rank;
- Ranking Readiness;
- Finalization Readiness.

Correction targets the actual source or invokes a specifically governed exception.

# 14. Coverage / exception / rank-eligibility integrity

The cluster preserves three separate questions:

```text
1. Is qualifying evidence factually sufficient?
   → Coverage

2. Does policy permit proceeding despite a known shortfall?
   → governed exception disposition

3. Is this Team/scope eligible for consequential ranking use now?
   → application-derived rank eligibility / Ranking Readiness
```

These can produce:

```text
Coverage = Incomplete
Exception = Accepted for ranking
Ranking Ready = true
```

without contradiction.

The design remains honest because factual insufficiency is still visible and the exception scope is attributable.

# 15. Aggregate / Rank integrity

Aggregate has no sufficiency or authority semantics.

Rank has no eligibility, recognition or officiality semantics.

Preserve:

```text
Aggregate
  = numeric combination

Rank
  = policy-governed ordering of supplied eligible set

Award
  = recognition

Outcome Declaration
  = official authority
```

Tie behavior is supplied by declared Evaluation Policy. Hidden ordering, insertion order or display rounding cannot silently resolve policy-level ties.

# 16. Award integrity

Award's purpose remains explicit recognition.

## Rank-derived Award

SelectionBasis is supplied Rank only when Ranking Ready.

The derived rule constrains the recipient, but Award still owns conferral.

## Discretionary Award

Authorized human selection remains explicit.

It cannot be represented as mathematically implied merely because data are visible.

## Correction

Later source/Rank change may create review pressure but cannot silently move recognition.

This preserves recognition history and the distinction:

```text
calculated
  != recognized
```

# 17. Competition Finalization integrity

Competition remains a lifecycle Concept.

Finalization means ordinary competition operation is closed under current closeout conditions.

It does not mean:

- all historical facts can never be corrected;
- Outcome Declaration can never become Affected;
- Award history can never be corrected;
- results are public;
- Export/Publication exist.

Post-Finalization source correction therefore leaves Competition Finalized.

This preserves COMP-002 and prevents lifecycle rollback from becoming a generic correction mechanism.

# 18. Outcome Declaration integrity

Outcome Declaration remains explicit authority over an immutable accepted basis.

Currentness:

```text
Current
Affected
Superseded
```

Preserve:

```text
Affected
  != Superseded
```

An Affected declaration is intentionally an unusual state:

- still the latest declared official authority;
- known to rely materially on changed/invalid basis;
- awaiting corrected reconciliation and explicit successor confirmation.

The design therefore supports honest statements such as:

> The currently declared official outcome is affected and under correction; newer calculations are not yet official.

That is more truthful than either silently replacing the declaration or pretending the source correction does not matter.

# 19. Same-visible-result integrity

A source correction may leave winner/rank/Award values visually unchanged.

If the immutable declared basis was materially affected:

```text
same visible result
  != same declared basis
```

The predecessor remains Affected until explicit successor confirmation.

This prevents declaration authority from silently migrating to a new basis under the same visible labels.

# 20. Closeout composition integrity

Closeout Basis is composition data, not a Concept.

It may identify:

- Competition Event Completed;
- current Evaluation Policy;
- Coverage and exception dispositions;
- Ranking Ready scopes;
- Aggregate/Rank basis;
- tie/policy decisions;
- required Award state;
- correction/reconciliation blockers;
- exact intended OutcomeBasis.

Finalization Readiness derives whether these are sufficiently resolved.

Then the explicit closeout action performs the owner-specific authority transitions.

```text
derived readiness
  → action availability

explicit authority action
  → Competition Finalized
  + Outcome Declaration Current
```

No hidden checklist completion writes authority.

# 21. Correction-after-closeout integrity

The full correction chain preserves independent ownership:

```text
source correction / invalidation
  → eligible evidence review
  → Coverage/Aggregate/Rank recompute as needed
  → Award consistency review
  → explicit Award correction if needed
  → Outcome Declaration Affected if material dependency changed
  → explicit successor declaration after reconciliation
```

Competition stays Finalized.

This chain does not automatically:

- create successor Judge work;
- move Award;
- create successor declaration;
- publish corrected results.

015-H will recheck automation boundaries across the complete chain.

# 22. Subject-purpose integrity summary

| Subject/mechanism | Integrity result |
| --- | --- |
| Coverage | Purpose preserved with explicit factual-vs-exception limitation |
| Aggregate | Purpose preserved; calculation never implies sufficiency/eligibility |
| Rank | Purpose preserved; ordering never owns eligibility/recognition/officiality |
| Ranking Readiness | Purpose preserved; derived permission/explanation only |
| Finalization Readiness | Purpose preserved; does not perform closeout |
| Award | Purpose preserved; explicit recognition remains independently owned |
| Competition | Purpose preserved; Finalization remains lifecycle closure |
| Outcome Declaration | Purpose preserved with explicit Affected-authority limitation |

# 23. Material finding result

015-F opens no corrective INT-F finding.

```text
INT-F corrective findings opened in 015-F = 0
```

Reason:

- evidence currentness propagates into derived state without rewriting source truth;
- Coverage fact and exception consequence remain separate;
- missing is never zero;
- Rank cannot confer recognition;
- recalculation cannot move an Award;
- Award correction cannot edit declaration history;
- source correction cannot silently replace official authority;
- Competition Finalization and Outcome Declaration remain independently owned;
- Readiness cannot become lifecycle/recognition/declaration authority.

# 24. Cross-cluster carry/recheck

These remain later **rechecks, not unresolved Cluster-D defects**:

- **DIR-026** → 015-H: system-triggered derived/currentness propagation must stop before discretionary Award/successor authority;
- **DIR-034** → 015-I: combined mapping must not visually promote calculated/readiness state into recognition/officiality;
- Award/Declaration correction chain → 015-H under DIR-044;
- Outcome Declaration → Export/Publication consequences → 015-G.

015-G begins from the now-verified boundary:

```text
official authority
  != representation
  != release
  != delivery
```

# 25. Implementation boundary

015-F does not prescribe:

- recalculation jobs;
- materialized views;
- cache invalidation;
- transaction boundaries;
- distributed closeout orchestration;
- job queues;
- locking;
- retry policies;
- award workflow screens;
- publication pipelines;
- executable consistency tests.

```text
derived currentness
  != cache design

coordinated closeout
  != transaction design

system-triggered affectedness
  != event-bus architecture

explicit authority
  != middleware role check
```

# Exit

**015-F COMPLETE — PASS.**

No semantic correction or upstream reopen is required.

Proceed to **015-G — Export, Publication, Disclosure, Currency, Withdrawal & External-Possession Integrity**.
