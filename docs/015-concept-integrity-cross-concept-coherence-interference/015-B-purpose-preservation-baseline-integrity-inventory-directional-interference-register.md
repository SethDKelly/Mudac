---
type: Phase Design Record
title: 015-B — Purpose-Preservation Baseline, Integrity Inventory & Directional Interference Register
description: "Establishes the Phase-015 purpose-preservation baseline for all eighteen Concepts, maps purpose obligations/invariants/tensions, creates a directional interference candidate register, and proves cluster coverage before substantive integrity disposition begins."
status: stable
tags: [phase-015, integrity, purpose-preservation, inventory, interference, directional, register]
sources:
  - resource: 015-A-integrity-audit-scope-interference-surfaces-whole-system-coverage-subphase-planning.md
  - resource: ../canonical/project/purpose-needs-success-tensions.md
  - resource: ../canonical/concepts/
  - resource: ../canonical/synchronizations/
  - resource: ../canonical/dependence/product-family-scope.md
  - resource: ../canonical/invariants/
  - resource: ../canonical/policies/
  - resource: ../canonical/experience/mapping-authority-baseline.md
  - resource: ../canonical/project/domain-vocabulary-expectation-transfer.md
  - resource: ../canonical/project/reusable-design-knowledge.md
---

# Purpose

Create the Phase-015 integrity baseline before any cluster-level integrity verdicts are made.

015-B answers:

1. What purpose promise must remain true for each of the eighteen retained Concepts?
2. Which product-purpose obligations, invariants and tensions make that promise materially important?
3. Which external Concepts, synchronizations, mechanisms, mappings or Phase-014 refinements can plausibly interfere with it?
4. Where will each directional interference candidate be examined?
5. Does the approved 015-C–I plan cover every materially important Concept and cross-family chain?

This record is an **integrity planning/evidence register**, not a second source of Concept semantics.

# Decision

**015-B COMPLETE — PASS. Proceed to 015-C.**

```text
current Concepts                         18
Concepts with purpose baseline           18 / 18
Concepts with directional interference   18 / 18
P-01–P-09 coverage                       COMPLETE
INV-001–INV-010 coverage                 MAPPED
T-01–T-10 relevance                      MAPPED
confirmed integrity violations           NONE — not dispositioned here
upstream semantic reopen                 NONE
documentation repair                     NONE REQUIRED
NEXT                                     015-C
```

015-B deliberately does **not** treat an interference candidate as evidence that a violation exists.

# 1. Baseline interpretation

For each Concept, Phase 015 protects the current canonical purpose rather than inventing a new whole-system purpose.

```text
Concept purpose owner
  = canonical Concept file

P-* obligation owner
  = canonical Project Purpose

015-B
  = concise integrity subject baseline
    + interference planning evidence
```

If this record and a current canonical owner differ, the canonical owner wins and this register must be reconciled.

# 2. Product-purpose obligations

The current integrity baseline uses:

- **P-01 — Independent human judgment**
- **P-02 — Fair and bias-aware Team treatment**
- **P-03 — Low-friction and accessible participation**
- **P-04 — Live operational coordination and completion**
- **P-05 — Resilient evaluation continuity**
- **P-06 — Trustworthy and explainable outcome formation**
- **P-07 — Correctable authority and historical truth**
- **P-08 — Contextual confidentiality and authority separation**
- **P-09 — Faithful external representation and controlled release**

No Phase-015 finding may improve one obligation by silently defeating another while both promises remain current.

# 3. Integrity subject inventory

The statements below are concise **purpose-preservation tests**, not replacement specifications.

| Concept | Purpose promise that must survive composition | Principal P-* obligations | Principal integrity constraints | Primary audit |
| --- | --- | --- | --- | --- |
| Competition | One competition occurrence retains an honest lifecycle/governing context without absorbing outcome or other domain authority | P-04, P-06, P-07 | COMP-001/002; T-05, T-07 | 015-C, 015-F |
| Division | Current competitive cohort assignment remains truthful without rewriting historical evaluation/presentation context or becoming Rank authority | P-02, P-06, P-07 | INV-005; T-06, T-07 | 015-C |
| Team | One scoped competing group remains the stable competing unit while Division/Alias/evaluation/outcome relationships stay externally owned | P-02, P-06 | Phase-014 Team genericity; T-02, T-06 | 015-C, 015-I |
| Panel | Intended reusable evaluator grouping remains distinct from actual occurrence participation, responsibility and evidence | P-03, P-04 | grouping/responsibility seam; T-01, T-04 | 015-C, 015-D |
| Evaluation Occurrence | What actually happened in one bounded evaluation remains truthful and historically stable even when grouping, responsibility or eligibility changes later | P-01, P-04, P-05, P-07 | INV-005, INV-008; T-04, T-07 | 015-D, 015-E |
| Evaluation Obligation | One evaluator's responsibility remains attributable and historically truthful without inventing judgment, reopening terminal work or conflating satisfaction with current eligibility | P-01, P-02, P-04, P-05, P-07 | INV-002, INV-003, INV-005; T-04, T-06, T-07 | 015-D, 015-E, 015-F |
| Rubric | Evaluation semantics remain stable for the exact supplied basis and historical responses are never silently reinterpreted by later Rubric change | P-01, P-02, P-06, P-07 | INV-003, INV-005; T-05, T-07 | 015-D, 015-E |
| Scorecard | One evaluator's independent judgment retains Draft/authority, fixed structural identity, authorship and legitimate successor-correction semantics | P-01, P-03, P-05, P-06, P-07 | INV-001, 002, 004, 005, 008, 010; T-01, T-04, T-07, T-09 | 015-D, 015-E, 015-F |
| Award | Explicit recognition remains owned by Award and is not silently equated with Rank, officiality or publication | P-02, P-06, P-07 | INV-005, INV-006; T-05, T-06, T-07 | 015-F |
| Identity | Human continuity remains distinct from current capacity, Access and event authority | P-03, P-08 | authority separation; T-01, T-03, T-08 | 015-C |
| Participation | Scope/capacity-limited involvement remains distinct from Identity, Access, Panel grouping and semantic authorship | P-03, P-04, P-08 | no capability union; T-01, T-03, T-08 | 015-C, 015-D |
| Alias | Context-specific alternate identity remains usable for bias control without becoming permanent identity, authentication or Access authority | P-02, P-08 | INV-005; T-02, T-09 | 015-C |
| Access | Contextual capability/disclosure remains distinct from identity, capacity and semantic authorship/decision authority | P-01, P-03, P-05, P-08 | INV-001, INV-004, INV-010; T-03, T-08, T-09 | 015-C, 015-D, 015-G |
| Versioning | Immutable authoritative snapshots/current eligibility remain truthful without deciding domain legitimacy or silently reviving predecessors | P-05, P-07 | INV-005; T-07 | 015-E |
| Provenance | Origin/transformation/actor/represented-authority explanation remains truthful without becoming Versioning or low-level telemetry | P-05, P-06, P-07, P-08 | INV-004, INV-005, INV-008; T-04, T-07, T-08 | 015-E |
| Outcome Declaration | Explicit official authority over an exact basis remains distinct from calculation, Competition lifecycle, recognition, Export and Publication; Affected remains honest until successor confirmation | P-06, P-07, P-09 | INV-005, INV-006, INV-007; T-05, T-07, T-10 | 015-F, 015-G |
| Export | Stable exact-source representation retains honest source/currentness relation without promoting authority or becoming release authority | P-06, P-07, P-09 | INV-005, INV-007; T-07, T-10 | 015-G |
| Publication | Deliberate release retains exact representation/audience/history without promoting source authority or implying distributed copies disappeared | P-09 | INV-005, INV-007; T-10 | 015-G |

# 4. Purpose-obligation coverage

The Concept inventory covers every current product-purpose obligation through multiple independent owners.

| Purpose obligation | Principal integrity subjects |
| --- | --- |
| P-01 Independent human judgment | Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Access |
| P-02 Fair/bias-aware Team treatment | Team, Division, Alias, Evaluation Obligation, Rubric, Award |
| P-03 Low-friction/accessibility | Identity, Participation, Access, Scorecard |
| P-04 Live coordination/completion | Competition, Panel, Evaluation Occurrence, Evaluation Obligation, Participation |
| P-05 Resilient continuity | Evaluation Occurrence, Evaluation Obligation, Scorecard, Access, Versioning, Provenance |
| P-06 Explainable outcome formation | Competition, Division, Rubric, Scorecard, Award, Provenance, Outcome Declaration, Export |
| P-07 Correctable authority/history | Competition, Division, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Award, Versioning, Provenance, Outcome Declaration, Export |
| P-08 Confidentiality/authority separation | Identity, Participation, Alias, Access, Provenance |
| P-09 External representation/release | Outcome Declaration, Export, Publication |

This table expresses **integrity accountability**, not exclusive ownership of a purpose.

# 5. Invariant coverage map

The current cross-cutting invariants become explicit Phase-015 probe anchors.

| Invariant | Principal Phase-015 subjects |
| --- | --- |
| INV-001 Judge Independence | Alias, Access, Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, derived views |
| INV-002 One Logical Evaluation per Evaluation Obligation | Evaluation Obligation, Scorecard, successor responsibility/correction |
| INV-003 Missing Is Never Zero | Evaluation Obligation, Rubric semantics, Scorecard, Coverage/Aggregate |
| INV-004 Organizer Does Not Become Judge Author | Participation, Access, Scorecard, Provenance, capture/correction |
| INV-005 Current vs Historical Truth | Division, Alias, Occurrence, Obligation, Scorecard, Award, Versioning, Provenance, Outcome Declaration, Export, Publication |
| INV-006 Calculated Is Not Declared Official | Coverage, Aggregate, Rank, Award, Competition, Outcome Declaration |
| INV-007 Official Is Not Automatically Public | Outcome Declaration, Export, Publication, disclosure profiles |
| INV-008 Capture-Channel Parity | Occurrence, Obligation, Scorecard, Provenance, accessibility/degraded paths |
| INV-009 Accessibility Semantic Parity | Participation, Access, Scorecard, all combined Experience actions |
| INV-010 Truthful Authority Under Uncertainty | Scorecard persistence/finalization, coordinated actions, recovery, officiality/externalization |

# 6. Tension coverage map

The current P/T baseline is intentionally not flattened into a priority score.

| Tension | Primary Phase-015 surfaces |
| --- | --- |
| T-01 friction vs attribution | Identity, Participation, Scorecard authorship |
| T-02 shielding vs explainability | Team, Alias, Division, occurrence history |
| T-03 Judge privacy vs Organizer oversight | Participation, Access, live/reconciliation views |
| T-04 resilience/capture vs singular authority | Occurrence, Obligation, Scorecard, Provenance |
| T-05 speed vs outcome correctness | Competition closeout, Coverage/Rank/Award/Declaration |
| T-06 exception handling vs Team consistency | Obligation/Coverage exceptions, Division/Team outcome treatment |
| T-07 correctability vs immutability | Versioning, Provenance, correction, Award, Declaration, Export/Publication |
| T-08 accessibility/continuity vs confidentiality | Access, identity context, degraded/paper/recovery |
| T-09 live visibility vs independent judgment | Alias, Access, derived standings/results |
| T-10 transparency vs controlled disclosure/currentness | Outcome Declaration, Export, Publication |

A later finding must explain why a tension remains an intentional bounded trade-off or crosses into a broken Concept promise.

# 7. Directional interference register

The following entries are **planned probes**, not findings.

Status legend:

- **OPEN-C** → disposition in 015-C;
- **OPEN-D** → disposition in 015-D;
- **OPEN-E** → disposition in 015-E;
- **OPEN-F** → disposition in 015-F;
- **OPEN-G** → disposition in 015-G;
- **OPEN-H** → cross-family recheck in 015-H;
- **OPEN-I** → combined mapping/profile/refinement recheck in 015-I.

## A. Competition context / actor / competitor structure

| ID | Interfering source → subject promise | Candidate concern | Lens | Owner phase |
| --- | --- | --- | --- | --- |
| DIR-001 | Competition lifecycle → Participation | Competition transitions may implicitly broaden/narrow Participation beyond its capacity-limited purpose | S01/S05/S06 | OPEN-C |
| DIR-002 | Competition + Participation lifecycle → Access | broad live-event capability may close while narrow pre-existing responsibility remains; avoid both hidden revocation and accidental reactivation | S01/S05/S06 | OPEN-C |
| DIR-003 | Identity reuse → Participation | returning identity could be mistaken for resumed event participation/capacity | S06/S10 | OPEN-C |
| DIR-004 | Participation/capacity → Identity | role/capacity state could overwrite or fragment stable human continuity | S03/S06 | OPEN-C |
| DIR-005 | Panel membership → Evaluation Occurrence / Obligation | intended evaluator grouping could be mistaken for actual participation or responsibility | S02/S06/S10 | OPEN-C/D |
| DIR-006 | Team/Division/Alias current correction → Evaluation Occurrence | current competitor metadata/identity may overwrite historical PresentedContext | S03/S05 | OPEN-C/D |
| DIR-007 | Alias resolution/disclosure → Team confidentiality | alternate identity may fail its bias-control purpose if neighboring Access/profile behavior leaks underlying identity | S06/S08 | OPEN-C/I |
| DIR-008 | Access/technical privilege → semantic domain authority | permission or support capability may be interpreted as Judge/Organizer authorship/decision authority | S06/S08 | OPEN-C/H/I |
| DIR-009 | Phase-014 Team genericity → Division/Alias/evaluation/outcome composition | broader intrinsic competing-group wording could omit a purpose-significant PF-01 assumption needed by neighbors | S09/S10 | OPEN-C/I |

## B. Evaluation occurrence / responsibility / basis / judgment

| ID | Interfering source → subject promise | Candidate concern | Lens | Owner phase |
| --- | --- | --- | --- | --- |
| DIR-010 | Evaluation Occurrence completion → Evaluation Obligation | occurrence ending could incorrectly imply individual responsibility ended | S03/S05 | OPEN-D |
| DIR-011 | Evaluation Obligation lifecycle → Evaluation Occurrence | reassignment/satisfaction could rewrite who actually participated in the occurrence | S03/S05 | OPEN-D |
| DIR-012 | Evaluation Obligation status → Scorecard | Satisfied/Outstanding could be mistaken for judgment authority/content state | S03/S06 | OPEN-D |
| DIR-013 | Scorecard Finalization → Evaluation Obligation | finalization composition could satisfy the wrong obligation or multiply logical evaluation weight | S02/S04/S06 | OPEN-D |
| DIR-014 | Rubric current definition → historical Scorecard/Occurrence | later Rubric change could silently reinterpret exact historical basis | S03/S05 | OPEN-D/E |
| DIR-015 | reassignment/substitution → Scorecard authorship | operational replacement could transfer authorship or mutate structural Scorecard identity | S05/S06 | OPEN-D/E |
| DIR-016 | paper/assisted capture → Scorecard authorship | capture actor could appear to become semantic Judge | S06/S08 | OPEN-D/E/I |
| DIR-017 | Access change → existing Scorecard work | confidentiality/lifecycle constraints may destroy legitimate continuity or, conversely, expose broader evaluation history | S01/S05/S06 | OPEN-D |

## C. Correction / Versioning / Provenance / historical truth

| ID | Interfering source → subject promise | Candidate concern | Lens | Owner phase |
| --- | --- | --- | --- | --- |
| DIR-018 | Scorecard amendment/capture correction → Versioning | successor-state mechanics could erase distinction between legitimate semantic amendment and source-faithful correction | S03/S05/S10 | OPEN-E |
| DIR-019 | Versioning currentness → domain correction semantics | generic supersession/invalidation might be treated as authority to decide whether a domain correction is legitimate | S06/S10 | OPEN-E |
| DIR-020 | Occurrence invalidation → Obligation history | ineligible occurrence could incorrectly reopen historically Satisfied obligations | S03/S05 | OPEN-E |
| DIR-021 | Occurrence/basis/evidence invalidation → Scorecard | external invalidation could destructively rewrite judgment history rather than affect eligibility | S03/S05 | OPEN-E |
| DIR-022 | evidence ineligibility → successor responsibility | correction propagation could automatically manufacture a new obligation without deliberate authority | S02/S06/S07 | OPEN-E/H |
| DIR-023 | Provenance actor/represented-authority data → Scorecard authorship | explanatory metadata could conflict with or overwrite semantic authorship rather than explain it | S03/S06 | OPEN-E |
| DIR-024 | Provenance correction → historical authority | fixing explanatory evidence could be mistaken for rewriting the underlying authoritative state/history | S03/S05 | OPEN-E |
| DIR-025 | Access revocation/completion → retained Version/Provenance | loss of current capability could be mistaken for deletion/loss of retained historical authority | S03/S05/S08 | OPEN-E/I |

## D. Evidence sufficiency / calculation / recognition / officiality

| ID | Interfering source → subject promise | Candidate concern | Lens | Owner phase |
| --- | --- | --- | --- | --- |
| DIR-026 | evidence eligibility change → Coverage/Aggregate/Rank | derived state may remain misleadingly current after upstream correction | S03/S05/S07 | OPEN-F/H |
| DIR-027 | exception disposition → Coverage | Organizer exception authority could rewrite factual sufficiency instead of governing what to do about it | S02/S06 | OPEN-F |
| DIR-028 | missing obligation/evidence → Aggregate/Rank | missing may be flattened into zero or silently excluded in a way that changes Team treatment | S03/S04 | OPEN-F |
| DIR-029 | Rank → Award | calculated ordering could silently confer recognition | S02/S06 | OPEN-F |
| DIR-030 | Rank change → existing Award | new calculation could silently move/revoke recognized achievement | S03/S05/S06 | OPEN-F |
| DIR-031 | Award correction → Outcome Declaration | official basis may remain falsely current or silently change when recognition changes | S03/S05 | OPEN-F |
| DIR-032 | evidence/policy correction → Outcome Declaration | official declaration may fail to become Affected or may be silently replaced without explicit successor | S03/S05/S06 | OPEN-F |
| DIR-033 | Competition Finalization → Outcome Declaration | lifecycle closure could be mistaken for officiality, or declaration correction could be mistaken for Competition reopen | S02/S03/S06 | OPEN-F |
| DIR-034 | derived readiness/calculation → officiality | readiness, Aggregate or Rank may acquire declaration authority through combined closeout mapping | S06/S08/S13 | OPEN-F/I |

## E. External representation / release

| ID | Interfering source → subject promise | Candidate concern | Lens | Owner phase |
| --- | --- | --- | --- | --- |
| DIR-035 | Outcome Declaration/source change → Export | representation may remain misleadingly Current after bound source becomes materially affected | S03/S05 | OPEN-G |
| DIR-036 | Export generation/currentness → source authority | rendered output may appear to promote provisional/non-official source state | S06/S08 | OPEN-G/I |
| DIR-037 | Export currentness → Publication | source/representation currentness changes may silently publish, withdraw or retarget release | S02/S05/S06 | OPEN-G |
| DIR-038 | Publication state → Export/source currentness | Published/Withdrawn could be mistaken for evidence that representation/source is current or invalid | S03/S08 | OPEN-G |
| DIR-039 | Publication withdrawal → external possession | current distribution closure could be represented as recall/deletion of already distributed copies | S03/S05/S08 | OPEN-G/I |
| DIR-040 | actor Access → audience disclosure | interactive permission could be mistaken for permission to include/release the same information externally | S06/S08 | OPEN-G/I |
| DIR-041 | successor Declaration → successor Export/Publication | official correction could silently rewrite or auto-replace historical external representations/releases | S05/S07 | OPEN-G/H |

## F. Whole-system action / mapping / profile candidates

| ID | Interfering source → subject promise | Candidate concern | Lens | Owner phase |
| --- | --- | --- | --- | --- |
| DIR-042 | coordinated application action → participant Concepts | one UI/business action may hide distinct authority-bearing effects or make optional semantic steps appear inseparable | S02/S07/S08 | OPEN-H/I |
| DIR-043 | system-triggered currentness propagation → authority owners | automation may cross from propagating known facts into manufacturing discretionary authority | S06/S07 | OPEN-H |
| DIR-044 | correction chain → Award/Declaration/Export/Publication | a long dependency chain may leave downstream states stale or over-automate successor authority | S03/S05/S07 | OPEN-H |
| DIR-045 | cross-role/profile mapping → Participation/Access | switching Judge/Organizer/support/public contexts may union capabilities or disclosures | S06/S08/S09 | OPEN-I |
| DIR-046 | familiar generic verbs/statuses → owner-specific semantics | Complete/Final/Submit/Winner/Result/Publish/Share language may collapse distinct lifecycle/authority meanings only in composed views | S08/S10 | OPEN-I |
| DIR-047 | accessible/degraded/paper mapping → semantic owners | adaptation may reduce information/control in a way that changes authorship, authority or uncertainty meaning | S01/S06/S08/S09 | OPEN-I |
| DIR-048 | uncertainty/recovery mapping → authoritative state | retry/resume/recovery may visually promote unknown persistence or stale local state into confirmed authority | S03/S08 | OPEN-I |

# 8. Directional coverage by Concept

Every Concept appears as a **subject whose promise can be threatened**, not merely as a source of interference.

| Concept | Register examples |
| --- | --- |
| Competition | DIR-033 plus 015-C lifecycle review |
| Division | DIR-006, DIR-009 |
| Team | DIR-007, DIR-009, DIR-028 |
| Panel | DIR-005 and inverse grouping-history probes in 015-C |
| Evaluation Occurrence | DIR-005, DIR-006, DIR-011, DIR-021 |
| Evaluation Obligation | DIR-010, DIR-013, DIR-020, DIR-022 |
| Rubric | DIR-014 plus exact-basis correction probes |
| Scorecard | DIR-012, DIR-013, DIR-015–018, DIR-021, DIR-023 |
| Award | DIR-029, DIR-030, DIR-044 |
| Identity | DIR-004 plus multi-capacity/profile probes |
| Participation | DIR-001, DIR-003, DIR-045 |
| Alias | DIR-006 plus resolution/disclosure profile probes |
| Access | DIR-002, DIR-017, DIR-045 |
| Versioning | DIR-018, DIR-019 |
| Provenance | DIR-023, DIR-024 |
| Outcome Declaration | DIR-031–034, DIR-041, DIR-044 |
| Export | DIR-035–038, DIR-041, DIR-044 |
| Publication | DIR-037–039, DIR-041, DIR-044 |

This fulfills 015-A's requirement that no Concept be omitted because interference seems unlikely.

# 9. Cluster coverage proof

The register routes candidates into the approved substantive phases:

```text
015-C
  → DIR-001 through DIR-009

015-D
  → DIR-005 and DIR-010 through DIR-017

015-E
  → DIR-014 through DIR-025

015-F
  → DIR-026 through DIR-034

015-G
  → DIR-035 through DIR-041

015-H
  → cross-family recheck of DIR-008, 022, 026, 041–044
    + any new chains discovered in C–G

015-I
  → mapping/profile/refinement recheck of
    DIR-007–009, 016, 025, 034, 036, 039–040, 042, 045–048
```

The ranges intentionally overlap. Interference can be discovered locally and still require later whole-system re-evaluation.

# 10. Finding register contract

Later phases may promote a directional candidate into a material finding.

Use IDs:

```text
INT-F001, INT-F002, ...
```

A finding must record:

- source DIR-* candidate(s), if applicable;
- subject Concept;
- current purpose/purpose obligation;
- interfering source;
- PF-01 context/profile;
- interference lens;
- counterexample/evidence;
- consequence to purpose;
- disposition;
- natural correction owner;
- propagation/re-audit scope;
- current resolution state.

A DIR-* entry is **not** itself an INT-F finding.

# 11. Initial disposition discipline

015-B makes only these baseline conclusions:

1. all eighteen Concepts have stable enough current purpose definitions for integrity audit;
2. every P-01–P-09 obligation has material Concept coverage;
3. every INV-001–INV-010 has an explicit Phase-015 probe surface;
4. every T-01–T-10 has a planned integrity context;
5. all eighteen Concepts have directional external-interference candidates;
6. the 015-C–I sequence covers the current known surfaces;
7. no prerequisite semantic contradiction is established by building the inventory.

```text
candidate exists
  != integrity violation exists

many candidates around one Concept
  != Concept is poorly designed

few candidates
  != integrity proven
```

# 12. Derived mechanisms and work contexts

Coverage, Aggregate, Rank and Readiness remain derived mechanisms. Reconciliation and Live Operations remain process/work contexts.

Phase 015 nevertheless audits their **interference effects** because a non-Concept can still make a Concept's promise misleading.

Preserve:

```text
derived mechanism
  != semantic authority owner

work context
  != lifecycle owner

integrity relevance
  != promotion to Concept
```

# 13. Phase-014 refinement coverage

The directional register explicitly includes:

- Team broader intrinsic genericity — DIR-009;
- familiar vocabulary under composition — DIR-046;
- exact-basis binding — DIR-014/018/021;
- successor-without-rewrite — DIR-018–024, DIR-032, DIR-041;
- actor/represented-authority/source — DIR-016/023/024;
- historical accomplishment/current eligibility — DIR-020–022/026;
- derivation→recognition→declaration — DIR-029–034;
- source→representation→release→delivery — DIR-035–041;
- context capability without authorship transfer — DIR-002/008/017/040/045.

Thus Phase-014 refinements cannot disappear from Phase-015 coverage merely because they were already locally accepted.

# 14. No all-pairs matrix requirement

An 18×18 all-pairs matrix would create false completeness.

Phase 015 instead requires:

- every Concept as an integrity subject;
- every materially plausible directional interference;
- cluster-level analysis for chained effects;
- re-opening the register whenever C–I discovers a new direction.

The register is **open to expansion** until 015-J closure.

# 15. Implementation boundary

Nothing in this inventory authorizes architecture or implementation work.

Terms such as stale, retry, recovery, currentness, propagation or chain are used semantically.

```text
directional interference != service dependency
currentness != cache coherency
historical truth != transaction isolation
authority != authorization middleware
counterexample != executable test
```

# Exit

**015-B COMPLETE — PASS.**

Proceed to **015-C — Competition Context, Competitor Structure, Identity, Participation, Alias, Access & Panel Integrity**.
