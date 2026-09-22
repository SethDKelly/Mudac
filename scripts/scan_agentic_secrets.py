#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fnmatch
import re
from pathlib import Path

ROOTS = (
    "AGENTS.md",
    "CLAUDE.md",
    ".agents",
    ".claude",
    ".cursor",
    "knowledge",
    "docs/canonical/governance",
    "docs/routing",
    "docs/018-pre-implementation-repository-qualification-agentic-development-architecture-reentry",
)
TEXT_SUFFIXES = {".md", ".mdc", ".json", ".yaml", ".yml", ".toml", ".txt"}
FORBIDDEN_NAMES = (
    ".env",
    ".env.local",
    ".env.production",
    "*.pem",
    "*.key",
    "*.p12",
    "*.pfx",
    "credentials.json",
    "secrets.json",
    "secrets.yaml",
    "secrets.yml",
    "id_rsa",
    "id_ed25519",
)
SECRET_PATTERNS = (
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("aws access key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("github classic token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("github fine-grained token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{40,}\b")),
    ("openai-style secret key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("anthropic secret key", re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}\b")),
    ("slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("google api key", re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b")),
)
STRUCTURED_SECRET = re.compile(
    r"^\s*[\"']?(password|passwd|secret|api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret)[\"']?\s*[:=]\s*[\"']?([^\"'\s,#}]+)",
    re.IGNORECASE | re.MULTILINE,
)
PLACEHOLDER = ("<", "redacted", "placeholder", "example", "dummy", "changeme", "not-a-secret", "not_secret")


def candidate_files(repo: Path):
    seen: set[Path] = set()
    for rel in ROOTS:
        root = repo / rel
        files = [root] if root.is_file() else ([p for p in root.rglob("*") if p.is_file()] if root.is_dir() else [])
        for path in files:
            if path in seen:
                continue
            seen.add(path)
            yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []
    scanned = 0

    for path in candidate_files(repo):
        rel = path.relative_to(repo)
        if any(fnmatch.fnmatch(path.name, pattern) for pattern in FORBIDDEN_NAMES):
            errors.append(f"{rel}: secret-bearing filename prohibited in agentic/authority surfaces")
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"AGENTS.md", "CLAUDE.md"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        scanned += 1
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"{rel}: high-confidence {label} pattern detected")
        if path.suffix.lower() in {".json", ".yaml", ".yml", ".toml"}:
            for match in STRUCTURED_SECRET.finditer(text):
                value = match.group(2)
                lowered = value.lower()
                if len(value) >= 8 and not any(marker in lowered for marker in PLACEHOLDER):
                    errors.append(f"{rel}: non-placeholder structured secret field {match.group(1)!r} detected")

    for error in errors:
        print("ERROR", error)
    print(f"Agentic/authority secret scan: {len(errors)} error(s), {scanned} text file(s) scanned")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
