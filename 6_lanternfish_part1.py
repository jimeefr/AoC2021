#!/usr/bin/env python3

from common import read_input

data = read_input(6)

lifetimes = map(int,data[0].split(","))
days = [0]*9
for i in lifetimes: days[i]+=1

for i in range(80):
    d0 = days.pop(0)
    days[6] += d0
    days.append(d0)
print(sum(days))
