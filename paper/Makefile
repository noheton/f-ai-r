# Makefile for the F(AI^2)R paper.
# Single-form short paper: ~10 pages of body, plus references and
# appendices. Targets: pdf, watch, clean, distclean, arxiv, check, pages.

LATEXMK     ?= latexmk
LATEXMKOPTS ?= -pdf -interaction=nonstopmode -halt-on-error -file-line-error

MAIN        := main
PAGE_BUDGET ?= 10

.PHONY: all pdf watch clean distclean arxiv check pages

all: pdf

pdf: check
	$(LATEXMK) $(LATEXMKOPTS) $(MAIN).tex

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
