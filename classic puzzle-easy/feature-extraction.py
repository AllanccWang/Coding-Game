#https://www.codingame.com/training/easy/feature-extraction
#FEATURE EXTRACTION
#concept: Dot product
import sys
import math

r,c=[int(i) for i in input().split()]
a,w=[],[]
for i in range(r):
    a+=[[int(j) for j in input().split()]]
m,n=[int(i) for i in input().split()]
for i in range(m):
    w+=[[int(j) for j in input().split()]]

for i in range(0,r-m+1):
    t=[]
    for j in range(0,c-n+1):
        s=0
        for k in range(0,m):
            for l in range(0,n):
                s+=a[i+k][j+l]*w[k][l]
        t+=[s]
    print(*t)
