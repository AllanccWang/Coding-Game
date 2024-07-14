#https://www.codingame.com/training/medium/ways-to-make-change
#WAYS TO MAKE CHANGE
import sys
import math

n=int(input())
s=int(input())
a=[int(i) for i in input().split()]
table=[0 for k in range(n+1)]
table[0]=1
for i in range(0,s):
    for j in range(a[i],n+1):
        table[j]+=table[j-a[i]]
print(table[-1])
