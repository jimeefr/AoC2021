#!/usr/bin/env python3

from common import read_input

position=0
depth=0
aim=0

commands=read_input(2)

for s in commands:
    c,p = s.split()
    p=int(p)
    if c=='forward':
        depth += aim*p
        position += p
    elif c=='down': aim += p
    elif c=='up': aim -= p

print(position,depth)
print(position*depth)
