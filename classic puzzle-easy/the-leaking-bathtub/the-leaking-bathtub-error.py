#https://www.codingame.com/training/easy/the-leaking-bathtub
#THE LEAKING BATHTUB
import math
import sys
s=int(input()) #the surface area of the bathtub in cm2
h=int(input()) #the height of the bathtub in cm
flow=int(input())*16.6667 #the tap water flow in cm3/sec
n=int(input()) #the number of leaks
a=[] #leak height
if n==0:
    sec=h*s/flow
else:
    for i in range(n):
        x,y=[int(j) for j in input().split()]
        f=1
        for j in range(len(a)):
            if a[j][0]==x:
                a[j][1]+=y*16.6667
                f=0
        if f:
            a+=[[x,y*16.6667]]
    a=sorted(a,key=lambda x:x[0])
    contain=a[0][0]*s
    sec=contain/flow
    t=[contain]
    #ERROR::Times out even wo the while-loop
    while 1:
        sec+=1
        contain+=flow
        l=contain/s
        if l>=h:break
        if l>=a[0][0]:
            for i in range(len(a)):
                if a[i][0]<l:
                    contain-=a[i][1]
        if max(t)>contain:
            print(f"Impossible, {round(contain/s)} cm.")
            exit()
        t+=[contain]
sec=round(sec)
m=sec//60
sec%=60
h=m//60
m%=60
print(f"{h:02d}:{m:02d}:{sec:02d}")
