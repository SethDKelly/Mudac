#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

PHASE018_INDEX = "docs/018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/index.md"
PHASE019_INDEX = "docs/019-architecture-engineering-reentry/index.md"
PHASE020_INDEX = "docs/020-autonomous-implementation-program-design-verification-v1-delivery/index.md"

PHASE018_MIRRORS = (
    "README.md",
    "docs/index.md",
    "docs/README.md",
    "AGENTS.md",
    "docs/canonical/index.md",
    "docs/017-methodology-closure-canonical-consolidation-completion-decision/index.md",
    "docs/canonical/implementation/index.md",
    "docs/018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/README.md",
)
PHASE019_MIRRORS = (
    "README.md",
    "docs/index.md",
    "docs/README.md",
    "AGENTS.md",
    "docs/canonical/index.md",
    "docs/canonical/architecture/index.md",
    "docs/canonical/implementation/index.md",
    "docs/018-pre-implementation-repository-qualification-agentic-development-architecture-reentry/index.md",
    "docs/019-architecture-engineering-reentry/README.md",
)
PHASE020_MIRRORS = (
    "README.md",
    "docs/index.md",
    "docs/README.md",
    "AGENTS.md",
    "docs/canonical/index.md",
    "docs/canonical/implementation/index.md",
    "docs/019-architecture-engineering-reentry/index.md",
    "docs/019-architecture-engineering-reentry/README.md",
    "docs/020-autonomous-implementation-program-design-verification-v1-delivery/README.md",
)

P18_ALL = [chr(code) for code in range(ord("A"), ord("M") + 1)]
P19_ALL = [chr(code) for code in range(ord("A"), ord("L") + 1)]
P20_ALL = [chr(code) for code in range(ord("A"), ord("L") + 1)]

P18_COMPLETE_RE = re.compile(r"^- \[018-([A-M])\b.*?— \*\*COMPLETE\b", re.MULTILINE)
P18_NEXT_RE = re.compile(r"^- (?:\[)?018-([A-M])\b.*?— \*\*NEXT\*\*", re.MULTILINE)
P19_COMPLETE_RE = re.compile(r"^- \[019-([A-L])\b.*?— \*\*COMPLETE\b", re.MULTILINE)
P19_NEXT_RE = re.compile(r"^- (?:\[)?019-([A-L])\b.*?— \*\*NEXT ELIGIBLE\*\*", re.MULTILINE)
P20_COMPLETE_RE = re.compile(r"^- \[020-([A-L])\b.*?— \*\*COMPLETE\b", re.MULTILINE)
P20_NEXT_RE = re.compile(r"^- (?:\[)?020-([A-L])\b.*?— \*\*NEXT ELIGIBLE\*\*", re.MULTILINE)


def require_token(repo: Path, mirrors: tuple[str, ...], token: str, errors: list[str]) -> None:
    for rel in mirrors:
        path = repo / rel
        if not path.is_file():
            errors.append(f"missing live status mirror: {rel}")
            continue
        mirror = path.read_text(encoding="utf-8")
        if token not in mirror:
            errors.append(f"{rel}: missing status mirror token {token!r}")


def validate_active_or_closed(
    *,
    repo: Path,
    text: str,
    complete_re: re.Pattern[str],
    next_re: re.Pattern[str],
    all_letters: list[str],
    phase: str,
    mirrors: tuple[str, ...],
    errors: list[str],
) -> tuple[bool, str | None, str]:
    completed = sorted(set(complete_re.findall(text)))
    next_ids = sorted(set(next_re.findall(text)))
    closed = False
    next_letter: str | None = None

    if len(next_ids) == 1:
        next_letter = next_ids[0]
        expected_completed = [chr(code) for code in range(ord("A"), ord(next_letter))]
        if completed != expected_completed:
            errors.append(
                f"Phase-{phase} completed sequence must be contiguous before {next_letter}; "
                f"expected {expected_completed}, found {completed}"
            )
    elif len(next_ids) == 0 and completed == all_letters:
        closed = True
    else:
        errors.append(
            f"Phase-{phase} index must have exactly one NEXT ELIGIBLE subphase with a contiguous "
            f"completed prefix, or be fully closed; next={next_ids}, completed={completed}"
        )

    completed_token = f"{phase}-" + "/".join(completed) + " COMPLETE" if completed else ""
    if completed_token:
        require_token(repo, mirrors, completed_token, errors)

    if closed:
        require_token(repo, mirrors, f"PHASE {phase} COMPLETE", errors)
    elif next_letter is not None:
        require_token(repo, mirrors, f"PHASE {phase} ACTIVE", errors)
        require_token(repo, mirrors, f"{phase}-{next_letter} NEXT ELIGIBLE", errors)

    return closed, next_letter, completed_token


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    errors: list[str] = []

    phase18 = repo / PHASE018_INDEX
    if not phase18.is_file():
        print("ERROR missing Phase-018 status authority index")
        return 1
    text18 = phase18.read_text(encoding="utf-8")
    completed18 = sorted(set(P18_COMPLETE_RE.findall(text18)))
    next18 = sorted(set(P18_NEXT_RE.findall(text18)))
    if completed18 != P18_ALL or next18:
        errors.append(
            "Phase 018 must remain fully closed A-M; "
            f"completed={completed18}, next={next18}"
        )
    p18_token = "018-" + "/".join(P18_ALL) + " COMPLETE"
    require_token(repo, PHASE018_MIRRORS, p18_token, errors)
    require_token(repo, PHASE018_MIRRORS, "PHASE 018 COMPLETE", errors)

    phase19 = repo / PHASE019_INDEX
    if not phase19.is_file():
        errors.append("missing Phase-019 status authority index")
        closed19 = False
    else:
        text19 = phase19.read_text(encoding="utf-8")
        completed19 = sorted(set(P19_COMPLETE_RE.findall(text19)))
        next19 = sorted(set(P19_NEXT_RE.findall(text19)))
        closed19 = completed19 == P19_ALL and not next19
        if not closed19:
            errors.append(
                "Phase 019 must remain fully closed A-L before/through Phase 020; "
                f"completed={completed19}, next={next19}"
            )
        p19_token = "019-" + "/".join(P19_ALL) + " COMPLETE"
        require_token(repo, PHASE019_MIRRORS, p19_token, errors)
        require_token(repo, PHASE019_MIRRORS, "PHASE 019 COMPLETE", errors)

    phase20 = repo / PHASE020_INDEX
    if phase20.is_file():
        text20 = phase20.read_text(encoding="utf-8")
        closed20, next20, p20_token = validate_active_or_closed(
            repo=repo,
            text=text20,
            complete_re=P20_COMPLETE_RE,
            next_re=P20_NEXT_RE,
            all_letters=P20_ALL,
            phase="020",
            mirrors=PHASE020_MIRRORS,
            errors=errors,
        )
    else:
        errors.append("missing Phase-020 status authority index")
        closed20, next20, p20_token = False, None, ""

    for error in errors:
        print("ERROR", error)

    if not errors:
        phase20_state = (
            f"020-{'/'.join(P20_ALL)} COMPLETE / PHASE 020 COMPLETE"
            if closed20
            else f"{p20_token} / PHASE 020 ACTIVE / 020-{next20} NEXT ELIGIBLE"
        )
        print(
            "Status mirror check: 0 errors; "
            f"{p18_token} / PHASE 018 COMPLETE / "
            f"019-{'/'.join(P19_ALL)} COMPLETE / PHASE 019 COMPLETE / "
            f"{phase20_state}"
        )
    else:
        print(f"Status mirror check: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
