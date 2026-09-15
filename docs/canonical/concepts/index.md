# MUDAC Concepts

Current canonical Concept catalog after Phase 010 modularity convergence and exit.

Each Concept owner exposes representation-independent Purpose, State, Actions/Queries, Operational Principle, intrinsic authority/history semantics where relevant, and explicit boundaries. Contextual MUDAC inclusion requirements belong to [Canonical Dependence](../dependence/), not intrinsic Concept definitions.

## Current eighteen-Concept catalog

1. [Competition](competition.md) — lifecycle and governing context for one competition occurrence.
2. [Division](division.md) — scoped competitive cohort definition and member assignment.
3. [Team](team.md) — stable scoped administrative competitor representation.
4. [Panel](panel.md) — reusable scoped grouping of evaluator members.
5. [Evaluation Occurrence](evaluation-occurrence.md) — bounded historical evaluation occurrence and actual presented/participant context.
6. [Evaluation Obligation](evaluation-obligation.md) — one evaluator's responsibility to produce a qualifying independent evaluation.
7. [Rubric](rubric.md) — structured evaluation instrument and response interpretation/validation semantics.
8. [Scorecard](scorecard.md) — one evaluator's independent judgment under supplied context and evaluation basis.
9. [Award](award.md) — scoped recognition definition and attributable conferral.
10. [Identity](identity.md) — stable human identity continuity independent of event capacity/permission.
11. [Participation](participation.md) — scoped, time-bounded involvement in a particular capacity.
12. [Alias](alias.md) — scoped alternate identity preserving historical mapping.
13. [Access](access.md) — contextual capability/disclosure decision over supplied facts and rules.
14. [Versioning](versioning.md) — immutable authoritative-state lineage, eligibility, invalidation and currentness.
15. [Provenance](provenance.md) — meaningful origin, actor, represented-authority and correction history.
16. [Outcome Declaration](outcome-declaration.md) — explicit declared outcome authority with Affected/successor history.
17. [Export](export.md) — stable source-bound external representation and representation currency.
18. [Publication](publication.md) — deliberate release/withdrawal/supersession of an identified representation.

## Superseded Concept boundary

[Judging Encounter](judging-encounter.md) remains only a deprecated historical adapter. Its former responsibilities are owned by **Evaluation Occurrence + Evaluation Obligation**.

## Explicit non-Concept classifications

Current non-Concept knowledge remains under [Mechanisms](../mechanisms/), [Policies](../policies/), [Invariants](../invariants/), and [Experience](../experience/).

Coverage/Evaluation Sufficiency is derived factual sufficiency; Aggregate, Rank and Readiness are derived mechanisms; Reconciliation is Organizer process/work context; Recovery/Continuity is a cross-cutting purpose obligation; correction remains owner-specific behavior/composition.

## Current composition authority

Phase 011 is complete. Current composition rules live under [Canonical Synchronizations](../synchronizations/).

Preserve:

- occurrence participation ≠ responsibility ≠ Scorecard evidence;
- historical satisfaction ≠ current evidence eligibility;
- Rank ≠ Award authority;
- Competition Finalization ≠ Outcome Declaration;
- calculated ≠ recognized ≠ official ≠ public ≠ delivered;
- source authority ≠ Export representation ≠ Publication release.

## Active methodology work — Phase 012

Current durable dependence lives in [MUDAC Application-Family Concept Dependence](../dependence/application-family-dependence.md), now partial through 012-F.

Current outcome edges are:

```text
Award               → Competition
Award               → Team
Outcome Declaration → Competition
```

These are contextual application dependencies and do not modify the independent Award, Competition, Team, or Outcome Declaration specifications.

Recognition and declaration remain independent:

```text
Award               ↛ Outcome Declaration
Outcome Declaration ↛ Award
```

Do not rewrite Outcome Declaration to directly depend on Team, Scorecard, Evaluation Obligation, Evaluation Occurrence, or Rubric merely because its supplied OutcomeBasis can be traced to those sources.

Do not rewrite Award to depend universally on Division; current rank-derived recognition is Division-contextual because the current Rank mechanism is Division-scoped, while discretionary/competition-wide recognition remains coherent without Division.

012-E authority-profile rules remain contextual rather than intrinsic:

```text
Authoritative Rubric Basis
  ⇒ Versioning + Provenance

Authoritative Scorecard Evidence
  ⇒ Versioning + Provenance
```

Likewise do not rewrite Outcome Declaration as a Versioning wrapper; it intrinsically owns declaration/currentness/successor history.

No Phase-010 Concept owner requires reopening from 012-F.

Next: **012-G — External Representation & Release Dependence**.
