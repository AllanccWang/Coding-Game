#https://www.codingame.com/training/easy/1000000000d-world
import sys
import math

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

n,m=0,0
ans=0
while n<len(a):
    times = min(a[n],b[m])
    a[n]-=times
    b[m]-=times
    ans += times*a[n+1]*b[m+1]
    if a[n]==0: n+=2
    if b[m]==0: m+=2
print(ans)
