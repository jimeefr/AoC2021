#!/usr/bin/env python3

from common import *
import re

data = read_input(22)

reg = re.compile(r"^(on|off) x=([-0-9]*)..([-0-9]*),y=([-0-9]*)..([-0-9]*),z=([-0-9]*)..([-0-9]*)$")

on = {}
for line in data:
    m = reg.match(line)
    g = m.group(1,2,3,4,5,6,7)
    x1,x2,y1,y2,z1,z2 = map(int,g[1:])
    state = g[0]
    x1 = max(x1,-50)
    y1 = max(y1,-50)
    z1 = max(z1,-50)
    x2 = min(x2,50)
    y2 = min(y2,50)
    z2 = min(z2,50)
    print(x1,x2,y1,y2,z1,z2)
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            for z in range(z1,z2+1):
                if state=='on' and (x,y,z) not in on: on[(x,y,z)]=1
                if state=='off' and (x,y,z) in on: del on[(x,y,z)]

print(len(on.keys()))
