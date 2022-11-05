#https://www.codingame.com/training/medium/network-cabling
#network-cabling
import sys
import math

n=int(input())
house=[]
for i in range(n):
    x,y=[int(j) for j in input().split()]
    house.append((x,y))
house.sort(key=lambda x:x[1])
if len(house)==1: print(0);exit()

#Calculate the median y position
mY=house[len(house)//2][1]
if len(house)%2==0:
    mY=(house[len(house)//2-1][1]+mY)//2

#Calculate the length of the main cable
minX,maxX=1e9,-1
for a in house:
    minX=min(minX,a[0])
    maxX=max(maxX,a[0])

#print(minX,maxX,mY)
cable=maxX-minX #x-direction length
for a in house:
    cable+=abs(a[1]-mY)
print(cable)
