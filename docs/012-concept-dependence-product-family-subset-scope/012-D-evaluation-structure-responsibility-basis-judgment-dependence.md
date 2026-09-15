---
type: Phase Design Record
title: 012-D — Evaluation Structure, Responsibility, Basis & Judgment Dependence
description: "Resolves MUDAC application-family inclusion dependence for Evaluation Occurrence, Evaluation Obligation, Rubric, and Scorecard; preserves their Phase-010 independence; accepts the smallest shared-context/basis edges; rejects automatic Occurrence/Obligation/Scorecard co-inclusion; and records variant-specific composition implications for later scope selection."
status: stable
tags: [phase-012, jackson, dependence, evaluation, occurrence, obligation, rubric, scorecard, subsets]
sources:
  - resource: 012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md
  - resource: 012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md
  - resource: 012-C-competition-actor-competitor-context-bias-control-dependence.md
  - resource: ../canonical/dependence/application-family-dependence.md
  - resource: ../canonical/project/mandate-context.md
  - resource: ../canonical/project/purpose-needs-success-tensions.md
  - resource: ../canonical/concepts/evaluation-occurrence.md
  - resource: ../canonical/concepts/evaluation-obligation.md
  - resource: ../canonical/concepts/rubric.md
  - resource: ../canonical/concepts/scorecard.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/synchronizations/evaluation-basis-scorecard-authority.md
  - resource: ../canonical/policies/evaluation-policy.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/006/dependence-subset-contract.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-15T14:11:00-05:00 }
---

# Purpose

Resolve the Phase 012 application-family inclusion dependence of the four Concepts that own MUDAC evaluation structure, responsibility, basis semantics, and individual judgment:

- Evaluation Occurrence;
- Evaluation Obligation;
- Rubric;
- Scorecard.

This subgroup asks which of these Concepts require one another for a meaningful MUDAC application role and which only synchronize in the current full application.

The central pressure is to avoid turning the ordinary Phase-011 live-judging chain:

```text
Evaluation Occurrence begin
  → Evaluation Obligations
  → Scorecard work/finalization
```

into a false product-family dependency cycle.

# Decision summary

**PASS — evaluation-family dependence resolved without a co-inclusion cycle.**

012-D accepts nine direct edges:

```text
Evaluation Occurrence  → Team
Evaluation Occurrence  → Participation
Evaluation Occurrence  → Rubric

Evaluation Obligation  → Team
Evaluation Obligation  → Participation
Evaluation Obligation  → Rubric

Scorecard              → Team
Scorecard              → Participation
Scorecard              → Rubric
```

It accepts **no universal inclusion edge** among Evaluation Occurrence, Evaluation Obligation, and Scorecard themselves.

Therefore:

```text
Evaluation Occurrence ↛ Evaluation Obligation
Evaluation Obligation ↛ Evaluation Occurrence
Evaluation Occurrence ↛ Scorecard
Scorecard             ↛ Evaluation Occurrence
Evaluation Obligation ↛ Scorecard
Scorecard             ↛ Evaluation Obligation
```

Rubric has no new outgoing direct edge in this subgroup.

The full current MUDAC application may include and synchronize all four Concepts. That does not make all four an inseparable product-family bundle.

# 1. Incoming canonical dependence

012-C already establishes:

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

012-D uses these transitively.

Therefore an evaluation Concept that directly depends on Team and Participation already inherits:

```text
→ Competition
→ Identity
```

without redundant direct edges.

# 2. Evaluation-role decomposition

## 2.1 Evaluation Occurrence role

Evaluation Occurrence preserves bounded historical truth about one evaluation situation:

- subject;
- presented context;
- actual evaluators;
- evaluation basis;
- timing;
- validity/replacement history.

Its application value is historical contextual truth, not responsibility tracking or judgment storage.

## 2.2 Evaluation Obligation role

Evaluation Obligation preserves one evaluator's responsibility to produce one qualifying evaluation and the truthful lifecycle of that responsibility.

Its application value is assignment, remaining-work truth, excusal/cancellation/reassignment, and successor responsibility—not the judgment itself.

## 2.3 Rubric role

Rubric defines the structured evaluation instrument and response interpretation/validation semantics.

Its application value is basis semantics and reusable evaluation definition. It is not an event, responsibility, or judgment owner.

## 2.4 Scorecard role

Scorecard captures one evaluator's independent judgment for one subject under a supplied context and evaluation basis.

Its application value is judgment content, Draft-versus-authoritative judgment state, and judgment amendment/correction semantics—not assignment or occurrence history.

# 3. Shared MUDAC context dependencies

The three evaluation-work Concepts—Occurrence, Obligation, and Scorecard—share the same current MUDAC role anchors:

```text
Subject   = Team
Evaluator = Judge Participation
Basis     = Rubric-defined evaluation semantics
```

These role anchors justify direct contextual dependence.

# 4. Accepted Evaluation Occurrence edges

<a id="dep-d-001"></a>
## DEP-D-001 — Evaluation Occurrence → Team

```text
Evaluation Occurrence → Team
```

Within MUDAC, the occurrence exists to preserve what happened when a student Team was presented/evaluated.

A generic occurrence over another Subject type is imaginable elsewhere, but that is not the current application-family role.

This edge transitively provides Competition through `Team → Competition`.

<a id="dep-d-002"></a>
## DEP-D-002 — Evaluation Occurrence → Participation

```text
Evaluation Occurrence → Participation
```

MUDAC occurrence participants are event-scoped Judge Participations rather than permanent human identities.

This preserves the distinction between:

```text
who the human is
!=
who participated as a Judge in this Competition
```

The edge transitively provides Identity and Competition through current 012-C dependence.

<a id="dep-d-003"></a>
## DEP-D-003 — Evaluation Occurrence → Rubric

```text
Evaluation Occurrence → Rubric
```

A meaningful MUDAC evaluation occurrence is governed by declared evaluation criteria/basis semantics. Rubric is the current Concept that owns those semantics.

The Evaluation Occurrence Concept remains intrinsically generic over `BasisRef`; this is contextual MUDAC inclusion dependence, not a specification dependency.

An individual Prepared or Cancelled occurrence may not yet have a usable basis instance. That does not remove Rubric from the application capability subset in which Evaluation Occurrence serves its evaluation role.

# 5. Evaluation Occurrence non-edges

## 5.1 Evaluation Occurrence ↛ Evaluation Obligation

**Decision: reject universal edge.**

A plausible MUDAC subset can use Evaluation Occurrence to preserve bounded presentation/participant/history context without using formal responsibility tracking.

Examples include:

- occurrence-history capture where evaluation responsibility is managed externally;
- a lightweight judging variant in which evaluators may submit judgments without pre-established individual obligations;
- preserved occurrence context for an event that completes/cancels without qualifying individual judgment.

This does not change ordinary Phase-011 composition, where occurrence begin establishes obligations in the current full application.

It means only that the synchronization is not universal product-family inclusion dependence.

## 5.2 Evaluation Occurrence ↛ Scorecard

**Decision: reject universal edge.**

Occurrence context remains meaningful even when no judgment is captured by MUDAC.

A cancelled occurrence, unusable occurrence, presentation-history-only subset, or externally captured evaluation path can still justify occurrence history.

## 5.3 Evaluation Occurrence ↛ Panel

012-C already establishes Panel as optional reusable grouping. Evaluation Occurrence may use Panel candidates, but actual participant history does not require Panel inclusion.

## 5.4 Evaluation Occurrence ↛ Alias / Division

Alias and Division may contribute PresentedContext when the selected variant uses blinded identity and/or multiple cohorts.

Neither is universally required by Evaluation Occurrence.

# 6. Accepted Evaluation Obligation edges

<a id="dep-d-004"></a>
## DEP-D-004 — Evaluation Obligation → Team

```text
Evaluation Obligation → Team
```

Within MUDAC, the responsibility is to evaluate a student Team.

This transitively supplies Competition context.

<a id="dep-d-005"></a>
## DEP-D-005 — Evaluation Obligation → Participation

```text
Evaluation Obligation → Participation
```

The responsible evaluator is an event-scoped Judge Participation, not merely an Identity.

This transitively supplies Competition and Identity.

<a id="dep-d-006"></a>
## DEP-D-006 — Evaluation Obligation → Rubric

```text
Evaluation Obligation → Rubric
```

MUDAC responsibility is responsibility to produce an evaluation under declared evaluation semantics. Rubric owns the current structured evaluation basis.

The generic Concept remains parameterized by `Basis`; the contextual edge says that MUDAC's current basis role is supplied by Rubric.

# 7. Evaluation Obligation non-edges

## 7.1 Evaluation Obligation ↛ Evaluation Occurrence

**Decision: reject universal edge.**

`OccurrenceRef` is explicitly optional in the Concept, and a coherent MUDAC subset can assign evaluation responsibility outside a bounded shared occurrence.

Representative case:

```text
Organizer assigns a make-up / asynchronous / individually scheduled Team evaluation
  → one Judge Participation receives responsibility
  → subject + basis are known
  → no shared Evaluation Occurrence is required merely to justify the obligation
```

If such a variant is later adopted into scope, its application composition must preserve enough supplied context for truthful judgment and historical explanation.

## 7.2 Evaluation Obligation ↛ Scorecard

**Decision: reject universal edge.**

Responsibility tracking is useful before evidence exists and can remain useful in a limited coordination subset even if judgment capture occurs outside MUDAC.

Evaluation Obligation can therefore support:

- assignment/remaining-work tracking;
- no-show/excusal/cancellation;
- substitution/reassignment;
- externally referenced qualifying evidence where an adopted variant legitimately supplies it.

The current full application uses Scorecard as qualifying evidence, but that does not prove universal co-inclusion.

# 8. Accepted Scorecard edges

<a id="dep-d-007"></a>
## DEP-D-007 — Scorecard → Team

```text
Scorecard → Team
```

Within MUDAC, a Scorecard is one Judge's evaluation of one student Team.

This transitively supplies Competition.

<a id="dep-d-008"></a>
## DEP-D-008 — Scorecard → Participation

```text
Scorecard → Participation
```

MUDAC judgment authorship is attributable to an event-scoped Judge Participation.

This preserves:

```text
stable human Identity
!=
Competition Participation
!=
semantic Scorecard authorship
```

while giving the Scorecard a meaningful Judge-author role.

The edge transitively supplies Identity and Competition.

<a id="dep-d-009"></a>
## DEP-D-009 — Scorecard → Rubric

```text
Scorecard → Rubric
```

MUDAC Scorecard responses derive their interpretation, validity, completeness, and scoring semantics from the declared Rubric basis.

A Scorecard without Rubric in this application family would require another owner of evaluation semantics; none exists in the current Concept model.

# 9. Scorecard non-edges

## 9.1 Scorecard ↛ Evaluation Obligation

**Decision: reject universal edge.**

A plausible lightweight MUDAC evaluation-capture subset can allow an eligible Judge Participation to record one independent Team judgment under a Rubric without representing formal assigned responsibility.

Such a subset loses responsibility/remaining-work semantics, but the Scorecard still has a coherent application role: capture independent judgment.

This subset is **not automatically in scope**. Phase 012-I owns scope adoption.

If adopted, current Phase-011 Scorecard-start/finalization composition would require variant-specific refinement because the current full-application path is obligation-bound.

## 9.2 Scorecard ↛ Evaluation Occurrence

**Decision: reject universal edge.**

Scorecard intrinsically requires an `OccurrenceContext`, not necessarily the Evaluation Occurrence Concept.

A coherent individually assigned/asynchronous judging subset can provide a sufficient supplied context snapshot without representing a shared bounded occurrence.

The current full MUDAC product normally binds this context to Evaluation Occurrence. That remains valid composition, not universal inclusion dependence.

## 9.3 Scorecard ↛ Panel / Alias / Division

Panel, Alias, and Division can shape the judging situation but are not universally required to give Scorecard its application role.

Their selected variant may supply contextual facts through composition.

# 10. Rubric non-edges

## 10.1 Rubric ↛ Competition

**Decision: reject universal edge.**

A reusable evaluation instrument can be prepared, reviewed, or retained independently of one Competition occurrence.

This is a meaningful MUDAC preparation/library role rather than arbitrary unrelated reuse.

## 10.2 Rubric ↛ Evaluation Occurrence

Rubric can exist before any occurrence and can be reused across multiple occurrences where policy permits.

## 10.3 Rubric ↛ Evaluation Obligation

Rubric can exist without evaluator assignments.

## 10.4 Rubric ↛ Scorecard

Rubric can exist before or without recorded judgment.

# 11. Minimal direct evaluation graph

012-D therefore adds:

```text
                     ┌────────→ Team ─────────→ Competition
                     │
Evaluation Occurrence├────────→ Participation ─→ Competition
                     │                    └────→ Identity
                     └────────→ Rubric

                     ┌────────→ Team ─────────→ Competition
                     │
Evaluation Obligation├────────→ Participation ─→ Competition
                     │                    └────→ Identity
                     └────────→ Rubric

                     ┌────────→ Team ─────────→ Competition
                     │
Scorecard            ├────────→ Participation ─→ Competition
                     │                    └────→ Identity
                     └────────→ Rubric
```

There is intentionally no direct arrow among Occurrence, Obligation, and Scorecard.

# 12. Why the apparent cycle is rejected

The current full-product synchronization chain can look cyclic when read as inclusion:

```text
Occurrence establishes Obligation
Obligation leads to Scorecard
Scorecard satisfies Obligation
Scorecard refers to Occurrence context
```

Those arrows have different meanings:

- establishment synchronization;
- responsibility/evidence association;
- satisfaction synchronization;
- contextual reference.

None proves that the Concepts only make sense when co-included.

A dependency cycle would incorrectly erase useful product-family contractions.

# 13. Representative dependence-valid contractions through 012-D

These are validity probes, not scope commitments.

## 13.1 Rubric preparation/library subset

```text
Rubric
```

A reusable instrument-definition capability is coherent without current Competition, occurrence, obligation, or Scorecard inclusion.

Whether MUDAC adopts such a standalone preparation surface is a later scope question.

## 13.2 Occurrence-history subset

```text
Competition
Team
Identity
Participation
Rubric
Evaluation Occurrence
```

This can preserve bounded presentation/participant/evaluation-context truth without formal obligation tracking or judgment capture.

## 13.3 Responsibility/remaining-work subset

```text
Competition
Team
Identity
Participation
Rubric
Evaluation Obligation
```

This can track who owes which evaluation under which basis without internally capturing the judgment.

## 13.4 Lightweight judgment-capture subset

```text
Competition
Team
Identity
Participation
Rubric
Scorecard
```

This can capture independent evaluation while omitting formal responsibility tracking and bounded shared occurrence history.

Whether such a contraction satisfies enough of MUDAC's purpose to be in scope is deliberately deferred to 012-I.

## 13.5 Full current evaluation subset

```text
Competition
Team
Identity
Participation
Rubric
Evaluation Occurrence
Evaluation Obligation
Scorecard
```

This supports the current full composition where occurrence begin establishes obligations and Scorecard Finalization satisfies them.

Optional Alias/Division/Panel/Access capability rules remain governed by 012-C and current composition/policy.

# 14. Representative invalid subsets through 012-D

Given current accepted dependence:

```text
Evaluation Occurrence without Team        = invalid
Evaluation Occurrence without Participation = invalid
Evaluation Occurrence without Rubric      = invalid

Evaluation Obligation without Team        = invalid
Evaluation Obligation without Participation = invalid
Evaluation Obligation without Rubric      = invalid

Scorecard without Team                    = invalid
Scorecard without Participation           = invalid
Scorecard without Rubric                  = invalid
```

Because Team and Participation themselves depend on Competition, and Participation depends on Identity, those omissions are transitively invalid as well.

# 15. Access remains a capability condition, not a new direct edge

012-C established that protected Judge/Organizer operations use Participation context plus Access decisions while Access itself remains context-generic.

012-D does not add:

```text
Evaluation Occurrence → Access
Evaluation Obligation → Access
Scorecard             → Access
Rubric                 → Access
```

Instead, any protected operation in a variant that includes these Concepts remains subject to the current protected-operation capability rule.

This avoids turning every protected Concept into a dense star around Access while preserving confidentiality and authority separation.

# 16. Versioning and Provenance remain unresolved here

Current full MUDAC authoritative Rubric/Scorecard composition uses Versioning and Provenance.

012-D does not decide whether:

```text
Rubric    → Versioning / Provenance
Scorecard → Versioning / Provenance
```

or whether those requirements are capability-conditioned instead of universal Concept edges.

That is exactly the scope of **012-E — Authority Lineage, Provenance & Correctability Dependence**.

# 17. Variant-specific composition implications

012-D identifies three possible contractions that current Phase-011 synchronization does not fully expose as first-class variants:

1. Evaluation Occurrence without Evaluation Obligation;
2. Evaluation Obligation without Evaluation Occurrence;
3. Scorecard without Evaluation Obligation and/or Evaluation Occurrence.

These are dependence-coherent, but they are not adopted merely by this phase.

If 012-I selects any of them into MUDAC scope, the natural Phase-011 synchronization owner must be revalidated/refined so that:

- obligation creation is not forced when the variant intentionally omits Evaluation Obligation;
- obligation establishment can occur outside occurrence-begin composition when the variant omits Evaluation Occurrence;
- Scorecard start/finalization has an owner-safe path when formal responsibility is intentionally absent;
- historical/contextual facts remain sufficient for correction and explainability;
- no contraction weakens Judge authorship, missing-versus-zero truth, or authority separation by accident.

Until scope selection, current Phase-011 full-application composition remains unchanged.

# 18. Upstream integrity result

No accepted 012-D edge reveals intrinsic Concept coupling.

The Phase-010 abstractions remain independently meaningful:

```text
EvaluationOccurrence<Scope, Subject, Evaluator, PresentedContext, BasisRef>
EvaluationObligation<Scope, Evaluator, Subject, Basis, OccurrenceRef, EvidenceRef>
Rubric
Scorecard<Evaluator, Subject, OccurrenceContext, EvaluationBasis>
```

012-D relationships are contextual application dependence only.

# 19. Explanation-order implication

For Phase 013/later conceptual explanation, the accepted graph suggests:

```text
Competition / Team / Identity / Participation
  ↓
Rubric
  ↓
Evaluation Occurrence | Evaluation Obligation | Scorecard
```

This is explanatory order only, not UI navigation, runtime sequencing, or implementation layering.

Occurrence, Obligation, and Scorecard should be explained as three independent answers to three different questions:

```text
What evaluation situation actually happened?
Who was responsible to produce evaluation?
What judgment did the evaluator record?
```

# Exit decision

**PASS.**

012-D establishes a sparse evaluation dependence relation without importing Phase-011 synchronization into inclusion semantics.

No Phase-010 reopening is required.

No Phase-011 repair is required yet because newly identified contractions remain candidate product-family variants until 012-I scope selection.

The next dependency-safe subgroup is:

> **012-E — Authority Lineage, Provenance & Correctability Dependence**
