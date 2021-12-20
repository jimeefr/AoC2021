#!/usr/bin/env python3

from common import *
from collections import defaultdict

data = read_input(19)

def rotate(p):
    x,y,z = p
    return [
        (x,y,z),
        (x,z,-y),
        (x,-y,-z),
        (x,-z,y),
        (-x,-y,z),
        (-x,z,y),
        (-x,y,-z),
        (-x,-z,-y),
        (y,-x,z),
        (y,z,x),
        (y,x,-z),
        (y,-z,-x),
        (-y,x,z),
        (-y,z,-x),
        (-y,-x,-z),
        (-y,-z,x),
        (z,x,y),
        (z,y,-x),
        (z,-x,-y),
        (z,-y,x),
        (-z,-x,y),
        (-z,y,x),
        (-z,x,-y),
        (-z,-y,-x)
        ]

def rotate_scanner(s):
    t = []
    for _ in range(24): t.append([])
    for p in s:
        for i in range(24): 
            r = rotate(p)
            t[i].append(r[i])
    return t

def comp_scanners(s1,s2):
    d = defaultdict(int)
    for i in range(len(s2)):
        for j in range(len(s1)):
            Dx = s1[j][0] - s2[i][0]
            Dy = s1[j][1] - s2[i][1]
            Dz = s1[j][2] - s2[i][2]
            d[(Dx,Dy,Dz)] += 1
            if d[(Dx,Dy,Dz)] == 12: return (Dx,Dy,Dz)
    return None

def comp_rotated_scanners(s1,s2):
    rs = rotate_scanner(s2)
    for i in range(24):
        r = comp_scanners(s1,rs[i])
        if r != None:
            dx,dy,dz = r
            return i,dx,dy,dz

def transform(s,r,dx,dy,dz):
    res = []
    for p in s:
        x,y,z=rotate(p)[r]
        res.append((x+dx,y+dy,z+dz))
    return res

scanners = []
scanid = -1
for l in data:
    if l == "": pass
    elif l[0:3] == '---':
        scanners.append([])
        scanid += 1
    else:
        x,y,z = map(int,l.split(','))
        scanners[scanid].append((x,y,z))

print(len(scanners))

corrected = [ scanners[0] ]
remaining = scanners[1:]
pos = [(0,0,0)]
while remaining:
    #print("-----------")
    #print(corrected)
    #print(remaining)
    found=[]
    r = None
    for i in range(len(remaining)):
        for j in corrected:
            r = comp_rotated_scanners(j,remaining[i])
            if r != None:
                found.append(i)
                print(i,r)
                s = transform(remaining[i],*r)
                corrected.insert(0,s)
                r,x,y,z=r
                pos.append((x,y,z))
                break
    assert found != []
    for i in reversed(found): remaining.pop(i)

points = []
for s in corrected:
    for p in s:
        if not p in points: points.append(p)

print(len(points))

print(pos)

def dist(p1,p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return abs(x1-x2)+abs(y1-y2)+abs(z1-z2)

dmax=0
for i in range(len(pos)-1):
    for j in range(i+1,len(pos)):
        d = dist(pos[i],pos[j])
        if d > dmax: dmax = d
print(dmax)
