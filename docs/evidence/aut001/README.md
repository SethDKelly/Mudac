# AUT-E03 live shadow evidence reference

This directory is the declared AUT-E03 `retention_or_reference` surface.

Normative machine contract:

- [`aut-e03-live-shadow-reference-contract.json`](./aut-e03-live-shadow-reference-contract.json)

## Rules

- A green `AUT-001 Read-Only Shadow` workflow means the bounded window reached terminal `PASS` with no blocking divergence, timeout, mutation, or structural failure.
- Workflow conclusion alone cannot qualify AUT-E03.
- Missing, expired, or unretrievable retained evidence is `INCONCLUSIVE`, not `PASS`.
- Exact candidate SHA / artifact identity is bound externally after the final candidate exists. This contract deliberately does not embed a final candidate SHA, to avoid a self-referential hash cycle.
- Read-only GitHub behavior remains mandatory. Artifact upload is evidence retention infrastructure, not repository coordination write authority.
