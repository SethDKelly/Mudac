---
type: Phase Qualification
title: 018-D — Canonical Ownership, Stable References, Deterministic Resolution & Drift-Control Design
description: "Makes MUDAC current semantic ownership machine-resolvable through an authored ownership-role policy, generated path-role inventory, generated stable-reference index, fail-closed resolver, explicit non-current candidate/history modes, relocation rules, and CI drift enforcement without making routing artifacts semantic authority."
status: stable
tags: [phase-018, ownership, stable-id, resolver, drift-control, routing, canonical, agents]
sources:
  - resource: 018-C-okf-v0.2-conformance-progressive-disclosure-metadata-knowledge-bundle-qualification.md
  - resource: ../canonical/governance/documentation-authority.md
  - resource: ../canonical/governance/rule-identifiers.md
  - resource: ../canonical/governance/deterministic-ownership-resolution.md
  - resource: ../canonical/governance/agent-context.md
  - resource: ../canonical/governance/validation-enforcement.md
  - resource: ../routing/canonical_ownership.json
  - resource: ../routing/canonical_owner_inventory.json
  - resource: ../routing/stable_reference_index.json
  - resource: ../../scripts/generate_owner_inventory.py
  - resource: ../../scripts/generate_stable_reference_index.py
  - resource: ../../scripts/resolve_stable_id.py
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T03:05:00Z }
---

# Purpose

018-D converts MUDAC's human-readable documentation authority model into deterministic machine routing without creating a second semantic authority plane.

018-C established where generic consumers should start. 018-D answers the narrower and more consequential question:

> Given an exact stable rule ID or governed authored path, what role does that artifact have and which authored location controls current meaning?

# 1. Governing principle

018-D adopts:

> **stable identity is semantic addressability; generated routing is not semantic ownership.**

The authority direction remains:

~~~text
stable ID or governed path
  ↓
authored ownership classification policy
  ↓
generated deterministic locator
  ↓
authored owner document
  ↓
smallest surrounding context needed
~~~

Never:

~~~text
search result / generated JSON / resolver output
  ↓
independent semantic authority
~~~

# 2. Authored ownership classification policy

018-D adds:

> docs/routing/canonical_ownership.json

The policy is machine-readable but remains routing/classification governance rather than a rule body.

It defines:

- authored discovery root;
- current canonical owner roots;
- quarantined downstream-candidate roots;
- external-reference root;
- generated OKF projection root;
- explicit historical-adapter paths;
- stable-rule registry path;
- generated inventory/index paths;
- default current-resolution roles;
- explicit flags required for non-current candidate/deprecated/history lookup;
- fail-closed behavior.

Role precedence is:

~~~text
explicit historical adapter
  ↓
downstream candidate root
  ↓
current canonical owner root
  ↓
external reference
  ↓
numbered phase evidence
  ↓
unresolved
~~~

This prevents path placement alone from creating current authority.

# 3. Generated full owner inventory

018-D adds:

> docs/routing/canonical_owner_inventory.json

It is generated from repository paths plus the authored classification policy.

Exit counts:

| Role | Governed paths |
| --- | ---: |
| current-authority | 82 |
| downstream-candidate | 15 |
| historical-adapter | 6 |
| external-reference | 2 |
| **Total** | **105** |

The inventory contains routing role and path only. It deliberately does not reproduce semantic prose.

This gives tools a compact answer to:

> What role does this authored knowledge path have?

without forcing them to infer authority from directory names or frontmatter alone.

# 4. Generated stable-reference index

018-D adds:

> docs/routing/stable_reference_index.json

It is generated from:

1. the authored ownership policy;
2. the authored stable-rule registry;
3. the actual target files and explicit stable anchors.

Exit counts:

~~~text
stable IDs total              226
current-authority IDs          84
downstream-candidate IDs      142
~~~

The generated index contains only:

- stable ID;
- authored owner path;
- exact anchor;
- owner role;
- locator.

It does not copy rule prose.

# 5. Why the current/candidate split matters

Before 018-D, the stable-rule registry preserved both current Concept Design/governance IDs and suspended downstream Architecture/Implementation IDs.

That was correct for referential integrity but expensive for agents to interpret because registry presence could be mistaken for active authority.

018-D makes the distinction machine-explicit:

~~~text
84 IDs
  role = current-authority

142 IDs
  role = downstream-candidate
~~~

Registry presence therefore means:

> stable and resolvable

not:

> currently accepted.

# 6. Deterministic resolver

018-D adds:

> scripts/resolve_stable_id.py

Normal current lookup:

~~~bash
python scripts/resolve_stable_id.py INV-001
~~~

Validated output:

~~~text
INV-001 -> docs/canonical/invariants/judge-independence.md#inv-001 [role=current-authority]
~~~

A quarantined candidate fails ordinary resolution:

~~~text
ARCH-001
  → ERROR
  → role = downstream-candidate
  → explicit --include-candidates required
~~~

Explicit candidate lookup:

~~~bash
python scripts/resolve_stable_id.py ARCH-001 --include-candidates
~~~

Validated output:

~~~text
ARCH-001 -> docs/canonical/architecture/architectural-foundation.md#arch-001 [role=downstream-candidate]
~~~

Deprecated/historical adapters similarly require explicit non-current lookup.

# 7. History/provenance resolution

Numbered-phase occurrences are never used to select a current owner.

Explicit provenance lookup is available through:

~~~bash
python scripts/resolve_stable_id.py <ID> --history
~~~

The resolver first establishes the permitted owner role, then reports numbered-phase occurrences separately as:

> numbered-phase-evidence

Line numbers may be shown for convenience but are not stable identity.

# 8. Known-ID versus unknown-subject retrieval

018-D adds CTX-006.

For an exact stable ID:

~~~text
exact ID
  ↓
resolver
  ↓
authored owner
~~~

Do not load the 32 KB registry or broad-search the repository first.

For an unknown subject:

~~~text
docs/index.md
  ↓
smallest relevant family
  ↓
natural owner
  ↓
exact rule/ID if needed
~~~

This prevents search ranking from becoming an accidental ownership algorithm.

# 9. New ownership governance

018-D adds OWN-001 through OWN-012 in:

> docs/canonical/governance/deterministic-ownership-resolution.md

The rules establish:

- authored owner documents remain semantic authority;
- role classification precedes trust in path location;
- exact ID resolution defaults to current authority;
- candidate IDs require explicit inclusion;
- deprecated/historical adapters cannot satisfy current resolution;
- numbered-phase occurrences are opt-in provenance;
- generated indexes are rebuildable routing artifacts;
- resolution fails closed on drift;
- stable identity is the rule ID, not current file path;
- unknown-subject discovery differs from known-ID resolution;
- OKF lifecycle and owner role remain distinct;
- routing/status mirrors cannot become independent authority.

# 10. Relocation safety

018-D formalizes:

~~~text
stable ID
  != file path
~~~

A safe owner relocation must update together:

- authored owner location;
- stable-rule registry target;
- generated path-role inventory;
- generated stable-reference index;
- affected current links.

Compatible semantic movement may retain the stable ID.

An incompatible semantic replacement receives a new ID.

# 11. Historical adapter disposition

018-D resolves the 018-B question about the six historical adapters.

They do **not** need to move merely for deterministic ownership.

All six are explicitly classified as:

> historical-adapter

before current-root classification is considered.

Therefore their current physical location under canonical no longer creates machine-resolution ambiguity.

Physical relocation remains optional and should be justified by human-navigation benefit rather than authority correctness.

# 12. Architecture and Implementation candidate disposition

The complete Architecture and Implementation roots are classified before individual IDs are resolved as:

> downstream-candidate

Therefore the 142 candidate stable IDs cannot satisfy ordinary current resolution.

018-D intentionally does not move, adopt, revise or retire those candidates.

Their content qualification remains Phase 018-J work.

# 13. Drift controls implemented

018-D adds blocking checks for:

1. authored stable anchors versus registry;
2. generated OKF projection drift;
3. generated path-role owner inventory drift;
4. generated stable-reference index drift;
5. missing or ambiguous stable owner targets;
6. explicit historical-adapter path existence;
7. deprecated canonical artifacts that are not explicitly classified as adapters;
8. current versus candidate resolver behavior;
9. unexpected direct edits to generated routing surfaces through byte-for-byte generation checks.

Knowledge-validation workflow path triggers now also include:

> knowledge/**

so a direct generated-OKF edit cannot bypass the workflow merely because no docs/ file changed.

# 14. Validation repair loop

The first new stable-index CI run failed after all pre-existing authored knowledge and OKF checks passed.

Cause:

> serialization mismatch only — Python JSON default ASCII escaping versus committed UTF-8 for an em dash.

That was a deterministic-generation defect, not a semantic or ownership defect.

The generator was corrected to emit UTF-8 deterministically.

The follow-up pass also added the full owner inventory and resolver smoke tests.

# 15. Final validation evidence

Final 018-D validation:

~~~text
Knowledge Validation run       35681684847

authored knowledge validation  PASS
Markdown files validated       334
frontmatter blocks             242
stable rule anchors            226
errors                          0
warnings                        0

OKF projection                 PASS — 19 files
owner inventory                PASS — 105 governed paths
stable-reference index         PASS — 226 IDs
current-ID smoke test          PASS — INV-001
candidate default rejection    PASS — ARCH-001 rejected
explicit candidate resolution  PASS — ARCH-001 resolved as downstream-candidate
~~~

# 16. Status-mirror drift boundary

018-D designs the governing rule for lifecycle/status mirrors through OWN-012 but does not create a new machine-owned lifecycle authority file.

That is intentional.

Creating such a file now would risk replacing several useful routers with a competing status authority.

Broader automated consistency enforcement among README/AGENTS/phase status mirrors remains correctly assigned to 018-H, where agentic/documentation conformance is evaluated as a whole.

# 17. 018-C handoff disposition

| 018-C requirement | 018-D result |
| --- | --- |
| machine-readable current-owner inventory | COMPLETE |
| deterministic known-ID resolution | COMPLETE |
| current/deprecated/candidate role separation | COMPLETE |
| avoid loading full rule registry for exact ID | COMPLETE |
| status/owner drift design | COMPLETE; broad mirror enforcement remains 018-H |
| relocation safety for historical adapters | COMPLETE |
| generated OKF must not become owner ledger | PRESERVED |
| unknown-subject versus known-ID retrieval | COMPLETE |

# 18. 018-E handoff

With ownership deterministic, the next risk is no longer:

> Can an agent find the right authority?

The next risk is:

> Once it finds that authority, what may the agent actually do?

018-E should define human-directed agent action classes, scope envelopes, semantic/architecture change boundaries, external/destructive action rules, review-versus-change distinctions and task-completion limits.

The ownership resolver should become an input to those action rules, not a permission system by itself.

# 19. Gate evaluation

| Phase-018 gate | 018-D result |
| --- | --- |
| P18-G1 semantic preservation | PASS |
| P18-G2 current/history integrity | PASS |
| P18-G3 documentation economy | PASS — compact generated routing instead of duplicated prose |
| P18-G4 OKF qualification | PRESERVED |
| P18-G5 deterministic routing | PASS |
| P18-G6 human-directed agent authority | NOT YET — 018-E |
| P18-G7 context proportionality | IMPROVED — exact-ID direct lookup |
| P18-G8 conformance proportionality | PASS for ownership/reference scope; broader agentic conformance remains 018-H |
| P18-G10 architecture re-entry integrity | PASS |
| P18-G12 execution boundary | PASS |

# 20. Exit decision

**018-D — COMPLETE — PASS.**

At exit:

~~~text
authored current owners          machine-classifiable
governed knowledge paths         105
current-authority paths           82
historical adapters                6
downstream candidate paths        15

stable IDs                       226
current-authority IDs             84
downstream-candidate IDs         142

exact current resolution          deterministic
candidate resolution              explicit opt-in
history resolution                explicit opt-in
search ranking as authority       prohibited
generated routing authority       none
feature implementation            not authorized
~~~

The next authorized work is:

> **018-E — Agentic Development Authority, Human-Directed Scope, Change Classes & Safety Boundaries**
