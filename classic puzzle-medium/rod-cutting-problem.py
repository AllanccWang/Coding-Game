#https://www.codingame.com/training/medium/rod-cutting-problem
#concept: Memoization / Dynamic programming
import sys
import math

l=int(input())
n=int(input())
rods=[]

def getAnswer(l,rods):
    #items[0]: length and items[1]:value
    sums=[0 for i in range(l+1)]
    for items in rods:
        for j in range(1,l+1):
            if j-items[0]>=0:
                sums[j]=max(sums[j],sums[j-items[0]]+items[1])
    return sums[l]

for i in range(n):
    ln,val=[int(j) for j in input().split()]
    rods.append([ln,val])

print(getAnswer(l,rods))
