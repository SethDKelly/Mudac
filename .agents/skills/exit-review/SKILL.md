---
name: exit-review
description: Evaluate one human-selected MUDAC phase, subphase, package, or bounded program against its documented exit gates and evidence. May record the decision only when explicitly requested.
---
# Exit review

## Human-directed boundary

Evaluation is **A1**. If the human explicitly requests repository recording of the exit, that bounded status/evidence update is **A2**. The workflow never starts the next item.

## Workflow

1. Identify the exact selected boundary and its acceptance/exit criteria.
2. Resolve governing current owners, stable IDs and evidence standards.
3. Inspect delivered artifacts and actual repository state.
4. Classify available evidence accurately: documentation/static, executable, integration/runtime, external/manual, unavailable.
5. Evaluate mandatory criteria independently as PASS, FAIL, DEGRADED/WAIVED only where allowed, or UNVERIFIED.
6. Confirm non-goals/deferred work did not leak into accepted scope.
7. If recording was explicitly requested, update only the directly affected exit/status artifacts and validate them.
8. State the exit decision, residual obligations and next eligible work as information only.

## Stop conditions

Do not self-waive mandatory criteria, manufacture evidence, equate static proof with runtime proof, or begin the next phase/package after acceptance.
