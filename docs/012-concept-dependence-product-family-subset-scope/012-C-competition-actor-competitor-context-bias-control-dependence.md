---
type: Phase Design Record
title: 012-C — Competition, Actor, Competitor Context & Bias-Control Dependence
description: "Resolves Phase 012 candidate dependence for Competition, Team, Identity, Participation, Access, Division, Alias and Panel; establishes the first accepted direct MUDAC inclusion edges, rejects transitive/redundant or over-broad edges, distinguishes capability constraints from graph dependencies, and hands evaluation-side dependence to 012-D."
status: stable
tags: [phase-012, dependence, competition, identity, participation, access, team, division, alias, panel, bias-control]
sources:
  - resource: 012-A-dependence-scope-subset-semantics-product-family-questions-subphase-planning.md
  - resource: 012-B-application-family-boundary-concept-inclusion-roles-candidate-dependence-inventory.md
  - resource: ../canonical/project/mandate-context.md
  - resource: ../canonical/project/purpose-needs-success-tensions.md
  - resource: ../canonical/concepts/competition.md
  - resource: ../canonical/concepts/team.md
  - resource: ../canonical/concepts/identity.md
  - resource: ../canonical/concepts/participation.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/concepts/division.md
  - resource: ../canonical/concepts/alias.md
  - resource: ../canonical/concepts/panel.md
  - resource: ../canonical/synchronizations/competition-participation-access.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/policies/anonymity-disclosure.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-15T11:26:00-05:00 }
---

# Purpose

Resolve the first bounded family of Phase 012 inclusion-dependence questions for the current MUDAC application family.

This subgroup considers:

- Competition;
- Team;
- Identity;
- Participation;
- Access;
- Division;
- Alias;
- Panel.

It decides which candidate relationships from 012-B become current direct extrinsic-dependence edges, which are better represented as transitive consequences, which are conditional capability/scope rules rather than graph edges, and which are rejected.

It does not resolve Evaluation Occurrence, Evaluation Obligation, Rubric, Scorecard, Versioning, Provenance, Award, Outcome Declaration, Export or Publication dependence. Those remain owned by 012-D through 012-G.

# Decision summary

**PASS — first accepted MUDAC dependence edges established.**

The current direct relation for the 012-C family is intentionally sparse:

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

These six edges are contextual to the **MUDAC live student data competition judging-and-outcome family**. They do not change the intrinsic generic definitions of the participating Concepts.

The following consequences are intentionally represented transitively rather than by duplicate direct edges:

```text
Division → Team → Competition
Alias    → Team → Competition
Panel    → Participation → Competition
Panel    → Participation → Identity
```

No universal direct dependence is accepted from Access to Identity or Participation.

No universal direct dependence is accepted from Competition to Division, Panel or Alias.

No universal direct dependence is accepted from Team to Alias.

The first durable canonical dependence owner may now be established because Phase 012 has accepted actual edges rather than only candidate hypotheses.

# 1. Dependence semantics used here

For each accepted edge:

```text
A → B
```

means:

> within the current MUDAC application family, every coherent subset containing A also contains B because A otherwise loses the application role for which it is included.

This does **not** mean:

- A is intrinsically specified in terms of B;
- A owns B state;
- A synchronizes with every action of B;
- B must exist because current code references it;
- B must be shown in the same UI;
- A and B are one product module;
- the edge determines implementation order.

# 2. Family-level Competition anchor

## 2.1 Current conclusion

Competition is the application-family anchor for MUDAC.

Every **in-scope MUDAC product/application variant** must retain a Competition context because the project mandate is specifically the operational judging and outcome lifecycle of a live student data competition.

This is a **family-scope rule**, not an outgoing graph edge from Competition to every other Concept.

A dependence-valid subset containing only reusable generic Concepts such as Identity, Rubric, Export or Access may be conceptually possible in another application or as a supporting tool, but it is not by itself an in-scope MUDAC application variant unless it participates in the current competition family role.

## 2.2 Why no `Competition → X` blanket edges

Family anchoring does not mean Competition requires every capability.

MUDAC may coherently contemplate:

- one cohort without Division;
- ad-hoc evaluator assignment without Panel;
- official outcome without Publication;
- judging without Award;
- internal operation without external release.

The family anchor constrains scope selection; it does not force the full eighteen-Concept set into every variant.

# 3. Accepted direct edge: Team → Competition

<a id="dep-c-001"></a>
## DEP-C-001 — Team requires Competition in MUDAC

```text
Team → Competition
```

### Rationale

Team's intrinsic form remains generic as `Team<Scope>`, but within MUDAC its application role is **one student group participating as a competing unit in a particular competition**.

Without Competition, Team becomes a generic roster/registry concept rather than the current project's competing-unit role.

### Counterexample tested — reusable pre-event Team registry

A reusable cross-event Team registry is conceptually plausible, but it would not be the current Team role established by the MUDAC mandate. It would either:

- be upstream administration outside the current product-family boundary;
- require a different Scope meaning/product role; or
- motivate future scope/design work rather than invalidate the present edge.

Therefore the candidate counterexample does not defeat the contextual dependence.

### Consequence

Any dependence-valid MUDAC subset containing Team also contains Competition.

# 4. Accepted direct edges: Participation → Competition and Participation → Identity

<a id="dep-c-002"></a>
## DEP-C-002 — Participation requires Competition in MUDAC

```text
Participation → Competition
```

### Rationale

Participation's MUDAC role is one human taking part in one Competition in a time-bounded capacity such as Judge or Organizer.

The generic Concept remains `Participation<Participant, Scope, Capacity>`, but the current application binds Scope to Competition. A reusable evaluator pool outside a particular event is not a Participation episode under current semantics.

### Counterexample tested — reusable evaluator pool

A persistent evaluator pool may be useful, but the persistent human continuity belongs to Identity. Event-specific capacity remains Participation. Treating the pool itself as Participation would collapse the separation established by Phase 010/011.

Therefore the counterexample does not defeat this edge.

<a id="dep-c-003"></a>
## DEP-C-003 — Participation requires Identity in MUDAC

```text
Participation → Identity
```

### Rationale

MUDAC needs participation to remain attributable to a stable human across:

- check-in and active work;
- interruption/recovery;
- correction/history;
- represented authorship;
- future competitions without reviving old event capacity.

P-03, P-07 and P-08 require low-friction participation **without erasing trustworthy attribution or authority separation**.

### Counterexample tested — ephemeral anonymous Judge

A purely anonymous/ephemeral principal could technically submit values, but it cannot satisfy the current MUDAC need to preserve who performed Judge work, distinguish actor from semantic authority where necessary, support legitimate recovery/correction, and prevent stale/ambiguous authority from being silently reused.

The counterexample therefore represents a different product-purpose posture rather than a coherent current MUDAC variant.

### Consequence

Any MUDAC subset containing Participation includes both Competition and Identity.

Identity itself does **not** depend on Competition or Participation. It remains meaningful as reusable continuity across competition occurrences.

# 5. Access — no universal peer edge accepted

## 5.1 `Access → Participation` rejected as universal direct dependence

012-B classified this as conditional. 012-C does **not** promote it to a universal graph edge.

Access is intrinsically generic over Principal, Capability, Resource, ContextFacts and Rule. Within MUDAC, protected Judge/Organizer operations normally supply one explicit Participation context, but Access also supports:

- technical/support authority boundaries;
- exceptional grants;
- purpose-specific disclosure decisions;
- potentially public/external resource contexts where ordinary Competition Participation is not the relevant source of authority.

Therefore:

```text
Access ↛ Participation     universal edge rejected
```

### Conditional application rule retained

For a protected action performed **in Judge or Organizer Competition capacity**, the current application composition requires a legitimate current Participation context.

This remains a capability/composition condition, not a universal Concept-inclusion edge.

## 5.2 `Access → Identity` rejected as universal direct dependence

Access may commonly consume an Identity-backed principal, but it can evaluate supplied principals/context without owning or universally requiring durable Identity.

Technical/support and external/disclosure contexts again provide legitimate counterexamples.

Therefore:

```text
Access ↛ Identity          universal edge rejected
```

### Transitive practical effect for normal human competition work

Normal Judge/Organizer protected actions typically use:

```text
Participation → Identity
Participation → Competition
        +
Access.check(current Participation context)
```

That composition is strong and mandatory for those operations without turning Access into a peer-dependent Concept.

# 6. Accepted direct edge: Division → Team

<a id="dep-c-004"></a>
## DEP-C-004 — Division requires Team in MUDAC

```text
Division → Team
```

### Rationale

Division's current MUDAC role is to partition competing Team members into mutually exclusive competitive cohorts.

A Division definition may exist before any concrete Team has been assigned, but the **Concept inclusion role** still targets Team membership. The edge concerns availability of the Team Concept in the subset, not cardinality of Team instances at one moment.

### Why no direct `Division → Competition` edge is recorded

Because:

```text
Division → Team → Competition
```

already establishes Competition transitively.

A separate direct edge would be true in application language but redundant in the minimal dependence graph.

# 7. Division is not required by Competition

## 7.1 `Competition → Division` rejected

The single-cohort probe remains conceptually coherent.

A Competition can support one undivided competitive cohort without inventing a placeholder Division merely to satisfy the full-product shape.

Therefore:

```text
Competition ↛ Division
```

Division is an optional/conditional structuring capability.

## 7.2 Current-policy tension: blinded judging says Alias + Division

Current Anonymity and Disclosure policy states that during blinded judging the Judge-facing Team representation is `Alias + Division`.

That policy reflects the present full-product baseline, but it is **not evidence that Division is conceptually required by every Competition**.

012-C therefore carries the following forward:

> A single-cohort no-Division variant is dependence-coherent, but before such a variant can be adopted as in scope, Phase 012-I must revalidate the blinded-judging policy/composition so it does not require a fake Division merely to satisfy historical wording.

This is variant-specific policy/composition revalidation, not a Phase-010 Concept defect and not a reason to add `Competition → Division`.

# 8. Accepted direct edge: Alias → Team

<a id="dep-c-005"></a>
## DEP-C-005 — Alias requires Team in MUDAC

```text
Alias → Team
```

### Rationale

Alias is intrinsically generic over Subject and Scope, but in MUDAC its purpose is to provide a Judge-facing alternate identity for a Team so protected administrative/institutional identity need not be exposed during judging.

Without Team, current MUDAC Alias loses the subject role that justifies its inclusion.

### Why no direct `Alias → Competition` edge is recorded

Because:

```text
Alias → Team → Competition
```

already establishes Competition transitively.

# 9. Team does not universally depend on Alias

## 9.1 `Team → Alias` rejected as a universal edge

Team remains meaningful for:

- Organizer-facing administration;
- pre-judging preparation;
- withdrawal/restoration;
- non-Judge contexts;
- potentially coherent non-blinded or differently represented variants.

Therefore:

```text
Team ↛ Alias
```

### Conditional in-scope bias-control rule

Any MUDAC variant that claims the **current blinded-judging baseline** must provide the bias-control role currently owned by Alias.

Under the present Concept catalog, that means Alias is included for blinded judging.

This is a **variant/capability inclusion rule**, not a universal Team dependency.

### No silent alternate identifier

A no-Alias variant cannot preserve the same blinded-judging claim merely by inventing an implementation-level opaque string outside Concept Design.

If an alternate identity is semantically meaningful and historically controlled, that is precisely Alias behavior under the current catalog.

# 10. Accepted direct edge: Panel → Participation

<a id="dep-c-006"></a>
## DEP-C-006 — Panel requires Participation in MUDAC

```text
Panel → Participation
```

### Rationale

Panel's current application role is reusable grouping of **Judge Participation identities** inside a Competition context.

Using Participation rather than permanent Identity is essential because Panel membership must represent event-scoped Judge capacity, not a permanent human role.

### Counterexample tested — pre-event evaluator pool

A reusable evaluator pool independent of Competition could plausibly group Identities, but that is not the current Panel role. Recasting Panel as a permanent human pool would undermine its scoped semantics and bypass current Participation authority.

### Transitive consequences

Because:

```text
Panel → Participation
Participation → Competition
Participation → Identity
```

Panel therefore transitively requires Competition and Identity.

No duplicate direct `Panel → Competition` or `Panel → Identity` edge is needed.

# 11. Panel is not required by Competition

## 11.1 `Competition → Panel` rejected

Phase 011 intentionally established Panel as reusable intended grouping rather than actual occurrence participation/responsibility.

A coherent MUDAC judging variant can directly establish eligible evaluators/occurrence participants without reusable Panel grouping.

Therefore:

```text
Competition ↛ Panel
```

Panel remains an optional evaluator-organization capability.

### Carry-forward to 012-D

012-D must verify that Evaluation Occurrence/Obligation dependence does not reintroduce Panel indirectly as a mandatory judging prerequisite merely because the ordinary workflow often starts from Panel candidates.

# 12. Identity does not depend on Competition or Participation

Identity is deliberately reusable across competitions and exists independently of current event capacity.

Therefore:

```text
Identity ↛ Competition
Identity ↛ Participation
```

This preserves the distinction:

```text
who the human is
  ≠
what event/capacity the human currently participates in
```

A future application might use Identity for a person who is not currently participating in any Competition; that remains coherent within MUDAC support/reuse context.

# 13. Competition does not depend on Team as a direct graph law

012-C does **not** add:

```text
Competition → Team
```

The project family is defined around competition judging/outcomes and any adopted full judging variant will necessarily involve competitors, but dependence analysis should not convert a useful **family/product-role minimum** into an intrinsic-looking edge without need.

A Competition may coherently exist during setup before Teams are created, and Concept inclusion does not require that every lifecycle state contain Team instances.

Whether every **in-scope adopted Phase-012 product variant** must include Team is therefore left to 012-H/012-I subset/scope analysis rather than encoded here as a direct Competition dependency.

# 14. Direct graph after 012-C

Current accepted direct edges are:

```text
Participation ─────→ Identity
       │
       └───────────→ Competition

Team ──────────────→ Competition
  ▲
  ├──────── Division
  └──────── Alias

Panel ─────────────→ Participation
```

Equivalent edge set:

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

# 15. Transitive closure relevant to this family

Derived transitive consequences include:

```text
Division → Team → Competition
Alias    → Team → Competition
Panel    → Participation → Competition
Panel    → Participation → Identity
```

Transitive reachability is not duplicated as direct canonical edges unless later analysis shows a distinct rationale that must survive removal/change of the intermediate relationship.

# 16. Explicit non-edges after 012-C

Current explicit non-edge conclusions include:

```text
Competition ↛ Division
Competition ↛ Panel
Team        ↛ Alias
Identity    ↛ Competition
Identity    ↛ Participation
Access      ↛ Participation   (universal)
Access      ↛ Identity        (universal)
```

And the following candidate direct edges are intentionally omitted as redundant because they are already transitive:

```text
Division → Competition
Alias    → Competition
Panel    → Competition
Panel    → Identity
```

# 17. Conditional capability/scope rules — not graph edges

Some inclusion requirements are real but cannot be represented honestly as a universal `A → B` edge.

## 17.1 Protected Judge/Organizer operation

When an operation is performed in Judge/Organizer Competition capacity:

- Participation is required as the current capacity context;
- Access evaluates that supplied context;
- Participation already requires Identity and Competition.

This is an action/capability condition, not `Access → Participation` for all Access uses.

## 17.2 Blinded judging

A variant claiming current blinded judging includes Alias as the current alternate-identity owner.

Current policy additionally expects Division in the Judge-facing representation; no-Division variant adoption requires later policy/composition revalidation.

This is not `Team → Alias` or `Competition → Division` as universal graph law.

## 17.3 Multi-cohort competition

A variant that supports distinct competitive cohorts includes Division.

This is a capability requirement; Competition itself remains valid without Division.

## 17.4 Reusable evaluator grouping

A variant that supports reusable intended evaluator groups includes Panel.

Ad-hoc assignment can omit Panel.

# 18. Representative subset pressure tests

## 18.1 Single-cohort competition without Division

Candidate subset fragment:

```text
Competition
Team
Alias (for blinded judging)
Identity
Participation
Access
...
```

Dependence result: **valid with respect to 012-C direct edges**.

Current-policy status: **requires later policy/composition revalidation** because DISC-001 currently names Division as part of blinded Judge representation.

This does not justify adding Division as a dependence edge.

## 18.2 Ad-hoc judging without Panel

Candidate subset fragment:

```text
Competition
Team
Identity
Participation
Access
...
```

with evaluators selected directly for later Evaluation Occurrences.

Dependence result: **valid with respect to 012-C**.

012-D must verify the evaluation family remains coherent without Panel.

## 18.3 Panel without Participation

Invalid under current 012-C dependence:

```text
Panel
(no Participation)
```

Panel loses its MUDAC role as grouping of event-scoped Judge capacities.

## 18.4 Participation without Identity

Invalid under current 012-C dependence.

The ephemeral anonymous-participant counterexample does not satisfy current MUDAC attribution/authority/recovery purpose.

## 18.5 Team without Alias

Dependence-valid under the direct graph.

Whether such a subset can be **in scope** depends on the claimed product role:

- Organizer/admin-only use may be coherent;
- current blinded judging is not coherent without the Alias role;
- a non-blinded judging product would require an explicit scope/purpose decision and must still satisfy P-02/P-08.

This distinction is reserved for 012-H/012-I scope selection.

# 19. No Concept-boundary repair required

The accepted dependence edges are all **extrinsic/contextual**.

They do not reveal that any Concept is intrinsically specified in terms of another peer:

- Team remains generic over Scope;
- Participation remains generic over Participant/Scope/Capacity;
- Division remains generic over Scope/Member;
- Alias remains generic over Subject/Scope;
- Panel remains generic over Scope/Member;
- Identity and Access remain independently specified.

Therefore Phase 010 does not need reopening.

# 20. No Phase-011 composition repair required yet

The accepted edges are compatible with current synchronization semantics.

The only bounded carry-forward is the single-cohort no-Division policy/composition question. That does not yet require changing Phase 011 because 012-I must first decide whether the no-Division variant is adopted into scope.

If adopted, the natural current policy/synchronization owner must be generalized without manufacturing placeholder Division state.

# 21. Canonical dependence promotion

012-C is the first Phase 012 subgroup to establish durable dependence truth.

Therefore current accepted direct edges and non-edge/conditional interpretation may now be promoted to a compact canonical dependence owner.

The canonical owner must:

- identify the MUDAC application-family context;
- record only accepted current direct edges;
- distinguish direct edges from transitive consequences;
- distinguish conditional capability/scope rules from graph edges;
- remain explicitly partial while 012-D through 012-G are unresolved;
- avoid duplicating full Concept specifications or synchronization contracts.

# 22. Handoff to 012-D

012-D now owns evaluation-side candidate relationships, including:

- Evaluation Occurrence → Competition / Team / Participation;
- Evaluation Occurrence → Panel / Alias / Division / Rubric challenges;
- Evaluation Obligation → Competition / Participation / Team / Rubric;
- Evaluation Obligation → Evaluation Occurrence challenge;
- Scorecard → Participation / Team / Rubric;
- Scorecard → Evaluation Occurrence / Evaluation Obligation challenges;
- Rubric → Competition challenge.

012-D must use the accepted 012-C edges transitively rather than duplicating context dependencies unnecessarily.

For example, if a later accepted edge is:

```text
Evaluation Occurrence → Participation
```

then Competition and Identity already follow through current 012-C dependence.

Likewise, if:

```text
Evaluation Occurrence → Team
```

then Competition follows through Team.

This keeps the final graph minimal and explanatory.

# Exit decision

**PASS — 012-C complete.**

Current accepted direct edge set:

```text
DEP-C-001  Team          → Competition
DEP-C-002  Participation → Competition
DEP-C-003  Participation → Identity
DEP-C-004  Division      → Team
DEP-C-005  Alias         → Team
DEP-C-006  Panel         → Participation
```

Key explicit non-edges:

```text
Competition ↛ Division
Competition ↛ Panel
Team        ↛ Alias
Identity    ↛ Competition
Identity    ↛ Participation
Access      ↛ Participation   universal
Access      ↛ Identity        universal
```

No upstream Concept repair is required.

No implementation authority is created.

Next:

> **012-D — Evaluation Structure, Responsibility, Basis & Judgment Dependence**
