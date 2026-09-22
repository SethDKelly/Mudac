---
name: run-conformance
description: Run and report the safe deterministic MUDAC checks appropriate to the current human-selected scope. Normally read-only; failures do not authorize fixes or requirement changes.
---
# Run conformance

## Human-directed boundary

This workflow is normally **A1**, although it may execute safe non-destructive validators/tests. Fixes require an enclosing human-selected A2 task.

## Workflow

1. Resolve the selected task and evidence claim.
2. Choose the lowest-cost repository-defined checks that actually bear on that claim.
3. For repository knowledge/agentic configuration, run `python scripts/run_agentic_conformance.py`; use `.github/workflows/knowledge-validation.yml` as the CI invocation authority.
4. Run safe local/static checks available in the environment.
5. Record PASS, FAIL, SKIPPED or UNAVAILABLE faithfully.
6. Distinguish documentation/static evidence from executable integration/runtime and production evidence.
7. Report environment limitations separately from repository defects.
8. Never rewrite a requirement merely to convert failure into pass.

## Stop conditions

Stop before A3 external/destructive actions. Route A4 conflicts through canonical change governance. Do not edit files unless separately authorized.
