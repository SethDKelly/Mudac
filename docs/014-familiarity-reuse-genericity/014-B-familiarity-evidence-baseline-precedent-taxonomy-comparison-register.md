---
type: Phase Design Record
title: 014-B — Familiarity Evidence Baseline, Precedent Taxonomy & Comparison Register
description: "Establishes the Phase-014 familiarity evidence hierarchy, precedent taxonomy, uncertainty discipline and concept-by-concept comparison register used by later familiarity/reuse audits without prematurely declaring semantic fit."
status: stable
tags: [phase-014, jackson, familiarity, reuse, precedent, taxonomy, comparison, evidence]
sources:
  - resource: 014-A-familiarity-reuse-genericity-scope-criteria-evidence-subphase-planning.md
  - resource: ../009-jackson-methodology-realignment/009-B-jackson-base-lifecycle-crosswalk-evidence-reuse-gap-map.md
  - resource: ../007-design-refinement/007-B-concept-completeness-independence-genericity-audit.md
  - resource: ../canonical/concepts/
  - resource: ../canonical/synchronizations/
  - resource: ../canonical/dependence/
  - resource: ../canonical/experience/mapping-authority-baseline.md
  - resource: ../canonical/experience/action-authority-traceability.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/008/phase-definition.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/008/familiarity-reuse-contract.md
---

# Purpose

Establish the comparison evidence and precedent vocabulary that Phase 014 will use before judging whether any current MUDAC Concept is familiar, reusable, falsely familiar, unnecessarily specialized or intentionally novel.

014-B is deliberately **evidence-forming, not disposition-forming**.

It answers:

- what kinds of familiarity evidence are trustworthy;
- which precedent families are plausible for MUDAC;
- which familiar expectations each precedent family tends to import;
- which concrete precedents should be tested against each of the eighteen current Concepts;
- which cross-cutting mechanisms/mapped terms require expectation-transfer review even though they are not Concepts;
- where precedent meaning is ambiguous enough that later phases must resist casual analogy.

It does **not** rename, merge, generalize, replace or catalog-promote any Concept.

# Decision

**COMPLETE — PASS. Proceed to 014-C.**

```text
014-A start gate                              COMPLETE — READY
014-B evidence / precedent baseline           COMPLETE — PASS
all 18 Concepts registered for comparison    YES
derived/work-context terms registered         YES
specific semantic-fit dispositions made       NO
Concept rename / merge / replacement           NONE
upstream reopen required                       NO
architecture / implementation influence        PROHIBITED
NEXT                                            014-C
```

# 1. Familiarity evidence is about expectation transfer

The central evidence question remains:

> If someone already understands the proposed familiar precedent, which expectations would they transfer to the MUDAC subject, and how likely are those expectations to be correct?

A precedent is therefore useful only when later comparison can inspect meaningful semantics such as:

```text
purpose
operational principle
state
actions / effects
lifecycle / reversibility
ownership / authority / authorship
history / correction / retention
scope / target
composition / automation
user-visible mapping / disclosure
```

Name similarity, popularity, visual resemblance or implementation analogy alone is not familiarity evidence.

# 2. Evidence hierarchy

Phase 014 uses the following evidence order.

## E1 — Current MUDAC semantic authority

Highest authority for what MUDAC currently means:

- Project Purpose / Mandate;
- current Concept owners;
- synchronization/application-action owners;
- dependence/PF-01 owners;
- policies/invariants;
- completed Phase-013 Experience owners.

A familiar precedent is always compared **to E1**, never substituted for E1 merely because it is conventional.

## E2 — Authoritative Concept Design precedents / documented concept definitions

Strong comparison evidence includes documented concept definitions, behavioral case studies and mature concept-design literature where purpose/actions/state are explicit.

Daniel Jackson / Base concept material belongs here.

E2 can establish what a precedent means; it cannot decide that MUDAC should adopt it.

## E3 — Established domain concepts and institutional vocabulary

Competition/judging/governance/publication concepts with relatively stable domain expectations are useful comparison evidence when the behavioral meaning is sufficiently clear.

Examples include:

- competition / division / team / judging panel;
- rubric / scorecard;
- award / recognition;
- official declaration / certification;
- publication / withdrawal / supersession.

Domain familiarity may still vary across institutions and must be tested rather than assumed.

## E4 — Widely used cross-application software concepts

Useful but frequently ambiguous precedents include:

- identity / account / principal;
- membership / enrollment / participation;
- role / permission / entitlement / access;
- alias / pseudonym / display name;
- assignment / task / obligation;
- version / revision / snapshot;
- provenance / audit trail / lineage;
- export / report / artifact;
- publish / release / distribute.

Because applications often use these words differently, E4 candidates require especially explicit false-familiarity testing.

## E5 — MUDAC historical alternatives and prior audits

Historical MUDAC concepts and design records are evidence of alternatives already considered, boundary pressure and prior expectation language.

Examples include:

- `Judging Encounter`;
- `Official Outcome Revision`;
- Publication's historical promotion out of Export;
- earlier genericity findings from Phase 007.

E5 is useful for counterexamples and design lineage. It does not become current authority and must not restore superseded models by familiarity alone.

## E6 — Comparable product/interface convention

A common application pattern, UI term or competitor convention may suggest a comparison candidate, but is weak evidence until its actual semantic behavior is established.

Use it to generate hypotheses, never to justify adoption directly.

## E7 — Historical architecture / implementation

Quarantined architecture or implementation can reveal terminology people may encounter or assumptions that contaminated earlier design.

It is **not** familiarity authority and may only be used as a contamination probe or historical expectation source.

# 3. Precedent-definition confidence

Not every familiar term has one stable meaning.

Each later comparison should classify the precedent evidence as one of:

- **Defined** — purpose/behavior is explicitly documented enough for semantic comparison;
- **Domain-stable** — meaning is broadly stable in the relevant domain, with known variation;
- **Conventionally familiar but variable** — common term whose authority/lifecycle semantics differ substantially by application;
- **Loose analogy** — useful explanatory resemblance, not a sufficiently defined concept candidate;
- **Historical-project precedent** — useful MUDAC lineage evidence only.

A variable or loose precedent cannot support a strong reuse claim without a narrower definition.

# 4. Precedent taxonomy

The following taxonomy organizes comparison evidence without asserting a universal concept hierarchy.

## PT-01 — Bounded event / competition context

Typical precedents:

```text
Competition
Contest
Tournament
Event
Program / event instance
```

Typical imported expectations:

- bounded context;
- participant scope;
- lifecycle/start/end;
- rules/configuration;
- result or completion.

Primary risk: familiar event/container semantics may obscure MUDAC's explicit lifecycle authority and independent official-result declaration.

## PT-02 — Classification / competitor / grouping

Typical precedents:

```text
Category / Division / Class
Entrant / Competitor / Team
Panel / Committee / Jury
Cohort / Group
```

Typical expectations:

- grouping or membership;
- classification;
- planned association;
- sometimes delegated decision authority.

Primary risk: grouping language can falsely imply actual evaluation participation, responsibility or authority.

## PT-03 — Human identity / membership / capacity

Typical precedents:

```text
Person / User / Identity
Account
Principal
Membership
Enrollment / Registration
Participation
Role assignment
```

Typical expectations:

- stable human continuity;
- scoped relationship to a context;
- current/expired/withdrawn relationship;
- role/capacity.

Primary risk: account, membership, role and participation frequently collapse identity, relationship and capability that MUDAC intentionally separates.

## PT-04 — Alternate identity / authorization / disclosure

Typical precedents:

```text
Alias
Pseudonym
Display name
Anonymized identifier
Permission
Authorization decision
Entitlement
Capability
Access-control decision
```

Typical expectations:

- alternate representation of identity;
- hidden/resolved underlying identity;
- allowed/denied operation;
- revocation/expiration;
- target/action scope.

Primary risk: `Alias` may sound cosmetic, and `Access` may sound like a persisted RBAC grant even though MUDAC uses scoped bias-control identity and contextual access decisions.

## PT-05 — Bounded occurrence / session / attempt

Typical precedents:

```text
Session
Encounter
Assessment event
Attempt
Meeting
Review occurrence
```

Typical expectations:

- bounded happening;
- actual participants;
- time/context;
- completion/cancellation;
- possible replacement.

Primary risk: many precedents also imply responsibility or result ownership; MUDAC separates occurrence from obligation and Scorecard evidence.

## PT-06 — Responsibility / assignment / duty

Typical precedents:

```text
Assignment
Task
Duty
Obligation
Review assignment
Work item
```

Typical expectations:

- responsible actor;
- subject/work target;
- outstanding/completed/excused state;
- possibly reassignment.

Primary risk: generic task models often reopen or regenerate work automatically and may not preserve MUDAC's historical-satisfaction/current-evidence distinction.

## PT-07 — Evaluation instrument / criteria template

Typical precedents:

```text
Rubric
Scoring guide
Evaluation form/template
Criteria set
Questionnaire definition
```

Typical expectations:

- reusable definition;
- criteria/scales;
- working versus released version;
- bound instrument used for later responses.

Primary risk: form/template familiarity may encourage mutable-current-template semantics inconsistent with exact authoritative Evaluation Basis history.

## PT-08 — Authored judgment / ballot / response record

Typical precedents:

```text
Scorecard
Ballot
Evaluation
Assessment response
Submission
Review
Completed form
```

Typical expectations:

- one actor's authored response;
- Draft and submit/finalize behavior;
- possible amendment/history;
- counted/eligible result.

Primary risk: submission/form semantics may collapse Draft persistence, semantic Finalization, evidence eligibility and weighting.

## PT-09 — Version / history / provenance

Typical precedents:

```text
Version
Revision
Snapshot
History
Audit trail
Provenance
Lineage
Attribution record
```

Typical expectations:

- predecessor/successor history;
- retained prior state;
- authorship/origin/time;
- currentness/invalidity.

Primary risk: technical version-control and audit-log expectations may introduce generic user actions or equate revision history with domain semantic authority.

## PT-10 — Recognition / award

Typical precedents:

```text
Award
Prize
Recognition
Badge / honor
Winner designation
```

Typical expectations:

- definition/category;
- recipient;
- conferral authority;
- possible revocation/correction;
- sometimes calculated selection.

Primary risk: competition products often equate rank/winner calculation with Award conferral, which MUDAC explicitly separates.

## PT-11 — Declaration / certification / official record

Typical precedents:

```text
Declaration
Certified result
Official result
Attestation
Decision record
Certification
```

Typical expectations:

- explicit authoritative statement;
- identified declaring authority;
- effective/current result;
- correction/supersession history.

Primary risk: `result`, `report` or `finalized competition` may be mistaken for the declaration itself; publication may also be falsely implied.

## PT-12 — Representation / export / snapshot

Typical precedents:

```text
Export
Report
Snapshot
Rendered artifact
Extract
Materialized representation
```

Typical expectations:

- exact or selected representation of source state;
- generated output;
- format/audience purpose;
- possible staleness/currentness.

Primary risk: ordinary `export` often means a disposable file and does not carry stable SourceBasis/currentness semantics.

## PT-13 — Publication / release / distribution

Typical precedents:

```text
Publication
Publish
Release
Distribution
Announcement
```

Typical expectations:

- deliberate audience availability;
- publishing/releasing authority;
- channel/audience;
- withdrawal/supersession;
- sometimes delivery.

Primary risk: publishing is often conflated with file generation, public visibility or successful delivery; MUDAC separates all three.

# 5. Comparison register — Family 1

The register lists **candidates to test**, not accepted replacements.

| MUDAC Concept | Primary precedent families | Concrete candidates to test | High-value expectation questions for 014-C |
| --- | --- | --- | --- |
| Competition | PT-01 | competition, contest, tournament, event | Does the precedent separate lifecycle completion/finalization from official-result declaration? Does it imply one event instance or a reusable program? |
| Division | PT-02 | division, category, class, bracket/cohort | Is it merely classification, or does the precedent import bracket progression/rank semantics MUDAC does not own? |
| Team | PT-02 | team, entrant, competitor, submission group | Does `Team` imply stable human roster or collaboration semantics beyond MUDAC's administrative competing unit? |
| Panel | PT-02 | panel, jury, committee, judge group | Does the precedent imply actual decision participation/collective authority rather than planned evaluator grouping? |
| Identity | PT-03 | identity, person, user, principal, account | Which precedent preserves human continuity without importing login/account/session behavior? |
| Participation | PT-03 | participation, membership, enrollment, registration, role assignment | Which expectations concern scoped relationship/capacity versus permission? Does `membership` imply persistence or governance rights MUDAC lacks? |
| Alias | PT-04 | alias, pseudonym, anonymized identifier, display name | Does the precedent imply cosmetic naming, resolvability, permanence or user control inconsistent with bias-control scope? |
| Access | PT-04 | access decision, permission, authorization, entitlement, capability | Is the familiar model persisted grant state or contextual decision? Does it separate actor visibility from audience disclosure? |

# 6. Comparison register — Family 2

| MUDAC Concept | Primary precedent families | Concrete candidates to test | High-value expectation questions for 014-D |
| --- | --- | --- | --- |
| Evaluation Occurrence | PT-05 | assessment event, judging session, encounter, attempt, review occurrence | Does the precedent preserve actual bounded happening without owning evaluator duty or judgment evidence? Does replacement preserve distinct identity/history? |
| Evaluation Obligation | PT-06 | obligation, assignment, review assignment, task, duty | Does completion mean historical responsibility satisfaction rather than current evidence eligibility? Do reassignment/successor semantics match? |
| Rubric | PT-07 | rubric, scoring guide, evaluation template, criteria set | Do users expect an editable template or an exact version-bound basis? Does the precedent separate definition from authoritative use? |
| Scorecard | PT-08 | scorecard, ballot, evaluation response, assessment, submission | Does the precedent preserve one Judge's authored judgment, Draft/finalize distinction, amendment lineage and one logical weight? |

# 7. Comparison register — Family 3

| MUDAC Concept | Primary precedent families | Concrete candidates to test | High-value expectation questions for 014-E |
| --- | --- | --- | --- |
| Versioning | PT-09 | version, revision, snapshot, version history | Can it remain composition-only support without generic edit/checkout/revert authority? Does `revision` falsely imply mutable content ownership? |
| Provenance | PT-09 | provenance, audit trail, lineage, attribution record | Does the precedent describe origin/authority evidence without becoming the source of authority or generic telemetry? |
| Award | PT-10 | award, prize, recognition, winner designation | Does the precedent separate selection basis from conferral authority and allow discretionary as well as rank-derived recognition? |
| Outcome Declaration | PT-11 | official result declaration, certification, attestation, decision record | Does the precedent capture explicit officiality/currentness without implying public release or destructive replacement? |
| Export | PT-12 | export, report, snapshot, extract, rendered artifact | Would users expect a stable SourceBasis/currentness-bearing representation, or merely an ephemeral download? |
| Publication | PT-13 | publication, release, distribution, announcement | Does the precedent separate release authority from generation, officiality and delivery/recipient possession? |

# 8. Cross-cutting non-Concept comparison register

These subjects are not Concept candidates merely because they have familiar analogies.

| Current classification | Familiar precedents worth testing | False-familiarity question |
| --- | --- | --- |
| Readiness — derived | checklist completion, gate, eligibility/readiness score | Would familiar checklist/gate semantics make users think readiness is writable or independently authoritative? |
| Remaining Work — derived | task list, work queue, inbox | Would task-list familiarity imply manually created/closed work rather than projection over Outstanding obligations? |
| Coverage — derived | completeness, quorum, coverage, sufficiency | Would familiar percentage/quorum semantics imply missing = zero or exception = factual satisfaction? |
| Aggregate — derived | total, average, composite score | Does ordinary aggregate language hide evidence eligibility/basis dependence? |
| Rank — derived | leaderboard, standing, placement | Would leaderboard familiarity imply editable/live official results or Award ownership? |
| Reconciliation — work context/process | exception queue, case management, issue resolution | Would ticket/workflow familiarity create a writable reconciliation state or generic `resolve` authority? |
| Live Operations — work context | operations center, dashboard, control room | Would control-room familiarity imply catch-all administrative authority? |
| Finalization Readiness — derived | approval gate, closeout checklist | Would familiar approval semantics collapse readiness with Competition Finalization/Outcome Declaration? |

# 9. Historical adapters as negative precedents

Two familiar-looking historical abstractions are retained specifically as counterexamples:

## `Judging Encounter`

`Encounter` is useful evidence that a familiar bounded-meeting/event word can become overloaded when it is asked to own:

- actual occurrence;
- evaluator grouping;
- responsibility;
- Scorecard context.

Phase 014 must not restore it merely because `encounter` or `session` sounds familiar.

## `Official Outcome Revision`

This historical abstraction is useful evidence that `revision` familiarity can obscure the difference between:

- official declaration authority;
- derived recalculation;
- predecessor/successor official history.

It remains a negative comparison precedent, not a candidate current Concept.

# 10. Prior-MUDAC familiarity evidence retained cautiously

The earlier 007-B audit observed that Identity, Participation, Alias, Access, Versioning, Provenance, Export and Publication looked comparatively reusable, while domain concepts such as the evaluation occurrence/Scorecard family appeared more competition-specific.

014-B records this only as a **historical hypothesis**.

It is not a current disposition because:

- the catalog changed after 007-B;
- Evaluation Occurrence / Evaluation Obligation replaced the older Encounter boundary;
- Outcome Declaration later became the officiality owner;
- synchronization, dependence and mapping semantics matured substantially in Phases 011–013;
- Phase 014 requires explicit precedent comparison after those later semantics settled.

# 11. Comparison template for 014-C through 014-E

For each current Concept, later family audits should capture at least:

```text
MUDAC Concept
current purpose / OP summary
precedent candidate
precedent evidence confidence
expected transferred mental model
semantic matches
semantic mismatches
high-consequence mismatch, if any
false-familiarity exposure
possible configuration-vs-intrinsic distinction
candidate disposition
canonical/reopen consequence
Phase-015 subtle integrity carry-forward, if any
```

Candidate disposition remains one of:

```text
SEMANTIC FIT / REUSE CANDIDATE
USEFUL ANALOGY ONLY
FALSE FAMILIARITY RISK
DISTINCT / RETAIN NOVELTY
BROADER GENERICITY CANDIDATE
UPSTREAM DEFECT / REOPEN CANDIDATE
```

# 12. Counterexample requirements

A family audit must not mark a familiar fit without trying to break it.

At minimum ask:

- Which expectation would a user of the precedent predict incorrectly?
- Is any mismatch high-consequence for authority, history, finality or disclosure?
- Does the precedent own more or less state than the MUDAC Concept?
- Is similarity actually produced by synchronization rather than intrinsic behavior?
- Is a supposedly intrinsic MUDAC difference really configuration?
- Does the familiar precedent depend on a product variant MUDAC intentionally does not have?
- Would explicit novelty produce a safer mental model?

# 13. Precedent-source acquisition discipline

Later family audits may add concrete external/domain sources as needed.

Use the smallest sufficient source set:

1. current MUDAC owner;
2. one or more sufficiently defined precedent sources;
3. historical MUDAC source only where it explains an alternative/counterexample.

Do not collect many examples merely to count prevalence.

When a precedent term has materially inconsistent meanings across sources, narrow the comparison or mark it variable rather than synthesizing a fictional universal definition.

# 14. No current semantic change

014-B changes no MUDAC Concept, synchronization, dependence edge, PF-01 scope, policy, invariant or Experience mapping.

The register exists so 014-C through 014-E can make deliberate comparisons against the **current** design.

Any later adopted refinement must still propagate through natural owners under the 014-A blast-radius rule.

# 15. FRG risk posture after evidence baseline

014-B particularly constrains:

- **FRG-R01 Name-equals-fit** — comparison requires semantic dimensions;
- **FRG-R02 Popularity bias** — prevalence is not evidence of fit;
- **FRG-R03 False familiarity** — every register entry includes expectation-risk questions;
- **FRG-R04 Implementation reuse leakage** — implementation evidence remains E7/quarantined;
- **FRG-R06 Similarity merge** — precedent families are not super-concepts;
- **FRG-R09 Novelty without justification** — every Concept now has comparison candidates;
- **FRG-R13 Historical-adapter revival** — old adapters are negative precedents only;
- **FRG-R14 Taxonomy for taxonomy's sake** — PT-01..PT-13 organize comparisons and own no semantics.

No risk is closed merely by creating the register; family audits must now test the hypotheses.

# 16. 014-C handoff

014-C should audit Family 1:

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

Use the PT-01 through PT-04 comparison candidates and E1–E7 evidence discipline.

014-C should produce actual candidate dispositions for this family, but must keep concept changes separate from comparison findings until a refinement is justified and its blast radius is understood.

# Exit decision

```text
014-B: COMPLETE — PASS
precedent taxonomy: ESTABLISHED
18-Concept comparison register: COMPLETE
derived/work-context register: COMPLETE
historical adapters: NEGATIVE PRECEDENTS ONLY
semantic dispositions: DEFERRED TO 014-C..E
canonical semantics changed: NO
architecture / implementation: SUSPENDED
next: 014-C
```
