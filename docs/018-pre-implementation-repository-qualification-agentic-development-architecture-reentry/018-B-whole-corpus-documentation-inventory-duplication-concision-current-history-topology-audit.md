---
type: Phase Audit
title: 018-B — Whole-Corpus Documentation Inventory, Duplication, Concision & Current/History Topology Audit
description: "Inventories the full MUDAC documentation corpus, classifies current authority, history, closure evidence, routing, external references and quarantined downstream knowledge, audits exact/current/historical duplication and context burden, repairs bounded lifecycle/routing defects, and identifies topology normalization work that must be deferred to OKF, stable-reference and architecture-candidate qualification."
status: stable
tags: [phase-018, documentation, inventory, duplication, concision, topology, current-truth, history, okf, agent-context]
sources:
  - resource: README.md
  - resource: 018-A-start-gate-closure-baseline-audit-authority-qualification-model-scorecard.md
  - resource: 018-B-documentation-inventory.json
  - resource: ../canonical/index.md
  - resource: ../canonical/governance/documentation-authority.md
  - resource: ../canonical/governance/metadata-trust-lifecycle.md
  - resource: ../canonical/governance/agent-context.md
  - resource: ../canonical/governance/downstream-authority-quarantine.md
  - resource: ../canonical/governance/post-concept-design-reentry.md
---

# Purpose

018-B audits the MUDAC documentation corpus as a **knowledge system** rather than as a sequence of design phases.

Phase 017 already proved that current semantic authority is coherent enough to close Concept Design. 018-B asks a different question:

> Is the repository corpus compact, correctly layered and sufficiently explicit about current truth versus provenance that humans and coding agents can retrieve the minimum sufficient authoritative context without mistaking historical repetition or downstream candidates for current authority?

The audit is repository-wide. It does not treat file count or document size as defects by themselves.

# 1. Audit method and entry snapshot

018-B used the recursive `main` repository tree as its entry snapshot and classified every Markdown artifact under `docs/`.

The durable machine-readable entry snapshot is:

- [018-B-documentation-inventory.json](018-B-documentation-inventory.json)

That snapshot intentionally records the corpus **before** 018-B audit records and repairs were added. It is evidence of the state being audited, not a continuously self-referential manifest.

Entry snapshot:

~~~text
Markdown files                    307
Markdown bytes              4,559,813
exact duplicate blob bodies        0
~~~

Approximate corpus distribution:

| Classification | Files | Bytes | Role |
| --- | ---: | ---: | --- |
| Phase 001–016 historical design evidence | 175 | 3,503,437 | provenance / rationale / accepted-era evidence |
| Phase 017 closure evidence | 10 | 174,401 | Concept Design closure proof |
| Phase 018 active qualification evidence | 3 | 34,851 | active post-closure program at audit entry |
| current canonical owners | 81 | 564,308 | current semantic/governance rule bodies |
| quarantined architecture/implementation candidates | 17 | 227,377 | downstream candidate knowledge |
| historical/deprecated adapters within canonical families | 6 | 26,882 | link/provenance continuity |
| routing/index surfaces | 12 | 22,126 | progressive disclosure |
| external reference/profile material | 3 | 6,431 | adopted/profiled external authorities |

The corpus is therefore large primarily because MUDAC preserves design evidence. Numbered phase material represented about **81% of Markdown bytes** at entry.

That is not itself a documentation defect.

# 2. Whole-corpus role classification

018-B adopts the following role model.

## Current canonical owner

A current rule body with a natural semantic/governance ownership responsibility.

At audit entry, 81 Markdown files meet this role after excluding routing indexes, quarantined downstream candidates and explicit historical adapters.

## Router / index

A progressive-disclosure surface that tells a human or tool where authority lives.

Routers may summarize lifecycle posture compactly, but must not become competing rule stores.

## Historical phase evidence

Phase 001–016 records preserve rationale, rejected alternatives, prior accepted states, refinement and validation evidence.

They remain stable evidence in their historical role even when their former current rules have been superseded.

## Closure evidence

Phase 017 records prove the final Jackson-aligned Concept Design closure and downstream handoff.

They do not become current semantic owners merely because they are later than a canonical owner.

## Active qualification evidence

Phase 018 records the current pre-implementation repository qualification program.

It is process/qualification authority only where explicitly stated and cannot override product-semantic owners.

## Downstream candidate knowledge

The `canonical/architecture/` and `canonical/implementation/` subtrees preserve pre-closure architecture and implementation decisions for later qualification.

They are physically located below `canonical/` but remain suspended/quarantined.

## Historical adapter

A superseded document intentionally kept addressable to preserve links and explain a semantic transition.

Adapters may not compete with the current successor.

## External reference

Adopted/profiled external methodology or standard material under `docs/references/`.

# 3. Duplication audit

018-B distinguishes several kinds of duplication.

## 3.1 Exact byte-identical duplication

**Finding: NONE.**

The entry snapshot contains no duplicate Markdown blob SHA across the corpus.

This means the repository is not suffering from simple copied-file duplication.

## 3.2 Historical semantic repetition

**Finding: EXPECTED / ACCEPTED.**

The same product concerns recur across numbered phases because later phases test, refine, repair or validate earlier work.

Examples include:

- evaluation authority;
- finalization/outcome officiality;
- correction/history;
- accessibility/degraded operation;
- Export/Publication;
- synchronization and application actions.

Deleting those repetitions would destroy design provenance.

Historical repetition becomes a problem only when normal current retrieval treats it as competing current authority.

## 3.3 Current-authority duplication

**Finding: NO NEW COMPETING CURRENT OWNER IDENTIFIED.**

Phase 017 closed with zero current-owner conflicts. 018-B found no evidence requiring that conclusion to be reopened.

The canonical family topology remains defensible:

~~~text
Project
Concepts
Synchronizations
Dependence
Experience
Mechanisms
Policies
Invariants
Governance
~~~

No current owner merge/split is required merely for concision.

## 3.4 Router/status repetition

**Finding: ACCEPTABLE BUT DRIFT-PRONE.**

Lifecycle posture is repeated in several deliberately small bootstrap surfaces, including:

- root `README.md`;
- `docs/index.md`;
- `docs/README.md`;
- `AGENTS.md`;
- `docs/canonical/index.md`;
- active phase indexes.

This repetition improves entry-point usability but creates status-drift risk.

018-B does not collapse these surfaces because each has a legitimate routing audience. 018-D/H should make lifecycle status mirrors machine-checkable or derivable from one declared current status source.

## 3.5 Historical adapters within canonical families

**Finding: SIX FILES / 26,882 BYTES — EXPLICIT BUT PHYSICALLY AMBIGUOUS.**

The six adapters are:

- `canonical/concepts/judging-encounter.md`;
- `canonical/mechanisms/official-outcome-revision.md`;
- `canonical/synchronizations/concept-synchronizations.md`;
- `canonical/experience/paper-export-publication.md`;
- `canonical/experience/reconciliation-finalization.md`;
- `canonical/experience/phase-013-entry-handoff.md`.

All explicitly deny current semantic authority or route to a current successor.

Their physical location under `canonical/` can nevertheless increase naive-search ambiguity.

018-B does **not** move them yet. Physical relocation must preserve stable links, source lineage and historical lookup behavior and therefore belongs after 018-C/D qualify OKF and stable-reference mechanics.

## 3.6 Quarantined downstream material inside the canonical namespace

**Finding: MATERIAL TOPOLOGY PRESSURE.**

The architecture and implementation subtrees contain:

~~~text
files                         17
bytes                    227,377
share of canonical bytes     27.3%
~~~

They are explicitly suspended and controlled by quarantine/re-entry governance.

However, a tool that gives path location excessive weight could still misread:

~~~text
docs/canonical/architecture/*
docs/canonical/implementation/*
~~~

as accepted current authority.

This is the most important physical-topology concern found by 018-B.

018-B does not move these trees because:

1. Phase 018-J must qualify the candidates before deciding their durable disposition;
2. stable architecture/implementation rule IDs and links exist;
3. premature relocation would create churn before 018-C/D define the long-term routing/reference model;
4. physical location does not currently override the explicit quarantine.

Disposition:

> **DEFER PHYSICAL RELOCATION DECISION TO 018-C/D/J; KEEP EXPLICIT QUARANTINE ACTIVE.**

# 4. Concision and document-size audit

Current canonical owner bodies are much smaller than the historical phase corpus.

After excluding indexes, historical adapters and downstream candidates:

~~~text
current canonical owner files          81
current owner files >= 15 KB            7
~~~

Largest current owner bodies at audit entry include:

| Owner | Bytes | Finding |
| --- | ---: | --- |
| `governance/rule-identifiers.md` | 32,558 | large structured registry; not prose-bloat evidence |
| `synchronizations/temporal-truth-correction.md` | 17,283 | coherent cross-concept synchronization owner |
| `synchronizations/competition-participation-access.md` | 16,944 | coherent composition owner |
| `synchronizations/evaluation-outcome-finalization-declaration.md` | 16,028 | coherent composition owner |
| `experience/action-authority-traceability.md` | 15,600 | cross-owner mapping integrity owner |
| `project/domain-vocabulary-expectation-transfer.md` | 15,269 | vocabulary/expectation-transfer owner |
| `governance/post-concept-design-reentry.md` | 15,116 | current downstream boundary owner |

018-B finds **no size-only reason to split these owners**.

The 32 KB rule registry is an automation candidate rather than an immediate split candidate. 018-D/H should determine whether deterministic lookup or generated views can reduce agent context without duplicating semantic authority.

# 5. Current/history topology defects found and repaired

018-B found several concrete defects whose meaning was already unambiguous.

## B-N01 — stale Architecture lifecycle language

The Architecture index still described Concept Design as reopened and Phase 017 closure as future.

**Disposition: REPAIRED.**

It now states that Concept Design closed in Phase 017, Phase 018 is active preparation, and candidate architecture still requires explicit downstream adoption.

## B-N02 — stale Implementation lifecycle language

The Implementation index still reported:

~~~text
Jackson Concept Design: IN PROGRESS — PHASE 017
implementation readiness: NOT READY
~~~

**Disposition: REPAIRED.**

It now reflects closed Concept Design, active Phase 018 qualification, readiness for post-closure preparation, no accepted implementation plan, and no execution authorization.

## B-N03 — invalid historical lifecycle metadata

Two Experience evidence adapters used:

~~~yaml
status: historical
~~~

while the repository OKF profile permits:

~~~text
draft | stable | deprecated
~~~

and already defines `deprecated` as the lifecycle state for a replaced canonical artifact retained for links/history.

Affected:

- `experience/paper-export-publication.md`;
- `experience/reconciliation-finalization.md`.

**Disposition: REPAIRED TO `status: deprecated`.**

Their current-successor routes were already explicit.

## B-N04 — historical Phase-013 handoff in current Experience authority chain

`experience/mapping-authority-baseline.md` included the historical Phase-013 Mapping Entry Authority inside the displayed current authority precedence.

That file is explicitly deprecated historical start-gate evidence.

**Disposition: REPAIRED.**

The current mapping chain now routes directly from current upstream authority into the current mapping baseline and accepted Experience owners. The historical handoff remains a provenance source only.

## B-N05 — canonical family indexes pointed to Phase 017 as current methodology status

Several family indexes still routed "current methodology status" to Phase 017.

Phase 017 remains the closure-evidence owner, but Phase 018 is now active post-closure qualification.

**Disposition: REPAIRED.**

Current indexes now distinguish:

- Phase 017 → Concept Design closure/repair evidence;
- Phase 018 → active post-closure repository qualification.

# 6. Normalization register

| ID | Finding | Disposition |
| --- | --- | --- |
| B-N01 | 81% of corpus bytes are numbered-phase evidence | ACCEPT — provenance, not active-rule duplication |
| B-N02 | no exact duplicate Markdown blobs | PASS |
| B-N03 | no newly discovered competing current semantic owner | PASS |
| B-N04 | Architecture index had stale pre-closure lifecycle posture | REPAIRED |
| B-N05 | Implementation index had stale pre-closure lifecycle posture | REPAIRED |
| B-N06 | two invalid `status: historical` values | REPAIRED TO `deprecated` |
| B-N07 | historical Phase-013 handoff appeared in current Experience authority chain | REPAIRED |
| B-N08 | six historical adapters remain physically within canonical families | DEFER MOVE/RETIRE DECISION TO 018-C/D |
| B-N09 | 17 quarantined architecture/implementation files occupy 27.3% of canonical bytes | DEFER PHYSICAL TOPOLOGY DECISION TO 018-C/D/J |
| B-N10 | lifecycle status is mirrored across several bootstrap routers | ACCEPT TEMPORARILY; ADD DRIFT CONTROL IN 018-D/H |
| B-N11 | rule-ID registry is a 32 KB current-owner outlier | KEEP; EVALUATE RESOLVER/GENERATED VIEW IN 018-D/H |
| B-N12 | seven current-owner files exceed 15 KB | NO SIZE-ONLY SPLIT; NATURAL OWNERSHIP REMAINS COHERENT |
| B-N13 | family indexes did not distinguish Phase-017 closure from active Phase 018 | REPAIRED |
| B-N14 | historical phase bodies contain repeated current vocabulary | ACCEPT; AGENT RETRIEVAL MUST FILTER BY AUTHORITY ROLE |

# 7. Why 018-B does not aggressively delete or move documentation

A superficially smaller repository could be a worse design repository.

018-B rejects these cleanup shortcuts:

- deleting historical phase evidence because canonical current owners now exist;
- merging conceptually distinct canonical owners merely to reduce file count;
- moving architecture/implementation candidates before their stable references and later qualification are understood;
- replacing current owners with one monolithic final specification;
- generating summaries that become a second semantic-authority plane;
- rewriting early phase files merely to modernize terminology.

The optimization target is **retrieval cost and authority clarity**, not minimum file count.

# 8. Progressive-disclosure finding

The current retrieval direction remains sound:

~~~text
docs/index.md
  ↓
canonical/index.md
  ↓
smallest relevant family
  ↓
natural current owner
  ↓
linked current dependency only when needed
  ↓
history only for rationale/provenance
~~~

The problem is therefore not a missing knowledge architecture.

The remaining work is to make that architecture more deterministic and machine-efficient.

# 9. Agentic context implications

018-B establishes four requirements for later agentic work.

## AC-B1 — path does not equal authority

A file under `docs/canonical/` may still be:

- deprecated historical adapter;
- suspended downstream candidate;
- router/index.

Agents must resolve role/authority, not infer authority from path alone.

## AC-B2 — search frequency does not equal authority

Historical phase evidence is the majority of repository text.

A naive full-text search can therefore return superseded vocabulary more often than current vocabulary.

Current-owner resolution must precede broad historical search for ordinary implementation tasks.

## AC-B3 — history loading must be opt-in by need

Normal implementation work should not preload numbered phases.

History is appropriate for:

- rationale;
- rejected alternatives;
- provenance;
- semantic-change investigation;
- repair propagation;
- audit.

## AC-B4 — status mirrors need drift enforcement

Because several small entry surfaces legitimately repeat lifecycle posture, automated consistency checks are preferable to deleting useful entry-point context.

# 10. 018-C handoff questions

018-C should now qualify the OKF model against the actual corpus rather than an abstract desired structure.

It must answer at least:

1. Should `docs/` remain the single authored repository-native knowledge plane?
2. Would a generated OKF compatibility projection improve generic-tool consumption without creating dual authority?
3. How should deprecated/historical adapters be represented and eventually relocated without breaking references?
4. Should downstream architecture/implementation candidates remain physically under `canonical/`, move to an explicit candidate/history namespace, or remain until 018-J disposition?
5. Which OKF metadata fields materially aid retrieval, trust and lifecycle behavior?
6. How should `stable` metadata be interpreted for suspended downstream candidates so it cannot imply semantic acceptance?
7. Which routing/status surfaces should be authored and which, if any, should be generated?
8. What machine-readable artifact should become the long-term owner/role inventory after this 018-B snapshot?

# 11. Gate evaluation

| Phase-018 gate | 018-B result |
| --- | --- |
| P18-G1 semantic preservation | PASS — no product semantics changed |
| P18-G2 current/history integrity | PASS WITH FOLLOW-ON — bounded topology ambiguity classified |
| P18-G3 documentation economy | PASS FOR AUDIT — material pressure identified; unsafe cleanup avoided |
| P18-G4 OKF qualification | NOT YET — 018-C |
| P18-G5 deterministic routing | PARTIAL — role inventory exists; 018-D owns final mechanics |
| P18-G7 context proportionality | BASELINE ESTABLISHED — 018-F owns measurable policy |
| P18-G8 conformance proportionality | PARTIAL — metadata defect exposed; 018-H owns expanded enforcement |
| P18-G10 architecture re-entry integrity | PASS — candidate trees remained quarantined |
| P18-G12 execution boundary | PASS — no feature implementation performed |

# 12. Exit decision

**018-B — COMPLETE — PASS WITH EXPLICIT TOPOLOGY CARRY-FORWARD.**

The corpus does **not** require broad deletion, phase-history compression or a canonical-owner rewrite.

The significant remaining topology questions are now bounded:

~~~text
historical adapters under canonical       6 files
downstream candidates under canonical    17 files / 27.3% canonical bytes
status mirrors                            useful but drift-prone
stable-ID registry                        useful but context-heavy
current owner splits/merges               none required by 018-B
exact duplicate files                     0
current-owner conflicts                   0 newly identified
~~~

The next authorized work is:

> **018-C — OKF v0.2 Conformance, Progressive Disclosure, Metadata & Knowledge-Bundle Qualification**

018-C should decide the durable knowledge-bundle/profile/projection model before 018-D codifies deterministic ownership and stable-reference resolution.
