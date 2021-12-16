#!/usr/bin/env python3

from common import *
from collections import defaultdict

data = read_input(16)

def parse_packet(s):
    version = int(s[0:3],2)
    typeid = int(s[3:6],2)
    if typeid==4:
        pos=6
        fin=False
        l = 0
        while not fin:
            if s[pos]=="0": fin=True
            l = l*16 + int(s[pos+1:pos+5],2)
            pos += 5
        return (version,typeid,l,pos)
    else:
        l =[]
        if s[6]=="0":
            length = int(s[7:22],2)
            fin = False
            pos = 22
            while not fin:
                packet = parse_packet(s[pos:])
                l.append(packet)
                pos += packet[3]
                length -= packet[3]
                assert length >= 0
                if length == 0: fin = True
        else:
            number = int(s[7:18],2)
            pos = 18
            for _ in range(number):
                packet = parse_packet(s[pos:])
                l.append(packet)
                pos += packet[3]
        return (version,typeid,l,pos)

def parse_hex(p):
    s=bin(int(p,16))[2:]
    while len(s)<4*len(p): s = "0"+s
    return parse_packet(s)

def product(l):
    p=1
    for i in l: p*=i
    return p
def greater(l):
    if l[0]>l[1]: return 1
    return 0
def lessthan(l):
    if l[0]<l[1]: return 1
    return 0
def equals(l):
    if l[0]==l[1]: return 1
    return 0
    
def analyze(p):
    version,typeid,value,length = p
    if typeid==4: return value
    values = list(map(analyze,value))
    if typeid==0: return sum(values)
    if typeid==1: return product(values)
    if typeid==2: return min(values)
    if typeid==3: return max(values)
    assert len(values)==2
    if typeid==5: return greater(values)
    if typeid==6: return lessthan(values)
    if typeid==7: return equals(values)

print(analyze(parse_hex(data[0])))
