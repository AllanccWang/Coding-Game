#https://www.codingame.com/training/medium/flood-fill-example
#concept: Flood fill / BFS

import sys
import math

w=int(input())
h=int(input())
end=False
t=1
ID=0
grid=[[' ' for i in range(0,31)] for j in range(0,31)]
tmp=[[' ' for i in range(0,31)] for j in range(0,31)]
time=[[1 for i in range(0,31)] for j in range(0,31)]
id=[[0 for i in range(0,31)] for j in range(0,31)]

def propagate(i,j,c,k):
    global t,end
    if grid[i][j]!="#":
        if time[i][j]==0:
            time[i][j]=t
            id[i][j]=k
            tmp[i][j]=c
            end=False
        elif time[i][j]==t:
            if id[i][j]!=k:
                tmp[i][j]='+'
                id[i][j]=-1
                end=False

def createTemp(w,h):
    for i in range(h):
        for j in range(w):
            tmp[i][j]=grid[i][j]

def updateData(w,h):
    for i in range(h):
        for j in range(w):
            grid[i][j]=tmp[i][j]

def isTroop(c):
    if c!='.' and c!='#':
        return True
    else:
        return False

def diffuse(w,h):
    global t,end
    createTemp(w,h)
    end=True
    t+=1
    for i in range(h):
        for j in range(w):
            c=grid[i][j]
            k=id[i][j]
            if isTroop(c):
                #Propagate North
                if i>0: propagate(i-1,j,c,k)
                #Propagate South
                if i<h-1: propagate(i+1,j,c,k)
                #Propagate West
                if j>0: propagate(i,j-1,c,k)
                #Propagate East
                if j<w-1: propagate(i,j+1,c,k)
    updateData(w,h)

def printState(w,h):
    for i in range(h):
        for j in range(w):
            print(grid[i][j],end='')
        print()

for i in range(h):
    line=input()
    for j in range(0,len(line)):
        grid[i][j]=line[j]
        if line[j]=='.' or line[j]=="#":
            time[i][j]=0
            id[i][j]=0
        else:
            time[i][j]=t
            ID+=1
            id[i][j]=ID
            
while (not end):
    diffuse(w,h)

printState(w,h)
