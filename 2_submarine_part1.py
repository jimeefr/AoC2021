#!/usr/bin/env python3

from common import read_input

position=0
depth=0

commands=read_input(2)

for s in commands:
    c,p = s.split()
    p=int(p)
    if c=='forward': position += p
    elif c=='down': depth += p
    elif c=='up': depth -= p

print(position,depth)
print(position*depth)
