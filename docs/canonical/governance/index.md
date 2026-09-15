# Governance

Current repository/design-governance knowledge for MUDAC.

# Methodology and authority

* [Methodology, OKF Adoption & Terminology](methodology-terminology.md) — Daniel Jackson Concept Design, Base lifecycle, OKF v0.2, MUDAC terminology and downstream realization layers.
* [Documentation Authority & Canonical Ownership](documentation-authority.md) — current-owner precedence, one-owner discipline, historical preservation and routing boundaries.
* [Design / Implementation Boundary](design-implementation-boundary.md) — current reopened Concept Design posture, active Phase 012 dependence/subset boundary, frozen 006-D bootstrap and suspended downstream authority.
* [Downstream Architecture & Implementation Authority Quarantine](downstream-authority-quarantine.md) — prevents premature downstream material from constraining reopened Concept Design.

# Retrieval and change governance

* [Agent Context & Progressive Retrieval](agent-context.md) — minimum-sufficient context, progressive disclosure and anti-bloat behavior.
* [Canonical Change & Conflict Governance](change-governance.md) — semantic changes, contradiction handling and downstream/design mismatch.

# Lineage, metadata and validation

* [Source Lineage and Historical Design Records](source-lineage.md)
* [OKF Metadata, Trust, Verification, Lifecycle & Freshness](metadata-trust-lifecycle.md)
* [Knowledge Validation & CI Enforcement](validation-enforcement.md)
* [Stable Rule Identifiers & Cross-Reference Contract](rule-identifiers.md)

# Current methodology posture

```text
Jackson Concept Design: REOPENED / IN PROGRESS
009 realignment/gap map: COMPLETE — PASS
010 foundational completion: COMPLETE — PASS
011 composition/synchronization: COMPLETE — PASS
012 dependence/product-family/subset/scope: IN PROGRESS
012-A: COMPLETE — READY
012-B: COMPLETE — PASS
012-C: COMPLETE — PASS
012-D: NEXT
architecture: SUSPENDED PENDING DESIGN CLOSURE
implementation planning: SUSPENDED
new domain implementation: NOT STARTED
implementation readiness: NOT READY
implementation authorization: NOT YET
```

# Current Concept, composition and dependence authority

[Canonical Concepts](../concepts/) owns the current eighteen-Concept catalog.

[Canonical Synchronizations](../synchronizations/) owns current application composition after Phase 011.

[Canonical Dependence](../dependence/) now owns accepted Phase 012 extrinsic inclusion dependence. It is explicitly partial through 012-C.

Current direct edges are:

```text
Team          → Competition
Participation → Competition
Participation → Identity
Division      → Team
Alias         → Team
Panel         → Participation
```

Current transitive consequences include:

```text
Division → Team → Competition
Alias    → Team → Competition
Panel    → Participation → Competition
Panel    → Participation → Identity
```

Do not duplicate these transitive paths as direct edges without a distinct application-role rationale.

Current explicit universal non-edges include:

```text
Competition ↛ Division
Competition ↛ Panel
Team        ↛ Alias
Identity    ↛ Competition
Identity    ↛ Participation
Access      ↛ Participation
Access      ↛ Identity
```

Access still participates in protected-operation composition; the non-edge conclusion concerns universal Concept inclusion only.

# Current Phase 012 scope conclusions

- Competition is the family anchor for every in-scope MUDAC application variant.
- Division is optional for single-cohort variants.
- Panel is optional for ad-hoc evaluator assignment.
- Alias is required for variants claiming the current blinded-judging role but is not a universal Team dependency.
- a single-cohort no-Division variant is dependence-coherent but needs later policy/composition revalidation before adoption because current disclosure policy names Division in blinded Judge-facing representation.

# Current handoff

012-D now owns Evaluation Occurrence, Evaluation Obligation, Rubric and Scorecard dependence. It should reuse 012-C transitive reachability rather than recreating Competition/Identity edges through every evaluation Concept.

Proceed to **012-D — Evaluation Structure, Responsibility, Basis & Judgment Dependence**.
