---
type: Validation Record
title: 016-C — Competition Context, Competitor Structure, Identity, Participation, Alias, Access & Bias-Control Scenario Validation
description: "Validates contextual identity, capacity, participation, competitor representation, alias, disclosure and access semantics under realistic blinded-judging and multi-capacity scenarios."
status: stable
tags: [phase-016, identity, participation, alias, access, bias-control, disclosure, scenario-validation]
sources:
  - resource: 016-A-validation-scope-misfit-hypotheses-risk-coverage-subphase-planning.md
  - resource: 016-B-archetypal-scenario-progressive-disclosure-purpose-preservation-baseline-validation.md
  - resource: ../canonical/concepts/
  - resource: ../canonical/synchronizations/
  - resource: ../canonical/experience/
---

# Purpose

016-C removes the simple-identity assumption from the archetypal baseline.

The governing question is:

> Can MUDAC preserve fair, bias-sensitive judging when identity, participation, representation, access and disclosure are composed realistically rather than treated as isolated fields?

Primary inherited targets:

- **SVT-01** — blinded judging under realistic participation/disclosure conditions;
- **SVT-02** — multi-capacity actor with stale or changing disclosure.

SVT-13 remains for degraded-operation replay in 016-I.

# Semantic distinctions

016-C requires preservation of:

```text
person / actor identity
  != capacity in context
  != participation
  != competitor
  != competitor membership
  != alias / blinded representation
  != access entitlement
  != disclosure permission
  != evaluation responsibility
```

A person's total knowledge does not define what MUDAC is authorized to disclose to that person in a particular capacity.

A legitimate participant does not automatically gain every representation associated with the competition.

# Contextual-authority rule

Authority, disclosure and access are contextual rather than globally attached to actor identity.

The design must be capable of interpreting:

```text
who is this actor acting as
  + in relation to which competition object
  + for what legitimate purpose
  + under what disclosure conditions
```

without turning this into an implementation-specific authorization architecture.

# Scenario validation

## IC-01 — Ordinary blinded competitor representation

A competitor remains a durable competition entity while a Judge sees an assigned alias/identifier such as `Team 104`.

The alias is a contextual representation; it is not literally the competitor's identity.

**Disposition: FIT.**

## IC-02 — Alias changes without competitor replacement

An alias may be corrected or changed without creating a new competitor, new participation or new evaluation responsibility.

Historical association remains preservable.

**Disposition: FIT — BOUNDARY CLARIFICATION.**

**BC-016C-01:** Alias is contextual representation, not durable competitor identity.

## IC-03 — One person holds multiple capacities

A person may be Organizer in one context and Judge in another.

Organizer access must not automatically enlarge the Judge-facing disclosure surface.

**Disposition: FIT — BOUNDARY CLARIFICATION.**

**BC-016C-02:** Capacity is contextual; multiple capacities do not automatically union authority or disclosure.

## IC-04 — Judge has prior independent knowledge

A Judge may recognize a competitor from real-world knowledge even when MUDAC withholds identity.

Bias control means controlling platform disclosure and conflict-handling semantics; it cannot guarantee human ignorance.

**Disposition: FIT.**

## IC-05 — Identity leakage through associated metadata

A Judge-facing artifact may reveal identity through affiliation, filename, logo, URL, byline, document metadata or narrative content.

Hiding a canonical identity field alone is not enough to prove blinded presentation.

**Disposition: FIT — BOUNDARY CLARIFICATION.**

**BC-016C-03:** Bias control applies to the effective identity-bearing representation exposed in context, not only explicit identity fields.

## IC-06 — Team name itself is identifying

A team name may be valid competition data yet inappropriate to expose in blinded judging.

Visibility is contextual; the attribute need not disappear from the model.

**Disposition: FIT.**

## IC-07 — Access exists for one purpose but not another

An Organizer may legitimately access competitor identity for participation verification while not needing that identity in a coverage-monitoring surface.

**Disposition: FIT — BOUNDARY CLARIFICATION.**

**BC-016C-04:** Legitimate access is purpose-relative, not merely account-relative.

## IC-08 — Participation changes after assignments exist

A Judge may withdraw or a capacity may change after responsibilities were created.

The model must preserve historical participation while allowing current actionability to differ.

**Disposition: FIT.**

## IC-09 — Newly disclosed relationship creates bias concern

A later-discovered relationship can affect recusal/responsibility without rewriting identity or pretending the Judge never participated.

**Disposition: FIT.**

## IC-10 — Same person participates across competitions

Knowledge or authority in Competition A does not automatically become platform disclosure or authority in Competition B.

**Disposition: FIT.**

## IC-11 — Organizer temporarily also serves as Judge

If competition policy permits dual capacity, the person's substantive evaluation is still Judge-capacity authorship; Organizer identity does not own the judgment.

**Disposition: FIT.**

## IC-12 — Shared affiliation among competitors

Affiliation may be valid administrative data, hidden during judging and later exposed in legitimate public results.

**Disposition: FIT.**

## IC-13 — Competitor composition changes

A team member may be corrected/added/removed according to policy without automatically creating a new competitor.

Competitor and membership/composition remain distinct.

**Disposition: FIT.**

## IC-14 — Different legitimate representations in different contexts

A Judge may see `Team 104`; an Organizer may see `Team 104 — University Example`; a public result may show a named team.

These can remain consistent representations of one authoritative competitor.

**Disposition: FIT.**

# Multi-capacity authority matrix

| Situation | Required interpretation |
| --- | --- |
| Same person holds multiple capacities | valid where policy permits |
| Capacity A has access X | does not imply capacity B should expose X |
| Person knows X outside MUDAC | does not authorize MUDAC to disclose X |
| Actor changes capacity | does not rewrite historical participation |
| New capacity is granted | does not retroactively authorize earlier actions |
| Capacity is removed | does not erase prior legitimate authored work |
| Organizer also acts as Judge | judgment remains Judge-capacity authorship |
| Judge has external relationship | identity remains; responsibility/recusal may change |

# Bias-control result

Bias control is not equivalent to deleting identity.

The mature design can preserve:

- real identity for legitimate administration;
- competitor continuity;
- Judge-facing aliases;
- public-facing names;
- internal provenance;
- contextual disclosure restrictions.

Rejected extremes:

```text
identity everywhere because the platform knows it      REJECTED
identity nowhere because Judges should not see it       REJECTED
contextual representation/disclosure                    RETAINED
```

# Direct SVT dispositions

## SVT-01 — realistic blinded judging

Tested through aliasing, identity-bearing attributes, identifying team names, artifact metadata, prior human knowledge, affiliation, competitor composition and contextual representations.

**Disposition: FIT — BOUNDARY CLARIFICATION.**

Blinding is a property of the effective Judge-facing disclosure surface, not merely suppression of one identity field.

## SVT-02 — multi-capacity/changing disclosure

Tested through Organizer+Judge overlap, capacity change, cross-competition capacity, newly disclosed relationships, changing participation and prior authorized access.

**Disposition: FIT — BOUNDARY CLARIFICATION.**

Actor identity must not collapse multiple capacities into one global authority/disclosure envelope.

# Additional boundary clarifications

**BC-016C-05 — Human knowledge and platform disclosure are distinct.**  
MUDAC cannot guarantee lack of prior knowledge; it must preserve correct disclosure/conflict semantics.

**BC-016C-06 — Historical capacity remains historical truth.**  
Changing current participation/capacity does not erase legitimate prior participation or authored actions.

# Validated invariants

1. Access to identity-bearing information derives from legitimate context, not actor existence.
2. A representation may expose less information than the authoritative entity contains.
3. Multiple legitimate representations may refer to the same competitor.
4. Alias changes do not necessarily alter competitor identity.
5. Person identity does not collapse multiple capacities.
6. Capacity does not inherit every entitlement of another capacity.
7. Current participation changes do not erase historical truth.
8. Bias control includes indirect identity-bearing representation.
9. Prior human knowledge does not redefine platform disclosure authority.
10. Administrative access does not imply universal exposure.

# Cross-phase handoff

016-D must validate recusal, newly discovered conflict, Judge withdrawal, participation change after responsibility assignment and coverage consequences.

016-E must validate historical truth after capacity/alias/association changes.

016-G must validate post-publication identity/disclosure/currentness.

016-I must replay these scenarios under offline/shared-device/stale-session/recovery pressure.

# Validation register

| Probe | Disposition |
| --- | --- |
| IC-01 ordinary blinded representation | FIT |
| IC-02 alias change | FIT — CLARIFICATION |
| IC-03 multi-capacity person | FIT — CLARIFICATION |
| IC-04 prior knowledge | FIT |
| IC-05 indirect identity leakage | FIT — CLARIFICATION |
| IC-06 identifying team name | FIT |
| IC-07 purpose-relative access | FIT — CLARIFICATION |
| IC-08 participation change | FIT |
| IC-09 newly disclosed relationship | FIT |
| IC-10 cross-competition actor | FIT |
| IC-11 Organizer + Judge | FIT |
| IC-12 affiliation visibility | FIT |
| IC-13 competitor composition | FIT |
| IC-14 contextual representations | FIT |
| SVT-01 | FIT — CLARIFICATION |
| SVT-02 | FIT — CLARIFICATION |

```text
semantic misfits          0
reopens required          0
semantic repairs          0
boundary clarifications   6
unresolved local probes   0
```

# Gate contribution

- **V1 Archetypal fit — FURTHER SUPPORTED**
- **V2 Exceptional fit — PARTIALLY SUPPORTED**
- **V3 Authority integrity — PARTIALLY SUPPORTED**
- **V8 Bias/privacy preservation — SUBSTANTIALLY SUPPORTED**
- **V9 Cross-family coherence — FURTHER SUPPORTED**

# 016-C decision

**016-C — COMPLETE — PASS**

The mature design survives realistic identity, participation, alias, access and bias-control composition.

It rejects the simplistic model:

```text
actor = role = authority = access
```

and retains context-dependent participation/disclosure while preserving stable actor and competitor identity.

No semantic reopen is required.

Proceed to:

> **016-D — Evaluation Occurrence, Responsibility, Obligation, Recusal, Missingness, Rubric, Scorecard & Judge-Authorship Scenario Validation**
