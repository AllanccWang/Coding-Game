#https://www.codingame.com/training/medium/minimal-number-of-swaps
#MINIMAL NUMBER OF SWAPS
import sys
import math

n = int(input())
x=[int(i) for i in input().split()]
a=sorted(x.copy(),reverse=True)
cnt=0
for i in range(n):
    if a[i]!=x[i]:
        cnt+=1
print(cnt//2)
