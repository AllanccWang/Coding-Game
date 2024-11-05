#https://www.codingame.com/training/medium/dominoes-path
#below program checks if the elements are in one group, not determines if it's constructed by single path

import sys
import math

g=[x for x in range(7)]
mergeNb=0

def findGroup(x):
    while x!=g[x]: 
        x=g[x]
    return x

def mergeGroup(x,y):
    global mergeNb
    x=findGroup(x)
    y=findGroup(y)
    if x==y: return
    mergeNb-=1
    g[y]=x

n = int(input())
domino=set()
for i in range(n):
    a,b=[int(j) for j in input().split()]
    domino.add(a)
    domino.add(b)
    mergeGroup(a,b)
    #print(domino)

if len(domino)+mergeNb>1:
    print("false")
else:
    print("true")
