#https://www.codingame.com/training/easy/mountain-map
import sys
import math

n=int(input())
hs=[]
maxh=0
for i in input().split():
    height=int(i)
    if height>maxh:
        maxh=height
    hs.append(height)

for hd in range(maxh,0,-1):
    s=""
    for j in range(0,len(hs)):
        h=hs[j]
        if h<hd:
            s+="".rjust(h*2)
        else:
            s+="/".rjust(hd)+"".rjust((h-hd)*2)+"\\".ljust(hd)
    print(s.rstrip())
