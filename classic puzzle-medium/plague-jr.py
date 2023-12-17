#https://www.codingame.com/training/medium/plague-jr
#concept: tree; graph

import sys
import math
#choose optimal initial node to find the maximum diameter of tree
#pass test cases #1,2, but inefficient for #3,4,5
n=int(input())
g=[[0 for i in range(n+1)] for j in range(n+1)]
distance=0

def DFS(x,px):
    global distance
    h1,h2=0,0
    for y in range(0,n+1):
        if g[x][y]==1 and y!=px:
            h=DFS(y,x)+1
            if h>h1:
                h2=h1
                h1=h
            elif h>h2:
                h2=h
            
    distance=max(distance,h1+h2)
    return h1
for i in range(n):
    a,b=[int(j) for j in input().split()]
    g[a][b]=1
    g[b][a]=1
ans=10**9
for i in range(n):
    ans=min(ans,DFS(i,i))
print(ans)
