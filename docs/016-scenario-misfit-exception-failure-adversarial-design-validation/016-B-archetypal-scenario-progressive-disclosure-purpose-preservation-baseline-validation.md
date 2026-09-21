---
type: Validation Record
title: 016-B — Archetypal Scenario, Progressive-Disclosure & Purpose-Preservation Baseline Validation
description: "Establishes the positive ordinary-use control case for Phase 016, validates progressive disclosure without converting dependence/synchronization into navigation, and exercises familiarity pressure SVT-12."
status: stable
tags: [phase-016, archetypal, progressive-disclosure, purpose-preservation, mapping, familiarity]
sources:
  - resource: 016-A-validation-scope-misfit-hypotheses-risk-coverage-subphase-planning.md
  - resource: ../canonical/project/purpose-needs-success-tensions.md
  - resource: ../canonical/concepts/
  - resource: ../canonical/synchronizations/
  - resource: ../canonical/dependence/
  - resource: ../canonical/experience/
---

# Purpose

016-B establishes the positive archetypal baseline against which later exceptional, degraded, corrective and adversarial scenarios can be compared.

The governing question is:

> When MUDAC is used in an ordinary intended competition situation, can actors understand and exercise the mature Concepts without hidden semantics, unnecessary conceptual burden, authority distortion or dependence on an implementation-specific workflow?

# Baseline assumptions

The control case assumes a legitimate competition, valid competitor participation, established judging responsibility, intended Judge capacities, functioning bias controls, an applicable evaluation basis, sufficient ordinary evaluation to progress, normal connectivity/representation and no retrospective correction.

These assumptions isolate ordinary use; they are not requirements that MUDAC may impose on all scenarios.

# Progressive-disclosure rule

Progressive disclosure is a semantic exposure principle, not a UI architecture.

> Expose the smallest semantically sufficient surface for an actor to understand their current legitimate purpose, available authoritative information and available actions without concealing consequences material to that action.

Therefore:

- dependence order is not navigation order;
- synchronization composition is not a mandatory wizard;
- one Concept does not require one screen;
- not every actor needs the whole Concept graph;
- familiar UI terms may be used only when they preserve canonical semantics.

# Archetypal scenarios

## ABS-01 — Competition readiness and contextual entry

A Judge enters a legitimate competition context to perform judging.

The Judge needs the applicable competition context, their participation/capacity, relevant evaluation responsibility, evaluation basis, authorized competitor representation and currently legitimate action surface.

The Judge does not need unrelated competition-creation, award, reconciliation, publication or organizer-only machinery merely because those semantics exist upstream/downstream.

**Disposition: FIT.**

The mature design supports contextually relevant entry without reproducing the Concept graph as navigation.

## ABS-02 — Blinded Judge encounters an assigned competitor

The relevant semantic composition is approximately:

```text
Competition context
  → Judge participation/capacity
  → Evaluation responsibility
  → authorized competitor representation
  → evaluation basis
  → evaluation occurrence
```

This chain does not imply six screens or six confirmations.

The Judge should not need identity information prohibited by the active bias-control context, other Judges' judgments where independence matters, organizer-only controls or downstream result state before it is legitimately relevant.

**Disposition: FIT.**

A familiar label such as "submission" is acceptable only if it does not collapse competitor, representation, responsibility, occurrence and basis into a false single semantic owner.

## ABS-03 — Independent scorecard authorship and completion

A Judge evaluates against the applicable basis and authors their own judgment.

The design preserves:

- evaluation basis;
- evaluation occurrence;
- Judge-authored judgment;
- scorecard representation;
- responsibility/obligation;
- completion.

A scorecard may be a useful representation without becoming a super-Concept that owns all of these semantics.

**Disposition: FIT.**

"Submit scorecard" may be usable interaction language, but cannot silently mean authorship + completion + organizer acceptance + immutable finality + downstream outcome eligibility.

## ABS-04 — Judge progresses across ordinary responsibilities

A Judge completes one responsibility and proceeds to another.

The application may choose a queue, dashboard, tabs, cards, "Next" affordance or another representation later. Concept Design does not require any of them.

**Disposition: FIT.**

One evaluation does not semantically create or authorize the next merely because the experience presents them sequentially.

## ABS-05 — Organizer observes progress without becoming evaluator

The Organizer may legitimately observe participation, responsibility state, coverage/readiness and operational exceptions.

That visibility does not confer Judge authorship.

> Observability ≠ authorship ≠ authority to substitute.

A familiar "approve" action may exist only where canonical authority actually provides approval semantics; it must not be invented merely because administrative products commonly use approval.

**Disposition: FIT.**

## ABS-06 — Ordinary coverage and aggregate formation

The design maintains separation among:

- individual judgment;
- coverage;
- aggregate;
- rank;
- award;
- competition finalization;
- outcome declaration.

A leaderboard may be a representation of legitimate rank information, but it must not silently collapse provisional aggregate/rank into official declared outcome.

**Disposition: FIT.**

## ABS-07 — Award and official outcome formation

Authorized outcome work may compose multiple legitimate actions.

A product-level "Publish winners" action can only compose existing semantics if:

1. each constituent action remains legitimate;
2. initiating authority is sufficient;
3. preconditions remain satisfied;
4. materially distinct consequences are not hidden;
5. failure cannot fabricate an invalid partial domain state.

Detailed chaining pressure remains for 016-H.

**Disposition: FIT.**

## ABS-08 — Ordinary external representation

After appropriate authority exists, an authorized result may be exported, printed or published.

> Representation of truth ≠ ownership of truth.

A recipient need not see internal Judge/coverage/reconciliation mechanics if the representation still communicates its intended meaning, provenance/currentness and authority accurately.

**Disposition: FIT.**

# Familiarity-pressure validation — SVT-12

| Familiar metaphor | Acceptable use | Invalid inference |
| --- | --- | --- |
| Dashboard | summarize relevant state/actions | dashboard defines underlying state |
| Scorecard | represent Judge evaluation | scorecard owns basis, occurrence, authorship, responsibility and finality |
| Submission | contextual label where accurate | competitor representation is necessarily one submission Concept |
| Submit | communicate a defined action | all authored material becomes permanently immutable |
| Approve | use where canonical authority exists | Organizer universally approves Judge judgment |
| Final | communicate specifically identified finality | nothing may ever be corrected |
| Leaderboard | represent legitimate rank | rank equals official/public outcome |
| Wizard | optional presentation | dependence/synchronization requires sequential navigation |
| Next | navigate to another relevant item | previous domain action creates the next responsibility |
| Publish | invoke authorized release behavior | publication creates underlying result authority |

**SVT-12 disposition: FIT — MAPPING DISCIPLINE REQUIRED.**

Familiarity is subordinate to semantic ownership.

# Boundary clarifications

**BC-016B-01 — Familiar labels remain context-qualified.**  
Terms such as submit, approve, final, publish and scorecard must map to canonical consequences.

**BC-016B-02 — Progressive disclosure cannot suppress consequential meaning.**  
The whole model need not be exposed, but a consequential action must expose enough meaning for legitimate understanding.

**BC-016B-03 — Interaction convenience does not create conceptual synchronization.**  
Bundling actions for usability does not merge their semantic ownership or authority.

# Purpose-preservation result

| Purpose / invariant | Result |
| --- | --- |
| Bias-sensitive judging | PRESERVED |
| Judge independence / authorship | PRESERVED |
| Organizer operational authority | PRESERVED |
| Organizer/Judge separation | PRESERVED |
| Responsibility visibility | PRESERVED |
| Evaluation provenance | PRESERVED |
| Dependence ≠ navigation | PRESERVED |
| Synchronization ≠ wizard | PRESERVED |
| Aggregate/rank/award separation | PRESERVED |
| Finalization/declaration separation | PRESERVED |
| Representation ≠ authority | PRESERVED |
| Progressive disclosure | PRESERVED |
| PF-01 one-product semantics | PRESERVED |

# Validation register

| Probe | Disposition |
| --- | --- |
| ABS-01 contextual entry | FIT |
| ABS-02 blinded evaluation entry | FIT |
| ABS-03 scorecard authorship/completion | FIT |
| ABS-04 progression across responsibilities | FIT |
| ABS-05 organizer oversight | FIT |
| ABS-06 coverage/aggregate formation | FIT |
| ABS-07 award/outcome formation | FIT |
| ABS-08 external representation | FIT |
| PD-01 minimal sufficient disclosure | FIT |
| PD-02 dependence vs interaction order | FIT |
| PD-03 synchronization vs wizard | FIT |
| SVT-12 familiarity pressure | FIT — MAPPING DISCIPLINE |

```text
semantic misfits             0
reopens required             0
semantic repairs             0
boundary clarifications      3
unresolved archetypal probes 0
```

# Gate contribution

- **V1 Archetypal fit — SUPPORTED**
- **V8 Bias/privacy preservation — PARTIALLY SUPPORTED**
- **V9 Cross-family coherence — BASELINE SUPPORTED**

# 016-B decision

**016-B — COMPLETE — PASS**

Normal end-to-end competition behavior fits the mature design without requiring the application to expose the design corpus literally.

Concept Design determines semantic truth.

Mapping makes that truth intelligible.

Progressive disclosure determines which portion is relevant to the actor's current legitimate purpose.

No semantic reopen is required.

Proceed to:

> **016-C — Competition Context, Competitor Structure, Identity, Participation, Alias, Access & Bias-Control Scenario Validation**
