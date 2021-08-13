# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 13:40:19 2021

@author: dg
"""

'공통문제 LuckyStraight'
N = list(map(int,list(str(input()))))
num = int(len(N)/2)
if sum(N[:num]) == sum(N[num:]): print("LUCKY")
else : print("READY")