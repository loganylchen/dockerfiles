#!/usr/bin/env python3
"""
Check upstream sources for newer versions of tools.

Reads tool_sources.yaml for source mappings, compares with versions.txt,
and reports any newer versions available.

Usage:
    python3 check_updates.py              # Print updates to stdout
    python3 check_updates.py --markdown   # Output as GitHub-flavored markdown
"""

import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

import yaml

TOOLS_DIR = Path("tools")
SOURCES_FILE = Path("tool_sources.yaml")


def load_sources():
    with open(SOURCES_FILE) as f:
        return yaml.safe_load(f)


def get_current_versions(tool_name):
    """Read versions from tools/<name>/versions.txt."""
    vf = TOOLS_DIR / tool_name / "versions.txt"
    if not vf.exists():
        return []
    return [l.strip() for l in vf.read_text().splitlines()
            if l.strip() and not l.startswith("#")]


def fetch_json(url):
    """Fetch JSON from a URL with a timeout."""
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
        print(f"  Warning: failed to fetch {url}: {e}", file=sys.stderr)
        return None


def get_github_latest(repo, tag_prefix="v"):
    """Get the latest non-prerelease version from GitHub Releases."""
    url = f"https://api.github.com/repos/{repo}/releases?per_page=10"
    data = fetch_json(url)
    if not data:
        return None

    for release in data:
        if release.get("prerelease") or release.get("draft"):
            continue
        tag = release.get("tag_name", "")
        if tag_prefix and tag.startswith(tag_prefix):
            return tag[len(tag_prefix):]
        elif not tag_prefix:
            return tag
    return None


def get_pypi_latest(package):
    """Get the latest version from PyPI."""
    url = f"https://pypi.org/pypi/{package}/json"
    data = fetch_json(url)
    if not data:
        return None
    return data.get("info", {}).get("version")


def check_tool(name, config):
    """Check a single tool for updates. Returns (name, current, latest) or None."""
    source = config.get("source")
    current_versions = get_current_versions(name)
    if not current_versions:
        return None

    latest = None
    if source == "github":
        repo = config.get("repo")
        prefix = config.get("tag_prefix", "v")
        latest = get_github_latest(repo, prefix)
    elif source == "pypi":
        package = config.get("package")
        latest = get_pypi_latest(package)

    if latest and latest not in current_versions:
        return (name, current_versions[0], latest)
    return None


def main():
    markdown = "--markdown" in sys.argv
    sources = load_sources()
    updates = []

    for name, config in sorted(sources.items()):
        if not (TOOLS_DIR / name / "Dockerfile").exists():
            continue
        result = check_tool(name, config)
        if result:
            updates.append(result)

    if not updates:
        if markdown:
            print("No version updates found.")
        else:
            print("All tools are up to date.")
        return

    if markdown:
        print("## Version Updates Available\n")
        print("| Tool | Current | Latest | Source |")
        print("|------|---------|--------|--------|")
        for name, current, latest in updates:
            src = sources[name]
            if src["source"] == "github":
                link = f"[GitHub](https://github.com/{src['repo']}/releases)"
            else:
                link = f"[PyPI](https://pypi.org/project/{src['package']}/)"
            print(f"| {name} | `{current}` | `{latest}` | {link} |")
        print(f"\n{len(updates)} tool(s) have updates available.")
    else:
        print(f"Found {len(updates)} update(s):\n")
        for name, current, latest in updates:
            print(f"  {name}: {current} -> {latest}")


if __name__ == "__main__":
    main()
