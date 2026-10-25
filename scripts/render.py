#!/usr/bin/env python3
"""Render README.md, llms.txt and docs/index.html from catalog.json (the single source of truth).

  python3 scripts/render.py          # write the three generated files
  python3 scripts/render.py --check  # exit 1 if any generated file is stale or catalog.json is invalid
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
SCHEMA = ROOT / "schema" / "catalog.schema.json"
INACTIVE_BEFORE = "2021-01-01"
CATEGORY_ORDER = ["Animation", "Transition", "UI", "Menu", "Alert", "Collection View", "Table View", "Indicator"]
APP_STORE = "https://apps.apple.com/app/id1205163580"


def load() -> dict:
    return json.loads(CATALOG.read_text())


def validate(doc: dict) -> list[str]:
    """Stdlib-only checks that mirror schema/catalog.schema.json."""
    schema = json.loads(SCHEMA.read_text())
    categories = schema["properties"]["libraries"]["items"]["properties"]["category"]["enum"]
    problems: list[str] = []
    for key in schema["required"]:
        if key not in doc:
            problems.append(f"missing top-level key {key}")
    if doc.get("schema_version") != "motionbook.catalog.v2":
        problems.append("schema_version must be motionbook.catalog.v2")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(doc.get("stats_as_of", ""))):
        problems.append("stats_as_of must be YYYY-MM-DD")
    titles: list[str] = []
    for entry in doc.get("libraries", []):
        name = entry.get("title", "<untitled>")
        titles.append(name)
        for key in schema["properties"]["libraries"]["items"]["required"]:
            if key not in entry:
                problems.append(f"{name}: missing {key}")
        if entry.get("category") not in categories:
            problems.append(f"{name}: unknown category {entry.get('category')}")
        if not re.match(r"^https://github\.com/[^/]+/[^/]+$", entry.get("url", "")):
            problems.append(f"{name}: url must be https://github.com/owner/repo")
        gif = entry.get("gif")
        if gif and not (ROOT / gif).is_file():
            problems.append(f"{name}: gif {gif} is not in the repository")
        if entry.get("live_demo") and not entry.get("verified"):
            problems.append(f"{name}: live_demo entries need a verified stamp")
        install = entry.get("install") or {}
        for flag in ("spm", "cocoapods", "carthage"):
            if not isinstance(install.get(flag), bool):
                problems.append(f"{name}: install.{flag} must be a boolean")
    dupes = sorted({t for t in titles if titles.count(t) > 1})
    if dupes:
        problems.append("duplicate titles: " + ", ".join(dupes))
    return problems


def is_inactive(entry: dict) -> bool:
    return bool(entry.get("archived")) or (entry.get("pushed") or "9999") < INACTIVE_BEFORE


def stars(entry: dict) -> str:
    value = entry.get("stars")
    if value is None:
        return "–"
    if value >= 10_000:
        return f"{value / 1000:.0f}K"
    if value >= 1_000:
        return f"{value / 1000:.1f}K"
    return str(value)


def badges(entry: dict) -> list[str]:
    out = []
    if entry.get("live_demo"):
        out.append("▶ Live demo in the app")
    if "swiftui" in entry.get("tags", []):
        out.append("SwiftUI")
    install = entry.get("install", {})
    if install.get("spm"):
        out.append("SPM")
    if install.get("cocoapods"):
        out.append("CocoaPods")
    if install.get("carthage"):
        out.append("Carthage")
    if entry.get("archived"):
        out.append("Archived")
    elif is_inactive(entry):
        out.append(f"Inactive since {entry['pushed'][:4]}")
    return out


def by_category(doc: dict) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {c: [] for c in CATEGORY_ORDER}
    for entry in doc["libraries"]:
        groups.setdefault(entry["category"], []).append(entry)
    for items in groups.values():
        items.sort(key=lambda e: (-(e.get("stars") or 0), e["title"].lower()))
    return groups


def render_readme(doc: dict) -> str:
    libs = doc["libraries"]
    live = [e for e in libs if e.get("live_demo")]
    swiftui = [e for e in libs if "swiftui" in e.get("tags", [])]
    inactive = [e for e in libs if is_inactive(e)]
    lines = [
        "# 📖 MotionBook — iOS motion libraries, catalogued for people and agents",
        "",
        "[![Platform](https://img.shields.io/badge/platform-iOS-green.svg?style=flat)](https://developer.apple.com/ios/)",
        "![Language](https://img.shields.io/badge/language-Swift-brightgreen.svg?style=flat)",
        "[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg?style=flat)](LICENSE)",
        "[![Catalog](https://img.shields.io/badge/catalog-" + str(len(libs)) + "%20libraries-ee165b.svg?style=flat)](catalog.json)",
        "[![Refresh](https://github.com/younatics/MotionBook/actions/workflows/refresh.yml/badge.svg)](https://github.com/younatics/MotionBook/actions/workflows/refresh.yml)",
        "",
        f'<a href="{APP_STORE}"><img src="Images/appstore.png" width="170" height="58" alt="Download on the App Store"></a>',
        "",
        f"**{len(libs)} open-source motion, transition and UI libraries for iOS**, with the real thing running inside the "
        f"[MotionBook app]({APP_STORE}) for {len(live)} of them. Every entry carries its GitHub stars, last push, license, "
        "latest tag, how to install it (Swift Package Manager / CocoaPods / Carthage) and, for the live ones, the Xcode "
        "version it was last built and run with.",
        "",
        "- **People**: browse the list below or the [web catalog](https://younatics.github.io/MotionBook/) with previews.",
        "- **Agents and tools**: read [`catalog.json`](catalog.json) (schema: [`schema/catalog.schema.json`](schema/catalog.schema.json)) "
        "or [`llms.txt`](llms.txt). Everything on this page is generated from that file by `scripts/render.py`.",
        f"- **Freshness**: GitHub numbers refreshed `{doc['stats_as_of']}` by the weekly [refresh workflow](.github/workflows/refresh.yml); "
        f"{len(swiftui)} SwiftUI-era libraries, {len(inactive)} marked inactive (no push since {INACTIVE_BEFORE[:4]}) or archived.",
        "",
        "## Use it from an agent",
        "",
        "```bash",
        "# all SwiftUI libraries that still get commits, as install lines",
        "curl -s https://raw.githubusercontent.com/younatics/MotionBook/master/catalog.json \\",
        "  | jq -r '.libraries[] | select(.tags | index(\"swiftui\")) | select(.archived | not) | .install.spm_package // .url'",
        "```",
        "",
        "Each library object has: `title`, `author`, `category`, `summary`, `url`, `tags`, `featured`, `gif`, `stars`, `pushed`, "
        "`license`, `archived`, `latest_tag`, `install.{spm,spm_package,cocoapods,carthage}`, `live_demo`, `verified.{date,xcode,ios,via}`.",
        "",
        "## Contribute",
        "",
        "Add a library with one command and open a pull request — see [CONTRIBUTING.md](CONTRIBUTING.md):",
        "",
        "```bash",
        "python3 scripts/refresh_catalog.py --add owner/repo --category Animation --tags swiftui,effects --no-refresh",
        "python3 scripts/render.py",
        "```",
        "",
        "## Libraries",
        "",
        "Grouped by category, sorted by stars. ★ = GitHub stars · ⟳ = last push · badges: ▶ live in the app, SwiftUI, SPM, CocoaPods, Carthage, Archived / Inactive.",
        "",
    ]
    groups = by_category(doc)
    lines.append(" · ".join(f"[{c}](#{c.lower().replace(' ', '-')}) ({len(groups[c])})" for c in CATEGORY_ORDER if groups.get(c)))
    lines.append("")
    for category in CATEGORY_ORDER:
        items = groups.get(category) or []
        if not items:
            continue
        lines += [f"### {category}", ""]
        for e in items:
            meta = [f"★ {stars(e)}"]
            if e.get("pushed"):
                meta.append(f"⟳ {e['pushed'][:7]}")
            if e.get("license"):
                meta.append(e["license"])
            if e.get("latest_tag"):
                meta.append(f"tag `{e['latest_tag']}`")
            lines.append(f"#### [{e['title']}]({e['url']})")
            lines.append(f"{e['author']} · " + " · ".join(meta))
            lines.append("")
            lines.append(e["summary"].strip() or "_No description._")
            lines.append("")
            badge_text = " · ".join(f"`{b}`" for b in badges(e))
            extras = []
            if e.get("gif"):
                extras.append(f"[preview GIF]({e['gif']})")
            if e.get("install", {}).get("spm_package"):
                extras.append(f"`{e['install']['spm_package']}`")
            if badge_text or extras:
                lines.append(" · ".join([badge_text] + extras).strip(" ·"))
                lines.append("")
    lines += [
        "## About",
        "",
        "MotionBook started in 2017 as the catalog behind the [MotionBook iOS app](" + APP_STORE + ") (Apple featured it as a "
        "best new app). The 2026 app runs the libraries live again on the current SDK; this repository is the list the app, "
        "its users and coding agents read. GIFs under `motion-book/` are the app's preview assets. `Data/motionbook.json` is the "
        "2017 format kept for old clients.",
        "",
        "Made by [younatics](https://github.com/younatics). MIT.",
        "",
    ]
    return "\n".join(lines)


def render_llms(doc: dict) -> str:
    lines = [
        "# MotionBook",
        "",
        f"> Catalog of {len(doc['libraries'])} open-source iOS motion, transition and UI libraries, maintained by younatics. "
        f"The MotionBook iOS app runs {sum(1 for e in doc['libraries'] if e.get('live_demo'))} of them live. "
        f"Stats as of {doc['stats_as_of']}.",
        "",
        "Use catalog.json for structured data (schema in schema/catalog.schema.json). Each entry has stars, last push, license, "
        "latest tag, install lines (SPM / CocoaPods / Carthage), a live-demo flag and the Xcode version it was last verified with. "
        "Entries with a live demo also carry `usage`: a minimal Swift snippet copied from the demo source, so it compiles against the "
        "pinned version; the same snippet is shown under the library below.",
        "",
        "## Catalog",
        "",
        "- [catalog.json](https://raw.githubusercontent.com/younatics/MotionBook/master/catalog.json): all libraries, machine-readable",
        "- [catalog.schema.json](https://raw.githubusercontent.com/younatics/MotionBook/master/schema/catalog.schema.json): JSON Schema",
        "- [README](https://github.com/younatics/MotionBook#readme): the same list for people",
        "- [Web catalog](https://younatics.github.io/MotionBook/): previews and filters",
        f"- [MotionBook app]({APP_STORE}): live demos on iPhone",
        "",
        "## Libraries",
        "",
    ]
    for category in CATEGORY_ORDER:
        items = by_category(doc).get(category) or []
        if not items:
            continue
        lines.append(f"### {category}")
        lines.append("")
        for e in items:
            flags = []
            if e.get("live_demo"):
                flags.append("live demo")
            if "swiftui" in e.get("tags", []):
                flags.append("SwiftUI")
            install = e.get("install", {})
            flags += [name for name, on in (("SPM", install.get("spm")), ("CocoaPods", install.get("cocoapods")), ("Carthage", install.get("carthage"))) if on]
            if e.get("archived"):
                flags.append("archived")
            elif is_inactive(e):
                flags.append("inactive")
            summary = (e["summary"].strip() or "no description").replace("\n", " ")
            lines.append(f"- [{e['title']}]({e['url']}): {summary} ({stars(e)} stars, pushed {e.get('pushed') or 'unknown'}; {', '.join(flags) or 'manual install'})")
            if e.get("usage"):
                if e.get("usage_note"):
                    lines.append(f"  {e['usage_note']}")
                lines.append(f"  ```{e.get('usage_language', 'swift')}")
                lines += ["  " + l if l.strip() else "" for l in e["usage"].rstrip().splitlines()]
                lines.append("  ```")
        lines.append("")
    return "\n".join(lines)


def render_site(doc: dict) -> str:
    cards = []
    for e in sorted(doc["libraries"], key=lambda x: (-(x.get("stars") or 0), x["title"].lower())):
        gif = f'<img loading="lazy" src="{html.escape(doc["gif_base_url"] + e["gif"])}" alt="{html.escape(e["title"])} preview">' if e.get("gif") else '<div class="nogif">no preview</div>'
        tags = " ".join(f'<span class="badge">{html.escape(b)}</span>' for b in badges(e))
        spm = e.get("install", {}).get("spm_package")
        install = f'<code>{html.escape(spm)}</code>' if spm else ""
        if e.get("usage"):
            note = f'<p>{html.escape(e["usage_note"])}</p>' if e.get("usage_note") else ""
            install += f'<details><summary>Usage</summary>{note}<pre>{html.escape(e["usage"].rstrip())}</pre></details>'
        cards.append(
            f'<article class="card" data-category="{html.escape(e["category"])}" data-live="{str(bool(e.get("live_demo"))).lower()}" '
            f'data-swiftui="{str("swiftui" in e.get("tags", [])).lower()}" data-inactive="{str(is_inactive(e)).lower()}">'
            f'{gif}<h3><a href="{html.escape(e["url"])}">{html.escape(e["title"])}</a></h3>'
            f'<p class="meta">{html.escape(e["author"])} · ★ {stars(e)} · ⟳ {html.escape((e.get("pushed") or "?")[:7])} · {html.escape(e.get("license") or "")}</p>'
            f'<p>{html.escape(e["summary"].strip())}</p><p>{tags}</p>{install}</article>'
        )
    categories = "".join(f'<option value="{c}">{c}</option>' for c in CATEGORY_ORDER)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>MotionBook — {len(doc['libraries'])} iOS motion libraries</title>
<link rel="icon" href="data:,">
<style>
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;margin:0;background:#f8fafc;color:#111827}}
header{{padding:28px 20px 12px;max-width:1200px;margin:0 auto}}h1{{margin:0 0 6px;font-size:28px}}
.controls{{display:flex;gap:10px;flex-wrap:wrap;padding:0 20px 16px;max-width:1200px;margin:0 auto}}
select,input,label{{font-size:15px}}input{{padding:8px 10px;border:1px solid #cbd5e1;border-radius:10px;min-width:220px}}
select{{padding:8px;border:1px solid #cbd5e1;border-radius:10px}}
main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;padding:0 20px 40px;max-width:1200px;margin:0 auto}}
.card{{background:#fff;border-radius:16px;padding:14px;box-shadow:0 1px 3px rgba(0,0,0,.08);display:flex;flex-direction:column;gap:6px}}
.card img,.nogif{{width:100%;aspect-ratio:9/16;object-fit:cover;border-radius:12px;background:#e5e7eb}}
.nogif{{display:flex;align-items:center;justify-content:center;color:#6b7280;font-size:13px;aspect-ratio:9/4}}
.card h3{{margin:6px 0 0;font-size:17px}}.card a{{color:#ee165b;text-decoration:none}}.meta{{color:#5b6674;font-size:13px;margin:0}}
.card details{{font-size:13px}}.card summary{{cursor:pointer;color:#5b6674}}.card pre{{margin:6px 0 0;padding:8px;background:#f3f4f6;border-radius:8px;font-size:12px;overflow:auto;white-space:pre}}
.card p{{margin:0;font-size:14px}}.badge{{display:inline-block;background:#fde7ee;color:#ee165b;border-radius:999px;padding:2px 8px;font-size:12px;margin:2px 4px 0 0}}
code{{font-size:12px;background:#f1f5f9;border-radius:8px;padding:6px 8px;overflow-wrap:anywhere;display:block}}
.hidden{{display:none}}footer{{text-align:center;color:#6b7280;font-size:13px;padding:0 20px 40px}}
</style></head><body>
<header><h1>📖 MotionBook</h1><p>{len(doc['libraries'])} open-source iOS motion libraries · stats as of {doc['stats_as_of']} · <a href="https://github.com/younatics/MotionBook">GitHub</a> · <a href="https://raw.githubusercontent.com/younatics/MotionBook/master/catalog.json">catalog.json</a> · <a href="{APP_STORE}">App Store</a></p></header>
<div class="controls"><input id="q" placeholder="Search title, author, tags…"><select id="cat"><option value="">All categories</option>{categories}</select>
<label><input type="checkbox" id="live"> Live in the app</label><label><input type="checkbox" id="swiftui"> SwiftUI</label><label><input type="checkbox" id="active" checked> Hide inactive</label></div>
<main id="grid">{''.join(cards)}</main>
<footer>Generated from catalog.json by scripts/render.py · MIT · younatics</footer>
<script>
const q=document.getElementById('q'),cat=document.getElementById('cat'),live=document.getElementById('live'),sw=document.getElementById('swiftui'),act=document.getElementById('active');
function apply(){{const t=q.value.toLowerCase();document.querySelectorAll('.card').forEach(c=>{{const ok=(!cat.value||c.dataset.category===cat.value)&&(!live.checked||c.dataset.live==='true')&&(!sw.checked||c.dataset.swiftui==='true')&&(!act.checked||c.dataset.inactive==='false')&&(!t||c.textContent.toLowerCase().includes(t));c.classList.toggle('hidden',!ok);}});}}
[q,cat,live,sw,act].forEach(el=>el.addEventListener('input',apply));apply();
</script></body></html>
"""


def render_robots(doc: dict) -> str:
    return "User-agent: *\nAllow: /\n"


def render_catalog_copy(doc: dict) -> str:
    """The site serves only docs/, so agents get /catalog.json and /llms.txt next to the page."""
    return json.dumps(doc, indent=1, ensure_ascii=False) + "\n"


OUTPUTS = {
    "README.md": render_readme,
    "llms.txt": render_llms,
    "docs/index.html": render_site,
    # GitHub Pages publishes docs/ only: without these copies https://younatics.github.io/MotionBook/llms.txt
    # and /catalog.json were 404 (2026-10-25), i.e. invisible to agents that look for the llms.txt convention.
    "docs/llms.txt": render_llms,
    "docs/catalog.json": render_catalog_copy,
    "docs/robots.txt": render_robots,
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="validate catalog.json and fail if generated files are stale")
    args = parser.parse_args()
    doc = load()
    problems = validate(doc)
    if problems:
        print("catalog.json problems:\n  " + "\n  ".join(problems))
        return 1
    stale = []
    for name, renderer in OUTPUTS.items():
        path = ROOT / name
        content = renderer(doc)
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            print(f"wrote {name} ({len(content.splitlines())} lines)")
    if args.check:
        if stale:
            print("stale generated files (run python3 scripts/render.py): " + ", ".join(stale))
            return 1
        print(f"catalog.json valid ({len(doc['libraries'])} libraries); README.md, llms.txt and docs/index.html are up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
