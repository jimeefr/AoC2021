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

X,Y=0,0
for x,y in points:
	X=max(x,X)
	Y=max(y,Y)
for y in range(Y+1):
	s=""
	for x in range(X+1):
		if [x,y] in points: s += "#"
		else: s += "."
	print(s)
