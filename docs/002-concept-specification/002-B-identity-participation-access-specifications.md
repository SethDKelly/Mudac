# 002-B — Identity, Participation & Access Specifications

Status: **Complete**

## 1. Purpose

002-B specifies the human-security boundary established in Phase 001. It covers three accepted supporting concepts:

1. Identity
2. Participation
3. Access

The goal is to preserve three distinct questions:

```text
Identity
    Who is this person?

Participation
    Why are they involved in this Competition, and in what capacity?

Access
    What may they do or see right now?
```

These concepts must remain independent. Authentication technology, session implementation, identity-provider choice, AWS authorization services, and concrete credential mechanisms remain deferred.

The specification also defines the role of Judge and Organizer as Participation roles, the system-level nature of Administrator authority, event-scoped Judge access, returning-Judge behavior, dual-role handling, shared-device expectations, and temporary post-event correction access.

---

## 2. Cross-concept model

```text
IDENTITY
    │
    │ establishes continuity
    ▼
PARTICIPATION
    │
    │ establishes event-scoped capacity
    ▼
ACCESS
    │
    │ permits or denies a capability
    ▼
Competition resources and actions
```

The arrows represent synchronization rather than ownership.

Identity does not know the person's Competition role.

Participation does not know how authentication was performed.

Access does not redefine the identity or participation relationship; it evaluates whether a particular capability is permitted in the current context.

---

# 3. Identity specification

## Purpose

> Maintain enough verified continuity to attribute actions and participation episodes to the same human identity without requiring permanent Competition authority.

Identity exists because the system must distinguish individual Judges and Organizers, attribute Scorecards and corrections, support safe recovery, and optionally recognize returning volunteers in later Competitions.

Identity does not imply a permanent application account experience. A first-time Judge may establish only the minimum continuity needed for the current Competition.

## State

Conceptual state:

```text
Identity
    stable identity reference
    human-facing identification attributes
    verification state
    verification/recovery handles
    status
```

Human-facing identification attributes should be limited to what is operationally necessary. Phase 002 does not require a large profile model.

Possible examples include:

- display/preferred name;
- contact or verification handle;
- optional recognition information needed for future re-verification.

The concrete fields remain an implementation/privacy decision.

## Identity status

A minimal working distinction is:

```text
Established
Disabled
```

`Established` means the system can maintain continuity for that person.

`Disabled` prevents ordinary future use while retaining historical attribution.

Identity should not acquire event states such as `Checked In`, `Judge`, or `Completed`; those belong to Participation.

## Actions

```text
establish
verify
reverify
updateNecessaryIdentityInformation
recover
recognizeReturningIdentity
disable
restore
```

The exact difference between establish and verify depends on the eventual authentication mechanism. Conceptually, however, identity continuity and proof of current control remain distinguishable.

## Queries

```text
isEstablished(identity)
isDisabled(identity)
canBeReverified(identity)
matchingIdentity(candidate information)
```

`matchingIdentity` must be designed cautiously. The system should not merge two people solely because they share a common name.

## Operational Principle

A first-time volunteer arrives at a Competition. The system establishes enough verified Identity continuity to distinguish that person from other Judges. The person then enrolls in a Competition Participation. At a later annual Competition, the prior Identity may be recognized and reverified, reducing repeated entry while still creating a new Participation for the new event.

## Invariants

1. Identity is independent of Competition role.
2. Identity does not automatically grant Competition access.
3. Historical actions remain attributable after Identity access is disabled.
4. Disabling an Identity does not delete Scorecards, Participation history, Provenance, or other historical records.
5. Identity matching must not silently merge distinct people based on weak evidence.
6. Returning recognition never restores prior Competition authority automatically.

## Explicit non-responsibilities

Identity does not own:

- Judge/Organizer role;
- expertise;
- Panel membership;
- Competition access;
- Scorecards;
- authorization policy;
- authentication technology.

---

# 4. Authentication boundary

Authentication is intentionally not an accepted Concept.

It is the implementation mechanism by which the system establishes current control of an Identity.

Possible future mechanisms include:

```text
one-time event link
QR-initiated verification
magic link
one-time code
passkey
federated identity
organizer-assisted activation
```

002-B requires only that the selected mechanism support the Identity and Access semantics defined here.

A QR code alone must never mean:

```text
possesses QR
    =
trusted Judge
```

A QR code may begin an authentication or Participation workflow, but Identity verification and Access evaluation remain separate.

---

# 5. Participation specification

## Purpose

> Represent an Identity taking part in a particular Competition in a particular capacity for a bounded period.

Participation solves the problem that the same person may participate differently across Competitions or even hold more than one legitimate capacity within one Competition.

Examples:

```text
Identity A
    ├── Competition 2026 → Judge Participation
    └── Competition 2027 → Judge Participation
```

or:

```text
Identity B
    └── Competition 2026
           ├── Organizer Participation
           └── Judge Participation
```

Whether a Competition allows dual-role participation is policy, but the conceptual model must not prohibit it accidentally.

## State

Conceptual state:

```text
Participation
    identity reference
    competition scope
    role
    status
    declared participation attributes
    lifecycle timestamps
```

For a Judge Participation, declared attributes may include:

```text
expertise: one or more values
primary expertise: optional
availability information: optional
```

Expertise remains Participation state rather than an independent Concept.

## Participation roles

Initial Competition-scoped roles:

```text
Judge
Organizer
```

Administrator is not simply another Competition role. Administrator authority is primarily system-scoped and is handled separately under Access policy.

Future delegated Organizer variants may exist without changing Participation's purpose.

## Participation lifecycle

A minimal lifecycle is:

```text
Enrolled
   ↓
Checked In
   ↓
Active
   ↓
Completed
```

with exceptional paths:

```text
Enrolled → Withdrawn
Checked In → Withdrawn
Active → Withdrawn
```

and possible restoration/re-enrollment while Competition policy permits.

The exact UI language may differ; these states express distinct behavioral meaning.

### Enrolled

The person has been accepted/recorded as participating in the Competition but is not yet considered present and operational.

### Checked In

The person is present for the live event and may become eligible for operational assignment.

### Active

The Participation is currently exercising its role in live Competition operations.

For Judges, this normally means the person can be assigned to a Panel and can participate in Judging Encounters if Access permits.

### Completed

The active event participation has ended. Historical attribution remains, but ordinary live-event capabilities no longer follow from the Participation.

### Withdrawn

The Participation should not be used for future live operations unless explicitly restored under policy.

Withdrawal does not erase prior Encounters or Scorecards.

## Actions

```text
enroll
checkIn
activate
updateDeclaredAttributes
withdraw
restore
complete
```

## Queries

```text
participationsFor(identity, competition)
roleOf(participation)
statusOf(participation)
isOperationallyEligible(participation)
expertiseOf(judge participation)
isCurrent(participation)
```

`isOperationallyEligible` is partly policy-derived. For example, a Judge may need to be Checked In or Active before Panel assignment.

## Operational Principle

A volunteer establishes Identity, enrolls as a Judge for the current Competition, confirms their current expertise, checks in upon arrival, becomes Active for live judging, participates in Panels and Encounters, and becomes Completed when the event ends. A later annual Competition creates a new Participation even if the same Identity is reused.

## Invariants

1. Participation is scoped to exactly one Competition.
2. Participation references one Identity.
3. Role is contextual to the Participation rather than permanent Identity state.
4. Completion or withdrawal never deletes historical actions attributable to the Participation.
5. A prior Competition's Participation never automatically becomes active in a later Competition.
6. Expertise belongs to Judge Participation and may contain more than one value.
7. Expertise does not itself grant authority.
8. Panel membership does not change Participation role.
9. Participation state alone is insufficient to authorize sensitive actions; Access must also permit them.

---

# 6. Judge participation semantics

Judge is a Participation role, not a standalone Concept.

The purpose of Judge Participation is:

> Represent this Identity's temporary capacity to perform independent evaluation in this Competition.

A Judge Participation may be first-time or returning. The Competition does not require a long-lived Judge account.

## First-time Judge

```text
no recognized Identity
        ↓
establish + verify Identity
        ↓
enroll Judge Participation
        ↓
confirm expertise
        ↓
check in
```

## Returning Judge

```text
recognized prior Identity
        ↓
reverify current control
        ↓
new Judge Participation
        ↓
reconfirm expertise
        ↓
check in
```

Prior expertise may be offered as a convenience but must not silently become authoritative current-event information.

## Judge history

A Judge's previous Participation and evaluation authorship remain part of the historical Competition record.

However, ordinary post-event access to prior private Scorecards and Notes does not follow merely because the same Identity exists.

This preserves the rule:

> Judge records persist; Judge access does not.

---

# 7. Organizer participation semantics

Organizer is also a Competition-scoped Participation role.

Its purpose is:

> Represent an Identity's authority to configure, operate, reconcile, and conclude a particular Competition.

Organizer Participation can be established before the live event and may remain operational through post-event reconciliation and historical administration according to policy.

Unlike Judge Participation, Organizer Participation does not automatically complete at Event Completed because the Organizer still needs to:

- capture paper Scorecards;
- resolve Coverage exceptions;
- review revisions;
- determine Rankings;
- confer Awards;
- finalize the Competition.

Organizer Participation therefore may remain Active beyond the live event until Competition governance no longer requires it.

The exact archival/retention lifecycle for Organizer Participation remains a later security/retention policy question.

---

# 8. Dual-role identities

The system must permit the conceptual possibility that one Identity has both:

```text
Organizer Participation
Judge Participation
```

in the same Competition.

This does not imply that such a pattern should be encouraged.

The critical rule is:

> Actions occur under an identifiable Participation context and receive only the Access appropriate to that context.

A dual-role person should therefore not automatically see Organizer scoring analytics while they are actively acting as a Judge.

The eventual UI should make the current operating context explicit rather than silently combining capabilities.

Conceptually:

```text
Identity X
    │
    ├── Organizer Participation
    │       └── Organizer Access context
    │
    └── Judge Participation
            └── Judge Access context
```

Switching contexts may require explicit interaction and, for high-sensitivity transitions, re-verification or another intentional confirmation depending on security policy.

---

# 9. Access specification

## Purpose

> Permit or deny a specific action or disclosure according to principal, capability, scope, resource, Competition state, ownership, and time.

Access exists because role alone cannot safely answer whether an operation is allowed.

For example:

```text
Judge
```

is insufficient to decide whether the person may edit a Scorecard.

The real question resembles:

```text
Is this Judge Participation
allowed to amend
this specific Scorecard
which they authored
for this Competition
in its current state
at this time?
```

## Access model

Conceptually, an Access decision evaluates:

```text
principal
    usually Identity + active Participation context

capability
    read / create / update / finalize / amend / confer / etc.

scope
    system / Competition / Encounter / resource

resource
    Scorecard / Team identity / Award / etc.

resource relationship
    own Scorecard / another Judge's Scorecard / etc.

Competition lifecycle
    Draft / Ready / Active / Event Completed / Finalized

validity
    ordinary / temporary / expired / revoked
```

This does not prescribe RBAC, ABAC, policy engines, IAM, or any specific authorization implementation.

## State

Conceptual Access state may include explicit grants or revocations where necessary:

```text
Access Grant
    principal/context
    capability set
    resource/scope
    valid-from
    valid-until
    status
    purpose/reason where exceptional
```

However, ordinary Access may be derived from Participation role + Competition state + ownership + policy rather than persisted as one grant per action.

The Concept's purpose is the authorization/disclosure decision, not a requirement that every permission be represented as a database row.

## Actions

```text
grant
revoke
expire
temporarilyGrant
check
```

`check` represents the conceptual decision operation.

## Queries

```text
may(principal, capability, resource, context)
activeGrants(principal)
accessExpiry(grant)
```

## Operational Principle

A Judge Participation is Active during the event. Access permits the Judge to see Team Alias and Division, read/write their own Draft Scorecard, finalize their own evaluation, and view their own event judging history. Access denies peer Scorecards, peer Notes, institutional Team identity, and competition standings. When the event completes, ordinary Judge access to private evaluation records expires while the records remain available to authorized Organizers.

## Invariants

1. Identity alone never grants sensitive Competition capability.
2. Participation role alone is insufficient for every Access decision.
3. Access cannot change underlying historical authorship.
4. Revoking Access never deletes the protected resource.
5. Judge Access never reveals administrative Team identity by default.
6. Judge Access never reveals peer evaluation content by default.
7. Judge Access never reveals competition-wide scoring or Ranking by default.
8. Organizer scoring visibility does not imply the right to silently rewrite Judge-authored evaluation.
9. Expired Judge Access cannot be recovered merely by using a stale URL or browser session.
10. Exceptional temporary Access must be narrower than ordinary Organizer-wide or Judge-wide historical access.
11. System administration authority does not automatically imply Competition decision authority.

---

# 10. Capability categories

002-B standardizes capability-oriented reasoning rather than broad role checks.

Initial capability families include:

```text
Competition structure
    configure competition
    manage divisions
    manage teams
    resolve aliases

Participation operations
    enroll judge
    check in
    manage expertise
    manage panels

Evaluation
    start own Scorecard
    edit own Scorecard
    finalize own Scorecard
    amend own Scorecard
    capture paper evaluation

Private-data disclosure
    view own Scorecard
    view own Notes
    view another Judge's Scorecard
    resolve Team administrative identity

Scoring/outcomes
    view aggregate scoring
    view ranking
    resolve coverage exception
    confer Award
    finalize Competition

System operations
    operate infrastructure
    support service
    perform exceptional break-glass intervention
```

Later specification groups refine the resource-specific conditions for these capabilities.

---

# 11. Judge default access profile

During Active Competition operation, an Active Judge Participation should normally be able to:

```text
view event information
view own Participation state
view own Panel context
view Team Alias and Division for relevant judging
view own event judging history
create/use own Scorecard for eligible Encounter
edit own Draft Scorecard
view own Notes
finalize own Scorecard
amend own Scorecard if current amendment policy permits
```

A Judge should normally not be able to:

```text
resolve Team Alias to institution
view another Judge's scores
view another Judge's Notes
view Panel aggregate scoring
view Team aggregate scoring
view Division Ranking
view Competition standings
alter Rubric definitions
change Panel membership
change Division assignment
confer Awards
finalize Competition
```

These are defaults, not a statement that every capability is implemented in 002-B.

---

# 12. Judge access cutoff

Phase 001 established that Judge Scorecards, Notes, and judging history are private data whose access should not persist indefinitely.

002-B standardizes the default cutoff as:

> **Competition Event Completed ends ordinary Judge access to private evaluation records.**

Thus:

```text
Competition = Active
    ↓
Judge ordinary evaluation Access active

Competition.completeEvent
    ↓
Judge ordinary private-data Access expires
```

After Event Completed, a Judge should not ordinarily be able to browse:

- prior Scorecards;
- prior Notes;
- Team-by-Team judging history;
- active or historical scoring information.

The Participation remains historically attributable.

The Identity remains available for re-verification or future event participation as appropriate.

The Scorecards and Notes remain in the Competition record.

---

# 13. Event completion synchronization

The following synchronization becomes canonical:

```text
when Competition.completeEvent succeeds

for ordinary Judge evaluation Access in that Competition:
    expire/revoke private evaluation capabilities

for Judge Participations:
    transition live participation toward Completed

preserve:
    Identity
    Participation history
    Scorecards
    Notes
    Encounter history
    Provenance
```

The exact ordering/transaction model is architectural, but the externally observable state must converge to this result.

If `Competition.resumeEvent` is legitimately used before Finalization, appropriate live capabilities may be re-established through a new Access evaluation rather than by assuming all previous sessions remain valid.

---

# 14. Post-event Scorecard correction

A Judge may still need to correct a legitimate error after ordinary access has expired.

This should not restore broad historical access.

The preferred model is:

```text
Organizer identifies/accepts correction need
        ↓
Judge Identity reverifies
        ↓
Access.temporarilyGrant
        ↓
capability:
    amend
resource:
    specific Scorecard
scope:
    current Competition
validity:
    bounded
purpose:
    correction
        ↓
Judge completes amendment
        ↓
Versioning + Provenance
        ↓
temporary Access revoked/expired
```

## Temporary grant invariants

1. A temporary correction grant applies only to the intended Judge Identity/Participation context.
2. It should target the specific Scorecard or narrow resource set requiring correction.
3. It does not restore general event judging history.
4. It has an explicit validity limit or ends upon successful correction.
5. Re-verification is required before exercising the grant.
6. Finalized Competition corrections require the stronger post-finalization governance defined in later Phase 002 work.

---

# 15. Access after Competition Finalized

Finalization establishes official Competition outcomes.

Judge access remains expired.

Organizer access may remain available for legitimate historical administration, but ordinary result-changing capabilities should no longer be available merely because the person is an Organizer.

Conceptually:

```text
Organizer Participation
        +
Competition = Finalized
        ↓
read/history capabilities may remain
ordinary mutation capabilities close
exceptional correction requires stronger authority
```

002-G and 002-E will specify the exact finalization/correction gates.

---

# 16. Organizer access profile

Organizer Access is broader than Judge Access because Organizers operate the Competition.

Before Finalization, authorized Organizer Participation may normally be able to:

```text
configure Competition structure
manage Divisions and Teams
resolve Alias mappings
manage Judge Participation
manage Panel membership
view Encounter operational state
view all Scorecard completion state
view evaluation content where governance permits
capture paper Scorecards
view Aggregates and Coverage
view Ranking
manage Awards
perform reconciliation
```

However:

> Organizer authority must not collapse authorship and operational control.

An Organizer being able to view or capture a Judge's evaluation does not mean the Organizer may silently alter the Judge's judgment.

Where an Organizer performs an exceptional change to Judge-authored evaluation, later Versioning/Provenance rules must clearly identify what happened and why.

---

# 17. Sensitive organizer capabilities

Some Organizer capabilities deserve stronger treatment than ordinary configuration.

Examples include:

```text
resolve Team administrative identity during blinded judging
view private Judge Notes
correct Division after judging exists
invalidate Encounter
open post-event Judge amendment
change official Award
finalize Competition
```

002-B classifies these as high-sensitivity capabilities but does not require separate Organizer roles yet.

The application may later implement stronger confirmation, reason capture, step-up authentication, or delegated authority without changing the underlying concepts.

---

# 18. Administrator boundary

Administrator is primarily a system-level authority role rather than Competition Participation.

Its purpose is operational:

> Keep the application available, secure, supportable, and maintainable.

The critical boundary remains:

```text
system authority
    ≠
Competition decision authority
```

An Administrator should not automatically receive ordinary capability to:

- alter Scorecards;
- change Rankings;
- confer Awards;
- resolve Team identities;
- inspect Judge Notes;
- finalize Competition outcomes.

Some technical operations may inherently expose protected data. Architecture should minimize this exposure where practical.

---

# 19. Break-glass administrative access

Phase 002 should allow for the possibility that extraordinary technical support requires access beyond ordinary Administrator scope.

This is **break-glass access**, not routine administration.

Conceptually:

```text
extraordinary operational need
        ↓
explicit break-glass authorization
        ↓
time/resource bounded Access
        ↓
Provenance / security audit
        ↓
automatic expiry
```

Examples might include recovery from corruption or a severe production incident.

002-B does not decide who approves break-glass access or which AWS mechanism implements it.

It does establish that such access must be distinguishable from normal Competition authority.

---

# 20. Shared and loaner devices

The Access model must support Judges who use Organizer-provided devices.

The core rule is:

> A device is not the principal; the verified Identity/Participation context is.

A shared device must therefore support explicit participant transitions.

Conceptually:

```text
Judge A session
    ↓
end/clear Judge A access context
    ↓
Judge B verifies
    ↓
Judge B session
```

The next Judge must not inherit:

- prior Scorecard content;
- prior Notes;
- prior judging history;
- prior Team context;
- reusable credentials permitting Judge A access.

Local/offline data clearing requirements will be addressed in architecture/operational continuity design, but the behavioral obligation is established here.

---

# 21. Lost device / session revocation

If a Judge loses a device:

```text
Judge Identity/Participation remains valid
        ↓
compromised session Access revoked
        ↓
Judge reverifies on another device
        ↓
new valid access context
```

The system should not require creation of a second Judge Participation merely because the device changed.

Any recoverable Scorecard Draft remains associated with the original Participation and Scorecard identity.

---

# 22. Session behavior boundary

Session management is implementation detail, but 002-B imposes behavioral requirements:

1. Active Judge sessions should remain usable through normal event activity without excessive repeated authentication.
2. Sessions must not remain indefinitely valid after their Access basis expires.
3. Event completion must render stale Judge sessions incapable of retrieving private evaluation data.
4. Session revocation must be possible after device loss or suspected compromise.
5. A resumed Competition should cause Access to be reevaluated rather than blindly trusting stale client state.

Exact session duration and refresh-token mechanics are deferred.

---

# 23. Information disclosure model

Access governs both **actions** and **representation**.

The same Team can therefore have:

```text
Organizer representation:
    administrative Team information
    Alias
    Division

Judge representation:
    Alias
    Division
```

This is not implemented by duplicating Team records.

Instead:

```text
Team + Alias + Access
        ↓
appropriate representation
```

This boundary must also hold in:

- print/export;
- notifications if later introduced;
- filenames;
- browser-visible metadata;
- shared displays.

---

# 24. Access to Judge Notes

Judge Notes are private evaluation data.

Default access:

```text
Authoring Judge
    during ordinary active access window

Authorized Organizer
    according to Competition governance needs
```

Default denial:

```text
other Judges
student Teams
public users
```

Notes do not become student feedback merely because they exist.

If a future feature publishes feedback, that should be an explicit release/transformation mechanism rather than direct exposure of the private judging record.

---

# 25. Access to results and scoring analytics

002-B confirms the Phase 001 visibility boundary:

```text
Judge
    no Competition-wide active scoring
    no Ranking
    no peer evaluation analytics
    no default post-event scoring archive

Organizer
    authorized operational scoring visibility
    Coverage
    Aggregates
    Ranking
    Panel/Judge analytical views
```

Public winner announcement is outside Judge Access semantics and may later be handled through public/exported event information if desired.

---

# 26. Participation and Panel eligibility

002-B provides the human-side contract for 002-C.

A Judge should normally be eligible for Panel membership only if:

```text
Participation.role = Judge
AND
Participation status satisfies live eligibility policy
AND
Identity is not disabled
AND
Access/security state does not prohibit participation
```

Expertise may influence Panel composition but does not determine permission by itself.

002-C will specify Panel membership and participant snapshots.

---

# 27. Participation and Scorecard authorship

002-B also establishes the identity-side contract for 002-D.

A Scorecard author reference must point to the relevant Judge Participation rather than merely a display name or transient session.

Thus historical attribution can resolve:

```text
Scorecard
    ↓
Judge Participation
    ↓
Identity
```

without making Identity itself the Competition role.

If a Judge's display name later changes, the historical authorship remains stable.

---

# 28. Access evaluation examples

## Example A — edit own active Draft

```text
principal:
    active Judge Participation J-12

capability:
    edit Scorecard

resource:
    Scorecard S-88

relationship:
    J-12 is author

Competition:
    Active

Scorecard:
    Draft

result:
    allow
```

## Example B — read another Judge's Scorecard

```text
principal:
    Judge Participation J-12

resource:
    Scorecard authored by J-13

result:
    deny
```

## Example C — access own Scorecard after event completion

```text
principal:
    Judge Participation J-12

Competition:
    Event Completed

ordinary grant:
    expired

result:
    deny
```

## Example D — post-event correction

```text
principal:
    Judge Participation J-12

Competition:
    Event Completed

resource:
    Scorecard S-88

temporary amendment grant:
    valid

Identity:
    reverified

result:
    allow amendment only
```

## Example E — Organizer captures paper Scorecard

```text
principal:
    Organizer Participation O-03

capability:
    capture paper evaluation

resource/evaluation author:
    Judge Participation J-12

result:
    allow if Competition policy permits

provenance:
    author = J-12
    capture actor = O-03
```

## Example F — Administrator tries to confer Award

```text
principal:
    system Administrator

capability:
    confer Award

Competition Participation:
    none

result:
    deny by default
```

---

# 29. Synchronization contracts

## Identity verification → Participation enrollment

```text
Identity verified
        +
Competition enrollment intent
        ↓
Participation.enroll
```

## Participation activation → ordinary Access

```text
Participation becomes operationally active
        ↓
Access evaluates/grants role-appropriate capabilities
```

## Participation withdrawal → Access restriction

```text
Participation.withdraw
        ↓
future operational capabilities revoked/denied
```

Historical attribution remains.

## Competition Event Completed → Judge completion/access expiry

```text
Competition.completeEvent
        ↓
Judge Participation leaves live operational state
        +
ordinary Judge private-data Access expires
```

## Competition resume → access reevaluation

```text
Competition.resumeEvent
        ↓
eligible Judge Participations reevaluated
        ↓
new valid Access context
```

## Temporary correction → Versioning/Provenance

```text
Organizer-authorized correction
        +
Judge reverification
        ↓
temporary Access
        ↓
Scorecard amendment
        ↓
Versioning + Provenance
        ↓
Access expiry
```

## Identity disablement → Access revocation

```text
Identity.disable
        ↓
active Access contexts revoked/denied
```

Historical Participation and authorship remain intact.

---

# 30. Access versus policy

002-B deliberately does not hard-code all permissions into Access.

Access answers whether a capability is currently permitted using policy supplied by the application.

Examples of later policy inputs include:

```text
Can a Judge self-reopen a finalized Scorecard during Active judging?

Does paper capture require verification by a second Organizer?

Can one person hold Organizer and Judge Participation simultaneously?

Which Organizer roles may view private Notes?

What constitutes valid post-finalization correction authority?
```

These may evolve without changing the purpose of Access.

---

# 31. Access failure behavior

An Access denial should be safe and non-destructive.

A denied action must not partially mutate the protected resource.

The user-facing experience should distinguish where useful between:

```text
not permitted
access expired
re-verification required
resource no longer editable
Competition state no longer permits action
```

without leaking protected information.

For example, a Judge following a stale Scorecard URL after Event Completed should not receive sensitive Scorecard content before the system reports that judging access has ended.

---

# 32. Privacy-oriented data minimization

002-B reinforces a broader design principle:

> Identity and Participation should store only information necessary for competition operation, verification, attribution, and legitimate future recognition.

The application should not accumulate extensive permanent Judge profiles merely because returning recognition is useful.

Likewise, Judge historical access is not justified solely by data retention.

Retention and access remain separate concerns.

---

# 33. Core 002-B invariants

1. Identity answers human continuity, not Competition role.
2. Participation answers scoped role, not authentication mechanism.
3. Access answers capability/disclosure, not historical identity.
4. Judge and Organizer are Participation roles.
5. Administrator is primarily a system authority role.
6. A returning Judge receives a new Competition Participation.
7. Returning recognition never automatically restores prior authority.
8. Expertise is Judge Participation state and may be plural.
9. Expertise never independently grants capability.
10. One Identity may hold multiple Participations where Competition policy permits.
11. Dual-role capabilities remain separable by Participation context.
12. Identity alone never grants sensitive Competition Access.
13. Participation role alone is not sufficient for every authorization decision.
14. Access decisions may depend on Competition state, resource ownership, scope, purpose, and time.
15. Judge ordinary access is limited to their own evaluation content and relevant operational context.
16. Judges do not receive peer evaluations, Team aggregates, Rankings, or standings by default.
17. Judges do not receive administrative Team identity by default.
18. Event Completed ends ordinary Judge access to private Scorecards, Notes, and judging history.
19. Access expiry never deletes historical records.
20. Post-event Judge correction uses temporary, narrow, reverified Access.
21. Temporary correction Access does not restore broad historical browsing.
22. Organizer access to Judge evaluation does not transfer evaluation authorship.
23. Administrator technical authority does not automatically confer Competition decision authority.
24. Break-glass technical access is exceptional, bounded, and attributable.
25. Shared-device transitions must not expose the previous Judge's private evaluation state.
26. Lost-device recovery revokes the compromised session rather than creating a duplicate Judge identity or Participation.
27. Stale sessions cannot override expired Access.
28. Historical Scorecard authorship resolves through Judge Participation to Identity.
29. Disabled Identity does not erase historical authorship.
30. Access denial must not partially mutate protected state.

---

# 34. Questions deferred to later groups

002-B intentionally defers:

- exact authentication mechanism;
- exact identity fields and verification handles;
- session duration and refresh strategy;
- precise Organizer sub-roles/delegation model;
- exact post-finalization correction approval chain;
- whether Judge self-amendment requires Organizer approval while Active;
- whether paper capture requires two-person verification;
- exact record retention period;
- local/offline encryption and clearing mechanics;
- exact AWS identity/authorization services;
- whether returning Judge recognition is opt-in or automatic;
- exact privacy policy wording and consent notices.

These are not blockers to the behavioral specification.

---

# 35. Handoff to 002-C

002-C can now treat Judge Participation as the stable human reference for Panel membership and Encounter participation.

The key contracts provided to 002-C are:

```text
Judge Participation
    has Competition scope
    has lifecycle state
    may carry multiple Expertise values
    becomes operationally eligible through Participation + Access policy

Panel
    should reference Judge Participation
    not a permanent global Judge user

Encounter participant snapshot
    should reference the Judge Participations
    who actually participated
```

002-C must define how Panel membership is formed, changed, and historically separated from Encounter participation.

---

# 002-B Exit Position

002-B confirms that MUDAC should not use a simplistic authorization model such as:

```text
user.role == "judge"
```

as the conceptual source of truth.

The actual model is:

```text
IDENTITY
    │
    │ who
    ▼
PARTICIPATION
    │
    │ why / capacity / Competition
    ▼
ACCESS
    │
    │ capability + resource + state + time
    ▼
ACTION OR DISCLOSURE
```

For a Judge:

```text
Identity J-12
    ↓
Competition 2026 Judge Participation
    ↓
Active-event Access
    ↓
own Scorecards / own Notes / relevant Team Alias
```

and at Event Completed:

```text
same Identity
same historical Participation
same authoritative Scorecards
        ↓
ordinary private-data Access expires
```

That separation allows the system to support first-time volunteers, returning volunteers, dual-role people, shared devices, device loss, historical attribution, and post-event correction without giving Judges permanent access to sensitive evaluation records or turning technical Administrators into Competition authorities.

No additional Concept is required by 002-B.
