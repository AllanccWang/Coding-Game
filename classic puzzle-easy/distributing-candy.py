#https://www.codingame.com/training/easy/distributing-candy
import sys
import math

n,m=map(int,input().split())
arr=[int(i) for i in input().split()]
arr.sort()
#print(arr)
ans=1e9
for i in range(0,n-m+1):
    ans=min(ans,arr[i+m-1]-arr[i])
print(ans)
