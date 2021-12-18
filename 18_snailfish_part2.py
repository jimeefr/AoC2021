#!/usr/bin/env python3

from common import *

data = read_input(18)

def myrepr(number):
    if isinstance(number,int): return str(number)
    left,right = number
    return '['+myrepr(left)+','+myrepr(right)+']'

def myread(s):
    pos=0
    if s[0] != '[':
        n=0
        while s[pos] in "0123456789": pos+=1
        return int(s[:pos]),pos
    else:
        assert s[pos]=='['
        pos += 1
        left,l = myread(s[pos:])
        pos += l
        assert s[pos]==','
        pos += 1
        right,l = myread(s[pos:])
        pos += l
        assert s[pos]==']'
        pos += 1
        return [left,right],pos

def change(n,pos,value):
    if len(pos)==1: 
        old = n[pos[0]]
        n[pos[0]]=value
        return old
    else: return change(n[pos[0]],pos[1:],value)

def explode(number):

    def seek_exploding(n,pos=[],exploded=None,prv=None,nxt=None):
        if isinstance(n,int):
            if exploded!=None and nxt==None: nxt=pos
            elif exploded==None: prv=pos
        else:
            if exploded==None and isinstance(n[0],int) and isinstance(n[1],int) and len(pos) >= 4:
                exploded = pos
            else:
                exploded,prv,nxt = seek_exploding(n[0],pos+[0],exploded,prv,nxt)
                exploded,prv,nxt = seek_exploding(n[1],pos+[1],exploded,prv,nxt)
        return exploded,prv,nxt

    exploded,prv,nxt = seek_exploding(number)
    if exploded != None:
        left,right = change(number,exploded,0)
        if prv:
            old=change(number,prv,0)
            change(number,prv,old+left)
        if nxt:
            old=change(number,nxt,0)
            change(number,nxt,old+right)
        return True
    return False

def split(number):
    
    def seek_splitting(n,pos=[]):
        if isinstance(n,int):
            if n >= 10: return pos
            return None
        else:
            splitted = seek_splitting(n[0],pos+[0])
            if splitted != None: return splitted
            return seek_splitting(n[1],pos+[1])

    pos = seek_splitting(number)
    if pos != None:
        old = change(number,pos,0)
        left = old // 2
        right = old-left
        change(number,pos,[left,right])
        return True
    return False

def red(number):
    test=True
    while test:
        while explode(number): pass
        test = split(number)
    return number

def copy(n):
    if isinstance(n,int): return n
    return [copy(n[0]),copy(n[1])]

def magnitude(number):
    if isinstance(number,int): return number
    else: return 3*magnitude(number[0]) + 2*magnitude(number[1])


def add(n1,n2): return red([n1,n2])

numbers = list(map(lambda x:myread(x)[0],data))

max_m = 0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            m = magnitude(add(copy(numbers[i]),copy(numbers[j])))
            if m > max_m: max_m=m
print(max_m)

