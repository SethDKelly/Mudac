---
type: Phase Design Record
title: 014-C — Competition, Competitor, Grouping, Identity, Participation, Alias & Access Familiarity/Reuse Audit
description: "Audits Phase-014 Family-1 Concepts against domain and cross-application familiarity precedents, dispositions expectation-transfer fit and false-familiarity risk, and routes one discovered event-completion Access composition contradiction to its natural Phase-011 owner."
status: stable
tags: [phase-014, jackson, familiarity, reuse, competition, grouping, identity, participation, alias, access]
sources:
  - resource: 014-A-familiarity-reuse-genericity-scope-criteria-evidence-subphase-planning.md
  - resource: 014-B-familiarity-evidence-baseline-precedent-taxonomy-comparison-register.md
  - resource: ../canonical/concepts/competition.md
  - resource: ../canonical/concepts/division.md
  - resource: ../canonical/concepts/team.md
  - resource: ../canonical/concepts/panel.md
  - resource: ../canonical/concepts/identity.md
  - resource: ../canonical/concepts/participation.md
  - resource: ../canonical/concepts/alias.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/synchronizations/competition-participation-access.md
  - resource: ../canonical/synchronizations/evaluation-occurrence-obligation.md
  - resource: ../canonical/experience/context-role-modes.md
  - resource: ../canonical/experience/judge-onboarding.md
  - resource: ../canonical/experience/judge-evaluation.md
  - resource: https://csrc.nist.gov/pubs/sp/800/63/4/final
    title: NIST SP 800-63-4 Digital Identity Guidelines
  - resource: https://csrc.nist.gov/pubs/sp/800/162/upd2/final
    title: NIST SP 800-162 Attribute Based Access Control
  - resource: https://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX:32018R1725
    title: EU Regulation 2018/1725 pseudonymisation definition
---

# Purpose

Perform the first disposition-forming Phase-014 familiarity/reuse audit over the Family-1 Concepts:

```text
Competition
Division
Team
Panel
Identity
Participation
Alias
Access
```

014-C asks whether familiar domain/software precedents transfer **mostly correct expectations** about each Concept's purpose and behavior, where familiar language creates false expectations, whether any concept identity/name should change, and whether comparison exposes an upstream semantic defect rather than a familiarity issue.

# Decision

**COMPLETE — PASS after one targeted Phase-011 canonical synchronization repair. Proceed to 014-D.**

```text
014-A start gate                                   COMPLETE — READY
014-B evidence / precedent baseline                COMPLETE — PASS
014-C Family-1 familiarity/reuse audit             COMPLETE — PASS
Concept rename / merge / replacement               NONE
new Concept                                        NONE
Phase-010 Concept-boundary reopen                  NO
Phase-011 targeted composition repair              YES — event-completion Access seam
Phase-012 dependence/PF-01 reopen                  NO
Phase-013 mapping reopen                           NO
architecture / implementation influence            PROHIBITED
NEXT                                                014-D
```

# 1. Family-level result

The current Family-1 model is **deliberately familiar at the concept level and deliberately non-collapsed at the authority seams**.

The core reuse result is:

```text
Competition    ≈ bounded competition occurrence
Division       ≈ scoped competitive cohort/category
Team           ≈ competing unit
Panel          ≈ reusable intended evaluator grouping
Identity       ≈ stable human identity continuity
Participation  ≈ scoped time-bounded involvement/capacity
Alias          ≈ scoped alternate/pseudonymous identity
Access         ≈ contextual authorization/disclosure decision
```

The approximation symbol means familiar conceptual family, not identity of every precedent implementation.

No Family-1 Concept should be replaced by a generic `User`, `Role`, `Permission`, `Group`, `Task`, or `Session` abstraction.

# 2. Disposition summary

| MUDAC Concept | Primary familiar precedent | Disposition | Current-name decision | Main transferred-expectation constraint |
| --- | --- | --- | --- | --- |
| Competition | competition / contest / event occurrence | **SEMANTIC FIT / REUSE CANDIDATE** | retain | lifecycle context must not imply official result/publication |
| Division | division / category / class / cohort | **SEMANTIC FIT / REUSE CANDIDATE** | retain | classification must not imply bracket progression/ranking ownership |
| Team | team / entrant / competing unit | **SEMANTIC FIT / REUSE CANDIDATE** | retain | administrative competing unit need not own roster/collaboration/evaluation semantics |
| Panel | judging panel / evaluator group | **SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS** | retain | intended grouping must not imply actual occurrence participation, responsibility or collective verdict authority |
| Identity | person identity / digital identity continuity | **SEMANTIC FIT / REUSE CANDIDATE** | retain | identity must not collapse into account/authentication/session or Competition authority |
| Participation | participation / enrollment / scoped membership | **SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS** | retain | scoped capacity must not imply current Access or permanent role membership |
| Alias | alias / pseudonym / pseudonymous identifier | **SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS** | retain | alternate identity must not be reduced to cosmetic display name or authentication secret |
| Access | contextual authorization / ABAC-like decision | **SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS** | retain pending 014-F terminology audit | permit/deny decision must not be interpreted as persisted RBAC grant or semantic authorship |

No concept receives **DISTINCT / RETAIN NOVELTY** as its primary Family-1 disposition; the novelty lies mainly in MUDAC's careful composition boundaries among otherwise recognizable concepts.

# 3. Competition

## Current meaning

Competition owns one competition occurrence's identity, descriptive context and lifecycle:

```text
Draft → Ready → Active → Event Completed → Finalized
```

It does not own declared official-result currentness, which belongs to Outcome Declaration.

## Familiar precedents

`competition`, `contest`, and bounded `event` all transfer useful expectations:

- one scoped occurrence;
- participants/configuration exist within it;
- it starts and ends;
- it has lifecycle consequences;
- results may later be associated with it.

## Fit

The term **Competition** is a strong domain-stable fit for MUDAC's governing occurrence context.

The important constraint is that many products colloquially treat “competition finished/finalized” as equivalent to “official results established/published.” MUDAC intentionally does not.

Preserve:

```text
Competition Event Completed
  != Competition Finalized
  != Outcome Declaration
  != Publication
```

## Disposition

**SEMANTIC FIT / REUSE CANDIDATE — retain `Competition`.**

`Event` is useful explanatory vocabulary but too broad to replace the domain term. `Tournament` is a poor substitute because it imports bracket/match progression expectations not owned by Competition.

# 4. Division

## Current meaning

Division partitions competing Members within a Scope into mutually exclusive cohorts intended for legitimate comparison. It owns cohort definition, assignment and assignment-correction history, not ranking.

## Familiar precedents

`division`, `category`, `class`, and `cohort` are domain-stable comparison concepts.

The strongest expectation transfer is:

- competitor classification into one comparison cohort;
- cohort naming/definition;
- assignment can change/correct;
- comparisons occur within the cohort.

## False-familiarity pressure

Some competition/sports meanings of `division` imply league hierarchy, bracket structure, promotion/relegation or a ranking owner. None belongs intrinsically to MUDAC Division.

## Disposition

**SEMANTIC FIT / REUSE CANDIDATE — retain `Division`.**

The current generic shape `Division<Scope, Member>` is already appropriately reusable. No broader generalization is adopted in 014-C.

# 5. Team

## Current meaning

Team is the stable administrative representation of one student group participating as one competing unit in Scope.

It owns administrative identity, descriptive attributes and Active/Withdrawn status. It does not own Division, Alias, evaluation responsibility/evidence or outcome state.

## Familiar precedents

`team`, `entrant`, `competitor`, and `submission group` transfer partially overlapping expectations.

Because MUDAC's real-world competitors are student groups, **Team** transfers the most useful domain understanding.

## False-familiarity pressure

A generic software or sports `team` may imply:

- member/roster management;
- collaboration permissions;
- internal ownership/leadership;
- persistent organization across many competitions.

MUDAC Team currently promises none of those as intrinsic semantics.

## Disposition

**SEMANTIC FIT / REUSE CANDIDATE — retain `Team`.**

`Entrant` is a useful analogy but weaker than Team for the current product because it obscures the real group nature of the competitor. If future scope introduces solo competitors, that would be a future genericity/product-family question rather than a reason to rename now.

# 6. Panel

## Current meaning

Panel maintains a reusable grouping of evaluator Members intended to operate together. It is planning/grouping authority, not actual occurrence participation, individual responsibility or judgment authority.

## Familiar precedents

`judging panel`, `jury`, `committee`, and `judge group` all transfer the basic idea of a group of evaluators.

`judging panel` is the best fit because reuse across multiple evaluation situations and human-facing grouping are familiar event concepts.

## False-familiarity pressure

The major transferred expectation to resist is:

```text
member of judging panel
  → actually participated
  → owes evaluation
  → shares collective decision authority
```

MUDAC explicitly preserves:

```text
Panel membership
  != Evaluation Occurrence participation
  != Evaluation Obligation
  != Scorecard evidence
```

`Jury` and `committee` are therefore weaker substitutes because they strongly suggest collective deliberation/decision authority.

## Disposition

**SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS — retain `Panel`.**

The mapping obligation remains to make Panel read as intended grouping, not proof of actual work or collective verdict.

# 7. Identity

## Current meaning

Identity maintains stable human continuity across Competition occurrences. It owns minimal identity continuity/verification state while Participation owns event capacity and Access owns current permission/disclosure.

## Defined precedent evidence

NIST SP 800-63-4 treats digital identity services as a family involving identity proofing/enrollment, authentication and federation rather than treating identity itself as application role authority.

That precedent supports MUDAC's separation between **who the human is** and what the human may currently do inside a Competition.

## False-familiarity pressure

The following are not semantic substitutes:

- `Account` — imports credential/profile/service-membership expectations;
- `User` — conflates human, system actor and application capacity;
- `Principal` — useful authorization input terminology but too technical and not necessarily a human identity concept;
- `Session` — runtime continuity, not human continuity.

## Disposition

**SEMANTIC FIT / REUSE CANDIDATE — retain `Identity`.**

The current concept is reusable beyond MUDAC precisely because it is independent of Competition role and authentication mechanism.

# 8. Participation

## Current meaning

Participation represents a Participant taking part in a supplied Scope for a limited period in a particular Capacity.

Conceptually:

```text
Participation<Participant, Scope, Capacity>
```

It owns the scoped relationship/capacity lifecycle, not Identity continuity or Access permission.

## Familiar precedents

Useful precedents include:

- participation;
- enrollment/registration;
- scoped membership;
- event role/capacity assignment.

No one substitute captures the current semantics as well as `Participation` itself.

## False-familiarity pressure

`Membership` may imply long-lived governance rights or group belonging.

`Role` may imply direct authorization capability.

`Enrollment`/`Registration` often describe only entry rather than the whole active/completed/withdrawn participation lifecycle.

Therefore:

```text
Participation
  != permanent membership
  != role/permission bundle
  != enrollment record only
```

## Disposition

**SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS — retain `Participation`.**

The existing generic parameters are already a strong reuse-oriented design. No additional generalization is adopted yet.

# 9. Alias

## Current meaning

Alias gives a Subject a context-specific alternate identity inside a Scope while preserving historical mapping and making resolution to the underlying Subject an Access-controlled operation.

Conceptually:

```text
Alias<Subject, Scope, AliasValue>
```

## Familiar precedents

`alias`, `pseudonym`, `pseudonymous identifier`, and `anonymized/blinded identifier` are useful comparisons.

The EU data-protection definition of pseudonymisation provides a useful defined precedent for **re-attributable alternate representation**: data can cease to be attributable without additional separately controlled information. MUDAC does not adopt the legal regime or claim GDPR/EUDPR pseudonymisation compliance, but the semantic shape is useful comparison evidence.

## False-familiarity pressure

`display name` and `nickname` import cosmetic, user-controlled and often non-historical expectations that are incompatible with bias-control identity.

`anonymous identifier` may incorrectly imply that resolution is impossible.

MUDAC requires:

```text
alternate scoped identity
+ historical reservation/traceability
+ protected resolution
```

## Disposition

**SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS — retain `Alias`.**

`Pseudonym` is a useful explanatory analogy, not a required rename. Terminology remains eligible for the cross-catalog 014-F review.

# 10. Access

## Current meaning

Access evaluates a contextual capability/disclosure decision over:

```text
Principal
Capability
Resource
ContextFacts
Rule
```

Ordinary capability may be derived rather than stored. Purpose-specific exceptional grants may exist. Permission never transfers semantic authorship.

## Defined precedent evidence

NIST SP 800-162 defines attribute-based access control as authorization determined by evaluating subject, object, requested operation and sometimes environment conditions against policy/rules/relationships.

That is a strong semantic precedent for MUDAC's contextual `Access.check` model:

```text
subject/principal attributes
+ protected resource/object
+ requested operation/capability
+ contextual/environment facts
+ rule/policy
→ permit / deny
```

The fit is conceptual, not an implementation mandate to use an ABAC product or architecture.

## False-familiarity pressure

The name `Access` is conventionally familiar but variable. It can incorrectly imply:

- a persisted permission row;
- role-based capability inheritance;
- broad account entitlement;
- possession of a URL/session/token;
- authority to author or decide the protected domain meaning.

MUDAC instead requires contextual evaluation and preserves:

```text
Identity != Participation != Access
Access permission != semantic authorship
actor visibility != audience disclosure permission
```

## Disposition

**SEMANTIC FIT / REUSE CANDIDATE WITH CONSTRAINTS — retain `Access` pending 014-F terminology audit.**

The most reusable precedent is contextual authorization/ABAC-like semantics, not a generic RBAC `Role → Permission` model.

# 11. Cross-concept familiarity result

The Family-1 concepts should be familiar **as a composition of independent ideas**, not simplified into a conventional actor model.

Reject:

```text
Account/User
  → Role
  → Permission
  → Group
```

as a replacement conceptual model because it would erase important MUDAC meanings:

```text
Identity continuity
  != Participation capacity
  != Panel grouping
  != Access decision
  != evaluation responsibility
  != semantic authorship
```

A familiar implementation model is not conceptual reuse when it destroys correct expectation transfer.

# 12. Upstream contradiction discovered — event completion Access seam

014-C identified a genuine composition contradiction rather than a familiarity defect.

The current Phase-011 synchronization owner still stated:

```text
Competition.completeEvent
  → live Judge Participations complete
  → ordinary Judge private-evaluation Access is categorically denied
```

But the accepted Phase-013 Experience model establishes:

```text
Event Completed
  != all Evaluation Obligations terminal
  != all Scorecards Finalized
  != universal hidden Access revocation

Outstanding Evaluation Obligation
  + current policy / Access permits continuation
  → same logical Judge evaluation may continue
```

Because synchronization authority is upstream of Experience mapping, leaving the older rule unchanged would make the current design internally contradictory.

## Corrected composition

The natural Phase-011 owner is repaired to distinguish **ordinary live-event capability** from **narrow continuation of already-established responsibility**:

```text
Competition.completeEvent
  → active live Judge Participations complete
  → broad/new live-event judging capability closes
  → no new occurrence/ordinary obligation establishment merely from old live context

existing Outstanding Evaluation Obligation
  + exact existing subject/basis/occurrence binding
  + current policy permits completion after event end
  + fresh Access.check permits obligation-scoped Judge work
  → same logical Scorecard may start/resume/finalize
```

This does not reactivate the Judge Participation, reopen the Competition, create new obligations, or restore general event-day capability.

If new live-event participation/new ordinary occurrences are required, use the explicit resume/restoration composition. If genuinely new responsibility is needed because prior responsibility terminated or evidence became unusable, use the established successor-work semantics.

## Routing decision

This is a **targeted Phase-011 canonical synchronization repair**, not a Phase-010 Concept-boundary reopen and not a Phase-013 mapping change.

The historical 011-C record remains provenance for the earlier decision and receives a later-correction notice rather than being rewritten as if the former rule never existed.

# 13. Genericity observations deferred to 014-G

Family-1 comparison exposes strong existing genericity but makes no additional generalization decision yet:

```text
Division<Scope, Member>
Team<Scope>
Panel<Scope, Member, CapacityLabel>
Participation<Participant, Scope, Capacity>
Alias<Subject, Scope, AliasValue>
Access<Principal, Capability, Resource, ContextFacts, Rule>
```

These abstractions already remove substantial MUDAC incidental specificity.

014-G should still probe whether:

- Team's fixed group semantics need a broader competitor/entrant concept for future product families;
- Competition is intentionally domain-specific rather than a generic Scope/Event concept;
- Access and Participation names remain the best familiar vocabulary for their generic shapes;
- Panel's `CapacityLabel` is configuration rather than over-specialization.

No change is adopted here.

# 14. Risk disposition

014-C materially advances the Phase-014 risk register:

- **FRG-R01 Name-equals-fit** — controlled; each Family-1 concept compared by behavior.
- **FRG-R02 Popularity bias** — controlled; no precedent adopted because it is common.
- **FRG-R03 False familiarity** — active constraints documented for every Family-1 concept.
- **FRG-R04 Implementation reuse leakage** — controlled; NIST ABAC used as semantic precedent only.
- **FRG-R05 Over-generalization** — no Family-1 generalization adopted yet.
- **FRG-R06 Similarity merge** — actor/context concepts remain independent.
- **FRG-R07 Under-generalization** — deferred to 014-G with concrete candidates.
- **FRG-R10 Mapping drift after rename/generalization** — no rename/generalization performed.
- **FRG-R11 Scope/composition breakage** — one pre-existing contradiction found and repaired in natural Phase-011 owner.
- **FRG-R12 Profile conflation** — no Judge/Organizer capability union permitted.
- **FRG-R13 Historical-adapter revival** — no Encounter/revision restoration.
- **FRG-R15 Integrity deferral abuse** — discovered composition contradiction repaired now rather than deferred to Phase 015.

# 15. 014-D handoff

014-D should audit:

```text
Evaluation Occurrence
Evaluation Obligation
Rubric
Scorecard
```

with particular attention to false transfer from:

- `session` / `encounter` / `attempt` into occurrence;
- `task` / `assignment` into obligation;
- `form` / `template` into Rubric;
- `submission` / `completed form` into Scorecard.

The Family-1 result that must remain fixed during 014-D is:

```text
Panel membership
  != occurrence participation
  != obligation responsibility
  != Scorecard evidence

Identity
  != Participation
  != Access
```

# Exit decision

**014-C COMPLETE — PASS. Proceed to 014-D — Evaluation Occurrence, Obligation, Rubric & Scorecard Familiarity/Reuse Audit.**
