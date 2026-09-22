#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

MANIFEST = "docs/routing/agent_tool_compatibility.json"
WORKFLOW_CONTRACT = "docs/canonical/governance/agent-workflow-portability.md"
SKILLS = (
    "resolve-context",
    "resolve-contract",
    "execute-selected-task",
    "review-change",
    "run-conformance",
    "update-traceability",
    "exit-review",
)
TOP_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")
ALLOWED_FRONTMATTER = {"name", "description"}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML frontmatter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("unterminated YAML frontmatter") from exc
    data: dict[str, str] = {}
    for line in lines[1:end]:
        match = TOP_KEY.match(line)
        if match:
            data[match.group(1)] = match.group(2).strip().strip("\"'")
    return data, "\n".join(lines[end + 1 :])


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    try:
        manifest = json.loads((repo / MANIFEST).read_text(encoding="utf-8"))
        budget = json.loads((repo / "docs/routing/context_budget.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print("ERROR", exc)
        return 1

    canonical = manifest.get("canonical", {})
    expected = {
        "shared_instructions": "AGENTS.md",
        "agentic_authority": "docs/canonical/governance/agentic-authority-scope.md",
        "context_policy": "docs/canonical/governance/agent-context.md",
        "workflow_contract": WORKFLOW_CONTRACT,
        "workflow_root": ".agents/skills",
        "knowledge_entry": "docs/index.md",
        "okf_compatibility_entry": "knowledge/index.md",
    }
    for key, value in expected.items():
        if canonical.get(key) != value:
            errors.append(f"manifest canonical.{key} must equal {value!r}")

    expected_classes = {
        "resolve-context": "A1",
        "resolve-contract": "A1",
        "execute-selected-task": "A2",
        "review-change": "A1",
        "run-conformance": "A1",
        "update-traceability": "A2",
        "exit-review": "A1/A2-record-only",
    }
    if set(manifest.get("skills", {})) != set(SKILLS):
        errors.append("manifest skill set drift")
    for name, action_class in expected_classes.items():
        if manifest.get("skills", {}).get(name, {}).get("action_class") != action_class:
            errors.append(f"manifest skill {name} action_class drift")

    skill_limit = int(budget["hard_limits"]["future_canonical_skill_each"])
    for name in SKILLS:
        path = repo / ".agents" / "skills" / name / "SKILL.md"
        if not path.is_file():
            errors.append(f"missing canonical skill: {path.relative_to(repo)}")
            continue
        text = path.read_text(encoding="utf-8")
        if len(text.encode("utf-8")) > skill_limit:
            errors.append(f"{path.relative_to(repo)} exceeds {skill_limit} byte skill budget")
        try:
            meta, body = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(f"{path.relative_to(repo)}: {exc}")
            continue
        if meta.get("name") != name:
            errors.append(f"{path.relative_to(repo)} name must equal {name!r}")
        if not meta.get("description"):
            errors.append(f"{path.relative_to(repo)} requires description")
        extras = sorted(set(meta) - ALLOWED_FRONTMATTER)
        if extras:
            errors.append(f"{path.relative_to(repo)} has non-portable frontmatter: {', '.join(extras)}")
        for heading in ("Human-directed boundary", "Workflow", "Stop conditions"):
            if heading not in body:
                errors.append(f"{path.relative_to(repo)} missing section: {heading}")

        bridge = repo / ".claude" / "commands" / f"{name}.md"
        if not bridge.is_file():
            errors.append(f"missing Claude bridge: {bridge.relative_to(repo)}")
        else:
            bt = bridge.read_text(encoding="utf-8")
            canonical_path = f".agents/skills/{name}/SKILL.md"
            if canonical_path not in bt:
                errors.append(f"{bridge.relative_to(repo)} must point to {canonical_path}")
            if len(bt.encode("utf-8")) > int(budget["hard_limits"]["claude_command_each"]):
                errors.append(f"{bridge.relative_to(repo)} exceeds thin bridge budget")

        for duplicate in (
            repo / ".claude" / "skills" / name / "SKILL.md",
            repo / ".cursor" / "skills" / name / "SKILL.md",
            repo / ".codex" / "skills" / name / "SKILL.md",
        ):
            if duplicate.exists():
                errors.append(f"duplicate workflow source: {duplicate.relative_to(repo)}")

    claude_path = repo / "CLAUDE.md"
    if not claude_path.is_file():
        errors.append("missing root CLAUDE.md")
    else:
        text = claude_path.read_text(encoding="utf-8")
        if "@AGENTS.md" not in text:
            errors.append("CLAUDE.md must import AGENTS.md")
        if ".agents/skills/" not in text:
            errors.append("CLAUDE.md must route to .agents/skills")
        if len(text.encode("utf-8")) > int(budget["hard_limits"]["claude_md"]):
            errors.append("CLAUDE.md exceeds adapter budget")

    cursor = repo / ".cursor" / "rules" / "00-mudac-routing.mdc"
    if not cursor.is_file():
        errors.append("missing Cursor routing adapter")
    else:
        text = cursor.read_text(encoding="utf-8")
        if re.search(r"(?mi)^alwaysApply:\s*true\s*$", text):
            errors.append("Cursor routing adapter must not be alwaysApply true")
        for token in ("AGENTS.md", ".agents/skills", "resolve_stable_id.py", "agentic-authority-scope.md"):
            if token not in text:
                errors.append(f"Cursor routing adapter missing {token}")
        if len(text.encode("utf-8")) > int(budget["hard_limits"]["cursor_rule_each"]):
            errors.append("Cursor routing adapter exceeds per-rule budget")

    for forbidden in (repo / "CODEX.md", repo / ".codex" / "AGENTS.md"):
        if forbidden.exists():
            errors.append(f"duplicate Codex semantic adapter prohibited: {forbidden.relative_to(repo)}")

    tools = manifest.get("tools", {})
    if set(tools) != {"codex", "cursor", "claude_code"}:
        errors.append("tool manifest must contain codex, cursor, claude_code")
    for name, item in tools.items():
        if item.get("runtime_status") != "not-smoke-verified-by-repository":
            errors.append(f"{name}: runtime_status must remain unverified until actual smoke evidence exists")
        if item.get("duplicate_semantic_adapter") != "none":
            errors.append(f"{name}: duplicate semantic adapter is prohibited")

    contract = (repo / WORKFLOW_CONTRACT).read_text(encoding="utf-8")
    for i in range(1, 13):
        token = f"WFL-{i:03d}"
        if f'id="{token.lower()}"' not in contract:
            errors.append(f"workflow contract missing {token}")

    for error in errors:
        print("ERROR", error)
    print(f"Agent workflow/adapter validation: {len(errors)} error(s), {len(SKILLS)} canonical skill(s), 3 tool profile(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
