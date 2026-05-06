# Makefile for the F(AI^2)R paper.
# Targets: pdf, condensed, all, figures, watch, clean, distclean, arxiv, check

LATEXMK     ?= latexmk
LATEXMKOPTS ?= -pdf -interaction=nonstopmode -halt-on-error -file-line-error

MAIN        := main
CONDENSED   := main-condensed

.PHONY: all pdf condensed figures watch clean distclean arxiv check

all: pdf condensed

pdf: check
	$(LATEXMK) $(LATEXMKOPTS) $(MAIN).tex

condensed: check
	$(LATEXMK) $(LATEXMKOPTS) $(CONDENSED).tex

figures:
	@echo "No automated figure pipeline yet. Drop sources into figures/."

watch: check
	$(LATEXMK) $(LATEXMKOPTS) -pvc $(MAIN).tex

clean:
	$(LATEXMK) -c || true
	rm -f *.bbl *.run.xml

distclean:
	$(LATEXMK) -C || true
	rm -f *.bbl *.run.xml $(MAIN).pdf $(CONDENSED).pdf

arxiv: pdf
	@mkdir -p build/arxiv
	@cp $(MAIN).tex references.bib build/arxiv/
	@cp -r figures build/arxiv/ 2>/dev/null || true
	@cd build && tar -czf arxiv.tar.gz arxiv
	@echo "build/arxiv.tar.gz ready"

check:
	@command -v $(LATEXMK) >/dev/null 2>&1 || { \
	  echo "ERROR: latexmk not found. Install TeX Live or MacTeX."; exit 1; }
	@command -v biber    >/dev/null 2>&1 || { \
	  echo "ERROR: biber not found. Install via your TeX distribution."; exit 1; }
