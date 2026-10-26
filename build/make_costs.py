import json
import sys

ROOT = "/Users/sanjivanrane/Desktop/claude/Singapore 2026"
SHOP = "browse; purchases not counted"

# label: (pp, kind, basis, confidence)
C = {
    # Day 1
    "Hillview MRT": (0, "free", "Home base station; fares are in the daily transport line", "high"),
    "Jewel Changi Airport": (18, "food", "Supper for one at Devil Chicken or Food Republic, est.; bag storage S$11-16 a bag extra", "medium"),

    # Day 2 main
    "Tiong Bahru Market": (9, "food", "Chicken rice (S$4.50-6 in 2026), shui kueh and kopi, est.", "medium"),
    "Tiong Bahru Estate": (0, "free", "Self-guided walk through the 1930s SIT blocks", "high"),
    "Amoy Street Food Centre": (4, "food", "Two J2 curry puffs at about S$1.40-2 each, est. 2026 price", "medium"),
    "Maxwell Food Centre": (15, "food", "Tian Tian chicken rice plus shared rojak, popiah, oyster cake, laksa, drink; est.", "medium"),
    "Ann Siang Road": (0, "shopping", SHOP, "high"),
    "Buddha Tooth Relic Temple": (0, "free", "Free; donations welcome", "high"),
    "Sri Mariamman Temple": (0, "free", "Free entry; no fee found in the notes", "medium"),
    "Chinatown Complex Food Centre": (9, "food", "Ann Chin popiah, Old Amoy chendol (S$2.80) and five CMY satay sticks, est.", "medium"),
    "Apple Marina Bay Sands": (0, "excluded", "iPhone purchase excluded from the trip cost", "high"),
    "Esplanade Theatres on the Bay": (0, "free", "Free Soundtracks show on the Concourse, Tue 3 Nov at 6:45pm or 7:45pm", "high"),
    "Lau Pa Sat": (19, "food", "Half of Best Satay Set A (S$31.20) plus a drink; budget S$38 for two", "high"),
    # Day 2 options
    "Tanjong Pagar Railway Station": (0, "free", "Facade seen from outside; not open to visitors", "high"),
    "Blair Road": (0, "free", "Street walk past conservation shophouses", "high"),
    "Hawker Chan": (7, "food", "Soy sauce chicken rice about S$6.80 (outlet and date unclear)", "medium"),
    "Food Playground": (120, "activity", "Cooking class, S$120 nett each for two or more (own page, valid to Jun 2027)", "high"),
    "Tanglin Crispy Curry Puff": (4, "food", "Two curry puffs at about S$2 each (undated)", "medium"),
    "Bee Cheng Hiang": (0, "shopping", SHOP, "high"),
    "Pretty Good Muffins": (8, "food", "One muffin (S$1.40-4.50) and a matcha latte (S$5-6), Jun 2026 prices", "medium"),
    "Rise Bakehouse": (9, "food", "One teacake or cake slice, S$8.20-9.20 (Apr 2025 prices)", "medium"),
    "Dome Bakery": (6, "food", "One fudge-filled brownie, S$6-6.80 (Apr 2023 prices)", "medium"),

    # Day 3 main
    "Singapore Botanic Gardens": (0, "free", "Free; only the National Orchid Garden is ticketed", "high"),
    "National Orchid Garden": (15, "ticket", "Standard (non-local) adult; no need to prebook", "high"),
    "NUS Frontier canteen": (6, "food", "One dish (S$2.30-5.90, Oct 2025) and a drink, est.; guide S$12 for two", "medium"),
    "Kent Ridge Park": (0, "free", "Free park and Canopy Walk", "high"),
    "HortPark": (0, "free", "Free gardens on the Southern Ridges", "high"),
    "Henderson Waves": (0, "free", "Free; lit 7pm to 2am", "high"),
    "Keng Eng Kee": (75, "food", "Chilli crab (~1 kg at ~S$100/kg) for two, mantou, rice, a vegetable, incl. ++", "medium"),
    # Day 3 options
    "Hundred Grains": (12, "food", "About 300 g at S$3.98 per 100 g; rice and drinks free-flow (Oct 2023), est.", "medium"),
    "Dempsey Hill": (0, "free", "Walk among the black-and-white buildings; cafe spend not counted", "high"),
    "Candlenut": (81, "food", "Tasting menu S$65-70++ (dated) with service and GST, no drinks; S$118++ menu is S$141", "low"),
    "Mount Faber Park": (0, "free", "Free park at the eastern end of the Southern Ridges", "high"),
    "Singapore Indoor Stadium": (140, "ticket", "LANY: budget S$190-370 for two incl. fees; face value from S$138", "low"),

    # Day 4 main
    "Sungei Buloh Wetland Reserve": (0, "free", "Treated as free; no 2026 entry fee found in the notes", "medium"),
    "Singapore Zoo": (49, "ticket", "Non-resident adult, weekday; lunch in the park (budget S$22.50 each) not counted", "high"),
    "Takashimaya / Ngee Ann City": (8, "food", "Snack at the B2 food hall, est.; budget S$15 for two", "low"),
    "City Bakery": (5, "food", "Pretzel croissant S$5 (Aug 2026)", "high"),
    "Sun with Moon": (45, "food", "Kamameshi set, a shared side and tea, with ++, est.; no price in the notes", "low"),
    "Emerald Hill": (0, "free", "Free walk past the Peranakan terraces", "high"),
    # Day 4 options
    "Newton Food Centre": (20, "food", "Dinner without crab, about S$20 each (budget estimate)", "medium"),
    "ION Orchard": (7, "food", "LiXin fishball noodles at Food Opera B4, est.; mall browsing not counted", "low"),
    "Night Safari": (58, "ticket", "Non-resident adult, regular night (Thu); late taxi home not in Day 4 transport", "high"),
    "Uncle Chieng ice cream": (2, "food", "Ice cream in wafer or bread, about S$1.50-2", "medium"),

    # Day 5 main
    "Keng Wah Sung": (6, "food", "Kaya toast set with kopi and a sugar doughnut, est.; budget S$12 for two", "medium"),
    "Joo Chiat Road": (0, "free", "Street walk; Eurasian Heritage Gallery (S$5) not counted", "high"),
    "Koon Seng Road": (0, "free", "Free street of Peranakan terraces", "high"),
    "328 Katong Laksa": (8, "food", "Large laksa S$7.50-8.30 (small S$6.30); budget S$15 for two", "medium"),
    "GoCycling C4 bike hire": (20, "activity", "Two hours at S$10 an hour; S$50 cash deposit refunded", "high"),
    "East Coast Park": (0, "free", "Free park; bike hire listed separately", "high"),
    "Old Airport Road Food Centre": (13, "food", "Oats pancakes, otah nasi lemak, small Nam Sing Hokkien mee (S$5), drink; est.", "medium"),
    # Day 5 options
    "Sushidan (Parkway Parade)": (24, "food", "About eight pieces from S$1.99++ or the S$19.90++ omakase, with ++, est.", "medium"),
    "Birds of Paradise (Katong)": (6, "food", "Single scoop in a thyme cone, about S$6; budget S$13 for two", "medium"),

    # Day 6 main
    "Ya Kun Kaya Toast": (6, "food", "Kaya toast set (toast, two eggs, kopi), about S$6.20 in 2026", "high"),
    "Thian Hock Keng Temple": (0, "free", "Free entry; dress modestly", "high"),
    "Fort Canning Park": (0, "free", "Park and Tree Tunnel free; Battlebox (S$20) not counted", "high"),
    "Hwa Kee Chicken Rice": (10, "food", "Half of the S$20 lemon and steamed chicken set for two (Feb 2024)", "medium"),
    "National Gallery Singapore": (20, "ticket", "General admission, other nationalities", "high"),
    "Merlion Park": (0, "free", "Free waterfront park", "high"),
    "Marina Bay Sands": (0, "free", "Bayfront promenade free; CATS (S$68-238) not counted", "high"),
    "Gardens by the Bay": (46, "ticket", "Flower Dome plus Cloud Forest, non-resident adult; Garden Rhapsody free", "high"),
    # Day 6 options
    "Clarke Quay": (0, "free", "Riverside walk free; river cruise (about S$25-28) not counted", "medium"),
    "Funan": (19, "activity", "GV Funan movie: S$16 standard on Sat, more for Deluxe Plus; budget S$32-45 for two", "medium"),
    "Victoria Theatre & Concert Hall": (40, "ticket", "Classic Memories S$35-45 (SISTIC), Fri 6 Nov only; nothing listed Sat", "medium"),
    "Singapore Chinese Cultural Centre": (10, "activity", "Clay Festival drop-in workshop from S$10", "medium"),
    "Chick-fil-A": (12, "food", "Chicken sandwich meal, est. from chain meal prices in the notes", "low"),
    "Sushidan (Raffles City)": (24, "food", "About eight pieces from S$1.99++ or the S$19.90++ omakase, with ++, est.", "medium"),
    "Fort Canning walking tour": (40, "activity", "Sat 9:30am Fort Canning and Battlebox walk, about S$40 each", "high"),

    # Day 7 main
    "Kampong Lorong Buangkok": (0, "free", "Quiet walk along the shared lane; free", "high"),
    "Golden Mile Food Centre": (11, "food", "Chef Lup three-meat rice S$8.80 (Sep 2025) or the S$10 set, plus a drink", "medium"),
    "Sultan Mosque": (0, "free", "Free; robes lent at the counter", "high"),
    "Arab Street": (0, "free", "Street walk; textile and rug shopping not counted", "high"),
    "Tarik": (3, "food", "Saffron teh tarik, S$2 on an older listing; est. 2026 price", "medium"),
    "Haji Lane": (0, "free", "Free lane of murals and small shops", "high"),
    "Heap Seng Leong": (5, "food", "Kopi gu you and kaya-butter toast (budget S$4) plus a curry puff, est.", "medium"),
    "Bugis Street": (0, "shopping", SHOP, "high"),
    "Geylang Claypot Rice": (22, "food", "Claypot rice for two, a vegetable and drinks, est.; no price in the notes", "low"),
    # Day 7 option
    "Little India": (0, "free", "Deepavali light-up and streets, free", "high"),

    # Day 8
    "Changi Airport Terminal 3": (10, "food", "Breakfast and coffee at Ya Kun B2 or Food Street, est.; taxi is in Day 8", "medium"),

    # Spare
    "Chinatown": (0, "free", "Streets and temples free; Chinatown Heritage Centre (about S$25) not counted", "high"),
    "Changi Village": (0, "free", "Village and coastal walk free; food and bumboat listed separately", "high"),
    "Baba House": (0, "excluded", "Closed for restoration until 2027 at the earliest; not costed", "high"),
    "Rochester Park": (0, "free", "Free walk past the colonial bungalows", "high"),
    "VivoCity": (0, "shopping", SHOP, "high"),
    "The Rail Mall": (10, "food", "Supper such as prata at Springleaf, est.; budget S$20 for two", "medium"),
    "HillV2": (0, "shopping", SHOP, "high"),
    "Dairy Farm Nature Park": (0, "free", "Free nature park", "high"),
    "Bukit Timah Nature Reserve": (0, "free", "Free nature reserve", "high"),
    "Singapore Quarry": (0, "free", "Free, inside Dairy Farm Nature Park", "high"),
    "Chestnut Nature Park": (0, "free", "Free trails", "high"),
    "Bukit Batok Town Park": (0, "free", "Free park and quarry viewpoint", "high"),
    "Bukit Timah Railway Station": (0, "free", "Station and Rail Corridor free; cafe not counted", "high"),
    "Former Ford Factory": (6, "ticket", "Visitor admission not in the notes; est. small museum fee", "low"),
    "Changi Chapel & Museum": (10, "ticket", "S$9 adult plus GST (S$9.81), cashless only", "medium"),
    "Changi Village Hawker Centre": (8, "food", "Nasi lemak with chicken and a drink, est.; no price in the notes", "low"),
    "Pulau Ubin": (8, "activity", "Bumboat S$4 each way, cash; island bike hire not priced in the notes", "medium"),
    "Hill Street Tai Hwa Pork Noodle": (10, "food", "Bak chor mee bowl, est.; no price in the notes", "low"),
    "Hjh Maimunah": (10, "food", "Nasi padang plate with two or three dishes and a drink, est.", "low"),
    "Standing Sushi Bar": (12, "food", "S$3.90 salmon deal plus a roll and tea, with ++, est.", "low"),
    "Kou Teppan": (94, "food", "Eight-course dinner omakase, S$82-105 each after ++; lunch about S$70", "medium"),
}

# Daily transport for two. Fares from the PTC table in force Nov 2026.
FEE = 0.60


def mrt(fares, extra=0.0):
    return round(2 * (sum(fares) + FEE) + extra)


T = {
    "1": (65, "Taxi Changi to Hillview at night: meter, 25% evening peak and S$8 airport surcharge; no MRT"),
    "2": (mrt([2.15, 1.28, 1.28, 2.15]),
          "4 MRT trips each (to Tiong Bahru, to Maxwell, Chinatown-Bayfront, Telok Ayer home), S$0.60 fee each"),
    "3": (mrt([1.75, 1.59, 2.02], 10),
          "3 MRT trips each (Botanic Gardens, Kent Ridge, Queenstown home), S$0.60 fee each, taxi to KEK est. S$10"),
    "4": (mrt([2.20, 2.15, 2.07, 1.94], 2 * 2 * 2.50),
          "4 MRT and bus trips each incl. bus 925, M2 shuttle S$2.50 each way each, S$0.60 fee each"),
    "5": (mrt([2.27, 1.49, 2.27]),
          "3 trips each (Paya Lebar, bus to Old Airport Road, Dakota home), S$0.60 fee each; rest on foot"),
    "6": (mrt([2.15, 1.28, 2.15]),
          "3 MRT trips each (Telok Ayer, Fort Canning, Bayfront home), S$0.60 fee each; the bay on foot"),
    "7": (mrt([2.33, 2.07, 2.07], 7),
          "3 trips each (Buangkok, Nicoll Highway, Bugis home), S$0.60 fee each, optional kampong taxi est. S$7"),
    "8": (60, "Pre-booked 04:30 taxi to T3 with 50% midnight surcharge and booking fee; no trains that early"),
}

it = json.load(open(f"{ROOT}/itinerary-current.json"))
labels = [p["label"] for p in it["places"]]
missing = [l for l in labels if l not in C]
extra = [l for l in C if l not in labels]
if missing or extra:
    sys.exit(f"missing={missing} extra={extra}")

KINDS = {"food", "ticket", "activity", "free", "shopping", "excluded"}
CONF = {"high", "medium", "low"}
bad = []
for l, (pp, kind, basis, conf) in C.items():
    if kind not in KINDS or conf not in CONF or len(basis) > 90 or not isinstance(pp, int):
        bad.append((l, len(basis)))
    if kind in ("free", "shopping", "excluded") and pp != 0:
        bad.append((l, "nonzero"))
for d, (amt, basis) in T.items():
    if len(basis) > 110:
        bad.append((d, len(basis)))
for s in [b for _, _, b, _ in C.values()] + [b for _, b in T.values()]:
    if "—" in s or "–" in s:
        bad.append(("dash", s))
if bad:
    sys.exit(f"bad={bad}")

out = {
    "currency": "SGD",
    "rate_inr": 74.10,
    "places": {l: {"pp": C[l][0], "kind": C[l][1], "basis": C[l][2], "confidence": C[l][3]} for l in labels},
    "transport": {d: {"amount": a, "basis": b} for d, (a, b) in T.items()},
}
text = json.dumps(out, ensure_ascii=False, indent=2)
text = text.replace('"rate_inr": 74.1,', '"rate_inr": 74.10,', 1)
with open(f"{ROOT}/build/places_cost.json", "w", encoding="utf-8") as f:
    f.write(text + "\n")
print("written")
