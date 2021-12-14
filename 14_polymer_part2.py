#!/usr/bin/env python3

from common import *
from collections import defaultdict

data = read_input(14)

s = data[0]
elementcount = defaultdict(int)
for e in s: elementcount[e]+=1

pairs = [ s[i:i+2] for i in range(len(s)-1) ]
paircounts = defaultdict(int)
for p in pairs: paircounts[p]+=1

rep = {}
for l in data[2:]:
    s1,s2 = l.split(' -> ')
    rep[s1]=s2

for step in range(40):
    np = defaultdict(int)
    for p,c in paircounts.items():
        elementcount[rep[p]]+=c
        np[p[0]+rep[p]]+=c
        np[rep[p]+p[1]]+=c
    paircounts = np

count = list(elementcount.values())
count.sort()
print(count[-1]-count[0])
