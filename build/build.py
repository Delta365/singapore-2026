import json, re, math, subprocess, urllib.parse

SRC="/Users/sanjivanrane/Desktop/claude/Singapore 2026/research_notes/Singapore November 2026 trip groundwork/sg_mrt_lrt_stations.geojson"
st=json.load(open(SRC))
LINES={'NS':("North South Line","#D42E12"),'EW':("East West Line","#009645"),
 'CG':("Changi Airport Branch","#009645"),'NE':("North East Line","#9900AA"),
 'CC':("Circle Line","#FA9E0D"),'DT':("Downtown Line","#005EC4"),
 'TE':("Thomson-East Coast Line","#9D5B25"),'SE':("Sengkang LRT","#748477"),
 'SW':("Sengkang LRT","#748477"),'STC':("Sengkang LRT","#748477"),'PTC':("Punggol LRT","#748477"),
 'BP':("Bukit Panjang LRT","#748477"),'PE':("Punggol LRT","#748477"),'PW':("Punggol LRT","#748477")}
NOT_OPEN={'DT36','DT37','TE30','TE31'}
pre=lambda c:(re.match(r'^([A-Z]+)',c) or [None,''])[1]
def num(c):
    m=re.match(r'^[A-Z]+(\d+)$',c); return int(m.group(1)) if m else None
stations={}
for f in st['features']:
    p=f['properties']; lon,lat=f['geometry']['coordinates']
    codes=[c for c in (p.get('codes') or []) if c not in NOT_OPEN and pre(c) in LINES]
    if not codes: continue
    n=p['name']
    if n in stations: stations[n]['codes']=sorted(set(stations[n]['codes'])|set(codes)); continue
    stations[n]={'n':n,'codes':sorted(set(codes)),'lat':round(lat,6),'lon':round(lon,6)}
by_code={c:s['n'] for s in stations.values() for c in s['codes']}
order={}
for s in stations.values():
    for c in s['codes']: order.setdefault(pre(c),[]).append((num(c) or 0,c,s['n']))
polys={}
for p,v in order.items():
    if p in ('STC','PTC'): continue
    polys[p]=[[stations[n]['lat'],stations[n]['lon']] for _,_,n in sorted(v)]
tm=stations['Tanah Merah']; polys['CG']=[[tm['lat'],tm['lon']]]+[x for x in polys['CG'] if x!=[tm['lat'],tm['lon']]]
pr=stations['Promenade']; polys['CC'].append([pr['lat'],pr['lon']])

INTER=[('DT9','CC19'),('DT15','CC4'),('DT26','CC10'),('DT16','CC34'),('DT10','TE11'),('DT11','NS21'),
       ('DT12','NE7'),('DT19','NE4'),('DT14','EW12'),('DT32','EW2'),('DT35','CG1'),('DT1','BP6')]
HOP,XFER,OVER,WALK=2.03,4.0,6.0,13.3
def ride(codes):
    best=None
    for c in codes:
        p,n=pre(c),num(c)
        if n is None: continue
        if p=='DT': cand=(OVER+HOP*abs(n-3),0,None)
        else:
            cand=None
            for dtc,oc in INTER:
                if pre(oc)!=p: continue
                m=OVER+HOP*abs(num(dtc)-3)+XFER+HOP*abs(num(oc)-n)
                if cand is None or m<cand[0]: cand=(m,1,by_code.get(dtc))
        if cand and (best is None or cand[0]<best[0]): best=cand
    return best
def hav(a,b,c,d):
    p1,p2=math.radians(a),math.radians(c)
    x=math.sin((p2-p1)/2)**2+math.cos(p1)*math.cos(p2)*math.sin(math.radians(d-b)/2)**2
    return 12742*math.asin(math.sqrt(x))

places=json.load(open("places.json"))
labels={p['label'] for p in places}
if 'Ya Kun Kaya Toast' not in labels:
    u="https://www.onemap.gov.sg/api/common/elastic/search?"+urllib.parse.urlencode({"searchVal":"Far East Square","returnGeom":"Y","getAddrDetails":"Y","pageNum":"1"})
    t=json.loads(subprocess.run(["curl","-s","-m","20",u],capture_output=True,text=True).stdout)["results"][0]
    places.append({"label":"Ya Kun Kaya Toast","cat":"hawker","note":"The original kaya toast shop, Far East Square",
        "lat":round(float(t["LATITUDE"]),6),"lon":round(float(t["LONGITUDE"]),6),"addr":"Far East Square, 18 China Street","src":"OneMap"})
    json.dump(places,open("places.json","w"),indent=1)

# notes from your saved videos
NOTES={
 "Maxwell Food Centre":"Ah Tai chicken rice (founded by Tian Tian's former chef, shorter queue) or Tian Tian itself. Old Nyonya laksa, Maxwell Fuzhou oyster cake, rojak, popiah",
 "Chinatown Complex Food Centre":"Ann Chin Popiah, Old Amoy Chendol #02-008, 168 CMY Satay #02-168 (closed Mondays), Hawker Chan. Big and busy, go before noon",
 "Hawker Chan":"Soya sauce chicken rice, 335 Smith Street #02-126. Lost its Michelin star in 2021; optional",
 "Old Airport Road Food Centre":"Aunty Oats Pancake (your oats pancake) and Hougang Otah #01-166 are both here. Dinner",
 "Tiong Bahru Market":"Tiong Bahru Hainanese Boneless Chicken Rice #02-82 opens 10am and sells out. Rest day Monday",
 "Ya Kun Kaya Toast":"The original Far East Square shop. Open Saturdays from about 8:30am",
 "ION Orchard":"LiXin Teochew fishball noodles has a food-court outlet here",
 "Changi Village Hawker Centre":"Nasi lemak at International Muslim Food Stall #01-03",
 "Maxwell Food Centre":"Tian Tian chicken rice on Tuesday (Ah Tai is closed on Tuesdays), Rojak Popiah & Cockle #01-56, Fu Shun roast meats, Old Nyonya laksa, Maxwell Fuzhou oyster cake",
 "Lau Pa Sat":"Satay Street closes to traffic from about 7pm. Satay under the towers",
 "Uncle Chieng ice cream":"Ice cream block in a wafer or a slice of bread, around S$2. A cart, so it moves along Orchard Road",
 "Takashimaya / Ngee Ann City":"Basement food hall. Uncle Chieng's ice cream cart is usually close by",
 "Amoy Street Food Centre":"J2 Famous Crispy Curry Puff #01-21, Mon to Fri 8am to 3pm only. Five minutes from Maxwell",
 "Heap Seng Leong":"1970s kopitiam on North Bridge Road. Kopi gu you, butter coffee. The curry puff stall next door from your video. Check it is open on Deepavali",
 "Golden Mile Food Centre":"Char siu. The $10 four combo roast meat sets are this kind of stall",
}
for p in places:
    if p['label'] in NOTES: p['note']=NOTES[p['label']]

DAYS=[
 {"d":1,"date":"Mon 2 Nov","title":"Land, Jewel, then Hillview","area":"Changi Airport and Jewel","badge":"Arrival",
  "how":"You land in the evening. Jewel is linked to the terminals; taxi to Hillview after, about 35 min",
  "stops":["Jewel Changi Airport","Hillview MRT"],
  "also":[],
  "tip":"Your flight most likely lands at Terminal 2; confirm in the airline's app on the day. With the automated lanes, aim to be out with your bags by about 20:45, then walk the link bridge to Jewel, about 10 minutes. The Rain Vortex light show runs at 8pm and 9pm on Mondays, so the 9pm show is catchable if the bags come quickly, and the waterfall runs until 10pm. Leave the big bags at the 24-hour Smarte Carte counter (about S$11 to S$16 a bag). Supper in Jewel: Devil Chicken in Basement 2 closes at 9:30pm, so go there first; Tokyo Milk Cheese Factory is next to it, and the Food Republic food court runs until 11pm. Then a taxi to Hillview, leaving before midnight to avoid the 50 percent midnight surcharge."},
 {"d":2,"date":"Tue 3 Nov","title":"Tiong Bahru, Chinatown and the Esplanade","area":"Tiong Bahru, Chinatown, Marina Bay",
  "how":"Downtown Line to Chinatown, about 35 min. Outram Park for Tiong Bahru",
  "stops":["Tiong Bahru Market","Tiong Bahru Estate","Amoy Street Food Centre","Maxwell Food Centre","Ann Siang Road","Buddha Tooth Relic Temple","Sri Mariamman Temple","Chinatown Complex Food Centre","Apple Marina Bay Sands","Esplanade Theatres on the Bay","Lau Pa Sat"],
  "also":["Pretty Good Muffins","Rise Bakehouse","Dome Bakery","Tanglin Crispy Curry Puff","Bee Cheng Hiang","Hawker Chan","Food Playground","Blair Road","Tanjong Pagar Railway Station"],
  "tip":"Tiong Bahru Market when the chicken rice stall opens at 10am, then a walk through the 1930s estate. Go on to Amoy Street before lunch: J2's curry puffs sell out early and the stall is shut at weekends. Then Maxwell, five minutes away: Tian Tian chicken rice (Ah Tai is closed on Tuesdays), rojak, popiah, cockles, oyster cake and Old Nyonya laksa. Kokuyo stationery on Ann Siang Road. Temples need shoulders and knees covered. Chinatown Complex for Ann Chin Popiah, Old Amoy Chendol and CMY satay, with your bakeries close by: Pretty Good Muffins in Hong Lim (until 3:30pm), Rise Bakehouse and Dome Bakery on South Bridge Road. Then the iPhone at Apple Marina Bay Sands: keep the box sealed until the GST refund at Changi. The free Soundtracks performance at the Esplanade is at 6:45pm or 7:45pm, then Satay Street at Lau Pa Sat. The Food Playground cooking class on Sago Street (9:30 to 12:30, about S$120 each) can replace the Tiong Bahru morning."},
 {"d":3,"date":"Wed 4 Nov","title":"Botanic Gardens to the Southern Ridges","area":"Botanic Gardens, NUS, Southern Ridges, Alexandra",
  "how":"Downtown Line to Botanic Gardens, then five stops on the Circle Line to Kent Ridge",
  "stops":["Singapore Botanic Gardens","National Orchid Garden","NUS Frontier canteen","Kent Ridge Park","HortPark","Henderson Waves","Keng Eng Kee"],
  "also":["Hundred Grains","Dempsey Hill","Candlenut","Mount Faber Park","Singapore Indoor Stadium"],
  "tip":"Botanic Gardens from 7am while it is cool; the Orchid Garden opens at 8:30am (S$15 each). Circle Line to Kent Ridge for lunch at the NUS Frontier canteen: it is late term, so go before noon or after 1:30pm and carry a card as well as cash. Rest, then walk the Southern Ridges in the late afternoon: Kent Ridge Park to HortPark (1.4 km) and on over Henderson Waves (1.6 km), which lights up at 7pm. Part of the Forest Walk east of Alexandra Arch was closed for slope repairs with no reopening notice found, so check NParks first; if it is still shut, walk along Alexandra Road or take a short taxi to Henderson Waves. Then down to Alexandra Village: Lina Confectionery closes at 8pm, so buy the kueh first, then chilli crab at Keng Eng Kee, your crab dinner (book ahead, about S$100 a kilo). LANY plays the Indoor Stadium tonight if you would rather; resold tickets are not honoured."},
 {"d":4,"date":"Thu 5 Nov","title":"Wetlands, wildlife and Orchard by night","area":"Sungei Buloh, Mandai, Orchard Road",
  "how":"Bus 925 from Kranji, Mandai shuttle from Khatib, then the North South Line to Orchard",
  "stops":["Sungei Buloh Wetland Reserve","Singapore Zoo","Takashimaya / Ngee Ann City","City Bakery","Sun with Moon","Emerald Hill"],
  "also":["Apple Orchard Road","Uncle Chieng ice cream","ION Orchard","Night Safari","Newton Food Centre"],
  "tip":"Sungei Buloh at 7am for the migratory birds; there is no guided walk on a Thursday. Then the North South Line from Kranji five stops to Khatib and the M2 Mandai shuttle (S$2.50) to the Zoo for late morning (S$49 each), three to four hours. From Khatib the North South Line runs straight to Orchard, eight stops, for an evening indoors: the Takashimaya food hall, City Bakery in Mandarin Gallery, dinner at Sun with Moon in Wheelock Place (book), and a walk up Emerald Hill's Peranakan terraces. Uncle Chieng's ice cream cart is usually outside Takashimaya from about 1pm to 10pm, and Apple Orchard Road is the iPhone backup. If you choose the Night Safari instead (S$58 each), skip Orchard and budget a taxi home. A long day: carry water and an N95 in case of haze."},
 {"d":5,"date":"Fri 6 Nov","title":"Paya Lebar, Katong and the East Coast","area":"Joo Chiat, Katong, East Coast Park, Old Airport Road",
  "how":"Change at Botanic Gardens to the Circle Line for Paya Lebar, about 45 min",
  "stops":["Keng Wah Sung","Joo Chiat Road","Koon Seng Road","328 Katong Laksa","GoCycling C4 bike hire","East Coast Park","Old Airport Road Food Centre"],
  "also":["Birds of Paradise (Katong)","Sushidan (Parkway Parade)"],
  "tip":"Breakfast at Keng Wah Sung, a 70-year-old kopitiam near Paya Lebar. Walk south down Joo Chiat Road to the Peranakan terraces on Koon Seng Road, then Katong laksa for lunch. Sit out the heat at Parkway Parade (Sushidan is there), then walk through the underpass to East Coast Park and hire bikes at GoCycling C4 for the late afternoon: S$10 an hour, S$50 cash deposit. Dinner at Old Airport Road: Aunty Oats Pancake and Hougang Otah. The Singapore Symphony Orchestra plays Sibelius and Wagner at the Esplanade at 7:30pm (S$15 to S$100) if you want a concert instead."},
 {"d":6,"date":"Sat 7 Nov","title":"Telok Ayer to Marina Bay","area":"Telok Ayer, Fort Canning, Marina Bay",
  "how":"Downtown Line direct to Telok Ayer, about 40 min",
  "stops":["Ya Kun Kaya Toast","Thian Hock Keng Temple","Fort Canning Park","Hwa Kee Chicken Rice","National Gallery Singapore","Merlion Park","Marina Bay Sands","Gardens by the Bay"],
  "also":["Fort Canning walking tour","Singapore Chinese Cultural Centre","Chick-fil-A","Sushidan (Raffles City)","Clarke Quay","Funan","Victoria Theatre & Concert Hall"],
  "tip":"Kaya toast at Ya Kun, Far East Square, from about 8:30am, and Thian Hock Keng across the road. Two stops to Fort Canning while it is cool; or swap the temple for the Saturday 9:30am Fort Canning and Battlebox walking tour from Fort Canning Centre (about S$40 each, book ahead). Lunch at Hwa Kee in Peninsula Shopping Centre, then the National Gallery (S$20 each) for the hot afternoon and the best sketching spot on your list. Walk the bay past the Merlion to Gardens by the Bay: both domes are open today (S$46 each) and Garden Rhapsody runs at 7:45pm and 8:45pm. Nothing is free at the Esplanade tonight; CATS plays Sands Theatre at 8pm (S$68 to S$238). The Clay Festival at the Chinese Cultural Centre has drop-in workshops from S$10, and GV Funan, inside Funan, is the cinema for the movie. Chick-fil-A at Bugis+ is open today but closed tomorrow."},
 {"d":7,"date":"Sun 8 Nov","title":"Kampong, Kampong Glam and Bugis","area":"Buangkok, then Kampong Glam","badge":"Deepavali",
  "how":"North East Line to Buangkok, then down to Bugis",
  "stops":["Kampong Lorong Buangkok","Golden Mile Food Centre","Sultan Mosque","Arab Street","Tarik","Haji Lane","Heap Seng Leong","Bugis Street","Geylang Claypot Rice"],
  "also":["Little India"],
  "tip":"Morning at Kampong Lorong Buangkok, quiet on a Sunday: it is about 1.7 km from Buangkok MRT, so walk 25 minutes or take a short taxi. People live there, so keep to the lane, keep voices down and do not photograph the homes. Lunch at Golden Mile: the char siu stall runs 10:30am to 2pm or until it sells out. Then Kampong Glam: the Sultan Mosque admits visitors outside prayer times, from about 2pm, and lends robes. Tarik on Arab Street for saffron teh tarik, and Heap Seng Leong for kopi gu you, but confirm it opens on Deepavali. Geylang Claypot Rice on Beach Road for dinner; Hjh Maimunah is closed on Sundays. Keepsakes: a copy of The Straits Times from any 7-Eleven, and a few crisp notes and coins set aside. Little India is two stops from Bugis and lit from 7pm, if you change your minds. Early night: your taxi leaves at about 04:30."},
 {"d":8,"date":"Mon 9 Nov","title":"Fly home","area":"Hillview to Changi Terminal 3","badge":"Public holiday",
  "how":"Pre-booked taxi at 04:30 to 04:45, roughly 35 min",
  "stops":["Changi Airport Terminal 3"],
  "also":[],
  "tip":"Your flight leaves early in the morning and check-in closes 40 minutes before departure. Trains start too late on a public holiday, so book a ComfortDelGro taxi the evening before. Expect about S$60 with the pre-6am surcharge and booking fee; check Grab's fare as a backup. For a GST refund on goods in your checked bag, use the kiosk before check-in. Ya Kun and Kopitiam in Basement 2 are open 24 hours; Singapore Food Street, airside, opens at 6am."},
]
SPARE={"title":"Spare and swaps","tip":"On your doorstep: The Rail Mall and HillV2 for food and groceries (Springleaf Prata Place there runs 24 hours), and for any early morning before the heat, Dairy Farm, Singapore Quarry, Bukit Timah, Chestnut, and the Rail Corridor from Hillview Exit B. If a day falls through, a Changi swap day: Changi Village nasi lemak, the bumboat to Pulau Ubin (S$4 each way, cash), and the Changi Chapel and Museum. For the fancy dinner beyond Keng Eng Kee: Candlenut (Michelin-starred Peranakan, Dempsey), Kou Teppan omakase at Great World, or Hill Street Tai Hwa for a starred hawker bowl. Baba House is closed for restoration this year."}

WXNOTE={
 1:"You land in the evening, inside the usual evening storm window. Storms can hold arrivals for a short while; the taxi rank is under cover.",
 2:"Mornings are usually the driest part of the day, which suits Tiong Bahru and Maxwell. Storms tend to build in the late afternoon, when you are resting. The Esplanade Concourse is indoors; if Satay Street is wet, eat inside the Lau Pa Sat pavilion.",
 3:"The Southern Ridges are the most exposed walk of the week. If thunder starts, shelter at HortPark or go straight down to Keng Eng Kee; Henderson Waves stays lit until 2am, so you can still see it after the rain.",
 4:"Sungei Buloh at 7am is the coolest and usually driest slot of the day. The Zoo has covered walkways and Orchard is indoors in the evening, so this day copes well with a late storm.",
 5:"Ride East Coast Park in the late afternoon but aim to be off the bikes by about 5:30pm, ahead of the usual storm window. If there is lightning, leave the open path for a shelter.",
 6:"Fort Canning and the bay walk are outdoors; the National Gallery and the two domes are not. Garden Rhapsody can pause for lightning, so treat the 8:45pm show as the backup.",
 7:"The kampong morning is your best dry window. If an evening storm comes in, the covered five-foot ways of Kampong Glam and Bugis Street give shelter.",
 8:"A 04:30 taxi to Terminal 3. Storms at that hour are uncommon, but leave ten minutes spare in case of wet roads.",
}
for _D in DAYS: _D['wx']=WXNOTE.get(_D['d'],'')
assign={}
for D in DAYS:
    for i,l in enumerate(D['stops']): assign[l]=(D['d'],i,False)
    for i,l in enumerate(D['also']): assign[l]=(D['d'],100+i,True)
missing=[l for D in DAYS for l in D['stops']+D['also'] if l not in {p['label'] for p in places}]
assert not missing, missing

SPECIAL={'Jewel Changi Airport':("2 changes via Bugis and Tanah Merah",60),
 'Changi Chapel & Museum':("2 changes, then a bus",75),'Singapore Zoo':("Downtown Line to Newton, North South Line to Khatib, then the M2 Mandai shuttle",70),
 'Night Safari':("Downtown Line to Newton, North South Line to Khatib, then the M2 Mandai shuttle",70),'Sungei Buloh Wetland Reserve':("Bus 925 from Kranji, or a short taxi",45),
 'East Coast Park':("Change at Bugis, then bus 16 or a 12 min walk",55),'Pulau Ubin':("To Changi Village, then a bumboat",90),
 'Changi Village':("2 changes, then bus 2 from Tanah Merah",75),'Changi Village Hawker Centre':("2 changes, then bus 2 from Tanah Merah",75)}
for pl in places:
    d=assign.get(pl['label'])
    pl['day'],pl['ord'],pl['opt']=(d if d else (0,999,False))
    if pl['label'] in SPECIAL:
        pl['route'],m=SPECIAL[pl['label']]; pl['time']=f"about {m} min"; pl['near']=''; pl['walk']=0; continue
    opts=[]
    for s in stations.values():
        km=hav(pl['lat'],pl['lon'],s['lat'],s['lon'])
        if km>1.6: continue
        r=ride(s['codes'])
        if r: opts.append((r[0]+km*WALK,s,r,km))
    if not opts: pl['route'],pl['time'],pl['near'],pl['walk']="Bus or taxi from the nearest station","",'',0; continue
    tot,s,r,km=min(opts,key=lambda t:t[0])
    pl['near']=s['n']; pl['nearCodes']=s['codes']; pl['walk']=int(round(km*WALK))
    pl['route']="Direct, no change" if r[1]==0 else f"1 change at {r[2]}"
    pl['time']=f"about {int(round(tot/5.0)*5)} min"

# per-place hours, prices and booking advice extracted from the research notes, when present
import os
_det=json.load(open('places_detail.json')) if os.path.exists('places_detail.json') else {}
for pl in places:
    d=_det.get(pl['label'])
    if d: pl['det']={k:v for k,v in d.items() if v and k!='confidence'}
print('places with detail:', sum(1 for p in places if p.get('det')))
H=stations['Hillview']
json.dump({'stations':list(stations.values()),'polys':polys,
  'lines':{k:{'name':v[0],'colour':v[1]} for k,v in LINES.items()},
  'places':places,'days':DAYS,'spare':SPARE,'hill':{'lat':H['lat'],'lon':H['lon']}},open("mapdata.json","w"))
import collections
print("places:",len(places),"| per day:",dict(sorted(collections.Counter(p['day'] for p in places).items())))

# assemble the single-file page next to this folder
import os
_here=os.path.dirname(os.path.abspath(__file__))
_tpl=open(os.path.join(_here,'tpl.html')).read()
_out=_tpl.replace('__DATA__', open(os.path.join(_here,'mapdata.json')).read()).replace('__BASE__', open(os.path.join(_here,'basemap.json')).read()).replace('__WX__', open(os.path.join(_here,'weather.json')).read())
assert '__DATA__' not in _out and '__BASE__' not in _out and '__WX__' not in _out
open(os.path.join(_here,'..','singapore-2026-map.html'),'w').write(_out)
print('wrote singapore-2026-map.html', len(_out))
