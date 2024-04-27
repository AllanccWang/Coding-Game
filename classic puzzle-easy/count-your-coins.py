#https://www.codingame.com/training/easy/count-your-coins
#concept: Arrays / Mathematics
import sys
import math

reach=int(input())
n=int(input())
data=[[0,0] for i in range(0,n)]
idx=0
for num in input().split():
    data[idx][0]=int(num) #number of coins
    idx+=1
idx=0
for val in input().split():
    data[idx][1]=int(val) #number of values
    idx+=1
data.sort(key=lambda x:x[1])
#print(data)
idx=0
ret=0

while reach>0 and idx<n:
    reach-=data[idx][0]*data[idx][1]
    if reach<=0:
        ret+=data[idx][0]-abs(reach)//data[idx][1]
    else:
        ret+=data[idx][0]
    idx+=1

print([ret,-1][reach>0])
