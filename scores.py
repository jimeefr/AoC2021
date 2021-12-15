#!/usr/bin/env python3

import requests,json
from datetime import datetime

from common import *

r = requests.get(f"https://adventofcode.com/{year}/leaderboard/private/view/{scoreboard}.json",cookies={'session':session})
scores = json.loads(r.content.decode())
nmembers = len(scores["members"])

print('+-------+',end='')
members=list(scores["members"].items())
members.sort(key=lambda x:-x[1]['local_score'])
for mi,m in members: print(f" {m['name']:18} {m['local_score']:3} |",end='')
print()
for d in map(str,range(1,26)):
    stars = { '1':[], '2':[] }
    t={ '1':{}, '2':{} }
    ts={ '1':{}, '2':{} }
    sc={ '1':{}, '2':{} }
    for mi,m in members:
        l = m['completion_day_level']
        for p in "12":
            sc[p][mi]=0
            if d in l and p in l[d]: 
                t1 = t[p][mi] = int(l[d][p]['get_star_ts'])
                ts[p][mi] = datetime.fromtimestamp(t1)
                stars[p].append((mi,t1))
            else: ts[p][mi] = "    -  -     :  :  "
    for p in "12":
        if len(stars[p]):
            print(f"| d{int(d):02}p{p} |",end='')
            stars[p].sort(key=lambda x:x[1])
            for i,s in enumerate(stars[p]): sc[p][s[0]] += nmembers-i
            for mi,m in members: print(f" {ts[p][mi]} {sc[p][mi]:2} |",end='')
            print()
