#!/usr/bin/env bash
# Start a long-lived stealth Chromium with a CDP endpoint other tools connect to.
# Default port 9222. Logs to /tmp/cloakserve.log, PID written to /tmp/cloakserve.pid.
#
# Usage:
#   serve.sh [--port 9222] [--humanize] [--proxy URL] [--geoip] [--user-data-dir DIR] [--url URL]
#
# Stop:
#   kill "$(cat /tmp/cloakserve.pid)"
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)

if command -v cloakbrowser-python >/dev/null 2>&1; then
  PY=$(command -v cloakbrowser-python)
elif [ -x /usr/local/bin/cloakbrowser-python ]; then
  PY=/usr/local/bin/cloakbrowser-python
elif command -v uv >/dev/null 2>&1 && [ -x "$(uv tool dir)/cloakbrowser/bin/python" ]; then
  PY="$(uv tool dir)/cloakbrowser/bin/python"
else
  echo "Could not find CloakBrowser Python. Try: uv tool install cloakbrowser" >&2
  exit 1
fi

nohup "$PY" "$HERE/serve.py" "$@" </dev/null > /tmp/cloakserve.log 2>&1 &
PID=$!
echo "$PID" > /tmp/cloakserve.pid
echo "started pid=$PID  log=/tmp/cloakserve.log"
