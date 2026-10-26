#!/usr/bin/env bash
# Commit and push this repo, then publish the public copy of the map (flight
# details removed, noindex added) through the Design-Portfolio repo, which
# Vercel deploys to https://sanjivanrane.com/singapore2026.
#
#   ./publish.sh            commit, push, publish, then wait for the live page
#   ./publish.sh --no-wait  the same without waiting for Vercel
#
# SITE_REPO overrides the location of the Design-Portfolio checkout.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
SITE="${SITE_REPO:-$HOME/Desktop/claude/Design-Portfolio}"
URL="https://sanjivanrane.com/singapore2026"
WAIT=1
[[ "${1:-}" == "--no-wait" ]] && WAIT=0

stamp="$(date '+%Y-%m-%d %H:%M')"
trailer=()
# Commits made from a Claude Code session carry the co-author line.
if [[ -n "${CLAUDECODE:-}" ]]; then
  trailer=(-m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")
fi

echo "1/3 Trip repo"
cd "$ROOT"
git add -A
if git diff --cached --quiet; then
  echo "    no changes to commit"
else
  git commit -q -m "Sync trip files ($stamp)" ${trailer[@]+"${trailer[@]}"}
fi
git push -q origin main

echo "2/3 Website"
git -C "$SITE" pull -q --ff-only
mkdir -p "$SITE/singapore2026"
python3 -I "$ROOT/publish/redact.py" "$ROOT/singapore-2026-map.html" "$SITE/singapore2026/index.html"
git -C "$SITE" add singapore2026
if git -C "$SITE" diff --cached --quiet -- singapore2026; then
  echo "    page unchanged"
else
  git -C "$SITE" commit -q -m "Update Singapore 2026 trip map ($stamp)" ${trailer[@]+"${trailer[@]}"} -- singapore2026
fi
git -C "$SITE" push -q origin main

echo "3/3 Live page"
if (( ! WAIT )); then
  echo "    skipped; Vercel usually deploys within a minute"
  exit 0
fi
want="$(shasum -a 256 < "$SITE/singapore2026/index.html" | cut -d' ' -f1)"
for _ in $(seq 1 30); do
  got="$( (curl -fsSL "$URL?check=$(date +%s)" || true) | shasum -a 256 | cut -d' ' -f1)"
  if [[ "$got" == "$want" ]]; then
    echo "    live at $URL"
    exit 0
  fi
  sleep 10
done
echo "    the live page still differs after 5 minutes; check the Vercel dashboard" >&2
exit 1
