#!/usr/bin/env python3

from common import *
import heapq

data = read_input(23)

A = [data[2][3],data[3][3]]
B = [data[2][5],data[3][5]]
C = [data[2][7],data[3][7]]
D = [data[2][9],data[3][9]]
rooms = [A,B,C,D]
halls = ['','','','','','','']

fpod = { 'A':1,'B':10,'C':100,'D':1000 }

def leave(rooms,halls,room,hall):
    halls = halls[::]
    rooms = [ r[::] for r in rooms ]
    if rooms[room] == []: return False,None,None,None
    pod = rooms[room].pop(0)
    if room == ord(pod)-ord('A'):
        if len(rooms[room]) == 0 or rooms[room][0] == pod:
            return False,None,None,None
    cost = 0
    if hall in [0,6]: cost -= 1
    if len(rooms[room]) == 0: cost += 1
    if hall <= room+1: p1,p2=hall,room+2
    else: p1,p2=room+2,hall+1
    for pos in range(p1,p2):
        if halls[pos] != '': return False,None,None,None
        cost += 2
    halls[hall]=pod
    cost *= fpod[pod]
    return True,rooms,halls,cost

def enter(rooms,halls,room,hall):
    halls = halls[::]
    rooms = [ r[::] for r in rooms ]
    if halls[hall] == '': return False,None,None,None
    if len(rooms[room])==2: return False,None,None,None
    pod = halls[hall]
    if room != ord(pod)-ord('A'): return False,None,None,None
    if len(rooms[room])==1 and rooms[room][0] != pod: return False,None,None,None
    cost = 2
    if hall in [0,6]: cost -= 1
    if len(rooms[room]) == 0: cost += 1
    if hall <= room+1: p1,p2=hall+1,room+2
    else: p1,p2=room+2,hall
    for pos in range(p1,p2):
        if halls[pos] != '': return False,None,None,None
        cost += 2
    halls[hall]=''
    rooms[room].insert(0,pod)
    cost *= fpod[pod]
    return True,rooms,halls,cost

def show(rooms,halls,moves,cost):
    s = " "
    for r in rooms:
        for i in range(2):
            if i < len(r): s+=r[i]
            else: s += '.'
        s += " "
    for h in halls:
        if h!= '': s += h
        else: s += '.'
    print(s,cost,moves)

checked = {}
def check(rooms,halls,moves=[],c=0):
    #show(rooms,halls,moves,c)
    if rooms == [ ['A','A'],['B','B'],['C','C'],['D','D'] ]: return True,0
    index = str((rooms,halls))
    if index in checked: return checked[index]
    bestcost = 100000
    found = False
    for e in True,False:
        for r in range(4):
            for h in range(7):
                if e: can,rr,hh,cost = enter(rooms,halls,r,h)
                else: can,rr,hh,cost = leave(rooms,halls,r,h)
                if can:
                    ok,co = check(rr,hh,moves+[(e,r,h)],cost+c)
                    cost += co
                    if ok and cost < bestcost:
                        bestcost = cost
                        found = True
                if e and found: break
            if e and found: break
        if e and found: break
    checked[index] = (found,bestcost)
    return found,bestcost

print(check(rooms,halls))
