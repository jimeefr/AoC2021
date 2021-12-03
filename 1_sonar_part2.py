#!/usr/bin/env python3

from common import read_input

incr=0
depths=read_input(1)
l = len(depths)

depths = [int(d) for d in depths]
for i in range(l-3):
    if depths[i+3] > depths[i]: incr += 1

print(incr)
