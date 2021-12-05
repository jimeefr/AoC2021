#!/usr/bin/env python3

from common import read_input
import sys

data = read_input(4)

numbers = [int(s) for s in data[0].split(',')]

grids = []
print(len(data))
l = (len(data)-1)//6
for i in range(l):
    g=[]
    for j in range(5):
        d=data[6*i+j+2]
        g.append([int(s) for s in d.split()])
    print(g)
    grids.append(g)

def check(g):
    for r in g:
        if sum(r)==0: return True
    for c in range(5):
        if sum([r[c] for r in g])==0: return True
    return False

def mark(g,n):
    for r in range(5):
        for c in range(5):
            if g[r][c] == n: g[r][c]=0
    w = check(g)
    return w,n*sum([sum(r) for r in g]),g

for n in numbers:
    ngrids = []
    for g in grids:
        w,s,gg = mark(g,n)
        if w:
            if len(grids)==1:
                print(s)
                sys.exit(0)
        else: ngrids.append(gg)
    grids = ngrids[::]

print("pas de gagnant")
