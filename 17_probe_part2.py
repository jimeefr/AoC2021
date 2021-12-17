#!/usr/bin/env python3

from common import *
from collections import defaultdict
from math import sqrt

data = read_input(17)

data=data[0].split(',')
targetx = list(map(int,data[0].split('=')[1].split('..')))
targety = list(map(int,data[1].split('=')[1].split('..')))

def vcheck(vx,vy):
    x,y=0,0
    while y >= targety[0] and x <= targetx[1]:
        x += vx
        y += vy
        if vx: vx -= 1
        vy -= 1
        if targetx[0]<=x<=targetx[1] and targety[0]<=y<=targety[1]: return True
    return False

count=0
for vy in range(-targety[0]-1,targety[0]-1,-1):
    s=""
    for vx in range(int(sqrt(targetx[0]*2))+1,targetx[1]+1):
        if vcheck(vx,vy):
            s += "X"
            count+=1
        else: s += "."
    print(s)
print(count)
