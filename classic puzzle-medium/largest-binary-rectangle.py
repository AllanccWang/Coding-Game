#https://www.codingame.com/training/medium/largest-binary-rectangle
#concept:2D array
import sys
import math

def maxHist(row):
    result=[]
    top_val,max_area,area,i=0,0,0,0
    while i<len(row):
        if len(result)==0 or row[result[-1]]<=row[i]:
            result.append(i)
            i += 1
        else:
            top_val=row[result.pop()]
            area=top_val * i
            if len(result):
                area=top_val*(i-result[-1]-1)
            max_area=max(area,max_area)
    while len(result):
        top_val=row[result.pop()]
        area=top_val * i
        if len(result):
            area=top_val*(i-result[-1]-1)
        max_area=max(area, max_area)
    return max_area

def maxRectangle(A):
    result=maxHist(A[0])
    for i in range(1,len(A)):
        for j in range(len(A[i])):
            if (A[i][j]):
                A[i][j]+=A[i - 1][j]
        result = max(result,maxHist(A[i]))
    return result

w,h=[int(i) for i in input().split()]
A=[[0 for i in range(w)] for j in range(h)]
for i in range(h):
    for j in input().split():
        A[i].append(int(j))
        
print(maxRectangle(A))
