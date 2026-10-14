#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
[ -d .venv ] || python3 -m venv .venv
.venv/bin/pip install -q -r requirements.txt

set +e
out=$(.venv/bin/python -m pytest -q 2>&1); code=$?
set -e
echo "$out"

passed=$(echo "$out" | grep -oE '[0-9]+ passed' | grep -oE '[0-9]+' || echo 0)
failed=$(echo "$out" | grep -oE '[0-9]+ failed' | grep -oE '[0-9]+' || echo 0)
echo "TESTS: ${passed}/$((passed + failed))"
exit $code