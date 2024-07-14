#https://www.codingame.com/training/easy/treasure-hunt
#TREASURE HUNT
#concept : DFS
import sys
import math
h,w=[int(i) for i in input().split()]
m=[]
x0,y0=-1,-1
for i in range(h):
    row=input()
    if "X" in row:
        x0,y0=i,row.index("X")
    m+=[[x for x in row]]
visit=[[False for i in range(w)] for j in range(h)]
coins=[[0 for i in range(w)] for j in range(h)]
dir=[[-1,0],[0,1],[0,-1],[1,0]]
max_coins=-1

def DFS(x0,y0):
    visit[x0][y0]=True
    global max_coins
    global coins
    for d in dir:
        x=x0+d[0]
        y=y0+d[1]
        if x>=0 and x<h and y>=0 and y<w and not visit[x][y] and m[x][y]!="#":
            if m[x][y].isdigit():
                coins[x][y]=coins[x0][y0]+int(m[x][y])
            else:
                coins[x][y]=coins[x0][y0]
            max_coins=max(max_coins,coins[x][y])
            DFS(x,y)
            visit[x][y]=False
DFS(x0,y0)
print(max_coins)
