#!/usr/bin/env python3
"""Check whether a scheduled post should already be live but is not.

Usage: due_posts.py [--days N] [--site URL] [--now ISO_DATE]

Reads the front matter of every post in content/<lang>/post/, keeps the ones dated
in the last N days (default 7) up to now, and requests their URL on the live site.
Prints "missing=true" for $GITHUB_OUTPUT if any of them does not answer yet, and
"missing=false" otherwise. Details go to stderr. --site and --now are for testing.
"""

import argparse
import datetime
import glob
import sys
import tomllib
import urllib.error
import urllib.request
from urllib.parse import quote

PREFIX = {"es": "/", "ca": "/ca/", "en": "/en/"}


def front_matter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read().replace("\r\n", "\n")
    if not text.startswith("+++\n"):
        return None
    end = text.find("\n+++", 4)
    return tomllib.loads(text[4:end]) if end != -1 else None


def as_datetime(value):
    if isinstance(value, str):
        value = datetime.datetime.fromisoformat(value)
    if isinstance(value, datetime.date) and not isinstance(value, datetime.datetime):
        value = datetime.datetime.combine(value, datetime.time())
    if value.tzinfo is None:
        value = value.replace(tzinfo=datetime.timezone.utc)
    return value


def status(url):
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "albertlg.com scheduled posts check"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code
    except OSError as error:
        print(f"Could not check {url}: {error}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--site", default="https://albertlg.com")
    parser.add_argument("--now")
    args = parser.parse_args()

    now = as_datetime(args.now) if args.now else datetime.datetime.now(datetime.timezone.utc)
    since = now - datetime.timedelta(days=args.days)

    missing = False
    for lang, prefix in PREFIX.items():
        for path in sorted(glob.glob(f"content/{lang}/post/**/*.html", recursive=True)):
            meta = front_matter(path)
            if not meta or meta.get("draft") or not meta.get("slug") or not meta.get("date"):
                continue
            date = as_datetime(meta["date"])
            if not since <= date <= now:
                continue
            url = args.site.rstrip("/") + prefix + quote(meta["slug"]) + "/"
            code = status(url)
            print(f"{code} {url} (dated {date.isoformat()})", file=sys.stderr)
            if code is not None and code != 200:
                missing = True

    print(f"missing={'true' if missing else 'false'}")


if __name__ == "__main__":
    main()
