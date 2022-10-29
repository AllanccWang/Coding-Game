#https://www.codingame.com/training/easy/logically-reasonable-inequalities
#LOGICALLY REASONABLE INEQUALITIES
import sys
import math
a=[]
n = int(input())
for i in range(n):
    row = input().split(" > ")
    
    if row[0] not in a and row[1] not in a:
        a.append(row[0])
        a.append(row[1])
    elif row[0] in a and row[1] not in a:
        k=a.index(row[0])
        a.insert(k+1,row[1])
    elif row[1] in a and row[0] not in a:
        t=a.index(row[1])
        a.insert(t+1,row[0])
    elif row[1] in a and row[0] in a:
        k=a.index(row[0])
        t=a.index(row[1])
        if k>t:
            print("contradiction")
            exit()
    #print(*a)
print("consistent")
