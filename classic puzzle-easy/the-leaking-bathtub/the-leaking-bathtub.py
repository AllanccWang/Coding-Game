#https://www.codingame.com/training/easy/the-leaking-bathtub
#The leaking bathtub
import sys
import math

s=int(input()) #the surface area of the bathtub in cm2
h=int(input()) #the height of the bathtub in cm
flow=int(input()) #the tap water flow in cm3/sec
n=int(input()) #the number of leaks
a=[] #flow
if n==0:
    sec=h*s*60/(flow*1000)
else:
    for i in range(n):
        x,y=[int(j) for j in input().split()]
        flag=1
        for j in range(len(a)):
            if a[j][0]==x:
                a[j][1]+=y
                flag=0
        if flag:
            a+=[[x,y]]
    a=sorted(a,key=lambda x:x[0])
    f=[]
    i=0
    sec=0
    if a[0][0]==0:
        f=[[0,flow-a[0][1]]]
        i+=1
    else:
        f=[[0,flow]]
    while i<len(a):
        f+=[[a[i][0],f[-1][1]-a[i][1]]]
        if f[-1][1]<=0:
            print(f"Impossible, {a[i][0]} cm.")
            exit()
        i+=1
    f+=[[h,f[-1][1]]]
    for i in range(1,len(f)):
        sec+=(f[i][0]-f[i-1][0])*s*60/(f[i-1][1]*1000)
        #print(f[i][0],f[i-1][0],f[i-1][1])
sec=int(sec)
m=sec//60
sec%=60
h=m//60
m%=60
print(f"{h:02d}:{m:02d}:{sec:02d}")
