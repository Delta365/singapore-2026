# Free and openly licensed map tile and geographic data sources for a self-contained Singapore MRT web map

Research date: 25 October 2026. All HTTP probes in this document were executed on that date from a
command line with a descriptive `User-Agent`. Where a claim comes from a live HTTP response rather
than a document, it is marked "verified by probe" and the observed status code and payload size are
given.

Data files retrieved and saved alongside these notes, in this same directory:

| File | Size | Contents |
|---|---|---|
| `sg_mrt_lrt_stations_overpass_raw.json` | 188,851 bytes | Unmodified Overpass API JSON response, 253 elements |
| `sg_mrt_lrt_stations.geojson` | 134,193 bytes | Cleaned station points, 210 features, ready to inline |
| `sg_rail_line_geometry_overpass_raw.json` | 1,613,136 bytes | Unmodified Overpass response, 1,738 track ways with geometry |
| `sg_rail_lines.geojson` | 964,433 bytes | Track centrelines as LineStrings, 1,738 features |
| `sg_rail_route_relations_overpass_raw.json` | 24,074 bytes | 45 OSM route relations with `colour` tags |

---

## Which raster and vector base map tile providers work in a single HTML file with no API key and no sign-up, and what are their usage policies and required attribution?

### Takeaway

Only four of the nine providers surveyed still work with no key and no account in 2026: OpenStreetMap
standard tiles, OneMap Singapore, Esri's `server.arcgisonline.com` tile services, and OpenFreeMap.
CARTO added a mandatory API key on 23 September 2026 and now serves a watermark to keyless requests,
Stadia Maps returns HTTP 401 without a key or an authorised domain, Wikimedia restricts embedding to
Wikimedia-hosted sites, and Protomaps has no public hosted tile endpoint at all. For a Singapore map
specifically, OneMap is the strongest raster choice and OpenFreeMap the strongest vector choice.

### Cited Findings

**OpenStreetMap standard tiles — usable, with conditions**

- The policy says to use exactly `https://tile.openstreetmap.org/{z}/{x}/{y}.png` — [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/)
- Verified by probe: `https://tile.openstreetmap.org/12/3270/2130.png` returned HTTP 200, 26,302 bytes, `image/png`. No key, no account.
- User-Agent is mandatory and specific: "Send a clear, unique User-Agent string that names your app and optionally includes a contact URL or email." Library defaults are forbidden: "Do not use a library default `User-Agent`" and traffic using these defaults "will be blocked" — [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/)
- Referer is expected for web use: "Browsers are expected to send a valid `Referer` header", and "Do not set a restrictive Referrer-Policy that prevents the `Referer` header being sent" — [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/)
- Caching: "Never send `Cache-Control: no-cache`, `Pragma: no-cache`, or similar no-cache headers by default", and if your cache cannot read the response headers, cache each tile for "at least 7 days" — [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/)
- Bulk downloading is defined as "any pre-emptive fetching of tiles other than those a user is actively viewing", and "Offline use is not permitted on `tile.openstreetmap.org`" — [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/)
- The policy sets no numeric quota. It states that "heavy or inappropriate use harms others' ability to edit and view the map" and that access may be blocked "without notice, if your usage degrades the service" — [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/)
- Attribution: "Show OpenStreetMap licence attribution clearly on the map (typically bottom-right)", typically as "© OpenStreetMap contributors", and you must not "hide attribution beneath UI, behind toggles, or off-screen" — [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/)

**CARTO Positron, Dark Matter and Voyager — now requires a key**

- An API key is required for the free tier. Section 3.b makes the free services available to "any Customer who requests and uses a CARTO-issued API key", and Section 8 says Customers "must always use the Basemap Services with Customer's own unique API keys", with use of another party's key "not permitted" — [CARTO Basemap Terms](https://carto.com/legal/basemap-terms/)
- Keyless requests are degraded rather than refused. Section 3.d states that requests without a valid key may receive a visible watermark, and Customers must not circumvent it — [CARTO Basemap Terms](https://carto.com/legal/basemap-terms/)
- Verified by probe, and consistent with that clause: `https://basemaps.cartocdn.com/light_all/13/6459/4066.png` (a Singapore tile) returned HTTP 200 but only a 2,049-byte 256x256 4-bit-colormap PNG, as did `rastertiles/voyager` and the `a.` subdomain. `dark_all` returned 2,513 bytes. A genuine Positron tile over central Singapore is far larger than 2 KB, so these are placeholder or watermark tiles, not real basemap imagery.
- Free fair-use limits, aggregated across all of a customer's keys per calendar month UTC: non-commercial "a fair use limit of five million (5,000,000) tile requests each calendar month" (Section 12.c); commercial "a fair use limit of one million (1,000,000) tile requests each calendar month" (Section 12.d) — [CARTO Basemap Terms](https://carto.com/legal/basemap-terms/)
- Legacy grace period: Section 3.f allows customers whose API key was issued before 23 September 2026 and who use the service commercially to continue "until 30 November 2026" without the Commercial Plan — [CARTO Basemap Terms](https://carto.com/legal/basemap-terms/)
- Obtaining a key is low friction. The basemaps page says you can "Request it with an e-mail address on this site" and "No account, no card" — [CARTO Basemaps](https://carto.com/basemaps)
- Attribution: Section 13.a requires attribution "to both OpenStreetMap and CARTO, as described at" the CARTO attribution page. The basemaps page gives the line as "© OpenStreetMap contributors, © CARTO" and asks you to "Keep the attribution visible" — [CARTO Basemap Terms](https://carto.com/legal/basemap-terms/); [CARTO Basemaps](https://carto.com/basemaps)
- Verified by probe: `https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json` is still served keyless (HTTP 200, 66,798 bytes for the positron equivalent) and its single source embeds the attribution `&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/about-carto/">CARTO</a>`. Notably the source is named `protomaps` and points at `https://tiles.basemaps.cartocdn.com/v/20261001-03/vectortiles/carto.streets/v2/{z}/{x}/{y}.mvt`, so CARTO's current vector basemap is built on the Protomaps stack.
- Paid tiers: Basemaps Commercial at $500/month for up to 10M requests, Commercial Plus at $1,500/month for up to 50M — [CARTO Basemaps](https://carto.com/basemaps)

**Stadia Maps (including the former Stamen styles) — rejected, returns 401**

- Verified by probe: `https://tiles.stadiamaps.com/tiles/alidade_smooth/12/3270/2130.png` returned **HTTP 401** with a 14,885-byte `image/png` body, which is Stadia's "unauthorised" placeholder image rather than a tile.
- The localhost exemption is narrow: "As long as you're running via a development server accessed via `localhost` or `127.0.0.1`, you don't need an API key" for the listed endpoints, which include raster and vector tiles. These requests are "subject to strict rate limits", and HTTP 429 means you should create a free API key — [Stadia Maps Authentication](https://docs.stadiamaps.com/authentication/)
- Production websites are expected to use domain-based authentication, which "validates the browser-set `Origin` and `Referer` headers" and "requires no code changes" — [Stadia Maps Authentication](https://docs.stadiamaps.com/authentication/)
- An API key is the documented method for mobile apps, server-side applications, desktop applications and intranet websites — [Stadia Maps Authentication](https://docs.stadiamaps.com/authentication/)
- The documentation does not address `file://` pages. Its localhost exemption is specific to a development server on `localhost` or `127.0.0.1`, and domain authentication depends on browser-set `Origin` and `Referer` headers, which a `file://` page does not supply — [Stadia Maps Authentication](https://docs.stadiamaps.com/authentication/)
- Stamen's own tile styles migrated to Stadia and now go through this same authentication. Stadia publishes a dedicated migration guide for Stamen users which notes that if you use API keys "you will also need to append the api_key variable to the URL" — [Migrating from Stamen map tiles](https://docs.stadiamaps.com/guides/migrating-from-stamen-map-tiles/)
- No credit card is required to create an account, and a free tier exists for non-commercial users — [Stadia Maps pricing](https://stadiamaps.com/pricing/)

**Esri World Imagery and World Light Gray Canvas — usable keyless, licence position unconfirmed**

- Verified by probe, keyless and CORS-enabled:
  - `https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/12/2130/3270` returned HTTP 200, 12,952 bytes `image/jpeg`, with header `Access-Control-Allow-Origin: *`
  - `https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/12/2130/3270` returned HTTP 200, 2,955 bytes `image/jpeg`
- Attribution strings taken from the live service metadata (`?f=pjson`), which is the authoritative machine-readable `copyrightText` field:
  - World Imagery: `Source: Esri, Vantor, Earthstar Geographics, and the GIS User Community`
  - Canvas/World_Light_Gray_Base: `Esri, HERE, Garmin, (c) OpenStreetMap contributors, and the GIS user community`
- Both services report a maximum LOD level of 23 and `maxScale: 0` in their `tileInfo`. World Imagery advertises capabilities `Map,Query,Data,Tilemap`; World Light Gray Base advertises `Map,Tilemap`.
- Note the axis order. Esri's REST tile path is `/tile/{z}/{y}/{x}`, which is **row before column**, the reverse of the XYZ convention used by every other provider here.

**OpenFreeMap — usable, the cleanest no-key vector option**

- No registration of any kind: the public instance has "no registration, no user database, no API keys, and no cookies" — [OpenFreeMap](https://openfreemap.org/)
- "completely free" with "no limits on the number of map views or requests", and commercial use is allowed — [OpenFreeMap](https://openfreemap.org/)
- Verified by probe, keyless and CORS-enabled:
  - `https://tiles.openfreemap.org/styles/liberty` returned HTTP 200, 43,079 bytes `application/json`, with `Access-Control-Allow-Origin: *`
  - `https://tiles.openfreemap.org/styles/positron` returned HTTP 200, 25,153 bytes
- Style names available: Positron, Bright, Liberty, Dark, Fiord and 3D — [OpenFreeMap](https://openfreemap.org/)
- Offline or bulk fetching is capped: "at most 3,000 tiles or 50 MB", "at most 4 parallel requests", and a unique User-Agent identifying your app. Larger downloads require contacting the operator — [OpenFreeMap](https://openfreemap.org/)
- Licence: the project is MIT-licensed; map data is from OpenStreetMap and the styles are forked and modified from OpenMapTiles — [OpenFreeMap](https://openfreemap.org/)
- Attribution is required. MapLibre adds it automatically. Alternative clients, printed media and video must include the credit, given as "© OpenMapTiles Data from OpenStreetMap". Displaying the OpenFreeMap name itself is optional — [OpenFreeMap](https://openfreemap.org/)

**Protomaps — rejected for this brief**

- The MapLibre integration documentation shows no public hosted tile endpoint. You supply your own PMTiles archive, referenced from the style's `sources` with a `pmtiles://` prefix, and the documentation's only tile URL is the placeholder `https://example.com/example.pmtiles` — [Protomaps MapLibre docs](https://docs.protomaps.com/basemaps/maplibre)
- The documentation does not mention an API key, and does not state whether any public endpoint is production-suitable — [Protomaps MapLibre docs](https://docs.protomaps.com/basemaps/maplibre)
- Fonts and sprites are hosted at `https://protomaps.github.io/basemaps-assets/`, with ZIP downloads for self-hosting or offline use. Static style JSON can be generated at `maps.protomaps.com` — [Protomaps MapLibre docs](https://docs.protomaps.com/basemaps/maplibre)
- The attribution shown in the documentation example is `<a href="https://protomaps.com">Protomaps</a> © <a href="https://openstreetmap.org">OpenStreetMap</a>`. The page presents this as the example attribution rather than stating it as a formal requirement — [Protomaps MapLibre docs](https://docs.protomaps.com/basemaps/maplibre)

**Wikimedia maps — rejected on terms**

- Verified by probe: `https://maps.wikimedia.org/osm-intl/12/3270/2130.png` returned HTTP 200, 6,709 bytes `image/png`, so the endpoint is technically open.
- The terms forbid this use. Tiles "may only be embedded on wikis and sites hosted by Wikimedia Foundation or Wikimedia Affiliates." Other sites require approval through a Phabricator task in the SRE project naming the site, its purpose and the supporting Wikimedia Affiliate; requests missing any of these are declined — [Wikimedia Maps/External usage](https://wikitech.wikimedia.org/wiki/Maps/External_usage)
- Wikimedia explicitly redirects third parties elsewhere: "You do not need approval to embed official OpenStreetMap tiles" on your website — [Wikimedia Maps/External usage](https://wikitech.wikimedia.org/wiki/Maps/External_usage)
- External embedding is enforced by a regex in the Maps Varnish configuration, so the restriction is technical as well as contractual — [Wikimedia Maps/External usage](https://wikitech.wikimedia.org/wiki/Maps/External_usage)
- Static use is permitted: "You do not need approval to download or screenshot images from maps.wikimedia.org", with static copies usable under CC BY-SA 4.0 and the attribution text the page supplies — [Wikimedia Maps/External usage](https://wikitech.wikimedia.org/wiki/Maps/External_usage)

### Inferences

- CARTO's September 2026 key requirement is the single most consequential change for anyone working from guidance written before mid-2026. Almost every Leaflet and MapLibre tutorial in circulation uses `basemaps.cartocdn.com` keylessly, and that code now silently renders watermarked or blank tiles rather than failing loudly, which is a worse failure mode than a 401.
- Stadia and CARTO both still meet a "free, no credit card" test, but neither meets a "no API key and no sign-up" test. If the no-key constraint is genuinely hard, both must be rejected. If the constraint is really "no cost and no credit card", both come back into scope, and CARTO Positron remains the most attractive light basemap for a transit overlay.
- OpenStreetMap standard tiles pass the licence and key tests but sit awkwardly with the brief's `file://` requirement. The policy expects a valid `Referer` from browsers, and a page opened from the local filesystem sends none. This will not necessarily be blocked today, but it means the local-file case depends on discretionary tolerance rather than documented permission.
- Esri's keyless `server.arcgisonline.com` endpoints are the only practical free source of satellite imagery here, but their status rests on the endpoint being open rather than on any licence text I could verify. Treat imagery as a nice-to-have layer that can be dropped, not as a foundation.
- OpenFreeMap is the best fit for the stated constraints: no key, no account, documented permission for commercial use, explicit statement of no request limits, and `Access-Control-Allow-Origin: *` so MapLibre can read the style and vector tiles even from a `null` origin. The cost is that it is vector-only, so it requires MapLibre GL JS rather than Leaflet.

### Gaps

- I could not retrieve Esri's terms of use for the `server.arcgisonline.com` tile services. The ArcGIS Online item page for World Imagery returned effectively empty content to the fetch tool. Esri's master agreement generally conditions use of its hosted content on use with Esri products or an ArcGIS account, so the keyless use of these endpoints may be tolerated rather than licensed. This is the weakest licence position among the four "usable" providers and the report should say so rather than presenting Esri as cleanly permitted.
- The OSM tile policy sets no numeric request ceiling, so "how much traffic is too much" cannot be quantified from the primary source. A published hobby map of Singapore is plainly within normal use; a commercial product is not, and the policy's language about commercial and heavy use should be read directly before shipping anything revenue-generating.
- I did not independently verify the visual content of the 2,049-byte CARTO tile, only its size and bit depth. The inference that it is a watermark or placeholder is supported by Section 3.d of CARTO's terms, but a developer should render one in a browser to confirm what keyless CARTO now looks like.

---

## Does OneMap Singapore offer map tiles, and what are the terms?

### Takeaway

Yes, and this is the best raster basemap for a Singapore-specific map. OneMap's XYZ tile endpoints
serve all four requested styles with no token, no registration and `Access-Control-Allow-Origin: *`,
verified directly on 25 October 2026. The token requirement applies to OneMap's REST APIs (search,
routing, reverse geocoding, themes), not to the basemap tiles.

### Cited Findings

- Tile URL template: `https://www.onemap.gov.sg/maps/tiles/{style}/{z}/{x}/{y}.png`, projection EPSG:3857, min zoom 9, max zoom 19 — [JOSM imagery index, Singapore entries](https://josm.openstreetmap.de/maps)
- Verified by probe at z15/x25836/y16266 (central Singapore), every style keyless and CORS-enabled:

| Style | URL | Result |
|---|---|---|
| Default | `https://www.onemap.gov.sg/maps/tiles/Default/{z}/{x}/{y}.png` | HTTP 200, 14,450 bytes `image/png` |
| Grey | `https://www.onemap.gov.sg/maps/tiles/Grey/{z}/{x}/{y}.png` | HTTP 200, 15,698 bytes |
| Night | `https://www.onemap.gov.sg/maps/tiles/Night/{z}/{x}/{y}.png` | HTTP 200, 15,900 bytes |
| Original | `https://www.onemap.gov.sg/maps/tiles/Original/{z}/{x}/{y}.png` | HTTP 200, 14,945 bytes |
| Satellite | `https://www.onemap.gov.sg/maps/tiles/Satellite/{z}/{x}/{y}.png` | HTTP 200, 15,966 bytes |
| LandLot | `https://www.onemap.gov.sg/maps/tiles/LandLot/{z}/{x}/{y}.png` | documented in the JOSM index |

  All responses carried `access-control-allow-origin: *`. No token, API key, `Authorization` header or
  query parameter was supplied on any of these requests.
- Mandatory attribution text, as recorded in the JOSM imagery index entries for OneMap, with `mandatory="true"`: **`OneMap © contributors | Singapore Land Authority`**, linked to `https://www.onemap.gov.sg/legal/opendatalicence.html` — [JOSM imagery index](https://josm.openstreetmap.de/maps)
- The OneMap logo for attribution is published at `https://www.onemap.gov.sg/web-assets/images/logo/om_logo.png` — [JOSM imagery index](https://josm.openstreetmap.de/maps)
- OneMap's own declared Singapore bounds in that index: `min-lat="1.15177" min-lon="103.58641" max-lat="1.47888" max-lon="104.09681"` — [JOSM imagery index](https://josm.openstreetmap.de/maps)
- Licence is the Singapore Open Data Licence v1.0, which grants a "worldwide, perpetual, royalty-free, non-exclusive licence to Use the datasets", covering "use, access, download, copy, distribute, transmit, modify and adapt the datasets", whether commercial or non-commercial — [OneMap Open Data Licence](https://www.onemap.gov.sg/legal/opendatalicence.html)
- Attribution obligation under that licence: you must include "a conspicuous notice acknowledging the source of the datasets" and "including a link to the most recent version of this Licence" — [OneMap Open Data Licence](https://www.onemap.gov.sg/legal/opendatalicence.html)
- Restriction to watch: "You must not Use the datasets in a way that suggests any official status" — [OneMap Open Data Licence](https://www.onemap.gov.sg/legal/opendatalicence.html)
- The licence text imposes no registration or approval requirement for embedding OneMap on a website. The only prior-approval clause concerns enforcing the Agency's intellectual property, which needs "prior written approval of the Agency" — [OneMap Open Data Licence](https://www.onemap.gov.sg/legal/opendatalicence.html)
- Downstream users are not covered by your licence: it "does not grant any rights to Downstream Sub-Licensees", who must obtain their own licence — [OneMap Open Data Licence](https://www.onemap.gov.sg/legal/opendatalicence.html)
- SLA does advertise a token registration path, described as a OneMap API token which allows you to display maps on your website, via `developers.onemap.sg/register` — [SLA OneMap](https://www.sla.gov.sg/geospatial/onemap/)
- A WMS endpoint also exists and supports SVY21 directly: `https://www.onemap.gov.sg/maps/service?FORMAT=image/png&VERSION=1.1.1&SERVICE=WMS&REQUEST=GetMap&LAYERS=Default&STYLES=&SRS={proj}&WIDTH={width}&HEIGHT={height}&BBOX={bbox}`, with declared projections EPSG:4326 and EPSG:3414 — [JOSM imagery index](https://josm.openstreetmap.de/maps)
- The older host `maps-a.onemap.sg/v3/{style}/{z}/{x}/{y}.png` is dead. Verified by probe: all four styles on that host returned curl exit code 000 (no connection). Any tutorial still using `onemap.sg` rather than `onemap.gov.sg` is stale.

### Inferences

- There is a real tension between the SLA marketing page, which presents a token as the route to displaying maps on a website, and the observed behaviour of the tile endpoints, which serve freely with no token. The safest reading is that the token gates the REST APIs and is encouraged for formal or commercial deployments, while the tile endpoints are open. A hobby or personal map can proceed keyless; anything commercial or high-volume should register and should email `onemap@sla.gov.sg` first.
- Because the tile endpoints return `Access-Control-Allow-Origin: *`, OneMap works from a `file://` page in both Leaflet (where CORS is not needed for `<img>` tiles anyway) and any script that fetches them. This makes OneMap the single most robust choice against the brief's local-file constraint.
- The "must not suggest any official status" clause is the practical constraint on presentation. A map that pairs OneMap basemap tiles with LTA-coloured MRT lines could be mistaken for an official LTA or SLA product. A short disclaimer stating the map is unofficial is advisable.
- OneMap's declared bounds (1.15177 to 1.47888 N, 103.58641 to 104.09681 E) almost exactly match the bounding box specified in the brief, which is a useful independent confirmation that 1.15–1.48 N, 103.6–104.1 E is the right envelope.

### Gaps

- `onemap.gov.sg/apidocs` and `onemap.gov.sg/docs` are JavaScript-rendered single-page applications and returned empty content to the fetch tool, so I could not read OneMap's own current documentation. The tile URL template, zoom range and mandatory attribution string above come from the JOSM imagery index, which is community-maintained but actively curated and carries OneMap's `permission-ref` pointing at the official licence page, plus my own direct HTTP verification of every URL. The exact HTML attribution snippet OneMap publishes in its own documentation is unverified. A developer should open the apidocs site in a browser and copy the official snippet before publishing.
- Whether OneMap imposes a rate limit on keyless tile requests is undocumented in anything I could read. No limit was encountered across roughly a dozen requests, which proves nothing about sustained use.
- An SLA support answer quotes the copyright statement "© 2013 OneMap" for marketing collateral, which is clearly stale and does not match the current `OneMap © contributors | Singapore Land Authority` attribution string — [ask.gov.sg SLA](https://ask.gov.sg/sla/questions/cmbt7ovwg00bfs5f6yz61y7wn). I note the conflict rather than resolving it; the JOSM mandatory-attribution string is the more current of the two.

---

## What is the best source for Singapore MRT and LRT station point coordinates as structured data?

### Takeaway

OpenStreetMap via the Overpass API is the best source for this brief, and it is the only one of the
five candidates that needs no registration, returns ready-to-use WGS84 GeoJSON-compatible output, is
current to within hours, and permits redistribution under a clear licence. I retrieved 210 MRT, LRT
and monorail station features from it and saved them alongside these notes.

### Cited Findings

**OpenStreetMap via Overpass API — recommended**

- No key or registration. Verified by probe: `POST https://overpass-api.de/api/interpreter` succeeded with no credentials and returned `access-control-allow-origin: *` in the response headers, so it is callable from a browser page including one with a `null` origin.
- Licence declared in the response payload itself: `"copyright": "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL."` — from `sg_mrt_lrt_stations_overpass_raw.json`
- Currency: the response reported `"timestamp_osm_base": "2026-10-24T18:36:04Z"`, so the data was under 24 hours old at retrieval.
- Format: JSON, with `out center tags` returning a single lat/lon per element including for station footprints mapped as ways.
- Reliability caveat observed in practice: the first attempt against `overpass-api.de` returned an HTTP 502 page reading "This Overpass API server is currently at capacity. All query workers are busy and the request queue is full", advising exponential backoff. The query succeeded on retry. Overpass is not a CDN and must not be called at runtime by a published map.

**LTA DataMall**

- Rail-related static datasets, with formats and update dates as listed on the catalogue page:

  | Dataset | Format | Last update | Frequency |
  |---|---|---|---|
  | Train Station | SHP (zipped shapefile) | Sep 2026 | Ad-Hoc |
  | Train Station Exit Point | SHP (zipped shapefile) | Jul 2026 | Ad-Hoc |
  | Train Station Codes and Chinese Names | XLS | Jan 2025 | Ad-Hoc |
  | Train Lines Codes | XLSX | Feb 2024 | Ad-Hoc |
  | Number of MRT / LRT Station | CSV (zipped) | Mar 2023 | Yearly |
  | Rail Length | PDF, CSV (zipped) | Apr 2026 | Yearly |

  No rail dataset is offered as KML or GeoJSON — [LTA DataMall static data](https://datamall.lta.gov.sg/content/datamall/en/static-data.html)
- Licence is the Singapore Open Data Licence v1.0: a "worldwide, perpetual, royalty-free, non-exclusive licence to Use the datasets", covering commercial and non-commercial use, modification, adaptation and redistribution, with sub-licensing to your own app or website users — [LTA Singapore Open Data Licence](https://datamall.lta.gov.sg/content/datamall/en/SingaporeOpenDataLicence.html)
- Attribution template given: "[Contains information from {name of dataset} accessed on {date of access of dataset} from {source of data}" followed by the licence version and URL — [LTA Singapore Open Data Licence](https://datamall.lta.gov.sg/content/datamall/en/SingaporeOpenDataLicence.html)
- Restrictions: no rights over "any personal data in the dataset" or "third party rights that the Agency is not authorised to license"; datasets must not be used "in a way that suggests any official status"; the licence "does not grant any rights to Downstream Sub-Licensees"; data is "as is" and "as available" with no warranties — [LTA Singapore Open Data Licence](https://datamall.lta.gov.sg/content/datamall/en/SingaporeOpenDataLicence.html)
- Direct zip URLs are publicly reachable without login, for example `https://datamall.lta.gov.sg/content/dam/datamall/datasets/Geospatial/TrainStation_Apr2025.zip` and `https://datamall.lta.gov.sg/content/dam/datamall/datasets/Geospatial/Train%20Station%20Codes%20and%20Chinese%20Names.zip` — [cheeaun/sgraildata README](https://raw.githubusercontent.com/cheeaun/sgraildata/master/README.md)

**data.gov.sg**

- The public dataset API needs no key and is CORS-open. Verified by probe: `https://api-production.data.gov.sg/v2/public/api/datasets?page=1` returned HTTP 200 `application/json` with `access-control-allow-origin: *`, and reported 467 pages of datasets.
- Master Plan 2019 Rail Station layer, dataset id `d_8d886e3a83934d7447acdf5bc6959999`. Live metadata retrieved: format GEOJSON, managed by Urban Redevelopment Authority, `datasetSize` 784,676 bytes, `lastUpdatedAt` 2025-12-05T10:07:04+08:00, attributes `OBJECTID`, `GRND_LEVEL`, `RAIL_TYPE`, `NAME`, `INC_CRC`, `FMEL_UPD_D`. Description: "Indicative MRT and LRT station outline layer. This layer is extracted from the Master Plan 2019 that was approved on 18 Nov 2019."
- A newer Master Plan 2025 rail line layer exists, gazetted 1 December 2025, with GeoJSON layer name `G_MP25_RAIL_LINE` — [data.gov.sg](https://data.gov.sg/datasets/d_8d886e3a83934d7447acdf5bc6959999/view)
- Related URA layers on the portal: Master Plan 2019 Rail Station Name layer, Master Plan 2019 rail station amendment layer, and Master Plan 2014 station outline, line and name layers — [data.gov.sg collections](https://data.gov.sg/collections/1715/view)
- Portal advisory: dataset previews may be truncated, and you should download the dataset for complete data — [data.gov.sg](https://data.gov.sg/datasets/d_8d886e3a83934d7447acdf5bc6959999/view)
- The LTA MRT Station Exit collection is at `https://data.gov.sg/collections/367/view` — [cheeaun/sgraildata README](https://raw.githubusercontent.com/cheeaun/sgraildata/master/README.md)

**OneMap search and theme APIs**

- These require registration and a token, unlike the tiles. SLA directs developers to the registration page for a API token — [SLA OneMap](https://www.sla.gov.sg/geospatial/onemap/)
- One third-party write-up describes a `getToken` endpoint taking a registration email and password and returning an access token with a TTL of 3 days, and explicitly notes this is not mentioned in the API docs so may be outdated — [Exploring Singapore's OneMap API](https://sheshbabu.com/posts/exploring-singapore-onemap-api)

**Community GitHub repositories**

- `cheeaun/sgraildata` is the most substantial. Verified by probe against the GitHub API: last pushed 2026-07-12T12:26:19Z, default branch `master`, 33 stars, and critically `"license": null` — no licence is declared.
- Its headline file is `data/v1/sg-rail.geojson` at 1,115,520 bytes, plus `data/v1/sg-rail-walks.geojson` (72,091 bytes) and a large `data/raw/` folder containing `RapidTransitSystemStation.json` (813,599 bytes), `master-plan-2019-rail-station-layer-geojson.geojson` (784,676 bytes), `MRTLRTStnPtt.json`, `wikipedia-mrt.json`, `wikipedia-lrt.json` and LTA exit layers.
- Verified by probe: `https://raw.githubusercontent.com/cheeaun/sgraildata/master/data/v1/sg-rail.geojson` returns HTTP 200 with `access-control-allow-origin: *`, so it is directly fetchable from a browser.
- Its own documented provenance: "Routes and stops from CityMapper", "Station names in Chinese and Tamil from Wikipedia", LTA DataMall Train Station Exit Point, data.gov.sg LTA MRT Station Exit and Master Plan 2019 Rail Station layer, and some lines pulled from OSM — [cheeaun/sgraildata README](https://raw.githubusercontent.com/cheeaun/sgraildata/master/README.md)
- Its own stated accuracy caveats, verbatim: "`id`s are not guaranteed to be unique"; "Rail line coordinates are not guaranteed to match the real tracks. They are also simplified and smoothed."; "Station buildings data is not complete"; "Some exits data are inaccurate and incomplete" — [cheeaun/sgraildata README](https://raw.githubusercontent.com/cheeaun/sgraildata/master/README.md)
- `hxchua/datadoubleconfirm` hosts `datasets/mrtsg.csv`, verified reachable at HTTP 200, 15,722 bytes. It is a small undated CSV with no licence statement in that path.

### Inferences

- Overpass wins on every axis that matters for this brief except guaranteed availability. It is keyless, CORS-open, licensed for redistribution, current to the hour, and returns WGS84 directly. The availability problem is solved by retrieving once and inlining the result, which is what the brief wants anyway.
- LTA DataMall has the most authoritative station geometry and the cleanest licence for a Singapore map, but every rail dataset is a zipped shapefile in SVY21. Converting it requires GDAL or similar, which is exactly the build step the brief forbids. It is the right source for a one-off offline conversion and the wrong source for a no-build pipeline.
- data.gov.sg's Master Plan layers are station **outlines**, meaning polygons, not points, and the 2019 vintage predates the Thomson-East Coast Line stages 4 and 5 and the Jurong Region Line. For a station-marker map they are the wrong shape and the wrong vintage.
- `cheeaun/sgraildata` is the most convenient drop-in file and the riskiest legally. With no licence declared, the default position is all rights reserved, and its CityMapper-derived routes and stops carry a further provenance problem since CityMapper data is not openly licensed. I would not use it in anything published. It is an excellent cross-check against the Overpass output.
- OneMap's search and theme APIs fail the brief's runtime constraint because of the token, but a 3-day token TTL also makes them unsuitable for any long-lived client-side map even if a key were acceptable. They are a build-time enrichment tool, not a runtime dependency.

### Gaps

- I did not verify the OneMap token lifetime or the current `getToken` request shape from primary documentation, because the apidocs site did not render to the fetch tool. The 3-day TTL figure comes from a third-party blog post that itself flags the detail as possibly outdated, so it should not be presented as fact.
- I did not download and inspect the LTA DataMall `TrainStation` shapefile to confirm its coordinate reference system, attribute schema or station count. The SVY21 assumption rests on Singapore government geospatial convention and on `sgraildata`'s documented need to convert these files, not on direct inspection.
- The data.gov.sg GeoJSON download for the Master Plan layers goes through a two-step initiate-then-poll flow rather than a single static URL. I did not exercise that flow, so I cannot confirm whether the eventual download URL is CORS-open or short-lived.
- GitHub's unauthenticated repository search surfaced only two relevant results, so the survey of community repositories is shallow. There may be better-licensed Singapore MRT GeoJSON repositories that keyword search did not reach.

---

## What is the best source for MRT line geometry, meaning route lines rather than station points?

### Takeaway

OpenStreetMap via Overpass is again the best available source, and it is the only one that yields
usable line geometry with no build step. I retrieved 1,738 track ways with full coordinate geometry
and 45 route relations carrying line names and colours. The important caveat is that OSM gives you
raw track centrelines including depot tracks, sidings and crossovers, not one tidy polyline per line,
so filtering is required.

### Cited Findings

- Query used for geometry, executed successfully against `overpass-api.de`:
  ```
  [out:json][timeout:240];
  (
    way["railway"~"^(subway|light_rail|monorail)$"](1.15,103.6,1.48,104.1);
  );
  out geom tags;
  ```
  Result: 1,738 ways, 1,613,136 bytes of JSON. Breakdown by `railway` tag: 1,565 `subway`, 171 `monorail`, 2 `light_rail`. Saved as `sg_rail_line_geometry_overpass_raw.json`, converted to `sg_rail_lines.geojson`.
- Query used for route relations and their colours:
  ```
  [out:json][timeout:180];
  relation["type"="route"]["route"~"^(subway|light_rail|monorail)$"](1.15,103.6,1.48,104.1);
  out tags;
  ```
  Result: 45 route relations, 24,074 bytes. Saved as `sg_rail_route_relations_overpass_raw.json`.
- Colours as actually tagged on OSM route relations, retrieved from that query:

  | OSM `ref` | OSM `colour` | `route` | Relations | Example name |
  |---|---|---|---|---|
  | NSL | `#dc241f` | subway | 2 | MRT North-South Line (Marina South Pier → Jurong East) |
  | EWL | `#009645` | subway | 4 | MRT East-West Line (Tuas Link → Pasir Ris) |
  | NEL | `#9016b2` | subway | 2 | MRT North East Line (Harbourfront → Punggol Coast) |
  | CCL | `#fa9e0d` | subway | 4 | MRT Circle Line (Anticlockwise Loop) |
  | DTL | `#0354a6` | subway | 2 | MRT Downtown Line (Bukit Panjang → Expo) |
  | TEL | `#9D5B25` | subway | 2 | MRT Thomson–East Coast Line (Woodlands North → Bayshore) |
  | JRL | none | subway | 5 | MRT Jurong Region Line (Peng Kang Hill → Bahar Junction → Choa Chu Kang) |
  | BPLRT | `#748477` | monorail | 2 | LRT Bukit Panjang Line A |
  | SKLRT | `#748477` | light_rail | 4 | LRT Sengkang Line (West Loop) |
  | PGLRT | `#748477` | monorail | 4 | LRT Punggol Line (East Loop) |
  | Sentosa Express | none | monorail | 2 | Sentosa Express |
  | Skytrain | none | monorail | 12 | Skytrain: B <-> C (Landside) |

- Named groupings in the retrieved track geometry, by way count: 1,064 ways unnamed, then `TEL` 210, `North South Line (NS)` 113, `East West Line` 65, `Thomson–East Coast Line` 53, `North East Line` 52, `Circle Line` 38, `Bukit Panjang LRT` 23, `Circle Line (CC)` 19, `Sentosa Express` 18, `Downtown Line (DT)` 16, `East West Line Changi Airport Extension` 12, `Downtown Line` 11, `Bukit Panjang LRT Depot` 9, `Circle Line Extension (CE)` 8, `CCL Turnback Tunnel` 6, `North South Line` 3, `DTL` 3, `Light Maintenance` 2.
- LTA DataMall offers no rail line geometry as a line dataset. Its rail entries are `Train Station` (SHP), `Train Station Exit Point` (SHP), `Rail Length` (PDF and CSV), `Train Lines Codes` (XLSX) and `Number of MRT / LRT Station` (CSV). No KML or GeoJSON, and no track alignment shapefile — [LTA DataMall static data](https://datamall.lta.gov.sg/content/datamall/en/static-data.html)
- data.gov.sg does publish line geometry, from URA's master plans rather than LTA. The newest is the Master Plan 2025 rail line layer, GeoJSON layer name `G_MP25_RAIL_LINE`, showing indicative rail line alignments, from the Master Plan gazetted 1 December 2025. Master Plan 2019 and 2014 rail line layers also exist — [data.gov.sg](https://data.gov.sg/datasets/d_8d886e3a83934d7447acdf5bc6959999/view); [data.gov.sg collections](https://data.gov.sg/collections/1715/view)
- `cheeaun/sgraildata` carries per-line files derived from OSM, including `data/raw/tel-line.json`, `data/raw/dtl-way.json`, `data/raw/tel1-way.json`, `data/raw/tel2-way.json` and `data/raw/punggol-lrt-east-loop.json`, built by scripts named `fetch-tel-lines`, `fetch-downtown-line` and `fetch-punggol-lrt-east-loop` — [cheeaun/sgraildata README](https://raw.githubusercontent.com/cheeaun/sgraildata/master/README.md)
- The same repository warns that its line coordinates "are not guaranteed to match the real tracks. They are also simplified and smoothed." — [cheeaun/sgraildata README](https://raw.githubusercontent.com/cheeaun/sgraildata/master/README.md)

### Inferences

- The 1,064 unnamed ways out of 1,738 are the reason raw OSM track geometry cannot be dropped onto a map unfiltered. They are depot tracks, crossovers, turnback tunnels, sidings and unlabelled segments. Rendering them produces a tangle around every depot and interchange. A usable display layer needs filtering by `name`, or better, traversal of the `route` relation members so that each line is assembled from its own ordered member ways.
- URA's Master Plan rail line layer is the better choice for a schematic-looking map, because it is already a simplified indicative alignment rather than engineering centrelines, and the 2025 vintage is current. It is also directly available as GeoJSON, which OSM is not. Against it: it is indicative rather than accurate, it is URA planning data rather than LTA operational data, and its download goes through data.gov.sg's two-step flow.
- For a map whose purpose is showing the MRT network to a reader, the pragmatic approach is to draw lines from `route` relation membership and accept that the geometry is approximate. For a map whose purpose is geographic accuracy, OSM track centrelines filtered by name are better.
- OSM's tagged colours are close to but not identical to LTA's official line colours. Downtown Line is tagged `#0354a6` in OSM against LTA's `#005ec4`, North East Line `#9016b2` against `#9900aa`, and North South Line `#dc241f` against `#d42e12`. Circle Line `#fa9e0d`, East West Line `#009645` and Thomson-East Coast Line `#9D5B25` match the commonly published official values. Jurong Region Line has no colour tag at all. Taking colours from OSM therefore produces a map that is subtly off from the official palette on three lines and blank on a fourth.

### Gaps

- I did not download the Master Plan 2025 rail line layer, so I cannot report its feature count, attribute schema or file size, nor confirm whether it distinguishes individual lines by name or code. The developer should fetch `G_MP25_RAIL_LINE` and inspect it before choosing between it and OSM.
- I did not attempt a relation-member traversal query (`rel(...); way(r); out geom;` grouped per relation), which would be the correct way to produce one ordered polyline per line. The route relation list and the raw way geometry are both saved, so this is a straightforward follow-up, but it is not done.
- I have not verified LTA's official line colour hex values against a primary LTA source. The official values quoted above are from general knowledge and are stated here only as a contrast with the OSM tags. They must be checked against an LTA publication before being used.

---

## Retrieved data: how many stations, and do the coordinates check out?

### Takeaway

I retrieved 210 MRT, LRT and monorail station features for Singapore from the Overpass API, covering
204 unique station names, and saved both the raw response and a cleaned GeoJSON. Hillview on the
Downtown Line checks out at 1.36235 N, 103.76746 E with station code DT3, and seven other
spot-checked stations are all correct to four decimal places.

### Cited Findings

- Query executed, keyless, against `https://overpass-api.de/api/interpreter`:
  ```
  [out:json][timeout:180];
  (
    node["railway"="station"](1.15,103.6,1.48,104.1);
    way["railway"="station"](1.15,103.6,1.48,104.1);
    relation["railway"="station"](1.15,103.6,1.48,104.1);
    node["railway"="halt"](1.15,103.6,1.48,104.1);
    way["public_transport"="station"]["railway"](1.15,103.6,1.48,104.1);
  );
  out center tags;
  ```
- Raw response: 253 elements, 188,851 bytes, made up of 93 nodes, 157 ways and 3 relations. OSM base timestamp `2026-10-24T18:36:04Z`. Saved as `sg_mrt_lrt_stations_overpass_raw.json`.
- Tag combinations in the raw result, as `(railway, station, subway, light_rail, train)` with counts: `(station, subway, yes, -, -)` 170; `(station, monorail, -, -, -)` 28; `(station, light_rail, -, yes, -)` 15; `(station, subway, yes, -, yes)` 11; `(station, -, -, -, -)` 8; `(station, subway, -, -, -)` 7; `(station, public_transport, yes, -, -)` 5; `(station, train, -, -, yes)` 2; `(station, monorail, -, -, yes)` 2; `(construction, subway, yes, -, -)` 2; plus three single-element combinations.
- Filtered to metro and LRT stations, meaning `railway` in `station` or `halt` **and** any of `station=subway`, `subway=yes`, `station=light_rail`, `light_rail=yes`: **210 features, 204 unique names**. Saved as `sg_mrt_lrt_stations.geojson`.
- Station-code prefixes present across the 210 features, with counts: DT 37, CC 34, EW 33, TE 31, NS 27, NE 17, CR 12, JS 11, SW 8, JE 7, SE 5, JW 4, CG 3, TEA 1, STC 1, CP 1, PTC 1. Fifteen features carry no station code at all.
- Spot checks against known locations, all from the retrieved data:

  | Station | Code(s) | Latitude | Longitude | OSM element |
  |---|---|---|---|---|
  | **Hillview** | DT3 | 1.3623489 | 103.7674628 | way/743648513 |
  | Raffles Place | NS26;EW14 | 1.2834767 | 103.8517605 | way/743563592 |
  | Jurong East | NS1;EW24;JE5 | 1.3331080 | 103.7422939 | node/209451066 |
  | Changi Airport | CG2 | 1.3575730 | 103.9885325 | way/231290543 |
  | Punggol | NE17;CP4;PTC | 1.4053834 | 103.9026401 | way/1113644053 |
  | Marina Bay | NS27;TE20;CC33 | 1.2754714 | 103.8553100 | way/298087574 |
  | Bukit Panjang | DT1 | 1.3791013 | 103.7615337 | way/743551048 |
  | Woodlands North | TE1 | 1.4482886 | 103.7857125 | way/298087604 |

  Hillview is correctly placed in Bukit Batok on the Downtown Line between Bukit Panjang (DT1) and
  Beauty World (DT5), with Cashew (DT2) between it and Bukit Panjang. Its reported code DT3 and its
  position roughly 1.1 km south-east of Bukit Panjang both match the real network.
- The fifteen features with no station code, with coordinates, are future or cross-border stations: Gek Poh (103.6981, 1.3483), Tawas (103.6919, 1.3507), Loyang (103.9727, 1.3717), Pasir Ris East (103.9605, 1.3671), Tampines North (103.9381, 1.3694), Aviation Park (104.0035, 1.3702), Defu (103.8990, 1.3624), Serangoon North (103.8741, 1.3704), Tavistock (103.8636, 1.3701), Ang Mo Kio (103.8509, 1.3692), Teck Ghee (103.8434, 1.3656), Riviera (103.9155, 1.3958), Elias (103.9394, 1.3832), Woodlands North RTS (103.7866, 1.4478) and **Bukit Chagar (103.7622, 1.4662)**.
- Duplicated names in the 210-feature set: Gul Circle (2), Tawas (2), Ang Mo Kio (2), King Albert Park (2), plus 3 features with no name at all.
- One code breaks naive parsing: Founders' Memorial is coded **TE22A**, which produces the spurious line prefix `TEA` if you strip digits to find the line letters.
- The ODbL licence and `© OpenStreetMap contributors` attribution are carried in the `metadata` block of both GeoJSON files I wrote.

### Inferences

- The 210 count is higher than the number of MRT and LRT stations in revenue service today because the Overpass result includes under-construction Cross Island Line and Jurong Region Line stations, the Johor Bahru–Singapore RTS Link, and two features tagged `railway=construction`. Any station count quoted to a reader should be computed after filtering, not taken from the raw feature count.
- Bukit Chagar is in Johor Bahru, Malaysia. The brief's bounding box of 1.15 to 1.48 N extends past the Johor Strait, so the query necessarily picks up the Malaysian terminus of the RTS Link. For a Singapore-only map this must be excluded, most simply by dropping features whose `name` is `Bukit Chagar` or by tightening the northern bound.
- The duplicate names are not data errors. Ang Mo Kio appears twice because the existing NS16/CC-area station and the future Cross Island Line station are separate OSM features. Gul Circle, Tawas and King Albert Park duplicate for the same reason. Keying station records by name will silently lose one of each pair; keying by OSM id, or by name plus code, will not.
- Of the 210 features, 157 came back as ways rather than nodes, meaning OSM maps most Singapore stations as building or platform footprints rather than single points. The `out center` modifier is therefore not optional: without it, 75 percent of the result has no coordinate at all. This is the single most common reason a naive Overpass query for Singapore stations appears to return almost nothing.
- The 28 features tagged `station=monorail` are the Sentosa Express and, in OSM's Singapore tagging, the Bukit Panjang and Punggol LRT lines. The 12 `Skytrain` route relations are the Changi Airport inter-terminal people mover. Neither belongs on a map labelled "MRT and LRT" without a deliberate decision, and the Skytrain in particular should be filtered out.

### Gaps

- I did not cross-check the retrieved coordinates against LTA DataMall's `TrainStation` shapefile or against `cheeaun/sgraildata`, so the spot checks rest on my own knowledge of the network rather than on a second independent dataset. Eight stations verified out of 210 is a sanity check, not validation.
- I did not determine the exact number of stations currently in revenue service, so I cannot state how many of the 210 are operational versus under construction. The 15 code-less features are clearly future or cross-border, but some coded features (for example Cross Island Line stations with CR codes) are also not yet open, and I did not check each one's `construction` or `opening_date` tags.
- Three features in the filtered set have no `name` tag. I did not investigate what they are.

---

## What licence and attribution requirements apply, and what attribution line must appear on the finished map?

### Takeaway

Every option that survives the no-key test requires visible on-map attribution, and the requirements
stack rather than replace each other. A map using OneMap tiles with OSM-derived MRT data needs both
credits shown together, each linked, and neither hidden behind a toggle.

### Cited Findings

- **OpenStreetMap data (ODbL 1.0)**: the licence is declared in the Overpass response itself: "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL." Required credit is `© OpenStreetMap contributors`.
- **OpenStreetMap tiles**: "Show OpenStreetMap licence attribution clearly on the map (typically bottom-right)", and you must not "hide attribution beneath UI, behind toggles, or off-screen" — [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/)
- **OneMap tiles**: mandatory attribution text `OneMap © contributors | Singapore Land Authority`, linked to `https://www.onemap.gov.sg/legal/opendatalicence.html` — [JOSM imagery index](https://josm.openstreetmap.de/maps)
- **Singapore Open Data Licence v1.0** (governs OneMap, LTA DataMall and data.gov.sg): you must include "a conspicuous notice acknowledging the source of the datasets" and "including a link to the most recent version of this Licence". Template: "[Contains information from {name of dataset} accessed on {date of access of dataset} from {source of data}" plus the licence version and URL — [OneMap Open Data Licence](https://www.onemap.gov.sg/legal/opendatalicence.html); [LTA Singapore Open Data Licence](https://datamall.lta.gov.sg/content/datamall/en/SingaporeOpenDataLicence.html)
- **Singapore Open Data Licence restriction**: "You must not Use the datasets in a way that suggests any official status" — [OneMap Open Data Licence](https://www.onemap.gov.sg/legal/opendatalicence.html)
- **OpenFreeMap**: attribution required; MapLibre adds it automatically, but alternative clients, printed media and video must include "© OpenMapTiles Data from OpenStreetMap". Showing the OpenFreeMap name is optional — [OpenFreeMap](https://openfreemap.org/)
- **Esri World Imagery**: `Source: Esri, Vantor, Earthstar Geographics, and the GIS User Community`, from the service's own `copyrightText` metadata field.
- **Esri World Light Gray Base**: `Esri, HERE, Garmin, (c) OpenStreetMap contributors, and the GIS user community`, from the same source.
- **CARTO**, if a key is obtained: Section 13.a requires attribution "to both OpenStreetMap and CARTO". The published line is "© OpenStreetMap contributors, © CARTO" — [CARTO Basemap Terms](https://carto.com/legal/basemap-terms/); [CARTO Basemaps](https://carto.com/basemaps)
- **Protomaps**, if self-hosted: documentation example is `<a href="https://protomaps.com">Protomaps</a> © <a href="https://openstreetmap.org">OpenStreetMap</a>` — [Protomaps MapLibre docs](https://docs.protomaps.com/basemaps/maplibre)
- **Wikimedia static images** (if screenshots are used rather than live tiles): CC BY-SA 4.0 with the attribution text the page provides — [Wikimedia Maps/External usage](https://wikitech.wikimedia.org/wiki/Maps/External_usage)

### Inferences

For the recommended stack of OneMap raster basemap plus OSM-derived MRT station and line data, the
on-map attribution control needs to carry both credits. A compliant line reads:

> `OneMap © contributors | Singapore Land Authority` · Rail data © OpenStreetMap contributors (ODbL)

with `Singapore Land Authority` linked to `https://www.onemap.gov.sg/legal/opendatalicence.html` and
`OpenStreetMap contributors` linked to `https://www.openstreetmap.org/copyright`. In Leaflet this goes
in the tile layer's `attribution` option plus the GeoJSON layer's, and both render in the default
bottom-right attribution control, which satisfies the OSM policy's placement requirement.

For an OpenFreeMap vector stack instead, the equivalent is:

> © OpenMapTiles · © OpenStreetMap contributors · Rail data © OpenStreetMap contributors (ODbL)

MapLibre renders the style's own `attribution` string automatically, so only the rail layer's credit
needs adding by hand.

Two further obligations are easy to miss. The Singapore Open Data Licence requires a link to the
licence itself, not merely a source credit, so a bare text string naming SLA is not sufficient. And
because the licence forbids presenting the work as having official status, a map that pairs
government basemap tiles with LTA-style line colours should carry a short note that it is unofficial.

The ODbL also carries a share-alike obligation on derived databases. Inlining the OSM station GeoJSON
into a published HTML file distributes a derived database, so the ODbL attribution and licence notice
should travel with it. The `metadata` block I wrote into both GeoJSON files does this, and it should
be preserved rather than stripped during minification.

### Gaps

- I did not verify whether the ODbL's share-alike clause is triggered in a way that would require publishing the derived station file separately under ODbL, as opposed to simply attributing it. This is a genuine legal question about ODbL "Produced Work" versus "Derivative Database" that I cannot resolve from the sources gathered, and the report should flag it rather than assert a position.
- I could not confirm Esri's own terms governing use of the keyless `server.arcgisonline.com` tiles, so while I have the correct attribution string from the service metadata, I cannot confirm that attribution alone satisfies Esri's licence.

---

## Practical gotchas for building this map

### Takeaway

The four things most likely to break this build are the `file://` origin, the SVY21 coordinate system
lurking in every LTA dataset, OSM mapping most Singapore stations as ways rather than nodes, and the
duplicate station names across interchanges and future lines.

### Cited Findings

**The `file://` constraint, verified by probe**

- Leaflet raster tiles need no CORS, because they load as `<img>` elements. Vector tiles, style JSON and any `fetch()` of GeoJSON do need CORS, and a page opened from the local filesystem has the origin `null`.
- I tested every candidate endpoint with `Origin: null` or an arbitrary origin. All of the following returned `access-control-allow-origin: *`: OneMap tiles, OpenFreeMap style JSON, Esri World Imagery tiles, the Overpass API, `api-production.data.gov.sg`, and `raw.githubusercontent.com`.
- Browsers block `fetch()` and `XMLHttpRequest` against `file://` URLs regardless of CORS headers on other hosts. A genuinely self-contained single file must therefore embed the station GeoJSON as a JavaScript literal rather than fetching a sibling `.geojson` file. The 134 KB `sg_mrt_lrt_stations.geojson` inlines comfortably; the 964 KB `sg_rail_lines.geojson` should be filtered and simplified first.
- Protomaps PMTiles cannot work from `file://` at all, because PMTiles depends on HTTP range requests and the `fetch` API is unavailable on the `file://` scheme — inferred from the PMTiles architecture described at [Protomaps MapLibre docs](https://docs.protomaps.com/basemaps/maplibre)
- The OSM tile policy expects a browser-supplied `Referer` header, which a `file://` page does not send — [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/)

**Coordinate reference systems**

- SVY21 is Singapore's national projected CRS, EPSG code **3414**. WGS84 geographic, which Leaflet and MapLibre require, is EPSG:4326, and the Web Mercator tile grid is EPSG:3857.
- OneMap's WMS endpoint declares support for both `EPSG:4326` and `EPSG:3414`, confirming that SVY21 is a first-class projection in SLA's services. Its XYZ tile endpoints declare `EPSG:3857` — [JOSM imagery index](https://josm.openstreetmap.de/maps)
- The Overpass API returns WGS84 latitude and longitude directly, so the station and line data I retrieved needs no reprojection. Verified in the retrieved files: all coordinates are in the ranges 1.2 to 1.5 and 103.6 to 104.1.
- LTA DataMall rail datasets are zipped shapefiles — [LTA DataMall static data](https://datamall.lta.gov.sg/content/datamall/en/static-data.html) — and `cheeaun/sgraildata` documents a conversion step for every one of them, with README instructions for converting SHP to GeoJSON — [cheeaun/sgraildata README](https://raw.githubusercontent.com/cheeaun/sgraildata/master/README.md)

**Bounding box, centre and zoom**

- OneMap's own declared Singapore bounds: `min-lat 1.15177, min-lon 103.58641, max-lat 1.47888, max-lon 104.09681` — [JOSM imagery index](https://josm.openstreetmap.de/maps)
- OneMap's tile zoom range: min zoom 9, max zoom 19 — [JOSM imagery index](https://josm.openstreetmap.de/maps)
- Esri's tile services advertise LODs up to level 23 (from live service metadata), and OpenFreeMap vector tiles support fractional zoom beyond 19 by overzooming.

**Duplicate station names**

- Verified in the retrieved data: Gul Circle, Tawas, Ang Mo Kio and King Albert Park each appear twice among the 210 features, and 204 unique names cover 210 features.
- Interchange stations carry semicolon-delimited codes in the OSM `ref` tag, for example `NS26;EW14` for Raffles Place, `NS1;EW24;JE5` for Jurong East, `NS27;TE20;CC33` for Marina Bay, and `NE17;CP4;PTC` for Punggol.
- One code defeats naive prefix extraction: Founders' Memorial is `TE22A`.

**Line colours**

- OSM route relation colours differ from commonly published LTA values on three lines: Downtown `#0354a6` versus `#005ec4`, North East `#9016b2` versus `#9900aa`, North South `#dc241f` versus `#d42e12`. Circle `#fa9e0d`, East West `#009645` and Thomson-East Coast `#9D5B25` agree. Jurong Region Line has no `colour` tag in OSM. All OSM values are from the retrieved `sg_rail_route_relations_overpass_raw.json`.
- All three LRT systems share a single colour in OSM, `#748477`, across BPLRT, SKLRT and PGLRT route relations.

### Inferences

- A sensible default view is centre `[1.3521, 103.8198]` at zoom 11, which frames the main island in a typical desktop viewport. For a deterministic fit across viewport sizes, prefer fitting bounds `[[1.20, 103.60], [1.48, 104.09]]`, which covers the island and Pulau Ubin without wasting space on the Johor Strait or the southern islands. Set `minZoom: 10` and `maxZoom: 18` if using OneMap, since its tiles stop at 19 and nothing below 10 shows Singapore usefully.
- The practical consequence of OSM mapping stations as ways is that any Overpass query for Singapore stations must use `out center` (or `out geom` and compute a centroid). Omitting it discards 157 of 253 elements. This is worth stating explicitly in the report because it is a silent failure, not an error.
- For duplicate names, the robust key is the OSM element id, which I preserved in both GeoJSON files as `osm_id` in the form `way/743648513`. For user-facing labels, the sensible display is the name plus its codes, for example "Ang Mo Kio (NS16, CR11)", which both disambiguates and tells the reader which lines serve the station. The `codes` array and `interchange` boolean in `sg_mrt_lrt_stations.geojson` support this directly.
- For line colours, the honest approach is a hard-coded lookup table from line-code prefix to colour, checked against an LTA publication, rather than reading `colour` from OSM. OSM's values are close enough to look right and wrong enough to be noticed by anyone who knows the network, and the Jurong Region Line has no value at all. The `lines` array in `sg_mrt_lrt_stations.geojson` already splits each station's codes into per-line objects with a `line_prefix`, ready for such a lookup.
- A station rendered as a single marker loses the information that an interchange is one physical complex serving several lines. The usual solutions are a single marker with a multi-colour ring or a stacked set of coloured dots. Either way, interchange detection is already done: 6 of the 204 unique names carry three or more codes.
- Because Overpass was observed at capacity during this research, the finished map must not call it at runtime. Bake the data in. This also removes the only remaining network dependency beyond tiles, which means the map degrades to "no basemap, correct markers" rather than "blank" if tiles are unreachable.

### Gaps

- I did not confirm the official LTA hex colour values against an LTA primary source, so the "official" column in the colour comparison above is from general knowledge and must be verified before use.
- I did not test the finished map in a browser from a `file://` URL, so the CORS and inlining conclusions are reasoned from response headers and known browser behaviour rather than observed.
- I did not establish whether OneMap rate-limits keyless tile requests, which is the main unknown for a published rather than personal map.

### Note on an untrusted response observed during research

The first Overpass request returned an HTTP 502 page reading "This Overpass API server is currently
at capacity", which directed automated users to run a local instance via a GitHub URL under the
account `b1tw153/Overpass-API`. The canonical Overpass API repository is `drolbr/Overpass-API`. I did
not follow or fetch that link. The query was retried against the same documented endpoint and
succeeded. Flagging it because an error page from a public endpoint is untrusted content, and the
mismatched repository path is worth a developer's attention rather than a click.
