#!/usr/bin/env python3
"""Refresh catalog.json from GitHub and add new libraries.

  python3 scripts/refresh_catalog.py                       # refresh stars / pushed / license / archived / latest tag / SPM for every entry
  python3 scripts/refresh_catalog.py --add EmergeTools/Pow --category Animation --tags swiftui,effects [--title Pow] [--summary "..."] [--featured]

Needs an authenticated `gh` (GITHUB_TOKEN in Actions). Entries whose repository cannot be
read keep their previous numbers. `stats_as_of` is set to today. After a refresh run
`python3 scripts/render.py` so README.md, llms.txt and docs/ match catalog.json.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
CATEGORIES = ["Alert", "Animation", "Collection View", "Indicator", "Menu", "Table View", "Transition", "UI"]


def gh(path: str) -> dict | list | None:
    result = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    if result.returncode != 0:
        return None
    return json.loads(result.stdout)


def repo_info(full: str) -> dict | None:
    info = gh(f"repos/{full}")
    if not isinstance(info, dict):
        return None
    try:
        urllib.request.urlopen(urllib.request.Request(f"https://raw.githubusercontent.com/{info['full_name']}/{info['default_branch']}/Package.swift"), timeout=15)
        info["spm"] = True
    except Exception:
        info["spm"] = False
    release = gh(f"repos/{full}/releases/latest")
    tags = gh(f"repos/{full}/tags?per_page=1")
    info["latest_tag"] = (release or {}).get("tag_name") if isinstance(release, dict) else None
    if not info["latest_tag"] and isinstance(tags, list) and tags:
        info["latest_tag"] = tags[0].get("name")
    return info


def full_name(url: str) -> str:
    return "/".join(url.rstrip("/").split("/")[-2:])


def spm_line(url: str, tag: str | None) -> str | None:
    if not tag or not re.match(r"^v?\d", tag):
        return None
    return f'.package(url: "{url}", from: "{tag.lstrip("v")}")'


def apply(entry: dict, info: dict) -> None:
    entry["stars"] = info.get("stargazers_count")
    entry["pushed"] = (info.get("pushed_at") or "")[:10] or entry.get("pushed")
    license_id = (info.get("license") or {}).get("spdx_id") if isinstance(info.get("license"), dict) else info.get("license")
    if license_id and license_id != "NOASSERTION":
        entry["license"] = license_id
    entry["archived"] = bool(info.get("archived"))
    entry["url"] = f"https://github.com/{info['full_name']}"
    entry["latest_tag"] = info.get("latest_tag") or entry.get("latest_tag")
    install = entry.setdefault("install", {"spm": False, "spm_package": None, "cocoapods": False, "carthage": False})
    install["spm"] = bool(info.get("spm"))
    install["spm_package"] = spm_line(entry["url"], entry["latest_tag"]) if install["spm"] else None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--add", action="append", default=[], help="owner/repo to add (repeatable)")
    parser.add_argument("--category", choices=CATEGORIES, help="category for --add entries")
    parser.add_argument("--tags", default="", help="comma separated tags for --add entries")
    parser.add_argument("--title", help="title override for a single --add")
    parser.add_argument("--summary", help="summary override for a single --add")
    parser.add_argument("--featured", action="store_true")
    parser.add_argument("--no-refresh", action="store_true", help="skip refreshing existing entries")
    args = parser.parse_args()

    doc = json.loads(CATALOG.read_text())
    libraries: list[dict] = doc["libraries"]
    by_url = {full_name(e["url"]).lower(): e for e in libraries}

    for full in args.add:
        if full.lower() in by_url:
            print(f"skip {full}: already in catalog as {by_url[full.lower()]['title']}")
            continue
        info = repo_info(full)
        if info is None:
            raise SystemExit(f"cannot read {full}")
        if not args.category:
            raise SystemExit("--category is required with --add")
        entry = {
            "title": args.title if (args.title and len(args.add) == 1) else full.split("/")[1],
            "author": full.split("/")[0],
            "category": args.category,
            "summary": (args.summary if (args.summary and len(args.add) == 1) else (info.get("description") or "")).strip(),
            "url": f"https://github.com/{info['full_name']}",
            "tags": [t.strip() for t in args.tags.split(",") if t.strip()],
            "featured": args.featured,
            "gif": None,
            "stars": None, "pushed": None, "license": None, "archived": False,
            "latest_tag": None,
            "install": {"spm": False, "spm_package": None, "cocoapods": False, "carthage": False},
            "live_demo": False,
            "verified": None,
        }
        apply(entry, info)
        libraries.append(entry)
        by_url[full.lower()] = entry
        print(f"added {entry['title']} ({entry['stars']}★, {entry['pushed']}, tag {entry['latest_tag']})")

    if not args.no_refresh:
        for entry in libraries:
            info = repo_info(full_name(entry["url"]))
            if info is None:
                print(f"keep {entry['title']}: repo unreadable")
                continue
            apply(entry, info)

    titles = [e["title"] for e in libraries]
    if len(set(titles)) != len(titles):
        raise SystemExit("duplicate titles: " + ", ".join(t for t in titles if titles.count(t) > 1))
    libraries.sort(key=lambda e: (-(e.get("stars") or 0), e["title"].lower()))
    doc["stats_as_of"] = dt.date.today().isoformat()
    CATALOG.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print(f"catalog: {len(libraries)} libraries, stats as of {doc['stats_as_of']}")


if __name__ == "__main__":
    main()
