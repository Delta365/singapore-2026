"""Write ../itinerary-current.json from mapdata.json: the plan as it is built, for the guide writers.
Flight numbers and times are deliberately left out (the repository is public)."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(here, 'mapdata.json')))
keep = ['label', 'cat', 'note', 'day', 'opt', 'ord', 'near', 'route', 'time', 'walk', 'addr', 'lat', 'lon']
it = {'trip': 'Singapore, 2 to 9 November 2026, based at Hillview MRT (DT3)',
      'flights': {'in': 'Mumbai to Singapore, lands on the evening of Mon 2 Nov (terminal likely T2)',
                  'out': 'Singapore to Mumbai, departs Changi T3 early on Mon 9 Nov'},
      'days': d['days'], 'spare': d['spare'], 'places': [{k: p.get(k) for k in keep} for p in d['places']]}
json.dump(it, open(os.path.join(here, '..', 'itinerary-current.json'), 'w'), indent=1, ensure_ascii=False)
print('itinerary-current.json:', len(it['places']), 'places')
