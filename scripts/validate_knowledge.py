#!/usr/bin/env python3
"""Deterministic structural validation for the MUDAC knowledge bundle.

This validator intentionally checks only properties that can be established
without semantic judgment or network access. A passing run is NOT an OKF
`verified` event and must never be represented as one.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml


ALLOWED_STATUS = {"draft", "stable", "deprecated"}
ACTOR_RE = re.compile(
    r"^(?:human:[^\s]+|process:[^\s]+|[A-Za-z0-9._-]+/[A-Za-z0-9._+:-]+)$"
)
STABLE_ID_RE = re.compile(r"^[a-z][a-z0-9]*-\d{3}$")
ANCHOR_RE = re.compile(r'<a\s+id=["\']([^"\']+)["\']\s*>\s*</a>', re.IGNORECASE)
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REGISTRY_ENTRY_RE = re.compile(
    r"^\s*[*-]\s+\[([A-Z][A-Z0-9]*-\d{3})[^\]]*\]\(([^)]+)\)\s*$",
    re.MULTILINE,
)
PHASE_DIR_RE = re.compile(r"^\d{3}-")


@dataclass(frozen=True)
class Finding:
    severity: str
    path: str
    message: str


class Validator:
    def __init__(self, root: Path, strict_warnings: bool = False) -> None:
        self.root = root.resolve()
        self.docs = self.root / "docs"
        self.strict_warnings = strict_warnings
        self.findings: list[Finding] = []
        self.markdown_count = 0
        self.frontmatter_count = 0
        self.stable_anchor_locations: dict[str, Path] = {}

    def error(self, path: Path | str, message: str) -> None:
        self.findings.append(Finding("ERROR", self._display(path), message))

    def warn(self, path: Path | str, message: str) -> None:
        self.findings.append(Finding("WARNING", self._display(path), message))

    def _display(self, path: Path | str) -> str:
        candidate = Path(path)
        try:
            return str(candidate.resolve().relative_to(self.root))
        except (ValueError, OSError):
            return str(path)

    def run(self) -> int:
        self.validate_routing_contract()

        markdown_files = sorted(self.root.rglob("*.md"))
        self.markdown_count = len(markdown_files)

        parsed: dict[Path, tuple[dict | None, str, str]] = {}
        for path in markdown_files:
            text = self._read(path)
            if text is None:
                continue
            frontmatter, body = self.parse_frontmatter(path, text)
            parsed[path] = (frontmatter, body, text)
            self.validate_frontmatter(path, frontmatter)
            self.collect_stable_anchors(path, body)

        self.validate_rule_registry(parsed)

        for path, (frontmatter, body, _) in parsed.items():
            if self.enforce_links_for(path):
                self.validate_markdown_links(path, body)
            if frontmatter is not None:
                self.validate_source_resources(path, frontmatter)

        self.validate_workflow_contract()
        return self.report()

    def _read(self, path: Path) -> str | None:
        try:
            return path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            self.error(path, "Markdown/text governance artifacts must be UTF-8.")
            return None
        except OSError as exc:
            self.error(path, f"Could not read file: {exc}")
            return None

    def parse_frontmatter(self, path: Path, text: str) -> tuple[dict | None, str]:
        lines = text.splitlines()
        if not lines or lines[0].strip() != "---":
            return None, text

        closing = None
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                closing = index
                break

        if closing is None:
            self.error(path, "Frontmatter opens with '---' but has no closing delimiter.")
            return None, text

        raw = "\n".join(lines[1:closing])
        try:
            loaded = yaml.safe_load(raw)
        except yaml.YAMLError as exc:
            self.error(path, f"Frontmatter is not valid YAML: {exc}")
            return None, "\n".join(lines[closing + 1 :])

        if loaded is None:
            loaded = {}
        if not isinstance(loaded, dict):
            self.error(path, "Frontmatter must decode to a YAML mapping.")
            loaded = {}
        self.frontmatter_count += 1
        return loaded, "\n".join(lines[closing + 1 :])

    def validate_routing_contract(self) -> None:
        required = [
            self.root / "AGENTS.md",
            self.root / "README.md",
            self.root / "requirements-docs.txt",
            self.root / "scripts" / "validate_knowledge.py",
            self.docs / "index.md",
            self.docs / "README.md",
            self.docs / "canonical" / "index.md",
            self.docs / "references" / "index.md",
            self.docs / "canonical" / "governance" / "rule-identifiers.md",
            self.docs / "canonical" / "governance" / "metadata-trust-lifecycle.md",
            self.docs / "canonical" / "governance" / "validation-enforcement.md",
        ]
        categories = [
            "architecture",
            "concepts",
            "experience",
            "governance",
            "invariants",
            "mechanisms",
            "policies",
        ]
        required.extend(self.docs / "canonical" / category / "index.md" for category in categories)

        for path in required:
            if not path.exists():
                self.error(path, "Required routing/governance surface is missing.")

        if self.docs.exists():
            for child in sorted(self.docs.iterdir()):
                if child.is_dir() and PHASE_DIR_RE.match(child.name):
                    index = child / "index.md"
                    if not index.exists():
                        self.error(index, f"Numbered phase directory {child.name!r} must have index.md.")

        bundle_index = self.docs / "index.md"
        if bundle_index.exists():
            text = self._read(bundle_index)
            if text:
                fm, _ = self.parse_frontmatter(bundle_index, text)
                if fm is None:
                    self.error(bundle_index, "Bundle root must declare okf_version frontmatter.")
                elif str(fm.get("okf_version")) != "0.2":
                    self.error(bundle_index, "Bundle root okf_version must be '0.2'.")

    def validate_frontmatter(self, path: Path, fm: dict | None) -> None:
        name = path.name
        is_docs_index_or_log = path.is_relative_to(self.docs) and name in {"index.md", "log.md"}

        if is_docs_index_or_log:
            if fm and "type" in fm:
                self.error(path, "Reserved index.md/log.md files must not be OKF concept documents with type.")
            return

        is_canonical_concept = path.is_relative_to(self.docs / "canonical")
        is_reference_concept = path.is_relative_to(self.docs / "references") and name not in {"index.md", "log.md"}

        if is_canonical_concept or is_reference_concept:
            if fm is None:
                self.error(path, "Current canonical/reference knowledge must have OKF frontmatter.")
                return
            required = ["type", "title", "description", "status", "tags", "sources"]
            for key in required:
                if key not in fm:
                    self.error(path, f"MUDAC current-knowledge profile requires frontmatter key {key!r}.")

        if fm is None:
            return

        if "type" in fm and (not isinstance(fm["type"], str) or not fm["type"].strip()):
            self.error(path, "type must be a non-empty string.")
        for key in ("title", "description"):
            if key in fm and (not isinstance(fm[key], str) or not fm[key].strip()):
                self.error(path, f"{key} must be a non-empty string when present.")

        if "status" in fm and fm["status"] not in ALLOWED_STATUS:
            self.error(path, f"status must be one of {sorted(ALLOWED_STATUS)}; got {fm['status']!r}.")

        if "tags" in fm:
            tags = fm["tags"]
            if not isinstance(tags, list) or any(not isinstance(tag, str) or not tag.strip() for tag in tags):
                self.error(path, "tags must be a YAML list of non-empty strings.")

        if "sources" in fm:
            self.validate_sources_shape(path, fm["sources"], fm.get("usage_window"))

        if "generated" in fm:
            self.validate_actor_event(path, "generated", fm["generated"])

        if "verified" in fm:
            verified = fm["verified"]
            events = verified if isinstance(verified, list) else [verified]
            if not all(isinstance(event, dict) for event in events):
                self.error(path, "verified must be a mapping or a list of mappings.")
            else:
                for index, event in enumerate(events):
                    self.validate_actor_event(path, f"verified[{index}]", event)

        if "stale_after" in fm:
            self.validate_timestamp(path, "stale_after", fm["stale_after"])

    def validate_sources_shape(self, path: Path, sources: object, shared_usage_window: object) -> None:
        if not isinstance(sources, list) or not sources:
            self.error(path, "sources must be a non-empty YAML list when present.")
            return
        for index, source in enumerate(sources):
            label = f"sources[{index}]"
            if not isinstance(source, dict):
                self.error(path, f"{label} must be a mapping.")
                continue
            resource = source.get("resource")
            if not isinstance(resource, str) or not resource.strip():
                self.error(path, f"{label}.resource is required and must be a non-empty string.")
            if "author" in source:
                self.validate_actor(path, f"{label}.author", source["author"])
            if "last_modified" in source:
                self.validate_timestamp(path, f"{label}.last_modified", source["last_modified"])
            if "usage_count" in source:
                value = source["usage_count"]
                if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                    self.error(path, f"{label}.usage_count must be a non-negative integer.")
            if "usage_window" in source:
                self.validate_usage_window(path, f"{label}.usage_window", source["usage_window"])

        if shared_usage_window is not None:
            self.validate_usage_window(path, "usage_window", shared_usage_window)

    def validate_usage_window(self, path: Path, label: str, value: object) -> None:
        if not isinstance(value, dict):
            self.error(path, f"{label} must be a mapping with from/to timestamps.")
            return
        for key in ("from", "to"):
            if key not in value:
                self.error(path, f"{label}.{key} is required.")
            else:
                self.validate_timestamp(path, f"{label}.{key}", value[key])

    def validate_actor_event(self, path: Path, label: str, event: object) -> None:
        if not isinstance(event, dict):
            self.error(path, f"{label} must be a mapping containing by and at.")
            return
        if "by" not in event:
            self.error(path, f"{label}.by is required.")
        else:
            self.validate_actor(path, f"{label}.by", event["by"])
        if "at" not in event:
            self.error(path, f"{label}.at is required.")
        else:
            self.validate_timestamp(path, f"{label}.at", event["at"])

    def validate_actor(self, path: Path, label: str, value: object) -> None:
        if not isinstance(value, str) or not ACTOR_RE.match(value):
            self.error(
                path,
                f"{label} must use OKF actor form human:<id>, process:<id>, or <producer>/<version>; got {value!r}.",
            )

    def validate_timestamp(self, path: Path, label: str, value: object) -> None:
        parsed: datetime | None = None
        if isinstance(value, datetime):
            parsed = value
        elif isinstance(value, date):
            self.error(path, f"{label} must be a datetime with explicit UTC offset, not a date.")
            return
        elif isinstance(value, str):
            candidate = value[:-1] + "+00:00" if value.endswith("Z") else value
            try:
                parsed = datetime.fromisoformat(candidate)
            except ValueError:
                self.error(path, f"{label} is not a valid ISO 8601 datetime: {value!r}.")
                return
        else:
            self.error(path, f"{label} must be an ISO 8601 datetime.")
            return

        if parsed.tzinfo is None or parsed.utcoffset() is None:
            self.error(path, f"{label} must include an explicit UTC offset.")

    def collect_stable_anchors(self, path: Path, body: str) -> None:
        if not path.is_relative_to(self.docs / "canonical"):
            return
        clean_body = self.strip_fenced_code(body)
        for match in ANCHOR_RE.finditer(clean_body):
            anchor = match.group(1).lower()
            if not STABLE_ID_RE.match(anchor):
                continue
            if anchor in self.stable_anchor_locations:
                other = self.stable_anchor_locations[anchor]
                self.error(path, f"Stable rule anchor {anchor!r} duplicates {self._display(other)}.")
            else:
                self.stable_anchor_locations[anchor] = path

            tail = clean_body[match.end() :]
            heading = next((line.strip() for line in tail.splitlines() if line.strip()), "")
            expected = anchor.upper()
            if not re.match(rf"^#+\s+{re.escape(expected)}\b", heading):
                self.error(path, f"Stable anchor {anchor!r} must be followed by a heading beginning {expected}.")

    def validate_rule_registry(self, parsed: dict[Path, tuple[dict | None, str, str]]) -> None:
        registry = self.docs / "canonical" / "governance" / "rule-identifiers.md"
        if registry not in parsed:
            return
        body = self.strip_fenced_code(parsed[registry][1])
        registry_ids: dict[str, tuple[Path, str]] = {}

        for match in REGISTRY_ENTRY_RE.finditer(body):
            visible_id = match.group(1)
            raw_target = match.group(2).strip()
            target_path_text, fragment = self.split_target(raw_target)
            stable_id = visible_id.lower()
            if not fragment or fragment.lower() != stable_id:
                self.error(
                    registry,
                    f"Registry entry {visible_id!r} must link to matching fragment #{stable_id}; got {raw_target!r}.",
                )
                continue
            if stable_id in registry_ids:
                self.error(registry, f"Stable rule {stable_id!r} appears more than once in the registry.")
                continue
            target = self.resolve_local_target(registry, target_path_text)
            if target is None:
                self.error(registry, f"Registry rule {stable_id!r} does not point to a local owner.")
                continue
            registry_ids[stable_id] = (target, raw_target)
            if not target.exists():
                self.error(registry, f"Registry target for {stable_id!r} does not exist: {self._display(target)}.")
                continue
            target_text = self._read(target)
            if target_text is not None and not re.search(
                rf'<a\s+id=["\']{re.escape(stable_id)}["\']\s*>\s*</a>', target_text, re.IGNORECASE
            ):
                self.error(registry, f"Registry target for {stable_id!r} lacks explicit owner anchor.")

        for stable_id, owner in sorted(self.stable_anchor_locations.items()):
            if stable_id not in registry_ids:
                self.error(owner, f"Stable rule anchor {stable_id!r} is not registered in rule-identifiers.md.")

        for stable_id, (target, _) in sorted(registry_ids.items()):
            owner = self.stable_anchor_locations.get(stable_id)
            if owner is None:
                self.error(registry, f"Registry lists {stable_id!r}, but no canonical stable anchor exists.")
            elif owner.resolve() != target.resolve():
                self.error(
                    registry,
                    f"Registry sends {stable_id!r} to {self._display(target)}, but anchor owner is {self._display(owner)}.",
                )

    def enforce_links_for(self, path: Path) -> bool:
        if path in {self.root / "AGENTS.md", self.root / "README.md", self.docs / "README.md", self.docs / "index.md"}:
            return True
        if path.is_relative_to(self.docs / "canonical") or path.is_relative_to(self.docs / "references"):
            return True
        if path.name in {"index.md", "README.md"} and path.parent.parent == self.docs:
            return True
        if path.is_relative_to(self.docs / "004-knowledge-architecture"):
            return True
        return False

    def extract_markdown_targets(self, body: str) -> list[str]:
        clean = self.strip_fenced_code(body)
        clean = re.sub(r"`[^`\n]*`", "", clean)
        targets: list[str] = []
        for match in MARKDOWN_LINK_RE.finditer(clean):
            raw = match.group(1).strip()
            if raw.startswith("<") and ">" in raw:
                raw = raw[1 : raw.index(">")]
            elif " \"" in raw or " '" in raw:
                raw = raw.split(maxsplit=1)[0]
            targets.append(raw)
        return targets

    def strip_fenced_code(self, text: str) -> str:
        output: list[str] = []
        fence: str | None = None
        for line in text.splitlines():
            stripped = line.lstrip()
            marker = None
            if stripped.startswith("```"):
                marker = "```"
            elif stripped.startswith("~~~"):
                marker = "~~~"
            if marker:
                if fence is None:
                    fence = marker
                elif fence == marker:
                    fence = None
                continue
            if fence is None:
                output.append(line)
        return "\n".join(output)

    def validate_markdown_links(self, path: Path, body: str) -> None:
        for raw in self.extract_markdown_targets(body):
            target_text, fragment = self.split_target(raw)
            if not target_text:
                if fragment and STABLE_ID_RE.match(fragment.lower()):
                    text = self._read(path)
                    if text and not re.search(
                        rf'<a\s+id=["\']{re.escape(fragment.lower())}["\']\s*>\s*</a>', text, re.IGNORECASE
                    ):
                        self.error(path, f"Stable local fragment #{fragment} has no explicit anchor.")
                continue
            if self.is_external_or_nonfile(target_text):
                continue
            target = self.resolve_local_target(path, target_text)
            if target is None:
                continue
            if not target.exists():
                self.error(path, f"Internal Markdown link target does not exist: {raw!r} -> {self._display(target)}.")
                continue
            if fragment and STABLE_ID_RE.match(fragment.lower()) and target.is_file():
                target_text_content = self._read(target)
                if target_text_content and not re.search(
                    rf'<a\s+id=["\']{re.escape(fragment.lower())}["\']\s*>\s*</a>',
                    target_text_content,
                    re.IGNORECASE,
                ):
                    self.error(path, f"Stable rule link {raw!r} points to file without anchor #{fragment}.")

    def validate_source_resources(self, path: Path, fm: dict) -> None:
        sources = fm.get("sources")
        if not isinstance(sources, list):
            return
        for index, source in enumerate(sources):
            if not isinstance(source, dict):
                continue
            resource = source.get("resource")
            if not isinstance(resource, str) or self.is_external_or_nonfile(resource):
                continue
            if not self.looks_like_local_path(resource):
                continue
            target_text, _ = self.split_target(resource)
            target = self.resolve_local_target(path, target_text)
            if target is not None and not target.exists():
                self.error(
                    path,
                    f"sources[{index}].resource does not resolve: {resource!r} -> {self._display(target)}.",
                )

    def split_target(self, raw: str) -> tuple[str, str]:
        target = unquote(raw.strip())
        if "#" in target:
            path, fragment = target.split("#", 1)
            return path, fragment
        return target, ""

    def is_external_or_nonfile(self, target: str) -> bool:
        lowered = target.lower()
        if lowered.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:")):
            return True
        parsed = urlparse(target)
        return bool(parsed.scheme and parsed.scheme not in {"file"})

    def looks_like_local_path(self, value: str) -> bool:
        path_part, _ = self.split_target(value)
        return path_part.startswith((".", "/")) or path_part.endswith(".md") or "/" in path_part

    def resolve_local_target(self, source_file: Path, target_text: str) -> Path | None:
        if not target_text or self.is_external_or_nonfile(target_text):
            return None
        target_text = target_text.split("?", 1)[0]
        if target_text.startswith("/"):
            base = self.docs if source_file.is_relative_to(self.docs) else self.root
            return (base / target_text.lstrip("/")).resolve()
        return (source_file.parent / target_text).resolve()

    def validate_workflow_contract(self) -> None:
        workflow = self.root / ".github" / "workflows" / "knowledge-validation.yml"
        if not workflow.exists():
            self.error(workflow, "Knowledge-validation GitHub Actions workflow is missing.")
            return
        text = self._read(workflow)
        if text is None:
            return
        required_snippets = [
            "contents: read",
            "python scripts/validate_knowledge.py",
            "requirements-docs.txt",
        ]
        for snippet in required_snippets:
            if snippet not in text:
                self.error(workflow, f"Workflow must contain {snippet!r}.")
        if re.search(r"\bcontents:\s*write\b", text):
            self.error(workflow, "Knowledge validation workflow must remain read-only for repository contents.")

    def report(self) -> int:
        warnings = [finding for finding in self.findings if finding.severity == "WARNING"]
        errors = [finding for finding in self.findings if finding.severity == "ERROR"]

        for finding in sorted(self.findings, key=lambda item: (item.severity, item.path, item.message)):
            print(f"{finding.severity}: {finding.path}: {finding.message}")

        if self.strict_warnings and warnings:
            errors = errors + warnings

        stable_count = len(self.stable_anchor_locations)
        summary = (
            f"Validated {self.markdown_count} Markdown files; "
            f"{self.frontmatter_count} frontmatter blocks; "
            f"{stable_count} stable rule anchors; "
            f"{len([f for f in self.findings if f.severity == 'ERROR'])} errors; "
            f"{len(warnings)} warnings."
        )

        if errors:
            print(f"KNOWLEDGE VALIDATION FAILED — {summary}")
            print("Passing this validator is structural evidence only; it is never an OKF verified event.")
            return 1

        print(f"KNOWLEDGE VALIDATION PASSED — {summary}")
        print("Passing this validator is structural evidence only; it is never an OKF verified event.")
        return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate MUDAC OKF knowledge structure and anti-drift contracts.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root (defaults to parent of scripts/).",
    )
    parser.add_argument(
        "--strict-warnings",
        action="store_true",
        help="Treat warnings as failures; intended for repository-wide drift audits.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return Validator(args.root, strict_warnings=args.strict_warnings).run()


if __name__ == "__main__":
    sys.exit(main())
