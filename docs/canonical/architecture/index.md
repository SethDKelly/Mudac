# Architecture

Current accepted MUDAC system/application architecture contracts and decisions.

Architecture remains downstream of canonical product, UX, invariant, policy, and governance knowledge. Architecture owners describe how those upstream contracts are realized; they do not redefine product meaning for implementation convenience.

# Current architecture

* [Architectural Foundation, Quality Attributes & Trust Boundaries](architectural-foundation.md) — `ARCH-*` architecture-wide constraints for authoritative transitions, client/local state, projections, attribution, retry/failure behavior, disclosure enforcement, freshness/uncertainty, trust boundaries, and architecture decision quality.
* [Application Boundaries, Modules & Dependency Architecture](application-boundaries.md) — `MOD-*` ownership/dependency contracts; six authoritative semantic modules, non-authoritative projection/query composition, thin cross-module coordination, and modular-monolith-first deployment posture.
* [Data, Persistence, Versioning, Provenance & Projection Architecture](data-persistence.md) — `DATA-*` persistence contracts; one PostgreSQL-compatible relational authority store with module-owned namespaces, stable IDs, append-stable Versions/Provenance, reconstructible derived state, rebuildable projections, and transactional change propagation without primary event sourcing.
* [Identity, Authentication, Access & Session Architecture](identity-access-session.md) — `AUTH-*` identity/security contracts; provider-backed authentication mapped to stable MUDAC Identity, explicit Participation context, contextual Access, opaque first-party server sessions, event-completion expiry, role-context isolation, revocation, narrow correction grants, and break-glass separation.
* [Commands, Queries, API, Transaction & Concurrency Architecture](commands-api-concurrency.md) — `API-*` request/transaction contracts; HTTPS/JSON command-query separation, current-context authorization, confirmed-after-commit semantics, optimistic concurrency, targeted locking/isolation, durable idempotency, lost-response recovery, and explicit projection freshness.
* [Draft Synchronization, Offline & Recovery Architecture](synchronization-recovery.md) — `SYNC-*` continuity contracts; bounded local Draft persistence, revision-aware synchronization, conflict preservation, online-only authoritative transitions, reconnect/Access revalidation, truthful sync state, and paper/electronic convergence.
* [External Representation, Artifact & Publication Architecture](external-representation.md) — `REP-*` externalization contracts; paper-source/capture authority boundaries, exact source/disclosure binding, immutable artifact bytes and digests, object-storage separation, idempotent generation, validation, explicit publication, supersession, and end-to-end representation provenance.
* [Front-End State, Navigation & Interaction Architecture](frontend-interaction.md) — `FE-*` browser contracts; React/TypeScript baseline, React Router route boundaries, TanStack Query remote cache, IndexedDB Draft continuity, explicit role/context and command states, accessible component layering, phone-primary Judge interaction, exception-first Organizer responsiveness, and failure/recovery containment.

# Planned architecture areas

Phase 005 will add the accepted AWS/runtime/operations owner here when 005-I becomes stable.

# Authority rule

Accepted architecture documents are current owners for architecture meaning in this subtree while numbered Phase 005 records preserve alternatives, rationale, tradeoffs, and decision lineage.

Architecture must cite task-relevant upstream stable rules and state local consequences rather than recreating complete upstream rule bodies. Knowledge topology does not dictate source-code topology.