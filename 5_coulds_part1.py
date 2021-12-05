#!/usr/bin/env python3

from common import read_input
import re

data = read_input(5)

f = re.compile(r",| -> ")
lines = [ list(map(int,f.split(l))) for l in data ]
mx = max([l[0] for l in lines]+[l[2] for l in lines])+1
my = max([l[1] for l in lines]+[l[3] for l in lines])+1
print(mx,my)

area = []
for i in range(mx): area.append([0]*my)
for x1,y1,x2,y2 in lines:
    if x1==x2:
        if y2<y1: y1,y2=y2,y1
        for y in range(y1,y2+1): area[x1][y]+=1
    if y1==y2:
        if x2<x1: x1,x2=x2,x1
        for x in range(x1,x2+1): area[x][y1]+=1
clouds=0
for x in range(mx):
    for y in range(my):
        if area[x][y]>1: clouds += 1
print(clouds)