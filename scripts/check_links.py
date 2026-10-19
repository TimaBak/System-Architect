#!/usr/bin/env python3
"""Validate local Markdown links without third-party dependencies.

Usage: python scripts/check_links.py
Checks relative file links in tracked .md files and reports missing targets.
Does not fetch external URLs or validate heading anchors.
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
IGNORE_DIRS = {".git", "node_modules", ".venv", "venv"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "data:")

def markdown_files():
    return sorted(
        p for p in ROOT.rglob("*.md")
        if not any(component in IGNORE_DIRS for component in p.relative_to(ROOT).parts)
    )

def main():
    checked = 0
    errors = []
    files = markdown_files()
    for file in files:
        text = file.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip().strip("<>")
            if target.startswith(SKIP_PREFIXES):
                continue
            local = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not local:
                continue
            checked += 1
            resolved = (file.parent / local).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append((file.relative_to(ROOT), target, "outside repository"))
            elif not resolved.exists():
                errors.append((file.relative_to(ROOT), target, "missing"))
    if errors:
        for source, dest, reason in errors:
            print(f"ERROR {source}: {dest} ({reason})")
        print(f"Failed: {len(errors)} broken links among {checked} local links")
        return 1
    print(f"OK: {len(files)} Markdown files, {checked} local links valid")
    return 0

if __name__ == "__main__":
    sys.exit(main())
