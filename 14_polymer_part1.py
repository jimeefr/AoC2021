#!/usr/bin/env python3

from common import *
from collections import defaultdict

data = read_input(14)

s = data[0]

rep = {}
for l in data[2:]:
    s1,s2 = l.split(' -> ')
    s2 = s1[0]+s2
    rep[s1]=s2

for step in range(10):
    ss = ""
    for i in range(1,len(s)):
        if s[i-1:i+1] in rep: ss += rep[s[i-1:i+1]]
        else: ss += s[i-1:i+1]
    s=ss+s[-1]

count=defaultdict(int)
for c in s: count[c] += 1
count = list(count.values())
count.sort()
print(count[-1]-count[0])
