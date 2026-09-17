---
type: Phase Design Record
title: 013-B — Experience Corpus Reconciliation, Terminology, Mapping Authority & Canonical Ownership Baseline
description: "Reconciles the pre-convergence Experience corpus against the current Purpose, Concept, Synchronization, Dependence and PF-01 model; classifies mapping authority, resolves deprecated terminology/reference routing, establishes durable canonical ownership destinations, and hands a trustworthy baseline to substantive mapping beginning in 013-C."
status: stable
tags: [phase-013, jackson, mapping, experience, terminology, authority, canonical-ownership, reconciliation]
sources:
  - resource: 013-A-mapping-scope-representation-semantics-experience-risk-subphase-planning.md
  - resource: ../012-concept-dependence-product-family-subset-scope/012-K-canonical-dependence-reconciliation-phase-012-consolidation-phase-013-handoff.md
  - resource: ../canonical/experience/phase-013-entry-handoff.md
  - resource: ../canonical/experience/
  - resource: ../canonical/concepts/
  - resource: ../canonical/synchronizations/
  - resource: ../canonical/synchronizations/application-action-surface-composition.md
  - resource: ../canonical/dependence/product-family-scope.md
  - resource: ../canonical/policies/
  - resource: ../canonical/invariants/
  - resource: https://github.com/SethDKelly/Base/blob/main/docs/phases/007/concept-mapping-contract.md
---

# Purpose

Establish a trustworthy Phase-013 mapping corpus before substantive concept mapping begins.

013-B does **not** redesign Judge or Organizer workflows, choose screens, prescribe navigation, or finish any of the twelve mapping dimensions identified by 013-A. It determines what existing Experience material means under the converged model, which material may be retained as evidence, which document boundaries remain natural, which must be split or superseded, and where durable Phase-013 mapping knowledge will live.

The governing question is:

> **Can later mapping work consume repository Experience knowledge without accidentally restoring superseded Concepts, archival synchronization authority, UI-owned state, or obsolete document boundaries?**

# Decision

**COMPLETE — PASS. Proceed to 013-C.**

```text
013-A START GATE                              COMPLETE — READY
013-B EXPERIENCE CORPUS RECONCILIATION       COMPLETE — PASS
CURRENT MAPPING AUTHORITY BASELINE            ESTABLISHED
ALL TEN INCOMING EXPERIENCE FILES             DISPOSITIONED
DEPRECATED ENCOUNTER AS CURRENT CONCEPT       PROHIBITED
OFFICIAL OUTCOME REVISION AS CURRENT CONCEPT  PROHIBITED
ARCHIVAL SYNCHRONIZATION ROUTING AS AUTHORITY PROHIBITED
CURRENT POLICY TERMINOLOGY DEFECTS FOUND      BOUNDED / REPAIRED
NEW CONCEPT REQUIRED                          NO
PHASE-010 REOPEN REQUIRED                     NO
PHASE-011 REOPEN REQUIRED                     NO
PHASE-012 REOPEN REQUIRED                     NO
SUBSTANTIVE EXPERIENCE MAPPING                BEGINS IN 013-C
ARCHITECTURE AUTHORITY                        SUSPENDED
IMPLEMENTATION PLANNING                       SUSPENDED
IMPLEMENTATION READINESS                      NOT READY
IMPLEMENTATION AUTHORIZATION                  NOT YET
NEXT                                           013-C
```

# 1. Mapping authority after 013-B

Phase 013 now distinguishes **conceptual authority**, **mapping authority**, **admitted evidence**, and **historical evidence**.

```text
Project Purpose / Mandate
  ↓
Current Concepts
  ↓
Current Synchronizations + application action surface
  ↓
Current Dependence / capability rules / PF-01 scope
  ↓
Current mapping-relevant Policies + Invariants
  ↓
Phase 013 Mapping Entry Authority
  ↓
Phase 013 Mapping Authority Baseline  ← established by 013-B
  ↓
Experience owners accepted/reworked by 013-C through 013-K
```

The pre-convergence Experience files are **admitted evidence/candidates**, not current mapping authority merely because they live under `docs/canonical/experience/` or carry an earlier `stable` marker.

Historical architecture, implementation, routes, screenshots, components and the incumbent UI remain downstream evidence only.

# 2. Corpus disposition

013-B evaluated all ten incoming Experience contracts.

| Incoming file | 013-B disposition | Natural destination / workstream | Reason |
| --- | --- | --- | --- |
| `context-role-modes.md` | **rewrite in place** | 013-C | Context/role organization remains useful; `Encounter` and role-mode implications require current Identity/Participation/Access/Occurrence/Obligation semantics. |
| `action-authority-traceability.md` | **retain as cross-cutting candidate; revalidate incrementally** | 013-C–K, final acceptance in 013-K | The traceability principle is strong, but examples contain pre-convergence terminology and archival synchronization routing. |
| `judge-onboarding.md` | **rewrite in place** | 013-C | Competition/Identity/Participation/Access/readiness separation is useful; exact entry/authority semantics require current mapping. |
| `judge-evaluation.md` | **split by responsibility** | active judging stays here in 013-E; amendment/correction/history moves to 013-F owner | The old file couples ordinary evaluation mapping to temporal correction semantics that now have distinct conceptual owners. |
| `organizer-preparation.md` | **rewrite in place** | 013-D | Non-linear preparation/readiness principles remain useful but must be remapped to current Concepts/actions and derived Readiness. |
| `live-operations.md` | **rewrite in place** | 013-G | Exception-first coordination remains useful; `Encounter` must be decomposed into Panel, Evaluation Occurrence, Evaluation Obligation and Scorecard/evidence state. |
| `reconciliation-finalization.md` | **split / supersede after replacement owners exist** | 013-G derived reconciliation owner + 013-H officiality owner | It currently bundles derived-state reconciliation, Award, Competition Finalization and obsolete `Official Outcome Revision` semantics. |
| `paper-export-publication.md` | **split / supersede after replacement owners exist** | paper/capture/correction → 013-F; Export/Publication/release → 013-I | Physical evidence capture and external release are independent mapping responsibilities accidentally bundled by medium/document intuition. |
| `accessibility-resilience.md` | **rewrite in place** | 013-J | Semantic parity/resilience principles remain useful and must be revalidated against current mappings. |
| `status-feedback-recovery.md` | **rewrite in place** | 013-J | Multidimensional status/uncertainty/recovery remains useful; stale `Encounter` example and current authority vocabulary require revalidation. |

No incoming Experience file is deleted in 013-B. Retaining the files preserves design provenance while the authority baseline prevents them from competing with the converged model.

# 3. Canonical Experience owner topology

013-B establishes the **natural ownership plan**, without creating empty placeholder documents.

Existing paths that remain natural:

```text
context-role-modes.md              → 013-C
judge-onboarding.md                → 013-C
organizer-preparation.md           → 013-D
judge-evaluation.md                → 013-E active evaluation
live-operations.md                 → 013-G live-event operations
accessibility-resilience.md        → 013-J
status-feedback-recovery.md        → 013-J
action-authority-traceability.md   → cross-cutting, final audit 013-K
```

New durable owners are created only when substantive work exists to populate them:

```text
authority-lineage-correction.md
  → 013-F
  → amendment, paper capture, correction, invalidation/replacement,
     current/history/successor representation obligations

reconciliation-derived-state.md
  → 013-G
  → remaining work, Coverage/Aggregate/Rank/Readiness explanation,
     exception/reconciliation and source-action versus projection semantics

outcome-officiality.md
  → 013-H
  → Award, Competition Finalization, Outcome Declaration,
     officiality, affected/successor authority

external-representation-release.md
  → 013-I
  → Export source/currentness, audience/disclosure, Publication,
     withdrawal/supersession and external-recipient meaning
```

The old `reconciliation-finalization.md` and `paper-export-publication.md` remain admitted evidence until their replacement owners have absorbed all still-valid semantics, after which they may be marked superseded rather than silently deleted.

This topology is intentionally **not** one file per page, screen or workflow. Owners correspond to distinct semantic mapping responsibilities future phases need to reference independently.

# 4. Terminology reconciliation contract

## 4.1 `Encounter`

`Judging Encounter` / `Encounter` is a deprecated historical adapter and must not be treated as a current Concept.

Each occurrence of the old term must be interpreted by meaning:

| Older intended meaning | Current semantic owner |
| --- | --- |
| bounded evaluation event; presented/actual participant context; begin/complete/invalidate/replace history | **Evaluation Occurrence** |
| one evaluator's responsibility; outstanding/satisfied/excused/ended/successor work | **Evaluation Obligation** |
| Judge-authored working/final evaluation evidence | **Scorecard** |
| planned evaluator grouping | **Panel** |
| actor/event relationship or role | **Participation** |
| permission to view/act | **Access** |

No blind `Encounter → Evaluation Occurrence` replacement is permitted because the older abstraction frequently bundled multiple meanings.

## 4.2 `Official Outcome Revision`

`Official Outcome Revision` is deprecated.

Current meaning is owned by **Outcome Declaration**:

```text
current declared official authority    → current Outcome Declaration
materially affected declared authority → Affected Outcome Declaration
explicit corrected official authority  → successor Outcome Declaration
prior declared authority               → Superseded historical Outcome Declaration
```

Competition Finalization remains separate lifecycle closure and Publication remains separate release authority.

## 4.3 Readiness and reconciliation

The following do not become Concepts or editable workflow state through mapping:

```text
Ready to Judge
Competition Ready
Ranking Readiness
Finalization Readiness
Reconciliation issue/work context
Coverage
Aggregate
Rank
```

They remain derived mechanisms/projections/process context. Mapping may make them prominent, explainable and actionable only through their legitimate source owners.

## 4.4 Role mode

`Judge mode`, `Organizer mode`, navigation area or selected work mode is an experience organization/disclosure context.

It does not create:

- Identity;
- Participation;
- Access;
- Competition authority;
- evaluation responsibility;
- semantic authorship.

## 4.5 Completion/finality vocabulary

Phase 013 must qualify finality by subject.

```text
Evaluation Occurrence completed
!= Evaluation Obligation satisfied
!= Scorecard Finalized
!= Competition Event Completed
!= Competition Finalized
!= Outcome Declaration official
!= Export generated
!= Publication released
!= transport delivered
```

# 5. Reference-routing reconciliation

Current composition authority is the seven-owner synchronization set under `docs/canonical/synchronizations/`.

`docs/canonical/synchronizations/concept-synchronizations.md` remains historical routing evidence only.

Therefore later mapping records must route application-action/composition questions to:

- `application-action-surface-composition.md` for D/C/P/S/X application action authority; and
- the relevant one of the six cohesive synchronization-family owners for cross-Concept consequences.

An older Experience file that still links to the archival adapter does not make that adapter current; the file remains admitted evidence until its assigned workstream rewrites the reference.

# 6. Current-owner terminology repairs

013-B inspected the current mapping-relevant policy corpus because 013-A identified stale `Encounter` usage outside Experience evidence.

Two active semantic clauses require bounded repair, with no semantic redesign:

1. `policies/anonymity-disclosure.md`
   - old: exposure may require invalidating an affected `Encounter/evidence`;
   - current: exposure may require invalidating an affected **Evaluation Occurrence and/or dependent evaluation evidence**, followed by legitimate replacement/rejudge semantics.

2. `policies/operational-exception-governance.md`
   - old: an exception cannot rewrite who participated in an `Encounter`;
   - current: an exception cannot rewrite who actually participated in an **Evaluation Occurrence**.

Historical phase filenames/source links containing `encounter` remain valid provenance references and are not renamed.

The current policy review otherwise aligns with the converged vocabulary: Evaluation Occurrence/Obligation, Scorecard, Outcome Declaration, Export and Publication are already used by their natural owners.

# 7. Mapping-knowledge ownership rules

The durable Phase-013 corpus follows these rules:

1. **One natural owner per reusable mapping rule.**
2. Concept definitions remain in `canonical/concepts/`; Experience references them rather than restating them.
3. Synchronization/action authority remains in `canonical/synchronizations/`; Experience owns what must be perceivable/invocable/understandable.
4. Dependence/PF-01 scope remains in `canonical/dependence/`; mapping does not turn dependence into navigation.
5. Policy/invariant truth remains in its natural policy/invariant owner.
6. Derived mechanisms remain derived; mapping does not create writable source state.
7. Exploratory representations and rejected alternatives stay in numbered phase evidence unless they establish durable semantic obligations.
8. A screenshot, route, component, page or work-area name never becomes authority merely by being familiar.
9. Empty placeholder owners are not created in advance; a new canonical file is created when its workstream has substantive current mapping knowledge to own.
10. Superseded Experience documents remain discoverable as provenance but are removed from current-authority navigation.

# 8. Mapping-risk disposition after 013-B

013-B does not claim to close the substantive mapping risks. It makes their ownership explicit.

| Risk | 013-B status |
| --- | --- |
| MAP-R01 `Encounter` collapse | **Contained / routed** — deprecated term prohibited as current; C/E/G perform substantive replacement by meaning. |
| MAP-R02 `Official Outcome Revision` | **Contained / routed** — Outcome Declaration is sole current owner; H performs substantive mapping. |
| MAP-R03 raw Concept action leakage | **Carried** — application action surface established; C–I/K validate mapping. |
| MAP-R04 Identity/Participation/Access collapse | **Carried to 013-C**. |
| MAP-R05 Panel/participant/responsibility/evidence collapse | **Carried to D/E/G/K**. |
| MAP-R06 Draft/persistence/authority collapse | **Carried to E/F/J**. |
| MAP-R07 missing/zero/incomplete/exception collapse | **Carried to G/H/J**. |
| MAP-R08 Rank/Award/declaration collapse | **Carried to G/H/K**. |
| MAP-R09 official/Export/Publication/delivery collapse | **Carried to H/I/K**. |
| MAP-R10 correction/history → edit/delete | **Carried to F/H/I/J**. |
| MAP-R11 PF-01 profile/product confusion | **Carried to G–K**. |
| MAP-R12 semantic parity loss | **Carried to J + C–I parity checks**. |
| MAP-R13 navigation/role mode creates authority | **Baseline rule established; substantive validation in C/K**. |
| MAP-R14 derived projections appear writable | **Baseline rule established; substantive validation in D/G/K**. |
| MAP-R15 technical privilege creates domain authority | **Baseline rule established; substantive validation in C/F/J/K**. |
| MAP-R16 old document boundaries dictate semantics | **Ownership-level defect closed** — split/retain plan is now explicit; K verifies final corpus. |

# 9. Upstream reopen audit

No corpus conflict exposed missing upstream semantics.

```text
Purpose conflict                              NO
missing Concept                               NO
Concept boundary defect                       NO
missing application action                    NO
missing synchronization family                NO
incorrect dependence edge                     NO
incorrect PF-01 scope                         NO
new product variant required                  NO
mapping-only terminology/ownership work       YES
```

Therefore Phases 010, 011 and 012 remain closed.

# 10. Implementation-contamination audit

013-B introduces no:

- route or screen hierarchy;
- frontend framework/component decision;
- CSS/design-system decision;
- client state model;
- API/transport contract;
- persistence schema;
- AWS/runtime topology;
- executable prototype/test;
- implementation-owned workflow state.

The owner topology is documentation/semantic ownership, not component or service decomposition.

# 11. Canonical outputs

013-B establishes:

- `docs/canonical/experience/mapping-authority-baseline.md` — durable mapping authority/evidence/ownership baseline;
- updated `docs/canonical/experience/index.md` — current navigation and corpus status;
- bounded terminology repairs in the natural current policy owners;
- updated repository/Phase-013 routing showing 013-B complete and 013-C next.

The ten old Experience contracts remain admitted evidence until their assigned workstreams accept, rewrite, split, merge or supersede them.

# 12. 013-C handoff

The next substantive mapping work is:

> **013-C — Context, Identity, Participation, Access, Bias-Control & Judge Entry Mapping**

013-C starts from this baseline and must map how a person understands:

- which Competition/context they are operating in;
- which Identity is active;
- what current Participation they hold;
- what Access permits now;
- what a Judge/Organizer mode does and does not mean;
- what Team identity/disclosure is intentionally visible;
- how event-day Judge entry/check-in/readiness works conceptually;
- how multiple capacities/contexts remain isolated;
- how revoked/stale/expired context is represented;
- how support recovery restores technical context without manufacturing domain authority.

It must consume current Identity, Participation, Access, Alias, Competition and relevant synchronization/policy authority rather than copying the old `context-role-modes.md` or `judge-onboarding.md` contracts verbatim.

# Final state

```text
013-A  COMPLETE — READY
013-B  COMPLETE — PASS
013-C  NEXT
013-D–L PLANNED
architecture authority: SUSPENDED
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```
