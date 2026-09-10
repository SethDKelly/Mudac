# Canonical MUDAC Knowledge

This subtree is the preferred source for current MUDAC product, conceptual UX, documentation-governance, accepted architecture, and accepted implementation meaning.

# Current Knowledge

* [Concepts](concepts/) — accepted MUDAC Concepts.
* [Synchronizations](synchronizations/) — current cross-concept trigger, authority, precondition/postcondition, failure/retry, and temporal/history coordination contracts.
* [Mechanisms](mechanisms/) — derived/supporting subjects that intentionally remain non-Concepts.
* [Policies](policies/) — governing/configurable Competition semantics, including [Operational Exception & Override Governance](policies/operational-exception-governance.md) for cross-cutting exception/override boundaries.
* [Invariants](invariants/) — cross-cutting normative constraints.
* [Experience](experience/) — current conceptual UX contracts, including [Experience Action, State & Authority Traceability](experience/action-authority-traceability.md) for consequential interaction-to-domain ownership.

# Governance, Architecture and Implementation

* [Governance](governance/) — methodology/terminology, documentation authority, agent context, canonical change, metadata/trust/lifecycle, validation/CI, source lineage, stable rule IDs, and the current [Design / Implementation Boundary](governance/design-implementation-boundary.md).
* [Architecture](architecture/) — current accepted system/application architecture contracts. Knowledge topology does not dictate source-code topology.
* [Implementation](implementation/) — accepted implementation/tooling contracts plus the protected 006-D non-domain bootstrap baseline. Implementation planning may now resume, but new domain implementation remains not started pending Phase 008 plan refresh and first-slice authorization.

# Current delivery posture

MUDAC has formally exited the renewed Jackson Concept Design methodology for the current accepted baseline.

Phase 007 is complete. 007-H found no known unresolved baseline semantic/design blocker; 007-I formally accepted that evidence and made the methodology-exit decision.

The current boundary is:

```text
Jackson Concept Design methodology: COMPLETE / EXITED
baseline semantic design: COMPLETE
known baseline semantic blockers: NONE OPEN
implementation planning: READY TO RESUME
Phase 008 plan refresh: NEXT / NOT STARTED
new domain implementation after 006-D: NOT STARTED
production readiness: NOT ESTABLISHED
```

The retained 006-D executable substrate is a protected non-domain implementation baseline. The old 006-E through 006-M sequence remains historical planning lineage and is superseded as the active execution queue.

Current work should proceed through **Phase 008 — Implementation Re-entry, Plan Refresh & Execution Readiness**, beginning by defining dependency-safe subgroups before any new domain implementation is authorized.

# Retrieval Rule

Load only the specific owner documents and linked dependencies required by the task. For behavior spanning more than one Concept, prefer the relevant [Synchronization](synchronizations/) owner rather than reconstructing coordination from scattered phase history. Use stable rule IDs for normative cross-reference and phase history only when rationale/chronology is needed.

For correction/current-vs-historical/invalidation/official-outcome/Publication-timeline questions, also load [Temporal Truth, Correction & Historical Authority](synchronizations/temporal-truth-correction.md).

For Judge/Organizer interaction, route, action visibility, status/exception, confirmation, recovery, or UI-authority design, load [Experience Action, State & Authority Traceability](experience/action-authority-traceability.md) plus only the relevant experience owner(s).

For exception, waiver, override, acknowledgement/suppression, policy bypass, or technical-emergency-versus-semantic-authority questions, load [Operational Exception & Override Governance](policies/operational-exception-governance.md) plus the specific policy/Concept owner involved.

For external representation/publication questions, preserve the chain from source authority through [Export](concepts/export.md) to [Publication](concepts/publication.md); a representation may not promote its source authority and official-result Publication must bind to an identified Official Outcome Revision.

Before any implementation/code/IaC work, load [Design / Implementation Boundary](governance/design-implementation-boundary.md). During Phase 008, implementation work is limited to planning/re-entry plus narrow maintenance of the protected 006-D baseline until an explicit first domain implementation slice is authorized.

Passing repository checks is evidence for a tested revision, not semantic verification, implementation correctness, authority to skip the plan-refresh boundary, or production certification.