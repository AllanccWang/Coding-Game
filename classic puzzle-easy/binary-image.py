#https://www.codingame.com/training/easy/binary-image
#concept : array
import sys
import math

h=int(input())
a=[]
for i in range(h):
    row=[int(x) for x in input().split()]
    s=""
    f=True
    for x in row:
        if x==0 and row.index(x)==0:
            f=False
        else:
            if f:
                s+="."*x
                f=False
            else:
                s+="O"*x
                f=True
    a+=[s]
ls=sorted(a,key=lambda x:len(x))
if len(ls[0])!=len(ls[-1]): print("INVALID")
else:
    for line in ls:
        print(line)
