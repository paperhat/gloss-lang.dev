#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def _fail(message: str) -> None:
    raise SystemExit(f"spec_link_check: {message}")


def _is_external(target: str) -> bool:
    return (
        target.startswith("http://")
        or target.startswith("https://")
        or target.startswith("mailto:")
        or target.startswith("#")
    )


def _strip_fragment_and_query(target: str) -> str:
    # Links in this repo sometimes include fragments. We only verify the file exists.
    target = target.split("#", 1)[0]
    target = target.split("?", 1)[0]
    return target


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        _fail(f"missing file: {path}")


def _iter_markdown_files(spec_root: Path) -> list[Path]:
    return sorted(spec_root.rglob("*.md"))


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: spec_link_check.py <spec_root_dir>", file=sys.stderr)
        return 2

    spec_root = Path(argv[1]).resolve()
    if not spec_root.exists() or not spec_root.is_dir():
        _fail(f"not a directory: {spec_root}")

    md_files = _iter_markdown_files(spec_root)
    if not md_files:
        _fail(f"no markdown files found under: {spec_root}")

    missing: list[tuple[Path, str, str]] = []

    for md_path in md_files:
        text = _read_text(md_path)
        for match in LINK_RE.finditer(text):
            raw_target = match.group(1).strip()
            if not raw_target or _is_external(raw_target):
                continue

            target = _strip_fragment_and_query(raw_target)
            if not target:
                continue

            # Only validate relative links (Codex/Gloss style).
            if target.startswith("/"):
                continue

            # Normalize ./
            if target.startswith("./"):
                target = target[2:]

            resolved = (md_path.parent / target).resolve()

            # Require the resolved path to be within this spec root.
            try:
                resolved.relative_to(spec_root)
            except ValueError:
                missing.append((md_path, raw_target, "link escapes spec root"))
                continue

            if not resolved.exists():
                missing.append((md_path, raw_target, "missing target"))

    if missing:
        for src, target, reason in missing:
            print(f"{src.as_posix()}: {reason}: {target}", file=sys.stderr)
        _fail(f"{len(missing)} broken links")

    print(f"ok: {len(md_files)} markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
