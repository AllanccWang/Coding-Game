#https://www.codingame.com/training/medium/robbery-optimisation
#concept: Dynamic programming / Mathematics
import sys
import math

n=int(input())
res=[0 for i in range(105)]
arr=[int(input()) for i in range(n)]

def find_max_value(i):
    if i>=n: return 0
    if res[i]==0:
        r1=arr[i]+find_max_value(i+2)
        r2=find_max_value(i+1)
        res[i]=max(r1,r2)
    return res[i]
  
print(find_max_value(0))
