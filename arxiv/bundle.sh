#!/usr/bin/env bash
# arxiv/bundle.sh --- assemble an arXiv-ready tarball.
# Guarded by paper/publication-consent.md.
set -euo pipefail

cd "$(dirname "$0")/.."
if ! grep -q '^\*\*Authorised:\*\* [0-9]' paper/publication-consent.md; then
  echo "ERROR: paper/publication-consent.md Authorised field is unset."
  echo "       Edit that file before running this script."
  exit 1
fi

VERSION="$(date +%Y%m%d)"
OUT="arxiv/f-ai-r-${VERSION}.tar.gz"

echo ">>> Building paper PDF..."
(cd paper && make pdf >/dev/null)

echo ">>> Assembling tarball: $OUT"
tar --transform 's,^,f-ai-r/,' \
    -czf "$OUT" \
    paper/main.tex \
    paper/main.pdf \
    paper/references.bib \
    paper/style/fair2r.sty \
    paper/sections/*.tex \
    paper/sections/_generated/*.tex \
    paper/figures/*.tex \
    paper/figures/*.pdf

echo "Done. Upload $OUT to arXiv."
