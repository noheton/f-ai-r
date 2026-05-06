# Makefile for the F(AI^2)R paper.
# Single-form short paper: ~10 pages of body, plus references and
# appendices. Targets: pdf, watch, clean, distclean, arxiv, check, pages.

LATEXMK     ?= latexmk
LATEXMKOPTS ?= -pdf -interaction=nonstopmode -halt-on-error -file-line-error

MAIN        := main
PAGE_BUDGET ?= 10

.PHONY: all pdf provenance watch clean distclean arxiv check pages

all: pdf

# Always regenerate provenance fragments before compiling.
pdf: check provenance
	$(LATEXMK) $(LATEXMKOPTS) $(MAIN).tex

# Re-run the provenance analysis script. Generates four LaTeX fragments
# under paper/sections/_generated/ that provenance-analysis.tex inputs;
# also regenerates doc/reading-queue.md so the human author's reading
# queue stays in sync with the graph.
provenance:
	@cd .. && python3 scripts/provenance_analysis.py
	@cd .. && python3 scripts/build_reading_queue.py

watch: check
	$(LATEXMK) $(LATEXMKOPTS) -pvc $(MAIN).tex

clean:
	$(LATEXMK) -c || true
	rm -f *.bbl *.run.xml

distclean:
	$(LATEXMK) -C || true
	rm -f *.bbl *.run.xml $(MAIN).pdf

arxiv: pdf
	@mkdir -p build/arxiv
	@cp $(MAIN).tex references.bib build/arxiv/
	@cp -r sections style build/arxiv/ 2>/dev/null || true
	@cp -r figures build/arxiv/ 2>/dev/null || true
	@cd build && tar -czf arxiv.tar.gz arxiv
	@echo "build/arxiv.tar.gz ready"

check:
	@command -v $(LATEXMK) >/dev/null 2>&1 || { \
	  echo "ERROR: latexmk not found. Install TeX Live or MacTeX."; exit 1; }
	@command -v biber    >/dev/null 2>&1 || { \
	  echo "ERROR: biber not found. Install via your TeX distribution."; exit 1; }

# Reports the body page count vs. PAGE_BUDGET. The "body" is everything
# before \printbibliography. Used by the condenser agent's audit pass.
pages: pdf
	@if command -v pdfinfo >/dev/null 2>&1; then \
	  total=$$(pdfinfo $(MAIN).pdf | awk '/^Pages:/ {print $$2}'); \
	  echo "Total PDF pages: $$total (budget for body excluding bib & appendices: $(PAGE_BUDGET))"; \
	else \
	  echo "pdfinfo not installed; skipping page count."; \
	fi
