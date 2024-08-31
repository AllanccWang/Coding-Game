#https://www.codingame.com/training/medium/langtons-ant
#concept: State machine

import sys
import math

w,h=[int(i) for i in input().split()] #the width and height of the grid
x,y=[int(i) for i in input().split()] #initial coordinates.
facing=[[0,-1],[1,0],[0,1],[-1,0]]

direction=input()
dir_i=0
match direction:
    case 'N': dir_i=0
    case 'E': dir_i = 1
    case 'S': dir_i = 2
    case 'W': dir_i = 3

mapp=[['' for i in range(w)] for j in range(h)]
T=int(input()) #the number of turns
for i in range(h):
    line=input()
    for j in range(w):
        mapp[i][j]=line[j]

for i in range(T):
    symbol=-1
    if mapp[y][x]=='#': symbol=1
    dir_i=(dir_i+4+symbol)%4 #exist in four direction

    if mapp[y][x]=='#': 
        mapp[y][x]='.'
    else: 
        mapp[y][x]='#'
    x += facing[dir_i][0]
    y += facing[dir_i][1]

for i in range(h):
    print(''.join(mapp[i]))
