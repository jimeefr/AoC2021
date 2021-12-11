#!/usr/bin/env python3

from common import read_input

data = read_input(11)

data = [ [ int(c) for c in l ] for l in data ]
X,Y=len(data[0]),len(data)

print(X,Y)

def print_data(d):
    for l in d:
        print("".join(map(str,l)))

def get_flash(d,x,y):
    if x<0 or x >=X or y<0 or y>=Y: return
    if d[y][x] > 0: d[y][x] += 1

def flash(d,x,y):
    get_flash(d,x-1,y-1)
    get_flash(d,x-1,y)
    get_flash(d,x-1,y+1)
    get_flash(d,x,y-1)
    get_flash(d,x,y+1)
    get_flash(d,x+1,y-1)
    get_flash(d,x+1,y)
    get_flash(d,x+1,y+1)

def step(d):
    for y in range(Y):
        for x in range(X):
            d[y][x] += 1
    lookup = True
    flashes = 0
    while lookup:
        lookup = False
        for y in range(Y):
            for x in range(X):
                if d[y][x] > 9:
                    d[y][x] = 0
                    flashes += 1
                    flash(d,x,y)
                    lookup = True
    return flashes

f = 0
for i in range(100): 
    #print(i)
    #print_data(data)
    f += step(data)
print(f)
