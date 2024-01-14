#https://www.codingame.com/training/hard/levenshtein-distance
#concept: dynamic programming
import sys
import math

#dynamic programming
w1 = input()
w2 = input()
grid=[[0 for i in range(len(w1)+1)] for j in range(len(w2)+1)]
for i in range(1,len(w1)+1): grid[0][i]=i
for i in range(1,len(w2)+1): grid[i][0]=i

for i in range(1,len(w1)+1):
    for j in range(1,len(w2)+1):
        cost=1
        if w1[i-1]==w2[j-1]: cost=0
        grid[j][i]=min(cost+grid[j-1][i-1],min(1+grid[j-1][i],1+grid[j][i-1]))

print(grid[len(w2)][len(w1)])
