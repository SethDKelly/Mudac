---
type: Design Phase Record
title: 005-A — Architectural Drivers, Quality Attributes, Trust Boundaries & Decision Principles
description: Establishes the architecture-wide drivers, trust model, quality-attribute priorities, failure posture, and decision criteria that constrain all later MUDAC system/application architecture choices.
status: stable
tags: [phase-005, architecture, quality-attributes, trust-boundaries, security, resilience]
sources:
  - resource: ../004-knowledge-architecture/004-J-phase-004-consolidation-knowledge-architecture-exit-review.md
  - resource: ../canonical/invariants/judge-independence.md
  - resource: ../canonical/invariants/one-logical-scorecard.md
  - resource: ../canonical/invariants/organizer-not-judge-author.md
  - resource: ../canonical/invariants/accessibility-semantic-parity.md
  - resource: ../canonical/invariants/truthful-authority-under-uncertainty.md
  - resource: ../canonical/concepts/access.md
  - resource: ../canonical/policies/anonymity-disclosure.md
  - resource: ../canonical/policies/continuity-paper.md
generated: { by: openai/gpt-5.6-sol, at: 2026-09-04T04:09:23Z }
---

# Purpose

005-A establishes the architecture-wide constraints that later Phase 005 groups must satisfy before MUDAC selects concrete implementation mechanisms.

The governing question is:

> What properties must the MUDAC architecture preserve across normal operation, event-day load, failures, stale state, device changes, paper fallback, security boundaries, and future implementation evolution so that technology cannot accidentally change Competition meaning or authority?

This subgroup does **not** select frameworks, databases, authentication providers, API styles, synchronization libraries, queues, artifact technologies, or AWS services.

Its output is the canonical [Architectural Foundation](../canonical/architecture/architectural-foundation.md).

# 1. Upstream authority

Architecture is downstream of current canonical product, UX, and governance knowledge.

The most architecture-sensitive upstream contracts include:

- [DOC-003](../canonical/governance/documentation-authority.md#doc-003) — architecture cannot override upstream canonical meaning;
- [INV-001](../canonical/invariants/judge-independence.md#inv-001) — Judge independence and non-disclosure of peer/results signals;
- [INV-002](../canonical/invariants/one-logical-scorecard.md#inv-002) — one logical Scorecard per Judge × Encounter across retry/device/paper/amendment paths;
- [INV-004](../canonical/invariants/organizer-not-judge-author.md#inv-004) — technical/process/capture authority cannot become Judge authorship;
- [INV-009](../canonical/invariants/accessibility-semantic-parity.md#inv-009) — accessibility changes interaction mechanics, not semantics;
- [INV-010](../canonical/invariants/truthful-authority-under-uncertainty.md#inv-010) — uncertain persistence/authority cannot be represented as confirmed success;
- [ACC-001](../canonical/concepts/access.md#acc-001) and [ACC-002](../canonical/concepts/access.md#acc-002) — Access is contextual and does not transfer semantic authority;
- [DISC-001](../canonical/policies/anonymity-disclosure.md#disc-001) and [DISC-002](../canonical/policies/anonymity-disclosure.md#disc-002) — blinded Team identity and purpose-specific disclosure;
- [Continuity & Paper](../canonical/policies/continuity-paper.md) — degraded operation preserves the same evaluation model.

The architecture must also preserve the established lifecycle, Versioning/Provenance, Coverage/Aggregate/Rank, official-outcome, publication, and recovery contracts through the relevant canonical owners as later subgroups touch those concerns.

# 2. Architectural drivers

## 2.1 Live-event correctness under bursty human activity

MUDAC is not a generic content application. Its highest-consequence writes occur during a bounded live event in which many Judges may save/finalize near the same presentation boundaries while Organizers simultaneously manage Panel/Encounter exceptions.

Architecture therefore optimizes for **correct bounded-event concurrency**, not arbitrary internet-scale throughput.

The system must tolerate concentrated bursts without turning contention into duplicate logical Scorecards, lost drafts, stale destructive updates, or falsely confirmed Finalization.

Numeric load/SLO targets are intentionally deferred until Phase 005 has an explicit workload model. 005-A rejects invented scale targets that would prematurely bias service/database choices.

## 2.2 Authority-sensitive state transitions

Several operations change authoritative state and have materially different consequences from ordinary Draft work:

- Scorecard Finalization and amendment Finalization;
- Competition activation, Event Completion, resume, and Finalization;
- Encounter invalidation/replacement;
- Coverage exceptions;
- official-outcome successor confirmation;
- public publication/republication.

These cannot be modeled as optimistic UI events that merely *eventually* become true. The architecture must establish an authoritative boundary where current state, actor Access, preconditions, idempotency, and concurrency are validated before success is confirmed.

## 2.3 Mobile-primary Judge operation

Judge operation is phone-primary and frequently interrupted. Device/browser state is therefore transient working context, not the durable identity of the evaluation.

A change of tab, browser process, phone, network, or interaction modality must not create a second logical Judge/Encounter evaluation.

## 2.4 Organizer exception-heavy operation

Organizer architecture must support live operational awareness, not merely CRUD over domain objects.

Read-heavy operational projections may summarize Judge readiness, Panel composition, Encounter obligations, paper capture, Coverage, or reconciliation state. Those projections may be eventually refreshed where safe, but they cannot silently become the authoritative source for high-consequence writes.

## 2.5 Controlled disclosure and fairness

Security architecture is not only about authentication. It must preserve purpose-specific disclosure and Judge independence across:

- interactive views;
- APIs;
- search/autocomplete;
- cached/local state;
- logs/telemetry;
- exports and filenames/metadata;
- print and publication;
- administrative tooling.

A front-end-hidden field is not considered protected merely because the UI does not render it.

## 2.6 Traceability and historical reconstruction

MUDAC's official results must remain explainable from authoritative evidence and policy. Architecture must therefore preserve stable identity, immutable/reconstructible committed versions where required, actor/author/authorizer attribution, correction lineage, and the ability to distinguish current authority from historical observed state.

## 2.7 Degraded operation and physical continuity

Digital availability is valuable, but false authority is worse than a temporarily unavailable digital action.

When digital authority cannot be trusted, MUDAC may degrade to paper under the existing Continuity/Paper contract. Recovery converges physical/electronic traces back to the same logical evaluations instead of inventing an independent offline authority model.

## 2.8 Accessibility and device independence

Architecture must not require a specific device capability, camera/QR, fine pointer, orientation, or visual-only representation to perform a core operation. Accessible alternatives share the same command/authority paths wherever possible rather than creating weaker side channels.

## 2.9 Operational simplicity and evolvability

The architecture should remain understandable and operable by a modest project/team footprint. Complexity must be justified by a concrete driver, failure mode, or quality requirement.

Future replacement of UI, identity provider, persistence implementation, deployment service, or projection mechanism should be possible without redefining canonical product meaning.

# 3. Quality-attribute priority model

005-A uses three tiers rather than a single total ordering because several concerns are simultaneously non-negotiable.

## Tier 1 — Semantic and trust integrity

These may not be traded away for speed, convenience, or apparent availability:

1. **Domain/authority correctness** — state transitions preserve canonical semantics and preconditions.
2. **Security/privacy/fairness** — Access and disclosure remain contextual; Judge independence is preserved.
3. **Evidence traceability/auditability** — authoritative history, attribution, version basis, and outcome derivation remain reconstructible.
4. **Truthful consistency** — uncertainty/staleness is surfaced instead of promoted into confirmed authority.

## Tier 2 — Event-critical usability and continuity

These must be strong enough that the live competition can operate effectively:

1. **Resilience/continuity** — recoverable drafts, safe retries, device replacement, controlled degraded operation, and paper fallback.
2. **Responsiveness** — ordinary Judge/Organizer interactions should remain fast under expected event bursts; long-running work should not block unrelated judging.
3. **Accessibility/device independence** — equivalent semantics across phone, keyboard/nonvisual interaction, narrow/wide layout, and legitimate accommodations.
4. **Availability** — digital services should be highly available during the event, but authority-sensitive operations fail safely rather than fabricate success.

## Tier 3 — Sustaining architecture quality

These shape implementation choices after Tier 1/2 requirements are satisfied:

1. **Maintainability/modularity** — clear ownership and dependency direction; change localized to appropriate boundaries.
2. **Observability/operability** — failures and authority uncertainty diagnosable without leaking sensitive evidence.
3. **Recoverability** — backups/restores and operational recovery preserve identity/version/authority semantics.
4. **Cost proportionality** — infrastructure complexity and spend should match event scale and reliability needs.
5. **Reversibility/evolvability** — avoid needless lock-in where a simpler boundary can preserve options.

# 4. Tradeoff rules

The quality model implies several explicit tradeoffs.

## 4.1 Correctness over false availability

For authoritative transitions:

```text
confirmed correct state
    >
apparent success with unknown authority
```

A timeout after a Finalize request may produce an **unknown confirmation state** and a safe status/retry path. It must not produce a second Scorecard or a fabricated success response.

## 4.2 Event continuity over digital feature completeness

If authoritative digital operation is unavailable:

```text
identified paper fallback
    >
unsafe local authority simulation
```

The event can continue with reduced digital capability while preserving the same evaluation model.

## 4.3 Privacy/fairness over convenient broad caching

Client caches, logs, read models, or exports must not retain or distribute information beyond their authorized purpose merely because broad caching simplifies implementation.

## 4.4 Simplicity over speculative scale

MUDAC should not adopt distributed complexity for hypothetical global scale before event workload evidence requires it.

The architecture should nevertheless maintain clean boundaries so later scaling mechanisms can be introduced without changing product semantics.

# 5. Trust-boundary model

A trust boundary is an architectural crossing where identity, authority, confidentiality, integrity, freshness, or provenance must be re-established rather than assumed.

| Boundary | What crosses it | Required posture |
| --- | --- | --- |
| Human ↔ device/browser | credentials/session, draft input, displayed state | Device is not principal or authority; protect private state; support replacement/shared-device recovery. |
| Client ↔ application authority | commands, queries, session context | Authenticate where required; authorize contextually; validate command preconditions server-side; never trust hidden client fields. |
| Identity/authentication ↔ Participation/Access | established principal claims | Authentication answers who; MUDAC Participation/Access still determines competition-scoped capability. |
| Application command ↔ authoritative persistence | intended state transition | Enforce current-state/precondition/concurrency/idempotency rules before confirming success. |
| Authoritative state ↔ read projection/cache | events/state transformed for reads | Projection may be stale; label/refresh as needed; never use stale projection as sole authority for consequential writes. |
| Judge semantic authorship ↔ Organizer/admin process authority | capture, correction, invalidation, support actions | Preserve actor/author/authorizer distinctions; process authority does not become Judge judgment. |
| Internal state ↔ external artifact/publication | exports, print, ceremony/public data | Apply audience/purpose disclosure; bind artifact to identified source/revision; publication is explicit. |
| Physical paper ↔ digital authoritative record | identified physical evaluation evidence | Verify source/context; preserve Judge author and capture actor; converge with any existing electronic trace. |
| Application ↔ external provider | identity, messaging, future managed services | Treat provider assertions/failures as bounded inputs; do not outsource MUDAC semantic authority accidentally. |
| Runtime/operator ↔ application/data plane | deployment, support, break-glass operations | Least privilege, audited exceptional access, no default product authority merely from infrastructure administration. |

# 6. Architecture foundation rules

005-A promotes the following architecture-wide rules to the canonical architecture foundation.

## ARCH-001 — Upstream canonical semantics constrain architecture

Every architecture decision must identify and satisfy the relevant canonical product/UX/governance contracts. Architecture is not an alternative place to redefine them.

## ARCH-002 — Authoritative transitions are validated and confirmed at the authoritative boundary

A client request does not make a transition true. Current state, Access, command preconditions, concurrency, and idempotency must be checked by the authoritative application/persistence path before authoritative success is reported.

## ARCH-003 — Client/device/local state is never the final authority

Browser/device/local storage may preserve working state and improve resilience, but device possession/cache state does not establish Identity, Access, Finalization, official outcome, or publication authority.

## ARCH-004 — Derived projections are not write authority

Read models, dashboards, aggregates, indexes, caches, and search projections may accelerate/compose reads. High-consequence commands must revalidate against authoritative state rather than relying solely on a potentially stale projection.

## ARCH-005 — Actor, author, authorizer, and capture attribution survive architectural boundaries

Authentication, service boundaries, queues, persistence, paper capture, and admin tooling must preserve the semantic distinction between who performed a technical action and whose authority/intent the domain state represents.

## ARCH-006 — Failure and retry paths preserve logical identity and evidence

Retries, ambiguous responses, device replacement, concurrency, paper fallback, and recovery must converge on existing logical resources rather than creating extra evaluation weight or silently overwriting newer authority.

## ARCH-007 — Security and disclosure are enforced beyond presentation code

Sensitive/hidden information must be protected at appropriate application/data/export/operational boundaries, not merely omitted from rendered UI. Purpose-specific disclosure applies to APIs, search, cache, telemetry, artifacts, and operator tools.

## ARCH-008 — Architecture must expose meaningful freshness and uncertainty

Where reads, projections, caches, or disconnected working state may be stale or unconfirmed, the architecture must retain enough freshness/version/confirmation information for UX and commands to distinguish confirmed authority from uncertain local observation.

# 7. Architecture decision rubric for later groups

Each later Phase 005 decision should answer, proportionally to consequence:

1. **Upstream contracts** — Which stable rules/canonical owners constrain this decision?
2. **Problem and assumptions** — What concrete workload/failure/security problem is being solved? Which assumptions remain unverified?
3. **Alternatives** — What materially different mechanisms were considered?
4. **Authority/trust impact** — Where does authority live? Which trust boundaries are crossed?
5. **Failure behavior** — What happens on timeout, retry, stale state, duplicate request, provider failure, and partial outage?
6. **Privacy/disclosure impact** — What sensitive data crosses/stays within the boundary?
7. **Accessibility/continuity impact** — Does the option preserve alternate interaction and degraded modes?
8. **Operability** — Can support/observability diagnose problems without silently increasing product authority or leaking evidence?
9. **Complexity/cost** — Is the operational complexity justified by a real driver?
10. **Reversibility** — What future choices does this lock in, and is that lock-in necessary?
11. **Canonicalization** — Once accepted/stable, what current architecture owner should represent the decision?

A design option that cannot explain how it satisfies its relevant upstream contracts is not ready for acceptance.

# 8. Quality-attribute scenarios

These scenarios provide architecture tests without prematurely selecting technologies.

## QA-01 — Judge Finalization under response loss

A Judge Finalize request reaches the server but the network response is lost.

Required outcome:

- the logical Scorecard is not duplicated;
- retry is safe/convergent;
- the client can learn whether Finalization actually occurred;
- the UX never promotes uncertainty into a fabricated success;
- current authoritative Version remains reconstructible.

Relevant rules: [INV-002](../canonical/invariants/one-logical-scorecard.md#inv-002), [INV-010](../canonical/invariants/truthful-authority-under-uncertainty.md#inv-010), `ARCH-002`, `ARCH-006`, `ARCH-008`.

## QA-02 — Organizer acts from stale operational projection

An Organizer has an open reconciliation/live-ops view while another Organizer or Judge changes relevant authoritative state.

Required outcome:

- stale reads may be detected/refreshed;
- a consequential command revalidates authoritative preconditions;
- newer state is not silently overwritten;
- the rejected/conflicting action provides recoverable domain-oriented feedback.

## QA-03 — Judge changes device mid-Draft

A Judge loses access to the original phone and re-establishes identity on another device.

Required outcome:

- the same Competition Participation and Scorecard logical identity are recovered;
- no second vote is created;
- prior private state is not leaked on a shared/replaced device;
- only durably preserved state is represented as confirmed.

## QA-04 — Full digital degradation during judging

The event cannot safely use digital authority for a period.

Required outcome:

- Judges can continue with identified paper forms where operational policy permits;
- paper retains the exact Rubric/context semantics;
- later capture preserves Judge authorship and Organizer capture attribution;
- electronic/paper traces for the same Judge × Encounter reconcile to one logical Scorecard.

## QA-05 — Public artifact after official correction

An already-published artifact represents Official Outcome Revision 1; a legitimate correction produces successor Revision 2.

Required outcome:

- Revision 1 remains historically traceable;
- current publication state can identify the stale/affected artifact;
- generating/publishing a replacement does not silently rewrite the historical artifact;
- disclosure rules remain applied to the replacement.

## QA-06 — Peak event save/finalize burst

Many Judges save/finalize around the end of simultaneous presentation blocks.

Required outcome:

- normal Draft work remains responsive enough for event use;
- contention is scoped to the relevant logical resources rather than globally serializing unrelated judges;
- authoritative writes retain correctness/idempotency;
- overload does not produce duplicate votes or false success.

Numeric latency/throughput budgets are deferred until the workload assumptions are defined and measurable.

## QA-07 — Accessible alternate interaction

A Judge uses keyboard/nonvisual interaction or a non-camera entry path.

Required outcome:

- the same Identity/Participation/Access and Scorecard command paths are used;
- no accessibility-specific path weakens confirmation, privacy, or evidence semantics;
- disclosure and authorship remain unchanged.

# 9. Security posture

005-A establishes architecture-level security principles without selecting authentication/security products.

1. **Least privilege and contextual authorization** — enforce current Competition/resource relationship, not merely global role.
2. **Server-side consequential authorization** — client routing/hidden controls are usability aids, not the enforcement boundary.
3. **Data minimization by purpose** — read models, exports, logs, and caches contain no broader sensitive fields than their function requires.
4. **Separation of product and operator authority** — infrastructure administration does not automatically confer Judge/Organizer product authority.
5. **Auditable exceptional paths** — break-glass/support operations that cross ordinary boundaries are explicit and reconstructible.
6. **No secret-by-obscurity identity model** — Team Alias/QR/deep-link identifiers are not authentication credentials merely because they are difficult to guess.
7. **Sensitive telemetry discipline** — diagnostic observability must avoid leaking Judge Notes, hidden Team identity, credentials, or raw private evidence by default.

Detailed authentication/session/credential architecture is deferred to 005-D; runtime/network/security-service choices are deferred to 005-I.

# 10. Consistency posture

005-A does not yet prescribe a database consistency model. It does prescribe where stronger semantics are required.

## Strong/authoritative precondition domain

Consequential transitions require current authoritative validation for their affected logical resource and relevant policy/access state.

Examples include Scorecard Finalization, Encounter invalidation, Coverage exception acceptance, Competition Finalization, and publication.

## Potentially eventually refreshed read domain

Operational dashboards, search indexes, aggregate summaries, and other derived views may use projection/caching models appropriate to later design if:

- staleness is bounded/visible where meaningful;
- source authority remains identifiable;
- commands do not trust stale projection state as final authority;
- downstream official calculations retain reconstructible source basis.

This separation is intentional and will guide 005-C through 005-F.

# 11. Availability and recovery posture

Availability requirements differ by function.

## Draft work

Architecture should prioritize preservation and resumption. Later 005-F will determine how much disconnected/local continuation is justified and safe.

## Authoritative transitions

Prefer safely unavailable/unknown over falsely successful. Retries must be idempotent or otherwise converge on one logical result.

## Live-event continuity

Paper provides the established semantic fallback when digital authority is unavailable. Digital architecture therefore need not invent a fully autonomous offline authority system merely to claim continuous availability.

## Publication/external artifacts

Publication failures are isolated from Competition Finalization authority; an official outcome can exist while publication is pending/failed.

# 12. Performance and scale posture

The expected workload is event-shaped rather than continuously high-volume:

- many low-cost Judge Draft writes;
- concentrated Finalization bursts;
- Organizer exception/read activity;
- periodic aggregation/reconciliation computation;
- relatively low-frequency artifact/publication operations.

005-A therefore rejects both extremes:

- **under-designing** authority-sensitive concurrency because the user population is modest; and
- **over-designing** for speculative global scale with distributed systems complexity not justified by the event model.

Later groups should establish explicit scale assumptions and measurable targets before using performance as justification for a complex architecture.

# 13. Observability posture

Observability must support both operational health and domain-level investigation.

Future architecture should make it possible to answer questions such as:

- Did a Finalize request reach authoritative processing?
- Was it rejected for Access/precondition/conflict, or did confirmation fail afterward?
- Which logical Scorecard/Encounter was involved without exposing private Note content?
- Is a read model stale relative to its source?
- Was a paper/electronic duplicate prevented/reconciled?
- Which official revision/artifact was generated/published?

Detailed telemetry schema/tooling is deferred to 005-I.

# 14. Architecture decisions intentionally deferred

005-A does not decide:

- modular monolith versus multiple deployable services;
- domain-module/package boundaries;
- relational/document/event-store persistence;
- database vendor;
- event sourcing/CQRS implementation;
- authentication/identity provider;
- API protocol/style;
- queue/event bus;
- local/offline storage implementation;
- synchronization/conflict algorithm;
- front-end framework/component library;
- artifact/PDF generation stack;
- cache/search technology;
- container/serverless/runtime model;
- concrete AWS services;
- monitoring/logging vendor.

These remain downstream because their evaluation requires the architecture foundation established here plus the narrower context of the corresponding subgroup.

# 15. 005-A exit criteria

005-A is complete when:

1. architecture is explicitly subordinate to canonical product/UX/governance authority;
2. major event/application drivers are identified without inventing technology;
3. quality attributes have a usable priority/tradeoff model;
4. trust boundaries identify where identity/authority/confidentiality/freshness must be re-established;
5. authoritative versus projection/local-state semantics are separated;
6. failure/availability posture preserves `INV-002`, `INV-004`, and `INV-010`;
7. accessibility and paper continuity remain architecture requirements, not UI-only concerns;
8. later architecture groups have a common decision rubric;
9. high-value architecture-wide rules have stable canonical IDs;
10. no framework/database/auth/AWS decision has been prematurely locked.

All ten criteria are satisfied by this subgroup and its canonical architecture owner.

# 16. Handoff to 005-B

005-B may now define **Application Boundaries, Modules, Domain Services & Dependency Architecture** under the foundation established here.

Its central problem is not which framework folders to create. It is which semantic responsibilities belong together, which dependencies are allowed, where authoritative commands and derived projections live, and how to prevent convenience coupling from crossing trust/authority boundaries.

The architecture foundation remains upstream of those module decisions.