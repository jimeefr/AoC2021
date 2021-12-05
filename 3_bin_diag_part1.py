#!/usr/bin/env python3

from common import read_input

diags=read_input(3)

l = len(diags)
dl = len(diags[0])

print(l,dl)

p = [0]*dl
for d in diags:
    for i in range(dl):
        if d[i] == "1": p[i]+=1

print(p)
gamma,epsilon = 0,0

for i in p:
    gamma <<= 1
    epsilon <<= 1
    if i > l/2: gamma += 1
    else: epsilon += 1

print(gamma,epsilon)
print(gamma*epsilon)
