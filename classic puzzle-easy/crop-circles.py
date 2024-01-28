#https://www.codingame.com/training/easy/crop-circles
#concept: 2D array / Geometry / Ascii Art
import sys
import math

instructions=input().split()
letters="abcdefghijklmnopqrstuvwxyz"
m=[[True for i in range(0,25)] for j in range(0,25)]
for v in instructions:
    ss=v
    code=0
    if ss.startswith("PLANTMOW"):
        code=2
        ss=ss.replace("PLANTMOW","")
    elif ss.startswith("PLANT"):
        code=1
        ss=ss.replace("PLANT","")
    x=letters.index(ss[0])
    y=letters.index(ss[1])
    r=int(ss[2:])
    #print(x,y,r)
    for i in range(0,19):
        for j in range(0,25):
             if (i-x)**2+(j-y)**2 <= r*r/4:
                if code==0:
                    m[i][j]=False
                elif code==1:
                    m[i][j]=True
                elif code==2:
                    m[i][j]=not m[i][j]
                
for i in range(0,25):
    for j in range(0,19):
        print(["  ","{}"][m[j][i]],end="")
    print()
