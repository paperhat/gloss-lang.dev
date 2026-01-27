#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any, Iterable, Optional


@dataclass(frozen=True)
class CommitVerification:
	sha: str
	verified: bool
	reason: str
	signature: Optional[str]
	signer_login: Optional[str]


def _github_request(url: str, token: str) -> tuple[int, dict[str, str], bytes]:
	req = urllib.request.Request(url)
	req.add_header("Accept", "application/vnd.github+json")
	req.add_header("X-GitHub-Api-Version", "2022-11-28")
	req.add_header("Authorization", f"Bearer {token}")

	try:
		with urllib.request.urlopen(req) as resp:
			status = int(resp.status)
			headers = {k.lower(): v for k, v in resp.headers.items()}
			body = resp.read()
			return status, headers, body
	except urllib.error.HTTPError as e:
		body = e.read() if e.fp else b""
		headers = {k.lower(): v for k, v in (e.headers.items() if e.headers else [])}
		return int(e.code), headers, body


def _parse_link_next(link_header: str) -> Optional[str]:
	# Very small Link parser: we only care about rel="next".
	# Example: <https://api.github.com/...&page=2>; rel="next", <...>; rel="last"
	parts = [p.strip() for p in link_header.split(",") if p.strip()]
	for part in parts:
		if ";" not in part:
			continue
		url_part, *params = [s.strip() for s in part.split(";")]
		if not (url_part.startswith("<") and url_part.endswith(">")):
			continue
		url = url_part[1:-1]
		rels = [p for p in params if p.startswith("rel=")]
		if any(p == 'rel="next"' for p in rels):
			return url
	return None


def _load_event_payload() -> dict[str, Any]:
	path = os.environ.get("GITHUB_EVENT_PATH")
	if not path:
		raise RuntimeError("GITHUB_EVENT_PATH is not set")
	with open(path, "r", encoding="utf-8") as f:
		return json.load(f)


def _get_pr_number(event: dict[str, Any]) -> int:
	pr = event.get("pull_request")
	if not isinstance(pr, dict):
		raise RuntimeError("This workflow must run on pull_request events")
	number = pr.get("number")
	if not isinstance(number, int):
		raise RuntimeError("Unable to determine pull_request.number")
	return number


def _iter_pr_commits(owner: str, repo: str, pr_number: int, token: str) -> Iterable[dict[str, Any]]:
	url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/commits?per_page=100"
	while url:
		status, headers, body = _github_request(url, token)
		if status != 200:
			try:
				error_text = body.decode("utf-8", errors="replace")
			except Exception:
				error_text = "<unreadable>"
			raise RuntimeError(f"GitHub API request failed ({status}) for {url}: {error_text}")

		data = json.loads(body.decode("utf-8"))
		if not isinstance(data, list):
			raise RuntimeError("Unexpected GitHub API response (expected a list)")
		for item in data:
			yield item

		next_url = _parse_link_next(headers.get("link", ""))
		url = next_url


def _extract_verification(commit_item: dict[str, Any]) -> CommitVerification:
	sha = str(commit_item.get("sha", ""))
	commit = commit_item.get("commit")
	if not isinstance(commit, dict):
		commit = {}
	verification = commit.get("verification")
	if not isinstance(verification, dict):
		verification = {}

	verified = bool(verification.get("verified", False))
	reason = str(verification.get("reason", ""))
	signature = verification.get("signature")
	if signature is not None:
		signature = str(signature)

	signer_login: Optional[str] = None
	signer = verification.get("signer")
	if isinstance(signer, dict) and isinstance(signer.get("login"), str):
		signer_login = signer["login"]

	return CommitVerification(
		sha=sha,
		verified=verified,
		reason=reason,
		signature=signature,
		signer_login=signer_login,
	)


def main() -> int:
	token = os.environ.get("GITHUB_TOKEN")
	if not token:
		print("error: GITHUB_TOKEN is not set", file=sys.stderr)
		return 2

	repo_full = os.environ.get("GITHUB_REPOSITORY")
	if not repo_full or "/" not in repo_full:
		print("error: GITHUB_REPOSITORY is not set or invalid", file=sys.stderr)
		return 2
	owner, repo = repo_full.split("/", 1)

	event = _load_event_payload()
	pr_number = _get_pr_number(event)

	failed: list[CommitVerification] = []
	count = 0
	for item in _iter_pr_commits(owner, repo, pr_number, token):
		count += 1
		ver = _extract_verification(item)
		if not ver.verified:
			failed.append(ver)

	if count == 0:
		print("error: PR has zero commits?", file=sys.stderr)
		return 2

	if failed:
		print("require-verified-commits: FAILED")
		print(f"Found {len(failed)} unverified commit(s) in PR #{pr_number}:")
		for ver in failed:
			who = f" signer={ver.signer_login}" if ver.signer_login else ""
			print(f"- {ver.sha[:12]} verified={ver.verified} reason={ver.reason}{who}")
		print("\nFix: ensure every commit is signed with a key GitHub can verify.")
		return 1

	print(f"ok: all {count} commit(s) in PR #{pr_number} are verified")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
