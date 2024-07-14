#https://www.codingame.com/training/medium/the-lost-child-episode-1
#THE LOST CHILD.EPISODE-1
import sys
import math
from collections import deque

def shortestPath(grid,mx,my):
    m,n=len(grid),len(grid[0])
    q=deque([(mx,my,1)])
    visted=set()
    dir=[(0,1),(1,0),(0,-1),(-1,0)]
    while q:
        r,c,step=q.popleft()
        if grid[r][c]=="C":return step
        for i,j in dir:
            if 0<=r+i and r+i<m and 0<=c+j and c+j<n and (r+i,c+j) not in visted:
                if grid[r+i][c+j]!="#":
                    q.append((r+i,c+j,step+1))
                    visted.add((r+i,c+j))          
    return -1
mx,my=0,0
a=[]
for i in range(10):
    row = input()
    if 'M' in row:
        mx=i
        my=row.index("M")
    if 'C' in row:
        cx=i
        cy=row.index("C")
    a+=[[x for x in row]]
print(f"{(shortestPath(a,mx,my)-1)*10}km")
