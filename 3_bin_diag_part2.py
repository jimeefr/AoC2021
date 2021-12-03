#!/usr/bin/env python3

from common import read_input

diags=read_input(3)

l = len(diags)
dl = len(diags[0])

print(l,dl)

oxy = lambda b0,b1 : b1 if len(b1)>=len(b0) else b0
co2 = lambda b0,b1 : b0 if len(b0)<=len(b1) else b1

def sel(diags,f):
    b = 0
    while len(diags) > 1:
        b0 = [d for d in diags if d[b]=='0']
        b1 = [d for d in diags if d[b]=='1']
        diags = f(b0,b1)
        b+=1
    return int(diags[0],2)

o,c = sel(diags[::],oxy),sel(diags[::],co2)
print(o,c)
print(o*c)