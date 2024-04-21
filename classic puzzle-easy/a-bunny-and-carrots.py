#https://www.codingame.com/training/easy/a-bunny-and-carrots
#concept: Math
import sys
import math

m,n=[int(i) for i in input().split()]
t=int(input())
d=[0 for i in range(n+3)]
d[0]=m
d[n+1]=m
ret=2*(m+n)
for a in input().split():
    a=int(a)
    d[a]+=1
    ret+=2
    if d[a-1]>=d[a]: ret-=2
    if d[a+1]>=d[a]: ret-=2
    if d[a]==m: ret-=2
    print(ret)
