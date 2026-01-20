#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


def _fail(message: str) -> None:
	raise SystemExit(f"conformance_smokecheck_cdx: {message}")


def _read_text(path: Path) -> str:
	try:
		return path.read_text(encoding="utf-8")
	except FileNotFoundError:
		_fail(f"missing file: {path}")


def _assert_lf_newlines(text: str, path: Path) -> None:
	if "\r" in text:
		_fail(f"CR/CRLF found in {path} (fixtures must use LF only)")


def _assert_trailing_newline(text: str, path: Path) -> None:
	if not text.endswith("\n"):
		_fail(f"missing trailing newline in {path}")


@dataclass(frozen=True)
class Case:
	case_id: str
	kind: str
	input_path: Path
	canonical_path: Path | None
	expected_error_path: Path | None


_SELF_CLOSING_MARKER_RE = re.compile(r"^\s*<(?P<name>[A-Za-z][A-Za-z0-9_-]*)\s*(?P<body>[^>]*)/>\s*$")
_OPEN_MARKER_INLINE_RE = re.compile(r"^\s*<(?P<name>[A-Za-z][A-Za-z0-9_-]*)\s*(?P<body>[^>]*)>\s*$")
_REASON_CODE_RE = re.compile(r"`(?P<code>~gloss-(?:syn|res)-[a-z0-9-]+)`")


def _parse_attrs(body: str) -> dict[str, str]:
	attrs: dict[str, str] = {}
	i = 0
	n = len(body)

	def skip_ws() -> None:
		nonlocal i
		while i < n and body[i].isspace():
			i += 1

	def parse_key() -> str:
		nonlocal i
		start = i
		while i < n and (body[i].isalnum() or body[i] in "_-" ):
			i += 1
		key = body[start:i]
		if not key:
			_fail("invalid trait key in manifest (empty)")
		return key

	def parse_value() -> str:
		nonlocal i
		if i >= n:
			_fail("missing trait value in manifest")
		if body[i] == '"':
			i += 1
			out: list[str] = []
			while i < n:
				ch = body[i]
				if ch == '"':
					i += 1
					return "".join(out)
				if ch == "\\":
					i += 1
					if i >= n:
						_fail("unterminated escape in quoted trait value")
					out.append(body[i])
					i += 1
					continue
				out.append(ch)
				i += 1
			_fail("unterminated quoted trait value")

		start = i
		while i < n and not body[i].isspace():
			i += 1
		return body[start:i]

	while True:
		skip_ws()
		if i >= n:
			break

		key = parse_key()
		skip_ws()
		if i >= n or body[i] != "=":
			_fail(f"missing '=' after trait key {key!r}")
		i += 1
		skip_ws()
		value = parse_value()

		if key in attrs:
			_fail(f"duplicate trait {key!r} in manifest")
		attrs[key] = value

	return attrs


def _load_manifest(path: Path) -> list[Case]:
	text = _read_text(path)
	_assert_lf_newlines(text, path)
	_assert_trailing_newline(text, path)

	lines = text.splitlines()
	if not lines:
		_fail("empty manifest")

	# This smokecheck intentionally uses a restricted subset of Codex:
	# - Root is an explicit open/close pair.
	# - Root marker MAY be multiline (3+ traits).
	# - Each Case is a self-closing marker which MAY be multiline (3+ traits).
	# - Only blank lines are permitted between cases.
	if not lines[0].startswith("<ConformanceManifest"):
		_fail("manifest must start with <ConformanceManifest ...>")
	if not lines[-1].startswith("</ConformanceManifest"):
		_fail("manifest must end with </ConformanceManifest>")

	def _enforce_canonical_trait_layout(*, trait_count: int, is_multiline: bool, where: str) -> None:
		# Canonical rule from Codex Surface Form:
		# - 0-2 traits: single line
		# - 3+ traits: multiline (one per line)
		if trait_count <= 2 and is_multiline:
			_fail(f"{where}: {trait_count} trait(s) MUST be single-line in canonical form")
		if trait_count >= 3 and not is_multiline:
			_fail(f"{where}: {trait_count} trait(s) MUST be multiline in canonical form")

	def consume_multiline_marker(
		*,
		start_index: int,
		indent: str,
		concept_name: str,
		terminator: str,
	) -> tuple[dict[str, str], int]:
		"""Consumes a canonical multiline marker.

		Expected form:
		- First line: f"{indent}<{concept_name}"
		- Trait lines: f"{indent}\tkey=value"
		- Terminator line: f"{indent}{terminator}" (either '>' or '/>')
		"""
		if start_index >= len(lines):
			_fail(f"unexpected EOF looking for <{concept_name}>")

		first = lines[start_index]
		if first != f"{indent}<{concept_name}":
			_fail(f"expected '{indent}<{concept_name}' but got: {first!r}")

		traits: list[str] = []
		i = start_index + 1
		while i < len(lines):
			line = lines[i]
			if line == f"{indent}{terminator}":
				attrs = _parse_attrs(" ".join(traits))
				_enforce_canonical_trait_layout(
					trait_count=len(attrs),
					is_multiline=True,
					where=f"<{concept_name}> marker",
				)
				return attrs, i + 1
			if not line.startswith(indent + "\t"):
				_fail(f"malformed trait line in <{concept_name}> marker: {line!r}")
			traits.append(line.strip())
			i += 1

		_fail(f"unterminated <{concept_name}> marker (missing {terminator!r})")

	def consume_open_marker(*, start_index: int, concept_name: str) -> tuple[dict[str, str], int]:
		"""Consumes the root open marker, enforcing canonical trait layout."""
		line = lines[start_index]
		m = _OPEN_MARKER_INLINE_RE.match(line)
		if m and m.group("name") == concept_name:
			attrs = _parse_attrs(m.group("body"))
			_enforce_canonical_trait_layout(
				trait_count=len(attrs),
				is_multiline=False,
				where=f"<{concept_name}> marker",
			)
			return attrs, start_index + 1

		# Multiline canonical open marker.
		return consume_multiline_marker(
			start_index=start_index,
			indent="",
			concept_name=concept_name,
			terminator=">",
		)

	def consume_self_closing_marker(
		*,
		start_index: int,
		indent: str,
		concept_name: str,
	) -> tuple[dict[str, str], int]:
		"""Consumes a self-closing marker, enforcing canonical trait layout."""
		line = lines[start_index]
		m = _SELF_CLOSING_MARKER_RE.match(line)
		if m and m.group("name") == concept_name:
			attrs = _parse_attrs(m.group("body"))
			_enforce_canonical_trait_layout(
				trait_count=len(attrs),
				is_multiline=False,
				where=f"<{concept_name} /> marker",
			)
			return attrs, start_index + 1

		# Multiline canonical self-closing marker.
		return consume_multiline_marker(
			start_index=start_index,
			indent=indent,
			concept_name=concept_name,
			terminator="/>",
		)

	manifest_dir = path.parent
	cases: list[Case] = []
	seen_ids: set[str] = set()

	# Consume the root marker (currently unused by the smokecheck besides structure validation).
	_, start = consume_open_marker(start_index=0, concept_name="ConformanceManifest")

	# Consume cases until the closing marker.
	i = start
	while i < len(lines) - 1:
		raw = lines[i]
		if not raw.strip():
			i += 1
			continue
		if raw.strip().startswith("</ConformanceManifest"):
			break
		# Case markers may be inline (0-2 traits) or multiline (3+ traits).
		if not raw.startswith("\t<Case"):
			_fail(f"unexpected content inside manifest: {raw!r}")
		attrs, i = consume_self_closing_marker(
			start_index=i,
			indent="\t",
			concept_name="Case",
		)

		case_id = attrs.get("id")
		kind = attrs.get("kind")
		input_rel = attrs.get("input")
		canonical_rel = attrs.get("canonical")
		expected_error_rel = attrs.get("expectedError")

		if not case_id:
			_fail("Case missing required trait id")
		if case_id in seen_ids:
			_fail(f"duplicate Case id: {case_id}")
		seen_ids.add(case_id)

		if kind not in ("~valid", "~invalid"):
			_fail(f"Case {case_id}: kind must be ~valid or ~invalid")
		if not input_rel:
			_fail(f"Case {case_id}: missing required trait input")

		input_path = (manifest_dir / input_rel).resolve()
		canonical_path = (manifest_dir / canonical_rel).resolve() if canonical_rel else None
		expected_error_path = (manifest_dir / expected_error_rel).resolve() if expected_error_rel else None

		if kind == "~valid":
			if expected_error_path is not None:
				_fail(f"Case {case_id}: valid case MUST NOT have expectedError")
		else:
			if expected_error_path is None:
				_fail(f"Case {case_id}: invalid case MUST have expectedError")
			if canonical_path is not None:
				_fail(f"Case {case_id}: invalid case MUST NOT have canonical")

		cases.append(
			Case(
				case_id=case_id,
				kind=kind,
				input_path=input_path,
				canonical_path=canonical_path,
				expected_error_path=expected_error_path,
			)
		)

	return cases


def _validate_expected_error(path: Path) -> None:
	# Legacy signature kept for compatibility; the authoritative entry point is
	# `_validate_expected_error_against_spec`.
	text = _read_text(path)
	_assert_lf_newlines(text, path)
	_assert_trailing_newline(text, path)

	line = text.strip("\n")
	m = _SELF_CLOSING_MARKER_RE.match(line)
	if not m or m.group("name") != "ExpectedError":
		_fail(f"expected error must be a single <ExpectedError .../> marker: {path}")

	attrs = _parse_attrs(m.group("body"))
	category = attrs.get("category")
	reason = attrs.get("reason")
	if category not in ("~syntax", "~resolution"):
		_fail(f"ExpectedError.category must be ~syntax or ~resolution: {path}")
	if not reason or not reason.startswith("~"):
		_fail(f"ExpectedError.reason must be a ~token: {path}")


def _load_allowed_reason_codes() -> set[str]:
	# Single source of truth: the v0.1 spec defines canonical reason codes.
	gloss_root = Path(__file__).resolve().parents[1]
	spec_path = gloss_root / "spec/0.1/validation-errors/index.md"
	text = _read_text(spec_path)

	codes = {m.group("code") for m in _REASON_CODE_RE.finditer(text)}
	if not codes:
		_fail(f"no reason codes found in {spec_path} (expected backticked `~gloss-syn-*` / `~gloss-res-*`) ")
	return codes


def _validate_expected_error_against_spec(path: Path, allowed_reason_codes: set[str]) -> None:
	text = _read_text(path)
	_assert_lf_newlines(text, path)
	_assert_trailing_newline(text, path)

	line = text.strip("\n")
	m = _SELF_CLOSING_MARKER_RE.match(line)
	if not m or m.group("name") != "ExpectedError":
		_fail(f"expected error must be a single <ExpectedError .../> marker: {path}")

	attrs = _parse_attrs(m.group("body"))
	category = attrs.get("category")
	reason = attrs.get("reason")
	if category not in ("~syntax", "~resolution"):
		_fail(f"ExpectedError.category must be ~syntax or ~resolution: {path}")
	if not reason or not reason.startswith("~"):
		_fail(f"ExpectedError.reason must be a ~token: {path}")
	if reason not in allowed_reason_codes:
		_fail(f"ExpectedError.reason {reason!r} is not a spec-defined code: {path}")


def main(argv: list[str]) -> int:
	if len(argv) != 2:
		print("usage: conformance_smokecheck_cdx.py <path/to/manifest.cdx>", file=sys.stderr)
		return 2

	manifest_path = Path(argv[1]).resolve()
	cases = _load_manifest(manifest_path)
	allowed_reason_codes = _load_allowed_reason_codes()

	for c in cases:
		input_text = _read_text(c.input_path)
		_assert_lf_newlines(input_text, c.input_path)
		_assert_trailing_newline(input_text, c.input_path)

		if c.canonical_path is not None:
			canonical_text = _read_text(c.canonical_path)
			_assert_lf_newlines(canonical_text, c.canonical_path)
			_assert_trailing_newline(canonical_text, c.canonical_path)

		if c.expected_error_path is not None:
			_validate_expected_error_against_spec(c.expected_error_path, allowed_reason_codes)

	print(f"ok: {len(cases)} conformance cases")
	return 0


if __name__ == "__main__":
	raise SystemExit(main(sys.argv))
