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

visited = [("start",0,False)]
paths = 0
while len(visited):
    n,i,d = visited.pop()
    if i == len(G[n]): continue
    visited.append((n,i+1,d))
    nn = G[n][i]
    if nn == "end":
        paths += 1
        continue
    if nn == "start": continue
    if ord(nn[0])>96:
        if nn in [v[0] for v in visited]:
            if d: continue
            else: d=True
    visited.append((nn,0,d))

print(paths)
