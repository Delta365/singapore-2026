# Singapore 2026

Planning files for an eight-day trip to Singapore, 2 to 9 November 2026, based near Hillview MRT on the Downtown Line.

The main output is `singapore-2026-map.html`, an interactive day-by-day itinerary map. It is a single self-contained page: Leaflet and Google Fonts load from CDNs, and all trip data is inlined. A public copy is at <https://sanjivanrane.com/singapore2026>.

## Contents

| Path | What it holds |
| --- | --- |
| `singapore-2026-map.html` | The map. Open it in a browser with an internet connection. |
| `build/` | The generator: `build.py`, the `tpl.html` template and the JSON data it inlines. |
| `itinerary-current.json` | The current day-by-day plan. |
| `places-raw-list.md` | The original wish list of food, sites and activities. |
| `research_notes/` | Research on food, transport, events, weather, budget, entry rules and map data. |
| `TRAVEL/Singapore/` | The written travel guide and its sources. |
| `publish.sh`, `publish/` | Publishing to sanjivanrane.com. |

## Rebuild the map

```bash
cd build && python3 -I build.py
```

## Publish to the website

```bash
./publish.sh
```

The script commits and pushes everything in this folder. It then writes a public copy of the map to `singapore2026/index.html` in the Design-Portfolio repo, pushes that repo so Vercel deploys it, and waits until the live page matches. Pass `--no-wait` to skip the wait. Set `SITE_REPO` if the Design-Portfolio checkout is not at `~/Desktop/claude/Design-Portfolio`.

To publish automatically while editing, run `publish/watch.sh`. It runs `publish.sh` once the folder has had no changes for 60 seconds, at most once every 5 minutes, until you stop it with Ctrl-C.

The public copy drops the Flights line in the header and every sentence that mentions a flight number or a flight time, and it adds a noindex tag. If a flight detail survives, `publish/redact.py` stops before anything reaches the website and prints where it found it. The flight times it checks are read from `publish/flight_times.local`, one per line. That file is git-ignored and exists only on the machine that publishes, so create it there and update it if the flights change.

## Privacy

This repository is public, so flight numbers and times are kept out of every file in it, and the publish step checks the website copy again before it goes out. PDFs are ignored by `.gitignore` so that tickets and booking confirmations are not committed by accident.
