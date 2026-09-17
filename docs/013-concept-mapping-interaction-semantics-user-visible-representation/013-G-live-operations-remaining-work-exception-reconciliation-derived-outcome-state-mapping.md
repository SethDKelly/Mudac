---
type: Phase Design Record
title: 013-G — Live Operations, Remaining Work, Exception/Reconciliation & Derived Outcome-State Mapping
description: "Maps Organizer live-event coordination, remaining Judge work, governed exceptions, reconciliation, current evidence eligibility, Coverage/Aggregate/Rank and readiness as source-derived operational explanations without creating ticket/workflow authority or prematurely establishing Award/finalization/outcome authority."
status: stable
tags: [phase-013, jackson, mapping, live-operations, remaining-work, exception, reconciliation, coverage, aggregate, rank, readiness]
sources:
  - resource: 013-F-authority-lineage-paper-capture-amendment-correction-historical-state-mapping.md
  - resource: ../canonical/experience/mapping-authority-baseline.md
  - resource: ../canonical/experience/live-operations.md
  - resource: ../canonical/experience/reconciliation-finalization.md
  - resource: ../canonical/experience/judge-evaluation.md
  - resource: ../canonical/experience/authority-lineage-correction.md
  - resource: ../canonical/mechanisms/coverage.md
  - resource: ../canonical/mechanisms/aggregate.md
  - resource: ../canonical/mechanisms/rank.md
  - resource: ../canonical/mechanisms/readiness.md
  - resource: ../canonical/mechanisms/reconciliation.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/synchronizations/temporal-truth-correction.md
  - resource: ../canonical/synchronizations/evaluation-outcome-finalization-declaration.md
  - resource: ../canonical/policies/evaluation-policy.md
  - resource: ../canonical/policies/operational-exception-governance.md
  - resource: ../canonical/invariants/missing-never-zero.md
  - resource: ../canonical/invariants/calculated-not-official.md
---

# Purpose

Map how Organizers understand and coordinate live Competition operation and post-event reconciliation while preserving the distinction between operational status, source authority, derived evidence state, governed exception disposition, and later official-result authority.

013-G focuses on:

- event-day operational context and exception-first coordination;
- actual occurrence/obligation/Scorecard state rather than Panel-plan inference;
- remaining Judge work as a projection of current responsibility;
- Event Completed versus unfinished evaluation work;
- warning, blocker, governed exception, correction and technical intervention distinctions;
- reconciliation as Organizer work over source conditions rather than a lifecycle/ticket Concept;
- current evidence eligibility after amendment/correction/invalidation;
- Coverage as factual sufficiency;
- Aggregate as numerical derivation;
- rank eligibility, Rank and ties;
- Ranking Readiness and Finalization Readiness;
- action/feedback semantics for resolving source conditions without editing derived state.

013-G deliberately stops before Award conferral, Competition Finalization, Outcome Declaration authority and successor official outcome semantics. Those user-visible authority transitions belong to 013-H.

It does not prescribe dashboards, queues, kanban boards, notification systems, polling, persistence, event buses, background jobs, cache behavior, service topology, database schemas, or implementation architecture.

# Decision

**COMPLETE — PASS. Proceed to 013-H.**

```text
013-A START GATE                                  COMPLETE — READY
013-B AUTHORITY / CORPUS BASELINE                COMPLETE — PASS
013-C CONTEXT / JUDGE ENTRY MAPPING              COMPLETE — PASS
013-D ORGANIZER PREPARATION MAPPING              COMPLETE — PASS
013-E ACTIVE EVALUATION MAPPING                  COMPLETE — PASS
013-F AUTHORITY / CORRECTION MAPPING             COMPLETE — PASS
013-G LIVE OPS / RECONCILIATION MAPPING          COMPLETE — PASS
LIVE-OPERATIONS OWNER REWRITTEN                  YES
RECONCILIATION-DERIVED-STATE OWNER CREATED       YES
RECONCILIATION AS LIFECYCLE/TICKET CONCEPT       PROHIBITED
REMAINING WORK AS MANUAL CHECKLIST               PROHIBITED
EVENT COMPLETED == ALL JUDGE WORK DONE            PROHIBITED
HISTORICALLY SATISFIED == CURRENTLY ELIGIBLE      PROHIBITED
COVERAGE EXCEPTION == COVERAGE SATISFIED          PROHIBITED
AGGREGATE EXISTS == COVERAGE/RANK READY            PROHIBITED
RANK EDITABLE                                    PROHIBITED
CALCULATED RANK == OFFICIAL OUTCOME               PROHIBITED
READINESS AS EDITABLE STATE                      PROHIBITED
EXCEPTION AS GENERIC OVERRIDE                    PROHIBITED
NEW WORK AUTO-CREATED BY EVIDENCE INVALIDATION    PROHIBITED
PHASE-010 REOPEN REQUIRED                        NO
PHASE-011 REOPEN REQUIRED                        NO
PHASE-012 REOPEN REQUIRED                        NO
NEXT                                               013-H
ARCHITECTURE / IMPLEMENTATION                     SUSPENDED
```

# 1. Governing operational model

Organizer live/reconciliation experience composes current source facts and derived explanations without becoming their owner.

```text
Competition / Participation / Panel plan
  + Evaluation Occurrence state
  + Evaluation Obligation state
  + Scorecard authority/currentness
  + correction/invalidation state
  + Evaluation Policy
    ↓
operational projections
  - current work
  - remaining responsibility
  - warnings / blockers
  - governed exception opportunities/dispositions
  - evidence eligibility
  - Coverage
  - Aggregate
  - rank eligibility / Rank
  - Ranking Readiness
  - Finalization Readiness
```

The arrows are interpretation/composition, not a hidden workflow or state machine.

The experience may group and prioritize operational conditions, but the grouping does not create authority.

# 2. Live Operations is an Organizer work context

`Live Operations` is a user-facing work context for coordinating an Active or recently completed Competition. It is not a Concept and has no lifecycle of its own.

The Organizer should be able to understand material current conditions such as:

- Competition lifecycle state;
- Judge Participation/readiness where operationally relevant;
- current Panel planning/composition;
- Prepared/Open/Complete/Cancelled/Invalidated Evaluation Occurrences;
- actual occurrence participants;
- Outstanding/Satisfied/Excused/Cancelled Evaluation Obligations;
- absent/Draft/finalized Scorecard work;
- paper/assisted capture state where applicable;
- uncertain authority/capture conditions;
- correction/invalidation/replacement pressure;
- warnings, blockers and governed exception conditions.

The representation should prioritize conditions requiring legitimate attention rather than foregrounding leaderboard-style outcome information during judging.

# 3. Planned grouping remains distinct from live truth

Preserve throughout live coordination:

```text
Panel membership
  != actual Evaluation Occurrence participation
  != Evaluation Obligation responsibility
  != Scorecard evidence
```

A permanent Panel membership change is not the same thing as an occurrence-specific participant substitution.

Changing current Panel membership never rewrites who participated in an already-begun or completed occurrence.

If a substitution creates or ends evaluator responsibility, that consequence must occur through the current occurrence/obligation composition rather than visual reassignment alone.

# 4. Remaining Judge work

`Remaining Work` is a derived Organizer/Judge explanation over current responsibility, not a manually maintained task list.

Ordinary remaining evaluation work consists of current **Outstanding Evaluation Obligations**, interpreted with their associated occurrence/basis/current Access context.

Examples:

```text
Outstanding obligation + no Scorecard
  → not-started remaining work

Outstanding obligation + Scorecard Draft
  → in-progress/deferred remaining work

Satisfied obligation
  → not remaining work merely because its Scorecard later becomes ineligible
```

The last distinction is critical.

If historically Satisfied evidence becomes ineligible, that creates an evidence/reconciliation condition. It becomes new Judge work only if an explicit successor Evaluation Obligation is legitimately established under 013-F semantics.

Therefore:

```text
ineligible evidence
  != reopened obligation
  != automatic successor obligation
```

# 5. Event Completed and unfinished work

`Competition.completeEvent` records that ordinary live-event activity has ended and moves Competition from Active to Event Completed.

It must not be represented as proving:

```text
all occurrences complete
all obligations terminal
all Scorecards finalized
Coverage satisfied
reconciliation complete
Finalization Ready
```

A completed Evaluation Occurrence can already coexist with an Outstanding obligation under 013-E. Likewise, Competition Event Completed may coexist with legitimate remaining Judge work if current policy and Access still permit that work.

Whether Judge capability continues, narrows or ends after Event Completed is an explicit current Access/policy question. Event completion alone must not be mapped as a universal hidden Access revocation rule.

# 6. Operational condition taxonomy

The experience must distinguish at least:

```text
warning
  = informative condition; does not itself block authority

blocking precondition
  = required condition is false; target action cannot proceed

governed exception
  = policy permits a scoped consequence despite preserved source shortfall

correction
  = source truth/authority requires legitimate edit, successor, invalidation or replacement

technical intervention
  = restore/restrict operation without substituting semantic authority
```

Generic `Resolve`, `Override`, `Force`, `Dismiss` or `Acknowledge` language must not imply these are interchangeable.

# 7. Governed exceptions preserve source truth

A governed exception changes only the explicitly permitted consequence.

It does not rewrite the fact that made the exception necessary.

Examples:

```text
Panel composition = Degraded
+ permitted composition exception
→ proceeding may be allowed
→ Panel does NOT become Compliant

Coverage = Incomplete
+ accepted ranking exception
→ ranking may be permitted if policy allows
→ Coverage remains Incomplete
```

A material exception representation must make the affected scope/condition, permitted consequence, authority/authorizer and reason reconstructible where relevant.

An accepted exception does not silently waive unrelated policy or invariants.

# 8. Acknowledgement is not resolution

Operational presentations may support acknowledgement, suppression or attention management, but those are presentation actions only.

```text
acknowledged
hidden
suppressed
viewed
```

must not mean the source problem is repaired.

A condition becomes semantically resolved only when:

1. its authoritative source changes;
2. a specifically permitted governed exception changes the allowed consequence; or
3. another owner-defined action establishes the required postcondition.

This prevents reconciliation from becoming a ticket-close system detached from domain truth.

# 9. Reconciliation is source-directed work

Reconciliation is an Organizer work context/process for resolving outcome-affecting conditions. It is not:

- a Competition lifecycle state;
- an independent Concept;
- a generic issue/ticket lifecycle;
- a source of evidence;
- a Rank editor;
- official outcome authority.

Reconciliation may begin surfacing conditions while the event is still Active and becomes especially important after Event Completed. It need not wait for a single navigation transition to exist conceptually.

Typical source categories include:

- Outstanding evaluation responsibility;
- paper/assisted capture not yet authoritatively established;
- uncertain Finalization/capture state;
- evidence invalidation/correction;
- occurrence invalidation/replacement;
- successor responsibility deliberately required;
- Team/Division eligibility issues;
- Rubric/Evaluation Basis compatibility;
- Coverage shortfall;
- governed Coverage/composition exception disposition;
- tie/policy conditions;
- Award/finalization prerequisites whose authority is handled later.

A reconciliation projection should route the Organizer toward the natural source/action rather than offering a generic `Mark resolved` mutation.

# 10. Current eligible evidence projection

Outcome-oriented operational views must distinguish historical authority from **current evidence eligibility**.

A finalized Scorecard contributes as current eligible evidence only when the current composition establishes the relevant Version, structural binding, historical obligation satisfaction, occurrence eligibility, basis eligibility and correction/invalidation conditions.

Therefore:

```text
Scorecard was Finalized
  != Scorecard is currently eligible

Evaluation Obligation is historically Satisfied
  != its evidence is currently eligible
```

An ineligible historical Scorecard remains authentic history unless separately corrected/invalidated as owned; it simply does not contribute to current outcome derivation when eligibility is false.

# 11. Coverage mapping

Coverage is derived factual sufficiency over qualifying current evidence and the applicable requirement basis.

User-visible factual result remains:

```text
Satisfied | Incomplete
```

Coverage should be explainable enough to identify the applicable requirement basis and observed qualifying evidence/shortfall without implying editable authority.

Missing evidence remains missing and is never represented as zero or fabricated presence.

## Coverage and exception disposition

The experience must be able to show simultaneously:

```text
Coverage = Incomplete
Exception = Accepted for a defined consequence
```

An exception does not change the Coverage label to `Satisfied`.

If a policy permits ranking/finalization despite incomplete Coverage, that permission should be shown as a separate governed disposition.

# 12. Aggregate mapping

Aggregate is a numerical derivation over current eligible authoritative individual Judge Scorecards under Evaluation Policy.

The representation must preserve:

```text
Aggregate exists
  != Coverage Satisfied
  != rank eligible
  != Ranking Ready
  != official outcome
```

A numeric Aggregate can therefore legitimately appear while Coverage remains Incomplete.

Panel/occurrence means may be analytical views but must not be represented as the official weighting unit when baseline policy weights each eligible individual Scorecard equally.

Missing evaluation remains absent from the Aggregate basis rather than zero-valued.

# 13. Rank eligibility and Rank mapping

Rank is derived only after the application supplies the rank-eligible Team set under current policy.

Rank must remain non-editable.

If a position is wrong, the experience should direct correction to the actual source category: evidence eligibility, Coverage/exception disposition, Division, Aggregate input, Evaluation Policy, tie handling, or other governing basis.

The experience must preserve:

```text
calculated Rank
  != Ranking Readiness
  != Award authority
  != official outcome authority
```

Display rounding, hidden ordering or implementation insertion order must not visually imply a resolved tie when policy says the result is tied/unresolved.

# 14. Derived currentness

Coverage, Aggregate, Rank and readiness are basis-relative derived state.

When a material input changes:

```text
source authority changes
  → affected/non-current derived result identified
  → recomputation against current basis
  → new current derived result
```

Recomputation never mutates the source Concepts that produced it.

Prior derivations may remain reconstructible where needed to explain historical decisions.

The experience should not present stale derived results as current merely because they have not yet been recomputed/acknowledged.

# 15. Ranking Readiness

Ranking Readiness answers whether a supplied result scope is currently fit for rank-dependent consequential use.

It is distinct from Rank existence.

Relevant blockers may include, as applicable:

- unresolved Team/Division eligibility;
- non-reconstructible evidence basis;
- Coverage `Incomplete` without an applicable accepted exception for ranking;
- incompatible/ineligible Evaluation Basis state;
- unresolved material correction/invalidation/replacement/successor-work conditions;
- unavailable Aggregate/policy basis;
- unresolved tie semantics.

Ranking Readiness is derived and has no generic write action.

A current calculated ordering may therefore be visible while Ranking Readiness is false, provided the representation does not imply consequential readiness or officiality.

# 16. Finalization Readiness boundary

013-G maps **Finalization Readiness** only as a derived explanation of whether current closeout inputs appear sufficiently resolved for the later high-consequence closeout action.

It may depend on:

- current eligible evidence;
- Coverage plus separate exception dispositions;
- Ranking Readiness;
- Evaluation Policy;
- required Award decisions;
- unresolved correction/reconciliation conditions;
- reconstructible intended OutcomeBasis/Closeout Basis.

Preserve:

```text
Finalization Readiness = true
  != Competition Finalized
  != Outcome Declaration exists
```

013-H owns how Award authority, Competition Finalization, explicit Outcome Declaration and successor official outcome are represented.

# 17. Operational action availability and feedback

Operational actions should expose the natural semantic action and consequence rather than a generic issue-state mutation.

Examples:

| Condition | Legitimate mapped direction |
| --- | --- |
| Judge has Outstanding obligation | start/resume same logical evaluation when permitted |
| occurrence participant unavailable | occurrence-specific adjustment plus separate responsibility consequence where required |
| Panel composition shortfall | repair grouping or use specifically permitted composition exception |
| paper capture incomplete | continue/verify same logical capture path |
| authoritative capture mismatch | 013-F capture-correction path |
| Scorecard/occurrence ineligible | owner-specific correction/invalidation/replacement path |
| Coverage Incomplete | obtain legitimate evidence if responsibility exists, correct eligibility/source, or use specifically permitted consequence exception |
| tie unresolved | apply declared policy/authorized tie resolution semantics, never hidden manual ordering |
| derived result stale | recompute from current authoritative basis |

The application should explain why a condition matters and which authority can legitimately change it without leaking protected information.

# 18. Organizer authority boundary

Live urgency and reconciliation pressure do not transfer Judge semantic authorship.

Organizer/support may coordinate, prompt, establish permitted grouping/responsibility consequences, invoke governed exception/correction actions, capture verified Judge paper content, or manage Competition lifecycle actions within authority.

They cannot:

- invent Judge responses;
- finalize a Judge's semantic judgment merely because work is late;
- turn missing evidence into zero;
- mark Coverage Satisfied;
- manually edit Rank;
- manufacture successor Judge work solely to clear a reconciliation item;
- use technical privilege as exception authority.

# 19. Derived-state explanation matrix

| User-visible condition | Source/derived meaning | Writable directly? |
| --- | --- | --- |
| Remaining work | projection over Outstanding obligations/current context | no |
| Warning | informative source/policy condition | no generic resolution |
| Blocker | false semantic precondition | no generic resolution |
| Governed exception | scoped permission despite preserved condition | only purpose-specific exception action |
| Coverage | factual evidence sufficiency | no |
| Aggregate | numerical current eligible-evidence derivation | no |
| Rank | derived ordering over supplied eligible set | no |
| Ranking Readiness | permission-to-use projection | no |
| Finalization Readiness | closeout permission-to-proceed projection | no |
| Reconciliation item | explanation of unresolved source condition | no ticket-style source truth |

# 20. Mapping-risk disposition

013-G closes/reduces:

- **MAP-R05** — Panel/participant/responsibility/evidence collapse: preserved under live operation;
- **MAP-R06** — Draft/finalized/eligible authority collapse: historical authority and current eligibility remain distinct;
- **MAP-R07** — missing/zero/incomplete/exception collapse: explicitly separated;
- **MAP-R08** — Rank/Award/official declaration collapse: Rank stops before H authority;
- **MAP-R10** — correction flattened to edit/delete: live reconciliation routes through 013-F owner-specific semantics;
- **MAP-R14** — Readiness/Reconciliation/exception projections appear editable: closed for live/reconciliation/derived state;
- **MAP-R15** — technical/support privilege appears semantic authority: preserved as prohibited.

No discovered 013-G mapping defect requires Phase 010, 011 or 012 reopening.

# 21. Canonical ownership result

013-G establishes two current Experience owners:

- `live-operations.md` — live-event operational coordination and remaining-work mapping;
- `reconciliation-derived-state.md` — reconciliation, current evidence eligibility, Coverage/Aggregate/Rank and readiness mapping.

The pre-convergence `reconciliation-finalization.md` mixed owner is split:

- its reconciliation/derived-state content migrates to `reconciliation-derived-state.md` in 013-G;
- its Award/finalization/officiality content remains admitted evidence only until 013-H;
- obsolete `Official Outcome Revision` language is not carried forward.

# 22. Handoff to 013-H

013-H inherits:

```text
current eligible evidence != merely historically Finalized evidence
Coverage fact != exception disposition
Aggregate != Coverage != Rank
calculated Rank != consequential readiness != official authority
Ranking Readiness = derived
Finalization Readiness = derived
Reconciliation = source-directed work, not lifecycle/ticket authority
invalid evidence != automatic successor Judge work
```

013-H should map Award conferral/correction authority, Competition Finalization, explicit Outcome Declaration, official current/Affected/Superseded state and successor official authority without allowing any derived mechanism to impersonate those Concepts.

# Exit decision

**013-G COMPLETE — PASS. Proceed to 013-H — Award, Competition Finalization, Outcome Declaration, Officiality & Successor-Authority Mapping.**
