#!/usr/bin/env python3
"""Validate VPskills Manager registry using only Python's standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "registry" / "index.json"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_NAME_RE = re.compile(r"^name:\s*([a-z0-9-]+)\s*$", re.MULTILINE)
ALLOWED_STATUS = {"active", "experimental", "deprecated", "disabled"}
ALLOWED_RISK = {"low", "medium", "high"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    errors: list[str] = []

    try:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"Missing registry: {REGISTRY_PATH}")
        return 1
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in registry: {exc}")
        return 1

    skills = registry.get("skills")
    if not isinstance(skills, list):
        fail("registry.skills must be an array")
        return 1

    seen: set[str] = set()

    for index, item in enumerate(skills):
        prefix = f"skills[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue

        required = {
            "name", "description", "path", "version", "status",
            "tags", "triggers", "compatibility", "risk_level", "source"
        }
        missing = sorted(required - item.keys())
        if missing:
            errors.append(f"{prefix} missing fields: {', '.join(missing)}")
            continue

        name = item["name"]
        if not isinstance(name, str) or not NAME_RE.fullmatch(name) or len(name) > 64:
            errors.append(f"{prefix}.name is invalid: {name!r}")
            continue

        if name in seen:
            errors.append(f"Duplicate skill name: {name}")
        seen.add(name)

        description = item["description"]
        if not isinstance(description, str) or not (1 <= len(description) <= 1024):
            errors.append(f"{name}: description must contain 1-1024 characters")

        if item["status"] not in ALLOWED_STATUS:
            errors.append(f"{name}: invalid status {item['status']!r}")

        if item["risk_level"] not in ALLOWED_RISK:
            errors.append(f"{name}: invalid risk_level {item['risk_level']!r}")

        for field in ("tags", "triggers", "compatibility"):
            if not isinstance(item[field], list) or not item[field]:
                errors.append(f"{name}: {field} must be a non-empty array")

        relative_path = Path(item["path"])
        if relative_path.is_absolute() or ".." in relative_path.parts:
            errors.append(f"{name}: unsafe path {item['path']!r}")
            continue

        skill_path = ROOT / relative_path
        if not skill_path.is_file():
            errors.append(f"{name}: missing file {item['path']}")
            continue

        text = skill_path.read_text(encoding="utf-8")
        match = FRONTMATTER_NAME_RE.search(text)
        if not match:
            errors.append(f"{name}: SKILL.md has no valid frontmatter name")
        elif match.group(1) != name:
            errors.append(
                f"{name}: registry name differs from SKILL.md name {match.group(1)!r}"
            )

        if skill_path.parent.name != name:
            errors.append(
                f"{name}: folder {skill_path.parent.name!r} must match skill name"
            )

    if errors:
        for error in errors:
            fail(error)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(skills)} skill(s) successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
