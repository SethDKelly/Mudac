# 004-B — Knowledge Bundle Topology, Canonical Authority Layers & Progressive Disclosure

Status: **Complete**

## 1. Purpose

004-B defines the physical and navigational topology for MUDAC's OKF-aligned documentation bundle.

It translates the authority model established in [004-A](004-A-okf-adoption-authority-methodology-compatibility-terminology-contract.md) into a concrete repository structure that can support:

- one preferred location for current canonical knowledge;
- preserved historical phase records and rationale;
- progressive disclosure for humans and agents;
- stable links during migration;
- explicit separation of governance, domain meaning, policy, derived mechanisms, UX contracts, architecture, and external references;
- future system/application architecture without forcing source-code structure to mirror documentation structure;
- gradual migration rather than a risky all-at-once rewrite.

The governing objective is:

> Make current MUDAC knowledge easy to find without destroying the design history that explains it, and make the preferred retrieval path obvious enough that humans and agents do not need to recursively load the full phase corpus.

---

## 2. Bundle root decision

The OKF **Knowledge Bundle root is `docs/`**.

MUDAC does not create a parallel `okf/`, `knowledge/`, or generated mirror beside the existing documentation.

The intended top-level shape is:

```text
docs/
├── index.md
├── README.md
├── canonical/
├── references/
├── 001-concept-design/
├── 002-concept-specification/
├── 003-conceptual-ux-architecture/
├── 004-knowledge-architecture/
└── future numbered phase directories...
```

This treats the existing documentation corpus as the knowledge bundle rather than creating two competing documentation systems.

The bundle-root `index.md` is the preferred progressive-disclosure entry point.

`docs/README.md` remains during migration as a human-friendly compatibility/documentation-authority entry point, but it must not evolve into a second independent canonical knowledge graph.

---

## 3. Root OKF version declaration

The bundle-root `docs/index.md` declares the adopted OKF baseline:

```yaml
---
okf_version: "0.2"
---
```

This follows the OKF v0.2 rule that `index.md` normally contains no frontmatter, with the bundle-root version declaration as the defined exception.

No nested `index.md` should carry OKF concept frontmatter.

The bundle-root declaration expresses the **MUDAC adopted OKF version**, not a promise to track whatever version upstream `main` later contains.

---

## 4. Canonical current knowledge lives under `docs/canonical/`

The canonical current-knowledge layer is grouped under a stable, non-phase-numbered path:

```text
docs/canonical/
├── index.md
├── governance/
│   └── index.md
├── concepts/
│   └── index.md
├── mechanisms/
│   └── index.md
├── policies/
│   └── index.md
├── invariants/
│   └── index.md
├── experience/
│   └── index.md
└── architecture/
    └── index.md
```

The purpose of `canonical/` is not to duplicate the phase documents.

It becomes the preferred ownership layer for statements such as:

```text
What is a Scorecard?
What lifecycle does Competition use?
What makes a Scorecard authoritative?
How is Coverage different from Aggregate?
What disclosure does Judge mode permit?
What is the controlled Finalization model?
What UX contract governs uncertain persistence?
What architecture contract later implementations must satisfy?
```

Canonical files use semantic names rather than phase numbers.

For example, later migration may produce:

```text
canonical/concepts/scorecard.md
canonical/concepts/judging-encounter.md
canonical/policies/evaluation-policy.md
canonical/mechanisms/coverage.md
canonical/invariants/judge-independence.md
canonical/experience/judge-evaluation.md
```

A rule should not be copied into each of those documents merely because several documents depend on it. One document owns it; others link to it.

---

## 5. Why `canonical/` is a separate subtree

The repository currently has phase-oriented documentation whose file names intentionally encode design chronology.

Current truth has different stability requirements.

A phase path answers:

> When and through what design work did this conclusion emerge?

A canonical path answers:

> Where should I go now to understand the current rule?

Separating them produces:

```text
chronology-oriented history
        ≠
meaning-oriented current knowledge
```

This allows future Phase 005, 006, and later work to refine canonical knowledge without forcing consumers to understand which phase most recently restated a rule.

---

## 6. Governance region

`docs/canonical/governance/` owns repository-level interpretation and knowledge-governance contracts.

Expected knowledge includes subjects such as:

```text
design methodology authority
OKF adoption profile
documentation authority and precedence
terminology contract
canonical ownership rules
cross-reference/restatement rules
agent retrieval/context rules
knowledge change governance
```

Governance answers how repository knowledge should be interpreted and maintained.

It does not own product-domain state merely because governance constrains its documentation.

004-A is a historical design record for this authority. Later Phase 004 work may extract a concise canonical governance document from it.

---

## 7. Concepts region

`docs/canonical/concepts/` owns the current definitions of accepted **MUDAC Concepts**.

The accepted 15-Concept catalog remains:

```text
Competition
Division
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

One canonical knowledge document per MUDAC Concept is the expected baseline unless a later design refinement shows that another arrangement better preserves Concept independence.

These documents should concentrate Concept meaning:

```text
purpose
owned state
actions
operational principle
important invariants
key synchronizations
links to related policy / mechanism / experience knowledge
historical sources
```

They should not become implementation class specifications.

---

## 8. Mechanisms region

`docs/canonical/mechanisms/` exists because several important MUDAC constructs deserve direct retrieval while deliberately remaining **non-Concepts**.

Expected examples include:

```text
Coverage
Aggregate
Rank
Evaluation Policy-derived readiness projections
Official Outcome Revision
Reconciliation projections
Team Attribute Definition
Panel Membership
Criterion / Note where independent retrieval is useful
```

The region prevents an undesirable choice between:

```text
hide important derived knowledge inside unrelated Concept prose
```

and:

```text
promote every important idea into a MUDAC Concept
```

A canonical mechanism document remains explicit about its non-Concept status where ambiguity is possible.

---

## 9. Policies region

`docs/canonical/policies/` owns configurable or governing competition semantics that are neither generic Concept identity nor implementation configuration details.

Expected subjects include:

```text
Evaluation Policy
Coverage / eligibility policy
aggregation policy
ranking and tie policy
anonymity/disclosure policy
Panel composition policy
Award/finalization policy
continuity/paper policy
correction/authority policy
```

Policy documents should link to the Concepts and mechanisms they govern rather than restating their full definitions.

Likewise, Concept documents should reference policy when behavior depends on configurable rules rather than embedding one current event's configuration as universal semantics.

---

## 10. Invariants region

`docs/canonical/invariants/` owns cross-cutting normative constraints whose scope spans multiple Concepts or workflows and for which a dedicated stable referent materially improves auditability.

Expected examples include constraints such as:

```text
Judge independence
one logical Scorecard per Judge × Encounter
missing is never zero
Organizer authority does not become Judge authorship
calculated is not official
Finalized is not automatically published
accessibility changes representation, not authority
connectivity uncertainty never becomes false authoritative success
```

Not every sentence in the corpus becomes an invariant file.

A standalone invariant is justified when it is:

- cross-cutting;
- repeatedly depended upon;
- normatively important;
- useful as a stable architecture/test reference;
- difficult to assign cleanly to only one Concept owner.

Rule-ID conventions are finalized in 004-E.

---

## 11. Experience region

`docs/canonical/experience/` owns the current conceptual UX contracts extracted from Phase 003.

Expected subjects include:

```text
experience context and role modes
Judge onboarding
Judge evaluation / amendment
Organizer preparation
live operations
reconciliation/finalization
paper capture and publication
accessibility/resilience
status/privacy/recovery grammar
```

These documents describe required user-facing meaning and interaction semantics.

They do not prescribe React components, routes, CSS, local-state libraries, or HTTP APIs.

Future visual/component design can reference these contracts directly rather than treating the Phase 003 chronology as a screen specification.

---

## 12. Architecture region

`docs/canonical/architecture/` is reserved for **current accepted architecture contracts and decisions** beginning with the later system/application architecture phase.

During Phase 004 it is intentionally sparse.

Its existence in the topology establishes the future authority relationship:

```text
canonical product / policy / invariant / experience knowledge
        ↓ constrains
canonical architecture knowledge
        ↓ constrains
implementation artifacts
```

Architecture documents may explain how a technology satisfies a canonical rule but cannot redefine the upstream rule by copying it differently.

The architecture directory does not imply any particular application package tree.

---

## 13. External/reference knowledge lives under `docs/references/`

MUDAC uses the OKF `references/` convention at the bundle root for knowledge about external authorities/resources that the project depends upon or profiles.

Expected examples include:

```text
Open Knowledge Format
Daniel Jackson Concept Design
WCAG 2.2
future AWS/security/platform standards
external rules or event references where appropriate
```

A reference knowledge document should capture:

- canonical external resource/link;
- version/date when material;
- why MUDAC uses it;
- MUDAC-specific profile/adoption choices;
- boundaries on what is not adopted.

It should not copy an entire external specification into the repository.

`references/` is not an authority shortcut: an external standard affects MUDAC through an explicit adoption/profile decision.

---

## 14. Historical phase records remain at their existing paths

**004-B decides not to physically relocate the existing numbered phase directories.**

Therefore these paths remain stable:

```text
docs/001-concept-design/
docs/002-concept-specification/
docs/003-conceptual-ux-architecture/
docs/004-knowledge-architecture/
```

Future numbered design phases may continue this convention.

This is deliberate.

Moving all existing phase files under a new `history/` directory would create widespread link churn without improving the meaning of the historical records themselves.

The existing paths are already descriptive, chronological, and version-controlled.

The root `docs/index.md` will identify them explicitly as **Design History / Phase Records**, which is sufficient to establish their authority role without changing their physical location.

---

## 15. No synthetic `history/` directory

Because the historical records remain physically in their current directories, MUDAC will not create a `docs/history/` directory merely to contain an index that points back out to sibling directories.

Such a directory would imply a physical hierarchy that does not exist and would weaken the clarity of OKF progressive-disclosure semantics.

Instead:

```text
docs/index.md
    ├── Current canonical knowledge → canonical/
    ├── External references → references/
    └── Design history → 001-*, 002-*, 003-*, 004-*, ...
```

The graph relationship provides the historical grouping; physical relocation is unnecessary.

---

## 16. Phase records remain source lineage, not duplicate current authority

Historical phase documents remain valid evidence of:

```text
discovery
rationale
tradeoffs
prior assumptions
accepted refinements
exit decisions
```

As canonical extraction progresses, phase records should increasingly link forward to canonical owners where useful.

Canonical documents should record phase files as internal OKF `sources` where they materially derive from them.

The intended relationship is:

```text
historical phase record
        ↓ source / rationale
canonical current knowledge
```

not:

```text
historical record and canonical file both independently own the current rule
```

During migration, where extraction is incomplete, the Phase 001–003 exits remain authoritative inputs exactly as specified by 004-A's precedence contract.

---

## 17. Transitional authority during Phase 004

The migration cannot become atomic without unnecessary risk.

Therefore Phase 004 explicitly supports a transitional state:

### Before canonical extraction of a subject

The accepted phase-exit records and refinements remain the current source of truth.

### After a subject is extracted and accepted into `canonical/`

The canonical knowledge document becomes the preferred current owner, with phase records retained as source/rationale.

### At Phase 004 exit

The repository must no longer require normal consumers to reconstruct baseline current truth from historical phases.

This prevents a dangerous assumption that merely creating the `canonical/` directory instantly supersedes all existing documents.

---

## 18. `docs/index.md` is the preferred navigation root

The root index should answer, before a consumer opens detailed files:

```text
What is current canonical knowledge?
Where are external authorities/references?
Where is design history?
What phase is active?
How should I navigate if I only need implementation context?
```

The index should remain concise.

It should **route**, not restate.

It may contain descriptions such as:

```text
Concepts — current definitions of accepted MUDAC Concepts.
Policies — configurable/governing competition rules.
Experience — current conceptual UX contracts.
```

It should not reproduce Scorecard lifecycle, Ranking equations, disclosure rules, or dozens of invariants.

---

## 19. Progressive disclosure contract

Agents and humans should traverse the bundle one semantic level at a time:

```text
docs/index.md
      ↓
canonical/index.md
      ↓
relevant category index.md
      ↓
specific knowledge document
      ↓
linked dependency only when needed
      ↓
historical source only when rationale/provenance is needed
```

Example:

```text
docs/index.md
      ↓
canonical/concepts/index.md
      ↓
canonical/concepts/scorecard.md
      ↓
linked:
  ../policies/evaluation-policy.md
  ../invariants/judge-independence.md
      ↓
002-D / 002-E / 003-C only if rationale is required
```

This traversal is the core context-budget strategy for future agents.

---

## 20. Index files are routing documents, not concept documents

Following OKF v0.2:

- `index.md` may exist at any directory level;
- nested index files carry no concept frontmatter;
- the bundle-root `index.md` may declare `okf_version`;
- indexes enumerate immediately useful child knowledge and subdirectories;
- descriptions should be concise enough to support retrieval decisions.

MUDAC adds these profile rules:

1. An index should normally describe one level of navigation rather than recursively enumerate the whole subtree.
2. An index should not become a second canonical owner for rules stated in linked documents.
3. If a category is intentionally empty or migration is pending, say so explicitly.
4. Index entries should use stable relative Markdown links.
5. Indexes should distinguish canonical/current content from historical/design records when both are presented.

---

## 21. Relative-link policy

MUDAC prefers **relative Markdown links** within the `docs/` bundle where practical.

OKF permits absolute URLs, bundle-relative paths, and relative paths. Relative Markdown links provide the best joint behavior for:

```text
GitHub browsing
local editors
static documentation tooling
OKF consumers
repository moves/forks
```

Examples:

From `canonical/concepts/scorecard.md`:

```text
../policies/evaluation-policy.md
../../002-concept-specification/002-D-rubric-criterion-scorecard-notes-specifications.md
```

External resources continue to use absolute URLs.

A future validator should check that internal links resolve.

---

## 22. Canonical path stability contract

Once a canonical knowledge document has been accepted and referenced by downstream architecture or implementation, its path should be treated as a stable interface.

Renaming/moving such a file requires:

1. a documented reason;
2. update of inbound references;
3. validation of link integrity;
4. consideration of a deprecation/redirect strategy where supported by the chosen documentation tooling;
5. change-impact review for stable rule IDs if applicable.

Canonical paths should therefore avoid transient phase numbers, implementation technology names, or event-year names unless the subject is intentionally version/event specific.

Good:

```text
canonical/concepts/scorecard.md
canonical/policies/ranking-and-ties.md
```

Poor for generic authority:

```text
canonical/phase-002-scorecard.md
canonical/react-scorecard.md
canonical/2026-ranking.md
```

---

## 23. Canonical categories are retrieval aids, not ontology boundaries

The directory structure organizes knowledge for progressive disclosure.

It does not mean a subject has only one relationship.

For example:

```text
Scorecard
```

lives under `concepts/`, but may link heavily to:

```text
policies/
invariants/
experience/
architecture/
```

The knowledge graph is therefore:

```text
tree for navigation
+
Markdown links for semantic relationships
```

MUDAC must not distort Concept Design merely to make every relationship fit a parent/child folder hierarchy.

---

## 24. Category-placement rule

A document should be placed according to its **primary authority purpose**, not every subject it mentions.

Use:

```text
governance/   how repository/design knowledge is governed
concepts/     accepted MUDAC Concept meaning
mechanisms/   important non-Concept/derived constructs
policies/     configurable/governing competition semantics
invariants/   cross-cutting normative constraints
experience/   actor-facing conceptual UX contracts
architecture/ accepted system/application architecture knowledge
references/   external authorities/resources and MUDAC adoption context
```

Cross-links express secondary relationships.

If placement remains ambiguous, prefer the category representing the document's normative owner and link from other relevant indexes rather than duplicating the document.

---

## 25. No canonical duplication by audience

MUDAC will not maintain separate independent copies such as:

```text
agent canonical rules
human canonical rules
architect canonical rules
developer canonical rules
```

The same canonical Markdown knowledge serves all consumers.

Indexes, generated views, search, or future agent rules may provide different **navigation** into that knowledge, but the underlying authority remains shared.

This is an important anti-drift property.

---

## 26. `docs/README.md` compatibility role

`docs/README.md` currently carries substantial documentation authority/history summary.

004-B does not delete or immediately rewrite it into a minimal pointer because migration is still incomplete.

Instead its role transitions in stages:

```text
Phase 004 early
    compatibility + current migration authority summary

Phase 004 middle
    points increasingly to docs/index.md + canonical/

Phase 004 exit
    concise human landing/compatibility document
    docs/index.md is preferred knowledge-bundle navigation root
```

The README must not become a permanent parallel canonical rule store.

---

## 27. Root repository README role

The repository-root `README.md` remains a product/repository introduction.

It may summarize:

```text
product purpose
design methodology
high-level principles
phase status
where canonical documentation lives
```

It should not be the canonical owner of detailed domain rules.

As Phase 004 progresses, detailed principles in the root README should increasingly reference canonical knowledge rather than accumulating independent full restatements.

---

## 28. Phase directories remain chronological work records

Numbered phase directories continue to serve as design-work records.

A future phase directory may contain:

```text
phase index / plan
subgroup design records
exit review
migration/refinement evidence
```

They should not become the preferred long-term retrieval structure for current domain semantics.

Future phase work should reference canonical knowledge as input instead of copying the entire existing baseline into every subgroup document.

This change should significantly reduce phase-document growth and context duplication beginning with Phase 005.

---

## 29. Architecture and implementation knowledge added later

When source code and infrastructure exist, `canonical/architecture/` may contain documents whose frontmatter `resource` or body links refer to:

```text
source modules
OpenAPI/schema files
migration definitions
CI workflows
infrastructure code
operational runbooks
tests
```

Those links make implementation resources part of the knowledge graph without requiring them to live under `docs/` or mirror the documentation taxonomy.

This preserves the 004-A boundary:

```text
knowledge topology
        ≠
source-code topology
```

---

## 30. Topology does not create authority by itself

Putting a file in `canonical/` is necessary for canonical ownership after migration, but physical placement alone is not sufficient.

Canonical acceptance also requires the repository's later governance/verification rules to establish that the document is:

```text
semantically extracted/reviewed
properly sourced
not contradicted by higher-precedence authority
valid under the adopted OKF profile
linked from the appropriate index
```

Therefore an agent may not create an arbitrary file under `canonical/` and thereby supersede accepted design authority.

The precise acceptance/verification process is finalized in 004-F/004-G.

---

## 31. Initial topology bootstrap

004-B authorizes creation of the following routing skeleton immediately:

```text
docs/index.md

docs/canonical/index.md
docs/canonical/governance/index.md
docs/canonical/concepts/index.md
docs/canonical/mechanisms/index.md
docs/canonical/policies/index.md
docs/canonical/invariants/index.md
docs/canonical/experience/index.md
docs/canonical/architecture/index.md

docs/references/index.md
```

These indexes may explicitly say that canonical extraction is pending.

Creating the navigation skeleton does **not** prematurely migrate semantics; 004-C performs the canonical extraction work.

---

## 32. Initial root navigation model

The bundle root should expose three major retrieval choices:

```text
CURRENT KNOWLEDGE
    canonical/

EXTERNAL AUTHORITIES / REFERENCES
    references/

DESIGN HISTORY / ACTIVE DESIGN WORK
    001-*
    002-*
    003-*
    004-*
    future phase directories
```

A human or agent asking a current product question should normally choose **Current Knowledge**.

A consumer checking an external methodology/standard should choose **References**.

A consumer asking why a choice was made, what alternatives were rejected, or how a rule evolved should choose **Design History**.

---

## 33. Retrieval authority examples

### Example A — "What is a Scorecard?"

Preferred future path:

```text
docs/index.md
→ canonical/concepts/index.md
→ canonical/concepts/scorecard.md
```

History only if rationale is needed.

### Example B — "Why are missing evaluations not zero?"

Preferred future path:

```text
docs/index.md
→ canonical/invariants/index.md
→ missing-is-not-zero canonical rule
→ linked Coverage/Aggregation policy
```

Historical 002-F only when rationale or original policy discussion is needed.

### Example C — "Which OKF version does MUDAC use?"

Preferred path:

```text
docs/index.md
→ canonical/governance/
→ OKF adoption profile
```

with a linked external reference under `references/`.

### Example D — "How did the Judge amendment UX evolve?"

This is a historical question, so direct navigation into the Phase 003 records is appropriate.

---

## 34. Anti-bloat consequence for future design phases

Once canonical extraction is sufficiently complete, future phase records should begin with focused references such as:

```text
Inputs:
- [Scorecard](../../canonical/concepts/scorecard.md)
- [Judge Independence](../../canonical/invariants/judge-independence.md)
- [Judge Evaluation Experience](../../canonical/experience/judge-evaluation.md)
```

rather than reproducing pages of baseline semantics.

A phase record should contain:

```text
new problem
new alternatives
new reasoning
new decision
new consequences
```

not another full copy of current MUDAC truth.

---

## 35. 004-B invariants

The topology must preserve these invariants:

1. `docs/` is the MUDAC OKF bundle root.
2. `docs/index.md` is the preferred progressive-disclosure entry point.
3. Only the bundle-root index may carry the OKF version frontmatter exception.
4. Current canonical knowledge lives under `docs/canonical/`.
5. Historical numbered phase directories remain at their existing paths.
6. Existing phase records are not physically moved merely to create a `history/` hierarchy.
7. No synthetic `history/` directory is required.
8. Canonical knowledge and phase history have different authority purposes.
9. Canonical extraction is gradual; creating a directory does not instantly supersede phase authority.
10. `canonical/concepts/` contains accepted MUDAC Concept knowledge, not every OKF knowledge document.
11. Important non-Concept constructs may receive first-class documents under `mechanisms/`.
12. Policies and invariants remain distinct from Concept identity.
13. Experience contracts remain technology-independent.
14. Architecture knowledge is downstream of product/policy/invariant/experience authority.
15. `references/` records external authorities without copying them into local competing specifications.
16. Index files route; they do not own duplicated normative rules.
17. Index traversal should normally expose one semantic level at a time.
18. Relative internal Markdown links are preferred.
19. Canonical paths become stable interfaces once accepted downstream.
20. Directory categories aid retrieval but do not define the Concept ontology.
21. Cross-links express relationships that do not fit the directory tree.
22. There is one shared canonical corpus for humans and agents.
23. `docs/README.md` transitions toward compatibility/landing-page status rather than remaining a parallel rule store.
24. Root README remains introductory rather than detailed canonical authority.
25. Future phase documents should consume canonical references instead of recursively restating baseline semantics.
26. Knowledge topology must not dictate source-code topology.
27. Physical placement alone cannot grant canonical authority.
28. Canonical acceptance requires later governance/verification rules.

---

## 36. 004-B exit finding

The MUDAC repository can adopt OKF without destabilizing its existing design record.

The preferred migration is an **overlay model**:

```text
existing phase history stays put
            +
new canonical meaning-oriented tree
            +
root progressive-disclosure index
            +
external references region
            ↓
agent/human knowledge graph
```

This avoids a high-cost documentation move while solving the actual problem: consumers need a stable, concise path to current truth.

The most important structural conclusion is:

> **Do not reorganize history merely to make it look canonical. Preserve history where it is, and create a new semantic ownership layer for current knowledge.**

---

## 37. Handoff to 004-C

004-C — **Canonical Concept, Policy, Invariant & Experience Knowledge Extraction** should now populate the approved topology.

It should:

1. extract the accepted 15 MUDAC Concepts into canonical knowledge documents;
2. identify first-class canonical mechanisms and policies;
3. identify cross-cutting invariants that merit independent stable ownership;
4. extract the Phase 003 experience contracts;
5. link each canonical document to its historical source records;
6. avoid introducing stable rule IDs prematurely where 004-E should define the namespace;
7. preserve semantic parity with the Phase 001–003 exits;
8. surface any discovered contradiction rather than silently normalizing it.

004-C should optimize for **one canonical owner per meaning**, not for mechanically converting every historical Markdown file into a new file.