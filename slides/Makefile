# Makefile for the F(AI)^2R slide decks.
# The DLR Marp theme references ./assets/*.png plates that headless
# Chromium cannot resolve through Marp's CSS @url(...) cleanly; the
# canonical marp-dlr framework solves that by inlining the assets as
# base64 data: URIs. We do the same via scripts/build_slides.py so the
# slide build matches the upstream behaviour without a Node toolchain.
#
# Usage:
#     make             # build both decks (PDF + PPTX + HTML)
#     make pitch       # build pitch-5min only
#     make conference  # build conference-30min only
#     make watch       # serve the pitch deck live during authoring
#     make clean       # remove dist/

PYTHON  ?= python3
DIST    := dist

.PHONY: all pitch conference watch clean

all: pitch conference

pitch: | $(DIST)
	cd .. && $(PYTHON) scripts/build_slides.py pitch

conference: | $(DIST)
	cd .. && $(PYTHON) scripts/build_slides.py conference

watch: | $(DIST)
	# Watch mode does not benefit from the asset-inlining preprocessor
	# (Marp's --watch needs to re-read the theme from disk), so this
	# falls back to direct Marp with the raw theme file. Use this for
	# fast authoring iteration only; for the canonical render run
	# `make pitch` or `make conference`.
	npx --yes -p @marp-team/marp-cli marp \
	    --theme static/dlr/dlr.css --allow-local-files \
	    -s . --watch

$(DIST):
	mkdir -p $(DIST)

clean:
	rm -rf $(DIST)
