# 002-A1 — Team Extensible Attributes & Team Name Refinement

Status: **Complete**

## 1. Purpose

This refinement extends the completed 002-A Team specification without changing the accepted Concept catalog or the Team concept's core purpose.

The need is straightforward: a Team may carry descriptive or event-specific information that is useful, enjoyable, or operationally convenient without affecting the Competition's evaluation semantics. A student-created Team name is the immediate example.

The refinement establishes:

```text
Team
    stable identity
    Competition scope
    participation status
    administrative record
    descriptive attributes
```

`teamName` is a standard optional descriptive Team attribute.

It is **not**:

- the Team Alias / Competition Identity;
- the Team's stable internal identity;
- a Division assignment;
- an evaluation input;
- a ranking input;
- an Award input by default;
- an authorization credential.

---

## 2. Team attributes

Team should support an extensible set of Competition-scoped attributes so adding benign event-specific metadata does not require redefining the Team concept or creating a new concept for every field.

Conceptually:

```text
Team Attribute Definition
    key
    human-facing label
    value type
    required / optional
    disclosure classification
    editability / lifecycle policy
    competitive significance

Team Attribute Value
    Team
    attribute key
    value
```

The exact storage representation is an implementation concern. It may eventually use typed columns for common attributes, a schema-driven attribute store, JSON, relational values, or another mechanism. The behavioral requirement is that additional Team metadata can be introduced without polluting scoring, Alias, or ranking semantics.

Attribute definitions are Competition configuration/policy rather than standalone Concepts.

---

## 3. Standard Team name attribute

The initial standard descriptive attribute is:

```text
teamName
```

Purpose:

> Allow students to give their Team a memorable or playful human-facing name without changing how the Competition identifies, evaluates, or ranks that Team.

Examples might include:

```text
Bayes Brigade
Data Dragons
Null Hypothesis
The Outliers
```

The name is optional by default.

A Team without a chosen name remains completely valid.

---

## 4. Team name versus Alias

These two values solve different problems.

```text
Team Name
    expressive / descriptive
    potentially student-selected
    need not be unique

Alias
    operational Competition identity
    unique in Competition scope
    stable enough for judging/paper traceability
    designed for blinded judging
```

For example:

```text
Stable Team:
    internal Team X

Team Name:
    Bayes Brigade

Competition Alias:
    Team 014
```

Judging evidence remains structurally associated with stable Team identity and historical Alias context, never merely with the Team name text.

Changing `Bayes Brigade` to `Bayesians at Work` does not create a new Team and does not alter existing Scorecards.

---

## 5. Competitive significance

The baseline policy for `teamName` is:

```text
competitive significance = None
```

Therefore it does not affect:

- Rubric selection;
- Scorecard calculation;
- Evaluation Coverage;
- Aggregate;
- Rank;
- Award eligibility or selection;
- Panel assignment.

A future attribute with competitive meaning must not acquire that meaning merely because it exists in the Team attribute set. Competitive effects require explicit Competition policy/synchronization.

This prevents a generic metadata facility from becoming a hidden rules engine.

---

## 6. Disclosure classification

Extensible Team attributes require an explicit disclosure posture because the actor who can see administrative Team information may be broader than the audience for a particular representation.

Useful conceptual classifications include:

```text
Organizer-only
Judge-safe
Public-after-approval
```

A single attribute may support more nuanced lifecycle rules later, but disclosure must never be inferred merely from storage location.

### Team name default

A student-created Team name is potentially identifying. It may contain:

- a school reference;
- a local organization reference;
- student names or initials;
- a previously public competition identity;
- another clue that defeats blinded judging.

Therefore the default MUDAC posture is:

```text
Organizer-visible             ✓
Judge-visible during blinded judging  ✗ by default
Public/ceremony use           allowed only when approved by Competition disclosure policy
```

A Competition may deliberately permit Judge-facing Team names if organizers determine that doing so does not undermine the event's identity-shielding goals, but that is an explicit disclosure decision rather than an assumed property of `teamName`.

Alias remains the required Judge-facing identity.

---

## 7. Extensibility rules

The attribute mechanism should satisfy these constraints:

1. Adding a descriptive attribute does not require a new Concept.
2. Attributes are typed/validated according to their definition rather than being an unconstrained arbitrary text bag in the experience model.
3. Attribute definitions can declare required versus optional behavior.
4. Attribute disclosure is explicit.
5. Attribute competitive significance is explicit; the default is no competitive effect.
6. Attribute absence does not make a Team invalid unless the definition is explicitly required by Competition policy.
7. Changing descriptive attributes does not change stable Team identity.
8. Attributes do not replace Division, Alias, Participation status, or other concept-owned relationships.
9. Export/print/publication applies audience disclosure rules to Team attributes just as it does to other Team information.
10. Historical external representations may retain the attribute value they represented at generation time even if the current Team attribute later changes.

---

## 8. Edit and provenance posture

Most descriptive Team attribute edits are low-consequence administrative changes.

Before or during normal event operation, an Organizer may correct them without triggering scoring recalculation.

However, once a value has been materially published or exported, changing it can make external representations stale. Export source/currentness behavior from 002-H applies.

If a Team name is used in an Official Outcome or public Award representation and later corrected, the correction should remain attributable even though it does not alter the underlying scoring result.

---

## 9. Examples of future attributes

The model can later support attributes such as:

```text
teamName
presentationTitle
optionalPronunciation
publicDescription
advisorDisplayName
accessibility/logistics metadata with restricted disclosure
```

without implying that all such attributes belong in the baseline implementation.

Sensitive or student-level information should still be minimized. Extensibility is not justification for indiscriminate data collection.

---

## 10. Revised Team state contract

The conceptual Team state from 002-A is refined to:

```text
Team
    stable id
    Competition scope
    participation status
    administrative record
    descriptive attributes
        teamName?         # standard optional attribute
        ...               # Competition-defined extensions
```

Division and Alias remain independent concepts/synchronizations.

The Team continues to own neither ranking nor judging relationships.

---

## 11. Invariants added by this refinement

1. Team descriptive attributes never replace stable Team identity.
2. `teamName` is optional by default.
3. `teamName` need not be unique.
4. Team Name and Alias are semantically distinct.
5. Alias remains the canonical Judge-facing Competition Identity during blinded judging.
6. Team attributes have no competitive effect unless explicitly declared by Competition policy.
7. Team-attribute disclosure is audience/lifecycle-aware rather than inferred from Organizer visibility.
8. Student-created Team names are not Judge-visible by default while institutional identity shielding is active.
9. Attribute changes do not mutate existing Scorecards or Encounters.
10. Extensible attributes must not become an ungoverned hidden policy mechanism.

## Exit position

This refinement does not expose a missing Concept.

It strengthens Team as an extensible administrative competitor model while preserving the existing boundaries:

```text
Team
    who/what the competitor is administratively

Alias
    how the competitor is safely identified for judging

Division
    which competitive population the Team belongs to

Team Attributes
    additional descriptive metadata with explicit disclosure and significance
```

Phase 003 should treat Team names and other descriptive attributes as presentation data whose visibility depends on role and disclosure policy, not as identity or evaluation semantics.
