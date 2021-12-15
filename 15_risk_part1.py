#!/usr/bin/env python3

from common import *
from collections import defaultdict

data = read_input(15)

G = defaultdict(list)
start = 0
end = len(data[0])-1+1j*(len(data)-1)
print(end)

for y in range(len(data)):
    for x in range(len(data[y])):
        if x < len(data[y])-1: G[x+1j*y].append([x+1+1j*y,int(data[y][x+1])])
        if y < len(data)-1: G[x+1j*y].append([x+1j*(y+1),int(data[y+1][x])])
        if x < len(data[y])-1: G[x+1+1j*y].append([x+1j*y,int(data[y][x])])
        if y < len(data)-1: G[x+1j*(y+1)].append([x+1j*y,int(data[y][x])])

if end in G: print('pouet')
for n in G: G[n].sort(key=lambda x:x[1])

new = [start]
distance = {start:0}
while new:
    n=new.pop(0)
    l=distance[n]
    for n1,d1 in G[n]:
        ll = l+d1
        if not n1 in distance or ll < distance[n1]:
            if n1 == end: print(f"found {ll}")
            distance[n1]=ll
            new.append(n1)
        else: continue

if end in distance: print(distance[end])
