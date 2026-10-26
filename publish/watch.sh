#!/usr/bin/env bash
# Run publish.sh whenever the trip folder changes. It waits until edits have
# settled, and leaves a gap between publishes so a busy editing session does
# not use up the daily Vercel deployment allowance. Stop it with Ctrl-C.
#
#   publish/watch.sh
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
POLL=20       # seconds between checks
SETTLE=60     # seconds without changes before publishing
MIN_GAP=300   # minimum seconds between publishes

fingerprint() {
  (cd "$ROOT" && find . \( -path ./.git -o -path ./build/osm \) -prune -o -type f -print0 \
    | xargs -0 stat -f '%m %z %N' | shasum | cut -d' ' -f1)
}

log() { echo "$(date '+%H:%M:%S') $*"; }

# Start unpublished so that edits made before the watcher started go out too.
published=""
seen="$(fingerprint)"
last_change=$(date +%s)
last_publish=0
log "watching $ROOT"

while true; do
  sleep "$POLL"
  now=$(date +%s)
  current="$(fingerprint)"
  if [[ "$current" != "$seen" ]]; then
    seen="$current"
    last_change=$now
    continue
  fi
  if [[ "$current" != "$published" ]] && (( now - last_change >= SETTLE && now - last_publish >= MIN_GAP )); then
    log "publishing"
    if "$ROOT/publish.sh"; then
      log "done"
    else
      log "publish failed; it will run again after the next change"
    fi
    # A failed publish of the same files would fail again, so wait for a change.
    published="$current"
    last_publish=$now
  fi
done
