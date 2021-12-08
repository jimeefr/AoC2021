#!/usr/bin/env python3

from common import read_input

data = read_input(8)
count = 0
for line in data:
    seq,val = line.split(' | ')
    val = val.split(' ')
    for v in val:
        if len(v) in [2,3,4,7]: count += 1
print(count)
