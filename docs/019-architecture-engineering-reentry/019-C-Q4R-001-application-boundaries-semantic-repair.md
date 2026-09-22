---
type: Architecture Candidate Repair
title: 019-C Q4R-001 — Historical Application-Boundary Semantic Repair
description: "Repairs the historical Application Boundaries candidate for current Phase-019 comparison by translating superseded Judging Encounter and Official Outcome Revision bindings to current Evaluation Occurrence, Evaluation Obligation, Outcome Declaration and temporal-correction authority without rewriting the historical candidate."
status: stable
tags: [phase-019, architecture, q4, repair, application-boundaries, semantics]
sources:
  - resource: ../canonical/architecture/application-boundaries.md
  - resource: ../canonical/concepts/evaluation-occurrence.md
  - resource: ../canonical/concepts/evaluation-obligation.md
  - resource: ../canonical/concepts/outcome-declaration.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/synchronizations/evaluation-outcome-finalization-declaration.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: ../canonical/dependence/application-family-dependence.md
  - resource: ../canonical/governance/architecture-decision-authority.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T07:35:00-05:00 }
---

# Purpose

Complete Q4R-001 before the historical Application Boundaries candidate participates in ADQ-002 comparison.

The source candidate remains unchanged historical evidence.

This record translates its stale semantic bindings into the current Concept/composition model.

# Candidate

> docs/canonical/architecture/application-boundaries.md

Qualification:

~~~text
Q2 / Q4
QUALIFIED_AFTER_REVISION
authority = suspended-candidate
comparison eligible before repair = false
~~~

# Stale binding 1 — Judging Encounter

Historical candidate wording assigns Judging Operations ownership over:

- Panel;
- Panel membership/composition;
- Judging Encounter lifecycle;
- effective participants;
- absence/recusal/substitution/replacement;
- Encounter obligations.

Current translation:

~~~text
Judging Encounter
  → Evaluation Occurrence
    + Evaluation Obligation
~~~

with current semantics:

- Panel owns reusable evaluator grouping/planning;
- Evaluation Occurrence owns one actual bounded evaluation occurrence, presented context, actual participants and occurrence history;
- Evaluation Obligation owns evaluator responsibility;
- Panel change does not rewrite begun occurrence history;
- occurrence completion does not imply obligation completion;
- occurrence invalidation/replacement preserves prior history and uses explicit successor responsibility where required.

The historical idea of one "Judging Operations" area remains a topology hypothesis only.

It may not collapse Evaluation Occurrence and Evaluation Obligation into one semantic owner.

# Stale binding 2 — Official Outcome Revision

Historical candidate wording assigns Outcomes & Closeout ownership over "Official Outcome Revision."

That is no longer a current Concept.

Current translation:

~~~text
ordinary official authority
  → Outcome Declaration.declare

material source correction
  → current temporal-correction owners
  → Outcome Declaration.identifyAffected

corrected reconciled basis
  → Outcome Declaration.confirmSuccessor
~~~

Competition remains the owner of lifecycle Finalization.

Outcome Declaration remains the owner of official declaration content, currentness and predecessor/successor history.

Coverage/Aggregate/Rank remain derived mechanisms, and Award remains independent recognition authority.

There is no generic "Official Outcome Revision" owner.

# Additional current-owner clarification

The historical candidate also mentions "Team Attributes."

Current Concept Design does not establish a standalone Team Attributes Concept.

Extensible Team/Competition structural attributes may exist as owned data within the natural Team/Competition context where current semantics permit them; they do not create an additional module owner by name.

# Retained architecture hypotheses

The following candidate ideas survive semantic repair and are eligible for comparison:

1. authoritative write ownership should be explicit;
2. application decomposition should follow cohesive semantic/authority responsibilities rather than one module per Concept;
3. cross-owner coordination belongs above natural owners and must not become a second semantic owner;
4. non-authoritative read/projection composition may span owners;
5. direct cross-owner storage mutation should be forbidden;
6. dependencies should avoid cycles and downstream concerns should not drive upstream authority;
7. Versioning/Provenance may use shared technical primitives without becoming a god-module;
8. infrastructure/framework/provider adapters should depend inward on application contracts;
9. physical distribution should require a demonstrated driver;
10. module boundaries should remain extractable/evolvable where justified.

# Excluded obsolete content

The repaired comparison hypothesis excludes:

- Judging Encounter as a current owner/name;
- Encounter obligations as one combined concept;
- Official Outcome Revision as a current owner/name;
- any implication that the historical six-module map is already accepted;
- the claim that one authoritative server deployment is already selected by history;
- any old Concept/phase dependency used only because it existed before Phase-009;
- any interpretation of ARCH-/MOD-* candidate rules as current authority.

# Revised comparison statement

The historical candidate may now be compared as this revised hypothesis:

> **Use an ownership-preserving modular application boundary in which cohesive current semantic owners are grouped into explicit modules, cross-owner workflows are coordinated above those modules without acquiring semantic authority, read projections remain non-authoritative, direct cross-owner persistence access is prohibited, and physical distribution is deferred until a demonstrated driver exists.**

The exact module grouping remains part of ADQ-002 comparison.

# Current semantic preservation evidence

This translation is grounded in:

- Evaluation Occurrence current ownership;
- Evaluation Obligation current ownership;
- current occurrence/obligation composition;
- Outcome Declaration current ownership;
- current temporal correction;
- current evaluation/outcome/finalization/declaration composition;
- current extrinsic dependence graph;
- ENG-001 / ENG-009 / ENG-017;
- DRV-001 / DRV-002 / DRV-005 / DRV-010 / DRV-011.

# Repair decision

**Q4R-001 — COMPLETE.**

~~~text
historical source rewritten        NO
current semantic translation       YES
comparison eligible                YES
candidate adopted                  NO
~~~

This repair establishes comparison eligibility only.
