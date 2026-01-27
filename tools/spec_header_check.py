#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path


def _fail(message: str) -> None:
    raise SystemExit(f"spec_header_check: {message}")


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        _fail(f"missing file: {path}")


def _assert_lf_newlines(text: str, path: Path) -> None:
    if "\r" in text:
        _fail(f"CR/CRLF found in {path} (spec files must use LF only)")


def _assert_trailing_newline(text: str, path: Path) -> None:
    if not text.endswith("\n"):
        _fail(f"missing trailing newline in {path}")


def _expected_status_for(path: Path) -> str:
    # Mirror Codex convention: PEG is informative; everything else in spec/ is normative.
    if path.as_posix().endswith("/grammar/peg/index.md"):
        return "INFORMATIVE"
    return "NORMATIVE"


def _check_index(path: Path, expected_version: str, expected_lock_state: str, expected_editor: str) -> None:
    text = _read_text(path)
    _assert_lf_newlines(text, path)
    _assert_trailing_newline(text, path)

    lines = text.splitlines()
    if not lines:
        _fail(f"empty file: {path}")

    # Allow optional YAML front matter (e.g., for GitHub Pages / Jekyll).
    # If present, it must be the first thing in the file.
    start_index = 0
    if lines[0].strip() == "---":
        end_index = None
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                end_index = i
                break
        if end_index is None:
            _fail(f"unterminated YAML front matter (missing closing '---'): {path}")
        start_index = end_index + 1
        # Skip blank lines after front matter.
        while start_index < len(lines) and lines[start_index].strip() == "":
            start_index += 1

    if start_index >= len(lines):
        _fail(f"file too short to contain header + title: {path}")

    if lines[start_index].strip() == "":
        _fail(f"leading blank line not allowed before header: {path}")

    if len(lines) - start_index < 6:
        _fail(f"file too short to contain header + title: {path}")

    expected_status = _expected_status_for(path)

    header = lines[start_index : start_index + 4]
    if not header[0].startswith("Status:"):
        _fail(f"{path}: header must start with 'Status:'")
    if header[0].strip() != f"Status: {expected_status}":
        _fail(f"{path}: Status must be 'Status: {expected_status}'")

    if header[1].strip() != f"Lock State: {expected_lock_state}":
        _fail(f"{path}: Lock State must be 'Lock State: {expected_lock_state}'")

    if header[2].strip() != f"Version: {expected_version}":
        _fail(f"{path}: Version must be 'Version: {expected_version}'")

    if header[3].strip() != f"Editor: {expected_editor}":
        _fail(f"{path}: Editor must be 'Editor: {expected_editor}'")

    if lines[start_index + 4].strip() != "":
        _fail(f"{path}: line after header must be blank")

    if not lines[start_index + 5].startswith("# "):
        _fail(f"{path}: expected a Markdown H1 title after the blank line")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: spec_header_check.py <spec_root_dir>", file=sys.stderr)
        return 2

    spec_root = Path(argv[1]).resolve()
    if not spec_root.exists() or not spec_root.is_dir():
        _fail(f"not a directory: {spec_root}")

    # The header's Version field must match the versioned directory name (e.g., "1.0.0").
    expected_version = spec_root.name
    # If the versioned spec directory contains FROZEN.md, it is frozen and must be LOCKED.
    expected_lock_state = "LOCKED" if (spec_root / "FROZEN.md").exists() else "UNLOCKED"
    expected_editor = "Charles F. Munat"

    index_paths = sorted(spec_root.rglob("index.md"))
    if not index_paths:
        _fail(f"no index.md files found under: {spec_root}")

    for path in index_paths:
        _check_index(
            path,
            expected_version=expected_version,
            expected_lock_state=expected_lock_state,
            expected_editor=expected_editor,
        )

    print(f"ok: {len(index_paths)} spec index files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
