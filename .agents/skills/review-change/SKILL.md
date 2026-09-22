---
name: review-change
description: Review a MUDAC change or diff against current canonical authority, task scope, agentic boundaries, evidence obligations, and downstream quarantine. Read-only unless fixes are separately requested.
---
# Review change

## Human-directed boundary

This workflow is **A1**. Finding a defect does not authorize editing it.

## Workflow

1. Identify what the human intended to change and the selected task boundary.
2. Inspect the actual changed files/diff rather than relying only on a prose summary.
3. Resolve affected current owners and stable IDs.
4. Check for semantic drift, candidate architecture leakage, current/history confusion, authority/authorship mistakes, and A1–A4 boundary violations.
5. Check whether validation/evidence is appropriate to the claim being made.
6. Check directly affected routing/status/reference/traceability only where material.
7. Prioritize correctness and risk over style.
8. Report confirmed defects separately from questions, unverified assumptions and optional improvements.

## Stop conditions

Do not edit unless the human separately requests A2 repair work. Do not invent architecture requirements or upgrade static evidence into runtime proof.
