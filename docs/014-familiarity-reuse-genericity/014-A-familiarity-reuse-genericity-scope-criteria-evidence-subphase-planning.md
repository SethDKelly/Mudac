---
type: Phase Start Gate
title: 014-A — Familiarity, Reuse & Genericity Scope, Criteria, Evidence & Subphase Planning
description: "Mandatory Phase-014 start gate defining MUDAC-specific familiarity, conceptual reuse, broader genericity, false-familiarity, novelty, reusable-knowledge and propagation criteria, evidence authority, risks and dependency-safe subphase plan."
status: stable
tags: [phase-014, jackson, familiarity, reuse, genericity, false-familiarity, novelty, catalog, planning]
sources:
  - resource: ../013-concept-mapping-interaction-semantics-user-visible-representation/013-L-canonical-mapping-reconciliation-phase-013-consolidation-phase-014-handoff.md
  - resource: ../009-jackson-methodology-realignment/009-B-jackson-base-lifecycle-crosswalk-evidence-reuse-gap-map.md
  - resource: ../canonical/project/
  - resource: ../canonical/concepts/
  - resource: ../canonical/synchronizations/
  - resource: ../canonical/dependence/
  - resource: ../canonical/experience/mapping-authority-baseline.md
  - resource: ../canonical/experience/action-authority-traceability.md
  - resource: ../canonical/policies/
  - resource: ../canonical/invariants/
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/008/phase-definition.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/008/008-a-start-gate.md
---

# Purpose

Open Phase 014 — Familiarity, Reuse & Genericity with a project-specific audit plan over the mature MUDAC conceptual system after Phase 013 mapping closure.

014-A plans the audit. It does **not** itself declare any MUDAC Concept familiar, reusable, generic, novel, catalog-ready, renamed or replaceable.

The gate exists to prevent two opposite design failures:

1. retaining unnecessary novelty where an established concept would transfer correct understanding and reusable design knowledge; and
2. forcing a familiar label or pattern onto MUDAC semantics whose purpose, authority, lifecycle, history or composition materially differ.

# Gate decision

**READY TO BEGIN PHASE 014 SUBPHASES. Proceed to 014-B.**

```text
Phase 013 mapping / representation                COMPLETE — PASS
Phase 014 start gate                              COMPLETE — READY
mature Concept specifications discoverable        YES
current synchronization/action surface             YES
current dependence / PF-01 scope                   YES
current Experience mapping corpus                  YES
terminology stable enough for familiarity audit    YES
implementation / architecture as authority         PROHIBITED
new domain implementation                          NOT STARTED
implementation readiness                           NOT READY
implementation authorization                       NOT YET
NEXT                                                 014-B
```

# 1. Phase-014 authority

Phase 014 audits **conceptual familiarity and reusable design knowledge**.

In scope:

- whether established/familiar concepts serve substantially the same purpose with compatible behavior;
- whether current terminology transfers correct or incorrect expectations;
- whether MUDAC Concepts are unnecessarily product/scenario specific;
- whether sound independent Concepts can become more reusable through safe parameterization/generalization;
- whether apparently duplicated semantics are genuinely reusable or only superficially similar;
- whether retained novelty is necessary and understandable;
- whether stable lessons are worth preserving as reusable concept knowledge;
- whether Phase-013 mapped experience exposes familiarity or false-familiarity concerns that concept titles alone hide;
- propagation/reopen decisions required by adopted familiarity/genericity refinements.

Out of scope:

- source-code/library/package reuse;
- frontend/component/design-system reuse;
- framework/vendor/platform/service selection;
- persistence/database/API/runtime reuse;
- infrastructure standardization;
- implementation templates or generators;
- architecture re-entry;
- popularity or competitor prevalence as sufficient evidence of conceptual fit.

# 2. Incoming mature-design baseline

Phase 014 consumes the current post-013 design rather than reconstructing it from history.

Current authority entering the phase is:

```text
Project Purpose / Mandate
  → 18 current Concepts
  → Phase-011 synchronization + D/C/P/S/X application action surface
  → Phase-012 dependence + PF-01 scope
  → Policies / Invariants
  → Phase-013 Experience mapping + whole-experience traceability
```

The current 18-Concept catalog is:

```text
Competition
Division
Team
Panel
Evaluation Occurrence
Evaluation Obligation
Rubric
Scorecard
Award
Identity
Participation
Alias
Access
Versioning
Provenance
Outcome Declaration
Export
Publication
```

Deprecated `Judging Encounter` / `Encounter` and `Official Outcome Revision` remain historical adapters, not familiarity candidates to restore by convention.

# 3. Familiarity criterion

A concept is not familiar merely because its name or interface shape resembles something common.

The core question for every comparison is:

> Would a person who understands the proposed familiar precedent bring **mostly correct expectations** about the MUDAC concept's purpose and behavior?

Compare, where material:

1. purpose / user need;
2. operational principle;
3. abstract state;
4. actions and queries;
5. lifecycle / finality / reversibility;
6. authority / authorship / delegation;
7. historical retention / correction semantics;
8. scope / target / generic parameters;
9. synchronization and automation consequences;
10. dependence / optionality assumptions;
11. user-visible mapping / disclosure expectations;
12. behavior across Judge, Organizer, support, public/history and degraded-operation contexts.

Similarity in only one or two dimensions is an analogy, not concept reuse.

# 4. Comparison dispositions

Later subphases may disposition a familiarity candidate as:

- **SEMANTIC FIT / REUSE CANDIDATE** — substantially same purpose and materially compatible behavior; adoption/reframing worth considering;
- **USEFUL ANALOGY ONLY** — helps explanation, but material semantic differences prevent concept substitution;
- **FALSE FAMILIARITY RISK** — familiar term/metaphor would cause materially incorrect expectation transfer;
- **DISTINCT / RETAIN NOVELTY** — familiar alternatives do not satisfy the MUDAC purpose/behavior and explicit novelty is clearer;
- **BROADER GENERICITY CANDIDATE** — current concept is sound but may safely remove incidental MUDAC-specificity;
- **UPSTREAM DEFECT / REOPEN CANDIDATE** — comparison exposes an actual purpose, boundary, behavior, composition, dependence or mapping defect rather than a Phase-014 familiarity issue.

014-A assigns none of these dispositions to a specific Concept.

# 5. Evidence hierarchy

Use evidence in this order:

1. **current MUDAC canonical authority** — purpose, Concepts, synchronizations, dependence, policies, invariants and Experience mapping;
2. **Phase-013 mapped user-visible semantics** — because familiarity must match the behavior people actually perceive/invoke;
3. **current/historical MUDAC discovery alternatives** — useful for already-considered boundaries and rejected meanings;
4. **authoritative concept-design/domain references and stable external conceptual precedents** — comparison evidence, never automatic authority;
5. **widely understood software/domain concepts** — hypotheses requiring semantic validation;
6. **historical MUDAC architecture/UI/implementation** — contamination probe or evidence of prior expectation only, never familiarity authority.

Do not infer conceptual fit from implementation similarity.

# 6. Plausible comparison-source classes

Phase 014 may use, when relevant:

- Daniel Jackson concept examples/catalog material;
- established domain concepts from competitions, judging/evaluation, governance and publication/release domains;
- mature cross-application concepts such as identity, participation/membership, authorization/access, version/history, provenance/audit, declaration/record, export/snapshot and publication/release;
- earlier MUDAC candidate concepts and rejected alternatives;
- comparable concepts already validated elsewhere in the user's concept-design repositories only as comparison evidence, not as shared authority.

Every precedent must be evaluated by semantics, not reputation or frequency of use.

# 7. False-familiarity risk baseline

Phase 014 must actively probe at least these expectation-transfer risks:

- **Competition** — event/container/workflow expectations versus current lifecycle authority;
- **Division / Team / Panel** — familiar organizational/grouping terms accidentally implying responsibility or authority;
- **Participation** — membership/session/role expectations versus Competition-scoped capacity state;
- **Access** — RBAC/permission-object expectations versus contextual capability/disclosure decision;
- **Alias** — nickname/account-alias expectations versus scoped bias-control alternate identity;
- **Evaluation Occurrence / Evaluation Obligation** — event/task/assignment expectations that collapse actual occurrence, responsibility and evidence;
- **Rubric / Scorecard** — template/form/record expectations that collapse basis, working Draft and authoritative judgment;
- **Award** — calculated rank/winner expectations versus explicit recognition authority;
- **Versioning / Provenance** — generic technical revision/audit-log expectations versus composition-only historical support;
- **Outcome Declaration** — result/report/publication expectations versus explicit official authority;
- **Export** — file/download expectations versus stable exact-source representation/currentness;
- **Publication** — content publishing/delivery expectations versus explicit release authority.

This is a probe register, not a finding that these names are wrong.

# 8. Broader genericity opportunity baseline

Phase 004/010 already resolved genericity required for independence. Phase 014 asks only the broader reuse question.

Probe whether any sound Concept contains incidental specificity in:

- target type;
- actor role name;
- Competition-only terminology;
- fixed subject class where a parameter would preserve purpose;
- state/action wording tied to one MUDAC scenario;
- duplicated history/currentness patterns that may share reusable knowledge without sharing authority;
- mapping terminology that obscures a broader stable conceptual idea.

Reject any generalization that:

- weakens purpose specificity;
- blurs authority or authorship;
- hides domain-significant lifecycle/history;
- causes capability union;
- merges distinct Concepts merely because their state shapes look similar;
- creates an abstract super-concept with no independent user-facing purpose.

# 9. Reusable-knowledge / catalog candidate baseline

A Concept may be a reusable-knowledge candidate when its stable design lessons plausibly apply beyond MUDAC.

Potential reusable knowledge includes:

- purpose and operational principle;
- generic parameters;
- abstract state/actions/invariants;
- common synchronization/dependence cautions;
- false-familiarity traps;
- history/correction/authority pitfalls;
- mapping/disclosure cautions;
- representative misfit cases.

Catalog candidacy does **not** require a duplicate catalog specification. The natural MUDAC canonical owner remains current truth; any reusable supplemental artifact must add genuinely distinct cross-context knowledge.

# 10. Refinement blast-radius rule

A Phase-014 refinement is incomplete until its consequences are propagated to natural owners.

Potential destinations are:

```text
purpose / boundary defect              → Phase 010 natural owner / explicit reopen if material
composition / action defect            → Phase 011
scope / dependence defect              → Phase 012
mapping / terminology defect           → Phase 013 natural Experience owner
familiarity / reuse / genericity only  → Phase 014 record + affected canonical owner
```

Any adopted rename/generalization/substitution must also reconcile:

- Concept index and references;
- synchronizations and action labels;
- dependence/PF-01 language;
- policies/invariants;
- Experience mapping terminology;
- governance/agent navigation where materially affected;
- supersession/history markers.

Phase 014 must not become a shadow canonical specification.

# 11. Concept-family coverage plan

To ensure every current Concept receives deliberate familiarity/reuse review without producing one redundant document per Concept, Phase 014 uses three dependency-safe semantic families.

## Family 1 — Competition context, competitor, grouping, identity and capability

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

Principal familiarity pressure: event/container semantics, organizational grouping, membership/role/capacity, identity aliases, contextual authorization/disclosure.

## Family 2 — Evaluation basis, occurrence, responsibility and judgment

```text
Evaluation Occurrence
Evaluation Obligation
Rubric
Scorecard
```

Principal familiarity pressure: event/session/task/assignment, rubric/template, form/submission/record, Draft versus committed judgment.

## Family 3 — Historical support, recognition, officiality and externalization

```text
Versioning
Provenance
Award
Outcome Declaration
Export
Publication
```

Principal familiarity pressure: technical version/audit concepts, winner/award calculation, declaration/result/report, export/snapshot/download, publish/release/delivery.

Cross-family mechanisms and mapped terms such as Readiness, Remaining Work, Coverage, Aggregate, Rank and Reconciliation are audited later for false familiarity and expectation transfer without promoting them to Concepts.

# 12. Approved Phase-014 subphase sequence

| Group | Topic | Purpose / dependency |
| --- | --- | --- |
| **014-A** | Familiarity, Reuse & Genericity Scope, Criteria, Evidence & Subphase Planning | Start gate; defines criteria, evidence and sequence. |
| **014-B** | Familiarity Evidence Baseline, Precedent Taxonomy & Comparison Register | Establish concrete comparison candidates/sources and uncertainty before judging individual Concepts. |
| **014-C** | Competition, Competitor, Grouping, Identity, Participation, Alias & Access Familiarity/Reuse Audit | Audit Family 1 against 014-B precedents and expectation transfer. |
| **014-D** | Evaluation Occurrence, Obligation, Rubric & Scorecard Familiarity/Reuse Audit | Audit Family 2 after context/responsibility distinctions are explicit. |
| **014-E** | Versioning, Provenance, Award, Outcome Declaration, Export & Publication Familiarity/Reuse Audit | Audit Family 3 and officiality/externalization expectation transfer. |
| **014-F** | Cross-Catalog False Familiarity, Terminology & Expectation-Transfer Audit | Reconcile names/actions/states across all Concepts, mechanisms and mapped profiles after family audits. |
| **014-G** | Broader Genericity, Parameterization, Duplication & Specialization-Pressure Audit | Test safe generalization only after actual familiarity fit/misfit is known. |
| **014-H** | Retained Novelty, Reusable Concept-Knowledge & Catalog-Candidate Audit | Justify necessary novelty and identify reusable lessons without duplicating current truth. |
| **014-I** | Refinement Propagation, Reopen/Repair Decisions & Obvious Integrity Check | Apply/route adopted changes, repair obvious breakage and prepare one coherent post-refinement design. |
| **014-J** | Phase 014 Consolidation, Documentation-Integrity Audit, Exit Review & Phase 015 Handoff | Final reconciliation and decision before whole-system integrity/interference analysis. |

# 13. Dependency rationale

The sequence is deliberate:

```text
criteria
  → concrete precedent evidence
  → family-level semantic comparisons
  → cross-catalog terminology / false-familiarity synthesis
  → broader genericity
  → novelty / reusable-knowledge disposition
  → propagation / obvious repair
  → exit review
```

Do not generalize first and search for familiarity afterward; that would reward abstraction for its own sake.

Do not rename first and test semantic transfer afterward; that risks false familiarity.

Do not create catalog artifacts before retained novelty/reuse has been justified.

# 14. Subphase completion obligations

Each substantive 014-B through 014-I record should identify, as applicable:

- subjects under review;
- comparison precedent/source;
- expected familiar mental model;
- semantic matches and mismatches;
- false-familiarity risk;
- reuse/generalization candidate or rejection;
- retained novelty rationale;
- affected canonical owners;
- reopen/propagation requirement;
- unresolved subtle integrity question for Phase 015.

A comparison matrix is permitted where useful but is not mandatory.

# 15. Reopen discipline

Phase 014 distinguishes critique from authority change.

A finding may be resolved locally only when current semantics remain valid and the issue is naming, explanatory familiarity, broader safe genericity or reusable knowledge.

Explicitly reopen/route when:

- the current Concept purpose or boundary is wrong;
- the current behavior cannot satisfy its stated purpose;
- composition/action semantics are missing or contradictory;
- current dependence/PF-01 scope is invalidated;
- mapping semantics materially misrepresent the current design.

Do not silently change upstream semantics inside a familiarity record.

# 16. Risk register

Phase 014 begins with these risks:

- **FRG-R01 — Name-equals-fit:** familiar terminology accepted without behavioral comparison.
- **FRG-R02 — Popularity bias:** common industry patterns treated as authority.
- **FRG-R03 — False familiarity:** familiar precedent imports wrong lifecycle/authority/history expectations.
- **FRG-R04 — Implementation reuse leakage:** libraries/frameworks/services influence conceptual reuse decisions.
- **FRG-R05 — Over-generalization:** abstraction weakens purpose, domain meaning or mental model.
- **FRG-R06 — Similarity merge:** distinct Concepts merged because state/action shapes resemble each other.
- **FRG-R07 — Under-generalization:** incidental MUDAC-specificity retained without semantic need.
- **FRG-R08 — Catalog duplication:** reusable-knowledge work creates parallel canonical specifications.
- **FRG-R09 — Novelty without justification:** distinct Concepts retained without explaining why familiar alternatives fail.
- **FRG-R10 — Mapping drift after rename/generalization:** canonical Experience terminology not propagated.
- **FRG-R11 — Scope/composition breakage:** familiarity refinement silently invalidates Phase 011/012 decisions.
- **FRG-R12 — Profile conflation:** reuse across Judge/Organizer/Public contexts becomes capability or disclosure union.
- **FRG-R13 — Historical-adapter revival:** Encounter/Official Outcome Revision return because they appear familiar.
- **FRG-R14 — Taxonomy for taxonomy's sake:** speculative universal hierarchy introduced without reusable evidence.
- **FRG-R15 — Integrity deferral abuse:** known contradiction deferred to Phase 015 instead of repaired in Phase 014.

# 17. Exit evidence planned for 014-J

Phase 014 may exit only when 014-J can demonstrate that:

- all materially important Concepts received deliberate familiarity/reuse consideration;
- adopted familiar concepts/terms are semantically compatible rather than merely similarly named;
- known false familiarity is corrected or explicitly avoided;
- broader genericity opportunities were tested without weakening purpose/authority/history;
- retained novelty has concise justification where familiar alternatives plausibly exist;
- reusable concept knowledge is preserved without duplicate current truth;
- adopted substitutions/generalizations/renames are propagated to natural canonical owners;
- obvious breakage introduced by refinements is repaired before Phase 015;
- terminology, indexes, links and supersession state remain coherent;
- no implementation/architecture reuse decisions entered design authority;
- Phase 015 can begin from one coherent current design rather than reconstructing alternatives.

# 18. Documentation and OKF plan

Phase records retain:

- precedent comparisons;
- rejected substitutions;
- failed generalizations;
- novelty rationale detail;
- tentative catalog hypotheses.

Canonical owners retain only adopted current semantics and concise reusable constraints where genuinely useful.

Historical adapters remain historical.

Do not create a second concept catalog that duplicates `docs/canonical/concepts/`.

# 19. Implementation state

```text
architecture authority: SUSPENDED
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

Phase 014 is design-only. Successful completion hands off to Phase 015 whole-system Concept Integrity / Cross-Concept Coherence & Interference analysis, not architecture or implementation.

# Start-gate outcome

**014-A COMPLETE — READY. Proceed to 014-B — Familiarity Evidence Baseline, Precedent Taxonomy & Comparison Register.**
