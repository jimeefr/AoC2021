#!/usr/bin/env python3

from common import *

data = read_input(20)

tr = data[0]

image = data[2:]

def pix(image,x,y,background='.'):
    h=len(image)
    w=len(image[0])
    if 0<=x<=w-1 and 0<=y<=h-1: return image[y][x]
    return background

def trpix(image,x,y,background):
    h=len(image)
    w=len(image[0])
    i=0
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            i<<=1
            if pix(image,x+dx,y+dy,background) == '#': i+=1
    return tr[i]

def trimg(image,background):
    h=len(image)
    w=len(image[0])

    image2 = []
    count = 0
    for y in range(h+2):
        s=""
        for x in range(w+2):
            p=trpix(image,x-1,y-1,background)
            if p=='#': count += 1
            s+=p
        image2.append(s)
    if tr[0] == '#':
        if background=='.': background='#'
        else: background='.'
    return image2,count,background

background='.'
for i in range(50):
    image,count,background = trimg(image,background)
print(count)
