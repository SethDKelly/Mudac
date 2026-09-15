---
type: Phase Design Record
title: 012-B — Application-Family Boundary, Concept Inclusion Roles & Candidate Dependence Inventory
description: "Defines each current Concept's intended role inside the MUDAC application family, classifies family-anchor/core/conditional/support/extension roles, inventories candidate extrinsic inclusion-dependence edges and explicit non-edges, and hands bounded candidate questions to 012-C through 012-G without accepting the final dependence graph prematurely."
status: stable
tags: [phase-012, jackson, dependence, subsets, product-family, inventory, roles]
sources:
  - resource: 012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md
  - resource: ../011-concept-composition-synchronization/011-J-canonical-synchronization-reconciliation-phase-011-consolidation-phase-012-handoff.md
  - resource: ../canonical/project/mandate-context.md
  - resource: ../canonical/project/purpose-needs-success-tensions.md
  - resource: ../canonical/concepts/
  - resource: ../canonical/synchronizations/
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/006/phase-definition.md
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/006/dependence-subset-contract.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-14T23:29:00-05:00 }
---

# Purpose

Perform the first substantive Phase 012 dependence pass after the 012-A start gate.

This subgroup answers three questions before family-specific edge acceptance begins:

1. What application role does each of the eighteen independent Concepts serve inside the **MUDAC live student data competition judging-and-outcome family**?
2. Which Concept pairs or conditional groups are plausible extrinsic inclusion dependencies worth testing?
3. Which tempting relationships should **not** enter the candidate graph because they are merely synchronization, intrinsic parameters, implementation habits, or derived/non-Concept behavior?

This record creates a **candidate inventory**, not the final dependence graph.

No candidate edge becomes canonical current dependence merely by appearing here.

# Decision summary

**PASS — candidate inventory established; no final dependence edge accepted.**

The application-family boundary from 012-A remains sound and requires no revision.

All eighteen current Concepts have a defensible role inside the family, but they do not all have the same inclusion posture. The inventory therefore separates:

- family-context anchors;
- judging/competitor core capability roles;
- contextual structuring roles;
- authority/history support roles;
- outcome/recognition roles;
- externalization/release roles.

The most important preliminary result is:

> **The current full MUDAC capability set is not treated as one indivisible product.**

Several Concepts are strong candidates for optional or conditional inclusion even though they are important in the full application. Conversely, some support Concepts may prove required whenever a higher-authority capability is included even though the support Concept is generic and never user-facing by itself.

The next subgroup remains:

> **012-C — Competition, Actor, Competitor Context & Bias-Control Dependence**

# 1. Application-family boundary revalidation

The Phase 012 application family remains:

> **software supporting live student data competition judging and outcome formation, including preparation, independent evaluation, operational correction, explicit outcome authority, and optional controlled external representation/release.**

This boundary is intentionally capability-oriented rather than implementation- or packaging-oriented.

## 1.1 Included family concerns

The family may include variants that differ in:

- single-cohort versus multi-cohort competition structure;
- reusable evaluator grouping versus ad-hoc assignment;
- judging-only versus outcome-declaring capability;
- Awards versus no Awards;
- internal official outcome versus external representation/release;
- representation without publication;
- different levels of authority-history support where conceptually coherent.

## 1.2 Not separate family members merely because realization differs

The following do not define separate Concept subsets by themselves:

- paper versus electronic capture;
- phone versus desktop interaction;
- online versus degraded-connectivity operation;
- synchronous versus asynchronous runtime behavior;
- AWS/service topology;
- source-code package boundaries;
- authentication provider choice;
- PDF versus another representation format.

These may matter in later mapping/architecture but are not Concept-inclusion axes unless a later phase exposes a genuine Concept distinction.

# 2. Role-classification vocabulary

012-B uses role classes only as analysis aids. They are not dependency semantics by themselves.

## Family anchor

A Concept whose application role appears tightly tied to the MUDAC family definition and is a strong candidate for inclusion in every meaningful in-family variant.

A family anchor is not yet proven universally required.

## Core judging role

A Concept directly involved in creating, assigning, performing, or preserving independent evaluation.

Core does not mean mandatory in every conceivable subset.

## Contextual structuring role

A Concept organizes scope, grouping, cohorting, presentation, or contextual capability. Such a Concept may be highly valuable yet optional in variants that obtain the relevant role another way.

## Authority/history support role

A generic Concept that preserves authoritative currentness, lineage, attribution, correction, or explainability for another capability.

Such support may become a conditional inclusion requirement when an authoritative capability is present.

## Outcome/recognition role

A Concept that adds recognition or official result authority after evaluation evidence exists.

## Externalization/release role

A Concept that externalizes already-existing source meaning or deliberately releases a representation.

# 3. Per-Concept MUDAC inclusion-role inventory

| Concept | MUDAC family role | Preliminary posture | Primary later owner |
| --- | --- | --- | --- |
| Competition | one live competition occurrence's lifecycle/governing context | **strong family-anchor candidate** | 012-C |
| Team | stable competing student-group identity within scope | **strong competitor-core candidate** | 012-C |
| Identity | persistent human continuity across participation episodes | **strong actor-support candidate; universality unresolved** | 012-C |
| Participation | scoped/time-bounded Judge or Organizer capacity | **strong live-operation candidate** | 012-C |
| Access | contextual capability/disclosure decision | **strong protected-operation candidate; conditionality unresolved** | 012-C |
| Division | competitive cohort partitioning | **optional/conditional candidate** | 012-C |
| Alias | bias-protecting alternate Team identity | **scope-sensitive bias-control candidate** | 012-C |
| Panel | reusable evaluator grouping | **optional organization candidate** | 012-C |
| Evaluation Occurrence | bounded historical evaluation context/participant truth | **strong live-evaluation context candidate** | 012-D |
| Evaluation Obligation | one evaluator's responsibility for qualifying evaluation | **strong accountability candidate** | 012-D |
| Rubric | structured evaluation instrument/response semantics | **strong basis candidate; universality unresolved** | 012-D |
| Scorecard | one evaluator's independent judgment | **judgment-core candidate** | 012-D |
| Versioning | immutable authoritative-state lineage/current eligibility | **conditional authority-history support candidate** | 012-E |
| Provenance | attributable origin/actor/represented-authority/correction history | **conditional explainability support candidate** | 012-E |
| Award | scoped recognition/conferral | **optional outcome extension candidate** | 012-F |
| Outcome Declaration | explicit official result authority | **optional for judging-only variants; strong official-outcome candidate** | 012-F |
| Export | stable source-bound external representation | **optional representation capability** | 012-G |
| Publication | deliberate release of exact representation | **optional release capability; likely depends on Export in MUDAC** | 012-G |

This table records inclusion roles, not accepted edges.

# 4. Candidate-edge confidence vocabulary

To prevent candidate inventory from becoming accidental authority, each candidate is classified as follows.

## Strong candidate

Current purpose, Concept binding, and counterexample pressure suggest a likely extrinsic dependence, but the designated later subgroup must still prove it.

## Conditional candidate

The relationship may hold only for a named capability/variant, not every inclusion of the source Concept.

## Alternative/disjunctive candidate

The source Concept likely requires one of several supporting roles, or the target role can be supplied by different included Concepts. It should not be forced into a simple binary edge without later analysis.

## Challenge candidate

A familiar-product assumption worth testing because current Concept boundaries make a coherent counterexample plausible.

## Rejected as candidate edge

The relationship is currently better explained as synchronization, intrinsic generic parameterization, derived behavior, or implementation coupling.

# 5. Candidate dependence inventory — family/context/actor side

The following are provisional only.

## CAND-C-01 — Team → Competition

**Classification:** strong candidate.

Within MUDAC, Team's intended role is a competing student group in a competition scope. Although `Team<Scope>` is intrinsically generic and does not need Competition internals, a Team included in this application family appears to lack its intended competing-unit role without a Competition context.

**Counterexample to test:** reusable pre-event Team registry independent of one Competition.

If such a registry is a meaningful current MUDAC family member rather than merely upstream administration, the edge may need refinement.

## CAND-C-02 — Participation → Competition

**Classification:** strong candidate.

MUDAC Participation normally means Judge/Organizer involvement in one Competition scope. The Concept is intrinsically generic over Scope, but its current project role is event-scoped human participation.

**Counterexample to test:** reusable evaluator pool represented as Participation outside a particular Competition. Current semantics suggest that would more likely be Identity or another future concept, not Participation.

## CAND-C-03 — Participation → Identity

**Classification:** strong candidate, but not intrinsic.

MUDAC's low-friction returning-user and attributable-authority goals bind Participant to stable Identity continuity. Participation itself accepts a generic Participant reference, so the candidate is contextual.

**Counterexample to test:** deliberately ephemeral anonymous Judge participation with no durable Identity continuity.

The question is not whether such a system can be implemented; it is whether it can satisfy MUDAC's attribution, correction, recovery, and authority-separation purposes.

## CAND-C-04 — Access → Participation

**Classification:** conditional candidate.

Most protected MUDAC domain actions depend on current Competition capacity supplied through Participation, but Access is intrinsically generic and may also evaluate technical-support or exceptional contexts that do not map cleanly to ordinary Participation.

Do not prematurely establish a universal edge.

## CAND-C-05 — Access → Identity

**Classification:** challenge candidate.

Access often receives an identity-backed principal, but its semantics require only a Principal plus supplied context. The application might legitimately evaluate some capability against a scoped principal/reference that is not itself a durable Identity Concept instance.

012-C must determine whether MUDAC's baseline confidentiality/authority purposes make Identity universally required whenever Access is included.

## CAND-C-06 — Division → Competition

**Classification:** strong candidate.

In MUDAC, Division organizes competitors within a Competition scope. Division is intrinsically generic over Scope, so this is contextual rather than intrinsic.

## CAND-C-07 — Division → Team

**Classification:** strong candidate.

MUDAC's Division members are Teams. A Division with no Team concept would lack the current project's competitor-cohort role.

**Counterexample to test:** Division definitions prepared before any Team exists. Presence of zero current members does not necessarily defeat the inclusion dependence because the role still targets Team membership.

## CAND-C-08 — Alias → Competition

**Classification:** strong candidate.

MUDAC Alias is scoped to blinded judging within one Competition context.

## CAND-C-09 — Alias → Team

**Classification:** strong candidate.

The current MUDAC Subject represented by Alias is Team. The generic Alias Concept could serve other subjects elsewhere, but that is outside this application family.

## CAND-C-10 — Panel → Competition

**Classification:** strong candidate.

Panel's MUDAC role is reusable Judge grouping inside a Competition scope.

## CAND-C-11 — Panel → Participation

**Classification:** strong candidate.

MUDAC Panel members are Judge Participation identities rather than permanent Identity roles. This preserves event-scoped capacity and prevents Panel membership from becoming permanent human authority.

## CAND-C-12 — Competition → Division

**Classification:** challenge candidate; likely reject.

A single-cohort competition appears coherent without Division. 012-C must explicitly test the single-cohort contraction rather than manufacture a placeholder Division.

## CAND-C-13 — Competition → Panel

**Classification:** challenge candidate; likely reject.

Ad-hoc evaluator assignment may support coherent live judging without reusable Panel grouping.

## CAND-C-14 — Team → Alias

**Classification:** conditional/scope candidate.

Bias-sensitive judging makes Alias important in the current baseline, but the inclusion rule may be better stated as a **variant/scope constraint** for in-scope blinded judging rather than a universal structural dependency of Team.

A Team remains meaningful administratively without Alias.

# 6. Candidate dependence inventory — evaluation side

## CAND-D-01 — Evaluation Occurrence → Competition

**Classification:** strong candidate.

Within MUDAC, bounded judging occurrences happen within a Competition scope.

## CAND-D-02 — Evaluation Occurrence → Team

**Classification:** strong candidate.

The current MUDAC evaluation Subject is Team.

## CAND-D-03 — Evaluation Occurrence → Participation

**Classification:** strong candidate.

Actual evaluators are Judge Participation identities in the MUDAC family.

## CAND-D-04 — Evaluation Occurrence → Panel

**Classification:** challenge candidate; likely reject.

Phase 011 intentionally made Panel optional as a supplier of intended starting membership. The occurrence can conceptually record actual participants without reusable Panel grouping.

## CAND-D-05 — Evaluation Occurrence → Alias

**Classification:** conditional candidate.

Occurrence preserves presented context, which in ordinary blinded judging includes Alias. But Alias may be absent from a coherent no-blinding variant, and PresentedContext can contain other supplied facts.

## CAND-D-06 — Evaluation Occurrence → Division

**Classification:** conditional candidate.

Division can be part of presented context, but a single-cohort variant may omit it.

## CAND-D-07 — Evaluation Occurrence → Rubric

**Classification:** strong candidate for current structured-judging variants; still requires proof.

MUDAC normally supplies an exact authoritative Rubric Version as BasisRef. The counterexample is a meaningful evaluation occurrence using a non-Rubric supplied basis without inventing a replacement concept.

## CAND-D-08 — Evaluation Obligation → Competition

**Classification:** strong candidate.

MUDAC responsibility exists within competition scope.

## CAND-D-09 — Evaluation Obligation → Participation

**Classification:** strong candidate.

The responsible evaluator is a Judge Participation identity in current MUDAC semantics.

## CAND-D-10 — Evaluation Obligation → Team

**Classification:** strong candidate.

The responsibility concerns evaluation of a Team in this application family.

## CAND-D-11 — Evaluation Obligation → Rubric

**Classification:** strong candidate for the ordinary current family.

The obligation Basis is normally an exact authoritative Rubric Version. 012-D must pressure-test whether a coherent variant can use another supplied evaluation basis while remaining MUDAC rather than a different product family.

## CAND-D-12 — Evaluation Obligation → Evaluation Occurrence

**Classification:** challenge candidate.

`OccurrenceRef` is explicitly optional in the Concept. Phase 012 must test individually assigned evaluation responsibility outside a bounded shared occurrence instead of converting ordinary occurrence-begin synchronization into inclusion dependence.

## CAND-D-13 — Scorecard → Participation

**Classification:** strong candidate.

The current MUDAC semantic author/evaluator is a Judge Participation identity.

## CAND-D-14 — Scorecard → Team

**Classification:** strong candidate.

The current MUDAC Subject is Team.

## CAND-D-15 — Scorecard → Rubric

**Classification:** strong candidate.

Current Scorecard response semantics depend on a supplied exact EvaluationBasis whose interpretation is owned by Rubric.

This is extrinsic application dependence, not intrinsic Scorecard coupling: Scorecard remains generic over EvaluationBasis.

## CAND-D-16 — Scorecard → Evaluation Occurrence

**Classification:** strong but challengeable candidate.

Current MUDAC Scorecard stores an OccurrenceContext and ordinary composition binds it to Evaluation Occurrence. 012-D must test whether an individually assigned evaluation can use a supplied non-occurrence context coherently.

## CAND-D-17 — Scorecard → Evaluation Obligation

**Classification:** strong but challengeable candidate.

The ordinary MUDAC path makes Scorecard evidence satisfy one obligation, and responsibility tracking is central to missing-work truth. However, Scorecard is intrinsically a judgment rather than responsibility state, so 012-D must establish whether any meaningful MUDAC judging variant can record independent judgment without Evaluation Obligation.

## CAND-D-18 — Rubric → Competition

**Classification:** challenge candidate; likely reject or conditional.

Rubric can be defined as a reusable evaluation instrument independently of a specific Competition. A library/preparation role may remain meaningful within MUDAC without Competition inclusion.

The later analysis must distinguish reusable instrument preparation from an executable competition variant.

# 7. Candidate dependence inventory — authority/history support

012-B does **not** model Versioning or Provenance as mandatory global dependencies for every Concept merely because history is valuable.

Their likely role is conditional on authoritative-state semantics.

## CAND-E-01 — authoritative Rubric use → Versioning

**Classification:** strong conditional candidate.

MUDAC establishes exact immutable Rubric bases for authoritative judging. Versioning currently owns the authoritative snapshot lineage/currentness needed to support that role.

The source of this candidate is the **authoritative-use capability**, not `Rubric` existence in Draft/preparation form.

## CAND-E-02 — authoritative Rubric use → Provenance

**Classification:** strong conditional candidate.

The application must explain who established the basis and through what authority when that fact is meaningful.

## CAND-E-03 — authoritative Scorecard use → Versioning

**Classification:** strong conditional candidate.

Current Scorecard Finalization/amendment/correction semantics rely on immutable authoritative versions and no silent predecessor revival.

## CAND-E-04 — authoritative Scorecard use → Provenance

**Classification:** strong conditional candidate.

Judge authorship, capture actor, represented authority, source channel, correction reason, and paper/electronic parity require attributable history.

## CAND-E-05 — Outcome Declaration → Versioning

**Classification:** challenge candidate.

Outcome Declaration already owns immutable predecessor/successor declaration history intrinsically. Do not assume every historical chain requires the generic Versioning Concept.

012-E must determine whether Versioning adds a distinct inclusion role here or would duplicate declaration-owned history.

## CAND-E-06 — Outcome Declaration → Provenance

**Classification:** conditional candidate.

Declaring authority and affected/successor reason are intrinsic declaration state, but broader actor/source explanation may still justify Provenance in the full application. This requires careful non-duplication analysis.

## CAND-E-07 — Competition → Versioning / Provenance

**Classification:** rejected as blanket candidates.

Competition itself owns meaningful lifecycle history. Generic Versioning/Provenance should not be included merely because every change can theoretically be audited.

Only specific authoritative/correction use cases may justify supporting inclusion.

# 8. Candidate dependence inventory — outcome/recognition

## CAND-F-01 — Award → Competition

**Classification:** strong candidate.

MUDAC Award recognition is scoped to a Competition.

## CAND-F-02 — Award → Team

**Classification:** strong candidate.

Current MUDAC Award recipients are Teams.

## CAND-F-03 — Award → Division

**Classification:** conditional candidate; likely reject as universal.

Rank-derived Awards may use Division-scoped results, while discretionary or competition-wide Awards may not require Division.

## CAND-F-04 — Award → Outcome Declaration

**Classification:** challenge candidate; likely reject.

Award conferral can be meaningful recognition without being included in an official outcome declaration. Conversely, official outcomes may exist without Awards.

## CAND-F-05 — Outcome Declaration → Competition

**Classification:** strong candidate.

The current declaration Scope is the Competition context, and its purpose is official competition outcome authority.

## CAND-F-06 — Outcome Declaration → Award

**Classification:** challenge candidate; likely reject.

Official result authority can coherently exist with no recognition awards.

## CAND-F-07 — Outcome Declaration → Scorecard / Evaluation Obligation / Evaluation Occurrence

**Classification:** alternative/transitive candidate, not direct edges yet.

Outcome Declaration consumes an OutcomeBasis rather than peer internals. Current full closeout traces to eligible evaluation evidence, but the appropriate Concept-level dependencies may be transitive through the in-scope outcome-forming variant rather than direct inclusion edges from Declaration to every source Concept.

012-F and 012-H must prevent a dense graph caused by traceability being mistaken for direct dependence.

# 9. Candidate dependence inventory — external representation/release

## CAND-G-01 — Export → Outcome Declaration

**Classification:** challenge candidate; likely reject.

Export can represent competition setup, judging material, calculated/provisional state, or official Outcome Declaration. Therefore Export does not appear universally dependent on Outcome Declaration.

## CAND-G-02 — Export → Competition

**Classification:** conditional/alternative candidate.

Most MUDAC Export sources are competition-scoped, but a reusable Rubric representation or other source may be meaningful without Competition. The real requirement may be “at least one valid exportable source” rather than one fixed Concept edge.

## CAND-G-03 — Publication → Export

**Classification:** strong candidate.

Publication intrinsically accepts any supplied Representation, but current MUDAC assigns stable external-representation ownership to Export. A Publication variant without Export would have no current Concept responsible for the exact representation being deliberately released.

012-G must test whether another in-family Representation owner exists before accepting this edge.

## CAND-G-04 — Export → Publication

**Classification:** rejected as likely dependence.

Stable printable/portable/internal representations remain useful even if nothing is deliberately published.

## CAND-G-05 — Publication → Outcome Declaration

**Classification:** challenge candidate; likely reject.

MUDAC may deliberately publish non-official operational/judging material if disclosure policy permits. Publication should not become synonymous with public official results.

# 10. Explicit non-edges / excluded graph nodes

The following must not enter the current candidate graph as ordinary Concept dependencies.

## 10.1 Derived mechanisms

Do not create vertices for:

- Readiness;
- Coverage;
- Aggregate;
- Rank;
- Ranking Readiness;
- Finalization Readiness.

They may provide rationale for why included Concepts matter, but they are not current Concepts.

## 10.2 Process/work context

Reconciliation remains Organizer work/process context and is not a dependency node.

## 10.3 Capture channel

Paper/electronic is not a Concept inclusion dimension.

## 10.4 Runtime/implementation

Do not create dependence edges from:

- authentication provider;
- session store;
- database;
- API;
- service/module/package;
- event bus/queue;
- AWS component;
- PDF renderer;
- storage/transport.

# 11. Candidate adjacency inventory by source Concept

This compact inventory exists to route later analysis; it is **not a canonical graph**.

| Source Concept | Candidate required/co-inclusion targets to test | Important likely non-targets/counterexamples |
| --- | --- | --- |
| Competition | none assumed at 012-B | Division, Panel, Award, Outcome Declaration, Export, Publication all require optionality testing |
| Team | Competition | Alias and Division not automatically required |
| Identity | none assumed | Competition/Participation may use Identity, but Identity itself may be reusable before/after a Competition |
| Participation | Competition, Identity | Panel not required |
| Access | Participation? Identity? conditional | Access is generic; technical/exception contexts challenge universal actor edges |
| Division | Competition, Team | no Scorecard/Outcome direct dependency merely due ranking use |
| Alias | Competition, Team | Access is not intrinsic to Alias identity existence |
| Panel | Competition, Participation | Evaluation Occurrence not required for Panel planning existence |
| Evaluation Occurrence | Competition, Team, Participation, Rubric? | Panel/Division/Alias conditional; Obligation not automatically required |
| Evaluation Obligation | Competition, Participation, Team, Rubric? | Evaluation Occurrence optionality must be tested |
| Rubric | none assumed at Draft/reusable-instrument level | Competition/Versioning/Provenance may be conditional on authoritative use |
| Scorecard | Participation, Team, Rubric, Evaluation Obligation?, Evaluation Occurrence? | Versioning/Provenance are conditional on authoritative use, not Draft existence |
| Versioning | none assumed | do not make every history-owning Concept depend on Versioning |
| Provenance | none assumed | do not make every action depend on Provenance merely for auditability |
| Award | Competition, Team | Division and Outcome Declaration conditional/not universal |
| Outcome Declaration | Competition | Award not universal; direct evidence-source edges may be transitive rather than direct |
| Export | no fixed peer assumed; requires a valid source basis | Outcome Declaration and Publication not universal |
| Publication | Export strong candidate | Outcome Declaration not universal |

# 12. Preliminary role groups for later subset analysis

These are **analysis groups**, not mutual-dependence groups.

## Competition/actor/competitor context group

- Competition
- Team
- Identity
- Participation
- Access
- Division
- Alias
- Panel

Owner: 012-C.

## Evaluation group

- Evaluation Occurrence
- Evaluation Obligation
- Rubric
- Scorecard

Owner: 012-D.

## Authority-history support group

- Versioning
- Provenance

Owner: 012-E.

These Concepts may support several other groups conditionally; they are not automatically a required pair.

## Outcome/recognition group

- Award
- Outcome Declaration

Owner: 012-F.

Coverage/Aggregate/Rank remain derived support and are not graph vertices.

## Externalization/release group

- Export
- Publication

Owner: 012-G.

# 13. Candidate transitivity risks

012-B identifies several places where later phases must avoid creating unnecessary dense direct graphs.

## 13.1 Scorecard traceability does not imply Outcome Declaration → Scorecard direct dependence

If Outcome Declaration requires Competition and an in-scope outcome-forming variant requires evaluation evidence, the final graph may express that requirement through a capability/group relationship or transitive dependencies rather than connecting Declaration directly to every upstream evidence Concept.

## 13.2 Competition scope bindings can create repetitive edges

Many Concepts use Competition as MUDAC Scope. Later phases should determine whether direct `X → Competition` edges are the clearest truthful model or whether some inclusion follows transitively through another role without loss of rationale.

Do not optimize graph appearance at the expense of semantic truth, but avoid redundant edges that communicate no additional inclusion rule.

## 13.3 Versioning/Provenance can become accidental universal sinks

Because authoritative state and history matter broadly, it would be easy to point many Concepts at Versioning/Provenance. Later analysis must distinguish:

- intrinsic history owned by a Concept itself;
- authoritative immutable state that specifically needs Versioning;
- explanatory attribution that specifically needs Provenance;
- ordinary record/history that does not justify either support Concept.

# 14. Candidate cycles/co-inclusion groups to watch

No mutual-dependence group is accepted in 012-B.

Potential cycle pressure includes:

- Participation ↔ Identity, if later analysis incorrectly treats Identity as meaningful only through Participation;
- Scorecard ↔ Evaluation Obligation, if responsibility and evidence are over-coupled;
- Export ↔ Publication, if representation and release are treated as inseparable;
- Award ↔ Outcome Declaration, if recognition and official outcome are collapsed.

Current evidence instead suggests these should remain directional or optional relationships, but later subphases must prove the result.

# 15. Representative candidate-subset pressure map

The following probes are now routed to owners.

| Probe | Primary owner | Core question |
| --- | --- | --- |
| single cohort, no Division | 012-C | does Competition/Team/judging remain coherent? |
| ad-hoc judges, no Panel | 012-C/012-D | can occurrence/responsibility be established directly from eligible Participation? |
| no Alias | 012-C | structurally coherent, but does current scope permit it under bias-control purposes? |
| obligation without occurrence | 012-D | can assigned evaluation responsibility exist without bounded occurrence history? |
| occurrence without obligation | 012-D | can occurrence history be meaningful without independent work? |
| Scorecard without obligation | 012-D | can MUDAC retain judgment without responsibility tracking? |
| Rubric preparation without Competition | 012-D | reusable instrument role versus executable product variant |
| authoritative judging without Versioning | 012-E | can current/correctable authority remain truthful? |
| authoritative judging without Provenance | 012-E | can authorship/capture/correction remain explainable? |
| outcome without Award | 012-F | official outcome versus optional recognition |
| judging without Outcome Declaration | 012-F | coherent judging-only variant? |
| Export without Outcome Declaration | 012-G | operational/non-official representation role |
| Export without Publication | 012-G | stable representation independent of release |
| Publication without Export | 012-G | does current MUDAC have another representation owner? |

# 16. Application-family boundary conclusions

012-B does not narrow or expand the Phase-012 family boundary.

However, it makes two clarifications.

## 16.1 Reusable preparation concepts can exist before an executable Competition variant

Identity and Rubric may have meaningful preparation/library roles that outlive or precede a specific Competition. This does not automatically mean `{Identity}` or `{Rubric}` alone is an in-scope product variant. Later subset analysis must distinguish **meaningful concept role** from **supported application variant**.

## 16.2 Full-purpose MUDAC versus coherent family members

A smaller coherent subset may intentionally satisfy only part of the current full-capability purpose set—for example judging without external publication—while still belonging to the MUDAC application family.

Phase 012-I will determine which such variants are actually in scope.

Do not make every current purpose obligation mandatory for every coherent subset unless the product-scope decision explicitly says so.

# 17. Canonical-knowledge decision

No `docs/canonical/dependence/` owner is created by 012-B.

Reason:

- this subgroup establishes candidate edges only;
- family-specific phases 012-C through 012-G must accept/reject/refine them;
- promoting a candidate graph now would create a parallel “current” truth that later phases immediately need to rewrite.

The first canonical dependence owner should be created only when accepted edge semantics exist and should clearly distinguish accepted current edges from phase-history candidates.

# 18. Reopening triggers

The Phase 012-A reopening rules remain active.

In particular:

- if a candidate edge exists only because one Concept literally cannot be specified without another, reopen Phase 010 rather than accepting extrinsic dependence;
- if an accepted subset requires new cross-Concept behavior, reopen/refine the natural Phase 011 synchronization owner;
- if a coherent variant materially changes the product mandate, revisit canonical project scope rather than silently broadening MUDAC;
- if a candidate depends on implementation topology, reject the implementation evidence;
- if a non-Concept mechanism repeatedly appears as a necessary independent inclusion vertex, reopen its Phase-010 classification.

No such blocking reopen is required by 012-B.

# 19. 012-B exit test

012-B is complete because:

- all eighteen Concepts have an explicit MUDAC application-family role;
- candidate edge semantics are separated from accepted dependence;
- every candidate question from 012-A is represented or routed;
- obvious optionality pressure around Division, Panel, Award, Outcome Declaration, Export and Publication remains visible rather than prematurely resolved;
- Versioning/Provenance are treated as conditional authority-history support rather than universal sinks;
- derived mechanisms and implementation dependencies are excluded from the graph;
- likely transitivity/cycle traps are identified;
- no intrinsic-coupling defect currently requires Phase 010 reopening;
- no missing synchronization currently requires Phase 011 reopening;
- 012-C through 012-G have bounded inventories to resolve.

# Exit decision

**PASS — 012-B complete.**

Candidate dependencies are intentionally provisional.

Proceed to:

> **012-C — Competition, Actor, Competitor Context & Bias-Control Dependence**

# Implementation state

```text
architecture authority: SUSPENDED
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```
