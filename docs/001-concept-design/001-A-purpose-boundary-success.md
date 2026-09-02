# 001-A — Competition Purpose, Product Boundary & Success

**Status:** Complete  
**Phase:** 001 — Concept Design Foundation

## Purpose

Establish the product's conceptual center before screens, components, infrastructure, or authentication technology are chosen.

## Product purpose

MUDAC should enable a live academic data competition to conduct **fair, traceable, efficient, multi-perspective evaluation of student Teams while minimizing administrative burden and preserving the human interaction at the center of judging**.

The product is not merely a digital replacement for paper scorecards. Its purpose includes coordination of Judge participation, Panel formation, repeated Judging Encounters, independent evaluation, controlled identity disclosure, score provenance, aggregation, operational review, results, Awards, and recovery.

## Primary actors and beneficiaries

| Participant | Fundamental purpose |
| --- | --- |
| Judge | Evaluate student work accurately and independently without being burdened by competition administration. |
| Organizer | Coordinate a fair competition and produce trustworthy results without manual orchestration and tabulation. |
| Administrator | Operate the technical system/environment without automatically inheriting competition decision authority. |
| Student Team | Receive a fair evaluation based on the quality of its work rather than institutional identity or administrative accident. |

Students are currently beneficiaries and competition participants, not application actors. Student accounts, submission portals, and student dashboards are outside the initial product boundary.

## Initial product boundary

The product initially owns the operational judging lifecycle:

```text
Competition configuration
  -> Team establishment
  -> anonymized competition identity
  -> Judge participation
  -> Panel formation
  -> Judging Encounters
  -> individual evaluation
  -> Scorecard capture
  -> aggregation
  -> review/reconciliation
  -> ranking and Awards
  -> competition finalization
```

### Explicitly outside the initial boundary

- student registration UI;
- dataset hosting/distribution;
- notebook or ML execution infrastructure;
- student submission management;
- faculty-advisor management;
- general ticketing/marketing;
- prize payment.

These may integrate later without becoming part of the first conceptual core.

## Canonical terminology

- **Team** means competitors.
- **Panel** means the group of Judges evaluating together.

The term "judging team" should be avoided because it conflicts with Team as the competitor concept.

## Evaluation structure

A Panel evaluates a Team during a **Judging Encounter**. Individual Judges author their own Scorecards within that encounter.

```text
Panel + Team
    -> Judging Encounter
        -> Judge A -> Scorecard A
        -> Judge B -> Scorecard B
        -> Judge C -> Scorecard C
```

A Team may participate in multiple Encounters. Its competition evaluation is derived from the individual Scorecards across those Encounters. The underlying Scorecards remain individually attributable and are not replaced by aggregation.

## Provenance principle

Every aggregate result should be decomposable into the evaluations that produced it:

```text
Team result
  -> Encounter contribution
      -> Judge Scorecard
          -> criterion response
          -> note
          -> rubric basis
```

This enables Organizers to answer why a Team received a particular outcome instead of trusting an opaque total.

## Identity shielding

The system should distinguish a Team's administrative identity from its competition-facing identity.

```text
Team
  administrative identity -> Organizer-visible
  competition identity     -> Judge-visible
```

Institution/school identity is bias-sensitive and should not be disclosed to Judges through the judging experience. Division is legitimate competition context and may remain visible.

## Division

Divisions should be organizer-defined competition configuration rather than hard-coded enums. A competition might use Novice, Undergraduate, Graduate, or another structure.

A Team belongs to one active Division. Division influences competitive comparison, ranking, and potentially award scope.

## Panel composition

Academic, Business, and Technical are initial expertise categories, not permanent hard-coded roles. Panel composition should be policy-driven so future competitions can alter requirements without architecture changes.

## Judge access mechanism

Low-friction day-of-event entry is required, but QR code, magic link, passkey, event code, or similar mechanisms are implementation choices. The enduring requirement is:

> A volunteer arriving at the event must be able to establish a trustworthy Judge identity and competition participation with very little friction.

## Paper parity

Paper is not a second-class workaround. A valid evaluation may originate through electronic or paper capture. Once captured, both paths must share the same scoring semantics and retain appropriate authorship and capture provenance.

## Mobile and resilience posture

Judge interaction is mobile-first. The event environment may include poor connectivity, interrupted sessions, device limitations, and accessibility needs. Technology degradation must not invalidate judging that has already occurred.

## Awards

Competition outcomes are broader than rank. The system must support organizer-defined Awards such as Most Innovative or Best Applied Analysis in addition to rank-derived winners.

## Architectural boundary condition

The intended deployment end state is:

```text
GitHub -> GitHub Actions -> AWS ecosystem
```

This is a constraint, not an architecture decision. Specific AWS services remain deferred.

## Working product principles

- Judging-centered.
- Independent evaluation.
- Traceable aggregation.
- Controlled identity disclosure.
- Configurable competition policy.
- Capture-channel neutrality.
- Mobile-first judging.
- Accessible participation.
- Operational resilience.
- Administrative visibility.
- Auditability without unnecessary surveillance.
- Technology independence during conceptual design.

## Initial conceptual spine

```text
Competition
  -> Division -> Team

Judge participation -> Panel

Panel + Team
  -> Judging Encounter
      -> individual Scorecards
          -> aggregation
              -> ranking / Awards
```

## Exit position

The product's conceptual center is a **trustworthy competition judging system that coordinates anonymous, repeated, multi-perspective evaluation of student Teams and turns individually attributable evaluations into traceable competition outcomes**.

Next: **001-B — Actors, Roles, Authorities & Participation**.
