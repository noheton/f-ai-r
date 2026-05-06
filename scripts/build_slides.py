#!/usr/bin/env python3
"""Render the F(AI)^2R slide decks via Marp + the DLR theme.

The DLR Marp theme references background plates (``url('./assets/...')``)
that headless Chromium cannot reliably resolve when Marp is invoked from
an arbitrary working directory. The canonical ``marp-dlr`` framework's
``scripts/run-marp.mjs`` solves this by inlining those references as
base64 data URIs before Marp ever sees them; we port the same idea to
Python so the slide build does not depend on a Node build of the
upstream framework.

Usage::

    python scripts/build_slides.py            # build both decks (PDF/PPTX/HTML)
    python scripts/build_slides.py pitch      # pitch deck only
    python scripts/build_slides.py conference # conference deck only

Marp CLI is invoked via ``npx --yes -p @marp-team/marp-cli marp``
(the same path as the Makefile), so no additional Python deps are
required beyond the standard library.
"""
from __future__ import annotations

import base64
import mimetypes
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLIDES = ROOT / "slides"
THEME = SLIDES / "static" / "dlr" / "dlr.css"
ASSETS = SLIDES / "static" / "dlr" / "assets"
DIST = SLIDES / "dist"

DECKS = {
    "pitch": SLIDES / "pitch-5min.md",
    "conference": SLIDES / "conference-30min.md",
}

URL_RE = re.compile(r"url\((['\"]?)(\.{0,2}/?assets/[^'\")]+)\1\)")


def inline_assets(css_path: Path) -> str:
    """Return the theme CSS with every ``url('assets/...')`` reference
    replaced by an inline base64 ``data:`` URI. The asset path is resolved
    relative to the CSS file. Files that don't exist are left untouched
    so a stylesheet error remains visible rather than silently swallowed.
    """
    css = css_path.read_text(encoding="utf-8")

    def _replace(match: re.Match[str]) -> str:
        quote = match.group(1)
        rel = match.group(2)
        # Strip any leading ./ or / so the join is well-behaved.
        clean_rel = rel.lstrip("./").lstrip("/")
        asset = (css_path.parent / clean_rel).resolve()
        if not asset.is_file():
            return match.group(0)
        mime, _ = mimetypes.guess_type(asset.name)
        if mime is None:
            mime = "application/octet-stream"
        data = base64.b64encode(asset.read_bytes()).decode("ascii")
        return f"url({quote}data:{mime};base64,{data}{quote})"

    return URL_RE.sub(_replace, css)


def run_marp(deck: Path, theme: Path, out_dir: Path, fmt: str) -> int:
    out = out_dir / f"{deck.stem}.{fmt}"
    cmd = [
        "npx",
        "--yes",
        "-p",
        "@marp-team/marp-cli",
        "marp",
        "--theme",
        str(theme),
        f"--{fmt}",
        "--allow-local-files",
        "-o",
        str(out),
        str(deck),
    ]
    print(f"--> {fmt.upper()} {deck.name}: {out.relative_to(ROOT)}")
    return subprocess.call(cmd, cwd=ROOT)


def main(argv: list[str]) -> int:
    if not THEME.is_file():
        print(f"ERROR: theme not found at {THEME}", file=sys.stderr)
        return 1

    DIST.mkdir(parents=True, exist_ok=True)

    targets = list(DECKS.keys()) if not argv else [a for a in argv if a in DECKS]
    if not targets:
        print(f"Usage: {sys.argv[0]} [{'|'.join(DECKS)}]", file=sys.stderr)
        return 2

    # Materialise the inlined theme to a tempfile that lives for the
    # duration of the build; Marp reads from this path.
    inlined = inline_assets(THEME)
    with tempfile.NamedTemporaryFile(
        mode="w", suffix="-dlr-resolved.css", delete=False, encoding="utf-8"
    ) as f:
        f.write(inlined)
        tmp_theme = Path(f.name)

    try:
        rc = 0
        for name in targets:
            deck = DECKS[name]
            for fmt in ("pdf", "pptx", "html"):
                rc |= run_marp(deck, tmp_theme, DIST, fmt)
        return rc
    finally:
        try:
            os.unlink(tmp_theme)
        except OSError:
            pass


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
