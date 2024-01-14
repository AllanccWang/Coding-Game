#https://www.codingame.com/training/easy/shadow-casting
#concept: Loops / Ascii Art
import sys
import math

n=int(input())
graph=[[' ' for i in range(100)] for j in range(n+2)]
for i in range(n):
    line=input()
    for j in range(len(line)):
        if not line[j].isspace():
            graph[i][j]=line[j]
            graph[i+1][j+1]='-'
            graph[i+2][j+2]='`'
for l in graph:
    print(''.join(l).rstrip())
