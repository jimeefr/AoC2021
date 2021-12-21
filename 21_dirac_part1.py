#!/usr/bin/env python3

from common import *

data = read_input(21)

D=0
Dc = 0
def dice():
    global D,Dc
    Dc += 1
    D += 1
    if D==101: D=1
    return D
def d3():
    return dice()+dice()+dice()
track=[10,1,2,3,4,5,6,7,8,9,10]

def play(pos,score,n):
    pos += d3()
    score += track[pos%10]
    return pos,score,n+3
P = []
P.append((int(data[0][-2:]),0,0))
P.append((int(data[1][-2:]),0,0))

i=0
while True:
    P[i] = play(*P[i])
    if P[i][1] >= 1000: break
    i = (i+1)%2

i = (i+1)%2
print(P,i)
print(P[i][1]*(P[0][2]+P[1][2]))
