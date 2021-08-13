# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 13:40:43 2021

@author: dg
"""

'15686 치킨배달'
from itertools import combinations
        
N, M = map(int,input().split())
mapp = []
home = []
chic = []
dist = []
a=[]
vil_dist = []
for i in range(N):
    mapp.append(list(map(int,input().split())))
    home.extend([[i, x] for x, value in enumerate(mapp[i]) if value == 1])
    chic.extend([[i, x] for x, value in enumerate(mapp[i]) if value == 2])
for i in range(len(home)):
    dist.append([abs(home[i][0]-chic[j][0])+abs(home[i][1]-chic[j][1]) for j in range(len(chic))])
for i in range(len(dist)):
    a.append(list(combinations(dist[:][i],M)))
for i in range(len(a[0])):
    x=0
    for j in range(len(a)):
        x+=min(a[j][i])
    vil_dist.append(x)
print(min(vil_dist))
