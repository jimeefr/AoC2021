#!/usr/bin/env python3

from common import read_input
import re

data = read_input(5)

f = re.compile(r",| -> ")
lines = [ list(map(int,f.split(l))) for l in data ]
mx = max([l[0] for l in lines]+[l[2] for l in lines])+1
my = max([l[1] for l in lines]+[l[3] for l in lines])+1
print(mx,my)

def delta(a,b):
    if b != a: return (b-a) // abs(b-a)
    return 0

area = []
for i in range(mx): area.append([0]*my)
for x1,y1,x2,y2 in lines:
    dx, dy = delta(x1,x2), delta(y1,y2)
    for i in range(max(abs(x2-x1),abs(y2-y1))+1):
        area[x1+i*dx][y1+i*dy] += 1

clouds=0
for x in range(mx):
    for y in range(my):
        if area[x][y]>1: clouds += 1
print(clouds)