@../AGENTS.md

# Claude Code adapter

This file is only a thin bridge to MUDAC's shared repository authority.

- Use `docs/index.md` for repository-native discovery; `knowledge/index.md` is generated OKF compatibility routing only.
- For exact stable IDs use `python scripts/resolve_stable_id.py <ID>`.
- Canonical reusable workflows live only in `.agents/skills/<name>/SKILL.md`.
- Thin command bridges live in `.claude/commands/` and add no workflow semantics.
- Follow the canonical A1–A4 and context-budget contracts from root `AGENTS.md`.
- Do not create duplicate MUDAC workflows under `.claude/skills/`.
- Do not use subagents/agent teams for repository implementation under the current human-directed foundation.
- Memory/chat/tool-native state remains advisory; durable correctness belongs in repository authority/evidence.
