---
type: Phase Design Record
title: 012-H — Whole-Graph Transitivity, Co-Inclusion, Optionality & Minimal/Unfamiliar Subsets
description: "Validates the complete Phase-012 direct dependence graph and capability-conditioned rules as one family model, proves acyclicity and transitive closure, classifies optionality, tests minimal and unfamiliar subsets, identifies one reachability-redundant-but-semantically-retained edge, and establishes the product-family decision inputs for 012-I."
status: stable
tags: [phase-012, jackson, dependence, transitivity, cycles, optionality, subsets, product-family]
sources:
  - resource: 012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md
  - resource: 012-C-competition-actor-competitor-context-bias-control-dependence.md
  - resource: 012-D-evaluation-structure-responsibility-basis-judgment-dependence.md
  - resource: 012-E-authority-lineage-provenance-correctability-dependence.md
  - resource: 012-F-outcome-recognition-official-authority-dependence.md
  - resource: 012-G-external-representation-release-dependence.md
  - resource: ../canonical/dependence/application-family-dependence.md
  - resource: ../canonical/project/purpose-needs-success-tensions.md
  - resource: ../canonical/synchronizations/
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/006/dependence-subset-contract.md
---

# Purpose

Treat the Phase-012-C through 012-G results as one complete application-family model and validate that model globally before selecting supported product-family variants.

012-H does **not** invent new family-local dependencies by default. It asks whether the already accepted direct graph plus capability-conditioned rules remain coherent when analyzed for:

- transitive closure;
- cycles / genuine co-inclusion groups;
- redundant direct edges;
- global optionality;
- minimal dependence closures;
- unfamiliar but coherent subsets;
- direct-edge versus capability-rule consistency;
- invalid claims;
- upstream Concept or synchronization defects.

The analyzed family remains:

> **MUDAC live student data competition judging and outcome formation**, including preparation, independent evaluation, correction, explicit outcome authority, and optional controlled external representation/release.

# Decision summary

**PASS — the complete Phase-012 graph is acyclic, no genuine Concept co-inclusion cycle exists, no new direct edge is required, and the current capability-conditioned rules are consistent with direct closure.**

Key conclusions:

1. the direct graph is a **DAG**;
2. every strongly connected component is a single Concept;
3. there is no universal mutual-dependence/co-inclusion group;
4. `Competition` is the only universal **in-scope family anchor**, but it is not a blanket direct dependency of every capability;
5. every other Concept is globally optional in the sense that at least one coherent MUDAC-family capability/subset can omit it;
6. optionality does **not** imply low importance—many Concepts are mandatory when a named capability is claimed;
7. `Award → Competition` is reachability-redundant through `Award → Team → Competition`, but remains semantically justified as a distinct scope edge and is retained;
8. the unfamiliar-subset probes from 012-A all have explicit outcomes;
9. no Phase-010 reopening and no immediate Phase-011 repair are required;
10. 012-I may now choose which coherent variants are actually in product scope.

# 1. Complete direct graph under test

012-H validates, without changing, the direct relation established through 012-G:

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation

Evaluation Occurrence → Team
Evaluation Occurrence → Participation
Evaluation Occurrence → Rubric

Evaluation Obligation → Team
Evaluation Obligation → Participation
Evaluation Obligation → Rubric

Scorecard → Team
Scorecard → Participation
Scorecard → Rubric

Award               → Competition
Award               → Team
Outcome Declaration → Competition

Publication → Export
```

The direct relation is distinct from capability-conditioned rules such as authoritative evaluation, ordinary official closeout, rank-derived recognition, and public official-result release.

# 2. Whole-graph acyclicity

## 2.1 No direct cycle

No current direct path returns to its origin.

The graph moves toward independently reusable/supporting roots such as:

- Competition;
- Identity;
- Rubric;
- Export.

Other independent Concepts with no direct outgoing edge include Access, Versioning, and Provenance.

No reverse edge from those roots closes a cycle.

## 2.2 Strongly connected components

Every strongly connected component contains exactly one Concept.

Therefore there is no current application-family co-inclusion group of the form:

```text
A → B
B → A
```

This matters because the full product contains many coordinated pairs that could have been mistaken for cycles:

```text
Identity / Participation
Evaluation Occurrence / Evaluation Obligation / Scorecard
Versioning / Provenance
Award / Outcome Declaration
Export / Publication
```

None is a mutual inclusion group.

# 3. Transitive closure

The direct graph produces the following Concept-level transitive requirements.

| Concept | Direct + transitive Concepts required by dependence |
| --- | --- |
| Competition | none |
| Division | Team, Competition |
| Team | Competition |
| Panel | Participation, Identity, Competition |
| Evaluation Occurrence | Team, Participation, Rubric, Identity, Competition |
| Evaluation Obligation | Team, Participation, Rubric, Identity, Competition |
| Rubric | none |
| Scorecard | Team, Participation, Rubric, Identity, Competition |
| Award | Team, Competition |
| Identity | none |
| Participation | Identity, Competition |
| Alias | Team, Competition |
| Access | none |
| Versioning | none |
| Provenance | none |
| Outcome Declaration | Competition |
| Export | none |
| Publication | Export |

This table is **dependence closure only**. It does not include capability-conditioned support such as Versioning + Provenance for authoritative evaluation, nor the family-scope rule that every adopted in-scope MUDAC variant retains Competition.

# 4. Direct-edge redundancy audit

## 4.1 Award → Competition is reachability-redundant

Because:

```text
Award → Team → Competition
```

Competition is already reachable from Award.

However 012-F accepted the direct edge for a distinct application-role reason:

```text
Award → Competition
  = where the recognition belongs

Award → Team
  = what kind of recipient receives it
```

If MUDAC later changes recipient policy while preserving Competition-scoped recognition, removing `Award → Competition` now would erase that independent scope meaning.

**Decision: retain the edge.**

012-H classifies it as:

> **reachability-redundant but semantically non-redundant**.

## 4.2 No other accepted direct edge is transitively redundant

The remaining direct edges provide unique immediate reachability or independent role anchors.

No pruning is required.

# 5. Global optionality

## 5.1 Competition is the family anchor

Every **adopted in-scope MUDAC product/application variant** includes Competition.

This is a scope rule established earlier in Phase 012 and reaffirmed here.

It does not mean:

```text
Competition → every Concept
```

and it does not make generic dependence-valid subsets containing reusable Concepts automatically in-scope MUDAC products.

## 5.2 All other Concepts are globally optional

For each of the other seventeen Concepts, at least one coherent MUDAC-family subset/capability can omit it.

Examples:

- Division can be omitted by a single-cohort variant;
- Panel can be omitted by ad-hoc evaluator assignment;
- Alias can be omitted by a non-blinded disclosure profile;
- Evaluation Occurrence / Obligation / Scorecard can each be omitted by different evaluation contractions;
- Versioning / Provenance can be omitted by working-only, non-authoritative evaluation profiles;
- Award can be omitted by official outcome without named recognition;
- Outcome Declaration can be omitted by judging/operation or recognition-only capability;
- Export can be omitted by official-but-non-public operation;
- Publication can be omitted by prepared-but-unreleased representation;
- Access can be omitted from a subset that exposes no protected contextual operation;
- Identity / Participation can be omitted from competition-structure or outcome-disposition subsets that do not include human participation capability;
- Rubric can be omitted from non-evaluation subsets.

This does **not** make these Concepts unimportant. It means only that the product family has coherent variants in which their capabilities are absent.

# 6. Capability-conditioned mandatory inclusion remains intact

Global optionality does not weaken capability rules.

## 6.1 Authoritative Rubric Basis

```text
Authoritative Rubric Basis
  ⇒ Rubric + Versioning + Provenance
```

For an adopted in-scope MUDAC variant, Competition is also present by family scope.

## 6.2 Authoritative Scorecard Evidence

Direct closure of Scorecard is:

```text
Scorecard
+ Team
+ Participation
+ Rubric
+ Identity
+ Competition
```

The authority profile adds:

```text
+ Versioning
+ Provenance
```

Therefore the minimum Concept set for that named capability is:

```text
Competition
Team
Identity
Participation
Rubric
Scorecard
Versioning
Provenance
```

Occurrence and Obligation are not added merely because the current full-product workflow often includes them.

## 6.3 Rank-derived Award

Direct Award closure is:

```text
Award + Team + Competition
```

Current rank-derived capability additionally requires Division context because the current Rank mechanism is Division-scoped.

Thus current capability closure includes:

```text
Competition + Team + Division + Award
```

plus a legitimate Ranking Ready supplied basis and applicable policy.

This still does not create a universal `Award → Division` edge.

## 6.4 Ordinary Official Closeout

```text
Ordinary Official Closeout
  ⇒ Competition + Outcome Declaration
```

`Outcome Declaration → Competition` already satisfies the direct graph closure.

No contradiction exists between the capability rule and the direct graph.

## 6.5 Public Official-Result Release

```text
Public Official-Result Release
  ⇒ Outcome Declaration + Export + Publication
```

Direct closure supplies:

```text
Outcome Declaration → Competition
Publication          → Export
```

so the resulting Concept closure is:

```text
Competition
Outcome Declaration
Export
Publication
```

plus the variant-specific accepted OutcomeBasis, disclosure and publishing-authority capabilities.

No Award or fixed evaluation-source Concept is universally required.

# 7. Minimal dependence closures

For a Concept `A`, this section gives the smallest Concept set closed under the direct graph that contains `A`.

```text
Competition
  → {Competition}

Team
  → {Team, Competition}

Division
  → {Division, Team, Competition}

Alias
  → {Alias, Team, Competition}

Participation
  → {Participation, Identity, Competition}

Panel
  → {Panel, Participation, Identity, Competition}

Evaluation Occurrence
  → {Evaluation Occurrence, Team, Participation, Rubric, Identity, Competition}

Evaluation Obligation
  → {Evaluation Obligation, Team, Participation, Rubric, Identity, Competition}

Scorecard
  → {Scorecard, Team, Participation, Rubric, Identity, Competition}

Award
  → {Award, Team, Competition}

Outcome Declaration
  → {Outcome Declaration, Competition}

Publication
  → {Publication, Export}
```

Concepts with no outgoing direct edge have singleton formal closures:

```text
Identity
Rubric
Access
Versioning
Provenance
Export
```

A singleton formal closure is **not automatically a meaningful MUDAC product variant**.

# 8. Formal validity versus meaningful MUDAC subset

The graph deliberately allows formally closed subsets that are too small or too generic to constitute a useful MUDAC product.

Examples:

```text
{Access}
{Versioning}
{Provenance}
{Export}
{Rubric}
{Competition}
```

may satisfy direct closure in isolation, but product-family meaning still requires a defensible MUDAC role.

012-H therefore preserves the 012-A distinction:

```text
dependence-valid
  != meaningful MUDAC family member
  != adopted in-scope variant
```

012-I owns the last step.

# 9. Minimal meaningful capability subsets

These are representative **meaningful capability closures**, not adopted variants.

## 9.1 Competitor structure

```text
Competition + Team
```

This is the smallest clear student-competition structure subset.

A bare Competition remains formally valid but does not by itself deliver a substantive judging/outcome capability; treat it as a lifecycle shell rather than a candidate product variant unless 012-I identifies a concrete purpose.

## 9.2 Scoped human participation

```text
Competition + Identity + Participation
```

This provides attributable event-scoped human involvement without requiring Panel, evaluation work or Access unless those capabilities are included.

## 9.3 Evaluation occurrence history

```text
Competition
+ Team
+ Identity
+ Participation
+ Rubric
+ Evaluation Occurrence
```

## 9.4 Responsibility tracking

```text
Competition
+ Team
+ Identity
+ Participation
+ Rubric
+ Evaluation Obligation
```

## 9.5 Working judgment capture

```text
Competition
+ Team
+ Identity
+ Participation
+ Rubric
+ Scorecard
```

This subset must not claim authoritative evidence unless Versioning + Provenance are added.

## 9.6 Authoritative judgment

```text
Competition
+ Team
+ Identity
+ Participation
+ Rubric
+ Scorecard
+ Versioning
+ Provenance
```

## 9.7 Discretionary recognition

```text
Competition + Team + Award
```

## 9.8 Official disposition

```text
Competition + Outcome Declaration
```

plus a reconstructible accepted OutcomeBasis capability.

This supports the important no-result/exception counterexample without forcing Team or evaluation-source edges into Outcome Declaration.

## 9.9 Prepared representation

```text
Competition + Export
```

plus a valid MUDAC SourceBasis capability.

`Export` alone is formally closed, but adopted MUDAC variants retain Competition.

## 9.10 Deliberate non-official release

```text
Competition + Export + Publication
```

plus a legitimate releasable non-official SourceBasis and disclosure/publishing authority.

## 9.11 Public official-result release

```text
Competition + Outcome Declaration + Export + Publication
```

plus accepted source/disclosure/publishing capability.

# 10. 012-A unfamiliar-subset probe closure

## U-01 — Single-cohort competition without Division

**Dependence result: coherent.**

No direct edge requires Division.

If the variant also claims the current blinded Judge-facing policy, anonymity/disclosure and occurrence-presentation composition require revalidation before adoption.

## U-02 — Ad-hoc judging without Panel

**Dependence result: coherent.**

Occurrence/Obligation/Scorecard depend on Participation rather than Panel. Panel remains a reusable intended-grouping capability.

## U-03 — Judging-only variant

**Dependence result: coherent.**

Evaluation capability may omit Award, Outcome Declaration, Export and Publication.

It must not claim ordinary official closeout or public result release.

## U-04 — Outcome variant without Awards

**Dependence result: coherent.**

Outcome Declaration does not depend on Award.

## U-05 — Official but non-public

**Dependence result: coherent.**

Outcome Declaration may exist without Export or Publication.

## U-06 — Export without Publication

**Dependence result: coherent.**

Export representation is useful without release.

## U-07 — Export from non-outcome source

**Dependence result: coherent.**

SourceBasis is variant-specific and may represent setup, Rubric/evaluation material, provisional result state or other legitimate source state.

## U-08 — Publication without Export

**Dependence result: invalid.**

`Publication → Export` is a current direct edge.

## U-09 — No-Alias judging

**Dependence result: coherent only for a disclosure profile that does not claim the current blinded-judging baseline.**

The direct graph does not require Alias from Team/evaluation Concepts. A variant claiming current blinded judging must include Alias.

## U-10 — Reduced authority history

**Dependence result: conditional.**

Working/preparation-only Rubric or Scorecard capability may omit Versioning/Provenance.

Authoritative Rubric Basis or authoritative Scorecard Evidence without either support Concept is invalid.

## U-11 — Responsibility without occurrence

**Dependence result: coherent.**

Evaluation Obligation has no universal Occurrence dependency.

## U-12 — Occurrence without responsibility

**Dependence result: coherent.**

Evaluation Occurrence has no universal Obligation dependency.

## U-13 — Paper/electronic contraction

**Not a Concept-subset axis.**

Paper versus electronic capture changes channel/representation path, not the Concept family itself. Paper continuity does not manufacture Export dependence unless stable external representation is explicitly part of the capability.

# 11. Additional unfamiliar subsets

## 11.1 Public non-official material

```text
Competition + Export + Publication
without Outcome Declaration
```

**Coherent.**

This is an important counterexample preventing `Publication → Outcome Declaration`.

## 11.2 Official no-result disposition without Team result content

```text
Competition + Outcome Declaration
```

with a reconstructible accepted exceptional/no-result basis.

**Coherent.**

This validates the absence of direct `Outcome Declaration → Team` and evaluation-source edges.

## 11.3 Discretionary Award without Division

```text
Competition + Team + Award
```

**Coherent.**

This validates the absence of universal `Award → Division`.

## 11.4 Publication over reusable non-result material

A MUDAC variant may publish an Export of reusable/public Rubric or event material without Outcome Declaration.

**Coherent at the dependence level.**

The adopted product still retains Competition as family scope; the source/disclosure policy must justify the release.

## 11.5 Access without Participation

Access has no universal outgoing edge to Participation/Identity.

A support/disclosure decision context can therefore be coherent without Judge/Organizer Participation.

However `{Access}` alone is not a meaningful product variant. It is an optional contextual capability that requires supplied facts/rules appropriate to the operation being guarded.

# 12. Invalid whole-graph subsets / claims

The whole-graph audit confirms these direct-dependence violations:

```text
Team without Competition
Participation without Competition
Participation without Identity
Division without Team
Alias without Team
Panel without Participation
Evaluation Occurrence without Team / Participation / Rubric
Evaluation Obligation without Team / Participation / Rubric
Scorecard without Team / Participation / Rubric
Award without Team
Award without Competition
Outcome Declaration without Competition
Publication without Export
```

Capability-invalid claims include:

```text
Authoritative Rubric Basis without Versioning
Authoritative Rubric Basis without Provenance
Authoritative Scorecard Evidence without Versioning
Authoritative Scorecard Evidence without Provenance
rank-derived Award without legitimate Ranking Ready basis
ordinary official closeout without Outcome Declaration
official Outcome Declaration without reconstructible accepted OutcomeBasis
Export without exact valid SourceBasis / purpose / AudienceProfile
public official-result release without Outcome Declaration
public official-result release without Export
public official-result release without Publication
public official-result release without legitimate disclosure/publishing authority
Publication treated as delivery success
Export generation treated as release
```

# 13. Direct-edge / capability-rule consistency audit

No capability rule contradicts the direct graph.

- authoritative Rubric/Scorecard rules add support Concepts without requiring reverse edges;
- current rank-derived Award adds Division context without making all Awards Division-dependent;
- ordinary official closeout includes Outcome Declaration without making all Competitions declaration-dependent;
- public official-result release combines Outcome Declaration + Publication/Export without creating an official/public cycle;
- corrected successor release uses the already accepted `Publication → Export` relation and explicit synchronization;
- paper continuity remains representation-channel behavior rather than a Concept edge.

No capability rule requires a Concept that its own direct closure forbids or creates a mutual-dependence contradiction.

# 14. Product-family optionality matrix for 012-I

012-I should evaluate capabilities, not infer importance from edge count.

| Concept | Family-wide status before 012-I | Capability pressure |
| --- | --- | --- |
| Competition | universal in-scope anchor | required in every adopted MUDAC variant |
| Team | optional globally | required by competitor/evaluation/Award capability |
| Identity | optional globally | required transitively by Participation |
| Participation | optional globally | required by Panel/evaluation-work capability |
| Division | optional globally | required for current multi-cohort and current rank-derived context |
| Alias | optional globally | required by current blinded-judging profile |
| Panel | optional globally | required by reusable intended evaluator grouping |
| Evaluation Occurrence | optional globally | bounded occurrence-history capability |
| Evaluation Obligation | optional globally | responsibility/remaining-work capability |
| Rubric | optional globally | required by current evaluation-work Concepts |
| Scorecard | optional globally | judgment-capture capability |
| Access | optional globally | protected contextual capability/disclosure decisions |
| Versioning | optional globally | mandatory in named authoritative evaluation profiles |
| Provenance | optional globally | mandatory in named authoritative evaluation profiles |
| Award | optional globally | recognition capability |
| Outcome Declaration | optional globally | mandatory for ordinary official closeout/official authority |
| Export | optional globally | representation capability; mandatory under Publication |
| Publication | optional globally | deliberate release capability |

# 15. Scope candidates handed to 012-I

012-I must deliberately classify, at minimum, these coherent families as **in scope** or **coherent but out of scope**:

1. single-cohort competition without Division;
2. multi-cohort competition with Division;
3. blinded judging with Alias;
4. alternate non-blinded judging without Alias;
5. ad-hoc evaluator assignment without Panel;
6. reusable evaluator grouping with Panel;
7. occurrence-history-only evaluation contraction;
8. responsibility-only evaluation contraction;
9. working Scorecard capture without Occurrence/Obligation;
10. authoritative Scorecard evaluation with Versioning + Provenance;
11. recognition without official declaration;
12. official declaration without Award;
13. judging/operation without Outcome Declaration;
14. Export without Publication;
15. official-but-non-public operation;
16. public non-official material;
17. public official-result release;
18. current Division-contextual rank-derived Award;
19. possible no-Division ranked variant requiring policy/composition generalization;
20. paper/electronic/mixed capture as a channel profile rather than a Concept-subset variant.

012-I need not turn these into commercial editions. The task is product-family scope selection and variant-specific composition revalidation.

# 16. Explanation-order implications

The graph suggests a clear explanation order for later mapping/documentation without implying implementation sequence:

```text
Competition
  → Team / Identity / Rubric / Export foundations as relevant
  → Participation
  → Division / Alias / Panel
  → Evaluation Occurrence / Obligation / Scorecard
  → Versioning / Provenance when authority profiles are claimed
  → Award / Outcome Declaration
  → Publication after Export
```

This is only an intelligibility aid. Phase 013 owns mapping/representation.

# 17. Upstream integrity and reopening decision

012-H finds:

- no intrinsic Concept coupling hidden by dependence;
- no cycle suggesting two Concepts should be merged;
- no missing Concept required to make the graph coherent;
- no derived mechanism that must become a Concept;
- no direct-edge/capability-rule contradiction;
- no subset contradiction forcing immediate Phase-011 repair.

Therefore:

```text
Phase 010 reopening: NOT REQUIRED
Phase 011 reopening: NOT REQUIRED NOW
```

Variant-specific Phase-011 refinement remains a legitimate 012-I consequence if an alternative subset is adopted.

# 18. Exit decision

**PASS.**

The complete dependence model is coherent enough to move from **what combinations are possible** to **which combinations MUDAC deliberately supports**.

012-I is authorized to perform product-family scope selection and variant-specific composition revalidation.

The next subgroup is:

> **012-I — Product-Family Variants, Scope Selection & Variant-Specific Composition Revalidation**
