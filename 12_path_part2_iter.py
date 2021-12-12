#!/usr/bin/env python3

from common import read_input

data = read_input(12)

G = {}

for l in data:
    a,b = l.split('-')
    if not a in G: G[a]=[]
    if not b in G: G[b]=[]
    G[a].append(b)
    G[b].append(a)

visited = [("start",0)]
paths = 0
nv = {"start":1}
while len(visited):
    n,i = visited.pop()
    if i == len(G[n]):
        if n in nv: nv[n] -= 1
        continue
    visited.append((n,i+1))
    nn = G[n][i]
    if nn == "end":
        paths += 1
        continue
    small = ord(nn[0])>96
    mvc = max(nv.values())
    if small and nn not in nv: nv[nn]=0
    if nn == "start" or small and nv[nn] and mvc==2: continue
    if small: nv[nn] += 1
    visited.append((nn,0))

print(paths)
