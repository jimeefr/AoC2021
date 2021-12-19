#!/usr/bin/env python3

from common import *

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
    for i in range(len(s2)//2):         # Shitty heuristic *4 optimization
        for h in range(len(s1)//2):
            Dx = s1[h][0] - s2[i][0]
            Dy = s1[h][1] - s2[i][1]
            Dz = s1[h][2] - s2[i][2]
            matches = 0
            for k in range(len(s2)):
                x = s2[k][0] + Dx
                y = s2[k][1] + Dy
                z = s2[k][2] + Dz
                for j in range(len(s1)):
                    if x==s1[j][0] and y==s1[j][1] and z==s1[j][2]:
                        matches += 1
                        if matches == 12: return (Dx,Dy,Dz)
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
                break
    assert found != []
    for i in reversed(found): remaining.pop(i)

points = []
for s in corrected:
    for p in s:
        if not p in points: points.append(p)

print(len(points))
