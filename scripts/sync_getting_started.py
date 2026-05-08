#!/usr/bin/env python3
"""Sync the auto-generated block(s) of ``site/getting-started.md`` from
the canonical sources of truth (``CLAUDE.md``, ``agents/*.md``).

The getting-started page hands a new adopter an initialisation prompt
plus the ground rules they will be bound by. Those rules live in
``CLAUDE.md``; if the page were hand-edited they would drift. This
script reads ``CLAUDE.md`` and rewrites the contents between

    <!-- BEGIN AUTO-SYNCED: ground-rules -->
    ...
    <!-- END AUTO-SYNCED: ground-rules -->

so the page always reflects the live binding rules.

Run before ``scripts/build_provenance_site.py``; idempotent.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAUDE_MD = ROOT / "CLAUDE.md"
PAGE = ROOT / "site" / "getting-started.md"

BEGIN = "<!-- BEGIN AUTO-SYNCED: ground-rules -->"
END = "<!-- END AUTO-SYNCED: ground-rules -->"


def _extract_ground_rules(claude_md_text: str) -> str:
    """Pull the ``## Ground rules`` section out of ``CLAUDE.md``."""
    lines = claude_md_text.splitlines()
    out: list[str] = []
    in_section = False
    for line in lines:
        if line.startswith("## Ground rules"):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section:
            out.append(line)
    text = "\n".join(out).strip()
    if not text:
        raise SystemExit(
            "ERROR: could not find '## Ground rules' section in CLAUDE.md"
        )
    return text


def _build_block(rules_body: str) -> str:
    """Compose the auto-synced block body."""
    header = (
        "_Auto-synced from `CLAUDE.md` by `scripts/sync_getting_started.py`."
        " Do not edit in place — edit `CLAUDE.md` and rebuild._\n"
    )
    intro = (
        "These are the rules the canonical repository runs under. The"
        " initialization prompt above hands the same rules to a new"
        " adopter; the block below is the source of truth as of the"
        " last site build.\n"
    )
    return f"{header}\n{intro}\n### Ground rules (live from CLAUDE.md)\n\n{rules_body}\n"


def main() -> None:
    if not CLAUDE_MD.is_file():
        raise SystemExit(f"ERROR: {CLAUDE_MD} not found")
    if not PAGE.is_file():
        raise SystemExit(f"ERROR: {PAGE} not found")

    rules = _extract_ground_rules(CLAUDE_MD.read_text(encoding="utf-8"))
    block_body = _build_block(rules)

    page_text = PAGE.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"{re.escape(BEGIN)}.*?{re.escape(END)}",
        re.DOTALL,
    )
    if not pattern.search(page_text):
        raise SystemExit(
            f"ERROR: sync markers not found in {PAGE}.\n"
            f"Expected '{BEGIN}' ... '{END}'."
        )
    replacement = f"{BEGIN}\n{block_body}\n{END}"
    new_text = pattern.sub(replacement, page_text)
    if new_text != page_text:
        PAGE.write_text(new_text, encoding="utf-8")
        print(f"sync_getting_started: updated {PAGE.relative_to(ROOT)}")
    else:
        print("sync_getting_started: already in sync")


if __name__ == "__main__":
    main()
