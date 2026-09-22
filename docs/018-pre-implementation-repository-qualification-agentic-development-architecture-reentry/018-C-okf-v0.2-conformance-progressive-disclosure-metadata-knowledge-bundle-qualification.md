---
type: Phase Qualification
title: 018-C — OKF v0.2 Conformance, Progressive Disclosure, Metadata & Knowledge-Bundle Qualification
description: "Qualifies MUDAC's OKF v0.2 adoption against the pinned specification, separates authored documentation/provenance from a strict generated OKF compatibility bundle, establishes deterministic projection and metadata rules, validates the projection in CI, and hands exact owner/stable-reference resolution to 018-D."
status: stable
tags: [phase-018, okf, progressive-disclosure, metadata, knowledge-bundle, projection, qualification, routing]
sources:
  - resource: 018-B-whole-corpus-documentation-inventory-duplication-concision-current-history-topology-audit.md
  - resource: ../references/open-knowledge-format.md
  - resource: ../canonical/governance/metadata-trust-lifecycle.md
  - resource: ../canonical/governance/documentation-authority.md
  - resource: ../canonical/governance/agent-context.md
  - resource: ../routing/okf_projection.json
  - resource: ../../scripts/generate_okf_projection.py
  - resource: ../../scripts/validate_knowledge.py
generated: { by: openai/gpt-5.6-sol, at: 2026-09-22T02:51:00Z }
---

# Purpose

018-C determines what MUDAC can truthfully call an Open Knowledge Format v0.2 bundle, how authored repository authority relates to machine-consumable OKF routing, and which metadata and progressive-disclosure rules should remain durable before 018-D adds deterministic ownership and stable-reference resolution.

This is a knowledge-format qualification, not a product-semantic or architecture-selection phase.

# 1. Specification baseline

MUDAC remains pinned to Open Knowledge Format v0.2 at the adopted upstream specification recorded by the Open Knowledge Format reference.

Relevant v0.2 rules include:

- a bundle is a directory tree of Markdown;
- every non-reserved concept Markdown file has YAML frontmatter;
- type is the only always-required concept key;
- index.md and log.md are reserved filenames;
- the bundle-root index.md may declare okf_version: "0.2";
- index files support progressive disclosure;
- sources, generated, verified, status, and stale_after are optional metadata families;
- missing optional metadata must not make a concept unconsumable;
- producer-defined additional metadata is permitted;
- status is draft, stable, or deprecated;
- trust tier derives from actual verified events;
- ordinary Markdown links form the knowledge graph.

MUDAC may use a stricter producer profile for authored current knowledge while remaining compatible with v0.2 consumers.

# 2. Entry conformance defect

Before 018-C, docs/index.md declared okf_version: "0.2", which implied that docs/ itself was the bundle root.

018-B established that docs/ intentionally contains preserved legacy phase evidence, including early Markdown records without OKF concept frontmatter.

Under the pinned specification:

~~~text
declared OKF bundle root
+ non-reserved Markdown without concept frontmatter
= not a strict conformant OKF bundle
~~~

Those legacy records are legitimate provenance and must not be bulk-rewritten merely for format uniformity.

The prior bundle-root claim was therefore too broad.

# 3. Durable two-layer decision

018-C adopts:

~~~text
AUTHORED REPOSITORY KNOWLEDGE
docs/
  = semantic authority
  = governance authority
  = historical provenance
  = phase evidence
  = downstream candidate evidence
  = repository-native progressive disclosure

STRICT OKF v0.2 COMPATIBILITY BUNDLE
knowledge/
  = generated routing projection
  = machine-consumable progressive disclosure
  = no independent semantics
  = no independent authority
  = no hand editing
~~~

The governing shorthand is:

> **two layers, one authority.**

The generated layer exists only to make the authored repository legible to generic OKF consumers without rewriting history or creating a parallel semantic corpus.

# 4. Authored discovery root

The repository-native discovery root remains docs/index.md.

It no longer declares okf_version.

Its broader role is to route current canonical owners, current lifecycle status, quarantined downstream candidates, external references, and numbered design history.

Repository agents should ordinarily use:

~~~text
AGENTS.md
  ↓
docs/index.md
  ↓
canonical family
  ↓
smallest current owner
~~~

The generated knowledge/ tree does not replace this path.

# 5. Strict generated OKF bundle

The strict compatibility bundle is knowledge/.

Its generation contract is:

- docs/routing/okf_projection.json;
- scripts/generate_okf_projection.py.

At 018-C exit the projection contains:

~~~text
domain route documents       8
project route documents      8
route concept documents     16
directory indexes            2
bundle root index            1
total Markdown files        19
~~~

knowledge/index.md is the only strict bundle root and declares okf_version: "0.2".

Every non-reserved generated Markdown file is an OKF concept document with frontmatter.

# 6. Projection route classes

The generated domain layer routes to Project/context, Concepts, Synchronizations, Dependence, Experience, Mechanisms, Policies, and Invariants.

The generated project layer routes to current Governance, authored documentation topology, repository-agent bootstrap, Phase-017 closure evidence, active Phase-018 qualification, suspended architecture candidates, suspended implementation candidates, and external references.

Candidate routes are explicitly labeled downstream-candidate.

A route to a candidate makes it discoverable. It does not adopt it.

# 7. Projection authority contract

The projection specification declares:

> **DERIVED ROUTING ONLY — NOT SEMANTIC AUTHORITY**

Each generated route repeats the boundary.

Authority remains:

~~~text
human-selected task
  ↓
authored current semantic/governance owner in docs/
  ↓
active downstream package when later accepted
  ↓
evidence appropriate to the claim
~~~

A generated route can never create or upgrade semantic, architecture, implementation, verification, deployment, or execution authority.

If authored authority and generated routing disagree, the authored owner wins and projection drift is a validation failure.

# 8. Metadata qualification

Base OKF requires type for strict bundle concept documents.

MUDAC retains a stricter authored current canonical/reference profile requiring:

- type;
- title;
- description;
- status;
- tags;
- sources.

This is compatible with OKF v0.2.

Evidence-dependent optional fields remain:

- resource when an underlying resource is meaningful;
- generated when actual producer/time is known;
- verified only after an actual verification event;
- stale_after only for a real absolute freshness boundary;
- optional source credibility fields only when factually known.

MUDAC does not fabricate metadata for uniformity.

# 9. Lifecycle and target-role distinction

018-C preserves:

~~~text
OKF artifact status
  != MUDAC product state
  != semantic authority
  != architecture acceptance
  != implementation authorization
~~~

A generated route may be status: stable because the route artifact is current in its routing role while the target role is downstream-candidate.

This does not make the target architecture or implementation current accepted authority.

# 10. Trust and verification

No CI result in 018-C creates OKF verified metadata.

The successful validation run proves structural and reproducibility claims only:

~~~text
CI structural PASS
  != OKF verified event
  != human-reviewed trust tier
  != semantic correctness proof
  != runtime proof
~~~

# 11. Progressive disclosure qualification

Repository-native navigation:

~~~text
docs/index.md
  ↓
canonical/index.md
  ↓
family index
  ↓
natural owner
  ↓
linked dependency if needed
  ↓
history only when needed
~~~

Generic OKF navigation:

~~~text
knowledge/index.md
  ↓
domains/ or project/
  ↓
generated routing reference
  ↓
authored repository target
~~~

The generated path terminates in authored knowledge instead of reproducing rule bodies.

# 12. Optional OKF features

MUDAC does not add knowledge/log.md during 018-C. Git and phase records already preserve chronology, and a generated or manually maintained log would add no current retrieval value.

MUDAC also does not adopt Attested Computation concepts during 018-C. There is no current requirement to express product computations as OKF executable contracts, and doing so before architecture selection would create implementation pressure.

# 13. Historical adapters and downstream candidates

018-C does not physically move the six historical/deprecated adapters identified by 018-B, docs/canonical/architecture/, or docs/canonical/implementation/.

The strict bundle no longer depends on those authored paths being intrinsically authoritative because route roles are explicit.

Historical-adapter relocation remains optional and should wait for stable-reference analysis in 018-D.

Downstream candidate disposition remains owned by 018-J.

# 14. Deterministic generation and validation

018-C adds:

- docs/routing/okf_projection.json;
- scripts/generate_okf_projection.py;
- generated knowledge/ projection;
- a generator check in Knowledge Validation CI.

The generator checks the projection authority contract, version and roots, duplicate route names, target existence, expected counts, exact generated content, and unexpected Markdown under knowledge/.

The authored validator now checks the generated bundle root instead of incorrectly requiring docs/index.md to be an OKF root.

# 15. Validation evidence and repair loop

The first 018-C validation run failed and correctly exposed two stable-ID registry defects:

- META-010, introduced by the two-layer OKF contract, was not yet registered;
- OPG-006, a pre-existing operational-exception rule, was also not registered.

Both were repaired before exit.

Final validation evidence:

~~~text
GitHub Actions workflow       Knowledge Validation
run                           35680905120
authored knowledge step       PASS
generated OKF projection      PASS
overall conclusion            SUCCESS
~~~

The repair loop demonstrates that the conformance path is enforcing existing repository invariants rather than merely documenting them.

# 16. 018-B carry-forward disposition

| 018-B concern | 018-C disposition |
| --- | --- |
| six historical adapters under canonical | OKF conformance does not require movement; reference implications to 018-D |
| architecture/implementation candidates under canonical | projection labels them as downstream candidates; physical disposition remains 018-J |
| status mirrors are drift-prone | remains 018-D/H work |
| rule registry is context-heavy | deterministic resolution remains 018-D |
| legacy records lack frontmatter | accepted authored provenance; excluded from strict-bundle requirement |

# 17. 018-D handoff

018-C establishes routing compatibility but not exact semantic-owner resolution.

018-D must define:

1. a machine-readable current-owner inventory;
2. deterministic known-ID resolution;
3. current, deprecated, historical, and candidate ownership roles;
4. stable-ID resolution without loading the full registry;
5. status and owner drift detection;
6. relocation safety for historical adapters;
7. how generated OKF routes consume ownership data without becoming the owner ledger;
8. how unknown-subject discovery differs from known-ID resolution.

The key distinction is:

> **OKF projection answers where a generic consumer should start; 018-D must answer which authored owner controls an exact current rule.**

# 18. Gate evaluation

| Phase-018 gate | 018-C result |
| --- | --- |
| P18-G1 semantic preservation | PASS |
| P18-G2 current/history integrity | PASS |
| P18-G3 documentation economy | PASS — routing projection does not duplicate rule bodies |
| P18-G4 OKF qualification | PASS |
| P18-G5 deterministic routing | PARTIAL — exact owner/ID resolution remains 018-D |
| P18-G7 context proportionality | IMPROVED |
| P18-G8 conformance proportionality | PASS for OKF projection; broader conformance remains 018-H |
| P18-G10 architecture re-entry integrity | PASS |
| P18-G12 execution boundary | PASS |

# 19. Exit decision

**018-C — COMPLETE — PASS.**

Final knowledge topology:

~~~text
docs/
  authored authority + provenance
        ↑
        | generated routes point here
        |
knowledge/
  strict OKF v0.2 routing projection
  deterministic / generated / non-authoritative
~~~

No product semantics were changed.

No architecture was adopted.

No implementation execution was authorized.

The next work is:

> **018-D — Canonical Ownership, Stable References, Deterministic Resolution & Drift-Control Design**
