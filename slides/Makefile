# Makefile for the F(AI)^2R slide decks (Beamer).
# Mirrors paper/Makefile in toolchain choice: latexmk + biber + the
# xu-cheng/latex-action container in CI. No Marp / Chromium / Node.

LATEXMK     ?= latexmk
LATEXMKOPTS ?= -pdf -interaction=nonstopmode -halt-on-error -file-line-error

PITCH       := pitch-5min
CONF        := conference-30min
POSTER      := poster-A0

.PHONY: all pitch conference poster watch clean distclean check

all: pitch conference poster

pitch: check
	$(LATEXMK) $(LATEXMKOPTS) $(PITCH).tex

conference: check
	$(LATEXMK) $(LATEXMKOPTS) $(CONF).tex

poster: check
	$(LATEXMK) $(LATEXMKOPTS) $(POSTER).tex

watch: check
	$(LATEXMK) $(LATEXMKOPTS) -pvc $(PITCH).tex

clean:
	$(LATEXMK) -c || true
	rm -f *.bbl *.run.xml *.snm *.nav *.vrb *.toc

distclean:
	$(LATEXMK) -C || true
	rm -f *.bbl *.run.xml *.snm *.nav *.vrb *.toc \
	      $(PITCH).pdf $(CONF).pdf $(POSTER).pdf

check:
	@command -v $(LATEXMK) >/dev/null 2>&1 || { \
	  echo "ERROR: latexmk not found. Install TeX Live or MacTeX."; exit 1; }
