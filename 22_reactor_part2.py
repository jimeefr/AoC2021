#!/usr/bin/env python3

from common import *
import re

data = read_input(22)

reg = re.compile(r"^(on|off) x=([-0-9]*)..([-0-9]*),y=([-0-9]*)..([-0-9]*),z=([-0-9]*)..([-0-9]*)$")

blocs = []
for line in data:
    m = reg.match(line)
    g = m.group(1,2,3,4,5,6,7)
    x1,x2,y1,y2,z1,z2 = map(int,g[1:])
    state = g[0]
    blocs.append((state,(x1,x2,y1,y2,z1,z2)))

# Séparer 2 intervalles en 3 zones (ou moins)
def cunion(c1,C1,c2,C2):
    if c1 > c2: return cunion(c2,C2,c1,C1)
    if c2 > C1: return [(c1,C1),(c2,C2)]
    _,i,I,_ = sorted([c1,C1,c2,C2])
    r = [(i,I)]
    if c1 < i: r.append((c1,i-1))
    if C2 > I: r.append((I+1,C2))
    if C1 > I: r.append((I+1,C1))
    return r

def inter(b1,b2):
    x1,X1,y1,Y1,z1,Z1 = b1
    x2,X2,y2,Y2,z2,Z2 = b2
    if X1<x2 or X2<x1 or Y1<y2 or Y2<y1 or Z1<z2 or Z2<z1: return [ ]
    _,x,X,_ = sorted([x1,X1,x2,X2])
    _,y,Y,_ = sorted([y1,Y1,y2,Y2])
    _,z,Z,_ = sorted([z1,Z1,z2,Z2])
    return [ (x,X,y,Y,z,Z) ]

def union(b1,b2):
    i = inter(b1,b2)
    if i == [ b1 ]: return [ b2 ]
    if i == [ b2 ]: return [ b1 ]
    if i == [ ]: return [ b1,b2 ]
    x1,X1,y1,Y1,z1,Z1 = b1
    x2,X2,y2,Y2,z2,Z2 = b2
    u = []
    for x,X in cunion(x1,X1,x2,X2):         # On a jusqu'à 27 zones
        for y,Y in cunion(y1,Y1,y2,Y2):     # à tester. Si elles font
            for z,Z in cunion(z1,Z1,z2,Z2): # partie d'un des deux
                b = (x,X,y,Y,z,Z)           # blocs, on les sélectionne
                u1 = inter(b,b1)
                u2 = inter(b,b2)
                if u1 != [] or u2 != []: u.append(b)
    return u

def crop(b1,b2):
    bu = union(b1,b2)
    c = []
    for b in bu:
        bi = inter(b,b2)
        if bi == []: c.append(b)
    return c

def taille(b):
    x,X,y,Y,z,Z = b
    return (1+X-x)*(1+Y-y)*(1+Z-z)

total = [ blocs[0][1] ]
for s,b in blocs[1:]:
    #print(len(total),s,b)
    newtot = []
    for bb in total: newtot += crop(bb,b)
    if s == 'on': newtot += [b]
    total = newtot
tailletotale=0
for b in total: tailletotale += taille(b)
print(len(total))
print(tailletotale)
