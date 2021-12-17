#!/usr/bin/env python3

from common import *
from collections import defaultdict

data = read_input(17)

data=data[0].split(',')
targetx = list(map(int,data[0].split('=')[1].split('..')))
targety = list(map(int,data[1].split('=')[1].split('..')))

print(targetx,targety)

vy=-targety[0]-1
print(vy)

print((vy*(vy+1))//2)
