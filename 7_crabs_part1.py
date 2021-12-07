#!/usr/bin/env python3

from common import read_input

data = read_input(7)

crabs = list(map(int,data[0].split(",")))
print(len(crabs))
M = max(crabs)
fuels = []
for i in range(M+1): fuels.append(sum(map(lambda x:abs(x-i),crabs)))
print(min(fuels))
