#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path


def main() -> int:
	# Policy gate: the Gloss project tree must not contain JSON.
	# This prevents accidental reintroduction of non-Codex artifacts.
	gloss_root = Path(__file__).resolve().parents[1]
	violations = sorted(gloss_root.rglob("*.json"))

	if violations:
		print("no_json_gate: JSON files are forbidden under gloss-lang.dev")
		for p in violations:
			print(f"- {p.relative_to(gloss_root)}")
		return 1

	print("ok: no JSON files under gloss-lang.dev")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
