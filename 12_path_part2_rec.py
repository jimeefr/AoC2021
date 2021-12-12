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

def path(begin="start",end="end",visited=[],double=False):
    if begin==end:
        return [",".join(visited)]
    v = visited[::]
    v.append(begin)
    p = []
    for n in G[begin]:
        if ord(n[0]) < 97 or n not in visited:
            p += path(n,end,v,double)
        elif not double and n != "start":
            p += path(n,end,v,True)
    return p

print(len(path()))