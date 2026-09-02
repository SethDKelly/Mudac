# 002-G — Awards, Reconciliation, Finalization & Official Outcomes

Status: **Complete**

## 1. Purpose

002-G specifies how a Competition moves from completed live judging and provisional derived results to an explicit official outcome.

The accepted Concept specified here is:

1. Award

Cross-cutting behavior specified here includes:

- Organizer reconciliation;
- ranking-readiness gates;
- rank-derived and discretionary Award semantics;
- Award definition authority and conferral;
- Award correction/revocation;
- Competition Finalization gates;
- official-outcome snapshot/revision semantics;
- post-finalization correction and re-confirmation;
- publication/disclosure boundaries for official results.

Reconciliation, Rank, and Official Outcome remain derived/process mechanisms rather than new standalone Concepts.

The central flow is:

```text
Event Completed
      ↓
Organizer Reconciliation
      ↓
Ranking Ready
      ↓
Award Decisions
      ↓
Finalization Readiness
      ↓
Competition.finalize
      ↓
Official Outcome Revision
```

Finalization does not merely mean that the event ended. It means the Organizer has explicitly confirmed that the authoritative evidence, evaluation policy, exceptions, rankings, and Awards are sufficiently reconciled to become official.

The specification remains implementation-neutral. Workflow engines, database transaction strategy, result-publication channels, PDF generation, public websites, API representations, and AWS services remain downstream concerns.

---

# 2. Event Completed versus Finalized

002-A established:

```text
Draft → Ready → Active → Event Completed → Finalized
```

002-G gives the final two states precise meaning.

## Event Completed

Event Completed means:

> Live judging activity has ended and ordinary Judge evaluation access has expired, but Competition evidence and outcomes may still require reconciliation.

Between Event Completed and Finalized, Organizers may legitimately:

- finish paper transcription;
- verify capture accuracy;
- resolve incomplete/invalid Encounters;
- coordinate post-event Judge amendments;
- accept or reject Coverage/composition exceptions;
- resolve Rubric-compatibility issues;
- correct Division assignment;
- resolve ranking ties according to policy;
- determine discretionary Awards;
- confirm rank-derived Award recipients.

Thus Event Completed is operational close, not official-result close.

## Finalized

Finalized means:

> The Competition has an explicitly confirmed official outcome based on identified authoritative evidence and policy, and ordinary outcome-changing workflows are closed.

Finalized does not mean legitimate correction is physically impossible. Post-finalization changes require the exceptional governance defined later in this document and 002-E.

---

# 3. Reconciliation

Reconciliation remains an Organizer activity/process rather than a Competition lifecycle state or Concept.

## Purpose

> Resolve outstanding evidence, eligibility, policy, and outcome questions so that provisional derived results can be safely treated as official.

Reconciliation consumes facts from the previously specified Concepts and derived mechanisms rather than owning those facts itself.

Conceptually:

```text
Scorecards / Versions / Provenance
Encounters / participant adjustments
Coverage / exceptions
Evaluation Policy
Division assignments
Rubric compatibility
Rank / ties
Award definitions
        ↓
Organizer Reconciliation
        ↓
readiness or unresolved issues
```

## Reconciliation is exception-oriented

The Organizer should not be required to manually approve every normal Scorecard one by one.

The system should automatically derive what is structurally healthy and surface items requiring attention, such as:

```text
paper Scorecards not yet captured
incomplete Encounter obligations
invalidated Encounter without replacement
Coverage Incomplete
pending Coverage exception
Rubric incompatibility
active Amendment Draft / pending requested correction
Division correction affecting ranking
unresolved tie requiring policy action
unconfirmed rank-derived Award
unconferred required Award
post-event correction affecting derived results
```

The goal is evidence-based closeout rather than bureaucratic repetition.

---

# 4. Reconciliation issue states

A reconciliation issue should be able to resolve into an explicit disposition such as:

```text
Resolved normally
Exception accepted
Evidence corrected
Evidence invalidated
Replacement established
Not applicable
Blocks finalization
```

The exact UI/state representation remains downstream, but the disposition must be explainable.

An unresolved material issue cannot be hidden merely because a numerical Rank is currently computable.

---

# 5. Ranking readiness

002-F defined Team rank eligibility and Division Ranking.

002-G distinguishes a calculated provisional ranking from a Division being **ranking ready**.

A Division is normally ranking ready when:

1. every Team expected to participate in official ranking has a resolved participation/withdrawal status;
2. every rank-eligible Team has Coverage `Satisfied` or `Exception Accepted`;
3. no unresolved invalid/replacement Encounter materially affects the Division;
4. all expected paper evaluations affecting the Division are captured or explicitly resolved;
5. no pending Scorecard correction is expected to materially alter the outcome;
6. Rubric-version compatibility is resolved;
7. Evaluation Policy for the ranking basis is authoritative and unambiguous;
8. every Team has a valid current Division assignment;
9. all required tie behavior has been applied or the declared tie remains valid as shared Rank;
10. no unresolved outcome-affecting correction remains.

A Division can have a visible provisional ranking before these gates are satisfied.

It cannot be treated as official simply because a sort order exists.

---

# 6. Competition-level reconciliation readiness

Competition Finalization requires more than each Division being numerically rankable.

At minimum, the Competition must have:

- Event Completed;
- all relevant Divisions ranking ready;
- all material evidence/reconciliation issues resolved;
- one authoritative Evaluation Policy basis for each affected result scope;
- no unresolved scoring-semantic Rubric incompatibility;
- all required Award decisions resolved;
- no outstanding post-event correction workflow intended to alter official outcomes;
- an Organizer with finalization authority explicitly confirming closeout.

002-H may add an operational requirement that all required official exports/publications can be regenerated from authoritative source state, but export generation itself should not normally be required simply to make the Competition logically Finalized.

---

# 7. Award specification

## Purpose

> Define and confer named Competition recognition upon eligible Teams without collapsing recognition into numerical Rank.

Award survives as a standalone Concept because it has an independent purpose and works even when no numerical Rank selects the recipient.

Examples include:

```text
Undergraduate Champion
Graduate Champion
Most Innovative
Best Applied Analysis
Best Presentation
```

## Award state

Conceptually:

```text
Award
    stable Award identity
    Competition scope
    name
    description
    scope
    selection method
    eligibility rules
    recipient cardinality
    lifecycle / availability state
    conferrals
```

`scope` may be:

```text
Competition-wide
Division-scoped
```

The current product does not introduce a Round/Stage scope unless that future extension is accepted.

## Selection method

At minimum:

```text
Rank-derived
Discretionary
```

The selection method must be visible/inspectable enough that the system does not misrepresent discretionary judgment as a mathematical result.

---

# 8. Award definition lifecycle and authority

Award definitions should normally be established before the Competition becomes Ready.

During Draft, Organizers may freely create/edit/delete unused Award definitions.

Once a Competition is Ready, Award definitions should be treated as authoritative Competition rules for that occurrence.

A change during Active or later Competition states that modifies:

- Award name in a meaningfully different way;
- scope;
- selection method;
- eligibility;
- recipient cardinality;
- rank linkage;

can change official recognition and therefore requires Organizer authority, reason, Versioning/Provenance where appropriate, and downstream review.

A superficial typographical correction may be classified as editorial, but it still must not make prior official output unreconstructible once an Award has been conferred or published.

---

# 9. Rank-derived Awards

A rank-derived Award links declared ranking semantics to recognition.

Example:

```text
Award:
    Undergraduate Champion

Scope:
    Undergraduate Division

Selection method:
    Rank-derived

Selection rule:
    Rank 1
```

The system can derive the candidate recipient from the ranking.

The initial MUDAC default is:

> **The system derives the candidate; an authorized Organizer confirms the Award conferral.**

This provides a deliberate final check around official recognition without allowing the Organizer to arbitrarily choose a different Team while pretending the Award was rank-derived.

If the Ranking has a valid shared Rank 1 and the Award definition permits multiple recipients, each tied eligible Team may be conferred.

If the Award definition permits only one recipient while the Ranking has an unresolved shared Rank 1, Award conferral is blocked until the Competition's declared tie/adjudication policy resolves the mismatch.

---

# 10. Rank-derived candidate consistency

For a rank-derived Award, the confirmed recipient must be consistent with:

- the declared Award scope;
- the authoritative Ranking basis;
- the Award selection rule;
- Team eligibility;
- tie policy;
- recipient cardinality.

An Organizer cannot confirm:

```text
Rank 2 Team → Rank 1 Champion Award
```

without changing/correcting the underlying authoritative facts or explicitly changing the Award definition under controlled governance.

This prevents a rank-derived Award from becoming a disguised discretionary Award.

---

# 11. Discretionary Awards

A discretionary Award may be conferred based on Organizer/judging deliberation rather than numerical Rank.

Examples:

```text
Most Innovative
Best Applied Analysis
Best Presentation
```

Organizers may consider authorized evidence such as:

- Scorecards;
- Criterion responses;
- Judge Notes;
- presentation observations;
- deliberation among Competition officials;

subject to Competition rules.

The system does not automatically convert Notes or text analysis into a hidden scoring formula.

The official record should identify the selection method as discretionary.

A human-readable rationale may be optional during ordinary pre-finalization conferral unless Competition policy requires it, but is recommended for high-consequence or unusual decisions.

---

# 12. Award conferral

Award conferral is the authoritative act of associating recognition with a Team.

Conceptually a conferral records:

```text
Award
Team
scope / Division if applicable
selection method
acting Organizer / authority
time
supporting Rank/result reference if rank-derived
optional rationale
status
```

Conferral does not rewrite Team state or Rank.

Award and recipient remain independently identifiable.

---

# 13. Recipient cardinality

Award definitions should explicitly support recipient cardinality semantics such as:

```text
Exactly one
One or more
Zero or one / optional
```

The initial baseline does not require arbitrarily complex nomination or multi-tier Award structures.

This matters for ties and optional alternative Awards.

For example:

```text
Undergraduate Champion
Exactly one
```

may require tie resolution.

Whereas:

```text
Judges' Innovation Recognition
One or more
```

may legitimately support co-recipients.

---

# 14. Required versus optional Awards

A Competition should be able to distinguish Awards required for closeout from optional recognitions.

For example:

```text
Division Champion
    required

Most Innovative
    optional
```

A required Award must have its conferral resolved before Finalization.

An optional Award may remain unconferred without blocking Finalization, provided its state is unambiguous rather than accidentally forgotten.

The exact configuration representation remains policy/state rather than another Concept.

---

# 15. Award correction and revocation before Finalization

Before Competition Finalization, an authorized Organizer may correct an Award conferral when an error is discovered.

The previous conferral must remain historically attributable once it had authoritative significance.

Examples:

```text
wrong Team selected accidentally
rank changed after valid Scorecard amendment
Award eligibility was misapplied
```

The correction should preserve:

- prior recipient;
- new recipient or revoked state;
- actor;
- time;
- reason where consequential;
- underlying result/evidence impact.

A rank-derived Award should normally refresh its candidate after a material Ranking change and require Organizer reconfirmation rather than silently moving the Award.

---

# 16. Award revocation

Revocation means:

> A previously conferred Award is no longer officially held by that Team.

It does not mean deletion of the historical fact that the Award had once been conferred.

Revocation may be followed by corrected conferral to another Team.

The record should preserve both states.

Post-finalization revocation is an exceptional official-outcome correction and follows the stronger governance specified below.

---

# 17. Finalization readiness

Competition Finalization is an explicit high-consequence action.

The system must derive a finalization-readiness assessment rather than exposing a blind `Finalize` operation.

The initial mandatory gates are:

1. Competition state is Event Completed.
2. Structural Team/Division/Alias integrity remains valid for official outcome interpretation.
3. All relevant Judging Encounters are resolved as valid, cancelled, invalidated, or replaced.
4. No unresolved effective Scorecard obligation that policy says must be resolved remains.
5. Expected paper-origin evidence is captured, intentionally excluded, or otherwise reconciled.
6. Current authoritative Scorecard Versions are identified and no material intended amendment remains pending.
7. Rubric-version aggregation compatibility is resolved.
8. Coverage is resolved for every Team expected to rank (`Satisfied`, `Exception Accepted`, withdrawn/excluded, or otherwise explicitly resolved).
9. Every relevant Division is ranking ready.
10. Required tie/adjudication actions are resolved.
11. Evaluation Policy is authoritative and all outcome-affecting policy changes are reconciled.
12. Required Awards are conferred/resolved.
13. Rank-derived Award conferrals are consistent with current Ranking.
14. No unresolved outcome-affecting correction/reconciliation issue remains.
15. An authorized Organizer explicitly confirms Finalization.

The system may surface warnings for non-blocking issues, but a blocking gate cannot be bypassed merely by ignoring the warning unless an explicit governed exception mechanism exists for that gate.

---

# 18. Organizer finalization confirmation

Finalization should require a high-consequence confirmation explaining what is becoming official.

Conceptually the Organizer confirms:

> The Competition's current authoritative evidence, policy, resolved exceptions, Division Rankings, and Award conferrals are accepted as the official outcome.

The action must record Provenance including:

- acting Organizer Participation;
- timestamp;
- Competition;
- finalization basis / official-outcome revision;
- any exceptional rationale required by policy.

This is more meaningful than merely setting:

```text
competition.finalized = true
```

---

# 19. Official Outcome is a snapshot/projection, not a new Concept

Phase 001 rejected a generic `Result` Concept because it would collapse Aggregate, Rank, Award, and finalization semantics.

002-G preserves that decision.

Instead, Finalization establishes an **Official Outcome Revision**: an authoritative reconstructible snapshot/projection of the Competition outcome at a point in time.

Conceptually it identifies/references:

```text
Official Outcome Revision
    Competition
    finalization time
    finalizing authority
    authoritative Evaluation Policy basis
    relevant Rubric compatibility basis
    resolved Coverage / accepted exceptions
    Division Ranking outcomes
    Award definitions/conferrals
    source evidence/version lineage references sufficient for reconstruction
```

The exact persistence strategy may store explicit snapshots, version references, hashes, or another reconstructible representation. Architecture remains deferred.

The important invariant is:

> The system must be able to reconstruct what was officially declared and the authoritative basis that produced it.

---

# 20. Why the official outcome needs revision identity

Suppose the Competition is finalized:

```text
Official Outcome v1
Undergraduate Champion = Team 014
```

Later a verified transcription error is discovered and corrected under post-finalization governance.

The corrected evidence changes Rank:

```text
Team 027 becomes Rank 1
```

The system must not erase the fact that v1 had declared Team 014 the Champion.

Instead:

```text
Official Outcome v1
    historical official declaration

post-finalization correction
        ↓
Organizer reconciliation / Award correction
        ↓
Official Outcome v2
    current corrected official declaration
```

This is controlled finality applied at Competition-outcome scope.

---

# 21. Competition lifecycle after post-finalization correction

A post-finalization correction does not need to force the Competition back through `Active` or `Event Completed`.

The Competition remains a finalized historical occurrence, but its current official outcome may temporarily be marked as affected / under correction until a successor Official Outcome Revision is confirmed.

Conceptually:

```text
Competition: Finalized
Official Outcome v1: current
        ↓
exceptional source correction
        ↓
v1: affected / historical basis retained
outcome correction pending
        ↓
reconciliation
        ↓
Official Outcome v2: current
```

The exact overlay/status vocabulary may be refined later. The key principle is that Competition lifecycle and Official Outcome revision lifecycle do not need to be the same state machine.

---

# 22. Post-finalization source correction

002-E established that post-finalization correction requires exceptional governance.

002-G adds the result-side behavior.

When a source correction can affect an official outcome:

1. preserve the prior Official Outcome Revision;
2. mark affected derived results/Awards as requiring review rather than silently changing official declarations;
3. recompute provisional corrected Coverage/Aggregate/Rank from the new authoritative source state;
4. identify every affected Division, Team, Rank, and rank-derived Award;
5. require Organizer reconciliation;
6. correct/revoke/reconfer Awards where necessary;
7. explicitly confirm a successor Official Outcome Revision.

Until the successor is confirmed, the system must distinguish:

```text
latest derived corrected calculation
```

from:

```text
current/previously declared official outcome
```

rather than ambiguously calling both `official`.

---

# 23. Post-finalization Award correction

If an Award must change after Finalization:

```text
Award Conferral A
    ↓
revoked/corrected with reason
    ↓
Award Conferral B
```

The original conferral remains historical.

A post-finalization Award correction requires:

- authorized Organizer action;
- human-readable reason;
- Provenance;
- consistency with corrected Rank if rank-derived;
- inclusion in the successor Official Outcome Revision.

The application must not silently transfer the Award recipient merely because a derived Rank changed.

---

# 24. Finalization does not publish automatically

Another important boundary:

> **Official does not automatically mean publicly disclosed.**

Competition Finalization establishes authoritative internal results.

Publication/announcement is a separate representation/disclosure action.

This matters because Organizers may want to:

```text
finalize results
        ↓
prepare ceremony/materials
        ↓
announce winners later
```

without exposing outcomes prematurely.

002-H will specify Export/external representation behavior. Access/disclosure continues to govern who may see official results before public release.

No public `Result` portal is assumed by this phase.

---

# 25. Judge visibility after Finalization

Nothing in Finalization restores Judge access to private Scorecards or Competition-wide standings.

Under the baseline:

```text
Event Completed
    ↓
ordinary Judge private evaluation access expires
```

and remains expired after Finalization.

If official Award/winner information is later publicly announced, a Judge may encounter that information through a public/result-publication channel, but not because their Judge Participation regains scoring access.

This preserves the privacy boundary established in 002-B.

---

# 26. Organizer historical view

Authorized Organizers should be able to inspect both current official outcomes and the source evidence/history behind them.

For a current Award, the trace may be:

```text
Award
    ↓
Conferral
    ↓
Official Outcome v2
    ↓
Division Rank
    ↓
Team Aggregate
    ↓
eligible Scorecards
    ↓
Scorecard Versions / Criteria
```

For a corrected result, Organizers should also be able to inspect:

```text
Official Outcome v1
        ↓
post-finalization correction
        ↓
Official Outcome v2
```

This maintains the explainability requirement through official closeout.

---

# 27. No manual official Rank override

Reconciliation and Finalization do not introduce a hidden ability to override Rank numerically.

If the Organizer believes Rank is wrong, the resolution must occur through:

- source evidence correction;
- eligibility/invalidation;
- Coverage exception;
- Division correction;
- authoritative Evaluation Policy/tie policy;
- explicit adjudication mechanism already declared by policy.

Then Rank is derived again.

The Organizer cannot simply persist:

```text
Team 014 = official Rank 1
```

contrary to the authoritative derivation.

---

# 28. No silent Award inference from discretionary evidence

Similarly, the system should not automatically mine Judge Notes or statistical patterns to choose discretionary Award recipients unless a future explicit Award-selection policy introduces such behavior.

The baseline keeps:

```text
Rank-derived Award
    → transparent derived candidate

Discretionary Award
    → explicit authorized human conferral
```

This prevents algorithmic behavior from being mistaken for human Competition judgment.

---

# 29. Finalization failure behavior

A Finalization attempt fails safely when any mandatory gate is unresolved.

The system should explain the blocking conditions, for example:

```text
Cannot finalize Competition:
- Graduate Division Coverage unresolved for Team G-014
- 2 paper Scorecards awaiting capture
- Undergraduate rank-derived Champion Award not confirmed
- one scoring-semantic Rubric compatibility issue unresolved
```

No partial official state should result from a failed Finalization attempt.

The exact transaction/atomicity implementation is architectural, but the domain effect must be all-or-nothing from the user's perspective.

---

# 30. Reopening an Event versus correcting a Finalized Competition

These remain different operations.

## Resume Event

Used when:

```text
Event Completed was premature
live judging actually needs to continue
```

This returns Competition operationally to Active under 002-A and may restore appropriate live Participation/Access behavior.

## Post-finalization correction

Used when:

```text
historical event is over
official outcome was already declared
new verified correction is necessary
```

This does **not** reopen the live event or broadly restore Judge participation.

The correction stays narrow and produces a successor Official Outcome Revision if needed.

---

# 31. Finalization and retention

Finalization increases the importance of retention and reconstructibility but does not itself define how long Competition data is kept.

Retention periods for:

- Scorecards;
- Notes;
- paper source evidence;
- identity mappings;
- official outcomes;
- Provenance;

remain a later governance/security policy question.

However, while an Official Outcome Revision is retained, the authoritative basis needed to explain it must not be prematurely discarded.

---

# 32. Synchronization contracts

## Event Completed → reconciliation

```text
Competition.completeEvent
        ↓
ordinary Judge Access expires
        ↓
Organizer reconciliation begins/continues
```

No new Reconciliation Concept is created.

## Evidence correction → ranking readiness refresh

```text
Scorecard / Encounter / Division / Policy changes
        ↓
Eligibility / Coverage / Aggregate / Rank refresh
        ↓
reconciliation issues refresh
        ↓
ranking readiness may change
```

## Ranking → rank-derived Award candidate

```text
ranking-ready Division
        ↓
Award selection rule
        ↓
candidate recipient(s)
        ↓
Organizer confirmation
        ↓
Award conferral
```

## Discretionary Award

```text
Organizer review / deliberation
        ↓
Award.confer(Team)
        ↓
Provenance
```

## Finalization

```text
all mandatory finalization gates satisfied
        ↓
Organizer confirms Competition.finalize
        ↓
Official Outcome Revision committed
        ↓
Provenance records finalization authority
```

## Post-finalization correction

```text
exceptional authoritative source correction
        ↓
current official outcome marked affected for review
        ↓
corrected derived results
        ↓
Award correction if required
        ↓
Organizer confirms successor Official Outcome Revision
```

---

# 33. 002-G invariants

002-G adds or confirms these invariants:

1. Event Completed and Finalized remain distinct.
2. Reconciliation is activity/process, not a lifecycle state or Concept.
3. A computable Ranking is not necessarily ranking ready.
4. Unresolved material reconciliation issues block official Finalization.
5. Award remains distinct from Rank.
6. Award definitions declare scope and selection method.
7. Rank-derived and discretionary Awards remain distinguishable.
8. Rank-derived Award candidates come from authoritative Ranking rules.
9. Organizer confirmation does not permit arbitrary deviation from a rank-derived candidate.
10. Award recipient cardinality is explicit.
11. Required Award decisions must be resolved before Finalization.
12. Optional Award non-conferral need not block Finalization when explicitly resolved.
13. Award conferral preserves authority/provenance.
14. Award revocation/correction does not delete historical conferral.
15. Rank-derived Awards do not silently migrate when Rank changes.
16. Finalization is an explicit high-consequence Organizer action.
17. Finalization requires all mandatory readiness gates to pass.
18. A failed Finalization attempt produces no partial official outcome.
19. Finalization establishes an Official Outcome Revision rather than only a boolean state.
20. Official Outcome is a reconstructible snapshot/projection, not another general Result Concept.
21. Every Official Outcome Revision identifies the authoritative basis sufficient to reconstruct it.
22. Prior Official Outcome Revisions remain historical after correction.
23. Post-finalization source changes never silently rewrite official Rank/Awards.
24. Post-finalization corrected outcomes require explicit Organizer reconciliation and successor confirmation.
25. Competition may remain lifecycle-Finalized while its official outcome undergoes exceptional correction.
26. Finalization does not automatically publish results publicly.
27. Public result disclosure remains separate from internal authority/finalization.
28. Finalization does not restore Judge access to private evaluation records.
29. Official Rank remains derived and cannot be manually overridden outside declared policy/adjudication.
30. Discretionary Award selection is not silently inferred from Note text or hidden algorithms.
31. Reopening live judging and correcting a Finalized Competition remain distinct operations.
32. Retained official outcomes must retain enough underlying authority context for explanation.

---

# 34. Open policy questions carried forward

002-G intentionally leaves several Competition-specific choices configurable or deferred:

- exact Award catalog;
- which Awards are required for Finalization;
- exact recipient cardinality per Award;
- whether discretionary Award rationale is mandatory;
- whether rank-derived Award confirmation can later be made fully automatic;
- whether public result publication exists in the initial release;
- official-outcome/public-announcement timing;
- detailed post-finalization outcome-correction status names;
- retention periods;
- whether formal multi-round advancement later introduces Stage/Round-scoped Awards and outcomes.

These do not block the current concept specification.

---

# 35. Handoff to 002-H

002-H should specify how authoritative Competition information is represented outside the live application and how the event remains operational when technology degrades.

The key inputs now available are:

```text
Rubric Versions
Competition/Event information
Panel / Encounter context
Team Alias
Judge participation/access initiation information
Scorecard semantics
Official Outcome Revisions
Award conferrals
```

002-H should therefore define:

- Export source/version identity;
- printable Rubrics/Scorecards;
- Event information artifacts;
- Panel/join materials;
- machine-readable identifiers where helpful;
- privacy-safe printed/displayed information;
- paper source handling;
- digital outage transition;
- later paper capture/reconciliation;
- regenerated official-result materials after correction;
- external representation traceability.

---

# 002-G Exit Position

The Competition-outcome lifecycle can now be expressed as:

```text
ACTIVE JUDGING
      ↓
EVENT COMPLETED
      ↓
RECONCILIATION
      │
      ├── evidence corrected
      ├── Coverage resolved
      ├── policy issues resolved
      ├── Rank becomes ready
      └── Awards resolved
      ↓
FINALIZATION READY
      ↓
Organizer explicit confirmation
      ↓
COMPETITION FINALIZED
      ↓
OFFICIAL OUTCOME v1
```

And exceptional correction remains controlled:

```text
OFFICIAL OUTCOME v1
      ↓
verified post-finalization issue
      ↓
source correction + impact review
      ↓
corrected provisional outcomes
      ↓
Award correction/reconfirmation
      ↓
OFFICIAL OUTCOME v2
```

This preserves a central MUDAC principle:

> **Official outcomes are authoritative and correctable, but never silently rewritten.**

The system can now move into 002-H with a complete distinction between internal authoritative state and the printable/public/external representations created from that state.
