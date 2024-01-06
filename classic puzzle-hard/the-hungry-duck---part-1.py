#https://www.codingame.com/training/hard/the-hungry-duck---part-1
import sys
import math

w,h=[int(i) for i in input().split()]
grid=[[0 for i in range(w+1)] for j in range(h+1)]
ans=[[0 for i in range(w+1)] for j in range(h+1)]

for i in range(h):
    arr=[int(j) for j in input().split()]
    for j in range(w):
        grid[i][j]=arr[j]

for i in range(1,h+1):
    for j in range(1,w+1):
        ans[i][j]=max(ans[i-1][j],ans[i][j-1])+grid[i-1][j-1]

print(ans[h][w])
