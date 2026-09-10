# Canonical MUDAC Knowledge

This subtree is the preferred source for current MUDAC product, conceptual UX, documentation-governance, accepted architecture, and accepted implementation meaning.

# Current Knowledge

* [Concepts](concepts/) — accepted MUDAC Concepts.
* [Synchronizations](synchronizations/) — current cross-concept trigger, authority, precondition/postcondition, failure/retry, and temporal/history coordination contracts.
* [Mechanisms](mechanisms/) — derived/supporting subjects that intentionally remain non-Concepts.
* [Policies](policies/) — governing/configurable Competition semantics, including [Operational Exception & Override Governance](policies/operational-exception-governance.md).
* [Invariants](invariants/) — cross-cutting normative constraints.
* [Experience](experience/) — current conceptual UX contracts, including [Experience Action, State & Authority Traceability](experience/action-authority-traceability.md).

# Governance, Architecture and Implementation

* [Governance](governance/) — methodology/terminology, documentation authority, agent context, canonical change, metadata/trust/lifecycle, validation/CI, source lineage, stable rule IDs, and the current [Design / Implementation Boundary](governance/design-implementation-boundary.md).
* [Architecture](architecture/) — current accepted system/application architecture contracts. Knowledge topology does not dictate source-code topology.
* [Implementation](implementation/) — accepted implementation/tooling contracts, the **qualified protected 006-D non-domain bootstrap**, and the accepted 008-D persistence/history implementation contract.

# Current delivery posture

MUDAC has formally exited the renewed Jackson Concept Design methodology for the current accepted baseline.

Phase 008 implementation planning is active. [008-A](../008-implementation-reentry/008-A-implementation-reentry-authority-canonical-baseline-change-control-planning-guardrails.md) established planning authority, [008-B](../008-implementation-reentry/008-B-protected-006-D-baseline-qualification-drift-audit-toolchain-environment-reconciliation.md) qualified the retained 006-D substrate, [008-C](../008-implementation-reentry/008-C-residual-risk-ingestion-historical-006-mapping-decision-register-supersession-matrix.md) reconciled residual/historical ownership, and [008-D](../008-implementation-reentry/008-D-persistence-temporal-truth-versioning-provenance-governed-exceptions-outbox-projection-migration-implementation-plan.md) accepted the physical persistence/history implementation plan.

The current boundary is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
implementation planning authority: ESTABLISHED
008-A: COMPLETE
008-B: COMPLETE — PASS AFTER NARROW REMEDIATION
008-C: COMPLETE — PASS
008-D: COMPLETE — PASS
protected 006-D baseline: QUALIFIED FOR PHASE 008 PLANNING
persistence/history implementation plan: ACCEPTED / NOT IMPLEMENTED
008-E: NEXT / NOT STARTED
first executable domain slice: NOT YET AUTHORIZED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

Durable 008-D implementation meaning is owned by [Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract](implementation/persistence-history-projection.md). The phase record preserves rationale and local decisions; it is not a parallel canonical rule store.

All 007-H Class 4 future-scope items remain outside the current baseline unless deliberate `CHG-*` work reopens them.

# Retrieval Rule

Load only the specific owner documents and linked dependencies required by the task. For behavior spanning more than one Concept, prefer the relevant [Synchronization](synchronizations/) owner rather than reconstructing coordination from scattered phase history. Use stable rule IDs for normative cross-reference and phase history only when rationale/chronology is needed.

For correction/current-vs-historical/invalidation/official-outcome/Publication-timeline questions, also load [Temporal Truth, Correction & Historical Authority](synchronizations/temporal-truth-correction.md).

For Judge/Organizer interaction, route, action visibility, status/exception, confirmation, recovery, or UI-authority design, load [Experience Action, State & Authority Traceability](experience/action-authority-traceability.md) plus only the relevant experience owner(s).

For exception, waiver, override, acknowledgement/suppression, policy bypass, or technical-emergency-versus-semantic-authority questions, load [Operational Exception & Override Governance](policies/operational-exception-governance.md) plus the specific policy/Concept owner involved.

For persistence/history/outbox/projection/migration planning or implementation, load [Persistence, History, Provenance, Outbox, Projection & Migration Implementation Contract](implementation/persistence-history-projection.md) plus the task-relevant upstream semantic/architecture owner.

For external representation/publication questions, preserve the chain from source authority through [Export](concepts/export.md) to [Publication](concepts/publication.md); a representation may not promote its source authority.

Before any implementation/code/IaC work, load [Design / Implementation Boundary](governance/design-implementation-boundary.md). During Phase 008, work remains planning/re-entry plus narrow maintenance of the qualified protected baseline until 008-L explicitly authorizes a first domain implementation slice.

The next planning subgroup is **008-E — Identity, Authentication, Participation, Access, Session, Invitation, Secrets & Technical-Authority Implementation Plan**.

Passing repository checks is evidence for a tested revision, not semantic verification, implementation correctness, executable-slice authorization, deployment authority, or production certification.
