#!/usr/bin/env python3

from common import read_input

def res(seq,val):
    x = {}
    y = [0]*10
    #print(seq)
    seq=list(map(sorted,seq))
    for s in seq:
        if len(s) == 2: x["".join(s)],y[1]=1,s
        if len(s) == 3: x["".join(s)],y[7]=7,s
        if len(s) == 4: x["".join(s)],y[4]=4,s
        if len(s) == 7: x["".join(s)],y[8]=8,s
    r={}
    for i in y[7]:
        if not i in y[1]: a=i
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
            if i not in y[4]: e=i
            if i in y[4]:
                if i in y[1]: c=i
                else: d=i
    for i,j in c5.items():
        if j==1:
            if i!=e: b=i
        if j==2:
            if i!=c: f=i
        if j==3:
            if i!=a and i!=d: g=i
    #print(a+b+c+d+e+f+g)
    x["".join(sorted(a+b+c+e+f+g))]=0
    x["".join(sorted(a+c+d+e+g))]=2
    x["".join(sorted(a+c+d+f+g))]=3
    x["".join(sorted(a+b+d+f+g))]=5
    x["".join(sorted(a+b+d+e+f+g))]=6
    x["".join(sorted(a+b+c+d+f+g))]=9
    #print(x)

    val=list(map(sorted,val))
    r=0
    for v in val:
        r = r*10 + x["".join(v)]
    return r

data = read_input(8)

count = 0
for line in data:
    seq,val = line.split(' | ')
    seq = seq.split(' ')
    val = val.split(' ')
    count += res(seq,val)
print(count)
