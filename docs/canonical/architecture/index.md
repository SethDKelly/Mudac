# Architecture

Current accepted MUDAC system/application architecture contracts and decisions.

Architecture remains downstream of canonical product, UX, invariant, policy, and governance knowledge. Architecture owners describe how those upstream contracts are realized; they do not redefine product meaning for implementation convenience.

# Current architecture

* [Architectural Foundation, Quality Attributes & Trust Boundaries](architectural-foundation.md) — `ARCH-*` architecture-wide constraints for authoritative transitions, client/local state, projections, attribution, retry/failure behavior, disclosure enforcement, freshness/uncertainty, trust boundaries, and architecture decision quality.
* [Application Boundaries, Modules & Dependency Architecture](application-boundaries.md) — `MOD-*` ownership/dependency contracts; six authoritative semantic modules, non-authoritative projection/query composition, thin cross-module coordination, and modular-monolith-first deployment posture.

# Planned architecture areas

Phase 005 will add accepted current owners here as persistence/data, identity/access, command/API/concurrency, synchronization/degraded operation, external representation, front-end, and AWS/runtime decisions become stable.

# Authority rule

Accepted architecture documents are current owners for architecture meaning in this subtree while numbered Phase 005 records preserve alternatives, rationale, tradeoffs, and decision lineage.

Architecture must cite task-relevant upstream stable rules and state local consequences rather than recreating complete upstream rule bodies. Knowledge topology does not dictate source-code topology.