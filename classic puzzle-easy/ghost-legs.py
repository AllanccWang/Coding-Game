#https://www.codingame.com/ide/puzzle/ghost-legs
import sys
import math

w,h=[int(i) for i in input().split()]

line=[input() for i in range(h)]
a=line[0].split()
b=line[-1].split()

for i in range(h-2,0,-1):
    k=line[i][1:-1].split("|")
    for x in range(len(k)):
        if k[x]=="--":
            temp=b[x]
            b[x]=b[x+1]
            b[x+1]=temp

for i in range(len(a)):
    print(f"{a[i]}{b[i]}")
