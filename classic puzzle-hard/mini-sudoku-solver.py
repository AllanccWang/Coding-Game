#https://www.codingame.com/training/hard/mini-sudoku-solver
#MINI SUDOKU SOLVER
import math
M=4

#determine if a number is already in 2*2, column or row
def solve(grid,row,col,num):
    for x in range(4):
        if grid[row][x]==num:return False
    for x in range(4):
        if grid[x][col]==num:return False

    sR=row-row%2
    sC=col-col%2
    for i in range(2):
        for j in range(2):
            if grid[i+sR][j+sC]==num:
                return False
    return True
    
#dfs go through each empty "0" cell
def Suduko(grid,row,col):
    if (row==M-1 and col==M):
        return True
    if col==M:
        row+=1
        col=0
    if grid[row][col]>0:
        return Suduko(grid,row,col+1)
    for num in range(1,M+1,1):
        if solve(grid,row,col,num):
            grid[row][col]=num
            if Suduko(grid,row,col+1):
                return True
        grid[row][col]=0
    return False
sudo=[]
for i in range(4):sudo+=[[int(x) for x in input()]]
Suduko(sudo,0,0)

for i in range(M):
    s="".join([str(sudo[i][j])for j in range(M)])
    print(s)
