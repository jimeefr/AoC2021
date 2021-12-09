#!/usr/bin/env python3

from common import read_input

data = read_input(9)

data = [ [ int(c) for c in l ] for l in data ]
X,Y=len(data[0]),len(data)

print(X,Y)
count = 0
for y in range(Y):
    for x in range(X):
        v=data[y][x]
        m=True
        if m and x>0 and data[y][x-1] <= v: m=False
        if m and y>0 and data[y-1][x] <= v: m=False
        if m and x<X-1 and data[y][x+1] <= v: m=False
        if m and y<Y-1 and data[y+1][x] <= v: m=False
        if m: count += v + 1

print(count)