#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def clone_repo(source: Path, parent: Path, name: str) -> Path:
    target = parent / name
    shutil.copytree(
        source,
        target,
        ignore=shutil.ignore_patterns(".git", "node_modules", ".venv", "__pycache__", "*.pyc"),
    )
    return target


def run_script(source_repo: Path, test_repo: Path, script: str, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(source_repo / script), *extra],
        cwd=test_repo,
        text=True,
        capture_output=True,
    )


def expect_failure(label: str, proc: subprocess.CompletedProcess[str], errors: list[str]) -> None:
    if proc.returncode == 0:
        errors.append(f"{label}: negative control unexpectedly passed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    source = Path(args.repo).resolve()
    errors: list[str] = []

    with tempfile.TemporaryDirectory(prefix="mudac-conformance-") as tmp_raw:
        tmp = Path(tmp_raw)

        status_repo = clone_repo(source, tmp, "status")
        agents = status_repo / "AGENTS.md"
        text = agents.read_text(encoding="utf-8")
        import re
        text = re.sub(r"018-[A-M] NEXT", "018-Z NEXT", text)
        agents.write_text(text, encoding="utf-8")
        expect_failure(
            "status mirror drift",
            run_script(source, status_repo, "scripts/validate_status_mirrors.py", "--repo", str(status_repo)),
            errors,
        )

        policy_repo = clone_repo(source, tmp, "policy")
        policy_path = policy_repo / "docs/routing/agentic_action_policy.json"
        policy = json.loads(policy_path.read_text(encoding="utf-8"))
        policy["action_classes"]["A1"]["repository_edits"] = True
        policy_path.write_text(json.dumps(policy, indent=2) + "\n", encoding="utf-8")
        expect_failure(
            "A1 authority corruption",
            run_script(source, policy_repo, "scripts/validate_agentic_authority_policy.py", "--repo", str(policy_repo)),
            errors,
        )

        workflow_repo = clone_repo(source, tmp, "workflow")
        duplicate = workflow_repo / ".claude/skills/resolve-context/SKILL.md"
        duplicate.parent.mkdir(parents=True, exist_ok=True)
        duplicate.write_text(
            (workflow_repo / ".agents/skills/resolve-context/SKILL.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        expect_failure(
            "duplicate provider workflow",
            run_script(source, workflow_repo, "scripts/validate_agent_workflows.py", "--repo", str(workflow_repo)),
            errors,
        )

        okf_repo = clone_repo(source, tmp, "okf")
        okf = okf_repo / "knowledge/index.md"
        okf.write_text(okf.read_text(encoding="utf-8") + "\nDRIFT\n", encoding="utf-8")
        expect_failure(
            "generated OKF drift",
            run_script(source, okf_repo, "scripts/generate_okf_projection.py", "--repo", str(okf_repo), "--check"),
            errors,
        )

        stable_repo = clone_repo(source, tmp, "stable")
        stable = stable_repo / "docs/routing/stable_reference_index.json"
        stable.write_text(stable.read_text(encoding="utf-8") + " ", encoding="utf-8")
        expect_failure(
            "stable-reference index drift",
            run_script(source, stable_repo, "scripts/generate_stable_reference_index.py", "--repo", str(stable_repo), "--check"),
            errors,
        )

        secret_repo = clone_repo(source, tmp, "secret")
        leak = secret_repo / ".agents/leak.txt"
        leak.parent.mkdir(parents=True, exist_ok=True)
        leak.write_text("token=" + "ghp_" + ("A" * 36) + "\n", encoding="utf-8")
        expect_failure(
            "high-confidence secret insertion",
            run_script(source, secret_repo, "scripts/scan_agentic_secrets.py", "--repo", str(secret_repo)),
            errors,
        )

    for error in errors:
        print("ERROR", error)
    print(f"Agentic negative controls: {len(errors)} error(s), 6 guard mutation(s) exercised")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
