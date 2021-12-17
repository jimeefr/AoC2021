#!/usr/bin/env python3

from common import *
from collections import defaultdict

data = read_input(17)

data=data[0].split(',')
targetx = list(map(int,data[0].split('=')[1].split('..')))
targety = list(map(int,data[1].split('=')[1].split('..')))

print(targetx,targety)

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
for vx in range(targetx[1]+1):
    for vy in range(targety[0]-1,-targety[0]+1):
        if vcheck(vx,vy): count+=1
print(count)
