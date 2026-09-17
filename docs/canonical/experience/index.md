# Experience Mapping Authority & Evidence

This directory contains MUDAC user-visible interaction/mapping knowledge.

## Current authority status

Phase 013 is **IN PROGRESS**.

```text
Phase 012  COMPLETE — PASS
013-A      COMPLETE — READY
013-B      COMPLETE — PASS
013-C      COMPLETE — PASS
013-D      NEXT — Competition Preparation, Competitor/Panel/Rubric Setup, Readiness & Organizer Configuration Mapping
```

Start with:

* [Phase 013 Mapping Authority, Evidence & Canonical Ownership Baseline](mapping-authority-baseline.md) — current authority/evidence classification, terminology contract and owner topology through 013-C.
* [Experience Context and Participation Modes](context-role-modes.md) — current operating-context, multi-capacity, role-mode and disclosure-context mapping accepted by 013-C.
* [Judge Entry, Participation & Readiness Mapping](judge-onboarding.md) — current Judge-entry, Competition Participation and Ready-to-Judge mapping accepted by 013-C.
* [Phase 013 Mapping Entry Authority](phase-013-entry-handoff.md) — Phase-013 entry/start-gate precedence, explanation-order constraints, risk register and reopen rules.
* [013-C Context, Identity, Participation, Access, Bias-Control & Judge Entry Mapping](../../013-concept-mapping-interaction-semantics-user-visible-representation/013-C-context-identity-participation-access-bias-control-judge-entry-mapping.md) — current phase evidence/rationale for accepted context and Judge-entry mapping.

Current conceptual meaning continues to come from:

* [Project Context & Purpose](../project/);
* [Concepts](../concepts/);
* [Synchronizations](../synchronizations/), especially the application action surface;
* [Dependence](../dependence/), including [PF-01 Product-Family Scope](../dependence/product-family-scope.md);
* mapping-relevant [Policies](../policies/) and [Invariants](../invariants/).

## Current accepted Experience owners

The following are now current mapping authority for their natural subjects:

| File | Accepted mapping subject | Phase |
| --- | --- | --- |
| [Experience Context and Participation Modes](context-role-modes.md) | Identity/Participation/Access operating context, role/capacity modes, multi-capacity isolation, context disclosure, current/history distinction | 013-C |
| [Judge Entry, Participation & Readiness Mapping](judge-onboarding.md) | Judge Competition entry, Identity continuity, Judge Participation, check-in/event attributes, Panel planning context, derived Ready-to-Judge semantics | 013-C |

## Remaining admitted Experience evidence

These documents remain admitted evidence/candidates until their assigned workstream explicitly accepts or rewrites them:

| File | Disposition | Subphase |
| --- | --- | --- |
| [Experience Action, State & Authority Traceability](action-authority-traceability.md) | retain/revalidate cross-cutting; final acceptance audit | 013-C–K |
| [Judge Evaluation](judge-evaluation.md) | retain active evaluation; split amendment/correction/history | 013-E/F |
| [Organizer Preparation](organizer-preparation.md) | rewrite/revalidate in place | 013-D |
| [Live Operations](live-operations.md) | rewrite/revalidate in place | 013-G |
| [Reconciliation & Finalization](reconciliation-finalization.md) | split into derived reconciliation + officiality owners, then supersede | 013-G/H |
| [Paper, Export & Publication](paper-export-publication.md) | split paper/correction from external release, then supersede | 013-F/I |
| [Accessibility & Resilience](accessibility-resilience.md) | rewrite/revalidate in place | 013-J |
| [Status, Feedback & Recovery](status-feedback-recovery.md) | rewrite/revalidate in place | 013-J |

Historical `stable` metadata on an admitted candidate does not override the current mapping baseline.

## 013-C context rules

```text
Identity != Participation != Access
one protected operation = one explicit Participation context
role/capacity mode = representation, not authority
multi-capacity capabilities never union
Judge context = Judge-safe disclosure posture
Panel membership != occurrence participation != responsibility != evidence
Ready to Judge = derived explanation, not writable state
technical support privilege != Competition authority
```

Judge-safe competitor identity remains **Alias + Division** during blinded judging. Organizer-sensitive information does not leak into Judge context simply because the same Identity also has Organizer Participation.

## Approved future owner additions

Create these only when their workstream has substantive durable mapping knowledge:

```text
authority-lineage-correction.md       013-F
reconciliation-derived-state.md       013-G
outcome-officiality.md                013-H
external-representation-release.md    013-I
```

No empty placeholders are needed.

## Terminology baseline

```text
Encounter
  → deprecated adapter; interpret by meaning as Evaluation Occurrence,
    Evaluation Obligation, Scorecard, Panel, Participation or Access

Official Outcome Revision
  → deprecated; current official authority/history is Outcome Declaration

Ready to Judge / Competition Ready / Ranking Readiness / Finalization Readiness
  → derived projections, not Concepts or editable workflow state

Reconciliation
  → work/process context, not a Competition lifecycle state or Concept
```

No blind search-and-replace is permitted.

## Mapping interpretation rule

```text
dependence order != navigation order
synchronization chain != mandatory wizard
```

Mappings expose enough context, basis, authority, consequence, currentness and history for correct understanding without turning Concept structure into interface architecture.

## Application-action rule

Phase 013 maps the established application action classes:

```text
D — direct
C — coordinated
P — composition-only participant
S — system-triggered reaction
X — intentionally unavailable generic action
```

Do not expose `P` or `X` as generic user controls.

## Next

Proceed to **013-D — Competition Preparation, Competitor/Panel/Rubric Setup, Readiness & Organizer Configuration Mapping**.
