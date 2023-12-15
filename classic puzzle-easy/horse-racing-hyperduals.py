import sys
import math

def cal_dis(v1,e1,v2,e2):
    return abs(v2-v1)+abs(e2-e1)

n=int(input())
a=[]
for i in range(n):
    v, e = [int(j) for j in input().split()]
    a+=[[v,e]]

ans=10**9
for i in range(0,n):
    for j in range(i+1,n):
        ans=min(cal_dis(a[i][0],a[i][1],a[j][0],a[j][1]),ans)
print(ans)
