#!/bin/sh
# Re-fetch the OpenStreetMap layers behind basemap.json into build/osm/, then run: python3 -I basemap.py
cd "$(dirname "$0")" && mkdir -p osm && cd osm
BB="1.15,103.59,1.48,104.10"
q(){ curl -s -m 280 -A "Singapore2026TripMap/1.0" -X POST https://overpass-api.de/api/interpreter --data-urlencode "data=$2" -o "$1"; echo "$1 $(wc -c < "$1")"; }
q coast.json "[out:json][timeout:240];way[\"natural\"=\"coastline\"]($BB);out geom;"
q roads.json "[out:json][timeout:240];way[\"highway\"~\"^(motorway|trunk|primary|secondary)\$\"]($BB);out geom;"
q places.json "[out:json][timeout:120];node[\"place\"~\"^(suburb|quarter|town|neighbourhood)\$\"]($BB);out;"
q green.json "[out:json][timeout:240];(way[\"leisure\"~\"^(nature_reserve|park|golf_course)\$\"]($BB);relation[\"leisure\"~\"^(nature_reserve|park)\$\"]($BB);way[\"landuse\"=\"forest\"]($BB);relation[\"landuse\"=\"forest\"]($BB);way[\"natural\"=\"wood\"]($BB);relation[\"natural\"=\"wood\"]($BB);way[\"boundary\"=\"national_park\"]($BB);relation[\"boundary\"=\"national_park\"]($BB););out geom;"
q water.json "[out:json][timeout:240];(way[\"natural\"=\"water\"]($BB);relation[\"natural\"=\"water\"]($BB);way[\"landuse\"=\"reservoir\"]($BB););out geom;"
