#!/usr/bin/env python3
"""Check all URLs in README.md and report broken links."""

import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

README = Path("README.md")
REPORT = Path("link-check-report.md")

URL_RE = re.compile(r'https?://[^\s\)\]>\"\']+')

ARXIV_DOMAINS = {"arxiv.org"}
RETRY_COUNT = 3
RETRY_WAIT = 5  # seconds

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; link-checker/1.0; +https://github.com)"
}


def is_arxiv(url: str) -> bool:
    return any(d in url for d in ARXIV_DOMAINS)


def check_url(url: str) -> tuple[int | None, str]:
    """Return (status_code, error_message). status_code is None on network error."""
    retries = RETRY_COUNT if is_arxiv(url) else 1

    for attempt in range(retries):
        try:
            resp = requests.head(
                url,
                headers=HEADERS,
                timeout=15,
                allow_redirects=True,
            )
            # Some servers reject HEAD; fall back to GET
            if resp.status_code in (405, 403):
                resp = requests.get(
                    url,
                    headers=HEADERS,
                    timeout=15,
                    allow_redirects=True,
                    stream=True,
                )

            if resp.status_code == 429 and attempt < retries - 1:
                time.sleep(RETRY_WAIT)
                continue

            return resp.status_code, ""
        except requests.RequestException as e:
            if attempt < retries - 1:
                time.sleep(RETRY_WAIT)
            else:
                return None, str(e)

    return None, "max retries exceeded"


def main() -> int:
    if not README.exists():
        print("README.md not found", file=sys.stderr)
        return 1

    text = README.read_text(encoding="utf-8")
    urls = sorted(set(URL_RE.findall(text)))

    print(f"Found {len(urls)} unique URLs")

    broken: list[tuple[str, int | None, str]] = []

    for url in urls:
        status, err = check_url(url)
        ok = status is not None and 200 <= status < 400
        icon = "✅" if ok else "❌"
        label = str(status) if status is not None else f"ERROR: {err}"
        print(f"  {icon} [{label}] {url}")
        if not ok:
            broken.append((url, status, err))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    if broken:
        lines = [
            f"## 🔗 Link Check Report — {now}",
            "",
            f"**{len(broken)} broken link(s)** found in `README.md`.",
            "",
            "| URL | Status |",
            "|-----|--------|",
        ]
        for url, status, err in broken:
            label = str(status) if status is not None else f"ERROR: {err}"
            lines.append(f"| {url} | `{label}` |")
        lines += [
            "",
            f"*Checked {len(urls)} URLs total.*",
        ]
        REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"\n{len(broken)} broken link(s) found.")
        return 1

    print("\nAll links OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
