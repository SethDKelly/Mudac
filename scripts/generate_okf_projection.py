#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path

SPEC = "docs/routing/okf_projection.json"
GENERATED_ROOT = "knowledge"


def rel_link(output: str, target: str) -> str:
    start = Path(output).parent
    return os.path.relpath(target, start=start).replace(os.sep, "/")


def q(value: str) -> str:
    return json.dumps(value)


def route_doc(kind: str, route: dict, output: str, generated_at: str) -> str:
    resource = rel_link(output, route["resource"])
    tags = ["mudac", "generated", "routing", "domain" if kind == "domains" else "project", route["role"]]
    return (
        "---\n"
        'type: "MUDAC Routing Reference"\n'
        f"title: {q(route['title'])}\n"
        f"description: {q(route['description'])}\n"
        f"resource: {q(resource)}\n"
        f"tags: [{', '.join(q(tag) for tag in tags)}]\n"
        'status: "stable"\n'
        "sources:\n"
        f"  - resource: {q(resource)}\n"
        f'generated: {{ by: "process:mudac-okf-projection", at: "{generated_at}" }}\n'
        "---\n"
        "# Use\n\n"
        "**GENERATED OKF PROJECTION — DO NOT HAND-EDIT.** Source: `docs/routing/okf_projection.json`.\n\n"
        f"Target role: **{route['role']}**.\n\n"
        f"Primary route: [{route['title']}]({resource}).\n\n"
        "This projection is routing only. It does not establish or upgrade product, design, architecture, implementation, verification, deployment, or execution authority.\n"
    )


def route_index(title: str, routes: list[dict]) -> str:
    body = f"# {title}\n\n**GENERATED OKF PROJECTION — DO NOT HAND-EDIT.**\n\n"
    for route in routes:
        body += f"- [{route['title']}]({route['name']}.md) — {route['description']}\n"
    return body


def render_all(repo: Path) -> dict[str, str]:
    spec = json.loads((repo / SPEC).read_text(encoding="utf-8"))
    if spec.get("status") != "active":
        raise RuntimeError("OKF projection specification is not active")
    if spec.get("authority") != "DERIVED ROUTING ONLY — NOT SEMANTIC AUTHORITY":
        raise RuntimeError("OKF projection authority contract drifted")
    if spec.get("discovery_root") != "docs/index.md" or spec.get("generated_root") != GENERATED_ROOT:
        raise RuntimeError("OKF projection root contract drifted")
    if str(spec.get("okf_version")) != "0.2":
        raise RuntimeError("OKF projection version must be 0.2")
    generated_at = spec["generated_at"]

    for group in ("domains", "project"):
        names = [route["name"] for route in spec[group]]
        if len(names) != len(set(names)):
            raise RuntimeError(f"duplicate OKF projection route name in {group}")
        for route in spec[group]:
            target = repo / route["resource"]
            if not target.exists():
                raise RuntimeError(f"OKF route target does not exist: {route['resource']}")

    files: dict[str, str] = {}
    for route in spec["domains"]:
        rel = f"domains/{route['name']}.md"
        files[rel] = route_doc("domains", route, f"knowledge/{rel}", generated_at)
    for route in spec["project"]:
        rel = f"project/{route['name']}.md"
        files[rel] = route_doc("project", route, f"knowledge/{rel}", generated_at)
    files["domains/index.md"] = route_index("Domain routing", spec["domains"])
    files["project/index.md"] = route_index("Project routing", spec["project"])
    files["index.md"] = '''---
okf_version: "0.2"
---
# MUDAC OKF Routing Projection

**GENERATED OKF PROJECTION — DO NOT HAND-EDIT.**

The authored repository-native discovery root is [`docs/index.md`](../docs/index.md). This `knowledge/` tree is the strict OKF v0.2 compatibility bundle and is **derived routing only**; it cannot establish MUDAC semantic, architecture, implementation, deployment, or execution authority.

- [Domain routes](domains/index.md)
- [Project and lifecycle routes](project/index.md)

For ordinary repository work, follow the authored discovery root and smallest current owner. Historical evidence and suspended downstream candidates are loaded only when the task requires them.
'''

    expected = spec["expected_counts"]
    actual = {
        "domains": len(spec["domains"]),
        "project": len(spec["project"]),
        "route_documents": len(spec["domains"]) + len(spec["project"]),
        "total_markdown_files": len(files),
    }
    for key, value in actual.items():
        if expected.get(key) != value:
            raise RuntimeError(f"OKF projection count drift for {key}: expected {expected.get(key)}, found {value}")
    return files


def check(repo: Path, files: dict[str, str]) -> int:
    root = repo / GENERATED_ROOT
    errors: list[str] = []
    expected = {Path(rel).as_posix() for rel in files}
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*.md")} if root.is_dir() else set()
    for rel in sorted(expected - actual):
        errors.append(f"missing generated OKF file: knowledge/{rel}")
    for rel in sorted(actual - expected):
        errors.append(f"unexpected non-generated OKF file: knowledge/{rel}")
    for rel in sorted(expected & actual):
        if (root / rel).read_text(encoding="utf-8") != files[rel]:
            errors.append(f"generated OKF drift: knowledge/{rel}")
    for error in errors:
        print("ERROR", error)
    print(f"OKF projection check: {len(errors)} error(s), {len(files)} tracked Markdown file(s)")
    return 1 if errors else 0


def write(repo: Path, files: dict[str, str]) -> int:
    root = repo / GENERATED_ROOT
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)
    for rel, content in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Generated {len(files)} OKF projection Markdown file(s) under knowledge/")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    try:
        files = render_all(repo)
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print("ERROR", exc)
        return 1
    return write(repo, files) if args.write else check(repo, files)


if __name__ == "__main__":
    raise SystemExit(main())
