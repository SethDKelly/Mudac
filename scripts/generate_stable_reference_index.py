#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

POLICY = "docs/routing/canonical_ownership.json"
OUTPUT = "docs/routing/stable_reference_index.json"
REGISTRY_ENTRY_RE = re.compile(r"^\s*[*-]\s+\[([A-Z][A-Z0-9]*-\d{3})[^\]]*\]\(([^)]+)\)\s*$", re.MULTILINE)
ANCHOR_RE_TEMPLATE = r'<a\s+id=["\']{anchor}["\']\s*>\s*</a>'
STATUS_RE = re.compile(r"^status:\s*([^#\n]+?)\s*$", re.MULTILINE)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(repo: Path, source: Path, raw: str) -> tuple[str, str]:
    target, sep, fragment = raw.partition("#")
    path = (source.parent / target).resolve()
    try:
        rel = path.relative_to(repo).as_posix()
    except ValueError as exc:
        raise RuntimeError(f"registry target leaves repository: {raw}") from exc
    return rel, fragment.lower() if sep else ""


def under(path: str, root: str) -> bool:
    return path == root or path.startswith(root.rstrip("/") + "/")


def frontmatter_status(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    match = STATUS_RE.search(text[4:end])
    if not match:
        return None
    return match.group(1).strip().strip('"\'')


def classify(repo: Path, rel: str, policy: dict) -> str:
    if rel in set(policy.get("historical_adapter_paths", [])):
        return "historical-adapter"
    for root in policy.get("downstream_candidate_roots", []):
        if under(rel, root):
            return "downstream-candidate"
    for root in policy.get("current_owner_roots", []):
        if under(rel, root):
            if frontmatter_status(repo / rel) == "deprecated":
                return "deprecated-adapter"
            return "current-authority"
    if under(rel, policy.get("external_reference_root", "__none__")):
        return "external-reference"
    return "unresolved"


def render(repo: Path) -> dict:
    policy = load_json(repo / POLICY)
    registry_rel = policy["stable_reference_registry"]
    registry = repo / registry_rel
    text = registry.read_text(encoding="utf-8")

    refs: dict[str, dict] = {}
    for match in REGISTRY_ENTRY_RE.finditer(text):
        stable_id = match.group(1).upper()
        if stable_id in refs:
            raise RuntimeError(f"duplicate stable ID in registry: {stable_id}")
        rel, fragment = normalize(repo, registry, match.group(2).strip())
        expected_fragment = stable_id.lower()
        if fragment != expected_fragment:
            raise RuntimeError(f"{stable_id} registry fragment must be #{expected_fragment}; got #{fragment}")
        target = repo / rel
        if not target.is_file():
            raise RuntimeError(f"{stable_id} target does not exist: {rel}")
        target_text = target.read_text(encoding="utf-8")
        anchor_re = re.compile(ANCHOR_RE_TEMPLATE.format(anchor=re.escape(expected_fragment)), re.IGNORECASE)
        if not anchor_re.search(target_text):
            raise RuntimeError(f"{stable_id} target lacks explicit anchor #{expected_fragment}: {rel}")
        role = classify(repo, rel, policy)
        if role == "unresolved":
            raise RuntimeError(f"{stable_id} target has unresolved ownership role: {rel}")
        refs[stable_id] = {
            "owner_path": rel,
            "anchor": expected_fragment,
            "role": role,
            "locator": f"{rel}#{expected_fragment}",
        }

    by_role: dict[str, int] = {}
    by_family: dict[str, int] = {}
    for stable_id, item in refs.items():
        by_role[item["role"]] = by_role.get(item["role"], 0) + 1
        family = stable_id.split("-", 1)[0]
        by_family[family] = by_family.get(family, 0) + 1

    return {
        "schema_version": "1.0",
        "authority": "DERIVED ROUTING ONLY — CANONICAL OWNER FILES RETAIN SEMANTIC AUTHORITY",
        "source_registry": registry_rel,
        "ownership_policy": POLICY,
        "summary": {
            "total": len(refs),
            "by_role": {key: by_role[key] for key in sorted(by_role)},
            "by_family": {key: by_family[key] for key in sorted(by_family)},
        },
        "references": {key: refs[key] for key in sorted(refs)},
    }


def serialized(payload: dict) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    try:
        body = serialized(render(repo))
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print("ERROR", exc)
        return 1
    output = repo / OUTPUT
    if args.write:
        output.write_text(body, encoding="utf-8")
        print(f"Wrote {OUTPUT}")
        return 0
    if not output.is_file():
        print(f"ERROR missing generated stable-reference index: {OUTPUT}")
        return 1
    actual = output.read_text(encoding="utf-8")
    if actual != body:
        print(f"ERROR generated stable-reference index drift: {OUTPUT}")
        return 1
    payload = json.loads(body)
    print(f"Stable-reference index check: 0 errors, {payload['summary']['total']} stable ID(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
