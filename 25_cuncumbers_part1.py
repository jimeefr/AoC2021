#!/usr/bin/env python3

from common import *

data = read_input(25)
data = [ [ c for c in l ] for l in data ]

def show(Map):
    for l in Map: print(''.join(l))
    print()

def moveeast(Map):
    w,h = len(Map[0]),len(Map)
    moved = False
    newmap = [ ['.']*w for _ in range(h) ]
    for y in range(h):
        for x in range(w):
            if Map[y][x] == '>' and Map[y][(x+1)%w] == '.':
                newmap[y][x] = '.'
                newmap[y][(x+1)%w] = '>'
                moved = True
            elif newmap[y][x]=='.': newmap[y][x] = Map[y][x]
    return moved,newmap

def movesouth(Map):
    w,h = len(Map[0]),len(Map)
    moved = False
    newmap = [ ['.']*w for _ in range(h) ]
    for y in range(h):
        for x in range(w):
            if Map[y][x] == 'v' and Map[(y+1)%h][x] == '.':
                newmap[y][x] = '.'
                newmap[(y+1)%h][x] = 'v'
                moved = True
            elif newmap[y][x]=='.': newmap[y][x] = Map[y][x]
    return moved,newmap

def move(m):
    m1,m = moveeast(m)
    m2,m = movesouth(m)
    return (m1 or m2),m

moved = True
steps = 0
m = data
while moved:
    moved,m = move(m)
    steps += 1
show(m)
print(steps)
