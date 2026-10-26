import json, math, sys, collections
D='osm/'
def dp(pts, tol):
    # Douglas-Peucker on [lon,lat] lists, iterative
    if len(pts)<3: return pts
    keep=[False]*len(pts); keep[0]=keep[-1]=True
    stack=[(0,len(pts)-1)]
    while stack:
        a,b=stack.pop()
        ax,ay=pts[a]; bx,by=pts[b]; dx,dy=bx-ax,by-ay; L=dx*dx+dy*dy
        best,bi=-1,-1
        for i in range(a+1,b):
            px,py=pts[i]
            if L==0: d=(px-ax)**2+(py-ay)**2
            else:
                t=max(0,min(1,((px-ax)*dx+(py-ay)*dy)/L)); qx,qy=ax+t*dx,ay+t*dy; d=(px-qx)**2+(py-qy)**2
            if d>best: best,bi=d,i
        if best>tol*tol:
            keep[bi]=True; stack+= [(a,bi),(bi,b)]
    return [p for p,k in zip(pts,keep) if k]
def area(r):
    return abs(sum(r[i][0]*r[i+1][1]-r[i+1][0]*r[i][1] for i in range(len(r)-1)))/2
def rnd(r): return [[round(x,5),round(y,5)] for x,y in r]
def stitch(segs):
    """segs: list of coordinate lists (lon,lat). Join by matching endpoints (rounded). Returns (closed rings, open chains)."""
    key=lambda p:(round(p[0],7),round(p[1],7))
    segs=[s[:] for s in segs if len(s)>=2]
    closed=[]; chains=[]
    for s in segs:
        if key(s[0])==key(s[-1]): closed.append(s)
        else: chains.append(s)
    changed=True
    while changed:
        changed=False
        ends={}
        for i,c in enumerate(chains):
            ends.setdefault(key(c[0]),[]).append((i,'s')); ends.setdefault(key(c[-1]),[]).append((i,'e'))
        used=set(); out=[]
        for i,c in enumerate(chains):
            if i in used: continue
            used.add(i); cur=c[:]
            grow=True
            while grow:
                grow=False
                for j,side in ends.get(key(cur[-1]),[]):
                    if j in used: continue
                    o=chains[j]
                    cur+= (o[1:] if side=='s' else o[::-1][1:]); used.add(j); grow=True; changed=True; break
            out.append(cur)
        chains=out
        still=[]
        for c in chains:
            if key(c[0])==key(c[-1]): closed.append(c)
            else: still.append(c)
        chains=still
    return closed, chains
def geomways(fn):
    els=json.load(open(D+fn))['elements']; ways=[]; rels=[]
    for e in els:
        if e['type']=='way' and e.get('geometry'):
            ways.append((e.get('tags',{}),[[g['lon'],g['lat']] for g in e['geometry']]))
        elif e['type']=='relation':
            outers=[[[g['lon'],g['lat']] for g in m['geometry']] for m in e.get('members',[]) if m.get('type')=='way' and m.get('role') in ('outer','') and m.get('geometry')]
            rels.append((e.get('tags',{}),outers))
    return ways,rels

out={}
# ---- land from coastline
ways,_=geomways('coast.json')
closed,open_=stitch([g for _,g in ways])
land=[rnd(dp(r,0.00009)) for r in closed if area(r)>2e-7]
print('coast: closed rings',len(closed),'kept',len(land),'open chains',len(open_), [ (round(c[0][0],3),round(c[0][1],3),round(c[-1][0],3),round(c[-1][1],3),len(c)) for c in open_][:8])
out['coastOpen']=[rnd(dp(c,0.00012)) for c in open_ if len(c)>5]
# close the edge-cut coasts so neighbouring land fills: Johor via the north, the Riau islands via the south
north=sorted([c for c in open_ if len(c)>100 and min(p[1] for p in c)>1.3], key=lambda c:min(p[0] for p in c))
if north:
    ring=[p for c in north for p in c]
    ring+= [[max(p[0] for p in ring)+0.05,1.65],[min(p[0] for p in ring)-0.05,1.65],ring[0]]
    land.append(rnd(dp(ring,0.00009)))
for c in open_:
    if len(c)>100 and min(p[1] for p in c)<1.21:
        land.append(rnd(dp(c+[[c[-1][0],1.0],[c[0][0],1.0],c[0]],0.00009)))
out['land']=land
out['land']=land
# ---- green
ways,rels=geomways('green.json')
green=[]
def gtype(t):
    if t.get('leisure')=='nature_reserve' or t.get('boundary')=='national_park': return 'r'
    if t.get('landuse')=='forest' or t.get('natural')=='wood': return 'f'
    if t.get('leisure')=='golf_course': return 'g'
    return 'p'
for t,g in ways:
    if len(g)>3 and g[0]==g[-1] and area(g)>4e-7: green.append([gtype(t),rnd(dp(g,0.0001))])
for t,outs in rels:
    cl,_=stitch(outs)
    for r in cl:
        if area(r)>4e-7: green.append([gtype(t),rnd(dp(r,0.0001))])
out['green']=green
# ---- water
ways,rels=geomways('water.json'); water=[]
for t,g in ways:
    if len(g)>3 and g[0]==g[-1] and area(g)>3e-7: water.append(rnd(dp(g,0.00008)))
for t,outs in rels:
    cl,_=stitch(outs)
    for r in cl:
        if area(r)>3e-7: water.append(rnd(dp(r,0.00008)))
out['water']=water
# ---- roads, merged per name+class to cut segment count
ways,_=geomways('roads.json')
cls={'motorway':0,'motorway_link':0,'trunk':1,'trunk_link':1,'primary':2,'primary_link':2,'secondary':3,'secondary_link':3}
groups=collections.defaultdict(list)
for t,g in ways:
    c=cls.get(t.get('highway'))
    if c is None or t.get('highway','').endswith('_link'): continue
    groups[(c,t.get('name') or t.get('ref') or '')].append(g)
roads=[[],[],[],[]]
for (c,name),segs in groups.items():
    cl,ch=stitch(segs)
    for line in cl+ch:
        s=dp(line,0.00012 if c<3 else 0.00016)
        if len(s)>=2: roads[c].append(rnd(s))
out['roads']=roads
# ---- labels
els=json.load(open(D+'places.json'))['elements']; labels=[]; seen=set()
rank={'town':0,'suburb':1,'quarter':2,'neighbourhood':3}
for e in els:
    t=e.get('tags',{}); n=t.get('name:en') or t.get('name')
    if not n or n in seen: continue
    if not (1.2<e['lat']<1.47 and 103.6<e['lon']<104.05): continue
    if any('一'<=ch<='鿿' for ch in n): continue
    seen.add(n); labels.append([n,round(e['lat'],5),round(e['lon'],5),rank.get(t.get('place'),3)])
out['labels']=labels
s=json.dumps(out,separators=(',',':'))
open('basemap.json','w').write(s)
pts=lambda L: sum(len(r) for r in L)
print('land pts',pts(land),'green',len(green),pts([g[1] for g in green]),'water',len(water),pts(water),
      'roads',[len(r) for r in roads],[pts(r) for r in roads],'labels',len(labels),collections.Counter(l[3] for l in labels))
print('basemap.json bytes',len(s))
