#!/usr/bin/env python3

from common import read_input

data = read_input(13)

points = []
fold=0
for line in data:
	fold+=1
	if line == "": break
	points.append(list(map(int,line.split(','))))

def folds(X,axe):
	for i in range(len(points)):
		if points[i][axe] > X: points[i][axe] = 2*X-points[i][axe]

for f in data[fold:]:
	if f[11]=='x':axe=0
	else: axe=1
	pos=int(f[13:])
	folds(pos,axe)
	break

print(len(points))
count=0
points2=[]
for p in points: 
	if not p in points2:
		points2.append(p)
		count += 1

print(count)
