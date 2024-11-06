#https://www.codingame.com/training/medium/dominoes-path
import sys
import math

link=[]
def dominoCheck(curr):
    global link    
    for i in range(len(link)):
        try:
            di=link[i] #i-th domino
        except:
            return
        if curr[0]==di[0] or curr[0]==di[1] or curr[1]==di[0] or curr[1]==di[1]:
            curr=di
            link=link[0:i]+link[i+1:]
            dominoCheck(curr)

n = int(input())
for i in range(n):
    a,b=[int(j) for j in input().split()]
    link+=[[a,b]]

curr=link[0]
link=link[1:]
dominoCheck(curr)
if len(link)==0:
    print("true")
else:
    print("false")
