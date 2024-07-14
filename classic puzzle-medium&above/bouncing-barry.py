#https://www.codingame.com/training/medium/bouncing-barry
#concept: Ascii Art

'''non optimized the time in Validator Drunk testing'''
import sys
import math

dirs=input().split()
bcs=[int(i) for i in input().split()]
moves=[[0,1],[1,0],[-1,0],[0,-1]] #North/East/West/South

record=[]
pos=[0,0]

for dir in range(0,len(dirs)):
    for i in range(0,bcs[dir]):
        vector=moves["NEWS".index(dirs[dir])]
        pos[0]+=vector[0]
        pos[1]+=vector[1]
    
        if [pos[0],pos[1]] in record: record.remove([pos[0],pos[1]])
        else: record.append([pos[0],pos[1]])
    #print(record)

if len(record)==0:
    print(".")
else:
    #print(record)
    x=sorted(record,key=lambda pos:pos[0])
    y=sorted(record,key=lambda pos:pos[1])
    xMin,xMax=x[0][0],x[-1][0]
    yMin,yMax=y[0][1],y[-1][1]
    #print(xMin,xMax,yMin,yMax)
    
    for i in range(yMax,yMin-1,-1):
        line=""
        for j in range(xMin,xMax+1):
            if [j,i] in record: line+="#"
            else: line+="."
        print(line)
