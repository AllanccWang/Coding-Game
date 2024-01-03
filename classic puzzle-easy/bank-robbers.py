#https://www.codingame.com/training/easy/bank-robbers
#concept: Loops / Mathematics
import sys
import math

r=int(input())
v=int(input())
val=[]
for i in range(v):
    c,n=[int(j) for j in input().split()]
    time=(10**n)*(5**(c-n))
    val.append(time)
arr=[0 for i in range(r)]
vau_open=0
for i in range(r):
    arr[i]+=val[vau_open]
    vau_open+=1

while vau_open<v:
    arr=sorted(arr)
    arr[0]+=val[vau_open]
    vau_open+=1

print(max(arr))
