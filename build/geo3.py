import json, subprocess, urllib.parse, time
def get(u):
    return subprocess.run(["curl","-s","-m","20","-A","Singapore2026TripMap/1.0",u],capture_output=True,text=True).stdout
def om(q):
    u="https://www.onemap.gov.sg/api/common/elastic/search?"+urllib.parse.urlencode({"searchVal":q,"returnGeom":"Y","getAddrDetails":"Y","pageNum":"1"})
    for attempt in range(3):
        try:
            r=json.loads(get(u)).get("results") or []
            if not r: return None
            t=r[0]; return float(t["LATITUDE"]),float(t["LONGITUDE"]),(t.get("ADDRESS") or "").title()
        except Exception:
            time.sleep(2+attempt*2)
    return None
def nomi(q):
    u="https://nominatim.openstreetmap.org/search?"+urllib.parse.urlencode({"q":q+", Singapore","format":"json","limit":"1","countrycodes":"sg"})
    try:
        d=json.loads(get(u))
        if d: return float(d[0]["lat"]),float(d[0]["lon"]),d[0].get("display_name","").split(", Singapore")[0]
    except Exception: pass
    return None
def geocode(*qs):
    for q in qs:
        g=om(q) or (time.sleep(1.1) or nomi(q))
        if g: return g
        time.sleep(.5)
    return None
