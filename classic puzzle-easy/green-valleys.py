#https://www.codingame.com/training/medium/green-valleys
#concept: DFS
import sys
import math

h=int(input())
n=int(input())
grid=[[0 for i in range(n)] for j in range(n)]
visit=[[0 for i in range(n)] for j in range(n)]

#DFS:went through grid to finnd valley
def check(i,j,cur):
    if i<0 or i>n-1 or j<0 or j>n-1: return
    if visit[i][j]==0:
        visit[i][j]=1
        if grid[i][j]<=h:
            cur[0]+=1
            #print(cur)
            cur[1]=min(cur[1],grid[i][j])
            check(i+1,j,cur)
            check(i-1,j,cur)
            check(i,j+1,cur)
            check(i,j-1,cur)

for i in range(n):
    col=0
    for j in input().split():
        grid[i][col]=int(j)
        col+=1

res=[0,0] #answer

for i in range(n):
    for j in range(n):
        if grid[i][j]<=h and visit[i][j]==0:
            cur=[0,h]
            check(i,j,cur)
            #print("results::",cur,res)
            if cur[0]>res[0]: res=cur
            elif cur[0]==res[0]:
                if cur[1]<res[1]:
                    res[1]=cur[1]

print(res[1])
