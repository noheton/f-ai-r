#!/bin/bash
# SessionStart hook for the F(AI)²R repository.
#
# Guarantees the Python toolchain the repo's generator scripts and
# invariant checks depend on is installed before the session starts:
#   - scripts/build_reading_queue.py      (rdflib + markdown)
#   - scripts/provenance_analysis.py      (rdflib; also validates that
#                                          doc/provenance.ttl parses)
#   - scripts/build_provenance_site.py    (markdown)
#   - paper/figures/src/*.py              (matplotlib; figure renders)
#
# LaTeX (latexmk + biber) is treated as best-effort: CI builds the PDF
# via a Docker action, and a full TeX Live apt install is gigabytes, so
# the hook reports its absence rather than failing the session on it.
#
# Synchronous, idempotent, non-interactive. Web-only.
set -euo pipefail

# Only run in the Claude Code web/remote environment.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

ROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$ROOT"

echo "[session-start] Installing Python dependencies (scripts/requirements.txt + matplotlib)"
python3 -m pip install --quiet --disable-pip-version-check \
  -r scripts/requirements.txt matplotlib

echo "[session-start] Python deps ready:"
python3 - <<'PY'
import importlib, sys
for mod in ("rdflib", "markdown", "matplotlib"):
    try:
        m = importlib.import_module(mod)
        print(f"  - {mod} {getattr(m, '__version__', '(version n/a)')}")
    except Exception as exc:  # pragma: no cover - diagnostic only
        print(f"  - {mod} MISSING: {exc}", file=sys.stderr)
        sys.exit(1)
PY

# LaTeX toolchain: report only; do not fail the session.
if command -v latexmk >/dev/null 2>&1 && command -v biber >/dev/null 2>&1; then
  echo "[session-start] LaTeX toolchain present (latexmk + biber): 'make -C paper pdf' available"
else
  echo "[session-start] NOTE: latexmk/biber not found; the LaTeX build is unavailable" \
       "in this environment (CI builds the PDF via a Docker action). Python-side" \
       "checks (provenance parse, reading queue, site, figures) are unaffected."
fi

echo "[session-start] Done."
