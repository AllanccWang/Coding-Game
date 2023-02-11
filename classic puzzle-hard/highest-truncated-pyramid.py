#https://www.codingame.com/training/hard/highest-truncated-pyramid
#HIGHEST TRUNCATED PYRAMID
import sys
import math

n=int(input())
h,w=-1,-1
for i in range(1,n+1):
    a=i*(i+1)//2
    f=False
    for j in range(0,i+1):
        b=j*(j+1)//2
        if a-b==n:h,w=i,j+1;f=True;break
        if b>a:break
    if f:break
for i in range(w,h+1):
    print(i*"*")
