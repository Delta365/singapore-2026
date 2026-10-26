"""Fetch the Open-Meteo daily forecast for the trip dates plus a 10-year climate baseline into weather.json.
Rerun closer to the trip: python3 -I fetch_weather.py && python3 -I build.py"""
import json, subprocess, statistics, collections, datetime
LAT, LON = 1.3521, 103.8198
START, END = "2026-11-02", "2026-11-09"
def get(url):
    return json.loads(subprocess.run(["curl", "-s", "-m", "60", url], capture_output=True, text=True).stdout)
fc = get("https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&timezone=Asia%%2FSingapore&start_date=%s&end_date=%s"
         "&daily=weather_code,temperature_2m_max,temperature_2m_min,apparent_temperature_max,precipitation_sum,precipitation_hours,"
         "precipitation_probability_max,uv_index_max,sunrise,sunset,wind_speed_10m_max&hourly=precipitation_probability,relative_humidity_2m"
         % (LAT, LON, START, END))
cl = get("https://archive-api.open-meteo.com/v1/archive?latitude=%s&longitude=%s&timezone=Asia%%2FSingapore"
         "&start_date=2016-11-01&end_date=2025-11-10&daily=temperature_2m_max,temperature_2m_min,precipitation_sum" % (LAT, LON))
clim = collections.defaultdict(list)
c = cl["daily"]
for t, mx, mn, pr in zip(c["time"], c["temperature_2m_max"], c["temperature_2m_min"], c["precipitation_sum"]):
    clim[t[5:]].append((mx, mn, pr))
d, h = fc["daily"], fc["hourly"]
days = []
for i, date in enumerate(d["time"]):
    hp = {t[11:13]: (p, rh) for t, p, rh in zip(h["time"], h["precipitation_probability"], h["relative_humidity_2m"]) if t.startswith(date)}
    band = lambda a, b: max((hp[f"{x:02d}"][0] or 0) for x in range(a, b) if f"{x:02d}" in hp)
    peak = max(range(6, 24), key=lambda x: (hp.get(f"{x:02d}", (0, 0))[0] or 0))
    v = clim.get(date[5:], [])
    days.append({
        "date": date, "code": d["weather_code"][i], "tmax": d["temperature_2m_max"][i], "tmin": d["temperature_2m_min"][i],
        "feels": d["apparent_temperature_max"][i], "rain": d["precipitation_sum"][i], "rainHours": d["precipitation_hours"][i],
        "prob": d["precipitation_probability_max"][i], "uv": d["uv_index_max"][i], "wind": d["wind_speed_10m_max"][i],
        "sunrise": d["sunrise"][i][11:], "sunset": d["sunset"][i][11:],
        "humidity": round(statistics.mean(rh for _, rh in hp.values() if rh is not None)),
        "bands": {"morning": band(6, 12), "afternoon": band(12, 18), "evening": band(18, 24)}, "peakHour": peak,
        "clim": {"tmax": round(statistics.mean(x[0] for x in v), 1), "tmin": round(statistics.mean(x[1] for x in v), 1),
                 "rain": round(statistics.mean(x[2] for x in v), 1), "wetYears": sum(1 for x in v if x[2] >= 1), "years": len(v)} if v else None,
    })
# ---- haze: model PM2.5 converted to a PSI estimate on NEA's 24-hour PM2.5 bands ----
BANDS = [(0, 12, 0, 50), (12, 55, 50, 100), (55, 150, 100, 200), (150, 250, 200, 300), (250, 350, 300, 400), (350, 500, 400, 500)]
def psi(pm):
    for lo, hi, plo, phi in BANDS:
        if pm <= hi:
            return round(plo + (pm - lo) / (hi - lo) * (phi - plo))
    return 500
def daily_pm(url, min_hours=18):
    h = get(url).get("hourly", {})
    by = collections.defaultdict(list)
    for t, v in zip(h.get("time", []), h.get("pm2_5", [])):
        if v is not None:
            by[t[:10]].append(v)
    return {k: statistics.mean(v) for k, v in by.items() if len(v) >= min_hours}
AQ = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=%s&longitude=%s&timezone=Asia%%2FSingapore&hourly=pm2_5" % (LAT, LON)
now_pm = daily_pm(AQ + "&past_days=3&forecast_days=7")
today = datetime.date.today().isoformat()
for day in days:
    pm = now_pm.get(day["date"])
    day["haze"] = {"pm25": round(pm, 1), "psi": psi(pm)} if pm is not None else None
    yrs = []
    for y in range(2022, 2026):
        v = daily_pm(AQ + "&start_date=%d%s&end_date=%d%s" % (y, day["date"][4:], y, day["date"][4:]))
        if v: yrs.append(psi(list(v.values())[0]))
    day["hazeTypical"] = {"psi": round(statistics.mean(yrs)), "worst": max(yrs), "years": len(yrs)} if yrs else None
haze_now = {"asOf": today, "days": [{"date": k, "psi": psi(v)} for k, v in sorted(now_pm.items()) if k >= today]}

out = {"fetched": datetime.date.today().isoformat(), "hazeNow": haze_now, "source": "Open-Meteo forecast and ERA5 archive (2016 to 2025)",
       "lat": LAT, "lon": LON, "days": days}
json.dump(out, open("weather.json", "w"), indent=1)
print("weather.json:", len(days), "days, fetched", out["fetched"])
