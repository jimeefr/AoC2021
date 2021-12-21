#!/usr/bin/env python3

from common import *
from collections import defaultdict

data = read_input(21)

def play(pos,score):
    track = [10,1,2,3,4,5,6,7,8,9]
    u = [ 0,0,0,1,3,6,7,6,3,1,0,0]
    p = []
    for d in range(3,10):
        newpos = (pos + d)%10
        newscore = score + track[newpos]
        p.append((newpos,newscore,u[d]))
    return p

p1 = int(data[0][-1:])
p2 = int(data[1][-1:])

init =((p1,0),(p2,0))
i=0
win = [0,0]
S = defaultdict(int)
S[init]+=1
while S:
    NS = defaultdict(int)
    for p in S:
        u=S[p]
        l = play(*p[i])
        for pp,s,uu in l:
            if s < 21:
                if i%2: np = (p[0],(pp,s))
                else: np = ((pp,s),p[1])
                NS[np]+=u*uu
            else: win[i]+=u*uu
    i = (i+1)%2
    S=NS
print(max(win))
