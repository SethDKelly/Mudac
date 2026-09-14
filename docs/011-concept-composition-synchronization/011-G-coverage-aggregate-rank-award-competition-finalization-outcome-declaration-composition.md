---
type: Concept Composition Revalidation
title: 011-G — Coverage, Aggregate, Rank, Award, Competition Finalization & Outcome Declaration Composition
description: "Establishes current MUDAC composition for eligible authoritative evidence, factual Coverage, Aggregate/Rank derivation and currency, Award selection/conferral, coordinated Competition Finalization and explicit Outcome Declaration authority, including post-finalization affected/successor semantics."
status: stable
tags: [phase-011, composition, coverage, aggregate, rank, award, finalization, outcome-declaration, authority]
sources:
  - resource: 011-A-composition-scope-evidence-reuse-synchronization-risk-subphase-planning.md
  - resource: 011-B-legacy-synchronization-inventory-composition-obligation-map-application-action-baseline.md
  - resource: 011-E-evaluation-basis-scorecard-authority-versioning-provenance-paper-capture-composition.md
  - resource: 011-F-temporal-correction-invalidation-replacement-successor-work-affected-state-propagation.md
  - resource: ../canonical/concepts/competition.md
  - resource: ../canonical/concepts/award.md
  - resource: ../canonical/concepts/outcome-declaration.md
  - resource: ../canonical/mechanisms/coverage.md
  - resource: ../canonical/mechanisms/aggregate.md
  - resource: ../canonical/mechanisms/rank.md
  - resource: ../canonical/policies/evaluation-policy.md
  - resource: ../canonical/policies/awards-finalization.md
  - resource: ../canonical/policies/operational-exception-governance.md
  - resource: ../canonical/invariants/missing-never-zero.md
  - resource: ../canonical/invariants/calculated-not-official.md
  - resource: ../canonical/invariants/official-not-automatically-public.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/005/composition-synchronization-contract.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T13:55:00-05:00 }
---

# Purpose

Establish how MUDAC turns currently eligible authoritative evaluation evidence into factual sufficiency, calculated outcomes, recognized Awards, lifecycle closeout and explicit official outcome authority without collapsing any of those meanings into one another.

011-G consumes the authority and temporal semantics established by 011-C through 011-F. In particular:

- historical Evaluation Obligation satisfaction is distinct from current evidence eligibility;
- one logical Scorecard has at most one current eligible authoritative Version;
- invalidated occurrences/evidence remain reconstructible but may be ineligible for current calculations;
- successor evaluation work never reopens a terminal predecessor obligation;
- source correction may make derived/declaration state non-current without rewriting historical authority;
- Competition Finalization remains separate from Outcome Declaration authority.

011-G answers:

1. Which Scorecard evidence qualifies for current Coverage/Aggregate/Rank input?
2. How do Coverage facts remain distinct from governed exception disposition?
3. When may Aggregate exist even though Coverage is Incomplete, and when may Rank legitimately consume an Aggregate?
4. How is calculated currentness tracked without turning Coverage/Aggregate/Rank into authority-owning Concepts?
5. How do rank-derived and discretionary Awards consume supplied selection basis while Award remains the conferral owner?
6. What exact closeout basis is required before MUDAC may Finalize a Competition?
7. How do `Competition.finalize` and `OutcomeDeclaration.declare` coordinate without merging lifecycle and declaration authority?
8. What happens after post-Finalization source correction changes Coverage/Aggregate/Rank/Award basis?
9. How does an Affected Outcome Declaration remain official until an explicit successor is confirmed?

# Decision summary

**PASS — 011-G is complete.**

No new `Result`, `Standing`, `Official Result`, `Finalization`, `Ranking`, `Coverage Status`, `Outcome Snapshot`, `Winner`, or workflow Concept is required.

The existing Concept/mechanism set is sufficient when composition preserves the following rules:

1. **Current eligible evaluation evidence is narrower than historical satisfaction.** A Scorecard can remain authentic historical evidence while being ineligible for current outcome calculation.
2. **Coverage is factual.** A governed exception may permit a downstream consequence while Coverage remains `Incomplete`.
3. **Aggregate is calculable from eligible evidence and does not imply Coverage satisfaction or rank eligibility.**
4. **Rank is derived only from the supplied rank-eligible Team set, current Aggregate basis, Division scope and Evaluation Policy.** It is never edited directly.
5. **Calculated currentness is basis-relative.** If an eligible input/policy basis changes, prior Coverage/Aggregate/Rank cannot masquerade as current; recomputation yields a new current derived result while preserving the prior basis for explanation.
6. **Award owns recognition.** Rank-derived Awards must be consistent with a current supplied Rank basis; discretionary Awards remain explicit authorized human decisions.
7. **Rank recalculation never silently moves an Award.** Existing conferral/revocation/correction history remains Award-owned and changes only through explicit Award actions.
8. **Ordinary MUDAC official closeout is one coordinated application action:** establish a valid closeout basis, `Competition.finalize`, and `OutcomeDeclaration.declare`. Semantic success requires both lifecycle Finalized and an explicit current Outcome Declaration over the exact accepted basis.
9. **Competition Finalization does not own declared-result content/history.** Outcome Declaration does not own Competition lifecycle.
10. **Calculated != official != public.** Outcome Declaration establishes official authority; Export/Publication remain 011-H.
11. **Post-Finalization correction does not roll Competition backward.** Derived results may recompute, Awards may require explicit review/correction, and the existing Outcome Declaration may become `Affected`.
12. **Affected remains official-but-known-affected.** A newer calculation does not become official until `OutcomeDeclaration.confirmSuccessor` explicitly establishes a successor declaration.

Durable current composition is promoted to [Evaluation Outcome, Award, Finalization & Declaration Composition](../canonical/synchronizations/evaluation-outcome-finalization-declaration.md).

# Scope ownership

011-G closes:

- legacy synchronization 11 — authoritative eligible evidence → Coverage/Aggregate/Rank;
- legacy synchronization 13 — Rank selection basis → rank-derived Award conferral;
- legacy synchronization 14 — Competition Finalization + explicit Outcome Declaration;
- legacy synchronization 09's derived-refresh residue;
- legacy synchronization 12's Coverage/Aggregate/Rank/Award/Outcome Declaration affectedness consequences;
- CO-09 and CO-10;
- CG-05, CG-06 and CG-09;
- 011-B provisional action-surface decisions for Competition `finalize`, Award consequential actions and Outcome Declaration actions.

011-G does **not** close:

- Export generation/currentness or Publication release — 011-H;
- final whole-application chaining/cycle/automation/action-surface audit — 011-I;
- Phase 012 inclusion/dependence questions;
- Phase 013 user interaction/presentation mapping;
- runtime recomputation, transactions, jobs, caches, materialized views or event propagation.

# 1. Eligible authoritative evaluation evidence

A Scorecard contributes to current outcome derivation only when its supplied evaluation evidence is currently eligible under all material current basis facts.

At minimum, current eligibility requires:

- one authoritative current eligible Scorecard Version exists for the logical Scorecard;
- the Scorecard is structurally bound to the intended Evaluator, Subject, Evaluation Occurrence and exact Evaluation Basis;
- the associated Evaluation Obligation is historically Satisfied by that logical Scorecard;
- the Evaluation Occurrence remains eligible for current evaluative use;
- the bound Rubric/Evaluation Basis remains eligible for this historical/current use under governing policy;
- no current evidence invalidation or correction state makes the Scorecard ineligible;
- the evidence is applicable to the supplied Competition/Division/outcome scope.

This is a derived eligibility determination over supplied owner state. It does not create an `Evidence Eligibility` Concept or mutate the Scorecard/Occurrence/Obligation.

Historical truth remains separately inspectable when one of these conditions later fails.

# 2. Coverage remains factual

Coverage consumes:

- the actual set of currently eligible authoritative evidence;
- the applicable evaluation-requirement basis;
- declared thresholds/composition requirements/exclusions.

It returns reconstructible factual sufficiency.

```text
Coverage = Satisfied | Incomplete
```

A governed exception may separately say that a later consequence is permitted despite `Incomplete` Coverage.

Example:

```text
Coverage factual sufficiency = Incomplete
Exception disposition        = Accepted for ranking/finalization
```

Both truths must remain visible.

The exception:

- does not fabricate a Scorecard;
- does not change an Outstanding/Cancelled/Excused/Satisfied obligation;
- does not convert missing evidence to zero;
- does not rewrite Coverage to Satisfied;
- does not silently waive a different policy condition.

# 3. Aggregate derivation

Aggregate uses the current set of eligible authoritative Scorecards and current Evaluation Policy.

The baseline remains one equal unit of weight per eligible individual Judge Scorecard. Panel/occurrence means remain analytical views unless policy explicitly supplies another legitimate aggregation rule.

Aggregate may be numerically calculable while Coverage is `Incomplete`.

Therefore:

```text
Aggregate exists
  != Coverage Satisfied
  != rank eligible
  != official result
```

Missing evidence is excluded as missing, never imputed as zero.

# 4. Rank eligibility and Rank derivation

Rank consumes a **supplied rank-eligible Team set** rather than deciding eligibility by itself.

MUDAC derives rank eligibility from current composition facts including:

- factual Coverage for the Team;
- any authorized exception disposition that explicitly permits ranking despite factual incompleteness;
- current Aggregate availability/basis;
- current Division membership/scope relevant to the result;
- applicable Evaluation Policy;
- other declared exclusion/disqualification conditions owned by policy/domain authority.

A Team with `Coverage=Incomplete` may be rank-eligible only when an explicit governing exception says that consequence is permitted. Rank never changes the Coverage fact.

Rank then orders the supplied rank-eligible Teams using current Aggregate values, Division scope and declared comparison/tie policy.

No direct `setRank`, `editRank`, manual tie breaking by hidden order, or rank-as-authority action is introduced.

# 5. Derived currentness

Coverage, Aggregate and Rank remain derived mechanisms, but the application must not present an old derivation as current after a material basis change.

The currentness contract is:

1. every material derived result is explainable from an identified source/policy basis;
2. a source/policy change that affects that basis makes the prior derived result non-current/affected for ordinary current use;
3. recomputation derives a new current result from the new basis;
4. prior derived results may remain reconstructible for historical explanation;
5. no derived result mutates its source Concepts.

This is conceptual currency, not a cache invalidation or recompute-job design.

# 6. Rank-derived Award composition

Application action: **Confer Rank-Derived Award**.

Participants:

- current Rank result supplied as SelectionBasis;
- `Award.confer`.

Conditions include:

- Award definition is current and available for the Competition scope;
- Award selection method is `Derived` and declares a rule compatible with the supplied Rank basis;
- relevant Rank is current under its identified basis;
- recipient is rank-eligible and consistent with the Award rule;
- tie/recipient-cardinality policy is satisfied;
- actor has legitimate Award-conferral authority.

Postconditions:

- Award owns an attributable conferral;
- the supplied Rank basis remains independently explainable;
- no Rank state is changed by the conferral.

A recalculated Rank that yields a different candidate does **not** silently transfer the existing Award. The Award becomes a review/correction concern and changes only through explicit `revoke`, `correctConferral`, or another legitimate Award action.

# 7. Discretionary Award composition

Application action: **Confer Discretionary Award**.

Participants:

- authorized human selection basis/reason;
- `Award.confer`.

Conditions:

- Award definition explicitly permits discretionary selection;
- supplied recipient is eligible under the Award definition;
- authorized actor deliberately chooses the recipient;
- any required rationale/source is attributable.

The application must not label the result as rank-derived merely because Rank information was visible to the decision maker.

# 8. Award correction and currentness

Award is authority-owning state, not a derived projection.

Source correction can therefore produce one of these outcomes:

- Award remains valid because its supplied selection basis/rule is unaffected;
- Award requires review because its basis became affected;
- a rank-derived Award is demonstrably inconsistent with the corrected current Rank and requires explicit Award correction/revocation;
- a discretionary Award may remain valid even if Rank changes, unless its own declared eligibility/selection basis was affected.

No source correction automatically revokes, reassigns or reconfers an Award.

# 9. Finalization readiness / closeout basis

MUDAC may attempt ordinary official closeout only when an explicit **Closeout Basis** can be assembled from current authoritative/derived facts.

Closeout Basis is composition data, not a new Concept.

It must identify, as applicable:

- Competition identity and lifecycle at `Event Completed`;
- applicable Evaluation Policy/basis;
- current Coverage for required scope plus any governed exception dispositions;
- current Aggregate/Rank basis for required ranked outcomes;
- explicit tie resolution or policy result where required;
- required Award decisions/conferrals and their current consistency;
- unresolved correction/reconciliation items that policy says block closeout;
- the exact accepted outcome basis intended for declaration.

A closeout exception may permit a specific incomplete factual condition, but the exception must remain separately attributable and cannot convert the underlying fact to success.

# 10. Coordinated official closeout

Application action: **Finalize Competition & Declare Outcome**.

Participants:

- `Competition.finalize`;
- `OutcomeDeclaration.declare`.

Conditions:

- Competition is in `Event Completed`;
- current Access/authority permits final closeout;
- Closeout Basis satisfies the applicable Awards & Finalization Policy;
- no unresolved condition that policy treats as blocking remains;
- the OutcomeBasis supplied to `declare` identifies the exact accepted evidence/policy/Coverage/Rank/Award basis strongly enough for later reconstruction;
- no current initial Outcome Declaration already exists for the same closeout scope.

Semantic success requires both:

```text
Competition.state = Finalized
AND
one explicit current Outcome Declaration exists over the accepted OutcomeBasis
```

The composition does **not** imply one database transaction or runtime atomic commit. It establishes the semantic condition MUDAC may represent as successful official closeout.

If the application cannot establish whether both postconditions hold, it must not present closeout as unambiguously successful until state is reconciled conceptually.

# 11. Why Finalization and Declaration remain separate owners

Competition Finalization means the competition occurrence's ordinary lifecycle is closed.

Outcome Declaration means an authorized actor explicitly established official result authority over one immutable supplied OutcomeBasis.

Therefore:

```text
Competition Finalized
  != Outcome Declaration content/history

Outcome Declaration exists
  != Competition lifecycle owner
```

Current MUDAC coordinates them for ordinary official closeout because that product behavior avoids a misleading `Finalized but no declared result` ordinary state. Phase 012 still owns whether every coherent product variant containing Competition Finalization must include Outcome Declaration.

# 12. Calculated does not mean official

At any time before Outcome Declaration:

- Coverage may be current;
- Aggregate may be current;
- Rank may be current;
- Award selections/conferrals may exist;

without those facts by themselves constituting the declared official outcome.

Only Outcome Declaration establishes official result authority.

# 13. Official does not mean public

An Outcome Declaration may be current official authority without being externally released.

Export and Publication remain distinct concepts and 011-H owns their composition.

011-G therefore never synchronizes declaration establishment directly into automatic publication.

# 14. Post-Finalization source correction

011-F already establishes that Competition remains Finalized after legitimate source correction.

011-G adds the outcome consequences:

1. affected eligible evidence/Coverage/Aggregate/Rank is recomputed or re-derived under the corrected basis;
2. Award basis is reviewed; Award authority changes only through explicit Award actions;
3. if the current Outcome Declaration depended materially on the changed basis, application composition invokes `OutcomeDeclaration.identifyAffected`;
4. the Affected declaration remains the latest declared official authority;
5. corrected calculations/Awards do not silently establish a new official outcome;
6. after reconciliation, authorized successor declaration may be explicitly confirmed.

# 15. Marking a declaration Affected

Application reaction: **Identify Official Outcome Affected**.

Participant:

- `OutcomeDeclaration.identifyAffected`.

Conditions:

- a current declaration exists;
- one or more material dependencies of its immutable OutcomeBasis have changed, become invalid/ineligible, or are now known not to support the declaration as originally accepted;
- the relationship is actual, not merely category-level similarity;
- the reason/basis is attributable.

Postconditions:

- declaration currentness becomes `Affected`;
- declaration content/history is unchanged;
- Competition remains Finalized;
- newer calculated state is not yet official by implication.

This reaction may follow source correction conceptually without requiring a separate user initiation, but the authority/reason for affectedness must remain explainable.

# 16. Successor official outcome

Application action: **Confirm Successor Outcome Declaration**.

Participant:

- `OutcomeDeclaration.confirmSuccessor`.

Conditions:

- current declaration is Affected;
- corrected source/derived/Award state has been reconciled sufficiently for a new accepted OutcomeBasis;
- governing closeout/exception rules for successor declaration are satisfied;
- authorized declaring authority explicitly confirms the corrected basis.

Postconditions:

- new declaration becomes `Current` official authority;
- predecessor becomes `Superseded` historical authority;
- predecessor and correction path remain reconstructible;
- Competition remains Finalized;
- no Publication/Export state changes automatically.

Successor confirmation is not an implicit side effect of recomputation.

# 17. Action-surface decisions

| Action family | Current MUDAC status after 011-G |
| --- | --- |
| Coverage/Aggregate/Rank derivation/recompute | system/application derived behavior; no direct write action |
| governed Coverage exception disposition | controlled policy/authority action; never Coverage mutation |
| Award `define` / `updateDefinition` / unused retirement | direct administrative Award actions |
| Confer Rank-Derived Award | coordinated high-consequence application action |
| Confer Discretionary Award | controlled direct/coordinated Award action |
| Award `revoke` / `correctConferral` | controlled high-consequence Award actions |
| generic manual Rank edit | intentionally unavailable |
| Competition `finalize` | composition-only within ordinary `Finalize Competition & Declare Outcome` closeout |
| OutcomeDeclaration `declare` | composition-only within ordinary initial closeout |
| OutcomeDeclaration `identifyAffected` | system-triggered/composition reaction after verified dependency affectedness |
| OutcomeDeclaration `confirmSuccessor` | controlled high-consequence explicit declaration action |
| automatic publication after declaration | intentionally unavailable; 011-H owns release |

011-I will perform final whole-application exposure closure.

# 18. Over-synchronization checks

011-G rejects:

- changing Coverage to `Satisfied` because an exception was accepted;
- preventing Aggregate calculation merely because Coverage is Incomplete;
- automatically making every Team with an Aggregate rank-eligible;
- letting Rank own tie-resolution authority beyond declared policy;
- automatically conferring or moving Awards when Rank changes;
- treating a discretionary Award as mathematically derived;
- making `Competition.finalize` intrinsically create Outcome Declaration state;
- making Outcome Declaration an intrinsic field of Competition;
- making current Rank automatically official;
- making official Outcome automatically public;
- automatically confirming a successor declaration after recomputation;
- rolling Competition backward after post-Finalization correction.

# 19. Under-synchronization checks

011-G requires explicit handling for:

- evidence that is historically valid but currently ineligible;
- factual Coverage and exception disposition as simultaneous independent truths;
- Aggregate basis/currentness after evidence correction;
- Rank eligibility before ordering;
- tie behavior before rank-derived Award/finalization consequences;
- Award consistency at closeout;
- explicit declaration authority at ordinary finalization;
- declaration affectedness after material source correction;
- explicit successor declaration after corrected reconciliation.

# 20. Chaining and cycle pressure test

Representative chains remain directional:

```text
current eligible Scorecards
  → Coverage + Aggregate
  → rank-eligibility decision
  → Rank
  → optional rank-derived Award conferral
```

```text
Event Completed + reconciled closeout basis
  → Finalize Competition & Declare Outcome
  → Competition Finalized
  + current Outcome Declaration
```

```text
source/evidence correction
  → derived basis non-current
  → recompute Coverage/Aggregate/Rank
  → explicit Award review/correction if required
  → current Outcome Declaration identifyAffected
  → explicit successor declaration when reconciled
```

No derived/output action writes backward into Scorecard, Evaluation Occurrence, Evaluation Obligation or Rubric authority. No semantic cycle or hidden Result/Finalization coordinator is required.

# 21. Upstream-boundary audit

011-G does not require reopening Phase 010 Concept boundaries.

Coverage, Aggregate and Rank remain derived mechanisms by design. Award already owns recognition definition/conferral history. Competition already owns lifecycle closure. Outcome Declaration already owns explicit official declaration/currentness/history.

The necessary behavior is application composition, not evidence for a new Concept.

# 22. Legacy-contract disposition after 011-G

Current Phase 011 authority now replaces/reframes:

- legacy 11 — current eligible evidence → Coverage/Aggregate/Rank;
- legacy 13 — Rank-derived selection basis → Award conferral;
- legacy 14 — replaced by coordinated Competition Finalization + Outcome Declaration;
- legacy 09's derived refresh residue;
- legacy 12's Coverage/Aggregate/Rank/Award/Outcome Declaration consequences.

Legacy 15 and Export/Publication consequences of legacy 12 remain 011-H.

# 23. Exit test

011-G passes because:

- current evidence eligibility is explicit and history-preserving;
- factual Coverage remains independent from governed exception disposition;
- Aggregate calculation is distinct from Coverage and ranking eligibility;
- Rank is derived from a supplied eligible set and declared policy;
- derived currentness responds to corrected basis without becoming domain authority;
- rank-derived/discretionary Award semantics preserve Award authority;
- Rank recalculation cannot silently move recognition;
- closeout basis is explicit without creating a Finalization Concept;
- ordinary MUDAC Finalization and initial Outcome Declaration coordinate while remaining independently owned;
- calculated, official and public meanings remain distinct;
- post-finalization correction preserves Competition Finalized and explicit declaration history;
- Affected declaration remains official until explicit successor confirmation;
- no hidden workflow/result coordinator or Phase 010 boundary repair is required;
- 011-H receives a clean official-outcome/currentness basis for Export/Publication composition.

# Decision

**PASS — 011-G is complete.**

# Handoff

Proceed to:

> **011-H — Export, Publication, Representation Currency & Release Composition**

011-H must consume the current Outcome Declaration and affected/successor semantics established through 011-F/G, then determine how Export binds source authority, becomes Current/Affected/Stale/Superseded/Retired, and how explicit Publication release/withdrawal/successor actions preserve historical public truth without generation implying publication or source correction silently retargeting a historical release.
