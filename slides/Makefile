# Makefile for the F(AI)^2R slide decks.
# Renders both decks to PDF (and PPTX where the toolchain supports it)
# using the Marp CLI with the vendored DLR theme. Marp is required at
# build time but not as a runtime dependency: the deck Markdown is the
# source of truth, the rendered .pdf and .pptx are derived artefacts.
#
# Usage:
#     make             # build both decks to dist/
#     make pitch       # build pitch-5min.pdf only
#     make conference  # build conference-30min.pdf only
#     make watch       # serve the pitch deck live during authoring
#     make clean       # remove dist/

MARP    ?= npx --yes -p @marp-team/marp-cli marp
THEME   := static/dlr/dlr.css
DIST    := dist
PITCH   := pitch-5min
CONF    := conference-30min

.PHONY: all pitch conference watch clean

all: pitch conference

pitch: | $(DIST)
	$(MARP) --theme $(THEME) --pdf -o $(DIST)/$(PITCH).pdf $(PITCH).md
	$(MARP) --theme $(THEME) --pptx -o $(DIST)/$(PITCH).pptx $(PITCH).md || true
	$(MARP) --theme $(THEME) --html -o $(DIST)/$(PITCH).html $(PITCH).md

conference: | $(DIST)
	$(MARP) --theme $(THEME) --pdf -o $(DIST)/$(CONF).pdf $(CONF).md
	$(MARP) --theme $(THEME) --pptx -o $(DIST)/$(CONF).pptx $(CONF).md || true
	$(MARP) --theme $(THEME) --html -o $(DIST)/$(CONF).html $(CONF).md

watch: | $(DIST)
	$(MARP) --theme $(THEME) -s . --watch

$(DIST):
	mkdir -p $(DIST)

clean:
	rm -rf $(DIST)
