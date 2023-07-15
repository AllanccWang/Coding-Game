#https://www.codingame.com/training/easy/the-travelling-salesman-problem
#THE TRAVELLING SALESMAN PROBLEM
#concept: Greedy algorithms/Graphs
import sys
import math

n=int(input())
m=[]
for i in range(n):m+=[[int(j) for j in input().split()]]
l=0
visit=[m[0]]
def distance(xi,yi,x0,y0):
    return ((xi-x0)**2+(yi-y0)**2)**0.5
#LOOP n-cities times to find out the shortest distance (Greedy Algo.)
for i in range(n):
    x0,y0=visit[-1][0],visit[-1][1]
    if i!=n-1:
        dis=10**6
        index=-1
        for j in range(n):
            x,y=m[j][0],m[j][1]
            d=distance(x,y,x0,y0)
            if d<dis and m[j] not in visit:
                dis=d
                index=j
        visit+=[m[index]]
        l+=dis
    #last route will be going back to original point
    else:
        l+=distance(visit[0][0],visit[0][1],x0,y0)
print(round(l))
