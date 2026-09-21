---
type: Experience Contract
title: Award, Finalization & Outcome Officiality Mapping
description: Current mapping for explicit Award recognition, coordinated Competition Finalization and initial Outcome Declaration, affected official authority and explicit successor declaration without conflating calculated, recognized, official, public or delivered state.
status: stable
tags: [experience, mapping, award, finalization, outcome-declaration, officiality, successor, phase-013]
sources:
  - resource: ../../013-concept-mapping-interaction-semantics-user-visible-representation/013-H-award-competition-finalization-outcome-declaration-officiality-successor-authority-mapping.md
  - resource: reconciliation-derived-state.md
  - resource: ../concepts/award.md
  - resource: ../concepts/competition.md
  - resource: ../concepts/outcome-declaration.md
  - resource: ../synchronizations/evaluation-outcome-finalization-declaration.md
  - resource: ../policies/awards-finalization.md
  - resource: ../invariants/calculated-not-official.md
  - resource: ../invariants/official-not-automatically-public.md
---

# Purpose

Define how MUDAC maps recognized Awards, Competition lifecycle closure and explicit official-result authority while preserving owner boundaries and honest successor history.

This owner stops before Export/Publication/distribution semantics, which belong to 013-I.

# Authority ladder

Preserve:

```text
calculated
  != ranking ready
  != recognized
  != Competition Finalized
  != official
  != public
  != delivered
```

Derived/reconciled state may permit consequential authority actions, but does not perform them.

# Award recognition

Award owns recognition.

A rank-derived Award consumes a current Ranking Ready SelectionBasis plus its declared scope/rule/eligibility/tie/cardinality semantics and legitimate conferral authority.

```text
Ranking Ready candidate/basis
  != conferred Award
```

The application may explain the candidate implied by a derived rule before conferral, but must not present that candidate as recognized until `Award.confer` succeeds.

A discretionary Award is an authorized human choice under a definition that permits discretion. It must not be portrayed as mathematically implied merely because Rank, Scorecards, Notes or other data are visible.

```text
rank-derived selection != discretionary selection
```

# Award correction

A later Rank/source change never silently moves recognition.

Where an existing conferral becomes inconsistent with current basis, the experience may identify review/correction pressure, but recognition changes only through explicit Award actions such as revoke, correct conferral or appropriate new conferral.

Award history remains attributable.

# Finalization Readiness

Finalization Readiness remains the derived projection established by 013-G.

```text
Finalization Readiness = true
  != Competition Finalized
  != Outcome Declaration exists
```

Readiness may make closeout available. The closeout action must revalidate current authoritative/reconciled basis rather than relying solely on a previously rendered readiness result.

# Closeout Basis

Ordinary closeout is based on a reconstructible current composition that may identify:

- Competition `Event Completed` state;
- current Evaluation Policy/basis;
- current Coverage and separate exception dispositions;
- Ranking Ready scopes and current Aggregate/Rank basis;
- tie/policy resolution;
- required/current Award decisions;
- unresolved correction/reconciliation blockers;
- exact intended OutcomeBasis.

This composed basis is explanatory/input data, not a new Concept.

# Finalize Competition & Declare Outcome

Ordinary MUDAC closeout is a coordinated application action:

```text
Competition.finalize
+
OutcomeDeclaration.declare
```

Semantic success requires:

```text
Competition = Finalized
AND
Outcome Declaration = Current
```

The owners remain distinct:

- Competition owns lifecycle closure;
- Outcome Declaration owns immutable declared OutcomeBasis, declaring authority, official currentness and declaration history.

Competition Finalization alone does not own official-result content.

# Consequence explanation

Before closeout commitment, the representation should make clear enough that:

- Competition lifecycle will become Finalized;
- the accepted OutcomeBasis will become explicit official authority;
- included Award recognition remains separately owned;
- later correction will not roll Competition lifecycle backward;
- officiality does not publish results.

No particular confirmation UI is prescribed.

# Official authority

Only explicit Outcome Declaration establishes official outcome authority.

```text
calculated Rank
  != Ranking Ready
  != Competition Finalized alone
  != official declaration
```

Do not restore `Official Outcome Revision`; that historical adapter is obsolete.

# Outcome Declaration currentness

User-visible declaration currentness is:

```text
Current
Affected
Superseded
```

`Current` means the currently declared official authority for the scope.

`Affected` means a material dependency of the immutable declared basis changed/became invalid or ineligible. An Affected declaration remains the latest explicitly declared official authority until an explicit successor is confirmed.

`Superseded` means an explicit successor declaration became current. The predecessor remains historical declared authority.

```text
Affected != Superseded
```

# Post-Finalization correction

Source correction after closeout preserves:

```text
Competition = Finalized
```

Current evidence/derived state may recompute. Award state may require explicit review/correction. If the current declared basis materially depended on changed source state, the Outcome Declaration becomes Affected.

New calculations do not become official automatically.

# Successor official authority

After corrected source/derived/Award state is reconciled, an authorized actor may explicitly confirm a successor Outcome Declaration.

```text
Affected declaration
  + corrected reconciled OutcomeBasis
  + successor closeout conditions
  + declaring authority
  → successor Current
  → predecessor Superseded
```

The successor has its own immutable basis/authority/time.

It does not re-finalize Competition.

# Same visible result, changed basis

A materially corrected declaration basis may still produce the same visible winner/rank/Award values.

```text
same visible result != same declared basis
```

If the predecessor was materially Affected, explicit successor confirmation is still required to establish official authority over the corrected basis.

# Award and Outcome Declaration remain separate

Outcome Declaration may identify current Award state in its supplied basis, but does not own Award semantics/history.

Award correction likewise does not edit an Outcome Declaration. If the declared basis is materially affected, use declaration affected/successor semantics.

# Official is not public

Preserve:

```text
Outcome Declaration exists
  != Export generated
  != Publication released
  != delivery
```

Competition Finalization also does not publish results.

Official-but-non-public is a legitimate PF-01 state/profile.

# Action availability

| Action | Ordinary semantic availability |
| --- | --- |
| Confer Rank-Derived Award | current Award definition + Ranking Ready basis + consistent recipient/tie/cardinality + authority |
| Confer Discretionary Award | Award permits discretionary selection + eligible recipient + authority |
| Revoke/Correct Award | current/history conferral + applicable correction authority/reason |
| Finalize Competition & Declare Outcome | Event Completed + reconciled/Finalization Ready closeout basis + declaring authority |
| Identify Official Outcome Affected | current declaration materially depends on changed/ineligible basis |
| Confirm Successor Outcome Declaration | current declaration Affected + corrected basis reconciled + successor authority |

Unavailable actions should explain their semantic blocker where that does not disclose protected information.

# Truthful authority feedback

Do not claim conferral, Finalization, declaration, affectedness or successor confirmation when the authoritative outcome is unknown.

The experience should distinguish pending/unknown, confirmed success and known rejection/failure as applicable. 013-J re-audits the cross-cutting feedback grammar.

# Privilege boundary

Technical/admin privilege does not create Award, Finalization or declaring authority.

Generic override cannot:

- contradict a rank-derived Award rule;
- manufacture discretionary recognition authority;
- bypass closeout blockers;
- mark calculated state official;
- clear an Affected declaration without explicit successor confirmation;
- publish results merely because they are official.

# 013-I boundary

This owner establishes internal officiality only.

013-I must preserve:

```text
Outcome Declaration != Export != Publication != delivery
successor declaration != automatic successor representation/release
Affected official basis != automatic Publication withdrawal
```


# Exceptional official outcome mapping

A policy-authorized **Exceptional Closeout Disposition** may support official closeout when no ordinary ranked result can legitimately exist for an identified scope.

The user-visible semantics must distinguish three materially different conditions:

```text
ordinary ranked result
  != official exceptional no-result outcome
  != unknown / unresolved result
```

An exceptional closeout representation should make clear enough that:

- the Competition is being Finalized;
- the preserved evidence/Coverage condition does not support an ordinary ranked result for the identified scope;
- the exceptional disposition is authorized and attributable;
- no winner, Rank, or rank-derived Award is being fabricated;
- the exceptional OutcomeBasis will become explicit official authority;
- unaffected result scopes or Awards, if any, remain separately identified;
- officiality still does not imply Publication.

A pending, uncertain, stale, or ambiguously confirmed result must never be shown as an official exceptional outcome. The application must first establish the policy-authorized exceptional disposition or resolve the ordinary outcome.

The existing **Finalize Competition & Declare Outcome** action therefore has two semantically valid closeout modes: ordinary resolved closeout and explicitly authorized exceptional no-result closeout. The experience may present these differently, but both preserve the same Competition/Outcome Declaration owner boundary.
