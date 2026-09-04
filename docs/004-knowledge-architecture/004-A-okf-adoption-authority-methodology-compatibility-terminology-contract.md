# 004-A — OKF Adoption Authority, Methodology Compatibility & Terminology Contract

Status: **Complete**

## 1. Purpose

004-A establishes the authoritative basis for adopting the Open Knowledge Format (OKF) within the MUDAC repository before any repository-wide documentation migration begins.

It defines:

- what OKF is authoritative for;
- what OKF is explicitly **not** authoritative for;
- how OKF coexists with Daniel Jackson Concept Design;
- how the overloaded word `Concept` is disambiguated;
- how MUDAC-defined knowledge types may extend OKF's generic metadata model;
- how external OKF evolution is incorporated without silently changing repository semantics;
- how precedence works when methodology, repository authority, historical phase records, canonical knowledge, and implementation documentation interact;
- what Phase 004 may refactor and what it must preserve.

The governing objective is:

> Adopt OKF as the repository's knowledge-format and navigation contract without allowing a documentation/interchange specification to redefine the product-design methodology, the accepted MUDAC Concept model, or the authoritative semantics already established in Phases 001–003.

---

## 2. Adoption decision

MUDAC adopts **Open Knowledge Format (OKF)** as the repository convention for structuring machine-readable/human-readable knowledge documents and progressive-disclosure knowledge navigation.

OKF is adopted for concerns such as:

```text
knowledge document metadata
knowledge typing
progressive-disclosure indexes
ordinary Markdown cross-reference
source/provenance linkage
knowledge lifecycle/freshness metadata
verification metadata
human + agent discoverability
bundle-relative resource addressing
```

OKF is **not** adopted as:

```text
a product design methodology
a domain model
a runtime architecture
a source-code package model
a database schema
a replacement for MUDAC Concepts
a replacement for Versioning/Provenance domain semantics
```

The core relationship is:

```text
Daniel Jackson Concept Design
        ↓
discovers / evaluates / specifies MUDAC meaning
        ↓
MUDAC canonical knowledge
        ↓
OKF
        ↓
structures, identifies, links and exposes that knowledge
```

Therefore:

> **Concept Design determines what MUDAC means. OKF determines how that knowledge is represented, navigated, attributed, and exchanged.**

---

## 3. Authoritative OKF source

The authoritative upstream source for MUDAC OKF adoption is the dedicated GoogleCloudPlatform **open-knowledge-format** repository rather than the historical/frozen copy formerly present inside `GoogleCloudPlatform/knowledge-catalog/okf`.

Phase 004 will target the currently adopted OKF specification version explicitly in repository metadata/rules rather than relying on an unversioned assumption that `main` always has identical semantics.

The initial adoption baseline is **OKF v0.2**.

The migration must not copy or fork upstream OKF prose into MUDAC as a competing local specification. MUDAC should reference the upstream specification and document only MUDAC-specific adoption choices, constraints, profiles, and extensions.

---

## 4. OKF version policy

MUDAC's OKF adoption is version-aware.

The repository should eventually expose an explicit declaration equivalent in meaning to:

```text
OKF adoption baseline: v0.2
```

A future upstream OKF release does **not** silently change MUDAC repository semantics.

An OKF upgrade requires:

1. identify the upstream version change;
2. review specification changes relevant to MUDAC;
3. evaluate compatibility with MUDAC metadata/profile conventions;
4. identify migration consequences;
5. update the MUDAC adoption declaration deliberately;
6. validate the repository before treating the upgrade as effective.

This separates:

```text
upstream OKF latest
        ≠
MUDAC adopted OKF version
```

---

## 5. Methodology authority remains Daniel Jackson Concept Design

The repository continues to use Daniel Jackson's Concept Design methodology as its product-design authority.

Concept Design remains authoritative for questions such as:

- whether something qualifies as a MUDAC Concept;
- Concept purpose;
- Concept-owned state;
- Concept actions;
- operational principles;
- Concept independence/genericity;
- synchronization between Concepts;
- whether derived mechanisms should remain derived rather than becoming Concepts;
- whether a later architecture decision is attempting to smuggle domain semantics into implementation.

OKF cannot promote a document subject into a MUDAC Concept merely because that subject is represented as an OKF knowledge document.

For example:

```text
Coverage
```

may have its own OKF document for efficient retrieval while remaining a derived/policy mechanism rather than a MUDAC Concept.

Likewise:

```text
Official Outcome Revision
```

may be represented as canonical knowledge while remaining a derived authoritative projection rather than a standalone Concept.

---

## 6. The word `Concept` is overloaded and must be qualified

OKF uses `concept` in the broad knowledge-management sense of an independently addressable knowledge unit/document.

MUDAC already uses **Concept** in the much stronger Daniel Jackson methodological sense.

These meanings must never be silently conflated.

Canonical terminology is therefore:

### MUDAC Concept

A formal application Concept accepted under the Daniel Jackson Concept Design methodology.

Examples:

```text
Competition
Team
Panel
Judging Encounter
Rubric
Scorecard
Award
Identity
Participation
Alias
Access
Versioning
Provenance
Export
```

### OKF knowledge document

An independently addressable knowledge document represented according to the adopted OKF convention.

An OKF knowledge document may describe:

```text
a MUDAC Concept
a policy
a derived mechanism
an invariant
a UX contract
an architecture decision
a design phase record
an external reference
an operational procedure
```

Repository prose should prefer **OKF knowledge document**, **knowledge document**, or **knowledge resource** rather than unqualified `OKF Concept` when confusion with MUDAC Concept is possible.

---

## 7. MUDAC knowledge types

OKF's generic metadata model may be specialized through MUDAC-defined `type` values.

MUDAC knowledge type is classification metadata. It does not create a new application Concept or authority category by itself.

The initial taxonomy is expected to include values conceptually equivalent to:

```text
Design Concept
Design Policy
Derived Mechanism
Design Invariant
Experience Contract
Architecture Contract
Architecture Decision
Design Phase Record
External Reference
Documentation Authority
```

The exact serialized spelling and taxonomy are finalized in later Phase 004 groups.

The governing rule is:

> **Knowledge type describes what kind of knowledge a document carries; it does not decide what domain construct exists.**

For example:

```yaml
type: Design Concept
```

may describe `Scorecard`, while:

```yaml
type: Design Policy
```

may describe Evaluation Policy, and:

```yaml
type: Experience Contract
```

may describe the Judge evaluation workflow.

---

## 8. Repository knowledge authority layers

004-A establishes the conceptual authority order that later migration will make concrete.

### Layer 1 — methodology/adoption authority

Defines how knowledge is produced/interpreted.

Examples:

```text
Daniel Jackson Concept Design methodology
MUDAC documentation authority rules
MUDAC OKF adoption profile
```

### Layer 2 — canonical current knowledge

Defines current MUDAC truth.

Examples:

```text
canonical Concept definitions
canonical policies
canonical invariants
canonical UX contracts
later canonical architecture contracts
```

### Layer 3 — historical design records

Preserves why/how the canonical state emerged.

Examples:

```text
001-* phase records
002-* phase records
003-* phase records
future phase working/consolidation records
```

### Layer 4 — implementation/supporting artifacts

Implements or operationalizes canonical knowledge.

Examples:

```text
source code
schemas
API definitions
infrastructure
CI configuration
tests
runbooks
```

The intended relationship is:

```text
methodology / governance
        ↓ constrains
canonical knowledge
        ↓ constrains
architecture / implementation

historical phase records
        ↑ provenance / rationale
        └──────── canonical knowledge
```

Historical phase records remain authoritative evidence of design evolution, but after migration they are not the preferred retrieval location for current truth when a canonical knowledge document owns that rule.

---

## 9. Canonical current truth versus historical provenance

Phase 004 adopts the following distinction:

> **Historical phase documents explain how MUDAC arrived at the design. Canonical knowledge documents state what MUDAC currently means.**

This is not license to discard phase history.

Phase documents remain important for:

- rationale;
- tradeoff reconstruction;
- design audit;
- source provenance;
- identifying when a rule was introduced/refined;
- understanding rejected alternatives;
- independent review of later canonical extraction.

But agents and humans should not ordinarily reconstruct current rules by recursively reading all historical phases once a canonical owner exists.

---

## 10. Cross-reference over restatement

004-A adopts the following repository-wide documentation principle, to be made enforceable in later Phase 004 work:

> **A normative rule should have one canonical owner. Other documents should reference that owner rather than fully restating the rule.**

Restatement is permitted when necessary for one of these reasons:

- the local architecture option must be independently auditable;
- a threat/failure analysis requires the relevant constraint immediately visible;
- a concise local summary materially improves comprehension;
- external publication must stand alone.

When a normative rule is restated, the restatement must:

1. identify or link the canonical source;
2. preserve the canonical meaning;
3. not claim independent authority;
4. be reviewed when the canonical rule changes if the dependency remains relevant.

The preferred pattern is:

```text
canonical rule
      ↓ reference
architecture / UX / implementation consequence
```

rather than:

```text
canonical rule copy A
canonical rule copy B
canonical rule copy C
```

---

## 11. Stable rule identifiers are compatible with OKF

Phase 004 will introduce stable identifiers for important normative rules/invariants/contracts where doing so improves durable cross-reference.

Conceptually:

```text
SC-001 — One logical Scorecard per Judge × Encounter
SC-002 — Exact Rubric Version binding
SC-003 — Draft is non-authoritative
SC-004 — Judge retains evaluation authorship
```

These identifiers are **MUDAC documentation identifiers**, not OKF-defined identifiers and not application database identifiers.

They provide stable semantic anchors for:

- Markdown links;
- architecture compliance references;
- agent retrieval;
- change-impact analysis;
- tests/acceptance criteria where appropriate.

Exact naming/namespace conventions are finalized in 004-E.

---

## 12. OKF metadata and MUDAC domain metadata remain distinct

OKF metadata such as knowledge lifecycle, provenance/source pointers, generation/verification information, or knowledge-document type describes the **knowledge artifact**.

It must not be confused with MUDAC application state.

For example:

```text
OKF knowledge document status: stable
```

is not:

```text
Competition state: Ready
```

and:

```text
knowledge document verified by a human
```

is not:

```text
paper Scorecard verified against physical source
```

Likewise, OKF provenance describing where documentation came from does not replace the MUDAC Provenance Concept that records meaningful application authority transitions.

The same word may exist in both systems only when its scope is explicit.

---

## 13. OKF provenance supplements rather than replaces MUDAC Provenance

MUDAC already has a formal **Provenance** Concept concerning application/domain authority history.

OKF also supports knowledge-source/provenance metadata.

These are related but operate at different layers:

```text
OKF provenance
    What knowledge sources produced this document?

MUDAC Provenance Concept
    How, why, when, and through whose authority did application state arise/change?
```

Therefore:

> **OKF provenance describes documentation lineage. MUDAC Provenance describes Competition-domain authority lineage.**

A canonical knowledge document about MUDAC Provenance may itself have OKF source metadata pointing to the historical phase records from which that Concept definition was extracted.

---

## 14. Verification semantics must not be overstated

OKF verification metadata must represent actual knowledge verification.

Agent generation, transformation, or migration does not automatically qualify as human verification.

The repository should preserve distinctions conceptually equivalent to:

```text
generated / migrated by automation or agent
        ≠
human-reviewed / verified
```

A migration process may produce structurally valid OKF documents while they remain pending semantic verification.

Human verification should be attributable to a real review event or accepted repository process rather than inferred from file existence or merge status alone.

Detailed metadata conventions are finalized in 004-G.

---

## 15. Knowledge lifecycle is not product lifecycle

OKF knowledge lifecycle metadata such as:

```text
draft
stable
deprecated
```

applies to the knowledge resource.

It must not be overloaded with Competition lifecycle:

```text
Draft
Ready
Active
Event Completed
Finalized
```

or Scorecard lifecycle:

```text
Draft
Finalized
Amendment Draft
```

UI/documentation must qualify the subject when overlapping words are present.

---

## 16. Source-code refactoring boundary

Phase 004 is authorized to refactor the repository's **knowledge/documentation structure**.

It is not authorized to invent future application module/package boundaries merely to mirror OKF organization.

The rule is:

```text
knowledge architecture
        ↔ references
application architecture

knowledge architecture
        ≠ dictates package tree
```

When application code exists, canonical knowledge may link to source modules, schemas, APIs, tests, and infrastructure as resources.

The later system/application architecture phase determines those implementation boundaries from product semantics, quality attributes, coupling/cohesion, security, deployment, and operational requirements.

---

## 17. Migration is allowed to change location, not meaning

Phase 004 may:

- create new OKF-aligned indexes;
- extract canonical knowledge from historical phase records;
- move/copy phase records into a history/provenance region when the migration plan calls for it;
- add metadata/frontmatter;
- replace duplicated restatement with canonical references;
- add stable rule identifiers;
- create documentation-governance rules;
- add validation tooling;
- update links and indexes.

Phase 004 may **not**, without an explicit design refinement:

- change the accepted Concept catalog;
- alter Competition/Scorecard lifecycle semantics;
- weaken Judge independence;
- change aggregation/Coverage/Ranking policy semantics;
- redefine authority boundaries;
- change anonymity/disclosure defaults;
- change Finalization or Official Outcome semantics;
- reinterpret paper/electronic evidence equivalence;
- weaken accessibility/resilience requirements.

If migration exposes a genuine contradiction or missing design rule, the issue must be surfaced explicitly as a design refinement rather than silently "fixed" during knowledge restructuring.

---

## 18. External references do not become local authority by copying

MUDAC may maintain knowledge documents that reference external standards/methodologies such as:

```text
Open Knowledge Format
Daniel Jackson Concept Design
WCAG
future AWS/security standards
```

The preferred pattern is to record:

- what external authority/resource is being used;
- which version/date/profile is adopted where material;
- what MUDAC-specific interpretation applies;
- what is deliberately not adopted.

The repository should not duplicate entire external specifications as local prose merely to make them searchable.

This reduces stale local copies and preserves a clear authority boundary.

---

## 19. Precedence contract

When interpreting repository documentation, the following precedence applies unless a more specific canonical rule explicitly says otherwise:

```text
1. Explicit current MUDAC canonical knowledge / governance
2. Current accepted phase-exit refinements not yet migrated into canonical knowledge
3. Historical phase records for rationale/provenance
4. Downstream architecture/implementation documentation
5. Incidental comments/examples/non-normative prose
```

External methodology/specification authority is applied through the MUDAC adoption/profile contract rather than assumed to override MUDAC semantics automatically.

An implementation document cannot override a canonical product rule by restating it differently.

A historical phase document does not regain current-rule ownership merely because it contains a fuller explanation than the extracted canonical document; instead the canonical document should link to that history for rationale.

---

## 20. Agent interpretation contract

Agents working in the repository should eventually be instructed to retrieve knowledge in this order:

```text
relevant index.md
      ↓
canonical knowledge document(s)
      ↓
linked dependencies
      ↓
historical phase records only when rationale/provenance is needed
```

They should not default to loading all phases recursively.

Agents must also distinguish:

```text
canonical rule
historical rationale
implementation choice
working hypothesis
external reference
```

and should prefer adding a reference to canonical authority over creating another full rule restatement.

Detailed agent/Cursor/Codex rules are defined in 004-F.

---

## 21. Compatibility tests

004-A considers OKF adoption compatible with the existing design only if all of the following remain true.

### Methodology test

Can MUDAC continue to use Daniel Jackson Concept Design without translating every formal Concept into an OKF-specific domain model?

**Pass.** OKF is treated as knowledge structure rather than domain methodology.

### Concept-boundary test

Can derived mechanisms such as Coverage or Ranking have dedicated knowledge documents without becoming MUDAC Concepts?

**Pass.** Knowledge-document identity and application Concept identity are explicitly separate.

### Provenance test

Can OKF source metadata coexist with the MUDAC Provenance Concept?

**Pass.** They describe different layers: documentation lineage versus Competition authority lineage.

### Lifecycle test

Can OKF knowledge status coexist with Competition/Scorecard lifecycle states?

**Pass.** Status scope is qualified and never conflated.

### History test

Can the phase corpus remain preserved while canonical current truth becomes easier to retrieve?

**Pass.** Historical records become provenance/rationale sources rather than being deleted.

### Agent-context test

Can agents retrieve less context while retaining authority traceability?

**Pass.** Progressive indexes + canonical owners + links allow selective traversal back to history only when needed.

### Architecture-independence test

Can later application architecture choose module/data/runtime boundaries independently of OKF directory structure?

**Pass.** OKF structures knowledge rather than implementation packages.

No compatibility blocker requires reopening Phase 001–003.

---

## 22. 004-A invariants

1. Daniel Jackson Concept Design remains MUDAC's product-design methodology authority.
2. OKF is a knowledge representation/navigation convention, not a domain methodology.
3. The dedicated upstream open-knowledge-format repository is the OKF authority; frozen legacy copies are not the implementation baseline.
4. MUDAC adopts OKF by explicit version/profile rather than silently tracking upstream `main`.
5. An OKF knowledge document is not automatically a MUDAC Concept.
6. The word `Concept` is qualified when OKF/MUDAC meaning could be ambiguous.
7. MUDAC knowledge `type` metadata classifies documents; it does not create domain constructs.
8. Canonical current knowledge and historical phase records are separate authority layers.
9. Historical phase records remain preserved as rationale/provenance.
10. Normative rules should have one canonical owner.
11. Downstream documents reference canonical rules rather than independently re-authoring them.
12. Necessary restatement identifies its canonical source and does not gain independent authority.
13. Stable rule identifiers may be introduced as MUDAC documentation anchors.
14. OKF metadata scope is separate from MUDAC domain state.
15. OKF provenance does not replace the MUDAC Provenance Concept.
16. OKF verification cannot claim human review that did not occur.
17. Knowledge lifecycle status does not redefine Competition/Scorecard lifecycle.
18. Knowledge-tree structure does not dictate source-code architecture.
19. Migration may restructure knowledge but cannot silently alter established product semantics.
20. External specifications are referenced/profiled rather than copied into competing local authorities.
21. Current canonical knowledge outranks downstream implementation restatements.
22. Agents should traverse indexes → canonical knowledge → dependencies → history as needed rather than recursively loading the corpus.
23. A contradiction discovered during migration must become an explicit design refinement, not an undocumented migration edit.
24. Phase 001–003 remain closed; 004-A introduces no reason to reopen their exits.

---

## 23. Explicit non-decisions

004-A does **not** yet decide:

- final `docs/` OKF directory topology;
- exact frontmatter schema/profile used by every document;
- exact knowledge type strings;
- rule-ID namespace syntax;
- whether existing phase directories move physically or remain in place with historical indexes;
- exact `index.md` decomposition;
- exact `log.md` usage;
- migration order for every document;
- automated validator implementation/language;
- CI workflow implementation;
- source-code architecture;
- application architecture;
- persistence/API/AWS architecture.

Those decisions belong to 004-B through 004-H and the later system-architecture phase.

---

## 24. Exit decision

004-A passes.

OKF adoption is compatible with the completed Concept and UX architecture provided it remains subordinate to MUDAC's design semantics and is used as a knowledge-format/governance layer rather than as an alternate domain methodology.

The next subgroup is:

**004-B — Knowledge Bundle Topology, Canonical Authority Layers & Progressive Disclosure**

004-B should turn the authority model established here into the concrete repository knowledge topology, including the location and role of root/index documents, canonical knowledge areas, historical phase records, references, progressive-disclosure traversal, and migration compatibility.
