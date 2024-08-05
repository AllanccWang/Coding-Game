#https://www.codingame.com/training/easy/treasure-hunt
#TREASURE HUNT
#concept: BFS
import sys
import math

#Using BFS method can't pass going-in-circle testcase
h,w=[int(i) for i in input().split()]
m=[]
x0,y0=-1,-1
for i in range(h):
    row=input()
    if "X" in row:
        x0,y0=i,row.index("X")
    m+=[[x for x in row]]

stk=[[x0,y0]]
visit=[[False for i in range(w)] for j in range(h)]
coins=[[0 for i in range(w)] for j in range(h)]
dir=[[-1,0],[0,1],[0,-1],[1,0]]
max_coins=-1
while len(stk)!=0:
    x,y=stk[0][0],stk[0][1]
    stk.pop(0)
    for d in dir:
        xi,yi=x+d[0],y+d[1]
        if xi>=0 and xi<h and yi>=0 and yi<w and not visit[xi][yi] and m[xi][yi]!="#":
            if m[xi][yi].isdigit():
                coins[xi][yi]=coins[x][y]+int(m[xi][yi])
            else:
                coins[xi][yi]=coins[x][y]
            max_coins=max(coins[xi][yi],max_coins)
            visit[xi][yi]=True
            stk.append([xi,yi])
'''
#coin map
#for i in range(h):
#    print(*coins[i])
'''
print(max_coins)
