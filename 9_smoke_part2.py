#!/usr/bin/env python3

from common import read_input

data = read_input(9)

data = [ [ int(c) for c in l ] for l in data ]
X,Y=len(data[0]),len(data)

def grow_bassin(data,x,y,bassin=[]):
    queue = []
    if not len(bassin): bassin = [(x,y)]
    v = data[y][x]
    if x>0:
        x1,y1 = x-1,y
        v1 = data[y1][x1]
        if v1 > v and v1 != 9 and not (x1,y1) in bassin: queue.append((x1,y1))
    if y>0:
        x1,y1 = x,y-1
        v1 = data[y1][x1]
        if v1 > v and v1 != 9 and not (x1,y1) in bassin: queue.append((x1,y1))
    if x<X-1:
        x1,y1 = x+1,y
        v1 = data[y1][x1]
        if v1 > v and v1 != 9 and not (x1,y1) in bassin: queue.append((x1,y1))
    if y<Y-1:
        x1,y1 = x,y+1
        v1 = data[y1][x1]
        if v1 > v and v1 != 9 and not (x1,y1) in bassin: queue.append((x1,y1))
    bassin += queue
    if len(queue):
        for x1,y1 in queue: bassin = grow_bassin(data,x1,y1,bassin)
    return bassin

print(X,Y)
count = 0
bassins=[]
for y in range(Y):
    for x in range(X):
        v=data[y][x]
        m=True
        if m and x>0 and data[y][x-1] <= v: m=False
        if m and y>0 and data[y-1][x] <= v: m=False
        if m and x<X-1 and data[y][x+1] <= v: m=False
        if m and y<Y-1 and data[y+1][x] <= v: m=False
        if m:
            bassin = grow_bassin(data,x,y)
            bassins.append(bassin)
bassins.sort(key=lambda x:-len(x))
print(len(bassins[0])*len(bassins[1])*len(bassins[2]))