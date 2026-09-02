#!/usr/bin/env python3
"""
Rebuilds the combined JellyUX plugin manifest.

Each JellyUX plugin repository publishes its own ``manifest.json`` (a JSON array
with a single plugin object). This script fetches every source listed in
``sources.json`` and concatenates their plugin objects into the repository-root
``manifest.json`` that users add to Jellyfin.

Run from the repository root:  python scripts/merge_manifests.py
"""
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = ROOT / "sources.json"
OUTPUT_FILE = ROOT / "manifest.json"


def fetch(url: str) -> list:
    req = urllib.request.Request(url, headers={"User-Agent": "jellyux-manifest-sync"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    if not isinstance(data, list):
        raise ValueError(f"{url} did not return a JSON array")
    return data


def main() -> None:
    sources = json.loads(SOURCES_FILE.read_text(encoding="utf-8"))["sources"]

    plugins: list = []
    seen: set = set()
    for url in sources:
        for plugin in fetch(url):
            guid = plugin.get("guid")
            if guid in seen:
                print(f"WARNING: duplicate guid {guid} from {url}, skipped", file=sys.stderr)
                continue
            seen.add(guid)
            plugins.append(plugin)

    plugins.sort(key=lambda p: p.get("name", "").lower())

    OUTPUT_FILE.write_text(
        json.dumps(plugins, indent=4, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"manifest.json rebuilt: {len(plugins)} plugin(s) from {len(sources)} source(s)")


if __name__ == "__main__":
    main()
