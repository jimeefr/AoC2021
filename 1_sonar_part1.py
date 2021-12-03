#!/usr/bin/env python3

from common import read_input

incr=0
depths=read_input(1)
l = len(depths)

depths = [int(d) for d in depths]
for i in range(l-1):
    if depths[i+1] > depths[i]: incr += 1

print(incr)
