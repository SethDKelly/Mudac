#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

CHECKS = (
    ("authored knowledge structure", "scripts/validate_knowledge.py", ("--root", "{repo}")),
    ("generated OKF projection", "scripts/generate_okf_projection.py", ("--repo", "{repo}", "--check")),
    ("generated owner inventory", "scripts/generate_owner_inventory.py", ("--repo", "{repo}", "--check")),
    ("generated stable-reference index", "scripts/generate_stable_reference_index.py", ("--repo", "{repo}", "--check")),
    ("agentic authority policy", "scripts/validate_agentic_authority_policy.py", ("--repo", "{repo}")),
    ("context budgets", "scripts/measure_context_budget.py", ("{repo}",)),
    ("portable skills and tool adapters", "scripts/validate_agent_workflows.py", ("--repo", "{repo}")),
    ("status mirror drift", "scripts/validate_status_mirrors.py", ("--repo", "{repo}")),
    ("stable-resolution behavior", "scripts/validate_resolution_smoke.py", ("--repo", "{repo}")),
    ("downstream candidate qualification", "scripts/validate_candidate_qualification.py", ("--repo", "{repo}")),
    ("architecture re-entry plan", "scripts/validate_architecture_reentry_plan.py", ("--repo", "{repo}")),
    ("implementation program framework", "scripts/validate_implementation_program_framework.py", ("--repo", "{repo}")),
    ("Phase 019 architecture decision control", "scripts/validate_phase019_architecture_control.py", ("--repo", "{repo}")),
    ("Phase 020 implementation design control", "scripts/validate_phase020_implementation_design_control.py", ("--repo", "{repo}")),
    ("Phase 021 start gate", "scripts/validate_phase021_start_gate.py", ("--repo", "{repo}")),
    ("agentic/authority secret scan", "scripts/scan_agentic_secrets.py", ("--repo", "{repo}")),
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--report")
    parser.add_argument("--skip-negative-controls", action="store_true")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    checks = list(CHECKS)
    if not args.skip_negative_controls:
        checks.append(
            ("cross-cutting negative controls", "scripts/test_agentic_conformance_guards.py", ("--repo", "{repo}"))
        )

    results: list[tuple[str, int, str]] = []
    for name, rel, raw_args in checks:
        expanded = [value.format(repo=str(repo)) for value in raw_args]
        proc = subprocess.run(
            [sys.executable, str(repo / rel), *expanded],
            cwd=repo,
            text=True,
            capture_output=True,
        )
        output = (proc.stdout + proc.stderr).strip()
        results.append((name, proc.returncode, output))
        print(("PASS" if proc.returncode == 0 else "FAIL"), name)
        if output:
            print(output)

    manifest = json.loads((repo / "docs/routing/agent_tool_compatibility.json").read_text(encoding="utf-8"))
    overall = "PASS" if all(code == 0 for _, code, _ in results) else "FAIL"
    lines = [
        "# MUDAC Agentic / Documentation Conformance Report",
        "",
        f"**Repository configuration conformance:** {overall}",
        "",
        "> This report covers repository documentation/agentic configuration only. It is not product runtime, provider-agent runtime, deployment or production evidence.",
        "",
        "## Checks",
        "",
        "| Check | Result |",
        "| --- | --- |",
    ]
    lines.extend(f"| {name} | {'PASS' if code == 0 else 'FAIL'} |" for name, code, _ in results)
    lines.extend(["", "## Provider runtime evidence", ""])
    for tool, data in manifest["tools"].items():
        lines.append(
            f"- **{tool}:** repository configuration '{data.get('repository_configuration_status', 'unknown')}'; "
            f"runtime '{data.get('runtime_status', 'unknown')}'."
        )
    lines.extend([
        "",
        "## Evidence boundary",
        "",
        "- Static repository PASS does not establish provider runtime obedience.",
        "- Static repository PASS does not establish MUDAC domain implementation correctness.",
        "- Static repository PASS does not establish deployment or production readiness.",
        "",
    ])
    report = "\n".join(lines)
    if args.report:
        path = Path(args.report)
        if not path.is_absolute():
            path = repo / path
        path.write_text(report, encoding="utf-8")
    print(report)
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
