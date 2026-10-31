#!/usr/bin/env python3
"""Check internal links in the generated site.

Usage: check_links.py PUBLIC_DIR [NETLIFY_TOML]

Reads every HTML file in PUBLIC_DIR and collects the links that point to this site
(https://albertlg.com/..., /... or relative paths) in href, src, srcset and social
image tags. A link is fine when Netlify would serve something for it: a file in
PUBLIC_DIR or a folder with index.html. Links that only work through a redirect
(public/_redirects or netlify.toml) are reported as warnings: they work, but should
point to the final URL. Broken links are reported as errors and the script exits
with 1.
"""

import os
import re
import sys
import tomllib
from collections import defaultdict
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlsplit

SITE_HOSTS = {"albertlg.com", "www.albertlg.com"}
SKIP_PREFIXES = ("#", "mailto:", "tel:", "javascript:", "data:", "whatsapp:")
LINK_ATTRS = {
    "a": ("href",),
    "link": ("href",),
    "img": ("src", "srcset"),
    "source": ("src", "srcset"),
    "script": ("src",),
    "iframe": ("src",),
}
SOCIAL_IMAGE_META = {"og:image", "og:url", "twitter:image"}


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for name in LINK_ATTRS.get(tag, ()):
            value = attrs.get(name)
            if not value:
                continue
            if name == "srcset":
                self.links += [part.strip().split()[0] for part in value.split(",") if part.strip()]
            else:
                self.links.append(value)
        if tag == "meta" and (attrs.get("property") or attrs.get("name")) in SOCIAL_IMAGE_META:
            if attrs.get("content"):
                self.links.append(attrs["content"])


def site_path(link, page_url):
    """Return the decoded path of a link to this site, or None for anything else."""
    link = link.strip()
    if not link or link.startswith(SKIP_PREFIXES):
        return None
    parts = urlsplit(urljoin(page_url, link))
    if parts.scheme not in ("http", "https") or parts.hostname not in SITE_HOSTS:
        return None
    return unquote(parts.path) or "/"


def load_redirects(public_dir, netlify_toml):
    """Return the 'from' paths of every redirect rule (domain-level rules are skipped)."""
    rules = []
    redirects_file = os.path.join(public_dir, "_redirects")
    if os.path.isfile(redirects_file):
        with open(redirects_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    rules.append(line.split()[0])
    if netlify_toml and os.path.isfile(netlify_toml):
        with open(netlify_toml, "rb") as f:
            rules += [r["from"] for r in tomllib.load(f).get("redirects", []) if "from" in r]
    patterns = []
    for rule in rules:
        if not rule.startswith("/"):
            continue
        rule = unquote(rule).rstrip("/") or "/"
        regex = re.escape(rule).replace(r"\*", ".*")
        regex = re.sub(r":[A-Za-z_]+", "[^/]+", regex)
        patterns.append(re.compile("^" + regex + "/?$"))
    return patterns


def exists(public_dir, path):
    target = os.path.join(public_dir, path.lstrip("/"))
    return (
        os.path.isfile(target)
        or os.path.isfile(os.path.join(target, "index.html"))
        or os.path.isfile(target.rstrip("/") + ".html")
    )


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    public_dir = sys.argv[1]
    netlify_toml = sys.argv[2] if len(sys.argv) > 2 else None
    redirects = load_redirects(public_dir, netlify_toml)

    broken = defaultdict(set)
    redirected = defaultdict(set)
    checked = set()
    pages = 0
    for root, _, files in os.walk(public_dir):
        for name in files:
            if not name.endswith(".html"):
                continue
            pages += 1
            file_path = os.path.join(root, name)
            rel = os.path.relpath(file_path, public_dir).replace(os.sep, "/")
            page_url = "https://albertlg.com/" + (rel[: -len("index.html")] if rel.endswith("index.html") else rel)
            parser = LinkParser()
            with open(file_path, encoding="utf-8", errors="replace") as f:
                parser.feed(f.read())
            for link in parser.links:
                path = site_path(link, page_url)
                if path is None:
                    continue
                checked.add(path)
                if exists(public_dir, path):
                    continue
                if any(p.match(path) for p in redirects):
                    redirected[path].add("/" + rel)
                else:
                    broken[path].add("/" + rel)

    print(f"Checked {len(checked)} internal links in {pages} HTML files.")
    report(redirected, "warning", "Link goes through a redirect:")
    report(broken, "error", "Broken link:")
    print(f"{len(broken)} broken, {len(redirected)} through a redirect.")
    return 1 if broken else 0


def report(links, level, label):
    for path in sorted(links):
        found_in = sorted(links[path])
        more = f" (+{len(found_in) - 3} more)" if len(found_in) > 3 else ""
        print(f"::{level}::{label} {path} in {', '.join(found_in[:3])}{more}")


if __name__ == "__main__":
    sys.exit(main())
