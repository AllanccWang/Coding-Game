#https://www.codingame.com/training/hard/the-max-surface-box
#THE MAX SURFACE BOX
import sys
import math

n = int(input())
if n==1:print("6 6");exit()
#maximum surface
yy=4*n+2
#minimum surface
z,x,y=-1,-1,-1
xx=yy
for j in range(1,round(n**(1/3))+1):
    t=n
    if t%j==0:
        t//=j;z=j
        for i in range(round(math.sqrt(t))+1,0,-1):
            if t%i==0:
                x=i;y=t//i;break
        xx=min(xx,(x*y+x*z+z*y)*2)
print(f"{int(xx)} {yy:d}")
