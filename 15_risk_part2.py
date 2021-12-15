#!/usr/bin/env python3

from common import *
from collections import defaultdict

data = read_input(15)

G = defaultdict(list)
start = 0

ly=len(data)
lx=len(data[0])
data2 = []
for y in range(ly*5):
    s=""
    dy=y//ly
    for x in range(lx*5):
        dx=x//lx
        n = (int(data[y%ly][x%lx])-1+dx+dy)%9+1
        s += f"{n}"
    data2.append(s)

for y in range(len(data2)):
    for x in range(len(data2[y])):
        if x < len(data2[y])-1: G[x+1j*y].append([x+1+1j*y,int(data2[y][x+1])])
        if y < len(data2)-1: G[x+1j*y].append([x+1j*(y+1),int(data2[y+1][x])])
        if x < len(data2[y])-1: G[x+1+1j*y].append([x+1j*y,int(data2[y][x])])
        if y < len(data2)-1: G[x+1j*(y+1)].append([x+1j*y,int(data2[y][x])])


end = 5*lx-1+1j*(5*ly-1)
for n in G: G[n].sort(key=lambda x:x[1])

new = [start]
distance = {start:0}
while new:
    n=new.pop(0)
    l=distance[n]
    for n1,d1 in G[n]:
        ll = l+d1
        if not n1 in distance or ll < distance[n1]:
            distance[n1]=ll
            new.append(n1)
        else: continue

if end in distance: print(distance[end])
