#!/usr/bin/env python3

from common import read_input

def res(seq,val):
    x = {}
    seq=[ "".join(s) for s in map(sorted,seq) ]
    for s in seq:
        if len(s) == 2: x[s],y1=1,s
        if len(s) == 3: x[s],y7=7,s
        if len(s) == 4: x[s],y4=4,s
        if len(s) == 7: x[s],y8=8,s
    for i in y7:
        if not i in y1: a=i
    c5={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
    c6={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
    n5 = [ s for s in seq if len(s)==5 ]
    n6 = [ s for s in seq if len(s)==6 ]
    for i in "abcdefg":
        for j in n5:
            if i in j: c5[i]+=1
        for j in n6:
            if i in j: c6[i]+=1
    for i,j in c6.items():
        if j==2:
            if i not in y4: e=i
            else:
                if i in y1: c=i
                else: d=i
    for i,j in c5.items():
        if j==1 and i!=e: b=i
        if j==2 and i!=c: f=i
        if j==3 and i!=a and i!=d: g=i
    x["".join(sorted(a+b+c+e+f+g))]=0
    x["".join(sorted(a+c+d+e+g))]=2
    x["".join(sorted(a+c+d+f+g))]=3
    x["".join(sorted(a+b+d+f+g))]=5
    x["".join(sorted(a+b+d+e+f+g))]=6
    x["".join(sorted(a+b+c+d+f+g))]=9

    val=[ "".join(v) for v in map(sorted,val) ]
    r=0
    for v in val: r = r*10 + x[v]
    return r

def valeur(line):
    seq,val = line.split(' | ')
    seq = seq.split(' ')
    val = val.split(' ')
    return res(seq,val)

data = read_input(8)
print(sum(map(valeur,data)))
