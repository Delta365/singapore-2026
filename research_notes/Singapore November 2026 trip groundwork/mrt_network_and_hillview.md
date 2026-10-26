# Singapore MRT/LRT network in late 2026, with focus on Hillview station (DT3)

Research date: 24-25 October 2026. Target travel window: 2-9 November 2026.

Important framing note for the report writer: LTA does not publish an open hex-code
palette for its line colours, and LTA's own newsroom had not, as of late October 2026,
announced a firm opening date for Thomson-East Coast Line Stage 5 or the Downtown Line 3
extension. Both points are flagged in detail below. Journey times in this document are
explicitly marked as either sourced or computed, and the computation method is stated so
the writer can reproduce or discard it.

## Q1. All MRT and LRT lines operating in Singapore as of late 2026: names, codes, colours, termini, station counts

### Takeaway

Eight rail lines carry passengers in November 2026: six MRT lines (NSL, EWL including the
Changi Airport branch, NEL, CCL, DTL, TEL) and three LRT systems (Bukit Panjang, Sengkang,
Punggol), all grey on the map. The one structural change during 2026 is that the Circle
Line became a closed loop on 12 July 2026. The Jurong Region Line and Cross Island Line
are not open and will not be open during the trip.

### Cited Findings

Lines and station counts:

- North South Line (NSL), red, Jurong East to Marina Bay/Marina South Pier, 27 stations — [Singapore MRT Line Colours 2026](https://singaporemrtmaps.com/blog/singapore-mrt-line-colours/)
- East West Line (EWL, codes EW plus the CG Changi Airport branch), green, Pasir Ris to Tuas Link with the Changi Airport branch running from Tanah Merah, 35 stations — [Singapore MRT Line Colours 2026](https://singaporemrtmaps.com/blog/singapore-mrt-line-colours/)
- North East Line (NEL), purple, HarbourFront to Punggol Coast, 17 stations — [Singapore MRT Line Colours 2026](https://singaporemrtmaps.com/blog/singapore-mrt-line-colours/)
- Circle Line (CCL), printed orange on LTA's map though commonly called yellow by riders, a closed loop with no termini since July 2026, 33 stations — [Singapore MRT Line Colours 2026](https://singaporemrtmaps.com/blog/singapore-mrt-line-colours/); station total confirmed by [LTA Circle Line 6 project page](https://www.lta.gov.sg/content/ltagov/en/upcoming_projects/rail_expansion/circle_line_6.html)
- Circle Line after Stage 6: 33 stations including 12 interchange stations — [LTA Circle Line 6 project page](https://www.lta.gov.sg/content/ltagov/en/upcoming_projects/rail_expansion/circle_line_6.html)
- Circle Line total length given as 39 km across 33 stations with 12 interchanges in LTA's Stage 6 announcement material — [LTA news release, 14 May 2026](https://www.lta.gov.sg/content/ltagov/en/newsroom/2026/5/news-releases/circle-line-stage-6-to-open-for-public-preview-on-4-july-2026.html)
- Downtown Line (DTL), blue, Bukit Panjang to Expo, 35 operational stations, 41.9 km — [SGTrains Downtown Line](https://www.sgtrains.com/network-dtl.html); 35 operational stations also stated by [Wikipedia: Downtown Line](https://en.wikipedia.org/wiki/Downtown_Line)
- Thomson-East Coast Line (TEL), brown, Woodlands North to Bayshore, 27 stations as currently operating — [Singapore MRT Line Colours 2026](https://singaporemrtmaps.com/blog/singapore-mrt-line-colours/)
- Bukit Panjang LRT (BP), grey, loop served from Choa Chu Kang and Bukit Panjang, 13 stations — [Singapore MRT Line Colours 2026](https://singaporemrtmaps.com/blog/singapore-mrt-line-colours/)
- Sengkang LRT (STC, SE, SW), grey, two loops from Sengkang, 13 stations — [Singapore MRT Line Colours 2026](https://singaporemrtmaps.com/blog/singapore-mrt-line-colours/)
- Punggol LRT (PTC, PE, PW), grey, two loops from Punggol, 14 stations — [Singapore MRT Line Colours 2026](https://singaporemrtmaps.com/blog/singapore-mrt-line-colours/)

Line colour hex codes (see the warning in Gaps below):

- North South Line: `#D42E12` — [Simple Wikipedia: Template:SMRT color](https://simple.wikipedia.org/wiki/Template:SMRT_color)
- East West Line: `#009645` — [Simple Wikipedia: Template:SMRT color](https://simple.wikipedia.org/wiki/Template:SMRT_color)
- North East Line: `#9900AA` — [Simple Wikipedia: Template:SMRT color](https://simple.wikipedia.org/wiki/Template:SMRT_color)
- Circle Line: `#FA9E0D` — [Wikipedia: Circle Line (Singapore)](https://en.wikipedia.org/wiki/Circle_Line_(Singapore)) and [Simple Wikipedia: Template:SMRT color](https://simple.wikipedia.org/wiki/Template:SMRT_color)
- Downtown Line: `#005EC4` — [Wikipedia: Downtown Line](https://en.wikipedia.org/wiki/Downtown_Line) and [Simple Wikipedia: Template:SMRT color](https://simple.wikipedia.org/wiki/Template:SMRT_color)
- Thomson-East Coast Line: `#9D5B25` — [Wikipedia: Thomson-East Coast Line](https://en.wikipedia.org/wiki/Thomson%E2%80%93East_Coast_Line) and [Simple Wikipedia: Template:SMRT color](https://simple.wikipedia.org/wiki/Template:SMRT_color)
- Cross Island Line (not yet open): `#97C616` — [Simple Wikipedia: Template:SMRT color](https://simple.wikipedia.org/wiki/Template:SMRT_color)
- All three LRT systems: `#748477` — [Wikipedia: Module:Adjacent stations/Singapore LRT](https://en.wikipedia.org/wiki/Module:Adjacent_stations/Singapore_LRT)

Operators:

- Downtown Line is operated by SBS Transit under the New Rail Financing Framework, on a consolidated rail licence running to 31 December 2032 — [Wikipedia: Downtown Line](https://en.wikipedia.org/wiki/Downtown_Line)
- Sungei Bedok, when it opens, will be operated jointly: SBS Transit for the DTL platforms and SMRT Trains for the TEL platforms — [LandTransportGuru: Sungei Bedok](https://landtransportguru.net/sungei-bedok-station/)

New station codes added by Circle Line Stage 6:

- CC30 Keppel, CC31 Cantonment, CC32 Prince Edward Road — [LandTransportGuru: Circle Line 6 opening](https://landtransportguru.net/circle-line-6-opening/). LTA's own project page does not print these codes in body text; they appear only in image filenames, so treat them as corroborated by LandTransportGuru rather than by LTA directly — [LTA Circle Line 6 project page](https://www.lta.gov.sg/content/ltagov/en/upcoming_projects/rail_expansion/circle_line_6.html)

Circle Line service pattern after loop closure (relevant to map labelling):

- Trains are now signed Clockwise (↻) and Anticlockwise (↺) rather than by terminal station — [LandTransportGuru: Circle Line 6 opening](https://landtransportguru.net/circle-line-6-opening/)
- Weekday peak: full-loop services every 2 minutes, plus a Dhoby Ghaut to Prince Edward Road service via Bishan every 4 minutes between Dhoby Ghaut and Promenade and between Prince Edward Road and Promenade — [LandTransportGuru: Circle Line 6 opening](https://landtransportguru.net/circle-line-6-opening/)
- Off-peak and weekends: full-loop services continue plus a Dhoby Ghaut to Stadium shuttle. On weekends the Dhoby Ghaut branch trains run only as far as Stadium, so passengers going further must change at Promenade, where the first-of-day transfer wait can be 18 to 20 minutes — [LandTransportGuru: Circle Line 6 opening](https://landtransportguru.net/circle-line-6-opening/)

### Inferences

- The "grey" LRT colour is a single shared value across all three LRT systems, so a map does not need three separate LRT colours.
- Because the Circle Line is now a true loop, a map should not draw a separate CE branch stub between Promenade and Marina Bay; the segment Promenade - Bayfront - Marina Bay - Prince Edward Road - Cantonment - Keppel - HarbourFront is now part of the continuous loop.
- Adding the per-line counts above gives 214 station entries, but the network has fewer unique stations because interchanges are counted once per line. The 180 figure quoted on singaporemrtmaps.com is presumably a unique-station count; the source does not reconcile the two numbers and says so, so neither figure should be presented as authoritative.

### Gaps

- LTA does not publish an official hex-code palette on its public website. Every hex value above comes from Wikipedia or Wikipedia templates. Two independent Wikipedia pages agree for DTL, CCL and TEL, which raises confidence, but for a map that must be exactly right the values should be sampled from the official LTA system map PDF. I could not retrieve and colour-sample that PDF in this research pass.
- The official LTA colour *names* (as opposed to common names) were not found in a primary source. The only naming evidence found is that LTA prints the Circle Line in orange while riders call it yellow.
- I could not confirm whether Marina Bay and Bayfront were renumbered from CE2/CE1 to CC33/CC34 when the loop closed. Neither LTA's Stage 6 project page nor LandTransportGuru's opening article mentions the codes for those two stations. This is a material gap for a map builder and must be checked against the current system map before drawing labels.
- Jurong Region Line and Cross Island Line hex codes: the CRL value `#97C616` comes from a single Wikipedia template. I found no sourced hex for the JRL. Since neither line is open in November 2026, this does not affect an operational map.
- Exact current TEL station count: the 27 figure is from a secondary source. TEL has had infill stations added over time (Mount Pleasant remains unopened), so the count should be verified if precision matters.

## Q2. What opened in 2025 and 2026, and what is still under construction

### Takeaway

Two things opened in this period: Hume station (DT4) on 28 February 2025 and Circle Line
Stage 6 on 12 July 2026. Thomson-East Coast Line Stage 5 and the Downtown Line 3 extension
were still unopened as of late October 2026, with only a "second half of 2026" target and
no announced date, so their availability during 2-9 November 2026 is genuinely uncertain.
The Jurong Region Line has slipped to mid-2028 and the Cross Island Line to 2030, so
neither will be open.

### Cited Findings

Open:

- Hume station (between Hillview and Beauty World) opened 28 February 2025 and is the first underground infill station to open in Singapore — [Wikipedia: Downtown Line](https://en.wikipedia.org/wiki/Downtown_Line)
- Circle Line Stage 6 opened for passenger service on 12 July 2026, completing Singapore's first orbital MRT loop; a free public preview of Keppel, Cantonment and Prince Edward Road ran on 4 July 2026 from 9.30am to 9.00pm — [LTA Circle Line 6 project page](https://www.lta.gov.sg/content/ltagov/en/upcoming_projects/rail_expansion/circle_line_6.html); date and preview also in [LTA news release, 14 May 2026](https://www.lta.gov.sg/content/ltagov/en/newsroom/2026/5/news-releases/circle-line-stage-6-to-open-for-public-preview-on-4-july-2026.html) and [LandTransportGuru](https://landtransportguru.net/circle-line-6-opening/)
- CCL6 adds a 4 km, three-station underground extension between HarbourFront and Marina Bay: CC30 Keppel beneath Keppel Road, CC31 Cantonment beneath the former Tanjong Pagar Railway Station, CC32 Prince Edward Road at the southern edge of the CBD about 30 m underground — [LandTransportGuru: Circle Line 6 opening](https://landtransportguru.net/circle-line-6-opening/); 4 km figure also in [LTA Circle Line 6 project page](https://www.lta.gov.sg/content/ltagov/en/upcoming_projects/rail_expansion/circle_line_6.html)
- LTA's stated benefit: a Telok Blangah to Marina Bay trip needs no transfers and saves around 10 minutes — [LTA news release, 14 May 2026](https://www.lta.gov.sg/content/ltagov/en/newsroom/2026/5/news-releases/circle-line-stage-6-to-open-for-public-preview-on-4-july-2026.html)
- A Sengkang West LRT segment reopened on 4 October (year implied 2026), per a headline on singaporemrtmaps.com, but the article gives no detail — [Singapore MRT Line Colours 2026](https://singaporemrtmaps.com/blog/singapore-mrt-line-colours/). Low confidence; needs a primary source.

Not open as of late October 2026:

- Thomson-East Coast Line Stage 5 runs Bayshore to Sungei Bedok and adds two stations, TE30 Bedok South and TE31/DT37 Sungei Bedok — [Wikipedia: Thomson-East Coast Line](https://en.wikipedia.org/wiki/Thomson%E2%80%93East_Coast_Line)
- Downtown Line 3 extension is a 2.2 km, two-station extension: DT36 Xilin and DT37 Sungei Bedok, with Sungei Bedok as the DTL/TEL interchange. Construction began 21 July 2016 — [SGTrains Downtown Line](https://www.sgtrains.com/network-dtl.html)
- In a February 2026 parliamentary reply, the Ministry of Transport said TEL5 and the DTL3 extension are expected to open in the second half of 2026, with more details on specific opening dates to be announced later — [MOT newsroom: Update on Progress of Train Lines Under Extension and Construction](https://www.mot.gov.sg/news-resources/newsroom/update-on-progress-of-train-lines-under-extension-and-construction/)
- LTA's March 2026 factsheet said three more stations under TEL5 and DTL3e are on track to open in the second half of 2026 — [LTA: Next phase of rail development](https://www.lta.gov.sg/content/ltagov/en/newsroom/2026/3/news-releases/next-phase-of-rail-development.html)
- LTA's 28 April 2026 release reiterated second-half 2026 and said LTA and the rail operators would conduct a series of final systems integration tests before opening — [LTA: Train service adjustments, TEL and DTL](https://www.lta.gov.sg/content/ltagov/en/newsroom/2026/4/news-releases/train-service-adjustments-tel-and-dtl-to-facilitate-rail-expansion-works.html)
- A July 2026 report describes LTA running test trains across the entire Downtown Line from Bukit Panjang to Xilin, plus trips to the East Coast Integrated Depot — [SGTrains, July 2026](https://blog.sgtrains.com/2026/07/downtown-line-to-end-earlier-on-fridays-start-later-on-saturdays-from-jul-10-to-sep-5-2026/)
- Sungei Bedok's opening has slipped repeatedly: first targeted 2024, pushed to 2025 in 2022, then pushed to 2026 at Committee of Supply 2024, with delays attributed to COVID-19 and tunnelling near existing critical infrastructure — [LandTransportGuru: Sungei Bedok](https://landtransportguru.net/sungei-bedok-station/); also [Wikipedia: Sungei Bedok MRT station](https://en.wikipedia.org/wiki/Sungei_Bedok_MRT_station)
- Jurong Region Line Stage 1 was delayed to mid-2028, announced by Acting Transport Minister Jeffrey Siow in Parliament in March 2026, a six-month slip from the original late-2027 target, attributed to construction complexity and unrecovered pandemic delays — [The Online Citizen, 4 March 2026](https://theonlinecitizen.com/2026/03/04/jurong-region-line-stage-1-opening-delayed-to-mid-2028)
- JRL Stage 1 covers the Choa Chu Kang to Boon Lay trunk plus Bahar Junction to Tawas. Interim shuttle buses are planned for end-2027 to serve areas Stage 1 was to cover. Stage 2 was set for 2028 and Stage 3 for 2029, dates which may shift. An infill station JS2A between Tengah Central and Choa Chu Kang West is projected for the mid-2030s — [The Online Citizen, 4 March 2026](https://theonlinecitizen.com/2026/03/04/jurong-region-line-stage-1-opening-delayed-to-mid-2028); see also [Wikipedia: Jurong Region Line](https://en.wikipedia.org/wiki/Jurong_Region_Line)
- Cross Island Line Phase 1 (Aviation Park to Bright Hill, 12 stations) is targeted for 2030; construction officially began 18 January 2023 — [Wikipedia: Cross Island Line](https://en.wikipedia.org/wiki/Cross_Island_Line)
- CRL Phase 2 (Turf City to Jurong Lake District) and the Punggol Extension are targeted for 2032; CRL Phase 3 is targeted for the late 2030s and the Changi Terminal 5 extension for the mid-2030s. CRL Phase 3 stations were announced on 31 July 2026 — [Wikipedia: Cross Island Line](https://en.wikipedia.org/wiki/Cross_Island_Line)
- Downtown Line 2 extension to Sungei Kadut: announced in the Land Transport Master Plan 2040 on 25 May 2019, would extend the line north from Bukit Panjang to a future Sungei Kadut station on the NSL between Yew Tee and Kranji, expected completion 2040 — [SGTrains Downtown Line](https://www.sgtrains.com/network-dtl.html)

### Inferences

- For the 2-9 November 2026 window, treat the network as: NSL, EWL+CG, NEL, CCL (closed loop), DTL (Bukit Panjang to Expo), TEL (Woodlands North to Bayshore), plus the three LRT systems. That is the safe baseline for a map.
- TEL5 and DTL3e could open during the trip window, but nothing found supports planning around it. The pattern of past openings is that LTA announces a specific date roughly 6 to 10 weeks ahead with a public preview a week before passenger service (CCL6: announced 14 May for a 4 July preview and 12 July opening; TEL4: announced March 2024 for a 23 June 2024 opening). No such announcement had appeared by late October 2026, which makes a very-early-November opening unlikely and a December 2026 opening plausible.
- Practical consequence for Hillview: the DTL eastern terminus should be drawn as Expo (DT35). If Xilin and Sungei Bedok do open mid-trip, the only change relevant to a Hillview-based traveller is a second DTL route to the TEL, which is not useful for any of the destinations in Q4.

### Gaps

- No confirmed opening date for TEL5, DTL3e, Bedok South, Xilin or Sungei Bedok was found in any source, including LTA's newsroom. The most recent official statement found is from 28 April 2026. I searched LTA, LandTransportGuru, SGTrains, SBS Transit and SMRT domains specifically and found nothing newer than July 2026 on this question. This should be re-checked on LTA's newsroom close to departure.
- The reported 4 October Sengkang West LRT reopening is sourced only to a headline on a secondary site with no supporting article text. I could not verify what it refers to or confirm the year.

## Q3. Where exactly is Hillview station (DT3), and what are its exits

### Takeaway

Hillview is an underground island-platform station on the Downtown Line at 510 Upper Bukit
Timah Road, Singapore 678211, opened 27 December 2015 with DTL Stage 2. OneMap places the
station entity at 1.36234, 103.76742. It has exactly two exits, A and B, both at ground
level on opposite sides of Upper Bukit Timah Road.

### Cited Findings

Coordinates, from OneMap's search API (SVY21 and WGS84 values returned directly by
`https://www.onemap.gov.sg/api/common/elastic/search?searchVal=HILLVIEW%20MRT%20STATION&returnGeom=Y&getAddrDetails=Y`
on 24 October 2026). Note the API returned an "Authentication token missing" message alongside
valid results, so the data is authoritative OneMap data but was retrieved without a token
and should be re-pulled with a token if it is going into production:

- `HILLVIEW MRT STATION (DT3)`, 510 Upper Bukit Timah Road, postal 678211: latitude **1.362344868035584**, longitude **103.7674182540068** (SVY21 X 20666.06754996069, Y 38266.7898455672) — OneMap API
- `HILLVIEW MRT STATION EXIT A`: latitude **1.362497532918702**, longitude **103.7676896995305** (SVY21 X 20696.27672298532, Y 38283.66993686929) — OneMap API
- `HILLVIEW MRT STATION EXIT B`: latitude **1.362088207171618**, longitude **103.7670880086075** (SVY21 X 20629.31431778427, Y 38238.41058403254) — OneMap API
- A second, unpostcoded `HILLVIEW MRT STATION` record also exists at latitude 1.362888457151686, longitude 103.7677809077064. The DT3-suffixed record with postal code 678211 is the one to use. — OneMap API
- Wikipedia gives the station as 01°21′45″N, 103°46′03″E, i.e. 1.36250, 103.76750 — [Wikipedia: Hillview MRT station](https://en.wikipedia.org/wiki/Hillview_MRT_station). This is a DMS-rounded value consistent with OneMap to about 20 m but not precise enough for a map at street scale.

Station basics:

- Address 510 Upper Bukit Timah Road, Singapore 678211; underground; island platform; opened 27 December 2015; Downtown Line; operated by SBS Transit — [LandTransportGuru: Hillview](https://landtransportguru.net/hillview-station/)
- Opened 27 December 2015 as part of Downtown Line Stage 2; two platforms (one island platform) and two tracks, underground; station abbreviation HVW; owner Land Transport Authority — [Wikipedia: Hillview MRT station](https://en.wikipedia.org/wiki/Hillview_MRT_station)

Exits:

- **Exit A** is on the southbound side of Upper Bukit Timah Road and has a pick-up/drop-off point. It serves Dairy Farm Road, Bukit Panjang Methodist Church, John Wesley Centre, Methodist School of Music, MOE Dairy Farm Adventure Centre, Praisehaven (The Salvation Army), Saint Francis Methodist School, Trinity Theological College and The Rail Mall — [LandTransportGuru: Hillview](https://landtransportguru.net/hillview-station/)
- **Exit B** is on the northbound side of Upper Bukit Timah Road and has taxi stand H21 plus a pick-up/drop-off point. It serves Hillview Road, HillV2 mall and Hillview Community Club — [LandTransportGuru: Hillview](https://landtransportguru.net/hillview-station/)
- Both exits are at ground level and offer barrier-free access — [LandTransportGuru: Hillview](https://landtransportguru.net/hillview-station/)

Vertical layout (matters for door-to-door time):

- L1 street level: bus stops, taxi stand, pick-up/drop-off
- B1 transfer level: escalators and lifts link Exit A to the concourse; escalators link Exit B to the concourse
- B2 concourse: faregates, ticketing service kiosks, Passenger Service Centre, public toilets, ATM
- B3 platforms: Platform A towards DT1/BP6 Bukit Panjang via Cashew; Platform B towards DT35/CG1 Expo via Hume
- Bicycle racks at station exits; the station is a designated Civil Defence shelter
— all from [LandTransportGuru: Hillview](https://landtransportguru.net/hillview-station/)

Bus connections at Hillview (useful fallback and for the Jurong East question):

- Exit A, stop 43069: services 67, 75, 170, 178, 184, 961, 961M, 973
- Exit B, stop 43061: services 67, 75, 170, 176, 178, 184, 961, 961M, 963, 970
- Other nearby stops: Glendale Pk Condo (43271), Aft Hillview Stn (43279), Bef Hillview Stn Exit B (42991), served by several of the above plus 653 and 973
- If the DTL is disrupted, MRT bridging buses towards Bukit Panjang board at Exit B (43061) and those towards Expo board at Exit A (43069)
— all from [LandTransportGuru: Hillview](https://landtransportguru.net/hillview-station/)

### Inferences

- Exit A and Exit B are about 80 m apart on the ground and sit on opposite sides of Upper Bukit Timah Road, which the OneMap coordinates bear out (a difference of roughly 0.00041 degrees of latitude and 0.00060 degrees of longitude).
- Platforms are at B3, two levels below the concourse. Allow 3 to 4 minutes from faregate to platform, and the same in reverse, when estimating door-to-door times.
- For a traveller staying near HillV2 or Hillview Road, Exit B is the relevant one; for The Rail Mall and Dairy Farm, Exit A.

### Gaps

- Neither source gives a lift at Exit B (escalators only are listed), so step-free access appears to be via Exit A. I did not find an explicit accessibility statement confirming which exit is the lift-served one, so this should not be stated as fact.
- No official LTA or SBS Transit station page for Hillview was retrieved directly; the exit detail rests on LandTransportGuru, which is a well-regarded specialist site but not a primary operator source.

## Q4. Journey times by MRT from Hillview to key destinations

### Takeaway

Only one published point-to-point figure was found for a Hillview journey (Orchard, about
20 minutes via Newton). Everything else below is computed from the Downtown Line's
published end-to-end running time and labelled as an estimate. Hillview's position at DT3
means it reaches Botanic Gardens, Newton, Little India, Bugis, Promenade and Bayfront with
no transfer at all, which makes it unusually well connected for an outer-western station.

### Cited Findings

Sourced anchors:

- Downtown Line end-to-end journey time, Bukit Panjang (DT1) to Expo (DT35), is 69 minutes — [Wikipedia: Downtown Line](https://en.wikipedia.org/wiki/Downtown_Line)
- Downtown Line length is 41.9 km over 35 operational stations — [SGTrains Downtown Line](https://www.sgtrains.com/network-dtl.html)
- Orchard MRT to Hillview MRT: no direct train, change at Newton, journey including transfers approximately 20 minutes — [Rome2Rio: Orchard MRT Station to Hillview MRT Station](https://www.rome2rio.com/s/Orchard-MRT-Station/Hillview-MRT-Station). Caveat: this page self-reports as roughly 1,500 days old, so it predates Hume station's insertion into the line in February 2025.
- The same Rome2Rio pages give a taxi between Orchard and Hillview as about 11 minutes and a bus journey as about 56 minutes — [Rome2Rio](https://www.rome2rio.com/s/Orchard-MRT-Station/Hillview-MRT-Station)
- Hillview's platform directions are Platform A towards Bukit Panjang via Cashew and Platform B towards Expo via Hume — [LandTransportGuru: Hillview](https://landtransportguru.net/hillview-station/)

### Inferences

Method, stated so it can be checked or rejected: 69 minutes over 34 inter-station hops on
the DTL gives an average of **2.03 minutes per hop**, inclusive of dwell time. I use 2.0
minutes per DTL hop and the same for NSL, EWL, NEL and CCL hops as a working figure, add
**4 minutes per interchange** for the walk plus wait, and add **5 to 7 minutes** at Hillview
for faregate-to-platform descent (3 levels) plus average wait. Every number below is an
estimate, not a published timetable value. Where a figure can be cross-checked it is noted.

DTL station order used: DT1 Bukit Panjang, DT2 Cashew, DT3 Hillview, DT4 Hume, DT5 Beauty
World, DT6 King Albert Park, DT7 Sixth Avenue, DT8 Tan Kah Kee, DT9 Botanic Gardens,
DT10 Stevens, DT11 Newton, DT12 Little India, DT13 Rochor, DT14 Bugis, DT15 Promenade,
DT16 Bayfront, DT17 Downtown, DT18 Telok Ayer, DT19 Chinatown, DT20 Fort Canning,
DT21 Bencoolen, DT22 Jalan Besar ... DT35 Expo.

No-transfer destinations (all on the DTL from Hillview Platform B, except Bukit Panjang
which is Platform A):

| Destination | Stops from DT3 | Est. train time | Est. door-to-door | Interchanges |
|---|---|---|---|---|
| Bukit Panjang (DT1/BP6) | 2 (Platform A) | ~4 min | ~10-12 min | 0 |
| Botanic Gardens (DT9/CC19) | 6 | ~12 min | ~18-20 min | 0 |
| Newton (DT11/NS21) | 8 | ~16 min | ~22-24 min | 0 |
| Little India (DT12/NE7) | 9 | ~18 min | ~24-26 min | 0 |
| Bugis (DT14/EW12) | 11 | ~22 min | ~28-30 min | 0 |
| Promenade (DT15/CC4) | 12 | ~24 min | ~30-32 min | 0 |
| Bayfront (DT16) - MBS, Gardens by the Bay | 13 | ~26 min | ~32-34 min | 0 |
| Chinatown (DT19/NE4) | 16 | ~32 min | ~38-40 min | 0 |

One-transfer and two-transfer destinations:

| Destination | Route | Est. door-to-door | Interchanges | Where |
|---|---|---|---|---|
| Orchard (NS22/TE14) | DTL to Newton (8 stops), NSL southbound 1 stop | ~22-25 min train time; published figure is about 20 min | 1 | Newton |
| Raffles Place (EW14/NS26) | DTL to Bugis (11 stops), EWL westbound 2 stops via City Hall | ~34-36 min | 1 | Bugis |
| Lavender (EW11) for Kampong Glam | DTL to Bugis (11 stops), EWL eastbound 1 stop | ~32-34 min | 1 | Bugis |
| Kampong Glam itself | DTL direct to Bugis, then 5-10 min walk | ~33-40 min | 0 | n/a |
| HarbourFront (NE1/CC29) for Sentosa | DTL to Botanic Gardens (6 stops), CCL anticlockwise 10 stops to HarbourFront | ~37-40 min | 1 | Botanic Gardens |
| HarbourFront, alternative | DTL to Chinatown (16 stops), NEL southbound 2 stops via Outram Park | ~42-45 min | 1 | Chinatown |
| Clarke Quay (NE5) | DTL to Chinatown (16 stops), NEL northbound 1 stop | ~42-44 min | 1 | Chinatown |
| Clarke Quay, alternative | DTL direct to Fort Canning (17 stops), then ~5 min walk to the riverside | ~40-45 min | 0 | n/a |
| Jurong East (NS1/EW24) | DTL to Botanic Gardens (6 stops), CCL anticlockwise 3 stops to Buona Vista, EWL westbound 3 stops | ~38-42 min | 2 | Botanic Gardens, Buona Vista |
| Jurong East, alternative | DTL to Bukit Panjang (2 stops), BPLRT to Choa Chu Kang, NSL southbound 3 stops | ~33-38 min | 2 | Bukit Panjang, Choa Chu Kang |
| Changi Airport (CG2) | DTL to Bugis (11 stops), EWL eastbound 8 stops to Tanah Merah, Changi branch 2 stops | ~58-65 min | 2 | Bugis, Tanah Merah |
| Changi Airport, alternative | DTL direct to Expo (32 stops, ~65 min), then CG 1 stop | ~75-80 min | 1 | Expo |

Notes on the harder cases:

- **Jurong East** is the weakest connection from Hillview despite being geographically close (about 7 km). The rail network offers no direct western link; both options need two changes. The Bukit Panjang/BPLRT route is probably quicker but involves an LRT leg and two transfers; the Botanic Gardens/Buona Vista route is all heavy rail. A bus from Hillview towards Bukit Batok and then one NSL stop may well beat both, and services 173 and 177 run along Upper Bukit Timah Road; this was not verified and should be checked in a live journey planner.
- **Changi Airport** via Bugis and Tanah Merah is materially faster than riding the DTL to its Expo terminus, because the EWL has wider station spacing and higher line speed than the DTL over the eastern corridor. The DTL-to-Expo route is the simplest but the slowest.
- **HarbourFront for Sentosa**: the Botanic Gardens to CCL route wins because it leaves the DTL after only six stops, whereas the Chinatown route rides 16 DTL stops first.
- **Chinatown** is reachable with no transfer at all on the DTL, which beats any routing via Newton and Dhoby Ghaut (that alternative needs two changes and comes out roughly the same or slower).

### Gaps

- No official LTA or operator journey-time matrix was found. LTA's DataMall provides network data but I did not retrieve a timetable or travel-time dataset in this pass. All times above except Orchard are my own computation from the published 69-minute end-to-end DTL figure.
- The 69-minute end-to-end figure is from Wikipedia and may predate the February 2025 insertion of Hume station, which would have added roughly two minutes to the end-to-end run. If so, the per-hop average is slightly conservative and real times may be marginally shorter than listed.
- Cross-line per-hop times differ in reality: EWL and NSL stations are further apart than DTL stations, so my uniform 2.0 min/hop understates NSL/EWL leg speed on long runs and may overstate it on short central runs. The Changi Airport estimate is the most exposed to this.
- Rome2Rio is an aggregator, not a primary source, and its Hillview page is roughly four years old. The ~20 minute Orchard figure should be re-verified in Google Maps or the LTA MyTransport journey planner.
- I did not verify whether bus services 173 or 177 serve the Hillview stops; the verified list of services at the two Hillview stops is given in Q3 and does not include them.

## Q5. Downtown Line frequency at Hillview, and first and last train times

### Takeaway

Published first and last train times for Hillview are 06:13 towards Bukit Panjang and 05:34
towards Expo on Mondays to Saturdays, twenty minutes later on Sundays and public holidays,
with last trains at 00:45 towards Bukit Panjang and 23:38 towards Expo every day. The only
frequency figure found for the Downtown Line is a line-wide 2.5 to 5 minutes; no
Hillview-specific peak and off-peak headways were published in any source I found.

### Cited Findings

First and last trains at Hillview (DT3). Two independent sources agree exactly:

| Direction | First train, Mon-Sat | First train, Sun and public holidays | Last train, daily |
|---|---|---|---|
| Towards DT1 Bukit Panjang (Platform A) | 06:13 | 06:33 | 00:45 |
| Towards DT35 Expo (Platform B) | 05:34 | 05:54 | 23:38 |

- [SGTrains: Hillview train timings](https://www.sgtrains.com/guide-traintiming?station=Hillview) — gives one first-train time for Monday to Saturday combined, one for Sundays and public holidays, and a single last-train time for every day. SGTrains notes these are scheduled times that do not reflect service-hour adjustments, and advises arriving early for late travel.
- [LandTransportGuru: Hillview](https://landtransportguru.net/hillview-station/) — same values.

Frequency:

- Downtown Line trains run every 2.5 to 5 minutes — [Wikipedia: Downtown Line](https://en.wikipedia.org/wiki/Downtown_Line)
- Rolling stock is Bombardier MOVIA C951, three cars per train, on a medium-capacity line — [SGTrains Downtown Line](https://www.sgtrains.com/network-dtl.html) and [Wikipedia: Downtown Line](https://en.wikipedia.org/wiki/Downtown_Line)
- SGTrains' Downtown Line page does not state peak or off-peak frequency — [SGTrains Downtown Line](https://www.sgtrains.com/network-dtl.html)
- For comparison, the Circle Line runs full-loop services every 2 minutes in the weekday peak — [LandTransportGuru: Circle Line 6 opening](https://landtransportguru.net/circle-line-6-opening/)

### Inferences

- The asymmetry in first-train times makes sense from Hillview's position at DT3: trains towards Expo start their run from Bukit Panjang two stops away and reach Hillview early (05:34), whereas trains towards Bukit Panjang have to come all the way from the eastern end of the line and so arrive later (06:13). The same logic explains why the last train towards Bukit Panjang is 00:45 while the last eastbound train leaves at 23:38, more than an hour earlier.
- The practical constraint for a traveller based at Hillview: the last useful inbound-to-outbound return is what matters, and the eastbound 23:38 cut-off is not the relevant one. Coming home from the city, the controlling times are the last DTL westbound departures from Bugis, Promenade or Chinatown, which were not found in this research and should be checked for each station the traveller plans to use late at night.
- The 2.5-to-5-minute band maps, in the normal Singapore pattern, to roughly 2.5 to 3 minutes in the weekday morning and evening peaks and roughly 4 to 5 minutes midday, late evening and at weekends. This is an inference from the published band, not a sourced split.
- Three-car MOVIA C951 trains mean lower capacity per train than the six-car trains on the NSL and EWL, so peak crowding on the DTL is felt more per train even at tight headways.

### Gaps

- No Hillview-specific or DTL-specific peak and off-peak headway figures were found from SBS Transit or LTA. The 2.5 to 5 minute band is line-wide and comes from Wikipedia. SBS Transit's own site would be the primary source and was not retrieved.
- Weekday and Saturday first-train times are published as a single combined figure, so if the traveller needs a Saturday-specific value it cannot be separated from these sources.
- Last-train times from the city-centre stations back towards Hillview were not retrieved. These are the operationally important ones for an evening out and should be looked up per station.

## Q6. Which interchanges matter most from Hillview, and the best transfer patterns

### Takeaway

Four interchanges carry almost all of a Hillview resident's trips: Botanic Gardens for
anything on the Circle Line and the south-west, Newton for Orchard and the North South
Line, Bugis for the East West Line and the east, and Chinatown for the North East Line and
HarbourFront. The city centre needs no interchange at all.

### Cited Findings

- Hillview is on the Downtown Line only; it is not itself an interchange — [LandTransportGuru: Hillview](https://landtransportguru.net/hillview-station/)
- Botanic Gardens is DT9/CC19, a DTL to Circle Line interchange — derived from DTL and CCL station codes in [SGTrains Downtown Line](https://www.sgtrains.com/network-dtl.html) and [Wikipedia: Circle Line (Singapore)](https://en.wikipedia.org/wiki/Circle_Line_(Singapore))
- Newton is NS21/DT11, a DTL to North South Line interchange, and is the published change point for Hillview to Orchard — [Rome2Rio](https://www.rome2rio.com/s/Orchard-MRT-Station/Hillview-MRT-Station)
- Orchard is NS22/TE14, so Newton also gives one-change access to the Thomson-East Coast Line via a second change at Orchard — [GESS: Orchard MRT Station (NS22/TE14)](https://www.gess.edu.sg/en/news/orchard-mrt-station-ns22-te14)
- The Circle Line now has 12 interchange stations across its 33 — [LTA Circle Line 6 project page](https://www.lta.gov.sg/content/ltagov/en/upcoming_projects/rail_expansion/circle_line_6.html)
- Promenade (DT15/CC4) is the Circle Line transfer point where weekend branch-service passengers must change, with a possible 18 to 20 minute first-of-day wait — [LandTransportGuru: Circle Line 6 opening](https://landtransportguru.net/circle-line-6-opening/)
- The Downtown Line's own interchange-rich central section from Newton through Chinatown gives direct access to NSL (Newton), NEL (Little India, Chinatown), EWL (Bugis), CCL (Botanic Gardens, Promenade, Bayfront area) — derived from the DTL station codes listed in [SGTrains Downtown Line](https://www.sgtrains.com/network-dtl.html)

### Inferences

Recommended transfer patterns from Hillview:

- **City centre (Orchard, Bugis, Raffles Place, Marina Bay, Chinatown, Clarke Quay, Little India):** stay on the Downtown Line. Bugis, Promenade, Bayfront, Chinatown, Little India and Newton are all direct. Only Orchard and Raffles Place need a single change, at Newton and Bugis respectively. This is the strongest feature of Hillview as a base: the DTL is the line that threads the city centre, so most central destinations are a single-seat ride of 20 to 40 minutes.
- **The east (Changi Airport, Tampines, Katong, Changi):** change at Bugis to the East West Line rather than riding the DTL to its eastern end. The DTL's eastern arm swings north through Macpherson, Bedok Reservoir and Tampines, which is a long detour for anything on the EWL corridor.
- **Sentosa and HarbourFront:** change at Botanic Gardens to the Circle Line anticlockwise and ride to HarbourFront. This leaves the DTL after six stops rather than sixteen.
- **The south-west (Holland Village, one-north, Buona Vista, Kent Ridge, Labrador Park):** change at Botanic Gardens. The Circle Line anticlockwise from CC19 serves the whole south-western arc directly.
- **The north (Woodlands, Yishun, Ang Mo Kio, Bishan):** change at Botanic Gardens to the Circle Line clockwise for Bishan and the NSL north, or at Newton to the NSL directly. Newton is simpler; Botanic Gardens to Bishan to NSL avoids the central congestion.
- **Thomson-East Coast Line destinations:** this is the gap in Hillview's connectivity. There is no one-change DTL-to-TEL interchange west of the city. Options are Newton then Orchard (two changes), or Botanic Gardens then Caldecott on the CCL (two changes), or Promenade then Marina Bay. None is quick. If TEL5 and DTL3e open, Sungei Bedok adds a DTL/TEL interchange, but at the far eastern end of both lines, which does not help a westbound Hillview traveller.
- **Avoid as a transfer point:** Promenade on weekends for Circle Line journeys, given the branch-service pattern and the documented long first-of-day transfer wait. Use Botanic Gardens instead for CCL trips.

Overall assessment of Hillview's connectivity: strong for the city centre and the
south-west, adequate for the east with one change at Bugis, weak for Jurong East and the
western industrial area despite short geographic distance, and weak for the
Thomson-East Coast Line corridor.

### Gaps

- I did not verify the physical transfer walk times at Botanic Gardens, Newton, Bugis or Chinatown. These vary a lot in Singapore (Botanic Gardens and Newton are compact; Bugis and Promenade involve longer walks), and my uniform 4-minute transfer allowance in Q4 may understate Bugis and Promenade.
- Whether the Circle Line weekend branch pattern affects a Botanic Gardens to HarbourFront journey was not established. Botanic Gardens is on the main loop, so full-loop services should serve it, but the interaction with the Dhoby Ghaut to Stadium weekend shuttle was not confirmed.

## Q7. Engineering works, early closures and upgrades affecting the Downtown Line in late 2026

### Takeaway

The Downtown Line had Friday early closures and Saturday late openings from 10 July to
5 September 2026, which finished well before the travel window. No announced works affect
the Downtown Line during 2-9 November 2026, but this is an absence of evidence rather than
a positive confirmation, and LTA's newsroom should be re-checked closer to departure.

### Cited Findings

- Downtown Line, 10 July to 5 September 2026, Fridays and Saturdays: services ended at 11.30pm on Fridays and started at 8.30am on Saturdays. Shuttle buses S43 (Bukit Panjang to Bugis), S42 (Bugis to Macpherson) and S41 (Macpherson to Expo) ran at about 5 to 10 minute intervals — [LTA: Train service adjustments, TEL and DTL](https://www.lta.gov.sg/content/ltagov/en/newsroom/2026/4/news-releases/train-service-adjustments-tel-and-dtl-to-facilitate-rail-expansion-works.html); also reported by [SGTrains, July 2026](https://blog.sgtrains.com/2026/07/downtown-line-to-end-earlier-on-fridays-start-later-on-saturdays-from-jul-10-to-sep-5-2026/)
- Thomson-East Coast Line, 22 May to 4 July 2026, Fridays and Saturdays: same 11.30pm end and 8.30am start, with shuttle buses S51 (Woodlands North to Caldecott), S52 (Caldecott to Marina Bay) and S53 (Marina Bay to Bayshore) at about 5 to 10 minute intervals, or about 10 minutes for S53 — [LTA: Train service adjustments, TEL and DTL](https://www.lta.gov.sg/content/ltagov/en/newsroom/2026/4/news-releases/train-service-adjustments-tel-and-dtl-to-facilitate-rail-expansion-works.html)
- Stated reason: preparing for the opening of TEL Stage 5 and the DTL extension in the second half of 2026. Final systems integration tests needed longer engineering hours than nightly windows allow, including full-line test runs and launching and withdrawing trains from the East Coast Integrated Depot — [LTA: Train service adjustments, TEL and DTL](https://www.lta.gov.sg/content/ltagov/en/newsroom/2026/4/news-releases/train-service-adjustments-tel-and-dtl-to-facilitate-rail-expansion-works.html)
- The LTA release does not mention Hillview by name, but DTL shuttle S43 started at Bukit Panjang and the test runs covered Bukit Panjang to Xilin, so the western end of the line including Hillview was within the affected stretch — [LTA: Train service adjustments, TEL and DTL](https://www.lta.gov.sg/content/ltagov/en/newsroom/2026/4/news-releases/train-service-adjustments-tel-and-dtl-to-facilitate-rail-expansion-works.html)
- SGTrains notes its published first and last train times are scheduled times that do not reflect service-hour adjustments — [SGTrains: Hillview train timings](https://www.sgtrains.com/guide-traintiming?station=Hillview)

### Inferences

- The July-to-September DTL window closed on 5 September 2026, so the Friday/Saturday restrictions do not apply to 2-9 November 2026 on the basis of what has been announced.
- If LTA announces a TEL5/DTL3e opening date for late 2026 or early 2027, a further round of early closures is plausible in the run-up, following the pattern of the May-to-July TEL window and the July-to-September DTL window. The traveller should check LTA's newsroom in the week before departure.
- A public preview day, if TEL5/DTL3e opens around the travel window, would mean free travel on the new stations but would not affect Hillview services.

### Gaps

- I found no announcement either confirming or ruling out Downtown Line engineering works during November 2026. Searches of LTA, LandTransportGuru, SGTrains, SBS Transit and SMRT domains surfaced nothing newer than July 2026 on DTL service adjustments. This is an absence of found evidence, not a confirmation that no works are planned.
- No information was found on DTL signalling or rolling-stock upgrade programmes that might cause late-2026 disruption.
